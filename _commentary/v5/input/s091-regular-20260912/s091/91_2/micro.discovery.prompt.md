# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **91:2**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s091-regular-20260912/s091/91_2/micro.discovery.json` and modify nothing
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
  "ayah_ref": "91:2",
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
{"branch_registry":[{"boundary":"Bu dal yalnızca yükseltiyi anlatır; boyun, yere serme, dökme ve öteki eş sesli anlamları kapsamaz.","branch_kind":"bare","branch_ref":"root_000185/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"küçük tepe veya yer kabartısı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yerden belirgin biçimde yükselen küçük tepeyi, tepeciği veya yer kabartısını belirtir."}}],"root_ar":"ت ل و","root_id":"root_000185","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çevresine göre yükselen küçük bir doğal yer biçiminin genel karşılığı olarak kullanılır.","boundary_detail":"Bu dal yalnızca yükseltiyi anlatır; boyun, yere serme, dökme ve öteki eş sesli anlamları kapsamaz.","branch_image_ar":"التل المرتفع","concept_gloss":"küçük tepe veya yer kabartısı","contextual_glosses":[{"applicability":"Bağlam yükseltinin küçük ve tek parça bir doğal tepe olduğunu gösterdiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Küçük ve çevresinden yükselen doğal yer biçimini korur."},"facet_ids":["F001"],"text":"tepecik","usage_role":"contextual"}],"definition":"Çevresindeki yerden yükselen, genellikle küçük tepe veya toprak kabartısıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yerden belirgin biçimde yükselen küçük tepeyi, tepeciği veya yer kabartısını belirtir."}],"identity_rationale":"Kaynak ifadesi, dalı çevresinden yükselen küçük bir tepe, yer kabartısı veya küçük tepecik olarak açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tepe, tepecik veya yüksekçe yer"}],"lexicalization_note":"Tanım yalın dal anlamıyla sınırlıdır ve başka kuruluşlara bağlı anlamları bu yükselti kavramına katmaz.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi; yayımlanan iki karşılaştırma yükseltinin genel kapsamını ve biçim sınırını en açık biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal daha çok küçük ve tepe görünüşlü yükseltiye gider; komşu dal ise yükselmiş araziyi daha genel biçimde adlandırır.","focus_only":"Odak dal küçük tepe ve küçük yer kabartısı görünümünü öne çıkarır.","gloss":"yüksek arazi","neighbor_only":"Komşu dal, boyut veya biçim sınırı koymadan her türlü yüksek araziyi kapsar.","neighbor_ref":"root_000537/B002","relation_type":"near_synonym","shared_zone":"Her ikisi de çevresindeki zeminden yükselen doğal bir yer parçasını anlatır."},{"boundary_match":"partial","distinction":"Komşu dal biçimi yuvarlaklıkla sınırlar; odak dalın çekirdeği ise küçük bir yükselti olmasıdır.","focus_only":"Odak dalda yuvarlaklık zorunlu değildir ve küçük yükseltiler genel olarak kapsanır.","gloss":"yuvarlak tepecik","neighbor_only":"Komşu dal yükseltinin yuvarlak biçimli olmasını ayrıca belirtir.","neighbor_ref":"root_001177/B004","relation_type":"near_synonym","shared_zone":"İki dal da çevresinden yükselen küçük bir yer biçimini anlatır."}],"source_phrase_ar":"التل معروف (maqayis); التل واحد التلال (sihah); التلال الروابي المخلوقة; التل من أصاغر الآكام (tahdhib); أصل التل المكان المرتفع (mufradat)","source_summary":"Kaynaklar, anlamın yükselmiş bir yer biçimi üzerinde birleştiğini; küçük tepeleri ve benzeri yer kabartılarını kapsadığını gösterir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"التل والتلال والروابي وصغار الآكام والمكان المرتفع","what_is_not_ar":"الصرع والإسقاط والصب والقلق والرقبة"},"support_links":[]},{"boundary":"Bu anatomik anlam, aynı kökün tepe, yere serme, dökme ve güç bildiren dallarından ayrıdır.","branch_kind":"bare","branch_ref":"root_000185/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"boyun","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başın altında bulunan ve başı gövdeye bağlayan boyun bölgesini belirtir."}}],"root_ar":"ت ل و","root_id":"root_000185","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Baş ile gövde arasındaki anatomik bölgeyi adlandıran bütün olağan bağlamlarda kullanılır.","boundary_detail":"Bu anatomik anlam, aynı kökün tepe, yere serme, dökme ve güç bildiren dallarından ayrıdır.","branch_image_ar":"التليل عنق","concept_gloss":"boyun","contextual_glosses":[{"applicability":"Anatomik sınırın açıkça belirtilmesi gereken açıklayıcı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başla gövde arasındaki anatomik bölgeyi açıkça korur."},"facet_ids":["F001"],"text":"boyun bölgesi","usage_role":"explanatory"}],"definition":"Baş ile gövdeyi birleştiren vücut bölümü olan boyundur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başın altında bulunan ve başı gövdeye bağlayan boyun bölgesini belirtir."}],"identity_rationale":"Kaynak ifadesi dalın tek ve doğrudan anlamını boyun olarak verir; saç tutamına ilişkin söz yalnızca betimleyici bir bağlamdır.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"boyun"}],"lexicalization_note":"Tanım yalın anatomik anlamı verir ve belirli bir söz kuruluşuna ya da komşu vücut bölgesine genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; öteki kartlar boyuna komşu bölgeleri veya ilgisiz kök dallarını gösterdiği için yalnızca doğrudan boyun karşılaştırması yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Gönderim örtüşür; ancak komşu dalın kullanımı belirli bir tutma anlatımına bağlıyken odak dal yalın anatomik addır.","focus_only":"Odak dal boynu herhangi bir eylem veya söz kalıbıyla sınırlamadan adlandırır.","gloss":"boyun","neighbor_only":"Komşu dal boyun anlamını özellikle birini boynundan tutma sözünde taşır.","neighbor_ref":"root_000622/B008","relation_type":"near_synonym","shared_zone":"Her iki dalın gönderimi insanın boyun bölgesidir."}],"source_phrase_ar":"التليل العنق (maqayis); التليل العنق (sihah); التليل العنق; بعنق ذي خصل من الشعر (tahdhib); والتليل العنق (mufradat)","source_summary":"Kaynakların tümü anatomik karşılığı boyun olarak verir; ek betimleme, boyundaki saç tutamlı görünüşe örnek oluşturur.","sources":["MQ","SI","TA","MU"],"what_is_ar":"التليل بمعنى العنق","what_is_not_ar":"التل المرتفع والصرع والرمح المتل"},"support_links":[]},{"boundary":"Dal eylemin kendisidir; dökme ve teslim etme eylemlerini ya da bu işte kullanılan mızrağın niteliğini kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000185/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"yere serme veya yüzüstü düşürme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birini gücünü yitirterek yere sermeyi veya düşürmeyi belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli kuruluşta düşürülen kişinin alnı veya yüzü üzerine kapanması özellikle belirtilir."}}],"root_ar":"ت ل و","root_id":"root_000185","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem genel yere serme eylemini hem de alın ya da yüz üzerine düşürme biçimini birlikte temsil eder.","boundary_detail":"Dal eylemin kendisidir; dökme ve teslim etme eylemlerini ya da bu işte kullanılan mızrağın niteliğini kapsamaz.","branch_image_ar":"تله صرعه","concept_gloss":"yere serme veya yüzüstü düşürme","contextual_glosses":[{"applicability":"Düşüş yönünün belirtilmediği genel devirmeyi anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Birini etkisiz bırakıp yere düşürme çekirdeğini korur."},"facet_ids":["F001"],"text":"yere serdi","usage_role":"general"},{"applicability":"Kişinin alnı ya da yüzü üzerine kapaklandığı özel kuruluşta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Düşürme eylemini ve düşüşün yüz tarafına yönelmesini birlikte korur."},"facet_ids":["F001","F002"],"text":"yüzüstü düşürdü","usage_role":"contextual"}],"definition":"Bir insanı ya da canlıyı yere sermek veya düşürmektir; belirli kuruluşta onu alnı ya da yüzü üzerine kapaklamak anlamına gelir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birini gücünü yitirterek yere sermeyi veya düşürmeyi belirtir."},{"facet_id":"F002","role":"specialization","statement":"Belirli kuruluşta düşürülen kişinin alnı veya yüzü üzerine kapanması özellikle belirtilir."}],"identity_rationale":"Kaynak ifadesi birini yere sermeyi veya düşürmeyi çekirdek anlam olarak, alın ya da yüz üzerine düşürmeyi ise belirgin bir gerçekleşme biçimi olarak destekler.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yere serdi veya düşürdü"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"alnı ya da yüzü üzerine düşürdü"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yere serilmiş kimse"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yere serilmiş kimse"}],"lexicalization_note":"Tanım yalın yere serme anlamını, alın veya yüz üzerine düşürme kuruluşundan ayırarak birlikte gösterir.","neighbor_coverage_note":"Bütün adaylar incelendi; yayımlanan iki yakın anlamlı dal, genel yere serme ile yüzüstü düşürme sınırlarını en yararlı biçimde karşılaştırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın genel çekirdeği yere sermedir; komşu dal ise ters çevirme ve yüzüstü bırakma sonucunu daha geniş nesne kapsamıyla öne çıkarır.","focus_only":"Odak dalın yalın biçimi düşüş yönünü zorunlu kılmadan birini yere sermeyi de kapsar.","gloss":"yüzüstü devirmek","neighbor_only":"Komşu dal kapları ters çevirmeye kadar uzanır ve yüz üzerine çevirme sonucunu çekirdek sayar.","neighbor_ref":"root_001278/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir insanı veya canlıyı yüz tarafına doğru düşürme bağlamında örtüşür."},{"boundary_match":"partial","distinction":"Komşu dal yere atma ya da çalma biçimine odaklanır; odak dal ise daha genel sermeyi ve yüz tarafına düşürme kuruluşunu birlikte barındırır.","focus_only":"Odak dal belirli kuruluşta alın veya yüz üzerine kapaklanmayı ayrıca kodlayabilir.","gloss":"yere çalmak","neighbor_only":"Komşu dal taşıyıp yere atma ve yere vurma biçimlerini açıkça kapsar.","neighbor_ref":"root_000249/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişiyi güç kullanarak yere sermeyi anlatır."}],"source_phrase_ar":"فتله أي صرعه; وتله للجبين (maqayis); وتله للجبين أي صرعه; كبه لوجهه (sihah); معنى تله صرعه; كبه لفيه (tahdhib); تله للجبين أسقطه على التل; أسقطه على تليله (mufradat)","source_summary":"Kaynaklar yere serme ve düşürme çekirdeğinde birleşir; anlatımın özel biçiminde kişinin alın ya da yüz tarafı üzerine kapaklanması öne çıkar.","sources":["MQ","SI","TA","MU"],"what_is_ar":"تله وصرعه وأسقطه وكبه للجبين أو للوجه","what_is_not_ar":"الصب والدفع والرمح الذي يصرع به والتل المرتفع"},"support_links":[]},{"boundary":"Dökme yalın çekirdektir; ele verme ve teslim etme anlamları yalnızca belirtilen kuruluşlarda geçerlidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000185/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"dökme; ele verme veya teslim etme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir maddeyi bulunduğu yerden akıtarak veya boşaltarak dökmeyi belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"El bildiren kuruluşlarda bir şeyi o ele dökmeyi, ulaştırmayı veya teslim etmeyi belirtir."}}],"root_ar":"ت ل و","root_id":"root_000185","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın dökme çekirdeğiyle ele yönelen kuruluş anlamlarının birlikte özetlenmesi gerektiğinde kullanılır.","boundary_detail":"Dökme yalın çekirdektir; ele verme ve teslim etme anlamları yalnızca belirtilen kuruluşlarda geçerlidir.","branch_image_ar":"تل صب ودفع","concept_gloss":"dökme; ele verme veya teslim etme","contextual_glosses":[{"applicability":"Bir maddenin boşaltılması veya akıtılması anlatıldığında yalın eylem karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Maddenin bir yerden boşaltılması biçimindeki yalın eylemi korur."},"facet_ids":["F001"],"text":"döktü","usage_role":"general"},{"applicability":"Bir şeyin başka birinin eline ulaştırıldığı veya teslim edildiği kuruluşta uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesnenin alıcının eline yöneltilip teslim edilmesini korur."},"facet_ids":["F002"],"text":"eline verdi","usage_role":"contextual"}],"definition":"Yalın kullanımda bir şeyi dökmektir. Belirli kuruluşlarda bir şeyi birinin eline dökmeyi, ona vermeyi veya teslim etmeyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir maddeyi bulunduğu yerden akıtarak veya boşaltarak dökmeyi belirtir."},{"facet_id":"F002","role":"specialization","statement":"El bildiren kuruluşlarda bir şeyi o ele dökmeyi, ulaştırmayı veya teslim etmeyi belirtir."}],"identity_rationale":"Kaynak ifadesi hem yalın dökme eylemini hem de bir şeyi birinin eline dökme, verme veya teslim etme kuruluşlarını destekler; bunlar tek bir sınırsız itme anlamında birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"eline verdi veya teslim etti"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"döktü"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bir dökümlük miktar veya dökülen şey"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"elime döküldü veya bırakıldı"}],"lexicalization_note":"Tanım yalın dökme anlamını korur, ele dökme ve birine teslim etme anlamlarını ise kuruluşla sınırlı ayrı yüzler olarak verir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen karşılaştırmalar dalın iki ayrı yüzünü, dökme ile alıcıya teslim etmeyi, doğrudan sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal akıtılan madde ve akış olayına genişler; odak dal ise ayrıca ele yönelen verme kuruluşlarına sahiptir.","focus_only":"Odak dal belirli kuruluşlarda ele verme ve teslim etme anlamını da taşır.","gloss":"akıtıp dökmek","neighbor_only":"Komşu dal kan, gözyaşı ve erimiş madde gibi sıvıları akıtma alanını ayrıntılı biçimde kapsar.","neighbor_ref":"root_000714/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir maddeyi bulunduğu yerden akıtarak dökme eyleminde örtüşür."},{"boundary_match":"partial","distinction":"Odak dalın teslim anlamı el bildiren özel kuruluşa bağlıdır; komşu dal ise alıcıya ulaştırmayı genel eylem olarak kodlar.","focus_only":"Odak dal yalın kullanımda doğrudan dökme eylemini de belirtir.","gloss":"birine ulaştırmak","neighbor_only":"Komşu dal bir şeyi alıcıya ulaştırma ve verme eylemini genel olarak kapsar.","neighbor_ref":"root_000480/B002","relation_type":"near_neighbor","shared_zone":"Bir nesnenin başka bir kişiye verilip teslim edildiği bağlamda iki dal kesişir."}],"source_phrase_ar":"تل إذا صب; التلة الصبة; فتلت في يدي معناه فصبت في يدي; تللت في يديه أي دفعت إليه سلما","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, dökme eyleminin yanı sıra bir şeyi ele boşaltma ve birine teslim etme kuruluşlarını da verir."}],"source_summary":"Dalın tek kaynaklı tanıklığı, yalın dökme anlamı ile ele yönelen dökme ve teslim etme kuruluşlarını birlikte kaydeder.","sources":["TA"],"what_is_ar":"تل بمعنى صب وتلت في اليد بمعنى صبت أو دفعت إليه","what_is_not_ar":"الصرع والسقوط والتل المرتفع والتلة البقية"},"support_links":[]},{"boundary":"Sarsıp huzursuz etme çekirdeği ile ağır sıkıntılar bildiren çoğul kullanım tanımda ayrı tutulur.","branch_kind":"bare","branch_ref":"root_000185/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"sarsıp huzursuz etme; ağır sıkıntılar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi sarsmayı, yerinden oynatmayı ve huzursuz duruma getirmeyi belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Çoğul ad kullanımında insanı sarsan ağır güçlükleri ve sıkıntıları belirtir."}}],"root_ar":"ت ل و","root_id":"root_000185","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel veya ruhsal sarsma çekirdeğiyle bunun ağır güçlükler uzantısının birlikte gösterilmesinde uygundur.","boundary_detail":"Sarsıp huzursuz etme çekirdeği ile ağır sıkıntılar bildiren çoğul kullanım tanımda ayrı tutulur.","branch_image_ar":"التلتلة إقلاق واضطراب","concept_gloss":"sarsıp huzursuz etme; ağır sıkıntılar","contextual_glosses":[{"applicability":"Bir şeyin hareket ettirilip düzeninin veya huzurunun bozulduğu eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sarsma, oynatma ve huzur bozma eylemlerini birlikte korur."},"facet_ids":["F001"],"text":"sarsıp huzursuz etti","usage_role":"general"},{"applicability":"Çoğul adın insanı zorlayan ağır güçlükleri anlattığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çoğul kullanımın ağır ve sarsıcı güçlükler anlamını korur."},"facet_ids":["F002"],"text":"ağır sıkıntılar","usage_role":"contextual"}],"definition":"Bir şeyi sarsarak hareket ettirmek ve huzurunu bozmak anlamına gelir; çoğul bir kullanımda ağır sıkıntıları da belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi sarsmayı, yerinden oynatmayı ve huzursuz duruma getirmeyi belirtir."},{"facet_id":"F002","role":"extension","statement":"Çoğul ad kullanımında insanı sarsan ağır güçlükleri ve sıkıntıları belirtir."}],"identity_rationale":"Kaynak ifadesi sarsma, huzursuz etme ve hareket ettirme çekirdeğini destekler; ağır sıkıntılar anlamı ise bu çekirdekle eş düzeyde fiziksel bir hareket değil, ayrı bir uzantıdır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sarsma, oynatma ve huzursuz etme"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"sarstı, oynattı ve huzursuz etti"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"ağır sıkıntılar"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"huzursuz etme ve hareket"}],"lexicalization_note":"Tanım yalın dalın sarsma anlamını esas alır ve ağır sıkıntılar uzantısını buna bağımlı ayrı bir yüz olarak gösterir.","neighbor_coverage_note":"Tüm aday kartlar gözden geçirildi; seçilen iki dal sarsma çekirdeğine en yakın olanlardır, ötekiler yalnızca sonuç veya aynı olay alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ağır sıkıntılar adını ayrıca taşırken komşu dal sarsıntının korku ve kaygı sonuçlarını daha geniş kapsar.","focus_only":"Odak dalın çoğul biçimi ağır sıkıntıları yerleşik bir ad anlamı olarak belirtir.","gloss":"sarsıntı ve tedirginlik","neighbor_only":"Komşu dal korku, ürküntü ve genel kaygı sonuçlarına daha açık biçimde genişler.","neighbor_ref":"root_000641/B008","relation_type":"near_synonym","shared_zone":"İki dal da sarsma, hareket, düzen bozma ve huzursuzluk alanında büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Komşu dal fiziksel titreşme ve çalkalanmaya yoğunlaşır; odak dal huzur bozma ile sıkıntı uzantısını da taşır.","focus_only":"Odak dal huzursuz etme ve ağır sıkıntılar uzantısını da içerir.","gloss":"sarsıp titreştirmek","neighbor_only":"Komşu dal deniz ve yer gibi varlıkların çalkalanıp titreşmesini özellikle kapsar.","neighbor_ref":"root_000541/B001","relation_type":"near_synonym","shared_zone":"Her ikisi de bir şeyi hareket ettirerek sarsma ve dengesini bozma eylemini anlatır."}],"source_phrase_ar":"التلتلة الإقلاق (maqayis); تلتله أي زعزعه وأقلقه وزلزله; التلاتل الشدائد (sihah); التليلة الإقلاق والحركة; البلابل والتلاتل الشدائد (tahdhib)","source_summary":"Kaynaklar sarsma ve huzursuz etme çekirdeğinde birleşir; bazı biçimler hareketi, çoğul biçim ise ağır sıkıntıları anlatır.","sources":["MQ","SI","TA"],"what_is_ar":"التلتلة والتليلة بمعنى الإقلاق والحركة والزعزعة والزلزلة والتلاتل للشدائد","what_is_not_ar":"الصب والمشربة والصرع والعلو"},"support_links":[]},{"boundary":"Dal yere serme eylemini değil, güçlü ve iri olma niteliğini ve bu nitelikteki mızrağı adlandırır.","branch_kind":"mixed_non_bare","branch_ref":"root_000185/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"iri ve güçlü oluş; kalın, sağlam mızrak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi veya nesne için irilik, sertlik, dayanıklılık ve güç niteliğini belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kalın ve güçlü olup rakibi yere sermede kullanılan mızrağı özellikle belirtir."}}],"root_ar":"ت ل و","root_id":"root_000185","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel nitelikle bunun kişi ve mızrak üzerindeki özel gerçekleşmelerinin birlikte özetlenmesinde kullanılır.","boundary_detail":"Dal yere serme eylemini değil, güçlü ve iri olma niteliğini ve bu nitelikteki mızrağı adlandırır.","branch_image_ar":"المتل شدة وغلظ","concept_gloss":"iri ve güçlü oluş; kalın, sağlam mızrak","contextual_glosses":[{"applicability":"Bir kişinin kalın yapılı, sert ve güçlü olduğu anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişideki irilik, sertlik ve güç niteliklerini korur."},"facet_ids":["F001"],"text":"iri ve güçlü","usage_role":"contextual"},{"applicability":"Niteliğin rakibi yere sermede kullanılabilen güçlü bir mızrağa uygulandığı bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mızrağın kalınlığını, sağlamlığını ve güçlü kullanımını korur."},"facet_ids":["F001","F002"],"text":"kalın ve sağlam mızrak","usage_role":"contextual"}],"definition":"Bir kimsenin veya nesnenin iri, sert ve güçlü oluşunu belirtir. Özellikle kalın, sağlam ve yere sermede kullanılan bir mızrağı adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi veya nesne için irilik, sertlik, dayanıklılık ve güç niteliğini belirtir."},{"facet_id":"F002","role":"specialization","statement":"Kalın ve güçlü olup rakibi yere sermede kullanılan mızrağı özellikle belirtir."}],"identity_rationale":"Kaynak ifadesi sertlik, güç ve irilik niteliğini hem kişi hem mızrak için verir; yere sermede kullanılan mızrak bu niteliğin özel nesneleşmesidir.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"iri ve güçlü; kalın, sağlam mızrak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kalın, sağlam ve yere seren mızrak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"iri yapılı ve güçlü adam"}],"lexicalization_note":"Tanım genel güç ve irilik niteliğini, kişi ile mızrağa bağlı özel kullanımlardan ayırarak korur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen kartlar genel sertlik-güç niteliğini ve insan bedenindeki irilik sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel bir nitelik adıdır; odak dal bu niteliği iri kişiye ve belirli işlevdeki kalın mızrağa bağlar.","focus_only":"Odak dal kişi ve özellikle yere sermede kullanılan kalın mızrakla bağlantılıdır.","gloss":"sert ve güçlü","neighbor_only":"Komşu dal sertlik ve güç niteliğini nesne türünü sınırlamadan, kimi aktarımda uzunlukla birlikte verir.","neighbor_ref":"root_000188/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir varlığın sert, dayanıklı ve güçlü oluşunu anlatır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeğinde kısalık yoktur ve nesnelere de uzanır; komşu dal kısa, toplu insan yapısına özgüdür.","focus_only":"Odak dal mızrağa uygulanabilir ve yere sermeye yarayan araç özelleşmesi taşır.","gloss":"kısa ve tıknaz","neighbor_only":"Komşu dal kişide kısalık ve bedenin toplu oluşunu ayrıca zorunlu kılar.","neighbor_ref":"root_001315/B008","relation_type":"near_neighbor","shared_zone":"İki dal insan bedeninde irilik, kalınlık ve güçlü yapı alanında kesişir."}],"source_phrase_ar":"المتل الرمح الذي يصرع به (maqayis); المتل الشديد; رمح متل يتل به (sihah); رجل متل إذا كان غليظا شديدا; رمح متل غليظ شديد (tahdhib); المتل الرمح الذي يتل به (mufradat)","source_summary":"Kaynaklar sertlik ve güç niteliğinde birleşir; insan için iri ve güçlü yapı, mızrak içinse kalınlık, sağlamlık ve yere serme işlevi belirtilir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"المتل للرجل أو الرمح الشديد الغليظ والرمح الذي يصرع به","what_is_not_ar":"الفعل صرعه نفسه والتل المرتفع والتلتلة الحركة"},"support_links":[]},{"boundary":"Dal her türlü bardağı değil, malzemesi ve içme işlevi belirtilmiş özel kabı adlandırır.","branch_kind":"bare","branch_ref":"root_000185/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"hurma salkımı kabuğundan içki kabı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hurma salkımının dış kabuğundan yapılmış bir içme kabını belirtir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kabın adı, içindekinin boğaza dökülerek içilmesiyle açıklanır."}}],"root_ar":"ت ل و","root_id":"root_000185","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Malzemesi hurma salkımı kabuğu ve işlevi içecek içmek olan özel kabın genel karşılığıdır.","boundary_detail":"Dal her türlü bardağı değil, malzemesi ve içme işlevi belirtilmiş özel kabı adlandırır.","branch_image_ar":"التلتلة مشربة","concept_gloss":"hurma salkımı kabuğundan içki kabı","contextual_glosses":[{"applicability":"Kabın yapıldığı malzeme ile içki içme işlevinin açıklanması gereken bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Özel malzemeyi ve içme kabı işlevini açıkça korur."},"facet_ids":["F001"],"text":"hurma kabuğundan içki tası","usage_role":"explanatory"}],"definition":"Hurma salkımının dış kabuğundan yapılan ve özellikle mayalanmış içecek içmekte kullanılan küçük kaptır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hurma salkımının dış kabuğundan yapılmış bir içme kabını belirtir."},{"facet_id":"F002","role":"associated_use","statement":"Kabın adı, içindekinin boğaza dökülerek içilmesiyle açıklanır."}],"identity_rationale":"Kaynak ifadesi genel bir içki kabından daha dar olarak, hurma salkımının dış kabuğundan yapılan ve içecek içilen bir kabı belirtir.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"hurma salkımı kabuğundan içki kabı"}],"lexicalization_note":"Tanım yalın adın özel kap anlamıyla sınırlıdır ve bunu genel kap ya da genel dökme anlamına genişletmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel içme kabı kartı en yakın karşılaştırmayı sağlar, öteki kaplar malzeme veya işlev bakımından daha uzaktır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel kadeh ve içecek kapsamındadır; odak dal malzemesi hurma salkımı kabuğu olan özel bir kaptır.","focus_only":"Odak dal kabın hurma salkımı kabuğundan yapılmasını ve özel içme kullanımını gerektirir.","gloss":"içeceğiyle birlikte kadeh","neighbor_only":"Komşu dal herhangi bir kadehi, içindeki içecekle birlikte veya tek başına genel biçimde adlandırabilir.","neighbor_ref":"root_001277/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da içecek taşımaya ve içmeye yarayan bir kabı anlatır."}],"source_phrase_ar":"التلتلة مشربة تتخذ من قيقاءة الطلع (sihah); التلتلة قشر الطلعة يشرب فيه النبيذ; منه قيل للمشربة تلتلة لأنه يصب ما فيها في الحلق (tahdhib)","source_summary":"Kaynaklar kabın hurma salkımının dış kabuğundan yapıldığı ve içki içmede kullanıldığı konusunda birleşir; adlandırma dökerek içmeyle ilişkilendirilir.","sources":["SI","TA"],"what_is_ar":"التلتلة مشربة أو قشر طلعة يشرب فيه النبيذ","what_is_not_ar":"التلتلة بمعنى الإقلاق والشدائد والصب نفسه"},"support_links":[]},{"boundary":"Bu anlam bağımsız bir yalın ad değil, kötü durum bildiren sabit kuruluşla sınırlıdır.","branch_kind":"non_bare","branch_ref":"root_000185/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"kötü durumda olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin içinde bulunduğu durumun kötü ve güç olduğunu belirtir."}}],"root_ar":"ت ل و","root_id":"root_000185","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kişinin elverişsiz koşulunu bildiren sağlanmış söz kuruluşunun karşılığı olarak kullanılır.","boundary_detail":"Bu anlam bağımsız bir yalın ad değil, kötü durum bildiren sabit kuruluşla sınırlıdır.","branch_image_ar":"تلة سوء حالة سوء","concept_gloss":"kötü durumda olma","contextual_glosses":[{"applicability":"Kuruluş bir kişinin içinde bulunduğu olumsuz durumu yüklem olarak bildirdiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin olumsuz bir durumda bulunmasını doğal cümle biçiminde korur."},"facet_ids":["F001"],"text":"kötü durumdaydı","usage_role":"contextual"}],"definition":"Belirli bir söz kuruluşunda, birinin kötü veya elverişsiz bir durumda bulunmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin içinde bulunduğu durumun kötü ve güç olduğunu belirtir."}],"identity_rationale":"Kaynak ifadesi yalnızca belirli bir söz kuruluşunda kişinin kötü, güç veya elverişsiz bir durumda bulunmasını bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kötü durumda olma"}],"lexicalization_note":"Tanım yalnızca kötü durum bildiren sağlanmış söz kuruluşuna bağlıdır ve yalın köke genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan kartlar genel durum kavramı ile kötü ve güç durum alanındaki en yakın sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hem olumsuz değer taşır hem belirli kuruluşa bağlıdır; komşu dal durum kavramını daha genel ve değer bakımından açık bırakır.","focus_only":"Odak dal yalnızca kötü durumu bildiren belirli kuruluşa bağlıdır.","gloss":"içinde bulunulan durum","neighbor_only":"Komşu dal bir şeyin içinde bulunduğu durumu iyi veya kötü olabilen genel bir kavram olarak kapsar.","neighbor_ref":"root_000067/B007","relation_type":"near_synonym","shared_zone":"İki dal da bir kişinin veya şeyin içinde bulunduğu hali anlatır."},{"boundary_match":"partial","distinction":"Komşu dal güçlüğü ve kıtlık yıllarını genişçe kapsar; odak dal kişinin kötü durumda oluşuna bağlı dar bir anlatımdır.","focus_only":"Odak dal belirli bir kişinin kötü durumda bulunmasını kuruluş içinde bildirir.","gloss":"kötü ve güç durum","neighbor_only":"Komşu dal ağır yıllar ve kuraklık gibi toplumsal veya zamansal güçlükleri de kapsar.","neighbor_ref":"root_000321/B010","relation_type":"near_synonym","shared_zone":"Her iki dal da olumsuz, zorlayıcı bir durumun varlığını anlatır."}],"source_phrase_ar":"هو بتلة سوء; ببيئة سوء; بحالة سوء","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynaklı kayıt, bu kuruluşun kişinin kötü bir durumda bulunmasını anlattığını belirtir."}],"source_summary":"Tek tanıklık, kuruluşu kötü durumda veya kötü koşullar içinde bulunma anlamıyla açıklar.","sources":["SI"],"what_is_ar":"تلة سوء بمعنى حالة سوء","what_is_not_ar":"الضجعة والكسل وبقية الدين والبلة"},"support_links":[]},{"boundary":"Dal kötü durum, borç kalanı, ağız ıslaklığı ve dökülen miktar anlamlarından ayrıdır.","branch_kind":"bare","branch_ref":"root_000185/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"uzanma ya da tembellik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bedenin dinlenmek üzere uzanıp yatması anlamını taşır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir işe yönelmede isteksizlik ve ağır davranma biçimindeki tembelliği belirtir."}}],"root_ar":"ت ل و","root_id":"root_000185","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın adın kayıtlı iki anlamını kısa biçimde birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Dal kötü durum, borç kalanı, ağız ıslaklığı ve dökülen miktar anlamlarından ayrıdır.","branch_image_ar":"التلة ضجعة وكسل","concept_gloss":"uzanma ya da tembellik","contextual_glosses":[{"applicability":"Söz bedensel olarak yere veya yatağa uzanmayı anlattığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedenin uzanmış duruma geçmesi anlamını korur."},"facet_ids":["F001"],"text":"uzanıp yatma","usage_role":"contextual"},{"applicability":"Söz bir işe karşı isteksizliği ve ağır davranmayı anlattığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşe yönelmede isteksizlik ve ağır davranma anlamını korur."},"facet_ids":["F002"],"text":"tembellik","usage_role":"contextual"}],"definition":"Uzanıp yatmayı veya bir işe karşı isteksizlik ve ağır davranma biçimindeki tembelliği belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bedenin dinlenmek üzere uzanıp yatması anlamını taşır."},{"facet_id":"F002","role":"source_variant","statement":"Bir işe yönelmede isteksizlik ve ağır davranma biçimindeki tembelliği belirtir."}],"identity_rationale":"Kaynak ifadesi aynı ad için uzanıp yatma ile tembellik anlamlarını birlikte verir; ikisi tek bir hareket olarak kaynaştırılmadan ayrı yüzler halinde korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"uzanıp yatma; tembellik"}],"lexicalization_note":"Tanım yalın adın iki kayıtlı anlamını, uzanıp yatma ile tembelliği, birbirine indirgemeden verir.","neighbor_coverage_note":"Tüm adaylar incelendi; seçilen iki kart dalın iki ayrı anlamını doğrudan karşılar, diğerleri yatış biçimi veya aynı kökün ilgisiz dallarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Uzanma yüzünde örtüşürler; odak dalın ayrıca bağımsız bir tembellik yüzü vardır.","focus_only":"Odak dal uzanmanın yanı sıra tembellik anlamını da taşır.","gloss":"uzanıp yatmak","neighbor_only":"Komşu dal yalnızca uzanıp yatma eylemini belirtir ve tembellik anlamı taşımaz.","neighbor_ref":"root_000729/B008","relation_type":"near_synonym","shared_zone":"İki dal bedenin uzanmış yatış durumuna geçmesini anlatır."},{"boundary_match":"partial","distinction":"Tembellik yüzleri yakındır; komşu dal görevden geri kalma sürecini ayrıntılandırırken odak dal ayrıca uzanmayı adlandırır.","focus_only":"Odak dal bedensel uzanıp yatma anlamını da taşır.","gloss":"tembellik ve ağırdan alma","neighbor_only":"Komşu dal yapılması gereken işi tamamlamaktan geri durma ve ağırdan alma ayrıntılarını kapsar.","neighbor_ref":"root_001299/B001","relation_type":"near_synonym","shared_zone":"İki dal bir işe karşı isteksizlik ve ağır davranma anlamında örtüşür."}],"source_phrase_ar":"والتلة الضجعة والكسل","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynaklı kayıt, uzanma ile tembelliği aynı biçimin iki ayrı anlamı olarak verir."}],"source_summary":"Tek tanıklık aynı biçime iki anlam bağlar: uzanıp yatma ve bir işe karşı isteksiz, ağır davranma.","sources":["TA"],"what_is_ar":"التلة بمعنى الضجعة والكسل","what_is_not_ar":"تلة السوء وبقية الدين والبلة والصبة"},"support_links":[]},{"boundary":"Bu dal genel bir kalanı değil, özellikle borcun henüz kapanmamış bölümünü belirtir.","branch_kind":"bare","branch_ref":"root_000185/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"borçtan kalan tutar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Borç toplamından geriye kalan ve hâlâ ödenmesi gereken miktarı belirtir."}}],"root_ar":"ت ل و","root_id":"root_000185","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir borcun henüz ödenmemiş ve kapanmamış bölümünü adlandırmak için kullanılır.","boundary_detail":"Bu dal genel bir kalanı değil, özellikle borcun henüz kapanmamış bölümünü belirtir.","branch_image_ar":"التلة بقية دين","concept_gloss":"borçtan kalan tutar","contextual_glosses":[{"applicability":"Ödemenin ardından hâlâ borç olarak duran miktarın söylendiği bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geriye kalan ve ödenmesi gereken borç miktarını korur."},"facet_ids":["F001"],"text":"kalan borç","usage_role":"contextual"}],"definition":"Bir borcun ödenmemiş veya kapanmamış olarak geride kalan bölümüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Borç toplamından geriye kalan ve hâlâ ödenmesi gereken miktarı belirtir."}],"identity_rationale":"Kaynak ifadesi dalı, ödenmiş veya ele alınmış bir borçtan geriye kalan bölüm olarak doğrudan tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"borçtan kalan bölüm"}],"lexicalization_note":"Tanım yalın adın borca özgü kalan bölüm anlamını korur ve bunu başka tür kalıntılara genellemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel kalan anlamıyla borç kalanı arasındaki kapsam farkını en doğrudan bu kart gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Borç bağlamında örtüşürler; komşu dalın kapsamı başka tür kalıntılara da açılırken odak dal borçla sınırlıdır.","focus_only":"Odak dal yalnızca borçtan geriye kalan bölümü belirtir.","gloss":"geriye kalan bölüm","neighbor_only":"Komşu dal borç kalanı yanında herhangi bir şeyden arta kalan bölümü de kapsar.","neighbor_ref":"root_000615/B006","relation_type":"near_synonym","shared_zone":"İki dal da borcun henüz kapanmamış kalan bölümünü adlandırabilir."}],"source_phrase_ar":"والتلة بقية الدين","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynaklı kayıt, anlamı özellikle borcun geriye kalan bölümüyle sınırlar."}],"source_summary":"Tek tanıklık, sözü borçtan geriye kalan ve henüz kapanmamış bölüm anlamında verir.","sources":["TA"],"what_is_ar":"التلة بمعنى بقية الدين","what_is_not_ar":"الصبة والضجعة والكسل والبلة"},"support_links":[]},{"boundary":"Anlam ağızdaki nemle sınırlıdır; tükürme, kan, el sertliği veya genel yer ıslaklığı değildir.","branch_kind":"non_bare","branch_ref":"root_000185/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"ağızdaki ıslaklık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ağız içini ıslak tutan nemi veya hafif ıslaklığı belirtir."}}],"root_ar":"ت ل و","root_id":"root_000185","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca ağız içinde bulunan nemi bildiren sağlanmış kuruluşun karşılığı olarak kullanılır.","boundary_detail":"Anlam ağızdaki nemle sınırlıdır; tükürme, kan, el sertliği veya genel yer ıslaklığı değildir.","branch_image_ar":"التلة بلة في الفم","concept_gloss":"ağızdaki ıslaklık","contextual_glosses":[{"applicability":"Bir kişinin ağzında bulunan hafif ıslaklıktan söz edilen cümlede uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nemin ağız içinde bulunması ve hafif ıslaklık olması anlamını korur."},"facet_ids":["F001"],"text":"ağzındaki nem","usage_role":"contextual"}],"definition":"Belirli bir söz kuruluşunda ağız içinde bulunan ıslaklık veya nemdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ağız içini ıslak tutan nemi veya hafif ıslaklığı belirtir."}],"identity_rationale":"Kaynak ifadesi belirli kuruluşta ağız içindeki ıslaklığı veya nemi anlatır ve bunu genel ıslaklık sözüyle açıklar.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"ağızdaki nem veya ıslaklık"}],"lexicalization_note":"Tanım ağız bildiren sağlanmış kuruluşa bağlıdır ve yalın biçime ya da genel nem alanına genişletilmez.","neighbor_coverage_note":"Tüm aday kartlar değerlendirildi; genel ıslaklık dalı en yakın kapsam karşılaştırmasını verir, ötekiler farklı maddeleri veya ağızdan çıkış eylemlerini anlatır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yer ve kuruluş bakımından ağızla sınırlıdır; komşu dal ise genel ıslaklık ve nem alanına yayılır.","focus_only":"Odak dal belirli bir kuruluşta yalnızca ağız içindeki ıslaklığı belirtir.","gloss":"ıslaklık ve nem","neighbor_only":"Komşu dal su, çiy, nemli rüzgâr ve kap içindeki su gibi çok çeşitli ıslaklık türlerini kapsar.","neighbor_ref":"root_000152/B001","relation_type":"near_synonym","shared_zone":"İki dal ağız veya boğaz çevresindeki nemi anlatan bağlamda örtüşebilir."}],"source_phrase_ar":"ما هذه التلة بفيك أي البلة; التلل والبلل والتلة والبلة شيء واحد","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynaklı kayıt, anlamı ağızda bulunan nem veya hafif ıslaklık olarak sınırlar."}],"source_summary":"Tek tanıklık, kuruluşu ağız içindeki ıslaklıkla açıklar ve ilgili iki ıslaklık adını aynı anlam alanında gösterir.","sources":["TA"],"what_is_ar":"التلة والبلة بمعنى البلل في الفم","what_is_not_ar":"الصبة وبقية الدين والضجعة والكسل"},"support_links":[]},{"boundary":"Dal sapma kavramının kendisi değil, o kavrama eşlik eden uyaklı ve anlamı bağımsız olmayan söz tekrarıdır.","branch_kind":"non_bare","branch_ref":"root_000185/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"sapma sözünde uyaklı pekiştirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Önceki sözle uyak kurarak ona sesçe eşlik eder ve anlatımı pekiştirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kullanımı sapma ve yanlış yola gitme bildiren sağlanmış söz dizileriyle sınırlıdır."}}],"root_ar":"ت ل و","root_id":"root_000185","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca sapma bildiren sağlanmış söz dizilerinde bağımsız anlam taşımayan eşlikçi öğeyi açıklar.","boundary_detail":"Dal sapma kavramının kendisi değil, o kavrama eşlik eden uyaklı ve anlamı bağımsız olmayan söz tekrarıdır.","branch_image_ar":"التلالة إتباع في الضلال","concept_gloss":"sapma sözünde uyaklı pekiştirme","contextual_glosses":[{"applicability":"Kişi bildiren ikili sözde ikinci öğenin sesçe pekiştirme etkisi doğal Türkçeyle verildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sapma anlamını pekiştiren ancak yeni bir kavram eklemeyen işlevi korur."},"facet_ids":["F001","F002"],"text":"büsbütün sapmış","usage_role":"contextual"},{"applicability":"Soyut adların sıralandığı sözde uyaklı yoğunlaştırmayı doğal biçimde aktarmak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Soyut sapma anlatımındaki yineleme ve pekiştirme işlevini korur."},"facet_ids":["F001","F002"],"text":"sapıklık üstüne sapıklık","usage_role":"contextual"}],"definition":"Sapma veya yanlış yola gitme bildiren bir sözün ardından, bağımsız yeni anlam katmadan ses uyumu ve pekiştirme sağlayan eşlikçi sözdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Önceki sözle uyak kurarak ona sesçe eşlik eder ve anlatımı pekiştirir."},{"facet_id":"F002","role":"specialization","statement":"Kullanımı sapma ve yanlış yola gitme bildiren sağlanmış söz dizileriyle sınırlıdır."}],"identity_rationale":"Kaynak ifadesi bu biçimlerin bağımsız bir kavram taşımadığını, sapma anlamlı sözlerin ardından ses uyumu için getirilen söz eşlikçileri olduğunu açıkça belirtir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"sapmış, büsbütün sapmış"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"sapıklık ve onu pekiştiren uyaklı söz"}],"lexicalization_note":"Tanım yalnızca sağlanmış ikili ve sıralı söz kuruluşlarındaki sesçe eşlik işlevine bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; çoğu yalnızca biçimsel kalıp alanını paylaşır, sapma dalı ise anlam taşıyan öğe ile sesçe eşlik eden öğeyi ayırır.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Komşu dal sapmanın sözlük anlamını taşır; odak dal ise o sözün ardından gelen, bağımsız anlamı olmayan uyaklı pekiştiricidir.","focus_only":"Odak dal bağımsız sapma anlamı kurmaz, yalnızca bu anlamdaki söze sesçe eşlik eder.","gloss":"doğru yoldan sapma","neighbor_only":"Komşu dal doğru yoldan ayrılma ve yanlış yola düşme kavramını doğrudan adlandırır.","neighbor_ref":"root_000913/B001","relation_type":"thematic","shared_zone":"İki dal aynı sapma ve yanlış yola gitme anlatımında yan yana bulunabilir."}],"source_phrase_ar":"رجل ضال تال; جاءنا بالضلالة والتلالة; كل ذلك إتباع (sihah); ضال تال آل وجاء بالضلالة والتلالة والألالة (tahdhib)","source_summary":"Kaynaklar, biçimlerin sapma bildiren sözlere sesçe eşlik ettiğini ve bağımsız bir nesne ya da eylem anlamı taşımadığını gösterir.","sources":["SI","TA"],"what_is_ar":"ضال تال والضلالة والتلالة والألالة على جهة الإتباع اللفظي","what_is_not_ar":"المعنى المستقل للتل أو التلتلة أو التلة"},"support_links":[]},{"boundary":"Dal çiftleşmenin kendisini veya erkek hayvanın davranışını değil, kısrak için eş aramaya gitme eylemini anlatır.","branch_kind":"non_bare","branch_ref":"root_000185/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"kısrağa damızlık erkek aramaya gitme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kısrağa eş olacak damızlık erkek atı aramak amacıyla yola çıkmayı belirtir."}}],"root_ar":"ت ل و","root_id":"root_000185","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin kısrağı için çiftleşecek erkek at bulma amacıyla gittiği özel eylem kuruluşunda kullanılır.","boundary_detail":"Dal çiftleşmenin kendisini veya erkek hayvanın davranışını değil, kısrak için eş aramaya gitme eylemini anlatır.","branch_image_ar":"ذهب يتال طلب فحلا","concept_gloss":"kısrağa damızlık erkek aramaya gitme","contextual_glosses":[{"applicability":"Eylemin öznesi, amacı ve kısrakla ilişkisi doğal bir cümlede açıkça verildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kısrak için damızlık erkek bulma amacıyla gitme eylemini korur."},"facet_ids":["F001"],"text":"kısrağına damızlık erkek aramaya gitti","usage_role":"contextual"}],"definition":"Bir kısrak için çiftleşecek damızlık bir erkek at bulmak veya istemek üzere gitmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kısrağa eş olacak damızlık erkek atı aramak amacıyla yola çıkmayı belirtir."}],"identity_rationale":"Kaynak ifadesi, kişinin kısrağı için çiftleşecek bir erkek at aramak üzere gitmesini belirli bir eylem kuruluşu olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kısrağına damızlık erkek aramaya gitti"}],"lexicalization_note":"Tanım yalnızca kısrak için damızlık erkek aramaya gitmeyi bildiren sağlanmış eylem kuruluşuna bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen kart arama aşaması ile çiftleşme ve damızlık erkeği sağlama aşamasını en açık biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hazırlık aşamasındaki arama ve gitme eylemidir; komşu dal çiftleşme eylemiyle erkeğin bu amaçla sağlanmasını anlatır.","focus_only":"Odak dal insanın kısrak için uygun erkek at aramak üzere gitmesini anlatır.","gloss":"damızlık erkeğin çiftleşmesi","neighbor_only":"Komşu dal erkek atın kısrakla çiftleşmesini, çiftleşmeye çağrılmasını veya bu amaçla ödünç verilmesini kapsar.","neighbor_ref":"root_000932/B005","relation_type":"near_neighbor","shared_zone":"İki dal atların çiftleştirilmesi ve damızlık erkek sağlanması olay alanını paylaşır."}],"source_phrase_ar":"ذهب يتال أي يطلب لفرسه فحلا وهو يفاعل","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynaklı kayıt, kişinin kısrağına damızlık erkek bulmak üzere gitmesini anlatır."}],"source_summary":"Tek tanıklık, eylemi kısrak için çiftleşecek bir erkek at arama amacıyla gitmek şeklinde sınırlar.","sources":["SI"],"what_is_ar":"ذهب يتال بمعنى طلب لفرسه فحلا","what_is_not_ar":"الصب والصرع والتل المرتفع والإتباع"},"support_links":[]},{"boundary":"Çekirdek, izleme ve ardışıklıkla sınırlıdır; borç, güvence, okuma ve terk kullanımları ayrı dallardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000186/B001","candidate_links":[{"candidate_id":"cand_4993df270cbab1e43424","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"ardından izleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlık ya da eylem, önce gelen bir başka şeye bağlı olarak ardından gelir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İzleme, fiziksel sıra kadar konum, derece ya da örnek alma düzeninde de kurulabilir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Atların art arda gelişi, dalın kesintisiz sıralanma örneğidir."}}],"root_ar":"ت ل و","root_id":"root_000186","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin önce geleni takip ettiği genel çekirdeği karşılar ve art arda geliş boyutunu açık bırakır.","boundary_detail":"Çekirdek, izleme ve ardışıklıkla sınırlıdır; borç, güvence, okuma ve terk kullanımları ayrı dallardır.","branch_image_ar":"اتباع وتتابع","concept_gloss":"ardından izleme","contextual_glosses":[{"applicability":"Bir kişi ya da şeyin somut olarak başka birinin ardından geldiği bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Makam, derece veya örnek alma yoluyla izleme boyutunu açıkça taşımaz.","preserves":"Takip ve ardından gelme ilişkisini korur."},"facet_ids":["F001"],"text":"peşinden gelmek","usage_role":"contextual"},{"applicability":"Birden çok unsurun kesintisiz sıra halinde geldiği örneklerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir öndere bağlı izleme ya da örnek alma ilişkisini belirtmez.","preserves":"Sıralı devam ve kesintisiz geliş yönünü korur."},"facet_ids":["F003"],"text":"art arda gelmek","usage_role":"contextual"}],"definition":"Bir şeyin kendinden önce gelen başka bir şeyi takip etmesi, onun ardından gelmesi veya aynı sırayı kesintisiz biçimde sürdürmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlık ya da eylem, önce gelen bir başka şeye bağlı olarak ardından gelir."},{"facet_id":"F002","role":"extension","statement":"İzleme, fiziksel sıra kadar konum, derece ya da örnek alma düzeninde de kurulabilir."},{"facet_id":"F003","role":"example","statement":"Atların art arda gelişi, dalın kesintisiz sıralanma örneğidir."}],"identity_rationale":"Dalın ana sözü, bir şeyin kendinden önce gelen şeyi izlemesi ve art arda gelme fikrini açıkça merkez yapar. Geçici çerçeve bunu bedensel, sıra ve makam bakımından izleme olarak doğru yakalar; borç kalanı, güvence ve terk etme gibi başka dallar bu çekirdeğe katılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyin ardından gelen"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"onu peşinden izledi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"ay onun ardından sıra ve örnek alma bakımından geldi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"atlar art arda geldi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"hakkımı tam alıncaya kadar izini sürdüm"}],"lexicalization_note":"Dal hem yalın izleme biçimlerini hem de belirli kalıp kullanımları içerir; kalıplar yalın anlamı genişletmeden ayrı yüzeyler olarak tutulur.","neighbor_coverage_note":"Adayların çoğu yalnızca sıra, peşinden gelme veya aynı kökten ayrılmış özel anlam alanlarını paylaşıyor; en yararlı sınırlar takip, genel ardışıklık ve kalan payla kuruldu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda ana sınır, önce geleni izleyen konum ve ardışıklıktır; komşuda iz, peş ve takip edilen yol daha güçlüdür.","focus_only":"Bu dal, ardından gelme ve sıra ilişkisini makam veya örnek alma alanına kadar taşıyabilir.","gloss":"iz sürme ile ardınca gelme","neighbor_only":"Komşu dal iz sürme ve peşinden gitme yönünü daha belirgin tutar.","neighbor_ref":"root_001247/B001","relation_type":"near_synonym","shared_zone":"İkisi de önce gelen bir unsurun peşinden gitme ya da onun ardında bulunma alanını paylaşır."},{"boundary_match":"partial","distinction":"Komşu dalda sıranın kendisi yeterlidir; bu dalda sıranın yanında bir önceki unsura bağlı izleme ilişkisi korunur.","focus_only":"Bu dalda takip edilen önceki unsurla bağlılık ve gerekirse örnek alma vardır.","gloss":"takipli sıra ile kesintisiz sıra","neighbor_only":"Komşu dal şeylerin peş peşe ve kesintisiz dizilmesini daha genel bir sıra olarak verir.","neighbor_ref":"root_001684/B002","relation_type":"near_synonym","shared_zone":"İkisi de art arda geliş ve kopmayan devam alanında buluşur."},{"boundary_match":"partial","distinction":"Burada süreç ve sıra anlatılır; komşuda bu ilişkiden doğan kalan miktar nesneleşmiştir.","focus_only":"Bu dalda izleme eylemi veya ardından gelme düzeni çekirdektir.","gloss":"izleme ile kalan pay","neighbor_only":"Komşu dal, öncekinin ardından kalan hak ya da borç parçasını adlandırır.","neighbor_ref":"root_000186/B003","relation_type":"near_neighbor","shared_zone":"Kalan şeyin önceki kısımdan sonra gelmesi, izleme fikriyle bağlantılıdır."}],"source_phrase_ar":"أصل واحد وهو الاتباع (maqayis)؛ تلو الشيء الذي يتلوه (sihah)؛ تلاه تبعه متابعة (mufradat)؛ جاءت الخيل تتاليا أي متتابعة (sihah)","source_summary":"Kaynaklar bu dalı izleme, ardından gelme ve art arda sıralanma etrafında birleştirir; özel kalıp örnekleri bu genel çekirdeğe bağlıdır.","sources":["MQ","SI","MU"],"what_is_ar":"اتباع الشيء لشيء قبله بالجسم أو المنزلة أو التتابع","what_is_not_ar":"ليس الخذلان بعد الصحبة ولا بقية الدين ولا الذمة"},"support_links":["sup_8de64c0a6e362031ee2f"]},{"boundary":"Sınır, kutsal kitap sözlerinin okunması ve izlenmesidir; sıradan metin okuma veya yalnız fiziksel ardışıklık değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000186/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"kutsal kitabı okuyup izleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kutsal kitap sözleri, bir parça diğerini izleyecek biçimde okunur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu kullanım indirilen kutsal kitaplarla sınırlanır, sıradan yazı okumaya genelleştirilmez."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Okuma, anlamı bilme ve gereklerini yerine getirme yönünde izleme anlamına da uzanır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Sözlerin muhataba indirilmesi veya bildirilmesi de bu kutsal metin aktarımı alanına bağlanır."}}],"root_ar":"ت ل و","root_id":"root_000186","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem ardışık okuma hem de anlam ve davranış bakımından izleme çekirdeğini birlikte taşır.","boundary_detail":"Sınır, kutsal kitap sözlerinin okunması ve izlenmesidir; sıradan metin okuma veya yalnız fiziksel ardışıklık değildir.","branch_image_ar":"تلاوة متبوعة","concept_gloss":"kutsal kitabı okuyup izleme","contextual_glosses":[{"applicability":"Okumanın öne çıktığı ve sözlerin sırayla aktarıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bilgi ve davranışla izleme boyutunu açıkça vermez.","preserves":"Kutsal metin sınırını ve okuma eylemini korur."},"facet_ids":["F001","F002"],"text":"kutsal metni okumak","usage_role":"contextual"},{"applicability":"Metnin hakkını verme, bilgi ve davranışla uyma bağlamlarında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sözlü okuma ve ayetlerin ardışıklığını geri planda bırakır.","preserves":"Anlamı ve buyruğu izleme yönünü korur."},"facet_ids":["F003"],"text":"gereğince izlemek","usage_role":"contextual"},{"applicability":"İlahi sözlerin muhataba indirildiği ya da aktarıldığı bağlamlarda açıklayıcıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Okuma ve davranışla izleme çekirdeğini kapsamaz.","preserves":"Sözlerin muhataba ulaştırılması yönünü korur."},"facet_ids":["F004"],"text":"sözleri bildirmek","usage_role":"explanatory"}],"definition":"İndirilen kutsal kitap sözlerini ardışık biçimde okumak ve bu okumanın gerektirdiği anlamı, bilgiyi ve davranışı izlemektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kutsal kitap sözleri, bir parça diğerini izleyecek biçimde okunur."},{"facet_id":"F002","role":"specialization","statement":"Bu kullanım indirilen kutsal kitaplarla sınırlanır, sıradan yazı okumaya genelleştirilmez."},{"facet_id":"F003","role":"extension","statement":"Okuma, anlamı bilme ve gereklerini yerine getirme yönünde izleme anlamına da uzanır."},{"facet_id":"F004","role":"associated_use","statement":"Sözlerin muhataba indirilmesi veya bildirilmesi de bu kutsal metin aktarımı alanına bağlanır."}],"identity_rationale":"Dalın ana sözü, indirilen kutsal kitapların ardışık sözlerini okumayı ve onların bilgi ile eylem bakımından izlenmesini anlatır. Bu nedenle dal sıradan herhangi bir metin okuması değil, kutsal kitap bağlamında okuma ve uymayı birlikte taşıyan özel bir kullanımdır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"indirilen kutsal kitapları okuyup anlamına uymak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kutsal kitabı okudum"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"onu hakkıyla bilgi ve eylemle izlerler"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"sözleri sana indirip bildiriyoruz"}],"lexicalization_note":"Dal hem adlaşmış okuma kavramını hem de belirli kutsal kitap kalıplarını içerir; kalıp anlamları genel izleme dalına taşırılmaz.","neighbor_coverage_note":"Adaylar arasında bazıları metin, okuma, irade veya cin alanlarıyla yalnız gevşek bağ kuruyordu; yayınlanan ayrımlar kutsal kitap okuma sınırını gerçekten netleştirenlerdir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal, genel izleme fikrini özel bir kutsal metin ve ona uyma alanında kullanır; komşu dal bu özel okuma sınırını taşımaz.","focus_only":"Bu dal kutsal kitap sözlerinin okunması ve gereğince izlenmesiyle sınırlıdır.","gloss":"kutsal okuma ile genel izleme","neighbor_only":"Komşu dal daha genel ardından gelme ve art arda sıralanma çekirdeğidir.","neighbor_ref":"root_000186/B001","relation_type":"near_neighbor","shared_zone":"Her ikisinde de bir şeyin başka bir şeyi ardışık biçimde izlemesi vardır."},{"boundary_match":"field_only","distinction":"Bu dalda fiil ve bağlılık vardır; komşuda kişinin yazı ve kitapla ilişkili vasfı vardır.","focus_only":"Bu dal okunan kutsal sözler ve onlara uyma üzerinedir.","gloss":"okuma eylemi ile okumama durumu","neighbor_only":"Komşu dal yazı okuyamayan veya yazı bilmeyen kişi durumunu anlatır.","neighbor_ref":"root_000053/B007","relation_type":"same_field","shared_zone":"İkisi de kitap ve okuryazarlık alanında okuyucu durumuyla temas eder."},{"boundary_match":"partial","distinction":"Bu dalda sözün ardışık okunması ve gereğince izlenmesi çekirdektir; komşuda anlamın sonucuna döndürme ya da açıklama çekirdektir.","focus_only":"Bu dal kutsal sözün okunması ve izlenmesini anlatır.","gloss":"okuyup izleme ile yoruma vardırma","neighbor_only":"Komşu dal sözün döndüğü son anlamı veya yorumla varılan sonucu anlatır.","neighbor_ref":"root_000067/B002","relation_type":"near_neighbor","shared_zone":"İkisi de metnin anlamıyla ilişki kurar."}],"source_phrase_ar":"تلاوة القرآن لأنه يتبع آية بعد آية (maqayis)؛ تلوت القرآن تلاوة (sihah)؛ التلاوة تختص باتباع كتب الله المنزلة تارة بالقراءة وتارة بالارتسام (mufradat)","source_summary":"Kaynaklar kutsal kitap bağlamını ve ayetlerin birbirini izlemesini birlikte verir; ayrıca doğru izleme bilgisini ve davranışını kapsayan genişletilmiş kullanımı da bildirir.","sources":["MQ","SI","MU"],"what_is_ar":"قراءة القرآن أو كتب الله مع تتابع الآيات واتباع المعنى والعمل","what_is_not_ar":"ليست كل قراءة لرقعة أو كلام عادي وليست مجرد تتابع حسي"},"support_links":[]},{"boundary":"Sınır, önceki miktarın ardından kalan paydır; güvence, havale ve kutsal metin okuma bu dalda değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000186/B003","candidate_links":[{"candidate_id":"cand_0b61df74c25a9d3ffcb2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"ardından kalan bakiye","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kalan parça, önceki alınmış veya geçmiş bölümün ardından gelir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kullanım özellikle borç ya da hak bakiyesi için belirgindir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kalan ihtiyacın ya da hakkın izini sürme eylemi bu bakiye fikrine bağlıdır."}}],"root_ar":"ت ل و","root_id":"root_000186","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Önceki miktarın ardından gelen kalan borç, hak veya şey parçasını karşılar.","boundary_detail":"Sınır, önceki miktarın ardından kalan paydır; güvence, havale ve kutsal metin okuma bu dalda değildir.","branch_image_ar":"بقية تتلو ما قبلها","concept_gloss":"ardından kalan bakiye","contextual_glosses":[{"applicability":"Hak veya alacak bağlamındaki örneklerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Borç dışı şeylerdeki genel kalan parça alanını daraltır.","preserves":"Hak alanındaki kalan payı korur."},"facet_ids":["F001","F002"],"text":"haktan kalan pay","usage_role":"contextual"},{"applicability":"Kalan ihtiyaç ya da hakkın peşine düşme kalıplarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kalan payın ad olarak kullanıldığı bağlamları kapsamaz.","preserves":"Kalan payın peşinden gitme eylemini korur."},"facet_ids":["F003"],"text":"kalanı izlemek","usage_role":"contextual"}],"definition":"Bir borç, hak veya şeyden, önceki kısmın ardından geride kalan ve onun izinden gelen pay ya da bakiyedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kalan parça, önceki alınmış veya geçmiş bölümün ardından gelir."},{"facet_id":"F002","role":"specialization","statement":"Kullanım özellikle borç ya da hak bakiyesi için belirgindir."},{"facet_id":"F003","role":"associated_use","statement":"Kalan ihtiyacın ya da hakkın izini sürme eylemi bu bakiye fikrine bağlıdır."}],"identity_rationale":"Dalın ana sözü, borçtan, haktan veya bir şeyden geriye kalan kısmı, önceki bölümün ardından gelmesi nedeniyle açıklar. Geçici çerçeve bu kalan parça fikrini doğru taşır ve onu güvence, aktarma veya okuma anlamlarından ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"önceki kısmın ardından kalan borç veya hak payı"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"borç ya da haktan geriye kalan pay"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"hakkımdan bana kalan bir pay oldu"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"hakkımdan onun yanında bir pay bıraktım"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kalan ihtiyacın peşine düşüyorum"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"ona izleyip alacağı bir kalan pay bıraktım"}],"lexicalization_note":"Dal ad biçimleriyle kalan payı, kalıplarla ise o payın kalması veya aranmasını verir; bu kalıplar ayrı tutulur.","neighbor_coverage_note":"Yayınlanan ayrımlar bakiye, alacak ve aynı kökten genel takip sınırını netleştirir; diğer adaylar yalnız çok dar kalıntı türleri veya uzak mali çağrışımlar sağlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda kalan parçanın önceki bölümü takip etmesi anlamın içindedir; komşuda sadece kalmış olma yeterli olabilir.","focus_only":"Bu dal kalan payı önceki kısmı izlemesi açısından açıklar.","gloss":"izleyen bakiye ile genel kalıntı","neighbor_only":"Komşu dal kalan şeyin varlığını daha genel biçimde anlatır.","neighbor_ref":"root_000142/B002","relation_type":"near_synonym","shared_zone":"İkisi de geride kalan miktar veya parça alanında örtüşür."},{"boundary_match":"field_only","distinction":"Bu dalda nesne kalan paydır; komşuda alacağı isteme ve alma eylemi çekirdektir.","focus_only":"Bu dal alacaktan geride kalan payı adlandırır.","gloss":"kalan alacak ile tahsil etme","neighbor_only":"Komşu dal borcu isteme veya alacağı tahsil etme eylemidir.","neighbor_ref":"root_000244/B003","relation_type":"same_field","shared_zone":"İkisi de borç, hak ve alacak alanında buluşur."},{"boundary_match":"partial","distinction":"Burada takip ilişkisi bir borç veya şey kalanı olarak sonuçlanır; komşuda sonuç değil sıranın kendisi öndedir.","focus_only":"Bu dal takip ilişkisinden doğan kalan payı belirtir.","gloss":"kalan pay ile takip","neighbor_only":"Komşu dal nesneleşmiş bakiye olmadan takip ve ardışıklık düzenini anlatır.","neighbor_ref":"root_000186/B001","relation_type":"near_neighbor","shared_zone":"Kalan şey önceki kısmın ardından geldiği için izleme fikrini paylaşır."}],"source_phrase_ar":"التلية والتلاوة وهي البقية لأنها تتلو ما تقدم منها (maqayis)؛ التلية بقية الدين وكذلك التلاوة (sihah)؛ التلاوة والتلية بقية مما يتلى أي يتبع (mufradat)","source_summary":"Kaynaklar kalan payı, önceki kısmı izlediği için bu dala bağlar; borç ve hak bağlamı ortak biçimde öne çıkar.","sources":["MQ","SI","MU"],"what_is_ar":"البقية من الدين أو الحق أو الشيء لأنها تتلو ما تقدم","what_is_not_ar":"ليست الذمة ولا الحوالة ولا القراءة"},"support_links":["sup_3547654bc514801e17ef"]},{"boundary":"Sınır, bağlı sorumluluk, güvence ve hakkın başka kişiye yöneltilmesidir; sırf izleme veya bakiye değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000186/B004","candidate_links":[{"candidate_id":"cand_ca87aef88979eb081a84","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"bağlı güvence ve talep","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sorumluluk veya güvence kişiye bağlı kalır ve ondan talep edilebilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kullanım, güvence verme ya da birini güvence altına alma kalıbında görünür."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hak veya alacağın başka bir kişi üzerine yöneltilmesi aynı bağlı talep alanına girer."}}],"root_ar":"ت ل و","root_id":"root_000186","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişiyi izleyen sorumluluk, güvence ve hakkın başka kişiye yöneltilmesi çekirdeğini kapsar.","boundary_detail":"Sınır, bağlı sorumluluk, güvence ve hakkın başka kişiye yöneltilmesidir; sırf izleme veya bakiye değildir.","branch_image_ar":"ذمة أو حق يتبع صاحبه","concept_gloss":"bağlı güvence ve talep","contextual_glosses":[{"applicability":"Birine koruma veya sorumluluk güvencesi verme kalıplarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Alacağın başka kişiye yöneltilmesi kullanımını kapsamaz.","preserves":"Güvence ve bağlı sorumluluk yönünü korur."},"facet_ids":["F001","F002"],"text":"güvence altına almak","usage_role":"contextual"},{"applicability":"Bir hak ya da borç talebinin başka kişi üzerine çevrildiği bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel güvence adı ve koruma ilişkisini kapsamaz.","preserves":"Hakkın talep için başka kişiye bağlanması yönünü korur."},"facet_ids":["F003"],"text":"alacağı başkasına yöneltmek","usage_role":"contextual"}],"definition":"Bir kişiye bağlı kalıp onun peşinden gelen güvence, sorumluluk veya bir hakkın talep için başka kişiye yöneltilmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sorumluluk veya güvence kişiye bağlı kalır ve ondan talep edilebilir."},{"facet_id":"F002","role":"specialization","statement":"Kullanım, güvence verme ya da birini güvence altına alma kalıbında görünür."},{"facet_id":"F003","role":"extension","statement":"Hak veya alacağın başka bir kişi üzerine yöneltilmesi aynı bağlı talep alanına girer."}],"identity_rationale":"Dalın ana sözü, kişinin peşinden gelen ve talep edilen güvence, sorumluluk ya da hakkın başka birine yöneltilmesi fikrini bir araya getirir. Çerçeve, güvence ve havale alanını doğru belirler; genel takip veya okuma anlamına genişletilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"kişiyi izleyen güvence veya yükümlülük"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ona güvence verdim"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"birini hakkı nedeniyle başka birine yönelttim"}],"lexicalization_note":"Dal bir ad biçimiyle bağlı sorumluluğu, kalıplarla güvence verme ve hakkı başka kişiye yöneltmeyi içerir.","neighbor_coverage_note":"Adaylardan güvence, kefillik ve borç yöneltme alanını gerçekten netleştirenler seçildi; genel belge veya ibra komşuları daha uzak kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda güvence ve izleyen sorumluluk da çekirdeğin parçasıdır; komşu daha dar biçimde borç yöneltme işlemidir.","focus_only":"Bu dal güvence ve kişiye bağlı sorumluluğu da kapsar.","gloss":"bağlı güvence ile borç yöneltme","neighbor_only":"Komşu dal borcun ya da alacağın başka kişiye devredilmesi işlemini daha doğrudan anlatır.","neighbor_ref":"root_000373/B010","relation_type":"near_synonym","shared_zone":"İkisi de bir hakkın talebini başka kişiyle ilişkilendirme alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşuda üstlenme edimi merkezdir; bu dalda kişiyi izleyen talep ve yöneltme ilişkisi de korunur.","focus_only":"Bu dal hakkı başka kişiye yöneltme kullanımını da içerir.","gloss":"güvence ile kefillik","neighbor_only":"Komşu dal kefil olma ve borcu üstlenme yönünü daha açık taşır.","neighbor_ref":"root_000633/B003","relation_type":"near_synonym","shared_zone":"İkisi de başkası adına sorumluluk yüklenme ve güvence verme alanında buluşur."},{"boundary_match":"field_only","distinction":"Bu dalda ilişki kişiye bağlı yükümlülüktür; komşuda nesne kalan miktardır.","focus_only":"Bu dal sorumluluk ve talebin kişiye bağlanmasını anlatır.","gloss":"güvence talebi ile kalan hak","neighbor_only":"Komşu dal borç ya da haktan geriye kalan payı anlatır.","neighbor_ref":"root_000186/B003","relation_type":"same_field","shared_zone":"İkisi de hak, borç ve talep alanında kullanılır."}],"source_phrase_ar":"التلاء الذمة لأنها تتبع وتطلب يقال أتليته ذمة (maqayis)؛ التلاء الذمة (sihah)؛ أتليته أحلته من الحوالة (sihah)؛ أتليت فلانا على فلان بحق أي أحلته عليه (mufradat)","source_summary":"Kaynaklar dalı kişiyi izleyen sorumluluk ve talep edilebilir hakla açıklar; güvence verme ve hakkı başkasına yöneltme kalıpları aynı alanda toplanır.","sources":["MQ","SI","MU"],"what_is_ar":"الذمة والكفالة والحوالة وإبقاء بعض الحق عند غيره","what_is_not_ar":"ليست تلاوة القرآن ولا مطلق الاتباع الحسي"},"support_links":["sup_1b217553d0fd07891f10"]},{"boundary":"Sınır, destekten vazgeçme veya öne geçip geride bırakmadır; sürekli takip, okuma ve bakiye değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000186/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"geride bırakıp terk etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Önceden ilişki içinde olunan kişi terk edilir veya yardımsız bırakılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Öne geçme sonucunda takip edilen kişi artık arkada kalır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kaynak sözü aynı dal içinde hem terk etme hem de geçip geride bırakma yönünü verir."}}],"root_ar":"ت ل و","root_id":"root_000186","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem yardımsız bırakmayı hem de öne geçerek arkada bırakma sonucunu kapsar.","boundary_detail":"Sınır, destekten vazgeçme veya öne geçip geride bırakmadır; sürekli takip, okuma ve bakiye değildir.","branch_image_ar":"ترك بعد صحبة","concept_gloss":"geride bırakıp terk etme","contextual_glosses":[{"applicability":"Kişiyi terk etme ve destekten yoksun bırakma bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öne geçerek arkada bırakma yönünü kapsamaz.","preserves":"Destek vermeme ve terk etme yönünü korur."},"facet_ids":["F001"],"text":"yardımsız bırakmak","usage_role":"contextual"},{"applicability":"Birinin önüne geçildiği ve onun arkada kaldığı bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yardımsız bırakma ve terk etme duygusunu açıkça vermez.","preserves":"Öne geçme ve arkada bırakma sonucunu korur."},"facet_ids":["F002"],"text":"geçip geride bırakmak","usage_role":"contextual"}],"definition":"Bir kişiyi önceki beraberlik veya takip ilişkisinden sonra bırakmak, desteklememek ya da öne geçerek onu arkada kalmış duruma getirmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Önceden ilişki içinde olunan kişi terk edilir veya yardımsız bırakılır."},{"facet_id":"F002","role":"extension","statement":"Öne geçme sonucunda takip edilen kişi artık arkada kalır."},{"facet_id":"F003","role":"source_variant","statement":"Kaynak sözü aynı dal içinde hem terk etme hem de geçip geride bırakma yönünü verir."}],"identity_rationale":"Dalın ana sözü, bir adamı destekten yoksun bırakıp terk etmeyi ve ilerleyerek onu arkada bırakmayı bildirir. Çerçeve, önceki izleme ilişkisinden kopma ve geride bırakma sonucunu doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"adamı terk edip yardımsız bıraktım"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"onu geçtim ve arkamda bıraktım"}],"lexicalization_note":"Dal belirli kişiyle kullanılan terk kalıbını ve öne geçme biçimini içerir; ikisi genel takip anlamıyla karıştırılmamalıdır.","neighbor_coverage_note":"En yararlı adaylar terk etme alanını ve aynı kökteki takip karşıtlığını gösterdi; arkadaşlık ya da uzaklaşma komşuları daha geniş alanı paylaşsa da sınırı daha az keskinleştiriyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşuda bırakma yeterlidir; bu dalda bırakma, önceki takip ilişkisine ve geride kalma sonucuna bağlanır.","focus_only":"Bu dal önceki takip veya beraberlikten sonra geride bırakma sonucunu da taşır.","gloss":"geride bırakma ile terk etme","neighbor_only":"Komşu dal genel olarak salıverme, boş bırakma veya desteklememe alanını verir.","neighbor_ref":"root_001004/B008","relation_type":"near_synonym","shared_zone":"İkisi de bir şeyi ya da kişiyi bırakma ve desteklememe alanında örtüşür."},{"boundary_match":"partial","distinction":"Bu dal kişi ve takip ilişkisi üzerinden kurulur; komşu daha geniş bir bırakma eylemidir.","focus_only":"Bu dal terk edilen kişinin geriye düşmesi veya desteksiz kalması sonucunu vurgular.","gloss":"kişiyi geride bırakma ile genel bırakma","neighbor_only":"Komşu dal daha genel olarak bir şeyi elden bırakma ya da terk etmedir.","neighbor_ref":"root_000180/B001","relation_type":"near_neighbor","shared_zone":"İkisi de bırakma ve vazgeçme alanında buluşur."},{"boundary_match":"opposed","distinction":"B001'de ikinci unsur önce geleni izler; bu dalda ilişki kopar veya öne geçme nedeniyle öteki arkada kalır.","focus_only":"Bu dal takip ilişkisinin kopması ve kişinin arkada bırakılmasıdır.","gloss":"takip etmek ile terk etmek","neighbor_only":"Komşu dal takip ve ardından gelme ilişkisinin sürmesidir.","neighbor_ref":"root_000186/B001","relation_type":"polarity_pair","shared_zone":"İkisi de önce ve sonra konumlarıyla ilişki kurar."}],"source_phrase_ar":"تلوت الرجل إذا خذلته وتركته (maqayis;sihah)؛ حتى أتليته أي حتى تقدمته وصار خلفي (sihah)؛ أتليته أي سبقته (sihah)","source_summary":"Kaynaklar bu dalda takip ilişkisinin tersine dönmesini öne çıkarır: kişi terk edilir, desteksiz kalır veya geriye düşmüş olur.","sources":["MQ","SI"],"what_is_ar":"خذلان الرجل وتركه أو سبقه حتى يصير خلفا بعد متابعة","what_is_not_ar":"ليس الاتباع المستمر ولا التلاوة ولا البقية"},"support_links":[]},{"boundary":"Sınır, yavru ve doğumla ilgili izleme ilişkisidir; borç kalanı, kutsal okuma ve güvence değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000186/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"anneyi izleyen yavru","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yavru, annesinin ardından giden ve ona bağlı olan varlık olarak adlandırılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Koyunlarda belirli doğum zamanı için kullanılan biçim bu doğum alanına bağlıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çocukların bir kimseye peş peşe verilmesi aynı yavru ve soy izleme fikrine uzanır."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Hayvanın yavrusuz kalması için edilen kötü dilek, dalın yavru sahibi olma alanını örnekler."}}],"root_ar":"ت ل و","root_id":"root_000186","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yavrunun anneye bağlı ardından gelişini ve doğumla ilgili uzantıları en kısa biçimde karşılar.","boundary_detail":"Sınır, yavru ve doğumla ilgili izleme ilişkisidir; borç kalanı, kutsal okuma ve güvence değildir.","branch_image_ar":"ولد يتلو أمه","concept_gloss":"anneyi izleyen yavru","contextual_glosses":[{"applicability":"Deve veya başka hayvan yavrusunun anneye bağlı izlenişi için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Doğum zamanı ve çocuk verilmesi uzantılarını kapsamaz.","preserves":"Yavru ve anneye bağlı takip ilişkisini korur."},"facet_ids":["F001"],"text":"annesinin peşindeki yavru","usage_role":"contextual"},{"applicability":"Bir kişiye peş peşe çocuklar verilmesi kalıbında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvan yavrusunun anne peşindeki temel görünümünü dışarıda bırakır.","preserves":"Soy ve çocuk verilmesi uzantısını korur."},"facet_ids":["F003"],"text":"çocuklar vermek","usage_role":"contextual"}],"definition":"Yavrunun annesini izlemesi veya doğumun, soyun ve çocukların birbirini takip eden bağlı gelişidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yavru, annesinin ardından giden ve ona bağlı olan varlık olarak adlandırılır."},{"facet_id":"F002","role":"specialization","statement":"Koyunlarda belirli doğum zamanı için kullanılan biçim bu doğum alanına bağlıdır."},{"facet_id":"F003","role":"extension","statement":"Çocukların bir kimseye peş peşe verilmesi aynı yavru ve soy izleme fikrine uzanır."},{"facet_id":"F004","role":"example","statement":"Hayvanın yavrusuz kalması için edilen kötü dilek, dalın yavru sahibi olma alanını örnekler."}],"identity_rationale":"Dalın ana sözü, devenin yavrusunun annesini izlemesi, koyunun doğum zamanı ve çocukların bir kişiye peş peşe verilmesi gibi soy ve doğum örneklerini içerir. Çerçeve, yavrunun anneye bağlı takip ilişkisini ve doğumla ilgili özel kullanımları doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"devenin annesini izleyen yavrusu"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"erken doğuran koyun"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"devenin yavrusu onun peşinden geldi"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"Tanrı ona peş peşe çocuklar verdi"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"sürülerin yavrusuz kalması dileği"}],"lexicalization_note":"Dal hayvan yavrusu ve doğum biçimlerini, ayrıca çocuk verilmesi kalıbını içerir; hayvan ve soy bağlamı korunur.","neighbor_coverage_note":"Seçilen ayrımlar yavru türü, küçük hayvan yavrusu ve genel takip sınırını açıklaştırır; diğer adaylar yalnız doğum, çocuk veya tür çağrışımı veriyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu sığır türüne daralır; bu dal hayvan yavrusu ve çocuk verilmesi alanını daha geniş tutar.","focus_only":"Bu dal deve yavrusu, koyun doğumu ve çocuk verilmesi gibi daha geniş soy örnekleri taşır.","gloss":"anneyi izleyen yavru türleri","neighbor_only":"Komşu dal özellikle sığır yavrusunun anneyi izlemesi ve buna bağlı hayvan sayımı alanıdır.","neighbor_ref":"root_000175/B007","relation_type":"near_synonym","shared_zone":"İkisi de yavrunun anneye bağlı olarak onun peşinden gitmesi fikrini paylaşır."},{"boundary_match":"field_only","distinction":"Bu dalda ilişki anneden sonra gelmedir; komşuda küçük yavru olma niteliği merkezdir.","focus_only":"Bu dal yavrunun anneye bağlı takip ilişkisini öne çıkarır.","gloss":"takip eden yavru ile küçük yavru","neighbor_only":"Komşu dal küçük hayvan yavrularını tür ve yaş olarak adlandırır.","neighbor_ref":"root_000160/B004","relation_type":"same_field","shared_zone":"İkisi de hayvan yavruları alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dal soy ve doğumla sınırlıdır; komşu dal bu özel biyolojik alanı taşımaz.","focus_only":"Bu dal takip çekirdeğini yavru ve doğum alanına özelleştirir.","gloss":"yavrunun takibi ile genel takip","neighbor_only":"Komşu dal herhangi bir şeyin ardından gelmesini genel olarak anlatır.","neighbor_ref":"root_000186/B001","relation_type":"near_neighbor","shared_zone":"Yavrunun anne peşinden gitmesi genel takip fikrine dayanır."}],"source_phrase_ar":"تلو الناقة ولدها الذي يتلوها؛ التلوة من الغنم التي تنتج قبل الصفرية؛ أتلت الناقة إذا تلاها ولدها؛ أتلاه الله أطفالا أي أتبعه أولادا","source_qualifications":[{"kind":"sole_attestation","summary":"Kanıt, devenin yavrusu, koyun doğumu, çocuk verilmesi ve yavrusuzluk dileği örneklerini tek dalda verir."}],"source_summary":"Bu dal tek kaynaklı kanıtta yavru, doğum ve çocukların peş peşe verilmesi alanında toplanır.","sources":["SI"],"what_is_ar":"ولد الناقة أو الأولاد الذين يتبعون أمهاتهم وما اتصل بذلك من ولادة الغنم","what_is_not_ar":"ليس بقية دين ولا تلاوة ولا ذمة"},"support_links":[]},{"boundary":"Sınır, sesle karşılık verme ve bir sesi izleme alanıdır; kitap okuma veya genel takip değildir.","branch_kind":"bare","branch_ref":"root_000186/B007","candidate_links":[{"candidate_id":"cand_84f74fa55961258a7af7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"sese karşılık veren eşlikçi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir ses, başka bir sesin ardından ona karşılık verecek biçimde gelir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kullanım şarkıcıya sesle eşlik eden veya karşılık veren kişi için özelleşmiştir."}}],"root_ar":"ت ل و","root_id":"root_000186","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Şarkıcıya ya da önceki sese onu izleyen bir sesle cevap veren kişiyi karşılar.","boundary_detail":"Sınır, sesle karşılık verme ve bir sesi izleme alanıdır; kitap okuma veya genel takip değildir.","branch_image_ar":"صوت يتلو صوتا","concept_gloss":"sese karşılık veren eşlikçi","contextual_glosses":[{"applicability":"Şarkı veya sesli icra bağlamında karşılık veren kişi için doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sesin önceki sesi takip etmesi gerekçesini açıkça belirtmez.","preserves":"Şarkıcıyla birlikte ses verme yönünü korur."},"facet_ids":["F002"],"text":"şarkıcıya eşlik eden","usage_role":"contextual"}],"definition":"Bir şarkıcıya ya da ses çıkarana, onun sesini izleyen yüksek ya da belirgin bir sesle karşılık veren kişidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir ses, başka bir sesin ardından ona karşılık verecek biçimde gelir."},{"facet_id":"F002","role":"specialization","statement":"Kullanım şarkıcıya sesle eşlik eden veya karşılık veren kişi için özelleşmiştir."}],"identity_rationale":"Dalın ana sözü, şarkıcıya karşılık veren ve sesi onun sesini izleyen kişiyi anlatır. Çerçeve bu sesli karşılıklı izleme alanını doğru yakalar ve okuma, güvence veya bakiye anlamlarıyla karıştırmaz.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"şarkıcıya sesle karşılık veren kişi"}],"lexicalization_note":"Mekanik profil yalın dal verir; tanım belirli bir kalıba değil, sesle karşılık veren kişi anlamına bağlanır.","neighbor_coverage_note":"Adaylar çoğunlukla ses alanından geldi; yankı, tekrar ve genel takip ayrımları okuyucu için en gerçek karışma noktalarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda sesli cevap veren kişi vardır; komşuda geri dönen ses olayı merkezdir.","focus_only":"Bu dal, bilinçli olarak şarkıcıya karşılık veren kişiyi anlatır.","gloss":"eşlik eden ses ile yankı","neighbor_only":"Komşu dal bir sesin mekandan geri dönmesi gibi yankı alanıdır.","neighbor_ref":"root_000853/B004","relation_type":"near_neighbor","shared_zone":"İkisi de bir sesin ardından başka bir sesin gelmesi alanını paylaşır."},{"boundary_match":"partial","distinction":"Bu dalda kişi ve karşılıklı icra öne çıkar; komşuda sesin kendisinin yinelenmesi çekirdektir.","focus_only":"Bu dal karşılık veren kişiyi adlandırır.","gloss":"eşlikçi ile ses tekrarı","neighbor_only":"Komşu dal sesin tekrarlanması, döndürülmesi veya nağmeyle yinelenmesi eylemini anlatır.","neighbor_ref":"root_000544/B007","relation_type":"near_neighbor","shared_zone":"İkisi de sesin önceki sese bağlı biçimde yeniden gelmesi alanındadır."},{"boundary_match":"partial","distinction":"Bu dalda izleyen unsur sestir ve kişi rolüyle belirlenir; komşu bu sesli icra sınırını taşımaz.","focus_only":"Bu dal genel takip fikrini sesli eşlik alanına özelleştirir.","gloss":"sesle takip ile genel takip","neighbor_only":"Komşu dal ses dışında her tür ardından gelme ve sıralanmayı kapsar.","neighbor_ref":"root_000186/B001","relation_type":"near_neighbor","shared_zone":"Her ikisinde de önce geleni izleme ilişkisi vardır."}],"source_phrase_ar":"المتالي الذي يراد صاحبه الغناء لأن كل واحد منهما يتلو صاحبه (maqayis)؛ المتالي الذي يراسل المغني بصوت رفيع (sihah)","source_summary":"Kaynaklar dalı, şarkıcının sesini izleyen ve ona karşılık veren kişi üzerinden açıklar; sesin başka sesi takip etmesi anlamın gerekçesidir.","sources":["MQ","SI"],"what_is_ar":"المتالي الذي يراسل المغني بصوت يتبع صوته","what_is_not_ar":"ليس قراءة ولا ذمة ولا بقية"},"support_links":["sup_10160ceae33d8cf40e18"]},{"boundary":"Sınır, kişinin son canlılık halinde bulunmasıdır; izleme, okuma veya kalan pay anlamı değildir.","branch_kind":"collocation","branch_ref":"root_000186/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"son nefeste olmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, ölüm öncesindeki son canlılık sınırında bulunur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kullanım bir kişi hakkındaki belirli kalıpla sınırlıdır."}}],"root_ar":"ت ل و","root_id":"root_000186","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi için hayatın bitme eşiğindeki son canlılık durumunu doğrudan karşılar.","boundary_detail":"Sınır, kişinin son canlılık halinde bulunmasıdır; izleme, okuma veya kalan pay anlamı değildir.","branch_image_ar":"آخر رمق","concept_gloss":"son nefeste olmak","contextual_glosses":[{"applicability":"Son nefes halinin doğal Türkçe anlatımı gerektiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölüm eşiğindeki son canlılık halini doğal biçimde korur."},"facet_ids":["F001"],"text":"can çekişmek","usage_role":"contextual"}],"definition":"Bir kişinin hayatının bitme eşiğinde, son nefes ya da son canlılık halinde bulunmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, ölüm öncesindeki son canlılık sınırında bulunur."},{"facet_id":"F002","role":"specialization","statement":"Kullanım bir kişi hakkındaki belirli kalıpla sınırlıdır."}],"identity_rationale":"Dalın ana sözü yalnızca kişinin son nefes sınırında bulunmasını bildirir. Çerçeve bu dar durumu doğru yakalar; ancak kullanım kalıp olduğundan genel takip veya bakiye anlamına genişletilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"adam son nefesindeydi"}],"lexicalization_note":"Mekanik profil kalıp kullanımı verir; tanım yalnız kişi için son canlılık haliyle sınırlı tutulur.","neighbor_coverage_note":"Ölüm eşiği ve nefes adayları sınırı açıklıyor; aynı kökten diğer dallar ise daha çok ayrıştırma amacıyla değerlendirilmiştir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal durum bildirir; komşu dal nefesin çıkışı veya göğüs olayı olarak daha olay merkezlidir.","focus_only":"Bu dal kişinin son canlılık halinde bulunmasını bildirir.","gloss":"son halde olmak ile son soluk","neighbor_only":"Komşu dal göğüsten çıkan son soluk veya nefes olayı üzerinde durur.","neighbor_ref":"root_001188/B010","relation_type":"near_neighbor","shared_zone":"İkisi de ölüm eşiği ve nefes alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dal daha genel son canlılık halidir; komşu özel boğaz ve yutkunma imgesiyle belirlenir.","focus_only":"Bu dal son nefes durumunda olmayı anlatır.","gloss":"son nefes ile boğazdaki son an","neighbor_only":"Komşu dal boğazdaki son yutkunma ya da ölüm kıyısından kurtulma gibi özel bir sınır durumunu anlatır.","neighbor_ref":"root_000237/B004","relation_type":"near_neighbor","shared_zone":"İkisi de ölüm eşiğindeki bedensel son an alanındadır."},{"boundary_match":"thematic_only","distinction":"Bu kalıp, genel ardından gelme anlamıyla çevrilirse yanlış olur; ölüm eşiği durumu olarak korunmalıdır.","focus_only":"Bu dal kalıplaşmış son canlılık durumudur.","gloss":"son canlılık ile takip","neighbor_only":"Komşu dal genel takip ve ardışıklık anlamını taşır.","neighbor_ref":"root_000186/B001","relation_type":"other","shared_zone":"Aynı kökten gelmeleri dışında açık bir kullanılabilir anlam örtüşmesi azdır."}],"source_phrase_ar":"تلى الرجل بالتشديد إذا كان بآخر رمق","source_qualifications":[{"kind":"sole_attestation","summary":"Kanıt, kalıbı kişinin son canlılık veya son nefes halinde bulunmasıyla sınırlar."}],"source_summary":"Bu dal tek kaynaklı kanıtta kişinin son nefes sınırındaki halini bildirir ve başka dal anlamlarıyla birleştirilmez.","sources":["SI"],"what_is_ar":"حال الرجل إذا كان بآخر رمق","what_is_not_ar":"ليس اتباعا حسيا ولا تلاوة ولا بقية"},"support_links":[]},{"boundary":"Sınır, bir kimse hakkında yalan isnat etmektir; okuma, izleme veya sorumluluk değildir.","branch_kind":"collocation","branch_ref":"root_000186/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","surface_ar":"تَلَىٰ"}],"gloss":"hakkında yalan söylemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Söyleyen kişi, başka biri hakkında yalan bir söz ileri sürer."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kullanım, bir kişi hakkında konuşma kalıbıyla sınırlıdır."}}],"root_ar":"ت ل و","root_id":"root_000186","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kimse hakkında gerçeğe aykırı söz söyleme kalıbını doğrudan karşılar.","boundary_detail":"Sınır, bir kimse hakkında yalan isnat etmektir; okuma, izleme veya sorumluluk değildir.","branch_image_ar":"قول كذب على غيره","concept_gloss":"hakkında yalan söylemek","contextual_glosses":[{"applicability":"Yalan sözün suçlayıcı veya kişiye zarar veren bağlamlarda doğal karşılığıdır.","error_profile":{"adds":"Suçlayıcı veya zarar verici niyet çağrışımı ekleyebilir.","collision":null,"fit":"narrowing","loses":"Her yalan söyleme bağlamında suçlayıcı zarar boyutu açık olmayabilir.","preserves":"Başka kişiye yönelen yalan isnadı korur."},"facet_ids":["F001"],"text":"iftira etmek","usage_role":"contextual"}],"definition":"Bir kişinin başka biri hakkında gerçeğe aykırı söz söylemesi, ona yalan isnat etmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Söyleyen kişi, başka biri hakkında yalan bir söz ileri sürer."},{"facet_id":"F002","role":"specialization","statement":"Kullanım, bir kişi hakkında konuşma kalıbıyla sınırlıdır."}],"identity_rationale":"Dalın ana sözü, bir kişinin başkası hakkında yalan söz söylemesini açıkça bildirir. Çerçeve bu kalıp anlamını doğru verir; kutsal metin okuma, genel takip veya güvence alanına taşınmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"biri hakkında yalan söylüyor"}],"lexicalization_note":"Mekanik profil kalıp kullanımı verir; tanım yalnız başkası hakkında yalan söyleme yapısına bağlıdır.","neighbor_coverage_note":"Yalan, isnat ve iftira adayları sınırı gerçekten açıklaştırıyor; diğer adaylar genel kötü söz alanında kalıyor veya yalnız aynı kök ayrımı sağlıyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda hedef kişi yapısı sınırdır; komşu dal daha geniş yalan üretme alanıdır.","focus_only":"Bu dal bir kişi hakkında yalan söyleme kalıbıyla sınırlıdır.","gloss":"kişiye yalan isnadı ile uydurma","neighbor_only":"Komşu dal uydurma, yalan ve ağır iftira alanını daha geniş verir.","neighbor_ref":"root_001150/B003","relation_type":"near_synonym","shared_zone":"İkisi de gerçeğe aykırı söz ve yalan isnadı alanını paylaşır."},{"boundary_match":"partial","distinction":"Komşu daha genel söz isnadı alanına gider; bu dalın sınırı kişi hakkında yalan söyleme kalıbıdır.","focus_only":"Bu dal belirli kalıpta bir kişi hakkında yalan söylemektir.","gloss":"hakkında yalan ile olmamış söz","neighbor_only":"Komşu dal genel olarak olmamış sözü söyleme veya birine söyletme alanını kapsar.","neighbor_ref":"root_001272/B005","relation_type":"near_synonym","shared_zone":"İkisi de gerçek olmayan sözü başkasına bağlama alanında örtüşür."},{"boundary_match":"thematic_only","distinction":"Genel takip anlamı buraya taşınırsa dal yanlış anlaşılır; burada söz eylemi gerçeğe aykırı isnattır.","focus_only":"Bu dal yalan isnat etme kalıbıdır.","gloss":"yalan isnat ile takip","neighbor_only":"Komşu dal genel ardından gelme ve takip ilişkisini anlatır.","neighbor_ref":"root_000186/B001","relation_type":"other","shared_zone":"Aynı kökten gelmeleri dışında işlevsel örtüşme çok sınırlıdır."}],"source_phrase_ar":"فلان يتلو على فلان ويقول عليه أي يكذب عليه","source_qualifications":[{"kind":"sole_attestation","summary":"Kanıt, kalıbı bir kişi hakkında gerçeğe aykırı söz söylemekle sınırlar."}],"source_summary":"Bu dal tek kaynaklı kanıtta başkası hakkında yalan söz söyleme kalıbı olarak verilir ve okuma anlamıyla birleştirilmez.","sources":["MU"],"what_is_ar":"أن يتلو الرجل على غيره أي يقول عليه كذبا","what_is_not_ar":"ليس تلاوة كتاب ولا اتباعا ولا ذمة"},"support_links":[]},{"boundary":"Dal, gök cismini ve onun ışığını kapsar; Ay'a benzeyen renkleri ya da yalnızca dolunaydaki tamamlanmayı kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001255/B001","candidate_links":[{"candidate_id":"cand_4993df270cbab1e43424","lane":"micro"},{"candidate_id":"cand_0b61df74c25a9d3ffcb2","lane":"micro"},{"candidate_id":"cand_84f74fa55961258a7af7","lane":"micro"},{"candidate_id":"cand_ca87aef88979eb081a84","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَمَر","morph_features":"STEM|POS:N|LEM:qamar|ROOT:qmr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:2:1:3","qac_word_ref":"91:2:1","surface_ar":"قَمَرِ"}],"gloss":"Ay, ay ışığı ve ayla aydınlanan gece","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim, gökte görülen Ay adlı gök cismidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ay'ın ışığı, bu ışıkla aydınlanan gece ve Ay'ın bir topluluk üzerine doğması aynı dala bağlı kullanımlardır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ay adının başlangıç sınırı hilalden sonraki birkaç geceyle, belirgin evresi ise dolunayla ilişkilendirilir."}}],"root_ar":"ق م ر","root_id":"root_001255","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gök cismi ile ondan gelen ışığın oluşturduğu temel anlam alanını birlikte karşılar.","boundary_detail":"Dal, gök cismini ve onun ışığını kapsar; Ay'a benzeyen renkleri ya da yalnızca dolunaydaki tamamlanmayı kapsamaz.","branch_image_ar":"القمر وضوؤه في السماء","concept_gloss":"Ay, ay ışığı ve ayla aydınlanan gece","contextual_glosses":[{"applicability":"Ay'ın görünür hale gelerek bir topluluğun üzerine doğmasını bildiren kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ay'ın doğup insanlarca görünür hale gelmesi olayını korur."},"facet_ids":["F002"],"text":"Ay üzerimize doğdu","usage_role":"contextual"}],"definition":"Gökteki Ay ile ondan yayılan ışığı ve bu ışığın geceyi aydınlatmasını anlatır. Bazı kaynaklar Ay adının hilalden sonraki günlerde, bazıları ise özellikle dolunayda kullanıldığını belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim, gökte görülen Ay adlı gök cismidir."},{"facet_id":"F002","role":"extension","statement":"Ay'ın ışığı, bu ışıkla aydınlanan gece ve Ay'ın bir topluluk üzerine doğması aynı dala bağlı kullanımlardır."},{"facet_id":"F003","role":"source_variant","statement":"Ay adının başlangıç sınırı hilalden sonraki birkaç geceyle, belirgin evresi ise dolunayla ilişkilendirilir."}],"identity_rationale":"Kaynak ifadesi gökteki Ay'ı, onun ışığını ve bu ışıkla aydınlanan geceyi aynı anlam alanında açıkça birleştirir. Ay adının hilalden sonraki günlerde ya da dolunay evresinde kullanılması kaynaklar arasındaki kapsam farkıdır; gök cismi ile ışık çekirdeğini değiştirmez.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"gökteki Ay"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"küçük Ay; Ay adının küçültme biçimi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"ay ışığı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ay ışığıyla aydınlanan gece"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"Ay üzerimize doğdu"}],"lexicalization_note":"Tanım, Ay'ın yalın adını ışık, aydınlık gece ve doğma bildiren yapıya bağlı kullanımlardan ayırarak birlikte gösterir.","neighbor_coverage_note":"Adayların tümü değerlendirildi; dolunay ve tamamlanma dalı, Ay'ın kendisiyle belirli evresini karıştırma ihtimali en yüksek olan yararlı karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği Ay adlı gök cismi ve onun ışığıdır; komşu dalın çekirdeği ise bir şeyin tamamlanıp dolmasıdır ve dolunay bunun belirgin bir örneğidir.","focus_only":"Ay'ı farklı evreleriyle, ışığını ve ay aydınlığındaki geceyi kapsar.","gloss":"dolunay ve tamamlanmış dolgunluk","neighbor_only":"Dolunayın yanında genel tamamlanma ve dolgunluk durumunu da anlatır.","neighbor_ref":"root_000093/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da Ay'ın dolunay evresindeki tam ve parlak görünümüyle ilişkilidir."}],"source_phrase_ar":"القمر قمر السماء سمى قمرا لبياضه (maqayis)؛ القمراء ضوء القمر وليلة مقمرة (ayn;tahdhib)؛ القمر بعد ثلاث ليال إلى آخر الشهر (sihah)؛ القمر قمر السماء يقال عند الامتلاء (mufradat)","source_summary":"Kaynaklar gökteki Ay, ay ışığı ve ayla aydınlanan gece üzerinde birleşir; adın ayın hangi evresinden itibaren öne çıktığı konusunda hilal sonrası ile dolunay arasında farklı sınırlar verir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه القمر السماوي، وضوءه القمراء، والليلة المقمرة أو التي أقمرت، وتسميته بعد الهلال أو عند الامتلاء بحسب نصوص المصادر.","what_is_not_ar":"لا يدخل فيه لون الأقمر في الحيوان والسحاب إلا من جهة البياض المشبه بضوء القمر."},"support_links":["sup_10160ceae33d8cf40e18","sup_1b217553d0fd07891f10","sup_3547654bc514801e17ef","sup_8de64c0a6e362031ee2f"]},{"boundary":"Dal, Ay'ın kendisini ya da ışığını değil, özellikle hayvanlar ve bulutlar için kullanılan beyazımsı veya yeşile çalan rengi anlatır.","branch_kind":"bare","branch_ref":"root_001255/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَمَر","morph_features":"STEM|POS:N|LEM:qamar|ROOT:qmr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:2:1:3","qac_word_ref":"91:2:1","surface_ar":"قَمَرِ"}],"gloss":"ay ışığını andıran beyaz ya da yeşile çalan açık renk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Renk çekirdeği beyaz veya çok açık beyazdır; bazı aktarımlarda yeşile çalan bir ton taşır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu renk eşek, dişi eşek, seçkin deve ve bulut gibi varlıkların niteliği olarak kullanılır."}}],"root_ar":"ق م ر","root_id":"root_001255","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanların veya bulutların rengini ay ışığına benzer bir açıklıkla betimlerken uygundur.","boundary_detail":"Dal, Ay'ın kendisini ya da ışığını değil, özellikle hayvanlar ve bulutlar için kullanılan beyazımsı veya yeşile çalan rengi anlatır.","branch_image_ar":"بياض قمري أو لون أقمر","concept_gloss":"ay ışığını andıran beyaz ya da yeşile çalan açık renk","contextual_glosses":[{"applicability":"Rengin düz beyazdan ayrılan yeşilimsi tonu bağlamda öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Beyazımsı açıklığı ve yeşile çalan özel tonu birlikte korur."},"facet_ids":["F001"],"text":"yeşile çalan beyazımsı renkli","usage_role":"contextual"}],"definition":"Özellikle hayvan ve bulut betimlemelerinde görülen, beyazdan çok açık beyaza uzanan ve kimi anlatımlarda yeşile çalan ay ışığı benzeri bir renktir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Renk çekirdeği beyaz veya çok açık beyazdır; bazı aktarımlarda yeşile çalan bir ton taşır."},{"facet_id":"F002","role":"specialization","statement":"Bu renk eşek, dişi eşek, seçkin deve ve bulut gibi varlıkların niteliği olarak kullanılır."}],"identity_rationale":"Kaynak ifadesi hayvan ve bulut betimlemelerinde beyaz, çok açık ya da yeşile çalan bir rengi açıkça tanımlar. Bu nedenle dal genel beyazlık değil, ay ışığına benzetilen ve bağlama göre yeşilimsi olabilen özel bir renk niteliğidir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"beyaz ya da yeşile çalan açık renkli"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yeşile çalan beyazımsı renk"}],"lexicalization_note":"Tanım yalın renk dalıyla sınırlıdır; ay ışığına ilişkin gece ve aydınlanma kullanımları bu dala taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel beyazlık dalı, bu özel beyazımsı tonu sıradan beyaz renkle karıştırma riskini en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal özel bir renk tonu ve sınırlı betimleme alanı taşır; komşu dal ise nesne türü ya da ton sınırlaması olmadan beyaz rengin genel adıdır.","focus_only":"Hayvan ve bulut betimlemelerinde yeşile çalabilen, ay ışığı benzeri özel tonu taşır.","gloss":"genel beyazlık ve beyazlaşma","neighbor_only":"Her tür nesnedeki genel beyazlığı, beyazlaşmayı ve beyazlatmayı kapsar.","neighbor_ref":"root_000168/B001","relation_type":"near_synonym","shared_zone":"İki dalın ortak alanı, bir varlığın beyaz veya çok açık renkte görünmesidir."}],"source_phrase_ar":"حمار أقمر أي أبيض (maqayis)؛ القمرة لون الحمار الأقمر وهو لون يضرب إلى الخضرة (ayn;tahdhib)؛ سحاب أقمر وأتان قمراء بيضاء وهجان أقمر (sihah;tahdhib)؛ حمار أقمر على لون القمراء (mufradat)","source_summary":"Kaynaklar beyazlık üzerinde birleşir; bazı anlatımlar rengi çok açık beyaz olarak verirken bazıları yeşile çalan tonu özellikle belirtir ve kullanım alanını hayvanlarla bulutlara yayar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الأقمر والقمراء في الحمار والأتان والسحاب والهجان، والقمرة كلون يضرب إلى الخضرة أو البياض الشديد.","what_is_not_ar":"لا يدخل فيه جرم القمر نفسه ولا ضوء القمراء إلا بوصفهما أصل التشبيه اللوني."},"support_links":[]},{"boundary":"Dal yalnızca ay ışığında yaklaşma ve gece avında görüşü şaşırtıp gafil yakalama kullanımlarını kapsar; genel avlanma veya genel aldatma değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001255/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَمَر","morph_features":"STEM|POS:N|LEM:qamar|ROOT:qmr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:2:1:3","qac_word_ref":"91:2:1","surface_ar":"قَمَرِ"}],"gloss":"ay ışığında yaklaşma, avı gafil yakalama ve avlama","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiye ay ışığında gitmek veya yaklaşmak dalın temel gece koşullu kullanımıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aslanın ya da avcının gece ava çıkması ve avın görüşünü şaşırtarak onu yakalaması özel avcılık gerçekleşmesidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birinin gafletini kollayıp onu hazırlıksız yakalamak veya aldatmak, avcılık görüntüsünden gelişen uzantıdır."}}],"root_ar":"ق م ر","root_id":"root_001255","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ay aydınlığında yaklaşma ile gece görüşü şaşan avı hazırlıksız yakalama çekirdeğini birlikte verir.","boundary_detail":"Dal yalnızca ay ışığında yaklaşma ve gece avında görüşü şaşırtıp gafil yakalama kullanımlarını kapsar; genel avlanma veya genel aldatma değildir.","branch_image_ar":"القصد أو الصيد في القمراء","concept_gloss":"ay ışığında yaklaşma, avı gafil yakalama ve avlama","contextual_glosses":[{"applicability":"Bir kişiye ay aydınlığında gitme veya yaklaşma yapısında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaklaşma eylemini ve ay ışığıyla belirlenen gece koşulunu korur."},"facet_ids":["F001"],"text":"ay ışığında yanına gitti","usage_role":"contextual"},{"applicability":"Kuş veya ceylanın gece görüşünü bozarak onu hazırlıksız yakalama bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Avın görüşünün şaşmasını, gafil yakalanmasını ve avlanma sonucunu korur."},"facet_ids":["F002"],"text":"gece görüşünü şaşırtıp avladı","usage_role":"contextual"}],"definition":"Birine ay ışığında yaklaşmayı veya gece ava çıkmayı anlatır; av bağlamında ışık ya da karanlık yüzünden görüşü şaşan hayvanı hazırlıksız yakalayıp avlama sonucuna uzanır. Bir kişinin gafletinden yararlanıp onu aldatma kullanımı da bu hazırlıksız yakalama çizgisine bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiye ay ışığında gitmek veya yaklaşmak dalın temel gece koşullu kullanımıdır."},{"facet_id":"F002","role":"specialization","statement":"Aslanın ya da avcının gece ava çıkması ve avın görüşünü şaşırtarak onu yakalaması özel avcılık gerçekleşmesidir."},{"facet_id":"F003","role":"extension","statement":"Birinin gafletini kollayıp onu hazırlıksız yakalamak veya aldatmak, avcılık görüntüsünden gelişen uzantıdır."}],"identity_rationale":"Kaynak ifadesi ay ışığında birine gitmeyi, avcının veya aslanın gece ava çıkmasını, kuş ya da ceylanların görüşünü şaşırtarak onları yakalamayı ve birinin gafletinden yararlanmayı aynı dalda toplar. Verilen çerçeve kullanılabilir, ancak anlam genel olarak yönelmek veya avlanmak değildir; ay aydınlığı, gece görüşü ya da hazırlıksız yakalama koşulu korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"ona ay ışığında gitti"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"aslan ay ışığında ava çıktı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kuşların gece görüşünü şaşırtıp onları avladılar"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ona ay ışığında gitti; gafletinden yararlanıp aldattı; başka bir açıklamada onunla evlenip onu götürdü"}],"lexicalization_note":"Tanım, birbirine bağlı fakat ayrı yapılardaki ay ışığında yaklaşma, gece ava çıkma ve avın görüşünü şaşırtma kullanımlarını karıştırmadan gösterir.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; gizlenerek ava sokulma dalı ortak avcılık ve gafil yakalama alanına rağmen yöntemdeki temel farkı en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda belirleyici koşul ay aydınlığı veya gece görüşünün şaşmasıdır; komşu dalda belirleyici yöntem avcının fiziksel olarak gizlenmesidir.","focus_only":"Ay ışığında yaklaşmayı ve gece görüşü şaşan avı hazırlıksız yakalamayı kapsar.","gloss":"gizlenerek ava sokulma","neighbor_only":"Avcıyı bir binek ya da başka bir örtü arkasında gizleyerek ava sokulmayı anlatır.","neighbor_ref":"root_000473/B003","relation_type":"near_neighbor","shared_zone":"İki dal da avın dikkatinden kaçıp ona yeterince yaklaşmayı ve ardından onu vurabilmeyi içerir."}],"source_phrase_ar":"تقمرته أتيته في القمراء (maqayis;sihah;mufradat)؛ تقمر الأسد إذا خرج في القمراء يطلب الصيد (maqayis;sihah)؛ قمر القوم الطير إذا عشوها ليلا فصادوها (maqayis)؛ تقمرها أتاها في القمراء وطلب غرتها وخدعها (tahdhib)؛ تقمر الصياد الظباء والطير بالليل فتقمر أبصارها فتصاد (tahdhib)","source_summary":"Kaynaklar ay ışığında yaklaşma ile gece avını ortak alanda verir; toplu ifade avın görüşünü şaşırtma, gafleti kollama ve aldatma ayrıntılarını da içerir, ancak bunlar genel aldatma anlamına dönüştürülmemelidir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه إتيان الشخص في القمراء، وخروج الأسد أو الصياد يطلب الصيد ليلا، وصيد الطير أو الظباء حين تغشى أبصارها بالليل أو الضوء.","what_is_not_ar":"لا يدخل فيه مطلق الخداع أو القمار إلا إذا كان النص يربطه بطلب الغرة أو تقمير الأبصار في الصيد."},"support_links":[]},{"boundary":"Dal yalnızca palmiye meyvesinin olgunlaşmadan önce soğuktan zarar görüp tadını yitirmesini kapsar.","branch_kind":"non_bare","branch_ref":"root_001255/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَمَر","morph_features":"STEM|POS:N|LEM:qamar|ROOT:qmr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:2:1:3","qac_word_ref":"91:2:1","surface_ar":"قَمَرِ"}],"gloss":"olgunlaşmadan soğuğa uğrayıp tatsızlaşma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Palmiye meyvesi henüz olgunlaşmadan soğuk tarafından zarar görür."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Soğuk zararı meyvenin tatlılığını ve tadını kaybetmesiyle sonuçlanır."}}],"root_ar":"ق م ر","root_id":"root_001255","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Palmiye meyvesinin olgunlaşma öncesi soğuk nedeniyle tadını yitirmesini anlatır.","boundary_detail":"Dal yalnızca palmiye meyvesinin olgunlaşmadan önce soğuktan zarar görüp tadını yitirmesini kapsar.","branch_image_ar":"تمر ضربه البرد قبل النضج","concept_gloss":"olgunlaşmadan soğuğa uğrayıp tatsızlaşma","contextual_glosses":[{"applicability":"Palmiye meyvesinin soğuk yüzünden olgunlaşamayıp tat kaybettiği cümlede kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Soğuk nedenini, erken evreyi ve tatsızlaşma sonucunu birlikte korur."},"facet_ids":["F001","F002"],"text":"soğuk vurunca olgunlaşmadan tatsızlaştı","usage_role":"contextual"}],"definition":"Palmiye meyvesinin olgunlaşmadan önce soğuğa uğraması ve bunun sonucunda tatlılığını ve tadını yitirmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Palmiye meyvesi henüz olgunlaşmadan soğuk tarafından zarar görür."},{"facet_id":"F002","role":"core","statement":"Soğuk zararı meyvenin tatlılığını ve tadını kaybetmesiyle sonuçlanır."}],"identity_rationale":"Kaynak ifadesi palmiye meyvesinin olgunlaşmadan önce soğuğa uğramasını ve bunun sonucunda tatlılığıyla tadını yitirmesini açık bir neden-sonuç dizisi olarak verir. Dal genel meyve bozulması değil, soğuğun olgunlaşma öncesindeki bu özel etkisidir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"palmiye meyvesi olgunlaşmadan soğuğa uğrayıp tadını ve tatlılığını yitirdi"}],"lexicalization_note":"Tanım, palmiye meyvesi ve olgunlaşma öncesi soğuk koşuluna bağlı özel kullanımla sınırlıdır.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; susuzluktan erken kuruma dalı, aynı meyve bozulması alanındaki neden ve sonuç farkını en yararlı biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dalda zarar veren etken soğuk ve belirgin sonuç tat kaybıdır; komşu dalda etken susuzluk, belirgin sonuç ise erken kuruma ve sertleşmedir.","focus_only":"Palmiye meyvesinin olgunlaşmadan önce soğuk yüzünden tatlılığını yitirmesini anlatır.","gloss":"susuzluktan erken kuruyan meyve","neighbor_only":"Meyvenin susuzluk nedeniyle olgunlaşmadan kurumasını ve farklı kuru ya da sert ürünleri kapsar.","neighbor_ref":"root_000695/B003","relation_type":"same_field","shared_zone":"İki dal da meyvenin normal olgunlaşma tamamlanmadan çevresel etkiyle bozulmasını anlatır."}],"source_phrase_ar":"قمر التمر وأقمر إذا ضربه البرد فذهبت حلاوته قبل أن ينضج (maqayis)؛ أقمر التمر أي لم ينضج حتى أصابه البرد فذهبت حلاوته وطعمه (ayn;tahdhib)؛ أقمر التمر ضربه البرد فذهبت حلاوته قبل أن ينضج (sihah)","source_summary":"Kaynaklar, olgunlaşma öncesinde soğuğa uğrayan palmiye meyvesinin tatlılığını yitirmesi üzerinde birleşir; bazı ifadeler genel tadın da kaybolduğunu ayrıca belirtir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه قمر التمر وأقمر التمر إذا أصابه البرد قبل أن ينضج فذهبت حلاوته وطعمه.","what_is_not_ar":"لا يدخل فيه فساد القربة ولا فساد آخر إلا إذا نص على التمر والبرد قبل النضج."},"support_links":[]},{"boundary":"Dal, kar beyazlığının gözü kamaştırıp görmeyi engellemesiyle sınırlıdır; doğuştan ya da kalıcı körlük değildir.","branch_kind":"non_bare","branch_ref":"root_001255/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَمَر","morph_features":"STEM|POS:N|LEM:qamar|ROOT:qmr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:2:1:3","qac_word_ref":"91:2:1","surface_ar":"قَمَرِ"}],"gloss":"kar beyazlığından gözü kamaşıp görememe","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kar beyazlığı kişinin gözünü kamaştırır ve görüşünü karıştırır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gözün kamaşması, kişinin o anda görememesi sonucuna ulaşır."}}],"root_ar":"ق م ر","root_id":"root_001255","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Karın parlak beyazlığının geçici görme güçlüğü yarattığı durumda kullanılır.","boundary_detail":"Dal, kar beyazlığının gözü kamaştırıp görmeyi engellemesiyle sınırlıdır; doğuştan ya da kalıcı körlük değildir.","branch_image_ar":"تحير البصر من بياض الثلج","concept_gloss":"kar beyazlığından gözü kamaşıp görememe","contextual_glosses":[{"applicability":"Bir kişinin kar beyazlığı içinde görüşünü geçici olarak yitirdiği cümlede uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kar ortamını, gözün kamaşmasını ve geçici görememe sonucunu korur."},"facet_ids":["F001","F002"],"text":"karda gözü kamaştı ve göremez oldu","usage_role":"contextual"}],"definition":"Karın yoğun beyazlığı karşısında gözün kamaşıp görüşün karışması ve kişinin bir süre göremez hale gelmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kar beyazlığı kişinin gözünü kamaştırır ve görüşünü karıştırır."},{"facet_id":"F002","role":"core","statement":"Gözün kamaşması, kişinin o anda görememesi sonucuna ulaşır."}],"identity_rationale":"Kaynak ifadesi kişinin karda gözünün şaşmasını, görüşünün karışmasını ve sonuçta görememesini doğrudan bildirir. Bu, genel körlükten farklı olarak kar beyazlığının doğurduğu geçici bir görme güçlüğüdür.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"kar beyazlığında gözü kamaşıp göremez oldu"}],"lexicalization_note":"Tanım, kişi ve kar koşulunu açıkça koruyan özel yapıyla sınırlıdır; genel görme kaybına yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; güneş ışığında görüşü bozulan göz dalı, ortak parlaklık etkisine rağmen ortam ve süre farkını en iyi ortaya koyar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın zorunlu ortamı kardır ve olay olarak göz kamaşmasını anlatır; komşu dal güneş altında ortaya çıkan daha kalıcı bir göz niteliğini betimler.","focus_only":"Karın beyazlığından gözü kamaşan kişinin o anda görememesini anlatır.","gloss":"güneş ışığında görüşü bozulan göz","neighbor_only":"Güneş ışığında göremeyen veya görüşü sersemleyen göz niteliğini, özellikle bazı hayvanlarda, kapsar.","neighbor_ref":"root_000269/B004","relation_type":"near_synonym","shared_zone":"İki dalda da güçlü bir aydınlık kaynağı görüşü bastırır ve geçici görememe doğurur."}],"source_phrase_ar":"قمر الرجل إذا لم يبصر في الثلج (maqayis;sihah)؛ قمر الرجل إذا حار بصره في الثلج فلم يبصر (tahdhib)","source_summary":"Kaynaklar kar içinde görememe üzerinde birleşir; daha ayrıntılı anlatım bunu kar beyazlığının görüşü şaşırtıp gözü kamaştırmasıyla açıklar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه قمر الرجل إذا لم يبصر أو حار بصره في الثلج.","what_is_not_ar":"لا يدخل فيه تقمير أبصار الصيد إلا من جهة غشيان البصر؛ صيد الليل محفوظ في B003."},"support_links":[]},{"boundary":"Dal genel deri hasarını değil, su tulumunun ay aydınlığıyla ilişkilendirilen yanık benzeri ya da katman arası su kaynaklı bozulmasını anlatır.","branch_kind":"non_bare","branch_ref":"root_001255/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَمَر","morph_features":"STEM|POS:N|LEM:qamar|ROOT:qmr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:2:1:3","qac_word_ref":"91:2:1","surface_ar":"قَمَرِ"}],"gloss":"su tulumunun ay aydınlığı ya da katman arası suyla bozulması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Su tulumu, yüzeyinde ya da deri yapısında oluşan özel bir hasarla bozulur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hasar ay aydınlığının yaptığı yanığa benzetilir veya suyun deri katmanları arasına girmesiyle açıklanır."}}],"root_ar":"ق م ر","root_id":"root_001255","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Su tulumundaki yanık benzeri veya deri katmanları arasındaki suya bağlı hasarı birlikte karşılar.","boundary_detail":"Dal genel deri hasarını değil, su tulumunun ay aydınlığıyla ilişkilendirilen yanık benzeri ya da katman arası su kaynaklı bozulmasını anlatır.","branch_image_ar":"قربة أفسدتها القمراء","concept_gloss":"su tulumunun ay aydınlığı ya da katman arası suyla bozulması","contextual_glosses":[{"applicability":"Suyun deri katmanları arasına girmesiyle oluşan hasar açıklaması öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Su tulumunu, katmanlar arasına su girişini ve bozulma sonucunu korur."},"facet_ids":["F001","F002"],"text":"su tulumu katmanlarına su girince bozuldu","usage_role":"contextual"}],"definition":"Bir su tulumunun ay aydınlığından yanmış gibi bozulması veya suyun derinin dış ve iç katmanları arasına girerek çürüme ve hasar oluşturmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Su tulumu, yüzeyinde ya da deri yapısında oluşan özel bir hasarla bozulur."},{"facet_id":"F002","role":"source_variant","statement":"Hasar ay aydınlığının yaptığı yanığa benzetilir veya suyun deri katmanları arasına girmesiyle açıklanır."}],"identity_rationale":"Kaynak ifadesi su tulumunda yanığa benzer bir bozulmayı ve suyun deri katmanları arasına girmesini aynı özel kullanımın açıklamaları olarak verir. Çerçeve bu iki açıklamayı da koruduğu sürece kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"su tulumu ay aydınlığından yanmış gibi ya da su deri katmanları arasına girdiği için bozuldu"}],"lexicalization_note":"Tanım yalnızca su tulumuna bağlı özel kullanımı kapsar ve buradan genel bozulma anlamı çıkarmaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; deri ya da su tulumundaki yarık dalı, aynı nesnede görülen fakat yapısı farklı hasarı en açık biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal katman yapısındaki bozulma ve çürümedir; komşu dal ise malzemenin fiziksel olarak yarılması veya delinmesidir.","focus_only":"Su tulumunun ay aydınlığı veya deri katmanları arasına giren su yüzünden bozulmasını anlatır.","gloss":"deri veya su tulumundaki yarık","neighbor_only":"Deri, kumaş ya da su tulumunda oluşan fiziksel yarık, delik veya küçük söküğü anlatır.","neighbor_ref":"root_001688/B002","relation_type":"same_field","shared_zone":"Her iki dal da deri eşyanın, özellikle su tulumunun işlevini bozan bir hasarı kapsar."}],"source_phrase_ar":"قمرت القربة وهو شيء يصيبها كالاحتراق من القمر (maqayis)؛ قمرت القربة... يصيبها من القمر كالاحتراق فيدخل الماء بين الأدمة والبشرة (sihah)؛ قمرت القربة... دخل الماء بين الأدمة والبشرة فأصابها قضاء وفساد (tahdhib)؛ قمرت القربة فسدت بالقمراء (mufradat)","source_summary":"Kaynaklar su tulumunun bozulduğunu ortak biçimde bildirir; açıklamalar ay aydınlığının yaptığı yanık benzeri etki ile suyun deri katmanları arasına girmesi arasında değişir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه قمرت القربة إذا أصابها من القمر كالاحتراق أو دخل الماء بين الأدمة والبشرة فأصابها فساد.","what_is_not_ar":"لا يدخل فيه فساد التمر بالبرد ولا فساد عام غير منصوص."},"support_links":[]},{"boundary":"Dal, ortaya değer koyulan talih oyunu, bu oyunda rakip arama ve yenme ile hileli aldatma uzantısını kapsar; her tür risk alma değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001255/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَمَر","morph_features":"STEM|POS:N|LEM:qamar|ROOT:qmr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:2:1:3","qac_word_ref":"91:2:1","surface_ar":"قَمَرِ"}],"gloss":"değer ortaya koyulan talih oyununda karşılaşma, yenme ve aldatma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, bir değer ortaya koyulan talih oyununda tarafların karşılıklı oynamasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir rakip aramak, onunla karşılaşmak ve oyunda onu yenmek eylem zincirinin özel aşamalarıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birini hileyle aldatıp ondan üstün çıkmak, oyun çekirdeğinden gelişen fakat her oyunda zorunlu olmayan uzantıdır."}}],"root_ar":"ق م ر","root_id":"root_001255","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Karşılıklı oyunu, rakibi yenmeyi ve hileli aldatma uzantısını birlikte gösteren genel açıklamadır.","boundary_detail":"Dal, ortaya değer koyulan talih oyunu, bu oyunda rakip arama ve yenme ile hileli aldatma uzantısını kapsar; her tür risk alma değildir.","branch_image_ar":"المقامرة والغلبة بالخداع","concept_gloss":"değer ortaya koyulan talih oyununda karşılaşma, yenme ve aldatma","contextual_glosses":[{"applicability":"İki kişinin karşılıklı oynadığı ve birinin ötekini yendiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı oynama eylemini ve rakibe üstün gelme sonucunu korur."},"facet_ids":["F001","F002"],"text":"onunla talih oyununda yarışıp onu yendi","usage_role":"contextual"},{"applicability":"Oyun çekirdeğinden uzanan hile ve aldatma kullanımı cümlede öne çıktığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hile kullanarak karşı tarafı aldatma eylemini korur."},"facet_ids":["F003"],"text":"onu hileyle aldattı","usage_role":"contextual"}],"definition":"Para ya da mal gibi bir değer ortaya koyulan talih oyununda karşılıklı oynamayı ve rakibi yenmeyi anlatır. Oynayacak rakip arama ve birini hileyle aldatarak üstün gelme anlamları bu çekirdeğe bağlı uzantılardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, bir değer ortaya koyulan talih oyununda tarafların karşılıklı oynamasıdır."},{"facet_id":"F002","role":"specialization","statement":"Bir rakip aramak, onunla karşılaşmak ve oyunda onu yenmek eylem zincirinin özel aşamalarıdır."},{"facet_id":"F003","role":"extension","statement":"Birini hileyle aldatıp ondan üstün çıkmak, oyun çekirdeğinden gelişen fakat her oyunda zorunlu olmayan uzantıdır."}],"identity_rationale":"Kaynak ifadesinin çekirdeği para veya mal ortaya konan talih oyununda karşılaşma ve rakibi yenmedir; rakip arama ve hileyle aldatma bununla bağlantılı uzantılardır. Çerçevedeki aldatma unsuru bütün oyun eylemlerinin zorunlu özelliği gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"para ya da mal ortaya konan talih oyunu ve bu oyunda karşılıklı yarışma"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"onunla talih oyununda yarışıp onu yendi"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"oynayacak rakip aradı ya da rakibini yendi"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"onu hileyle aldattı"}],"lexicalization_note":"Tanım, oyun adını ve karşılıklı oynama çekirdeğini rakip arama, yenme ve aldatma bildiren yapılardan ayırarak korur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; geniş bahis ve risk dalı, talih oyunu çekirdeğiyle en yakın örtüşmeyi ve kapsam farkını birlikte gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal talih oyunu ve rakibe karşı kazanma çevresinde kuruludur; komşu dal oyun türüyle sınırlı olmayan daha geniş bahis ve risk alanını kapsar.","focus_only":"Talih oyununda karşılıklı oynama, rakip arama, rakibi yenme ve hileyle aldatma uzantısını taşır.","gloss":"bahse girme ve değer ortaya koyma","neighbor_only":"At yarışı gibi beceri yarışları dahil daha geniş biçimde bahse girme ve bir şeyi tehlikeye atmayı kapsar.","neighbor_ref":"root_000607/B004","relation_type":"near_synonym","shared_zone":"İki dalda da belirsiz bir sonuç üzerine değer ortaya koyma ve taraflar arasında yarışma bulunur."}],"source_phrase_ar":"القمار من المقامرة... تقمر الرجل إذا طلب من يقامره (maqayis)؛ قامرته فقمرته من القمار (ayn)؛ تقمر فلان أي غلب من يقامره وتقامروا لعبوا القمار وقمرت الرجل إذا لاعبته فغلبته (sihah)؛ القمار مأخوذ من الخداع يقال قامره بالخداع فقمره (tahdhib)؛ قمرت فلانا خدعته عنه (mufradat)","source_summary":"Kaynaklar karşılıklı talih oyunu ve rakibi yenme çekirdeğinde birleşir; toplu ifade rakip arama, övünme yarışı ve hileyle aldatma ayrıntılarını da farklı ağırlıklarla kapsar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه القمار والمقامرة، قامرته أو لاعبته فغلبته، وتقامروا، وتقمر الرجل إذا طلب من يقامره، وقمر فلانا بمعنى خدعه عنه.","what_is_not_ar":"لا يدخل فيه صيد القمراء إلا إذا كان النص على طلب الغرة في الصيد؛ ولا يلزم منه أصل البياض."},"support_links":[]},{"boundary":"Dal yalnızca suyun ve otlağın bol olmasını anlatır; genel çokluk veya her tür verimlilik anlamına genişletilmez.","branch_kind":"non_bare","branch_ref":"root_001255/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَمَر","morph_features":"STEM|POS:N|LEM:qamar|ROOT:qmr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:2:1:3","qac_word_ref":"91:2:1","surface_ar":"قَمَرِ"}],"gloss":"su ve otlağın bol olması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Su ve otlak birlikte çoğalır veya bol hale gelir."}}],"root_ar":"ق م ر","root_id":"root_001255","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Su kaynakları ile otlak bitkilerinin birlikte çok bulunduğu yer veya dönem için uygundur.","boundary_detail":"Dal yalnızca suyun ve otlağın bol olmasını anlatır; genel çokluk veya her tür verimlilik anlamına genişletilmez.","branch_image_ar":"كثرة الماء والكلأ","concept_gloss":"su ve otlağın bol olması","contextual_glosses":[{"applicability":"Bir yerin su ve otlak bakımından zengin olduğunu bildiren cümlede kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Su ve otlağın birlikte bol bulunması durumunu korur."},"facet_ids":["F001"],"text":"suyu ve otlağı boldu","usage_role":"contextual"}],"definition":"Bir yerde suyun ve hayvanların otlayacağı bitki örtüsünün bol miktarda bulunmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Su ve otlak birlikte çoğalır veya bol hale gelir."}],"identity_rationale":"Tek kaynak ifadesi su ile otlağın çoğalmasını aynı dar kullanımda doğrudan bildirir. Çerçeve, bolluğu yalnızca bu iki varlıkla sınırladığı için kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"su ve otlak bol oldu"}],"lexicalization_note":"Tanım, su ile otlağı birlikte konu alan özel yapıya bağlıdır ve yalın bir genel çokluk anlamı üretmez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; genel çokluk dalı, su ve otlakla sınırlı bu kullanımın neden yalın bir çokluk anlamı olmadığını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal su ve otlakla sınırlı özel bir kullanımdır; komşu dal ise nesne türü sınırlaması olmadan genel nicelik artışını anlatır.","focus_only":"Çokluğu yalnızca su ile hayvanların otlayacağı bitki örtüsüne bağlı bir yapıda anlatır.","gloss":"genel çokluk ve sayıca artma","neighbor_only":"Nesne, sayı, para ve başka alanlardaki genel çokluğu, çoğalmayı ve çoğaltmayı kapsar.","neighbor_ref":"root_001286/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak çekirdeği bir şeyin az değil, çok miktarda bulunmasıdır."}],"source_phrase_ar":"قمر الماء والكلأ إذا كثر (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kayıt, suyun ve otlağın çoğalmasını aynı yapı içinde bildirir."}],"source_summary":"Bu dal, su ile otlağın birlikte bolluğunu bildiren dar kapsamlı bir kullanımdır.","sources":["TA"],"what_is_ar":"يدخل فيه قمر الماء والكلأ إذا كثر.","what_is_not_ar":"لا يدخل فيه ضوء القمر أو بياضه إلا إن نص المصدر على الكثرة."},"support_links":[]},{"boundary":"Dal, ay aydınlığında uykunun kaçıp kişinin uyuyamamasını anlatır; başka koşullardaki genel uykusuzluğu kapsamaz.","branch_kind":"non_bare","branch_ref":"root_001255/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَمَر","morph_features":"STEM|POS:N|LEM:qamar|ROOT:qmr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:2:1:3","qac_word_ref":"91:2:1","surface_ar":"قَمَرِ"}],"gloss":"ay ışığında uykusu kaçıp uyuyamama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin ay aydınlığında uykusu kaçar ve kişi uyuyamaz."}}],"root_ar":"ق م ر","root_id":"root_001255","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin ay aydınlığında uykusunun kaçıp uyuyamadığı gece durumu için kullanılır.","boundary_detail":"Dal, ay aydınlığında uykunun kaçıp kişinin uyuyamamasını anlatır; başka koşullardaki genel uykusuzluğu kapsamaz.","branch_image_ar":"الأرق في ضوء القمر","concept_gloss":"ay ışığında uykusu kaçıp uyuyamama","contextual_glosses":[{"applicability":"Kişinin ay aydınlığında gece uyuyamadığını anlatan cümlede uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ay ışığı koşulunu ve uykunun kaçması durumunu korur."},"facet_ids":["F001"],"text":"ay ışığında uykusu kaçtı","usage_role":"contextual"}],"definition":"Kişinin ay aydınlığında uykusunun kaçması ve gece uyuyamamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin ay aydınlığında uykusu kaçar ve kişi uyuyamaz."}],"identity_rationale":"Tek kaynak ifadesi kişinin ay aydınlığında uykusunun kaçmasını ve uyuyamamasını açıkça verir. Bu nedenle dal genel uykusuzluk değil, ay ışığı koşulunda yaşanan uyanıklık durumudur.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"ay ışığında uykusu kaçtı ve uyuyamadı"}],"lexicalization_note":"Tanım, kişi ile ay aydınlığını birlikte gerektiren özel yapıya bağlıdır ve yalın uyuyamama anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel uykusuzluk dalı çekirdekteki örtüşmeyi ve ay ışığına bağlı neden sınırlamasını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda ay aydınlığı zorunlu nedendir; komşu dal ise neden belirtmeyen genel uykusuzluğu ve ettirgen kullanımları da taşır.","focus_only":"Uykusuzluğu özellikle ay aydınlığının etkisine bağlayan dar bir gece kullanımını anlatır.","gloss":"genel uykusuzluk ve uyanık kalma","neighbor_only":"Nedeni ay ışığıyla sınırlı olmayan uykusuzluğu ve bir başkasını uyanık bırakmayı da kapsar.","neighbor_ref":"root_000752/B001","relation_type":"near_synonym","shared_zone":"İki dalda da kişi gece uyuyamaz ve uyanık kalır."}],"source_phrase_ar":"قمر الرجل أرق في القمر فلم ينم (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kayıt, kişinin ay ışığında uykusu kaçtığı için uyuyamamasını bildirir."}],"source_summary":"Bu dal, ay aydınlığında yaşanan uykusuzluğu anlatan dar kapsamlı bir kullanımdır.","sources":["TA"],"what_is_ar":"يدخل فيه قمر الرجل إذا أرق في القمر فلم ينم.","what_is_not_ar":"لا يدخل فيه مجرد قيام الليل أو الخروج للصيد في القمراء."},"support_links":[]},{"boundary":"Dal yalnızca develerin akşam yemeğinin gecikmesini kapsar; genel açlık, geç kalma veya otlama değildir.","branch_kind":"non_bare","branch_ref":"root_001255/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَمَر","morph_features":"STEM|POS:N|LEM:qamar|ROOT:qmr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:2:1:3","qac_word_ref":"91:2:1","surface_ar":"قَمَرِ"}],"gloss":"develerin akşam yeminin gecikmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Develerin akşam yemi veya akşam beslenmesi gecikir."}}],"root_ar":"ق م ر","root_id":"root_001255","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Develerin akşam beslenmesinin olağan saatten sonraya kaldığı durumda kullanılır.","boundary_detail":"Dal yalnızca develerin akşam yemeğinin gecikmesini kapsar; genel açlık, geç kalma veya otlama değildir.","branch_image_ar":"تأخر عشاء الإبل","concept_gloss":"develerin akşam yeminin gecikmesi","contextual_glosses":[{"applicability":"Akşam öğününün develere geç verildiğini bildiren cümlede uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvan türünü, akşam öğününü ve gecikme durumunu korur."},"facet_ids":["F001"],"text":"develerin akşam yemi gecikti","usage_role":"contextual"}],"definition":"Develere akşam verilmesi gereken yemin olağan vaktinden sonraya kalmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Develerin akşam yemi veya akşam beslenmesi gecikir."}],"identity_rationale":"Tek kaynak ifadesi develerin akşam yemeğinin gecikmesini doğrudan bildirir. Dal genel gecikme ya da hayvanların yorgun kalması değil, belirli hayvanların akşam beslenmesindeki zaman kaymasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"develerin akşam yemi gecikti"}],"lexicalization_note":"Tanım, develer ile akşam yemeğinin gecikmesini birlikte gerektiren özel yapıyla sınırlıdır.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; akşam yemeği ve beslenme dalı, aynı zaman ve katılımcı alanında gecikme çekirdeğini ayıran en yararlı komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği beslenme eylemi değil, akşam öğününün gecikmesidir; komşu dal ise öğün, yeme, yedirme ve otlama eylemlerini kapsar.","focus_only":"Develerin akşam yemeğinin olağan vaktinden sonraya kalmasını anlatır.","gloss":"akşam yemeği ve akşam beslenmesi","neighbor_only":"Akşam yemeğinin kendisini, onu yemeyi veya yedirmeyi ve hayvanların akşam ya da öğleden sonra otlamasını kapsar.","neighbor_ref":"root_001017/B005","relation_type":"near_neighbor","shared_zone":"İki dal da akşam vaktinde hayvanların yemesi veya beslenmesi alanındadır."}],"source_phrase_ar":"قمرت الإبل إذا تأخر عشاؤها (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kayıt, develerin akşam yemeğinin olağan vaktinden sonraya kalmasını bildirir."}],"source_summary":"Bu dal, develerin akşam beslenmesindeki gecikmeyi anlatan dar kapsamlı bir kullanımdır.","sources":["TA"],"what_is_ar":"يدخل فيه قمرت الإبل إذا تأخر عشاؤها.","what_is_not_ar":"لا يدخل فيه تأخر عام أو إهمال مال ليلا إلا بنص مستقل."},"support_links":[]},{"boundary":"Dal yalnızca malı veya hayvan sürüsünü gece çobansız ve korumasız bırakmayı bildiren özel yapıyı kapsar.","branch_kind":"collocation","branch_ref":"root_001255/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَمَر","morph_features":"STEM|POS:N|LEM:qamar|ROOT:qmr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:2:1:3","qac_word_ref":"91:2:1","surface_ar":"قَمَرِ"}],"gloss":"hayvan sürüsünü gece çobansız ve gözetimsiz bırakma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Mülk veya hayvan sürüsü gece koruyucu bir çoban olmadan gözetimsiz bırakılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ay ve güneşle kurulan karşılaştırmalı ifade, gece ve gündüz boyunca ihmal etmeme ya da başıboş bırakmama karşıtlığını taşır."}}],"root_ar":"ق م ر","root_id":"root_001255","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sürünün gece boyunca onu koruyacak bir çoban olmadan başıboş bırakıldığı durumda kullanılır.","boundary_detail":"Dal yalnızca malı veya hayvan sürüsünü gece çobansız ve korumasız bırakmayı bildiren özel yapıyı kapsar.","branch_image_ar":"إهمال المال ليلا للقمر","concept_gloss":"hayvan sürüsünü gece çobansız ve gözetimsiz bırakma","contextual_glosses":[{"applicability":"Bir hayvan sürüsünü gece koruyucu olmadan bırakma eylemini anlatan cümlede uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sürüyü, geceyi ve çoban gözetiminin bulunmamasını korur."},"facet_ids":["F001"],"text":"sürüyü gece çobansız bıraktım","usage_role":"contextual"}],"definition":"Malı veya hayvan sürüsünü gece boyunca onu koruyacak bir çoban ya da gözeten kimse olmadan başıboş bırakmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Mülk veya hayvan sürüsü gece koruyucu bir çoban olmadan gözetimsiz bırakılır."},{"facet_id":"F002","role":"specialization","statement":"Ay ve güneşle kurulan karşılaştırmalı ifade, gece ve gündüz boyunca ihmal etmeme ya da başıboş bırakmama karşıtlığını taşır."}],"identity_rationale":"Kaynak ifadesi malı gece boyunca çobansız ve koruyucusuz bırakmayı açıkça tanımlar; gündüz güneş altında bırakma ile gece ay altında bırakma karşıtlığı da ihmal anlamını pekiştirir. Bu, genel otlatma değil, gözetimsiz bırakma yapısıdır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"hayvan sürüsünü gece çobansız ve gözetimsiz bıraktım"}],"lexicalization_note":"Tanım bütünüyle verilen gece ve ay öğeli yapıya bağlıdır; buradan Ay'ın yalın anlamına ya da genel otlatmaya geçilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sürünün gece başıboş yayılması dalı, ortak gece ve gözetimsizlik alanına rağmen eyleyen ile sonuç farkını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sahibin gözetimi kaldırarak sürüyü ihmal etmesine odaklanır; komşu dal sürünün fiilen dağılması, yayılması ya da gece otlamasına odaklanır.","focus_only":"Mülk sahibinin sürüyü gece boyunca koruyucu bir çoban olmadan bırakma eylemini anlatır.","gloss":"sürünün gece başıboş yayılması","neighbor_only":"Hayvanların gece kendiliğinden dağılmasını, otlamasını veya sahibinin onları gece otlağa salmasını kapsar.","neighbor_ref":"root_001534/B003","relation_type":"near_synonym","shared_zone":"İki dalda da hayvan sürüsü gece vakti çoban gözetimi dışında kalabilir."}],"source_phrase_ar":"استرعيت مالي القمر إذا تركته هملا ليلا بلا راع يحفظه (tahdhib)؛ لم أسترعها الشمس والقمر أي لم أهملها (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kayıt, malı gece koruyucu bir çoban olmadan başıboş bırakmayı ve bunun tersini karşılaştırmalı biçimde açıklar."}],"source_summary":"Bu dal, malın gece boyunca çobansız bırakılmasını anlatan ve ay ile güneş karşıtlığıyla ihmal sınırını belirleyen özel bir kullanımdır.","sources":["TA"],"what_is_ar":"يدخل فيه استرعيت مالي القمر إذا ترك المال هملا ليلا بلا راع يحفظه، في مقابلة استرعيته الشمس نهارا.","what_is_not_ar":"لا يدخل فيه كل رعي أو كل قمر سماوي؛ هذا فرع تعبيري في الإهمال الليلي."},"support_links":[]},{"boundary":"Dal belirli bir kuş adıdır; genel olarak bütün güvercinleri, bütün üveyikleri veya benzer ad taşıyan başka nesneleri kapsamaz.","branch_kind":"bare","branch_ref":"root_001255/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَمَر","morph_features":"STEM|POS:N|LEM:qamar|ROOT:qmr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:2:1:3","qac_word_ref":"91:2:1","surface_ar":"قَمَرِ"}],"gloss":"üveyik ya da güvercin benzeri kuş","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dalın çekirdeği, güvercin türlerine yakın belirli bir kuşun adıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuş üveyiğe veya güvercine benzetilir; bir aktarım Hicaz'ı yaşam alanı olarak belirtir."}}],"root_ar":"ق م ر","root_id":"root_001255","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli kuşu yakın görünümlü güvercin türleri üzerinden açıklamak için uygundur.","boundary_detail":"Dal belirli bir kuş adıdır; genel olarak bütün güvercinleri, bütün üveyikleri veya benzer ad taşıyan başka nesneleri kapsamaz.","branch_image_ar":"طائر القمري والقمارى","concept_gloss":"üveyik ya da güvercin benzeri kuş","contextual_glosses":[{"applicability":"Kuş türünün kesin hedef dil adı yerine görünüş benzerliğiyle açıklandığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli bir kuş olduğunu ve güvercine benzediğini korur."},"facet_ids":["F001","F002"],"text":"güvercine benzeyen bir kuş","usage_role":"explanatory"}],"definition":"Üveyiğe benzeyen veya güvercin türlerine yakın görülen belirli bir kuştur; kaynaklar görünüş benzerliğini farklı kuşlarla açıklar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dalın çekirdeği, güvercin türlerine yakın belirli bir kuşun adıdır."},{"facet_id":"F002","role":"source_variant","statement":"Kuş üveyiğe veya güvercine benzetilir; bir aktarım Hicaz'ı yaşam alanı olarak belirtir."}],"identity_rationale":"Kaynak ifadesi üveyiğe benzeyen veya güvercini andıran belirli bir kuşu tanımlar ve çoğul biçimini verir. Bir aktarım Hicaz'ı kuşun yaşam alanı olarak belirtir; bu ayrıntı kuş kimliğinin çekirdeğini değiştirmez.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"üveyik ya da güvercin benzeri kuş ve bu kuşların çoğulu"}],"lexicalization_note":"Tanım yalın kuş adıyla sınırlıdır; yer adından türemiş başka nesne adları ya da Ay'la ilgili anlamlar bu dala alınmaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; üveyik adıyla ilgili dal, görünüş benzerliğine rağmen ayrı kuş adlarının özdeş sayılmaması gerektiğini en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal üveyiğe benzetilerek tanımlanan ayrı bir kuş adıdır; komşu dal ise üveyiğin kendisi için veya ona benzeyen başka bir kuş için kullanılan farklı addır.","focus_only":"Güvercine yakın ve üveyiğe benzetilen belirli kuşu, kendi tekil ve çoğul adlarıyla belirtir.","gloss":"üveyik adı veya üveyiğe benzeyen kuş","neighbor_only":"Ayrı bir kuş adı olarak doğrudan üveyiği veya ona benzeyen başka bir kuşu belirtir.","neighbor_ref":"root_000878/B004","relation_type":"near_neighbor","shared_zone":"İki dal da güvercin ailesine yakın görülen ve üveyikle ilişkilendirilen kuş adlarını kapsar."}],"source_phrase_ar":"القمري طائر كالفاختة مسكنه الحجاز (ayn)؛ القمرى منسوب إلى طير قمر والجمع قماري (sihah)؛ القمري طائر يشبه الحمام (tahdhib)","source_summary":"Kaynaklar belirli bir kuş adında birleşir; kuşu üveyiğe ya da güvercine benzeterek açıklar, bir anlatım ayrıca Hicaz'ı kuşun yaşam alanı olarak belirtir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه القمري أو طير قمر، طائر كالفاختة أو يشبه الحمام، ومسكنه الحجاز، وجمعه قماري.","what_is_not_ar":"لا يدخل فيه عود قماري المنسوب إلى موضع ببلاد الهند إلا كنسبة مكانية لا كصورة الطائر."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["91:2:1"],"branch_refs":[],"candidate_id":"cand_41176d78570278eec078","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:2:1:audible-liaison","source_type":"word_analysis","support_ids":["sup_0676a5bc7de60e8c3e04","sup_ad307fb0c208814b76e4"],"title":"bound sound makes attachment audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:1","qac_refs":["91:2:1:1"],"status":"accepted"}},{"anchor_refs":["91:2:1"],"branch_refs":[],"candidate_id":"cand_3eb4365f66e8d630b253","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:2:1:chain-continuation","source_type":"word_analysis","support_ids":["sup_0676a5bc7de60e8c3e04","sup_f5069b6ed8ec2fd1db15"],"title":"ayah boundary remains in the oath chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:1","qac_refs":["91:2:1:1"],"status":"accepted"}},{"anchor_refs":["91:2:1"],"branch_refs":[],"candidate_id":"cand_a1e45b7e0eaf8cb3cce6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:2:1:oath-governance","source_type":"word_analysis","support_ids":["sup_0676a5bc7de60e8c3e04","sup_cfa94a2060bd4a2eb3ae"],"title":"qasam force governs the moon phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:1","qac_refs":["91:2:1:1"],"status":"accepted"}},{"anchor_refs":["91:2:2"],"branch_refs":[],"candidate_id":"cand_7d37f3ad76d2444bc3ef","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001255"],"scope":"focus_ayah","source_local_id":"91:2:2:article-sound-contrast","source_type":"word_analysis","support_ids":["sup_273a339522f40eb140ba","sup_b237d30d5aeec8058f60"],"title":"audible article distinguishes the moon","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:2","qac_refs":["91:2:1:2","91:2:1:3"],"status":"accepted"}},{"anchor_refs":["91:2:2"],"branch_refs":[],"candidate_id":"cand_a0a1209f5a5862df99fb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001255"],"scope":"focus_ayah","source_local_id":"91:2:2:definite-genitive-witness","source_type":"word_analysis","support_ids":["sup_273a339522f40eb140ba","sup_9c63015da919943d52b9"],"title":"recognized moon as sworn witness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:2","qac_refs":["91:2:1:2","91:2:1:3"],"status":"accepted"}},{"anchor_refs":["91:2:2"],"branch_refs":[],"candidate_id":"cand_5f673910bae410c51f7d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001255"],"scope":"focus_ayah","source_local_id":"91:2:2:intertext-pair-horizon","source_type":"word_analysis","support_ids":["sup_273a339522f40eb140ba","sup_dce70d655b939e368723"],"title":"stable pair against disruption horizon","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:2","qac_refs":["91:2:1:2","91:2:1:3"],"status":"accepted"}},{"anchor_refs":["91:2:2"],"branch_refs":[],"candidate_id":"cand_33fa1ddb840f378cf7fb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001255"],"scope":"focus_ayah","source_local_id":"91:2:2:lunar-light-narrowing","source_type":"word_analysis","support_ids":["sup_273a339522f40eb140ba","sup_9f5c3b395c72b5cbc426"],"title":"lunar radiance narrowed to the concrete moon","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:2","qac_refs":["91:2:1:2","91:2:1:3"],"status":"accepted"}},{"anchor_refs":["91:2:2"],"branch_refs":[],"candidate_id":"cand_b08b553d45798b1aad99","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001255"],"scope":"focus_ayah","source_local_id":"91:2:2:oath-object-subject-role","source_type":"word_analysis","support_ids":["sup_273a339522f40eb140ba","sup_4683dc9566279ee63b0f"],"title":"witness becomes actor","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:2","qac_refs":["91:2:1:2","91:2:1:3"],"status":"accepted"}},{"anchor_refs":["91:2:2"],"branch_refs":[],"candidate_id":"cand_4ff7572ef7a106712470","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001255"],"scope":"focus_ayah","source_local_id":"91:2:2:structured-oath-series","source_type":"word_analysis","support_ids":["sup_273a339522f40eb140ba","sup_62547779415f21f5ed4b"],"title":"entity joined to relational condition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:2","qac_refs":["91:2:1:2","91:2:1:3"],"status":"accepted"}},{"anchor_refs":["91:2:2"],"branch_refs":[],"candidate_id":"cand_9e726223223e32931d2d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001255"],"scope":"focus_ayah","source_local_id":"91:2:2:sun-moon-pair","source_type":"word_analysis","support_ids":["sup_273a339522f40eb140ba","sup_905f40a9071b403b310c"],"title":"sun and moon made a grammatical pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:2","qac_refs":["91:2:1:2","91:2:1:3"],"status":"accepted"}},{"anchor_refs":["91:2:3"],"branch_refs":[],"candidate_id":"cand_032e51456aa6f7f453a3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:2:3:hamza-onset","source_type":"word_analysis","support_ids":["sup_bd95c5d354a632e8a37f","sup_c32414b67baa02a750e1"],"title":"pronounced onset marks the hinge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:3","qac_refs":["91:2:2:1"],"status":"accepted"}},{"anchor_refs":["91:2:3"],"branch_refs":[],"candidate_id":"cand_1080d5d16eb0e7541e8c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:2:3:opening-parallel","source_type":"word_analysis","support_ids":["sup_73b029fe9660c90a2e75","sup_c32414b67baa02a750e1"],"title":"parallel temporal pattern with 91:1","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:3","qac_refs":["91:2:2:1"],"status":"accepted"}},{"anchor_refs":["91:2:3"],"branch_refs":[],"candidate_id":"cand_40e7b2e5933d7523c311","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:2:3:structural-hinge","source_type":"word_analysis","support_ids":["sup_c32414b67baa02a750e1","sup_c77194c2c1b76fba487f"],"title":"visible hinge from noun to event","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:3","qac_refs":["91:2:2:1"],"status":"accepted"}},{"anchor_refs":["91:2:3"],"branch_refs":[],"candidate_id":"cand_4062a9902d0048dd1ac5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:2:3:temporal-restrictor","source_type":"word_analysis","support_ids":["sup_a069d540bc06c3774ebb","sup_c32414b67baa02a750e1"],"title":"oath narrowed to a recurring moment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:3","qac_refs":["91:2:2:1"],"status":"accepted"}},{"anchor_refs":["91:2:4"],"branch_refs":[],"candidate_id":"cand_1ce64e45b1a134fe42b3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000185","root_000186"],"scope":"focus_ayah","source_local_id":"91:2:4:ayah-closing-cadence","source_type":"word_analysis","support_ids":["sup_2ca8939bcc34c0fb5e36","sup_3e8479a9e04db5c0616a"],"title":"final cadence binds adjacent oaths","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:4","qac_refs":["91:2:3:1","91:2:3:2"],"status":"accepted"}},{"anchor_refs":["91:2:4"],"branch_refs":[],"candidate_id":"cand_c98bc07c7f61ae02cbc8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000185","root_000186"],"scope":"focus_ayah","source_local_id":"91:2:4:boundary-shift","source_type":"word_analysis","support_ids":["sup_23d4a8277376a7ed5366","sup_3e8479a9e04db5c0616a"],"title":"brightness becomes following event","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:4","qac_refs":["91:2:3:1","91:2:3:2"],"status":"accepted"}},{"anchor_refs":["91:2:4"],"branch_refs":[],"candidate_id":"cand_f9f464b7b6e10696ee42","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000185","root_000186"],"scope":"focus_ayah","source_local_id":"91:2:4:convergent-final-word","source_type":"word_analysis","support_ids":["sup_3e8479a9e04db5c0616a","sup_4865ac60d8995706d141"],"title":"grammar sound and sense converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:4","qac_refs":["91:2:3:1","91:2:3:2"],"status":"accepted"}},{"anchor_refs":["91:2:4"],"branch_refs":[],"candidate_id":"cand_d67cef476d49b40789a3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000185","root_000186"],"scope":"focus_ayah","source_local_id":"91:2:4:cross-ayah-object-suffix","source_type":"word_analysis","support_ids":["sup_3e8479a9e04db5c0616a","sup_c9820d8dca4e1a64f383"],"title":"feminine object points back to 91:1","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:4","qac_refs":["91:2:3:1","91:2:3:2"],"status":"accepted"}},{"anchor_refs":["91:2:4"],"branch_refs":[],"candidate_id":"cand_106ffa16bbe827c0fa4c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000185","root_000186"],"scope":"focus_ayah","source_local_id":"91:2:4:finite-event-not-category","source_type":"word_analysis","support_ids":["sup_3e8479a9e04db5c0616a","sup_9b6fc2bdf09bd98119a4"],"title":"finite event rather than abstract category","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:4","qac_refs":["91:2:3:1","91:2:3:2"],"status":"accepted"}},{"anchor_refs":["91:2:4"],"branch_refs":[],"candidate_id":"cand_e35fccd56818b4749f54","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000185","root_000186"],"scope":"focus_ayah","source_local_id":"91:2:4:follow-recitation-resonance","source_type":"word_analysis","support_ids":["sup_3e8479a9e04db5c0616a","sup_52f9f11552da0cd168a4"],"title":"following with recitation resonance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:4","qac_refs":["91:2:3:1","91:2:3:2"],"status":"accepted"}},{"anchor_refs":["91:2:4"],"branch_refs":[],"candidate_id":"cand_5482ef825b0722e48d18","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000185","root_000186"],"scope":"focus_ayah","source_local_id":"91:2:4:form-i-perfect-following","source_type":"word_analysis","support_ids":["sup_3e8479a9e04db5c0616a","sup_6914c28267c19425bd7d"],"title":"active Form I perfect following","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:4","qac_refs":["91:2:3:1","91:2:3:2"],"status":"accepted"}},{"anchor_refs":["91:2:4"],"branch_refs":[],"candidate_id":"cand_40fed62881382a35f741","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000185","root_000186"],"scope":"focus_ayah","source_local_id":"91:2:4:rare-cosmic-register","source_type":"word_analysis","support_ids":["sup_3e8479a9e04db5c0616a","sup_50d16a9703178f4ccb27"],"title":"marked form shifts register to a cosmic sign","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:4","qac_refs":["91:2:3:1","91:2:3:2"],"status":"accepted"}},{"anchor_refs":["91:2:4"],"branch_refs":[],"candidate_id":"cand_1bf74f170d1af4e3e844","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000185","root_000186"],"scope":"focus_ayah","source_local_id":"91:2:4:transitive-targeted-relation","source_type":"word_analysis","support_ids":["sup_3e8479a9e04db5c0616a","sup_e83746afd09b527c3c3a"],"title":"following takes a specific object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:4","qac_refs":["91:2:3:1","91:2:3:2"],"status":"accepted"}},{"anchor_refs":["91:2:4"],"branch_refs":[],"candidate_id":"cand_c2b0dcf00f0eeac23333","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000185","root_000186"],"scope":"focus_ayah","source_local_id":"91:2:4:two-participant-morphology","source_type":"word_analysis","support_ids":["sup_3e8479a9e04db5c0616a","sup_80e213bc6b0d8ccafc08"],"title":"moon agent and feminine object stay distinct","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:2:4","qac_refs":["91:2:3:1","91:2:3:2"],"status":"accepted"}},{"anchor_refs":["91:2:1"],"branch_refs":[],"candidate_id":"cand_1bdcd8ae2c9bd0a18bb8","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001255"],"scope":"focus_ayah","source_local_id":"91:2:1:3","source_type":"qac_morpheme","support_ids":["sup_bb12355586e45e8e0a9f"],"title":"QAC root occurrence: ق م ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:2:3"],"branch_refs":[],"candidate_id":"cand_1805014fcbca9272f0a5","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000185","root_000186"],"scope":"focus_ayah","source_local_id":"91:2:3:1","source_type":"qac_morpheme","support_ids":["sup_4159913e6732903ff4de"],"title":"QAC root occurrence: ت ل و","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:2","branch_refs":["root_000186/B001","root_001255/B001"],"candidate_id":"cand_4993df270cbab1e43424","commentary_obligation":"review","hft_ref":"hft_c9d7c20fab557d403cb4","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b01_ordered_celestial_succession","source_type":"hft","support_ids":["sup_8de64c0a6e362031ee2f"],"title":"b01_ordered_celestial_succession","trust":"legacy_unbound"},{"anchor_refs":["91:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:2","branch_refs":["root_000186/B003","root_001255/B001"],"candidate_id":"cand_0b61df74c25a9d3ffcb2","commentary_obligation":"review","hft_ref":"hft_bf1760af503da2adb933","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b02_dependent_afterlight","source_type":"hft","support_ids":["sup_3547654bc514801e17ef"],"title":"b02_dependent_afterlight","trust":"legacy_unbound"},{"anchor_refs":["91:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:2","branch_refs":["root_000186/B007","root_001255/B001"],"candidate_id":"cand_84f74fa55961258a7af7","commentary_obligation":"review","hft_ref":"hft_94663eebaba3a3fb5d85","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b03_antiphonal_response","source_type":"hft","support_ids":["sup_10160ceae33d8cf40e18"],"title":"b03_antiphonal_response","trust":"legacy_unbound"},{"anchor_refs":["91:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:2","branch_refs":["root_000186/B004","root_001255/B001"],"candidate_id":"cand_ca87aef88979eb081a84","commentary_obligation":"review","hft_ref":"hft_78f2d120f748bfbb2853","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b04_attached_claim","source_type":"hft","support_ids":["sup_1b217553d0fd07891f10"],"title":"b04_attached_claim","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَٱلْقَمَرِ إِذَا تَلَىٰهَا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:2:1:1","qac_word_ref":"91:2:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"91:2:1:2","qac_word_ref":"91:2:1","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"قَمَر","morph_features":"STEM|POS:N|LEM:qamar|ROOT:qmr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:2:1:3","qac_word_ref":"91:2:1","root_ar":"ق م ر","surface_ar":"قَمَرِ"},{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"91:2:2:1","qac_word_ref":"91:2:2","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","root_ar":"ت ل و","surface_ar":"تَلَىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:2:3:2","qac_word_ref":"91:2:3","root_ar":"","surface_ar":"هَا"}],"word_analysis_qac_refs":[["91:2:1:1"],["91:2:1:2","91:2:1:3"],["91:2:2:1"],["91:2:3:1","91:2:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["91:2:1","91:2:2","91:2:3","91:2:4"]},"focus_surface_evidence":{"arabic_uthmani":"وَٱلْقَمَرِ إِذَا تَلَىٰهَا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:2:1:1","qac_word_ref":"91:2:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"91:2:1:2","qac_word_ref":"91:2:1","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"قَمَر","morph_features":"STEM|POS:N|LEM:qamar|ROOT:qmr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:2:1:3","qac_word_ref":"91:2:1","root_ar":"ق م ر","surface_ar":"قَمَرِ"},{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"91:2:2:1","qac_word_ref":"91:2:2","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"تَلَىٰ","morph_features":"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:2:3:1","qac_word_ref":"91:2:3","root_ar":"ت ل و","surface_ar":"تَلَىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:2:3:2","qac_word_ref":"91:2:3","root_ar":"","surface_ar":"هَا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["91:2:1:1"],["91:2:1:2","91:2:1:3"],["91:2:2:1"],["91:2:3:1","91:2:3:2"]],"word_analysis_refs":["91:2:1","91:2:2","91:2:3","91:2:4"],"word_rows":[{"analysis_record_ref":"91:2:1","analytic_gloss_range_en":"oath-coordinating particle that renews the qasam chain before the moon; not merely ordinary coordination here","analytic_root_gloss_range_en":null,"qac_refs":["91:2:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"91:2:2","analytic_gloss_range_en":"the recognized moon as a definite genitive oath object that also supplies the following verb's subject","analytic_root_gloss_range_en":"broad lunar field including moon, moonlight, moon-white brightness, moonlit conditions, and unrelated derived branches; local syntax selects the concrete lunar body in relation to the sun","qac_refs":["91:2:1:2","91:2:1:3"],"root":{"arabic":"ق م ر","transliteration":"q-m-r"},"surface":{"arabic":"ٱلْقَمَرِ","transliteration":"al-qamari"}},{"analysis_record_ref":"91:2:3","analytic_gloss_range_en":"temporal-conditional particle meaning when/whenever in this oath frame, not a merely hypothetical if","analytic_root_gloss_range_en":null,"qac_refs":["91:2:2:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"إِذَا","transliteration":"idhā"}},{"analysis_record_ref":"91:2:4","analytic_gloss_range_en":"Form I perfect verb with 3ms subject and 3fs object suffix: he/it followed her/it; local sense is physical or sequential following with recitation resonance kept secondary","analytic_root_gloss_range_en":"broad root range includes following, reciting, remainder after what came before, and other distant branches; local grammar selects direct following of a prior feminine referent","qac_refs":["91:2:3:1","91:2:3:2"],"root":{"arabic":"ت ل و","transliteration":"t-l-w"},"surface":{"arabic":"تَلَىٰهَا","transliteration":"talāhā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["91:2"],"branch_refs":["root_000186/B001","root_001255/B001"],"candidate_id":"cand_4993df270cbab1e43424","evidence_scope":"focus_ayah","hft_ref":"hft_c9d7c20fab557d403cb4","item_id":"b01_ordered_celestial_succession","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b01_ordered_celestial_succession","support_id":"sup_8de64c0a6e362031ee2f"},{"anchor_refs":["91:2"],"branch_refs":["root_000186/B003","root_001255/B001"],"candidate_id":"cand_0b61df74c25a9d3ffcb2","evidence_scope":"focus_ayah","hft_ref":"hft_bf1760af503da2adb933","item_id":"b02_dependent_afterlight","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b02_dependent_afterlight","support_id":"sup_3547654bc514801e17ef"},{"anchor_refs":["91:2"],"branch_refs":["root_000186/B007","root_001255/B001"],"candidate_id":"cand_84f74fa55961258a7af7","evidence_scope":"focus_ayah","hft_ref":"hft_94663eebaba3a3fb5d85","item_id":"b03_antiphonal_response","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b03_antiphonal_response","support_id":"sup_10160ceae33d8cf40e18"},{"anchor_refs":["91:2"],"branch_refs":["root_000186/B004","root_001255/B001"],"candidate_id":"cand_ca87aef88979eb081a84","evidence_scope":"focus_ayah","hft_ref":"hft_78f2d120f748bfbb2853","item_id":"b04_attached_claim","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b04_attached_claim","support_id":"sup_1b217553d0fd07891f10"}],"diagnostics":[],"lane_counts":{"global":10,"macro":11,"micro":4},"packet_summary":{"ayah_count":15,"focus_ref":"91:2","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ت ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000186","furuq_root_norm":"ت ل و","furuq_source_root_norm":"ت ل و","is_dominant":true,"target_occurrences":39,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000185","furuq_root_norm":"ت ل ل","furuq_source_root_norm":"ت ل ل","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["91:1","91:2","91:3","91:4","91:5","91:6","91:7","91:8","91:9","91:10","91:11","91:12","91:13","91:14","91:15"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"91:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"91:2","lane":"micro","linguistic_source_ref":"91:2","surface_ref":"91:2","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"91:2","target_tokens":[["Ve",["91:2:1"]],["onu",["91:2:3"]],["izlediğinde",["91:2:2","91:2:3"]],["aya",["91:2:1"]]],"text":"Ve onu izlediğinde aya,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":15,"id":"s091-p01-001-015","label":"Whole surah","number":1,"refs":["91:1","91:2","91:3","91:4","91:5","91:6","91:7","91:8","91:9","91:10","91:11","91:12","91:13","91:14","91:15"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:1","source_type":"word_analysis","support_id":"sup_0676a5bc7de60e8c3e04","text":"{\"gloss_range\":\"oath-coordinating particle that renews the qasam chain before the moon; not merely ordinary coordination here\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) carries 91:2 forward inside the oath chain opened in 91:1, so the moon is not introduced as an independent new sentence or a loose list item. The particle both coordinates and renews qasam force: it governs the genitive moon phrase through the compressed oath construction, while the ayah boundary remains syntactically open rather than a full break. Its launch also repeats the opening pattern of 91:1: oath particle, definite noun, temporal particle, then verb. In recitation, the particle's liaison with the following definite noun makes that attachment audible as well as grammatical.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:4:boundary-shift","source_type":"word_analysis","support_id":"sup_23d4a8277376a7ed5366","text":"{\"blocking_evidence\":null,\"headline\":\"brightness becomes following event\",\"reader_payoff\":\"The reader notices a movement from the sun's manifested brightness in 91:1 to the moon's action of coming after it in 91:2.\",\"reason\":\"The final suffix points back to the previous ayah while the local verb supplies a new event, supporting the CRITICAL boundary rows about a shift from possession/brightness to action.\",\"representative_source_ids\":[\"QB-3efde23c\",\"QB-b051474a\",\"QB-eda74e96\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:2","source_type":"word_analysis","support_id":"sup_273a339522f40eb140ba","text":"{\"gloss_range\":\"the recognized moon as a definite genitive oath object that also supplies the following verb's subject\",\"prose\":\"{{ar:ٱلْقَمَرِ}} ({{tr:al-qamari}}) is the known moon, definite and genitive because the oath particle has made it the sworn object. The noun is not only named as a witness: it is also the recoverable masculine subject of {{ar:تَلَىٰهَا}} ({{tr:talāhā}}), so the sworn body becomes an actor in the temporal scene. Its root field supports lunar light, pale radiance, and moonlit effects, but the local form narrows that range to the concrete moon whose significance is relational: it follows the prior feminine solar referent from 91:1 as a secondary luminous witness rather than a self-standing light-source. The locally ordered pair also sits against a wider horizon where the sun-moon relation can be disrupted or made portentous (75:8-9; 54:1), without turning this oath scene into that collapse. Even the article's audible {{ar:ل}} ({{tr:l}}) differs from the assimilated article in {{ar:ٱلشَّمْسِ}} ({{tr:al-shamsi}}) in 91:1, so the paired luminaries are distinguished in sound before their relation is completed by the verb.\",\"root_display\":\"{{ar:ق م ر}} ({{tr:q-m-r}})\",\"root_gloss_range\":\"broad lunar field including moon, moonlight, moon-white brightness, moonlit conditions, and unrelated derived branches; local syntax selects the concrete lunar body in relation to the sun\",\"surface_display\":\"{{ar:ٱلْقَمَرِ}} ({{tr:al-qamari}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:4:ayah-closing-cadence","source_type":"word_analysis","support_id":"sup_2ca8939bcc34c0fb5e36","text":"{\"blocking_evidence\":null,\"headline\":\"final cadence binds adjacent oaths\",\"reader_payoff\":\"The reader notices that the long final suffix links backward to 91:1 and forward to 91:3 through sound as well as grammar.\",\"reason\":\"The surface ending shares the {{ar:ـاهَا}} ({{tr:-āhā}}) cadence with the adjacent oath clauses, and the object suffix also participates in the cross-ayah referential chain.\",\"representative_source_ids\":[\"QF-69882188\",\"QE-a3bf96d5\",\"QE-eba10735\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:4","source_type":"word_analysis","support_id":"sup_3e8479a9e04db5c0616a","text":"{\"gloss_range\":\"Form I perfect verb with 3ms subject and 3fs object suffix: he/it followed her/it; local sense is physical or sequential following with recitation resonance kept secondary\",\"prose\":\"{{ar:تَلَىٰهَا}} ({{tr:talāhā}}) closes the ayah by making the moon's oath value an action: it follows a prior feminine referent from 91:1. The Form I perfect presents that following as an accomplished, recurring relation inside the {{ar:إِذَا}} ({{tr:idhā}}) clause, and the active masculine verb keeps the moon as the agent while the attached feminine suffix keeps the object distinct. That suffix reaches back across the ayah boundary, with {{ar:ٱلشَّمْسِ}} ({{tr:al-shamsi}}) in 91:1 strongly licensed and {{ar:ضُحَىٰهَا}} ({{tr:duḥāhā}}) in 91:1 a lower-confidence possibility, so translation should not flatten the ambiguity too quickly. The root's recitation field remains a meaningful resonance because a lunar follower of solar brightness can be heard as re-articulating a prior light, but local grammar keeps physical or sequential following as the primary sense. Against a supplied Form I comparison in human speech (10:16), this use shifts the marked first-form action onto a cosmic body, so the sky-event becomes something ordered enough to be read as well as seen. The long {{ar:ـاهَا}} ({{tr:-āhā}}) ending answers 91:1 and prepares the matching closure of 91:3, so the final word binds grammar, sound, and the sun-moon relation at once.\",\"root_display\":\"{{ar:ت ل و}} ({{tr:t-l-w}})\",\"root_gloss_range\":\"broad root range includes following, reciting, remainder after what came before, and other distant branches; local grammar selects direct following of a prior feminine referent\",\"surface_display\":\"{{ar:تَلَىٰهَا}} ({{tr:talāhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"91:2:3:1","source_type":"qac_morpheme","support_id":"sup_4159913e6732903ff4de","text":"{\"lemma_ar\":\"تَلَىٰ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:talaY`|ROOT:tlw|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"91:2:3:1\",\"qac_word_ref\":\"91:2:3\",\"root_ar\":\"ت ل و\",\"surface_ar\":\"تَلَىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:2:oath-object-subject-role","source_type":"word_analysis","support_id":"sup_4683dc9566279ee63b0f","text":"{\"blocking_evidence\":null,\"headline\":\"witness becomes actor\",\"reader_payoff\":\"The reader notices that the moon carries two roles: genitive oath object first, then subject of the following verb.\",\"reason\":\"Attachment evidence licenses the moon as subject of {{ar:تَلَىٰهَا}} ({{tr:talāhā}}), while the same noun remains genitive under the oath particle.\",\"representative_source_ids\":[\"QG-ecb6ccfa\",\"QG-f85ea5cd\",\"QS-d1053ae3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:4:convergent-final-word","source_type":"word_analysis","support_id":"sup_4865ac60d8995706d141","text":"{\"blocking_evidence\":null,\"headline\":\"grammar sound and sense converge\",\"reader_payoff\":\"The reader notices that the final word is a compact knot of root sense, rare form, pronoun dependency, and rhyme.\",\"reason\":\"The synthesis rows are supported by already licensed pieces: Form I following, a bound feminine object, cross-ayah reference, and the repeated {{ar:ـاهَا}} ({{tr:-āhā}}) cadence.\",\"representative_source_ids\":[\"QY-3b7aa5f2\",\"QY-4b22a2c3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:4:rare-cosmic-register","source_type":"word_analysis","support_id":"sup_50d16a9703178f4ccb27","text":"{\"blocking_evidence\":null,\"headline\":\"marked form shifts register to a cosmic sign\",\"reader_payoff\":\"The reader notices that a root often associated with recitation is here placed in an observable sky-event, making the cosmic sequence legible as a sign.\",\"reason\":\"The contextual profile marks the exact Form I usage as low occurrence, and V4 preserves a recitation branch without making it the local primary branch.\",\"representative_source_ids\":[\"QI-2086ea48\",\"QI-af128d55\",\"QI-da7e2e0e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:4:follow-recitation-resonance","source_type":"word_analysis","support_id":"sup_52f9f11552da0cd168a4","text":"{\"blocking_evidence\":null,\"headline\":\"following with recitation resonance\",\"reader_payoff\":\"The reader notices that the moon's following can also sound like a secondary articulation of prior light, while the primary local sense remains sequential following.\",\"reason\":\"V4 distinguishes following-in-sequence and reciting branches; the local cosmic subject and direct object select following, but the root's Quranic recitation field can remain a secondary resonance rather than an equal lexical sense.\",\"representative_source_ids\":[\"QS-3de2097e\",\"QS-4f3c725a\",\"MS-d9365ff7\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:2:structured-oath-series","source_type":"word_analysis","support_id":"sup_62547779415f21f5ed4b","text":"{\"blocking_evidence\":null,\"headline\":\"entity joined to relational condition\",\"reader_payoff\":\"The reader notices that the oath is not on the moon in isolation but on the moon as it enters a timed relational action.\",\"reason\":\"The clause evidence makes {{ar:إِذَا}} ({{tr:idhā}}) the temporal setting for {{ar:تَلَىٰهَا}} ({{tr:talāhā}}), so the noun is paired with a following event inside the oath series.\",\"representative_source_ids\":[\"QT-6f8bc2cd\",\"QE-eeedac47\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:4:form-i-perfect-following","source_type":"word_analysis","support_id":"sup_6914c28267c19425bd7d","text":"{\"blocking_evidence\":null,\"headline\":\"active Form I perfect following\",\"reader_payoff\":\"The reader notices that the word presents the moon's following as an accomplished recurring action, with physical sequence at the surface.\",\"reason\":\"QAC and verb-instance evidence identify the local word as Form I perfect, active, third masculine singular with a clitic object, while V4's first branch supports following in sequence.\",\"representative_source_ids\":[\"QG-0a78e306\",\"QF-4d074fc9\",\"MF-a83c1711\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:3:opening-parallel","source_type":"word_analysis","support_id":"sup_73b029fe9660c90a2e75","text":"{\"blocking_evidence\":null,\"headline\":\"parallel temporal pattern with 91:1\",\"reader_payoff\":\"The reader notices that the second oath repeats the temporalized structure of 91:1 while shifting from brightness possession to following process.\",\"reason\":\"The CRITICAL row supplies the concrete 91:1 comparison, and the local 91:2 clause has the same particle-plus-verb architecture.\",\"representative_source_ids\":[\"MT-349643ce\",\"QB-2c70c496\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:4:two-participant-morphology","source_type":"word_analysis","support_id":"sup_80e213bc6b0d8ccafc08","text":"{\"blocking_evidence\":null,\"headline\":\"moon agent and feminine object stay distinct\",\"reader_payoff\":\"The reader notices that the single word stores two participants: masculine lunar action and feminine object reference.\",\"reason\":\"The verb is third masculine singular and attachment evidence licenses the moon as subject, while the suffix is a third feminine singular direct object.\",\"representative_source_ids\":[\"QG-5dd97e76\",\"QG-7d2e65b6\",\"QF-84f8e461\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:2:sun-moon-pair","source_type":"word_analysis","support_id":"sup_905f40a9071b403b310c","text":"{\"blocking_evidence\":null,\"headline\":\"sun and moon made a grammatical pair\",\"reader_payoff\":\"The reader notices that the moon completes a paired luminary movement with the sun from 91:1 through sequence, grammar, and the final pronoun.\",\"reason\":\"The final object suffix in 91:2 reaches back to a feminine referent in 91:1, and the contextual profile shows {{ar:ق م ر}} ({{tr:q-m-r}}) frequently collocated with {{ar:ش م س}} ({{tr:sh-m-s}}), supporting the local paired reading.\",\"representative_source_ids\":[\"QI-cd0a18df\",\"QE-335f3252\",\"QY-0be67340\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:4:finite-event-not-category","source_type":"word_analysis","support_id":"sup_9b6fc2bdf09bd98119a4","text":"{\"blocking_evidence\":null,\"headline\":\"finite event rather than abstract category\",\"reader_payoff\":\"The reader notices that the oath points to an enacted following event, not an abstract noun or a class of followers.\",\"reason\":\"The local form is a finite perfect verb inside the temporal clause, not a participle or verbal noun.\",\"representative_source_ids\":[\"QF-541dc9f8\",\"QS-b4856766\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:2:definite-genitive-witness","source_type":"word_analysis","support_id":"sup_9c63015da919943d52b9","text":"{\"blocking_evidence\":null,\"headline\":\"recognized moon as sworn witness\",\"reader_payoff\":\"The reader notices that the familiar singular moon is formally installed as sworn evidence, not mentioned as a generic bright object.\",\"reason\":\"QAC and noun-instance evidence identify {{ar:ٱلْقَمَرِ}} ({{tr:al-qamari}}) as a definite concrete genitive noun governed by the oath particle.\",\"representative_source_ids\":[\"QG-038f08b4\",\"QG-38f369eb\",\"QI-bfca6885\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:2:lunar-light-narrowing","source_type":"word_analysis","support_id":"sup_9f5c3b395c72b5cbc426","text":"{\"blocking_evidence\":null,\"headline\":\"lunar radiance narrowed to the concrete moon\",\"reader_payoff\":\"The reader notices lunar brightness as part of the word's pressure, while the local oath keeps the referent the concrete moon that follows the sun.\",\"reason\":\"V4 supports moon, moonlight, and whiteness branches, and contextual profiles keep {{ar:ق م ر}} ({{tr:q-m-r}}) as nature-creation usage; the local noun is concrete, so derivative effects such as exposure, dazzlement, or technical reflected-light claims must remain coloring rather than replacement.\",\"representative_source_ids\":[\"QS-23d50d82\",\"QS-a78a6719\",\"MS-5d629de5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:3:temporal-restrictor","source_type":"word_analysis","support_id":"sup_a069d540bc06c3774ebb","text":"{\"blocking_evidence\":null,\"headline\":\"oath narrowed to a recurring moment\",\"reader_payoff\":\"The reader notices that the oath is on the moon at the moment of following, not on the moon as an isolated object.\",\"reason\":\"QAC marks {{ar:إِذَا}} ({{tr:idhā}}) as a temporal adverb, and attachment evidence makes it the adverbial setting for {{ar:تَلَىٰهَا}} ({{tr:talāhā}}).\",\"representative_source_ids\":[\"QG-31458625\",\"QG-439417db\",\"QS-d598ac95\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:1:audible-liaison","source_type":"word_analysis","support_id":"sup_ad307fb0c208814b76e4","text":"{\"blocking_evidence\":null,\"headline\":\"bound sound makes attachment audible\",\"reader_payoff\":\"The reader notices that the oath bond is heard at the word boundary, not only inferred from syntax.\",\"reason\":\"The particle is immediately followed by the definite moon noun in the same oath pattern as 91:1, so the liaison and parallel-surface observations are locally coherent.\",\"representative_source_ids\":[\"QP-6bb71339\",\"MT-a2849b2b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:2:article-sound-contrast","source_type":"word_analysis","support_id":"sup_b237d30d5aeec8058f60","text":"{\"blocking_evidence\":null,\"headline\":\"audible article distinguishes the moon\",\"reader_payoff\":\"The reader notices that the moon's definite article stays audible, giving the paired luminaries different recited contours.\",\"reason\":\"The surface form begins with a moon-letter environment where the article's {{ar:ل}} ({{tr:l}}) remains pronounced, unlike the assimilating article before {{ar:ٱلشَّمْسِ}} ({{tr:al-shamsi}}) in 91:1.\",\"representative_source_ids\":[\"QF-70cf04e0\",\"QP-72bee593\",\"QP-060bbb72\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"91:2:1:3","source_type":"qac_morpheme","support_id":"sup_bb12355586e45e8e0a9f","text":"{\"lemma_ar\":\"قَمَر\",\"morph_features\":\"STEM|POS:N|LEM:qamar|ROOT:qmr|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"91:2:1:3\",\"qac_word_ref\":\"91:2:1\",\"root_ar\":\"ق م ر\",\"surface_ar\":\"قَمَرِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:3:hamza-onset","source_type":"word_analysis","support_id":"sup_bd95c5d354a632e8a37f","text":"{\"blocking_evidence\":null,\"headline\":\"pronounced onset marks the hinge\",\"reader_payoff\":\"The reader notices that the turn from object to condition is articulated in the sound of the particle.\",\"reason\":\"The surface form begins with pronounced hamza, so the sound observation aligns with the word's syntactic role as temporal pivot.\",\"representative_source_ids\":[\"QF-79c150e9\",\"QP-d4ee40e8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:3","source_type":"word_analysis","support_id":"sup_c32414b67baa02a750e1","text":"{\"gloss_range\":\"temporal-conditional particle meaning when/whenever in this oath frame, not a merely hypothetical if\",\"prose\":\"{{ar:إِذَا}} ({{tr:idhā}}) is the hinge that turns the moon from a static sworn object into a timed scene: the oath concerns the moon when it follows the prior feminine referent. With the following perfect verb, the particle gives the action the feel of a completed yet recurring celestial moment, closer to when or whenever than to an uncertain if. Its independent written and pronounced onset creates a small boundary between the noun and the verb, and the same construction mirrors the opening temporal pattern of 91:1.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِذَا}} ({{tr:idhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:3:structural-hinge","source_type":"word_analysis","support_id":"sup_c77194c2c1b76fba487f","text":"{\"blocking_evidence\":null,\"headline\":\"visible hinge from noun to event\",\"reader_payoff\":\"The reader notices the exact surface point where the oath object becomes a verbal scene.\",\"reason\":\"The particle stands as its own word between the moon noun and the following verb, and local syntax makes it the adverbial link into the predicate.\",\"representative_source_ids\":[\"QF-7474f7cc\",\"QT-7629df10\",\"QT-ccdbf0bd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:4:cross-ayah-object-suffix","source_type":"word_analysis","support_id":"sup_c9820d8dca4e1a64f383","text":"{\"blocking_evidence\":null,\"headline\":\"feminine object points back to 91:1\",\"reader_payoff\":\"The reader notices that the final suffix makes 91:2 depend on 91:1, while leaving a controlled choice between the sun and its brightness.\",\"reason\":\"Attachment evidence treats the suffix as a direct object and warns against resolving it by default; {{ar:ٱلشَّمْسِ}} ({{tr:al-shamsi}}) in 91:1 is strongly licensed, while {{ar:ضُحَىٰهَا}} ({{tr:duḥāhā}}) in 91:1 remains a lower-confidence candidate.\",\"representative_source_ids\":[\"QG-3be32565\",\"QG-46191a2a\",\"MG-92f3f91f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:1:oath-governance","source_type":"word_analysis","support_id":"sup_cfa94a2060bd4a2eb3ae","text":"{\"blocking_evidence\":null,\"headline\":\"qasam force governs the moon phrase\",\"reader_payoff\":\"The reader notices that one small particle is doing the oath work that turns the moon into sworn evidence.\",\"reason\":\"QAC labels {{ar:وَ}} ({{tr:wa}}) as conjunction and oath particle, and attachment evidence makes {{ar:ٱلْقَمَرِ}} ({{tr:al-qamari}}) its genitive oath complement with the oath performative left implicit.\",\"representative_source_ids\":[\"QG-303a9125\",\"QF-dc5d9ba1\",\"QI-658bff72\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:2:intertext-pair-horizon","source_type":"word_analysis","support_id":"sup_dce70d655b939e368723","text":"{\"blocking_evidence\":null,\"headline\":\"stable pair against disruption horizon\",\"reader_payoff\":\"The reader notices that the locally ordered sun-moon succession stands against Quranic scenes where the pair can be eclipsed or gathered (75:8-9) and where the moon itself becomes a sign (54:1).\",\"reason\":\"The cited inter-ayah horizon is useful as contrast, but it does not control the local parse; 91:2 remains an oath on ordered following rather than an eschatological collapse scene.\",\"representative_source_ids\":[\"QI-738e5c0e\",\"MI-f2d718e5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:4:transitive-targeted-relation","source_type":"word_analysis","support_id":"sup_e83746afd09b527c3c3a","text":"{\"blocking_evidence\":null,\"headline\":\"following takes a specific object\",\"reader_payoff\":\"The reader notices that the verb does not merely say the moon comes after; it follows a marked prior object.\",\"reason\":\"Local attachment makes the suffix the direct object, and contextual valency confirms clitic objects as part of this exact-root form's usage profile.\",\"representative_source_ids\":[\"QG-97c00654\",\"QF-2b3de4ed\",\"QT-ec2d188f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:2:1:chain-continuation","source_type":"word_analysis","support_id":"sup_f5069b6ed8ec2fd1db15","text":"{\"blocking_evidence\":null,\"headline\":\"ayah boundary remains in the oath chain\",\"reader_payoff\":\"The reader notices that 91:2 starts by carrying forward the oath frame of 91:1 rather than resetting the discourse.\",\"reason\":\"The initial particle is locally marked as oath force and coordination, so the CRITICAL rows about cross-ayah continuation are supported by the surface launch of 91:2.\",\"representative_source_ids\":[\"QG-0c622f97\",\"MG-fbe6aa31\",\"QT-6de693b5\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْقَمَرِ إِذَا تَلَىٰهَا","ayah_ref":"91:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000186/B001","root_001255/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001255","role":"The celestial body together with its illumination supplies the visible entity whose position is tracked.","root":"ق م ر","source_ref":"91:2","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000186","role":"Physical, ranked, or sequential following supplies the ordered relation to the unresolved feminine referent.","root":"ت ل و","source_ref":"91:2","source_word_indices":["3"]}],"changed_reading":{"after":"An oath by the moon specifically in the condition of taking an ordered place after a feminine antecedent.","before":"A static oath by the moon."},"confidence":"strong","focus_anchor":"The noun at word 1 supplies the lunar entity, while the verb at word 3 predicates its following of a feminine pronominal object.","mechanism":"The moon and its light are placed in bodily, ranked, or temporal sequence after an antecedent that remains unresolved within the focus ayah alone.","model_id":"b01_ordered_celestial_succession"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b01_ordered_celestial_succession","source_type":"hft","support_id":"sup_8de64c0a6e362031ee2f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْقَمَرِ إِذَا تَلَىٰهَا","ayah_ref":"91:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000186/B003","root_001255/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001255","role":"The moon's visible illumination provides the material that can persist as an afterlight.","root":"ق م ر","source_ref":"91:2","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000186","role":"A remainder coming after an earlier portion turns succession into residual continuation rather than mere adjacency.","root":"ت ل و","source_ref":"91:2","source_word_indices":["3"]}],"changed_reading":{"after":"The moon can be heard as an afterlight or remainder that carries forward what preceded it, making dependence coexist with sequence.","before":"A coequal second luminary simply comes next."},"confidence":"medium","focus_anchor":"The lunar-light scope of word 1 combines with the remainder sense available to the following verb at word 3.","mechanism":"What follows can be the residue of what came before, so the moon is not merely a second coequal object but a dependent afterlight carrying a prior presence forward.","model_id":"b02_dependent_afterlight"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b02_dependent_afterlight","source_type":"hft","support_id":"sup_3547654bc514801e17ef","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْقَمَرِ إِذَا تَلَىٰهَا","ayah_ref":"91:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000186/B007","root_001255/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001255","role":"The sky-visible moon and its light function as the second signal in the proposed visual relay.","root":"ق م ر","source_ref":"91:2","source_word_indices":["1"]},{"branch_id":"B007","mapped_root_id":"root_000186","role":"A voice answering a preceding voice supplies the responsive, antiphonal structure assigned to lunar following.","root":"ت ل و","source_ref":"91:2","source_word_indices":["3"]}],"changed_reading":{"after":"The moon answers a prior presence like a second voice, preserving responsive relay alongside physical succession.","before":"The moon passively trails another body."},"confidence":"exploratory","focus_anchor":"The visible moon at word 1 is coupled to the responding-voice branch of the verb at word 3.","mechanism":"Following can be antiphonal: a second voice answers a first. Crossed into the visual domain, the lunar presence becomes a response to an unresolved prior signal rather than a silent trailer.","model_id":"b03_antiphonal_response"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b03_antiphonal_response","source_type":"hft","support_id":"sup_10160ceae33d8cf40e18","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْقَمَرِ إِذَا تَلَىٰهَا","ayah_ref":"91:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000186/B004","root_001255/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001255","role":"The recognizable lunar bearer gives the proposed attached claim a recurring visible locus.","root":"ق م ر","source_ref":"91:2","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_000186","role":"A due or liability that follows its possessor supplies the non-spatial bond between follower and antecedent.","root":"ت ل و","source_ref":"91:2","source_word_indices":["3"]}],"changed_reading":{"after":"Following can also be an attached due or turn that remains bound to the antecedent.","before":"Following means only being spatially or temporally behind."},"confidence":"exploratory","focus_anchor":"The verb at word 3 permits a right or liability that remains attached to its holder, while word 1 gives that attachment a recurrent celestial bearer.","mechanism":"Following may describe an encumbrance or due that accompanies its source. The moon's relation to the feminine object can therefore be tested as an attached turn or claim, not only a location behind it.","model_id":"b04_attached_claim"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b04_attached_claim","source_type":"hft","support_id":"sup_1b217553d0fd07891f10","trust":"legacy_unbound"}]}
</lane_packet_json>
