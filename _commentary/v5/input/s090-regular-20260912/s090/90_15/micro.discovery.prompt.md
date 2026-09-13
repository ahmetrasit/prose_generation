# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **90:15**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s090-regular-20260912/s090/90_15/micro.discovery.json` and modify nothing
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
  "ayah_ref": "90:15",
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
{"analysis_context":{"analysis_id":"s090-regular-20260912","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"90:15","host_surah":90,"lane_context_refs":[],"ordered_context_refs":["90:1","90:2","90:3","90:4","90:5","90:6","90:7","90:8","90:9","90:10","90:11","90:12","90:13","90:14","90:16","90:17","90:18","90:19","90:20","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Genel yakınlık çekirdeği, akrabalık, dinsel sunu, su arama ve kap adları gibi ayrı sözlüksel kollara genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001212/B001","candidate_links":[{"candidate_id":"cand_9bbf162904d99c2dcac2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَقْرَبَة","morph_features":"STEM|POS:N|LEM:maqorabap|ROOT:qrb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:3:1","qac_word_ref":"90:15:3","surface_ar":"مَقْرَبَةٍ"}],"gloss":"yakın olma, yaklaşma veya yaklaştırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlık yer veya anlam bakımından uzakta değildir ya da başka bir varlığa yaklaşır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir varlık başka bir varlığa yaklaştırılabilir; böylece aralarındaki uzaklık azaltılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yakınlık, suyu erişilebilir yerde olan kuyuya veya parçaları birbirine yakın kısa beden yapısına özgülenebilir."}}],"root_ar":"ق ر ب","root_id":"root_001212","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer ve anlam alanındaki temel ilişkiyi ve bu ilişkiyi kuran değişimi birlikte karşılayan genel açıklamadır.","boundary_detail":"Genel yakınlık çekirdeği, akrabalık, dinsel sunu, su arama ve kap adları gibi ayrı sözlüksel kollara genişletilmez.","branch_image_ar":"الدنو وخلاف البعد","concept_gloss":"yakın olma, yaklaşma veya yaklaştırma","contextual_glosses":[{"applicability":"Bir varlığın başka bir varlığa doğru gelip aradaki uzaklığı azalttığı hareket bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Durağan yakınlık durumunu, yaklaştırma işlemini ve özel kuyu ile beden uygulamalarını dışarıda bırakır.","preserves":"Yakınlığa doğru gerçekleşen hareketi doğal bir fiille korur."},"facet_ids":["F001"],"text":"yaklaşmak","usage_role":"contextual"},{"applicability":"Bir kişinin veya nesnenin başka bir şeye yaklaştırıldığı ettirgen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kendiliğinden yaklaşmayı, durağan yakınlığı ve özel sözlüksel uygulamaları dışarıda bırakır.","preserves":"Bir varlığın dışarıdan yapılan işlemle yaklaştırılmasını korur."},"facet_ids":["F002"],"text":"yakına getirmek","usage_role":"contextual"}],"definition":"Bir şeyin yer veya anlam bakımından uzakta olmaması, başka bir şeye yaklaşması ya da yaklaştırılmasıdır. Suyu erişilebilir yerde olan kuyu ve parçaları birbirine yakın kısa beden bu temel ilişkinin özel uygulamalarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlık yer veya anlam bakımından uzakta değildir ya da başka bir varlığa yaklaşır."},{"facet_id":"F002","role":"core","statement":"Bir varlık başka bir varlığa yaklaştırılabilir; böylece aralarındaki uzaklık azaltılır."},{"facet_id":"F003","role":"specialization","statement":"Yakınlık, suyu erişilebilir yerde olan kuyuya veya parçaları birbirine yakın kısa beden yapısına özgülenebilir."}],"identity_rationale":"Kaynak ifadesinin ortak çekirdeği, bir varlığın yer veya anlam bakımından uzakta olmaması, yaklaşması ya da yaklaştırılmasıdır. Kuyu suyunun erişilebilir yakınlığı ile kısa bedende parçaların birbirine yakınlığı bu çekirdeğin özel gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yakın olmak veya yaklaşmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yaklaştırmak, yakına getirmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yaklaşma"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ses değişmesiyle yaklaşmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"suyu yakın kuyu"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"parçaları birbirine yakın, kısa yapılı"}],"lexicalization_note":"Tanım çıplak yakınlık çekirdeğini verir; kuyu, beden yapısı ve ses değişmeli kullanım yalnız kendi sözlüksel bağlamlarında tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en güçlü karışma olasılığı yaklaşma ve yaklaştırma çekirdeğini paylaşan bu komşuda bulundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın merkezi uzak olmama ilişkisidir; komşu dal ise yakınlığa doğru atılımı ve parçaları bir araya getirme işlemini daha belirgin biçimde öne çıkarır.","focus_only":"Odak dal, uzaklığın karşıtı olan durağan yakınlığı ve kuyu ile beden yapısındaki özel uygulamaları da kapsar.","gloss":"yaklaşma ve yaklaştırma","neighbor_only":"Komşu dal, öne ilerletme ile parçaları birbirine yaklaştırıp toplama işlemlerini ayrıca kapsar.","neighbor_ref":"root_000639/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin başka bir şeye yaklaşmasını veya yaklaştırılmasını anlatır."}],"source_phrase_ar":"أصل صحيح يدل على خلاف البعد (maqayis)؛ كرب الشيء دنا فليس من الباب وإنما هو من الإبدال من القرب (maqayis-ibdal)؛ قرب الشيء قربا ضد البعد (jamhara)؛ قرب الشيء يقرب قربا أي دنا والقرب ضد البعد (sihah)؛ القرب نقيض البعد والتقرب التدني إلى شيء والاقتراب الدنو والقرب البئر القريبة الماء والرجل القصير متقارب (tahdhib)؛ القرب والبعد يتقابلان ويستعمل ذلك في المكان (mufradat)","source_summary":"Tanıklıklar yakınlığı uzaklığın karşıtı olarak birleştirir; yaklaşma ve yaklaştırmayı aynı çekirdeğe bağlar, kuyu ile kısa beden kullanımlarını da özel örnekler olarak verir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه قرب الشيء أو الشخص في المكان أو المعنى وإدناؤه والاقتراب والتقارب والبئر القريبة الماء وقصر الخلقة لتقارب الأجزاء","what_is_not_ar":"ليس القرابة الخاصة ولا القربان ولا طلب الماء ولا أوعية السيف والماء"},"support_links":["sup_f485dfbf32fa0aced728"]},{"boundary":"Dal, zamandaki yakınlık ve yenilik ilişkisini kapsar; salt mekansal yakınlık veya genel bitiş anlamına indirgenmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001212/B002","candidate_links":[{"candidate_id":"cand_ffa8b32ec312649e6326","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَقْرَبَة","morph_features":"STEM|POS:N|LEM:maqorabap|ROOT:qrb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:3:1","qac_word_ref":"90:15:3","surface_ar":"مَقْرَبَةٍ"}],"gloss":"zamanca yaklaşma veya yakın geçmişe ait olma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir olayın veya belirli bir vaktin gerçekleşme zamanı yaklaşır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir ürün olgunlaşma evresine, güneş ise batış vaktine yaklaşır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Geçip uzaklaşan bir şey, kaynakta ayrı bir zamansal varyant olarak bu dille anlatılır."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Tuzlanmış balığın henüz taze oluşu, yapıya bağlı özel bir sözlüksel kullanımdır."}}],"root_ar":"ق ر ب","root_id":"root_001212","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın gelecek bir vaktin yaklaşmasıyla yakın geçmişten kalan yeniliği bir arada taşıyan en kısa kapsayıcı açıklamasıdır.","boundary_detail":"Dal, zamandaki yakınlık ve yenilik ilişkisini kapsar; salt mekansal yakınlık veya genel bitiş anlamına indirgenmez.","branch_image_ar":"دنو الزمان وانقضاء الشيء","concept_gloss":"zamanca yaklaşma veya yakın geçmişe ait olma","contextual_glosses":[{"applicability":"Vaat, hesap, olgunlaşma veya batış gibi beklenen bir evrenin yakın olduğunu anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Geçip gitme ile yakın geçmişe bağlı tazelik kullanımlarını dışarıda bırakır.","preserves":"Bir olayın veya gelişim evresinin zamanca yaklaşmasını korur."},"facet_ids":["F001","F002"],"text":"vakti yaklaşmak","usage_role":"contextual"},{"applicability":"Tuzlanmış balığın yeniliğini ve tazeliğini anlatan özel adlandırma bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gelecek vaktin yaklaşmasını, olgunlaşmayı, batışı ve geçip gitmeyi dışarıda bırakır.","preserves":"Yakın geçmişe ait olmanın doğurduğu tazelik niteliğini korur."},"facet_ids":["F004"],"text":"henüz taze","usage_role":"contextual"}],"definition":"Bir olayın, vaktin veya gelişim evresinin zamanca yaklaşmasıdır. Bağlama göre vaat veya hesap vaktinin yaklaşmasını, ürünün olgunlaşmaya ve güneşin batışa varmasını, bir şeyin geçip gitmesini ya da tuzlanmış balığın yapı içinde taze oluşunu anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir olayın veya belirli bir vaktin gerçekleşme zamanı yaklaşır."},{"facet_id":"F002","role":"extension","statement":"Bir ürün olgunlaşma evresine, güneş ise batış vaktine yaklaşır."},{"facet_id":"F003","role":"source_variant","statement":"Geçip uzaklaşan bir şey, kaynakta ayrı bir zamansal varyant olarak bu dille anlatılır."},{"facet_id":"F004","role":"specialization","statement":"Tuzlanmış balığın henüz taze oluşu, yapıya bağlı özel bir sözlüksel kullanımdır."}],"identity_rationale":"Kaynak ifadesi yalnız gelecekteki bir vaktin yaklaşmasını değil, ekinin olgunlaşmaya yaklaşmasını, güneşin batıma varmasını, bir şeyin geçip gitmesini ve tuzlu balığın henüz taze olmasını da içerir. Bu nedenle dal zamansal yakınlık çekirdeğiyle korunabilir, fakat bütün kullanımlar tek başına sona erme diye açıklanamaz.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"vaadin veya hesap vaktinin yaklaşması"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"son saatin yaklaşması"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ürünün olgunlaşma vaktinin yaklaşması"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"güneşin batmaya yaklaşması"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"henüz taze olan tuzlu balık"}],"lexicalization_note":"Zamansal yaklaşma çekirdeği ile vaat, olgunlaşma, batış, tazelik ve geçip gitme yapıları ayrı bağlamsal gerçekleşmeler olarak tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; zamansal yaklaşma çekirdeğini paylaşan bu komşu, dal sınırını en yararlı biçimde açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel yaklaşma ile vakit darlığına uzanırken odak dal, belirli zamansal evreleri ve yakın geçmişe bağlı tazelik adlandırmasını kendi sözlüksel sınırları içinde toplar.","focus_only":"Odak dal olgunlaşma, batış, geçip gitme ve tuzlu balığın tazeliği gibi sözlüksel uzantıları içerir.","gloss":"zamanın yaklaşması","neighbor_only":"Komşu dal nesnenin genel yaklaşmasını ve yakın vaktin doğurduğu zaman darlığını da kapsar.","neighbor_ref":"root_000029/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir olayın veya belirlenmiş vaktin yakına gelmesini anlatır."}],"source_phrase_ar":"اقترب الوعد أي تقارب (sihah)؛ تقارب الزمان اقتراب الساعة وتقارب الزرع إذا دنا إدراكه والشيء إذا ولى وأدبر قد تقارب والقريب السمك المملح ما دام في طراءته (tahdhib)؛ في الزمان نحو اقترب للناس حسابهم (mufradat)؛ كربت الشمس دنت للمغيب (maqayis-ibdal)","source_summary":"Tanıklıklar gelecek bir vaktin yaklaşmasını temel alır; olgunlaşma ve batış evrelerini, geçip gitmeyi ve yakın geçmişten gelen tazeliği de aynı zamansal alanın bağlamsal kullanımları olarak kaydeder.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه اقتراب الوعد والحساب والساعة ودنو إدراك الزرع ودنو الشمس للمغيب وطراءة الشيء وحداثته وما ولى فأدبر","what_is_not_ar":"ليس القرب المكاني المحض ولا قرابة الرحم ولا القربان"},"support_links":["sup_bea0d49e5e6df578106e"]},{"boundary":"Tanım yalnız soy ve aile bağına dayalı yakınlığı kapsar; evlilik, komşuluk ve makam yakınlığı ayrı tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_001212/B003","candidate_links":[{"candidate_id":"cand_196524c06262313fb4fd","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَقْرَبَة","morph_features":"STEM|POS:N|LEM:maqorabap|ROOT:qrb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:3:1","qac_word_ref":"90:15:3","surface_ar":"مَقْرَبَةٍ"}],"gloss":"akrabalık ve yakın akraba","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişiler anne veya baba yönünden soy bağıyla birbirine bağlıdır ve bu bağın derecesine göre yakın akraba sayılır."}}],"root_ar":"ق ر ب","root_id":"root_001212","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Soy bağının kendisini ve bu bağla yakın olan kişiyi birlikte karşılayan genel Türkçe açıklamadır.","boundary_detail":"Tanım yalnız soy ve aile bağına dayalı yakınlığı kapsar; evlilik, komşuluk ve makam yakınlığı ayrı tutulur.","branch_image_ar":"قرابة الرحم والنسب","concept_gloss":"akrabalık ve yakın akraba","contextual_glosses":[{"applicability":"Soy bağıyla kişiye yakın olan bir bireyin söz konusu olduğu cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişiler arasındaki bağın soyut adı olan akrabalığı tek başına karşılamaz.","preserves":"Soy bağı bulunan yakın kişiyi doğal ve açık biçimde karşılar."},"facet_ids":["F001"],"text":"yakın akraba","usage_role":"contextual"}],"definition":"İki kişi arasında anne veya baba tarafından soy ve aile bağı bulunması ya da bu bağla yakın olan kişidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişiler anne veya baba yönünden soy bağıyla birbirine bağlıdır ve bu bağın derecesine göre yakın akraba sayılır."}],"identity_rationale":"Kaynak ifadesi anne veya baba tarafından soy bağıyla yakın olan kişiyi ve bu bağı adlandıran biçimleri açıkça bir araya getirir. Komşuluk, toplumsal ayrıcalık veya genel mekansal yakınlık bu kimliğin kurucu parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"akrabalık, soy bağı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yakın akraba"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yakın akrabalığı olan kimse"}],"lexicalization_note":"Akrabalık çekirdeği genel biçimlerde ve yakın akrabayı belirten kalıplaşmış birimlerde korunur; mekansal yakınlığa genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; soy bağı ile aile dışı bağlılık arasındaki olası karışmayı bu komşu en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal gerçek aile ve soy yakınlığıyla sınırlıdır; komşu dal aynı bağ dilini aile dışı bağlılık ilişkisine de aktarır.","focus_only":"Odak dal anne veya baba yönünden akrabalığı ve yakın akraba derecesini adlandırır.","gloss":"soy bağı","neighbor_only":"Komşu dal soy bağının yanında bağlılık ve koruyuculuk ilişkisini de soy bağına benzeterek kapsar.","neighbor_ref":"root_001348/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da insanlar arasındaki akrabalık bağını temel bir ilişki olarak içerir."}],"source_phrase_ar":"فلان ذو قرابتي وهو من يقرب منك رحما والقربة والقربى القرابة (maqayis)؛ قريب الرجل مدانيه من نسب أم أو أب والجمع قرابة وقرباء وأقرباء (jamhara)؛ القرابة القربى في الرحم وهو قريبي وذو قرابتي وهم أقربائي وأقاربي (sihah)؛ القريب والقريبة ذو القرابة وفلان ذو قرابتي وذو مقربة وذو قربى (tahdhib)؛ في النسبة أولوا القربى والأقربون وذو قربى ولذي القربى والجار ذي القربى ويتيما ذا مقربة (mufradat)","source_summary":"Tanıklıklar kavramı soy ve aile yakınlığı olarak ortaklaştırır; bağı, bu bağın sahiplerini ve yakınlık derecesini bildiren çeşitli adlandırmaları birlikte destekler.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه القريب وذو القرابة والقربى والمقربة والأقربون والأقارب والجار ذو القربى وكل قرب رحم أو نسب","what_is_not_ar":"ليس مجرد قرب المكان ولا حظوة المقربين ولا قرابين الملك"},"support_links":["sup_d222801d97d8d4b15059"]},{"boundary":"Dal, bir makam sahibinin ayrıcalıklı yakın çevresiyle sınırlıdır; akrabalık ve dinsel sunu anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001212/B004","candidate_links":[{"candidate_id":"cand_e49c796183af29c5e8b0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَقْرَبَة","morph_features":"STEM|POS:N|LEM:maqorabap|ROOT:qrb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:3:1","qac_word_ref":"90:15:3","surface_ar":"مَقْرَبَةٍ"}],"gloss":"ayrıcalıklı yakın çevre","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya varlık yüksek makam sahibine ya da Tanrı'ya mevki ve kabul bakımından yakın kılınır ve ayrıcalıklı sayılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hükümdarın oturum arkadaşları, özel çevresi ve yöneticileri bu ayrıcalıklı yakınlığın topluluk olarak adlandırılmış biçimidir."}}],"root_ar":"ق ر ب","root_id":"root_001212","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Makam sahibine yakın tutulma durumunu ve bu konumdaki kişiler topluluğunu birlikte karşılar.","boundary_detail":"Dal, bir makam sahibinin ayrıcalıklı yakın çevresiyle sınırlıdır; akrabalık ve dinsel sunu anlamlarını kapsamaz.","branch_image_ar":"حظوة المقربين وخاصة الملك","concept_gloss":"ayrıcalıklı yakın çevre","contextual_glosses":[{"applicability":"Bir hükümdar veya makam sahibinin ayrıcalık tanıdığı kişilerden söz edilirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yönetici ve oturum arkadaşı gibi tarihsel topluluk adlandırmalarını açıkça belirtmez.","preserves":"Kişilerin kabul ve mevki bakımından ayrıcalıklı yakınlığını korur."},"facet_ids":["F001"],"text":"gözde ve yakın tutulmuş kişiler","usage_role":"explanatory"}],"definition":"Bir hükümdara, yüksek makama veya Tanrı'ya kabul ve mevki bakımından yakın kılınıp ayrıcalık gören kişi ya da varlık; hükümdar bağlamında bu kişilerden oluşan özel çevredir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya varlık yüksek makam sahibine ya da Tanrı'ya mevki ve kabul bakımından yakın kılınır ve ayrıcalıklı sayılır."},{"facet_id":"F002","role":"specialization","statement":"Hükümdarın oturum arkadaşları, özel çevresi ve yöneticileri bu ayrıcalıklı yakınlığın topluluk olarak adlandırılmış biçimidir."}],"identity_rationale":"Kaynak ifadesi bir hükümdara veya yüksek makama yakın tutulup ayrıcalık gören kişileri, özellikle yakın çevreyi, oturum arkadaşlarını ve yöneticileri anlatır. Buradaki yakınlık soy veya mekan değil, mevki ve kabul yakınlığıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yakın kılınmış, gözde kişiler"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"hükümdarın özel çevresi, oturum arkadaşları ve yöneticileri"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yakın kılınmış melekler"}],"lexicalization_note":"Mevki bakımından yakın kılınma çekirdeği ile hükümdarın çevresine özgü adlandırmalar ayrı sözlüksel gerçekleşmeler olarak korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; makam yakınlığı ile sırdaş iç çevre arasındaki ayrımı bu komşu en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın sınırı makam ve ayrıcalıkla çizilir; komşu dalın sınırı ise sırdaşlık ve iç işlere kabul edilmekle çizilir.","focus_only":"Odak dal özellikle hükümdar veya yüksek makam çevresindeki mevki ve ayrıcalık yakınlığını anlatır.","gloss":"özel yakın çevre","neighbor_only":"Komşu dal herhangi bir kişinin sırlarına ve işlerine alınan güvenilir iç çevreyi kapsar.","neighbor_ref":"root_000128/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişinin başkalarından ayırıp kendine yakın tuttuğu özel çevreyi anlatır."}],"source_phrase_ar":"قربان الملك وقرابينه وزراؤه وجلساؤه (maqayis)؛ قرابين الملك خاصته وقربان الملك قرابته والجمع قرابين (jamhara)؛ القربان واحد قرابين الملك وهم جلساؤه وخاصته (sihah)؛ القرابين جلساء الملوك وخاصته وقرابين الملك وزراؤه (tahdhib)؛ في الحظوة الملائكة المقربون ومن المقربين وقربناه نجيا (mufradat)؛ الملائكة الكروبيون وهم المقربون (maqayis-ibdal)","source_summary":"Tanıklıklar mevki bakımından yakın kılınmış kişileri ortak çekirdek olarak verir; hükümdarın özel çevresi, oturum arkadaşları ve yöneticileri bu çekirdeğin belirgin topluluk örnekleridir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه المقربون وأهل الحظوة وقربان الملك وقرابين الملك وخاصته وجلساؤه ووزراؤه","what_is_not_ar":"ليس قرابة النسب ولا القربان بمعنى النسيكة ولا قرب المكان"},"support_links":["sup_445e7b651dd2ef824320"]},{"boundary":"Amaç Tanrı'ya yakınlık kazanmaktır; kesilen hayvan önemli bir özel türdür, fakat kavram yalnız kesime indirgenmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001212/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَقْرَبَة","morph_features":"STEM|POS:N|LEM:maqorabap|ROOT:qrb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:3:1","qac_word_ref":"90:15:3","surface_ar":"مَقْرَبَةٍ"}],"gloss":"Tanrı'ya yakınlık kazandıran iş veya sunu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir iş veya sunu aracılığıyla Tanrı'ya yakınlık kazanmayı amaçlar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu amaçla kesilip sunulan hayvan, genel aracın özel ve adlaşmış bir türüdür."}}],"root_ar":"ق ر ب","root_id":"root_001212","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel amacı ve bu amaçla kullanılan aracı, yalnız hayvan kesmeye daraltmadan birlikte karşılar.","boundary_detail":"Amaç Tanrı'ya yakınlık kazanmaktır; kesilen hayvan önemli bir özel türdür, fakat kavram yalnız kesime indirgenmez.","branch_image_ar":"القربة والقربان إلى الله","concept_gloss":"Tanrı'ya yakınlık kazandıran iş veya sunu","contextual_glosses":[{"applicability":"Tanrı'ya yakınlık kazanmak amacıyla sunulan veya kesilen belirli bir şeyden söz edilirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Maddi bir sunu olmayan iyi işleri ve genel yakınlık kazanma sürecini dışarıda bırakır.","preserves":"Dinsel amaçla sunulan şeyi ve sunma eyleminin yöneldiği yakınlık arzusunu korur."},"facet_ids":["F002"],"text":"adak sunusu","usage_role":"contextual"}],"definition":"Tanrı'ya yakınlık kazanma amacıyla yapılan iyi iş veya sunulan şeydir. Kesilen hayvan bu amaca yönelik sununun yaygın ve adlaşmış özel bir türüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir iş veya sunu aracılığıyla Tanrı'ya yakınlık kazanmayı amaçlar."},{"facet_id":"F002","role":"specialization","statement":"Bu amaçla kesilip sunulan hayvan, genel aracın özel ve adlaşmış bir türüdür."}],"identity_rationale":"Kaynak ifadesi Tanrı'ya yakınlık kazanmak amacıyla yapılan işi veya sunulan şeyi çekirdek kabul eder; kesilen hayvan bunun yaygın ve adlaşmış bir türüdür. Hükümdarın yakın çevresiyle ilgili eşsesli kullanım bu dala girmez.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"Tanrı'ya yakınlık kazandıran iyi iş veya araç"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"Tanrı'ya yakınlık için sunulan şey veya kesilen hayvan"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"iyi bir iş veya sunuyla Tanrı'ya yakınlık aramak"}],"lexicalization_note":"Yakınlık kazanma amacı ile bu amaçla sunulan şeyin adı birlikte korunur; kesilen hayvan yalnız özel bir gerçekleştirimdir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yakınlık aracı ile hayvan kesmeye özgü sunu arasındaki sınırı bu komşu en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Kesilen hayvan odak dalın yalnız özel bir türüdür; komşu dalın çekirdeği ise doğrudan bu kesim ve kanlı sunudur.","focus_only":"Odak dal kesim dışındaki iyi işleri ve sunuları da Tanrı'ya yakınlık kazanma amacıyla kapsar.","gloss":"yakınlık için sunulan kurbanlık","neighbor_only":"Komşu dal özellikle kesilen hayvanı ve akıtılan kanı adlandırır.","neighbor_ref":"root_001498/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da Tanrı'ya yakınlık amacıyla kesilip sunulan hayvan bulunur."}],"source_phrase_ar":"القربان ما قرب إلى الله تعالى من نسيكة أو غيرها (maqayis)؛ ما له عند الله قربة والقربان الأضاحي وكل ما تقرب إلى الله فهو قربان (jamhara)؛ القربان ما تقربت به إلى الله وتقرب إلى الله بشيء طلب به القربة (sihah)؛ القربان ما قربت إلى الله تبتغي بذلك قربة ووسيلة وهي ذبائح كانوا يذبحونها (tahdhib)؛ القربان ما يتقرب به إلى الله وصار اسما للنسيكة التي هي الذبيحة والقربة قربات عند الله (mufradat)","source_summary":"Tanıklıklar kavramı Tanrı'ya yakınlık kazanmak için yapılan veya sunulan şey olarak birleştirir; hayvan kesip sunmayı genel amacın belirgin özel türü sayar.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه القربة والقربات والتقرب إلى الله والقربان والنسيكة والذبيحة وكل ما يتوسل به طالبا القربة","what_is_not_ar":"ليس قرابين الملك ولا مجرد الحظوة الاجتماعية ولا قرب الرحم"},"support_links":[]},{"boundary":"Yakınlık bedensel veya mekansal değildir; Tanrı ve insan yönleri farklı ilişkilerle açıklanmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001212/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَقْرَبَة","morph_features":"STEM|POS:N|LEM:maqorabap|ROOT:qrb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:3:1","qac_word_ref":"90:15:3","surface_ar":"مَقْرَبَةٍ"}],"gloss":"gözetme, güç ve ruhsal yöneliş bakımından yakınlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tanrı'nın insana yakınlığı gözetme, karşılık verme ve iyilik ulaştırma ilişkisiyle gerçekleşir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tanrı'nın yakınlığı, insan üzerindeki güç ve erişiminin eksiksiz oluşunu da anlatır."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsanın Tanrı'ya yakınlığı bedensel değil, ruhsal yöneliş ve ilişki bakımındandır."}}],"root_ar":"ق ر ب","root_id":"root_001212","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İlişkinin iki yönünü ve mekansal olmadığını birlikte koruyan açıklayıcı karşılıktır.","boundary_detail":"Yakınlık bedensel veya mekansal değildir; Tanrı ve insan yönleri farklı ilişkilerle açıklanmalıdır.","branch_image_ar":"القرب بالرعاية والقدرة","concept_gloss":"gözetme, güç ve ruhsal yöneliş bakımından yakınlık","contextual_glosses":[{"applicability":"Tanrı'nın insana yakınlığının gözetme ve çağrıya karşılık verme yönünü açıklayan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güç yönünü ve insanın Tanrı'ya ruhsal yakınlığını dışarıda bırakır.","preserves":"Gözetme ve karşılık verme ilişkisini mekansal yakınlığa çevirmeden korur."},"facet_ids":["F001"],"text":"gözetip karşılık vermek üzere yakın","usage_role":"explanatory"}],"definition":"Tanrı'nın insana gözetme, karşılık verme, güç ve iyilik ulaştırma bakımından yakın olması ya da insanın Tanrı'ya ruhsal olarak yönelip yakınlık kurmasıdır. Bu ilişki yer veya beden yakınlığı değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tanrı'nın insana yakınlığı gözetme, karşılık verme ve iyilik ulaştırma ilişkisiyle gerçekleşir."},{"facet_id":"F002","role":"core","statement":"Tanrı'nın yakınlığı, insan üzerindeki güç ve erişiminin eksiksiz oluşunu da anlatır."},{"facet_id":"F003","role":"core","statement":"İnsanın Tanrı'ya yakınlığı bedensel değil, ruhsal yöneliş ve ilişki bakımındandır."}],"identity_rationale":"Kaynak ifadesi mekansal olmayan iki yönlü bir ilişki kurar: Tanrı'nın insana yakınlığı gözetme, karşılık verme, güç ve iyilikle; insanın Tanrı'ya yakınlığı ise ruhsal yönelişle açıklanır. Bu katılımcı ayrımı dalın kimliğini belirler.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"gözetip karşılık vermek üzere yakın"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"gücü ve erişimi bakımından insana en yakından hakim"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"insanın Tanrı'ya ruhsal yakınlığı"}],"lexicalization_note":"Mekansal olmayan yakınlık yalnız Tanrı-insan ilişkisini belirten yapılarda korunur; genel yer yakınlığına dönüştürülmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; mecazi ve ilişkisel kullanımın genel yakınlıkla karışmasını aynı kökün temel dalı en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda yakınlık bir yer ölçüsü değildir ve katılımcı yönüne göre gözetme, güç ya da ruhsal yöneliş demektir; komşu dal genel yakınlık ilişkisidir.","focus_only":"Odak dal gözetme, güç, iyilik ve ruhsal yönelişten oluşan Tanrı-insan ilişkisini anlatır.","gloss":"mekansal olmayan ilahi yakınlık","neighbor_only":"Komşu dal yer veya anlam bakımından genel uzak olmama, yaklaşma ve yaklaştırma ilişkisini anlatır.","neighbor_ref":"root_001212/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da uzaklığın karşıtı olan yakınlık dilinden yararlanır."}],"source_phrase_ar":"في الرعاية نحو فإني قريب أجيب دعوة الداع وفي القدرة نحو ونحن أقرب إليه من حبل الوريد وقرب الله تعالى من العبد هو بالإفضال عليه والفيض لا بالمكان وقرب العبد من الله قرب روحاني لا بدني (mufradat)","source_summary":"Tek tanıklık, Tanrı'dan insana yönelen gözetme, karşılık, güç ve iyilik ile insandan Tanrı'ya yönelen ruhsal yakınlığı ayırır ve her ikisini de mekansal yakınlığın dışında tutar.","sources":["MU"],"what_is_ar":"يدخل فيه القرب الذي يفسر بالرعاية والإجابة والإفضال والقدرة والقرب الروحاني لا قرب المكان","what_is_not_ar":"ليس الدنو المكاني ولا القرابة ولا القربان المذبوح"},"support_links":[]},{"boundary":"Dal, bir işe veya kişiye temas ve dahil olma sınırına yaklaşmayı anlatır; salt mesafe yakınlığı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001212/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَقْرَبَة","morph_features":"STEM|POS:N|LEM:maqorabap|ROOT:qrb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:3:1","qac_word_ref":"90:15:3","surface_ar":"مَقْرَبَةٍ"}],"gloss":"temas edip içine girecek ölçüde yaklaşma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir işe yalnız mesafece yaklaşmaz; onunla temas kurar, içine girer veya gerçekleşme sınırına varır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yasak bir şeye yaklaşmama buyruğu, eylemin kendisinden önce ona götüren temas ve yönelişi de engeller."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Eşe yaklaşma sözü, cinsel ilişkiyi dolaylı biçimde anlatan özel bir kullanımdır."}}],"root_ar":"ق ر ب","root_id":"root_001212","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Salt mesafeyi değil, bir işe karışma veya onu gerçekleştirme sınırına varmayı karşılar.","boundary_detail":"Dal, bir işe veya kişiye temas ve dahil olma sınırına yaklaşmayı anlatır; salt mesafe yakınlığı değildir.","branch_image_ar":"مقاربة الشيء وملابسته","concept_gloss":"temas edip içine girecek ölçüde yaklaşma","contextual_glosses":[{"applicability":"Bir işin sınırında kalmayıp onunla temas kurma ve içine girme bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yasağa götüren ön davranışları ve cinsel ilişkiyi dolaylı anlatan kullanımı dışarıda bırakır.","preserves":"İşe temas etme ve onun içine girme yönünü açık biçimde korur."},"facet_ids":["F001"],"text":"bir işe bulaşmak veya girişmek","usage_role":"contextual"},{"applicability":"Eşe yaklaşma sözünün cinsel ilişkiyi dolaylı anlattığı özel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel işe karışma çekirdeğini ve yasak eyleme yaklaşmama kapsamını dışarıda bırakır.","preserves":"Eşe yaklaşmanın bağlama özgü cinsel ilişki anlamını açıkça korur."},"facet_ids":["F003"],"text":"eşle cinsel ilişkide bulunmak","usage_role":"contextual"}],"definition":"Bir işe veya şeye temas edecek, onun içine girecek ya da onu gerçekleştirecek ölçüde yaklaşmaktır. Yasak bir şeye hiç yönelmeme buyruğu ve eşle cinsel ilişki bu sınır yakınlığının özel kullanımlarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir işe yalnız mesafece yaklaşmaz; onunla temas kurar, içine girer veya gerçekleşme sınırına varır."},{"facet_id":"F002","role":"extension","statement":"Yasak bir şeye yaklaşmama buyruğu, eylemin kendisinden önce ona götüren temas ve yönelişi de engeller."},{"facet_id":"F003","role":"associated_use","statement":"Eşe yaklaşma sözü, cinsel ilişkiyi dolaylı biçimde anlatan özel bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi bir işe yalnız mesafece yaklaşmayı değil, onunla temas kurmayı, içine girmeyi veya gerçekleşme sınırına varmayı anlatır. Yasak şeye yaklaşmama ve eşle cinsel ilişki bu ilişki çekirdeğinin belirgin bağlamsal kullanımlarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bir işe bulaşmak, girişmek veya onu yapmak üzere olmak"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"yasak şeye yönelmemek ve onunla temas kurmamak"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"eşiyle cinsel ilişkide bulunmak"}],"lexicalization_note":"İşe karışma çekirdeği ile yasaktan uzak durma ve cinsel ilişki yapıları ayrı bağlamsal kullanımlar olarak korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yaklaşma ile fiilen karışma arasındaki sınırı bu komşu en güçlü biçimde aydınlatır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal temas eşiğine yaklaşmayı ve bu eşiği yasaklayan yapıları merkezde tutar; komşu dal gerçekleşmiş karışma ve işleme sonucuna daha geniş yer verir.","focus_only":"Odak dal yasak şeye yaklaşmama buyruğunu ve buyruktaki önleyici kapsamı ayrıca içerir.","gloss":"yaklaşıp karışma","neighbor_only":"Komşu dal yanlış bir işi işleme, bir şeye karışma ve genel karışım adlarını daha geniş biçimde kapsar.","neighbor_ref":"root_001220/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da bir işe yaklaşmanın onunla temas ve karışmaya dönüşmesini, ayrıca cinsel ilişki kullanımını içerir."}],"source_phrase_ar":"ما قربت هذا الأمر ولا أقربه إذا لم تشامه ولم تلتبس به (maqayis)؛ قرب فلان أهله قربانا إذا غشيها وما قربت هذا الأمر ولا قربته ولا تقربا هذه الشجرة ولا تقربوا الزنى (tahdhib)؛ ولا تقربوهن كناية عن الجماع ولا تقربوا مال اليتيم أبلغ من النهي عن تناوله ولا تقربوا الزنى (mufradat)","source_summary":"Tanıklıklar bir işle temas kurup ona karışmayı çekirdek kabul eder; yasağa yaklaşmama ifadesini kapsamlı önleme, eşe yaklaşmayı ise cinsel ilişkiyi dolaylı anlatma olarak açıklar.","sources":["MQ","TA","MU"],"what_is_ar":"يدخل فيه قرب الأمر أو الشيء بمعنى ملابسته ومشارفته والنهي عن قرب المحظور وقربان المرأة كناية عن الجماع","what_is_not_ar":"ليس مجرد المسافة ولا القربة الدينية ولا قراب السيف"},"support_links":[]},{"boundary":"Dal, gece yürüyüşünü yalnız suya ulaşma amacı ve yaklaşan sulama vaktiyle birlikte kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001212/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَقْرَبَة","morph_features":"STEM|POS:N|LEM:maqorabap|ROOT:qrb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:3:1","qac_word_ref":"90:15:3","surface_ar":"مَقْرَبَةٍ"}],"gloss":"geceleyin su kaynağına yönelme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Topluluk veya hayvanlar, ertesi gün suya varmak üzere geceleyin su kaynağına doğru yürür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Suya varış yaklaşınca yürüyüş hızlanabilir ve hayvanlar kaynağa doğru sertçe sürülebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gece su arayan kişi veya hayvan ile bu yolculuğun gecesi olaydan türeyen adlarla belirtilir."}}],"root_ar":"ق ر ب","root_id":"root_001212","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yolculuğun zamanını, suya ulaşma amacını ve kaynağa yaklaşma hareketini birlikte karşılar.","boundary_detail":"Dal, gece yürüyüşünü yalnız suya ulaşma amacı ve yaklaşan sulama vaktiyle birlikte kapsar.","branch_image_ar":"ليلة القرب وطلب الماء","concept_gloss":"geceleyin su kaynağına yönelme","contextual_glosses":[{"applicability":"İnsan veya hayvan topluluğunun ertesi günkü suya varış için gece yol aldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Acele ettirme ile su arayan varlık ve yolculuk gecesinin adlarını dışarıda bırakır.","preserves":"Gece hareketini ve suya ulaşma amacını açık biçimde korur."},"facet_ids":["F001"],"text":"suya varmak için gece yürümek","usage_role":"contextual"}],"definition":"İnsanların veya hayvanların suya varış vakti yaklaşınca geceleyin hızlanarak su kaynağına yönelmesidir. Bu yolculuğun gecesi ve gece su arayan varlık da aynı olaydan adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Topluluk veya hayvanlar, ertesi gün suya varmak üzere geceleyin su kaynağına doğru yürür."},{"facet_id":"F002","role":"specialization","statement":"Suya varış yaklaşınca yürüyüş hızlanabilir ve hayvanlar kaynağa doğru sertçe sürülebilir."},{"facet_id":"F003","role":"associated_use","statement":"Gece su arayan kişi veya hayvan ile bu yolculuğun gecesi olaydan türeyen adlarla belirtilir."}],"identity_rationale":"Kaynak ifadesi insanların veya hayvanların suya varış yaklaşınca geceleyin aceleyle su kaynağına yönelmesini ve bu yolculuğun gecesini anlatır. Suyu arayan kişi veya hayvan da aynı amaçlı hareketten adlandırılır.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"suya varıştan önceki gece yolculuğu"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"su arayıp kaynağa doğru gitmek"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"geceleyin su arayan kişi veya hayvan"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"suya doğru giderken acele etmek"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"suya gidip gelen hiç kimsesi yok"}],"lexicalization_note":"Suya gece yönelme olayı, bu gecenin adı ve su arayan varlık ayrı sözlüksel yapılarda tutulur; genel gece yolculuğuna genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gece yolculuğu ile suya yönelik özel yürüyüş arasındaki sınırı bu komşu en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda suya ulaşma amacı ve yaklaşan varış nedeniyle hızlanma kurucudur; komşu dalda gece yolculuğunun amacı sınırlı değildir.","focus_only":"Odak dal gece yürüyüşünü özellikle su kaynağına ulaşma ve hayvanları sulama amacıyla sınırlar.","gloss":"gece yolculuğu","neighbor_only":"Komşu dal insan, topluluk veya bulutun herhangi bir amaçla gece ilerlemesini kapsar.","neighbor_ref":"root_000702/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın çekirdeğinde geceleyin yol alma bulunur."}],"source_phrase_ar":"من الباب القرب وهي ليلة ورود الإبل الماء والقارب الطالب الماء ليلا (maqayis)؛ القرب أن يرعى القوم بينهم وبين المورد حتى إذا كان بينهم وبين الماء عشية أو ليلة عجلوا فقربوا وحمار قارب يطلب الماء (ayn)؛ قربت الإبل الماء إذا طلبته وليلة القرب ليلة طلب الماء (jamhara)؛ القرب سير الليل لورد الغد والقارب طالب الماء ليلا (sihah)؛ ليلة القرب هو السوق الشديد وتقرب أي اعجل وقربت الماء أي طلبته والقرب سير الليل (tahdhib)؛ رجل قارب قرب من الماء وليلة القرب وأقربوا إبلهم (mufradat)","source_summary":"Tanıklıklar suya varıştan önceki gece yürüyüşünü, kaynağa doğru acele ettirmeyi ve su arayan varlığı ortak bir olay çevresinde birleştirir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه سير القوم والإبل نحو الماء عند قرب الورد وليلة القرب والقارب طالب الماء ليلا والعجلة والسوق الشديد إلى المورد","what_is_not_ar":"ليس القربة الوعاء ولا القارب السفينة ولا القرب المكاني العام"},"support_links":[]},{"boundary":"Tanım su almaya yarayan su tulumuyla sınırlıdır; başka kaplar ve suya gitme olayı ayrı tutulur.","branch_kind":"bare","branch_ref":"root_001212/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَقْرَبَة","morph_features":"STEM|POS:N|LEM:maqorabap|ROOT:qrb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:3:1","qac_word_ref":"90:15:3","surface_ar":"مَقْرَبَةٍ"}],"gloss":"su tulumu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne su çekmek ve taşımak için kullanılan bir su kabıdır."}}],"root_ar":"ق ر ب","root_id":"root_001212","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Su çekme ve taşıma işlevli kabı doğal ve doğrudan karşılayan Türkçe addır.","boundary_detail":"Tanım su almaya yarayan su tulumuyla sınırlıdır; başka kaplar ve suya gitme olayı ayrı tutulur.","branch_image_ar":"القربة وعاء الماء","concept_gloss":"su tulumu","contextual_glosses":[{"applicability":"Nesnenin biçim ve kullanımını tanımayan okur için açıklayıcı karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesnenin kap oluşunu, su taşıma işlevini ve yaygın deri malzemesini korur."},"facet_ids":["F001"],"text":"deri su kabı","usage_role":"explanatory"}],"definition":"Kuyudan veya başka bir kaynaktan su çekmek ve su taşımak için kullanılan, çoğunlukla deriden yapılmış su tulumudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne su çekmek ve taşımak için kullanılan bir su kabıdır."}],"identity_rationale":"Kaynak ifadesi su çekmek ve taşımak için kullanılan bilinen deri su kabını açıkça adlandırır. Su arama gecesi, kılıç kabı ve doluluğa yaklaşma anlamları bu nesne kimliğine dahil değildir.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"su tulumu, deri su kabı"}],"lexicalization_note":"Çıplak dal yalnız su çekilen ve taşınan su tulumunu tanımlar; başka kalıplaşmış yakınlık anlamları içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı kap alanındaki özel büyük veya birleşik su kabı en yararlı sınır karşılaştırmasını sağlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal işlev bakımından genel su tulumudur; komşu dal biçimi, büyüklüğü veya birleşik yapısıyla belirlenen ayrı bir kap türüdür.","focus_only":"Odak dal genel olarak su çekip taşımaya yarayan su tulumunu adlandırır.","gloss":"deri su kabı","neighbor_only":"Komşu dal büyük, parçaları birleştirilmiş veya eskidiğinde su sızdırabilen özel bir su kabını da adlandırır.","neighbor_ref":"root_000797/B007","relation_type":"near_neighbor","shared_zone":"Her iki dalda da sıvı, özellikle su taşımaya yarayan deri kap bulunur."}],"source_phrase_ar":"القربة معروفة (jamhara)؛ القربة ما يستقى فيه الماء والجمع قربات وقربات وقربات وللكثير قرب (sihah)؛ القربة وجمعها قرب من الأساقي (tahdhib)","source_summary":"Tanıklıklar sözcüğü su çekmeye yarayan bilinen bir su tulumu olarak ortak biçimde tanımlar ve tekil ile çoğul biçimlerini kaydeder.","sources":["JA","SI","TA"],"what_is_ar":"يدخل فيه القربة التي يستقى فيها الماء وجمعها قرب وقربات","what_is_not_ar":"ليس ليلة طلب الماء ولا قراب السيف ولا القارب السفينة"},"support_links":[]},{"boundary":"Kavram kılıç veya bıçak kabıdır; bazı kullanımlarda kının kendisini, bazılarında kını saran dış deri kabı belirtir.","branch_kind":"mixed_non_bare","branch_ref":"root_001212/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَقْرَبَة","morph_features":"STEM|POS:N|LEM:maqorabap|ROOT:qrb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:3:1","qac_word_ref":"90:15:3","surface_ar":"مَقْرَبَةٍ"}],"gloss":"kılıç kını veya deri dış kabı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne kılıç veya bıçağı içinde taşıyan kap ya da kını çevreleyen deri dış kaptır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kılıcı kaba yerleştirmek veya ona bir kap sağlamak aynı sözlüksel alandaki eylem kullanımıdır."}}],"root_ar":"ق ر ب","root_id":"root_001212","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynaklardaki kın ile kının dışındaki deri kap ayrımını silmeden nesnenin ortak işlevini karşılar.","boundary_detail":"Kavram kılıç veya bıçak kabıdır; bazı kullanımlarda kının kendisini, bazılarında kını saran dış deri kabı belirtir.","branch_image_ar":"قراب السيف ووعاؤه","concept_gloss":"kılıç kını veya deri dış kabı","contextual_glosses":[{"applicability":"Kın ile dış deri kap ayrımının bağlamda önemli olmadığı genel anlatımlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kabın bazı tanıklıklarda kının kendisi, bazılarında ise kının dışındaki deri parça olması ayrımını belirsiz bırakır.","preserves":"Nesnenin kılıcı taşıyan ve koruyan kap işlevini korur."},"facet_ids":["F001"],"text":"kılıç kabı","usage_role":"general"}],"definition":"Kılıç veya bıçağın taşındığı kın ya da kını ve askısını çevreleyen deri dış kaptır. Aynı söz alanı, kılıcı bu kaba koyma işlemini de anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne kılıç veya bıçağı içinde taşıyan kap ya da kını çevreleyen deri dış kaptır."},{"facet_id":"F002","role":"associated_use","statement":"Kılıcı kaba yerleştirmek veya ona bir kap sağlamak aynı sözlüksel alandaki eylem kullanımıdır."}],"identity_rationale":"Kaynak ifadesi kılıç veya bıçağın içinde taşındığı kabı ortaklaştırır, fakat bunun doğrudan kın mı yoksa kının üstündeki deri dış kap mı olduğu konusunda iki sınır verir. Dal korunabilir, ancak bu nesne farkı tanımda açık bırakılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"kılıç kını veya kını saran deri kap"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"kılıcı kabına koymak veya ona bir kap yapmak"}],"lexicalization_note":"Kılıç kabı adı ile kılıcı bu kaba koyma yapısı birlikte korunur; su tulumuna veya genel kap anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kın ile kınlı kılıcı alan deri çanta arasındaki karışmayı bu komşu en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kılıca doğrudan bağlı kın veya dış kın alanındadır; komşu dal kınlı kılıcı başka araçlarla birlikte alabilen daha geniş bir taşıma çantasıdır.","focus_only":"Odak dal kılıç veya bıçak kınını ya da kını saran dış deri kabı ve kaba koyma eylemini kapsar.","gloss":"kılıç için deri kap","neighbor_only":"Komşu dal kılıcın kınlı olarak konduğu deri çantayı ve binici araçlarının da taşındığı daha geniş kabı kapsar.","neighbor_ref":"root_000252/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da kılıcın taşındığı deri bir koruyucu kabı anlatır."}],"source_phrase_ar":"منه القراب قراب السيف والجمع قرب (maqayis)؛ قراب السيف جلد يكون فيه وليس بالغمد والجمع قرب (jamhara)؛ قراب السيف جفنه وهو وعاء يكون فيه السيف بغمده وحمالته (sihah)؛ القراب للسيف والسكين وقربته جعلته في القراب (tahdhib)؛ القراب وعاء السيف وقيل جلد فوق الغمد لا الغمد نفسه (mufradat)","source_summary":"Tanıklıklar kılıç veya bıçak için bir taşıma kabında birleşir; kabın doğrudan kın mı yoksa kının üzerindeki deri dışlık mı sayılacağı konusunda iki açıklama sunar ve kılıcı kaba koyma eylemini de kaydeder.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه قراب السيف والسكين والجراب أو الجلد الذي يكون فيه السيف وجعل السيف في القراب","what_is_not_ar":"ليس القربة وعاء الماء ولا قراب الامتلاء ولا الخاصرة"},"support_links":[]},{"boundary":"Dal, büyük gemiye bağlı veya onun hizmetinde kullanılan küçük tekneyle sınırlıdır.","branch_kind":"bare","branch_ref":"root_001212/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَقْرَبَة","morph_features":"STEM|POS:N|LEM:maqorabap|ROOT:qrb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:3:1","qac_word_ref":"90:15:3","surface_ar":"مَقْرَبَةٍ"}],"gloss":"gemiye bağlı küçük hizmet teknesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Küçük tekne büyük bir deniz gemisine eşlik eder ve gemidekilerin kısa işleri için kullanılır."}}],"root_ar":"ق ر ب","root_id":"root_001212","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Küçüklüğü, ana gemiyle ilişkisini ve hizmet işlevini birlikte karşılayan açıklamadır.","boundary_detail":"Dal, büyük gemiye bağlı veya onun hizmetinde kullanılan küçük tekneyle sınırlıdır.","branch_image_ar":"القارب السفينة الصغيرة","concept_gloss":"gemiye bağlı küçük hizmet teknesi","contextual_glosses":[{"applicability":"Ana gemiye bağlı küçük teknenin hizmet veya kısa ulaşım amacıyla kullanıldığı bağlamlarda uygundur.","error_profile":{"adds":"Modern kullanımda özellikle can kurtarma işlevini çağrıştırabilir; kaynak çekirdeğinde bu işlev zorunlu değildir.","collision":null,"fit":"broadening","loses":null,"preserves":"Ana gemide taşınabilen veya ona bağlı küçük tekne düşüncesini korur."},"facet_ids":["F001"],"text":"filika","usage_role":"contextual"}],"definition":"Büyük deniz gemisinin yanında bulunan, onu izleyen veya gemidekilerin kısa süreli işleri için kullanılan küçük teknedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Küçük tekne büyük bir deniz gemisine eşlik eder ve gemidekilerin kısa işleri için kullanılır."}],"identity_rationale":"Kaynak ifadesi büyük deniz gemilerinin yanında bulunan, onları izleyen veya kısa işler için kullanılan küçük tekneyi açıkça tanımlar. Gece su arayan kişiyle eşseslilik, nesnenin kimliğine dahil değildir.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"gemiye eşlik eden küçük hizmet teknesi"}],"lexicalization_note":"Çıplak dal küçük hizmet teknesini tanımlar; su arayan kişi anlamı veya genel gemi adı içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel küçük tekne ile ana geminin hizmet teknesi arasındaki sınırı bu komşu en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kimliği ana gemiyle işlevsel bağlılığa dayanır; komşu dal ise bu ilişkiyi gerektirmeyen genel bir küçük tekne adıdır.","focus_only":"Odak dal küçük teknenin büyük deniz gemisine eşlik etmesini ve onun işleri için kullanılmasını şart koşar.","gloss":"küçük tekne","neighbor_only":"Komşu dal küçük tekneyi ana gemiye bağlı olma veya hizmet amacı şartı olmadan adlandırır.","neighbor_ref":"root_000631/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da küçük bir tekne türünü anlatır."}],"source_phrase_ar":"القارب سفينة صغيرة تكون مع أصحاب السفن البحرية وكأنها سميت بذلك لقربها منهم (maqayis)؛ قارب السفينة وهو الصغير الذي يتبعها (jamhara)؛ القارب سفينة صغيرة تكون مع أصحاب السفن البحرية تستخف لحوائجهم (sihah)؛ القارب سفينة صغيرة تكون مع أصحاب السفن البحرية تستخف لحوائجهم والجميع القوارب (tahdhib)","source_summary":"Tanıklıklar nesneyi büyük deniz gemisine eşlik eden ve gemi sahiplerinin işleri için kullanılan küçük tekne olarak ortak biçimde tanımlar.","sources":["MQ","JA","SI","TA"],"what_is_ar":"يدخل فيه القارب وهو سفينة صغيرة تتبع السفن أو تكون مع أصحاب السفن لحوائجهم","what_is_not_ar":"ليس القارب طالب الماء ولا قرب الإبل من الماء"},"support_links":[]},{"boundary":"Yaklaşan doğum kurucudur; sözlüksel adlandırmanın deveye uygulanması tanıklıklarda açıkça sınırlandırılır.","branch_kind":"mixed_non_bare","branch_ref":"root_001212/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَقْرَبَة","morph_features":"STEM|POS:N|LEM:maqorabap|ROOT:qrb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:3:1","qac_word_ref":"90:15:3","surface_ar":"مَقْرَبَةٍ"}],"gloss":"doğumu yaklaşmış gebe dişi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gebe dişinin doğum veya yavrulama vakti yaklaşmıştır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırma koyun, kısrak, kadın ve dişi eşek için tanıklanırken bazı tanıklıklarda deve kapsam dışında tutulur."}}],"root_ar":"ق ر ب","root_id":"root_001212","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaklaşan doğum evresini ve bu evredeki dişiyi birlikte karşılar; tür sınırlaması ayrıca belirtilmelidir.","boundary_detail":"Yaklaşan doğum kurucudur; sözlüksel adlandırmanın deveye uygulanması tanıklıklarda açıkça sınırlandırılır.","branch_image_ar":"دنو الولادة في الحيوان","concept_gloss":"doğumu yaklaşmış gebe dişi","contextual_glosses":[{"applicability":"Koyun, kısrak, kadın veya dişi eşeğin doğum vaktinin yakın olduğunu bildiren cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bu durumdaki dişiyi adlandıran isim kullanımını ve deveye ilişkin sözlüksel sınırlamayı tek başına göstermez.","preserves":"Doğum vaktinin yaklaşması olayını doğal bir fiil yapısıyla korur."},"facet_ids":["F001"],"text":"doğumu yaklaşmak","usage_role":"contextual"}],"definition":"Koyun, kısrak, kadın veya dişi eşek gibi gebe bir dişinin doğum vaktinin yaklaşması ya da bu durumdaki dişidir. Bazı tanıklıklarda aynı adlandırmanın deve için kullanılmadığı belirtilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gebe dişinin doğum veya yavrulama vakti yaklaşmıştır."},{"facet_id":"F002","role":"source_variant","statement":"Adlandırma koyun, kısrak, kadın ve dişi eşek için tanıklanırken bazı tanıklıklarda deve kapsam dışında tutulur."}],"identity_rationale":"Kaynak ifadesi doğumu yaklaşmış gebe dişiyi ortaklaştırır ve koyun, kısrak, kadın ile dişi eşek örneklerini verir. Bununla birlikte bazı tanıklıklar aynı adlandırmayı deve için kullanmamayı özellikle belirttiğinden tanım bütün gebe hayvanlara sınırsızca genellenemez.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"koyunun doğumu yaklaşmak"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"doğumu yaklaşmış gebe dişi"}],"lexicalization_note":"Doğumu yaklaşma olayı ile bu durumdaki dişinin adı birlikte korunur; yapı bütün hayvan türlerine genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ortak olay çekirdeğine rağmen deve kapsamındaki farkı gösteren bu komşu en yararlı karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Olay çekirdeği ortaktır; ayrım, odak daldaki tarihsel sözlüksel biçimin türlere göre sınırlı dağılım göstermesidir.","focus_only":"Odak dal belirli sözlüksel biçimi koyun, kısrak, kadın ve dişi eşek için tanıklar, bazı tanıklıklarda deveyi dışlar.","gloss":"doğumu yaklaşmış gebe","neighbor_only":"Komşu dal doğumu yaklaşmış gebe varlığı daha genel biçimde anlatır ve deveyi de açıkça kapsayabilir.","neighbor_ref":"root_000548/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da gebe dişinin doğum veya yavrulama vaktinin yaklaşmasını anlatır."}],"source_phrase_ar":"أقربت الشاة دنا نتاجها (maqayis)؛ شاة مقرب إذا دنا ولادها (jamhara)؛ أقربت المرأة إذا قرب ولادها وكذلك الفرس والشاة فهي مقرب ولا يقال للناقة (sihah)؛ أقربت الشاة والأتان فهي مقرب ولا يقال للناقة إلا إذا أدنت فهي مدن (tahdhib)؛ المقرب الحامل التي قربت ولادتها (mufradat)","source_summary":"Tanıklıklar doğumu yaklaşmış gebe dişide birleşir; tür örnekleri koyun, kısrak, kadın ve dişi eşeğe uzanır, deve içinse açık bir kullanım sınırlaması bildirilir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الشاة والفرس والمرأة والأتان إذا دنا نتاجها أو ولادها وصارت مقربا أو مقربة","what_is_not_ar":"ليس الناقة في بعض المصادر ولا الفرس المقربة المكرمة ولا قرابة الرحم"},"support_links":[]},{"boundary":"Dal yalnız hazırlanıp yakında tutulan binek hayvanlarına özgü adlandırmaları kapsar; genel hayvan veya gebelik adı değildir.","branch_kind":"non_bare","branch_ref":"root_001212/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَقْرَبَة","morph_features":"STEM|POS:N|LEM:maqorabap|ROOT:qrb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:3:1","qac_word_ref":"90:15:3","surface_ar":"مَقْرَبَةٍ"}],"gloss":"yakında tutulan ve binmeye hazırlanan hayvan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"At kullanılmaya hazır biçimde yakında tutulur, gözetilir ve değer verilerek başıboş bırakılmaz."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Develer binmek amacıyla bağlanmış, donatılmış veya üzerlerine eyer konmuş durumda olabilir."}}],"root_ar":"ق ر ب","root_id":"root_001212","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Atla ilgili gözetme ve hazırlığı, deveyle ilgili bağlama ve eyerlemeyi ortak binek işlevinde birleştirir.","boundary_detail":"Dal yalnız hazırlanıp yakında tutulan binek hayvanlarına özgü adlandırmaları kapsar; genel hayvan veya gebelik adı değildir.","branch_image_ar":"الخيل والإبل المقربة","concept_gloss":"yakında tutulan ve binmeye hazırlanan hayvan","contextual_glosses":[{"applicability":"At veya devenin yakın yerde hazır ve donatılmış durumda tutulduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Atın özellikle değer görüp başıboş bırakılmaması ile devenin bağlanıp eyerlenmesi ayrıntılarını birleştirir.","preserves":"Binek hayvanının kullanılmaya hazır ve yakın tutulması özelliklerini korur."},"facet_ids":["F001","F002"],"text":"binmeye hazır tutulmuş","usage_role":"contextual"}],"definition":"Atın kullanılmaya hazır biçimde yakında tutulup gözetilmesi ve değer verilerek başıboş bırakılmaması ya da develerin binmek için bağlanıp eyerlenmiş olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"At kullanılmaya hazır biçimde yakında tutulur, gözetilir ve değer verilerek başıboş bırakılmaz."},{"facet_id":"F002","role":"specialization","statement":"Develer binmek amacıyla bağlanmış, donatılmış veya üzerlerine eyer konmuş durumda olabilir."}],"identity_rationale":"Kaynak ifadesi atın yakında tutulup gözetilmesini, hazırlanmasını ve değer verilerek başıboş bırakılmamasını; develerin ise binmek için bağlanıp eyerlenmesini anlatır. Doğumun yaklaşması bu hayvan niteliğinin parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"yakında tutulan, gözetilen ve binmeye hazır at"},{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"binmek için bağlanmış veya eyerlenmiş develer"}],"lexicalization_note":"Anlam yalnız at ve deveyle kurulan özel ad öbeklerinde geçerlidir; çıplak köke genel bir binek anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hazırlık ortaklığının gözetilme ile güç niteliğini karıştırabileceği bu komşu en yararlı karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ayırıcı yönü hayvanın yakında tutulması ve gözetilmesidir; komşu dalın ayırıcı yönü fiziksel güç ve koşuya hazır oluşudur.","focus_only":"Odak dal atın yakında tutulup değer görmesini ve ayrıca binmek için bağlanan develeri kapsar.","gloss":"hazır tutulan at","neighbor_only":"Komşu dal atın güçlü, eksiksiz yapılı ve hemen koşmaya veya binilmeye hazır olmasını öne çıkarır.","neighbor_ref":"root_000978/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da kullanılmaya ve binilmeye hazır tutulan atı kapsar."}],"source_phrase_ar":"فرس مقربة وهي التي ترتاد وتقرب ولا تترك أن ترود (maqayis)؛ فرس مقربة وهي التي تدنى وتقرب ولا تترك أن ترود والمقربة المكرمة (jamhara)؛ المقرب من الخيل الذي يدنى ويكرم والأنثى مقربة (sihah)؛ الخيل المقربة التي تكون قريبا معدة والتي تدنى وتقرب وتكرم والإبل المقربة التي حزمت للركوب (tahdhib)","source_summary":"Tanıklıklar at için yakında tutma, hazırlama ve değer verme özelliklerini birleştirir; deve kullanımında ise binmek üzere bağlama ve eyerleme öne çıkar.","sources":["MQ","JA","SI","TA"],"what_is_ar":"يدخل فيه الفرس أو الخيل المقربة التي تدنى وتكرم أو تعد للركوب والإبل المقربة المحزومة أو ذات الرحل","what_is_not_ar":"ليس دنو الولادة ولا حظوة الأشخاص ولا تقريب عدو الفرس"},"support_links":[]},{"boundary":"Dal yalnız ata özgü belirli koşu biçimidir; hazırlanmış at adı veya genel hızlı koşu anlamı değildir.","branch_kind":"non_bare","branch_ref":"root_001212/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَقْرَبَة","morph_features":"STEM|POS:N|LEM:maqorabap|ROOT:qrb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:3:1","qac_word_ref":"90:15:3","surface_ar":"مَقْرَبَةٍ"}],"gloss":"atın dörtnaldan yavaş özel koşusu","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"At, hızlı dört nala koşudan daha yavaş belirli bir koşu biçimiyle ilerler."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Koşunun alt ve üst dereceleri bulunabilir; bir açıklama iki ön ayağın birlikte kaldırılıp indirilmesini ayırıcı hareket sayar."}}],"root_ar":"ق ر ب","root_id":"root_001212","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanı, hareket türünü ve hız sınırını birlikte belirten açıklayıcı karşılıktır.","boundary_detail":"Dal yalnız ata özgü belirli koşu biçimidir; hazırlanmış at adı veya genel hızlı koşu anlamı değildir.","branch_image_ar":"تقريب الفرس في العدو","concept_gloss":"atın dörtnaldan yavaş özel koşusu","contextual_glosses":[{"applicability":"Atın hızlı dört nala çıkmadan özel bir koşu biçimiyle ilerlediği anlatımlarda kullanılabilir.","error_profile":{"adds":"Genel Türkçede başka hayvanlara ve belirli olmayan her orta hıza uygulanabilir.","collision":"Ata özgü tarihsel koşu tekniğini sıradan hız betimlemesiyle karıştırabilir.","fit":"broadening","loses":null,"preserves":"Hareketin koşu oluşunu ve en hızlı koşudan daha yavaş gerçekleşmesini korur."},"facet_ids":["F001"],"text":"orta hızda koşmak","usage_role":"contextual"}],"definition":"Atın hızlı dört nala koşusundan daha yavaş olan, alt ve üst dereceleri bulunabilen özel bir koşu biçimidir. Bir tanıklıkta iki ön ayağın birlikte kaldırılıp birlikte indirilmesiyle açıklanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"At, hızlı dört nala koşudan daha yavaş belirli bir koşu biçimiyle ilerler."},{"facet_id":"F002","role":"source_variant","statement":"Koşunun alt ve üst dereceleri bulunabilir; bir açıklama iki ön ayağın birlikte kaldırılıp indirilmesini ayırıcı hareket sayar."}],"identity_rationale":"Kaynak ifadesi atın hızlı dört nala koşusundan daha yavaş olan belirli bir koşu biçiminde birleşir. Bazı tanıklıklar alt ve üst türleri, biri de iki ön ayağın birlikte kaldırılıp indirilmesini belirtir; bu ayrıntılar tek bir zorunlu mekanik özellik gibi genellenmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"atın dörtnaldan yavaş özel koşu biçimi"}],"lexicalization_note":"Anlam yalnız atın koşu biçimini belirten özel yapıda geçerlidir; çıplak köke genel koşma anlamı verilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; benzer hız alanında farklı bacak mekaniği ve hayvan kapsamı taşıyan bu komşu en açıklayıcı karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hız sınıfı ve ata özgü tarihsel adıyla belirlenir; komşu dal hayvan kapsamını genişletir ve ön bacakların uzatılmasını kurucu hareket yapar.","focus_only":"Odak dal yalnız ata özgüdür, hızlı dörtnaldan aşağı bir hız sınırı taşır ve derecelere ayrılabilir.","gloss":"özel at koşusu","neighbor_only":"Komşu dal at veya devenin ön bacaklarını uzatarak yaptığı hafif koşuyu anlatır.","neighbor_ref":"root_000901/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da binek hayvanının bacak hareketiyle belirlenen hafif veya orta hızlı koşusunu anlatır."}],"source_phrase_ar":"قرب الفرس تقريبا وهو دون الحضر وله تقريبان أدنى وأعلى (maqayis)؛ قرب الفرس تقريبا وهو تقريبان التقريب الأدنى والتقريب الأعلى وهو دون الحضر (jamhara)؛ التقريب ضرب من العدو وهو دون الحضر (sihah)؛ إذا رفع الفرس يديه معا ووضعهما معا فذلك التقريب (tahdhib)؛ تقريب الفرس سير يقرب من عدوه (mufradat)","source_summary":"Tanıklıklar atın hızlı dört nala koşusundan daha yavaş özel bir koşusunda birleşir; dereceler ve iki ön ayağın eş zamanlı hareketi ek açıklamalar olarak verilir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه تقريب الفرس وهو ضرب من العدو دون الحضر وله أدنى وأعلى أو رفع اليدين ووضعهما معا","what_is_not_ar":"ليس الخيل المقربة المعدة ولا قرب الولادة"},"support_links":[]},{"boundary":"Dal anatomik böğür ve yan bölgesiyle sınırlıdır; kılıç kabı, su kabı veya genel yakınlık değildir.","branch_kind":"bare","branch_ref":"root_001212/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَقْرَبَة","morph_features":"STEM|POS:N|LEM:maqorabap|ROOT:qrb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:3:1","qac_word_ref":"90:15:3","surface_ar":"مَقْرَبَةٍ"}],"gloss":"böğür, bedenin yan bölgesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Beden bölümü atın veya insanın bel ile karnın alt yanı arasındaki böğür ve yan tarafıdır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yürürken eli bu böğür bölgesine koymak, beden adından türeyen özel bir durum anlatımıdır."}}],"root_ar":"ق ر ب","root_id":"root_001212","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Anatomik alanı hem yaygın adıyla hem de açıklayıcı sınırıyla karşılar.","boundary_detail":"Dal anatomik böğür ve yan bölgesiyle sınırlıdır; kılıç kabı, su kabı veya genel yakınlık değildir.","branch_image_ar":"قُرْب الفرس والخاصرة","concept_gloss":"böğür, bedenin yan bölgesi","contextual_glosses":[{"applicability":"Anatomik konumun teknik ayrıntısının gerekli olmadığı cümlelerde böğür bölgesini belirtmek için kullanılır.","error_profile":{"adds":"Genel kullanımda beden dışındaki nesnelerin yanını ve bedenin daha geniş bir kısmını da kapsayabilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Bölgenin bedenin yanında bulunmasını korur."},"facet_ids":["F001"],"text":"yan taraf","usage_role":"contextual"}],"definition":"Atın veya insanın yan tarafında, bel ile karnın alt yanı arasında bulunan böğür ve yan bölgesidir. Elini bu bölgeye koyarak yürüme de aynı beden adından türeyen bir kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Beden bölümü atın veya insanın bel ile karnın alt yanı arasındaki böğür ve yan tarafıdır."},{"facet_id":"F002","role":"associated_use","statement":"Yürürken eli bu böğür bölgesine koymak, beden adından türeyen özel bir durum anlatımıdır."}],"identity_rationale":"Kaynak ifadesi atın veya insanın yan tarafındaki böğür ve bel bölgesini, özellikle kalça önü ile karnın alt yanı arasındaki alanı adlandırır. Elini bu bölgeye koyma eylemi, beden bölümünün ikincil kullanımını oluşturur.","lexical_glosses":[{"lexical_unit_id":"lu_041","rendering_kind":"ordinary","target_gloss":"böğür, bel ile karnın alt yanı arasındaki bölge"},{"lexical_unit_id":"lu_042","rendering_kind":"ordinary","target_gloss":"böğürler, bedenin yanları"},{"lexical_unit_id":"lu_043","rendering_kind":"ordinary","target_gloss":"yürürken elini böğrüne koymuş"}],"lexicalization_note":"Çıplak dal bedenin böğür ve yan bölgesini tanımlar; eşsesli kap ve yakınlık anlamları içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı anatomik bölgeyi doğrudan adlandıran bu komşu dışında yayımlanmaya değer eşdeğer bir sınır bulunmadı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek anatomik sınırlar arasında anlamlı bir fark görünmez; odak daldaki elini böğre koyma kullanımı çekirdeğin bağımlı türevidir.","focus_only":null,"gloss":"böğür","neighbor_only":null,"neighbor_ref":"root_000040/B007","relation_type":"synonym","shared_zone":"Her iki dal da bedenin yanındaki böğür bölgesini adlandırır."}],"source_phrase_ar":"الخاصرة هي القرب سميت لقربها من الجنب (maqayis)؛ قرب الفرس كشحه وهو الخصر والجمع أقراب (jamhara)؛ القرب من الشاكلة إلى مراق البطن والجمع الأقراب (sihah)؛ القرب من لدن الشاكلة إلى مراق البطن ومتقربا أي واضعا يده على قربه (tahdhib)؛ فرس لاحق الأقراب أي الخواصر (mufradat)","source_summary":"Tanıklıklar at veya insan bedenindeki böğür ve yan bölgesinde birleşir; çoğul biçimi yanları, türemiş kullanım ise yürürken eli bu bölgeye koymayı anlatır.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه قرب الفرس أو الإنسان بمعنى الكشح والخاصرة وما بين الشاكلة ومراق البطن ووضع اليد على القرب","what_is_not_ar":"ليس قراب السيف ولا القربة الوعاء ولا القرب المكاني"},"support_links":[]},{"boundary":"Dal kesin miktarı değil, doluluk, sayı, miktar ve zamanda yaklaşık değeri anlatır; kalite, fiyat ve satış kullanımları kendi sözlüksel yapısında tutulmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001212/B016","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَقْرَبَة","morph_features":"STEM|POS:N|LEM:maqorabap|ROOT:qrb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:3:1","qac_word_ref":"90:15:3","surface_ar":"مَقْرَبَةٍ"}],"gloss":"bir ölçü veya sınıra yaklaşık olma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir ölçü, sayı veya miktar belirli bir sınıra tam ulaşmadan ona yaklaşır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kap içindeki madde, kabı doldurmaya yaklaşmış fakat tam doldurmamıştır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yaklaşık değer ilişkisi akşam veya gece gibi bir zamana uygulanır; orta kalite ya da düşük fiyat yapıya bağlı bir uzmanlaşma olarak ayrıca verilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Satışta pazarlık etme, kaynakta ayrı bir işlem bağlamı olarak verilen yapıya bağlı kullanımdır."}}],"root_ar":"ق ر ب","root_id":"root_001212","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın sayı, doluluk, zaman, kalite, fiyat ve pazarlık alanlarındaki ortak yaklaşma ilişkisini karşılar.","boundary_detail":"Dal kesin miktarı değil, doluluk, sayı, miktar ve zamanda yaklaşık değeri anlatır; kalite, fiyat ve satış kullanımları kendi sözlüksel yapısında tutulmalıdır.","branch_image_ar":"القراب والمقاربة في المقدار","concept_gloss":"bir ölçü veya sınıra yaklaşık olma","contextual_glosses":[{"applicability":"Bir kap içindeki maddenin doluluk sınırına çok yaklaştığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sayı, zaman, kalite, fiyat ve satış alanlarındaki diğer yaklaşık olma kullanımlarını dışarıda bırakır.","preserves":"Doluluk sınırına yaklaşmayı ve tam dolu olmamayı korur."},"facet_ids":["F002"],"text":"neredeyse dolu","usage_role":"contextual"},{"applicability":"Sayı, miktar veya zamanın belirli bir değere yakın olduğu genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Orta kalite, düşük fiyat ve satışta tarafların birbirine yaklaşması gibi yapıların özel içeriğini dışarıda bırakır.","preserves":"Kesin değere ulaşmadan ona yakın olma ilişkisini korur."},"facet_ids":["F001","F003"],"text":"yaklaşık","usage_role":"general"}],"definition":"Bir miktar, sayı, zaman veya doluluğun belirli bir değere yaklaşık olmasıdır. Bu çekirdek neredeyse dolu kapta, yüze yakın sayıda ve akşama yakın vakitte görünür; orta kalite veya ucuz mal ile satışta pazarlık etme ise yapıya bağlı ayrı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir ölçü, sayı veya miktar belirli bir sınıra tam ulaşmadan ona yaklaşır."},{"facet_id":"F002","role":"specialization","statement":"Kap içindeki madde, kabı doldurmaya yaklaşmış fakat tam doldurmamıştır."},{"facet_id":"F003","role":"extension","statement":"Yaklaşık değer ilişkisi akşam veya gece gibi bir zamana uygulanır; orta kalite ya da düşük fiyat yapıya bağlı bir uzmanlaşma olarak ayrıca verilir."},{"facet_id":"F004","role":"associated_use","statement":"Satışta pazarlık etme, kaynakta ayrı bir işlem bağlamı olarak verilen yapıya bağlı kullanımdır."}],"identity_rationale":"Kaynak ifadesi doluluk, sayı, miktar ve zaman bakımından belirli bir değere yakın olmayı ortaklaştırır. Orta kalite veya ucuz mal ile satışta pazarlık etme ise bu çekirdeğe zorla indirgenmeyen yapıya bağlı kullanımlardır; bunlar tek bir ölçü adı gibi birleştirilemez.","lexical_glosses":[{"lexical_unit_id":"lu_044","rendering_kind":"ordinary","target_gloss":"bir şeyin doluluğuna, sayısına veya miktarına yakın değer"},{"lexical_unit_id":"lu_045","rendering_kind":"ordinary","target_gloss":"neredeyse dolu kap"},{"lexical_unit_id":"lu_046","rendering_kind":"ordinary","target_gloss":"ses değişmesiyle neredeyse dolu kap"},{"lexical_unit_id":"lu_047","rendering_kind":"ordinary","target_gloss":"orta kalitede veya ucuz kumaş"},{"lexical_unit_id":"lu_048","rendering_kind":"ordinary","target_gloss":"satışta önerileri birbirine yaklaştırmak"},{"lexical_unit_id":"lu_049","rendering_kind":"ordinary","target_gloss":"akşama veya geceye yakın vakit"}],"lexicalization_note":"Yaklaşık miktar çekirdeği çıplak ve yapıya bağlı kullanımlarda ayrıştırılır; doluluk, sayı, zaman, kalite ve satış alanları birbirine karıştırılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yaklaşık miktar ile kesin sayısal toplam arasındaki sınırı bu komşu en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda değer sınıra yaklaşık kalır ve ona tam ulaşması gerekmez; komşu dalda bildirilen miktar sayının doğrudan değeri veya ulaştığı toplamdır.","focus_only":"Odak dal sayının yanında doluluk, zaman, kalite, fiyat ve satışta belirli bir sınıra yaklaşmayı kapsar.","gloss":"bir sayıya yakın miktar","neighbor_only":"Komşu dal bir sayının ulaştığı miktarı veya toplamı daha doğrudan ve kesin biçimde bildirir.","neighbor_ref":"root_001560/B010","relation_type":"near_synonym","shared_zone":"Her iki dal da belirli bir sayıyla ilişkili miktarı anlatabilir."}],"source_phrase_ar":"ثوب مقارب إذا لم يكن جيدا وهذا على معنى أنه مقارب في ثمنه (maqayis)؛ الدراهم قراب مائة وإناء قربان إذا قارب أن يمتلىء وقراب كل شيء ما قارب الامتلاء (jamhara)؛ شيء مقارب وسط بين الجيد والردئ أو رخيص وقدح قربان إذا قارب أن يمتلئ وقاربته في البيع مقاربة (sihah)؛ القراب مقاربة الشيء معه ألف درهم أو قرابه وأتيته قراب العشي أو قراب الليل وقدح قربان ماء ولو أن في قراب هذا ذهبا (tahdhib)؛ القراب المقاربة وقدح قربان قريب من الملء (mufradat)؛ إناء كربان كرب أن يمتلىء (maqayis-ibdal)","source_summary":"Tanıklıklar kesin sınıra varmadan ona yaklaşma ilişkisini sayı, doluluk, zaman, nitelik, fiyat ve satış alanlarında gösterir; kap doluluğu ve yaklaşık miktar en belirgin örneklerdir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه قراب الشيء وما يقارب ملأه أو عدده أو زمنه والقدح القربان والإناء الكربان والثوب أو الشيء المقارب بين الجودة والرداءة أو في الثمن","what_is_not_ar":"ليس قراب السيف ولا القرب المكاني ولا قربان النسيكة"},"support_links":[]},{"boundary":"İnsan çocuğu için baba kaybı ve ergenlik sınırı, hayvan yavrusu için anne kaybı esastır; genel yalnızlık bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001692/B001","candidate_links":[{"candidate_id":"cand_196524c06262313fb4fd","lane":"micro"},{"candidate_id":"cand_e49c796183af29c5e8b0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:1:1","qac_word_ref":"90:15:1","surface_ar":"يَتِيمًا"}],"gloss":"babasını yitirmiş çocuk veya annesini yitirmiş hayvan yavrusu olma","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanlarda durum, bir çocuğun ergenliğe ulaşmadan babasını yitirmesiyle oluşur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsan dışındaki hayvanlarda karşılık gelen durum, yavrunun annesini yitirmesidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Türemiş eylemler, bir çocuğu babasız bırakmayı veya çocukları topluca bu duruma düşürmeyi anlatır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bazı türemiş kadın adları, çocukları babasız kalmış olan anneyi niteler."}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan ve hayvan için farklı ebeveyn koşullarını birlikte belirtmek gereken genel açıklamada kullanılır.","boundary_detail":"İnsan çocuğu için baba kaybı ve ergenlik sınırı, hayvan yavrusu için anne kaybı esastır; genel yalnızlık bu dala girmez.","branch_image_ar":"انقطاع الولد عن كافله","concept_gloss":"babasını yitirmiş çocuk veya annesini yitirmiş hayvan yavrusu olma","contextual_glosses":[{"applicability":"Ergenliğe ulaşmadan babası ölen bir insan çocuğundan söz edilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan çocuğunu ve belirleyici baba kaybını açık biçimde korur."},"facet_ids":["F001"],"text":"babasını yitirmiş çocuk","usage_role":"contextual"},{"applicability":"İnsan dışındaki bir hayvanın annesini yitirmiş yavrusundan söz edilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvan yavrusunu ve belirleyici anne kaybını açık biçimde korur."},"facet_ids":["F002"],"text":"annesini yitirmiş hayvan yavrusu","usage_role":"contextual"}],"definition":"İnsanlarda ergenliğe ulaşmadan babasını yitirmiş çocuk olma, öteki hayvanlarda ise annesini yitirmiş yavru olma durumudur. Bir çocuğu bu duruma düşürme ve çocukları babasız kalan kadını niteleme gibi türev kullanımlar bu çekirdeğe bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanlarda durum, bir çocuğun ergenliğe ulaşmadan babasını yitirmesiyle oluşur."},{"facet_id":"F002","role":"specialization","statement":"İnsan dışındaki hayvanlarda karşılık gelen durum, yavrunun annesini yitirmesidir."},{"facet_id":"F003","role":"extension","statement":"Türemiş eylemler, bir çocuğu babasız bırakmayı veya çocukları topluca bu duruma düşürmeyi anlatır."},{"facet_id":"F004","role":"associated_use","statement":"Bazı türemiş kadın adları, çocukları babasız kalmış olan anneyi niteler."}],"identity_rationale":"Kaynak ifadesi genel olarak bakımı üstlenen kişiden ayrılmayı değil, insan çocuğunda ergenlikten önce babanın, öteki hayvanlarda ise annenin ölümünü belirleyici sayar. Bu nedenle dal, bu iki katılımcı ayrımı açıkça korunarak tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"insanda babasız, hayvanda annesiz kalma"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"babasını yitirmiş çocuk veya annesini yitirmiş hayvan yavrusu"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"çocuk babasını yitirip babasız kaldı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"Tanrı onu babasız bıraktı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"çocukları babasız bıraktı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"babasını yitirmiş çocuklar"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"babasını yitirmiş çocuklar"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"çocukları babasız kalmış kadın"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"çocukları babasız kalmış kadın"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"onları babasız bıraktı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"çocukken kendisini yetiştiren kişiye nispetle, büyüdüğünde de babasını yitirmiş çocuk diye anılan kişi"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"babasını yitirmiş çocuklar topluluğu"}],"lexicalization_note":"Tanım, yalın durum ve kişi adlandırmalarını temel alır; çocukları babasız kalan kadın ile büyüdükten sonra da sürdürülen adlandırma yalnız kendi kalıpları içinde tutulur.","neighbor_coverage_note":"Sunulan bütün komşu adaylar değerlendirildi; ebeveyn ölümü, bırakılma, bakım bağı ve tek kalma arasındaki sınırı en açık gösteren üç karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ölümden doğan ve türe göre baba ya da anne üzerinden tanımlanan statüdür; komşu dal ise ölüm gerektirmeyen bırakılma ve bulunma olayını anlatır.","focus_only":"Odak dalda ebeveynin ölümü, insan ve hayvan için ayrı ebeveyn rolleriyle belirleyicidir.","gloss":"ebeveynini yitirmiş yavru ile bırakılmış çocuk","neighbor_only":"Komşu dalda çocuk annesi tarafından bırakılır ve başka biri tarafından bulunur.","neighbor_ref":"root_001466/B007","relation_type":"near_neighbor","shared_zone":"Her ikisi de bir çocuğun veya yavrunun doğal ebeveyn bakımından yoksun kalabildiği durumları anlatır."},{"boundary_match":"field_only","distinction":"Bakıma muhtaçlık odak dalın tanımı değildir ve her bakmakla yükümlü olunan kişi ebeveynini yitirmiş değildir.","focus_only":"Odak dal, insan çocuğunda baba ve hayvan yavrusunda anne ölümüyle sınırlı bir durumdur.","gloss":"ebeveyn kaybı ile bakıma muhtaç olma","neighbor_only":"Komşu dal bakmakla yükümlü olunanları, yük sayılan kişileri ve çocuğu olmayanları da kapsar.","neighbor_ref":"root_001315/B002","relation_type":"same_field","shared_zone":"İki dal da başkasının bakımına veya desteğine ihtiyaç duyan kişilerin alanına değebilir."},{"boundary_match":"partial","distinction":"Odak dalın koşulları ebeveyn türü ve insanlarda ergenlik sınırıyla belirlenir; komşu dal bu koşulları taşımaz ve nadir nesnelere de uygulanır.","focus_only":"Odak dal canlılarda belirli bir ebeveynin ölümüne bağlı statüyü bildirir.","gloss":"ebeveyn kaybı ile tek kalma","neighbor_only":"Komşu dal canlı ya da cansız herhangi bir şeyin tek kalmasını veya benzerinin zor bulunmasını bildirir.","neighbor_ref":"root_001692/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da önceki bir bağdan veya eşlikten yoksun kalma düşüncesi bulunabilir."}],"source_phrase_ar":"اليتم في الناس من قبل الأب وفي سائر الحيوان من جهة الأم (maqayis)؛ يتم الصبي إذا صار يتيما وأيتمه الله (jamhara)؛ أيتمت المرأة فهي موتم (jamhara;sihah)؛ يتمهم الله تيتيما (sihah)؛ اليتيم الذي مات أبوه حتى يبلغ (tahdhib)؛ انقطاع الصبي عن أبيه قبل بلوغه وفي سائر الحيوانات من قبل أمه (mufradat)","source_summary":"Kanıt bütünü, insan çocuğunda baba kaybını, hayvan yavrusunda anne kaybını ve bu durumla ilgili türemiş biçimleri verir. Ergenlik sınırı bazı aktarımlarda açıkça belirtilir; ettirgen ve topluluk bildiren biçimler ayrı tanıklamalar olarak bu çekirdeğe bağlanır.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الصبي الذي مات أبوه قبل بلوغه، والبهيمة التي ماتت أمها، وجعل الأولاد أيتاما","what_is_not_ar":"ليس مجرد الانفراد في الأشياء النفيسة ولا الإبطاء في السير ولا الغفلة والتقصير"},"support_links":["sup_445e7b651dd2ef824320","sup_d222801d97d8d4b15059"]},{"boundary":"Dal, ebeveyn kaybını değil tekliği veya benzer azlığını anlatır; değerli nesne ve şiir örnekleri çekirdeğin kendisi değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001692/B002","candidate_links":[{"candidate_id":"cand_9bbf162904d99c2dcac2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:1:1","qac_word_ref":"90:15:1","surface_ar":"يَتِيمًا"}],"gloss":"tek kalmış ya da benzeri zor bulunan şey","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Canlı ya da cansız bir varlık, başka bir eşlikçi olmadan tek başına bulunduğunda bu nitelemeyi alabilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Niteleme, benzeri veya dengi zor bulunan seçkin bir varlığa da uygulanabilir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tek başına duran şiir dizesi, eşi zor bulunan inci ve ayrı kumluk kaynaklarda örneklenir."}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tek başına bulunma ile eşine az rastlanma kapsamlarının ikisini de taşıyan genel niteleme için kullanılır.","boundary_detail":"Dal, ebeveyn kaybını değil tekliği veya benzer azlığını anlatır; değerli nesne ve şiir örnekleri çekirdeğin kendisi değildir.","branch_image_ar":"انفراد الشيء وانقطاع نظيره","concept_gloss":"tek kalmış ya da benzeri zor bulunan şey","contextual_glosses":[{"applicability":"Varlığın eşlikçisiz veya çevresindekilerden ayrı bulunmasının öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Varlığın başka bir eşlikçi olmadan tek kalması özelliğini korur."},"facet_ids":["F001"],"text":"tek başına kalmış","usage_role":"contextual"},{"applicability":"Bir nesnenin veya söz ürününün benzerinin az bulunması vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Benzer azlığını ve bundan doğan eşsizlik niteliğini korur."},"facet_ids":["F002"],"text":"eşi zor bulunan","usage_role":"contextual"}],"definition":"Bir varlığın tek başına kalması veya benzerinin zor bulunmasıdır; şiir dizesi, inci ve tek başına duran kumluk bu niteliğin özel örnekleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Canlı ya da cansız bir varlık, başka bir eşlikçi olmadan tek başına bulunduğunda bu nitelemeyi alabilir."},{"facet_id":"F002","role":"extension","statement":"Niteleme, benzeri veya dengi zor bulunan seçkin bir varlığa da uygulanabilir."},{"facet_id":"F003","role":"example","statement":"Tek başına duran şiir dizesi, eşi zor bulunan inci ve ayrı kumluk kaynaklarda örneklenir."}],"identity_rationale":"Kaynak ifadesi, tek başına kalan şeyi ve benzeri zor bulunan şeyi aynı dalda açıkça toplar; şiir dizesi, inci ve tek kumluk bu çekirdeğin örnekleridir. Geçici çerçeve bu kapsamı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"tek başına veya eşi zor bulunan"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"tek başına duran veya benzeri olmayan şiir dizesi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"tek ve eşi zor bulunan inci"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"tek başına duran kumluk veya dişil varlık"}],"lexicalization_note":"Yalın niteleme tekliği veya benzer azlığını bildirir; şiir dizesi ve inci okumaları yalnız tanıklanmış ad öbeklerinin özel uygulamalarıdır.","neighbor_coverage_note":"Bütün adaylar incelendi; genel teklik, nadirlik, belirli bir nitelikte rakipsizlik ve ebeveyn kaybı ile en güçlü sınırları kuran dört aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal tek kalmayı benzer azlığına kadar genişletirken komşu dal sayısal birlik ve tekleştirme işlemlerine de uzanır; bu yüzden kapsamları bütünüyle örtüşmez.","focus_only":"Odak dal, benzeri zor bulunan nesne ile şiir dizesi ve inci gibi kalıplaşmış uygulamaları özellikle kapsar.","gloss":"tek kalmış ve bir olan","neighbor_only":"Komşu dal bir olma, teklik, birer birer gelme ve tek başına gönderme gibi daha geniş işlemleri de kapsar.","neighbor_ref":"root_001141/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir varlığın tek başına ve eşlikçisiz bulunmasını doğrudan anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği tek kalmadır; komşu dalın çekirdeği ise kıtlık ve erişim güçlüğüdür, dolayısıyla yalnızlığın kendisini gerektirmez.","focus_only":"Odak dalda tek başına bulunma yeterlidir ve erişim güçlüğü gerekli değildir.","gloss":"eşi zor bulunan ile nadir ve güç erişilen","neighbor_only":"Komşu dal az bulunmanın yanında bir şeye erişmenin veya benzerini bulmanın güçlüğünü bildirir.","neighbor_ref":"root_001008/B003","relation_type":"near_neighbor","shared_zone":"Benzeri az bulunan bir nesne iki dalın kapsamına da girebilir."},{"boundary_match":"partial","distinction":"Komşu dal belirli insani niteliklerle sınırlı bir üstünlük veya uçluk bildirirken odak dal tek başına bulunmayı da kapsayan daha genel bir nesne niteliğidir.","focus_only":"Odak dal her tür canlı veya cansız varlığın tekliğine ve benzer azlığına uygulanabilir.","gloss":"genel eşsizlik ile bir nitelikte rakipsizlik","neighbor_only":"Komşu dal cömertlik, erdem, iyilik ya da kötülük gibi belirli değerlendirme alanlarında dengi olmayan kişiyi niteler.","neighbor_ref":"root_001240/B018","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir varlığın belli bakımdan denginin bulunmamasını anlatabilir."},{"boundary_match":"partial","distinction":"Bu çağrışım iki dalı özdeş kılmaz; odak dal genel teklik ve eşsizlik, komşu dal ise canlılara özgü ve koşulları belirli bir ebeveyn kaybı statüsüdür.","focus_only":"Odak dal ebeveyn ölümü olmadan da tek kalan veya benzeri az bulunan her şeye uygulanabilir.","gloss":"tek kalma ile ebeveynini yitirme","neighbor_only":"Komşu dal insan çocuğunda baba, hayvan yavrusunda anne ölümünü ve insan için ergenlik sınırını gerektirir.","neighbor_ref":"root_001692/B001","relation_type":"near_neighbor","shared_zone":"Ebeveynini yitiren çocuk veya yavru, tek kalma düşüncesiyle ilişkilendirilebilir."}],"source_phrase_ar":"لكل منفرد يتيم وبيت من الشعر يتيم (maqayis)؛ اليتيم الفرد (jamhara)؛ كل شيء مفرد يعز نظيره فهو يتيم ودرة يتيمة (sihah)؛ الرملة المنفردة وكل منفرد ومنفردة يتيم ويتيمة (tahdhib)؛ كل منفرد يتيم ودرة يتيمة وبيت يتيم (mufradat)","source_summary":"Kaynaklar tek kalma anlamında birleşir ve bir şeyin benzerinin az bulunmasını buna bağlı bir kapsam olarak verir. Şiir dizesi, inci ve kumluk bu ortak anlamı görünür kılan örneklerdir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه كل منفرد أو منفردة، وما عز نظيره كالدرة اليتيمة وبيت الشعر اليتيم والرملة المنفردة","what_is_not_ar":"ليس خصوص موت الأب عن الصبي ولا موت الأم عن البهيمة ولا الإبطاء في السير"},"support_links":["sup_f485dfbf32fa0aced728"]},{"boundary":"Buradaki anlam zihinsel dikkatsizlik ile görevde eksik bırakmayı birlikte kapsar; salt yavaşlama ayrı daldadır.","branch_kind":"mixed_non_bare","branch_ref":"root_001692/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:1:1","qac_word_ref":"90:15:1","surface_ar":"يَتِيمًا"}],"gloss":"dalgınlık ve gerekeni eksik yapma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Anlam, dikkat göstermeme ile bir işi veya yükümlülüğü gerektiği kadar yerine getirmemeyi birlikte kapsar."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yol alış hakkında kullanılan olumsuz kalıp, gidişte dalgınlık veya eksik davranış bulunmadığını bildirir."}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dikkat eksikliği ile görevde yetersiz kalmanın birlikte anlatıldığı genel bağlamlarda kullanılır.","boundary_detail":"Buradaki anlam zihinsel dikkatsizlik ile görevde eksik bırakmayı birlikte kapsar; salt yavaşlama ayrı daldadır.","branch_image_ar":"غفلة وتقصير","concept_gloss":"dalgınlık ve gerekeni eksik yapma","contextual_glosses":[{"applicability":"Bir kişinin yol alışında dikkatsizlik veya kusurlu davranış bulunmadığını söyleyen tanıklanmış kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Olumsuzluğu, yol alış bağlamını ve iki kusurun yokluğunu korur."},"facet_ids":["F002"],"text":"gidişinde dalgınlık veya eksiklik yok","usage_role":"contextual"}],"definition":"Bir şeyi yeterince gözetmeyerek dalgın davranma ve yapılması gerekeni eksik bırakmadır; yol alışa ilişkin kalıpta bu özelliklerin bulunmadığı söylenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Anlam, dikkat göstermeme ile bir işi veya yükümlülüğü gerektiği kadar yerine getirmemeyi birlikte kapsar."},{"facet_id":"F002","role":"associated_use","statement":"Yol alış hakkında kullanılan olumsuz kalıp, gidişte dalgınlık veya eksik davranış bulunmadığını bildirir."}],"identity_rationale":"Kaynak ifadesi dalı açıkça dalgınlık ve gerekeni eksik yapma olarak tanımlar; yol alış kalıbı da bu iki niteliğin bulunmadığını söyleyen bir uygulamadır. Geçici çerçeve kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"dalgınlık ve gerekeni eksik yapma"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"gidişinde dalgınlık veya eksik davranış yok"}],"lexicalization_note":"Yalın biçim dalgınlık ve eksik davranmayı anlatır; yol alışa ilişkin olumsuz okuma yalnız tanıklanmış cümle kalıbının kapsamındadır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dikkatsizlik, savsaklama, mazeretli eksiklik ve yavaşlama arasındaki ayrımları en iyi gösteren dört aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dikkatsizlik ile kusuru birleştirir; komşu dal ise bilinçli oyalanma, tembellik ve güçsüz değerlendirme gibi nedenleri de kapsar.","focus_only":"Odak dal dalgınlığı ve eksik yapmayı yalın bir anlam olarak, ayrıca yol alış kalıbındaki olumsuz uygulamayla verir.","gloss":"dalgınlık ve eksik yapma ile savsaklama","neighbor_only":"Komşu dal işi savsaklama, oyalanma, tembellikten yatma ve görüş zayıflığı gibi daha geniş davranışları kapsar.","neighbor_ref":"root_000902/B003","relation_type":"near_synonym","shared_zone":"İki dal da kişinin üstlendiği işi yeterince yerine getirmemesini anlatabilir."},{"boundary_match":"partial","distinction":"Komşu dal dikkat dışına çıkma olayında yoğunlaşır; odak dal ise bunun yanında görev veya davranıştaki yetersizliği de kurucu sayar.","focus_only":"Odak dal dikkat eksikliğinin yanında yapılması gerekeni eksik bırakmayı da doğrudan içerir.","gloss":"dalgınlık ve eksik yapma ile gözden kaçırma","neighbor_only":"Komşu dal bir şeyi uyanıklık ve koruma azlığından dolayı unutma veya gözden kaçırma yönünü öne çıkarır.","neighbor_ref":"root_001097/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak alanı, yeterli dikkat göstermemektir."},{"boundary_match":"partial","distinction":"Odak dal dikkatsizlik ve eksikliktir; komşu dal ise eksikliği mazeret gösterme tavrıyla birlikte tanımlar.","focus_only":"Odak dalda sahte mazeret gösterme veya kendini haklı çıkarma koşulu yoktur.","gloss":"eksik yapma ile mazeretli savsaklama","neighbor_only":"Komşu dal eksik davranışa gerçek olmayan bir mazeret gösterme veya özür görüntüsü verme boyutunu ekler.","neighbor_ref":"root_000995/B005","relation_type":"near_neighbor","shared_zone":"İki dal da bir işin gerektiği gibi yerine getirilmemesini kapsayabilir."},{"boundary_match":"partial","distinction":"Ortak kalıp anlam özdeşliği yaratmaz; bu dal davranış kusurunu, komşu dal ise hızın düşmesini veya gecikmeyi anlatır.","focus_only":"Odak dal dikkatsizlik ve gerekeni eksik yapma kusurlarını bildirir.","gloss":"dikkatsizlik ile yavaşlama","neighbor_only":"Komşu dal hareketin veya yol alışın ağırlaşmasını ve iyiliğin gecikmesini bildirir.","neighbor_ref":"root_001692/B004","relation_type":"near_neighbor","shared_zone":"Aynı yol alış ifadesi kaynaklarda iki ayrı yorumun bağlamı olabilir."}],"source_phrase_ar":"اليتم الغفلة والتقصير وما في سيره يتم أي ما فيه غفلة ولا تقصير (jamhara)؛ أصل اليتم الغفلة وبه يسمى اليتيم لأنه يتغافل عن بره (tahdhib)","source_summary":"Kaynakların ortak alanı dalgınlıktır. Eksik davranma ve yol alışta dalgınlık ya da eksiklik bulunmadığını bildiren kalıp, bunları açıkça birlikte veren aktarımın ek ayrıntılarıdır.","sources":["JA","TA"],"what_is_ar":"يدخل فيه اليتم بمعنى الغفلة والتقصير، وما نفي عن السير في قولهم ما في سيره يتم عند من فسره بذلك","what_is_not_ar":"ليس اليتم بمعنى اليتيم الذي مات أبوه ولا الانفراد النفيس ولا الإبطاء الخالص"},"support_links":[]},{"boundary":"Çekirdek hareketin ağırlaşması veya gecikmesidir; çocuğa iyiliğin geç ulaşması yalnız açıklayıcı bir bağlantıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001692/B004","candidate_links":[{"candidate_id":"cand_ffa8b32ec312649e6326","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:1:1","qac_word_ref":"90:15:1","surface_ar":"يَتِيمًا"}],"gloss":"yavaşlama veya gecikme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, hareketin olağan hızından daha ağır ilerlemesi veya gecikmesidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tanıklanmış yol alış kalıbında, bir kimsenin gidişinde yavaşlama bulunduğu anlatılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Babasını yitirmiş çocuğa iyiliğin geç ulaşması, ebeveyn kaybı adlandırmasıyla kurulan açıklayıcı bağ olarak verilir."}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hareketin ya da ilerleyişin olağan hızından daha ağır sürmesini anlatan genel bağlamlarda kullanılır.","boundary_detail":"Çekirdek hareketin ağırlaşması veya gecikmesidir; çocuğa iyiliğin geç ulaşması yalnız açıklayıcı bir bağlantıdır.","branch_image_ar":"إبطاء السير والبر","concept_gloss":"yavaşlama veya gecikme","contextual_glosses":[{"applicability":"Tanıklanmış yol alış kalıbında kişinin ilerleyişinin ağır olduğunu belirtmek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yol alış bağlamını ve hareket hızının düşmesini açıkça korur."},"facet_ids":["F002"],"text":"gidişinde yavaşlama var","usage_role":"contextual"},{"applicability":"Babasını yitirmiş çocuğa gösterilen iyiliğin gecikmesini adlandırma gerekçesi olarak açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İyilik alanını, gecikmeyi ve açıklayıcı bağlantının yönünü korur."},"facet_ids":["F003"],"text":"iyiliğin geç ulaşması","usage_role":"explanatory"}],"definition":"Bir şeyin yavaşlaması veya gecikmesidir. Yol alışın ağırlaşması bunun özel uygulamasıdır; babasını yitirmiş çocuğa iyiliğin geç ulaşması ise açıklayıcı bir bağlantıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, hareketin olağan hızından daha ağır ilerlemesi veya gecikmesidir."},{"facet_id":"F002","role":"specialization","statement":"Tanıklanmış yol alış kalıbında, bir kimsenin gidişinde yavaşlama bulunduğu anlatılır."},{"facet_id":"F003","role":"associated_use","statement":"Babasını yitirmiş çocuğa iyiliğin geç ulaşması, ebeveyn kaybı adlandırmasıyla kurulan açıklayıcı bağ olarak verilir."}],"identity_rationale":"Kaynak ifadesi yavaşlama anlamını ve yol alış uygulamasını doğrudan destekler; babasını yitirmiş çocuğa iyiliğin geç ulaşması ise adlandırmayı açıklayan bağımlı bir gerekçedir. Bu açıklama çekirdekle eş düzeye çıkarılmadan dal korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"gidişinde yavaşlama var"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yavaşlama ve gecikme"}],"lexicalization_note":"Yalın biçim yavaşlama anlamını taşır; yol alış okuması kendi kalıbında tutulur ve iyiliğin geç ulaşması bağımsız bir yalın anlam sayılmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; çaba eksikliği, güçten düşme, isteksiz ağırlaşma ve dikkatsizlikten ayrımı en belirgin dört komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hız ve zaman bakımından ağırlaşmayı temel alır; komşu dal ise görevde yetersiz çaba gösterme anlamına da uzanır.","focus_only":"Odak dal yalın yavaşlamayı ve babasını yitirmiş çocuğa iyiliğin geç ulaşmasına ilişkin açıklamayı içerir.","gloss":"yavaşlama ile çabada geri kalma","neighbor_only":"Komşu dal bir işte, özellikle öğüt vermede, gereken çabayı göstermeyip geri kalmayı da içerir.","neighbor_ref":"root_000048/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir işin veya ilerleyişin beklenenden geç gerçekleşmesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal gözlenen hız düşüşüdür; komşu dal ise hareketin altında yatan gevşeme ve güç azalması durumunu öne çıkarır.","focus_only":"Odak dal yavaşlamayı nedenine bakmadan bildirir ve iyiliğin gecikmesine ilişkin açıklayıcı bir bağlantı taşır.","gloss":"yavaşlama ile güçten düşme","neighbor_only":"Komşu dal işte veya yol alışta güç ve canlılığın azalmasından doğan gevşemeyi anlatır.","neighbor_ref":"root_001621/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal yol alışın veya işin daha ağır sürmesine uygulanabilir."},{"boundary_match":"partial","distinction":"Odak dal sonucun hız boyutunu adlandırır; komşu dal bedensel veya ruhsal gevşekliği kurucu unsur yapar.","focus_only":"Odak dal gecikmeyi ve ilerleyişin ağırlaşmasını bedensel bir neden gerektirmeden anlatır.","gloss":"gecikme ile gevşek ve isteksiz davranma","neighbor_only":"Komşu dal tembellik, ateşli hastalık veya beden gevşekliğiyle bağlantılı isteksizlik ve ağır davranmayı kapsar.","neighbor_ref":"root_000392/B001","relation_type":"near_neighbor","shared_zone":"Ağır yürüyen veya işini yavaş yapan kişi iki alanın görünür sonucunu paylaşabilir."},{"boundary_match":"partial","distinction":"Bu dal zamansal ve devinimsel ağırlaşmadır; komşu dal ise davranış ve dikkat kusurudur.","focus_only":"Odak dal hareket hızının düşmesini veya bir şeyin geç ulaşmasını anlatır.","gloss":"yavaşlama ile dikkatsizlik","neighbor_only":"Komşu dal dikkat göstermemeyi ve yapılması gerekeni eksik bırakmayı anlatır.","neighbor_ref":"root_001692/B003","relation_type":"near_neighbor","shared_zone":"Yol alışa ilişkin aynı kalıp iki anlam için kaynaklarda yorumlanmıştır."}],"source_phrase_ar":"في سيره يتم أي إبطاء (sihah)؛ اليتم الإبطاء ومنه أخذ اليتيم لأن البر يبطىء عنه (tahdhib)","source_summary":"Kaynakların ortak alanı genel yavaşlama ve gecikmedir. Yol alıştaki ağırlaşma bir aktarımdaki özel uygulama, iyiliğin babasını yitirmiş çocuğa geç ulaşması ise diğer aktarımdaki adlandırma açıklamasıdır.","sources":["SI","TA"],"what_is_ar":"يدخل فيه اليتم بمعنى الإبطاء، وخاصة قولهم في سيره يتم، وتعليل تسمية اليتيم بأن البر يبطئ عنه","what_is_not_ar":"ليس الغفلة والتقصير إلا حيث جعلها المصدر تفسيرا آخر، وليس الانفراد في الشيء"},"support_links":["sup_bea0d49e5e6df578106e"]},{"boundary":"Kullanım yalnız kadınlara yönelik tanıklanmış adlandırma kalıplarıyla sınırlıdır; gerçek bir eş kaybı veya genel eşsizlik anlamı çıkarılamaz.","branch_kind":"collocation","branch_ref":"root_001692/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:1:1","qac_word_ref":"90:15:1","surface_ar":"يَتِيمًا"}],"gloss":"evlilikle sona erip ermediği tartışmalı kadın adlandırması","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kullanım, babasını yitirmiş çocuklara verilen adın kadın hakkında da söylenmesinden oluşur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir aktarımda kadın evlenince bu adlandırma sona erer; karşıt aktarımda ise kadın bu adı hiçbir zaman yitirmez."}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kadına yönelik bu özel adın evlilikten sonra sürüp sürmediğine ilişkin iki aktarımı birlikte özetlerken kullanılır.","boundary_detail":"Kullanım yalnız kadınlara yönelik tanıklanmış adlandırma kalıplarıyla sınırlıdır; gerçek bir eş kaybı veya genel eşsizlik anlamı çıkarılamaz.","branch_image_ar":"انفراد المرأة عن الزوج","concept_gloss":"evlilikle sona erip ermediği tartışmalı kadın adlandırması","contextual_glosses":[{"applicability":"Adlandırmanın kadının evlenmesiyle sona erdiğini kabul eden aktarımın bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadına yönelik kullanımı ve evlilikte sona erme sınırını korur."},"facet_ids":["F001","F002"],"text":"evlenene dek bu adla anılan kadın","usage_role":"contextual"},{"applicability":"Adlandırmanın evlilikten sonra da sürdüğünü kabul eden karşıt aktarımın bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadına yönelik kullanımı ve evlilikten sonra sürme bilgisini korur."},"facet_ids":["F001","F002"],"text":"evlendikten sonra da bu adla anılan kadın","usage_role":"contextual"}],"definition":"Kadına, babasını yitirmiş çocuklara verilen adla seslenilen kalıplaşmış bir kullanımdır. Bir aktarım bu adın evlilikle sona erdiğini, diğeri ise evlilikten sonra da sürdüğünü bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kullanım, babasını yitirmiş çocuklara verilen adın kadın hakkında da söylenmesinden oluşur."},{"facet_id":"F002","role":"source_variant","statement":"Bir aktarımda kadın evlenince bu adlandırma sona erer; karşıt aktarımda ise kadın bu adı hiçbir zaman yitirmez."}],"identity_rationale":"Kaynak ifadesi kocasından ayrılmış kadını tanımlamaz; kadına belirli bir adın verilmesini ve bu adın evlilikle sona erip ermediğine ilişkin iki karşıt aktarımı bildirir. Dal korunabilir, ancak tanımı eşten ayrılma yerine bu kalıplaşmış ve tartışmalı adlandırmaya bağlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"evlenene dek, başka bir aktarıma göre ise evlendikten sonra da babasını yitirmiş çocuk adıyla anılan kadın"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kadınların babasını yitirmiş çocuk adıyla anılabileceğini bildiren söz"}],"lexicalization_note":"Tanım yalnız kadın hakkında kullanılan iki tanıklanmış söz kalıbına bağlıdır; buradan yalın biçime genel bir evlenmemişlik veya eşten ayrılma anlamı aktarılamaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel kadın adlandırmasını eşsiz olma, eşten kopma, ebeveyn kaybı ve eş olma alanlarından ayıran dört aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal gerçek medeni durumu tanımlamak yerine özel bir adlandırmayı aktarır; komşu dal ise kişinin eşinin bulunmamasını cinsiyet ayrımı olmadan bildirir.","focus_only":"Odak dal kadınlara verilen özel bir addır ve bir aktarımda evlilikten sonra da sürebilir.","gloss":"kadına verilen özel ad ile eşsiz olma","neighbor_only":"Komşu dal kadın veya erkeğin fiilen eşsiz olmasını ve evlenmeden kalmasını doğrudan anlatır.","neighbor_ref":"root_000073/B001","relation_type":"near_neighbor","shared_zone":"Evlenmemiş kadın, bir aktarımda iki kullanımın ortak bağlamında bulunabilir."},{"boundary_match":"partial","distinction":"Odak dal eşten ayrılmayı gerektirmez; komşu dalın çekirdeği ise eş bağının bulunmaması veya kesilmesidir.","focus_only":"Odak dal evlilik öncesinde kullanılan ve bazı aktarımlarda evlilik sonrasında da süren bir kadın adlandırmasıdır.","gloss":"kadın adlandırması ile eşten kopma","neighbor_only":"Komşu dal eşten kopma, uzun süre eşsiz kalma ve evlenmeme durumunu anlatır.","neighbor_ref":"root_001252/B009","relation_type":"near_neighbor","shared_zone":"Her iki dal kadın ve evlilik durumu çevresinde kullanılabilir."},{"boundary_match":"partial","distinction":"Biçim ortaklığına rağmen odak dalda ebeveyn ölümü kurucu değildir; komşu dalda ise ebeveynin ölümü ve katılımcı ayrımı anlamın temelidir.","focus_only":"Odak dal kadın hakkındaki kalıplaşmış adlandırmayı ve süresine ilişkin aktarım ayrılığını içerir.","gloss":"kadına verilen ad ile ebeveyn kaybı","neighbor_only":"Komşu dal insan çocuğunun babasını ergenlikten önce, hayvan yavrusunun ise annesini yitirmesiyle oluşan gerçek durumu bildirir.","neighbor_ref":"root_001692/B001","relation_type":"near_neighbor","shared_zone":"Kadına verilen ad, babasını yitirmiş çocuk için kullanılan adlandırmayla biçimsel olarak ortaktır."},{"boundary_match":"thematic_only","distinction":"Odak dalın içeriği adlandırmanın süresidir; komşu dalın içeriği ise eşin kendisi ve eş olma bağıdır, bu nedenle anlamsal örtüşme çok sınırlıdır.","focus_only":"Odak dal, kadına yönelik özel bir adın evlilikle sona erip ermediğini tartışır.","gloss":"kadın adlandırması ve eş olma","neighbor_only":"Komşu dal eş olan erkeği, eş olan kadını ve eş olma ilişkisini doğrudan adlandırır.","neighbor_ref":"root_000134/B001","relation_type":"thematic","shared_zone":"İki dal da evlilik ilişkisini çevreleyen söz varlığında yer alır."}],"source_phrase_ar":"المرأة تدعى يتيما ما لم تتزوج فإذا تزوجت زال عنها اسم اليتم؛ يقال للمرأة يتيمة لا يزول عنها اسم اليتم أبدا (tahdhib)","source_qualifications":[{"kind":"disagreement","summary":"Bir aktarım adlandırmayı evlenene kadar sürdürürken diğeri evliliğin bu adı sona erdirmediğini bildirir."}],"source_summary":"Kanıt, kadınlara özgü bu kalıplaşmış adlandırmanın evlilikle ilişkili olduğunu, ancak kullanım süresinin tek biçimde aktarılmadığını gösterir.","sources":["TA"],"what_is_ar":"يدخل فيه إطلاق يتيمة على المرأة عند من يجعله قبل الزواج أو لا يزيله الزواج","what_is_not_ar":"ليس اليتيم من الصبيان ولا كل منفرد من الأشياء ولا أم الأيتام"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["90:15:1"],"branch_refs":[],"candidate_id":"cand_ee5a4136c476ca058056","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"90:15:1:delayed-accusative-recipient","source_type":"word_analysis","support_ids":["sup_9f0a131267ae9bad0024","sup_e8b94b8bdedbf592e6b3"],"title":"delayed object completes feeding","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:15:1","qac_refs":["90:15:1:1"],"status":"accepted"}},{"anchor_refs":["90:15:1"],"branch_refs":[],"candidate_id":"cand_0be25367fbde69893fc9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"90:15:1:indefinite-cadence-binds-need-and-relation","source_type":"word_analysis","support_ids":["sup_1fae61e014efe29f17e1","sup_e8b94b8bdedbf592e6b3"],"title":"tanwin cadence frames vulnerability and relation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:15:1","qac_refs":["90:15:1:1"],"status":"accepted"}},{"anchor_refs":["90:15:1"],"branch_refs":[],"candidate_id":"cand_a05227262bcc2f542977","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"90:15:1:indefinite-singular-human-case","source_type":"word_analysis","support_ids":["sup_211e80bc06697f1efb67","sup_e8b94b8bdedbf592e6b3"],"title":"unnamed singular condition becomes concrete recipient","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:15:1","qac_refs":["90:15:1:1"],"status":"accepted"}},{"anchor_refs":["90:15:1"],"branch_refs":[],"candidate_id":"cand_322b3d6bd34921678f99","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"90:15:1:orphanhood-as-severed-support","source_type":"word_analysis","support_ids":["sup_ca3c64ce5e9e108783cc","sup_e8b94b8bdedbf592e6b3"],"title":"orphan sense carries cut-off support pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:15:1","qac_refs":["90:15:1:1"],"status":"accepted"}},{"anchor_refs":["90:15:1"],"branch_refs":[],"candidate_id":"cand_455b13a224570fb5fb54","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"90:15:1:proximity-narrows-open-recipient","source_type":"word_analysis","support_ids":["sup_05ac8b25f2ae18f863ca","sup_e8b94b8bdedbf592e6b3"],"title":"kinship qualifier sharpens the claim","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:15:1","qac_refs":["90:15:1:1"],"status":"accepted"}},{"anchor_refs":["90:15:1"],"branch_refs":[],"candidate_id":"cand_37f7c2856835a0ad1b97","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"90:15:1:recipient-sequence-and-mercy-arc","source_type":"word_analysis","support_ids":["sup_9f00278eebda02910bdc","sup_e8b94b8bdedbf592e6b3"],"title":"orphan opens the recipient sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:15:1","qac_refs":["90:15:1:1"],"status":"accepted"}},{"anchor_refs":["90:15:2"],"branch_refs":[],"candidate_id":"cand_eebfa74bb2b6574d159d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:15:2:agreement-keeps-orphan-head","source_type":"word_analysis","support_ids":["sup_1ab8a0f696c192849f7b","sup_f0702c5a888c8f1a20fb"],"title":"case agreement keeps one recipient phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:15:2","qac_refs":["90:15:2:1"],"status":"accepted"}},{"anchor_refs":["90:15:2"],"branch_refs":[],"candidate_id":"cand_888fa1958f6fdfe9ccb0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:15:2:characterization-not-demonstration-or-ownership","source_type":"word_analysis","support_ids":["sup_1ab8a0f696c192849f7b","sup_4757123f6fe4823070e0"],"title":"possession becomes borne relational status","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:15:2","qac_refs":["90:15:2:1"],"status":"accepted"}},{"anchor_refs":["90:15:2"],"branch_refs":[],"candidate_id":"cand_ee57a01441320037fa5d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:15:2:compact-form-makes-claim-individual","source_type":"word_analysis","support_ids":["sup_1ab8a0f696c192849f7b","sup_1cf3519cd0ba7847e7d8"],"title":"compact singular form individualizes the claim","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:15:2","qac_refs":["90:15:2:1"],"status":"accepted"}},{"anchor_refs":["90:15:2"],"branch_refs":[],"candidate_id":"cand_6b2060fe7cbe50f4ff1f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:15:2:construct-hinge-requires-relation","source_type":"word_analysis","support_ids":["sup_1ab8a0f696c192849f7b","sup_d8c07868c4beefe8299c"],"title":"construct hinge binds the genitive relation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:15:2","qac_refs":["90:15:2:1"],"status":"accepted"}},{"anchor_refs":["90:15:2"],"branch_refs":[],"candidate_id":"cand_ce52af74d1ad437b8a01","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:15:2:rights-bearing-nearness-frame","source_type":"word_analysis","support_ids":["sup_1ab8a0f696c192849f7b","sup_fba60473cc04627a8882"],"title":"near-relation formula carries claim pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:15:2","qac_refs":["90:15:2:1"],"status":"accepted"}},{"anchor_refs":["90:15:2"],"branch_refs":[],"candidate_id":"cand_cc7a3a03c13fa4624d21","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:15:2:sequence-and-sound-hinge","source_type":"word_analysis","support_ids":["sup_1ab8a0f696c192849f7b","sup_711a17b3357093cd42ad"],"title":"same possessor frame bridges adjacent pressures","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:15:2","qac_refs":["90:15:2:1"],"status":"accepted"}},{"anchor_refs":["90:15:3"],"branch_refs":[],"candidate_id":"cand_2fc35bddf270bf08c83a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001212"],"scope":"focus_ayah","source_local_id":"90:15:3:abstract-form-makes-nearness-state","source_type":"word_analysis","support_ids":["sup_4001dca0008f60b2c8b2","sup_412c6e9e0b8a7a8b846f"],"title":"marked abstract form foregrounds relation itself","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:15:3","qac_refs":["90:15:3:1"],"status":"accepted"}},{"anchor_refs":["90:15:3"],"branch_refs":[],"candidate_id":"cand_733f8ff27ef67adced48","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001212"],"scope":"focus_ayah","source_local_id":"90:15:3:closing-accountability","source_type":"word_analysis","support_ids":["sup_412c6e9e0b8a7a8b846f","sup_d6d26f77aa3906417c07"],"title":"final relation word seals accountability","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:15:3","qac_refs":["90:15:3:1"],"status":"accepted"}},{"anchor_refs":["90:15:3"],"branch_refs":[],"candidate_id":"cand_1204e4bb63f4ab1033d3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001212"],"scope":"focus_ayah","source_local_id":"90:15:3:genitive-relation-not-object","source_type":"word_analysis","support_ids":["sup_412c6e9e0b8a7a8b846f","sup_7faf99d6c6d5c5f343bf"],"title":"genitive relation completes one recipient","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:15:3","qac_refs":["90:15:3:1"],"status":"accepted"}},{"anchor_refs":["90:15:3"],"branch_refs":[],"candidate_id":"cand_7a4c71e240b068c59fd7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001212"],"scope":"focus_ayah","source_local_id":"90:15:3:kinship-with-proximity-pressure","source_type":"word_analysis","support_ids":["sup_412c6e9e0b8a7a8b846f","sup_81828cab72653f0f677b"],"title":"kinship selected from wider nearness field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:15:3","qac_refs":["90:15:3:1"],"status":"accepted"}},{"anchor_refs":["90:15:3"],"branch_refs":[],"candidate_id":"cand_8ca449c71fe4a48c7fa2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001212"],"scope":"focus_ayah","source_local_id":"90:15:3:one-recipient-fuses-charity-categories","source_type":"word_analysis","support_ids":["sup_412c6e9e0b8a7a8b846f","sup_cb3bc9be2435e9c5b9bd"],"title":"orphan and near relative fuse into one claim-holder","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:15:3","qac_refs":["90:15:3:1"],"status":"accepted"}},{"anchor_refs":["90:15:3"],"branch_refs":[],"candidate_id":"cand_97926ee03a3e1eaf1df3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001212"],"scope":"focus_ayah","source_local_id":"90:15:3:sound-chain-hunger-nearness-dust","source_type":"word_analysis","support_ids":["sup_412c6e9e0b8a7a8b846f","sup_4235ea3fdb2afd050ce2"],"title":"middle rhyme links hunger, nearness, and destitution","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:15:3","qac_refs":["90:15:3:1"],"status":"accepted"}},{"anchor_refs":["90:15:1"],"branch_refs":[],"candidate_id":"cand_b38607f020ef90d8d0a9","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"90:15:1:1","source_type":"qac_morpheme","support_ids":["sup_8d7c2bec78098aade78a"],"title":"QAC root occurrence: ي ت م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["90:15:3"],"branch_refs":[],"candidate_id":"cand_72369d983aa68693985c","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001212"],"scope":"focus_ayah","source_local_id":"90:15:3:1","source_type":"qac_morpheme","support_ids":["sup_c5fcab6ccc57b9ac56cf"],"title":"QAC root occurrence: ق ر ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["90:15"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:15","branch_refs":["root_001212/B003","root_001692/B001"],"candidate_id":"cand_196524c06262313fb4fd","commentary_obligation":"review","hft_ref":"hft_a3be13f4a9149f575a84","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b01_severance_within_kinship","source_type":"hft","support_ids":["sup_d222801d97d8d4b15059"],"title":"b01_severance_within_kinship","trust":"legacy_unbound"},{"anchor_refs":["90:15"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:15","branch_refs":["root_001212/B001","root_001692/B002"],"candidate_id":"cand_9bbf162904d99c2dcac2","commentary_obligation":"review","hft_ref":"hft_30c5c4b2aec793f0439d","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b02_near_yet_unaccompanied","source_type":"hft","support_ids":["sup_f485dfbf32fa0aced728"],"title":"b02_near_yet_unaccompanied","trust":"legacy_unbound"},{"anchor_refs":["90:15"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:15","branch_refs":["root_001212/B002","root_001692/B004"],"candidate_id":"cand_ffa8b32ec312649e6326","commentary_obligation":"review","hft_ref":"hft_1a8ef0a681dd90de2762","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b03_delayed_care_at_a_closing_interval","source_type":"hft","support_ids":["sup_bea0d49e5e6df578106e"],"title":"b03_delayed_care_at_a_closing_interval","trust":"legacy_unbound"},{"anchor_refs":["90:15"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:15","branch_refs":["root_001212/B004","root_001692/B001"],"candidate_id":"cand_e49c796183af29c5e8b0","commentary_obligation":"review","hft_ref":"hft_88fc74ceb0aeaff915f8","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b04_access_reversal","source_type":"hft","support_ids":["sup_445e7b651dd2ef824320"],"title":"b04_access_reversal","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"يَتِيمًۭا ذَا مَقْرَبَةٍ","qac_morphemes":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:1:1","qac_word_ref":"90:15:1","root_ar":"ي ت م","surface_ar":"يَتِيمًا"},{"lemma_ar":"ذَا","morph_features":"STEM|POS:N|LEM:*aA|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:2:1","qac_word_ref":"90:15:2","root_ar":"","surface_ar":"ذَا"},{"lemma_ar":"مَقْرَبَة","morph_features":"STEM|POS:N|LEM:maqorabap|ROOT:qrb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:3:1","qac_word_ref":"90:15:3","root_ar":"ق ر ب","surface_ar":"مَقْرَبَةٍ"}],"word_analysis_qac_refs":[["90:15:1:1"],["90:15:2:1"],["90:15:3:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["90:15:1","90:15:2","90:15:3"]},"focus_surface_evidence":{"arabic_uthmani":"يَتِيمًۭا ذَا مَقْرَبَةٍ","qac_morphemes":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:1:1","qac_word_ref":"90:15:1","root_ar":"ي ت م","surface_ar":"يَتِيمًا"},{"lemma_ar":"ذَا","morph_features":"STEM|POS:N|LEM:*aA|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:2:1","qac_word_ref":"90:15:2","root_ar":"","surface_ar":"ذَا"},{"lemma_ar":"مَقْرَبَة","morph_features":"STEM|POS:N|LEM:maqorabap|ROOT:qrb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:15:3:1","qac_word_ref":"90:15:3","root_ar":"ق ر ب","surface_ar":"مَقْرَبَةٍ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["90:15:1:1"],["90:15:2:1"],["90:15:3:1"]],"word_analysis_refs":["90:15:1","90:15:2","90:15:3"],"word_rows":[{"analysis_record_ref":"90:15:1","analytic_gloss_range_en":"an unnamed singular orphan or dependent child, accusative as the recipient of the feeding action carried over from 90:14 and then narrowed by a nearness qualifier","analytic_root_gloss_range_en":"the root includes orphaned offspring cut off from protection and broader isolation or secondary lack branches; the local feeding frame selects dependent orphanhood while retaining severed-support pressure","qac_refs":["90:15:1:1"],"root":{"arabic":"ي ت م","transliteration":"y-t-m"},"surface":{"arabic":"يَتِيمًۭا","transliteration":"yatīman"}},{"analysis_record_ref":"90:15:2","analytic_gloss_range_en":"accusative masculine singular five-noun construct used adjectivally, marking the orphan as characterized by nearness rather than adding a separate owner or demonstrative element","analytic_root_gloss_range_en":"the root/form family includes possessor-characterization, dialectal relative use, demonstrative use, and interrogative compounds; the local construct with a genitive abstract selects possessor-characterization","qac_refs":["90:15:2:1"],"root":{"arabic":"ذ و و","transliteration":"dh-w-w"},"surface":{"arabic":"ذَا","transliteration":"dhā"}},{"analysis_record_ref":"90:15:3","analytic_gloss_range_en":"a genitive indefinite abstract noun naming nearness or kin relation as the possessed qualifier of the orphan, not a second feeding object or direct adjective","analytic_root_gloss_range_en":"the root spans spatial nearness, kinship, access, approach, offering, imminence, and other concrete branches; the local construct selects social or kin nearness while allowing proximity, access, and urgency pressure to remain felt","qac_refs":["90:15:3:1"],"root":{"arabic":"ق ر ب","transliteration":"q-r-b"},"surface":{"arabic":"مَقْرَبَةٍ","transliteration":"maqrabatin"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["90:15"],"branch_refs":["root_001212/B003","root_001692/B001"],"candidate_id":"cand_196524c06262313fb4fd","evidence_scope":"focus_ayah","hft_ref":"hft_a3be13f4a9149f575a84","item_id":"b01_severance_within_kinship","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b01_severance_within_kinship","support_id":"sup_d222801d97d8d4b15059"},{"anchor_refs":["90:15"],"branch_refs":["root_001212/B001","root_001692/B002"],"candidate_id":"cand_9bbf162904d99c2dcac2","evidence_scope":"focus_ayah","hft_ref":"hft_30c5c4b2aec793f0439d","item_id":"b02_near_yet_unaccompanied","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b02_near_yet_unaccompanied","support_id":"sup_f485dfbf32fa0aced728"},{"anchor_refs":["90:15"],"branch_refs":["root_001212/B002","root_001692/B004"],"candidate_id":"cand_ffa8b32ec312649e6326","evidence_scope":"focus_ayah","hft_ref":"hft_1a8ef0a681dd90de2762","item_id":"b03_delayed_care_at_a_closing_interval","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b03_delayed_care_at_a_closing_interval","support_id":"sup_bea0d49e5e6df578106e"},{"anchor_refs":["90:15"],"branch_refs":["root_001212/B004","root_001692/B001"],"candidate_id":"cand_e49c796183af29c5e8b0","evidence_scope":"focus_ayah","hft_ref":"hft_88fc74ceb0aeaff915f8","item_id":"b04_access_reversal","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b04_access_reversal","support_id":"sup_445e7b651dd2ef824320"}],"diagnostics":[],"lane_counts":{"global":17,"macro":3,"micro":4},"packet_summary":{"ayah_count":20,"focus_ref":"90:15","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ح ل ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000351","furuq_root_norm":"ح ل ل","furuq_source_root_norm":"ح ل ل","is_dominant":true,"target_occurrences":39,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000353","furuq_root_norm":"ح ل ي","furuq_source_root_norm":"ح ل ي","is_dominant":false,"target_occurrences":6,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"و ص د","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000036","furuq_root_norm":"ء ص د","furuq_source_root_norm":"أ ص د","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001653","furuq_root_norm":"و ص د","furuq_source_root_norm":"و ص د","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["90:1","90:2","90:3","90:4","90:5","90:6","90:7","90:8","90:9","90:10","90:11","90:12","90:13","90:14","90:15","90:16","90:17","90:18","90:19","90:20"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"90:15","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"90:15","lane":"micro","linguistic_source_ref":"90:15","surface_ref":"90:15","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"90:15","target_tokens":[["Akraba",["90:15:2","90:15:3"]],["bir",["90:15:1"]],["yetime",["90:15:1"]]],"text":"Akraba bir yetime"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":11,"ayah_to":20,"id":"s090-p02-011-020","label":"The steep path and the two companies","number":2,"refs":["90:11","90:12","90:13","90:14","90:15","90:16","90:17","90:18","90:19","90:20"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:1:proximity-narrows-open-recipient","source_type":"word_analysis","support_id":"sup_05ac8b25f2ae18f863ca","text":"{\"blocking_evidence\":null,\"headline\":\"kinship qualifier sharpens the claim\",\"reader_payoff\":\"The reader notices vulnerability first and then sees nearby relation intensify the obligation instead of replacing the orphan's need.\",\"reason\":\"Attachment evidence binds {{ar:ذَا مَقْرَبَةٍ}} ({{tr:dhā maqrabatin}}) to {{ar:يَتِيمًۭا}} ({{tr:yatīman}}), so the relation narrows the same recipient rather than adding a second participant.\",\"representative_source_ids\":[\"QI-3fd1f77b\",\"QI-f8b44711\",\"MT-201ec54c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:2","source_type":"word_analysis","support_id":"sup_1ab8a0f696c192849f7b","text":"{\"gloss_range\":\"accusative masculine singular five-noun construct used adjectivally, marking the orphan as characterized by nearness rather than adding a separate owner or demonstrative element\",\"prose\":\"{{ar:ذَا}} ({{tr:dhā}}) is the grammatical hinge that turns orphanhood and nearness into one recipient description. Its accusative masculine singular form agrees with {{ar:يَتِيمًۭا}} ({{tr:yatīman}}), not with the feminine genitive noun after it, so the orphan remains the head of the phrase. At the same time, {{ar:ذَا}} ({{tr:dhā}}) requires {{ar:مَقْرَبَةٍ}} ({{tr:maqrabatin}}) as its construct complement; the relation is therefore fastened to the orphan rather than left as outside context. The wider form family can include demonstrative or relative functions, but this local iḍāfa selects characterization: the orphan is one bearing nearness as a status, not one owning a thing. The compact one-syllable surface carries case, possession-status, and singular focus at once, so the relational claim stays attached to one orphan rather than dissolving into a plural class. It also lets the near-relative right named in 17:26 press into this phrase, now embedded inside orphanhood. The same five-noun frame links the surrounding sequence: a day characterized by famine in 90:14 gives way to an orphan characterized by nearness here, then to a poor person characterized by dust in 90:16.\",\"root_display\":\"{{ar:ذ و و}} ({{tr:dh-w-w}})\",\"root_gloss_range\":\"the root/form family includes possessor-characterization, dialectal relative use, demonstrative use, and interrogative compounds; the local construct with a genitive abstract selects possessor-characterization\",\"surface_display\":\"{{ar:ذَا}} ({{tr:dhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:2:compact-form-makes-claim-individual","source_type":"word_analysis","support_id":"sup_1cf3519cd0ba7847e7d8","text":"{\"blocking_evidence\":null,\"headline\":\"compact singular form individualizes the claim\",\"reader_payoff\":\"The reader feels one syllable carrying case, characterization, and singular focus, so the relational claim is faced person by person.\",\"reason\":\"The five-noun paradigm makes the accusative form visible in {{ar:ذَا}} ({{tr:dhā}}), and the singular form keeps the qualifier attached to one orphan.\",\"representative_source_ids\":[\"QF-296e989e\",\"QF-331e7c43\",\"QF-5a44ff7f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:1:indefinite-cadence-binds-need-and-relation","source_type":"word_analysis","support_id":"sup_1fae61e014efe29f17e1","text":"{\"blocking_evidence\":null,\"headline\":\"tanwin cadence frames vulnerability and relation\",\"reader_payoff\":\"The reader hears the orphan and the relation as one linked recipient phrase, with the open noun answered by the closing relation noun.\",\"reason\":\"The repeated indefinite endings around {{ar:ذَا}} ({{tr:dhā}}) support an audible bond between {{ar:يَتِيمًۭا}} ({{tr:yatīman}}) and {{ar:مَقْرَبَةٍ}} ({{tr:maqrabatin}}).\",\"representative_source_ids\":[\"QE-08207703\",\"QP-4a0af7c0\",\"QP-6c7b3254\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:1:indefinite-singular-human-case","source_type":"word_analysis","support_id":"sup_211e80bc06697f1efb67","text":"{\"blocking_evidence\":null,\"headline\":\"unnamed singular condition becomes concrete recipient\",\"reader_payoff\":\"The reader sees one concrete vulnerable person, not a named beneficiary, a bulk social category, or orphanhood as an abstraction.\",\"reason\":\"The local form is indefinite, masculine singular, and substantival, so {{ar:يَتِيمًۭا}} ({{tr:yatīman}}) identifies a person through the condition he bears.\",\"representative_source_ids\":[\"QG-e51f7544\",\"QG-e702373f\",\"QF-0557c233\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:3:abstract-form-makes-nearness-state","source_type":"word_analysis","support_id":"sup_4001dca0008f60b2c8b2","text":"{\"blocking_evidence\":null,\"headline\":\"marked abstract form foregrounds relation itself\",\"reader_payoff\":\"The reader notices that the ayah does not merely call the orphan near; it names nearness as the state he bears.\",\"reason\":\"The feminine abstract genitive form {{ar:مَقْرَبَةٍ}} ({{tr:maqrabatin}}) avoids a direct masculine adjective and packages relation as a possessed state.\",\"representative_source_ids\":[\"QF-24958cda\",\"QF-d753477b\",\"MF-a71a8eb5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:3","source_type":"word_analysis","support_id":"sup_412c6e9e0b8a7a8b846f","text":"{\"gloss_range\":\"a genitive indefinite abstract noun naming nearness or kin relation as the possessed qualifier of the orphan, not a second feeding object or direct adjective\",\"prose\":\"{{ar:مَقْرَبَةٍ}} ({{tr:maqrabatin}}) closes the phrase by naming the relation borne by the orphan. Its genitive case after {{ar:ذَا}} ({{tr:dhā}}) blocks a second feeding-object reading and blocks a simple direct-adjective reading; the grammar is not merely a near orphan, but an orphan characterized by nearness. The local sense selects social or kin nearness, yet the broader {{ar:ق ر ب}} ({{tr:q-r-b}}) field keeps proximity active: the need is close enough to know, to approach, and to answer. Its marked abstract form matters too. Instead of a plain person-label or a definite legal category, {{ar:مَقْرَبَةٍ}} ({{tr:maqrabatin}}) makes nearness itself the qualifying state, allowing the duty to generalize while still pressing kinship. As the final word, it leaves relational accountability ringing at the phrase edge. It also sits in a sound-and-meaning chain with the famine condition of 90:14 and the dust-poverty qualifier of 90:16, while 2:177 shows relatives and orphans as separable charity categories that 90:15 compresses into one recipient.\",\"root_display\":\"{{ar:ق ر ب}} ({{tr:q-r-b}})\",\"root_gloss_range\":\"the root spans spatial nearness, kinship, access, approach, offering, imminence, and other concrete branches; the local construct selects social or kin nearness while allowing proximity, access, and urgency pressure to remain felt\",\"surface_display\":\"{{ar:مَقْرَبَةٍ}} ({{tr:maqrabatin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:3:sound-chain-hunger-nearness-dust","source_type":"word_analysis","support_id":"sup_4235ea3fdb2afd050ce2","text":"{\"blocking_evidence\":null,\"headline\":\"middle rhyme links hunger, nearness, and destitution\",\"reader_payoff\":\"The reader hears {{ar:مَقْرَبَةٍ}} ({{tr:maqrabatin}}) as the middle term in a three-ayah cadence joining hunger in 90:14, kin-nearness here, and dust-poverty in 90:16.\",\"reason\":\"The rows identify repeated abstract shapes, tanwīn cadence, and adjacent qualifier slots across 90:14-16 with {{ar:مَقْرَبَةٍ}} ({{tr:maqrabatin}}) as the middle term.\",\"representative_source_ids\":[\"QP-093a98a3\",\"QE-d046298a\",\"QY-ee8694a4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:2:characterization-not-demonstration-or-ownership","source_type":"word_analysis","support_id":"sup_4757123f6fe4823070e0","text":"{\"blocking_evidence\":null,\"headline\":\"possession becomes borne relational status\",\"reader_payoff\":\"The reader understands nearness as a status adhering to the orphan, not as property ownership or a demonstrative pointer.\",\"reason\":\"V4 lists demonstrative and relative branches for {{ar:ذ و و}} ({{tr:dh-w-w}}), but the local five-noun construct with an abstract genitive selects possessor-characterization.\",\"representative_source_ids\":[\"QS-22a51db5\",\"QS-0c0199ba\",\"MS-8112d113\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:2:sequence-and-sound-hinge","source_type":"word_analysis","support_id":"sup_711a17b3357093cd42ad","text":"{\"blocking_evidence\":null,\"headline\":\"same possessor frame bridges adjacent pressures\",\"reader_payoff\":\"The reader hears and sees a repeated possessor skeleton shift from famine to kinship to dust-poverty across 90:14-16.\",\"reason\":\"The rows track the five-noun frame across 90:14-16 and note the short central sound of {{ar:ذَا}} ({{tr:dhā}}) between the heavier indefinite nouns.\",\"representative_source_ids\":[\"QE-87847648\",\"QP-f1b3eaff\",\"QB-eb35b72e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:3:genitive-relation-not-object","source_type":"word_analysis","support_id":"sup_7faf99d6c6d5c5f343bf","text":"{\"blocking_evidence\":null,\"headline\":\"genitive relation completes one recipient\",\"reader_payoff\":\"The reader sees nearness as the orphan's qualifying relation, not as another recipient or a loose noun beside him.\",\"reason\":\"QAC marks {{ar:مَقْرَبَةٍ}} ({{tr:maqrabatin}}) as genitive, and attachment evidence says it is governed by construct {{ar:ذَا}} ({{tr:dhā}}).\",\"representative_source_ids\":[\"QG-32637842\",\"QG-4bd17780\",\"MG-5b84761c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:3:kinship-with-proximity-pressure","source_type":"word_analysis","support_id":"sup_81828cab72653f0f677b","text":"{\"blocking_evidence\":null,\"headline\":\"kinship selected from wider nearness field\",\"reader_payoff\":\"The reader feels kinship as more than genealogy: the relation is near enough to remove distance as an excuse.\",\"reason\":\"The local pairing with {{ar:يَتِيمًۭا}} ({{tr:yatīman}}) and {{ar:ذَا}} ({{tr:dhā}}) selects kinship or social nearness while V4's access, approach, offering, and imminence branches survive only as pressure.\",\"representative_source_ids\":[\"QS-890e42a0\",\"QS-8cf927c0\",\"MS-d4cf9e22\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"90:15:1:1","source_type":"qac_morpheme","support_id":"sup_8d7c2bec78098aade78a","text":"{\"lemma_ar\":\"يَتِيم\",\"morph_features\":\"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|INDEF|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"90:15:1:1\",\"qac_word_ref\":\"90:15:1\",\"root_ar\":\"ي ت م\",\"surface_ar\":\"يَتِيمًا\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:1:recipient-sequence-and-mercy-arc","source_type":"word_analysis","support_id":"sup_9f00278eebda02910bdc","text":"{\"blocking_evidence\":null,\"headline\":\"orphan opens the recipient sequence\",\"reader_payoff\":\"The reader can track the orphan from sheltered-orphan memory (93:6) into the paired recipient sequence with the destitute person in 90:16 and the mercy ethic in 90:17.\",\"reason\":\"The CRITICAL rows give concrete links to 93:6, 90:16, and 90:17; these links extend the local role of {{ar:يَتِيمًۭا}} ({{tr:yatīman}}) without changing its grammar.\",\"representative_source_ids\":[\"MI-0366325e\",\"QE-02d19b4c\",\"ME-07002ad6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:1:delayed-accusative-recipient","source_type":"word_analysis","support_id":"sup_9f0a131267ae9bad0024","text":"{\"blocking_evidence\":null,\"headline\":\"delayed object completes feeding\",\"reader_payoff\":\"The reader notices that the first word of 90:15 completes the feeding action from 90:14 rather than starting an isolated new thought.\",\"reason\":\"QAC marks {{ar:يَتِيمًۭا}} ({{tr:yatīman}}) as accusative, and the attachment support warns that it continues the feeding construction begun in 90:14.\",\"representative_source_ids\":[\"QG-d45bcc65\",\"QG-0d33268c\",\"QB-39e4dc7e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"90:15:3:1","source_type":"qac_morpheme","support_id":"sup_c5fcab6ccc57b9ac56cf","text":"{\"lemma_ar\":\"مَقْرَبَة\",\"morph_features\":\"STEM|POS:N|LEM:maqorabap|ROOT:qrb|F|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"90:15:3:1\",\"qac_word_ref\":\"90:15:3\",\"root_ar\":\"ق ر ب\",\"surface_ar\":\"مَقْرَبَةٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:1:orphanhood-as-severed-support","source_type":"word_analysis","support_id":"sup_ca3c64ce5e9e108783cc","text":"{\"blocking_evidence\":null,\"headline\":\"orphan sense carries cut-off support pressure\",\"reader_payoff\":\"The reader hears the recipient as someone whose ordinary channel of care has failed, so feeding becomes repair of exposed dependency.\",\"reason\":\"V4 allows wider isolation branches for {{ar:ي ت م}} ({{tr:y-t-m}}), but the local recipient of feeding selects orphaned dependency rather than peerless uniqueness or unrelated secondary senses.\",\"representative_source_ids\":[\"QS-14e359d1\",\"QS-a41c1afe\",\"MS-701b0b12\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:3:one-recipient-fuses-charity-categories","source_type":"word_analysis","support_id":"sup_cb3bc9be2435e9c5b9bd","text":"{\"blocking_evidence\":null,\"headline\":\"orphan and near relative fuse into one claim-holder\",\"reader_payoff\":\"The reader sees one person carry two claims that can be listed separately elsewhere: orphan vulnerability and near-relative obligation (2:177).\",\"reason\":\"The CRITICAL rows explicitly compare 90:15 with 2:177, where relatives and orphans can be separate categories, while the local phrase joins them.\",\"representative_source_ids\":[\"QI-4c37019a\",\"QI-a64dbc6e\",\"MI-37ba47bf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:3:closing-accountability","source_type":"word_analysis","support_id":"sup_d6d26f77aa3906417c07","text":"{\"blocking_evidence\":null,\"headline\":\"final relation word seals accountability\",\"reader_payoff\":\"The reader feels the ayah end on relational accountability while the accountable giver remains implicit.\",\"reason\":\"{{ar:مَقْرَبَةٍ}} ({{tr:maqrabatin}}) is the final word of 90:15 and completes the phrase without naming the side to whom the orphan is near.\",\"representative_source_ids\":[\"QT-844c7e4c\",\"QT-bf27b547\",\"QT-fc409f2f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:2:construct-hinge-requires-relation","source_type":"word_analysis","support_id":"sup_d8c07868c4beefe8299c","text":"{\"blocking_evidence\":null,\"headline\":\"construct hinge binds the genitive relation\",\"reader_payoff\":\"The reader notices that the small middle word is incomplete by itself and makes nearness the content of the orphan's qualifier.\",\"reason\":\"Attachment evidence makes {{ar:مَقْرَبَةٍ}} ({{tr:maqrabatin}}) the syntactically forced genitive complement of construct {{ar:ذَا}} ({{tr:dhā}}).\",\"representative_source_ids\":[\"QG-93823dd6\",\"QF-2da2ebcb\",\"QT-a2e59846\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:1","source_type":"word_analysis","support_id":"sup_e8b94b8bdedbf592e6b3","text":"{\"gloss_range\":\"an unnamed singular orphan or dependent child, accusative as the recipient of the feeding action carried over from 90:14 and then narrowed by a nearness qualifier\",\"prose\":\"{{ar:يَتِيمًۭا}} ({{tr:yatīman}}) opens the ayah by filling the object position left waiting after the feeding scene of 90:14. Its accusative form keeps the word tied to that prior action, so the reader meets the recipient as delayed grammatical completion rather than as a fresh sentence. The indefinite singular does not name a known child or an abstract class; it lets one recognizable case of orphaned dependency stand in front of the listener. The root field can reach broader isolation, but the feeding frame selects a dependent child cut off from ordinary protection, making the act answer a broken support channel. Only after that vulnerability is named does {{ar:ذَا مَقْرَبَةٍ}} ({{tr:dhā maqrabatin}}) tighten the scene: the orphan is near in relation, so the duty remains general in principle but becomes especially hard to evade when proximity is present. The word also starts a recipient sequence: the sheltered-orphan memory of 93:6 turns here into a human test of whether shelter is extended, this orphan is paired with the destitute person of 90:16, and the ethic widens into mutual mercy in 90:17. Its indefinite cadence is part of that compression: the opening orphan noun is audibly answered by the closing relation noun, so vulnerability and nearness are heard as one recipient description.\",\"root_display\":\"{{ar:ي ت م}} ({{tr:y-t-m}})\",\"root_gloss_range\":\"the root includes orphaned offspring cut off from protection and broader isolation or secondary lack branches; the local feeding frame selects dependent orphanhood while retaining severed-support pressure\",\"surface_display\":\"{{ar:يَتِيمًۭا}} ({{tr:yatīman}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:2:agreement-keeps-orphan-head","source_type":"word_analysis","support_id":"sup_f0702c5a888c8f1a20fb","text":"{\"blocking_evidence\":null,\"headline\":\"case agreement keeps one recipient phrase\",\"reader_payoff\":\"The reader sees the nearness phrase as an adjective of the orphan, not as a second object or a phrase controlled by the relation noun.\",\"reason\":\"QAC and attachment evidence identify {{ar:ذَا}} ({{tr:dhā}}) as accusative masculine singular and adjectival to {{ar:يَتِيمًۭا}} ({{tr:yatīman}}).\",\"representative_source_ids\":[\"QG-21213cf3\",\"QG-60e664dc\",\"MG-d636c934\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:15:2:rights-bearing-nearness-frame","source_type":"word_analysis","support_id":"sup_fba60473cc04627a8882","text":"{\"blocking_evidence\":null,\"headline\":\"near-relation formula carries claim pressure\",\"reader_payoff\":\"The reader hears the near-relation formula as claim-bearing, with the right of the near relative (17:26) embedded inside orphanhood here.\",\"reason\":\"The CRITICAL rows connect the {{ar:ذَا}} ({{tr:dhā}}) plus nearness frame to 17:26 while local grammar keeps the claim embedded in the orphan phrase.\",\"representative_source_ids\":[\"QI-2d38bee4\",\"QI-bf00a891\",\"MI-ad495453\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"يَتِيمًۭا ذَا مَقْرَبَةٍ","ayah_ref":"90:15"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001212/B003","root_001692/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001692","role":"Orphaned offspring cut off from a protector supplies the severed protective bond that defines the vulnerability.","root":"ي ت م","source_ref":"90:15","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_001212","role":"Blood kinship supplies the still-intact near network and makes that network the possible site of repair.","root":"ق ر ب","source_ref":"90:15","source_word_indices":["3"]}],"changed_reading":{"after":"A child bearing a severed protective bond inside a still-near kinship network; nearness intensifies rather than cancels the rupture.","before":"An orphan who happens to be a relative."},"confidence":"strong","focus_anchor":"The pairing of يَتِيمًا at word 1 with ذَا مَقْرَبَةٍ, anchored in مَقْرَبَةٍ at word 3.","mechanism":"The orphan branch supplies a child cut off from a protecting parent, while the nearness branch supplies a surviving blood relation. The phrase therefore holds rupture and connection together: one protective edge is gone, but a near relational network remains available to answer the loss.","model_id":"b01_severance_within_kinship"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b01_severance_within_kinship","source_type":"hft","support_id":"sup_d222801d97d8d4b15059","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"يَتِيمًۭا ذَا مَقْرَبَةٍ","ayah_ref":"90:15"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001212/B001","root_001692/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001692","role":"Isolated singleness supplies functional aloneness and distinguishes it from mere material need.","root":"ي ت م","source_ref":"90:15","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001212","role":"Nearness as the opposite of distance places that aloneness in immediate reach rather than far away.","root":"ق ر ب","source_ref":"90:15","source_word_indices":["3"]}],"changed_reading":{"after":"A person who is near enough to encounter but still socially singular: proximity without accompaniment.","before":"A nearby orphan."},"confidence":"medium","focus_anchor":"The semantic collision between يَتِيمًا at word 1 and مَقْرَبَةٍ at word 3.","mechanism":"Isolated singleness and nearness coexist in one person. The result is a social topology in which someone can be physically or relationally close yet functionally alone; the problem is not lack of adjacency but lack of protective accompaniment.","model_id":"b02_near_yet_unaccompanied"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b02_near_yet_unaccompanied","source_type":"hft","support_id":"sup_f485dfbf32fa0aced728","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"يَتِيمًۭا ذَا مَقْرَبَةٍ","ayah_ref":"90:15"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001212/B002","root_001692/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001692","role":"Slowing or delay in care supplies the neglected interval built into the orphan's condition.","root":"ي ت م","source_ref":"90:15","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001212","role":"Temporal nearness and approaching completion turn delayed care into a narrowing window rather than a timeless duty.","root":"ق ر ب","source_ref":"90:15","source_word_indices":["3"]}],"changed_reading":{"after":"One for whom beneficence has been late and whose window for relational repair is now pressing near.","before":"An orphan of close kin."},"confidence":"exploratory","focus_anchor":"The delayed-care branch of ي ت م at word 1 interacting with the temporal-nearness branch of مَقْرَبَةٍ at word 3.","mechanism":"One branch explains orphanhood through beneficence arriving slowly, while the other makes nearness temporal and end-directed. Their conjunction activates a deadline model: the vulnerable person is one toward whom care has lagged while the interval for effective repair is drawing close.","model_id":"b03_delayed_care_at_a_closing_interval"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b03_delayed_care_at_a_closing_interval","source_type":"hft","support_id":"sup_bea0d49e5e6df578106e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"يَتِيمًۭا ذَا مَقْرَبَةٍ","ayah_ref":"90:15"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001212/B004","root_001692/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001692","role":"Cutoff from a protecting parent supplies the person's exclusion from ordinary access and advocacy.","root":"ي ت م","source_ref":"90:15","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_001212","role":"Favored access and privileged nearness supply the inverted social position into which the unprotected person may be brought.","root":"ق ر ب","source_ref":"90:15","source_word_indices":["3"]}],"changed_reading":{"after":"The unprotected one figured as an insider with priority access, reversing the ordinary hierarchy of social favor.","before":"A kin orphan within the donor's existing circle."},"confidence":"exploratory","focus_anchor":"يَتِيمًا at word 1 joined to the access-and-favor branch available through مَقْرَبَةٍ at word 3.","mechanism":"The phrase juxtaposes loss of a protector with privileged nearness and access. This supports a status-reversal reading in which the socially unshielded person is not kept at the edge but treated as an insider whose access has priority.","model_id":"b04_access_reversal"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b04_access_reversal","source_type":"hft","support_id":"sup_445e7b651dd2ef824320","trust":"legacy_unbound"}]}
</lane_packet_json>
