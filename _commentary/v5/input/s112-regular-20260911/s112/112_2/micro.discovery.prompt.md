# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **112:2**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s112-regular-20260911/s112/112_2/micro.discovery.json` and modify nothing
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
  "ayah_ref": "112:2",
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
{"analysis_context":{"analysis_id":"s112-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"112:2","host_surah":112,"lane_context_refs":[],"ordered_context_refs":["112:0","112:1","112:3","112:4","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, tapınma eylemi ile bundan türeyen tapınılan veya tapınılır kılınan varlık anlamlarını kapsar; şaşkınlık, yoğun üzüntü ve salt özel ad kullanımları bu sınırın dışındadır.","branch_kind":"mixed_non_bare","branch_ref":"root_000047/B001","candidate_links":[{"candidate_id":"cand_a42921341111986525d0","lane":"micro"},{"candidate_id":"cand_53a3f384ada79dfbceb0","lane":"micro"},{"candidate_id":"cand_d5725b0c659bce7656db","lane":"micro"},{"candidate_id":"cand_c06b38ac32ecb0390a84","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|NOM","morpheme_role":"STEM","pos":"PN","qac_ref":"112:2:1:1","qac_word_ref":"112:2:1","surface_ar":"ٱللَّهُ"}],"gloss":"tapınma ve tapınılan varlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel eylem, bir varlığa tapınmak ve kişinin kendini bu tapınmaya vermesidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylemden türeyen varlık anlamı, kendisine tapınılan varlığı veya tapınma konusu sayılan nesneyi gösterir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen kullanım, bir varlığı başkalarınca tapınılır duruma getirme veya öyle sunma işlemini bildirir."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Güneşe kimi topluluklarca tapınılması nedeniyle ona tapınılan varlık anlamındaki bir ad verilmesi, varlık anlamının tarihsel bir örneğidir."}}],"root_ar":"ء ل ه","root_id":"root_000047","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eylem çekirdeğiyle ondan türeyen tapınılan varlık anlamının birlikte temsil edilmesi gereken genel açıklamalarda kullanılır.","boundary_detail":"Dal, tapınma eylemi ile bundan türeyen tapınılan veya tapınılır kılınan varlık anlamlarını kapsar; şaşkınlık, yoğun üzüntü ve salt özel ad kullanımları bu sınırın dışındadır.","branch_image_ar":"التعبد والمعبود","concept_gloss":"tapınma ve tapınılan varlık","contextual_glosses":[{"applicability":"Bir kişinin tapınma eylemini veya kendini tapınmaya vermesini bildiren eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylem olarak tapınma çekirdeğini eksiksiz korur."},"facet_ids":["F001"],"text":"tapınmak","usage_role":"general"},{"applicability":"Bir topluluğun kendisine tapındığı varlık veya nesneden söz edilen ad bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tapınmanın yöneldiği varlık veya nesne anlamını korur."},"facet_ids":["F002"],"text":"tapınılan varlık","usage_role":"contextual"},{"applicability":"Bir varlığın başkalarına tapınma konusu olarak benimsetilmesini anlatan ettirgen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir varlığı tapınma konusu durumuna getirme işlemini korur."},"facet_ids":["F003"],"text":"tapınılır kılmak","usage_role":"explanatory"}],"definition":"Bir varlığa tapınma eylemini ve kişinin kendini tapınmaya vermesini anlatır. Türemiş kullanımlarda bir varlığı tapınılır kılmayı, tapınılan varlığı ve tapınma konusu sayılan varlıkları da adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel eylem, bir varlığa tapınmak ve kişinin kendini bu tapınmaya vermesidir."},{"facet_id":"F002","role":"extension","statement":"Eylemden türeyen varlık anlamı, kendisine tapınılan varlığı veya tapınma konusu sayılan nesneyi gösterir."},{"facet_id":"F003","role":"specialization","statement":"Ettirgen kullanım, bir varlığı başkalarınca tapınılır duruma getirme veya öyle sunma işlemini bildirir."},{"facet_id":"F004","role":"example","statement":"Güneşe kimi topluluklarca tapınılması nedeniyle ona tapınılan varlık anlamındaki bir ad verilmesi, varlık anlamının tarihsel bir örneğidir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Yalnızca belirli bir varlık türünü adlandırdığı için bütün dalın karşılığı sanılabilir.","fit":"narrowing","loses":"Tapınma eylemini, kişinin tapınmaya yönelmesini ve tapınılır kılma işlemini karşılamaz.","preserves":"Tapınılan varlık anlamını kısa ve doğal biçimde korur."},"text":"tanrı"}],"identity_rationale":"Kaynak ifadesi tapınma eylemini, kişinin kendini tapınmaya vermesini, bir varlığı tapınılır kılmayı ve tapınılan varlığı aynı anlam örgüsü içinde açıkça birleştirir. Geçici dal çerçevesi bu çekirdeği ve ondan türeyen varlık adlarını doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tapınmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kendini tapınmaya vermek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"tapınılır kılmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"tapınılan varlık, tanrı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"tapınılan varlık"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"tanrılar, tapınılan nesneler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"tapınma"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kimi toplulukların tapındığı için bu adla anılan güneş"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"senin tapınman"}],"lexicalization_note":"Tanım, yalın eylem çekirdeğini türemiş eylem ve varlık adlarından ayırır; türemiş biçimlerin kapsamı yalın eylemin tamamına aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Tapınma eylemi, korkuya bağlı özel tapınma yaşayışı ve aynı kökün özel ad dalı sınırı keskinleştirdi; peygamberlik, büyücülük, belirli tapınma nesneleri, sahiplik ve tarihsel hizmet grubu adayları ise yalnızca aynı dinsel alana veya tekil örneklere temas ettiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal eylem ve yaklaşma yönünde yoğunlaşırken bu dal aynı çekirdekten tapınılan varlık ile ettirgen kılma anlamlarını da türetir; bu yüzden yalnızca eylem bağlamında yakınlaşırlar.","focus_only":"Tapınılan varlığı ve bir varlığı tapınılır kılma işlemini de adlandırır.","gloss":"tapınma ve yaklaşarak yönelme","neighbor_only":"Tapınmayla birlikte yaklaşma ve kendini bu işe verme yönünü öne çıkarır.","neighbor_ref":"root_001498/B001","relation_type":"near_synonym","shared_zone":"İki dal da tapınma eylemini ve kişinin bu eyleme yönelmesini kapsar."},{"boundary_match":"partial","distinction":"Bu dal genel tapınma çekirdeğini ve ondan türeyen varlık anlamlarını kapsar; komşu dal ise korku, inziva ve olağanın üstündeki uygulamalarla sınırlı özel bir yaşayışı anlatır.","focus_only":"Tapınmayı korku, inziva veya aşırı uygulama koşuluna bağlamaz ve tapınılan varlığı da adlandırabilir.","gloss":"korkuyla yoğunlaşan özel tapınma yaşayışı","neighbor_only":"Korkudan doğan, inziva veya ek yüklenme biçimindeki özel bir tapınma yaşayışını bildirir.","neighbor_ref":"root_000604/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da kişinin kendini tapınmaya vermesi bulunur."},{"boundary_match":"partial","distinction":"Bu dal genel anlam örgüsünü verir; komşu dal ise o örgüden türemiş özel adı ve adın belirli söz kalıplarındaki kullanımını ayrı bir biçim alanı olarak sınırlar.","focus_only":"Genel tapınma eylemini, tapınılan varlığı ve tapınılır kılmayı kapsar.","gloss":"Yaratıcıya özgü ad ve kullanım kalıpları","neighbor_only":"Yaratıcıya özgü adı ve bu adla kurulan seslenme, dilek ve ant kalıplarını kapsar.","neighbor_ref":"root_000047/B002","relation_type":"near_neighbor","shared_zone":"Özel ad, tapınılan yüce varlık düşüncesi üzerinden bu dalın varlık anlamıyla bağlantılıdır."}],"source_phrase_ar":"أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)","source_summary":"Kaynakların ortak çizgisi, tapınmayı anlamın temeli sayar; kişinin tapınmaya yönelmesini, tapınılan varlığı ve tapınılır kılma işlemini bu temelden türetir. Tapınma konusu sayılan yontular ve güneş örneği, varlık anlamının belirli uygulamalarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه أله وتأله بمعنى عبد وتنسك، والتأليه بمعنى التعبيد، والإله والآلهة والإلاهة لما جعل معبودا.","what_is_not_ar":"لا يدخل فيه أله بمعنى تحير، ولا ألهت على فلان بمعنى اشتد جزعي عليه، ولا أسماء المواضع أو الحية أو الهلال إلا من جهة التسمية لا معنى العبادة."},"support_links":["sup_0bcf15b6b317decc09cb","sup_4ea991c1511a7c7096c3","sup_53737a18d5bd4e8a4646","sup_c4b06d7e7f5b24bb607f"]},{"boundary":"Dal, özel ad ile bu ada bağlı seslenme, dilek, şaşma ve ant biçimleriyle sınırlıdır; herhangi bir tapınılan varlığı gösteren genel ad anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000047/B002","candidate_links":[{"candidate_id":"cand_a50f256eef039a196575","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|NOM","morpheme_role":"STEM","pos":"PN","qac_ref":"112:2:1:1","qac_word_ref":"112:2:1","surface_ar":"ٱللَّهُ"}],"gloss":"Yaratıcıya özgü ad ile seslenme ve ant biçimleri","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dalın merkezinde, Yaratıcıyı başkalarından ayırarak gösteren ve yalnız ona özgü sayılan özel ad bulunur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Özel adın, tapınılan varlığı bildiren genel addan ses düşmesi ve belirleyici unsur eklenmesiyle oluştuğu açıklanır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özel ad, sözün başında ant değeri taşıyarak ardından gelen yapmama bildirimini güçlendirebilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Özel adın doğrudan ya da seslenme öğesi yerine geçen bir sonla kullanılması, yakarma ve dilek bildiren seslenme biçimleri kurar."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Ses veya parçaların düşürüldüğü kısalmış biçimler, şaşma ve ant anlatan kalıplarda kullanılır."}}],"root_ar":"ء ل ه","root_id":"root_000047","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özel adın kendisiyle ona bağlı seslenme, dilek ve ant kullanımlarının birlikte açıklanması gereken dal düzeyinde kullanılır.","boundary_detail":"Dal, özel ad ile bu ada bağlı seslenme, dilek, şaşma ve ant biçimleriyle sınırlıdır; herhangi bir tapınılan varlığı gösteren genel ad anlamına genişletilmez.","branch_image_ar":"اسم الله في القسم والنداء","concept_gloss":"Yaratıcıya özgü ad ile seslenme ve ant biçimleri","contextual_glosses":[{"applicability":"Söz konusu adın yalnız Yaratıcıyı gösteren yalın ad olarak ele alındığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adın Yaratıcıya özgü olmasını ve ayırt edici ad işlevini korur."},"facet_ids":["F001"],"text":"Yaratıcı'nın özel adı","usage_role":"general"},{"applicability":"Yakarış veya dilek sırasında Yaratıcıya doğrudan seslenilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaratıcıya yöneltilen doğrudan seslenme işlevini doğal biçimde korur."},"facet_ids":["F004"],"text":"ey Tanrı","usage_role":"contextual"},{"applicability":"Özel adın bir bildirimin doğruluğunu pekiştiren ant değeri taşıdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaratıcıya dayanarak ant verme işlevini açık biçimde korur."},"facet_ids":["F003"],"text":"Tanrı adına ant olsun","usage_role":"contextual"},{"applicability":"Özel adın ses veya parçaları düşürülmüş tarihsel kalıplarının işlevini açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kısaltılma biçimini ve şaşma ya da ant işlevini birlikte korur."},"facet_ids":["F005"],"text":"kısaltılmış şaşma veya ant sözü","usage_role":"explanatory"}],"definition":"Yaratıcıya özgü adın kendisini ve bu adla kurulan seslenme, dilek, şaşma ve ant biçimlerini kapsar. Bu biçimler doğrudan seslenme, adın ant değeriyle kullanılması veya ses ve parçaların düşürülmesiyle kısaltılma yollarını gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dalın merkezinde, Yaratıcıyı başkalarından ayırarak gösteren ve yalnız ona özgü sayılan özel ad bulunur."},{"facet_id":"F002","role":"source_variant","statement":"Özel adın, tapınılan varlığı bildiren genel addan ses düşmesi ve belirleyici unsur eklenmesiyle oluştuğu açıklanır."},{"facet_id":"F003","role":"associated_use","statement":"Özel ad, sözün başında ant değeri taşıyarak ardından gelen yapmama bildirimini güçlendirebilir."},{"facet_id":"F004","role":"associated_use","statement":"Özel adın doğrudan ya da seslenme öğesi yerine geçen bir sonla kullanılması, yakarma ve dilek bildiren seslenme biçimleri kurar."},{"facet_id":"F005","role":"source_variant","statement":"Ses veya parçaların düşürüldüğü kısalmış biçimler, şaşma ve ant anlatan kalıplarda kullanılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Genel tür adı olarak başka tapınılan varlıklar için de kullanılabildiğinden özel adla karışır.","fit":"narrowing","loses":"Adın tek bir varlığa özgü özel ad oluşunu ve seslenme ile ant biçimlerini karşılamaz.","preserves":"Yüce bir tapınılan varlığa gönderimde bulunma yönünü korur."},"text":"tanrı"}],"identity_rationale":"Kaynak ifadesi Yaratıcıya özgü adın kendisini, genel tapınılan-varlık adından türetiliş açıklamasını ve bu özel adla kurulan seslenme ile ant biçimlerini birlikte verir. Geçici çerçeve kullanılabilir, ancak dal yalnızca seslenme ve ant kalıpları değildir; özel adın yalın kullanımı da çekirdekte tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"Yaratıcıya özgü ad"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"Tanrı adına ant olsun, bunu yapmadım"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ey Tanrı; yakarma seslenişi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ey Tanrı; doğrudan seslenme"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"Tanrı adına sen veya baban; şaşma ya da ant kalıbı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları"}],"lexicalization_note":"Yalın özel ad, doğrudan seslenme biçimleri ve ant ya da şaşma kalıpları ayrı tutulur; kalıplara özgü işlevler özel adın her kullanımına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Genel tapınma dalı, yaşam üzerine ant, genel seslenme, kısaltılmış kişi seslenmesi ve yakarışa karşılık sözü gerçek sınır karşılaştırmaları sağladı; baba hitapları, genel dışlama yapıları, başka ant sözleri ve sesçe eşlik eden kalıplar daha zayıf ya da yalnızca biçimsel temas gösterdiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli bir özel adın biçim ve kullanım alanıdır; komşu dal ise özel adla sınırlanmayan genel tapınma eylemini ve tapınılan varlık anlamını verir.","focus_only":"Yaratıcıya özgü adı ve bu adla kurulan seslenme, dilek, şaşma ve ant biçimlerini kapsar.","gloss":"tapınma ve tapınılan varlık","neighbor_only":"Genel tapınma eylemini, tapınılan varlığı ve bir varlığı tapınılır kılma işlemini kapsar.","neighbor_ref":"root_000047/B001","relation_type":"near_neighbor","shared_zone":"Özel ad, tapınılan yüce varlığı göstermesi bakımından genel varlık anlamına dayanır."},{"boundary_match":"partial","distinction":"Ortak işlev ant vermedir, fakat bu dalın dayanağı Yaratıcıya özgü addır; komşu dal yaşam süresini bildiren sözleri kullanır ve ayrıca ısrarlı istemeye uzanabilir.","focus_only":"Ant işlevini Yaratıcıya özgü adın yalın veya kısalmış biçimleriyle kurar.","gloss":"ömür üzerine ant ve ısrarlı isteme","neighbor_only":"Ant veya ısrarlı isteme işlevini yaşam süresini bildiren sözlerle kurar.","neighbor_ref":"root_001044/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir sözü güçlendiren ant işlevli kalıplar içerir."},{"boundary_match":"field_only","distinction":"Bu dal belirli bir muhatabın özel adı çevresinde oluşur; komşu dal ise muhatabın kimliğinden bağımsız genel seslenme araçlarını ve uzaklık ayrımını konu edinir.","focus_only":"Belirli bir özel adı ve o adın yakarma ile ant kullanımlarını içerir.","gloss":"genel seslenme öğeleri","neighbor_only":"Yakın veya uzaktaki muhataba yöneltilen genel seslenme öğelerini bildirir.","neighbor_ref":"root_000074/B008","relation_type":"same_field","shared_zone":"Her iki dal da doğrudan seslenme sırasında kullanılan biçimlerle ilgilidir."},{"boundary_match":"field_only","distinction":"Bu dalın kısalmaları belirli özel adın dinsel seslenme ve ant işlevlerine bağlıdır; komşu dalın kısalmaları ise belirsiz bir kişiye seslenmenin dilbilgisel biçimleridir.","focus_only":"Yaratıcıya özgü adı ve ona bağlı seslenme ile ant biçimlerini kapsar.","gloss":"kişiye yönelik kısaltılmış seslenme","neighbor_only":"Belirsiz bir kişiye yönelen kısaltılmış seslenme biçimlerini kapsar.","neighbor_ref":"root_001178/B003","relation_type":"same_field","shared_zone":"Her iki dalda da seslenme sırasında biçimsel kısalma görülebilir."},{"boundary_match":"thematic_only","distinction":"Bu dal bir muhataba seslenir; komşu dal ise söylenmiş yakarışa kabul dileği veya onayla karşılık verir. Aynı sahnede bulunsalar da anlam çekirdekleri örtüşmez.","focus_only":"Yakarışın yöneltildiği Yaratıcıyı özel adıyla çağırır.","gloss":"yakarışın kabulünü isteyen karşılık","neighbor_only":"Yakarışın kabul edilmesini isteyen veya söyleneni onaylayan karşılık sözünü bildirir.","neighbor_ref":"root_000054/B003","relation_type":"thematic","shared_zone":"İki dal da yakarış ortamında kullanılan kısa söz biçimlerine katılır."}],"source_phrase_ar":"فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)","source_summary":"Kaynaklar özel adı Yaratıcıya özgü bir ad olarak tanımlar ve onu tapınılan varlığı gösteren genel adla köken bakımından ilişkilendirir. Aynı adın doğrudan seslenmede, yakarmada, ant bildiriminde ve parçaları düşürülmüş kalıplarda kullanıldığı birlikte gösterilir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اسم الله والقول في أصله من إله، وصيغ الاستعمال مثل الله ما فعلت بمعنى والله، واللهم، ويا الله، ولاه أبوك أو لاه أنت ونحوها.","what_is_not_ar":"ليس فرعا مستقلا عن معنى الإله المعبود من جهة الاشتقاق، ولا يدخل فيه إطلاق إله أو آلهة على كل معبود إذا لم يكن الكلام على صيغة الاسم أو النداء أو القسم."},"support_links":["sup_d38b0b75483e693be95a"]},{"boundary":"Dal, yalnızca istemeyi değil, belirli bir hedefe dayanarak yönelmeyi anlatır; katılık, tıkaç, baş sargısı, vurma ve sırf kalıcılık anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000882/B001","candidate_links":[{"candidate_id":"cand_a42921341111986525d0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صَّمَد","morph_features":"STEM|POS:N|LEM:S~amad|ROOT:Smd|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:2:2:2","qac_word_ref":"112:2:2","surface_ar":"صَّمَدُ"}],"gloss":"dayanak alarak bir hedefe yönelme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir hedefe bilerek yönelme ve o hedefi dayanak edinme eylemidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İşlerde ve ihtiyaçlarda kendisine yönelinen, topluluğunda üstün konumdaki kişiyi belirtir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsanların dua ve istekle yöneldiği yüce varlığa ilişkin özel bir adlandırmada kullanılır."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İnsanların gitmeyi amaçladığı bir ev, yönelinen ev olarak nitelenebilir."}}],"root_ar":"ص م د","root_id":"root_000882","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın eylemsel çekirdeğini verir; kişi ve özel adlandırma kullanımları bağlama göre ayrıca açıklanır.","boundary_detail":"Dal, yalnızca istemeyi değil, belirli bir hedefe dayanarak yönelmeyi anlatır; katılık, tıkaç, baş sargısı, vurma ve sırf kalıcılık anlamlarını kapsamaz.","branch_image_ar":"القصد إلى المعتمد المقصود","concept_gloss":"dayanak alarak bir hedefe yönelme","contextual_glosses":[{"applicability":"Topluluğunda üstün olan ve meselelerde başvuru mercii sayılan kişi için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Üstün kişi olmayı ve işlerde kendisine yönelinmesini birlikte korur."},"facet_ids":["F002"],"text":"işlerde kendisine başvurulan önder","usage_role":"contextual"},{"applicability":"İnsanların gitmeyi hedeflediği bir evin nitelemesi olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Evin belirli bir yönelişin hedefi oluşunu açıkça korur."},"facet_ids":["F004"],"text":"amaçlanan ev","usage_role":"contextual"}],"definition":"Bir şeyi belirli bir hedef edinerek ona yönelmek ve onu dayanak almaktır. Bundan hareketle, işlerde ve ihtiyaçlarda kendisine başvurulan üstün kişi de yönelinen merci olarak adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir hedefe bilerek yönelme ve o hedefi dayanak edinme eylemidir."},{"facet_id":"F002","role":"extension","statement":"İşlerde ve ihtiyaçlarda kendisine yönelinen, topluluğunda üstün konumdaki kişiyi belirtir."},{"facet_id":"F003","role":"specialization","statement":"İnsanların dua ve istekle yöneldiği yüce varlığa ilişkin özel bir adlandırmada kullanılır."},{"facet_id":"F004","role":"example","statement":"İnsanların gitmeyi amaçladığı bir ev, yönelinen ev olarak nitelenebilir."}],"identity_rationale":"Kaynak ifadesi, bir hedefe bilerek yönelme ve onu dayanak edinme çekirdeğini; ayrıca iş ve ihtiyaçlarda kendisine yönelinen üstün kişiyi açıkça bir arada verir. Verilen dal çerçevesi bu çekirdeği ve ondan gelişen kişi kullanımını doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"amaç edinme ve dayanarak yönelme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"onu amaçlayıp ona dayanarak yöneldi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"işlerde kendisine başvurulan en üstün kişi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"işlerde kendisine yönelinen kişi veya amaçlanan şey"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"amaçlanıp gidilen ev"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kulların dua ve istekle yöneldiği yüce varlığın adı"}],"lexicalization_note":"Tanım, hedefe yönelme çekirdeğini temel alır; kendisine başvurulan üstün kişi, amaçlanan ev ve özel adlandırma gibi biçime ya da belirli kullanıma bağlı yönleri ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan iki karşılaştırma, yönelişin sığınmadan ve önderlikte salt öncelikten ayrıldığı sınırları en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal amaçlama ve dayanma ilişkisini genel olarak kurar; komşu dal ise tehlike veya korku karşısında korunma ve yardım arayışını anlatır.","focus_only":"Yöneliş herhangi bir hedefe ya da işlerde başvurulan üstün kişiye olabilir ve acil korku şartı taşımaz.","gloss":"hedefe yönelme ile sığınma","neighbor_only":"Komşu dal, korkutucu bir durumda yardım için sığınılan kişi veya yere özgüdür.","neighbor_ref":"root_001152/B003","relation_type":"near_neighbor","shared_zone":"Her ikisinde de bir kişi ya da yer, kendisine yönelinen odak olabilir."},{"boundary_match":"field_only","distinction":"Buradaki ayırt edici ilişki başvuru ve yöneliştir; komşuda ise anılma sırasındaki öncelik belirleyicidir.","focus_only":"Üstün kişi, başkalarının iş ve ihtiyaçlarda kendisine yönelmesi bakımından adlandırılır.","gloss":"başvurulan önder ile önce anılan önder","neighbor_only":"Komşu dalda üstün kişi, önceliği nedeniyle adı ilk anılan kişidir.","neighbor_ref":"root_000091/B003","relation_type":"same_field","shared_zone":"İki dal da topluluk içinde üstün ve önde gelen bir kişiyi konu eder."}],"source_phrase_ar":"الصمد القصد وصمدته صمدا (maqayis); وصمدت قصدت وصمدت صمد كذا أي قصدت قصده واعتمدته (ayn); صمده يصمده صمدا أي قصده والصمد السيد لأنه يصمد إليه في الحوائج وبيت مصمد أي مقصود (sihah); الصمد السيد الذي قد انتهى سؤدده والذي يصمد إليه الأمر وصمدت صمد هذا الأمر أي قصدت قصده واعتمدته (tahdhib); الصمد السيد الذي يصمد إليه في الأمر وصمده قصد معتمدا عليه قصده (mufradat)","source_summary":"Kaynakların ortak çizgisi, hedefe yönelmeyi dayanak ve amaç ilişkisiyle kurar. Kişi kullanımında üstünlük, başkalarının iş ve ihtiyaçlarında o kişiye yönelmesiyle anlam kazanır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"قصد الشيء واعتماده؛ السيد الذي يقصد إليه في الأمور والحوائج؛ الصمد من جهة الصمود إليه","what_is_not_ar":"الصلابة وانعدام الجوف؛ المكان الصلب؛ الصماد عفاص القارورة؛ خرقة الرأس؛ الضرب بالعصا؛ الدوام المجرد"},"support_links":["sup_0bcf15b6b317decc09cb"]},{"boundary":"Dal genel bir katılık sözünden daha dardır: yoğun, oyuksuz ya da yarıksız bütünlük belirleyicidir; yönelme, kapatma, sarma, vurma ve kalıcılık bu sınıra girmez.","branch_kind":"bare","branch_ref":"root_000882/B002","candidate_links":[{"candidate_id":"cand_a50f256eef039a196575","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صَّمَد","morph_features":"STEM|POS:N|LEM:S~amad|ROOT:Smd|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:2:2:2","qac_word_ref":"112:2:2","surface_ar":"صَّمَدُ"}],"gloss":"içi boş olmayan katı bütünlük","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Katı, yoğun, içi boş olmayan ve yarık taşımayan bütünlük niteliğidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sert ya da yüksek ve kalın bir yerin fiziksel niteliğini belirtir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yere sağlam oturmuş kaya ile çetin ve sert zemin bu niteliğin örnekleridir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Dağın kalın bölümünden alçalıp düzleşen ve üzerinde ağaç yetişen arazi parçası özel bir yer kullanımıdır."}}],"root_ar":"ص م د","root_id":"root_000882","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın nesne ve yer kullanımlarını birleştiren fiziksel çekirdeği karşılar.","boundary_detail":"Dal genel bir katılık sözünden daha dardır: yoğun, oyuksuz ya da yarıksız bütünlük belirleyicidir; yönelme, kapatma, sarma, vurma ve kalıcılık bu sınıra girmez.","branch_image_ar":"الصلابة المكتنزة بلا جوف","concept_gloss":"içi boş olmayan katı bütünlük","contextual_glosses":[{"applicability":"Sert ya da yüksek ve kalın bir yerin anlatıldığı arazi bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dalın başka nesnelerdeki boşluksuz ve yoğun bütünlük kapsamını dışarıda bırakır.","preserves":"Yer kullanımındaki sertlik ve yükselti ya da kalınlık özelliklerini korur."},"facet_ids":["F002"],"text":"sert ve yüksekçe arazi","usage_role":"contextual"},{"applicability":"Toprakla aynı düzeyde sağlam duran kaya örneği için uygun bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel nitelik ile diğer sert yer ve nesne kullanımlarını dışarıda bırakır.","preserves":"Kayanın yere sağlam oturmuş ve sert oluşunu korur."},"facet_ids":["F003"],"text":"yere oturmuş kaya","usage_role":"contextual"}],"definition":"Bir şeyin katı, yoğun ve iç boşluğu ya da yarığı bulunmayan bir bütün oluşturmasıdır. Sert, yüksek ve kalın yerler ile yere sağlam oturmuş kaya ve çetin zemin bu niteliğin yer örnekleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Katı, yoğun, içi boş olmayan ve yarık taşımayan bütünlük niteliğidir."},{"facet_id":"F002","role":"specialization","statement":"Sert ya da yüksek ve kalın bir yerin fiziksel niteliğini belirtir."},{"facet_id":"F003","role":"example","statement":"Yere sağlam oturmuş kaya ile çetin ve sert zemin bu niteliğin örnekleridir."},{"facet_id":"F004","role":"source_variant","statement":"Dağın kalın bölümünden alçalıp düzleşen ve üzerinde ağaç yetişen arazi parçası özel bir yer kullanımıdır."}],"identity_rationale":"Kaynak ifadesi katılık, yoğun bütünlük ve iç boşluğunun bulunmamasını doğrudan bildirir; sert veya yüksek ve kalın yer, yere oturmuş kaya ve yarıktan yoksun sert yüzey örnekleri de bu çekirdeğe bağlıdır. Verilen dal çerçevesi kaynak kapsamını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"sert veya yüksek ve kalın yer"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"içi boş ve yüzeyi yarık olmayan katı şey"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"içi boş olmayan"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yere sağlam oturmuş düz kaya"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"dağın kalın bölümünden alçalıp düzleşen ağaçlı arazi"}],"lexicalization_note":"Tanım çıplak dalın katı, yoğun ve içi boş olmayan bütünlük çekirdeğiyle sınırlıdır; belirli nesne ve yer örnekleri bu çekirdeğin gerçekleşmeleridir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen karşılaştırmalar boşluksuz katılığı yoğunluk, kalınlık ve kazıyı durduran sert zemin kavramlarından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal boşluksuz bütünlüğü ve sert yerleri merkez alır; komşu dal yoğunlaşmayı daha çeşitli gövde ve topluluk örneklerine yayar.","focus_only":"İç boşluğunun bulunmaması ile sert, yüksek veya kalın yer ve zemin kullanımları bu dalda açıkça yer alır.","gloss":"boşluksuz katılık ile sıkı yoğunluk","neighbor_only":"Komşu dal, boru içinin doluluğundan sıkışık topluluğa kadar gövde yoğunluğu ve aralık azlığına uzanır.","neighbor_ref":"root_000884/B003","relation_type":"near_synonym","shared_zone":"İki dal da katı, sıkı ve boşluğu az bir fiziksel yapıyı anlatabilir."},{"boundary_match":"partial","distinction":"Burada yapıdaki boşluksuz katılık öndedir; komşuda cismin kalınlığı ve bunun akış ya da uzama üzerindeki etkisi öndedir.","focus_only":"Bu dalda iç boşluğu ve yarık bulunmaması belirleyici olabilir.","gloss":"katı bütünlük ile kalınlık","neighbor_only":"Komşu dal kalınlık ve iriliği, ayrıca akmayı veya uzamayı önleme sonuçlarını kapsar.","neighbor_ref":"root_000196/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal sertlik, yoğunluk ve kalınlık alanında kesişebilir."},{"boundary_match":"field_only","distinction":"Bu dal zeminin niteliğini adlandırır; komşu dal ise kazma eyleminin bu nitelik yüzünden durduğu olayı anlatır.","focus_only":"Sert zemin, bu dalda genel fiziksel niteliğin doğrudan bir yer gerçekleşmesidir.","gloss":"sert zemin ile kazı engeli","neighbor_only":"Komşu dal, kazının sert zemin veya dağa ulaşıp artık ilerleyememesi olayını gerektirir.","neighbor_ref":"root_000217/B005","relation_type":"same_field","shared_zone":"İki dal da sert toprak ya da dağ zeminiyle ilgilidir."}],"source_phrase_ar":"الصلابة في الشيء والصمد كل مكان صلب (maqayis); المصمت الذي ليس بأجوف والصمدة صخرة راسية (ayn); الصمد المكان المرتفع الغليظ والمصمد لغة في المصمت وهو الذي لا جوف له (sihah); المصمت الذي لا جوف له والمكان المرتفع الغليظ والمصمد الصلب الذي ليس فيه خدد والشديد من الأرض (tahdhib); الصمد الذي ليس بأجوف (mufradat)","source_summary":"Ortak anlatım katılığı, yoğunluğu ve boşluksuz bütünlüğü birleştirir. Yer kullanımları sert veya yüksek ve kalın araziyi; somut örnekler ise yere oturmuş kaya, yarıksız sert yüzey ve çetin zemini gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الصلابة والاكتناز وانعدام الجوف؛ المكان الصلب أو المرتفع الغليظ؛ الصخرة الراسية والأرض الشديدة","what_is_not_ar":"القصد إلى الشيء والسؤدد المقصود؛ الصماد بمعنى عفاص القارورة أو خرقة الرأس؛ الضرب بالعصا؛ الدوام"},"support_links":["sup_d38b0b75483e693be95a"]},{"boundary":"Dal yalnızca şişenin ağzındaki kapatma parçasına ve bu parçayla kapatma işlemine bağlıdır; genel kapatma, katılık veya başı bezle sarma anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000882/B003","candidate_links":[{"candidate_id":"cand_53a3f384ada79dfbceb0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صَّمَد","morph_features":"STEM|POS:N|LEM:S~amad|ROOT:Smd|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:2:2:2","qac_word_ref":"112:2:2","surface_ar":"صَّمَدُ"}],"gloss":"şişe ağzı tıkacı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Şişenin ağzını sıkıca kapatan tıkaç ya da kapatma parçasıdır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Şişeye bu kapatma parçasını takarak ağzını kapatma eylemidir."}}],"root_ar":"ص م د","root_id":"root_000882","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın nesne çekirdeğini kısa ve doğal biçimde karşılar; kapatma eylemi ayrıca verilir.","boundary_detail":"Dal yalnızca şişenin ağzındaki kapatma parçasına ve bu parçayla kapatma işlemine bağlıdır; genel kapatma, katılık veya başı bezle sarma anlamına genişletilmez.","branch_image_ar":"سدادة القارورة المحكمة","concept_gloss":"şişe ağzı tıkacı","contextual_glosses":[{"applicability":"Şişeye kapatma parçası takma eyleminin anlatıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Şişeye tıkaç takma işlemini ve bunun kapatma sonucunu korur."},"facet_ids":["F002"],"text":"şişeyi tıkaçla kapatmak","usage_role":"contextual"}],"definition":"Şişenin ağzına geçirilen ve içeriği dış etkilerden koruyarak ağzı kapatan tıkaçtır. Buna bağlı eylem, şişeye böyle bir tıkaç takıp ağzını kapatmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Şişenin ağzını sıkıca kapatan tıkaç ya da kapatma parçasıdır."},{"facet_id":"F002","role":"associated_use","statement":"Şişeye bu kapatma parçasını takarak ağzını kapatma eylemidir."}],"identity_rationale":"Kaynak ifadesi hem şişenin ağzını kapatan tıkacı hem de şişeye bu parçayı takarak ağzını kapatma eylemini verir. Verilen çerçeve nesne ile ona bağlı işlemi doğru biçimde bir arada, ancak ayırt edilebilir olarak tutar.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"şişe ağzı tıkacı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"şişeye tıkaç takıp ağzını kapatmak"}],"lexicalization_note":"Tanım şişe tıkacı adını, şişeyi bu tıkaçla kapatma kullanımından ayırır; işlem anlamı bağımsız bir genel kapatma fiili sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen iki komşu, şişeye özgü tıkaç ve takma işlemini daha geniş kapatıcı araç alanından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal şişeye ve ona tıkaç takma işlemine bağlıdır; komşu dalın kap ve kuyu kapsamı daha geniştir.","focus_only":"Bu dal hem şişe tıkacını hem de şişeyi o parçayla kapatma eylemini içerir.","gloss":"şişe tıkacı","neighbor_only":"Komşu dal tıkaç parçasını başka bir kap türüyle ve kuyu bağlamıyla da ilişkilendirir.","neighbor_ref":"root_000840/B018","relation_type":"near_synonym","shared_zone":"İki dal da dar ağızlı bir kabın ağzını kapatan parçayı adlandırır."},{"boundary_match":"partial","distinction":"Burada kapatılan açıklık şişenin ağzıdır; komşuda fiziksel veya mecazlı çok çeşitli eksiklik ve açıklıklar söz konusudur.","focus_only":"Belirli nesne şişe tıkacıdır ve buna bağlı takma eylemi de dalın parçasıdır.","gloss":"şişe tıkacı ile boşluk kapatıcı","neighbor_only":"Komşu dal delik, gedik, geçit ve ihtiyaç gibi çok çeşitli boşlukları gideren araçları kapsar.","neighbor_ref":"root_000687/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir açıklığı kapatan araç düşüncesi bulunur."}],"source_phrase_ar":"الصماد عفاص القارورة وصمدتها صمدا (ayn); الصماد عفاص القارورة (sihah); الصماد سداد القارورة والصماد عفاص القارورة وقد صمدتها أصمدها (tahdhib)","source_summary":"Kaynaklar şişe ağzındaki tıkaç konusunda birleşir; aktarılan fiil kullanımı da şişeye bu parçayı takıp ağzını kapatmayı anlatır.","sources":["AY","SI","TA"],"what_is_ar":"الصماد بمعنى عفاص القارورة أو سدادها؛ فعل صمد القارورة أي جعل لها صمادا","what_is_not_ar":"القصد والسؤدد؛ الصلابة العامة؛ خرقة الرأس؛ الضرب بالعصا؛ الدوام"},"support_links":["sup_c4b06d7e7f5b24bb607f"]},{"boundary":"Sarma işlemi başa ve sarık dışındaki bir bez, mendil ya da kumaşa özgüdür; şişe tıkacı, genel örtme ve sarık sarma bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000882/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صَّمَد","morph_features":"STEM|POS:N|LEM:S~amad|ROOT:Smd|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:2:2:2","qac_word_ref":"112:2:2","surface_ar":"صَّمَدُ"}],"gloss":"başı sarık dışındaki bezle sarma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başı bez, mendil veya kumaşla çevreleyip sarma eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kullanılan baş sargısı sarık değildir; başka tür bir bez, mendil veya kumaştır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başı sarmakta kullanılan bez, mendil veya kumaş parçasının adıdır."}}],"root_ar":"ص م د","root_id":"root_000882","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın işlem çekirdeğini ve sarığı dışlayan araç sınırını birlikte karşılar.","boundary_detail":"Sarma işlemi başa ve sarık dışındaki bir bez, mendil ya da kumaşa özgüdür; şişe tıkacı, genel örtme ve sarık sarma bu dala girmez.","branch_image_ar":"شد الرأس بصماد","concept_gloss":"başı sarık dışındaki bezle sarma","contextual_glosses":[{"applicability":"Başı sarmakta kullanılan bez, mendil veya kumaş parçası için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Parçanın başı sarmak için kullanılan bir kumaş olmasını korur."},"facet_ids":["F003"],"text":"baş sargısı","usage_role":"contextual"}],"definition":"Başı, sarık sayılmayan bir bez, mendil ya da kumaş parçasıyla çevreleyip sarmaktır. Bu işte kullanılan kumaş parçası da baş sargısı olarak adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başı bez, mendil veya kumaşla çevreleyip sarma eylemidir."},{"facet_id":"F002","role":"specialization","statement":"Kullanılan baş sargısı sarık değildir; başka tür bir bez, mendil veya kumaştır."},{"facet_id":"F003","role":"associated_use","statement":"Başı sarmakta kullanılan bez, mendil veya kumaş parçasının adıdır."}],"identity_rationale":"Kaynak ifadesi başın bez, mendil veya kumaşla sarılmasını ve kullanılan sargı parçasını açıkça belirtir; sarığı ise özellikle dışarıda bırakır. Verilen dal çerçevesi bu işlem, araç ve dışlama sınırını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"başını sarık dışındaki bir bezle sardı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"sarık olmayan bez baş sargısı"}],"lexicalization_note":"Tanım, başı belirli bir kumaş parçasıyla sarma kullanımını ve bu işte kullanılan sargıyı ayırır; anlam genel sarma ya da örtmeye genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan karşılaştırmalar bu baş sargısını genel bağlama ve çene altından geçirilen sarık kullanımından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın konusu yalnızca baş ve sarık dışındaki sargıdır; komşu dalın işlemi, nesnesi ve başlık türleri çok daha geniştir.","focus_only":"Bu dal başı bezle sarmaya özgüdür ve sarığı açıkça dışarıda bırakır.","gloss":"baş sargısı ile genel bağlama","neighbor_only":"Komşu dal baş dışında da bağlama, burma ve sıkıca katlamaya uzanır; sarık ve benzeri başlıkları da kapsar.","neighbor_ref":"root_001018/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir kumaş ya da bağla çevreleyip sıkı tutma düşüncesi bulunur."},{"boundary_match":"field_only","distinction":"Burada sarık özellikle dışlanır; komşu dal ise sarığın çene altından geçirilmesini kurucu koşul olarak taşır.","focus_only":"Baş, sarık sayılmayan bir bez veya kumaşla sarılır.","gloss":"bez baş sargısı ile çene altı sarığı","neighbor_only":"Komşu dalda sarık çene altından geçirilerek belirli bir sarma düzeni kurulur.","neighbor_ref":"root_001350/B003","relation_type":"same_field","shared_zone":"İki dal da baş çevresinde kumaşla yapılan bir sarma biçimini anlatır."}],"source_phrase_ar":"صمد رأسه تصميدا وذلك إذا لف رأسه بخرقة أو منديل أو ثوب ما خلا العمامة وهي الصماد (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, başın bez, mendil veya kumaşla sarıldığını ve bu parçanın sarık olmadığını özellikle belirtir."}],"source_summary":"Aktarılan kullanım başı kumaşla sarma işlemini, kullanılan baş sargısını ve sarığın kapsam dışında tutulmasını birlikte bildirir.","sources":["TA"],"what_is_ar":"تصميد الرأس بخرقة أو منديل أو ثوب دون العمامة","what_is_not_ar":"عفاص القارورة؛ القصد؛ الصلابة؛ الضرب بالعصا؛ الدوام"},"support_links":[]},{"boundary":"Dal belirli bir söz kalıbına bağlı olarak bir işin başında bulunma ve ona özen gösterme birlikteliğini anlatır; genel yönetim veya salt önemseme değildir.","branch_kind":"non_bare","branch_ref":"root_000882/B005","candidate_links":[{"candidate_id":"cand_c06b38ac32ecb0390a84","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صَّمَد","morph_features":"STEM|POS:N|LEM:S~amad|ROOT:Smd|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:2:2:2","qac_word_ref":"112:2:2","surface_ar":"صَّمَدُ"}],"gloss":"bir işin başında durup ona özen gösterme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir işin üzerinde bulunup gidişini gözetmektir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gözetilen işe önem vermek ve onunla özenle ilgilenmek kurucu bir koşuldur."}}],"root_ar":"ص م د","root_id":"root_000882","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Verilen özel kullanımın gözetim ve özen bileşenlerini birlikte karşılar.","boundary_detail":"Dal belirli bir söz kalıbına bağlı olarak bir işin başında bulunma ve ona özen gösterme birlikteliğini anlatır; genel yönetim veya salt önemseme değildir.","branch_image_ar":"الإشراف على الأمر مع الحفل به","concept_gloss":"bir işin başında durup ona özen gösterme","contextual_glosses":[{"applicability":"Bir kişinin sorumlu biçimde bir işin gidişiyle ilgilendiği bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gözetim ile önem ve özen göstermeyi birlikte korur."},"facet_ids":["F001","F002"],"text":"işi gözetip önemsemek","usage_role":"contextual"}],"definition":"Bir işin başında bulunarak onu gözetmek ve aynı zamanda o işe önem verip özen göstermektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir işin üzerinde bulunup gidişini gözetmektir."},{"facet_id":"F002","role":"core","statement":"Gözetilen işe önem vermek ve onunla özenle ilgilenmek kurucu bir koşuldur."}],"identity_rationale":"Kaynak ifadesi bir işin üzerinde bulunup onu gözetmeyi, aynı zamanda o işe önem ve özen vermeyi birlikte şart koşar. Verilen dal çerçevesi, yalnızca yönelme ya da ilgilenme değil, gözetim ile özenin birleştiği bu özel kullanımı doğru aktarır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir işin başında durup ona özen gösteren"}],"lexicalization_note":"Tanım yalnızca verilen söz kalıbındaki işin başında bulunma ve ona özen gösterme anlamına bağlıdır; çıplak köke bağımsız bir gözetim anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen ilişkiler özenli iş gözetimini genel idareden ve resmî göreve getirilmeden ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda işe önem verme ve özen gösterme zorunludur; komşu dal daha geniş koruma, bakım ve yönetim görevlerini içerir.","focus_only":"Bu dal belirli bir iş üzerinde bulunmayı ve o işe gönülden önem vermeyi birlikte gerektirir.","gloss":"özenli iş gözetimi ile genel idare","neighbor_only":"Komşu dal koruma, sürekli bakım, siyasal yönetim ve yetki gibi daha geniş görev ilişkilerini kapsar.","neighbor_ref":"root_001273/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir işin ya da şeyin başında bulunup onunla ilgilenmeyi anlatır."},{"boundary_match":"partial","distinction":"Burada ilişkinin özü fiilî gözetim ve özendir; komşuda görevin verilmesi ve resmî yetki belirleyicidir.","focus_only":"Gözetim, işe önem ve özen göstermeyle tanımlanır; resmî atama şart değildir.","gloss":"özenli gözetim ile göreve atanma","neighbor_only":"Komşu dal resmî bir göreve getirilme ve özellikle kamu işini üstlenme ilişkisini taşır.","neighbor_ref":"root_001046/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal bir işin sorumluluğunu üstlenip onun başında bulunma alanında buluşur."}],"source_phrase_ar":"إني على صمادة من أمر إذا أشرف عليه وحفلت به (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, işin başında bulunma ile o işi önemseyip özenle yürütmeyi aynı kullanım içinde birleştirir."}],"source_summary":"Aktarılan özel kullanım, bir iş üzerinde gözetici konumda bulunmayı o işe içten önem ve özen göstermeyle birleştirir.","sources":["TA"],"what_is_ar":"قولهم على صمادة من أمر لمن أشرف عليه وحفل به","what_is_not_ar":"القصد المجرد؛ الصلابة؛ عفاص القارورة؛ خرقة الرأس؛ الضرب بالعصا"},"support_links":["sup_4ea991c1511a7c7096c3"]},{"boundary":"Dal değnekle vurma söz öbeğine bağlıdır; genel vurma, kılıçla vurma veya çıplak kökün bağımsız anlamı olarak yorumlanmaz.","branch_kind":"collocation","branch_ref":"root_000882/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صَّمَد","morph_features":"STEM|POS:N|LEM:S~amad|ROOT:Smd|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:2:2:2","qac_word_ref":"112:2:2","surface_ar":"صَّمَدُ"}],"gloss":"değnekle vurma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir hedefe vurma eylemi değnek aracılığıyla gerçekleştirilir."}}],"root_ar":"ص م د","root_id":"root_000882","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca değnek aracını içeren söz öbeğinin tam eylem anlamını karşılar.","boundary_detail":"Dal değnekle vurma söz öbeğine bağlıdır; genel vurma, kılıçla vurma veya çıplak kökün bağımsız anlamı olarak yorumlanmaz.","branch_image_ar":"إيقاع الضرب بالعصا","concept_gloss":"değnekle vurma","contextual_glosses":[{"applicability":"Geçmiş zamanda bir hedefe değnekle vurulduğunu anlatan cümlelerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemin hedefini, vurmayı ve değnek aracını doğal cümle biçiminde korur."},"facet_ids":["F001"],"text":"ona değnekle vurdu","usage_role":"contextual"}],"definition":"Bir kişiye ya da nesneye değnek kullanarak vurma eylemidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir hedefe vurma eylemi değnek aracılığıyla gerçekleştirilir."}],"identity_rationale":"Kaynak ifadesi bir kişiye ya da nesneye değnekle vurmayı açıkça ve yalnızca bu araçla kurulan kullanım içinde bildirir. Verilen dal çerçevesi eylemi, aracı ve kullanım sınırını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ona değnekle vurdu"}],"lexicalization_note":"Tanım yalnızca değnek aracını açıkça içeren yapıya bağlıdır; buradan genel bir vurma anlamı ya da başka araçlara uzanan çıplak dal çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen iki yakın ilişki, değnek koşulunu genel vurma ve daha özel çubukla vurma kapsamlarından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Değnekli bağlamda karşılıklar yakındır; komşu dalın araçsız genel vurma kapsamı bu dalda bulunmaz.","focus_only":"Bu dal yalnızca değnek aracını içeren belirli yapıyla sınırlıdır.","gloss":"değnekle vurma","neighbor_only":"Komşu dal değnekle vurmanın yanında araç belirtilmeyen genel vurma kullanımını da kapsar.","neighbor_ref":"root_001443/B006","relation_type":"near_synonym","shared_zone":"İki dal da bir hedefe değnek kullanarak vurma bağlamında örtüşür."},{"boundary_match":"partial","distinction":"Ortak eylem vurmadır, ancak araç sınırı aynı değildir: bu dal değneği, komşu ise özel olarak ince çubuğu öne çıkarır.","focus_only":"Bu dalda araç genel olarak değnektir ve belirli söz öbeği sınırı korunur.","gloss":"değnekle vurma ile çubukla vurma","neighbor_only":"Komşu dal, daha ince ve belirli bir çubuk türüyle vurmayı gerektirir.","neighbor_ref":"root_001236/B006","relation_type":"near_synonym","shared_zone":"İki dal da sopa türü bir araçla vurma eylemini anlatır."}],"source_phrase_ar":"صمده بالعصا صمدا إذا ضربه بها (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, eylemin değnekle gerçekleştirilen bir vurma olduğunu açıkça sınırlar."}],"source_summary":"Aktarılan kullanım vurma eylemini, kullanılan aracın değnek olması koşuluyla verir.","sources":["TA"],"what_is_ar":"صمده بالعصا بمعنى ضربه بها","what_is_not_ar":"قصد الشيء واعتماده؛ الصلابة؛ السداد؛ الدوام"},"support_links":[]},{"boundary":"Genel anlam kalıcılık ve sürekliliktir; soğuk, kıtlık ve sürekli süt verme koşulları yalnızca dişi deveye ilişkin özel kullanıma aittir.","branch_kind":"mixed_non_bare","branch_ref":"root_000882/B007","candidate_links":[{"candidate_id":"cand_d5725b0c659bce7656db","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صَّمَد","morph_features":"STEM|POS:N|LEM:S~amad|ROOT:Smd|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:2:2:2","qac_word_ref":"112:2:2","surface_ar":"صَّمَدُ"}],"gloss":"kalıcı ve sürekli olma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sürekli olma, kalma ve yok oluşa rağmen varlığını koruma niteliğidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişi devenin soğuk ve kıtlık koşullarında varlığını ve dayanıklılığını korumasıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu dişi devenin zorlu koşullarda süt vermeyi kesintisiz sürdürmesi de özel kullanımın parçasıdır."}}],"root_ar":"ص م د","root_id":"root_000882","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın genel çekirdeğini karşılar; dişi deveye özgü dayanma ve süt verme ayrıntıları ayrıca belirtilir.","boundary_detail":"Genel anlam kalıcılık ve sürekliliktir; soğuk, kıtlık ve sürekli süt verme koşulları yalnızca dişi deveye ilişkin özel kullanıma aittir.","branch_image_ar":"الدوام والبقاء على الشدة","concept_gloss":"kalıcı ve sürekli olma","contextual_glosses":[{"applicability":"Başka varlıklar yok olduktan sonra da varlığını sürdüren için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başkalarının yok oluşundan sonra da kalma sınırını açıkça korur."},"facet_ids":["F001"],"text":"yok oluştan sonra da kalan","usage_role":"contextual"},{"applicability":"Soğuk ve kıtlığa dayanırken süt vermeyi sürdüren dişi deve için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanı, zorlu koşullara dayanmayı ve kesintisiz süt vermeyi birlikte korur."},"facet_ids":["F002","F003"],"text":"zorlu koşullarda sütü kesilmeyen dişi deve","usage_role":"explanatory"}],"definition":"Bir varlığın sürekli olması ve başkaları yok olduktan sonra da varlığını korumasıdır. Dişi deveye ilişkin özel kullanım, soğuk ve kıtlıkta ayakta kalırken süt vermeyi kesintisiz sürdürmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sürekli olma, kalma ve yok oluşa rağmen varlığını koruma niteliğidir."},{"facet_id":"F002","role":"specialization","statement":"Dişi devenin soğuk ve kıtlık koşullarında varlığını ve dayanıklılığını korumasıdır."},{"facet_id":"F003","role":"specialization","statement":"Bu dişi devenin zorlu koşullarda süt vermeyi kesintisiz sürdürmesi de özel kullanımın parçasıdır."}],"identity_rationale":"Kaynak ifadesinin genel çekirdeği sürekli olma ve yok oluştan sonra da kalmadır. Soğuk ve kıtlık altında dayanma ile sütün kesintisiz gelmesi ise yalnızca dişi deve kullanımının kurucu ayrıntılarıdır; bu nedenle dal başlığındaki zorluk altında kalma unsuru genel kalıcılığa yayılmadan sınırlandırılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"sürekli ve yok oluştan sonra da kalan"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"soğuk ve kıtlıkta dayanıp sütü kesilmeyen dişi deve"}],"lexicalization_note":"Tanım genel kalıcı ve sürekli olma biçimini, zorlu koşullara dayanıp sütü sürme anlamındaki dişi deve kullanımından ayırır; özel koşullar genel çekirdeğe katılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen yakın anlamlar genel kalıcılık çekirdeğini uzun ömür, etki, mekânda kalma ve direnme uzantılarından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Genel kalıcılıkta yakın olsalar da bu dalın yok oluştan sonra kalma ve hayvana özgü dayanma ayrıntıları, komşunun uzun ömür ve etki kapsamından ayrılır.","focus_only":"Bu dal, başkalarının yok oluşundan sonra kalmayı ve dişi devenin zorlu koşullarda sütü sürdürmesini içerir.","gloss":"kalıcı olma ile varlığını sürdürme","neighbor_only":"Komşu dal uzun yaşama, izin veya etkinin kalması ve ödülün sürmesi gibi daha geniş sonuçlara uzanır.","neighbor_ref":"root_000142/B001","relation_type":"near_synonym","shared_zone":"İki dal da yok olmama, kalma ve süreklilik çekirdeğinde büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Bu dal süreklilik ve sonradan da kalma eksenindedir; komşu dal mekânda kalma ve eylem sırasında sağlam durma alanlarına da yayılır.","focus_only":"Bu dalda başkalarının yok oluşundan sonra kalma ve özel hayvan kullanımı bulunur.","gloss":"kalıcılık ile süreğen sağlam duruş","neighbor_only":"Komşu dal bir yerde kalma, savaşta direnme ve ayakların sağlam durması gibi durumları kapsar.","neighbor_ref":"root_000192/B001","relation_type":"near_synonym","shared_zone":"İki dal da devam etme, yok olmama ve varlığını koruma düşüncesini taşır."}],"source_phrase_ar":"الصمد الدائم والدائم الباقي بعد فناء خلقه وناقة مصماد وهي الباقية على القر والجدب الدائمة الرسل (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, genel kalıcılık anlamının yanında soğuk ve kıtlıkta ayakta kalıp sürekli süt veren dişi deve kullanımını aktarır."}],"source_summary":"Aktarılan anlam genel düzeyde süreklilik ve başkalarının yok oluşundan sonra da kalmayı bildirir. Hayvan kullanımında bu çekirdek, soğuk ve kıtlığa dayanma ile süt vermeyi sürdürme ayrıntılarıyla özelleşir.","sources":["TA"],"what_is_ar":"الدوام والبقاء؛ الناقة المصماد الباقية على القر والجدب الدائمة الرسل","what_is_not_ar":"القصد إلى المقصود؛ الصلابة بلا جوف؛ عفاص القارورة؛ خرقة الرأس؛ الضرب بالعصا"},"support_links":["sup_53737a18d5bd4e8a4646"]}],"candidate_inventory":[{"anchor_refs":["112:2:1"],"branch_refs":[],"candidate_id":"cand_be85a610006b70017251","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:2:1:asyndetic-declaration","source_type":"word_analysis","support_ids":["sup_2c21b2dd987040ecb483","sup_3657b78e40854ed40f66"],"title":"bare declaration after command scope","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:1","qac_refs":["112:2:1:1"],"status":"accepted"}},{"anchor_refs":["112:2:1"],"branch_refs":[],"candidate_id":"cand_650efb38734c925d4fe4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:2:1:boundary-resolution-launch","source_type":"word_analysis","support_ids":["sup_3657b78e40854ed40f66","sup_850a3987a3a5d3154252"],"title":"repeated name resolves and relaunches","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:1","qac_refs":["112:2:1:1"],"status":"accepted"}},{"anchor_refs":["112:2:1"],"branch_refs":[],"candidate_id":"cand_bcc8f5d4cb3c0fb506d5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:2:1:compressed-subject-against-expansion","source_type":"word_analysis","support_ids":["sup_09350a9f0eb1d555f41c","sup_3657b78e40854ed40f66"],"title":"variant expansion highlights compression","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:1","qac_refs":["112:2:1:1"],"status":"accepted"}},{"anchor_refs":["112:2:1"],"branch_refs":[],"candidate_id":"cand_be0b4899f2c04b9244d5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:2:1:directional-name-resonance","source_type":"word_analysis","support_ids":["sup_3657b78e40854ed40f66","sup_a06bb63529f36a8c2a4c"],"title":"refuge and worship pressure meets the predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:1","qac_refs":["112:2:1:1"],"status":"accepted"}},{"anchor_refs":["112:2:1"],"branch_refs":[],"candidate_id":"cand_51d9f1bb05f512d00ff1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:2:1:formal-pairing-cadence","source_type":"word_analysis","support_ids":["sup_3657b78e40854ed40f66","sup_c1384eaf3bfba1cae322"],"title":"definite nominative pair heard as one frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:1","qac_refs":["112:2:1:1"],"status":"accepted"}},{"anchor_refs":["112:2:1"],"branch_refs":[],"candidate_id":"cand_ee72f60bcbd4da276191","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:2:1:nominal-identity-equation","source_type":"word_analysis","support_ids":["sup_2e56c8f9887b8ca526bf","sup_3657b78e40854ed40f66"],"title":"proper-name subject in a verbless equation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:1","qac_refs":["112:2:1:1"],"status":"accepted"}},{"anchor_refs":["112:2:1"],"branch_refs":[],"candidate_id":"cand_e9fe68c16d1e74997db4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:2:1:proper-name-definiteness","source_type":"word_analysis","support_ids":["sup_3657b78e40854ed40f66","sup_4ce2fc96e45b91297dd2"],"title":"proper name blocks a class reading","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:1","qac_refs":["112:2:1:1"],"status":"accepted"}},{"anchor_refs":["112:2:1"],"branch_refs":[],"candidate_id":"cand_ebd9bf3a1c41fa3f7051","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:2:1:recognizable-name-before-rare-predicate","source_type":"word_analysis","support_ids":["sup_3657b78e40854ed40f66","sup_b46945dbddc2e67a5259"],"title":"familiar subject before rare predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:1","qac_refs":["112:2:1:1"],"status":"accepted"}},{"anchor_refs":["112:2:2"],"branch_refs":[],"candidate_id":"cand_4326d6eee9ff03458f8c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000882"],"scope":"focus_ayah","source_local_id":"112:2:2:bare-equation-contraction","source_type":"word_analysis","support_ids":["sup_0e5281b0114a391ad145","sup_ae3ad031df9e82bd1f10"],"title":"definition contracts into two elements","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:2","qac_refs":["112:2:2:1","112:2:2:2"],"status":"accepted"}},{"anchor_refs":["112:2:2"],"branch_refs":[],"candidate_id":"cand_bad4a453decdb5dbed8d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000882"],"scope":"focus_ayah","source_local_id":"112:2:2:chiefly-center-of-recourse","source_type":"word_analysis","support_ids":["sup_ae3ad031df9e82bd1f10","sup_f86d32971f6b9d57eb5e"],"title":"recognized center of recourse","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:2","qac_refs":["112:2:2:1","112:2:2:2"],"status":"accepted"}},{"anchor_refs":["112:2:2"],"branch_refs":[],"candidate_id":"cand_1429db97204cf3639a6e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000882"],"scope":"focus_ayah","source_local_id":"112:2:2:closure-and-surah-arc","source_type":"word_analysis","support_ids":["sup_8a3a825a40b8805afd24","sup_ae3ad031df9e82bd1f10"],"title":"predicate closes and bridges the surah","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:2","qac_refs":["112:2:2:1","112:2:2:2"],"status":"accepted"}},{"anchor_refs":["112:2:2"],"branch_refs":[],"candidate_id":"cand_4ceb16888d2675c2df52","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000882"],"scope":"focus_ayah","source_local_id":"112:2:2:convergent-sealed-effect","source_type":"word_analysis","support_ids":["sup_31dbb87f2905814ce559","sup_ae3ad031df9e82bd1f10"],"title":"rarity, position, sound, and polysemy converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:2","qac_refs":["112:2:2:1","112:2:2:2"],"status":"accepted"}},{"anchor_refs":["112:2:2"],"branch_refs":[],"candidate_id":"cand_098a69395fee737bbcea","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000882"],"scope":"focus_ayah","source_local_id":"112:2:2:definite-title-shape","source_type":"word_analysis","support_ids":["sup_461893262197fc0192b6","sup_ae3ad031df9e82bd1f10"],"title":"al-marked singular noun becomes a title","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:2","qac_refs":["112:2:2:1","112:2:2:2"],"status":"accepted"}},{"anchor_refs":["112:2:2"],"branch_refs":[],"candidate_id":"cand_6c83ff34129d8b670544","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000882"],"scope":"focus_ayah","source_local_id":"112:2:2:endurance-background","source_type":"word_analysis","support_ids":["sup_48455856256947a984ce","sup_ae3ad031df9e82bd1f10"],"title":"endurance colors the title without changing its form","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:2","qac_refs":["112:2:2:1","112:2:2:2"],"status":"accepted"}},{"anchor_refs":["112:2:2"],"branch_refs":[],"candidate_id":"cand_4e10e4859bc26b628bfe","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000882"],"scope":"focus_ayah","source_local_id":"112:2:2:formal-attribute-option","source_type":"word_analysis","support_ids":["sup_7c9c965565caaeb279c2","sup_ae3ad031df9e82bd1f10"],"title":"case permits attribute, clause need selects predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:2","qac_refs":["112:2:2:1","112:2:2:2"],"status":"accepted"}},{"anchor_refs":["112:2:2"],"branch_refs":[],"candidate_id":"cand_4b05e24b1774baf39eaf","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000882"],"scope":"focus_ayah","source_local_id":"112:2:2:formal-reprise-rhyme","source_type":"word_analysis","support_ids":["sup_ae3ad031df9e82bd1f10","sup_fcf8c4d28f4f368a1350"],"title":"local reprise and rhyme bind the definition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:2","qac_refs":["112:2:2:1","112:2:2:2"],"status":"accepted"}},{"anchor_refs":["112:2:2"],"branch_refs":[],"candidate_id":"cand_9baa8defff3953ac3287","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000882"],"scope":"focus_ayah","source_local_id":"112:2:2:hapax-isolated-predicate","source_type":"word_analysis","support_ids":["sup_427cff871706e1041d34","sup_ae3ad031df9e82bd1f10"],"title":"single Quranic occurrence concentrates meaning","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:2","qac_refs":["112:2:2:1","112:2:2:2"],"status":"accepted"}},{"anchor_refs":["112:2:2"],"branch_refs":[],"candidate_id":"cand_0e2f8eaf5e40f2207d62","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000882"],"scope":"focus_ayah","source_local_id":"112:2:2:predicate-title-closes-clause","source_type":"word_analysis","support_ids":["sup_ae3ad031df9e82bd1f10","sup_d095877a796dc847aaf7"],"title":"definite predicate completes the equation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:2","qac_refs":["112:2:2:1","112:2:2:2"],"status":"accepted"}},{"anchor_refs":["112:2:2"],"branch_refs":[],"candidate_id":"cand_bee77edbda88fed1d2a4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000882"],"scope":"focus_ayah","source_local_id":"112:2:2:resort-and-self-sufficiency","source_type":"word_analysis","support_ids":["sup_ae3ad031df9e82bd1f10","sup_d52145faa12efa8ae768"],"title":"need moves one way toward the self-sufficient","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:2","qac_refs":["112:2:2:1","112:2:2:2"],"status":"accepted"}},{"anchor_refs":["112:2:2"],"branch_refs":[],"candidate_id":"cand_7657a95740300f3857b4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000882"],"scope":"focus_ayah","source_local_id":"112:2:2:solid-no-hollow-image","source_type":"word_analysis","support_ids":["sup_3fd710d799eba5b6d215","sup_ae3ad031df9e82bd1f10"],"title":"solid no-hollow image becomes metaphysical","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:2","qac_refs":["112:2:2:1","112:2:2:2"],"status":"accepted"}},{"anchor_refs":["112:2:2"],"branch_refs":[],"candidate_id":"cand_cdb4dfc053c52b703611","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000882"],"scope":"focus_ayah","source_local_id":"112:2:2:sound-pressure","source_type":"word_analysis","support_ids":["sup_ae3ad031df9e82bd1f10","sup_e1ccac6f9cd2b203e7d5"],"title":"compressed sound reinforces the no-hollow image","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:2","qac_refs":["112:2:2:1","112:2:2:2"],"status":"accepted"}},{"anchor_refs":["112:2:2"],"branch_refs":[],"candidate_id":"cand_57c24b9ae3f82884c592","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000882"],"scope":"focus_ayah","source_local_id":"112:2:2:surface-noun-not-process","source_type":"word_analysis","support_ids":["sup_56f7390885ea359e3ac3","sup_ae3ad031df9e82bd1f10"],"title":"settled noun absorbs process meanings","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:2","qac_refs":["112:2:2:1","112:2:2:2"],"status":"accepted"}},{"anchor_refs":["112:2:2"],"branch_refs":[],"candidate_id":"cand_f2a002c050c3b204f702","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000882"],"scope":"focus_ayah","source_local_id":"112:2:2:variant-compression","source_type":"word_analysis","support_ids":["sup_442f46dbfacf4e28327a","sup_ae3ad031df9e82bd1f10"],"title":"expanded variants highlight immediate predication","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:2:2","qac_refs":["112:2:2:1","112:2:2:2"],"status":"accepted"}},{"anchor_refs":["112:2:1"],"branch_refs":[],"candidate_id":"cand_bb3e31b563d8692eb0c8","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000047"],"scope":"focus_ayah","source_local_id":"112:2:1:1","source_type":"qac_morpheme","support_ids":["sup_624bd68b52a4949c925d"],"title":"QAC root occurrence: ء ل ه","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["112:2:2"],"branch_refs":[],"candidate_id":"cand_c4e17f0bcccf4ca31f14","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000882"],"scope":"focus_ayah","source_local_id":"112:2:2:2","source_type":"qac_morpheme","support_ids":["sup_7929d4c7ca526c6f45d7"],"title":"QAC root occurrence: ص م د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["112:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:2","branch_refs":["root_000047/B001","root_000882/B001"],"candidate_id":"cand_a42921341111986525d0","commentary_obligation":"review","hft_ref":"hft_4c76530b560b236a7aa1","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-resort-terminal","source_type":"hft","support_ids":["sup_0bcf15b6b317decc09cb"],"title":"baseline-resort-terminal","trust":"legacy_unbound"},{"anchor_refs":["112:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:2","branch_refs":["root_000047/B002","root_000882/B002"],"candidate_id":"cand_a50f256eef039a196575","commentary_obligation":"review","hft_ref":"hft_0051e0fd0ef0c406e885","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-compact-integrity","source_type":"hft","support_ids":["sup_d38b0b75483e693be95a"],"title":"baseline-compact-integrity","trust":"legacy_unbound"},{"anchor_refs":["112:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:2","branch_refs":["root_000047/B001","root_000882/B003"],"candidate_id":"cand_53a3f384ada79dfbceb0","commentary_obligation":"review","hft_ref":"hft_bb9f3c6a27acf5c7108b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-sealing-closure","source_type":"hft","support_ids":["sup_c4b06d7e7f5b24bb607f"],"title":"baseline-sealing-closure","trust":"legacy_unbound"},{"anchor_refs":["112:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:2","branch_refs":["root_000047/B001","root_000882/B007"],"candidate_id":"cand_d5725b0c659bce7656db","commentary_obligation":"review","hft_ref":"hft_0154a4557c4d8460685b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-enduring-supply","source_type":"hft","support_ids":["sup_53737a18d5bd4e8a4646"],"title":"baseline-enduring-supply","trust":"legacy_unbound"},{"anchor_refs":["112:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:2","branch_refs":["root_000047/B001","root_000882/B005"],"candidate_id":"cand_c06b38ac32ecb0390a84","commentary_obligation":"review","hft_ref":"hft_a093934e794fe6217b76","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-attentive-threshold","source_type":"hft","support_ids":["sup_4ea991c1511a7c7096c3"],"title":"baseline-attentive-threshold","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","qac_morphemes":[{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|NOM","morpheme_role":"STEM","pos":"PN","qac_ref":"112:2:1:1","qac_word_ref":"112:2:1","root_ar":"ء ل ه","surface_ar":"ٱللَّهُ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"112:2:2:1","qac_word_ref":"112:2:2","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"صَّمَد","morph_features":"STEM|POS:N|LEM:S~amad|ROOT:Smd|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:2:2:2","qac_word_ref":"112:2:2","root_ar":"ص م د","surface_ar":"صَّمَدُ"}],"word_analysis_qac_refs":[["112:2:1:1"],["112:2:2:1","112:2:2:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["112:2:1","112:2:2"]},"focus_surface_evidence":{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","qac_morphemes":[{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|NOM","morpheme_role":"STEM","pos":"PN","qac_ref":"112:2:1:1","qac_word_ref":"112:2:1","root_ar":"ء ل ه","surface_ar":"ٱللَّهُ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"112:2:2:1","qac_word_ref":"112:2:2","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"صَّمَد","morph_features":"STEM|POS:N|LEM:S~amad|ROOT:Smd|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:2:2:2","qac_word_ref":"112:2:2","root_ar":"ص م د","surface_ar":"صَّمَدُ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["112:2:1:1"],["112:2:2:1","112:2:2:2"]],"word_analysis_refs":["112:2:1","112:2:2"],"word_rows":[{"analysis_record_ref":"112:2:1","analytic_gloss_range_en":"the proper divine name as nominative subject of a two-word nominal equation; not the common countable deity noun","analytic_root_gloss_range_en":"proper-name field with debated derivational pressure around worship, bewilderment, and refuge; local grammar selects the fixed divine name while allowing directional resonance with the predicate","qac_refs":["112:2:1:1"],"root":{"arabic":"أ ل ه","transliteration":"ʾ-l-h"},"surface":{"arabic":"ٱللَّهُ","transliteration":"allāhu"}},{"analysis_record_ref":"112:2:2","analytic_gloss_range_en":"the definite predicate-title, locally gathering resort-in-need, self-sufficiency, solidity without hollowness, and acknowledged mastery while excluding process senses as the main local reading","analytic_root_gloss_range_en":"accepted root range includes intending and resorting to a relied-on one, compact solidity without hollowness, stopping, wrapping, attention to an affair, striking with a stick, and enduring; the local title activates the resort, solidity, endurance, and mastery field, not the unrelated stopper, wrapping, verge, or striking branches","qac_refs":["112:2:2:1","112:2:2:2"],"root":{"arabic":"ص م د","transliteration":"ṣ-m-d"},"surface":{"arabic":"ٱلصَّمَدُ","transliteration":"aṣ-ṣamad"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":2,"words_total":2,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["112:2"],"branch_refs":["root_000047/B001","root_000882/B001"],"candidate_id":"cand_a42921341111986525d0","evidence_scope":"focus_ayah","hft_ref":"hft_4c76530b560b236a7aa1","item_id":"baseline-resort-terminal","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-resort-terminal","support_id":"sup_0bcf15b6b317decc09cb"},{"anchor_refs":["112:2"],"branch_refs":["root_000047/B002","root_000882/B002"],"candidate_id":"cand_a50f256eef039a196575","evidence_scope":"focus_ayah","hft_ref":"hft_0051e0fd0ef0c406e885","item_id":"baseline-compact-integrity","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-compact-integrity","support_id":"sup_d38b0b75483e693be95a"},{"anchor_refs":["112:2"],"branch_refs":["root_000047/B001","root_000882/B003"],"candidate_id":"cand_53a3f384ada79dfbceb0","evidence_scope":"focus_ayah","hft_ref":"hft_bb9f3c6a27acf5c7108b","item_id":"baseline-sealing-closure","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-sealing-closure","support_id":"sup_c4b06d7e7f5b24bb607f"},{"anchor_refs":["112:2"],"branch_refs":["root_000047/B001","root_000882/B007"],"candidate_id":"cand_d5725b0c659bce7656db","evidence_scope":"focus_ayah","hft_ref":"hft_0154a4557c4d8460685b","item_id":"baseline-enduring-supply","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-enduring-supply","support_id":"sup_53737a18d5bd4e8a4646"},{"anchor_refs":["112:2"],"branch_refs":["root_000047/B001","root_000882/B005"],"candidate_id":"cand_c06b38ac32ecb0390a84","evidence_scope":"focus_ayah","hft_ref":"hft_a093934e794fe6217b76","item_id":"baseline-attentive-threshold","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-attentive-threshold","support_id":"sup_4ea991c1511a7c7096c3"}],"diagnostics":[],"lane_counts":{"global":9,"macro":11,"micro":5},"packet_summary":{"ayah_count":4,"focus_ref":"112:2","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]}],"window":["112:1","112:2","112:3","112:4"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"112:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":16,"unstructured_record_count":0},"identity":{"ayah_ref":"112:2","lane":"micro","linguistic_source_ref":"112:2","surface_ref":"112:2","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"112:2","target_tokens":[["Allah",["112:2:1"]],["herkesin",["112:2:2"]],["dayanağıdır",["112:2:2"]]],"text":"Allah, herkesin dayanağıdır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":4,"id":"s112-p01-001-004","label":"Whole surah","number":1,"refs":["112:1","112:2","112:3","112:4"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:1:compressed-subject-against-expansion","source_type":"word_analysis","support_id":"sup_09350a9f0eb1d555f41c","text":"{\"blocking_evidence\":null,\"headline\":\"variant expansion highlights compression\",\"reader_payoff\":\"The reader notices how little the standard subject slot says before the predicate arrives: one fixed name carries what expanded formulae might spell out.\",\"reason\":\"The variant and derivational pressures are useful as contrast, but they are narrowed because the local Hafs surface remains the compact proper name.\",\"representative_source_ids\":[\"QF-6b358e7e\",\"QF-56f51878\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:2:bare-equation-contraction","source_type":"word_analysis","support_id":"sup_0e5281b0114a391ad145","text":"{\"blocking_evidence\":null,\"headline\":\"definition contracts into two elements\",\"reader_payoff\":\"The reader notices the structural contraction from proposition to bare equation as the second predicate gives content to divine oneness.\",\"reason\":\"The local attachment evidence confirms that 112:2 is only subject plus predicate, allowing the boundary claim about contraction from 112:1 to survive.\",\"representative_source_ids\":[\"QB-6c4a0e9a\",\"QB-8e53d222\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:1:asyndetic-declaration","source_type":"word_analysis","support_id":"sup_2c21b2dd987040ecb483","text":"{\"blocking_evidence\":null,\"headline\":\"bare declaration after command scope\",\"reader_payoff\":\"The reader feels the ayah as a bare declaration even though it may still belong to the commanded speech opened in 112:1.\",\"reason\":\"The complete nominal clause and lack of an opening connector support a declarative restart, while the broader command scope from 112:1 is not grammatically excluded.\",\"representative_source_ids\":[\"QG-a7660f10\",\"QT-5188bd8c\",\"QB-215ba493\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:1:nominal-identity-equation","source_type":"word_analysis","support_id":"sup_2e56c8f9887b8ca526bf","text":"{\"blocking_evidence\":null,\"headline\":\"proper-name subject in a verbless equation\",\"reader_payoff\":\"The reader notices that the ayah states identity through a subject-predicate frame, not through an event, command, or timed action.\",\"reason\":\"QAC and attachment evidence identify {{ar:ٱللَّهُ}} ({{tr:allāhu}}) as the nominative mubtada and {{ar:ٱلصَّمَدُ}} ({{tr:aṣ-ṣamad}}) as its predicate in a complete nominal clause.\",\"representative_source_ids\":[\"QG-3b9bd78e\",\"QS-2e5afc7b\",\"QT-1ffb26f2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:2:convergent-sealed-effect","source_type":"word_analysis","support_id":"sup_31dbb87f2905814ce559","text":"{\"blocking_evidence\":null,\"headline\":\"rarity, position, sound, and polysemy converge\",\"reader_payoff\":\"The reader notices that the final predicate feels sealed because rarity, final position, recited pressure, and layered meaning converge on one word.\",\"reason\":\"The convergence topic gathers already supported facts: hapax distribution, ayah-final predicate position, accepted lexical branches, and sound-form observations.\",\"representative_source_ids\":[\"QY-450f43e1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:1","source_type":"word_analysis","support_id":"sup_3657b78e40854ed40f66","text":"{\"gloss_range\":\"the proper divine name as nominative subject of a two-word nominal equation; not the common countable deity noun\",\"prose\":\"{{ar:ٱللَّهُ}} ({{tr:allāhu}}) opens the ayah as the named subject of a verbless equation. Its proper-name definiteness blocks a generic deity-class reading, while the shared definiteness and final u cadence balance the following definite predicate, {{ar:ٱلصَّمَدُ}} ({{tr:aṣ-ṣamad}}), as a matched two-noun frame. The repeated name also resets the boundary after 112:1: the prior pointing is resolved into explicit naming, and the clause launches without a connector or command marker. Against expanded variant formulae, the standard subject slot stays compressed into one fixed and highly recognizable name before the rare predicate arrives. The debated worship, bewilderment, and refuge background remains a narrowed resonance, because the local sense is the fixed name; it matters here by aligning the one sought in orientation with the title toward which need is directed.\",\"root_display\":\"{{ar:أ ل ه}} ({{tr:ʾ-l-h}})\",\"root_gloss_range\":\"proper-name field with debated derivational pressure around worship, bewilderment, and refuge; local grammar selects the fixed divine name while allowing directional resonance with the predicate\",\"surface_display\":\"{{ar:ٱللَّهُ}} ({{tr:allāhu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:2:solid-no-hollow-image","source_type":"word_analysis","support_id":"sup_3fd710d799eba5b6d215","text":"{\"blocking_evidence\":null,\"headline\":\"solid no-hollow image becomes metaphysical\",\"reader_payoff\":\"The reader notices that self-sufficiency is made concrete through solidity, elevation, no hollow interior, and freedom from intake dependence.\",\"reason\":\"V4 accepts the compact-solidity branch, including hard or elevated ground and solid compactness without hollowness; this supports the physical image while local predication turns it into theological description.\",\"representative_source_ids\":[\"QS-02e08f9f\",\"QS-a2e27c3c\",\"QS-47330b04\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:2:hapax-isolated-predicate","source_type":"word_analysis","support_id":"sup_427cff871706e1041d34","text":"{\"blocking_evidence\":null,\"headline\":\"single Quranic occurrence concentrates meaning\",\"reader_payoff\":\"The reader notices that this title has no second Quranic setting to redirect it, so its grammar and supplied lexical field carry unusual weight here.\",\"reason\":\"The contextual profile marks the root/form as a single occurrence with no recurring pair network, and V4 supplies lexical branches that must be evaluated through this local predicate.\",\"representative_source_ids\":[\"QI-564c3864\",\"QH-c24e5e9f\",\"MH-2055c414\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:2:variant-compression","source_type":"word_analysis","support_id":"sup_442f46dbfacf4e28327a","text":"{\"blocking_evidence\":null,\"headline\":\"expanded variants highlight immediate predication\",\"reader_payoff\":\"The reader notices how compressed the standard reading is: the title arrives immediately after the name instead of after a longer creedal expansion.\",\"reason\":\"Variant pressure is retained as contrast, while the local Hafs surface remains a single immediate predicate.\",\"representative_source_ids\":[\"QF-4e88c624\",\"QF-df792d85\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:2:definite-title-shape","source_type":"word_analysis","support_id":"sup_461893262197fc0192b6","text":"{\"blocking_evidence\":null,\"headline\":\"al-marked singular noun becomes a title\",\"reader_payoff\":\"The reader notices that definiteness and singular nominal shape make the word a bounded title, not a generic class property.\",\"reason\":\"The local form is singular, definite, nominative, and without tanwin, and the word table explicitly warns that the article marks the title rather than a mere quality.\",\"representative_source_ids\":[\"QG-c8824527\",\"QF-adc1976c\",\"QI-7d81ae2d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:2:endurance-background","source_type":"word_analysis","support_id":"sup_48455856256947a984ce","text":"{\"blocking_evidence\":null,\"headline\":\"endurance colors the title without changing its form\",\"reader_payoff\":\"The reader notices a firmness-and-endurance background, while the local form still presents inherent settled identity rather than acquired endurance.\",\"reason\":\"V4 accepts lasting endurance as a branch, but the local noun is not a reflexive becoming-hard or endurance process form.\",\"representative_source_ids\":[\"QS-dceb6307\",\"QF-da027333\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:1:proper-name-definiteness","source_type":"word_analysis","support_id":"sup_4ce2fc96e45b91297dd2","text":"{\"blocking_evidence\":null,\"headline\":\"proper name blocks a class reading\",\"reader_payoff\":\"The reader sees that the predicate is attached to the identified divine name, not to one member of a broader deity category.\",\"reason\":\"The word table distinguishes the proper divine name from the common deity noun, and contextual referent evidence keeps the form overwhelmingly tied to God as referent.\",\"representative_source_ids\":[\"QG-e040062f\",\"QS-970bf1fb\",\"QF-29b17c53\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:2:surface-noun-not-process","source_type":"word_analysis","support_id":"sup_56f7390885ea359e3ac3","text":"{\"blocking_evidence\":null,\"headline\":\"settled noun absorbs process meanings\",\"reader_payoff\":\"The reader notices that the ayah names a settled title and destination rather than narrating aiming, hardening, or becoming hard as an action.\",\"reason\":\"Related verbal and derivative fields color the noun, but the local surface is a predicate noun-title, so process branches must be kept as background pressure rather than local actions.\",\"representative_source_ids\":[\"QF-0f8a6338\",\"QF-437f5674\",\"QF-89575094\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"112:2:1:1","source_type":"qac_morpheme","support_id":"sup_624bd68b52a4949c925d","text":"{\"lemma_ar\":\"ٱللَّه\",\"morph_features\":\"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"PN\",\"qac_ref\":\"112:2:1:1\",\"qac_word_ref\":\"112:2:1\",\"root_ar\":\"ء ل ه\",\"surface_ar\":\"ٱللَّهُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"112:2:2:2","source_type":"qac_morpheme","support_id":"sup_7929d4c7ca526c6f45d7","text":"{\"lemma_ar\":\"صَّمَد\",\"morph_features\":\"STEM|POS:N|LEM:S~amad|ROOT:Smd|MS|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"112:2:2:2\",\"qac_word_ref\":\"112:2:2\",\"root_ar\":\"ص م د\",\"surface_ar\":\"صَّمَدُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:2:formal-attribute-option","source_type":"word_analysis","support_id":"sup_7c9c965565caaeb279c2","text":"{\"blocking_evidence\":null,\"headline\":\"case permits attribute, clause need selects predicate\",\"reader_payoff\":\"The reader sees why the word is not merely an epithet after the name: a formal attribute option exists, but the sentence is completed by the predicate reading.\",\"reason\":\"Definiteness and nominative case could support an attributive parse, but the attachment layer marks the predicate relation as syntactically forced.\",\"representative_source_ids\":[\"QG-49e7b74d\",\"QG-e063ce79\",\"QG-f8cf1d23\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:1:boundary-resolution-launch","source_type":"word_analysis","support_id":"sup_850a3987a3a5d3154252","text":"{\"blocking_evidence\":null,\"headline\":\"repeated name resolves and relaunches\",\"reader_payoff\":\"The reader notices that the repeated name both closes the pointing movement from 112:1 and starts a fresh predicate claim in 112:2.\",\"reason\":\"The local clause begins with the explicit name rather than a pronoun or ellipsis, so the boundary movement from 112:1 can be retained without changing the local subject-predicate parse.\",\"representative_source_ids\":[\"QG-fcd5312d\",\"QI-c2c7c677\",\"QY-463a5583\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:2:closure-and-surah-arc","source_type":"word_analysis","support_id":"sup_8a3a825a40b8805afd24","text":"{\"blocking_evidence\":null,\"headline\":\"predicate closes and bridges the surah\",\"reader_payoff\":\"The reader sees 112:2 land on the predicate-title, complete the oneness claim from 112:1, and prepare the generation negation of 112:3.\",\"reason\":\"The title is the ayah-final predicate, and the CRITICAL boundary rows give concrete same-surah links to 112:1 and 112:3 without making those links override the local parse.\",\"representative_source_ids\":[\"QT-2a9b0def\",\"QE-4f95b3fc\",\"QB-5409f989\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:1:directional-name-resonance","source_type":"word_analysis","support_id":"sup_a06bb63529f36a8c2a4c","text":"{\"blocking_evidence\":null,\"headline\":\"refuge and worship pressure meets the predicate\",\"reader_payoff\":\"The reader notices a directional fit: the name's worship, bewilderment, and refuge background faces the predicate-title that names the endpoint of need.\",\"reason\":\"The root-origin material survives as resonance, but it is narrowed because local QAC selects the fixed proper name and V4 has no guardrail rows for this root.\",\"representative_source_ids\":[\"QS-462e184c\",\"QS-ac7960c0\",\"MS-b9cb58e9\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:2","source_type":"word_analysis","support_id":"sup_ae3ad031df9e82bd1f10","text":"{\"gloss_range\":\"the definite predicate-title, locally gathering resort-in-need, self-sufficiency, solidity without hollowness, and acknowledged mastery while excluding process senses as the main local reading\",\"prose\":\"{{ar:ٱلصَّمَدُ}} ({{tr:aṣ-ṣamad}}) completes the two-word equation as a definite singular predicate-title, not a loose adjective or generic class property. Its grammar is decisive because case alone could also fit an attributive reading; the clause needs a predicate, and this word supplies it without a verb or qualifier. The title gathers several supported pressures at once: needs move toward the relied-on one as a recognized center of recourse and authority, the one named is self-sufficient in return, and the hard raised no-hollow image becomes a metaphysical statement of non-lack, indivisibility, and freedom from intake dependence. The surface noun also matters: it names the destination and settled title rather than narrating aiming, hardening, endurance, or becoming hard as a process, so firmness and endurance remain background pressures on inherent identity. Against expanded variant forms, the standard reading lets the title arrive immediately after the name, and the bare two-element equation contracts the definition from 112:1 into this predicate. Its hapax status, final position, al-plus-u reprise with {{ar:ٱللَّهُ}} ({{tr:allāhu}}), final -ad rhyme with 112:1, and doubled onset make the predicate feel sealed, while the next ayah unfolds one part of its self-sufficiency by negating generation in 112:3.\",\"root_display\":\"{{ar:ص م د}} ({{tr:ṣ-m-d}})\",\"root_gloss_range\":\"accepted root range includes intending and resorting to a relied-on one, compact solidity without hollowness, stopping, wrapping, attention to an affair, striking with a stick, and enduring; the local title activates the resort, solidity, endurance, and mastery field, not the unrelated stopper, wrapping, verge, or striking branches\",\"surface_display\":\"{{ar:ٱلصَّمَدُ}} ({{tr:aṣ-ṣamad}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:1:recognizable-name-before-rare-predicate","source_type":"word_analysis","support_id":"sup_b46945dbddc2e67a5259","text":"{\"blocking_evidence\":null,\"headline\":\"familiar subject before rare predicate\",\"reader_payoff\":\"The reader notices the asymmetry between the Quran's highly familiar divine name and the rare predicate that follows it.\",\"reason\":\"The contextual profile lists thousands of proper-name occurrences for the subject, while the paired predicate root appears once in this form.\",\"representative_source_ids\":[\"QI-5fc4ff40\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:1:formal-pairing-cadence","source_type":"word_analysis","support_id":"sup_c1384eaf3bfba1cae322","text":"{\"blocking_evidence\":null,\"headline\":\"definite nominative pair heard as one frame\",\"reader_payoff\":\"The reader hears and sees the two nouns as a matched frame, with definiteness and final nominative cadence binding subject to predicate.\",\"reason\":\"Both local nouns are definite and nominative, and the attachment parse makes that formal matching serve predication rather than loose juxtaposition.\",\"representative_source_ids\":[\"QF-3ac40393\",\"QE-adb3d5f5\",\"QP-0c771c6b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:2:predicate-title-closes-clause","source_type":"word_analysis","support_id":"sup_d095877a796dc847aaf7","text":"{\"blocking_evidence\":null,\"headline\":\"definite predicate completes the equation\",\"reader_payoff\":\"The reader notices that the title is the content of the identity claim, carried by one predicate noun without verbal mediation.\",\"reason\":\"Attachment evidence syntactically forces {{ar:ٱلصَّمَدُ}} ({{tr:aṣ-ṣamad}}) as the nominative predicate of {{ar:ٱللَّهُ}} ({{tr:allāhu}}), preserving the title rather than reducing it to a paraphrased quality.\",\"representative_source_ids\":[\"QG-a1cea8a0\",\"QS-15ce0844\",\"QT-f54e93b9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:2:resort-and-self-sufficiency","source_type":"word_analysis","support_id":"sup_d52145faa12efa8ae768","text":"{\"blocking_evidence\":null,\"headline\":\"need moves one way toward the self-sufficient\",\"reader_payoff\":\"The reader sees a one-way relation: need and intention move toward the title-bearer, while the title-bearer is not sustained by need in return.\",\"reason\":\"V4 accepts the branch of intending and resorting to the relied-on one, and local predication lets that dependence relation define the named subject.\",\"representative_source_ids\":[\"QS-023054d5\",\"QS-745d9ce5\",\"QS-8ccb45e3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:2:sound-pressure","source_type":"word_analysis","support_id":"sup_e1ccac6f9cd2b203e7d5","text":"{\"blocking_evidence\":null,\"headline\":\"compressed sound reinforces the no-hollow image\",\"reader_payoff\":\"The reader hears the doubled onset and closing consonant texture as reinforcement of compactness, while the lexical claim still comes from grammar and root evidence.\",\"reason\":\"The sound observations can reinforce the accepted solidity image, but they are narrowed because articulation alone does not establish lexical meaning.\",\"representative_source_ids\":[\"QP-2b5e3969\",\"QP-56a8e1d1\",\"QP-e2cef511\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:2:chiefly-center-of-recourse","source_type":"word_analysis","support_id":"sup_f86d32971f6b9d57eb5e","text":"{\"blocking_evidence\":null,\"headline\":\"recognized center of recourse\",\"reader_payoff\":\"The reader notices that dependence is not only abstract need but also a social-spatial movement toward a recognized center of recourse and authority.\",\"reason\":\"The accepted resort branch includes the chief or relied-on one to whom affairs and needs are directed, so mastery and recourse can survive with the predicate title.\",\"representative_source_ids\":[\"QS-93be6476\",\"QS-a209d72d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:2:2:formal-reprise-rhyme","source_type":"word_analysis","support_id":"sup_fcf8c4d28f4f368a1350","text":"{\"blocking_evidence\":null,\"headline\":\"local reprise and rhyme bind the definition\",\"reader_payoff\":\"The reader hears the predicate as formally paired with the subject and rhymically linked to 112:1, so the definition is carried by cadence as well as syntax.\",\"reason\":\"The article assimilation, final nominative cadence, and 112:1 rhyme link are compatible with the forced predicate relation and add formal reinforcement.\",\"representative_source_ids\":[\"QF-5682c18e\",\"QE-3d0b423a\",\"QP-4aed6e65\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","ayah_ref":"112:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_000882/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000047","role":"The worshipped one supplies the relational pole that the predicate identifies more precisely.","root":"ء ل ه","source_ref":"112:2","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000882","role":"Intentional resort to a relied-on one supplies the directed motion and makes that pole the endpoint for affairs and needs.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]}],"changed_reading":{"after":"Allah is presented functionally as the terminal destination of directed need and reliance.","before":"Allah bears an honorific meaning roughly 'the self-sufficient lord.'"},"confidence":"strong","focus_anchor":"The nominal predicate الصمد is attached directly to the named divine referent الله.","mechanism":"The worshipped referent and the one intentionally resorted to combine into a directed dependency structure: affairs and needs move toward this referent and terminate in reliance there rather than being passed onward.","model_id":"baseline-resort-terminal"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-resort-terminal","source_type":"hft","support_id":"sup_0bcf15b6b317decc09cb","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","ayah_ref":"112:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000047/B002","root_000882/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000047","role":"The fixed divine name holds the concrete analogy to this particular referent rather than to an unnamed solid object.","root":"ء ل ه","source_ref":"112:2","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000882","role":"Compact, non-hollow solidity supplies the image of integral support that does not depend on filling an inner lack.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]}],"changed_reading":{"after":"Their dependence terminates in one pictured as integrally full: support is not obtained by first repairing an interior deficiency.","before":"The predicate says only that others seek or depend on Allah."},"confidence":"medium","focus_anchor":"The same predicate الصمد carries a concrete image of compact solidity without hollowness.","mechanism":"A material analogy overlays the social image of a relied-on chief: dependability is pictured as compact integrity with no cavity or internal lack through which support would have to be received. The analogy concerns structure, not divine anatomy.","model_id":"baseline-compact-integrity"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-compact-integrity","source_type":"hft","support_id":"sup_d38b0b75483e693be95a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","ayah_ref":"112:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_000882/B003"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000047","role":"The worshipped referent supplies the personal pole to which the sealing image is predicated.","root":"ء ل ه","source_ref":"112:2","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000882","role":"A tight stopper supplies containment and closure, functioning as an analogy for an affair that does not leak into further dependencies.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]}],"changed_reading":{"after":"The predicate pictures the point at which recourse is sealed and the chain of referral closes.","before":"The sought destination is simply the highest point in a chain of recourse."},"confidence":"exploratory","focus_anchor":"The root ص م د in الصمد also supplies the concrete operation of tightly stopping a bottle.","mechanism":"By material analogy, the predicate does more than name a destination: it marks closure. Resort reaches one capable of containing an affair and stopping leakage or indefinite referral beyond that point.","model_id":"baseline-sealing-closure"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-sealing-closure","source_type":"hft","support_id":"sup_c4b06d7e7f5b24bb607f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","ayah_ref":"112:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_000882/B007"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000047","role":"The worshipped one supplies the recipient of dependence whose reliability is being characterized.","root":"ء ل ه","source_ref":"112:2","source_word_indices":["1"]},{"branch_id":"B007","mapped_root_id":"root_000882","role":"Lasting through cold and drought while continuing provision supplies resilient continuity as the reason reliance holds under pressure.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]}],"changed_reading":{"after":"Allah's permanence is read dynamically as support whose continuance is not exhausted by adverse or barren conditions.","before":"Allah is permanently present as an abstract invariant."},"confidence":"medium","focus_anchor":"The branch of الصمد involving continued endurance under severity remains attached to the divine predicate.","mechanism":"Dependability becomes tested continuity rather than static permanence: the branch's creature enduring cold and drought while continuing its yield makes الصمد evoke support that does not cease when conditions become scarce or severe.","model_id":"baseline-enduring-supply"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-enduring-supply","source_type":"hft","support_id":"sup_53737a18d5bd4e8a4646","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","ayah_ref":"112:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_000882/B005"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000047","role":"The worshipped referent anchors the otherwise idiomatic image as a claim about the divine relation to an affair.","root":"ء ل ه","source_ref":"112:2","source_word_indices":["1"]},{"branch_id":"B005","mapped_root_id":"root_000882","role":"Being on the verge of an affair and occupied with it supplies attentive immediacy to the endpoint of recourse.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]}],"changed_reading":{"after":"The approached one is also pictured as attentively poised over the affair for which recourse is made.","before":"The predicate names a remote superior approached by petitioners."},"confidence":"exploratory","focus_anchor":"The predicate الصمد retains a branch for being poised over an affair and occupied with it.","mechanism":"The branch changes the relied-on endpoint from remote rank into attentive proximity: an affair brought to the Samad is pictured as already under concentrated regard at its threshold.","model_id":"baseline-attentive-threshold"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-attentive-threshold","source_type":"hft","support_id":"sup_4ea991c1511a7c7096c3","trust":"legacy_unbound"}]}
</lane_packet_json>
