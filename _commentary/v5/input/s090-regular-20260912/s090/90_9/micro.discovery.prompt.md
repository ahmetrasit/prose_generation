# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **90:9**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s090-regular-20260912/s090/90_9/micro.discovery.json` and modify nothing
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
  "ayah_ref": "90:9",
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
{"branch_registry":[{"boundary":"Dalın çekirdeği dudak organıdır; kişi nitelemeleri ve dudaksıl sesler bu çekirdeğe bağlı özel kullanımlardır, konuşma eylemi bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000804/B001","candidate_links":[{"candidate_id":"cand_1d72102d119910411acf","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَفَتَيْن","morph_features":"STEM|POS:N|LEM:$afatayon|ROOT:$fh|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:9:2:2","qac_word_ref":"90:9:2","surface_ar":"شَفَتَيْنِ"}],"gloss":"dudak; dudak yapısı ve dudaksıl sesler","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ağzın kenarında bulunan dudak organını ifade eder."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Organ adının çoğul, küçültme ve eski biçimde korunan son sessizli söyleyişleri vardır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişi nitelemelerinde dudakların kapanmaması veya iri olması belirtilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bazı sesler, iki dudakla ya da dudakların katılımıyla çıkarılmaları bakımından sınıflandırılır."}}],"root_ar":"ش ف ه","root_id":"root_000804","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dudak organının çekirdek anlamını ve ona bağlı kişi nitelemeleriyle ses sınıfını birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Dalın çekirdeği dudak organıdır; kişi nitelemeleri ve dudaksıl sesler bu çekirdeğe bağlı özel kullanımlardır, konuşma eylemi bu dala girmez.","branch_image_ar":"الشفة والشفاه","concept_gloss":"dudak; dudak yapısı ve dudaksıl sesler","contextual_glosses":[{"applicability":"Doğrudan ağızdaki organın adlandırıldığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Biçim çeşitlerini, dudak yapısına dayalı kişi nitelemelerini ve ses sınıflandırmasını göstermez.","preserves":"Ağızdaki organı doğrudan ve doğal biçimde karşılar."},"facet_ids":["F001"],"text":"dudak","usage_role":"general"},{"applicability":"Dudaklarını doğal biçimde birleştiremeyen bir kişinin nitelenmesinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dudağın genel organ anlamını, iri dudaklı olmayı ve ses sınıfını dışarıda bırakır.","preserves":"Dudakların kapanmaması biçimindeki fiziksel niteliği korur."},"facet_ids":["F003"],"text":"dudakları kapanmayan","usage_role":"contextual"},{"applicability":"Dudaklarının büyüklüğüyle nitelenen bir kişi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel organ anlamını, dudakların kapanmaması niteliğini ve ses sınıfını kapsamaz.","preserves":"Kişinin dudaklarının iri olması niteliğini korur."},"facet_ids":["F003"],"text":"iri dudaklı","usage_role":"contextual"},{"applicability":"Dudakların katılımıyla çıkarılan belirli harflerin sınıflandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Organın genel anlamını ve kişilerin dudak yapısına ilişkin nitelemeleri kapsamaz.","preserves":"Seslerin dudaklarla çıkarılmasına dayanan sınıflandırmayı korur."},"facet_ids":["F004"],"text":"dudaksıl harfler","usage_role":"contextual"}],"definition":"Çekirdekte, ağzın kenarını oluşturan dudak organı bulunur. Buna bağlı kullanımlar dudakların büyüklüğünü ya da kapanmamasını taşıyan kişi nitelemelerini ve dudaklarla çıkarılan seslerin sınıflandırılmasını kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ağzın kenarında bulunan dudak organını ifade eder."},{"facet_id":"F002","role":"source_variant","statement":"Organ adının çoğul, küçültme ve eski biçimde korunan son sessizli söyleyişleri vardır."},{"facet_id":"F003","role":"specialization","statement":"Kişi nitelemelerinde dudakların kapanmaması veya iri olması belirtilir."},{"facet_id":"F004","role":"associated_use","statement":"Bazı sesler, iki dudakla ya da dudakların katılımıyla çıkarılmaları bakımından sınıflandırılır."}],"identity_rationale":"Kaynak ifadesi, temel olarak ağızdaki dudak organını; bunun çoğul ve küçültme biçimlerini, dudakların yapısına ilişkin nitelemeleri ve dudaklarla çıkarılan sesleri birlikte gösterir. Verilen dal çerçevesi bu anatomik çekirdeği ve ona bağlı kullanımları doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"dudak; ağız kenarındaki organ"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"dudaklar"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"küçük dudak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"organ adının eski son sessizini koruyan biçimi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"dudakları kapanmayan adam"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"iri dudaklı adam"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"dudaksıl harfler; dudaklarla çıkarılan üç belirli harf"}],"lexicalization_note":"Tanım, yalın organ anlamını biçim ve tamlama içindeki dudak yapısı ya da ses üretimi nitelemelerinden ayırır; bu özel kullanımlar yalın anlamın bütünü sayılmaz.","neighbor_coverage_note":"Adayların tümü anatomik kapsam, konuşma, kenar, yüz hareketi ve öteki iç dallar bakımından karşılaştırıldı; burada yalnızca sınırı en açık biçimde keskinleştiren dört ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal anatomik dudak çekirdeğini, dudak yapısını ve dudaksıl sesleri düzenler; komşu dal ise bunlara yüz yüze sözlü iletişim alanını da eklediği için sınırlar tam örtüşmez.","focus_only":"Dudaklarla çıkarılan belirli seslerin sınıflandırılması bu dalda açıkça yer alır.","gloss":"dudak ve ağızdan ağıza konuşma","neighbor_only":"Komşu dal, dudaktan dudağa konuşmayı ve dudağa bağlı başka biçimleri de aynı kapsamda toplar.","neighbor_ref":"root_000806/B004","relation_type":"near_synonym","shared_zone":"Her iki dal dudak organını ve dudakların yapısına ilişkin kişi nitelemelerini kapsar."},{"boundary_match":"field_only","distinction":"Ağız dudağı içeren daha geniş anatomik yapıdır; odak dal bu bütünün kenarındaki organa özgüdür ve iki kavram olağan kullanımda birbirinin yerine geçmez.","focus_only":"Odak dal yalnızca dudağı, dudak yapısını ve dudakların ses üretimindeki rolünü konu eder.","gloss":"ağız ve ağzın açık oluşu","neighbor_only":"Komşu dal bütün ağzı, ağzın açık oluşunu ve ağız adının çeşitli biçimlerini kapsar.","neighbor_ref":"root_001190/B001","relation_type":"same_field","shared_zone":"Dudak ile ağız aynı anatomik bölgede bulunur ve konuşma seslerinin oluşumuna katılır."},{"boundary_match":"partial","distinction":"Odak anlam anatomik organdır; komşu anlam ise nesnelerin sınır ve kenarına uzanan genel bir uzamsal kavramdır, bu nedenle yalnızca biçimsel bir yakınlık vardır.","focus_only":"Odak dal canlıdaki ağız dudağını ve ona bağlı fiziksel ya da sesbilimsel nitelikleri bildirir.","gloss":"bir şeyin kenarı veya ağzı","neighbor_only":"Komşu dal kuyu, çukur veya herhangi bir nesnenin sınırını ve kenarını bildirir.","neighbor_ref":"root_000805/B002","relation_type":"near_neighbor","shared_zone":"Her iki kavram da bir açıklığın ya da yapının sınır oluşturan kenarıyla ilişkilidir."}],"source_phrase_ar":"الشفة حذفت منها الهاء وتصغيرها شفيهة والجميع الشفاه (ayn;tahdhib)؛ رجل أشفى إذا كان لا تنضم شفتاه (sihah)؛ رجل شفاهي عظيم الشفتين (sihah)؛ الحروف الشفهية الباء والفاء والميم (sihah)","source_summary":"Kaynakların ortak anlatımı dudak organını, adın çoğul ve küçültme biçimlerini, dudak yapısına göre kişi nitelemelerini ve dudaklarla çıkarılan belirli seslerin sınıflandırılmasını aynı anlam alanında toplar.","sources":["AY","SI","TA"],"what_is_ar":"الشفة والشفاه، وما يوصف بعظم الشفتين أو عدم انضمامهما، وما نسب إلى الشفتين من الحروف","what_is_not_ar":"ليس الكلام ولا السؤال ولا الثناء"},"support_links":["sup_3421cdd1d27b672b19d1"]},{"boundary":"Yüz yüze sözlü iletişim ana kullanımdır; tek söz anlamı yalnızca verilen olumsuz kalıplara bağlıdır ve genel bir organ anlamı oluşturmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000804/B002","candidate_links":[{"candidate_id":"cand_74fb2f232417f40ef98c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَفَتَيْن","morph_features":"STEM|POS:N|LEM:$afatayon|ROOT:$fh|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:9:2:2","qac_word_ref":"90:9:2","surface_ar":"شَفَتَيْنِ"}],"gloss":"yüz yüze konuşma; olumsuz kalıplarda tek söz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki kişinin karşı karşıya, ağızdan ağıza ve doğrudan konuşmasını ifade eder."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli bir olumsuz kalıpta birine tek söz dahi söylememiş olmayı bildirir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başka bir olumsuz kalıpta birinden tek söz dahi işitmemiş olmayı bildirir."}}],"root_ar":"ش ف ه","root_id":"root_000804","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Doğrudan karşılıklı konuşma ile yalnızca verilen olumsuz yapılardaki tek söz değerini birlikte gösteren üst anlatım olarak kullanılır.","boundary_detail":"Yüz yüze sözlü iletişim ana kullanımdır; tek söz anlamı yalnızca verilen olumsuz kalıplara bağlıdır ve genel bir organ anlamı oluşturmaz.","branch_image_ar":"الكلام من الشفة إلى الشفة","concept_gloss":"yüz yüze konuşma; olumsuz kalıplarda tek söz","contextual_glosses":[{"applicability":"İki kişinin doğrudan karşı karşıya konuştuğu bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Olumsuz kalıplarda tek söz söylememe veya işitmeme kullanımlarını göstermez.","preserves":"Doğrudan ve karşılıklı sözlü iletişim çekirdeğini korur."},"facet_ids":["F001"],"text":"yüz yüze konuşma","usage_role":"general"},{"applicability":"Belirtilen kişiye hiçbir şey söylenmediğini vurgulayan olumsuz kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yüz yüze konuşma çekirdeğini ve birinden söz işitmeme kullanımını kapsamaz.","preserves":"Birine tek söz bile söylememe yönündeki olumsuzluğu korur."},"facet_ids":["F002"],"text":"ona tek söz söylemedim","usage_role":"contextual"},{"applicability":"Belirtilen kişiden hiçbir söz duyulmadığını vurgulayan olumsuz kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yüz yüze konuşma çekirdeğini ve birine söz söylememe kullanımını kapsamaz.","preserves":"Birinden tek söz bile işitmeme yönündeki olumsuzluğu korur."},"facet_ids":["F003"],"text":"ondan tek söz işitmedim","usage_role":"contextual"}],"definition":"Bir kullanım, iki kişinin karşı karşıya ve doğrudan sözlü iletişim kurmasını anlatır. Ayrı olumsuz kalıplarda ise birine tek söz söylememek ya da ondan tek söz bile işitmemek belirtilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki kişinin karşı karşıya, ağızdan ağıza ve doğrudan konuşmasını ifade eder."},{"facet_id":"F002","role":"associated_use","statement":"Belirli bir olumsuz kalıpta birine tek söz dahi söylememiş olmayı bildirir."},{"facet_id":"F003","role":"associated_use","statement":"Başka bir olumsuz kalıpta birinden tek söz dahi işitmemiş olmayı bildirir."}],"identity_rationale":"Kaynak ifadesi iki bağlı kullanımı açıkça destekler: kişilerin ağızdan ağıza, karşı karşıya konuşması ve olumsuz cümlelerde tek bir sözün bile söylenmediğini ya da işitilmediğini bildiren kalıplar. Dal çerçevesi bu ikisini konuşma alanı içinde doğru biçimde bir araya getirir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"yüz yüze konuşma; doğrudan sözlü iletişim"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ona tek söz söylemedim"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ondan tek söz işitmedim"}],"lexicalization_note":"Tanım, türemiş yüz yüze konuşma biçimini iki olumsuz söz kalıbından ayırır; kalıplardaki tek söz anlamı yalın köke genellenmez.","neighbor_coverage_note":"Bütün adaylar konuşmanın yönü, sözün gerçekleşmesi, genel konuşma alanı, dudak anatomisi ve diğer iç dallar bakımından değerlendirildi; en ayırt edici dört komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal konuşmanın katılımcılar arasındaki doğrudan yüz yüze yönünü şart koşar; komşu dalda bu şart yoktur ve tek bir kişinin söz söylemesi de yeterlidir.","focus_only":"Odak dal, konuşmayı özellikle karşı karşıya iletişim olarak kurar ve olumsuz kalıplarda tek söz değerini de içerir.","gloss":"ağzını açıp konuşmak","neighbor_only":"Komşu dal ağzı açıp söz söylemeyi, konuşkanlığı ve konuşmanın niteliğini daha genel biçimde kapsar.","neighbor_ref":"root_001190/B003","relation_type":"near_synonym","shared_zone":"İki dal da ağızdan söz çıkarma ve konuşma eyleminde örtüşür."},{"boundary_match":"partial","distinction":"Konuşma alanında güçlü örtüşme vardır; ancak komşu dal anatomik dudak alanına genişlerken odak dal tek sözlü olumsuz anlatımları ayrıca taşır.","focus_only":"Olumsuz kalıplarda tek söz söylememe veya işitmeme değeri yalnızca odak dalda belirtilir.","gloss":"dudak ve yüz yüze konuşma","neighbor_only":"Komşu dal dudak organını, dudak biçimlerini ve iri dudaklı olmayı da kapsar.","neighbor_ref":"root_000805/B005","relation_type":"near_synonym","shared_zone":"Her iki dal yüz yüze, ağızdan ağıza konuşma anlamını açıkça paylaşır."},{"boundary_match":"partial","distinction":"Genel konuşma kavramı yüz yüze olma veya ağızdan ağıza yönelme şartı taşımaz; odak dal bu ilişki biçimiyle sınırlıdır ve kendine özgü olumsuz kalıplar barındırır.","focus_only":"Odak dal doğrudan yüz yüze konuşmayı ve iki belirli olumsuz söz kalıbını içerir.","gloss":"anlaşılır sözlü iletişim","neighbor_only":"Komşu dal anlaşılır söz üretimini, konuşan kişiyi ve konuşmanın yerini kapsayan genel bir konuşma alanıdır.","neighbor_ref":"root_001316/B001","relation_type":"near_neighbor","shared_zone":"Her iki kavram insanlar arasında söz yoluyla iletişim kurulmasını içerir."},{"boundary_match":"partial","distinction":"Odak dal gerçekleşen sözlü iletişimi esas alır; komşu dal ise konuşma hazırlığına benzeyen ağız hareketini, açık söyleyiş gerçekleşmese bile ifade eder.","focus_only":"Odak dalda anlaşılır sözlerle doğrudan iletişim veya tek sözün yokluğu söz konusudur.","gloss":"konuşur gibi ağzını oynatmak","neighbor_only":"Komşu dalda ağız ya da dudaklar konuşmak üzere hareket eder, fakat açık bir ses veya harf çıkmayabilir.","neighbor_ref":"root_000601/B008","relation_type":"near_neighbor","shared_zone":"İki dal da ağız ve dudakların konuşma amacıyla kullanılmasına dayanır."}],"source_phrase_ar":"المشافهة بالكلام المواجهة من فيك إلى فيه (ayn)؛ المشافهة المخاطبة من فيك إلى فيه (sihah)؛ ما كلمته ببنت شفة أي بكلمة (sihah)؛ ما سمعت منه ذات شفة أي كلمة (tahdhib)","source_summary":"Kaynaklar, doğrudan yüz yüze konuşmayı ortak çekirdek olarak verir; ayrıca iki ayrı olumsuz anlatımda konuşulan ya da işitilen en küçük söz birimini tek söz değeriyle açıklar.","sources":["AY","SI","TA"],"what_is_ar":"المشافهة والمخاطبة من الفم إلى الفم، والكلمة المفردة في عبارات النفي كذات شفة وبنت شفة","what_is_not_ar":"ليس الثناء في الناس ولا كثرة السؤال"},"support_links":["sup_aac6cd799f56f97f1332"]},{"boundary":"Genel meşgul etme çekirdeği korunmalı; ısrarlı isteme, talep altında tükenme, kıtlaşma ve az isteme anlamları yalnızca kendi biçim ve tamlamalarına bağlanmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000804/B003","candidate_links":[{"candidate_id":"cand_f078256199261d22734d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَفَتَيْن","morph_features":"STEM|POS:N|LEM:$afatayon|ROOT:$fh|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:9:2:2","qac_word_ref":"90:9:2","surface_ar":"شَفَتَيْنِ"}],"gloss":"meşgul etme; yoğun taleple tüketme veya kıtlaştırma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiyi veya kaynağı başka bir işten alıkoyacak biçimde meşgul etmeyi ifade eder."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişiye ısrarla istekte bulunup onun elindekini tüketme noktasına kadar yüklenmeyi bildirir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsanların yoğun yönelişi yüzünden suyun veya yiyeceğin azalması, tükenmeye yaklaşması ya da kullanımının kısıtlanmasını anlatır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir kişinin başkalarının yoğun istekleriyle meşgul ve bunalmış durumda bulunmasını anlatır."}},{"facet_id":"F005","role":"specialization","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Özel bir nitelemede kişinin insanlardan az istekte bulunması belirtilir."}}],"root_ar":"ش ف ه","root_id":"root_000804","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel meşguliyet çekirdeğiyle talep baskısının kişide ya da kaynakta doğurduğu tükenme ve azalma sonuçlarını birlikte anlatmak için kullanılır.","boundary_detail":"Genel meşgul etme çekirdeği korunmalı; ısrarlı isteme, talep altında tükenme, kıtlaşma ve az isteme anlamları yalnızca kendi biçim ve tamlamalarına bağlanmalıdır.","branch_image_ar":"الشغل بكثرة الطلب والسؤال","concept_gloss":"meşgul etme; yoğun taleple tüketme veya kıtlaştırma","contextual_glosses":[{"applicability":"Birinin başka bir işe yönelmesini engelleyecek ölçüde uğraştırıldığı yalın bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yoğun isteği, eldekinin tükenmesini, kaynak kıtlığını ve az isteme niteliğini göstermez.","preserves":"Birini başka bir şeyden alıkoyan meşguliyet çekirdeğini korur."},"facet_ids":["F001"],"text":"meşgul etmek","usage_role":"general"},{"applicability":"Bir kişiye ısrarla başvurularak sahip olduğu şeylerin tüketildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel meşguliyet, su ve yiyecek kıtlığı ile az istekte bulunma kullanımlarını kapsamaz.","preserves":"Yoğun isteğin kişiyi bunaltması ve elindekini tüketmesi ilişkisini korur."},"facet_ids":["F002","F004"],"text":"istekleriyle bunaltıp elindekini tüketmek","usage_role":"contextual"},{"applicability":"İnsanların çokça yöneldiği su veya yiyeceğin azaldığı ve tükenmeye yaklaştığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel meşguliyet, kişiye yönelen ısrarlı istek ve az isteme niteliğini kapsamaz.","preserves":"Kalabalık talebin bir kaynağı azaltması veya tükenmeye yaklaştırması sonucunu korur."},"facet_ids":["F003"],"text":"yoğun kullanımla azalmış","usage_role":"contextual"},{"applicability":"Başka insanlardan az talepte bulunan bir kişinin nitelenmesinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Meşgul etme, yoğun taleple tüketme ve kaynak kıtlığı anlamlarını kapsamaz.","preserves":"Kişinin başkalarından az istekte bulunması niteliğini korur."},"facet_ids":["F005"],"text":"insanlardan az isteyen","usage_role":"contextual"}],"definition":"Çekirdek anlam, bir kişiyi ya da kaynağı başka bir uğraştan alıkoyacak biçimde meşgul etmektir. Belirli yapılarda yoğun istek ve başvuru bu meşguliyetin nedeni olur; kişideki varlığı tüketebilir, suyu veya yiyeceği azaltabilir ya da ters yönden birinin insanlardan az istediğini belirtebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiyi veya kaynağı başka bir işten alıkoyacak biçimde meşgul etmeyi ifade eder."},{"facet_id":"F002","role":"specialization","statement":"Bir kişiye ısrarla istekte bulunup onun elindekini tüketme noktasına kadar yüklenmeyi bildirir."},{"facet_id":"F003","role":"extension","statement":"İnsanların yoğun yönelişi yüzünden suyun veya yiyeceğin azalması, tükenmeye yaklaşması ya da kullanımının kısıtlanmasını anlatır."},{"facet_id":"F004","role":"associated_use","statement":"Bir kişinin başkalarının yoğun istekleriyle meşgul ve bunalmış durumda bulunmasını anlatır."},{"facet_id":"F005","role":"specialization","statement":"Özel bir nitelemede kişinin insanlardan az istekte bulunması belirtilir."}],"identity_rationale":"Kaynak ifadesi yoğun istek ve başvurunun kişiyi ya da kaynağı meşgul etmesini, eldeki şeyi tüketmesini ve suyla yiyeceği azaltmasını güçlü biçimde destekler. Bununla birlikte aynı ifade yalın meşguliyet ve birini başka işten alıkoyma anlamlarını da verir; bu yüzden dal yalnızca çok soru sormaya indirgenemez.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"meşguliyet; uğraş"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"beni bundan alıkoydu"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"otlağı ve suyu senin kullanımından alıkoyuyoruz; ikisinde de fazlalık yok"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"ısrarlı istekleriyle beni tüketti"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"insanların üşüşerek azalttığı veya azlığından kullanımı engellenen su"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"insanların üşüştüğü veya çoğu tüketilmiş sular"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"az yiyecek"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"insanların istekleriyle elindekiler tüketilmiş adam"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"çok kalabalık bir ailen oldu ya da soru ve sözle bunaltıldın"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bizden uzak, başkalarının yoğun talepleriyle meşgul"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"insanlardan az isteyen"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"o kişinin iyiliğinden sana düşen hiçbir şeyi meşgul edip tüketmedim"}],"lexicalization_note":"Tanım yalın meşguliyet anlamını ayrı tutar; yoğun talep, tükenme, kıtlık ve az soru sorma değerlerini yalnızca onları taşıyan yapılara bağlar.","neighbor_coverage_note":"Adayların tamamı ısrarın yönü, meşguliyet, ihtiyaç, bağış isteme, tüketim sonucu ve öteki iç dallarla ilişki bakımından incelendi; sınırı en yararlı biçimde gösteren dört karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal ısrarın kendisini ve çeşitli söylem türlerini öne çıkarır; odak dal ise meşgul olma ile eldekinin ya da kaynağın tükenmesi sonucunu yapısal olarak taşır.","focus_only":"Odak dal genel meşgul etmeyi, yoğun talep altında tükenmeyi ve su ya da yiyeceğin azalmasını da kapsar.","gloss":"ısrarla ve tüketircesine isteme","neighbor_only":"Komşu dal ısrarı soru yanında öğüt, talep, konuşma ve çekişme gibi daha geniş eylem türlerine yayar.","neighbor_ref":"root_000344/B002","relation_type":"near_synonym","shared_zone":"Her iki dal sorulan veya talepte bulunulan kişiyi zorlayan yoğun ısrarı içerir."},{"boundary_match":"partial","distinction":"Komşu kavram doğrudan soru sormadaki ısrarla sınırlıdır; odak kavram bu ısrarın kişiyi meşgul etmesi ve elindekini tüketmesi sonuçlarına kadar uzanır.","focus_only":"Odak dal, ısrarın yanı sıra kişinin meşgul edilmesini ve sahip olunan şeyin ya da kaynağın azalmasını içerir.","gloss":"soru sormada ısrar","neighbor_only":null,"neighbor_ref":"root_000567/B006","relation_type":"near_synonym","shared_zone":"İki dal bir kişiye soru veya istekle tekrar tekrar yüklenme alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu dal isteyen kişinin eylemine odaklanır; odak dal ise çoğunlukla talebe maruz kalan kişi veya kaynağın meşgul olması ve azalması sonucunu öne çıkarır.","focus_only":"Odak dal yoğun talebin hedef üzerindeki meşguliyet ve tükenme etkisini, ayrıca az isteme niteliğini bildirir.","gloss":"insanlardan bir şey istemek","neighbor_only":"Komşu dal insanların kendilerinden bağış veya verilecek bir şey isteme eylemini anlatır.","neighbor_ref":"root_001028/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal insanlar arasındaki isteme ve karşı taraftan bir şey talep etme durumuyla ilişkilidir."},{"boundary_match":"partial","distinction":"Odak dal azalmanın nedenini kalabalık talep ve kullanım baskısına bağlar; komşu dal ise yalnızca içeceğin kesilmesi ya da bitmesi sonucunu ifade eder.","focus_only":"Odak dalda azalma insanların yoğun yönelişinden doğar ve suyla yiyeceğe de uygulanabilir.","gloss":"içeceğin tükenmesi","neighbor_only":"Komşu dal içeceğin kesilmesi ya da bütünüyle tükenmesini, yoğun talep koşulu olmadan bildirir.","neighbor_ref":"root_001491/B004","relation_type":"near_neighbor","shared_zone":"İki dal eldeki içilebilir kaynağın azalması veya sona ermesi sonucunda buluşur."}],"source_phrase_ar":"ماء مشفوة أي مطلوب مسؤول وهو الذي كثر عليه الناس وأنفدوه إلا أقله (ayn)؛ طعام مشفوه أي قليل (ayn)؛ الشفه الشغل (sihah)؛ شفهني عن كذا أي شغلني (sihah)؛ خفيف الشفة أي قليل السؤال للناس (sihah)؛ رجل مشفوه إذا كثر سؤال الناس إياه حتى نفذ ما عنده (sihah)؛ ماء مشفوه وهو الذي كثر عليه الناس (tahdhib)؛ ما شفهت عليك من خير فلان شيئا (tahdhib)؛ فلان مشفوة عنا أي مشغول عنا مكثور عليه (tahdhib)؛ كان مشفوها أي كان قليلا (tahdhib)","source_summary":"Toplu kaynak anlatımı genel meşgul etme anlamıyla yoğun talepten doğan yükü birleştirir. Bu yük bir kişiyi başka şeyden alıkoyabilir, elindekini tüketebilir veya su ve yiyeceği azaltabilir; ayrı bir niteleme ise kişinin insanlardan az istekte bulunduğunu bildirir.","sources":["AY","SI","TA"],"what_is_ar":"إلحاح السؤال وكثرة الواردين، وما ينتج عنه من نفاد ما عند الشخص أو قلة الماء والطعام أو شغل المورد والشخص عن غيره","what_is_not_ar":"ليس الشفة العضو ولا المشافهة بالكلام"},"support_links":["sup_f596bfe56fbac6f071b8"]},{"boundary":"Anlam yalnızca verilen yapılarda kişinin toplum içindeki iyi adı ve övgüsüdür; organ adı veya genel bir övme fiili olarak genişletilmez.","branch_kind":"collocation","branch_ref":"root_000804/B004","candidate_links":[{"candidate_id":"cand_17fa6cfc2e668b9f7c36","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَفَتَيْن","morph_features":"STEM|POS:N|LEM:$afatayon|ROOT:$fh|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:9:2:2","qac_word_ref":"90:9:2","surface_ar":"شَفَتَيْنِ"}],"gloss":"insanlar arasındaki iyi ad ve övgü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin toplum içindeki iyi adını, güzel anılışını ve olumlu övgü görmesini bildirir."}}],"root_ar":"ش ف ه","root_id":"root_000804","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Verilen yapılarda bir kişinin toplumsal ününün ve onun hakkındaki övgünün olumlu olduğunu birlikte anlatır.","boundary_detail":"Anlam yalnızca verilen yapılarda kişinin toplum içindeki iyi adı ve övgüsüdür; organ adı veya genel bir övme fiili olarak genişletilmez.","branch_image_ar":"الشفة الحسنة في الناس","concept_gloss":"insanlar arasındaki iyi ad ve övgü","contextual_glosses":[{"applicability":"Bir kişinin toplum içinde iyi tanındığını ve güzel anıldığını bildiren ilk yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin insanlar arasındaki iyi adını ve olumlu anılışını doğal biçimde korur."},"facet_ids":["F001"],"text":"insanlar arasında iyi bir adı var","usage_role":"contextual"},{"applicability":"İnsanların muhatap hakkındaki anış ve övgüsünün olumlu olduğunu bildiren ikinci yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluğun kişi hakkındaki güzel sözünü ve olumlu övgüsünü açıkça korur."},"facet_ids":["F001"],"text":"insanların senin hakkındaki sözü ve övgüsü güzel","usage_role":"contextual"}],"definition":"Belirli yapılarda, bir kişinin insanlar arasında iyi anılması ve onun hakkında güzel sözlerle övgüde bulunulması ifade edilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin toplum içindeki iyi adını, güzel anılışını ve olumlu övgü görmesini bildirir."}],"identity_rationale":"Kaynak ifadesi, bir kişinin insanlar arasındaki iyi anılışını ve onun hakkındaki güzel övgüyü iki yapı üzerinden açıkça bildirir. Dal çerçevesi bu toplumsal değerlendirme anlamını doğru verir ve onu tek söz ya da soru anlamlarıyla karıştırmaz.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"insanlar arasında iyi bir adı ve övgüsü var"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"insanların senin hakkındaki sözü ve övgüsü güzel"}],"lexicalization_note":"Tanım kesin olarak verilen iki yapıya bağlıdır; iyi ün ve övgü anlamı yalın köke veya organ adına taşınmaz.","neighbor_coverage_note":"Tüm adaylar iyi ün, övgü eylemi, onurlu nitelik, toplumsal düşüş ve diğer iç dallar bakımından karşılaştırıldı; en yakın ve sınır açıklayıcı dört ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yapı bağımlı iyi ad ve övgü anlamıyla sınırlıdır; komşu dal buna şeref, yücelik ve toplumsal konum gibi daha geniş değerler ekler.","focus_only":"Odak dal yalnızca verilen yapılarda kişinin insanlar arasındaki iyi anılışını ve övgüsünü bildirir.","gloss":"şeref, ün ve iyi anılma","neighbor_only":"Komşu dal şeref, yücelik, yaygın ün ve iyi anılmanın yanında toplumsal mevkiyi de kapsar.","neighbor_ref":"root_000516/B007","relation_type":"near_synonym","shared_zone":"Her iki dal kişinin toplumdaki olumlu ünü, güzel anılışı ve övgüsü alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu kavramda ünün yaygınlaşması öne çıkar; odak dal için yaygınlık şart değildir ve kişinin hakkındaki güzel övgü de anlamın parçasıdır.","focus_only":"Odak dal güzel anılmanın yanında kişiye yöneltilen olumlu övgüyü de açıkça içerir.","gloss":"yaygın iyi ün","neighbor_only":"Komşu dal iyi ünün insanlar arasında yayılmış olmasını belirgin bir koşul olarak taşır.","neighbor_ref":"root_000890/B002","relation_type":"near_synonym","shared_zone":"İki dal bir kişinin toplum içinde iyi tanınması ve güzel anılması anlamını paylaşır."},{"boundary_match":"partial","distinction":"Odak dal övgüyle birlikte ortaya çıkan toplumsal iyi adı ifade eder; komşu dal ise olumlu nitelikleri yineleyerek övme eyleminin kendisine odaklanır.","focus_only":"Odak dal kişinin insanlar arasındaki yerleşik iyi adını da bildirir.","gloss":"iyilikleri anarak övme","neighbor_only":"Komşu dal kişinin iyi yönlerini tekrar tekrar anarak övme eylemini özellikle belirtir.","neighbor_ref":"root_000208/B010","relation_type":"near_synonym","shared_zone":"Her iki dal kişi hakkında olumlu söz söyleme ve onu güzel biçimde anma alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu kavram etkin ve yükseltilmiş bir övgü eylemidir; odak kavram ise belirli yapılarda kişinin toplumda sahip olduğu iyi anılışı ve olumlu değerlendirmeyi bildirir.","focus_only":"Odak dal toplum içindeki iyi adı ve insanların genel olumlu anışını ifade eder.","gloss":"güçlü övgü ve yüceltme","neighbor_only":"Komşu dal kişiyi en iyi özellikleriyle överek övgüyü yükseltme eylemini anlatır.","neighbor_ref":"root_000933/B002","relation_type":"near_neighbor","shared_zone":"İki dal bir kişi hakkında olumlu ve övücü söz söylenmesi alanında buluşur."}],"source_phrase_ar":"له في الناس شفة أي ثناء حسن (sihah)؛ شفة الناس عليك لحسنة أي ذكرهم لك وثناءهم عليك حسن (tahdhib)","source_summary":"Kaynakların ortak anlamı, kişinin insanlar arasında güzel anılması ve onun hakkındaki söz ile övgünün olumlu olmasıdır.","sources":["SI","TA"],"what_is_ar":"الذكر والثناء الحسن للمرء بين الناس","what_is_not_ar":"ليس الكلمة المفردة ولا السؤال"},"support_links":["sup_0fd8fd3a9ce231928ad3"]},{"boundary":"Bu dal konuşma organı ile onun söyleyiş gücünü kapsar; dil sistemi, güzel konuşma ve dile benzeyen biçimler ayrı dallardadır.","branch_kind":"bare","branch_ref":"root_001355/B001","candidate_links":[{"candidate_id":"cand_1d72102d119910411acf","lane":"micro"},{"candidate_id":"cand_f078256199261d22734d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لِسَان","morph_features":"STEM|POS:N|LEM:lisaAn|ROOT:lsn|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:9:1:2","qac_word_ref":"90:9:1","surface_ar":"لِسَانًا"}],"gloss":"konuşma organı ve söyleyiş gücü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Konuşmada kullanılan, ağız içindeki bilinen organdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Organın kendisinden onunla gerçekleştirilen söyleyiş gücüne de uzanır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Adın hem erkek hem dişi sayılabilmesi ve buna göre değişen çoğul biçimleri sözlük bilgisinin parçasıdır."}}],"root_ar":"ل س ن","root_id":"root_001355","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Organın kendisiyle ondan ayrılmayan konuşma yetisinin birlikte anlatıldığı genel tanımda uygundur.","boundary_detail":"Bu dal konuşma organı ile onun söyleyiş gücünü kapsar; dil sistemi, güzel konuşma ve dile benzeyen biçimler ayrı dallardadır.","branch_image_ar":"اللسان جارحة الكلام","concept_gloss":"konuşma organı ve söyleyiş gücü","contextual_glosses":[{"applicability":"Beden organının açıkça söz konusu olduğu cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":"Türkçede dil sistemi anlamıyla da kullanılabildiği için bağlamsız durumda öteki dalla karışabilir.","fit":"narrowing","loses":"Bağlam desteklemezse organa bağlı söyleyiş gücünü ayrıca belirtmez.","preserves":"Ağız içindeki konuşma organını doğal ve kısa biçimde karşılar."},"facet_ids":["F001"],"text":"dil","usage_role":"contextual"}],"definition":"Ağızda bulunan ve konuşmanın gerçekleşmesini sağlayan organ ile bu organa bağlı söyleyiş gücüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Konuşmada kullanılan, ağız içindeki bilinen organdır."},{"facet_id":"F002","role":"extension","statement":"Organın kendisinden onunla gerçekleştirilen söyleyiş gücüne de uzanır."},{"facet_id":"F003","role":"associated_use","statement":"Adın hem erkek hem dişi sayılabilmesi ve buna göre değişen çoğul biçimleri sözlük bilgisinin parçasıdır."}],"identity_rationale":"Kaynak ifadesi, bilinen konuşma organını ve bu organla gerçekleşen söyleyiş gücünü birlikte verir. Dalın organ, konuşma yetisi, dil bilgisel cinsiyet ve çoğul biçimler çevresindeki sınırı bu ifadeyle tam olarak örtüşür.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"konuşma organı olan dil ve onun söyleyiş gücü"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"konuşma organı anlamındaki dilin çoğulu"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"konuşma organı anlamındaki dilin çoğulu"}],"lexicalization_note":"Çıplak biçim doğrudan konuşma organını ve onun söyleyiş gücünü adlandırır; başka yapılara bağlı anlamlar tanıma katılmaz.","neighbor_coverage_note":"Verilen bütün komşular değerlendirildi; organın işlevi, başka bir ağız organı ve dil sistemiyle karışma ihtimalini en iyi açıklayan üç karşıtlık seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal organın kendisini ve gücünü tanımlar; komşu dal ise aynı organı özellikle söz söyleme aracı olma bakımından adlandırır.","focus_only":"Konuşma organını kendi bedensel kimliğiyle ve ona bağlı söyleyiş gücüyle birlikte kapsar.","gloss":"konuşmanın aracı olan dil","neighbor_only":"Organı yalnızca söz üretmeye yarayan araç olarak adlandıran daha sınırlı bir kullanım sunar.","neighbor_ref":"root_001272/B002","relation_type":"near_synonym","shared_zone":"İki dal da konuşmayı mümkün kılan bedensel dil üzerinde buluşur."},{"boundary_match":"field_only","distinction":"Ortak alan konuşma aygıtıdır; ancak odak dil organına, komşu ise dudaklara ve dudakla ilişkili kullanımlara dayanır.","focus_only":"Ağız içindeki dili ve onun söyleyiş gücünü kapsar.","gloss":"dudak ve yüz yüze söyleşme","neighbor_only":"Dudakları, dudakların özelliklerini ve ağızdan ağıza konuşmayı kapsar.","neighbor_ref":"root_000805/B005","relation_type":"same_field","shared_zone":"Her ikisi de ağız çevresindeki konuşma organları alanındadır."},{"boundary_match":"partial","distinction":"Odak dal bedenseldir; komşu dal organ adından gelişen dil, konuşma ve söz anlamlarını taşır.","focus_only":"Bedensel organı ve bu organın söyleyiş gücünü bildirir.","gloss":"organ olarak dil ve iletişim sistemi olarak dil","neighbor_only":"Bir topluluğun konuşma sistemini, sözü ve bunlardan gelişen haber ya da övgü kullanımlarını bildirir.","neighbor_ref":"root_001355/B006","relation_type":"near_neighbor","shared_zone":"Konuşma organı, konuşulan sistemin adı için anlam aktarımına temel olur."}],"source_phrase_ar":"اللسان معروف وهو مذكر والجمع ألسن (maqayis)؛ اللسان ما ينطق يذكر ويؤنث والألسن والألسنة (ayn)؛ اللسان جارحة الكلام (sihah)؛ اللسان يذكر ويؤنث وجمعه ألسن وألسنة (tahdhib)؛ اللسان الجارحة وقوتها (mufradat)","source_summary":"Kaynaklar, bu anlamı konuşma organı ve onun söyleyiş gücü üzerinde birleştirir; ayrıca adın iki dil bilgisel cinsiyette kullanılabildiğini ve birden çok çoğul biçimi bulunduğunu bildirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اللسان المعروف وجارحة الكلام وقوة النطق به وتذكيره وتأنيثه وجموعه","what_is_not_ar":"ليس اللغة المجردة ولا الفصاحة ولا أخذ الإنسان باللسان ولا الشكل الشبيه باللسان"},"support_links":["sup_3421cdd1d27b672b19d1","sup_f596bfe56fbac6f071b8"]},{"boundary":"Anlam sıradan konuşmayı değil, belirli bir kişiye yöneltilen sataşma, çıkışma veya sözlü saldırıyı gerektirir.","branch_kind":"non_bare","branch_ref":"root_001355/B002","candidate_links":[{"candidate_id":"cand_17fa6cfc2e668b9f7c36","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لِسَان","morph_features":"STEM|POS:N|LEM:lisaAn|ROOT:lsn|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:9:1:2","qac_word_ref":"90:9:1","surface_ar":"لِسَانًا"}],"gloss":"birine sözle sataşma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözün belirli bir kişiye yöneltilmesi ve o kişinin sözle hedef alınmasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem, kişiye sataşma veya çıkışma niteliği taşır; tarafsız konuşma değildir."}}],"root_ar":"ل س ن","root_id":"root_001355","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli bir kişiye yönelen sözlü çıkışma veya saldırının genel karşılığıdır.","boundary_detail":"Anlam sıradan konuşmayı değil, belirli bir kişiye yöneltilen sataşma, çıkışma veya sözlü saldırıyı gerektirir.","branch_image_ar":"الأخذ باللسان","concept_gloss":"birine sözle sataşma","contextual_glosses":[{"applicability":"Sataşmanın sert bir çıkışma veya sözlü baskı biçimi aldığı cümlelerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli kişiye yönelme ile sözlü saldırı niteliğini birlikte korur."},"facet_ids":["F001","F002"],"text":"sözle üzerine gitmek","usage_role":"contextual"}],"definition":"Bir kimseyi diliyle hedef alarak ona sözle sataşmak, çıkışmak veya sözlü biçimde üzerine gitmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözün belirli bir kişiye yöneltilmesi ve o kişinin sözle hedef alınmasıdır."},{"facet_id":"F002","role":"specialization","statement":"Eylem, kişiye sataşma veya çıkışma niteliği taşır; tarafsız konuşma değildir."}],"identity_rationale":"Kaynak ifadesi, bir kimseyi diliyle hedef alıp ona sözle sataşma veya çıkışma eylemini açıkça anlatır. Dal başlığındaki alma sözü düz bir edinme değil, sözlü saldırı ve üzerine gitme olarak anlaşılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"birine sözle sataşmak veya çıkışmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bana sözle sataştı veya üzerime geldi"}],"lexicalization_note":"Anlam belirli eylem yapılarında ve kişi nesnesiyle gerçekleşir; kökün yalın kullanımına genel bir konuşma anlamı olarak taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel hakaret, dedikodu ve suçlamadan ayrımı en açık gösteren iki yakın karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sözle üzerine gitme eylemini genel olarak kapsar; komşu dal ise saldırıyı özellikle yaralayan tek söz imgesiyle sınırlar.","focus_only":"Bir kişiyi dille hedef alma eylemini, belirli bir hakaret türü belirtmeden anlatır.","gloss":"birine sözle saldırmak","neighbor_only":"Tek bir incitici sözle kişiyi yaralama benzetisini öne çıkarır.","neighbor_ref":"root_001490/B002","relation_type":"near_synonym","shared_zone":"İki dal da belirli bir kişiye yönelen incitici sözü anlatır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği kişiye sözle yönelmektir; komşu dalın çekirdeği ise o kişiye bir kusur veya ayıp yüklemektir.","focus_only":"Sataşma ve sözlü çıkışmayı, mutlaka kusur yükleme şartı olmadan kapsar.","gloss":"sözle sataşma ve sözle kusur yükleme","neighbor_only":"Kişiye, onuruna veya inancına sözle kusur yükleme ve kötüleme sonucunu gerektirir.","neighbor_ref":"root_000935/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da söz belirli bir kişiye karşı zarar verici biçimde kullanılır."}],"source_phrase_ar":"لسنته إذا أخذته بلسانك (maqayis)؛ لسن فلان فلانا يلسنه أي أخذه بلسانه (ayn)؛ لسنته إذا أخذته بلسانك (sihah)؛ لسنت الرجل ألسنه لسنا إذا أخذته بلسانك (tahdhib)","source_summary":"Kaynaklar, eylemi bir kişiyi dille hedef alma ve ona sözle sataşma olarak ortak biçimde açıklar.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه لسنت الرجل وتلسنني إذا أخذه أو تعرض له بلسانه","what_is_not_ar":"ليس مطلق الكلام ولا اللغة ولا الفصاحة"},"support_links":["sup_0fd8fd3a9ce231928ad3"]},{"boundary":"Bu dal konuşmanın açıklık, düzgünlük ve ikna gücünü kapsar; konuşma organı ya da belirli bir dil sistemi değildir.","branch_kind":"bare","branch_ref":"root_001355/B003","candidate_links":[{"candidate_id":"cand_17fa6cfc2e668b9f7c36","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لِسَان","morph_features":"STEM|POS:N|LEM:lisaAn|ROOT:lsn|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:9:1:2","qac_word_ref":"90:9:1","surface_ar":"لِسَانًا"}],"gloss":"açık ve etkili konuşma yetkinliği","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Konuşmanın açık, düzgün ve etkili olmasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin sözünü gerekçelerle savunabilme ve tartışmada güçlü olma yetisini de içerir."}}],"root_ar":"ل س ن","root_id":"root_001355","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem anlatım açıklığını hem de güçlü gerekçe sunabilmeyi kapsayan genel karşılıktır.","boundary_detail":"Bu dal konuşmanın açıklık, düzgünlük ve ikna gücünü kapsar; konuşma organı ya da belirli bir dil sistemi değildir.","branch_image_ar":"اللسن والفصاحة","concept_gloss":"açık ve etkili konuşma yetkinliği","contextual_glosses":[{"applicability":"Tartışma gücünden çok anlatım niteliğinin öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güçlü gerekçelerle karşısındakine üstün gelme yetisini açıkça taşımaz.","preserves":"Konuşmanın açıklığını, düzgünlüğünü ve etkileyiciliğini korur."},"facet_ids":["F001"],"text":"güzel ve açık konuşma","usage_role":"contextual"},{"applicability":"Kişinin tartışmada gerekçe üretme ve sözünü savunma gücü vurgulandığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel konuşma açıklığı ve düzgünlüğünü tek başına belirtmez.","preserves":"Gerekçelendirme ve sözle üstün gelme gücünü korur."},"facet_ids":["F002"],"text":"sözü güçlü olmak","usage_role":"contextual"}],"definition":"Sözü açık, düzgün ve etkili biçimde anlatma; gerektiğinde güçlü gerekçelerle karşısındakine üstün gelme yetkinliğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Konuşmanın açık, düzgün ve etkili olmasıdır."},{"facet_id":"F002","role":"specialization","statement":"Kişinin sözünü gerekçelerle savunabilme ve tartışmada güçlü olma yetisini de içerir."}],"identity_rationale":"Kaynak ifadesi güzel ve açık konuşmayı, anlatım açıklığını ve gerekçeyle üstün gelme gücünü aynı yetkinlik alanında birleştirir. Dalın yalnızca organ sahibi olmayı veya bir topluluğun dilini değil, konuşma niteliğini anlatan çerçevesi uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"açık, düzgün ve etkili konuşma yetkinliği"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"açık ve etkili konuşan"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"daha açık, etkili ve gerekçesi güçlü konuşan"}],"lexicalization_note":"Çıplak biçimler doğrudan güzel, açık ve güçlü konuşma yetkinliğini adlandırır; başka yapılara özgü anlamlar eklenmez.","neighbor_coverage_note":"Bütün komşu adayları incelendi; en yakın iki olumlu konuşma yetkinliği ile doğrudan karşıt anlatım yetersizliği seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal konuşanın genel anlatım ve gerekçelendirme yetisini vurgular; komşu dal sözün amaçlanan anlamı başarıyla ulaştırmasını öne çıkarır.","focus_only":"Açık konuşmanın yanında gerekçe üretme ve tartışmada güçlü olma yetisini de kapsar.","gloss":"etkili ve amaca ulaşan anlatım","neighbor_only":"Sözün amaçlanan anlamı dinleyiciye ulaştıracak yeterlikte olmasını öne çıkarır.","neighbor_ref":"root_000151/B004","relation_type":"near_synonym","shared_zone":"İki dal da açık, etkili ve amacına ulaşan konuşma niteliğini anlatır."},{"boundary_match":"partial","distinction":"Odak dal anlatım ve savunma yetkinliğine dayanır; komşu dal dilin kurallarına uygunluğu ve belirli bir dili düzgün söylemeyi de sınırına alır.","focus_only":"Belirli bir dile bağlı olmadan açıklık, etkileyicilik ve gerekçe gücünü kapsar.","gloss":"açık konuşma ve dili düzgün kullanma","neighbor_only":"Yanlışsız dil kullanımı, belirli bir dili düzgün konuşma ve doğallık karşısında yapmacık güzel konuşmayı da kapsar.","neighbor_ref":"root_001158/B002","relation_type":"near_synonym","shared_zone":"Her ikisi de düzgün, anlaşılır ve akıcı konuşma alanındadır."},{"boundary_match":"opposed","distinction":"Odak dal eksenin olumlu ucundaki açıklık ve güçtür; komşu dal bunun karşıtı olan söyleyememe ve anlatamama durumudur.","focus_only":"Sözü açıkça kurma ve gerekçeyle savunma yeterliğidir.","gloss":"açık konuşma ve anlatım tutulması","neighbor_only":"Konuşma, anlatım veya gerekçe üretmede tutulup kalma yetersizliğidir.","neighbor_ref":"root_001070/B001","relation_type":"antonym","shared_zone":"İki dal aynı konuşma ve anlatım yeterliği ekseni üzerindedir."}],"source_phrase_ar":"اللسن جودة اللسان والفصاحة (maqayis)؛ رجل لسن بين اللسن (ayn)؛ اللسن الفصاحة وقد لسن فهو لسن وألسن (sihah)؛ رجل لسن بين اللسن إذا كان ذا بيان وفصاحة (tahdhib)؛ أفصح وأبين كلاما وأقدر على الحجة (mufradat)","source_summary":"Kaynaklar bu anlamı güzel, açık ve güçlü konuşma yetkinliğinde birleştirir; açıklık ve gerekçe sunma gücü bu yetkinliğin bileşenleridir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اللسن وجودة اللسان والفصاحة والبيان والقدرة على الحجة والرجل اللسن","what_is_not_ar":"ليس مجرد امتلاك اللسان ولا مجرد اللغة القومية ولا الرسالة"},"support_links":["sup_0fd8fd3a9ce231928ad3"]},{"boundary":"Çekirdek, dil ucuna benzeyen biçimdir; ayakkabı ucu ve ince, hafif uzun ayak bu biçimin özel gerçekleşmeleridir.","branch_kind":"mixed_non_bare","branch_ref":"root_001355/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لِسَان","morph_features":"STEM|POS:N|LEM:lisaAn|ROOT:lsn|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:9:1:2","qac_word_ref":"90:9:1","surface_ar":"لِسَانًا"}],"gloss":"dil ucunu andıran ince ve uzunca biçim","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin ucu, dil ucunu andıracak biçimde yapılmıştır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayakkabının ön ucu dil ucu biçiminde, ince ve uzunca olabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ayak için kullanıldığında incelik ve hafif uzunluk anlatılır."}}],"root_ar":"ل س ن","root_id":"root_001355","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel biçimi ve ayakkabı ile ayaktaki özel gerçekleşmelerin ortak görünüşünü karşılar.","boundary_detail":"Çekirdek, dil ucuna benzeyen biçimdir; ayakkabı ucu ve ince, hafif uzun ayak bu biçimin özel gerçekleşmeleridir.","branch_image_ar":"الشيء على هيئة اللسان","concept_gloss":"dil ucunu andıran ince ve uzunca biçim","contextual_glosses":[{"applicability":"Bir nesnenin veya ayakkabının ön ucunun biçimi anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ayak için belirtilen genel incelik ve hafif uzunluk özelliğini kapsamaz.","preserves":"Ucun dil ucuna benzer biçimini korur."},"facet_ids":["F001","F002"],"text":"dil biçimli uç","usage_role":"contextual"},{"applicability":"Kullanım doğrudan ayağın görünüşünü nitelediğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel dil ucu benzetisini ve ayakkabı uygulamasını taşımaz.","preserves":"Ayaktaki incelik ve sınırlı uzunluğu korur."},"facet_ids":["F003"],"text":"ince ve hafif uzun ayak","usage_role":"explanatory"}],"definition":"Bir nesnenin ucunun dil ucu gibi biçimlendirilmesi veya ince ve hafif uzun bir görünüş taşımasıdır. Ayakkabının ön ucu ile ayağın biçimi bu görünüşün özel uygulamalarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin ucu, dil ucunu andıracak biçimde yapılmıştır."},{"facet_id":"F002","role":"specialization","statement":"Ayakkabının ön ucu dil ucu biçiminde, ince ve uzunca olabilir."},{"facet_id":"F003","role":"specialization","statement":"Ayak için kullanıldığında incelik ve hafif uzunluk anlatılır."}],"identity_rationale":"Kaynak ifadesi, bir şeyin ucunun dil ucuna benzetilmesini ve ayakkabı ya da ayakta görülen ince, hafif uzun biçimi birlikte destekler. Genel biçim ile verilen özel nesne örnekleri ayrıştırıldığında dal çerçevesi kaynağa uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ucu dil gibi olan; ince ve hafif uzun"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ön ucu dil biçiminde, ince ve uzunca ayakkabı"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ince ve hafif uzun ayak"}],"lexicalization_note":"Genel biçim bildiren yalın kullanım ile ayakkabı ve ayağa bağlı özel kullanımlar ayrı tutulur; özel örnekler bütün nesnelere yayılmaz.","neighbor_coverage_note":"Bütün komşular değerlendirildi; genel uç, başka bir uzunluk benzetisi ve benzetmenin kaynağı olan gerçek organla sınır karşılaştırmaları seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir dil ucu biçimini şart koşar; komşu dal biçimi ne olursa olsun öne çıkan uçları daha geniş olarak kapsar.","focus_only":"Ucun dil ucuna benzemesini, incelik ve hafif uzunlukla birlikte gerektirir.","gloss":"dil biçimli uç ve genel çıkıntılı uç","neighbor_only":"Bir şeyin öne çıkan ya da dışarı uzanan herhangi bir ucunu biçim benzetisi aramadan kapsar.","neighbor_ref":"root_000060/B003","relation_type":"near_neighbor","shared_zone":"İki dal da bir nesnenin öne çıkan uç bölümünü konu alır."},{"boundary_match":"partial","distinction":"Odak dal küçük, ince ve dil ucu benzeri şekle; komşu dal ise mızrak benzeri belirgin uzantıya dayanır.","focus_only":"Benzetme modeli dil ucudur ve incelikle sınırlı uzunluk öne çıkar.","gloss":"dil biçimli ve mızrak biçimli çıkıntı","neighbor_only":"Benzetme modeli mızraktır; boynuz, kuyruk, bacak veya belirgin uzunluk gibi çok farklı taşıyıcıları kapsar.","neighbor_ref":"root_000597/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal bir nesneyi uzun ve çıkıntılı başka bir nesneye benzeterek niteler."},{"boundary_match":"partial","distinction":"Odak dal benzetmeyle oluşan şekildir; komşu dal benzetmeye temel olan gerçek organdır.","focus_only":"Başka nesnelerde dil ucuna benzeyen biçimi bildirir.","gloss":"dil organı ve dil biçimli uç","neighbor_only":"Konuşmada kullanılan gerçek beden organını ve onun söyleyiş gücünü bildirir.","neighbor_ref":"root_001355/B001","relation_type":"near_neighbor","shared_zone":"Gerçek organın biçimi, odak daldaki benzetmenin kaynağıdır."}],"source_phrase_ar":"أصل يدل على طول لطيف غير بائن ونعل ملسنة على صورة اللسان وقدم ملسنة فيها لطافة وطول يسير (maqayis)؛ شيء ملسن جعل طرفه كطرف اللسان (ayn)؛ الملسن من النعال الذي فيه طول ولطافة على هيئة اللسان وامرأة ملسنة القدمين (sihah)؛ نعل ملسنة إذا جعل طرف مقدمها كطرف اللسان (tahdhib)","source_summary":"Kaynaklar dil ucuna benzeyen ince ve uzunca biçimde birleşir; ayakkabının ön ucu ve ayağın hafif uzun, ince yapısı bu biçimin başlıca özel örnekleridir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الشيء أو النعل أو القدم إذا جعل طرفه كطرف اللسان أو كانت فيه لطافة وطول يسير","what_is_not_ar":"ليس جارحة اللسان نفسها ولا اللغة ولا التلسين في الإبل أو الليف"},"support_links":[]},{"boundary":"Kesilen bölüm özellikle dilin ucudur; genel yaralama, başka bir organı kesme veya yalan söyleme bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001355/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لِسَان","morph_features":"STEM|POS:N|LEM:lisaAn|ROOT:lsn|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:9:1:2","qac_word_ref":"90:9:1","surface_ar":"لِسَانًا"}],"gloss":"dil ucunun kesilmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin dilinin uç bölümünün kesilmesi eylemidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylemin sonucu, dilinin ucu kesilmiş kişiyi niteleyen bir biçimle anlatılır."}}],"root_ar":"ل س ن","root_id":"root_001355","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem kesme eylemini hem de kişide ortaya çıkan sonucu kapsayan genel karşılıktır.","boundary_detail":"Kesilen bölüm özellikle dilin ucudur; genel yaralama, başka bir organı kesme veya yalan söyleme bu dala girmez.","branch_image_ar":"قطع طرف اللسان","concept_gloss":"dil ucunun kesilmesi","contextual_glosses":[{"applicability":"Eylemi yapan ve eylemden etkilenen kişinin bulunduğu fiil bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dil ucu kesilmiş kişiyi niteleyen sonuç biçimini kapsamaz.","preserves":"Dil ucuna yönelik kesme eylemini eksiksiz korur."},"facet_ids":["F001"],"text":"dilinin ucunu kesmek","usage_role":"contextual"},{"applicability":"Eylemin sonucu olarak kişiyi niteleyen kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kesme eylemini gerçekleştirme anlamını kapsamaz.","preserves":"Kişideki kesilme sonucunu ve kesilen özel bölümü korur."},"facet_ids":["F002"],"text":"dilinin ucu kesilmiş","usage_role":"contextual"}],"definition":"Bir kişinin dilinin ucunu kesmek ve bunun sonucunda o kişinin dil ucunun kesilmiş olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin dilinin uç bölümünün kesilmesi eylemidir."},{"facet_id":"F002","role":"extension","statement":"Eylemin sonucu, dilinin ucu kesilmiş kişiyi niteleyen bir biçimle anlatılır."}],"identity_rationale":"Tek kaynak ifadesi, bir kişinin dilinin ucunu kesme eylemini ve bu eylemin sonucu olarak dil ucu kesilmiş kişiyi açıkça verir. Dal bu dar bedensel işlemi başka kesme türlerine veya yalancı anlamındaki ayrı sözcüğe genişletmez.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kişinin dil ucunu kesmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"dilinin ucu kesilmiş kişi"}],"lexicalization_note":"Kişi nesneli kesme eylemi ile eylemin sonucunu bildiren biçim ayrı facetlerde tutulur; bunlardan genel bir kesme anlamı çıkarılmaz.","neighbor_coverage_note":"Verilen tüm komşular değerlendirildi; özel dil ucu kesimini genel eksiltici kesmeden ve başka organların kesilmesinden ayıran iki karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal beden bölümüne ve belirli bir kesim yerine bağlıdır; komşu dal nesne ve bölüm bakımından çok daha genel bir kesilme alanıdır.","focus_only":"Kesilen yer özellikle kişinin dil ucudur ve sonuç kişiyi niteler.","gloss":"dil ucunu kesme ve eksik bırakacak biçimde kesme","neighbor_only":"Her tür nesnenin tamamlanmadan kesilmesini, kuyruk gibi bölümlerin kökünden alınmasını ve kesici nesneleri kapsar.","neighbor_ref":"root_000080/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir şeyin uç veya tamamlayıcı bölümünü keserek eksiltmeyi anlatabilir."},{"boundary_match":"field_only","distinction":"Ortak eylem kesmedir; fakat etkilenen organ ve kesilen bölüm kesin biçimde farklıdır.","focus_only":"Dilin yalnızca uç bölümünün kesilmesini bildirir.","gloss":"dil ucu, baş veya burun kesme","neighbor_only":"Başın veya burnun kesilmesini bildirir.","neighbor_ref":"root_000642/B010","relation_type":"same_field","shared_zone":"Her iki dal bir beden bölümünün kesilmesi alanındadır."}],"source_phrase_ar":"لسن الرجل أي قطع طرف لسانه فهو ملسون (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, dil ucunu kesme eylemiyle dil ucu kesilmiş kişi sonucunu birlikte verir."}],"source_summary":"Kaynaklar arası ortaklaştırılabilecek ayrı bir iddia yoktur; dal tek bir sözlük tanıklığına dayanır.","sources":["AY"],"what_is_ar":"يدخل فيه لسن الرجل إذا قطع طرف لسانه والملسون بهذا المعنى","what_is_not_ar":"ليس الملسون بمعنى الكذاب ولا الملسن على هيئة اللسان"},"support_links":[]},{"boundary":"Çekirdek bir topluluğun dili ve konuşmasıdır; söz, haber, ileti, sözcülük ve övgü kullanımları bu çekirdeğe bağlı uzantılardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001355/B006","candidate_links":[{"candidate_id":"cand_74fb2f232417f40ef98c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لِسَان","morph_features":"STEM|POS:N|LEM:lisaAn|ROOT:lsn|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:9:1:2","qac_word_ref":"90:9:1","surface_ar":"لِسَانًا"}],"gloss":"bir topluluğun dili ve konuşması","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun kullandığı dil sistemi ve o sistemle gerçekleşen konuşmadır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Konuşma ürününden hareketle söz, sözcük, haber veya ileti anlamına uzanır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Topluluk adına konuşan kişi, özel bir yapıda topluluğun sesi olarak adlandırılır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İnsanların biri hakkında söyledikleri, özellikle dolaşan övgü, başka bir özel yapıda anlatılır."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Çoğul kullanım, dillerin ve konuşma seslerinin çeşitliliğini gösterebilir."}}],"root_ar":"ل س ن","root_id":"root_001355","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın bütün aktarmalı kullanımlarına temel olan dil sistemi ve konuşma çekirdeğini en kısa doğal biçimde karşılar.","boundary_detail":"Çekirdek bir topluluğun dili ve konuşmasıdır; söz, haber, ileti, sözcülük ve övgü kullanımları bu çekirdeğe bağlı uzantılardır.","branch_image_ar":"اللسان لغة وكلاما","concept_gloss":"bir topluluğun dili ve konuşması","contextual_glosses":[{"applicability":"Bir topluluğun iletişim sistemi veya farklı toplulukların dilleri söz konusu olduğunda uygundur.","error_profile":{"adds":null,"collision":"Bağlamsız kullanımda konuşma organı anlamıyla karışabilir.","fit":"narrowing","loses":"Söz, haber, sözcü ve insanlar arasında dolaşan övgü uzantılarını tek başına taşımaz.","preserves":"Topluluğun konuşma sistemini doğal biçimde karşılar."},"facet_ids":["F001","F005"],"text":"dil","usage_role":"general"},{"applicability":"Tek bir konuşma ürünü, sözcük, haber ya da ileti kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dil sistemi çekirdeğini ve diğer özel kullanımları kapsamaz.","preserves":"Konuşmadan doğan tekil söz, haber veya ileti uzantısını korur."},"facet_ids":["F002"],"text":"söz veya haber","usage_role":"contextual"},{"applicability":"Bir kişinin bir topluluk adına konuştuğu özel yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dil ve konuşma çekirdeğiyle öteki uzantıları kapsamaz.","preserves":"Topluluk adına konuşan kişi uzantısını açıkça karşılar."},"facet_ids":["F003"],"text":"topluluğun sözcüsü","usage_role":"contextual"},{"applicability":"İnsanların bir kişi hakkında iyi söz söylemesini anlatan özel yapıda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dil sistemi, haber ve sözcülük anlamlarını kapsamaz.","preserves":"İnsanların sözünde dolaşan övgü uzantısını korur."},"facet_ids":["F004"],"text":"hakkında dolaşan övgü","usage_role":"explanatory"}],"definition":"Bir topluluğun kullandığı dil sistemi veya bu sistemle ortaya konan konuşmadır. Bu çekirdekten söz, haber ya da ileti; topluluk adına konuşan kişi; insanlar arasında dolaşan övgü ve dillerle ses renkleri arasındaki ayrılık anlamları gelişir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun kullandığı dil sistemi ve o sistemle gerçekleşen konuşmadır."},{"facet_id":"F002","role":"extension","statement":"Konuşma ürününden hareketle söz, sözcük, haber veya ileti anlamına uzanır."},{"facet_id":"F003","role":"associated_use","statement":"Topluluk adına konuşan kişi, özel bir yapıda topluluğun sesi olarak adlandırılır."},{"facet_id":"F004","role":"associated_use","statement":"İnsanların biri hakkında söyledikleri, özellikle dolaşan övgü, başka bir özel yapıda anlatılır."},{"facet_id":"F005","role":"extension","statement":"Çoğul kullanım, dillerin ve konuşma seslerinin çeşitliliğini gösterebilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bedensel organı bu dalın asıl konusuymuş gibi ekler.","collision":"Kökün konuşma organını anlatan ayrı dalıyla doğrudan karışır.","fit":"displacement","loses":"Topluluğun dil sistemi ile söz, haber ve öteki aktarmalı kullanımları kaybeder.","preserves":"Konuşmayla bağlantıyı dolaylı olarak korur."},"text":"konuşma organı"}],"identity_rationale":"Kaynak ifadesi topluluğun dili ve konuşması çekirdeğini destekler; sözcük, haber, ileti, topluluk adına konuşan kişi ve insanlar arasında dolaşan övgü ise bu çekirdekten gelişen aktarmalı kullanımlardır. Dal korunabilir, ancak bu bağımlı kullanımlar dil ve konuşmanın eş düzeyli tanımları sayılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bir topluluğun dili ve konuşması"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"bir topluluğun konuştuğu dil"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"söz, sözcük, haber veya ileti"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"topluluk adına konuşan kişi, topluluğun sözcüsü"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"insanların kişi hakkında söylediği övgü"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"farklı diller ve konuşma sesleri"}],"lexicalization_note":"Yalın dil ve konuşma anlamları, sözcük ya da haber uzantıları ve topluluğa veya övgüye bağlı özel yapılar birbirine karıştırılmadan tanımlanır.","neighbor_coverage_note":"Bütün komşu adaylar değerlendirildi; beden organı, söz ve haber alanı ile iletiyi ulaştırma eylemi, dalın çekirdeğini ve uzantılarını en iyi sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal aktarmalı dil ve konuşma anlamındadır; komşu dal gerçek beden organıdır.","focus_only":"Dil sistemi, konuşma, söz ve bunlardan gelişen toplumsal kullanımları kapsar.","gloss":"iletişim sistemi olarak dil ve organ olarak dil","neighbor_only":"Ağızdaki beden organını ve ona bağlı söyleyiş gücünü kapsar.","neighbor_ref":"root_001355/B001","relation_type":"near_neighbor","shared_zone":"Konuşma organının adı, iletişim sisteminin ve sözün adı olarak da kullanılır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği dil sistemidir ve haber yalnızca bir uzantıdır; komşu dalın çekirdeği anlatılan ya da yenilenen söz ve haberdir.","focus_only":"Topluluğun dil sistemini, tekil söz ve haber uzantılarını ve toplumsal kullanımları kapsar.","gloss":"dil ve anlatılan söz","neighbor_only":"Yeniden anlatılan haber, konuşma, söyleşi ve bunları sıkça yapan kişi çevresinde genişler.","neighbor_ref":"root_000299/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal konuşma ürünü olan söz veya haber alanında kesişir."},{"boundary_match":"partial","distinction":"Odak dal iletiyi konuşmanın bir ürünü olarak adlandırır; komşu dal o iletinin aktarılması işlemini tanımlar.","focus_only":"Dil, söz, haber veya iletiyi ad olarak bildirir.","gloss":"ileti ve iletiyi ulaştırma","neighbor_only":"Bir iletiyi bir kişiden ya da bir kişiye ulaştırma eylemini bildirir.","neighbor_ref":"root_001355/B008","relation_type":"near_neighbor","shared_zone":"İleti veya haber iki dalın ortak içerik alanıdır."}],"source_phrase_ar":"اللسن اللغة ويعبر بالرسالة عن اللسان (maqayis)؛ اللسان الكلام (ayn)؛ يكنى بها عن الكلمة واللسن اللغة لكل قوم لسن (sihah)؛ لكل قوم لسن أي لغة ولسان الناس عليك ثناؤهم ولسان بني عامر الكلمة أو الخبر (tahdhib)؛ لكل قوم لسان ولسن أي لغة واختلاف الألسنة إشارة إلى اختلاف اللغات والنغمات (mufradat)","source_summary":"Kaynaklar dil ve konuşma çekirdeğinde birleşir; söz, haber, ileti, topluluk adına konuşma, insanlar arasında dolaşan övgü ve dillerle seslerin çeşitliliği bu çekirdekten gelişen kullanımlar olarak aktarılır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اللسان واللسن بمعنى اللغة والكلام والكلمة والخبر والرسالة والثناء الجاري على الألسنة","what_is_not_ar":"ليس جارحة اللسان نفسها ولا صفة الفصاحة ولا فعل الإبلاغ بصيغة ألسني"},"support_links":["sup_aac6cd799f56f97f1332"]},{"boundary":"İşlem ödünç yavru, sütü indirilecek dişi deve, sütü tattırma ve ardından yavruyu uzaklaştırma aşamalarının tümünü gerektirir.","branch_kind":"bare","branch_ref":"root_001355/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لِسَان","morph_features":"STEM|POS:N|LEM:lisaAn|ROOT:lsn|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:9:1:2","qac_word_ref":"90:9:1","surface_ar":"لِسَانًا"}],"gloss":"ödünç yavruyla dişi devenin sütünü indirtme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi kendi deve yavrusunu, başka birinin dişi devesinin sütünü indirtmek için ödünç verir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yavru sütten diliyle tadar; dişi devenin sütü inince yavru ondan uzaklaştırılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu işlemde yavru verilen yavrusuz dişi deve özel bir adla anılır."}}],"root_ar":"ل س ن","root_id":"root_001355","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yavrunun ödünç verilmesi, sütü tattırması ve sağım başlayınca uzaklaştırılmasıyla oluşan işlemin genel adıdır.","boundary_detail":"İşlem ödünç yavru, sütü indirilecek dişi deve, sütü tattırma ve ardından yavruyu uzaklaştırma aşamalarının tümünü gerektirir.","branch_image_ar":"التلسين في إدرار الناقة","concept_gloss":"ödünç yavruyla dişi devenin sütünü indirtme","contextual_glosses":[{"applicability":"İşlemin sütü tattırma ve yavruyu uzaklaştırma aşamaları açıklanırken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yavrunun başka bir kişiden ödünç alınması ve yavrusuz dişi devenin özel adı açıkça görünmez.","preserves":"Sütü tattırma, sütü indirtme ve yavruyu uzaklaştırma sırasını korur."},"facet_ids":["F002"],"text":"yavruyu emzirip sonra uzaklaştırarak süt indirtmek","usage_role":"explanatory"}],"definition":"Bir kişinin deve yavrusunu, başkasının dişi devesinin sütünü indirtmek üzere ödünç vermesi; yavrunun sütten diliyle tatmasından ve süt inmesinden sonra uzaklaştırılması işlemidir. İşlemde yavru verilen yavrusuz dişi deve de özel olarak adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi kendi deve yavrusunu, başka birinin dişi devesinin sütünü indirtmek için ödünç verir."},{"facet_id":"F002","role":"specialization","statement":"Yavru sütten diliyle tadar; dişi devenin sütü inince yavru ondan uzaklaştırılır."},{"facet_id":"F003","role":"associated_use","statement":"Bu işlemde yavru verilen yavrusuz dişi deve özel bir adla anılır."}],"identity_rationale":"Kaynak ifadesi, bir kişinin kendi deve yavrusunu başkasına ödünç vermesini, yavrunun dişi deveden süt tatmasını, süt inince uzaklaştırılmasını ve yavrusuz dişi devenin bu işlemdeki adını açıkça sıralar. Dal çerçevesi bu teknik süreci doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"ödünç yavruya süt tattırıp onu uzaklaştırarak dişi devenin sütünü indirtme"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bu işlem için ödünç yavru verilen yavrusuz dişi deve"}],"lexicalization_note":"Yalın terimler bu özel hayvancılık işlemini ve işlemdeki yavrusuz dişi deveyi adlandırır; genel süt verme veya sağma anlamına genişletilmez.","neighbor_coverage_note":"Bütün komşular değerlendirildi; yavrusuz dişi deveyle doğrudan kesişen dal ve aynı sağım sahnesindeki fakat başka çekirdek taşıyan dal seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ödünç verme ve uzaklaştırma aşamalı işlemdir; komşu dalın çekirdeği yavrusuz dişi devenin durumu ve başka yavruya yöneltilmesidir.","focus_only":"Yavrunun ödünç verilmesi, sütü tattırması ve sonra uzaklaştırılmasıyla yürütülen işlemi kapsar.","gloss":"yavrusuz dişi deve ve ödünç yavruyla süt indirtme","neighbor_only":"Kendi yavrusu bulunmayan veya yavrusu uzaklaştırılmış dişi devenin durumunu ve başka yavruya alıştırılmasını genel olarak kapsar.","neighbor_ref":"root_000436/B010","relation_type":"near_neighbor","shared_zone":"Her iki dal yavrusu yanında olmayan dişi deveye başka bir yavru yaklaştırılarak süt indirilmesi alanında kesişir."},{"boundary_match":"thematic_only","distinction":"Odak dal yavru kullanılarak sütü başlatan işlemdir; komşu dal devenin duruşu ve o durumda elde edilen süttür.","focus_only":"Ödünç yavru aracılığıyla sütü indirtme yöntemini anlatır.","gloss":"sütü indirtme yöntemi ve çökmüş deveyi sağma","neighbor_only":"Dişi devenin çökmüş durumdayken süt vermesini ve o sırada sağılan sütü anlatır.","neighbor_ref":"root_000109/B007","relation_type":"thematic","shared_zone":"İki dal da dişi devenin süt vermesi ve sağım çevresindeki aynı hayvancılık sahnesine aittir."}],"source_phrase_ar":"التلسين أن يعير الرجل الرجل فصيلا لتدر عليه ناقته فإذا درت نحي الفصيل ومعناه أنه ذاق اللبن بلسانه (maqayis)؛ التلسين أن يعير الرجل فصيلا لتدر عليه ناقته فإذا درت نحي الفصيل ومعناه أنه ذاق اللبن بلسانه (maqayis-routing)؛ الخلية من الإبل يقال لها المتلسنة وهو التلسن (tahdhib)","source_summary":"Kaynaklar ödünç verilen yavrunun dişi deveye sütü tattırılması ve süt inince uzaklaştırılması sürecini paylaşır; yavrusuz dişi devenin işlem içindeki özel adı da aktarılır.","sources":["MQ","TA"],"what_is_ar":"يدخل فيه التلسين والمتلسنة والخلية من الإبل في إعارة الفصيل لتدر عليه الناقة ثم ينحى عنها","what_is_not_ar":"ليس التلسين في الليف ولا الشكل الملسن ولا اللغة"},"support_links":[]},{"boundary":"Bu dal bir iletiyi ulaştırma eylemidir; dil sistemi, iletinin içeriği veya karşılıklı görüşme tek başına bu anlama girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001355/B008","candidate_links":[{"candidate_id":"cand_74fb2f232417f40ef98c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لِسَان","morph_features":"STEM|POS:N|LEM:lisaAn|ROOT:lsn|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:9:1:2","qac_word_ref":"90:9:1","surface_ar":"لِسَانًا"}],"gloss":"iletiyi ulaştırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iletinin bir alıcıya ulaştırılması eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi bağlı yapılarda söz, belirli bir kişiden veya o kişiye bir başkası için aktarılır."}}],"root_ar":"ل س ن","root_id":"root_001355","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir sözün ya da iletinin gönderenden alıcıya aktarılması çekirdeğini karşılar.","boundary_detail":"Bu dal bir iletiyi ulaştırma eylemidir; dil sistemi, iletinin içeriği veya karşılıklı görüşme tek başına bu anlama girmez.","branch_image_ar":"الإلسان إبلاغ الرسالة","concept_gloss":"iletiyi ulaştırma","contextual_glosses":[{"applicability":"Belirli bir kişinin sözünün veya haberinin başkasına aktarılması bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İleti dışındaki genel söz aktarımını ve eylem adını bütünüyle kapsamaz.","preserves":"Kişiye bağlı haberin bir alıcıya ulaştırılmasını korur."},"facet_ids":["F002"],"text":"haberini iletmek","usage_role":"contextual"},{"applicability":"Gönderen ile alıcı arasında somut bir mesaj taşıma bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mesajın bir kişiden diğerine aktarılması eylemini korur."},"facet_ids":["F001","F002"],"text":"mesaj götürmek","usage_role":"contextual"}],"definition":"Bir iletiyi hedef kişiye ulaştırmak veya belirli bir kişiden ya da kişiye sözü başkası adına aktarmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iletinin bir alıcıya ulaştırılması eylemidir."},{"facet_id":"F002","role":"specialization","statement":"Kişi bağlı yapılarda söz, belirli bir kişiden veya o kişiye bir başkası için aktarılır."}],"identity_rationale":"Kaynak ifadesi hem ileti ulaştırma eyleminin adını hem de bir kişiden ya da bir kişiye ileti götürmeyi bildiren kişi bağlı yapıları destekler. Dal, iletinin kendisini değil onun ulaştırılması işlemini çekirdek alarak kaynağa uygun kalır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"iletiyi ulaştırma"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"o kişiden veya o kişiye haberi benim için ilet"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"o kişiyle ilgili sözü benim için ilet"}],"lexicalization_note":"Eylemin adı ile bir kişi üzerinden ileti ulaştırmayı bildiren yapılar ayrı tutulur; kişi bağlı kullanımlar yalın biçimin dışına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel ileti ulaştırma, daha geniş ulaşma alanı ve iletinin ad olduğu kök içi dal en açıklayıcı sınırları verdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişi bağlı söz aktarımı yapılarını da içeren özel bir sözlük alanıdır; komşu dal aynı işlemi ileti türü ve yapı bakımından daha genel anlatır.","focus_only":"Belirli kişi yapılarında sözün bir başkası için aktarılmasını özel olarak gösterir.","gloss":"iletiyi ulaştırmak","neighbor_only":"Her tür iletiyi hedefe ulaştırmayı daha genel olarak kapsar.","neighbor_ref":"root_000151/B002","relation_type":"near_synonym","shared_zone":"İki dalın çekirdeği bir iletiyi gönderenden alıcıya ulaştırmaktır."},{"boundary_match":"partial","distinction":"Odak dal ileti taşımaya özgüdür; komşu dal nesne ve yön bakımından daha geniş bir ulaştırma ya da ulaşma alanıdır.","focus_only":"Aktarılan şey söz veya iletidir ve kişi bağlı kullanımlar merkezîdir.","gloss":"iletiyi aktarma ve genel ulaştırma","neighbor_only":"Her türlü nesnenin ulaştırılmasını, varmasını ve sözün kendiliğinden muhataba erişmesini kapsar.","neighbor_ref":"root_000021/B001","relation_type":"near_neighbor","shared_zone":"Bir sözün veya haberin muhataba erişmesi iki dalda da bulunur."},{"boundary_match":"partial","distinction":"Odak dal aktarım işlemidir; komşu dal ise aktarılabilen sözün ya da iletinin adı ve daha geniş dil alanıdır.","focus_only":"İletinin bir kişiden diğerine geçirilmesi eylemini bildirir.","gloss":"ileti ve iletiyi aktarma","neighbor_only":"Dil sistemini, konuşmayı ve iletinin kendisini adlandırır.","neighbor_ref":"root_001355/B006","relation_type":"near_neighbor","shared_zone":"Her iki dalda da söz veya ileti ortak içeriktir."}],"source_phrase_ar":"يعبر بالرسالة عن اللسان (maqayis)؛ الإلسان إبلاغ الرسالة وألسني فلانا وألسن لي فلانا كذا أي أبلغ لي (tahdhib)","source_summary":"Kaynaklar ileti ile dil arasındaki anlam aktarımını destekler; belirgin eylem kullanımı, bir iletinin veya belirli bir kişiyle ilgili sözün başkası için ulaştırılmasıdır.","sources":["MQ","TA"],"what_is_ar":"يدخل فيه الإلسان وألسني فلانا وألسن لي فلانا إذا أبلغه رسالة","what_is_not_ar":"ليس اللسان بمعنى اللغة العامة ولا الرسالة اسما فقط"},"support_links":["sup_aac6cd799f56f97f1332"]},{"boundary":"Anlam lifin ezilmesi ve büküme hazır şeritlere ayrılmasıyla sınırlıdır; asıl bükme işlemi veya deve sağımıyla ilgili aynı sesli biçim bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001355/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لِسَان","morph_features":"STEM|POS:N|LEM:lisaAn|ROOT:lsn|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:9:1:2","qac_word_ref":"90:9:1","surface_ar":"لِسَانًا"}],"gloss":"lifi ezip şeritlere ayırarak büküme hazırlama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bitki lifi önce ezilerek ve işlenerek yumuşatılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İşlenmiş lif, daha sonra bükülmeye hazır ince şeritler hâline getirilir."}}],"root_ar":"ل س ن","root_id":"root_001355","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Malzemenin ilk işlenmesinden bükülecek ince şeritlerin hazırlanmasına kadar bütün süreci karşılar.","boundary_detail":"Anlam lifin ezilmesi ve büküme hazır şeritlere ayrılmasıyla sınırlıdır; asıl bükme işlemi veya deve sağımıyla ilgili aynı sesli biçim bu dala girmez.","branch_image_ar":"تلسين الليف","concept_gloss":"lifi ezip şeritlere ayırarak büküme hazırlama","contextual_glosses":[{"applicability":"Ezme ve şeritlere ayırma aşamalarının bağlamdan anlaşıldığı eylem cümlesinde kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ezme ve ince şeritlere ayırma aşamalarını açıkça söylemez.","preserves":"İşlemin büküm öncesi hazırlık amacını korur."},"facet_ids":["F001","F002"],"text":"lifi büküme hazırlamak","usage_role":"contextual"}],"definition":"Bitki lifini ezip yumuşattıktan sonra onu bükülmeye hazır ince şeritler hâline getirme işlemidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bitki lifi önce ezilerek ve işlenerek yumuşatılır."},{"facet_id":"F002","role":"specialization","statement":"İşlenmiş lif, daha sonra bükülmeye hazır ince şeritler hâline getirilir."}],"identity_rationale":"Tek kaynak ifadesi, bitki lifini önce ezip yumuşatmayı, ardından bükülmeye hazır ince şeritler hâline getirmeyi ardışık iki işlem olarak verir. Dalın hazırlık süreci çerçevesi bu aşamaları eksiksiz korur.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"lifi ezip ince şeritler hâline getirerek büküme hazırlamak"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"lifi ezip ince şeritlere ayırarak büküme hazırlama"}],"lexicalization_note":"Nesnesi lif olan eylem yapısı ile bu hazırlık işleminin adı ayrı tutulur; anlam başka malzemelere veya doğrudan ip bükmeye genişletilmez.","neighbor_coverage_note":"Bütün komşular değerlendirildi; sonraki bükme aşaması, ortaya çıkan tek şerit ve başka lifli malzemenin kabartılmasıyla sınırlar açıklandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal büküm öncesi hazırlıktır; komşu dal ise malzemeyi gerçekten büküp ipi sağlamlaştırma aşamasıdır.","focus_only":"Lifi ezip şeritlere ayırarak bükülmeye hazırlar; bükmenin kendisi çekirdeğe girmez.","gloss":"büküme hazırlama ve ipi sıkıca bükme","neighbor_only":"Hazırlanmış şeritleri bükerek sağlam bir ip oluşturma ve ipin büküm kuvvetlerini kapsar.","neighbor_ref":"root_001414/B005","relation_type":"near_neighbor","shared_zone":"İki dal ip yapımının ardışık aşamalarında lif veya şeritlerle çalışır."},{"boundary_match":"partial","distinction":"Odak dal parçaları üretme sürecidir; komşu dal ise ortaya çıkan türden tek bir ince parçanın adıdır.","focus_only":"Malzemeyi ezip çok sayıda ince şeride dönüştüren hazırlık işlemini anlatır.","gloss":"ince şerit hazırlama ve tek ince şerit","neighbor_only":"İplik, saç veya bitkiden tek bir ince parçayı nesne olarak adlandırır.","neighbor_ref":"root_000958/B003","relation_type":"near_neighbor","shared_zone":"Odak işlemin sonunda büküme hazır ince parçalar ortaya çıkar."},{"boundary_match":"partial","distinction":"Odak dalın sonucu bükülecek ince şeritlerdir; komşu dalın sonucu kabarmış ve dağılmış yün ya da pamuktur.","focus_only":"Lifi ince şeritlere ayırıp büküme hazırlar.","gloss":"lifi şeritlere ayırma ve yünü kabartma","neighbor_only":"Yün veya pamuğu döverek kabartır ve parçalarını birbirinden gevşetir.","neighbor_ref":"root_001534/B001","relation_type":"near_neighbor","shared_zone":"İki dal da lifli malzemeyi dövme veya ayırma yoluyla sonraki işleme hazırlar."}],"source_phrase_ar":"لسنت الليف إذا مشنته ثم جعلته فتائل مهيأة للفتل ويسمى ذلك التلسين (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, lifi ezip yumuşatma ve ardından büküme hazır ince şeritlere ayırma aşamalarını birlikte verir."}],"source_summary":"Kaynaklar arası ortaklaştırılabilecek ayrı bir iddia yoktur; dal tek bir sözlük tanıklığına dayanır.","sources":["TA"],"what_is_ar":"يدخل فيه لسنت الليف والتلسين إذا مشن الليف ثم جعل فتائل مهيأة للفتل","what_is_not_ar":"ليس التلسين في الناقة ولا هيئة اللسان في النعل أو القدم"},"support_links":[]},{"boundary":"Dal yalnızca tartışmalı biçimde yalancı diye nitelenen kişiyi kapsar; dil ucu kesilmiş kişi ve genel güzel konuşan kişi ayrı anlamlardır.","branch_kind":"bare","branch_ref":"root_001355/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لِسَان","morph_features":"STEM|POS:N|LEM:lisaAn|ROOT:lsn|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:9:1:2","qac_word_ref":"90:9:1","surface_ar":"لِسَانًا"}],"gloss":"yalancı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yalan söyleyen kişiyi, yani yalancıyı niteler."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kullanım bazı aktarımlarda kabul edilirken aynı kaynak kümesinde onu tanımadığını bildiren bir itiraz bulunur."}}],"root_ar":"ل س ن","root_id":"root_001355","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalan söyleyen kişiyi gösteren anlamsal karşılıktır; kaynak kullanımının tartışmalı olduğu ayrıca belirtilmelidir.","boundary_detail":"Dal yalnızca tartışmalı biçimde yalancı diye nitelenen kişiyi kapsar; dil ucu kesilmiş kişi ve genel güzel konuşan kişi ayrı anlamlardır.","branch_image_ar":"الملسون الكذاب","concept_gloss":"yalancı","contextual_glosses":[{"applicability":"Tartışmalı kaynak biçimin kişi anlamını açıklamak gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":"Karşılık tek başına tanıklığın tartışmalı olduğunu bildirmez.","fit":"none","loses":null,"preserves":"Yalan söyleyen kişi çekirdeğini açıkça verir."},"facet_ids":["F001","F002"],"text":"yalan söyleyen kimse","usage_role":"explanatory"}],"definition":"Yalan söyleyen kişiyi niteleyen, sözlüklerde aktarılmış olmakla birlikte kullanımının tanınırlığına açıkça itiraz edilmiş bir addır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yalan söyleyen kişiyi, yani yalancıyı niteler."},{"facet_id":"F002","role":"source_variant","statement":"Kullanım bazı aktarımlarda kabul edilirken aynı kaynak kümesinde onu tanımadığını bildiren bir itiraz bulunur."}],"identity_rationale":"Kaynak ifadesi sözcüğün yalancı anlamında aktarıldığını gösterir, ancak aynı toplu tanıklık içinde bu kullanımın tanınmadığını bildiren açık bir itiraz da vardır. Anlam dalı korunabilir, fakat kullanımın tartışmalı olduğu her tanımda görünür kalmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"yalancı; kullanımı tartışmalı"}],"lexicalization_note":"Yalın biçimin yalancı kişi anlamı, tanıklık üzerindeki itirazla birlikte verilir; daha genel yalan veya söz söyleme anlamları eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalancı kişiyle en yakın örtüşen dal, daha geniş yalan alanı ve ağır uydurma suçlama dalı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Kişi anlamında büyük ölçüde örtüşürler; odak dal tartışmalı tek kişi adıdır, komşu dal ise eylem ve uydurma söz alanına da uzanır.","focus_only":"Yalancı kişi anlamındaki tek biçimdir ve bu kullanımın tanınırlığı tartışmalıdır.","gloss":"yalancı","neighbor_only":"Yalancı kişi yanında yalan söyleme eylemini ve uydurulmuş sözü de kapsar.","neighbor_ref":"root_000693/B005","relation_type":"near_synonym","shared_zone":"İki dal da yalan söyleyen kişiyi adlandırabilir."},{"boundary_match":"partial","distinction":"Odak dal kişi niteliğiyle sınırlıdır; komşu dal yalanın türünü, eylemini ve saptırıcı etkisini de kapsayan daha geniş bir alandır.","focus_only":"Yalnızca yalan söyleyen kişiyi niteleyen tartışmalı bir biçimdir.","gloss":"yalancı ve saptırıcı yalan","neighbor_only":"Yalanın kendisini, büyük yalanı, yalan söyleyen kişiyi ve insanları gerçekten saptırmayı kapsar.","neighbor_ref":"root_000041/B002","relation_type":"near_neighbor","shared_zone":"Yalan söyleyen kişi iki dalın kesişim alanıdır."},{"boundary_match":"partial","distinction":"Odak dal yalancı kişiyi adlandırır; komşu dal belirli bir mağdura yönelen ağır, uydurma suçlamayı tanımlar.","focus_only":"Yalan söyleme alışkanlığı veya niteliği bulunan kişiyi genel olarak gösterir.","gloss":"yalancı ve iftira niteliğindeki yalan","neighbor_only":"Suçsuz bir kişiye yapmadığı bir şeyi yükleyen, şaşırtıcı ve çirkin bir yalanı gerektirir.","neighbor_ref":"root_000157/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal gerçek dışı söz söyleme alanındadır."}],"source_phrase_ar":"الملسون الكذاب (sihah)؛ يقولون الملسون الكذاب وهذا مشتق من اللسان (maqayis)؛ الملسون الكذاب قال الشيخ لا أعرفه (tahdhib)","source_summary":"Sözcük yalancı diye açıklanır; ancak aynı aktarım kümesinde bu kullanımı tanımadığını bildiren açık bir itiraz da yer alır.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه الملسون إذا أريد به الكذاب على قول من أثبته","what_is_not_ar":"ليس الملسون الذي قطع طرف لسانه ولا مطلق الفصيح"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["90:9:1"],"branch_refs":[],"candidate_id":"cand_94a56fcda9ab97a79916","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:9:1:additive-apparatus-and-forward-chain","source_type":"word_analysis","support_ids":["sup_102f78b4b31854ba762e","sup_73c7ce0bb90cb59be2c4"],"title":"additive chain binds the speech apparatus","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:1","qac_refs":["90:9:1:1"],"status":"accepted"}},{"anchor_refs":["90:9:1"],"branch_refs":[],"candidate_id":"cand_197c3cb1068ab0b45a48","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:9:1:cross-ayah-continuation","source_type":"word_analysis","support_ids":["sup_102f78b4b31854ba762e","sup_54fc3cd3ba021fdc058e"],"title":"continuation under the prior making-question","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:1","qac_refs":["90:9:1:1"],"status":"accepted"}},{"anchor_refs":["90:9:1"],"branch_refs":[],"candidate_id":"cand_3e1efe3514ee5aab5544","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:9:1:prefixed-recited-liaison","source_type":"word_analysis","support_ids":["sup_102f78b4b31854ba762e","sup_4a7761d7f1017a85f314"],"title":"prefixed form makes dependency audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:1","qac_refs":["90:9:1:1"],"status":"accepted"}},{"anchor_refs":["90:9:2"],"branch_refs":[],"candidate_id":"cand_490bb290ed3d27845c28","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001355"],"scope":"focus_ayah","source_local_id":"90:9:2:accusative-object-under-prior-making","source_type":"word_analysis","support_ids":["sup_45fcfe076c0bc8258646","sup_f71ed5ce1d306a699be8"],"title":"accusative object under the prior making verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:2","qac_refs":["90:9:1:2"],"status":"accepted"}},{"anchor_refs":["90:9:2"],"branch_refs":[],"candidate_id":"cand_4426de9d28a1565e10cd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001355"],"scope":"focus_ayah","source_local_id":"90:9:2:eloquence-and-public-accountability-pressure","source_type":"word_analysis","support_ids":["sup_afd211dd3d05882c0990","sup_f71ed5ce1d306a699be8"],"title":"eloquence and social consequence pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:2","qac_refs":["90:9:1:2"],"status":"accepted"}},{"anchor_refs":["90:9:2"],"branch_refs":[],"candidate_id":"cand_890a68570bc71c254c86","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001355"],"scope":"focus_ayah","source_local_id":"90:9:2:indefinite-singular-faculty","source_type":"word_analysis","support_ids":["sup_405fae33f39cbbe1833e","sup_f71ed5ce1d306a699be8"],"title":"bare singular speech faculty","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:2","qac_refs":["90:9:1:2"],"status":"accepted"}},{"anchor_refs":["90:9:2"],"branch_refs":[],"candidate_id":"cand_8e31c80850ecdd4fac0d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001355"],"scope":"focus_ayah","source_local_id":"90:9:2:organ-language-expression-range","source_type":"word_analysis","support_ids":["sup_5e7d871cd96af75dd824","sup_f71ed5ce1d306a699be8"],"title":"organ and language range held together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:2","qac_refs":["90:9:1:2"],"status":"accepted"}},{"anchor_refs":["90:9:2"],"branch_refs":[],"candidate_id":"cand_7eb6258ccc77d4751f9d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001355"],"scope":"focus_ayah","source_local_id":"90:9:2:perception-to-expression-bridge","source_type":"word_analysis","support_ids":["sup_4cf765caf13ba68c42c9","sup_f71ed5ce1d306a699be8"],"title":"pivot from sight to bounded speech","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:2","qac_refs":["90:9:1:2"],"status":"accepted"}},{"anchor_refs":["90:9:2"],"branch_refs":[],"candidate_id":"cand_5ebe008239a0a97f70ad","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001355"],"scope":"focus_ayah","source_local_id":"90:9:2:speech-sound-cadence","source_type":"word_analysis","support_ids":["sup_b56ebef7ec0e3b03da7b","sup_f71ed5ce1d306a699be8"],"title":"sound opens into utterance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:2","qac_refs":["90:9:1:2"],"status":"accepted"}},{"anchor_refs":["90:9:3"],"branch_refs":[],"candidate_id":"cand_82e6ec283992e2c44641","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:9:3:apparatus-binding-completion","source_type":"word_analysis","support_ids":["sup_a0679e941a95f095e7a4","sup_a81af7f73897152df791"],"title":"conjunction completes the speech apparatus","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:3","qac_refs":["90:9:2:1"],"status":"accepted"}},{"anchor_refs":["90:9:3"],"branch_refs":[],"candidate_id":"cand_d3bc7a1fd581d96c3a4c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:9:3:audible-two-link-rhythm","source_type":"word_analysis","support_ids":["sup_a81af7f73897152df791","sup_aa9f98e642f831a25dde"],"title":"matched connective rhythm","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:3","qac_refs":["90:9:2:1"],"status":"accepted"}},{"anchor_refs":["90:9:3"],"branch_refs":[],"candidate_id":"cand_4767f8e8b90e3f2babac","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:9:3:forward-connective-chain","source_type":"word_analysis","support_ids":["sup_2157ccf4563eb0fb8363","sup_a81af7f73897152df791"],"title":"connective habit points beyond anatomy","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:3","qac_refs":["90:9:2:1"],"status":"accepted"}},{"anchor_refs":["90:9:3"],"branch_refs":[],"candidate_id":"cand_0eea1595aefa2c4b5f6c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:9:3:local-coordination-scope","source_type":"word_analysis","support_ids":["sup_1e67285347acf6e0e8cc","sup_a81af7f73897152df791"],"title":"local coordination within the carried frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:3","qac_refs":["90:9:2:1"],"status":"accepted"}},{"anchor_refs":["90:9:4"],"branch_refs":[],"candidate_id":"cand_47bf33706edb53c02403","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000804"],"scope":"focus_ayah","source_local_id":"90:9:4:coordinated-oblique-object","source_type":"word_analysis","support_ids":["sup_a08899c52ecc3a322d89","sup_f7ec8c4a4760ce21a2d2"],"title":"dual oblique resolved as coordinated object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:4","qac_refs":["90:9:2:2"],"status":"accepted"}},{"anchor_refs":["90:9:4"],"branch_refs":[],"candidate_id":"cand_c91e900d8c998f09ae8e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000804"],"scope":"focus_ayah","source_local_id":"90:9:4:final-apparatus-closure","source_type":"word_analysis","support_ids":["sup_5c60b1f4db64aa1cfab5","sup_f7ec8c4a4760ce21a2d2"],"title":"final word completes the speech system","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:4","qac_refs":["90:9:2:2"],"status":"accepted"}},{"anchor_refs":["90:9:4"],"branch_refs":[],"candidate_id":"cand_659f154816974e2a4ce5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000804"],"scope":"focus_ayah","source_local_id":"90:9:4:front-mouth-sound-and-dual-cadence","source_type":"word_analysis","support_ids":["sup_11686291402c3f25a0d8","sup_f7ec8c4a4760ce21a2d2"],"title":"front-mouth sound and dual closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:4","qac_refs":["90:9:2:2"],"status":"accepted"}},{"anchor_refs":["90:9:4"],"branch_refs":[],"candidate_id":"cand_0af5aff59ed06c1ab0f2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000804"],"scope":"focus_ayah","source_local_id":"90:9:4:indefinite-exact-dual-pair","source_type":"word_analysis","support_ids":["sup_3ffdf0c93c697e77bcd5","sup_f7ec8c4a4760ce21a2d2"],"title":"unclaimed exact natural pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:4","qac_refs":["90:9:2:2"],"status":"accepted"}},{"anchor_refs":["90:9:4"],"branch_refs":[],"candidate_id":"cand_73a4050decf0b0713d08","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000804"],"scope":"focus_ayah","source_local_id":"90:9:4:mouth-edge-boundary-and-oral-transmission","source_type":"word_analysis","support_ids":["sup_57883f2032bceeaf6f0f","sup_f7ec8c4a4760ce21a2d2"],"title":"mouth-edge boundary with oral-address pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:4","qac_refs":["90:9:2:2"],"status":"accepted"}},{"anchor_refs":["90:9:4"],"branch_refs":[],"candidate_id":"cand_39c5802a19b2fe8641bf","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000804"],"scope":"focus_ayah","source_local_id":"90:9:4:paired-boundary-to-paired-paths","source_type":"word_analysis","support_ids":["sup_d2a18cfb49b1370a91ab","sup_f7ec8c4a4760ce21a2d2"],"title":"paired body boundary prepares paired paths","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:4","qac_refs":["90:9:2:2"],"status":"accepted"}},{"anchor_refs":["90:9:4"],"branch_refs":[],"candidate_id":"cand_a02d639e5f906c8c37a9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000804"],"scope":"focus_ayah","source_local_id":"90:9:4:rare-concrete-lip-noun","source_type":"word_analysis","support_ids":["sup_eb914058c5e201f25ac3","sup_f7ec8c4a4760ce21a2d2"],"title":"rare concrete lip noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:4","qac_refs":["90:9:2:2"],"status":"accepted"}},{"anchor_refs":["90:9:4"],"branch_refs":[],"candidate_id":"cand_b1c2b96f7babb286ccba","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000804"],"scope":"focus_ayah","source_local_id":"90:9:4:root-alignment-mouth-not-transparency","source_type":"word_analysis","support_ids":["sup_25347c4cac16dbab88cf","sup_f7ec8c4a4760ce21a2d2"],"title":"mouth-boundary root alignment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:9:4","qac_refs":["90:9:2:2"],"status":"accepted"}},{"anchor_refs":["90:9:1"],"branch_refs":[],"candidate_id":"cand_db1f2d7995f7e16ccb2d","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001355"],"scope":"focus_ayah","source_local_id":"90:9:1:2","source_type":"qac_morpheme","support_ids":["sup_b9a5c0f864f1163f3aba"],"title":"QAC root occurrence: ل س ن","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["90:9:2"],"branch_refs":[],"candidate_id":"cand_9b090e229b70e11f991a","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000804"],"scope":"focus_ayah","source_local_id":"90:9:2:2","source_type":"qac_morpheme","support_ids":["sup_e4ebd09bf5f29ae8aad0"],"title":"QAC root occurrence: ش ف ه","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["90:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:9","branch_refs":["root_000804/B001","root_001355/B001"],"candidate_id":"cand_1d72102d119910411acf","commentary_obligation":"review","hft_ref":"hft_842ecceb14b2b5ec70c5","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_articulation_apparatus","source_type":"hft","support_ids":["sup_3421cdd1d27b672b19d1"],"title":"baseline_articulation_apparatus","trust":"legacy_unbound"},{"anchor_refs":["90:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:9","branch_refs":["root_000804/B002","root_001355/B006","root_001355/B008"],"candidate_id":"cand_74fb2f232417f40ef98c","commentary_obligation":"review","hft_ref":"hft_ccc8eeda3d9b66fab519","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_relational_relay","source_type":"hft","support_ids":["sup_aac6cd799f56f97f1332"],"title":"baseline_relational_relay","trust":"legacy_unbound"},{"anchor_refs":["90:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:9","branch_refs":["root_000804/B004","root_001355/B002","root_001355/B003"],"candidate_id":"cand_17fa6cfc2e668b9f7c36","commentary_obligation":"review","hft_ref":"hft_16b01c6a7f0979ddc920","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_social_force_and_reputation","source_type":"hft","support_ids":["sup_0fd8fd3a9ce231928ad3"],"title":"baseline_social_force_and_reputation","trust":"legacy_unbound"},{"anchor_refs":["90:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:9","branch_refs":["root_000804/B003","root_001355/B001"],"candidate_id":"cand_f078256199261d22734d","commentary_obligation":"review","hft_ref":"hft_4d67f3eba03751302485","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_request_resource_pressure","source_type":"hft","support_ids":["sup_f596bfe56fbac6f071b8"],"title":"baseline_request_resource_pressure","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَلِسَانًۭا وَشَفَتَيْنِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"90:9:1:1","qac_word_ref":"90:9:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لِسَان","morph_features":"STEM|POS:N|LEM:lisaAn|ROOT:lsn|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:9:1:2","qac_word_ref":"90:9:1","root_ar":"ل س ن","surface_ar":"لِسَانًا"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"90:9:2:1","qac_word_ref":"90:9:2","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"شَفَتَيْن","morph_features":"STEM|POS:N|LEM:$afatayon|ROOT:$fh|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:9:2:2","qac_word_ref":"90:9:2","root_ar":"ش ف ه","surface_ar":"شَفَتَيْنِ"}],"word_analysis_qac_refs":[["90:9:1:1"],["90:9:1:2"],["90:9:2:1"],["90:9:2:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["90:9:1","90:9:2","90:9:3","90:9:4"]},"focus_surface_evidence":{"arabic_uthmani":"وَلِسَانًۭا وَشَفَتَيْنِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"90:9:1:1","qac_word_ref":"90:9:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لِسَان","morph_features":"STEM|POS:N|LEM:lisaAn|ROOT:lsn|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:9:1:2","qac_word_ref":"90:9:1","root_ar":"ل س ن","surface_ar":"لِسَانًا"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"90:9:2:1","qac_word_ref":"90:9:2","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"شَفَتَيْن","morph_features":"STEM|POS:N|LEM:$afatayon|ROOT:$fh|FD|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:9:2:2","qac_word_ref":"90:9:2","root_ar":"ش ف ه","surface_ar":"شَفَتَيْنِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["90:9:1:1"],["90:9:1:2"],["90:9:2:1"],["90:9:2:2"]],"word_analysis_refs":["90:9:1","90:9:2","90:9:3","90:9:4"],"word_rows":[{"analysis_record_ref":"90:9:1","analytic_gloss_range_en":"coordinating continuation particle that carries the prior making-question across the ayah boundary into the next object","analytic_root_gloss_range_en":null,"qac_refs":["90:9:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"90:9:2","analytic_gloss_range_en":"indefinite singular tongue as a made speech faculty: concrete organ, language-capacity, articulation, and accountable expression held together locally","analytic_root_gloss_range_en":"root range covers the tongue as speech organ, language and expression, eloquence, tongue-based confrontation, public mention, and more remote specialized branches; the local noun selects the organ-faculty range and narrows derivative actions into pressure only","qac_refs":["90:9:1:2"],"root":{"arabic":"ل س ن","transliteration":"l-s-n"},"surface":{"arabic":"لِسَانًۭا","transliteration":"lisānan"}},{"analysis_record_ref":"90:9:3","analytic_gloss_range_en":"second coordinating particle that joins the dual lips to the tongue inside the same carried object-list and speech apparatus","analytic_root_gloss_range_en":null,"qac_refs":["90:9:2:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"90:9:4","analytic_gloss_range_en":"the two lips as an exact, indefinite, coordinated dual object: mouth-edge boundary, speech release and restraint, and oral transmission surface","analytic_root_gloss_range_en":"root range centers on lip and mouth-edge meanings, with accepted extensions into face-to-face oral address and word-of-mouth expression plus other nonlocal branches; this ayah selects the lip-boundary and oral-address pressure, not unrelated transparency semantics","qac_refs":["90:9:2:2"],"root":{"arabic":"ش ف ه","transliteration":"sh-f-h"},"surface":{"arabic":"شَفَتَيْنِ","transliteration":"shafatayni"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["90:9"],"branch_refs":["root_000804/B001","root_001355/B001"],"candidate_id":"cand_1d72102d119910411acf","evidence_scope":"focus_ayah","hft_ref":"hft_842ecceb14b2b5ec70c5","item_id":"baseline_articulation_apparatus","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_articulation_apparatus","support_id":"sup_3421cdd1d27b672b19d1"},{"anchor_refs":["90:9"],"branch_refs":["root_000804/B002","root_001355/B006","root_001355/B008"],"candidate_id":"cand_74fb2f232417f40ef98c","evidence_scope":"focus_ayah","hft_ref":"hft_ccc8eeda3d9b66fab519","item_id":"baseline_relational_relay","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_relational_relay","support_id":"sup_aac6cd799f56f97f1332"},{"anchor_refs":["90:9"],"branch_refs":["root_000804/B004","root_001355/B002","root_001355/B003"],"candidate_id":"cand_17fa6cfc2e668b9f7c36","evidence_scope":"focus_ayah","hft_ref":"hft_16b01c6a7f0979ddc920","item_id":"baseline_social_force_and_reputation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_social_force_and_reputation","support_id":"sup_0fd8fd3a9ce231928ad3"},{"anchor_refs":["90:9"],"branch_refs":["root_000804/B003","root_001355/B001"],"candidate_id":"cand_f078256199261d22734d","evidence_scope":"focus_ayah","hft_ref":"hft_4d67f3eba03751302485","item_id":"baseline_request_resource_pressure","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_request_resource_pressure","support_id":"sup_f596bfe56fbac6f071b8"}],"diagnostics":[],"lane_counts":{"global":16,"macro":4,"micro":4},"packet_summary":{"ayah_count":20,"focus_ref":"90:9","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ح ل ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000351","furuq_root_norm":"ح ل ل","furuq_source_root_norm":"ح ل ل","is_dominant":true,"target_occurrences":39,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000353","furuq_root_norm":"ح ل ي","furuq_source_root_norm":"ح ل ي","is_dominant":false,"target_occurrences":6,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"و ص د","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000036","furuq_root_norm":"ء ص د","furuq_source_root_norm":"أ ص د","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001653","furuq_root_norm":"و ص د","furuq_source_root_norm":"و ص د","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["90:1","90:2","90:3","90:4","90:5","90:6","90:7","90:8","90:9","90:10","90:11","90:12","90:13","90:14","90:15","90:16","90:17","90:18","90:19","90:20"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"90:9","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"90:9","lane":"micro","linguistic_source_ref":"90:9","surface_ref":"90:9","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"90:9","target_tokens":[["Bir",["90:9:1"]],["dil",["90:9:1"]],["ve",["90:9:2"]],["iki",["90:9:2"]],["dudak",["90:9:2"]],["da",["90:9:1","90:9:2"]]],"text":"Bir dil ve iki dudak da?"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":10,"id":"s090-p01-001-010","label":"Human toil and the two paths","number":1,"refs":["90:1","90:2","90:3","90:4","90:5","90:6","90:7","90:8","90:9","90:10"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:1","source_type":"word_analysis","support_id":"sup_102f78b4b31854ba762e","text":"{\"gloss_range\":\"coordinating continuation particle that carries the prior making-question across the ayah boundary into the next object\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) makes 90:9 begin as continuation rather than restart. The particle keeps the tongue inside the prior making-question from 90:8, so the new object is not an orphan accusative or a fresh assertion. Its prefixed, recited form lets the list move directly from paired sight into speech capacity, and the immediate particle-to-noun liaison makes that dependency audible before the noun is even interpreted. Because the same connective opens the lip-pair too, the listener hears an additive refrain that binds tongue and lips as one speech apparatus, with nasal cadence across the two nouns and a forward pull toward guidance in 90:10.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:4:front-mouth-sound-and-dual-cadence","source_type":"word_analysis","support_id":"sup_11686291402c3f25a0d8","text":"{\"blocking_evidence\":null,\"headline\":\"front-mouth sound and dual closure\",\"reader_payoff\":\"The reader hears the word for lips use the mouth-front and close with a dual cadence that links paired body design to paired choice.\",\"reason\":\"The phonetic and cadence observations are local to the recited surface and align with the word's final dual position.\",\"representative_source_ids\":[\"QP-263f6314\",\"QP-51e152da\",\"QP-911d43f3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:3:local-coordination-scope","source_type":"word_analysis","support_id":"sup_1e67285347acf6e0e8cc","text":"{\"blocking_evidence\":null,\"headline\":\"local coordination within the carried frame\",\"reader_payoff\":\"The reader notices that the lips are not detached from the tongue but are coordinated inside the same object chain.\",\"reason\":\"Attachment evidence directly marks the final noun as conjoined with the tongue in the same accusative list.\",\"representative_source_ids\":[\"QG-8d743bdd\",\"QG-d231f6d8\",\"MG-82d78cb5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:3:forward-connective-chain","source_type":"word_analysis","support_id":"sup_2157ccf4563eb0fb8363","text":"{\"blocking_evidence\":null,\"headline\":\"connective habit points beyond anatomy\",\"reader_payoff\":\"The reader notices that the coordination pattern does not end at body parts but helps carry endowment toward moral direction in 90:10.\",\"reason\":\"The local coordination belongs to a sequence of endowed faculties that continues into the next ayah.\",\"representative_source_ids\":[\"QB-2ca295b8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:4:root-alignment-mouth-not-transparency","source_type":"word_analysis","support_id":"sup_25347c4cac16dbab88cf","text":"{\"blocking_evidence\":null,\"headline\":\"mouth-boundary root alignment\",\"reader_payoff\":\"The reader keeps the image in the mouth-boundary field instead of drifting toward unrelated transparency semantics.\",\"reason\":\"The aligned QAC root and V4 evidence support the lip root; the local analysis should follow mouth-edge semantics.\",\"representative_source_ids\":[\"QS-5ff3dabd\",\"MF-25da56bc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:4:indefinite-exact-dual-pair","source_type":"word_analysis","support_id":"sup_3ffdf0c93c697e77bcd5","text":"{\"blocking_evidence\":null,\"headline\":\"unclaimed exact natural pair\",\"reader_payoff\":\"The reader sees two lips as a precise created pair without shifting the emphasis to ownership or an unspecified collective.\",\"reason\":\"The local form is an indefinite dual concrete noun with no possessive suffix, and dictionary evidence supports the lip-pair field.\",\"representative_source_ids\":[\"QG-0b9c1f0d\",\"QF-1f171ee8\",\"QF-aa3e774c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:2:indefinite-singular-faculty","source_type":"word_analysis","support_id":"sup_405fae33f39cbbe1833e","text":"{\"blocking_evidence\":null,\"headline\":\"bare singular speech faculty\",\"reader_payoff\":\"The reader sees a general created capacity rather than a possessed tongue, a plural of languages, or a performed act of eloquence.\",\"reason\":\"The local form is an indefinite singular concrete noun without a possessive suffix.\",\"representative_source_ids\":[\"QG-5e6bafda\",\"QF-09a0c74e\",\"QF-ad4dc0a3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:2:accusative-object-under-prior-making","source_type":"word_analysis","support_id":"sup_45fcfe076c0bc8258646","text":"{\"blocking_evidence\":null,\"headline\":\"accusative object under the prior making verb\",\"reader_payoff\":\"The reader notices the tongue as something made within the prior divine question, not as a detached anatomical note.\",\"reason\":\"QAC marks the noun as accusative, and attachment evidence supplies the continued governing verb from 90:8.\",\"representative_source_ids\":[\"QG-1f0a581f\",\"QG-400e44d7\",\"QG-db5e6ffe\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:1:prefixed-recited-liaison","source_type":"word_analysis","support_id":"sup_4a7761d7f1017a85f314","text":"{\"blocking_evidence\":null,\"headline\":\"prefixed form makes dependency audible\",\"reader_payoff\":\"The reader hears the first noun enter attached to the previous list from its first sound.\",\"reason\":\"The local word is a prefixed coordinating conjunction, so the written and recited surface itself carries continuation.\",\"representative_source_ids\":[\"QF-41b86368\",\"QF-5110c493\",\"QP-51cb783d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:2:perception-to-expression-bridge","source_type":"word_analysis","support_id":"sup_4cf765caf13ba68c42c9","text":"{\"blocking_evidence\":null,\"headline\":\"pivot from sight to bounded speech\",\"reader_payoff\":\"The reader notices a staged body sequence: paired reception, one inner articulator, then paired boundary, before guidance is named in 90:10.\",\"reason\":\"The noun is coordinated with the lips and remains in sequence with the two eyes of 90:8 and the two paths of 90:10.\",\"representative_source_ids\":[\"QT-5ff883e5\",\"QT-e4641d27\",\"QY-b792ec3e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:1:cross-ayah-continuation","source_type":"word_analysis","support_id":"sup_54fc3cd3ba021fdc058e","text":"{\"blocking_evidence\":null,\"headline\":\"continuation under the prior making-question\",\"reader_payoff\":\"The reader notices that 90:9 does not launch a new sentence but carries the prior question into another made faculty.\",\"reason\":\"QAC identifies the particle as coordination, and attachment evidence marks the nouns of 90:9 as continuing the object list governed from 90:8.\",\"representative_source_ids\":[\"QG-2f86ad7c\",\"QG-b4e349d7\",\"MG-240bce51\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:4:mouth-edge-boundary-and-oral-transmission","source_type":"word_analysis","support_id":"sup_57883f2032bceeaf6f0f","text":"{\"blocking_evidence\":null,\"headline\":\"mouth-edge boundary with oral-address pressure\",\"reader_payoff\":\"The reader notices the lips as control surfaces for speech: they release, close, shape, withhold, and carry oral address.\",\"reason\":\"The local noun selects the concrete lip-pair, while accepted oral-address and word-of-mouth branches survive as pressure on how the lip boundary functions.\",\"representative_source_ids\":[\"QS-0087720e\",\"QS-108f2edf\",\"QS-fcdc150e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:4:final-apparatus-closure","source_type":"word_analysis","support_id":"sup_5c60b1f4db64aa1cfab5","text":"{\"blocking_evidence\":null,\"headline\":\"final word completes the speech system\",\"reader_payoff\":\"The reader feels the ayah close on boundary and restraint after the singular inner articulator.\",\"reason\":\"The final coordinated object completes the tongue-and-lips apparatus and makes the closing position semantically consequential.\",\"representative_source_ids\":[\"QT-0223a4d5\",\"QT-9e0317f6\",\"QT-c58f2684\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:2:organ-language-expression-range","source_type":"word_analysis","support_id":"sup_5e7d871cd96af75dd824","text":"{\"blocking_evidence\":null,\"headline\":\"organ and language range held together\",\"reader_payoff\":\"The reader notices that the word is not flesh alone; the concrete organ is also the medium of language and meaningful expression.\",\"reason\":\"The local body-part context selects the organ, while the accepted root branches and distributional evidence support language and speech-faculty pressure without turning the noun into an abstract language word only.\",\"representative_source_ids\":[\"QS-191a8e04\",\"QS-5436fcca\",\"MS-d0cdbaff\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:1:additive-apparatus-and-forward-chain","source_type":"word_analysis","support_id":"sup_73c7ce0bb90cb59be2c4","text":"{\"blocking_evidence\":null,\"headline\":\"additive chain binds the speech apparatus\",\"reader_payoff\":\"The reader notices the connective as part of an accumulating endowment sequence, not as loose addition.\",\"reason\":\"The two content nouns are coordinated as a local apparatus, while the same connective habit keeps the sequence moving from organs toward guidance in 90:10.\",\"representative_source_ids\":[\"QS-1e9805e8\",\"QE-671b071f\",\"QB-840206ef\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:3:apparatus-binding-completion","source_type":"word_analysis","support_id":"sup_a0679e941a95f095e7a4","text":"{\"blocking_evidence\":null,\"headline\":\"conjunction completes the speech apparatus\",\"reader_payoff\":\"The reader sees coordination as functional apparatus-binding, making speech a system of organ and boundary.\",\"reason\":\"The two content nouns are coordinated, and their local semantic fields converge on articulation, release, and restraint.\",\"representative_source_ids\":[\"QS-ef33a655\",\"QT-4cfd1be7\",\"MT-bdee9cbc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:4:coordinated-oblique-object","source_type":"word_analysis","support_id":"sup_a08899c52ecc3a322d89","text":"{\"blocking_evidence\":null,\"headline\":\"dual oblique resolved as coordinated object\",\"reader_payoff\":\"The reader notices that the lip-pair still belongs to the earlier making act and is not syntactically independent.\",\"reason\":\"QAC marks the word as dual oblique, and attachment evidence resolves it as coordinated with the tongue under the carried governing verb.\",\"representative_source_ids\":[\"QG-24493dcc\",\"QG-a0b3e292\",\"QG-aa8a1959\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:3","source_type":"word_analysis","support_id":"sup_a81af7f73897152df791","text":"{\"gloss_range\":\"second coordinating particle that joins the dual lips to the tongue inside the same carried object-list and speech apparatus\",\"prose\":\"The second {{ar:وَ}} ({{tr:wa}}) has a tighter local job than the opening particle. It does not reopen the ayah; it joins the lip-pair to the tongue within the same accusative list and the same carried making-frame, so the lips cannot stand apart as a detached topic. Because the conjunction is prefixed to the closing noun, the lips arrive as completion of the speech apparatus, not an afterthought. The matched onset before both nouns makes syntax audible as a two-link refrain, and that connective habit carries created organ and boundary toward guidance in 90:10.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:3:audible-two-link-rhythm","source_type":"word_analysis","support_id":"sup_aa9f98e642f831a25dde","text":"{\"blocking_evidence\":null,\"headline\":\"matched connective rhythm\",\"reader_payoff\":\"The reader hears the repeated connective before both nouns as a small refrain that makes enumeration audible.\",\"reason\":\"The same particle opens both coordinated content nouns, producing a local recitational echo.\",\"representative_source_ids\":[\"QE-5082f530\",\"QP-a0a76c4f\",\"QP-ff7f924a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:2:eloquence-and-public-accountability-pressure","source_type":"word_analysis","support_id":"sup_afd211dd3d05882c0990","text":"{\"blocking_evidence\":null,\"headline\":\"eloquence and social consequence pressure\",\"reader_payoff\":\"The reader senses the made tongue as a capacity that can become eloquent, sharp, confrontational, or publicly remembered.\",\"reason\":\"Derivative and idiomatic rows belong to the same root field, but the local word remains a concrete noun, so these survive as pressure on the faculty rather than as separate local actions.\",\"representative_source_ids\":[\"QS-469ac806\",\"QS-62502fdc\",\"QS-90ed1715\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:2:speech-sound-cadence","source_type":"word_analysis","support_id":"sup_b56ebef7ec0e3b03da7b","text":"{\"blocking_evidence\":null,\"headline\":\"sound opens into utterance\",\"reader_payoff\":\"The reader hears the speech-organ word release in liquid, sibilant, and nasal sound before the phrase narrows toward the lip-pair ending.\",\"reason\":\"The phonetic observation is local to the recited surface and aligns with the articulation topic already carried by the noun.\",\"representative_source_ids\":[\"QP-2d21ff78\",\"QP-e561c826\",\"MP-f6954f95\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"90:9:1:2","source_type":"qac_morpheme","support_id":"sup_b9a5c0f864f1163f3aba","text":"{\"lemma_ar\":\"لِسَان\",\"morph_features\":\"STEM|POS:N|LEM:lisaAn|ROOT:lsn|M|INDEF|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"90:9:1:2\",\"qac_word_ref\":\"90:9:1\",\"root_ar\":\"ل س ن\",\"surface_ar\":\"لِسَانًا\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:4:paired-boundary-to-paired-paths","source_type":"word_analysis","support_id":"sup_d2a18cfb49b1370a91ab","text":"{\"blocking_evidence\":null,\"headline\":\"paired body boundary prepares paired paths\",\"reader_payoff\":\"The reader sees the paired lips as a formal prelude to the two paths of 90:10, joining bodily design to moral direction.\",\"reason\":\"The word is dual, closes the ayah, and sits between the prior paired eyes in 90:8 and the paired paths in 90:10.\",\"representative_source_ids\":[\"QB-323c7a7e\",\"QB-6174137c\",\"QY-adf99835\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"90:9:2:2","source_type":"qac_morpheme","support_id":"sup_e4ebd09bf5f29ae8aad0","text":"{\"lemma_ar\":\"شَفَتَيْن\",\"morph_features\":\"STEM|POS:N|LEM:$afatayon|ROOT:$fh|FD|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"90:9:2:2\",\"qac_word_ref\":\"90:9:2\",\"root_ar\":\"ش ف ه\",\"surface_ar\":\"شَفَتَيْنِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:4:rare-concrete-lip-noun","source_type":"word_analysis","support_id":"sup_eb914058c5e201f25ac3","text":"{\"blocking_evidence\":null,\"headline\":\"rare concrete lip noun\",\"reader_payoff\":\"The reader notices an ordinary organ becoming conspicuous because the concrete lip noun is rare in the supplied profile.\",\"reason\":\"The contextual profile marks this exact root-form as a single occurrence, supporting a marked local focus without overextending the rarity claim.\",\"representative_source_ids\":[\"QH-a4371cfd\",\"MH-59e7dc61\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:2","source_type":"word_analysis","support_id":"sup_f71ed5ce1d306a699be8","text":"{\"gloss_range\":\"indefinite singular tongue as a made speech faculty: concrete organ, language-capacity, articulation, and accountable expression held together locally\",\"prose\":\"{{ar:لِسَانًۭا}} ({{tr:lisānan}}) is accusative even though 90:9 has no new verb, so the tongue remains an object made under the prior question from 90:8. Its indefiniteness and singular form make it a general speech faculty before it becomes human property, a plurality of languages, or a performed act of eloquence. The word names a concrete organ, but its root field keeps language, articulation, testimony, communicative adequacy, and public trace in view: revelation reaches a people through their language in 14:4, Moses names communicative adequacy in 28:34, and here that same range begins as a made bodily faculty. Eloquence, training, sharp speech, and truthful enduring mention do not replace the local body-part sense; they make the endowed organ feel capable of refinement, confrontation, witness, and reputation. Placed between the two eyes of 90:8 and the two lips of this ayah, it turns received perception into communicable and accountable speech, with the liquid-sibilant-nasal sound of the word opening into breath before the tighter dual closure that follows.\",\"root_display\":\"{{ar:ل س ن}} ({{tr:l-s-n}})\",\"root_gloss_range\":\"root range covers the tongue as speech organ, language and expression, eloquence, tongue-based confrontation, public mention, and more remote specialized branches; the local noun selects the organ-faculty range and narrows derivative actions into pressure only\",\"surface_display\":\"{{ar:لِسَانًۭا}} ({{tr:lisānan}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:9:4","source_type":"word_analysis","support_id":"sup_f7ec8c4a4760ce21a2d2","text":"{\"gloss_range\":\"the two lips as an exact, indefinite, coordinated dual object: mouth-edge boundary, speech release and restraint, and oral transmission surface\",\"prose\":\"{{ar:شَفَتَيْنِ}} ({{tr:shafatayni}}) closes the ayah as a dual object still governed by the prior making-question. The oblique dual form is resolved by coordination with the tongue, so the lips are made objects in the same list, not a genitive aside or a new topic. Their indefiniteness and lack of possessive suffix keep the focus on an exact natural pair as endowment: two coordinated mouth-edges, not an owned mouth or an unspecified collective surface. Lexically, the word belongs to the lip and mouth-edge field, not a transparency field; oral face-to-face and word-of-mouth pressure are narrowed into the local image of a boundary that opens, closes, shapes, withholds, and carries address. The concrete lip noun is rare in the supplied profile, so this ordinary organ becomes conspicuous as the argument slows over articulation's boundary. The final position, front-mouth sounds, nasal answer to the tongue's open ending, and dual cadence make the ayah land on controlled closure, and that paired closure prepares the next paired paths in 90:10.\",\"root_display\":\"{{ar:ش ف ه}} ({{tr:sh-f-h}})\",\"root_gloss_range\":\"root range centers on lip and mouth-edge meanings, with accepted extensions into face-to-face oral address and word-of-mouth expression plus other nonlocal branches; this ayah selects the lip-boundary and oral-address pressure, not unrelated transparency semantics\",\"surface_display\":\"{{ar:شَفَتَيْنِ}} ({{tr:shafatayni}})\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَلِسَانًۭا وَشَفَتَيْنِ","ayah_ref":"90:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000804/B001","root_001355/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001355","role":"The organ-of-speech image supplies the mobile articulator at the mechanism's center.","root":"ل س ن","source_ref":"90:9","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000804","role":"The lip and labial-letter image supplies the paired outer articulators and their shaping boundary.","root":"ش ف ه","source_ref":"90:9","source_word_indices":["2"]}],"changed_reading":{"after":"A deliberately coordinated speech apparatus whose asymmetry—one mobile tongue within two lips—makes articulation possible.","before":"A bare inventory of one tongue and two lips."},"confidence":"strong","focus_anchor":"The singular tongue is coordinated with the explicitly dual lips.","mechanism":"A mobile inner articulator works against a paired outer boundary, converting breath and bodily motion into differentiated speech.","model_id":"baseline_articulation_apparatus"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_articulation_apparatus","source_type":"hft","support_id":"sup_3421cdd1d27b672b19d1","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَلِسَانًۭا وَشَفَتَيْنِ","ayah_ref":"90:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000804/B002","root_001355/B006","root_001355/B008"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_001355","role":"The language, report, and message scope makes the tongue a carrier of content that can outlive its first utterance.","root":"ل س ن","source_ref":"90:9","source_word_indices":["1"]},{"branch_id":"B008","mapped_root_id":"root_001355","role":"The conveyed-message image gives the tongue a relay function rather than mere sound production.","root":"ل س ن","source_ref":"90:9","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000804","role":"The mouth-to-mouth address image makes the relay interpersonal, embodied, and reciprocal-capable.","root":"ش ف ه","source_ref":"90:9","source_word_indices":["2"]}],"changed_reading":{"after":"A relational channel by which a message crosses from one embodied person to another.","before":"A private capacity possessed by one body."},"confidence":"strong","focus_anchor":"Tongue and lips are named together as an embodied channel rather than as isolated anatomy.","mechanism":"The tongue forms transmissible language and messages, while the lips place that content into face-to-face circulation between mouths.","model_id":"baseline_relational_relay"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_relational_relay","source_type":"hft","support_id":"sup_aac6cd799f56f97f1332","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَلِسَانًۭا وَشَفَتَيْنِ","ayah_ref":"90:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000804/B004","root_001355/B002","root_001355/B003"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001355","role":"The verbal taking or confrontation image gives the tongue force directed at another person.","root":"ل س ن","source_ref":"90:9","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_001355","role":"The eloquence and argumentative-power image supplies speech's ability to persuade or overpower.","root":"ل س ن","source_ref":"90:9","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_000804","role":"The good-public-mention image supplies the reputational residue left among other people.","root":"ش ف ه","source_ref":"90:9","source_word_indices":["2"]}],"changed_reading":{"after":"A socially consequential instrument that can confront, persuade, and leave a reputation circulating among people.","before":"Neutral equipment for making speech."},"confidence":"medium","focus_anchor":"The same tongue-and-lips apparatus can act upon another person and continue in public memory.","mechanism":"Articulate speech confronts, argues, and then circulates as public mention; the endowment therefore carries social force and reputational consequences.","model_id":"baseline_social_force_and_reputation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_social_force_and_reputation","source_type":"hft","support_id":"sup_0fd8fd3a9ce231928ad3","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَلِسَانًۭا وَشَفَتَيْنِ","ayah_ref":"90:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000804/B003","root_001355/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001355","role":"The speech-organ image supplies the means by which a need can be voiced.","root":"ل س ن","source_ref":"90:9","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000804","role":"The repeated-asking image connects the lips to demand that can occupy or exhaust a finite resource.","root":"ش ف ه","source_ref":"90:9","source_word_indices":["2"]}],"changed_reading":{"after":"The mouth as a pressure point where need is voiced and finite social resources are claimed.","before":"The mouth as an expressive possession."},"confidence":"exploratory","focus_anchor":"The lips inventory itself includes persistent asking that occupies a person or exhausts access to food and water.","mechanism":"The mouth is not only an outlet for expression; it is where need becomes an audible claim upon finite stores and upon another person's attention.","model_id":"baseline_request_resource_pressure"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_request_resource_pressure","source_type":"hft","support_id":"sup_f596bfe56fbac6f071b8","trust":"legacy_unbound"}]}
</lane_packet_json>
