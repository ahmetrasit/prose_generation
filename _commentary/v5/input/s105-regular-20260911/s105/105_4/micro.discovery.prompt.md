# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **105:4**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s105-regular-20260911/s105/105_4/micro.discovery.json` and modify nothing
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
  "ayah_ref": "105:4",
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
{"analysis_context":{"analysis_id":"s105-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"105:4","host_surah":105,"lane_context_refs":[],"ordered_context_refs":["105:0","105:1","105:2","105:3","105:5","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, katı nesne ya da çevrili mekan anlamını değil, erişimi veya işlem yapmayı önleyen sınırlandırmayı anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000296/B001","candidate_links":[{"candidate_id":"cand_6b884ba12a183d8932d4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حِجَارَة","morph_features":"STEM|POS:N|LEM:HijaArap|ROOT:Hjr|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:4:2:2","qac_word_ref":"105:4:2","surface_ar":"حِجَارَةٍ"}],"gloss":"engelleme ve erişimi sınırlama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığa erişmeyi, ondan yararlanmayı veya onun üzerinde işlem yapmayı engelleyen sınırlandırmadır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyi dokunulması ya da yapılması yasak saymak, genel engellemenin kurallı bir uygulamasıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişinin malı üzerinde işlem yapma yetkisini yargı kararıyla kısıtlamak, çekirdeğin hukuki uygulamasıdır."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeye ulaşmanın, ondan yararlanmanın veya onun üzerinde işlem yapmanın önlenmesini anlatan genel karşılıktır.","boundary_detail":"Dal, katı nesne ya da çevrili mekan anlamını değil, erişimi veya işlem yapmayı önleyen sınırlandırmayı anlatır.","branch_image_ar":"المنع والإحاطة","concept_gloss":"engelleme ve erişimi sınırlama","contextual_glosses":[{"applicability":"Bir nesnenin, eylemin veya erişimin kuralla izin dışına çıkarıldığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kurallı biçimde izin vermeme ve erişimi önleme anlamını eksiksiz korur."},"facet_ids":["F002"],"text":"yasaklama","usage_role":"contextual"},{"applicability":"Bir kişinin malı üzerinde hukuken işlem yapmasının önlendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mal üzerindeki işlem yetkisinin yargısal olarak sınırlandırılmasını açıkça korur."},"facet_ids":["F003"],"text":"tasarruf yetkisini kısıtlama","usage_role":"explanatory"}],"definition":"Bir şeye ulaşmayı, ondan yararlanmayı ya da onun üzerinde işlem yapmayı engelleyen bir sınır koymadır. Bu çekirdek, bir şeyi yasak saymayı ve kişinin malı üzerindeki işlem yetkisini yargı kararıyla kısıtlamayı da kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığa erişmeyi, ondan yararlanmayı veya onun üzerinde işlem yapmayı engelleyen sınırlandırmadır."},{"facet_id":"F002","role":"specialization","statement":"Bir şeyi dokunulması ya da yapılması yasak saymak, genel engellemenin kurallı bir uygulamasıdır."},{"facet_id":"F003","role":"specialization","statement":"Bir kişinin malı üzerinde işlem yapma yetkisini yargı kararıyla kısıtlamak, çekirdeğin hukuki uygulamasıdır."}],"identity_rationale":"Kaynak ifadesi dalı tutarlı biçimde engelleme ve çevreleme ilkesiyle tanımlar; genel erişim engeli, yasaklama ve mal üzerinde işlem yapmanın yargı kararıyla kısıtlanması bu ilkenin açık uygulamalarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"erişimi veya işlem yapmayı engelleme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yasaklanmış, dokunulması önlenmiş şey"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"benden uzak dur; bana zarar vermen yasaktır"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sığınak ya da koruyucu dayanak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"geniş tutulmuş bir imkanı yasaklayıp daraltmak"}],"lexicalization_note":"Tanım genel engelleme çekirdeğini korur; belirli söz kalıplarındaki yasak, sığınma ve daraltma kullanımları yalnızca kendi sözcüksel karşılıklarında ele alınır.","neighbor_coverage_note":"Tüm adaylar incelendi; en güçlü iki sınır karşılaştırması yayımlandı, yalnızca koruma, aynı konu alanı veya uzak çağrışım paylaşan adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal doğrudan izin vermemenin ve engellemenin alan örneklerini öne çıkarır; odak dal ise çevreleyici sınır fikrini ve kişinin mal üzerindeki işlem yetkisinin kaldırılmasını da kendi çekirdeğine bağlar.","focus_only":"Mal üzerinde işlem yetkisinin yargısal olarak kısıtlanmasını ve genel çevreleme ilkesini de kapsar.","gloss":"yasaklama ve engelleme","neighbor_only":"Ekin veya otlak kullanımını engelleme gibi belirli arazi kullanımlarına ayrıca uzanır.","neighbor_ref":"root_000338/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir eylemi, erişimi veya yararlanmayı izin alanının dışında bırakır."},{"boundary_match":"partial","distinction":"Odak dal engeli çevreleme ve hukuki işlem kısıtıyla kurar; komşu dal ise geçişi tutan kişilerden cezai sınıra kadar daha geniş bir alıkoyma düzeni taşır.","focus_only":"Çevreleme ilkesi ile mal üzerinde işlem yapma yetkisinin hukuken sınırlandırılmasını içerir.","gloss":"alıkoyma ve yasak koyma","neighbor_only":"Kapı görevlisi, tutuklu kişi ve yeniden suç işlemeyi önleyen ceza sınırı gibi rolleri içerir.","neighbor_ref":"root_000002/B002","relation_type":"near_synonym","shared_zone":"İki dal da giriş, çıkış veya eylem imkanını bir sınırla önleme alanında buluşur."}],"source_phrase_ar":"أصل واحد مطرد وهو المنع والإحاطة (maqayis)؛ الحجر والحجر لغتان وهو الحرام (ayn;tahdhib)؛ كل شيء حجرت عليه فقد منعت عنه (jamhara)؛ حجر عليه القاضي إذا منعه من التصرف في ماله (sihah)؛ وأصل الحجر في اللغة ما حجرت عليه أي منعته (tahdhib)؛ الحجر الممنوع منه بتحريمه (mufradat)","source_summary":"Kaynakların ortak anlatımı, temel anlamı engelleme ve çevreleme olarak verir; yasaklanmış şey ile mal üzerinde işlem yapması önlenen kişi bu ortak çekirdeğin belirgin uygulamalarıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه المنع والحظر والتحريم والاعتصام والذمام والمنعة ومنع التصرف في المال","what_is_not_ar":"ليس الحجر الصلب ولا الحجرة المبنية ولا دارة القمر"},"support_links":["sup_092334f1b90a87fb6510"]},{"boundary":"Buradaki engel dışarıdan konan bir yasak değil, kişinin davranışını içeriden denetleyen anlama ve yargılama yetisidir.","branch_kind":"bare","branch_ref":"root_000296/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حِجَارَة","morph_features":"STEM|POS:N|LEM:HijaArap|ROOT:Hjr|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:4:2:2","qac_word_ref":"105:4:2","surface_ar":"حِجَارَةٍ"}],"gloss":"yanlıştan alıkoyan akıl","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Anlama ve yargılama gücü, kişiyi yapılmaması gereken davranışlardan alıkoyan içsel bir engel gibi işler."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Zihinsel yetinin düşünme ile davranışı dizginleme işlevlerinin birlikte anlatılması gereken bağlamlarda kullanılır.","boundary_detail":"Buradaki engel dışarıdan konan bir yasak değil, kişinin davranışını içeriden denetleyen anlama ve yargılama yetisidir.","branch_image_ar":"العقل الحاجز","concept_gloss":"yanlıştan alıkoyan akıl","contextual_glosses":[{"applicability":"Engelleyici işlevin bağlamdan anlaşıldığı doğal ve kısa kullanımlarda uygun karşılıktır.","error_profile":{"adds":null,"collision":"Genel zihinsel kapasite anlamıyla bağlam dışında karışabilir.","fit":"narrowing","loses":"Uygun olmayan davranıştan alıkoyma işlevini açıkça söylemez.","preserves":"Düşünme ve yargılama yetisi anlamını doğal biçimde korur."},"facet_ids":["F001"],"text":"akıl","usage_role":"general"}],"definition":"İnsanın düşünüp yargılamasını ve uygun olmayan davranışlardan kendini alıkoymasını sağlayan zihinsel yetidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Anlama ve yargılama gücü, kişiyi yapılmaması gereken davranışlardan alıkoyan içsel bir engel gibi işler."}],"identity_rationale":"Kaynak ifadesi, zihinsel yetiyi insanı uygun olmayan davranışlardan alıkoyma işlevi üzerinden tanımlar; dalın engelleyici akıl çerçevesi bu ilişkiyi doğru ve eksiksiz yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kişiyi yanlıştan alıkoyan akıl ve sağduyu"}],"lexicalization_note":"Dal yalın sözcükteki zihinsel yeti anlamını tanımlar ve başka yapılara özgü yasaklama ya da maddi çevreleme anlamlarını içeri almaz.","neighbor_coverage_note":"Tüm adaylar incelendi; zihinsel yetiyle doğrudan karışabilecek iki dal ve aynı kökün genel engelleme dalı seçildi, yalnızca sonuç veya konu yakınlığı taşıyanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekler çok yakındır; odak dal uygun olmayan davranış ölçüsünü daha genel kurarken komşu dal engeli özellikle çirkin davranış ekseninde belirginleştirir.","focus_only":"Yapılması uygun olmayan davranışların bütününe karşı işleyen genel zihinsel yetiyi anlatır.","gloss":"kötü davranıştan alıkoyan akıl","neighbor_only":"Özellikle çirkin davranışı durduran zihinsel uyarı yönünü öne çıkarır.","neighbor_ref":"root_001560/B003","relation_type":"near_synonym","shared_zone":"Her iki dalda da akıl, kişiyi yanlış veya çirkin davranıştan geri tutan içsel güçtür."},{"boundary_match":"partial","distinction":"Odak dalın ayırıcı çekirdeği davranışı engelleme işlevidir; komşu dal aynı yetinin bilgi edinme, anlama ve sağlam karar verme boyutlarını da bağımsız bileşenler olarak taşır.","focus_only":"Zihinsel yetinin davranış üzerinde engelleyici bir sınır kurmasını merkez alır.","gloss":"anlama ve kendini dizginleme gücü","neighbor_only":"Bilgi, ayırt etme, anlama ve sağlam karar verme gibi bilişsel işlevleri daha geniş biçimde kapsar.","neighbor_ref":"root_001036/B001","relation_type":"near_synonym","shared_zone":"İki dal da anlayan, ayırt eden ve kişiyi yanlış davranıştan geri tutan zihinsel yetiyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal bir zihinsel yetiyi adlandırır; komşu dal ise nesnelere, eylemlere veya mal üzerindeki işlemlere getirilen engelleme eylemini ve durumunu adlandırır.","focus_only":"Engeli kuran şey kişinin kendi anlama ve yargılama yetisidir.","gloss":"içsel davranış engeli","neighbor_only":"Engel dışarıdan konan yasak, erişim sınırı veya yargısal işlem kısıtı olabilir.","neighbor_ref":"root_000296/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir eylemi yapılmaması gereken sınırın gerisinde tutma düşüncesini paylaşır."}],"source_phrase_ar":"العقل يسمى حجرا لأنه يمنع من إتيان ما لا ينبغي (maqayis)؛ والحجر العقل (jamhara)؛ والحجر العقل (sihah)؛ والحجر اللب والعقل (tahdhib)؛ فقيل للعقل حجر لكون الإنسان في منع منه مما تدعو إليه نفسه (mufradat)","source_summary":"Kaynaklar zihinsel yetiyi yalnızca düşünme gücü olarak değil, kişinin isteklerini denetleyip onu uygun olmayan eylemden geri tutan bir iç sınır olarak açıklar.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحجر بمعنى العقل واللب الذي يمنع صاحبه مما لا ينبغي","what_is_not_ar":"ليس التحريم ولا الحجر على المال ولا الحجارة"},"support_links":[]},{"boundary":"Dalın çekirdeği sert taş nesnesidir; türemiş eylemler, deyimsel felaket anlatımı ve altın-gümüş ikilisi yalnızca kendi birimleriyle sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000296/B003","candidate_links":[{"candidate_id":"cand_0819d1aab4a78d02a5c7","lane":"micro"},{"candidate_id":"cand_76be9c458609695a8d5d","lane":"micro"},{"candidate_id":"cand_6b884ba12a183d8932d4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حِجَارَة","morph_features":"STEM|POS:N|LEM:HijaArap|ROOT:Hjr|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:4:2:2","qac_word_ref":"105:4:2","surface_ar":"حِجَارَةٍ"}],"gloss":"taş","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bilinen sert ve katı taş nesnesini, tek bir parçayı ve aynı türden taşların çoğulunu anlatır."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sert ve katı doğal nesnenin tekil ya da tür adı olarak karşılandığı genel bağlamlarda kullanılır.","boundary_detail":"Dalın çekirdeği sert taş nesnesidir; türemiş eylemler, deyimsel felaket anlatımı ve altın-gümüş ikilisi yalnızca kendi birimleriyle sınırlıdır.","branch_image_ar":"الحَجَر الصلب","concept_gloss":"taş","contextual_glosses":[{"applicability":"Nesnenin katılığı ile tek bir parça oluşunun açıkça belirtilmesi gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taşın sert ve katı bir nesne oluşunu, tek parça görünümüyle birlikte korur."},"facet_ids":["F001"],"text":"sert taş parçası","usage_role":"explanatory"}],"definition":"Doğada bulunan, sert ve katı yapılı bilinen taş nesnesi ile bu nesnenin tekil ve çoğul örnekleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bilinen sert ve katı taş nesnesini, tek bir parçayı ve aynı türden taşların çoğulunu anlatır."}],"identity_rationale":"Kaynak ifadesi dal düzeyinde bilinen sert taşı ve onun çoğul biçimlerini açıkça destekler. Geçici çerçevedeki taşlaşma, deyim ve özel adlandırmalar ise ayrı sözcüksel birimlerde bulunur ve yalın taş çekirdeğinin kurucu parçaları sayılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"taş; taşlar"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"taşlaşmak ve sertleşmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"başına çok çetin bir kişi ya da ağır bir iş gelmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"altın ve gümüş"}],"lexicalization_note":"Tanım yalın taş anlamını temel alır; taşlaşma, deyimsel kullanım ve özel ikili adlandırma ayrı sözcüksel karşılıklarda tutulur.","neighbor_coverage_note":"Tüm adaylar incelendi; genel taşla en kolay karışan iri kaya ve çakıl dalları ile aynı kökün çevrili mekan dalı yayımlandı, uzak deyim ve nitelik benzerlikleri elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sıradan boyuttaki taşı da kapsayan genel addır; komşu dal ise aynı nesne alanını büyüklük ve kaya kütlesi niteliğiyle daraltır.","focus_only":"Boyut bakımından büyük olma şartı taşımayan genel taş türünü ve çoğulunu kapsar.","gloss":"iri ve sert kaya","neighbor_only":"Özellikle büyük ve kütleli kaya ya da iri taş olma sınırını taşır.","neighbor_ref":"root_000847/B001","relation_type":"near_synonym","shared_zone":"İki dal da sert, katı ve doğal taş maddesinden oluşan nesneleri adlandırır."},{"boundary_match":"partial","distinction":"Odak dal boyut ve zemin türü bakımından sınırsız genel taş adıdır; komşu dal küçük çakıl boyutuna ve çakıllı yüzeye özgüdür.","focus_only":"Küçük ya da büyük her türlü sıradan taş parçasını kapsayabilir.","gloss":"çakıl ve küçük taş","neighbor_only":"Küçük, yuvarlanmış çakıl parçalarını ve bunlarla kaplı zemini özellikle adlandırır.","neighbor_ref":"root_000332/B001","relation_type":"near_synonym","shared_zone":"Her iki dal taş maddesinden oluşan ayrık parçaları anlatır."},{"boundary_match":"partial","distinction":"Odak dal sınırı oluşturan malzeme ya da nesnedir; komşu dal ise bu veya başka bir sınırın içinde kalan mekandır.","focus_only":"Sınır kurup kurmamasından bağımsız olarak taş maddesini ve taş parçasını adlandırır.","gloss":"taş ile çevrili yer ayrımı","neighbor_only":"Taş veya duvarla çevrilmiş alanı, odayı, ağılı ya da yerleşim bölümünü adlandırır.","neighbor_ref":"root_000296/B004","relation_type":"near_neighbor","shared_zone":"Çevrili mekanın sınırı taşla kurulabildiği için iki dal aynı somut sahnede buluşabilir."}],"source_phrase_ar":"والحجر معروف (maqayis)؛ الأحجار جمع الحجر والحجارة جمع الحجر أيضا (ayn)؛ الحجر معروف ويجمع أحجارا وحجارة (jamhara)؛ الحجر جمعه في القلة أحجار وفي الكثرة حجار وحجارة (sihah)؛ الحجر وجمعه الحجارة (tahdhib)؛ الحجر الجوهر الصلب المعروف وجمعه أحجار وحجارة (mufradat)","source_summary":"Kaynaklar ortak biçimde bilinen sert taş nesnesini tanır ve bu nesne için birden çok çoğul biçimin kullanıldığını belirtir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحجر المعروف والحجارة والصلابة والتحجر وما يلحق بذلك من أمثال وأسماء مبنية على الحجارة","what_is_not_ar":"ليس الحرام ولا العقل ولا الحجرة المحوطة"},"support_links":["sup_092334f1b90a87fb6510","sup_0cfb5995aa42493eee81","sup_e12af88c6d6fb2856c10"]},{"boundary":"Dal sınırın yapıldığı taşı veya duvarı değil, sınırın içinde kalan yeri ve bu modele göre adlandırılmış mekanları anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000296/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حِجَارَة","morph_features":"STEM|POS:N|LEM:HijaArap|ROOT:Hjr|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:4:2:2","qac_word_ref":"105:4:2","surface_ar":"حِجَارَةٍ"}],"gloss":"çevrili yer","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir sınır, duvar veya taş çevre içinde kalan ve dışarıdan ayrılan mekandır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir yapının içindeki oda ya da ayrılmış bölüm, çevrili mekanın yapı içindeki uygulamasıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hayvanları bir arada tutan çevrili ağıl, çekirdeğin barınak uygulamasıdır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir topluluğun evinin veya yerleşiminin yanı ve korunan çevresi, mekan çekirdeğinin alan uzantısıdır."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Kaynaklarda kutsal bir yapının çevrili yanı ile eski bir topluluğun yurdu da bu çevreleme modeline göre adlandırılır."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Duvar, taş veya başka bir sınır içinde kalan mekanın genel ve türden bağımsız karşılığıdır.","boundary_detail":"Dal sınırın yapıldığı taşı veya duvarı değil, sınırın içinde kalan yeri ve bu modele göre adlandırılmış mekanları anlatır.","branch_image_ar":"المكان المحوط","concept_gloss":"çevrili yer","contextual_glosses":[{"applicability":"Bir yapının içinde duvarlarla ayrılmış yaşama veya kullanma bölümü anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapı içinde sınırlarla ayrılmış kapalı bölüm anlamını eksiksiz korur."},"facet_ids":["F002"],"text":"oda","usage_role":"contextual"},{"applicability":"Hayvanların çevrili bir alanda tutulduğu barınak bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanları sınır içinde bir arada tutan çevrili barınak anlamını korur."},"facet_ids":["F003"],"text":"ağıl","usage_role":"contextual"},{"applicability":"Bir evin ya da yerleşimin yakınındaki ayrılmış ve korunan alan anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yerleşimin yakınında sınırlandırılmış ve korunan alan anlamını tam olarak korur."},"facet_ids":["F004"],"text":"korunan çevre","usage_role":"explanatory"}],"definition":"Duvar, taş dizisi ya da başka bir sınırla çevrilmiş ve dışarıdan ayrılmış yerdir. Oda, hayvan ağılı, bir yerleşimin yanı ve bu çevreleme modeline göre adlandırılmış belirli mekanlar bu çekirdeğin uygulamalarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir sınır, duvar veya taş çevre içinde kalan ve dışarıdan ayrılan mekandır."},{"facet_id":"F002","role":"specialization","statement":"Bir yapının içindeki oda ya da ayrılmış bölüm, çevrili mekanın yapı içindeki uygulamasıdır."},{"facet_id":"F003","role":"specialization","statement":"Hayvanları bir arada tutan çevrili ağıl, çekirdeğin barınak uygulamasıdır."},{"facet_id":"F004","role":"extension","statement":"Bir topluluğun evinin veya yerleşiminin yanı ve korunan çevresi, mekan çekirdeğinin alan uzantısıdır."},{"facet_id":"F005","role":"source_variant","statement":"Kaynaklarda kutsal bir yapının çevrili yanı ile eski bir topluluğun yurdu da bu çevreleme modeline göre adlandırılır."}],"identity_rationale":"Kaynak ifadesi oda, duvarla çevrili yer, hayvan ağılı, evin yanı ve belirli kutsal ya da eski yer adlarını çevrilmiş alan ilişkisiyle birlikte verir; mekan merkezli dal çerçevesi bu ortak yapıyı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kutsal yapının çevrili yan bölümü"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"eski bir topluluğun yurt edindiği bölge"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"oda, çevrili yer veya ağıl"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"topluluğun evinin yanı ya da korunan çevresi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"vadide veya çukur yerde suyu tutan setli alan"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bahçe, koruluk veya köy çevresindeki korunan alan"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"çevrili bir yer edinmek"}],"lexicalization_note":"Genel çevrili mekan çekirdeği ile oda ve ağıl uygulamaları tanımda ayrılır; belirli yapı, yer, su tutma alanı ve köy çevresi kullanımları kendi birimlerine bağlı kalır.","neighbor_coverage_note":"Tüm adaylar incelendi; ağıl, duvar ve ayrılmış yapı bölümüyle kurulan en açıklayıcı üç sınır yayımlandı, yalnızca aynı sahneyi paylaşan uzak mekan adayları elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal hayvan ağılına ve kapsama işlevine özgüdür; odak dal aynı çevreleme düzenini odadan yerleşim çevresine kadar daha geniş mekanlara taşır.","focus_only":"Oda, ev yanı, kutsal yapı bölümü ve geniş yerleşim alanı gibi farklı mekan türlerini kapsar.","gloss":"çevrili ağıl","neighbor_only":"İçindekileri bir arada tutan ağıl olma işlevini adlandırmanın açık merkezi yapar.","neighbor_ref":"root_000036/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir sınırın içindekileri dışarıdan ayırdığı çevrili mekanı anlatır."},{"boundary_match":"partial","distinction":"Odak dal çevrelenen iç mekandır; komşu dal ise bu mekanı oluşturan dik sınır yapısıdır ve iç alanın kendisi yerine duvarı öne çıkarır.","focus_only":"Duvarın veya sınırın içinde kalan oda, ağıl ya da bölgeyi adlandırır.","gloss":"çevrili alan ile duvar ayrımı","neighbor_only":"Alanı çevreleyen yükseltilmiş duvarı, seti veya suyu tutan yapı unsurunu adlandırır.","neighbor_ref":"root_000228/B001","relation_type":"near_neighbor","shared_zone":"Bir duvarın çevrelediği mekan sahnesinde iki dal doğrudan yan yana bulunur."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği yalnızca çevrilmiş olmaktır; komşu dal ise büyük yapı ya da yapı içindeki özel ayrılmış kesim türlerini kendi adlandırma alanına alır.","focus_only":"Basit oda, hayvan ağılı ve yerleşim çevresi gibi büyük yapı niteliği gerektirmeyen mekanları kapsar.","gloss":"ayrılmış yapı bölümü","neighbor_only":"Büyük yapı olarak sarayı ve ev ya da ibadet yapısı içindeki özel ayrılmış bölümü kapsar.","neighbor_ref":"root_001231/B005","relation_type":"near_neighbor","shared_zone":"İki dal da duvarlarla belirlenmiş bir yapı veya yapı içi bölüm alanında buluşur."}],"source_phrase_ar":"حجرة القوم ناحية دارهم والحجرة من الأبنية معروفة (maqayis)؛ الحجر حطيم مكة وحجر موضع كان لثمود والحجرة ناحية كل موضع (ayn)؛ الحجر حجر الكعبة والحجر بلاد ثمود والحجرة الحائط يحجر على دار (jamhara)؛ الحجرة حظيرة الإبل ومنه حجرة الدار والحجر حجر الكعبة والحجر منازل ثمود (sihah)؛ الحجرة التي ينزلها الناس وهو ما حوطوا عليه (tahdhib)؛ سمي ما أحيط به الحجارة حجرا وبه سمي حجر الكعبة وديار ثمود (mufradat)","source_summary":"Kaynaklar çevrelenerek ayrılmış yer çekirdeğinde birleşir; oda, duvarlı bölüm, hayvan ağılı, evin yakını, kutsal bir yapının yanı ve eski bir yerleşim alanı bu mekan düzeninin farklı gerçekleşmeleridir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحجرة والحائط والحظيرة وحجر الكعبة وديار ثمود والحديقة والحاجر ومحجر القرية","what_is_not_ar":"ليس الحِجر بمعنى الحضن ولا دارة القمر ولا الفرس الأنثى"},"support_links":[]},{"boundary":"Dal genel yasaklamayı ya da yapı içindeki odayı değil, kucak alanını ve bir kişinin yakın koruması altında bulunma durumunu anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000296/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حِجَارَة","morph_features":"STEM|POS:N|LEM:HijaArap|ROOT:Hjr|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:4:2:2","qac_word_ref":"105:4:2","surface_ar":"حِجَارَةٍ"}],"gloss":"kucak ve yakın koruma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanın gövdesi ile bacakları arasında, birini veya bir şeyi yakında tutmaya yarayan kucak alanıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birinin kucağında ya da kanadı altında olmak, onun yakın koruması ve denetimi altında bulunmayı anlatır."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedensel kucak alanı ile bundan gelişen koruma ilişkisini birlikte karşılamanın gerektiği genel açıklamalarda kullanılır.","boundary_detail":"Dal genel yasaklamayı ya da yapı içindeki odayı değil, kucak alanını ve bir kişinin yakın koruması altında bulunma durumunu anlatır.","branch_image_ar":"الحِجر والحضن","concept_gloss":"kucak ve yakın koruma","contextual_glosses":[{"applicability":"Bir insanın otururken gövdesi ile bacakları arasındaki yakın tutma alanı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedensel yakınlık ve birini ya da bir şeyi sararak tutma alanını korur."},"facet_ids":["F001"],"text":"kucak","usage_role":"general"},{"applicability":"Bir kişinin başka birinin yakın koruması ve denetimi altında bulunduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Birinin yakın koruması ve gözetimi altında bulunma ilişkisini doğal biçimde korur."},"facet_ids":["F002"],"text":"kanadı altında","usage_role":"contextual"}],"definition":"İnsanın otururken gövdesi ile bacakları arasında oluşan, birini ya da bir şeyi yakınında tutup sardığı kucak alanıdır. Bu bedensel yakınlık, birinin koruması ve denetimi altında bulunma ilişkisine de uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanın gövdesi ile bacakları arasında, birini veya bir şeyi yakında tutmaya yarayan kucak alanıdır."},{"facet_id":"F002","role":"extension","statement":"Birinin kucağında ya da kanadı altında olmak, onun yakın koruması ve denetimi altında bulunmayı anlatır."}],"identity_rationale":"Kaynak ifadesi insanın, özellikle kadının, kucağını ve birinin kucağında ya da kanadı altında bulunmayı birlikte verir; yakın bedensel alan ile bu alandan gelişen koruma ilişkisi dal çerçevesinde doğru biçimde ayrılabilir.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kucak, yakın sığınak ve koruma"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"birinin kanadı ve denetimi altında"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"gömleğin içinde bir şeyi tutan kıvrım"}],"lexicalization_note":"Kucak anlamı ile yakın koruma uzantısı tanımda ayrılır; birinin kanadı altında bulunma ve gömlek kıvrımı kullanımları kendi sözcüksel birimleriyle sınırlıdır.","neighbor_coverage_note":"Tüm adaylar incelendi; sığınak, sarılma ve genel engelleme ile kurulabilecek başlıca karışıklıklar yayımlandı, yalnızca aile veya koruma sahnesini uzaktan paylaşanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal korumayı kucak ve kişisel yakınlık üzerinden kurar; komşu dal ise kişiden bağımsız fiziksel siperleri ve doğa koşullarından saklanmayı da kapsar.","focus_only":"İnsanın bedensel kucak alanını ve bu alana dayalı yakın denetimi içerir.","gloss":"sığınak ve kanat altı","neighbor_only":"Rüzgar, soğuk veya güneşten koruyan ağaç ve benzeri siperleri de kapsar.","neighbor_ref":"root_000513/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişi ya da nesnenin yakınına girerek korunma durumunu anlatır."},{"boundary_match":"partial","distinction":"Odak dal bir yer ve koruma ilişkisi olarak kucağı anlatır; komşu dal ise bedenlerin birbirine sarılması eylemini anlatır.","focus_only":"Kucak olarak kullanılan bedensel alanı ve orada korunma durumunu adlandırır.","gloss":"kucak ile sarılma ayrımı","neighbor_only":"İki bedenin birbirine sarılması ve bu temasın sürdürülmesi eylemini adlandırır.","neighbor_ref":"root_001354/B005","relation_type":"near_neighbor","shared_zone":"İki dal bedensel yakınlık, sarma ve temas sahnesini paylaşır."},{"boundary_match":"partial","distinction":"Odak dal korumayı kucak ve kişisel yakınlık ilişkisiyle somutlaştırır; komşu dalın çekirdeği ise herhangi bir erişim ya da işlemi engellemektir.","focus_only":"Yakın bedensel alanı ve bir kişinin koruması altında bulunmayı içerir.","gloss":"yakın koruma ile engelleme ayrımı","neighbor_only":"Genel erişim yasağını ve mal üzerinde işlem yapma yetkisinin hukuken kısıtlanmasını içerir.","neighbor_ref":"root_000296/B001","relation_type":"near_neighbor","shared_zone":"Korunan kişiye dışarıdan müdahaleyi önleme düşüncesi iki dalı birbirine bağlar."}],"source_phrase_ar":"الحجر حجر الإنسان وقد تكسر حاؤه (maqayis)؛ حجر المرأة وحجرها لغتان للحضنين (ayn)؛ حجر المرأة وقالوا حجرها (jamhara)؛ حجر الإنسان وحجره والجمع حجور (sihah)؛ حجر المرأة وحجرها حضنها وفلان حجر فلان أي في كنفه ومنعته (tahdhib)؛ فلان في حجر فلان أي في منع منه وجمعه حجور (mufradat)","source_summary":"Kaynaklar kucak alanını ortak çekirdek olarak verir; bir kişinin yakınında, korumasında ve denetimi altında bulunma ilişkisi bu bedensel alandan gelişen uzantıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه حجر الإنسان وحجر المرأة والحضن والكنف والمنعة القريبة","what_is_not_ar":"ليس حجر القاضي على المال ولا حجر الكعبة ولا الحجر الصلب"},"support_links":[]},{"boundary":"Dal her türlü daireselliği kapsamaz; bir nesnenin, özellikle ayın ya da gözün, çevresini belirleyen halka, iz ve bölgeyle sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000296/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حِجَارَة","morph_features":"STEM|POS:N|LEM:HijaArap|ROOT:Hjr|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:4:2:2","qac_word_ref":"105:4:2","surface_ar":"حِجَارَةٍ"}],"gloss":"çevreleyen halka veya sınır","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesnenin çevresini halka, çizgi veya belirgin bölge halinde kuşatan çevre sınırıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayın çevresinde beliren ince halka, çevre sınırının gökyüzündeki görünümüdür."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir hayvanın göz çevresine yuvarlak damga vurmak, halka biçimli sınırı kasıtlı olarak oluşturma eylemidir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Göz çukuru çevresi ile yüz örtüsünün göz çevresine oturduğu bölüm, çekirdeğin bedensel alan uzantısıdır."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin çevresini halka, çizgi ya da belirgin bölge olarak kuşatan biçimin genel karşılığıdır.","boundary_detail":"Dal her türlü daireselliği kapsamaz; bir nesnenin, özellikle ayın ya da gözün, çevresini belirleyen halka, iz ve bölgeyle sınırlıdır.","branch_image_ar":"الدائرة حول الشيء","concept_gloss":"çevreleyen halka veya sınır","contextual_glosses":[{"applicability":"Ayın çevresinde ince ve yuvarlak bir ışık kuşağı görüldüğü gökyüzü bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ayın çevresinde beliren ince ve yuvarlak halka görünümünü açıkça korur."},"facet_ids":["F002"],"text":"ayın çevresindeki ışık halkası","usage_role":"contextual"},{"applicability":"Bir hayvanın gözünün çevresinin yuvarlak bir damgayla işaretlendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın göz çevresinde damgayla yuvarlak bir iz oluşturma eylemini tam korur."},"facet_ids":["F003"],"text":"göz çevresine yuvarlak damga vurmak","usage_role":"explanatory"},{"applicability":"Gözün çevresindeki anatomik bölge veya yüz örtüsünün göz yanında durduğu kesim anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gözün çevresindeki belirgin yüz bölgesini ve sınır niteliğini korur."},"facet_ids":["F004"],"text":"göz çukuru çevresi","usage_role":"contextual"}],"definition":"Bir şeyin, özellikle ayın ya da gözün, çevresini halka, ince çizgi veya belirgin bir bölge halinde kuşatan çevredir. Hayvan gözünün çevresine yuvarlak damga vurma eylemi bu biçimi kasıtlı olarak oluşturur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesnenin çevresini halka, çizgi veya belirgin bölge halinde kuşatan çevre sınırıdır."},{"facet_id":"F002","role":"specialization","statement":"Ayın çevresinde beliren ince halka, çevre sınırının gökyüzündeki görünümüdür."},{"facet_id":"F003","role":"associated_use","statement":"Bir hayvanın göz çevresine yuvarlak damga vurmak, halka biçimli sınırı kasıtlı olarak oluşturma eylemidir."},{"facet_id":"F004","role":"extension","statement":"Göz çukuru çevresi ile yüz örtüsünün göz çevresine oturduğu bölüm, çekirdeğin bedensel alan uzantısıdır."}],"identity_rationale":"Kaynak ifadesi ayın çevresindeki halka, hayvan gözünün çevresine vurulan yuvarlak damga ve göz çevresi bölgesini ortak bir çevre çizgisi ilişkisiyle birleştirir. Dal korunabilir, ancak çekirdek dönme eylemi değil bir şeyi kuşatan halka, iz veya çevre bölgesidir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"ayın çevresinde ince bir halka belirmek"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"hayvanın göz çevresine yuvarlak damga vurmak"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"göz çukuru çevresi veya yüz örtüsünün gözü açıkta bırakan bölümü"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"çocukların çizilmiş bir çember çevresinde oynadığı oyun"}],"lexicalization_note":"Genel çevre halkası çekirdeği korunur; ay halkası, göz çevresine damga vurma, göz çevresi bölgesi ve çocuk oyunu yalnızca kendi yapılardaki kullanımlarıyla ayrılır.","neighbor_coverage_note":"Tüm adaylar incelendi; ay halkası, genel dairesellik ve çevresini kuşatma ile kurulan üç temel sınır yayımlandı, yalnızca biçim ya da aynı sahne çağrışımı taşıyanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ay bağlamında karşılıklar çok yakındır; odak dal aynı çevre biçimini göz çevresi ve yuvarlak damga alanına da taşırken komşu dal yalnızca ay halkasına özgüdür.","focus_only":"Göz çevresi, yüz bölgesi ve göz çevresine vurulan yuvarlak damga kullanımlarını da kapsar.","gloss":"ayın çevresindeki halka","neighbor_only":"Ay çevresindeki ışık görünümünü bağımsız ve yalnızca gökyüzüne özgü bir anlam olarak adlandırır.","neighbor_ref":"root_001613/B003","relation_type":"near_synonym","shared_zone":"İki dal da ayın çevresinde görülen yuvarlak kuşağı doğrudan anlatır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği çevreleyen sınırın kendisidir; komşu dal ise hem daire biçimini hem de dönme ve döndürme hareketini kapsayan daha geniş bir süreç alanına sahiptir.","focus_only":"Bir nesnenin çevresini kuşatan sabit halka, iz veya anatomik bölgeyi merkez alır.","gloss":"çevre halkası ile dönme ayrımı","neighbor_only":"Dönme eylemini, dönüş döngüsünü ve döndürülen araç ya da nesneleri geniş biçimde kapsar.","neighbor_ref":"root_000499/B001","relation_type":"near_neighbor","shared_zone":"Daire biçimi ve bir merkez çevresinde düzenlenme iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal çevrede oluşan biçim veya bölgedir; komşu dal ise katılımcıların bir nesnenin etrafını çevirmesi eylemidir.","focus_only":"Halka, ince çizgi, damga izi veya göz çevresi gibi kalıcı ya da görünür sınırı adlandırır.","gloss":"çevre çizgisi ile kuşatma ayrımı","neighbor_only":"İnsanların veya başka ögelerin bir şeyin çevresinde toplanıp onu kuşatması eylemini adlandırır.","neighbor_ref":"root_000300/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal bir merkezin bütün çevresinin sarılması ilişkisini taşır."}],"source_phrase_ar":"حجر القمر إذا صارت حوله دارة وحجرت عين البعير إذا وسمت حولها بميسم مستدير ومحجر العين ما يدور بها (maqayis)؛ المحجر حيث يقع عليه النقاب من الوجه (ayn)؛ حجر القمر إذا صارت حوله دارة وحجرت عين البعير إذا وسمت حولها بميسم مستدير ومحجر العين معروف (jamhara)؛ حجر القمر إذا استدار بخط دقيق والتحجير أن تسم حول عين البعير بميسم مستدير (sihah)؛ المحجر من الوجه حيث يقع عليه النقاب والمحجر العين (tahdhib)؛ حجرت عين الفرس إذا وسمت حولها بميسم وحجر القمر صار حوله دائرة ومحجر العين منه (mufradat)","source_summary":"Kaynak anlatımı ay çevresindeki ince halkayı, hayvan gözünün çevresine vurulan yuvarlak damgayı ve göz ya da yüz çevresindeki bölgeyi aynı çevreleme biçiminin farklı uygulamaları olarak bir araya getirir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه دارة القمر والوسم المستدير حول عين الدابة ومحجر العين وما يشبه الخط المستدير","what_is_not_ar":"ليس الحائط والحجرة ولا الحجر بمعنى الحرام"},"support_links":[]},{"boundary":"Dal genel olarak dişi hayvanı değil dişi atı anlatır; koruma ve damızlık için ayırma bu referentin belirgin fakat kaynaklarda farklı vurgulanan nitelikleridir.","branch_kind":"bare","branch_ref":"root_000296/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حِجَارَة","morph_features":"STEM|POS:N|LEM:HijaArap|ROOT:Hjr|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:4:2:2","qac_word_ref":"105:4:2","surface_ar":"حِجَارَةٍ"}],"gloss":"dişi at, özellikle damızlık kısrak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Referent, genel hayvan türü içinde özellikle dişi attır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişi atın üreme için ayrılması, özenle korunması ve yalnızca seçilmiş bir erkekle çiftleştirilmesi belirgin yetiştirme uygulamasıdır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Adlandırma, dişi atın karnında yavru taşıyıp onu içinde barındırmasıyla da açıklanır."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişi at çekirdeği ile üreme için ayrılıp korunma niteliğinin birlikte gösterilmesi gereken genel açıklamalarda kullanılır.","boundary_detail":"Dal genel olarak dişi hayvanı değil dişi atı anlatır; koruma ve damızlık için ayırma bu referentin belirgin fakat kaynaklarda farklı vurgulanan nitelikleridir.","branch_image_ar":"الفرس الأنثى المصونة","concept_gloss":"dişi at, özellikle damızlık kısrak","contextual_glosses":[{"applicability":"Yalnızca hayvanın cinsiyeti ve türünün gerekli olduğu doğal metin bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dişi at referentini kısa ve doğal biçimde eksiksiz korur."},"facet_ids":["F001"],"text":"kısrak","usage_role":"general"},{"applicability":"Dişi atın üreme için ayrılıp özenle korunduğu yetiştiricilik bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalnızca seçilmiş bir erkekle çiftleştirilme koşulunu açıkça belirtmez.","preserves":"Dişi atın üreme amacıyla ayrılması ve korunması anlamını korur."},"facet_ids":["F002"],"text":"damızlık kısrak","usage_role":"contextual"}],"definition":"Dişi at, özellikle üreme için ayrılıp korunan ve yalnızca seçilmiş bir erkekle çiftleştirilen kısraktır. Adlandırma kaynaklarda ayrıca karnında yavru taşımasına bağlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Referent, genel hayvan türü içinde özellikle dişi attır."},{"facet_id":"F002","role":"specialization","statement":"Dişi atın üreme için ayrılması, özenle korunması ve yalnızca seçilmiş bir erkekle çiftleştirilmesi belirgin yetiştirme uygulamasıdır."},{"facet_id":"F003","role":"source_variant","statement":"Adlandırma, dişi atın karnında yavru taşıyıp onu içinde barındırmasıyla da açıklanır."}],"identity_rationale":"Kaynak ifadesi dişi atı temel referent olarak verir ve onu korunan, üreme için ayrılan, seçilmiş erkek dışında çiftleştirilmeyen ya da yavru taşıyan hayvan olarak açıklar; geçici dal çerçevesi bu ortak alanı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"korunan ya da damızlık olarak ayrılan kısrak"}],"lexicalization_note":"Dal yalın sözcükteki dişi at anlamını tanımlar; koruma, damızlık için ayırma ve yavru taşıma açıklamaları aynı referentin sınırları içinde tutulur.","neighbor_coverage_note":"Tüm adaylar incelendi; üreyen dişi hayvan, korunan seçkin hayvan ve yavru-soy alanlarıyla kurulan üç açıklayıcı karşılaştırma yayımlandı, yalnızca erkek hayvan ya da çiftleşme olayı odaklı adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal tür bakımından dişi atla sınırlıdır ve seçici çiftleştirmeyi vurgular; komşu dal üreme değeri taşıyan dişi hayvanları daha geniş bir tür alanında toplar.","focus_only":"Yalnızca at türündeki dişiyi ve seçilmiş erkekle çiftleştirme kısıtını kapsar.","gloss":"yavru vermesi beklenen dişi hayvan","neighbor_only":"At dışındaki mal ve çiftlik hayvanlarının yavru vermesi beklenen dişilerini de kapsar.","neighbor_ref":"root_000233/B006","relation_type":"near_synonym","shared_zone":"İki dal da yavru üretmesi beklenen ve bu amaçla değer verilen dişi hayvanı anlatır."},{"boundary_match":"partial","distinction":"Odak dal dişi atı damızlık olarak korur; komşu dal ise seçkin deveyi güvenilir yedek olarak saklar ve aynı çiftleştirme sınırını taşımaz.","focus_only":"Korunan hayvan dişi attır ve üreme amacı ile eş seçimi açıkça belirleyicidir.","gloss":"özenle saklanan seçkin hayvan","neighbor_only":"Korunan hayvan devedir; seçim cinsiyetten çok yormadan saklama, güvenilir yedek ve sürü niteliğine dayanır.","neighbor_ref":"root_001235/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da değerli bir hayvanın yıpratılmadan korunup gelecekteki yarar için ayrılmasını anlatır."},{"boundary_match":"field_only","distinction":"Odak dal üremeye katılan korunan dişi hayvandır; komşu dal ise üremenin sonucu olan yavruyu ve kuşaklar boyunca çoğalan soyu anlatır.","focus_only":"Üreme için ayrılan ana hayvanı, yani dişi atı adlandırır.","gloss":"damızlık ana ile yavru-soy ayrımı","neighbor_only":"Doğan yavruyu, soyu ve canlıların birbirinden çoğalmasını adlandırır.","neighbor_ref":"root_001499/B001","relation_type":"same_field","shared_zone":"İki dal hayvan yetiştiriciliği, çiftleşme ve neslin sürdürülmesi alanını paylaşır."}],"source_phrase_ar":"والحجر الفرس الأنثى وهي تصان ويضن بها (maqayis)؛ أحجار الخيل ما اتخذ منها للنسل (ayn)؛ سميت الأنثى من الخيل حجرا لأنها حجرت عن الذكور إلا عن فحل كريم (jamhara)؛ والحجر أيضا الأنثى من الخيل (sihah)؛ الحجر الفرس الأنثى وما اتخذ منها للنسل (tahdhib)؛ يقال للأنثى من الفرس حجر لكونها مشتملة على ما في بطنها من الولد (mufradat)","source_summary":"Kaynaklar referentin dişi at olduğu konusunda birleşir; korunan ve üreme için ayrılan hayvan oluşu, seçilmiş erkek dışında çiftleştirilmemesi ve karnında yavru taşıması adlandırmayı açıklayan tamamlayıcı vurgulardır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحجر من الخيل وهي الأنثى المصونة أو المعدة للنسل","what_is_not_ar":"ليس حجر المرأة ولا الحجر الصلب ولا الحرام"},"support_links":[]},{"boundary":"Çekirdek fiziksel atmadır; karşılıklı atışma ile hedefe ya da ava çıkma, belirli biçim ve söz öbeklerine bağlı kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000603/B001","candidate_links":[{"candidate_id":"cand_0819d1aab4a78d02a5c7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"رَمَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:ramaY`|ROOT:rmy|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"105:4:1:1","qac_word_ref":"105:4:1","surface_ar":"تَرْمِي"}],"gloss":"elden atmak veya hedefe fırlatmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesne elden bırakılır ve uzağa ya da bir hedefe doğru hareket ettirilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Taş ve ok gibi somut nesneler atılabilir; ok atışı yayla ve hedef gözetilerek yapılabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli biçimler karşılıklı atışmayı, hedefe atış yapmaya çıkmayı veya av atışına çıkmayı anlatır."}}],"root_ar":"ر م ي","root_id":"root_000603","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel atma çekirdeğini ve hedefe yönelmeyi birlikte anlatan genel kavram karşılığıdır.","boundary_detail":"Çekirdek fiziksel atmadır; karşılıklı atışma ile hedefe ya da ava çıkma, belirli biçim ve söz öbeklerine bağlı kalır.","branch_image_ar":"إرسال الشيء ورميه","concept_gloss":"elden atmak veya hedefe fırlatmak","contextual_glosses":[{"applicability":"Nesnenin elden bırakıldığı taş, araç ve benzeri genel fiziksel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Elden çıkarma ve uzağa gönderme hareketini doğal biçimde korur."},"facet_ids":["F001"],"text":"atmak","usage_role":"general"},{"applicability":"Ok, talim hedefi veya av gibi yöneltilmiş atış bağlamları için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Atışın belirli bir hedefe yöneltilmesi ve amaçlı yapılmasını korur."},"facet_ids":["F002","F003"],"text":"hedefe atış yapmak","usage_role":"contextual"}],"definition":"Bir nesneyi elden çıkararak uzağa ya da belirli bir hedefe doğru göndermektir. Okla atış, karşılıklı atışma ve hedefe veya ava çıkma bu çekirdeğin biçime bağlı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesne elden bırakılır ve uzağa ya da bir hedefe doğru hareket ettirilir."},{"facet_id":"F002","role":"specialization","statement":"Taş ve ok gibi somut nesneler atılabilir; ok atışı yayla ve hedef gözetilerek yapılabilir."},{"facet_id":"F003","role":"associated_use","statement":"Belirli biçimler karşılıklı atışmayı, hedefe atış yapmaya çıkmayı veya av atışına çıkmayı anlatır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ok dışındaki nesneleri elden atma biçimlerini dışarıda bırakır.","preserves":"Hedefe yöneltilmiş ok atışı anlamını eksiksiz biçimde korur."},"text":"ok atmak"}],"identity_rationale":"Kaynak ifadesi, bir nesneyi elden bırakıp uzağa göndermeyi temel alıyor; ok, taş, hedef ve av örnekleri bu fiziksel atma çekirdeğinin özel gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi elden atmak veya okla fırlatmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yay kullanarak ok atmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"karşılıklı atışmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"hedefe atış yapmaya çıkmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"av atışına çıkmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bir şeyi elden atmak veya birini bineğinden düşürmek"}],"lexicalization_note":"Tanım fiziksel atma çekirdeğini verir, ancak yay kullanma, karşılıklı atışma ve av amacıyla çıkma anlamlarını kendi biçim ve söz öbekleriyle sınırlar.","neighbor_coverage_note":"Listelenen bütün komşular değerlendirildi; fiziksel atmanın genel sınırını ve yayın işlevini en açık gösteren iki karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel atma araçlarını ve uzağa fırlatılan nesneleri genişçe toplar; odak dal ise elden çıkarma çekirdeğini hedef, yay ve avla sınırlı özel kullanımlarla birlikte kurar.","focus_only":"Elden bırakma yanında hedefe ve ava çıkmaya bağlı özel kullanımları içerir.","gloss":"genel atma ve uzağa fırlatma","neighbor_only":"Atılan araç, atış aracı ve uzak fırlatma alanını daha geniş biçimde adlandırır.","neighbor_ref":"root_001209/B001","relation_type":"near_synonym","shared_zone":"İki dal da somut bir nesnenin kuvvetle uzağa gönderilmesini kapsar."},{"boundary_match":"field_only","distinction":"Odak dal atıcının yaptığı atma eylemini belirtir; komşu dal ise yayın oku hızlandıran mekanik etkisini belirtir, bu yüzden birbirinin yerine geçmez.","focus_only":"Nesnenin elden çıkarılıp uzağa veya hedefe gönderilmesi eylemidir.","gloss":"yayın oku hızlandırması","neighbor_only":"Yayın oku ileriye doğru hızlandıran itici etkisini anlatır.","neighbor_ref":"root_000593/B005","relation_type":"same_field","shared_zone":"Her iki dal ok atışı sahnesinde yer alır ve okun ileri hareketiyle ilgilidir."}],"source_phrase_ar":"أصل واحد وهو نبذ الشيء (maqayis)؛ رمى يرمي رميا فهو رام (ayn;tahdhib)؛ رميت الشيء من يدي أي ألقيته (sihah)؛ الرمي يقال في الأعيان كالسهم والحجر (mufradat)؛ خرجت أترمى إذا خرجت ترمى في الأغراض (maqayis;sihah)؛ خرجت أرتمي إذا رميت القنص (sihah)","source_summary":"Kaynakların ortak çizgisi, nesnenin elden çıkarılıp uzağa veya hedefe gönderilmesidir; taş ve ok örnekleri ile hedef ve av kullanımları bu çizgiyi somutlaştırır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"إرسال الشيء من اليد أو بالقوس أو الحصى والسهم والرمي في الغرض والقنص","what_is_not_ar":"ليس زيادة ولا قذفا بالقول ولا ظنا ولا سفرا"},"support_links":["sup_0cfb5995aa42493eee81"]},{"boundary":"Sayısal ya da miktarsal artış çekirdektir; faiz anlamı ayrı bir biçime bağlı uzmanlaşmış kullanımdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000603/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَمَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:ramaY`|ROOT:rmy|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"105:4:1:1","qac_word_ref":"105:4:1","surface_ar":"تَرْمِي"}],"gloss":"üzerine ekleyerek artırmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Mevcut sayı veya miktara ekleme yapılarak önceki sınır aşılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli bir ad artışın yanında faiz anlamını da taşır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sayının üzerine çıkma anlatımı, genel olarak bir şeyde fazlalık oluşturma kullanımına genişler."}}],"root_ar":"ر م ي","root_id":"root_000603","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sayısal ve miktarsal eşiği aşma çekirdeğini doğal Türkçe ile karşılar.","boundary_detail":"Sayısal ya da miktarsal artış çekirdektir; faiz anlamı ayrı bir biçime bağlı uzmanlaşmış kullanımdır.","branch_image_ar":"تجاوز بالزيادة","concept_gloss":"üzerine ekleyerek artırmak","contextual_glosses":[{"applicability":"Belirtilen bir sayı veya ölçünün eklemeyle aşıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli sayısal eşiğin ek bir miktarla aşılmasını açıkça korur."},"facet_ids":["F001"],"text":"sayının üstüne çıkmak","usage_role":"contextual"},{"applicability":"Yalnızca artış adının faiz anlamında kullanıldığı mali bağlam için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mali fazlalığın yerleşmiş özel adlandırmasını eksiksiz korur."},"facet_ids":["F002"],"text":"faizli artış","usage_role":"contextual"}],"definition":"Bir sayı, miktar veya şey üzerine ekleme yaparak önceki düzeyi aşmaktır. Faiz anlamı, bu artış kavramının belirli bir adda yerleşmiş özel kullanımıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Mevcut sayı veya miktara ekleme yapılarak önceki sınır aşılır."},{"facet_id":"F002","role":"specialization","statement":"Belirli bir ad artışın yanında faiz anlamını da taşır."},{"facet_id":"F003","role":"extension","statement":"Sayının üzerine çıkma anlatımı, genel olarak bir şeyde fazlalık oluşturma kullanımına genişler."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sayı ve miktarlardaki genel artış çekirdeğini bütünüyle dışarıda bırakır.","preserves":"Mali fazlalıkla ilgili uzmanlaşmış kullanımı doğru biçimde korur."},"text":"faiz"}],"identity_rationale":"Kaynak ifadesi bir sayı veya miktarın üstüne çıkmayı ortak çekirdek olarak veriyor ve faiz anlamını bu artış fikrinin yerleşmiş özel kullanımı olarak kaydediyor.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir sayı veya miktarın üstüne çıkacak kadar artırmak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"artış; faiz"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"artırmak veya faizli fazlalık oluşturmak"}],"lexicalization_note":"Tanım artış çekirdeğini korur; bir sayının üstüne çıkma söz öbeği ile faiz anlamını bütün biçimlere yaymaz.","neighbor_coverage_note":"Bütün komşu adaylar değerlendirildi; genel artışla ve yükselerek büyümeyle olan iki yakın sınır, faiz ve eşik özelliklerini göstermek için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal sayı, bağış ve sözdeki genel fazlalığı kapsar; odak dal ise özellikle bir sayının üzerine çıkmayı ve artışın faiz olarak adlandırılmasını birlikte sınırlar.","focus_only":"Bir eşiğin üstüne çıkma kalıbını ve faiz anlamındaki özel adı içerir.","gloss":"ölçüyü aşan artış","neighbor_only":"Artışı sayı yanında bağış ve söz miktarı gibi daha çeşitli alanlara yayar.","neighbor_ref":"root_000558/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da önceki miktara göre fazlalık oluşmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal eklemeyle miktarı aşmaya dayanır; komşu dal ise artışa fiziksel yükselme ve kabarma yönlerini de katar.","focus_only":"Sayısal sınırı aşma ve faiz anlamını belirli kullanımlarda birleştirir.","gloss":"artma ve yükselme","neighbor_only":"Artışla birlikte yükselme, kabarma ve fiziksel büyüme anlamlarını da kapsar.","neighbor_ref":"root_000537/B001","relation_type":"near_synonym","shared_zone":"İki dalda da bir önceki düzeye göre artış veya fazlalık bulunur."}],"source_phrase_ar":"أرميت على المائة زدت عليها (maqayis)؛ أرمى فلان في هذا الشيء أي زاد فيه (ayn)؛ رميت على الخمسين وأرميت أيضا أي زدت (sihah)؛ الرماء الربا (ayn;sihah)؛ أرمى فلان على مائة استعارة للزيادة (mufradat)","source_summary":"Kaynaklar sayı veya miktarın üzerine çıkma ve bir şeyde fazlalık oluşturma noktasında birleşir; ayrıca artış adı faiz için özel bir kullanım kazanır.","sources":["MQ","AY","SI","MU"],"what_is_ar":"الزيادة على العدد أو الشيء والربا بوصفه زيادة","what_is_not_ar":"ليس رمي جسم ولا قذفا بالقول ولا سفرا"},"support_links":[]},{"boundary":"Bu dal ortak bir nesne sınıfı değil, atışla tanımlanan araç, ok ve av adlarının sınırlı bir kümesidir.","branch_kind":"bare","branch_ref":"root_000603/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَمَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:ramaY`|ROOT:rmy|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"105:4:1:1","qac_word_ref":"105:4:1","surface_ar":"تَرْمِي"}],"gloss":"atış aracı veya vurulan av","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Adlandırılan şeyin belirleyici bağı atış eylemi, atış aracı veya atışın sonucudur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir ad yuvarlak ok ucunu veya atış öğrenmekte kullanılan oku belirtir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başka bir ad, atışla vurulup yere serilen avı belirtir."}}],"root_ar":"ر م ي","root_id":"root_000603","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın araç ve sonuç olarak ayrılan iki ad grubunu tek üst ifadede gösterir.","boundary_detail":"Bu dal ortak bir nesne sınıfı değil, atışla tanımlanan araç, ok ve av adlarının sınırlı bir kümesidir.","branch_image_ar":"ما يتصل بالرمي من آلة أو صيد","concept_gloss":"atış aracı veya vurulan av","contextual_glosses":[{"applicability":"Araç adının iki kaynak açıklamasını birlikte vermek gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hem yuvarlak ok ucu hem de eğitimde kullanılan ok açıklamasını korur."},"facet_ids":["F002"],"text":"yuvarlak ok ucu veya talim oku","usage_role":"explanatory"},{"applicability":"Atışın hedefi olup vurularak yere serilen av hayvanı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Avın atışla hedef alınması ve vurulması sonucunu birlikte korur."},"facet_ids":["F003"],"text":"atılarak vurulan av","usage_role":"contextual"}],"definition":"Atışla ilişkisi üzerinden adlandırılan belirli şeyleri kapsar: yuvarlak bir ok ucu, atış taliminde kullanılan ok ve atılarak yere serilen av. Bunlar tek bir nesne türü değil, aynı eylem alanındaki ayrı adlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Adlandırılan şeyin belirleyici bağı atış eylemi, atış aracı veya atışın sonucudur."},{"facet_id":"F002","role":"source_variant","statement":"Bir ad yuvarlak ok ucunu veya atış öğrenmekte kullanılan oku belirtir."},{"facet_id":"F003","role":"source_variant","statement":"Başka bir ad, atışla vurulup yere serilen avı belirtir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Talim oku açıklamasını ve atışla vurulan av adını dışarıda bırakır.","preserves":"Okun uç parçasına ilişkin araç açıklamasını doğru biçimde korur."},"text":"ok ucu"}],"identity_rationale":"Kaynak ifadesi tek bir nesne türü vermiyor; yuvarlak ok ucu veya talim oku ile atılarak yere serilen avı, atış eylemiyle ilişkili ayrı adlandırmalar olarak bir araya getiriyor.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yuvarlak ok ucu veya atış taliminde kullanılan ok"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"atılarak vurulup yere serilen av"}],"lexicalization_note":"Tanım yalnızca kaynakta verilen atış bağlantılı adları kapsar; bunlardan genel bir atma eylemi veya bütün av araçları anlamı çıkarmaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; ok türleriyle ve av sağlayan araçlarla sınırı gösteren iki alan karşılaştırması, dalın çift yapısını en iyi açıklıyor.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal iki farklı araç açıklamasını vurulan av adıyla birlikte taşır; komşu dal ise küçük, hedeflik veya demir uçsuz ok türlerini belirtir.","focus_only":"Yuvarlak ok ucu veya talim oku yanında vurulan av adını da içerir.","gloss":"küçük ve özel yapılı oklar","neighbor_only":"Küçük okları, hedef oklarını ve demir ucu bulunmayan okları sınıflandırır.","neighbor_ref":"root_001199/B006","relation_type":"same_field","shared_zone":"İki dal da ok ve atış araçlarının adlandırıldığı aynı teknik alanda yer alır."},{"boundary_match":"field_only","distinction":"Odak dal belirli bir ok parçasını veya oku ve vurulmuş avı adlandırır; komşu dal ise sahibine av kazandıran aracı işlevi üzerinden tanımlar.","focus_only":"Atış aracını ve atışla yere serilen avı adlandırır.","gloss":"av sağlayan araç","neighbor_only":"Sahibine av sağlayan yay, yırtıcı hayvan veya parmak gibi av aracını belirtir.","neighbor_ref":"root_000934/B006","relation_type":"same_field","shared_zone":"Her iki dal avlanma sahnesinde araç ile elde edilen av arasındaki ilişkiye dokunur."}],"source_phrase_ar":"المرماة نصل السهم المدور (maqayis;sihah)؛ المرماة السهم الذي يتعلم به الرمي (ayn)؛ الرمية الصيد الذي يرمى (maqayis;ayn;sihah)","source_summary":"Kaynaklar atış alanında iki ayrı adlandırmayı aktarır: ok ucu veya talim oku olarak açıklanan araç ve atışla vurulan av. Araç açıklamasındaki iki değer birlikte korunmalıdır.","sources":["MQ","AY","SI"],"what_is_ar":"اسم لما يتصل بالرمي من سهم أو نصل أو صيد مصروع بالرمي","what_is_not_ar":"ليس نفس فعل الرمي ولا الزيادة ولا القذف بالقول؛ وتأويل الظلف موضع إشكال"},"support_links":[]},{"boundary":"Büyük ve yoğun yağışlı bulut ile ince küçük bulut parçaları, aynı ad alanındaki karşıt kaynak görünümleri olarak korunur.","branch_kind":"bare","branch_ref":"root_000603/B004","candidate_links":[{"candidate_id":"cand_76be9c458609695a8d5d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"رَمَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:ramaY`|ROOT:rmy|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"105:4:1:1","qac_word_ref":"105:4:1","surface_ar":"تَرْمِي"}],"gloss":"bol ve şiddetli yağış taşıyan büyük bulut veya ince bulut parçaları","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Adlandırma bulut veya yağmur görünümüne ilişkindir ve meteorolojik bir varlığı belirtir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kaynak çizgisi bol ve şiddetli yağış taşıyan büyük bulutu öne çıkarır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Diğer kaynak çizgisi ince ve küçük bulut parçalarını öne çıkarır."}}],"root_ar":"ر م ي","root_id":"root_000603","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynaklardaki iki farklı meteorolojik görünümü eksiltmeden birlikte verir.","boundary_detail":"Büyük ve yoğun yağışlı bulut ile ince küçük bulut parçaları, aynı ad alanındaki karşıt kaynak görünümleri olarak korunur.","branch_image_ar":"سحاب يرمى بقطع أو قطر","concept_gloss":"bol ve şiddetli yağış taşıyan büyük bulut veya ince bulut parçaları","contextual_glosses":[{"applicability":"Büyük, bol ve şiddetli yağış taşıyan bulut açıklaması için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bulutun büyüklüğünü, yağış bolluğunu ve şiddetli etkisini korur."},"facet_ids":["F002"],"text":"bol ve şiddetli yağış taşıyan büyük bulut","usage_role":"contextual"},{"applicability":"Parçalı, küçük ve ince bulut görünümünü aktaran açıklama için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bulutun küçük parçalara ayrılmış ve ince görünümünü eksiksiz korur."},"facet_ids":["F003"],"text":"ince küçük bulut parçaları","usage_role":"contextual"}],"definition":"Yağışla ilişkili bir bulut adıdır; bir açıklamada bol ve şiddetli yağış taşıyan büyük bulutu, başka bir açıklamada ise ince küçük bulut parçalarını belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Adlandırma bulut veya yağmur görünümüne ilişkindir ve meteorolojik bir varlığı belirtir."},{"facet_id":"F002","role":"source_variant","statement":"Bir kaynak çizgisi bol ve şiddetli yağış taşıyan büyük bulutu öne çıkarır."},{"facet_id":"F003","role":"source_variant","statement":"Diğer kaynak çizgisi ince ve küçük bulut parçalarını öne çıkarır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnce küçük bulut parçaları açıklamasını ve iri damla ayrıntısını siler.","preserves":"Bulutun yağışla ilişkili meteorolojik niteliğini doğru biçimde korur."},"text":"yağmur bulutu"}],"identity_rationale":"Kaynak ifadesi hem bol ve şiddetli yağış taşıyan büyük bulutu hem de ince, küçük bulut parçalarını veriyor; dalın meteorolojik çerçevesi doğru olsa da tek boyutlu bir bulut tasviri yeterli değildir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bol ve şiddetli yağış taşıyan büyük bulut veya ince küçük bulut parçaları"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yağmur bulutları veya bulut parçaları"}],"lexicalization_note":"Tanım kaynakta verilen bulut ve yağmur adlarını doğrudan kapsar; fiziksel atma eylemini bu dala taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; iri damlalı bulutla yakın örtüşme ve genel bulut alanıyla kapsam farkı, iki kaynak görünümünü en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal bol ve şiddetli yağış taşıyan büyük bulut görünümüyle sınırlıdır; odak dal aynı görünümün yanında ince küçük bulut parçaları açıklamasını da korur.","focus_only":"Bol ve şiddetli yağış taşıyan büyük bulut yanında ince küçük bulut parçalarını da kapsar.","gloss":"bol ve şiddetli yağış taşıyan büyük bulut","neighbor_only":"Yalnızca bol ve şiddetli yağış taşıyan büyük bulut görünümüne odaklanır.","neighbor_ref":"root_000615/B014","relation_type":"near_synonym","shared_zone":"İki dal da bol ve şiddetli yağış taşıyan büyük bulutu kapsar."},{"boundary_match":"partial","distinction":"Odak dal belirli yağış yoğunluğu ve parçalılık görünümlerini taşır; komşu dal ise bulut ve yağış alanını bu niteliklerle sınırlamadan daha genel kapsar.","focus_only":"Bulutu yağış bolluğu, yağış etkisi veya ince parçalılık üzerinden sınırlar.","gloss":"genel bulut ve yağış","neighbor_only":"Bulut, bir bulut parçası, yağmur ve dolu için daha genel bir ad alanı sunar.","neighbor_ref":"root_001419/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal bulut parçalarını ve bunlarla bağlantılı yağış türlerini adlandırır."}],"source_phrase_ar":"الرمي السحابة العظيمة القطر (maqayis)؛ الرمي قطع صغار من السحاب رقاق (ayn)؛ الرمى السقى وهي السحابة العظيمة القطر الشديدة الوقع (sihah)؛ ترمى بقطع من السحاب (maqayis)","source_summary":"Kaynaklar adın bulut ve yağmur alanına ait olduğunda birleşir, fakat görünüm konusunda iki yön aktarır: bol ve şiddetli yağış taşıyan büyük bulut ve ince küçük bulut parçaları.","sources":["MQ","AY","SI"],"what_is_ar":"السحاب أو المطر الذي يجيء كقطع مرمية أو كسحابة كثيرة القطر","what_is_not_ar":"ليس رمي السهم ولا الربا"},"support_links":["sup_e12af88c6d6fb2856c10"]},{"boundary":"Anlam yalnızca ilahi yardım ve işi gözetme dileğine veya bildirimine bağlıdır; genel yardım fiiline yayılmaz.","branch_kind":"non_bare","branch_ref":"root_000603/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَمَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:ramaY`|ROOT:rmy|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"105:4:1:1","qac_word_ref":"105:4:1","surface_ar":"تَرْمِي"}],"gloss":"Tanrısal yardım ve gözetme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi için Tanrı'nın yardım ve destek sağlaması dile getirilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yardım, kişinin işinin gözetilmesi ve uygun biçimde yoluna konması yönünü de taşır."}}],"root_ar":"ر م ي","root_id":"root_000603","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Verilen özel sözde yardım ile işi yoluna koyma yönlerini birlikte karşılar.","boundary_detail":"Anlam yalnızca ilahi yardım ve işi gözetme dileğine veya bildirimine bağlıdır; genel yardım fiiline yayılmaz.","branch_image_ar":"نصر يصنع للمرء","concept_gloss":"Tanrısal yardım ve gözetme","contextual_glosses":[{"applicability":"Bir kişi için yardım ve işlerinin düzelmesi dileğinde bulunulan bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yardım dileğini ve kişinin işinin yoluna konması isteğini birlikte korur."},"facet_ids":["F001","F002"],"text":"Tanrı sana yardım etsin ve işini yoluna koysun","usage_role":"contextual"}],"definition":"Tanrı'nın bir kişiye yardım etmesini ve onun işini gözetip yoluna koymasını dilemek veya bildirmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi için Tanrı'nın yardım ve destek sağlaması dile getirilir."},{"facet_id":"F002","role":"specialization","statement":"Yardım, kişinin işinin gözetilmesi ve uygun biçimde yoluna konması yönünü de taşır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yardımın Tanrı'dan gelmesini ve işin gözetilip yoluna konmasını siler.","preserves":"Bir kişiye destek sağlama yönünü genel düzeyde doğru biçimde korur."},"text":"yardım etmek"}],"identity_rationale":"Kaynak ifadesi, Tanrı'nın bir kişiye yardım etmesini ve onun işini gözetip yoluna koymasını dile getiren sınırlı bir sözün anlamını açıkça veriyor.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"Tanrı'nın sana yardım etmesi ve işini yoluna koyması"}],"lexicalization_note":"Tanım yalnızca verilen kalıpla sınırlıdır ve bu kalıbın ilahi yardım ile işi yoluna koyma anlamını çıplak köke genellemez.","neighbor_coverage_note":"Listelenen bütün adaylar değerlendirildi; hiçbiri ilahi yardım ile kişinin işini yoluna koyma birleşimini doğrudan paylaşmadığı için yayımlanacak bir karşılaştırma seçilmedi.","source_phrase_ar":"أرمى الله لك أي نصرك وصنع لك (maqayis;sihah)","source_summary":"Kaynakların ortak açıklaması, bir kişi için Tanrı'nın yardımını ve onun işini gözetip yoluna koymasını dile getiren özel bir sözdür.","sources":["MQ","SI"],"what_is_ar":"الدعاء أو الخبر بأن الله نصر واصطنع للمرء","what_is_not_ar":"ليس إلقاء حسيا ولا زيادة عددية"},"support_links":[]},{"boundary":"Ulaşma sonucu tek başına yeterli değildir; süreç, iki uç arasındaki hareket ve yaraya bağlı kötüleşme kullanımı korunmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000603/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَمَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:ramaY`|ROOT:rmy|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"105:4:1:1","qac_word_ref":"105:4:1","surface_ar":"تَرْمِي"}],"gloss":"iki sınır arasında ilerleyip sonuca varmak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey iki sınır arasında ilerler, uzanır veya gidip gelir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Süreç, ulaşılan bir yer veya varılan bir son durumla tamamlanabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yara için kullanılan söz öbeği, durumun ilerleyip bozulmaya varmasını anlatır."}}],"root_ar":"ر م ي","root_id":"root_000603","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hareket veya gelişme sürecini ve ulaşılan yer ya da durumu birlikte kapsar.","boundary_detail":"Ulaşma sonucu tek başına yeterli değildir; süreç, iki uç arasındaki hareket ve yaraya bağlı kötüleşme kullanımı korunmalıdır.","branch_image_ar":"ترام إلى غاية","concept_gloss":"iki sınır arasında ilerleyip sonuca varmak","contextual_glosses":[{"applicability":"Bir şeyin hareket veya yayılma yoluyla belirli bir yere ulaştığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Süreç boyunca ilerlemeyi ve ulaşılan yer sınırını birlikte korur."},"facet_ids":["F001","F002"],"text":"bir noktaya kadar uzanmak","usage_role":"general"},{"applicability":"Yaranın durumunun giderek kötüleşip bozulma aşamasına vardığı bağlam içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaranın aşamalı gelişmesini ve bozulma sonucuna varmasını korur."},"facet_ids":["F003"],"text":"yara bozulmaya doğru ilerlemek","usage_role":"contextual"}],"definition":"Bir şeyin iki sınır arasında ilerlemesi, uzanması veya gidip gelerek belirli bir yere ya da sonuca varmasıdır. Yaranın bozulmaya doğru gelişmesi bu sürecin belirli bir söz öbeğine bağlı uygulamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey iki sınır arasında ilerler, uzanır veya gidip gelir."},{"facet_id":"F002","role":"extension","statement":"Süreç, ulaşılan bir yer veya varılan bir son durumla tamamlanabilir."},{"facet_id":"F003","role":"specialization","statement":"Yara için kullanılan söz öbeği, durumun ilerleyip bozulmaya varmasını anlatır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İki sınır arasındaki hareketi ve yaranın aşamalı kötüleşmesini siler.","preserves":"Bir yere veya son duruma varma sonucunu açık biçimde korur."},"text":"ulaşmak"}],"identity_rationale":"Kaynak ifadesi yalnızca son noktaya ulaşmayı değil, iki sınır arasında ilerleme veya gidip gelme sürecini ve yaranın bozulmaya doğru gelişmesini de içeriyor.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"uzanıp belirli bir yere veya sonuca varmak"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yaranın durumu ilerleyerek bozulmaya varmak"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"iki şey arasında gidip gelmek"}],"lexicalization_note":"Tanım ilerleme ve sonuca varma çekirdeğini verir; yaranın bozulması ile iki şey arasında hareket etme anlamlarını kendi biçimlerine bağlı tutar.","neighbor_coverage_note":"Bütün komşular değerlendirildi; genel ulaşma ile son nokta kavramları, odak dalın süreç ve sonuç ayrımını en yararlı biçimde gösteriyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel varış ve tamamlanma sonucuna odaklanır; odak dal ise iki uç arasındaki ilerleme sürecini ve yaranın bozulmaya doğru gelişmesini ayrıca taşır.","focus_only":"İki sınır arasında süren hareketi ve yaranın bozulmaya ilerlemesini içerir.","gloss":"bir sona ulaşmak","neighbor_only":"Zamanın dolması, erginlik ve bir şeye erişme gibi daha genel varış türlerini kapsar.","neighbor_ref":"root_000151/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir hareketin veya sürecin belirli bir son sınıra varmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal sona götüren dinamik hareketi belirtir; komşu dal ise varılan son noktayı veya sınırı kavramlaştırır.","focus_only":"Bir şeyin ilerleyerek, uzanarak veya gidip gelerek sona varmasını anlatır.","gloss":"son nokta ve sınır","neighbor_only":"Sürecin kendisinden çok son noktayı, sınırı veya hedefe ulaşan haberi adlandırır.","neighbor_ref":"root_001560/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir hareketin ya da iletimin sonlandığı hedef veya sınırla ilişkilidir."}],"source_phrase_ar":"ترامى إلى الموضع الذي بلغه (maqayis)؛ الإرتماء أن يترامى الشيء بين الشيئين (ayn)؛ ترامى الجرح إلى الفساد (sihah)","source_summary":"Kaynaklar hareketin veya gelişmenin bir sınırdan ötekine ilerlemesini aktarır; ulaşılan yer, iki şey arasındaki hareket ve yaranın bozulmaya varması bu yapının ayrı görünümleridir.","sources":["MQ","AY","SI"],"what_is_ar":"بلوغ الشيء أو اندفاعه بين طرفين حتى ينتهي إلى موضع أو حال كالفساد","what_is_not_ar":"ليس زيادة مقصودة ولا رمي جسم باليد ولا سفرا"},"support_links":[]},{"boundary":"Anlam yolculuk ve yön niyeti bildiren sözlerle sınırlıdır; genel fiziksel atma veya her türlü yönelme anlamına gelmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000603/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَمَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:ramaY`|ROOT:rmy|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"105:4:1:1","qac_word_ref":"105:4:1","surface_ar":"تَرْمِي"}],"gloss":"yolculuk etmek veya bir yöne niyetlenmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi bulunduğu yerden ayrılarak bir yöne doğru yolculuk eder."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Soru kalıbı, kişinin hangi yöne veya yere gitmeyi düşündüğünü sorar."}}],"root_ar":"ر م ي","root_id":"root_000603","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Verilen söz kalıplarındaki fiili yolculuğu ve yön niyetini birlikte kapsar.","boundary_detail":"Anlam yolculuk ve yön niyeti bildiren sözlerle sınırlıdır; genel fiziksel atma veya her türlü yönelme anlamına gelmez.","branch_image_ar":"سفر إلى جهة","concept_gloss":"yolculuk etmek veya bir yöne niyetlenmek","contextual_glosses":[{"applicability":"Bir kişinin bulunduğu yerden ayrılıp yolculuk etmeye başladığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin ayrılıp bir yöne doğru yolculuğa başlamasını korur."},"facet_ids":["F001"],"text":"yola çıkmak","usage_role":"contextual"},{"applicability":"Bir kişinin amaçladığı yönü veya varış yerini soran kalıp için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Henüz gerçekleşmeyebilen yön ve yolculuk niyetini açıkça korur."},"facet_ids":["F002"],"text":"hangi yöne gitmeyi düşünmek","usage_role":"explanatory"}],"definition":"Belirli söz kalıplarında yolculuğa çıkmak veya gidilmesi düşünülen yönü ve varış yerini belirtmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi bulunduğu yerden ayrılarak bir yöne doğru yolculuk eder."},{"facet_id":"F002","role":"associated_use","statement":"Soru kalıbı, kişinin hangi yöne veya yere gitmeyi düşündüğünü sorar."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gidilecek yönü henüz niyet düzeyinde bildiren soru kullanımını siler.","preserves":"Bir yerden ayrılıp başka bir yere gitme eylemini doğru biçimde korur."},"text":"seyahat etmek"}],"identity_rationale":"Kaynak ifadesi belirli kullanımlarda yolculuk etmeyi ve hangi yöne gidilmek istendiğini sormayı açıkça birlikte veriyor; ortak sınır yönelinen yolculuk niyetidir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yolculuk etmek veya bir yöne gitmek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"hangi yöne gitmeyi düşünüyorsun"}],"lexicalization_note":"Tanım, yolculuk etme ve yön sorma anlamlarını yalnızca verilen kişi ve soru kalıplarında tutar; çıplak biçime genel bir seyahat anlamı yüklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yol alma ve daha geniş yer değiştirme dalları, odak kullanımdaki yön niyeti ile kalıp sınırını en açık biçimde gösteriyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal gerçekleşen yolculuk ve ilerlemeyi genel olarak belirtir; odak dal ise bu anlamı belirli kalıplarda verir ve ayrıca gidilecek yönün niyetini sorar.","focus_only":"Gerçek yolculuk yanında henüz düşünülen yönü soran özel kullanımı içerir.","gloss":"bir yere doğru yol almak","neighbor_only":"Yola çıkma, yol alma ve bir varış yerine ilerleme eylemlerini genel biçimde kapsar.","neighbor_ref":"root_000551/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bulunduğu yerden ayrılıp belirli bir yöne yolculuk etmeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal yolculuğu ve tasarlanan yönü sınırlı söz kalıplarında anlatır; komşu dal ise seyahat ve yer değiştirme türlerini daha geniş toplar.","focus_only":"Yön niyetini soran ve yolculuk anlamını belirli kalıba bağlayan kullanımı taşır.","gloss":"yer değiştirerek yolculuk etmek","neighbor_only":"Yer değiştirme, kısa yolculuk ve göç etme gibi daha geniş hareket türlerini kapsar.","neighbor_ref":"root_000964/B001","relation_type":"near_synonym","shared_zone":"İki dal da kişinin bir yerden ayrılıp başka bir yere doğru gitmesini kapsar."}],"source_phrase_ar":"رمى الرجل إذا سافر (tahdhib)؛ أين ترمي أي جهة تنوي (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu kullanım, yolculuk eylemi ile gidilmesi düşünülen yönü soran kalıbı birlikte aktarır."}],"source_summary":"Tek kaynak çizgisi, kişiyle kullanılan biçimi yolculuk etmek; soru biçimini ise gidilmesi düşünülen yönü veya yeri sormak olarak açıklar.","sources":["TA"],"what_is_ar":"السفر أو قصد جهة معينة","what_is_not_ar":"ليس رمي السهم ولا القذف ولا الظن"},"support_links":[]},{"boundary":"Çekirdek sözle yöneltilen suçlama veya hakarettir; nötr konuşma, yalnızca düşünme ve fiziksel atma bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000603/B008","candidate_links":[{"candidate_id":"cand_6b884ba12a183d8932d4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"رَمَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:ramaY`|ROOT:rmy|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"105:4:1:1","qac_word_ref":"105:4:1","surface_ar":"تَرْمِي"}],"gloss":"sözle suçlama veya hakaret","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi söz yoluyla suçlanır, kötülenir veya hakarete uğratılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Fiziksel atma hareketi, incitici veya suçlayıcı sözün bir hedefe yöneltilmesine aktarılır."}}],"root_ar":"ر م ي","root_id":"root_000603","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişiye yöneltilen suçlayıcı ve aşağılayıcı sözlerin ortak çekirdeğini karşılar.","boundary_detail":"Çekirdek sözle yöneltilen suçlama veya hakarettir; nötr konuşma, yalnızca düşünme ve fiziksel atma bu dala girmez.","branch_image_ar":"قذف بالكلام","concept_gloss":"sözle suçlama veya hakaret","contextual_glosses":[{"applicability":"Bir kişiye kötü bir fiil veya nitelik yükleyen suçlayıcı söz bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Suçlayıcı içeriğin sözle ve belirli bir kişiye yöneltilmesini korur."},"facet_ids":["F001"],"text":"sözle suçlamak","usage_role":"general"},{"applicability":"Suçlamadan çok aşağılayıcı ve incitici konuşmanın öne çıktığı bağlam içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözle incitme ve kişiyi kötüleme yönünü doğal biçimde korur."},"facet_ids":["F001"],"text":"sövmek","usage_role":"contextual"}],"definition":"Bir kişiye sözle suçlama, kötüleme veya hakaret yöneltmektir; fiziksel atma tasarımı burada incitici sözün hedefe yöneltilmesini anlatan bir aktarımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi söz yoluyla suçlanır, kötülenir veya hakarete uğratılır."},{"facet_id":"F002","role":"extension","statement":"Fiziksel atma hareketi, incitici veya suçlayıcı sözün bir hedefe yöneltilmesine aktarılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hakaret içermeden de gerçekleşebilen sözlü suçlama yönünü dışarıda bırakır.","preserves":"Kişiye yöneltilen aşağılayıcı ve incitici söz boyutunu korur."},"text":"hakaret etmek"}],"identity_rationale":"Kaynak ifadesi fiziksel atmanın söz alanına aktarılmasını açıkça, bir kişiyi sözle suçlama, kötüleme veya hakaret etme olarak sınırlandırıyor.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"birini sözle suçlamak veya ona hakaret etmek"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"atma anlatımını konuşmada suçlama ve hakaret için kullanmak"}],"lexicalization_note":"Tanım sözle suçlama ve hakaret anlamını verilen kişi ve konuşma kullanımlarında tutar; bunu genel konuşmaya veya çıplak fiziksel atmaya yaymaz.","neighbor_coverage_note":"Listelenen bütün adaylar değerlendirildi; en yakın iki sözlü saldırı dalı, odak anlamın hedef kişi, suçlama ve hakaret sınırlarını açıklamak için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal konuşmadaki suçlama ve hakareti atma aktarımıyla verir; komşu dal ise ayıp yükleme ve belirli ağır suçlamalar dahil daha ayrıntılı sözlü saldırı türlerini kapsar.","focus_only":"Fiziksel atma tasarımının konuşmaya aktarılmasını ve genel sözlü suçlamayı vurgular.","gloss":"sözle ayıplama ve suçlama","neighbor_only":"Ayıp yükleme, sövme ve belirli bir namus suçlaması gibi daha özel alanları da kapsar.","neighbor_ref":"root_001209/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir kişiye sözle suçlama, kötüleme veya hakaret yöneltir."},{"boundary_match":"partial","distinction":"Odak dal hedef kişiye suçlama veya hakaret yöneltmekle sınırlıdır; komşu dal karşılıklı sövüşme ve yerini bulmayan çok konuşma alanlarına da genişler.","focus_only":"Belirli bir kişiye yöneltilen suçlama veya hakareti çekirdek alır.","gloss":"kötü söz yöneltmek","neighbor_only":"Karşılıklı sövüşme ve hedefsizce çok konuşma gibi ek kullanımları içerir.","neighbor_ref":"root_000140/B005","relation_type":"near_synonym","shared_zone":"Her iki dal kötü, incitici veya iftira niteliğindeki sözün yöneltilmesini kapsar."}],"source_phrase_ar":"رمى فلان فلانا أي قذفه (tahdhib)؛ الرمي يقال في المقال كناية عن الشتم كالقذف (mufradat)","source_summary":"Kaynaklar bir kişiye sözle suçlama veya hakaret yöneltme anlamında birleşir ve fiziksel atma anlatımının konuşmaya aktarıldığını belirtir.","sources":["TA","MU"],"what_is_ar":"القذف بالكلام والشتم والاتهام","what_is_not_ar":"ليس رمي الأعيان ولا زيادة العدد ولا الظن المجرد"},"support_links":["sup_092334f1b90a87fb6510"]},{"boundary":"Anlam yalnızca hatalı olduğu belirtilen sanıdır; nötr tahmin, kesin bilgi ve sözlü suçlama bu dala girmez.","branch_kind":"bare","branch_ref":"root_000603/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَمَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:ramaY`|ROOT:rmy|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"105:4:1:1","qac_word_ref":"105:4:1","surface_ar":"تَرْمِي"}],"gloss":"yanlış bir kanıya varmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir durum hakkında sanıya dayalı bir yargı oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Oluşturulan sanı gerçeğe uymaz ve bu nedenle isabetsizdir."}}],"root_ar":"ر م ي","root_id":"root_000603","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sanıya dayalı yargıyı ve bu yargının isabetsiz oluşunu birlikte karşılar.","boundary_detail":"Anlam yalnızca hatalı olduğu belirtilen sanıdır; nötr tahmin, kesin bilgi ve sözlü suçlama bu dala girmez.","branch_image_ar":"ظن غير مصيب","concept_gloss":"yanlış bir kanıya varmak","contextual_glosses":[{"applicability":"Bir kişi veya durum hakkında oluşan sanının doğru çıkmadığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sanıya dayalı yargıyı ve yargının yanlış olmasını açıkça korur."},"facet_ids":["F001","F002"],"text":"yanlış sanmak","usage_role":"general"}],"definition":"Bir durum hakkında sanıya dayalı bir yargıya varmak ve bu yargının doğru çıkmamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir durum hakkında sanıya dayalı bir yargı oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Oluşturulan sanı gerçeğe uymaz ve bu nedenle isabetsizdir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Doğru veya nötr çıkabilecek sanıları da anlam alanına ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Bir durum hakkında kesin bilgi olmadan yargı oluşturma yönünü korur."},"text":"sanmak"}],"identity_rationale":"Kaynak ifadesi, bir kişinin doğrulanmamış bir yargıda bulunmasından daha dar olarak, özellikle doğru çıkmayan bir sanıya varmasını bildiriyor.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"isabetsiz bir sanıda bulunmak"}],"lexicalization_note":"Tanım çıplak dalı yanlış sanıda bulunma olarak verir ve konuşmaya bağlı suçlama anlamını bu dala taşımaz.","neighbor_coverage_note":"Bütün komşu adaylar değerlendirildi; geniş sanı alanı ve kesin bilgi karşı kutbu, yanlışlık koşulunu en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnızca yanlış çıkan sanıyı belirtir; komşu dal ise sanı yanında hayal, karışıklık ve benzerlikten doğan kuşku gibi çeşitli zihinsel durumları içerir.","focus_only":"Oluşan sanının yanlış ve isabetsiz olduğunu zorunlu olarak bildirir.","gloss":"sanı, hayal ve karışıklık","neighbor_only":"Hayal, karışıklık, kuşku ve benzerliğe dayalı suçlama gibi daha geniş durumları kapsar.","neighbor_ref":"root_000454/B005","relation_type":"near_synonym","shared_zone":"Her iki dal kesin bilgi yerine sanı veya zihinsel belirsizlikle yargı kurmayı kapsar."},{"boundary_match":"opposed","distinction":"Odak dal isabetsiz sanı kutbunda, komşu dal ise şüphenin kalktığı kesin bilgi kutbunda yer alır; ortak eksen yargının doğrulanma ve güven derecesidir.","focus_only":"Doğrulanmamış ve sonuçta yanlış çıkan bir sanıyı bildirir.","gloss":"yanlış sanı ile kesin bilgi","neighbor_only":"Şüphenin giderildiği, bilginin sağlam ve kesin olduğu durumu bildirir.","neighbor_ref":"root_001696/B001","relation_type":"polarity_pair","shared_zone":"İki dal bir yargının bilgi ve doğruluk bakımından taşıdığı güven düzeyini karşılaştırır."}],"source_phrase_ar":"رمى فلان يرمي إذا ظن ظنا غير مصيب (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu tekil açıklama, sanının yalnızca belirsiz değil, sonuçta yanlış olduğunu özellikle belirtir."}],"source_summary":"Tek kaynak çizgisi, bu kullanımı bir kişinin isabet etmeyen bir sanıda bulunması olarak sınırlar.","sources":["TA"],"what_is_ar":"إلقاء الظن غير المصيب أو الحكم بغير تحقق","what_is_not_ar":"ليس قذفا للمحصنات ولا رمي جسم"},"support_links":[]},{"boundary":"Dal, su taşıyan kovayı çekirdek alır; havuzu doldurma ve suyu dökme kullanımları bu çekirdeğe bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000677/B001","candidate_links":[{"candidate_id":"cand_0819d1aab4a78d02a5c7","lane":"micro"},{"candidate_id":"cand_76be9c458609695a8d5d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سِجِّيل","morph_features":"STEM|POS:N|LEM:sij~iyl|ROOT:sjl|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:4:4:1","qac_word_ref":"105:4:4","surface_ar":"سِجِّيلٍ"}],"gloss":"su bulunan kova ve ona bağlı doldurma-dökme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İçinde su bulunan kova anlatılır; bazı anlatımlarda kovanın iriliği veya suyla doluluğu özellikle öne çıkar."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kovaya bağlı olarak suyu doldurma, dökme ve dökülen suyun akması eylemleri anlatılır."}}],"root_ar":"س ج ل","root_id":"root_000677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kova çekirdeğiyle birlikte doldurma ve suyu döküp akıtma uzantılarının tümünü kapsayan dal düzeyi karşılıktır.","boundary_detail":"Dal, su taşıyan kovayı çekirdek alır; havuzu doldurma ve suyu dökme kullanımları bu çekirdeğe bağlıdır.","branch_image_ar":"الدلو الممتلئ وانصبابه","concept_gloss":"su bulunan kova ve ona bağlı doldurma-dökme","contextual_glosses":[{"applicability":"Kovanın kendisinin ve özellikle iriliğinin öne çıktığı ad kullanımlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Su içeren kova çekirdeğini ve iri kova niteliğini korur."},"facet_ids":["F001"],"text":"içinde su bulunan iri kova","usage_role":"contextual"},{"applicability":"Suyun kovadan dökülmesi ve ardından akması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dökme işlemini ve suyun bunun sonucunda akmasını birlikte korur."},"facet_ids":["F002"],"text":"suyu döküp akıtmak","usage_role":"contextual"},{"applicability":"Özel olarak havuzun suyla doldurulduğu kalıplaşmış kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Havuzun suyla doldurulması eylemini eksiksiz biçimde korur."},"facet_ids":["F002"],"text":"havuzu doldurmak","usage_role":"contextual"}],"definition":"Çekirdek anlam, içinde su bulunan ve kimi anlatımlarda iri ya da dolu olan kovadır. Bu çekirdekten, kovayı veya havuzu doldurma ile suyu döküp akıtma kullanımları gelişir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İçinde su bulunan kova anlatılır; bazı anlatımlarda kovanın iriliği veya suyla doluluğu özellikle öne çıkar."},{"facet_id":"F002","role":"extension","statement":"Kovaya bağlı olarak suyu doldurma, dökme ve dökülen suyun akması eylemleri anlatılır."}],"identity_rationale":"Kaynak ifadesi, çekirdekte içinde su bulunan kovayı ve buna bağlı doldurma ile dökme eylemlerini açıkça bir araya getirir. Ancak kovanın mutlaka ağzına kadar dolu ya da her zaman çok büyük olduğu söylenemez; bazı anlatımlar içindeki suyun az veya çok olabileceğini belirtir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"içinde su bulunan iri veya dolu kova"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"çok büyük kova"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"suyu döktü, su da akıp boşaldı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"havuzu doldurdu"}],"lexicalization_note":"Yalın ad biçimleri kova türünü, kalıplaşmış kullanımlar ise suyu dökme ve havuzu doldurma eylemlerini anlatır; bu katmanlar birbirine karıştırılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; kova doluluğu, genel dökme ve havuz doldurma adayları sınırı doğrudan aydınlattığı için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu, kabın doluluğunu ve büyüklüğünü çekirdek yapar. Odak ise su bulunan kovadan hareketle doldurma, dökme ve akma süreçlerine de uzanır.","focus_only":"Odak dal, kovayı taşıdığı su miktarından bağımsız olarak ele alabilir ve doldurma ile dökme eylemlerini de kapsar.","gloss":"dolu büyük kova","neighbor_only":"Komşu dal özellikle büyük, dolu veya doluya yakın kovayı anlatır ve doldurma-dökme eylemlerini kapsamaz.","neighbor_ref":"root_000521/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da içinde su bulunan, çoğu kez iri veya dolu bir kovayı adlandırır."},{"boundary_match":"partial","distinction":"Odak anlam kova merkezlidir ve kabın kendisini de adlandırır. Komşu anlam ise kap türünden bağımsız dökme, boşaltma ve akma olayını öne çıkarır.","focus_only":"Odak dalın somut çekirdeği su bulunan kovadır; ayrıca havuzu doldurma kullanımını içerir.","gloss":"sıvıyı dökme ve kabı boşaltma","neighbor_only":"Komşu dal, farklı kaplardaki içeriği boşaltmayı ve genel dökülme ya da akma olayını kapsar.","neighbor_ref":"root_001147/B002","relation_type":"near_neighbor","shared_zone":"İki dal, suyun bir kaptan dökülmesi ve akması olayında kesişir."},{"boundary_match":"partial","distinction":"Havuzu doldurma, odak dalın kova ve su dökme çekirdeğine bağlı tek bir kullanımken komşu dalın doğrudan merkezidir.","focus_only":"Odak dal su taşıyan kovayı ve suyu dökme eylemini de içerir.","gloss":"havuzu doldurma","neighbor_only":"Komşu dal yalnızca havuzu doldurma eylemi ile doldurulmuş havuz çevresinde kalır.","neighbor_ref":"root_000642/B008","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir havuzun suyla doldurulması anlatılabilir."}],"source_phrase_ar":"أصل واحد يدل على انصباب شيء بعد امتلائه (maqayis)؛ السجل وهو الدلو العظيمة (maqayis;mufradat)؛ السجل ملاك الدلو وأعطيته سجلا وسجلين وأسجلته (ayn)؛ السجل الدلو ولا يكون سجلا حتى يكون فيه ماء (jamhara)؛ السجل الدلو إذا كان فيه ماء قل أو كثر (sihah)؛ سجلت الماء فانسجل أي صببته فانصب (sihah;mufradat)؛ أسجلت الحوض ملأته (sihah)؛ السجل الدلو ملآن ماء (tahdhib)","source_summary":"Kaynakların ortak çizgisi, içinde su bulunan kovayı merkeze alır ve doldurma ile döküp akıtma eylemlerini bu somut araçtan türetir. Kovanın büyüklüğü ve doluluk derecesi anlatımlar arasında değişir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"السجل والدلو العظيمة إذا كان فيها ماء وملء الدلو أو الحوض وصب الماء وانصبابه وإعطاء سجل أو سجلين","what_is_not_ar":"ليس الكتاب ولا حجارة السجيل ولا المرآة"},"support_links":["sup_0cfb5995aa42493eee81","sup_e12af88c6d6fb2856c10"]},{"boundary":"Dal, tek taraflı yenmeyi değil, iki tarafın aynı alanda karşılık vererek yarışmasını ve kimi bağlamlarda üstünlüğün el değiştirmesini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000677/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سِجِّيل","morph_features":"STEM|POS:N|LEM:sij~iyl|ROOT:sjl|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:4:4:1","qac_word_ref":"105:4:4","surface_ar":"سِجِّيلٍ"}],"gloss":"karşılıklı boy ölçüşme ve üstünlük yarışı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki taraf aynı tür edimi karşılıklı sürdürür ve her biri ötekini geçmeye ya da onunla boy ölçüşmeye çalışır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karşılıklı yarışmanın örnek düzeni, iki tarafın sırayla kovayla su çekmesidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Savaşta üstünlük ve başarı iki taraf arasında sırayla el değiştirir."}}],"root_ar":"س ج ل","root_id":"root_000677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Övünme, yarışma, birbirinin yaptığını yapma ve üstünlüğün dönüşümlü el değiştirmesi çekirdeğini birlikte temsil eder.","boundary_detail":"Dal, tek taraflı yenmeyi değil, iki tarafın aynı alanda karşılık vererek yarışmasını ve kimi bağlamlarda üstünlüğün el değiştirmesini anlatır.","branch_image_ar":"المساجلة بين دلوي المتغالبين","concept_gloss":"karşılıklı boy ölçüşme ve üstünlük yarışı","contextual_glosses":[{"applicability":"İki tarafın aynı işi karşılıklı yaparak birbirini geçmeye çalıştığı genel bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki taraflı yarışmayı ve üstün gelme çabasını birlikte korur."},"facet_ids":["F001"],"text":"birbiriyle boy ölçüşmek","usage_role":"general"},{"applicability":"Savaşın kimi zaman bir tarafın, kimi zaman öteki tarafın lehine döndüğü kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Savaş başarısının taraflar arasında dönüşümlü olmasını korur."},"facet_ids":["F003"],"text":"savaşta üstünlüğün el değiştirmesi","usage_role":"contextual"}],"definition":"İki tarafın aynı tür işi karşılıklı yaparak boy ölçüşmesi, övünmesi veya birbirine üstün gelmeye çalışmasıdır. Savaş bağlamında bu düzen, üstünlüğün bir kez bir tarafa, bir kez ötekine geçmesiyle gerçekleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki taraf aynı tür edimi karşılıklı sürdürür ve her biri ötekini geçmeye ya da onunla boy ölçüşmeye çalışır."},{"facet_id":"F002","role":"associated_use","statement":"Karşılıklı yarışmanın örnek düzeni, iki tarafın sırayla kovayla su çekmesidir."},{"facet_id":"F003","role":"extension","statement":"Savaşta üstünlük ve başarı iki taraf arasında sırayla el değiştirir."}],"identity_rationale":"Kaynak ifadesi, sırayla su çekme yarışından doğan karşılıklı boy ölçüşme, övünme ve üstün gelme çabasını tutarlı biçimde verir. Savaşta üstünlüğün iki taraf arasında sırayla el değiştirmesi de bu karşılıklılık düzeninin belirgin bir uzantısıdır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"karşılıklı yarışma, övünme ve üstünlük çekişmesi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"savaşta üstünlüğün iki taraf arasında el değiştirmesi"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"iki kişi övünme ve üstün gelme yarışına girdi"}],"lexicalization_note":"Yalın eylem adı karşılıklı yarışma alanını kurar; savaşın dönüşümlü gidişi ve iki kişinin boy ölçüşmesi yalnız kendi kalıpları içinde korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; denk karşılık verme, uzayan karşılıklı çekişme ve tek taraflı üstün gelme en yararlı üç sınırı oluşturdu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu anlamın ölçütü denk kalmaktır; odak anlamda ise yarış, övünme ve rakibe üstün gelme daha belirgindir, ayrıca savaşın dönüşümlü gidişi de kapsanır.","focus_only":"Odak dal övünme, üstün gelme isteği ve savaşta üstünlüğün dönüşümlü el değiştirmesini kapsar.","gloss":"eşit düzeyde karşılık verme","neighbor_only":"Komşu dal, karşıdakinin yaptığını eşit düzeyde yapmayı ve ondan aşağı kalmamayı öne çıkarır.","neighbor_ref":"root_001648/B006","relation_type":"near_synonym","shared_zone":"Her iki dalda iki taraf aynı tür edimi karşılıklı yaparak birbirine denk olmaya çalışır."},{"boundary_match":"partial","distinction":"Odak dalın merkezi karşılıklı boy ölçüşme ve üstünlük yarışıdır. Komşu dalda süreci uzatma ve belirli tartışma ya da şiir bağlamları ayrıca belirleyicidir.","focus_only":"Odak dal sırayla su çekme örüntüsünü ve savaşta değişen üstünlüğü içerir.","gloss":"uzayan karşılıklı çekişme","neighbor_only":"Komşu dal çekişmeyi uzatma, tartışmada karşılık verme ve iki ozanın birbirine benzer edimde bulunması gibi özel alanlara uzanır.","neighbor_ref":"root_001396/B007","relation_type":"near_synonym","shared_zone":"İki dal da tarafların aynı alanda birbirine karşılık vererek yarışmasını anlatır."},{"boundary_match":"partial","distinction":"Komşu anlam tek taraflı zafer sonucunu adlandırır. Odak anlam ise sonucun yanı sıra karşılıklı yarışma düzenini ve dönüşümlü üstünlüğü korur.","focus_only":"Odak dal yarışın karşılıklı sürmesini ve kimi zaman üstünlüğün taraflar arasında el değiştirmesini gerektirir.","gloss":"rakibi yenip üstün çıkma","neighbor_only":"Komşu dal, rakibi sonunda yenip üstün çıkma sonucuna odaklanır.","neighbor_ref":"root_001281/B011","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir rakibe karşı üstünlük kurma amacı bulunur."}],"source_phrase_ar":"المساجلة المفاخرة والأصل في الدلاء (maqayis)؛ الحرب سجال أي مرة منها سجل على هؤلاء ومرة على هؤلاء (ayn)؛ المساجلة المغالبة أيهما يغلب صاحبه (ayn)؛ تساجل الرجلان إذا تفاخرا وأصله من تساجلهما في الاستقاء (jamhara)؛ المساجلة المفاخرة بأن تصنع مثله صنعه في جري أو سقي (sihah)؛ الحرب بيننا سجال (tahdhib)؛ المساجلة المساقاة بالسجل وجعلت عبارة عن المباراة والمناضلة (mufradat)","source_summary":"Kaynaklar karşılıklı yarışma, övünme ve üstünlük arayışını sırayla su çekme örneğine bağlar. Aynı karşılıklılık, savaşın bir tarafın ardından öteki taraf lehine dönmesi için de kullanılır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"المساجلة والمغالبة والمفاخرة والمباراة والمناضلة والحرب التي تكون سجالا مرة لهؤلاء ومرة لهؤلاء","what_is_not_ar":"ليس مجرد صب الماء ولا الكتاب ولا العطاء المباح"},"support_links":[]},{"boundary":"Dalın çekirdeği yalnız cömertlik değil, sunulan şeyin kimseye kapatılmaması ve koşula bağlanmamasıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000677/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سِجِّيل","morph_features":"STEM|POS:N|LEM:sij~iyl|ROOT:sjl|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:4:4:1","qac_word_ref":"105:4:4","surface_ar":"سِجِّيلٍ"}],"gloss":"herkese serbestçe sunma ve engellemeden salıverme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey herkese sunulur; isteyen onu alabilir veya ondan yararlanabilir ve hiç kimse engellenmez."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin iyiliği ve verdiği şeyler çoktur; verme eylemi bol ve geniştir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Söz herhangi bir engel veya kısıt konmadan serbestçe söylenir ya da aktarılır."}}],"root_ar":"س ج ل","root_id":"root_000677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Herkesin yararlanmasına açık sunumu, bol vermeyi ve sözün kısıtsız bırakılmasını birlikte temsil eder.","boundary_detail":"Dalın çekirdeği yalnız cömertlik değil, sunulan şeyin kimseye kapatılmaması ve koşula bağlanmamasıdır.","branch_image_ar":"البذل المرسل من فيض العطاء","concept_gloss":"herkese serbestçe sunma ve engellemeden salıverme","contextual_glosses":[{"applicability":"Bir şeyin ayırım yapılmadan herkesçe alınabildiği veya kullanılabildiği bağlamlar içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sunulan şeyin genel erişime açık ve kimseye yasak olmamasını korur."},"facet_ids":["F001"],"text":"herkesin yararlanmasına açık","usage_role":"general"},{"applicability":"Bir kişinin iyiliğinin ve verdiği şeylerin çokluğu anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin bol iyilik yapmasını ve çok vermesini korur."},"facet_ids":["F002"],"text":"eli açık ve bol veren","usage_role":"contextual"},{"applicability":"Sözün herhangi bir engel veya koşul konmadan söylenmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Söz üzerindeki engelin kaldırılmasını ve sözün salıverilmesini korur."},"facet_ids":["F003"],"text":"sözü serbest bırakmak","usage_role":"contextual"}],"definition":"Çekirdek, bir şeyi ayırım ve koşul koymadan herkesin yararlanmasına açık biçimde sunmaktır. Bundan bol iyilik ve veriş ile sözün engellenmeden salıverilmesi kullanımları doğar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey herkese sunulur; isteyen onu alabilir veya ondan yararlanabilir ve hiç kimse engellenmez."},{"facet_id":"F002","role":"specialization","statement":"Bir kişinin iyiliği ve verdiği şeyler çoktur; verme eylemi bol ve geniştir."},{"facet_id":"F003","role":"extension","statement":"Söz herhangi bir engel veya kısıt konmadan serbestçe söylenir ya da aktarılır."}],"identity_rationale":"Kaynak ifadesi, bir şeyi ayırım ve koşul koymadan herkesin yararlanmasına sunma çekirdeğini açıkça destekler. Bol iyilik ve verme bu açıklığın nicelikçe güçlenmiş biçimi, sözün engellenmeden salıverilmesi ise aynı serbest bırakma düzeninin başka bir alana uzanmasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"herkese açık ve kimseye yasaklanmamış"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"iyiliği ve verdiği şeyler çoğaldı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"sözü engellemeden serbest bıraktı"}],"lexicalization_note":"Yalın niteleme herkese açık sunumu gösterir; kişinin bol vermesi ve sözü serbest bırakması yalnız belirtilen kalıplara bağlı uzantılardır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; cömertlik, yayılma ve esirgeme adayları açık sunum çekirdeğinin en belirgin yakınlık ve karşıtlıklarını gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu anlam veren kişinin cömertliğini merkez alır. Odak anlamda ise sunulan şeyin herkese açık olması ve kimseden esirgenmemesi belirleyicidir; söz de bu düzende salıverilebilir.","focus_only":"Odak dal bir şeyi herkesin erişimine açmayı ve sözün kısıtsız bırakılmasını kapsar.","gloss":"cömertlik ve bol verme","neighbor_only":"Komşu dal mal veya bilgi verme erdemini ve veren kişinin cömert niteliğini öne çıkarır.","neighbor_ref":"root_000274/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir şeyi başkasına esirgemeden ve bolca verme düşüncesi bulunur."},{"boundary_match":"partial","distinction":"Odak anlam erişimi açan veya sözü salan edimdir; yayılmanın gerçekleşmesini gerektirmez. Komşu anlam ise salıverme nedeninden bağımsız olarak ortaya çıkan yayılmayı adlandırır.","focus_only":"Odak dal sözün veya başka bir şeyin önündeki engelin kaldırılmasını, yani salıverme eylemini anlatır.","gloss":"yayılma ve duyulma","neighbor_only":"Komşu dal haberin veya şeyin fiilen yayılıp çok sayıda yere ya da kişiye ulaşmasını anlatır.","neighbor_ref":"root_000836/B003","relation_type":"near_neighbor","shared_zone":"Serbest bırakılan sözün insanlar arasında yayılması iki alanı aynı olay dizisinde buluşturabilir."},{"boundary_match":"opposed","distinction":"Odak dal açıklık ve salıverme kutbundadır; komşu dal ise erişimi kapatma, vermeme ve sözü tutma kutbundadır.","focus_only":"Odak dal verme, erişime açma ve söz üzerindeki engeli kaldırma yönündedir.","gloss":"esirgeme ve sözü kapatma","neighbor_only":"Komşu dal vermeyi esirgeme, elde tutma veya ağzı kapatıp sözü durdurma yönündedir.","neighbor_ref":"root_001678/B002","relation_type":"polarity_pair","shared_zone":"İki dal, malı ya da sözü serbest bırakma ile tutma arasındaki aynı karşıt eksende yer alır."}],"source_phrase_ar":"الشيء المسجل وهو المبذول لكل أحد كأنه قد صب صبا (maqayis)؛ هذا الشيء مسجل للعامة أي مرسل من شاء أخذه أو أخذ منه (ayn)؛ أسجل فلان إذا كثر خيره وعطاؤه فهو مسجل (jamhara)؛ المسجل المبذول المباح الذي لا يمنع من أحد (sihah)؛ مسجلة للبر والفاجر أي مرسلة لم يشترط فيها (sihah;tahdhib)؛ أسجلت الكلام أي أرسلته (sihah)؛ أسجلته أعطيته سجلا واستعير للعطية الكثيرة (mufradat)","source_summary":"Kaynaklar, herkese açık ve yasaksız sunma düşüncesini bolca dökülen bir verişe benzetir. Kişinin iyiliğinin çoğalması ve sözün serbest bırakılması aynı engellenmeme çizgisinin bağlı kullanımlarıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"كثرة الخير والعطاء والبذل المباح العام والإرسال غير المشروط وكلام يرسل بلا منع","what_is_not_ar":"ليس الصك ولا المساجلة ولا حجارة السجيل"},"support_links":[]},{"boundary":"Yazılı kayıt veya belge çekirdektir; yönetici ya da yargıcın bir hakkı kayda bağlaması yalnız kalıplaşmış eylem kullanımında geçerlidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000677/B004","candidate_links":[{"candidate_id":"cand_6b884ba12a183d8932d4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سِجِّيل","morph_features":"STEM|POS:N|LEM:sij~iyl|ROOT:sjl|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:4:4:1","qac_word_ref":"105:4:4","surface_ar":"سِجِّيلٍ"}],"gloss":"yazılı kayıt ve hakkı kayda bağlayarak güvenceye alma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yazılı içeriği bir arada tutan kayıt defteri, belge veya yazılı sayfa anlatılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir yükümlülüğü veya hakkı gösteren senet ve resmî belge bu kayıt türünün özel biçimidir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir açıklamada ad önce üzerine yazı yazılan taşa, ardından genel olarak her türlü yazı taşıyıcısına verilmiştir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yönetici veya yargıç bir hakkı kayda geçirir ve böylece hak sahibinin dayanağını güvenceye alır."}}],"root_ar":"س ج ل","root_id":"root_000677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yazılı belge çekirdeğini ve yönetici ya da yargıcın hakkı resmî kayda geçirme kullanımını birlikte temsil eder.","boundary_detail":"Yazılı kayıt veya belge çekirdektir; yönetici ya da yargıcın bir hakkı kayda bağlaması yalnız kalıplaşmış eylem kullanımında geçerlidir.","branch_image_ar":"الكتاب الذي يجمع ويثبت","concept_gloss":"yazılı kayıt ve hakkı kayda bağlayarak güvenceye alma","contextual_glosses":[{"applicability":"Yalın biçimin yazılı içeriği taşıyan nesneyi adlandırdığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yazıyı taşıyan defter, belge ve sayfa seçeneklerini korur."},"facet_ids":["F001"],"text":"kayıt defteri, belge veya yazılı sayfa","usage_role":"general"},{"applicability":"Bir yönetici veya yargıcın hakkı belgeleyip hak sahibine dayanak sağladığı kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yetkili kişinin kayıt işlemini ve hakkın güvence altına alınmasını korur."},"facet_ids":["F004"],"text":"hakkı resmî kayda geçirip güvenceye almak","usage_role":"contextual"}],"definition":"Çekirdek anlam, yazıyı bir arada tutan kayıt defteri, belge, senet veya yazılı sayfadır. Yönetici ya da yargıcın bir hakkı resmî kayda geçirerek güvenceye alması bu çekirdeğe bağlı eylem kullanımıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yazılı içeriği bir arada tutan kayıt defteri, belge veya yazılı sayfa anlatılır."},{"facet_id":"F002","role":"specialization","statement":"Bir yükümlülüğü veya hakkı gösteren senet ve resmî belge bu kayıt türünün özel biçimidir."},{"facet_id":"F003","role":"source_variant","statement":"Bir açıklamada ad önce üzerine yazı yazılan taşa, ardından genel olarak her türlü yazı taşıyıcısına verilmiştir."},{"facet_id":"F004","role":"associated_use","statement":"Yönetici veya yargıç bir hakkı kayda geçirir ve böylece hak sahibinin dayanağını güvenceye alır."}],"identity_rationale":"Kaynak ifadesi yazılı belge, kayıt defteri, yazı taşıyan sayfa ve hakkı güvenceye alan resmî kaydı aynı dalda destekler. Ancak çekirdek yalnızca kitap toplamak değildir; yazılı taşıyıcı ile hukuki kayda geçirme eylemi ayrı katmanlar olarak korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kayıt defteri, senet, belge veya yazılı sayfa"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yönetici veya yargıç hakkı kayda geçirip güvenceye aldı"}],"lexicalization_note":"Yalın biçim yazılı belge, kayıt defteri veya yazı taşıyıcısını gösterir; hakkı güvenceye alan kayıt eylemi yalnız yönetici ve yargıç kalıbına bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hak senedi, yazılı sayfa ve yazma-işaretleme alanları belgenin kapsamını en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu anlam hak senediyle sınırlıdır. Odak anlam ise hak senedini daha geniş yazılı kayıt alanına yerleştirir ve yetkilinin hakkı kayda geçirme eylemini de kapsar.","focus_only":"Odak dal genel yazılı kayıtları, kayıt defterlerini ve resmî kayda geçirme eylemini kapsar.","gloss":"hakkı gösteren senet","neighbor_only":"Komşu dal özellikle bir hakkı gösteren senet veya hakkın yazılı anılışında kalır.","neighbor_ref":"root_000516/B008","relation_type":"near_synonym","shared_zone":"Her iki dal bir hakkı yazılı biçimde belgeleyen senet alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu anlam taşıyıcının bilgi içeriğine yönelir. Odak anlamda içerik daha genel olabilir; resmî belge ve hakkı kayda bağlama ayrıca belirleyicidir.","focus_only":"Odak dal resmî senedi, hakkın belgelenmesini ve yetkili kişinin kayıt eylemini içerir.","gloss":"bilgi yazılan sayfa veya kitap","neighbor_only":"Komşu dal özellikle bilgelik veya bilgi yazılan sayfa ve kitap türüne yönelir.","neighbor_ref":"root_000255/B006","relation_type":"near_synonym","shared_zone":"İki dal da üzerine yazı yazılmış sayfa ya da kitap türü bir taşıyıcıyı adlandırabilir."},{"boundary_match":"partial","distinction":"Odak anlam kayıt veya belgenin kendisini ve resmî işlevini öne çıkarır. Komşu anlam ise yazının oluşturulma biçimleri ile bıraktığı çizgi ve işaretlere yönelir.","focus_only":"Odak dal tamamlanmış kayıt taşıyıcısını ve hakkı güvenceye alan belgeyi merkez alır.","gloss":"yazı, çizgi ve işaret koyma","neighbor_only":"Komşu dal çizgi çekme, yazma, damgalama, harfleri işaretleme ve satırları düzenleme işlemlerini kapsar.","neighbor_ref":"root_000587/B001","relation_type":"near_neighbor","shared_zone":"Yazılı bir kayıt, yazma ve işaret koyma işlemlerinin ürünü olabilir."}],"source_phrase_ar":"السجل كتاب يجمع كتبا ومعاني (maqayis)؛ السجل كتاب العهدة ويجمع سجلات (ayn)؛ السجل الكتاب (jamhara)؛ السجل الصك وقد سجل الحاكم تسجيلا (sihah)؛ سجل القاضي لفلان ماله أي استوثق له به (tahdhib)؛ السجل الصحيفة التي فيها الكتاب (tahdhib)؛ السجل قيل حجر كان يكتب فيه ثم سمي كل ما يكتب فيه سجلا (mufradat)","source_summary":"Kaynaklar yazılı kayıt, belge, senet ve yazı taşıyan sayfa çevresinde birleşir. Kimi anlatım yazı taşıyıcısının kökenini bir taşa bağlarken, resmî kayıt eylemi hakkın belgelenip güvenceye alınmasını gösterir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"السجل بمعنى كتاب العهدة والصك والصحيفة التي فيها الكتاب وما يكتب فيه وتسجيل الحاكم واستيثاق الحق","what_is_not_ar":"ليس الدلو ولا حجارة السجيل ولا العطاء المباح"},"support_links":["sup_092334f1b90a87fb6510"]},{"boundary":"Taş ve kil bileşimi temel gönderimdir; köken, sertlik, çokluk, gönderilme ve yazıyla belirlenme açıklamaları ayrı seçenekler olarak tutulur.","branch_kind":"unresolved","branch_ref":"root_000677/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سِجِّيل","morph_features":"STEM|POS:N|LEM:sij~iyl|ROOT:sjl|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:4:4:1","qac_word_ref":"105:4:4","surface_ar":"سِجِّيلٍ"}],"gloss":"kökeni ve niteliği tartışmalı kil ya da taş-kil parçaları","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderim, kil parçasına benzeyen taşlara, kilden taşlara veya taşla kilin karışımından oluşan parçalara yönelir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bazı açıklamalar adın başka bir dilden alınıp yerli söyleyişe uyarlandığını belirtir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başka yorumlar taşları çok veya sert diye niteler ya da adı gönderilme ve yazıyla belirlenme düşüncelerine bağlar."}}],"root_ar":"س ج ل","root_id":"root_000677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Taş gönderimini ve bunun kil bileşimiyle yabancı köken açıklamasını birlikte gösteren dal düzeyi karşılıktır.","boundary_detail":"Taş ve kil bileşimi temel gönderimdir; köken, sertlik, çokluk, gönderilme ve yazıyla belirlenme açıklamaları ayrı seçenekler olarak tutulur.","branch_image_ar":"حجارة السجيل من طين وحجر","concept_gloss":"kökeni ve niteliği tartışmalı kil ya da taş-kil parçaları","contextual_glosses":[{"applicability":"Taşların doğrudan kilden oluştuğu açıklamanın benimsendiği bağlam içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taş gönderimini ve malzemenin kil olarak açıklanmasını korur."},"facet_ids":["F001"],"text":"kilden taşlar","usage_role":"contextual"},{"applicability":"Malzemenin taşla kilin karışımı sayıldığı açıklama için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taş ve kilin birlikte oluşturduğu parça açıklamasını korur."},"facet_ids":["F001"],"text":"taş ve kil karışımı parçalar","usage_role":"contextual"},{"applicability":"Adın taşların çokluğunu ve sertliğini bildirdiği alternatif yorum için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çokluk ve sertlik üzerinden yapılan alternatif nitelemeyi korur."},"facet_ids":["F003"],"text":"çok ve sert taşlar","usage_role":"explanatory"}],"definition":"Dal, kilden oluştuğu veya taşla kilin karışımı olduğu söylenen taşları anlatır. Adın yabancı kökeni ile sertlik, çokluk, gönderilme ya da yazıyla belirlenme üzerinden yapılan açıklamalar alternatif yorumlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderim, kil parçasına benzeyen taşlara, kilden taşlara veya taşla kilin karışımından oluşan parçalara yönelir."},{"facet_id":"F002","role":"source_variant","statement":"Bazı açıklamalar adın başka bir dilden alınıp yerli söyleyişe uyarlandığını belirtir."},{"facet_id":"F003","role":"source_variant","statement":"Başka yorumlar taşları çok veya sert diye niteler ya da adı gönderilme ve yazıyla belirlenme düşüncelerine bağlar."}],"identity_rationale":"Kaynak ifadesinde temel gönderim kil benzeri taşlara veya taşla kilin karışımına yönelir; bu nedenle taş dalı korunabilir. Bununla birlikte sözcüğün yabancı kökenli oluşu, sertlik veya çokluk bildirmesi, gönderilmiş ya da yazıyla belirlenmiş şey anlamından türemesi gibi açıklamalar birbirinin yerine geçen yorumlardır ve tek bir kurucu anlam gibi birleştirilemez.","lexicalization_note":"Kanıt herhangi bir yalın ya da kalıplaşmış birim sınıfı belirlemez; bu yüzden dalın kapsamı bağımsız bir yalın kök anlamı olarak varsayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnız küçük taş ve çakıl adayı taş gönderiminin sınırını doğrudan aydınlattı, öteki adaylar ortak alan bakımından yetersiz kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu anlam taşın küçüklüğüne ve toplu küçük taşlara dayanır. Odak anlamın belirleyici yanı kil ya da taş-kil bileşimi ve buna eşlik eden yorum ayrılıklarıdır.","focus_only":"Odak dal taşların kil kökenini veya taş-kil bileşimini ve adın yorumlanan niteliğini içerir.","gloss":"küçük taş ve çakıl","neighbor_only":"Komşu dal genel olarak küçük taşları, tek bir küçük taşı veya küçük taşlı araziyi anlatır.","neighbor_ref":"root_000332/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da tek tek taş parçalarını adlandırabilir."}],"source_phrase_ar":"السجيل حجارة كالمدر وهو حجر وطين ويفسر أنه معرب دخيل (ayn)؛ حجارة من سجيل قالوا هي حجارة من طين (sihah)؛ السجيل حجر وطين مختلط وأصله فيما قيل فارسي معرب (mufradat)؛ سجيل من السجل وقد يحتمل أن يكون مشتقا وقالوا السجيل الشديد (maqayis)؛ من سجيل أقوالا (tahdhib)؛ فارسي أعرب (tahdhib)؛ تأويله كثيرة شديدة (tahdhib)؛ سجيل من سجلته أي أرسلته (tahdhib)؛ من سجل أي ما كتب لهم (tahdhib)؛ أراد سجيلا أي شديدا وإنما أبدل اللام نونا (maqayis)","source_summary":"Kaynaklar taşları kil kökenli veya taş-kil karışımı parçalar olarak açıklama eğilimindedir. Adın başka bir dilden gelişi ile sertlik, çokluk, gönderilme ve yazıyla belirlenme açıklamaları ise birbirinden farklı seçenekler olarak aktarılır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"السجيل بمعنى حجارة من طين أو حجر وطين مع ما قيل في كونها معربة أو شديدة أو كثيرة أو مرسلة أو مكتوبة","what_is_not_ar":"ليس السجل الصك ولا الدلو ولا السجنجل"},"support_links":[]},{"boundary":"Memenin dolu, uzun veya büyük oluşu çekirdektir; gevşek sallanan meme ile torbası gevşemiş testis ayrı uzmanlaşmış kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000677/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سِجِّيل","morph_features":"STEM|POS:N|LEM:sij~iyl|ROOT:sjl|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:4:4:1","qac_word_ref":"105:4:4","surface_ar":"سِجِّيلٍ"}],"gloss":"dolgun, uzun veya gevşekçe sarkan organ","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Meme dolu, uzun veya büyük olarak nitelenir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Meme geniş, gevşek ve hareket ettikçe sallanır durumdadır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Testis, onu saran torbanın gevşemiş olmasıyla nitelenir."}}],"root_ar":"س ج ل","root_id":"root_000677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Memenin doluluk, uzunluk, büyüklük ve gevşekliğini, ayrıca testis torbasındaki gevşemeyi üst düzeyde bir araya getirir.","boundary_detail":"Memenin dolu, uzun veya büyük oluşu çekirdektir; gevşek sallanan meme ile torbası gevşemiş testis ayrı uzmanlaşmış kullanımlardır.","branch_image_ar":"امتلاء العضو وطوله واسترخاؤه","concept_gloss":"dolgun, uzun veya gevşekçe sarkan organ","contextual_glosses":[{"applicability":"Memenin doluluğu, uzunluğu ya da büyüklüğü öne çıkarıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Meme için verilen doluluk, uzunluk ve büyüklük seçeneklerini korur."},"facet_ids":["F001"],"text":"dolu, uzun veya büyük meme","usage_role":"general"},{"applicability":"Memenin genişliğiyle birlikte gevşek ve hareketli oluşunu anlatan özel kalıp içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Memenin geniş, gevşek ve sallanır durumunu birlikte korur."},"facet_ids":["F002"],"text":"geniş, gevşek ve sallanan meme","usage_role":"contextual"},{"applicability":"Testisi saran torbanın gevşek olduğu organ nitelemesi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Niteliğin testis torbasındaki gevşeklikten kaynaklandığını korur."},"facet_ids":["F003"],"text":"torbası gevşemiş testis","usage_role":"contextual"}],"definition":"Meme için dolu, uzun veya büyük oluşu; daha dar bir kullanımda geniş, gevşek ve sallanır oluşu anlatır. Ayrı bir bağlı kullanım, torbası gevşemiş testisi niteler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Meme dolu, uzun veya büyük olarak nitelenir."},{"facet_id":"F002","role":"specialization","statement":"Meme geniş, gevşek ve hareket ettikçe sallanır durumdadır."},{"facet_id":"F003","role":"specialization","statement":"Testis, onu saran torbanın gevşemiş olmasıyla nitelenir."}],"identity_rationale":"Kaynak ifadesi meme için doluluk, uzunluk, büyüklük, genişlik ve gevşek sallanma niteliklerini; testis için ise torbanın gevşemiş olmasını destekler. Bu nitelikler ortak bir bedensel görünüm alanında buluşsa da hepsi her organ için geçerli değildir ve ayrı kullanımlar olarak sınırlandırılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"uzun, dolu veya büyük meme"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"geniş, gevşek ve sallanan meme"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"torbası gevşemiş testis"}],"lexicalization_note":"Yalın biçim memenin doluluk, uzunluk veya büyüklüğünü anlatır; gevşek meme ve testis nitelemeleri yalnız kendi organ adlarıyla kurulan kalıplarda geçerlidir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; meme doluluğu ve genel gevşeklik adayları organ niteliğinin sınırlarını en doğrudan gösterdiği için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu anlam sütle dolma ve yukarı yükselmeye odaklanır. Odak anlam ise doluluğun yanında uzunluk, büyüklük ve gevşek sallanmayı da içerir.","focus_only":"Odak dal memenin uzun veya büyük oluşunu, gevşekçe sallanmasını ve ayrıca testis torbasındaki gevşekliği kapsar.","gloss":"sütle dolup yükselen meme","neighbor_only":"Komşu dal memenin karna doğru yükselmesini veya sütle dolmasını özellikle öne çıkarır.","neighbor_ref":"root_000350/B005","relation_type":"near_synonym","shared_zone":"İki dal da memenin dolu ve belirgin görünümünü anlatabilir."},{"boundary_match":"partial","distinction":"Komşu anlam dolma sürecini ve sıvı birikimini merkez alır. Odak anlam ise organın uzun, büyük ya da gevşek görünüşünü niteleyen durum sözüdür.","focus_only":"Odak dal memenin uzunluğunu, büyüklüğünü ve gevşekliğini, ayrıca testis torbasındaki gevşemeyi içerir.","gloss":"memenin dolması ve sıvının birikmesi","neighbor_only":"Komşu dal memenin sütle dolma sürecinden başka suyun çoğalması ve başka sıvıların birikmesi alanlarına da uzanır.","neighbor_ref":"root_000555/B007","relation_type":"near_synonym","shared_zone":"Her iki dal memenin dolu hale gelmesini veya dolu görünmesini anlatır."},{"boundary_match":"partial","distinction":"Odak anlam anatomik biçim ve sarkma niteliğidir; güçsüzlük gerektirmez. Komşu anlam ise daha geniş bir alanda yapısal zayıflık ve dayanıksızlığı anlatır.","focus_only":"Odak dal gevşekliği belirli organların sarkık ve sallanır görünümüyle sınırlar.","gloss":"gevşeklik ve güçsüzlük","neighbor_only":"Komşu dal gevşekliği insan, mızrak, toprak veya dal gibi çok çeşitli varlıklarda zayıflık ve dayanıksızlık olarak ele alır.","neighbor_ref":"root_000445/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da sıkılığın azalması ve gevşek bir durum bulunur."}],"source_phrase_ar":"يقال للضرع الممتلئ سجل (maqayis)؛ السجل من الضروع الطويل (ayn)؛ خصية سجيلة أي مسترخية الصفن (ayn)؛ ناقة سجلاء عظيمة الضرع (jamhara)؛ السجيل من الضروع الطويل يقال ناقة سجلاء (sihah)؛ السجيل من الضروع الطويل (tahdhib)؛ الخصية السجيلة المسترخية الصفن (tahdhib)؛ ضرع أسجل وهو الواسع الرخو المضطرب (tahdhib)","source_summary":"Kaynaklar memenin dolu, uzun veya büyük görünümünde birleşir ve geniş, gevşek, sallanan meme kullanımını ayrıca verir. Testise ilişkin kullanımda nitelik doğrudan testisten çok onu saran torbanın gevşekliğidir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"الضرع الممتلئ أو الطويل أو العظيم أو الواسع الرخو وخصية سجيلة مسترخية الصفن","what_is_not_ar":"ليس الدلو ولا الكتاب ولا المساجلة"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["105:4:1"],"branch_refs":[],"candidate_id":"cand_9cb7412ac160e13f0ded","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000603"],"scope":"focus_ayah","source_local_id":"105:4:1:feminine-and-variant-agency","source_type":"word_analysis","support_ids":["sup_30d13eb494c312bfae11","sup_6780b01fec69d668a88e"],"title":"main agreement names the birds while variant exposes agency layering","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:4:1","qac_refs":["105:4:1:1","105:4:1:2"],"status":"accepted"}},{"anchor_refs":["105:4:1"],"branch_refs":[],"candidate_id":"cand_8680b82b043fe58a44a1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000603"],"scope":"focus_ayah","source_local_id":"105:4:1:projectile-and-verdict-root-pressure","source_type":"word_analysis","support_ids":["sup_6780b01fec69d668a88e","sup_99eb4c84d49ec2c3915d"],"title":"physical throwing carries judgment pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:4:1","qac_refs":["105:4:1:1","105:4:1:2"],"status":"accepted"}},{"anchor_refs":["105:4:1"],"branch_refs":[],"candidate_id":"cand_a5681db42bde231025f5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000603"],"scope":"focus_ayah","source_local_id":"105:4:1:target-in-verb-frame","source_type":"word_analysis","support_ids":["sup_6780b01fec69d668a88e","sup_9cfa033cc045d0270fb8"],"title":"attached object fixes the army as target","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:4:1","qac_refs":["105:4:1:1","105:4:1:2"],"status":"accepted"}},{"anchor_refs":["105:4:1"],"branch_refs":[],"candidate_id":"cand_e002a7476588c0f62c0f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000603"],"scope":"focus_ayah","source_local_id":"105:4:1:vivid-imperfect-continuation","source_type":"word_analysis","support_ids":["sup_6780b01fec69d668a88e","sup_74d840ec90e5f57627db"],"title":"imperfect verb makes dispatch visible as pelting","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:4:1","qac_refs":["105:4:1:1","105:4:1:2"],"status":"accepted"}},{"anchor_refs":["105:4:2"],"branch_refs":[],"candidate_id":"cand_2a1096f72858c5d68396","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000296"],"scope":"focus_ayah","source_local_id":"105:4:2:formulaic-stone-sijjil-pair","source_type":"word_analysis","support_ids":["sup_bd2dfe26f6b692cd38eb","sup_f6e010fe8501ca5eb1cc"],"title":"stone phrase joins a repeated punishment formula","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:4:2","qac_refs":["105:4:2:1","105:4:2:2"],"status":"accepted"}},{"anchor_refs":["105:4:2"],"branch_refs":[],"candidate_id":"cand_0098fb0885ab2430890a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000296"],"scope":"focus_ayah","source_local_id":"105:4:2:indefinite-plural-payload","source_type":"word_analysis","support_ids":["sup_990d8e57c55524eafb2e","sup_f6e010fe8501ca5eb1cc"],"title":"indefinite broken plural leaves the payload uncounted","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:4:2","qac_refs":["105:4:2:1","105:4:2:2"],"status":"accepted"}},{"anchor_refs":["105:4:2"],"branch_refs":[],"candidate_id":"cand_fcd2c707c016b0a19521","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000296"],"scope":"focus_ayah","source_local_id":"105:4:2:instrumental-projectile","source_type":"word_analysis","support_ids":["sup_ba00da212aa573f0f84a","sup_f6e010fe8501ca5eb1cc"],"title":"bāʾ marks stones as projectile means","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:4:2","qac_refs":["105:4:2:1","105:4:2:2"],"status":"accepted"}},{"anchor_refs":["105:4:2"],"branch_refs":[],"candidate_id":"cand_1f8fd52c1755de41772a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000296"],"scope":"focus_ayah","source_local_id":"105:4:2:prepositional-hinge-and-cadence","source_type":"word_analysis","support_ids":["sup_20bdacd136aa6c58e970","sup_f6e010fe8501ca5eb1cc"],"title":"middle phrase hands action to final specification","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:4:2","qac_refs":["105:4:2:1","105:4:2:2"],"status":"accepted"}},{"anchor_refs":["105:4:2"],"branch_refs":[],"candidate_id":"cand_44373352818fc4a2d9fa","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000296"],"scope":"focus_ayah","source_local_id":"105:4:2:stone-restraint-pressure","source_type":"word_analysis","support_ids":["sup_413b3564246e7be78c51","sup_f6e010fe8501ca5eb1cc"],"title":"concrete stones carry restraint pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:4:2","qac_refs":["105:4:2:1","105:4:2:2"],"status":"accepted"}},{"anchor_refs":["105:4:3"],"branch_refs":[],"candidate_id":"cand_0abefd90a0e126b4edcd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:4:3:internal-preposition-chain","source_type":"word_analysis","support_ids":["sup_841b0370fee01f956464","sup_dc0b5dce8941f9343439"],"title":"internal prepositions tighten one syntactic unit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:4:3","qac_refs":["105:4:3:1"],"status":"accepted"}},{"anchor_refs":["105:4:3"],"branch_refs":[],"candidate_id":"cand_7a288b3f4ad439899849","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:4:3:min-material-source-polyvalence","source_type":"word_analysis","support_ids":["sup_dc0b5dce8941f9343439","sup_e71cd930989d1d7ff899"],"title":"particle keeps material and source readings live","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:4:3","qac_refs":["105:4:3:1"],"status":"accepted"}},{"anchor_refs":["105:4:3"],"branch_refs":[],"candidate_id":"cand_3eacbc23a6d5499410c7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"105:4:3:separate-preposition-and-sound-hinge","source_type":"word_analysis","support_ids":["sup_59982430216b37893fb0","sup_dc0b5dce8941f9343439"],"title":"separate preposition makes the final turn audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:4:3","qac_refs":["105:4:3:1"],"status":"accepted"}},{"anchor_refs":["105:4:4"],"branch_refs":[],"candidate_id":"cand_15a0686cd6ac92583045","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000677"],"scope":"focus_ayah","source_local_id":"105:4:4:arabicized-indefinite-loanword","source_type":"word_analysis","support_ids":["sup_718ff68b907c7c50f390","sup_9e363270cb85bb5fb2b4"],"title":"foreign-looking term is fully integrated grammatically","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:4:4","qac_refs":["105:4:4:1"],"status":"accepted"}},{"anchor_refs":["105:4:4"],"branch_refs":[],"candidate_id":"cand_9cf19048d8798cb19833","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000677"],"scope":"focus_ayah","source_local_id":"105:4:4:final-position-and-sound-closure","source_type":"word_analysis","support_ids":["sup_718ff68b907c7c50f390","sup_a10a1bb73e68ceca75ac"],"title":"closing sound and position seal the ayah","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:4:4","qac_refs":["105:4:4:1"],"status":"accepted"}},{"anchor_refs":["105:4:4"],"branch_refs":[],"candidate_id":"cand_5a47520a6884167bb83c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000677"],"scope":"focus_ayah","source_local_id":"105:4:4:min-endpoint-and-attachment","source_type":"word_analysis","support_ids":["sup_718ff68b907c7c50f390","sup_f28dda40e958c6c32202"],"title":"final genitive completes source or material specification","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:4:4","qac_refs":["105:4:4:1"],"status":"accepted"}},{"anchor_refs":["105:4:4"],"branch_refs":[],"candidate_id":"cand_2b5859b2b5fd692589a4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000677"],"scope":"focus_ayah","source_local_id":"105:4:4:poured-and-formulaic-parallels","source_type":"word_analysis","support_ids":["sup_718ff68b907c7c50f390","sup_fe0b7a6ffa9966a22238"],"title":"formula recurrence adds rained-stone pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:4:4","qac_refs":["105:4:4:1"],"status":"accepted"}},{"anchor_refs":["105:4:4"],"branch_refs":[],"candidate_id":"cand_8699b5037056379631b9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000677"],"scope":"focus_ayah","source_local_id":"105:4:4:stone-clay-and-record-tension","source_type":"word_analysis","support_ids":["sup_718ff68b907c7c50f390","sup_ee6be9887692297f9795"],"title":"material clay and decree pressure remain together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"105:4:4","qac_refs":["105:4:4:1"],"status":"accepted"}},{"anchor_refs":["105:4:1"],"branch_refs":[],"candidate_id":"cand_a5f4153f8d0ed935a052","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000603"],"scope":"focus_ayah","source_local_id":"105:4:1:1","source_type":"qac_morpheme","support_ids":["sup_245caa6afeaaab5feb92"],"title":"QAC root occurrence: ر م ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["105:4:2"],"branch_refs":[],"candidate_id":"cand_1b2f06db33a3d57ba861","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000296"],"scope":"focus_ayah","source_local_id":"105:4:2:2","source_type":"qac_morpheme","support_ids":["sup_3d72b10023d73f1341f3"],"title":"QAC root occurrence: ح ج ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["105:4:4"],"branch_refs":[],"candidate_id":"cand_d7f27f20963e5e83c400","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000677"],"scope":"focus_ayah","source_local_id":"105:4:4:1","source_type":"qac_morpheme","support_ids":["sup_1f06aaa8462766499a36"],"title":"QAC root occurrence: س ج ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["105:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"105:4","branch_refs":["root_000296/B003","root_000603/B001","root_000677/B001"],"candidate_id":"cand_0819d1aab4a78d02a5c7","commentary_obligation":"review","hft_ref":"hft_afb964e2c20ee6f0fb9e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_projectile_outpouring","source_type":"hft","support_ids":["sup_0cfb5995aa42493eee81"],"title":"base_projectile_outpouring","trust":"legacy_unbound"},{"anchor_refs":["105:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"105:4","branch_refs":["root_000296/B003","root_000603/B004","root_000677/B001"],"candidate_id":"cand_76be9c458609695a8d5d","commentary_obligation":"review","hft_ref":"hft_19cd95d015464f92f757","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_lithic_precipitation","source_type":"hft","support_ids":["sup_e12af88c6d6fb2856c10"],"title":"base_lithic_precipitation","trust":"legacy_unbound"},{"anchor_refs":["105:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"105:4","branch_refs":["root_000296/B001","root_000296/B003","root_000603/B008","root_000677/B004"],"candidate_id":"cand_6b884ba12a183d8932d4","commentary_obligation":"review","hft_ref":"hft_be518c7379d2a8071072","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_executable_record","source_type":"hft","support_ids":["sup_092334f1b90a87fb6510"],"title":"base_executable_record","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"تَرْمِيهِم بِحِجَارَةٍۢ مِّن سِجِّيلٍۢ","qac_morphemes":[{"lemma_ar":"رَمَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:ramaY`|ROOT:rmy|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"105:4:1:1","qac_word_ref":"105:4:1","root_ar":"ر م ي","surface_ar":"تَرْمِي"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"105:4:1:2","qac_word_ref":"105:4:1","root_ar":"","surface_ar":"هِم"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"105:4:2:1","qac_word_ref":"105:4:2","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"حِجَارَة","morph_features":"STEM|POS:N|LEM:HijaArap|ROOT:Hjr|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:4:2:2","qac_word_ref":"105:4:2","root_ar":"ح ج ر","surface_ar":"حِجَارَةٍ"},{"lemma_ar":"مِن","morph_features":"STEM|POS:P|LEM:min","morpheme_role":"STEM","pos":"P","qac_ref":"105:4:3:1","qac_word_ref":"105:4:3","root_ar":"","surface_ar":"مِّن"},{"lemma_ar":"سِجِّيل","morph_features":"STEM|POS:N|LEM:sij~iyl|ROOT:sjl|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:4:4:1","qac_word_ref":"105:4:4","root_ar":"س ج ل","surface_ar":"سِجِّيلٍ"}],"word_analysis_qac_refs":[["105:4:1:1","105:4:1:2"],["105:4:2:1","105:4:2:2"],["105:4:3:1"],["105:4:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["105:4:1","105:4:2","105:4:3","105:4:4"]},"focus_surface_evidence":{"arabic_uthmani":"تَرْمِيهِم بِحِجَارَةٍۢ مِّن سِجِّيلٍۢ","qac_morphemes":[{"lemma_ar":"رَمَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:ramaY`|ROOT:rmy|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"105:4:1:1","qac_word_ref":"105:4:1","root_ar":"ر م ي","surface_ar":"تَرْمِي"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"105:4:1:2","qac_word_ref":"105:4:1","root_ar":"","surface_ar":"هِم"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"105:4:2:1","qac_word_ref":"105:4:2","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"حِجَارَة","morph_features":"STEM|POS:N|LEM:HijaArap|ROOT:Hjr|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:4:2:2","qac_word_ref":"105:4:2","root_ar":"ح ج ر","surface_ar":"حِجَارَةٍ"},{"lemma_ar":"مِن","morph_features":"STEM|POS:P|LEM:min","morpheme_role":"STEM","pos":"P","qac_ref":"105:4:3:1","qac_word_ref":"105:4:3","root_ar":"","surface_ar":"مِّن"},{"lemma_ar":"سِجِّيل","morph_features":"STEM|POS:N|LEM:sij~iyl|ROOT:sjl|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"105:4:4:1","qac_word_ref":"105:4:4","root_ar":"س ج ل","surface_ar":"سِجِّيلٍ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["105:4:1:1","105:4:1:2"],["105:4:2:1","105:4:2:2"],["105:4:3:1"],["105:4:4:1"]],"word_analysis_refs":["105:4:1","105:4:2","105:4:3","105:4:4"],"word_rows":[{"analysis_record_ref":"105:4:1","analytic_gloss_range_en":"ongoing directed pelting with an attached human target and a separate bāʾ-marked projectile instrument","analytic_root_gloss_range_en":"root range includes physical throwing or shooting, projectile targeting, accusatory speech, reaching a limit, and other construction-bound branches; the local frame selects physical pelting while accusation and agency pressure remain secondary","qac_refs":["105:4:1:1","105:4:1:2"],"root":{"arabic":"ر م ي","transliteration":"r-m-y"},"surface":{"arabic":"تَرْمِيهِم","transliteration":"tarmīhim"}},{"analysis_record_ref":"105:4:2","analytic_gloss_range_en":"indefinite broken plural stones marked by bāʾ as the projectile instrument of the pelting","analytic_root_gloss_range_en":"root range includes hard stone, restraint, enclosure, protected space, and related boundary images; the local noun selects concrete stones while restraint/boundary pressure survives as impact imagery","qac_refs":["105:4:2:1","105:4:2:2"],"root":{"arabic":"ح ج ر","transliteration":"ḥ-j-r"},"surface":{"arabic":"بِحِجَارَةٍ","transliteration":"bi-ḥijāratin"}},{"analysis_record_ref":"105:4:3","analytic_gloss_range_en":"preposition introducing the final source, kind, or material specification of the stones, with partitive source-depth possible but not forced","analytic_root_gloss_range_en":null,"qac_refs":["105:4:3:1"],"root":{},"surface":{"arabic":"مِن","transliteration":"min"}},{"analysis_record_ref":"105:4:4","analytic_gloss_range_en":"final genitive noun specifying the stones as sijjīl, locally holding hardened clay/stone material together with source, record, or decree pressure","analytic_root_gloss_range_en":"root range includes bucket/pouring imagery, record or registration, competitive exchange, unrestricted outpouring, and the reviewed sijjīl stone-clay branch; the local phrase selects the stone-clay/decree-marked punishment term while other branches remain secondary pressure","qac_refs":["105:4:4:1"],"root":{"arabic":"س ج ل","transliteration":"s-j-l"},"surface":{"arabic":"سِجِّيلٍ","transliteration":"sijjīlin"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["105:4"],"branch_refs":["root_000296/B003","root_000603/B001","root_000677/B001"],"candidate_id":"cand_0819d1aab4a78d02a5c7","evidence_scope":"focus_ayah","hft_ref":"hft_afb964e2c20ee6f0fb9e","item_id":"base_projectile_outpouring","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_projectile_outpouring","support_id":"sup_0cfb5995aa42493eee81"},{"anchor_refs":["105:4"],"branch_refs":["root_000296/B003","root_000603/B004","root_000677/B001"],"candidate_id":"cand_76be9c458609695a8d5d","evidence_scope":"focus_ayah","hft_ref":"hft_19cd95d015464f92f757","item_id":"base_lithic_precipitation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_lithic_precipitation","support_id":"sup_e12af88c6d6fb2856c10"},{"anchor_refs":["105:4"],"branch_refs":["root_000296/B001","root_000296/B003","root_000603/B008","root_000677/B004"],"candidate_id":"cand_6b884ba12a183d8932d4","evidence_scope":"focus_ayah","hft_ref":"hft_be518c7379d2a8071072","item_id":"base_executable_record","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_executable_record","support_id":"sup_092334f1b90a87fb6510"}],"diagnostics":[],"lane_counts":{"global":9,"macro":9,"micro":3},"packet_summary":{"ayah_count":5,"focus_ref":"105:4","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]}],"window":["105:1","105:2","105:3","105:4","105:5"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"105:4","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":12,"unstructured_record_count":0},"identity":{"ayah_ref":"105:4","lane":"micro","linguistic_source_ref":"105:4","surface_ref":"105:4","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"105:4","target_tokens":[["Onlara",["105:4:1"]],["pişmiş",["105:4:4"]],["balçıktan",["105:4:3","105:4:4"]],["taşlar",["105:4:2"]],["atıyorlardı",["105:4:1"]]],"text":"Onlara pişmiş balçıktan taşlar atıyorlardı."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":5,"id":"s105-p01-001-005","label":"Whole surah","number":1,"refs":["105:1","105:2","105:3","105:4","105:5"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"105:4:4:1","source_type":"qac_morpheme","support_id":"sup_1f06aaa8462766499a36","text":"{\"lemma_ar\":\"سِجِّيل\",\"morph_features\":\"STEM|POS:N|LEM:sij~iyl|ROOT:sjl|M|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"105:4:4:1\",\"qac_word_ref\":\"105:4:4\",\"root_ar\":\"س ج ل\",\"surface_ar\":\"سِجِّيلٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:2:prepositional-hinge-and-cadence","source_type":"word_analysis","support_id":"sup_20bdacd136aa6c58e970","text":"{\"blocking_evidence\":null,\"headline\":\"middle phrase hands action to final specification\",\"reader_payoff\":\"The reader notices the word as the middle hinge: the pelting is narrowed into a stone instrument, and the stone instrument is then narrowed by its source or material.\",\"reason\":\"Attachment evidence links the stone phrase to the verb and then links {{ar:سِجِّيلٍ}} ({{tr:sijjīlin}}) to the stone phrase through {{ar:مِن}} ({{tr:min}}), supporting the cascade and cadence claims.\",\"representative_source_ids\":[\"QT-8831df8e\",\"QT-b3b29b9a\",\"QP-1549802f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"105:4:1:1","source_type":"qac_morpheme","support_id":"sup_245caa6afeaaab5feb92","text":"{\"lemma_ar\":\"رَمَىٰ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:ramaY`|ROOT:rmy|3FS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"105:4:1:1\",\"qac_word_ref\":\"105:4:1\",\"root_ar\":\"ر م ي\",\"surface_ar\":\"تَرْمِي\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:1:feminine-and-variant-agency","source_type":"word_analysis","support_id":"sup_30d13eb494c312bfae11","text":"{\"blocking_evidence\":null,\"headline\":\"main agreement names the birds while variant exposes agency layering\",\"reader_payoff\":\"The reader notices two layers of agency: the main form grammatically assigns the pelting to the birds from 105:3, while {{ar:يَرْمِيهِمْ}} ({{tr:yarmīhim}}) makes the higher-agent pressure visible without controlling the canonical parse.\",\"reason\":\"The canonical local grammar supports the feminine collective subject from {{ar:طَيْرًا}} ({{tr:ṭayran}}); the masculine variant is useful as contrast but cannot replace that main agreement.\",\"representative_source_ids\":[\"QG-378c0f29\",\"QG-d69c5dc3\",\"QY-2b7965bd\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"105:4:2:2","source_type":"qac_morpheme","support_id":"sup_3d72b10023d73f1341f3","text":"{\"lemma_ar\":\"حِجَارَة\",\"morph_features\":\"STEM|POS:N|LEM:HijaArap|ROOT:Hjr|F|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"105:4:2:2\",\"qac_word_ref\":\"105:4:2\",\"root_ar\":\"ح ج ر\",\"surface_ar\":\"حِجَارَةٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:2:stone-restraint-pressure","source_type":"word_analysis","support_id":"sup_413b3564246e7be78c51","text":"{\"blocking_evidence\":null,\"headline\":\"concrete stones carry restraint pressure\",\"reader_payoff\":\"The reader notices that the stones are concrete projectiles, while the broader {{ar:ح ج ر}} ({{tr:ḥ-j-r}}) field makes their impact feel like enforced limit and restraint.\",\"reason\":\"V4 separates hard-stone senses from restraint and enclosure branches; the local noun selects concrete stones, so restraint survives as image pressure rather than an alternate local gloss.\",\"representative_source_ids\":[\"QS-4eb0c77c\",\"QS-66b7d41d\",\"QS-ce7bd6d7\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:3:separate-preposition-and-sound-hinge","source_type":"word_analysis","support_id":"sup_59982430216b37893fb0","text":"{\"blocking_evidence\":null,\"headline\":\"separate preposition makes the final turn audible\",\"reader_payoff\":\"The reader notices a formal contrast: the bāʾ is fused to the stone noun, but {{ar:مِن}} ({{tr:min}}) stands as a separate, audibly compressed hinge into the final word.\",\"reason\":\"The surface form is an independent preposition before {{ar:سِجِّيلٍ}} ({{tr:sijjīlin}}), and the recited transition after the tanwīn of {{ar:حِجَارَةٍ}} ({{tr:ḥijāratin}}) supports the sound-hinge claim.\",\"representative_source_ids\":[\"QF-61054e56\",\"QF-a4f5ba8e\",\"QP-627de166\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:1","source_type":"word_analysis","support_id":"sup_6780b01fec69d668a88e","text":"{\"gloss_range\":\"ongoing directed pelting with an attached human target and a separate bāʾ-marked projectile instrument\",\"prose\":\"{{ar:تَرْمِيهِم}} ({{tr:tarmīhim}}) turns the prior sending of birds into a live impact scene: the imperfect form lets the listener watch the pelting happen rather than receive it as a completed report. The opening verb also keeps 105:4 dependent on 105:3, because its feminine singular agreement reaches back to {{ar:طَيْرًا}} ({{tr:ṭayran}}) while its attached {{ar:هِم}} ({{tr:him}}) keeps the elephant people as the fixed target. The verb's frame splits target from projectile: {{ar:هِم}} ({{tr:him}}) is the direct object, while {{ar:بِحِجَارَةٍ}} ({{tr:bi-ḥijāratin}}) names the means, so the scene is not falling debris but directed pelting of identified victims. The masculine variant {{ar:يَرْمِيهِمْ}} ({{tr:yarmīhim}}) does not replace the main reading, but it exposes the agency layering already present between visible birds and divine dispatch. The broader {{ar:ر م ي}} ({{tr:r-m-y}}) field selects physical throwing here, while its accusation register lets the stones feel like materialized judgment rather than random projectiles; the same root-and-bāʾ projectile frame recurs in 77:32.\",\"root_display\":\"{{ar:ر م ي}} ({{tr:r-m-y}})\",\"root_gloss_range\":\"root range includes physical throwing or shooting, projectile targeting, accusatory speech, reaching a limit, and other construction-bound branches; the local frame selects physical pelting while accusation and agency pressure remain secondary\",\"surface_display\":\"{{ar:تَرْمِيهِم}} ({{tr:tarmīhim}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:4","source_type":"word_analysis","support_id":"sup_718ff68b907c7c50f390","text":"{\"gloss_range\":\"final genitive noun specifying the stones as sijjīl, locally holding hardened clay/stone material together with source, record, or decree pressure\",\"prose\":\"{{ar:سِجِّيلٍ}} ({{tr:sijjīlin}}) is the endpoint of the ayah's narrowing chain: after pelting and stones, this final genitive word decides the stones' nature or source. Its position after {{ar:مِن}} ({{tr:min}}) allows two local routes, either classifying {{ar:حِجَارَةٍ}} ({{tr:ḥijāratin}}) by material/kind or presenting {{ar:سِجِّيلٍ}} ({{tr:sijjīlin}}) as the source or authority behind the pelting. The foreign-loan and Arabic-root dispute is therefore not ornamental here: the phrase keeps hardened stone-clay matter and record/decree pressure together, while speculative extensions beyond that are not needed. The tanwīn and full declension integrate the debated word into Arabic grammar even as its exact substance remains unspecific. The same stone-with-{{ar:سِجِّيلٍ}} ({{tr:sijjīlin}}) formula recurs at 11:82 and 15:74, keeping poured or rained delivery pressure in the background, and the comparison with clay-stones at 51:33 shows what a plainer material wording would lose. The doubled jīm, long ī, and final lām give the closing word a compressed terminal weight, so the ayah lands on matter, mark, recurrence, and closure at once.\",\"root_display\":\"{{ar:س ج ل}} ({{tr:s-j-l}})\",\"root_gloss_range\":\"root range includes bucket/pouring imagery, record or registration, competitive exchange, unrestricted outpouring, and the reviewed sijjīl stone-clay branch; the local phrase selects the stone-clay/decree-marked punishment term while other branches remain secondary pressure\",\"surface_display\":\"{{ar:سِجِّيلٍ}} ({{tr:sijjīlin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:1:vivid-imperfect-continuation","source_type":"word_analysis","support_id":"sup_74d840ec90e5f57627db","text":"{\"blocking_evidence\":null,\"headline\":\"imperfect verb makes dispatch visible as pelting\",\"reader_payoff\":\"The reader notices that 105:4 does not restart the story; {{ar:تَرْمِيهِم}} ({{tr:tarmīhim}}) turns the birds sent in 105:3 into an ongoing impact scene.\",\"reason\":\"QAC identifies the word as an imperfect verb with 3fs agreement, and the clause opens without a new conjunction, so the CRITICAL continuation and vivid-aspect claims are locally supported.\",\"representative_source_ids\":[\"QG-24796217\",\"QF-69786638\",\"QT-306ccbbb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:3:internal-preposition-chain","source_type":"word_analysis","support_id":"sup_841b0370fee01f956464","text":"{\"blocking_evidence\":null,\"headline\":\"internal prepositions tighten one syntactic unit\",\"reader_payoff\":\"The reader notices that the ayah is organized by internal prepositions rather than a new boundary connector, so the pelting remains an elaboration of the birds from 105:3.\",\"reason\":\"Attachment evidence treats the whole phrase as one verbal clause headed by {{ar:تَرْمِيهِم}} ({{tr:tarmīhim}}), with bāʾ and {{ar:مِن}} ({{tr:min}}) organizing the instrument-to-source progression.\",\"representative_source_ids\":[\"QT-b13464af\",\"QT-f2830f1d\",\"QB-47d68195\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:2:indefinite-plural-payload","source_type":"word_analysis","support_id":"sup_990d8e57c55524eafb2e","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite broken plural leaves the payload uncounted\",\"reader_payoff\":\"The reader notices that the wording gives concrete stones without a fixed known set, so the payload feels multiple and unspecified.\",\"reason\":\"The noun is an indefinite genitive broken plural with tanwīn, matching the CRITICAL claim that quantity and individual identity are left open.\",\"representative_source_ids\":[\"QG-c4d179e3\",\"QF-3acb49d5\",\"QF-546fd03d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:1:projectile-and-verdict-root-pressure","source_type":"word_analysis","support_id":"sup_99eb4c84d49ec2c3915d","text":"{\"blocking_evidence\":null,\"headline\":\"physical throwing carries judgment pressure\",\"reader_payoff\":\"The reader notices that the local act is physical pelting, yet the wider {{ar:ر م ي}} ({{tr:r-m-y}}) field lets the strike feel like accusation or condemnation made material.\",\"reason\":\"The bāʾ-projectile frame selects physical throwing, and the recurrence of the same construction in 77:32 supports the projectile syntax; accusation remains root-family pressure rather than the selected local sense.\",\"representative_source_ids\":[\"QS-d12cf8ed\",\"QI-7b3b83c7\",\"QI-f44048e4\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:1:target-in-verb-frame","source_type":"word_analysis","support_id":"sup_9cfa033cc045d0270fb8","text":"{\"blocking_evidence\":null,\"headline\":\"attached object fixes the army as target\",\"reader_payoff\":\"The reader notices that the victims are grammatically named before the stones; the attached {{ar:هِم}} ({{tr:him}}) makes the army the target and the stones the means.\",\"reason\":\"Attachment evidence marks {{ar:هِم}} ({{tr:him}}) as the direct object and {{ar:بِحِجَارَةٍ}} ({{tr:bi-ḥijāratin}}) as the bāʾ-governed instrument complement.\",\"representative_source_ids\":[\"QG-3fff3d76\",\"QG-82aad6e2\",\"QF-cb361b40\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:4:arabicized-indefinite-loanword","source_type":"word_analysis","support_id":"sup_9e363270cb85bb5fb2b4","text":"{\"blocking_evidence\":null,\"headline\":\"foreign-looking term is fully integrated grammatically\",\"reader_payoff\":\"The reader notices that the debated or foreign-looking word remains indefinite and fully declined, so its origin is open while its grammatical role is settled.\",\"reason\":\"The MASAQ evidence flags probable foreign status, while the local case and tanwīn show a governed, Arabicized noun inside the phrase.\",\"representative_source_ids\":[\"QG-cabddbad\",\"QF-56f321d5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:4:final-position-and-sound-closure","source_type":"word_analysis","support_id":"sup_a10a1bb73e68ceca75ac","text":"{\"blocking_evidence\":null,\"headline\":\"closing sound and position seal the ayah\",\"reader_payoff\":\"The reader notices that the ayah does not close on action but on the loaded final specification, whose sound and position make the source/material word the landing point.\",\"reason\":\"The word is the final term of the clause and contains the doubled consonant and long īl cadence described by the CRITICAL rows, so closure and sound claims are locally visible.\",\"representative_source_ids\":[\"QT-f237c69b\",\"QP-32d82a97\",\"QY-0ff7f3df\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:2:instrumental-projectile","source_type":"word_analysis","support_id":"sup_ba00da212aa573f0f84a","text":"{\"blocking_evidence\":null,\"headline\":\"bāʾ marks stones as projectile means\",\"reader_payoff\":\"The reader notices that the stones are the means of pelting, not a second target or loose object after the verb.\",\"reason\":\"QAC and attachment evidence both identify {{ar:بِحِجَارَةٍ}} ({{tr:bi-ḥijāratin}}) as a bāʾ-governed instrumental phrase attached to the pelting verb.\",\"representative_source_ids\":[\"QG-05ae8b68\",\"QG-364a1b51\",\"QG-96cd9871\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:2:formulaic-stone-sijjil-pair","source_type":"word_analysis","support_id":"sup_bd2dfe26f6b692cd38eb","text":"{\"blocking_evidence\":null,\"headline\":\"stone phrase joins a repeated punishment formula\",\"reader_payoff\":\"The reader notices that these stones are not an isolated image; the same stone-with-{{ar:سِجِّيلٍ}} ({{tr:sijjīlin}}) punishment formula recurs at 11:82 and 15:74.\",\"reason\":\"The contextual collocation profile names {{ar:سِجِّيلٍ}} ({{tr:sijjīlin}}) as the top partner for the stone root, and the CRITICAL rows cite the repeated phrase at 11:82 and 15:74.\",\"representative_source_ids\":[\"QI-a4e1cae4\",\"QE-02ca2ad3\",\"MI-4d1c2a9f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:3","source_type":"word_analysis","support_id":"sup_dc0b5dce8941f9343439","text":"{\"gloss_range\":\"preposition introducing the final source, kind, or material specification of the stones, with partitive source-depth possible but not forced\",\"prose\":\"{{ar:مِن}} ({{tr:min}}) is the hinge where the stones receive their final specification. It can work explicatively, making {{ar:سِجِّيلٍ}} ({{tr:sijjīlin}}) the kind or material of the stones, or inceptively, making it their source or origin; a partitive reading can add source-depth, but the local guardrail more securely supports kind/source than a fully separate mass extraction. Formally, {{ar:مِن}} ({{tr:min}}) stands as its own preposition after the fused bāʾ of {{ar:بِحِجَارَةٍ}} ({{tr:bi-ḥijāratin}}), so the ayah has two layers: instrument first, then source or material. Its doubled mīm after tanwīn makes the turn from stones to {{ar:سِجِّيلٍ}} ({{tr:sijjīlin}}) sound compressed rather than loosely appended. Because 105:4 begins without a connector, this internal preposition chain helps the ayah remain one elaboration of the sent birds while tightening action into instrument and instrument into origin or composition.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مِن}} ({{tr:min}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:3:min-material-source-polyvalence","source_type":"word_analysis","support_id":"sup_e71cd930989d1d7ff899","text":"{\"blocking_evidence\":null,\"headline\":\"particle keeps material and source readings live\",\"reader_payoff\":\"The reader notices that {{ar:مِن}} ({{tr:min}}) does more than connect two nouns; it lets the stones be read by kind/material and by source/origin at once.\",\"reason\":\"The input grammar explicitly allows explicative or inceptive {{ar:مِن}} ({{tr:min}}); the partitive rows are kept as source-depth but narrowed because the local guardrail does not force extraction from a larger mass.\",\"representative_source_ids\":[\"QG-2b033dd6\",\"QG-cf1cb97c\",\"QS-62da3906\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:4:stone-clay-and-record-tension","source_type":"word_analysis","support_id":"sup_ee6be9887692297f9795","text":"{\"blocking_evidence\":null,\"headline\":\"material clay and decree pressure remain together\",\"reader_payoff\":\"The reader notices that {{ar:سِجِّيلٍ}} ({{tr:sijjīlin}}) makes the projectiles both materially specified and textually marked, not merely geological stones.\",\"reason\":\"The local collocation with {{ar:حِجَارَةٍ}} ({{tr:ḥijāratin}}) selects the stone-clay punishment term, while the root and record/decree evidence remains valid pressure; speculative encoded-projectile language is not carried forward.\",\"representative_source_ids\":[\"QS-063a3ee0\",\"QS-22e13623\",\"MS-9785a47d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:4:min-endpoint-and-attachment","source_type":"word_analysis","support_id":"sup_f28dda40e958c6c32202","text":"{\"blocking_evidence\":null,\"headline\":\"final genitive completes source or material specification\",\"reader_payoff\":\"The reader notices that {{ar:سِجِّيلٍ}} ({{tr:sijjīlin}}) is not a loose final noun; it is the governed endpoint that determines whether the stones are classified by material or sourced from decree.\",\"reason\":\"QAC marks {{ar:سِجِّيلٍ}} ({{tr:sijjīlin}}) as genitive under {{ar:مِن}} ({{tr:min}}), and attachment evidence lets the phrase specify the kind or source of the stones.\",\"representative_source_ids\":[\"QG-47ed4fac\",\"QG-8be5cffa\",\"QG-b3b968ae\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:2","source_type":"word_analysis","support_id":"sup_f6e010fe8501ca5eb1cc","text":"{\"gloss_range\":\"indefinite broken plural stones marked by bāʾ as the projectile instrument of the pelting\",\"prose\":\"{{ar:بِحِجَارَةٍ}} ({{tr:bi-ḥijāratin}}) is not the direct object of the throwing; the bāʾ marks the stones as the hard means by which {{ar:تَرْمِيهِم}} ({{tr:tarmīhim}}) reaches its targets, while its contact value lets the same phrase register the stones as the touching surface of punishment at impact. The indefinite broken plural keeps the payload concrete but uncounted: the line names stones without making them a known inventory. The local sense is plain stone, yet the wider {{ar:ح ج ر}} ({{tr:ḥ-j-r}}) field of restraint and enclosure gives the impact a boundary-making feel, as released birds deliver objects that stop and confine the aggressors' movement. Structurally, this word is the hinge of the ayah's cascade: action becomes instrument, then the instrument is narrowed further by {{ar:مِن سِجِّيلٍ}} ({{tr:min sijjīlin}}). The pairing with {{ar:سِجِّيلٍ}} ({{tr:sijjīlin}}) also places the phrase inside the repeated punishment formula found at 11:82 and 15:74, while the paired genitive tanwīn and nasal transition keep the stone phrase and its source specification audibly bound.\",\"root_display\":\"{{ar:ح ج ر}} ({{tr:ḥ-j-r}})\",\"root_gloss_range\":\"root range includes hard stone, restraint, enclosure, protected space, and related boundary images; the local noun selects concrete stones while restraint/boundary pressure survives as impact imagery\",\"surface_display\":\"{{ar:بِحِجَارَةٍ}} ({{tr:bi-ḥijāratin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"105:4:4:poured-and-formulaic-parallels","source_type":"word_analysis","support_id":"sup_fe0b7a6ffa9966a22238","text":"{\"blocking_evidence\":null,\"headline\":\"formula recurrence adds rained-stone pressure\",\"reader_payoff\":\"The reader notices that the closing word belongs to a repeated stone-punishment phrase at 11:82 and 15:74, with poured or rained delivery pressure kept as an echo rather than the local grammar.\",\"reason\":\"The parallels at 11:82 and 15:74 support a repeated punishment formula; pouring imagery is lexical pressure from the {{ar:س ج ل}} ({{tr:s-j-l}}) family, not a replacement for the local genitive noun.\",\"representative_source_ids\":[\"QS-58891dd6\",\"QI-bac5ff65\",\"QE-0ae21ea3\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"تَرْمِيهِم بِحِجَارَةٍۢ مِّن سِجِّيلٍۢ","ayah_ref":"105:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000296/B003","root_000603/B001","root_000677/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000603","role":"Physical casting contributes directed transfer and functions as the payload's targetward trajectory.","root":"ر م ي","source_ref":"105:4","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000296","role":"Hard stone contributes discrete resistant matter and functions as the damaging payload.","root":"ح ج ر","source_ref":"105:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000677","role":"A filled bucket pouring out contributes volume and flow, functioning as the discharge pattern for many stones.","root":"س ج ل","source_ref":"105:4","source_word_indices":["4"]}],"changed_reading":{"after":"They are subjected to a directed, bucket-like outpouring of hard projectiles: a load is released, not merely a stone thrown.","before":"They are struck by stones."},"confidence":"strong","focus_anchor":"The directed verb at word 1, the plural stone payload at word 2, and the material qualifier at word 4.","mechanism":"Directed casting supplies a trajectory, hard stones supply discrete resistant units, and the filled-bucket branch supplies massed release. Focus-only, the event is therefore not a lone hit but a loaded discharge emptied onto a target.","model_id":"base_projectile_outpouring"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_projectile_outpouring","source_type":"hft","support_id":"sup_0cfb5995aa42493eee81","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"تَرْمِيهِم بِحِجَارَةٍۢ مِّن سِجِّيلٍۢ","ayah_ref":"105:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000296/B003","root_000603/B004","root_000677/B001"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000603","role":"Cloud or heavy rain contributes precipitation imagery and functions as an atmospheric model for the casting.","root":"ر م ي","source_ref":"105:4","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000296","role":"Hard stone contributes the actual particulate matter and prevents the rain model from becoming merely watery.","root":"ح ج ر","source_ref":"105:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000677","role":"Bucketful outpouring contributes a dense downward flow and functions as the precipitation's release pattern.","root":"س ج ل","source_ref":"105:4","source_word_indices":["4"]}],"changed_reading":{"after":"The wording also supports lithic precipitation: a cloudlike cast whose poured drops are hard stones.","before":"Separate agents throw separate stones in an ordinary ballistic scene."},"confidence":"medium","focus_anchor":"The same casting verb at word 1 can activate its cloud-and-rain branch while words 2 and 4 specify hard matter and outpouring.","mechanism":"The cloud/rain branch of casting changes the delivery morphology, the stone branch changes the droplets into hard particles, and the outpouring branch gives the fall density. This coexists with ordinary projectile delivery as a stone-rain image.","model_id":"base_lithic_precipitation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_lithic_precipitation","source_type":"hft","support_id":"sup_e12af88c6d6fb2856c10","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"تَرْمِيهِم بِحِجَارَةٍۢ مِّن سِجِّيلٍۢ","ayah_ref":"105:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000296/B001","root_000296/B003","root_000603/B008","root_000677/B004"],"payload":{"activation_trace":[{"branch_id":"B008","mapped_root_id":"root_000603","role":"Casting an accusation contributes imposed charge and functions as the event's juridical-speech layer.","root":"ر م ي","source_ref":"105:4","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000296","role":"Enclosure and prohibition contribute binding restraint and function as the charge's enforceable effect.","root":"ح ج ر","source_ref":"105:4","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000296","role":"Hard stone contributes literal material impact and keeps the record model anchored in the physical event.","root":"ح ج ر","source_ref":"105:4","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_000677","role":"A record that gathers and secures contributes fixation and functions as the lasting registration of each impact.","root":"س ج ل","source_ref":"105:4","source_word_indices":["4"]}],"changed_reading":{"after":"Each impact can also be heard as a materially enforced entry—charge, restraint, and record—without ceasing to be a stone.","before":"The stones are only unnamed ammunition."},"confidence":"exploratory","focus_anchor":"Word 1 can carry accusatory casting, word 2 can carry both hard matter and restraint, and word 4 can carry a secured record.","mechanism":"Accusatory casting supplies a charge, enclosure/prohibition supplies binding restraint, and the secured-record branch supplies fixation; the hard-stone branch keeps the chain material. The impacts can thus coexist as executable entries rather than becoming a purely abstract allegory.","model_id":"base_executable_record"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_executable_record","source_type":"hft","support_id":"sup_092334f1b90a87fb6510","trust":"legacy_unbound"}]}
</lane_packet_json>
