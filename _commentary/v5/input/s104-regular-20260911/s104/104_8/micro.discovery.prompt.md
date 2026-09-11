# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **104:8**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s104-regular-20260911/s104/104_8/micro.discovery.json` and modify nothing
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
  "ayah_ref": "104:8",
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
{"analysis_context":{"analysis_id":"s104-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"104:8","host_surah":104,"lane_context_refs":[],"ordered_context_refs":["104:0","104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:9","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dalın çekirdeği kapatma ve kuşatmadır; kapı, ateş ve kişi grubu yalnızca bu çekirdeğin belirli gerçekleşmeleridir.","branch_kind":"mixed_non_bare","branch_ref":"root_000036/B001","candidate_links":[{"candidate_id":"cand_c9024a88350aef77c079","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","surface_ar":"مُّؤْصَدَةٌ"}],"gloss":"kuşatıp kapatma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey başka bir şeyi içine alır, üstüne kapanır ve onun dışarıya açılmasını engeller."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kapı söz konusu olduğunda eylem, kapıyı kapalı duruma getirmeyi anlatır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir topluluğun üzerine kapatma ve ateşin üzerlerine kapatılmış olması, çekirdeğin yapıya bağlı kullanımlarıdır."}}],"root_ar":"و ص د","root_id":"root_000036","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem kapsama hem de kapalı duruma getirme öğelerini birlikte taşıyan en kısa genel karşılığıdır.","boundary_detail":"Dalın çekirdeği kapatma ve kuşatmadır; kapı, ateş ve kişi grubu yalnızca bu çekirdeğin belirli gerçekleşmeleridir.","branch_image_ar":"الإطباق والإغلاق على الشيء","concept_gloss":"kuşatıp kapatma","contextual_glosses":[{"applicability":"Kapının açık durumdan kapalı duruma getirildiği eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dalın kapı dışındaki kuşatma ve üzerini kapatma kapsamını taşımaz.","preserves":"Kapalı duruma getirme işlemini açık biçimde korur."},"facet_ids":["F002"],"text":"kapıyı kapatmak","usage_role":"contextual"},{"applicability":"Bir topluluğun ya da kapatılmış ateşin dışarıya açılmayacak biçimde çevrelendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel ad anlamını ve kapı kapatma kullanımını dışarıda bırakır.","preserves":"Bir şeyin başkalarının üzerine kapanması ve onları içeride tutması korunur."},"facet_ids":["F003"],"text":"üzerlerine kapatılmış","usage_role":"contextual"}],"definition":"Bir şeyi başka bir şeyin üzerine kapatmak ya da onu bütünüyle kuşatıp dışarıya açılmasını engellemektir. Bu çekirdek, kapı kapatma gibi eylemlerde ve kapatılmış şeyleri niteleyen yapılarda gerçekleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey başka bir şeyi içine alır, üstüne kapanır ve onun dışarıya açılmasını engeller."},{"facet_id":"F002","role":"specialization","statement":"Kapı söz konusu olduğunda eylem, kapıyı kapalı duruma getirmeyi anlatır."},{"facet_id":"F003","role":"associated_use","statement":"Bir topluluğun üzerine kapatma ve ateşin üzerlerine kapatılmış olması, çekirdeğin yapıya bağlı kullanımlarıdır."}],"identity_rationale":"Kaynak ifadesi, bir şeyin başka bir şeyi içine alıp üstüne kapanması çekirdeğini; kapı kapatma, birilerinin üzerine kapatma ve kapatılmış ateş örnekleriyle birlikte açıkça verir. Hazırlanan dal bu ortak kapatma ve kuşatma anlamını doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kapatıp örten şey"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kuşatıp kapatma"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"üzerlerine kapattı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kapıyı kapattı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"üzerlerine kapatılmış ateş"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kapatıp örten şey için kullanılan ad"}],"lexicalization_note":"Tanım genel kapatma çekirdeğini korur; kapıyı kapatma, insanların üzerine kapatma ve kapatılmış ateş kullanımlarını yalnızca bağlı yapılara özgü gerçekleşmeler olarak ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan üç karşılaştırma kapı kapatma, açıklığı tıkama ve erişimi engelleme ile karışabilecek sınırları gösterir, diğer adaylar ise daha uzak sonuçları ya da ayrı dal anlamlarını yineler.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal kapı üzerinde gerçekleşen özel bir eylemdir; odak dalın çekirdeği ise daha genel kuşatıp kapatma ilişkisidir ve kapı dışındaki nesne ya da katılımcılara da uygulanır.","focus_only":"Odak dal, bir şeyi kuşatıp üzerine kapanma ile kapatılmış nesne ve durumları da kapsar.","gloss":"kapıyı çekip kapatma","neighbor_only":"Komşu dal özellikle kapıyı geri itip kapatma eylemine bağlıdır.","neighbor_ref":"root_000279/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da kapının kapalı duruma getirilmesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalın tanımlayıcı yönü kuşatıp üzerine kapanmadır; komşu dalda ise belirleyici işlem boşluğu tıkamak veya ağzı sıkıca bağlamaktır.","focus_only":"Odak dal, bir şeyin başka bir şeyin üzerine kapanması veya onu kuşatması işlemini öne çıkarır.","gloss":"açıklığı tıkayıp kapatma","neighbor_only":"Komşu dal, bir açıklığın tıkaçla ya da sıkıca bağlanarak ortadan kaldırılmasını öne çıkarır.","neighbor_ref":"root_000884/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da açıklığın kalmaması ve dışarıyla bağlantının kesilmesi sonucu bulunur."},{"boundary_match":"partial","distinction":"Erişimin engellenmesi odak dalda kapatmanın sonucu olabilir; komşu dalda ise sonuç doğrudan çekirdektir ve kuşatıp kapanma şart değildir.","focus_only":"Odak dal somut biçimde kuşatıp kapatma işlemini bildirir.","gloss":"erişimi engelleme","neighbor_only":"Komşu dalın çekirdeği, belirli bir kapatma biçimi aramadan erişimi engellemektir.","neighbor_ref":"root_000294/B001","relation_type":"near_neighbor","shared_zone":"Kapatma, içeridekine erişimi engelleyebilir ve böylece iki anlam aynı sonuçta buluşabilir."}],"source_phrase_ar":"شيء يشتمل على الشيء (maqayis); الإِصد والإِصاد والوصاد بمنزلة المطبق (ayn); أصدت عليهم وأوصدته (ayn); نار مُؤصدة أي مطبقة (ayn); آصدت الباب إذا أغلقته (sihah)","source_summary":"Kaynaklar, anlamı bir şeyin diğerini kuşatıp kapatması çevresinde birleştirir; ad biçimleri kapatan şeyi, eylem biçimleri ise kapatma işlemini belirtir.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه الإِصاد والإِصد بمعنى المطبق؛ وآصدت الباب؛ ونار مُؤصدة","what_is_not_ar":"الحظيرة والقميص والفناء والموضع"},"support_links":["sup_db1e92643b01c2e563f6"]},{"boundary":"Bu dal bir kapatma eylemini değil, içindekileri çevreleyen ve tutan alan türünü anlatır.","branch_kind":"bare","branch_ref":"root_000036/B002","candidate_links":[{"candidate_id":"cand_e8ec6bd110cdfdf5c767","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","surface_ar":"مُّؤْصَدَةٌ"}],"gloss":"çevrili barınak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Alan, içinde bulunanları çevreler ve sınırları içinde bir arada tutar."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynak ifadesinde bu alan, ağıl ya da ona denk bir çevrili yer olarak açıklanır."}}],"root_ar":"و ص د","root_id":"root_000036","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İçindekileri çevreleyip bir arada tutan alanın yalın ve genel Türkçe karşılığıdır.","boundary_detail":"Bu dal bir kapatma eylemini değil, içindekileri çevreleyen ve tutan alan türünü anlatır.","branch_image_ar":"الحظيرة المشتملة على ما فيها","concept_gloss":"çevrili barınak","contextual_glosses":[{"applicability":"Çevrili alanın hayvan barındıran bir yer olarak kullanıldığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İçeride tutulanların mutlaka hayvan olmadığı daha genel alan kapsamını daraltır.","preserves":"Çevrili ve barındırıcı alan niteliğini korur."},"facet_ids":["F002"],"text":"ağıl","usage_role":"contextual"}],"definition":"İçinde bulunanları çevreleyerek bir arada tutan, barınak veya ağıl niteliğindeki çevrili alandır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Alan, içinde bulunanları çevreler ve sınırları içinde bir arada tutar."},{"facet_id":"F002","role":"source_variant","statement":"Kaynak ifadesinde bu alan, ağıl ya da ona denk bir çevrili yer olarak açıklanır."}],"identity_rationale":"Kaynak ifadesi, içindekileri çevreleyip barındırdığı için bu adla anılan bir çitli ya da çevrili alanı doğrudan tanımlar. Hazırlanan dalın çevreleme ve içeride tutma çerçevesi bu ifadeyle uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"içindekileri çevreleyen barınak veya ağıl"}],"lexicalization_note":"Tanım yalın alan adını esas alır ve başka dallardaki kapatma eylemi ya da özel söz öbeklerini bu anlama katmaz.","neighbor_coverage_note":"Tüm adaylar incelendi; hayvan ağılı, çitli alan ve somut çevreleme ile yapılan üç karşılaştırma dalın yer türü ve kapsam sınırını yeterince belirginleştirir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal hayvan barındırma bakımından özelleşmiştir; odak dalın kaynak ifadesi ise çevreleme ve içeride tutmayı temel alır, içeridekilerin türünü sınırlamaz.","focus_only":"Odak dal, içindekileri çevreleyen alanı barındırdığı şeyin türünü zorunlu kılmadan adlandırır.","gloss":"hayvan ağılı","neighbor_only":"Komşu dal özellikle sığır veya koyun gibi hayvanların barındığı ağılı anlatır.","neighbor_ref":"root_000897/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da çevrili bir barınak veya ağıl alanını gösterebilir."},{"boundary_match":"partial","distinction":"Odak dal kapsayıcı alan adı olarak daha yalındır; komşu dal yapı malzemesini, duvarı ve çevrili yerin farklı kullanım alanlarını ayrıca kapsar.","focus_only":"Odak dal, alanın içindekileri kapsayıp bir arada tutma işlevini öne çıkarır.","gloss":"çitli alan","neighbor_only":"Komşu dal, ahşap, kamış veya ağaçtan yapılabilen duvarı ve bu duvarla kurulan çevrili yeri de kapsar.","neighbor_ref":"root_000338/B001","relation_type":"near_synonym","shared_zone":"İki dal da içindekileri sınırlandıran çevrili alanı anlatır."},{"boundary_match":"partial","distinction":"Odak dal bir yer türüdür; komşu dalın çekirdeği ise o yeri meydana getirebilen çevreleme ilişkisidir.","focus_only":"Odak dal, çevreleme sonucunda oluşan barınak niteliğindeki alanı adlandırır.","gloss":"çevreleme","neighbor_only":"Komşu dal, bir şeyi duvarla veya başka unsurlarla çevreleme eylem ve durumunu anlatır.","neighbor_ref":"root_000372/B001","relation_type":"near_neighbor","shared_zone":"Çevrili bir alan, somut çevreleme işleminin sonucudur."}],"source_phrase_ar":"الحظيرة أُصيدة سميت بذلك لاشتمالها على ما فيها (maqayis); الأُصيدة كالحظيرة لغة في الوصيدة (sihah)","source_summary":"Kaynaklar, bu adı içindekileri çevreleyip tutan ağıl benzeri bir alan için verir ve adlandırmayı alanın kapsayıcı niteliğiyle ilişkilendirir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه الأُصيدة بمعنى الحظيرة أو الوصيدة لاشتمالها على ما فيها","what_is_not_ar":"الإغلاق والقميص والفناء والموضع"},"support_links":["sup_21b3392510bfac082b4f"]},{"boundary":"Giysi anlamı dalın çekirdeğidir; giysiye sahip olma ve onu giydirme eylemi çekirdekle eşitlenmemelidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000036/B003","candidate_links":[{"candidate_id":"cand_5e4cd83747dde09ca7c5","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","surface_ar":"مُّؤْصَدَةٌ"}],"gloss":"kız çocuklarının giydiği küçük veya içe giyilen gömlek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kız çocuklarının giydiği küçük bir gömlek veya giysi altına giyilen gömlek türüdür."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kız çocuğunun bu giysiye sahip olduğu, giysi adıyla kurulan bağlı bir yapıda belirtilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Türemiş eylem, birine bu küçük gömleği giydirmeyi anlatır."}}],"root_ar":"و ص د","root_id":"root_000036","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynaklardaki küçük gömlek ve giysi altına giyilen gömlek çeşitlerini, kız çocuklarıyla ilişkisini koruyarak seçenekli biçimde yansıtır.","boundary_detail":"Giysi anlamı dalın çekirdeğidir; giysiye sahip olma ve onu giydirme eylemi çekirdekle eşitlenmemelidir.","branch_image_ar":"الأُصدة التي تلبسها الصبايا","concept_gloss":"kız çocuklarının giydiği küçük veya içe giyilen gömlek","contextual_glosses":[{"applicability":"Kullanıcının bağlamdan kız çocuğu olduğunun anlaşıldığı giysi anlatımlarında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kız çocuklarına özgü kullanım bilgisini açıkça söylemez.","preserves":"Giysinin küçük bir iç gömleği olmasını korur."},"facet_ids":["F001"],"text":"küçük iç gömleği","usage_role":"general"},{"applicability":"Kız çocuğunun söz konusu giysiye sahip olduğunu bildiren bağlı yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kız çocuğu ile sahip olduğu küçük iç gömleği arasındaki ilişkiyi eksiksiz korur."},"facet_ids":["F002"],"text":"küçük iç gömleği olan kız","usage_role":"contextual"},{"applicability":"Birine bu özel giysi türünün giydirildiği türemiş eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Giysiyi başka birine giydirme işlemini ve giysi türünü korur."},"facet_ids":["F003"],"text":"küçük iç gömleğini giydirmek","usage_role":"contextual"}],"definition":"Kız çocuklarının giydiği küçük bir gömlek ya da başka bir giysinin altına giyilen gömlektir. Bu giysiye sahip olma ve birine onu giydirme, ayrı yapılarda kurulan bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kız çocuklarının giydiği küçük bir gömlek veya giysi altına giyilen gömlek türüdür."},{"facet_id":"F002","role":"associated_use","statement":"Bir kız çocuğunun bu giysiye sahip olduğu, giysi adıyla kurulan bağlı bir yapıda belirtilir."},{"facet_id":"F003","role":"extension","statement":"Türemiş eylem, birine bu küçük gömleği giydirmeyi anlatır."}],"identity_rationale":"Kaynak ifadesi kız çocuklarının giydiği küçük gömleği veya giysi altına giyilen gömleği temel alır, fakat aynı iddia bu giysiye sahip olma ve birine bu giysiyi giydirme yapılarını da içerir. Dal korunabilir; giysinin kendisi çekirdek, sahiplik ve giydirme ise yapıya bağlı kullanımlar olarak ayrılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kız çocuklarının giydiği küçük veya içe giyilen gömlek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"küçük iç gömleği olan kız"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ona küçük iç gömleğini giydirdi"}],"lexicalization_note":"Tanım küçük iç gömleğini merkezde tutar; giysiye sahip olma ve birine onu giydirme anlamlarını yalnızca ilgili söz öbekleri ve türemiş eylemle sınırlar.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; küçük kısa giysi, iç kat ve genel gömlek karşılaştırmaları bu özel çocuk giysisinin biçim, kullanım ve kullanıcı sınırlarını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal gömlek ve içe giyilme özellikleriyle sınırlıdır; komşu dal ise kesim ve gövdedeki duruş bakımından farklı kısa giysileri de içine alır.","focus_only":"Odak dal, kız çocuklarının giydiği veya başka giysinin altına giyilen küçük gömleği anlatır.","gloss":"kısa çocuk giysisi","neighbor_only":"Komşu dal küçük gömleğin yanında gövdeye asılı duran, bele kadar uzanan başka kısa giysi türlerini de kapsar.","neighbor_ref":"root_001039/B015","relation_type":"near_synonym","shared_zone":"Her iki dal da kız çocuklarıyla ilişkilendirilebilen küçük veya kısa bir üst giysisini gösterebilir."},{"boundary_match":"partial","distinction":"Odak dal çocuklara özgü küçük gömlek türüdür; komşu dalın kullanıcı, konum ve giysi biçimi kapsamı daha geniştir.","focus_only":"Odak dal giysiyi küçük kızların giydiği küçük bir gömlek olarak sınırlar.","gloss":"giysi altına giyilen ince kat","neighbor_only":"Komşu dal iki giysi arasında, zırh altında veya kadınların bedeninin başka bölümünde kullanılan daha geniş bir iç giysi sınıfıdır.","neighbor_ref":"root_001102/B007","relation_type":"near_synonym","shared_zone":"İki dal da başka bir giysinin altında giyilen bir giysiyi anlatabilir."},{"boundary_match":"partial","distinction":"Genel gömlek karşılığı odak dalın kullanıcı ve kullanım sınırlarını siler; odak dal da komşunun genel ve aktarmalı kapsamının tümünü taşımaz.","focus_only":"Odak dal küçük boyut, içe giyilme ve kız çocuklarıyla kullanım sınırlarını taşır.","gloss":"gömlek","neighbor_only":"Komşu dal genel gömlek ve giyme anlamlarının yanı sıra örtü ve görev gibi aktarmalı kullanımları da kapsar.","neighbor_ref":"root_001256/B001","relation_type":"near_synonym","shared_zone":"Odak giysi genel gömlek sınıfının küçük ve özel bir türüdür."}],"source_phrase_ar":"الأُصدة قميص صغير يلبسه الصبايا (maqayis); صبية ذات مُؤصد (maqayis); الأُصدة قميص يلبس تحت الثوب وتلبسه صغار الجواري (sihah); أصدته تأصيدا (sihah)","source_summary":"Kaynaklar küçük kızların giydiği, kimi açıklamada başka bir giysinin altında bulunan küçük gömleği bildirir; ayrıca bu giysiye sahip olma ve onu giydirme yapıları aynı iddiada yer alır.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه الأُصدة وهي قميص صغير أو قميص يلبس تحت الثوب وتلبسه صغار الجواري","what_is_not_ar":"الإغلاق والحظيرة والفناء والموضع"},"support_links":["sup_dcc6dbecd739ec9c683e"]},{"boundary":"Dal yalnızca avlu anlamıdır; kapı, giriş veya kapatma anlamları bu dala taşınmaz.","branch_kind":"bare","branch_ref":"root_000036/B004","candidate_links":[{"candidate_id":"cand_c6ef6bb179b2970db052","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","surface_ar":"مُّؤْصَدَةٌ"}],"gloss":"avlu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yapıyla bağlantılı açık alanı, başka bir deyişle avluyu belirtir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu anlam, aynı avlu adının dilsel bir biçim değişkesi olarak aktarılır."}}],"root_ar":"و ص د","root_id":"root_000036","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yapıyla bağlantılı açık alan anlamını tam ve doğal biçimde karşılar.","boundary_detail":"Dal yalnızca avlu anlamıdır; kapı, giriş veya kapatma anlamları bu dala taşınmaz.","branch_image_ar":"الفناء والوصيد","concept_gloss":"avlu","contextual_glosses":[{"applicability":"Açık alanın bir eve bağlı olduğunun bağlamda belirtilmesi gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ev dışındaki yapılara bağlı avlu olasılığını sınırlar.","preserves":"Avlunun bir yapıyla bağlantılı açık alan olmasını korur."},"facet_ids":["F001"],"text":"evin avlusu","usage_role":"contextual"}],"definition":"Bir evin ya da yapının çevresinde veya önünde bulunan açık alan, yani avludur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yapıyla bağlantılı açık alanı, başka bir deyişle avluyu belirtir."},{"facet_id":"F002","role":"source_variant","statement":"Bu anlam, aynı avlu adının dilsel bir biçim değişkesi olarak aktarılır."}],"identity_rationale":"Kaynak ifadesi sözcüğü doğrudan avlu anlamındaki başka bir biçimin dilsel çeşidi olarak tanımlar. Hazırlanan dalın avlu odağı bu tek kaynaklı ve açık tanımla tam olarak örtüşür.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"avlu"}],"lexicalization_note":"Tanım yalın biçimin avlu anlamıyla sınırlıdır ve komşu biçimin kapı gibi ek anlamlarını ya da başka söz öbeklerini içeri almaz.","neighbor_coverage_note":"Bütün komşular gözden geçirildi; ev avlusu, evin önü ve genel açık alanla ilgili üç yakın karşılaştırma avlu çekirdeğini ve kapı anlamının dışarıda kalışını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Avlu bağlamında anlamlar örtüşür, ancak komşu dalın kapı kapsamı odak dalda bulunmaz; bu nedenle tam eş anlamlılık yalnızca avlu kullanımında geçerlidir.","focus_only":null,"gloss":"ev avlusu veya kapısı","neighbor_only":"Komşu dal avlunun yanı sıra evin kapısını da gösterebilir ve alanı eve bitişik oluşuyla açıklar.","neighbor_ref":"root_001653/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da evle bağlantılı avlu anlamında kullanılabilir."},{"boundary_match":"partial","distinction":"Odak dal genel avlu adıdır; komşu dal alanın evin yanlarına uzanması ve önündeki genişlik gibi mekânsal ayrıntıları ayrıca taşır.","focus_only":"Odak dal yalın biçimde avlu alanını adlandırır.","gloss":"evin avlusu ve önü","neighbor_only":"Komşu dal evin çevresine uzanan alanı ve özellikle evin önündeki genişliği de vurgular.","neighbor_ref":"root_001181/B002","relation_type":"near_synonym","shared_zone":"İki dal evle bağlantılı avlu veya açık alan anlamında buluşur."},{"boundary_match":"partial","distinction":"Gösterilen yer büyük ölçüde örtüşse de odak dal belirli bir avlu adının biçim çeşididir; komşu dalın sözlüksel kapsamı evin sahası olarak bağımsızdır.","focus_only":"Odak dal kaynakta başka bir avlu adının söyleyiş çeşidi olarak belirlenmiştir.","gloss":"evin açık alanı","neighbor_only":"Komşu dal evin saha ve açık alanını daha genel bir yer adıyla ifade eder.","neighbor_ref":"root_000756/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bir evin avlusunu veya açık sahasını gösterebilir."}],"source_phrase_ar":"الأَصيد لغة في الوصيد وهو الفناء (sihah)","source_summary":"Tek kaynak, biçimi avlu anlamındaki eşdeğer bir söyleyiş çeşidi olarak verir.","sources":["SI"],"what_is_ar":"يدخل فيه الأَصيد لغة في الوصيد وهو الفناء","what_is_not_ar":"الإغلاق والحظيرة والقميص والموضع"},"support_links":["sup_44177d56d62a6d0ff7e9"]},{"boundary":"Dağlar arasındaki çukur alan yer türüdür; belirli yeri gösteren uzun ifade ise bu çekirdeğe bağlı ayrı bir sözlüksel kullanımdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000036/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","surface_ar":"مُّؤْصَدَةٌ"}],"gloss":"dağlar arasındaki çukur alan","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dağlar arasında yer alan çukur veya çanak biçimli doğal alanı belirtir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Daha uzun bir sözlüksel ifade, belirli bir yerin adı olarak kullanılır."}}],"root_ar":"و ص د","root_id":"root_000036","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın biçimin doğal yer türünü eksiksiz karşılar; belirli yer kullanımı ayrıca bağlamsal olarak gösterilir.","boundary_detail":"Dağlar arasındaki çukur alan yer türüdür; belirli yeri gösteren uzun ifade ise bu çekirdeğe bağlı ayrı bir sözlüksel kullanımdır.","branch_image_ar":"الموضع بين الجبال","concept_gloss":"dağlar arasındaki çukur alan","contextual_glosses":[{"applicability":"Dağlar arasında kalan çukur ve çanak biçimli doğal alanın kısa bağlamsal karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dağlarla çevrili çukur alan görünümünü doğal bir Türkçe ifadeyle korur."},"facet_ids":["F001"],"text":"dağ çanağı","usage_role":"contextual"},{"applicability":"Daha uzun sözlüksel ifadenin özel bir yeri gösterdiği kullanım açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yerin dağlar arasındaki çukur alanla sözlüksel bağlantısını açıkça taşımaz.","preserves":"İfadenin tek ve belirli bir yere gönderimde bulunmasını korur."},"facet_ids":["F002"],"text":"belirli bir yer","usage_role":"explanatory"}],"definition":"Dağlar arasında bulunan çukur veya çanak biçimli bir alandır. Daha uzun bir sözlüksel yapıda ise belirli bir yeri gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dağlar arasında yer alan çukur veya çanak biçimli doğal alanı belirtir."},{"facet_id":"F002","role":"associated_use","statement":"Daha uzun bir sözlüksel ifade, belirli bir yerin adı olarak kullanılır."}],"identity_rationale":"Kaynak ifadesi iki bağlı kullanımı birlikte verir: dağlar arasındaki çukur alanı belirten yalın biçim ve belirli bir yeri gösteren daha uzun ifade. Hazırlanan dal kullanılabilir, ancak yer türü ile özel bir yeri belirten sözlüksel kullanım tek ve belirsiz bir yer anlamıymış gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"belirli bir yer adı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"dağlar arasındaki çukur alan"}],"lexicalization_note":"Tanım yalın biçimin dağlar arasındaki çukur alan anlamıyla daha uzun ifadenin belirli yer kullanımını açıkça ayırır.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; alçak arazi, tepe arası çöküntü, dağ geçidi ve özel dağ adı karşılaştırmaları doğal yer türü ile belirli yer kullanımının sınırlarını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dağlık çevre ve çukur alanla sınırlıdır; komşu dal farklı yükselti türleri ve benzetmeli beden bölgeleri arasında da kullanılabilir.","focus_only":"Odak dal dağlarla çevrili çukur bir alanı belirtir.","gloss":"iki yükselti arasındaki alçak yer","neighbor_only":"Komşu dal iki yükselti, kum sırtı veya başka beden çıkıntıları arasındaki alçak boşluğa kadar uzanan daha geniş bir kapsama sahiptir.","neighbor_ref":"root_001176/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da dağlar veya yükseltiler arasında kalan alçak bir yeri gösterebilir."},{"boundary_match":"partial","distinction":"Odak dal çanak veya çukur alanı vurgular; komşu dalın ayırt edici yönü düşen şeyin yöneldiği alçak ve eğimli yer olmasıdır ve ayrıca araç parçasına uzanır.","focus_only":"Odak dal dağlar arasındaki çukur doğal alanı yer türü olarak adlandırır.","gloss":"iki tepe arasındaki alçak yer","neighbor_only":"Komşu dal iki tepe arasındaki eğimli alçak yerin yanı sıra tahılın düştüğü değirmen bölümünü de kapsar.","neighbor_ref":"root_000402/B003","relation_type":"near_neighbor","shared_zone":"İki dal, yükseltiler arasında bulunan alçak bir doğal alanı anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal kapalıca bir çukur alan görünümündedir; komşu dal ise aralık, geçiş yolu veya akış koridoru olmasıyla ayrılır.","focus_only":"Odak dal dağlar arasında kalan çukur veya çanak biçimli alanı anlatır.","gloss":"dağ geçidi","neighbor_only":"Komşu dal iki dağ arasındaki yarık, geçit, yol veya su yatağı niteliğini öne çıkarır.","neighbor_ref":"root_000797/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da iki dağ arasındaki bir arazi biçimini gösterebilir."},{"boundary_match":"thematic_only","distinction":"Odak dalın yalın biçiminde tanımlanabilir bir arazi türü vardır; komşu dal ise yalnızca belirli bir coğrafi varlığı adlandırır.","focus_only":"Odak dal bir doğal yer türünü ve buna bağlı belirli yer kullanımını içerir.","gloss":"belirli dağ veya yer adı","neighbor_only":"Komşu dal belirli bir dağın veya yerin özel adıdır.","neighbor_ref":"root_001243/B009","relation_type":"thematic","shared_zone":"İki dal da dağlık bir coğrafyada belirli bir yere gönderimde bulunabilir."}],"source_phrase_ar":"ذات الأَصاد موضع (sihah); الأَصاد ردهة بين أجبل (sihah)","source_summary":"Tek kaynak, yalın biçimi dağlar arasındaki çukur alan olarak açıklar ve aynı öğeyi içeren daha uzun ifadeyi belirli bir yer için kaydeder.","sources":["SI"],"what_is_ar":"يدخل فيه الأَصاد علما على موضع أو ردهة بين أجبل","what_is_not_ar":"الإغلاق والحظيرة والقميص والفناء"},"support_links":[]},{"boundary":"Genel bitiştirme çekirdeği ile kapıyı örtüp sıkıca kapatma gerçekleşimi ayrı tutulmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001653/B001","candidate_links":[{"candidate_id":"cand_c9024a88350aef77c079","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","surface_ar":"مُّؤْصَدَةٌ"}],"gloss":"bitiştirerek sıkıca kapatma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel ilişki, bir şeyi başka bir şeye katıp iki şeyi birbirine bitiştirmektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kapıya bağlı gerçekleşimde kapı örtülür, iki yüzey birbirine getirilir ve kapanış sağlamlaştırılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Eylemin sonucu, kapının bütünüyle örtülmüş ve sıkıca kapalı durumda bulunmasıdır."}}],"root_ar":"و ص د","root_id":"root_001653","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel bitiştirme çekirdeğini ve kapı bağlamındaki örtme, sağlam kapatma ve kapalı sonuç bütününü birlikte anlatır.","boundary_detail":"Genel bitiştirme çekirdeği ile kapıyı örtüp sıkıca kapatma gerçekleşimi ayrı tutulmalıdır.","branch_image_ar":"إطباق الباب وإحكام إغلاقه","concept_gloss":"bitiştirerek sıkıca kapatma","contextual_glosses":[{"applicability":"Kapının örtülerek sağlam biçimde kapatıldığı eylem bağlamlarında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel bitiştirme çekirdeğini ve kapalı sonucu ayrıca adlandırmaz.","preserves":"Kapıya uygulanan örtme ve sağlam kapatma eylemini korur."},"facet_ids":["F002"],"text":"kapıyı sıkıca kapatmak","usage_role":"contextual"},{"applicability":"Eylemden çok kapının eriştiği örtülü ve sağlam kapalı durumu öne çıkaran bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bitiştirme çekirdeğini ve kapatma işlemini göstermez.","preserves":"Ortaya çıkan sağlam kapalı durumu korur."},"facet_ids":["F003"],"text":"sıkıca kapalı","usage_role":"contextual"}],"definition":"Bir şeyi başka bir şeye katıp bitiştirme düşüncesidir. Kapı bağlamında iki yüzeyi birbirine getirerek kapıyı örtmeyi, sıkıca kapatmayı ve böyle kapalı durumda bulunmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel ilişki, bir şeyi başka bir şeye katıp iki şeyi birbirine bitiştirmektir."},{"facet_id":"F002","role":"specialization","statement":"Kapıya bağlı gerçekleşimde kapı örtülür, iki yüzey birbirine getirilir ve kapanış sağlamlaştırılır."},{"facet_id":"F003","role":"extension","statement":"Eylemin sonucu, kapının bütünüyle örtülmüş ve sıkıca kapalı durumda bulunmasıdır."}],"identity_rationale":"Kaynak sözü, kapıyı kapatma kullanımının arkasında bir şeyi başka bir şeye katıp bitiştirme çekirdeğini de açıkça verir. Bu nedenle sağlanan kapı çerçevesi geçerlidir, ancak dalın bütününü yalnızca kapıyla sınırlandırmamak gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kapıyı örtüp sıkıca kapatmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kapıyı örtüp sıkıca kapatmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"örtülmüş ve kapalı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"örtülmüş ve sıkıca kapatılmış"}],"lexicalization_note":"Tanım, genel bitiştirme çekirdeğini kapıya bağlı eylem ve kapalı durum bildiren biçimlerle kaynaştırmadan ayırır.","neighbor_coverage_note":"En yakın kapanma eylemleri, kilitleme alanı ve aynı kökteki kapı adı yayımlandı; set çekme, çevreleme, mühürleme, taş barınak ve bitki dalları ise ya daha uzak ya da bu karşıtlıkları yineleyen adaylardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kapıdaki yüzeyleri bitiştirip kapanışı sağlamlaştırırken komşu dalın kapsamı bir şeyin üzerine kapanma yönünde daha geneldir.","focus_only":"Bitiştirme yönü ve kapının sağlam biçimde kapanması bu dalda birlikte öne çıkar.","gloss":"üzerine kapatma","neighbor_only":"Komşu dal, kapanmayı kapı dışındaki bir şeyin üzerine kapanma biçiminde de kurar.","neighbor_ref":"root_000036/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi örtme, kapatma ve kapalı duruma getirme alanını paylaşır."},{"boundary_match":"partial","distinction":"Komşu dal kapıyı geri getiren hareketi öne çıkarır; bu dal ise yüzeylerin bitişmesiyle oluşan tam ve sağlam kapanışı vurgular.","focus_only":"Yüzeyleri bitiştirme, kapanışı sıkılaştırma ve kapalı sonucu birlikte içerir.","gloss":"kapıyı geri çekip kapatma","neighbor_only":"Kapıyı geri itme ya da çekme hareketi komşu dalın ayırt edici yönüdür.","neighbor_ref":"root_000279/B007","relation_type":"near_synonym","shared_zone":"İki dal da kapının açık durumdan kapalı duruma geçirilmesini anlatır."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği örtüp kapatmaktır; komşu dalın çekirdeği kilitleme ya da bağlama yoluyla kapalı tutmadır ve daha geniş yan anlamları vardır.","focus_only":"Kapının örtülüp yüzeylerinin bitişmesi ve böylece kapalı duruma gelmesi anlatılır.","gloss":"kilitleyip bağlama","neighbor_only":"Kilitleme ve bağlama yanında sertleşme, kuruma ve başka genişlemeler de bulunur.","neighbor_ref":"root_001246/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal kapının açılmasını engelleyen sağlam bir kapanışla ilişkilendirilebilir."},{"boundary_match":"field_only","distinction":"Bu dal bir kapatma işlemi ve durumudur; komşu dal ise bir yerin ya da nesnenin adıdır, bu nedenle ortak bağlam anlam özdeşliği doğurmaz.","focus_only":"Kapıyı örtme ve sıkıca kapatma eylemi ile bunun sonucu anlatılır.","gloss":"eve bağlı avlu veya kapı","neighbor_only":"Eve bağlı açık alanı ya da bazı kullanımlarda kapının kendisini adlandırır.","neighbor_ref":"root_001653/B002","relation_type":"same_field","shared_zone":"Her iki dalın kullanımı ev ve kapı çevresinde görülebilir."}],"source_phrase_ar":"أصل يدل على ضم شيء إلى شيء (maqayis)؛ أوصدت الباب أغلقته والموصد المطبق (maqayis)؛ أوصدت الباب وآصدته إذا أغلقته فهو موصد ومطبقة (sihah)؛ أوصدت الباب وآصدته أي أطبقته وأحكمته ومؤصدة مطبقة (mufradat)","source_summary":"Kaynakların ortak anlatımı, bitiştirme temelini kapının örtülüp kapanmasıyla ilişkilendirir; kapatma eylemi, sıkılık ve ortaya çıkan kapalı durum aynı anlam çevresinde yer alır.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه أوصدت وآصدت الباب بمعنى أغلقته، والموصد أو المؤصد بمعنى المطبق المحكم.","what_is_not_ar":"لا يدخل فيه الوصيد بمعنى الفناء أو النبات أو الوصيدة الحجرية إلا من جهة اشتراكها في أصل الضم والاتصال."},"support_links":["sup_db1e92643b01c2e563f6"]},{"boundary":"Eve bağlı açık alan temel anlamdır; kapı anlamı kaynaklarda yer alan ayrı bir kullanım olarak korunmalıdır.","branch_kind":"non_bare","branch_ref":"root_001653/B002","candidate_links":[{"candidate_id":"cand_c6ef6bb179b2970db052","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","surface_ar":"مُّؤْصَدَةٌ"}],"gloss":"eve bağlı avlu veya kapı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderge, eve bağlı açık alan ya da evin önündeki avludur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Açık alanın ayırt edici ilişkisi, evle bitişik ya da eve bağlı olmasıdır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı ad bazı kullanımlarda evin kapısını belirtir."}}],"root_ar":"و ص د","root_id":"root_001653","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eve bağlı açık alanı temel gönderge, evin kapısını ise ayrı bir kaynak kullanımı olarak birlikte kapsar.","boundary_detail":"Eve bağlı açık alan temel anlamdır; kapı anlamı kaynaklarda yer alan ayrı bir kullanım olarak korunmalıdır.","branch_image_ar":"فناء البيت أو بابه المتصل بالربع","concept_gloss":"eve bağlı avlu veya kapı","contextual_glosses":[{"applicability":"Sözcük evin önündeki ya da eve bağlı açık alanı gösterdiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı adın kapıyı belirten kaynak kullanımını dışarıda bırakır.","preserves":"Eve bağlı açık alanın yer ve bağlantı niteliğini korur."},"facet_ids":["F001","F002"],"text":"evin avlusu","usage_role":"contextual"},{"applicability":"Sözcüğün açık alanı değil doğrudan evin kapısını gösterdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eve bağlı açık alan olan temel göndergeyi içermez.","preserves":"Kapıyı adlandıran kaynak kullanımını korur."},"facet_ids":["F003"],"text":"evin kapısı","usage_role":"contextual"}],"definition":"Eve bağlı olan ve evin önünde ya da çevresinde yer alan açık alandır. Bazı kullanımlarda evin kapısını da adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderge, eve bağlı açık alan ya da evin önündeki avludur."},{"facet_id":"F002","role":"core","statement":"Açık alanın ayırt edici ilişkisi, evle bitişik ya da eve bağlı olmasıdır."},{"facet_id":"F003","role":"source_variant","statement":"Aynı ad bazı kullanımlarda evin kapısını belirtir."}],"identity_rationale":"Kaynak sözü, eve bağlı açık alan anlamını bağlantı ilişkisiyle açıklar ve aynı biçim için kapı anlamını da bildirir. Sağlanan çerçeve bu iki tanıklığı sınırlarını bozmadan yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"evin avlusu veya kapısı"}],"lexicalization_note":"Tanım yalnızca belirtilen adın eve bağlı açık alan ve kapı anlamlarıyla sınırlıdır; kökün genel anlamı gibi sunulmaz.","neighbor_coverage_note":"Eve bağlı açık alan ve kapı anlamına en çok yaklaşan üç yer dalı ile aynı kökteki kapatma dalı yayımlandı; genel meydan, giriş, kısa duvar, gizlenme yeri ve diğer kök içi dallar daha uzak alan ilişkileridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Açık alan anlamında örtüşürler; bu dalın ayrıca kapı kullanımı bulunduğu için bütün kapsamları birbirinin yerine geçmez.","focus_only":"Eve bağlı açık alan yanında evin kapısını belirten ayrı bir kullanım da vardır.","gloss":"evin açık alanı","neighbor_only":"Komşu dal yalnızca açık alanı adlandıran sesçe farklı bir biçimdir.","neighbor_ref":"root_000036/B004","relation_type":"near_synonym","shared_zone":"İki dal da eve bağlı açık alanı aynı temel yer ilişkisiyle adlandırır."},{"boundary_match":"partial","distinction":"Bu dal eve bağlı avlu ile kapı arasında sınırlı kalır; komşu dal kapı önü yapıları ve başka kurumsal kullanımlara uzanır.","focus_only":"Eve bağlantıyla tanımlanan avlu ve ayrıca kapı kullanımı bulunur.","gloss":"kapı önü ve avlu","neighbor_only":"Kapı önü, eşik çevresi, gölgelik ya da yönetici kapıları gibi daha geniş kullanımları kapsar.","neighbor_ref":"root_000687/B004","relation_type":"near_synonym","shared_zone":"Her iki dal kapıyı ve kapının önündeki açık alanı adlandırabilir."},{"boundary_match":"partial","distinction":"Komşu dal açık alanın yayılım ve genişlik yönünü öne çıkarır; bu dal ise eve bağlantıyı temel alır ve kapıyı da adlandırabilir.","focus_only":"Açık alanın yanında kapıyı adlandıran kullanım da bulunur.","gloss":"evin önü ve çevresindeki avlu","neighbor_only":"Evin önüne ve yanlarına uzanan genişliği özellikle belirtir.","neighbor_ref":"root_001181/B002","relation_type":"near_synonym","shared_zone":"İki dal da eve bitişik ya da evin önündeki açık alanı anlatır."},{"boundary_match":"field_only","distinction":"Bu dal bir yer ya da nesne adıdır; komşu dal ise kapıya uygulanan eylem ve ortaya çıkan durumdur.","focus_only":"Eve bağlı açık alanı veya kapının kendisini adlandırır.","gloss":"kapıyı sıkıca kapatma","neighbor_only":"Kapıyı örtme, yüzeylerini bitiştirme ve sıkıca kapatma eylemini anlatır.","neighbor_ref":"root_001653/B001","relation_type":"same_field","shared_zone":"İki dal da ev ve kapı çevresinde kullanılan kavramlardır."}],"source_phrase_ar":"الوصيد الفناء لاتصاله بالربع (maqayis)؛ الوصيد فناء البيت والوصيد الباب (ayn)؛ الوصيد الفناء (sihah)","source_summary":"Toplu kaynak anlatımında eve bağlı açık alan ortak merkezdir; bağlantı, bu adlandırmanın gerekçesi olarak verilir. Bunun yanında aynı adın evin kapısını belirttiği bir kullanım da kaydedilir.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه الوصيد بمعنى فناء البيت، وبمعنى الباب، والفناء لاتصاله بالربع.","what_is_not_ar":"لا يدخل فيه إطباق الباب فعلا، ولا الوصيدة الحجرية، ولا النبات المتقارب الأصول."},"support_links":["sup_44177d56d62a6d0ff7e9"]},{"boundary":"Taştan yapılma, dağda bulunma ve hayvanları barındırma özellikleri genel çevrili alan anlamına indirgenmemelidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001653/B003","candidate_links":[{"candidate_id":"cand_e8ec6bd110cdfdf5c767","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","surface_ar":"مُّؤْصَدَةٌ"}],"gloss":"dağdaki taş hayvan barınağı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderge, hayvanları içinde tutmak ya da barındırmak için yapılmış oda benzeri çevrili bir yapıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yapı dağda bulunur ve dallardan değil taşlardan yapılmasıyla sıradan hayvan çevirmeliğinden ayrılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu yapıdan türeyen kullanım, dağda böyle bir taş barınak kurma eylemini anlatır."}}],"root_ar":"و ص د","root_id":"root_001653","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yapının dağda bulunmasını, taş malzemesini, çevrili oda biçimini ve hayvan barındırma amacını birlikte taşır.","boundary_detail":"Taştan yapılma, dağda bulunma ve hayvanları barındırma özellikleri genel çevrili alan anlamına indirgenmemelidir.","branch_image_ar":"وصيدة حجرية للمال في الجبل","concept_gloss":"dağdaki taş hayvan barınağı","contextual_glosses":[{"applicability":"Oda görünümünden çok hayvanları çevreleyip içinde tutma işlevinin öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dağda bulunma koşulunu ve oda biçimi seçeneğini açıkça belirtmez.","preserves":"Taş malzemeyi ve hayvanları çevrili alanda tutma işlevini korur."},"facet_ids":["F001","F002"],"text":"taştan hayvan çevirmeliği","usage_role":"contextual"},{"applicability":"Adlandırılan yapının kendisini değil, dağda bu yapıyı kurma eylemini anlatan kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yapı adının hayvan barındırma amacını açıkça söylemez.","preserves":"Dağda taş barınak yapma eylemini korur."},"facet_ids":["F003"],"text":"dağda taş barınak kurmak","usage_role":"contextual"}],"definition":"Dağda hayvanları barındırmak için taşlardan yapılan oda ya da çevrili alandır. Buna bağlı eylem, dağda böyle bir taş barınak kurmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderge, hayvanları içinde tutmak ya da barındırmak için yapılmış oda benzeri çevrili bir yapıdır."},{"facet_id":"F002","role":"specialization","statement":"Yapı dağda bulunur ve dallardan değil taşlardan yapılmasıyla sıradan hayvan çevirmeliğinden ayrılır."},{"facet_id":"F003","role":"associated_use","statement":"Bu yapıdan türeyen kullanım, dağda böyle bir taş barınak kurma eylemini anlatır."}],"identity_rationale":"Kaynak sözü, dağda hayvanları barındırmak için taşlardan yapılan oda ya da çevrili alanı açıkça tanımlar ve böyle bir yapı kurma eylemini de bildirir. Sağlanan dal çerçevesi yapı, malzeme, yer ve amaç sınırlarını korur.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"dağda hayvanlar için yapılan taş oda veya çevirmelik"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"dağda böyle bir taş barınak kurmak"}],"lexicalization_note":"Tanım, özel yapı adını dağda bu yapıyı kurma eyleminden ayırır ve ikisini genel bir çevreleme anlamına genişletmez.","neighbor_coverage_note":"Taş çevirmeliğe en yakın genel ve bitkisel malzemeli çevirmelikler, çevrili yer ve dağ mağarası yayımlandı; çatı, üst örtü, kapatma eylemi, avlu ve bitki dalları yapının yalnızca ortamını ya da uzak bir özelliğini paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalı belirleyen malzeme taş ve yer dağdır; komşu dal bitkisel malzemeli çevirmelikleri ve daha geniş amaçları kapsar.","focus_only":"Dağda bulunan ve özellikle taşlardan yapılan oda ya da çevrili barınaktır.","gloss":"dal veya kamıştan hayvan çevirmeliği","neighbor_only":"Tahta, kamış, ağaç ya da dallardan yapılabilir ve ekini çevreleme amacı da taşıyabilir.","neighbor_ref":"root_000338/B001","relation_type":"near_synonym","shared_zone":"İki dal da hayvanları bir arada tutan çevrili bir yapı bildirebilir."},{"boundary_match":"partial","distinction":"Komşu dal kuşatma işlevine dayalı genel çevirmeliktir; bu dal ise dağda hayvanlar için taştan yapılmış özel yapıdır.","focus_only":"Taş malzeme, dağ ortamı ve hayvan barındırma amacı zorunlu sınırlar olarak öne çıkar.","gloss":"içindekileri kuşatan çevirmelik","neighbor_only":"İçindekileri kuşatan genel bir çevirmelik olarak daha geniş kapsamlıdır.","neighbor_ref":"root_000036/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da içindekileri çevreleyip bir arada tutan barınak türünü anlatır."},{"boundary_match":"partial","distinction":"Bu dalın malzeme, yer ve kullanım amacı belirgindir; komşu dal ise çevrili mekânların genel alanıdır.","focus_only":"Dağda hayvanlar için taştan yapılan belirli bir oda ya da çevirmeliktir.","gloss":"duvarla çevrili yer","neighbor_only":"Duvarla çevrilmiş yer, oda, bahçe ve yerleşim gibi pek çok farklı mekânı kapsar.","neighbor_ref":"root_000296/B004","relation_type":"near_neighbor","shared_zone":"İki dal da sınırları belirlenmiş ve çevrelenmiş bir mekânı gösterebilir."},{"boundary_match":"field_only","distinction":"Bu dal taşla kurulan hayvan yapısıdır; komşu dal dağın içinde bulunan mağaradır ve yapım malzemesi ile hayvan amacı taşımaz.","focus_only":"Taşların bir araya getirilmesiyle hayvanlar için insan eliyle kurulan yapıdır.","gloss":"dağ mağarası","neighbor_only":"Dağın içinde doğal ya da oyulmuş geniş bir boşluktur.","neighbor_ref":"root_001325/B001","relation_type":"same_field","shared_zone":"Her iki dal da dağda bulunan, içine girilebilen ve barınma sağlayabilen bir yeri anlatır."}],"source_phrase_ar":"الوصيدة كالحظيرة تتخذ للمال إلا أنها من الحجارة والحظيرة من الغصنة واستوصدت في الجبل (sihah)؛ الوصيدة حجرة تجعل للمال في الجبل (mufradat)","source_summary":"Kaynakların ortak çekirdeği, dağda hayvanlar için yapılan taş oda ya da taşla çevrili barınaktır. Toplu anlatım ayrıca yapıyı dallardan yapılan çevirmelikten ayırır ve dağda bu yapıyı kurma eylemini kaydeder.","sources":["SI","MU"],"what_is_ar":"يدخل فيه الوصيدة: حجرة أو شبه حظيرة من حجارة تتخذ للمال في الجبل، ومنه استوصد في الجبل إذا اتخذها.","what_is_not_ar":"لا يدخل فيه الحظيرة من الغصنة عند الصحاح، ولا مطلق الفناء أو إغلاق الباب."},"support_links":["sup_21b3392510bfac082b4f"]},{"boundary":"Yakınlık bitkinin üst bölümünde değil kökler arasındadır; yalnızca sık ya da bol bitki yeterli değildir.","branch_kind":"non_bare","branch_ref":"root_001653/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","surface_ar":"مُّؤْصَدَةٌ"}],"gloss":"kökleri birbirine yakın bitki","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ayırt edici özellik, bitki köklerinin birbirine yakın aralıklarla bulunmasıdır."}}],"root_ar":"و ص د","root_id":"root_001653","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bitkiyi kökler arasındaki yakınlık ölçütüyle tanımlar ve başka bir sıklık türü eklemez.","boundary_detail":"Yakınlık bitkinin üst bölümünde değil kökler arasındadır; yalnızca sık ya da bol bitki yeterli değildir.","branch_image_ar":"نبات متقارب الأصول","concept_gloss":"kökleri birbirine yakın bitki","contextual_glosses":[{"applicability":"Kök yakınlığının yüzeyde dipten sık bir görünüm oluşturduğu betimleyici bağlamlarda kullanılabilir.","error_profile":{"adds":"Kök yakınlığı dışında genel bir örtü yoğunluğu izlenimi ekleyebilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Bitkilerin dip bölümündeki sık ve yakın düzeni korur."},"facet_ids":["F001"],"text":"dipten sık bitki örtüsü","usage_role":"contextual"}],"definition":"Kökleri birbirine yakın duran, dipten sık ve bitişik görünüm veren bitki ya da bitki topluluğudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ayırt edici özellik, bitki köklerinin birbirine yakın aralıklarla bulunmasıdır."}],"identity_rationale":"Kaynak sözü, bitkiyi köklerinin birbirine yakın olmasıyla tanımlar. Sağlanan çerçeve bu ölçütü doğru biçimde korur ve onu genel bitki sıklığı ya da dal dolaşıklığıyla karıştırmaz.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kökleri birbirine yakın bitki"}],"lexicalization_note":"Tanım yalnızca kökleri birbirine yakın bitkiyi adlandıran belirtilmiş sözcükle sınırlıdır ve genel bir kök anlamı sayılmaz.","neighbor_coverage_note":"Genel bitki yoğunluğu, dal dolaşıklığı ve üst üste dizilme en açıklayıcı karşıtlardır; belirli bitki türleri, kumda büyüme, diken filizi ve belirli ağaçlık alan adayları yalnızca bitki alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal miktar ve genel yoğunluğu öne çıkarır; bu dalda belirleyici olan bitki sayısı değil köklerin birbirine yakınlığıdır.","focus_only":"Sıklık özellikle köklerin birbirine yakın aralıklarla bulunmasına dayanır.","gloss":"yoğun bitki örtüsü","neighbor_only":"Bir yerde çok sayıda bitki ya da ağaç bulunmasına ve genel yoğun görünüme dayanır.","neighbor_ref":"root_000798/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da bitkilerin sık ve yoğun görünmesini anlatabilir."},{"boundary_match":"partial","distinction":"Bu dal köklerin yakınlığını ölçüt alır; komşu dal ise dalların çoğalması ve birbirine geçmesiyle oluşan üst bölüm yoğunluğunu anlatır.","focus_only":"Yakınlık bitkinin toprak altındaki ya da dipteki kök düzenindedir.","gloss":"dalları çok ve birbirine geçmiş ağaç","neighbor_only":"Yoğunluk dalların çokluğu ve birbirine dolanıp sıkı biçimde örtüşmesindedir.","neighbor_ref":"root_001025/B007","relation_type":"near_neighbor","shared_zone":"İki dal da bitkinin parçalarının birbirine yakın ve sık bir düzen oluşturmasını anlatır."},{"boundary_match":"partial","distinction":"Bu dal köklerin yan yana yakınlığıdır; komşu dalın belirleyici ilişkisi cisimlerin üst üste binmesi ve katmanlaşmasıdır.","focus_only":"Bitki kökleri aynı düzlemde birbirine yakın konumlanır.","gloss":"üst üste yığılma","neighbor_only":"Doğal cisimler, bulutlar ya da ürünler üst üste dizilip katman oluşturur.","neighbor_ref":"root_001515/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal doğal varlıkların aralarında az boşluk kalacak biçimde düzenlenmesini anlatabilir."}],"source_phrase_ar":"الوصيد النبت المتقارب الأصول (maqayis)؛ الوصيد النبات المتقارب الاصول (sihah)؛ الوصيد المتقارب الأصول (mufradat)","source_summary":"Kaynaklar bitkiyi ortak biçimde köklerinin birbirine yakın oluşuyla tanımlar; belirleyici ölçüt bitkinin türü, boyu ya da dal sayısı değil kökler arasındaki yakınlıktır.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه الوصيد بمعنى النبت أو النبات المتقارب الأصول.","what_is_not_ar":"لا يدخل فيه الفناء أو الباب أو الوصيدة الحجرية أو إطباق الباب إلا من جهة أصل التقارب والضم."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["104:8:1"],"branch_refs":[],"candidate_id":"cand_bc122aa639b1d9d61324","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:1:emphatic-nominal-declaration","source_type":"word_analysis","support_ids":["sup_0601b1331e7cfa26b0c4","sup_a5b634c7602bfeb2b639"],"title":"emphatic opening makes the sealed state declarative","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:1","qac_refs":["104:8:1:1","104:8:1:2"],"status":"accepted"}},{"anchor_refs":["104:8:1"],"branch_refs":[],"candidate_id":"cand_d5545d65cd4628b97dba","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:1:feminine-anaphoric-fire-subject","source_type":"word_analysis","support_ids":["sup_a5b634c7602bfeb2b639","sup_eaa46a35d1448839ac86"],"title":"bound feminine pronoun keeps the fire already present","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:1","qac_refs":["104:8:1:1","104:8:1:2"],"status":"accepted"}},{"anchor_refs":["104:8:1"],"branch_refs":[],"candidate_id":"cand_39100351800341422f31","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:1:fused-certainty-and-anaphora","source_type":"word_analysis","support_ids":["sup_09648cd0fbdf055f2c55","sup_a5b634c7602bfeb2b639"],"title":"particle and suffix fuse certainty with reference","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:1","qac_refs":["104:8:1:1","104:8:1:2"],"status":"accepted"}},{"anchor_refs":["104:8:1"],"branch_refs":[],"candidate_id":"cand_de5db96c74d4f678ff87","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:1:nasal-compressed-opening","source_type":"word_analysis","support_ids":["sup_a5b634c7602bfeb2b639","sup_e2517b6b0f7813a0b6e4"],"title":"nasal opening starts the clause's tightening sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:1","qac_refs":["104:8:1:1","104:8:1:2"],"status":"accepted"}},{"anchor_refs":["104:8:1"],"branch_refs":[],"candidate_id":"cand_1cb5c439f270825b6411","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:1:scope-into-column-specification","source_type":"word_analysis","support_ids":["sup_a5b634c7602bfeb2b639","sup_e9326941b17d3c80997c"],"title":"clause closes here but can open into the columns","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:1","qac_refs":["104:8:1:1","104:8:1:2"],"status":"accepted"}},{"anchor_refs":["104:8:2"],"branch_refs":[],"candidate_id":"cand_5b6ecc8f23e43b4582f0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:2:from-penetration-to-static-weight","source_type":"word_analysis","support_ids":["sup_454ba8add14bbdaf1500","sup_93f0fb97a2c757df8523"],"title":"overness shifts from peering motion to sealed weight","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:2","qac_refs":["104:8:2:1","104:8:2:2"],"status":"accepted"}},{"anchor_refs":["104:8:2"],"branch_refs":[],"candidate_id":"cand_d629b2721e91225b45c0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:2:fronted-target-hinge","source_type":"word_analysis","support_ids":["sup_4274d62636b9eb759a9e","sup_93f0fb97a2c757df8523"],"title":"fronted phrase fixes the target before the predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:2","qac_refs":["104:8:2:1","104:8:2:2"],"status":"accepted"}},{"anchor_refs":["104:8:2"],"branch_refs":[],"candidate_id":"cand_66a9ae265a29a3e142de","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:2:nasal-boundary-to-predicate","source_type":"word_analysis","support_ids":["sup_75caf1b8ca8df76d39ff","sup_93f0fb97a2c757df8523"],"title":"final nasal binds target to predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:2","qac_refs":["104:8:2:1","104:8:2:2"],"status":"accepted"}},{"anchor_refs":["104:8:2"],"branch_refs":[],"candidate_id":"cand_66b11607b954b5f3dd08","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:2:overhead-adversarial-pressure","source_type":"word_analysis","support_ids":["sup_4514b9bb26b254f3f463","sup_93f0fb97a2c757df8523"],"title":"upon makes the enclosure press from above","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:2","qac_refs":["104:8:2:1","104:8:2:2"],"status":"accepted"}},{"anchor_refs":["104:8:2"],"branch_refs":[],"candidate_id":"cand_42b9d29d009a24d54593","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:2:plural-bound-target-class","source_type":"word_analysis","support_ids":["sup_93f0fb97a2c757df8523","sup_d195d6f15bbe94351c1b"],"title":"plural suffix turns the profile into a class","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:2","qac_refs":["104:8:2:1","104:8:2:2"],"status":"accepted"}},{"anchor_refs":["104:8:3"],"branch_refs":[],"candidate_id":"cand_70b25f41efd94366d176","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:3:ayah-final-cadence","source_type":"word_analysis","support_ids":["sup_48587b9c8fbc607445ac","sup_6b1994e308f3b94bc6eb"],"title":"sound and syntax close together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:3","qac_refs":["104:8:3:1"],"status":"accepted"}},{"anchor_refs":["104:8:3"],"branch_refs":[],"candidate_id":"cand_35e0268b4579734e8033","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:3:boundary-from-peering-to-enclosure","source_type":"word_analysis","support_ids":["sup_48587b9c8fbc607445ac","sup_ddb45d5e8faaca996117"],"title":"dynamic peering becomes static enclosure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:3","qac_refs":["104:8:3:1"],"status":"accepted"}},{"anchor_refs":["104:8:3"],"branch_refs":[],"candidate_id":"cand_f44c41f94e6eed4de36d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:3:complete-predicate-extends-to-columns","source_type":"word_analysis","support_ids":["sup_1cfadbca42268500f39a","sup_48587b9c8fbc607445ac"],"title":"complete predicate can still point into 104:9","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:3","qac_refs":["104:8:3:1"],"status":"accepted"}},{"anchor_refs":["104:8:3"],"branch_refs":[],"candidate_id":"cand_534118e2c383be38e80c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:3:door-bolted-architecture","source_type":"word_analysis","support_ids":["sup_040f2c6cebf35ba329c6","sup_48587b9c8fbc607445ac"],"title":"door-bolting turns fire into architecture","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:3","qac_refs":["104:8:3:1"],"status":"accepted"}},{"anchor_refs":["104:8:3"],"branch_refs":[],"candidate_id":"cand_492d951fc8073715eebc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:3:feminine-predicate-agreement","source_type":"word_analysis","support_ids":["sup_48587b9c8fbc607445ac","sup_5befa8c756a8031317d9"],"title":"agreement keeps the fire as subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:3","qac_refs":["104:8:3:1"],"status":"accepted"}},{"anchor_refs":["104:8:3"],"branch_refs":[],"candidate_id":"cand_a0d627ebe113937324ab","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:3:fronted-target-restricts-predicate","source_type":"word_analysis","support_ids":["sup_48587b9c8fbc607445ac","sup_cd2942d5a0469647f68b"],"title":"fronted target routes the predicate onto them","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:3","qac_refs":["104:8:3:1"],"status":"accepted"}},{"anchor_refs":["104:8:3"],"branch_refs":[],"candidate_id":"cand_4611bc2acfb171359cec","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:3:hamza-glottal-catch","source_type":"word_analysis","support_ids":["sup_01b87186684c2023e8f6","sup_48587b9c8fbc607445ac"],"title":"hamza gives the closure an audible catch","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:3","qac_refs":["104:8:3:1"],"status":"accepted"}},{"anchor_refs":["104:8:3"],"branch_refs":[],"candidate_id":"cand_7807086ee2f7bdbdf118","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:3:indefinite-sealed-mode","source_type":"word_analysis","support_ids":["sup_48587b9c8fbc607445ac","sup_e53768839a2318625141"],"title":"tanwin leaves the mode of sealing open","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:3","qac_refs":["104:8:3:1"],"status":"accepted"}},{"anchor_refs":["104:8:3"],"branch_refs":[],"candidate_id":"cand_d0a98c915a4d54217396","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:3:khabar-landing-of-inna","source_type":"word_analysis","support_ids":["sup_48587b9c8fbc607445ac","sup_c63028260b6602ae5d02"],"title":"predicate completes the emphatic clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:3","qac_refs":["104:8:3:1"],"status":"accepted"}},{"anchor_refs":["104:8:3"],"branch_refs":[],"candidate_id":"cand_e78ee99664105aa1cf74","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:3:kindled-undertone-under-closure","source_type":"word_analysis","support_ids":["sup_48587b9c8fbc607445ac","sup_b6232964d21d85aad6d8"],"title":"kindling echo stays beneath the closure sense","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:3","qac_refs":["104:8:3:1"],"status":"accepted"}},{"anchor_refs":["104:8:3"],"branch_refs":[],"candidate_id":"cand_0d153a7547e7e2025533","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:3:passive-participle-sealed-state","source_type":"word_analysis","support_ids":["sup_1ca914669b26272b350e","sup_48587b9c8fbc607445ac"],"title":"passive participle makes closure a completed state","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:3","qac_refs":["104:8:3:1"],"status":"accepted"}},{"anchor_refs":["104:8:3"],"branch_refs":[],"candidate_id":"cand_94a6621faaedbf21a83f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:3:rare-upon-them-formula","source_type":"word_analysis","support_ids":["sup_3acb9e0bbc0e9f01ecb4","sup_48587b9c8fbc607445ac"],"title":"rare formula links this closure with 90:20","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:3","qac_refs":["104:8:3:1"],"status":"accepted"}},{"anchor_refs":["104:8:3"],"branch_refs":[],"candidate_id":"cand_10dfbf9461db666b90ac","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:3:synthesis-closure-knot","source_type":"word_analysis","support_ids":["sup_022c0bc3d3d7a53ea5ee","sup_48587b9c8fbc607445ac"],"title":"multiple pressures converge in the final word","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:3","qac_refs":["104:8:3:1"],"status":"accepted"}},{"anchor_refs":["104:8:3"],"branch_refs":[],"candidate_id":"cand_aad6131955945cfd69cc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:8:3:variant-preserves-sealed-predicate","source_type":"word_analysis","support_ids":["sup_15c65c343b61132ff6f4","sup_48587b9c8fbc607445ac"],"title":"variants test sound while preserving sealedness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:8:3","qac_refs":["104:8:3:1"],"status":"accepted"}},{"anchor_refs":["104:8:3"],"branch_refs":[],"candidate_id":"cand_70df011b556989d8121a","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000036","root_001653"],"scope":"focus_ayah","source_local_id":"104:8:3:1","source_type":"qac_morpheme","support_ids":["sup_dda0cef3b58695fb9c43"],"title":"QAC root occurrence: و ص د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["104:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:8","branch_refs":["root_000036/B001","root_001653/B001"],"candidate_id":"cand_c9024a88350aef77c079","commentary_obligation":"review","hft_ref":"hft_5d44a5384be35802a66f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_hermetic_door","source_type":"hft","support_ids":["sup_db1e92643b01c2e563f6"],"title":"baseline_hermetic_door","trust":"legacy_unbound"},{"anchor_refs":["104:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:8","branch_refs":["root_000036/B002","root_001653/B003"],"candidate_id":"cand_e8ec6bd110cdfdf5c767","commentary_obligation":"review","hft_ref":"hft_d367da04d707f6c43af5","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_total_enclosure","source_type":"hft","support_ids":["sup_21b3392510bfac082b4f"],"title":"baseline_total_enclosure","trust":"legacy_unbound"},{"anchor_refs":["104:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:8","branch_refs":["root_000036/B004","root_001653/B002"],"candidate_id":"cand_c6ef6bb179b2970db052","commentary_obligation":"review","hft_ref":"hft_c10fb620f68bf8c2e7f1","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_liminal_capture","source_type":"hft","support_ids":["sup_44177d56d62a6d0ff7e9"],"title":"baseline_liminal_capture","trust":"legacy_unbound"},{"anchor_refs":["104:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:8","branch_refs":["root_000036/B003"],"candidate_id":"cand_5e4cd83747dde09ca7c5","commentary_obligation":"review","hft_ref":"hft_2abee5983003a34c66af","kind":"surprising_outlier","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:outlier_close_worn_as_membrane","source_type":"hft","support_ids":["sup_dcc6dbecd739ec9c683e"],"title":"outlier_close_worn_as_membrane","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ","qac_morphemes":[{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"104:8:1:1","qac_word_ref":"104:8:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"104:8:1:2","qac_word_ref":"104:8:1","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"104:8:2:1","qac_word_ref":"104:8:2","root_ar":"","surface_ar":"عَلَيْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"104:8:2:2","qac_word_ref":"104:8:2","root_ar":"","surface_ar":"هِم"},{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","root_ar":"و ص د","surface_ar":"مُّؤْصَدَةٌ"}],"word_analysis_qac_refs":[["104:8:1:1","104:8:1:2"],["104:8:2:1","104:8:2:2"],["104:8:3:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["104:8:1","104:8:2","104:8:3"]},"focus_surface_evidence":{"arabic_uthmani":"إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ","qac_morphemes":[{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"104:8:1:1","qac_word_ref":"104:8:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"104:8:1:2","qac_word_ref":"104:8:1","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"104:8:2:1","qac_word_ref":"104:8:2","root_ar":"","surface_ar":"عَلَيْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"104:8:2:2","qac_word_ref":"104:8:2","root_ar":"","surface_ar":"هِم"},{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","root_ar":"و ص د","surface_ar":"مُّؤْصَدَةٌ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["104:8:1:1","104:8:1:2"],["104:8:2:1","104:8:2:2"],["104:8:3:1"]],"word_analysis_refs":["104:8:1","104:8:2","104:8:3"],"word_rows":[{"analysis_record_ref":"104:8:1","analytic_gloss_range_en":"emphatic clause opening with a bound feminine subject pronoun","analytic_root_gloss_range_en":null,"qac_refs":["104:8:1:1","104:8:1:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"إِنَّهَا","transliteration":"innahā"}},{"analysis_record_ref":"104:8:2","analytic_gloss_range_en":"fronted upon-them phrase binding the plural target to the sealed state","analytic_root_gloss_range_en":null,"qac_refs":["104:8:2:1","104:8:2:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"عَلَيْهِمْ","transliteration":"ʿalayhim"}},{"analysis_record_ref":"104:8:3","analytic_gloss_range_en":"sealed, shut, or bolted as a completed passive state in this clause","analytic_root_gloss_range_en":"closure and door-fastening pressure is locally selected; supplied fire-kindling associations can remain undertone only, not the governing sense","qac_refs":["104:8:3:1"],"root":{"arabic":"أ ص د","transliteration":"ʾ-ṣ-d"},"surface":{"arabic":"مُّؤْصَدَةٌ","transliteration":"muʾṣadatun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["104:8"],"branch_refs":["root_000036/B001","root_001653/B001"],"candidate_id":"cand_c9024a88350aef77c079","evidence_scope":"focus_ayah","hft_ref":"hft_5d44a5384be35802a66f","item_id":"baseline_hermetic_door","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_hermetic_door","support_id":"sup_db1e92643b01c2e563f6"},{"anchor_refs":["104:8"],"branch_refs":["root_000036/B002","root_001653/B003"],"candidate_id":"cand_e8ec6bd110cdfdf5c767","evidence_scope":"focus_ayah","hft_ref":"hft_d367da04d707f6c43af5","item_id":"baseline_total_enclosure","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_total_enclosure","support_id":"sup_21b3392510bfac082b4f"},{"anchor_refs":["104:8"],"branch_refs":["root_000036/B004","root_001653/B002"],"candidate_id":"cand_c6ef6bb179b2970db052","evidence_scope":"focus_ayah","hft_ref":"hft_c10fb620f68bf8c2e7f1","item_id":"baseline_liminal_capture","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_liminal_capture","support_id":"sup_44177d56d62a6d0ff7e9"},{"anchor_refs":["104:8"],"branch_refs":["root_000036/B003"],"candidate_id":"cand_5e4cd83747dde09ca7c5","evidence_scope":"focus_ayah","hft_ref":"hft_2abee5983003a34c66af","item_id":"outlier_close_worn_as_membrane","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_close_worn_as_membrane","support_id":"sup_dcc6dbecd739ec9c683e"}],"diagnostics":[],"lane_counts":{"global":9,"macro":10,"micro":4},"packet_summary":{"ayah_count":9,"focus_ref":"104:8","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"و ص د","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000036","furuq_root_norm":"ء ص د","furuq_source_root_norm":"أ ص د","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001653","furuq_root_norm":"و ص د","furuq_source_root_norm":"و ص د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]}],"window":["104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:8","104:9"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"104:8","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"104:8","lane":"micro","linguistic_source_ref":"104:8","surface_ref":"104:8","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"104:8","target_tokens":[["Gerçekten",["104:8:1"]],["o",["104:8:1"]],["üzerlerine",["104:8:2"]],["kapatılmıştır",["104:8:3"]]],"text":"Gerçekten o, üzerlerine kapatılmıştır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":9,"id":"s104-p01-001-009","label":"Whole surah","number":1,"refs":["104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:8","104:9"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:3:hamza-glottal-catch","source_type":"word_analysis","support_id":"sup_01b87186684c2023e8f6","text":"{\"blocking_evidence\":null,\"headline\":\"hamza gives the closure an audible catch\",\"reader_payoff\":\"The reader hears the Hafs surface catch inside the sealing word before the heavier closure consonants arrive.\",\"reason\":\"The sound claim is tied to the local written and recited form and remains secondary to the unchanged closure meaning.\",\"representative_source_ids\":[\"QP-11fd14dc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:3:synthesis-closure-knot","source_type":"word_analysis","support_id":"sup_022c0bc3d3d7a53ea5ee","text":"{\"blocking_evidence\":null,\"headline\":\"multiple pressures converge in the final word\",\"reader_payoff\":\"The reader sees why the final word is dense: grammar, rarity, variant surface, sound, and fire-closure tension all concentrate on inescapable sealed fire.\",\"reason\":\"The synthesis row is not a separate lexical claim; it gathers surviving grammar, distribution, variant, sound, and narrowed lexical tensions already accounted for by the other topics.\",\"representative_source_ids\":[\"QY-51f4be44\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:3:door-bolted-architecture","source_type":"word_analysis","support_id":"sup_040f2c6cebf35ba329c6","text":"{\"blocking_evidence\":null,\"headline\":\"door-bolting turns fire into architecture\",\"reader_payoff\":\"The reader pictures the fire not as loose heat but as a locked structure whose closure can be specified by the columns of 104:9.\",\"reason\":\"The supplied CRITICAL lexicon evidence for shutting or bolting is coherent with the local passive participle, but the threshold and foundation imagery is limited to architectural pressure rather than made a separate lexical sense.\",\"representative_source_ids\":[\"QS-4d97325c\",\"QS-dcfa435c\",\"QS-70c2a9bf\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:1:emphatic-nominal-declaration","source_type":"word_analysis","support_id":"sup_0601b1331e7cfa26b0c4","text":"{\"blocking_evidence\":null,\"headline\":\"emphatic opening makes the sealed state declarative\",\"reader_payoff\":\"The reader notices that the ayah relaunches the fire scene as an emphatic statement of fact, not as a continued description or conditional warning.\",\"reason\":\"QAC and attachment evidence identify an emphatic particle opening an inna-clause whose predicate is the final passive participle.\",\"representative_source_ids\":[\"QG-081f48bd\",\"MG-7c8e4ea4\",\"QT-81bfab83\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:1:fused-certainty-and-anaphora","source_type":"word_analysis","support_id":"sup_09648cd0fbdf055f2c55","text":"{\"blocking_evidence\":null,\"headline\":\"particle and suffix fuse certainty with reference\",\"reader_payoff\":\"The reader notices how the word compresses assertion and referent into one grammatical package instead of pausing to repeat the fire noun.\",\"reason\":\"The governed suffix is attached directly to the emphatic particle, so cohesion is carried by bound morphology rather than by an explicit repeated noun.\",\"representative_source_ids\":[\"QF-40374470\",\"QF-d61ab4d5\",\"MG-f54744c0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:3:variant-preserves-sealed-predicate","source_type":"word_analysis","support_id":"sup_15c65c343b61132ff6f4","text":"{\"blocking_evidence\":null,\"headline\":\"variants test sound while preserving sealedness\",\"reader_payoff\":\"The reader notices that accepted variant surfaces change the acoustic route but keep the feminine passive predicate of completed closure stable.\",\"reason\":\"Variant evidence is retained as form and sound contrast; it does not displace the local Hafs surface or the selected sealed-state sense.\",\"representative_source_ids\":[\"QF-131c264c\",\"QF-50fd89d3\",\"QF-c31551ca\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:3:passive-participle-sealed-state","source_type":"word_analysis","support_id":"sup_1ca914669b26272b350e","text":"{\"blocking_evidence\":null,\"headline\":\"passive participle makes closure a completed state\",\"reader_payoff\":\"The reader notices that the line presents an already sealed condition, not the event of someone now sealing it.\",\"reason\":\"QAC identifies the word as a feminine singular passive participle functioning as the predicate of the inna-clause.\",\"representative_source_ids\":[\"QG-05562663\",\"QF-5af2d394\",\"QT-d7e30619\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:3:complete-predicate-extends-to-columns","source_type":"word_analysis","support_id":"sup_1cfadbca42268500f39a","text":"{\"blocking_evidence\":null,\"headline\":\"complete predicate can still point into 104:9\",\"reader_payoff\":\"The reader notices that the sealed-state word can be complete here and still prepare the structural column detail in 104:9.\",\"reason\":\"The syntax of 104:8 is complete, so the 104:9 relation is retained as continuation or specification rather than as an obligatory local complement.\",\"representative_source_ids\":[\"QE-3b58f9ee\",\"QB-5523d498\",\"QB-bc680d67\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:3:rare-upon-them-formula","source_type":"word_analysis","support_id":"sup_3acb9e0bbc0e9f01ecb4","text":"{\"blocking_evidence\":null,\"headline\":\"rare formula links this closure with 90:20\",\"reader_payoff\":\"The reader sees the word as a marked closure term whose only paired occurrence shares the upon-them judgment formula in 90:20.\",\"reason\":\"The contextual profiles mark the exact root-form field as low occurrence with two instances, and the CRITICAL rows supply the concrete 90:20 formula comparison.\",\"representative_source_ids\":[\"QI-02101e8f\",\"QI-4d276c71\",\"QH-16bb272b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:2:fronted-target-hinge","source_type":"word_analysis","support_id":"sup_4274d62636b9eb759a9e","text":"{\"blocking_evidence\":null,\"headline\":\"fronted phrase fixes the target before the predicate\",\"reader_payoff\":\"The reader notices the enclosed group before the sealing word lands, so the final predicate is directed rather than generic.\",\"reason\":\"Attachment evidence makes the prepositional phrase modify the sealed predicate; the clause-level framing claim is therefore limited to foregrounding and hinge effect.\",\"representative_source_ids\":[\"QG-2fbd0c60\",\"QT-2ee010d7\",\"QT-6d3f3051\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:2:overhead-adversarial-pressure","source_type":"word_analysis","support_id":"sup_4514b9bb26b254f3f463","text":"{\"blocking_evidence\":null,\"headline\":\"upon makes the enclosure press from above\",\"reader_payoff\":\"The reader feels the sealing as overhead burden and hostile enclosure, not as mere proximity or accompaniment.\",\"reason\":\"The local preposition is a governed over-them phrase attached to the sealed state, supporting superposition and adversarial pressure.\",\"representative_source_ids\":[\"QG-334723bb\",\"MG-b190f12f\",\"QS-0e087c7a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:2:from-penetration-to-static-weight","source_type":"word_analysis","support_id":"sup_454ba8add14bbdaf1500","text":"{\"blocking_evidence\":null,\"headline\":\"overness shifts from peering motion to sealed weight\",\"reader_payoff\":\"The reader notices the boundary movement from the fire reaching into hearts in 104:7 to the fire settled over people in 104:8.\",\"reason\":\"The repeated over-them relation is coherent as a same-surah boundary observation, while the local parse keeps the phrase attached to the sealed predicate.\",\"representative_source_ids\":[\"QB-6b5a8627\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:3","source_type":"word_analysis","support_id":"sup_48587b9c8fbc607445ac","text":"{\"gloss_range\":\"sealed, shut, or bolted as a completed passive state in this clause\",\"prose\":\"{{ar:مُّؤْصَدَةٌ}} ({{tr:muʾṣadatun}}) is the predicate where the ayah finally lands: a feminine passive participle that makes closure a completed condition rather than a newly narrated act. Its agreement keeps the sealed entity tied to the feminine fire or Crusher, while the prior prepositional phrase keeps that condition directed over the plural target. The door-bolting field makes the fire read as constructed enclosure, and 104:9 can then specify that architecture with extended columns. The kindled-fire undertone from the same-surah passive participle in 104:6 survives only beneath the selected closure sense, as the scene shifts from fire reaching into hearts in 104:7 to fire closed over people in 104:8. The tanwīn leaves the mode of sealing unnamed and magnified, while the accepted smoothed variant changes the acoustic route without changing the feminine passive predicate of completed closure. The rare two-attestation formula with 90:20, the hamza catch, the heavy final cadence, and the final position all converge on a short line that closes syntactically, semantically, and acoustically.\",\"root_display\":\"{{ar:أ ص د}} ({{tr:ʾ-ṣ-d}})\",\"root_gloss_range\":\"closure and door-fastening pressure is locally selected; supplied fire-kindling associations can remain undertone only, not the governing sense\",\"surface_display\":\"{{ar:مُّؤْصَدَةٌ}} ({{tr:muʾṣadatun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:3:feminine-predicate-agreement","source_type":"word_analysis","support_id":"sup_5befa8c756a8031317d9","text":"{\"blocking_evidence\":null,\"headline\":\"agreement keeps the fire as subject\",\"reader_payoff\":\"The reader sees that the plural people are not the grammatical subject; the sealed predicate agrees with the feminine fire referent carried by the opening suffix.\",\"reason\":\"The feminine singular predicate matches the feminine suffix governed by the emphatic particle, while the plural suffix belongs to the intervening prepositional phrase.\",\"representative_source_ids\":[\"QG-5c16cc29\",\"QG-6f65f5de\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:3:ayah-final-cadence","source_type":"word_analysis","support_id":"sup_6b1994e308f3b94bc6eb","text":"{\"blocking_evidence\":null,\"headline\":\"sound and syntax close together\",\"reader_payoff\":\"The reader hears the short clause tighten into the final heavy closure word, where rhythm and syntax end together.\",\"reason\":\"The phonetic rows describe the actual final word and its boundary with the preceding phrase, and they reinforce the word's structural finality.\",\"representative_source_ids\":[\"QP-123bfb15\",\"QP-4c773ebf\",\"QP-b2070489\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:2:nasal-boundary-to-predicate","source_type":"word_analysis","support_id":"sup_75caf1b8ca8df76d39ff","text":"{\"blocking_evidence\":null,\"headline\":\"final nasal binds target to predicate\",\"reader_payoff\":\"The reader hears the target phrase run into the sealing word, making the syntactic bond audible.\",\"reason\":\"The sound observation follows the actual boundary between the prepositional phrase and the passive participle.\",\"representative_source_ids\":[\"QP-c1782a45\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:2","source_type":"word_analysis","support_id":"sup_93f0fb97a2c757df8523","text":"{\"gloss_range\":\"fronted upon-them phrase binding the plural target to the sealed state\",\"prose\":\"{{ar:عَلَيْهِمْ}} ({{tr:ʿalayhim}}) stands between the emphatic subject and the final predicate, fixing the target before the sealing word arrives. The preposition gives the enclosure an over-them, burdening direction rather than a neutral nearby location, and the bound plural suffix gathers the earlier singular culprit profile into a judged class. Across the boundary, the fire's reaching into hearts in 104:7 becomes a static weight settled over people in 104:8. Locally the phrase modifies the sealed predicate, so any broader clause-framing force is best heard as foregrounding the target rather than replacing the participial attachment. Its final nasal also runs directly into the next word, audibly binding the people to the sealed state.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:عَلَيْهِمْ}} ({{tr:ʿalayhim}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:1","source_type":"word_analysis","support_id":"sup_a5b634c7602bfeb2b639","text":"{\"gloss_range\":\"emphatic clause opening with a bound feminine subject pronoun\",\"prose\":\"{{ar:إِنَّهَا}} ({{tr:innahā}}) turns the prior fire-description into a certified nominal assertion: the scene is no longer only being characterized, but declared as a settled state. The attached feminine suffix carries the already active fire or Crusher referent forward without renaming it, so the ayah begins with certainty and anaphora fused into one word. That same opening also controls how tightly the following column phrase is heard: the clause is complete at the final sealed predicate, while 104:9 can still be read as a specification of the sealed structure. The doubled nasal opening and the short clause's nasal chain help the sound move toward sealed closure.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِنَّهَا}} ({{tr:innahā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:3:kindled-undertone-under-closure","source_type":"word_analysis","support_id":"sup_b6232964d21d85aad6d8","text":"{\"blocking_evidence\":null,\"headline\":\"kindling echo stays beneath the closure sense\",\"reader_payoff\":\"The reader notices the same-surah movement from the kindled passive participle of 104:6 to the sealed passive participle here, without replacing the local closure meaning.\",\"reason\":\"The local grammar and QAC gloss select sealed closure; supplied kindling evidence survives only as undertone because the referent is fire and 104:6 gives a same-surah passive-participle contrast.\",\"representative_source_ids\":[\"QS-680e19a4\",\"QE-a7b80680\",\"QE-d839c473\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:3:khabar-landing-of-inna","source_type":"word_analysis","support_id":"sup_c63028260b6602ae5d02","text":"{\"blocking_evidence\":null,\"headline\":\"predicate completes the emphatic clause\",\"reader_payoff\":\"The reader feels the emphatic clause wait until the last word to disclose its asserted completion: sealed.\",\"reason\":\"The word is the predicate of the emphatic nominal clause and comes after the target phrase, making final position and predication reinforce each other.\",\"representative_source_ids\":[\"QG-6af73792\",\"QT-8e17c076\",\"QT-5643223e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:3:fronted-target-restricts-predicate","source_type":"word_analysis","support_id":"sup_cd2942d5a0469647f68b","text":"{\"blocking_evidence\":null,\"headline\":\"fronted target routes the predicate onto them\",\"reader_payoff\":\"The reader notices that the final sealed property lands only after the plural target has been fixed by the preceding phrase.\",\"reason\":\"The prepositional phrase immediately precedes and modifies the passive participle, so the predicate is locally routed onto the bound plural target.\",\"representative_source_ids\":[\"QI-04ab2a3a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:2:plural-bound-target-class","source_type":"word_analysis","support_id":"sup_d195d6f15bbe94351c1b","text":"{\"blocking_evidence\":null,\"headline\":\"plural suffix turns the profile into a class\",\"reader_payoff\":\"The reader sees the earlier singular slanderer-hoarder profile broaden into a definite plural target under the same outcome.\",\"reason\":\"The third masculine plural suffix is a bound definite target, and attachment evidence licenses resolving it to the condemned class described earlier.\",\"representative_source_ids\":[\"QG-9b8f9cb8\",\"QF-8f41bed8\",\"QI-14f2d1b0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"104:8:3:1","source_type":"qac_morpheme","support_id":"sup_dda0cef3b58695fb9c43","text":"{\"lemma_ar\":\"مُّؤْصَدَة\",\"morph_features\":\"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"104:8:3:1\",\"qac_word_ref\":\"104:8:3\",\"root_ar\":\"و ص د\",\"surface_ar\":\"مُّؤْصَدَةٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:3:boundary-from-peering-to-enclosure","source_type":"word_analysis","support_id":"sup_ddb45d5e8faaca996117","text":"{\"blocking_evidence\":null,\"headline\":\"dynamic peering becomes static enclosure\",\"reader_payoff\":\"The reader notices the scene shift from fire reaching into hearts in 104:7 to fire closed over people in 104:8.\",\"reason\":\"The boundary observation is coherent with the prior ayah's action and the current ayah's passive-state predicate.\",\"representative_source_ids\":[\"QB-051dfc83\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:1:nasal-compressed-opening","source_type":"word_analysis","support_id":"sup_e2517b6b0f7813a0b6e4","text":"{\"blocking_evidence\":null,\"headline\":\"nasal opening starts the clause's tightening sound\",\"reader_payoff\":\"The reader hears the doubled nasal opening and the short clause's nasal chain as part of the movement toward sealed closure.\",\"reason\":\"The phonetic observation is local to the three-word clause and supports the compression already visible in the grammar.\",\"representative_source_ids\":[\"QP-5284ab3b\",\"QP-7be96c59\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:3:indefinite-sealed-mode","source_type":"word_analysis","support_id":"sup_e53768839a2318625141","text":"{\"blocking_evidence\":null,\"headline\":\"tanwin leaves the mode of sealing open\",\"reader_payoff\":\"The reader notices that the predicate names a kind of sealed condition without reducing it to a familiar definite seal.\",\"reason\":\"QAC marks the passive participle as indefinite with tanwīn, so the form supports open-ended quality rather than a named definite object.\",\"representative_source_ids\":[\"QF-5ad16da1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:1:scope-into-column-specification","source_type":"word_analysis","support_id":"sup_e9326941b17d3c80997c","text":"{\"blocking_evidence\":null,\"headline\":\"clause closes here but can open into the columns\",\"reader_payoff\":\"The reader notices that 104:9 may specify the same sealed structure even though 104:8 already forms a complete assertion.\",\"reason\":\"The local clause is syntactically complete at the predicate, so the wider reading is retained as a specification relation with 104:9 rather than as a required continuation.\",\"representative_source_ids\":[\"QG-6efc7b33\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:8:1:feminine-anaphoric-fire-subject","source_type":"word_analysis","support_id":"sup_eaa46a35d1448839ac86","text":"{\"blocking_evidence\":null,\"headline\":\"bound feminine pronoun keeps the fire already present\",\"reader_payoff\":\"The reader sees that the subject is not newly introduced; the feminine suffix pulls the fire or Crusher already defined in 104:4-7 into the sealed-state assertion.\",\"reason\":\"The reference evidence strongly licenses the feminine suffix as resuming the prior feminine fire entity, while allowing the local antecedent range to include the Crusher title or broader preceding scene.\",\"representative_source_ids\":[\"QG-d8c09d64\",\"QS-52edd1b5\",\"QB-279186e9\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ","ayah_ref":"104:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000036/B001","root_001653/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000036","role":"Closing over and shutting in supplies the literal completed seal and makes it a containment imposed upon those inside.","root":"و ص د","source_ref":"104:8","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001653","role":"The firmly sealed door sharpens the closure from a loose covering into a secured, exit-denying barrier.","root":"و ص د","source_ref":"104:8","source_word_indices":["3"]}],"changed_reading":{"after":"A completed seal is fastened over them from the controlling side of the boundary, making non-exit the ayah's primary spatial force.","before":"Something is simply closed."},"confidence":"strong","focus_anchor":"The passive result form مُّؤْصَدَةٌ is predicated with عَلَيْهِم, placing the completed closure over or against the occupants.","mechanism":"Both mapped roots converge on shutting a door firmly. The construction therefore presents an externally completed seal with a directional asymmetry: something can be closed upon the occupants, while they have no corresponding route outward.","model_id":"baseline_hermetic_door"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_hermetic_door","source_type":"hft","support_id":"sup_db1e92643b01c2e563f6","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ","ayah_ref":"104:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000036/B002","root_001653/B003"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000036","role":"The enclosing pen contributes containment on several sides and recasts the sealed object as an environment holding what is within.","root":"و ص د","source_ref":"104:8","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_001653","role":"The stone pen in a mountain gives the enclosure mass, depth, and a chamber-like relation to its confined contents.","root":"و ص د","source_ref":"104:8","source_word_indices":["3"]}],"changed_reading":{"after":"The entire place functions as a containing pen or chamber whose closure comes down over those held within it.","before":"A door blocks one opening."},"confidence":"strong","focus_anchor":"مُّؤْصَدَةٌ can activate not only the shut door but the containing enclosure associated with the same focus root.","mechanism":"The pen and stone chamber images change the geometry from one blocked aperture to a whole containing environment. عَلَيْهِم then reads as the enclosure closing over its contents, not merely a door somewhere beside them.","model_id":"baseline_total_enclosure"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_total_enclosure","source_type":"hft","support_id":"sup_21b3392510bfac082b4f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ","ayah_ref":"104:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000036/B004","root_001653/B002"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000036","role":"The courtyard or threshold-close supplies a liminal zone and makes failed passage, rather than mere walling, central to the closure.","root":"و ص د","source_ref":"104:8","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001653","role":"The doorway or forecourt joined to a dwelling turns the boundary into an attached interface that can decisively assign the occupants to the inside.","root":"و ص د","source_ref":"104:8","source_word_indices":["3"]}],"changed_reading":{"after":"The verse freezes a threshold at the moment it ceases to permit passage and becomes the captor of those on its inner side.","before":"The verse describes a static sealed location."},"confidence":"medium","focus_anchor":"The focus root also supplies adjoining forecourt, threshold, and doorway images, while عَلَيْهِم marks the people as the side upon which the boundary closes.","mechanism":"These branches locate the decisive action at an interface joined to a dwelling or chamber. The ayah can therefore be heard as capture at the last threshold: the boundary that might have mediated passage instead becomes the mechanism that fixes inside and outside.","model_id":"baseline_liminal_capture"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_liminal_capture","source_type":"hft","support_id":"sup_44177d56d62a6d0ff7e9","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ","ayah_ref":"104:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000036/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000036","role":"The small under-garment contributes a close-fitting layer and turns enclosure into intimate contact with the body.","root":"و ص د","source_ref":"104:8","source_word_indices":["3"]}],"changed_reading":{"after":"Exploratorily, the closure clings over them like a close-worn membrane, collapsing the distance between prisoner and prison.","before":"The seal stands at the perimeter of a room, separated from the occupants."},"confidence":"exploratory","containment":"The under-garment branch is surprising and form-distant from ordinary door closure, but it remains anchored in the focus root and gains spatial support from عَلَيْهِم. Carry it only as a tactile material analogy: downstream prose should say the seal behaves like a close-worn layer, not translate مُّؤْصَدَةٌ as clothing.","focus_anchor":"The focus participle and عَلَيْهِم permit the enclosing result to be imagined in immediate contact with those under it rather than at a distant doorway.","outlier_id":"outlier_close_worn_as_membrane"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:outlier_close_worn_as_membrane","source_type":"hft","support_id":"sup_dcc6dbecd739ec9c683e","trust":"legacy_unbound"}]}
</lane_packet_json>
