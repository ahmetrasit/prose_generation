# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **111:5**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s111-regular-20260911/s111/111_5/micro.discovery.json` and modify nothing
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
  "ayah_ref": "111:5",
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
{"analysis_context":{"analysis_id":"s111-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"111:5","host_surah":111,"lane_context_refs":[],"ordered_context_refs":["111:0","111:1","111:2","111:3","111:4","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, cömertlik, nitelik, mal veya bilgi verme ve yabancı kökenli örtü adlarıyla ilgili eş yazımlı anlamları kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000284/B001","candidate_links":[{"candidate_id":"cand_95babfbcc004a565e904","lane":"micro"},{"candidate_id":"cand_2fdced5c1589ea1bdfdc","lane":"micro"},{"candidate_id":"cand_ac8d8659ce8481fc5aac","lane":"micro"},{"candidate_id":"cand_0807c6428416b020e630","lane":"micro"},{"candidate_id":"cand_b52007d35c7c96d74abe","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جِيد","morph_features":"STEM|POS:N|LEM:jiyd|ROOT:jyd|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:2:1","qac_word_ref":"111:5:2","surface_ar":"جِيدِ"}],"gloss":"boyun; boynun önü, uzunluğu ve güzelliği","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim, baş ile gövde arasındaki boyun bölgesidir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bazı kaynaklarda temel ad özellikle boynun ön kısmını gösterir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı ad, bir kullanımda boynun uzunluğu anlamına gelir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Türemiş kişi nitelemeleri ve bağlı ifade, boynun uzun ya da güzel oluşunu bildirir."}}],"root_ar":"ج ي د","root_id":"root_000284","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yalın anatomik çekirdeğini ve ona bağlı uzunluk ile güzellik nitelemelerini birlikte özetleyen üst anlatımdır.","boundary_detail":"Dal, cömertlik, nitelik, mal veya bilgi verme ve yabancı kökenli örtü adlarıyla ilgili eş yazımlı anlamları kapsamaz.","branch_image_ar":"الجيد والعنق","concept_gloss":"boyun; boynun önü, uzunluğu ve güzelliği","contextual_glosses":[{"applicability":"Yalın adın bütün boyun bölgesini gösterdiği genel anatomik bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Boynun ön kısmına özgülenmeyi ve uzunluk ile güzellik nitelemelerini dışarıda bırakır.","preserves":"Dalın temel anatomik boyun anlamını doğal ve kısa biçimde korur."},"facet_ids":["F001"],"text":"boyun","usage_role":"general"},{"applicability":"Adın bütün boyun yerine özellikle öndeki anatomik bölgeyi gösterdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bütün boyun kapsamını ve uzunluk ile güzellik nitelemelerini dışarıda bırakır.","preserves":"Kaynaklardan birindeki ön bölge özgüllemesini açık biçimde korur."},"facet_ids":["F002"],"text":"boynun ön kısmı","usage_role":"contextual"},{"applicability":"Aynı adın anatomik bölgenin kendisinden çok onun uzunluğunu gösterdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Boynun kendisini, ön kısmını ve güzellik nitelemesini dışarıda bırakır.","preserves":"Boynun uzunluğunu adlandıran kaynak varyantını doğrudan korur."},"facet_ids":["F003"],"text":"boyun uzunluğu","usage_role":"contextual"},{"applicability":"Türemiş kişi nitelemeleri ile boyun güzelliğini bildiren bağlı ifadenin ortak anlatımında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalın anatomik adı, ön kısım özgüllemesini ve türemiş biçimler arasındaki kişi ayrımlarını dışarıda bırakır.","preserves":"Kişinin boyun uzunluğu veya güzelliğiyle nitelenmesini doğal Türkçeyle korur."},"facet_ids":["F004"],"text":"uzun ya da güzel boyunlu","usage_role":"explanatory"}],"definition":"Temel anlam boyundur; bazı kaynaklarda boynun ön kısmına, bir kullanımda da boynun uzunluğuna özgülenir. Türemiş kişi nitelemeleri ve bağlı ifade, boynun uzun veya güzel oluşunu belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim, baş ile gövde arasındaki boyun bölgesidir."},{"facet_id":"F002","role":"source_variant","statement":"Bazı kaynaklarda temel ad özellikle boynun ön kısmını gösterir."},{"facet_id":"F003","role":"source_variant","statement":"Aynı ad, bir kullanımda boynun uzunluğu anlamına gelir."},{"facet_id":"F004","role":"extension","statement":"Türemiş kişi nitelemeleri ve bağlı ifade, boynun uzun ya da güzel oluşunu bildirir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bu dala ait olmayan verme ve eli açıklık anlamını ekler.","collision":"Aynı harf dizisine bağlanan ayrı anlam alanıyla karışmaya yol açar.","fit":"displacement","loses":"Boyun, boynun önü ve boyuna ilişkin uzunluk veya güzellik içeriğinin tamamını yitirir.","preserves":"Verme ve eli açıklıkla ilgili ayrı anlam alanını doğal Türkçeyle anlatır."},"text":"cömertlik"}],"identity_rationale":"Yetkili dal ifadesi anlam çekirdeğini boyun olarak verir; kaynaklar bunun bütün boynu ya da özellikle ön kısmını gösterebildiğini, ayrıca boynun uzunluğu ve güzelliğiyle ilgili türemiş nitelemelere dayanak olduğunu belirtir. Geçici dal çerçevesi bu katmanları aynı boyun kavramına bağlı tuttuğu için kaynak ifadesiyle uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"boyun veya boynun ön kısmı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"boyun uzunluğu"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"boyunlar"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"uzun boyunlu veya güzel boyunlu erkek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"uzun ya da güzel boyunlu kadın"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"güzel boyunlu kadın"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"boynu güzel kadın"}],"lexicalization_note":"Tanım, yalın kullanımdaki boyun anlamını korur; boynun uzun ya da güzel oluşunu bildiren türemiş biçimleri ve bağlı ifadeyi bu çekirdeğin kapsamına genellemez.","neighbor_coverage_note":"Sekiz adayın tamamı değerlendirildi; boyun sınırı veya alt bölgesiyle doğrudan karışabilecek dört karşıtlık yayımlandı. Saçın görünümü, genel beden yapısı, ince boyun-büyük baş bileşimi ve yüz güzelliği yalnızca betimleme alanını paylaştığı için eklenmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği bütün boyundur ve ön kısım yalnızca kaynaklardan birindeki özgüllemedir; komşu dal ise boynun belirli bir yüzünü veya bölümünü esas alır. Bu nedenle anatomik örtüşme vardır, fakat olağan kullanımda birbirlerinin yerine geçmezler.","focus_only":"Odak dal bütün boynu da kapsar ve boynun uzunluğu ile güzelliğine bağlı nitelemeler geliştirir.","gloss":"boynun yüzü, üstü ya da önü","neighbor_only":"Komşu dal insan veya at boynunun belirli yüzünü, üstünü ya da önünü ayrı bir anatomik bölüm olarak adlandırır.","neighbor_ref":"root_000733/B007","relation_type":"near_neighbor","shared_zone":"İki dal da boynu, özellikle onun ön veya üst yöndeki bölümünü konu edinir."},{"boundary_match":"field_only","distinction":"Odak dal boynun kendisini adlandırır; komşu dal ise boynun altındaki üst göğüs ve kesim bölgesini merkez alır. Bitişik beden bölgeleri olmaları ortak bir alan yaratır, ancak gönderimleri farklıdır.","focus_only":"Odak dal boynu ve boynun uzun ya da güzel oluşuna bağlı nitelemeleri içerir.","gloss":"üst göğüs ve kesim yeri","neighbor_only":"Komşu dal üst göğsü, kesim yerini, kolye bölgesini ve buradaki belirli anatomik öğeleri kapsar.","neighbor_ref":"root_001479/B001","relation_type":"same_field","shared_zone":"Her iki dal boyun ile göğsün birleştiği anatomik çevrede yer alır."},{"boundary_match":"field_only","distinction":"Odak dal boyun merkezlidir; komşu dal göğüs önündeki çukur ve kolye yeri gibi alt sınır noktalarını, ayrıca bu bölgeyle ilişkili eylemleri merkez alır. Yakın konumları eş anlamlılık oluşturmaz.","focus_only":"Odak dal boynun kendisini, önünü ve uzunluk veya güzellik bakımından nitelenmesini kapsar.","gloss":"köprücük çukuru ve kolye yeri","neighbor_only":"Komşu dal köprücük çukurunu, kolyenin durduğu yeri ve göğüs önünde tutma veya kavrama eylemlerini kapsar.","neighbor_ref":"root_001338/B005","relation_type":"same_field","shared_zone":"İki dal boynun alt sınırı ile üst göğüs çevresinde anatomik yakınlık taşır."},{"boundary_match":"field_only","distinction":"Odak dal boynun kendisidir; komşu dal ise boynun yanında, omuzla birleşme noktasındaki etli dokuyu gösterir. Gönderim alanları bitişik olsa da aynı anatomik parça değildir.","focus_only":"Odak dal bütün boynu ve ona bağlanan uzunluk ile güzellik nitelemelerini içerir.","gloss":"omuz ile boyun arasındaki etli bölge","neighbor_only":"Komşu dal omuz ile boyun arasındaki etli yan bölgeyi ve bu çevredeki belirli dokuları adlandırır.","neighbor_ref":"root_000093/B006","relation_type":"same_field","shared_zone":"Her iki dal boynun omuzla birleştiği anatomik çevreye temas eder."}],"source_phrase_ar":"الجيم والياء والدال أصل واحد وهو العنق (maqayis)؛ الجيد مقدم العنق (ayn)؛ الجيد العنق (jamhara)؛ الجيد طول الجيد والجيداء الطويلة الجيد (maqayis)؛ رجل أجيد وامرأة جيداء حسنة الجيد إذا كانت طويلة العنق (jamhara)؛ امرأة جيدانة حسنة الجيد (ayn)","source_summary":"Kaynaklar anlam çekirdeğini boyun olarak paylaşır; bunlardan biri boynun ön kısmını öne çıkarırken diğer tanıklıklar aynı adı boyun uzunluğu için de verir. Türemiş biçimler ve bağlı ifade, kişiyi boynunun uzunluğu ya da güzelliği üzerinden niteler.","sources":["MQ","AY","JA"],"what_is_ar":"العنق ومقدمه وما يقال في طول الجيد وحسنه كأجيد وجيداء وجيدانة","what_is_not_ar":"لا يدخل الجود والجودة وبذل المال والعلم، ولا الأكسية المعربة"},"support_links":["sup_0c0f822a5ee347126fb0","sup_500faf58bc2cb81867aa","sup_57e3c6af36af0c4bffed","sup_619d8105a0e1cc83eb79","sup_908f195f4a0af0b20175"]},{"boundary":"Bu dal söz, güvence, beden damarı, tuzak, kum şeridi veya gebelik anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000291/B001","candidate_links":[{"candidate_id":"cand_95babfbcc004a565e904","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَبْل","morph_features":"STEM|POS:N|LEM:Habol|ROOT:Hbl|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:3:1","qac_word_ref":"111:5:3","surface_ar":"حَبْلٌ"}],"gloss":"bağlama ve yedme ipi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bağlama, tutma veya yedme işlevi gören bilinen somut ip."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ağaca çıkarken kullanılan kalın ve taşıyıcı ip."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bükülmüş ya da kıvrılmış saç tutamlarının ipe benzetilmesi."}}],"root_ar":"ح ب ل","root_id":"root_000291","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın somut, uzun ve bağlayıcı araç çekirdeğini karşılar.","boundary_detail":"Bu dal söz, güvence, beden damarı, tuzak, kum şeridi veya gebelik anlamlarını kapsamaz.","branch_image_ar":"حبل ممدود يربط ويقاد به","concept_gloss":"bağlama ve yedme ipi","contextual_glosses":[{"applicability":"Ağaca çıkmak için kullanılan kalın ip söz konusu olduğunda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tırmanma işlevini ve somut ip niteliğini korur."},"facet_ids":["F002"],"text":"tırmanma ipi","usage_role":"contextual"},{"applicability":"Saç tutamlarının ip biçimine benzetildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Saçın bükümlü ip görünümünü açıkça korur."},"facet_ids":["F003"],"text":"ip gibi bükümlü saç","usage_role":"explanatory"}],"definition":"Bir şeyi bağlamak ya da yedmek için kullanılan uzun, bükümlü iptir. Ağaca çıkmaya yarayan kalın ip ve saçın ip gibi bükümlü görünmesi bu çekirdeğin özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bağlama, tutma veya yedme işlevi gören bilinen somut ip."},{"facet_id":"F002","role":"specialization","statement":"Ağaca çıkarken kullanılan kalın ve taşıyıcı ip."},{"facet_id":"F003","role":"associated_use","statement":"Bükülmüş ya da kıvrılmış saç tutamlarının ipe benzetilmesi."}],"identity_rationale":"Kaynak ifadesi, bağlamak, yedmek ya da tırmanmak için kullanılan somut ipi açıkça merkeze alır; bükümlü saç benzetmesi de bu biçimsel çekirdeğe bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ip veya yular"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ağaca çıkma ipi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"ip"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ip gibi örülmüş ya da kıvrılmış saç"}],"lexicalization_note":"Tanım genel ip anlamını, tırmanma ipi gibi özel biçimleri ve yalnız saç bağlamında görülen benzetmeli kullanımı ayrı tutar.","neighbor_coverage_note":"Adayların tümü karşılaştırıldı; yalnız somut ip, yular ve bükme sınırını açıklayan üç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal kalın ve bükümlü yapıyı belirginleştirirken bu dal genel ip ve yular çekirdeğini, tırmanma aracını ve saç benzetmesini birlikte kapsar.","focus_only":"Genel yular işlevini ve saçın ip görünümünü de kapsar.","gloss":"kalın bükümlü ip","neighbor_only":"Kalın, bükümlü ipi yelken ve yük takımı gibi daha özel araçlarda da kapsar.","neighbor_ref":"root_001292/B002","relation_type":"near_synonym","shared_zone":"Her ikisinin merkezinde taşıyan veya bağlayan somut ip bulunur."},{"boundary_match":"partial","distinction":"Komşu dal yular ve yedilme işleviyle sınırlıyken odak dal somut ipin daha genel araç alanını kapsar.","focus_only":"Tırmanma ipini ve saç benzetmesini içerir.","gloss":"boyun ipi ve dizgin","neighbor_only":"Özellikle boyun ipi, dizgin ve yedilme durumuna odaklanır.","neighbor_ref":"root_000235/B003","relation_type":"near_synonym","shared_zone":"İki dal da hayvanı yedmeye yarayan ip alanında kesişir."},{"boundary_match":"partial","distinction":"Odak dal araç olan ipi, komşu dal ise bu yapıyı meydana getiren burma işlemini anlatır.","focus_only":"Ortaya çıkan ipi nesne olarak adlandırır.","gloss":"ipi bükmek","neighbor_only":"İpi ve benzer nesneleri bükme ya da burma eylemini adlandırır.","neighbor_ref":"root_001127/B001","relation_type":"near_neighbor","shared_zone":"Bükümlü ip yapısı iki dalın ortak maddi alanıdır."}],"source_phrase_ar":"الحبل الرسن (ayn;tahdhib)؛ الحبل معروف (jamhara;mufradat)؛ الحبل الرسن معروف والجمع حبال (maqayis)؛ الحابول الكر الذي يصعد به إلى النخل (jamhara;sihah)؛ المحبل الحبل (tahdhib)؛ محبل الشعر كأن كل قرن من قرون رأسه حبل (tahdhib)","source_summary":"Kaynaklar somut ip ve yular çekirdeğinde birleşir; tırmanma ipini ve saçın ip görünümünü bu çekirdeğin özel kullanımları olarak verir.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الحبل المعروف والرسن والحابول الذي يصعد به النخل والمحبل بمعنى الحبل وما يشبه الحبل في الشعر المفتول","what_is_not_ar":"لا يدخل فيه العهد والأمان ولا العرق المسمى حبلا ولا الحبالة المصيدة"},"support_links":["sup_619d8105a0e1cc83eb79"]},{"boundary":"Somut ip yalnız benzetmenin dayanağıdır; bu dalın göndergesi fiziksel ip, tuzak veya kum değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000291/B002","candidate_links":[{"candidate_id":"cand_ac8d8659ce8481fc5aac","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَبْل","morph_features":"STEM|POS:N|LEM:Habol|ROOT:Hbl|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:3:1","qac_word_ref":"111:5:3","surface_ar":"حَبْلٌ"}],"gloss":"bağlayıcı söz ve güvence","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Taraflar arasında koruma ve bağlılık doğuran söz ya da güvence."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsanlar arasında süreklilik, yakınlık ve bağlantı sağlayan bağ."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişiyi veya topluluğu bir amaca ulaştıran manevi dayanak ya da araç."}}],"root_ar":"ح ب ل","root_id":"root_000291","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kişiler arası bağlılık, koruma ve güvence çekirdeğini birlikte karşılar.","boundary_detail":"Somut ip yalnız benzetmenin dayanağıdır; bu dalın göndergesi fiziksel ip, tuzak veya kum değildir.","branch_image_ar":"حبل عهد وأمان ووصل","concept_gloss":"bağlayıcı söz ve güvence","contextual_glosses":[{"applicability":"Bir kişi veya topluluktan güvence alma bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Koruma sağlayan bağlayıcı söz anlamını korur."},"facet_ids":["F001"],"text":"koruma sözü","usage_role":"contextual"},{"applicability":"Bir amaca erişmeyi sağlayan manevi araç anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir hedefe erişim sağlayan dayanak işlevini korur."},"facet_ids":["F003"],"text":"ulaştıran dayanak","usage_role":"explanatory"}],"definition":"Kişiyi başkasına bağlayan söz, güvence, koruma veya süreklilik bağıdır; daha geniş olarak bir amaca ulaşmayı sağlayan dayanak da bu görüntüyle anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Taraflar arasında koruma ve bağlılık doğuran söz ya da güvence."},{"facet_id":"F002","role":"extension","statement":"İnsanlar arasında süreklilik, yakınlık ve bağlantı sağlayan bağ."},{"facet_id":"F003","role":"extension","statement":"Bir kişiyi veya topluluğu bir amaca ulaştıran manevi dayanak ya da araç."}],"identity_rationale":"Kaynak ifadesi söz, güvence, koruma, bağ ve bir şeye ulaşmayı sağlayan araç anlamlarını ortak bir bağlayıcılık görüntüsü altında açıkça toplar.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"söz, güvence ve bağlılık bağı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"birinden koruma sözü almak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"Tanrı'ya yönelten ve birlik sağlayan dayanak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"Tanrı'dan ve insanlardan gelen söz ve güvence"}],"lexicalization_note":"Genel mecaz anlam ile söz alma, ilahi dayanağa tutunma ve iki taraftan güvence alma gibi yapıya bağlı kullanımlar ayrı gösterilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sözün bağlayıcılığı, hak boyutu ve bozulma karşıtlığını en iyi gösteren üçü seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal resmî ve korunmuş sözleşmeyi öne çıkarır; odak dal güvence yanında bağlantı ve erişim aracını da kapsar.","focus_only":"Bağlantı ve bir amaca ulaştıran dayanak anlamlarına da uzanır.","gloss":"korunan sözleşme","neighbor_only":"Yeminle pekiştirilebilen resmî sözleşme ve bu sözün taraflarına odaklanır.","neighbor_ref":"root_001055/B003","relation_type":"near_synonym","shared_zone":"İki dal da güvenlik ve yükümlülük doğuran söz alanını paylaşır."},{"boundary_match":"partial","distinction":"Odak dal bağ kurma ve erişim görüntüsünü korurken komşu dal sözden doğan hak ve sorumluluğu merkezileştirir.","focus_only":"Süreklilik bağı ve bir şeye ulaştıran araç anlamlarını içerir.","gloss":"sözün dokunulmazlığı","neighbor_only":"Hakkı gözetme, borç üstlenme ve bu yükümlülüğün dokunulmazlığına ağırlık verir.","neighbor_ref":"root_000520/B002","relation_type":"near_synonym","shared_zone":"Söz, güvence ve korunan hak iki dalın ortak alanıdır."},{"boundary_match":"opposed","distinction":"Odak dal koruyucu bağı var eden ya da sürdüren kutbu, komşu dal ise onu çözen karşı kutbu anlatır.","focus_only":"Sözü ve bağı kurup sürdürür.","gloss":"bağı bozmak","neighbor_only":"Kurulmuş ittifakı veya bağlayıcı bağı bozup kaldırır.","neighbor_ref":"root_000432/B007","relation_type":"polarity_pair","shared_zone":"İki dal aynı toplumsal bağın kurulması ve çözülmesi eksenindedir."}],"source_phrase_ar":"الحبل العهد والأمان والحبل التواصل (ayn)؛ الحبل العهد والحبل الأمان وأخذت بحبل من فلان أي عهدا وأمانا (jamhara)؛ الحبل العهد والأمان وهو مثل الجوار والحبل الوصال (sihah)؛ الحبل العهد والأمان والحبل التواصل والعهد والذمة (tahdhib)؛ استعير للوصل ولكل ما يتوصل به إلى شيء ويقال للعهد حبل (mufradat)؛ المحمول عليه الحبل وهو العهد ويريد الأمان وعهود الخفارة (maqayis)","source_summary":"Kaynaklar söz, güvence, koruma ve bağlantı anlamlarında birleşir; bir şeye erişmeyi sağlayan dayanak anlamını bunların genişlemesi olarak sunar.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه العهد والأمان والجوار والذمة والوصال والمواصلة وكل ما يتوصل به إلى شيء","what_is_not_ar":"لا يدخل فيه الرسن الحسي ولا الحبالة المصيدة ولا الرمل المستطيل"},"support_links":["sup_0c0f822a5ee347126fb0"]},{"boundary":"Bu dal kumun biçimine ilişkindir; aynı biçimsel adın ip, beden damarı veya yer adı kullanımları buraya girmez.","branch_kind":"bare","branch_ref":"root_000291/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَبْل","morph_features":"STEM|POS:N|LEM:Habol|ROOT:Hbl|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:3:1","qac_word_ref":"111:5:3","surface_ar":"حَبْلٌ"}],"gloss":"uzun kum sırtı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çevresine göre uzunlamasına uzanan kum parçası."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kum oluşumunun toplu, çok, iri veya yüksek oluşunun ayrıca belirtilmesi."}}],"root_ar":"ح ب ل","root_id":"root_000291","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Uzunlamasına uzanan kum oluşumunun yalın karşılığıdır.","boundary_detail":"Bu dal kumun biçimine ilişkindir; aynı biçimsel adın ip, beden damarı veya yer adı kullanımları buraya girmez.","branch_image_ar":"رمل مستطيل ممتد","concept_gloss":"uzun kum sırtı","contextual_glosses":[{"applicability":"Yükseklikten çok yatay uzanışın öne çıktığı betimlemelerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uzunlamasına uzanan kum parçası anlamını korur."},"facet_ids":["F001"],"text":"uzanan kum şeridi","usage_role":"contextual"}],"definition":"Uzunlamasına uzanan ve çoğu kez toplu, iri ya da yüksek görünen bir kum şeridi veya kum sırtıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çevresine göre uzunlamasına uzanan kum parçası."},{"facet_id":"F002","role":"source_variant","statement":"Kum oluşumunun toplu, çok, iri veya yüksek oluşunun ayrıca belirtilmesi."}],"identity_rationale":"Kaynak ifadesi uzunlamasına uzanan, kimi anlatımlarda toplu, yüksek ve iri olan bir kum oluşumunu tutarlı biçimde gösterir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"uzun ve yüksek kum sırtı"}],"lexicalization_note":"Tanım yalnız çıplak biçimin uzun kum şeridi anlamını verir ve başka yapılara bağlı anlamları içeri almaz.","neighbor_coverage_note":"Tüm adaylar incelendi; uzunluk, yükselti ve ip biçimiyle karışma ihtimalini açıklayan üç karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ayırıcı özelliği uzun şerit biçimidir; komşu dalda biçimsel benzetme ve yükselti daha belirleyicidir.","focus_only":"Uzunlamasına uzanmayı kurucu özellik sayar.","gloss":"yükselmiş kum tepesi","neighbor_only":"Kalçaya benzetilen yükseltiyi ve bitki yetiştiren özel kum tepesini kapsar.","neighbor_ref":"root_000985/B005","relation_type":"near_synonym","shared_zone":"Her iki dal yükselmiş bir kum oluşumunu anlatır."},{"boundary_match":"partial","distinction":"Komşu dal dikey yükselişi, odak dal ise uzunlamasına devam eden kum sırtını öne çıkarır.","focus_only":"Uzanmış kum şeridi olmayı gerektirir.","gloss":"yüksek kum tepesi","neighbor_only":"Belirgin biçimde yüksek ve çevreye yukarıdan bakan bir kum tepesine odaklanır.","neighbor_ref":"root_001607/B007","relation_type":"near_synonym","shared_zone":"Kumdan oluşan yükselti iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Biçim benzerliği dışında göndergeler ayrıdır: biri arazi oluşumu, öteki kullanılan somut bir iptir.","focus_only":"Doğal bir kum oluşumudur.","gloss":"uzun ip","neighbor_only":"Bağlama ve yedme için kullanılan yapılmış bir araçtır.","neighbor_ref":"root_000291/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da uzun ve çizgisel biçim algısı bulunur."}],"source_phrase_ar":"الحبل الرمل الطويل الضخم (ayn)؛ يقال للرمل يستطيل حبل (sihah)؛ الحبل من الرمل المجتمع الكثير العالي والحبل رمل يستطيل ويمتد (tahdhib)؛ الحبل المستطيل من الرمل (mufradat)؛ الحبل القطعة من الرمل يستطيل (maqayis)","source_summary":"Kaynaklar uzun ve uzanan kum oluşumunda birleşir; bazı anlatımlar bunun toplu, iri ya da yüksek görünümünü de belirtir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الحبل من الرمل إذا استطال وامتد أو كان مجتمعا كثيرا عاليا","what_is_not_ar":"لا يدخل فيه الحبل الرسن ولا الموضع المسمى حبل ولا عروق البدن"},"support_links":[]},{"boundary":"Anatomik yapılar çekirdektir; atın bileği özel adlandırma, yakınlık ve kolaylık anlatımı ise ayrı bir ilişkili kullanımdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000291/B004","candidate_links":[{"candidate_id":"cand_b52007d35c7c96d74abe","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَبْل","morph_features":"STEM|POS:N|LEM:Habol|ROOT:Hbl|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:3:1","qac_word_ref":"111:5:3","surface_ar":"حَبْلٌ"}],"gloss":"ip biçimli damar veya bağ","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Boyun, kol veya omuz çevresindeki ip biçimli damar, sinir ya da bağlantı."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Atın bacak damarları ve bilekleri için kullanılan özel beden adları."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kol üzerindeki yapıya dayanarak bir işin yakın, kolay veya kişinin elinde olduğunu anlatan söz."}}],"root_ar":"ح ب ل","root_id":"root_000291","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın insan ve hayvan bedenindeki çizgisel yapı çekirdeğini karşılar.","boundary_detail":"Anatomik yapılar çekirdektir; atın bileği özel adlandırma, yakınlık ve kolaylık anlatımı ise ayrı bir ilişkili kullanımdır.","branch_image_ar":"حبال البدن عروق ووصلات","concept_gloss":"ip biçimli damar veya bağ","contextual_glosses":[{"applicability":"Bir işin kişiye yakın, kolay veya onun denetiminde olduğu kalıplaşmış bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakınlık ve kolay erişilebilirlik anlamını korur."},"facet_ids":["F003"],"text":"yakında ve elde","usage_role":"contextual"}],"definition":"İp gibi uzanan damar, sinir veya beden bağlantısıdır; boyun, omuz-kol birleşimi ve hayvan bacaklarındaki belirli yapılar için kullanılır. Atın bileği ile kol üzerinden anlatılan yakınlık ya da kolaylık kullanımları bu çekirdeğe bağlı özelleşmelerdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Boyun, kol veya omuz çevresindeki ip biçimli damar, sinir ya da bağlantı."},{"facet_id":"F002","role":"specialization","statement":"Atın bacak damarları ve bilekleri için kullanılan özel beden adları."},{"facet_id":"F003","role":"associated_use","statement":"Kol üzerindeki yapıya dayanarak bir işin yakın, kolay veya kişinin elinde olduğunu anlatan söz."}],"identity_rationale":"Kaynak ifadesi ip görünümündeki damar, sinir ve eklem bağlantılarını destekler; ancak kol bağı üzerinden kurulan yakınlık veya kolaylık sözü anatomik çekirdeğin kendisi değil, ona bağlı kalıplaşmış bir kullanımdır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"omuz ile kol arasındaki sinir veya bağ"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"boyundaki ana damar"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"koldaki damar"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yakınında, kolayca elinin altında"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"atın bacak damarları"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"atın veya başka bir binek hayvanının bileği"}],"lexicalization_note":"Tanım yalnız belirtilen beden yapılarıyla kalır; at bileği ve kol bağına dayanan kalıplaşmış söz ayrı yüzlerde tutulur.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; anatomik yapı, sert kiriş ve gerçek ip arasındaki sınırı gösteren üçü yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal belirli anatomik yapıların adıdır; komşu dal bu yapıların yayılması veya belirginleşmesi durumunu anlatır.","focus_only":"Belirli damarları, omuz bağlantısını ve atın bileğini adlandırır.","gloss":"damar ve sinirlerin yayılması","neighbor_only":"Yorgunlukla sinirlerin yayılıp belirginleşmesini ve başka bir bedensel durumu anlatır.","neighbor_ref":"root_001503/B007","relation_type":"same_field","shared_zone":"İki dal damar ve sinir yapılarını konu edinir."},{"boundary_match":"field_only","distinction":"Komşu dal sert kirişin maddesine ve kullanımına, odak dal ise belirli damar ve bağlantıların adlandırılmasına odaklanır.","focus_only":"Damar ve beden bağlantılarını ip görünümüyle adlandırır.","gloss":"sert sinir ve kiriş","neighbor_only":"Sert beyaz sinir ya da kirişi ve ondan yapılan bağlama gereçlerini anlatır.","neighbor_ref":"root_001033/B001","relation_type":"same_field","shared_zone":"İki dal bedendeki lifli, uzunca yapılar alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal benzetmeyle adlandırılmış anatomik yapıyı, komşu dal ise benzetmenin kaynağı olan gerçek ipi gösterir.","focus_only":"Canlı bedeninin iç veya birleşim yapısıdır.","gloss":"somut ip","neighbor_only":"Bağlamak veya yedmek için dışarıdan kullanılan araçtır.","neighbor_ref":"root_000291/B001","relation_type":"near_neighbor","shared_zone":"İp biçimli uzanış iki dalın ortak görüntüsüdür."}],"source_phrase_ar":"حبل العاتق وصلة ما بين العاتق والمنكب وحبل الوريد عرق (ayn;tahdhib)؛ حبل الذراع معروف وهذا الأمر على حبل ذراعك أي ممكن لك (jamhara)؛ حبل الوريد عرق في العنق وحبل الذراع في اليد وهو على حبل ذراعك أي في القرب منك (sihah)؛ حبال الفرس عروق قوائمه والمحتبل رسغها (tahdhib)؛ شبه به من حيث الهيئة حبل الوريد وحبل العاتق (mufradat)؛ الحبل حبل العاتق ومحتبله أرساغه (maqayis)","source_summary":"Kaynaklar boyun ve omuz çevresindeki ip biçimli beden yapılarını ortaklaşa verir; atın bacak damarları, bilekleri ve yakınlık anlatan söz aynı toplu kanıtta yer alır.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه حبل الوريد وحبل العاتق وحبل الذراع وحبال الفرس ومحتبل الفرس والأمثال المبنية على حبل الذراع","what_is_not_ar":"لا يدخل فيه الحبل الخارجي الذي يربط به ولا العهد والأمان"},"support_links":["sup_908f195f4a0af0b20175"]},{"boundary":"Dalın çekirdeği yakalayan düzenektir; ölüm ve ayartma anlatımları mecaz, avcı-okçu sözleri ise ilişkili kalıplaşmış kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000291/B005","candidate_links":[{"candidate_id":"cand_0807c6428416b020e630","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَبْل","morph_features":"STEM|POS:N|LEM:Habol|ROOT:Hbl|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:3:1","qac_word_ref":"111:5:3","surface_ar":"حَبْلٌ"}],"gloss":"avı yakalayan ipli tuzak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Avın takılıp yakalandığı ipli tuzak."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tuzağı kurma, avı onunla yakalama, kuran kişi ve yakalanmış av."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ölüme veya ayartılmaya götüren nedenlerin tuzağa benzetilmesi."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Tuzak kuran ile ok atan avcı üzerinden korku veya karışıklık anlatan kalıplaşmış sözler."}}],"root_ar":"ح ب ل","root_id":"root_000291","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın düzenek ve yakalama işlevinden oluşan tam çekirdeğini karşılar.","boundary_detail":"Dalın çekirdeği yakalayan düzenektir; ölüm ve ayartma anlatımları mecaz, avcı-okçu sözleri ise ilişkili kalıplaşmış kullanımlardır.","branch_image_ar":"حبالة تصيد وتوقع","concept_gloss":"avı yakalayan ipli tuzak","contextual_glosses":[{"applicability":"Avın düzenek kurularak yakalanması eyleminde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tuzak kurma ve avı yakalama işlemini korur."},"facet_ids":["F002"],"text":"tuzağa düşürmek","usage_role":"contextual"},{"applicability":"Ölüm nedenlerinin yakalayan tuzaklar gibi sunulduğu mecazda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kaçışı engelleyen neden ve ölüm sonucunu korur."},"facet_ids":["F003"],"text":"ölüme götüren tuzaklar","usage_role":"explanatory"}],"definition":"Avı yakalamak için kurulan ipli tuzak ve bu tuzağı kurarak avı yakalama sürecidir. Tuzağı kuran, tuzağa düşen av, insanı ölüme veya ayartmaya götüren nedenler ve avcılarla ilgili kalıplaşmış sözler bu çekirdeğe bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Avın takılıp yakalandığı ipli tuzak."},{"facet_id":"F002","role":"specialization","statement":"Tuzağı kurma, avı onunla yakalama, kuran kişi ve yakalanmış av."},{"facet_id":"F003","role":"extension","statement":"Ölüme veya ayartılmaya götüren nedenlerin tuzağa benzetilmesi."},{"facet_id":"F004","role":"associated_use","statement":"Tuzak kuran ile ok atan avcı üzerinden korku veya karışıklık anlatan kalıplaşmış sözler."}],"identity_rationale":"Kaynak ifadesi avı yakalayan tuzağı, onu kurma ve tuzağa düşme sürecini, kuran ile yakalananı ve buradan gelişen mecazları tek bir işlevsel çekirdekte toplar.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"avı tuzak kurarak yakalamak"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"avı ipli tuzakla yakalamak"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"ipli av tuzağı"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"av tuzağını kuran kişi"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"tuzağa yakalanmış av"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"ölüme götüren tuzaklar ve nedenler"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kötülüğe sürükleyen ayartma tuzakları"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"ortalığın karışması veya her yandan korku gelmesi"}],"lexicalization_note":"Genel tuzak çekirdeği; kurma, yakalama, yakalanan av, mecaz ve kalıplaşmış söz yüzlerinden ayrı olarak tanımlanır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; düzenek, kurulmuş kapan ve yakalanma durumu arasındaki sınırı en açık veren üçü seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal düzenek ve mecazla sınırlı kalırken odak dal bütün yakalama sürecini ve katılımcılarını da adlandırır.","focus_only":"Tuzak kurma eylemini, kuranı, yakalananı ve avcı sözlerini de kapsar.","gloss":"avcının tuzağı","neighbor_only":"Kuşlar için kurulan biçimi ayrıca belirginleştirir.","neighbor_ref":"root_000791/B006","relation_type":"near_synonym","shared_zone":"İki dalın çekirdeği avın takılıp kaldığı tuzaktır."},{"boundary_match":"partial","distinction":"Odak dal özellikle ipli av tuzağını ve türev rollerini, komşu dal ise kurulmuş kapan sınıfını öne çıkarır.","focus_only":"İpli tuzağı, avcıyı ve yakalanan avı birlikte kapsar.","gloss":"kurulmuş kapan","neighbor_only":"Kurulmuş kapanların genel sınıfını ve insanı düşürmeye yönelik kurulumu da kapsar.","neighbor_ref":"root_000879/B004","relation_type":"near_synonym","shared_zone":"Yakalamak için önceden kurulan düzenek ortak çekirdektir."},{"boundary_match":"partial","distinction":"Odak dal düzenek ile yakalama eylemini merkez alır; komşu dal yakalananın takılı kalmış durumunu merkez alır.","focus_only":"Yakalama düzeneğini kurma ve kullanma sürecini içerir.","gloss":"tuzağa takılıp kalmak","neighbor_only":"Avın tuzağa takılıp kurtulamaması durumuna ve boyun halkasına odaklanır.","neighbor_ref":"root_001506/B001","relation_type":"near_neighbor","shared_zone":"Tuzağa yakalanma olayı iki dalı birleştirir."}],"source_phrase_ar":"الحبل مصدر حبلت الصيد واحتبلته أي أخذته والحبالة المصيدة وحبائل الموت أسبابه (ayn)؛ الحبالة شرك الصائد والصيد محبول ومحتبل إذا وقع في الحبالة وأنا بين حابل ونابل (jamhara)؛ الحبالة التي يصاد بها والحابل الذي ينصب الحبالة والمحبول الوحشي الذي نشب في الحبالة واحتبله أي اصطاده بالحبالة واختلط الحابل بالنابل (sihah)؛ الحبل مصدر حبلت الصيد واحتبلته إذا نصبت له حبالة فنشب فيها والحبالة المصيدة وثار حابلهم على نابلهم (tahdhib)؛ الحبالة خصت بحبل الصائد والنساء حبائل الشيطان والمحتبل والحابل صاحب الحبالة (mufradat)؛ الحبالة حبالة الصائد واحتبل الصيد إذا صاده بالحبالة (maqayis)","source_summary":"Kaynaklar av tuzağı, tuzakla yakalama, tuzağı kuran ve yakalanan av üzerinde birleşir; ölüm, ayartma ve avcı sözleri de toplu kanıtta yer alır.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الحبالة والمصيدة وحبل الصيد واحتبال الصيد والحابل والمحتبل وما استعير لأسباب الموت أو حبائل الشيطان وأمثال الحابل والنابل","what_is_not_ar":"لا يدخل فيه حبل العهد والأمان ولا الحمل في البطن"},"support_links":["sup_500faf58bc2cb81867aa"]},{"boundary":"Gebelik çekirdektir; kuşak içindeki sonraki yavru, gebelik başlangıcının zamanı ve rahimdeki yer ayrı özelleşmelerdir.","branch_kind":"mixed_non_bare","branch_ref":"root_000291/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَبْل","morph_features":"STEM|POS:N|LEM:Habol|ROOT:Hbl|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:3:1","qac_word_ref":"111:5:3","surface_ar":"حَبْلٌ"}],"gloss":"gebelik ve karındaki yavru","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadın veya başka bir dişinin karnında yavru taşıması ve gebe olması."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gebelikte karında bulunan yavrunun kendisinin adlandırılması."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Karındaki yavrunun gelecekte doğuracağı yavru, yani bir sonraki kuşak."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Gebeliğin başladığı zaman veya yavrunun rahimde yerleştiği bölüm."}}],"root_ar":"ح ب ل","root_id":"root_000291","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın durum ile taşınan yavruyu birlikte içeren temel kapsamını karşılar.","boundary_detail":"Gebelik çekirdektir; kuşak içindeki sonraki yavru, gebelik başlangıcının zamanı ve rahimdeki yer ayrı özelleşmelerdir.","branch_image_ar":"حمل يمتد في البطن","concept_gloss":"gebelik ve karındaki yavru","contextual_glosses":[{"applicability":"Kadın veya başka bir dişinin gebeliğe girmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gebeliğin başlamasını ve dişi katılımcıyı korur."},"facet_ids":["F001"],"text":"gebe kalmak","usage_role":"contextual"},{"applicability":"Henüz karındaki yavrunun gelecekte doğuracağı sonraki kuşak anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki aşamalı kuşak ilişkisini açıkça korur."},"facet_ids":["F003"],"text":"yavrunun ilerideki yavrusu","usage_role":"explanatory"}],"definition":"Bir kadın veya dişinin yavru taşıdığı gebelik durumu ve karnındaki yavrudur. Henüz doğmamış yavrunun ilerideki yavrusu ile gebeliğin başladığı zaman veya rahimdeki yer bu çekirdeğin özel uzantılarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadın veya başka bir dişinin karnında yavru taşıması ve gebe olması."},{"facet_id":"F002","role":"extension","statement":"Gebelikte karında bulunan yavrunun kendisinin adlandırılması."},{"facet_id":"F003","role":"specialization","statement":"Karındaki yavrunun gelecekte doğuracağı yavru, yani bir sonraki kuşak."},{"facet_id":"F004","role":"specialization","statement":"Gebeliğin başladığı zaman veya yavrunun rahimde yerleştiği bölüm."}],"identity_rationale":"Kaynak ifadesi gebeliği, gebe dişiyi, karındaki yavruyu, yavrunun ilerideki yavrusunu ve gebeliğin zaman ya da yerini aynı üreme alanında açıkça sıralar.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"gebelik veya karındaki yavru"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"kadın gebe kaldı"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"gebe dişi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"karındaki yavrunun ilerideki yavrusu"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"gebeliğin başladığı zaman veya yer"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"yavrunun rahimde yerleştiği bölüm"}],"lexicalization_note":"Genel gebelik anlamı ile kadın, hayvan, sonraki kuşak ve gebeliğin zamanı ya da yeri için kullanılan sınırlı biçimler ayrılır.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; gebelik, rahimde tutunma ve rahmin içeriği arasındaki aşama ve kapsam farklarını gösteren üçü seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal gebeliği bitkisel ürüne de yayar; odak dal ise üreme sürecinin kuşak, zaman ve yer ayrıntılarını kapsar.","focus_only":"Gebe dişiyi, sonraki kuşağı ve gebeliğin başlangıç zamanı ya da yerini kapsar.","gloss":"içte taşınan yavru ve meyve","neighbor_only":"Aynı taşıma görüntüsünü ağacın ürünü ve meyvesine de genişletir.","neighbor_ref":"root_000357/B002","relation_type":"near_synonym","shared_zone":"Kadın veya dişinin karnında yavru taşıması iki dalın ortak çekirdeğidir."},{"boundary_match":"partial","distinction":"Komşu dal başlangıçtaki tutunma aşamasını, odak dal ise gebeliğin daha geniş durumunu ve ilişkili adları anlatır.","focus_only":"Gebeliğin sürmesini, gebe dişiyi ve sonraki kuşağı kapsar.","gloss":"döllenmenin rahimde tutunması","neighbor_only":"Döllenmenin tutunup rahimde sabitlenmesi aşamasına odaklanır.","neighbor_ref":"root_001039/B009","relation_type":"near_synonym","shared_zone":"Gebeliğin oluşması ve rahimde yavru taşınması ortak alandır."},{"boundary_match":"partial","distinction":"Odak dal gebelik durumunu ve kuşak ilişkisini, komşu dal rahmin içeriğini ve onun dışarı atılmasını öne çıkarır.","focus_only":"Gebe olma, gebe dişi, sonraki kuşak ve başlangıç zamanı gibi ayrıntıları kapsar.","gloss":"rahmin taşıdığı içerik","neighbor_only":"Rahmin topladığı yavru veya kanı ve bazı anlatımlarda doğum artıklarının atılmasını kapsar.","neighbor_ref":"root_001211/B003","relation_type":"near_synonym","shared_zone":"Rahimde yavru bulunması ve taşınması iki dalda ortaktır."}],"source_phrase_ar":"حبلت المرأة حبلا فهي حبلى وحبل الحبلة ولد الولد الذي في البطن (ayn)؛ حبلت من الإنس وغيرهم وربما سمي ما في البطن بعينه حبلا والمحبل وقت الحبل وحبل الحبلة ما يكون في بطن الناقة التي هي في بطن أمها (jamhara)؛ الحبل الحمل وقد حبلت المرأة فهي حبلى وحبل الحبلة نتاج النتاج وولد الجنين وكان ذلك في محبل فلان أي في وقت حبل أمه به (sihah)؛ حبلت المرأة تحبل حبلا وهي حبلى وحبل الحبلة ولد الولد الذي في البطن والمحبل موضع الحبل (tahdhib)؛ الحبل وهو الحمل وذلك أن الأيام تمتد به (maqayis)؛ المهبل مستقر الولد من الرحم وهو من باب الإبدال وأصله محبل (maqayis)","source_summary":"Kaynaklar gebelik, gebe dişi ve karındaki yavru çekirdeğinde birleşir; sonraki kuşak ile gebeliğin zamanı ve yeri de toplu kanıtta belirtilir.","sources":["AY","JA","SI","TA","MQ"],"what_is_ar":"يدخل فيه حبل المرأة والأنثى والحبلى وما في البطن وحبل الحبلة ووقت الحبل ومحبل الحمل ومستقر الولد بإبدال المهبل عن محبل","what_is_not_ar":"لا يدخل فيه الحبل الرسن ولا الحبلة النباتية ولا الحلي المسمى حبلة"},"support_links":[]},{"boundary":"Dal yalnız bitki alanındaki kullanımları toplar; asma, ağaç meyvesi ve fasulye yüzleri birbirinin yerine kullanılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000291/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَبْل","morph_features":"STEM|POS:N|LEM:Habol|ROOT:Hbl|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:3:1","qac_word_ref":"111:5:3","surface_ar":"حَبْلٌ"}],"gloss":"asma sürgünü ve bitkisel adlar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Üzüm asması, asmanın kökü veya ondan çıkan bir sürgün."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli dikenli ağaçların meyvesi veya benzer bir ağaç türü."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bölgesel kullanımda fasulye adı."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir kertenkelenin bu bitkiyi otladığını bildiren sınırlı niteleme."}}],"root_ar":"ح ب ل","root_id":"root_000291","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tek bir tür eşitliği kurmadan dalın bitki alanındaki çoklu kapsamını gösterir.","boundary_detail":"Dal yalnız bitki alanındaki kullanımları toplar; asma, ağaç meyvesi ve fasulye yüzleri birbirinin yerine kullanılmaz.","branch_image_ar":"حبلة نبات وثمر ممتد","concept_gloss":"asma sürgünü ve bitkisel adlar","contextual_glosses":[{"applicability":"Üzüm asmasının tek bir dalı veya sürgünü anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Asmaya bağlı tek sürgün anlamını korur."},"facet_ids":["F001"],"text":"asma sürgünü","usage_role":"contextual"},{"applicability":"Dikenli ağaçların ürünü söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Meyve olmayı ve ağaç grubunu korur."},"facet_ids":["F002"],"text":"dikenli ağaç meyvesi","usage_role":"explanatory"}],"definition":"Üzüm asmasının bir sürgünü veya asmanın kendisi için kullanılan bitki adıdır; ayrıca belirli dikenli ağaçların meyvesini, bir ağaç türünü ve bölgesel olarak fasulyeyi adlandıran ayrı kullanımları vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Üzüm asması, asmanın kökü veya ondan çıkan bir sürgün."},{"facet_id":"F002","role":"source_variant","statement":"Belirli dikenli ağaçların meyvesi veya benzer bir ağaç türü."},{"facet_id":"F003","role":"source_variant","statement":"Bölgesel kullanımda fasulye adı."},{"facet_id":"F004","role":"associated_use","statement":"Bir kertenkelenin bu bitkiyi otladığını bildiren sınırlı niteleme."}],"identity_rationale":"Kaynak ifadesi üzüm asmasının sürgünü veya kökü, dikenli ağaçların meyvesi, bir ağaç türü ve bölgesel fasulye adını aynı bitki alanında verir; bunlar tek bir botanik gönderge değil, kaynakta yan yana duran ayrı bitkisel kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"asma veya asma sürgünü"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"dikenli ağaçların meyvesi"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"bölgesel dilde fasulye"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"bu bitkiyi otlayan kertenkele"}],"lexicalization_note":"Çıplak bitki adları ile yalnız hayvanın o bitkiyi otlamasını bildiren yapı birbirine karıştırılmadan ayrı yüzlerde verilir.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; asma, ağaç meyvesi ve genel yeşil bitki sınırlarını açıklayan üçü seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal üzüm bitkisinin genel adıdır; odak dal asma sürgününden hareket eder ve başka bitkisel adlara da ayrılır.","focus_only":"Asmanın tek sürgününü ve ayrıca başka ağaç meyveleriyle fasulyeyi kapsar.","gloss":"üzüm asması ve üzüm","neighbor_only":"Üzüm bitkisini, ağacını ve meyvesini genel adlarıyla kapsar.","neighbor_ref":"root_001294/B004","relation_type":"near_neighbor","shared_zone":"Üzüm asması iki dalın ortak bitkisel alanıdır."},{"boundary_match":"partial","distinction":"Komşu dal tek bir ağaç meyvesine özgüdür; odak dalın meyve yüzü daha geniş bir ağaç grubuyla birlikte başka bitki yüzlerine bağlıdır.","focus_only":"Asma sürgünü, ağaç türü ve bölgesel fasulye anlamlarını da taşır.","gloss":"belirli ağaç meyvesi","neighbor_only":"Özellikle belirli bir çöl ağacının meyvesini adlandırır.","neighbor_ref":"root_000104/B007","relation_type":"near_synonym","shared_zone":"Dikenli ağaçların meyvesini adlandırma alanında örtüşürler."},{"boundary_match":"field_only","distinction":"Odak dal belirli bitki ve meyve adlarından oluşur; komşu dal ise ağaç dışı taze bitkilerin genel sınıfıdır.","focus_only":"Asma sürgünü, ağaç meyvesi ve fasulye gibi belirli göndergeleri adlandırır.","gloss":"taze yeşil bitki","neighbor_only":"Ağaç sayılmayan taze ve yeşil bitkilerin genel sınıfını anlatır.","neighbor_ref":"root_000141/B001","relation_type":"same_field","shared_zone":"İki dal bitkiler alanına aittir."}],"source_phrase_ar":"الحبلة طاقة من قضبان الكرم والحبل نوع من الشجر مثل السمر (ayn)؛ الحبلة الكرم والأحبل الذي يسمى اللوبياء لغة يمانية (jamhara)؛ الحبلة ثمر العضاه والحبلة القضيب من الكرم وضب حابل يرعى الحبلة (sihah)؛ الكرمة حبلة والحبلة طاق من قضبان الكرم والحبلة ثمر السمر وثمر العضاه والأحبل اللوبياء (tahdhib)؛ الكرم يقال له حبلة وحبلة لأنه في نباته كالأرشية والحبلة ثمر العضاة (maqayis)","source_summary":"Toplu kanıt üzüm asması ve sürgününü, dikenli ağaç meyvesini, benzer bir ağaç türünü ve bölgesel fasulye adını ayrı bitkisel kullanımlar olarak verir.","sources":["AY","JA","SI","TA","MQ"],"what_is_ar":"يدخل فيه الحبلة من قضبان الكرم وأصل الكرمة وضرب من الشجر وثمر العضاه أو السمر والأحبل بمعنى اللوبياء","what_is_not_ar":"لا يدخل فيه الحبلة بمعنى الحلي ولا حبل الحبلة في الحمل ولا الحنبل إذا كان مادة أخرى"},"support_links":[]},{"boundary":"Bu dal yalnız kolye süsünü kapsar; asma sürgünü, ağaç meyvesi ve sonraki kuşak anlamları dışarıda kalır.","branch_kind":"bare","branch_ref":"root_000291/B008","candidate_links":[{"candidate_id":"cand_2fdced5c1589ea1bdfdc","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَبْل","morph_features":"STEM|POS:N|LEM:Habol|ROOT:Hbl|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:3:1","qac_word_ref":"111:5:3","surface_ar":"حَبْلٌ"}],"gloss":"kolyeye takılan süs parçası","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kolyenin üzerinde yer alan, biçimlendirilmiş süs öğesi."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu parçaların başka süslerle birlikte bir kolye dizisi oluşturması."}}],"root_ar":"ح ب ل","root_id":"root_000291","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın nesne türünü ve kolyedeki işlevini tam olarak karşılar.","boundary_detail":"Bu dal yalnız kolye süsünü kapsar; asma sürgünü, ağaç meyvesi ve sonraki kuşak anlamları dışarıda kalır.","branch_image_ar":"حبلة حلي في القلادة","concept_gloss":"kolyeye takılan süs parçası","definition":"Kolyelere takılan veya kolye dizisine yerleştirilen belirli bir süs parçasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kolyenin üzerinde yer alan, biçimlendirilmiş süs öğesi."},{"facet_id":"F002","role":"associated_use","statement":"Bu parçaların başka süslerle birlikte bir kolye dizisi oluşturması."}],"identity_rationale":"Kaynak ifadesi, kolyeye yerleştirilen belirli bir süs parçasını tutarlı biçimde gösterir; bitki ve gebelik kullanımlarıyla yalnız biçim ortaklığı vardır.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"kolyeye takılan süs parçası"}],"lexicalization_note":"Tanım çıplak biçimin kolyeye takılan süs anlamıyla sınırlıdır ve başka yapılardaki benzer biçimleri içeri almaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; parça, ayırıcı boncuk ve bütün süs dizisi farkını gösteren üç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kolyedeki tek tür parçayı, komşu dal ise yuvarlak süsü veya bütün boncuklu diziyi anlatır.","focus_only":"Kolyeye yerleştirilen belirli bir süs parçasıyla sınırlıdır.","gloss":"yuvarlak veya boncuklu süs","neighbor_only":"Yuvarlak bir süsü veya boncuklu ve gümüş hilalli bütün bir ipi kapsar.","neighbor_ref":"root_000372/B007","relation_type":"near_synonym","shared_zone":"İki dal boyna takılan dizili süsler alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal süs parçasını adlandırır; komşu dal parçanın iki inciyi ayıran yerleşim işlevini öne çıkarır.","focus_only":"Kolyenin süs öğesinin kendisidir.","gloss":"inciler arasındaki ayırıcı boncuk","neighbor_only":"İki inci arasına ayırıcı boncuk veya taş yerleştirme düzenini anlatır.","neighbor_ref":"root_001159/B012","relation_type":"near_neighbor","shared_zone":"Kolyede dizilen küçük süs öğeleri ortak alandır."},{"boundary_match":"field_only","distinction":"Komşu dal gümüş malzemeyi ve boncuk dizisini gerektirir; odak dal yalnız kolyeye takılan belirli süs türünü belirtir.","focus_only":"Malzemesi belirtilmeyen kolye süsüdür.","gloss":"dizili gümüş boncuk","neighbor_only":"Dizilmiş gümüş boncuk veya gümüş taneciklerden oluşur.","neighbor_ref":"root_001206/B006","relation_type":"same_field","shared_zone":"İki dal kolyelik boncuk ve süs alanındadır."}],"source_phrase_ar":"الحبلة ضرب يصاغ من الحلي (jamhara)؛ الحبلة أيضا حلى يجعل في القلائد وقلائد من حبلة وسلوس (sihah)؛ الحبلة حلي كان يجعل في القلائد في الجاهلية وقلائد من حبلة وسلوس (tahdhib)؛ الحبلة اسم لما يجعل في القلادة (mufradat)؛ الحبلة حلي يجعل في القلائد ولعله مشبه بثمره (maqayis)","source_summary":"Kaynaklar bunun kolyeye yerleştirilen işlenmiş bir süs olduğu konusunda birleşir; kimi anlatımlar onu kolye dizisinin bir öğesi olarak açıklar.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الحبلة أو الحبلة ضربا من الحلي يجعل في القلائد","what_is_not_ar":"لا يدخل فيه الحبلة من الكرم أو ثمر الشجر ولا حبل الحبلة في الحمل"},"support_links":["sup_57e3c6af36af0c4bffed"]},{"boundary":"Adlandırılmış yer ile atların başlangıçta beklediği alan ayrı yüzlerdir; sıradan uzun kum oluşumu bu dala ancak özel ad olmuşsa girer.","branch_kind":"mixed_non_bare","branch_ref":"root_000291/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَبْل","morph_features":"STEM|POS:N|LEM:Habol|ROOT:Hbl|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:3:1","qac_word_ref":"111:5:3","surface_ar":"حَبْلٌ"}],"gloss":"yer adı ve at yarışı başlangıç alanı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kaynaklarda belirli bir kıyı yerini veya şiirde geçen yeri adlandıran özel kullanım."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yarış atlarının salınmadan önce durduğu başlangıç alanı."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yer adının atların başlangıç alanından türediğini bildiren adlandırma açıklaması."}}],"root_ar":"ح ب ل","root_id":"root_000291","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Birbirine adlandırma yoluyla bağlanan iki kaynak yüzünü genelleştirmeden gösterir.","boundary_detail":"Adlandırılmış yer ile atların başlangıçta beklediği alan ayrı yüzlerdir; sıradan uzun kum oluşumu bu dala ancak özel ad olmuşsa girer.","branch_image_ar":"حبل موضع وموقف","concept_gloss":"yer adı ve at yarışı başlangıç alanı","contextual_glosses":[{"applicability":"Yarış atlarının bırakılmadan önce toplandığı alan anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Atları, yarış öncesini ve bekleme yerini korur."},"facet_ids":["F002"],"text":"atların çıkış öncesi bekleme yeri","usage_role":"explanatory"}],"definition":"Kaynaklarda belirli bir yerin adı ve yarış atlarının salınmadan önce beklediği başlangıç alanı olarak kullanılır. Bir anlatım, söz konusu yer adının bu başlangıç alanından geldiğini bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kaynaklarda belirli bir kıyı yerini veya şiirde geçen yeri adlandıran özel kullanım."},{"facet_id":"F002","role":"source_variant","statement":"Yarış atlarının salınmadan önce durduğu başlangıç alanı."},{"facet_id":"F003","role":"associated_use","statement":"Yer adının atların başlangıç alanından türediğini bildiren adlandırma açıklaması."}],"identity_rationale":"Kaynak ifadesi hem belirli bir yer adını hem yarış atlarının salınmadan önce beklediği başlangıç yerini verir ve bir anlatım yer adını bu başlangıç alanına bağlar; bu nedenle genel bir yer anlamı kurulamaz.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"kaynaklarda adı verilen belirli bir yer"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"bir kentteki yarış alanının başlangıç bölümü"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"atların yarıştan önce beklediği başlangıç yeri"}],"lexicalization_note":"Tanım yer adı kullanımını ve at yarışına özgü başlangıç alanını ayırır; bunlardan genel bir çıplak yer anlamı türetmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; doğal arazi, alışılmış yer ve salt yer adıyla karışma sınırını gösteren üçü seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal özel ad ve işlevsel başlangıç alanını, komşu dal ise doğal kum biçimini anlatır.","focus_only":"Belirli bir yer adı veya at yarışına ayrılmış başlangıç alanıdır.","gloss":"uzun kum sırtı","neighbor_only":"Özel ad olmayan, uzunlamasına uzanan doğal kum oluşumudur.","neighbor_ref":"root_000291/B003","relation_type":"same_field","shared_zone":"İki dal arazi veya yer algısıyla ilişkilidir."},{"boundary_match":"field_only","distinction":"Komşu dal yerin tanınmışlık ve geri dönülme niteliğini, odak dal ise özel ad veya yarış işlevini gerektirir.","focus_only":"Özel yer adı ve atların başlangıç alanını içerir.","gloss":"alışılmış ve bilinen yer","neighbor_only":"İnsanların tanıdığı, geri döndüğü veya bir durumu bildiği alışılmış yeri anlatır.","neighbor_ref":"root_001055/B005","relation_type":"same_field","shared_zone":"Her iki dal bir mekânı konu edinir."},{"boundary_match":"field_only","distinction":"Komşu dal genel olarak yer adı türünü gösterir; odak dal belirli adlandırmayı yarış başlangıcıyla ilişkilendirir.","focus_only":"Belirli bir yer adıyla yarış başlangıç alanını birlikte taşır.","gloss":"yer adı","neighbor_only":"Bir sözcüğün kaynakta doğrudan yer adı türünde açıklanmasıyla sınırlıdır.","neighbor_ref":"root_000248/B011","relation_type":"same_field","shared_zone":"İki dal da bir yeri adlandıran söz varlığı alanındadır."}],"source_phrase_ar":"الحبل موضع بالبصرة على شاطىء النهر (ayn)؛ الحبل موضع والحبل موقف خيل الحلبة قبل أن تطلق وبه سمي حبل البصرة (jamhara)؛ حبل موضع في شعر لبيد (tahdhib)","source_summary":"Toplu kanıt belirli bir yer adını ve yarış atlarının başlangıçta beklediği alanı birlikte verir; yer adının bu alandan geldiği açıklaması da aynı kanıttadır.","sources":["AY","JA","TA"],"what_is_ar":"يدخل فيه حبل علما لموضع بالبصرة أو في الشعر وموقف الخيل قبل الإطلاق","what_is_not_ar":"لا يدخل فيه الرمل المستطيل إذا لم يكن علما لموضع ولا حبل الرسن"},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000291/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَبْل","morph_features":"STEM|POS:N|LEM:Habol|ROOT:Hbl|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:3:1","qac_word_ref":"111:5:3","surface_ar":"حَبْلٌ"}],"gloss":"biçime bağlı adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun adı ve o topluluğa mensubiyeti bildiren sıfat biçimleri."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Topluluk göndergesinden bağımsız olarak kullanılan erkek adı."}}],"root_ar":"ح ب ل","root_id":"root_000291","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"نسبة واسم إلى الحبلى","concept_gloss":"biçime bağlı adlandırmalar","contextual_glosses":[{"applicability":"Topluluğa bağlılığı bildiren sıfat biçimleri için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mensubiyet ilişkisini ve topluluk hedefini korur."},"facet_ids":["F001"],"text":"belirli bir topluluğa mensup","usage_role":"explanatory"},{"applicability":"Topluluk anlamından bağımsız kişi adı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişi adı olmayı ve bağımsız kimliği korur."},"facet_ids":["F002"],"text":"bir erkek adı","usage_role":"explanatory"}],"definition":"Bu dal tek bir kavram oluşturmaz: bir topluluğun adı ve o topluluğa bağlılığı bildiren sıfatlar ile bağımsız bir erkek adı aynı yerde toplanmıştır. Kişi adı ayrılmadan ortak bir tanım kurulamaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun adı ve o topluluğa mensubiyeti bildiren sıfat biçimleri."},{"facet_id":"F002","role":"source_variant","statement":"Topluluk göndergesinden bağımsız olarak kullanılan erkek adı."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"belirli bir topluluğa mensup"},{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"kaynaklarda adı verilen bir topluluk"},{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"bir erkek adı"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"فلان الحبلي منسوب إلى حي من اليمن (ayn)؛ بنو الحبلى بطن من العرب (jamhara)؛ حبال اسم رجل (sihah)؛ الحبلي منسوب إلى حي من اليمن وبنو الحبلى من الأنصار وحبلوي وحبلي وحبلاوي (tahdhib)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["AY","JA","SI","TA"],"what_is_ar":"يدخل فيه الحبلي والحبلوي والحبلاوي نسبة إلى حي أو بني الحبلى واسم حبال علما لشخص","what_is_not_ar":"لا يدخل فيه الحمل والحبلى إذا كان وصفا للأنثى الحامل"},"support_links":[]},{"boundary":"Bela anlamı ile uyanık kişi nitelemesi ayrı yüzlerdir; tuzak benzetmesi açıklayıcı köprü, genel hile ise dış sınırdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000291/B011","candidate_links":[{"candidate_id":"cand_0807c6428416b020e630","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَبْل","morph_features":"STEM|POS:N|LEM:Habol|ROOT:Hbl|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:3:1","qac_word_ref":"111:5:3","surface_ar":"حَبْلٌ"}],"gloss":"ağır bela","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin başına gelen ağır bela, yıkıcı olay veya içinden çıkılması güç durum."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bilgili, uyanık ve keskin kavrayışlı kişi için kullanılan niteleme."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bela anlamının tuzağa yakalanmış olma görüntüsüyle açıklanması."}}],"root_ar":"ح ب ل","root_id":"root_000291","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kişiyi yakalayıp çıkmaza sokan olay çekirdeğini karşılar.","boundary_detail":"Bela anlamı ile uyanık kişi nitelemesi ayrı yüzlerdir; tuzak benzetmesi açıklayıcı köprü, genel hile ise dış sınırdır.","branch_image_ar":"داهية تحبل بصاحبها","concept_gloss":"ağır bela","contextual_glosses":[{"applicability":"Bir insanın bilgisi, uyanıklığı ve güçlü sezgisi övüldüğünde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilgili, uyanık ve keskin kavrayışlı kişi niteliğini korur."},"facet_ids":["F002"],"text":"uyanık ve keskin kavrayışlı kişi","usage_role":"contextual"}],"definition":"İnsanı bir tuzağa düşmüş gibi çaresiz bırakan ağır bela veya yıkıcı olaydır. Ayrı bir kişi nitelemesinde bilgili, uyanık ve keskin kavrayışlı kimseyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin başına gelen ağır bela, yıkıcı olay veya içinden çıkılması güç durum."},{"facet_id":"F002","role":"associated_use","statement":"Bilgili, uyanık ve keskin kavrayışlı kişi için kullanılan niteleme."},{"facet_id":"F003","role":"source_variant","statement":"Bela anlamının tuzağa yakalanmış olma görüntüsüyle açıklanması."}],"identity_rationale":"Kaynak ifadesi ağır bela veya yıkıcı olay anlamını ve bilgili, uyanık, keskin kavrayışlı kişi nitelemesini destekler; genel hile ya da düzenbazlık eylemi ise doğrudan dal çekirdeği değildir.","lexical_glosses":[{"lexical_unit_id":"lu_041","rendering_kind":"ordinary","target_gloss":"ağır bela veya çıkmaza düşüren olay"},{"lexical_unit_id":"lu_042","rendering_kind":"ordinary","target_gloss":"bilgili, uyanık ve keskin kavrayışlı adam"}],"lexicalization_note":"Çıplak bela adı ile yalnız kişi nitelemesinde görülen bilgili ve uyanık anlam birbirine karıştırılmadan tanımlanır.","neighbor_coverage_note":"Adayların tümü karşılaştırıldı; bela, kasıtlı düzen ve gerçek tuzak arasındaki ilişkiyi gösteren üçü seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal dikkatli kuşu da kapsar; odak dal ise belayı tuzağa düşme görüntüsüyle açıklar ve kişi yüzünü bilgiyle niteler.","focus_only":"Bela ile tuzağa yakalanma arasında açıklayıcı bağ kurar ve bilgili kişiyi niteler.","gloss":"bela ve keskin görüşlü kişi","neighbor_only":"Keskin görüşlü kişiyi ve dikkatli kuşu da aynı niteleme alanında kapsar.","neighbor_ref":"root_000140/B004","relation_type":"near_synonym","shared_zone":"Ağır bela ve becerikli, uyanık kişi anlamları iki dalda örtüşür."},{"boundary_match":"partial","distinction":"Odak dal bela sonucunu ve kişi niteliğini, komşu dal ise bu sonucu doğurabilecek kasıtlı düzen kurma eylemini merkez alır.","focus_only":"Ortaya çıkan ağır belayı veya uyanık kişiyi adlandırır.","gloss":"kötü amaçlı düzen kurma","neighbor_only":"Kötülük amacıyla kurulan düzeni, kandırmayı ve adım adım tuzağa çekmeyi anlatır.","neighbor_ref":"root_001334/B002","relation_type":"near_neighbor","shared_zone":"Birini zarara veya çıkmaza götüren düzen görüntüsü ortaktır."},{"boundary_match":"partial","distinction":"Komşu dal gerçek düzenek ve yakalama sürecidir; odak dal bu görüntüyle açıklanan bela anlamıdır.","focus_only":"Tuzağa benzetilen ağır olay ve uyanık kişi nitelemesidir.","gloss":"av tuzağı","neighbor_only":"Gerçek av düzeneğini, kurma eylemini, avcıyı ve yakalanan avı kapsar.","neighbor_ref":"root_000291/B005","relation_type":"near_neighbor","shared_zone":"Yakalanıp çıkamama görüntüsü iki dalı birbirine bağlar."}],"source_phrase_ar":"الحبل الداهية والجمع حبول (jamhara)؛ الحبل بالكسر الداهية والجمع الحبول (sihah)؛ الحبل الرجل العالم الفطن الداهي والحبل الداهية وجمعه حبول (tahdhib)؛ الحبل بكسر الحاء وهي الداهية ووجهه أن الإنسان إذا دهي فكأنه قد حبل أي وقع في الحبالة (maqayis)","source_summary":"Kaynaklar ağır bela anlamında birleşir; toplu kanıt ayrıca bilgili ve uyanık kişi nitelemesini ve bela ile tuzak arasındaki açıklayıcı bağı verir.","sources":["JA","SI","TA","MQ"],"what_is_ar":"يدخل فيه الحبل بمعنى الداهية والخبث والحيلة والرجل الداهي الفطن إذا صرح المصدر بذلك","what_is_not_ar":"لا يدخل فيه الحبالة الحسية ولا الشجاعة والثبات في حبيل براح"},"support_links":["sup_500faf58bc2cb81867aa"]},{"boundary":"Yerinden kaçmayan cesur kişi çekirdektir; aslan benzetmesi ve ölüm kullanımı bağımlı yüzlerdir.","branch_kind":"mixed_non_bare","branch_ref":"root_000291/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَبْل","morph_features":"STEM|POS:N|LEM:Habol|ROOT:Hbl|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:3:1","qac_word_ref":"111:5:3","surface_ar":"حَبْلٌ"}],"gloss":"yerinden kaçmayan cesur kişi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tehlike karşısında yerinde duran ve kaçmayan cesur kişi."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı sabitlik ve cesaret niteliğiyle aslanın adlandırılması."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kalıplaşmış sözün ölüm için de kullanıldığını bildiren sınırlı aktarım."}}],"root_ar":"ح ب ل","root_id":"root_000291","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalıplaşmış sözün insan için taşıdığı tam davranışsal çekirdeği karşılar.","boundary_detail":"Yerinden kaçmayan cesur kişi çekirdektir; aslan benzetmesi ve ölüm kullanımı bağımlı yüzlerdir.","branch_image_ar":"حبيل براح ثابت لا يفر","concept_gloss":"yerinden kaçmayan cesur kişi","contextual_glosses":[{"applicability":"Kalıplaşmış nitelemenin aslana uygulandığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aslan göndergesini ve yerinden kaçmama niteliğini korur."},"facet_ids":["F002"],"text":"yerini bırakmayan aslan","usage_role":"contextual"},{"applicability":"Aynı sözün ölüm için kullanıldığı sınırlı kaynak bağlamını açıklar.","error_profile":{"adds":"Kaynak ifadesinde açıkça kurulmamış kaçınılmazlık yorumunu ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Ölüm göndergesini ve kaçışsızlık çağrışımını korur."},"facet_ids":["F003"],"text":"kaçınılmaz ölüm","usage_role":"explanatory"}],"definition":"Yerini bırakmayan, düşman karşısında kaçmayan cesur kişi için kullanılan kalıplaşmış nitelemedir; aslana da uygulanır. Aynı sözün ölüm için kullanıldığı sınırlı bir aktarım ayrıca bildirilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tehlike karşısında yerinde duran ve kaçmayan cesur kişi."},{"facet_id":"F002","role":"extension","statement":"Aynı sabitlik ve cesaret niteliğiyle aslanın adlandırılması."},{"facet_id":"F003","role":"source_variant","statement":"Kalıplaşmış sözün ölüm için de kullanıldığını bildiren sınırlı aktarım."}],"identity_rationale":"Kaynak ifadesi kalıplaşmış sözün temelinde yerinde duran, kaçmayan cesur kişiyi ve aslanı destekler; ölüm için söylenmesi yalnız tek kaynağın bildirdiği ayrı ve sınırlı bir kullanımdır.","lexical_glosses":[{"lexical_unit_id":"lu_043","rendering_kind":"ordinary","target_gloss":"yerinde duran, kaçmayan cesur kişi; aslan"},{"lexical_unit_id":"lu_044","rendering_kind":"ordinary","target_gloss":"ölüm için kullanılan kalıplaşmış niteleme"}],"lexicalization_note":"Tanım yalnız verilen kalıplaşmış söz ve onun ölümle kurulan özel yapısı içinde kalır; genel bir cesaret ya da ölüm anlamına genişletilmez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; genel kahramanlık ile yerinde durmaya bağlı özel cesaret sınırını gösteren üçü seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal doğrudan savaşçı davranışına bağlıdır; odak dal kalıplaşmış nitelemedir ve aslan ile ölüm yüzlerine uzanır.","focus_only":"Kalıplaşmış söz aslana ve sınırlı olarak ölüme de uygulanır.","gloss":"savaşta yerini bırakmayan cesur","neighbor_only":"Savaşın korkutamadığı ve karşısındaki rakibi bırakmayan savaşçıyı özellikle anlatır.","neighbor_ref":"root_001390/B004","relation_type":"near_synonym","shared_zone":"Tehlike karşısında korkmadan yerinde durma iki dalın çekirdeğidir."},{"boundary_match":"partial","distinction":"Komşu dal düşmana yapışma görüntüsünü, odak dal ise bulunduğu yeri terk etmeme ve kaçmama davranışını öne çıkarır.","focus_only":"Genel olarak yerini bırakmayan kişiyi ve aslanı niteler.","gloss":"düşmanına yapışan cesur","neighbor_only":"Düşmanına sıkıca yapışıp onun boğazında kalan savaşçıyı betimler.","neighbor_ref":"root_001424/B012","relation_type":"near_synonym","shared_zone":"Cesaret ve düşman karşısında sebat iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Komşu dal genel kahramanlığı, odak dal ise kaçmayıp yerinde durma davranışıyla tanımlanan özel nitelemeyi anlatır.","focus_only":"Yerinde durma ve kaçmama koşulunu, ayrıca aslan ve ölüm yüzlerini taşır.","gloss":"kahraman ve cesur kişi","neighbor_only":"Tehlikeye atılan kahramanı ve kahramanlık niteliğini daha genel biçimde kapsar.","neighbor_ref":"root_000127/B004","relation_type":"near_synonym","shared_zone":"Korku karşısında cesur davranan kişi ortak alandır."}],"source_phrase_ar":"رجل حبيل براح إذا كان شجاعا ويسمى به الأسد أيضا (jamhara)؛ يقال للواقف مكانه كالأسد لا يفر حبيل براح (sihah)؛ يقال للموت حبيل براح (tahdhib)؛ للواقف مكانه لا يفر حبيل براح كأنه محبول وزعم ناس أن الأسد يقال له حبيل براح (maqayis)","source_summary":"Toplu kanıt yerinde duran ve kaçmayan cesur kişi ile aslan kullanımını verir; ölüm için söylenen biçim de aynı aggregate iddia içinde yer alır.","sources":["JA","SI","TA","MQ"],"what_is_ar":"يدخل فيه حبيل براح للرجل الشجاع أو الواقف مكانه لا يفر وللأسد وما يذكر للموت بهذا اللفظ","what_is_not_ar":"لا يدخل فيه الداهية المسماة حبلا ولا الحبالة المصيدة"},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000291/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَبْل","morph_features":"STEM|POS:N|LEM:Habol|ROOT:Hbl|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:3:1","qac_word_ref":"111:5:3","surface_ar":"حَبْلٌ"}],"gloss":"yalıtık adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin yaradılış veya hoşgörü bakımından geniş ya da dar oluşu."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyin ağırlığı veya yük olma niteliği."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İçecek nedeniyle karnın şişmesi ve kişinin su ya da içkiyle doyması."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kişinin öfke, sıkıntı veya kederle dolması."}}],"root_ar":"ح ب ل","root_id":"root_000291","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"سعة وضيق وامتلاء داخلي","concept_gloss":"yalıtık adlandırmalar","contextual_glosses":[{"applicability":"Kişinin huy veya hoşgörü genişliği ve darlığı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişi niteliğini ve genişlik-darlık karşıtlığını korur."},"facet_ids":["F001"],"text":"geniş veya dar yaradılışlı","usage_role":"contextual"},{"applicability":"Kişinin öfke, su veya içki bakımından doluluğu anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Duygusal veya fiziksel doluluk ile dolan kişiyi korur."},"facet_ids":["F003","F004"],"text":"öfkeyle veya içecekle dolmuş","usage_role":"explanatory"}],"definition":"Bu dal tek bir kavram oluşturmaz: geniş veya dar yaradılış, ağırlık, içecekten karın şişmesi ve öfke ya da sıvıyla dolma anlamları aynı yerde toplanmıştır. Bu yüzler ayrılmadan ortak bir tanım kurulamaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin yaradılış veya hoşgörü bakımından geniş ya da dar oluşu."},{"facet_id":"F002","role":"source_variant","statement":"Bir şeyin ağırlığı veya yük olma niteliği."},{"facet_id":"F003","role":"source_variant","statement":"İçecek nedeniyle karnın şişmesi ve kişinin su ya da içkiyle doyması."},{"facet_id":"F004","role":"source_variant","statement":"Kişinin öfke, sıkıntı veya kederle dolması."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_045","rendering_kind":"ordinary","target_gloss":"geniş veya dar yaradılışlı"},{"lexical_unit_id":"lu_046","rendering_kind":"ordinary","target_gloss":"öfke, su veya içkiyle dolmuş"},{"lexical_unit_id":"lu_047","rendering_kind":"ordinary","target_gloss":"ağırlık"},{"lexical_unit_id":"lu_048","rendering_kind":"ordinary","target_gloss":"içecekten kaynaklanan karın şişliği"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"واسع الحبل وضيق الحبل كضيق الخلق وواسع الخلق ورجل حبلان إذا امتلأ غيظا ورجل حبلان من الماء والشراب إذا امتلأ ريا والحبل الثقل والحبال انتفاخ البطن من الشراب والنبيذ ورجل حبلان وامرأة حبلانة وفلان حبلان على فلان أي غضبان وبه حبل أي غضب وغم (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Huy, ağırlık, bedensel doluluk ve öfke anlamlarının tümü yalnız bu toplu tanıklıkta yer alır."}],"source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["TA"],"what_is_ar":"يدخل فيه واسع الحبل وضيق الحبل في الخلق والحبل بمعنى الثقل والحبال بمعنى انتفاخ البطن ورجل حبلان أو امرأة حبلانة من الغيظ أو الشراب أو الري","what_is_not_ar":"لا يدخل فيه حمل المرأة إلا من جهة قول المصدر إنه أصل التسمية ولا يدخل فيه الداهية"},"support_links":[]},{"boundary":"Bu dal yalnız verilen zaman kalıbıdır; tuzak adı veya gebelikle ilgili yapı buraya girmez.","branch_kind":"collocation","branch_ref":"root_000291/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَبْل","morph_features":"STEM|POS:N|LEM:Habol|ROOT:Hbl|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:3:1","qac_word_ref":"111:5:3","surface_ar":"حَبْلٌ"}],"gloss":"o sırada","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir olay veya durumla aynı zamana işaret eden kalıplaşmış zaman anlatımı."}}],"root_ar":"ح ب ل","root_id":"root_000291","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kaynakta verilen zaman kalıbının doğal Türkçe karşılığıdır.","boundary_detail":"Bu dal yalnız verilen zaman kalıbıdır; tuzak adı veya gebelikle ilgili yapı buraya girmez.","branch_image_ar":"حبالة حين ووقت","concept_gloss":"o sırada","contextual_glosses":[{"applicability":"Zaman çakışmasının özellikle vurgulandığı cümlede kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli zaman noktasını ve vurgulu eşzamanlılığı korur."},"facet_ids":["F001"],"text":"tam o vakit","usage_role":"contextual"}],"definition":"Yalnız belirli bir kalıp içinde, sözü edilen olayın gerçekleştiği sırayı, yani o vakti bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir olay veya durumla aynı zamana işaret eden kalıplaşmış zaman anlatımı."}],"identity_rationale":"Kaynak ifadesi tek bir kalıplaşmış yapıyı ve onun o sırada ya da o vakit anlamını doğrudan bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_050","rendering_kind":"ordinary","target_gloss":"o sırada, o vakit"}],"lexicalization_note":"Tanım yalnız kaynakta verilen kalıba bağlı zaman anlamını karşılar ve çıplak biçime genel zaman anlamı yüklemez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel zaman, yinelenen vakit ve sürmekte olan olay içindeki zamanla sınırı gösteren üçü seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel zaman söz varlığıdır; odak dal tek bir kalıbın o sırada anlamıyla sınırlıdır.","focus_only":"Yalnız belirli bir kalıp içinde o sırayı gösterir.","gloss":"zaman ve dönem","neighbor_only":"Genel zaman, süre, dönem ve yakın vakit anlamlarını geniş biçimde kapsar.","neighbor_ref":"root_000382/B001","relation_type":"near_synonym","shared_zone":"Belirli veya genel bir zamanı gösterme işlevi ortaktır."},{"boundary_match":"partial","distinction":"Komşu dal bağımsız ve genel zaman adıdır; odak dal yalnız belirli yapıda işaret edilen vakti bildirir.","focus_only":"Sözü edilen olayla aynı sıraya bağlı kalıplaşmış bir gösterimdir.","gloss":"vakit ve zamanlar","neighbor_only":"Genel vakti ve aralıklı ya da yinelenen zamanları adlandırır.","neighbor_ref":"root_000068/B003","relation_type":"near_synonym","shared_zone":"Vakit bildirme iki dalın ortak çekirdeğidir."},{"boundary_match":"partial","distinction":"Komşu dal sürmekte olan durum içindeki zamanı, odak dal ise işaret edilen o vakti bildirir.","focus_only":"İşaret edilen tek vakti bildirir.","gloss":"bir olay sürerken","neighbor_only":"Bir eylem ya da durum sürerken gerçekleşen başka bir olayı zaman cümlesiyle bağlar.","neighbor_ref":"root_000170/B010","relation_type":"near_synonym","shared_zone":"Bir olayı başka bir zamansal duruma bağlama işlevi ortaktır."}],"source_phrase_ar":"أتيته على حبالة ذاك أي على حين ذاك (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu zaman anlamı yalnız söz konusu kalıplaşmış kullanım için tanıklanmıştır."}],"source_summary":"Tek tanıklık, kalıplaşmış yapının sözü edilen olayın gerçekleştiği sırayı bildirdiğini açıkça belirtir.","sources":["TA"],"what_is_ar":"يدخل فيه قولهم على حبالة ذاك بمعنى على حين ذاك","what_is_not_ar":"لا يدخل فيه الحبالة المصيدة ولا حبل الحبلة في الحمل"},"support_links":[]},{"boundary":"Yazılı kayıt yorumu ile gebelik zamanı veya yeri yorumu eşitlenemez; yazının yazıldığı genel yer anlamı çıkarılamaz.","branch_kind":"bare","branch_ref":"root_000291/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَبْل","morph_features":"STEM|POS:N|LEM:Habol|ROOT:Hbl|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:3:1","qac_word_ref":"111:5:3","surface_ar":"حَبْلٌ"}],"gloss":"yazılı kayıt; başka yoruma göre gebelik başlangıcı","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcüğün yazılı kayıt veya yazgının yazıldığı kayıt olarak okunması."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sözün, ölümün anne gebe kaldığında yazılmış olmasını anlattığı yorumu."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Biçimin gebeliğin yeri veya başlangıcıyla ilişkilendirilmesi."}}],"root_ar":"ح ب ل","root_id":"root_000291","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynak ayrılığını tek bir kesin anlama dönüştürmeden iki ana okumayı gösterir.","boundary_detail":"Yazılı kayıt yorumu ile gebelik zamanı veya yeri yorumu eşitlenemez; yazının yazıldığı genel yer anlamı çıkarılamaz.","branch_image_ar":"محبل كتاب أو كتابة","concept_gloss":"yazılı kayıt; başka yoruma göre gebelik başlangıcı","contextual_glosses":[{"applicability":"Sözcüğün yazılı kayıt olarak okunduğu yoruma bağlı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yazılı kayıt niteliğini ve yazgıyla ilişkisini korur."},"facet_ids":["F001"],"text":"yazgının yazılı kaydı","usage_role":"contextual"},{"applicability":"Sözün gebelik anına bağlanan yorumunu açıkça vermek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölüm yazgısını, yazma olayını ve gebelik zamanını korur."},"facet_ids":["F002","F003"],"text":"anne gebe kaldığında yazılan ölüm yazgısı","usage_role":"explanatory"}],"definition":"Tartışmalı bir şiir sözünde, bir okumaya göre yazılı kayıt veya yazgının kaydıdır; başka yoruma göre söz, ölümün anne gebe kaldığında yazılmasına ve gebeliğin yer ya da başlangıcına gönderme yapar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcüğün yazılı kayıt veya yazgının yazıldığı kayıt olarak okunması."},{"facet_id":"F002","role":"source_variant","statement":"Sözün, ölümün anne gebe kaldığında yazılmış olmasını anlattığı yorumu."},{"facet_id":"F003","role":"source_variant","statement":"Biçimin gebeliğin yeri veya başlangıcıyla ilişkilendirilmesi."}],"identity_rationale":"Kaynak ifadesi tek ve güvenli bir 'kitap veya yazı yeri' anlamı kurmaz: bir yorum biçimi sözcüğü yazılı kayıt sayarken başka yorum, ölümün anne gebe kaldığında yazılmış olmasını ve gebeliğin yerini anlatır. Dal bu yorum ayrılığı olarak yeniden çerçevelenmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_051","rendering_kind":"ordinary","target_gloss":"yazılı kayıt; başka yoruma göre gebeliğin yeri veya başlangıcı"}],"lexicalization_note":"Çıplak biçim kaynaklar arasındaki okuma ayrılığıyla tanımlanır; ona genel kitap, yazı yeri veya gebelik anlamı zorla yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yorum ayrılığı nedeniyle yalnız gebelik yüzü ve yazgının sonucu ile kurulan iki sınırlı ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal doğrudan gebelik kavramıdır; odak dal ise yalnız tartışmalı yorumun bir yüzünde gebelikle ilişkilidir.","focus_only":"Tartışmalı şiir sözünde yazılı kayıt okumasını da taşır.","gloss":"gebelik ve karındaki yavru","neighbor_only":"Gebelik durumunu, gebe dişiyi, yavruyu ve sonraki kuşağı doğrudan adlandırır.","neighbor_ref":"root_000291/B006","relation_type":"near_neighbor","shared_zone":"Gebeliğin başlangıç zamanı veya yeri yorumunda iki dal temas eder."},{"boundary_match":"thematic_only","distinction":"Odak dal tartışmalı bir kayıt ya da gebelik anı yorumudur; komşu dal ise dönüş ve sonuçlanma sürecini doğrudan anlatır.","focus_only":"Yazılı kayıt ile gebelik anında yazılmış ölüm yazgısı arasında yorum ayrılığı taşır.","gloss":"sonuç ve son varış","neighbor_only":"Bir şeyin sonucuna dönmesini, son varışını ve sözün anlamına götürülmesini anlatır.","neighbor_ref":"root_000067/B002","relation_type":"thematic","shared_zone":"Ölüm yazgısı ve varılan son düşüncesi aynı sonuç senaryosunda buluşur."}],"source_phrase_ar":"المحبل الكتاب فمن كسر الباء عنى به الكتاب ومن لم يكسر الباء فإنه يريد وأمه حبلى (jamhara)؛ خط له ذلك في المحبل أي كتب له الموت حين حبلت به أمه والمحبل موضع الحبل (tahdhib)","source_summary":"Toplu kanıt iki yorumu karşı karşıya getirir: yazılı kayıt okuması ile ölüm yazgısını annenin gebe kaldığı ana ve gebeliğin yerine bağlayan okuma.","sources":["JA","TA"],"what_is_ar":"يدخل فيه المحبل إذا أريد به الكتاب أو موضع الكتابة في الشاهد المختلف فيه","what_is_not_ar":"لا يدخل فيه المحبل بمعنى الحبل ولا محبل الحمل إذا أريد به وقت الحبل"},"support_links":[]},{"boundary":"Dalın ad anlamı ile yalnızca belirli yapılarda görülen bükme eylemi birbirine karıştırılmamalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001422/B001","candidate_links":[{"candidate_id":"cand_95babfbcc004a565e904","lane":"micro"},{"candidate_id":"cand_2fdced5c1589ea1bdfdc","lane":"micro"},{"candidate_id":"cand_ac8d8659ce8481fc5aac","lane":"micro"},{"candidate_id":"cand_0807c6428416b020e630","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَّسَد","morph_features":"STEM|POS:N|LEM:m~asad|ROOT:msd|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:5:1","qac_word_ref":"111:5:5","surface_ar":"مَّسَدٍۭ"}],"gloss":"bükülü lif veya ip; ipi ustaca bükme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hurma lifi veya yaprağından, deve tüyünden ya da derisinden yapılmış lif veya ipi belirtir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İpi ustalıkla, sağlam ve düzgün biçimde bükme eylemini belirtir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bir yapıda, bükülü lifsi malzemeden yapılmış ipi anlatır."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Niteleme yapısında, bükümü özenle ve sağlam yapılmış ipi anlatır."}}],"root_ar":"م س د","root_id":"root_001422","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın malzeme ve ürün anlamı ile yapıya bağlı bükme eyleminin birlikte temsil edilmesi gerektiğinde kullanılır.","boundary_detail":"Dalın ad anlamı ile yalnızca belirli yapılarda görülen bükme eylemi birbirine karıştırılmamalıdır.","branch_image_ar":"الحبل المفتول","concept_gloss":"bükülü lif veya ip; ipi ustaca bükme","contextual_glosses":[{"applicability":"Söz konusu olan malzeme ya da bu malzemeden yapılmış ipin kendisi olduğunda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İpi ustaca bükme eylemini dışarıda bırakır.","preserves":"Bükülü malzemeyi ve ondan yapılan ipi korur."},"facet_ids":["F001","F003"],"text":"liften veya deriden yapılmış bükülü ip","usage_role":"contextual"},{"applicability":"Bir ipin bükülme işlemi ve bu işlemin özenli oluşu anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Lif veya ip adı olan bağımsız ürün anlamını dışarıda bırakır.","preserves":"Bükme eylemini ve bükümün iyi yapılmasını korur."},"facet_ids":["F002","F004"],"text":"ipi sağlam ve düzgün bükmek","usage_role":"contextual"}],"definition":"Hurma lifi veya yaprağından, deve tüyünden ya da derisinden elde edilen bükülü lif veya iptir; ayrıca ipi sağlam ve düzgün biçimde bükme eylemini ve bu eylemin iyi bükülmüş ürününü kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hurma lifi veya yaprağından, deve tüyünden ya da derisinden yapılmış lif veya ipi belirtir."},{"facet_id":"F002","role":"core","statement":"İpi ustalıkla, sağlam ve düzgün biçimde bükme eylemini belirtir."},{"facet_id":"F003","role":"specialization","statement":"Belirli bir yapıda, bükülü lifsi malzemeden yapılmış ipi anlatır."},{"facet_id":"F004","role":"specialization","statement":"Niteleme yapısında, bükümü özenle ve sağlam yapılmış ipi anlatır."}],"identity_rationale":"Kaynak ifadesi hem hurma lifi, hurma yaprağı, deve tüyü veya derisinden yapılan bükülü lif ve ipi hem de ipi ustaca bükme eylemini içerir. Bu nedenle dal yalnızca bir ip adı olarak değil, malzeme, ürün ve yapım eylemini ayıran karma bir alan olarak ele alınmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"hurma lifi veya yaprağından, deve tüyünden ya da derisinden yapılmış lif veya ip"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ipi sağlam ve düzgün biçimde bükmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bükülü lifsi malzemeden yapılmış ip"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"iyi bükülmüş ip"}],"lexicalization_note":"Tanım, bağımsız lif veya ip anlamını korurken ipi bükme eylemini ve nitelikli ip yapılarını ayrı, yapıya bağlı yüzler olarak gösterir.","neighbor_coverage_note":"Verilen komşuların tümü karşılaştırıldı; yayımlanan üç ilişki, bükülü ip, sıkı büküm ve bedene aktarılan ip benzetmesi sınırlarını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli lif ve deri kaynaklı ürünleri de adlandırır; komşu ise malzeme listesinden çok sıkı büküm ve bükülü ip parçaları çevresinde genişler.","focus_only":"Odak dal, ipin yapılabileceği hurma lifi, yaprak, deve tüyü ve deri gibi malzemeleri ve ustaca bükme eylemini birlikte kapsar.","gloss":"ipi sıkı bükme","neighbor_only":"Komşu dal, güçlü veya sıkı bükümü ve ipin bükülü kollarını daha geniş bir sözcük ailesi içinde öne çıkarır.","neighbor_ref":"root_001414/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da ipin bükülmesi ve bükümün sağlamlığı alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği malzeme ile bükme işlemini birlikte taşır; komşunun çekirdeği ise bağlama işlevli şerit veya ip nesnesidir.","focus_only":"Odak dal malzeme türlerini ve ipi iyi bükme işlemini anlamın içine alır.","gloss":"bükülü şerit veya bağ","neighbor_only":"Komşu dal, hayvan bağlamakta kullanılan şerit veya bükülü ip gibi belirli kullanım nesnelerini kapsar.","neighbor_ref":"root_000788/B004","relation_type":"near_neighbor","shared_zone":"İki dal da lifli malzemeden yapılmış bükülü ip ya da şerit nesnesine yaklaşır."},{"boundary_match":"partial","distinction":"Biri somut ip ve bükme alanıdır; diğeri bu biçimi insan bedenine aktaran bir nitelemedir ve ipin kendisini adlandırmaz.","focus_only":"Odak dal gerçek lif, ip ve bunların bükülmesiyle ilgilidir.","gloss":"ip gibi sıkı yapılı beden","neighbor_only":"Komşu dal insan bedeninin ip gibi sıkı, ince ve düzgün kuruluşunu anlatır.","neighbor_ref":"root_001422/B002","relation_type":"near_neighbor","shared_zone":"Komşu bedensel niteleme, odak daldaki bükülü ve sıkı ip görünümünden yararlanır."}],"source_phrase_ar":"أصل صحيح يدل على جدل شيء وطية (maqayis)؛ المسد ليف يتخذ من جريد النخل (maqayis;ayn;mufradat)؛ المسد حبل يتخذ من أوبار الإبل (maqayis;tahdhib)؛ حبل من ليف أو خوص وقد يكون من جلود الإبل أو من أوبارها (sihah;tahdhib)؛ مسدت الحبل أي أجدت فتله (sihah;tahdhib)","source_summary":"Kaynakların ortak çizgisi bükme ve katlama işlemini, çeşitli lif ve deri türlerinden yapılan ipi ve ip bükümünün iyi yapılmasını aynı anlam alanında birleştirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"اللّيف والحبل من النخل أو الخوص أو وبر الإبل أو جلودها، وما أُجيد فتله وليّه","what_is_not_ar":"ليس النحي ولا المحور ولا إدآب السير بالليل ولا قوام الشعر"},"support_links":["sup_0c0f822a5ee347126fb0","sup_500faf58bc2cb81867aa","sup_57e3c6af36af0c4bffed","sup_619d8105a0e1cc83eb79"]},{"boundary":"Bu dal ipin kendisini değil, ip benzetmesiyle anlatılan beden yapısını ve ona bağlı sıkılaştırma eylemini kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001422/B002","candidate_links":[{"candidate_id":"cand_b52007d35c7c96d74abe","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَّسَد","morph_features":"STEM|POS:N|LEM:m~asad|ROOT:msd|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:5:1","qac_word_ref":"111:5:5","surface_ar":"مَّسَدٍۭ"}],"gloss":"ip gibi sıkı ve düzgün beden; eti sıkılaştırma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan bedenini bükülmüş ip gibi sıkı ve birbirine geçmiş bir yapıda gösterir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bedenin ince, toplu, düzgün ve güzel kuruluşunu öne çıkarır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bir eylem yapısında üst et bölümünü sıkılaştırıp güçlendirmeyi anlatır."}}],"root_ar":"م س د","root_id":"root_001422","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Beden niteliği ile ona bağlı sıkılaştırma eyleminin dal düzeyinde birlikte gösterilmesi gerektiğinde kullanılır.","boundary_detail":"Bu dal ipin kendisini değil, ip benzetmesiyle anlatılan beden yapısını ve ona bağlı sıkılaştırma eylemini kapsar.","branch_image_ar":"الجسم الممسود","concept_gloss":"ip gibi sıkı ve düzgün beden; eti sıkılaştırma","contextual_glosses":[{"applicability":"Bir insanın beden kuruluşu sıkılık, incelik ve düzgünlük bakımından nitelendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Üst et bölümünü sıkılaştırma eylemini dışarıda bırakır.","preserves":"Bedenin sıkı, ince ve düzgün kuruluşunu korur."},"facet_ids":["F001","F002"],"text":"ip gibi sıkı ve ince yapılı","usage_role":"contextual"},{"applicability":"Eylem doğrudan bedenin üst et bölümünün sıkılaştırılması ve güçlendirilmesi olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan bedeninin ip gibi ince ve düzgün kuruluşunu dışarıda bırakır.","preserves":"Sıkılaştırma ve güçlendirme eylemini korur."},"facet_ids":["F003"],"text":"üst etini sıkılaştırıp güçlendirmek","usage_role":"contextual"}],"definition":"İnsan bedeninin bükülmüş ip gibi sıkı, toplu, ince ve düzgün yapılı olmasıdır; buna bağlı kullanımda üst et bölümünü sıkılaştırıp güçlendirmeyi de anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan bedenini bükülmüş ip gibi sıkı ve birbirine geçmiş bir yapıda gösterir."},{"facet_id":"F002","role":"specialization","statement":"Bedenin ince, toplu, düzgün ve güzel kuruluşunu öne çıkarır."},{"facet_id":"F003","role":"associated_use","statement":"Belirli bir eylem yapısında üst et bölümünü sıkılaştırıp güçlendirmeyi anlatır."}],"identity_rationale":"Kaynak ifadesinin çekirdeği, insan bedeninin bükülü ip gibi sıkı kurulmuş, ince ve düzgün görünmesidir. Aynı ifade üst et bölümünü sıkılaştırma eylemini de verdiğinden, beden niteliği korunmalı fakat bu eylem ona bağlı ayrı bir yüz olarak gösterilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"ip gibi sıkı, ince ve düzgün yapılı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"beden yapısı güzel ve sıkı"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"üst etini sıkılaştırıp güçlendirmek"}],"lexicalization_note":"Tanım, insan bedenine ait nitelemeyi çekirdekte tutar; güzel yapı ve eti sıkılaştırma anlamlarını yalnızca kendi söz dizimsel yapıları içinde ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen üç komşu sıkı beden kuruluşunu uzuv inceliği, ölçülü yapı ve gerçek ip alanından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sıkılığı ip benzetmesiyle kurar ve bir sıkılaştırma eylemine uzanır; komşu ise uzuvların inceliği ve düzgünlüğünü merkeze alır.","focus_only":"Odak dal, bedenin bükülü ip gibi sıkı ve toplu oluşunu ve eti sıkılaştırma eylemini içerir.","gloss":"ince ve düzgün yapılı beden","neighbor_only":"Komşu dal, özellikle uzuvların ince, narin ve düzgün kuruluşuna yönelir.","neighbor_ref":"root_000229/B006","relation_type":"near_synonym","shared_zone":"İki dal da insan bedeninin ince, düzgün ve iyi kurulmuş görünüşünü niteleyebilir."},{"boundary_match":"partial","distinction":"Odak dal sıkı ve ince dokuyu, komşu ise boyu, oranı ve beden bölümlerinin dengeli biçimini temel alır.","focus_only":"Odak dalın ayırıcı yanı ip gibi bükülü, sıkı ve toplu beden kuruluşudur.","gloss":"düzgün ve ölçülü beden yapısı","neighbor_only":"Komşu dal boy, diklik, ölçülü oran ve beden bölümlerinin güzel dağılımını öne çıkarır.","neighbor_ref":"root_001204/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da bedenin düzgün ve beğenilen kuruluşunu anlatır."},{"boundary_match":"partial","distinction":"Odak dal benzetmenin bedensel sonucunu anlatır; komşu ise benzetmeye kaynak olan somut ipi ve yapım işlemini anlatır.","focus_only":"Odak dal insan bedenine ait bir niteleme ve sıkılaştırma eylemidir.","gloss":"bükülü lif veya ip","neighbor_only":"Komşu dal gerçek lif, ip ve ipin ustaca bükülmesini adlandırır.","neighbor_ref":"root_001422/B001","relation_type":"near_neighbor","shared_zone":"Bedenin sıkı kuruluşu, komşu daldaki bükülmüş ipin biçimine benzetilir."}],"source_phrase_ar":"امرأة ممسودة مجدولة الخلق كالحبل الممسود (maqayis;mufradat)؛ جارية ممسودة مطوية ممشوقة (ayn;tahdhib)؛ رجل ممسود أي مجدول الخلق (sihah;tahdhib)؛ يمسد أعلى لحمه ويأرمه أي يشده (sihah;tahdhib)","source_summary":"Kaynaklar, kadın veya erkek bedenini bükülü ip gibi sıkı, ince ve düzgün kuruluşlu gösteren nitelemede birleşir; aynı alan üst et bölümünü sıkılaştırma eylemine de uzanır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الممسود من الإنسان أو الجارية، أي المجدول أو المطوي أو الممشوق الخلق كالحبل","what_is_not_ar":"ليس الحبل نفسه ولا النحي ولا المحور ولا السير بالليل"},"support_links":["sup_908f195f4a0af0b20175"]},{"boundary":"Gece koşulu ile aralıksız çaba birlikte korunmalı; anlam yalnızca yolculuk veya yalnızca güçlük diye genişletilmemelidir.","branch_kind":"bare","branch_ref":"root_001422/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّسَد","morph_features":"STEM|POS:N|LEM:m~asad|ROOT:msd|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:5:1","qac_word_ref":"111:5:5","surface_ar":"مَّسَدٍۭ"}],"gloss":"gece boyunca durmadan ve güçlüğe göğüs gererek yol alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yolculuğu gece boyunca ısrarla ve kesintisiz sürdürmeyi anlatır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gecenin yolculuk sırasında getirdiği güçlük ve yorgunluğa katlanmayı içerir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sürekli yol çabasının bedeni sıkılaştırıp zayıflatmasıyla açıklanan bir bağlantı taşır."}}],"root_ar":"م س د","root_id":"root_001422","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gece koşulu, yolculuğun sürekliliği ve güçlüğe dayanma birlikte söz konusu olduğunda dalın tam karşılığıdır.","boundary_detail":"Gece koşulu ile aralıksız çaba birlikte korunmalı; anlam yalnızca yolculuk veya yalnızca güçlük diye genişletilmemelidir.","branch_image_ar":"إدآب السير في الليل","concept_gloss":"gece boyunca durmadan ve güçlüğe göğüs gererek yol alma","contextual_glosses":[{"applicability":"Akıcı anlatımda gece boyunca süren ısrarlı yolculuk vurgulanmak istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geceyi, sürekliliği ve zorluğa rağmen yol almayı korur."},"facet_ids":["F001","F002"],"text":"gece boyu yılmadan yol almak","usage_role":"contextual"}],"definition":"Gece boyunca yolculuğu durmadan ve güçlüğüne katlanarak sürdürmedir; sürekli çabanın bedeni sıkılaştırıp zayıflatması bu eyleme bağlı bir açıklamadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yolculuğu gece boyunca ısrarla ve kesintisiz sürdürmeyi anlatır."},{"facet_id":"F002","role":"core","statement":"Gecenin yolculuk sırasında getirdiği güçlük ve yorgunluğa katlanmayı içerir."},{"facet_id":"F003","role":"associated_use","statement":"Sürekli yol çabasının bedeni sıkılaştırıp zayıflatmasıyla açıklanan bir bağlantı taşır."}],"identity_rationale":"Kaynak ifadesi gece yolculuğunu sıradan gece hareketi olarak değil, gece boyunca ısrarla sürdürme ve güçlüğüne katlanma olarak tanımlar. Sürekli çabanın bedeni sıkılaştırıp zayıflatmasına ilişkin açıklama anlamın kökenlendirilmiş çağrışımıdır, çekirdek eylemin yerine geçmez.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"gece boyunca durmadan ve güçlüğe katlanarak yol alma"}],"lexicalization_note":"Tanım bağımsız dalı gece boyunca ısrarlı ve zorlu yol alma olarak sınırlar; komşu yapıların daha genel yolculuk anlamlarını içeri almaz.","neighbor_coverage_note":"Tüm komşu adaylar incelendi; seçilenler çekirdeği genel gece yolculuğu, uzun süreli az dinlenme ve zamandan bağımsız kesintisiz ilerlemeden ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu genel gece yolculuğunu karşılayabilir; odak dal ise bunun aralıksız, yorucu ve dayanma gerektiren biçimine ayrılmıştır.","focus_only":"Odak dal gece boyunca ısrarı, yorgunluğu ve güçlüğe katlanmayı zorunlu kılar.","gloss":"gece yolculuğu","neighbor_only":"Komşu dal gece yolculuğunu daha genel biçimde, insan topluluğu veya gece ilerleyen bulut gibi öznelerle de anlatabilir.","neighbor_ref":"root_000702/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak alanı gece vakti yer değiştirme ve yolculuktur."},{"boundary_match":"partial","distinction":"Odak dal güçlüğe katlanma yönünü çekirdeğe alır; komşu ise zaman süresi ve dinlenmenin azlığı bakımından daha geniştir.","focus_only":"Odak dal gecenin güçlüğüyle mücadeleyi ve bedeni yoran ısrarlı çabayı öne çıkarır.","gloss":"gece boyu az dinlenerek yol alma","neighbor_only":"Komşu dal gece boyu yol alma yanında gece ve gündüz az dinlenerek ilerleme kapsamına uzanır.","neighbor_ref":"root_001601/B005","relation_type":"near_synonym","shared_zone":"İki dal da gece boyunca uzun ve az kesintili yolculuğu anlatır."},{"boundary_match":"partial","distinction":"Odak dal mutlaka geceyi ve güçlüğe dayanmayı içerir; komşunun ayırıcı yönü yalnızca temponun kesilmemesidir.","focus_only":"Odak dalın gece koşulu ve gecenin güçlüğüne katlanma yönü vardır.","gloss":"duraksamadan yol alma","neighbor_only":"Komşu dal duraksamayan yolculuğu günün belirli bir bölümüne bağlamaz.","neighbor_ref":"root_000838/B010","relation_type":"near_synonym","shared_zone":"Her iki dal da gevşeme ve duraklama olmadan sürdürülen yolculuğu belirtir."}],"source_phrase_ar":"المسد إدآب السير في الليل (ayn;sihah;tahdhib)؛ يكابد الليل عليها مسدا (ayn;tahdhib)؛ جعل الليث الدأب مسدا لأنه يمسد خلق من يدأب فيطويه ويضمره (tahdhib)","source_summary":"Kaynaklar gece yolculuğunu sürekli çaba ve gecenin güçlüğüne dayanma yönleriyle verir; bedensel sıkılaşma ve zayıflama açıklaması bu çekirdeğe bağlı bir gerekçelendirmedir.","sources":["AY","SI","TA"],"what_is_ar":"إدآب السير في الليل ومكابدة الليل في السير","what_is_not_ar":"ليس الحبل ولا الليف ولا النحي ولا المحور"},"support_links":[]},{"boundary":"Anlam deri tulum niteliği ile yağ veya bal saklama işlevine bağlıdır; her türlü kap için kullanılamaz.","branch_kind":"bare","branch_ref":"root_001422/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّسَد","morph_features":"STEM|POS:N|LEM:m~asad|ROOT:msd|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:5:1","qac_word_ref":"111:5:5","surface_ar":"مَّسَدٍۭ"}],"gloss":"yağ veya bal tulumu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Deri tulum veya deri kap türünde bir saklama nesnesidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İçine özellikle yağ veya bal konmasıyla işlevsel olarak sınırlandırılır."}}],"root_ar":"م س د","root_id":"root_001422","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Deri bir kabın özellikle yağ ya da bal saklama amacıyla kullanıldığı bağlamlarda tam çekirdeği karşılar.","boundary_detail":"Anlam deri tulum niteliği ile yağ veya bal saklama işlevine bağlıdır; her türlü kap için kullanılamaz.","branch_image_ar":"المِساد نحي السمن والعسل","concept_gloss":"yağ veya bal tulumu","contextual_glosses":[{"applicability":"Nesnenin malzemesi ve içine konan ürünün açıkça belirtilmesi gereken açıklayıcı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kabın deriden oluşunu ve yağ ya da bala ayrılmasını korur."},"facet_ids":["F001","F002"],"text":"yağ ya da bal konan deri tulum","usage_role":"explanatory"}],"definition":"Yağ veya bal koyup saklamak için kullanılan deri tulum ya da deri kaptır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Deri tulum veya deri kap türünde bir saklama nesnesidir."},{"facet_id":"F002","role":"specialization","statement":"İçine özellikle yağ veya bal konmasıyla işlevsel olarak sınırlandırılır."}],"identity_rationale":"Kaynak ifadesi nesneyi yağ veya bal koymak için kullanılan deri bir tulum ya da kap olarak açıkça sınırlar. Yağ ile bal seçenekleri kabın işlevsel kapsamıdır ve kabı genel bir saklama kabına dönüştürmez.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yağ veya bal konan deri tulum"}],"lexicalization_note":"Tanım bağımsız kap adını deri tulum ve yağ ya da bal içeriğiyle sınırlar; komşu kap türlerini dalın içine katmaz.","neighbor_coverage_note":"Bütün komşular değerlendirildi; seçilen üçü deri kap ortaklığını korurken içerik, boyut ve taşıma işlevi bakımından en yararlı sınırları verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Kap türleri yakın olsa da odak dalın içeriği yağ veya bal, komşunun içeriği su veya süttür; bu kullanım sınırları birbirinin yerine geçmez.","focus_only":"Odak dal deri tulumu özellikle yağ veya bal saklama işleviyle sınırlar.","gloss":"küçük deri su veya süt kabı","neighbor_only":"Komşu dal küçük deri kabı su veya süt taşımaya ayırır ve kabın yapımını da kapsayabilir.","neighbor_ref":"root_000814/B004","relation_type":"near_synonym","shared_zone":"İki dal da sıvı veya yarı sıvı ürünler için kullanılan küçük deri kapları belirtir."},{"boundary_match":"partial","distinction":"Odak dal içerik ve işlev bakımından dardır; komşu ise birleştirilme biçimi ve su ya da yük taşıma kullanımlarıyla ayrılır.","focus_only":"Odak dal yağ veya bala ayrılmış deri tulumu adlandırır.","gloss":"birleştirilmiş su veya taşıma kabı","neighbor_only":"Komşu dal su kabı, yük düzeneği veya parçaları birleştirilmiş ve eskimiş taşıma nesnesi gibi daha geniş kullanımlara sahiptir.","neighbor_ref":"root_000797/B007","relation_type":"near_neighbor","shared_zone":"Her iki dal deri ya da benzeri esnek malzemeden yapılmış bir taşıma kabına yaklaşabilir."},{"boundary_match":"partial","distinction":"Odak dal tek bir işlevsel kap türüdür; komşu dal farklı biçim ve içeriklerdeki taşıma kaplarını bir araya getiren daha geniş bir alandır.","focus_only":"Odak dal yalnızca yağ veya bal için ayrılmış deri tulumu belirtir.","gloss":"su veya eşya taşıyan deri kap","neighbor_only":"Komşu dal su, eşya veya giysi taşıyan kova, torba ve sofra örtüsü gibi çeşitli kap biçimlerini içerir.","neighbor_ref":"root_000872/B002","relation_type":"near_neighbor","shared_zone":"İki dalın kesişimi deriden yapılmış taşıma ve saklama kabıdır."}],"source_phrase_ar":"المساد نحي السمن أو العسل (ayn)؛ المساد لغة في المساب وهو نحي السمن وسقاء العسل (sihah)؛ المساد نحي يجعل فيه سمن وعسل (tahdhib)","source_summary":"Kaynaklar nesneyi yağ veya bal konan deri tulum ya da deri kap olarak ortak biçimde tanımlar.","sources":["AY","SI","TA"],"what_is_ar":"المِساد، وهو نحي أو سقاء يجعل فيه السمن أو العسل","what_is_not_ar":"ليس الحبل ولا الفتل ولا إدآب السير ولا المحور"},"support_links":[]},{"boundary":"Nesnenin eksen işlevi ve demir malzemesi birlikte korunmalıdır.","branch_kind":"bare","branch_ref":"root_001422/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّسَد","morph_features":"STEM|POS:N|LEM:m~asad|ROOT:msd|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:5:1","qac_word_ref":"111:5:5","surface_ar":"مَّسَدٍۭ"}],"gloss":"demir mil","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir parçanın çevresinde döndüğü merkez mili veya eksenidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Milin veya eksenin demirden yapılmış olması anlamın zorunlu sınırıdır."}}],"root_ar":"م س د","root_id":"root_001422","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir dönme düzenindeki mil veya eksenin demirden yapıldığı açık olduğunda kullanılır.","boundary_detail":"Nesnenin eksen işlevi ve demir malzemesi birlikte korunmalıdır.","branch_image_ar":"محور الحديد","concept_gloss":"demir mil","contextual_glosses":[{"applicability":"Nesnenin hem dönme düzenindeki görevi hem de malzemesi açıklanmak istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dönme ekseni görevini ve demir oluşunu eksiksiz korur."},"facet_ids":["F001","F002"],"text":"demirden yapılmış dönme ekseni","usage_role":"explanatory"}],"definition":"Dönen bir parçanın merkezinde bulunan, demirden yapılmış mil veya eksendir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir parçanın çevresinde döndüğü merkez mili veya eksenidir."},{"facet_id":"F002","role":"specialization","statement":"Milin veya eksenin demirden yapılmış olması anlamın zorunlu sınırıdır."}],"identity_rationale":"Kaynak ifadesi anlamı demirden yapılmış bir dönme mili veya eksenle açıkça sınırlar. Dal ne genel olarak demiri ne de her malzemeden yapılmış her türlü çubuk ve desteği kapsar.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"demirden yapılmış mil veya eksen"}],"lexicalization_note":"Tanım bağımsız nesne adını demirden yapılmış mil veya eksenle sınırlar; genel araç ve metal anlamlarını içeri almaz.","neighbor_coverage_note":"Tüm komşular karşılaştırıldı; seçilenler demir ekseni daha geniş döndürme araçlarından, dönme eyleminden ve genel demir alanından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ortak nesnede anlamlar yaklaşır; ancak komşu dal farklı döndürme araçlarına uzanırken odak dal demir eksenle sınırlı kalır.","focus_only":"Odak dal yalnızca demirden yapılmış mil veya ekseni adlandırır.","gloss":"döndürme araçları ve demir eksen","neighbor_only":"Komşu dal değirmen kolu, döndürme çubuğu ve dizgin içindeki döner metal parça gibi çeşitli yönetme araçlarını da kapsar.","neighbor_ref":"root_000610/B006","relation_type":"near_synonym","shared_zone":"Her iki dal demirden yapılmış bir dönme milini veya eksenini karşılayabilir."},{"boundary_match":"partial","distinction":"Odak dal belirli malzemeden yapılmış parçanın adıdır; komşu dal dönme ilişkisini ve eylemini daha geniş biçimde anlatır.","focus_only":"Odak dal eksenin demirden yapılmasını zorunlu kılar.","gloss":"eksen çevresinde dönme","neighbor_only":"Komşu dal eksen çevresinde dönme eylemini ve başka bir nesneyi döndürerek biçimlendirmeyi de kapsar.","neighbor_ref":"root_000369/B007","relation_type":"near_neighbor","shared_zone":"İki dal da bir mil veya eksen çevresindeki dönme düzenine bağlıdır."},{"boundary_match":"field_only","distinction":"Malzeme ortaklığı dışında çekirdekler farklıdır: odak mekanik eksen işlevine, komşu ise demirin kendisine ve genel özelliklerine dayanır.","focus_only":"Odak dal demirden yapılmış belirli bir mekanik parçayı, mili veya ekseni adlandırır.","gloss":"demir ve demir nesneler","neighbor_only":"Komşu dal demir madenini, demir nesneleri, demir işçisini ve sertlik özelliklerini genişçe kapsar.","neighbor_ref":"root_000002/B004","relation_type":"same_field","shared_zone":"İki dal demir malzeme alanında buluşur."}],"source_phrase_ar":"المسد المحور إذا كان من حديد (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Dalın tek tanıklığı, dönme ekseni işlevindeki nesnenin demirden yapılmış olmasını açıkça şart koşar."}],"source_summary":"Verilen tanıklık, nesneyi demirden yapılmış mil veya eksen olarak sınırlar ve başka bir kullanım belirtmez.","sources":["AY"],"what_is_ar":"المسد بمعنى المحور إذا كان من حديد","what_is_not_ar":"ليس الحبل ولا النحي ولا إدآب السير ولا الممسود من الخلق"},"support_links":[]},{"boundary":"Siyah renk ile ince deri nesnesi korunmalı; yazılı belge veya genel hayvan derisi anlamı eklenmemelidir.","branch_kind":"bare","branch_ref":"root_001422/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّسَد","morph_features":"STEM|POS:N|LEM:m~asad|ROOT:msd|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:5:1","qac_word_ref":"111:5:5","surface_ar":"مَّسَدٍۭ"}],"gloss":"siyah ince deri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnce deri yaprağı veya deri parçası türünde bir nesnedir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Derinin siyah renkli olması anlamın belirtilen ayırıcı özelliğidir."}}],"root_ar":"م س د","root_id":"root_001422","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesne ince bir deri parçası olduğunda ve siyah rengi anlamın ayırıcı parçası olarak korunduğunda kullanılır.","boundary_detail":"Siyah renk ile ince deri nesnesi korunmalı; yazılı belge veya genel hayvan derisi anlamı eklenmemelidir.","branch_image_ar":"المِساد الرق الأسود","concept_gloss":"siyah ince deri","contextual_glosses":[{"applicability":"Nesnenin türü ve rengi açık bir açıklamayla verilmek istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Deri türünü, inceliği ve siyah rengi eksiksiz korur."},"facet_ids":["F001","F002"],"text":"siyah renkli ince deri parçası","usage_role":"explanatory"}],"definition":"Siyah renkli, ince bir deri yaprağı veya deri parçasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnce deri yaprağı veya deri parçası türünde bir nesnedir."},{"facet_id":"F002","role":"specialization","statement":"Derinin siyah renkli olması anlamın belirtilen ayırıcı özelliğidir."}],"identity_rationale":"Kaynak ifadesi dalı siyah renkli ince deri olarak verir. Yakın komşular yazı yüzeyi veya beden örtüsü işlevlerini taşısa da bu dalda yazılmış olma, belirli bir kullanım veya genel deri anlamı belirtilmemiştir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"siyah ince deri"}],"lexicalization_note":"Tanım bağımsız nesne adını siyah ince deriyle sınırlar ve yazı, belge ya da beden örtüsü gibi komşu işlevleri içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan iki karşılaştırma siyah ince deriyi yazı yüzeyi olan ince deriden ve bedeni örten genel deriden ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal renk özelliğiyle, komşu dal ise yazı yüzeyi ve sayfa işleviyle sınırlandırılır; bu ek koşullar birbirinden farklıdır.","focus_only":"Odak dal ince derinin siyah renkli olmasını zorunlu kılar ve yazı işlevi belirtmez.","gloss":"yazı için ince deri yaprağı","neighbor_only":"Komşu dal üzerinde yazı bulunan veya yazı için açılmış ince deri ya da sayfa işlevini öne çıkarır.","neighbor_ref":"root_000586/B002","relation_type":"near_synonym","shared_zone":"Her iki dal ince deri yaprağı türündeki aynı nesne alanına yaklaşır."},{"boundary_match":"partial","distinction":"Odak işlenmiş veya ayrılmış ince bir deri parçasına ve siyah renge bağlıdır; komşu ise beden örtüsü olan deriyi temel alır.","focus_only":"Odak dal siyah ve ince bir deri parçasını bağımsız nesne olarak belirtir.","gloss":"bedeni örten deri","neighbor_only":"Komşu dal hayvan bedenini örten deriyi, göz derisini ve bedenle ilgili aktarmalı kullanımları genişçe kapsar.","neighbor_ref":"root_000253/B001","relation_type":"near_neighbor","shared_zone":"İki dalın ortak maddesi hayvansal deridir."}],"source_phrase_ar":"المساد الرق الأسود (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Dal yalnızca siyah ince deri anlamıyla tanıklanmıştır; başka bir işlev veya kapsam belirtilmemiştir."}],"source_summary":"Verilen tek tanıklık nesneyi siyah renkli ince deri olarak tanımlar; kullanım amacıyla ilgili ek bir koşul vermez.","sources":["TA"],"what_is_ar":"المِساد بمعنى الرق الأسود","what_is_not_ar":"ليس نحي السمن والعسل ولا الحبل ولا الفتل"},"support_links":[]},{"boundary":"Anlam yalnızca saçın yapısı ve güzel görünüşünü belirten söz öbeğinde geçerlidir.","branch_kind":"collocation","branch_ref":"root_001422/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّسَد","morph_features":"STEM|POS:N|LEM:m~asad|ROOT:msd|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:5:1","qac_word_ref":"111:5:5","surface_ar":"مَّسَدٍۭ"}],"gloss":"saçın düzgün yapısı ve güzel görünüşü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Saçın düzgün kuruluşunu ve biçimli duruşunu belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Saçın görünüş bakımından güzel ve beğenilir olmasını içerir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişinin saç yapısının başka bir kişininkinden daha güzel olduğu karşılaştırmada kullanılabilir."}}],"root_ar":"م س د","root_id":"root_001422","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca saçla kurulan söz öbeğinde, saçın kuruluşu ve görünüş güzelliği birlikte anlatıldığında kullanılır.","boundary_detail":"Anlam yalnızca saçın yapısı ve güzel görünüşünü belirten söz öbeğinde geçerlidir.","branch_image_ar":"مساد الشعر","concept_gloss":"saçın düzgün yapısı ve güzel görünüşü","contextual_glosses":[{"applicability":"İki kişinin saç kuruluşu ve görünüşü karşılaştırılırken akıcı bir yüklem karşılığı olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Saç yapısını, güzelliği ve karşılaştırmalı kullanımı korur."},"facet_ids":["F001","F002","F003"],"text":"saçı daha düzgün ve güzel","usage_role":"contextual"}],"definition":"Saçla kurulan belirli söz öbeğinde, saçın düzgün kuruluşunu, biçimli duruşunu ve güzel görünüşünü anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Saçın düzgün kuruluşunu ve biçimli duruşunu belirtir."},{"facet_id":"F002","role":"specialization","statement":"Saçın görünüş bakımından güzel ve beğenilir olmasını içerir."},{"facet_id":"F003","role":"example","statement":"Bir kişinin saç yapısının başka bir kişininkinden daha güzel olduğu karşılaştırmada kullanılabilir."}],"identity_rationale":"Kaynak ifadesi anlamı saçla kurulan belirli bir yapıya bağlar ve bir kişinin saç kuruluşunun başka bir kişininkinden daha düzgün veya güzel oluşunu anlatır. Bu nedenle genel güzellik ya da bağımsız bir saç türü anlamına genişletilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"saçın düzgün yapısı ve güzel görünüşü"}],"lexicalization_note":"Tanım açıkça saçla kurulan söz öbeğine bağlıdır; bu kullanım bağımsız ve genel bir kök anlamı olarak sunulmaz.","neighbor_coverage_note":"Tüm adaylar karşılaştırıldı; seçilen ilişkiler saçın düzgün ve güzel kuruluşunu saç dokusu veya tarama, kişide genel güzellik ve genel dış görünüş alanlarından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bütünsel yapı ve güzelliği değerlendirir; komşu ise belirli saç dokusunu veya tarama eylemini anlatır.","focus_only":"Odak dal saçın genel kuruluşunu ve güzel görünüşünü belirli bir söz öbeğinde değerlendirir.","gloss":"orta dalgalı veya taranmış saç","neighbor_only":"Komşu dal saçın ne çok kıvırcık ne de tümüyle düz olan dokusunu ve saçın taranmasını belirtir.","neighbor_ref":"root_000546/B010","relation_type":"near_neighbor","shared_zone":"İki dal da saçın biçimi ve düzenli görünüşüyle ilgilidir."},{"boundary_match":"partial","distinction":"Odak dal saç yapısının niteliğidir; komşu dal insanı bütün olarak niteler ve güzellik ile saç çokluğu arasında değişebilir.","focus_only":"Odak dal yalnızca saçın düzgün kuruluşu ve güzel görünüşü üzerinde durur.","gloss":"çok saçlı veya çok güzel kişi","neighbor_only":"Komşu dal kişinin genel güzelliğini ya da saçının çokluğunu niteleyebilir.","neighbor_ref":"root_001379/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal saç üzerinden beğenilen bir görünüşe bağlanabilir."},{"boundary_match":"field_only","distinction":"Odak saçla ve belirli yapıyla sınırlıdır; komşu ise görünüş güzelliğini saç koşulu olmadan genel biçimde anlatır.","focus_only":"Odak dal güzel görünüşü yalnızca saçın yapısı içinde ve belirli bir söz öbeğinde ifade eder.","gloss":"güzel dış görünüş","neighbor_only":"Komşu dal herhangi bir kişinin veya nesnenin dış görünüşündeki genel güzelliği kapsar.","neighbor_ref":"root_000615/B009","relation_type":"same_field","shared_zone":"İki dal görünüşün beğenilir ve güzel oluşu alanında buluşur."}],"source_phrase_ar":"فلان أحسن مساد شعر من فلان يريد أحسن قوام شعر (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, bir kişinin saç kuruluşunun başka bir kişininkinden daha güzel sayıldığı karşılaştırmalı kullanımı verir."}],"source_summary":"Verilen tanıklık, saçın düzgün kuruluşu ve güzel görünüşü anlamını kişiler arasında karşılaştırma yapılan bir örnekle gösterir.","sources":["TA"],"what_is_ar":"مساد الشعر، أي قوام الشعر وحسن هيئته","what_is_not_ar":"ليس الحبل ولا النحي ولا الرق الأسود ولا إدآب السير"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["111:5:1"],"branch_refs":[],"candidate_id":"cand_6a54247e3232e0d845d9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:5:1:boundary-scope-narrowed","source_type":"word_analysis","support_ids":["sup_287184b1fa344b42fab6","sup_de81961b891a13e83219"],"title":"boundary continuity does not override the clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:1","qac_refs":["111:5:1:1"],"status":"accepted"}},{"anchor_refs":["111:5:1"],"branch_refs":[],"candidate_id":"cand_7af1118a0f02505dc9fb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:5:1:fronted-predicate-reveal","source_type":"word_analysis","support_ids":["sup_9c09e2fb991ceade0d65","sup_de81961b891a13e83219"],"title":"location precedes the rope","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:1","qac_refs":["111:5:1:1"],"status":"accepted"}},{"anchor_refs":["111:5:1"],"branch_refs":[],"candidate_id":"cand_55a463872e7e6451c4f2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:5:1:locative-containment","source_type":"word_analysis","support_ids":["sup_6ad29a4c3e565a436674","sup_de81961b891a13e83219"],"title":"containment frames the neck-space","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:1","qac_refs":["111:5:1:1"],"status":"accepted"}},{"anchor_refs":["111:5:1"],"branch_refs":[],"candidate_id":"cand_15bf3f1ee38313276910","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:5:1:opening-sound-stretch","source_type":"word_analysis","support_ids":["sup_a5241a7cf8f26b67b0c3","sup_de81961b891a13e83219"],"title":"long vowel stretches the opening","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:1","qac_refs":["111:5:1:1"],"status":"accepted"}},{"anchor_refs":["111:5:2"],"branch_refs":[],"candidate_id":"cand_0925913e85692d281731","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000284"],"scope":"focus_ayah","source_local_id":"111:5:2:adornment-neck-reversal","source_type":"word_analysis","support_ids":["sup_3f0d1d1ccd69c450c042","sup_f9c6102222ef3aa4907d"],"title":"adornment site receives rough binding","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:2","qac_refs":["111:5:2:1","111:5:2:2"],"status":"accepted"}},{"anchor_refs":["111:5:2"],"branch_refs":[],"candidate_id":"cand_4a9b327adec3c2417acb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000284"],"scope":"focus_ayah","source_local_id":"111:5:2:attachment-boundary-narrowed","source_type":"word_analysis","support_ids":["sup_3f0d1d1ccd69c450c042","sup_6d484a63a5a0e3b751c0"],"title":"attachment choice is locally settled","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:2","qac_refs":["111:5:2:1","111:5:2:2"],"status":"accepted"}},{"anchor_refs":["111:5:2"],"branch_refs":[],"candidate_id":"cand_e2000101346b4adf7cbd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000284"],"scope":"focus_ayah","source_local_id":"111:5:2:body-part-bookend","source_type":"word_analysis","support_ids":["sup_1f1f82fab2d8293f008e","sup_3f0d1d1ccd69c450c042"],"title":"hands give way to neck","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:2","qac_refs":["111:5:2:1","111:5:2:2"],"status":"accepted"}},{"anchor_refs":["111:5:2"],"branch_refs":[],"candidate_id":"cand_5278ac250f32cf863b6c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000284"],"scope":"focus_ayah","source_local_id":"111:5:2:excellence-overlap-narrowed","source_type":"word_analysis","support_ids":["sup_3f0d1d1ccd69c450c042","sup_ecde4663f58461643079"],"title":"fineness pressure stays lexical-adjacent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:2","qac_refs":["111:5:2:1","111:5:2:2"],"status":"accepted"}},{"anchor_refs":["111:5:2"],"branch_refs":[],"candidate_id":"cand_c7b989bd69e5b521127e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000284"],"scope":"focus_ayah","source_local_id":"111:5:2:governed-front-neck-site","source_type":"word_analysis","support_ids":["sup_3f0d1d1ccd69c450c042","sup_472d218f0db21aed71bc"],"title":"one governed site is foregrounded","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:2","qac_refs":["111:5:2:1","111:5:2:2"],"status":"accepted"}},{"anchor_refs":["111:5:2"],"branch_refs":[],"candidate_id":"cand_2263bcd4d33481dc8660","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000284"],"scope":"focus_ayah","source_local_id":"111:5:2:possessive-boundary-referent","source_type":"word_analysis","support_ids":["sup_3f0d1d1ccd69c450c042","sup_a6546239459128c101bc"],"title":"suffix carries the prior woman","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:2","qac_refs":["111:5:2:1","111:5:2:2"],"status":"accepted"}},{"anchor_refs":["111:5:2"],"branch_refs":[],"candidate_id":"cand_0f6b2348c67fdc008722","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000284"],"scope":"focus_ayah","source_local_id":"111:5:2:rare-neck-choice","source_type":"word_analysis","support_ids":["sup_3f0d1d1ccd69c450c042","sup_d717681bbeab05d7b842"],"title":"hapax profile marks the choice","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:2","qac_refs":["111:5:2:1","111:5:2:2"],"status":"accepted"}},{"anchor_refs":["111:5:2"],"branch_refs":[],"candidate_id":"cand_1cc3e2d90460222a1d9d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000284"],"scope":"focus_ayah","source_local_id":"111:5:2:smooth-opening-cadence","source_type":"word_analysis","support_ids":["sup_3f0d1d1ccd69c450c042","sup_628268e5a57c391eb0c4"],"title":"neck phrase prolongs the opening","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:2","qac_refs":["111:5:2:1","111:5:2:2"],"status":"accepted"}},{"anchor_refs":["111:5:2"],"branch_refs":[],"candidate_id":"cand_285b3611dba0a22cb9da","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000284"],"scope":"focus_ayah","source_local_id":"111:5:2:throat-vulnerability-narrowed","source_type":"word_analysis","support_ids":["sup_3f0d1d1ccd69c450c042","sup_6de2d7c3d2176b1593a7"],"title":"vulnerability is secondary to front-neck sense","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:2","qac_refs":["111:5:2:1","111:5:2:2"],"status":"accepted"}},{"anchor_refs":["111:5:3"],"branch_refs":[],"candidate_id":"cand_f08df8b2717ec43122a8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000291"],"scope":"focus_ayah","source_local_id":"111:5:3:bond-field-narrowed-to-restraint","source_type":"word_analysis","support_ids":["sup_dcca9a8406d4d5859613","sup_e0966f3318d68354d818"],"title":"connection range becomes constriction","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:3","qac_refs":["111:5:3:1"],"status":"accepted"}},{"anchor_refs":["111:5:3"],"branch_refs":[],"candidate_id":"cand_03c657ad26c25e9c6f75","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000291"],"scope":"focus_ayah","source_local_id":"111:5:3:carrier-boundary-reversal","source_type":"word_analysis","support_ids":["sup_49f7557f945a927d3f76","sup_dcca9a8406d4d5859613"],"title":"carrying turns into being bound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:3","qac_refs":["111:5:3:1"],"status":"accepted"}},{"anchor_refs":["111:5:3"],"branch_refs":[],"candidate_id":"cand_1127c0580159cf72702e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000291"],"scope":"focus_ayah","source_local_id":"111:5:3:covenant-form-contrast","source_type":"word_analysis","support_ids":["sup_dcca9a8406d4d5859613","sup_f0b1b5b31879d83d4be7"],"title":"free indefinite form differs from covenant formula","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:3","qac_refs":["111:5:3:1"],"status":"accepted"}},{"anchor_refs":["111:5:3"],"branch_refs":[],"candidate_id":"cand_c23818888a508a17c3ef","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000291"],"scope":"focus_ayah","source_local_id":"111:5:3:delayed-subject-static-assertion","source_type":"word_analysis","support_ids":["sup_62a899feea6a4974e6a1","sup_dcca9a8406d4d5859613"],"title":"verbless clause fixes the rope as condition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:3","qac_refs":["111:5:3:1"],"status":"accepted"}},{"anchor_refs":["111:5:3"],"branch_refs":[],"candidate_id":"cand_b33832c47f8b7b3734aa","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000291"],"scope":"focus_ayah","source_local_id":"111:5:3:indefinite-binding-instrument","source_type":"word_analysis","support_ids":["sup_dcca9a8406d4d5859613","sup_dfa87f7133a73cff2eb1"],"title":"indefinite rope withholds identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:3","qac_refs":["111:5:3:1"],"status":"accepted"}},{"anchor_refs":["111:5:3"],"branch_refs":[],"candidate_id":"cand_3a731ef71a2bba9aff5d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000291"],"scope":"focus_ayah","source_local_id":"111:5:3:jugular-cord-pressure","source_type":"word_analysis","support_ids":["sup_90b5e683654c982b52e0","sup_dcca9a8406d4d5859613"],"title":"neck-cord echo sharpens bodily pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:3","qac_refs":["111:5:3:1"],"status":"accepted"}},{"anchor_refs":["111:5:3"],"branch_refs":[],"candidate_id":"cand_07e740db4858f232831f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000291"],"scope":"focus_ayah","source_local_id":"111:5:3:materially-specified-rope","source_type":"word_analysis","support_ids":["sup_d62dbc0d779c15c39e53","sup_dcca9a8406d4d5859613"],"title":"material phrase fixes the rope","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:3","qac_refs":["111:5:3:1"],"status":"accepted"}},{"anchor_refs":["111:5:3"],"branch_refs":[],"candidate_id":"cand_d5612f6afa9f7c77bbdc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000291"],"scope":"focus_ayah","source_local_id":"111:5:3:occurrence-spectrum-reversal","source_type":"word_analysis","support_ids":["sup_67f5038b796b37f17949","sup_dcca9a8406d4d5859613"],"title":"other rope contexts reverse into punishment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:3","qac_refs":["111:5:3:1"],"status":"accepted"}},{"anchor_refs":["111:5:3"],"branch_refs":[],"candidate_id":"cand_0bddc050b430e6ebf298","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000291"],"scope":"focus_ayah","source_local_id":"111:5:3:small-distribution-range","source_type":"word_analysis","support_ids":["sup_d134f2547519ea810899","sup_dcca9a8406d4d5859613"],"title":"small occurrence set spans concrete and abstract","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:3","qac_refs":["111:5:3:1"],"status":"accepted"}},{"anchor_refs":["111:5:3"],"branch_refs":[],"candidate_id":"cand_e9cd18c0828843504e48","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000291"],"scope":"focus_ayah","source_local_id":"111:5:3:snare-pressure","source_type":"word_analysis","support_ids":["sup_4d5c5d4c0ee59ce0ce74","sup_dcca9a8406d4d5859613"],"title":"snare branch colors the rope","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:3","qac_refs":["111:5:3:1"],"status":"accepted"}},{"anchor_refs":["111:5:3"],"branch_refs":[],"candidate_id":"cand_155b684696e8e8bb3a41","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000291"],"scope":"focus_ayah","source_local_id":"111:5:3:sound-and-tanwin-cadence","source_type":"word_analysis","support_ids":["sup_1e0f1fd4b98b3f6099f6","sup_dcca9a8406d4d5859613"],"title":"sound links rope and material","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:3","qac_refs":["111:5:3:1"],"status":"accepted"}},{"anchor_refs":["111:5:3"],"branch_refs":[],"candidate_id":"cand_3959ac3076d3ae4d8131","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000291"],"scope":"focus_ayah","source_local_id":"111:5:3:staged-reveal","source_type":"word_analysis","support_ids":["sup_d530df3b5c15f35bba11","sup_dcca9a8406d4d5859613"],"title":"rope arrives after the neck","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:3","qac_refs":["111:5:3:1"],"status":"accepted"}},{"anchor_refs":["111:5:4"],"branch_refs":[],"candidate_id":"cand_542d2aeaf2e192104fc8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:5:4:bayaniyya-material-identity","source_type":"word_analysis","support_ids":["sup_1f8e5de65bd6bc0921da","sup_942b9ba51f579513a0d9"],"title":"particle defines rope by material","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:4","qac_refs":["111:5:4:1"],"status":"accepted"}},{"anchor_refs":["111:5:4"],"branch_refs":[],"candidate_id":"cand_0da0aa16e6ddaa6ccec6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:5:4:mim-fusion","source_type":"word_analysis","support_ids":["sup_1f8e5de65bd6bc0921da","sup_43336620d099718e5aeb"],"title":"sound binds particle to material","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:4","qac_refs":["111:5:4:1"],"status":"accepted"}},{"anchor_refs":["111:5:4"],"branch_refs":[],"candidate_id":"cand_fdeecff8c352ffbb23d0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:5:4:object-to-substance-turn","source_type":"word_analysis","support_ids":["sup_1f8e5de65bd6bc0921da","sup_40c5c7b2d57fefd89c42"],"title":"final phrase closes the narrowing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:4","qac_refs":["111:5:4:1"],"status":"accepted"}},{"anchor_refs":["111:5:4"],"branch_refs":[],"candidate_id":"cand_faaeb5718c8b66e2e617","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:5:4:source-partitive-nuance-narrowed","source_type":"word_analysis","support_ids":["sup_1f8e5de65bd6bc0921da","sup_9ca78447e4472d2714f3"],"title":"other min values stay subordinate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:4","qac_refs":["111:5:4:1"],"status":"accepted"}},{"anchor_refs":["111:5:5"],"branch_refs":[],"candidate_id":"cand_28ccad2e47892394b35d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001422"],"scope":"focus_ayah","source_local_id":"111:5:5:final-sound-texture","source_type":"word_analysis","support_ids":["sup_10bdfc046d876570f178","sup_852c2e7061f3d23a501a"],"title":"sound compresses at the final material","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:5","qac_refs":["111:5:5:1"],"status":"accepted"}},{"anchor_refs":["111:5:5"],"branch_refs":[],"candidate_id":"cand_3e079bf4bfebcfc7eee5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001422"],"scope":"focus_ayah","source_local_id":"111:5:5:governed-material-complement","source_type":"word_analysis","support_ids":["sup_09115d7e1b36ee936d02","sup_10bdfc046d876570f178"],"title":"genitive complement gives rope composition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:5","qac_refs":["111:5:5:1"],"status":"accepted"}},{"anchor_refs":["111:5:5"],"branch_refs":[],"candidate_id":"cand_59f94f80e18b453d91cb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001422"],"scope":"focus_ayah","source_local_id":"111:5:5:hapax-title-closure","source_type":"word_analysis","support_ids":["sup_10bdfc046d876570f178","sup_f0dab67679c602c53579"],"title":"final hapax becomes the surah label","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:5","qac_refs":["111:5:5:1"],"status":"accepted"}},{"anchor_refs":["111:5:5"],"branch_refs":[],"candidate_id":"cand_19520c9f0ed0536b23c2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001422"],"scope":"focus_ayah","source_local_id":"111:5:5:indefinite-rough-material","source_type":"word_analysis","support_ids":["sup_10bdfc046d876570f178","sup_d76fc1b693336c80ace6"],"title":"indefinite material closes as texture","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:5","qac_refs":["111:5:5:1"],"status":"accepted"}},{"anchor_refs":["111:5:5"],"branch_refs":[],"candidate_id":"cand_690c48f94a9713e087d4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001422"],"scope":"focus_ayah","source_local_id":"111:5:5:load-and-plant-boundary","source_type":"word_analysis","support_ids":["sup_10bdfc046d876570f178","sup_67be4a463c915da4abf5"],"title":"firewood field returns as binding fiber","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:5","qac_refs":["111:5:5:1"],"status":"accepted"}},{"anchor_refs":["111:5:5"],"branch_refs":[],"candidate_id":"cand_32c49e8d113b5cde2a6f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001422"],"scope":"focus_ayah","source_local_id":"111:5:5:motion-to-static-fiber","source_type":"word_analysis","support_ids":["sup_10bdfc046d876570f178","sup_3e483e3c35a3f0e8f79d"],"title":"labor stops in fixed substance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:5","qac_refs":["111:5:5:1"],"status":"accepted"}},{"anchor_refs":["111:5:5"],"branch_refs":[],"candidate_id":"cand_315b3ff8d2c76f6c2a76","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001422"],"scope":"focus_ayah","source_local_id":"111:5:5:predicate-layer-narrowed","source_type":"word_analysis","support_ids":["sup_10bdfc046d876570f178","sup_fef53f58f7f2affc9015"],"title":"load-bearing role stays inside material phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:5","qac_refs":["111:5:5:1"],"status":"accepted"}},{"anchor_refs":["111:5:5"],"branch_refs":[],"candidate_id":"cand_7249475485efb410e309","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001422"],"scope":"focus_ayah","source_local_id":"111:5:5:secondary-compression-narrowed","source_type":"word_analysis","support_ids":["sup_10bdfc046d876570f178","sup_ad883f3993dcb09ae8d9"],"title":"darkness and bodily compression remain secondary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:5","qac_refs":["111:5:5:1"],"status":"accepted"}},{"anchor_refs":["111:5:5"],"branch_refs":[],"candidate_id":"cand_e33d2b962013f7996ed2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001422"],"scope":"focus_ayah","source_local_id":"111:5:5:surah-seal-material","source_type":"word_analysis","support_ids":["sup_10bdfc046d876570f178","sup_b70bb828f3f7203239be"],"title":"last word leaves tactile material","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:5","qac_refs":["111:5:5:1"],"status":"accepted"}},{"anchor_refs":["111:5:5"],"branch_refs":[],"candidate_id":"cand_4b5a6515a061887e4dfb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001422"],"scope":"focus_ayah","source_local_id":"111:5:5:title-form-contrast","source_type":"word_analysis","support_ids":["sup_0e24aadd70b004216741","sup_10bdfc046d876570f178"],"title":"unnamed material becomes named title","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:5","qac_refs":["111:5:5:1"],"status":"accepted"}},{"anchor_refs":["111:5:5"],"branch_refs":[],"candidate_id":"cand_2f54c10c728fe26eeaf6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001422"],"scope":"focus_ayah","source_local_id":"111:5:5:twisted-fiber-process","source_type":"word_analysis","support_ids":["sup_10bdfc046d876570f178","sup_5d09f7c2c1b8a284e2c6"],"title":"material keeps the act of twisting","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:5:5","qac_refs":["111:5:5:1"],"status":"accepted"}},{"anchor_refs":["111:5:2"],"branch_refs":[],"candidate_id":"cand_b390d8cbaf3d490aa217","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000284"],"scope":"focus_ayah","source_local_id":"111:5:2:1","source_type":"qac_morpheme","support_ids":["sup_2b05d9609a9cded6e453"],"title":"QAC root occurrence: ج ي د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["111:5:3"],"branch_refs":[],"candidate_id":"cand_9152ed0178ad9a64be27","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000291"],"scope":"focus_ayah","source_local_id":"111:5:3:1","source_type":"qac_morpheme","support_ids":["sup_a27ae16bb0ff553c90b3"],"title":"QAC root occurrence: ح ب ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["111:5:5"],"branch_refs":[],"candidate_id":"cand_b2e92ad1c4b8abea1ac9","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001422"],"scope":"focus_ayah","source_local_id":"111:5:5:1","source_type":"qac_morpheme","support_ids":["sup_103ee64ecb2e87ced15e"],"title":"QAC root occurrence: م س د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["111:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"111:5","branch_refs":["root_000284/B001","root_000291/B001","root_001422/B001"],"candidate_id":"cand_95babfbcc004a565e904","commentary_obligation":"review","hft_ref":"hft_f6488e21b00df5b82c46","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b01_neck_halter","source_type":"hft","support_ids":["sup_619d8105a0e1cc83eb79"],"title":"b01_neck_halter","trust":"legacy_unbound"},{"anchor_refs":["111:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"111:5","branch_refs":["root_000284/B001","root_000291/B008","root_001422/B001"],"candidate_id":"cand_2fdced5c1589ea1bdfdc","commentary_obligation":"review","hft_ref":"hft_0eb8b609ebe62bd9a0d5","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b02_inverted_necklace","source_type":"hft","support_ids":["sup_57e3c6af36af0c4bffed"],"title":"b02_inverted_necklace","trust":"legacy_unbound"},{"anchor_refs":["111:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"111:5","branch_refs":["root_000284/B001","root_000291/B002","root_001422/B001"],"candidate_id":"cand_ac8d8659ce8481fc5aac","commentary_obligation":"review","hft_ref":"hft_94f029a9aec5a1fa6ba8","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b03_protection_inverted","source_type":"hft","support_ids":["sup_0c0f822a5ee347126fb0"],"title":"b03_protection_inverted","trust":"legacy_unbound"},{"anchor_refs":["111:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"111:5","branch_refs":["root_000284/B001","root_000291/B005","root_000291/B011","root_001422/B001"],"candidate_id":"cand_0807c6428416b020e630","commentary_obligation":"review","hft_ref":"hft_06521e42afaa8a02f948","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b04_snare_that_closes","source_type":"hft","support_ids":["sup_500faf58bc2cb81867aa"],"title":"b04_snare_that_closes","trust":"legacy_unbound"},{"anchor_refs":["111:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"111:5","branch_refs":["root_000284/B001","root_000291/B004","root_001422/B002"],"candidate_id":"cand_b52007d35c7c96d74abe","commentary_obligation":"review","hft_ref":"hft_b6c5c62c2548249e6c0f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b05_constraint_embodied","source_type":"hft","support_ids":["sup_908f195f4a0af0b20175"],"title":"b05_constraint_embodied","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ","qac_morphemes":[{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"111:5:1:1","qac_word_ref":"111:5:1","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"جِيد","morph_features":"STEM|POS:N|LEM:jiyd|ROOT:jyd|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:2:1","qac_word_ref":"111:5:2","root_ar":"ج ي د","surface_ar":"جِيدِ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"111:5:2:2","qac_word_ref":"111:5:2","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"حَبْل","morph_features":"STEM|POS:N|LEM:Habol|ROOT:Hbl|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:3:1","qac_word_ref":"111:5:3","root_ar":"ح ب ل","surface_ar":"حَبْلٌ"},{"lemma_ar":"مِن","morph_features":"STEM|POS:P|LEM:min","morpheme_role":"STEM","pos":"P","qac_ref":"111:5:4:1","qac_word_ref":"111:5:4","root_ar":"","surface_ar":"مِّن"},{"lemma_ar":"مَّسَد","morph_features":"STEM|POS:N|LEM:m~asad|ROOT:msd|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:5:1","qac_word_ref":"111:5:5","root_ar":"م س د","surface_ar":"مَّسَدٍۭ"}],"word_analysis_qac_refs":[["111:5:1:1"],["111:5:2:1","111:5:2:2"],["111:5:3:1"],["111:5:4:1"],["111:5:5:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["111:5:1","111:5:2","111:5:3","111:5:4","111:5:5"]},"focus_surface_evidence":{"arabic_uthmani":"فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ","qac_morphemes":[{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"111:5:1:1","qac_word_ref":"111:5:1","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"جِيد","morph_features":"STEM|POS:N|LEM:jiyd|ROOT:jyd|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:2:1","qac_word_ref":"111:5:2","root_ar":"ج ي د","surface_ar":"جِيدِ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"111:5:2:2","qac_word_ref":"111:5:2","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"حَبْل","morph_features":"STEM|POS:N|LEM:Habol|ROOT:Hbl|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:3:1","qac_word_ref":"111:5:3","root_ar":"ح ب ل","surface_ar":"حَبْلٌ"},{"lemma_ar":"مِن","morph_features":"STEM|POS:P|LEM:min","morpheme_role":"STEM","pos":"P","qac_ref":"111:5:4:1","qac_word_ref":"111:5:4","root_ar":"","surface_ar":"مِّن"},{"lemma_ar":"مَّسَد","morph_features":"STEM|POS:N|LEM:m~asad|ROOT:msd|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"111:5:5:1","qac_word_ref":"111:5:5","root_ar":"م س د","surface_ar":"مَّسَدٍۭ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["111:5:1:1"],["111:5:2:1","111:5:2:2"],["111:5:3:1"],["111:5:4:1"],["111:5:5:1"]],"word_analysis_refs":["111:5:1","111:5:2","111:5:3","111:5:4","111:5:5"],"word_rows":[{"analysis_record_ref":"111:5:1","analytic_gloss_range_en":"locative preposition governing the possessed neck phrase, with containment or encirclement force rather than simple surface placement","analytic_root_gloss_range_en":null,"qac_refs":["111:5:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"فِى","transliteration":"fī"}},{"analysis_record_ref":"111:5:2","analytic_gloss_range_en":"her possessed front-neck or adornment-neck, governed by the locative preposition and tied by suffix to the woman of 111:4","analytic_root_gloss_range_en":"front of the neck, especially a fine or necklace-bearing neck; local usage selects the body part while allowing adornment and display pressure","qac_refs":["111:5:2:1","111:5:2:2"],"root":{"arabic":"ج ي د","transliteration":"j-y-d"},"surface":{"arabic":"جِيدِهَا","transliteration":"jīdihā"}},{"analysis_record_ref":"111:5:3","analytic_gloss_range_en":"an indefinite rope as delayed subject of the nominal clause, materially specified by the following phrase and locally functioning as constricting binding","analytic_root_gloss_range_en":"rope, cord, bond, covenant, connection, anatomical cord, snare, and other extended-line branches; the local phrase selects the physical rope while retaining narrowed bond and occurrence-spectrum pressure","qac_refs":["111:5:3:1"],"root":{"arabic":"ح ب ل","transliteration":"ḥ-b-l"},"surface":{"arabic":"حَبْلٌ","transliteration":"ḥablun"}},{"analysis_record_ref":"111:5:4","analytic_gloss_range_en":"material-specifying preposition that makes the following noun define the rope's composition, with source or partitive alternatives narrowed out locally","analytic_root_gloss_range_en":null,"qac_refs":["111:5:4:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"مِّن","transliteration":"min"}},{"analysis_record_ref":"111:5:5","analytic_gloss_range_en":"indefinite genitive material noun specifying tightly twisted fiber or palm-fiber rope as the composition of the preceding rope","analytic_root_gloss_range_en":"twisted rope, firm twisting, palm fiber or similar coarse cordage, with secondary compression, darkness, body-form, and material extensions narrowed under the local rope-composition sense","qac_refs":["111:5:5:1"],"root":{"arabic":"م س د","transliteration":"m-s-d"},"surface":{"arabic":"مَسَدٍ","transliteration":"masadin"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["111:5"],"branch_refs":["root_000284/B001","root_000291/B001","root_001422/B001"],"candidate_id":"cand_95babfbcc004a565e904","evidence_scope":"focus_ayah","hft_ref":"hft_f6488e21b00df5b82c46","item_id":"b01_neck_halter","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b01_neck_halter","support_id":"sup_619d8105a0e1cc83eb79"},{"anchor_refs":["111:5"],"branch_refs":["root_000284/B001","root_000291/B008","root_001422/B001"],"candidate_id":"cand_2fdced5c1589ea1bdfdc","evidence_scope":"focus_ayah","hft_ref":"hft_0eb8b609ebe62bd9a0d5","item_id":"b02_inverted_necklace","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b02_inverted_necklace","support_id":"sup_57e3c6af36af0c4bffed"},{"anchor_refs":["111:5"],"branch_refs":["root_000284/B001","root_000291/B002","root_001422/B001"],"candidate_id":"cand_ac8d8659ce8481fc5aac","evidence_scope":"focus_ayah","hft_ref":"hft_94f029a9aec5a1fa6ba8","item_id":"b03_protection_inverted","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b03_protection_inverted","support_id":"sup_0c0f822a5ee347126fb0"},{"anchor_refs":["111:5"],"branch_refs":["root_000284/B001","root_000291/B005","root_000291/B011","root_001422/B001"],"candidate_id":"cand_0807c6428416b020e630","evidence_scope":"focus_ayah","hft_ref":"hft_06521e42afaa8a02f948","item_id":"b04_snare_that_closes","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b04_snare_that_closes","support_id":"sup_500faf58bc2cb81867aa"},{"anchor_refs":["111:5"],"branch_refs":["root_000284/B001","root_000291/B004","root_001422/B002"],"candidate_id":"cand_b52007d35c7c96d74abe","evidence_scope":"focus_ayah","hft_ref":"hft_b6c5c62c2548249e6c0f","item_id":"b05_constraint_embodied","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b05_constraint_embodied","support_id":"sup_908f195f4a0af0b20175"}],"diagnostics":[],"lane_counts":{"global":10,"macro":13,"micro":5},"packet_summary":{"ayah_count":5,"focus_ref":"111:5","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ي د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001693","furuq_root_norm":"ي د ي","furuq_source_root_norm":"ي د ي","is_dominant":true,"target_occurrences":107,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000071","furuq_root_norm":"ء ي د","furuq_source_root_norm":"أ ي د","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]}],"window":["111:1","111:2","111:3","111:4","111:5"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"111:5","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":18,"unstructured_record_count":0},"identity":{"ayah_ref":"111:5","lane":"micro","linguistic_source_ref":"111:5","surface_ref":"111:5","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"111:5","target_tokens":[["Boynunda",["111:5:1","111:5:2"]],["liften",["111:5:4","111:5:5"]],["bir",["111:5:3"]],["ip",["111:5:3"]],["vardır",["111:5:3"]]],"text":"Boynunda liften bir ip vardır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":5,"id":"s111-p01-001-005","label":"Whole surah","number":1,"refs":["111:1","111:2","111:3","111:4","111:5"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:5:governed-material-complement","source_type":"word_analysis","support_id":"sup_09115d7e1b36ee936d02","text":"{\"blocking_evidence\":null,\"headline\":\"genitive complement gives rope composition\",\"reader_payoff\":\"The reader notices that the final noun is the rope's governed substance, not a second object in the scene.\",\"reason\":\"QAC and attachment evidence mark {{ar:مَسَدٍ}} ({{tr:masadin}}) as genitive under {{ar:مِّن}} ({{tr:min}}), specifying the material of {{ar:حَبْلٌ}} ({{tr:ḥablun}}).\",\"representative_source_ids\":[\"QG-8447ee1a\",\"QG-b0ff4930\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:5:title-form-contrast","source_type":"word_analysis","support_id":"sup_0e24aadd70b004216741","text":"{\"blocking_evidence\":null,\"headline\":\"unnamed material becomes named title\",\"reader_payoff\":\"The reader notices the contrast between the indefinite in-ayah material and the title-like name by which the surah is known.\",\"reason\":\"Inside the ayah {{ar:مَسَدٍ}} ({{tr:masadin}}) is indefinite and genitive, while QAC notes the surah's naming from this word.\",\"representative_source_ids\":[\"QF-acf654e3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"111:5:5:1","source_type":"qac_morpheme","support_id":"sup_103ee64ecb2e87ced15e","text":"{\"lemma_ar\":\"مَّسَد\",\"morph_features\":\"STEM|POS:N|LEM:m~asad|ROOT:msd|M|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"111:5:5:1\",\"qac_word_ref\":\"111:5:5\",\"root_ar\":\"م س د\",\"surface_ar\":\"مَّسَدٍۭ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:5","source_type":"word_analysis","support_id":"sup_10bdfc046d876570f178","text":"{\"gloss_range\":\"indefinite genitive material noun specifying tightly twisted fiber or palm-fiber rope as the composition of the preceding rope\",\"prose\":\"{{ar:مَسَدٍ}} ({{tr:masadin}}) is the final material landing of the ayah and the surah. Governed by {{ar:مِّن}} ({{tr:min}}), it is the rope's load-bearing material complement, not a second object or independent predicate, and it makes the rope's composition coarse, twisted fiber rather than a neutral or ornamental cord. Its indefiniteness leaves the material unnamed as a known object, while the root image keeps process inside the noun: fiber has been tightened into binding. Secondary lexicon extensions toward darkness, bodily compression, or gauntness are useful only as narrowed pressures; the local sense remains the rope-material branch. The word also answers the prior plant-material field of {{ar:ٱلْحَطَبِ}} ({{tr:al-ḥaṭab}}) in 111:4, changing carried firewood into binding fiber as mobile labor stops in a fixed substance. As the final word, it leaves rough material as the last heard detail, and its repeated mīm and closure-friction-stop sound texture make that final material feel compressed. The in-ayah indefinite material also becomes the named label of the surah.\",\"root_display\":\"{{ar:م س د}} ({{tr:m-s-d}})\",\"root_gloss_range\":\"twisted rope, firm twisting, palm fiber or similar coarse cordage, with secondary compression, darkness, body-form, and material extensions narrowed under the local rope-composition sense\",\"surface_display\":\"{{ar:مَسَدٍ}} ({{tr:masadin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:3:sound-and-tanwin-cadence","source_type":"word_analysis","support_id":"sup_1e0f1fd4b98b3f6099f6","text":"{\"blocking_evidence\":null,\"headline\":\"sound links rope and material\",\"reader_payoff\":\"The reader hears the rope-word's constricted onset and its tanwīn pairing with the final material noun.\",\"reason\":\"{{ar:حَبْلٌ}} ({{tr:ḥablun}}) and {{ar:مَسَدٍ}} ({{tr:masadin}}) both carry tanwīn, and the CRITICAL sound row identifies the internal movement of the rope-word.\",\"representative_source_ids\":[\"QP-09813218\",\"QP-60e89bd2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:2:body-part-bookend","source_type":"word_analysis","support_id":"sup_1f1f82fab2d8293f008e","text":"{\"blocking_evidence\":null,\"headline\":\"hands give way to neck\",\"reader_payoff\":\"The reader notices the surah's bodily movement from the hands in 111:1 to the bound neck in 111:5.\",\"reason\":\"The CRITICAL rows supply the same-surah body-part comparison between {{ar:يَدَا}} ({{tr:yadā}}) in 111:1 and {{ar:جِيدِهَا}} ({{tr:jīdihā}}) in 111:5; no guardrail evidence contradicts that structural echo.\",\"representative_source_ids\":[\"QE-547b229f\",\"QE-84730a44\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:4","source_type":"word_analysis","support_id":"sup_1f8e5de65bd6bc0921da","text":"{\"gloss_range\":\"material-specifying preposition that makes the following noun define the rope's composition, with source or partitive alternatives narrowed out locally\",\"prose\":\"{{ar:مِّن}} ({{tr:min}}) is the hinge from object to substance. After {{ar:حَبْلٌ}} ({{tr:ḥablun}}) names the rope, {{ar:مِّن}} ({{tr:min}}) introduces {{ar:مَسَدٍ}} ({{tr:masadin}}) as the rope's composition, not merely its origin or a portion of it. That material-specifying force makes the coarse fiber definitional for the rope. The doubled mīm across {{ar:مِّن مَسَدٍ}} ({{tr:min masadin}}) also makes the grammatical dependency audible, as the particle is drawn into the material word it governs.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مِّن}} ({{tr:min}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:1:boundary-scope-narrowed","source_type":"word_analysis","support_id":"sup_287184b1fa344b42fab6","text":"{\"blocking_evidence\":null,\"headline\":\"boundary continuity does not override the clause\",\"reader_payoff\":\"The reader notices that the opening phrase keeps continuity with the prior woman, while the local syntax still forms its own nominal assertion.\",\"reason\":\"The CRITICAL row's boundary sensitivity survives, but attachment evidence forces {{ar:فِى جِيدِهَا}} ({{tr:fī jīdihā}}) as the predicate linked to {{ar:حَبْلٌ}} ({{tr:ḥablun}}), not as the governing continuation of the previous ayah.\",\"representative_source_ids\":[\"QG-2100e07e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"111:5:2:1","source_type":"qac_morpheme","support_id":"sup_2b05d9609a9cded6e453","text":"{\"lemma_ar\":\"جِيد\",\"morph_features\":\"STEM|POS:N|LEM:jiyd|ROOT:jyd|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"111:5:2:1\",\"qac_word_ref\":\"111:5:2\",\"root_ar\":\"ج ي د\",\"surface_ar\":\"جِيدِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:5:motion-to-static-fiber","source_type":"word_analysis","support_id":"sup_3e483e3c35a3f0e8f79d","text":"{\"blocking_evidence\":null,\"headline\":\"labor stops in fixed substance\",\"reader_payoff\":\"The reader notices that the prior mobile carrying role gives way to a static material noun at the close.\",\"reason\":\"The boundary moves from {{ar:حَمَّالَةَ}} ({{tr:ḥammālata}}) in 111:4 to the final static noun {{ar:مَسَدٍ}} ({{tr:masadin}}) in the verbless nominal scene.\",\"representative_source_ids\":[\"QB-6664d2b5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:2","source_type":"word_analysis","support_id":"sup_3f0d1d1ccd69c450c042","text":"{\"gloss_range\":\"her possessed front-neck or adornment-neck, governed by the locative preposition and tied by suffix to the woman of 111:4\",\"prose\":\"{{ar:جِيدِهَا}} ({{tr:jīdihā}}) is not a generic neck. The suffix makes it her neck and carries the woman of {{ar:ٱمْرَأَتُهُۥ}} ({{tr:imraʾatuhu}}) from 111:4 into the final image without renaming her. The governed singular form fixes one exposed front-neck before the rope is named, so the later rope is read through that body location; the neck phrase remains the hinge of boundary continuity while attachment evidence keeps it inside the local nominal clause. Lexically, the word selects the visible front-neck associated with adornment, so the rough rope becomes a reversal at the very site where ornament and status would normally be displayed. The word is also rare in the supplied Quranic profile, which makes this front-neck choice marked. A throat-passage pressure can be kept only as a narrowed effect of neck vulnerability, and a faint fineness or excellence pressure can remain at the edge of the word, while the local sense remains the adorned front of the neck. The closing image also moves the surah's body frame from hands in 111:1 to a bound neck in 111:5, with the long opening cadence of the neck phrase giving way to the abrupt rope-word.\",\"root_display\":\"{{ar:ج ي د}} ({{tr:j-y-d}})\",\"root_gloss_range\":\"front of the neck, especially a fine or necklace-bearing neck; local usage selects the body part while allowing adornment and display pressure\",\"surface_display\":\"{{ar:جِيدِهَا}} ({{tr:jīdihā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:4:object-to-substance-turn","source_type":"word_analysis","support_id":"sup_40c5c7b2d57fefd89c42","text":"{\"blocking_evidence\":null,\"headline\":\"final phrase closes the narrowing\",\"reader_payoff\":\"The reader feels the image narrow from location, to object, to tactile substance.\",\"reason\":\"The word order places {{ar:مِّن مَسَدٍ}} ({{tr:min masadin}}) after the location and rope, making {{ar:مِّن}} ({{tr:min}}) the turn into material closure.\",\"representative_source_ids\":[\"QT-7c49fa1e\",\"QT-a02ab173\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:4:mim-fusion","source_type":"word_analysis","support_id":"sup_43336620d099718e5aeb","text":"{\"blocking_evidence\":null,\"headline\":\"sound binds particle to material\",\"reader_payoff\":\"The reader hears the particle and material noun fuse at the same point where syntax binds them.\",\"reason\":\"The adjacent mīm sounds in {{ar:مِّن مَسَدٍ}} ({{tr:min masadin}}) create a local acoustic attachment matching the grammatical dependency.\",\"representative_source_ids\":[\"QF-344c8753\",\"QF-9f5570e2\",\"QP-e14d40e3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:2:governed-front-neck-site","source_type":"word_analysis","support_id":"sup_472d218f0db21aed71bc","text":"{\"blocking_evidence\":null,\"headline\":\"one governed site is foregrounded\",\"reader_payoff\":\"The reader notices one exposed neck-site fixed before the rope is named, so the rope reads through that body location.\",\"reason\":\"{{ar:جِيدِهَا}} ({{tr:jīdihā}}) is governed by {{ar:فِى}} ({{tr:fī}}) inside the fronted predicate, and the singular possessed noun narrows the scene to a single visible site.\",\"representative_source_ids\":[\"QG-4df9fdce\",\"QF-4a320269\",\"QT-27a39432\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:3:carrier-boundary-reversal","source_type":"word_analysis","support_id":"sup_49f7557f945a927d3f76","text":"{\"blocking_evidence\":null,\"headline\":\"carrying turns into being bound\",\"reader_payoff\":\"The reader notices the boundary shift from the active carrier in 111:4 to the static rope fixed on her in 111:5.\",\"reason\":\"The prior {{ar:حَمَّالَةَ}} ({{tr:ḥammālata}}) in 111:4 supplies the carrier frame, while {{ar:حَبْلٌ}} ({{tr:ḥablun}}) in the verbless clause supplies the fixed binding instrument.\",\"representative_source_ids\":[\"QB-959f98e6\",\"QB-965f92f1\",\"QY-87e1e50e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:3:snare-pressure","source_type":"word_analysis","support_id":"sup_4d5c5d4c0ee59ce0ce74","text":"{\"blocking_evidence\":null,\"headline\":\"snare branch colors the rope\",\"reader_payoff\":\"The reader can feel the rope as an ensnaring instrument, while the local noun still denotes the rope itself.\",\"reason\":\"V4 includes a snare branch for {{ar:ح ب ل}} ({{tr:ḥ-b-l}}), but the local surface {{ar:حَبْلٌ}} ({{tr:ḥablun}}) with material specification keeps rope as the selected gloss.\",\"representative_source_ids\":[\"QS-eb2f13da\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:5:twisted-fiber-process","source_type":"word_analysis","support_id":"sup_5d09f7c2c1b8a284e2c6","text":"{\"blocking_evidence\":null,\"headline\":\"material keeps the act of twisting\",\"reader_payoff\":\"The reader notices that the material is not soft or neutral; it is fiber tightened by twisting, so process-force remains inside the noun.\",\"reason\":\"QAC and V4 support {{ar:مَسَدٍ}} ({{tr:masadin}}) as twisted rope, palm fiber, or firm twisting, matching the local material complement.\",\"representative_source_ids\":[\"QS-0764c011\",\"QS-2655445b\",\"QS-80209765\",\"QF-0099583c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:2:smooth-opening-cadence","source_type":"word_analysis","support_id":"sup_628268e5a57c391eb0c4","text":"{\"blocking_evidence\":null,\"headline\":\"neck phrase prolongs the opening\",\"reader_payoff\":\"The reader hears the opening locative phrase lengthen before the abrupt rope-word interrupts it.\",\"reason\":\"{{ar:جِيدِهَا}} ({{tr:jīdihā}}) continues the long-vowel opening begun by {{ar:فِى}} ({{tr:fī}}), before {{ar:حَبْلٌ}} ({{tr:ḥablun}}) lands.\",\"representative_source_ids\":[\"QP-d21ca79c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:3:delayed-subject-static-assertion","source_type":"word_analysis","support_id":"sup_62a899feea6a4974e6a1","text":"{\"blocking_evidence\":null,\"headline\":\"verbless clause fixes the rope as condition\",\"reader_payoff\":\"The reader notices that the clause does not narrate tying; it asserts the rope's presence as a fixed state after the location has been set.\",\"reason\":\"The local clause is analyzed as a nominal sentence with {{ar:حَبْلٌ}} ({{tr:ḥablun}}) as the delayed subject; possible existential supply in translation does not add an overt Arabic verb.\",\"representative_source_ids\":[\"QG-270faa9e\",\"QG-adab9144\",\"QT-54c588b5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:5:load-and-plant-boundary","source_type":"word_analysis","support_id":"sup_67be4a463c915da4abf5","text":"{\"blocking_evidence\":null,\"headline\":\"firewood field returns as binding fiber\",\"reader_payoff\":\"The reader notices the same-surah material turn from firewood she carried in 111:4 to plant fiber that binds her in 111:5.\",\"reason\":\"The boundary evidence relates {{ar:ٱلْحَطَبِ}} ({{tr:al-ḥaṭab}}) in 111:4 to {{ar:مَسَدٍ}} ({{tr:masadin}}) in 111:5 as a shift from combustible plant matter to binding plant fiber.\",\"representative_source_ids\":[\"QS-6b7db7b9\",\"QI-e8ea9ee5\",\"QE-846346d4\",\"QB-96c94a42\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:3:occurrence-spectrum-reversal","source_type":"word_analysis","support_id":"sup_67f5038b796b37f17949","text":"{\"blocking_evidence\":null,\"headline\":\"other rope contexts reverse into punishment\",\"reader_payoff\":\"The reader sees this rope against a Quranic occurrence spectrum where covenant, illusion, and anatomical cord are reversed into punitive material binding.\",\"reason\":\"The CRITICAL evidence cites covenant-rope in 3:103 and 3:112, magicians' ropes in 20:66 and 26:44, and {{ar:حَبْلِ الْوَرِيدِ}} ({{tr:ḥabli l-warīd}}) in 50:16; local material specification prevents those from becoming the selected sense.\",\"representative_source_ids\":[\"MS-7f777d41\",\"QI-58c024b9\",\"QE-bbe1f594\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:1:locative-containment","source_type":"word_analysis","support_id":"sup_6ad29a4c3e565a436674","text":"{\"blocking_evidence\":null,\"headline\":\"containment frames the neck-space\",\"reader_payoff\":\"The reader notices that the rope is framed as embedded in the neck-space rather than simply lying on a surface.\",\"reason\":\"QAC and attachment evidence identify {{ar:فِى}} ({{tr:fī}}) as governing {{ar:جِيدِهَا}} ({{tr:jīdihā}}), with local locative force that supports encirclement or containment.\",\"representative_source_ids\":[\"QG-5885fbfa\",\"MG-b997cc06\",\"QS-5dc9e5f0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:2:attachment-boundary-narrowed","source_type":"word_analysis","support_id":"sup_6d484a63a5a0e3b751c0","text":"{\"blocking_evidence\":null,\"headline\":\"attachment choice is locally settled\",\"reader_payoff\":\"The reader sees why the neck phrase is the hinge of boundary continuity, while still reading it as part of the local nominal clause.\",\"reason\":\"The alternative PP attachment is narrowed because attachment evidence marks {{ar:فِى جِيدِهَا}} ({{tr:fī jīdihā}}) as the fronted predicate of {{ar:حَبْلٌ}} ({{tr:ḥablun}}).\",\"representative_source_ids\":[\"QG-9ad21a51\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:2:throat-vulnerability-narrowed","source_type":"word_analysis","support_id":"sup_6de2d7c3d2176b1593a7","text":"{\"blocking_evidence\":null,\"headline\":\"vulnerability is secondary to front-neck sense\",\"reader_payoff\":\"The reader can feel neck vulnerability in the placement, while the selected lexical sense remains the visible front-neck rather than a separate throat-channel term.\",\"reason\":\"V4 and QAC select front-neck meaning for {{ar:جِيدِهَا}} ({{tr:jīdihā}}); constriction near breath or voice is a local image pressure, not the primary gloss.\",\"representative_source_ids\":[\"QS-c0f8ea0d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:5:final-sound-texture","source_type":"word_analysis","support_id":"sup_852c2e7061f3d23a501a","text":"{\"blocking_evidence\":null,\"headline\":\"sound compresses at the final material\",\"reader_payoff\":\"The reader hears repeated mīm and the final consonant movement make the material phrase feel tight and abrasive.\",\"reason\":\"The adjacent {{ar:مِّن مَسَدٍ}} ({{tr:min masadin}}) repeats mīm, and the CRITICAL sound rows track the final word's movement from closure through friction to stop.\",\"representative_source_ids\":[\"QE-0b382242\",\"QP-779ad1f7\",\"QP-9f3d67b0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:3:jugular-cord-pressure","source_type":"word_analysis","support_id":"sup_90b5e683654c982b52e0","text":"{\"blocking_evidence\":null,\"headline\":\"neck-cord echo sharpens bodily pressure\",\"reader_payoff\":\"The reader notices that the rope at the neck is sharpened by the Quranic neck-cord occurrence (50:16), though it remains an external rope here.\",\"reason\":\"The occurrence echo to {{ar:حَبْلِ الْوَرِيدِ}} ({{tr:ḥabli l-warīd}}) in 50:16 is useful as bodily pressure, but the material phrase in 111:5 selects rope, not anatomical cord.\",\"representative_source_ids\":[\"QS-0196254b\",\"QE-3211bc99\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:4:bayaniyya-material-identity","source_type":"word_analysis","support_id":"sup_942b9ba51f579513a0d9","text":"{\"blocking_evidence\":null,\"headline\":\"particle defines rope by material\",\"reader_payoff\":\"The reader notices that the final phrase tells what the rope consists of, not where it came from.\",\"reason\":\"QAC and attachment evidence mark {{ar:مِّن}} ({{tr:min}}) as material-specifying before {{ar:مَسَدٍ}} ({{tr:masadin}}), attached to {{ar:حَبْلٌ}} ({{tr:ḥablun}}).\",\"representative_source_ids\":[\"QG-3939aa3d\",\"QG-45181678\",\"MG-97b2e93f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:1:fronted-predicate-reveal","source_type":"word_analysis","support_id":"sup_9c09e2fb991ceade0d65","text":"{\"blocking_evidence\":null,\"headline\":\"location precedes the rope\",\"reader_payoff\":\"The reader notices the sequence of disclosure: first the binding site, then the rope that answers it.\",\"reason\":\"The clause is marked as a nominal clause with {{ar:فِى جِيدِهَا}} ({{tr:fī jīdihā}}) fronted before the delayed subject {{ar:حَبْلٌ}} ({{tr:ḥablun}}).\",\"representative_source_ids\":[\"QT-5db57144\",\"QT-cca19bbf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:4:source-partitive-nuance-narrowed","source_type":"word_analysis","support_id":"sup_9ca78447e4472d2714f3","text":"{\"blocking_evidence\":null,\"headline\":\"other min values stay subordinate\",\"reader_payoff\":\"The reader notices that possible source or partitive associations remain backgrounded while material explanation governs the line.\",\"reason\":\"The row's broader possibilities are narrowed because the input grammar explicitly distinguishes this {{ar:مِّن}} ({{tr:min}}) from partitive or ablative uses.\",\"representative_source_ids\":[\"QS-85e0e67e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"111:5:3:1","source_type":"qac_morpheme","support_id":"sup_a27ae16bb0ff553c90b3","text":"{\"lemma_ar\":\"حَبْل\",\"morph_features\":\"STEM|POS:N|LEM:Habol|ROOT:Hbl|M|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"111:5:3:1\",\"qac_word_ref\":\"111:5:3\",\"root_ar\":\"ح ب ل\",\"surface_ar\":\"حَبْلٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:1:opening-sound-stretch","source_type":"word_analysis","support_id":"sup_a5241a7cf8f26b67b0c3","text":"{\"blocking_evidence\":null,\"headline\":\"long vowel stretches the opening\",\"reader_payoff\":\"The reader hears the locative opening stretch across the governed neck phrase before the rope lands.\",\"reason\":\"The surface sequence {{ar:فِى جِيدِهَا}} ({{tr:fī jīdihā}}) repeats a long high vowel across the preposition and governed noun.\",\"representative_source_ids\":[\"QP-0c1047f4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:2:possessive-boundary-referent","source_type":"word_analysis","support_id":"sup_a6546239459128c101bc","text":"{\"blocking_evidence\":null,\"headline\":\"suffix carries the prior woman\",\"reader_payoff\":\"The reader notices that the woman is carried into 111:5 by a bound suffix on the body part, not by being renamed.\",\"reason\":\"Attachment evidence resolves the 3fs suffix in {{ar:جِيدِهَا}} ({{tr:jīdihā}}) to {{ar:ٱمْرَأَتُهُۥ}} ({{tr:imraʾatuhu}}) in 111:4 and marks the suffix as the possessive dependent.\",\"representative_source_ids\":[\"QG-2c54180a\",\"QG-875aff37\",\"QB-6ab0a5c9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:5:secondary-compression-narrowed","source_type":"word_analysis","support_id":"sup_ad883f3993dcb09ae8d9","text":"{\"blocking_evidence\":null,\"headline\":\"darkness and bodily compression remain secondary\",\"reader_payoff\":\"The reader can feel darker enclosure and bodily compression as extensions of tight twisting, while the selected sense remains coarse rope-material.\",\"reason\":\"V4 lists secondary branches for compact body, night exertion, black hide, and other extensions, but the local {{ar:مِّن}} ({{tr:min}}) phrase selects the twisted-rope material branch.\",\"representative_source_ids\":[\"QS-102c675f\",\"QS-98ed4cca\",\"MH-dbd54505\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:5:surah-seal-material","source_type":"word_analysis","support_id":"sup_b70bb828f3f7203239be","text":"{\"blocking_evidence\":null,\"headline\":\"last word leaves tactile material\",\"reader_payoff\":\"The reader feels the three-beat narrowing end on rough material as the surah's final heard detail.\",\"reason\":\"The clause moves from {{ar:فِى جِيدِهَا}} ({{tr:fī jīdihā}}), to {{ar:حَبْلٌ}} ({{tr:ḥablun}}), to {{ar:مِّن مَسَدٍ}} ({{tr:min masadin}}), and the final noun is also the surah's naming material.\",\"representative_source_ids\":[\"QT-34cecf53\",\"QT-6ac14c4b\",\"QT-a05058e7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:3:small-distribution-range","source_type":"word_analysis","support_id":"sup_d134f2547519ea810899","text":"{\"blocking_evidence\":null,\"headline\":\"small occurrence set spans concrete and abstract\",\"reader_payoff\":\"The reader notices that the local physical rope sits at one edge of a small distribution that also includes abstract bonds and illusory ropes.\",\"reason\":\"The contextual profile gives five instances for the root, while V4 branches explain why the local material phrase selects physical rope rather than illusion or covenant as the governing sense.\",\"representative_source_ids\":[\"QS-6a8f35bd\",\"QI-408f2aae\",\"QI-c489422e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:3:staged-reveal","source_type":"word_analysis","support_id":"sup_d530df3b5c15f35bba11","text":"{\"blocking_evidence\":null,\"headline\":\"rope arrives after the neck\",\"reader_payoff\":\"The reader experiences the rope as the reveal that answers an already established neck-location.\",\"reason\":\"Both the delayed-subject analysis and any translation-level existential supply preserve {{ar:فِى جِيدِهَا}} ({{tr:fī jīdihā}}) as the fronted scene-setting pivot.\",\"representative_source_ids\":[\"QT-937acc46\",\"QY-3c08bdcc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:3:materially-specified-rope","source_type":"word_analysis","support_id":"sup_d62dbc0d779c15c39e53","text":"{\"blocking_evidence\":null,\"headline\":\"material phrase fixes the rope\",\"reader_payoff\":\"The reader notices that the rope is not materially open; the next phrase immediately defines what kind of rope it is.\",\"reason\":\"Attachment evidence links {{ar:مَسَدٍ}} ({{tr:masadin}}) to {{ar:حَبْلٌ}} ({{tr:ḥablun}}) through material-specifying {{ar:مِّن}} ({{tr:min}}).\",\"representative_source_ids\":[\"QG-0b487493\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:2:rare-neck-choice","source_type":"word_analysis","support_id":"sup_d717681bbeab05d7b842","text":"{\"blocking_evidence\":null,\"headline\":\"hapax profile marks the choice\",\"reader_payoff\":\"The reader notices that the neck term is not normalized by repeated Quranic contexts; its single occurrence makes the chosen register stand out.\",\"reason\":\"The contextual profile lists only one occurrence for the {{ar:ج ي د}} ({{tr:j-y-d}}) noun here, matching the CRITICAL hapax claim.\",\"representative_source_ids\":[\"QI-83069d1d\",\"QH-0bcc986d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:5:indefinite-rough-material","source_type":"word_analysis","support_id":"sup_d76fc1b693336c80ace6","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite material closes as texture\",\"reader_payoff\":\"The reader notices that the phrase specifies rough substance while withholding a named or possessed object identity.\",\"reason\":\"Both {{ar:حَبْلٌ}} ({{tr:ḥablun}}) and {{ar:مَسَدٍ}} ({{tr:masadin}}) are indefinite, and the final noun is singular genitive after {{ar:مِّن}} ({{tr:min}}).\",\"representative_source_ids\":[\"QG-e3e0b678\",\"QF-e1ee8d33\",\"QF-e3233471\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:3","source_type":"word_analysis","support_id":"sup_dcca9a8406d4d5859613","text":"{\"gloss_range\":\"an indefinite rope as delayed subject of the nominal clause, materially specified by the following phrase and locally functioning as constricting binding\",\"prose\":\"{{ar:حَبْلٌ}} ({{tr:ḥablun}}) is the delayed subject that answers the already fixed location {{ar:فِى جِيدِهَا}} ({{tr:fī jīdihā}}). Its indefiniteness makes the object arrive as one unspecific binding instrument, not a named or familiar rope, and the nominal clause presents it as a settled condition rather than an action of tying. The following {{ar:مِّن مَسَدٍ}} ({{tr:min masadin}}) selects the physical rope branch and makes the material part of its identity. Wider root pressure survives in narrowed form: the word can mean cord, bond, covenant, anatomical cord, or snare, but here those ranges are pulled into constricting binding, with notable contrasts to covenant-rope contexts (3:103, 3:112), magicians' ropes (20:66, 26:44), and the jugular cord (50:16). The boundary also turns the prior carrier role of 111:4 into being bound, while the rough onset of the rope-word and its tanwīn pairing with the final material noun make the rope and fiber sound like a joined unit.\",\"root_display\":\"{{ar:ح ب ل}} ({{tr:ḥ-b-l}})\",\"root_gloss_range\":\"rope, cord, bond, covenant, connection, anatomical cord, snare, and other extended-line branches; the local phrase selects the physical rope while retaining narrowed bond and occurrence-spectrum pressure\",\"surface_display\":\"{{ar:حَبْلٌ}} ({{tr:ḥablun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:1","source_type":"word_analysis","support_id":"sup_de81961b891a13e83219","text":"{\"gloss_range\":\"locative preposition governing the possessed neck phrase, with containment or encirclement force rather than simple surface placement\",\"prose\":\"{{ar:فِى}} ({{tr:fī}}) opens the ayah by making the neck-space the first thing heard. It governs {{ar:جِيدِهَا}} ({{tr:jīdihā}}) and frames the rope as in or around that site, not merely resting on it. The attachment evidence keeps {{ar:فِى جِيدِهَا}} ({{tr:fī jīdihā}}) as the fronted predicate of the delayed {{ar:حَبْلٌ}} ({{tr:ḥablun}}), so any boundary pressure from the previous ayah is narrowed to continuity, not a competing parse. The long opening vowel also lets the locative phrase stretch before the heavier rope-word arrives.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فِى}} ({{tr:fī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:3:indefinite-binding-instrument","source_type":"word_analysis","support_id":"sup_dfa87f7133a73cff2eb1","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite rope withholds identity\",\"reader_payoff\":\"The reader notices that the word gives one unspecific binding instrument and lets the object itself carry the tying action.\",\"reason\":\"QAC marks {{ar:حَبْلٌ}} ({{tr:ḥablun}}) as singular indefinite and nominative, and the verbless clause lets the instrument noun carry binding force without a separate verb.\",\"representative_source_ids\":[\"QG-f3328d1c\",\"QF-bd88752d\",\"QF-b1562a6e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:3:bond-field-narrowed-to-restraint","source_type":"word_analysis","support_id":"sup_e0966f3318d68354d818","text":"{\"blocking_evidence\":null,\"headline\":\"connection range becomes constriction\",\"reader_payoff\":\"The reader notices that a root field capable of connection or bond is locally tightened into restraint around the neck.\",\"reason\":\"V4 supports rope, bond, covenant, cord, and snare branches for {{ar:ح ب ل}} ({{tr:ḥ-b-l}}), but {{ar:مِّن مَسَدٍ}} ({{tr:min masadin}}) and the neck placement select the physical constricting rope here.\",\"representative_source_ids\":[\"QS-1f2f1f45\",\"QS-5bf4adab\",\"QS-cd13194a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:2:excellence-overlap-narrowed","source_type":"word_analysis","support_id":"sup_ecde4663f58461643079","text":"{\"blocking_evidence\":null,\"headline\":\"fineness pressure stays lexical-adjacent\",\"reader_payoff\":\"The reader notices a faint fineness or excellence pressure around the chosen neck word, but it does not replace the body-part sense.\",\"reason\":\"The supplied guardrail evidence for {{ar:ج ي د}} ({{tr:j-y-d}}) supports the neck branch; any excellence overlap remains an adjacent lexical pressure, especially because the row itself allows separate-root treatment.\",\"representative_source_ids\":[\"QS-fe95c8a9\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:3:covenant-form-contrast","source_type":"word_analysis","support_id":"sup_f0b1b5b31879d83d4be7","text":"{\"blocking_evidence\":null,\"headline\":\"free indefinite form differs from covenant formula\",\"reader_payoff\":\"The reader notices that this is not the definite covenant-rope formula of 3:103, but an indefinite rope later specified only by material.\",\"reason\":\"{{ar:حَبْلٌ}} ({{tr:ḥablun}}) is indefinite and free here, not an iḍāfa like {{ar:حَبْلِ ٱللَّهِ}} ({{tr:ḥabli llāh}}) in 3:103.\",\"representative_source_ids\":[\"QF-973c8159\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:5:hapax-title-closure","source_type":"word_analysis","support_id":"sup_f0dab67679c602c53579","text":"{\"blocking_evidence\":null,\"headline\":\"final hapax becomes the surah label\",\"reader_payoff\":\"The reader notices that the surah closes on a unique material word that also becomes its identifying label.\",\"reason\":\"The contextual evidence marks {{ar:م س د}} ({{tr:m-s-d}}) as a single occurrence, and QAC notes that the surah takes its name from {{ar:مَسَدٍ}} ({{tr:masadin}}).\",\"representative_source_ids\":[\"QI-363822ba\",\"QI-f301413e\",\"QH-f996ce19\",\"QY-a28227f6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:2:adornment-neck-reversal","source_type":"word_analysis","support_id":"sup_f9c6102222ef3aa4907d","text":"{\"blocking_evidence\":null,\"headline\":\"adornment site receives rough binding\",\"reader_payoff\":\"The reader notices the reversal: a necklace-bearing display site receives coarse binding fiber instead of ornament.\",\"reason\":\"QAC and V4 support {{ar:جِيد}} ({{tr:jīd}}) as the front of the neck, with lexical evidence for a fine or adornment-bearing neck; local syntax places {{ar:حَبْلٌ مِّن مَسَدٍ}} ({{tr:ḥablun min masadin}}) at that site.\",\"representative_source_ids\":[\"QS-72037ead\",\"QS-8f70f161\",\"QI-93494fae\",\"MH-7d0b0ba4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:5:5:predicate-layer-narrowed","source_type":"word_analysis","support_id":"sup_fef53f58f7f2affc9015","text":"{\"blocking_evidence\":null,\"headline\":\"load-bearing role stays inside material phrase\",\"reader_payoff\":\"The reader notices that the final material noun is syntactically load-bearing, while local attachment keeps it inside the material complement rather than an independent predicate.\",\"reason\":\"The row's secondary-predicate possibility is narrowed because the attachment guardrail specifically governs {{ar:مَسَدٍ}} ({{tr:masadin}}) by {{ar:مِّن}} ({{tr:min}}) as the material complement of {{ar:حَبْلٌ}} ({{tr:ḥablun}}).\",\"representative_source_ids\":[\"QG-157370a6\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ","ayah_ref":"111:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000284/B001","root_000291/B001","root_001422/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000284","role":"Locates the mechanism on the exposed front neck, where a tether can redirect the whole body.","root":"ج ي د","source_ref":"111:5","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000291","role":"Supplies an extended cord that binds or leads, giving the neck object restraint and directional force.","root":"ح ب ل","source_ref":"111:5","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001422","role":"Supplies firmly twisted fibrous construction, making the restraint durable under tension.","root":"م س د","source_ref":"111:5","source_word_indices":["5"]}],"changed_reading":{"after":"A deliberately constructed halter occupies the bodily point from which a person can be bound, led, and denied self-direction.","before":"A rope happens to be worn at her neck."},"confidence":"strong","focus_anchor":"The locative construction puts a cord at the front neck and then specifies its masad construction.","mechanism":"A cord capable of binding and leading is fixed at the body's exposed steering point, while masad supplies a tightly twisted build. The three focus nouns compose a tension-bearing halter rather than an object merely resting near the neck.","model_id":"b01_neck_halter"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b01_neck_halter","source_type":"hft","support_id":"sup_619d8105a0e1cc83eb79","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ","ayah_ref":"111:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000284/B001","root_000291/B008","root_001422/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000284","role":"Provides the front neck as a conspicuous display site, including the lexical association with a fine or elongated neck.","root":"ج ي د","source_ref":"111:5","source_word_indices":["2"]},{"branch_id":"B008","mapped_root_id":"root_000291","role":"Activates a cord-derived ornament specifically placed among necklace elements.","root":"ح ب ل","source_ref":"111:5","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001422","role":"Replaces ornamental fineness with forcefully twisted palm, hair, or hide fiber.","root":"م س د","source_ref":"111:5","source_word_indices":["5"]}],"changed_reading":{"after":"The restraint is also an anti-necklace: the form and display position of adornment survive while its material and function turn punitive.","before":"The neck rope is only an instrument of restraint."},"confidence":"medium","focus_anchor":"The focus places a named cord-form at a neck, the ordinary display site of a necklace, but qualifies it with coarse twisted material.","mechanism":"The ornament branch of the cord root and the neck's display associations establish a necklace slot; masad fills that slot with hard-twisted fiber. Adornment is not simply absent but structurally retained and materially reversed.","model_id":"b02_inverted_necklace"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b02_inverted_necklace","source_type":"hft","support_id":"sup_57e3c6af36af0c4bffed","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ","ayah_ref":"111:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000284/B001","root_000291/B002","root_001422/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000291","role":"Supplies covenant, protection, attachment, and means of access as a second functional register for the cord.","root":"ح ب ل","source_ref":"111:5","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000284","role":"Turns an abstract bond into something borne visibly at a vulnerable bodily site.","root":"ج ي د","source_ref":"111:5","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001422","role":"Gives multiple connective strands a single tightened and load-bearing form.","root":"م س د","source_ref":"111:5","source_word_indices":["5"]}],"changed_reading":{"after":"It can simultaneously stage a bond of protection or affiliation whose very closeness has inverted into bodily liability.","before":"The verse describes only a physical cord."},"confidence":"medium","focus_anchor":"The same focus word that denotes a material cord can denote covenant, protection, attachment, or a means of access, and it is fixed at her neck.","mechanism":"A bond normally providing connection or security becomes inseparable from the bearer and changes polarity into encumbrance. Masad's twisting gives the social bond a material image: separate ties become one constricting liability.","model_id":"b03_protection_inverted"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b03_protection_inverted","source_type":"hft","support_id":"sup_0c0f822a5ee347126fb0","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ","ayah_ref":"111:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000284/B001","root_000291/B005","root_000291/B011","root_001422/B001"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000291","role":"Supplies a catching and entangling trap, converting the cord into an event of capture.","root":"ح ب ل","source_ref":"111:5","source_word_indices":["3"]},{"branch_id":"B011","mapped_root_id":"root_000291","role":"Adds calamity or cunning that catches its own subject, making entanglement consequential rather than accidental.","root":"ح ب ل","source_ref":"111:5","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000284","role":"Marks the neck as the point at which capture has become bodily control.","root":"ج ي د","source_ref":"111:5","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001422","role":"Supplies torsion and tensile coherence, allowing the trap to close rather than fall apart.","root":"م س د","source_ref":"111:5","source_word_indices":["5"]}],"changed_reading":{"after":"The rope is itself the closing trap, with the focus presenting the instant of entanglement as a settled bodily condition.","before":"The rope is a static punishment imposed after capture."},"confidence":"medium","focus_anchor":"The cord root carries both hunting-snare and ensnaring-calamity branches, while the focus fixes the result around the neck.","mechanism":"The cord is an active capture system rather than passive equipment. The neck location shows the trap already closed, and the twisted material suggests tightening under struggle.","model_id":"b04_snare_that_closes"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b04_snare_that_closes","source_type":"hft","support_id":"sup_500faf58bc2cb81867aa","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ","ayah_ref":"111:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000284/B001","root_000291/B004","root_001422/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000284","role":"Provides the anatomical site at which external tether and internal bodily structures can meet.","root":"ج ي د","source_ref":"111:5","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_000291","role":"Supplies vein-like, sinew-like, and joint-like cords inside the body.","root":"ح ب ل","source_ref":"111:5","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001422","role":"Supplies a human body understood as tightly formed or corded, extending twist from material to physique.","root":"م س د","source_ref":"111:5","source_word_indices":["5"]}],"changed_reading":{"after":"The body itself is rendered cord-like, so that the imposed constraint seems to invade and reorganize embodiment.","before":"A foreign object is attached to an otherwise separate body."},"confidence":"exploratory","focus_anchor":"At the neck, the cord root can name bodily veins and sinews, while masad can describe a compactly twisted human form.","mechanism":"External rope and bodily cord become analogues. The restraint does not merely touch the body; its corded structure echoes the body's own connective tissues and tightly formed shape, making captivity appear incorporated.","model_id":"b05_constraint_embodied"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b05_constraint_embodied","source_type":"hft","support_id":"sup_908f195f4a0af0b20175","trust":"legacy_unbound"}]}
</lane_packet_json>
