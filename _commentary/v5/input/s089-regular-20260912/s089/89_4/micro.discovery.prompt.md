# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **89:4**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s089-regular-20260912/s089/89_4/micro.discovery.json` and modify nothing
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
  "ayah_ref": "89:4",
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
{"branch_registry":[{"boundary":"Anlam hem saklı içerik ve iç durumları hem de kişiler arasındaki gizli konuşmayı kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000697/B001","candidate_links":[{"candidate_id":"cand_eef72432a253294c4c15","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"saklama ve gizli paylaşım","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bilgi, söz, iş veya iç durum başkalarının bilgisine kapalı tutulur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Söz, bir kişiye gizlice söylenir veya kişiler kendi aralarında gizli konuşur."}}],"root_ar":"س ر ي","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Saklı içerik ile kişiler arasındaki gizli söz alışverişini birlikte karşılayan genel kavram anlatımıdır.","boundary_detail":"Anlam hem saklı içerik ve iç durumları hem de kişiler arasındaki gizli konuşmayı kapsar.","branch_image_ar":"إخفاء الشيء في الباطن","concept_gloss":"saklama ve gizli paylaşım","contextual_glosses":[{"applicability":"İki veya daha çok kişinin başkalarından saklı biçimde konuştuğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Konuşma dışındaki saklı bilgi, iş ve iç durum anlamlarını karşılamaz.","preserves":"Gizli söz alışverişini ve açıklamama koşulunu korur."},"facet_ids":["F002"],"text":"gizlice konuşmak","usage_role":"contextual"}],"definition":"Bir bilgi, söz, iş veya iç durumun başkalarına açıklanmadan saklanmasıdır; ayrıca bu tür bir sözün bir kişiye gizlice iletilmesini kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bilgi, söz, iş veya iç durum başkalarının bilgisine kapalı tutulur."},{"facet_id":"F002","role":"specialization","statement":"Söz, bir kişiye gizlice söylenir veya kişiler kendi aralarında gizli konuşur."}],"identity_rationale":"Kaynak ifadesi, bir şeyi başkalarından saklama durumunu ve birine sözü gizlice iletme eylemini birlikte açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"gizlenen bilgi veya durum"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kişinin gizli iç durumu veya gizlice yaptığı iş"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyi gizleyip saklamak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"birine bir sözü gizlice açmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kulağına gizlice söylemek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kendi aralarında gizlice konuşmak"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"gizlice konuşmaya yarayan tomar benzeri araç"}],"lexicalization_note":"Tanım, yalın biçimlerin giz ve iç durum anlamıyla türemiş eylemlerin saklama ve gizli konuşma anlamlarını ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yakın karışma alanını gizli konuşma dalı açıklamaktadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal gizli konuşmaya odaklanırken bu dal daha geniş biçimde saklı içerik, iç durum ve saklama eylemini de içerir.","focus_only":"Saklı bilgi, iç durum ve tek başına gizleme eylemi de kapsama girer.","gloss":"gizli konuşma","neighbor_only":"Özel konuşma, bir kişiyi gizli söz için ayırma çerçevesinde belirginleşir.","neighbor_ref":"root_001476/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da başkalarından saklanan sözün kişiler arasında iletilmesini kapsar."}],"source_phrase_ar":"السر خلاف الإعلان (maqayis)؛ السر ما أسررت والسريرة عمل السر (ayn)؛ السر الذي يكتم والسريرة مثله (sihah)؛ الإسرار خلاف الإعلان والسر هو الحديث المكتم في النفس (mufradat)؛ ساره في أذنه وتساروا (sihah)","source_summary":"Tanıklıklar saklamayı açıklamanın karşıtı olarak verir; içte tutulan söz, gizli durum ve özel konuşma bu çekirdeğin görünümleridir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"السر والإسرار والسريرة والمناجاة والمسارة وما يفضى به في خفية","what_is_not_ar":"الإعلان؛ النكاح؛ السرور؛ السرار القمري"},"support_links":["sup_35209214a5688a067e3f"]},{"boundary":"Bu, yerleşik saklama anlamının karşıtı olan tartışmalı bir kullanım olarak sunulmalıdır.","branch_kind":"unresolved","branch_ref":"root_000697/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"açığa vurma, tartışmalı kullanım","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eylem bazı tanıklıklarda bir şeyi açıklamak veya görünür kılmak anlamında verilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı okuma başka değerlendirmelerde yanlış, işitilmemiş veya güvenilmez sayılır."}}],"root_ar":"س ر ي","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kaynaklarda aktarılıp aynı zamanda eleştirilen karşıt anlamı ihtiyatla göstermek için uygundur.","boundary_detail":"Bu, yerleşik saklama anlamının karşıtı olan tartışmalı bir kullanım olarak sunulmalıdır.","branch_image_ar":"إظهار ما قيل فيه أسر","concept_gloss":"açığa vurma, tartışmalı kullanım","contextual_glosses":[{"applicability":"Anlamın doğrudan onaylanmadığı, yalnızca eski bir yorum olarak aktarıldığı açıklamalarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Açıklama iddiasını kesin hüküm vermeden aktarır ve tartışmalı niteliği sezdirir."},"facet_ids":["F001","F002"],"text":"açıkladığı ileri sürülmek","usage_role":"explanatory"}],"definition":"Tartışmalı bir kullanımda, saklamak beklenen eylemin bir şeyi açıklamak veya görünür kılmak anlamına gelmesidir; bu okumanın güvenilirliğine bazı kaynak değerlendirmelerinde itiraz edilmiştir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eylem bazı tanıklıklarda bir şeyi açıklamak veya görünür kılmak anlamında verilir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı okuma başka değerlendirmelerde yanlış, işitilmemiş veya güvenilmez sayılır."}],"identity_rationale":"Kaynak ifadesi açıklama anlamındaki kullanımı bildirir, ancak aynı toplu tanıklık bu okumanın yanlış veya tekil sayıldığını da kaydeder.","lexicalization_note":"Yalın ya da belirli bir yapıya bağlı olduğu kanıtlanmadığından tanım kullanımın biçimsel kapsamını varsaymaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel ortaya çıkma dalı tartışmalı kullanımın sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel ortaya çıkmayı anlatır; bu dal ise belirli bir sözcüğe atfedilen ve güvenilirliği tartışılan karşıt anlam kaydıdır.","focus_only":"Açıklama anlamı, normalde saklama bildiren bir eyleme yüklenen tartışmalı karşıt okumadır.","gloss":"gizlinin ortaya çıkması","neighbor_only":"Bir şeyin gizlilikten çıkıp görünür olması veya doğrudan ortaya çıkarılması genel ve yerleşik anlamdır.","neighbor_ref":"root_000105/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da gizli veya görünmez olan bir şeyin bilinir ve görünür hale gelmesi vardır."}],"source_phrase_ar":"أسررته أعلنته (maqayis)؛ أسررت الشيء أظهرته وكتمته أيضا (jamhara)؛ أسررت الشيء كتمته وأعلنته أيضا (sihah)؛ قال الفراء أخطأ أبو عبيدة (maqayis)؛ لم أسمع ذلك لغيره (tahdhib)","source_summary":"Toplu tanıklık hem açıklama anlamını aktarır hem de bu anlamın güvenilirliğine yönelik açık itirazı korur; bu nedenle kullanım kesinleştirilemez.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"استعمال أسررت بمعنى أعلنت أو أظهرت مع كونه موضع خلاف في المصادر","what_is_not_ar":"الإسرار المستقر بمعنى الكتمان؛ أشررت بالشين"},"support_links":[]},{"boundary":"Dal genel gizli konuşma değildir; evlilik ve cinsellikle ilgili örtülü kullanımla sınırlıdır.","branch_kind":"unresolved","branch_ref":"root_000697/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"gizli tutulan evlilik veya cinsel ilişki","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Evlilik veya cinsel birleşme, gizli tutulan bir ilişki olarak örtülü biçimde adlandırılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kullanım evlilik dışı ilişkiye veya bekleme süresindeki kadına evlenme önerisine uzanabilir."}}],"root_ar":"س ر ي","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Evlilik ve cinsel birlikteliği gizlilik bağıyla birlikte veren en geniş doğal karşılıktır.","boundary_detail":"Dal genel gizli konuşma değildir; evlilik ve cinsellikle ilgili örtülü kullanımla sınırlıdır.","branch_image_ar":"سر النكاح المستور","concept_gloss":"gizli tutulan evlilik veya cinsel ilişki","contextual_glosses":[{"applicability":"Sözün özellikle cinsel birleşmeyi dolaylı ve gizlilik vurgusuyla anlattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Evlilik, evlenme önerisi ve evlilik dışı ilişki arasındaki geniş kapsamı daraltır.","preserves":"Cinsel birliktelik ve örtülü adlandırma bağını korur."},"facet_ids":["F001"],"text":"örtülü biçimde cinsel birliktelik","usage_role":"contextual"}],"definition":"Evlilik veya cinsel birleşmenin, genellikle gizli tutulması nedeniyle örtülü biçimde adlandırılmasıdır; kimi kullanımlarda evlilik dışı ilişkiyi ya da bekleme süresindeki kadına evlenme önerisini de belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Evlilik veya cinsel birleşme, gizli tutulan bir ilişki olarak örtülü biçimde adlandırılır."},{"facet_id":"F002","role":"extension","statement":"Kullanım evlilik dışı ilişkiye veya bekleme süresindeki kadına evlenme önerisine uzanabilir."}],"identity_rationale":"Kaynak ifadesi evlilik ve cinsel birleşmeyi gizlilik üzerinden adlandırır; evlilik dışı ilişki ve bekleme süresindeki kadına evlenme önerisi de kapsam uzantılarıdır.","lexicalization_note":"Belirli bir yalın veya yapıya bağlı dağılım kanıtlanmadığı için tanım yalnızca aktarılan cinsel ve evlilik alanını korur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; doğrudan cinsel birleşme dalı örtülü kullanımın sınırını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal doğrudan birleşme eylemine odaklanır; bu dal gizlilikten doğan örtülü adlandırmayı ve evlilik alanındaki uzantıları korur.","focus_only":"Evlilik, evlilik dışı ilişki ve belirli evlenme önerileri gizlilik bağıyla kapsama girebilir.","gloss":"cinsel birleşme","neighbor_only":"Cinsel birleşme ve çiftleşme eylemi doğrudan anlam çekirdeğidir.","neighbor_ref":"root_000259/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da cinsel birleşmeyi veya evlilik içindeki cinsel birlikteliği anlatabilir."}],"source_phrase_ar":"السر وهو النكاح (maqayis)؛ السر الجماع والسر الذكر (sihah)؛ السر النكاح والزنى وخطبة المعتدة (tahdhib)؛ كني عن النكاح بالسر من حيث إنه يخفى (mufradat)","source_summary":"Tanıklıklar evlilik ve cinsel birleşme çekirdeğinde birleşir; toplu ifade, örtülü adlandırmanın evlilik dışı ilişki ve belirli evlenme önerilerine uzandığını da gösterir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"السر بمعنى النكاح والجماع وما يتصل به من الزنى أو خطبة المعتدة والسريّة في اختلاف المصادر","what_is_not_ar":"المناجاة العامة؛ خالص النسب؛ السرور"},"support_links":[]},{"boundary":"Anlam ay sonundaki görünmezlik zamanına bağlıdır ve genel gizlenme anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000697/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"ayın görünmediği ay sonu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hilalin ay sonunda görünmez olduğu son gün, gece veya kısa dönem adlandırılır."}}],"root_ar":"س ر ي","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hilalin kaybolduğu ay sonu zamanını gün ve gece ayrıntılarını zorlamadan karşılar.","boundary_detail":"Anlam ay sonundaki görünmezlik zamanına bağlıdır ve genel gizlenme anlamına genişletilmez.","branch_image_ar":"استتار الهلال آخر الشهر","concept_gloss":"ayın görünmediği ay sonu","contextual_glosses":[{"applicability":"Kaynak bağlamı özellikle ayın son gecesini işaret ettiğinde doğal bir zaman karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Son gün veya iki gecelik dönem olarak verilen kapsamı dışarıda bırakır.","preserves":"Ay sonundaki görünmezlik ve gece zamanını korur."},"facet_ids":["F001"],"text":"ayın son görünmez gecesi","usage_role":"contextual"}],"definition":"Ayın sonunda hilalin görünmediği son gün, son gece veya bir iki gecelik kısa dönemdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hilalin ay sonunda görünmez olduğu son gün, gece veya kısa dönem adlandırılır."}],"identity_rationale":"Kaynak ifadesi ayın sonunda hilalin görünmez olduğu son gün, gece veya iki gecelik dönemi tutarlı biçimde tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ayın sonunda hilalin görünmediği bir veya iki günlük dönem"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"ayın son gecesi"}],"lexicalization_note":"Tanım hem dönem adını hem de ayın son gecesini bildiren yapıya bağlı kullanımı ayırmadan ama aynı zaman sınırında tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ayın sönümlenmesi dalı zaman ile olay arasındaki sınırı en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal ışığın azalması ve görünmezleşme olayına, bu dal ise o olayla belirlenen son gün veya geceye odaklanır.","focus_only":"Ayın görünmediği son gün veya geceyi bir zaman dilimi olarak adlandırır.","gloss":"ayın sönümlenmesi","neighbor_only":"Ay ışığının azalması ve ayın görünmez hale gelmesi sürecini anlatır.","neighbor_ref":"root_001401/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal ayın sonunda hilalin görünmez olması çevresinde buluşur."}],"source_phrase_ar":"السرار ليلة يستسر الهلال (maqayis)؛ السرار يوم يستسر فيه الهلال آخر يوم من الشهر (ayn)؛ سرر الشهر آخر ليلة منه وكذلك سراره (sihah)؛ السرار اليوم الذي يستتر فيه القمر آخر الشهر (mufradat)","source_summary":"Tanıklıklar ay sonundaki görünmezlikte birleşir; süreyi son gün, son gece veya bir iki gece olarak ifade edebilir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"السرار وسرر الشهر لآخر الشهر حين يستتر الهلال ليلة أو ليلتين","what_is_not_ar":"سر الإنسان؛ السرور؛ سر الوادي"},"support_links":[]},{"boundary":"Anlam yalnızca verilen tamlamalarda ortaya çıkar; yalın köke genel bir öz anlamı yüklenmez.","branch_kind":"collocation","branch_ref":"root_000697/B005","candidate_links":[{"candidate_id":"cand_eef72432a253294c4c15","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"bir şeyin arı özü veya en seçkin bölümü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin katkısız, arı özü veya niteliğinin en yoğun bölümü belirtilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Topluluk, soy, vadi veya yaşam içinde en seçkin, merkezi ya da elverişli bölüm belirtilir."}}],"root_ar":"س ر ي","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca belirtilen yapılar içinde arılık ile üstün veya merkezi bölüm değerini birlikte taşır.","boundary_detail":"Anlam yalnızca verilen tamlamalarda ortaya çıkar; yalın köke genel bir öz anlamı yüklenmez.","branch_image_ar":"خالص الشيء وأكرم موضعه","concept_gloss":"bir şeyin arı özü veya en seçkin bölümü","contextual_glosses":[{"applicability":"Yapının vadiyi belirttiği ve toprağın ya da konumun üstünlüğünün anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Arı öz, seçkin topluluk, soy ve iyi yaşam kullanımlarını dışarıda bırakır.","preserves":"Bir bütün içindeki en iyi ve elverişli bölümü korur."},"facet_ids":["F002"],"text":"vadinin en iyi yeri","usage_role":"contextual"}],"definition":"Belirli yapılarda bir şeyin katkısız özü ya da bir topluluğun, soyun, yerin veya yaşamın en seçkin, merkezi ve elverişli bölümüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin katkısız, arı özü veya niteliğinin en yoğun bölümü belirtilir."},{"facet_id":"F002","role":"specialization","statement":"Topluluk, soy, vadi veya yaşam içinde en seçkin, merkezi ya da elverişli bölüm belirtilir."}],"identity_rationale":"Kaynak ifadesi bir şeyin arı özü ile bir topluluğun veya yerin en seçkin, orta ya da elverişli bölümünü yapı içinde tutarlı biçimde birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bir şeyin katkısız özü"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"topluluğunun merkezindeki en seçkin kesim"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"soyun katkısız ve en seçkin kolu"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"vadinin toprağı en iyi veya en elverişli yeri"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"bir şeyin özü ve üstün niteliğinin çekirdeği"}],"lexicalization_note":"Tanım yalnızca şey, topluluk, soy, vadi ve yaşam gibi belirtilen yapılar içindeki arı veya en iyi bölüm anlamına bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel arı öz dalı yapıya bağlı kapsamın sınırını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel öz ve çekirdek anlamına sahiptir; bu dal yalnızca belirli yapılarda yer, soy, topluluk ve yaşamın en iyi bölümünü de belirtir.","focus_only":"Topluluk, soy, vadi ve yaşam gibi belirli yapılarda merkezilik ve elverişlilik de ifade edilir.","gloss":"bir şeyin arı özü","neighbor_only":"Bir şeyin özü ve en arı bölümü yapıdan bağımsız, genel bir adlandırma olarak verilir.","neighbor_ref":"root_001248/B002","relation_type":"near_synonym","shared_zone":"Her iki dal bir bütünün katkısız, seçkin veya çekirdek bölümünü gösterebilir."}],"source_phrase_ar":"السر خالص الشيء وسر النسب (maqayis)؛ سر كل شيء خالصه وسر الوادي وسراره أطيبه ترابا (jamhara)؛ في سر قومه أي في أوسطهم وسر الوادي أفضل موضع (sihah)؛ استعير للخالص ومنه سر الوادي وسرارته (mufradat)","source_summary":"Tanıklıklar katkısız öz anlamında birleşir; toplulukta seçkin veya orta kesim, vadide en iyi yer ve yaşamda en iyi durum bu yapıya bağlı görünümlerdir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"سر الشيء وسر النسب وسر القوم وسر الوادي وسرارته وسرارة الفضل والعيش","what_is_not_ar":"الكتمان المجرد؛ السرة؛ السرير"},"support_links":["sup_35209214a5688a067e3f"]},{"boundary":"Anlam hem bedendeki kalıcı yeri hem de doğum sırasında kesilen parçayı içerir.","branch_kind":"mixed_non_bare","branch_ref":"root_000697/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"göbek ve kesilen göbek bağı parçası","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Göbek bağının kesilmesinden sonra karnın ortasında kalan yer belirtilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bebekten kesilen göbek bağı parçası ve bu parçayı kesme eylemi belirtilir."}}],"root_ar":"س ر ي","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedendeki kalıcı yer ile doğumda kesilen parçayı birlikte karşılayan açıklayıcı üst karşılıktır.","boundary_detail":"Anlam hem bedendeki kalıcı yeri hem de doğum sırasında kesilen parçayı içerir.","branch_image_ar":"سرة البطن وما يقطع منها","concept_gloss":"göbek ve kesilen göbek bağı parçası","contextual_glosses":[{"applicability":"Eylem biçiminin doğumdan sonra göbek bağı parçasını kesmeyi anlattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Karında kalan göbek yerini adlandırma anlamını karşılamaz.","preserves":"Kesilen göbek bağı parçasını ve kesme eylemini korur."},"facet_ids":["F002"],"text":"bebeğin göbek bağını kesmek","usage_role":"contextual"}],"definition":"Karnın ortasında göbek bağının kesilmesinden sonra kalan yer ile doğum sırasında bebekten kesilen göbek bağı parçasıdır; ayrıca bu parçayı kesme eylemini kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Göbek bağının kesilmesinden sonra karnın ortasında kalan yer belirtilir."},{"facet_id":"F002","role":"specialization","statement":"Bebekten kesilen göbek bağı parçası ve bu parçayı kesme eylemi belirtilir."}],"identity_rationale":"Kaynak ifadesi karındaki göbek yerini, doğumdan sonra kalan bölümü ve bebekten kesilen göbek bağı parçasını açıkça ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"göbek"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bebekten kesilen göbek bağı parçası"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"bebeğin göbek bağı parçasını kesmek"}],"lexicalization_note":"Tanım ad biçimlerindeki göbek ve kesilen parça anlamlarını, kesme eylemini bildiren türemiş kullanımdan ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yenidoğan örtüsü dalı göbek bağı parçasıyla karışabilecek doğum dokusunu ayırır.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Komşu dal bebeğin üzerindeki geçici deri örtüsünü, bu dal ise karında kalan göbeği ve kesilen göbek bağı parçasını adlandırır.","focus_only":"Göbek yeri, kesilen göbek bağı parçası ve bu parçanın kesilmesi temel kapsamdadır.","gloss":"yenidoğan üzerindeki deri örtüsü","neighbor_only":"Doğum sırasında bebeğin başı ve elleri üzerinde bulunan ince deri örtüsü anlatılır.","neighbor_ref":"root_001424/B010","relation_type":"thematic","shared_zone":"Her iki dal doğum sırasında bebekle birlikte görülen bedensel bir parçaya ilişkindir."}],"source_phrase_ar":"السرة سرة الإنسان (maqayis)؛ السرة في البطن موضع السرر الذي يقطع من الصبي (jamhara)؛ السر ما تقطعه القابلة من سرة الصبي (sihah)؛ سرة البطن ما يبقى بعد القطع والسر والسرر لما يقطع منها (mufradat)","source_summary":"Tanıklıklar göbekte kalan yer ile bebekten kesilen parçayı birbirinden ayırır ve ilgili kesme eylemini aynı beden alanına bağlar.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"السرة والسر والسرر لما يبقى أو يقطع من سرة الصبي وموضع السرة في البطن","what_is_not_ar":"سر النسب؛ أسرار الكف؛ سرر الشهر"},"support_links":[]},{"boundary":"Hastalığın deveye özgü olduğu korunmalı, kesin anatomik yeri tek bir bölgeye indirgenmemelidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000697/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"devede gövde içi ağrı hastalığı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Deve veya dişi deveyi etkileyen bir ağrı ya da hastalık belirtilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hastalığın yeri göbek, göğüs veya göğsün altındaki yastıksı bölüm olarak değişik biçimde verilir."}}],"root_ar":"س ر ي","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Deveye özgü hastalığı korur ve tartışmalı anatomik yeri gereksiz biçimde kesinleştirmez.","boundary_detail":"Hastalığın deveye özgü olduğu korunmalı, kesin anatomik yeri tek bir bölgeye indirgenmemelidir.","branch_image_ar":"وجع البعير في باطنه","concept_gloss":"devede gövde içi ağrı hastalığı","contextual_glosses":[{"applicability":"Bağlam rahatsızlığı göğsün altındaki yastıksı bölgeye yerleştirdiğinde hayvanı nitelemek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Göbek veya göğüs konumunu veren diğer tanıklıkları dışarıda bırakır.","preserves":"Deveye özgü rahatsızlığı ve gövde içindeki ağrı yerini korur."},"facet_ids":["F001","F002"],"text":"göğüs altı ağrısı bulunan deve","usage_role":"contextual"}],"definition":"Deve veya dişi devede göbek, göğüs ya da göğsün altındaki yastıksı bölüm çevresinde görüldüğü aktarılan bir ağrı veya hastalıktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Deve veya dişi deveyi etkileyen bir ağrı ya da hastalık belirtilir."},{"facet_id":"F002","role":"source_variant","statement":"Hastalığın yeri göbek, göğüs veya göğsün altındaki yastıksı bölüm olarak değişik biçimde verilir."}],"identity_rationale":"Kaynak ifadesi develerde bir hastalık veya ağrıda birleşir, fakat yerini göbek, göğüs ya da göğüs altındaki yastıksı bölüm olarak farklı verir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"devede göbek, göğüs veya göğüs altı ağrısı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bu gövde ağrısına tutulmuş deve"}],"lexicalization_note":"Tanım hastalık adını ve bu hastalığa tutulmuş deveyi bildiren yapıya bağlı kullanımı birbirinden ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; belirli uzuv hastalığı anatomik belirsizliği en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal gövdenin iç veya alt bölgelerindeki değişken bir ağrıyı, komşu dal ise belirli biçimde üst ön bacak hastalığını anlatır.","focus_only":"Rahatsızlık göbek, göğüs veya göğüs altındaki yastıksı bölüm çevresine yerleştirilir.","gloss":"devede üst ön bacak hastalığı","neighbor_only":"Rahatsızlık özellikle devenin üst ön bacak bölümünü etkiler.","neighbor_ref":"root_001023/B007","relation_type":"same_field","shared_zone":"Her iki dal develerde görülen, beden bölümüne bağlanan bir hastalık adıdır."}],"source_phrase_ar":"السرر داء يأخذ البعير في سرته (maqayis)؛ السرر داء يصيب الإبل في صدورها (jamhara)؛ بعير أسر وناقة سراء (sihah)؛ وجع يأخذ في الكركرة (tahdhib)","source_summary":"Tanıklıklar deve hastalığı çekirdeğinde birleşir, ancak rahatsızlığın anatomik yerini göbek, göğüs veya göğüs altı olarak farklılaştırır.","sources":["MQ","JA","SI","TA"],"what_is_ar":"السرر داء أو وجع في البعير أو الناقة مع اختلاف موضعه بين السرة والصدر والكركرة","what_is_not_ar":"السرة المقطوعة؛ التجويف؛ خطوط الكف"},"support_links":[]},{"boundary":"Genel iç bölüm değil, içi boş nesne veya beden ile oyuğa çubuk yerleştirme işlemidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000697/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"içi oyuk olma ve oyuğa çubuk yerleştirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ateş çubuğu, boru biçimli çubuk veya insan içi oyuk olarak nitelenir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ateş yakma amacıyla oyuk çubuğun içine başka bir çubuk parçası yerleştirilir."}}],"root_ar":"س ر ي","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem oyukluk niteliğini hem de ateş çubuğuna özgü yerleştirme işlemini eksiksiz karşılar.","boundary_detail":"Genel iç bölüm değil, içi boş nesne veya beden ile oyuğa çubuk yerleştirme işlemidir.","branch_image_ar":"جوف الزند والقناة","concept_gloss":"içi oyuk olma ve oyuğa çubuk yerleştirme","contextual_glosses":[{"applicability":"Nitelemenin kamış veya boru biçimli bir çubuğun iç boşluğuna yöneldiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan için oyukluk nitelemesini ve oyuğa parça yerleştirme işlemini dışarıda bırakır.","preserves":"İçi oyuk olma niteliğini ve çubuk biçimli nesneyi korur."},"facet_ids":["F001"],"text":"içi oyuk boru biçimli çubuk","usage_role":"contextual"}],"definition":"Bir ateş çubuğunun, boru biçimli çubuğun ya da kişinin içinin oyuk olmasıdır; ayrıca ateş yakmak için çubuğun oyuğuna başka bir parça yerleştirme işlemini belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ateş çubuğu, boru biçimli çubuk veya insan içi oyuk olarak nitelenir."},{"facet_id":"F002","role":"specialization","statement":"Ateş yakma amacıyla oyuk çubuğun içine başka bir çubuk parçası yerleştirilir."}],"identity_rationale":"Kaynak ifadesi içi oyuk olma niteliğini ateş çubuğu, kamış benzeri boru ve insan için; oyuğa çubuk yerleştirme işlemini de ilgili eylem için destekler.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"ateş çubuğunun oyuğuna tutuşturma çubuğu yerleştirmek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"içi oyuk boru biçimli çubuk"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"içi oyuk kişi"}],"lexicalization_note":"Tanım, yapıya bağlı içi oyuk nitelemeleri ile ateş çubuğunun oyuğuna parça yerleştiren eylemi ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel iç boşluk dalı nitelik ile özel işlem sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel iç ve boşluk kavramıdır; bu dal belirli oyuk nitelemeleriyle ateş çubuğuna özgü yerleştirme işlemini birleştirir.","focus_only":"Belirli nesne ve kişilerin oyukluğu ile ateş çubuğunun oyuğuna parça yerleştirme işlemi vardır.","gloss":"bir şeyin içi ve boşluğu","neighbor_only":"Her tür şeyin içi, dibi, karın bölgesi ve iç hacmin genişliği genel olarak adlandırılır.","neighbor_ref":"root_000279/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal bir nesne veya bedenin iç boşluğu ve oyuk yapısıyla ilgilidir."}],"source_phrase_ar":"سررت الزند وذلك أن يبقى أسر أي أجوف (maqayis)؛ قناة سراء أي جوفاء (maqayis)؛ سر زندك فإنه أسر أي أجوف (sihah)؛ رجل أسر إذا كان أجوف (tahdhib)","source_summary":"Tanıklıklar içi oyuk olma niteliğinde birleşir ve ateş yakma aracında bu oyuğa bir çubuk yerleştirme işlemini aynı çekirdeğe bağlar.","sources":["MQ","SI","TA"],"what_is_ar":"سر الزند إذا جعل في جوفه عود وقدح به والقناة السراء والرجل الأسر بمعنى الأجوف","what_is_not_ar":"السرة؛ السرور؛ السرار القمري"},"support_links":[]},{"boundary":"Anlam avuç ve alın yüzeyindeki doğal çizgilerle sınırlıdır; gizli bilgi anlamına geçmez.","branch_kind":"bare","branch_ref":"root_000697/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"avuç ve alın çizgileri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Avuç içinde veya alın ve yüzde görülen doğal çizgi ve kırışıklıklar belirtilir."}}],"root_ar":"س ر ي","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki anatomik yüzeydeki doğal çizgi ve kırışıklıkları kısa ve eksiksiz biçimde karşılar.","boundary_detail":"Anlam avuç ve alın yüzeyindeki doğal çizgilerle sınırlıdır; gizli bilgi anlamına geçmez.","branch_image_ar":"خطوط الكف والجبهة","concept_gloss":"avuç ve alın çizgileri","contextual_glosses":[{"applicability":"Bağlam çizgileri özellikle alın veya yüz yüzeyinde gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Avuç içindeki çizgileri adlandıran kullanımı dışarıda bırakır.","preserves":"Alın ve yüzdeki çizgi veya kırışıklık anlamını korur."},"facet_ids":["F001"],"text":"alın kırışıklıkları","usage_role":"contextual"}],"definition":"Avuç içinin doğal çizgileri ile alın veya yüzde görülen çizgi ve kırışıklıklardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Avuç içinde veya alın ve yüzde görülen doğal çizgi ve kırışıklıklar belirtilir."}],"identity_rationale":"Kaynak ifadesi avuç içindeki çizgileri ve alındaki çizgi ya da kırışıklıkları ortak bir beden yüzeyi izi olarak açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"avuç içi çizgileri"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"alın veya yüz çizgileri ve kırışıklıkları"}],"lexicalization_note":"Tanım yalın biçimlerin doğrudan beden çizgisi anlamını verir ve yapıya bağlı başka okumalar eklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kat izi dalı doğal beden çizgisi ile oluşmuş yüzey izi ayrımını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal katlama ve kırılmanın nesne yüzeyindeki izidir; bu dal avuç ve alındaki doğal beden çizgileridir.","focus_only":"Çizgiler avuç içi, alın veya yüzün doğal anatomik izleridir.","gloss":"kat ve kırılma izi","neighbor_only":"İz kumaş veya deri gibi bir yüzeyde kırılma ve ilk katlama sonucunda oluşur.","neighbor_ref":"root_001078/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal bir yüzeyde görülen çizgisel kırılma veya kat izini anlatabilir."}],"source_phrase_ar":"الأسرار خطوط باطن الراحة (maqayis)؛ السر والسرار والجميع الأسرار خطوط راحة الكف (ayn)؛ السرر واحد أسرار الكف والجبهة (sihah)؛ أسرة الراحة وأسارير الجبهة (mufradat)","source_summary":"Tanıklıklar avuç içi çizgileri ve alın kırışıklıklarını aynı beden yüzeyi izi alanında birleştirir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"أسرار الكف وأسراره وأسارير الجبهة وخطوط باطن الراحة والكسور في الجبهة","what_is_not_ar":"السر المكتوم؛ السرة؛ السرر القمري"},"support_links":[]},{"boundary":"Duygusal sevinç ile iyi ve rahat yaşam durumu ayrı görünümler olarak korunmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000697/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"sevinç ve gönence","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Üzüntüden uzak, içte duyulan sevinç ve birini sevindirme durumu belirtilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sıkıntı ve darlığın karşıtı olan rahatlık, bolluk ve iyi yaşam durumu belirtilir."}}],"root_ar":"س ر ي","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Duygusal sevinç ile sıkıntının karşıtı olan rahat ve bolluk içindeki durumu birlikte karşılar.","boundary_detail":"Duygusal sevinç ile iyi ve rahat yaşam durumu ayrı görünümler olarak korunmalıdır.","branch_image_ar":"فرح خفي ورخاء","concept_gloss":"sevinç ve gönence","contextual_glosses":[{"applicability":"Bir kişinin başka bir kişide sevinç doğurduğu eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Rahatlık, bolluk ve iyi yaşam durumu anlamlarını karşılamaz.","preserves":"Sevinç duygusunu ve bu duygunun bir başkasınca oluşturulmasını korur."},"facet_ids":["F001"],"text":"onu sevindirdi","usage_role":"contextual"}],"definition":"Üzüntünün bulunmadığı, içte duyulan sevinçtir; ayrıca sıkıntı ve darlığın karşıtı olan rahatlık, bolluk ve iyi yaşam durumunu belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Üzüntüden uzak, içte duyulan sevinç ve birini sevindirme durumu belirtilir."},{"facet_id":"F002","role":"extension","statement":"Sıkıntı ve darlığın karşıtı olan rahatlık, bolluk ve iyi yaşam durumu belirtilir."}],"identity_rationale":"Kaynak ifadesi üzüntüden uzak sevinç ile sıkıntının karşıtı olan gönenceyi aynı dalda açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"üzüntüden uzak iç sevinci"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"beni sevindirdi"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"rahatlık, bolluk ve gönence"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"iyilik eden ve sevindiren kişi"}],"lexicalization_note":"Tanım yalın sevinç ve gönence biçimlerini, sevindirme eylemini ve kişiyi niteleyen yapıya bağlı kullanımı ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel sevinç dalı duyguyla gönence arasındaki ek kapsamı en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel sevinçtir; bu dal içte duyulan sevinç yanında darlığın karşıtı rahatlık ve bolluk durumunu da taşır.","focus_only":"Sıkıntının karşıtı olan rahatlık, bolluk ve iyi yaşam durumu da kapsanır.","gloss":"sevinç ve coşku","neighbor_only":"Genel sevinç ve coşku, içte kalma veya gönence koşulu olmadan ifade edilir.","neighbor_ref":"root_000158/B002","relation_type":"near_synonym","shared_zone":"Her iki dal üzüntünün karşıtı olan sevinç ve mutlu olma durumunu kapsar."}],"source_phrase_ar":"السرور أمر خال من الحزن (maqayis)؛ السر ضد الضر وقال قوم السر والسرور واحد (jamhara)؛ السراء الرخاء نقيض الضراء (sihah)؛ السرور ما ينكتم من الفرح (mufradat)","source_summary":"Tanıklıklar sevinci üzüntüden uzak bir iç durum olarak verir ve aynı alanı sıkıntının karşıtı olan rahat yaşam ile genişletir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"السرور والمسرة والسراء والسر بمعنى ضد الضر أو موضع الفرح والرخاء","what_is_not_ar":"السر المكتوم؛ النكاح؛ السرير"},"support_links":[]},{"boundary":"Somut yatak çekirdeği, başın dayanağı ve yaşamın rahat düzeni gibi yapıya bağlı uzantılardan ayrılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000697/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"oturma, yaslanma veya dinlenme yeri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanın oturduğu, yaslandığı veya dinlendiği yatak ya da destekli yer belirtilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başın dayandığı yer veya yaşamın yerleşik rahatlığı yapıya bağlı uzantılar olarak belirtilir."}}],"root_ar":"س ر ي","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Somut yatağı ve dayanak işlevini korurken yapıya bağlı yerleşme uzantılarına temel sağlar.","boundary_detail":"Somut yatak çekirdeği, başın dayanağı ve yaşamın rahat düzeni gibi yapıya bağlı uzantılardan ayrılmalıdır.","branch_image_ar":"موضع الاستقرار والاتكاء","concept_gloss":"oturma, yaslanma veya dinlenme yeri","contextual_glosses":[{"applicability":"Yapı doğrudan başın oturduğu veya dayandığı bölgeyi anlattığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel yatak, oturma yeri ve rahat yaşam düzeni anlamlarını dışarıda bırakır.","preserves":"Dayanma ve yerleşme ilişkisini baş bölgesi için korur."},"facet_ids":["F002"],"text":"başın dayandığı yer","usage_role":"contextual"}],"definition":"Oturmak, yaslanmak veya dinlenmek için kullanılan yatak ya da destekli yerdir; yapıya bağlı kullanımlarda başın dayandığı yeri veya yaşamın yerleşik rahatlığını belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanın oturduğu, yaslandığı veya dinlendiği yatak ya da destekli yer belirtilir."},{"facet_id":"F002","role":"extension","statement":"Başın dayandığı yer veya yaşamın yerleşik rahatlığı yapıya bağlı uzantılar olarak belirtilir."}],"identity_rationale":"Kaynak ifadesi oturulan veya yaslanılan yatağı, başın dayandığı yeri ve yaşamın yerleşik rahatlığını ortak bir dayanma ve yerleşme ilişkisiyle destekler.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"oturulan, yaslanılan veya yatılan yer"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"başın dayandığı yer"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"yaşamın yerleşik rahatlığı ve dinginliği"}],"lexicalization_note":"Tanım yalın yatak ve oturma desteğini, başın dayandığı yer ile yaşamın yerleşik rahatlığını bildiren yapılardan ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel döşenmiş yatak dalı genel nesne ile özel tür ayrımını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal döşenmiş ve örtülü yerdeki özel yatağa bağlıdır; bu dal daha genel destekli yeri ve mecazlaşmış dayanak uzantılarını içerir.","focus_only":"Genel yatak ve oturma desteği yanında başın dayanağı ve yaşamın rahat düzeni uzantıları vardır.","gloss":"örtülü yerde süslü yatak","neighbor_only":"Özellikle örtülü bir bölmede bulunan döşenmiş ve süslü oturma yatağı belirtilir.","neighbor_ref":"root_000026/B004","relation_type":"near_synonym","shared_zone":"Her iki dal oturmak, yaslanmak veya dinlenmek için hazırlanmış bir yatak türünü kapsar."}],"source_phrase_ar":"السرير وجمعه سرر وأسرة (maqayis)؛ سرير الرأس مستقره (maqayis)؛ السرير معروف والعدد أسرة والجميع السرر (tahdhib)؛ السرير الذي يجلس عليه من السرور (mufradat)","source_summary":"Tanıklıklar oturulan ya da dinlenilen destekli yer çekirdeğinde birleşir; başın dayanağı ve rahat yaşam düzeni bu çekirdeğin yapıya bağlı uzantılarıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"السرير والسرر والأسرة وسرير الرأس وسرير العيش وما يستقر عليه أو عنده","what_is_not_ar":"سر النسب؛ السرة؛ السرار القمري"},"support_links":[]},{"boundary":"Anlam bitkinin nemli üst bölümleridir; bütün bitkiyi veya yalnızca tek bir ucu anlatmaz.","branch_kind":"collocation","branch_ref":"root_000697/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"bitkinin nemli üst bölümleri","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bitkinin uç veya üst gövde bölümündeki taze ve nemli kısımlar belirtilir."}}],"root_ar":"س ر ي","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Uçlar ile gövdenin üst yarısını ortak tazelik ve nemlilik özelliği altında karşılar.","boundary_detail":"Anlam bitkinin nemli üst bölümleridir; bütün bitkiyi veya yalnızca tek bir ucu anlatmaz.","branch_image_ar":"غضارة أطراف النبات","concept_gloss":"bitkinin nemli üst bölümleri","contextual_glosses":[{"applicability":"Bağlam özellikle hoş kokulu otların en taze uçlarını gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka bitkilerin gövde üst yarılarını kapsayan daha geniş kullanımı dışarıda bırakır.","preserves":"Bitkinin üst, taze ve nemli kısmını korur."},"facet_ids":["F001"],"text":"hoş kokulu otların nemli uçları","usage_role":"contextual"}],"definition":"Bitkiyi belirten yapıda, hoş kokulu otların en nemli uçları veya bitki gövdelerinin üst yarılarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bitkinin uç veya üst gövde bölümündeki taze ve nemli kısımlar belirtilir."}],"identity_rationale":"Kaynak ifadesi bitkinin en nemli uçlarını ve gövdelerin üst yarılarını birlikte verir; geçici dal imgesi yalnızca uçlarla sınırlandırılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bitkilerin nemli uçları veya gövdelerinin üst yarıları"}],"lexicalization_note":"Tanım yalnızca bitkiyi belirten yapıda üst, taze ve nemli bölümler anlamını taşır; yalın anlama genişlemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; taze otsu bitki dalı bütün ile üst bölüm arasındaki sınırı en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal otsu bitkinin bütününü, bu dal ise belirli yapı içinde yalnızca üst ve nemli bölümlerini adlandırır.","focus_only":"Bitkinin yalnızca nemli uçları veya gövdesinin üst yarıları belirtilir.","gloss":"taze otsu bitki","neighbor_only":"Ağaç sayılmayan yeşil ve taze otsu bitkinin bütünü adlandırılır.","neighbor_ref":"root_000141/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal yeşil, taze ve nemli bitki dokusuyla ilgilidir."}],"source_phrase_ar":"أطراف الريحان تسمى سرورا لأنها أرطب شيء فيه (maqayis)؛ السرور من النبات أنصاف سوقها العلى (tahdhib)","source_summary":"Tanıklıklar bitkinin üst ve nemli bölümünde birleşir; biri özellikle hoş kokulu otların uçlarını, diğeri gövdelerin üst yarılarını öne çıkarır.","sources":["MQ","TA"],"what_is_ar":"سرور النبات وأطراف الرياحين أو أنصاف سوق النبات العليا الرطبة","what_is_not_ar":"سرور الفرح؛ سرير العيش؛ قشور الكمأة"},"support_links":[]},{"boundary":"Anlam yer mantarının kendisi değil, onun yüzeyine yapışmış kabuk ve toprak örtüsüdür.","branch_kind":"collocation","branch_ref":"root_000697/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"yer mantarı üzerindeki kabuk ve toprak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yer mantarının üzerinde kabuk, çamur veya topraktan oluşan bir yüzey örtüsü bulunur."}}],"root_ar":"س ر ي","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Mantarın kendisiyle yüzeyine yapışan kabuklu toprak örtüsünü açıkça ayırır.","boundary_detail":"Anlam yer mantarının kendisi değil, onun yüzeyine yapışmış kabuk ve toprak örtüsüdür.","branch_image_ar":"قشور الكمأة وترابها","concept_gloss":"yer mantarı üzerindeki kabuk ve toprak","contextual_glosses":[{"applicability":"Bağlam yüzey örtüsünü mantara yapışmış kabuk ve toprak olarak betimlediğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mantar yüzeyi, yapışma, kabuk ve toprak unsurlarının tümünü korur."},"facet_ids":["F001"],"text":"yer mantarına yapışmış topraklı kabuk","usage_role":"contextual"}],"definition":"Yer mantarının yüzeyinde bulunan veya ona yapışan kabuk, çamur ve toprak örtüsüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yer mantarının üzerinde kabuk, çamur veya topraktan oluşan bir yüzey örtüsü bulunur."}],"identity_rationale":"Kaynak ifadesi yer mantarının üzerinde bulunan kabuk, çamur ve toprak örtüsünü doğrudan ve tutarlı biçimde tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"yer mantarı üzerindeki kabuk, çamur ve toprak"}],"lexicalization_note":"Tanım yalnızca yer mantarını belirten yapıda yüzey kabuğu, çamur ve toprak anlamını taşır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kuruyan yer kabuğu dalı mantar yüzeyi ile çevre zemin arasındaki sınırı açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal kuruyup ayrılan zemin kabuğunu daha geniş biçimde anlatır; bu dal yalnızca mantarın kendi yüzeyindeki yapışık örtüdür.","focus_only":"Örtü doğrudan yer mantarının üzerinde bulunan kabuk, çamur ve topraktır.","gloss":"kuruyup ayrılan yer kabuğu","neighbor_only":"Kuruyup çatlayan yer veya çamur kabuğu ve yer mantarının üstündeki yükselmiş zemin kabuğu da kapsanır.","neighbor_ref":"root_001250/B009","relation_type":"near_neighbor","shared_zone":"Her iki dal yer mantarı çevresindeki kabuklu toprak oluşumuna değinebilir."}],"source_phrase_ar":"السرر ما على الكمأة من القشور والطين (sihah)؛ السرار ما على الكمأة من القشور والتراب (tahdhib)","source_summary":"Tanıklıklar yer mantarının üzerindeki kabuklu ve topraklı örtüde birleşir; örtünün maddesi çamur veya toprak olarak değişebilir.","sources":["SI","TA"],"what_is_ar":"سرر الكمأة وأسرارها لما عليها من القشور والطين أو التراب","what_is_not_ar":"خطوط الكف؛ سرر الشهر؛ سرر الصبي"},"support_links":[]},{"boundary":"Uzman ve kavrayışlı kişi çekirdeği, yakın ve sevilen kişi anlamıyla özdeşleştirilmemelidir.","branch_kind":"bare","branch_ref":"root_000697/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"işlerin inceliğini bilen becerikli kişi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir işin inceliklerini bilir, güçlü kavrayış gösterir ve o işe ustalıkla girer."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı bir kullanım aynı biçim ailesini sevilen veya çok yakın kişi için kullanır."}}],"root_ar":"س ر ي","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın baskın uzmanlık ve kavrayış çekirdeğini doğal biçimde karşılar; yakın kişi kullanımı ayrıca gösterilir.","boundary_detail":"Uzman ve kavrayışlı kişi çekirdeği, yakın ve sevilen kişi anlamıyla özdeşleştirilmemelidir.","branch_image_ar":"نفاذ إلى خفايا الأمور","concept_gloss":"işlerin inceliğini bilen becerikli kişi","contextual_glosses":[{"applicability":"Bir kişinin belirli bir işte bilgili, kavrayışlı ve deneyimli olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sevilen veya yakın kişi anlamını ve genel kişi adlandırmasını dışarıda bırakır.","preserves":"Belirli bir işi derinden bilme ve o alanda kavrayışlı olma yönünü korur."},"facet_ids":["F001"],"text":"bu işin bütün inceliklerini bilir","usage_role":"contextual"},{"applicability":"Biçimin bilgi ve uzmanlık değil, sevgi ve yakınlık bildiren hitap olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bilgili, kavrayışlı ve işlere ustalıkla giren kişi çekirdeğini karşılamaz.","preserves":"Sevilen ve yakın kişi için kullanılan özel hitap değerini korur."},"facet_ids":["F002"],"text":"sevdiğim yakın kişi","usage_role":"contextual"}],"definition":"Bir işin inceliklerini bilen, kavrayışlı ve o işin içine ustalıkla girebilen kişidir; ayrı bir kullanımda sevilen veya çok yakın kişi için söylenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir işin inceliklerini bilir, güçlü kavrayış gösterir ve o işe ustalıkla girer."},{"facet_id":"F002","role":"source_variant","statement":"Ayrı bir kullanım aynı biçim ailesini sevilen veya çok yakın kişi için kullanır."}],"identity_rationale":"Kaynak ifadesinin ana bölümü işleri derinden bilen becerikli kişiyi destekler; aynı biçim ailesindeki sevgili veya yakın kişi kullanımı ayrı bir kaynak uzantısıdır.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"işlerin inceliğini bilen kavrayışlı kişi"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"sevdiğim ve çok yakın bulduğum kişi"}],"lexicalization_note":"Tanım yalın biçimlerdeki bilgili ve becerikli kişi anlamını verir, ayrı sevgi hitabını yalnızca kaynak uzantısı olarak korur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; derin kavrayış dalı yeti ile bu yetiyi taşıyan kişi arasındaki sınırı gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal bilme ve iç görüş yetisine odaklanır; bu dal bu yetiye sahip becerikli kişiyi adlandırır ve ayrı bir yakınlık kullanımı taşır.","focus_only":"Bilgi bir kişiyi işlerin içine ustalıkla giren uzman olarak niteler ve ayrı yakınlık kullanımı taşır.","gloss":"derin kavrayış","neighbor_only":"Bilme, doğrulama, düşünsel kavrayış ve kanıta dayalı iç görüş bir yeti veya durum olarak anlatılır.","neighbor_ref":"root_000121/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal yüzeyin ötesine geçen bilgi, kavrayış ve bir konuyu derinden anlama alanındadır."}],"source_phrase_ar":"السرسور العالم الفطن (maqayis)؛ السرسور العالم الفطن الدخال في الأمور (sihah)؛ سرسور هذا الأمر إذا كان عالما به (tahdhib)؛ سرسوري وسرسورتي أي حبيبي وخاصتي (tahdhib)","source_summary":"Tanıklıklar bilgili, kavrayışlı ve işlere nüfuz eden kişi çekirdeğinde birleşir; toplu ifade ayrıca sevilen veya yakın kişi kullanımını korur.","sources":["MQ","SI","TA"],"what_is_ar":"السرسور العالم الفطن الدخال في الأمور ومن يقوم على المال أو يكون خاصة وحبيبا","what_is_not_ar":"السرور؛ السرير؛ السرار القمري"},"support_links":[]},{"boundary":"Anlam yükseltinin kendisi değil, onun üzerinde yer alan kumdur.","branch_kind":"bare","branch_ref":"root_000697/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"tepecik üzerindeki kum tabakası","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kum, küçük bir tepe veya yükseltinin üzerinde yer alan tabaka olarak belirtilir."}}],"root_ar":"س ر ي","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kumun türünden çok küçük bir yükselti üzerindeki konumunu eksiksiz biçimde belirtir.","boundary_detail":"Anlam yükseltinin kendisi değil, onun üzerinde yer alan kumdur.","branch_image_ar":"رمل على الأكمة","concept_gloss":"tepecik üzerindeki kum tabakası","contextual_glosses":[{"applicability":"Bir metinde küçük yükseltinin üstünü kaplayan kumdan söz edildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kum ile tepe üzerindeki konum ilişkisini tam olarak korur."},"facet_ids":["F001"],"text":"tepenin üstündeki kum","usage_role":"contextual"}],"definition":"Küçük bir tepe veya yükseltinin üzerinde bulunan kum tabakasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kum, küçük bir tepe veya yükseltinin üzerinde yer alan tabaka olarak belirtilir."}],"identity_rationale":"Tek kaynak ifadesi, küçük bir yükseltinin üzerinde bulunan kumu doğrudan ve herhangi bir ek koşul olmadan tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"küçük bir tepenin üzerindeki kum"}],"lexicalization_note":"Tanım yalın biçimin doğrudan küçük yükselti üzerindeki kum anlamını verir ve başka kum oluşumlarını eklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yüksek kum tepesi dalı taşıyıcı yükselti ile kum oluşumu ayrımını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal kumdan oluşan yükseltiyi, bu dal ise önceden var olan küçük yükseltinin üzerindeki kumu adlandırır.","focus_only":"Kum, başka bir küçük yükseltinin üzerinde bulunan tabaka olarak tanımlanır.","gloss":"yüksek kum tepesi","neighbor_only":"Kumun kendisi yükselmiş ve uzaktan belirgin bir kum tepesi oluşturur.","neighbor_ref":"root_001607/B007","relation_type":"near_neighbor","shared_zone":"Her iki dal yükselti ve kumun bir arada bulunduğu yer biçimini anlatır."}],"source_phrase_ar":"السري ما على الأكمة من الرمل (maqayis)","source_qualifications":[{"kind":"sole_attestation","summary":"Küçük bir tepe veya yükselti üzerinde bulunan kum olarak tanıklanır."}],"source_summary":"Bu anlam yalnızca tek sözlük tanıklığına dayanır ve küçük yükselti üzerindeki kumu bildirir.","sources":["MQ"],"what_is_ar":"السري لما يكون على الأكمة من الرمل","what_is_not_ar":"سر الوادي؛ سرار الشهر؛ السرير"},"support_links":[]},{"boundary":"Dal gece vakti yapılan yolculukla sınırlıdır; asker birliği adı yalnızca ilişkili bir kullanım olarak tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_000702/B001","candidate_links":[{"candidate_id":"cand_b288aa75c0cb6835b3d9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"geceleyin yol alma ve gece götürme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin ya da topluluğun geceleyin yol alması."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birini beraberinde geceleyin götürmek."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gece ilerleyen topluluğu veya gece gelen ve ilerleyen bulutu adlandırmak."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir asker birliğini adlandırmak; kaynak ifadesi bu kullanım için gece yolculuğu şartı koymaz."}}],"root_ar":"س ر ي","root_id":"root_000702","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gece vaktini kurucu koşul olarak koruyan eylem çekirdeği ve onun ettirgen kullanımını birlikte karşılar.","boundary_detail":"Dal gece vakti yapılan yolculukla sınırlıdır; asker birliği adı yalnızca ilişkili bir kullanım olarak tutulur.","branch_image_ar":"السُّرى وسير الليل","concept_gloss":"geceleyin yol alma ve gece götürme","contextual_glosses":[{"applicability":"Öznenin kendisinin gece vakti ilerlediği temel eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öznenin gece vakti yol alma eylemini eksiksiz korur."},"facet_ids":["F001"],"text":"geceleyin yol almak","usage_role":"general"},{"applicability":"Bir kişinin başka birini beraberinde geceleyin götürdüğü kalıplarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gece koşulunu ve götüren ile götürülen katılımcılar arasındaki ayrımı korur."},"facet_ids":["F002"],"text":"birini gece götürmek","usage_role":"contextual"},{"applicability":"Gece gelen veya gece ilerleyen bulutun adlandırıldığı bağlamla sınırlıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bulut katılımcısını ve geceleyin gelme ya da ilerleme özelliğini korur."},"facet_ids":["F003"],"text":"gece gelen bulut","usage_role":"contextual"}],"definition":"Temel anlam, geceleyin yol almak veya birini gece götürmektir. Gece ilerleyen topluluk ile gece gelen bulut bu harekete göre adlandırılır; asker birliği adıysa yalnızca ilişkili bir kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin ya da topluluğun geceleyin yol alması."},{"facet_id":"F002","role":"specialization","statement":"Birini beraberinde geceleyin götürmek."},{"facet_id":"F003","role":"associated_use","statement":"Gece ilerleyen topluluğu veya gece gelen ve ilerleyen bulutu adlandırmak."},{"facet_id":"F004","role":"associated_use","statement":"Bir asker birliğini adlandırmak; kaynak ifadesi bu kullanım için gece yolculuğu şartı koymaz."}],"identity_rationale":"Kaynak ifadesinin çekirdeği geceleyin yol alma eylemidir; birini gece götürme, gece ilerleyen topluluk ve gece gelen bulut da bu çekirdeğe bağlıdır. Asker birliği anlamı ise kaynakta ayrıca yer alır, fakat onun gece yolculuğu yaptığı açıkça belirtilmez; bu nedenle dal ancak bu adlandırma çekirdek anlamla özdeş sayılmazsa korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"gece yolculuğu"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"geceleyin yol aldı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"geceleyin yol aldı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"onu gece götürdü"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"onu gece götürdü"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"gece gelen veya ilerleyen bulut"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"gece yol alan topluluk"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"küçük asker birliği"}],"lexicalization_note":"Tanım, bağımsız biçimlerdeki gece yolculuğunu, birini gece götürme kalıplarını ve bunlara bağlı adlandırmaları ayrı yüzler olarak gösterir.","neighbor_coverage_note":"Adayların tümü değerlendirildi; gece yolculuğunun çaba derecesini ve genel yolculuktan zaman bakımından ayrımını en açık gösteren iki komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal için geceleyin yol almak yeterlidir; komşu dal ise geceyi aşmaya dönük sürekli çabayı ve zorluğu anlamın parçası yapar.","focus_only":"Gece vaktini şart koşar, fakat yorucu çaba veya kesintisiz ilerleme şartı taşımaz.","gloss":"gece yolculuğu ile zorlu gece yürüyüşü","neighbor_only":"Gece boyunca yorucu ve ısrarlı biçimde ilerlemeyi özellikle öne çıkarır.","neighbor_ref":"root_001422/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da gece vaktinde yol alma eylemini anlatır."},{"boundary_match":"partial","distinction":"Bu dal genel yolculuğun yalnızca gece gerçekleşen türünü anlatır; komşu dalın sınırında gece koşulu bulunmaz.","focus_only":"Yolculuğun gece yapılmasını kurucu koşul sayar ve geceye bağlı adlandırmalar üretir.","gloss":"gece yolculuğu ile genel yolculuk","neighbor_only":"Belirli bir yöne yapılan yolculuğu günün herhangi bir vaktinde kapsar.","neighbor_ref":"root_000551/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir yere doğru yol alma ve seyahat etme vardır."}],"source_phrase_ar":"السرى سير الليل (maqayis;ayn;sihah;mufradat)؛ سرى وأسرى لغتان (ayn;mufradat)؛ سريت سرى ومسرى وأسريت بمعنى (sihah)؛ السارية للقوم الذين يسرون بالليل وللسحابة التي تسري (mufradat)؛ السارية من السحاب التي تجيء ليلا (ayn;sihah)؛ السرية قطعة من الجيش (sihah)","source_summary":"Kaynaklar gece yolculuğunu ortak çekirdek olarak verir ve kişinin kendisinin gece ilerlemesiyle bir başkasını gece götürmesini aynı anlam alanında toplar. Gece ilerleyen topluluk ve bulut bu çekirdeğe bağlı adlardır; asker birliği anlamı ayrıca kaydedilir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"سير الليل بالفعل سرى وأسرى، والسارية أو السرية للقوم أو السحاب الذي يسري ليلا","what_is_not_ar":"لا يدخل فيه السري للنهر ولا السارية للأسطوانة ولا سراة الشيء ولا الكشف"},"support_links":["sup_be8d43e7d63f3850dd0c"]},{"boundary":"Küçük akarsu adı bağımsız bir addır; kökün toprakta ilerlemesi ise yalnızca belirtilen yapıya bağlı kullanımdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000702/B002","candidate_links":[{"candidate_id":"cand_3a88fc0bc6be8a8aada7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"küçük akarsu ve toprağa yayılan kök","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dereyi andıran küçük ve akan bir su yolu."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ağaç kökünün toprağın içinde sürünür gibi yayılıp ilerlemesi."}}],"root_ar":"س ر ي","root_id":"root_000702","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın su yolu adını ve yalnızca ağaç kökü yapısında görülen toprak içi ilerleme uzantısını birlikte özetler.","boundary_detail":"Küçük akarsu adı bağımsız bir addır; kökün toprakta ilerlemesi ise yalnızca belirtilen yapıya bağlı kullanımdır.","branch_image_ar":"السَّرِي والسريان الجاري","concept_gloss":"küçük akarsu ve toprağa yayılan kök","contextual_glosses":[{"applicability":"Dere veya küçük akarsu adı olarak kullanıldığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Akarsu oluşunu ve küçük ölçek sınırını korur."},"facet_ids":["F001"],"text":"küçük dere","usage_role":"general"},{"applicability":"Ağaç kökünün yer altında sürünür gibi yayılmasını anlatan yapıyla sınırlıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ağaç kökünü, toprak içindeki yönelimi ve yavaş ilerleme biçimini korur."},"facet_ids":["F002"],"text":"kökün toprak içinde ilerlemesi","usage_role":"explanatory"}],"definition":"Dal, küçük ve akan bir su yolunu adlandırır. Ayrıca ağaç kökünün toprak içinde sürünür gibi yayılıp ilerlemesini anlatan yapıyı kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dereyi andıran küçük ve akan bir su yolu."},{"facet_id":"F002","role":"extension","statement":"Ağaç kökünün toprağın içinde sürünür gibi yayılıp ilerlemesi."}],"identity_rationale":"Kaynak ifadesi küçük, akan bir su yolunu ve ağaç kökünün toprak içinde sürünür gibi ilerlemesini birlikte verir. Dal çerçevesi bu iki gerçekleşmeyi doğru biçimde ayırır ve gece yolculuğu ya da yükseklik anlamlarını buraya taşımaz.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"küçük dere"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"akan küçük dere"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ağacın kökü toprağın içinde ilerledi"}],"lexicalization_note":"Tanım, küçük akarsuya verilen bağımsız adı, akan akarsu kullanımını ve ağaç köküyle kurulan ilerleme kalıbını birbirine karıştırmadan kapsar.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; küçük su yolu sınırını kanal anlamından ve genel akış alanından ayıran iki komşu yeterli bulundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal doğal küçük akarsu adıyla kökün ilerlemesini bir arada taşır; komşu dalın odağı suyu ileten küçük kanal veya su koludur.","focus_only":"Küçük akarsu adının yanında ağaç kökünün toprak içindeki ilerleyişini de kapsar.","gloss":"küçük dere ile küçük su kanalı","neighbor_only":"Havuzdan su alan veya suyu taşıyan küçük kanal ve uzanan su kolu ayrıntılarını kapsar.","neighbor_ref":"root_000229/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal küçük ve uzanan bir su yolunu adlandırabilir."},{"boundary_match":"partial","distinction":"Bu dal belirli bir küçük su yolu ve kök yapısıyla sınırlıdır; komşu dal ise çok farklı varlıkların genel akış hareketini anlatır.","focus_only":"Küçük bir akarsu adını ve ağaç kökünün toprak içindeki ilerlemesini özelleştirir.","gloss":"küçük akarsu ile genel akış","neighbor_only":"Su dışındaki rüzgar, güneş, gemi ve hayvan gibi çok sayıda hareketli varlığın akışını da kapsar.","neighbor_ref":"root_000240/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da kesintisiz ilerleme veya akma görüntüsü bulunur."}],"source_phrase_ar":"السرى أيضا نهر صغير كالجدول (sihah)؛ سريا أي نهرا يسري (mufradat)؛ سرى عرق الشجرة يسري في الأرض سريا دب دبيبا فيها (ayn)","source_summary":"Kaynak ifadesi küçük akarsu adını, akan su niteliğiyle birlikte verir. Aynı dalda ağaç kökünün toprağın içinde yavaşça ilerlemesi de ayrı bir yapı olarak yer alır.","sources":["AY","SI","MU"],"what_is_ar":"النهر الصغير الجاري المسمى سريا أو السرى، وامتداد عرق الشجرة في الأرض دبيبا","what_is_not_ar":"لا يدخل فيه سير الليل ولا سراة العلو ولا السارية للأسطوانة"},"support_links":["sup_dcd36bde82b0c8b5539d"]},{"boundary":"Fiziksel üstlük, toplumsal seçkinlik ve en iyiyi seçme bağlantılıdır; günün vakti için yükselmiş ve orta vakit açıklamaları birlikte korunur.","branch_kind":"mixed_non_bare","branch_ref":"root_000702/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"üstlük, seçkinlik ve en iyiyi seçme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin üstü veya arkası ve günün yükselmiş ya da orta vakti."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişide seçkinlik, yücelik, saygınlık ve erdemli cömertlik."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Seçkin duruma gelmek veya seçkin görünmek için çaba göstermek."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İnsanlar, hayvanlar veya mallar arasından önde gelenleri ve en iyileri seçmek."}}],"root_ar":"س ر ي","root_id":"root_000702","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel üstlükten kişi veya maldaki üstün niteliğe ve bu niteliğe göre seçime uzanan dalın tamamını kapsar.","boundary_detail":"Fiziksel üstlük, toplumsal seçkinlik ve en iyiyi seçme bağlantılıdır; günün vakti için yükselmiş ve orta vakit açıklamaları birlikte korunur.","branch_image_ar":"السراة والرفعة","concept_gloss":"üstlük, seçkinlik ve en iyiyi seçme","contextual_glosses":[{"applicability":"Bir nesnenin üst bölümünü veya arka yüzünü gösteren yapılarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesne üzerindeki üst ya da arka bölüm ilişkisini korur."},"facet_ids":["F001"],"text":"bir şeyin üstü veya arkası","usage_role":"contextual"},{"applicability":"Günün ilerleyip yükseldiği bölüm için kullanılır ve aktarımlar arasındaki orta vakit sınırını da korur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Günün yükselmiş bölümü ile orta vakit açıklaması arasındaki kaynak farkını görünür tutar."},"facet_ids":["F001"],"text":"günün yükselmiş veya orta vakti","usage_role":"explanatory"},{"applicability":"Kişinin yüce konumunu, saygınlığını ve seçkin niteliğini anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiye yüklenen seçkinlik, yücelik ve saygınlık niteliklerini korur."},"facet_ids":["F002"],"text":"seçkin ve saygın kişi","usage_role":"general"},{"applicability":"Bir insan, hayvan veya mal topluluğundan önde gelenleri ayırma eyleminde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir kümeden üstün ve seçkin üyeleri ayırma işlemini korur."},"facet_ids":["F004"],"text":"en iyilerini seçmek","usage_role":"contextual"}],"definition":"Bir şeyin üstü veya arkası ile günün yükselmiş ya da orta vakti fiziksel üstlük yüzünü oluşturur. Buradan seçkinlik, onurlu cömertlik, seçkin duruma gelme ve bir topluluğun ya da malın en iyilerini ayırıp seçme anlamları doğar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin üstü veya arkası ve günün yükselmiş ya da orta vakti."},{"facet_id":"F002","role":"extension","statement":"Kişide seçkinlik, yücelik, saygınlık ve erdemli cömertlik."},{"facet_id":"F003","role":"extension","statement":"Seçkin duruma gelmek veya seçkin görünmek için çaba göstermek."},{"facet_id":"F004","role":"specialization","statement":"İnsanlar, hayvanlar veya mallar arasından önde gelenleri ve en iyileri seçmek."}],"identity_rationale":"Kaynak ifadesi fiziksel üstlükten toplumsal seçkinliğe uzanan bir alanı destekler; üst yüz, günün yükselmiş ya da orta vakti, onurlu cömertlik, seçkin kişi ve en iyileri seçme bu alanda yer alır. Ancak günle ilgili kullanım bir aktarımda yükselme, diğerinde orta vakit olarak sınırlandığından tanım bu farkı açıkça korumalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bir şeyin üstü veya arkası"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"günün yükselmiş veya orta vakti"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"seçkin ve saygın kişi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yüce nitelikli adam"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"erdemli cömertlik ve yücelik"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"seçkin duruma geldi"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"seçkin duruma gelme"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"seçkin görünmeye çalıştı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"en seçkinlerini seçti"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"ölüm o topluluğun önde gelenlerini aldı"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"sürüsünün ve malının en iyi bölümü"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yücelik veya seçkinliğe işaret eden kullanım"}],"lexicalization_note":"Tanım, bağımsız seçkinlik biçimlerini; nesnenin üstü, günün vakti, kişi ve sürüyle kurulan yapılardan ayrı ama bağlantılı yüzler olarak sunar.","neighbor_coverage_note":"Tüm adaylar incelendi; fiziksel ve toplumsal yüksekliğin en yakın iki komşusu ile açık değer karşıtı, dalın sınırını yeterince gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal seçkinlik ve seçme ölçütünü anlamın merkezine alır; komşu dalda temel yön yukarı doğru yükselme ve yüksek konumdur.","focus_only":"Üst yüzün yanında erdemli cömertliği, seçkin kişiyi ve en iyileri seçme işlemini kapsar.","gloss":"seçkinlik ile yükselme","neighbor_only":"Bir yerde yükselme ile yüksek konumu adlandırır ve belirli bir türemiş unvan kullanımını da içerir.","neighbor_ref":"root_001470/B001","relation_type":"near_synonym","shared_zone":"Her iki dal fiziksel yükseklikten değer ve makam yüksekliğine uzanır."},{"boundary_match":"opposed","distinction":"Bu dal eksenin yüksek ve seçkin ucunu, komşu dal ise düşük ve değersiz ucunu anlatır.","focus_only":"Üstün konumu, seçkin niteliği ve önde gelenlerin ayrılmasını bildirir.","gloss":"yücelik ile düşüklük","neighbor_only":"Aşağı konumu, değersizliği, eksikliği ve zayıf düzeyi bildirir.","neighbor_ref":"root_000493/B003","relation_type":"polarity_pair","shared_zone":"İki dal kişi veya şeylerin değer ve konum bakımından derecelendirildiği ortak eksende yer alır."},{"boundary_match":"partial","distinction":"Bu dal üstün niteliğe göre seçkinleşmeye uzanır; komşu dal somut tepe ve çıkıntıları da merkezî biçimde kapsar.","focus_only":"Erdemli cömertlik, seçkinleşme ve bir kümenin en iyilerini seçme işlemlerini içerir.","gloss":"üstlük ile doruk ve önderlik","neighbor_only":"Dağ tepesi, hörgüç ve burun gibi somut çıkıntıları geniş biçimde adlandırır.","neighbor_ref":"root_000999/B006","relation_type":"near_synonym","shared_zone":"Her iki dal üst bölüm, yücelik ve toplumsal önderlik alanlarında buluşur."}],"source_phrase_ar":"سراة الشيء ظهره وسراة النهار ارتفاعه (maqayis;mufradat)؛ سراة كل شيء أعلاه وسراة النهار وسطه (sihah)؛ السرو سخاء في مروءة (maqayis;sihah)؛ رجل سرو (mufradat)؛ استريت الإبل والغنم والناس أي اخترتهم (sihah)","source_summary":"Kaynak ifadesi üst ve arka yüzü, günün yükselmiş bölümünü, seçkinlik ile erdemli cömertliği ve en iyileri seçmeyi ortak bir üstlük alanında toplar. Günün ilgili bölümü yükselmiş vakit veya orta vakit olarak iki farklı sınırla açıklanır.","sources":["MQ","SI","MU"],"what_is_ar":"أعلى الشيء وظهره وارتفاع النهار، والرجل السري والسرو بمعنى الرفعة والمروءة، واختيار السراة","what_is_not_ar":"لا يدخل فيه سير الليل ولا النهر الجاري ولا كشف الثوب أو الهم"},"support_links":[]},{"boundary":"Somut kaldırma ile ruhsal veya bedensel durumun dağılması ayrılır; gece yolculuğu, akarsu ve yükseklik anlamları dışarıda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000702/B004","candidate_links":[{"candidate_id":"cand_3a88fc0bc6be8a8aada7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"üzerindekini kaldırma ve sıkıntının dağılması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi başka bir şeyin üzerinden kaldırarak alttakini açığa çıkarmak."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Giysiyi veya zırhı kişinin üzerinden çıkarmak ya da atmak."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Öfke veya baygınlığın bir kişiden kalkıp geçmesi."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kaygı ve sıkıntının kişinin üzerinden kalkıp dağılması."}}],"root_ar":"س ر ي","root_id":"root_000702","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Somut bir örtü veya giysinin kaldırılmasını ve kişiyi kaplayan olumsuz durumun geçmesini birlikte temsil eder.","boundary_detail":"Somut kaldırma ile ruhsal veya bedensel durumun dağılması ayrılır; gece yolculuğu, akarsu ve yükseklik anlamları dışarıda kalır.","branch_image_ar":"الكشف والانسراء","concept_gloss":"üzerindekini kaldırma ve sıkıntının dağılması","contextual_glosses":[{"applicability":"Bir nesnenin üzerindeki başka bir şeyin kaldırıldığı temel somut işlemde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Örten şeyin kaldırılması ile alttaki şeyin açığa çıkması aşamalarını korur."},"facet_ids":["F001"],"text":"üstündekini kaldırıp açığa çıkarmak","usage_role":"general"},{"applicability":"Giysi veya zırhın kişinin üzerinden çıkarıldığı somut bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Giysi veya zırhı kişinin üzerinden ayırma işlemini korur."},"facet_ids":["F002"],"text":"giysisini üzerinden çıkarmak","usage_role":"contextual"},{"applicability":"Kişinin kaygı veya sıkıntıdan kurtulduğu durumlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kaygının kişiden kalkıp etkisini yitirmesi sonucunu korur."},"facet_ids":["F004"],"text":"kaygısı dağıldı","usage_role":"contextual"},{"applicability":"Öfkenin yatışması veya baygınlık durumunun sona ermesi bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öfke veya baygınlığın kişiden kalkarak sona ermesini korur."},"facet_ids":["F003"],"text":"öfkesi veya baygınlığı geçti","usage_role":"contextual"}],"definition":"Temel anlam, bir şeyin üzerindeki başka bir şeyi kaldırıp alttakini açığa çıkarmaktır; giysi veya zırhı üzerinden çıkarmak bunun somut türüdür. Kaygı, öfke ya da baygınlığın kişiden kalkıp dağılması aynı görüntünün durumlara uzanmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi başka bir şeyin üzerinden kaldırarak alttakini açığa çıkarmak."},{"facet_id":"F002","role":"specialization","statement":"Giysiyi veya zırhı kişinin üzerinden çıkarmak ya da atmak."},{"facet_id":"F003","role":"extension","statement":"Öfke veya baygınlığın bir kişiden kalkıp geçmesi."},{"facet_id":"F004","role":"extension","statement":"Kaygı ve sıkıntının kişinin üzerinden kalkıp dağılması."}],"identity_rationale":"Kaynak ifadesi bir şeyi örten veya üzerinde bulunan başka bir şeyi kaldırarak açığa çıkarmayı çekirdek anlam olarak verir. Giysi ile zırhın çıkarılması bu işlemin somut gerçekleşmeleri, kaygı, öfke veya baygınlığın geçmesi ise durumun ortadan kalkmasına dayanan uzantılardır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bir şeyi üzerindekini kaldırarak açığa çıkarma"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"giysiyi üzerinden çıkarma"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"zırhını üzerinden atma"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"öfkesi veya baygınlığı geçti"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"kaygım dağıldı"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"kaygım dağıldı"}],"lexicalization_note":"Tanım, bağımsız açığa çıkarma anlamını giysi, zırh, kaygı, öfke ve baygınlıkla kurulan yapılardan ayrı yüzler halinde korur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; somut örtü kaldırma, giysi çıkarma ve ruhsal rahatlama sınırlarını gösteren üç komşu yayımlanmaya değer bulundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kişinin üzerinden giysi, zırh veya belirli bir durumun kalkmasına odaklanır; komşu dal örtü ve kötülük alanında daha genel bir açılma taşır.","focus_only":"Giysi ve zırhı kişinin üzerinden çıkarma ile öfke veya baygınlığın geçmesini ayrıca kapsar.","gloss":"örtüyü kaldırma ve sıkıntıyı açma","neighbor_only":"Örtünün açılmasının yanında genel kötülüğün veya zararın açığa çıkıp giderilmesini kapsar.","neighbor_ref":"root_001302/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bir örtünün kaldırılmasını ve kişiyi kaplayan sıkıntının geçmesini anlatabilir."},{"boundary_match":"partial","distinction":"Bu dal somut çıkarma görüntüsünü ruhsal ve bedensel durumlara taşır; komşu dalın ağırlığı farklı örtülerin sökülmesindedir.","focus_only":"Kaygı, öfke ve baygınlığın geçmesine uzanır ve giysiyle zırhın kişinin üzerinden çıkarılmasını belirtir.","gloss":"üzerindekini kaldırma ile örtüyü sökme","neighbor_only":"Çatı, gök örtüsü ve hayvanın sırtındaki örtü gibi çok çeşitli kapatıcıların sökülmesini kapsar.","neighbor_ref":"root_001301/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bir şeyi örten katmanı kaldırıp alttakini görünür kılma işleminde buluşur."},{"boundary_match":"partial","distinction":"Bu dal duygusal rahatlamayı somut bir şeyin üzerinden kaldırılması görüntüsüne bağlar; komşu dal genel kurtulma ve ferahlama sonucuna odaklanır.","focus_only":"Somut örtü, giysi ve zırh kaldırmayı; ayrıca öfke ile baygınlığın geçmesini kapsar.","gloss":"sıkıntının dağılması ile ferahlama","neighbor_only":"Keder, hastalık ve sıkıntıdan kurtulmayı daha geniş bir rahatlama alanında toplar.","neighbor_ref":"root_001139/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal kaygı veya sıkıntının kişiden uzaklaşıp sona ermesini anlatır."}],"source_phrase_ar":"السرو كشف الشيء عن الشيء (maqayis)؛ سروت عني الثوب أي كشفته (maqayis)؛ سرى عن فلان أي تجلى عنه الغضب أو غشية (ayn)؛ انسرى عني الهم انكشف وسري عني الهم مثله (sihah)؛ سروت الثوب عني أي نزعته (mufradat)","source_summary":"Kaynaklar örtücü bir şeyi kaldırıp alttakini açığa çıkarma çekirdeğini; giysi veya zırhı üzerinden çıkarma örnekleriyle somutlaştırır. Aynı yapı kaygının, öfkenin veya baygınlığın kişiden kalkmasına genişler.","sources":["MQ","AY","SI","MU"],"what_is_ar":"كشف الشيء عن الشيء، ونزع الثوب أو الدرع، وانكشاف الهم أو الغضب أو الغشية","what_is_not_ar":"لا يدخل فيه سير الليل ولا السري للنهر ولا السراة للعلو"},"support_links":["sup_dcd36bde82b0c8b5539d"]},{"boundary":"Anlam taş ya da tuğladan yapılmış dikmeyle sınırlıdır; aynı biçimdeki bulut ve topluluk adları bu dala girmez.","branch_kind":"bare","branch_ref":"root_000702/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"taş veya tuğla dikme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Taş veya tuğladan yapılan dikey yapı öğesi."}}],"root_ar":"س ر ي","root_id":"root_000702","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Taş ya da tuğladan yapılmış dikey yapı öğesinin bağımsız adı olarak tam karşılık verir.","boundary_detail":"Anlam taş ya da tuğladan yapılmış dikmeyle sınırlıdır; aynı biçimdeki bulut ve topluluk adları bu dala girmez.","branch_image_ar":"السارية الأسطوانة","concept_gloss":"taş veya tuğla dikme","contextual_glosses":[{"applicability":"Yapı öğesinin özellikle taştan yapıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taştan yapılmış dikey yapı öğesi sınırını korur."},"facet_ids":["F001"],"text":"taş dikme","usage_role":"contextual"}],"definition":"Taş ya da tuğladan yapılmış dikey bir yapı öğesi, yani bir dikmedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Taş veya tuğladan yapılan dikey yapı öğesi."}],"identity_rationale":"Kaynak ifadesi taş veya tuğladan yapılmış dikey yapı öğesini doğrudan tanımlar. Dal çerçevesi bu nesneyi gece gelen bulut veya gece yürüyen toplulukla aynı biçimi taşıyan kullanımlardan doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"taş veya tuğla dikme"}],"lexicalization_note":"Tanım yalnızca bağımsız nesne adını verir ve başka dallardaki aynı biçimli kullanımları ya da yapıya bağlı anlamları buraya taşımaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; tam eşdeğer ad ile malzeme ve benzetme bakımından daha geniş iki direk dalı en yararlı karşılaştırmaları sağlar.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kaynakta komşu dalın adı doğrudan bu daldaki nesneye eşitlenir; anlam sınırları arasında gösterilebilir bir fark yoktur.","focus_only":null,"gloss":"taş veya tuğla dikme","neighbor_only":null,"neighbor_ref":"root_000034/B005","relation_type":"synonym","shared_zone":"Her iki dal aynı dikey yapı öğesini adlandırır."},{"boundary_match":"partial","distinction":"Bu dal taş veya tuğla malzemeli belirli dikmeye odaklanır; komşu dal farklı malzemelerden taşıyıcı direklerin genel alanıdır.","focus_only":"Malzemeyi taş veya tuğlayla sınırlar ve nesneyi bu belirli adıyla verir.","gloss":"taş dikme ile genel yapı direği","neighbor_only":"Ahşap, demir ve mermer gibi başka malzemeleri ve evi ya da çadırı taşıma işlevini de kapsar.","neighbor_ref":"root_001043/B003","relation_type":"near_synonym","shared_zone":"İki dal da dikey duran ve yapının parçası olan bir öğeyi adlandırır."},{"boundary_match":"partial","distinction":"Bu dal malzemesi belirtilen yapı öğesidir; komşu dal dikili direği ve ona dayanan benzetmeli kullanımı daha geniş biçimde kapsar.","focus_only":"Taş veya tuğladan yapılan yapı öğesiyle sınırlıdır.","gloss":"yapı dikmesi ile dikili direk","neighbor_only":"Ev ya da çadır direğinin yanında uzun hayvan için benzetmeli kullanımı da kapsar.","neighbor_ref":"root_000706/B003","relation_type":"near_synonym","shared_zone":"Her iki dal yapı içinde dikey olarak yerleştirilen bir öğeyi anlatır."}],"source_phrase_ar":"السارية الأسطوانة (maqayis;sihah)؛ السارية أسطوانة من حجارة أو آجر (ayn)؛ السارية يقال للأسطوانة (mufradat)","source_summary":"Kaynaklar bu sözcüğü taş veya tuğladan yapılmış dikey bir yapı öğesi olarak ortak biçimde tanımlar.","sources":["MQ","AY","SI","MU"],"what_is_ar":"الأسطوانة من حجارة أو آجر وما يسمى السارية","what_is_not_ar":"لا يدخل فيه السارية من السحاب ولا السارية للقوم السائرين ليلا"},"support_links":[]},{"boundary":"Bu dalın öğeleri genel kök anlamı gibi genişletilmemeli, birbirinin yerine geçebilen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtta verilen biçim veya bağlam sınırı içinde tutulmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000702/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","surface_ar":"يَسْرِ"}],"gloss":"özel adlandırma kümesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birbirinden farklı iki biçimle verilen ağaç adları."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir yer adı ve açıklanmayan başka bir yer türüne benzetilen kullanım."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Küçük bir hayvana verilen ad."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Küçük bir oka verilen ad."}}],"root_ar":"س ر ي","root_id":"root_000702","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki dağınık veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu dalın öğeleri genel kök anlamı gibi genişletilmemeli, birbirinin yerine geçebilen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtta verilen biçim veya bağlam sınırı içinde tutulmalıdır.","branch_image_ar":"أسماء متفرقة","concept_gloss":"özel adlandırma kümesi","definition":"Bu dal tek bir kavram tanımlamaz; ağaç, yer, küçük hayvan ve küçük ok için birbirinden bağımsız adlandırmaları geçici olarak bir arada tutar. Anlamlar ayrı dallara bölünmelidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birbirinden farklı iki biçimle verilen ağaç adları."},{"facet_id":"F002","role":"source_variant","statement":"Bir yer adı ve açıklanmayan başka bir yer türüne benzetilen kullanım."},{"facet_id":"F003","role":"source_variant","statement":"Küçük bir hayvana verilen ad."},{"facet_id":"F004","role":"source_variant","statement":"Küçük bir oka verilen ad."}],"identity_rationale":"Bu dal packet düzeyinde inceleme statüsünde tutulmuş sınır-riskli malzemeyi taşır. Kanıt, tek bir yalın kök imgesinden çok biçime veya özel kullanıma bağlı dağınık adlandırmaları gösterdiği için dal yapısal bölme şartı koşmadan sınırlı bir adlandırma kümesi olarak okunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"bir ağaç türü"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"belirli bir topluluğa ait yerleşim"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"başka bir yer türüne benzer yer"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"yay yapılan bir ağaç"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"küçük bir hayvan veya çekirgenin kurtçuk evresi"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"bu küçük hayvanın çok bulunduğu arazi"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"küçük ok"}],"lexicalization_note":"Kapsam verilen biçim veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"السرو شجر (sihah)؛ السرو محلة حمير (maqayis;sihah)؛ السرو مثل الخيف (sihah)؛ السراء شجر (maqayis;sihah)؛ السروة دويبة (maqayis)؛ السروة سهم صغير (sihah)","source_summary":"İnceleme statüsündeki kanıt, tek bir birleşik anlamdan çok biçime veya özel bağlama bağlı sınırlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["MQ","SI"],"what_is_ar":"ألفاظ مفردة متفرقة مثل السرو للشجر أو الموضع، والسراء للشجر، والسروة للدويبة أو السهم","what_is_not_ar":"لا يدخل فيه سير الليل ولا النهر ولا الرفعة ولا الكشف ولا الأسطوانة"},"support_links":[]},{"boundary":"Dal genel gece zamanını ve karanlığını kapsar; şiddet, uzunluk ve ayın son gecesi anlamları yalnız ilgili söz öbeklerine bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001392/B001","candidate_links":[{"candidate_id":"cand_b288aa75c0cb6835b3d9","lane":"micro"},{"candidate_id":"cand_eef72432a253294c4c15","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:4:1:3","qac_word_ref":"89:4:1","surface_ar":"يْلِ"}],"gloss":"gündüzün karşıtı olan gece ve onun karanlığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gündüzün karşıtı olan zaman bölümü gecedir; tek bir gece veya birden çok gece olarak sayılabilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gece adı, bu zaman bölümüne özgü karanlığı da anlatabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli niteleme kalıpları çok karanlık veya çetin bir geceyi anlatır."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir başka pekiştirme kalıbı gecenin uzunluğunu veya şiddetini özellikle öne çıkarır."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Özel bir söz öbeği, ayın hem en karanlık hem de son gecesini belirtir."}}],"root_ar":"ل ي ل","root_id":"root_001392","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel gece zamanını ve bu zamana bağlı karanlık anlamını birlikte temsil eder; özel nitelemeler ayrıca bağlama göre çevrilir.","boundary_detail":"Dal genel gece zamanını ve karanlığını kapsar; şiddet, uzunluk ve ayın son gecesi anlamları yalnız ilgili söz öbeklerine bağlıdır.","branch_image_ar":"الليل خلاف النهار وظلمته","concept_gloss":"gündüzün karşıtı olan gece ve onun karanlığı","contextual_glosses":[{"applicability":"Zaman bölümünden çok o zamandaki karanlığın anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geceye özgü karanlık görünümünü doğrudan korur."},"facet_ids":["F002"],"text":"gece karanlığı","usage_role":"contextual"},{"applicability":"Yalnız karanlığın şiddetini veya gecenin çetinliğini pekiştiren söz öbeklerinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gecenin yoğun karanlığını ve çetinlik vurgusunu korur."},"facet_ids":["F003"],"text":"çok karanlık ve çetin gece","usage_role":"contextual"},{"applicability":"Uzunluk ile genel şiddet arasında değişebilen özel pekiştirme kalıbını açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kalıbın uzunluk ve pekiştirilmiş şiddet seçeneklerini birlikte korur."},"facet_ids":["F004"],"text":"uzun ya da şiddeti pekiştirilmiş gece","usage_role":"explanatory"},{"applicability":"Yalnız ay içindeki özel konumu ve olağanüstü karanlığı birlikte belirten söz öbeğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ayın son gecesi olma koşulunu ve en yoğun karanlığı korur."},"facet_ids":["F005"],"text":"ayın en karanlık ve son gecesi","usage_role":"contextual"}],"definition":"Gündüzün karşıtı olan gece zamanı ve bu zamana özgü karanlıktır. Belirli söz öbekleri, temel anlamı değiştirmeden gecenin çok karanlık, çetin ya da uzun oluşunu veya ayın en karanlık son gecesini belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gündüzün karşıtı olan zaman bölümü gecedir; tek bir gece veya birden çok gece olarak sayılabilir."},{"facet_id":"F002","role":"extension","statement":"Gece adı, bu zaman bölümüne özgü karanlığı da anlatabilir."},{"facet_id":"F003","role":"specialization","statement":"Belirli niteleme kalıpları çok karanlık veya çetin bir geceyi anlatır."},{"facet_id":"F004","role":"specialization","statement":"Bir başka pekiştirme kalıbı gecenin uzunluğunu veya şiddetini özellikle öne çıkarır."},{"facet_id":"F005","role":"source_variant","statement":"Özel bir söz öbeği, ayın hem en karanlık hem de son gecesini belirtir."}],"identity_rationale":"Kaynak ifadesi, gündüzün karşıtı olan gece zamanını ve gece karanlığını açıkça temel anlam olarak verir; tekil ve çoğul biçimlerin yanında karanlığın şiddetini, gecenin uzunluğunu veya belirli bir ay gecesini anlatan kalıpları da ayrıca tanıklar. Bu nedenle dal kimliği korunabilir, ancak kalıba bağlı nitelemeler temel gece anlamıyla bir tutulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"gündüzün karşıtı olan gece"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"gece karanlığı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"tek bir gece"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"geceler"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"geceler"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"geceler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"çok karanlık ve çetin gece"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"çok karanlık gece"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"uzun ya da şiddeti pekiştirilmiş gece"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ayın en karanlık ve son gecesi"}],"lexicalization_note":"Dal hem genel gece adını hem de yalnız belirli söz öbeklerinde ortaya çıkan karanlık, zorluk, uzunluk ve ay sonu nitelemelerini içerir; tanım bu iki düzeyi ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gece, geceleyin eylem, bugüne bağlı gece, yoğunlaşan karanlık ve adlandırma arasındaki sınırı en açık gösteren dört komşu seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal gecenin kendisini ve karanlığını gösterir; komşu dal ise geceyi bir eylemin gerçekleşme zamanı veya yönü olarak kodlar.","focus_only":"Geceyi bir zaman bölümü ve karanlık olarak adlandırır.","gloss":"gece ile geceleyin yapılan iş arasındaki ayrım","neighbor_only":"Geceye girme, geceleyin işlem yapma veya gece yol alma eylemlerini anlatır.","neighbor_ref":"root_001392/B002","relation_type":"same_field","shared_zone":"Her iki dal da geceyi zaman bakımından ortak eksen olarak kullanır."},{"boundary_match":"partial","distinction":"Bu dalda bugüne göre yakınlık zorunlu değildir; komşu dalın anlamı konuşma gününe ve gün içindeki söyleme anına bağlı bir gece seçimi gerektirir.","focus_only":"Herhangi bir geceyi genel zaman türü olarak kapsar.","gloss":"genel gece ile bugüne bağlı gece arasındaki ayrım","neighbor_only":"Konuşma gününe göre en yakın, geçen veya girilecek geceyi seçer.","neighbor_ref":"root_001392/B003","relation_type":"near_neighbor","shared_zone":"İki dal da gece zamanını gösterir ve belirli bağlamlarda aynı zaman dilimine işaret edebilir."},{"boundary_match":"partial","distinction":"Bu dal geceyi veya mevcut karanlığını adlandırabilir; komşu dal ise karanlığın şiddetlenmesi durumunu öne çıkarır ve genel gece adı yerine geçmez.","focus_only":"Gece zamanını, karanlığını ve bazı kalıplarda yoğun karanlık niteliğini kapsar.","gloss":"gece karanlığı ile karanlığın şiddetlenmesi arasındaki ayrım","neighbor_only":"Gecenin giderek koyulaşmasını veya karanlığının şiddetlenmesini merkez alır.","neighbor_ref":"root_001015/B004","relation_type":"near_neighbor","shared_zone":"Her ikisi de gecenin yoğun karanlığını anlatan bağlamlarda buluşur."},{"boundary_match":"thematic_only","distinction":"Bu dalın çekirdeği bir zaman bölümü ve karanlıktır; komşu dalda biçim bir kişiyi adlandırır veya daha geniş bir söz öbeği içinde şarabı örtülü biçimde anar.","focus_only":"Gece zamanını ve onun karanlığını anlatır.","gloss":"gece anlamı ile adlandırma kullanımı arasındaki ayrım","neighbor_only":"Bir kadın adını ve ayrı bir söz öbeğinde şarabın örtülü adını anlatır.","neighbor_ref":"root_001392/B004","relation_type":"thematic","shared_zone":"Dallar aynı biçim ailesiyle bağlantılıdır, fakat kavramsal alanları örtüşmez."}],"source_phrase_ar":"الليل خلاف النهار (maqayis)؛ الليل ضد النهار (jamhara;tahdhib)؛ ظلام الليل (tahdhib)؛ ليل وليلة وليلات وليال (maqayis;sihah;mufradat)؛ ليل أليل وليلة ليلاء وليل لائل (jamhara;sihah;tahdhib;mufradat)؛ ليلة ليلى أشد ليلة في الشهر ظلمة وآخر ليلة فيه (jamhara)","source_summary":"Kaynakların ortak çekirdeği geceyi gündüzün karşıtı bir zaman ve ona bağlı karanlık olarak tanımlar. Toplu kanıt ayrıca tek ve çok gece biçimlerini, karanlığı ya da uzunluğu pekiştiren kullanımları ve ayın en karanlık son gecesine özgü ifadeyi birlikte gösterir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الليل والليلة والليالي، وضده النهار، وظلام الليل وشدته وطوله في نحو ليلة ليلاء وليل أليل وليل لائل وليلة ليلى","what_is_not_ar":"لا يدخل فيه النهار ولا اليوم إلا من جهة المقابلة، ولا التسمية بليلى، ولا ولد الطائر المختلف فيه"},"support_links":["sup_35209214a5688a067e3f","sup_be8d43e7d63f3850dd0c"]},{"boundary":"Dal gecenin kendisini değil, geceye geçişi veya geceyi zaman ve yön olarak alan işlem ile yolculuk kullanımlarını kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001392/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:4:1:3","qac_word_ref":"89:4:1","surface_ar":"يْلِ"}],"gloss":"geceye girme ya da geceleyin iş görüp yol alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iş veya karşılıklı işlem, gündüz yerine geceye göre yürütülür."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Zaman akışı içinde geceye girme veya gece vaktine ulaşma anlatılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Geceleyin yol alan veya gece yolculuğuna dayanabilen kişi anlatılır."}}],"root_ar":"ل ي ل","root_id":"root_001392","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın geceye geçiş, geceye göre işlem ve gece yolculuğu alt görünümlerini birlikte açıklayan üst karşılıktır.","boundary_detail":"Dal gecenin kendisini değil, geceye geçişi veya geceyi zaman ve yön olarak alan işlem ile yolculuk kullanımlarını kapsar.","branch_image_ar":"مزاولة الأمر في الليل","concept_gloss":"geceye girme ya da geceleyin iş görüp yol alma","contextual_glosses":[{"applicability":"Bir işlemin gündüze göre yapılan benzeriyle karşılaştırılarak gece üzerinden yürütüldüğü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı işlemin özellikle geceye göre yürütülmesini korur."},"facet_ids":["F001"],"text":"geceye göre karşılıklı işlem yapmak","usage_role":"contextual"},{"applicability":"Bir kişinin veya durumun gece vaktine ulaştığını bildiren kullanımda geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gündüzden gece vaktine geçiş ilişkisini doğrudan korur."},"facet_ids":["F002"],"text":"geceye girmek","usage_role":"contextual"},{"applicability":"Gece yolculuğu yapan veya böyle bir yolculuğa dayanabilen kişinin anlatıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gece yolculuğu yapan kişiyi ve bu yolculuğa güç yetirme koşulunu korur."},"facet_ids":["F003"],"text":"gece yol alan kimse","usage_role":"contextual"}],"definition":"Geceye girmek ya da bir işi, karşılıklı işlemi veya yolculuğu geceyi zaman ve yön olarak alarak gerçekleştirmektir. Gece yolculuğuna dayanabilen kişi de bu eylem alanına bağlı olarak adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iş veya karşılıklı işlem, gündüz yerine geceye göre yürütülür."},{"facet_id":"F002","role":"core","statement":"Zaman akışı içinde geceye girme veya gece vaktine ulaşma anlatılır."},{"facet_id":"F003","role":"specialization","statement":"Geceleyin yol alan veya gece yolculuğuna dayanabilen kişi anlatılır."}],"identity_rationale":"Kaynak ifadesi geceyi yalın bir zaman adı olarak değil, karşılıklı bir işlemin geceye göre yapılması, geceye girilmesi ve gece yolculuğu yapılması ya da buna güç yetirilmesi üzerinden verir. Geçici dal çerçevesi bu ortak eylem yönelimini doğru yakalar.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"geceye göre karşılıklı işlem yapma"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"geceye girmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"gece yol alan veya gece yolculuğuna dayanabilen kimse"}],"lexicalization_note":"Anlam yalnız türemiş biçimlerde ve belirli kullanım kalıplarında tanıklanır; karşılıklı işlem, geceye giriş ve gece yolculuğu ayrı alt görünümler olarak tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gece anlamı ile gece yolculuğunun bağımsız, zorlu veya gündüzden geceye kesintisiz türleri en yararlı dört karşılaştırmayı verdi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dalda gece, girişin, işlemin veya yolculuğun yönünü belirler; komşu dalda ise eylem değil, doğrudan zaman bölümü ve karanlık adlandırılır.","focus_only":"Geceye girme veya geceyi bir eylemin zamanı olarak kullanma anlamlarını taşır.","gloss":"geceleyin eylem ile gece zamanının ayrımı","neighbor_only":"Gece zamanını ve ona bağlı karanlığı adlandırır.","neighbor_ref":"root_001392/B001","relation_type":"same_field","shared_zone":"Her iki dalın ortak zaman ekseni gecedir."},{"boundary_match":"partial","distinction":"Bu dalın yolculuk görünümü yanında geceye giriş ve işlem anlamları vardır; komşu dal ise gece yolculuğunu kendi başına merkezî bir hareket alanı olarak kurar.","focus_only":"Geceye giriş ve geceye göre karşılıklı işlem yapma anlamlarını da kapsar.","gloss":"geniş gece eylemi ile gece yolculuğu arasındaki ayrım","neighbor_only":"Gece yolculuğunu bağımsız bir hareket olarak ve yol alan topluluğu da kapsayacak biçimde merkezleştirir.","neighbor_ref":"root_000702/B001","relation_type":"near_neighbor","shared_zone":"İki dal geceleyin yol alma anlamında belirgin biçimde örtüşür."},{"boundary_match":"partial","distinction":"Bu dal için sürekli çaba ve güçlük kurucu değildir; komşu dal gece boyunca ısrarlı ilerlemeyi ve yolculuğun zahmetini anlamın merkezine alır.","focus_only":"Geceyle bağlantılı işlemi, geçişi ve olağan yolculuk yetisini kapsar.","gloss":"gece yol alma ile gece boyunca çabalayarak ilerleme ayrımı","neighbor_only":"Gece boyunca yolculuğu sürdürme ve bunun güçlüğüne katlanma yönünü özellikle öne çıkarır.","neighbor_ref":"root_001422/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal gece yolculuğu ve bu yolculuğa dayanma alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dalda gündüzden geceye kesintisiz devam şartı yoktur; komşu dalın ayırt edici sınırı, yolculuğun bir gündüz ile bir gece boyunca sürdürülmesidir.","focus_only":"Eylemin yalnız geceye göre yapılmasını veya geceye girilmesini anlatabilir.","gloss":"geceye bağlı eylem ile kesintisiz gündüz gece yolculuğu ayrımı","neighbor_only":"Yolculuğun gündüz ile gece arasında kesintisiz sürdürülmesini zorunlu kılar.","neighbor_ref":"root_001670/B006","relation_type":"near_neighbor","shared_zone":"İki dalın kesişiminde gece boyunca yol alma bulunur."}],"source_phrase_ar":"عاملته ملايلة كما تقول مياومة من اليوم (sihah)؛ أليلت صرت في الليل (tahdhib)؛ لست بليلي ولكني نهر أي أسير بالنهار ولا أطيق سرى الليل (tahdhib)","source_summary":"Toplu kanıt geceye göre yapılan karşılıklı işlemi, gece vaktine girmeyi ve gece yolculuğu yapabilen kişiyi aynı eylem alanında birleştirir. Bu kullanımların hiçbiri yalın gece zamanını tek başına adlandırmaz.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الفعل أو المعاملة على جهة الليل، مثل الملايلة، والدخول في الليل، والسير أو السرى في الليل","what_is_not_ar":"لا يدخل فيه اسم الليل نفسه ولا الليلة بوصفها زمنا مجردا"},"support_links":[]},{"boundary":"Dal yalnız konuşma gününe göre belirlenen en yakın geceyi kapsar; yönelim, cümlenin zamanı ve gün içindeki söyleme anına göre geçmişe veya geleceğe dönebilir.","branch_kind":"non_bare","branch_ref":"root_001392/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:4:1:3","qac_word_ref":"89:4:1","surface_ar":"يْلِ"}],"gloss":"bugüne göre belirlenen en yakın gece","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gece, konuşmacının içinde bulunduğu güne göre en yakın gece olarak belirlenir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gündüz söylenen ileri yönelimli kullanım, konuşmacının gireceği yaklaşan geceyi gösterir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tamamlanmış bir eylem günün ilk yarısında anlatılırken ifade önceki geceye dönebilir; gün ilerleyince geçmiş gece için başka bir zaman sözü seçilir."}}],"root_ar":"ل ي ل","root_id":"root_001392","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Geçmiş veya gelecek yönelimi cümle bağlamından anlaşılan, konuşma gününe en yakın geceyi üst düzeyde karşılar.","boundary_detail":"Dal yalnız konuşma gününe göre belirlenen en yakın geceyi kapsar; yönelim, cümlenin zamanı ve gün içindeki söyleme anına göre geçmişe veya geleceğe dönebilir.","branch_image_ar":"الليلة القريبة من اليوم","concept_gloss":"bugüne göre belirlenen en yakın gece","contextual_glosses":[{"applicability":"Gündüz söylenip konuşmacının gireceği yaklaşan geceye yönelen bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Konuşma gününe en yakın yaklaşan gece yönelimini korur."},"facet_ids":["F001","F002"],"text":"bu gece","usage_role":"contextual"},{"applicability":"Günün ilk yarısında tamamlanmış bir eylemi en yakın önceki geceye bağlayan Türkçe anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tamamlanmış eylemin konuşma gününden önceki en yakın geceye bağlanmasını korur."},"facet_ids":["F001","F003"],"text":"dün gece","usage_role":"contextual"}],"definition":"Konuşma gününe en yakın olan ve bağlama göre bir önceki ya da girilecek olan gecedir. Geçmiş bir eylem anlatılırken günün ilk yarısında önceki geceyi gösterebilir; gündüzden yaklaşan gece anlatılırken sonraki geceyi seçer.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gece, konuşmacının içinde bulunduğu güne göre en yakın gece olarak belirlenir."},{"facet_id":"F002","role":"specialization","statement":"Gündüz söylenen ileri yönelimli kullanım, konuşmacının gireceği yaklaşan geceyi gösterir."},{"facet_id":"F003","role":"specialization","statement":"Tamamlanmış bir eylem günün ilk yarısında anlatılırken ifade önceki geceye dönebilir; gün ilerleyince geçmiş gece için başka bir zaman sözü seçilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Bugünle ilişkisi bulunmayan herhangi bir geceyi de kapsar.","collision":null,"fit":"broadening","loses":"Konuşma gününe göre yakınlık ve bağlama bağlı zaman yönelimini belirtmez.","preserves":"Gece zamanına yapılan temel gönderimi korur."},"text":"gece"}],"identity_rationale":"Kaynak ifadesi, genel gece türünü değil konuşma gününe en yakın geceyi seçen bağlamsal bir kullanımı açıkça tanımlar. Gündüz konuşulurken girilecek geceye yönelim ile günün ilk yarısında tamamlanmış bir eylemin önceki geceye bağlanması, geçici çerçevede belirtilen yakınlık ve söyleme zamanı sınırını doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bugüne en yakın gece; bağlama göre geçen ya da girilecek olan gece"}],"lexicalization_note":"Anlam belirli bir gece ifadesinin konuşma gününe göre yorumlanmasına bağlıdır; genel ve bağlamsız gece anlamına genişletilemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gece, geceleyin eylem, ertesi gün ve bitişik zaman sınırı karşılaştırmaları dalın bugüne bağlı gönderimini en açık biçimde ayırdı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın gönderimi konuşma gününe göre hesaplanır; komşu dal genel gece adıdır ve bugüne yakınlık, söyleme anı veya geçmiş gelecek yönelimi gerektirmez.","focus_only":"Konuşma gününe en yakın geceyi ve bağlama bağlı geçmiş ya da gelecek yönelimini zorunlu kılar.","gloss":"bugüne en yakın gece ile genel gece arasındaki ayrım","neighbor_only":"Herhangi bir geceyi, geceleri ve gece karanlığını bağlamsız olarak kapsayabilir.","neighbor_ref":"root_001392/B001","relation_type":"near_synonym","shared_zone":"İki dal da tek bir gece zamanını gösterebilir ve uygun bağlamda aynı zaman aralığına işaret edebilir."},{"boundary_match":"field_only","distinction":"Bu dalın çekirdeği bağlam içinde seçilen gecedir; komşu dalda gece bir geçişin, işlemin veya yolculuğun gerçekleşme zamanı ve yönüdür.","focus_only":"Bugüne göre seçilen belirli bir gece zamanını gösterir.","gloss":"yakın gece göndergesi ile geceleyin eylem arasındaki ayrım","neighbor_only":"Geceye girme, geceleyin işlem yapma veya gece yolculuğu gerçekleştirme eylemini gösterir.","neighbor_ref":"root_001392/B002","relation_type":"same_field","shared_zone":"Her iki dal da geceyi konuşma veya eylem için zaman çerçevesi yapar."},{"boundary_match":"field_only","distinction":"Bu dal geceyi seçer ve yönelimi bağlama göre değişebilir; komşu dal ise gün birimini seçer ve zorunlu olarak konuşma gününün sonrasına yönelir.","focus_only":"Bugüne komşu geceyi, cümle yönelimine göre geçmişte veya gelecekte seçebilir.","gloss":"en yakın gece ile ertesi gün arasındaki ayrım","neighbor_only":"Yalnız konuşma gününden sonraki günü, yani gelecek gündüzlü zaman birimini seçer.","neighbor_ref":"root_001076/B002","relation_type":"same_field","shared_zone":"İki dal da konuşma gününü merkez alan yakın zaman ifadeleridir."},{"boundary_match":"field_only","distinction":"Bu dal belirli bir gece göndergesini seçer; komşu dal ise geceyi seçmekten çok iki zaman bölümünün birbirine değen başlangıç veya bitiş sınırını adlandırır.","focus_only":"Konuşma gününe göre en yakın gecenin hangisi olduğunu belirler.","gloss":"yakın gece seçimi ile zaman sınırı arasındaki ayrım","neighbor_only":"Bir zaman parçasının başlangıç veya bitiş sınırında başka bir zamanla karşı karşıya gelmesini anlatır.","neighbor_ref":"root_001479/B006","relation_type":"same_field","shared_zone":"Her ikisi de komşu zaman parçaları arasındaki ilişkiyi konu eder."}],"source_phrase_ar":"إلى نصف النهار تقول فعلت الليلة فإذا زالت الشمس قلت فعلت البارحة (tahdhib)؛ هذه الليلة التي في السماء أقرب الليالي من يومك وهي الليلة التي تليه (tahdhib)؛ الهلال في هذه الليلة التي في السماء يعني الليلة التي تدخلها يتكلم بهذا في النهار (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, günün ilk yarısında tamamlanmış bir eylem için önceki gecenin bu ifadeyle anılabildiğini, gün ilerleyince başka bir geçmiş zaman sözünün seçildiğini ve gündüzden bakıldığında yaklaşan gecenin de aynı yakınlık ilkesiyle belirlendiğini bildirir."}],"source_summary":"Kanıt, bu kullanımın genel gece adından farklı olarak konuşma gününe ve gün içindeki söyleme anına göre çözüldüğünü gösterir. Yaklaşan gece ile henüz yakın geçmiş sayılan önceki gece, cümlenin yönelimine göre ayrılır.","sources":["TA"],"what_is_ar":"يدخل فيه إطلاق الليلة على أقرب الليالي من اليوم أو على الليلة الداخلة، والفصل بينها وبين البارحة بحسب وقت الكلام","what_is_not_ar":"لا يدخل فيه مطلق الليل ولا الليالي المجموعة ولا أوصاف شدة الظلمة"},"support_links":[]},{"boundary":"Kadın adı temel adlandırma kullanımıdır; şarap anlamı yalnız ayrı ve tam bir söz öbeğinin örtülü ad işlevine aittir.","branch_kind":"non_bare","branch_ref":"root_001392/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:4:1:3","qac_word_ref":"89:4:1","surface_ar":"يْلِ"}],"gloss":"bir kadın adı; ayrıca belirli bir söz öbeğinde şarabın örtülü adı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Söz konusu biçim bir kadını adlandıran kişi adı olarak kullanılır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu adı içeren ayrı bir söz öbeği, şarabı doğrudan söylemeden anan örtülü bir ad olarak kullanılır."}}],"root_ar":"ل ي ل","root_id":"root_001392","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kişi adı çekirdeğini ve yalnız tam söz öbeğine bağlı şarap adlandırmasını sınırlarıyla birlikte açıklar.","boundary_detail":"Kadın adı temel adlandırma kullanımıdır; şarap anlamı yalnız ayrı ve tam bir söz öbeğinin örtülü ad işlevine aittir.","branch_image_ar":"التسمية بليلى","concept_gloss":"bir kadın adı; ayrıca belirli bir söz öbeğinde şarabın örtülü adı","contextual_glosses":[{"applicability":"Biçimin bir kadını adlandırdığı kişi adı kullanımında geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Biçimin kadın kişi adı olma işlevini korur."},"facet_ids":["F001"],"text":"bir kadın adı","usage_role":"contextual"},{"applicability":"Yalnız kadın adını içeren tam söz öbeğinin şarabı dolaylı biçimde andığı kullanımda geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tam söz öbeğinin şarabı örterek adlandırma işlevini korur."},"facet_ids":["F002"],"text":"şarap için kullanılan örtülü ad","usage_role":"contextual"}],"definition":"Bir biçimin kadın adı olarak kullanılmasıdır; aynı adı içeren ayrı bir söz öbeği ise şarabı anan örtülü bir ad işlevi görür. İki kullanım aynı dalda bulunsa da kadın adı ile içki anlamı birbirine eşit değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Söz konusu biçim bir kadını adlandıran kişi adı olarak kullanılır."},{"facet_id":"F002","role":"associated_use","statement":"Bu adı içeren ayrı bir söz öbeği, şarabı doğrudan söylemeden anan örtülü bir ad olarak kullanılır."}],"identity_rationale":"Kaynak ifadesi bir biçimin kadın adı olduğunu ve bu adı içeren ayrı bir söz öbeğinin şarabı örtülü biçimde anlattığını doğrular. Dal bir adlandırma kümesi olarak korunabilir; ancak kadın adının kendi başına şarap anlamına geldiği sanılmamalı, şarap anlamı yalnız tam söz öbeğine bağlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"bir kadın adı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"şarap için kullanılan örtülü ad"}],"lexicalization_note":"Dal yalnız ad olarak kullanılan biçimi ve şarabı anan tam söz öbeğini kapsar; bunlar genel gece veya karanlık anlamına genişletilemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gece dalı ile iki ayrı kişi adı dalı, adlandırma işlevini biçimsel yakınlıktan ve farklı ad kimliklerinden ayırmak için seçildi.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Bu dalın anlamı kişi ve içki adlandırmasıdır; komşu dal ise bir zaman bölümünü ve karanlığı gösterir, dolayısıyla iki dal olağan kullanımda birbirinin yerine geçmez.","focus_only":"Bir kadın adını ve ayrı bir söz öbeğinde şarabın örtülü adını kapsar.","gloss":"adlandırma ile gece anlamı arasındaki ayrım","neighbor_only":"Gece zamanını ve gece karanlığını anlatır.","neighbor_ref":"root_001392/B001","relation_type":"thematic","shared_zone":"Dallar aynı biçim ailesiyle bağlantılıdır, fakat yalnız tarihsel ve biçimsel bir çağrışım paylaşır."},{"boundary_match":"field_only","distinction":"Adlandırma işlevleri aynı alandadır, fakat adların kimlikleri ayrıdır; ayrıca bu dalda belirli bir söz öbeğine bağlı şarap kullanımı bulunur.","focus_only":"Farklı bir kadın adını ve bu adı içeren örtülü şarap sözünü kapsar.","gloss":"iki ayrı kadın adının anlam alanı","neighbor_only":"Başka ve ayrı bir kadın adını kapsar.","neighbor_ref":"root_000848/B009","relation_type":"same_field","shared_zone":"Her iki dal da bir biçimin kadın kişi adı olarak kullanılmasını tanıklar."},{"boundary_match":"field_only","distinction":"Ortak alan adlandırmadır; ancak gösterilen adlar farklıdır ve komşu dalın erkek adı ile lakap kapsamı bu dalda bulunmaz, bu dalın şarap söz öbeği de komşuda yoktur.","focus_only":"Bir kadın adı ile ona bağlı örtülü şarap sözünü içerir.","gloss":"ayrı kişi adları ve lakaplar alanı","neighbor_only":"Başka biçimlerin erkek adı, kadın adı veya lakap olarak kullanılmasını içerir.","neighbor_ref":"root_000799/B007","relation_type":"same_field","shared_zone":"İki dal da sözlük biçimlerinin kişi adı olarak aktarılmasını konu eder."}],"source_phrase_ar":"وبه سميت ليلى (jamhara)؛ ليلى اسم امرأة (sihah)؛ أم ليلى هي الخمر (tahdhib)","source_summary":"Toplu kanıt kadın adı kullanımını ortak biçimde destekler ve ayrıca bu adı içeren tam bir söz öbeğinin şarabı örten bir ad olduğunu bildirir. İkinci kullanım bağımsız söz öbeğine bağlı tutulmalıdır.","sources":["JA","SI","TA"],"what_is_ar":"يدخل فيه ليلى اسما لامرأة، وأم ليلى كنية للخمر","what_is_not_ar":"لا يدخل فيه الليل زمنا ولا الظلمة ولا المعاملة بالليل"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["89:4:1"],"branch_refs":[],"candidate_id":"cand_5255c03841346621a329","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:4:1:closing-oath-dependency","source_type":"word_analysis","support_ids":["sup_46b84c9801643269990c","sup_50bb3d0e96399dc5fe89"],"title":"last overt oath item still awaits its answer","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:1","qac_refs":["89:4:1:1"],"status":"accepted"}},{"anchor_refs":["89:4:1"],"branch_refs":[],"candidate_id":"cand_8feb286e32271ec20248","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:4:1:fused-surface-beat","source_type":"word_analysis","support_ids":["sup_50bb3d0e96399dc5fe89","sup_558bcf2c63c715d4af46"],"title":"prefixed particle tightens the noun's entry","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:1","qac_refs":["89:4:1:1"],"status":"accepted"}},{"anchor_refs":["89:4:1"],"branch_refs":[],"candidate_id":"cand_21a8160ab55554a98aa6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:4:1:oath-connector","source_type":"word_analysis","support_ids":["sup_50bb3d0e96399dc5fe89","sup_a1f0ac3fb391601ac0f7"],"title":"one particle carries oath and continuation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:1","qac_refs":["89:4:1:1"],"status":"accepted"}},{"anchor_refs":["89:4:2"],"branch_refs":[],"candidate_id":"cand_9d4e2af2114b9dfa4596","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"89:4:2:boundary-and-forward-oath","source_type":"word_analysis","support_ids":["sup_932f86aa9e184ae74dc4","sup_c82db92a2ca7bb751f95"],"title":"night closes the prelude for the oath question","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:2","qac_refs":["89:4:1:2","89:4:1:3"],"status":"accepted"}},{"anchor_refs":["89:4:2"],"branch_refs":[],"candidate_id":"cand_8a7739e7485bdabd7332","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"89:4:2:bounded-night-field","source_type":"word_analysis","support_ids":["sup_2036f98113a1637fc12e","sup_932f86aa9e184ae74dc4"],"title":"night is a governed time span","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:2","qac_refs":["89:4:1:2","89:4:1:3"],"status":"accepted"}},{"anchor_refs":["89:4:2"],"branch_refs":[],"candidate_id":"cand_8e2af31b0506f32abd99","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"89:4:2:definite-genitive-oath-night","source_type":"word_analysis","support_ids":["sup_54cd33644fe8c1b0523d","sup_932f86aa9e184ae74dc4"],"title":"known night made evidentiary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:2","qac_refs":["89:4:1:2","89:4:1:3"],"status":"accepted"}},{"anchor_refs":["89:4:2"],"branch_refs":[],"candidate_id":"cand_a7f7e14bd8e0f111434a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"89:4:2:lam-sound-span","source_type":"word_analysis","support_ids":["sup_38b6566cf5333cb75214","sup_932f86aa9e184ae74dc4"],"title":"liquid sound stretches the night noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:2","qac_refs":["89:4:1:2","89:4:1:3"],"status":"accepted"}},{"anchor_refs":["89:4:2"],"branch_refs":[],"candidate_id":"cand_dd712a19946fc5ade474","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"89:4:2:night-oath-reprofiled","source_type":"word_analysis","support_ids":["sup_84075b0aa169ef90d97a","sup_932f86aa9e184ae74dc4"],"title":"covering or stillness becomes transit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:2","qac_refs":["89:4:1:2","89:4:1:3"],"status":"accepted"}},{"anchor_refs":["89:4:2"],"branch_refs":[],"candidate_id":"cand_c8adfcdb50c5be88a0e1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"89:4:2:night-travel-pairing","source_type":"word_analysis","support_ids":["sup_08c961f8e0364caa3b30","sup_932f86aa9e184ae74dc4"],"title":"common night sharpened by rare transit frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:2","qac_refs":["89:4:1:2","89:4:1:3"],"status":"accepted"}},{"anchor_refs":["89:4:2"],"branch_refs":[],"candidate_id":"cand_66e9c8c46394ca9fb13e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"89:4:2:oath-object-becomes-subject","source_type":"word_analysis","support_ids":["sup_45fe20f150ce05b342eb","sup_932f86aa9e184ae74dc4"],"title":"sworn noun becomes moving subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:2","qac_refs":["89:4:1:2","89:4:1:3"],"status":"accepted"}},{"anchor_refs":["89:4:2"],"branch_refs":[],"candidate_id":"cand_340896716f7bb5eb95c5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"89:4:2:plural-to-definite-singular","source_type":"word_analysis","support_ids":["sup_932f86aa9e184ae74dc4","sup_e44d15b3935cdf764a0f"],"title":"plural nights focus into the night","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:2","qac_refs":["89:4:1:2","89:4:1:3"],"status":"accepted"}},{"anchor_refs":["89:4:2"],"branch_refs":[],"candidate_id":"cand_f0e26794306ffe603bb9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"89:4:2:root-dispute-restraint","source_type":"word_analysis","support_ids":["sup_220a9a030e73f8602d80","sup_932f86aa9e184ae74dc4"],"title":"derivative claims stay restrained","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:2","qac_refs":["89:4:1:2","89:4:1:3"],"status":"accepted"}},{"anchor_refs":["89:4:3"],"branch_refs":[],"candidate_id":"cand_66d1a520799f78f4a8b3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:4:3:attached-temporal-clause","source_type":"word_analysis","support_ids":["sup_5acaa483313c68d3bcb8","sup_f30214f9cae4bd36c084"],"title":"temporal clause qualifies the oath noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:3","qac_refs":["89:4:2:1"],"status":"accepted"}},{"anchor_refs":["89:4:3"],"branch_refs":[],"candidate_id":"cand_3219e40475d1c12a17e1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:4:3:boundary-register-shift","source_type":"word_analysis","support_ids":["sup_5acaa483313c68d3bcb8","sup_afe6647aee278b69efa0"],"title":"nominal oath sequence becomes a verbal scene","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:3","qac_refs":["89:4:2:1"],"status":"accepted"}},{"anchor_refs":["89:4:3"],"branch_refs":[],"candidate_id":"cand_5cedd9cb74002ab3eae5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:4:3:event-state-activation","source_type":"word_analysis","support_ids":["sup_5acaa483313c68d3bcb8","sup_837bd727262b51b7e92f"],"title":"night is selected at its moving moment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:3","qac_refs":["89:4:2:1"],"status":"accepted"}},{"anchor_refs":["89:4:3"],"branch_refs":[],"candidate_id":"cand_6fee1318f8d37077f984","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:4:3:separate-threshold","source_type":"word_analysis","support_ids":["sup_5acaa483313c68d3bcb8","sup_fe0fd616015848073ee7"],"title":"particle creates a threshold before motion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:3","qac_refs":["89:4:2:1"],"status":"accepted"}},{"anchor_refs":["89:4:3"],"branch_refs":[],"candidate_id":"cand_a942a88c2088b672a4fc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:4:3:when-whenever-recurrence","source_type":"word_analysis","support_ids":["sup_5acaa483313c68d3bcb8","sup_7f2b5d2e0019a4d91c76"],"title":"punctual scene and recurring order remain together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:3","qac_refs":["89:4:2:1"],"status":"accepted"}},{"anchor_refs":["89:4:4"],"branch_refs":[],"candidate_id":"cand_4cde558d281a70df0366","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000697","root_000702"],"scope":"focus_ayah","source_local_id":"89:4:4:ayah-final-suspended-closure","source_type":"word_analysis","support_ids":["sup_17f119ffbe8d085d3f04","sup_51378820b43478f36a46"],"title":"motion closes the line but not the oath argument","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:4","qac_refs":["89:4:3:1"],"status":"accepted"}},{"anchor_refs":["89:4:4"],"branch_refs":[],"candidate_id":"cand_a1b7d98d530b250970ea","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000697","root_000702"],"scope":"focus_ayah","source_local_id":"89:4:4:boundary-motion-synthesis","source_type":"word_analysis","support_ids":["sup_17f119ffbe8d085d3f04","sup_c333f96950bc26ea7560"],"title":"static counting gives way to flowing transit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:4","qac_refs":["89:4:3:1"],"status":"accepted"}},{"anchor_refs":["89:4:4"],"branch_refs":[],"candidate_id":"cand_64661889367d01886481","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000697","root_000702"],"scope":"focus_ayah","source_local_id":"89:4:4:form-i-not-causative","source_type":"word_analysis","support_ids":["sup_17f119ffbe8d085d3f04","sup_cec5eb32f4bce931b51b"],"title":"agency stays inside the night's own passing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:4","qac_refs":["89:4:3:1"],"status":"accepted"}},{"anchor_refs":["89:4:4"],"branch_refs":[],"candidate_id":"cand_99974d47c0a32ae7c70f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000697","root_000702"],"scope":"focus_ayah","source_local_id":"89:4:4:local-night-travel-echo","source_type":"word_analysis","support_ids":["sup_17f119ffbe8d085d3f04","sup_849a02e2a3934d1a6e4b"],"title":"night noun and travel verb answer each other","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:4","qac_refs":["89:4:3:1"],"status":"accepted"}},{"anchor_refs":["89:4:4"],"branch_refs":[],"candidate_id":"cand_40e66f31540a12835899","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000697","root_000702"],"scope":"focus_ayah","source_local_id":"89:4:4:night-as-moving-subject","source_type":"word_analysis","support_ids":["sup_0bf4892a33ba5ae686fa","sup_17f119ffbe8d085d3f04"],"title":"night itself performs the travel","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:4","qac_refs":["89:4:3:1"],"status":"accepted"}},{"anchor_refs":["89:4:4"],"branch_refs":[],"candidate_id":"cand_cd32543c99b8e489d6a8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000697","root_000702"],"scope":"focus_ayah","source_local_id":"89:4:4:night-travel-lexical-branch","source_type":"word_analysis","support_ids":["sup_17f119ffbe8d085d3f04","sup_cc201f0daf6e3180425d"],"title":"night-travel route pressure survives locally","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:4","qac_refs":["89:4:3:1"],"status":"accepted"}},{"anchor_refs":["89:4:4"],"branch_refs":[],"candidate_id":"cand_62d6a56238c786c6a2d9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000697","root_000702"],"scope":"focus_ayah","source_local_id":"89:4:4:objectless-passage","source_type":"word_analysis","support_ids":["sup_0f989fbb3085108f9139","sup_17f119ffbe8d085d3f04"],"title":"passage matters without endpoint","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:4","qac_refs":["89:4:3:1"],"status":"accepted"}},{"anchor_refs":["89:4:4"],"branch_refs":[],"candidate_id":"cand_2d8ccfc68235691fa07c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000697","root_000702"],"scope":"focus_ayah","source_local_id":"89:4:4:rare-root-pairing","source_type":"word_analysis","support_ids":["sup_17f119ffbe8d085d3f04","sup_46c7fc656e5767bc3485"],"title":"rare travel root is compressed with night","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:4","qac_refs":["89:4:3:1"],"status":"accepted"}},{"anchor_refs":["89:4:4"],"branch_refs":[],"candidate_id":"cand_2cfb6a4137b3f81bba05","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000697","root_000702"],"scope":"focus_ayah","source_local_id":"89:4:4:recurrent-ongoing-imperfect","source_type":"word_analysis","support_ids":["sup_17f119ffbe8d085d3f04","sup_d7fcad51230491255a16"],"title":"motion is caught underway and repeatable","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:4","qac_refs":["89:4:3:1"],"status":"accepted"}},{"anchor_refs":["89:4:4"],"branch_refs":[],"candidate_id":"cand_e75f0160d2939e8afed0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000697","root_000702"],"scope":"focus_ayah","source_local_id":"89:4:4:weak-final-clipping-and-qiraat","source_type":"word_analysis","support_ids":["sup_17f119ffbe8d085d3f04","sup_18b273c4ae45e15ba5d2"],"title":"clipped edge and fuller flow meet at the weak letter","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:4:4","qac_refs":["89:4:3:1"],"status":"accepted"}},{"anchor_refs":["89:4:1"],"branch_refs":[],"candidate_id":"cand_0cc149faac31a4e269b5","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"89:4:1:3","source_type":"qac_morpheme","support_ids":["sup_061dc8cd98306e2c3fff"],"title":"QAC root occurrence: ل ي ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:4:3"],"branch_refs":[],"candidate_id":"cand_2a7181594e1c6efccfd4","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000697","root_000702"],"scope":"focus_ayah","source_local_id":"89:4:3:1","source_type":"qac_morpheme","support_ids":["sup_c44ee89712637a542bde"],"title":"QAC root occurrence: س ر ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:4","branch_refs":["root_000702/B001","root_001392/B001"],"candidate_id":"cand_b288aa75c0cb6835b3d9","commentary_obligation":"review","hft_ref":"hft_547c079b86f565424025","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b01_night_in_transit","source_type":"hft","support_ids":["sup_be8d43e7d63f3850dd0c"],"title":"b01_night_in_transit","trust":"legacy_unbound"},{"anchor_refs":["89:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:4","branch_refs":["root_000702/B002","root_000702/B004"],"candidate_id":"cand_3a88fc0bc6be8a8aada7","commentary_obligation":"review","hft_ref":"hft_bd2ea7b2da4c9fe7e0f5","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b02_flow_unveiling","source_type":"hft","support_ids":["sup_dcd36bde82b0c8b5539d"],"title":"b02_flow_unveiling","trust":"legacy_unbound"},{"anchor_refs":["89:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:4","branch_refs":["root_000697/B001","root_000697/B005","root_001392/B001"],"candidate_id":"cand_eef72432a253294c4c15","commentary_obligation":"review","hft_ref":"hft_2e59b2e3140377d7886b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b03_secret_interior","source_type":"hft","support_ids":["sup_35209214a5688a067e3f"],"title":"b03_secret_interior","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَٱلَّيْلِ إِذَا يَسْرِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"89:4:1:1","qac_word_ref":"89:4:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:4:1:2","qac_word_ref":"89:4:1","root_ar":"","surface_ar":"ٱلَّ"},{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:4:1:3","qac_word_ref":"89:4:1","root_ar":"ل ي ل","surface_ar":"يْلِ"},{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"89:4:2:1","qac_word_ref":"89:4:2","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","root_ar":"س ر ي","surface_ar":"يَسْرِ"}],"word_analysis_qac_refs":[["89:4:1:1"],["89:4:1:2","89:4:1:3"],["89:4:2:1"],["89:4:3:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["89:4:1","89:4:2","89:4:3","89:4:4"]},"focus_surface_evidence":{"arabic_uthmani":"وَٱلَّيْلِ إِذَا يَسْرِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"89:4:1:1","qac_word_ref":"89:4:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:4:1:2","qac_word_ref":"89:4:1","root_ar":"","surface_ar":"ٱلَّ"},{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:4:1:3","qac_word_ref":"89:4:1","root_ar":"ل ي ل","surface_ar":"يْلِ"},{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"89:4:2:1","qac_word_ref":"89:4:2","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"يَسْرِ","morph_features":"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:4:3:1","qac_word_ref":"89:4:3","root_ar":"س ر ي","surface_ar":"يَسْرِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["89:4:1:1"],["89:4:1:2","89:4:1:3"],["89:4:2:1"],["89:4:3:1"]],"word_analysis_refs":["89:4:1","89:4:2","89:4:3","89:4:4"],"word_rows":[{"analysis_record_ref":"89:4:1","analytic_gloss_range_en":"oath particle and connector in the continuing oath sequence","analytic_root_gloss_range_en":null,"qac_refs":["89:4:1:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"89:4:2","analytic_gloss_range_en":"the definite, bounded night interval in an oath frame; not abstract darkness alone","analytic_root_gloss_range_en":"night as the opposite of day and its darkness, with related night-oriented actions and deictic uses; local sense is the known night interval","qac_refs":["89:4:1:2","89:4:1:3"],"root":{"arabic":"ل ي ل","transliteration":"l-y-l"},"surface":{"arabic":"ٱلَّيْلِ","transliteration":"al-layli"}},{"analysis_record_ref":"89:4:3","analytic_gloss_range_en":"temporal when/whenever particle introducing the verbal clause","analytic_root_gloss_range_en":null,"qac_refs":["89:4:2:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"إِذَا","transliteration":"idhā"}},{"analysis_record_ref":"89:4:4","analytic_gloss_range_en":"night passing, travelling, or moving onward intransitively; locally not a command, prohibition, or caused-travel frame","analytic_root_gloss_range_en":"broad root range includes night travel, running flow, height or nobility, uncovering or relief, and fixed nouns; local branch is night-travel motion applied to night itself","qac_refs":["89:4:3:1"],"root":{"arabic":"س ر ي","transliteration":"s-r-y"},"surface":{"arabic":"يَسْرِ","transliteration":"yasri"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["89:4"],"branch_refs":["root_000702/B001","root_001392/B001"],"candidate_id":"cand_b288aa75c0cb6835b3d9","evidence_scope":"focus_ayah","hft_ref":"hft_547c079b86f565424025","item_id":"b01_night_in_transit","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b01_night_in_transit","support_id":"sup_be8d43e7d63f3850dd0c"},{"anchor_refs":["89:4"],"branch_refs":["root_000702/B002","root_000702/B004"],"candidate_id":"cand_3a88fc0bc6be8a8aada7","evidence_scope":"focus_ayah","hft_ref":"hft_bd2ea7b2da4c9fe7e0f5","item_id":"b02_flow_unveiling","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b02_flow_unveiling","support_id":"sup_dcd36bde82b0c8b5539d"},{"anchor_refs":["89:4"],"branch_refs":["root_000697/B001","root_000697/B005","root_001392/B001"],"candidate_id":"cand_eef72432a253294c4c15","evidence_scope":"focus_ayah","hft_ref":"hft_2e59b2e3140377d7886b","item_id":"b03_secret_interior","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b03_secret_interior","support_id":"sup_35209214a5688a067e3f"}],"diagnostics":[],"lane_counts":{"global":18,"macro":8,"micro":3},"packet_summary":{"ayah_count":30,"focus_ref":"89:4","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000702","furuq_root_norm":"س ر ي","furuq_source_root_norm":"س ر ي","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000697","furuq_root_norm":"س ر ر","furuq_source_root_norm":"س ر ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ع و د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":true,"target_occurrences":35,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ج و ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000273","furuq_root_norm":"ج و ب","furuq_source_root_norm":"ج و ب","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000283","furuq_root_norm":"ج ي ب","furuq_source_root_norm":"ج ي ب","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000220","furuq_root_norm":"ج ب ي","furuq_source_root_norm":"ج ب ي","is_dominant":false,"target_occurrences":2,"target_rank":3},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000214","furuq_root_norm":"ج ب ب","furuq_source_root_norm":"ج ب ب","is_dominant":false,"target_occurrences":1,"target_rank":4}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ب ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000153","furuq_root_norm":"ب ل و","furuq_source_root_norm":"ب ل و","is_dominant":true,"target_occurrences":28,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000154","furuq_root_norm":"ب ل ي","furuq_source_root_norm":"ب ل ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ه و ن","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001453","furuq_root_norm":"م ه ن","furuq_source_root_norm":"م ه ن","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001608","furuq_root_norm":"ه و ن","furuq_source_root_norm":"ه و ن","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001687","furuq_root_norm":"و ه ن","furuq_source_root_norm":"و ه ن","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14","89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"89:4","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":12,"source_present":true,"structured_insight_count":17,"unstructured_record_count":0},"identity":{"ayah_ref":"89:4","lane":"micro","linguistic_source_ref":"89:4","surface_ref":"89:4","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"89:4","target_tokens":[["Geçip",["89:4:3"]],["gittiğinde",["89:4:2","89:4:3"]],["geceye",["89:4:1"]],["andolsun",["89:4:1"]]],"text":"Geçip gittiğinde geceye andolsun!"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":14,"id":"s089-p01-001-014","label":"Oaths and the downfall of tyrants","number":1,"refs":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:4:1:3","source_type":"qac_morpheme","support_id":"sup_061dc8cd98306e2c3fff","text":"{\"lemma_ar\":\"لَيْل\",\"morph_features\":\"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"89:4:1:3\",\"qac_word_ref\":\"89:4:1\",\"root_ar\":\"ل ي ل\",\"surface_ar\":\"يْلِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:2:night-travel-pairing","source_type":"word_analysis","support_id":"sup_08c961f8e0364caa3b30","text":"{\"blocking_evidence\":null,\"headline\":\"common night sharpened by rare transit frame\",\"reader_payoff\":\"The reader sees an ordinary night noun sharpened by its constrained pairing with a travel verb.\",\"reason\":\"{{ar:ل ي ل}} ({{tr:l-y-l}}) is common in the profile, while {{ar:س ر ي}} ({{tr:s-r-y}}) is low-occurrence; their local pairing makes night a marked moving sign.\",\"representative_source_ids\":[\"QI-0bfc207a\",\"QI-3af3a541\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:4:night-as-moving-subject","source_type":"word_analysis","support_id":"sup_0bf4892a33ba5ae686fa","text":"{\"blocking_evidence\":null,\"headline\":\"night itself performs the travel\",\"reader_payoff\":\"The reader notices that the action is assigned to night itself, turning cosmic time into an acting subject.\",\"reason\":\"The verb is finite 3ms, and the attachment evidence says its implicit subject is syntactically controlled by {{ar:ٱلَّيْلِ}} ({{tr:al-layli}}), so the personification is grammatically anchored.\",\"representative_source_ids\":[\"QG-4023a1f3\",\"QS-137b8139\",\"MT-98e97c18\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:4:objectless-passage","source_type":"word_analysis","support_id":"sup_0f989fbb3085108f9139","text":"{\"blocking_evidence\":null,\"headline\":\"passage matters without endpoint\",\"reader_payoff\":\"The reader feels the act of passing carry the oath's force without needing a named path, object, or destination.\",\"reason\":\"The verb-instance frame is intransitive with no object or prepositional profile, supporting the CRITICAL compression around motion itself.\",\"representative_source_ids\":[\"QG-77c7f18f\",\"MG-6104e21e\",\"QS-339a3d73\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:4","source_type":"word_analysis","support_id":"sup_17f119ffbe8d085d3f04","text":"{\"gloss_range\":\"night passing, travelling, or moving onward intransitively; locally not a command, prohibition, or caused-travel frame\",\"prose\":\"{{ar:يَسْرِ}} ({{tr:yasri}}) makes the night itself move. Its 3ms finite form points back to {{ar:ٱلَّيْلِ}} ({{tr:al-layli}}), and its objectless frame withholds route and endpoint so passage itself carries the evidentiary force. The selected {{ar:س ر ي}} ({{tr:s-r-y}}) branch is night-travel motion, not a generic elapsed-time verb: the image is a covered route in progress, while the local Form I reading keeps agency inside the night's own passing rather than making another agent cause travel as in 17:1. The limited night-travel field also includes 15:65 and 44:23, but 89:4 compresses that field inward so the night noun and travel verb answer each other locally. The clipped weak-final surface and fuller {{ar:يَسْرِي}} ({{tr:yasrī}}) realization keep both edge and flow audible at the ayah boundary, closing the local oath scene without resolving the larger oath dependency. As the sequence moves from counted or separated time into flowing passage, the final verb turns static oath material into a moving sign.\",\"root_display\":\"{{ar:س ر ي}} ({{tr:s-r-y}})\",\"root_gloss_range\":\"broad root range includes night travel, running flow, height or nobility, uncovering or relief, and fixed nouns; local branch is night-travel motion applied to night itself\",\"surface_display\":\"{{ar:يَسْرِ}} ({{tr:yasri}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:4:weak-final-clipping-and-qiraat","source_type":"word_analysis","support_id":"sup_18b273c4ae45e15ba5d2","text":"{\"blocking_evidence\":null,\"headline\":\"clipped edge and fuller flow meet at the weak letter\",\"reader_payoff\":\"The reader hears the motion word as both compressed at the ayah edge and capable of fuller flow in the restored weak-final reading.\",\"reason\":\"The local parse is finite motion, not a governed jussive command or prohibition; qiraat and surface notes are therefore used to explain weak-final pressure, not to replace the verbal reading.\",\"representative_source_ids\":[\"QG-963aef0c\",\"QF-a237d12e\",\"QF-eb3cbe8d\",\"MP-df5cd87c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:2:bounded-night-field","source_type":"word_analysis","support_id":"sup_2036f98113a1637fc12e","text":"{\"blocking_evidence\":null,\"headline\":\"night is a governed time span\",\"reader_payoff\":\"The reader sees night as a bounded interval capable of passage, not as darkness detached from time.\",\"reason\":\"The V4 branch supports night as the opposite of day and its darkness, while the local noun form and following motion clause select the time-span sense.\",\"representative_source_ids\":[\"QS-b77d7a16\",\"MS-d6c44280\",\"QF-754d95e7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:2:root-dispute-restraint","source_type":"word_analysis","support_id":"sup_220a9a030e73f8602d80","text":"{\"blocking_evidence\":null,\"headline\":\"derivative claims stay restrained\",\"reader_payoff\":\"The reader keeps the recognizable night-field while avoiding overconfident derivative claims from a disputed root analysis.\",\"reason\":\"The QAC root alignment gives {{ar:ل ي ل}} ({{tr:l-y-l}}), but the CRITICAL row itself reports a dispute; the local gloss remains stable, while broader derivative analysis is narrowed.\",\"representative_source_ids\":[\"QS-fdfa7310\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:2:lam-sound-span","source_type":"word_analysis","support_id":"sup_38b6566cf5333cb75214","text":"{\"blocking_evidence\":null,\"headline\":\"liquid sound stretches the night noun\",\"reader_payoff\":\"The reader hears the repeated lām texture lengthen the noun before the ayah releases into the clipped verb.\",\"reason\":\"The assimilated definite article and noun surface make the lām repetition formal, not decorative, and the cadence claim remains local to this phrase.\",\"representative_source_ids\":[\"QF-b2ac55d2\",\"QP-266b659c\",\"MP-78a5962b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:2:oath-object-becomes-subject","source_type":"word_analysis","support_id":"sup_45fe20f150ce05b342eb","text":"{\"blocking_evidence\":null,\"headline\":\"sworn noun becomes moving subject\",\"reader_payoff\":\"The reader notices the same noun move from evidentiary object to semantic actor once the verb arrives.\",\"reason\":\"The implicit-subject evidence identifies the 3ms subject of {{ar:يَسْرِ}} ({{tr:yasri}}) as controlled by the immediately preceding masculine singular {{ar:ٱلَّيْلِ}} ({{tr:al-layli}}).\",\"representative_source_ids\":[\"QG-60232fa1\",\"QT-f8794005\",\"MT-07a88150\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:1:closing-oath-dependency","source_type":"word_analysis","support_id":"sup_46b84c9801643269990c","text":"{\"blocking_evidence\":null,\"headline\":\"last overt oath item still awaits its answer\",\"reader_payoff\":\"The reader sees 89:4 as a closing oath member whose force remains suspended beyond the ayah rather than a self-contained night image.\",\"reason\":\"The ellipsis evidence marks the oath predicate as omitted by convention, and the discourse support says the temporal night clause continues the oath sequence rather than standing alone.\",\"representative_source_ids\":[\"QG-f0674175\",\"QT-4e2b020e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:4:rare-root-pairing","source_type":"word_analysis","support_id":"sup_46c7fc656e5767bc3485","text":"{\"blocking_evidence\":null,\"headline\":\"rare travel root is compressed with night\",\"reader_payoff\":\"The reader notices that a limited {{ar:س ر ي}} ({{tr:s-r-y}}) movement field is concentrated into an ayah-final verb beside the night noun.\",\"reason\":\"The context profile marks the local root-form as low occurrence, and the CRITICAL row gives concrete night-travel co-occurrences in 15:65, 17:1, and 44:23; 89:4 turns that field inward by making night itself travel.\",\"representative_source_ids\":[\"QI-b40182b4\",\"QI-efeb7e93\",\"QH-c75c7d9f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:1","source_type":"word_analysis","support_id":"sup_50bb3d0e96399dc5fe89","text":"{\"gloss_range\":\"oath particle and connector in the continuing oath sequence\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) does double work: it joins this phrase to the previous oath terms and also makes {{ar:ٱلَّيْلِ}} ({{tr:al-layli}}) a fresh sworn witness. Because the particle is prefixed directly onto the noun, the entry of night feels compressed into one oath beat rather than added as a loose preface, with the liquid opening of the night noun preparing the later clipped motion verb. It also leaves the oath dependency unresolved inside 89:4, so the ayah closes the overt oath prelude while still waiting for the later answer.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:4:ayah-final-suspended-closure","source_type":"word_analysis","support_id":"sup_51378820b43478f36a46","text":"{\"blocking_evidence\":null,\"headline\":\"motion closes the line but not the oath argument\",\"reader_payoff\":\"The reader feels local closure at the final verb while the oath's argumentative answer remains delayed.\",\"reason\":\"The verb is ayah-final and closes the overt oath item, while attachment evidence keeps the oath predicate omitted and the larger sequence unresolved beyond this ayah.\",\"representative_source_ids\":[\"QT-485e0a8c\",\"QB-0a4569bf\",\"QP-e45e36b9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:2:definite-genitive-oath-night","source_type":"word_analysis","support_id":"sup_54cd33644fe8c1b0523d","text":"{\"blocking_evidence\":null,\"headline\":\"known night made evidentiary\",\"reader_payoff\":\"The reader notices that the verse swears by the known recurring night, not an unspecified dark episode.\",\"reason\":\"QAC marks {{ar:ٱلَّيْلِ}} ({{tr:al-layli}}) as singular definite genitive, and attachment evidence makes it the oath complement governed by {{ar:وَ}} ({{tr:wa}}).\",\"representative_source_ids\":[\"QG-b1ac9fa9\",\"QG-b35fa6a7\",\"MG-bfcb9eeb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:1:fused-surface-beat","source_type":"word_analysis","support_id":"sup_558bcf2c63c715d4af46","text":"{\"blocking_evidence\":null,\"headline\":\"prefixed particle tightens the noun's entry\",\"reader_payoff\":\"The reader hears the particle and night noun enter as one compact surface beat before the later clipped motion verb.\",\"reason\":\"Bundle segmentation splits the particle, but the surface phrase is prefixed in recitation and writing, supporting the CRITICAL point about formal compression and sound texture.\",\"representative_source_ids\":[\"QF-c8c96c0f\",\"QP-4588fb37\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:3","source_type":"word_analysis","support_id":"sup_5acaa483313c68d3bcb8","text":"{\"gloss_range\":\"temporal when/whenever particle introducing the verbal clause\",\"prose\":\"{{ar:إِذَا}} ({{tr:idhā}}) is the hinge that keeps {{ar:يَسْرِ}} ({{tr:yasri}}) attached to the sworn night rather than opening an independent condition. It does more than supply bare time: after the noun has been named, it activates the moment when night enters motion. Its when/whenever force lets the scene be vivid at a point and recurrent in cosmic order, while the separate particle creates a brief threshold before the motion verb. After the nominal oath terms of 89:1-3, this temporal hinge is where the sequence turns into a kinetic scene.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِذَا}} ({{tr:idhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:3:when-whenever-recurrence","source_type":"word_analysis","support_id":"sup_7f2b5d2e0019a4d91c76","text":"{\"blocking_evidence\":null,\"headline\":\"punctual scene and recurring order remain together\",\"reader_payoff\":\"The reader feels both the immediate scene of night passing and the recurring rhythm by which night passes again and again.\",\"reason\":\"QAC identifies {{ar:إِذَا}} ({{tr:idhā}}) as a temporal particle introducing a recurring or eventive time clause, so neither punctual nor recurrent force needs to be erased.\",\"representative_source_ids\":[\"QS-57a49d24\",\"QS-6a7904bc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:3:event-state-activation","source_type":"word_analysis","support_id":"sup_837bd727262b51b7e92f","text":"{\"blocking_evidence\":null,\"headline\":\"night is selected at its moving moment\",\"reader_payoff\":\"The reader notices that the oath focuses on night as it begins to move, not night as a static category.\",\"reason\":\"The particle follows the oath noun and governs the verbal clause, creating a marked event-time in which the named night becomes eventive.\",\"representative_source_ids\":[\"QG-758d630a\",\"QS-639ccea9\",\"QT-31bd4171\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:2:night-oath-reprofiled","source_type":"word_analysis","support_id":"sup_84075b0aa169ef90d97a","text":"{\"blocking_evidence\":null,\"headline\":\"covering or stillness becomes transit\",\"reader_payoff\":\"The reader hears the familiar night-oath field shift from covering in 92:1 and stillness in 93:2 into motion in 89:4.\",\"reason\":\"The inter-ayah rows give concrete contrasts, so the echo survives as a profile shift: the same night-field receives a changed predicate in 89:4.\",\"representative_source_ids\":[\"QI-a52c8020\",\"MI-0b1ce35e\",\"QE-30865acf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:4:local-night-travel-echo","source_type":"word_analysis","support_id":"sup_849a02e2a3934d1a6e4b","text":"{\"blocking_evidence\":null,\"headline\":\"night noun and travel verb answer each other\",\"reader_payoff\":\"The reader hears the local roots form a compact exchange: the noun names the time and the verb gives that time its movement.\",\"reason\":\"Both local roots are present in the same clause, and the syntax makes {{ar:ٱلَّيْلِ}} ({{tr:al-layli}}) the controller of {{ar:يَسْرِ}} ({{tr:yasri}}).\",\"representative_source_ids\":[\"QE-f0e1feb9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:2","source_type":"word_analysis","support_id":"sup_932f86aa9e184ae74dc4","text":"{\"gloss_range\":\"the definite, bounded night interval in an oath frame; not abstract darkness alone\",\"prose\":\"{{ar:ٱلَّيْلِ}} ({{tr:al-layli}}) is definite and genitive, so the familiar night is not just named but placed under oath. Its sense is a bounded dark interval rather than darkness as a substance, and the singular definite form gathers the earlier plural nights of 89:2 into one known night-field while keeping broader root-derivative claims restrained. The repeated lām texture lets that known night-field sound extended before release into motion. The following {{ar:إِذَا يَسْرِ}} ({{tr:idhā yasri}}) then animates the field: the noun begins as the sworn object and becomes the understood subject of motion, and the common night noun is sharpened by a rarer transit pairing. This differs from night as covering in 92:1 or stillness in 93:2; here the known night is reprofiled as ordered transit after the numerical pair of 89:3 and becomes the final oath item gathered by the question in 89:5.\",\"root_display\":\"{{ar:ل ي ل}} ({{tr:l-y-l}})\",\"root_gloss_range\":\"night as the opposite of day and its darkness, with related night-oriented actions and deictic uses; local sense is the known night interval\",\"surface_display\":\"{{ar:ٱلَّيْلِ}} ({{tr:al-layli}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:1:oath-connector","source_type":"word_analysis","support_id":"sup_a1f0ac3fb391601ac0f7","text":"{\"blocking_evidence\":null,\"headline\":\"one particle carries oath and continuation\",\"reader_payoff\":\"The reader notices that {{ar:وَ}} ({{tr:wa}}) is not merely and; it keeps the sequence moving while also making the night evidentiary.\",\"reason\":\"The QAC grammar allows oath, coordination, or resumption, and the attachment evidence governs {{ar:ٱلَّيْلِ}} ({{tr:al-layli}}) under the oath particle; the CRITICAL claim therefore survives as a combined oath-connector force.\",\"representative_source_ids\":[\"QG-095a41c0\",\"QS-3d5f203c\",\"MG-1cadac51\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:3:boundary-register-shift","source_type":"word_analysis","support_id":"sup_afe6647aee278b69efa0","text":"{\"blocking_evidence\":null,\"headline\":\"nominal oath sequence becomes a verbal scene\",\"reader_payoff\":\"The reader notices the oath sequence turn from named categories into a kinetic scene at 89:4.\",\"reason\":\"The boundary claim is supported by the local form shift: 89:4 contains a temporal particle plus finite verb after the previous nominal oath items.\",\"representative_source_ids\":[\"QB-0d287c33\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:4:boundary-motion-synthesis","source_type":"word_analysis","support_id":"sup_c333f96950bc26ea7560","text":"{\"blocking_evidence\":null,\"headline\":\"static counting gives way to flowing transit\",\"reader_payoff\":\"The reader notices the oath sequence turn from counted or separated time into a moving night scene.\",\"reason\":\"The synthesis rows are supported by local structure: definite night, temporal {{ar:إِذَا}} ({{tr:idhā}}), and the clipped motion verb together make the final oath member an ordered passage in progress.\",\"representative_source_ids\":[\"QB-1c0b87a7\",\"QB-d1597b08\",\"QY-6f0f593e\",\"QY-aae4b088\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:4:3:1","source_type":"qac_morpheme","support_id":"sup_c44ee89712637a542bde","text":"{\"lemma_ar\":\"يَسْرِ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:yasori|ROOT:sry|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"89:4:3:1\",\"qac_word_ref\":\"89:4:3\",\"root_ar\":\"س ر ي\",\"surface_ar\":\"يَسْرِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:2:boundary-and-forward-oath","source_type":"word_analysis","support_id":"sup_c82db92a2ca7bb751f95","text":"{\"blocking_evidence\":null,\"headline\":\"night closes the prelude for the oath question\",\"reader_payoff\":\"The reader sees the night term return after the numerical pair of 89:3 and feed the oath-question of 89:5.\",\"reason\":\"The boundary rows name the local sequence: 89:3 intervenes with paired numerical abstraction, then 89:4 supplies the final overt oath object gathered by 89:5.\",\"representative_source_ids\":[\"QB-0eaa092c\",\"QB-cd579d3e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:4:night-travel-lexical-branch","source_type":"word_analysis","support_id":"sup_cc201f0daf6e3180425d","text":"{\"blocking_evidence\":null,\"headline\":\"night-travel route pressure survives locally\",\"reader_payoff\":\"The reader senses a route-in-progress under night cover rather than a generic word for going or elapsed time.\",\"reason\":\"V4 accepts a night-travel branch for {{ar:س ر ي}} ({{tr:s-r-y}}), and the local noun {{ar:ٱلَّيْلِ}} ({{tr:al-layli}}) strongly licenses that branch; derivative details such as detachments remain illustrative rather than independent local senses.\",\"representative_source_ids\":[\"QS-3d803317\",\"QS-4af91bbb\",\"QS-bd6d1381\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:4:form-i-not-causative","source_type":"word_analysis","support_id":"sup_cec5eb32f4bce931b51b","text":"{\"blocking_evidence\":null,\"headline\":\"agency stays inside the night's own passing\",\"reader_payoff\":\"The reader sees the contrast with caused night travel in 17:1: here the night moves, rather than someone being led through it.\",\"reason\":\"The CRITICAL contrast with {{ar:أَسْرَى}} ({{tr:asrā}}) survives, but it is narrowed to agency and form contrast; it does not import a causative frame into 89:4.\",\"representative_source_ids\":[\"QF-df99fe95\",\"QI-deaf7b80\",\"MI-4d1d602a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:4:recurrent-ongoing-imperfect","source_type":"word_analysis","support_id":"sup_d7fcad51230491255a16","text":"{\"blocking_evidence\":null,\"headline\":\"motion is caught underway and repeatable\",\"reader_payoff\":\"The reader sees night in the act of passing, not as a completed departure once in the past.\",\"reason\":\"QAC describes the local form as finite imperfect-like, and the pairing with {{ar:إِذَا}} ({{tr:idhā}}) licenses eventive recurrence.\",\"representative_source_ids\":[\"QG-ca3f7797\",\"QG-d20bfb4b\",\"QF-8cbc4cbb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:2:plural-to-definite-singular","source_type":"word_analysis","support_id":"sup_e44d15b3935cdf764a0f","text":"{\"blocking_evidence\":null,\"headline\":\"plural nights focus into the night\",\"reader_payoff\":\"The reader catches the sequence moving from the plural nights of 89:2 to one definite archetypal night in 89:4.\",\"reason\":\"The CRITICAL echo is intra-surah and concrete: the singular definite noun in 89:4 recalls and focuses the earlier plural night-field from 89:2.\",\"representative_source_ids\":[\"QG-e718c18c\",\"QE-c036b092\",\"ME-0c3d255c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:3:attached-temporal-clause","source_type":"word_analysis","support_id":"sup_f30214f9cae4bd36c084","text":"{\"blocking_evidence\":null,\"headline\":\"temporal clause qualifies the oath noun\",\"reader_payoff\":\"The reader keeps the motion clause tied to the sworn night instead of treating it as a free-standing condition.\",\"reason\":\"Attachment evidence marks {{ar:إِذَا يَسْرِ}} ({{tr:idhā yasri}}) as a temporal clause describing when the night moves on, with no separate apodosis inside 89:4.\",\"representative_source_ids\":[\"QG-5f31ef99\",\"QT-a88bbe8e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:4:3:separate-threshold","source_type":"word_analysis","support_id":"sup_fe0fd616015848073ee7","text":"{\"blocking_evidence\":null,\"headline\":\"particle creates a threshold before motion\",\"reader_payoff\":\"The reader hears a small formal pause between the night noun and the verb, matching the particle's threshold role.\",\"reason\":\"The particle stands separately between the noun and verb, and its hamza-bearing onset supports the local sound-function observation without changing the parse.\",\"representative_source_ids\":[\"QF-4ba02fcf\",\"QP-dc0ea3df\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلَّيْلِ إِذَا يَسْرِ","ayah_ref":"89:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000702/B001","root_001392/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001392","role":"Supplies night as darkness opposed to day, the interval whose motion is being predicated.","root":"ل ي ل","source_ref":"89:4","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000702","role":"Supplies travel by night and makes the nocturnal interval itself a traveler.","root":"س ر ي","source_ref":"89:4","source_word_indices":["3"]}],"changed_reading":{"after":"An oath by night precisely as it is in transit, making passage and impermanence the focus.","before":"An oath by night as a dark span of time."},"confidence":"strong","focus_anchor":"Focus word 1 names night, while the verb at word 3 predicates motion of that night rather than merely locating an unnamed traveler within it.","mechanism":"Darkness becomes an agentive temporal interval: it enters, traverses, and leaves. The oath therefore attends to transition itself, not to a static nocturnal scene.","model_id":"b01_night_in_transit"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b01_night_in_transit","source_type":"hft","support_id":"sup_be8d43e7d63f3850dd0c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلَّيْلِ إِذَا يَسْرِ","ayah_ref":"89:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000702/B002","root_000702/B004"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000702","role":"Supplies running water and creeping root-flow, giving the passage continuity, materiality, and direction.","root":"س ر ي","source_ref":"89:4","source_word_indices":["3"]},{"branch_id":"B004","mapped_root_id":"root_000702","role":"Supplies uncovering and relief, making the current's departure a disclosure rather than a mere disappearance.","root":"س ر ي","source_ref":"89:4","source_word_indices":["3"]}],"changed_reading":{"after":"Night drains onward as a current whose very passing uncovers and relieves.","before":"Night simply goes away."},"confidence":"medium","focus_anchor":"The motion verb at focus word 3 carries branch images of continuous flow and of uncovering.","mechanism":"Night passes like a running or creeping current. Its movement does work: as the current advances, what darkness covered is progressively released or disclosed.","model_id":"b02_flow_unveiling"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b02_flow_unveiling","source_type":"hft","support_id":"sup_dcd36bde82b0c8b5539d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلَّيْلِ إِذَا يَسْرِ","ayah_ref":"89:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000697/B001","root_000697/B005","root_001392/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001392","role":"Supplies the covering darkness within which an interior process can remain unseen.","root":"ل ي ل","source_ref":"89:4","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000697","role":"Supplies inward concealment from the split mapping and turns transit into hidden interior work.","root":"س ر ي","source_ref":"89:4","source_word_indices":["3"]},{"branch_id":"B005","mapped_root_id":"root_000697","role":"Supplies an innermost or choicest core, giving the concealed movement a possible point of concentration.","root":"س ر ي","source_ref":"89:4","source_word_indices":["3"]}],"changed_reading":{"after":"A public cosmic motion that may simultaneously figure concealed inward change.","before":"A public cosmic scene in which darkness moves across the sky."},"confidence":"exploratory","focus_anchor":"The packet's non-dominant split mapping for the focus root at word 3 opens an inward-concealment branch while word 1 still anchors the reading in night.","mechanism":"The night's visible transit can carry an invisible interior process: concealed matter moves, matures, or reaches its choicest core beneath the dark surface.","model_id":"b03_secret_interior"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b03_secret_interior","source_type":"hft","support_id":"sup_35209214a5688a067e3f","trust":"legacy_unbound"}]}
</lane_packet_json>
