# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **91:15**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s091-regular-20260912/s091/91_15/micro.discovery.json` and modify nothing
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
  "ayah_ref": "91:15",
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
{"branch_registry":[{"boundary":"Dal, korkunun kendisini ve kötü bir sonuç beklentisini kapsar; korkutma, korkuda yarışma, eksiltme ve eşya adları bu çekirdeğe girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000447/B001","candidate_links":[{"candidate_id":"cand_c38510af3c397691475f","lane":"micro"},{"candidate_id":"cand_5af7408e71349f106522","lane":"micro"},{"candidate_id":"cand_0cf01fe81cc5449f4dbc","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَافَ","morph_features":"STEM|POS:V|IMPF|LEM:xaAfa|ROOT:xwf|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:15:2:1","qac_word_ref":"91:15:2","surface_ar":"يَخَافُ"}],"gloss":"bir belirtiye dayanarak kötü bir şey bekleme korkusu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İstenmeyen bir olayın gerçekleşeceği, bilinen ya da sanılan bir belirtiye dayanılarak beklenir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu beklenti kişide korku, ürküntü ve kaçınma eğilimi doğuran bir ruh hali olarak yaşanır."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kavram, kişinin kendisini güven içinde hissettiği durumun karşı kutbunu oluşturur."}}],"root_ar":"خ و ف","root_id":"root_000447","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Korkunun hem istenmeyen sonuç beklentisini hem de bu beklentiyi doğuran belirtiyi içerdiği genel kavramsal anlatımda kullanılır.","boundary_detail":"Dal, korkunun kendisini ve kötü bir sonuç beklentisini kapsar; korkutma, korkuda yarışma, eksiltme ve eşya adları bu çekirdeğe girmez.","branch_image_ar":"ذعر يتوقع المكروه","concept_gloss":"bir belirtiye dayanarak kötü bir şey bekleme korkusu","contextual_glosses":[{"applicability":"Bağlamın korkulan sonucu ve bu sonuca ilişkin belirtiyi zaten açıkça verdiği akıcı anlatımlarda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kötü sonucu bir belirtiye dayanarak bekleme yapısını ve güven karşıtlığını tek başına göstermez.","preserves":"Kişideki temel korku ve ürküntü halini korur."},"facet_ids":["F002"],"text":"korku","usage_role":"general"},{"applicability":"Belirtinin yaklaşan bir zarar ya da tehlike olarak yorumlandığı açıklayıcı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirtiyi sezmeyi, kötü sonuç beklentisini ve korku duymayı birlikte anlatır."},"facet_ids":["F001","F002"],"text":"tehlike sezerek korkma","usage_role":"explanatory"}],"definition":"Bilinen ya da sanılan bir belirtiye dayanarak istenmeyen bir şeyin gerçekleşmesini beklerken duyulan korku ve ürküntü halidir; güven içinde olmanın karşıtıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İstenmeyen bir olayın gerçekleşeceği, bilinen ya da sanılan bir belirtiye dayanılarak beklenir."},{"facet_id":"F002","role":"core","statement":"Bu beklenti kişide korku, ürküntü ve kaçınma eğilimi doğuran bir ruh hali olarak yaşanır."},{"facet_id":"F003","role":"core","statement":"Kavram, kişinin kendisini güven içinde hissettiği durumun karşı kutbunu oluşturur."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Ani, denetimsiz ve çok yoğun bir tepki izlenimi ekler.","collision":"Ani bunalım veya toplu kargaşa anlamlarıyla karışabilir.","fit":"displacement","loses":"Belirtiye dayalı kötü sonuç beklentisini ve daha sakin korku durumlarını dışarıda bırakır.","preserves":"Yoğun korku ve sarsılma yönünü kısmen korur."},"text":"panik"},{"category":"confusable","error_profile":{"adds":"Kişilere ya da kurumlara güvenmeme anlamını ekleyebilir.","collision":"Güven ilişkilerindeki kuşku anlamıyla karışabilir.","fit":"displacement","loses":"Kötü bir sonuç beklerken duyulan korku ve ürküntüyü belirtmez.","preserves":"Güven içinde olmama yönünü korur."},"text":"güvensizlik"}],"identity_rationale":"Hazırlanan dal, kaynak ifadesindeki ortak çekirdeği doğru biçimde karşılar: bilinen ya da sanılan bir belirtiye dayanarak istenmeyen bir şey beklemek kişide korku ve ürküntü doğurur. Kaynakların korkuyu güven içinde olmanın karşıtı sayması da aynı sınır içinde kalır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"korku"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"korkmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"korku hali"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"korku halleri"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"korku ve sakınma"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"korkan kimse"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"çok korkan adam"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"korkan topluluk"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"korkan topluluk"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kork!"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"onun başına bir şey gelmesinden korkmak"}],"lexicalization_note":"Yalın korku çekirdeği ile belirli söz öbeklerine ve katılımcı ilişkilerine bağlı kullanımlar ayrı tutulur; çok korkan kişi veya topluluk anlatımları ve başkası için korkma kullanımı yalın anlamın tamamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; korkunun içte duyulması, ani irkilme, uyanık sakınma, korkaklık ve korkutma sınırı açıklayan beş karşıtlık seçildi. Yalnızca aynı duygu alanında kalan ya da bu seçilenlerle tekrarlanan adaylar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ayırıcı yönü, istenmeyen sonucu bir belirtiye dayanarak beklemektir; komşu dal ise korkunun içte hissedilişini öne çıkarır ve bu beklenti yapısını zorunlu kılmaz.","focus_only":"Odak dal, korkuyu kötü bir sonucun belirtisine ve beklentisine açıkça bağlar.","gloss":"içte duyulan korku","neighbor_only":"Komşu dal, korkunun kalpte hissedilmesini ve içte duyulan ürkekliği öne çıkarır.","neighbor_ref":"root_001629/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da kişide yaşanan korku ve ürküntü halini anlatır."},{"boundary_match":"partial","distinction":"Komşu dal daha çok anlık sarsılma ve geri çekilme tepkisine yönelirken odak dal, bir belirti üzerinden kötü sonuç beklemeye uzanan daha genel korku halini anlatır.","focus_only":"Odak dalda kötü sonuç beklentisi ve güvenin karşıtı olma sınırı bulunur.","gloss":"irkilme ve geri çekilme","neighbor_only":"Komşu dal, korkutucu şey karşısında büzülme, irkilme ve ondan uzaklaşma tepkisini öne çıkarır.","neighbor_ref":"root_001152/B001","relation_type":"near_synonym","shared_zone":"İki dal da korkutucu bir şey karşısındaki korku yaşantısını kapsar."},{"boundary_match":"partial","distinction":"Korku bir ruh hali ve beklentidir; uyanık sakınma ise bu beklenti karşısında gösterilen dikkatli davranıştır. Biri ötekinin nedeni olabilir, fakat yerlerine kullanılamazlar.","focus_only":"Odak dal, istenmeyen sonucu beklerken duyulan korku halini merkez alır.","gloss":"uyanık sakınma","neighbor_only":"Komşu dal, tehlikeye karşı uyanık davranmayı, önlem almayı ve sakınmayı merkez alır.","neighbor_ref":"root_000301/B001","relation_type":"near_neighbor","shared_zone":"Korkulan bir zararı fark etme ve ondan kaçınma alanında buluşurlar."},{"boundary_match":"partial","distinction":"Odak dal kişilik özelliği gerektirmeyen bir korku halidir; komşu dal ise yaygın korkma eğilimine ve yüreksizliğe yaklaşır.","focus_only":"Odak dal, belirli bir kötü sonuç beklentisiyle ortaya çıkabilen durumluk korkuyu da kapsar.","gloss":"korkaklık ve ürkeklik","neighbor_only":"Komşu dal, her şeyden korkmaya yatkınlık ve yüreksizlik yönünü öne çıkarır.","neighbor_ref":"root_001625/B005","relation_type":"near_neighbor","shared_zone":"Her ikisinde de korku ve ürkme duygusu bulunur."},{"boundary_match":"partial","distinction":"Odak dal korkuyu yaşayan kişinin durumunu, komşu dal ise korkuyu başkasında meydana getiren eylemi veya özelliği anlatır.","focus_only":"Odak dal, korkunun kişinin içinde bulunması ve kötü sonucu beklemesidir.","gloss":"korkutma","neighbor_only":"Komşu dal, başka bir kişide korku doğuran neden ya da eylemdir.","neighbor_ref":"root_000447/B002","relation_type":"near_neighbor","shared_zone":"İki dal aynı korku yaşantısının farklı katılımcı ve aşamalarına bağlanır."}],"source_phrase_ar":"الخوف ضد الأمن خاف يخاف خوفا (jamhara خفو)؛ والخيفة مثل الخوف والجمع خيف (jamhara خيف)؛ خاف الرجل يخاف خوفا وخيفة ومخافة فهو خائف؛ والخيفة الخوف والجمع خيف وأصله الواو (sihah)؛ الخوف توقع مكروه عن أمارة مظنونة أو معلومة ويضاد الخوف الأمن (mufradat)؛ أصل واحد يدل على الذعر والفزع؛ خفت الشيء خوفا وخيفة (maqayis 992)؛ الخيف فجمع خيفة وليس من هذا الباب وقد ذكر في باب الواو بعد الخاء (maqayis 1001)؛ الخيفة الخوف (ayn)","source_summary":"Tanıklıklar korku ve ürküntüyü ortak çekirdek olarak verir. Bazı anlatımlar bu hali güvenin karşıtı diye sınırlar, bazıları ise bilinen ya da sanılan bir belirtiden hareketle kötü bir sonuç bekleme yönünü açıklar. Kaynaklar, çoğul biçimin bu kök altında değerlendirilip değerlendirilmemesi konusunda ayrılır.","sources":["AY","JA","SI","MU","MQ"],"what_is_ar":"الخوف والخيفة والمخافة؛ الفزع والذعر؛ توقع المكروه عن أمارة؛ ضد الأمن؛ حالة الخائف وما يتصل بها من خاف وخائف","what_is_not_ar":"ليس الأمن؛ وليس خيف الاختلاف في اللون أو العين أو السفح أو الضرع؛ وليس الخافة الوعاء أو الجبة"},"support_links":["sup_3a894df59abb0a29a206","sup_4a590348a1d84b3e8feb","sup_ef5715203eeafd5b4736"]},{"boundary":"Dal korkunun meydana getirilmesini kapsar; kişinin kendi korkusu ve iki kişinin korkuda birbirini geçmesi bu ettirgen anlamdan ayrıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000447/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَافَ","morph_features":"STEM|POS:V|IMPF|LEM:xaAfa|ROOT:xwf|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:15:2:1","qac_word_ref":"91:15:2","surface_ar":"يَخَافُ"}],"gloss":"korku doğurma ya da korkulur kılma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi, nesne veya durum başka birinde korku doğurur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi ya da şey, insanların ondan korkacağı bir duruma getirilir veya öyle nitelenir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Korku uyandırma, muhatabı sakınmaya ve önlem almaya yöneltmek için kullanılabilir."}}],"root_ar":"خ و ف","root_id":"root_000447","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir eylemin başkasını korkutmasını veya bir kişi ya da şeyin korkulan hale gelmesini birlikte kapsayan genel açıklamada kullanılır.","boundary_detail":"Dal korkunun meydana getirilmesini kapsar; kişinin kendi korkusu ve iki kişinin korkuda birbirini geçmesi bu ettirgen anlamdan ayrıdır.","branch_image_ar":"إدخال الخوف في الغير","concept_gloss":"korku doğurma ya da korkulur kılma","contextual_glosses":[{"applicability":"Bir kişinin başka bir kişide doğrudan korku uyandırdığı sıradan ettirgen bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir kişi ya da şeyi korkulur hale getirme ve korkuyla sakındırma uzantılarını tek başına göstermez.","preserves":"Başkasında korku doğurma çekirdeğini doğal ve kısa biçimde korur."},"facet_ids":["F001"],"text":"korkutma","usage_role":"general"},{"applicability":"Korku uyandırmanın amacının muhatabı tehlikeden uzak tutmak ve önlem almaya yöneltmek olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sakındırma amacı taşımayan korkutma ve korkulur hale getirme kullanımlarını dışarıda bırakır.","preserves":"Korku uyandırma ile sakınmaya yöneltme arasındaki amaç ilişkisini korur."},"facet_ids":["F001","F003"],"text":"korkuyla sakındırma","usage_role":"contextual"}],"definition":"Bir kişi, nesne veya durumun başkasında korku doğurması ya da bir kişi veya şeyi insanların korkacağı hale getirmesidir. Bu korku, kimi bağlamlarda muhatabı sakınmaya ve önlem almaya yöneltir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi, nesne veya durum başka birinde korku doğurur."},{"facet_id":"F002","role":"extension","statement":"Bir kişi ya da şey, insanların ondan korkacağı bir duruma getirilir veya öyle nitelenir."},{"facet_id":"F003","role":"specialization","statement":"Korku uyandırma, muhatabı sakınmaya ve önlem almaya yöneltmek için kullanılabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kasıtlı bir zarar bildirimi veya güç gösterisi bulunduğu izlenimini ekler.","collision":"Sözlü ya da davranışsal yıldırma anlamıyla karışabilir.","fit":"displacement","loses":"Korkutucu nesne ve yolları, ayrıca kendiliğinden korku doğuran durumları kapsamaz.","preserves":"Birini korkutarak davranışını etkileme yönünü korur."},"text":"gözdağı verme"},{"category":"confusable","error_profile":{"adds":"Korku içermeyen her türlü bilgi verme ve hatırlatma eylemini kapsar.","collision":"Tarafsız bilgilendirme veya kural hatırlatma anlamıyla karışabilir.","fit":"displacement","loses":"Başkasında korku doğurma çekirdeğini zorunlu olarak anlatmaz.","preserves":"Sakınmaya ve önlem almaya yöneltme sonucunu koruyabilir."},"text":"uyarma"}],"identity_rationale":"Hazırlanan dal, kaynak ifadesindeki ettirgen çekirdeği doğru verir: bir başkasına korku vermek, bir kişi ya da şeyi korkulur hale getirmek ve korku yoluyla sakınmaya yöneltmek. Korkuyu yaşayan kişi ile korkuyu doğuran kişi, nesne veya durum arasındaki yön farkı korunmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"korkutma veya korkuyla sakındırma"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"başkasını korkutma"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"korkutucu"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"korkulan veya tehlikeli"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"insanların korktuğu tehlikeli yol"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"Tanrı'nın korku uyandırarak sakındırması"}],"lexicalization_note":"Genel korkutma çekirdeği ile korkulan yol ve korku yoluyla sakındırma gibi söz öbeğine bağlı kullanımlar ayrı tutulur; bu özel kullanımlar yalın eylemin bütün kapsamına yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; içte yaşanan korku, doğrudan ürkütme, sakındırma, gözdağı ve baskıyla korkutma sınırlarını en iyi gösteren beş aday seçildi. Aynı ayrımı daha dar örneklerle yineleyen veya yalnızca ortak konu taşıyan adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ettirgendir ve korkuyu meydana getiren tarafa bakar; komşu dal ise korkuyu yaşayan kişinin iç durumuna bakar.","focus_only":"Odak dal, korkuyu başka bir kişide doğuran eylemi, nedeni veya niteliği anlatır.","gloss":"korku hali","neighbor_only":"Komşu dal, korkuyu yaşayan kişinin kötü bir sonuç beklerken içinde bulunduğu hali anlatır.","neighbor_ref":"root_000447/B001","relation_type":"near_neighbor","shared_zone":"İki dal aynı korku olayının neden ve yaşantı aşamalarına bağlanır."},{"boundary_match":"partial","distinction":"Komşu dal doğrudan ürkütme eylemine daha sıkı bağlıdır; odak dal ise korkutucu nitelik taşıyan şeyleri ve korkuyla sakındırma işlevini de içine alır.","focus_only":"Odak dal, korkulur hale getirme ve korku yoluyla sakındırma uzantılarını da kapsar.","gloss":"birini ürkütme","neighbor_only":"Komşu dal, bir kişiyi sarsıp ürküterek onda doğrudan korku meydana getirmeyi öne çıkarır.","neighbor_ref":"root_001152/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da başka bir kişide korku meydana getirme çekirdeğini paylaşır."},{"boundary_match":"partial","distinction":"Odak dal sonuç olarak korkuyu merkez alır; komşu dal ise korku doğmasa bile uyarma ve sakındırma eylemiyle tamamlanabilir.","focus_only":"Odak dalda korku doğurma, amaç olsun ya da olmasın, temel sonuçtur.","gloss":"sakınmaya çağırma","neighbor_only":"Komşu dalda temel amaç muhatabı tehlikeye karşı uyarmak ve sakınmaya çağırmaktır.","neighbor_ref":"root_000301/B002","relation_type":"near_neighbor","shared_zone":"Korku uyandıran bir uyarı, muhatabı tehlikeden sakınmaya yöneltebilir."},{"boundary_match":"partial","distinction":"Her gözdağı korkutma amacı taşısa da her korkutma bir zarar bildirimi değildir; odak dal sonuç ve nitelik bakımından daha geniştir.","focus_only":"Odak dal, sözlü bildirim bulunmadan da bir nesne, yol veya durumun korkutucu olmasını kapsar.","gloss":"gözdağı ve yıldırma","neighbor_only":"Komşu dal, gelecekte zarar verileceğini bildiren gözdağı ve yıldırma sözünü merkez alır.","neighbor_ref":"root_001580/B010","relation_type":"near_neighbor","shared_zone":"Gözdağı vermek, muhatapta korku doğurabilen bir eylemdir."},{"boundary_match":"partial","distinction":"Odak dal genel korkutma ve korkutucu niteliktir; komşu dal ise baskı kurma, gözdağı verme ve korkuyla hareket ettirme yönünde özelleşir.","focus_only":"Odak dal, korkulur nesne ve yol nitelemeleriyle korku yoluyla sakındırmayı da kapsar.","gloss":"korkutup yıldırma","neighbor_only":"Komşu dal, korkuyu baskı, yıldırma veya canlıları sürme aracı olarak kullanmaya kadar uzanır.","neighbor_ref":"root_000604/B002","relation_type":"near_synonym","shared_zone":"İki dal da başkasında korku meydana getiren ettirgen eylemi anlatır."}],"source_phrase_ar":"ومنه التخويف والإخافة؛ طريق مخوف يخافه الناس ومخيف يخيف الناس؛ خوفت الرجل جعلت فيه الخوف؛ خوفت الرجل أي صيرته بحال يخافه الناس (ayn)؛ الإخافة التخويف؛ وجع مخيف أي يخيف من رآه؛ طريق مخوف لأنه لا يخيف وإنما يخيف فيه قاطع الطريق (sihah)؛ التخويف من الله تعالى هو الحث على التحرز؛ ذلك يخوف الله به عباده؛ الشيطان يخوف أولياءه (mufradat)","source_summary":"Tanıklıklar başkasında korku doğurma üzerinde birleşir. Ortak anlatım, korkutucu nitelik taşıyan kişi, nesne ve yolları da kapsar; ayrıca korkunun sakınmaya yönelten bir uyarı işlevi görebileceğini belirtir.","sources":["AY","SI","MU"],"what_is_ar":"التخويف والإخافة؛ جعل الإنسان أو الطريق أو الشيء مخوفا أو مخيفا؛ الحث على التحرز بإثارة الخوف","what_is_not_ar":"ليس مجرد قيام الخوف في النفس؛ وليس المغالبة في الخوف بصيغة خاوفه"},"support_links":[]},{"boundary":"Dal yalnızca karşılıklı ve karşılaştırmalı kullanım içindir; sıradan korku hali ya da bir başkasını korkutma anlamına genellenemez.","branch_kind":"non_bare","branch_ref":"root_000447/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَافَ","morph_features":"STEM|POS:V|IMPF|LEM:xaAfa|ROOT:xwf|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:15:2:1","qac_word_ref":"91:15:2","surface_ar":"يَخَافُ"}],"gloss":"korkuda yarışıp ötekinden daha çok korkma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki kişi korku derecesi bakımından karşılıklı bir karşılaştırmaya girer."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sonuçta katılımcılardan biri ötekinden daha çok korkmuş sayılarak onu bu alanda geçer."}}],"root_ar":"خ و ف","root_id":"root_000447","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki kişinin korku derecesinin karşılaştırıldığı ve birinin daha çok korktuğunun belirtildiği özel kullanımda geçerlidir.","boundary_detail":"Dal yalnızca karşılıklı ve karşılaştırmalı kullanım içindir; sıradan korku hali ya da bir başkasını korkutma anlamına genellenemez.","branch_image_ar":"مغالبة في الخوف","concept_gloss":"korkuda yarışıp ötekinden daha çok korkma","contextual_glosses":[{"applicability":"Karşılıklı eylem biçiminin Türkçede açıklayıcı bir söz öbeğiyle açılması gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki taraflı karşılaştırmayı ve üstünlüğün daha çok korkmakla oluştuğunu korur."},"facet_ids":["F001","F002"],"text":"korku bakımından ötekini geçme","usage_role":"explanatory"},{"applicability":"Karşılaştırılan iki kişinin önceki cümlede açıkça belirtildiği kısa bağlamlarda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Karşılıklı çekişme ve birini aynı alanda geçme yapısını tek başına belirtmez.","preserves":"Bir kişinin ötekinden daha yüksek korku derecesinde olmasını korur."},"facet_ids":["F002"],"text":"daha çok korkma","usage_role":"contextual"}],"definition":"İki kişinin korku bakımından karşılaştırmalı bir çekişmeye girmesi ve birinin ötekinden daha çok korkarak onu bu ölçüde geçmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki kişi korku derecesi bakımından karşılıklı bir karşılaştırmaya girer."},{"facet_id":"F002","role":"core","statement":"Sonuçta katılımcılardan biri ötekinden daha çok korkmuş sayılarak onu bu alanda geçer."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bir katılımcının ötekinde korku meydana getirdiği ettirgen ilişkiyi ekler.","collision":"Aynı kökün başkasında korku doğurma dalıyla karışır.","fit":"displacement","loses":"Katılımcıların korku derecelerinin karşılaştırılmasını ve birinin daha çok korkmasını siler.","preserves":"Korku alanını ve iki katılımcı bulunabilmesini korur."},"text":"korkutma"},{"category":"confusable","error_profile":{"adds":"Daha az korkanın üstün sayıldığı karşıt bir ölçü ekler.","collision":"Cesaret veya dayanıklılık yarışmasıyla karışır.","fit":"displacement","loses":"Üstünlüğün daha çok korkmakla elde edilmesi yönünü tersine çevirir.","preserves":"İki katılımcı arasındaki yarışma yapısını korur."},"text":"korkusuzluk yarışı"}],"identity_rationale":"Hazırlanan dal, kaynakların verdiği karşılaştırmalı yapıyı doğru korur: iki kişi korku bakımından karşı karşıya gelir ve biri ötekinden daha çok korkarak onu bu ölçüde geçer. Buradaki üstünlük korkusuzluk değil, korkunun daha fazla olmasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"korkuda yarışıp ötekinden daha çok korkmak"}],"lexicalization_note":"Anlam, iki katılımcıyı korku derecesi bakımından karşılaştıran özel eylem biçimine bağlıdır; yalın kökün genel korku anlamı olarak sunulmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalın korku ve korkutma dallarıyla sınırın yanında, başka alanlardaki karşılıklı üstün gelme kalıbını gösteren üç temsilci seçildi. Ağlama örneklerinin tekrarı ve yalnızca başka duygu alanlarında kalan adaylar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal korkuyu tek başına adlandırmaz; iki katılımcılı özel bir karşılaştırma ister. Komşu dalda ise yarışma veya üstün gelme koşulu yoktur.","focus_only":"Odak dalda iki kişinin korku derecesi karşılaştırılır ve biri ötekini geçer.","gloss":"korku hali","neighbor_only":"Komşu dalda tek bir kişinin kötü bir sonuç beklerken duyduğu korku hali yeterlidir.","neighbor_ref":"root_000447/B001","relation_type":"near_neighbor","shared_zone":"İki dalın ortak alanı, kişide korkunun bulunmasıdır."},{"boundary_match":"field_only","distinction":"Daha çok korkmak, karşıdakini korkutmak değildir. Odak dal korkunun derecesini karşılaştırır; komşu dal korkunun nedenini ve ettirgen yönünü belirtir.","focus_only":"Odak dal, bir katılımcının ötekinden daha çok korkmasıyla sonuçlanan karşılaştırmayı anlatır.","gloss":"başkasını korkutma","neighbor_only":"Komşu dal, bir katılımcının ötekinde korku doğurmasını anlatır.","neighbor_ref":"root_000447/B002","relation_type":"same_field","shared_zone":"İki dalda da korku ve birden çok katılımcı vardır."},{"boundary_match":"partial","distinction":"İşlem yapısı benzer olsa da ölçü alanları ayrıdır: odak korku derecesini, komşu ağlama miktarını karşılaştırır ve birbirlerinin yerine kullanılamazlar.","focus_only":"Odak dalda karşılaştırılan ölçü korkunun şiddetidir.","gloss":"ağlamada ötekini geçme","neighbor_only":"Komşu dalda karşılaştırılan ölçü ağlamanın çokluğudur.","neighbor_ref":"root_000146/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal, karşılıklı bir eylemde bir katılımcının ötekini aynı ölçü bakımından geçmesini anlatır."},{"boundary_match":"partial","distinction":"Ortak karşılaştırma kalıbı anlamları eşitlemez; odak korku derecesine, komşu ise övünme ve değer iddiasına bağlıdır.","focus_only":"Odak dalda üstünlük, ötekinden daha çok korkmuş olmakla kurulur.","gloss":"övünmede üstün gelme","neighbor_only":"Komşu dalda üstünlük, övünme sırasında kendi değerini ve başarısını öne sürmekle kurulur.","neighbor_ref":"root_001135/B002","relation_type":"near_neighbor","shared_zone":"İki dal da karşılıklı bir yarışma ve sonunda bir tarafın üstün gelmesi yapısını taşır."},{"boundary_match":"partial","distinction":"Odak dal duygunun derecesini, komşu dal ise karşılık verme eylemindeki başarıyı ölçer; yalnızca karşılaştırmalı yapı ortaktır.","focus_only":"Odak dalın karşılaştırma alanı korkudur ve üstün gelen taraf daha çok korkandır.","gloss":"karşılık vermede üstün gelme","neighbor_only":"Komşu dalın karşılaştırma alanı karşılık verme ve yapılanı karşılamadır.","neighbor_ref":"root_000244/B005","relation_type":"near_neighbor","shared_zone":"Her iki dalda da karşılıklı bir eylem ve bir tarafın ötekini geçmesi bulunur."}],"source_phrase_ar":"خاوفه فخافه يخوفه غلبه بالخوف أي كان أشد خوفا منه (sihah)؛ خاوفني فلان فخفته أي كنت أشد خوفا منه (maqayis)","source_summary":"Tanıklıklar, karşılıklı eylemin sonucunu aynı biçimde açıklar: konuşan ya da belirtilen kişi, ötekinden daha çok korktuğu için korku derecesinde üstün gelir.","sources":["SI","MQ"],"what_is_ar":"خاوفه فخافه؛ أن يغلبه بالخوف أو يكون أحدهما أشد خوفا من الآخر","what_is_not_ar":"ليس التخويف والإخافة بمعنى جعل الغير يخاف؛ وليس أصل الخوف العام"},"support_links":[]},{"boundary":"Dal, korku duygusunu değil bir şeyin miktarından alarak azaltmayı anlatır; kullanım özel eylem biçimiyle sınırlıdır.","branch_kind":"non_bare","branch_ref":"root_000447/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَافَ","morph_features":"STEM|POS:V|IMPF|LEM:xaAfa|ROOT:xwf|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:15:2:1","qac_word_ref":"91:15:2","surface_ar":"يَخَافُ"}],"gloss":"bir şeyden alarak eksiltme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyden bir bölüm alınır ve böylece onun miktarı azaltılır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eksiltme, bir açıklamada korkunun gerektirdiği bir sonuç olarak ilişkilendirilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başka bir açıklama, sözcük biçimini eksiltme anlamındaki ayrı bir kökten ses değişmesiyle oluşmuş sayar."}}],"root_ar":"خ و ف","root_id":"root_000447","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli eylem biçiminin bir nesnenin veya miktarın bir bölümünü alıp azaltmayı anlattığı kullanımda geçerlidir.","boundary_detail":"Dal, korku duygusunu değil bir şeyin miktarından alarak azaltmayı anlatır; kullanım özel eylem biçimiyle sınırlıdır.","branch_image_ar":"نقص يأخذ من الشيء","concept_gloss":"bir şeyden alarak eksiltme","contextual_glosses":[{"applicability":"Eksiltmenin bir şeyden bölüm bölüm alma yoluyla gerçekleştiğini vurgulayan akıcı bağlamlarda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alma işlemini ve miktarın bu yolla azalmasını açıkça korur."},"facet_ids":["F001"],"text":"ala ala azaltma","usage_role":"contextual"},{"applicability":"Alınan bölümün kendisi açıkça belirtilmediğinde eksilme sonucunu öne çıkaran açıklamalarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Azalmanın o şeyden alma yoluyla gerçekleştiğini tek başına zorunlu kılmaz.","preserves":"Bir bütünün miktarının bir bölüm kadar azalmasını korur."},"facet_ids":["F001"],"text":"bir bölümünü eksiltme","usage_role":"explanatory"}],"definition":"Bir şeyden alarak onun miktarını eksiltmektir. Bir açıklama bu eksiltmeyi korkunun doğurduğu bir sonuçla ilişkilendirirken başka bir açıklama sözcük biçimini ses değişmesine dayanan ayrı bir oluşum sayar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyden bir bölüm alınır ve böylece onun miktarı azaltılır."},{"facet_id":"F002","role":"source_variant","statement":"Eksiltme, bir açıklamada korkunun gerektirdiği bir sonuç olarak ilişkilendirilir."},{"facet_id":"F003","role":"source_variant","statement":"Başka bir açıklama, sözcük biçimini eksiltme anlamındaki ayrı bir kökten ses değişmesiyle oluşmuş sayar."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Eylemi bir kişinin yaşadığı korku hali gibi gösterir.","collision":"Aynı kökün temel korku dalıyla karışır.","fit":"displacement","loses":"Bir şeyden alma ve onu eksiltme işlemini bütünüyle siler.","preserves":"Bir kaynak açıklamasındaki korkuyla ilişkilendirme yönünü korur."},"text":"korkma"},{"category":"confusable","error_profile":{"adds":"Şeyin tümüyle ortadan kaldırıldığı sonucunu ekler.","collision":"Tüketme veya bütünüyle ortadan kaldırma anlamıyla karışır.","fit":"displacement","loses":"Bir şeyden bölüm alarak eksiltme işleminin dereceli yapısını siler.","preserves":"Bir şeyin miktarında azalma ve kayıp meydana gelmesi yönünü korur."},"text":"yok etme"}],"identity_rationale":"Hazırlanan dal, kaynak ifadesindeki eylemi doğru verir: bir şeyden alarak onu eksiltmek. Kaynak içindeki iki açıklama da dalı bozmadan korunabilir; biri eksiltmeyi korkunun gerektirdiği bir sonuçla ilişkilendirir, öteki biçimi ses değişmesiyle ortaya çıkmış ayrı bir kullanım sayar.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bir şeyi eksiltip ondan bir bölüm almak"}],"lexicalization_note":"Anlam, belirli eylem biçiminin bir şeyi eksiltip ondan alma kullanımına bağlıdır; kökün yalın korku anlamına taşınmaz ve genel bir korku tanımı olarak sunulmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel azalma, kenarlardan eksiltme, haktan eksiltme, tüketme ve korkuyla kurulan açıklayıcı bağ en yararlı beş sınır olarak seçildi. Yalnızca kalan az miktarı veya başka özel azalma sonuçlarını adlandıran adaylar bu ayrımları tekrarladığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda eksilme bir şeyden alma işlemi olarak kurulur; komşu dal ise nedeni ve yöntemi belirlenmemiş genel azalmadır.","focus_only":"Odak dal, eksilmeyi bir şeyden alma eylemiyle ve özel bir sözcük biçimiyle anlatır.","gloss":"genel azalma","neighbor_only":"Komşu dal, miktar veya değerin herhangi bir yolla azalmasını genel olarak kapsar.","neighbor_ref":"root_000409/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin önceki miktarından daha aza inmesini anlatır."},{"boundary_match":"partial","distinction":"Komşu dal alma işlemini kenarlara bağlayan daha dar bir yöntem taşır; odak dalın çekirdeğinde böyle bir yer sınırı yoktur.","focus_only":"Odak dal, alınan bölümün şeyin hangi kısmından geldiğini zorunlu olarak belirtmez.","gloss":"kenarlardan eksiltme","neighbor_only":"Komşu dal, özellikle kenarlardan ve çevreden alarak eksiltmeyi anlatır.","neighbor_ref":"root_000380/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir şeyden bölüm alınır ve miktarı azaltılır."},{"boundary_match":"partial","distinction":"Odak dal genel alma ve eksiltme işlemidir; komşu dal ise özellikle hak kaybı ve gizli aşındırma çağrışımıyla daralabilir.","focus_only":"Odak dal, herhangi bir şeyden alarak eksiltmeyi anlatır ve gizli davranış koşulu koymaz.","gloss":"haktan gizlice eksiltme","neighbor_only":"Komşu dal, hakkı veya şeyi gizlice aşındırma ve ona bağlı güveni bozma yönünü taşıyabilir.","neighbor_ref":"root_000449/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin ya da hakkın miktarını azaltma alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal kısmi eksilmeyi kapsar; komşu dal ise süreci sonuna kadar götürüp şeyin tükenmesini veya elden çıkmasını anlatır.","focus_only":"Odak dal, bir şeyden bölüm alıp onu eksiltmekle tamamlanır; tümünün bitmesi gerekmez.","gloss":"alıp tüketme","neighbor_only":"Komşu dal, alma veya içme sonunda eldekinin tümüyle tükenmesini öne çıkarır.","neighbor_ref":"root_000528/B002","relation_type":"near_neighbor","shared_zone":"Her ikisinde de bir şeyden alma sonucunda miktar kaybı meydana gelir."},{"boundary_match":"thematic_only","distinction":"Bu açıklayıcı bağ, anlamları birleştirmez: odak dal nicelikte azalma eylemidir, komşu dal ise kişinin yaşadığı duygusal durumdur.","focus_only":"Odak dalın çekirdeği bir şeyden alıp onun miktarını azaltmaktır.","gloss":"korku hali","neighbor_only":"Komşu dalın çekirdeği kötü bir sonuç beklerken duyulan korkudur.","neighbor_ref":"root_000447/B001","relation_type":"thematic","shared_zone":"Bir açıklama, eksiltme olayını korkunun gerektirdiği bir sonuçla ilişkilendirir."}],"source_phrase_ar":"والتخوف التنقص (ayn)؛ وتخوفه أي تنقصه (sihah)؛ تخوفناهم أي تنقصناهم تنقصا اقتضاه الخوف منه (mufradat)؛ تخوفت الشيء أي تنقصته فهو الصحيح الفصيح إلا أنه من الإبدال والأصل النون من التنقص (maqayis)","source_summary":"Tanıklıklar bir şeyden alıp onu eksiltme anlamında birleşir. Ayrışan açıklamalardan biri eksiltmeyi korkunun yol açtığı bir sonuç sayarken diğeri aynı biçimi ses değişmesiyle açıklanan ayrı bir kökene bağlar.","sources":["AY","SI","MU","MQ"],"what_is_ar":"تخوف الشيء بمعنى تنقصه وأخذ منه؛ تنقصا اقتضاه الخوف منه عند من يربطه بالخوف؛ الفرع الإبدالي المذكور في المصادر","what_is_not_ar":"ليس توقع المكروه نفسه؛ وليس ظهور الخوف من الإنسان عند مفردات الراغب"},"support_links":[]},{"boundary":"Dal, korkunun kişide belli olmasına özgüdür; bir şeyi eksiltme ve başkasını korkutma anlamları bu kullanıma girmez.","branch_kind":"bare","branch_ref":"root_000447/B005","candidate_links":[{"candidate_id":"cand_bd93f051dfdb269fd8d0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَافَ","morph_features":"STEM|POS:V|IMPF|LEM:xaAfa|ROOT:xwf|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:15:2:1","qac_word_ref":"91:15:2","surface_ar":"يَخَافُ"}],"gloss":"korkunun kişide dışa vurması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Korku, kişide dışarıdan fark edilir biçimde belirir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Anlam, korkunun yalnızca içte bulunmasını değil kişiden görünür hale gelmesini gösterir."}}],"root_ar":"خ و ف","root_id":"root_000447","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin korktuğunun dışarıdan anlaşılır hale geldiğini anlatan dar ve bağımsız kullanımda geçerlidir.","boundary_detail":"Dal, korkunun kişide belli olmasına özgüdür; bir şeyi eksiltme ve başkasını korkutma anlamları bu kullanıma girmez.","branch_image_ar":"ظهور الخوف على الإنسان","concept_gloss":"korkunun kişide dışa vurması","contextual_glosses":[{"applicability":"Bir kişinin korktuğunun görünüşünden veya genel halinden anlaşıldığı akıcı bağlamlarda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Korkunun kişide görünür ve anlaşılır hale gelmesini doğal Türkçeyle korur."},"facet_ids":["F001","F002"],"text":"korkusunun belli olması","usage_role":"general"},{"applicability":"Anlatımın kişinin dışarıdan nasıl göründüğüne odaklandığı bağlamlarda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Görünüş dışındaki davranış veya genel hal üzerinden belli olma olasılığını daraltır.","preserves":"Korkunun dışarıdan fark edilen görünüşünü korur."},"facet_ids":["F001"],"text":"korkmuş görünme","usage_role":"contextual"}],"definition":"Korkunun kişide dışarıdan fark edilir biçimde belirmesi, yani kişinin korktuğunun görünür hale gelmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Korku, kişide dışarıdan fark edilir biçimde belirir."},{"facet_id":"F002","role":"core","statement":"Anlam, korkunun yalnızca içte bulunmasını değil kişiden görünür hale gelmesini gösterir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Aynı kökün genel korku dalıyla karışır.","fit":"narrowing","loses":"Bu duygunun kişiden görünür hale gelmesi aşamasını belirtmez.","preserves":"Kişide bulunan temel duyguyu korur."},"text":"korku"},{"category":"confusable","error_profile":{"adds":"Başka bir kişinin korkuyu meydana getirdiği ettirgen bir eylem ekler.","collision":"Aynı kökün başkasında korku doğurma dalıyla karışır.","fit":"displacement","loses":"Korkunun onu yaşayan kişide görünür hale gelmesini siler.","preserves":"Korku olayının varlığını korur."},"text":"korkutma"}],"identity_rationale":"Hazırlanan dal, tek kaynak ifadesindeki dar anlamı doğrudan karşılar: korku yalnızca kişinin içinde bulunmaz, kişiden görünür biçimde dışa vurur. Bu, korkunun adıyla aynı şey değildir; duygunun görünme aşamasını anlatır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"korkunun kişide dışa vurması"}],"lexicalization_note":"Dal, verilen sözcük biçiminin bağımsız olarak korkunun kişide görünmesini anlatan yalın kullanımına dayanır; herhangi bir söz öbeğinden yeni bir anlam çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; iç korku, genel görünme, açığa çıkma, şaşkınlık ve korkutma ile kurulan sınırlar seçildi. Aynı genel görünürlük ayrımını tekrarlayan veya yalnızca başka bir duygunun dış belirtisini çağrıştıran adaylar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal duygunun dışarıdan fark edilmesini zorunlu kılar; komşu dal için korkunun yaşanması yeterlidir ve görünürlük şart değildir.","focus_only":"Odak dal, korkunun kişiden dışarıya yansıyarak görünür hale gelmesini anlatır.","gloss":"içte yaşanan korku","neighbor_only":"Komşu dal, görünür olsun ya da olmasın, kötü bir sonuç bekleyen kişinin iç korkusunu anlatır.","neighbor_ref":"root_000447/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da aynı korku duygusu kişide bulunur."},{"boundary_match":"partial","distinction":"Komşu dal genel görünme ve gösterme eylemidir; odak dal ise korku duygusunun kişide belirmesine bağlı dar bir kullanım taşır.","focus_only":"Odak dal yalnızca korkunun bir kişide görünür hale gelmesini anlatır.","gloss":"genel görünür hale gelme","neighbor_only":"Komşu dal herhangi bir şeyin gizlilikten çıkıp görünmesini ve başkasınca görünür kılınmasını kapsar.","neighbor_ref":"root_000097/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da daha önce görünmeyen bir durumun dışarıdan fark edilir olması vardır."},{"boundary_match":"partial","distinction":"Odak dal belirli bir duygunun kişide belirmesidir; komşu dal ise her türlü bilginin veya olayın açıklık kazanmasına uzanan daha geniş bir görünürlük alanıdır.","focus_only":"Odak dal, korkunun kişinin hali üzerinden kendiliğinden belli olmasını yeterli görür.","gloss":"açığa çıkma ve açıklama","neighbor_only":"Komşu dal, bir şeyin açığa çıkmasını, yayılmasını veya başkasına açıkça bildirilmesini kapsar.","neighbor_ref":"root_001041/B001","relation_type":"near_neighbor","shared_zone":"Her ikisi de gizli ya da içte olan bir şeyin görünür veya bilinir hale gelmesiyle ilgilidir."},{"boundary_match":"field_only","distinction":"Odak dalın zorunlu içeriği görünür korkudur; komşu dalın çekirdeği ise düşünme ve yönelme gücünü bozan şaşkınlıktır.","focus_only":"Odak dal, kişinin korkusunun dışarıdan anlaşılır hale gelmesini anlatır.","gloss":"şaşkınlık ve afallama","neighbor_only":"Komşu dal, kişinin şaşkınlık, afallama ve ne yapacağını bilememe durumunu anlatır.","neighbor_ref":"root_000086/B008","relation_type":"same_field","shared_zone":"Korku ve şaşkınlık aynı olayda kişinin halinde birlikte görülebilir."},{"boundary_match":"field_only","distinction":"Neden ile görünür sonuç ayrıdır: komşu dal korkuyu doğurur, odak dal ise doğmuş korkunun kişide belli olmasını anlatır.","focus_only":"Odak dal, korkunun onu yaşayan kişide görünür hale geldiği sonuç aşamasıdır.","gloss":"korku doğurma","neighbor_only":"Komşu dal, korkuyu meydana getiren kişi, şey veya eylemi anlatır.","neighbor_ref":"root_000447/B002","relation_type":"same_field","shared_zone":"Bir korkutma olayı, korkunun kişide görünür hale gelmesine yol açabilir."}],"source_phrase_ar":"والتخوف ظهور الخوف من الإنسان (mufradat)","source_qualifications":[{"kind":"sole_attestation","summary":"Korkunun kişide görünür hale gelmesini bağımsız bir anlam olarak tanıklar."}],"source_summary":"Kaynaklar arasında ortaklaştırılacak ayrı anlatımlar yoktur; dal, tek tanıklığın belirlediği dar görünürlük anlamını korur.","sources":["MU"],"what_is_ar":"التخوف عند الراغب بمعنى ظهور الخوف من الإنسان؛ حالة ظاهرة لا مجرد تسمية الخوف","what_is_not_ar":"ليس تخوفه بمعنى تنقصه؛ وليس التخويف بمعنى جعل الغير يخاف"},"support_links":["sup_e7226e38b3b6f183e86f"]},{"boundary":"Dal korku anlamına değil mesleki bir deri eşyaya aittir; üstlük ve torba seçenekleri tek nesneymiş gibi daraltılmamalıdır.","branch_kind":"bare","branch_ref":"root_000447/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَافَ","morph_features":"STEM|POS:V|IMPF|LEM:xaAfa|ROOT:xwf|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:15:2:1","qac_word_ref":"91:15:2","surface_ar":"يَخَافُ"}],"gloss":"arıcı ya da su taşıyıcısının deri torbası veya üstlüğü","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Arıcı veya su taşıyıcısı tarafından kullanılan mesleki bir eşyadır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eşya, giyilen bir üstlük ya da taşınan bir deri torba ve kap olarak açıklanır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Deri torba biçimi, arıcının bal toplama işinde kullandığı araç olarak özelleşir."}}],"root_ar":"خ و ف","root_id":"root_000447","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesnenin kaynaklardaki üstlük ve taşıma kabı seçeneklerini daraltmadan birlikte göstermek gereken sözlük açıklamasında kullanılır.","boundary_detail":"Dal korku anlamına değil mesleki bir deri eşyaya aittir; üstlük ve torba seçenekleri tek nesneymiş gibi daraltılmamalıdır.","branch_image_ar":"خافة العسال والسقاء","concept_gloss":"arıcı ya da su taşıyıcısının deri torbası veya üstlüğü","contextual_glosses":[{"applicability":"Nesnenin arıcının bal toplarken kullandığı deri torba olduğu açık bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Su taşıyıcısının eşyasını ve giyilen üstlük açıklamasını dışarıda bırakır.","preserves":"Arıcılık işlevini ve bal toplamada kullanılan taşıma kabını korur."},"facet_ids":["F001","F003"],"text":"bal toplama torbası","usage_role":"contextual"},{"applicability":"Eşyanın torba veya kap biçiminin öne çıktığı, fakat taşıdığı şeyin belirtilmediği açıklayıcı bağlamlarda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Giyilen üstlük seçeneğini ve arıcılık ile su taşıma işlevlerini tek başına belirtmez.","preserves":"Deri bir kap ve taşıma aracı olma yönünü korur."},"facet_ids":["F001","F002"],"text":"deri taşıma torbası","usage_role":"explanatory"}],"definition":"Arıcının ya da su taşıyıcısının giydiği üstlük veya taşıdığı deri torba ve kaptır. Arıcının bal toplarken kullandığı deri torba, bu eşyanın özellikle belirtilen kullanımlarındandır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Arıcı veya su taşıyıcısı tarafından kullanılan mesleki bir eşyadır."},{"facet_id":"F002","role":"source_variant","statement":"Eşya, giyilen bir üstlük ya da taşınan bir deri torba ve kap olarak açıklanır."},{"facet_id":"F003","role":"specialization","statement":"Deri torba biçimi, arıcının bal toplama işinde kullandığı araç olarak özelleşir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kabın özellikle sıvı taşımaya yaradığı ve belirli bir torba biçiminde olduğu sınırını ekler.","collision":"Yalnızca su taşımaya ayrılmış deri kap adıyla karışır.","fit":"displacement","loses":"Arıcılık kullanımını, bal toplama torbasını ve giyilen üstlük seçeneğini dışarıda bırakır.","preserves":"Deri kap ve su taşıyıcısı bağlamını kısmen korur."},"text":"su tulumu"},{"category":"confusable","error_profile":{"adds":"Büyük, kaba dokumadan yapılmış genel yük torbası izlenimini ekler.","collision":"Tahıl veya yük taşımaya yarayan büyük torba anlamıyla karışır.","fit":"displacement","loses":"Deri malzemeyi, mesleki kullanımı ve giyilen üstlük seçeneğini siler.","preserves":"Taşımaya yarayan bir kap olma yönünü çok genel biçimde korur."},"text":"çuval"}],"identity_rationale":"Hazırlanan dalın meslek ve eşya alanı doğrudur, ancak kaynak ifadesi tek biçimli bir nesne tanımlamaz. Tanıklıklar arıcı veya su taşıyıcısının giydiği bir üstlük ile taşıdığı deri torba ya da kabı yan yana verir; bal toplamada kullanılan deri torba da bu alanın özel bir görünümüdür.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"arıcı veya su taşıyıcısının deri torbası, kabı ya da üstlüğü"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"aynı eşyanın küçük biçimi"}],"lexicalization_note":"Eşya adı bağımsız bir sözcük biçimi olarak tanımlanır; arıcı ve su taşıyıcısı bağlamları kullanım alanını açıklar, bunlardan kökün genel korku anlamına geçiş yapılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bal kabı, küçük sıvı kabı, azık torbası, deri sadak ve büyük deri hazırlama kabı nesnenin sınırını en iyi gösteren beş karşılaştırma olarak seçildi. Diğer torba ve araç adayları bu işlev ayrımlarını yinelediği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal mesleki eşya olarak üstlük seçeneğine ve daha genel torba kullanımına açıktır; komşu dal ise büyüklüğü belirtilen bal kaplarına özgüdür.","focus_only":"Odak dal, arıcı veya su taşıyıcısının üstlüğünü ya da deri torbasını kapsar.","gloss":"bal için büyük deri kap","neighbor_only":"Komşu dal, özellikle bal için kullanılan büyük deri kapları ve bunların çoğul sınıfını anlatır.","neighbor_ref":"root_001625/B009","relation_type":"near_neighbor","shared_zone":"İki dal da balın toplanması veya taşınmasıyla ilişkili deri kapları kapsayabilir."},{"boundary_match":"partial","distinction":"Komşu dal sıvı kabı ve küçük boyutla sınırlıdır; odak dalın meslek alanı ve nesne türleri daha farklıdır, ayrıca üstlük olarak da açıklanabilir.","focus_only":"Odak dal, arıcılıkta kullanılan torbayı ve giyilen üstlük seçeneğini de kapsar.","gloss":"küçük deri sıvı kabı","neighbor_only":"Komşu dal, su veya süt koymaya yarayan küçük deri kabı özel olarak anlatır.","neighbor_ref":"root_000814/B004","relation_type":"near_neighbor","shared_zone":"Her iki dalda da taşıma amacıyla kullanılan deri bir kap bulunabilir."},{"boundary_match":"field_only","distinction":"Odak dal mesleğe ve deri malzemeye bağlıdır; komşu dal ise içeriği yiyecek olan genel bir taşıma kabıdır.","focus_only":"Odak dal, arıcı veya su taşıyıcısının deri eşyasını ve bal toplama aracını anlatır.","gloss":"azık torbası","neighbor_only":"Komşu dal, yolculukta veya gündelik kullanımda yiyecek koymaya yarayan azık torbasını anlatır.","neighbor_ref":"root_000653/B002","relation_type":"same_field","shared_zone":"İki dal da kişinin yanında taşıdığı bir torba veya kap türünü adlandırır."},{"boundary_match":"field_only","distinction":"İşlevleri ayrıdır: odak dal arıcılık ve su taşıma çevresindedir; komşu dal öncelikle okları veya başka yükleri taşımaya yarar.","focus_only":"Odak dal, bal toplama veya su taşıma işinde kullanılan torba ya da üstlüktür.","gloss":"deri sadak veya torba","neighbor_only":"Komşu dal, ok taşımaya yarayan deri sadak veya yiyecek taşınabilen ayrı bir kap türüdür.","neighbor_ref":"root_001667/B003","relation_type":"same_field","shared_zone":"Her iki dal deri malzemeden yapılmış taşıma kapları alanında yer alır."},{"boundary_match":"field_only","distinction":"Odak dal taşınan ya da giyilen kişisel meslek eşyasıdır; komşu dal ise yerde duran, ayaklı ve hazırlama işlevli büyük bir kaptır.","focus_only":"Odak dal, kişinin giyebildiği veya yanında taşıyabildiği mesleki bir eşyadır.","gloss":"büyük deri hazırlama kabı","neighbor_only":"Komşu dal, ayakları bulunan ve içinde içecek hazırlanan büyük deri bir tekne biçimindedir.","neighbor_ref":"root_000799/B006","relation_type":"same_field","shared_zone":"İki dal deri malzemeden yapılan kap veya donanım alanını paylaşır."}],"source_phrase_ar":"الخافة تصغيرها خويفة واشتقاقها من الخوف وهي جبة يلبسها العسال والسقاء والخافة العيبة (ayn)؛ الخافة خريطة من أدم يشتار فيها العسل (sihah)","source_summary":"Tanıklıklar sözcüğü arıcı ve su taşıyıcısı çevresinde kullanılan bir eşya olarak birleştirir. Anlatımlardan biri giyilen üstlüğü ve taşıma kabını birlikte verirken diğeri bal toplamada kullanılan deri torbayı öne çıkarır.","sources":["AY","SI"],"what_is_ar":"الخافة: جبة أو عيبة يلبسها أو يحملها العسال والسقاء؛ خريطة من أدم يشتار فيها العسل","what_is_not_ar":"ليس الخوف الحالة النفسية؛ وليس التخويف والإخافة؛ وليس الخيفة بمعنى الخوف"},"support_links":[]},{"boundary":"Dal, çıplak topuk anlamını değil, malzeme olan sinir dokusunu ve ona bağlı kullanımları kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُقْبَى","morph_features":"STEM|POS:N|LEM:EuqobaY|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:15:3:1","qac_word_ref":"91:15:3","surface_ar":"عُقْبَٰ"}],"gloss":"bağlama ve kiriş yapımında kullanılan sert beyaz tendon","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Beyaz, sert ve dayanıklı sinir ya da tendon dokusu kiriş yapımında kullanılan temel malzemedir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayak bileklerinin arkasındaki gergin tendon, aynı doku adının anatomik bir özelleşmesidir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ok, yay, mızrak ve benzeri araçlar bu dokuyla sarılarak sağlamlaştırılır."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın temel malzemesini ve bu malzemenin başlıca işlevini birlikte karşılar.","boundary_detail":"Dal, çıplak topuk anlamını değil, malzeme olan sinir dokusunu ve ona bağlı kullanımları kapsar.","branch_image_ar":"العَقَب الأبيض الشديد","concept_gloss":"bağlama ve kiriş yapımında kullanılan sert beyaz tendon","contextual_glosses":[{"applicability":"Ok, yay, mızrak veya benzeri bir aracın bu malzemeyle bağlandığı yapılarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tendon malzemesini, sarma işlemini ve sağlamlaştırma sonucunu korur."},"facet_ids":["F003"],"text":"tendonla sarıp sağlamlaştırmak","usage_role":"contextual"}],"definition":"Kiriş yapımında ve araçları sarıp sağlamlaştırmada kullanılan beyaz, sert ve dayanıklı sinir ya da tendon dokusudur; ayak bileklerinin arkasındaki gergin tendon da buna bağlı bir anatomik kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Beyaz, sert ve dayanıklı sinir ya da tendon dokusu kiriş yapımında kullanılan temel malzemedir."},{"facet_id":"F002","role":"specialization","statement":"Ayak bileklerinin arkasındaki gergin tendon, aynı doku adının anatomik bir özelleşmesidir."},{"facet_id":"F003","role":"associated_use","statement":"Ok, yay, mızrak ve benzeri araçlar bu dokuyla sarılarak sağlamlaştırılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Dalın merkezinde bulunmayan çıplak ayak arkası anlamını ekler.","collision":"Aynı kökün ayak arkasını anlatan ayrı dalıyla karışır.","fit":"displacement","loses":"Sert tendon dokusunu ve bu dokunun malzeme olarak kullanımını yitirir.","preserves":"Ayak bölgesiyle dolaylı anatomik yakınlığı korur."},"text":"topuk"}],"identity_rationale":"Kaynak ifadesi, kiriş yapılan sert beyaz sinir dokusunu, ayak bileği arkasındaki gergin uzantısını ve bu dokuyla araçları sarıp sağlamlaştırma işini birlikte destekler.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kiriş yapılan sert beyaz tendon"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ayak bileklerinin arkasındaki gergin tendon"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"oku, yayı ya da mızrağı tendonla sarıp sağlamlaştırmak"}],"lexicalization_note":"Tanım, dokunun yalın adını anatomik uzantısından ve araçları bu dokuyla sarma yapısından ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yakın sınır karşılaştırması belirli sırt tendonu dalıdır, öteki adaylar yalnız araç, ip veya aynı kökün uzak anlamlarını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu, belirli bir anatomik kaynağa ve kiriş üretimine daralır; odak dalı daha geniş tendon malzemesini ve bağlama kullanımını içerir.","focus_only":"Bu dal, genel sert tendon malzemesini ve onunla araç sarma işini de kapsar.","gloss":"yay kirişi yapılan sırt tendonu","neighbor_only":"Komşu dal, özellikle sırtın iki yanından çıkarılıp yay kirişi yapılan belirli tendon parçalarını anlatır.","neighbor_ref":"root_000698/B008","relation_type":"near_synonym","shared_zone":"İki dal da hayvansal tendonun işlenip yay kirişi yapılmasını kapsar."}],"source_phrase_ar":"العقب العصب الذي تعمل منه الأوتار (ayn); عقب الإنسان والدابة معروف في معنى العصب (jamhara); العقب بالتحريك العصب الذي تعمل منه الأوتار (sihah); عقبت الخوق وعقبت القدح بالعقب (tahdhib); العقب ما يقعب به الرماح والسهام وهو أصلبهما وأمتنهما (maqayis); عقبت الرمح شددته بالعقب (mufradat); العرقوب عقب موتر خلف الكعبين والراء زائدة (maqayis-variant)","source_summary":"Kaynaklar sert sinir dokusunu hem kiriş malzemesi hem de ok, yay ve mızrak gibi araçları bağlayıp güçlendiren malzeme olarak verir; bir biçim çeşidi ayak bileği arkasındaki gergin tendonu gösterir.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"العَقَب بمعنى العصب أو الوتر الأبيض الصلب الذي تعمل منه الأوتار وتشد به السهام والقداح والرماح والقسي وحلقة القرط، وما اتصل به من العرقوب الموتر خلف الكعبين","what_is_not_ar":"ليس مؤخر القدم المجرد ولا العاقبة ولا العقوبة"},"support_links":[]},{"boundary":"Dal, zaman içindeki genel ardışıklığı değil, ayak arkasından gelişen uzamsal iz ve takip ilişkisini kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُقْبَى","morph_features":"STEM|POS:N|LEM:EuqobaY|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:15:3:1","qac_word_ref":"91:15:3","surface_ar":"عُقْبَٰ"}],"gloss":"topuk ve hemen arkasında kalan iz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim ayağın arka bölümü, yani topuktur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayak arkasındaki yer ve iz, birinin hemen ardından gelme ilişkisine genişler."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişinin ardınca çok kimsenin yürümesi, onun çok sayıda izleyeni olduğunu anlatır."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Anatomik çekirdeği ve ondan doğan uzamsal art alanı birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Dal, zaman içindeki genel ardışıklığı değil, ayak arkasından gelişen uzamsal iz ve takip ilişkisini kapsar.","branch_image_ar":"مؤخر القدم والأثر","concept_gloss":"topuk ve hemen arkasında kalan iz","contextual_glosses":[{"applicability":"Bir kişinin gittiği yolun veya yaptığı hareketin doğrudan arkasından gelme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önceki kişinin izine ve arkasındaki yakın konuma bağlı takip ilişkisini korur."},"facet_ids":["F002"],"text":"hemen ardından","usage_role":"contextual"}],"definition":"Ayağın arka bölümü ve bu bölümün gerisinde kalan yer ya da izdir; buna bağlı yapılar birinin hemen ardından gelmeyi veya çok sayıda kişi tarafından izlenmeyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim ayağın arka bölümü, yani topuktur."},{"facet_id":"F002","role":"extension","statement":"Ayak arkasındaki yer ve iz, birinin hemen ardından gelme ilişkisine genişler."},{"facet_id":"F003","role":"associated_use","statement":"Bir kişinin ardınca çok kimsenin yürümesi, onun çok sayıda izleyeni olduğunu anlatır."}],"identity_rationale":"Kaynak ifadesi ayağın arka bölümünü temel alır ve buradan kişinin hemen arkasındaki iz, yer ve izleyenler için kurulan kullanımlara geçer.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"topuk, ayağın arka bölümü"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"topuklar"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"ardınca çok kişi yürüyen, çok izlenen"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birinin hemen ardından, onun izinden"}],"lexicalization_note":"Yalın anatomik anlam, çoğul biçim, çok izleneni anlatan söz ve birinin hemen ardını belirten yapı ayrı gösterilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; izden gitme dalı en yararlı karşılaştırmadır, ötekiler yalnız yürüyüş, ayak konumu veya geniş uzam özellikleri paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı anatomik ve uzamsal bir adlandırmadan takip ilişkisine geçer; komşu dalın çekirdeği ise iz sürerek ilerleme eylemidir.","focus_only":"Odak dalında ayağın arka bölümü ve onun gerisindeki yer temel anlamdır.","gloss":"öncekinin izinden gitmek","neighbor_only":"Komşu dal, öncekinin izini izleyerek yol alma eylemini doğrudan anlatır.","neighbor_ref":"root_000011/B004","relation_type":"near_neighbor","shared_zone":"İki dal da bir kişinin ardından onun bıraktığı izi izlemeyi kapsar."}],"source_phrase_ar":"العقب مؤخر القدم (ayn); عقب الإنسان معروف يحرك ويسكن (jamhara); العقب بكسر القاف مؤخر القدم (sihah); عقب القدم مؤخرها وجمعه أعقاب (tahdhib); العقب مؤخر الرجل وجمعه أعقاب (mufradat); من الباب عقب القدم مؤخرها (maqayis); موطأ العقب أي كثير الأتباع (maqayis)","source_summary":"Kaynaklar ayağın arka bölümünde birleşir; aynı görüntü, birinin ardındaki izi ve yeri, hemen ardından gelmeyi ve çok izleyeni olmayı anlatan yapılara temel olur.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"العقب بمعنى مؤخر القدم وما خلف الإنسان أو القوم من أثر وموضع يتبع، ومنه وطء العقب وكون الإنسان موطأ العقب","what_is_not_ar":"ليس التعاقب الزمني ولا العقبى ولا الطائر"},"support_links":[]},{"boundary":"Bu anlam yalnız belirtilen dönüş ve olumsuz dönüş yapılarında geçerlidir; yalın ayak arkası anlamına genişletilmez.","branch_kind":"collocation","branch_ref":"root_001033/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُقْبَى","morph_features":"STEM|POS:N|LEM:EuqobaY|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:15:3:1","qac_word_ref":"91:15:3","surface_ar":"عُقْبَٰ"}],"gloss":"dönüp geri çekilmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İleri gidişten sonra yön değiştirip geri çekilme hareketi anlatılır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Olumsuz yapı, uzaklaşanın dönmemesini, arkasına bakmamasını veya beklememesini belirtir."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İleri hareketten sonra yönünü tersine çeviren kişi için kullanılan yapıyı doğal biçimde karşılar.","boundary_detail":"Bu anlam yalnız belirtilen dönüş ve olumsuz dönüş yapılarında geçerlidir; yalın ayak arkası anlamına genişletilmez.","branch_image_ar":"الرجوع على العقب","concept_gloss":"dönüp geri çekilmek","contextual_glosses":[{"applicability":"Geri dönme, arkaya bakma veya bekleme eylemlerinin olumsuzlandığı kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uzaklaşmayı ve geriye yönelmenin gerçekleşmemesini açık biçimde korur."},"facet_ids":["F002"],"text":"arkasına bakmadan uzaklaşmak","usage_role":"contextual"}],"definition":"İleri yönelmişken dönüp geri çekilmek veya geldiği yöne dönmektir; olumsuz yapıda ise uzaklaşırken geri dönmemek, arkaya bakmamak ya da beklememektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İleri gidişten sonra yön değiştirip geri çekilme hareketi anlatılır."},{"facet_id":"F002","role":"associated_use","statement":"Olumsuz yapı, uzaklaşanın dönmemesini, arkasına bakmamasını veya beklememesini belirtir."}],"identity_rationale":"Kaynak ifadesi, ileri gidişten sonra dönüp geri çekilmeyi ve olumsuz yapıda geriye dönmemeyi, bakmamayı ya da beklememeyi açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"dönüp geri çekilmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"geri dönmedi, arkasına bakmadı veya beklemedi"}],"lexicalization_note":"Tanım bütünüyle geri dönme ve dönmeden uzaklaşma kalıplarına bağlıdır; yalın kök anlamı ileri sürülmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sırt çevirip uzaklaşma dalı en yakın sınırı verir, diğerleri genel dönüş, sapma veya arkadan alma eylemleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı belirli geri dönüş kalıplarıyla sınırlıdır; komşu dal fiziksel dönüşün yanında soyut yüz çevirme ve yenilgiyi de içerir.","focus_only":"Odak dalı, ilerledikten sonra geldiği yöne fiziksel olarak dönüp çekilmeyi öne çıkarır.","gloss":"dönüp uzaklaşma","neighbor_only":"Komşu dal, savaşta sırt çevirme, sözden yüz çevirme ve yenilgi gibi daha geniş uzaklaşmaları kapsar.","neighbor_ref":"root_000458/B003","relation_type":"near_synonym","shared_zone":"İki dal da ileri yönelişi bırakıp ters yöne dönmeyi anlatabilir."}],"source_phrase_ar":"ولى فلان على عقبه وعقبيه أي انثنى راجعا (ayn); ولى مدبرا ولم يعقب أي لم يعطف ولم ينتظر (sihah); كل راجع معقب ولم يلتفت ولم يرجع (tahdhib); رجع على عقبه وانقلب على عقبيه (mufradat); ولي مدبرا ولم يعقب أي لم يعطف (maqayis)","source_summary":"Kaynaklar, kişinin geldiği yöne dönüp çekilmesinde ve olumsuz biçimde dönmeden, bakmadan veya beklemeden uzaklaşmasında birleşir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"الرجوع والانثناء والنكوص بعد الإقبال، ومنه ولى على عقبه أو عقبيه، ولم يعقب بمعنى لم يعطف أو لم يرجع أو لم يلتفت","what_is_not_ar":"ليس مجرد مؤخر القدم ولا التعاقب الدوري ولا طلب الحق بعده"},"support_links":[]},{"boundary":"Dal genel sonu veya sonucu değil, bir kişinin kendisinden sonra süren doğrudan soyunu anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُقْبَى","morph_features":"STEM|POS:N|LEM:EuqobaY|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:15:3:1","qac_word_ref":"91:15:3","surface_ar":"عُقْبَٰ"}],"gloss":"ardında kalan çocuklar ve torunlar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin kendisinden sonra kalan çocukları ve torunları sürmekte olan soyunu oluşturur."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Olumsuz kalıp, kişinin ardında çocuk veya devam eden bir soy bırakmadığını belirtir."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin ölümünden veya ayrılışından sonra soyunu sürdüren alt kuşakları birlikte anlatır.","boundary_detail":"Dal genel sonu veya sonucu değil, bir kişinin kendisinden sonra süren doğrudan soyunu anlatır.","branch_image_ar":"العَقِب من الولد","concept_gloss":"ardında kalan çocuklar ve torunlar","contextual_glosses":[{"applicability":"Bir kişinin kendisinden sonra yaşayan çocuk veya devam eden soy bırakmadığı durumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Soyun devam etmemesini ve kişinin ardında alt kuşak kalmamasını korur."},"facet_ids":["F002"],"text":"ardında soy bırakmadı","usage_role":"contextual"}],"definition":"Bir kişinin ardından kalan çocukları ve çocuklarının çocukları, yani sürmekte olan soyudur; olumsuz kullanım kişinin ardında çocuk veya soy bırakmadığını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin kendisinden sonra kalan çocukları ve torunları sürmekte olan soyunu oluşturur."},{"facet_id":"F002","role":"associated_use","statement":"Olumsuz kalıp, kişinin ardında çocuk veya devam eden bir soy bırakmadığını belirtir."}],"identity_rationale":"Kaynak ifadesi, kişinin ardından kalan çocuklarını ve torunlarını açıkça tanımlar; soy bırakmama kalıbı da aynı sınırın olumsuzunu verir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kişinin ardından kalan çocukları ve torunları"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ardında çocuk veya soy bırakmadı"}],"lexicalization_note":"Soy adı ile soy kalmadığını bildiren olumsuz kalıp ayrılır; anlam genel bir sonralık kavramına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel çocuk ve soy dalı en yakın karşılıktır, ötekiler soyun kesilmesi, hane halkı veya özel akrabalık türleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında atadan sonra kalma ilişkisi kurucudur; komşu dalda ise genel çocuk ve üreme bağı yeterlidir.","focus_only":"Odak dalı, özellikle bir kişiden sonra kalan ve onun soyunu sürdüren alt kuşakları anlatır.","gloss":"çocuklar ve süren soy","neighbor_only":"Komşu dal, çocuk ve soy kavramını genel üreme ve nesil üretme ilişkisi içinde ele alır.","neighbor_ref":"root_001499/B001","relation_type":"near_synonym","shared_zone":"İki dal da çocukları, torunları ve neslin devamını kapsar."}],"source_phrase_ar":"عقب الرجل ولده وولد ولده الباقون من بعده (ayn); ليست لفلان عاقبة أي ولد وعقب الرجل ولده وولد ولده (sihah); قيل لولد الرجل عقبه وكذلك آخر كل شيء عقبه (tahdhib); استعير العقب للولد وولد الولد وفلان لم يعقب (mufradat); ليس لفلان عاقبة يعني عقبا (maqayis)","source_summary":"Kaynaklar anlamı kişinin ardından kalan çocuklar ve torunlarda birleştirir; soy bırakmama anlatımı bu kavramın olumsuz sınırını gösterir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"ولد الرجل وولد ولده ومن يبقى بعده من نسله، وما ينفى بقولهم لا عقب له، والذرية الباقية في عقب الإنسان","what_is_not_ar":"ليس العاقبة العامة ولا العقبى الجزاء ولا مجرد آخر الشيء"},"support_links":[]},{"boundary":"Dal, tek başına geri dönüşü veya nihai sonucu değil, sonradan gelme, yerini alma ve sıra değişimini kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُقْبَى","morph_features":"STEM|POS:N|LEM:EuqobaY|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:15:3:1","qac_word_ref":"91:15:3","surface_ar":"عُقْبَٰ"}],"gloss":"birbirinin ardından gelme ve yerini alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sonraki öğe öncekinin ardından gelir ve onun bıraktığı yeri alır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İki taraflı düzende öğeler sırayla birbirinin yerini alarak dönüşümlü ilerler."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gece ile gündüzün, görevli toplulukların veya binicilerin sıra değişimi bu düzeni örnekler."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem tek yönlü ardıllığı hem de iki tarafın dönüşümlü biçimde yer değiştirmesini kapsar.","boundary_detail":"Dal, tek başına geri dönüşü veya nihai sonucu değil, sonradan gelme, yerini alma ve sıra değişimini kapsar.","branch_image_ar":"الخلف والتعاقب","concept_gloss":"birbirinin ardından gelme ve yerini alma","contextual_glosses":[{"applicability":"Gece ile gündüz veya iki görevli gibi tarafların dönüşümlü geldiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dönüşümlü sırayı ve her tarafın ötekinin ardından gelip yerini almasını korur."},"facet_ids":["F002","F003"],"text":"sırayla birbirinin yerini almak","usage_role":"contextual"}],"definition":"Bir şeyin başka bir şeyden sonra gelmesi ve onun yerini almasıdır; karşılıklı düzenlerde taraflar sırayla birbirinin ardından gelir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sonraki öğe öncekinin ardından gelir ve onun bıraktığı yeri alır."},{"facet_id":"F002","role":"specialization","statement":"İki taraflı düzende öğeler sırayla birbirinin yerini alarak dönüşümlü ilerler."},{"facet_id":"F003","role":"example","statement":"Gece ile gündüzün, görevli toplulukların veya binicilerin sıra değişimi bu düzeni örnekler."}],"identity_rationale":"Kaynak ifadesi bir şeyin diğerinden sonra gelmesini, onun yerini almasını ve iki tarafın sırayla birbirini izlemesini ortak bir ardıllık çekirdeğinde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"öncekinin ardından gelen ve onun yerini alan"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ardıl, bir başkasının ardından gelen"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"gece ile gündüzün sırayla birbirinin yerini alması"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"sırayla nöbet değiştiren gece ve gündüz görevlileri"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"binme veya çalışma sırası, nöbet"}],"lexicalization_note":"Genel ardıl adı, gece ile gündüzün sıra değişimi ve sırayla binme ya da çalışma kullanımları ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dönüşümlü yer alma dalı en yakın sınırı verir, diğerleri yalnız nöbet, süreklilik, sonralık veya ilerleme alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal dönüşümlü yer değişimine daha sıkı bağlıdır; odak dalı genel ardıllığı ve sonradan gelen kişiyi de içerir.","focus_only":"Odak dalı, dönüşüm gerekmeksizin bir ardılın öncekinin ardından gelmesini de kapsar.","gloss":"ardından gelip yerini alma","neighbor_only":"Komşu dal, bir şeyin gidip benzerinin yerine gelmesiyle kurulan dönüşümlü değişimi öne çıkarır.","neighbor_ref":"root_000433/B006","relation_type":"near_synonym","shared_zone":"İki dal da öğelerin birbirinin ardından gelerek yer değiştirmesini kapsar."}],"source_phrase_ar":"كل شيء يعقب شيئا فهو عقيبه (ayn;maqayis); العاقب الذي يجيء في أثر صاحبه (jamhara); كل من خلف بعد شيء فهو عاقبه (sihah); كل شيء خلف بعد شيء فهو عاقب له (tahdhib); التعقيب أن يأتي بشيء بعد آخر والمعقبات ملائكة يتعاقبون (mufradat); الليل والنهار يتعاقبان (tahdhib)","source_summary":"Kaynaklar sonradan gelme ve öncekinin yerini alma çekirdeğinde birleşir; gece ile gündüz, görevli topluluklar ve binme nöbetleri bu çekirdeğin dönüşümlü örnekleridir.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"مجيء شيء بعد شيء وخلافته له، وتعاقب الليل والنهار والملائكة والطير والإبل والركاب والنوب، والعاقب الذي يأتي في أثر غيره أو يخلفه","what_is_not_ar":"ليس الجزاء والعقوبة المختصة ولا الرجوع والنكوص ولا الصعود الصعب"},"support_links":[]},{"boundary":"Genel sonuç çekirdeği korunmalı, iyi karşılığa özgü kullanım ve hastalık kalıntısı bütün dala yayılmamalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B006","candidate_links":[{"candidate_id":"cand_c38510af3c397691475f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عُقْبَى","morph_features":"STEM|POS:N|LEM:EuqobaY|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:15:3:1","qac_word_ref":"91:15:3","surface_ar":"عُقْبَٰ"}],"gloss":"sonuç ve varılan son durum","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir süreç veya işin vardığı son durum ve nihai sonuç temel anlamı oluşturur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kullanım sonuç alanını özellikle yararlı ve iyi karşılıkla sınırlar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir eylemin ardından hastalık, pişmanlık, iyilik veya kötülük gibi bir sonuç doğabilir."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir işin bitişini ve o işten sonra ortaya çıkan iyi ya da kötü nihai durumu birlikte anlatır.","boundary_detail":"Genel sonuç çekirdeği korunmalı, iyi karşılığa özgü kullanım ve hastalık kalıntısı bütün dala yayılmamalıdır.","branch_image_ar":"آخر الشيء وعاقبته","concept_gloss":"sonuç ve varılan son durum","contextual_glosses":[{"applicability":"Bir davranışın ardından iyi veya kötü yeni bir durumun doğduğunu bildiren yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önceki eylem ile ardından doğan sonuç arasındaki neden ilişkisini korur."},"facet_ids":["F003"],"text":"buna yol açtı","usage_role":"contextual"}],"definition":"Bir şeyin sonu veya bir eylemin ardından ortaya çıkan nihai sonuçtur; sonuç iyi ya da kötü olabilir, kimi kullanım iyi karşılığa daralır ve hastalıktan kalan belirti ayrı bir kalıntı örneğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir süreç veya işin vardığı son durum ve nihai sonuç temel anlamı oluşturur."},{"facet_id":"F002","role":"source_variant","statement":"Bir kullanım sonuç alanını özellikle yararlı ve iyi karşılıkla sınırlar."},{"facet_id":"F003","role":"associated_use","statement":"Bir eylemin ardından hastalık, pişmanlık, iyilik veya kötülük gibi bir sonuç doğabilir."}],"identity_rationale":"Kaynak ifadesi son, sonuç ve bir eylemin doğurduğu iyi ya da kötü durumu destekler; ancak bir kullanım sonucu özellikle iyi karşılıkla sınırlar ve hastalıktan kalan belirtiyi yan bir kalıntı olarak ekler.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"son, sonuç, varılan nihai durum"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"karşılık veya sonuç; kimi kullanımda iyi karşılık"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"buna yol açtı, ardından bunu doğurdu"}],"lexicalization_note":"Son ve sonuç adları, iyi karşılığa daralan biçim ile bir şeyin sonuç doğurmasını anlatan yapıdan ayrı gösterilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; varılan son durum dalı en yakın karşılıktır, ötekiler yalnız bitiş, yarar, neden olunan zarar veya gecikme alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında önceki işin sonucu olma ilişkisi belirgindir; komşu dalda dönüşme ve bir sona varma daha geniştir.","focus_only":"Odak dalı, işin ardından doğan iyi ya da kötü sonucu ve karşılığı da kapsar.","gloss":"varılan son durum","neighbor_only":"Komşu dal, bir şeyin başka bir duruma dönüşmesini veya belirli bir varış noktasına ulaşmasını öne çıkarır.","neighbor_ref":"root_000897/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir sürecin sonunda ulaşılan durumu anlatır."}],"source_phrase_ar":"أتى فلان خبرا فعقب بخير منه (ayn); أعقب الله فلانا عقبى نافعة (jamhara); عاقبة كل شيء آخره والعقبى جزاء الأمر (sihah); عاقبة كل شيء آخره واستعقب من أمره ندما (tahdhib;maqayis); العقب والعقبى يختصان بالثواب والعاقبة للمتقين (mufradat); العقبول بقية المرض واللام زائدة (maqayis-variant)","source_summary":"Kaynak ifadesi son ve sonuç anlamını iyi ya da kötü doğabilecek etkilerle verir; bunun içinde iyi karşılığa daralan bir yorum ve ağır hastalıktan sonra kalan belirti de yer alır.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"آخر الشيء وخاتمته وعاقبته وعقباه، وما يورثه الفعل أو يستعقبه من خير أو شر أو ندم أو مرض","what_is_not_ar":"لا يدخل فيه العقاب بمعنى الطائر ولا العقبة الجبلية ولا العصب"},"support_links":["sup_4a590348a1d84b3e8feb"]},{"boundary":"Dal her türlü karşılığı değil, kusur veya suçtan sonra verilen kötü ve acı verici karşılığı kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B007","candidate_links":[{"candidate_id":"cand_5af7408e71349f106522","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عُقْبَى","morph_features":"STEM|POS:N|LEM:EuqobaY|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:15:3:1","qac_word_ref":"91:15:3","surface_ar":"عُقْبَٰ"}],"gloss":"suçtan sonra verilen kötü karşılık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kötü davranış veya suçtan sonra fail kötü bir karşılıkla sorumlu tutulur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Savaş bağlamındaki yorum, karşı tarafı cezalandırarak üstün gelip kazanç elde etmeyi anlatır."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir failin önceki kötülüğü nedeniyle acı verici bir karşılıkla sorumlu tutulduğu durumları kapsar.","boundary_detail":"Dal her türlü karşılığı değil, kusur veya suçtan sonra verilen kötü ve acı verici karşılığı kapsar.","branch_image_ar":"العقوبة بعد الذنب","concept_gloss":"suçtan sonra verilen kötü karşılık","contextual_glosses":[{"applicability":"Kişinin belirli bir suça veya kötü davranışa karşılık sorumlu tutulduğu bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Faili, önceki suçu ve ona karşılık verilen cezayı açıkça korur."},"facet_ids":["F001"],"text":"işlediği suçtan dolayı cezalandırmak","usage_role":"general"}],"definition":"Bir kişiye işlediği suç veya kötülükten sonra kötü ve acı verici bir karşılık vermek, onu sorumlu tutup cezalandırmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kötü davranış veya suçtan sonra fail kötü bir karşılıkla sorumlu tutulur."},{"facet_id":"F002","role":"specialization","statement":"Savaş bağlamındaki yorum, karşı tarafı cezalandırarak üstün gelip kazanç elde etmeyi anlatır."}],"identity_rationale":"Kaynak ifadesi, işlenen suç veya kötülükten sonra kötü bir karşılık verme, sorumlu tutma ve acı çektirme anlamında birleşir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"ceza, cezalandırma"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"onları cezalandırıp üstün geldiniz ve kazanç elde ettiniz"}],"lexicalization_note":"Genel ceza biçimleri ile savaşta cezalandırma sonucunda ele geçirme yorumu ayrı bir özel kullanım olarak tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; öç alma yönü taşıyan ceza dalı en yakın sınırı verir, ötekiler yargılama, caydırma, kısas veya genel karşılıktır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı genel cezalandırmadır; komşu dalda cezaya kızgınlık, karşılık verme ve öç alma güdüsü eşlik eder.","focus_only":"Odak dalı, suçtan sonra verilen her türlü kötü ve acı verici cezayı kapsar.","gloss":"kötülüğe ceza ile karşılık verme","neighbor_only":"Komşu dal, kızgınlık ve öç alma yönü belirgin olan cezayı öne çıkarır.","neighbor_ref":"root_001545/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir kötülükten sonra faili cezalandırmayı kapsar."}],"source_phrase_ar":"عاقبه الله عقابا ومعاقبة وعقوبة (jamhara); العقاب العقوبة وقد عاقبته بذنبه (sihah); العقاب والمعاقبة أن تجزي الرجل بما فعل سوءا (tahdhib); العقوبة والمعاقبة والعقاب يختص بالعذاب (mufradat); سميت عقوبة لأنها تكون آخرا وثاني الذنب (maqayis)","source_summary":"Kaynaklar cezayı, kişinin yaptığı kötülüğe daha sonra verilen acı verici karşılık olarak tanımlar; savaş bağlamındaki özel yorum cezalandırma yoluyla üstün gelmeye uzanır.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"العقاب والعقوبة والمعاقبة بمعنى الجزاء بالسوء أو المؤاخذة على الذنب أو إدراك الثأر، وما فسر به فعاقبتم من الإصابة والغنيمة على وجه العقوبة","what_is_not_ar":"ليس العقبى المحمودة ولا العقاب الطائر ولا العقب الوتر"},"support_links":["sup_ef5715203eeafd5b4736"]},{"boundary":"Dal sırf zaman bakımından sonra gelmeyi değil, önceki bir işin izini amaçlı biçimde sürüp yeniden ele almayı anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B008","candidate_links":[{"candidate_id":"cand_0cf01fe81cc5449f4dbc","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عُقْبَى","morph_features":"STEM|POS:N|LEM:EuqobaY|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:15:3:1","qac_word_ref":"91:15:3","surface_ar":"عُقْبَٰ"}],"gloss":"ardından izleyip yeniden inceleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Önceki kişi veya iş, ardından gidilip izi sürülerek yeniden ele alınır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İzleme; hak isteme, şüphe üzerine yeniden sorma, inceleme veya karşı çıkma amacı taşıyabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir hükmün ardından onu geri çevirecek veya ona karşı çıkacak kimsenin bulunmaması ayrıca anlatılır."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Önceki bir işin veya haberin izini sürerek onu soru, hak talebi ya da itirazla yeniden ele almayı kapsar.","boundary_detail":"Dal sırf zaman bakımından sonra gelmeyi değil, önceki bir işin izini amaçlı biçimde sürüp yeniden ele almayı anlatır.","branch_image_ar":"التعقب والمراجعة","concept_gloss":"ardından izleyip yeniden inceleme","contextual_glosses":[{"applicability":"Şüphe duyulan bir haber veya iş hakkında yeniden soru sorulup inceleme yapıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önceki konuya geri dönmeyi, soru sormayı ve araştırmayı korur."},"facet_ids":["F001","F002"],"text":"yeniden dönüp araştırmak","usage_role":"contextual"}],"definition":"Bir kişi, haber, iş veya hükmün ardından giderek onu hak arama, soru sorma, inceleme, karşı çıkma ya da geri çevirme amacıyla yeniden ele almaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Önceki kişi veya iş, ardından gidilip izi sürülerek yeniden ele alınır."},{"facet_id":"F002","role":"specialization","statement":"İzleme; hak isteme, şüphe üzerine yeniden sorma, inceleme veya karşı çıkma amacı taşıyabilir."},{"facet_id":"F003","role":"associated_use","statement":"Bir hükmün ardından onu geri çevirecek veya ona karşı çıkacak kimsenin bulunmaması ayrıca anlatılır."}],"identity_rationale":"Kaynak ifadesi bir kişiyi, işi, haberi veya hükmü sonradan izleyip hak arama, yeniden sorma, inceleme, karşı çıkma ya da geri çevirme işlemlerini destekler.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"hak istemek veya itiraz etmek için ardından izleyen kişi"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"onun hükmünü geri çevirecek veya sorgulayacak kimse yoktur"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"haberi veya işi yeniden dönüp araştırmak"}],"lexicalization_note":"İzleyen kişi adı, hükmün geri çevrilemezliğini bildiren söz ve haberi yeniden inceleme yapısı ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; haberin izini sürme dalı en yakın karşılıktır, ötekiler inkâr, kanıt, hüküm açıklama veya kapsamlı arama alanında kalır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında önceki konuya geri dönme ve onu inceleme kurucudur; komşu dal genel haber edinme etkinliğidir.","focus_only":"Odak dalı, önceden verilmiş hükme karşı çıkmayı ve hak istemek için kişiyi izlemeyi de kapsar.","gloss":"haberin izini sürüp araştırma","neighbor_only":"Komşu dal, henüz öğrenilmek istenen haberi soru, dinleme veya gözlemle toplama üzerinde yoğunlaşır.","neighbor_ref":"root_000321/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir haberin izini sürmeyi ve soru yoluyla bilgi aramayı kapsar."}],"source_phrase_ar":"المعقب الذي يتتبع عقب إنسان في طلب حق (ayn); لا معقب لحكمه أي لا راد لقضائه (ayn); تعقبت الرجل إذا أخذته بذنب وتعقبت عن الخبر إذا شككت وعدت للسؤال (sihah); المعقب الذي يكر على الشيء ولا يكر أحد على ما أحكمه الله (tahdhib); لا أحد يتعقبه ويبحث عن فعله (mufradat); تعقبت ما صنع فلان أي تتبعت أثره (maqayis)","source_summary":"Kaynaklar önceki kişi, haber, iş veya hükmün izini amaçlı biçimde sürme çekirdeğinde birleşir; amaç hak isteme, yeniden sorma, inceleme, itiraz veya geri çevirme olabilir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"تتبع الأمر أو الخبر أو الحكم بعده للسؤال أو الطلب أو الاعتراض أو الرد، ومنه المعقب طالب الحق ولا معقب لحكمه أي لا راد أو لا متتبع معارض","what_is_not_ar":"ليس مجرد التعاقب الزمني ولا الرجوع على العقب ولا العقوبة"},"support_links":["sup_3a894df59abb0a29a206"]},{"boundary":"Dal yalnız birinin ardından gelmeyi değil, daha önce yapılmış aynı tür etkinliğe yeniden dönmeyi gerektirir.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُقْبَى","morph_features":"STEM|POS:N|LEM:EuqobaY|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:15:3:1","qac_word_ref":"91:15:3","surface_ar":"عُقْبَٰ"}],"gloss":"aynı tür işi yeniden yapma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Daha önce yapılmış bir işin ardından aynı tür iş yeniden gerçekleştirilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Koşu ve otlama gibi etkinliklerde benzer veya karşılıklı evreler yeniden başlar."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kuşun yükselip alçalması ve ayın kaybolduktan sonra yeniden görünmesi döngüsel örneklerdir."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir işin tamamlanmasından sonra aynı tür etkinliğe yeniden dönülen bütün temel bağlamları kapsar.","boundary_detail":"Dal yalnız birinin ardından gelmeyi değil, daha önce yapılmış aynı tür etkinliğe yeniden dönmeyi gerektirir.","branch_image_ar":"العود مرة بعد مرة","concept_gloss":"aynı tür işi yeniden yapma","contextual_glosses":[{"applicability":"Sefer, ibadet veya koşu gibi tamamlanmış bir etkinliğin yeniden yapıldığı durumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İlk tamamlanmayı, geri dönüşü ve aynı tür etkinliğin yinelenmesini korur."},"facet_ids":["F001","F002"],"text":"bir kez daha dönüp yapmak","usage_role":"contextual"}],"definition":"Bir işi yaptıktan sonra aynı tür işe yeniden dönmek veya benzer bir hareket evresini yinelemektir; koşu, otlama, uçuş ve aylık görünme bunun özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Daha önce yapılmış bir işin ardından aynı tür iş yeniden gerçekleştirilir."},{"facet_id":"F002","role":"specialization","statement":"Koşu ve otlama gibi etkinliklerde benzer veya karşılıklı evreler yeniden başlar."},{"facet_id":"F003","role":"example","statement":"Kuşun yükselip alçalması ve ayın kaybolduktan sonra yeniden görünmesi döngüsel örneklerdir."}],"identity_rationale":"Kaynak ifadesi aynı tür işin bir ilk gerçekleştirmeden sonra yeniden yapılmasını ve koşu, otlama, uçuş ya da aylık dönüş gibi yinelenen devreleri destekler.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"aynı tür işi yeniden yapma"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"atın bir koşudan sonra yeniden ve daha iyi koşması"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"bir otlak türünden ötekine dönüşümlü geçen deve sürüsü"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"kuşun yükselişiyle alçalışı arasındaki hareket evresi"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"ayın kaybolduktan sonra yeniden görünmesi, aylık dönüşü"}],"lexicalization_note":"Genel yeniden yapma biçimi, koşu ve otlama yapıları ile kuş ve ayın döngüsel hareket adları ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yeniden yapma dalı en yakın sınırı verir, ötekiler dönüş, tereddüt, erken gitme veya konu dışı alanlardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında önceki etkinliğe dönüş ve yeni bir evre başlatma belirgindir; komşu dal genel yineleme sayısını öne çıkarır.","focus_only":"Odak dalı, tamamlanan işe geri dönmeyi ve koşu, otlama, uçuş gibi belirli devreleri kapsar.","gloss":"bir işi yeniden yapma","neighbor_only":"Komşu dal, aynı şeyin iki kez veya art arda yinelenmesini daha genel biçimde anlatır.","neighbor_ref":"root_000208/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir eylemin daha önceki örneğinden sonra yeniden gerçekleşmesini kapsar."}],"source_phrase_ar":"التعقيب غزوة بعد غزوة وسير بعد سير والخيل تعقب في حضرها (ayn); المعقب الذي يجيء مرة بعد أخرى وعقب الغازي إذا قفل ثم رجع (jamhara); عقب للفرس جري بعد جري والتعقيب أن يغزو الرجل ثم يثني من سنته (sihah); كل من عمل عملا ثم عاد إليه فقد عقب والتعقيب صلاة أو غيرها ثم يعود فيه (tahdhib); عقب الفرس في عدوه وعقبة الطائر صعوده وانحداره (mufradat); عقبة الإبل أن ترعى الحمض مرة والخلة أخرى (maqayis)","source_summary":"Kaynaklar bir işten sonra aynı tür işe yeniden dönmede birleşir; sefer, ibadet, koşu, otlama, uçuş ve ayın görünmesi bu yinelemenin farklı bağlamlarıdır.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"العود إلى العمل بعد عمل مثله، كغزوة بعد غزوة، وصلاة بعد صلاة، وجري بعد جري، ومرعى بعد مرعى، وطلوع بعد غياب","what_is_not_ar":"ليس التعاقب الذي هو خلافة شخص لشخص فقط ولا آخر الشيء وحده"},"support_links":[]},{"boundary":"Üç kullanım ortak bir değişim ve güvence alanında tutulabilir, fakat her birinin işlem koşulları ayrı belirtilmelidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُقْبَى","morph_features":"STEM|POS:N|LEM:EuqobaY|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:15:3:1","qac_word_ref":"91:15:3","surface_ar":"عُقْبَٰ"}],"gloss":"bedel, satış başvurusu ve elde tutma güvencesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya şeyin yerine başka bir bedel alınır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Satılan maldaki sorun nedeniyle satıcıya sonradan başvurma ve ondan karşılık isteme hakkı doğar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Satıcı malı ödeme gelene dek yanında tutarsa, malın kaybından kendisi sorumlu olur."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın tek kavrama indirgenemeyen üç alışveriş kullanımını kısa ve açık biçimde birlikte gösterir.","boundary_detail":"Üç kullanım ortak bir değişim ve güvence alanında tutulabilir, fakat her birinin işlem koşulları ayrı belirtilmelidir.","branch_image_ar":"العقبة بدلا وضمانا","concept_gloss":"bedel, satış başvurusu ve elde tutma güvencesi","contextual_glosses":[{"applicability":"Satıştan sonra bir kusur veya kayıp nedeniyle sorumluluğun kime ait olduğunun belirtildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Satışı, sonradan doğan başvuruyu ve malı elde tutanın sorumluluğunu korur."},"facet_ids":["F002","F003"],"text":"satılan maldan doğan başvuru ve güvence","usage_role":"contextual"}],"definition":"Değişim ve satış alanında, bir şeyin yerine alınan bedeli, satılan mal yüzünden sonradan doğan başvuru ve sorumluluğu ya da malın ödeme gelene dek satıcıda tutulup onun güvencesinde kalmasını anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya şeyin yerine başka bir bedel alınır."},{"facet_id":"F002","role":"specialization","statement":"Satılan maldaki sorun nedeniyle satıcıya sonradan başvurma ve ondan karşılık isteme hakkı doğar."},{"facet_id":"F003","role":"specialization","statement":"Satıcı malı ödeme gelene dek yanında tutarsa, malın kaybından kendisi sorumlu olur."}],"identity_rationale":"Kaynak ifadesi bedel alma, satışta sonradan doğan sorumluluk ve satılan malı ödeme gelene dek elde tutma güvencesini destekler; bunlar tek işlem değil, aynı dalda toplanmış üç hukuk ve alışveriş kullanımıdır.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"tutsağın veya bir şeyin yerine alınan bedel"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"satılan maldan doğan başvuru hakkı ve sorumluluk"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"malı ödeme gelene dek elinde tutan satıcı kayıptan sorumludur"}],"lexicalization_note":"Bedel, satıştaki sonradan doğan sorumluluk ve malı elde tutan satıcının güvencesi ayrı söz birimleri olarak korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; satış güvencesi dalı en yakın sınırı verir, diğer adaylar yalnız bedel, kefalet, rehin, ibra veya emanet alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel satış güvencesidir; odak dalı bunun yanında ayrı bir bedel alma işlemini ve malı elinde tutan satıcıyı içerir.","focus_only":"Odak dalı, yerine alınan bedeli ve satılan malı ödeme gelene dek elde tutma sorumluluğunu da kapsar.","gloss":"satıştan doğan güvence ve başvuru","neighbor_only":"Komşu dal, alışverişte kusur çıkarsa başvurmayı güvenceye alan belge, koşul ve yükümlülüğü geniş biçimde kapsar.","neighbor_ref":"root_001055/B006","relation_type":"near_neighbor","shared_zone":"İki dal da satıştan sonra ortaya çıkabilecek kusur veya kayıp için güvence ve sorumluluk kurar."}],"source_phrase_ar":"أخذت من أسيري عقبة إذا أخذت منه بدلا (sihah); المعتقب ضامن لما اعتقب أي اعتقبت الشيء إذا حبسته عندك (tahdhib); عقب علي في تلك السلعة عقب أي أدركني فيها درك والتعقبة الدرك (maqayis); أخذت عقبة من أسيري وهو أن تأخذ منه بدلا (maqayis)","source_summary":"Kaynak ifadesi üç ayrı işlemi bir araya getirir: yerine bedel alma, satıştan doğan sonradan başvuru ve satılan malı ödeme gelene dek elde tutanın sorumluluğu.","sources":["SI","TA","MQ"],"what_is_ar":"العقبة بمعنى بدل يؤخذ مكان شيء، أو درك يلحق في السلعة، أو احتباس المبيع حتى يقبض الثمن مع ضمان المعتقب","what_is_not_ar":"ليس العقبة الجبلية ولا النوبة في الركوب ولا العقوبة العامة"},"support_links":[]},{"boundary":"Dal nihai hüküm veya soy anlamını değil, önceki madde, durum ya da niteliğin geride bıraktığı kalanı kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B011","candidate_links":[{"candidate_id":"cand_bd93f051dfdb269fd8d0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عُقْبَى","morph_features":"STEM|POS:N|LEM:EuqobaY|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:15:3:1","qac_word_ref":"91:15:3","surface_ar":"عُقْبَٰ"}],"gloss":"geride kalan son parça ya da iz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Önceki şey tükendikten veya değiştikten sonra ondan bir bölüm ya da iz kalır."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kapta kalan son yemek suyu, maddi kalıntının belirgin örneğidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Geçmiş bir nitelik veya hastalık, kişide görünür bir iz ya da belirti bırakabilir."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem maddi bir artığı hem de geçmiş durumdan kişide kalan görünür belirtiyi kapsar.","boundary_detail":"Dal nihai hüküm veya soy anlamını değil, önceki madde, durum ya da niteliğin geride bıraktığı kalanı kapsar.","branch_image_ar":"بقية الشيء وأثره","concept_gloss":"geride kalan son parça ya da iz","contextual_glosses":[{"applicability":"Hastalık, görünüş veya başka bir niteliğin etkisi kişide sürmeye devam ettiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önceki durumu, ondan sonra kalmayı ve görünür belirtinin sürmesini korur."},"facet_ids":["F003"],"text":"önceki durumdan kalan belirti","usage_role":"contextual"}],"definition":"Bir madde, durum veya niteliğin kullanım ya da değişimden sonra geride kalan son bölümü, belirtisi veya görünür izidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Önceki şey tükendikten veya değiştikten sonra ondan bir bölüm ya da iz kalır."},{"facet_id":"F002","role":"example","statement":"Kapta kalan son yemek suyu, maddi kalıntının belirgin örneğidir."},{"facet_id":"F003","role":"extension","statement":"Geçmiş bir nitelik veya hastalık, kişide görünür bir iz ya da belirti bırakabilir."}],"identity_rationale":"Kaynak ifadesi bir şeyin kullanım veya değişim sonrasında kalan son bölümünü, kişide görülen kalıcı izi ve hastalıktan geriye kalan belirtiyi ortak kalıntı çekirdeğinde destekler.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"ağır hastalıktan kalan belirti"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"kapta kalan son yemek suyu"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"soyluluk ve güzellikten kişide kalan görünür iz"}],"lexicalization_note":"Hastalık kalıntısı biçimi, kapta kalan son bölüm ve kişide kalan görünür nitelik ayrı söz birimleri olarak korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; geçmiş şeyi gösteren kalıcı iz dalı en yakın karşılıktır, ötekiler az miktar, özel madde izi veya bozulma durumudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında kalan son bölüm veya belirti yeterlidir; komşu dalda iz, geçmiş varlığı ya da olayı gösteren bir işarettir.","focus_only":"Odak dalı, kapta kalan maddi son bölümü ve hastalıktan kalan belirtiyi de kapsar.","gloss":"önceki şeyden kalan iz","neighbor_only":"Komşu dal, geçmişte var olmuş bir şeyi gösteren işaret ve kalıntının kanıt değerini öne çıkarır.","neighbor_ref":"root_000011/B003","relation_type":"near_synonym","shared_zone":"İki dal da geçmiş bir madde veya durumdan geriye kalan izi kapsar."}],"source_phrase_ar":"العقبة شيء من المرق يرده مستعير القدر (sihah); عليه عقبه السرو والجمال أي أثر ذلك وهيئته (sihah); العقبة الشيء من المرق يرده مستعير القدر (tahdhib); عقبة القدر آخر ما في القدر أو يبقى بعد أن يغرف منها (maqayis); العقبول بقية المرض (maqayis-variant)","source_summary":"Kaynaklar kapta kalan son yemek suyu ile kişide süren görünüş veya hastalık belirtisini, önceki şeyden geriye kalan bölüm ya da iz olarak birleştirir.","sources":["SI","TA","MQ"],"what_is_ar":"ما يبقى في آخر الشيء أو يرد بعد استعماله أو يظهر أثره وهيئته، كعقبة القدر وبقية السرو والجمال وبقية المرض","what_is_not_ar":"ليس العاقبة الحكمية وحدها ولا الولد الباقي ولا العقبة الطريق"},"support_links":["sup_e7226e38b3b6f183e86f"]},{"boundary":"Dal dağ yolunun sarp yükselişini ve kayalık çıkıntıyı kapsar; binme sırası veya ceza anlamına geçmez.","branch_kind":"bare","branch_ref":"root_001033/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُقْبَى","morph_features":"STEM|POS:N|LEM:EuqobaY|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:15:3:1","qac_word_ref":"91:15:3","surface_ar":"عُقْبَٰ"}],"gloss":"sarp dağ geçidi ve kayalık çıkıntı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dağdaki yol yukarı yönelir, sarptır ve geçilmesi belirgin güçlük taşır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuyu veya dağ yüzündeki dışarı taşan sert kaya, basamak ya da çıkıntı aynı alana bağlıdır."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yükselen zorlu yolu ve aynı alandaki dışarı taşan kaya anlamını birlikte temsil eder.","boundary_detail":"Dal dağ yolunun sarp yükselişini ve kayalık çıkıntıyı kapsar; binme sırası veya ceza anlamına geçmez.","branch_image_ar":"العقبة الصعبة والناشز","concept_gloss":"sarp dağ geçidi ve kayalık çıkıntı","contextual_glosses":[{"applicability":"Dağda yukarı çıkan, engebeli ve geçilmesi güç yol veya geçit için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yukarı yönü, dağ ortamını, sarplığı ve geçiş güçlüğünü korur."},"facet_ids":["F001"],"text":"dik ve zorlu dağ yolu","usage_role":"general"}],"definition":"Dağda yükselen sarp, engebeli ve geçilmesi güç yol veya geçittir; ayrıca kuyu içinde ya da dağ yüzünde dışarı taşan sert kaya ve basamak benzeri çıkıntıyı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dağdaki yol yukarı yönelir, sarptır ve geçilmesi belirgin güçlük taşır."},{"facet_id":"F002","role":"extension","statement":"Kuyu veya dağ yüzündeki dışarı taşan sert kaya, basamak ya da çıkıntı aynı alana bağlıdır."}],"identity_rationale":"Kaynak ifadesi dağdaki dik, sarp ve zorlu yolu temel anlam olarak verir; kuyu veya dağ yüzündeki dışarı taşan kaya ve yükseltiyi aynı sertlik ve yükselme alanında ayrıca destekler.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"dik ve zorlu dağ yolu veya geçidi"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"kuyu ya da dağ yüzündeki dışarı taşan kaya"}],"lexicalization_note":"Tanım yalnız kanıtlanan yalın coğrafi anlamları kapsar ve başka yapılardaki sıra ya da ceza anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sarp geçit dalı en yakın karşılıktır, ötekiler iniş, taşlı arazi, uzunluk, yükselti veya yol kıvrımı gibi yan sınırlar sunar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal zorluk niteliğine daha dardır; odak dalı coğrafi yolu ve ayrıca çıkıntılı kaya anlamını taşır.","focus_only":"Odak dalı, sarp dağ yolunun yanında kuyu veya dağ yüzündeki kaya çıkıntısını da kapsar.","gloss":"çıkılması güç sarp geçit","neighbor_only":"Komşu dal, özellikle çıkılması çok güç olan tepe ve dik geçit niteliğine daralır.","neighbor_ref":"root_001051/B005","relation_type":"near_synonym","shared_zone":"İki dal da dik, sarp ve çıkılması zor bir dağ geçidini kapsar."}],"source_phrase_ar":"العقبة المصعد في الجبل والجمع عقاب (jamhara); العقبة واحدة عقاب الجبال والعقاب حجر ناتئ في جوف بئر (sihah); العقبة الجبل الطويل يعرض للطريق وهو صعب شديد (tahdhib); العقبة طريق وعر في الجبل (mufradat); الأصل الآخر يدل على ارتفاع وشدة وصعوبة والعقبة طريق في الجبل (maqayis)","source_summary":"Kaynaklar dağdaki sarp ve zorlu yükselen yolda birleşir; ayrıca kuyu içindeki veya dağ yüzündeki çıkıntılı kaya ve basamak benzeri yükseltiyi verir.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"العقبة طريق وعر صاعد في الجبل، وما شابهها من مرقى أو صخرة أو حجر ناشز في البئر أو عرض الجبل أو بناء الطي","what_is_not_ar":"ليس النوبة في الركوب ولا العقوبة ولا العقاب الطائر"},"support_links":[]},{"boundary":"Kuş çekirdektir; sancak benzetme yoluyla bağlıdır, korkunç bela ise özel bir türevdir ve ceza anlamıyla karıştırılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُقْبَى","morph_features":"STEM|POS:N|LEM:EuqobaY|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:15:3:1","qac_word_ref":"91:15:3","surface_ar":"عُقْبَٰ"}],"gloss":"kartal ve ona benzetilen büyük sancak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim güçlü ve büyük yırtıcı kuştur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Büyük sancak, görünüşü yırtıcı kuşa benzetildiği için aynı adla anılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Büyütme ve korkutma etkisi taşıyan özel türev, ağır ve korkunç belayı belirtir."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kuş çekirdeğini ve biçim benzerliğiyle oluşan sancak uzantısını birlikte temsil eder.","boundary_detail":"Kuş çekirdektir; sancak benzetme yoluyla bağlıdır, korkunç bela ise özel bir türevdir ve ceza anlamıyla karıştırılmaz.","branch_image_ar":"العقاب الجارح والراية","concept_gloss":"kartal ve ona benzetilen büyük sancak","contextual_glosses":[{"applicability":"Kuşun kendisi değil, ona görünüş bakımından benzetilmiş bayrak veya büyük sancak anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sancağı, büyüklüğünü ve kartalla kurulan görünüş benzetmesini korur."},"facet_ids":["F002"],"text":"kartala benzetilen büyük sancak","usage_role":"explanatory"}],"definition":"Gücüyle tanınan büyük bir yırtıcı kuştur; biçim benzerliği nedeniyle büyük sancak veya bayrak da onun adıyla anılır, özel bir büyütülmüş biçim ise korkunç belayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim güçlü ve büyük yırtıcı kuştur."},{"facet_id":"F002","role":"extension","statement":"Büyük sancak, görünüşü yırtıcı kuşa benzetildiği için aynı adla anılır."},{"facet_id":"F003","role":"specialization","statement":"Büyütme ve korkutma etkisi taşıyan özel türev, ağır ve korkunç belayı belirtir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Önceki suça verilen kötü karşılık anlamını ekler.","collision":"Aynı kökün cezalandırma dalıyla doğrudan karışır.","fit":"displacement","loses":"Yırtıcı kuşu, güç niteliğini ve sancak benzetmesini bütünüyle yitirir.","preserves":"Aynı ses dizisine bağlı başka bir sözlük alanıyla yalnız biçimsel yakınlık taşır."},"text":"ceza"}],"identity_rationale":"Kaynak ifadesi güçlü yırtıcı kuşu temel alır, büyük sancağın biçim benzerliğiyle ondan adlandırılmasını açıklar ve büyütülmüş türevde korkunç bela anlamını ayrıca verir.","lexical_glosses":[{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"kartal, güçlü yırtıcı kuş"},{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"kartala benzetilen büyük sancak veya bayrak"},{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"korkunç ve ağır bela"}],"lexicalization_note":"Yalın kuş adı, kuşa benzetilen sancak ve korkunç belayı anlatan türemiş biçim birbirinden ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dikili sancak dalı uzantı için en yararlı karşılaştırmadır, ötekiler yalnız güç, renk, öncülük veya görünüş alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalındaki sancak kuş benzetmesine dayanan bir uzantıdır; komşu dalda bayrak doğrudan temel gönderimdir.","focus_only":"Odak dalı yırtıcı kuşu temel alır ve sancağı yalnız kuşa benzetilmesi yoluyla kapsar.","gloss":"görünür büyük sancak","neighbor_only":"Komşu dal, görünür olmak üzere dikilmiş bayrak veya işareti benzetme gerektirmeden anlatır.","neighbor_ref":"root_000531/B011","relation_type":"near_neighbor","shared_zone":"İki dal da uzaktan görülebilen büyük bayrak veya sancağı kapsar."}],"source_phrase_ar":"العقاب الطائر المعروف وسميت الراية عقابا (jamhara); العقاب طائر والعقاب عقاب الراية (sihah); العقاب هذا الطائر والعقاب العلم الضخم واللواء (tahdhib); العقاب سمي لتعاقب جريه في الصيد وبه شبه في الهيئة الراية (mufradat); العقاب من الطير سميت لشددتها وقوتها ثم شبهت الراية بها (maqayis); العقنباة الداهية من العقبان وأصلها عقاب (maqayis-variant)","source_summary":"Kaynaklar güçlü yırtıcı kuşta ve biçimce ona benzetilen büyük sancakta birleşir; ayrıca tek kaynaklı biçim çeşidi korkunç bela anlamını taşır.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"العقاب الطائر الجارح المعروف، وما شبه به من الراية أو اللواء أو الناقة السوداء، والعقنباة الداهية من العقبان","what_is_not_ar":"ليس العقاب بمعنى العقوبة ولا العقبة الطريق ولا العقب الوتر"},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_001033/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُقْبَى","morph_features":"STEM|POS:N|LEM:EuqobaY|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:15:3:1","qac_word_ref":"91:15:3","surface_ar":"عُقْبَٰ"}],"gloss":"özel adlandırma kümesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"source_variant","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kullanım, ortak kavramsal bağ gösterilmeden erkek kişi adı olarak verilmiştir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvan merkezli kullanımın temel gönderimi erkek kekliktir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Atlar görünüş veya hareket benzerliği yoluyla erkek kekliğe benzetilerek adlandırılır."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"يعقوب واليعقوب","concept_gloss":"özel adlandırma kümesi","contextual_glosses":[{"applicability":"Kişi adından bağımsız olan hayvan merkezli kullanım ve onun benzetme uzantısı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Erkek keklik çekirdeğini ve atlara aktarılan benzetme ilişkisini korur."},"facet_ids":["F002","F003"],"text":"erkek keklik; ona benzetilen at","usage_role":"explanatory"}],"definition":"Bu dal tek bir üretken kök anlamına indirgenmez: bir yanda erkek kişi adı, öte yanda erkek keklik ve ona benzetilerek adlandırılan at aynı sınırlı adlandırma kümesi içinde tutulur.","distinctive_facets":[{"facet_id":"F001","role":"source_variant","statement":"Bir kullanım, ortak kavramsal bağ gösterilmeden erkek kişi adı olarak verilmiştir."},{"facet_id":"F002","role":"core","statement":"Hayvan merkezli kullanımın temel gönderimi erkek kekliktir."},{"facet_id":"F003","role":"extension","statement":"Atlar görünüş veya hareket benzerliği yoluyla erkek kekliğe benzetilerek adlandırılır."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_041","rendering_kind":"ordinary","target_gloss":"erkek kişi adı"},{"lexical_unit_id":"lu_042","rendering_kind":"ordinary","target_gloss":"erkek keklik ve ona benzetilen at"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"يعقوب اسم رجل واليعقوب ذكر الحجل (sihah); يعقوب متعلق بعقب عيصو واليعقوب ذكر الحجل وتسمى الخيل يعاقيب (tahdhib); اليعقوب ذكر الحجل لما له من عقب الجري (mufradat)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["SI","TA","MU"],"what_is_ar":"يعقوب اسم رجل في الاستعمال العربي والقرآني، واليعقوب ذكر الحجل وما شبه به من الخيل، مع تعليل بعض المصادر بالتعلق بالعقب أو عقب الجري","what_is_not_ar":"ليس كل عاقب أو معقب ولا العقاب الطائر الجارح"},"support_links":[]},{"boundary":"Dal yalnız bitkiyle kurulan yapıda, sararma ve kurumaya yaklaşma evresini anlatır; genel son veya sonuç anlamına genişlemez.","branch_kind":"collocation","branch_ref":"root_001033/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عُقْبَى","morph_features":"STEM|POS:N|LEM:EuqobaY|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:15:3:1","qac_word_ref":"91:15:3","surface_ar":"عُقْبَٰ"}],"gloss":"bitkinin sararıp kurumaya yaklaşması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bitkinin sapı incelirken yaprağı veya meyvesi sararır ve kuruma evresi yaklaşır."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sapın incelmesiyle yaprak veya meyvenin sarardığı ve kurumanın yaklaştığı bitki evresini karşılar.","boundary_detail":"Dal yalnız bitkiyle kurulan yapıda, sararma ve kurumaya yaklaşma evresini anlatır; genel son veya sonuç anlamına genişlemez.","branch_image_ar":"اصفرار النبت ويبس العود","concept_gloss":"bitkinin sararıp kurumaya yaklaşması","contextual_glosses":[{"applicability":"Bitki veya çalının olgunluk sonrasında kurumadan hemen önceki görünüşü için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sararmayı, kurumanın henüz tamamlanmamasını ve ona yaklaşmayı korur."},"facet_ids":["F001"],"text":"sararıp kurumaya yüz tutmak","usage_role":"contextual"}],"definition":"Bir bitkinin sapının incelip sertleşmesi, yaprak veya meyvesinin sararması ve kurumaya çok yaklaşmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bitkinin sapı incelirken yaprağı veya meyvesi sararır ve kuruma evresi yaklaşır."}],"identity_rationale":"Kaynak ifadesi bitkinin sapının incelmesini, yaprak veya meyvesinin sararmasını ve bunun hemen ardından kuruma evresine yaklaşmasını birlikte destekler.","lexical_glosses":[{"lexical_unit_id":"lu_043","rendering_kind":"ordinary","target_gloss":"bitkinin sapı incelip yaprağı veya meyvesi sararmak ve kurumaya yaklaşmak"}],"lexicalization_note":"Tanım yalnız bitki veya belirli çalı adıyla kurulan yapıya bağlıdır; yalın kök için genel kuruma anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel bitki sararması ve kuruması dalı en yakın sınırı verir, ötekiler belirli kuru bitkiler veya farklı olgunlaşma evreleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı kurumadan hemen önceki belirli evreye ve sap incelmesine bağlıdır; komşu dal genel sararma ve kuruluğu içerir.","focus_only":"Odak dalı, sapın incelmesi ve yaprak veya meyvenin sararmasından sonra kurumanın yaklaşmasını belirli yapıda anlatır.","gloss":"bitkinin sararıp kuruması","neighbor_only":"Komşu dal, çeşitli bitki ve arazide genel sararma, kuruma ve kurutma durumlarını daha geniş kapsar.","neighbor_ref":"root_001612/B001","relation_type":"near_synonym","shared_zone":"İki dal da bitkinin yeşilliğini yitirip sararmasını ve kuruma yönünde değişmesini kapsar."}],"source_phrase_ar":"عقب العرفج إذا اصفرت ثمرته وحان يبسه (sihah); عقب النبت إذا دق عوده واصفر ورقه (tahdhib); عقب العرفج يعقب وعقبه أن يدق عوده وتصفر ثمرته ثم ليس بعد ذلك إلا يبسه (maqayis)","source_summary":"Kaynaklar bitki veya belirli çalının sapının incelmesi, yaprak ya da meyvesinin sararması ve bundan sonra kurumanın yaklaşması üzerinde birleşir.","sources":["SI","TA","MQ"],"what_is_ar":"عقب النبت أو العرفج إذا دق عوده واصفر ورقه أو ثمره وحان يبسه، بوصفه انتقالا إلى شدة ويبوسة","what_is_not_ar":"ليس العاقبة العامة ولا عقبة الطريق ولا العقوبة"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["91:15:1"],"branch_refs":[],"candidate_id":"cand_4356e75fefc656fb93f4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:15:1:backward-binding-connector","source_type":"word_analysis","support_ids":["sup_4b5aeac7e31a040be3c8","sup_6850b338b06f310a75fb"],"title":"backward-binding final connector","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:15:1","qac_refs":["91:15:1:1"],"status":"accepted"}},{"anchor_refs":["91:15:1"],"branch_refs":[],"candidate_id":"cand_aeabfdc41e331a11d44b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:15:1:connector-variant-consequence","source_type":"word_analysis","support_ids":["sup_1c0b7eb1fa802a10acc9","sup_4b5aeac7e31a040be3c8"],"title":"variant connector sharpens consequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:15:1","qac_refs":["91:15:1:1"],"status":"accepted"}},{"anchor_refs":["91:15:1"],"branch_refs":[],"candidate_id":"cand_e228f76c805d48cc438e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:15:1:fused-clipped-opening","source_type":"word_analysis","support_ids":["sup_4b5aeac7e31a040be3c8","sup_cb4d5a917fa9c63289e6"],"title":"fused clipped polarity opening","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:15:1","qac_refs":["91:15:1:1"],"status":"accepted"}},{"anchor_refs":["91:15:2"],"branch_refs":[],"candidate_id":"cand_1eb0b821bf23df5eef0c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:15:2:declarative-negation-scope","source_type":"word_analysis","support_ids":["sup_1f30ce93824205c52f2e","sup_53a6d5f56b706be58eb5"],"title":"declarative negation over the whole predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:15:2","qac_refs":["91:15:1:2"],"status":"accepted"}},{"anchor_refs":["91:15:2"],"branch_refs":[],"candidate_id":"cand_b83ec9ea1d57b2e6846b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:15:2:durable-non-fear","source_type":"word_analysis","support_ids":["sup_1f30ce93824205c52f2e","sup_daa52e7a338a9489de95"],"title":"durable denial of fearing aftermath","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:15:2","qac_refs":["91:15:1:2"],"status":"accepted"}},{"anchor_refs":["91:15:2"],"branch_refs":[],"candidate_id":"cand_b5c6951703ad721bb706","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:15:2:fused-boundary-polarity","source_type":"word_analysis","support_ids":["sup_1f30ce93824205c52f2e","sup_b7c2b3d30dcb45e98f81"],"title":"boundary and polarity fused","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:15:2","qac_refs":["91:15:1:2"],"status":"accepted"}},{"anchor_refs":["91:15:2"],"branch_refs":[],"candidate_id":"cand_b96e20f95182be2d4c34","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:15:2:variant-negator-mood-contrast","source_type":"word_analysis","support_ids":["sup_0b0839356b0f0745879d","sup_1f30ce93824205c52f2e"],"title":"variant negator changes time and mood","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:15:2","qac_refs":["91:15:1:2"],"status":"accepted"}},{"anchor_refs":["91:15:3"],"branch_refs":[],"candidate_id":"cand_79883d690861f5ab089e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000447"],"scope":"focus_ayah","source_local_id":"91:15:3:base-form-not-causative-or-processual","source_type":"word_analysis","support_ids":["sup_49e6cb53ac84ec9d98c6","sup_8a9e0ce7ce13d620ff98"],"title":"base fear state, not frightening or depletion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:15:3","qac_refs":["91:15:2:1"],"status":"accepted"}},{"anchor_refs":["91:15:3"],"branch_refs":[],"candidate_id":"cand_acd93ddfa4b93a6d89ff","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000447"],"scope":"focus_ayah","source_local_id":"91:15:3:fear-field-and-formula-inversion","source_type":"word_analysis","support_ids":["sup_49e6cb53ac84ec9d98c6","sup_8aae999289e94db7274f"],"title":"fear field inverted into agent non-fear","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:15:3","qac_refs":["91:15:2:1"],"status":"accepted"}},{"anchor_refs":["91:15:3"],"branch_refs":[],"candidate_id":"cand_90c9d61ae70818875c6f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000447"],"scope":"focus_ayah","source_local_id":"91:15:3:imperfect-indicative-standing-assertion","source_type":"word_analysis","support_ids":["sup_49e6cb53ac84ec9d98c6","sup_9c69c7d04c1ee68e51ea"],"title":"standing assertion after completed actions","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:15:3","qac_refs":["91:15:2:1"],"status":"accepted"}},{"anchor_refs":["91:15:3"],"branch_refs":[],"candidate_id":"cand_56493aab062e63ae57aa","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000447"],"scope":"focus_ayah","source_local_id":"91:15:3:implicit-subject-primary-divine-resolution","source_type":"word_analysis","support_ids":["sup_49e6cb53ac84ec9d98c6","sup_834cf70751208ed17df5"],"title":"implicit subject with favored divine recovery","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:15:3","qac_refs":["91:15:2:1"],"status":"accepted"}},{"anchor_refs":["91:15:3"],"branch_refs":[],"candidate_id":"cand_078725b3b9ff1728c621","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000447"],"scope":"focus_ayah","source_local_id":"91:15:3:sound-drawn-into-aftermath","source_type":"word_analysis","support_ids":["sup_49e6cb53ac84ec9d98c6","sup_8bd6e9e7a8f303193bc8"],"title":"fear sound drawn toward aftermath","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:15:3","qac_refs":["91:15:2:1"],"status":"accepted"}},{"anchor_refs":["91:15:3"],"branch_refs":[],"candidate_id":"cand_85fe9fc803a7b0a5e8fa","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000447"],"scope":"focus_ayah","source_local_id":"91:15:3:surah-closing-moral-answer","source_type":"word_analysis","support_ids":["sup_49e6cb53ac84ec9d98c6","sup_dbe44b2414e66084ee2a"],"title":"closing answer to success and denial","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:15:3","qac_refs":["91:15:2:1"],"status":"accepted"}},{"anchor_refs":["91:15:3"],"branch_refs":[],"candidate_id":"cand_64ccb5e98d3d2082ea81","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000447"],"scope":"focus_ayah","source_local_id":"91:15:3:transitive-consequence-frame","source_type":"word_analysis","support_ids":["sup_49e6cb53ac84ec9d98c6","sup_66d21b74ac399771ee03"],"title":"fear aimed at aftermath","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:15:3","qac_refs":["91:15:2:1"],"status":"accepted"}},{"anchor_refs":["91:15:4"],"branch_refs":[],"candidate_id":"cand_70b261332631cf61ec9c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001033"],"scope":"focus_ayah","source_local_id":"91:15:4:compact-singular-marked-form","source_type":"word_analysis","support_ids":["sup_9f164ceae112b47d1bba","sup_f3ab201c0aefe660d61f"],"title":"compact singular marked consequence form","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:15:4","qac_refs":["91:15:3:1","91:15:3:2"],"status":"accepted"}},{"anchor_refs":["91:15:4"],"branch_refs":[],"candidate_id":"cand_d3f358f798ec4630dc46","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001033"],"scope":"focus_ayah","source_local_id":"91:15:4:heel-following-punitive-aftermath","source_type":"word_analysis","support_ids":["sup_10c196f904a3dfc7256e","sup_f3ab201c0aefe660d61f"],"title":"heel-following punitive aftermath","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:15:4","qac_refs":["91:15:3:1","91:15:3:2"],"status":"accepted"}},{"anchor_refs":["91:15:4"],"branch_refs":[],"candidate_id":"cand_f1bedb63e63dfde23e16","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001033"],"scope":"focus_ayah","source_local_id":"91:15:4:object-as-threatening-sequel","source_type":"word_analysis","support_ids":["sup_54a3d46f17f574df746f","sup_f3ab201c0aefe660d61f"],"title":"object that functions as sequel","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:15:4","qac_refs":["91:15:3:1","91:15:3:2"],"status":"accepted"}},{"anchor_refs":["91:15:4"],"branch_refs":[],"candidate_id":"cand_371211ae5a9dfbcb9416","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001033"],"scope":"focus_ayah","source_local_id":"91:15:4:sound-weighted-final-word","source_type":"word_analysis","support_ids":["sup_d773afb83ed346c7d5e3","sup_f3ab201c0aefe660d61f"],"title":"heavy consequence sound trailing out","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:15:4","qac_refs":["91:15:3:1","91:15:3:2"],"status":"accepted"}},{"anchor_refs":["91:15:4"],"branch_refs":[],"candidate_id":"cand_188129ab832f77824fe4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001033"],"scope":"focus_ayah","source_local_id":"91:15:4:suffix-bound-specific-aftermath","source_type":"word_analysis","support_ids":["sup_d4f8ec6b12ed79e9e478","sup_f3ab201c0aefe660d61f"],"title":"suffix-bound specific aftermath","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:15:4","qac_refs":["91:15:3:1","91:15:3:2"],"status":"accepted"}},{"anchor_refs":["91:15:4"],"branch_refs":[],"candidate_id":"cand_09272a6bbbe5bd016398","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001033"],"scope":"focus_ayah","source_local_id":"91:15:4:surah-final-object-closure","source_type":"word_analysis","support_ids":["sup_12dc99dd84a69976ca3b","sup_f3ab201c0aefe660d61f"],"title":"surah-final object of consequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:15:4","qac_refs":["91:15:3:1","91:15:3:2"],"status":"accepted"}},{"anchor_refs":["91:15:2"],"branch_refs":[],"candidate_id":"cand_68c158c6376fc604c03d","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000447"],"scope":"focus_ayah","source_local_id":"91:15:2:1","source_type":"qac_morpheme","support_ids":["sup_313749ee0072e020fc3b"],"title":"QAC root occurrence: خ و ف","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:15:3"],"branch_refs":[],"candidate_id":"cand_0148db928fe36316af0e","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001033"],"scope":"focus_ayah","source_local_id":"91:15:3:1","source_type":"qac_morpheme","support_ids":["sup_fb45d91234f716f3825e"],"title":"QAC root occurrence: ع ق ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:15"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:15","branch_refs":["root_000447/B001","root_001033/B006"],"candidate_id":"cand_c38510af3c397691475f","commentary_obligation":"review","hft_ref":"hft_337dcf33c024f832b153","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b01-anticipated-aftermath","source_type":"hft","support_ids":["sup_4a590348a1d84b3e8feb"],"title":"b01-anticipated-aftermath","trust":"legacy_unbound"},{"anchor_refs":["91:15"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:15","branch_refs":["root_000447/B001","root_001033/B007"],"candidate_id":"cand_5af7408e71349f106522","commentary_obligation":"review","hft_ref":"hft_c41462d4642fab078d99","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b02-no-punitive-requital","source_type":"hft","support_ids":["sup_ef5715203eeafd5b4736"],"title":"b02-no-punitive-requital","trust":"legacy_unbound"},{"anchor_refs":["91:15"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:15","branch_refs":["root_000447/B001","root_001033/B008"],"candidate_id":"cand_0cf01fe81cc5449f4dbc","commentary_obligation":"review","hft_ref":"hft_dd0537694023106a0dee","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b03-no-follow-up-challenge","source_type":"hft","support_ids":["sup_3a894df59abb0a29a206"],"title":"b03-no-follow-up-challenge","trust":"legacy_unbound"},{"anchor_refs":["91:15"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:15","branch_refs":["root_000447/B005","root_001033/B011"],"candidate_id":"cand_bd93f051dfdb269fd8d0","commentary_obligation":"review","hft_ref":"hft_b5ce312985ae11a3b808","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b04-no-visible-fear-residue","source_type":"hft","support_ids":["sup_e7226e38b3b6f183e86f"],"title":"b04-no-visible-fear-residue","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَلَا يَخَافُ عُقْبَٰهَا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:15:1:1","qac_word_ref":"91:15:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"91:15:1:2","qac_word_ref":"91:15:1","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"خَافَ","morph_features":"STEM|POS:V|IMPF|LEM:xaAfa|ROOT:xwf|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:15:2:1","qac_word_ref":"91:15:2","root_ar":"خ و ف","surface_ar":"يَخَافُ"},{"lemma_ar":"عُقْبَى","morph_features":"STEM|POS:N|LEM:EuqobaY|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:15:3:1","qac_word_ref":"91:15:3","root_ar":"ع ق ب","surface_ar":"عُقْبَٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:15:3:2","qac_word_ref":"91:15:3","root_ar":"","surface_ar":"هَا"}],"word_analysis_qac_refs":[["91:15:1:1"],["91:15:1:2"],["91:15:2:1"],["91:15:3:1","91:15:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["91:15:1","91:15:2","91:15:3","91:15:4"]},"focus_surface_evidence":{"arabic_uthmani":"وَلَا يَخَافُ عُقْبَٰهَا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:15:1:1","qac_word_ref":"91:15:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"91:15:1:2","qac_word_ref":"91:15:1","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"خَافَ","morph_features":"STEM|POS:V|IMPF|LEM:xaAfa|ROOT:xwf|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:15:2:1","qac_word_ref":"91:15:2","root_ar":"خ و ف","surface_ar":"يَخَافُ"},{"lemma_ar":"عُقْبَى","morph_features":"STEM|POS:N|LEM:EuqobaY|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"91:15:3:1","qac_word_ref":"91:15:3","root_ar":"ع ق ب","surface_ar":"عُقْبَٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:15:3:2","qac_word_ref":"91:15:3","root_ar":"","surface_ar":"هَا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["91:15:1:1"],["91:15:1:2"],["91:15:2:1"],["91:15:3:1","91:15:3:2"]],"word_analysis_refs":["91:15:1","91:15:2","91:15:3","91:15:4"],"word_rows":[{"analysis_record_ref":"91:15:1","analytic_gloss_range_en":"clause-opening connector; locally it keeps the final negated clause attached to the prior action, with coordination, circumstantial, and resumptive readings available in the apparatus","analytic_root_gloss_range_en":null,"qac_refs":["91:15:1:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"91:15:2","analytic_gloss_range_en":"negating particle over the imperfect verb and its object; declarative non-fear rather than prohibition","analytic_root_gloss_range_en":null,"qac_refs":["91:15:1:2"],"root":{"note":"— (no root)"},"surface":{"arabic":"لَا","transliteration":"lā"}},{"analysis_record_ref":"91:15:3","analytic_gloss_range_en":"to fear, dread, or apprehend harm; locally negated and directed toward the explicit aftermath object","analytic_root_gloss_range_en":"broad fear family includes fearful anticipation, causing fear, comparative fear, diminishment, visible fear, and concrete nonlocal items; the local Form I verb selects the subject's own fear/apprehension and excludes causative or gradual-diminishing branches","qac_refs":["91:15:2:1"],"root":{"arabic":"خ و ف","transliteration":"kh-w-f"},"surface":{"arabic":"يَخَافُ","transliteration":"yakhāfu"}},{"analysis_record_ref":"91:15:4","analytic_gloss_range_en":"its aftermath, outcome, or consequence; locally the accusative object of fear, singular and suffix-bound to a prior event","analytic_root_gloss_range_en":"broad range includes heel/rear trace, following, turning back, posterity, succession, outcome, punitive consequence, pursuit or challenge, repetition, residue, and other nonlocal concrete branches; the local noun selects aftermath/outcome with punitive and heel-following pressure","qac_refs":["91:15:3:1","91:15:3:2"],"root":{"arabic":"ع ق ب","transliteration":"ʿ-q-b"},"surface":{"arabic":"عُقْبَٰهَا","transliteration":"ʿuqbāhā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["91:15"],"branch_refs":["root_000447/B001","root_001033/B006"],"candidate_id":"cand_c38510af3c397691475f","evidence_scope":"focus_ayah","hft_ref":"hft_337dcf33c024f832b153","item_id":"b01-anticipated-aftermath","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b01-anticipated-aftermath","support_id":"sup_4a590348a1d84b3e8feb"},{"anchor_refs":["91:15"],"branch_refs":["root_000447/B001","root_001033/B007"],"candidate_id":"cand_5af7408e71349f106522","evidence_scope":"focus_ayah","hft_ref":"hft_c41462d4642fab078d99","item_id":"b02-no-punitive-requital","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b02-no-punitive-requital","support_id":"sup_ef5715203eeafd5b4736"},{"anchor_refs":["91:15"],"branch_refs":["root_000447/B001","root_001033/B008"],"candidate_id":"cand_0cf01fe81cc5449f4dbc","evidence_scope":"focus_ayah","hft_ref":"hft_dd0537694023106a0dee","item_id":"b03-no-follow-up-challenge","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b03-no-follow-up-challenge","support_id":"sup_3a894df59abb0a29a206"},{"anchor_refs":["91:15"],"branch_refs":["root_000447/B005","root_001033/B011"],"candidate_id":"cand_bd93f051dfdb269fd8d0","evidence_scope":"focus_ayah","hft_ref":"hft_b5ce312985ae11a3b808","item_id":"b04-no-visible-fear-residue","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b04-no-visible-fear-residue","support_id":"sup_e7226e38b3b6f183e86f"}],"diagnostics":[],"lane_counts":{"global":10,"macro":15,"micro":4},"packet_summary":{"ayah_count":15,"focus_ref":"91:15","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ت ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000186","furuq_root_norm":"ت ل و","furuq_source_root_norm":"ت ل و","is_dominant":true,"target_occurrences":39,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000185","furuq_root_norm":"ت ل ل","furuq_source_root_norm":"ت ل ل","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["91:1","91:2","91:3","91:4","91:5","91:6","91:7","91:8","91:9","91:10","91:11","91:12","91:13","91:14","91:15"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"91:15","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":19,"unstructured_record_count":0},"identity":{"ayah_ref":"91:15","lane":"micro","linguistic_source_ref":"91:15","surface_ref":"91:15","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"91:15","target_tokens":[["O",["91:15:2"]],["bunun",["91:15:3"]],["sonucundan",["91:15:3"]],["korkmaz",["91:15:1","91:15:2"]]],"text":"O, bunun sonucundan korkmaz."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":15,"id":"s091-p01-001-015","label":"Whole surah","number":1,"refs":["91:1","91:2","91:3","91:4","91:5","91:6","91:7","91:8","91:9","91:10","91:11","91:12","91:13","91:14","91:15"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:2:variant-negator-mood-contrast","source_type":"word_analysis","support_id":"sup_0b0839356b0f0745879d","text":"{\"blocking_evidence\":null,\"headline\":\"variant negator changes time and mood\",\"reader_payoff\":\"The reader sees that the particle choice controls whether the closing non-fear feels standing and present or completed and past.\",\"reason\":\"The variant clarifies the force of the local negator but must not recast the canonical surface as the past-negating construction.\",\"representative_source_ids\":[\"QG-1fd74518\",\"QF-0110bc78\",\"QY-898a91b9\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:4:heel-following-punitive-aftermath","source_type":"word_analysis","support_id":"sup_10c196f904a3dfc7256e","text":"{\"blocking_evidence\":null,\"headline\":\"heel-following punitive aftermath\",\"reader_payoff\":\"The reader feels consequence as something that follows on the heels of the act, with punitive nearness supplied by context rather than by an explicit punishment form.\",\"reason\":\"V4 supports outcome and punitive branches, but the local noun remains aftermath; physical heel, hobbling, and punishment derivatives are retained as pressure, not replacement senses.\",\"representative_source_ids\":[\"QS-32ca4e14\",\"QS-463d4c98\",\"QS-a686ef57\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:4:surah-final-object-closure","source_type":"word_analysis","support_id":"sup_12dc99dd84a69976ca3b","text":"{\"blocking_evidence\":null,\"headline\":\"surah-final object of consequence\",\"reader_payoff\":\"The reader feels the whole episode land on the aftermath that is not feared, not merely on the act of destruction.\",\"reason\":\"The local word is both the verb's object and the final word, so the closure payoff is structural and directly anchored.\",\"representative_source_ids\":[\"QT-93707517\",\"QB-a8087a4c\",\"QY-1bbb7d50\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:1:connector-variant-consequence","source_type":"word_analysis","support_id":"sup_1c0b7eb1fa802a10acc9","text":"{\"blocking_evidence\":null,\"headline\":\"variant connector sharpens consequence\",\"reader_payoff\":\"The reader sees that connector choice affects whether the ending sounds like open attachment or a sharper consequence of the preceding destruction.\",\"reason\":\"The variant is useful for contrast, but the local surface remains {{ar:وَ}} ({{tr:wa}}), so consequential force must not overwrite the broader connective value.\",\"representative_source_ids\":[\"MG-88118cec\",\"QF-45b5b66f\",\"QY-af28feb4\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:2","source_type":"word_analysis","support_id":"sup_1f30ce93824205c52f2e","text":"{\"gloss_range\":\"negating particle over the imperfect verb and its object; declarative non-fear rather than prohibition\",\"prose\":\"{{ar:لَا}} ({{tr:lā}}) is the hinge of the ayah's whole assertion. It negates the finite predicate through the verb and its object, so the clause does not say only that fear is absent in the abstract; it says the aftermath itself falls inside the denied fear-frame. Because the following verb remains indicative, {{ar:لَا}} ({{tr:lā}}) reports non-fear rather than commanding someone not to fear. Its pairing with the imperfect makes the denial durable, while the variant with a past-negating particle shows how different the ending would feel if the closure were cast as completed past non-fear. As the second half of the opening particle pair, it keeps polarity fused to the backward-linking boundary, and its open vowel runs straight into the long vowel of the fear verb as one audible denial-unit.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَا}} ({{tr:lā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"91:15:2:1","source_type":"qac_morpheme","support_id":"sup_313749ee0072e020fc3b","text":"{\"lemma_ar\":\"خَافَ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:xaAfa|ROOT:xwf|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"91:15:2:1\",\"qac_word_ref\":\"91:15:2\",\"root_ar\":\"خ و ف\",\"surface_ar\":\"يَخَافُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:3","source_type":"word_analysis","support_id":"sup_49e6cb53ac84ec9d98c6","text":"{\"gloss_range\":\"to fear, dread, or apprehend harm; locally negated and directed toward the explicit aftermath object\",\"prose\":\"{{ar:يَخَافُ}} ({{tr:yakhāfu}}) carries the only finite verb of the ayah, and it is not absolute: the verb takes {{ar:عُقْبَٰهَا}} ({{tr:ʿuqbāhā}}) as its explicit object, so the denial is focused on fearing what follows from the prior act. The imperfect indicative makes that non-fear a standing assertion rather than a completed narrative action, with the variant past-negated form showing how sharply mood and aspect could change the closure. Its 3ms subject is not named inside the ayah; grammar leaves recovery inside the verb, while the attachment evidence most strongly links the subject to the prior divine actor in 91:14, so human heedlessness remains a contrastive possibility rather than the primary local resolution. The root's fear field includes dread and apprehensive risk-recognition, which makes the negation more than emotional calm: it denies vulnerability before consequence. Against the familiar no-fear reassurance formula (2:38; 2:62), this is non-fear predicated of the acting agent at the end of a destruction narrative, answering the surah's success and corruption axis (91:9) and the Thamud denial sequence (91:11). The Form I shape keeps the word on the subject's own fear state, not on making others afraid or on a gradual depletion image, while the sound moves from back-throat friction through an open vowel to lip closure before being pulled into the heavy gutturals of the aftermath noun.\",\"root_display\":\"{{ar:خ و ف}} ({{tr:kh-w-f}})\",\"root_gloss_range\":\"broad fear family includes fearful anticipation, causing fear, comparative fear, diminishment, visible fear, and concrete nonlocal items; the local Form I verb selects the subject's own fear/apprehension and excludes causative or gradual-diminishing branches\",\"surface_display\":\"{{ar:يَخَافُ}} ({{tr:yakhāfu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:1","source_type":"word_analysis","support_id":"sup_4b5aeac7e31a040be3c8","text":"{\"gloss_range\":\"clause-opening connector; locally it keeps the final negated clause attached to the prior action, with coordination, circumstantial, and resumptive readings available in the apparatus\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) opens the final ayah by binding it backward before the negation is even heard. The connector can be read as coordination, circumstance, or resumption, so the non-fear clause is not an isolated maxim: it can add a second assertion after 91:14, frame fearlessness as simultaneous with the leveling, or restart the close while keeping discourse continuity. The recognized connector variant with consequential force shows how a different opening particle would press the clause toward \\\"and so,\\\" but the local surface keeps the broader connective field of {{ar:وَ}} ({{tr:wa}}). In recitation the particle fuses immediately with {{ar:لَا}} ({{tr:lā}}), giving the ayah a clipped boundary-launch before the heavier verb-object unit arrives.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:2:declarative-negation-scope","source_type":"word_analysis","support_id":"sup_53a6d5f56b706be58eb5","text":"{\"blocking_evidence\":null,\"headline\":\"declarative negation over the whole predicate\",\"reader_payoff\":\"The reader notices that the ending denies fearing the specific aftermath, not merely fear in isolation.\",\"reason\":\"Attachment evidence explicitly scopes negation over the finite predicate with the object, and QAC identifies the particle as negating rather than prohibitive.\",\"representative_source_ids\":[\"QG-b0e56e95\",\"QG-d0d46544\",\"QT-3c01d38e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:4:object-as-threatening-sequel","source_type":"word_analysis","support_id":"sup_54a3d46f17f574df746f","text":"{\"blocking_evidence\":null,\"headline\":\"object that functions as sequel\",\"reader_payoff\":\"The reader sees that consequence is not a loose final noun; it is exactly what the verb says is not feared.\",\"reason\":\"Attachment evidence identifies the noun as the explicit object of the verb, while the semantic rows correctly describe the object as the feared sequel rather than a patient acted upon.\",\"representative_source_ids\":[\"QG-130eed65\",\"QS-5173a798\",\"QI-8658376f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:3:transitive-consequence-frame","source_type":"word_analysis","support_id":"sup_66d21b74ac399771ee03","text":"{\"blocking_evidence\":null,\"headline\":\"fear aimed at aftermath\",\"reader_payoff\":\"The reader notices that the fear word and the consequence word form one tight relation: not fearing what follows.\",\"reason\":\"The attachment evidence makes the object syntactically explicit, and the contextual frame supports transitive fear as a local pattern.\",\"representative_source_ids\":[\"QG-4e670e2a\",\"QI-6c8efb12\",\"QI-f4fa94d4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:1:backward-binding-connector","source_type":"word_analysis","support_id":"sup_6850b338b06f310a75fb","text":"{\"blocking_evidence\":null,\"headline\":\"backward-binding final connector\",\"reader_payoff\":\"The reader notices that the last sentence begins by tying itself back to 91:14 rather than floating as a detached proverb.\",\"reason\":\"The local evidence confirms a negated finite predicate following the connector, but it does not force only one of the coordination, circumstance, or resumption parses.\",\"representative_source_ids\":[\"QG-100d4255\",\"QS-18e6188b\",\"QB-63b7da46\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:3:implicit-subject-primary-divine-resolution","source_type":"word_analysis","support_id":"sup_834cf70751208ed17df5","text":"{\"blocking_evidence\":null,\"headline\":\"implicit subject with favored divine recovery\",\"reader_payoff\":\"The reader notices that agency is carried by morphology and context, with divine non-fear as the strongest local reading and human heedlessness as a contrastive shadow.\",\"reason\":\"The CRITICAL rows rightly notice pro-drop ambiguity, but attachment evidence strongly links the 3ms verb to the prior masculine singular divine subject in 91:14.\",\"representative_source_ids\":[\"QG-b7e69034\",\"QF-94964dc2\",\"MT-9fa32aee\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:3:base-form-not-causative-or-processual","source_type":"word_analysis","support_id":"sup_8a9e0ce7ce13d620ff98","text":"{\"blocking_evidence\":null,\"headline\":\"base fear state, not frightening or depletion\",\"reader_payoff\":\"The reader keeps the predicate on the agent's own non-fear instead of importing causative frightening or gradual wearing-down imagery.\",\"reason\":\"The local surface is Form I, so other root-family branches can sharpen the boundary but do not become active local senses.\",\"representative_source_ids\":[\"QF-75239c97\",\"QF-fc08495a\",\"QS-4feac0dd\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:3:fear-field-and-formula-inversion","source_type":"word_analysis","support_id":"sup_8aae999289e94db7274f","text":"{\"blocking_evidence\":null,\"headline\":\"fear field inverted into agent non-fear\",\"reader_payoff\":\"The reader notices that the ending denies not only emotion but also risk-recognition before consequence, unlike the no-fear reassurance formula (2:38; 2:62).\",\"reason\":\"The accepted fear branch supports dread and apprehension, and the formula rows include concrete references that function as contrast rather than local syntax.\",\"representative_source_ids\":[\"QS-17a75761\",\"QI-a06b8083\",\"ME-a84d3d89\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:3:sound-drawn-into-aftermath","source_type":"word_analysis","support_id":"sup_8bd6e9e7a8f303193bc8","text":"{\"blocking_evidence\":null,\"headline\":\"fear sound drawn toward aftermath\",\"reader_payoff\":\"The reader hears the fear verb move into the heavier aftermath word rather than ending as an isolated sound effect.\",\"reason\":\"The phonetic rows are retained because they are anchored to the local verb-object phrase and do not claim an independent semantic sense.\",\"representative_source_ids\":[\"QP-250284f1\",\"QP-a9d2949b\",\"MP-98c8cdd5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:3:imperfect-indicative-standing-assertion","source_type":"word_analysis","support_id":"sup_9c69c7d04c1ee68e51ea","text":"{\"blocking_evidence\":null,\"headline\":\"standing assertion after completed actions\",\"reader_payoff\":\"The reader feels the shift from the completed action chain of 91:14 into a lasting characterization at the close.\",\"reason\":\"QAC supports imperfect indicative morphology, but the variant rows are apparatus and therefore clarify rather than replace the local form.\",\"representative_source_ids\":[\"QG-f95b7246\",\"QT-c29ed27f\",\"QB-e452360a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:4:compact-singular-marked-form","source_type":"word_analysis","support_id":"sup_9f164ceae112b47d1bba","text":"{\"blocking_evidence\":null,\"headline\":\"compact singular marked consequence form\",\"reader_payoff\":\"The reader notices that the surah closes on one compressed aftermath word rather than a plural set of consequences or an explicit punishment noun.\",\"reason\":\"The local form is singular abstract with a suffix; distributional and form-comparison rows are useful when kept as marked-form contrast rather than a claim about a different local noun.\",\"representative_source_ids\":[\"QF-22c06075\",\"QF-a60a5a08\",\"QH-72c90b64\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:2:fused-boundary-polarity","source_type":"word_analysis","support_id":"sup_b7c2b3d30dcb45e98f81","text":"{\"blocking_evidence\":null,\"headline\":\"boundary and polarity fused\",\"reader_payoff\":\"The reader hears the ayah turn from prior action into final denial without an intervening pause or new noun subject.\",\"reason\":\"The particle sequence is local and directly structures the one-clause ayah.\",\"representative_source_ids\":[\"QF-e1ab88b4\",\"QT-e441a8c2\",\"QP-82bb743f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:1:fused-clipped-opening","source_type":"word_analysis","support_id":"sup_cb4d5a917fa9c63289e6","text":"{\"blocking_evidence\":null,\"headline\":\"fused clipped polarity opening\",\"reader_payoff\":\"The reader hears the final ayah start with two light particles before the heavier fear-and-aftermath phrase.\",\"reason\":\"The particle sequence is locally present and its sound observation stays tied to the actual two-particle opening.\",\"representative_source_ids\":[\"QF-edb42158\",\"QP-7c59bf5f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:4:suffix-bound-specific-aftermath","source_type":"word_analysis","support_id":"sup_d4f8ec6b12ed79e9e478","text":"{\"blocking_evidence\":null,\"headline\":\"suffix-bound specific aftermath\",\"reader_payoff\":\"The reader notices that the last word contains a pronoun problem: the aftermath belongs to a prior event, not to an unnamed generic consequence.\",\"reason\":\"The CRITICAL rows preserve antecedent pressure, but attachment evidence strongly licenses the suffix as resuming the immediately preceding divine action in 91:14.\",\"representative_source_ids\":[\"QG-0d52b59c\",\"QG-d32e698c\",\"QB-e7c49f37\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:4:sound-weighted-final-word","source_type":"word_analysis","support_id":"sup_d773afb83ed346c7d5e3","text":"{\"blocking_evidence\":null,\"headline\":\"heavy consequence sound trailing out\",\"reader_payoff\":\"The reader hears the closing consequence word as heavy before it opens into the final suffix.\",\"reason\":\"The sound rows are anchored in the actual final word and are kept as recitational texture, not independent semantic proof.\",\"representative_source_ids\":[\"QE-02023d7e\",\"QP-4884c8b0\",\"QP-c76644b5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:2:durable-non-fear","source_type":"word_analysis","support_id":"sup_daa52e7a338a9489de95","text":"{\"blocking_evidence\":null,\"headline\":\"durable denial of fearing aftermath\",\"reader_payoff\":\"The reader hears the ending as a standing characterization, not a one-time missing reaction.\",\"reason\":\"The imperfect verb under negation licenses a durable reading, while the explicit object prevents the claim from becoming generalized bravery.\",\"representative_source_ids\":[\"MG-94a29dd5\",\"QS-4d31d664\",\"QS-9bf9fdef\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:3:surah-closing-moral-answer","source_type":"word_analysis","support_id":"sup_dbe44b2414e66084ee2a","text":"{\"blocking_evidence\":null,\"headline\":\"closing answer to success and denial\",\"reader_payoff\":\"The reader sees the closing non-fear as part of the surah's moral arc, after success and purification (91:9) and after Thamud denial (91:11).\",\"reason\":\"The inter-ayah rows give concrete references and remain coherent as narrative-arc observations without controlling the local verb parse.\",\"representative_source_ids\":[\"MI-468a75ba\",\"MT-57aed69f\",\"QE-faef82c7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:15:4","source_type":"word_analysis","support_id":"sup_f3ab201c0aefe660d61f","text":"{\"gloss_range\":\"its aftermath, outcome, or consequence; locally the accusative object of fear, singular and suffix-bound to a prior event\",\"prose\":\"{{ar:عُقْبَٰهَا}} ({{tr:ʿuqbāhā}}) is the final object of the surah: grammatically the thing not feared, and semantically the sequel that could have occasioned fear. The suffix makes the aftermath definite and event-bound, not a generic consequence; its feminine form steers reference away from the masculine agent and most strongly back toward the preceding divine action in 91:14, while the repeated suffix shape carries the unresolved boundary from the prior leveling clause into the final word. The root selects the aftermath/outcome branch, but it keeps pressure from heel-following and punitive consequence: the result follows at the heels of the act and is close to requital without being named by the explicit punishment noun. The compact singular form gathers possible consequences into one object, distinguished from the more common outcome noun and fused to its suffix in the closing word. Because it is both object and last word, the whole Thamud narrative lands not simply on destruction but on the aftermath that is not feared; the heavy throat sounds and final open suffix make that consequence audible as the surah trails out.\",\"root_display\":\"{{ar:ع ق ب}} ({{tr:ʿ-q-b}})\",\"root_gloss_range\":\"broad range includes heel/rear trace, following, turning back, posterity, succession, outcome, punitive consequence, pursuit or challenge, repetition, residue, and other nonlocal concrete branches; the local noun selects aftermath/outcome with punitive and heel-following pressure\",\"surface_display\":\"{{ar:عُقْبَٰهَا}} ({{tr:ʿuqbāhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"91:15:3:1","source_type":"qac_morpheme","support_id":"sup_fb45d91234f716f3825e","text":"{\"lemma_ar\":\"عُقْبَى\",\"morph_features\":\"STEM|POS:N|LEM:EuqobaY|ROOT:Eqb|F|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"91:15:3:1\",\"qac_word_ref\":\"91:15:3\",\"root_ar\":\"ع ق ب\",\"surface_ar\":\"عُقْبَٰ\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَلَا يَخَافُ عُقْبَٰهَا","ayah_ref":"91:15"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000447/B001","root_001033/B006"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000447","role":"Anticipated harm makes the negation prospective rather than merely describing calm after an event.","root":"خ و ف","source_ref":"91:15","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_001033","role":"The terminal result of an act supplies the feared object as its eventual aftermath.","root":"ع ق ب","source_ref":"91:15","source_word_indices":["3"]}],"changed_reading":{"after":"The subject does not anticipate harm from the event's eventual aftermath.","before":"The clause merely says that an unnamed subject is not afraid."},"confidence":"strong","focus_anchor":"The negated verb at 91:15.2 governs the feminine-marked outcome noun at 91:15.3.","mechanism":"Fear is prospective anticipation, while the object names what an unspecified feminine event eventually leaves or produces.","model_id":"b01-anticipated-aftermath"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b01-anticipated-aftermath","source_type":"hft","support_id":"sup_4a590348a1d84b3e8feb","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَلَا يَخَافُ عُقْبَٰهَا","ayah_ref":"91:15"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000447/B001","root_001033/B007"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000447","role":"Expectation of harm supplies the deterrent force that the negation removes.","root":"خ و ف","source_ref":"91:15","source_word_indices":["2"]},{"branch_id":"B007","mapped_root_id":"root_001033","role":"Punitive consequence after an offense turns a generic result into retaliatory requital.","root":"ع ق ب","source_ref":"91:15","source_word_indices":["3"]}],"changed_reading":{"after":"The subject is undeterred by, or unexposed to, punitive requital after the deed.","before":"The subject has no anxiety about a generic result."},"confidence":"medium","focus_anchor":"The same verb-object construction can narrow the outcome at 91:15.3 to a retaliatory consequence.","mechanism":"The outcome is not neutral futurity but adverse requital arriving after a deed, so the denial concerns deterrence or exposure to punishment.","model_id":"b02-no-punitive-requital"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b02-no-punitive-requital","source_type":"hft","support_id":"sup_ef5715203eeafd5b4736","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَلَا يَخَافُ عُقْبَٰهَا","ayah_ref":"91:15"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000447/B001","root_001033/B008"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000447","role":"Prospective apprehension supplies the subject's possible exposure to a later challenger.","root":"خ و ف","source_ref":"91:15","source_word_indices":["2"]},{"branch_id":"B008","mapped_root_id":"root_001033","role":"Following up to question, claim, or reverse supplies an institutional rather than merely emotional aftermath.","root":"ع ق ب","source_ref":"91:15","source_word_indices":["3"]}],"changed_reading":{"after":"No later claimant, reviewer, or reverser is apprehended after the act.","before":"No bad consequence causes fear."},"confidence":"exploratory","focus_anchor":"The outcome noun at 91:15.3 remains rooted in what follows after, including a reviewing or reversing follower.","mechanism":"What comes afterward can be a claimant, review, or attempt at reversal; negated fear then describes an act performed without apprehension of later challenge.","model_id":"b03-no-follow-up-challenge"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b03-no-follow-up-challenge","source_type":"hft","support_id":"sup_3a894df59abb0a29a206","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَلَا يَخَافُ عُقْبَٰهَا","ayah_ref":"91:15"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000447/B005","root_001033/B011"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000447","role":"Visible manifestation shifts fear from an inner state to an outwardly readable sign.","root":"خ و ف","source_ref":"91:15","source_word_indices":["2"]},{"branch_id":"B011","mapped_root_id":"root_001033","role":"A remaining residue supplies the wake in which such a sign could persist.","root":"ع ق ب","source_ref":"91:15","source_word_indices":["3"]}],"changed_reading":{"after":"The event's wake leaves no visible residue of fear on the subject.","before":"The subject does not internally feel fear of the result."},"confidence":"exploratory","focus_anchor":"The negated fear at 91:15.2 and the remaining wake at 91:15.3 can both be read as observable traces.","mechanism":"Fear can manifest on a person, and an aftermath can be a residue; their pairing allows the clause to deny that the event leaves a legible mark of fear on the subject.","model_id":"b04-no-visible-fear-residue"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b04-no-visible-fear-residue","source_type":"hft","support_id":"sup_e7226e38b3b6f183e86f","trust":"legacy_unbound"}]}
</lane_packet_json>
