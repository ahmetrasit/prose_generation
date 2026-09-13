# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **91:7**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s091-regular-20260912/s091/91_7/micro.discovery.json` and modify nothing
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
  "ayah_ref": "91:7",
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
{"branch_registry":[{"boundary":"Bu dal başkalık, orta konum ya da bir nesnenin kendi içinde düzgün olması anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000766/B001","candidate_links":[{"candidate_id":"cand_4179c04160b9c40cdde6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:7:3:1","qac_word_ref":"91:7:3","surface_ar":"سَوَّىٰ"}],"gloss":"iki şeyi birbirine denk kılma veya denk sayma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki şey aynı ölçüye ya da değere eriştiğinde birbirini karşılar ve eş sayılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir malın belirli bir değeri karşılaması, denkliğin fiyat ve ölçü alanındaki görünümüdür."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Eşlik bildiren kalıplar iki kişi ya da şey arasında ayrım bulunmadığını anlatır."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ölçü, değer, nicelik, nitelik ve durum bakımından karşılıklı denkliği anlatan çekirdek kullanımlar için uygundur.","boundary_detail":"Bu dal başkalık, orta konum ya da bir nesnenin kendi içinde düzgün olması anlamlarını kapsamaz.","branch_image_ar":"مساواة ومعادلة بين شيئين","concept_gloss":"iki şeyi birbirine denk kılma veya denk sayma","contextual_glosses":[{"applicability":"İki tarafın aynı düzeyde bulunduğunu söyleyen kısa ve doğal bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılaştırılan iki tarafın aynı düzeyde bulunması anlamını korur."},"facet_ids":["F001"],"text":"eşit olmak","usage_role":"contextual"},{"applicability":"Bir malın fiyatının ya da ölçülebilir değerinin başka bir miktarı karşılaması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Değer karşılaştırmasını ve iki miktarın birbirini karşılamasını korur."},"facet_ids":["F002"],"text":"değeri buna denk olmak","usage_role":"contextual"}],"definition":"İki şeyi ölçü, değer, nicelik, nitelik ya da durum bakımından birbirine denk kılma veya denk sayma; bu denkliği eşlik bildiren belirli söz kalıplarında dile getirme.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki şey aynı ölçüye ya da değere eriştiğinde birbirini karşılar ve eş sayılır."},{"facet_id":"F002","role":"specialization","statement":"Bir malın belirli bir değeri karşılaması, denkliğin fiyat ve ölçü alanındaki görünümüdür."},{"facet_id":"F003","role":"associated_use","statement":"Eşlik bildiren kalıplar iki kişi ya da şey arasında ayrım bulunmadığını anlatır."}],"identity_rationale":"Kaynak anlatımı, iki şeyin değer, ölçü ya da durum bakımından birbirini karşılamasını çekirdek anlam olarak verir; eş olma bildiren kalıplaşmış kullanımlar da bu çekirdeğe bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi ötekinin ölçüsüne ulaştırarak eşitlemek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"iki şeyi ölçü, ağırlık, nicelik ya da nitelik bakımından eşitleme"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir işte aynı düzeyde ve eşit durumda"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"eş, benzer"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"ikisi de bir, ikisi eşit"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"özellikle, hele"}],"lexicalization_note":"Tanım eşitlik çekirdeğini korur; belirli söz kalıplarının özel işlevlerini yalın biçimin bütün anlamına yaymaz.","neighbor_coverage_note":"Adayların tümü karşılaştırıldı; genel eşitlik dalı, kapsam farkını en açık gösteren ve okur karışıklığını en iyi gideren komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın sınırı belirli değer karşılaştırmalarını ve kalıplaşmış eşlik sözlerini içerirken komşu dal genel eşitleme, benzetme ve dengeleme alanında kalır.","focus_only":"Odak dal, değer ve fiyat denkliğini ve eşlik bildiren özel söz kalıplarını da içerir.","gloss":"genel eşitlik ve benzerlik","neighbor_only":"Komşu dal, iki şeyi benzetme ve dengeleme işlemini daha genel bir alanda anlatır.","neighbor_ref":"root_000991/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da iki şeyin birbirini karşılaması ve eş sayılması alanında buluşur."}],"source_phrase_ar":"أصل يدل على استقامة واعتدال بين شيئين (maqayis)؛ لا يساوي كذا أي لا يعادله (maqayis;sihah;tahdhib)؛ المساواة والاستواء واحد (ayn)؛ السِيّ المثل من قولهم سِيّان أي مثلان (jamhara;maqayis;mufradat)؛ لا سِيّما أي لا مثل ما (maqayis)؛ هذا الثوب يساوي كذا (mufradat)","source_summary":"Kaynakların ortak çizgisi, iki tarafın birbirinin ölçüsüne ulaşması ve bu nedenle eş ya da birbirini karşılar durumda bulunmasıdır; değer bildirme ve eşlik kalıpları bu çizginin özel kullanımlarıdır.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه ساوى ويساوي وتساوى واستوى بمعنى تعادل، والسواء والسَّويّة في الأمر، والسِيّ وسِيّان ولا سِيّما، وما يوازي الشيء في قدر أو ثمن.","what_is_not_ar":"ليس هو سوى بمعنى غير، ولا وسط الشيء، ولا كساء السَّويّة."},"support_links":["sup_051b15c553e5f0bf5c7a"]},{"boundary":"Buradaki düzgünlük iki ayrı şeyi eşitlemek değil, tek bir varlığın kendi yapısındaki doğruluk ve iyiliktir.","branch_kind":"mixed_non_bare","branch_ref":"root_000766/B002","candidate_links":[{"candidate_id":"cand_4c482ef9adf32142ff3b","lane":"micro"},{"candidate_id":"cand_b0ce2b6cc5181e104841","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:7:3:1","qac_word_ref":"91:7:3","surface_ar":"سَوَّىٰ"}],"gloss":"kendi içinde düzgün ve tam duruma gelme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin kendi yapısı içinde eğrilikten kurtulması ve düzgün duruma gelmesi çekirdektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsan yaratılışında düzgünlük, görünür bozukluk ve hastalık bulunmayan tam bir yapıyı anlatır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çocukların ve hayvanların iyi durumda olması, belirli bir söz kalıbına bağlı değerlendirmedir."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir varlığın eğrilikten, eksiklikten ya da yapısal bozukluktan kurtulmasını anlatan genel kullanımlar için uygundur.","boundary_detail":"Buradaki düzgünlük iki ayrı şeyi eşitlemek değil, tek bir varlığın kendi yapısındaki doğruluk ve iyiliktir.","branch_image_ar":"استقامة وتمام في الذات","concept_gloss":"kendi içinde düzgün ve tam duruma gelme","contextual_glosses":[{"applicability":"Önceden eğri olan bir nesnenin düz ve doğru duruma gelmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başlangıçtaki eğriliğin giderilmesini ve düzgünleşme sonucunu korur."},"facet_ids":["F001"],"text":"eğrilikten kurtulup doğrulmak","usage_role":"contextual"},{"applicability":"İnsanın görünüş ve sağlık bakımından kusursuz sayılan yapısını anlatırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapısal düzgünlüğü, görünür bozukluk bulunmamasını ve sağlığı korur."},"facet_ids":["F002"],"text":"yapısı düzgün ve sağlıklı olmak","usage_role":"contextual"}],"definition":"Bir şeyi eğrilik, eksiklik ya da yapısal bozukluktan arındırarak kendi içinde düzgün ve tam duruma getirme; varlığın bu düzgün, sağlıklı ya da iyi durumda bulunması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin kendi yapısı içinde eğrilikten kurtulması ve düzgün duruma gelmesi çekirdektir."},{"facet_id":"F002","role":"specialization","statement":"İnsan yaratılışında düzgünlük, görünür bozukluk ve hastalık bulunmayan tam bir yapıyı anlatır."},{"facet_id":"F003","role":"associated_use","statement":"Çocukların ve hayvanların iyi durumda olması, belirli bir söz kalıbına bağlı değerlendirmedir."}],"identity_rationale":"Kaynak anlatımı bir şeyin eğrilikten kurtulup kendi yapısı içinde düzgünleşmesini, eksiksiz ve sağlıklı duruma gelmesini açıkça aynı dalda toplar.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir şeyi düzeltip düzgün ya da eksiksiz duruma getirmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"eğrilikten kurtulup doğrulmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yapısı düzgün, eksiksiz ve sağlıklı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"çocuklarımız ve hayvanlarımız iyi durumda"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"düz arazi"}],"lexicalization_note":"Tanım yalın düzgünleşme anlamını korur; arazi, çocuklar ve hayvanlarla kurulan özel sözlerin kapsamını ayrıca belirtir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; doğrultma ve dengeli olma dalı, yapısal düzgünlükle en güçlü anlam örtüşmesini gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal tek varlığın yapısal tamlığına ve sağlığına uzanır; komşu dal ise doğrultma eylemi ile beden veya sıcaklık dengesini daha belirgin biçimde öne çıkarır.","focus_only":"Odak dal, sağlıklı ve eksiksiz yaratılış ile çocukların ve hayvanların iyi durumunu da kapsar.","gloss":"doğrultma ve dengeli olma","neighbor_only":"Komşu dal, bir şeyi doğrultma eylemini ve organlar ile sıcaklık arasındaki dengeyi ayrıca kapsar.","neighbor_ref":"root_000991/B005","relation_type":"near_synonym","shared_zone":"İki dal da eğrilik ya da dengesizlikten uzak, düzgün bir durumu anlatır."}],"source_phrase_ar":"سويت الشيء فاستوى (ayn;sihah)؛ استوى من اعوجاج (sihah;tahdhib)؛ السوي الذي سوى الله خلقه لا دمامة فيه ولا داء (ayn)؛ السوي فعيل في معنى مفتعل أي مستو (tahdhib)؛ السوي يقال فيما يصان عن الإفراط والتفريط (mufradat)؛ أولادنا وماشيتنا سوية صالحة (maqayis;tahdhib)","source_summary":"Kaynaklar düzgünleştirme ile düzgün duruma gelmeyi birbirine bağlı verir; insan yapısındaki sağlık ve tamlık ile ev halkı ve hayvanların iyi durumu bu çekirdeğin özel görünümleridir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه تسوية الشيء حتى يستوي، والاعتدال بعد اعوجاج، والسوي في الخلق أو الخلق، وصلاح الأولاد والماشية.","what_is_not_ar":"ليس هو المعادلة بين شيئين، ولا العلو على شيء، ولا سوى بمعنى غير."},"support_links":["sup_7476908a9241241c8779","sup_cb48e2d7a205ef978585"]},{"boundary":"Anlam yalnız üzerine gelme yapısına bağlıdır; bir yöne yönelme ya da iki şeyin eşitliği bu dala girmez.","branch_kind":"collocation","branch_ref":"root_000766/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:7:3:1","qac_word_ref":"91:7:3","surface_ar":"سَوَّىٰ"}],"gloss":"üzerine çıkıp yerleşmek veya egemen olmak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bineğin ya da başka bir şeyin üstüne çıkmak ve onun üzerinde yerleşmek temel somut kullanımdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı yapı üstün gelip denetimi ele alma ve egemen olma anlamına genişleyebilir."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Üzerine gelme bildiren yapı içindeki somut yükselme ve bağlamsal egemenlik kullanımlarına özgüdür.","boundary_detail":"Anlam yalnız üzerine gelme yapısına bağlıdır; bir yöne yönelme ya da iki şeyin eşitliği bu dala girmez.","branch_image_ar":"علو واستقرار على شيء","concept_gloss":"üzerine çıkıp yerleşmek veya egemen olmak","contextual_glosses":[{"applicability":"Bir kişinin bineğin sırtına çıkarak üzerinde oturması ya da durması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yukarı çıkma hedefini ve çıkıştan sonra üzerinde yerleşme sonucunu korur."},"facet_ids":["F001"],"text":"bineğin sırtına çıkıp yerleşmek","usage_role":"contextual"},{"applicability":"Bedensel çıkıştan çok güç ve denetim üstünlüğünün anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Üstünlük kurma ve denetimi ele geçirme genişlemesini korur."},"facet_ids":["F002"],"text":"üstün gelip egemen olmak","usage_role":"contextual"}],"definition":"Üzerine gelme bildiren yapı içinde bir şeyin üstüne çıkıp orada yerleşme; bağlama göre üstünlük kurup egemen duruma gelme.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bineğin ya da başka bir şeyin üstüne çıkmak ve onun üzerinde yerleşmek temel somut kullanımdır."},{"facet_id":"F002","role":"extension","statement":"Aynı yapı üstün gelip denetimi ele alma ve egemen olma anlamına genişleyebilir."}],"identity_rationale":"Kaynak anlatımı, üzerine gelme bildiren yapı içinde hem bir bineğin üstüne çıkıp yerleşmeyi hem de üstün gelip egemen olmayı verir; bu nedenle dal yalnız bedensel yükselişle sınırlandırılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bineğinin sırtına çıkıp yerleşmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"üzerine çıkmak ya da egemen olmak"}],"lexicalization_note":"Tanım yalnız üzerine gelme bildiren yapıya bağlanır ve bu yapının yükselme, yerleşme ve egemen olma kapsamını korur.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; seçilen komşu somut binme kesişimini gösterirken dalın yerleşme ve egemenlik sınırını da belirginleştirir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal belirli binme ve çiftleşme eylemlerine odaklanır; odak dal ise üzerine gelme yapısında yerleşmeyi ve egemenlik genişlemesini de taşır.","focus_only":"Odak dal, çıkıştan sonra üstte yerleşmeyi ve bağlama göre egemenlik kurmayı içerir.","gloss":"bir canlının üstüne çıkma","neighbor_only":"Komşu dal, kişinin ata sıçrayarak binmesini ve erkek hayvanın dişinin üstüne çıkmasını anlatır.","neighbor_ref":"root_000459/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir canlının başka bir canlının sırtına ya da üstüne çıkması bulunur."}],"source_phrase_ar":"استوى على ظهر دابته أي علا واستقر (sihah)؛ استويت فوق الدابة وعلى ظهر الدابة أي علوته (tahdhib)؛ استوى أي استولى وظهر (sihah)؛ متى عدي بعلى اقتضى معنى الاستيلاء (mufradat)","source_summary":"Kaynak anlatımı, üzerine çıkıp yerleşme ile üstünlük kurma arasında yapıya bağlı bir anlam alanı kurar; somut binme örneği çekirdeği, egemenlik ise bağlamsal genişlemeyi gösterir.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه استوى على الدابة أو فوقها بمعنى علا واستقر، واستوى على بمعنى علا أو استولى وظهر في الشواهد التي تذكرها المصادر.","what_is_not_ar":"ليس هو استوى إلى بمعنى قصد، ولا تساوى بمعنى تعادل، ولا استواء الخلقة."},"support_links":[]},{"boundary":"Bu anlam yönelme bildiren yapıya bağlıdır; üzerine çıkma, kendi içinde düzgünleşme ve eşitlik anlamlarından ayrıdır.","branch_kind":"collocation","branch_ref":"root_000766/B004","candidate_links":[{"candidate_id":"cand_74b25835ef8bf1766191","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:7:3:1","qac_word_ref":"91:7:3","surface_ar":"سَوَّىٰ"}],"gloss":"bir hedefe yönelip onu amaç edinmek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir hedefe yönelmek ve onu amaç edinmek yapının temel anlamıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yöneliş bazı açıklamalarda hedefe erişme, bazılarında hedefle ilgili işi düzenleme olarak belirginleşir."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yönelme bildiren yapı içinde hedefe dönme, onu amaçlama ve ona yönelik işe koyulma bağlamlarında kullanılır.","boundary_detail":"Bu anlam yönelme bildiren yapıya bağlıdır; üzerine çıkma, kendi içinde düzgünleşme ve eşitlik anlamlarından ayrıdır.","branch_image_ar":"إقبال وقصد إلى جهة","concept_gloss":"bir hedefe yönelip onu amaç edinmek","contextual_glosses":[{"applicability":"Göğün hedef olarak gösterildiği ve hareket ya da yönelişin öne çıktığı bağlam için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli hedefe doğru yönelme ve onu amaç edinme özelliklerini korur."},"facet_ids":["F001"],"text":"göğe yönelmek","usage_role":"contextual"},{"applicability":"Bedensel hareket yerine hedefle ilgili işi yönetme yorumunun gerektiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hedefe yönelişi ve onunla ilgili işi amaçlı biçimde yürütmeyi korur."},"facet_ids":["F002"],"text":"ona yönelik işi düzenlemeye koyulmak","usage_role":"explanatory"}],"definition":"Bir hedefe doğru yönelmek ve onu amaç edinmek; bağlama göre hedefe varmaya ya da onunla ilgili işi düzenlemeye koyulmak.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir hedefe yönelmek ve onu amaç edinmek yapının temel anlamıdır."},{"facet_id":"F002","role":"source_variant","statement":"Yöneliş bazı açıklamalarda hedefe erişme, bazılarında hedefle ilgili işi düzenleme olarak belirginleşir."}],"identity_rationale":"Kaynak anlatımı bir hedefe yönelme ve onu amaçlama yanında hedefe erişme ya da ona yönelik işi düzenleme yorumlarını da içerir; dal yalnız devinim başlangıcına indirgenemez.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"göğe yönelmek, ona varmak ya da ona yönelik işi düzenlemek"}],"lexicalization_note":"Tanım yalnız bir hedefe doğru yönelme bildiren yapıyı açıklar; bunu yalın kökün genel anlamı gibi sunmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yönelme dalı çekirdek örtüşmeyi ve odak dalın yapıya bağlı özel sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel amaçlama ve yaklaşma alanındadır; odak dal ise belirli bir dil yapısına bağlı olup hedefe erişme veya hedefle ilgili işi düzenleme yorumunu da taşır.","focus_only":"Odak dal belirli bir yönelme yapısına bağlıdır ve hedefe erişme ya da işi düzenleme yorumuna açılır.","gloss":"bir şeye yönelmek","neighbor_only":"Komşu dal, bir şeyi düşünceye alma, ona gelme ve onu amaçlama eylemlerini daha geniş biçimde kapsar.","neighbor_ref":"root_001230/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da belirli bir şeyi hedef seçip ona doğru yönelmeyi anlatır."}],"source_phrase_ar":"استوى إلى السماء أي قصد (sihah)؛ استوى علي وإلي يشاتمني على معنى أقبل إلي وعلي (tahdhib)؛ ثم استوى إلى بلد معناه قصد بالاستواء إليه (tahdhib)؛ إذا عدي بإلى اقتضى معنى الانتهاء إليه إما بالذات أو بالتدبير (mufradat)","source_summary":"Ortak çekirdek bir hedefe dönme ve onu amaç edinmedir; toplu kaynak anlatımı bu yönelişin hedefe varma veya hedefle ilgili işi yürütme biçiminde yorumlanabildiğini gösterir.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه استوى إلى الشيء بمعنى قصد أو أقبل أو انتهى إليه، وما قارب ذلك من صعود أو تدبير بحسب عبارة المصدر.","what_is_not_ar":"ليس هو العلو على شيء بحرف على، ولا سوى بمعنى غير، ولا مجرد مساواة."},"support_links":["sup_de61a071343d2648747b"]},{"boundary":"Dal insanın gençlik olgunluğuna erişmesiyle sınırlıdır; doğuştan düzgün yapı ya da hayvanın yaş basamağı değildir.","branch_kind":"bare","branch_ref":"root_000766/B005","candidate_links":[{"candidate_id":"cand_96796df5bfc5071e3f22","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:7:3:1","qac_word_ref":"91:7:3","surface_ar":"سَوَّىٰ"}],"gloss":"gençlik olgunluğuna erişmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanın gençlik dönemindeki gelişiminin tamamlanması temel anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu tamamlanma güç, beden yapısı ve kavrayışın olgunlaşmasıyla açıklanır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kırk yaş, olgunluğun kendisi değil, kaynak anlatımında verilen olası bir yaş sınırıdır."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir insanın gençlik gelişimini tamamlayıp güç ve kavrayış bakımından olgunlaşmasını anlatır.","boundary_detail":"Dal insanın gençlik olgunluğuna erişmesiyle sınırlıdır; doğuştan düzgün yapı ya da hayvanın yaş basamağı değildir.","branch_image_ar":"بلوغ وتمام الشباب","concept_gloss":"gençlik olgunluğuna erişmek","contextual_glosses":[{"applicability":"Yaştan çok gençlik döneminin sona erip gelişimin tamamlanmasının vurgulandığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gençlik döneminin sonuna erişme ve gelişimin tamamlanması anlamını korur."},"facet_ids":["F001"],"text":"gençliği tamamlanmak","usage_role":"contextual"},{"applicability":"Olgunluğun bedensel güç ve kavrayış bakımından açılması gereken bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedensel güç ile kavrayışın birlikte olgunlaşması anlamını korur."},"facet_ids":["F002"],"text":"gücü ve kavrayışı olgunlaşmak","usage_role":"explanatory"}],"definition":"Bir insanın gençliğinin sonuna erişerek bedensel gücünün, yapısının ve kavrayışının olgunlaşıp tamamlanması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanın gençlik dönemindeki gelişiminin tamamlanması temel anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Bu tamamlanma güç, beden yapısı ve kavrayışın olgunlaşmasıyla açıklanır."},{"facet_id":"F003","role":"source_variant","statement":"Kırk yaş, olgunluğun kendisi değil, kaynak anlatımında verilen olası bir yaş sınırıdır."}],"identity_rationale":"Kaynak anlatımı insanın gençliğinin tamamlanmasını, gücünün ve kavrayışının olgunlaşmasını bu dalda toplar; belirli bir yaş yalnız olası bir sınır açıklamasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"gençliğinin sonuna erişip gücü ve kavrayışı olgunlaşmak"}],"lexicalization_note":"Tanım yalın dalın insan gençliğinin tamamlanması anlamını verir ve başka dallardaki özel yapılardan anlam aktarmaz.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; seçilen komşu olgunlaşma alanını paylaşır, ancak insan ile hayvan ve gelişim ölçüsü ayrımını açık tutar.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal insan gençliğinin bedensel ve kavrayışsal tamamlanmasıdır; komşu dal ise hayvanlara özgü yaş sınıflarını ve yetişkinlik ölçülerini anlatır.","focus_only":"Odak dal insanın gençliğinin, gücünün ve kavrayışının tamamlanmasını anlatır.","gloss":"yaşça olgunlaşma","neighbor_only":"Komşu dal hayvanın belirli yaş basamaklarına erişmesini ve özellikle atın yaşça olgunlaşmasını anlatır.","neighbor_ref":"root_000517/B004","relation_type":"same_field","shared_zone":"İki dal da canlı bir varlığın gelişim sürecinde olgunluk sınırına erişmesiyle ilgilidir."}],"source_phrase_ar":"استوى الرجل إذا انتهى شبابه (sihah)؛ بلغ أشده واستوى قيل بلغ الأربعين (tahdhib)؛ المستوي هو الذي تم شبابه (tahdhib)؛ فإذا استويت أنت (mufradat)","source_summary":"Kaynak anlatımının ortak yönü insanın gençliğinin ve gücünün tamamlanmasıdır; kırk yaş açıklaması çekirdeği değiştiren zorunlu bir koşul değil, olgunluğun sınırına ilişkin bir yorumdur.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه استوى الرجل إذا انتهى شبابه أو تمت قوته وخلقه وعقله، وما قيل في بلوغ الأشد أو الأربعين.","what_is_not_ar":"ليس هو صحة الخلقة ابتداء، ولا استواء الدابة، ولا التسوية بين شيئين."},"support_links":["sup_2f4d9b3d80971f6ff8fe"]},{"boundary":"Dal yer ve tutum bakımından ortalık ile yansızlığı kapsar; iki nesnenin yalnız ölçü bakımından eşit olması değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000766/B006","candidate_links":[{"candidate_id":"cand_4179c04160b9c40cdde6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:7:3:1","qac_word_ref":"91:7:3","surface_ar":"سَوَّىٰ"}],"gloss":"iki yanın ortasında ve ikisine karşı yansız olma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bütünün ya da yerin iki uç arasında kalan orta bölümü somut çekirdektir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ortalık ilişkisi, taraflara eşit davranan yansız ve hak gözetir tutuma genişler."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli yer kullanımında iki yana denk, ortada ve herkesçe bilinen buluşma yeri anlatılır."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Somut orta konumu ve bu konumdan gelişen iki tarafa eşit, hak gözetir tutumu birlikte anlatır.","boundary_detail":"Dal yer ve tutum bakımından ortalık ile yansızlığı kapsar; iki nesnenin yalnız ölçü bakımından eşit olması değildir.","branch_image_ar":"وسط وعدل ومكان منصف","concept_gloss":"iki yanın ortasında ve ikisine karşı yansız olma","contextual_glosses":[{"applicability":"Bir yerin ya da bütünün iki uç arasında kalan orta bölümünü gösteren bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bütünün iki ucu arasında kalan somut orta konumu korur."},"facet_ids":["F001"],"text":"tam ortasında","usage_role":"contextual"},{"applicability":"Taraflar arasında hak gözeten bir yer, söz ya da tutumun anlatıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taraflara denk uzaklığı, yansızlığı ve hak gözetme niteliğini korur."},"facet_ids":["F002","F003"],"text":"iki tarafa da eşit ve yansız","usage_role":"contextual"}],"definition":"Bir şeyin iki uç ya da yan arasında ortada bulunması; yer veya tutumun taraflara eşit uzaklıkta, yansız ve hak gözetir olması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bütünün ya da yerin iki uç arasında kalan orta bölümü somut çekirdektir."},{"facet_id":"F002","role":"extension","statement":"Ortalık ilişkisi, taraflara eşit davranan yansız ve hak gözetir tutuma genişler."},{"facet_id":"F003","role":"specialization","statement":"Belirli yer kullanımında iki yana denk, ortada ve herkesçe bilinen buluşma yeri anlatılır."}],"identity_rationale":"Kaynak anlatımı somut orta konumu, iki yana eşit ve herkesçe bilinen yeri, ayrıca hak gözeten ortak tutumu aynı dalda verir; bunlar tek bir belirsiz orta sözüne indirgenmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"orta; iki yana eşit ve yansız durum"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"iki yana eşit, ortada ve herkesçe bilinen yer"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"iki tarafın da hakkını gözeten ortak söz"}],"lexicalization_note":"Tanım yalın orta ve yansızlık anlamlarını ayırır; yer ve söz bildiren özel yapıların koşullarını bütün dala yaymaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; seçilen komşu orta ile hak gözetme bağını paylaşırken somut yer ve ölçülü davranış kapsamlarını ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal somut orta ve iki tarafa denk yer anlamını korur; komşu dal ise ölçülülük ve seçkinlik değerlendirmesine daha geniş biçimde uzanır.","focus_only":"Odak dal somut bir yerin ortasını ve taraflara eşit uzaklıktaki belirli yeri de anlatır.","gloss":"ölçülü ve hak gözetir orta","neighbor_only":"Komşu dal ölçülülüğü, aşırılıklardan kaçınmayı ve bir topluluğun en seçkin üyelerini de anlatır.","neighbor_ref":"root_001646/B001","relation_type":"near_synonym","shared_zone":"İki dal da uçlardan uzak orta konumu hak gözetme ve yansızlıkla ilişkilendirir."}],"source_phrase_ar":"السواء ممدود وسط كل شيء (ayn)؛ مكانا سوى أي معلما قد علم القوم به (ayn;maqayis)؛ مكان سوى أي عدل ووسط (sihah)؛ السواء وسط الدار وغيرها (maqayis)؛ سواء بمعنى العدل والنصفة (tahdhib)؛ كلمة سواء أي عدل (tahdhib;mufradat)؛ في سواء الجحيم (maqayis;mufradat)","source_summary":"Kaynaklar somut ortayı temel alır ve bu ilişkiyi iki taraf arasında yansız, hak gözetir konuma taşır; yer ve ortak söz kullanımları bu iki yönün belirli bağlamlardaki biçimleridir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه السواء وسط الشيء أو الدار، وسواء السبيل، وكلمة سواء، وعلى سواء، ومكان سوى بمعنى وسط أو عدل أو منصف أو مستو معلوم.","what_is_not_ar":"ليس هو المثلية بين شيئين من جهة المقدار فقط، ولا سوى بمعنى غير، ولا الفضاء الواسع المسمى السي."},"support_links":["sup_051b15c553e5f0bf5c7a"]},{"boundary":"Dal başkalık ve ayrılık bildirir; orta konum, eşitlik ya da aynı şeyin kendisi olma anlamlarını kapsamaz.","branch_kind":"bare","branch_ref":"root_000766/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:7:3:1","qac_word_ref":"91:7:3","surface_ar":"سَوَّىٰ"}],"gloss":"başka ve ayrı olan","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığın söz konusu varlıkla aynı olmayıp ondan başka olması temel anlamdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başkalık, bazı bağlamlarda birinin yerinde bulunan ya da onun yerine geçen ötekiyi gösterir."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi ya da şeyin söz konusu olandan farklı olduğunu veya onun yerine geçen öteki olduğunu anlatır.","boundary_detail":"Dal başkalık ve ayrılık bildirir; orta konum, eşitlik ya da aynı şeyin kendisi olma anlamlarını kapsamaz.","branch_image_ar":"مباينة وكون الشيء غيره","concept_gloss":"başka ve ayrı olan","contextual_glosses":[{"applicability":"Bir varlığı belirtilen kişi ya da şeyin dışında tutan kısa kullanımlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirtilen varlıkla aynı olmama ve onun dışında kalma anlamını korur."},"facet_ids":["F001"],"text":"ondan başka","usage_role":"contextual"},{"applicability":"Bir kişinin yerinde bulunan ya da onun yerine düşünülen başka kişiyi anlatırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başkalığı ve belirtilen kişinin yerini tutma ilişkisini korur."},"facet_ids":["F002"],"text":"onun yerine bir başkası","usage_role":"contextual"}],"definition":"Bir kişi ya da şeyin söz konusu olandan başka, ayrı veya onun yerini tutan bir öteki olması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığın söz konusu varlıkla aynı olmayıp ondan başka olması temel anlamdır."},{"facet_id":"F002","role":"extension","statement":"Başkalık, bazı bağlamlarda birinin yerinde bulunan ya da onun yerine geçen ötekiyi gösterir."}],"identity_rationale":"Kaynak anlatımı temel olarak bir şeyin ötekinden başka ve ayrı olmasını verir; birinin yerinde ya da onun yerine bulunma açıklaması bu başkalığın bağlamsal görünümüdür.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"başka, öteki"}],"lexicalization_note":"Tanım yalın başkalık anlamıyla sınırlıdır ve örneklerdeki yerine geçme yorumunu zorunlu çekirdek yapmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; seçilen komşu yalın başkalıkla en güçlü örtüşmeyi gösterir ve dilbilgisel genişlemeleriyle ayrılır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalın başkalık ve yerine bulunma ilişkisine bağlıdır; komşu dal ise başkalığı karşıtlık, dışarıda bırakma ve olumsuzlama görevlerine kadar genişletir.","focus_only":"Odak dal bir başkasının yerinde ya da yerine bulunan öteki yorumunu da taşır.","gloss":"başkalık ve dışarıda bırakma","neighbor_only":"Komşu dal başkalık yanında karşıtlık, dışarıda bırakma, olumsuzlama ve dilbilgisel görevleri de kapsar.","neighbor_ref":"root_001119/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişi ya da şeyin söz konusu olandan başka olduğunu bildirir."}],"source_phrase_ar":"سوى مقصور إذا كان في موضع غير (ayn)؛ سواء الشيء غيره (sihah;tahdhib)؛ مررت برجل سواك أي غيرك (sihah)؛ هذا سوى ذلك أي غيره (maqayis)؛ يستعمل سوى وسواء بمعنى غير (mufradat)؛ عندي رجل سواك أي مكانك وبدلك (mufradat)","source_summary":"Kaynakların ortak çekirdeği aynılık dışındaki başkalık ve ayrılıktır; yer veya yerini tutma açıklaması bu başkalığın belirli bir kişiyle kurulan ilişkide aldığı biçimdir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه سوى وسواء بمعنى غير، والبدل أو المكان المنفصل عن المخاطب في نحو عندي رجل سواك.","what_is_not_ar":"ليس هو السواء بمعنى الوسط أو العدل، ولا سوى بمعنى نفس الشيء في النقل المختلف."},"support_links":[]},{"boundary":"Dal yalnız verilen söz yapısında yön ve hedef bildirir; genel başkalık ya da bağımsız amaçlama anlamı değildir.","branch_kind":"collocation","branch_ref":"root_000766/B008","candidate_links":[{"candidate_id":"cand_74b25835ef8bf1766191","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:7:3:1","qac_word_ref":"91:7:3","surface_ar":"سَوَّىٰ"}],"gloss":"birinin yöneldiği hedefe yönelmek","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin kendisini değil, onun tuttuğu yönü veya amaçladığı hedefi izlemek temel ilişkidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sözün ya da övgünün belirli bir kişiye çevrilmesi, yönelme ilişkisinin söylem alanındaki kullanımıdır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Atışın iki hedefin bulunduğu yönü tutturamaması, doğrultunun hedefle ilişkisini gösterir."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız belirli söz yapısı içinde bir kişinin yönünü ya da hedefini izlemeyi anlatan kullanımlara uygundur.","boundary_detail":"Dal yalnız verilen söz yapısında yön ve hedef bildirir; genel başkalık ya da bağımsız amaçlama anlamı değildir.","branch_image_ar":"قصد نحو شخص أو جهة","concept_gloss":"birinin yöneldiği hedefe yönelmek","contextual_glosses":[{"applicability":"Bir kişinin seçtiği doğrultunun izlenmesi veya onun hedefinin hedeflenmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin tuttuğu doğrultuyu ve aynı yöne dönme eylemini korur."},"facet_ids":["F001"],"text":"onun tuttuğu yöne yönelmek","usage_role":"contextual"},{"applicability":"Bir sözün ya da övgünün belirli bir kişiye çevrilmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Söylemin yönünü belirli kişiye çevirme ilişkisini korur."},"facet_ids":["F002"],"text":"övgüyü ona yöneltmek","usage_role":"contextual"}],"definition":"Belirli söz yapısı içinde bir kişinin yöneldiği hedefe ya da doğrultuya yönelmek; sözü veya övgüyü o doğrultudaki kişiye çevirmek.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin kendisini değil, onun tuttuğu yönü veya amaçladığı hedefi izlemek temel ilişkidir."},{"facet_id":"F002","role":"associated_use","statement":"Sözün ya da övgünün belirli bir kişiye çevrilmesi, yönelme ilişkisinin söylem alanındaki kullanımıdır."},{"facet_id":"F003","role":"example","statement":"Atışın iki hedefin bulunduğu yönü tutturamaması, doğrultunun hedefle ilişkisini gösterir."}],"identity_rationale":"Kaynak deyim belirli bir kişiyi doğrudan hedeflemekten çok onun yöneldiği yöne ya da hedefe yönelmeyi anlatır; övgünün birine çevrilmesi ve hedefi ıskalama örneği de yön doğrultusunu öne çıkarır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"birinin tuttuğu yöne ya da hedefe yönelmek"}],"lexicalization_note":"Tanım belirli söz yapısına bağlı yönelme anlamını korur ve bunu yalın biçime ait genel bir anlam olarak sunmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen komşu hedefe yönelme çekirdeğini paylaşır ve odak dalın kişi üzerinden kurulan yapısal sınırını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel ve doğrudan amaçlamayı anlatır; odak dal ise başka birinin yönünü izleyen, belirli söz yapısına bağlı dolaylı yöneliştir.","focus_only":"Odak dal yalnız belirli bir söz yapısında başka bir kişinin tuttuğu yönü ya da hedefi izler.","gloss":"amaçlayıp hedefe yönelmek","neighbor_only":"Komşu dal genel amaçlama, bilinçli yönelme ve ok ya da mızrağı doğrudan hedefe çevirme eylemlerini kapsar.","neighbor_ref":"root_000053/B012","relation_type":"near_synonym","shared_zone":"İki dal da bir hedef seçme ve hareketi ya da dikkati o hedefe çevirme alanında buluşur."}],"source_phrase_ar":"يقال قصدت سوى فلان كما يقال قصدت قصده (maqayis)؛ قصدت سوى فلان أي قصدت قصده (sihah)؛ فلأصرفن سوى حذيفة مدحتى (maqayis;sihah)؛ وقع المزار على سواهما أخطأهما (tahdhib)","source_summary":"Kaynak anlatımı birinin tuttuğu yönü hedef alma çekirdeğinde birleşir; övgünün o yana çevrilmesi ve atışın hedefleri ıskalaması bu yön ilişkisinin farklı bağlamlarıdır.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه قصدت سوى فلان بمعنى قصدت قصده، وصرف الكلام أو المدح نحو شخص.","what_is_not_ar":"ليس هو سوى بمعنى غير، ولا استوى إلى السماء بالتركيب الفعلي، ولا المساواة."},"support_links":["sup_de61a071343d2648747b"]},{"boundary":"Dal açık ve geniş yer ile buna bağlı bolluğu anlatır; eş, orta ya da deve sırtlığı anlamlarından ayrıdır.","branch_kind":"bare","branch_ref":"root_000766/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:7:3:1","qac_word_ref":"91:7:3","surface_ar":"سَوَّىٰ"}],"gloss":"geniş ve açık arazi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ufku açık, geniş bir arazi parçası dalın temel yer anlamıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir anlatım bu geniş yeri özellikle bozkırdaki pürüzsüz bir alan olarak sınırlar."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Arazinin genişliği, otlağın veya suyun çok ve yaygın oluşunu anlatmaya genişler."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Geniş, açık ve kimi bağlamlarda pürüzsüz bir bozkır yerini anlatan yalın yer adı için uygundur.","boundary_detail":"Dal açık ve geniş yer ile buna bağlı bolluğu anlatır; eş, orta ya da deve sırtlığı anlamlarından ayrıdır.","branch_image_ar":"السِيّ واسع أملس من الأرض","concept_gloss":"geniş ve açık arazi","contextual_glosses":[{"applicability":"Arazinin hem genişliği hem de bozkır içindeki pürüzsüz yüzeyi öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Genişliği, açıklığı, bozkır bağlamını ve pürüzsüz yüzey niteliğini korur."},"facet_ids":["F001","F002"],"text":"geniş, düz ve açık bozkır yeri","usage_role":"contextual"},{"applicability":"Otlak ya da suyun geniş alana yayılan çokluğunu anlatan uzantı kullanımında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mekânsal genişliğin ot veya su bolluğuna taşınan uzantısını korur."},"facet_ids":["F003"],"text":"bol ve yaygın","usage_role":"contextual"}],"definition":"Geniş, açık ve yer yer pürüzsüz bir arazi ya da bozkır yeri; buradaki mekânsal genişlikten hareketle ot veya suyun bol ve yaygın oluşu.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ufku açık, geniş bir arazi parçası dalın temel yer anlamıdır."},{"facet_id":"F002","role":"source_variant","statement":"Bir anlatım bu geniş yeri özellikle bozkırdaki pürüzsüz bir alan olarak sınırlar."},{"facet_id":"F003","role":"extension","statement":"Arazinin genişliği, otlağın veya suyun çok ve yaygın oluşunu anlatmaya genişler."}],"identity_rationale":"Kaynak anlatımı geniş açık araziyi temel alır, fakat bir aktarımda bozkırdaki pürüzsüz yer öne çıkar; otlak ve su için kullanılan bolluk anlatımı ise bu mekânsal genişliğin uzantısıdır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"geniş, açık ya da pürüzsüz arazi"}],"lexicalization_note":"Tanım yalın arazi adını temel alır ve otlak ile suya ilişkin bolluk kullanımını ona bağlı bir genişleme olarak tutar.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; seçilen komşu açık arazi çekirdeğini paylaşır ve bozkır, pürüzsüzlük ile bolluk sınırlarını görünür kılar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal geniş bozkır ve pürüzsüz arazi çevresinde toplanıp bolluğa uzanır; komşu dal ise farklı türden çıplak ve açık yerleri daha geniş bir adlandırma alanında toplar.","focus_only":"Odak dal pürüzsüz bozkır yerini ve ot ile suyun bol oluşuna uzanan kullanımı içerir.","gloss":"örtüsüz açık alan","neighbor_only":"Komşu dal boş yer, avlu, yüzey, yan ve örtüsüz alan gibi daha çeşitli açık yer türlerini kapsar.","neighbor_ref":"root_001005/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da üstü örtülü olmayan, açık ve geniş bir kara parçasını anlatabilir."}],"source_phrase_ar":"السِيّ الفضاء من الأرض الواسع (jamhara)؛ ومن الباب السِيّ الفضاء من الأرض (maqayis)؛ السِيّ موضع بالبادية أملس (ayn)؛ نزلنا في كلاء سِيّ وأنبط ماء سِيًّا أي كثيرا واسعا (tahdhib)","source_summary":"Kaynak anlatımında geniş açık arazi ortak çekirdektir; pürüzsüz bozkır yeri bunun daha dar betimlemesi, ot ve su bolluğu ise genişlik düşüncesinin nitelik alanına taşınmasıdır.","sources":["AY","JA","TA","MQ"],"what_is_ar":"يدخل فيه السِيّ بمعنى الفضاء الواسع من الأرض أو الموضع الأملس، وما وصف من كلأ أو ماء بالسعة والكثرة.","what_is_not_ar":"ليس هو السِيّ بمعنى المثل، ولا السَّويّة التي تلقى على البعير، ولا السواء وسط الشيء."},"support_links":[]},{"boundary":"Dal deve sırtında binmek için kullanılan nesneye özgüdür; eşitleme, açık arazi ya da yay parçası anlamı değildir.","branch_kind":"bare","branch_ref":"root_000766/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:7:3:1","qac_word_ref":"91:7:3","surface_ar":"سَوَّىٰ"}],"gloss":"devenin sırtına konan dolgulu binme örtüsü","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne devenin sırtına yerleştirilir ve binicinin oturmasına ya da binmesine yarar."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynak anlatımları nesneyi sırtlık, sarılı örtü veya bitki sapı ve lifle doldurulmuş örtü biçimlerinde betimler."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Örtü biçimi devenin hörgücünün çevresini sararak binici için oturma yeri oluşturur."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Devenin sırtı ya da hörgücü çevresinde binicinin oturmasını sağlayan örtü veya sırtlık türü araç için kullanılır.","boundary_detail":"Dal deve sırtında binmek için kullanılan nesneye özgüdür; eşitleme, açık arazi ya da yay parçası anlamı değildir.","branch_image_ar":"السَّويّة على ظهر البعير","concept_gloss":"devenin sırtına konan dolgulu binme örtüsü","contextual_glosses":[{"applicability":"Nesnenin örtü yapısından çok deve üzerinde binmeye yarayan sırtlık oluşu öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sarılı veya içi bitki sapı ve lifle doldurulmuş örtü biçimi belirtilmez.","preserves":"Deve sırtındaki konumu ve biniciyi taşıyan araç olma işlevini korur."},"facet_ids":["F001"],"text":"deve sırtlığı","usage_role":"contextual"},{"applicability":"Aracın hörgüç çevresine sarılan ve biniciye oturma yeri sağlayan örtü biçimi anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hörgüç çevresindeki yerleşimi, örtü yapısını ve binme işlevini korur."},"facet_ids":["F001","F003"],"text":"hörgüç çevresine sarılan binme örtüsü","usage_role":"explanatory"}],"definition":"Devenin sırtına ya da hörgücünün çevresine konup binmeye yarayan, kimi biçimi sarılı veya dolgulu örtüye, kimi biçimi sırtlığa benzeyen araç.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne devenin sırtına yerleştirilir ve binicinin oturmasına ya da binmesine yarar."},{"facet_id":"F002","role":"source_variant","statement":"Kaynak anlatımları nesneyi sırtlık, sarılı örtü veya bitki sapı ve lifle doldurulmuş örtü biçimlerinde betimler."},{"facet_id":"F003","role":"specialization","statement":"Örtü biçimi devenin hörgücünün çevresini sararak binici için oturma yeri oluşturur."}],"identity_rationale":"Kaynak anlatımları aynı nesneyi kimi yerde deve için bir sırtlık, kimi yerde hörgüç çevresine sarılan ya da doldurulan örtü olarak açıklar; tanım bu yapım ve biçim çeşitliliğini korumalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"devenin sırtına ya da hörgücü çevresine konan binme örtüsü"}],"lexicalization_note":"Tanım yalın nesne adını verir ve kaynaklardaki sırtlık, dolgulu örtü ve hörgüç çevresi biçimlerini aynı araç altında toplar.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; seçilen komşu nesne ve işlev bakımından en yakın eşleşmedir, ancak daha büyük taşıma düzeneği kapsamıyla ayrılır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal deve sırtlığı ve dolgulu örtü biçiminde sınırlıdır; komşu dal buna ek olarak kapalı ya da sedye benzeri taşıma düzeneklerini de kapsar.","focus_only":"Odak dal deveye özgü sırtlık ya da dolgulu örtüyü ve hörgüç çevresindeki yerleşimini anlatır.","gloss":"biniciyi saran deve örtüsü","neighbor_only":"Komşu dal kadın için hazırlanan taşıma düzeneğini ve sedye benzeri daha büyük bir binme aracını da kapsar.","neighbor_ref":"root_000374/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da deve sırtında veya hörgüç çevresinde biniciyi taşıyan örtülü bir düzenek anlatabilir."}],"source_phrase_ar":"السَّويّة قتب أعجمي للبعير والجميع السوايا (ayn;tahdhib)؛ السَّويّة كساء يلف ويجعل شبيها بالحوية يلقى على سنام البعير (jamhara)؛ السَّويّة كساء محشو بثمام ونحوه كالبرذعة (sihah)؛ كساء محشو بثمام أو ليف يجعل على ظهر البعير (tahdhib)","source_summary":"Ortak işlev devenin sırtında binmeye yarayan bir araç olmaktır; toplu anlatım aracın sırtlık, sarılı örtü veya içi doldurulmuş örtü biçimlerinde tasarlanabildiğini gösterir.","sources":["AY","JA","SI","TA"],"what_is_ar":"يدخل فيه السَّويّة وهي كساء أو قتب أو برذعة تجعل على ظهر البعير أو حول سنامه للركوب.","what_is_not_ar":"ليس هو التسوية بمعنى التعديل، ولا السِيّ الفضاء، ولا سِيَة القوس أو الأسد."},"support_links":[]},{"boundary":"Bu dal bir öğeyi işlem dışında bırakmayı anlatır; düzeltme, eşitleme ya da orta konum bildirmez.","branch_kind":"bare","branch_ref":"root_000766/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:7:3:1","qac_word_ref":"91:7:3","surface_ar":"سَوَّىٰ"}],"gloss":"atlayıp dışarıda bırakmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir öğeyi izlenen işlem ya da sıra içine almadan atlamak temel eylemdir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Atlanan öğeyi bırakmak ve ona gereken ilgiyi göstermemek eylemin sonuç yönüdür."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir yazı bölümünü veya geçilen bir yeri atlamak, çekirdeğin belirli nesneler üzerindeki örneğidir."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir öğenin sıra, işlem veya anlatım içine alınmayarak bırakılması ve göz ardı edilmesi için uygundur.","boundary_detail":"Bu dal bir öğeyi işlem dışında bırakmayı anlatır; düzeltme, eşitleme ya da orta konum bildirmez.","branch_image_ar":"إسقاط وإغفال","concept_gloss":"atlayıp dışarıda bırakmak","contextual_glosses":[{"applicability":"Bir yazı ya da anlatımdaki parçanın okunmadan veya aktarılmadan geçilmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli bir bölümün sıra içinde işlenmeden geçilmesi anlamını korur."},"facet_ids":["F001","F003"],"text":"bir bölümü atlamak","usage_role":"contextual"},{"applicability":"Bir şeyin bilinçli ya da sonuç bakımından işlem dışında bırakıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öğeyi bırakma ve ona gereken ilgiyi göstermeme sonucunu korur."},"facet_ids":["F002"],"text":"bırakıp göz ardı etmek","usage_role":"contextual"}],"definition":"Bir şeyi izlenen sıra, işlem ya da anlatım içinde atlayarak dışarıda bırakma ve ona gereken ilgiyi göstermeme.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir öğeyi izlenen işlem ya da sıra içine almadan atlamak temel eylemdir."},{"facet_id":"F002","role":"extension","statement":"Atlanan öğeyi bırakmak ve ona gereken ilgiyi göstermemek eylemin sonuç yönüdür."},{"facet_id":"F003","role":"example","statement":"Bir yazı bölümünü veya geçilen bir yeri atlamak, çekirdeğin belirli nesneler üzerindeki örneğidir."}],"identity_rationale":"Kaynak anlatımı bir şeyi, yazıdaki bir bölümü ya da geçilen bir yeri atlama, bırakma ve göz ardı etme işlemini açıkça aynı çekirdekte birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"atlamak, dışarıda bırakmak ve göz ardı etmek"}],"lexicalization_note":"Tanım yalın bırakma ve atlama eylemini verir; örneklerdeki yazı parçasını bütün dal için zorunlu nesne saymaz.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; seçilen komşu bırakma alanını paylaşır ve odak dalın sıradan bir öğeyi atlama özelliğini en açık biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal seçili bir öğeyi atlama ve göz ardı etme işlemidir; komşu dal ise yetersizlikten doğan savsaklama, unutma ve yitirme sonuçlarına daha geniş biçimde uzanır.","focus_only":"Odak dal bir öğeyi sıra, işlem veya anlatım içinde atlayıp dışarıda bırakmayı öne çıkarır.","gloss":"savsaklayıp yitirme","neighbor_only":"Komşu dal yetersiz kalma, savsaklama, unutma, geride bırakma ve bütünüyle yitirme sonuçlarını da kapsar.","neighbor_ref":"root_001145/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeye gereken işlemi veya ilgiyi göstermeyerek onu bırakma alanında buluşur."}],"source_phrase_ar":"أسوى فلان حرفا من كتاب الله أي أسقط وأغفل (ayn)؛ أسويت الشيء أي تركته وأغفلته (sihah)؛ أسوى برزخا ثم رجع إليه (tahdhib)؛ أسوى يعني أسقط وأغفل (tahdhib)","source_summary":"Kaynaklar bir öğeyi sıradan düşürme, üzerinden geçme ve ilgisiz bırakma çekirdeğinde birleşir; yazı bölümü ile geçilen yer bu işlemin ayrı örnekleridir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه أسوى الشيء أو الحرف إذا أسقطه أو تركه وأغفله.","what_is_not_ar":"ليس هو التسوية ولا الاستواء ولا السواء بمعنى العدل."},"support_links":[]},{"boundary":"Dal yalnız ayın on üçüncü gecesinin adıdır; yer ortası, yansızlık ya da genel ay ışığı anlamı değildir.","branch_kind":"bare","branch_ref":"root_000766/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:7:3:1","qac_word_ref":"91:7:3","surface_ar":"سَوَّىٰ"}],"gloss":"ayın on üçüncü gecesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Adlandırılan zaman ayın on üçüncü gecesidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gece adı, ayın o sırada dengeli bir görünüme erişmesi açıklamasıyla ilişkilendirilir."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ayın dengeli göründüğü kabul edilen belirli geceyi takvim içindeki sırasıyla adlandırmak için kullanılır.","boundary_detail":"Dal yalnız ayın on üçüncü gecesinin adıdır; yer ortası, yansızlık ya da genel ay ışığı anlamı değildir.","branch_image_ar":"ليلة استواء القمر","concept_gloss":"ayın on üçüncü gecesi","contextual_glosses":[{"applicability":"Gece adının hem takvimdeki sırası hem de ayın görünümüyle bağı açıklanmak istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"On üçüncü geceyi ve adlandırmanın ayın dengeli görünümüyle kurulan bağını korur."},"facet_ids":["F001","F002"],"text":"ayın dengelendiği on üçüncü gece","usage_role":"explanatory"}],"definition":"Ayın görünümünün dengelendiği kabul edilen, ayın on üçüncü gecesine verilen ad.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Adlandırılan zaman ayın on üçüncü gecesidir."},{"facet_id":"F002","role":"associated_use","statement":"Gece adı, ayın o sırada dengeli bir görünüme erişmesi açıklamasıyla ilişkilendirilir."}],"identity_rationale":"Kaynak anlatımı bu gece adını ayın on üçüncü gecesi olarak belirler ve adlandırmayı ayın o sıradaki dengeli görünümüne bağlar.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"ayın dengeli göründüğü on üçüncü gece"}],"lexicalization_note":"Tanım gece adını kendi başına verir ve başka dallardaki orta, eşitlik veya düzgünlük anlamlarını ona taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen komşu aynı gök ve gece alanını paylaşır, ancak belirli gece adıyla genel ay ve ışık anlamını açıkça ayırır.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Odak dal yalnız takvimde belirli bir geceyi adlandırır; komşu dal ise ayın kendisini, ışığını ve aydınlattığı geceleri tarih sırasından bağımsız biçimde kapsar.","focus_only":"Odak dal ay içindeki belirli bir sıraya, on üçüncü geceye verilen addır.","gloss":"ay ve ay ışığı","neighbor_only":"Komşu dal gökteki ayı, onun ışığını ve ay ışığıyla aydınlanan geceleri genel olarak anlatır.","neighbor_ref":"root_001255/B001","relation_type":"thematic","shared_zone":"Her iki dal ayın gece göğündeki görünümü ve aydınlığı çevresindeki aynı zaman alanına bağlıdır."}],"source_phrase_ar":"ليلة السواء ليلة ثلاث عشرة (sihah)؛ السواء ممدود ليلة ثلاث عشرة وفيها يستوي القمر (tahdhib)","source_summary":"Kaynaklar ayın on üçüncü gecesini aynı adla belirler; bunlardan biri adın ayın o gecedeki dengeli görünümüne dayandığını ayrıca açıklar.","sources":["SI","TA"],"what_is_ar":"يدخل فيه ليلة السواء، وهي ليلة ثلاث عشرة عند استواء القمر في النقلين.","what_is_not_ar":"ليس هو السواء بمعنى العدل أو الوسط في المكان."},"support_links":[]},{"boundary":"Dal yalnız baş ölçüsü çevresinde kurulan söz kalıbına bağlıdır; genel eşitlik, para adı ya da herhangi bir mal miktarı değildir.","branch_kind":"collocation","branch_ref":"root_000766/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:7:3:1","qac_word_ref":"91:7:3","surface_ar":"سَوَّىٰ"}],"gloss":"başına denk mal ve bolluk","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Mal miktarı kişinin başına denk sayılan bir ölçüyle anlatılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Baş ölçüsüne denk mal düşüncesi, kişinin bolluk ve iyi yaşam içinde bulunmasını anlatmaya genişler."}}],"root_ar":"س و ي","root_id":"root_000766","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız baş ölçüsü çevresinde kurulan kalıp içinde mal miktarını veya kişinin bolluk içindeki durumunu anlatır.","boundary_detail":"Dal yalnız baş ölçüsü çevresinde kurulan söz kalıbına bağlıdır; genel eşitlik, para adı ya da herhangi bir mal miktarı değildir.","branch_image_ar":"سِيّ الرأس وقدر يوازي الرأس من مال أو نعمة","concept_gloss":"başına denk mal ve bolluk","contextual_glosses":[{"applicability":"Kalıbın bir kişinin başına denk sayılan mal miktarını bildirdiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin başını ölçü alan denkliği ve bunun mal miktarı oluşunu korur."},"facet_ids":["F001"],"text":"başı ölçüsünde mal","usage_role":"explanatory"},{"applicability":"Aynı söz kalıbının mal ölçüsünden çok kişinin iyi ve bol durumunu anlattığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kalıbın kişiye bağlanan bolluk ve iyi yaşam durumunu korur."},"facet_ids":["F002"],"text":"bolluk içinde olmak","usage_role":"contextual"}],"definition":"Belirli söz kalıbında bir kişinin başına denk ya da onu karşılar sayılan mal miktarı; aynı kalıpta kişinin içinde bulunduğu bolluk ve iyi yaşam durumu.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Mal miktarı kişinin başına denk sayılan bir ölçüyle anlatılır."},{"facet_id":"F002","role":"extension","statement":"Baş ölçüsüne denk mal düşüncesi, kişinin bolluk ve iyi yaşam içinde bulunmasını anlatmaya genişler."}],"identity_rationale":"Kaynak anlatımı sabit söz içinde bir kişinin başına denk sayılan mal miktarını verir, fakat aynı kalıp bolluk veya iyi yaşam durumu için de kullanılır; tanım iki görünümü ayırmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"başına denk sayılan mal miktarı ya da bolluk"}],"lexicalization_note":"Tanım yalnız baş ölçüsünü kullanan kalıba bağlanır ve buradaki mal ile bolluk anlamını yalın biçime genellemez.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; kökün genel denklik dalı ölçü ilişkisini açıklar ve bu dalın yalnız belirli söz kalıbına bağlı olduğunu gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel ve üretken denklik alanıdır; odak dal ise yalnız başı ölçü alan kalıpla mal ve bolluk anlatan özel bir kullanımdır.","focus_only":"Odak dal baş ölçüsüne bağlı sabit söz içinde mal miktarını ve bolluk durumunu anlatır.","gloss":"iki şey arasında denklik","neighbor_only":"Komşu dal iki şey arasındaki genel ölçü, değer, nicelik veya nitelik denkliğini ve eşlik kalıplarını kapsar.","neighbor_ref":"root_000766/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir miktarın seçilen ölçüyü karşılaması ve ona denk sayılması ilişkisi vardır."}],"source_phrase_ar":"جاء فلان بسِيّ رأسه من المال أي ما يوازي رأسه (jamhara)؛ وقع فلان في سواء رأسه أي فيما ساوى رأسه من النعمة (tahdhib)؛ هو في سِيّ رأسه وسواء رأسه وهي النعمة (tahdhib)","source_summary":"Kaynak anlatımı başa denk sayılan mal ölçüsü ile bu ölçünün bolluk ve iyi yaşam durumu bildiren kullanımını aynı söz kalıbında birleştirir.","sources":["JA","TA"],"what_is_ar":"يدخل فيه قولهم بسِيّ رأسه أو في سواء رأسه لما يوازي رأسه من مال أو نعمة.","what_is_not_ar":"ليس هو السِيّ بمعنى الفضاء، ولا السِيّ بمعنى المثل المطلق، ولا سواء الشيء بمعنى وسطه."},"support_links":[]},{"boundary":"Anlam, canlı solunumuyla sınırlıdır; can, kan, öz varlık ya da sıkıntı giderme anlamlarını içermez.","branch_kind":"bare","branch_ref":"root_001533/B001","candidate_links":[{"candidate_id":"cand_b0ce2b6cc5181e104841","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:7:1:2","qac_word_ref":"91:7:1","surface_ar":"نَفْسٍ"}],"gloss":"soluk alıp verme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Havanın ağız ya da burun yoluyla gövdeye girip yeniden çıkmasıdır."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İçme sırasında verilen her ara soluk, aynı solunum döngüsünün sayılan bir örneğidir."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Canlının havayı içine alıp dışarı verdiği temel bedensel süreç için kullanılır.","boundary_detail":"Anlam, canlı solunumuyla sınırlıdır; can, kan, öz varlık ya da sıkıntı giderme anlamlarını içermez.","branch_image_ar":"خروج النسيم من الجوف","concept_gloss":"soluk alıp verme","contextual_glosses":[{"applicability":"Solunumun ya da içme sırasında verilen aranın tek bir döngü olarak sayıldığı yerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tek bir giriş-çıkış döngüsünün sayılabilirliğini korur."},"facet_ids":["F002"],"text":"bir soluk","usage_role":"contextual"}],"definition":"Akciğerli bir canlının havayı ağız ya da burun yoluyla gövdesine alıp yeniden dışarı vermesidir. Her bir giriş-çıkış döngüsü ayrı bir soluk olarak sayılabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Havanın ağız ya da burun yoluyla gövdeye girip yeniden çıkmasıdır."},{"facet_id":"F002","role":"example","statement":"İçme sırasında verilen her ara soluk, aynı solunum döngüsünün sayılan bir örneğidir."}],"identity_rationale":"Kaynak ifadesi, akciğerli bir canlının gövdesine havanın girip çıkmasını ve bu döngünün tek tek sayılabilmesini doğrudan anlatır. İçme sırasında sayılan soluklar da bu bedensel sürecin özel bir bağlamıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"soluk alıp verme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"gövdeye girip çıkan hava; soluk"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"tek soluk ya da soluklanma arası"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"soluklar"}],"lexicalization_note":"Çıplak dal, soluk alıp verme sürecini bildirir; içme bağlamı yalnızca bu sürecin sayıldığı bir kullanımdır.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı; soluk verme odağındaki bu komşu, temel sınırı en açık biçimde gösterdiği için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hava alma ile vermeyi birlikte içeren genel solunumdur; komşu ise özellikle güçlü dışa verişi ve doğan sesi anlatır.","focus_only":"Odak dal, sessiz ve olağan hava girişini de kapsayan tam solunum döngüsüdür.","gloss":"soluk verme ve ses çıkarma","neighbor_only":"Komşu dal, göğüsten havayı dışarı vermeye, buna eşlik eden sese ve sıkıntı belirtisine ağırlık verir.","neighbor_ref":"root_000634/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da gövdedeki havanın dışarı çıkması bulunur."}],"source_phrase_ar":"التنفس خروج النسيم من الجوف (maqayis;ayn); النفس واحد الأنفاس وكل ذي رئة متنفس (sihah); التنفس في الإناء وثلاثة أنفاس (tahdhib); النفس الريح الداخل والخارج في البدن من الفم والمنخر (mufradat)","source_summary":"Kaynaklar, temel anlamı havanın canlı gövdesine girip çıkması ve bu hareketin tekil döngüler hâlinde sayılması olarak ortaklaştırır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه التنفس والأنفاس وخروج الريح من الجوف أو الفم والمنخر، وما يلحق به من نفس الشرب إذا كان المراد به نفسا في الشرب.","what_is_not_ar":"ليس هو الروح أو الذات أو الدم ولا التفريج عن الكربة إلا من جهة المجاز."},"support_links":["sup_7476908a9241241c8779"]},{"boundary":"Dal, önceden var olan bir sıkıntının giderilmesini gerektirir; genel genişlik, süre ya da bedensel solunum değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B002","candidate_links":[{"candidate_id":"cand_b0ce2b6cc5181e104841","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:7:1:2","qac_word_ref":"91:7:1","surface_ar":"نَفْسٍ"}],"gloss":"sıkıntıyı hafifletip ferahlatma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sıkıntı içindeki kişinin yükünü hafifletip onu rahatlatma eylemidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Esinti veya yardım, sıkıntıdakine ferahlık getiren araç olarak adlandırılabilir."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin içinde bulunduğu darlık ya da ağır durum etkin biçimde azaltıldığında uygundur.","boundary_detail":"Dal, önceden var olan bir sıkıntının giderilmesini gerektirir; genel genişlik, süre ya da bedensel solunum değildir.","branch_image_ar":"توسيع الكربة بالتنفيس","concept_gloss":"sıkıntıyı hafifletip ferahlatma","contextual_glosses":[{"applicability":"Esinti veya yardım, sıkıntıdaki kişiyi rahatlatan araç olarak anıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aracın sıkıntıyı gideren işlevini açıkça korur."},"facet_ids":["F002"],"text":"ferahlık getiren esinti ya da yardım","usage_role":"explanatory"}],"definition":"Sıkıntı içindeki birinin üzerindeki baskıyı azaltıp ona rahatlama sağlamaktır. Esinti ya da yardım, bu rahatlamayı sağladığı ölçüde aynı anlam alanına girer.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sıkıntı içindeki kişinin yükünü hafifletip onu rahatlatma eylemidir."},{"facet_id":"F002","role":"associated_use","statement":"Esinti veya yardım, sıkıntıdakine ferahlık getiren araç olarak adlandırılabilir."}],"identity_rationale":"Kaynak ifadesi, sıkıntı içindeki kişinin yükünü hafifletme ve ona ferahlık sağlama eylemini açıkça kurar. Esinti ya da yardım da ancak bu rahatlatıcı işlev bakımından dala girer.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"Tanrı onun sıkıntısını giderdi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"beni sıkıntıdan kurtarıp rahatlat"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"Tanrı'nın sıkıntıdakilere ferahlık getiren esintisi ya da yardımı"}],"lexicalization_note":"Eylem kalıpları sıkıntıyı giderme işini, ayrı bir kullanım ise esinti ya da yardımı bu işin aracı olarak anlatır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sıkıntının giderilmesiyle doğan rahatlama sınırını en iyi açıklayan yakın anlamlı komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak, bir sıkıntıyı giderip kişiye ferahlık verme eylemidir; komşu, bu etkinin sonucu olan çözülme ve kurtulma durumuna daha çok ağırlık verir.","focus_only":"Odak dal, sıkıntıyı etkin biçimde hafifleten kişi, güç ya da aracı öne çıkarır.","gloss":"üzüntü ve sıkıntının çözülmesi","neighbor_only":"Komşu dal, üzüntü ve kaygının çözülüp ortadan kalkması sonucunu daha geniş biçimde kapsar.","neighbor_ref":"root_001139/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da darlık ve üzüntüden rahatlığa geçişi anlatır."}],"source_phrase_ar":"نفس الله كربته والنفس كل شيء يفرج به عن مكروب (maqayis); نفست عنه تنفيسا أي رفهت (sihah); اللهم نفس عني أي فرج عني والريح من نفس الرحمن (tahdhib;mufradat)","source_summary":"Kaynaklar, sıkıntının hafifletilmesi ile bunun sağladığı ferahlığı ortak çekirdek sayar; esinti ve yardım bu işlevle ilişkilendirilir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه نفس الله الكربة، والتنفس عن المكروب، والفرج من الشدة، والريح أو الأنصار حين تذكر باعتبار التفريج.","what_is_not_ar":"ليس هو مجرد النفس الهوائي ولا مطلق السعة أو المهلة بلا كربة."},"support_links":["sup_7476908a9241241c8779"]},{"boundary":"Buradaki göz, görme organı ya da özdeşlik bildiren göz değil, zarar verdiğine inanılan bakıştır.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:7:1:2","qac_word_ref":"91:7:1","surface_ar":"نَفْسٍ"}],"gloss":"kem gözle zarar verme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Zarar verdiğine inanılan bakışın bir kişiye yönelip onu etkilemesidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Zararlı bakışı yönelten kişi, bu etkiyi yapan kimse olarak adlandırılır."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir bakışın kişiye zarar getirdiğine inanılan etkiyi ve gerçekleşmesini anlatır.","boundary_detail":"Buradaki göz, görme organı ya da özdeşlik bildiren göz değil, zarar verdiğine inanılan bakıştır.","branch_image_ar":"إصابة العين بالنفس","concept_gloss":"kem gözle zarar verme","contextual_glosses":[{"applicability":"Zararlı olduğuna inanılan bakışın bir kişiyi etkilediği cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bakışın hedefe ulaşıp zarar vermesi olayını korur."},"facet_ids":["F001"],"text":"kem göz değmesi","usage_role":"contextual"}],"definition":"Bir kişinin bakışıyla başkasına zarar verdiğine inanılan etki ve bu etkinin birine ulaşmasıdır. Bu bakışı yönelten kişi de dalın adlandırma alanındadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Zarar verdiğine inanılan bakışın bir kişiye yönelip onu etkilemesidir."},{"facet_id":"F002","role":"associated_use","statement":"Zararlı bakışı yönelten kişi, bu etkiyi yapan kimse olarak adlandırılır."}],"identity_rationale":"Kaynak ifadesi, bir bakışın kişiye zarar verdiği inancını, bu zararın gerçekleşmesini ve zararlı bakışı yönelten kişiyi aynı dalda açıkça birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"zarar verdiğine inanılan bakış"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ona kem göz değdi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kem gözle zarar veren kişi"}],"lexicalization_note":"Çıplak biçimler zararlı bakışı ve bunu yönelten kişiyi, kalıp kullanım ise bakışın birine değmesini anlatır.","neighbor_coverage_note":"Bütün aday kartlar gözden geçirildi; yalnızca sınırları tam örtüşen eş anlamlı dal yayımlanmaya değer bulundu.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kartlarda çekirdek, katılımcılar ve kapsam bakımından anlamlı bir ayrım görünmez; iki dal birbirinin yerine geçebilir.","focus_only":null,"gloss":"kem gözle zarar verme","neighbor_only":null,"neighbor_ref":"root_001069/B004","relation_type":"synonym","shared_zone":"İki dal da bakışla zarar verme, bunu yapan kişi ve bundan etkilenen kişi sınırlarını paylaşır."}],"source_phrase_ar":"يقال للعين نفس وأصابت فلانا نفس (maqayis); النفس العين ونفسته بنفس إذا أصبته بعين والنافس العائن (sihah); النفس العين التي تصيب المعين وإن فلانا لنفوس أي عيون (tahdhib)","source_summary":"Kaynaklar, zarar veren bakış, bu bakışın birine değmesi ve onu yönelten kişi arasında ortak ve tutarlı bir anlam bağı kurar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه تسمية العين نفسا، وإصابة المنظور بنفس، والنافس بمعنى العائن.","what_is_not_ar":"ليس هو عين الشيء بمعنى ذاته ولا النفس الروح."},"support_links":[]},{"boundary":"Dal kanı anlatır; canın kendisi, doğum sonrası kanama ya da her türlü sıvı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:7:1:2","qac_word_ref":"91:7:1","surface_ar":"نَفْسٍ"}],"gloss":"canlıdaki akışkan kan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Canlı gövdesinde bulunan ve akabilen kanı adlandırır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kanın yitirilmesi yaşamın yitirilmesine yol açtığı için kan ile can arasında bağ kurulur."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Canlı gövdesindeki kan ve özellikle akışkan kana sahip olma anlatıldığında uygundur.","boundary_detail":"Dal kanı anlatır; canın kendisi, doğum sonrası kanama ya da her türlü sıvı değildir.","branch_image_ar":"الدم السائل قوام النفس","concept_gloss":"canlıdaki akışkan kan","contextual_glosses":[{"applicability":"Bir hayvanın akışkan kana sahip olduğu kalıp kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Canlının akışkan kana sahip olması koşulunu korur."},"facet_ids":["F001"],"text":"kanı akan canlı","usage_role":"contextual"}],"definition":"Canlı gövdesinde dolaşan ve akabilen kandır; kaybının yaşamı sona erdirmesi, adlandırmanın gerekçesi olarak görülür. Akışkan kana sahip olma da özel bir kalıpla belirtilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Canlı gövdesinde bulunan ve akabilen kanı adlandırır."},{"facet_id":"F002","role":"associated_use","statement":"Kanın yitirilmesi yaşamın yitirilmesine yol açtığı için kan ile can arasında bağ kurulur."}],"identity_rationale":"Kaynak ifadesi, anlamı doğrudan kana bağlar ve kanın kaybı ile yaşamın kaybı arasındaki ilişkiyi adlandırmanın gerekçesi olarak verir. Akışkan kanlı canlılara ilişkin kalıp da aynı sınırı doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kaybıyla yaşamın da yitirildiği kan"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"hayvandaki akışkan kan"}],"lexicalization_note":"Çıplak biçim kanı adlandırır; kalıp kullanım yalnızca hayvandaki akışkan kanı ve ona sahip olmayı belirtir.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel kan alanıyla örtüşen bu komşu, odaktaki yaşam ve akışkanlık sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kanı yaşamı taşıyan akışkan madde olarak adlandırır; komşu dal ise kanın kendisine ek olarak yaradan dışarı çıkma olayını da anlatır.","focus_only":"Odak dal, kanı yaşamın sürmesiyle ilişkilendirir ve akışkan kanlı canlı kalıbını kapsar.","gloss":"kan ve kanama","neighbor_only":"Komşu dal, yara ya da kesikten kan çıkması olayını ve kan parçasını da kapsar.","neighbor_ref":"root_000491/B001","relation_type":"near_synonym","shared_zone":"İki dalın ortak alanı canlı gövdesindeki bilinen kandır."}],"source_phrase_ar":"النفس الدم وإذا فقد الدم فقد نفسه (maqayis); النفس الدم وما ليس له نفس سائلة (sihah); النفس الدم وكل شيء له نفس سائلة أراد دما سائلا (tahdhib)","source_summary":"Kaynaklar anlamı kan olarak ortaklaştırır; akışkan kanlı olma kalıbını ve kan kaybıyla yaşam kaybı arasındaki bağı da birlikte aktarır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه النفس بمعنى الدم، والنفس السائلة، وتسميته نفسا لأن فقد الدم يذهب بالنفس.","what_is_not_ar":"ليس هو الروح نفسها ولا دم النفاس من جهة الولادة إلا إذا كان اللفظ دما."},"support_links":[]},{"boundary":"Doğum ve doğum sonrası durum çekirdektir; adet görme, kaynakça bildirilen bağımlı bir yan kullanımdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B005","candidate_links":[{"candidate_id":"cand_96796df5bfc5071e3f22","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:7:1:2","qac_word_ref":"91:7:1","surface_ar":"نَفْسٍ"}],"gloss":"doğum ve doğuma bağlı kadın-çocuk durumu","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadının doğurmasını ve doğumdan sonraki kanamalı durumunu kapsar."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Doğan çocuk ve henüz doğmamış olma, doğum olayına göre adlandırılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bazı kaynak kullanımlarında kadın için adet görme anlamı da bildirilir."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Doğurma olayı, doğum sonrası kadın ve doğan çocuk birlikte kavramsallaştırıldığında uygundur.","boundary_detail":"Doğum ve doğum sonrası durum çekirdektir; adet görme, kaynakça bildirilen bağımlı bir yan kullanımdır.","branch_image_ar":"خروج الولد ودم النفاس","concept_gloss":"doğum ve doğuma bağlı kadın-çocuk durumu","contextual_glosses":[{"applicability":"Yalnızca kaynakça bildirilen yan kullanımda, kadının dönemsel kanaması kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yan kullanımın kadın ve dönemsel kanama sınırını korur."},"facet_ids":["F003"],"text":"adet görme","usage_role":"contextual"}],"definition":"Kadının doğurması, doğumdan sonraki kanamalı durumu ve dünyaya gelen çocuğun bu olayla ilişkili adlandırılmasıdır. Bazı kullanımlarda aynı söz ailesi adet görmeye de uygulanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadının doğurmasını ve doğumdan sonraki kanamalı durumunu kapsar."},{"facet_id":"F002","role":"associated_use","statement":"Doğan çocuk ve henüz doğmamış olma, doğum olayına göre adlandırılır."},{"facet_id":"F003","role":"source_variant","statement":"Bazı kaynak kullanımlarında kadın için adet görme anlamı da bildirilir."}],"identity_rationale":"Kaynak ifadesinin ana ekseni kadının doğurması, doğumdan sonraki durumu ve doğan çocuktur. Bunun yanında bazı kullanımlarda aynı söz ailesi adet görme için de aktarılır; bu yan kullanım doğum çekirdeğiyle özdeşleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"doğum yapmış ya da doğum sonrası kanaması olan kadın"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"doğum ve doğum sonrası kanama dönemi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yeni doğan çocuk"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"doğmadan önce"}],"lexicalization_note":"Biçimler doğum yapan kadını, doğum sürecini ve yeni doğanı; ayrı kullanım ise doğmadan önceki zamanı belirtir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; adet kanaması komşusu, doğum çekirdeği ile yan kullanım arasındaki sınırı doğrudan aydınlatır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda adet görme yalnızca yan kullanımdır ve ana eksen doğumdur; komşu dalın çekirdeği ise dönemsel rahim kanamasıdır.","focus_only":"Odak dalın çekirdeği doğum, doğum sonrası kadın ve yeni doğan çocuktur.","gloss":"adet kanaması","neighbor_only":"Komşu dal, rahim kanının belirli dönemlerde çıkmasını, bunun zamanını ve yerini kapsar.","neighbor_ref":"root_000379/B001","relation_type":"near_neighbor","shared_zone":"İki dal, kadından kan gelmesi bağlamında sınırlı olarak kesişir."}],"source_phrase_ar":"الحائض تسمى النفساء والنفاس ولاد المرأة والولد منفوس (maqayis); النفاس ولادة المرأة فإذا وضعت كانت نفساء (ayn;mufradat); نفست المرأة غلاما والولد منفوس وورث قبل أن ينفس أي يولد (sihah); نفست المرأة إذا حاضت وأنفست أراد أحضت (tahdhib)","source_summary":"Toplu kaynak kaydı doğum, doğum yapan kadın ve yeni doğanı ortak eksende birleştirir; ayrıca adet görme yönünde sınırlı bir kullanım farkı taşır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه النفاس ولادة المرأة، والنفساء، والمنفوس بمعنى المولود، واستعماله في الحيض حيث نص المصدر عليه.","what_is_not_ar":"ليس هو كل دم ولا كل خروج نفس، بل باب الولادة والحيض المنصوص عليه."},"support_links":["sup_2f4d9b3d80971f6ff8fe"]},{"boundary":"Dal yalnızca içme bağlamındaki sayılabilir içim bölümleridir; genel solunum ya da her küçük sıvı miktarı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:7:1:2","qac_word_ref":"91:7:1","surface_ar":"نَفْسٍ"}],"gloss":"soluk aralı içim ve bir içimlik yudum","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İçme eylemi soluklanma aralarıyla ayrılan sayılabilir bölümlere ayrılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tek bölüm, bir yudum ya da bir solukta alınan içimlik paydır."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İçeceğin aralarda soluklanılarak bölümler hâlinde içilmesi ve her bölümün sayılması için uygundur.","boundary_detail":"Dal yalnızca içme bağlamındaki sayılabilir içim bölümleridir; genel solunum ya da her küçük sıvı miktarı değildir.","branch_image_ar":"نفس الشرب وجرعته","concept_gloss":"soluk aralı içim ve bir içimlik yudum","contextual_glosses":[{"applicability":"İçme eylemi üç ayrı bölümde ve aralarda soluklanarak yapıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İçmenin üç sayılabilir bölüme ayrılmasını korur."},"facet_ids":["F001"],"text":"üç solukta içmek","usage_role":"contextual"}],"definition":"Bir içeceği, aralarda soluklanarak bir veya birkaç ayrı içim bölümünde içmektir. Her bölüm tek bir yudumlama ya da içimlik pay olarak sayılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İçme eylemi soluklanma aralarıyla ayrılan sayılabilir bölümlere ayrılır."},{"facet_id":"F002","role":"specialization","statement":"Tek bölüm, bir yudum ya da bir solukta alınan içimlik paydır."}],"identity_rationale":"Kaynak ifadesi, içmeyi soluk aralarıyla bölünen bir eylem olarak ve bu eylemin tek bir içimlik bölümünü açıkça anlatır. Bir, iki ya da üç olarak sayılan şey içmenin bu bölümleridir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bir solukta alınan yudum ya da içim"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"üç soluk arasıyla içme"}],"lexicalization_note":"Çıplak biçim bir içimlik bölümü, kalıp ise içmenin üç soluk arasıyla yapılmasını anlatır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yudum komşusu, miktar ile soluk aralığına göre bölünmüş içim arasındaki farkı en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odaktaki birim soluk arasıyla belirlenen içim bölümüdür; komşudaki birim ise boğazdan geçirilen sıvı miktarı ve yutma hareketidir.","focus_only":"Odak dal, içmeyi soluklanma aralarıyla bölüp her bölümü sayar.","gloss":"yudum ve yutma","neighbor_only":"Komşu dal, boğazdan geçirilen küçük miktarı, ağız dolusunu ve istemeden art arda yutmayı kapsar.","neighbor_ref":"root_000237/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir içeceğin küçük ve tek seferlik alınışını kapsar."}],"source_phrase_ar":"كرع في الإناء نفسا أو نفسين (maqayis); شربت الماء بنفس وثلاثة أنفاس وكل مستراح منه نفس (ayn); النفس الجرعة اكرع في الإناء نفسا أو نفسين (sihah); يشرب الماء وغيره بثلاث أنفاس (tahdhib)","source_summary":"Kaynaklar, içme eyleminin bir, iki veya üç soluk aralığına bölünmesini ve her bölümün bir içimlik pay sayılmasını ortaklaştırır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الشرب بنفس أو أنفاس، والنفس بمعنى الجرعة أو المستراح في الشرب.","what_is_not_ar":"ليس هو مجرد التنفس خارج الشرب ولا قدر الدباغ وإن وافقه في صغر المقدار."},"support_links":[]},{"boundary":"Dal, deri işleme maddesinin ölçüsüdür; işlenmiş derinin kendisi, belirli bir bitki ya da içecek yudumu değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:7:1:2","qac_word_ref":"91:7:1","surface_ar":"نَفْسٍ"}],"gloss":"bir deri işlemeye yetecek sepi maddesi payı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir derinin tek seferlik işlenmesine yetecek küçük sepi maddesi miktarıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İşleme maddesi bir veya iki küçük pay hâlinde ölçülüp verilebilir."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Deri işlemede kullanılan maddenin tek uygulamalık küçük miktarı için uygundur.","boundary_detail":"Dal, deri işleme maddesinin ölçüsüdür; işlenmiş derinin kendisi, belirli bir bitki ya da içecek yudumu değildir.","branch_image_ar":"قدر دبغة يسيرة","concept_gloss":"bir deri işlemeye yetecek sepi maddesi payı","contextual_glosses":[{"applicability":"Malzeme iki küçük uygulama payı olarak istendiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Maddenin iki ayrı işleme payı olarak sayılmasını korur."},"facet_ids":["F002"],"text":"iki işlemelik sepi maddesi","usage_role":"contextual"}],"definition":"Bir deriyi bir kez sepelemek için gereken küçük işleme maddesi miktarıdır. Bu miktar bir ya da iki pay olarak sayılabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir derinin tek seferlik işlenmesine yetecek küçük sepi maddesi miktarıdır."},{"facet_id":"F002","role":"specialization","statement":"İşleme maddesi bir veya iki küçük pay hâlinde ölçülüp verilebilir."}],"identity_rationale":"Kaynak ifadesi, bir deriyi bir kez işlemek için gereken küçük sepi maddesi miktarını ve bunun bir ya da iki pay olarak sayılmasını açıkça bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"deriyi bir kez işlemeye yetecek sepi maddesi"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bir işlemelik sepi maddesi payı"}],"lexicalization_note":"Çıplak biçim küçük sepi maddesi payını, kalıp kullanım ise bunun bir veya iki pay olarak verilmesini anlatır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; belirli işleme bitkisini anlatan komşu, malzeme türü ile malzeme miktarı ayrımını açıkça gösterir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak bir ölçü birimidir; komşu ise belirli bir bitkiyi ve ondan türeyen deri işleme kullanımlarını adlandırır.","focus_only":"Odak dal, deri işlemede kullanılan maddenin tek uygulamalık miktarını bildirir.","gloss":"deri işlemede kullanılan ağaç","neighbor_only":"Komşu dal, belirli bir ağacı, onunla işlenmiş deriyi ve ağacın hayvana etkisini kapsar.","neighbor_ref":"root_001079/B003","relation_type":"same_field","shared_zone":"İki dal da deri işleme sürecinde kullanılan maddeler alanındadır."}],"source_phrase_ar":"في الدباغ نفس قدر ما يدبغ به الإهاب مرة (maqayis); النفس قدر دبغة مما يدبغ به الأديم (sihah); النفس قدر دبغة أو دبغتين من الدباغ (tahdhib)","source_summary":"Kaynaklar, anlamı derinin bir kez işlenmesine yetecek küçük sepi maddesi payı olarak ortak biçimde verir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه النفس أو النفسين من الدباغ، أي مقدار يسير يدبغ به الجلد مرة أو مرتين.","what_is_not_ar":"ليس هو جرعة الشراب ولا النفاسة في المال."},"support_links":[]},{"boundary":"Dal, su ve içeceğin yaşamı sürdürme ya da doyurucu olma niteliğidir; sayılan tek yudum veya canın kendisi değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:7:1:2","qac_word_ref":"91:7:1","surface_ar":"نَفْسٍ"}],"gloss":"yaşamı sürdüren, bol ve doyurucu su","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Su, yaşamın sürmesini sağlayan temel içecek olarak adlandırılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İçecek, bol ve susuzluğu giderici olduğunda doyurucu bir genişlik taşır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Karşıt kalıp, içecekte doyurucu ve rahat içimli niteliğin bulunmadığını bildirir."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Su ya da içecek, yaşamı destekleyen ve susuzluğu gideren yeterlilik bakımından anlatıldığında uygundur.","boundary_detail":"Dal, su ve içeceğin yaşamı sürdürme ya da doyurucu olma niteliğidir; sayılan tek yudum veya canın kendisi değildir.","branch_image_ar":"ماء تقام به النفس","concept_gloss":"yaşamı sürdüren, bol ve doyurucu su","contextual_glosses":[{"applicability":"İçeceğin karşıt kalıpla, rahat içim ve doyuruculuktan yoksun olduğu anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doyurucu ve rahat içimli niteliğin yokluğunu korur."},"facet_ids":["F003"],"text":"içimi güç ve doyurmayan içecek","usage_role":"contextual"}],"definition":"Yaşamı ayakta tutan su ve içene genişlik sağlayıp susuzluğu gideren doyurucu içecektir. Karşıt kullanım, içeceğin bu rahat içimli ve doyurucu niteliği taşımadığını belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Su, yaşamın sürmesini sağlayan temel içecek olarak adlandırılır."},{"facet_id":"F002","role":"specialization","statement":"İçecek, bol ve susuzluğu giderici olduğunda doyurucu bir genişlik taşır."},{"facet_id":"F003","role":"source_variant","statement":"Karşıt kalıp, içecekte doyurucu ve rahat içimli niteliğin bulunmadığını bildirir."}],"identity_rationale":"Kaynak ifadesi suyu yaşamı ayakta tutan madde olarak adlandırır ve içeceğin bol, doyurucu ve susuzluğu giderici oluşunu aynı bağıntıyla açıklar. Karşıt kalıp bu niteliğin bulunmadığını bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yaşamı ayakta tutan su"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bol ve susuzluğu gideren içecek"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"tadı kötü, bayat ve içimi güç içecek"}],"lexicalization_note":"Çıplak biçim suyu, iki karşıt kalıp ise içecekte doyurucu genişliğin bulunmasını ya da bulunmamasını anlatır.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı; susuzluğu giderme komşusu, içeceğin niteliği ile içenin ulaştığı sonuç arasındaki sınırı belirginleştirir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak, suyun ya da içeceğin yeterli ve doyurucu niteliğidir; komşu ise içenin susuzluktan kurtulması sonucunu ve bunun mecazlı uzantısını anlatır.","focus_only":"Odak dal suyu ve içeceği, doyurucu niteliğin taşıyıcısı olarak adlandırır.","gloss":"susuzluğu giderme","neighbor_only":"Komşu dal susuzluğu giderme eylemini ve haber ya da görüşle iç rahatlığı bulma uzantısını kapsar.","neighbor_ref":"root_001544/B002","relation_type":"near_synonym","shared_zone":"İki dal da su içmenin susuzluğu giderip rahatlık sağlaması alanında örtüşür."}],"source_phrase_ar":"يقال للماء نفس ولأن قوام النفس به (maqayis); النفس الماء وشراب ذو نفس أي فيه سعة وري وشراب غير ذي نفس (tahdhib)","source_summary":"Kaynaklar suyu yaşamın dayanağı sayar; içecekte bolluk ve susuzluğu giderme niteliğini olumlu ve olumsuz kalıplarla karşılaştırır.","sources":["MQ","TA"],"what_is_ar":"يدخل فيه تسمية الماء نفسا، والشراب ذو النفس إذا كان فيه سعة وري، ونقيضه الشراب غير ذي نفس.","what_is_not_ar":"ليس هو النفس الروح نفسها ولا جرعة الشرب المعدودة فقط."},"support_links":[]},{"boundary":"Dal, yayılma ve açılmayı belirli öznelere bağlayan kalıplardan oluşur; genel bir çıplak anlam ya da canlı solunumu değildir.","branch_kind":"collocation","branch_ref":"root_001533/B009","candidate_links":[{"candidate_id":"cand_b0ce2b6cc5181e104841","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:7:1:2","qac_word_ref":"91:7:1","surface_ar":"نَفْسٍ"}],"gloss":"kalıba bağlı yarılıp açılma ve genişleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"specialization","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yay için kullanıldığında yarılma ya da çatlama olayını bildirir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sabah ve gündüz için kullanıldığında aydınlığın açılmasını, sürenin uzayıp genişlemesini bildirir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Irmak ya da dalga için kullanıldığında suyun artıp dışarı doğru yayılmasını bildirir."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca verilen yay, sabah, gündüz ve su kalıplarının ortak görüntüsünü topluca anlatmak için uygundur.","boundary_detail":"Dal, yayılma ve açılmayı belirli öznelere bağlayan kalıplardan oluşur; genel bir çıplak anlam ya da canlı solunumu değildir.","branch_image_ar":"انفتاح الصبح والشيء كالنفس","concept_gloss":"kalıba bağlı yarılıp açılma ve genişleme","contextual_glosses":[{"applicability":"Karanlığın yarılıp sabah aydınlığının belirmesi kalıbında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sabah aydınlığının yarılıp açılarak belirmesini korur."},"facet_ids":["F002"],"text":"sabahın sökmesi","usage_role":"contextual"},{"applicability":"Irmak suyunun yükselip çevreye doğru yayılması kalıbında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Su miktarındaki artışı ve dışa doğru yayılmayı korur."},"facet_ids":["F003"],"text":"suyun artıp yayılması","usage_role":"contextual"}],"definition":"Yalnızca belirli kalıplarda, yayın yarılması; sabahın açılması; gündüzün uzayıp genişlemesi veya ırmak suyunun artıp yayılmasıdır. Ortak görüntü, kapalı ya da dar bir durumdan açılma ve genişlemeye geçiştir.","distinctive_facets":[{"facet_id":"F001","role":"specialization","statement":"Yay için kullanıldığında yarılma ya da çatlama olayını bildirir."},{"facet_id":"F002","role":"core","statement":"Sabah ve gündüz için kullanıldığında aydınlığın açılmasını, sürenin uzayıp genişlemesini bildirir."},{"facet_id":"F003","role":"extension","statement":"Irmak ya da dalga için kullanıldığında suyun artıp dışarı doğru yayılmasını bildirir."}],"identity_rationale":"Kaynak ifadesindeki kullanımlar, belirli öznelerin yarılması, açılması, uzayıp genişlemesi veya suyu artarak yayılması ortak görüntüsünde birleşir. Bu anlam yalnızca verilen kalıplarda geçerlidir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yay çatladı ya da yarıldı"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"sabah söktü, aydınlık yayıldı"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"gündüz uzayıp genişledi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"ırmağın suyu artıp yayıldı"}],"lexicalization_note":"Anlam yalnızca yay, sabah, gündüz ve ırmakla kurulan kalıplara bağlıdır; çıplak kök anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sabahın açılması ortaklığını ve kalıpların farklı yönlere uzanmasını en açık gösteren komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ortak sabah görüntüsüne rağmen odak dalın öteki kalıpları yay, gündüz ve suya uzanır; komşu ise bulut açıklığı ve yağış alanındaki boşluk yönünde genişler.","focus_only":"Odak dal, sabah yanında yayın çatlamasını, gündüzün genişlemesini ve suyun artmasını da kapsayan ayrı kalıplar taşır.","gloss":"sabahın ve bulutun yarılıp açılması","neighbor_only":"Komşu dal, güneş ya da ayın bulut aralığından çıkmasını ve çevresi yağmurluyken kuru kalan yeri de kapsar.","neighbor_ref":"root_001126/B003","relation_type":"near_neighbor","shared_zone":"İki dal, sabah aydınlığının karanlığı yararak ortaya çıkması görüntüsünde kesişir."}],"source_phrase_ar":"تنفست القوس انشقت (maqayis); تنفس الصبح أي تبلج وتنفس النهار إذا زاد والموج إذا نضح الماء (sihah); إذا انشق الفجر وانفلق وتنفس دجلة إذا زاد ماؤها (tahdhib); تنفس النهار عبارة عن توسعه (mufradat)","source_summary":"Toplu kaynak kaydı, yaydaki çatlama, sabahtaki açılma, gündüzdeki genişleme ve sudaki artışı kalıba bağlı bir açılma-yayılma görüntüsünde birleştirir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه تنفس الصبح والنهار إذا تبلج أو امتد، وتنفس القوس إذا انشقت، وزيادة الماء أو الموج حين يخرجان أو ينتشران.","what_is_not_ar":"ليس هو التنفس الحيواني ولا مجرد السعة الزمنية إلا إذا كان اللفظ عن الانفتاح أو الامتداد."},"support_links":["sup_7476908a9241241c8779"]},{"boundary":"Dal dışarıdaki değerli şeye yönelen istek ve çekişmeyle ilgilidir; kişinin kendi onuru ya da yücelik duygusu değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:7:1:2","qac_word_ref":"91:7:1","surface_ar":"نَفْسٍ"}],"gloss":"değerli ve uğrunda yarışılan şey","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yüksek değer ve önem taşıdığı için insanların arzuladığı şeydir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsanlar bu şeyi elde etmek ya da üstünlere benzemek için birbirleriyle yarışabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Değerli şeyi başkasından esirgeme veya ona sahip olanı kıskanma biçiminde bir sahiplenme doğabilir."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin yüksek değeri insanların onu istemesine ve elde etmek için yarışmasına yol açtığında uygundur.","boundary_detail":"Dal dışarıdaki değerli şeye yönelen istek ve çekişmeyle ilgilidir; kişinin kendi onuru ya da yücelik duygusu değildir.","branch_image_ar":"شيء نفيس تتنافس فيه النفوس","concept_gloss":"değerli ve uğrunda yarışılan şey","contextual_glosses":[{"applicability":"Değerli görülen şeyin başkasına geçmesi istenmediğinde veya sahibi kıskanıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Değerli şeye yönelik kıskanç sahiplenmeyi ve esirgemeyi korur."},"facet_ids":["F003"],"text":"kıskanıp başkasından esirgemek","usage_role":"contextual"}],"definition":"İnsanların değer ve önem yüklediği, elde etmek ya da benzemek için uğrunda yarıştığı şeydir; bu yönelim, şeyin başkasına geçmesini istemeyerek esirgeme veya kıskanma biçimini de alabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yüksek değer ve önem taşıdığı için insanların arzuladığı şeydir."},{"facet_id":"F002","role":"extension","statement":"İnsanlar bu şeyi elde etmek ya da üstünlere benzemek için birbirleriyle yarışabilir."},{"facet_id":"F003","role":"associated_use","statement":"Değerli şeyi başkasından esirgeme veya ona sahip olanı kıskanma biçiminde bir sahiplenme doğabilir."}],"identity_rationale":"Kaynak ifadesi değerli şeyi, ona yönelen isteği, uğrunda yarışmayı ve başkasına geçmesini istemeyerek esirgeme ya da kıskanmayı tek bir değer-yönelim zincirinde açıkça birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"değerli, önemli ve arzulanan"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"bir şeyi elde etme ya da üstünlere benzeme yarışı"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"başkasına vermeye kıyamayıp esirgemek"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"sahip olduğu şey yüzünden onu kıskanmak"}],"lexicalization_note":"Biçimler değerli şeyi ve yarışmayı, kalıplar ise o şeyi başkasından esirgeme veya kıskanmayı anlatır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; değerli nesne ortaklığı yanında yarışma sınırını görünür kılan en yararlı komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal değerden doğan kişiler arası yarışma ve kıskançlığı kurar; komşu dal ise değerli nesne ile sahibinin ona bağlılığı üzerinde durur.","focus_only":"Odak dal, yüksek değerin yanında o şey uğrundaki yarışmayı ve kıskanç esirgemeyi de kapsar.","gloss":"bağlanılan değerli şey","neighbor_only":"Komşu dal, sahibinin bağlandığı ve koruduğu malı ya da başka değerli nesneleri adlandırmaya ağırlık verir.","neighbor_ref":"root_001039/B007","relation_type":"near_synonym","shared_zone":"İki dal da değerli görülen ve sahibinin kolayca vazgeçmediği şeyi kapsar."}],"source_phrase_ar":"شيء نفيس ذو نفس وخطر يتنافس به والتنافس يبرز كل واحد قوة نفسه (maqayis); شيء نفيس متنافس فيه ونفست به ضننت (ayn); نافست في الشيء إذا رغبت فيه وتنافسوا فيه ونفس به أي ضن أو حسد (sihah); مال نفيس ومنفس وكل شيء له خطر وقدر ونفس عليك أي حسدك (tahdhib); المنافسة مجاهدة النفس للتشبه بالأفاضل ونفست بكذا ضنت نفسي به وشيء نفيس (mufradat)","source_summary":"Kaynaklar yüksek değer, ona duyulan istek, yarışma ve değerli şeyi başkasından esirgeme ya da kıskanma ilişkilerini tek bir toplu iddiada birleştirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه النفيس والنفاسة والمنفس، والرغبة والمنافسة في الشيء، والضن أو الحسد به إذا كان لقيمته ورغبة النفس فيه.","what_is_not_ar":"ليس هو عزة النفس والهمة في صاحبها إلا إذا كان الكلام عن المال أو الشيء المرغوب فيه."},"support_links":[]},{"boundary":"Dal bedensel yaşamı sağlayan can ve canlı bireydir; düşünce, özdeşlik vurgusu, kan ya da soluk değildir.","branch_kind":"bare","branch_ref":"root_001533/B011","candidate_links":[{"candidate_id":"cand_4c482ef9adf32142ff3b","lane":"micro"},{"candidate_id":"cand_96796df5bfc5071e3f22","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:7:1:2","qac_word_ref":"91:7:1","surface_ar":"نَفْسٍ"}],"gloss":"bedene yaşam veren can","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bedene yaşam veren ve bedenden ayrılması ölüm sayılan candır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu canı taşıyan her insan ayrı bir canlı birey olarak adlandırılabilir."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Canlılığı sağlayan ve bedenden ayrılması ölüm anlamına gelen yaşam taşıyıcısı için uygundur.","boundary_detail":"Dal bedensel yaşamı sağlayan can ve canlı bireydir; düşünce, özdeşlik vurgusu, kan ya da soluk değildir.","branch_image_ar":"النفس التي بها الحياة","concept_gloss":"bedene yaşam veren can","contextual_glosses":[{"applicability":"İnsanların tek tek canlı varlıklar olarak sayıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Her insanın ayrı bir canlı birey olarak sayılmasını korur."},"facet_ids":["F002"],"text":"canlı birey","usage_role":"contextual"}],"definition":"Bedeni canlı tutan ve ayrılmasıyla ölümün gerçekleştiği candır. Bu yaşam taşıyıcısı bakımından her insan ayrı bir canlı birey olarak da sayılabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bedene yaşam veren ve bedenden ayrılması ölüm sayılan candır."},{"facet_id":"F002","role":"extension","statement":"Bu canı taşıyan her insan ayrı bir canlı birey olarak adlandırılabilir."}],"identity_rationale":"Kaynak ifadesi bedeni canlı tutan ilkeyi, onun bedenden çıkmasıyla ölümü ve her insanın canlı bir birey olarak bu adla sayılabilmesini doğrudan açıklar.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"bedene yaşam veren can"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"insan ya da canlı birey"}],"lexicalization_note":"Çıplak dal, bedene yaşam veren canı ve bununla canlı sayılan bireyi kapsar; kalıp anlamı içe aktarılmaz.","neighbor_coverage_note":"Bütün adaylar gözden geçirildi; yalnızca yaşam veren can anlamında tam sınır eşleşmesi gösteren eş anlamlı komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kartlarda çekirdek, yaşam işlevi ve bedenden ayrılma sınırı bütünüyle örtüşür; anlamlı bir ayrım yoktur.","focus_only":null,"gloss":"bedene yaşam veren can","neighbor_only":null,"neighbor_ref":"root_000609/B001","relation_type":"synonym","shared_zone":"İki dal da bedeni canlı tutan canı ve onun bedenden çıkmasını aynı sınırlarla anlatır."}],"source_phrase_ar":"النفس الروح الذي به حياة الجسد وكل إنسان نفس (ayn); النفس الروح يقال خرجت نفسه (sihah); خرجت نفس فلان أي روحه ونفس الحياة هي الروح (tahdhib); النفس الروح في قوله أخرجوا أنفسكم (mufradat)","source_summary":"Kaynaklar, bedensel yaşamı sağlayan can, bu canın çıkmasıyla ölüm ve insanın canlı birey olarak sayılması üzerinde birleşir.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه النفس بمعنى الروح والحياة، وكل إنسان نفس، وخروج النفس عند الموت، والنفس الحية التي بها حياة الجسد.","what_is_not_ar":"ليس هو ذات الشيء للتوكيد ولا ما في النفس من قصد أو غيب فقط."},"support_links":["sup_2f4d9b3d80971f6ff8fe","sup_cb48e2d7a205ef978585"]},{"boundary":"Dal yalnızca özdeşlik ve pekiştirme kalıplarındadır; canlılık ilkesi, zararlı bakış ya da iç düşünce değildir.","branch_kind":"collocation","branch_ref":"root_001533/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:7:1:2","qac_word_ref":"91:7:1","surface_ar":"نَفْسٍ"}],"gloss":"şeyin kendisi ve bütün öz varlığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin bütün gerçeği ve öz varlığıyla kendisini pekiştirerek gösterir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin başkası aracılığıyla değil, bizzat kendisinin bulunmasını belirtir."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesne ya da kişinin başkası değil tam olarak kendisi olduğu vurgulandığında uygundur.","boundary_detail":"Dal yalnızca özdeşlik ve pekiştirme kalıplarındadır; canlılık ilkesi, zararlı bakış ya da iç düşünce değildir.","branch_image_ar":"عين الشيء وذاته","concept_gloss":"şeyin kendisi ve bütün öz varlığı","contextual_glosses":[{"applicability":"Bir kişinin aracı kullanmadan doğrudan bulunduğu ya da eylemi yaptığı bağlamda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin doğrudan ve aracısız bulunması vurgusunu korur."},"facet_ids":["F002"],"text":"bizzat kendisi","usage_role":"contextual"}],"definition":"Bir şeyin başkası ya da bir parçası değil, bütün gerçeği ve öz varlığıyla kendisi olduğunu vurgulamaktır. Kişi için kullanıldığında onun aracısız biçimde bizzat bulunmasını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin bütün gerçeği ve öz varlığıyla kendisini pekiştirerek gösterir."},{"facet_id":"F002","role":"specialization","statement":"Kişinin başkası aracılığıyla değil, bizzat kendisinin bulunmasını belirtir."}],"identity_rationale":"Kaynak ifadesi bir şeyin aynısını, bütün varlığını, gerçeğini ve özünü vurgulayan kullanımı açıkça verir. Kişinin aracısız olarak bizzat bulunması da aynı özdeşlik kalıbına bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"şeyin tam kendisi ve gerçeği"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"başkası aracılığıyla değil, bizzat kendisi"}],"lexicalization_note":"Anlam, bir şeyin kendisini ya da bir kişinin bizzat bulunmasını bildiren kalıplarla sınırlıdır; çıplak anlama genellenmez.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı; özdeşlik ortaklığını ve pekiştirme-seçip belirleme farkını gösteren komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kalıba bağlı özdeşlik pekiştirmesidir; komşu dal özdeşliğe ek olarak bir öğeyi topluluktan ayırıp belirleme işlevi taşır.","focus_only":"Odak dal, bütün öz varlığı ve bizzat bulunmayı pekiştiren kalıpları kapsar.","gloss":"şeyin aynısı ve kendisi","neighbor_only":"Komşu dal, bir öğeyi topluluğun geri kalanından özellikle seçip belirtme kullanımını da kapsar.","neighbor_ref":"root_001069/B013","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin başka bir şey değil, tam olarak kendisi olduğunu bildirir."}],"source_phrase_ar":"كل شيء بعينه نفس (ayn); نفس الشيء عينه يؤكد به (sihah); معنى النفس حقيقة الشيء وجملته وذاته كلها وعين الشيء وكنهه وجوهره (tahdhib); نفسه ذاته (mufradat)","source_summary":"Kaynaklar, şeyin kendisini bütün gerçeği ve özüyle vurgulama ile kişinin bizzat bulunması kullanımında birleşir.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه النفس بمعنى عين الشيء، ذاته، حقيقته، جملته، كنهه وجوهره، واستعمالها للتوكيد.","what_is_not_ar":"ليس هو الروح الحية ولا العين المؤذية ولا المعنى الباطن من القصد إلا بقرينة."},"support_links":[]},{"boundary":"Dal iç düşünce ve ayırt etme gücüyle sınırlıdır; kişinin bütünü, bedensel canı veya yalnızca dışa vurulmuş söz değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B013","candidate_links":[{"candidate_id":"cand_4179c04160b9c40cdde6","lane":"micro"},{"candidate_id":"cand_74b25835ef8bf1766191","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:7:1:2","qac_word_ref":"91:7:1","surface_ar":"نَفْسٍ"}],"gloss":"iç düşünce, niyet ve ayırt etme gücü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin içinde tuttuğu düşünce, niyet ya da kendine özgü bilgidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Doğru ayrımlar yapmayı sağlayan zihinsel yeti de bu içsel idrak alanında adlandırılır."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin dışa vurmadığı içeriği veya ayrım yapmasını sağlayan zihinsel yetisi anlatıldığında uygundur.","boundary_detail":"Dal iç düşünce ve ayırt etme gücüyle sınırlıdır; kişinin bütünü, bedensel canı veya yalnızca dışa vurulmuş söz değildir.","branch_image_ar":"ما في النفس من عقل وروع","concept_gloss":"iç düşünce, niyet ve ayırt etme gücü","contextual_glosses":[{"applicability":"Kişinin henüz söylemediği bir şeyi düşünmesi ya da yapmaya niyetlenmesi bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Düşüncenin içte bulunmasını ve henüz dışa vurulmamasını korur."},"facet_ids":["F001"],"text":"aklından geçirmek","usage_role":"contextual"}],"definition":"Kişinin içinde bulunan, henüz dışa vurulmamış düşünce, niyet veya bilgidir. Aynı alan, kişinin ayırt etmesini sağlayan zihinsel gücü de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin içinde tuttuğu düşünce, niyet ya da kendine özgü bilgidir."},{"facet_id":"F002","role":"extension","statement":"Doğru ayrımlar yapmayı sağlayan zihinsel yeti de bu içsel idrak alanında adlandırılır."}],"identity_rationale":"Kaynak ifadesi kişinin içinde taşıdığı düşünceyi, niyeti ve bilgiyi; ayrıca ayırt etmeyi sağlayan zihinsel yetiyi açıkça aynı içsel idrak alanında toplar.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"onun içinden geçen düşünce ya da niyet"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"ayırt etmeyi sağlayan zihinsel güç"}],"lexicalization_note":"Kalıp kullanım içteki düşünce ve niyeti, ayrı birim ise ayırt etmeyi sağlayan zihinsel gücü anlatır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; söylenmemiş düşünce komşusu, içsel alanın söz tasarısından daha geniş olduğunu en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal içsel idrakin daha geniş alanıdır; komşu dal özellikle dile getirilmeden önce zihinde tasarlanan söze yönelir.","focus_only":"Odak dal, dışa vurulmamış düşüncenin yanında niyet, iç bilgi ve ayırt etme yetisini de kapsar.","gloss":"söylenmemiş iç düşünce","neighbor_only":"Komşu dal, sözle ortaya konmadan önce zihinde tasarlanan söyleyiş içeriğine odaklanır.","neighbor_ref":"root_001272/B012","relation_type":"near_synonym","shared_zone":"İki dal da kişinin zihninde bulunan fakat henüz sözle açıklanmamış içeriği kapsar."}],"source_phrase_ar":"نفس العقل التي يكون بها التمييز وفي نفس فلان أن يفعل أي في روعه وتعلم ما في نفسي أي ما عندي أو غيبك (tahdhib); يعلم ما في أنفسكم وتعلم ما في نفسي ولا أعلم ما في نفسك (mufradat)","source_summary":"Kaynaklar, kişinin içindeki düşünce ve bilgiyi ayırt etme yetisiyle birlikte içsel idrak alanında birleştirir.","sources":["TA","MU"],"what_is_ar":"يدخل فيه ما في نفس المرء من روع وقصد، ونفس العقل والتمييز، وما يعبر عنه بالغيب أو العندية في سياق ما في النفس.","what_is_not_ar":"ليس هو الذات المؤكدة ولا الروح التي بها الحياة إلا إذا دل السياق على الإدراك الباطن."},"support_links":["sup_051b15c553e5f0bf5c7a","sup_de61a071343d2648747b"]},{"boundary":"Karakter gücü ile yüksek özdeğer aynı dalda iki bağlı görünüm olarak ayrılır; dışarıdaki değerli mal ve onun için yarışma kapsama girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:7:1:2","qac_word_ref":"91:7:1","surface_ar":"نَفْسٍ"}],"gloss":"sağlam, cömert ve onurlu yaradılış","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin sağlam karakterli, dayanıklı ve cömert oluşunu bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin büyüklük duygusu, gururu, onuru, yüksek amacı ve kendine saygısı da ayrı görünüm olarak aktarılır."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin dayanıklılığı, cömertliği ve kendine verdiği yüksek değer birlikte anlatıldığında uygundur.","boundary_detail":"Karakter gücü ile yüksek özdeğer aynı dalda iki bağlı görünüm olarak ayrılır; dışarıdaki değerli mal ve onun için yarışma kapsama girmez.","branch_image_ar":"قوة النفس وخلقها","concept_gloss":"sağlam, cömert ve onurlu yaradılış","contextual_glosses":[{"applicability":"Kişinin kendi değerini koruması, yüksek hedef taşıması veya gurur göstermesi bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Onuru, yüksek amacı ve kendine değer verme yönünü korur."},"facet_ids":["F002"],"text":"yüksek amaç ve kendine saygı","usage_role":"contextual"}],"definition":"Kişide görülen sağlam karakter, dayanıklılık ve cömertliktir; buna bağlı ikinci görünüm, kişinin kendi değerini yüksek tutması, onur, yüksek amaç ve kimi bağlamlarda gurur göstermesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin sağlam karakterli, dayanıklı ve cömert oluşunu bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Kişinin büyüklük duygusu, gururu, onuru, yüksek amacı ve kendine saygısı da ayrı görünüm olarak aktarılır."}],"identity_rationale":"Kaynak ifadesi bir yanda karakter, dayanıklılık ve cömertliği; öte yanda büyüklük duygusu, gurur, onur, yüksek amaç ve kendine saygıyı aktarır. Dal korunabilir, ancak bu iki görünüm tek ve ayrışmaz bir huy gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"sağlam karakterli, dayanıklı ve cömert adam"},{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"büyüklük duygusu, onur, yüksek amaç ve kendine saygı"}],"lexicalization_note":"Kişiyle kurulan kalıp karakter, dayanıklılık ve cömertliği; çıplak biçim büyüklük, onur ve yüksek amacı bildirir.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı; cömertlik ortaklığı ile karakter gücü ve eylem hevesi ayrımını gösteren komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kişinin yerleşik karakter gücü ve özdeğerini anlatır; komşu ise iyilik yapma anındaki gönüllü canlılık ve atılganlığı öne çıkarır.","focus_only":"Odak dal, dayanıklılık ve cömertliğin yanında gurur, onur ve yüksek amacı da kapsar.","gloss":"iyiliğe heves ve eli açıklık","neighbor_only":"Komşu dal, iyilik yapmaya hevesle yönelme, canlılık ve gönül genişliği üzerinde durur.","neighbor_ref":"root_000609/B010","relation_type":"near_synonym","shared_zone":"İki dal, cömert ve iyi davranışa yatkın kişi görünümünde örtüşür."}],"source_phrase_ar":"رجل له نفس أي خلق وجلادة وسخاء (ayn); النفس العظمة والكبر والعزة والهمة والأنفة (tahdhib)","source_summary":"Toplu kaynak kaydı, sağlam ve cömert karakter görünümünü kişinin büyüklük, onur, yüksek amaç ve kendine saygı duygularıyla yan yana getirir.","sources":["AY","TA"],"what_is_ar":"يدخل فيه النفس بمعنى الخلق والجلادة والسخاء، وبمعنى العظمة والكبر والعزة والهمة والأنفة.","what_is_not_ar":"ليس هو النفيس من المال ولا المنافسة على شيء خارج النفس."},"support_links":[]},{"boundary":"Dal ölçülebilir yer, boyut veya süre genişliğidir; belirli bir sıkıntıyı giderme ya da sabahın açılması değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:7:1:2","qac_word_ref":"91:7:1","surface_ar":"نَفْسٍ"}],"gloss":"uzaklık, genişlik ve zaman payı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Mekânda iki sınır arasındaki uzaklık, açıklık veya boyutsal genişliktir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Zamanda ek süre, işte ise rahat davranmaya elveren hareket alanıdır."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Mekânsal aralık, nesne boyutu, ek süre veya bir işteki hareket alanı anlatıldığında uygundur.","boundary_detail":"Dal ölçülebilir yer, boyut veya süre genişliğidir; belirli bir sıkıntıyı giderme ya da sabahın açılması değildir.","branch_image_ar":"سعة ومسافة ومهلة","concept_gloss":"uzaklık, genişlik ve zaman payı","contextual_glosses":[{"applicability":"Bir işi yapmak için yeterli serbestlik ve ek zaman bulunduğu bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşteki serbestliği ve ek süre payını birlikte korur."},"facet_ids":["F002"],"text":"rahat hareket edecek alan ve süre","usage_role":"contextual"}],"definition":"Yer bakımından uzaklık veya aralık, boyut bakımından uzunluk ve genişlik, zaman ya da iş bakımından ise ek süre ve hareket alanıdır. Bütün kullanımlarda sınırlar arasındaki payın büyümesi esastır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Mekânda iki sınır arasındaki uzaklık, açıklık veya boyutsal genişliktir."},{"facet_id":"F002","role":"extension","statement":"Zamanda ek süre, işte ise rahat davranmaya elveren hareket alanıdır."}],"identity_rationale":"Kaynak ifadesi mekânsal uzaklık ve genişliği, işte hareket alanı ve süre payını, ayrıca uzunluk ve zaman uzatımını aynı genişleme ölçüsü altında açıkça toplar.","lexical_glosses":[{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"işinde rahat hareket edecek genişlikte"},{"lexical_unit_id":"lu_041","rendering_kind":"ordinary","target_gloss":"ek süre ya da hareket alanı"},{"lexical_unit_id":"lu_042","rendering_kind":"ordinary","target_gloss":"daha uzak, daha uzun ya da daha geniş"}],"lexicalization_note":"Kalıp kullanım bir işteki hareket alanını, biçimler ise süre payı ile mekânsal ya da boyutsal genişliği anlatır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; uzunluk ve uzaklık ortaklığının yanında odaktaki süre ve hareket alanı ekini gösteren komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genişleyen payı yer, boyut ve süre arasında geneller; komşu dal belirli varlıkların uzun veya uzak oluşuna ve işin uzamasına yönelir.","focus_only":"Odak dal, uzaklık ve uzunluğun yanında ek süreyi ve bir işteki rahat hareket alanını kapsar.","gloss":"uzunluk ve uzaklığa yayılma","neighbor_only":"Komşu dal, uzun insanı, uçsuz bucaksız yeri ve uzun süren işleri özel kullanımlar olarak kapsar.","neighbor_ref":"root_001402/B009","relation_type":"near_synonym","shared_zone":"İki dal mekânsal uzaklık, uzunluk ve bir işin sürmesi alanında örtüşür."}],"source_phrase_ar":"هذا المكان أنفس من ذاك أي أبعد شيئا (ayn); أنت في نفس من أمرك أي في سعة ولك في هذا الأمر نفسة أي مهلة (sihah); هذا المنزل أنفس أي أبعد وكتبت كتابا نفسا أي طويلا وزد في أجلي نفسا وبين الفريقين نفس أي متسع (tahdhib)","source_summary":"Kaynaklar uzaklık, açıklık, uzunluk, ek süre ve işte hareket alanını sınırlar arasındaki payın genişlemesi altında birleştirir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه السعة في الأمر، والفسحة، والمهلة، وطول الأجل أو النهار أو الكتاب، وبعد المنزل واتساع ما بين الفريقين.","what_is_not_ar":"ليس هو تفريج الكربة المخصوص ولا تنفس الصبح من حيث الانفلاق إلا إن كان المراد مطلق الامتداد."},"support_links":[]},{"boundary":"Adlandırma eski bahis oyunundaki belirli oka aittir; temel sıra beşinci, kayıtlı karşı görüş dördüncüdür.","branch_kind":"bare","branch_ref":"root_001533/B016","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:7:1:2","qac_word_ref":"91:7:1","surface_ar":"نَفْسٍ"}],"gloss":"eski bahis oyunundaki beşinci pay oku","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eski bahis oyunundaki beşinci pay oku olarak ve beş payla tanımlanır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı toplu kaynak kaydında okun dördüncü sırada olduğu yönünde karşı bir aktarım bulunur."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli oyun okunun baskın aktarımdaki sırası ve pay değeri kastedildiğinde uygundur.","boundary_detail":"Adlandırma eski bahis oyunundaki belirli oka aittir; temel sıra beşinci, kayıtlı karşı görüş dördüncüdür.","branch_image_ar":"النافس سهم الميسر الخامس","concept_gloss":"eski bahis oyunundaki beşinci pay oku","contextual_glosses":[{"applicability":"Sıra konusundaki karşı aktarım özellikle belirtilirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli oyun okunu ve dördüncü sıra karşı aktarımını korur."},"facet_ids":["F002"],"text":"dördüncü sayıldığı da aktarılan oyun oku","usage_role":"explanatory"}],"definition":"Eski bir bahis oyununda kullanılan, çoğunluk aktarımına göre beşinci sıradaki ve beş pay taşıyan oktur. Başka bir aktarım onu dördüncü sıraya koyar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eski bahis oyunundaki beşinci pay oku olarak ve beş payla tanımlanır."},{"facet_id":"F002","role":"source_variant","statement":"Aynı toplu kaynak kaydında okun dördüncü sırada olduğu yönünde karşı bir aktarım bulunur."}],"identity_rationale":"Kaynak ifadesinin baskın bildirimi, belirli bahis okunun beşinci sırada olduğu ve beş pay taşıdığı yönündedir. Aynı toplu iddiada dördüncü sıra biçiminde bir aktarım da bulunduğu için sıra tartışmasız gösterilemez.","lexical_glosses":[{"lexical_unit_id":"lu_043","rendering_kind":"ordinary","target_gloss":"eski bahis oyunundaki beşinci pay oku; bir aktarıma göre dördüncü ok"}],"lexicalization_note":"Çıplak biçim yalnızca eski bahis oyunundaki belirli pay okunu adlandırır; kişi ya da değer yarışması anlamı taşımaz.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi; genel oyun oku komşusu, özel sıra ve pay değerinin dalı nasıl daralttığını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sıra ve pay değeriyle belirlenen özel oktur; komşu dal ise herhangi bir oyun okunu veya işlenmemiş ok gövdesini anlatır.","focus_only":"Odak dal, belirli sıraya ve beş pay değerine sahip tek bir oyun okunu adlandırır.","gloss":"oyun oku ve çıplak ok gövdesi","neighbor_only":"Komşu dal, henüz uç ve tüy takılmamış ok gövdesini ve oyun oklarının herhangi birini genel olarak kapsar.","neighbor_ref":"root_001203/B007","relation_type":"near_neighbor","shared_zone":"İki dal da eski bahis oyununda kullanılan ok biçimli araç alanında kesişir."}],"source_phrase_ar":"النافس الخامس من القداح (ayn); النافس الخامس من سهام الميسر ويقال هو الرابع (sihah); النافس الخامس من قداح الميسر وفيه خمسة فروض (tahdhib)","source_summary":"Toplu kaynak kaydı belirli oyun okunu çoğunlukla beşinci sıra ve beş payla tanımlar; bunun yanında dördüncü sıra aktarımını da korur.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه النافس اسما لقدح من قداح الميسر، خاصة الخامس على نص أكثر المصادر، مع التنبيه إلى قول الرابع في Sihah.","what_is_not_ar":"ليس هو العائن ولا المتنافس في القيمة."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["91:7:1"],"branch_refs":[],"candidate_id":"cand_f97b195e114d2cc1e477","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:7:1:cosmos-to-self-pivot","source_type":"word_analysis","support_ids":["sup_7a246b5a2f9faba0c0e2","sup_97eece20e105b8ac4d77"],"title":"oath chain pivots from cosmos to self","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:1","qac_refs":["91:7:1:1"],"status":"accepted"}},{"anchor_refs":["91:7:1"],"branch_refs":[],"candidate_id":"cand_070fc6c1bc01a3468ee1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:7:1:oath-force","source_type":"word_analysis","support_ids":["sup_97eece20e105b8ac4d77","sup_ead1ff6f85b775179361"],"title":"initial particle renews oath force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:1","qac_refs":["91:7:1:1"],"status":"accepted"}},{"anchor_refs":["91:7:1"],"branch_refs":[],"candidate_id":"cand_95dd80b6dbfcb61177d4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:7:1:two-beat-cadence","source_type":"word_analysis","support_ids":["sup_97eece20e105b8ac4d77","sup_f6b6eca901b84207d711"],"title":"two short openings frame the ayah","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:1","qac_refs":["91:7:1:1"],"status":"accepted"}},{"anchor_refs":["91:7:2"],"branch_refs":[],"candidate_id":"cand_66fb9f280aa3a0b0d6d2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"91:7:2:audible-indefinite-closure","source_type":"word_analysis","support_ids":["sup_1c997a0c3859464fd990","sup_5312c6c5e4f509f2f924"],"title":"tanwin sound closes and opens the beat","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:2","qac_refs":["91:7:1:2"],"status":"accepted"}},{"anchor_refs":["91:7:2"],"branch_refs":[],"candidate_id":"cand_47f0a7f54b9a88f99995","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"91:7:2:desire-before-moral-polarity","source_type":"word_analysis","support_ids":["sup_5312c6c5e4f509f2f924","sup_53ba13c31254742e728d"],"title":"desire and will prepare moral polarity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:2","qac_refs":["91:7:1:2"],"status":"accepted"}},{"anchor_refs":["91:7:2"],"branch_refs":[],"candidate_id":"cand_e8d476b6dfefeb0ca43a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"91:7:2:genitive-oath-object","source_type":"word_analysis","support_ids":["sup_12463ff26f4f88396d1a","sup_5312c6c5e4f509f2f924"],"title":"case marks the sworn object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:2","qac_refs":["91:7:1:2"],"status":"accepted"}},{"anchor_refs":["91:7:2"],"branch_refs":[],"candidate_id":"cand_ed402c6a55547e5792bf","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"91:7:2:indefinite-universal-self","source_type":"word_analysis","support_ids":["sup_5312c6c5e4f509f2f924","sup_68a2ac2e8066305c5652"],"title":"indefinite singular universalizes the self","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:2","qac_refs":["91:7:1:2"],"status":"accepted"}},{"anchor_refs":["91:7:2"],"branch_refs":[],"candidate_id":"cand_257f798d6d738c2e8cd5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"91:7:2:later-ethical-echoes","source_type":"word_analysis","support_ids":["sup_51ff4bca9527aad1d464","sup_5312c6c5e4f509f2f924"],"title":"the sworn self returns as ethical object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:2","qac_refs":["91:7:1:2"],"status":"accepted"}},{"anchor_refs":["91:7:2"],"branch_refs":[],"candidate_id":"cand_6eba1c9e2c9080debd1b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"91:7:2:living-moral-polysemy","source_type":"word_analysis","support_ids":["sup_5312c6c5e4f509f2f924","sup_6da6724b3e16b5a16ac1"],"title":"selfhood carries breath and desire pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:2","qac_refs":["91:7:1:2"],"status":"accepted"}},{"anchor_refs":["91:7:2"],"branch_refs":[],"candidate_id":"cand_9d1527598601fa3ba1df","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"91:7:2:nominal-entity-not-breathing-action","source_type":"word_analysis","support_ids":["sup_5312c6c5e4f509f2f924","sup_a4798ce67f0c0d271efb"],"title":"nominal form selects the self as entity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:2","qac_refs":["91:7:1:2"],"status":"accepted"}},{"anchor_refs":["91:7:2"],"branch_refs":[],"candidate_id":"cand_dbec46c7c8b8fd750156","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"91:7:2:object-of-proportioning-and-ethics","source_type":"word_analysis","support_ids":["sup_5312c6c5e4f509f2f924","sup_7f018cf5c184f98e7ef4"],"title":"the noun anchors later feminine suffixes","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:2","qac_refs":["91:7:1:2"],"status":"accepted"}},{"anchor_refs":["91:7:2"],"branch_refs":[],"candidate_id":"cand_d9402ec320448a8d745f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"91:7:2:soul-and-proportioning-pair","source_type":"word_analysis","support_ids":["sup_5312c6c5e4f509f2f924","sup_9f01563e6a6cea65b5de"],"title":"the self is named through its shaping relation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:2","qac_refs":["91:7:1:2"],"status":"accepted"}},{"anchor_refs":["91:7:2"],"branch_refs":[],"candidate_id":"cand_8e9b35df97038cf9c1e4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"91:7:2:surah-ethical-pivot","source_type":"word_analysis","support_ids":["sup_2f88af597b225ca672d6","sup_5312c6c5e4f509f2f924"],"title":"cosmic sequence turns toward ethics","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:2","qac_refs":["91:7:1:2"],"status":"accepted"}},{"anchor_refs":["91:7:3"],"branch_refs":[],"candidate_id":"cand_583ad61560ed41354eb1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:7:3:hinge-to-shaping-relation","source_type":"word_analysis","support_ids":["sup_205efa26a407054c5164","sup_bbabb6964b83ff18f8fe"],"title":"hinge moves from entity to relation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:3","qac_refs":["91:7:2:1"],"status":"accepted"}},{"anchor_refs":["91:7:3"],"branch_refs":[],"candidate_id":"cand_6a1ef9b1c56d21fe3e3b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:7:3:paired-without-collapse","source_type":"word_analysis","support_ids":["sup_205efa26a407054c5164","sup_78fb17020468aff902da"],"title":"coordination pairs without apposition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:3","qac_refs":["91:7:2:1"],"status":"accepted"}},{"anchor_refs":["91:7:3"],"branch_refs":[],"candidate_id":"cand_7c6b90c3f392adf5971a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:7:3:second-oath-renewal","source_type":"word_analysis","support_ids":["sup_205efa26a407054c5164","sup_e645d49a00917656f9af"],"title":"second particle renews oath force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:3","qac_refs":["91:7:2:1"],"status":"accepted"}},{"anchor_refs":["91:7:4"],"branch_refs":[],"candidate_id":"cand_a2d6edf115604438ad24","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:7:4:adjacent-ma-clause-template","source_type":"word_analysis","support_ids":["sup_835ce882264422075e6b","sup_e8c5de95f8143f157e9b"],"title":"mā-clause repeats the nearby oath template","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:4","qac_refs":["91:7:2:2"],"status":"accepted"}},{"anchor_refs":["91:7:4"],"branch_refs":[],"candidate_id":"cand_372be2eac12e3d5e0b1a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:7:4:masdariyya-process-reading","source_type":"word_analysis","support_ids":["sup_e8c5de95f8143f157e9b","sup_f34b4a2dfdc466bf8adc"],"title":"masdariyya reading makes the act oath-worthy","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:4","qac_refs":["91:7:2:2"],"status":"accepted"}},{"anchor_refs":["91:7:4"],"branch_refs":[],"candidate_id":"cand_59d497532e3bae426fd0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:7:4:productive-ambiguity","source_type":"word_analysis","support_ids":["sup_8104011e4fd3742311c3","sup_e8c5de95f8143f157e9b"],"title":"one surface holds agent and act","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:4","qac_refs":["91:7:2:2"],"status":"accepted"}},{"anchor_refs":["91:7:4"],"branch_refs":[],"candidate_id":"cand_4efab3407c708944bd19","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:7:4:relative-head-reading","source_type":"word_analysis","support_ids":["sup_301b45e2e1fc030b5c3b","sup_e8c5de95f8143f157e9b"],"title":"relative reading makes a compact clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:4","qac_refs":["91:7:2:2"],"status":"accepted"}},{"anchor_refs":["91:7:4"],"branch_refs":[],"candidate_id":"cand_3f56f25cea1e57b7aeff","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:7:4:uninflected-nonspecified-form","source_type":"word_analysis","support_ids":["sup_182738efcd7836b43387","sup_e8c5de95f8143f157e9b"],"title":"uninflected form keeps the referent open","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:4","qac_refs":["91:7:2:2"],"status":"accepted"}},{"anchor_refs":["91:7:4"],"branch_refs":[],"candidate_id":"cand_1225659a8f5a90d44fba","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:7:4:wa-ma-oath-onset","source_type":"word_analysis","support_ids":["sup_112b0fc2d238f08a604f","sup_e8c5de95f8143f157e9b"],"title":"attached onset compresses oath and ambiguity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:4","qac_refs":["91:7:2:2"],"status":"accepted"}},{"anchor_refs":["91:7:5"],"branch_refs":[],"candidate_id":"cand_cb46c92cd7506303cd61","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"91:7:5:active-subject-through-ma","source_type":"word_analysis","support_ids":["sup_65c7ebd812ad0da4eb1f","sup_87e2ebd4650f0d298980"],"title":"active form preserves a shaping source","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:5","qac_refs":["91:7:3:1","91:7:3:2"],"status":"accepted"}},{"anchor_refs":["91:7:5"],"branch_refs":[],"candidate_id":"cand_1611838720f806361c57","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"91:7:5:balance-calibration-field","source_type":"word_analysis","support_ids":["sup_6fc043f5cac3884f0b90","sup_87e2ebd4650f0d298980"],"title":"root image gives balanced calibration","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:5","qac_refs":["91:7:3:1","91:7:3:2"],"status":"accepted"}},{"anchor_refs":["91:7:5"],"branch_refs":[],"candidate_id":"cand_8f84495218bd3f898d16","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"91:7:5:clause-closing-oath-beat","source_type":"word_analysis","support_ids":["sup_5d777d99d16fd8976fb0","sup_87e2ebd4650f0d298980"],"title":"the ayah closes on performed formation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:5","qac_refs":["91:7:3:1","91:7:3:2"],"status":"accepted"}},{"anchor_refs":["91:7:5"],"branch_refs":[],"candidate_id":"cand_df4c1ec85d28a930a881","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"91:7:5:completed-baseline-before-ethics","source_type":"word_analysis","support_ids":["sup_87e2ebd4650f0d298980","sup_b9243fc4acdf7f9d1610"],"title":"perfect aspect gives completed moral architecture","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:5","qac_refs":["91:7:3:1","91:7:3:2"],"status":"accepted"}},{"anchor_refs":["91:7:5"],"branch_refs":[],"candidate_id":"cand_890c671259e6db0d2ebc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"91:7:5:creation-proportioning-echoes","source_type":"word_analysis","support_ids":["sup_87e2ebd4650f0d298980","sup_d524571775724538d3fe"],"title":"creation echoes move inward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:5","qac_refs":["91:7:3:1","91:7:3:2"],"status":"accepted"}},{"anchor_refs":["91:7:5"],"branch_refs":[],"candidate_id":"cand_093e8965979bac47f90f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"91:7:5:direct-transitive-compression","source_type":"word_analysis","support_ids":["sup_3d951cd6aac9cfe96734","sup_87e2ebd4650f0d298980"],"title":"direct object compresses action and patient","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:5","qac_refs":["91:7:3:1","91:7:3:2"],"status":"accepted"}},{"anchor_refs":["91:7:5"],"branch_refs":[],"candidate_id":"cand_0c157836bf50e8420854","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"91:7:5:exclude-self-proportioning","source_type":"word_analysis","support_ids":["sup_87e2ebd4650f0d298980","sup_89e7ca26eaf180eb5350"],"title":"morphology blocks self-evening","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:5","qac_refs":["91:7:3:1","91:7:3:2"],"status":"accepted"}},{"anchor_refs":["91:7:5"],"branch_refs":[],"candidate_id":"cand_305eea41ad0566b1486b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"91:7:5:feminine-object-link","source_type":"word_analysis","support_ids":["sup_87e2ebd4650f0d298980","sup_fc4b01273481a0538d67"],"title":"suffix returns to the soul","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:5","qac_refs":["91:7:3:1","91:7:3:2"],"status":"accepted"}},{"anchor_refs":["91:7:5"],"branch_refs":[],"candidate_id":"cand_8fc41eaad9a73faa5109","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"91:7:5:form-ii-caused-proportioning","source_type":"word_analysis","support_ids":["sup_2dbd2b70d26f9e782300","sup_87e2ebd4650f0d298980"],"title":"Form II makes balance caused","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:5","qac_refs":["91:7:3:1","91:7:3:2"],"status":"accepted"}},{"anchor_refs":["91:7:5"],"branch_refs":[],"candidate_id":"cand_01a077d6412e86126e8f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"91:7:5:local-root-pair","source_type":"word_analysis","support_ids":["sup_87e2ebd4650f0d298980","sup_eea47a5084db049b1a53"],"title":"root pair is grammatically local","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:5","qac_refs":["91:7:3:1","91:7:3:2"],"status":"accepted"}},{"anchor_refs":["91:7:5"],"branch_refs":[],"candidate_id":"cand_1f055a842c2af29354d7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"91:7:5:next-action-on-same-object","source_type":"word_analysis","support_ids":["sup_179434b57aa7459ecaf2","sup_87e2ebd4650f0d298980"],"title":"closing verb launches the next suffix","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:5","qac_refs":["91:7:3:1","91:7:3:2"],"status":"accepted"}},{"anchor_refs":["91:7:5"],"branch_refs":[],"candidate_id":"cand_2bacf4b22953f318479f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"91:7:5:parallel-ha-formative-clauses","source_type":"word_analysis","support_ids":["sup_5e392a10195bd7b00911","sup_87e2ebd4650f0d298980"],"title":"parallel suffix endings bind adjacent acts","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:5","qac_refs":["91:7:3:1","91:7:3:2"],"status":"accepted"}},{"anchor_refs":["91:7:5"],"branch_refs":[],"candidate_id":"cand_db9c3290878683e2bcca","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"91:7:5:physical-to-moral-proportioning","source_type":"word_analysis","support_ids":["sup_87e2ebd4650f0d298980","sup_8edc17476cca19dbbcb7"],"title":"physical balance shifts inward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:5","qac_refs":["91:7:3:1","91:7:3:2"],"status":"accepted"}},{"anchor_refs":["91:7:5"],"branch_refs":[],"candidate_id":"cand_727237920c7215d11b6f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"91:7:5:settled-readiness-pressure","source_type":"word_analysis","support_ids":["sup_3a79a4645e881e7b031d","sup_87e2ebd4650f0d298980"],"title":"settled maturity colors readiness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:5","qac_refs":["91:7:3:1","91:7:3:2"],"status":"accepted"}},{"anchor_refs":["91:7:5"],"branch_refs":[],"candidate_id":"cand_6ce60268fc8e57e93f26","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"91:7:5:sound-and-fasila-landing","source_type":"word_analysis","support_ids":["sup_21801a453a58a1c6536a","sup_87e2ebd4650f0d298980"],"title":"sound makes the proportioning land","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:5","qac_refs":["91:7:3:1","91:7:3:2"],"status":"accepted"}},{"anchor_refs":["91:7:5"],"branch_refs":[],"candidate_id":"cand_5d9f5f761151677c2baf","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"91:7:5:surah-local-opposite-polarity","source_type":"word_analysis","support_ids":["sup_87e2ebd4650f0d298980","sup_f3cca24c34c9a97c37ac"],"title":"same root later levels destructively","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:5","qac_refs":["91:7:3:1","91:7:3:2"],"status":"accepted"}},{"anchor_refs":["91:7:5"],"branch_refs":[],"candidate_id":"cand_ff4f157ff8a2c2728a33","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"91:7:5:taswiya-process-under-ma","source_type":"word_analysis","support_ids":["sup_0f0ef7cc5bdcd865fd97","sup_87e2ebd4650f0d298980"],"title":"process sense remains oath-worthy","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:7:5","qac_refs":["91:7:3:1","91:7:3:2"],"status":"accepted"}},{"anchor_refs":["91:7:1"],"branch_refs":[],"candidate_id":"cand_2e9de8b0610f4c42a3bc","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"91:7:1:2","source_type":"qac_morpheme","support_ids":["sup_382900673f29d7e28d7c"],"title":"QAC root occurrence: ن ف س","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:7:3"],"branch_refs":[],"candidate_id":"cand_2f4c4614de49ad2e841e","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000766"],"scope":"focus_ayah","source_local_id":"91:7:3:1","source_type":"qac_morpheme","support_ids":["sup_0a991b770d7642be5ea4"],"title":"QAC root occurrence: س و ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:7","branch_refs":["root_000766/B002","root_001533/B011"],"candidate_id":"cand_4c482ef9adf32142ff3b","commentary_obligation":"review","hft_ref":"hft_2e929c1eae54a11b183e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_living_whole","source_type":"hft","support_ids":["sup_cb48e2d7a205ef978585"],"title":"baseline_living_whole","trust":"legacy_unbound"},{"anchor_refs":["91:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:7","branch_refs":["root_000766/B001","root_000766/B006","root_001533/B013"],"candidate_id":"cand_4179c04160b9c40cdde6","commentary_obligation":"review","hft_ref":"hft_b7354aacdf6734bb1e5b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_interior_equilibrium","source_type":"hft","support_ids":["sup_051b15c553e5f0bf5c7a"],"title":"baseline_interior_equilibrium","trust":"legacy_unbound"},{"anchor_refs":["91:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:7","branch_refs":["root_000766/B005","root_001533/B005","root_001533/B011"],"candidate_id":"cand_96796df5bfc5071e3f22","commentary_obligation":"review","hft_ref":"hft_504b508979857ddb85f4","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_developmental_completion","source_type":"hft","support_ids":["sup_2f4d9b3d80971f6ff8fe"],"title":"baseline_developmental_completion","trust":"legacy_unbound"},{"anchor_refs":["91:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:7","branch_refs":["root_000766/B004","root_000766/B008","root_001533/B013"],"candidate_id":"cand_74b25835ef8bf1766191","commentary_obligation":"review","hft_ref":"hft_e58d77659fc0aa3eeaac","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_oriented_intent","source_type":"hft","support_ids":["sup_de61a071343d2648747b"],"title":"baseline_oriented_intent","trust":"legacy_unbound"},{"anchor_refs":["91:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:7","branch_refs":["root_000766/B002","root_001533/B001","root_001533/B002","root_001533/B009"],"candidate_id":"cand_b0ce2b6cc5181e104841","commentary_obligation":"review","hft_ref":"hft_f3f14b7c8860704aded0","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_breathing_open_system","source_type":"hft","support_ids":["sup_7476908a9241241c8779"],"title":"baseline_breathing_open_system","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَنَفْسٍۢ وَمَا سَوَّىٰهَا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:7:1:1","qac_word_ref":"91:7:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:7:1:2","qac_word_ref":"91:7:1","root_ar":"ن ف س","surface_ar":"نَفْسٍ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:7:2:1","qac_word_ref":"91:7:2","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:REL|LEM:maA","morpheme_role":"STEM","pos":"REL","qac_ref":"91:7:2:2","qac_word_ref":"91:7:2","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:7:3:1","qac_word_ref":"91:7:3","root_ar":"س و ي","surface_ar":"سَوَّىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:7:3:2","qac_word_ref":"91:7:3","root_ar":"","surface_ar":"هَا"}],"word_analysis_qac_refs":[["91:7:1:1"],["91:7:1:2"],["91:7:2:1"],["91:7:2:2"],["91:7:3:1","91:7:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["91:7:1","91:7:2","91:7:3","91:7:4","91:7:5"]},"focus_surface_evidence":{"arabic_uthmani":"وَنَفْسٍۢ وَمَا سَوَّىٰهَا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:7:1:1","qac_word_ref":"91:7:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:7:1:2","qac_word_ref":"91:7:1","root_ar":"ن ف س","surface_ar":"نَفْسٍ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:7:2:1","qac_word_ref":"91:7:2","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:REL|LEM:maA","morpheme_role":"STEM","pos":"REL","qac_ref":"91:7:2:2","qac_word_ref":"91:7:2","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"سَوَّىٰ","morph_features":"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:7:3:1","qac_word_ref":"91:7:3","root_ar":"س و ي","surface_ar":"سَوَّىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:7:3:2","qac_word_ref":"91:7:3","root_ar":"","surface_ar":"هَا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["91:7:1:1"],["91:7:1:2"],["91:7:2:1"],["91:7:2:2"],["91:7:3:1","91:7:3:2"]],"word_analysis_refs":["91:7:1","91:7:2","91:7:3","91:7:4","91:7:5"],"word_rows":[{"analysis_record_ref":"91:7:1","analytic_gloss_range_en":"oath particle and connector that reopens the qasam frame and governs the following genitive self as a sworn object","analytic_root_gloss_range_en":null,"qac_refs":["91:7:1:1"],"root":{"note":"-"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"91:7:2","analytic_gloss_range_en":"indefinite genitive soul, self, or living moral subject, locally universalized and immediately taken up by feminine suffixes","analytic_root_gloss_range_en":"root range includes breath, life-blood, living self, personhood, inner intent, desire, essence, and related branches; locally the living self and moral interiority are selected while breath and appetite remain image pressure","qac_refs":["91:7:1:2"],"root":{"arabic":"ن ف س","transliteration":"n-f-s"},"surface":{"arabic":"نَفْسٍ","transliteration":"nafsin"}},{"analysis_record_ref":"91:7:3","analytic_gloss_range_en":"second oath particle that coordinates and renews oath force before the ambiguous mā-clause","analytic_root_gloss_range_en":null,"qac_refs":["91:7:2:1"],"root":{"note":"-"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"91:7:4","analytic_gloss_range_en":"ambiguous oath particle or relative/complementizer that can point to the proportioner or convert the following verb phrase into the act of proportioning","analytic_root_gloss_range_en":null,"qac_refs":["91:7:2:2"],"root":{"note":"-"},"surface":{"arabic":"مَا","transliteration":"mā"}},{"analysis_record_ref":"91:7:5","analytic_gloss_range_en":"completed Form II proportioning of the soul through a direct feminine object suffix, with balance, evenness, calibration, and completed formation locally active","analytic_root_gloss_range_en":"root range includes equality, evenness, straightness, completion, settling, maturity, direction, middle or fairness, and specialized branches; locally Form II selects caused proportioning and calibrated completion, while other collocational branches remain background only","qac_refs":["91:7:3:1","91:7:3:2"],"root":{"arabic":"س و ي","transliteration":"s-w-y"},"surface":{"arabic":"سَوَّىٰهَا","transliteration":"sawwāhā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["91:7"],"branch_refs":["root_000766/B002","root_001533/B011"],"candidate_id":"cand_4c482ef9adf32142ff3b","evidence_scope":"focus_ayah","hft_ref":"hft_2e929c1eae54a11b183e","item_id":"baseline_living_whole","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_living_whole","support_id":"sup_cb48e2d7a205ef978585"},{"anchor_refs":["91:7"],"branch_refs":["root_000766/B001","root_000766/B006","root_001533/B013"],"candidate_id":"cand_4179c04160b9c40cdde6","evidence_scope":"focus_ayah","hft_ref":"hft_b7354aacdf6734bb1e5b","item_id":"baseline_interior_equilibrium","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_interior_equilibrium","support_id":"sup_051b15c553e5f0bf5c7a"},{"anchor_refs":["91:7"],"branch_refs":["root_000766/B005","root_001533/B005","root_001533/B011"],"candidate_id":"cand_96796df5bfc5071e3f22","evidence_scope":"focus_ayah","hft_ref":"hft_504b508979857ddb85f4","item_id":"baseline_developmental_completion","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_developmental_completion","support_id":"sup_2f4d9b3d80971f6ff8fe"},{"anchor_refs":["91:7"],"branch_refs":["root_000766/B004","root_000766/B008","root_001533/B013"],"candidate_id":"cand_74b25835ef8bf1766191","evidence_scope":"focus_ayah","hft_ref":"hft_e58d77659fc0aa3eeaac","item_id":"baseline_oriented_intent","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_oriented_intent","support_id":"sup_de61a071343d2648747b"},{"anchor_refs":["91:7"],"branch_refs":["root_000766/B002","root_001533/B001","root_001533/B002","root_001533/B009"],"candidate_id":"cand_b0ce2b6cc5181e104841","evidence_scope":"focus_ayah","hft_ref":"hft_f3f14b7c8860704aded0","item_id":"baseline_breathing_open_system","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_breathing_open_system","support_id":"sup_7476908a9241241c8779"}],"diagnostics":[],"lane_counts":{"global":11,"macro":15,"micro":5},"packet_summary":{"ayah_count":15,"focus_ref":"91:7","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ت ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000186","furuq_root_norm":"ت ل و","furuq_source_root_norm":"ت ل و","is_dominant":true,"target_occurrences":39,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000185","furuq_root_norm":"ت ل ل","furuq_source_root_norm":"ت ل ل","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["91:1","91:2","91:3","91:4","91:5","91:6","91:7","91:8","91:9","91:10","91:11","91:12","91:13","91:14","91:15"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"91:7","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":11,"source_present":true,"structured_insight_count":20,"unstructured_record_count":0},"identity":{"ayah_ref":"91:7","lane":"micro","linguistic_source_ref":"91:7","surface_ref":"91:7","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"91:7","target_tokens":[["Bir",["91:7:1"]],["cana",["91:7:1"]],["ve",["91:7:2"]],["onu",["91:7:3"]],["biçimlendirene",["91:7:2","91:7:3"]]],"text":"Bir cana ve onu biçimlendirene,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":15,"id":"s091-p01-001-015","label":"Whole surah","number":1,"refs":["91:1","91:2","91:3","91:4","91:5","91:6","91:7","91:8","91:9","91:10","91:11","91:12","91:13","91:14","91:15"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"91:7:3:1","source_type":"qac_morpheme","support_id":"sup_0a991b770d7642be5ea4","text":"{\"lemma_ar\":\"سَوَّىٰ\",\"morph_features\":\"STEM|POS:V|PERF|(II)|LEM:saw~aY`|ROOT:swy|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"91:7:3:1\",\"qac_word_ref\":\"91:7:3\",\"root_ar\":\"س و ي\",\"surface_ar\":\"سَوَّىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:5:taswiya-process-under-ma","source_type":"word_analysis","support_id":"sup_0f0ef7cc5bdcd865fd97","text":"{\"blocking_evidence\":null,\"headline\":\"process sense remains oath-worthy\",\"reader_payoff\":\"The reader sees the proportioning process itself as available within the oath's scope.\",\"reason\":\"The grammar allows maṣdariyya {{ar:مَا}} ({{tr:mā}}), and the verbal noun {{ar:تَسْوِيَة}} ({{tr:taswiya}}) is a supported process expression within the root field.\",\"representative_source_ids\":[\"QS-74a92474\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:4:wa-ma-oath-onset","source_type":"word_analysis","support_id":"sup_112b0fc2d238f08a604f","text":"{\"blocking_evidence\":null,\"headline\":\"attached onset compresses oath and ambiguity\",\"reader_payoff\":\"The reader hears oath renewal and referential openness arrive in one compact onset.\",\"reason\":\"{{ar:وَمَا}} ({{tr:wa-mā}}) is the second oath onset, and attachment evidence identifies the parallel pattern as part of the oath construction.\",\"representative_source_ids\":[\"QF-f3f3b0a5\",\"QB-b1525e4e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:2:genitive-oath-object","source_type":"word_analysis","support_id":"sup_12463ff26f4f88396d1a","text":"{\"blocking_evidence\":null,\"headline\":\"case marks the sworn object\",\"reader_payoff\":\"The reader sees the self formally elevated into the oath's witness field by case and position.\",\"reason\":\"Attachment evidence makes the initial {{ar:وَ}} ({{tr:wa}}) the governing oath particle and {{ar:نَفْسٍ}} ({{tr:nafsin}}) its genitive complement.\",\"representative_source_ids\":[\"QG-f8395d24\",\"QI-40f191b0\",\"QT-cb1a2fda\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:5:next-action-on-same-object","source_type":"word_analysis","support_id":"sup_179434b57aa7459ecaf2","text":"{\"blocking_evidence\":null,\"headline\":\"closing verb launches the next suffix\",\"reader_payoff\":\"The reader follows a serial movement: proportioned it, then inspired it in 91:8.\",\"reason\":\"The same feminine object continues from {{ar:سَوَّىٰهَا}} ({{tr:sawwāhā}}) into the next ayah's suffix sequence.\",\"representative_source_ids\":[\"QT-7fbf1d6e\",\"QT-e6063fef\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:4:uninflected-nonspecified-form","source_type":"word_analysis","support_id":"sup_182738efcd7836b43387","text":"{\"blocking_evidence\":null,\"headline\":\"uninflected form keeps the referent open\",\"reader_payoff\":\"The reader notices that the ambiguity is built into the particle's form, not added by later interpretation.\",\"reason\":\"The particle has no surface gender, number, or person marking, and the supplied guardrail marks its referent as indeterminate.\",\"representative_source_ids\":[\"QS-c85ad3a0\",\"MS-48eafc5f\",\"QF-75a8ca13\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:2:audible-indefinite-closure","source_type":"word_analysis","support_id":"sup_1c997a0c3859464fd990","text":"{\"blocking_evidence\":null,\"headline\":\"tanwin sound closes and opens the beat\",\"reader_payoff\":\"The reader hears a single bounded word that still opens onto a general class of moral subjects.\",\"reason\":\"The noun is singular and indefinite with tanwin, so the form supplies both individual shape and broad reference.\",\"representative_source_ids\":[\"QF-4102508a\",\"QP-a840079a\",\"QF-c8b53bb0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:3","source_type":"word_analysis","support_id":"sup_205efa26a407054c5164","text":"{\"gloss_range\":\"second oath particle that coordinates and renews oath force before the ambiguous mā-clause\",\"prose\":\"The second {{ar:وَ}} ({{tr:wa}}) opens a fresh oath beat instead of turning {{ar:مَا سَوَّىٰهَا}} ({{tr:mā sawwāhā}}) into a loose explanation of {{ar:نَفْسٍ}} ({{tr:nafsin}}). It both coordinates and renews qasam force, so the soul and what proportioned it, or the proportioning itself, stand side by side without collapsing into one apposition. That repeated onset gives the ayah a balanced two-beat cadence: first the self, then the shaping relation that accounts for the self's ordered condition.\",\"root_display\":\"-\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:5:sound-and-fasila-landing","source_type":"word_analysis","support_id":"sup_21801a453a58a1c6536a","text":"{\"blocking_evidence\":null,\"headline\":\"sound makes the proportioning land\",\"reader_payoff\":\"The reader hears the completed proportioning occupy the acoustic landing of the verse.\",\"reason\":\"The surface preserves the doubled {{ar:و}} ({{tr:w}}), long-vowel closure, and final {{ar:هَا}} ({{tr:hā}}) ending that align with the local oath cadence.\",\"representative_source_ids\":[\"QF-f591f200\",\"QP-06d19f69\",\"QP-d5aa1f78\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:5:form-ii-caused-proportioning","source_type":"word_analysis","support_id":"sup_2dbd2b70d26f9e782300","text":"{\"blocking_evidence\":null,\"headline\":\"Form II makes balance caused\",\"reader_payoff\":\"The reader notices that the soul is caused to be proportioned rather than simply becoming even by itself.\",\"reason\":\"QAC identifies the local stem as Form II, and the CRITICAL rows' causative-intensive claim fits the active transitive verb with a direct object.\",\"representative_source_ids\":[\"QF-c05c2e57\",\"MF-26f06da1\",\"QY-0dee2b36\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:2:surah-ethical-pivot","source_type":"word_analysis","support_id":"sup_2f88af597b225ca672d6","text":"{\"blocking_evidence\":null,\"headline\":\"cosmic sequence turns toward ethics\",\"reader_payoff\":\"The reader feels the scale change from external created order to the interior subject of moral outcome.\",\"reason\":\"The ayah places {{ar:نَفْسٍ}} ({{tr:nafsin}}) after the prior oath sequence and before the suffix-linked moral statements in 91:8-10.\",\"representative_source_ids\":[\"MT-fd18aa2c\",\"QB-4a8b1cad\",\"QB-f004e372\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:4:relative-head-reading","source_type":"word_analysis","support_id":"sup_301b45e2e1fc030b5c3b","text":"{\"blocking_evidence\":null,\"headline\":\"relative reading makes a compact clause\",\"reader_payoff\":\"The reader sees the second oath beat as a clause, not just a noun phrase.\",\"reason\":\"Attachment evidence reads {{ar:مَا}} ({{tr:mā}}) as the visible subject of {{ar:سَوَّىٰهَا}} ({{tr:sawwāhā}}) within the subordinate oath element.\",\"representative_source_ids\":[\"QG-7183ef2d\",\"QT-1005acc2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"91:7:1:2","source_type":"qac_morpheme","support_id":"sup_382900673f29d7e28d7c","text":"{\"lemma_ar\":\"نَفْس\",\"morph_features\":\"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"91:7:1:2\",\"qac_word_ref\":\"91:7:1\",\"root_ar\":\"ن ف س\",\"surface_ar\":\"نَفْسٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:5:settled-readiness-pressure","source_type":"word_analysis","support_id":"sup_3a79a4645e881e7b031d","text":"{\"blocking_evidence\":null,\"headline\":\"settled maturity colors readiness\",\"reader_payoff\":\"The reader senses the proportioned soul as made functionally ready, not merely geometrically symmetrical.\",\"reason\":\"V4 supports maturity and settledness elsewhere in the root family, but local grammar selects {{ar:سَوَّىٰهَا}} ({{tr:sawwāhā}}), so the payoff is readiness pressure rather than a replacement sense.\",\"representative_source_ids\":[\"QS-ee713dd9\",\"QS-a155fd3f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:5:direct-transitive-compression","source_type":"word_analysis","support_id":"sup_3d951cd6aac9cfe96734","text":"{\"blocking_evidence\":null,\"headline\":\"direct object compresses action and patient\",\"reader_payoff\":\"The reader feels proportioning land directly on the soul in one compact verb-suffix unit.\",\"reason\":\"The verb instance has a clitic object and no prepositional profile, matching the local direct-object attachment.\",\"representative_source_ids\":[\"QG-99a0ef96\",\"QF-9dff31a6\",\"QI-ed63d450\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:2:later-ethical-echoes","source_type":"word_analysis","support_id":"sup_51ff4bca9527aad1d464","text":"{\"blocking_evidence\":null,\"headline\":\"the sworn self returns as ethical object\",\"reader_payoff\":\"The reader follows the same self from oath dignity into responsibility for purification or burial.\",\"reason\":\"The CRITICAL rows give concrete links to the following suffix chain, including inspiration in 91:8 and purification in 91:9.\",\"representative_source_ids\":[\"MI-0a5950a6\",\"MT-99173495\",\"QE-fc89808e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:2","source_type":"word_analysis","support_id":"sup_5312c6c5e4f509f2f924","text":"{\"gloss_range\":\"indefinite genitive soul, self, or living moral subject, locally universalized and immediately taken up by feminine suffixes\",\"prose\":\"{{ar:نَفْسٍ}} ({{tr:nafsin}}) is the ayah's turn from outer created signs to the living moral subject. Its genitive form makes it the object sworn by under {{ar:وَ}} ({{tr:wa}}), while its indefiniteness lets one singular self stand for any soul rather than one named person; the tanwin gives the first beat a bounded audible close while keeping that reference open. The {{ar:ن ف س}} ({{tr:n-f-s}}) field keeps that self thick: soul, living person, inward intent, desire, and breath-pressure are gathered into one oath noun, so the reader does not reduce the word to a purely abstract faculty or to an action of breathing. The feminine noun also becomes the grammatical anchor for {{ar:سَوَّىٰهَا}} ({{tr:sawwāhā}}) here and the following suffix chain in 91:8-10, where the self that is sworn by is proportioned, inspired toward moral polarity in 91:8, and then purified or buried in 91:9-10.\",\"root_display\":\"{{ar:ن ف س}} ({{tr:n-f-s}})\",\"root_gloss_range\":\"root range includes breath, life-blood, living self, personhood, inner intent, desire, essence, and related branches; locally the living self and moral interiority are selected while breath and appetite remain image pressure\",\"surface_display\":\"{{ar:نَفْسٍ}} ({{tr:nafsin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:2:desire-before-moral-polarity","source_type":"word_analysis","support_id":"sup_53ba13c31254742e728d","text":"{\"blocking_evidence\":null,\"headline\":\"desire and will prepare moral polarity\",\"reader_payoff\":\"The reader sees moral receptivity housed in the whole living self, including desire and will.\",\"reason\":\"V4 supports inwardness, resolve, and desire-adjacent branches, and the same feminine referent is continued into the moral polarity of 91:8; the local word remains soul or self, not desire alone.\",\"representative_source_ids\":[\"QS-b7345a16\",\"QS-f6870e1e\",\"QE-ed6747ba\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:5:clause-closing-oath-beat","source_type":"word_analysis","support_id":"sup_5d777d99d16fd8976fb0","text":"{\"blocking_evidence\":null,\"headline\":\"the ayah closes on performed formation\",\"reader_payoff\":\"The reader hears the oath land on completed proportioning while still waiting for the oath answer beyond the ayah.\",\"reason\":\"The ayah's second beat is a clause completed by the final verb, and the larger qasam sequence continues toward its later answer.\",\"representative_source_ids\":[\"QT-d45874cb\",\"QG-9691c950\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:5:parallel-ha-formative-clauses","source_type":"word_analysis","support_id":"sup_5e392a10195bd7b00911","text":"{\"blocking_evidence\":null,\"headline\":\"parallel suffix endings bind adjacent acts\",\"reader_payoff\":\"The reader hears earth-spreading and soul-proportioning as parallel acts while keeping their objects distinct.\",\"reason\":\"The adjacent oath clauses share a {{ar:مَا}} ({{tr:mā}}) plus perfect verb plus {{ar:هَا}} ({{tr:hā}}) template, though the pronoun antecedents differ between 91:6 and 91:7.\",\"representative_source_ids\":[\"QB-e3dc16a4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:5:active-subject-through-ma","source_type":"word_analysis","support_id":"sup_65c7ebd812ad0da4eb1f","text":"{\"blocking_evidence\":null,\"headline\":\"active form preserves a shaping source\",\"reader_payoff\":\"The reader notices a distinction between shaper and shaped without forcing a named subject into the Arabic.\",\"reason\":\"Attachment evidence reads {{ar:مَا}} ({{tr:mā}}) as the visible subject of the active verb, but translation support marks the referent as ambiguous and warns against over-resolution.\",\"representative_source_ids\":[\"QG-6f227294\",\"QG-a9dd250c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:2:indefinite-universal-self","source_type":"word_analysis","support_id":"sup_68a2ac2e8066305c5652","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite singular universalizes the self\",\"reader_payoff\":\"The reader notices that the oath opens onto any soul, not a named or restricted self.\",\"reason\":\"QAC and noun-instance evidence mark {{ar:نَفْسٍ}} ({{tr:nafsin}}) as singular, indefinite, feminine, and genitive under the oath particle.\",\"representative_source_ids\":[\"QG-671f8015\",\"MG-c3319d7d\",\"QY-3f71a9ce\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:2:living-moral-polysemy","source_type":"word_analysis","support_id":"sup_6da6724b3e16b5a16ac1","text":"{\"blocking_evidence\":null,\"headline\":\"selfhood carries breath and desire pressure\",\"reader_payoff\":\"The reader notices that the oath names an embodied living moral subject, not a flattened abstraction called soul.\",\"reason\":\"V4 supports breath, life-self, essence, inwardness, and desire branches for {{ar:ن ف س}} ({{tr:n-f-s}}), while the local noun and oath grammar select the living self rather than activating every branch independently.\",\"representative_source_ids\":[\"QS-1b9ac426\",\"QS-55af093c\",\"MS-012c199c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:5:balance-calibration-field","source_type":"word_analysis","support_id":"sup_6fc043f5cac3884f0b90","text":"{\"blocking_evidence\":null,\"headline\":\"root image gives balanced calibration\",\"reader_payoff\":\"The reader sees the soul as made into an ordered equilibrium, not merely produced.\",\"reason\":\"V4 supports equality, internal straightness, sound completion, middle-point, and evenness branches for {{ar:س و ي}} ({{tr:s-w-y}}), and the local Form II verb applies that field to the soul.\",\"representative_source_ids\":[\"QS-1aab9477\",\"QS-26a0f9ee\",\"QS-27d13aa3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:3:paired-without-collapse","source_type":"word_analysis","support_id":"sup_78fb17020468aff902da","text":"{\"blocking_evidence\":null,\"headline\":\"coordination pairs without apposition\",\"reader_payoff\":\"The reader holds the soul and its proportioning relation together while still distinguishing them.\",\"reason\":\"The conjunction joins the two elements in one oath sequence, but the separate onset prevents {{ar:مَا سَوَّىٰهَا}} ({{tr:mā sawwāhā}}) from being only a restatement of {{ar:نَفْسٍ}} ({{tr:nafsin}}).\",\"representative_source_ids\":[\"QS-0e15c5fb\",\"QS-fdd143a9\",\"QT-d923fa28\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:1:cosmos-to-self-pivot","source_type":"word_analysis","support_id":"sup_7a246b5a2f9faba0c0e2","text":"{\"blocking_evidence\":null,\"headline\":\"oath chain pivots from cosmos to self\",\"reader_payoff\":\"The reader sees the self as the climax of the preceding witness sequence rather than as a new topic after the cosmos.\",\"reason\":\"The discourse reference identifies the near-verbatim oath pattern as a continued construction, anchored earlier in the surah at 91:5.\",\"representative_source_ids\":[\"MG-e4cdaaea\",\"MT-9c8700c4\",\"QB-94c214ce\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:2:object-of-proportioning-and-ethics","source_type":"word_analysis","support_id":"sup_7f018cf5c184f98e7ef4","text":"{\"blocking_evidence\":null,\"headline\":\"the noun anchors later feminine suffixes\",\"reader_payoff\":\"The reader tracks one feminine referent from oath object to proportioned object and then into moral inspiration.\",\"reason\":\"Attachment evidence strongly licenses {{ar:نَفْسٍ}} ({{tr:nafsin}}) as the antecedent of the feminine suffix in {{ar:سَوَّىٰهَا}} ({{tr:sawwāhā}}), and translation support recommends reading the next ayah's suffixes in that window.\",\"representative_source_ids\":[\"QG-07e6d01d\",\"QI-1e475c3d\",\"QB-a78b8d87\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:4:productive-ambiguity","source_type":"word_analysis","support_id":"sup_8104011e4fd3742311c3","text":"{\"blocking_evidence\":null,\"headline\":\"one surface holds agent and act\",\"reader_payoff\":\"The reader feels the oath hold the proportioner and the proportioning together without choosing a single explicit referent.\",\"reason\":\"The local evidence marks {{ar:مَا}} ({{tr:mā}}) as grammatically ambiguous and specifically warns that naming the subject may over-resolve the Arabic.\",\"representative_source_ids\":[\"QG-f4df9247\",\"QS-145fa38e\",\"QY-1c8793b6\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:4:adjacent-ma-clause-template","source_type":"word_analysis","support_id":"sup_835ce882264422075e6b","text":"{\"blocking_evidence\":null,\"headline\":\"mā-clause repeats the nearby oath template\",\"reader_payoff\":\"The reader sees the move from earth to soul happen through repeated grammar as well as theme.\",\"reason\":\"The construction repeats the adjacent {{ar:وَمَا}} ({{tr:wa-mā}}) plus perfect-verb pattern, linking the previous earth-spreading oath in 91:6 to this soul-proportioning oath in 91:7.\",\"representative_source_ids\":[\"QB-cad1f3aa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:5","source_type":"word_analysis","support_id":"sup_87e2ebd4650f0d298980","text":"{\"gloss_range\":\"completed Form II proportioning of the soul through a direct feminine object suffix, with balance, evenness, calibration, and completed formation locally active\",\"prose\":\"{{ar:سَوَّىٰهَا}} ({{tr:sawwāhā}}) closes the ayah on action performed directly on the same {{ar:نَفْسٍ}} ({{tr:nafsin}}). The perfect aspect presents the proportioning as completed before 91:8 names the soul's moral inspiration, and the attached {{ar:هَا}} ({{tr:hā}}) keeps the target precise: it is this feminine self, not an unspecified object. The active form keeps shaper and shaped distinct through the ambiguous {{ar:مَا}} ({{tr:mā}}), while the direct verb-suffix unit makes the formative act land immediately on the soul. The {{ar:س و ي}} ({{tr:s-w-y}}) field gives the act a balance image - evenness, straightness, completion, calibration, and a middle point through {{ar:سَوَاء}} ({{tr:sawāʾ}}) - while Form II makes that equilibrium caused and deliberate rather than self-generated, a ready functional coherence rather than only external symmetry. The maṣdariyya possibility in {{ar:مَا}} ({{tr:mā}}) lets {{ar:تَسْوِيَة}} ({{tr:taswiya}}), the act of proportioning, remain oath-worthy alongside the proportioner. The word also sets up the next action on the same feminine object in 91:8, leaves the larger oath chain waiting for its answer, parallels the adjacent earth-spreading clause through a matching perfect verb plus {{ar:هَا}} ({{tr:hā}}) ending, and echoes both constructive formation in 82:7 and 87:2 and opposite-polarity leveling in 91:14.\",\"root_display\":\"{{ar:س و ي}} ({{tr:s-w-y}})\",\"root_gloss_range\":\"root range includes equality, evenness, straightness, completion, settling, maturity, direction, middle or fairness, and specialized branches; locally Form II selects caused proportioning and calibrated completion, while other collocational branches remain background only\",\"surface_display\":\"{{ar:سَوَّىٰهَا}} ({{tr:sawwāhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:5:exclude-self-proportioning","source_type":"word_analysis","support_id":"sup_89e7ca26eaf180eb5350","text":"{\"blocking_evidence\":null,\"headline\":\"morphology blocks self-evening\",\"reader_payoff\":\"The reader avoids reading the soul as autonomously balancing itself in this clause.\",\"reason\":\"The local surface is active transitive Form II with a direct feminine object, not an intransitive Form I description of the soul becoming even.\",\"representative_source_ids\":[\"QF-7fffe77c\",\"QF-0377f3e8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:5:physical-to-moral-proportioning","source_type":"word_analysis","support_id":"sup_8edc17476cca19dbbcb7","text":"{\"blocking_evidence\":null,\"headline\":\"physical balance shifts inward\",\"reader_payoff\":\"The reader sees cosmic or bodily order transposed into the soul's inner architecture.\",\"reason\":\"The local object is {{ar:نَفْسٍ}} ({{tr:nafsin}}), so evenness and proportioning branches are applied to a moral self rather than to external geometry alone.\",\"representative_source_ids\":[\"QS-6cb9999d\",\"MS-018cdd7b\",\"QB-ad232413\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:1","source_type":"word_analysis","support_id":"sup_97eece20e105b8ac4d77","text":"{\"gloss_range\":\"oath particle and connector that reopens the qasam frame and governs the following genitive self as a sworn object\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) does more than add another item. It renews the oath frame and makes {{ar:نَفْسٍ}} ({{tr:nafsin}}) the governed sworn object, so the ayah crosses from the cosmic sequence of 91:1-6 into the self without starting a detached sentence. The single attached particle also preserves the speed of the oath series: a suppressed oath act is felt through case and position rather than stated in a separate verb. Because a second {{ar:وَ}} ({{tr:wa}}) soon opens {{ar:وَمَا سَوَّىٰهَا}} ({{tr:wa-mā sawwāhā}}), the first onset helps the listener hear the ayah as two compact oath beats, with the soul brought into the same witness field as the sun, sky, and earth.\",\"root_display\":\"-\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:2:soul-and-proportioning-pair","source_type":"word_analysis","support_id":"sup_9f01563e6a6cea65b5de","text":"{\"blocking_evidence\":null,\"headline\":\"the self is named through its shaping relation\",\"reader_payoff\":\"The reader sees the self introduced relationally: the ayah names the soul and immediately names its proportioning.\",\"reason\":\"The second oath element {{ar:مَا سَوَّىٰهَا}} ({{tr:mā sawwāhā}}) is conjoined with {{ar:نَفْسٍ}} ({{tr:nafsin}}), and the verb's suffix resumes that same noun.\",\"representative_source_ids\":[\"QI-251fe02b\",\"MI-72255183\",\"QT-a5d1f5da\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:2:nominal-entity-not-breathing-action","source_type":"word_analysis","support_id":"sup_a4798ce67f0c0d271efb","text":"{\"blocking_evidence\":null,\"headline\":\"nominal form selects the self as entity\",\"reader_payoff\":\"The reader notices that breath-pressure supports living selfhood while the local form still presents a moral entity.\",\"reason\":\"The local form is a noun abstract, and V4 breath branches can enrich the living-self image without changing the surface into an action of breathing.\",\"representative_source_ids\":[\"QF-427a9462\",\"QS-440b43c4\",\"ME-0ba92a71\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:5:completed-baseline-before-ethics","source_type":"word_analysis","support_id":"sup_b9243fc4acdf7f9d1610","text":"{\"blocking_evidence\":null,\"headline\":\"perfect aspect gives completed moral architecture\",\"reader_payoff\":\"The reader sees the soul's balanced structure as already installed before 91:8 names its moral alternatives.\",\"reason\":\"QAC marks the verb as perfect Form II, and the same feminine object is continued into the following moral sequence in 91:8.\",\"representative_source_ids\":[\"QG-55dd148c\",\"MG-be651998\",\"QB-61757e6f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:3:hinge-to-shaping-relation","source_type":"word_analysis","support_id":"sup_bbabb6964b83ff18f8fe","text":"{\"blocking_evidence\":null,\"headline\":\"hinge moves from entity to relation\",\"reader_payoff\":\"The reader hears the ayah turn from the soul as entity to the act or agent that made it balanced.\",\"reason\":\"The particle attaches directly to {{ar:مَا}} ({{tr:mā}}), compressing coordination and oath renewal at the start of the second beat.\",\"representative_source_ids\":[\"QF-83a83e5f\",\"QT-e382663d\",\"QP-b7dd15f4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:5:creation-proportioning-echoes","source_type":"word_analysis","support_id":"sup_d524571775724538d3fe","text":"{\"blocking_evidence\":null,\"headline\":\"creation echoes move inward\",\"reader_payoff\":\"The reader sees a creation-proportioning vocabulary turned inward toward moral architecture.\",\"reason\":\"The CRITICAL rows give concrete parallels in 82:7 and 87:2, while the local object in 91:7 is the soul.\",\"representative_source_ids\":[\"MI-1ea5ec2b\",\"QE-955acbf9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:3:second-oath-renewal","source_type":"word_analysis","support_id":"sup_e645d49a00917656f9af","text":"{\"blocking_evidence\":null,\"headline\":\"second particle renews oath force\",\"reader_payoff\":\"The reader notices that the second beat is itself sworn by, not merely appended as explanation.\",\"reason\":\"Attachment evidence treats {{ar:مَا سَوَّىٰهَا}} ({{tr:mā sawwāhā}}) as a conjoined subordinate oath element alongside {{ar:نَفْسٍ}} ({{tr:nafsin}}).\",\"representative_source_ids\":[\"QG-2bebe84f\",\"MG-e07ea971\",\"QI-fdb078cc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:4","source_type":"word_analysis","support_id":"sup_e8c5de95f8143f157e9b","text":"{\"gloss_range\":\"ambiguous oath particle or relative/complementizer that can point to the proportioner or convert the following verb phrase into the act of proportioning\",\"prose\":\"{{ar:مَا}} ({{tr:mā}}) is the ayah's point of deliberate grammatical openness. As a relative, it heads the clause {{ar:مَا سَوَّىٰهَا}} ({{tr:mā sawwāhā}}), so the oath can point to the one who proportioned the soul. As maṣdariyya, it can turn the verb phrase into the act of proportioning itself. The form gives no gender, number, or person mark that would force one option, and the attachment evidence explicitly warns against naming the referent too tightly. Joined to the preceding {{ar:وَ}} ({{tr:wa}}), the ambiguity remains inside qasam: the solemn witness can hold the proportioner and the proportioning act together without resolving the surface. The same adjacent mā-clause template also carries the movement from earth-spreading in 91:6 to soul-proportioning in 91:7 through repeated grammar, not theme alone.\",\"root_display\":\"-\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مَا}} ({{tr:mā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:1:oath-force","source_type":"word_analysis","support_id":"sup_ead1ff6f85b775179361","text":"{\"blocking_evidence\":null,\"headline\":\"initial particle renews oath force\",\"reader_payoff\":\"The reader notices that the self enters as a sworn witness under qasam grammar, not as a casual continuation.\",\"reason\":\"QAC marks the particle as conjunction and oath particle, and attachment evidence makes {{ar:نَفْسٍ}} ({{tr:nafsin}}) its genitive oath complement with a compressed oath performative.\",\"representative_source_ids\":[\"QG-0d30d41f\",\"QS-8e73969d\",\"QI-a418517a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:5:local-root-pair","source_type":"word_analysis","support_id":"sup_eea47a5084db049b1a53","text":"{\"blocking_evidence\":null,\"headline\":\"root pair is grammatically local\",\"reader_payoff\":\"The reader sees the balance root focused onto the self by grammar, not by loose association.\",\"reason\":\"The object suffix of {{ar:سَوَّىٰهَا}} ({{tr:sawwāhā}}) resumes {{ar:نَفْسٍ}} ({{tr:nafsin}}), so the root-pair claim is licensed by the local clause.\",\"representative_source_ids\":[\"QI-e05d410c\",\"ME-eaf4ff94\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:4:masdariyya-process-reading","source_type":"word_analysis","support_id":"sup_f34b4a2dfdc466bf8adc","text":"{\"blocking_evidence\":null,\"headline\":\"masdariyya reading makes the act oath-worthy\",\"reader_payoff\":\"The reader notices that the oath can solemnize the proportioning process itself, not only the agent behind it.\",\"reason\":\"QAC allows a complementizer or maṣdariyya analysis, and attachment translation support says the target language may need to choose while the Arabic does not.\",\"representative_source_ids\":[\"QG-a386c692\",\"MG-f2066fb3\",\"QI-716cd408\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:5:surah-local-opposite-polarity","source_type":"word_analysis","support_id":"sup_f3cca24c34c9a97c37ac","text":"{\"blocking_evidence\":null,\"headline\":\"same root later levels destructively\",\"reader_payoff\":\"The reader notices that the same root can mark ordered formation in 91:7 and ruinous leveling in 91:14.\",\"reason\":\"The CRITICAL rows give the concrete same-surah contrast between {{ar:سَوَّىٰهَا}} ({{tr:sawwāhā}}) in 91:7 and the same root in destructive leveling at 91:14.\",\"representative_source_ids\":[\"QI-b6478415\",\"QE-a3a5f7de\",\"ME-95a0a115\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:1:two-beat-cadence","source_type":"word_analysis","support_id":"sup_f6b6eca901b84207d711","text":"{\"blocking_evidence\":null,\"headline\":\"two short openings frame the ayah\",\"reader_payoff\":\"The reader hears the ayah as paired oath beats before the second clause has been fully interpreted.\",\"reason\":\"The first {{ar:وَ}} ({{tr:wa}}) attaches directly to the oath noun, and the second opens the parallel {{ar:مَا}} ({{tr:mā}}) clause.\",\"representative_source_ids\":[\"QF-82e977d4\",\"QT-932b2193\",\"QP-5b70bef8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:7:5:feminine-object-link","source_type":"word_analysis","support_id":"sup_fc4b01273481a0538d67","text":"{\"blocking_evidence\":null,\"headline\":\"suffix returns to the soul\",\"reader_payoff\":\"The reader tracks the action as proportioning this same soul, not a general act of shaping.\",\"reason\":\"Attachment evidence strongly licenses the suffix {{ar:هَا}} ({{tr:hā}}) in {{ar:سَوَّىٰهَا}} ({{tr:sawwāhā}}) as a direct object referring back to {{ar:نَفْسٍ}} ({{tr:nafsin}}).\",\"representative_source_ids\":[\"QG-3f50a35e\",\"MG-ecf9aa90\",\"QF-7396ac9f\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَنَفْسٍۢ وَمَا سَوَّىٰهَا","ayah_ref":"91:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000766/B002","root_001533/B011"],"payload":{"activation_trace":[{"branch_id":"B011","mapped_root_id":"root_001533","role":"The living soul-self supplies the animate whole whose constitution is being considered.","root":"ن ف س","source_ref":"91:7","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000766","role":"Internal straightness and sound completion supply the formative operation that integrates the living whole.","root":"س و ي","source_ref":"91:7","source_word_indices":["3"]}],"changed_reading":{"after":"A living whole, together with the act or agent that brought its own constitution into internally sound completion.","before":"A soul, and whoever or whatever made it."},"confidence":"strong","focus_anchor":"The oath joins نَفْسٍ at 91:7[1] to سَوَّىٰهَا at 91:7[3], with the feminine object pronoun returning the configuring act to that same self.","mechanism":"The living soul-self is not presented as a bare unit but together with the act or agent that gives it internal straightness and sound completion. The paired oath therefore foregrounds both an achieved living whole and the formative relation that makes it coherent.","model_id":"baseline_living_whole"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_living_whole","source_type":"hft","support_id":"sup_cb48e2d7a205ef978585","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَنَفْسٍۢ وَمَا سَوَّىٰهَا","ayah_ref":"91:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000766/B001","root_000766/B006","root_001533/B013"],"payload":{"activation_trace":[{"branch_id":"B013","mapped_root_id":"root_001533","role":"The inner mind, thought, and hidden intent make the oath's object an inward field of discernment.","root":"ن ف س","source_ref":"91:7","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000766","role":"Equality and equivalence supply measured relation among distinguishable inward powers.","root":"س و ي","source_ref":"91:7","source_word_indices":["3"]},{"branch_id":"B006","mapped_root_id":"root_000766","role":"The middle, fairness, and even meeting place make equilibrium a relational center rather than featureless sameness.","root":"س و ي","source_ref":"91:7","source_word_indices":["3"]}],"changed_reading":{"after":"The self's hidden cognitive and intentional powers were calibrated into a workable internal relation.","before":"The self was given a generally well-proportioned form."},"confidence":"medium","focus_anchor":"نَفْسٍ can name the inward mind and hidden intent, while سَوَّىٰهَا can activate equivalence and a fair middle.","mechanism":"The focus can describe calibration within an interior field: thought, intention, and discernment are placed into measured relation rather than left as an undifferentiated substance. This is structural equilibrium, not yet a verdict that every impulse is morally equal.","model_id":"baseline_interior_equilibrium"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_interior_equilibrium","source_type":"hft","support_id":"sup_051b15c553e5f0bf5c7a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَنَفْسٍۢ وَمَا سَوَّىٰهَا","ayah_ref":"91:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000766/B005","root_001533/B005","root_001533/B011"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001533","role":"Birth and postpartum emergence provide the developmental starting edge of the self.","root":"ن ف س","source_ref":"91:7","source_word_indices":["1"]},{"branch_id":"B011","mapped_root_id":"root_001533","role":"The living soul-self carries continuity between emergence and later capacity.","root":"ن ف س","source_ref":"91:7","source_word_indices":["1"]},{"branch_id":"B005","mapped_root_id":"root_000766","role":"Reaching full bodily and intellectual maturity supplies the developmental endpoint of taswiya.","root":"س و ي","source_ref":"91:7","source_word_indices":["3"]}],"changed_reading":{"after":"Living emergence was brought toward mature strength, form, and intelligence through a completing process.","before":"The self was fashioned as a finished object."},"confidence":"medium","focus_anchor":"The focus inventory places birth within ن ف س and full maturity within س و ي, allowing سَوَّىٰهَا to span a developmental arc.","mechanism":"The shaping can be read temporally: emergent life is carried toward mature bodily, intellectual, and dispositional capacity. Completion is then a process of becoming able, not merely an instantaneous geometric arrangement.","model_id":"baseline_developmental_completion"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_developmental_completion","source_type":"hft","support_id":"sup_2f4d9b3d80971f6ff8fe","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَنَفْسٍۢ وَمَا سَوَّىٰهَا","ayah_ref":"91:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000766/B004","root_000766/B008","root_001533/B013"],"payload":{"activation_trace":[{"branch_id":"B013","mapped_root_id":"root_001533","role":"Hidden intent supplies the interior source from which direction can arise.","root":"ن ف س","source_ref":"91:7","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_000766","role":"Turning toward a direction supplies an orienting function for the formative act.","root":"س و ي","source_ref":"91:7","source_word_indices":["3"]},{"branch_id":"B008","mapped_root_id":"root_000766","role":"Aiming toward a person or direction sharpens orientation into targetable intention.","root":"س و ي","source_ref":"91:7","source_word_indices":["3"]}],"changed_reading":{"after":"The self was fitted with inward intention and the capacity to orient and aim, without predetermining its chosen target.","before":"The self was made proportionate."},"confidence":"medium","focus_anchor":"The inward-intent branch of ن ف س meets two directional branches of س و ي in the causative focus verb.","mechanism":"Taswiya may include orienting rather than only balancing: an inwardly intending self is furnished with the capacity to turn toward and aim at a direction. The focus then concerns a directional agent, while leaving the direction and its later use open.","model_id":"baseline_oriented_intent"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_oriented_intent","source_type":"hft","support_id":"sup_de61a071343d2648747b","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَنَفْسٍۢ وَمَا سَوَّىٰهَا","ayah_ref":"91:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000766/B002","root_001533/B001","root_001533/B002","root_001533/B009"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001533","role":"Breath leaving the body supplies rhythmic exchange as a literal image of living selfhood.","root":"ن ف س","source_ref":"91:7","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001533","role":"Relief by giving breath and space makes room an enabling condition for continued life.","root":"ن ف س","source_ref":"91:7","source_word_indices":["1"]},{"branch_id":"B009","mapped_root_id":"root_001533","role":"Opening and spreading like breath supply expansion that can remain part of a regulated whole.","root":"ن ف س","source_ref":"91:7","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000766","role":"Sound internal completion contains the respiratory imagery within an organized living system.","root":"س و ي","source_ref":"91:7","source_word_indices":["3"]}],"changed_reading":{"after":"The self is an open, breathing process made sound through regulated expansion, exchange, and relief.","before":"The self is a bounded entity made even."},"confidence":"exploratory","focus_anchor":"Several ن ف س branches image breath, relief through space, and opening or spreading; سَوَّىٰهَا anchors those motions in sound regulation.","mechanism":"The self can be carried as an open living process whose integrity depends on patterned exchange: breath exits, constriction is relieved by room, and openings spread without destroying the whole. Taswiya becomes dynamic regulation of expansion and return rather than immobile symmetry.","model_id":"baseline_breathing_open_system"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_breathing_open_system","source_type":"hft","support_id":"sup_7476908a9241241c8779","trust":"legacy_unbound"}]}
</lane_packet_json>
