# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **109:3**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s109-regular-20260911/s109/109_3/micro.discovery.json` and modify nothing
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
  "ayah_ref": "109:3",
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
{"analysis_context":{"analysis_id":"s109-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"109:3","host_surah":109,"lane_context_refs":[],"ordered_context_refs":["109:0","109:1","109:2","109:4","109:5","109:6","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Anlam, köle edinme eylemini ve dinsel bağlılığı değil, özgür olmayan kişinin statüsünü bildirir.","branch_kind":"bare","branch_ref":"root_000973/B001","candidate_links":[{"candidate_id":"cand_bf82e5441a1d7719e35b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَابِد","morph_features":"STEM|POS:N|ACT|PCPL|LEM:EaAbid|ROOT:Ebd|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:3:3:1","qac_word_ref":"109:3:3","surface_ar":"عَٰبِدُونَ"},{"lemma_ar":"عَبَدَ","morph_features":"STEM|POS:V|IMPF|LEM:Eabada|ROOT:Ebd|1S","morpheme_role":"STEM","pos":"V","qac_ref":"109:3:5:1","qac_word_ref":"109:3:5","surface_ar":"أَعْبُدُ"}],"gloss":"özgür olmayan, sahip olunan kişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi özgürün karşıtı olarak bir başkasının mülkiyetinde bulunur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hukuki ölçüt, kişinin alım satıma konu edilebilmesidir."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kölelik statüsündeki kişiyi hem toplumsal hem de eski hukuki sınırıyla karşılar.","boundary_detail":"Anlam, köle edinme eylemini ve dinsel bağlılığı değil, özgür olmayan kişinin statüsünü bildirir.","branch_image_ar":"الرق والملك","concept_gloss":"özgür olmayan, sahip olunan kişi","contextual_glosses":[{"applicability":"Bağlam tarihsel mülkiyet statüsünü zaten açıkça gösterdiğinde doğal ve kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Özgürün karşıtı olan ve bir başkasına ait sayılan kişiyi belirtir."},"facet_ids":["F001","F002"],"text":"köle","usage_role":"general"}],"definition":"Özgür olmayan, bir başkasının mülkiyetinde sayılan ve eski hukuk düzeninde alınıp satılabilen insandır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi özgürün karşıtı olarak bir başkasının mülkiyetinde bulunur."},{"facet_id":"F002","role":"specialization","statement":"Hukuki ölçüt, kişinin alım satıma konu edilebilmesidir."}],"identity_rationale":"Kaynak ifadesi, özgür kişinin karşıtı olan ve hukuken sahip olunup alınıp satılabilen insanı açıkça tanımlar. Bu nedenle dalın çekirdeği tapınma ya da boyun eğme eylemi değil, kölelik durumundaki kişidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"özgür olmayan, sahip olunan kişi"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"köleler"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"köle doğmuş veya kuşaklar boyunca köle kalmış kişiler"}],"lexicalization_note":"Dal yalın bir ad anlamıdır; tanım herhangi bir özel söz öbeğine bağlı ek anlam taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kişi ile kölelik alanını ayıran ve kölelik ile özgürleşme karşıtlığını gösteren iki ilişki sınırı en iyi açıklayan adaylardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın göndergesi köle durumundaki insandır; komşu dal ise bu insanı da içeren daha geniş bir statü, mülkiyet ve köleleştirme alanı kurar.","focus_only":"Odak dal doğrudan kölelik statüsündeki kişiyi adlandırır.","gloss":"köle kişi ile kölelik düzeni","neighbor_only":"Komşu dal kölelik durumunu, köle mülkiyetini ve köleleştirme eylemini de kapsar.","neighbor_ref":"root_000586/B003","relation_type":"near_synonym","shared_zone":"İki dal da insanın özgürlükten yoksun bırakılıp sahip olunması alanındadır."},{"boundary_match":"opposed","distinction":"Odak dal özgürlükten yoksun statüyü adlandırırken komşu dal o statünün sona erdirilmesini ve kişinin özgür kılınmasını anlatır.","focus_only":"Kişi özgür değildir ve bir başkasının mülkiyetinde sayılır.","gloss":"kölelik durumu ve özgürleşme","neighbor_only":"Kişi kölelik bağından çıkarılarak özgürlüğüne kavuşur.","neighbor_ref":"root_000979/B001","relation_type":"polarity_pair","shared_zone":"İki dal kişinin hukuki ve toplumsal özgürlük durumunu karşıt yönlerden ele alır."}],"source_phrase_ar":"العبد وهو المملوك (maqayis)؛ العبد المملوك وجمعه عبيد (ayn)؛ العبد ضد الحر (jamhara)؛ العبد خلاف الحر والجمع عبيد (sihah)؛ العبيد مماليك (tahdhib)؛ عبد بحكم الشرع الإنسان الذي يصح بيعه وابتياعه (mufradat)","source_summary":"Kaynaklar, bu kişiyi özgürün karşıtı ve sahip olunan insan olarak ortak biçimde tanımlar; hukuki açıklama alınıp satılabilmeyi belirleyici sayar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه العبد المملوك وخلاف الحر ومن يصح بيعه وابتياعه وجموع العبيد والأعبد والعبدى والمعبدة","what_is_not_ar":"ليس عبادة الله ولا الطاعة الخاضعة ولا تعبيد الطريق أو البعير"},"support_links":["sup_85f9ebc7d6564cbecf79"]},{"boundary":"Dal, insanın Tanrı'ya nispet edilen konumunu anlatır; kişinin hukuki statüsünü veya yaptığı tapınmayı tek başına bildirmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000973/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَابِد","morph_features":"STEM|POS:N|ACT|PCPL|LEM:EaAbid|ROOT:Ebd|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:3:3:1","qac_word_ref":"109:3:3","surface_ar":"عَٰبِدُونَ"},{"lemma_ar":"عَبَدَ","morph_features":"STEM|POS:V|IMPF|LEM:Eabada|ROOT:Ebd|1S","morpheme_role":"STEM","pos":"V","qac_ref":"109:3:5:1","qac_word_ref":"109:3:5","surface_ar":"أَعْبُدُ"}],"gloss":"Tanrı'ya ait sayılan insan veya topluluk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Her insan yaratılmışlık ve aitlik bakımından Tanrı'nın kulu sayılabilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Çoğul adlandırma, Tanrı'ya bağlı topluluğu veya onun tarafında bulunanları gösterebilir."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaratılmışlık, aitlik ve topluluk bağlılığını hukuki kölelikle karıştırmadan birlikte karşılar.","boundary_detail":"Dal, insanın Tanrı'ya nispet edilen konumunu anlatır; kişinin hukuki statüsünü veya yaptığı tapınmayı tek başına bildirmez.","branch_image_ar":"الانتساب إلى الله عبدا","concept_gloss":"Tanrı'ya ait sayılan insan veya topluluk","contextual_glosses":[{"applicability":"Tek bir insanın yaratılmışlık ve aitlik yönünden Tanrı'ya nispet edildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çoğul kullanımın bağlı topluluk veya taraf anlamını göstermez.","preserves":"Tek kişinin Tanrı'ya ait sayılma yönünü korur."},"facet_ids":["F001"],"text":"Tanrı'nın kulu","usage_role":"contextual"},{"applicability":"Çoğul adlandırmanın bir topluluğu veya Tanrı'nın tarafında bulunanları gösterdiği yerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek tek bütün insanların yaratılmışlık temelindeki kulluğunu göstermez.","preserves":"Topluluk bağlılığını ve Tanrı'ya nispeti korur."},"facet_ids":["F002"],"text":"Tanrı'ya bağlı topluluk","usage_role":"contextual"}],"definition":"Özgür ya da köle ayrımı olmaksızın insanın, yaratılmış ve ona ait olması bakımından Tanrı'nın kulu sayılmasıdır; çoğul kullanım ona bağlı topluluğu da gösterebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Her insan yaratılmışlık ve aitlik bakımından Tanrı'nın kulu sayılabilir."},{"facet_id":"F002","role":"extension","statement":"Çoğul adlandırma, Tanrı'ya bağlı topluluğu veya onun tarafında bulunanları gösterebilir."}],"identity_rationale":"Kaynak ifadesi, özgür ya da köle her insanın yaratılmışlık ve aitlik bakımından Tanrı'nın kulu sayılmasını, ayrıca ona bağlı topluluğu bildirir. Bu kimlik, hukuki kölelikten ve tapınma eyleminden ayrı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"Tanrı'nın kulu"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"Tanrı'nın kulları veya ona bağlı topluluk"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"Tanrı'ya ait sayılan bütün kullar"}],"lexicalization_note":"Yalın insan adlandırması ile Tanrı'ya aitliği bildiren ad öbekleri birlikte bulunur; tanım bu kullanımları birbirine karıştırmadan kapsar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dalın sınırını en açık biçimde hukuki kölelik statüsü ve etkin tapınma davranışıyla yapılan karşılaştırmalar gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bütün insanlara uzanabilen dinsel ve yaratılışsal bir nispet kurar; komşu dal ise insanlar arasındaki somut kölelik statüsünü adlandırır.","focus_only":"Özgür veya köle her insan yaratılmışlık bakımından Tanrı'ya ait sayılabilir.","gloss":"Tanrı'ya kulluk nispeti ve hukuki kölelik","neighbor_only":"Komşu dal yalnızca özgür olmayan ve insanlar arasında mülkiyet konusu sayılan kişiyi anlatır.","neighbor_ref":"root_000973/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir insanın başka bir varlığa ait sayılması düşüncesini paylaşır."},{"boundary_match":"partial","distinction":"Bir insan eylemden bağımsız olarak Tanrı'nın kulu sayılabilir; tapınma dalı ise öznenin boyun eğme ve yönelme davranışını gerektirir.","focus_only":"Odak dal kişinin yaratılmışlık veya bağlılık temelindeki konumunu bildirir.","gloss":"kul sayılma ve tapınma","neighbor_only":"Komşu dal boyun eğerek tapınma ve itaat etme eylemini bildirir.","neighbor_ref":"root_000973/B003","relation_type":"near_neighbor","shared_zone":"İki dal Tanrı ile insan arasındaki bağlılık alanında buluşur."}],"source_phrase_ar":"تفرقة ما بين عباد الله والعبيد المملوكين (maqayis)؛ العبد الإنسان حرا أو رقيقا هو عبد الله (ayn)؛ فادخلي في عبادي أي في حزبي (sihah)؛ عبد بالإيجاد وذلك ليس إلا لله (mufradat)","source_summary":"Kaynaklar, bu nispetin özgür ve köle bütün insanları kapsayabildiğini, yaratılmış olmaya dayandığını ve çoğul kullanımda Tanrı'ya bağlı topluluğu gösterebildiğini bildirir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه إطلاق العبد على الإنسان حرا أو رقيقا منسوبا إلى الله وعلى الخلق عبيدا لله بالإيجاد وعلى جماعة عباد الله أو حزبه","what_is_not_ar":"ليس العبد المملوك بحكم الشرع وحده ولا فعل العبادة نفسه"},"support_links":[]},{"boundary":"Dal hukuki köleliği değil, bir öznenin boyun eğerek itaat veya tapınma göstermesini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000973/B003","candidate_links":[{"candidate_id":"cand_4afebc1b5f392f28652a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَابِد","morph_features":"STEM|POS:N|ACT|PCPL|LEM:EaAbid|ROOT:Ebd|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:3:3:1","qac_word_ref":"109:3:3","surface_ar":"عَٰبِدُونَ"},{"lemma_ar":"عَبَدَ","morph_features":"STEM|POS:V|IMPF|LEM:Eabada|ROOT:Ebd|1S","morpheme_role":"STEM","pos":"V","qac_ref":"109:3:5:1","qac_word_ref":"109:3:5","surface_ar":"أَعْبُدُ"}],"gloss":"boyun eğerek itaat ve tapınma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eylem, sıradan itaati aşan bir boyun eğme ve alçalma tutumu içerir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Merkezî dinsel kullanım, Tanrı'ya yönelen tapınma ve kendini bu yönelişe vermedir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Boyun eğme, özel kullanımlarda bir insana veya sahte tanrısal güce yöneltilebilir."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem davranışsal boyun eğme çekirdeğini hem de dinsel tapınma yönünü birlikte verir.","boundary_detail":"Dal hukuki köleliği değil, bir öznenin boyun eğerek itaat veya tapınma göstermesini anlatır.","branch_image_ar":"العبادة والطاعة الخاضعة","concept_gloss":"boyun eğerek itaat ve tapınma","contextual_glosses":[{"applicability":"Eylemin Tanrı'ya yöneldiği dinsel bağlamlarda en doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsana veya sahte tanrısal güce yönelen özel itaat kullanımlarını dışarıda bırakır.","preserves":"Dinsel yönelişi ve boyun eğerek tapınmayı korur."},"facet_ids":["F001","F002"],"text":"Tanrı'ya tapınmak","usage_role":"contextual"},{"applicability":"Bir insan veya sahte güç karşısındaki alçaltıcı itaati anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tanrı'ya yönelen tapınma ve kendini tapınmaya verme yönünü tek başına taşımaz.","preserves":"Boyun eğme ve itaat çekirdeğini korur."},"facet_ids":["F001","F003"],"text":"boyun eğip itaat etmek","usage_role":"contextual"}],"definition":"Bir varlığa en ileri ölçüde boyun eğerek itaat etmek ve tapınma yönelişi göstermektir; dinsel kullanım Tanrı'ya, bazı özel söz öbekleri ise sahte tanrısal güçlere yönelir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eylem, sıradan itaati aşan bir boyun eğme ve alçalma tutumu içerir."},{"facet_id":"F002","role":"specialization","statement":"Merkezî dinsel kullanım, Tanrı'ya yönelen tapınma ve kendini bu yönelişe vermedir."},{"facet_id":"F003","role":"extension","statement":"Boyun eğme, özel kullanımlarda bir insana veya sahte tanrısal güce yöneltilebilir."}],"identity_rationale":"Kaynak ifadesi, çekirdeği boyun eğmeyle birlikte itaat ve tapınma olarak kurar; Tanrı'ya yönelen kullanım merkezde olsa da bir insana veya sahte tanrısal güce boyun eğme kullanımları da belirtilir. Bu nedenle tapınma, uysal itaat ve en ileri boyun eğme birlikte korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"Tanrı'ya boyun eğerek tapındı"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"boyun eğerek tapınma"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kendini tapınmaya verme"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"sahte tanrısal güce boyun eğip itaat etti"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"sahte tanrısal güçlere veya putlara tapan topluluk"}],"lexicalization_note":"Yalın eylem ve adlar ile belirli nesnelere yönelen söz öbekleri birlikte bulunur; özel nesneli kullanımlar bütün dalın tek sınırı yapılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tapınma ile genel dinsel itaat arasındaki sınırı gösteren iki yakın anlamlı dal en yararlı karşılaştırmaları sağlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın sınırı boyun eğmeyle birlikte itaat üzerinden daha geniştir; komşu dal ise Tanrı'ya yakınlaşma amacı ve dinsel yöneliş üzerinde yoğunlaşır.","focus_only":"Odak dal boyun eğen itaati ve sahte güçlere yönelen özel kullanımları da kapsar.","gloss":"boyun eğerek tapınma ve Tanrı'ya yönelme","neighbor_only":"Komşu dal Tanrı'ya yakınlaşma amacı taşıyan dinsel yönelişi ve bu yönelişteki kişiyi özellikle kapsar.","neighbor_ref":"root_001498/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın merkezinde Tanrı'ya tapınma ve kendini dinsel yönelişe verme bulunur."},{"boundary_match":"partial","distinction":"Odak dal tapınma yönelişini kurucu unsur yapar; komşu dal ise tapınma şartı olmadan dinsel doğrultuda itaat ve görev yerine getirmeye uzanır.","focus_only":"Odak dal tapınma ve boyun eğmenin en ileri derecesini içerir.","gloss":"tapınma ve dinsel itaat","neighbor_only":"Komşu dal dinsel yolda doğru davranmayı ve buyruğu yerine getirmeyi de kapsar.","neighbor_ref":"root_001260/B001","relation_type":"near_synonym","shared_zone":"İki dal dinsel bağlamdaki itaat ve boyun eğme alanını paylaşır."}],"source_phrase_ar":"عبد يعبد عبادة فلا يقال إلا لمن يعبد الله (maqayis;ayn)؛ تعبدت للرجل إذا تذللت له (jamhara)؛ العبادة الطاعة والتعبد التنسك (sihah)؛ إياك نعبد إياك نطيع الطاعة التي نخضع معها (tahdhib)؛ العبودية إظهار التذلل والعبادة غاية التذلل (mufradat)","source_summary":"Kaynaklar tapınmayı boyun eğmeyle birlikte itaat ve en ileri alçalma olarak açıklar; dinsel yöneliş merkezdeyken insanlara veya sahte güçlere yönelen bağımlı kullanımlar da vardır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه عبادة الله والتنسك والطاعة مع الخضوع والتوحيد وعبادة الطاغوت بمعنى طاعته والخضوع لملك أو دنيا","what_is_not_ar":"ليس الرق الشرعي ولا مجرد الانتساب إلى الله بالإيجاد ولا تذليل الطريق أو البعير"},"support_links":["sup_74874eb41af4fb5819f2"]},{"boundary":"Anlam insanı köleleştiren veya köle gibi boyunduruk altına alan eylemdir; tapınma ya da nesneleri kullanıma hazırlama değildir.","branch_kind":"bare","branch_ref":"root_000973/B004","candidate_links":[{"candidate_id":"cand_bf82e5441a1d7719e35b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَابِد","morph_features":"STEM|POS:N|ACT|PCPL|LEM:EaAbid|ROOT:Ebd|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:3:3:1","qac_word_ref":"109:3:3","surface_ar":"عَٰبِدُونَ"},{"lemma_ar":"عَبَدَ","morph_features":"STEM|POS:V|IMPF|LEM:Eabada|ROOT:Ebd|1S","morpheme_role":"STEM","pos":"V","qac_ref":"109:3:5:1","qac_word_ref":"109:3:5","surface_ar":"أَعْبُدُ"}],"gloss":"köleleştirmek veya köle gibi boyunduruk altına almak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eyleyen, başka bir insanı köle edinir veya köle durumuna getirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hukuki statü değişmese bile kişiyi köle gibi çalıştıracak ölçüde ezme ve boyunduruk altına alma da kapsama girer."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem gerçek köle edinmeyi hem de özgür kişiyi köle gibi çalıştıracak ölçüde ezmeyi karşılar.","boundary_detail":"Anlam insanı köleleştiren veya köle gibi boyunduruk altına alan eylemdir; tapınma ya da nesneleri kullanıma hazırlama değildir.","branch_image_ar":"التعبيد والاستعباد","concept_gloss":"köleleştirmek veya köle gibi boyunduruk altına almak","contextual_glosses":[{"applicability":"Kişinin gerçekten köle edinildiği veya köle durumuna getirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Özgür kişiyi hukuken köle yapmadan köle gibi boyunduruk altına alma uzantısını belirtmez.","preserves":"Gerçek köle edinme ve statüye sokma eylemini korur."},"facet_ids":["F001"],"text":"köleleştirmek","usage_role":"general"},{"applicability":"Özgür bir kişinin köle gibi boyunduruk altına alındığı bağlamı açıklar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişiyi hukuken köle edinme veya köle statüsüne sokma sonucunu zorunlu kılmaz.","preserves":"Köle gibi boyunduruk altına alma ve çalıştırma yönünü korur."},"facet_ids":["F002"],"text":"köle gibi ezip çalıştırmak","usage_role":"explanatory"}],"definition":"Bir insanı köle edinmek, köle durumuna getirmek ya da özgür olsa bile köle gibi çalışacak ölçüde boyunduruk altına almaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eyleyen, başka bir insanı köle edinir veya köle durumuna getirir."},{"facet_id":"F002","role":"extension","statement":"Hukuki statü değişmese bile kişiyi köle gibi çalıştıracak ölçüde ezme ve boyunduruk altına alma da kapsama girer."}],"identity_rationale":"Kaynak ifadesi bir kişiyi köle edinme, köle durumuna getirme veya özgür olsa bile köle gibi çalışacak ölçüde boyunduruk altına alma eylemlerini ortak bir ettirgen çekirdekte birleştirir. Dal bu eylemi, kişinin mevcut kölelik statüsünden ayrı olarak tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"onu köleleştirdi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"kişiyi ezip köleleştirdi; topluluğu köle edindi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"onu köle durumuna getirdi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"özgür olsa da onu köle gibi boyunduruk altına aldı"}],"lexicalization_note":"Dal yalın eylem anlamını taşır; tanım belirli bir söz öbeğine özgü kapsam eklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel baskı alanıyla ve ortaya çıkan kölelik statüsüyle yapılan iki karşılaştırma eylemin özel sonucunu açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kurucu sonucu köle edinme ya da köle gibi çalıştırmadır; komşu dal bu sonuca varmayan genel baskı ve zorlamaya da uzanır.","focus_only":"Odak dal insanı özellikle köle edinme veya köle gibi çalıştırma sonucuna bağlar.","gloss":"köleleştirme ve zorla boyunduruk altına alma","neighbor_only":"Komşu dal mülkiyetin yanı sıra genel zorlama, aşağılama ve istenmeyen işe sürüklemeyi de kapsar.","neighbor_ref":"root_000504/B004","relation_type":"near_synonym","shared_zone":"İki dal insan üzerinde egemenlik kurma, aşağılama ve mülkiyet alanında önemli ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal süreç ve ettirgen işlemdir; komşu dal ise bu işlemin olası sonucundaki kişiyi ve statüsünü gösterir.","focus_only":"Odak dal bir insanı köle yapan veya köle gibi boyunduruk altına alan eylemi bildirir.","gloss":"köleleştirme eylemi ve köle kişi","neighbor_only":"Komşu dal eylemi değil, kölelik durumunda bulunan kişiyi adlandırır.","neighbor_ref":"root_000973/B001","relation_type":"near_neighbor","shared_zone":"İki dal aynı kölelik ilişkisinin neden olan eylemi ile ortaya çıkan kişi durumunu ele alır."}],"source_phrase_ar":"استعبدت فلانا اتخذته عبدا (maqayis;ayn)؛ عبدت الرجل إذا ذللته وعبدت القوم اتخذتهم عبيدا (jamhara)؛ التعبيد الاستعباد (sihah)؛ عبدت العبيد وأعبدتهم أي صيرتهم عبيدا (tahdhib)؛ عبدت فلانا إذا ذللته وإذا اتخذته عبدا (mufradat)","source_summary":"Kaynaklar eylemi köle edinme, köle durumuna getirme ve kişiyi köle gibi çalışacak ölçüde boyunduruk altına alma yönleriyle ortaklaştırır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه عبدت الرجل واستعبدته وأعبدته وتعبدت فلانا إذا اتخذته عبدا أو صيرته كالعبد أو ذللته حتى يعمل عمل العبد","what_is_not_ar":"ليس العبادة لله ولا الطريق المعبد ولا البعير المعبد"},"support_links":["sup_85f9ebc7d6564cbecf79"]},{"boundary":"Tanım yalnızca verilen yol, deve ve gemi yapılarıyla sınırlıdır; insanı köleleştirme anlamına genellenemez.","branch_kind":"mixed_non_bare","branch_ref":"root_000973/B005","candidate_links":[{"candidate_id":"cand_7150c8229bead3f14f5d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَابِد","morph_features":"STEM|POS:N|ACT|PCPL|LEM:EaAbid|ROOT:Ebd|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:3:3:1","qac_word_ref":"109:3:3","surface_ar":"عَٰبِدُونَ"},{"lemma_ar":"عَبَدَ","morph_features":"STEM|POS:V|IMPF|LEM:Eabada|ROOT:Ebd|1S","morpheme_role":"STEM","pos":"V","qac_ref":"109:3:5:1","qac_word_ref":"109:3:5","surface_ar":"أَعْبُدُ"}],"gloss":"düzleşmiş yol, katranlanmış deve veya kaplanmış gemi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yol kullanımı, sık geçişle basılıp düzleşmiş ve geçişe elverişli hâle gelmiş yolu niteler."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Deve kullanımı, derisi baştan başa katranlanmış ve bununla birlikte uysallaştırılmış hayvanı niteler."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gemi kullanımı, dışı katran, yağ veya benzeri koruyucu maddeyle kaplanmış tekneyi niteler."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Üç yapıdaki ayrı nesne ve işlemleri yalın bir kök anlamına genellemeden birlikte temsil eder.","boundary_detail":"Tanım yalnızca verilen yol, deve ve gemi yapılarıyla sınırlıdır; insanı köleleştirme anlamına genellenemez.","branch_image_ar":"التذليل والتسوية","concept_gloss":"düzleşmiş yol, katranlanmış deve veya kaplanmış gemi","contextual_glosses":[{"applicability":"Nitelemenin yol için kullanıldığı ve sık geçiş sonucu düzleşmeyi anlattığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Devenin katranlanması ile geminin kaplanması kullanımlarını dışarıda bırakır.","preserves":"Yolun basılıp düzleşerek geçişe elverişli olmasını korur."},"facet_ids":["F001"],"text":"çok geçilerek düzleşmiş yol","usage_role":"contextual"},{"applicability":"Nitelemenin derisi bütünüyle katranlanmış ve uysallaştırılmış deve için kullanıldığı yerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Düzleşmiş yol ve kaplanmış gemi kullanımlarını göstermez.","preserves":"Devenin katranla kaplanması ve uysallaştırılması yönünü korur."},"facet_ids":["F002"],"text":"derisi katranlanmış deve","usage_role":"contextual"},{"applicability":"Gemi yüzeyinin katran veya benzeri bir maddeyle kaplandığı kullanımda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yol ve deve kullanımlarını dışarıda bırakır.","preserves":"Geminin koruyucu bir maddeyle kaplanmış olmasını korur."},"facet_ids":["F003"],"text":"katranla kaplanmış gemi","usage_role":"contextual"}],"definition":"Verilen yapılarda yolun çok geçilerek düzleşip kolay kullanılır olması, devenin derisinin katranla kaplanıp uysallaştırılması veya geminin katran, yağ ya da benzeri bir maddeyle kaplanması anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yol kullanımı, sık geçişle basılıp düzleşmiş ve geçişe elverişli hâle gelmiş yolu niteler."},{"facet_id":"F002","role":"source_variant","statement":"Deve kullanımı, derisi baştan başa katranlanmış ve bununla birlikte uysallaştırılmış hayvanı niteler."},{"facet_id":"F003","role":"source_variant","statement":"Gemi kullanımı, dışı katran, yağ veya benzeri koruyucu maddeyle kaplanmış tekneyi niteler."}],"identity_rationale":"Kaynak ifadesi tek bir genel eylemden çok üç yapıya bağlı kullanımı yan yana verir: çok geçilerek düzleşmiş yol, katranlanmış ve uysallaştırılmış deve, katran veya yağla kaplanmış gemi. Dal korunabilir, ancak bu kullanımlar tek bir yalın anlammış gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"çok geçilerek düzleşmiş yol"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"derisi baştan başa katranlanmış ve uysallaştırılmış deve"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"katranla kaplanmış gemi"}],"lexicalization_note":"Dal söz öbeğine bağlı yol ve deve anlamlarıyla bir gemi adlandırmasını birlikte taşır; her kullanım kendi nesnesi ve işlemiyle ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yumuşatma alanı ve aynı kökün insanı köleleştirme dalı, yapıların nesne ve işlem sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız verilen yol, deve ve gemi yapılarına bağlıdır; komşu dal ise nesneyi yumuşatma ve kullanıma hazırlama yönünde daha genel bir kapsama sahiptir.","focus_only":"Odak dal yol dışındaki kullanımlarda devenin veya geminin bir maddeyle kaplanmasını da içerir.","gloss":"basılıp düzleşmiş yol ve genel yumuşatma","neighbor_only":"Komşu dal yer, döşek, oturak, hayvan ve insan için genel yumuşatma ve kolaylaştırmaya uzanır.","neighbor_ref":"root_001659/B002","relation_type":"near_neighbor","shared_zone":"İki dal yol veya başka bir yüzeyin kullanıma elverişli ve kolay hâle gelmesi alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dalın belirlenmiş nesneleri yol, deve ve gemidir; insan üzerinde mülkiyet ve zor kullanma sonucu kuran anlam yalnız komşu daldadır.","focus_only":"Odak dal yolun düzleşmesini ve hayvan ya da geminin yüzeyinin işlenmesini anlatır.","gloss":"nesneyi kullanıma hazırlama ve insanı köleleştirme","neighbor_only":"Komşu dal bir insanı köle edinme veya köle gibi boyunduruk altına alma eylemidir.","neighbor_ref":"root_000973/B004","relation_type":"near_neighbor","shared_zone":"İki dalda da bir varlığı denetim veya kullanım için elverişli hâle getirme çağrışımı bulunur."}],"source_phrase_ar":"الطريق المعبد وهو المسلوك المذلل (maqayis)؛ طريق معبد أي مذلل (jamhara;mufradat)؛ البعير المعبد المهنوء بالقطران المذلل (maqayis;sihah)؛ المعبدة السفينة المقيرة (sihah;tahdhib)؛ المعبد من الإبل الذي عم جلده بالقطران (tahdhib)","source_summary":"Toplu kaynak ifadesi, yol için basılıp düzleşmeyi; deve için katranlanma ve uysallaşmayı; gemi içinse katran ya da yağla kaplanmayı ayrı gerçekleşmeler olarak verir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الطريق المعبد المسلوك المذلل والبعير أو الجمل المعبد المهنوء بالقطران والسفينة المعبدة المقيرة","what_is_not_ar":"ليس استعباد الإنسان ولا العبادة ولا التكريم"},"support_links":["sup_7309fb3f9cd8c6e06413"]},{"boundary":"Dal, saygı ve hizmet gören kişiyi niteler; alçaltma, köleleştirme veya nesneyi işleme anlamı taşımaz.","branch_kind":"bare","branch_ref":"root_000973/B006","candidate_links":[{"candidate_id":"cand_7150c8229bead3f14f5d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَابِد","morph_features":"STEM|POS:N|ACT|PCPL|LEM:EaAbid|ROOT:Ebd|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:3:3:1","qac_word_ref":"109:3:3","surface_ar":"عَٰبِدُونَ"},{"lemma_ar":"عَبَدَ","morph_features":"STEM|POS:V|IMPF|LEM:Eabada|ROOT:Ebd|1S","morpheme_role":"STEM","pos":"V","qac_ref":"109:3:5:1","qac_word_ref":"109:3:5","surface_ar":"أَعْبُدُ"}],"gloss":"saygı gösterilip hizmet edilen kişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi çevresindekilerce saygıdeğer ve yüce tutulur."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu yüksek konumun sonucu olarak kişiye hizmet edilir."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin hem yüce tutulmasını hem de bu konum nedeniyle hizmet görmesini birlikte karşılar.","boundary_detail":"Dal, saygı ve hizmet gören kişiyi niteler; alçaltma, köleleştirme veya nesneyi işleme anlamı taşımaz.","branch_image_ar":"التكريم والتعظيم","concept_gloss":"saygı gösterilip hizmet edilen kişi","contextual_glosses":[{"applicability":"Bir kişinin yüksek saygınlığı ile kendisine sunulan hizmet birlikte vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yüceltilme ve hizmet görme yönlerini birlikte korur."},"facet_ids":["F001","F002"],"text":"yüceltilip hizmet edilen","usage_role":"contextual"}],"definition":"Kendisine saygı gösterilen, yüceltilen ve hizmet edilen kişidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi çevresindekilerce saygıdeğer ve yüce tutulur."},{"facet_id":"F002","role":"associated_use","statement":"Bu yüksek konumun sonucu olarak kişiye hizmet edilir."}],"identity_rationale":"Kaynak ifadesi nitelenen kişinin saygı gösterilen, yüceltilen ve hizmet edilen biri olduğunu açıkça belirtir. Bu anlam, benzer biçimin ezilmiş veya kullanıma hazırlanmış nesneyi nitelediği daldan karşıt bir değerle ayrılır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"saygı gösterilen, yüceltilen ve hizmet edilen kişi"}],"lexicalization_note":"Dal yalın bir niteleme anlamıdır; özel bir söz öbeğine bağlı ek kapsam gerektirmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yüksek değer kazanma ve sözle yüceltme dalları, kişi niteliği ile ettirgen eylem arasındaki sınırı gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yüksek tutulup hizmet edilen kişiyi niteler; komşu dal ise bir kişi, anı veya makamı yükseltme eylemini daha geniş kapsamda anlatır.","focus_only":"Odak dal kişinin saygı görmesi yanında kendisine hizmet edilmesini de içerir.","gloss":"saygı gören kişi ve değerini yükseltme","neighbor_only":"Komşu dal bir kişinin, anının veya makamın değerini yükseltme eylemine uzanır.","neighbor_ref":"root_000582/B002","relation_type":"near_synonym","shared_zone":"İki dal kişi veya makamın yüksek değer ve saygınlık kazanması alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal bir kişinin niteliği ve gördüğü muameledir; komşu dal ise övgü sözleriyle yüceltme eylemidir.","focus_only":"Odak dal kişinin saygın konumunu ve gördüğü hizmeti bildirir.","gloss":"saygın kişi ve sözle yüceltme","neighbor_only":"Komşu dal güzel nitelikleri sözle anıp yücelik yükleme eylemini bildirir.","neighbor_ref":"root_001398/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal birini yüksek ve değerli gösterme alanına bağlıdır."}],"source_phrase_ar":"المعبد المكرم والمعظم كأنه يعبد (jamhara)؛ المعبد أي معظما مخدوما (tahdhib)","source_summary":"Kaynaklar nitelemeyi saygı görme, yüceltilme ve hizmet edilme özelliklerini bir arada taşıyan kişi için kullanır.","sources":["JA","TA"],"what_is_ar":"يدخل فيه المعبد بمعنى المكرم والمعظم والمخدوم","what_is_not_ar":"ليس المعبد المذلل ولا الطريق الموطوء ولا البعير المطلي بالقطران"},"support_links":["sup_7309fb3f9cd8c6e06413"]},{"boundary":"Dal fiziksel güç, sağlamlık ve dayanıklılığı anlatır; toplumsal kölelik ya da duygusal öfke anlamı taşımaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000973/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَابِد","morph_features":"STEM|POS:N|ACT|PCPL|LEM:EaAbid|ROOT:Ebd|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:3:3:1","qac_word_ref":"109:3:3","surface_ar":"عَٰبِدُونَ"},{"lemma_ar":"عَبَدَ","morph_features":"STEM|POS:V|IMPF|LEM:Eabada|ROOT:Ebd|1S","morpheme_role":"STEM","pos":"V","qac_ref":"109:3:5:1","qac_word_ref":"109:3:5","surface_ar":"أَعْبُدُ"}],"gloss":"güç, sağlamlık ve dayanıklılık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel nitelik fiziksel güç ve sağlamlıktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kumaş bağlamında güç, kullanıma karşı dayanma ve kalıcılık olarak görünür."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dişi deve bağlamında güçlü yapıya semizlik de eklenir."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın niteliği, kumaştaki kalıcılığı ve devedeki güçlü yapıyı ortak çekirdekte karşılar.","boundary_detail":"Dal fiziksel güç, sağlamlık ve dayanıklılığı anlatır; toplumsal kölelik ya da duygusal öfke anlamı taşımaz.","branch_image_ar":"القوة والصلابة","concept_gloss":"güç, sağlamlık ve dayanıklılık","contextual_glosses":[{"applicability":"Niteliğin dişi deve için kullanıldığı ve güçle semizliğin birlikte anlatıldığı bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kumaşın dayanıklılığını ve yalın sağlamlık adını göstermez.","preserves":"Canlıdaki güçlü yapı ve semizlik görünümünü korur."},"facet_ids":["F001","F003"],"text":"güçlü ve semiz dişi deve","usage_role":"contextual"},{"applicability":"Bir kumaşın kullanım ve zaman karşısındaki gücünün sorgulandığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dişi deveye özgü güç ve semizlik görünümünü dışarıda bırakır.","preserves":"Gücün kalıcılık ve dayanma yönünü korur."},"facet_ids":["F001","F002"],"text":"kumaşın dayanıklılığı","usage_role":"contextual"}],"definition":"Bir varlığın güçlü, sağlam ve zaman içinde dayanıklı olmasıdır; dişi deve bağlamında bu sağlamlığa semizlik de eşlik eder.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel nitelik fiziksel güç ve sağlamlıktır."},{"facet_id":"F002","role":"extension","statement":"Kumaş bağlamında güç, kullanıma karşı dayanma ve kalıcılık olarak görünür."},{"facet_id":"F003","role":"specialization","statement":"Dişi deve bağlamında güçlü yapıya semizlik de eklenir."}],"identity_rationale":"Kaynak ifadesi çekirdeği güç ve sağlamlık olarak verir; dayanıklılık ve kalıcılık bunun zaman içindeki görünümü, dişi devedeki semizlik ise canlıya özgü belirti olarak sunulur. Bunlar kölelik veya boyun eğmeyle ilişkili değildir.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"güç, sağlamlık ve dayanıklılık"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"güçlü ve semiz dişi deve"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kumaşının hiç dayanıklılığı yok"}],"lexicalization_note":"Yalın güç adı ile deve ve kumaşa bağlı söz öbekleri birlikte bulunur; canlıya özgü semizlik bütün dalın genel anlamı yapılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; geniş güç alanı ve sert nesne niteliği, bu dalın dayanıklılık ile özel deve ve kumaş sınırını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal nesnenin veya hayvanın dayanıklı yapısıyla sınırlıdır; komşu dal ruhsal cesaretten zorlu koşullara kadar çok daha geniş bir güç alanı kurar.","focus_only":"Odak dal kumaşın kalıcılığına ve dişi devenin semiz gücüne bağlı özel kullanımları içerir.","gloss":"dayanıklı sağlamlık ve geniş güç alanı","neighbor_only":"Komşu dal cesaret, yürek sağlamlığı, zorlu durum, çaba ve acı gibi daha geniş güç ve şiddet alanlarına uzanır.","neighbor_ref":"root_000782/B002","relation_type":"near_synonym","shared_zone":"İki dal fiziksel güç, sertlik ve sağlamlık çekirdeğinde belirgin biçimde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal süre boyunca dayanmayı ve özel bağlamsal görünümleri kapsar; komşu dal doğrudan sert veya güçlü nesne niteliğidir.","focus_only":"Odak dal güçle birlikte dayanıklılık ve kalıcılığı, deve bağlamında semizliği içerir.","gloss":"dayanıklılık ve sert nesne","neighbor_only":"Komşu dal tek bir şeyi sert, güçlü veya kimi aktarımda uzun diye niteler.","neighbor_ref":"root_000188/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal somut bir varlığın güçlü ve sağlam oluşunu anlatabilir."}],"source_phrase_ar":"العبدة وهي القوة والصلابة (maqayis)؛ ناقة ذات عبدة أي ذات قوة وسمن وما لثوبك عبدة أي قوة (sihah)؛ العبدة البقاء وقيل الشدة (tahdhib)","source_summary":"Kaynaklar güç ve sağlamlık çekirdeğinde birleşir; bunu kumaşın dayanması ve dişi devenin güçlü, semiz yapısı üzerinden somutlaştırır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه العبدة بمعنى القوة والصلابة والشدة والبقاء والسمن في الناقة وقوة الثوب","what_is_not_ar":"ليس الذل والرق ولا الأنفة والغضب"},"support_links":[]},{"boundary":"Dal incinmiş gururdan yükselen öfke ile kederli iç duygulanımı kapsar; güç ve sağlamlık anlamından ayrıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000973/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَابِد","morph_features":"STEM|POS:N|ACT|PCPL|LEM:EaAbid|ROOT:Ebd|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:3:3:1","qac_word_ref":"109:3:3","surface_ar":"عَٰبِدُونَ"},{"lemma_ar":"عَبَدَ","morph_features":"STEM|POS:V|IMPF|LEM:Eabada|ROOT:Ebd|1S","morpheme_role":"STEM","pos":"V","qac_ref":"109:3:5:1","qac_word_ref":"109:3:5","surface_ar":"أَعْبُدُ"}],"gloss":"incinmiş gurur, öfke veya kederli iç duygulanım","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Duygu incinmiş gurur, onurunu koruma isteği ve öfke çevresinde oluşur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynak ifadesi anlamı keder ve yoğun iç sıkıntısına da uzatır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özel söz öbeğinde gururu incinen kişinin tepkisi susmak olur."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gurur ve öfke çekirdeğiyle kaynakta verilen kederli iç duygulanım uzantısını birlikte karşılar.","boundary_detail":"Dal incinmiş gururdan yükselen öfke ile kederli iç duygulanımı kapsar; güç ve sağlamlık anlamından ayrıdır.","branch_image_ar":"الأنفة والغضب","concept_gloss":"incinmiş gurur, öfke veya kederli iç duygulanım","contextual_glosses":[{"applicability":"Onur kırılmasının öfke ve kendini koruma tepkisi doğurduğu bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Keder ve yoğun iç sıkıntısı uzantısını tek başına göstermez.","preserves":"İncinmiş gurur ve öfke çekirdeğini korur."},"facet_ids":["F001"],"text":"gururu incinip öfkelenmek","usage_role":"contextual"},{"applicability":"İncinme tepkisinin susma olarak gerçekleştiği özel söz bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel öfke ve keder alanının tamamını kapsamaz.","preserves":"Gurur incinmesini ve bunun sonucundaki susmayı korur."},"facet_ids":["F001","F003"],"text":"gururu incindiği için sustu","usage_role":"contextual"}],"definition":"İncinmiş gurur ve kendini koruma duygusuyla yükselen öfke ya da içe çöken kederli duygulanımdır; özel kullanımda kişi bu incinme yüzünden susar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Duygu incinmiş gurur, onurunu koruma isteği ve öfke çevresinde oluşur."},{"facet_id":"F002","role":"extension","statement":"Kaynak ifadesi anlamı keder ve yoğun iç sıkıntısına da uzatır."},{"facet_id":"F003","role":"example","statement":"Özel söz öbeğinde gururu incinen kişinin tepkisi susmak olur."}],"identity_rationale":"Kaynak ifadesi incinmiş gurur, öfke ve kendini koruma duygusunu merkezde verir; ayrıca keder ve yoğun iç duygulanımı aktarır. Geçici çerçevedeki kaçırılmış şey için pişmanlık ayrıntısı kaynak cümlesinde açık değildir, bu yüzden tanım bu ek koşula bağlanmadan kurulmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"incinmiş gurur, öfke, keder veya iç sıkıntısı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"gururu incindiği için sustu"}],"lexicalization_note":"Yalın duygu adı ile gururu incindiği için susmayı anlatan söz öbeği birlikte bulunur; susma yalnız özel kullanımın sonucudur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; öfke ve onur çekirdeğine en yakın dal ile daha geniş duygulanım dalı, keder uzantısının sınırını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kaynak aktarımında kedere ve iç sıkıntısına açılır; komşu dalın merkezi daha sıkı biçimde gurur ve kızgınlıktır.","focus_only":"Odak dal öfkenin yanı sıra keder ve yoğun iç duygulanımı da kapsar.","gloss":"incinmiş gurur ve kabaran öfke","neighbor_only":"Komşu dal burunla ilişkilendirilen kendini koruma gururunu ve içte kabaran kızgınlığı özellikle vurgular.","neighbor_ref":"root_000358/B003","relation_type":"near_synonym","shared_zone":"İki dal incinmiş onur, kendini koruma duygusu ve öfke alanında büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dalın duygusal çekirdeği onur ve öfkeyle sınırlanır; komşu dal sevgiye ve özleme de uzanan daha genel bir duygulanım alanıdır.","focus_only":"Odak dal kederi incinmiş gurur ve öfke alanıyla birlikte taşır.","gloss":"gururlu öfke ve duygusal keder","neighbor_only":"Komşu dal kederin yanında sevgi, özlem ve başka duygusal yönelimleri de kapsar.","neighbor_ref":"root_001626/B004","relation_type":"near_neighbor","shared_zone":"İki dal yoğun iç duygulanım ve keder alanında kesişir."}],"source_phrase_ar":"العبد مثل الأنف والحمية (maqayis)؛ العبد الأنفة وعبدت فصمت أي أنفت فسكت (jamhara)؛ العبد بالتحريك الغضب والأنف والاسم العبدة (sihah)؛ العبد الأنف والحمية ويقال عبد عليه أي غضب والعبد الحزن والوجد (tahdhib)","source_summary":"Kaynaklar incinmiş gurur, öfke ve kendini koruma duygusunu ortak çekirdek yapar; bazı aktarımlar keder ve yoğun iç duygulanımı da aynı ad altında verir.","sources":["MQ","JA","SI","TA"],"what_is_ar":"يدخل فيه العبد والعبدة بمعنى الأنفة والحمية والغضب والحزن والوجد والندم عند فوات الشيء","what_is_not_ar":"ليس العبادة والطاعة الخاضعة ولا القوة والصلابة"},"support_links":[]},{"boundary":"Dal yalnız verilen iki söz öbeğinde gecikmeme veya biraz hızlanma bildirir; genel bir hız kökü gibi yorumlanmaz.","branch_kind":"collocation","branch_ref":"root_000973/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَابِد","morph_features":"STEM|POS:N|ACT|PCPL|LEM:EaAbid|ROOT:Ebd|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:3:3:1","qac_word_ref":"109:3:3","surface_ar":"عَٰبِدُونَ"},{"lemma_ar":"عَبَدَ","morph_features":"STEM|POS:V|IMPF|LEM:Eabada|ROOT:Ebd|1S","morpheme_role":"STEM","pos":"V","qac_ref":"109:3:5:1","qac_word_ref":"109:3:5","surface_ar":"أَعْبُدُ"}],"gloss":"gecikmeden yapmak veya koşuda biraz hızlanmak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İlk yapı, belirtilen işi yapmak için beklememeyi ve kısa sürede harekete geçmeyi bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İkinci yapı, koşunun hızını bir miktar artırmayı bildirir."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki yapıdaki farklı eylemleri yapı sınırlarını koruyarak birlikte temsil eder.","boundary_detail":"Dal yalnız verilen iki söz öbeğinde gecikmeme veya biraz hızlanma bildirir; genel bir hız kökü gibi yorumlanmaz.","branch_image_ar":"قلة اللبث وسرعة العدو","concept_gloss":"gecikmeden yapmak veya koşuda biraz hızlanmak","contextual_glosses":[{"applicability":"Bir kişinin belirtilen işi beklemeden gerçekleştirdiğini bildiren yapı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Koşuda biraz hızlanma okumasını dışarıda bırakır.","preserves":"İşi yapmak için oyalanmama ve gecikmeme yönünü korur."},"facet_ids":["F001"],"text":"yapmakta gecikmedi","usage_role":"contextual"},{"applicability":"Koşunun bir miktar hızlandığını anlatan yapı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir işi yapmakta gecikmeme okumasını dışarıda bırakır.","preserves":"Koşuda sınırlı hız artışı yönünü korur."},"facet_ids":["F002"],"text":"koşarken biraz hızlandı","usage_role":"contextual"}],"definition":"Verilen bir söz öbeğinde bir işi yapmakta hiç gecikmemeyi, diğerinde ise koşarken bir ölçü hızlanmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İlk yapı, belirtilen işi yapmak için beklememeyi ve kısa sürede harekete geçmeyi bildirir."},{"facet_id":"F002","role":"source_variant","statement":"İkinci yapı, koşunun hızını bir miktar artırmayı bildirir."}],"identity_rationale":"Kaynak ifadesi iki ayrı söz öbeğine bağlı anlam verir: bir işi yapmakta gecikmemek ve koşarken bir ölçü hızlanmak. Bunlar tek bir yalın eylem anlamına indirgenemez, fakat dal iki yapı açıkça ayrılarak korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"yapmakta gecikmedi"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"koşarken biraz hızlandı"}],"lexicalization_note":"Bütün anlam söz öbeklerine bağlıdır; gecikmeme ve koşuda biraz hızlanma okumaları yalın biçime genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hızlanma yönünü aynı ölçülülükle veren komşu, söz öbeğine bağlı kapsamı açıklayan en keskin karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Hızlanma yönü bakımından yakındırlar, ancak odak dal iki özel yapıya bağlıdır ve ayrıca gecikmeme anlamı taşır; komşu dal doğrudan hızlı hareket alanındadır.","focus_only":"Odak dal hızlanma yapısının yanında bir işi yapmakta gecikmeme yapısını da içerir.","gloss":"biraz hızlanma ve hızlı hareket","neighbor_only":"Komşu dal hızlı geçip gitme kullanımını da doğrudan hareket hızı alanında taşır.","neighbor_ref":"root_001445/B008","relation_type":"near_synonym","shared_zone":"İki dal koşuda veya geçişte belirli ölçüde hız kazanmayı anlatır."}],"source_phrase_ar":"ما عبد أن فعل ذاك أي ما لبث (sihah;tahdhib)؛ عبد يعدو إذا أسرع بعض الإسراع (tahdhib)","source_summary":"Toplu kaynak ifadesi, gecikmeden yapma ile koşuda biraz hızlanma okumalarını iki ayrı yapıya bağlar; ortak bir yalın anlam ileri sürmez.","sources":["SI","TA"],"what_is_ar":"يدخل فيه ما عبد أن فعل أي ما لبث وعبد يعدو إذا أسرع بعض الإسراع","what_is_not_ar":"ليس العبادة ولا الغضب ولا العطب"},"support_links":[]},{"boundary":"Dal insan, nesne veya yolların ayrı yönlere dağılmışlığını bildirir; kölelerin çoğul adı değildir.","branch_kind":"bare","branch_ref":"root_000973/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَابِد","morph_features":"STEM|POS:N|ACT|PCPL|LEM:EaAbid|ROOT:Ebd|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:3:3:1","qac_word_ref":"109:3:3","surface_ar":"عَٰبِدُونَ"},{"lemma_ar":"عَبَدَ","morph_features":"STEM|POS:V|IMPF|LEM:Eabada|ROOT:Ebd|1S","morpheme_role":"STEM","pos":"V","qac_ref":"109:3:5:1","qac_word_ref":"109:3:5","surface_ar":"أَعْبُدُ"}],"gloss":"her yana dağılmış kümeler, nesneler veya yollar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birlik oluşturan öğeler birbirinden ayrılır ve değişik yönlere dağılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dağılmış öğeler insan kümeleri, nesneler, uzak uçlar veya farklı yollar olabilir."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dağılma yönünü ve kaynakta sayılan insan, nesne ve yol türlerini birlikte karşılar.","boundary_detail":"Dal insan, nesne veya yolların ayrı yönlere dağılmışlığını bildirir; kölelerin çoğul adı değildir.","branch_image_ar":"التفرق في الوجوه","concept_gloss":"her yana dağılmış kümeler, nesneler veya yollar","contextual_glosses":[{"applicability":"Adlandırmanın farklı yönlere gitmiş insan grupları için kullanıldığı bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesneler, uzak uçlar ve farklı yollar için kullanımı göstermez.","preserves":"İnsan kümelerinin birbirinden ayrılarak her yana gitmesini korur."},"facet_ids":["F001","F002"],"text":"her yöne dağılmış insan kümeleri","usage_role":"contextual"},{"applicability":"Adlandırmanın çeşitli yönlere uzanan yolları gösterdiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan kümeleri ve dağınık nesneler için kullanımı dışarıda bırakır.","preserves":"Yolların birbirinden ayrılıp farklı yönlere uzanmasını korur."},"facet_ids":["F001","F002"],"text":"birbirinden ayrılan farklı yollar","usage_role":"contextual"}],"definition":"İnsan kümelerinin, nesnelerin, uzak uçların veya yolların birbirinden ayrılarak çeşitli yönlere dağılmış olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birlik oluşturan öğeler birbirinden ayrılır ve değişik yönlere dağılır."},{"facet_id":"F002","role":"extension","statement":"Dağılmış öğeler insan kümeleri, nesneler, uzak uçlar veya farklı yollar olabilir."}],"identity_rationale":"Kaynak ifadesi insan kümeleri, nesneler, uzak uçlar ve farklı yollar için ortak olarak birbirinden ayrılıp çeşitli yönlere dağılma görüntüsünü verir. Bunlar köle adının çoğulları değil, dağınıklığı anlatan ayrı adlandırmalardır.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"her yana dağılmış insan kümeleri, nesneler veya yollar"}],"lexicalization_note":"Dal yalın bir çoğul adlandırmadır; özel bir söz öbeğinden alınmış ek kapsam içermez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel olarak her yöne dağılan topluluk ile daha geniş ayrışma dalı, bu adlandırmanın sonuç ve kapsam sınırını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sonuçtaki dağınık kümeleri ve insan dışı öğeleri adlandırabilir; komşu dal topluluğun dağılma olayına bağlı özel bir anlatımdır.","focus_only":"Odak dal insan kümeleri yanında nesneleri, uzak uçları ve farklı yolları da adlandırır.","gloss":"her yana dağılmış öğeler ve dağılan topluluk","neighbor_only":"Komşu dal belirli bir kalıp içinde bir topluluğun her yöne gitme olayını anlatır.","neighbor_ref":"root_000231/B006","relation_type":"near_synonym","shared_zone":"İki dal insanların her yönde birbirinden ayrılıp dağılması görüntüsünde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal yönlere yayılmış insan, nesne ve yolların durumudur; komşu dal ettirgen dağıtmadan soyut farklılaşmaya kadar daha geniştir.","focus_only":"Odak dal uzak uçlar ve farklı yönlere uzanan yollar gibi somut dağınık öğeleri özellikle kapsar.","gloss":"yönlere dağılmışlık ve genel ayrışma","neighbor_only":"Komşu dal topluluğu dağıtma eylemine, türlerin ve gönüllerin farklılaşmasına kadar uzanır.","neighbor_ref":"root_000775/B001","relation_type":"near_synonym","shared_zone":"İki dal bir bütünün parçalarının ayrılması ve dağılması alanını paylaşır."}],"source_phrase_ar":"العباديد الفرق من الناس الذاهبون في كل وجه وكذلك العبابيد (sihah)؛ العباديد والعبابيد الأطراف البعيدة والأشياء المتفرقة والطرق المختلفة (tahdhib)","source_summary":"Kaynaklar ortak biçimde her yana dağılma ve birbirinden uzaklaşma görüntüsünü verir; kapsam insan topluluklarından nesnelere ve yollara kadar uzanır.","sources":["SI","TA"],"what_is_ar":"يدخل فيه العباديد والعبابيد للفرق من الناس أو الأشياء أو الطرق المتفرقة الذاهبة في كل وجه","what_is_not_ar":"ليس جمع العبد المملوك ولا أسماء القبائل"},"support_links":[]},{"boundary":"Dal bineğe bağlı yolda kalma ve güçlükle direnen deve kullanımlarıyla sınırlıdır; genel yorgunluk veya nesneyi uysallaştırma anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000973/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَابِد","morph_features":"STEM|POS:N|ACT|PCPL|LEM:EaAbid|ROOT:Ebd|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:3:3:1","qac_word_ref":"109:3:3","surface_ar":"عَٰبِدُونَ"},{"lemma_ar":"عَبَدَ","morph_features":"STEM|POS:V|IMPF|LEM:Eabada|ROOT:Ebd|1S","morpheme_role":"STEM","pos":"V","qac_ref":"109:3:5:1","qac_word_ref":"109:3:5","surface_ar":"أَعْبُدُ"}],"gloss":"bineği yüzünden yolda kalma veya güçlükle direnen deve","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yolcunun ilerleyememesi, bineğinin yorulması, zarar görmesi veya ortadan kaybolması sonucudur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Deve nitelemesi, hayvanın insanlara karşı güçlükle direnip kolayca boyun eğmemesini bildirir."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yolcu sonucunu ve deve niteliğini iki yapı sınırını koruyarak birlikte temsil eder.","boundary_detail":"Dal bineğe bağlı yolda kalma ve güçlükle direnen deve kullanımlarıyla sınırlıdır; genel yorgunluk veya nesneyi uysallaştırma anlamı değildir.","branch_image_ar":"العطب والانقطاع","concept_gloss":"bineği yüzünden yolda kalma veya güçlükle direnen deve","contextual_glosses":[{"applicability":"Bineğin yorulması, zarar görmesi veya kaybı yüzünden yolculuğun kesildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsanlara güçlük çıkararak direnen deve nitelemesini dışarıda bırakır.","preserves":"Binek kaynaklı ilerleyememe ve yolda kalma sonucunu korur."},"facet_ids":["F001"],"text":"bineği elden çıkınca yolda kaldı","usage_role":"contextual"},{"applicability":"Hayvanın insanlara karşı dirençli ve kolay yönetilemez oluşunu bildiren yapıda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Binek kaybı veya tükenmesi yüzünden yolda kalma olayını göstermez.","preserves":"Devenin güçlük çıkarma ve direnme niteliğini korur."},"facet_ids":["F002"],"text":"insanlara güçlükle direnen deve","usage_role":"contextual"}],"definition":"Bir yapıda yolcunun bineği yorulduğu, zarar gördüğü veya elden çıktığı için yolda kalması; diğerinde ise devenin insanlara güçlük çıkararak direnmesi anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yolcunun ilerleyememesi, bineğinin yorulması, zarar görmesi veya ortadan kaybolması sonucudur."},{"facet_id":"F002","role":"source_variant","statement":"Deve nitelemesi, hayvanın insanlara karşı güçlükle direnip kolayca boyun eğmemesini bildirir."}],"identity_rationale":"Kaynak ifadesi, yolcunun bineği yorulduğu, zarar gördüğü veya ortadan kaybolduğu için yolda kalmasını anlatan yapı ile insanlara güçlük çıkararak direnen deve nitelemesini birlikte verir. Bu iki kullanım aynı dalda tutulabilir, ancak genel bir bozulma veya yorgunluk anlamı gibi birleştirilemez.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"bineği yorulduğu, zarar gördüğü veya kaybolduğu için yolda kaldı"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"insanlara güçlük çıkararak direnen deve"}],"lexicalization_note":"Yolda kalmayı anlatan kalıpla güç deve nitelemesi birlikte bulunur; iki yapı kendi katılımcıları ve sonuçlarıyla ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel binek tükenmesi ile geride kalan yorgun binek dalları, yolcu sonucu ve dirençli deve uzantısının sınırını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli yapıda binek kaybı sonucunu ve güç deveyi taşır; komşu dal yorgunluk, arıza ve soyut yetersizlikleri daha geniş kapsamda anlatır.","focus_only":"Odak dal ayrıca insanlara güçlük çıkararak direnen deve nitelemesini içerir.","gloss":"binek yüzünden yolda kalma ve genel tükenme","neighbor_only":"Komşu dal bineğin topallaması, zayıflaması ve çeşitli soyut yetersizlikler gibi daha geniş kesilme alanlarına uzanır.","neighbor_ref":"root_000094/B004","relation_type":"near_synonym","shared_zone":"İki dal bineğin yorulması veya zarar görmesi yüzünden yolculuğun kesilmesinde belirgin biçimde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal yolcunun yolda kalmasına odaklanır ve kayıp ile dirençli deveyi de içerir; komşu dal doğrudan bineklerin geride kalma durumudur.","focus_only":"Odak dal bineğin kaybolması veya zarar görmesini ve ayrı bir dirençli deve nitelemesini de kapsar.","gloss":"yolda kalma ve geride kalan yorgun binek","neighbor_only":"Komşu dal yorgun bineklerin geride kalması ve sürüye yetişememesi sonucunu özellikle bildirir.","neighbor_ref":"root_000520/B006","relation_type":"near_neighbor","shared_zone":"İki dal yorgunluk nedeniyle bineğin ilerleyememesi alanında kesişir."}],"source_phrase_ar":"أعبد بفلان بمعنى أبدع به إذا كلت راحلته أو عطبت (sihah)؛ أعبد به إذا ذهبت راحلته وكذلك أبدع به (tahdhib)؛ بعير متعبد ومتأبد إذا امتنع على الناس صعوبة (tahdhib)","source_summary":"Toplu kaynak ifadesi, bineğin yorulması, zarar görmesi veya kaybıyla yolculuğun kesilmesini; ayrıca insanlara güçlük çıkaran dirençli deveyi ayrı yapılarda aktarır.","sources":["SI","TA"],"what_is_ar":"يدخل فيه أعبد بفلان أو أعبد به بمعنى أبدع به إذا كلت راحلته أو عطبت أو ذهبت ويدخل فيه البعير المتعبد الممتنع صعوبة","what_is_not_ar":"ليس التعبيد بمعنى التذليل ولا عبد يعدو بمعنى أسرع"},"support_links":[]},{"boundary":"Dal güzel koku hazırlamada kullanılan ezme aracını adlandırır; koku maddesinin kendisini, kokuyu veya güç niteliğini bildirmez.","branch_kind":"bare","branch_ref":"root_000973/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَابِد","morph_features":"STEM|POS:N|ACT|PCPL|LEM:EaAbid|ROOT:Ebd|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:3:3:1","qac_word_ref":"109:3:3","surface_ar":"عَٰبِدُونَ"},{"lemma_ar":"عَبَدَ","morph_features":"STEM|POS:V|IMPF|LEM:Eabada|ROOT:Ebd|1S","morpheme_role":"STEM","pos":"V","qac_ref":"109:3:5:1","qac_word_ref":"109:3:5","surface_ar":"أَعْبُدُ"}],"gloss":"güzel koku maddesi ezme taşı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Araç, güzel koku maddelerini ezme ve hazırlama işinde kullanılır."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Aracın biçiminden çok güzel koku hazırlamadaki ezme işlevini açık ve doğal biçimde belirtir.","boundary_detail":"Dal güzel koku hazırlamada kullanılan ezme aracını adlandırır; koku maddesinin kendisini, kokuyu veya güç niteliğini bildirmez.","branch_image_ar":"صَلاءة الطيب","concept_gloss":"güzel koku maddesi ezme taşı","contextual_glosses":[{"applicability":"Güzel koku maddelerinin ezilip karıştırıldığı araç bağlamında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Koku maddelerini ezme ve hazırlama işlevini araç niteliğiyle birlikte korur."},"facet_ids":["F001"],"text":"koku hazırlama havanı","usage_role":"contextual"}],"definition":"Güzel koku maddelerinin ezilip karıştırılarak hazırlanmasında kullanılan taş ya da havandır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Araç, güzel koku maddelerini ezme ve hazırlama işinde kullanılır."}],"identity_rationale":"Tek kaynak ifadesi sözcüğü güzel koku maddelerinin ezilip hazırlanmasında kullanılan taş veya havan olarak adlandırır. Bu araç anlamı, aynı biçimin güç ve duygulanım dallarından bütünüyle ayrıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"güzel koku maddelerini ezme taşı"}],"lexicalization_note":"Dal yalın bir araç adıdır; özel bir söz öbeğine bağlı ek anlam taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; koku maddeleri ile tütsü odunu ve kabı, ezme aracının aynı alandaki farklı işlevini en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal işleme aracıdır; komşu dal ise o araçla işlenebilecek kokulu maddeler ve karışım bileşenleridir.","focus_only":"Odak dal güzel koku maddelerini ezip hazırlamaya yarayan aracı adlandırır.","gloss":"koku hazırlama aracı ve koku maddeleri","neighbor_only":"Komşu dal güzel koku karışımına giren maddeleri ve kokulu malzemeleri adlandırır.","neighbor_ref":"root_001190/B005","relation_type":"same_field","shared_zone":"İki dal güzel koku hazırlama işi ve bu işte kullanılan nesneler alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal ezme ve karıştırma aşamasına aittir; komşu dal kokulu odunun yakılması ve dumanının çıkarılması aşamasına aittir.","focus_only":"Odak dal koku maddelerini ezmeye yarayan taş veya havandır.","gloss":"koku ezme taşı ve tütsü aracı","neighbor_only":"Komşu dal yakılan güzel kokulu odunu ve onun konduğu tütsü kabını kapsar.","neighbor_ref":"root_001238/B007","relation_type":"same_field","shared_zone":"İki dal kokulu madde hazırlama veya kullanma araçları çevresinde yer alır."}],"source_phrase_ar":"العبدة صلاءة الطيب (jamhara)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu adlandırma yalnız bir kaynakta, güzel koku maddelerini ezmeye yarayan araç anlamıyla aktarılır."}],"source_summary":"Tek kaynak aktarımı, sözcüğü güzel koku maddelerinin hazırlanmasında kullanılan ezme taşı veya havan olarak verir.","sources":["JA"],"what_is_ar":"يدخل فيه العبدة اسما لصَلاءة الطيب","what_is_not_ar":"ليس العبدة بمعنى القوة ولا الأنفة"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["109:3:1"],"branch_refs":[],"candidate_id":"cand_68805b28f8c1d4fe4c10","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:1:coordinated-second-panel","source_type":"word_analysis","support_ids":["sup_78c42d41e8e123d96450","sup_960baee9d0b03277f7f5"],"title":"coordination makes a second denial panel","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:1","qac_refs":["109:3:1:1"],"status":"accepted"}},{"anchor_refs":["109:3:1"],"branch_refs":[],"candidate_id":"cand_d94ccc5c284f13eab923","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:1:fused-negative-refrain","source_type":"word_analysis","support_ids":["sup_960baee9d0b03277f7f5","sup_f65dc4ac148ded65bd30"],"title":"connection and negation are fused","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:1","qac_refs":["109:3:1:1"],"status":"accepted"}},{"anchor_refs":["109:3:1"],"branch_refs":[],"candidate_id":"cand_7235349b11f07933190b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:1:open-vowel-frame","source_type":"word_analysis","support_ids":["sup_3f731811d9e86480a188","sup_960baee9d0b03277f7f5"],"title":"open vowel links negation and object marker","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:1","qac_refs":["109:3:1:1"],"status":"accepted"}},{"anchor_refs":["109:3:1"],"branch_refs":[],"candidate_id":"cand_00d07b479f19cac6b37c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:1:unlike-clause-types","source_type":"word_analysis","support_ids":["sup_2ffa754836df2a8fedd5","sup_960baee9d0b03277f7f5"],"title":"verbal clause joins nominal clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:1","qac_refs":["109:3:1:1"],"status":"accepted"}},{"anchor_refs":["109:3:2"],"branch_refs":[],"candidate_id":"cand_2ef47dbb26b8dca6531f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:2:categorical-separation","source_type":"word_analysis","support_ids":["sup_0366e6375273ab0e8bd8","sup_4892f9fa52e2e908b94a"],"title":"the denial excludes shared relation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:2","qac_refs":["109:3:1:2"],"status":"accepted"}},{"anchor_refs":["109:3:2"],"branch_refs":[],"candidate_id":"cand_2fe39c5351cb134b617e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:2:nominal-negation-scope","source_type":"word_analysis","support_ids":["sup_4892f9fa52e2e908b94a","sup_e1b355c2a92be98678f7"],"title":"negation scopes over identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:2","qac_refs":["109:3:1:2"],"status":"accepted"}},{"anchor_refs":["109:3:2"],"branch_refs":[],"candidate_id":"cand_35870401d899fec0a799","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:2:surah-denial-refrain","source_type":"word_analysis","support_ids":["sup_4892f9fa52e2e908b94a","sup_e95292844245a1c841f1"],"title":"negative particle recurs as refrain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:2","qac_refs":["109:3:1:2"],"status":"accepted"}},{"anchor_refs":["109:3:2"],"branch_refs":[],"candidate_id":"cand_250ade7ac4945c8b2d41","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:2:weighted-negation-sound","source_type":"word_analysis","support_ids":["sup_38c5bcdd950b4726e309","sup_4892f9fa52e2e908b94a"],"title":"long negation is audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:2","qac_refs":["109:3:1:2"],"status":"accepted"}},{"anchor_refs":["109:3:3"],"branch_refs":[],"candidate_id":"cand_190d09607314e9e0a858","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:3:addressee-under-denial","source_type":"word_analysis","support_ids":["sup_3f6ddaac9f74932f4f2a","sup_7d23934cc363872541ed"],"title":"the named group bears the denial","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:3","qac_refs":["109:3:2:1"],"status":"accepted"}},{"anchor_refs":["109:3:3"],"branch_refs":[],"candidate_id":"cand_256ed0dffb83d14c4a10","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:3:explicit-subject-spotlight","source_type":"word_analysis","support_ids":["sup_151ec6869666703ee529","sup_3f6ddaac9f74932f4f2a"],"title":"explicit pronoun spotlights the addressees","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:3","qac_refs":["109:3:2:1"],"status":"accepted"}},{"anchor_refs":["109:3:3"],"branch_refs":[],"candidate_id":"cand_a9e92b8b20ce311ae062","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:3:nasal-local-binding","source_type":"word_analysis","support_ids":["sup_3f6ddaac9f74932f4f2a","sup_a1ff4c558681a597246c"],"title":"nasal sound binds subject and object clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:3","qac_refs":["109:3:2:1"],"status":"accepted"}},{"anchor_refs":["109:3:3"],"branch_refs":[],"candidate_id":"cand_d505f4f90a5d4ba618b7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:3:participant-prominence-reversal","source_type":"word_analysis","support_ids":["sup_3f6ddaac9f74932f4f2a","sup_be6ab934df70c153416c"],"title":"speaker and addressees trade prominence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:3","qac_refs":["109:3:2:1"],"status":"accepted"}},{"anchor_refs":["109:3:3"],"branch_refs":[],"candidate_id":"cand_f6268bf4b78185f83b88","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:3:same-surah-panel-anchor","source_type":"word_analysis","support_ids":["sup_3f6ddaac9f74932f4f2a","sup_4442d24de4cb0e57196c"],"title":"pronoun returns as panel anchor","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:3","qac_refs":["109:3:2:1"],"status":"accepted"}},{"anchor_refs":["109:3:4"],"branch_refs":[],"candidate_id":"cand_3d3bcbcc3ce4762072ae","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"109:3:4:act-to-identity-register-shift","source_type":"word_analysis","support_ids":["sup_354ebfa093721722e037","sup_6ba96717ccbf89bc5e0b"],"title":"boundary shifts from act to identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:4","qac_refs":["109:3:3:1"],"status":"accepted"}},{"anchor_refs":["109:3:4"],"branch_refs":[],"candidate_id":"cand_26d08b426b3826e321fd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"109:3:4:derivational-boundary","source_type":"word_analysis","support_ids":["sup_354ebfa093721722e037","sup_cf5604d8e73b6f259963"],"title":"basic participle avoids causative enslavement","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:4","qac_refs":["109:3:3:1"],"status":"accepted"}},{"anchor_refs":["109:3:4"],"branch_refs":[],"candidate_id":"cand_c8afb7e280d6dd67e2bb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"109:3:4:hinge-position","source_type":"word_analysis","support_ids":["sup_354ebfa093721722e037","sup_63522807a8e7712bfd92"],"title":"predicate hinges subject to object clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:4","qac_refs":["109:3:3:1"],"status":"accepted"}},{"anchor_refs":["109:3:4"],"branch_refs":[],"candidate_id":"cand_4f2e779e9612a8edcf6d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"109:3:4:identity-not-action","source_type":"word_analysis","support_ids":["sup_354ebfa093721722e037","sup_977f141c2ab18e7509a8"],"title":"participle denies identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:4","qac_refs":["109:3:3:1"],"status":"accepted"}},{"anchor_refs":["109:3:4"],"branch_refs":[],"candidate_id":"cand_eb38b1d329854066cb6a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"109:3:4:local-sound-cohesion","source_type":"word_analysis","support_ids":["sup_31cab2da5fead936d3d3","sup_354ebfa093721722e037"],"title":"sound echo binds identity and action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:4","qac_refs":["109:3:3:1"],"status":"accepted"}},{"anchor_refs":["109:3:4"],"branch_refs":[],"candidate_id":"cand_075047d12ac8de6003de","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"109:3:4:marked-participle-pathway","source_type":"word_analysis","support_ids":["sup_354ebfa093721722e037","sup_cb882d6ca78b582179b2"],"title":"marked form inside a common root","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:4","qac_refs":["109:3:3:1"],"status":"accepted"}},{"anchor_refs":["109:3:4"],"branch_refs":[],"candidate_id":"cand_6ff22a5c339128773b60","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"109:3:4:predicate-agreement-and-object","source_type":"word_analysis","support_ids":["sup_354ebfa093721722e037","sup_35e525393fbdad932344"],"title":"predicate agrees and governs","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:4","qac_refs":["109:3:3:1"],"status":"accepted"}},{"anchor_refs":["109:3:4"],"branch_refs":[],"candidate_id":"cand_55e66912dbf22aa9d0da","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"109:3:4:recitational-surface","source_type":"word_analysis","support_ids":["sup_354ebfa093721722e037","sup_36c655bd76c91427b795"],"title":"surface sound sustains the identity term","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:4","qac_refs":["109:3:3:1"],"status":"accepted"}},{"anchor_refs":["109:3:4"],"branch_refs":[],"candidate_id":"cand_f5d48978f62d9e8e56e0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"109:3:4:root-echo-and-refrain","source_type":"word_analysis","support_ids":["sup_354ebfa093721722e037","sup_5c8f922089f757198c37"],"title":"same root returns in changed roles","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:4","qac_refs":["109:3:3:1"],"status":"accepted"}},{"anchor_refs":["109:3:4"],"branch_refs":[],"candidate_id":"cand_6aa4baf17136d0427cf2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"109:3:4:root-submission-pressure","source_type":"word_analysis","support_ids":["sup_354ebfa093721722e037","sup_6bfd52ca0cf4d358af05"],"title":"submission field thickens worshipper-status","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:4","qac_refs":["109:3:3:1"],"status":"accepted"}},{"anchor_refs":["109:3:5"],"branch_refs":[],"candidate_id":"cand_688ec8cb56fc3329ea72","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:5:devotion-field-through-mode-reading","source_type":"word_analysis","support_ids":["sup_97e0d45e654cae28efdc","sup_c6cf5c1c087230337be9"],"title":"mode reading invokes worship-field pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:5","qac_refs":["109:3:4:1"],"status":"accepted"}},{"anchor_refs":["109:3:5"],"branch_refs":[],"candidate_id":"cand_152f0788abf6b1f3cc04","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:5:interrogative-distance","source_type":"word_analysis","support_ids":["sup_97e0d45e654cae28efdc","sup_9f8bb2c70336834ed179"],"title":"interrogative coloring remains secondary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:5","qac_refs":["109:3:4:1"],"status":"accepted"}},{"anchor_refs":["109:3:5"],"branch_refs":[],"candidate_id":"cand_3120dab9655dee2f2e70","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:5:object-expression-under-predicate","source_type":"word_analysis","support_ids":["sup_705c4b061b443f68329d","sup_97e0d45e654cae28efdc"],"title":"marker supplies the governed object expression","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:5","qac_refs":["109:3:4:1"],"status":"accepted"}},{"anchor_refs":["109:3:5"],"branch_refs":[],"candidate_id":"cand_7dc3ceb27354b794d7ec","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:5:object-or-mode-ambiguity","source_type":"word_analysis","support_ids":["sup_97e0d45e654cae28efdc","sup_e22e80edf1afed6f7b6a"],"title":"one marker keeps object and mode live","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:5","qac_refs":["109:3:4:1"],"status":"accepted"}},{"anchor_refs":["109:3:5"],"branch_refs":[],"candidate_id":"cand_9fc8194a3393795d3da2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:5:open-vowel-echo","source_type":"word_analysis","support_ids":["sup_97e0d45e654cae28efdc","sup_ed0a16435400af66fe0d"],"title":"long vowel echoes the negator","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:5","qac_refs":["109:3:4:1"],"status":"accepted"}},{"anchor_refs":["109:3:5"],"branch_refs":[],"candidate_id":"cand_6ae385488d8521463efe","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:5:open-what-not-who","source_type":"word_analysis","support_ids":["sup_97e0d45e654cae28efdc","sup_bb57b1bcaf689778417a"],"title":"open what-reference avoids personal narrowing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:5","qac_refs":["109:3:4:1"],"status":"accepted"}},{"anchor_refs":["109:3:5"],"branch_refs":[],"candidate_id":"cand_d8f8b87cdc06d2dea9f7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:5:reciprocal-ma-bridge","source_type":"word_analysis","support_ids":["sup_7020a487226680ffcbd6","sup_97e0d45e654cae28efdc"],"title":"marker bridges reciprocal panels","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:5","qac_refs":["109:3:4:1"],"status":"accepted"}},{"anchor_refs":["109:3:5"],"branch_refs":[],"candidate_id":"cand_0f2bf479f89ff26c0646","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:3:5:relative-reading-with-recovered-object","source_type":"word_analysis","support_ids":["sup_97e0d45e654cae28efdc","sup_b81f38a7d65c43bc522b"],"title":"relative reading recovers the object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:5","qac_refs":["109:3:4:1"],"status":"accepted"}},{"anchor_refs":["109:3:6"],"branch_refs":[],"candidate_id":"cand_6451c57472f3d5234e52","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"109:3:6:dominant-imperfect-pathway","source_type":"word_analysis","support_ids":["sup_310cca33fe6ce2870290","sup_de90e43c18ac35bd7af3"],"title":"speaker uses the dominant verbal pathway","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:6","qac_refs":["109:3:5:1"],"status":"accepted"}},{"anchor_refs":["109:3:6"],"branch_refs":[],"candidate_id":"cand_cbf991be9bc65b6c4cba","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"109:3:6:final-measure","source_type":"word_analysis","support_ids":["sup_de90e43c18ac35bd7af3","sup_f344ac56bb3885bfb2b2"],"title":"closing verb becomes the measure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:6","qac_refs":["109:3:5:1"],"status":"accepted"}},{"anchor_refs":["109:3:6"],"branch_refs":[],"candidate_id":"cand_8603cec0e611efbc4f53","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"109:3:6:first-person-embedded-prominence","source_type":"word_analysis","support_ids":["sup_67e9472e2ed7d69c3c36","sup_de90e43c18ac35bd7af3"],"title":"speaker is present inside the clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:6","qac_refs":["109:3:5:1"],"status":"accepted"}},{"anchor_refs":["109:3:6"],"branch_refs":[],"candidate_id":"cand_4fdc36be2a0cb61e964b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"109:3:6:form-one-boundary","source_type":"word_analysis","support_ids":["sup_cb0e58a5621725a201bc","sup_de90e43c18ac35bd7af3"],"title":"basic Form I avoids specialized alternatives","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:6","qac_refs":["109:3:5:1"],"status":"accepted"}},{"anchor_refs":["109:3:6"],"branch_refs":[],"candidate_id":"cand_f20dfaccd06b383ddaba","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"109:3:6:local-root-sound-echo","source_type":"word_analysis","support_ids":["sup_4e42728b2af93409b71e","sup_de90e43c18ac35bd7af3"],"title":"root sound ties predicate to verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:6","qac_refs":["109:3:5:1"],"status":"accepted"}},{"anchor_refs":["109:3:6"],"branch_refs":[],"candidate_id":"cand_c0cfb535e8e8cfc8c553","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"109:3:6:ongoing-first-person-action","source_type":"word_analysis","support_ids":["sup_3bcafe193026e7f31e31","sup_de90e43c18ac35bd7af3"],"title":"imperfect marks ongoing speaker worship","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:6","qac_refs":["109:3:5:1"],"status":"accepted"}},{"anchor_refs":["109:3:6"],"branch_refs":[],"candidate_id":"cand_9c03b697e7791df1a303","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"109:3:6:root-devotion-submission","source_type":"word_analysis","support_ids":["sup_6e2c8df2cd3f9e5c3774","sup_de90e43c18ac35bd7af3"],"title":"root field makes worship submitted devotion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:6","qac_refs":["109:3:5:1"],"status":"accepted"}},{"anchor_refs":["109:3:6"],"branch_refs":[],"candidate_id":"cand_b8c10ed66c466047a048","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"109:3:6:surah-root-thread","source_type":"word_analysis","support_ids":["sup_1be9fea92d07e96101ef","sup_de90e43c18ac35bd7af3"],"title":"worship root threads through the surah","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:6","qac_refs":["109:3:5:1"],"status":"accepted"}},{"anchor_refs":["109:3:6"],"branch_refs":[],"candidate_id":"cand_dbafbedabb047c71b8b1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"109:3:6:transitive-recovered-object","source_type":"word_analysis","support_ids":["sup_de90e43c18ac35bd7af3","sup_defd6032bf4eb0f2d91e"],"title":"worship is directed, not objectless","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:3:6","qac_refs":["109:3:5:1"],"status":"accepted"}},{"anchor_refs":["109:3:3"],"branch_refs":[],"candidate_id":"cand_3d11616cff7a1e3584b6","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"109:3:3:1","source_type":"qac_morpheme","support_ids":["sup_7b594288f2955471d943"],"title":"QAC root occurrence: ع ب د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["109:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"109:3","branch_refs":["root_000973/B003"],"candidate_id":"cand_4afebc1b5f392f28652a","commentary_obligation":"review","hft_ref":"hft_589d2d3aa4df74652933","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_devotional_relation","source_type":"hft","support_ids":["sup_74874eb41af4fb5819f2"],"title":"baseline_devotional_relation","trust":"legacy_unbound"},{"anchor_refs":["109:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"109:3","branch_refs":["root_000973/B001","root_000973/B004"],"candidate_id":"cand_bf82e5441a1d7719e35b","commentary_obligation":"review","hft_ref":"hft_8d7efeb988598b1f9b6b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_master_service_relation","source_type":"hft","support_ids":["sup_85f9ebc7d6564cbecf79"],"title":"baseline_master_service_relation","trust":"legacy_unbound"},{"anchor_refs":["109:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"109:3","branch_refs":["root_000973/B005","root_000973/B006"],"candidate_id":"cand_7150c8229bead3f14f5d","commentary_obligation":"review","hft_ref":"hft_0ca4b8be47bcc6d9479c","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_formative_honor_path","source_type":"hft","support_ids":["sup_7309fb3f9cd8c6e06413"],"title":"baseline_formative_honor_path","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"109:3:1:1","qac_word_ref":"109:3:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"109:3:1:2","qac_word_ref":"109:3:1","root_ar":"","surface_ar":"لَآ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|2MP","morpheme_role":"STEM","pos":"PRON","qac_ref":"109:3:2:1","qac_word_ref":"109:3:2","root_ar":"","surface_ar":"أَنتُمْ"},{"lemma_ar":"عَابِد","morph_features":"STEM|POS:N|ACT|PCPL|LEM:EaAbid|ROOT:Ebd|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:3:3:1","qac_word_ref":"109:3:3","root_ar":"ع ب د","surface_ar":"عَٰبِدُونَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:REL|LEM:maA","morpheme_role":"STEM","pos":"REL","qac_ref":"109:3:4:1","qac_word_ref":"109:3:4","root_ar":"","surface_ar":"مَآ"},{"lemma_ar":"عَبَدَ","morph_features":"STEM|POS:V|IMPF|LEM:Eabada|ROOT:Ebd|1S","morpheme_role":"STEM","pos":"V","qac_ref":"109:3:5:1","qac_word_ref":"109:3:5","root_ar":"ع ب د","surface_ar":"أَعْبُدُ"}],"word_analysis_qac_refs":[["109:3:1:1"],["109:3:1:2"],["109:3:2:1"],["109:3:3:1"],["109:3:4:1"],["109:3:5:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["109:3:1","109:3:2","109:3:3","109:3:4","109:3:5","109:3:6"]},"focus_surface_evidence":{"arabic_uthmani":"وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"109:3:1:1","qac_word_ref":"109:3:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"109:3:1:2","qac_word_ref":"109:3:1","root_ar":"","surface_ar":"لَآ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|2MP","morpheme_role":"STEM","pos":"PRON","qac_ref":"109:3:2:1","qac_word_ref":"109:3:2","root_ar":"","surface_ar":"أَنتُمْ"},{"lemma_ar":"عَابِد","morph_features":"STEM|POS:N|ACT|PCPL|LEM:EaAbid|ROOT:Ebd|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:3:3:1","qac_word_ref":"109:3:3","root_ar":"ع ب د","surface_ar":"عَٰبِدُونَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:REL|LEM:maA","morpheme_role":"STEM","pos":"REL","qac_ref":"109:3:4:1","qac_word_ref":"109:3:4","root_ar":"","surface_ar":"مَآ"},{"lemma_ar":"عَبَدَ","morph_features":"STEM|POS:V|IMPF|LEM:Eabada|ROOT:Ebd|1S","morpheme_role":"STEM","pos":"V","qac_ref":"109:3:5:1","qac_word_ref":"109:3:5","root_ar":"ع ب د","surface_ar":"أَعْبُدُ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["109:3:1:1"],["109:3:1:2"],["109:3:2:1"],["109:3:3:1"],["109:3:4:1"],["109:3:5:1"]],"word_analysis_refs":["109:3:1","109:3:2","109:3:3","109:3:4","109:3:5","109:3:6"],"word_rows":[{"analysis_record_ref":"109:3:1","analytic_gloss_range_en":"coordinating conjunction that binds this negated nominal panel to the preceding negated verbal panel rather than opening a fresh topic","analytic_root_gloss_range_en":null,"qac_refs":["109:3:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"109:3:2","analytic_gloss_range_en":"negative particle scoping over a nominal predication, denying worshipper-status and its object expression rather than a single finite action","analytic_root_gloss_range_en":null,"qac_refs":["109:3:1:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَآ","transliteration":"la"}},{"analysis_record_ref":"109:3:3","analytic_gloss_range_en":"explicit independent second-person plural subject foregrounding the addressees inside a negated nominal identity clause","analytic_root_gloss_range_en":null,"qac_refs":["109:3:2:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"أَنتُمْ","transliteration":"antum"}},{"analysis_record_ref":"109:3:4","analytic_gloss_range_en":"active-participle plural predicate naming the addressees as worshippers in a directed relation, here categorically denied with respect to the speaker's worship reference","analytic_root_gloss_range_en":"worship, devotion, service, servanthood, owned or submitted status, and physical subduing or smoothing; locally the worship/submission branch is selected, while other branches remain image-pressure or inactive constructional background","qac_refs":["109:3:3:1"],"root":{"arabic":"ع ب د","transliteration":"ʿ-b-d"},"surface":{"arabic":"عَٰبِدُونَ","transliteration":"ʿabiduna"}},{"analysis_record_ref":"109:3:5","analytic_gloss_range_en":"open relative or verbal-noun marker serving as the object expression under the denied predicate, keeping both worship object and worship mode available","analytic_root_gloss_range_en":null,"qac_refs":["109:3:4:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"مَآ","transliteration":"ma"}},{"analysis_record_ref":"109:3:6","analytic_gloss_range_en":"first-person Form I imperfect worship verb inside the relative clause, ongoing and directed through the recovered object carried by the preceding marker","analytic_root_gloss_range_en":"worship, devotion, service, servanthood, submitted obedience, and related subduing imagery; locally the Form I imperfect selects direct ongoing worship/submission rather than specialized devotion or coercive enslavement","qac_refs":["109:3:5:1"],"root":{"arabic":"ع ب د","transliteration":"ʿ-b-d"},"surface":{"arabic":"أَعْبُدُ","transliteration":"aʿbudu"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":6,"words_total":6,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["109:3"],"branch_refs":["root_000973/B003"],"candidate_id":"cand_4afebc1b5f392f28652a","evidence_scope":"focus_ayah","hft_ref":"hft_589d2d3aa4df74652933","item_id":"baseline_devotional_relation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_devotional_relation","support_id":"sup_74874eb41af4fb5819f2"},{"anchor_refs":["109:3"],"branch_refs":["root_000973/B001","root_000973/B004"],"candidate_id":"cand_bf82e5441a1d7719e35b","evidence_scope":"focus_ayah","hft_ref":"hft_8d7efeb988598b1f9b6b","item_id":"baseline_master_service_relation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_master_service_relation","support_id":"sup_85f9ebc7d6564cbecf79"},{"anchor_refs":["109:3"],"branch_refs":["root_000973/B005","root_000973/B006"],"candidate_id":"cand_7150c8229bead3f14f5d","evidence_scope":"focus_ayah","hft_ref":"hft_0ca4b8be47bcc6d9479c","item_id":"baseline_formative_honor_path","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_formative_honor_path","support_id":"sup_7309fb3f9cd8c6e06413"}],"diagnostics":[],"lane_counts":{"global":8,"macro":11,"micro":3},"packet_summary":{"ayah_count":6,"focus_ref":"109:3","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]}],"window":["109:1","109:2","109:3","109:4","109:5","109:6"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"109:3","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"109:3","lane":"micro","linguistic_source_ref":"109:3","surface_ref":"109:3","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"109:3","target_tokens":[["Siz",["109:3:2"]],["de",["109:3:1"]],["benim",["109:3:5"]],["taptığıma",["109:3:4","109:3:5"]],["tapanlar",["109:3:3"]],["değilsiniz",["109:3:1","109:3:2","109:3:3"]]],"text":"Siz de benim taptığıma tapanlar değilsiniz."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":6,"id":"s109-p01-001-006","label":"Whole surah","number":1,"refs":["109:1","109:2","109:3","109:4","109:5","109:6"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:2:categorical-separation","source_type":"word_analysis","support_id":"sup_0366e6375273ab0e8bd8","text":"{\"blocking_evidence\":null,\"headline\":\"the denial excludes shared relation\",\"reader_payoff\":\"The reader notices that the wording excludes overlap with the speaker's worship relation rather than merely noting practical difference.\",\"reason\":\"Attachment evidence keeps the negated predicate and its governed object expression together, so the exclusion reaches the addressees' relation to what the speaker worships.\",\"representative_source_ids\":[\"QS-78827e81\",\"QI-83bffefc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:3:explicit-subject-spotlight","source_type":"word_analysis","support_id":"sup_151ec6869666703ee529","text":"{\"blocking_evidence\":null,\"headline\":\"explicit pronoun spotlights the addressees\",\"reader_payoff\":\"The reader notices that the addressees are deliberately foregrounded before the denied predicate appears.\",\"reason\":\"QAC and attachment evidence identify the pronoun as the nominative subject of the nominal sentence, while the predicate already supplies plural agreement.\",\"representative_source_ids\":[\"QG-6df0c069\",\"QG-c220a76f\",\"MG-9e01bec8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:6:surah-root-thread","source_type":"word_analysis","support_id":"sup_1be9fea92d07e96101ef","text":"{\"blocking_evidence\":null,\"headline\":\"worship root threads through the surah\",\"reader_payoff\":\"The reader notices that this closing verb is part of the surah's concentrated worship-root network, not an isolated clause ending.\",\"reason\":\"The same root recurs in the local predicate and in nearby same-surah worship panels.\",\"representative_source_ids\":[\"QI-1abf7544\",\"QE-c6be6b11\",\"QB-f970cfed\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:1:unlike-clause-types","source_type":"word_analysis","support_id":"sup_2ffa754836df2a8fedd5","text":"{\"blocking_evidence\":null,\"headline\":\"verbal clause joins nominal clause\",\"reader_payoff\":\"The reader notices the grammatical escalation: the connector joins a prior action-denial to a current identity-denial.\",\"reason\":\"The local clause is nominal while 109:2 carries the preceding verbal panel, so the coordination preserves contrast rather than flattening the two clauses into one type.\",\"representative_source_ids\":[\"QT-345ce439\",\"QB-57a95b0e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:6:dominant-imperfect-pathway","source_type":"word_analysis","support_id":"sup_310cca33fe6ce2870290","text":"{\"blocking_evidence\":null,\"headline\":\"speaker uses the dominant verbal pathway\",\"reader_payoff\":\"The reader notices that the speaker's side uses the common imperfect pathway while the addressees are cast in the more marked participial pathway.\",\"reason\":\"The contextual profile lists many imperfect instances for the root-form group compared with the smaller active-participle group.\",\"representative_source_ids\":[\"QI-9aff2c3e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:4:local-sound-cohesion","source_type":"word_analysis","support_id":"sup_31cab2da5fead936d3d3","text":"{\"blocking_evidence\":null,\"headline\":\"sound echo binds identity and action\",\"reader_payoff\":\"The reader notices that the shared root sound ties the predicate to the closing verb while morphology keeps their roles apart.\",\"reason\":\"The rows identify local sound cohesion between the participle and the first-person verb, with no claim that sound overrides grammar.\",\"representative_source_ids\":[\"QE-2edcb7ea\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:4","source_type":"word_analysis","support_id":"sup_354ebfa093721722e037","text":"{\"gloss_range\":\"active-participle plural predicate naming the addressees as worshippers in a directed relation, here categorically denied with respect to the speaker's worship reference\",\"prose\":\"{{ar:عَٰبِدُونَ}} ({{tr:ʿabiduna}}) is the ayah's identity word. It agrees with {{ar:أَنتُمْ}} ({{tr:antum}}) as a plural predicate, so the denied worshipper-status is fixed on the addressed group rather than left generic. Although nominal in form, it still governs {{ar:مَآ أَعْبُدُ}} ({{tr:ma aʿbudu}}), making the denied identity a directed relation toward the speaker's worship reference. The active participle shifts the register from the verbal action of 109:2 to a stable predicate here: not merely that they fail to perform an act, but that they are not worshippers in this relation. The root field keeps worship, service, submission, and the road-subduing image present as pressure, while local form keeps the sense to baseline worshipper-orientation, not causative enslavement or every remote dictionary branch. Within the common worship root, the active-participle pathway is comparatively marked and returns as a same-surah identity panel, so the form feels chosen rather than automatic. Its recitational surface also matters locally: the imala variant changes vowel color without changing grammar, and the visible long-vowel shape sustains the identity term itself. Its sound and root echo with {{ar:أَعْبُدُ}} ({{tr:aʿbudu}}) bind the two worship terms while their forms separate addressee identity from speaker action.\",\"root_display\":\"{{ar:ع ب د}} ({{tr:ʿ-b-d}})\",\"root_gloss_range\":\"worship, devotion, service, servanthood, owned or submitted status, and physical subduing or smoothing; locally the worship/submission branch is selected, while other branches remain image-pressure or inactive constructional background\",\"surface_display\":\"{{ar:عَٰبِدُونَ}} ({{tr:ʿabiduna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:4:predicate-agreement-and-object","source_type":"word_analysis","support_id":"sup_35e525393fbdad932344","text":"{\"blocking_evidence\":null,\"headline\":\"predicate agrees and governs\",\"reader_payoff\":\"The reader notices that the word both predicates identity of the addressed group and directs that identity toward the following worship reference.\",\"reason\":\"Attachment evidence marks {{ar:عَٰبِدُونَ}} ({{tr:ʿabiduna}}) as predicate of {{ar:أَنتُمْ}} ({{tr:antum}}) and as governing the following object expression.\",\"representative_source_ids\":[\"QG-770248a1\",\"QG-796b247b\",\"QG-926f7bfd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:4:recitational-surface","source_type":"word_analysis","support_id":"sup_36c655bd76c91427b795","text":"{\"blocking_evidence\":null,\"headline\":\"surface sound sustains the identity term\",\"reader_payoff\":\"The reader notices that recitational texture falls on the predicate without changing its identity-denial mechanism.\",\"reason\":\"The qiraat and spelling observations affect sound and recitational coloring while preserving the same active-participle grammar.\",\"representative_source_ids\":[\"QF-30dc3be2\",\"QF-7c7f411c\",\"QP-5255801d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:2:weighted-negation-sound","source_type":"word_analysis","support_id":"sup_38c5bcdd950b4726e309","text":"{\"blocking_evidence\":null,\"headline\":\"long negation is audible\",\"reader_payoff\":\"The reader notices that the negation is given recitational prominence before the addressees are named.\",\"reason\":\"The written long-vowel form supports a local sound payoff without changing the syntactic scope of the particle.\",\"representative_source_ids\":[\"QF-208a0895\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:6:ongoing-first-person-action","source_type":"word_analysis","support_id":"sup_3bcafe193026e7f31e31","text":"{\"blocking_evidence\":null,\"headline\":\"imperfect marks ongoing speaker worship\",\"reader_payoff\":\"The reader notices that the speaker's side is an ongoing verbal action, not a second nominal identity claim.\",\"reason\":\"QAC identifies the word as a first-person imperfect Form I verb inside the relative clause, contrasting with the active participle in the main predicate.\",\"representative_source_ids\":[\"QG-29dc5d23\",\"QF-de10ec25\",\"MG-c9c4a5fc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:3","source_type":"word_analysis","support_id":"sup_3f6ddaac9f74932f4f2a","text":"{\"gloss_range\":\"explicit independent second-person plural subject foregrounding the addressees inside a negated nominal identity clause\",\"prose\":\"{{ar:أَنتُمْ}} ({{tr:antum}}) makes the addressees the explicit subject of the nominal clause. The following predicate already carries plural agreement, so the separate pronoun is not just required for person marking; it spotlights the addressed group before their worshipper-identity is denied. Across the boundary from 109:2, this reverses prominence: the addressees move from an embedded role to the main subject, while the speaker retreats into {{ar:أَعْبُدُ}} ({{tr:aʿbudu}}) inside the object clause. The pronoun also becomes a same-surah panel anchor, and even the local nasal echo with {{ar:مَآ}} ({{tr:ma}}) binds the named addressees to the worship reference against which they are measured.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:أَنتُمْ}} ({{tr:antum}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:1:open-vowel-frame","source_type":"word_analysis","support_id":"sup_3f731811d9e86480a188","text":"{\"blocking_evidence\":null,\"headline\":\"open vowel links negation and object marker\",\"reader_payoff\":\"The reader notices a small sound frame linking the opening negation to the later object marker.\",\"reason\":\"The row makes an acoustic claim only; it is kept as a local cadence payoff and not expanded into an independent semantic argument.\",\"representative_source_ids\":[\"QP-e20d7ee0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:3:same-surah-panel-anchor","source_type":"word_analysis","support_id":"sup_4442d24de4cb0e57196c","text":"{\"blocking_evidence\":null,\"headline\":\"pronoun returns as panel anchor\",\"reader_payoff\":\"The reader notices that the explicit addressee is not a one-time emphasis but part of the surah's repeating panel structure.\",\"reason\":\"The row identifies the same clause opening as returning in the nearby same-surah panel.\",\"representative_source_ids\":[\"QE-4c7c6c05\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:2","source_type":"word_analysis","support_id":"sup_4892f9fa52e2e908b94a","text":"{\"gloss_range\":\"negative particle scoping over a nominal predication, denying worshipper-status and its object expression rather than a single finite action\",\"prose\":\"{{ar:لَآ}} ({{tr:la}}) does not simply negate another finite verb. Here it scopes over {{ar:أَنتُمْ عَٰبِدُونَ}} ({{tr:antum ʿabiduna}}), a nominal predication, and through the following {{ar:مَآ أَعْبُدُ}} ({{tr:ma aʿbudu}}). That makes the denial categorical: the addressees are not placed in the worshipper-state directed toward the speaker's worship reference. The long written negation also gives the short clause audible weight before the explicit addressees are named, and its recurrence across the surah turns this particle into a refrain of separated worship relations.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَآ}} ({{tr:la}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:6:local-root-sound-echo","source_type":"word_analysis","support_id":"sup_4e42728b2af93409b71e","text":"{\"blocking_evidence\":null,\"headline\":\"root sound ties predicate to verb\",\"reader_payoff\":\"The reader notices that the same consonant thread binds the addressee predicate to the speaker's verb while their grammar separates identity from action.\",\"reason\":\"The local words share the same root skeleton, but their forms and clause roles differ.\",\"representative_source_ids\":[\"QE-73f2dad4\",\"QP-5bad54d7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:4:root-echo-and-refrain","source_type":"word_analysis","support_id":"sup_5c8f922089f757198c37","text":"{\"blocking_evidence\":null,\"headline\":\"same root returns in changed roles\",\"reader_payoff\":\"The reader notices a concentrated root thread in which the same worship root marks different participants and grammatical roles.\",\"reason\":\"The same root appears locally in the participial predicate and the embedded first-person verb, and the contextual profiles show this root as a common worship field.\",\"representative_source_ids\":[\"QI-23bec8ab\",\"QE-8994fed0\",\"QY-2ae22264\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:4:hinge-position","source_type":"word_analysis","support_id":"sup_63522807a8e7712bfd92","text":"{\"blocking_evidence\":null,\"headline\":\"predicate hinges subject to object clause\",\"reader_payoff\":\"The reader notices that the word is the hinge from named addressees to the worship reference they are denied.\",\"reason\":\"Local attachment makes the predicate relate the explicit subject to the following object expression.\",\"representative_source_ids\":[\"QI-5c5f1703\",\"QT-d300e6c8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:6:first-person-embedded-prominence","source_type":"word_analysis","support_id":"sup_67e9472e2ed7d69c3c36","text":"{\"blocking_evidence\":null,\"headline\":\"speaker is present inside the clause\",\"reader_payoff\":\"The reader notices that the speaker remains the worship reference while the main-clause spotlight rests on the addressees.\",\"reason\":\"The first-person subject is encoded in the verb prefix inside the relative clause rather than expressed as an independent pronoun in the main clause.\",\"representative_source_ids\":[\"QF-8b24408d\",\"QI-065a72c3\",\"QB-221cfde7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:4:act-to-identity-register-shift","source_type":"word_analysis","support_id":"sup_6ba96717ccbf89bc5e0b","text":"{\"blocking_evidence\":null,\"headline\":\"boundary shifts from act to identity\",\"reader_payoff\":\"The reader notices that 109:3 answers the prior verbal panel by changing the same worship root into an identity predicate.\",\"reason\":\"The previous panel uses finite worship verbs, while this clause centers the same root in a nominal active-participle predicate.\",\"representative_source_ids\":[\"QT-5c68fa5a\",\"QT-c9c37058\",\"QB-357c46e1\",\"QY-fe4b3900\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:4:root-submission-pressure","source_type":"word_analysis","support_id":"sup_6bfd52ca0cf4d358af05","text":"{\"blocking_evidence\":null,\"headline\":\"submission field thickens worshipper-status\",\"reader_payoff\":\"The reader notices that the denied worshipper-state is a submitted orientation, with service and subduing pressure behind the worship sense.\",\"reason\":\"V4 supports worship, devotion, service, servanthood, and physical subduing branches, but the local active-participle predicate selects worshipper-status rather than activating every branch as a local sense.\",\"representative_source_ids\":[\"QS-3452cdf7\",\"QS-7818a7a3\",\"QY-1a9e7969\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:6:root-devotion-submission","source_type":"word_analysis","support_id":"sup_6e2c8df2cd3f9e5c3774","text":"{\"blocking_evidence\":null,\"headline\":\"root field makes worship submitted devotion\",\"reader_payoff\":\"The reader notices that the speaker's action is directed devotion and submitted service, not a thin ritual verb.\",\"reason\":\"V4 supports worship, devotion, service, submission, and physical subduing pressure for the root, while local Form I imperfect grammar selects direct worship as the active sense.\",\"representative_source_ids\":[\"QS-27278cf3\",\"QS-2e26f1d0\",\"QS-9e2c674f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:5:reciprocal-ma-bridge","source_type":"word_analysis","support_id":"sup_7020a487226680ffcbd6","text":"{\"blocking_evidence\":null,\"headline\":\"marker bridges reciprocal panels\",\"reader_payoff\":\"The reader notices that the same open marker helps carry object-or-mode ambiguity across the reciprocal denial panels.\",\"reason\":\"The rows connect the marker to the same-surah reciprocal pattern while local grammar fixes its role as the object expression in this clause.\",\"representative_source_ids\":[\"QI-325f84bf\",\"QE-cd4ee92e\",\"QB-a74397f8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:5:object-expression-under-predicate","source_type":"word_analysis","support_id":"sup_705c4b061b443f68329d","text":"{\"blocking_evidence\":null,\"headline\":\"marker supplies the governed object expression\",\"reader_payoff\":\"The reader notices that the speaker's worship reference is embedded inside the addressees' denied predicate.\",\"reason\":\"Attachment evidence marks {{ar:مَآ أَعْبُدُ}} ({{tr:ma aʿbudu}}) as the object expression governed by {{ar:عَٰبِدُونَ}} ({{tr:ʿabiduna}}).\",\"representative_source_ids\":[\"QG-601fc5d0\",\"QT-dbec872a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:1:coordinated-second-panel","source_type":"word_analysis","support_id":"sup_78c42d41e8e123d96450","text":"{\"blocking_evidence\":null,\"headline\":\"coordination makes a second denial panel\",\"reader_payoff\":\"The reader notices that 109:3 continues 109:2 as a paired denial rather than starting an unrelated sentence.\",\"reason\":\"QAC and attachment evidence identify {{ar:وَ}} ({{tr:wa}}) as coordination linking the negated nominal clause of 109:3 to the preceding negated predication in 109:2.\",\"representative_source_ids\":[\"QG-3bfc45dc\",\"MG-7f1f4c5a\",\"QS-1f7c339a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"109:3:3:1","source_type":"qac_morpheme","support_id":"sup_7b594288f2955471d943","text":"{\"lemma_ar\":\"عَابِد\",\"morph_features\":\"STEM|POS:N|ACT|PCPL|LEM:EaAbid|ROOT:Ebd|MP|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"109:3:3:1\",\"qac_word_ref\":\"109:3:3\",\"root_ar\":\"ع ب د\",\"surface_ar\":\"عَٰبِدُونَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:3:addressee-under-denial","source_type":"word_analysis","support_id":"sup_7d23934cc363872541ed","text":"{\"blocking_evidence\":null,\"headline\":\"the named group bears the denial\",\"reader_payoff\":\"The reader notices that the boundary is drawn directly onto the addressed group, not hidden in a verb ending.\",\"reason\":\"The pronoun resolves to the addressed group from the vocative context and launches the core nominal frame after the negator.\",\"representative_source_ids\":[\"QS-00ef13b9\",\"QT-d7ae1846\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:1","source_type":"word_analysis","support_id":"sup_960baee9d0b03277f7f5","text":"{\"gloss_range\":\"coordinating conjunction that binds this negated nominal panel to the preceding negated verbal panel rather than opening a fresh topic\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) keeps 109:3 inside the same two-panel denial that began in 109:2. It is coordination, not a topic reset: the previous verbal denial is now joined to a nominal denial, so the reader sees the surah move from denied action to denied worshipper-identity. Because the particle is attached directly to {{ar:لَآ}} ({{tr:la}}), the surface opening compresses connection and negation into one movement. Its recurrence in the surah makes the denial arrive as another linked panel, while the open vowel echo with {{ar:مَآ}} ({{tr:ma}}) supports that small architecture audibly.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:4:identity-not-action","source_type":"word_analysis","support_id":"sup_977f141c2ab18e7509a8","text":"{\"blocking_evidence\":null,\"headline\":\"participle denies identity\",\"reader_payoff\":\"The reader notices that the active participle turns worship into a denied state of being, not just an action they are not doing.\",\"reason\":\"The aligned form is an active participle functioning as a nominal predicate, not a finite imperfect verb.\",\"representative_source_ids\":[\"QS-a6b8078a\",\"QF-d3caa7be\",\"MF-35f55a38\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:5","source_type":"word_analysis","support_id":"sup_97e0d45e654cae28efdc","text":"{\"gloss_range\":\"open relative or verbal-noun marker serving as the object expression under the denied predicate, keeping both worship object and worship mode available\",\"prose\":\"{{ar:مَآ}} ({{tr:ma}}) supplies the object expression for the denied predicate, not a free-standing new topic. As a relative marker, it heads {{ar:مَآ أَعْبُدُ}} ({{tr:ma aʿbudu}}) and lets the speaker's worship define the reference without naming it directly; the recovered object relation gives this reading real grammatical weight. At the same time, the verbal-noun reading remains locally meaningful, so the denial can reach both what the speaker worships and the speaker's worshipping as a mode of devotion and service. The choice of {{ar:مَآ}} ({{tr:ma}}) rather than a personal who-form keeps the reference open instead of forcing a person-like classification. An interrogative coloring can be kept only as a secondary distance effect, while the local syntax still makes the marker the embedded object expression governed by the predicate.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مَآ}} ({{tr:ma}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:5:interrogative-distance","source_type":"word_analysis","support_id":"sup_9f8bb2c70336834ed179","text":"{\"blocking_evidence\":null,\"headline\":\"interrogative coloring remains secondary\",\"reader_payoff\":\"The reader notices a possible distance effect around identifying the worship reference, while the local object-clause parse still governs the sentence.\",\"reason\":\"QAC lists an interrogative possibility, but attachment evidence strongly projects a relative object expression here, so interrogative force can only be a secondary coloring.\",\"representative_source_ids\":[\"QF-308bc8c6\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:3:nasal-local-binding","source_type":"word_analysis","support_id":"sup_a1ff4c558681a597246c","text":"{\"blocking_evidence\":null,\"headline\":\"nasal sound binds subject and object clause\",\"reader_payoff\":\"The reader notices a local sound binding between the named addressees and the following worship reference.\",\"reason\":\"The row is a sound observation; it is kept as a minor local payoff because it supports the syntax without changing the parse.\",\"representative_source_ids\":[\"QP-f5056cf3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:5:relative-reading-with-recovered-object","source_type":"word_analysis","support_id":"sup_b81f38a7d65c43bc522b","text":"{\"blocking_evidence\":null,\"headline\":\"relative reading recovers the object\",\"reader_payoff\":\"The reader notices that the relative reading lets the speaker's worship define the reference while the object relation remains recoverable.\",\"reason\":\"QAC treats the relative reading as the main contextual parse, and attachment evidence marks {{ar:مَآ}} ({{tr:ma}}) as the object within the relative clause.\",\"representative_source_ids\":[\"QG-94452ea6\",\"QG-f07d50e5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:5:open-what-not-who","source_type":"word_analysis","support_id":"sup_bb57b1bcaf689778417a","text":"{\"blocking_evidence\":null,\"headline\":\"open what-reference avoids personal narrowing\",\"reader_payoff\":\"The reader notices that the marker keeps the worship reference open as object, act, or mode instead of forcing it into a personal who-category.\",\"reason\":\"The local surface is the open marker, and the source rows present the personal who-form only as a contrast, not as the selected wording.\",\"representative_source_ids\":[\"MG-3d5c7131\",\"QS-edb2f9ac\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:3:participant-prominence-reversal","source_type":"word_analysis","support_id":"sup_be6ab934df70c153416c","text":"{\"blocking_evidence\":null,\"headline\":\"speaker and addressees trade prominence\",\"reader_payoff\":\"The reader notices the cross-ayah reversal: the addressees become the main subject while the speaker becomes the embedded worship reference.\",\"reason\":\"The local clause foregrounds {{ar:أَنتُمْ}} ({{tr:antum}}), while the first-person subject is encoded only in the embedded verb.\",\"representative_source_ids\":[\"QI-916d2a94\",\"QT-7c4b0b87\",\"QB-3ad8de8d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:5:devotion-field-through-mode-reading","source_type":"word_analysis","support_id":"sup_c6cf5c1c087230337be9","text":"{\"blocking_evidence\":null,\"headline\":\"mode reading invokes worship-field pressure\",\"reader_payoff\":\"The reader notices that if the verbal-noun parse is heard, the denial reaches worshipping as devotion and service, not only a named object.\",\"reason\":\"The root evidence supports worship, devotion, service, and submission, but this topic depends on the verbal-noun parse and therefore remains secondary to the relative-object parse.\",\"representative_source_ids\":[\"QS-ca433128\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:6:form-one-boundary","source_type":"word_analysis","support_id":"sup_cb0e58a5621725a201bc","text":"{\"blocking_evidence\":null,\"headline\":\"basic Form I avoids specialized alternatives\",\"reader_payoff\":\"The reader notices that the verb presents direct ongoing worship as the measure, not reflexive devotional practice or taking someone as a slave.\",\"reason\":\"The broader root includes other derivational pathways, but the aligned local form is basic Form I imperfect.\",\"representative_source_ids\":[\"QF-b51eae0a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:4:marked-participle-pathway","source_type":"word_analysis","support_id":"sup_cb882d6ca78b582179b2","text":"{\"blocking_evidence\":null,\"headline\":\"marked form inside a common root\",\"reader_payoff\":\"The reader notices that the surah chooses a relatively marked participial pathway for the addressees within a very common worship root.\",\"reason\":\"The contextual profile lists fewer active-participle instances than imperfect instances, and the same participial wording recurs in the surah.\",\"representative_source_ids\":[\"QI-bbbf8b3f\",\"QE-bf928ac1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:4:derivational-boundary","source_type":"word_analysis","support_id":"sup_cf5604d8e73b6f259963","text":"{\"blocking_evidence\":null,\"headline\":\"basic participle avoids causative enslavement\",\"reader_payoff\":\"The reader notices that nearby derivational possibilities sharpen the chosen form: it denies their own worshipper-orientation, not their role as enslavers or specialists in devotional practice.\",\"reason\":\"The broader root family includes enslaving and specialized devotion pathways, but the local form is the basic Form I active participle.\",\"representative_source_ids\":[\"QS-b127d5d3\",\"QF-be41388c\",\"QF-fa359fa8\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:6","source_type":"word_analysis","support_id":"sup_de90e43c18ac35bd7af3","text":"{\"gloss_range\":\"first-person Form I imperfect worship verb inside the relative clause, ongoing and directed through the recovered object carried by the preceding marker\",\"prose\":\"{{ar:أَعْبُدُ}} ({{tr:aʿbudu}}) closes the ayah as a first-person imperfect verb inside the relative clause. Its aspect makes the speaker's worship ongoing or habitual, while its finite form uses the root's common imperfect pathway and contrasts with the addressees' more marked participial identity in {{ar:عَٰبِدُونَ}} ({{tr:ʿabiduna}}). The verb is not objectless here: {{ar:مَآ}} ({{tr:ma}}) supplies the recovered object, so the speaker's worship remains directed. The root field gives the action the force of worship, service, devotion, and submission, but the Form I imperfect keeps it as direct worship rather than specialized devotional practice or coercive enslavement. The first-person prefix lets the speaker remain present without an independent pronoun, and the final position makes his ongoing directed worship the measure by which the addressees' denied identity is framed. Because the same worship verb returns across the surah panels and after the participial detour in this ayah, the closing word is part of a concentrated root thread, not just the end of one relative clause.\",\"root_display\":\"{{ar:ع ب د}} ({{tr:ʿ-b-d}})\",\"root_gloss_range\":\"worship, devotion, service, servanthood, submitted obedience, and related subduing imagery; locally the Form I imperfect selects direct ongoing worship/submission rather than specialized devotion or coercive enslavement\",\"surface_display\":\"{{ar:أَعْبُدُ}} ({{tr:aʿbudu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:6:transitive-recovered-object","source_type":"word_analysis","support_id":"sup_defd6032bf4eb0f2d91e","text":"{\"blocking_evidence\":null,\"headline\":\"worship is directed, not objectless\",\"reader_payoff\":\"The reader notices that the speaker's worship is aimed through the recovered object relation carried by the preceding marker.\",\"reason\":\"Attachment evidence marks {{ar:مَآ}} ({{tr:ma}}) as the fronted object of the verb, and the valency profile shows explicit objects as the dominant pathway for this form.\",\"representative_source_ids\":[\"QG-d418378b\",\"QG-d5d850f1\",\"QT-1a185f61\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:2:nominal-negation-scope","source_type":"word_analysis","support_id":"sup_e1b355c2a92be98678f7","text":"{\"blocking_evidence\":null,\"headline\":\"negation scopes over identity\",\"reader_payoff\":\"The reader notices that the particle denies a worshipper-status, not merely a momentary act.\",\"reason\":\"The local syntax is a negated nominal clause whose predicate is the active participle and whose object expression follows it.\",\"representative_source_ids\":[\"QG-3d73dd3d\",\"MG-3e771024\",\"QT-7fe18b72\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:5:object-or-mode-ambiguity","source_type":"word_analysis","support_id":"sup_e22e80edf1afed6f7b6a","text":"{\"blocking_evidence\":null,\"headline\":\"one marker keeps object and mode live\",\"reader_payoff\":\"The reader notices that the same surface can deny shared object-relation and shared worship-mode without adding a second word.\",\"reason\":\"The local grammar strongly licenses the relative object clause, while QAC also allows a verbal-noun parse that keeps mode-denial available.\",\"representative_source_ids\":[\"QS-50b0dd1e\",\"QF-0cd44f35\",\"QY-32de6f20\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:2:surah-denial-refrain","source_type":"word_analysis","support_id":"sup_e95292844245a1c841f1","text":"{\"blocking_evidence\":null,\"headline\":\"negative particle recurs as refrain\",\"reader_payoff\":\"The reader notices that this negator belongs to the surah's repeated frame of reciprocal denials.\",\"reason\":\"The same particle recurs across the inner surah panels, while local grammar determines its specific nominal scope here.\",\"representative_source_ids\":[\"QE-3340846b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:5:open-vowel-echo","source_type":"word_analysis","support_id":"sup_ed0a16435400af66fe0d","text":"{\"blocking_evidence\":null,\"headline\":\"long vowel echoes the negator\",\"reader_payoff\":\"The reader notices that the object marker is audibly tied to the negation that governs the clause.\",\"reason\":\"The sound row is kept as a local cadence payoff and not made to control the grammatical parse.\",\"representative_source_ids\":[\"QP-84d80c80\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:6:final-measure","source_type":"word_analysis","support_id":"sup_f344ac56bb3885bfb2b2","text":"{\"blocking_evidence\":null,\"headline\":\"closing verb becomes the measure\",\"reader_payoff\":\"The reader notices that the ayah lands on the speaker's ongoing directed worship as the final measure of the denied addressee identity.\",\"reason\":\"The final word is the imperfect transitive verb whose object is recovered through the preceding marker, so closure falls on the speaker's active worship reference.\",\"representative_source_ids\":[\"QT-cb58f183\",\"QY-d0864ef6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:3:1:fused-negative-refrain","source_type":"word_analysis","support_id":"sup_f65dc4ac148ded65bd30","text":"{\"blocking_evidence\":null,\"headline\":\"connection and negation are fused\",\"reader_payoff\":\"The reader notices that the conjunction is not neutral connective padding; it arrives fused to the negative refrain.\",\"reason\":\"The surface form attaches the proclitic conjunction directly to the negator, and same-surah recurrence supports its role in cascading negative panels.\",\"representative_source_ids\":[\"QF-a4713b64\",\"QE-1a336e61\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ","ayah_ref":"109:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000973/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000973","role":"Worship and submissive obedience supplies the literal service relation and makes the repeated root a directed bond between worshipper and object.","root":"ع ب د","source_ref":"109:3","source_word_indices":["3","5"]}],"changed_reading":{"after":"You do not stand as submissive worshippers in relation to the very object toward which my worship remains directed.","before":"You are not performing the same worship I perform."},"confidence":"strong","focus_anchor":"The negated plural participle at word 3 is set against the speaker's ongoing act at word 5, while the intervening relative construction keeps an object of service in view.","mechanism":"The two عبد occurrences form a directed devotional relation: worshipper-status is constituted by submissive obedience toward an object. The negation therefore denies equivalence of relations, not religious activity in the abstract.","model_id":"baseline_devotional_relation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_devotional_relation","source_type":"hft","support_id":"sup_74874eb41af4fb5819f2","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ","ayah_ref":"109:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000973/B001","root_000973/B004"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000973","role":"Owned status supplies a master-servant verticality and recasts the participial predicate as a standing relation of belonging.","root":"ع ب د","source_ref":"109:3","source_word_indices":["3","5"]},{"branch_id":"B004","mapped_root_id":"root_000973","role":"Making someone slave-like contributes the process by which an allegiance claims and shapes its servant.","root":"ع ب د","source_ref":"109:3","source_word_indices":["3","5"]}],"changed_reading":{"after":"The addressees do not occupy the same master-servant relation: what lays claim to the speaker's service does not possess their service.","before":"The two sides practice different cults."},"confidence":"medium","focus_anchor":"The same عبد root names the addressees' denied status and the speaker's affirmative service, permitting a shared vertical relation to be tested and refused.","mechanism":"Owned status and the process of making someone slave-like expose worship as a claim over the person. On this reading, the verse denies that the addressees are claimed by, or stand under, what commands the speaker's service.","model_id":"baseline_master_service_relation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_master_service_relation","source_type":"hft","support_id":"sup_85f9ebc7d6564cbecf79","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ","ayah_ref":"109:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000973/B005","root_000973/B006"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000973","role":"Physical subduing and smoothing supplies the image of a person or path made traversable by repeated service.","root":"ع ب د","source_ref":"109:3","source_word_indices":["3","5"]},{"branch_id":"B006","mapped_root_id":"root_000973","role":"Honoring and magnifying supplies the upward allocation of value to the object that service centers.","root":"ع ب د","source_ref":"109:3","source_word_indices":["3","5"]}],"changed_reading":{"after":"You are not being formed along the same subdued path or magnifying the same center that forms and orients my service.","before":"You do not direct the same ritual toward my object."},"confidence":"exploratory","focus_anchor":"The paired عبد forms can distribute one root's effects across the worshipping subject and the honored object without leaving the focus construction.","mechanism":"Service both subdues and smooths the one who travels its way and magnifies what receives that service. The negation can therefore mark incompatible formation: the addressees are neither made passable by the same path nor oriented toward the same center of honor.","model_id":"baseline_formative_honor_path"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_formative_honor_path","source_type":"hft","support_id":"sup_7309fb3f9cd8c6e06413","trust":"legacy_unbound"}]}
</lane_packet_json>
