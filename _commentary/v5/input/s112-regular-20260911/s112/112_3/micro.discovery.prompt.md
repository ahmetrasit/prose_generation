# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **112:3**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s112-regular-20260911/s112/112_3/micro.discovery.json` and modify nothing
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
  "ayah_ref": "112:3",
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
{"analysis_context":{"analysis_id":"s112-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"112:3","host_surah":112,"lane_context_refs":[],"ordered_context_refs":["112:0","112:1","112:2","112:4","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, doğuran ana babayı ve doğurma olayını değil, bu olay sonucunda dünyaya gelen kişiyi gösterir.","branch_kind":"mixed_non_bare","branch_ref":"root_001683/B001","candidate_links":[{"candidate_id":"cand_03b5d0cb321b5265ebcb","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:2:1","qac_word_ref":"112:3:2","surface_ar":"يَلِدْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:4:1","qac_word_ref":"112:3:4","surface_ar":"يُولَدْ"}],"gloss":"ana babadan doğan kişi veya kişiler","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim, bir ana babadan doğmuş kişidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırma sayı, cinsiyet ve yaş bakımından sınırlı değildir; bir veya çok kişiyi, kız veya erkeği, küçüğü veya yetişkini gösterebilir."}}],"root_ar":"و ل د","root_id":"root_001683","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın bütün çekirdeğini karşılar; tek ve çok kişi ile kız, erkek, küçük ve yetişkin kullanımlarının hepsine açıktır.","boundary_detail":"Dal, doğuran ana babayı ve doğurma olayını değil, bu olay sonucunda dünyaya gelen kişiyi gösterir.","branch_image_ar":"مولود من نسل","concept_gloss":"ana babadan doğan kişi veya kişiler","contextual_glosses":[{"applicability":"Tek bir kişinin ana babasına göre konumunu anlatan doğal cümlelerde kullanılır; kişinin yaşını veya cinsiyetini sınırlamaz.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ana babadan doğmuş kişi olma bağını bağlam içinde eksiksiz korur."},"facet_ids":["F001","F002"],"text":"birinin çocuğu","usage_role":"general"},{"applicability":"Bir ana babadan doğan birden çok kişiden söz edilen çoğul bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğum bağını ve çoğul gönderimi ilgili bağlamda korur."},"facet_ids":["F001","F002"],"text":"çocukları","usage_role":"contextual"}],"definition":"Bir ana babadan doğan kişi; bu kişi tek ya da birden çok, kız ya da erkek, küçük ya da yetişkin olabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim, bir ana babadan doğmuş kişidir."},{"facet_id":"F002","role":"extension","statement":"Adlandırma sayı, cinsiyet ve yaş bakımından sınırlı değildir; bir veya çok kişiyi, kız veya erkeği, küçüğü veya yetişkini gösterebilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kızları ve cinsiyetten bağımsız genel kullanımı dışarıda bırakır.","preserves":"Ana babadan doğan kişi olma bağını korur."},"text":"oğul"},{"category":"confusable","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Daha büyük çocuklar ile yetişkin çocuklara uzanan yaş kapsamını kaybeder.","preserves":"Doğmuş ve küçük bir kişi olma yönünü korur."},"text":"bebek"}],"identity_rationale":"Kaynak ifadesi, ana babadan doğan çocuğu temel alır ve bu adlandırmanın tek ya da çok kişi, kız ya da erkek, küçük ya da yetişkin için kullanılabildiğini açıkça belirtir. Verilen dal çerçevesi bu kapsamı doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"birinin çocuğu; bir veya birden çok doğmuş kişi"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"çocuklar"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"doğmuş çocuk; yeni doğan"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kim olduğunu bilmiyorum"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"birbirlerinden çocuk sahibi olup çoğaldılar"}],"lexicalization_note":"Tanım, doğan kişiye ilişkin yalın çekirdeği temel alır; listedeki kalıba bağlı ve türemiş kullanımlar ayrı sözlük karşılıklarında tutulur.","neighbor_coverage_note":"Verilen bütün komşu adayları değerlendirildi; yayımlanan dört karşılaştırma doğrudan çocuk, geniş çocukluk bağı, yeni doğmuşluk ve süren soy sınırlarını en açık biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın çekirdeği doğmuş kişidir; komşu dal ise çocuk yanında karşılıklı çoğalma sürecini ve hayvanların üretim amacını da anlamın içine alır.","focus_only":"Bu dal, insan çocuğunun sayı, cinsiyet ve yaş bakımından geniş adlandırılmasını öne çıkarır.","gloss":"çocuk ve çoğalan soy","neighbor_only":"Komşu dal, birbirinden çoğalmayı ve soy üretmek için tutulan hayvanları da kapsar.","neighbor_ref":"root_001499/B001","relation_type":"near_synonym","shared_zone":"İki dal da doğan çocuk ve soyun sürmesi alanında örtüşür."},{"boundary_match":"partial","distinction":"Bu dal gerçek doğum sonucundaki kişiye dayanır; komşu dal çocukluk bağını doğum dışındaki edinme, yetiştirme ve kaynaktan gelme ilişkilerine genişletir.","focus_only":"Bu dal, doğmuş kişinin kendisini sayı, cinsiyet ve yaştan bağımsız biçimde adlandırır.","gloss":"çocuk ve çocukluk bağı","neighbor_only":"Komşu dal evlat edinmeyi, yetiştirmeyi, hizmeti ve bir kaynaktan gelme benzetmelerini de kapsar.","neighbor_ref":"root_000156/B007","relation_type":"near_synonym","shared_zone":"İki dal da oğul, kız ve çocuk olma bağında örtüşür."},{"boundary_match":"partial","distinction":"Bu dal çocukluk bağını yaş sınırlaması olmadan verir; komşu dal yeni doğmuşluk çevresinde daralır ve ayrıca yaşla sınırlı olmayan köle anlamını taşır.","focus_only":"Bu dal her yaştaki çocuğu kapsar ve kölelik konumunu anlamın parçası yapmaz.","gloss":"çocuk / yeni doğmuş çocuk veya köle","neighbor_only":"Komşu dal yakın zamanda doğmuş çocuğa ve ayrıca erkek ya da kadın köleye özgü kullanımları kapsar.","neighbor_ref":"root_001683/B004","relation_type":"near_neighbor","shared_zone":"Yakın zamanda doğmuş çocuk, iki dalın kesiştiği alandır."},{"boundary_match":"field_only","distinction":"Bu dalın çekirdeği doğmuş çocukken komşu dal kuşaklar boyunca geride kalan soyun devamına ve torunlara yönelir.","focus_only":"Bu dal doğrudan ana babadan doğan kişiyi ve genel çocuk adlandırmasını öne çıkarır.","gloss":"çocuk / ardından gelen soy","neighbor_only":"Komşu dal kişinin ardından kalan çocukları, çocuklarının çocuklarını ve süren soy çizgisini kapsar.","neighbor_ref":"root_001033/B004","relation_type":"same_field","shared_zone":"Her iki dal da çocuk ve soy bağı alanındadır."}],"source_phrase_ar":"أصل صحيح وهو دليل النجل والنسل؛ الولد وهو للواحد والجميع (maqayis)؛ الولد قد يكون واحدا وجمعا؛ الوليد الصبي (sihah)؛ الولد اسم يجمع الواحد والكثير والذكر والأنثى؛ الوليد الصبي حين يولد (tahdhib)؛ الولد المولود؛ الابن والابنة؛ جمع الولد أولاد (mufradat)","source_summary":"Kaynakların ortak çekirdeği, ana babadan doğan kişidir. Kullanımın tekillik, çoğulluk, cinsiyet ve yaş sınırlarını aşabildiği de aynı toplu kanıtta belirtilir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الولد والمولود والابن والابنة والأولاد، ويستعمل للواحد والجمع وللصغير والكبير وللذكر والأنثى بحسب نصوص المصادر.","what_is_not_ar":"لا يدخل هنا خصوص الأب أو الأم، ولا نفس فعل الولادة، ولا معنى العبد أو الأمة للوليد والوليدة إلا من جهة تسمية الصغير."},"support_links":["sup_b482b332bbbb1905260d"]},{"boundary":"Buradaki ana baba, çocuğa göre doğum bağı taşıyan iki kişidir; çocuk, bakıcı veya daha uzak büyükler bu dalın çekirdeği değildir.","branch_kind":"bare","branch_ref":"root_001683/B002","candidate_links":[{"candidate_id":"cand_03b5d0cb321b5265ebcb","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:2:1","qac_word_ref":"112:3:2","surface_ar":"يَلِدْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:4:1","qac_word_ref":"112:3:4","surface_ar":"يُولَدْ"}],"gloss":"öz ana baba","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Erkek yönündeki kişi, çocuğun öz babasıdır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kadın yönündeki kişi, çocuğun öz anasıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İki kişi birlikte çocuğun ana babası olarak adlandırılır."}}],"root_ar":"و ل د","root_id":"root_001683","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çocuğun doğum bağıyla bağlı olduğu babayı, anayı veya ikisini birlikte anlatan genel karşılıktır.","boundary_detail":"Buradaki ana baba, çocuğa göre doğum bağı taşıyan iki kişidir; çocuk, bakıcı veya daha uzak büyükler bu dalın çekirdeği değildir.","branch_image_ar":"أبوان من جهة الولادة","concept_gloss":"öz ana baba","contextual_glosses":[{"applicability":"Doğum bağının erkek tarafındaki tek kişiden söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Baba yönündeki doğum bağını ilgili tekil bağlamda tam olarak korur."},"facet_ids":["F001"],"text":"öz baba","usage_role":"contextual"},{"applicability":"Doğum bağının kadın tarafındaki tek kişiden söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ana yönündeki doğum bağını ilgili tekil bağlamda tam olarak korur."},"facet_ids":["F002"],"text":"öz ana","usage_role":"contextual"},{"applicability":"İki doğum bağı kişisinin birlikte anıldığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ana ve babayı birlikte gösteren çift kapsamını korur."},"facet_ids":["F001","F002","F003"],"text":"anası ile babası","usage_role":"general"}],"definition":"Bir çocuğun doğum bağıyla bağlı olduğu öz babası, öz anası ve bu ikisinin birlikte oluşturduğu ana baba çifti.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Erkek yönündeki kişi, çocuğun öz babasıdır."},{"facet_id":"F002","role":"core","statement":"Kadın yönündeki kişi, çocuğun öz anasıdır."},{"facet_id":"F003","role":"extension","statement":"İki kişi birlikte çocuğun ana babası olarak adlandırılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Doğum bağı bulunmayan koruyucu ve bakım veren kişileri de kapsama ekler.","collision":"Bakım görevi ile doğumdan gelen ana babalık bağını birbirine karıştırır.","fit":"broadening","loses":null,"preserves":"Çocukla ilgilenen yetişkinler çevresini çağrıştırır."},"text":"bakıcılar"}],"identity_rationale":"Kaynak ifadesi, babayı doğum bağı yönünden baba, anayı da aynı yönden ana olarak adlandırır ve ikisini birlikte bir çift halinde verir. Dal çerçevesi bu üçlü dağılımı doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"öz baba"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"öz ana"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ana baba"}],"lexicalization_note":"Tanım yalın ana, baba ve ikisini birlikte gösteren adlandırmayla sınırlıdır; başka aile veya bakım ilişkileri içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; seçilen karşılaştırmalar çocukla karşılıklı konumu, baba ve ana yönündeki genişlemeleri ve kuşak sınırını en yararlı biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Bir dal doğuran ana baba yönünü, öteki dal doğan çocuk yönünü adlandırır; aynı ilişkinin karşılıklı uçlarıdır.","focus_only":"Bu dal doğum bağının ana ve baba yönündeki kişilerini gösterir.","gloss":"ana baba / çocuk","neighbor_only":"Komşu dal aynı bağın doğan çocuk yönündeki kişisini gösterir.","neighbor_ref":"root_001683/B001","relation_type":"polarity_pair","shared_zone":"İki dal aynı doğum bağındaki karşılıklı aile konumlarını paylaşır."},{"boundary_match":"partial","distinction":"Bu dal ana ile babayı doğum bağı içinde birlikte düzenler; komşu dal baba adını doğum dışındaki neden olma ve bakım işlevlerine de genişletir.","focus_only":"Bu dal öz ana ile öz babayı birlikte kapsar ve doğum bağını temel alır.","gloss":"öz ana baba / babalık ve bakım","neighbor_only":"Komşu dal yalnız baba yönünden başlayıp var etmeye, yetiştirmeye ve koruyup beslemeye de uzanır.","neighbor_ref":"root_000007/B001","relation_type":"near_neighbor","shared_zone":"Öz baba, iki dalın doğrudan kesiştiği kişidir."},{"boundary_match":"partial","distinction":"Bu dal doğum bağındaki ana babayı gösterir; komşu dal yalnız ana yönünü ele alır ve analığı bakım ile kalıplaşmış söyleyişlere taşır.","focus_only":"Bu dal öz babayı da içerir ve ana babayı çift olarak kurar.","gloss":"öz ana baba / analık ve bakım","neighbor_only":"Komşu dal ana adını yakın ve uzak analara, ana gibi besleyip yetiştirmeye ve kalıp sözlere genişletir.","neighbor_ref":"root_000053/B001","relation_type":"near_neighbor","shared_zone":"Öz ana, iki dalın doğrudan kesiştiği kişidir."}],"source_phrase_ar":"الوالد الأب والوالدة الأم وهما الوالدان (sihah)؛ يقال لأم الرجل هذه والدة (tahdhib)؛ الأب يقال له والد والأم والدة ويقال لهما والدان (mufradat)","source_summary":"Kaynaklar babayı, anayı ve ikisini birlikte gösteren ana baba çiftini aynı doğum bağı içinde ortak biçimde tanımlar.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه الوالد بمعنى الأب، والوالدة بمعنى الأم، والوالدان للأب والأم.","what_is_not_ar":"لا يدخل هنا الولد نفسه ولا الصبي ولا المولد موضعا أو زمانا."},"support_links":["sup_b482b332bbbb1905260d"]},{"boundary":"Dal, doğmuş çocuğun kendisini değil doğurma olayını ve kaynakta açıkça verilen olaya bağlı kullanımları kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001683/B003","candidate_links":[{"candidate_id":"cand_03b5d0cb321b5265ebcb","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:2:1","qac_word_ref":"112:3:2","surface_ar":"يَلِدْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:4:1","qac_word_ref":"112:3:4","surface_ar":"يُولَدْ"}],"gloss":"çocuğu dünyaya getirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek olay, kadının çocuğunu dünyaya getirmesidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir dişinin doğum zamanının gelmesi ayrıca belirtilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hayvan bağlamında gebe koyun bu söz alanındaki özel bir nitelemeyle gösterilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir koyunun doğumunu üstlenmek veya doğumuna yardım etmek ayrıca anlatılır."}},{"facet_id":"F005","role":"example","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Bir kişinin doğduğu gün, olayın zamanını belirten kullanım örneğidir."}}],"root_ar":"و ل د","root_id":"root_001683","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın temel doğurma olayını karşılar; zaman, hayvan ve yardım kullanımları bağlama göre ayrıca açıklanır.","boundary_detail":"Dal, doğmuş çocuğun kendisini değil doğurma olayını ve kaynakta açıkça verilen olaya bağlı kullanımları kapsar.","branch_image_ar":"حدوث الولادة ووضع الحمل","concept_gloss":"çocuğu dünyaya getirme","contextual_glosses":[{"applicability":"Kadının çocuğunu dünyaya getirdiği olayın eylem olarak anlatıldığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğurma olayını eylem bağlamında eksiksiz korur."},"facet_ids":["F001"],"text":"doğurmak","usage_role":"general"},{"applicability":"Bir dişinin doğum zamanının geldiği veya çok yaklaştığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğum vaktinin gelmesi yönünü ilgili bağlamda korur."},"facet_ids":["F002"],"text":"doğumu yaklaşmak","usage_role":"contextual"},{"applicability":"Bir koyunun doğurma sürecini üstlenen kişinin eylemini açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğuran hayvana yardım eden kişinin katılımını açıkça korur."},"facet_ids":["F004"],"text":"doğumuna yardım etmek","usage_role":"explanatory"}],"definition":"Bir kadının çocuğunu bedeninden çıkararak dünyaya getirmesi. Buna bağlı kullanımlar doğum zamanının gelmesini, gebe koyunu, koyunun doğumunu üstlenmeyi ve doğulan günü de anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek olay, kadının çocuğunu dünyaya getirmesidir."},{"facet_id":"F002","role":"associated_use","statement":"Bir dişinin doğum zamanının gelmesi ayrıca belirtilir."},{"facet_id":"F003","role":"specialization","statement":"Hayvan bağlamında gebe koyun bu söz alanındaki özel bir nitelemeyle gösterilir."},{"facet_id":"F004","role":"associated_use","statement":"Bir koyunun doğumunu üstlenmek veya doğumuna yardım etmek ayrıca anlatılır."},{"facet_id":"F005","role":"example","statement":"Bir kişinin doğduğu gün, olayın zamanını belirten kullanım örneğidir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Çiftleşme ve çoğalma gibi doğurma anından önceki veya daha geniş süreçleri kapsama ekler.","collision":"Doğurma olayı ile bütün çoğalma sürecini birbirine karıştırabilir.","fit":"broadening","loses":null,"preserves":"Yeni bir canlının ortaya çıkması yönünü genel olarak korur."},"text":"üreme"}],"identity_rationale":"Kaynak ifadesi kadının çocuğunu dünyaya getirmesini çekirdek yapar; doğum zamanının gelmesi, gebe koyun, koyunun doğumunu üstlenme ve doğulan gün kullanımlarını da aynı dalda bildirir. Verilen çerçeve bu olay ile ona bağlı kullanımları ayırt etmeye elverişlidir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kadın çocuğunu dünyaya getirdi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"doğum; çocuğu dünyaya getirme"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"doğum zamanı geldi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"gebe koyun"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"koyunun doğumunu üstlendik"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"birbirlerinden çocuk sahibi olup çoğaldılar"}],"lexicalization_note":"Yalın çekirdek doğurma olayıdır; zaman, gebe koyun ve doğuma yardım bildiren kalıba bağlı kullanımlar ayrı yüzler olarak tutulur.","neighbor_coverage_note":"Bütün komşular değerlendirildi; seçilenler genel doğumun gebeliği bırakma, güç doğum, erken doğum ve doğmuş çocuktan ayrıldığı sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"İki dal doğurma olayında yaklaşır; bu dal olay çevresindeki hayvan ve yardım kullanımlarını toplarken komşu dal gebeliğin bırakılması ile özel döngü zamanlamasını öne çıkarır.","focus_only":"Bu dal genel doğurma olayının yanında doğum vaktini, gebe koyunu ve doğuma yardımı da kapsar.","gloss":"doğurma / gebeliği doğumla bırakma","neighbor_only":"Komşu dal gebeliğin doğumla bırakılmasını ve kadın döngüsünün sonuyla ilgili özel zamanlamayı da içerir.","neighbor_ref":"root_001657/B002","relation_type":"near_synonym","shared_zone":"Kadının taşıdığı çocuğu doğumla bedeninden çıkarması iki dalın ortak çekirdeğidir."},{"boundary_match":"partial","distinction":"Bu dal doğumun genel gerçekleşmesini gösterir; komşu dal aynı olayın güçlükle gerçekleşen özel durumuna daralır.","focus_only":"Bu dal doğurmanın kendisini güçlük şartı olmadan anlatır.","gloss":"doğurma / güç doğum","neighbor_only":"Komşu dal yalnız doğumun güçleşmesi durumunu ve bu güçlükle ilgili dilek söyleyişlerini anlatır.","neighbor_ref":"root_001012/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da doğum olayını ve doğuran kadını içerir."},{"boundary_match":"partial","distinction":"Bu dal zaman bakımından yansız doğurma olayıdır; komşu dal süre dolmadan gerçekleşip yavrunun yaşadığı doğumla sınırlıdır.","focus_only":"Bu dal doğumun zamanından önce olmasını şart koşmaz ve genel olayı anlatır.","gloss":"doğurma / erken doğurma","neighbor_only":"Komşu dal yavrunun süresi tamamlanmadan doğduğu ve yaşamayı sürdürdüğü özel erken doğumu anlatır.","neighbor_ref":"root_000987/B007","relation_type":"near_neighbor","shared_zone":"Her iki dalda da gebe dişi yavrusunu dünyaya getirir."},{"boundary_match":"partial","distinction":"Bu dal süreç ve olaydır; komşu dal o sürecin katılımcısı ve sonucu olan doğmuş kişidir.","focus_only":"Bu dal çocuğu dünyaya getiren olay ve bu olaya bağlı kullanımları gösterir.","gloss":"doğurma / doğan çocuk","neighbor_only":"Komşu dal olay tamamlandıktan sonra doğmuş kişinin kendisini gösterir.","neighbor_ref":"root_001683/B001","relation_type":"near_neighbor","shared_zone":"Doğum olayı ile bu olay sonucunda ortaya çıkan çocuk aynı sahneyi paylaşır."}],"source_phrase_ar":"ولدت المرأة تلد ولادا وولادة؛ أولدت حان ولادها (sihah)؛ الولادة فهو وضع الوالدة ولدها؛ شاة والد وهي الحامل؛ ولدناها أي ولينا ولادتها (tahdhib)؛ يوم ولدت؛ يوم ولد (mufradat)","source_summary":"Toplu kanıt doğurma olayını merkeze alır; doğum vaktinin gelmesini, gebe koyunu, doğuma yardım etmeyi ve kişinin doğduğu günü bu olay çevresindeki kullanımlar olarak verir.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه ولدت المرأة، والولادة بوضع الوالدة ولدها، وما قرب من وقت الولادة أو حان ولاده في أولدت، وولادة الحيوان إذا نصت المصادر عليها.","what_is_not_ar":"لا يدخل هنا مجرد الولد بعد ولادته، ولا الوالدين كعلاقة اسمية، ولا المولد إذا أريد به المكان أو الوقت."},"support_links":["sup_b482b332bbbb1905260d"]},{"boundary":"Erkek biçimin çocuk yönü yeni doğmuş çocuk yanında ergenlik öncesi oğlanı da kapsar; kadın biçimi kız çocuğu ve kadın köle için kullanılır, köle anlamı özellikle kadın biçiminde yaş şartına bağlı değildir.","branch_kind":"bare","branch_ref":"root_001683/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:2:1","qac_word_ref":"112:3:2","surface_ar":"يَلِدْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:4:1","qac_word_ref":"112:3:4","surface_ar":"يُولَدْ"}],"gloss":"yeni doğmuş çocuk veya köle","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Erkek biçimi yakın zamanda doğmuş çocuk veya ergenlik öncesi oğlan için kullanılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Erkek biçimi bir erkek köleyi de gösterebilir."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kadın biçimi kız çocuğunu gösterebilir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kadın biçimi kadın köleyi gösterir ve bu kullanım ileri yaşta da geçerli olabilir."}}],"root_ar":"و ل د","root_id":"root_001683","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Erkek ve kadın biçimlerinin çocuk ile köle yönlerini birlikte özetler; kadın kölede yaş sınırlaması bulunmadığını açıklama tamamlar.","boundary_detail":"Erkek biçimin çocuk yönü yeni doğmuş çocuk yanında ergenlik öncesi oğlanı da kapsar; kadın biçimi kız çocuğu ve kadın köle için kullanılır, köle anlamı özellikle kadın biçiminde yaş şartına bağlı değildir.","branch_image_ar":"صغير قريب العهد بالولادة أو مملوك","concept_gloss":"yeni doğmuş çocuk veya köle","contextual_glosses":[{"applicability":"Erkek biçimin yakın zamanda doğmuş çocuk anlamıyla kullanıldığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Erkek çocuk ve yakın zamanda doğmuşluk özelliklerini birlikte korur."},"facet_ids":["F001"],"text":"yeni doğmuş erkek çocuk","usage_role":"contextual"},{"applicability":"Kadın biçimin köle anlamında, yaştan bağımsız kullanıldığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadın oluşu, kölelik konumunu ve yaş bağımsızlığını korur."},"facet_ids":["F004"],"text":"kadın köle","usage_role":"contextual"}],"definition":"Erkek biçimde yakın zamanda doğmuş çocuk veya ergenlik öncesi oğlan; kadın biçimde kız çocuk; ayrıca erkek ya da kadın köle. Kadın köle anlamı kişinin ileri yaşta olmasına karşın sürebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Erkek biçimi yakın zamanda doğmuş çocuk veya ergenlik öncesi oğlan için kullanılır."},{"facet_id":"F002","role":"extension","statement":"Erkek biçimi bir erkek köleyi de gösterebilir."},{"facet_id":"F003","role":"core","statement":"Kadın biçimi kız çocuğunu gösterebilir."},{"facet_id":"F004","role":"extension","statement":"Kadın biçimi kadın köleyi gösterir ve bu kullanım ileri yaşta da geçerli olabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Erkek ve kadın köle anlamlarını, ayrıca yaştan bağımsız kadın köle kullanımını kaybeder.","preserves":"Yakın zamanda doğmuş küçük çocuk yönünü korur."},"text":"bebek"},{"category":"confusable","error_profile":{"adds":"Özgür ve ücretli çalışanları da kapsama sokabilir.","collision":"Hizmet görevi ile kişinin kölelik konumunu birbirine karıştırır.","fit":"displacement","loses":"Yeni doğmuş çocuk anlamını ve kölelik konumunun açık sınırını kaybeder.","preserves":"Bir başkasına hizmet eden kişi çağrışımını kısmen korur."},"text":"hizmetçi"}],"identity_rationale":"Kaynak ifadesi erkek biçimi için yeni doğmuş çocuk, ergenlik öncesi oğlan ve erkek köleyi; kadın biçimi için kız çocuk ile kadın köleyi birlikte verir. Dal çerçevesindeki çocuk ve köle yönleri uygundur, ancak çocuk yönü yalnız yeni doğmuşlukla sınırlandırılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yeni doğmuş erkek çocuk; erkek köle"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kız çocuk; kadın köle"}],"lexicalization_note":"Tanım, yalın biçimlerin çocuk ve köle yönlerini birlikte korur; genel çocuk anlamı veya herhangi bir hizmetçilik ilişkisi içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler kadın köle, küçük yavru, gençlik adıyla köle ve genel çocuk sınırlarını açıkça karşılaştırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal çocuk ve köle yönlerini cinsiyet biçimleriyle birlikte taşır; komşu dal bu çoklu yapıdan yalnız kadın köle anlamını ayırır.","focus_only":"Bu dal erkek çocuk, özellikle yeni doğmuş çocuk veya ergenlik öncesi oğlan, kız çocuk ve erkek köleyi de kapsar.","gloss":"çocuk veya köle / kadın köle","neighbor_only":"Komşu dal yalnız kadın köle anlamına odaklanır.","neighbor_ref":"root_000053/B014","relation_type":"near_neighbor","shared_zone":"Kadın köle anlamı iki dalın doğrudan kesişimidir."},{"boundary_match":"partial","distinction":"Bu dal köle anlamına uzanır ve insan kullanımlarında kalır; komşu dal köleliği içermez, küçük olmayı hayvan yavrularına kadar genişletir.","focus_only":"Bu dal insan çocuğunun yanında erkek veya kadın köle anlamını da taşır.","gloss":"çocuk veya köle / küçük yavru","neighbor_only":"Komşu dal küçük insan çocuğuyla birlikte evcil ve yabani hayvan yavrularını da kapsar.","neighbor_ref":"root_000942/B001","relation_type":"near_neighbor","shared_zone":"Küçük insan çocuğu iki dalın kesiştiği alandır; bu dal erkek biçimde yeni doğmuş veya ergenlik öncesi oğlanı, kadın biçimde kız çocuğunu kapsar."},{"boundary_match":"partial","distinction":"Bu dalın çocuk yönü erkek biçimde yeni doğmuş veya ergenlik öncesi oğlanı, kadın biçimde kız çocuğunu kapsar; komşu dal genç kişi adlarını köle ve hizmetçi için örtülü bir söyleyiş olarak kullanır.","focus_only":"Bu dal erkek çocuk, özellikle yeni doğmuş veya ergenlik öncesi oğlan, ve kız çocuk anlamını taşır; köle kullanımını da bu adlandırma alanıyla birlikte verir.","gloss":"çocuk veya köle / genç diye anılan köle","neighbor_only":"Komşu dal genç erkek ve kız adlarını köle veya hizmetçi için örtülü biçimde kullanır.","neighbor_ref":"root_001130/B002","relation_type":"near_neighbor","shared_zone":"Erkek ve kadın kölenin yaş bildiren bir adla gösterilmesi iki dalı yaklaştırır."},{"boundary_match":"partial","distinction":"Bu dal biçime bağlı çocuk kapsamıyla köle anlamını birleştirir; komşu dal köleliği dışarıda bırakıp çocukluk bağını yaş ve sayı bakımından geniş tutar.","focus_only":"Bu dal erkek biçimde yeni doğmuş veya ergenlik öncesi oğlanı, kadın biçimde kız çocuğunu kapsar ve ayrıca köle anlamı taşır.","gloss":"çocuk veya köle / genel çocuk","neighbor_only":"Komşu dal çocuğu her yaşta, her cinsiyette ve tek ya da çok kişi olarak kapsar.","neighbor_ref":"root_001683/B001","relation_type":"near_neighbor","shared_zone":"İnsan çocuğu iki dalda da yer alır; bu dal erkek biçimde yeni doğmuş veya ergenlik öncesi oğlanı, kadın biçimde kız çocuğunu gösterir."}],"source_phrase_ar":"الوليدة الأنثى والجمع ولائد (maqayis)؛ الوليد الصبي والعبد والجمع ولدان وولدة؛ الوليد الصبية والأمة والجمع الولائد (sihah)؛ الوليد الصبي حين يولد؛ يقال للأمة وليدة وإن كانت مسنة (tahdhib)؛ الوليد يقال لمن قرب عهده بالولادة؛ الوليدة مختصة بالإماء في عامة كلامهم (mufradat)","source_summary":"Toplu kanıt erkek biçimi yeni doğmuş çocuk, ergenlik öncesi oğlan ve erkek köleye; kadın biçimi kız çocuk ile kadın köleye dağıtır. Kadın köle adlandırmasının ileri yaşta da kullanılabildiği ayrıca belirtilir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الوليد للصبي أو الغلام القريب العهد بالولادة، والوليدة للصبية أو الأمة، وما جمعه ولدان أو ولائد بحسب النص.","what_is_not_ar":"لا يدخل هنا الولد العام للصغير والكبير، ولا التليدة أو المولدة إلا إذا دل السياق على الجارية أو العبد المولود في الملك."},"support_links":[]},{"boundary":"Dal gerçek doğurma olayını değil nedene bağlı ortaya çıkmayı, sonradan oluşturulmayı, uydurulmayı ve katışıksız sayılmamayı anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001683/B005","candidate_links":[{"candidate_id":"cand_3f7c4ee040f717a5ed78","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:2:1","qac_word_ref":"112:3:2","surface_ar":"يَلِدْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:4:1","qac_word_ref":"112:3:4","surface_ar":"يُولَدْ"}],"gloss":"bir şeyden nedenle türeme veya sonradan oluşturulma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli söz biriminde bir şey, başka bir şeyden bir neden aracılığıyla ortaya çıkar."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sonradan oluşturulan söz bu ortaya çıkma düşüncesinin bir uzantısıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Uydurulmuş kitap ve doğrulanmamış, üretilmiş kanıt aynı niteleme alanındadır."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Katışıksız sayılmayan dil veya kişi için de bu niteleme kullanılır."}}],"root_ar":"و ل د","root_id":"root_001683","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nedene bağlı ortaya çıkma çekirdeğiyle sonradan oluşturulmuş, uydurulmuş ve katışıksız olmayan uzantıları birlikte temsil eder.","boundary_detail":"Dal gerçek doğurma olayını değil nedene bağlı ortaya çıkmayı, sonradan oluşturulmayı, uydurulmayı ve katışıksız sayılmamayı anlatır.","branch_image_ar":"شيء حاصل عن شيء أو مستحدث منه","concept_gloss":"bir şeyden nedenle türeme veya sonradan oluşturulma","contextual_glosses":[{"applicability":"Bir sonucun başka bir şeyden belirli bir nedenle çıktığı süreçlerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kaynak, neden ve ortaya çıkan sonuç arasındaki bağı korur."},"facet_ids":["F001"],"text":"bir şeyden ortaya çıkmak","usage_role":"general"},{"applicability":"Daha önce bulunmayıp sonradan üretilen bir söz veya benzeri oluşum için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sonradan ortaya çıkarılmış olma özelliğini korur."},"facet_ids":["F002"],"text":"sonradan oluşturulmuş","usage_role":"contextual"},{"applicability":"Gerçekliği bulunmayan veya doğrulanmamış kitap ve kanıt gibi örneklerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gerçek olmayıp sonradan üretilmiş olma yönünü korur."},"facet_ids":["F003"],"text":"uydurulmuş","usage_role":"contextual"}],"definition":"Belirli söz biriminde bir şeyin başka bir şeyden bir neden aracılığıyla ortaya çıkması. Buna bağlı olarak sonradan oluşturulan söz, uydurulan kitap veya kanıt ve katışıksız sayılmayan dil ya da kişi de kendi biçim ve kalıplarında nitelenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli söz biriminde bir şey, başka bir şeyden bir neden aracılığıyla ortaya çıkar."},{"facet_id":"F002","role":"extension","statement":"Sonradan oluşturulan söz bu ortaya çıkma düşüncesinin bir uzantısıdır."},{"facet_id":"F003","role":"extension","statement":"Uydurulmuş kitap ve doğrulanmamış, üretilmiş kanıt aynı niteleme alanındadır."},{"facet_id":"F004","role":"specialization","statement":"Katışıksız sayılmayan dil veya kişi için de bu niteleme kullanılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ortaya çıkışın neden bağını, sürecini ve sonradan oluşturulmuş ya da uydurulmuş nitelemelerini kaybeder.","preserves":"Başka bir şeyden ortaya çıkan son ürünü gösterir."},"text":"sonuç"},{"category":"confusable","error_profile":{"adds":"Başka bir kaynaktan türemeyen ve örneksiz başlayan oluşturma türlerini de kapsama ekler.","collision":"Bir kaynaktan nedenle türeme ile kaynaksız başlatmayı karıştırabilir.","fit":"broadening","loses":null,"preserves":"Daha önce bulunmayan bir şeyin ortaya çıkması yönünü korur."},"text":"yaratma"}],"identity_rationale":"Kaynak ifadesi bir şeyin başka bir şeyden bir nedenle ortaya çıkmasını çekirdek yapar; sonradan oluşturulmuş söz, uydurulmuş kitap veya kanıt ve katışıksız sayılmayan dil ya da kişi kullanımlarını buna bağlar. Verilen dal bu çekirdek ile uzantıları doğru biçimde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir şeyin başka bir şeyden bir nedenle ortaya çıkması"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"sonradan oluşturulmuş, uydurulmuş veya katışıksız olmayan"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"katışıksız sayılmayan dil veya kişi"}],"lexicalization_note":"Nedene bağlı ortaya çıkma yalnız ilgili söz biriminde çekirdektir; sonradan oluşturulmuş, uydurulmuş ve katışıksız olmayan anlamlar kendi biçim ve kalıplarıyla ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen dört komşu uydurma, örneksiz başlatma, yararlı sonuç ve genel var etme karşısındaki sınırları açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın çekirdeği başka bir şeyden nedenle ortaya çıkmadır ve uydurma yalnız bir uzantıdır; komşu dal gerçeğe aykırı ürün kurmayı doğrudan merkezine alır.","focus_only":"Bu dal uydurma yanında nedene bağlı ortaya çıkmayı, sonradan oluşturulmayı ve katışıksız olmamayı kapsar.","gloss":"türeme veya sonradan üretme / düzmece kurma","neighbor_only":"Komşu dal yalan, düzmece anlatı, şiir ve ezgi gibi gerçeğe aykırı biçimde kurulmuş ürünlere yoğunlaşır.","neighbor_ref":"root_001167/B004","relation_type":"near_neighbor","shared_zone":"Uydurulmuş bir söz ya da metin iki dalın kesiştiği alandır."},{"boundary_match":"partial","distinction":"Bu dalda ortaya çıkan şeyin bir kaynağı ve nedeni vardır; komşu dalda yenilik, önceki bir örnek bulunmamasına dayanır.","focus_only":"Bu dal başka bir şeyden neden yoluyla çıkmayı ve türetilmiş olmayı temel alır.","gloss":"türeme / örneksiz başlatma","neighbor_only":"Komşu dal önceden örneği bulunmayan bir şeyi ilk kez başlatmayı veya yapmayı temel alır.","neighbor_ref":"root_000094/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da yeni bir şeyin ortaya çıkması alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dal çıkış ilişkisini ve sonradan üretilmişliği anlatır; komşu dal çıkan şeyin yararlı bir ürün veya kazanç olmasını öne çıkarır.","focus_only":"Bu dal bir şeyin başka bir şeyden çıkma sürecini ve sonradan oluşturulmuş ürünleri kapsar.","gloss":"türeme / yararlı ürün","neighbor_only":"Komşu dal ortaya çıkan yararlı sonucu ve bir şeyin verdiği ürünü öne çıkarır.","neighbor_ref":"root_000205/B003","relation_type":"near_neighbor","shared_zone":"Bir kaynaktan çıkan sonuç düşüncesi iki dalı birbirine yaklaştırır."},{"boundary_match":"partial","distinction":"Bu dal kaynak ile sonuç arasındaki türeme bağını gerektirir; komşu dal bu bağı şart koşmadan genel var etme ve başlatmayı anlatır.","focus_only":"Bu dal başka bir kaynaktan neden aracılığıyla türemeyi şart koşar ve uydurma uzantıları taşır.","gloss":"türeme / var etme","neighbor_only":"Komşu dal bir şeyi var etmeyi, başlatmayı, bulmayı ve yapıtını ortaya koymayı genel olarak kapsar.","neighbor_ref":"root_001165/B002","relation_type":"near_neighbor","shared_zone":"Yeni bir varlık veya ürünün ortaya çıkması iki dalın ortak alanıdır."}],"source_phrase_ar":"تولد الشيء عن الشيء حصل عنه (maqayis)؛ عربية مولدة ورجل مولد إذا كان عربيا غير محض (sihah)؛ المولد من الكلام مولدا إذا استحدثوه؛ كتاب مولد أي مفتعل؛ بينة مولدة وليست بمحققة (tahdhib)؛ تولد الشيء من الشيء حصوله عنه بسبب من الأسباب (mufradat)","source_summary":"Kaynakların toplu anlatımı nedene bağlı türemeyi merkeze alır; sonradan oluşturulmuş söz, uydurulmuş metin veya kanıt ve katışıksız sayılmayan dil ya da kişi bu çekirdeğin yerleşmiş uzantılarıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه تولد الشيء من الشيء إذا حصل عنه بسبب، والمولد من الكلام إذا استحدث، وما كان غير محض أو ناشئا في بيئة معينة مثل عربية مولدة ورجل مولد.","what_is_not_ar":"لا يدخل هنا النسل الآدمي المباشر إلا من جهة القياس العام، ولا الولادة الحسية نفسها."},"support_links":["sup_b23751a6a40c49f22149"]},{"boundary":"Dal genel benzerlik veya arkadaşlık değil, özellikle aynı yaşta olma bakımından denk kişiyi gösterir.","branch_kind":"bare","branch_ref":"root_001683/B006","candidate_links":[{"candidate_id":"cand_2356b7a7d80dcdad6d04","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:2:1","qac_word_ref":"112:3:2","surface_ar":"يَلِدْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:4:1","qac_word_ref":"112:3:4","surface_ar":"يُولَدْ"}],"gloss":"yaşıt","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki kişi arasındaki belirleyici bağ aynı yaşta olmalarıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adın tekil, ikili ve çoğul biçimleri bir veya birden çok yaştaşı gösterebilir."}}],"root_ar":"و ل د","root_id":"root_001683","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiyle aynı yaşta olan kimseyi, başka benzerlik veya arkadaşlık şartı eklemeden karşılar.","boundary_detail":"Dal genel benzerlik veya arkadaşlık değil, özellikle aynı yaşta olma bakımından denk kişiyi gösterir.","branch_image_ar":"قرين في سن الولادة","concept_gloss":"yaşıt","contextual_glosses":[{"applicability":"Yaştaşlık ilişkisinin bir cümle içinde açıkça çözülmesi gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılaştırılan iki kişinin yaş eşitliğini açıkça korur."},"facet_ids":["F001"],"text":"onunla aynı yaşta","usage_role":"explanatory"}],"definition":"Başka bir kişiyle aynı yaşta olan kimse; yaş bakımından onun dengi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki kişi arasındaki belirleyici bağ aynı yaşta olmalarıdır."},{"facet_id":"F002","role":"source_variant","statement":"Adın tekil, ikili ve çoğul biçimleri bir veya birden çok yaştaşı gösterebilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yaş eşitliği gerektirmeyen kişisel yakınlık ve birlikte bulunma ilişkisini ekler.","collision":"Yaştaşlık ile kişisel dostluğu birbirine karıştırır.","fit":"displacement","loses":"Aynı yaşta olma şartını bütünüyle kaybeder.","preserves":"İki kişi arasında yakın bir bağ bulunduğu çağrışımını korur."},"text":"arkadaş"}],"identity_rationale":"Kaynak ifadesi bir kişiyi başka bir kişinin yaştaşı ve dengi olarak tanımlar; biçimin kökenine ve çoğul kullanımına ilişkin bilgiler de bu çekirdeği değiştirmez. Verilen dal çerçevesi yaş eşitliğini doğru biçimde merkeze alır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yaşıt; aynı yaşta olan kimse"}],"lexicalization_note":"Tanım yalın yaştaş anlamıyla sınırlıdır; güç, tür, arkadaşlık veya genel benzerlik gibi ek ölçütler içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; yayımlanan üç komşu yaş eşitliğine arkadaşlık, güç denkliği veya genel benzerlik ekleyen sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yaş eşitliğini tek belirleyici sınır yapar; komşu dal aynı yaş çevresine arkadaşlık veya birlikte yetişme bağını da katabilir.","focus_only":"Bu dal için aynı yaşta olmak yeterlidir; birlikte büyüme veya arkadaşlık şart değildir.","gloss":"yaşıt / yaşıt ve birlikte büyüyen","neighbor_only":"Komşu dal yaş eşitliğinin yanında arkadaşlığı, yakınlığı ve birlikte büyümeyi de çağrıştırabilir.","neighbor_ref":"root_000178/B004","relation_type":"near_synonym","shared_zone":"Aynı yaşta olan iki kişi iki dalın ortak çekirdeğidir."},{"boundary_match":"partial","distinction":"Bu dal aynı yaş koşulundan ayrılmaz; komşu dal denkliği güç ve yiğitlik gibi başka karşılaştırma ölçülerine genişletir.","focus_only":"Bu dal denkliği yalnız yaş ölçüsüne göre kurar.","gloss":"yaşıt / yaşta veya güçte denk","neighbor_only":"Komşu dal yaş yanında yiğitlik, güç ve dayanıklılık bakımından denk rakibi de kapsar.","neighbor_ref":"root_001221/B003","relation_type":"near_neighbor","shared_zone":"Yaş bakımından denk kişi iki dalın kesiştiği alandır."},{"boundary_match":"partial","distinction":"Bu dal denklik ölçüsünü yaş olarak sabitler; komşu dal benzerlik ve denkliği belirli bir ölçüyle sınırlamaz.","focus_only":"Bu dal benzerliği yalnız iki kişinin aynı yaşta olmasına bağlar.","gloss":"yaşıt / genel benzer","neighbor_only":"Komşu dal yaş şartı olmadan tür, durum veya başka özelliklerde benzer ve denk olanı gösterir.","neighbor_ref":"root_000906/B008","relation_type":"near_neighbor","shared_zone":"Bir kişinin başka bir kişiye denk sayılması iki dalı yakınlaştırır."}],"source_phrase_ar":"اللدة نقصانه الواو لأن أصله ولدة (maqayis)؛ لدة الرجل تربه؛ وهما لدان والجمع لدات ولدون (sihah)؛ اللدة مختصة بالترب يقال فلان لدة فلان وتربه (mufradat)","source_summary":"Kaynakların ortak çekirdeği aynı yaşta olan denk kişidir; tekil, ikili ve çoğul biçim bilgileri bu yaştaşlık ilişkisini sayı bakımından çeşitlendirir.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه اللدة أو لدة الرجل بمعنى تربه ومثيله في السن.","what_is_not_ar":"لا يدخل هنا الولد بمعنى الابن ولا الوالد ولا التولد."},"support_links":["sup_7059ac681109a5d863d1"]},{"boundary":"Anlam yalnız verilen kalıp sözde geçerlidir; tek başına çocuk adını veya bu kalıp dışında kalan her büyüklük ve bolluk durumunu kapsamaz.","branch_kind":"collocation","branch_ref":"root_001683/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:2:1","qac_word_ref":"112:3:2","surface_ar":"يَلِدْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:4:1","qac_word_ref":"112:3:4","surface_ar":"يُولَدْ"}],"gloss":"çok büyük bir durum ya da pek bol bir şey","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kalıp söz çok büyük, önemli veya ağır bir durumu anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı kalıp söz çok bol bir şeyi anlatmak için de kullanılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Söyleyişin çıkışı, baskın sırasında yaşanan ağır duruma bağlanır."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Çok yiyecek ve çok otlak, bolluk yönünün açık örnekleridir."}}],"root_ar":"و ل د","root_id":"root_001683","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kanıtta verilen sabit söyleyişin anlamını karşılar; yalın bir sözcük anlamı olarak kullanılamaz.","boundary_detail":"Anlam yalnız verilen kalıp sözde geçerlidir; tek başına çocuk adını veya bu kalıp dışında kalan her büyüklük ve bolluk durumunu kapsamaz.","branch_image_ar":"أمر لا ينادى وليده","concept_gloss":"çok büyük bir durum ya da pek bol bir şey","contextual_glosses":[{"applicability":"Kalıp söz büyük, önemli ve ağır bir olay veya durum için söylendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Durumun olağanüstü büyüklük ve ağırlık derecesini korur."},"facet_ids":["F001","F003"],"text":"çok ağır bir durum","usage_role":"contextual"},{"applicability":"Kalıp söz yiyecek veya otlak gibi bir şeyin çokluğunu anlatırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir şeyin olağanüstü bolluk derecesini ilgili bağlamda korur."},"facet_ids":["F002","F004"],"text":"pek bol","usage_role":"contextual"}],"definition":"Yalnız belirli bir kalıp söz içinde, çok büyük veya ağır bir durumu ya da çok bol bir şeyi anlatır. Söyleyişin kökeni baskına bağlanır; çok yiyecek ve çok otlak bolluk örnekleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kalıp söz çok büyük, önemli veya ağır bir durumu anlatır."},{"facet_id":"F002","role":"extension","statement":"Aynı kalıp söz çok bol bir şeyi anlatmak için de kullanılır."},{"facet_id":"F003","role":"source_variant","statement":"Söyleyişin çıkışı, baskın sırasında yaşanan ağır duruma bağlanır."},{"facet_id":"F004","role":"example","statement":"Çok yiyecek ve çok otlak, bolluk yönünün açık örnekleridir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Gerçek bir çocuğun çağrılmadığı sıradan bir olayı anlamın içine ekler.","collision":"Sabit söyleyişin yerleşmiş anlamını sözcüğü sözcüğüne bir olayla karıştırır.","fit":"displacement","loses":"Çok büyük veya ağır durum ile çok bol şey bildiren yerleşmiş anlamı kaybeder.","preserves":"Kalıbın sözcük düzeyindeki çağırma ve çocuk görüntüsünü korur."},"text":"çocuk çağrılmaz"}],"identity_rationale":"Kaynak ifadesi yalnız sabit bir söyleyiş içinde çok büyük veya ağır bir durumu ve çok bol bir şeyi anlatır; kökeni baskına bağlar, yiyecek ve otlağı bolluk örnekleri olarak verir. Ön çerçevedeki süt örneği yetkili kaynak ifadesinde bulunmadığından tanım bu örneği dışarıda bırakacak biçimde yeniden kurulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"çok büyük veya ağır bir durum yahut çok bol bir şey için söylenen kalıp söz"}],"lexicalization_note":"Tanım yalnız verilen sabit söyleyişe bağlıdır; buradaki büyüklük, ağırlık ve bolluk anlamları yalın kök anlamına genellenmez.","neighbor_coverage_note":"Verilen bütün komşu adayları değerlendirildi; hiçbiri bu sabit söyleyişin büyük olay ve bolluk sınırını doğrudan paylaşmadığından yayımlanacak yararlı bir karşılaştırma bulunmadı.","source_phrase_ar":"أمر لا ينادى وليده؛ قيل ذلك لكل أمر عظيم ولكل شيء كثير (sihah)؛ هو أمر لا ينادى وليده؛ أمر جليل شديد؛ أصله في الغارة؛ طعام لا ينادى وليده؛ عشب لا ينادى وليده (tahdhib)","source_summary":"Toplu kanıt, sabit söyleyişi büyük veya ağır durum ile bolluk arasında açıklar; çıkışını baskına bağlar ve yiyecek ile otlağı bolluk örnekleri olarak verir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه المثل لا ينادى وليده وما فسرته المصادر من أمر عظيم أو شديد، أو شيء كثير، أو غارة تذهل الأم عن ولدها، أو طعام ولبن وعشب كثير لا يحتاج فيه إلى نداء الوليد.","what_is_not_ar":"لا يدخل هنا معنى الوليد المفرد خارج هذا التركيب، ولا كل شدة أو كثرة بلا هذا المثل."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["112:3:1"],"branch_refs":[],"candidate_id":"cand_67c8caffbb99818d5907","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:3:1:jussive-categorical-negation","source_type":"word_analysis","support_ids":["sup_3a9f56a1a31a2dc34369","sup_45d6a3fca36250705495"],"title":"categorical jussive negation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:1","qac_refs":["112:3:1:1"],"status":"accepted"}},{"anchor_refs":["112:3:1"],"branch_refs":[],"candidate_id":"cand_029370f6bc309c841f48","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:3:1:opening-discourse-continuity","source_type":"word_analysis","support_ids":["sup_45d6a3fca36250705495","sup_bbba8a17fce379e97b6c"],"title":"verbal denial opens without a restated subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:1","qac_refs":["112:3:1:1"],"status":"accepted"}},{"anchor_refs":["112:3:1"],"branch_refs":[],"candidate_id":"cand_0ea7a3530d0430220c33","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:3:1:twin-negation-cadence","source_type":"word_analysis","support_ids":["sup_268cc3e6a6503bb45cac","sup_45d6a3fca36250705495"],"title":"first beat of the paired negation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:1","qac_refs":["112:3:1:1"],"status":"accepted"}},{"anchor_refs":["112:3:2"],"branch_refs":[],"candidate_id":"cand_f6e33eb84c7a6402a8d0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001683"],"scope":"focus_ayah","source_local_id":"112:3:2:absolute-active-denial","source_type":"word_analysis","support_ids":["sup_488044474e87872da409","sup_4bd9eabfdd826a350576"],"title":"objectless active begetting denied absolutely","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:2","qac_refs":["112:3:2:1"],"status":"accepted"}},{"anchor_refs":["112:3:2"],"branch_refs":[],"candidate_id":"cand_338ff2fc388bcbcaf8a1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001683"],"scope":"focus_ayah","source_local_id":"112:3:2:first-half-of-mirror","source_type":"word_analysis","support_ids":["sup_4bd9eabfdd826a350576","sup_e6d503612ce66f05f981"],"title":"active side of the two-clause mirror","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:2","qac_refs":["112:3:2:1"],"status":"accepted"}},{"anchor_refs":["112:3:2"],"branch_refs":[],"candidate_id":"cand_700164e3c582f5e66da1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001683"],"scope":"focus_ayah","source_local_id":"112:3:2:implicit-subject-continuity","source_type":"word_analysis","support_ids":["sup_4bd9eabfdd826a350576","sup_55bc68c703373f9b0452"],"title":"hidden subject carries the same referent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:2","qac_refs":["112:3:2:1"],"status":"accepted"}},{"anchor_refs":["112:3:2"],"branch_refs":[],"candidate_id":"cand_87419819e579228425c8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001683"],"scope":"focus_ayah","source_local_id":"112:3:2:jussive-form-and-direct-agency","source_type":"word_analysis","support_ids":["sup_4bd9eabfdd826a350576","sup_8d78e373b2200b274cf7"],"title":"active jussive form keeps direct agency visible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:2","qac_refs":["112:3:2:1"],"status":"accepted"}},{"anchor_refs":["112:3:2"],"branch_refs":[],"candidate_id":"cand_560c262f27dbd1b3e670","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001683"],"scope":"focus_ayah","source_local_id":"112:3:2:root-field-narrowed-to-generation","source_type":"word_analysis","support_ids":["sup_4bd9eabfdd826a350576","sup_5b898ca869f2790442f0"],"title":"birth-root pressure narrowed to active generation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:2","qac_refs":["112:3:2:1"],"status":"accepted"}},{"anchor_refs":["112:3:2"],"branch_refs":[],"candidate_id":"cand_7929bcdbaf1edde536a4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001683"],"scope":"focus_ayah","source_local_id":"112:3:2:sound-reprise-with-role-reversal","source_type":"word_analysis","support_ids":["sup_017baf59920aa0d5b1a2","sup_4bd9eabfdd826a350576"],"title":"similar sound with opposite grammatical role","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:2","qac_refs":["112:3:2:1"],"status":"accepted"}},{"anchor_refs":["112:3:2"],"branch_refs":[],"candidate_id":"cand_f3d27ed06b389b620232","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001683"],"scope":"focus_ayah","source_local_id":"112:3:2:sparse-verbal-slot","source_type":"word_analysis","support_ids":["sup_4bd9eabfdd826a350576","sup_e60bbb3dd45af74ec36f"],"title":"active imperfect stands out in the root distribution","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:2","qac_refs":["112:3:2:1"],"status":"accepted"}},{"anchor_refs":["112:3:3"],"branch_refs":[],"candidate_id":"cand_7336e3a38e79df9d9c2a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:3:3:active-passive-completion","source_type":"word_analysis","support_ids":["sup_4e9a9fec95630ee79782","sup_7f2adc5ab4cf7e6370dc"],"title":"hinge from sourcehood to originatedness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:3","qac_refs":["112:3:3:1"],"status":"accepted"}},{"anchor_refs":["112:3:3"],"branch_refs":[],"candidate_id":"cand_56bb82d8d18be1508d93","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:3:3:separate-scope-coordination","source_type":"word_analysis","support_ids":["sup_5f20642af7667a7633ae","sup_7f2adc5ab4cf7e6370dc"],"title":"coordination without collapsed scope","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:3","qac_refs":["112:3:3:1"],"status":"accepted"}},{"anchor_refs":["112:3:3"],"branch_refs":[],"candidate_id":"cand_f4180a1979052498885d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:3:3:wa-lam-formal-cluster","source_type":"word_analysis","support_ids":["sup_7f2adc5ab4cf7e6370dc","sup_ecbb36e2d2fd6275a765"],"title":"clustered connector and renewed negator","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:3","qac_refs":["112:3:3:1"],"status":"accepted"}},{"anchor_refs":["112:3:4"],"branch_refs":[],"candidate_id":"cand_4b5686f9c43f0fd51a93","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:3:4:compressed-two-direction-frame","source_type":"word_analysis","support_ids":["sup_1896140564aa1d2c410f","sup_65029fbb7ab28882f428"],"title":"four-word compression of both directions","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:4","qac_refs":["112:3:3:2"],"status":"accepted"}},{"anchor_refs":["112:3:4"],"branch_refs":[],"candidate_id":"cand_cef7907e5e60c4073ae5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:3:4:independent-passive-scope","source_type":"word_analysis","support_ids":["sup_65029fbb7ab28882f428","sup_772329d21039e5ef4d66"],"title":"passive denial receives its own negator","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:4","qac_refs":["112:3:3:2"],"status":"accepted"}},{"anchor_refs":["112:3:4"],"branch_refs":[],"candidate_id":"cand_64f29d2bd801a1bcf4d8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:3:4:next-ayah-particle-continuity","source_type":"word_analysis","support_ids":["sup_32689b91bd63d327ae16","sup_65029fbb7ab28882f428"],"title":"negative particle architecture continues in 112:4","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:4","qac_refs":["112:3:3:2"],"status":"accepted"}},{"anchor_refs":["112:3:4"],"branch_refs":[],"candidate_id":"cand_4fe2d20e27f0627d6f9b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:3:4:separable-particle-in-cluster","source_type":"word_analysis","support_ids":["sup_65029fbb7ab28882f428","sup_93da330481556f942d05"],"title":"negator remains distinct inside the cluster","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:4","qac_refs":["112:3:3:2"],"status":"accepted"}},{"anchor_refs":["112:3:4"],"branch_refs":[],"candidate_id":"cand_dd45d05c66b57a47f488","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:3:4:two-beat-negation-sound","source_type":"word_analysis","support_ids":["sup_65029fbb7ab28882f428","sup_bb27ba6053f68843fce1"],"title":"audible return of the negation frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:4","qac_refs":["112:3:3:2"],"status":"accepted"}},{"anchor_refs":["112:3:5"],"branch_refs":[],"candidate_id":"cand_6f4de502541f8843adfc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001683"],"scope":"focus_ayah","source_local_id":"112:3:5:boundary-with-self-sufficiency-and-equivalence","source_type":"word_analysis","support_ids":["sup_45f663874dd4cad39259","sup_c81315a37e2fff514b90"],"title":"non-origin bridges 112:2 and 112:4","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:5","qac_refs":["112:3:4:1"],"status":"accepted"}},{"anchor_refs":["112:3:5"],"branch_refs":[],"candidate_id":"cand_20ab66b1aa709959d1a3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001683"],"scope":"focus_ayah","source_local_id":"112:3:5:closing-active-passive-mirror","source_type":"word_analysis","support_ids":["sup_c81315a37e2fff514b90","sup_f9edd06c6cbe1d56d9cf"],"title":"passive landing completes the mirror","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:5","qac_refs":["112:3:4:1"],"status":"accepted"}},{"anchor_refs":["112:3:5"],"branch_refs":[],"candidate_id":"cand_6a3d211f8aaf5f6bff62","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001683"],"scope":"focus_ayah","source_local_id":"112:3:5:finite-passive-form-contrast","source_type":"word_analysis","support_ids":["sup_c81315a37e2fff514b90","sup_e238d0dae2b1d92d798a"],"title":"finite passive differs from reflexive or participial alternatives","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:5","qac_refs":["112:3:4:1"],"status":"accepted"}},{"anchor_refs":["112:3:5"],"branch_refs":[],"candidate_id":"cand_d699dcd516d30edb78c4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001683"],"scope":"focus_ayah","source_local_id":"112:3:5:passive-jussive-categorical-origin-denial","source_type":"word_analysis","support_ids":["sup_c81315a37e2fff514b90","sup_fe0a71a5a42c994ccf01"],"title":"passive jussive makes non-origin categorical","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:5","qac_refs":["112:3:4:1"],"status":"accepted"}},{"anchor_refs":["112:3:5"],"branch_refs":[],"candidate_id":"cand_e6f045801fd11d60a8ae","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001683"],"scope":"focus_ayah","source_local_id":"112:3:5:rare-passive-imperfect-in-common-root","source_type":"word_analysis","support_ids":["sup_1e4654db9c75c6c6d611","sup_c81315a37e2fff514b90"],"title":"rare passive imperfect concentrates a common root field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:5","qac_refs":["112:3:4:1"],"status":"accepted"}},{"anchor_refs":["112:3:5"],"branch_refs":[],"candidate_id":"cand_b0e5eabbd07ae79ffeef","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001683"],"scope":"focus_ayah","source_local_id":"112:3:5:root-field-origin-pressure","source_type":"word_analysis","support_ids":["sup_3f6c75dfc578fcfd879d","sup_c81315a37e2fff514b90"],"title":"root field widens non-origin beyond biological birth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:5","qac_refs":["112:3:4:1"],"status":"accepted"}},{"anchor_refs":["112:3:5"],"branch_refs":[],"candidate_id":"cand_8ba73dd98b780012891d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001683"],"scope":"focus_ayah","source_local_id":"112:3:5:same-referent-patient-role-refused","source_type":"word_analysis","support_ids":["sup_bb2459af56f6635a1008","sup_c81315a37e2fff514b90"],"title":"same subject placed in the refused patient role","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:5","qac_refs":["112:3:4:1"],"status":"accepted"}},{"anchor_refs":["112:3:5"],"branch_refs":[],"candidate_id":"cand_417219da481b263e038d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001683"],"scope":"focus_ayah","source_local_id":"112:3:5:source-agent-suppressed","source_type":"word_analysis","support_ids":["sup_0c92fa1ada914df617b2","sup_c81315a37e2fff514b90"],"title":"no source phrase or passive agent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:3:5","qac_refs":["112:3:4:1"],"status":"accepted"}},{"anchor_refs":["112:3:2"],"branch_refs":[],"candidate_id":"cand_5393d4938cf3a5e68493","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001683"],"scope":"focus_ayah","source_local_id":"112:3:2:1","source_type":"qac_morpheme","support_ids":["sup_6cff27bff7ff792c1af8"],"title":"QAC root occurrence: و ل د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["112:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:3","branch_refs":["root_001683/B001","root_001683/B002","root_001683/B003"],"candidate_id":"cand_03b5d0cb321b5265ebcb","commentary_obligation":"review","hft_ref":"hft_d5c2e299c23a14c7b434","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_bidirectional_birth_closure","source_type":"hft","support_ids":["sup_b482b332bbbb1905260d"],"title":"base_bidirectional_birth_closure","trust":"legacy_unbound"},{"anchor_refs":["112:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:3","branch_refs":["root_001683/B005"],"candidate_id":"cand_3f7c4ee040f717a5ed78","commentary_obligation":"review","hft_ref":"hft_741c9f83b805420aa87c","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_nonderived_nongenerative","source_type":"hft","support_ids":["sup_b23751a6a40c49f22149"],"title":"base_nonderived_nongenerative","trust":"legacy_unbound"},{"anchor_refs":["112:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:3","branch_refs":["root_001683/B006"],"candidate_id":"cand_2356b7a7d80dcdad6d04","commentary_obligation":"review","hft_ref":"hft_3ac48a965d6373569b84","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_outside_birth_cohort","source_type":"hft","support_ids":["sup_7059ac681109a5d863d1"],"title":"base_outside_birth_cohort","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"لَمْ يَلِدْ وَلَمْ يُولَدْ","qac_morphemes":[{"lemma_ar":"لَم","morph_features":"STEM|POS:NEG|LEM:lam","morpheme_role":"STEM","pos":"NEG","qac_ref":"112:3:1:1","qac_word_ref":"112:3:1","root_ar":"","surface_ar":"لَمْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:2:1","qac_word_ref":"112:3:2","root_ar":"و ل د","surface_ar":"يَلِدْ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"112:3:3:1","qac_word_ref":"112:3:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لَم","morph_features":"STEM|POS:NEG|LEM:lam","morpheme_role":"STEM","pos":"NEG","qac_ref":"112:3:3:2","qac_word_ref":"112:3:3","root_ar":"","surface_ar":"لَمْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:4:1","qac_word_ref":"112:3:4","root_ar":"و ل د","surface_ar":"يُولَدْ"}],"word_analysis_qac_refs":[["112:3:1:1"],["112:3:2:1"],["112:3:3:1"],["112:3:3:2"],["112:3:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["112:3:1","112:3:2","112:3:3","112:3:4","112:3:5"]},"focus_surface_evidence":{"arabic_uthmani":"لَمْ يَلِدْ وَلَمْ يُولَدْ","qac_morphemes":[{"lemma_ar":"لَم","morph_features":"STEM|POS:NEG|LEM:lam","morpheme_role":"STEM","pos":"NEG","qac_ref":"112:3:1:1","qac_word_ref":"112:3:1","root_ar":"","surface_ar":"لَمْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:2:1","qac_word_ref":"112:3:2","root_ar":"و ل د","surface_ar":"يَلِدْ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"112:3:3:1","qac_word_ref":"112:3:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لَم","morph_features":"STEM|POS:NEG|LEM:lam","morpheme_role":"STEM","pos":"NEG","qac_ref":"112:3:3:2","qac_word_ref":"112:3:3","root_ar":"","surface_ar":"لَمْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:4:1","qac_word_ref":"112:3:4","root_ar":"و ل د","surface_ar":"يُولَدْ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["112:3:1:1"],["112:3:2:1"],["112:3:3:1"],["112:3:3:2"],["112:3:4:1"]],"word_analysis_refs":["112:3:1","112:3:2","112:3:3","112:3:4","112:3:5"],"word_rows":[{"analysis_record_ref":"112:3:1","analytic_gloss_range_en":"jussive negator governing the following imperfect verb, locally giving the first denial categorical scope rather than a mere report of one past non-event","analytic_root_gloss_range_en":null,"qac_refs":["112:3:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَمْ","transliteration":"lam"}},{"analysis_record_ref":"112:3:2","analytic_gloss_range_en":"active Form I begetting or generating, locally negated without an object so that outward generative sourcehood is denied absolutely","analytic_root_gloss_range_en":"birth, offspring, parentage, delivery, and generated-or-derived production; locally the active verb selects the begetting/generating branch while broader noun and derivative branches remain guardrails rather than separate active senses","qac_refs":["112:3:2:1"],"root":{"arabic":"و ل د","transliteration":"w-l-d"},"surface":{"arabic":"يَلِدْ","transliteration":"yalid"}},{"analysis_record_ref":"112:3:3","analytic_gloss_range_en":"coordinating conjunction that links two separately scoped negated verbal clauses and pivots the ayah from active sourcehood to passive originatedness","analytic_root_gloss_range_en":null,"qac_refs":["112:3:3:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"112:3:4","analytic_gloss_range_en":"second jussive negator, independently governing the passive verb and making non-origin a complete denial rather than an ellipsis after the conjunction","analytic_root_gloss_range_en":null,"qac_refs":["112:3:3:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَمْ","transliteration":"lam"}},{"analysis_record_ref":"112:3:5","analytic_gloss_range_en":"passive Form I being begotten, generated, or brought forth, locally negated as originatedness without naming any source or agent","analytic_root_gloss_range_en":"birth, offspring, parentage, delivery, generated derivation, and origin-point language; locally the passive verb selects generated-origin as the denied branch while derivative and place-or-time senses contribute bounded origin pressure","qac_refs":["112:3:4:1"],"root":{"arabic":"و ل د","transliteration":"w-l-d"},"surface":{"arabic":"يُولَدْ","transliteration":"yūlad"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["112:3"],"branch_refs":["root_001683/B001","root_001683/B002","root_001683/B003"],"candidate_id":"cand_03b5d0cb321b5265ebcb","evidence_scope":"focus_ayah","hft_ref":"hft_d5c2e299c23a14c7b434","item_id":"base_bidirectional_birth_closure","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_bidirectional_birth_closure","support_id":"sup_b482b332bbbb1905260d"},{"anchor_refs":["112:3"],"branch_refs":["root_001683/B005"],"candidate_id":"cand_3f7c4ee040f717a5ed78","evidence_scope":"focus_ayah","hft_ref":"hft_741c9f83b805420aa87c","item_id":"base_nonderived_nongenerative","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_nonderived_nongenerative","support_id":"sup_b23751a6a40c49f22149"},{"anchor_refs":["112:3"],"branch_refs":["root_001683/B006"],"candidate_id":"cand_2356b7a7d80dcdad6d04","evidence_scope":"focus_ayah","hft_ref":"hft_3ac48a965d6373569b84","item_id":"base_outside_birth_cohort","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_outside_birth_cohort","support_id":"sup_7059ac681109a5d863d1"}],"diagnostics":[],"lane_counts":{"global":11,"macro":10,"micro":3},"packet_summary":{"ayah_count":4,"focus_ref":"112:3","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]}],"window":["112:1","112:2","112:3","112:4"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"112:3","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":11,"source_present":true,"structured_insight_count":13,"unstructured_record_count":0},"identity":{"ayah_ref":"112:3","lane":"micro","linguistic_source_ref":"112:3","surface_ref":"112:3","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"112:3","target_tokens":[["Doğurmadı",["112:3:1","112:3:2"]],["ve",["112:3:3"]],["doğurulmadı",["112:3:3","112:3:4"]]],"text":"Doğurmadı ve doğurulmadı."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":4,"id":"s112-p01-001-004","label":"Whole surah","number":1,"refs":["112:1","112:2","112:3","112:4"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:2:sound-reprise-with-role-reversal","source_type":"word_analysis","support_id":"sup_017baf59920aa0d5b1a2","text":"{\"blocking_evidence\":null,\"headline\":\"similar sound with opposite grammatical role\",\"reader_payoff\":\"The reader hears a compact first denial that will be reprised by a similar-sounding passive form, so sameness of field and reversal of role arrive together.\",\"reason\":\"The two local verbs share the same root field while QAC distinguishes active and passive voice; the sound claim is a local formal payoff rather than a separate lexical sense.\",\"representative_source_ids\":[\"QE-aa782edd\",\"QE-e7c7f491\",\"QP-dde9718d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:5:source-agent-suppressed","source_type":"word_analysis","support_id":"sup_0c92fa1ada914df617b2","text":"{\"blocking_evidence\":null,\"headline\":\"no source phrase or passive agent\",\"reader_payoff\":\"The reader notices that the passive denial excludes every possible origin-source without naming and limiting the denial to one agent.\",\"reason\":\"Attachment evidence marks the passive agent as morphologically present but unresolved and instructs translators not to add an explanatory noun; the passive event itself is negated.\",\"representative_source_ids\":[\"QG-7229e1a1\",\"QG-fbc41fef\",\"QI-dfdcb7c7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:4:compressed-two-direction-frame","source_type":"word_analysis","support_id":"sup_1896140564aa1d2c410f","text":"{\"blocking_evidence\":null,\"headline\":\"four-word compression of both directions\",\"reader_payoff\":\"The reader sees how active non-begetting and passive non-origin are packed into a short balanced verbal frame.\",\"reason\":\"The local syntax has two coordinated negated clauses in four words, preserving both directions without recoverable ellipsis.\",\"representative_source_ids\":[\"QS-2338a417\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:5:rare-passive-imperfect-in-common-root","source_type":"word_analysis","support_id":"sup_1e4654db9c75c6c6d611","text":"{\"blocking_evidence\":null,\"headline\":\"rare passive imperfect concentrates a common root field\",\"reader_payoff\":\"The reader sees a common kinship and origin root field concentrated into an unusually specific passive imperfect denial.\",\"reason\":\"The contextual profile marks the passive exact form as a single low-occurrence instance, while the supplied root evidence shows a much wider field of nouns, participles, and verbal uses.\",\"representative_source_ids\":[\"QI-684a7931\",\"QI-cac56d90\",\"QH-92ed37e8\",\"MH-9179db71\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:1:twin-negation-cadence","source_type":"word_analysis","support_id":"sup_268cc3e6a6503bb45cac","text":"{\"blocking_evidence\":null,\"headline\":\"first beat of the paired negation\",\"reader_payoff\":\"The reader hears the first negator as the audible pattern that will return in the second clause.\",\"reason\":\"The repeated particle frame is locally visible at words 1 and 4, and attachment evidence warns against collapsing the two clauses into a single negation.\",\"representative_source_ids\":[\"QP-5680a771\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:4:next-ayah-particle-continuity","source_type":"word_analysis","support_id":"sup_32689b91bd63d327ae16","text":"{\"blocking_evidence\":null,\"headline\":\"negative particle architecture continues in 112:4\",\"reader_payoff\":\"The reader notices that the particle frame carries categorical negation from generation in 112:3 into equivalence in 112:4.\",\"reason\":\"The row names a concrete boundary continuation into 112:4, and nothing in local grammar contradicts treating it as a structural echo.\",\"representative_source_ids\":[\"QB-557d39dc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:1:jussive-categorical-negation","source_type":"word_analysis","support_id":"sup_3a9f56a1a31a2dc34369","text":"{\"blocking_evidence\":null,\"headline\":\"categorical jussive negation\",\"reader_payoff\":\"The reader notices that the first denial is framed as categorical exclusion of begetting, not as a report that one past event did not happen.\",\"reason\":\"QAC and attachment evidence identify the particle as a jussive negator governing the following imperfect, which supports the CRITICAL claim about categorical scope.\",\"representative_source_ids\":[\"QG-a33ecb27\",\"MG-de0906ee\",\"QS-ede22201\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:5:root-field-origin-pressure","source_type":"word_analysis","support_id":"sup_3f6c75dfc578fcfd879d","text":"{\"blocking_evidence\":null,\"headline\":\"root field widens non-origin beyond biological birth\",\"reader_payoff\":\"The reader notices that the denial reaches parentage, produced effect, and origin-point pressure, while local grammar keeps passive generated origin as the selected sense.\",\"reason\":\"V4 supports birth, offspring, generated-or-derived, and place-or-time-of-birth fields, but the local passive Form I verb selects being generated or brought forth by another rather than activating every derivative form as an independent local sense.\",\"representative_source_ids\":[\"QS-c272f3af\",\"QS-e563a3df\",\"QS-f9bba964\",\"QS-fbe4025a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:1","source_type":"word_analysis","support_id":"sup_45d6a3fca36250705495","text":"{\"gloss_range\":\"jussive negator governing the following imperfect verb, locally giving the first denial categorical scope rather than a mere report of one past non-event\",\"prose\":\"{{ar:لَمْ}} ({{tr:lam}}) opens the ayah by placing the already established divine subject into a negated verbal frame. Its government of the following imperfect makes the first denial categorical: the clause does not narrate one missing event, but bars active begetting as a valid predicate. Because this first particle governs only the first verb, the reader can feel a complete first denial before the ayah turns to the matched second denial. Its cadence also sets the template that returns at word 4, making the two negations parallel in sound as well as grammar.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَمْ}} ({{tr:lam}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:5:boundary-with-self-sufficiency-and-equivalence","source_type":"word_analysis","support_id":"sup_45f663874dd4cad39259","text":"{\"blocking_evidence\":null,\"headline\":\"non-origin bridges 112:2 and 112:4\",\"reader_payoff\":\"The reader notices that non-origin protects the self-sufficiency claim in 112:2 and prepares the equivalence denial in 112:4, while the local word remains the passive verb of originatedness.\",\"reason\":\"The boundary rows give concrete nearby references, and local grammar supports the passive non-origin denial as the bridge without turning the prior title or next ayah into the local lexical sense.\",\"representative_source_ids\":[\"QB-4249b021\",\"QB-aad583a8\",\"QB-db3eb264\",\"QB-fc91b87a\",\"QB-fd3a88c4\",\"QY-9006f84b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:2:absolute-active-denial","source_type":"word_analysis","support_id":"sup_488044474e87872da409","text":"{\"blocking_evidence\":null,\"headline\":\"objectless active begetting denied absolutely\",\"reader_payoff\":\"The reader notices that the clause denies the whole outward begetting relation, not merely the existence of one named offspring.\",\"reason\":\"Attachment evidence marks the active verb with no object, and translation support warns against adding an object where the Arabic presents absolute compression.\",\"representative_source_ids\":[\"QG-2abf49ce\",\"QG-d5a57a55\",\"QI-dd316622\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:2","source_type":"word_analysis","support_id":"sup_4bd9eabfdd826a350576","text":"{\"gloss_range\":\"active Form I begetting or generating, locally negated without an object so that outward generative sourcehood is denied absolutely\",\"prose\":\"{{ar:يَلِدْ}} ({{tr:yalid}}) is the active half of the ayah's generative denial. It has no expressed object, so the clause does not deny one named child or product; it denies the divine subject as source of begetting at all. The clipped jussive form under {{ar:لَمْ}} ({{tr:lam}}) keeps that denial categorical, while the hidden third-person subject carries the same referent from 112:1-2 into the verb without restating the name. The root field can include birth, offspring, and generated production, but the local Form I active verb narrows that field to direct generative sourcehood rather than causative production. The short clipped form lands on a dental stop, and its sound and root then return in {{ar:يُولَدْ}} ({{tr:yūlad}}), where the same field is reversed into passive affectedness.\",\"root_display\":\"{{ar:و ل د}} ({{tr:w-l-d}})\",\"root_gloss_range\":\"birth, offspring, parentage, delivery, and generated-or-derived production; locally the active verb selects the begetting/generating branch while broader noun and derivative branches remain guardrails rather than separate active senses\",\"surface_display\":\"{{ar:يَلِدْ}} ({{tr:yalid}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:3:active-passive-completion","source_type":"word_analysis","support_id":"sup_4e9a9fec95630ee79782","text":"{\"blocking_evidence\":null,\"headline\":\"hinge from sourcehood to originatedness\",\"reader_payoff\":\"The reader sees the second denial as the completing counterpart to the first, closing both directions of the generative relation.\",\"reason\":\"The attachment profile coordinates the passive verb with the active verb, and the local voice reversal supports the hinge from source role to product or patient role.\",\"representative_source_ids\":[\"QS-732effe5\",\"QI-e577e9ea\",\"QT-720baba5\",\"QT-b6cb4d57\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:2:implicit-subject-continuity","source_type":"word_analysis","support_id":"sup_55bc68c703373f9b0452","text":"{\"blocking_evidence\":null,\"headline\":\"hidden subject carries the same referent\",\"reader_payoff\":\"The reader notices that the denied active agency belongs to the same discourse subject from 112:1-2 even though the noun is not repeated.\",\"reason\":\"The verb is third-person masculine singular with no overt subject, and attachment evidence resolves the subject through discourse continuity.\",\"representative_source_ids\":[\"QG-c496d220\",\"QB-3e1d27b6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:2:root-field-narrowed-to-generation","source_type":"word_analysis","support_id":"sup_5b898ca869f2790442f0","text":"{\"blocking_evidence\":null,\"headline\":\"birth-root pressure narrowed to active generation\",\"reader_payoff\":\"The reader notices that the denial reaches beyond a possession formula for offspring into the act of generating, while local grammar keeps the selected sense on active begetting.\",\"reason\":\"V4 supports birth, offspring, and generated-production branches for the root, but the local active Form I verb selects the direct begetting or generating action rather than a nominal offspring formula or every derivative branch.\",\"representative_source_ids\":[\"QS-466aa5dc\",\"QF-1b067ccb\",\"MF-a4fa7bed\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:3:separate-scope-coordination","source_type":"word_analysis","support_id":"sup_5f20642af7667a7633ae","text":"{\"blocking_evidence\":null,\"headline\":\"coordination without collapsed scope\",\"reader_payoff\":\"The reader notices that the conjunction binds two complete denials without letting the first negator govern both verbs.\",\"reason\":\"QAC identifies coordination, and attachment evidence marks the second negated verbal clause as coordinated with the first while preserving separate jussive governors.\",\"representative_source_ids\":[\"QG-f189cf5c\",\"QT-2399dcdc\",\"QY-7af5d9f0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:4","source_type":"word_analysis","support_id":"sup_65029fbb7ab28882f428","text":"{\"gloss_range\":\"second jussive negator, independently governing the passive verb and making non-origin a complete denial rather than an ellipsis after the conjunction\",\"prose\":\"The second {{ar:لَمْ}} ({{tr:lam}}) gives the passive denial its own scope. The ayah does not rely on ellipsis after the conjunction; it chooses explicit repetition, an elaborating form rather than omission, so that non-origin stands as a separate proposition. Even inside the compact cluster with {{ar:وَ}} ({{tr:wa}}), coordination and negation remain formally distinct. This repetition creates the two-beat negative frame of the ayah and also anticipates the continued negative particle architecture in 112:4.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَمْ}} ({{tr:lam}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"112:3:2:1","source_type":"qac_morpheme","support_id":"sup_6cff27bff7ff792c1af8","text":"{\"lemma_ar\":\"وَلَدَ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:walada|ROOT:wld|3MS|MOOD:JUS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"112:3:2:1\",\"qac_word_ref\":\"112:3:2\",\"root_ar\":\"و ل د\",\"surface_ar\":\"يَلِدْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:4:independent-passive-scope","source_type":"word_analysis","support_id":"sup_772329d21039e5ef4d66","text":"{\"blocking_evidence\":null,\"headline\":\"passive denial receives its own negator\",\"reader_payoff\":\"The reader notices that non-origin is asserted as an independent denial, not as a grammatical afterthought to the first negation.\",\"reason\":\"QAC and attachment evidence identify the second particle as governing the passive verb, and translation support warns against collapsing the repeated negations into one scope.\",\"representative_source_ids\":[\"QG-6a8f9e8f\",\"MG-8ba8f189\",\"QS-3498ede5\",\"QI-4ceed910\",\"QT-ec372bdd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:3","source_type":"word_analysis","support_id":"sup_7f2adc5ab4cf7e6370dc","text":"{\"gloss_range\":\"coordinating conjunction that links two separately scoped negated verbal clauses and pivots the ayah from active sourcehood to passive originatedness\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) is the hinge, not a spillover of the first negation. It joins two complete clauses whose negators remain separate, so the active denial and the passive denial keep equal weight. The conjunction makes the second half feel like the necessary complement of the first: sourcehood has been denied, then originatedness is denied. In the tight cluster with the second {{ar:لَمْ}} ({{tr:lam}}), the reader hears the sentence restart the negation frame before reaching the passive verb.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:2:jussive-form-and-direct-agency","source_type":"word_analysis","support_id":"sup_8d78e373b2200b274cf7","text":"{\"blocking_evidence\":null,\"headline\":\"active jussive form keeps direct agency visible\",\"reader_payoff\":\"The reader sees direct generative agency being denied in a clipped governed verb rather than in a looser causative or independent ongoing form.\",\"reason\":\"QAC identifies the word as Form I active imperfect in jussive mood after the negator; this supports direct agency while excluding an imported causative form.\",\"representative_source_ids\":[\"QG-bc999522\",\"QF-abc4cf84\",\"QF-fab1271a\",\"QF-fb8638a9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:4:separable-particle-in-cluster","source_type":"word_analysis","support_id":"sup_93da330481556f942d05","text":"{\"blocking_evidence\":null,\"headline\":\"negator remains distinct inside the cluster\",\"reader_payoff\":\"The reader notices that the tight surface cluster still contains two functions: connection and renewed negation.\",\"reason\":\"The conjunction and negator appear together in the surface cluster, but QAC tags the negator separately and attachment evidence assigns it its own verbal complement.\",\"representative_source_ids\":[\"QF-9446802c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:5:same-referent-patient-role-refused","source_type":"word_analysis","support_id":"sup_bb2459af56f6635a1008","text":"{\"blocking_evidence\":null,\"headline\":\"same subject placed in the refused patient role\",\"reader_payoff\":\"The reader notices that the same divine referent denied as active source is also denied as passive product.\",\"reason\":\"The passive verb is third-person masculine singular with an implicit subject continuing the discourse subject, and the passive morphology makes that referent the patient role only to have that role negated.\",\"representative_source_ids\":[\"QG-cc02c9a4\",\"QS-88d630b2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:4:two-beat-negation-sound","source_type":"word_analysis","support_id":"sup_bb27ba6053f68843fce1","text":"{\"blocking_evidence\":null,\"headline\":\"audible return of the negation frame\",\"reader_payoff\":\"The reader hears the logical symmetry as a repeated negative beat before parsing the full active-passive contrast.\",\"reason\":\"The repeated negator occurs at words 1 and 4, making the formal symmetry audible in the local wording.\",\"representative_source_ids\":[\"QP-f15eda95\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:1:opening-discourse-continuity","source_type":"word_analysis","support_id":"sup_bbba8a17fce379e97b6c","text":"{\"blocking_evidence\":null,\"headline\":\"verbal denial opens without a restated subject\",\"reader_payoff\":\"The reader sees ayah 3 as an immediate verbal unpacking of the divine subject established in 112:1-2.\",\"reason\":\"The local verb has an implicit third-person masculine subject, and the attachment profile treats the first two words as a complete negated verbal clause continuing the prior discourse subject.\",\"representative_source_ids\":[\"QT-476c2d91\",\"QT-4bf83681\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:5","source_type":"word_analysis","support_id":"sup_c81315a37e2fff514b90","text":"{\"gloss_range\":\"passive Form I being begotten, generated, or brought forth, locally negated as originatedness without naming any source or agent\",\"prose\":\"{{ar:يُولَدْ}} ({{tr:yūlad}}) closes the ayah by reversing the root field into passive affectedness. The passive form lets the sentence raise the patient role of being generated, then the second {{ar:لَمْ}} ({{tr:lam}}) refuses that role altogether. No source phrase or passive agent is supplied, so the denial is not limited to one parent, source, or process; the whole possibility of divine originatedness is blocked. The broader {{ar:و ل د}} ({{tr:w-l-d}}) field includes birth, offspring, produced result, and origin-point language, but local grammar narrows it to passive generated origin. The finite passive denies the generating event itself, not reflexive arising or an already-born identity label, and the imperfect-jussive construction makes the denial categorical rather than a denied historical birth report. This rare passive imperfect then lands as the counterpart to {{ar:يَلِدْ}} ({{tr:yalid}}), protecting the self-sufficiency claim in 112:2 and preparing the move to equivalence-denial in 112:4.\",\"root_display\":\"{{ar:و ل د}} ({{tr:w-l-d}})\",\"root_gloss_range\":\"birth, offspring, parentage, delivery, generated derivation, and origin-point language; locally the passive verb selects generated-origin as the denied branch while derivative and place-or-time senses contribute bounded origin pressure\",\"surface_display\":\"{{ar:يُولَدْ}} ({{tr:yūlad}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:5:finite-passive-form-contrast","source_type":"word_analysis","support_id":"sup_e238d0dae2b1d92d798a","text":"{\"blocking_evidence\":null,\"headline\":\"finite passive differs from reflexive or participial alternatives\",\"reader_payoff\":\"The reader notices that the actual form negates being generated by another as an event, not reflexive arising or an already-born identity label.\",\"reason\":\"The local word is finite passive Form I; comparison with forms such as {{ar:يَتَوَلَّدْ}} ({{tr:yatawallad}}) or {{ar:مَوْلُود}} ({{tr:mawlūd}}) is useful only as contrast, not as replacement of the local parse.\",\"representative_source_ids\":[\"QF-62c991f0\",\"QF-d3d7b150\",\"QF-fe1f006f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:2:sparse-verbal-slot","source_type":"word_analysis","support_id":"sup_e60bbb3dd45af74ec36f","text":"{\"blocking_evidence\":null,\"headline\":\"active imperfect stands out in the root distribution\",\"reader_payoff\":\"The reader notices that a root field often carried by kinship nouns is concentrated here into a sparse active verbal denial.\",\"reason\":\"The contextual profile marks the exact active form as low-occurrence, and V4 shows many noun or form units in the same root field.\",\"representative_source_ids\":[\"QI-7726dea8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:2:first-half-of-mirror","source_type":"word_analysis","support_id":"sup_e6d503612ce66f05f981","text":"{\"blocking_evidence\":null,\"headline\":\"active side of the two-clause mirror\",\"reader_payoff\":\"The reader sees the first clause as a complete active denial that prepares, but does not absorb, the later passive denial.\",\"reason\":\"Attachment evidence treats words 1-2 as a complete negated verbal clause and coordinates the passive clause separately after it.\",\"representative_source_ids\":[\"QT-d0ed5432\",\"QT-fe506ce9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:3:wa-lam-formal-cluster","source_type":"word_analysis","support_id":"sup_ecbb36e2d2fd6275a765","text":"{\"blocking_evidence\":null,\"headline\":\"clustered connector and renewed negator\",\"reader_payoff\":\"The reader hears the connector and renewed negator arrive as one compact beat while still performing different grammatical jobs.\",\"reason\":\"The surface cluster combines the conjunction with the second negator, but QAC and attachment evidence keep coordination and negation distinct.\",\"representative_source_ids\":[\"QF-de7dd0b6\",\"QE-c381eade\",\"QP-c76491f6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:5:closing-active-passive-mirror","source_type":"word_analysis","support_id":"sup_f9edd06c6cbe1d56d9cf","text":"{\"blocking_evidence\":null,\"headline\":\"passive landing completes the mirror\",\"reader_payoff\":\"The reader hears and sees the ayah close on the same generative field with the grammatical role reversed from active source to passive product.\",\"reason\":\"The second verb is coordinated with the first, shares the root field, and changes voice; its final position makes the passive non-origin denial the ayah's landing point.\",\"representative_source_ids\":[\"QT-78379326\",\"QT-ad78c467\",\"QE-10197b7f\",\"QE-4af18b0b\",\"QP-cc19f413\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:3:5:passive-jussive-categorical-origin-denial","source_type":"word_analysis","support_id":"sup_fe0a71a5a42c994ccf01","text":"{\"blocking_evidence\":null,\"headline\":\"passive jussive makes non-origin categorical\",\"reader_payoff\":\"The reader sees originatedness denied as a category, not as the absence of one historical birth event.\",\"reason\":\"QAC identifies a passive imperfect made jussive by the second negator, and the local construction supports categorical non-origin rather than a perfect-passive birth report.\",\"representative_source_ids\":[\"QG-bc9fabb4\",\"QF-284f9c01\",\"QF-e9b8837b\",\"QH-4b0bb4bd\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"لَمْ يَلِدْ وَلَمْ يُولَدْ","ayah_ref":"112:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001683/B001","root_001683/B002","root_001683/B003"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001683","role":"Born offspring supplies the relation's descendant endpoint, which the passive clause denies for the subject and the active clause denies as an output from the subject.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]},{"branch_id":"B002","mapped_root_id":"root_001683","role":"Parents by birth relation supplies the complementary progenitor endpoint, making the two clauses a closure of both kinship directions.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]},{"branch_id":"B003","mapped_root_id":"root_001683","role":"Birth and delivery supplies the event linking parent and born one; repeated negation blocks the event with the subject on either side.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]}],"changed_reading":{"after":"A two-way closure of birth relation: no descendant proceeds from the subject, and the subject proceeds from no progenitor.","before":"A one-sided statement that the subject has no child."},"confidence":"strong","focus_anchor":"The root و ل د occurs at words 2 and 4 under repeated negation, first in active voice and then in passive voice.","mechanism":"The voice reversal closes both orientations of one birth relation. The subject is denied the parent or producer position, the offspring or product position, and participation in the event that would connect those positions.","model_id":"base_bidirectional_birth_closure"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_bidirectional_birth_closure","source_type":"hft","support_id":"sup_b482b332bbbb1905260d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَمْ يَلِدْ وَلَمْ يُولَدْ","ayah_ref":"112:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001683/B005"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001683","role":"A thing generated, newly produced, or derived supplies a non-biological source-result relation that the two voices negate in opposite directions.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]}],"changed_reading":{"after":"The subject is neither a source of derivative being nor a derivative whose identity depends on an originating source.","before":"The negations concern only biological ancestry and offspring."},"confidence":"exploratory","focus_anchor":"The active-passive pair at words 2 and 4 can orient the same root as output-from-subject and subject-as-output.","mechanism":"The generated-or-derived branch lifts the pair beyond literal delivery into provenance. Active voice denies that the subject generates a derivative; passive voice denies that the subject is itself generated or derivative. This remains a branch-led extension, not a replacement for the birth sense.","model_id":"base_nonderived_nongenerative"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_nonderived_nongenerative","source_type":"hft","support_id":"sup_b23751a6a40c49f22149","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَمْ يَلِدْ وَلَمْ يُولَدْ","ayah_ref":"112:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001683/B006"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_001683","role":"A peer defined by shared birth-age supplies cohort placement; the passive clause removes such placement and the active clause removes downstream generational placement.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]}],"changed_reading":{"after":"The subject also resists classification by birth cohort or by a generation descending from it.","before":"The subject lacks direct ascendants and descendants."},"confidence":"exploratory","focus_anchor":"The passive denial at word 4 removes a birth event for the subject, while the active denial at word 2 removes a descendant generation.","mechanism":"The same-birth-age branch makes birth a coordinate that groups beings into cohorts. Denying birth removes that coordinate for the subject; denying begetting prevents a later cohort from being organized as the subject's issue.","model_id":"base_outside_birth_cohort"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_outside_birth_cohort","source_type":"hft","support_id":"sup_7059ac681109a5d863d1","trust":"legacy_unbound"}]}
</lane_packet_json>
