# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **111:2**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s111-regular-20260911/s111/111_2/micro.discovery.json` and modify nothing
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
  "ayah_ref": "111:2",
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
{"analysis_context":{"analysis_id":"s111-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"111:2","host_surah":111,"lane_context_refs":[],"ordered_context_refs":["111:0","111:1","111:3","111:4","111:5","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, başkasının ihtiyacını karşılamayı, sesle ezgi söylemeyi veya bir yerde kalmayı değil, varlıklı ve ihtiyaçtan bağımsız olmayı anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001110/B001","candidate_links":[{"candidate_id":"cand_83db1874cff5e496c72e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَغْنَىٰ","morph_features":"STEM|POS:V|PERF|LEM:>agonaY`|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"111:2:2:1","qac_word_ref":"111:2:2","surface_ar":"أَغْنَىٰ"}],"gloss":"maddi bolluk ve ihtiyaçtan bağımsızlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Maddi varlık, bolluk ve çok sayıda mala sahip olma durumunu kapsar."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İhtiyaçların bulunmaması ya da az olması, maddi bollukla birlikte çekirdeğin bir parçasıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir şeyle yetinerek veya bir şeye gerek duymayarak ihtiyaçtan bağımsız hale gelme, bağıntılı yapılarda gerçekleşir."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Maddi varlık ile ihtiyaç duymama çekirdeğini birlikte anlatan genel kavram karşılığıdır.","boundary_detail":"Dal, başkasının ihtiyacını karşılamayı, sesle ezgi söylemeyi veya bir yerde kalmayı değil, varlıklı ve ihtiyaçtan bağımsız olmayı anlatır.","branch_image_ar":"الغنى والاستغناء","concept_gloss":"maddi bolluk ve ihtiyaçtan bağımsızlık","contextual_glosses":[{"applicability":"Bağlam yalnızca para, mal ve maddi bolluk durumunu öne çıkardığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İhtiyaç duymama ile bir şey sayesinde yetinme ilişkisini tek başına açıkça vermez.","preserves":"Maddi varlık ve bolluk yönünü doğal biçimde korur."},"facet_ids":["F001"],"text":"zenginlik","usage_role":"contextual"},{"applicability":"Kişinin bir şeye ihtiyaç duymaması veya elindekiyle yetinmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Maddi servet ve çok sayıda mala sahip olma yönünü zorunlu olarak taşımaz.","preserves":"İhtiyaçtan bağımsızlık ve bir şeyle yetinme yönünü korur."},"facet_ids":["F002","F003"],"text":"kendine yetmek","usage_role":"contextual"}],"definition":"Maddi varlığa ve bolluğa sahip olma, ihtiyaç duymama ya da az ihtiyaç duyma durumudur. Bağıntılı kullanımlarda kişi bir şey sayesinde yetinir veya başka bir şeye gerek duymaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Maddi varlık, bolluk ve çok sayıda mala sahip olma durumunu kapsar."},{"facet_id":"F002","role":"core","statement":"İhtiyaçların bulunmaması ya da az olması, maddi bollukla birlikte çekirdeğin bir parçasıdır."},{"facet_id":"F003","role":"extension","statement":"Bir şeyle yetinerek veya bir şeye gerek duymayarak ihtiyaçtan bağımsız hale gelme, bağıntılı yapılarda gerçekleşir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İhtiyaç duymama ve bir şeyle yetinme yönlerini karşılamaz.","preserves":"Maddi mala ve bolluğa sahip olma yönünü korur."},"text":"varlıklılık"},{"category":"confusable","error_profile":{"adds":"Bir şeyin başkası için yeterli olma işlevini çağrıştırır.","collision":"Başkası için yeterli olma dalıyla karışır.","fit":"displacement","loses":"Maddi bolluk ve kişinin ihtiyaçtan bağımsız olma durumunu silikleştirir.","preserves":"İhtiyacın karşılanmış olmasıyla ilgili sınırlı bir yakınlığı korur."},"text":"yeterlilik"}],"identity_rationale":"Kaynak sözü, maddi varlık ve bolluğun yanı sıra ihtiyaç duymama ya da az ihtiyaç duyma durumunu açıkça birlikte verir. Bir şey sayesinde yetinme ve bir şeye gerek duymama anlatımları da bu çekirdeğin bağıntılı kullanımlarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"maddi zenginlik, bolluk ve ihtiyaçsızlık"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"varlıklı, zengin"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"zenginleşmek veya başkasına ihtiyaç duymayacak duruma gelmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ona ihtiyaç duymamak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"onunla yetinip başka bir şeye ihtiyaç duymamak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bir şeye ihtiyaç duymama durumu"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"zenginlik ve bolluk"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"gönül tokluğu ve az şeye ihtiyaç duyma"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"zengin etmek veya yoksunluğunu gidermek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"Kur'an'la yetinip başka bir şeye ihtiyaç duymamak"}],"lexicalization_note":"Yalın biçimler maddi bolluk ve ihtiyaçsızlık durumunu adlandırırken bağıntılı yapılar bir şeyle yetinmeyi veya bir şeye gerek duymamayı belirtir; bu iki kapsam tanımda ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; maddi bolluk, yeterlik ve sonradan zenginleşme sınırlarını en açık gösteren dört karşılaştırma seçildi, yalnızca dar örnek veya uzak alan ortaklığı sunanlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bir sahibin varlık ve ihtiyaçsızlık durumunu anlatır; komşu dal ise bir unsurun başka biri için yeterli olma ve onun işini görme ilişkisini anlatır.","focus_only":"Kişinin maddi bolluğu ve kendisinin ihtiyaçtan bağımsız oluşu bu dala özgüdür.","gloss":"kendine yeterlik ve başkasına yetme","neighbor_only":"Bir şeyin veya kişinin başkası için yeterli olması, yarar sağlaması ve onun yerini tutması komşuya özgüdür.","neighbor_ref":"root_001110/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir ihtiyacın ortadan kalkması veya karşılanması çevresinde buluşur."},{"boundary_match":"partial","distinction":"Komşu dal genişlik ve refahı öne çıkarırken odak dal bunu ihtiyaçların yokluğu veya azalması ve bağımsızlıkla daha sıkı bağlar.","focus_only":"Az ihtiyaç duyma, çok mala sahip olma ve bir şeyle yetinme bağıntıları odakta açıkça yer alır.","gloss":"bolluk ve refah","neighbor_only":"Genel genişlik ve ferahlık anlatımı komşu dalda daha belirgindir.","neighbor_ref":"root_001694/B003","relation_type":"near_synonym","shared_zone":"İki dal da maddi genişlik, refah ve yoksunluktan çıkma durumunu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal zenginliği ihtiyaçtan bağımsızlıkla tanımlar; komşu dal ise birikmiş malın veya başka şeylerin çokluğuna kadar genişleyebilir.","focus_only":"İhtiyaç duymama veya bir şeyle yetinme odak dalın kurucu sınırıdır.","gloss":"zenginlik ve mal çokluğu","neighbor_only":"Her tür çokluk ve malı iyi yönetme anlatımı komşu dalın ek kapsamıdır.","neighbor_ref":"root_000459/B001","relation_type":"near_synonym","shared_zone":"Her iki dal maddi varlığın çokluğunu ve zenginliği anlatır."},{"boundary_match":"partial","distinction":"Odak dal genel ve sürebilen bir zenginlik durumudur; komşu dal aynı sonucu özellikle önceki yoksulluktan sonraki değişim olarak sınırlar.","focus_only":"Öncesinde yoksulluk bulunması gerekmeksizin varlıklı ve ihtiyaçsız olmayı kapsar.","gloss":"zenginlik ve sonradan zenginleşme","neighbor_only":"Yoksulluktan sonra zenginleşme geçişi komşu dalın zorunlu koşuludur.","neighbor_ref":"root_000406/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin zengin duruma gelmesini veya zengin olmasını içerir."}],"source_phrase_ar":"الغنى في المال (maqayis;tahdhib)؛ الغنى مقصور في المال واستغنى الرجل أصاب غنى (ayn;tahdhib)؛ الغنى مقصور اليسار وتغنى الرجل أي استغنى (sihah)؛ الغني ذو الوفر (ayn;tahdhib)؛ عدم الحاجات وقلة الحاجات وكثرة القنيات (mufradat)؛ تغنيت وتغانيت بمعنى استغنيت (maqayis;tahdhib)","source_summary":"Kaynakların ortak çerçevesi maddi zenginliği, bolluğu ve ihtiyaçların yokluğunu ya da azalmasını bir araya getirir; ayrıca bir şeyle yetinip başkasına ihtiyaç duymama kullanımını destekler.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الغنى في المال والوفر وعدم الحاجة أو قلتها وكثرة القنيات والاستغناء بالشيء أو عنه وتغنى وتغانى بمعنى استغنى","what_is_not_ar":"ليس إجزاء الشيء عن غيره ولا الغناء بالصوت ولا المقام بالمكان"},"support_links":["sup_4f00fbc02ad26fa8a71d"]},{"boundary":"Dal, kendisi ihtiyaçsız olma durumundan ayrılır; burada bir unsur başka biri için yeterli olur, onun ihtiyacını karşılar veya yerini doldurur.","branch_kind":"mixed_non_bare","branch_ref":"root_001110/B002","candidate_links":[{"candidate_id":"cand_5d7bed8ee6cb087f5c69","lane":"micro"},{"candidate_id":"cand_1aed28b6ee13f6e80f94","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَغْنَىٰ","morph_features":"STEM|POS:V|PERF|LEM:>agonaY`|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"111:2:2:1","qac_word_ref":"111:2:2","surface_ar":"أَغْنَىٰ"}],"gloss":"ihtiyacı karşılayıp yarar sağlama ve yerini tutma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir unsur, başka bir kişi veya durum için yeterli olur ve ihtiyacı karşılar."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yeterli olan unsur yarar sağlar ve beklenen işlevi yerine getirir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bağıntılı kullanımlarda bir kişi veya şey, başka birinin ya da şeyin yerini tutar."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir unsurun başkası için hem yeterli hem yararlı olması ve gerektiğinde başka bir unsurun işlevini üstlenmesi için kullanılır.","boundary_detail":"Dal, kendisi ihtiyaçsız olma durumundan ayrılır; burada bir unsur başka biri için yeterli olur, onun ihtiyacını karşılar veya yerini doldurur.","branch_image_ar":"الغَناء والكفاية","concept_gloss":"ihtiyacı karşılayıp yarar sağlama ve yerini tutma","contextual_glosses":[{"applicability":"Bir şeyin miktar veya işlev bakımından ihtiyacı karşılaması öne çıktığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yarar sağlama ve başka bir unsurun yerini tutma yönlerini açıkça belirtmez.","preserves":"Yeterli olma ve ihtiyacı karşılama çekirdeğini korur."},"facet_ids":["F001"],"text":"yetmek","usage_role":"contextual"},{"applicability":"Bir unsurun beklenen yararı sağlaması veya başka bir unsur yerine kullanılabilmesi bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel yeterlik ile ihtiyacın bütünüyle karşılanmasını zorunlu olarak anlatmaz.","preserves":"Yarar sağlama ve beklenen işlevi yerine getirme yönünü korur."},"facet_ids":["F002","F003"],"text":"işini görmek","usage_role":"contextual"}],"definition":"Bir şeyin ya da kişinin başkası için yeterli olması, onun ihtiyacını karşılaması ve yarar sağlamasıdır; bağlama göre başka bir unsurun işini görüp onun yerini de tutabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir unsur, başka bir kişi veya durum için yeterli olur ve ihtiyacı karşılar."},{"facet_id":"F002","role":"core","statement":"Yeterli olan unsur yarar sağlar ve beklenen işlevi yerine getirir."},{"facet_id":"F003","role":"extension","statement":"Bağıntılı kullanımlarda bir kişi veya şey, başka birinin ya da şeyin yerini tutar."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yeterli olma, ihtiyacı karşılama ve başkasının yerini tutma ilişkilerini vermez.","preserves":"Olumlu sonuç ve işe yarama yönünü korur."},"text":"yarar"},{"category":"confusable","error_profile":{"adds":null,"collision":"Genel değiştirme ve takas alanıyla karışabilir.","fit":"narrowing","loses":"Yer değiştirme bulunmayan yeterlik ve yarar kullanımlarını dışarıda bırakır.","preserves":"Bir unsurun başka bir unsurun işlevini üstlenmesi yönünü korur."},"text":"yerine geçme"}],"identity_rationale":"Kaynak sözü, bir şeyin ya da kişinin başkası için yeterli olmasını, ihtiyacı karşılamasını, yarar sağlamasını ve gerektiğinde başka bir unsurun yerini tutmasını birlikte verir. Bu nedenle dalın çekirdeği, sahibin zenginliği değil, iki katılımcı arasındaki yeterlik ilişkisidir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yeterlilik, ihtiyacı karşılama ve yarar"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"onun yerine yetmek, ihtiyacını karşılamak ve yarar sağlamak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bu sana yetmez ve yarar sağlamaz"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yeterli ve ihtiyacı karşılayan"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"birinin yerini tutan yeterlilik ve işlev"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"zararını benden uzak tut"}],"lexicalization_note":"Yalın biçimler yeterlik ve yararı adlandırır; bağıntılı yapılar kimin için yeterli olunduğunu, neyin yerini tuttuğunu veya hangi zararın uzak tutulduğunu açıklar.","neighbor_coverage_note":"Bütün adaylar incelendi; genel yeterlik, bir şeyle yetinme, başkası adına iş görme ve gerçek değiştirme arasındaki sınırları gösteren dört aday seçildi, daha uzak alan ortaklıkları elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bir unsurun başkası için yeterli ve yararlı oluşuna dayanır; komşu dal ise işi üstlenip sürdürerek açığı kapatma ve sonuca ulaştırma sürecini öne çıkarır.","focus_only":"Yarar sağlama ve bir kişi ya da şeyin yerini tutma ilişkileri odakta açıkça bulunur.","gloss":"yetme ve işi tamamlayarak yetme","neighbor_only":"Bir işi yürütüp açığı kapatarak amaca ulaşma süreci komşu dalda daha belirgindir.","neighbor_ref":"root_001310/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bir ihtiyacın karşılanması ve yeterli sonucun elde edilmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal genel yeterlik ve yararı da içerir; komşu dal yerini tutma ve özellikle bir yükümlülüğü başkası adına yerine getirme ilişkisine daha sıkı bağlıdır.","focus_only":"Bir şeyin yalnızca yeterli veya yararlı olması, yer değiştirme gerçekleşmeden de bu dala girebilir.","gloss":"yetme ve başkasının yerine ödeme","neighbor_only":"Hak, borç veya bağış gibi yükümlülükleri başkası adına yerine getirme komşu dalın ek alanıdır.","neighbor_ref":"root_000244/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir unsurun başka birinin yerini tutup onun adına yeterli olmasını kapsar."},{"boundary_match":"partial","distinction":"Odak dal yeterli unsur ile yararlanan katılımcı arasındaki ilişkiyi kurar; komşu dal eldeki şeyle yetinme ve başkasından vazgeçebilme sonucunu öne çıkarır.","focus_only":"Bir kişinin ya da şeyin başkası için yararlı ve yeterli olup onun yerini tutması odakta belirgindir.","gloss":"ihtiyacı karşılama ve bir şeyle yetinme","neighbor_only":"Bir şeyle yetinip başka bir şeye gerek duymama sonucu komşu dalda çekirdeğe daha yakındır.","neighbor_ref":"root_000241/B001","relation_type":"near_synonym","shared_zone":"Her iki dal, eldeki bir unsurun ihtiyacı karşılayarak başka bir gereği ortadan kaldırmasını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal işlev bakımından yetmeyi anlatır; komşu dal ise bir unsurun yerine diğerini koyma veya onları değiştirme işlemini anlatır.","focus_only":"Yeterli olma ve yarar sağlama, gerçek bir değiştirme işlemi olmadan da gerçekleşebilir.","gloss":"işlevsel yeterlik ve değiştirme","neighbor_only":"Bir unsurun çıkarılıp yerine başka bir unsurun konması ve karşılıklı değiştirme komşu dala özgüdür.","neighbor_ref":"root_000095/B001","relation_type":"near_neighbor","shared_zone":"Bir unsurun başka bir unsurun konumunu veya işlevini üstlenmesi iki dalda da görülebilir."}],"source_phrase_ar":"الغناء بالفتح الكفاية ولا يغني أي لا يكفي (maqayis)؛ الغناء الاستغناء والكفاية ورجل مغن أي مجزئ (ayn)؛ ما يغني عنك هذا أي ما يجزئ وما ينفع والغناء بالفتح النفع (sihah)؛ الإجزاء والكفاية ورجل مغن أي مجزئ كاف (tahdhib)؛ أغناني كذا وأغنى عنه كذا إذا كفاه (mufradat)","source_summary":"Kaynaklar yeterli olma, ihtiyacı karşılama, yarar sağlama ve başkasının yerini tutma yönlerinde birleşir; olumsuz yapılarda aynı ilişki yetersizlik veya yararsızlık olarak görünür.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه أن يكفي الشيء أو الشخص غيره ويجزئ عنه وينفعه ويقوم مقامه","what_is_not_ar":"ليس اليسار والوفر ولا الغناء بالصوت ولا سكنى المكان"},"support_links":["sup_8af5d3e738e6144d04c0","sup_c7fb5e5f2013ea90882e"]},{"boundary":"Çekirdek sesle ezgi üretme ve dinleme alanıdır; okuyuştaki duygulu seslendirme özel kullanımdır, maddi zenginlik ve yeterlik bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001110/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَغْنَىٰ","morph_features":"STEM|POS:V|PERF|LEM:>agonaY`|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"111:2:2:1","qac_word_ref":"111:2:2","surface_ar":"أَغْنَىٰ"}],"gloss":"sesle ezgi söyleme, dinleme ve ezgili okuma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan sesiyle ezgi söyleme ve bu seslendirmeyi dinleme çekirdeği oluşturur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ezgili biçimde söylenen tek bir parça, bu ses etkinliğinin ürünüdür."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir metni ezgili, hüzünlü ve yumuşak sesle okumak, seslendirme çekirdeğinin özel kullanımıdır."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın ses üretme, dinleme ve özel metin okuma yönlerini birlikte gösteren açıklayıcı karşılıktır.","boundary_detail":"Çekirdek sesle ezgi üretme ve dinleme alanıdır; okuyuştaki duygulu seslendirme özel kullanımdır, maddi zenginlik ve yeterlik bu dala girmez.","branch_image_ar":"الغِناء والصوت","concept_gloss":"sesle ezgi söyleme, dinleme ve ezgili okuma","contextual_glosses":[{"applicability":"İnsan sesiyle ezgili bir parça seslendirme eylemi anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dinleme ile metni hüzünlü ve yumuşak sesle okuma yönlerini dışarıda bırakır.","preserves":"Sesle ezgi üretme ve ezgili parça yönlerini korur."},"facet_ids":["F001","F002"],"text":"şarkı söylemek","usage_role":"contextual"},{"applicability":"Bir metnin sesi yumuşatıp duygulandırarak ezgili biçimde okunması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel şarkı söyleme, ezgili parça ve dinleme alanlarını kapsamaz.","preserves":"Okuyuşta ezgi, hüzün ve ses yumuşaklığı yönünü korur."},"facet_ids":["F003"],"text":"ezgili okumak","usage_role":"contextual"}],"definition":"Sesle ezgi söyleme, söylenen ezgili parça ve bunu dinleme alanıdır. Okuyuşu ezgili, hüzünlü ve yumuşak bir sesle gerçekleştirme bunun özel bir uygulamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan sesiyle ezgi söyleme ve bu seslendirmeyi dinleme çekirdeği oluşturur."},{"facet_id":"F002","role":"extension","statement":"Ezgili biçimde söylenen tek bir parça, bu ses etkinliğinin ürünüdür."},{"facet_id":"F003","role":"specialization","statement":"Bir metni ezgili, hüzünlü ve yumuşak sesle okumak, seslendirme çekirdeğinin özel kullanımıdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"İnsan sesi bulunmayan çalgısal üretim ve düzenleme alanlarını da kapsar.","collision":"Çalgı müziğiyle gereksiz bir kapsam çakışması doğurur.","fit":"broadening","loses":null,"preserves":"Ezgi ve işitsel sanat alanıyla olan bağı korur."},"text":"müzik"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Söyleme ve dinleme etkinliğiyle özel ezgili okuma kullanımını tek başına karşılamaz.","preserves":"Ezgili söylenen parça yönünü güçlü biçimde korur."},"text":"şarkı"}],"identity_rationale":"Kaynak sözü sesle ezgi söylemeyi, söylenen ezgili parçayı ve dinlemeyi açıkça bu dalda toplar. Okuyuşu ezgili, hüzünlü ve yumuşak seslendirme ise aynı ses kullanımının özel bir uygulamasıdır, dalın bütününü tek başına tanımlamaz.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"şarkı söyleme, ezgili seslendirme ve dinleti"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"şarkı; ezgili söylenen parça"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"şarkı söylemek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"şarkı söylemek veya sesi ezgili ve duygulu kullanmak"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"Kur'an'ı hüzünlü, yumuşak ve ezgili bir sesle okumak"}],"lexicalization_note":"Yalın biçimler şarkı söyleme, ezgili parça ve dinletiyi adlandırır; belirli metni ezgili okuma anlamı yalnızca ilgili bağıntılı yapıya bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hoş insan sesi, özel yolcu ezgisi, ses yineleme ve çalgı sesiyle sınırı en iyi gösteren dört aday seçildi, yalnızca yüksek ses veya uzak konu ortaklığı sunanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal şarkı söyleme, parça, dinleme ve özel okuma kullanımını toplar; komşu dal özellikle hoş işitilen ses niteliği ve bunu üreten kişiye yönelir.","focus_only":"Ezgili parça ile metni hüzünlü ve yumuşak sesle okuma kullanımı odakta açıkça bulunur.","gloss":"şarkı ve hoş ezgili ses","neighbor_only":"Sesin hoş ve zevk verici niteliği ile icracıyı adlandırma komşu dalda daha belirgindir.","neighbor_ref":"root_000741/B007","relation_type":"near_synonym","shared_zone":"İki dal da insan sesiyle üretilen hoş ezgiyi ve şarkı söylemeyi kapsar."},{"boundary_match":"partial","distinction":"Odak dal geniş sesli ezgi alanını anlatır; komşu dal bunu yüksek sesli ve yolculukla ilişkili belirli bir söyleyiş türüyle sınırlar.","focus_only":"Genel şarkı söyleme, ezgili parça, dinleme ve yumuşak okuyuş odak dalda yer alır.","gloss":"genel şarkı ve yolcu ezgisi","neighbor_only":"Yolcuların yüksek sesle söylediği çağrı ve belirli ezgi türü komşuya özgüdür.","neighbor_ref":"root_001507/B009","relation_type":"near_neighbor","shared_zone":"Her iki dal insan sesiyle ezgili söyleme etkinliğine girer."},{"boundary_match":"partial","distinction":"Odak dal ezgi üretimi ve dinlemeyi tanımlar; komşu dal sesin yinelenmesi veya geri döndürülmesi biçimine dayanır ve ezgi gerektirmez.","focus_only":"Ezgili parça ve şarkı söyleme etkinliği odak dalın merkezindedir.","gloss":"ezgili söyleme ve ses yineleme","neighbor_only":"Çağrı, gök gürültüsü ve başka seslerde yineleme veya yankılanma komşu dalın ek kapsamıdır.","neighbor_ref":"root_000544/B007","relation_type":"near_neighbor","shared_zone":"Şarkı ve okuma sırasında sesin düzenli biçimde çevrilmesi iki dalda kesişebilir."},{"boundary_match":"field_only","distinction":"Odak dal insan sesi ve şarkıya dayanır; komşu dalın çekirdeği üflemeli çalgıdan çıkan sestir ve insan sesi zorunlu değildir.","focus_only":"İnsan sesiyle şarkı söyleme ve metni ezgili okuma odak dalın çekirdeğidir.","gloss":"insan sesi ve çalgı sesi","neighbor_only":"Üflemeli çalgıyla ses üretme ve aynı sözcüğün bazı hayvan seslerine uygulanması komşuya özgüdür.","neighbor_ref":"root_000643/B002","relation_type":"same_field","shared_zone":"İki dal ezgili veya hoş işitilebilen ses üretimi alanında buluşur."}],"source_phrase_ar":"الغناء من الصوت والأغنية اللون من الغناء (maqayis)؛ الغناء ممدود في الصوت وغنى يغني أغنية وغناء (ayn)؛ الأغنية الغناء والجمع الأغاني والغناء بالكسر من السماع (sihah)؛ الغناء الصوت ممدود والتطريب وتحزين القراءة وترقيقها (tahdhib)؛ غنى أغنية وغناء (mufradat)","source_summary":"Kaynaklar insan sesiyle ezgi söyleme, ezgili parça ve dinleme anlamlarında birleşir; ayrıca okuyuştaki ezgili, hüzünlü ve yumuşak seslendirmeyi özel bir kullanım olarak verir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الغناء بالصوت والأغنية والسماع والتطريب وتحزين القراءة وترقيقها","what_is_not_ar":"ليس الغنى في المال ولا الغَناء بمعنى الكفاية ولا المقام بالمكان"},"support_links":[]},{"boundary":"Dalın çekirdeği bir yerde oturmak ve uzun süre kalmaktır; geçmişte orada yaşamış olma ile ev ve yer adları buna bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001110/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَغْنَىٰ","morph_features":"STEM|POS:V|PERF|LEM:>agonaY`|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"111:2:2:1","qac_word_ref":"111:2:2","surface_ar":"أَغْنَىٰ"}],"gloss":"bir yerde uzun süre kalıp yaşama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi veya topluluk belirli bir yerde oturur ve orada uzun süre kalır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bağlama göre aynı alan, kişinin geçmişte o yerde yaşamış veya bulunmuş olmasını anlatır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir topluluğun oturduğu evler ile kalma eylemi veya kalınan yer bu çekirdekten adlandırılır."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yer, süre ve yaşama katılımlarını birlikte taşıyan genel kavram karşılığıdır.","boundary_detail":"Dalın çekirdeği bir yerde oturmak ve uzun süre kalmaktır; geçmişte orada yaşamış olma ile ev ve yer adları buna bağlıdır.","branch_image_ar":"الغنى بالمكان","concept_gloss":"bir yerde uzun süre kalıp yaşama","contextual_glosses":[{"applicability":"Bir kişi veya topluluğun belirli bir yeri yaşama yeri edinmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uzun süre kalma vurgusunu ve bundan doğan yer adlarını açıkça vermez.","preserves":"Belirli bir yerde yaşama ve yerle bağ kurma yönünü korur."},"facet_ids":["F001"],"text":"bir yerde oturmak","usage_role":"contextual"},{"applicability":"Kalınan yer ile kalış süresinin öne çıktığı cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Orada yaşama ile ev veya yer adı türetme yönlerini zorunlu olarak taşımaz.","preserves":"Belirli yerde kalma ve süreklilik yönünü korur."},"facet_ids":["F001"],"text":"uzun süre kalmak","usage_role":"contextual"},{"applicability":"Geçmişte bir yerde bulunmuş ve yaşamış olmanın sonradan yokluğu anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel uzun süre kalma çekirdeği ile konut ve eylem adlarını kapsamaz.","preserves":"Geçmişte o yerde yaşama veya bulunma yönünü korur."},"facet_ids":["F002"],"text":"orada yaşamış olmak","usage_role":"contextual"}],"definition":"Bir yerde oturmak, orada uzun süre kalmak ve yaşamak anlamıdır. Geçmişte orada bulunmuş olma anlatımı ile bir topluluğun oturduğu evleri, kalma eylemini veya kalınan yeri bildiren adlar bu çekirdeğe bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi veya topluluk belirli bir yerde oturur ve orada uzun süre kalır."},{"facet_id":"F002","role":"extension","statement":"Bağlama göre aynı alan, kişinin geçmişte o yerde yaşamış veya bulunmuş olmasını anlatır."},{"facet_id":"F003","role":"associated_use","statement":"Bir topluluğun oturduğu evler ile kalma eylemi veya kalınan yer bu çekirdekten adlandırılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uzun süreli oturma, yaşama ve o yerin ev sayılması yönlerini zayıflatır.","preserves":"Belirli bir yerde kalma yönünü korur."},"text":"konaklamak"},{"category":"alternative","error_profile":{"adds":"Başlangıçtaki taşınma ve kalıcı düzen kurma olayını öne çıkarır.","collision":"Yer edinme eylemiyle kalış durumunu birbirine yaklaştırır.","fit":"displacement","loses":"Geçmişte bulunmuş olma ve yalnızca uzun süre kalma kullanımlarını daraltır.","preserves":"Bir yeri yaşama yeri edinme yönünü korur."},"text":"yerleşmek"}],"identity_rationale":"Kaynak sözü bir yerde oturup uzun süre kalmayı çekirdek olarak verir; orada yaşamış veya bulunmuş olma anlatımı ile oturulan ev ve yer adları bu çekirdekten doğan kullanımlardır. Bu nedenle geçici bulunma ile konut adı aynı düzeyde tek anlam sayılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bir yerde oturmak ve uzun süre kalmak"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"sanki daha dün orada hiç yaşamamıştı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bir topluluğun oturduğu evler ve yurtlar"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"oturma eylemi veya oturulan yer"}],"lexicalization_note":"Bir yerde uzun kalma ve geçmişte orada yaşama anlamları belirli bağıntılı yapılarda görünür; yalın ad biçimleri ise kalma eylemini veya oturulan yeri gösterir.","neighbor_coverage_note":"Bütün adaylar incelendi; uzun kalış, genel kalma, konut edinme ve oturma duruşu arasındaki sınırı gösteren beş aday seçildi, yalnızca yer adı veya uzaktan alan ortaklığı sunanlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yaşama, geçmişte bulunma ve konut adlarına uzanır; komşu dal ise yerleşik kalmayı farklı kişi durumlarına ve özel kalış bağlamlarına genişletir.","focus_only":"Topluluğun evleri ile kalma eylemini veya yerini adlandıran biçimler odakta bulunur.","gloss":"uzun süre yaşama ve yerleşik kalma","neighbor_only":"Yabancının kalışı, kutsal yerde komşuluk, hapiste kalma ve öldürülmüş kişi kullanımları komşuya özgüdür.","neighbor_ref":"root_000211/B001","relation_type":"near_synonym","shared_zone":"İki dal da belirli bir yerde oturma, kalma ve özellikle uzun süren yerleşikliği anlatır."},{"boundary_match":"partial","distinction":"Odak dal uzun yaşama ile bundan doğan ev ve yer adlarını toplar; komşu dal aynı alanı durma, bekleme ve soyut yerleşiklik kullanımlarına taşır.","focus_only":"Geçmişte orada yaşamış olma ve topluluğun evlerini adlandırma odakta belirgindir.","gloss":"oturma ve yerleşik kalma","neighbor_only":"Durma, ağırdan alma ve eskiden beri yerleşmiş bir iş anlatımı komşu dalın ek kapsamıdır.","neighbor_ref":"root_000536/B006","relation_type":"near_synonym","shared_zone":"Her iki dal bir yerde oturma, ev ve yerleşik kalma alanında geniş ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal süreyi, yaşamayı ve bağlı yer adlarını içerir; komşu dal ise süre veya konut sonucu belirtmeden bir yerde kalma eylemiyle sınırlıdır.","focus_only":"Uzun süre yaşama, geçmişte bulunma ve oturulan evleri adlandırma odakta yer alır.","gloss":"uzun süre yaşama ve bir yerde kalma","neighbor_only":"Komşu dal yalnızca bir yerde kalmayı bildiren daha dar bir eylem çerçevesidir.","neighbor_ref":"root_000168/B016","relation_type":"near_synonym","shared_zone":"İki dal da bir kişinin belirli bir yerde kalmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal sürmekte olan kalış ve yaşam durumunu anlatır; komşu dal ise yeri konut seçme ya da başkasına konut sağlama işlemini öne çıkarır.","focus_only":"Bir yerde fiilen uzun süre yaşama ve geçmişte orada bulunmuş olma odak dalın merkezidir.","gloss":"orada yaşama ve konut edinme","neighbor_only":"Bir yeri konut edinme veya birini bir yere yerleştirme işlemi komşu dalda belirgindir.","neighbor_ref":"root_000162/B001","relation_type":"near_neighbor","shared_zone":"İki dal da kişi ile yaşadığı yer arasında kalıcı veya uzun süreli bir bağ kurar."},{"boundary_match":"partial","distinction":"Odak dal yaşama yeri ve uzun kalışla ilgilidir; komşu dal bedenin oturma duruşunu ve bu duruş çevresindeki birlikteliği anlatır.","focus_only":"Yerde uzun süre yaşama ve o yeri konut edinme odak dala özgüdür.","gloss":"bir yerde yaşama ve oturma duruşu","neighbor_only":"İnsan bedeninin oturma duruşu, oturum ve birlikte oturma komşu dalın çekirdeğidir.","neighbor_ref":"root_000254/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda kişi bir yerde bulunur ve o yere bağlı bir süreklilik gösterebilir."}],"source_phrase_ar":"غني القوم في دارهم أقاموا ومغانيهم منازلهم (maqayis)؛ غني القوم في المحلة طال مقامهم فيها وكأن لم يغن بالأمس أي كأن لم يكن (ayn)؛ غنى بالمكان أي أقام وغني أي عاش والمغنى واحد المغاني (sihah)؛ غني القوم في دارهم إذا طال مقامهم والمغاني المنازل (tahdhib)؛ غنى في مكان كذا إذا طال مقامه فيه والمغنى للمصدر وللمكان (mufradat)","source_summary":"Kaynaklar bir yerde oturma ve uzun süre kalma çekirdeğinde birleşir; geçmişte orada yaşama anlatımını, topluluğun evlerini ve hem eylemi hem yeri gösterebilen adları da bu alana bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الإقامة وطول المقام في الدار أو المحلة والمغاني منازل القوم والمغنى للمصدر أو المكان وما يقرب من العيش والكون السابق","what_is_not_ar":"ليس الغنى في المال ولا الكفاية ولا الغناء بالصوت"},"support_links":[]},{"boundary":"Süsten bağımsız sayılma ana açıklamadır, fakat sözcük her kaynakta aynı koşulları taşımaz; gençlik, güzellik, evlilik ve genel kadın kullanımları ayrı sınır çeşitleridir.","branch_kind":"bare","branch_ref":"root_001110/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَغْنَىٰ","morph_features":"STEM|POS:V|PERF|LEM:>agonaY`|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"111:2:2:1","qac_word_ref":"111:2:2","surface_ar":"أَغْنَىٰ"}],"gloss":"süsten bağımsız sayılan; bazen genç, güzel veya evli kadın","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadın, eşi veya kendi güzelliği sayesinde takı ve süslenmeye ihtiyaç duymayan biri olarak nitelenir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Nitelemenin sınırı gençlik, güzellik veya evlilik koşullarından yalnızca birine dayanabilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"En geniş kaynak kullanımında niteleme belirli bir koşul aranmadan genel olarak kadına uygulanabilir."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ana açıklama ile kaynaklarda görülen daha geniş kadın nitelemelerini birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Süsten bağımsız sayılma ana açıklamadır, fakat sözcük her kaynakta aynı koşulları taşımaz; gençlik, güzellik, evlilik ve genel kadın kullanımları ayrı sınır çeşitleridir.","branch_image_ar":"الغانية المستغنية","concept_gloss":"süsten bağımsız sayılan; bazen genç, güzel veya evli kadın","contextual_glosses":[{"applicability":"Nitelemenin kadının kendi güzelliği sayesinde süslenmeye gerek duymaması açıklamasına dayandığı bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eş sayesinde bağımsızlık ile yalnız gençlik, evlilik veya genel kadın kullanımını dışarıda bırakır.","preserves":"Güzellik nedeniyle süsten bağımsız sayılma yönünü açıkça korur."},"facet_ids":["F001"],"text":"güzelliğiyle süse ihtiyaç duymayan kadın","usage_role":"explanatory"},{"applicability":"Kaynak sınırının gençlik ve güzellik özelliklerine dayandığı kullanımda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eş veya güzellik sayesinde süsten bağımsız olma açıklamasını ve genel kadın kullanımını vermez.","preserves":"Gençlik ve güzellik temelli kaynak çeşidini korur."},"facet_ids":["F002"],"text":"genç ve güzel kadın","usage_role":"contextual"},{"applicability":"Nitelemenin yalnızca evlilik durumuna göre sınırlandığı kaynak kullanımında geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güzellik, gençlik, süsten bağımsızlık ve evli olmayan kadın kullanımlarını dışarıda bırakır.","preserves":"Evlilik koşuluna dayanan dar kaynak çeşidini korur."},"facet_ids":["F002"],"text":"evli kadın","usage_role":"contextual"}],"definition":"Eşi sayesinde takıya gerek duymadığı veya güzelliği nedeniyle süslenmeye ihtiyaç duymadığı düşünülen kadını anlatan bir nitelemedir. Kullanım sınırı bazı kaynaklarda genç evli kadın, güzel genç kadın, evli olsun olmasın güzel kadın, hatta genel olarak kadın olacak kadar genişler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadın, eşi veya kendi güzelliği sayesinde takı ve süslenmeye ihtiyaç duymayan biri olarak nitelenir."},{"facet_id":"F002","role":"source_variant","statement":"Nitelemenin sınırı gençlik, güzellik veya evlilik koşullarından yalnızca birine dayanabilir."},{"facet_id":"F003","role":"source_variant","statement":"En geniş kaynak kullanımında niteleme belirli bir koşul aranmadan genel olarak kadına uygulanabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eş sayesinde süsten bağımsızlık, evlilik, gençlik ve koşulsuz kadın kullanımlarını dışarıda bırakır.","preserves":"Güzellik özelliğine dayanan kullanımı korur."},"text":"güzel kadın"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Evli olmayan güzel kadın, süsten bağımsız kadın ve genel kadın kullanımlarını kapsamaz.","preserves":"Gençlik ile evliliği birlikte arayan dar kaynak çeşidini korur."},"text":"evli genç kadın"}],"identity_rationale":"Kaynak sözü, eşi veya güzelliği sayesinde takı ve süslenmeye ihtiyaç duymadığı düşünülen kadın açıklamasını güçlü biçimde destekler; ancak bütün tanımlar bu sınırı korumaz. Bazı kullanımlar genç evli kadın, güzel genç kadın, evli olsun olmasın güzel kadın, hatta genel olarak kadın düzeyine kadar genişler.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"eşi veya güzelliği sayesinde süse ihtiyaç duymadığı düşünülen; ayrıca genç, güzel ya da evli kadın"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bu niteliklerle anılan kadınlar; bazı kullanımlarda genç, güzel, evli ya da genel olarak kadınlar"}],"lexicalization_note":"Tanım yalın kadın nitelemesine bağlıdır; eşi, güzelliği, gençliği veya evliliği anlatan sınır çeşitleri korunur ve başka dallardaki evlenme olayına dönüştürülmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel ihtiyaçsızlık, genç ve güzel kadın, süs eşyası ve evlilik durumu ile sınırı gösteren dört aday seçildi, yalnızca aynı toplumsal sahneyi paylaşan daha uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli ve sınırları değişken bir kadın adıdır; komşu dal ise cinsiyet veya niteleme sınırlaması olmadan zenginlik ve ihtiyaçsızlık durumunu anlatır.","focus_only":"Belirli bir kadın nitelemesi ve bunun gençlik, güzellik veya evlilik sınırları odak dala özgüdür.","gloss":"kadın nitelemesi ve genel ihtiyaçsızlık","neighbor_only":"Genel maddi bolluk, mal çokluğu ve herhangi bir kişinin ihtiyaçtan bağımsızlığı komşu dalın kapsamıdır.","neighbor_ref":"root_001110/B001","relation_type":"near_neighbor","shared_zone":"Kadının eşi veya güzelliği sayesinde süse ihtiyaç duymadığı açıklaması, ihtiyaçtan bağımsızlık düşüncesiyle kesişir."},{"boundary_match":"partial","distinction":"Odak dalın ana açıklaması eş veya güzellik sayesinde süsten bağımsızlıktır ve sınırı değişkendir; komşu dal doğrudan gençlik ve güzelliği bildirir.","focus_only":"Eş veya güzellik sayesinde süse ihtiyaç duymama ve evlilik sınırı odakta bulunabilir.","gloss":"süsten bağımsız kadın ve genç güzel kız","neighbor_only":"Genç ve güzel kız olma, başka bir gerekçe aranmadan komşu dalın doğrudan çekirdeğidir.","neighbor_ref":"root_000610/B008","relation_type":"near_neighbor","shared_zone":"İki dal da genç ve güzel bir kadını nitelemek için kullanılabilir."},{"boundary_match":"thematic_only","distinction":"Odak dal bir kadını süse gerek duymama veya başka özelliklerle niteler; komşu dal ise süs eşyasını ve süslenme eylemini anlatır.","focus_only":"Süse ihtiyaç duymadığı düşünülen kadının kendisi odak dalda adlandırılır.","gloss":"süsten bağımsız kadın ve süs eşyası","neighbor_only":"Takı ve süs eşyasının kendisi ile bunları takma eylemi komşu dalda adlandırılır.","neighbor_ref":"root_000353/B001","relation_type":"thematic","shared_zone":"Her iki dal kadın, takı ve süslenme durumunun aynı sahnesinde yer alır."},{"boundary_match":"field_only","distinction":"Odakta evlilik yalnızca değişken sınırlardan biridir; komşu dal ise önceki evlilik veya birleşme sonrasındaki medeni durumu doğrudan tanımlar.","focus_only":"Güzellik, gençlik veya eş sayesinde süsten bağımsızlıkla kurulan kadın nitelemesi odakta yer alır.","gloss":"kadın nitelemesi ve önceki evlilik durumu","neighbor_only":"Evlilik ilişkisinin sona ermesi ya da evlilikte cinsel birleşme sonrası kazanılan durum komşuya özgüdür.","neighbor_ref":"root_000209/B005","relation_type":"same_field","shared_zone":"Her iki dal bir kadını evlilik durumu üzerinden niteleyebilir."}],"source_phrase_ar":"الغانية المرأة واستغنت ببعلها أو بجمالها عن لبس الحلي (maqayis)؛ الغانية الشابة المتزوجة غنيت بزوجها وغنيت بجمالها عن الزينة (ayn)؛ الغانية الجارية التي غنيت بزوجها وقد تكون التي غنيت بحسنها وجمالها (sihah)؛ الغواني ذوات الأزواج أو الشواب أو الجارية الحسناء أو كل امرأة (tahdhib)؛ الغانية المستغنية بزوجها عن الزينة أو بحسنها عن التزين (mufradat)","source_summary":"Kaynaklar kadın nitelemesinde birleşir, fakat sınırı farklı kurar: eşi veya güzelliği nedeniyle süse ihtiyaç duymama ana açıklamadır; gençlik, güzellik, evlilik ve koşulsuz kadın kullanımları daha geniş çeşitlerdir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الغانية والغواني على اختلاف تفسيرها بالمتزوجة أو الشابة أو الحسناء أو من استغنت بزوجها أو حسنها عن الزينة","what_is_not_ar":"ليس الغناء بالصوت ولا مطلق الغنى في المال ولا التزويج نفسه"},"support_links":[]},{"boundary":"Dal evlilik bağı kurma ve birini evlendirme olayına aittir; evliliğin koruyucu sayılması buna bağlı bir değerlendirmedir.","branch_kind":"bare","branch_ref":"root_001110/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَغْنَىٰ","morph_features":"STEM|POS:V|PERF|LEM:>agonaY`|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"111:2:2:1","qac_word_ref":"111:2:2","surface_ar":"أَغْنَىٰ"}],"gloss":"evlenme ve evlendirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi evlilik bağı kurar veya evlilik durumu adlandırılır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ettirgen kullanımda bir başkası, özellikle bir gelin, evlendirilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Evlilik, bekâr kişi için koruma sağlayan bir güvence olarak değerlendirilir."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Evlilik bağının kurulmasını hem kişinin kendisi hem de bir başkasını evlendiren katılımcı açısından kapsar.","boundary_detail":"Dal evlilik bağı kurma ve birini evlendirme olayına aittir; evliliğin koruyucu sayılması buna bağlı bir değerlendirmedir.","branch_image_ar":"الغنى والتزويج","concept_gloss":"evlenme ve evlendirme","contextual_glosses":[{"applicability":"Kişinin evlenmesi veya evlilik durumuna girmesi anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir başkasını evlendirme ve evliliği koruyucu sayma yönlerini dışarıda bırakır.","preserves":"Kişinin evlenmesi ve evlilik bağının kurulması yönünü korur."},"facet_ids":["F001"],"text":"evlilik bağı kurmak","usage_role":"contextual"},{"applicability":"Ettirgen kullanımda bir gelin için evlilik bağı kurulması anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin kendi evlenmesini ve evliliğin koruyucu sayılmasını kapsamaz.","preserves":"Bir başkasını, özellikle gelini, evlendirme yönünü korur."},"facet_ids":["F002"],"text":"bir gelini evlendirmek","usage_role":"contextual"}],"definition":"Evlilik bağı kurma veya birini, özellikle bir gelini, evlendirme anlamıdır. Evlilik ayrıca bekâr kişiyi koruyan bir güvence olarak tasarlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi evlilik bağı kurar veya evlilik durumu adlandırılır."},{"facet_id":"F002","role":"core","statement":"Ettirgen kullanımda bir başkası, özellikle bir gelin, evlendirilir."},{"facet_id":"F003","role":"associated_use","statement":"Evlilik, bekâr kişi için koruma sağlayan bir güvence olarak değerlendirilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kutlama ve tören olayını zorunluymuş gibi öne çıkarır.","collision":"Evlilik bağı ile düğün törenini birbirine karıştırır.","fit":"displacement","loses":"Evlilik bağını kurma ve birini evlendirme işlemlerini hukuki ve ilişkisel yönleriyle vermez.","preserves":"Evlilik çevresindeki toplumsal olaya gönderme yapar."},"text":"düğün"}],"identity_rationale":"Kaynak sözü evlenmeyi, gelinleri evlendirmeyi ve evliliğin bekâr kişi için koruyucu bir durum sayılmasını aynı dalda açıkça verir. Kadın nitelemesi, maddi zenginlik ve sesle ezgi anlamları bu çekirdeğin parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"evlenme; bekâr kişi için koruyucu sayılan evlilik"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"gelinleri evlendirme"}],"lexicalization_note":"Tanım yalın ad ve ettirgen biçimlerin evlenme ile evlendirme anlamlarını kapsar; düğün töreni, eşin kendisi veya evliliğin sonraki aşamaları eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; evlilik sözleşmesi, eş edinme, birlikte yaşama aşaması, örtülü evlilik anlatımı ve kadın nitelemesiyle sınırı gösteren beş aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal evlenme ile başkasını evlendirmeyi birlikte kapsar; komşu dal özellikle evlilik sözleşmesini ve bu sözleşmeyle evlenmeyi öne çıkarır.","focus_only":"Bir gelini evlendirme ve evliliği bekâr için koruyucu sayma yönleri odakta bulunur.","gloss":"evlenme ve evlilik sözleşmesi","neighbor_only":"Evlilik sözleşmesinin kendisini doğrudan adlandırma komşu dalda daha belirgindir.","neighbor_ref":"root_001548/B002","relation_type":"near_synonym","shared_zone":"Her iki dal evlilik bağının kurulmasını ve kişinin evlenmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal evlilik bağını kurma ve kurdurma olayını anlatır; komşu dal eş ve aile edinme sonucunu öne çıkarır.","focus_only":"Bir gelini evlendirme ve evliliği koruyucu bir güvence sayma odak dala özgüdür.","gloss":"evlenme ve eş edinme","neighbor_only":"Eş edinerek aile sahibi olma ve kişiye bir eş verilmesi komşu dalda daha belirgindir.","neighbor_ref":"root_000064/B002","relation_type":"near_synonym","shared_zone":"İki dal da kişinin evlenerek bir eş ve aile bağı edinmesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal bağın kurulmasını anlatır; komşu dal ise kurulmuş evliliğin ardından eşlerin bir araya gelmesi ve ortak yaşama geçmesi aşamasına yönelir.","focus_only":"Evlilik bağını kurma ve bir başkasını evlendirme odak dalın çekirdeğidir.","gloss":"evlenme ve eşlerin birleşmesi","neighbor_only":"Evliliğin ardından eşlerin birlikte yaşamaya başlaması ve gelinin eve getirilmesi komşuya özgüdür.","neighbor_ref":"root_000156/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal evlilik sürecinin birbirine yakın aşamalarında yer alır."},{"boundary_match":"partial","distinction":"Odak dal doğrudan evlenme ve evlendirme anlamındadır; komşu dal örtülü bir anlatımla evlilikten cinsel birleşmeye kadar genişleyebilir.","focus_only":"Bir başkasını evlendirme ve koruyucu evlilik düşüncesi odak dalda açıkça yer alır.","gloss":"evlilik bağı ve evlilik için örtülü anlatım","neighbor_only":"Evlilik yanında cinsel birleşmeye kadar uzanan örtülü kullanım komşu dalın ek kapsamıdır.","neighbor_ref":"root_000161/B005","relation_type":"near_neighbor","shared_zone":"İki dal da evlenme anlamını veya evliliğe gönderme yapan bir kullanımı kapsar."},{"boundary_match":"field_only","distinction":"Odak dal bir olay ve ilişki kurma sürecidir; komşu dal ise evli olabilen veya başka özelliklerle tanımlanan bir kadın adıdır.","focus_only":"Evlilik bağını kurma veya birini evlendirme olayı odak dala özgüdür.","gloss":"evlenme olayı ve kadın nitelemesi","neighbor_only":"Evlilik, güzellik veya gençlik üzerinden tanımlanan kadın nitelemesi komşu dala özgüdür.","neighbor_ref":"root_001110/B005","relation_type":"same_field","shared_zone":"Her iki dal evlilik ve kadınla ilgili aynı toplumsal alan içinde yer alabilir."}],"source_phrase_ar":"الأغناء إملاكات العرائس (tahdhib)؛ الغنى التزويج (tahdhib)؛ الغنى حصن للعزب أي التزويج (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynaklı kullanım, evlenmeyi ve gelinleri evlendirmeyi anlatır; evliliği de bekâr kişi için koruyucu bir güvence sayar."}],"source_summary":"Bu dalda ad ve ettirgen biçim, evlilik bağı kurma çevresinde birleşir; koruma düşüncesi evlenmenin sonucu olarak sunulur.","sources":["TA"],"what_is_ar":"يدخل فيه الغنى بمعنى التزويج والأغناء بمعنى إملاكات العرائس وجعل التزويج حصنا للعزب","what_is_not_ar":"ليس الغانية نفسها ولا الغناء بالصوت ولا الغنى في المال"},"support_links":[]},{"boundary":"Bu kol başkasına kazandırmayı, beden üyelerine verilen adı ve yağdan çıkan ayrı maddeyi kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001296/B001","candidate_links":[{"candidate_id":"cand_5d7bed8ee6cb087f5c69","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَسَبَ","morph_features":"STEM|POS:V|PERF|LEM:kasaba|ROOT:ksb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"111:2:6:1","qac_word_ref":"111:2:6","surface_ar":"كَسَبَ"}],"gloss":"kendisi için geçimlik ya da yarar arayıp elde etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yarar sağlayacak bir şeyi arama ve isteme, ona ulaşıp onu edinme sonucuna yönelir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Geçimlik ve para, bu arama ve edinme hareketinin öne çıkan nesneleridir."}}],"root_ar":"ك س ب","root_id":"root_001296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Arama, isteme ve sonuca ulaşma aşamalarını; geçimlik, para ve daha geniş yarar alanını birlikte karşılayan tam kavram anlatımıdır.","boundary_detail":"Bu kol başkasına kazandırmayı, beden üyelerine verilen adı ve yağdan çıkan ayrı maddeyi kapsamaz.","branch_image_ar":"طلب الرزق والنفع وإصابته","concept_gloss":"kendisi için geçimlik ya da yarar arayıp elde etme","contextual_glosses":[{"applicability":"Sözün özellikle geçim sağlama ve para kazanma bağlamında kullanıldığı yerlerde doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Geçimlik ya da para dışındaki yarar türlerini anlatımın dışında bırakır.","preserves":"Çaba göstererek kişinin kendisi için yararlı bir sonuç edinmesini korur."},"facet_ids":["F001","F002"],"text":"geçimini kazanma","usage_role":"contextual"},{"applicability":"Sonuca ulaşmanın öne çıktığı, yararın para veya geçimlikle sınırlı olmadığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sonuçtan önceki arama ve isteme aşamasını açık biçimde taşımaz.","preserves":"Kişinin kendisi için yararlı bir sonuç edinmesi yönünü açıkça korur."},"facet_ids":["F001"],"text":"bir yarar elde etme","usage_role":"contextual"},{"applicability":"Henüz arama ve uğraş aşamasının anlatıldığı, sonucun kesinleşmediği bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aranan şeye ulaşıp ondan pay edinme sonucunu anlatımın dışında bırakır.","preserves":"Yarar arama, isteme ve bunun için çaba gösterme aşamasını korur."},"facet_ids":["F001"],"text":"kazanç peşinde olma","usage_role":"contextual"}],"definition":"Kişinin kendisi için geçimlik, para ya da başka bir yararı arayıp istemesi ve ona ulaşarak pay edinmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yarar sağlayacak bir şeyi arama ve isteme, ona ulaşıp onu edinme sonucuna yönelir."},{"facet_id":"F002","role":"specialization","statement":"Geçimlik ve para, bu arama ve edinme hareketinin öne çıkan nesneleridir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Geçimlik dışındaki para olmayan yararları ve daha geniş edinim alanını dışarıda bırakır.","preserves":"Kişinin çaba göstererek kendisi için para edinmesi yönünü korur."},"text":"para kazanma"}],"identity_rationale":"Kaynak sözü, yararlı bir şeyi arama ve isteme hareketini ona ulaşıp pay edinme sonucuyla birlikte verir. Geçimlik ve para bu çekirdeğin belirgin uygulamalarıdır; kişinin kendisi için edinmesi de bu kolun katılımcı sınırını gösterir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"geçimlik ve yarar arayıp elde etme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyi ya da parayı kendisi için kazanmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyi özellikle kendisi için edinmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kazanç sağlamak için uğraşmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"çok kazanan ya da geçimini arayan kimse"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kişinin kazandığı şey ya da kazanç yolu"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"iyi ve temiz kazanç"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"para kazanan; ayrıca kurt ya da dişi köpek adı olarak kullanılan biçim"}],"lexicalization_note":"Kapsam, yalın biçimlerdeki arama ve elde etme çekirdeğiyle yalnız belirli söz öbeğinde bulunan nitelikli kazancı birlikte içerir; söz öbeğindeki iyi ve temiz olma niteliği genel tanıma taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan üç karşılaştırma katılımcı yönünü, ekonomik alan sınırını ve arama-sonuç ayrımını en açık biçimde gösterir. Kalan adaylar yalnız ortak kazanç alanını tekrarlar ya da uzak bir tema sunar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kolunda kişi yararı kendisi için arayıp edinir. Komşu kolda ise bir kişi, başka birinin para ya da iyilik edinmesini sağlar; bu katılımcı değişimi iki kullanımı birbirinin yerine geçmez kılar.","focus_only":"Yararı arayan ve edinen kişi aynı kişidir; hareket onun kendi payına yönelir.","gloss":"kendisi için kazanma / başkasına kazandırma","neighbor_only":"Bir başkasına para ya da iyilik kazandıran ayrı bir katılımcı ve iki nesneli kullanım vardır.","neighbor_ref":"root_001296/B002","relation_type":"near_neighbor","shared_zone":"Her iki kol da para ya da başka bir yararın bir kişinin eline geçmesini konu eder."},{"boundary_match":"partial","distinction":"Komşu, kazancı meslek, zanaat, ticaret ve mal artışı gibi ekonomik uygulamalarla genişletir. Odak kolunun çekirdeği ise belirli bir iş alanına bağlı olmadan yararı arayıp ona ulaşmaktır.","focus_only":"Yarar arama ve edinme çekirdeği meslek, ticaret ya da mal artışıyla sınırlı değildir.","gloss":"yarar edinme / mesleki ve ticari kazanç","neighbor_only":"Meslek, zanaat, ticari işlem ve malın büyümesi gibi özel ekonomik alanları ayrıca kapsar.","neighbor_ref":"root_000310/B006","relation_type":"near_synonym","shared_zone":"İki kol da geçim arama, para kazanma ve emek yoluyla yararlı sonuç edinme alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu kol elde edilmiş kazanç sonucuna yoğunlaşır. Odak kolu ise isteme ve arama hareketini sonuca ulaşıp yarar edinmeyle birlikte kurduğu için süreç sınırı daha belirgindir.","focus_only":"Sonuca varmadan önceki arama ve isteme aşamasını açıkça çekirdeğe alır.","gloss":"yararı arayıp edinme / kazancı elde etme","neighbor_only":"Kazanca ya da paraya ulaşma sonucunu daha dar ve belirgin biçimde öne çıkarır.","neighbor_ref":"root_000580/B004","relation_type":"near_synonym","shared_zone":"Her iki kol da kişinin kendi emeğiyle kazanç ya da para elde etmesini anlatabilir."}],"source_phrase_ar":"الكاف والسين والباء أصل صحيح وهو يدل على ابتغاء وطلب وإصابة (maqayis)؛ الكسب طلب الرزق (ayn;sihah;tahdhib)؛ الكسب ما يتحراه الإنسان مما فيه اجتلاب نفع وتحصيل حظ ككسب المال (mufradat)؛ كسبت الشيء واكتسبته (jamhara;sihah)","source_summary":"Kaynaklar ortak biçimde arama ve isteme ile sonuca ulaşıp yarar edinmeyi bir arada tutar. Geçimlik ve para başlıca örneklerdir; kişinin kazandığı şeyi kendisi için edinmesi bu kolun olağan yönelimidir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"طلب الرزق والمال والنفع وتحصيله للنفس، وما يتكلفه الإنسان من المكاسب، وما يقال فيه كسب واكتسب لنفسه","what_is_not_ar":"إكساب غيره مالا أو خيرا؛ الكُسب عصارة الدهن؛ الكواسب الجوارح؛ الأعلام مثل كساب وكسيب وكيسبة"},"support_links":["sup_8af5d3e738e6144d04c0"]},{"boundary":"Bu kol doğrudan verme eyleminin geneli değil, bir başkasına para ya da iyilik kazandıran özel kullanımdır.","branch_kind":"non_bare","branch_ref":"root_001296/B002","candidate_links":[{"candidate_id":"cand_1aed28b6ee13f6e80f94","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَسَبَ","morph_features":"STEM|POS:V|PERF|LEM:kasaba|ROOT:ksb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"111:2:6:1","qac_word_ref":"111:2:6","surface_ar":"كَسَبَ"}],"gloss":"birine para ya da iyilik kazandırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi, para ya da iyiliği başka bir kişinin eline geçirecek biçimde sağlar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sağlayan, edinen ve edinilen şeyin ayrı öğeler olduğu iki nesneli yapı bu anlamı belirginleştirir."}}],"root_ar":"ك س ب","root_id":"root_001296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sağlayanın başka, yararı edinenin başka kişi olduğu özel yapıyı kısa ve doğal biçimde karşılar.","boundary_detail":"Bu kol doğrudan verme eyleminin geneli değil, bir başkasına para ya da iyilik kazandıran özel kullanımdır.","branch_image_ar":"إكساب غيره خيرا أو مالا","concept_gloss":"birine para ya da iyilik kazandırma","contextual_glosses":[{"applicability":"Yararın aile üyelerine yöneldiği ve sağlanan şeyin geçimlik olduğu örneklerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aile dışındaki alıcıları ve geçimlik dışında kalan iyilik türlerini dışarıda bırakır.","preserves":"Sağlayan kişiyle yararı edinen kişilerin ayrı oluşunu ve geçim sağlamayı korur."},"facet_ids":["F001","F002"],"text":"ailesine geçim sağlama","usage_role":"contextual"},{"applicability":"Sağlayanın malı kendi payına değil başka bir kişinin payına elde ettiği kullanımı açıklamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Mal dışındaki iyilikleri ve alıcının edinmesine doğrudan yol açma yönünü zayıflatır.","preserves":"Edinilen şeyin başka bir kişiye yönelmesini ve katılımcı ayrımını korur."},"facet_ids":["F001","F002"],"text":"bir başkası için mal edinme","usage_role":"explanatory"}],"definition":"Bir başkası için para ya da iyilik sağlayarak onun bunu edinmesine yol açmaktır; anlam, sağlayan ile edinenin ayrı kişiler olduğu özel kullanıma bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi, para ya da iyiliği başka bir kişinin eline geçirecek biçimde sağlar."},{"facet_id":"F002","role":"specialization","statement":"Sağlayan, edinen ve edinilen şeyin ayrı öğeler olduğu iki nesneli yapı bu anlamı belirginleştirir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Karşılıksız bağış ve sıradan nesne aktarımı gibi daha geniş verme durumlarını ekler.","collision":null,"fit":"displacement","loses":"Alıcının kazanmasına ya da edinmesine yol açan özel yapıyı kaybeder.","preserves":"Bir yararın başka bir kişinin eline geçmesi yönünü kısmen korur."},"text":"birine vermek"}],"identity_rationale":"Kaynak sözü, bir kişinin ailesine veya başka birine para ya da iyilik sağlamasını ve o kişinin bunu edinmesine yol açmasını açıkça anlatır. İki nesneli kullanım, bu kolu kişinin yalnız kendisi için edinmesinden ayıran yapısal sınırdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"birine para ya da iyilik kazandırmak"}],"lexicalization_note":"Tanım yalnızca bir başkasını yararın alıcısı yapan, iki katılımcılı ve iki nesneli kullanıma bağlıdır; yalın kazanma anlamına genişletilemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen karşılaştırmalar kendi adına kazanma, genel ulaştırma ve doğrudan verme ile olan temel ayrımları gösterir. Öteki adaylar bu üç sınırın daha geniş ya da daha uzak örneklerini yineler.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kolu, bir kişinin başka birine yarar kazandırdığı özel yapıdır. Komşu kol ise kişinin yararı kendi adına arayıp edinmesini anlatır; alıcının değişmesi anlam sınırını değiştirir.","focus_only":"Sağlayan kişi ile para ya da iyiliği edinen kişi birbirinden ayrıdır.","gloss":"başkasına kazandırma / kendisi için kazanma","neighbor_only":"Arayan, çabalayan ve yararı kendi payına edinen tek bir kişi vardır.","neighbor_ref":"root_001296/B001","relation_type":"near_neighbor","shared_zone":"İki kol da para ya da yararın edinilmesi ve bir kişinin payına geçmesi çevresinde buluşur."},{"boundary_match":"partial","distinction":"Komşu kol genel ulaştırma ve eriştirme hareketidir. Odak kolu ise para ya da iyiliğin başka birine kazandırılmasına ve o kişinin edinim sonucuna bağlıdır.","focus_only":"Aktarılan şey para ya da iyiliktir ve alıcının bunu kazanması sağlanır.","gloss":"yarar kazandırma / bir şeyi ulaştırma","neighbor_only":"Herhangi bir şeyi başkasına ulaştırma anlamı, kazanma ilişkisi aramadan daha geniş işler.","neighbor_ref":"root_001572/B002","relation_type":"near_neighbor","shared_zone":"Her ikisinde de bir şey bir kişinin aracılığıyla başka bir kişinin eline geçer."},{"boundary_match":"partial","distinction":"Komşu kolun çekirdeği doğrudan verme ve sahip kılmadır. Odak kolu, alıcının para ya da iyilik edinmesini sağlayan kazanma ilişkisini gerektirir; her verme bu özel yapıyı karşılamaz.","focus_only":"Bir başkasının para ya da iyilik kazanmasına yol açan özel edinim ilişkisini kurar.","gloss":"kazandırma / verip sahip kılma","neighbor_only":"Verenin bir şeyi doğrudan verip alıcıyı onun sahibi yapması yeterlidir.","neighbor_ref":"root_000448/B002","relation_type":"near_neighbor","shared_zone":"Her iki kol da bir yararın başka bir kişiye geçmesi ve onun payı olması sonucunu taşıyabilir."}],"source_phrase_ar":"كسب أهله خيرا (maqayis)؛ كسبت الرجل مالا فكسبه (maqayis;jamhara;sihah)؛ فلان يكسب أهله خيرا (tahdhib)؛ الكسب يقال فيما أخذه لنفسه ولغيره ويتعدى إلى مفعولين (mufradat)","source_summary":"Kaynaklar, aileye ya da başka bir kişiye para veya iyilik sağlama örneklerinde sağlayanla edinen kişiyi ayırır. Bir şeyi kendisi için edinme anlamının yanında, başkası için edinmeyi ve iki nesneli yapıyı da açıkça tanır.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"إيصال المال أو الخير إلى غيره وجعله يكسبه، واستعمال كسب مع مفعولين لما يأخذه الإنسان لغيره","what_is_not_ar":"طلب الرزق للنفس وحدها؛ الاكتساب الذي لا يقال إلا لما يستفيده المرء لنفسه؛ الكُسب عصارة الدهن؛ الكواسب الجوارح"},"support_links":["sup_c7fb5e5f2013ea90882e"]},{"boundary":"Anlam beden üyeleriyle sınırlıdır; avcı hayvanları, pençeyi ya da kazanma sürecini doğrudan adlandırmaz.","branch_kind":"non_bare","branch_ref":"root_001296/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَسَبَ","morph_features":"STEM|POS:V|PERF|LEM:kasaba|ROOT:ksb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"111:2:6:1","qac_word_ref":"111:2:6","surface_ar":"كَسَبَ"}],"gloss":"bedenin iş gören üyeleri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Adlandırılan varlıklar, insan bedeninin iş yapan üyeleridir."}}],"root_ar":"ك س ب","root_id":"root_001296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Toplu adın gösterdiği varlık kümesini işlem ya da avcılık anlamı eklemeden doğrudan karşılar.","boundary_detail":"Anlam beden üyeleriyle sınırlıdır; avcı hayvanları, pençeyi ya da kazanma sürecini doğrudan adlandırmaz.","branch_image_ar":"الكواسب الجوارح","concept_gloss":"bedenin iş gören üyeleri","contextual_glosses":[{"applicability":"İş görme çağrışımının bağlamdan anlaşılabildiği düz anlatımlarda doğal ve kısa bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bu üyelerin iş gören parçalar olarak adlandırılması çağrışımını açıkça taşımaz.","preserves":"Adlandırılan kümenin bedenin üyelerinden oluştuğunu eksiksiz biçimde korur."},"facet_ids":["F001"],"text":"beden üyeleri","usage_role":"general"}],"definition":"Bedenin iş gören üyeleri için kullanılan toplu bir addır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Adlandırılan varlıklar, insan bedeninin iş yapan üyeleridir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kuş, köpek ve yırtıcı hayvanlarla avcılık alanını haksız biçimde ekler.","collision":"Beden üyeleriyle avcı hayvanları karşılayabilen komşu bir söz alanıyla karışır.","fit":"displacement","loses":"İnsan bedeninin üyelerini gösteren asıl varlık kümesini bütünüyle kaybeder.","preserves":"Canlı bir varlığın iş gören gücüyle ilgili uzak çağrışımı korur."},"text":"avcı hayvanlar"}],"identity_rationale":"Kaynak sözü, ilgili çoğul adı doğrudan beden üyeleriyle açıklar. Bu nedenle kol bir kazanma eylemi değil, bedenin iş gören üyeleri için kullanılan yerleşik bir ad olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bedenin iş gören üyeleri"}],"lexicalization_note":"Tanım yalnızca beden üyelerini topluca adlandıran çoğul sözlük birimine bağlıdır; kökün genel kazanma anlamına ya da başka canlılara genişletilemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan iki ilişki eylem ile organ adı arasındaki tematik bağı ve özel beden parçasıyla toplu ad arasındaki alan sınırını gösterir. Av hayvanları ve av olaylarıyla ilgili adaylar anlam çekirdeği paylaşmaz.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Odak kolu bir eylem değil, beden üyelerinin adıdır. Komşu kol ise yarar arama ve edinme sürecidir; yalnız ortak bir iş görme senaryosunda buluşurlar ve birbirlerinin yerine kullanılamazlar.","focus_only":"Beden üyelerinden oluşan bir varlık kümesini topluca adlandırır.","gloss":"iş gören beden üyeleri / yarar edinme","neighbor_only":"Bir yararı arama, isteme ve onu kişinin kendi payına edinmesi sürecini anlatır.","neighbor_ref":"root_001296/B001","relation_type":"thematic","shared_zone":"Beden üyeleri, kişinin iş yapıp yarar edinmesi senaryosunda araç rolü taşıyabilir."},{"boundary_match":"field_only","distinction":"Komşu kol belirli bir beden yapısı olan tırnak ve pençeye odaklanır. Odak kolu ise tek bir yapı türünü değil, bedenin iş gören üyelerini topluca adlandırır.","focus_only":"Bedenin iş gören üyelerini ayrım yapmadan toplu bir küme olarak gösterir.","gloss":"beden üyeleri / tırnak ve pençe","neighbor_only":"Tırnak, pençe ve bunlara benzeyen sivri beden yapılarını özel olarak gösterir.","neighbor_ref":"root_000965/B002","relation_type":"same_field","shared_zone":"İki kol da canlı bedenindeki iş gören yapıları ve parçaları adlandırır."}],"source_phrase_ar":"الكواسب الجوارح (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu tek tanıklık, sözü bedenin iş gören üyeleri için kullanılan toplu bir ad olarak verir."}],"source_summary":"Tek kaynak tanıklığı, çoğul bir adı doğrudan beden üyeleriyle karşılar ve bunun dışında bir işlem, araç türü ya da avcılık kapsamı belirtmez.","sources":["SI"],"what_is_ar":"الجوارح التي تسمى الكواسب","what_is_not_ar":"طلب الرزق والمال؛ إكساب غيره؛ الكُسب عصارة الدهن"},"support_links":[]},{"boundary":"Tanım yağdan çıkan belirli özlü sıkım maddesiyle sınırlı tutulmalı; genel yağ, sıkma işlemi veya her türlü artık anlamına açılmamalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001296/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَسَبَ","morph_features":"STEM|POS:V|PERF|LEM:kasaba|ROOT:ksb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"111:2:6:1","qac_word_ref":"111:2:6","surface_ar":"كَسَبَ"}],"gloss":"yağdan çıkan özlü sıkım maddesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gösterilen şey, yağdan çıkan özlü sıkım ürünü niteliğinde belirli bir maddedir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı madde, açıklayıcı karşılık yerine iki başka adla da tanıtılır."}}],"root_ar":"ك س ب","root_id":"root_001296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli maddeyi genel yağdan ve sıkma işleminden ayırırken kaynak açıklamasındaki öz ile kalıntı arasındaki genişliği korur.","boundary_detail":"Tanım yağdan çıkan belirli özlü sıkım maddesiyle sınırlı tutulmalı; genel yağ, sıkma işlemi veya her türlü artık anlamına açılmamalıdır.","branch_image_ar":"الكُسب عصارة الدهن","concept_gloss":"yağdan çıkan özlü sıkım maddesi","contextual_glosses":[{"applicability":"Maddenin sıkımdan sonra kalan yoğun bölüm olarak anlaşıldığı bağlamlarda kullanılabilecek doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kaynak açıklamasının sıvı ya da özlü çıktı olarak anlaşılabilen daha geniş yönünü dışarıda bırakır.","preserves":"Yağla ilişkiyi, sıkım sonucunu ve ayrı bir ürün oluşunu açıkça korur."},"facet_ids":["F001"],"text":"yağ sıkımından çıkan artık","usage_role":"contextual"},{"applicability":"Maddenin posa ya da sıvı öz diye kesinleştirilmeden açıklanması gereken sözlük bağlamlarına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yağ kökenini, sıkımla ortaya çıkışı ve ürünün kıvamca açık bırakılmasını korur."},"facet_ids":["F001","F002"],"text":"yağın özlü sıkım ürünü","usage_role":"explanatory"}],"definition":"Yağdan çıkan özlü sıkım maddesi olarak açıklanan belirli bir üründür. Kaynaklarda aynı madde iki başka adla da tanıtılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gösterilen şey, yağdan çıkan özlü sıkım ürünü niteliğinde belirli bir maddedir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı madde, açıklayıcı karşılık yerine iki başka adla da tanıtılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Sıkımdan çıkan belirli ürünü değil, bütün yağ türlerini ve yağın kendisini kapsar.","collision":"Yağın kendisiyle yağdan çıkan özel sıkım maddesini birbirine karıştırır.","fit":"broadening","loses":null,"preserves":"Adlandırılan ürünün yağla olan temel malzeme ilişkisini korur."},"text":"yağ"}],"identity_rationale":"Kaynak sözü belirli bir yağ kökenli maddeyi hem yağın özlü sıkım çıktısı diye açıklar hem de iki başka adla eşler. Kolun ayrı bir madde adı oluşu sağlamdır; ancak açıklamayı yalnız modern anlamdaki posa ya da yalnız sıvı öz diye daraltmak kaynak sınırını aşar.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yağdan çıkan özlü sıkım maddesi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"aynı yağ sıkım maddesi için kullanılan başka bir ad"}],"lexicalization_note":"Kapsam, ana madde adını ve ona bağlı başka adlandırmayı birlikte içerir; tanım yalnız bu yağ kökenli maddeye bağlanır ve kökün kazanma anlamına ya da genel sıkım ürünlerine taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen dört karşılaştırma sıkma işlemi, benzer yağ kalıntıları, genel öz ve artıklar ile yağın kendisi karşısındaki sınırı gösterir. Öteki adaylar daha uzak yiyecek artıkları ya da hazırlama işlemleri sunar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu kolun çekirdeği sıkma işlemi ve ondan doğan genel ürünlerdir. Odak kolu ise yalnız yağla ilişkili, özel adlandırılmış bir maddeyi gösterir; işlem anlamı taşımaz.","focus_only":"Yağdan çıkan ve özel bir ad taşıyan belirli sıkım maddesini gösterir.","gloss":"özel yağ sıkım maddesi / sıkma ve çıktıları","neighbor_only":"Sıkma işlemini, bu işlemin araçlarını ve üzüm ya da zeytin gibi çeşitli sıkım çıktılarını kapsar.","neighbor_ref":"root_001019/B002","relation_type":"near_neighbor","shared_zone":"İki kol da sıkma sonucunda bir maddeden öz ya da çıktı elde edilmesi alanında buluşur."},{"boundary_match":"partial","distinction":"Komşu, eski yağ kalıntısı ile arıtılmış yağ veya süt özünü kapsayan başka bir madde kümesidir. Odak kolu yalnız yağ sıkımından çıkan ve özel biçimde adlandırılan üründür.","focus_only":"Yağ sıkımından çıkan, kendi özel adı bulunan belirli maddeyi gösterir.","gloss":"yağ sıkım maddesi / yağ kalıntısı ve öz","neighbor_only":"Eski yağın kalıntısını ya da arıtılmış yağ ve süt özünü gösteren ayrı maddeleri kapsar.","neighbor_ref":"root_000011/B009","relation_type":"near_neighbor","shared_zone":"Her iki kol yağlı bir maddeden kalan ya da ayrılan yoğun öz ve kalıntı alanına girer."},{"boundary_match":"partial","distinction":"Komşu kol birçok yiyecekten ayrılan öz ve artıkları kapsayan geniş bir alandır. Odak kolu ise malzeme ve ad bakımından yalnız belirli yağ sıkım ürününe bağlıdır.","focus_only":"Yalnız yağdan çıkan ve özel adı olan bir sıkım maddesine bağlıdır.","gloss":"özel yağ ürünü / ayrıştırılmış öz ve artık","neighbor_only":"Yağ, süt, hurma ve başka yiyeceklerden ayırma yoluyla çıkan özleri ve dip artıklarını genişçe kapsar.","neighbor_ref":"root_000430/B008","relation_type":"near_neighbor","shared_zone":"İki kol da bir yiyecek ya da yağlı karışımdan ayrılan öz veya kalıntıyı konu edebilir."},{"boundary_match":"partial","distinction":"Komşu kol yağın kendisini ve zeytin özünü gösterir. Odak kolu ise yağdan çıkan, ayrı adlandırılmış sıkım maddesidir; ham madde ile türeyen ürün aynı sayılmaz.","focus_only":"Yağın kendisini değil, ondan çıkan özel sıkım maddesini gösterir.","gloss":"yağdan çıkan madde / yağ ve zeytin özü","neighbor_only":"Bilinen yağı, zeytinyağını ve zeytinden çıkan yağ özünü doğrudan kapsar.","neighbor_ref":"root_000656/B001","relation_type":"near_neighbor","shared_zone":"Her iki kol yağ ve yağın çıkarıldığı ya da ondan türeyen ürünler alanında yer alır."}],"source_phrase_ar":"الكُسب الكنجارق ويقال الكسبج (ayn)؛ الكُسب عصارة الدهن (sihah)؛ الكُسب الكنجارق وبعض السواديين يسمونه الكسبج (tahdhib)","source_summary":"Kaynak kümesi, sözü yağdan çıkan özlü bir sıkım maddesi olarak açıklar ve aynı maddeyi iki başka adla eşler. Bu anlatım, maddenin tam olarak sıvı öz mü yoksa yoğun kalıntı mı olduğunu modern bir teknik sınıfa kesin biçimde yerleştirmez.","sources":["AY","SI","TA"],"what_is_ar":"اسم للمادة المسماة الكنجارق أو الكسبج، وفسرت بأنها عصارة الدهن","what_is_not_ar":"طلب الرزق والمال؛ إكساب غيره؛ الكواسب الجوارح"},"support_links":[]},{"boundary":"Dal yalnızca para ya da birikmiş değer değildir; varlığın kendisini, edinilmesini, artmasını, varlıklı duruma geçişi ve başkasına varlık kazandırmayı ayırarak kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001457/B001","candidate_links":[{"candidate_id":"cand_83db1874cff5e496c72e","lane":"micro"},{"candidate_id":"cand_5d7bed8ee6cb087f5c69","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:2:4:1","qac_word_ref":"111:2:4","surface_ar":"مَالُ"}],"gloss":"varlık; edinme, çoğalma ve başkasına kazandırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin sahip olduğu ve değer taşıyan varlıkların bütünü bu dalın ad çekirdeğini oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Göçebe toplulukların varlığına ilişkin belirli kullanımda bu varlık, hayvan sürüleriyle somutlaşır."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişinin kendisi için değerli varlık edinmesi ve onu kalıcı sahiplik konusu yapması eylem çekirdeğidir."}},{"facet_id":"F004","role":"core","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kişinin varlığının çoğalması ya da onun varlık sahibi bir duruma geçmesi ayrı bir süreç görünümüdür."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Bir başkasına değerli varlık vererek onu varlık sahibi duruma getirmek, çekirdeğin ettirgen uzantısıdır."}},{"facet_id":"F006","role":"associated_use","source_fields":["distinctive_facets[F006]"],"statements":{"statement":"Bir kimsenin varlığının çokluğuna şaşma bildiren söyleyiş, artış ve bolluk görünümüne bağlı bir kullanımdır."}}],"root_ar":"م و ل","root_id":"root_001457","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın sahip olunan varlık, onu edinme, varlıklı duruma gelme ve başkasını varlık sahibi kılma çekirdeklerini birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Dal yalnızca para ya da birikmiş değer değildir; varlığın kendisini, edinilmesini, artmasını, varlıklı duruma geçişi ve başkasına varlık kazandırmayı ayırarak kapsar.","branch_image_ar":"اتخاذ المال وكثرته","concept_gloss":"varlık; edinme, çoğalma ve başkasına kazandırma","contextual_glosses":[{"applicability":"Bir kişinin elindeki değer taşıyan şeylerin bütünü ya da bunların çoğulu ad olarak anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Edinme, çoğalma, varlıklı duruma gelme ve başkasına varlık kazandırma süreçlerini karşılamaz.","preserves":"Dalın kişiye ait değerli varlıklar bildiren ad çekirdeğini korur."},"facet_ids":["F001"],"text":"sahip olunan değerli varlıklar","usage_role":"general"},{"applicability":"Kişinin değerli bir şeyi kendisi için edinip sahipliğinde tutması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Varlık adını, varlığın kendiliğinden artmasını ve başkasına varlık kazandırmayı dışarıda bırakır.","preserves":"Kendisi için varlık edinme ve onu kalıcı sahiplik konusu yapma sürecini korur."},"facet_ids":["F003"],"text":"kendine kalıcı varlık edinmek","usage_role":"contextual"},{"applicability":"Bir kişinin sahip olduklarının artması ya da kişinin varlık sahibi hale gelmesi anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Varlığın ad çekirdeğini, bilinçli edinmeyi ve başkasını varlık sahibi kılmayı karşılamaz.","preserves":"Varlık artışını ve kişinin varlıklı duruma geçişini açıkça korur."},"facet_ids":["F004"],"text":"varlığı çoğalmak veya varlıklı duruma gelmek","usage_role":"contextual"},{"applicability":"Bir kişinin başkasına değerli varlık vererek onun sahiplik durumunu değiştirmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Varlığın kendisini, kişinin kendisi için edinmesini ve kendi varlığının artmasını karşılamaz.","preserves":"Başkasına varlık kazandıran ettirgen katılımcı değişimini korur."},"facet_ids":["F005"],"text":"birini varlık sahibi yapmak","usage_role":"contextual"}],"definition":"Kişinin sahip olduğu değerli varlıkların bütünü ile bunları edinme, çoğaltma ya da bunlara sahip duruma gelme alanıdır. Ayrıca başkasını varlık sahibi kılmayı kapsar; göçebe topluluklara özgü kullanımda sahip olunan varlık özellikle hayvan sürüleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin sahip olduğu ve değer taşıyan varlıkların bütünü bu dalın ad çekirdeğini oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Göçebe toplulukların varlığına ilişkin belirli kullanımda bu varlık, hayvan sürüleriyle somutlaşır."},{"facet_id":"F003","role":"core","statement":"Kişinin kendisi için değerli varlık edinmesi ve onu kalıcı sahiplik konusu yapması eylem çekirdeğidir."},{"facet_id":"F004","role":"core","statement":"Kişinin varlığının çoğalması ya da onun varlık sahibi bir duruma geçmesi ayrı bir süreç görünümüdür."},{"facet_id":"F005","role":"extension","statement":"Bir başkasına değerli varlık vererek onu varlık sahibi duruma getirmek, çekirdeğin ettirgen uzantısıdır."},{"facet_id":"F006","role":"associated_use","statement":"Bir kimsenin varlığının çokluğuna şaşma bildiren söyleyiş, artış ve bolluk görünümüne bağlı bir kullanımdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Dalın bütün sahip olunan varlıkları kapsayan alanını yalnızca ödeme aracına indirger.","fit":"narrowing","loses":"Nakit dışındaki varlıkları, hayvan sürüsü özelleşmesini ve edinme, artma, varlıklılaşma ile kazandırma süreçlerini siler.","preserves":"Değer taşıyan ve sahip olunabilen bir şey düşüncesinin yalnızca nakit yönünü korur."},"text":"para"}],"identity_rationale":"Kaynak ifadesi, sahip olunan değerli varlıkları ve bunların çoğulunu; kişinin kendisi için varlık edinmesini, varlığının çoğalmasını ya da varlıklı duruma gelmesini ve başkasını varlık sahibi kılmasını birlikte aktarır. Göçebe toplulukların varlığının hayvan sürüleriyle somutlaşması bu çekirdeğin bağlama bağlı bir özelleşmesidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kişinin sahip olduğu değerli varlık"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kişinin sahip olduğu değerli varlıklar"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"göçebe toplulukların başlıca varlığı sayılan hayvan sürüleri"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"varlık sahibi veya çok varlıklı kimse"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kendine kalıcı varlık edinmek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"varlığı çoğalmak veya varlık sahibi duruma gelmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birini varlık sahibi yapmak veya ona değerli varlık vermek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"mal sözcüğünün küçültme biçimi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ne çok varlığı var!"}],"lexicalization_note":"Tanım, genel varlık ve varlık edinme çekirdeğini ayrı tutar; göçebe toplulukların hayvan sürülerini varlık sayan kullanımını yalnızca belirli bir söz öbeğine bağlı özelleşme olarak sınırlar.","neighbor_coverage_note":"Sekiz adayın tümü karşılaştırıldı. Edinme ve varlık artışıyla doğrudan sınır paylaşan üç aday yayımlandı; para yönetimi, belirli varlık türleri, geçim ve sürü adlandırmalarıyla yalnızca uzak alan ortaklığı kuran ötekiler dal sınırını keskinleştirmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın edinme görünümü komşuya yaklaşır, fakat odak daha geniş bir sahip olunan varlık ve varlıklılaşma ailesidir. Komşu ise edinimin amacı ve saklama biçimiyle sınırlı, daha özel bir sahiplik türünü belirtir.","focus_only":"Odak dal, sahip olunan varlığın adını, varlığın artmasını, varlıklı duruma gelmeyi ve başkasını varlık sahibi kılmayı da kapsar.","gloss":"kendisi için edinilen ve saklanan varlık","neighbor_only":"Komşu dal, kişinin kendisi için satış ve ticaret amacı dışında edindiği, gereksinim sonrasında sakladığı ya da temel dayanak yaptığı varlığa özgü koşullar taşır.","neighbor_ref":"root_001265/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin kendisi için değerli varlık edinmesi ve bunu sahipliğinde tutması alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşunun çekirdeği belirli bir mülk ve taşınmaz türüne yönelirken odak dal varlığın türünü sınırlandırmaz; ayrıca artış, varlıklı duruma geçiş ve ettirgen kazandırma anlamlarını içerir.","focus_only":"Odak dal taşınır ya da taşınmaz ayrımı yapmadan varlığı, varlık artışını ve başkasına varlık kazandırmayı kapsar.","gloss":"taşınmaz edinme ve elde tutma","neighbor_only":"Komşu dal özellikle taşınmazı, gelir getiren yeri ve bunları edinip kalıcı sahiplik konusu yapmayı öne çıkarır.","neighbor_ref":"root_001034/B004","relation_type":"near_synonym","shared_zone":"İki dal, değer taşıyan bir şeyi edinme ve kalıcı sahiplik altında bulundurma düşüncesinde birleşir."},{"boundary_match":"partial","distinction":"Örtüşme varlık artışıyla sınırlıdır. Odak dal sahiplik ve edinme ailesini kurarken komşu, büyüyen varlık ile onun bakımı ve artışına ilişkin değerlendirmeleri ayrı bir çekirdek yapar.","focus_only":"Odak dal varlığın genel adını, edinilmesini ve başkasının varlık sahibi yapılmasını da içerir.","gloss":"artan varlık ve onu iyi yönetme","neighbor_only":"Komşu dal büyüyen ya da çok olan varlığı, onun iyi yönetilmesini ve artması yönündeki iyi dileği özellikle öne çıkarır.","neighbor_ref":"root_000205/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da sahip olunan varlığın çokluğu veya artışı belirgin bir ortak alandır."}],"source_phrase_ar":"تمول الرجل اتخذ مالا؛ مال يمال كثر ماله (maqayis)؛ المال معروف وجمعه أموال؛ كانت أموال العرب أنعامهم؛ رجل مال أي ذو مال والفعل تمول (ayn)؛ مال الرجل يمول ويمال إذا صار ذا مال؛ تمول مثله؛ موله غيره (sihah)؛ مال أهل البادية النعم؛ تمول فلان مالا إذا اتخذ قنية من المال؛ ما أموله أي ما أكثر ماله (tahdhib)","source_summary":"Kaynakların toplu anlatımı, sahip olunan değerli varlıkları ve bunların çoğulunu temel alır; varlık edinme, varlığın çoğalması, varlıklı duruma gelme ve başkasını varlık sahibi kılma süreçlerini bu temel çevresinde birleştirir. Hayvan sürüleri göçebe topluluklara özgü somutlaşma, çokluk karşısındaki şaşma söyleyişi ise bağlı bir kullanım olarak aktarılır. Mal adının küçültme biçimi de ayrıca kaydedilir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه المال والأموال واتخاذ المال قنية وكثرة المال وصيرورة الرجل ذا مال وتمويل غيره ونعم أهل البادية","what_is_not_ar":"ليس للمولة العنكبوت ولا للميل عن الوسط ولا لميل الحائط"},"support_links":["sup_4f00fbc02ad26fa8a71d","sup_8af5d3e738e6144d04c0"]},{"boundary":"Dal, örümceğin özelliklerini tanımlamaz; yalnızca örümcek için aktarılan ve güvenilirliği açıkça tartışılan bir adlandırmayı temsil eder.","branch_kind":"unresolved","branch_ref":"root_001457/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:2:4:1","qac_word_ref":"111:2:4","surface_ar":"مَالُ"}],"gloss":"örümcek için tartışmalı bir ad","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcük, bazı sözlük aktarımlarında örümceği gösteren bir hayvan adı olarak verilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırmanın doğruluğu ve güvenilir aktarımı açıkça sorgulandığı için bu gönderim kesin kabul edilemez."}}],"root_ar":"م و ل","root_id":"root_001457","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözcüğün örümceğe gönderimi aktarılırken bu adlandırmanın güvenilirliğine ilişkin açık kuşkunun da korunması gereken her durumda uygundur.","boundary_detail":"Dal, örümceğin özelliklerini tanımlamaz; yalnızca örümcek için aktarılan ve güvenilirliği açıkça tartışılan bir adlandırmayı temsil eder.","branch_image_ar":"المُولة العنكبوت","concept_gloss":"örümcek için tartışmalı bir ad","contextual_glosses":[{"applicability":"Tartışmalı hayvan adının bir metinde doğrudan canlıya gönderim yaptığı bağlamda akıcı karşılık olarak kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bu adlandırmanın güvenilirliği ve yerleşikliği üzerindeki açık kaynak kuşkusunu görünmez kılar.","preserves":"Adlandırmanın gönderimde bulunduğu hayvanı doğru biçimde korur."},"facet_ids":["F001"],"text":"örümcek","usage_role":"contextual"}],"definition":"Örümceğe verilen bir ad olarak aktarılır; ancak bu adlandırmanın güvenilirliği kaynak anlatımının kendi içinde açıkça tartışmalıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcük, bazı sözlük aktarımlarında örümceği gösteren bir hayvan adı olarak verilir."},{"facet_id":"F002","role":"source_variant","statement":"Adlandırmanın doğruluğu ve güvenilir aktarımı açıkça sorgulandığı için bu gönderim kesin kabul edilemez."}],"identity_rationale":"Kaynak ifadesi sözcüğü örümceğe verilen bir ad olarak aktarır, fakat aynı ifadenin içinde bu aktarımın kuşkuyla karşılandığını ve güvenilir bir aktarıcıdan işitilmediğini de açıkça bildirir. Bu nedenle hayvanla kurulan bağ korunabilir, ancak yerleşik ve tartışmasız bir ad gibi sunulamaz.","lexicalization_note":"Kanıt, bu tartışmalı adlandırmanın bağımsız ve yerleşik bir yalın sözlük birimi olup olmadığını mekanik olarak çözmez; tanım bu yüzden yalın kullanım varsaymaz.","neighbor_coverage_note":"Dokuz adayın tümü değerlendirildi. Aynı canlıya yönelen iki adlandırma gerçek bir sınır karşılaştırması sağladı; öteki hayvan adları yalnızca geniş canlılar alanını paylaştı, varlık dalı ise ortak köke rağmen anlamsal örtüşme göstermedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Gönderim ortak olsa da odak dalın sözlüksel kimliği kuşkulu bir ad aktarımına bağlıdır. Komşu dal ise canlının doğrudan adını ve onu tanıtan özellikleri kapsadığı için iki adın kullanım sınırları tam olarak eşleşmez.","focus_only":"Odak dal, aynı canlıya yönelen fakat güvenilirliği açıkça tartışılan özel bir ad aktarımıdır.","gloss":"ağ ören örümcek","neighbor_only":"Komşu dal canlının olağan adını, ağ örme niteliğini, ad çeşitlerini ve dil bilgisel biçimlerini kapsar.","neighbor_ref":"root_001054/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın hayvansal gönderimi aynı canlıya, yani örümceğe yönelir."},{"boundary_match":"partial","distinction":"Odak dal yalnızca kuşkulu hayvan adı aktarımıyla sınırlıdır; komşu dalın kendi ayrı adı ve yuvayı gösteren bağlı kullanımı vardır. Bu ek kapsam ve odaktaki güvenilirlik çekincesi tam eşdeğerliği engeller.","focus_only":"Odak dalın örümcek adı sayılması kaynak anlatımında açık kuşku ve güven sorunu taşır.","gloss":"örümcek ve yuvası için özel ad","neighbor_only":"Komşu dal başka bir örümcek adının yanı sıra o örümceğin yuvasını gösteren bağlı bir söz öbeğini de kapsar.","neighbor_ref":"root_001326/B008","relation_type":"near_synonym","shared_zone":"İki dal da örümceğe verilen alışılmadık bir adlandırma üzerinden aynı canlıya gönderimde bulunur."}],"source_phrase_ar":"إن المولة العنكبوت وفيه نظر (maqayis)؛ المولة اسم العنكبوت (ayn)؛ زعم قوم أن المول العنكبوت الواحدة مولة ولم أسمعه عن ثقة (sihah)؛ هي العنكبوت والمولة (tahdhib)","source_summary":"Toplu kaynak kaydı sözcüğü örümceğin adı olarak aktarır, fakat aynı kayıtta bu eşleştirmenin kuşkulu olduğu ve güvenilir bir kaynaktan işitilmediği yönünde açık çekinceler bulunur. Bu yüzden hayvana gönderim ile aktarımın belirsizliği birlikte korunmalıdır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه إطلاق المولة أو المول على العنكبوت إذا ثبتت النسبة","what_is_not_ar":"ليس للمال والأموال ولا لاتخاذ القنية ولا لكثرة المال"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["111:2:1"],"branch_refs":[],"candidate_id":"cand_296e756cc6a78da4881b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:2:1:particle-polyvalence","source_type":"word_analysis","support_ids":["sup_1896817156e3f1edcce9","sup_bca1e092b9a9810ee26e"],"title":"negative and rhetorical-question readings converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:1","qac_refs":["111:2:1:1"],"status":"accepted"}},{"anchor_refs":["111:2:1"],"branch_refs":[],"candidate_id":"cand_badd1ba735898cff9b71","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:2:1:scope-over-resources","source_type":"word_analysis","support_ids":["sup_1396700b54fce1bac3bd","sup_1896817156e3f1edcce9"],"title":"opening futility scopes over both resources","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:1","qac_refs":["111:2:1:1"],"status":"accepted"}},{"anchor_refs":["111:2:1"],"branch_refs":[],"candidate_id":"cand_ece4049c1dddc461c25f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:2:1:sound-reprise","source_type":"word_analysis","support_ids":["sup_1896817156e3f1edcce9","sup_57c13d007f2571e19ec6"],"title":"long sound links the two beats","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:1","qac_refs":["111:2:1:1"],"status":"accepted"}},{"anchor_refs":["111:2:2"],"branch_refs":[],"candidate_id":"cand_33c6b4252782ce903726","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"111:2:2:formula-and-boundary","source_type":"word_analysis","support_ids":["sup_815147959c7bb6c3e3a1","sup_d24a1f8dc67d4aa6cc6f"],"title":"failed-availing formula links outward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:2","qac_refs":["111:2:2:1"],"status":"accepted"}},{"anchor_refs":["111:2:2"],"branch_refs":[],"candidate_id":"cand_224c446453e89a79a934","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"111:2:2:nonselected-root-images","source_type":"word_analysis","support_ids":["sup_0611080fea827302340d","sup_d24a1f8dc67d4aa6cc6f"],"title":"dwelling and song images remain background pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:2","qac_refs":["111:2:2:1"],"status":"accepted"}},{"anchor_refs":["111:2:2"],"branch_refs":[],"candidate_id":"cand_74ae6b3fd69959fb9e53","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"111:2:2:one-frame-two-resources","source_type":"word_analysis","support_ids":["sup_ad70ac02aa7fd171e841","sup_d24a1f8dc67d4aa6cc6f"],"title":"one failed predicate governs two resources","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:2","qac_refs":["111:2:2:1"],"status":"accepted"}},{"anchor_refs":["111:2:2"],"branch_refs":[],"candidate_id":"cand_998174225861cc9f0f64","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"111:2:2:protection-frame-and-ellipsis","source_type":"word_analysis","support_ids":["sup_5e75274f53515c9079fc","sup_d24a1f8dc67d4aa6cc6f"],"title":"availing frame denies any specified protection","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:2","qac_refs":["111:2:2:1"],"status":"accepted"}},{"anchor_refs":["111:2:2"],"branch_refs":[],"candidate_id":"cand_3fc74c9309cc320cabe3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"111:2:2:settled-negated-perfect","source_type":"word_analysis","support_ids":["sup_863285fa6099ef0f40fd","sup_d24a1f8dc67d4aa6cc6f"],"title":"perfect form makes failure settled","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:2","qac_refs":["111:2:2:1"],"status":"accepted"}},{"anchor_refs":["111:2:2"],"branch_refs":[],"candidate_id":"cand_48f7d732c117bd0dd61c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"111:2:2:sound-cadence","source_type":"word_analysis","support_ids":["sup_d24a1f8dc67d4aa6cc6f","sup_e44a378467c2c2cfe698"],"title":"sound binds negation, availing, and wealth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:2","qac_refs":["111:2:2:1"],"status":"accepted"}},{"anchor_refs":["111:2:2"],"branch_refs":[],"candidate_id":"cand_01d7f503506422a23059","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"111:2:2:sufficiency-root-field","source_type":"word_analysis","support_ids":["sup_4da48326739ae093651f","sup_d24a1f8dc67d4aa6cc6f"],"title":"root field tests human sufficiency through wealth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:2","qac_refs":["111:2:2:1"],"status":"accepted"}},{"anchor_refs":["111:2:3"],"branch_refs":[],"candidate_id":"cand_2c4177a45a046c1ff618","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:2:3:bound-form-and-sound","source_type":"word_analysis","support_ids":["sup_58ce518b3d39adc26dc5","sup_c0747cb56f01b30376a1"],"title":"bound form compresses relation and referent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:3","qac_refs":["111:2:3:1","111:2:3:2"],"status":"accepted"}},{"anchor_refs":["111:2:3"],"branch_refs":[],"candidate_id":"cand_3ec48f39e2cf0f87dea3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:2:3:placement-hinge","source_type":"word_analysis","support_ids":["sup_a47000b5f6ad54759288","sup_c0747cb56f01b30376a1"],"title":"exposed person appears before failed protector","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:3","qac_refs":["111:2:3:1","111:2:3:2"],"status":"accepted"}},{"anchor_refs":["111:2:3"],"branch_refs":[],"candidate_id":"cand_a2ea2e9e1471cd14b958","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:2:3:pronoun-chain","source_type":"word_analysis","support_ids":["sup_9fed24244f101e1195fb","sup_c0747cb56f01b30376a1"],"title":"suffix carries the prior referent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:3","qac_refs":["111:2:3:1","111:2:3:2"],"status":"accepted"}},{"anchor_refs":["111:2:3"],"branch_refs":[],"candidate_id":"cand_2df947598496918dc184","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:2:3:separation-protection-frame","source_type":"word_analysis","support_ids":["sup_09e226540d4df793add2","sup_c0747cb56f01b30376a1"],"title":"preposition frames failed shielding","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:3","qac_refs":["111:2:3:1","111:2:3:2"],"status":"accepted"}},{"anchor_refs":["111:2:4"],"branch_refs":[],"candidate_id":"cand_e79526c4350921c64650","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"111:2:4:concrete-aggregate-resource","source_type":"word_analysis","support_ids":["sup_068cc98752b54455d894","sup_339c1e42372d536f8413"],"title":"singular wealth gathers stored assets","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:4","qac_refs":["111:2:4:1","111:2:4:2"],"status":"accepted"}},{"anchor_refs":["111:2:4"],"branch_refs":[],"candidate_id":"cand_b4e0cf21dfdd1eefaef3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"111:2:4:delayed-failed-subject","source_type":"word_analysis","support_ids":["sup_2b10cbb99e486fdfa82b","sup_339c1e42372d536f8413"],"title":"wealth is the delayed failed actor","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:4","qac_refs":["111:2:4:1","111:2:4:2"],"status":"accepted"}},{"anchor_refs":["111:2:4"],"branch_refs":[],"candidate_id":"cand_3b3881a6955f41257329","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"111:2:4:failed-wealth-echoes","source_type":"word_analysis","support_ids":["sup_2c475f76849dc2c606f0","sup_339c1e42372d536f8413"],"title":"failed wealth echoes outward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:4","qac_refs":["111:2:4:1","111:2:4:2"],"status":"accepted"}},{"anchor_refs":["111:2:4"],"branch_refs":[],"candidate_id":"cand_0477795cf4fbeb72e9c7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"111:2:4:possession-acquisition-pair","source_type":"word_analysis","support_ids":["sup_339c1e42372d536f8413","sup_73ce84db345d29fbf7dc"],"title":"possession is paired with acquisition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:4","qac_refs":["111:2:4:1","111:2:4:2"],"status":"accepted"}},{"anchor_refs":["111:2:4"],"branch_refs":[],"candidate_id":"cand_953378dffd89c509787b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"111:2:4:possessive-referent-chain","source_type":"word_analysis","support_ids":["sup_018223a2b00475547d25","sup_339c1e42372d536f8413"],"title":"his wealth is tied to the exposed person","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:4","qac_refs":["111:2:4:1","111:2:4:2"],"status":"accepted"}},{"anchor_refs":["111:2:4"],"branch_refs":[],"candidate_id":"cand_d015882949ac689d68ef","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"111:2:4:root-instability-pressure","source_type":"word_analysis","support_ids":["sup_339c1e42372d536f8413","sup_d21ae611393fe3b826c9"],"title":"leaning image undercuts wealth as shield","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:4","qac_refs":["111:2:4:1","111:2:4:2"],"status":"accepted"}},{"anchor_refs":["111:2:4"],"branch_refs":[],"candidate_id":"cand_faefb120dd3a532fe89c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"111:2:4:sound-frame","source_type":"word_analysis","support_ids":["sup_339c1e42372d536f8413","sup_eee21d36f6edb5f2fbbc"],"title":"wealth thickens the repeated sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:4","qac_refs":["111:2:4:1","111:2:4:2"],"status":"accepted"}},{"anchor_refs":["111:2:5"],"branch_refs":[],"candidate_id":"cand_72e0ba753e79ab2158e6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:2:5:boundary-reprise","source_type":"word_analysis","support_ids":["sup_27496c06749b80fad932","sup_8cae8239eaa78db9468a"],"title":"conjunction repeats prior expansion logic","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:5","qac_refs":["111:2:5:1"],"status":"accepted"}},{"anchor_refs":["111:2:5"],"branch_refs":[],"candidate_id":"cand_ef631c84a993a3a1e044","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:2:5:coordination-under-negation","source_type":"word_analysis","support_ids":["sup_8cae8239eaa78db9468a","sup_df8e01b929734d24e4b2"],"title":"conjunction extends one negation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:5","qac_refs":["111:2:5:1"],"status":"accepted"}},{"anchor_refs":["111:2:5"],"branch_refs":[],"candidate_id":"cand_304be4c85534568e2c1f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:2:5:fused-continuation","source_type":"word_analysis","support_ids":["sup_44b295b51fd6d9f7f3d2","sup_8cae8239eaa78db9468a"],"title":"fused form blocks a restart","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:5","qac_refs":["111:2:5:1"],"status":"accepted"}},{"anchor_refs":["111:2:5"],"branch_refs":[],"candidate_id":"cand_8b2b1a2f6cbe2da02224","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:2:5:resource-expansion","source_type":"word_analysis","support_ids":["sup_8cae8239eaa78db9468a","sup_f03ec03ecf632f39dbb9"],"title":"wealth expands to all acquired gain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:5","qac_refs":["111:2:5:1"],"status":"accepted"}},{"anchor_refs":["111:2:6"],"branch_refs":[],"candidate_id":"cand_44bdbc88b9231d351e9c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:2:6:coordination-pivot","source_type":"word_analysis","support_ids":["sup_7635e8076545522de4c4","sup_fac7dba58eec1e75ac56"],"title":"coordination pivots into a clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:6","qac_refs":["111:2:5:2"],"status":"accepted"}},{"anchor_refs":["111:2:6"],"branch_refs":[],"candidate_id":"cand_72c02cd70dc8cc8847b3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:2:6:open-acquisition-field","source_type":"word_analysis","support_ids":["sup_1cc208080795ebcf0cec","sup_7635e8076545522de4c4"],"title":"open reference maximizes what was earned","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:6","qac_refs":["111:2:5:2"],"status":"accepted"}},{"anchor_refs":["111:2:6"],"branch_refs":[],"candidate_id":"cand_b70a8fadc68d5afec5ac","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:2:6:product-process-ambiguity","source_type":"word_analysis","support_ids":["sup_7635e8076545522de4c4","sup_ddd4c1316f35a7246a1a"],"title":"product reading dominates while process pressure survives","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:6","qac_refs":["111:2:5:2"],"status":"accepted"}},{"anchor_refs":["111:2:6"],"branch_refs":[],"candidate_id":"cand_7c163298a642556c3488","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:2:6:relative-nested-roles","source_type":"word_analysis","support_ids":["sup_7635e8076545522de4c4","sup_b9f814d248f4fa260469"],"title":"relative word is object inside and subject outside","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:6","qac_refs":["111:2:5:2"],"status":"accepted"}},{"anchor_refs":["111:2:6"],"branch_refs":[],"candidate_id":"cand_ff880fb6b8eab6f0cbe2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:2:6:sound-shift","source_type":"word_analysis","support_ids":["sup_4c054cce69a64f863c56","sup_7635e8076545522de4c4"],"title":"same sound changes grammatical work","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:6","qac_refs":["111:2:5:2"],"status":"accepted"}},{"anchor_refs":["111:2:7"],"branch_refs":[],"candidate_id":"cand_a5e600fc030b63020d07","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001296"],"scope":"focus_ayah","source_local_id":"111:2:7:closing-and-forward-pressure","source_type":"word_analysis","support_ids":["sup_bde409e63401072efd9c","sup_e7a6ea878b640967923f"],"title":"final verb tightens toward the next verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:7","qac_refs":["111:2:6:1"],"status":"accepted"}},{"anchor_refs":["111:2:7"],"branch_refs":[],"candidate_id":"cand_a709f13f6d33564a4ef5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001296"],"scope":"focus_ayah","source_local_id":"111:2:7:completed-simple-form","source_type":"word_analysis","support_ids":["sup_43755c26f9734daaf34f","sup_bde409e63401072efd9c"],"title":"perfect Form I closes acquisition as judged","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:7","qac_refs":["111:2:6:1"],"status":"accepted"}},{"anchor_refs":["111:2:7"],"branch_refs":[],"candidate_id":"cand_d1ca14918a5ec7de7125","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001296"],"scope":"focus_ayah","source_local_id":"111:2:7:hidden-earner-agency","source_type":"word_analysis","support_ids":["sup_32d9373290eed28dde11","sup_bde409e63401072efd9c"],"title":"hidden subject makes the owner active earner","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:7","qac_refs":["111:2:6:1"],"status":"accepted"}},{"anchor_refs":["111:2:7"],"branch_refs":[],"candidate_id":"cand_ddb4436d01275abfa4b5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001296"],"scope":"focus_ayah","source_local_id":"111:2:7:material-and-moral-acquisition","source_type":"word_analysis","support_ids":["sup_bde409e63401072efd9c","sup_f465b8b3ed43509d0f4a"],"title":"earning includes gain and liability","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:7","qac_refs":["111:2:6:1"],"status":"accepted"}},{"anchor_refs":["111:2:7"],"branch_refs":[],"candidate_id":"cand_35b565e4e61a53b8361e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001296"],"scope":"focus_ayah","source_local_id":"111:2:7:open-earned-object","source_type":"word_analysis","support_ids":["sup_0301df50f5c24ffcf056","sup_bde409e63401072efd9c"],"title":"open object makes acquisition totalizing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:7","qac_refs":["111:2:6:1"],"status":"accepted"}},{"anchor_refs":["111:2:7"],"branch_refs":[],"candidate_id":"cand_f1f9c782aad46070a469","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001296"],"scope":"focus_ayah","source_local_id":"111:2:7:resource-pairing","source_type":"word_analysis","support_ids":["sup_bde409e63401072efd9c","sup_d00e6b9f8786cf53cb38"],"title":"earned gain joins wealth under failed sufficiency","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:7","qac_refs":["111:2:6:1"],"status":"accepted"}},{"anchor_refs":["111:2:7"],"branch_refs":[],"candidate_id":"cand_5b996293513ee211c95d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001296"],"scope":"focus_ayah","source_local_id":"111:2:7:sound-closure","source_type":"word_analysis","support_ids":["sup_82f9b179812d524bab8e","sup_bde409e63401072efd9c"],"title":"compact ending gives acquisition a clipped landing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:7","qac_refs":["111:2:6:1"],"status":"accepted"}},{"anchor_refs":["111:2:7"],"branch_refs":[],"candidate_id":"cand_7b16910dcc4fe856847a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001296"],"scope":"focus_ayah","source_local_id":"111:2:7:variant-and-concrete-pressure","source_type":"word_analysis","support_ids":["sup_bde409e63401072efd9c","sup_fa5febb847a79a0c46ec"],"title":"deliberate acquisition colors the surface verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:2:7","qac_refs":["111:2:6:1"],"status":"accepted"}},{"anchor_refs":["111:2:2"],"branch_refs":[],"candidate_id":"cand_176aeb2627de25792610","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"111:2:2:1","source_type":"qac_morpheme","support_ids":["sup_b369e925e3e454045b07"],"title":"QAC root occurrence: غ ن ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["111:2:4"],"branch_refs":[],"candidate_id":"cand_3035370842d62b05e845","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"111:2:4:1","source_type":"qac_morpheme","support_ids":["sup_17655e6439a4462c3ba2"],"title":"QAC root occurrence: م و ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["111:2:6"],"branch_refs":[],"candidate_id":"cand_02cb0347bca81e987a86","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001296"],"scope":"focus_ayah","source_local_id":"111:2:6:1","source_type":"qac_morpheme","support_ids":["sup_1afa35958ef8accfd044"],"title":"QAC root occurrence: ك س ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["111:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"111:2","branch_refs":["root_001110/B001","root_001457/B001"],"candidate_id":"cand_83db1874cff5e496c72e","commentary_obligation":"review","hft_ref":"hft_20be9628e18f1d180c6d","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_failed_insulation","source_type":"hft","support_ids":["sup_4f00fbc02ad26fa8a71d"],"title":"baseline_failed_insulation","trust":"legacy_unbound"},{"anchor_refs":["111:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"111:2","branch_refs":["root_001110/B002","root_001296/B001","root_001457/B001"],"candidate_id":"cand_5d7bed8ee6cb087f5c69","commentary_obligation":"review","hft_ref":"hft_20e1a5c4c68b0dc15fcc","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_stock_flow_substitution","source_type":"hft","support_ids":["sup_8af5d3e738e6144d04c0"],"title":"baseline_stock_flow_substitution","trust":"legacy_unbound"},{"anchor_refs":["111:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"111:2","branch_refs":["root_001110/B002","root_001296/B002"],"candidate_id":"cand_1aed28b6ee13f6e80f94","commentary_obligation":"review","hft_ref":"hft_7d1e8adb8062d573e431","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_outward_gain_network","source_type":"hft","support_ids":["sup_c7fb5e5f2013ea90882e"],"title":"baseline_outward_gain_network","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ","qac_morphemes":[{"lemma_ar":"مَا","morph_features":"STEM|POS:NEG|LEM:maA","morpheme_role":"STEM","pos":"NEG","qac_ref":"111:2:1:1","qac_word_ref":"111:2:1","root_ar":"","surface_ar":"مَآ"},{"lemma_ar":"أَغْنَىٰ","morph_features":"STEM|POS:V|PERF|LEM:>agonaY`|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"111:2:2:1","qac_word_ref":"111:2:2","root_ar":"غ ن ي","surface_ar":"أَغْنَىٰ"},{"lemma_ar":"عَن","morph_features":"STEM|POS:P|LEM:Ean","morpheme_role":"STEM","pos":"P","qac_ref":"111:2:3:1","qac_word_ref":"111:2:3","root_ar":"","surface_ar":"عَنْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"111:2:3:2","qac_word_ref":"111:2:3","root_ar":"","surface_ar":"هُ"},{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:2:4:1","qac_word_ref":"111:2:4","root_ar":"م و ل","surface_ar":"مَالُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"111:2:4:2","qac_word_ref":"111:2:4","root_ar":"","surface_ar":"هُۥ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"111:2:5:1","qac_word_ref":"111:2:5","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:REL|LEM:maA","morpheme_role":"STEM","pos":"REL","qac_ref":"111:2:5:2","qac_word_ref":"111:2:5","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"كَسَبَ","morph_features":"STEM|POS:V|PERF|LEM:kasaba|ROOT:ksb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"111:2:6:1","qac_word_ref":"111:2:6","root_ar":"ك س ب","surface_ar":"كَسَبَ"}],"word_analysis_qac_refs":[["111:2:1:1"],["111:2:2:1"],["111:2:3:1","111:2:3:2"],["111:2:4:1","111:2:4:2"],["111:2:5:1"],["111:2:5:2"],["111:2:6:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["111:2:1","111:2:2","111:2:3","111:2:4","111:2:5","111:2:6","111:2:7"]},"focus_surface_evidence":{"arabic_uthmani":"مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ","qac_morphemes":[{"lemma_ar":"مَا","morph_features":"STEM|POS:NEG|LEM:maA","morpheme_role":"STEM","pos":"NEG","qac_ref":"111:2:1:1","qac_word_ref":"111:2:1","root_ar":"","surface_ar":"مَآ"},{"lemma_ar":"أَغْنَىٰ","morph_features":"STEM|POS:V|PERF|LEM:>agonaY`|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"111:2:2:1","qac_word_ref":"111:2:2","root_ar":"غ ن ي","surface_ar":"أَغْنَىٰ"},{"lemma_ar":"عَن","morph_features":"STEM|POS:P|LEM:Ean","morpheme_role":"STEM","pos":"P","qac_ref":"111:2:3:1","qac_word_ref":"111:2:3","root_ar":"","surface_ar":"عَنْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"111:2:3:2","qac_word_ref":"111:2:3","root_ar":"","surface_ar":"هُ"},{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:2:4:1","qac_word_ref":"111:2:4","root_ar":"م و ل","surface_ar":"مَالُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"111:2:4:2","qac_word_ref":"111:2:4","root_ar":"","surface_ar":"هُۥ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"111:2:5:1","qac_word_ref":"111:2:5","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:REL|LEM:maA","morpheme_role":"STEM","pos":"REL","qac_ref":"111:2:5:2","qac_word_ref":"111:2:5","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"كَسَبَ","morph_features":"STEM|POS:V|PERF|LEM:kasaba|ROOT:ksb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"111:2:6:1","qac_word_ref":"111:2:6","root_ar":"ك س ب","surface_ar":"كَسَبَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["111:2:1:1"],["111:2:2:1"],["111:2:3:1","111:2:3:2"],["111:2:4:1","111:2:4:2"],["111:2:5:1"],["111:2:5:2"],["111:2:6:1"]],"word_analysis_refs":["111:2:1","111:2:2","111:2:3","111:2:4","111:2:5","111:2:6","111:2:7"],"word_rows":[{"analysis_record_ref":"111:2:1","analytic_gloss_range_en":"opening particle of futility, locally negative or rhetorical-interrogative, scoping the whole availing clause and its two resource subjects","analytic_root_gloss_range_en":null,"qac_refs":["111:2:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"مَآ","transliteration":"mā"}},{"analysis_record_ref":"111:2:2","analytic_gloss_range_en":"negated Form IV availing or making sufficient in a protection frame, with no explicit direct object and with the affected person expressed through the following prepositional complement","analytic_root_gloss_range_en":"self-sufficiency, wealth, sufficing and availing are the relevant local branches; song, dwelling, and marriage-related branches remain nonselected background images or contrasts when pressed by CRITICAL rows","qac_refs":["111:2:2:1"],"root":{"arabic":"غ ن ي","transliteration":"gh-n-y"},"surface":{"arabic":"أَغْنَىٰ","transliteration":"aghnā"}},{"analysis_record_ref":"111:2:3","analytic_gloss_range_en":"governed prepositional complement meaning availing or protection for/against the prior masculine referent, with separation imagery and a bound 3ms suffix","analytic_root_gloss_range_en":null,"qac_refs":["111:2:3:1","111:2:3:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"عَنْهُ","transliteration":"ʿanhu"}},{"analysis_record_ref":"111:2:4","analytic_gloss_range_en":"his concrete wealth or possessed property, definite by suffix and functioning as the delayed subject that fails to avail","analytic_root_gloss_range_en":"wealth, property, possession, and acquisition of wealth are locally relevant; any leaning or swaying image remains a narrowed etymological pressure, not the selected noun sense","qac_refs":["111:2:4:1","111:2:4:2"],"root":{"arabic":"م و ل","transliteration":"m-w-l"},"surface":{"arabic":"مَالُهُۥ","transliteration":"māluhū"}},{"analysis_record_ref":"111:2:5","analytic_gloss_range_en":"coordinating conjunction joining the earned-gain phrase to wealth under the same negation, functioning locally like a neither/nor extension rather than a restart","analytic_root_gloss_range_en":null,"qac_refs":["111:2:5:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"111:2:6","analytic_gloss_range_en":"relative pronoun introducing an open earned object and forming a free-relative subject phrase coordinated with wealth; masdar-style product/process pressure is possible but secondary to the local relative parse","analytic_root_gloss_range_en":null,"qac_refs":["111:2:5:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"مَا","transliteration":"mā"}},{"analysis_record_ref":"111:2:7","analytic_gloss_range_en":"Form I perfect earning or acquisition, with the relative pronoun as its open object and an implicit 3ms subject tied to the prior referent","analytic_root_gloss_range_en":"earning, gaining, acquiring, seeking benefit, and incurring liability are relevant; causative gain-for-another, hunting-creature, and substance-name branches are not locally selected","qac_refs":["111:2:6:1"],"root":{"arabic":"ك س ب","transliteration":"k-s-b"},"surface":{"arabic":"كَسَبَ","transliteration":"kasaba"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":7,"words_total":7,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["111:2"],"branch_refs":["root_001110/B001","root_001457/B001"],"candidate_id":"cand_83db1874cff5e496c72e","evidence_scope":"focus_ayah","hft_ref":"hft_20be9628e18f1d180c6d","item_id":"baseline_failed_insulation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_failed_insulation","support_id":"sup_4f00fbc02ad26fa8a71d"},{"anchor_refs":["111:2"],"branch_refs":["root_001110/B002","root_001296/B001","root_001457/B001"],"candidate_id":"cand_5d7bed8ee6cb087f5c69","evidence_scope":"focus_ayah","hft_ref":"hft_20e1a5c4c68b0dc15fcc","item_id":"baseline_stock_flow_substitution","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_stock_flow_substitution","support_id":"sup_8af5d3e738e6144d04c0"},{"anchor_refs":["111:2"],"branch_refs":["root_001110/B002","root_001296/B002"],"candidate_id":"cand_1aed28b6ee13f6e80f94","evidence_scope":"focus_ayah","hft_ref":"hft_7d1e8adb8062d573e431","item_id":"baseline_outward_gain_network","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_outward_gain_network","support_id":"sup_c7fb5e5f2013ea90882e"}],"diagnostics":[],"lane_counts":{"global":9,"macro":12,"micro":3},"packet_summary":{"ayah_count":5,"focus_ref":"111:2","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ي د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001693","furuq_root_norm":"ي د ي","furuq_source_root_norm":"ي د ي","is_dominant":true,"target_occurrences":107,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000071","furuq_root_norm":"ء ي د","furuq_source_root_norm":"أ ي د","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]}],"window":["111:1","111:2","111:3","111:4","111:5"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"111:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"111:2","lane":"micro","linguistic_source_ref":"111:2","surface_ref":"111:2","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"111:2","target_tokens":[["Malı",["111:2:4"]],["ve",["111:2:5"]],["kazandığı",["111:2:6"]],["şey",["111:2:5"]],["ona",["111:2:3"]],["yarar",["111:2:2"]],["sağlamadı",["111:2:1","111:2:2"]]],"text":"Malı ve kazandığı şey ona yarar sağlamadı."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":5,"id":"s111-p01-001-005","label":"Whole surah","number":1,"refs":["111:1","111:2","111:3","111:4","111:5"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:4:possessive-referent-chain","source_type":"word_analysis","support_id":"sup_018223a2b00475547d25","text":"{\"blocking_evidence\":null,\"headline\":\"his wealth is tied to the exposed person\",\"reader_payoff\":\"The reader notices that the failed wealth is not generic wealth but the very wealth of the person already exposed by the pronoun chain.\",\"reason\":\"QAC and attachment evidence identify the suffix as possessive and linked to the same masculine discourse participant.\",\"representative_source_ids\":[\"QG-3ca2daa5\",\"QG-6297b6b8\",\"QF-47ae4413\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:7:open-earned-object","source_type":"word_analysis","support_id":"sup_0301df50f5c24ffcf056","text":"{\"blocking_evidence\":null,\"headline\":\"open object makes acquisition totalizing\",\"reader_payoff\":\"The reader notices that the verb does not itemize the acquired object, so the failed category remains broad and exhaustive.\",\"reason\":\"QAC and attachment evidence identify the relative pronoun as the object of the earning verb, preserving open reference rather than a separately named object.\",\"representative_source_ids\":[\"QG-d0a6e40d\",\"QT-0c683ffa\",\"QY-34a5f399\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:2:nonselected-root-images","source_type":"word_analysis","support_id":"sup_0611080fea827302340d","text":"{\"blocking_evidence\":null,\"headline\":\"dwelling and song images remain background pressure\",\"reader_payoff\":\"The reader notices a narrowed image of lost rootedness or fullness while the local verb still means availing or making sufficient.\",\"reason\":\"V4 separates dwelling and song as distinct branches, so they should not be activated as local meanings; they survive only as limited root-family pressure from the CRITICAL rows.\",\"representative_source_ids\":[\"QS-4ac396f4\",\"QS-c10fa24a\",\"MS-a1ca9b7b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:4:concrete-aggregate-resource","source_type":"word_analysis","support_id":"sup_068cc98752b54455d894","text":"{\"blocking_evidence\":null,\"headline\":\"singular wealth gathers stored assets\",\"reader_payoff\":\"The reader notices that a whole concrete store of property is gathered into one failed subject before the wording widens to earned gain.\",\"reason\":\"QAC and V4 support wealth or property as the local noun range, and the singular possessed form gathers the resource as one unit.\",\"representative_source_ids\":[\"QS-501bc4b6\",\"QF-43bf3fd1\",\"QS-7af835c9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:3:separation-protection-frame","source_type":"word_analysis","support_id":"sup_09e226540d4df793add2","text":"{\"blocking_evidence\":null,\"headline\":\"preposition frames failed shielding\",\"reader_payoff\":\"The reader notices that the phrase concerns failed protection or availing against exposure, not merely a generic benefit granted to him.\",\"reason\":\"QAC and attachment evidence treat the word as the governed complement of the availing verb, with the affected participant expressed through the prepositional phrase.\",\"representative_source_ids\":[\"QG-6fc08934\",\"QG-cec9f13a\",\"QS-3cfb876c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:1:scope-over-resources","source_type":"word_analysis","support_id":"sup_1396700b54fce1bac3bd","text":"{\"blocking_evidence\":null,\"headline\":\"opening futility scopes over both resources\",\"reader_payoff\":\"The reader notices that failure is the starting frame and that both wealth and earned gain are judged inside it.\",\"reason\":\"QAC and attachment evidence place the opening particle over the one negated verbal clause whose subjects are the named wealth and the coordinated earned-gain phrase.\",\"representative_source_ids\":[\"QG-2b5058da\",\"QT-5406d18c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"111:2:4:1","source_type":"qac_morpheme","support_id":"sup_17655e6439a4462c3ba2","text":"{\"lemma_ar\":\"مَال\",\"morph_features\":\"STEM|POS:N|LEM:maAl|ROOT:mwl|M|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"111:2:4:1\",\"qac_word_ref\":\"111:2:4\",\"root_ar\":\"م و ل\",\"surface_ar\":\"مَالُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:1","source_type":"word_analysis","support_id":"sup_1896817156e3f1edcce9","text":"{\"gloss_range\":\"opening particle of futility, locally negative or rhetorical-interrogative, scoping the whole availing clause and its two resource subjects\",\"prose\":\"{{ar:مَآ}} ({{tr:mā}}) makes futility arrive before any resource is named. It can be heard as direct negation or as a rhetorical question whose answer is nothing; the possible exclamatory pressure is best kept as evaluative force rather than as the controlling parse. Because the particle opens the clause, both the named wealth and the later earned-gain phrase remain under the same failed-availing frame. Its long sound also returns inside the ayah, so the reader hears one compact particle bind the two beats while the grammar shifts at the second occurrence.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مَآ}} ({{tr:mā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"111:2:6:1","source_type":"qac_morpheme","support_id":"sup_1afa35958ef8accfd044","text":"{\"lemma_ar\":\"كَسَبَ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:kasaba|ROOT:ksb|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"111:2:6:1\",\"qac_word_ref\":\"111:2:6\",\"root_ar\":\"ك س ب\",\"surface_ar\":\"كَسَبَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:6:open-acquisition-field","source_type":"word_analysis","support_id":"sup_1cc208080795ebcf0cec","text":"{\"blocking_evidence\":null,\"headline\":\"open reference maximizes what was earned\",\"reader_payoff\":\"The reader notices that the wording avoids naming a specific acquired thing so the failed category can include every kind of gain.\",\"reason\":\"The local relative pronoun supplies an unspecified object, and translation support warns that the coordinated free relative must remain under the same negated frame.\",\"representative_source_ids\":[\"MG-ac0158d2\",\"QS-3a213a3c\",\"QS-70795473\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:5:boundary-reprise","source_type":"word_analysis","support_id":"sup_27496c06749b80fad932","text":"{\"blocking_evidence\":null,\"headline\":\"conjunction repeats prior expansion logic\",\"reader_payoff\":\"The reader notices the same connective expansion operating across the move from 111:1 into the resource list of 111:2.\",\"reason\":\"The boundary rows give concrete 111:1 and 111:2 evidence for repeated conjunctional expansion, while local syntax keeps this instance coordinated inside the negated clause.\",\"representative_source_ids\":[\"QE-f6eb72e2\",\"QB-1a72e7f2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:4:delayed-failed-subject","source_type":"word_analysis","support_id":"sup_2b10cbb99e486fdfa82b","text":"{\"blocking_evidence\":null,\"headline\":\"wealth is the delayed failed actor\",\"reader_payoff\":\"The reader notices wealth being grammatically cast as the actor that should have availed, making its failure more pointed.\",\"reason\":\"Attachment evidence marks the noun as the explicit subject of the negated availing verb, delayed after the verb and prepositional phrase.\",\"representative_source_ids\":[\"QG-7c98d789\",\"QS-1f768099\",\"QT-e9ce5df0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:4:failed-wealth-echoes","source_type":"word_analysis","support_id":"sup_2c475f76849dc2c606f0","text":"{\"blocking_evidence\":null,\"headline\":\"failed wealth echoes outward\",\"reader_payoff\":\"The reader notices that this named wealth is part of a wider failed-resource pattern and is linked to the surah's surrounding ruin imagery.\",\"reason\":\"The CRITICAL rows supply concrete links to failed wealth in 69:28 and to the surah boundary material in 111:1 and 111:4.\",\"representative_source_ids\":[\"QI-ccc464de\",\"MI-47de8ae9\",\"QB-dc2b2ba3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:7:hidden-earner-agency","source_type":"word_analysis","support_id":"sup_32d9373290eed28dde11","text":"{\"blocking_evidence\":null,\"headline\":\"hidden subject makes the owner active earner\",\"reader_payoff\":\"The reader notices the shift from wealth as failed actor to the owner himself re-entering as the covert agent of acquisition.\",\"reason\":\"Attachment evidence marks an implicit 3ms subject compatible with the same discourse participant resumed by the suffixes.\",\"representative_source_ids\":[\"QG-5379879c\",\"QG-bdf70a6f\",\"QS-b70eb4df\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:4","source_type":"word_analysis","support_id":"sup_339c1e42372d536f8413","text":"{\"gloss_range\":\"his concrete wealth or possessed property, definite by suffix and functioning as the delayed subject that fails to avail\",\"prose\":\"{{ar:مَالُهُۥ}} ({{tr:māluhū}}) finally names the supposed protector, but grammar gives it the role of subject only after failure and exposure have already been heard. The suffix makes the wealth specifically his, tying possessor and exposed beneficiary to the same referent from 111:1. The singular noun gathers the whole property mass into one bounded resource, including tangible goods and livestock-like movable wealth, then the next phrase expands beyond stored possession to what was acquired. CRITICAL rows about leaning or swaying are best kept as narrowed image-pressure: the local sense is wealth, but the image sharpens the irony of a resource asked to stand firm and unable to do so. The failed-wealth motif also resonates with 69:28 and moves toward the household fire imagery of 111:4.\",\"root_display\":\"{{ar:م و ل}} ({{tr:m-w-l}})\",\"root_gloss_range\":\"wealth, property, possession, and acquisition of wealth are locally relevant; any leaning or swaying image remains a narrowed etymological pressure, not the selected noun sense\",\"surface_display\":\"{{ar:مَالُهُۥ}} ({{tr:māluhū}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:7:completed-simple-form","source_type":"word_analysis","support_id":"sup_43755c26f9734daaf34f","text":"{\"blocking_evidence\":null,\"headline\":\"perfect Form I closes acquisition as judged\",\"reader_payoff\":\"The reader notices ordinary acquisition in completed aspect, not intensified earning or an ongoing habit.\",\"reason\":\"QAC gives a Form I perfect verb, and contextual evidence distinguishes the local perfect from broader perfect/imperfect distribution.\",\"representative_source_ids\":[\"QG-a256fbf8\",\"QF-76ca2f22\",\"QF-82f89192\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:5:fused-continuation","source_type":"word_analysis","support_id":"sup_44b295b51fd6d9f7f3d2","text":"{\"blocking_evidence\":null,\"headline\":\"fused form blocks a restart\",\"reader_payoff\":\"The reader notices that the connector and relative word flow as one continuation into the second subject.\",\"reason\":\"The form and recitation rows align with the local syntax, where the second phrase is attached to the first subject under one predicate.\",\"representative_source_ids\":[\"QF-058e8881\",\"QF-f913f3a0\",\"QP-d12d40e6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:6:sound-shift","source_type":"word_analysis","support_id":"sup_4c054cce69a64f863c56","text":"{\"blocking_evidence\":null,\"headline\":\"same sound changes grammatical work\",\"reader_payoff\":\"The reader notices the repeated sound binding the ayah while the second occurrence performs a different grammatical function.\",\"reason\":\"The sound rows are supported by the visible repeated form, while QAC distinguishes the first particle from this relative pronoun.\",\"representative_source_ids\":[\"QE-320cd740\",\"QE-e8521049\",\"QP-3e276326\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:2:sufficiency-root-field","source_type":"word_analysis","support_id":"sup_4da48326739ae093651f","text":"{\"blocking_evidence\":null,\"headline\":\"root field tests human sufficiency through wealth\",\"reader_payoff\":\"The reader notices that the word denies not only a useful transaction but the whole expected state of resource-based sufficiency.\",\"reason\":\"The wealth and sufficiency branches are locally coherent with the verb and its subject; non-surface self-sufficiency forms and proper-name contrast are kept as contrastive pressure, not as replacement senses.\",\"representative_source_ids\":[\"QS-1f39d897\",\"QS-2b2187b2\",\"QS-c4ac6f03\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:1:sound-reprise","source_type":"word_analysis","support_id":"sup_57c13d007f2571e19ec6","text":"{\"blocking_evidence\":null,\"headline\":\"long sound links the two beats\",\"reader_payoff\":\"The reader notices that the tiny opening particle is acoustically weighty and returns later with a different grammatical job.\",\"reason\":\"The source rows tie the written long opening and the later repeated sound to the ayah's two-beat resource structure.\",\"representative_source_ids\":[\"QF-bbab6046\",\"QE-8425e91f\",\"QP-62e75580\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:3:bound-form-and-sound","source_type":"word_analysis","support_id":"sup_58ce518b3d39adc26dc5","text":"{\"blocking_evidence\":null,\"headline\":\"bound form compresses relation and referent\",\"reader_payoff\":\"The reader notices how a small bound form joins the relation of failed shielding to the person and then echoes into the possessive suffix.\",\"reason\":\"The rows describe form and sound effects that align with the local syntax and repeated suffix chain.\",\"representative_source_ids\":[\"QF-2f88f45f\",\"QF-c8cb03f0\",\"QP-88f4791b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:2:protection-frame-and-ellipsis","source_type":"word_analysis","support_id":"sup_5e75274f53515c9079fc","text":"{\"blocking_evidence\":null,\"headline\":\"availing frame denies any specified protection\",\"reader_payoff\":\"The reader notices that the verb is not just about wealth helping in general; it tests whether wealth could shield or suffice for him in any unstated measure.\",\"reason\":\"Attachment evidence gives the governed prepositional complement and no direct object, while V4 includes the availing and sufficing construction for this root.\",\"representative_source_ids\":[\"QG-83fcea81\",\"QG-ba17e5e2\",\"QF-8cd39340\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:4:possession-acquisition-pair","source_type":"word_analysis","support_id":"sup_73ce84db345d29fbf7dc","text":"{\"blocking_evidence\":null,\"headline\":\"possession is paired with acquisition\",\"reader_payoff\":\"The reader notices an ordered resource pair: what he has and what he acquired both fail under the same predicate.\",\"reason\":\"Attachment evidence coordinates the later relative phrase with this noun as a second subject under the same negated verb.\",\"representative_source_ids\":[\"QI-91268630\",\"QT-6cd94e89\",\"QS-97ec2be5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:6","source_type":"word_analysis","support_id":"sup_7635e8076545522de4c4","text":"{\"gloss_range\":\"relative pronoun introducing an open earned object and forming a free-relative subject phrase coordinated with wealth; masdar-style product/process pressure is possible but secondary to the local relative parse\",\"prose\":\"{{ar:مَا}} ({{tr:mā}}) is not the opening negator repeated with the same job. Here it introduces the earned item as an open relative object inside the clause, while the whole relative phrase becomes the second subject under the failed-availing verb. That double role lets the wording treat acquisition as both acted-on gain and a resource that fails. The open reference refuses to specify money, status, offspring, reputation, or deeds, so all acquired categories can be swept in. A masdar-style reading can add process pressure, but local attachment evidence keeps the relative-object parse primary. The repeated sound ties the second beat back to the opening while forcing the reader to track a real grammatical shift.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مَا}} ({{tr:mā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:2:formula-and-boundary","source_type":"word_analysis","support_id":"sup_815147959c7bb6c3e3a1","text":"{\"blocking_evidence\":null,\"headline\":\"failed-availing formula links outward\",\"reader_payoff\":\"The reader notices that this personal condemnation participates in a broader failed-reliance formula and prepares the next ayah's consequence.\",\"reason\":\"The CRITICAL rows give concrete parallels and the local attachment evidence supports the failed-availing construction; any commentary mention should keep the references explicit (7:48, 11:101, 15:84, 39:50, 111:3).\",\"representative_source_ids\":[\"QI-bafdd5ca\",\"MI-21b352a9\",\"QE-e870c6a6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:7:sound-closure","source_type":"word_analysis","support_id":"sup_82f9b179812d524bab8e","text":"{\"blocking_evidence\":null,\"headline\":\"compact ending gives acquisition a clipped landing\",\"reader_payoff\":\"The reader notices the shorter second beat tightening into the final acquisition verb.\",\"reason\":\"The sound rows are coherent with the final word position and compact second beat; they remain secondary to the lexical and syntactic topics.\",\"representative_source_ids\":[\"QP-2a931220\",\"QP-631e9bca\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:2:settled-negated-perfect","source_type":"word_analysis","support_id":"sup_863285fa6099ef0f40fd","text":"{\"blocking_evidence\":null,\"headline\":\"perfect form makes failure settled\",\"reader_payoff\":\"The reader notices that the verb presents the collapse of availing as already established, not merely pending.\",\"reason\":\"QAC marks the verb as perfect, and the contextual profile shows this root-form is frequently negated in scoped availing contexts.\",\"representative_source_ids\":[\"QG-3c04c144\",\"QG-7bb85284\",\"QI-e1d199e0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:5","source_type":"word_analysis","support_id":"sup_8cae8239eaa78db9468a","text":"{\"gloss_range\":\"coordinating conjunction joining the earned-gain phrase to wealth under the same negation, functioning locally like a neither/nor extension rather than a restart\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) does the expansion work. It prevents the following earned-gain phrase from becoming a new sentence or a mere restatement of wealth; instead, it makes a second subject share the same negated availing predicate. In the negative setting its force is effectively neither/nor: not his wealth, and not what he earned. The fused sound with the following relative word keeps the second beat attached, and the boundary rows show the same conjunctional expansion continuing the movement from 111:1 into 111:2: from hands to person, then from wealth to all earning.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:3:pronoun-chain","source_type":"word_analysis","support_id":"sup_9fed24244f101e1195fb","text":"{\"blocking_evidence\":null,\"headline\":\"suffix carries the prior referent\",\"reader_payoff\":\"The reader notices that the ayah does not restart with an unnamed person; the bound suffix keeps the prior condemned figure grammatically present.\",\"reason\":\"Attachment evidence links the 3ms suffix to the prior proper-name span in 111:1.\",\"representative_source_ids\":[\"QG-031525bb\",\"QB-5fd10f63\",\"QY-ecd9e643\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:3:placement-hinge","source_type":"word_analysis","support_id":"sup_a47000b5f6ad54759288","text":"{\"blocking_evidence\":null,\"headline\":\"exposed person appears before failed protector\",\"reader_payoff\":\"The reader notices the experiential order: failure and exposure are heard before the asset that was supposed to protect him.\",\"reason\":\"The local word order places this prepositional phrase between the negated verb and the delayed subject.\",\"representative_source_ids\":[\"MG-bef59e2f\",\"QT-35d3aba2\",\"QT-a01f6dd9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:2:one-frame-two-resources","source_type":"word_analysis","support_id":"sup_ad70ac02aa7fd171e841","text":"{\"blocking_evidence\":null,\"headline\":\"one failed predicate governs two resources\",\"reader_payoff\":\"The reader notices that wealth and earned gain do not receive separate verdicts; one negated verb governs both.\",\"reason\":\"Attachment evidence analyzes the ayah as one verbal clause with the named wealth and the coordinated relative phrase as subjects under the same predicate.\",\"representative_source_ids\":[\"QT-5b4ba539\",\"QT-69c7c1a8\",\"QT-97ee5064\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"111:2:2:1","source_type":"qac_morpheme","support_id":"sup_b369e925e3e454045b07","text":"{\"lemma_ar\":\"أَغْنَىٰ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:>agonaY`|ROOT:gny|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"111:2:2:1\",\"qac_word_ref\":\"111:2:2\",\"root_ar\":\"غ ن ي\",\"surface_ar\":\"أَغْنَىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:6:relative-nested-roles","source_type":"word_analysis","support_id":"sup_b9f814d248f4fa260469","text":"{\"blocking_evidence\":null,\"headline\":\"relative word is object inside and subject outside\",\"reader_payoff\":\"The reader notices that a small relative word turns an earning clause into a resource subject while still serving as the verb's object inside that clause.\",\"reason\":\"QAC and attachment evidence identify the word as the relative pronoun/object of the earning verb and the relative phrase as coordinated subject of the negated availing verb.\",\"representative_source_ids\":[\"QG-e0d4d7dc\",\"QG-edb7bbb5\",\"QT-fa65a450\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:1:particle-polyvalence","source_type":"word_analysis","support_id":"sup_bca1e092b9a9810ee26e","text":"{\"blocking_evidence\":null,\"headline\":\"negative and rhetorical-question readings converge\",\"reader_payoff\":\"The reader notices that the same short surface can deny availing or ask what availing occurred, with both routes producing a null result.\",\"reason\":\"QAC explicitly supports negative and interrogative parsing; exclamatory force is retained only as rhetorical coloring because the local guardrail does not make it the main parse.\",\"representative_source_ids\":[\"MG-954600ce\",\"QS-4c8200f8\",\"QF-2f973911\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:7","source_type":"word_analysis","support_id":"sup_bde409e63401072efd9c","text":"{\"gloss_range\":\"Form I perfect earning or acquisition, with the relative pronoun as its open object and an implicit 3ms subject tied to the prior referent\",\"prose\":\"{{ar:كَسَبَ}} ({{tr:kasaba}}) closes the ayah with acquisition itself. The verb is perfect, so the earning is presented as completed and available for judgment, not still unfolding. Its subject is hidden in the 3ms form, bringing the same person back as active earner after wealth had been cast as the failed subject. The relative object before it keeps the earned domain open, so ordinary gain, accumulated benefit, and moral liability can all fall under the failed-availing verdict. Form VIII, gathering, and livestock-management pressure should be heard only as narrowed color toward deliberate acquisition, tying earned effort back to concrete wealth without replacing the surface Form I. As the final word, it compresses the second beat and leaves earned gain as the last failed support before 111:3 names the consequence.\",\"root_display\":\"{{ar:ك س ب}} ({{tr:k-s-b}})\",\"root_gloss_range\":\"earning, gaining, acquiring, seeking benefit, and incurring liability are relevant; causative gain-for-another, hunting-creature, and substance-name branches are not locally selected\",\"surface_display\":\"{{ar:كَسَبَ}} ({{tr:kasaba}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:3","source_type":"word_analysis","support_id":"sup_c0747cb56f01b30376a1","text":"{\"gloss_range\":\"governed prepositional complement meaning availing or protection for/against the prior masculine referent, with separation imagery and a bound 3ms suffix\",\"prose\":\"{{ar:عَنْهُ}} ({{tr:ʿanhu}}) makes the failed availing personal before the wealth is named. The preposition supplies a separation or shielding frame: the question is whether anything could stand away from him as protection. The suffix silently carries the condemned referent from 111:1, and its placement between the verb and wealth means the exposed person is heard before the failed protector. The repeated suffix in the next word tightens the point: the one needing protection is the same one whose own wealth fails.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:عَنْهُ}} ({{tr:ʿanhu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:7:resource-pairing","source_type":"word_analysis","support_id":"sup_d00e6b9f8786cf53cb38","text":"{\"blocking_evidence\":null,\"headline\":\"earned gain joins wealth under failed sufficiency\",\"reader_payoff\":\"The reader notices earned gain as the dynamic counterpart to stored wealth inside the same failed-sufficiency test.\",\"reason\":\"Attachment evidence coordinates the earned phrase with wealth, and the CRITICAL rows connect this pairing to wider failed-availing formulas such as 15:84 and 39:50.\",\"representative_source_ids\":[\"QI-001bf7e5\",\"QI-331492b7\",\"QI-f5e8538d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:4:root-instability-pressure","source_type":"word_analysis","support_id":"sup_d21ae611393fe3b826c9","text":"{\"blocking_evidence\":null,\"headline\":\"leaning image undercuts wealth as shield\",\"reader_payoff\":\"The reader notices the irony of wealth being assigned a protective role while leaning or swaying root-image pressure makes it feel unstable.\",\"reason\":\"The local noun sense remains wealth or property; leaning imagery survives only as narrowed etymological pressure from the CRITICAL evidence, not as the selected meaning.\",\"representative_source_ids\":[\"QS-409d8517\",\"MS-a69ed033\",\"QY-8a215c3d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:2","source_type":"word_analysis","support_id":"sup_d24a1f8dc67d4aa6cc6f","text":"{\"gloss_range\":\"negated Form IV availing or making sufficient in a protection frame, with no explicit direct object and with the affected person expressed through the following prepositional complement\",\"prose\":\"{{ar:أَغْنَىٰ}} ({{tr:aghnā}}) is the clause's center: a perfect Form IV verb whose availing has already been negated before the wealth is named. The local frame asks whether a resource could make someone sufficient, protect him, or stand in for him; the prepositional complement carries the exposed person while the direct object is absent, so the failure is not restricted to one named benefit. The root field of sufficiency and wealth is locally active, while dwelling, song, and absolute divine self-sufficiency work only as narrowed contrasts: they intensify the loss of stability or fullness without replacing the availing sense. The wording also belongs to a wider failed-reliance formula (7:48, 11:101, 15:84, 39:50), and it points forward to the fire outcome in 111:3. Even the sound hinge is tight: the guttural opening of the verb meets the constricted onset of the following prepositional complement, matching the protective relation as it collapses.\",\"root_display\":\"{{ar:غ ن ي}} ({{tr:gh-n-y}})\",\"root_gloss_range\":\"self-sufficiency, wealth, sufficing and availing are the relevant local branches; song, dwelling, and marriage-related branches remain nonselected background images or contrasts when pressed by CRITICAL rows\",\"surface_display\":\"{{ar:أَغْنَىٰ}} ({{tr:aghnā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:6:product-process-ambiguity","source_type":"word_analysis","support_id":"sup_ddd4c1316f35a7246a1a","text":"{\"blocking_evidence\":null,\"headline\":\"product reading dominates while process pressure survives\",\"reader_payoff\":\"The reader notices that what he earned is primary, while the act of earning itself can also be felt as denied availing force.\",\"reason\":\"The attachment guardrail strongly supports the relative-object parse; masdar-style reading survives only as secondary product/process pressure from the CRITICAL rows.\",\"representative_source_ids\":[\"QG-bb59db11\",\"QS-9d0a3b62\",\"QF-b387a577\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:5:coordination-under-negation","source_type":"word_analysis","support_id":"sup_df8e01b929734d24e4b2","text":"{\"blocking_evidence\":null,\"headline\":\"conjunction extends one negation\",\"reader_payoff\":\"The reader notices that the second resource remains under the same failed-availing frame instead of becoming a separate claim.\",\"reason\":\"QAC and attachment evidence identify strict coordination of the relative phrase with the wealth subject under the existing negation.\",\"representative_source_ids\":[\"QG-b13d6207\",\"QS-386a888b\",\"QT-c63120e2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:2:sound-cadence","source_type":"word_analysis","support_id":"sup_e44a378467c2c2cfe698","text":"{\"blocking_evidence\":null,\"headline\":\"sound binds negation, availing, and wealth\",\"reader_payoff\":\"The reader notices the verb as part of the ayah's audible chain, not only as an abstract predicate.\",\"reason\":\"The sound rows are coherent with the local sequence and do not conflict with grammar; they remain secondary to the semantic frame.\",\"representative_source_ids\":[\"QF-3bfa83ea\",\"QP-b8ca72fc\",\"QP-dd724d96\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:7:closing-and-forward-pressure","source_type":"word_analysis","support_id":"sup_e7a6ea878b640967923f","text":"{\"blocking_evidence\":null,\"headline\":\"final verb tightens toward the next verdict\",\"reader_payoff\":\"The reader notices acquisition as the ayah's last named failed support before the next ayah supplies the consequence.\",\"reason\":\"The word is final in 111:2, and the CRITICAL rows explicitly connect the failed-resource closure to the outcome in 111:3.\",\"representative_source_ids\":[\"QT-5939fd43\",\"QE-732ff118\",\"QB-671678a3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:4:sound-frame","source_type":"word_analysis","support_id":"sup_eee21d36f6edb5f2fbbc","text":"{\"blocking_evidence\":null,\"headline\":\"wealth thickens the repeated sound\",\"reader_payoff\":\"The reader notices the wealth word as the concrete middle of the ayah's repeated sound frame.\",\"reason\":\"The sound rows align with the local sequence and preserve a secondary acoustic payoff without changing the noun's semantic range.\",\"representative_source_ids\":[\"QE-311e4124\",\"QP-c875505f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:5:resource-expansion","source_type":"word_analysis","support_id":"sup_f03ec03ecf632f39dbb9","text":"{\"blocking_evidence\":null,\"headline\":\"wealth expands to all acquired gain\",\"reader_payoff\":\"The reader notices that possession and acquisition remain distinct categories while both are denied availing force.\",\"reason\":\"The conjunction creates a second coordinated subject rather than apposition, preserving the movement from named wealth to open acquisition.\",\"representative_source_ids\":[\"QG-0704fd72\",\"QT-df263ace\",\"QY-db1f315a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:7:material-and-moral-acquisition","source_type":"word_analysis","support_id":"sup_f465b8b3ed43509d0f4a","text":"{\"blocking_evidence\":null,\"headline\":\"earning includes gain and liability\",\"reader_payoff\":\"The reader notices that acquisition is not merely income; the open phrase can include accumulated benefit and incurred moral liability.\",\"reason\":\"V4 supports seeking and obtaining livelihood or benefit as the selected branch; moral and gathering pressure survives because the open object does not narrow the acquired domain.\",\"representative_source_ids\":[\"QS-093621e9\",\"QS-40d131a7\",\"QS-753f0fdf\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:7:variant-and-concrete-pressure","source_type":"word_analysis","support_id":"sup_fa5febb847a79a0c46ec","text":"{\"blocking_evidence\":null,\"headline\":\"deliberate acquisition colors the surface verb\",\"reader_payoff\":\"The reader notices active accumulation and livestock-management pressure while the canonical surface remains the simple Form I verb.\",\"reason\":\"Variant and concrete-image rows may color deliberateness, but local form evidence keeps the canonical surface as Form I rather than replacing it with another form.\",\"representative_source_ids\":[\"QS-713cadd9\",\"QS-910095f2\",\"QI-b27b88ca\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:2:6:coordination-pivot","source_type":"word_analysis","support_id":"sup_fac7dba58eec1e75ac56","text":"{\"blocking_evidence\":null,\"headline\":\"coordination pivots into a clause\",\"reader_payoff\":\"The reader notices that the second coordinated resource is not another simple noun but an open clause of acquisition.\",\"reason\":\"Attachment evidence analyzes the relative construction as the second subject expression, with the earning verb carrying an implicit 3ms subject.\",\"representative_source_ids\":[\"QG-48877879\",\"QT-175afa8a\",\"QY-b3898b13\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ","ayah_ref":"111:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001110/B001","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001110","role":"Self-sufficiency and reduced need supply the literal state that the negated verb denies wealth can produce.","root":"غ ن ي","source_ref":"111:2","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Acquired and abundant property supplies the possessed resource that fails to become insulation.","root":"م و ل","source_ref":"111:2","source_word_indices":["4"]}],"changed_reading":{"after":"His owned abundance failed to make him independent or reduce his exposure; possession did not become insulation.","before":"His wealth did not benefit him."},"confidence":"strong","focus_anchor":"The negated sufficiency verb attaches directly to him, while his wealth is the would-be means.","mechanism":"The self-sufficiency branch makes wealth an attempted reduction of need and exposure. Negation leaves possession intact but blocks it from becoming independence.","model_id":"baseline_failed_insulation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_failed_insulation","source_type":"hft","support_id":"sup_4f00fbc02ad26fa8a71d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ","ayah_ref":"111:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001110/B002","root_001296/B001","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001110","role":"Sufficing, sparing, and standing in for another define the failed substitutive function.","root":"غ ن ي","source_ref":"111:2","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Possessed wealth supplies the accumulated stock side of the resource system.","root":"م و ل","source_ref":"111:2","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001296","role":"Seeking and obtaining benefit supplies the active flow and yield side of the resource system.","root":"ك س ب","source_ref":"111:2","source_word_indices":["6"]}],"changed_reading":{"after":"Accumulated capital and the entire gain-producing process jointly fail to spare or replace the person who owns them.","before":"Wealth and earnings are two loose items that happened not to help."},"confidence":"strong","focus_anchor":"His wealth and whatever he acquired are coordinated under one negated claim of availing.","mechanism":"The verse couples a stock of property with the process and yield of acquisition. The availing branch asks whether either resource can suffice, spare, or stand in for its owner, and the negation rejects the whole stock-flow system as a substitute.","model_id":"baseline_stock_flow_substitution"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_stock_flow_substitution","source_type":"hft","support_id":"sup_8af5d3e738e6144d04c0","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ","ayah_ref":"111:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001110/B002","root_001296/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001296","role":"Causing another to receive gain supplies the outward transmission model, though its construction is more specific than the focus form.","root":"ك س ب","source_ref":"111:2","source_word_indices":["6"]},{"branch_id":"B002","mapped_root_id":"root_001110","role":"Availing or standing in for someone makes the transmitted network relevant as a possible source of rescue.","root":"غ ن ي","source_ref":"111:2","source_word_indices":["2"]}],"changed_reading":{"after":"What he acquired may also probe gains he caused to reach others and the outward network expected to avail him.","before":"What he earned means only his privately retained proceeds."},"confidence":"exploratory","focus_anchor":"The open object of acquisition can probe more than gains retained by the subject.","mechanism":"The branch in which acquisition brings gain to someone else opens a form-distant but live reading of an outward benefit network. What fails may include not only private earnings but gains, beneficiaries, or dependencies produced through him.","model_id":"baseline_outward_gain_network"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_outward_gain_network","source_type":"hft","support_id":"sup_c7fb5e5f2013ea90882e","trust":"legacy_unbound"}]}
</lane_packet_json>
