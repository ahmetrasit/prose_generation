# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **89:30**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s089-regular-20260912/s089/89_30/micro.discovery.json` and modify nothing
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
  "ayah_ref": "89:30",
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
{"branch_registry":[{"boundary":"Dal yalnızca örtme ve gizlenme alanındadır; akıl yitimi, bahçe ve görünmeyen varlık anlamlarını içermez.","branch_kind":"bare","branch_ref":"root_000266/B001","candidate_links":[{"candidate_id":"cand_8776312a86b2c0b3c773","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:30:2:1","qac_word_ref":"89:30:2","surface_ar":"جَنَّتِ"}],"gloss":"örtme ve duyulardan gizleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey örtülerek ya da gizlenerek duyuların erişiminden çıkarılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir örtünün arkasına saklanma, bir şeyi içinde saklama ve insanı örten giysi aynı gizleme çekirdeğine dayanır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin örtülmesini, bir kişinin saklanmasını veya örtü işlevli bir şeyi birlikte temsil eden en geniş karşılıktır.","boundary_detail":"Dal yalnızca örtme ve gizlenme alanındadır; akıl yitimi, bahçe ve görünmeyen varlık anlamlarını içermez.","branch_image_ar":"الستر والاستتار","concept_gloss":"örtme ve duyulardan gizleme","contextual_glosses":[{"applicability":"Bir öznenin nesneyi görünmez veya algılanamaz duruma getirdiği geçişli kullanımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geçişli örtme eylemini ve bunun doğurduğu gizlenme sonucunu eksiksiz korur."},"facet_ids":["F001"],"text":"örtüp gizlemek","usage_role":"contextual"},{"applicability":"Kişinin bir örtü veya engel aracılığıyla kendini duyulardan sakladığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Örtü aracını ve öznenin kendisini algıdan saklaması anlamını birlikte korur."},"facet_ids":["F002"],"text":"bir şeyin arkasına gizlenmek","usage_role":"contextual"}],"definition":"Bir şeyi duyuların erişiminden çıkaracak biçimde örtmek ya da gizlemek; kişinin bir şeyin arkasına saklanması, bir şeyi içinde saklaması ve insanı örten giysi bu çekirdeğin gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey örtülerek ya da gizlenerek duyuların erişiminden çıkarılır."},{"facet_id":"F002","role":"extension","statement":"Bir örtünün arkasına saklanma, bir şeyi içinde saklama ve insanı örten giysi aynı gizleme çekirdeğine dayanır."}],"identity_rationale":"Kaynak ifadesi dalı örtme, duyulardan gizleme ve bir örtünün arkasına saklanma çekirdeğinde kurar; içte saklama ile insanı örten giysi de bu çekirdeğin açık gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"örtmek; gizleyecek bir örtü sağlamak; içinde saklamak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyin arkasına gizlenmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"insanı örten giysi veya örtü"}],"lexicalization_note":"Tanım yalın dalı kapsar ve başka dallara ya da yalnızca belirli bir söz öbeğine bağlı anlamları içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yakın sınır karşılaştırmasını genel örtme dalı sağladığı için yalnızca bu ayrım yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kurucu sonucu duyusal erişimden gizlenmedir; komşu dal ise genel örtme ve kaplama alanını daha geniş biçimde adlandırır.","focus_only":"Odak dal, duyulardan saklanmayı, içte gizlemeyi ve insanı örten giysiyi aynı çekirdekte toplar.","gloss":"örtme ve gizleme","neighbor_only":"Komşu dal, örtü ve örtme araçlarının genel söz varlığını daha doğrudan kapsar.","neighbor_ref":"root_000674/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi örtme ve böylece görünmesini engelleme alanında buluşur."}],"source_phrase_ar":"الجيم والنون أصل واحد وهو الستر والتستر (maqayis)؛ أصل الجن ستر الشيء عن الحاسة (mufradat)؛ استجن فلان إذا استتر بشيء (ayn;tahdhib)؛ أجننت الشيء في صدري أكننته (sihah)؛ ما علي جنان إلا ما ترى أي ثوب يواريني (sihah;tahdhib)","source_summary":"Kaynakların ortak ekseni, bir şeyi duyusal algıdan örterek gizlemek ve bu örtünün sağladığı saklılık durumudur.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه ستر الشيء عن الحس والاستتار بشيء وإكنان الشيء في الصدر وما يواري من ثوب أو غيره","what_is_not_ar":"ليس الجنون ولا الجنة ولا الجن"},"support_links":["sup_d530d8e3c93ad64186f9"]},{"boundary":"Sırf gece, sırf karanlık veya güneşin batması yeterli değildir; karanlığın bir şeyi örtmesi kurucudur.","branch_kind":"bare","branch_ref":"root_000266/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:30:2:1","qac_word_ref":"89:30:2","surface_ar":"جَنَّتِ"}],"gloss":"gecenin karartıp örtmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gece kararır ve karanlığı bir şeyin üzerini örter."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gece karanlığının bir kişi, yer veya nesneyi kaplayıp görünmez kıldığı bütün yalın kullanımlara uygundur.","boundary_detail":"Sırf gece, sırf karanlık veya güneşin batması yeterli değildir; karanlığın bir şeyi örtmesi kurucudur.","branch_image_ar":"غشيان الليل","concept_gloss":"gecenin karartıp örtmesi","contextual_glosses":[{"applicability":"Bir yerin veya nesnenin gece bastığında karanlık içinde görünmez hale geldiği anlatımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gecenin bastırmasını ve nesnenin karanlıkla örtülmesini birlikte korur."},"facet_ids":["F001"],"text":"gece karanlığına gömülmek","usage_role":"contextual"}],"definition":"Gecenin kararması ve bir şeyi kendi karanlığıyla örterek görünmez kılmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gece kararır ve karanlığı bir şeyin üzerini örter."}],"identity_rationale":"Kaynak ifadesi yalnızca gecenin kararıp bir şeyi karanlığıyla örtmesini bildirir; dalın gece karanlığı ile örtme işlemini birlikte tutan çerçevesi buna uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"gecenin kararıp üzerini örtmesi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"gecenin koyu karanlığı ve nesneleri örtmesi"}],"lexicalization_note":"Tanım yalın dalı verir; başka gece sözlerine veya insan topluluğu ve iç dünya anlamlarına genişletilmez.","neighbor_coverage_note":"Bütün gece, ışık ve aynı kökten gelen dal adayları değerlendirildi; örtme koşulunu en iyi sınayan kararma dalı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu için kararma yeterliyken odak dalda karanlığın bir kişi, yer veya nesneyi örtmesi anlamın kurucu parçasıdır.","focus_only":"Odak dalda gece karanlığı yalnızca artmaz, aynı zamanda bir şeyin üzerini örter.","gloss":"gecenin kararması","neighbor_only":"Komşu dal gecenin karanlık hale gelmesini örtülen bir nesne şartı olmadan kapsar.","neighbor_ref":"root_001094/B001","relation_type":"near_synonym","shared_zone":"İki dal da gecenin karanlıklaşması ve yoğun karanlık alanında örtüşür."}],"source_phrase_ar":"جنان الليل سواده وستره الأشياء (maqayis)؛ أجنه الليل وجن عليه الليل إذا أظلم حتى يستره بظلمته (ayn)؛ جن عليه الليل يجن بالضم جنونا (sihah)؛ جن عليه الليل وأجنه الليل إذا أظلم حتى يستره بظلمته (tahdhib)؛ جنه الليل وأجنه وجن عليه (mufradat)","source_summary":"Kaynaklar gecenin kararmasını, bu karanlığın nesneleri örtüp görünmez kılmasıyla birlikte anlatır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه جن الليل على الشيء إذا أظلم وستره بسواده","what_is_not_ar":"ليس سواد الناس ولا الجنان بمعنى القلب"},"support_links":[]},{"boundary":"Her çevrili alan veya her ekili toprak bu dala girmez; ağaçlı bahçe ve ağaçların örttüğü zemin esastır.","branch_kind":"bare","branch_ref":"root_000266/B003","candidate_links":[{"candidate_id":"cand_2caa272e4a2e2ed43a49","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:30:2:1","qac_word_ref":"89:30:2","surface_ar":"جَنَّتِ"}],"gloss":"zemini ağaçlarla örtülü bahçe","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ağaçlı bahçenin zemini ağaçların oluşturduğu örtü altında kalır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ağaçların veya hurmalıkların yoğunluğu sayesinde zemini örtülen bahçe ve koruluklar için tam karşılıktır.","boundary_detail":"Her çevrili alan veya her ekili toprak bu dala girmez; ağaçlı bahçe ve ağaçların örttüğü zemin esastır.","branch_image_ar":"البستان المستور بالشجر","concept_gloss":"zemini ağaçlarla örtülü bahçe","contextual_glosses":[{"applicability":"Bağlam zeminin ağaçlarla örtülü olduğunu zaten gösterdiğinde doğal ve kısa bir çeviridir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ağaçlarla kaplı bahçe referansını bağlam desteğiyle eksiksiz korur."},"facet_ids":["F001"],"text":"ağaçlık bahçe","usage_role":"contextual"}],"definition":"Ağaçları, özellikle de sık ağaç veya hurmalıkları zemini örten bahçe ya da koruluk niteliğindeki yerdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ağaçlı bahçenin zemini ağaçların oluşturduğu örtü altında kalır."}],"identity_rationale":"Kaynak ifadesi bahçeyi ağaçları veya hurmalıkları toprağı örten ağaçlı bir yer olarak tanımlar; dalın ağaç örtüsünü merkeze alan çerçevesi kaynağa uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"zemini ağaçlarla örtülü bahçe veya koruluk"}],"lexicalization_note":"Tanım yalın ağaçlı bahçe anlamını taşır ve ölüm sonrası ödül yurdu ya da genel bitki örtüsü anlamını içeri almaz.","neighbor_coverage_note":"Bütün bahçe, hurmalık, bitki ve aynı kökten dal adayları değerlendirildi; dış sınır ile ağaç örtüsü karşıtlığı en yararlı ayrımdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta içteki ağaç örtüsü, komşuda ise alanı dıştan kuşatan sınır belirleyicidir; bu yüzden sıradan bağlamda birbirlerinin yerine geçmezler.","focus_only":"Odak dal bahçeyi ağaçların zemini örtmesiyle tanımlar.","gloss":"ağaç örtülü ve çevrili bahçe","neighbor_only":"Komşu dal bahçeyi çevresindeki duvar, engel veya yükseltiyle tanımlar.","neighbor_ref":"root_000300/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da ağaç veya bitki içeren sınırlı bir bahçe alanına gönderimde bulunabilir."}],"source_phrase_ar":"الجنة البستان (maqayis;sihah)؛ الجنة الحديقة وهي بستان ذات شجر ونزهة (ayn)؛ العرب تسمي النخيل جنة (sihah)؛ كل بستان ذي شجر يستر بأشجاره الأرض (mufradat)","source_summary":"Kaynaklar anlamı bahçe, ağaçlı bahçe ve hurmalık çevresinde birleştirir; ayırt edici özellik ağaçların zemini örtmesidir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الجنة بمعنى البستان والحديقة ذات الشجر والنخل الساتر","what_is_not_ar":"ليس الجنة الأخروية ولا الجنون"},"support_links":["sup_e0ec521aea7e8ca54491"]},{"boundary":"Dal ölüm sonrası ödül yurduyla sınırlıdır; dünyadaki ağaçlı bahçe veya görünmeyen varlıklar topluluğu değildir.","branch_kind":"bare","branch_ref":"root_000266/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:30:2:1","qac_word_ref":"89:30:2","surface_ar":"جَنَّتِ"}],"gloss":"ölüm sonrası gizli nimetler yurdu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Müslümanların ölümden sonra varacağı ödül yurdunun nimetleri bugün kendilerinden gizlidir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırma ya dünyadaki ağaçlı bahçeye benzetilmekte ya da nimetlerin şimdilik gizli oluşuyla açıklanmaktadır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Müslümanların ölümden sonra ulaşacağı ödül yurdundan ve henüz görünmeyen nimetlerinden söz edilen bağlamlara uygundur.","boundary_detail":"Dal ölüm sonrası ödül yurduyla sınırlıdır; dünyadaki ağaçlı bahçe veya görünmeyen varlıklar topluluğu değildir.","branch_image_ar":"الجنة الأخروية","concept_gloss":"ölüm sonrası gizli nimetler yurdu","contextual_glosses":[{"applicability":"Nimetlerin henüz görünmediği bilgisi bağlamdan anlaşıldığında akıcı bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölüm sonrası varış yerini ve ödül olma niteliğini bağlam desteğiyle korur."},"facet_ids":["F001"],"text":"ölüm sonrası ödül yurdu","usage_role":"contextual"}],"definition":"Müslümanların ölümden sonra ulaşacağı, ödülü ve nimetleri bugün onlardan gizli olan yurttur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Müslümanların ölümden sonra varacağı ödül yurdunun nimetleri bugün kendilerinden gizlidir."},{"facet_id":"F002","role":"source_variant","statement":"Adlandırma ya dünyadaki ağaçlı bahçeye benzetilmekte ya da nimetlerin şimdilik gizli oluşuyla açıklanmaktadır."}],"identity_rationale":"Kaynak ifadesi Müslümanların ölümden sonra ulaşacağı ödül yurdunu ve bugün onlardan gizli olan nimetlerini bildirir; dünyevi bahçe benzetmesi yalnızca adlandırma açıklamasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ölüm sonrası ödül ve gizli nimetler yurdu"}],"lexicalization_note":"Tanım yalın ölüm sonrası ödül yurdu anlamını korur ve dünyadaki bahçe anlamını bu dala katmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dış adaylar bitki adlarıyla sınırlı kaldığından en açıklayıcı karşılaştırma aynı kökün dünyevi bahçe dalıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Biri ölüm sonrası ve inanç alanına ait bir varış yeridir, diğeri dünyadaki ağaçlı bir alandır; benzetme referansları özdeş kılmaz.","focus_only":"Odak dal ölüm sonrası ulaşılan ödül yurdunu ve bugün gizli olan nimetleri bildirir.","gloss":"ödül yurdu ve ağaçlı bahçe","neighbor_only":"Komşu dal dünyadaki, zemini ağaçlarla örtülü somut bir bahçeyi bildirir.","neighbor_ref":"root_000266/B003","relation_type":"near_neighbor","shared_zone":"Adlandırma, ödül yurdunu ağaçlı bahçe imgesiyle ilişkilendirebilir."}],"source_phrase_ar":"الجنة ما يصير إليه المسلمون في الآخرة وهو ثواب مستور عنهم اليوم (maqayis)؛ سميت الجنة إما تشبيها بالجنة في الأرض وإما لستره نعمها عنا (mufradat)","source_summary":"Kaynaklar ölüm sonrası ödül yurdunda birleşir; adın gerekçesini ağaçlı bahçe benzetmesi veya nimetlerin bugün gizli olmasıyla açıklar.","sources":["MQ","MU"],"what_is_ar":"يدخل فيه الجنة التي يصير إليها المسلمون وثوابها المستور عنهم","what_is_not_ar":"ليس البستان الدنيوي ولا جماعة الجن"},"support_links":[]},{"boundary":"Yılan adı ve akıl yitimi bu dalın dışında kalır; yer anlamı yalnızca çokluk bildiren belirli söz öbeğine bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000266/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:30:2:1","qac_word_ref":"89:30:2","surface_ar":"جَنَّتِ"}],"gloss":"gözle görülmeyen ruhani varlıklar topluluğu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ruhani varlıklar insan gözünden ve duyularından gizlidir; ad hem türü hem topluluğunu karşılayabilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tekil biçim bu varlıkların atasını veya bir bireyini, başka biçimler ise topluluğunu bildirir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu varlıkların çok bulunduğu yer anlamı yalın değildir ve belirli bir yer söz öbeğiyle sınırlıdır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın biçimlerin gizli ruhani varlık türünü veya bu türün topluluğunu bildirdiği genel bağlamlara uygundur.","boundary_detail":"Yılan adı ve akıl yitimi bu dalın dışında kalır; yer anlamı yalnızca çokluk bildiren belirli söz öbeğine bağlıdır.","branch_image_ar":"الجن المستترون","concept_gloss":"gözle görülmeyen ruhani varlıklar topluluğu","contextual_glosses":[{"applicability":"Söz konusu türün tek bir bireyi veya atası anlatıldığında tekil bağlama uyar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Birey olmayı, ruhani niteliği ve insan duyularından gizli oluşu korur."},"facet_ids":["F001","F002"],"text":"görünmeyen ruhani varlık","usage_role":"contextual"},{"applicability":"Yalnızca kanıtta verilen yer söz öbeğinin çokluk bildiren bağımlı kullanımında geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yer referansını, varlıkların çokluğunu ve kullanımın söz öbeğine bağlılığını korur."},"facet_ids":["F003"],"text":"görünmeyen varlıkların çok bulunduğu yer","usage_role":"explanatory"}],"definition":"İnsanların duyularından gizli kabul edilen ruhani varlıklar ve onların topluluğudur. Bu varlıklardan çok bulunan yer anlamı yalnızca ilgili yer söz öbeğine bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ruhani varlıklar insan gözünden ve duyularından gizlidir; ad hem türü hem topluluğunu karşılayabilir."},{"facet_id":"F002","role":"specialization","statement":"Tekil biçim bu varlıkların atasını veya bir bireyini, başka biçimler ise topluluğunu bildirir."},{"facet_id":"F003","role":"extension","statement":"Bu varlıkların çok bulunduğu yer anlamı yalın değildir ve belirli bir yer söz öbeğiyle sınırlıdır."}],"identity_rationale":"Kaynak ifadesi insan gözünden gizli ruhani varlıkları, onların tekil ve topluluk adlarını ve bu varlıkların çok bulunduğu yer için kullanılan bağımlı söz öbeğini birlikte verir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"gözle görülmeyen ruhani varlıklar"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"görünmeyen varlıkların atası veya bir bireyi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"görünmeyen ruhani varlıkların topluluğu"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"görünmeyen ruhani varlıkların çok bulunduğu yer"}],"lexicalization_note":"Yalın varlık ve topluluk anlamları, bu varlıkların çok bulunduğu yeri bildiren söz öbeğine bağlı kullanımdan ayrı tutulur.","neighbor_coverage_note":"Bütün varlık, canlı, yer ve aynı kökten adaylar değerlendirildi; genel tür ile ayrı alt topluluk arasındaki sınır en yararlı ayrımdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak genel tür ve topluluk adıdır; komşu ise aynı alandaki ayrı bir sınıf veya ona bağlı varlıkları bildirir, bu yüzden ikame edilemez.","focus_only":"Odak dal görünmeyen ruhani varlık türünün genel adını, bireyini ve topluluğunu kapsar.","gloss":"görünmeyen varlıklar ve bir alt topluluk","neighbor_only":"Komşu dal bu alandaki ayrı bir topluluğu, alt türü veya onlara bağlanan köpekleri bildirir.","neighbor_ref":"root_000364/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal insan gözünden gizli kabul edilen ruhani varlıklar alanındadır."}],"source_phrase_ar":"الجن سموا بذلك لأنهم متسترون عن أعين الخلق (maqayis)؛ الجن جماعة ولد الجان وجمعهم الجنة والجنان (ayn;tahdhib)؛ الجن خلاف الإنس والواحد جني (sihah)؛ الجنة جماعة الجن (mufradat)؛ أرض مجنة كثيرة الجن (ayn;sihah;tahdhib)","source_summary":"Kaynaklar insan duyularından gizli ruhani varlıklar çekirdeğinde birleşir; birey, ata, topluluk ve çok bulundukları yer için ayrı biçimler verir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الجن والجان والجنة جماعة الجن والموضع الكثير الجن","what_is_not_ar":"ليس الجان بمعنى الحية ولا الجنة بمعنى الجنون"},"support_links":[]},{"boundary":"Dal gerçek ya da gösterilen akıl yitimiyle sınırlıdır; görünmeyen varlıklar ve ağaçlı bahçe anlamları dışarıda kalır.","branch_kind":"bare","branch_ref":"root_000266/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:30:2:1","qac_word_ref":"89:30:2","surface_ar":"جَنَّتِ"}],"gloss":"aklı örten akıl yitimi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Akıl yitimi, aklın örtülmesi veya benlik ile akıl arasına engel girmesi olarak kavranır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin aklını yitirmesi ile bir etkenin onu bu duruma getirmesi katılımcıları farklı iki süreçtir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gerçek durumdan ayrı olarak kişi kendisini aklını yitirmiş gibi gösterebilir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin akıl işleyişini kaybettiği veya aklı ile benliği arasına engel girdiği genel durumlara uygundur.","boundary_detail":"Dal gerçek ya da gösterilen akıl yitimiyle sınırlıdır; görünmeyen varlıklar ve ağaçlı bahçe anlamları dışarıda kalır.","branch_image_ar":"ستر العقل بالجنون","concept_gloss":"aklı örten akıl yitimi","contextual_glosses":[{"applicability":"Kişinin gerçek bir akıl yitimi durumuna girdiği geçişsiz kullanımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin akıl işleyişini kaybetmesini ve durum değişimini korur."},"facet_ids":["F001","F002"],"text":"aklını yitirmek","usage_role":"contextual"},{"applicability":"Kişinin gerçek durumu değil, bu durumun görünüşünü isteyerek sergilediği bağlamlara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Akıl yitimini gerçek yaşamadan onun görünüşünü sergileme ayrımını korur."},"facet_ids":["F003"],"text":"aklını yitirmiş gibi davranmak","usage_role":"contextual"}],"definition":"Aklın işleyişini örten veya benlik ile akıl arasına engel koyan akıl yitimi durumudur; kişi bu duruma düşebilir, düşürülebilir ya da böyleymiş gibi davranabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Akıl yitimi, aklın örtülmesi veya benlik ile akıl arasına engel girmesi olarak kavranır."},{"facet_id":"F002","role":"extension","statement":"Kişinin aklını yitirmesi ile bir etkenin onu bu duruma getirmesi katılımcıları farklı iki süreçtir."},{"facet_id":"F003","role":"associated_use","statement":"Gerçek durumdan ayrı olarak kişi kendisini aklını yitirmiş gibi gösterebilir."}],"identity_rationale":"Kaynak ifadesi aklın örtülmesini, benlik ile akıl arasına engel girmesini, kişinin bu duruma düşmesini veya düşürülmesini bildirir; görünüşte bu hali takınma da ayrı bir kullanımdır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"aklını yitirmek; aklını yitirmiş duruma getirmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"akıl yitimi; benlik ile akıl arasındaki engel"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"aklını yitirmiş gibi davranmak"}],"lexicalization_note":"Tanım yalın akıl yitimi dalını kapsar ve başka dalların varlık ya da yer anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün akıl, karar, görünmeyen etki ve aynı kökten adaylar değerlendirildi; kapsamı en çok çakışan bozulma dalı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak örtülme temelli akıl yitimini ve onun dilbilgisel süreçlerini öne çıkarır; komşu ise neden ve bozulma türleri bakımından daha geniştir.","focus_only":"Odak dal akıl yitimini örtülme veya benlik ile akıl arasına giren engel olarak kurar ve bu görünüşü takınmayı da kapsar.","gloss":"akıl işleyişinin bozulması","neighbor_only":"Komşu dal akıl ve yürek bozulmasını hastalık, dokunma, sevgi veya başka etkenlerle daha geniş biçimde ilişkilendirir.","neighbor_ref":"root_000390/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da aklın sağlıklı işleyişini yitirmesi alanında önemli ölçüde örtüşür."}],"source_phrase_ar":"الجنة الجنون وذلك أنه يغطي العقل (maqayis)؛ المجنة الجنون وجن الرجل وأجنه الله فهو مجنون (ayn)؛ جن الرجل جنونا وأجنه الله فهو مجنون (sihah)؛ به جنون وجنة ومجنة (tahdhib)؛ الجنون حائل بين النفس والعقل (mufradat)","source_summary":"Kaynaklar akıl işleyişinin örtülmesi ve kişinin aklını yitirmesi çekirdeğinde birleşir; ettirgen süreç ile görünüşte bu hali takınmayı da kaydeder.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الجنون والجنة والمجنة والجنن ومجنون وتجانن إذا تعلق المعنى بزوال العقل أو إظهاره","what_is_not_ar":"ليس الجن ولا الجنة البستان"},"support_links":[]},{"boundary":"Dal rahimdeki çocuk ve onun saklı bulunduğu dönemle sınırlıdır; gömülmüş kişi veya gömüt anlamına gelmez.","branch_kind":"bare","branch_ref":"root_000266/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:30:2:1","qac_word_ref":"89:30:2","surface_ar":"جَنَّتِ"}],"gloss":"ana rahmindeki doğmamış çocuk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çocuk, annesinin karnında veya rahminde bulunduğu süre boyunca doğmamış durumdadır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Annenin doğmamış çocuğu taşıması ile çocuğun rahimde saklı bulunması katılımcıları farklı bağlantılı süreçlerdir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çocuğun doğumdan önce annesinin karnında veya rahminde bulunduğu bütün yalın bağlamlara uygundur.","boundary_detail":"Dal rahimdeki çocuk ve onun saklı bulunduğu dönemle sınırlıdır; gömülmüş kişi veya gömüt anlamına gelmez.","branch_image_ar":"الجنين المستور في البطن","concept_gloss":"ana rahmindeki doğmamış çocuk","contextual_glosses":[{"applicability":"Annenin doğmamış çocuğu karnında taşıdığı süreç özne üzerinden anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Annenin taşıyan katılımcı, çocuğun da rahimde saklı katılımcı oluşunu korur."},"facet_ids":["F002"],"text":"rahminde çocuk taşımak","usage_role":"contextual"}],"definition":"Doğmamış çocuk, annesinin karnında veya rahminde kaldığı süre boyunca bu dalın referansıdır; annenin onu taşıması ve çocuğun rahimde saklı kalması buna bağlı süreçlerdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çocuk, annesinin karnında veya rahminde bulunduğu süre boyunca doğmamış durumdadır."},{"facet_id":"F002","role":"associated_use","statement":"Annenin doğmamış çocuğu taşıması ile çocuğun rahimde saklı bulunması katılımcıları farklı bağlantılı süreçlerdir."}],"identity_rationale":"Kaynaklar çocuğu annesinin karnında veya rahminde kaldığı süre boyunca tanımlar ve annenin bu çocuğu taşımasıyla çocuğun rahimde saklı kalmasını ayrı süreçler olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"ana rahmindeki doğmamış çocuk"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"rahminde çocuk taşımak; çocuğun rahimde saklı kalması"}],"lexicalization_note":"Tanım yalın rahimdeki çocuk anlamını korur; gebelik, doğum veya gömme alanının tamamına genişletilmez.","neighbor_coverage_note":"Bütün rahim, gebelik, doğum ve aynı kökten adaylar değerlendirildi; çocuk ile gebelik durumu ayrımı en açıklayıcı sınırı verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği rahimdeki çocuktur; komşu dalın çekirdeği ise annenin taşıma durumu ve bunun süresidir.","focus_only":"Odak dal anne rahminde bulunan doğmamış çocuğu referans alır.","gloss":"doğmamış çocuk ve gebelik","neighbor_only":"Komşu dal annenin gebelik durumunu, süresini ve karındaki yükü daha geniş biçimde kapsar.","neighbor_ref":"root_000291/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da annenin karnındaki çocuk ve doğum öncesi dönem alanındadır."}],"source_phrase_ar":"الجنين الولد في بطن أمه (maqayis)؛ أجنت الحامل الجنين أي الولد في بطنها (ayn)؛ الجنين الولد ما دام في البطن (sihah)؛ الجنين الولد في الرحم (tahdhib)؛ الجنين الولد ما دام في بطن أمه (mufradat)","source_summary":"Kaynaklar rahimde veya anne karnında bulunan doğmamış çocuk tanımında birleşir; taşıma ve rahimde saklı kalma süreçlerini de kaydeder.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الجنين والولد ما دام في بطن أمه وأجنة البطون","what_is_not_ar":"ليس المقبور ولا القبر"},"support_links":[]},{"boundary":"Dal koruyucu siper veya savaş donanımıyla sınırlıdır; bahçe, akıl yitimi ve sıradan örtü anlamlarına genişlemez.","branch_kind":"bare","branch_ref":"root_000266/B008","candidate_links":[{"candidate_id":"cand_8776312a86b2c0b3c773","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:30:2:1","qac_word_ref":"89:30:2","surface_ar":"جَنَّتِ"}],"gloss":"koruyucu siper veya savaş donanımı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir örtü veya savaş donanımı kişiyi tehlikeden koruyan siper işlevi görür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kalkan ve zırh, koruyucu siper çekirdeğinin açık araç türleridir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalkan, zırh ya da kişinin arkasına sığınıp kendini koruduğu başka bir savaş örtüsü için uygundur.","boundary_detail":"Dal koruyucu siper veya savaş donanımıyla sınırlıdır; bahçe, akıl yitimi ve sıradan örtü anlamlarına genişlemez.","branch_image_ar":"الجُنّة الواقية","concept_gloss":"koruyucu siper veya savaş donanımı","contextual_glosses":[{"applicability":"Kaynak biçim özellikle elde taşınan koruyucu savaş aracını gösterdiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Elde taşınan siper aracını ve sahibini koruma işlevini tam olarak korur."},"facet_ids":["F001","F002"],"text":"kalkan","usage_role":"contextual"}],"definition":"Kişinin tehlikeden korunmak için arkasına sığındığı veya üzerine aldığı koruyucu örtü ya da savaş donanımıdır; kalkan ve zırh bunun başlıca türleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir örtü veya savaş donanımı kişiyi tehlikeden koruyan siper işlevi görür."},{"facet_id":"F002","role":"specialization","statement":"Kalkan ve zırh, koruyucu siper çekirdeğinin açık araç türleridir."}],"identity_rationale":"Kaynak ifadesi korunmak için arkasına sığınılan silah veya örtüyü genel çekirdek, kalkanı ve zırhı ise belirgin gerçekleşmeler olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"koruyucu örtü, siper veya savaş donanımı"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kalkan"}],"lexicalization_note":"Tanım yalın koruyucu örtü ve silah anlamını kapsar; yalnızca belirli bir savaş söz öbeğine bağlanmaz.","neighbor_coverage_note":"Bütün kalkan, zırh, hazırlık, korunma ve aynı kökten adaylar değerlendirildi; giyilebilir zırh ile genel siper ayrımı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kalkan gibi giyilmeyen siperleri de kapsar; komşu ise giyilebilir zırh ve korunma giysisine daha sıkı bağlıdır.","focus_only":"Odak dal kalkanı ve korunmak için arkasına sığınılan her türlü savaş örtüsünü kapsar.","gloss":"koruyucu savaş donanımı","neighbor_only":"Komşu dal özellikle savaşta giyilen zırhı ve giyilebilir koruyucu donanımı öne çıkarır.","neighbor_ref":"root_001341/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da savaşta bedeni saldırıdan koruyan araç ve donanımları bildirir."}],"source_phrase_ar":"المجن الترس وكل ما استتر به من السلاح فهو جنة (maqayis)؛ المجن الترس والجنة الدرع وكل ما وقاك فهو جنتك (ayn)؛ الجنة ما استترت به من سلاح والجنة السترة والمجن الترس (sihah)؛ المجن الترس (tahdhib)؛ المجن والمجنة الترس الذي يجن صاحبه (mufradat)","source_summary":"Kaynaklar korunmak için kullanılan örtü veya silah çekirdeğinde birleşir ve özellikle kalkan ile zırhı bu kapsamda anar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الجنة التي يتقى بها والمجن الترس والسلاح وما وقاك","what_is_not_ar":"ليس الجنة البستان ولا الجنون"},"support_links":["sup_d530d8e3c93ad64186f9"]},{"boundary":"Dal ölü ve gömme alanındadır; anne rahmindeki doğmamış çocuk anlamıyla yalnızca biçim benzerliği paylaşır.","branch_kind":"bare","branch_ref":"root_000266/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:30:2:1","qac_word_ref":"89:30:2","surface_ar":"جَنَّتِ"}],"gloss":"ölüyü örtüp gömme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ölü örtülerek gözden kaldırılır ve toprağa gömülür."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gömüt, ölü örtüsü ve gömülmüş kişi aynı işlemin sırasıyla yer, araç ve sonuç katılımcılarını adlandırır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ölünün gözden kaldırılarak toprağa verilmesini ve bu işlemin örtme yönünü birlikte anlatan bağlamlara uygundur.","boundary_detail":"Dal ölü ve gömme alanındadır; anne rahmindeki doğmamış çocuk anlamıyla yalnızca biçim benzerliği paylaşır.","branch_image_ar":"مواراة الميت","concept_gloss":"ölüyü örtüp gömme","contextual_glosses":[{"applicability":"Örtme ayrıntısının gömme eyleminden doğal olarak anlaşıldığı akıcı anlatımlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölü katılımcısını ve gömerek gözden kaldırma işlemini bağlam içinde korur."},"facet_ids":["F001"],"text":"ölüyü toprağa vermek","usage_role":"contextual"}],"definition":"Ölüyü örterek gözden kaldırmak ve toprağa gömmektir; gömüt, ölü örtüsü ve gömülmüş kişi bu işlemin yer, araç ve sonuç odaklı adlarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ölü örtülerek gözden kaldırılır ve toprağa gömülür."},{"facet_id":"F002","role":"extension","statement":"Gömüt, ölü örtüsü ve gömülmüş kişi aynı işlemin sırasıyla yer, araç ve sonuç katılımcılarını adlandırır."}],"identity_rationale":"Kaynak ifadesi ölüyü örterek gözden kaldırma ve gömme eylemini, gömütü, ölü örtüsünü ve gömülmüş kişiyi aynı dalda açıkça kaydeder.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"ölüyü örtmek ve gömmek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"gömüt; ölü örtüsü; gömülmüş kişi"}],"lexicalization_note":"Tanım yalın gömme ve ölü örtme dalını kapsar; genel çukur açma veya doğmamış çocuk anlamına genişletilmez.","neighbor_coverage_note":"Bütün gömme, gömüt, örtme ve aynı kökten adaylar değerlendirildi; genel gömüt dalı en yakın fakat kapsamı farklı komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak örtüp gözden kaldırma çekirdeği ile ölü örtüsü sonucunu korur; komşu ise gömüt kurumu ve gömme izni gibi daha geniş işlemleri kapsar.","focus_only":"Odak dal gömmenin yanında ölü örtüsünü ve gömülmüş kişi yorumunu da aynı biçim alanında taşır.","gloss":"ölüyü gömme","neighbor_only":"Komşu dal gömüt yerini, gömme eylemini, gömüt hazırlamayı ve gömülmeye izin vermeyi daha geniş biçimde kapsar.","neighbor_ref":"root_001195/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da ölünün gömüte yerleştirilerek toprağa verilmesi alanında örtüşür."}],"source_phrase_ar":"الجنين المقبور (maqayis)؛ الجنن القبر وقيل للكفن أيضا (ayn)؛ جننت الميت وأجننته أي واريته والجنن القبر (sihah)؛ جننته في القبر وأجننته والجنن القبر والجنن الكفن (tahdhib)؛ الجنين القبر (mufradat)","source_summary":"Kaynaklar ölüyü örtüp gömme eyleminde birleşir; aynı biçim alanında gömüt, ölü örtüsü ve gömülmüş kişi yorumlarını da verir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه جن الميت وأجنه إذا واراه والجنن القبر والكفن والجنين بمعنى المقبور أو القبر","what_is_not_ar":"ليس الجنين في الرحم"},"support_links":[]},{"boundary":"Dal içte saklı yürek ve gizli yönle sınırlıdır; gece karanlığı veya insan topluluğu anlamlarını içermez.","branch_kind":"bare","branch_ref":"root_000266/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:30:2:1","qac_word_ref":"89:30:2","surface_ar":"جَنَّتِ"}],"gloss":"duyulardan saklı yürek ve gizli yön","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yürek ve onun korkuyla sarsılan iç yönü bedende duyulardan saklıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir işin gizli veya görünmeyen yanı, içte saklı olma özelliğinden türeyen soyut kullanımdır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem bedende saklı yüreği hem de bir işin görünmeyen iç yönünü kapsaması gereken genel açıklamalarda kullanılır.","boundary_detail":"Dal içte saklı yürek ve gizli yönle sınırlıdır; gece karanlığı veya insan topluluğu anlamlarını içermez.","branch_image_ar":"الجنان المستور في الصدر","concept_gloss":"duyulardan saklı yürek ve gizli yön","contextual_glosses":[{"applicability":"Bedendeki iç organ veya korkunun yerleştiği iç merkez anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedende saklı iç organı ve duygusal iç merkez işlevini korur."},"facet_ids":["F001"],"text":"yürek","usage_role":"contextual"},{"applicability":"Somut organ değil, bir olayın görünmeyen veya saklı tarafı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Soyut iş referansını ve onun görünmeyen iç tarafını eksiksiz korur."},"facet_ids":["F002"],"text":"işin gizli yönü","usage_role":"contextual"}],"definition":"Duyulardan saklı olduğu için yürek veya yüreğin iç yönü; buradan hareketle bir işin gizli, görünmeyen yanı anlamıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yürek ve onun korkuyla sarsılan iç yönü bedende duyulardan saklıdır."},{"facet_id":"F002","role":"extension","statement":"Bir işin gizli veya görünmeyen yanı, içte saklı olma özelliğinden türeyen soyut kullanımdır."}],"identity_rationale":"Kaynak ifadesi duyulardan saklı iç organı ve onun korkuyla sarsılan iç yönünü, ayrıca gizli iş veya görünmeyen yön kullanımını açıkça ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yürek veya yüreğin saklı iç yönü"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"gizli iş veya görünmeyen yön"}],"lexicalization_note":"Tanım yalın içte saklı yürek ve gizli yön anlamlarını kapsar; başka söz öbeklerinden anlam aktarmaz.","neighbor_coverage_note":"Bütün göğüs, yürek, gizli iş ve aynı kökten adaylar değerlendirildi; iç organ ile içte saklama eylemi ayrımı en yararlı karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bir iç organı veya gizli yönü adlandırır; komşu ise bir içeriği zihinde saklama eylemini kurar, bu nedenle çekirdekleri farklıdır.","focus_only":"Odak dal öncelikle duyulardan saklı yüreği adlandırır ve gizli iş anlamına uzanır.","gloss":"yürek ve içte saklama","neighbor_only":"Komşu dal bilgi, düşünce veya sırrın kişinin iç dünyasında saklanması eylemini bildirir.","neighbor_ref":"root_001324/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişinin iç dünyası ve duyulardan saklı içerik alanında buluşur."}],"source_phrase_ar":"الجنان القلب (maqayis)؛ الجنان روع القلب (ayn;tahdhib)؛ أراد بالجن القلب (sihah)؛ الجنان القلب لكونه مستورا عن الحاسة (mufradat)؛ الجنان الأمر الخفي (tahdhib)","source_summary":"Kaynaklar duyulardan saklı yürek anlamında birleşir; bir kaynak aynı biçimi gizli iş ve görünmeyen yön için de kaydeder.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الجنان بمعنى القلب أو روع القلب والأمر الخفي المستور","what_is_not_ar":"ليس جنان الليل ولا جنان الناس"},"support_links":[]},{"boundary":"Dal bitki gelişimi ve yoğunluğuyla sınırlıdır; böcek sesi veya sırf ağaçlı bahçe adı bu çekirdeğe girmez.","branch_kind":"bare","branch_ref":"root_000266/B011","candidate_links":[{"candidate_id":"cand_52184e28b0f598806e3a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:30:2:1","qac_word_ref":"89:30:2","surface_ar":"جَنَّتِ"}],"gloss":"bitkinin güçlenip boylanması ve sıklaşması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bitki güçlenir, boy atar, sıklaşıp dolaşır veya çiçek açarak gelişimini belirginleştirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Uzun ağaç ile yoğun ve bol otlu arazi, bitkisel gelişimin sonuç veya alan odaklı uzantılarıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bol otlu arazi kullanımında bitki örtüsünün henüz otlanmamış olması ayrıca belirtilir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bitkinin gelişerek uzadığı, yoğunlaştığı, birbirine dolaştığı veya çiçek açtığı genel bağlamlara uygundur.","boundary_detail":"Dal bitki gelişimi ve yoğunluğuyla sınırlıdır; böcek sesi veya sırf ağaçlı bahçe adı bu çekirdeğe girmez.","branch_image_ar":"التفاف النبات واندفاعه","concept_gloss":"bitkinin güçlenip boylanması ve sıklaşması","contextual_glosses":[{"applicability":"Bahçe, vadi veya ufuk gibi bir alanın yoğun bitki örtüsüyle kaplandığı bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alan katılımcısını ve bitki örtüsünün yoğunlaşıp alanı kaplaması sonucunu korur."},"facet_ids":["F001","F002"],"text":"bitkiyle dolup sıklaşmak","usage_role":"contextual"}],"definition":"Bitkinin güçlenmesi, boy atması, sıklaşıp birbirine dolaşması veya çiçek açmasıdır; uzun ağaç ve bol, otlanmamış bitki örtüsü bu gelişimin sonuç odaklı görünümleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bitki güçlenir, boy atar, sıklaşıp dolaşır veya çiçek açarak gelişimini belirginleştirir."},{"facet_id":"F002","role":"extension","statement":"Uzun ağaç ile yoğun ve bol otlu arazi, bitkisel gelişimin sonuç veya alan odaklı uzantılarıdır."},{"facet_id":"F003","role":"specialization","statement":"Bol otlu arazi kullanımında bitki örtüsünün henüz otlanmamış olması ayrıca belirtilir."}],"identity_rationale":"Kaynak ifadesi bitkinin güçlenme, boy atma, sıklaşıp birbirine dolaşma veya çiçek açma gelişimini; uzun ağaç ve bol otlu arazi sonuçlarını da buna bağlı biçimde verir.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"bitkinin güçlenmesi, boylanması, sıklaşması veya çiçek açması"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"uzun ağaç; bol otlu ve henüz otlanmamış arazi"}],"lexicalization_note":"Tanım yalın bitki gelişimi dalını korur ve böcek sesine bağlı kullanımı ya da başka dalların yer adlarını içeri almaz.","neighbor_coverage_note":"Bütün yoğun bitki, bahçe, ot ve aynı kökten adaylar değerlendirildi; gelişim süreci ile dolaşık düzen arasındaki sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak gelişimin birden çok aşamasını ve sonucunu kapsar; komşunun çekirdeği ise bitkilerin birbirine dolaşmış düzenidir.","focus_only":"Odak dal bitkinin güçlenmesini, boy atmasını ve çiçek açmasını sıklaşmanın yanında kapsar.","gloss":"bitkinin sıklaşıp dolaşması","neighbor_only":"Komşu dal bitki veya ağaçların özellikle birbirine dolaşmış, kat kat kıvrılmış düzenini öne çıkarır.","neighbor_ref":"root_001365/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da yoğunlaşan bitkilerin birbirine girip sık bir örtü oluşturması alanında örtüşür."}],"source_phrase_ar":"جن النبت جنونا إذا اشتد وخرج زهره (maqayis)؛ جن النبت جنونا أي طال والتف وخرج زهره ونخلة مجنونة أي طويلة (sihah)؛ للنبت الملتف الكثيف مجنون وجنت الرياض جنونا إذا اعتم نبتها (tahdhib)؛ جن التلاع والآفاق أي كثر عشبها (mufradat)","source_summary":"Kaynaklar bitkinin güçlenmesi, uzaması, sıklaşması ve çiçeklenmesi çevresinde birleşir; uzun ağaç ile bol ve otlanmamış araziyi sonuç olarak ekler.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه النبات إذا اشتد أو طال أو التف أو خرج زهره والنخل الطويل والأرض الكثيرة العشب","what_is_not_ar":"ليس الذباب إذا حمل على الصوت"},"support_links":["sup_e612bf358beccf576d7a"]},{"boundary":"Dal yılan referansıyla sınırlıdır; görünmeyen ruhani varlığın atası veya bireyi anlamını içermez.","branch_kind":"bare","branch_ref":"root_000266/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:30:2:1","qac_word_ref":"89:30:2","surface_ar":"جَنَّتِ"}],"gloss":"yılan, özellikle beyaz bir tür","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Referans bir yılan, kimi kaynaklarda özellikle beyaz yılan veya belirli bir yılan türüdür."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Görünmeyen varlık bireyine benzetme, yılan referansının açıklaması olup onu o varlıkla özdeşleştirmez."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Biçimin genel bir yılanı, beyaz yılanı veya belirli bir yılan türünü adlandırdığı bağlamlara uygundur.","boundary_detail":"Dal yılan referansıyla sınırlıdır; görünmeyen ruhani varlığın atası veya bireyi anlamını içermez.","branch_image_ar":"الجان حية","concept_gloss":"yılan, özellikle beyaz bir tür","contextual_glosses":[{"applicability":"Kaynağın veya bağlamın yılanın beyaz olduğunu açıkça belirttiği kullanımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yılan türünü ve bağlamda açıkça verilen beyazlık niteliğini korur."},"facet_ids":["F001"],"text":"beyaz yılan","usage_role":"contextual"}],"definition":"Yılanı, özellikle beyaz bir yılanı veya belirli bir yılan türünü adlandıran kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Referans bir yılan, kimi kaynaklarda özellikle beyaz yılan veya belirli bir yılan türüdür."},{"facet_id":"F002","role":"source_variant","statement":"Görünmeyen varlık bireyine benzetme, yılan referansının açıklaması olup onu o varlıkla özdeşleştirmez."}],"identity_rationale":"Kaynak ifadesi biçimi yılan, beyaz yılan veya belirli bir yılan türü olarak verir; görünmeyen varlık anlamıyla bağ yalnızca benzetme açıklamasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"yılan, beyaz yılan veya belirli bir yılan türü"}],"lexicalization_note":"Tanım yalın yılan adını korur ve aynı biçimin görünmeyen varlık anlamını bu dala taşımaz.","neighbor_coverage_note":"Bütün yılan, küçük canlı ve aynı kökten adaylar değerlendirildi; beyaz yılan ortaklığı taşıyan ayrı ad en keskin karşılaştırmayı sağlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Referans özellikleri kesişse de bunlar ayrı yılan adlarıdır; odak daha geniş ve türü değişken, komşu ise ayrı benzetmeyle kurulmuş addır.","focus_only":"Odak dal genel yılanı veya beyaz ya da belirli bir yılan türünü aynı ad altında kapsar.","gloss":"beyaz yılan adları","neighbor_only":"Komşu dal beyaz yılanı bir takı parçasının biçimine benzetilen ayrı bir adla sınırlar.","neighbor_ref":"root_001248/B009","relation_type":"near_neighbor","shared_zone":"Her iki dalın referansı bazı kullanımlarda beyaz bir yılan olabilir."}],"source_phrase_ar":"الحية الذي يسمى الجان فهو تشبيه له بالواحد من الجان (maqayis)؛ الجان حية بيضاء (ayn)؛ الجان أيضا حية بيضاء (sihah)؛ الجان الحية وجمعها جوان (tahdhib)؛ الجان ضرب من الحيات (mufradat)","source_summary":"Kaynaklar yılan referansında birleşir; bazıları beyazlığı belirtir, biri bunu görünmeyen varlık bireyine benzetmeyle açıklar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الجان بمعنى الحية أو الحية البيضاء أو ضرب من الحيات","what_is_not_ar":"ليس الجان أبو الجن إلا من جهة اللفظ"},"support_links":[]},{"boundary":"Her küçük grup bu dala girmez; insanların ana gövdesi, büyük kitlesi veya çoğunluğu söz konusudur.","branch_kind":"bare","branch_ref":"root_000266/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:30:2:1","qac_word_ref":"89:30:2","surface_ar":"جَنَّتِ"}],"gloss":"halkın büyük kitlesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanların çoğunluğu veya ana kitlesi tek bir toplumsal gövde olarak ele alınır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir topluluğun çoğunluğunu, ana gövdesini veya sıradan insanlardan oluşan geniş kesimini anlatan bağlamlara uygundur.","boundary_detail":"Her küçük grup bu dala girmez; insanların ana gövdesi, büyük kitlesi veya çoğunluğu söz konusudur.","branch_image_ar":"سواد الناس وجماعتهم","concept_gloss":"halkın büyük kitlesi","contextual_glosses":[{"applicability":"Sayısal veya toplumsal bakımdan grubun ana bölümünün kastedildiği cümlelerde doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan grubunu ve grubun büyük ana bölümünü gösterme işlevini korur."},"facet_ids":["F001"],"text":"insanların çoğunluğu","usage_role":"contextual"}],"definition":"Bir insan topluluğunun büyük çoğunluğu, sıradan kitlesi veya topluca oluşturduğu ana gövdesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanların çoğunluğu veya ana kitlesi tek bir toplumsal gövde olarak ele alınır."}],"identity_rationale":"Kaynak ifadesi insanların büyük çoğunluğunu, sıradan kitlesini veya topluca oluşturduğu ana gövdeyi bildirir; gece karanlığı ve yürek anlamları açıkça dışarıdadır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"insanların çoğunluğu veya halkın büyük kitlesi"}],"lexicalization_note":"Tanım yalın insan kitlesi anlamını korur ve başka topluluk türlerini ya da karanlık anlamını içeri almaz.","neighbor_coverage_note":"Bütün topluluk, çoğunluk, kalabalık ve aynı kökten adaylar değerlendirildi; ana kitle ile fiziksel izdiham ayrımı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta toplumsal çoğunluk veya ana gövde yeterlidir; komşuda insanların birbirini örten yoğun bir kalabalık oluşturması kurucu koşuldur.","focus_only":"Odak dal bir topluluğun ana gövdesini veya çoğunluğunu, fiziksel sıkışıklık şartı olmadan bildirir.","gloss":"insan kitlesi ve sık kalabalık","neighbor_only":"Komşu dal insanların kalabalıkta birbirini örtecek ölçüde sıkışmasını ve izdihamını gerektirir.","neighbor_ref":"root_001105/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da çok sayıda insanın oluşturduğu büyük topluluk alanında örtüşür."}],"source_phrase_ar":"جنان الناس معظمهم ويسمى السواد (maqayis)؛ جنان الناس دهماؤهم (sihah)؛ جنانهم جماعتهم وسوادهم (tahdhib)","source_summary":"Kaynaklar insanların çoğunluğu, kalabalık ana kitlesi ve sıradan toplumsal gövdesi anlamlarında birleşir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه جنان الناس بمعنى معظمهم أو دهمائهم أو سوادهم وجماعتهم","what_is_not_ar":"ليس جنان الليل ولا الجنان القلب"},"support_links":[]},{"boundary":"Dal bir şeyin ilk ve yeni evresiyle sınırlıdır; genel olarak başlama eylemi veya ardışık evrelerin tamamı değildir.","branch_kind":"bare","branch_ref":"root_000266/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:30:2:1","qac_word_ref":"89:30:2","surface_ar":"جَنَّتِ"}],"gloss":"bir şeyin ilk ve yeni dönemi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin sürecindeki ilk, yeni ve henüz gelişmekte olan başlangıç dönemi seçilir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gençliğin veya çocukluğun ilk dönemi bu genel başlangıç evresinin belirgin örnekleridir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gençlik, çocukluk, dönem veya başka bir sürecin henüz başlangıçta olduğu ilk evresini anlatmaya uygundur.","boundary_detail":"Dal bir şeyin ilk ve yeni evresiyle sınırlıdır; genel olarak başlama eylemi veya ardışık evrelerin tamamı değildir.","branch_image_ar":"جن الشيء في بدايته","concept_gloss":"bir şeyin ilk ve yeni dönemi","contextual_glosses":[{"applicability":"Bir kişinin gençlik döneminin başlangıç kısmı özellikle kastedildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gençlik dönemini ve bu dönemin ilk, yeni evresini tam olarak korur."},"facet_ids":["F001","F002"],"text":"gençliğinin ilk yılları","usage_role":"contextual"}],"definition":"Gençlik, çocukluk, bir dönem veya herhangi bir şeyin henüz yeni olduğu ilk başlangıç evresidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin sürecindeki ilk, yeni ve henüz gelişmekte olan başlangıç dönemi seçilir."},{"facet_id":"F002","role":"example","statement":"Gençliğin veya çocukluğun ilk dönemi bu genel başlangıç evresinin belirgin örnekleridir."}],"identity_rationale":"Kaynak ifadesi gençlik, çocukluk, dönem veya herhangi bir şeyin ilk başlangıcını ve henüz yeni oluşunu bildirir; bu nedenle dal başlangıç evresi olarak doğru kurulmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"gençliğin, çocukluğun veya bir dönemin ilk başlangıcı"}],"lexicalization_note":"Tanım yalın ilk dönem anlamını kapsar ve belirli bir başlama söz öbeğine ya da bütün yaşam evrelerine genişletilmez.","neighbor_coverage_note":"Bütün gençlik, başlama, evre ve karşıt zaman adayları değerlendirildi; başlangıç evresi ile başlama eylemi ayrımı en yararlı olandır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bir başlangıç evresini adlandırır; komşu ise başlama eylemini ve yeniden başlatmayı da kapsar, bu yüzden kapsamları tam çakışmaz.","focus_only":"Odak dal başlayan şeyin ilk ve yeni dönemini, yani süreç içindeki bir evreyi adlandırır.","gloss":"başlangıç ve ilk dönem","neighbor_only":"Komşu dal bir işe başlama, yeniden başlama veya yakın geçmişteki ilk zamanı da kapsayan eylemsel bir alandır.","neighbor_ref":"root_000060/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir sürecin ilk noktasına veya başlangıç bölümüne yönelir."}],"source_phrase_ar":"كان ذلك في جن شبابه أي في أول شبابه (sihah)؛ كان ذلك في جن صباه أي في حداثته وكذلك جن كل شيء أول ابتدائه (tahdhib)","source_summary":"Kaynaklar gençlik ve çocukluk örneklerinden hareketle anlamı herhangi bir şeyin ilk başlangıç ve yenilik dönemine geneller.","sources":["SI","TA"],"what_is_ar":"يدخل فيه جن الشباب أو الصبا أو العهد أو كل شيء بمعنى أول ابتدائه وحدثانه","what_is_not_ar":"ليس جنون العقل"},"support_links":[]},{"boundary":"Ses anlamı böcek yorumu şartına bağlıdır; aynı biçim bitkiyi gösterdiğinde sıklaşma anlamı bu dalın dışında kalır.","branch_kind":"bare","branch_ref":"root_000266/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:30:2:1","qac_word_ref":"89:30:2","surface_ar":"جَنَّتِ"}],"gloss":"uçuş sırasında çoğalan sinek vızıltısı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sinek uçarken çıkardığı sesi veya vızıltıyı çoğaltır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İki yorumlu ad böceği gösterirse uçuş sesi, bitkiyi gösterirse sıklaşıp dolaşma anlamına gelir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Referansın sinek veya benzeri küçük uçucu canlı olduğu ve sesin uçuşta arttığı bağlamlara uygundur.","boundary_detail":"Ses anlamı böcek yorumu şartına bağlıdır; aynı biçim bitkiyi gösterdiğinde sıklaşma anlamı bu dalın dışında kalır.","branch_image_ar":"جن الذباب وصوت الخازباز","concept_gloss":"uçuş sırasında çoğalan sinek vızıltısı","contextual_glosses":[{"applicability":"Sinek veya benzeri küçük uçucu canlının çıkardığı sesin çoğalması eylem olarak anlatıldığında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Böcek sesini ve bu sesin miktar veya yoğunluk bakımından artmasını korur."},"facet_ids":["F001"],"text":"vızıldaması artmak","usage_role":"contextual"}],"definition":"Sineğin veya sinek olarak yorumlanan küçük uçucu canlının uçuş sırasında sesini ve vızıltısını çoğaltmasıdır. Aynı ad bitkiyi gösterirse anlam ses değil, bitkinin sıklaşmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sinek uçarken çıkardığı sesi veya vızıltıyı çoğaltır."},{"facet_id":"F002","role":"source_variant","statement":"İki yorumlu ad böceği gösterirse uçuş sesi, bitkiyi gösterirse sıklaşıp dolaşma anlamına gelir."}],"identity_rationale":"Kaynak ifadesi sineğin sesinin çoğalmasını açıkça destekler, ancak ikinci biçimin hem uçarken çok ses çıkaran bir böceğe hem de sıklaşan bir bitkiye yorumlanabileceğini söyler; dal yalnızca böcek yorumu altında ses dalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"sineğin vızıltısının veya sesinin çoğalması"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"böcekse uçuş vızıltısının artması; bitkiyse sıklaşıp dolaşması"}],"lexicalization_note":"Yalın ses dalı korunur, fakat iki yorumlu biçim yalnızca böcek referansı kesin olduğunda bu tanıma bağlanır.","neighbor_coverage_note":"Bütün böcek, ses, hareket ve aynı kökten adaylar değerlendirildi; ses kaynağını sınayan genel hareket uğultusu dalı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta ses kaynağı küçük uçucu böcektir ve ses çoğalır; komşu çok çeşitli hareket kaynaklarından çıkan hışırtı ve uğultuyu kapsar.","focus_only":"Odak dal belirli bir uçucu böceğin uçarken artan vızıltısına bağlıdır.","gloss":"vızıltı ve hareket uğultusu","neighbor_only":"Komşu dal rüzgar, hareket, alay veya kaynayan kap gibi çeşitli kaynakların hışırtı ve uğultusunu kapsar.","neighbor_ref":"root_001588/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da hareket sırasında doğan sürekli veya yinelenen sesi anlatabilir."}],"source_phrase_ar":"جن الذباب أي كثر صوته (sihah)؛ جن الخازباز به جنونا يحتمل هذين الوجهين (sihah)؛ قيل هو ذباب وجنونه كثرة ترنمه في طيرانه وقيل هو نبت وجنون النبت التفافه (tahdhib)","source_summary":"Kaynaklar sineğin sesinin çoğalmasını verir; iki yorumlu adın böcek okumasında uçuş vızıltısı, bitki okumasında ise sıklaşma bildirdiğini ayrıca belirtir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه كثرة صوت الذباب أو ترنم الخازباز حيث نص المصدر على ذلك","what_is_not_ar":"ليس نبات الخازباز إذا حمل على النبات"},"support_links":[]},{"boundary":"Dal göğüs kafesinin kemik yapısıyla sınırlıdır; yürek, göğüs eti veya kalça kemikleri anlamına gelmez.","branch_kind":"bare","branch_ref":"root_000266/B016","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:30:2:1","qac_word_ref":"89:30:2","surface_ar":"جَنَّتِ"}],"gloss":"göğüs kemikleri ve kaburga uçları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Referans göğüs kafesinin kemikleri veya kaburgaların göğse yakın uçlarıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir açıklama aynı anatomik adı göğsün içteki orta kemiğine kadar genişletir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Göğüs kafesindeki kemiklerin topluca veya kaburgaların göğse yakın uçlarının özel olarak kastedildiği bağlamlara uygundur.","boundary_detail":"Dal göğüs kafesinin kemik yapısıyla sınırlıdır; yürek, göğüs eti veya kalça kemikleri anlamına gelmez.","branch_image_ar":"الجناجن عظام الصدر","concept_gloss":"göğüs kemikleri ve kaburga uçları","contextual_glosses":[{"applicability":"Anatomik anlatım genel göğüs kemiklerinden daha dar olarak kaburga uçlarını seçtiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kaburga katılımcısını, uç bölümünü ve göğse yakın konumu eksiksiz korur."},"facet_ids":["F001"],"text":"kaburgaların göğse yakın uçları","usage_role":"explanatory"}],"definition":"Göğüs kafesindeki kemikler, özellikle kaburgaların göğse yakın uçları ve kimi açıklamada göğsün içteki orta kemiğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Referans göğüs kafesinin kemikleri veya kaburgaların göğse yakın uçlarıdır."},{"facet_id":"F002","role":"source_variant","statement":"Bir açıklama aynı anatomik adı göğsün içteki orta kemiğine kadar genişletir."}],"identity_rationale":"Kaynak ifadesi göğüs kemiklerini ve kaburgaların göğse yakın uçlarını bildirir; bir kaynak içteki orta kemiği de aynı anatomik bölgeye dahil eder.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"göğüs kemikleri veya kaburgaların göğse yakın uçları"}],"lexicalization_note":"Tanım yalın anatomik kemik adını korur ve komşu organ, et veya başka eklem adlarını içeri almaz.","neighbor_coverage_note":"Bütün göğüs, kaburga, kalça, eklem ve aynı kökten adaylar değerlendirildi; kemik grubu ile orta göğüs kemiği ayrımı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak çoğul bir kemik grubu ve kaburga uçlarıdır; komşu ise göğsün ortasındaki belirli tek kemiği adlandırır.","focus_only":"Odak dal göğüs kemiklerini topluca ve özellikle kaburgaların göğse yakın uçlarını kapsar.","gloss":"göğüs kemikleri ve orta göğüs kemiği","neighbor_only":"Komşu dal göğsün ortasındaki tek kemiği, başını ve üzerindeki kıl çıkış yerini kapsar.","neighbor_ref":"root_001232/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal göğüs kafesinin ön ve orta bölümündeki kemik yapılarıyla ilgilidir."}],"source_phrase_ar":"الجناجن عظام الصدر (maqayis)؛ الجنجن والجناجن أطراف الأضلاع مما يلي الصدر وعظم القلب (ayn)؛ الجناجن عظام الصدر الواحد جنجن (sihah)","source_summary":"Kaynaklar göğüs kemikleri tanımında birleşir; daha ayrıntılı açıklama kaburga uçlarını ve göğsün içteki orta kemiğini belirtir.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه الجناجن والجنجن عظام الصدر أو أطراف الأضلاع مما يلي الصدر","what_is_not_ar":"ليس الجنان القلب"},"support_links":[]},{"boundary":"Genel anlam saklanma yeridir; özel yer kullanımı belirli bir tarihsel pazar adına bağlıdır ve akıl yitimi anlamıyla karıştırılmaz.","branch_kind":"bare","branch_ref":"root_000266/B017","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:30:2:1","qac_word_ref":"89:30:2","surface_ar":"جَنَّتِ"}],"gloss":"içine girilip saklanılan yer","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yer, kişinin içine girerek görünmekten saklanmasına imkan verir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı biçim kaynakta anılan kent yakınındaki belirli bir eski pazar yerinin adı olarak da kullanılır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin görünmemek veya korunmak için içine girdiği genel saklanma yerini anlatan bağlamlara uygundur.","boundary_detail":"Genel anlam saklanma yeridir; özel yer kullanımı belirli bir tarihsel pazar adına bağlıdır ve akıl yitimi anlamıyla karıştırılmaz.","branch_image_ar":"المَجَنَّة موضع الاستتار","concept_gloss":"içine girilip saklanılan yer","contextual_glosses":[{"applicability":"Özel tarihsel yer adı değil, genel olarak saklanmaya yarayan mekan kastedildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mekan referansını ve saklanma işlevini bağlam içinde eksiksiz korur."},"facet_ids":["F001"],"text":"saklanma yeri","usage_role":"contextual"}],"definition":"Bir kişinin içine girip saklanabildiği yerdir; ayrıca kaynakta anılan kentten birkaç mil uzakta bulunan belirli bir eski pazar yerinin adı olarak kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yer, kişinin içine girerek görünmekten saklanmasına imkan verir."},{"facet_id":"F002","role":"specialization","statement":"Aynı biçim kaynakta anılan kent yakınındaki belirli bir eski pazar yerinin adı olarak da kullanılır."}],"identity_rationale":"Tek kaynaklı ifade hem kişinin saklanabildiği bir yeri hem de kaynakta anılan kentten birkaç mil uzaktaki belirli eski pazar yerinin adını verir; dal iki kullanımı da kapsar.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"saklanılan yer; ayrıca kaynakta belirli bir eski pazar yerinin adı"}],"lexicalization_note":"Tanım yalın saklanma yeri anlamını ve kanıttaki özel yer kullanımını korur; barınak eylemlerinin tamamına genişletilmez.","neighbor_coverage_note":"Bütün barınak, gizlenme, korku, yer ve aynı kökten adaylar değerlendirildi; mekan ile sığınağa girme eylemi ayrımı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak öncelikle mekanı adlandırır; komşu ise bu mekana girme ve orada gizlenme eylemlerini kurucu anlam olarak taşır.","focus_only":"Odak dal saklanmaya imkan veren yeri adlandırır ve ayrıca belirli bir tarihsel yer kullanımına sahiptir.","gloss":"saklanma yeri ve sığınağa girme","neighbor_only":"Komşu dal bir sığınağa girme, orada kalma ve yüzünü gizleme eylemlerini de kapsar.","neighbor_ref":"root_001324/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişinin bir örtü veya sığınak içinde görünmekten saklanması alanındadır."}],"source_phrase_ar":"المجنة اسم موضع على أميال من مكة؛ كانت مجنة وذو المجاز وعكاظ أسواقا في الجاهلية؛ المجنة أيضا الموضع الذي يستتر فيه (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Saklanma yeri anlamı ile belirli eski pazar yerinin adı aynı tek kaynakta birlikte tanıklanır."}],"source_summary":"Tek kaynak saklanılan yer anlamını, kent yakınındaki ve eski pazarlar arasında sayılan belirli bir yer adıyla birlikte verir.","sources":["SI"],"what_is_ar":"يدخل فيه المجنة اسم موضع أو الموضع الذي يستتر فيه","what_is_not_ar":"ليس المجنة بمعنى الجنون"},"support_links":[]},{"boundary":"Bu dal içeriye geçişi temel alır; gizli iç yüz, içten bozukluk ve kalıplaşmış eşlik kullanımları ayrı dallarda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000464/B001","candidate_links":[{"candidate_id":"cand_2caa272e4a2e2ed43a49","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:30:1:2","qac_word_ref":"89:30:1","surface_ar":"ٱدْخُلِ"}],"gloss":"içeri girmek veya içeri sokmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi ya da şey dışarıdaki bir konum veya durumdan içerideki konum veya duruma geçer."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ettirgen kullanım, başka bir kişi ya da şeyin içeriye geçmesini sağlamayı bildirir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Geçiş yer, zaman veya iş alanında gerçekleşebilir ve kimi kullanımda azar azar ilerleyen bir süreç olarak sunulur."}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer, zaman ya da bir işe katılma alanında dışarıdan içeriye geçişi ve bunun ettirgen karşılığını birlikte anlatmak için uygundur.","boundary_detail":"Bu dal içeriye geçişi temel alır; gizli iç yüz, içten bozukluk ve kalıplaşmış eşlik kullanımları ayrı dallarda kalır.","branch_image_ar":"الولوج إلى داخل","concept_gloss":"içeri girmek veya içeri sokmak","contextual_glosses":[{"applicability":"Bir yere veya sınırları belirli başka bir alana dışarıdan geçiş anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ettirgen içeri sokma ve zaman ya da iş alanına girme uzantılarını tek başına göstermez.","preserves":"Dışarıdan içeriye yönelen temel geçişi korur."},"facet_ids":["F001"],"text":"içeri girmek","usage_role":"general"},{"applicability":"Geçiş fiziksel bir yere değil zamansal bir evreye ya da yürütülen bir işe yöneldiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Fiziksel yer değişimini ve ettirgen kullanımı dışarıda bırakır.","preserves":"İçeri geçiş düzeninin soyut alanlara uygulanmasını korur."},"facet_ids":["F001","F003"],"text":"bir döneme veya işe girmek","usage_role":"contextual"},{"applicability":"Özne başka bir kişi ya da şeyin içeriye geçmesini sağladığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öznenin kendisinin içeri girdiği yalın kullanımı kapsamaz.","preserves":"Geçişin ettirgen ve yönlü oluşunu korur."},"facet_ids":["F002"],"text":"içeri sokmak","usage_role":"contextual"}],"definition":"Bir kişi ya da şey bir yerin, zamanın veya işin dışından içine geçer. Aynı çekirdek, bir başkasını içeri sokma ve bir şeyin içine aşamalı biçimde ilerleme yönleriyle genişler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi ya da şey dışarıdaki bir konum veya durumdan içerideki konum veya duruma geçer."},{"facet_id":"F002","role":"extension","statement":"Ettirgen kullanım, başka bir kişi ya da şeyin içeriye geçmesini sağlamayı bildirir."},{"facet_id":"F003","role":"specialization","statement":"Geçiş yer, zaman veya iş alanında gerçekleşebilir ve kimi kullanımda azar azar ilerleyen bir süreç olarak sunulur."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"İçeri geçiş bulunmayan her türlü grup üyeliğini ve ortak faaliyeti kapsar.","collision":"Sıradan birlikte hareket etme anlamıyla karışır.","fit":"broadening","loses":"Dışarıdan içeriye yönelen fiziksel geçişi ve ettirgen kullanımı siler.","preserves":"Bir işe dahil olma bağlamındaki soyut geçişi kısmen korur."},"text":"katılmak"}],"identity_rationale":"Kaynak ifadesi, temel anlamı dışarıdan içeriye geçiş olarak kuruyor; yerin yanı sıra zaman ve işe girmeyi, ayrıca bir şeyi içeri sokmayı ve aşamalı biçimde içine ilerlemeyi de bu çekirdeğe bağlıyor.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir yere, zamana veya işe girmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"içeri girme veya giriş"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"başkasını ya da bir şeyi içeri sokmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir şeyin içine azar azar girmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"girme eylemi veya giriş yeri"}],"lexicalization_note":"Tanım yalın içeri girme çekirdeğini, bir başkasını içeri sokan ettirgen kullanımdan ve özel türemiş kullanımlardan açıkça ayırır.","neighbor_coverage_note":"On yedi adayın tamamı karşılaştırıldı; çekirdeğe en yakın iki giriş dalı ile yön karşıtını gösteren dal seçildi, yalnızca aynı sahneyi paylaşan veya ayrı kardeş anlamları temsil eden adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekleri çok yakındır, ancak odak dalın kullanım alanı yer, zaman ve iş boyunca düzenlenirken komşu dal bazı özel geçit ve zaman eklenmesi örnekleriyle farklılaşır.","focus_only":"Odak dal zaman ve işe girmeyi, giriş yerini ve aşamalı ilerlemeyi de açıkça kapsar.","gloss":"içine geçme","neighbor_only":"Komşu dal dar geçitleri ve gecenin gündüze ya da gündüzün geceye eklenmesi gibi özel görünümleri öne çıkarır.","neighbor_ref":"root_001682/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin başka bir şeyin içine yönlü biçimde geçmesini temel alır."},{"boundary_match":"opposed","distinction":"Paylaşılan eksen geçiş yönüdür; odak dal içeriye, komşu dal dışarıya yönelir.","focus_only":"Odak dal sınırın dışından içine doğru geçişi bildirir.","gloss":"girme ve çıkma","neighbor_only":"Komşu dal içerideki yerden dışarı çıkmayı veya bir durumdan ayrılmayı bildirir.","neighbor_ref":"root_000400/B001","relation_type":"antonym","shared_zone":"İki dal da bir sınırın iki yanı arasında yönlü geçişi anlatır."},{"boundary_match":"partial","distinction":"Komşu dal yer ve giriş koşulu bakımından daha dardır; odak dal ise farklı alanlara taşınabilen genel geçiş çekirdeğidir.","focus_only":"Odak dal yer dışında zaman ve işe girmeyi, ayrıca ettirgen kullanımı kapsar.","gloss":"bir yere girme","neighbor_only":"Komşu dal özellikle bir eve, topluluğun yanına veya saklanma yerine girmeyi ve kimi zaman izinsizliği öne çıkarır.","neighbor_ref":"root_000487/B001","relation_type":"near_synonym","shared_zone":"Her ikisi de fiziksel bir yerin içine geçiş bağlamında kullanılabilir."}],"source_phrase_ar":"أصل مطرد منقاس وهو الولوج (maqayis)؛ دخل يدخل دخولا (maqayis)؛ ادخل في غار وتدخل فيه (ayn)؛ دخلت الدار وغيرها وأدخلت غيري (jamhara)؛ دخلت البيت وادخل وتدخل الشيء (sihah)؛ الدخول نقيض الخروج ويستعمل في المكان والزمان والأعمال (mufradat)","source_summary":"Ortak anlatım, dışarıdan içeriye yönelen geçişi esas alır; yer, zaman ve iş alanlarını, ettirgen içeri sokmayı ve aşamalı ilerlemeyi bu esasın düzenli görünümleri sayar.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الدخول في مكان أو زمان أو عمل، والإدخال والتدخل والمدخل من جهة الولوج أو الإيلاج.","what_is_not_ar":"لا يدخل فيه اسم الموضع دخول إذا أريد علما، ولا الكناية الزوجية الخاصة."},"support_links":["sup_e0ec521aea7e8ca54491"]},{"boundary":"Anlam yalnızca eşli kalıpta geçerlidir; sıradan bir yere girme veya genel evlenme anlamına genişletilemez.","branch_kind":"collocation","branch_ref":"root_000464/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:30:1:2","qac_word_ref":"89:30:1","surface_ar":"ٱدْخُلِ"}],"gloss":"eşiyle cinsel birleşmede bulunmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Erkeğin eşiyle cinsel birleşmesi örtülü bir sözle anlatılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu anlam yalnızca eşin söz diziminde açıkça yer aldığı kalıplaşmış kullanımda doğar."}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli kalıbın örtülü olarak anlattığı, erkeğin eşiyle cinsel birleşmesi bağlamında kullanılmalıdır.","boundary_detail":"Anlam yalnızca eşli kalıpta geçerlidir; sıradan bir yere girme veya genel evlenme anlamına genişletilemez.","branch_image_ar":"الإفضاء الزوجي","concept_gloss":"eşiyle cinsel birleşmede bulunmak","contextual_glosses":[{"applicability":"Cinsel birleşmenin hedef metinde de örtülü ve ölçülü biçimde anlatılması gerektiğinde doğal karşılıktır.","error_profile":{"adds":"Bağlam yetersizse cinsel olmayan beraberlik olarak da anlaşılabilir.","collision":"Gündelik olarak aynı yerde bulunma anlamıyla karışabilir.","fit":"broadening","loses":null,"preserves":"Eşler arasındaki yakın birlikteliği ve örtülü anlatımı korur."},"facet_ids":["F001","F002"],"text":"eşiyle birlikte olmak","usage_role":"contextual"}],"definition":"Belirli eşli söz kalıbı, erkeğin eşiyle cinsel birleşmesini doğrudan söylemeden anlatır. Anlam, bu kalıbın dışındaki genel girme kullanımlarına taşınmaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Erkeğin eşiyle cinsel birleşmesi örtülü bir sözle anlatılır."},{"facet_id":"F002","role":"specialization","statement":"Bu anlam yalnızca eşin söz diziminde açıkça yer aldığı kalıplaşmış kullanımda doğar."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Evlilik bağının kurulması gibi daha geniş ve farklı bir olayı ekler.","collision":"Evlilik sözleşmesi veya düğün olayıyla karışır.","fit":"displacement","loses":"Cinsel birleşmenin gerçekleşmesi ve örtülü anlatım işlevi kaybolur.","preserves":"Eşler arasındaki ilişki alanını korur."},"text":"evlenmek"}],"identity_rationale":"Kaynak ifadesi, belirli bir eşli söz dizimini erkeğin eşiyle cinsel birleşmesini örtülü biçimde anlatan bir kullanım olarak sınırlar; hazırlanan dal bu kalıp ve katılımcı sınırını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"eşiyle cinsel birleşmede bulunmak"}],"lexicalization_note":"Tanım yalnızca verilen eşli söz kalıbına bağlıdır ve bu örtülü cinsel birleşme anlamını yalın kökün genel anlamı gibi sunmaz.","neighbor_coverage_note":"On yedi adayın tamamı değerlendirildi; aynı olayı ve örtülü anlatım işlevini paylaşan üç dal seçildi, yalnızca evlilik çevresini paylaşanlar ve bu kökün başka dalları sınırı keskinleştirmediği için dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Sağlanan sınırlar katılımcı, olay ve örtülü anlatım bakımından örtüşür; kartlardaki ifade farkı ayrı bir kavramsal sınır oluşturmuyor.","focus_only":null,"gloss":"eşle cinsel birleşmeyi örtülü anlatma","neighbor_only":null,"neighbor_ref":"root_001164/B003","relation_type":"synonym","shared_zone":"Her iki dal da erkeğin eşiyle cinsel birleşmesini doğrudan söylemeden anlatır."},{"boundary_match":"partial","distinction":"Olay örtüşür, fakat odak dalın anlamı tek bir örtülü kalıba bağlıyken komşu dal daha genel ve doğrudan anlatımları da içerir.","focus_only":"Odak dal yalnızca belirli bir eşli girme kalıbının örtülü anlamıdır.","gloss":"eşler arası birleşme","neighbor_only":"Komşu dal evlenme ve cinsel birleşmeyi doğrudan karşılayan daha geniş bir söz ailesini kapsar.","neighbor_ref":"root_000259/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da eşler arasındaki cinsel birleşmeyi gösterebilir."},{"boundary_match":"partial","distinction":"İletilen olay aynı olsa da örtülü anlatımı kuran eylem ve söz kalıbı farklıdır; bu nedenle her bağlamda biçimsel olarak birbirinin yerine geçmezler.","focus_only":"Odak dal eşle girme biçimindeki belirli söz dizimine bağlıdır.","gloss":"örtülü cinsel birleşme","neighbor_only":"Komşu dal dokunma sözlerinin cinsel birleşme için örtülü kullanılmasını temel alır.","neighbor_ref":"root_001423/B002","relation_type":"near_synonym","shared_zone":"İki dal da cinsel birleşmeyi başka bir eylem üzerinden örtülü biçimde anlatır."}],"source_phrase_ar":"دخل بامرأته كناية عن الإفضاء إليها (mufradat)","source_summary":"Verilen tek tanıklık, eşle cinsel birleşmeyi doğrudan adlandırmayan ve yalnızca belirli bir söz diziminde işleyen örtülü kullanımı bildirir.","sources":["MU"],"what_is_ar":"يدخل فيه قولهم دخل بامرأته كناية عن الإفضاء إليها.","what_is_not_ar":"لا يدخل فيه مطلق دخول مكان أو مدخل."},"support_links":[]},{"boundary":"İçte veya gizli kalan yan burada kendi başına kötü değildir; kusur, aldatma ve içten bozukluk bir sonraki dalın sınırıdır.","branch_kind":"bare","branch_ref":"root_000464/B003","candidate_links":[{"candidate_id":"cand_8776312a86b2c0b3c773","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:30:1:2","qac_word_ref":"89:30:1","surface_ar":"ٱدْخُلِ"}],"gloss":"içte kalan yan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya işin dışarıdan görünmeyen iç durumu ve saklı yönü anlatılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Giysinin bedene bakan iç kenarı, aynı içte kalma ilişkisinin somut bir görünümüdür."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birine gizli bir işi açmak veya onun saklı iç yüzünü bilmek de bu iç alanla ilişkilidir."}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin veya işin görünmeyen iç yüzü ile bir nesnenin bedene ya da merkeze bakan iç yanı birlikte düşünülürken uygundur.","boundary_detail":"İçte veya gizli kalan yan burada kendi başına kötü değildir; kusur, aldatma ve içten bozukluk bir sonraki dalın sınırıdır.","branch_image_ar":"الباطن والسريرة","concept_gloss":"içte kalan yan","contextual_glosses":[{"applicability":"Kişinin eğilimi, niyeti ya da bir işin dışarıdan görünmeyen gerçek durumu anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Giysinin bedene bakan somut iç kenarını kapsamaz.","preserves":"Kişi veya işin görünmeyen iç durumunu korur."},"facet_ids":["F001","F003"],"text":"birinin veya bir işin iç yüzü","usage_role":"general"},{"applicability":"Söz konusu olan giysinin doğrudan bedene dönük olan kenarıysa tam ve doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişi ve işlerin saklı iç yüzünü dışarıda bırakır.","preserves":"Somut iç yan ile bedene yakınlık ilişkisini korur."},"facet_ids":["F002"],"text":"giysinin bedene bakan iç kenarı","usage_role":"contextual"}],"definition":"Bir kişinin, işin veya nesnenin dışarıdan görünmeyen, içeride kalan yanı söz konusudur. Bu yan kişinin iç yüzü ve saklı işleri olabileceği gibi giysinin bedene değen iç kenarı da olabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya işin dışarıdan görünmeyen iç durumu ve saklı yönü anlatılır."},{"facet_id":"F002","role":"specialization","statement":"Giysinin bedene bakan iç kenarı, aynı içte kalma ilişkisinin somut bir görünümüdür."},{"facet_id":"F003","role":"associated_use","statement":"Birine gizli bir işi açmak veya onun saklı iç yüzünü bilmek de bu iç alanla ilişkilidir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Yalnızca gizli bilgi adı olarak anlaşılabilir.","fit":"narrowing","loses":"Kişi veya işin genel iç yüzünü ve giysinin somut iç kenarını siler.","preserves":"Başkalarından saklanan bilgi yönünü korur."},"text":"sır"}],"identity_rationale":"Kaynak ifadesi kişinin veya işin görünmeyen iç yüzünü, gizli tutulan bilgiyi ve giysinin bedene bakan iç kenarını aynı içte kalma düzeninde toplar; dalın tarafsız iç yüz vurgusu bu kapsamı karşılar.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir işin veya kişinin iç yüzü"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"giysinin bedene bakan iç kenarı"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"saklı tutulan iş veya açılan gizli iç yüz"}],"lexicalization_note":"Tanım yalın dalın içte kalan yan anlamını verir; başka dallardaki kalıplaşmış veya bozukluk bildiren kullanımları buraya taşımaz.","neighbor_coverage_note":"On yedi adayın tamamı incelendi; iç yüz, gizleme ve olumsuz iç bozuklukla en açıklayıcı üç karşılaştırma seçildi, yalnızca örtme eylemini veya uzak kardeş anlamlarını paylaşan adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Soyut iç yüz alanında güçlü biçimde örtüşürler; odak dal somut iç kenara uzanırken komşu dal gizli olanı öğrenme ve bilme yönünde genişler.","focus_only":"Odak dal giysinin bedene bakan iç kenarı gibi somut bir iç yanı da kapsar.","gloss":"gizli iç yüz","neighbor_only":"Komşu dal bir şeyin iç yapısını öğrenme ve gizli olanı bilme sürecini daha açık biçimde kapsar.","neighbor_ref":"root_000128/B002","relation_type":"near_synonym","shared_zone":"Her iki dal kişi veya işin görünmeyen iç tarafını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal bir iç durum veya iç yan adıdır; komşu dal ise gizleme ve gizli iletişim eylemlerini merkez alır.","focus_only":"Odak dal gizli ya da içte kalan şeyin kendisini ve iç konumunu bildirir.","gloss":"iç yüz ve gizleme","neighbor_only":"Komşu dal bir şeyi gizleme, gizlice konuşma veya saklı biçimde iletme eylemini bildirir.","neighbor_ref":"root_000697/B001","relation_type":"near_neighbor","shared_zone":"İki dal da başkalarından görünmeyen bilgi ve iç durum alanında buluşur."},{"boundary_match":"partial","distinction":"İçte bulunma ortak olsa da odak dal tarafsızdır; komşu dal olumsuz bir kusur ya da bozulmayı zorunlu kılar.","focus_only":"Odak dal içte kalan yanı değer yargısı taşımadan anlatabilir.","gloss":"iç yüz ve içten bozukluk","neighbor_only":"Komşu dal içteki şeyin kusur, bozukluk, kuşku veya aldatma niteliği taşımasını gerektirir.","neighbor_ref":"root_000464/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal görünmeyen veya içeride bulunan bir niteliğe yönelir."}],"source_phrase_ar":"الدخلة باطن أمر الرجل وأنا عالم بدخلته (maqayis)؛ الدخلة بطانة من الأمر وعالم بدخلة أمرهم (ayn)؛ دخلل أمري إذا بثثته مكتومك (jamhara)؛ داخلة الإزار طرفه الذي يلي الجسد وداخلة الرجل باطن أمره (sihah)","source_summary":"Toplu kanıt, kişi ve işlerin saklı iç yüzünü merkeze alır; gizli bilginin açılmasını ve giysinin bedene bakan kenarını bu içte kalma ilişkisinin soyut ve somut görünümleri olarak birleştirir.","sources":["MQ","AY","JA","SI"],"what_is_ar":"يدخل فيه باطن الأمر والسريرة والدخلة والداخلة، وطرف الإزار الذي يلي الجسد، وما يطلع عليه من مكتوم الأمر.","what_is_not_ar":"لا يدخل فيه الفساد أو المكر من حيث هو عيب، إلا إذا دل السياق على الباطن فقط."},"support_links":["sup_d530d8e3c93ad64186f9"]},{"boundary":"Yalnızca içeride veya gizli olmak yetmez; bu dalda içteki nitelik kusur, bozulma, kuşku, aldatma ya da gizli düşmanlık taşımalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000464/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:30:1:2","qac_word_ref":"89:30:1","surface_ar":"ٱدْخُلِ"}],"gloss":"içten bozan kusur","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi, iş, köken veya nesnede içeride yer alan kusur ya da bozulma bulunur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İç bozukluk kuşku, hile, aldatma veya gizli düşmanlık olarak davranış ve ilişki alanına uzanır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişide zihinsel yetersizlik ya da kökende bozukluk bulunması özel bir görünüm oluşturur."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İçi çürümüş bir palmiye veya böcekçe yenmiş yiyecek, nesnedeki iç bozulmanın somut örnekleridir."}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kusurun veya bozulmanın kişi, iş, köken ya da nesnenin içinde bulunması ve dışarıdan hemen görünmemesi temel olduğunda uygundur.","boundary_detail":"Yalnızca içeride veya gizli olmak yetmez; bu dalda içteki nitelik kusur, bozulma, kuşku, aldatma ya da gizli düşmanlık taşımalıdır.","branch_image_ar":"فساد مستبطن","concept_gloss":"içten bozan kusur","contextual_glosses":[{"applicability":"Bir işte, kişide, kökende veya nesnede saklı bir kusur ve bozulma bulunduğunda genel karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aldatma ve gizli düşmanlık gibi amaçlı davranış görünümlerini açıkça belirtmez.","preserves":"İçte yer alan kusur ve bozulma çekirdeğini korur."},"facet_ids":["F001","F003","F004"],"text":"içten bozukluk","usage_role":"general"},{"applicability":"İç bozukluk antları veya güven ilişkisini aldatma aracı yapma biçiminde ortaya çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Zihinsel kusur, köken bozukluğu ve nesnelerdeki çürüme görünümlerini kapsamaz.","preserves":"Olumsuzluğun gizli ve amaçlı aldatma yönünü korur."},"facet_ids":["F002"],"text":"gizli hile ve aldatma","usage_role":"contextual"}],"definition":"Bir kişinin, soyun, işin veya şeyin içinde dışarıdan hemen görünmeyen bir kusur ya da bozulma bulunur. Bu iç bozukluk kuşku, aldatma, gizli düşmanlık, zihinsel yetersizlik, çürüme veya yenme zararı biçiminde gerçekleşebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi, iş, köken veya nesnede içeride yer alan kusur ya da bozulma bulunur."},{"facet_id":"F002","role":"extension","statement":"İç bozukluk kuşku, hile, aldatma veya gizli düşmanlık olarak davranış ve ilişki alanına uzanır."},{"facet_id":"F003","role":"specialization","statement":"Kişide zihinsel yetersizlik ya da kökende bozukluk bulunması özel bir görünüm oluşturur."},{"facet_id":"F004","role":"example","statement":"İçi çürümüş bir palmiye veya böcekçe yenmiş yiyecek, nesnedeki iç bozulmanın somut örnekleridir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Dışarıdan açıkça görülen sıradan eksikliklerle karışır.","fit":"narrowing","loses":"Kusurun içte veya gizli oluşunu, aldatma ve iç çürüme uzantılarını göstermez.","preserves":"Olumsuz eksiklik ve bozukluk yönünü korur."},"text":"kusur"}],"identity_rationale":"Kaynak ifadesi soydaki veya işteki kusurdan zihinsel bozukluğa, içten çürümüş bitkiye, bozulmuş yiyeceğe, kuşkuya ve gizli aldatmaya uzanan olumsuz bir iç bozukluk alanı kurar; hazırlanan dal bu ortak niteliği korur.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"içteki kusur, bozukluk veya kuşku"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"antları hile ve aldatma aracı yapmak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"içten kusurlu, zayıf veya zihni bozuk"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"içi çürümüş palmiye"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"böcekçe yenmiş veya kurtlanmış yiyecek"}],"lexicalization_note":"Yalın iç kusur çekirdeği, antları aldatma aracı yapma, içi çürümüş bitki ve bozulmuş yiyecek gibi kalıba bağlı özel kullanımlardan ayrı tutulur.","neighbor_coverage_note":"On yedi adayın tamamı karşılaştırıldı; iç bozulma, genel kusur ve güvene aykırı davranış sınırlarını gösteren üçü seçildi, yalnızca hile örneğini ya da başka kardeş anlamları paylaşanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bozucu iç kusurda örtüşürler; odak dal farklı taşıyıcılardaki gizli bozukluğu genişçe toplarken komşu dal arılığın bozulması çevresinde başka olumsuz niteliklere açılır.","focus_only":"Odak dal zihinsel bozukluğu, köken kusurunu, gizli aldatmayı ve nesnelerde iç çürümeyi kapsar.","gloss":"içe karışan bozukluk","neighbor_only":"Komşu dal arılığa karışan bozulmanın yanı sıra eğrilik, sertlik ve ağır sıkıntı görünümlerine uzanır.","neighbor_ref":"root_000977/B003","relation_type":"near_synonym","shared_zone":"Her iki dal bir şeyin iç bütünlüğünü bozan kusur veya bozulmayı anlatır."},{"boundary_match":"partial","distinction":"Komşu dal genel kusur alanıdır; odak dal ise kusuru içte bulunma ve içeriden bozma ilişkisiyle sınırlar.","focus_only":"Odak dal kusurun içeride, saklı veya içten bozucu olmasını gerektirir.","gloss":"iç kusur ve genel kusur","neighbor_only":"Komşu dal görünür ya da görünmez her türlü eksiklik, eleştiri noktası, suçlama ve zayıflığı kapsar.","neighbor_ref":"root_001106/B003","relation_type":"near_neighbor","shared_zone":"İki dal da eksiklik ve bozukluk değerlendirmesi taşır."},{"boundary_match":"field_only","distinction":"Odak dalın çekirdeği iç kusurdur; komşu dalın çekirdeği kişinin güvene aykırı davranışı olduğundan sıradan kullanımda birbirlerinin yerine geçmezler.","focus_only":"Odak dal kusur, bozulma, kuşku ve çürümeyi davranış dışındaki taşıyıcılarda da kapsar.","gloss":"gizli bozukluk ve ihanet","neighbor_only":"Komşu dal özellikle kişiyi hain sayan bir niteleme ve bağlılık karşısındaki ihanet üzerinde durur.","neighbor_ref":"root_000841/B005","relation_type":"same_field","shared_zone":"Her iki dal güveni zedeleyen gizli olumsuzluk alanında buluşabilir."}],"source_phrase_ar":"الدخل العيب في الحسب وكالدغل (maqayis)؛ دخل فلان وهو مدخول إذا كان في عقله دخل ونخلة مدخولة عفنة الجوف (maqayis)؛ عيب في الحسب وفي هذا الأمر دخل ودغل ودخل حسبه أو عقله (ayn)؛ في أمره دخل أي فساد (jamhara)؛ الدخل العيب والريبة ومكرا وخديعة ومدخول في عقله ونخلة مدخولة (sihah)؛ الدخل كناية عن الفساد والعداوة المستبطنة كالدغل ومدخول كناية عن بله في عقله وفساد في أصله (mufradat)","source_summary":"Toplu anlatım, içeride bulunan olumsuz kusuru ortak çekirdek sayar; soy ve akıldaki bozukluğu, işteki kuşkuyu, aldatmayı, gizli düşmanlığı, iç çürümeyi ve yiyecek zararını bu çekirdeğin farklı görünümleri olarak sıralar.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الدخل بمعنى العيب والفساد والدغل والريبة والمكر والخديعة والعداوة المستبطنة، وما وصف بمدخول لخلل في العقل أو الأصل أو الجوف أو الطعام.","what_is_not_ar":"لا يدخل فيه مجرد السريرة الباطنة بلا عيب، ولا مجرد الانتساب الداخل بلا فساد."},"support_links":[]},{"boundary":"Kişi veya topluluk ilişkisine sonradan girme esastır; mali gelir ve iç kusur anlamları bu dala ait değildir.","branch_kind":"bare","branch_ref":"root_000464/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:30:1:2","qac_word_ref":"89:30:1","surface_ar":"ٱدْخُلِ"}],"gloss":"sonradan araya katılan kimse","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi başka birinin özel işlerine veya köken bakımından ait olmadığı bir topluluğa girer."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Topluluğa katılma, gerçek kökenden değil sonradan kurulan bir bağlılıktan doğar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bilmediği işlere kendini sokan kişi, araya girmenin uygunsuz ve gösterişli biçimini temsil eder."}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin özel işlerine alınan, bir topluluğa dışarıdan bağlanan veya bilmediği işe kendini sokan kişi için kullanılabilir.","boundary_detail":"Kişi veya topluluk ilişkisine sonradan girme esastır; mali gelir ve iç kusur anlamları bu dala ait değildir.","branch_image_ar":"دخيل يخالط القوم أو الأمر","concept_gloss":"sonradan araya katılan kimse","contextual_glosses":[{"applicability":"Kişinin bir topluluğun gerçek kökeninden gelmediği halde ona bağlanması anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir kişinin özel işlerine alınma ve bilgisizce işe karışma görünümlerini kapsamaz.","preserves":"Dışarıdan gelme ve topluluğa sonradan bağlanma yönünü korur."},"facet_ids":["F001","F002"],"text":"topluluğa dışarıdan katılmış kimse","usage_role":"contextual"},{"applicability":"Kişi yeterli bilgisi olmadığı halde bir işi sahiplenerek araya girdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yakın sırdaş ve topluluğa sonradan bağlanan kişi anlamlarını dışarıda bırakır.","preserves":"Uygunsuz biçimde işe aradan girme yönünü korur."},"facet_ids":["F003"],"text":"bilmediği işe zorla karışan kimse","usage_role":"contextual"}],"definition":"Bir kimse, başka bir kişinin özel işlerine alınır veya köken olarak kendilerinden olmadığı bir topluluğa katılır. Bilgisi olmadığı halde işlere zorla karışan kişi de aynı araya girme düzeninin olumsuz bir görünümüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi başka birinin özel işlerine veya köken bakımından ait olmadığı bir topluluğa girer."},{"facet_id":"F002","role":"specialization","statement":"Topluluğa katılma, gerçek kökenden değil sonradan kurulan bir bağlılıktan doğar."},{"facet_id":"F003","role":"associated_use","statement":"Bilmediği işlere kendini sokan kişi, araya girmenin uygunsuz ve gösterişli biçimini temsil eder."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Hiçbir ilişki kurmamış tanınmayan kişiyle karışır.","fit":"narrowing","loses":"Topluluğa veya kişinin özel işlerine gerçekten katılmış olma ilişkisini siler.","preserves":"Topluluğun asıl kökeninden gelmeme yönünü korur."},"text":"yabancı"}],"identity_rationale":"Kaynak ifadesi hem bir kişinin özel işlerine alınan kimseyi hem de köken olarak kendilerinden olmadığı halde bir topluluğa katılanı, ayrıca bilmediği işe zorla karışanı anlatır; dal bu sonradan araya girme bağını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"özel işlere alınan veya bir topluluğa dışarıdan katılan kimse"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"kişinin özel işlerine aldığı yakın kimse"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bilmediği işlere zorla karışan kimse"}],"lexicalization_note":"Tanım, kişi ve topluluk ilişkisine giren kimseyi yalın dal olarak açıklar; bozuk soy yargısını veya başka kalıplara bağlı anlamları kendiliğinden eklemez.","neighbor_coverage_note":"On yedi adayın tümü değerlendirildi; dışarıdan topluluğa bağlanma ve araya girme sınırlarını en iyi gösteren üçü seçildi, yalnızca akrabalık alanını veya başka kardeş dalları paylaşanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Topluluğa dışarıdan katılma alanında örtüşürler; odak dal daha tarafsız ve ilişki bakımından geniş, komşu dal ise damgalayıcı ve soy bağına daha sıkı bağlıdır.","focus_only":"Odak dal bir kişinin özel işlerine alınan yakın kimseyi ve bilgisizce işe karışanı da kapsar.","gloss":"topluluğa dışarıdan eklenen kimse","neighbor_only":"Komşu dal topluluğa yapıştırılmış kişinin kötü tanınması ve düşük görülmesi gibi olumsuz değerlendirmeleri de taşır.","neighbor_ref":"root_000647/B002","relation_type":"near_synonym","shared_zone":"Her iki dal köken olarak topluluktan olmadığı halde ona bağlanan kişiyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal bağlı kişinin durumunu daha geniş ilişkilerle anlatır; komşu dal ise bağlama veya soy iddiası kurma işlemini merkez alır.","focus_only":"Odak dal kişinin özel işlerine girme ve bilmediği işe karışma görünümlerini de içerir.","gloss":"sonradan topluluğa bağlanma","neighbor_only":"Komşu dal birini bir topluluğa veya gerçek babasından başkasına bağlama eylemini öne çıkarır.","neighbor_ref":"root_001347/B002","relation_type":"near_synonym","shared_zone":"İki dal da gerçek kökenden farklı bir topluluğa sonradan bağlanma durumunu kapsar."},{"boundary_match":"field_only","distinction":"Odak dalın katılma ilişkisi tarafsız veya yakın olabilir; komşu dalda çıkarcılık ve istenmeme belirleyicidir.","focus_only":"Odak dal dışarıdan katılan kişinin yakın ve kabul edilmiş olmasına da izin verir.","gloss":"araya katılan ve asalak","neighbor_only":"Komşu dal topluluğun işine çıkar için sızan asalak ve istenmeyen kişiyi zorunlu kılar.","neighbor_ref":"root_001216/B009","relation_type":"same_field","shared_zone":"Her iki dal bir gruba dışarıdan giren kişiyi konu eder."}],"source_phrase_ar":"دخيلك الذي يداخلك في أمورك وبنو فلان في بني فلان دخيل (maqayis)؛ دخيلك الذي تدخله في أمورك ودخلل والمتدخل في الأمور المتكلف فيها (ayn)؛ فلان دخيل في بني فلان إذا كان من غيرهم (jamhara)؛ هم دخل في بني فلان ودخيل الرجل ودخلله الذي يداخله في أموره (sihah)؛ وعن الدعوة في النسب (mufradat)","source_summary":"Toplu kanıt, dışarıdan gelip bir kişinin özel işlerine veya bir topluluğun bağına giren kimseyi ortaklaştırır; sonradan soy bağı iddiasını ve bilgisizce işe karışmayı bu ilişkinin özel görünümleri olarak verir.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الدخيل والدخلل ومن يداخل الشخص في أموره، والقوم المنتسبون في غيرهم، والمتدخل المتكلف في الأمور.","what_is_not_ar":"لا يدخل فيه الدخل المالي ولا العيب إلا إذا صرح بفساد النسب أو الأصل."},"support_links":[]},{"boundary":"Bu dal parasal veya mal niteliğindeki girişi anlatır; genel içeri girme ile gizli kusur anlamlarını kapsamaz.","branch_kind":"bare","branch_ref":"root_000464/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:30:1:2","qac_word_ref":"89:30:1","surface_ar":"ٱدْخُلِ"}],"gloss":"gelir","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kazanç veya getiri olarak kişinin mülküne ya da işine giren mal anlatılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu mali giriş, hesap düzeninde dışarı çıkan malın karşıtı olarak belirlenir."}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi, mülk veya iş bakımından içeri giren kazanç ve bunun gider karşıtı oluşu anlatıldığında tam karşılıktır.","boundary_detail":"Bu dal parasal veya mal niteliğindeki girişi anlatır; genel içeri girme ile gizli kusur anlamlarını kapsamaz.","branch_image_ar":"ما يدخل من كسب","concept_gloss":"gelir","contextual_glosses":[{"applicability":"Tarihsel mülk veya işletme bağlamında mali girişin açıkça anlatılması gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek başına kullanıldığında gider karşıtlığını doğrudan belirtmez.","preserves":"Kazancın bir işe veya mülke girişini açıkça korur."},"facet_ids":["F001"],"text":"işletmeye giren kazanç","usage_role":"explanatory"}],"definition":"Bir kişinin mülküne veya yürüttüğü işe kazanç ya da getiri olarak giren maldır. Hesap ilişkisinde dışarı çıkan malın karşı kutbunu oluşturur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kazanç veya getiri olarak kişinin mülküne ya da işine giren mal anlatılır."},{"facet_id":"F002","role":"specialization","statement":"Bu mali giriş, hesap düzeninde dışarı çıkan malın karşıtı olarak belirlenir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Henüz tahsil edilmemiş değer artışı veya genel başarıyla karışabilir.","fit":"narrowing","loses":"Değerin mülke giren akış ve giderin karşıtı olma yönünü zayıflatır.","preserves":"Elde edilen mali değeri korur."},"text":"kazanç"}],"identity_rationale":"Kaynak ifadesi, kişinin mülküne veya işletmesine kazanç olarak giren şeyi ve bunun dışarı çıkan malın karşıtı oluşunu açıkça bildirir; hazırlanan mali giriş dalı bu iki unsuru korur.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"gelir veya içeri giren kazanç"}],"lexicalization_note":"Tanım, yalın mali giriş ve gelir anlamıyla sınırlıdır; kazancın özel elde edilme yollarını veya başka dalların kullanımlarını eklemez.","neighbor_coverage_note":"On yedi adayın tamamı karşılaştırıldı; gelir-gider karşıtını, kazanma eylemini ve ticari artışı ayıran üçü seçildi, fiyat, mal edinme ve genel geçim alanındaki daha uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Paylaşılan mali akış ekseninde yönleri karşıttır; odak dal giriş, komşu dal çıkış tarafıdır.","focus_only":"Odak dal mülke veya işe giren mali değeri bildirir.","gloss":"gelir ve gider","neighbor_only":"Komşu dal belirli bir amaçla dışarı çıkarılan malı bildirir.","neighbor_ref":"root_000400/B003","relation_type":"antonym","shared_zone":"İki dal aynı mali hesabın içeri ve dışarı yönlü akışlarını gösterir."},{"boundary_match":"partial","distinction":"Odak dal sonuçta oluşan mali giriştir; komşu dal bu değeri elde etme eylemidir.","focus_only":"Odak dal elde edilmiş değerin içeri giren mali kalem oluşunu bildirir.","gloss":"gelir ve kazanma","neighbor_only":"Komşu dal malı kazanma veya kazanca ulaşma eylemini bildirir.","neighbor_ref":"root_000580/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal ekonomik değer ve kazanç alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal genel mali giriştir; komşu dal özellikle alım satım sonucundaki artışı anlatır.","focus_only":"Odak dal kaynağı ne olursa olsun içeri giren kazanç kalemini kapsar.","gloss":"gelir ve ticaret artısı","neighbor_only":"Komşu dal alışveriş ve ticaret sonunda oluşan artışla sınırlıdır.","neighbor_ref":"root_000533/B001","relation_type":"near_neighbor","shared_zone":"Ticari artış bir işin gelirine dönüşebildiği için iki alan kesişebilir."}],"source_phrase_ar":"الدخل ما دخل ضيعة الإنسان من المنالة (ayn)؛ الدخل خلاف الخرج (sihah)","source_summary":"Kanıt, kişinin mülküne kazanç olarak giren malı ortak çekirdek sayar ve onu dışarı çıkan malın karşısına yerleştirir.","sources":["AY","SI"],"what_is_ar":"يدخل فيه الدخل بمعنى مقابل الخرج، وما يدخل ضيعة الإنسان من المنالة.","what_is_not_ar":"لا يدخل فيه الدخول المكاني ولا الدخل بمعنى الفساد."},"support_links":[]},{"boundary":"Bu dal genel sulama değil, develerin su başındaki ikinci girişini veya sürüye aradan katılarak içmesini düzenleyen özel işlemdir.","branch_kind":"bare","branch_ref":"root_000464/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:30:1:2","qac_word_ref":"89:30:1","surface_ar":"ٱدْخُلِ"}],"gloss":"develeri yeniden ya da araya katarak sulama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Su içmiş develer ikinci kez su başına döndürülerek yeniden içirilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Susuz develer henüz içmemiş develerin arasına katılır ve onlarla birlikte içmeleri sağlanır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başka bir görünümde sürü, aralarında sıkışıklık olacak biçimde bir kerede su başına sürülür."}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Develerin ikinci kez su başına götürülmesi veya susuz hayvanların içen sürünün arasına katılması anlatıldığında kullanılmalıdır.","boundary_detail":"Bu dal genel sulama değil, develerin su başındaki ikinci girişini veya sürüye aradan katılarak içmesini düzenleyen özel işlemdir.","branch_image_ar":"إدخال الإبل في الشرب مرة أخرى","concept_gloss":"develeri yeniden ya da araya katarak sulama","contextual_glosses":[{"applicability":"Sürü daha önce içmişken yeniden su başına döndürülüyorsa bu açık karşılık kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Susuz hayvanları başka develerin arasına katma ve tek seferlik sıkışık sulama çeşitlerini kapsamaz.","preserves":"Develerin yeniden su başına götürülmesi işlemini korur."},"facet_ids":["F001"],"text":"develeri ikinci kez suya götürmek","usage_role":"contextual"},{"applicability":"İkinci içişin, susuz hayvanların öteki develerin arasına sokulmasıyla sağlandığı durumda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bütün sürüyü yeniden suya döndürme ve sıkışık biçimde bir kerede sürme çeşitlerini dışarıda bırakır.","preserves":"Susuz deveyi sürü arasına katma ve içmesini sağlama yönünü korur."},"facet_ids":["F002"],"text":"susuz develeri içen sürünün arasına katmak","usage_role":"explanatory"}],"definition":"Develer su içtikten sonra yeniden su başına götürülür veya susuz develer içmekte olanların arasına katılarak ikinci kez içmeleri sağlanır. Bir kaynak anlatımı, sürünün bir kerede sıkışık biçimde suya sürülmesini de aynı düzenin başka bir yüzü sayar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Su içmiş develer ikinci kez su başına döndürülerek yeniden içirilir."},{"facet_id":"F002","role":"specialization","statement":"Susuz develer henüz içmemiş develerin arasına katılır ve onlarla birlikte içmeleri sağlanır."},{"facet_id":"F003","role":"source_variant","statement":"Başka bir görünümde sürü, aralarında sıkışıklık olacak biçimde bir kerede su başına sürülür."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Her hayvanı ve her türlü su verme işlemini kapsar.","collision":"Sıradan ilk sulama işlemiyle karışır.","fit":"broadening","loses":"İkinci kez götürme veya sürünün arasına katma düzenini siler.","preserves":"Hayvana su içirme amacını korur."},"text":"sulamak"}],"identity_rationale":"Kaynak ifadesi develerin içtikten sonra yeniden su başına götürülmesini temel görünüm olarak verir; ayrıca susuz develeri henüz içmemiş olanların arasına katma ve sürüyü bir kerede sıkışık biçimde sulama çeşitlemelerini de açıkça kaydeder.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"develeri ikinci kez suya götürme veya susuz deveyi sürüye katma"}],"lexicalization_note":"Tanım, yalın dalın deve sulama düzenini verir ve bu özel hayvancılık anlamını genel içeri girme ya da her türlü sulama anlamına genişletmez.","neighbor_coverage_note":"On yedi adayın tamamı değerlendirildi; su başından geçirme, suya doyma ve sırada bekleme ile en açıklayıcı üç sınır seçildi, gün aralığına dayalı sulama adları ve uzak kardeş dallar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın amacı ve sonucu içmedir; komşu dalda temel işlem yalnızca su yalağı boyunca geçirmektir.","focus_only":"Odak dal develeri ikinci kez içirmek veya susuz deveyi içenlerin arasına katmak için su başına sokar.","gloss":"yeniden içirme ve su başından geçirme","neighbor_only":"Komşu dal develeri su yalağının yanından ya da üzerinden geçirmekle sınırlıdır ve içirme sonucu gerektirmez.","neighbor_ref":"root_000867/B010","relation_type":"near_neighbor","shared_zone":"Her iki dal develerin su yalağı çevresindeki yönlendirilmesini anlatır."},{"boundary_match":"field_only","distinction":"Odak dal düzenleme işlemidir; komşu dal ise içmenin tamamlanıp hayvanın suya doyması sonucudur.","focus_only":"Odak dal sürünün suya hangi sırayla veya kaçıncı kez sokulduğunu düzenler.","gloss":"sulama düzeni ve suya doyma","neighbor_only":"Komşu dal develerin yeterince su içmiş ve susuzluğunu gidermiş olma sonucunu bildirir.","neighbor_ref":"root_001509/B004","relation_type":"same_field","shared_zone":"İki dal deve sulama sürecinin farklı yönlerini konu eder."},{"boundary_match":"partial","distinction":"Odak dalda araya sokma veya geri döndürme vardır; komşu dalda hayvanlar sıranın açılmasını bekler.","focus_only":"Odak dal susuz develerin içenlerin arasına etkin biçimde katılmasını veya yeniden götürülmesini bildirir.","gloss":"araya katma ve sırada bekleme","neighbor_only":"Komşu dal su başındaki içenlerin arkasında bekleyip onların ayrılmasından sonra girecek develeri adlandırır.","neighbor_ref":"root_000851/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal bazı develerin su başındaki başka develere göre konumunu ve içme sırasını düzenler."}],"source_phrase_ar":"الدخال في الورد أن تشرب الإبل ثم ترد إلى الحوض (maqayis)؛ سقيت الإبل دخالا إذا حملتها على الحوض ثانية والدخال في وجه آخر أن تحملها على الحوض بمرة واحدة عراكا (ayn)؛ أورد الرجل إبله دخالا (jamhara)؛ الدخال في الورد أن يشرب البعير ثم يرد من العطن إلى الحوض (sihah)؛ الدخال في الإبل أن يدخل إبل في أثناء ما لم تشرب لتشرب معها ثانيا (mufradat)","source_summary":"Toplu anlatım, develeri su başına yeniden sokarak içirmeyi merkez alır; susuz hayvanları sürünün arasına katma ile sürüyü bir kerede sıkışık götürme biçimlerini aynı ad altında farklı uygulamalar olarak korur.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الدخال في الورد: أن ترد الإبل إلى الحوض ثانية أو يدخل بعير عطشان بين بعيرين ليتم شربه، وكذلك إيرادها عراكا في وجه آخر.","what_is_not_ar":"لا يدخل فيه مطلق الدخول ولا الدخل المالي."},"support_links":[]},{"boundary":"Dal, parçaların birbirine geçmesi veya başka parçaların arasında kalmasıyla sınırlıdır; küçük kuş adı ve örme kap adı ayrı dallardır.","branch_kind":"bare","branch_ref":"root_000464/B008","candidate_links":[{"candidate_id":"cand_52184e28b0f598806e3a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:30:1:2","qac_word_ref":"89:30:1","surface_ar":"ٱدْخُلِ"}],"gloss":"iç içe geçme ve arada kalma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir parçanın başka parçaların arasına girmesi veya onlarla iç içe birleşmesi temel ilişkidir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eklemlerin birbirine geçmesi ve etin bir sinir üzerinde toplanması yapısal örneklerdir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir ana rengin içinde başka renklerin dağınık biçimde bulunması görsel alandaki uzantıdır."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kuşun sırtıyla karnı arasındaki tüyler ve ağaç kökleri arasına giren ot, ara konum örnekleridir."}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Parçalar birbirine geçtiğinde, bir çekirdek çevresinde toplandığında veya iki bölüm arasındaki iç konumu doldurduğunda uygundur.","boundary_detail":"Dal, parçaların birbirine geçmesi veya başka parçaların arasında kalmasıyla sınırlıdır; küçük kuş adı ve örme kap adı ayrı dallardır.","branch_image_ar":"تداخل الأجزاء وما بين الداخل","concept_gloss":"iç içe geçme ve arada kalma","contextual_glosses":[{"applicability":"Eklemler veya başka yapısal parçalar birbirinin arasına girerek bağlandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Renk karışımını ve iki bölge arasında bulunan tüy ya da ot örneklerini kapsamaz.","preserves":"Yapısal iç içe geçme ve birleşme ilişkisini korur."},"facet_ids":["F001","F002"],"text":"parçaların birbirine geçmesi","usage_role":"general"},{"applicability":"Tek bir ana görünüm içinde başka renkler dağınık biçimde bulunduğunda açıklayıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eklemler, et, tüy ve otla ilgili yapısal örnekleri dışarıda bırakır.","preserves":"Renk parçalarının ana renk içinde yer almasını korur."},"facet_ids":["F003"],"text":"bir rengin içine başka renklerin karışması","usage_role":"contextual"},{"applicability":"Tüy veya ot gibi bir parça iki bölgenin arasında ya da başka yapıların kökünde yer aldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Karşılıklı geçme ve renklerin birbirine karışması süreçlerini göstermez.","preserves":"Parçanın içteki ara konumunu korur."},"facet_ids":["F004"],"text":"iki bölüm arasında kalan parça","usage_role":"explanatory"}],"definition":"Parçalar birbirinin arasına girerek birleşir, bir ana bölüm çevresinde toplanır veya iki bölüm arasında yer alır. Bu düzen eklem, et, renk, tüy ve bitki örtüsü gibi farklı maddelerde görülebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir parçanın başka parçaların arasına girmesi veya onlarla iç içe birleşmesi temel ilişkidir."},{"facet_id":"F002","role":"example","statement":"Eklemlerin birbirine geçmesi ve etin bir sinir üzerinde toplanması yapısal örneklerdir."},{"facet_id":"F003","role":"extension","statement":"Bir ana rengin içinde başka renklerin dağınık biçimde bulunması görsel alandaki uzantıdır."},{"facet_id":"F004","role":"example","statement":"Kuşun sırtıyla karnı arasındaki tüyler ve ağaç kökleri arasına giren ot, ara konum örnekleridir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Düzensiz birleşme, bulanma ve toplumsal müdahale gibi ilgisiz anlamları kapsar.","collision":"Genel karışıklık veya bir işe müdahale anlamıyla karışır.","fit":"broadening","loses":"Birbirinin arasına girme, belirli bir çevrede toplanma ve ara konum ayrımlarını siler.","preserves":"Renklerin veya parçaların bir arada bulunma yönünü kısmen korur."},"text":"karışmak"}],"identity_rationale":"Kaynak ifadesi eklemlerin birbirine geçmesini, sinir çevresinde toplanan eti, bir renge karışan başka renkleri ve iki bölge arasında veya ağaç köklerinde kalan tüy ile otu ortak bir iç içelik ve ara konum düzeninde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"eklemlerin birbirine geçmesi"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir sinir üzerinde toplanmış et parçası"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bir ana renge karışmış başka renkler"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kuşun sırtıyla karnı arasındaki tüyler"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"ağaç köklerinin arasına girmiş ot"}],"lexicalization_note":"Tanım yalın iç içelik ve ara konum dalını açıklar; özel kuş ve kap adlarını ya da kalıba bağlı başka kullanımları buraya taşımaz.","neighbor_coverage_note":"On yedi adayın tamamı değerlendirildi; genel karışma, basınçlı iç içe geçme ve renk ayrımıyla üç yararlı sınır seçildi, yalnızca benzer maddi örnekleri veya uzak kardeş anlamlarını paylaşanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal iç yapı ve ara konumu ayrıntılandırır; komşu dal ise iki taraflı karışma ilişkisini örnek sınırı koymadan verir.","focus_only":"Odak dal yapısal geçme, ara konum, renk dağılımı ve belirli maddi örnekleri kapsar.","gloss":"iç içelik ve karşılıklı karışma","neighbor_only":"Komşu dal iki tarafın karşılıklı karışmasını genel ve daha soyut biçimde bildirir.","neighbor_ref":"root_000370/B006","relation_type":"near_synonym","shared_zone":"Her iki dal iki veya daha çok unsurun birbirinin alanına girmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dalın belirleyicisi iç konumdur; komşu dalda buna ek olarak güçlü baskı ve sıkışıklık zorunludur.","focus_only":"Odak dalda iç içelik baskı bulunmadan da oluşabilir ve renk, tüy veya ot gibi örneklere uzanır.","gloss":"iç içe geçme ve sıkışma","neighbor_only":"Komşu dal parçaların güçlü basınç altında sıkıca birbirine girmesini gerektirir.","neighbor_ref":"root_000495/B002","relation_type":"near_neighbor","shared_zone":"İki dal da parçaların birbirinin arasına girip yakın bağ kurmasını anlatabilir."},{"boundary_match":"field_only","distinction":"Odak dal renklerin ana renk içine karışmasını genel iç içelik düzenine bağlar; komşu dal ise belirli canlılardaki iki renkli veya çizgili görünüşü adlandırır.","focus_only":"Odak dal renk dışında eklem, et, tüy ve bitki parçalarındaki iç konumu da kapsar.","gloss":"renk karışımı ve iki renkli görünüş","neighbor_only":"Komşu dal hayvan ve bitkilerde iki rengin ayrımlı görünüşünü ve çizgili yapıyı merkez alır.","neighbor_ref":"root_000421/B004","relation_type":"same_field","shared_zone":"Her iki dal tek bir görünümde birden çok rengin bulunmasını konu edebilir."}],"source_phrase_ar":"كل لحمة مجتمعة دخلة والدخل من ريش الطائر ما بين الظهران والبطنان والدخل من الكلأ ما دخل منه في أصول الشجر (maqayis)؛ الدخلة في اللون تحليط من ألوان في لون والدخال مداخلة المفاصل بعضها في بعض (ayn)؛ كل لحمة مجتمعة على عصب فهي دخلة (jamhara)؛ الدخل من الكلأ ما دخل منه في أصول الشجر (sihah)","source_summary":"Toplu kanıt, parçaların iç içe geçmesi ve arada yer alması düzenini eklem, sinir çevresindeki et, renk karışımı, kuş tüyleri ve ağaç köklerindeki ot üzerinden farklı maddi görünümlerle açıklar.","sources":["MQ","AY","JA","SI"],"what_is_ar":"يدخل فيه مداخلة المفاصل، واللحمة المجتمعة على عصب، والدخلة في اللون، وريش ما بين الظهر والبطن، والكلأ الداخل في أصول الشجر.","what_is_not_ar":"لا يدخل فيه الطائر المسمى دخلا ولا الوعاء الدوخلة."},"support_links":["sup_e612bf358beccf576d7a"]},{"boundary":"Bu dal belirli küçük kuş adıdır; her küçük kuşa, kuşun yaşadığı çalılığa veya örme kaba genellenemez.","branch_kind":"bare","branch_ref":"root_000464/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:30:1:2","qac_word_ref":"89:30:1","surface_ar":"ٱدْخُلِ"}],"gloss":"sık ağaçlıkta barınan küçük kuş","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir küçük kuş ve bu kuşun oyuklar ile sık ağaç altlarındaki barınma alanı anlatılır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuş adının, hayvanın sık ağaçların arasına girme davranışından doğduğu açıklanır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kuş adının iki farklı çoğul biçimi aktarılır."}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Adı bilinmeyen genel bir kuş türü gibi değil, kanıtta oyuk ve sık ağaçlık yaşamıyla tanımlanan belirli küçük kuş için kullanılmalıdır.","boundary_detail":"Bu dal belirli küçük kuş adıdır; her küçük kuşa, kuşun yaşadığı çalılığa veya örme kaba genellenemez.","branch_image_ar":"طائر يدخل الغيران والشجر","concept_gloss":"sık ağaçlıkta barınan küçük kuş","contextual_glosses":[{"applicability":"Tür adının hedef dilde yerleşik bir karşılığı verilmeden yaşam alanıyla açıklanması gerektiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Adın içeri girme davranışından türetilmesi ve çoğul biçimleri açıklamada görünmez.","preserves":"Kuşun küçüklüğünü ve oyuklarla sık bitki örtüsündeki yaşamını korur."},"facet_ids":["F001"],"text":"oyuklarda ve çalılıkta yaşayan küçük kuş","usage_role":"explanatory"}],"definition":"Oyuklarda, vadi içlerinde ve sık ağaçların altında barınan belirli bir küçük kuştur. Adı, sık ağaçların arasına girmesiyle açıklanır ve iki ayrı çoğul biçimi vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir küçük kuş ve bu kuşun oyuklar ile sık ağaç altlarındaki barınma alanı anlatılır."},{"facet_id":"F002","role":"source_variant","statement":"Kuş adının, hayvanın sık ağaçların arasına girme davranışından doğduğu açıklanır."},{"facet_id":"F003","role":"source_variant","statement":"Kuş adının iki farklı çoğul biçimi aktarılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kanıtın belirlemediği ayrı bir kuş türü kimliği ekler.","collision":"Bilinen serçe türleriyle yanlış özdeşlik kurar.","fit":"displacement","loses":"Oyuk ve sık ağaçlık yaşam alanını, içeri girme açıklamasını ve özgül adı siler.","preserves":"Küçük bir kuş olma yönünü korur."},"text":"serçe"}],"identity_rationale":"Kaynak ifadesi, oyuklarda, vadi içlerinde ve sık ağaçların altında barınan küçük bir kuş adını verir; adın kuşun sık ağaçların arasına girmesiyle açıklanmasını ve iki çoğul biçimini de kaydeder.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"oyuklarda ve sık ağaç altında barınan küçük kuş"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"bu küçük kuş adının bir çoğul biçimi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bu küçük kuş adının öteki çoğul biçimi"}],"lexicalization_note":"Tanım yalın dalda kaydedilen kuş adını ve onun çoğullarını verir; yaşam alanını ayrı bir bitki anlamına dönüştürmez.","neighbor_coverage_note":"On yedi adayın tamamı karşılaştırıldı; başka bir küçük kuş, farklı özellikte bir kuş ve yaşam alanı olan sık koruluk seçildi, avlanma, başka kuş türleri ve uzak kardeş dallar ek sınır sağlamadığı için elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Küçüklük ortak bir niteliktir, fakat adlandırılan kuşlar ve onları belirleyen özellikler ayrıdır; birbirlerinin yerine kullanılamazlar.","focus_only":"Odak dal oyuk ve sık ağaç altında barınmayı ve içeri girme davranışıyla açıklanan adı içerir.","gloss":"iki küçük kuş adı","neighbor_only":"Komşu dal yalnızca başka bir adla anılan, serçeden de küçük ayrı bir kuşu bildirir.","neighbor_ref":"root_000187/B007","relation_type":"near_neighbor","shared_zone":"Her iki dal belirli bir küçük kuş adını verir."},{"boundary_match":"field_only","distinction":"Ortak alan kuş adlarıdır; boyut, yaşam alanı ve benzetilen kuş farklı olduğundan kavramsal çekirdekleri örtüşmez.","focus_only":"Odak dal küçük oluş, oyuk ve sık ağaçlık yaşamı ile tanımlanır.","gloss":"küçük kuş ve güvercine benzeyen kuş","neighbor_only":"Komşu dal yüksek bölgelerde yaşayan ve güvercine benzeyen başka bir kuşu bildirir.","neighbor_ref":"root_001066/B009","relation_type":"same_field","shared_zone":"İki dal da görünüş veya yaşam alanıyla açıklanan kuş adlarıdır."},{"boundary_match":"thematic_only","distinction":"Bağ yalnızca yaşam alanı düzeyindedir; biri kuş, öteki bitki örtüsü olduğu için anlam bakımından birbirlerinin yerine geçmezler.","focus_only":"Odak dal sık ağaçların arasında barınan kuşun kendisini adlandırır.","gloss":"çalılık kuşu ve sık koruluk","neighbor_only":"Komşu dal çok ve birbirine geçmiş ağaçlardan oluşan koruluğu adlandırır.","neighbor_ref":"root_000072/B001","relation_type":"thematic","shared_zone":"Sık ve birbirine geçmiş ağaçlık, odak kuşunun barınma sahnesini oluşturabilir."}],"source_phrase_ar":"بذلك سمي هذا الطائر دخلا (maqayis)؛ الدخل صغار الطير مأواها الغيران وبطون الأودية تحت شجر ملتف والجميع الدخاخيل (ayn)؛ الدخل طائر صغير وجمع دخل دخاخيل (jamhara)؛ الدخل طائر صغير والجمع الدخاليل (sihah)؛ الدخل طائر سمي بذلك لدخوله فيما بين الأشجار الملتفة (mufradat)","source_summary":"Toplu anlatım küçük bir kuşu, onun oyuk ve sık ağaç altı yaşam alanını, adın ağaçların arasına girme davranışıyla açıklanmasını ve iki çoğul biçimini birlikte kaydeder.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الدخل اسم الطائر الصغير، وجمعه دخاخيل أو دخاليل، مع تعليل دخوله بين الأشجار الملتفة.","what_is_not_ar":"لا يدخل فيه كل طائر صغير إذا لم يسم دخلا، ولا الوعاء الدوخلة."},"support_links":[]},{"boundary":"Bu dal belirli küçük örme kaptır; genel sepet, deri kap, kuş adı veya yalın içeri girme anlamına genişletilemez.","branch_kind":"bare","branch_ref":"root_000464/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:30:1:2","qac_word_ref":"89:30:1","surface_ar":"ٱدْخُلِ"}],"gloss":"taze palmiye meyvesi için küçük örgü sepet","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kap, palmiye yaprağından örülmüş küçük bir taşıma veya saklama nesnesidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kabın özgül kullanımı, içine taze palmiye meyvesi koymaktır."}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Palmiye yaprağından örülmüş ve özellikle taze palmiye meyvesi koymak için kullanılan küçük kap anlatıldığında uygundur.","boundary_detail":"Bu dal belirli küçük örme kaptır; genel sepet, deri kap, kuş adı veya yalın içeri girme anlamına genişletilemez.","branch_image_ar":"دوخلة الخوص للرطب","concept_gloss":"taze palmiye meyvesi için küçük örgü sepet","contextual_glosses":[{"applicability":"Kabın geleneksel adını aktarmak yerine malzeme, boyut ve kullanımını açıklamak gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Meyvenin özellikle taze palmiye meyvesi oluşunu daha genel ifade eder.","preserves":"Palmiye yaprağını, küçük sepet biçimini ve meyve taşıma işlevini korur."},"facet_ids":["F001","F002"],"text":"palmiye yaprağından örülmüş küçük meyve sepeti","usage_role":"explanatory"}],"definition":"Palmiye yaprağından örülen küçük bir kaptır ve içine taze palmiye meyvesi konur. Kabın malzemesi, küçük oluşu ve kullanım amacı birlikte belirleyicidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kap, palmiye yaprağından örülmüş küçük bir taşıma veya saklama nesnesidir."},{"facet_id":"F002","role":"specialization","statement":"Kabın özgül kullanımı, içine taze palmiye meyvesi koymaktır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Her boyutta, her malzemeden ve her amaçla kullanılan sepetleri kapsar.","collision":"Genel taşıma ve saklama kaplarıyla karışır.","fit":"broadening","loses":"Palmiye yaprağı malzemesini, küçük boyutu ve taze meyve kullanımını siler.","preserves":"İçine ürün konan örme kap oluşunu kısmen korur."},"text":"sepet"}],"identity_rationale":"Kaynak ifadesi, palmiye yaprağından örülmüş küçük bir kabı ve içine taze palmiye meyvesi konmasını bildirir; hazırlanan dal malzeme, biçim ve kullanım amacını doğru biçimde bir arada tutar.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"taze palmiye meyvesi konan küçük örgü sepet"}],"lexicalization_note":"Tanım yalın dalda kaydedilen küçük örme kap adını verir; başka malzemeden kapları veya içine konan meyvenin genel adını kapsamaz.","neighbor_coverage_note":"On yedi adayın tamamı değerlendirildi; genel örgü kap, geniş yaprak örgüsü alanı ve deri taşıma kabıyla üç yararlı sınır seçildi, yalnızca içerik olarak meyveyi veya uzak kardeş dalları paylaşanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal malzeme, boyut ve meyve kullanımıyla dardır; komşu dal farklı örgü araç türlerine açılır.","focus_only":"Odak dal palmiye yaprağından yapılan küçük bir kap ve taze meyve kullanımını gerektirir.","gloss":"küçük meyve sepeti ve genel örgü araç","neighbor_only":"Komşu dal genel bir örgü kap ile örgü oturak parçasını aynı ad alanında kapsar.","neighbor_ref":"root_001658/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal örülerek yapılan kap benzeri bir aracı anlatabilir."},{"boundary_match":"field_only","distinction":"Odak dal tek bir küçük kap türüdür; komşu dal biçim ve işlev bakımından birbirinden farklı daha geniş bir örme nesne kümesidir.","focus_only":"Odak dal küçük olup taze palmiye meyvesi koymak için kullanılır.","gloss":"küçük meyve kabı ve çeşitli yaprak örgüleri","neighbor_only":"Komşu dal büyük meyve küfeleri, hasırlar, kalın dokumalar ve ayakkabı onarım parçası gibi çeşitli örmeleri kapsar.","neighbor_ref":"root_000415/B002","relation_type":"same_field","shared_zone":"İki dal palmiye yaprağı benzeri malzemelerin örülmesiyle yapılan nesneler alanındadır."},{"boundary_match":"field_only","distinction":"Kap işlevi ortaktır; malzeme, tipik içerik ve yapım biçimi tamamen farklıdır.","focus_only":"Odak dal palmiye yaprağından örülür ve taze meyve için kullanılır.","gloss":"örgü meyve kabı ve deri taşıma kabı","neighbor_only":"Komşu dal deriden yapılır ve toprak, et, yağ veya başka taşınan maddeleri toplar.","neighbor_ref":"root_000214/B005","relation_type":"same_field","shared_zone":"Her iki dal içine bir şey konup taşınabilen kapları anlatır."}],"source_phrase_ar":"الدوخلة سفيفة من خوص صغيرة يجعل فيها الرطب (ayn)؛ الدوخلة هذا المنسوج من الخوص يجعل فيه الرطب (sihah)؛ الدوخلة معروفة (mufradat)","source_summary":"Kanıt, küçük ve palmiye yaprağından örülmüş kabı ortaklaştırır; belirgin kullanımını taze palmiye meyvesini içine koymak olarak verir.","sources":["AY","SI","MU"],"what_is_ar":"يدخل فيه الدوخلة: سفيفة أو منسوج من خوص يجعل فيه الرطب.","what_is_not_ar":"لا يدخل فيه الدخل الطائر ولا مطلق الدخول."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["89:30:1"],"branch_refs":[],"candidate_id":"cand_131128b3fd367a0b4845","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:30:1:additive-amplification","source_type":"word_analysis","support_ids":["sup_622915cb95142849bafc","sup_7e426b0b87e166faae39"],"title":"addition rather than rigid result sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:30:1","qac_refs":["89:30:1:1"],"status":"accepted"}},{"anchor_refs":["89:30:1"],"branch_refs":[],"candidate_id":"cand_064f759f7e00fbcd7d28","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:30:1:coordinated-command-chain","source_type":"word_analysis","support_ids":["sup_3e3ab9750d71abcf0b0b","sup_622915cb95142849bafc"],"title":"connector keeps the final command inside the command chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:30:1","qac_refs":["89:30:1:1"],"status":"accepted"}},{"anchor_refs":["89:30:1"],"branch_refs":[],"candidate_id":"cand_cf2e451a0f0b409b720f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:30:1:fused-command-onset","source_type":"word_analysis","support_ids":["sup_4ee090537ded3b42d3a1","sup_622915cb95142849bafc"],"title":"linkage is fused into the command onset","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:30:1","qac_refs":["89:30:1:1"],"status":"accepted"}},{"anchor_refs":["89:30:1"],"branch_refs":[],"candidate_id":"cand_f86d7321b9d0133fbfef","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:30:1:servant-inclusion-to-garden-entry","source_type":"word_analysis","support_ids":["sup_622915cb95142849bafc","sup_db2a0bc9d1cf02dc407a"],"title":"servant inclusion opens the final garden threshold","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:30:1","qac_refs":["89:30:1:1"],"status":"accepted"}},{"anchor_refs":["89:30:2"],"branch_refs":[],"candidate_id":"cand_a5e0ec91b32fcad10764","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000464"],"scope":"focus_ayah","source_local_id":"89:30:2:feminine-singular-direct-address","source_type":"word_analysis","support_ids":["sup_6c294c7902c8c70c6299","sup_805ca875dfb43c10bb8c"],"title":"feminine singular imperative keeps one soul addressed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:30:2","qac_refs":["89:30:1:2","89:30:1:3"],"status":"accepted"}},{"anchor_refs":["89:30:2"],"branch_refs":[],"candidate_id":"cand_99902a80fc9dd44025eb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000464"],"scope":"focus_ayah","source_local_id":"89:30:2:form-i-boundary-crossing","source_type":"word_analysis","support_ids":["sup_6c294c7902c8c70c6299","sup_bf1a44c98a876d6a4539"],"title":"entry is direct boundary crossing into an inside","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:30:2","qac_refs":["89:30:1:2","89:30:1:3"],"status":"accepted"}},{"anchor_refs":["89:30:2"],"branch_refs":[],"candidate_id":"cand_07ab448c4e320db710da","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000464"],"scope":"focus_ayah","source_local_id":"89:30:2:governed-possessed-destination","source_type":"word_analysis","support_ids":["sup_6c294c7902c8c70c6299","sup_9edf568f5514b6bb43c1"],"title":"the imperative is completed by a possessed endpoint","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:30:2","qac_refs":["89:30:1:2","89:30:1:3"],"status":"accepted"}},{"anchor_refs":["89:30:2"],"branch_refs":[],"candidate_id":"cand_7f2e8ab9c7d88c3e5374","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000464"],"scope":"focus_ayah","source_local_id":"89:30:2:morphological-role-compression","source_type":"word_analysis","support_ids":["sup_6c294c7902c8c70c6299","sup_a661eede6459974b7a64"],"title":"verb ending and noun suffix carry the two persons","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:30:2","qac_refs":["89:30:1:2","89:30:1:3"],"status":"accepted"}},{"anchor_refs":["89:30:2"],"branch_refs":[],"candidate_id":"cand_c7e68427a2b553e21368","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000464"],"scope":"focus_ayah","source_local_id":"89:30:2:singular-entry-contrast","source_type":"word_analysis","support_ids":["sup_6c294c7902c8c70c6299","sup_e9798ce7a150be66e677"],"title":"singular entry sharpens a familiar paradise-entry pattern","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:30:2","qac_refs":["89:30:1:2","89:30:1:3"],"status":"accepted"}},{"anchor_refs":["89:30:2"],"branch_refs":[],"candidate_id":"cand_9b2c34484e5743a78b24","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000464"],"scope":"focus_ayah","source_local_id":"89:30:2:staged-entry-from-servants-to-garden","source_type":"word_analysis","support_ids":["sup_2a5fb5dd818e270b0be5","sup_6c294c7902c8c70c6299"],"title":"same entry verb, changed complement, staged reception","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:30:2","qac_refs":["89:30:1:2","89:30:1:3"],"status":"accepted"}},{"anchor_refs":["89:30:2"],"branch_refs":[],"candidate_id":"cand_6cb42680745e6baa0dc9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000464"],"scope":"focus_ayah","source_local_id":"89:30:2:threshold-sound-texture","source_type":"word_analysis","support_ids":["sup_6a9edbd438e270f03bc4","sup_6c294c7902c8c70c6299"],"title":"compact sound supports the threshold action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:30:2","qac_refs":["89:30:1:2","89:30:1:3"],"status":"accepted"}},{"anchor_refs":["89:30:2"],"branch_refs":[],"candidate_id":"cand_9507095a116a6d9711fe","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000464"],"scope":"focus_ayah","source_local_id":"89:30:2:wa-prefixed-repetition","source_type":"word_analysis","support_ids":["sup_19322a7d7a70658ad43f","sup_6c294c7902c8c70c6299"],"title":"prefixed command returns within the linked sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:30:2","qac_refs":["89:30:1:2","89:30:1:3"],"status":"accepted"}},{"anchor_refs":["89:30:3"],"branch_refs":[],"candidate_id":"cand_4b419afc2c13b2750aec","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"89:30:3:compact-final-destination","source_type":"word_analysis","support_ids":["sup_421525c8b251c799aa59","sup_edaa23ff4f884e27d747"],"title":"the surah closes on the possessed destination","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:30:3","qac_refs":["89:30:2:1","89:30:2:2"],"status":"accepted"}},{"anchor_refs":["89:30:3"],"branch_refs":[],"candidate_id":"cand_720bdab07500dc7b58c7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"89:30:3:covering-garden-refuge","source_type":"word_analysis","support_ids":["sup_2180ff72d5ac6945f4b9","sup_421525c8b251c799aa59"],"title":"garden sense carries sheltering-cover pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:30:3","qac_refs":["89:30:2:1","89:30:2:2"],"status":"accepted"}},{"anchor_refs":["89:30:3"],"branch_refs":[],"candidate_id":"cand_25803ea3409a536c1ff8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"89:30:3:entry-root-covering-root-convergence","source_type":"word_analysis","support_ids":["sup_421525c8b251c799aa59","sup_f29ddcd50fc82c35da03"],"title":"entry and covering converge as enacted refuge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:30:3","qac_refs":["89:30:2:1","89:30:2:2"],"status":"accepted"}},{"anchor_refs":["89:30:3"],"branch_refs":[],"candidate_id":"cand_ce3747b4fb73f1dbad28","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"89:30:3:governed-goal-and-variant-syntax","source_type":"word_analysis","support_ids":["sup_421525c8b251c799aa59","sup_eaf71766375f957cc363"],"title":"final noun supplies the verb's goal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:30:3","qac_refs":["89:30:2:1","89:30:2:2"],"status":"accepted"}},{"anchor_refs":["89:30:3"],"branch_refs":[],"candidate_id":"cand_60c1e113ac670b174c49","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"89:30:3:possessed-definite-destination","source_type":"word_analysis","support_ids":["sup_421525c8b251c799aa59","sup_8600c4c2c21759244e54"],"title":"possessive suffix makes the garden speaker-owned","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:30:3","qac_refs":["89:30:2:1","89:30:2:2"],"status":"accepted"}},{"anchor_refs":["89:30:3"],"branch_refs":[],"candidate_id":"cand_d023d74b677e8b8459cc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"89:30:3:possessed-servants-to-possessed-garden","source_type":"word_analysis","support_ids":["sup_08d20b6158c90201ed05","sup_421525c8b251c799aa59"],"title":"possessed people give way to possessed place","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:30:3","qac_refs":["89:30:2:1","89:30:2:2"],"status":"accepted"}},{"anchor_refs":["89:30:3"],"branch_refs":[],"candidate_id":"cand_c4726911bbc791dac044","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"89:30:3:role-and-cadence-pairing","source_type":"word_analysis","support_ids":["sup_421525c8b251c799aa59","sup_8467a3e3c2515c634286"],"title":"matching final sound pairs command and destination","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:30:3","qac_refs":["89:30:2:1","89:30:2:2"],"status":"accepted"}},{"anchor_refs":["89:30:3"],"branch_refs":[],"candidate_id":"cand_b83910152690b2f2962c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"89:30:3:singular-personal-reception","source_type":"word_analysis","support_ids":["sup_421525c8b251c799aa59","sup_e6d316138d08bdb4eab7"],"title":"singular possessed garden matches singular address","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:30:3","qac_refs":["89:30:2:1","89:30:2:2"],"status":"accepted"}},{"anchor_refs":["89:30:1"],"branch_refs":[],"candidate_id":"cand_f9efc4dfef3806f0a496","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000464"],"scope":"focus_ayah","source_local_id":"89:30:1:2","source_type":"qac_morpheme","support_ids":["sup_3460c852e6389c53bc72"],"title":"QAC root occurrence: د خ ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:30:2"],"branch_refs":[],"candidate_id":"cand_badc143afdc3e6594de5","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"89:30:2:1","source_type":"qac_morpheme","support_ids":["sup_39fd15630e73cb321e20"],"title":"QAC root occurrence: ج ن ن","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:30"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:30","branch_refs":["root_000266/B003","root_000464/B001"],"candidate_id":"cand_2caa272e4a2e2ed43a49","commentary_obligation":"review","hft_ref":"hft_0c911ebff0816df8131d","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_spatial_orchard_entry","source_type":"hft","support_ids":["sup_e0ec521aea7e8ca54491"],"title":"baseline_spatial_orchard_entry","trust":"legacy_unbound"},{"anchor_refs":["89:30"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:30","branch_refs":["root_000266/B001","root_000266/B008","root_000464/B003"],"candidate_id":"cand_8776312a86b2c0b3c773","commentary_obligation":"review","hft_ref":"hft_2611e3a132cfbfbe3a8b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_protected_interior","source_type":"hft","support_ids":["sup_d530d8e3c93ad64186f9"],"title":"baseline_protected_interior","trust":"legacy_unbound"},{"anchor_refs":["89:30"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:30","branch_refs":["root_000266/B011","root_000464/B008"],"candidate_id":"cand_52184e28b0f598806e3a","commentary_obligation":"review","hft_ref":"hft_66a2324411cd1fccf19a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_living_interleaving","source_type":"hft","support_ids":["sup_e612bf358beccf576d7a"],"title":"baseline_living_interleaving","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَٱدْخُلِى جَنَّتِى","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"89:30:1:1","qac_word_ref":"89:30:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:30:1:2","qac_word_ref":"89:30:1","root_ar":"د خ ل","surface_ar":"ٱدْخُلِ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:30:1:3","qac_word_ref":"89:30:1","root_ar":"","surface_ar":"ى"},{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:30:2:1","qac_word_ref":"89:30:2","root_ar":"ج ن ن","surface_ar":"جَنَّتِ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1S","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:30:2:2","qac_word_ref":"89:30:2","root_ar":"","surface_ar":"ى"}],"word_analysis_qac_refs":[["89:30:1:1"],["89:30:1:2","89:30:1:3"],["89:30:2:1","89:30:2:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["89:30:1","89:30:2","89:30:3"]},"focus_surface_evidence":{"arabic_uthmani":"وَٱدْخُلِى جَنَّتِى","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"89:30:1:1","qac_word_ref":"89:30:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:30:1:2","qac_word_ref":"89:30:1","root_ar":"د خ ل","surface_ar":"ٱدْخُلِ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:30:1:3","qac_word_ref":"89:30:1","root_ar":"","surface_ar":"ى"},{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:30:2:1","qac_word_ref":"89:30:2","root_ar":"ج ن ن","surface_ar":"جَنَّتِ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1S","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:30:2:2","qac_word_ref":"89:30:2","root_ar":"","surface_ar":"ى"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["89:30:1:1"],["89:30:1:2","89:30:1:3"],["89:30:2:1","89:30:2:2"]],"word_analysis_refs":["89:30:1","89:30:2","89:30:3"],"word_rows":[{"analysis_record_ref":"89:30:1","analytic_gloss_range_en":"prefixed conjunction coordinating or resuming the final imperative with the preceding command chain","analytic_root_gloss_range_en":null,"qac_refs":["89:30:1:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"89:30:2","analytic_gloss_range_en":"second-person feminine singular Form I imperative commanding direct entry into the named possessed destination","analytic_root_gloss_range_en":"broad entry and interiority family; the local Form I imperative selects direct boundary-crossing into a governed goal, not causative admission or reciprocal mixing","qac_refs":["89:30:1:2","89:30:1:3"],"root":{"arabic":"د خ ل","transliteration":"d-kh-l"},"surface":{"arabic":"ٱدْخُلِى","transliteration":"udkhulī"}},{"analysis_record_ref":"89:30:3","analytic_gloss_range_en":"singular possessed garden or afterlife garden as the governed destination of entry","analytic_root_gloss_range_en":"covering, concealment, tree-covered garden, afterlife garden, protection, and life-sheltering enclosure belong to the wider family; the local noun selects the possessed garden while allowing sheltering-cover pressure","qac_refs":["89:30:2:1","89:30:2:2"],"root":{"arabic":"ج ن ن","transliteration":"j-n-n"},"surface":{"arabic":"جَنَّتِى","transliteration":"jannatī"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["89:30"],"branch_refs":["root_000266/B003","root_000464/B001"],"candidate_id":"cand_2caa272e4a2e2ed43a49","evidence_scope":"focus_ayah","hft_ref":"hft_0c911ebff0816df8131d","item_id":"baseline_spatial_orchard_entry","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_spatial_orchard_entry","support_id":"sup_e0ec521aea7e8ca54491"},{"anchor_refs":["89:30"],"branch_refs":["root_000266/B001","root_000266/B008","root_000464/B003"],"candidate_id":"cand_8776312a86b2c0b3c773","evidence_scope":"focus_ayah","hft_ref":"hft_2611e3a132cfbfbe3a8b","item_id":"baseline_protected_interior","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_protected_interior","support_id":"sup_d530d8e3c93ad64186f9"},{"anchor_refs":["89:30"],"branch_refs":["root_000266/B011","root_000464/B008"],"candidate_id":"cand_52184e28b0f598806e3a","evidence_scope":"focus_ayah","hft_ref":"hft_66a2324411cd1fccf19a","item_id":"baseline_living_interleaving","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_living_interleaving","support_id":"sup_e612bf358beccf576d7a"}],"diagnostics":[],"lane_counts":{"global":15,"macro":11,"micro":3},"packet_summary":{"ayah_count":30,"focus_ref":"89:30","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000702","furuq_root_norm":"س ر ي","furuq_source_root_norm":"س ر ي","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000697","furuq_root_norm":"س ر ر","furuq_source_root_norm":"س ر ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ع و د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":true,"target_occurrences":35,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ج و ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000273","furuq_root_norm":"ج و ب","furuq_source_root_norm":"ج و ب","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000283","furuq_root_norm":"ج ي ب","furuq_source_root_norm":"ج ي ب","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000220","furuq_root_norm":"ج ب ي","furuq_source_root_norm":"ج ب ي","is_dominant":false,"target_occurrences":2,"target_rank":3},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000214","furuq_root_norm":"ج ب ب","furuq_source_root_norm":"ج ب ب","is_dominant":false,"target_occurrences":1,"target_rank":4}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ب ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000153","furuq_root_norm":"ب ل و","furuq_source_root_norm":"ب ل و","is_dominant":true,"target_occurrences":28,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000154","furuq_root_norm":"ب ل ي","furuq_source_root_norm":"ب ل ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ه و ن","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001453","furuq_root_norm":"م ه ن","furuq_source_root_norm":"م ه ن","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001608","furuq_root_norm":"ه و ن","furuq_source_root_norm":"ه و ن","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001687","furuq_root_norm":"و ه ن","furuq_source_root_norm":"و ه ن","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14","89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"89:30","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":20,"unstructured_record_count":0},"identity":{"ayah_ref":"89:30","lane":"micro","linguistic_source_ref":"89:30","surface_ref":"89:30","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"89:30","target_tokens":[["Cennetime",["89:30:2"]],["de",["89:30:1"]],["gir",["89:30:1"]]],"text":"Cennetime de gir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":15,"ayah_to":30,"id":"s089-p02-015-030","label":"The wealth test, judgment, and tranquil soul","number":2,"refs":["89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:3:possessed-servants-to-possessed-garden","source_type":"word_analysis","support_id":"sup_08d20b6158c90201ed05","text":"{\"blocking_evidence\":null,\"headline\":\"possessed people give way to possessed place\",\"reader_payoff\":\"The reader sees the last two ayahs move through two possessed domains under one speaker: servants in 89:29, garden in 89:30.\",\"reason\":\"The possessive suffix evidence keeps the same speaker role in the final noun, while the boundary rows give the concrete 89:29 to 89:30 staged movement.\",\"representative_source_ids\":[\"QE-06d2b1a4\",\"QE-dec065bd\",\"ME-052985ed\",\"QY-12b8266a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:2:wa-prefixed-repetition","source_type":"word_analysis","support_id":"sup_19322a7d7a70658ad43f","text":"{\"blocking_evidence\":null,\"headline\":\"prefixed command returns within the linked sequence\",\"reader_payoff\":\"The reader hears the verb arrive already connected to the prior entry command, so the repeated command feels like the next threshold rather than a fresh scene.\",\"reason\":\"QAC records the imperative as prefixed by the conjunction, and translation support keeps the final command inside the 89:27-30 direct-address chain.\",\"representative_source_ids\":[\"QG-2b859048\",\"QF-59ce0f6d\",\"QT-0547e473\",\"QP-a593f51a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:3:covering-garden-refuge","source_type":"word_analysis","support_id":"sup_2180ff72d5ac6945f4b9","text":"{\"blocking_evidence\":null,\"headline\":\"garden sense carries sheltering-cover pressure\",\"reader_payoff\":\"The reader sees the local garden as a possessed refuge: paradise remains the selected sense, while the root's covering and protection field gives the destination enclosed shelter force.\",\"reason\":\"V4 preserves garden, afterlife garden, covering, protective cover, and hidden-life branches for the root family, while QAC keeps the local word as a concrete possessed noun governed by entry.\",\"representative_source_ids\":[\"QS-753596c9\",\"QS-b097ead5\",\"QS-fed2427a\",\"MS-699a82be\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:2:staged-entry-from-servants-to-garden","source_type":"word_analysis","support_id":"sup_2a5fb5dd818e270b0be5","text":"{\"blocking_evidence\":null,\"headline\":\"same entry verb, changed complement, staged reception\",\"reader_payoff\":\"The reader sees the repeated entry verb carry the soul from social belonging in 89:29 to spatial arrival in 89:30.\",\"reason\":\"The local verb repeats the prior imperative form while attachment evidence shows a new governed endpoint in the current ayah.\",\"representative_source_ids\":[\"MT-699f1929\",\"QE-59f670f5\",\"QE-a7fbae36\",\"ME-fd3363b2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:30:1:2","source_type":"qac_morpheme","support_id":"sup_3460c852e6389c53bc72","text":"{\"lemma_ar\":\"دَخَلَ\",\"morph_features\":\"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"89:30:1:2\",\"qac_word_ref\":\"89:30:1\",\"root_ar\":\"د خ ل\",\"surface_ar\":\"ٱدْخُلِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:30:2:1","source_type":"qac_morpheme","support_id":"sup_39fd15630e73cb321e20","text":"{\"lemma_ar\":\"جَنَّة\",\"morph_features\":\"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"89:30:2:1\",\"qac_word_ref\":\"89:30:2\",\"root_ar\":\"ج ن ن\",\"surface_ar\":\"جَنَّتِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:1:coordinated-command-chain","source_type":"word_analysis","support_id":"sup_3e3ab9750d71abcf0b0b","text":"{\"blocking_evidence\":null,\"headline\":\"connector keeps the final command inside the command chain\",\"reader_payoff\":\"The reader notices that the ayah opens as a continuation of the prior imperative sequence rather than as an isolated paradise notice.\",\"reason\":\"QAC identifies the word as a prefixed conjunction, and attachment evidence reads the whole ayah as an imperative clause continuing the direct-address frame.\",\"representative_source_ids\":[\"QG-09c112af\",\"QG-e6d5a078\",\"MG-2d8c3c9a\",\"QT-0be0c443\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:3","source_type":"word_analysis","support_id":"sup_421525c8b251c799aa59","text":"{\"gloss_range\":\"singular possessed garden or afterlife garden as the governed destination of entry\",\"prose\":\"{{ar:جَنَّتِى}} ({{tr:jannatī}}) is the governed destination of the imperative, not an appositional afterthought; even the reported prepositional variant preserves the same noun and shifts the pressure to whether entry is direct or mediated. Its first-person suffix makes the endpoint definite by possession: the final place is not a generic garden but the speaker's own domain. That same suffix keeps the divine speaker present at the surah's last sound, while the singular noun matches the singular addressee of {{ar:ٱدْخُلِى}} ({{tr:udkhulī}}), narrowing a familiar plural paradise-entry pattern such as 16:32 into one owned reception. The root family lets garden and covering work together: the local sense is the possessed afterlife garden, while the wider covering, protective, and life-sheltering branches make the place feel like enclosed refuge rather than scenery alone; the night-covering contrast in 6:76 helps show the same covering field transformed here into a life-bearing divine enclosure. The word also closes the staged movement from 89:29: the soul moves from belonging among possessed servants to dwelling in a possessed enclosure. Its final cadence pairs with the imperative's ending, and the doubled nasal gives the destination acoustic weight, but the grammar keeps their roles distinct: one ending marks the addressed soul, the other marks the owner's garden.\",\"root_display\":\"{{ar:ج ن ن}} ({{tr:j-n-n}})\",\"root_gloss_range\":\"covering, concealment, tree-covered garden, afterlife garden, protection, and life-sheltering enclosure belong to the wider family; the local noun selects the possessed garden while allowing sheltering-cover pressure\",\"surface_display\":\"{{ar:جَنَّتِى}} ({{tr:jannatī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:1:fused-command-onset","source_type":"word_analysis","support_id":"sup_4ee090537ded3b42d3a1","text":"{\"blocking_evidence\":null,\"headline\":\"linkage is fused into the command onset\",\"reader_payoff\":\"The reader hears and sees the connector flow straight into the threshold verb, so continuation is not separated from entry.\",\"reason\":\"The bundle splits the conjunction analytically but also records it as prefixed to the imperative surface, preserving the compact visual and recitational onset.\",\"representative_source_ids\":[\"QF-1264bd23\",\"QF-6aec8534\",\"QP-1de3ef47\",\"QP-8bd38e73\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:1","source_type":"word_analysis","support_id":"sup_622915cb95142849bafc","text":"{\"gloss_range\":\"prefixed conjunction coordinating or resuming the final imperative with the preceding command chain\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) makes the final ayah begin in continuation, not as a detached reward statement. It links the garden-entry command to the prior entry command in 89:29, so servant inclusion becomes the platform for one more threshold rather than the stopping point. Its force is additive and resumptive rather than rigidly resultive: after the consequence-marked return has already moved into servant inclusion, this connector amplifies admission without making garden entry a new condition. Because the brief particle is heard and written into the onset of {{ar:ٱدْخُلِى}} ({{tr:udkhulī}}), the reader meets a light pickup that flows directly into the heavier threshold command before the destination is named.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:2:threshold-sound-texture","source_type":"word_analysis","support_id":"sup_6a9edbd438e270f03bc4","text":"{\"blocking_evidence\":null,\"headline\":\"compact sound supports the threshold action\",\"reader_payoff\":\"The reader can hear the compact consonantal pressure of the command fit its boundary-crossing action.\",\"reason\":\"The phonetic claim is local to the actual imperative surface and reinforces, without replacing, the grammatical entry sense.\",\"representative_source_ids\":[\"QP-ca011a90\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:2","source_type":"word_analysis","support_id":"sup_6c294c7902c8c70c6299","text":"{\"gloss_range\":\"second-person feminine singular Form I imperative commanding direct entry into the named possessed destination\",\"prose\":\"{{ar:ٱدْخُلِى}} ({{tr:udkhulī}}) repeats the entry command as direct second-person feminine address. The verb ending keeps the same addressed soul from 89:27 under command, while the final noun supplies the speaker-owned endpoint. Its Form I shape makes the crossing grammatically active for the addressee: the soul is told to enter, not merely described as rewarded or made the object of a separate admission verb. The root's entry-and-interior field turns the closure into threshold movement into a named inside, making the addressed soul an insider of the possessed domain while local grammar blocks reciprocal mixture or unrelated inward-defect branches. Because the same command appeared in 89:29 with a different complement, the repeated verb stages reception: first entry among servants, then entry into the possessed garden. Unlike the plural paradise-entry formula in 16:32, this closing command is singular and speaker-owned, intensifying personal reception. The command also reaches the listener before the destination is named, so obedience is enacted before the final sanctuary is revealed, and its compact consonantal pressure fits the boundary-crossing action.\",\"root_display\":\"{{ar:د خ ل}} ({{tr:d-kh-l}})\",\"root_gloss_range\":\"broad entry and interiority family; the local Form I imperative selects direct boundary-crossing into a governed goal, not causative admission or reciprocal mixing\",\"surface_display\":\"{{ar:ٱدْخُلِى}} ({{tr:udkhulī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:1:additive-amplification","source_type":"word_analysis","support_id":"sup_7e426b0b87e166faae39","text":"{\"blocking_evidence\":null,\"headline\":\"addition rather than rigid result sequence\",\"reader_payoff\":\"The reader notices that the second entry amplifies the prior admission without making the particle itself encode strict before-after logic.\",\"reason\":\"The conjunction supports coordination and resumption, while the local surface does not make the particle a result marker; the sequential force comes from the repeated command frame across 89:29-30.\",\"representative_source_ids\":[\"QS-619f2caf\",\"QS-8f1c9db7\",\"QB-618663ab\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:2:feminine-singular-direct-address","source_type":"word_analysis","support_id":"sup_805ca875dfb43c10bb8c","text":"{\"blocking_evidence\":null,\"headline\":\"feminine singular imperative keeps one soul addressed\",\"reader_payoff\":\"The reader notices that the final command is personally addressed to the same feminine singular soul, not narrated about a group or reward class.\",\"reason\":\"QAC marks the form as a second-person feminine singular imperative, and attachment evidence supplies the same implicit feminine singular addressee as the prior command.\",\"representative_source_ids\":[\"QG-7aa08827\",\"MG-3a6a46cf\",\"QF-052ff2c4\",\"QB-b0d3209b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:3:role-and-cadence-pairing","source_type":"word_analysis","support_id":"sup_8467a3e3c2515c634286","text":"{\"blocking_evidence\":null,\"headline\":\"matching final sound pairs command and destination\",\"reader_payoff\":\"The reader hears the imperative and the garden noun close with matching sound while recognizing that the two endings do different grammatical work.\",\"reason\":\"The surface forms share a final long-vowel cadence, while attachment evidence distinguishes the verb's feminine addressee marking from the noun's first-person possession.\",\"representative_source_ids\":[\"QF-16de11d0\",\"QE-fadc6e1f\",\"QP-a6cf4340\",\"MP-96d880c6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:3:possessed-definite-destination","source_type":"word_analysis","support_id":"sup_8600c4c2c21759244e54","text":"{\"blocking_evidence\":null,\"headline\":\"possessive suffix makes the garden speaker-owned\",\"reader_payoff\":\"The reader notices that the final destination is made definite through the speaker's possession, not through a generic paradise label.\",\"reason\":\"QAC identifies a first-person singular possessive suffix, and attachment evidence marks it as an idafa relation with the noun and as the direct-speech speaker's possession.\",\"representative_source_ids\":[\"QG-35fa8c07\",\"QG-3aeb3b89\",\"QG-dd20f138\",\"MG-50be5a9a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:2:governed-possessed-destination","source_type":"word_analysis","support_id":"sup_9edf568f5514b6bb43c1","text":"{\"blocking_evidence\":null,\"headline\":\"the imperative is completed by a possessed endpoint\",\"reader_payoff\":\"The reader notices that the command grants access to the speaker-owned destination named after it, not a bare motion command.\",\"reason\":\"Attachment evidence marks the final noun as the explicit object or goal of {{ar:ٱدْخُلِى}} ({{tr:udkhulī}}), so the imperative's force is completed by the possessed destination.\",\"representative_source_ids\":[\"QG-833a99bf\",\"QI-f7a37af5\",\"QT-d53219f5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:2:morphological-role-compression","source_type":"word_analysis","support_id":"sup_a661eede6459974b7a64","text":"{\"blocking_evidence\":null,\"headline\":\"verb ending and noun suffix carry the two persons\",\"reader_payoff\":\"The reader notices that the addressee and speaker are carried by endings, so the short clause binds movement and possession without renaming either participant.\",\"reason\":\"Attachment evidence identifies the verb's implicit feminine singular subject and the final noun's first-person possessive suffix, supporting the row's role-compression payoff.\",\"representative_source_ids\":[\"QG-d4e69c34\",\"QP-4215fb78\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:2:form-i-boundary-crossing","source_type":"word_analysis","support_id":"sup_bf1a44c98a876d6a4539","text":"{\"blocking_evidence\":null,\"headline\":\"entry is direct boundary crossing into an inside\",\"reader_payoff\":\"The reader sees salvation as commanded crossing into a secure interior, while the local Form I verb prevents causative admission or reciprocal blending from taking over.\",\"reason\":\"V4 supports entry and interiority within the root family, but QAC and attachment evidence keep the local form as a Form I imperative governing an explicit goal.\",\"representative_source_ids\":[\"QG-db1262f4\",\"QS-034daf0d\",\"QS-fd98b6dc\",\"MS-b2cd3b3c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:1:servant-inclusion-to-garden-entry","source_type":"word_analysis","support_id":"sup_db2a0bc9d1cf02dc407a","text":"{\"blocking_evidence\":null,\"headline\":\"servant inclusion opens the final garden threshold\",\"reader_payoff\":\"The reader sees 89:29 and 89:30 as a staged admission: first belonging among servants, then entry into the possessed garden.\",\"reason\":\"Translation support recommends reading the final command with the preceding direct-address window, and the particle supplies the local continuation.\",\"representative_source_ids\":[\"QT-c7b5cee6\",\"MT-bf14af1a\",\"QB-4d83b000\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:3:singular-personal-reception","source_type":"word_analysis","support_id":"sup_e6d316138d08bdb4eab7","text":"{\"blocking_evidence\":null,\"headline\":\"singular possessed garden matches singular address\",\"reader_payoff\":\"The reader notices the final reception is individualized by a singular destination paired with a singular addressee, rather than spread across a plural reward formula such as 16:32.\",\"reason\":\"The local noun is singular and possessed, and the governing imperative carries a feminine singular addressee; the contrast row supplies the concrete plural reference at 16:32.\",\"representative_source_ids\":[\"QF-29b4a270\",\"QF-5b80f6b2\",\"QI-f1657550\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:2:singular-entry-contrast","source_type":"word_analysis","support_id":"sup_e9798ce7a150be66e677","text":"{\"blocking_evidence\":null,\"headline\":\"singular entry sharpens a familiar paradise-entry pattern\",\"reader_payoff\":\"The reader notices that the familiar paradise-entry formula is here narrowed into a singular reception by a possessed destination, unlike the plural entry scene in 16:32.\",\"reason\":\"Contextual profiles show this Form I root commonly appears as imperatives with explicit objects, while local agreement and the final possessive endpoint make the current deployment singular and personal.\",\"representative_source_ids\":[\"QI-eac72cdd\",\"MI-7b1f418d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:3:governed-goal-and-variant-syntax","source_type":"word_analysis","support_id":"sup_eaf71766375f957cc363","text":"{\"blocking_evidence\":null,\"headline\":\"final noun supplies the verb's goal\",\"reader_payoff\":\"The reader sees the garden as the command's syntactic endpoint, with variant evidence sharpening governance rather than changing the noun's identity.\",\"reason\":\"Attachment evidence makes {{ar:جَنَّتِى}} ({{tr:jannatī}}) the explicit object or goal of {{ar:ٱدْخُلِى}} ({{tr:udkhulī}}); the reported prepositional variant affects syntax, not the local noun form or possessed garden sense.\",\"representative_source_ids\":[\"QG-6c49c34d\",\"QF-90953fd2\",\"QH-6c1a9cf5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:3:compact-final-destination","source_type":"word_analysis","support_id":"sup_edaa23ff4f884e27d747","text":"{\"blocking_evidence\":null,\"headline\":\"the surah closes on the possessed destination\",\"reader_payoff\":\"The reader feels the ayah's compression: command first, destination last, with the final heard content being the owned enclosure.\",\"reason\":\"The word is the final noun of the ayah and the explicit endpoint of the imperative clause, so the two-word construction delays the destination until closure.\",\"representative_source_ids\":[\"QT-683433b2\",\"QT-79db6351\",\"QT-ad2b81ae\",\"MT-ff5234ef\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:30:3:entry-root-covering-root-convergence","source_type":"word_analysis","support_id":"sup_f29ddcd50fc82c35da03","text":"{\"blocking_evidence\":null,\"headline\":\"entry and covering converge as enacted refuge\",\"reader_payoff\":\"The reader sees the motion root and the covering-root noun combine into a commanded crossing into protected interior, while local grammar keeps each word's role distinct.\",\"reason\":\"Contextual evidence supports entry-goal deployment and V4 supports covering-garden pressure, but the local syntax assigns the crossing to the verb and the possessed enclosure to the noun.\",\"representative_source_ids\":[\"QI-a13921d1\",\"QY-256caa9a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَٱدْخُلِى جَنَّتِى","ayah_ref":"89:30"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000266/B003","root_000464/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000464","role":"The basic image of going inside supplies the directed threshold crossing.","root":"د خ ل","source_ref":"89:30","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000266","role":"The tree-covered orchard image supplies the concrete destination and its enveloping vegetation.","root":"ج ن ن","source_ref":"89:30","source_word_indices":["2"]}],"changed_reading":{"after":"A direct admission into the speaker's tree-covered garden.","before":"A bare command to move somewhere."},"confidence":"strong","focus_anchor":"The imperative of entry is followed directly by a first-person-possessed garden noun.","mechanism":"A commanded crossing moves the addressee from outside to inside a tree-covered, speaker-owned enclosure.","model_id":"baseline_spatial_orchard_entry"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_spatial_orchard_entry","source_type":"hft","support_id":"sup_e0ec521aea7e8ca54491","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱدْخُلِى جَنَّتِى","ayah_ref":"89:30"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000266/B001","root_000266/B008","root_000464/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000464","role":"The hidden-interior image turns entry into access to an inward side.","root":"د خ ل","source_ref":"89:30","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000266","role":"The covering image makes concealment a property of the destination.","root":"ج ن ن","source_ref":"89:30","source_word_indices":["2"]},{"branch_id":"B008","mapped_root_id":"root_000266","role":"The shield-like cover gives that concealment a protective rather than merely visual function.","root":"ج ن ن","source_ref":"89:30","source_word_indices":["2"]}],"changed_reading":{"after":"The garden is also a protected interior into which access is granted.","before":"The garden is only an attractive exterior place."},"confidence":"medium","focus_anchor":"Both the entry verb and the garden noun can foreground an inside that is hidden or covered.","mechanism":"The command moves the addressee not merely onto pleasant terrain but into an inward, perception-screened, protective domain.","model_id":"baseline_protected_interior"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_protected_interior","source_type":"hft","support_id":"sup_d530d8e3c93ad64186f9","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱدْخُلِى جَنَّتِى","ayah_ref":"89:30"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000266/B011","root_000464/B008"],"payload":{"activation_trace":[{"branch_id":"B008","mapped_root_id":"root_000464","role":"The interlocked-layers image supplies incorporation among already joined parts.","root":"د خ ل","source_ref":"89:30","source_word_indices":["1"]},{"branch_id":"B011","mapped_root_id":"root_000266","role":"The vigorous intertwined-growth image makes the receiving whole living and proliferative.","root":"ج ن ن","source_ref":"89:30","source_word_indices":["2"]}],"changed_reading":{"after":"Entry integrates a person into the garden's living, interwoven order.","before":"Entry places a person within a garden."},"confidence":"exploratory","focus_anchor":"The entry root can image interleaving, while the garden root can image thick, intertwined growth.","mechanism":"Entry becomes incorporation: the addressee is fitted into a dense living fabric rather than merely positioned inside a boundary.","model_id":"baseline_living_interleaving"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_living_interleaving","source_type":"hft","support_id":"sup_e612bf358beccf576d7a","trust":"legacy_unbound"}]}
</lane_packet_json>
