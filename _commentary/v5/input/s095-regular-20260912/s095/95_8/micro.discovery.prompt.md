# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **95:8**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s095-regular-20260912/s095/95_8/micro.discovery.json` and modify nothing
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
  "ayah_ref": "95:8",
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
{"branch_registry":[{"boundary":"Dal, tapınma eylemi ile bundan türeyen tapınılan veya tapınılır kılınan varlık anlamlarını kapsar; şaşkınlık, yoğun üzüntü ve salt özel ad kullanımları bu sınırın dışındadır.","branch_kind":"mixed_non_bare","branch_ref":"root_000047/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|NOM","morpheme_role":"STEM","pos":"PN","qac_ref":"95:8:2:1","qac_word_ref":"95:8:2","surface_ar":"ٱللَّهُ"}],"gloss":"tapınma ve tapınılan varlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel eylem, bir varlığa tapınmak ve kişinin kendini bu tapınmaya vermesidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylemden türeyen varlık anlamı, kendisine tapınılan varlığı veya tapınma konusu sayılan nesneyi gösterir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen kullanım, bir varlığı başkalarınca tapınılır duruma getirme veya öyle sunma işlemini bildirir."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Güneşe kimi topluluklarca tapınılması nedeniyle ona tapınılan varlık anlamındaki bir ad verilmesi, varlık anlamının tarihsel bir örneğidir."}}],"root_ar":"ء ل ه","root_id":"root_000047","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eylem çekirdeğiyle ondan türeyen tapınılan varlık anlamının birlikte temsil edilmesi gereken genel açıklamalarda kullanılır.","boundary_detail":"Dal, tapınma eylemi ile bundan türeyen tapınılan veya tapınılır kılınan varlık anlamlarını kapsar; şaşkınlık, yoğun üzüntü ve salt özel ad kullanımları bu sınırın dışındadır.","branch_image_ar":"التعبد والمعبود","concept_gloss":"tapınma ve tapınılan varlık","contextual_glosses":[{"applicability":"Bir kişinin tapınma eylemini veya kendini tapınmaya vermesini bildiren eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylem olarak tapınma çekirdeğini eksiksiz korur."},"facet_ids":["F001"],"text":"tapınmak","usage_role":"general"},{"applicability":"Bir topluluğun kendisine tapındığı varlık veya nesneden söz edilen ad bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tapınmanın yöneldiği varlık veya nesne anlamını korur."},"facet_ids":["F002"],"text":"tapınılan varlık","usage_role":"contextual"},{"applicability":"Bir varlığın başkalarına tapınma konusu olarak benimsetilmesini anlatan ettirgen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir varlığı tapınma konusu durumuna getirme işlemini korur."},"facet_ids":["F003"],"text":"tapınılır kılmak","usage_role":"explanatory"}],"definition":"Bir varlığa tapınma eylemini ve kişinin kendini tapınmaya vermesini anlatır. Türemiş kullanımlarda bir varlığı tapınılır kılmayı, tapınılan varlığı ve tapınma konusu sayılan varlıkları da adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel eylem, bir varlığa tapınmak ve kişinin kendini bu tapınmaya vermesidir."},{"facet_id":"F002","role":"extension","statement":"Eylemden türeyen varlık anlamı, kendisine tapınılan varlığı veya tapınma konusu sayılan nesneyi gösterir."},{"facet_id":"F003","role":"specialization","statement":"Ettirgen kullanım, bir varlığı başkalarınca tapınılır duruma getirme veya öyle sunma işlemini bildirir."},{"facet_id":"F004","role":"example","statement":"Güneşe kimi topluluklarca tapınılması nedeniyle ona tapınılan varlık anlamındaki bir ad verilmesi, varlık anlamının tarihsel bir örneğidir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Yalnızca belirli bir varlık türünü adlandırdığı için bütün dalın karşılığı sanılabilir.","fit":"narrowing","loses":"Tapınma eylemini, kişinin tapınmaya yönelmesini ve tapınılır kılma işlemini karşılamaz.","preserves":"Tapınılan varlık anlamını kısa ve doğal biçimde korur."},"text":"tanrı"}],"identity_rationale":"Kaynak ifadesi tapınma eylemini, kişinin kendini tapınmaya vermesini, bir varlığı tapınılır kılmayı ve tapınılan varlığı aynı anlam örgüsü içinde açıkça birleştirir. Geçici dal çerçevesi bu çekirdeği ve ondan türeyen varlık adlarını doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tapınmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kendini tapınmaya vermek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"tapınılır kılmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"tapınılan varlık, tanrı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"tapınılan varlık"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"tanrılar, tapınılan nesneler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"tapınma"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kimi toplulukların tapındığı için bu adla anılan güneş"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"senin tapınman"}],"lexicalization_note":"Tanım, yalın eylem çekirdeğini türemiş eylem ve varlık adlarından ayırır; türemiş biçimlerin kapsamı yalın eylemin tamamına aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Tapınma eylemi, korkuya bağlı özel tapınma yaşayışı ve aynı kökün özel ad dalı sınırı keskinleştirdi; peygamberlik, büyücülük, belirli tapınma nesneleri, sahiplik ve tarihsel hizmet grubu adayları ise yalnızca aynı dinsel alana veya tekil örneklere temas ettiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal eylem ve yaklaşma yönünde yoğunlaşırken bu dal aynı çekirdekten tapınılan varlık ile ettirgen kılma anlamlarını da türetir; bu yüzden yalnızca eylem bağlamında yakınlaşırlar.","focus_only":"Tapınılan varlığı ve bir varlığı tapınılır kılma işlemini de adlandırır.","gloss":"tapınma ve yaklaşarak yönelme","neighbor_only":"Tapınmayla birlikte yaklaşma ve kendini bu işe verme yönünü öne çıkarır.","neighbor_ref":"root_001498/B001","relation_type":"near_synonym","shared_zone":"İki dal da tapınma eylemini ve kişinin bu eyleme yönelmesini kapsar."},{"boundary_match":"partial","distinction":"Bu dal genel tapınma çekirdeğini ve ondan türeyen varlık anlamlarını kapsar; komşu dal ise korku, inziva ve olağanın üstündeki uygulamalarla sınırlı özel bir yaşayışı anlatır.","focus_only":"Tapınmayı korku, inziva veya aşırı uygulama koşuluna bağlamaz ve tapınılan varlığı da adlandırabilir.","gloss":"korkuyla yoğunlaşan özel tapınma yaşayışı","neighbor_only":"Korkudan doğan, inziva veya ek yüklenme biçimindeki özel bir tapınma yaşayışını bildirir.","neighbor_ref":"root_000604/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da kişinin kendini tapınmaya vermesi bulunur."},{"boundary_match":"partial","distinction":"Bu dal genel anlam örgüsünü verir; komşu dal ise o örgüden türemiş özel adı ve adın belirli söz kalıplarındaki kullanımını ayrı bir biçim alanı olarak sınırlar.","focus_only":"Genel tapınma eylemini, tapınılan varlığı ve tapınılır kılmayı kapsar.","gloss":"Yaratıcıya özgü ad ve kullanım kalıpları","neighbor_only":"Yaratıcıya özgü adı ve bu adla kurulan seslenme, dilek ve ant kalıplarını kapsar.","neighbor_ref":"root_000047/B002","relation_type":"near_neighbor","shared_zone":"Özel ad, tapınılan yüce varlık düşüncesi üzerinden bu dalın varlık anlamıyla bağlantılıdır."}],"source_phrase_ar":"أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)","source_summary":"Kaynakların ortak çizgisi, tapınmayı anlamın temeli sayar; kişinin tapınmaya yönelmesini, tapınılan varlığı ve tapınılır kılma işlemini bu temelden türetir. Tapınma konusu sayılan yontular ve güneş örneği, varlık anlamının belirli uygulamalarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه أله وتأله بمعنى عبد وتنسك، والتأليه بمعنى التعبيد، والإله والآلهة والإلاهة لما جعل معبودا.","what_is_not_ar":"لا يدخل فيه أله بمعنى تحير، ولا ألهت على فلان بمعنى اشتد جزعي عليه، ولا أسماء المواضع أو الحية أو الهلال إلا من جهة التسمية لا معنى العبادة."},"support_links":[]},{"boundary":"Dal, özel ad ile bu ada bağlı seslenme, dilek, şaşma ve ant biçimleriyle sınırlıdır; herhangi bir tapınılan varlığı gösteren genel ad anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000047/B002","candidate_links":[{"candidate_id":"cand_5f7ec71ec2a78a45509d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|NOM","morpheme_role":"STEM","pos":"PN","qac_ref":"95:8:2:1","qac_word_ref":"95:8:2","surface_ar":"ٱللَّهُ"}],"gloss":"Yaratıcıya özgü ad ile seslenme ve ant biçimleri","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dalın merkezinde, Yaratıcıyı başkalarından ayırarak gösteren ve yalnız ona özgü sayılan özel ad bulunur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Özel adın, tapınılan varlığı bildiren genel addan ses düşmesi ve belirleyici unsur eklenmesiyle oluştuğu açıklanır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özel ad, sözün başında ant değeri taşıyarak ardından gelen yapmama bildirimini güçlendirebilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Özel adın doğrudan ya da seslenme öğesi yerine geçen bir sonla kullanılması, yakarma ve dilek bildiren seslenme biçimleri kurar."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Ses veya parçaların düşürüldüğü kısalmış biçimler, şaşma ve ant anlatan kalıplarda kullanılır."}}],"root_ar":"ء ل ه","root_id":"root_000047","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özel adın kendisiyle ona bağlı seslenme, dilek ve ant kullanımlarının birlikte açıklanması gereken dal düzeyinde kullanılır.","boundary_detail":"Dal, özel ad ile bu ada bağlı seslenme, dilek, şaşma ve ant biçimleriyle sınırlıdır; herhangi bir tapınılan varlığı gösteren genel ad anlamına genişletilmez.","branch_image_ar":"اسم الله في القسم والنداء","concept_gloss":"Yaratıcıya özgü ad ile seslenme ve ant biçimleri","contextual_glosses":[{"applicability":"Söz konusu adın yalnız Yaratıcıyı gösteren yalın ad olarak ele alındığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adın Yaratıcıya özgü olmasını ve ayırt edici ad işlevini korur."},"facet_ids":["F001"],"text":"Yaratıcı'nın özel adı","usage_role":"general"},{"applicability":"Yakarış veya dilek sırasında Yaratıcıya doğrudan seslenilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaratıcıya yöneltilen doğrudan seslenme işlevini doğal biçimde korur."},"facet_ids":["F004"],"text":"ey Tanrı","usage_role":"contextual"},{"applicability":"Özel adın bir bildirimin doğruluğunu pekiştiren ant değeri taşıdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaratıcıya dayanarak ant verme işlevini açık biçimde korur."},"facet_ids":["F003"],"text":"Tanrı adına ant olsun","usage_role":"contextual"},{"applicability":"Özel adın ses veya parçaları düşürülmüş tarihsel kalıplarının işlevini açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kısaltılma biçimini ve şaşma ya da ant işlevini birlikte korur."},"facet_ids":["F005"],"text":"kısaltılmış şaşma veya ant sözü","usage_role":"explanatory"}],"definition":"Yaratıcıya özgü adın kendisini ve bu adla kurulan seslenme, dilek, şaşma ve ant biçimlerini kapsar. Bu biçimler doğrudan seslenme, adın ant değeriyle kullanılması veya ses ve parçaların düşürülmesiyle kısaltılma yollarını gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dalın merkezinde, Yaratıcıyı başkalarından ayırarak gösteren ve yalnız ona özgü sayılan özel ad bulunur."},{"facet_id":"F002","role":"source_variant","statement":"Özel adın, tapınılan varlığı bildiren genel addan ses düşmesi ve belirleyici unsur eklenmesiyle oluştuğu açıklanır."},{"facet_id":"F003","role":"associated_use","statement":"Özel ad, sözün başında ant değeri taşıyarak ardından gelen yapmama bildirimini güçlendirebilir."},{"facet_id":"F004","role":"associated_use","statement":"Özel adın doğrudan ya da seslenme öğesi yerine geçen bir sonla kullanılması, yakarma ve dilek bildiren seslenme biçimleri kurar."},{"facet_id":"F005","role":"source_variant","statement":"Ses veya parçaların düşürüldüğü kısalmış biçimler, şaşma ve ant anlatan kalıplarda kullanılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Genel tür adı olarak başka tapınılan varlıklar için de kullanılabildiğinden özel adla karışır.","fit":"narrowing","loses":"Adın tek bir varlığa özgü özel ad oluşunu ve seslenme ile ant biçimlerini karşılamaz.","preserves":"Yüce bir tapınılan varlığa gönderimde bulunma yönünü korur."},"text":"tanrı"}],"identity_rationale":"Kaynak ifadesi Yaratıcıya özgü adın kendisini, genel tapınılan-varlık adından türetiliş açıklamasını ve bu özel adla kurulan seslenme ile ant biçimlerini birlikte verir. Geçici çerçeve kullanılabilir, ancak dal yalnızca seslenme ve ant kalıpları değildir; özel adın yalın kullanımı da çekirdekte tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"Yaratıcıya özgü ad"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"Tanrı adına ant olsun, bunu yapmadım"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ey Tanrı; yakarma seslenişi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ey Tanrı; doğrudan seslenme"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"Tanrı adına sen veya baban; şaşma ya da ant kalıbı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları"}],"lexicalization_note":"Yalın özel ad, doğrudan seslenme biçimleri ve ant ya da şaşma kalıpları ayrı tutulur; kalıplara özgü işlevler özel adın her kullanımına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Genel tapınma dalı, yaşam üzerine ant, genel seslenme, kısaltılmış kişi seslenmesi ve yakarışa karşılık sözü gerçek sınır karşılaştırmaları sağladı; baba hitapları, genel dışlama yapıları, başka ant sözleri ve sesçe eşlik eden kalıplar daha zayıf ya da yalnızca biçimsel temas gösterdiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli bir özel adın biçim ve kullanım alanıdır; komşu dal ise özel adla sınırlanmayan genel tapınma eylemini ve tapınılan varlık anlamını verir.","focus_only":"Yaratıcıya özgü adı ve bu adla kurulan seslenme, dilek, şaşma ve ant biçimlerini kapsar.","gloss":"tapınma ve tapınılan varlık","neighbor_only":"Genel tapınma eylemini, tapınılan varlığı ve bir varlığı tapınılır kılma işlemini kapsar.","neighbor_ref":"root_000047/B001","relation_type":"near_neighbor","shared_zone":"Özel ad, tapınılan yüce varlığı göstermesi bakımından genel varlık anlamına dayanır."},{"boundary_match":"partial","distinction":"Ortak işlev ant vermedir, fakat bu dalın dayanağı Yaratıcıya özgü addır; komşu dal yaşam süresini bildiren sözleri kullanır ve ayrıca ısrarlı istemeye uzanabilir.","focus_only":"Ant işlevini Yaratıcıya özgü adın yalın veya kısalmış biçimleriyle kurar.","gloss":"ömür üzerine ant ve ısrarlı isteme","neighbor_only":"Ant veya ısrarlı isteme işlevini yaşam süresini bildiren sözlerle kurar.","neighbor_ref":"root_001044/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir sözü güçlendiren ant işlevli kalıplar içerir."},{"boundary_match":"field_only","distinction":"Bu dal belirli bir muhatabın özel adı çevresinde oluşur; komşu dal ise muhatabın kimliğinden bağımsız genel seslenme araçlarını ve uzaklık ayrımını konu edinir.","focus_only":"Belirli bir özel adı ve o adın yakarma ile ant kullanımlarını içerir.","gloss":"genel seslenme öğeleri","neighbor_only":"Yakın veya uzaktaki muhataba yöneltilen genel seslenme öğelerini bildirir.","neighbor_ref":"root_000074/B008","relation_type":"same_field","shared_zone":"Her iki dal da doğrudan seslenme sırasında kullanılan biçimlerle ilgilidir."},{"boundary_match":"field_only","distinction":"Bu dalın kısalmaları belirli özel adın dinsel seslenme ve ant işlevlerine bağlıdır; komşu dalın kısalmaları ise belirsiz bir kişiye seslenmenin dilbilgisel biçimleridir.","focus_only":"Yaratıcıya özgü adı ve ona bağlı seslenme ile ant biçimlerini kapsar.","gloss":"kişiye yönelik kısaltılmış seslenme","neighbor_only":"Belirsiz bir kişiye yönelen kısaltılmış seslenme biçimlerini kapsar.","neighbor_ref":"root_001178/B003","relation_type":"same_field","shared_zone":"Her iki dalda da seslenme sırasında biçimsel kısalma görülebilir."},{"boundary_match":"thematic_only","distinction":"Bu dal bir muhataba seslenir; komşu dal ise söylenmiş yakarışa kabul dileği veya onayla karşılık verir. Aynı sahnede bulunsalar da anlam çekirdekleri örtüşmez.","focus_only":"Yakarışın yöneltildiği Yaratıcıyı özel adıyla çağırır.","gloss":"yakarışın kabulünü isteyen karşılık","neighbor_only":"Yakarışın kabul edilmesini isteyen veya söyleneni onaylayan karşılık sözünü bildirir.","neighbor_ref":"root_000054/B003","relation_type":"thematic","shared_zone":"İki dal da yakarış ortamında kullanılan kısa söz biçimlerine katılır."}],"source_phrase_ar":"فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)","source_summary":"Kaynaklar özel adı Yaratıcıya özgü bir ad olarak tanımlar ve onu tapınılan varlığı gösteren genel adla köken bakımından ilişkilendirir. Aynı adın doğrudan seslenmede, yakarmada, ant bildiriminde ve parçaları düşürülmüş kalıplarda kullanıldığı birlikte gösterilir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اسم الله والقول في أصله من إله، وصيغ الاستعمال مثل الله ما فعلت بمعنى والله، واللهم، ويا الله، ولاه أبوك أو لاه أنت ونحوها.","what_is_not_ar":"ليس فرعا مستقلا عن معنى الإله المعبود من جهة الاشتقاق، ولا يدخل فيه إطلاق إله أو آلهة على كل معبود إذا لم يكن الكلام على صيغة الاسم أو النداء أو القسم."},"support_links":["sup_9591c7e41a55ecca2efb"]},{"boundary":"Alan, yargıda bulunmayı veya bir şeyi sağlamlaştırmayı değil, engelleyip geri çevirmeyi kapsar; düzeltme bu işlemin belirgin bir amacıdır ama her kullanımı sınırlandırmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000348/B001","candidate_links":[{"candidate_id":"cand_5d5b596d8050b161ed4a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحْكَم","morph_features":"STEM|POS:N|LEM:>aHokam|ROOT:Hkm|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:8:3:2","qac_word_ref":"95:8:3","surface_ar":"أَحْكَمِ"},{"lemma_ar":"حَٰكِمِين","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ha`kimiyn|ROOT:Hkm|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:8:4:2","qac_word_ref":"95:8:4","surface_ar":"حَٰكِمِينَ"}],"gloss":"alıkoyup geri çevirmek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel işlem, birini istediği veya yöneldiği şeyden ya da bir şeyi bozulmadan alıkoyup geri çevirmektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Savurgan ya da sorumsuz kişinin elini tutmak, onun zarar verici girişimini durdurmanın özel bir örneğidir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Koruma altındaki birini bozulmadan uzak tutmak, yalnız engellemeyi değil onun durumunu düzeltme amacını da içerir."}}],"root_ar":"ح ك م","root_id":"root_000348","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel engelleme ve geri çevirme işlemini kısa biçimde karşılar; düzeltici kullanımlar kavram haritasındaki özelleşmelerle açıklanır.","boundary_detail":"Alan, yargıda bulunmayı veya bir şeyi sağlamlaştırmayı değil, engelleyip geri çevirmeyi kapsar; düzeltme bu işlemin belirgin bir amacıdır ama her kullanımı sınırlandırmaz.","branch_image_ar":"المنع والرد للإصلاح","concept_gloss":"alıkoyup geri çevirmek","contextual_glosses":[{"applicability":"Bir kişinin zararlı veya sorumsuz bir davranışa girişmesini fiilen önleme bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan dışındaki şeylerin bozulmasını önleme kapsamını dışarıda bırakır.","preserves":"Kişiyi zararlı davranıştan engelleme yönünü korur."},"facet_ids":["F001","F002"],"text":"elini tutup yanlışından alıkoymak","usage_role":"contextual"},{"applicability":"Koruma altındaki bir kişiyi bozulmadan uzak tutma ve durumunu düzeltme bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel engelleme ve geri çevirme işleminin bütün kullanım alanlarını kapsamaz.","preserves":"Koruma ve düzeltme amacını açık biçimde korur."},"facet_ids":["F001","F003"],"text":"koruyup doğru yola yöneltmek","usage_role":"contextual"}],"definition":"Birini istediği veya yöneldiği şeyden, bir şeyi de bozulmadan alıkoyup geri çevirmektir; bu işlem özellikle haksızlığı ya da bozulmayı önleme ve düzeltme amacıyla kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel işlem, birini istediği veya yöneldiği şeyden ya da bir şeyi bozulmadan alıkoyup geri çevirmektir."},{"facet_id":"F002","role":"specialization","statement":"Savurgan ya da sorumsuz kişinin elini tutmak, onun zarar verici girişimini durdurmanın özel bir örneğidir."},{"facet_id":"F003","role":"specialization","statement":"Koruma altındaki birini bozulmadan uzak tutmak, yalnız engellemeyi değil onun durumunu düzeltme amacını da içerir."}],"identity_rationale":"Kaynak anlatımlarının ortak işlemi, birini ya da bir şeyi yöneldiği veya istediği şeyden alıkoyup geri çevirmektir. Haksızlığı ve bozulmayı önleme ile düzeltme amacı bu işlemin güçlü bir gerekçesidir, ancak bütün tanıklıklarda zorunlu koşul olarak belirtilmez.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"haksızlıktan veya bozulmadan alıkoyup geri çevirmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"sorumsuz kişinin elini tutup zarar vermesini önlemek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yetimi bozulmadan koruyup durumunu düzeltmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"birini yapmak istediği şeyden alıkoymak"}],"lexicalization_note":"Tanım ortak engelleme çekirdeğini korur; kişi, savurgan ve yetimle kurulan özel yapılar bu çekirdeğin ayrı gerçekleşmeleridir.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yayımlanan üç ilişki, düzeltici engellemenin genel önleme, tutma ve yargılama karşısındaki sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda haksızlığı veya bozulmayı önleme ve kişiyi istediği şeyden alıkoyma kullanımları öne çıkar; komşu dal kişinin kendini tutmasına ve gözyaşını bastırmaya da uzanır.","focus_only":"Engellemenin öne çıkan kullanımları haksızlığı veya bozulmayı önlemeye yönelir; dal ayrıca kişiyi istediği şeyden alıkoymayı da kapsar.","gloss":"alıkoyma ve önleme","neighbor_only":"Komşu dal kişinin kendini tutmasını ve gözyaşını bastırma gibi daha geniş kullanımları da kapsar.","neighbor_ref":"root_001308/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir eylemin sürmesini önleme ve bir şeyi geri tutma vardır."},{"boundary_match":"partial","distinction":"Komşu dal fiziksel tutma ve yoksun bırakma sonucuna daha geniş yer verir; odak dalda haksızlığı ya da bozulmayı önleme ve kişiyi istediğinden alıkoyma kullanımları öne çıkar.","focus_only":"Durdurma işleminin öne çıkan kullanımları haksızlığı ve bozulmayı önlemeye yönelir; dal ayrıca kişiyi istediği şeyden alıkoymayı da kapsar.","gloss":"tutup geri çevirmek","neighbor_only":"Komşu dal tutma, hapsetme, geri çevirme ve iyilikten yoksun bırakılma sonuçlarını birlikte kapsar.","neighbor_ref":"root_000193/B003","relation_type":"near_synonym","shared_zone":"İki dal da birini veya bir şeyi ilerlemekten ya da bir işe girişmekten alıkoyabilir."},{"boundary_match":"field_only","distinction":"Birincisi engelleme eylemini, ikincisi ise uyuşmazlığı karara bağlama eylemini temel alır; aynı bağlamda görülebilseler de birbirinin yerine geçmezler.","focus_only":"Odak dal birini ya da bir şeyi engelleyip geri çevirir; haksızlığı veya bozulmayı önleme bunun belirgin kullanımlarındandır.","gloss":"engelleme ile yargılama","neighbor_only":"Komşu dal taraflar veya bir önerme hakkında bağlayıcı karar verir.","neighbor_ref":"root_000348/B002","relation_type":"same_field","shared_zone":"İki dal haksızlığı önleme düşüncesinde ve insanlar arasındaki düzen alanında buluşur."}],"source_phrase_ar":"الحكم وهو المنع من الظلم (maqayis)؛ كل شيء منعته من الفساد فقد حكمته وحكمته وأحكمته (ayn)؛ حكمت السفيه وأحكمته إذا أخذت على يده (sihah)؛ كل من منعته من شيء فقد حكمته وأحكمته (tahdhib)؛ حكم أصله منع منعا لإصلاح (mufradat)","source_summary":"Kaynak anlatımları alıkoyma ve geri çevirme işleminde birleşir; haksızlığı veya bozulmayı önleme ile düzeltme amacı bu anlatımlardaki belirgin vurgulardır, ancak her tanıklığın zorunlu sınırı değildir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"منع الظلم والفساد؛ رد السفيه أو منعه؛ كف المرء عما يريد","what_is_not_ar":"القضاء بمجرده؛ الحكمة العلمية؛ إحكام الشيء وإتقانه؛ حكمة اللجام اسما للآلة"},"support_links":["sup_894381612f755e3fff01"]},{"boundary":"Dalın çekirdeği uyuşmazlığı veya bir savı karara bağlamaktır; özel bedel hesapları ve salt yetki devri çekirdeğe katılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000348/B002","candidate_links":[{"candidate_id":"cand_5f7ec71ec2a78a45509d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحْكَم","morph_features":"STEM|POS:N|LEM:>aHokam|ROOT:Hkm|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:8:3:2","qac_word_ref":"95:8:3","surface_ar":"أَحْكَمِ"},{"lemma_ar":"حَٰكِمِين","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ha`kimiyn|ROOT:Hkm|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:8:4:2","qac_word_ref":"95:8:4","surface_ar":"حَٰكِمِينَ"}],"gloss":"uyuşmazlığı bağlayıcı kararla sonuçlandırmak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel işlem, insanlar arasındaki uyuşmazlığı bağlayıcı bir kararla sona erdirmektir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karar verme, bir durumun belirli biçimde olduğunu ya da olmadığını saptamaya da uzanır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tarafların yetkili bir karar merciine başvurması, kararın kendisi değil bu sürece giriş eylemidir."}}],"root_ar":"ح ك م","root_id":"root_000348","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsanlar arasındaki karar verme çekirdeğini doğal biçimde karşılar ve salt engellemeden ayrılır.","boundary_detail":"Dalın çekirdeği uyuşmazlığı veya bir savı karara bağlamaktır; özel bedel hesapları ve salt yetki devri çekirdeğe katılmaz.","branch_image_ar":"الحكم والقضاء بين الناس","concept_gloss":"uyuşmazlığı bağlayıcı kararla sonuçlandırmak","contextual_glosses":[{"applicability":"İki ya da daha çok taraf arasındaki çekişmenin karara bağlandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir savın doğru olup olmadığını belirleme uzantısını kapsamaz.","preserves":"Taraflar arasında karar verme işlemini korur."},"facet_ids":["F001"],"text":"taraflar arasında karar vermek","usage_role":"general"},{"applicability":"Bir nesne, olay veya sav hakkında olumlu ya da olumsuz belirleme yapıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsanlar arasındaki uyuşmazlığı sonuçlandırma çekirdeğini dışarıda bırakır.","preserves":"Bir durumun öyle olup olmadığını karara bağlama yönünü korur."},"facet_ids":["F002"],"text":"öyle olduğuna karar vermek","usage_role":"contextual"}],"definition":"İnsanlar arasındaki bir uyuşmazlığı doğru ölçüye göre bağlayıcı bir kararla sonuçlandırmak veya bir şeyin öyle olup olmadığına karar vermektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel işlem, insanlar arasındaki uyuşmazlığı bağlayıcı bir kararla sona erdirmektir."},{"facet_id":"F002","role":"extension","statement":"Karar verme, bir durumun belirli biçimde olduğunu ya da olmadığını saptamaya da uzanır."},{"facet_id":"F003","role":"associated_use","statement":"Tarafların yetkili bir karar merciine başvurması, kararın kendisi değil bu sürece giriş eylemidir."}],"identity_rationale":"Kaynak anlatımı, insanlar arasında karar vermeyi ve bir şeyin öyle olup olmadığına karar bağlamayı açıkça destekler. Yaralanma bedelini hesaplama gibi özel uygulamalar ayrı sözcük birimlerinde görülür; bunlar dalın genel çekirdeği değil, yargısal karar vermenin özel kullanımlarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"insanlar arasında doğru ölçüyle karar vermek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"biri lehine veya aleyhine karar vermek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"karar verme veya işi karara bağlama"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"insanlar arasında karar veren kişi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"karar verme işiyle özellikle görevli kişi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"çekişmede verilen karar veya yaralanma karşılığını belirleme"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"çekişmeyi karar verecek bir mercie götürmek"}],"lexicalization_note":"Tanım karar verme çekirdeğini verir; kişiler arasında karar verme, biri lehine karar verme ve bir karar merciine başvurma yapıları ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen ilişkiler karar verme çekirdeğini yakın karar dallarından ve yetki devrinden ayıran en yararlı karşılaştırmalardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekler büyük ölçüde örtüşür; odak dal belirleme anlamına uzanırken komşu dal ayırıp sonuca bağlama yönünü daha belirgin taşır.","focus_only":"Odak dal, bir durumun öyle olup olmadığını belirleme kullanımını da taşır.","gloss":"uyuşmazlığı karara bağlamak","neighbor_only":"Komşu dal, doğru ile yanlışı keskin biçimde ayırma ve son sözü söyleme görüntüsünü öne çıkarır.","neighbor_ref":"root_001159/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da çekişen taraflar arasında ayırıcı ve sonuçlandırıcı karar vermeyi kapsar."},{"boundary_match":"partial","distinction":"Odak dalın önerme hakkında karar verme uzantısı daha geniştir; komşu dal ise açıp ayırarak çözme görüntüsüne ve karar vericiye bağlıdır.","focus_only":"Odak dal kararın içeriğini ve bir sav hakkında belirleme yapmayı birlikte kapsar.","gloss":"taraflar arasında karar vermek","neighbor_only":"Komşu dal, uyuşmazlığı açıp çözerek kapatan karar verici kişiyi de adlandırır.","neighbor_ref":"root_001124/B003","relation_type":"near_synonym","shared_zone":"İki dalın merkezinde çekişen taraflar arasında karar vererek uyuşmazlığı bitirmek bulunur."},{"boundary_match":"field_only","distinction":"Karar verme eylemi ile o eylemi yapma yetkisinin başkasına bırakılması farklı aşamalardır; biri diğerini gerektirebilir ama tanımlamaz.","focus_only":"Odak dal bağlayıcı kararın verilmesini anlatır.","gloss":"karar ile yetki devri","neighbor_only":"Komşu dal karar verme yetkisinin bir kişiye bırakılmasını anlatır.","neighbor_ref":"root_000348/B005","relation_type":"same_field","shared_zone":"Her iki dalda da bir kişi karar verme görevini üstlenebilir ve taraflar bu karara bağlanabilir."}],"source_phrase_ar":"الحكم وهو المنع من الظلم (maqayis)؛ حاكمناه إلى الله دعوناه إلى حكم الله (ayn)؛ الحكم مصدر قولك حكم بينهم أي قضى (sihah)؛ الحكم أيضا القضاء بالعدل (tahdhib)؛ الحكم بالشيء أن تقضي بأنه كذا أو ليس بكذا (mufradat)","source_summary":"Kaynaklar, insanlar arasında karar vermeyi, haksızlığı önleyen bir sonuç üretmeyi ve bir durumun öyle olup olmadığını karara bağlamayı ortaklaştırır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"القضاء بالعدل؛ الحكم بين الناس؛ الحكومة والتحاكم والمحاكمة؛ تقدير الأرش في الجراحات","what_is_not_ar":"المنع العام؛ الحكمة بمعنى العلم؛ تفويض التصرف في المال بلا خصومة"},"support_links":["sup_9591c7e41a55ecca2efb"]},{"boundary":"Dal, bilgi ve usla doğruyu bulma yetkinliğidir; yargısal karar, salt öğrenilmiş bilgi veya yalnızca işçilik ustalığı değildir.","branch_kind":"bare","branch_ref":"root_000348/B003","candidate_links":[{"candidate_id":"cand_1bd3cf21390948048637","lane":"micro"},{"candidate_id":"cand_aaa916deb478185bf2df","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحْكَم","morph_features":"STEM|POS:N|LEM:>aHokam|ROOT:Hkm|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:8:3:2","qac_word_ref":"95:8:3","surface_ar":"أَحْكَمِ"},{"lemma_ar":"حَٰكِمِين","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ha`kimiyn|ROOT:Hkm|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:8:4:2","qac_word_ref":"95:8:4","surface_ar":"حَٰكِمِينَ"}],"gloss":"bilgi ve usla doğruyu bulma yetkinliği","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bilgi ve us, kişinin doğruyu yanlıştan ayırıp doğru olana ulaşmasını sağlar."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu yetkinlikte bilgiye ölçülülük ve ağırbaşlılık eşlik eder."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu yetkinliğe sahip kişi bilgili, deneyimli ve yerinde davranan biri olarak nitelenir."}}],"root_ar":"ح ك م","root_id":"root_000348","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bilgi, us, ölçülülük ve doğruya ulaşma bileşenlerini tek bir doğal açıklamada birleştirir.","boundary_detail":"Dal, bilgi ve usla doğruyu bulma yetkinliğidir; yargısal karar, salt öğrenilmiş bilgi veya yalnızca işçilik ustalığı değildir.","branch_image_ar":"الحكمة والعلم المصيب","concept_gloss":"bilgi ve usla doğruyu bulma yetkinliği","contextual_glosses":[{"applicability":"Bilgi, deneyim, ölçülülük ve doğru davranışı birlikte düşündüren genel bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilgi, deneyim, ölçülülük ve doğruyu bulma yetkinliğini birlikte korur."},"facet_ids":["F001","F002","F003"],"text":"bilgelik","usage_role":"general"},{"applicability":"Bu yetkinliği taşıyan kişinin bilgisi ve yerinde kavrayışı vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ölçülülük ve iyi davranış boyutunu açıkça taşımaz.","preserves":"Kişinin bilgili oluşunu ve doğruya ulaşma yetisini korur."},"facet_ids":["F001","F003"],"text":"doğruyu gören bilgili kişi","usage_role":"contextual"}],"definition":"Bilgi, us ve ağırbaşlılık sayesinde doğruyu yerinde bulma yetkinliğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bilgi ve us, kişinin doğruyu yanlıştan ayırıp doğru olana ulaşmasını sağlar."},{"facet_id":"F002","role":"core","statement":"Bu yetkinlikte bilgiye ölçülülük ve ağırbaşlılık eşlik eder."},{"facet_id":"F003","role":"associated_use","statement":"Bu yetkinliğe sahip kişi bilgili, deneyimli ve yerinde davranan biri olarak nitelenir."}],"identity_rationale":"Kaynak anlatımı bilgiyi, anlayışı, ağırbaşlılığı ve doğruyu bilgi ile us yoluyla bulmayı tek bir yetkinlik alanında birleştirir. Bu alan salt bilgi sahibi olmaktan daha güçlü, yargılama ya da teknik ustalıktan ise farklıdır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bilgi ve kavrayış ya da doğru bir önerme"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bilgi ve usla doğruyu bulma yetkinliği"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bilgili, deneyimli ve doğruyu bulan kişi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"deneyimle olgunlaşmış bilge yaşlı"}],"lexicalization_note":"Tanım çıplak dalın bilgi, anlayış, ölçülülük ve doğruya erişme çekirdeğiyle sınırlıdır; başka dalların özel yapılarını içeri almaz.","neighbor_coverage_note":"Tüm adaylar karşılaştırıldı; yayımlanan ilişkiler bu dalı salt bilgiden, hızlı kavrayıştan ve yalnız ağırbaşlılıktan ayıran temel sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal bilişsel kavrayışa odaklanır; odak dal ise bu kavrayışın doğruyu bulma, ölçülülük ve iyi davranışla bütünleşmesini gerektirir.","focus_only":"Odak dal, bilgiyi ölçülü ve doğru davranışa dönüştürme yetkinliğini içerir.","gloss":"bilme ve doğruyu bulma","neighbor_only":"Komşu dal hızlı kavrama ve bir şeyin anlamlarını doğrulama süreçlerini daha geniş biçimde kapsar.","neighbor_ref":"root_001182/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bilgi edinme, anlama ve bir şeyin anlamını usla kavrama alanında örtüşür."},{"boundary_match":"partial","distinction":"Ağırbaşlılık odak dalın bir bileşenidir ama bilgiyle doğruyu bulma çekirdeğinin yerini tutmaz; komşu dal bu bilişsel koşulu gerektirmez.","focus_only":"Bilgi ve us yoluyla doğruya erişme yetkinliği belirleyicidir.","gloss":"bilgelik ve ağırbaşlılık","neighbor_only":"Komşu dal zihinsel sağlamlık, ağırbaşlılık ve cömertlik niteliklerini öne çıkarır.","neighbor_ref":"root_000591/B006","relation_type":"near_neighbor","shared_zone":"İki dal da ölçülü, dengeli ve yerinde davranan kişinin niteliğini anlatabilir."},{"boundary_match":"partial","distinction":"Bilgi odak dalın gerekli öğesidir, fakat odak dal onu us, ölçü ve doğru davranışla birleştirir; komşu dal salt bilgi süreçlerini de kapsar.","focus_only":"Doğruya ulaşan ölçülü uygulama ve davranış sonucu bulunur.","gloss":"bilgi ve bilgelik","neighbor_only":"Komşu dal öğrenme, öğretme, bildirme ve haber edinme süreçlerine kadar uzanır.","neighbor_ref":"root_001040/B001","relation_type":"near_neighbor","shared_zone":"Bilgi edinme ve bir şeyi bilinir duruma getirme iki alanın ortak zeminidir."}],"source_phrase_ar":"الحكمة تمنع من الجهل (maqayis)؛ الحكمة مرجعها إلى العدل والعلم والحلم (ayn)؛ الحكمة من العلم والحكيم العالم وصاحب الحكمة (sihah)؛ الحكم العلم والفقه (tahdhib)؛ الحكمة إصابة الحق بالعلم والعقل (mufradat)","source_summary":"Kaynakların ortak özeti, bilgisizliği uzaklaştıran bilgi ve anlayışın ölçülü davranışla birleşerek kişiyi doğru sonuca ulaştırmasıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"العلم والفقه؛ الحلم؛ إصابة الحق بالعلم والعقل؛ وصف الحكيم والعالم وصاحب الحكمة","what_is_not_ar":"القضاء بين الخصوم؛ إتقان الصنعة فقط؛ مجرد المنع الحسي"},"support_links":["sup_6651a80eed86d23a341f","sup_e27ec30ec80adc276402"]},{"boundary":"Çekirdek sağlamlaştırma ve kusursuzlaştırmadır; bilgi sahibi olma, yargılama ve düzeltici engelleme bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000348/B004","candidate_links":[{"candidate_id":"cand_1bd3cf21390948048637","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحْكَم","morph_features":"STEM|POS:N|LEM:>aHokam|ROOT:Hkm|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:8:3:2","qac_word_ref":"95:8:3","surface_ar":"أَحْكَمِ"},{"lemma_ar":"حَٰكِمِين","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ha`kimiyn|ROOT:Hkm|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:8:4:2","qac_word_ref":"95:8:4","surface_ar":"حَٰكِمِينَ"}],"gloss":"sağlam ve kusursuz duruma getirmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin yapısı veya düzeni sağlamlaştırılır ve kusur barındırmayacak biçimde tamamlanır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Süreç sonunda şey, sağlamlığı yerleşmiş ve bozulmaya karşı dirençli bir duruma gelir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir söz veya metin, kuşkuya ve karışıklığa yer bırakmayacak açıklıkta düzenlenmiş olabilir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir kişinin övgüye değer niteliğinde en ileri düzeye varması, sağlamlaşmanın kişiye uygulanmış özel bir anlatımıdır."}}],"root_ar":"ح ك م","root_id":"root_000348","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yapılan işlemi ve amaçlanan sağlam, eksiksiz sonuç durumunu birlikte taşıyan genel karşılıktır.","boundary_detail":"Çekirdek sağlamlaştırma ve kusursuzlaştırmadır; bilgi sahibi olma, yargılama ve düzeltici engelleme bu dala girmez.","branch_image_ar":"الإحكام والإتقان والوثاقة","concept_gloss":"sağlam ve kusursuz duruma getirmek","contextual_glosses":[{"applicability":"Bir işin, yapının veya düzenin gevşeklik bırakmadan güçlendirildiği bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kusursuzluk ve kuşkusuz açıklık yönlerini açıkça belirtmez.","preserves":"Sağlamlaştırma işlemini ve yerleşmiş sonucu korur."},"facet_ids":["F001","F002"],"text":"iyice sağlamlaştırmak","usage_role":"general"},{"applicability":"Bir sözün veya metnin açıklık ve tutarlılık bakımından eksiksiz kılındığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Fiziksel ya da genel sağlamlaştırma kapsamını dışarıda bırakır.","preserves":"Kuşku ve karışıklığı gideren düzenleme yönünü korur."},"facet_ids":["F003"],"text":"kuşkuya yer bırakmayacak biçimde düzenlemek","usage_role":"contextual"}],"definition":"Bir şeyi gevşeklik, eksik veya kuşku taşımayacak ölçüde sağlam ve kusursuz duruma getirmek ya da onun böyle bir duruma yerleşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin yapısı veya düzeni sağlamlaştırılır ve kusur barındırmayacak biçimde tamamlanır."},{"facet_id":"F002","role":"core","statement":"Süreç sonunda şey, sağlamlığı yerleşmiş ve bozulmaya karşı dirençli bir duruma gelir."},{"facet_id":"F003","role":"extension","statement":"Bir söz veya metin, kuşkuya ve karışıklığa yer bırakmayacak açıklıkta düzenlenmiş olabilir."},{"facet_id":"F004","role":"source_variant","statement":"Bir kişinin övgüye değer niteliğinde en ileri düzeye varması, sağlamlaşmanın kişiye uygulanmış özel bir anlatımıdır."}],"identity_rationale":"Kaynak anlatımı bir şeyi sağlam, kusursuz ve kuşkuya yer bırakmayacak duruma getirme ile bu durumun yerleşmesini ortak çekirdek olarak destekler. Bir kişinin kendi niteliğinde en ileri düzeye varması ise aynı sağlamlaşma görüntüsünün özel uzantısıdır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir şeyi sağlamlaştırmak veya sağlam duruma gelmek"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kusur ve kuşkuya yer bırakmayacak biçimde sağlamlaştırılmış"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"işleri sağlam ve kusursuz yapan"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"övgüye değer niteliğinde doruğa varmak"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kendisine zarar verecek şeylerden bütünüyle uzaklaşmak"}],"lexicalization_note":"Tanım yapma ve sonuç durumunu ayırır; metnin açıklığı ile kişinin kendi niteliğinde doruğa varması özel, yapıya bağlı uzantılar olarak kalır.","neighbor_coverage_note":"Bütün adaylar incelendi; seçilen üç yakın ilişki genel sağlamlaştırmayı işçilik, yapısal güç ve söz ya da dokuma alanındaki sıkılıktan ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Sağlamlaştırma çekirdekleri yakındır; odak dal kusursuzluk ve kuşkusuz açıklığı, komşu dal ise yapısal güç ile güvenilir seçimi ayrıca kapsar.","focus_only":"Odak dal kuşkuyu gideren açıklık ve bir niteliğin doruğuna ulaşma uzantılarını taşır.","gloss":"sağlamlaştırma ve güvenilirlik","neighbor_only":"Komşu dal canlıların yapısal sağlamlığına ve bir işte en güvenilir olanı seçmeye kadar uzanır.","neighbor_ref":"root_001623/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi güçlü, dayanıklı ve güvenilir duruma getirmeyi anlatır."},{"boundary_match":"partial","distinction":"Komşu dal yapım becerisi ve güzel işçiliğe daha yakındır; odak dal sağlam, eksiksiz ve kuşkusuz sonuç durumunu temel alır.","focus_only":"Odak dal kuşkuya yer bırakmayan açıklık ve yerleşmiş sağlamlık sonucunu içerir.","gloss":"kusursuz yapma","neighbor_only":"Komşu dal işçilik becerisini, güzel yapmayı ve canlıdaki güçlü yaratılışı öne çıkarır.","neighbor_ref":"root_000290/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bir işi iyi yapıp ürünü sağlam ve düzgün bir sonuca ulaştırabilir."},{"boundary_match":"partial","distinction":"Komşu dalın dokuma ve söz alanı belirgindir; odak dal ise genel sağlamlaştırmayı, sonuç durumunu ve kuşkunun giderilmesini kapsar.","focus_only":"Odak dal her tür şeyin sağlamlaştırılmasını ve sağlamlığın yerleşmesini kapsar.","gloss":"sağlam ve düzgün kurmak","neighbor_only":"Komşu dal özellikle dokuma ile sözün sıkı, doğru ve düzgün kurulmasına bağlıdır.","neighbor_ref":"root_000347/B010","relation_type":"near_synonym","shared_zone":"İki dal da bir ürünü gevşeklik ve kusur bırakmadan sağlam, tutarlı biçimde kurmayı anlatır."}],"source_phrase_ar":"استحكم الأمر وثق (ayn)؛ أحكمت الشيء فاستحكم أي صار محكما (sihah)؛ آياته أحكمت وفصلت (tahdhib)؛ المحكم ما لا يعرض فيه شبهة (mufradat)؛ حكم الرجل إذا بلغ النهاية في معناه (tahdhib)","source_summary":"Kaynaklar bir şeyi sağlamlaştırma, onun bu durumda yerleşmesi ve kuşku ya da eksik barındırmayan bir bütünlük kazanması çevresinde birleşir.","sources":["AY","SI","TA","MU"],"what_is_ar":"إحكام الشيء حتى يستحكم؛ كون الأمر وثيقا أو محكما؛ الآيات المحكمات؛ بلوغ الشيء نهايته في المدح أو السلامة","what_is_not_ar":"القضاء بين الناس؛ الحكمة بمعنى العلم فقط؛ منع السفيه أو الدابة"},"support_links":["sup_6651a80eed86d23a341f"]},{"boundary":"Dal, kararın kendisini değil karar verme veya davranma yetkisinin birine bırakılmasını kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000348/B005","candidate_links":[{"candidate_id":"cand_04abacf600b6ffea90ce","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحْكَم","morph_features":"STEM|POS:N|LEM:>aHokam|ROOT:Hkm|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:8:3:2","qac_word_ref":"95:8:3","surface_ar":"أَحْكَمِ"},{"lemma_ar":"حَٰكِمِين","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ha`kimiyn|ROOT:Hkm|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:8:4:2","qac_word_ref":"95:8:4","surface_ar":"حَٰكِمِينَ"}],"gloss":"karar verme yetkisini başkasına bırakmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işin yürütülmesi veya karara bağlanması başka bir kişinin yetkisine bırakılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Çekişen taraflar, aralarındaki konuda seçtikleri kişinin vereceği kararı geçerli sayar."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yetki verilen kişi, belirlenen iş veya mal üzerinde uygun gördüğü biçimde davranabilir."}}],"root_ar":"ح ك م","root_id":"root_000348","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İş, mal ve uyuşmazlık bağlamlarında ortak olan yetki devri çekirdeğini en kısa doğal biçimde karşılar.","boundary_detail":"Dal, kararın kendisini değil karar verme veya davranma yetkisinin birine bırakılmasını kapsar.","branch_image_ar":"التفويض والتحكيم","concept_gloss":"karar verme yetkisini başkasına bırakmak","contextual_glosses":[{"applicability":"Bir işin sonucunu başka bir kişinin seçimine ve kararına bağlama bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşi devretme, karar yetkisi verme ve sonucu o seçime bağlama yönlerini korur."},"facet_ids":["F001","F002","F003"],"text":"işi onun kararına bırakmak","usage_role":"general"},{"applicability":"Kişiye bir mal veya iş üzerinde uygun gördüğü gibi davranma izni verildiğinde doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Taraflar arasında karar verme görevinin devrini kapsamaz.","preserves":"Kişiye serbest davranma yetkisi verilmesini korur."},"facet_ids":["F003"],"text":"eli serbest bırakılmak","usage_role":"contextual"}],"definition":"Bir iş, mal veya uyuşmazlık hakkında karar verme ve uygun gördüğü biçimde davranma yetkisini başka bir kişiye bırakmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işin yürütülmesi veya karara bağlanması başka bir kişinin yetkisine bırakılır."},{"facet_id":"F002","role":"specialization","statement":"Çekişen taraflar, aralarındaki konuda seçtikleri kişinin vereceği kararı geçerli sayar."},{"facet_id":"F003","role":"extension","statement":"Yetki verilen kişi, belirlenen iş veya mal üzerinde uygun gördüğü biçimde davranabilir."}],"identity_rationale":"Kaynak anlatımı bir işin veya karar verme yetkisinin başka bir kişiye bırakılmasını, tarafların o kişinin kararını geçerli saymasını ve kişiye belirli alanda serbest davranma gücü verilmesini ortaklaştırır. Verilen kararın içeriği değil, yetkinin devri çekirdektir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir işte karar verme yetkisini ona bırakmak"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"malı üzerinde uygun gördüğü gibi davranabilmek"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yetim malını yönetmeye elverişli duruma geldiğinde malı üzerinde tasarruf etmesine izin vermek"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"birinin elini istediğini yapmakta serbest bırakmak"}],"lexicalization_note":"Tanım yetki devri çekirdeğini korur; mal üzerinde serbest davranma, taraflar arasında karar verme ve elini serbest bırakma yapıları ayrı uygulamalardır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan ilişkiler özel karar yetkisi devrini genel iş devrinden, vekillikten ve kararın verilmesinden ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın belirleyici yönü karar veya davranma yetkisidir; komşu dalda işi geri çevirip başkasına dayanma ilişkisi daha geniştir.","focus_only":"Odak dal, tarafların bir kişiye karar verme gücü tanımasını ve onun kararını geçerli saymasını kapsar.","gloss":"işi başkasına bırakmak","neighbor_only":"Komşu dal işi başkasına bırakırken ona dayanma ve sonucu ona emanet etme tutumunu öne çıkarır.","neighbor_ref":"root_001187/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda bir işin yönetimi veya sonucu başka bir kişinin eline verilir."},{"boundary_match":"partial","distinction":"Genel iş devri komşu dalda yeterlidir; odak dal özellikle karar verme serbestisini ve verilen kararın kabulünü öne çıkarır.","focus_only":"Uyuşmazlıktaki tarafların seçilen kişinin kararını önceden geçerli sayması odak dala özgüdür.","gloss":"yetkiyi başkasına vermek","neighbor_only":"Komşu dal vekil kılmayı ve genel olarak bir işi başkasına gördürmeyi daha geniş kapsar.","neighbor_ref":"root_001681/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir işin yürütülmesi veya karara bağlanması için başkasına yetki vermeyi içerir."},{"boundary_match":"field_only","distinction":"Yetkinin verilmesi ile bu yetkiye dayanılarak karar verilmesi ayrı işlemlerdir; odak dal sonuçtan önceki yetkilendirme aşamasıdır.","focus_only":"Odak dal karar verme yetkisinin kurulmasını anlatır.","gloss":"yetkilendirme ve karar","neighbor_only":"Komşu dal yetki kullanılarak bağlayıcı karar verilmesini anlatır.","neighbor_ref":"root_000348/B002","relation_type":"same_field","shared_zone":"İki dal aynı uyuşmazlıkta ardışık aşamalar olarak bulunabilir ve karar veren bir kişiyi gerektirebilir."}],"source_phrase_ar":"حكم فلان في كذا إذا جعل أمره إليه (maqayis)؛ احتكم في ماله إذا جاز فيه حكمه (ayn)؛ حكمته في مالي إذا جعلت إليه الحكم فيه (sihah)؛ حكمنا فلانا بيننا أي أجزنا حكمه بيننا (tahdhib)؛ الحكمين أن يتوليا الحكم عليهم ولهم حسب ما يستصوبانه (mufradat)","source_summary":"Kaynaklar, bir işin veya karar verme gücünün başka bir kişiye bırakılması ve o kişinin belirlenen alandaki seçiminin geçerli sayılması üzerinde birleşir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"جعل الحكم أو الأمر إلى شخص؛ إجازة حكمه بين المتخاصمين؛ الاحتكام إلى من يحكم؛ إطلاق يد المرء فيما شاء","what_is_not_ar":"القضاء الصادر نفسه؛ المنع والرد؛ الحكمة العلمية"},"support_links":["sup_0cddc03f956e5a2a9f09"]},{"boundary":"Çekirdek, gemin çene çevresini kuşatan kısıtlayıcı parçasıdır; her halka, bağ veya hayvan çenesi genel olarak bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000348/B006","candidate_links":[{"candidate_id":"cand_5d5b596d8050b161ed4a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحْكَم","morph_features":"STEM|POS:N|LEM:>aHokam|ROOT:Hkm|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:8:3:2","qac_word_ref":"95:8:3","surface_ar":"أَحْكَمِ"},{"lemma_ar":"حَٰكِمِين","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ha`kimiyn|ROOT:Hkm|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:8:4:2","qac_word_ref":"95:8:4","surface_ar":"حَٰكِمِينَ"}],"gloss":"gemin çene çevresini kuşatan kısıtlayıcı parçası","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Parça, hayvanın iki çene yanını veya ağız çevresini kuşatan bir gem bölümüdür."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu kuşatma hayvanın koşmasını ve denetimsiz ilerlemesini sınırlar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Adlandırma, aracın hayvanı engelleme işleviyle açıklanır; salt genel engelleme anlamı değildir."}}],"root_ar":"ح ك م","root_id":"root_000348","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Aracın yerini ve hayvanın hareketini sınırlayan temel işlevini birlikte açıklar.","boundary_detail":"Çekirdek, gemin çene çevresini kuşatan kısıtlayıcı parçasıdır; her halka, bağ veya hayvan çenesi genel olarak bu dala girmez.","branch_image_ar":"حكمة اللجام","concept_gloss":"gemin çene çevresini kuşatan kısıtlayıcı parçası","contextual_glosses":[{"applicability":"Parçanın hayvanın başındaki konumu anlatılırken kullanılan kısa ve doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvanın koşmasını sınırlayan işlevi açıkça söylemez.","preserves":"Gem bölümünü ve çene çevresindeki konumunu korur."},"facet_ids":["F001"],"text":"gemin çeneyi saran bölümü","usage_role":"general"},{"applicability":"Parçanın koşmayı ve ileri atılmayı sınırlayan işlevi öne çıkarıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Parçanın çene veya ağız çevresini kuşatan konumunu açıkça vermez.","preserves":"Gemin hayvanı kısıtlayan işlevini korur."},"facet_ids":["F002","F003"],"text":"hayvanı tutan gem parçası","usage_role":"contextual"}],"definition":"Gemin, hayvanın çene çevresini veya ağzını kuşatarak onun koşmasını ve ileri atılmasını sınırlayan parçasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Parça, hayvanın iki çene yanını veya ağız çevresini kuşatan bir gem bölümüdür."},{"facet_id":"F002","role":"core","statement":"Bu kuşatma hayvanın koşmasını ve denetimsiz ilerlemesini sınırlar."},{"facet_id":"F003","role":"associated_use","statement":"Adlandırma, aracın hayvanı engelleme işleviyle açıklanır; salt genel engelleme anlamı değildir."}],"identity_rationale":"Kaynak anlatımı dalı, gemin hayvanın çene çevresini kuşatan ve koşmasını sınırlayan parçası olarak destekler. Geçici çerçevedeki halka veya çenenin kendisi ifadesi genel tanıma katılmamalıdır; çene anlamı yalnız ayrı bir sözcük biriminde özel olarak bulunur.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"gemin hayvanın çene çevresini kuşatıp koşmasını sınırlayan parçası"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"hayvana gem takmak veya onu gemle durdurmak"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"koyunun çenesi"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"başında gemin kısıtlayıcı parçası bulunan at"}],"lexicalization_note":"Tanım gem ve hayvanla sınırlı araç anlamını korur; gem takma eylemi, koyun çenesi ve bu parçayı taşıyan at ayrı kullanımlardır.","neighbor_coverage_note":"Tüm adaylar incelendi; seçilen ilişkiler bu parçayı gem halkalarından, genel kısıtlama araçlarından ve çene kemiğinin kendisinden ayırır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Komşu dal belirli iki halkaya, odak dal ise çene çevresini kuşatıp hareketi sınırlayan daha işlevsel gem bölümüne karşılık gelir.","focus_only":"Odak dal çene çevresini kuşatan ve hayvanı kısıtlayan gem bölümünün bütününü anlatır.","gloss":"gem bölümü ve uç halkaları","neighbor_only":"Komşu dal yalnız ağız demirinin iki ucundaki iki halkayı adlandırır.","neighbor_ref":"root_000684/B008","relation_type":"same_field","shared_zone":"İki dal da gem takımının hayvanın ağzı çevresinde bulunan parçalarını anlatır."},{"boundary_match":"partial","distinction":"Odak dalın araç türü ve hayvan başındaki konumu belirgindir; komşu dal her türlü kısıtlayıcı bağ ve araca uzanan daha geniş bir alandır.","focus_only":"Odak dal hayvanın çene çevresindeki belirli gem parçasıyla sınırlıdır.","gloss":"kısıtlayıcı gem parçası","neighbor_only":"Komşu dal insanı veya şeyi hareketten alıkoyan zincir, demir ve başka araçları da kapsar.","neighbor_ref":"root_001554/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir araç veya gem bölümü hareketi engelleme işlevi görür."},{"boundary_match":"field_only","distinction":"Biri çene çevresine yerleştirilen işlevsel bir araç parçası, diğeri ise bedenin doğal kemik bölümüdür.","focus_only":"Odak dal çene çevresine takılan ve kısıtlama işlevi gören bir araç parçasıdır.","gloss":"gem parçası ve çene kemiği","neighbor_only":"Komşu dal çene kemiğinin kendisini ve diş ya da sakal köklerinin bulunduğu bölgeyi anlatır.","neighbor_ref":"root_001350/B001","relation_type":"same_field","shared_zone":"İki dal aynı çene bölgesine gönderme yapar ve hayvan betimlemelerinde birlikte görülebilir."}],"source_phrase_ar":"حكمة الدابة لأنها تمنعها (maqayis)؛ حكمة اللجام ما أحاط بحنكيه (ayn)؛ حكمة اللجام ما أحاط بالحنك (sihah)؛ حكمة اللجام ما أحاط بحنكيه (tahdhib)؛ سميت اللجام حكمة الدابة (mufradat)","source_summary":"Kaynaklar terimi hayvanın gemiyle ilişkisi çevresinde birleştirir; tanıklıklar çene çevresini kuşatan bölüm, hayvanı kısıtlama işlevi ve gemin bu adla anılması yönlerini farklı biçimlerde öne çıkarır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"حكمة الدابة؛ ما يحيط بحنكي الدابة؛ الحلقة أو الذقن وما يمنع الفرس من الجري","what_is_not_ar":"الحكمة بمعنى العلم؛ الحكم القضائي؛ المنع المجرد من غير آلة"},"support_links":["sup_894381612f755e3fff01"]},{"boundary":"Alan yalnız belirtilen yapıdaki kendiliğinden geri dönme ve ettirgen geri döndürme anlamlarını kapsar.","branch_kind":"non_bare","branch_ref":"root_000348/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحْكَم","morph_features":"STEM|POS:N|LEM:>aHokam|ROOT:Hkm|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:8:3:2","qac_word_ref":"95:8:3","surface_ar":"أَحْكَمِ"},{"lemma_ar":"حَٰكِمِين","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ha`kimiyn|ROOT:Hkm|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:8:4:2","qac_word_ref":"95:8:4","surface_ar":"حَٰكِمِينَ"}],"gloss":"bir şeyden geri dönmek veya birini döndürmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi yöneldiği veya giriştiği bir şeyden kendi hareketiyle geri döner."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ettirgen kullanımda başka biri kişiyi yöneldiği şeyden geri döndürür."}}],"root_ar":"ح ك م","root_id":"root_000348","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kanıtlanan özel yapılarda hem kendiliğinden hem ettirgen katılımcı düzenini karşılar.","boundary_detail":"Alan yalnız belirtilen yapıdaki kendiliğinden geri dönme ve ettirgen geri döndürme anlamlarını kapsar.","branch_image_ar":"الرجوع والإرجاع عن الشيء","concept_gloss":"bir şeyden geri dönmek veya birini döndürmek","contextual_glosses":[{"applicability":"Kişinin yöneldiği veya giriştiği bir şeyden kendi isteği ya da hareketiyle dönmesi bağlamındadır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka bir kişinin onu geri döndürdüğü ettirgen düzeni kapsamaz.","preserves":"Kişinin bir şeyden kendi hareketiyle geri dönmesini korur."},"facet_ids":["F001"],"text":"o işten geri dönmek","usage_role":"contextual"},{"applicability":"Bir kişinin başka birini yöneldiği veya giriştiği şeyden çevirmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin kendi hareketiyle geri dönmesi kullanımını kapsamaz.","preserves":"Başkasını belirli bir şeyden geri döndürme işlemini korur."},"facet_ids":["F002"],"text":"onu o işten geri döndürmek","usage_role":"contextual"}],"definition":"Belirli yapı içinde bir kişinin yöneldiği bir şeyden geri dönmesi veya başka birinin onu o şeyden geri döndürmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi yöneldiği veya giriştiği bir şeyden kendi hareketiyle geri döner."},{"facet_id":"F002","role":"core","statement":"Ettirgen kullanımda başka biri kişiyi yöneldiği şeyden geri döndürür."}],"identity_rationale":"Tek kaynak anlatımı, belirli bir yapı içinde kişinin bir şeyden geri dönmesi ile başka birinin onu o şeyden geri döndürmesini açıkça ayırır. Dal, genel geri dönüş anlamına değil bu iki yapıya bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"bir şeyden geri dönmek"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"birini bir şeyden geri döndürmek"}],"lexicalization_note":"Tanım çıplak köke genellenmez; bir şeyden geri dönme ve birini o şeyden geri döndürme yapılarıyla sınırlı tutulur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; seçilen ilişkiler yapıya bağlı bu kullanımı genel dönüşten, önceki duruma getirmeden ve uzamsal geri çekilmeden ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Katılımcı düzenleri yakındır; odak dal yapısal olarak sınırlı ve tek tanıklı bir kullanımdır, komşu dal ise genel dönüş ve yön değiştirme alanına yayılır.","focus_only":"Odak dal yalnız kanıtlanan özel yapılarda geri dönme ve geri döndürme çiftini taşır.","gloss":"geri dönmek ve döndürmek","neighbor_only":"Komşu dal ayrılıktan sonra dönüşü, başka bir işe yönelmeyi ve geri döndürmeyi daha genel biçimde kapsar.","neighbor_ref":"root_001191/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda kişi önceki yönelişinden ayrılır veya başka biri onu bu yönelişten çevirir."},{"boundary_match":"partial","distinction":"Komşu dal başlangıç yönüne veya önceki duruma dönüşü gerektirir; odak dalda belirleyici olan yönelinen şeyden uzaklaşmadır.","focus_only":"Odak dal bir şeyden vazgeçer gibi geri dönmeyi ve birini ondan çevirmeyi anlatır.","gloss":"geri dönme ve geri getirme","neighbor_only":"Komşu dal bir nesne veya kişiyi başladığı yere ya da önceki durumuna geri getirmeyi kapsar.","neighbor_ref":"root_000544/B001","relation_type":"near_synonym","shared_zone":"İki dal da öznenin geri hareketini ve başka bir katılımcının bu dönüşü sağlamasını kapsayabilir."},{"boundary_match":"partial","distinction":"Komşu dalın uzamsal geri adım görüntüsü güçlüdür; odak dal ise bir işten veya yönelişten dönmeye bağlıdır ve ettirgen biçimi de içerir.","focus_only":"Odak dal geri dönülen şeyden uzaklaşmayı ve ettirgen geri döndürmeyi kapsar.","gloss":"geri dönme ve geri çekilme","neighbor_only":"Komşu dal geri adım atma, arkaya dönme ve ilerledikten sonra gerileme görüntüsünü öne çıkarır.","neighbor_ref":"root_001033/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal önceki ileri yönelişin tersine çevrilmesini veya bırakılmasını anlatabilir."}],"source_phrase_ar":"حكم فلان عن الشيء أي رجع؛ وأحكمته أنا أي رجعته (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu özel kullanım tek kaynakta, geri dönme ve geri döndürme biçimleri birlikte verilerek tanıklanır."}],"source_summary":"Kanıt, aynı özel yapı alanında kendiliğinden geri dönme ile başkasını geri döndürme arasında açık bir katılımcı ayrımı kurar.","sources":["TA"],"what_is_ar":"حكم عن الشيء بمعنى رجع؛ أحكمته بمعنى رجعته","what_is_not_ar":"المنع العام المتعدي؛ القضاء؛ الحكمة العلمية"},"support_links":[]},{"boundary":"Bu dal yalnızca yüklemli olumsuzluk işlevini kapsar; istisna, bağlama olumsuzluğu ve kişi nitelikleri ayrı dallardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001390/B001","candidate_links":[{"candidate_id":"cand_5f7ec71ec2a78a45509d","lane":"micro"},{"candidate_id":"cand_04abacf600b6ffea90ce","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لَّيْسَ","morph_features":"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"95:8:1:2","qac_word_ref":"95:8:1","surface_ar":"لَيْسَ"}],"gloss":"özneyi yalın, yüklemi belirtme durumunda tutan geçmiş biçimli olumsuzluk eylemi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir durum ya da niteliğin özne için geçerli olmadığını bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Biçimce geçmiş zamanlı ve değişmez bir eylemdir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özneyi yalın durumda, yüklem öğesini belirtme durumunda kullanır."}}],"root_ar":"ل ي س","root_id":"root_001390","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın olumsuzluk, biçim ve söz dizimi özelliklerinin birlikte açıklanması gereken genel kullanımına uygundur.","boundary_detail":"Bu dal yalnızca yüklemli olumsuzluk işlevini kapsar; istisna, bağlama olumsuzluğu ve kişi nitelikleri ayrı dallardır.","branch_image_ar":"ليس جحود ينفي الحال كفعل جامد","concept_gloss":"özneyi yalın, yüklemi belirtme durumunda tutan geçmiş biçimli olumsuzluk eylemi","contextual_glosses":[{"applicability":"Bir özneye yüklenen durum ya da niteliği doğal Türkçe bir cümlede olumsuzlamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kaynak biçimin geçmiş zaman görünümünü ve öğelerin durumunu yöneten eylem niteliğini açıkça göstermez.","preserves":"Yüklemli olumsuzluk işlevini doğal bir Türkçe karşılıkla korur."},"facet_ids":["F001"],"text":"değildir","usage_role":"contextual"}],"definition":"Biçimce geçmiş zamanlı ve değişmez bir eylem olarak yüklemli olumsuzluk bildirir; özneyi yalın durumda, yüklem öğesini belirtme durumunda tutar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir durum ya da niteliğin özne için geçerli olmadığını bildirir."},{"facet_id":"F002","role":"specialization","statement":"Biçimce geçmiş zamanlı ve değişmez bir eylemdir."},{"facet_id":"F003","role":"specialization","statement":"Özneyi yalın durumda, yüklem öğesini belirtme durumunda kullanır."}],"identity_rationale":"Kaynak ifadesi bu dalı olumsuzluk bildiren, biçimce geçmiş zamanlı olan ve özne ile yüklem öğesini belirli durumlara sokan değişmez bir eylem olarak kurar. Geçici dal çerçevesi bu dilbilgisel çekirdeği doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"özneyi yalın, yüklem öğesini belirtme durumunda kullanarak olumsuzluk bildiren geçmiş biçimli eylem"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bulunduğu ya da bulunmadığı yerden"}],"lexicalization_note":"Tanım temel dilbilgisel işlevi verir; özel söz öbeğinin bağlama bağlı anlamı bu çekirdeğe genellenmeden ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca yüklemli olumsuzluğu istisnadan, özel olumsuzluk kullanımından ve bilinçli inkârdan ayıran üç karşılaştırma sınırı belirginleştirdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal bir cümlenin yüklemli olumsuzluğunu eylem gibi kurar; komşu dal ise başka olumsuzluk araçlarının bağlama ya da tümel yokluk işlevinde kullanılır.","focus_only":"Yüklemli olumsuzluk kurar ve özne ile yüklem öğesinin dilbilgisel durumunu yönetir.","gloss":"yüklemli olumsuzluk ile özel olumsuzluk ayrımı","neighbor_only":"Bağlama olumsuzluğu veya bir türün bütünüyle yokluğunu bildiren özel kullanımın yerini tutar.","neighbor_ref":"root_001390/B003","relation_type":"near_neighbor","shared_zone":"İki dal da olumsuzluk bildirir ve aynı biçim ailesine dayanır."},{"boundary_match":"partial","distinction":"Bu dal yüklemi olumsuzlar; komşu dal ise ardından gelen öğeyi istisna eder ve olumsuz yüklem kurmak zorunda değildir.","focus_only":"Bir durumun özne için geçerli olmadığını yüklem düzeyinde bildirir.","gloss":"olumsuzlama ile dışarıda bırakma ayrımı","neighbor_only":"Bir öğeyi anılan topluluğun ya da hükmün dışında bırakır.","neighbor_ref":"root_001390/B002","relation_type":"near_neighbor","shared_zone":"İki kullanım aynı dilbilgisel biçimi kullanır ve cümlede bir sınırlandırma etkisi oluşturur."},{"boundary_match":"field_only","distinction":"Bu dalın çekirdeği cümle kuran dilbilgisel olumsuzluktur; komşu dal bilgiye rağmen yapılan iradeli inkârdır.","focus_only":"Tarafsız bir dilbilgisel olumsuzluk işlemi bildirir.","gloss":"dilbilgisel olumsuzluk ile bilinçli inkâr","neighbor_only":"Doğru olduğunu bildiği bir şeyi bilinçli biçimde inkâr eden kişinin tutumunu bildirir.","neighbor_ref":"root_000224/B001","relation_type":"same_field","shared_zone":"Her ikisi de bir içeriği geçersiz sayma ya da reddetme alanıyla ilişkilidir."}],"source_phrase_ar":"ليس كلمة جحود ... معناه لا أيس (ayn;tahdhib)؛ ليس: كلمة نفي، وهو فعل ماض (sihah)؛ تكون بمنزلة كان، ترفع الاسم وتنصب الخبر (tahdhib)","source_summary":"Kaynaklar, bu biçimin olumsuzluk bildirdiği, geçmiş zaman görünümünde olduğu ve özne ile yüklem öğesinin durumunu belirleyen bir eylem gibi işlediği konusunda birleşir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه ليس كلمة جحود أو نفي، وعملها عمل كان فترفع الاسم وتنصب الخبر، وتصريفها بلفظ الماضي دون المستقبل، ودخول الباء في خبرها لتأكيد النفي.","what_is_not_ar":"لا يدخل فيه الاستثناء بليس، ولا ليس بمعنى لا النسقية أو لا التبرئة، ولا أوصاف الأليس."},"support_links":["sup_0cddc03f956e5a2a9f09","sup_9591c7e41a55ecca2efb"]},{"boundary":"Dal, yalnızca öğeyi dışarıda bırakan özel dilbilgisel yapıyı kapsar; genel olumsuzluk veya bağımsız bir dışlama kavramı değildir.","branch_kind":"non_bare","branch_ref":"root_001390/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَّيْسَ","morph_features":"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"95:8:1:2","qac_word_ref":"95:8:1","surface_ar":"لَيْسَ"}],"gloss":"ardından gelen öğeyi belirtme durumunda dışarıda bırakan istisna yapısı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ardından gelen öğeyi daha önce anılan kapsamın dışında bırakır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dışarıda bırakılan öğe belirtme durumunda kullanılır."}}],"root_ar":"ل ي س","root_id":"root_001390","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem dışlama işlemini hem de özel söz dizimsel davranışını birlikte belirtmek gereken yerlerde uygundur.","boundary_detail":"Dal, yalnızca öğeyi dışarıda bırakan özel dilbilgisel yapıyı kapsar; genel olumsuzluk veya bağımsız bir dışlama kavramı değildir.","branch_image_ar":"ليس استثناء يخرج المذكور","concept_gloss":"ardından gelen öğeyi belirtme durumunda dışarıda bırakan istisna yapısı","contextual_glosses":[{"applicability":"Bir topluluktan ya da hükümden tek bir öğeyi doğal Türkçede ayırmak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dışarıda bırakılan öğenin kaynak yapıdaki belirtme durumu özelliğini göstermez.","preserves":"Öğeyi verilen kapsamın dışında bırakma işlevini korur."},"facet_ids":["F001"],"text":"dışında","usage_role":"contextual"}],"definition":"Belirli bir söz dizimsel yapıda ardından gelen öğeyi anılan topluluğun ya da hükmün dışında bırakır ve bu öğeyi belirtme durumunda kullanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ardından gelen öğeyi daha önce anılan kapsamın dışında bırakır."},{"facet_id":"F002","role":"specialization","statement":"Dışarıda bırakılan öğe belirtme durumunda kullanılır."}],"identity_rationale":"Kaynak ifadesi, bu kullanımda ardından gelen öğenin dışarıda bırakıldığını ve belirtme durumunda bulunduğunu açıkça belirtir. Geçici çerçeve bu özel istisna işlevini yüklemli olumsuzluktan doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ardından gelen adı belirtme durumunda kullanarak dışarıda bırakan istisna yapısı"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"senin dışında"}],"lexicalization_note":"Tanım, biçimin yalnızca istisna kurduğu özel söz dizimsel kullanıma bağlıdır ve yalın kök anlamı olarak genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel istisna kavramı, başka bir özel istisna aracı ve aynı biçimin yüklemli olumsuzluğu en yararlı sınırları verdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal tek bir özel söz dizimsel aracın istisna işlevidir; komşu dal ise istisna etmenin çeşitli biçim ve alanlarını kapsayan daha geniş kavramdır.","focus_only":"Belirli bir dilbilgisel biçimle kurulur ve dışarıda bırakılan öğeyi belirtme durumunda kullanır.","gloss":"özel istisna yapısı ile genel istisna","neighbor_only":"İstisna işlemini ad, söz, yemin ve alışveriş gibi daha geniş yapılarda kapsar.","neighbor_ref":"root_000208/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da bir öğeyi genel kapsamın hükmünden çıkarır."},{"boundary_match":"partial","distinction":"İşlevleri bazı bağlamlarda yaklaşsa da kullanılan araç ve söz dizimsel sınırları ayrıdır; komşu kullanım ayrıca başka bir bağıntı yorumuna açıktır.","focus_only":"Dışarıda bırakılan öğenin belirtme durumunda kullanıldığı bir eylem biçimine bağlıdır.","gloss":"iki özel istisna aracının ayrımı","neighbor_only":"Başka bir özel araçla kurulur ve kaynak yorumuna göre dışlama dışında farklı bir bağıntı da bildirebilir.","neighbor_ref":"root_000167/B003","relation_type":"near_synonym","shared_zone":"İki dal da belirli bir dilbilgisel araçla dışarıda bırakma anlamı verebilir."},{"boundary_match":"partial","distinction":"Bu dal öğeyi kapsam dışında bırakır; komşu dal ise özne ile yüklem arasında olumsuz bir yargı kurar.","focus_only":"Bir öğeyi anılan kapsamdan çıkarır.","gloss":"istisna ile yüklemli olumsuzluk","neighbor_only":"Bir özneye yüklenen durum ya da niteliği olumsuzlar.","neighbor_ref":"root_001390/B001","relation_type":"near_neighbor","shared_zone":"İki dal aynı biçim ailesini ve sınırlandırıcı bir dilbilgisel etkiyi paylaşır."}],"source_phrase_ar":"وقد يستثنى بها، تقول: جاءني القوم ليس زيدا (sihah)؛ يكون استثناء، ينصب به ... بمعنى ما عدا زيدا ... بمعنى إلا زيدا (tahdhib)","source_summary":"Kaynaklar, yapının istisna bildirdiği, ardından gelen öğeyi kapsam dışında bıraktığı ve bu öğeyi belirtme durumunda kullandığı konusunda birleşir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه استعمال ليس للاستثناء بمعنى إلا أو ما عدا، مثل نصب الاسم بعدها في جاءني القوم ليس زيدا.","what_is_not_ar":"لا يدخل فيه نفي الجملة على عمل كان، ولا لا النسقية، ولا أوصاف الأليس."},"support_links":[]},{"boundary":"Bu dal yalnızca belirtilen iki özel dilbilgisel ikameyi kapsar; yüklemli olumsuzluk ve istisna işlevleri dışarıda kalır.","branch_kind":"non_bare","branch_ref":"root_001390/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَّيْسَ","morph_features":"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"95:8:1:2","qac_word_ref":"95:8:1","surface_ar":"لَيْسَ"}],"gloss":"bağlama ya da tümel yokluk bildiren özel olumsuzluk kullanımı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bağlama yapısında sonraki öğeye olumsuzluk yükleyen aracın yerini tutar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir türün hiçbir üyesinin bulunmadığını bildiren genel olumsuzluk aracının yerini tutar."}}],"root_ar":"ل ي س","root_id":"root_001390","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın iki ayrı özel dilbilgisel çevresini tek üst ifadede göstermek gereken açıklamalarda uygundur.","boundary_detail":"Bu dal yalnızca belirtilen iki özel dilbilgisel ikameyi kapsar; yüklemli olumsuzluk ve istisna işlevleri dışarıda kalır.","branch_image_ar":"ليس تقوم مقام لا في النسق والتبرئة","concept_gloss":"bağlama ya da tümel yokluk bildiren özel olumsuzluk kullanımı","contextual_glosses":[{"applicability":"Bağlanan ikinci öğeyi doğal Türkçede olumsuzlamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir türün bütün üyelerini yok sayan genel olumsuzluk kullanımını kapsamaz.","preserves":"Bağlama yapısındaki olumsuzluk işlevini korur."},"facet_ids":["F001"],"text":"ne de","usage_role":"contextual"},{"applicability":"Bir türün hiçbir üyesinin bulunmadığını doğal Türkçede bildirmek için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bağlanan ikinci öğeyi olumsuzlama işlevini kapsamaz.","preserves":"Türün bütünüyle yokluğunu bildiren genel olumsuzluğu korur."},"facet_ids":["F002"],"text":"hiçbir","usage_role":"contextual"}],"definition":"Özel dilbilgisel çevrelerde ya bağlanan bir öğeyi olumsuzlar ya da adı geçen türün bütünüyle bulunmadığını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bağlama yapısında sonraki öğeye olumsuzluk yükleyen aracın yerini tutar."},{"facet_id":"F002","role":"specialization","statement":"Bir türün hiçbir üyesinin bulunmadığını bildiren genel olumsuzluk aracının yerini tutar."}],"identity_rationale":"Kaynak ifadesi iki özel işlevi birlikte verir: bağlama sırasında olumsuzluk kurma ve bir türün tamamını yok sayan genel olumsuzluk. Geçici dal çerçevesi bu iki işlevi olağan yüklemli olumsuzluktan doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bağlanan öğeyi olumsuzlayan ya da bir türün bütünüyle bulunmadığını bildiren söz"}],"lexicalization_note":"Tanım iki özel dilbilgisel çevreyle sınırlıdır; bunlar biçimin genel ve bağlamdan bağımsız anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; temel yüklemli olumsuzluk, daha geniş başkalık alanı ve olumsuzluğu bozan cevap aracı bu özel kullanımların sınırını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal iki özel ikame çevresine bağlıdır; komşu dal ise özne ve yüklem ilişkisini doğrudan olumsuzlayan temel kullanımdır.","focus_only":"Bağlama olumsuzluğu ya da bir türün bütünüyle yokluğu için başka bir aracın yerini tutar.","gloss":"özel olumsuzluk ile yüklemli olumsuzluk","neighbor_only":"Özne ile yüklem arasında olumsuz yargı kuran eylem gibi davranır.","neighbor_ref":"root_001390/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir içeriğin geçerli olmadığını dilbilgisel olarak bildirir."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği belirli olumsuzluk görevleridir; komşu dalın çekirdeği başkalık ve ayrılıktır, olumsuzluk bunun yalnızca bir uzantısıdır.","focus_only":"Bağlama ya da tümel yokluk bildiren iki belirli dilbilgisel işleve bağlıdır.","gloss":"özel olumsuzluk ile başkalık alanı","neighbor_only":"Başkalık, karşıtlık, istisna ve olumsuzluğu daha geniş bir anlam alanında birleştirir.","neighbor_ref":"root_001119/B005","relation_type":"near_neighbor","shared_zone":"İki dal da olumsuzluk veya bir öğenin kapsam dışında kalmasıyla ilişkilidir."},{"boundary_match":"thematic_only","distinction":"Bu dal olumsuzluk kurar; komşu dal ise var olan olumsuzluğa cevap vererek onu tersine çevirir.","focus_only":"Bir öğeyi ya da türü olumsuzlar.","gloss":"olumsuzluk ile olumsuzu bozma","neighbor_only":"Önceden kurulmuş olumsuzluğu yanıt içinde bozup olumlu hükmü geri getirir.","neighbor_ref":"root_000154/B010","relation_type":"thematic","shared_zone":"İki dal da olumsuz bir ifadenin dilbilgisel yönetiminde rol oynar."}],"source_phrase_ar":"ربما جاءت ليس بمعنى لا التي ينسق بها؛ وربما جاءت ليس بمعنى لا التبرئة (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, biçimin hem bağlama olumsuzluğu hem de bir türü bütünüyle yok sayan genel olumsuzluk işlevinde kullanılabildiğini bildirir."}],"source_summary":"Bu dal için kaynaklar arasında ortaklaştırılacak ayrı bir anlatım yoktur; iki özel dilbilgisel işlev tek tanıklıkla sınırlıdır.","sources":["TA"],"what_is_ar":"يدخل فيه مجيء ليس بمعنى لا التي ينسق بها، ومجيئها بمعنى لا التبرئة.","what_is_not_ar":"لا يدخل فيه ليس العاملة عمل كان، ولا الاستثناء بليس، ولا أوصاف الأليس."},"support_links":[]},{"boundary":"Dal savaşta korkusuz ve rakibine karşı sebatlı kişiyi kapsar; yerinde kalma, yumuşak huyluluk, zayıf yargı ve yergi anlamları ayrıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001390/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَّيْسَ","morph_features":"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"95:8:1:2","qac_word_ref":"95:8:1","surface_ar":"لَيْسَ"}],"gloss":"savaşta korkmayan ve rakibini bırakmayan yiğit","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Savaş karşısında korkuya kapılmayan yiğit kişiyi belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karşısındaki rakibi bırakmadan mücadelede sebat eder."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu nitelikteki kişi için övgü sözü olarak kullanılabilir."}}],"root_ar":"ل ي س","root_id":"root_001390","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın savaş korkusuzluğu ile rakip karşısındaki sebatını birlikte aktarmak gereken genel açıklamalarda uygundur.","boundary_detail":"Dal savaşta korkusuz ve rakibine karşı sebatlı kişiyi kapsar; yerinde kalma, yumuşak huyluluk, zayıf yargı ve yergi anlamları ayrıdır.","branch_image_ar":"الأليس شجاع لا تروعه الحرب","concept_gloss":"savaşta korkmayan ve rakibini bırakmayan yiğit","contextual_glosses":[{"applicability":"Savaşta korkusuzluk özelliğini doğal ve kısa bir Türkçe ifadeyle öne çıkarmak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Rakibinden ayrılmama ve mücadeleyi sürdürme koşulunu açıkça belirtmez.","preserves":"Savaş bağlamındaki yiğitlik ve korkusuzluğu korur."},"facet_ids":["F001"],"text":"gözü pek savaşçı","usage_role":"contextual"}],"definition":"Savaşın korkutmadığı ve karşısındaki rakipten ayrılmadan mücadeleyi sürdüren yiğit kişidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Savaş karşısında korkuya kapılmayan yiğit kişiyi belirtir."},{"facet_id":"F002","role":"specialization","statement":"Karşısındaki rakibi bırakmadan mücadelede sebat eder."},{"facet_id":"F003","role":"associated_use","statement":"Bu nitelikteki kişi için övgü sözü olarak kullanılabilir."}],"identity_rationale":"Kaynak ifadesi kişiyi savaşın korkutmadığı, rakibinden ayrılmadığı ve bu nedenle yiğit sayıldığı özelliklerle tanımlar. Geçici çerçeve savaş bağlamındaki korkusuzluk ile sebatı doğru biçimde bir arada tutar.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"savaş karşısında yılmayan yiğitlik"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"savaştan korkmayan ve rakibini bırakmayan yiğit"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"övgüde gözü pek kişi, yergide evinden ayrılmayan kimse için söylenen söz"}],"lexicalization_note":"Tanım savaşta korkusuzluk ve rakibi bırakmama çekirdeğini korur; övgü sözü bu çekirdeğe bağlı özel bir gerçekleşimdir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; çatışmadan ayrılmayan kişi, genel kahraman ve aynı kökteki yerinden ayrılmama dalı savaşçı yiğitliğin sınırını en iyi belirledi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal korkusuzluğu ve rakip karşısındaki yiğitliği tanımın çekirdeğine alır; komşu dal daha çok çatışma alanından ayrılmama davranışına odaklanır.","focus_only":"Savaşın korkutmaması ve belirli rakibi bırakmama özelliklerini birlikte taşır.","gloss":"korkusuz yiğit ile çatışmadan ayrılmayan kişi","neighbor_only":"Doğrudan çatışma alanından ayrılmama ve savaşa bağlı kalma davranışını öne çıkarır.","neighbor_ref":"root_000304/B012","relation_type":"near_synonym","shared_zone":"Her iki dal da savaşta sebat eden ve çatışmayı bırakmayan kişiyi anlatır."},{"boundary_match":"partial","distinction":"Bu dal savaş ve rakip karşısındaki belirli davranışlarla tanımlanır; komşu dal kahramanlığı daha genel ve tehlikeye atılma yönüyle anlatır.","focus_only":"Savaşın korkutmaması ve rakipten ayrılmama koşullarıyla sınırlıdır.","gloss":"sebatlı savaşçı ile genel kahraman","neighbor_only":"Tehlikeye atılan kahramanı ve yiğitliği savaş dışına da uzanan daha geniş bir çerçevede kapsar.","neighbor_ref":"root_000127/B004","relation_type":"near_synonym","shared_zone":"İki dal da tehlike karşısında cesaret gösteren yiğit kişiyi belirtir."},{"boundary_match":"partial","distinction":"Bu dalda ayrılmama savaşçı sebatıdır; komşu dalda fiziksel bir yerde kalma ve kimi zaman ağır bulunma söz konusudur.","focus_only":"Rakip karşısında savaşmayı sürdürmek olumlu bir yiğitlik niteliğidir.","gloss":"mücadelede sebat ile yerinden ayrılmama","neighbor_only":"Bir yerden ya da evden ayrılmamak ağırlık veya yergi taşıyabilir ve savaş gerektirmez.","neighbor_ref":"root_001390/B005","relation_type":"near_neighbor","shared_zone":"İki dalda da bir konumdan ya da karşı karşıya olunan şeyden ayrılmama öğesi vardır."}],"source_phrase_ar":"الأليس وهو الشجاع الذي لا يروعه الحرب (ayn;tahdhib)؛ ورجل أليس، أي شجاع بين الليس (sihah)؛ الأليس الذي لا يبارح قرنه؛ يقال للرجل الشجاع: أهيس أليس (tahdhib)","source_summary":"Kaynaklar savaşın korkutmadığı yiğit kişi çekirdeğinde birleşir; ayrıca rakibi bırakmama ve bu niteliği övgüyle anma ayrıntıları verilir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه الأليس والرجل الأليس بمعنى الشجاع الذي لا تروعه الحرب، ولا يبارح قرنه، وما جاء في المدح مثل أهيس أليس إذا أريد به الشجاع.","what_is_not_ar":"لا يدخل فيه الثقل ولزوم البيت أو الحوض، ولا ضعف الرأي، ولا الديوثي الذي لا يغار، ولا استعمال ليس النحوي."},"support_links":[]},{"boundary":"Dal fiziksel bir yerde kalmayı kapsar; savaşta sebat, güçlüğe katlanma ve yumuşak huyluluk bu anlamın parçası değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001390/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَّيْسَ","morph_features":"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"95:8:1:2","qac_word_ref":"95:8:1","surface_ar":"لَيْسَ"}],"gloss":"yerinden ayrılmayan ağır kişi veya bulunduğu yerde kalan hayvan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bulunduğu yerden ayrılmayıp orada kalmayı belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi için yerinden veya evinden ayrılmayan ağır kimseyi anlatır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Develer için su başında kalıp oradan ayrılmamayı anlatır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Evinden ayrılmayan kişi hakkında yergi olarak kullanılabilir."}}],"root_ar":"ل ي س","root_id":"root_001390","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişi ile hayvan uygulamalarını ortak kalma çekirdeği altında birlikte göstermek gereken genel açıklamalarda uygundur.","boundary_detail":"Dal fiziksel bir yerde kalmayı kapsar; savaşta sebat, güçlüğe katlanma ve yumuşak huyluluk bu anlamın parçası değildir.","branch_image_ar":"الأليس ملازم لا يبرح مكانه","concept_gloss":"yerinden ayrılmayan ağır kişi veya bulunduğu yerde kalan hayvan","contextual_glosses":[{"applicability":"Bir kişinin bulunduğu yerden ya da evinden ayrılmamasını doğal Türkçede anlatmak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Develerin su başında kalması uzantısını kapsamaz.","preserves":"Kişinin bir yerde kalıp ayrılmaması özelliğini korur."},"facet_ids":["F001","F002"],"text":"yerinden kımıldamayan kimse","usage_role":"contextual"}],"definition":"Bir kişinin yerinden ya da evinden, develerin ise su başından ayrılmayıp orada kalmasıdır; kişi için ağırlık ve yergi çağrışımı taşıyabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bulunduğu yerden ayrılmayıp orada kalmayı belirtir."},{"facet_id":"F002","role":"specialization","statement":"Kişi için yerinden veya evinden ayrılmayan ağır kimseyi anlatır."},{"facet_id":"F003","role":"extension","statement":"Develer için su başında kalıp oradan ayrılmamayı anlatır."},{"facet_id":"F004","role":"associated_use","statement":"Evinden ayrılmayan kişi hakkında yergi olarak kullanılabilir."}],"identity_rationale":"Kaynak ifadesi çekirdeği bir yerden ayrılmama olarak kurar ve bunu evinden çıkmayan ağır kişi ile su başında kalan develere uygular. Geçici çerçeve kişi, hayvan ve yergi boyutlarını aynı kalma çekirdeğine bağlı tutar.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yerinden ya da evinden ayrılmayan ağır kimse"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"övgüde gözü pek kişi, yergide evinden ayrılmayan kimse için söylenen söz"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"su başında kalıp oradan ayrılmayan develer"}],"lexicalization_note":"Kişinin yerinden ayrılmaması temel nitelik olarak, ev ve su başı kullanımları ise kendi varlık ve yapı sınırları içinde ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sabit duran kişi, genel yerleşip kalma, savaşta sebat ve uğraşa devam karşılaştırmaları mekânsal kalma çekirdeğini en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Kişi uygulamasında çekirdekler çok yakındır; bu dal hayvan uzantısı ve değerlendirme taşırken komşu dal hareket etmeme karşıtlığını ayrıca içerir.","focus_only":"Kişide ağırlık veya yergi, ayrıca develerin su başında kalması kapsamını taşır.","gloss":"yerinden ayrılmayan varlık ile sabit duran kişi","neighbor_only":"Yalnızca yerinde duran kişi anlamını, hareket etmemeyi olumsuzlayan ayrı bir kullanımla birlikte verir.","neighbor_ref":"root_000599/B010","relation_type":"near_synonym","shared_zone":"Her iki dal da bulunduğu yerden ayrılmayan kişiyi anlatır."},{"boundary_match":"partial","distinction":"Bu dalın kapsamı belirli kişi ve su başı kullanımlarıyla, kimi zaman yergiyle sınırlıdır; komşu dal genel yerleşip kalma anlamını taşır.","focus_only":"Evinden ayrılmayan ağır kişi ve su başında kalan develer gibi belirli uygulamalara sahiptir.","gloss":"belirli yerde kalma ile genel yerleşip kalma","neighbor_only":"Bir yerde kalmayı kişi, deve ve otlak bağlamlarında daha genel olarak kapsar.","neighbor_ref":"root_000026/B003","relation_type":"near_synonym","shared_zone":"İki dalın çekirdeği kişi ya da hayvanın bulunduğu yerde kalıp ayrılmamasıdır."},{"boundary_match":"partial","distinction":"Bu dal mekânsal kalıcılıktır; komşu dal savaşçı kişinin rakibi bırakmayan olumlu sebatıdır.","focus_only":"Fiziksel bir yerde kalmayı ve kimi zaman ağır bulunmayı bildirir.","gloss":"yerinde kalma ile savaşta sebat","neighbor_only":"Savaşta rakipten ayrılmamayı yiğitlik olarak bildirir.","neighbor_ref":"root_001390/B004","relation_type":"near_neighbor","shared_zone":"İki dalda da bir yerden ya da karşı karşıya olunan şeyden ayrılmama öğesi bulunur."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği mekânsal olarak ayrılmamaktır; komşu dal yönelme, uğraş ve düzenli devamı da içine alan daha geniş sürekliliktir.","focus_only":"Bir fiziksel yerden ayrılmama durumunu belirtir.","gloss":"mekânda kalma ile uğraşa devam","neighbor_only":"Bir işe veya şeye yönelip onu sürekli sürdürmeyi de kapsar.","neighbor_ref":"root_001038/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir şeye bağlı kalma ve süreklilik alanındadır."}],"source_phrase_ar":"الأليس الرجل الثقيل الذي لا يبرح مكانه (ayn)؛ الأليس: الذي لا يبرح بيته؛ إبل ليس على الحوض: إذا أقامت عليه فلم تبرحه؛ وبالأليس الذي لا يبرح بيته، وهذا ذم (tahdhib)","source_summary":"Kaynaklar bir yerden ayrılmama çekirdeğinde birleşir; kişi için ağırlık veya evden çıkmama, develer için su başında kalma ve kişi kullanımında yergi ayrıntıları bu çekirdeğe bağlanır.","sources":["AY","TA"],"what_is_ar":"يدخل فيه الأليس بمعنى الرجل الثقيل أو الملازم الذي لا يبرح مكانه أو بيته، وإبل ليس على الحوض إذا أقامت عليه فلم تبرحه، وما ذم به من لا يبرح بيته.","what_is_not_ar":"لا يدخل فيه ثبات الشجاع في الحرب، ولا تحمل الخلق والتغاضي، ولا ضعف الرأي، ولا ليس النحوية."},"support_links":[]},{"boundary":"Fiziksel yük taşıma, insanda güçlüğe katlanma, yumuşak huyluluk ve görmezden gelme birlikte kapsanır; bunlar yerinde kalma veya savaşçı cesareti değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001390/B006","candidate_links":[{"candidate_id":"cand_aaa916deb478185bf2df","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لَّيْسَ","morph_features":"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"95:8:1:2","qac_word_ref":"95:8:1","surface_ar":"لَيْسَ"}],"gloss":"yük taşıma, güçlüğe katlanma ve rahatsızlığı görmezden gelme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Devenin üzerine yüklenen her şeyi taşıyabilmesini belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin güçlüğe katlanan ve yumuşak huylu biri olmasını belirtir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Rahatsız edici bir şeyi görmezden gelip üzerinde durmamayı belirtir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yumuşak huylu kişiyi niteleyen özel bir söz öbeğinde kullanılır."}}],"root_ar":"ل ي س","root_id":"root_001390","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel taşıma ile insana özgü katlanma ve hoşgörülü aşma uzantılarını birlikte göstermek gereken genel açıklamada uygundur.","boundary_detail":"Fiziksel yük taşıma, insanda güçlüğe katlanma, yumuşak huyluluk ve görmezden gelme birlikte kapsanır; bunlar yerinde kalma veya savaşçı cesareti değildir.","branch_image_ar":"تلايس احتمال وتغاض حسن الخلق","concept_gloss":"yük taşıma, güçlüğe katlanma ve rahatsızlığı görmezden gelme","contextual_glosses":[{"applicability":"Kişinin güç bir duruma katlanması veya rahatsız edici bir şeyi büyütmeden geçmesi bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Devenin fiziksel olarak her yükü taşıması anlamını kapsamaz.","preserves":"İnsana özgü katlanma ve görmezden gelme yönlerini korur."},"facet_ids":["F002","F003"],"text":"hoşgörüyle karşılamak","usage_role":"contextual"}],"definition":"Yüklenen şeyi taşıma çekirdeğinden, kişinin güçlüğe katlanıp yumuşak huylu davranmasına ve rahatsız edici bir şeyi görmezden gelerek aşmasına uzanan kullanımları kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Devenin üzerine yüklenen her şeyi taşıyabilmesini belirtir."},{"facet_id":"F002","role":"extension","statement":"Kişinin güçlüğe katlanan ve yumuşak huylu biri olmasını belirtir."},{"facet_id":"F003","role":"extension","statement":"Rahatsız edici bir şeyi görmezden gelip üzerinde durmamayı belirtir."},{"facet_id":"F004","role":"associated_use","statement":"Yumuşak huylu kişiyi niteleyen özel bir söz öbeğinde kullanılır."}],"identity_rationale":"Kaynak ifadesi yalnızca insanın yumuşak huylu oluşunu ve görmezden gelmesini değil, devenin yüklenen her şeyi taşımasını da içerir. Dal korunabilir, ancak fiziksel yük taşıma ile insandaki güçlüğe katlanma ve hoşgörülü davranma aynı üst dayanma ilişkisine bağlı farklı gerçekleşimler olarak ayrılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"üzerine yüklenen her yükü taşıyan deve"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"güçlüğe katlanan ve yumuşak huylu olmak"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"görmezden gelip üzerinde durmamak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yumuşak huylu"}],"lexicalization_note":"Devenin yük taşıması temel fiziksel gerçekleşim, insandaki katlanma ile görmezden gelme ise kendi yapılara bağlı insani gerçekleşimler olarak ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tartışmayı bırakma, sabır, bağışlama ve öfke denetimi karşılaştırmaları yük taşıma ile hoşgörülü katlanma arasındaki özgül bağı en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal görmezden gelmeyi daha geniş taşıma ve yumuşak huyluluk alanına bağlar; komşu dal doğrudan tartışmayı ve kuşkuyu bırakmaya yönelten bir sözdür.","focus_only":"Fiziksel yük taşıma ile yumuşak huylu katlanmayı da kapsar.","gloss":"görmezden gelme ile tartışmayı bırakma","neighbor_only":"Tartışmayı bırakma, kuşkudan uzaklaşma ve karşıdakini hoş görme yönlendirmesi taşır.","neighbor_ref":"root_000769/B007","relation_type":"near_neighbor","shared_zone":"İki dal da rahatsız edici bir şeyi büyütmeden geçme ve katlanma davranışında buluşur."},{"boundary_match":"partial","distinction":"Bu dal yükü üstlenme ve hoşgörülü geçme eksenindedir; komşu dal kişinin kaygı ve yakınma tepkisini dizginlemesine odaklanır.","focus_only":"Yük taşıma ve rahatsızlığı görmezden gelme uzantılarını içerir.","gloss":"katlanma ile kendini tutma","neighbor_only":"Sarsıntı ve yakınma karşısında kişinin kendini tutmasını, akıl veya değer ölçüsüne bağlı sabrı anlatır.","neighbor_ref":"root_000840/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da güçlük karşısında dayanma ve taşkın tepki vermeme alanındadır."},{"boundary_match":"partial","distinction":"Bu dalda görmezden gelme katlanma davranışıdır; komşu dalda asıl işlem kusuru bağışlamak ve kınamayı bırakmaktır.","focus_only":"Katlanma, yumuşak huyluluk ve yük taşıma anlam alanını birlikte kapsar.","gloss":"görmezden gelme ile bağışlama","neighbor_only":"Bir kusuru bağışlayıp kınamaktan vazgeçmeyi ve ondan yüz çevirmeyi belirtir.","neighbor_ref":"root_000867/B002","relation_type":"near_neighbor","shared_zone":"İki dal da rahatsız edici bir davranışın üzerinde durmamayı içerebilir."},{"boundary_match":"field_only","distinction":"Bu dal yük ve güçlüğü taşıma üzerinden kurulur; komşu dalın çekirdeği öfke ve taşkınlığı akılla denetlemektir.","focus_only":"Fiziksel yük taşıma ile bir şeyi görmezden gelmeye kadar uzanır.","gloss":"yumuşak huyluluk ile öfke denetimi","neighbor_only":"Öfke kabarmasını denetleyen ağırbaşlılık ve akla dayalı özdenetimi anlatır.","neighbor_ref":"root_000352/B001","relation_type":"same_field","shared_zone":"İki dal da yumuşak davranma, sabır ve sert tepkiyi önleme alanında buluşur."}],"source_phrase_ar":"الأليس: البعير يحمل كل ما حمل (sihah)؛ تلايس الرجل: إذا كان حمولا حسن الخلق؛ وتلايست عن كذا وكذا: أي غمضت عنه؛ وفلان أليس دهثم: أي حسن الخلق (tahdhib)","source_summary":"Toplu kanıt fiziksel yük taşıma ile insanın güçlüğe katlanması, yumuşak huylu olması ve bir şeyi görmezden gelmesi arasında uzanan bir anlam alanı verir; ayrıntılar tek kaynaklara bölünebilecek ayrı iddialar halinde sunulmamıştır.","sources":["SI","TA"],"what_is_ar":"يدخل فيه تلايس الرجل إذا كان حمولا حسن الخلق، وتلايست عن كذا إذا غمضت عنه، وفلان أليس دهثم أي حسن الخلق، ومعه الأليس من الإبل الذي يحمل كل ما حمل.","what_is_not_ar":"لا يدخل فيه نفي ليس، ولا الاستثناء، ولا الشجاعة، ولا لزوم المكان، ولا ضعف الرأي."},"support_links":["sup_e27ec30ec80adc276402"]},{"boundary":"Dal yalnızca görüşü zayıf kişiyi kapsar; genel akıl eksikliği, budalalık veya kararsızlık ancak ayrıca kanıtlanırsa bu sınıra girer.","branch_kind":"bare","branch_ref":"root_001390/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَّيْسَ","morph_features":"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"95:8:1:2","qac_word_ref":"95:8:1","surface_ar":"لَيْسَ"}],"gloss":"görüşü ve yargısı zayıf kişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin görüş ve yargı gücünün zayıf olmasını belirtir."}}],"root_ar":"ل ي س","root_id":"root_001390","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yalın ve tek çekirdekli kişi niteliğini doğrudan karşılamak için uygundur.","boundary_detail":"Dal yalnızca görüşü zayıf kişiyi kapsar; genel akıl eksikliği, budalalık veya kararsızlık ancak ayrıca kanıtlanırsa bu sınıra girer.","branch_image_ar":"الأليس ضعيف الرأي","concept_gloss":"görüşü ve yargısı zayıf kişi","contextual_glosses":[{"applicability":"Görüş zayıflığının ileriyi sağlıklı değerlendirememe olarak belirdiği bağlamlarda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Görüş zayıflığının öngörü dışındaki bütün biçimlerini kapsamaz.","preserves":"Sağlam değerlendirme yapamama yönünü korur."},"facet_ids":["F001"],"text":"öngörüsüz","usage_role":"contextual"}],"definition":"Sağlam değerlendirme yapamayan, görüşü ve yargısı zayıf kişiyi belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin görüş ve yargı gücünün zayıf olmasını belirtir."}],"identity_rationale":"Kaynak ifadesi anlamı doğrudan görüş ve yargı zayıflığıyla sınırlar. Geçici çerçeve bu kısa ve yalın kişi niteliğini cesaret, yerinde kalma ve dilbilgisel kullanımlardan doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"görüşü zayıf kimse"}],"lexicalization_note":"Tanım, herhangi bir özel söz öbeğinden anlam aktarmadan yalın biçimin görüş zayıflığı anlamıyla sınırlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sezgi zayıflığına, daha geniş eksikliğe ve budalalığa uzanan yakın anlamlar ile sağlam görüş karşıtlığı dal sınırını en açık biçimde belirledi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal görüş zayıflığıyla sınırlıdır; komşu dal sezgi ve kestirim yetisinin zayıflığını veya yanılmasını da içerir.","focus_only":"Yalnızca görüş ve yargı zayıflığını bildirir.","gloss":"görüş zayıflığı ile sezgi zayıflığı","neighbor_only":"Görüşün yanında sezgi zayıflığı ve yanılmasını da kapsar.","neighbor_ref":"root_001193/B001","relation_type":"near_synonym","shared_zone":"İki dal da kişinin doğru değerlendirme gücündeki eksikliği anlatır."},{"boundary_match":"partial","distinction":"Bu dal yalnızca görüş gücünü niteler; komşu dal akıl ve değer alanına uzanan daha geniş bir eksiklik çerçevesi taşır.","focus_only":"Görüş zayıflığını tek başına kişi niteliği olarak verir.","gloss":"zayıf görüş ile daha geniş eksiklik","neighbor_only":"Görüş kusurunu akıl veya değer alanındaki eksikliklere kadar genişletir.","neighbor_ref":"root_001072/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da görüşün zayıf ve yetersiz olmasını kapsar."},{"boundary_match":"partial","distinction":"Bu dalın kanıtı görüş zayıflığıyla sınırlıdır; komşu dal daha ağır bir zihinsel yetersizlik yargısı ekler.","focus_only":"Budalalık yargısı eklemeden görüşün zayıflığını belirtir.","gloss":"zayıf görüş ile budalalık","neighbor_only":"Görüş zayıflığını budalalıkla birlikte veya onun eşdeğeri olarak sunar.","neighbor_ref":"root_001360/B003","relation_type":"near_synonym","shared_zone":"İki dal da görüşü zayıf kişiyi ifade edebilir."},{"boundary_match":"opposed","distinction":"Bu dal değerlendirme gücünün olumsuz ucunu, komşu dal ise sağlam ve iyi görüşten oluşan olumlu ucunu temsil eder.","focus_only":"Görüşün zayıf ve güvenilmez olmasını bildirir.","gloss":"zayıf görüş ile sağlam görüş","neighbor_only":"Görüşün sağlam, dengeli ve iyi olmasını bildirir.","neighbor_ref":"root_000599/B008","relation_type":"polarity_pair","shared_zone":"İki dal da kişinin görüş ve değerlendirme niteliğini aynı eksende belirler."}],"source_phrase_ar":"الأليس الضعيف الرأي (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, biçimi görüşü ve yargısı zayıf kişi olarak açıklar."}],"source_summary":"Bu dal için kaynaklar arasında ortaklaştırılacak ayrı bir anlatım yoktur; görüş zayıflığı anlamı tek tanıklıkla sınırlıdır.","sources":["AY"],"what_is_ar":"يدخل فيه الأليس بمعنى ضعيف الرأي.","what_is_not_ar":"لا يدخل فيه الشجاع الأليس، ولا الملازم الذي لا يبرح، ولا ليس النحوية."},"support_links":[]},{"boundary":"Dal, koruyucu kıskançlık göstermeyen erkeğe yönelik yergi ve alayı kapsar; aynı biçimin yiğitlik övgüsü bu dala alınmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001390/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَّيْسَ","morph_features":"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"95:8:1:2","qac_word_ref":"95:8:1","surface_ar":"لَيْسَ"}],"gloss":"ailesine karşı koruyucu kıskançlık göstermeyen erkeğe yönelik alaycı yergi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ailesine karşı koruyucu kıskançlık göstermeyen erkeği aşağılayıcı biçimde niteler."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu nitelikteki kişiye yönelik alaycı ve yergili bir sözde kullanılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı biçimin başka bir dalda övgü bildirebilmesi, buradaki yergi anlamının bağlamsal sınırını gösterir."}}],"root_ar":"ل ي س","root_id":"root_001390","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişideki eksikliği ve bu eksikliğin aşağılayıcı, alaycı değerlendirilmesini birlikte aktarmak gereken genel açıklamada uygundur.","boundary_detail":"Dal, koruyucu kıskançlık göstermeyen erkeğe yönelik yergi ve alayı kapsar; aynı biçimin yiğitlik övgüsü bu dala alınmaz.","branch_image_ar":"الأليس ذم لمن لا يغار","concept_gloss":"ailesine karşı koruyucu kıskançlık göstermeyen erkeğe yönelik alaycı yergi","contextual_glosses":[{"applicability":"Kişiye yüklenen olumsuz niteliği açık ve doğal Türkçeyle anlatmak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sözün alaycı kalıbını ve açık yergi tonunu tam olarak taşımaz.","preserves":"Erkeğin ailesine karşı koruyucu kıskançlık göstermemesi niteliğini korur."},"facet_ids":["F001"],"text":"ailesini kıskanıp korumayan adam","usage_role":"explanatory"}],"definition":"Ailesini kıskanıp koruma duyarlılığı göstermeyen erkeği aşağılayarak niteler ve bu kişiye yönelik alaycı bir yergi sözü kurar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ailesine karşı koruyucu kıskançlık göstermeyen erkeği aşağılayıcı biçimde niteler."},{"facet_id":"F002","role":"associated_use","statement":"Bu nitelikteki kişiye yönelik alaycı ve yergili bir sözde kullanılır."},{"facet_id":"F003","role":"source_variant","statement":"Aynı biçimin başka bir dalda övgü bildirebilmesi, buradaki yergi anlamının bağlamsal sınırını gösterir."}],"identity_rationale":"Kaynak ifadesi bu dalda ailesini kıskanıp koruma duyarlılığı göstermeyen erkeğe yöneltilen alaycı yergiyi açıkça verir. Aynı ifade biçimin övgü ve yergi anlamlarına girebildiğini de not eder; bu dal yalnızca yergi tarafını temsil etmeli, övgüdeki yiğitlik ayrı dalda kalmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ailesine karşı koruyucu kıskançlık göstermediği için alay edilen erkek"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ailesine karşı koruyucu kıskançlık göstermeyen erkeği alaya alan yergi sözü"}],"lexicalization_note":"Kişiye yüklenen olumsuz nitelik temel anlam, alaycı yergi sözü ise yalnızca kendi söz öbeğine bağlı kullanım olarak ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eş anlamlı kişi niteliği, koruyucu kıskançlık karşıtı ve iki genel yergi alanı bu özel aşağılamanın sınırını en iyi belirledi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek kişi niteliği ve değerlendirme sınırı aynıdır; bu daldaki alaycı söz yalnızca kullanım örneğidir ve eş anlamlılığı bozmaz.","focus_only":null,"gloss":"koruyucu kıskançlığı olmayan erkek","neighbor_only":null,"neighbor_ref":"root_001450/B014","relation_type":"synonym","shared_zone":"İki dal da ailesine karşı koruyucu kıskançlık göstermeyen erkeği aşağılayıcı biçimde belirtir."},{"boundary_match":"opposed","distinction":"Bu dal niteliğin yokluğunu aşağılayıcı biçimde bildirir; komşu dal aynı niteliğin varlığını ve bunu taşıyan kişiyi belirtir.","focus_only":"Ailesine karşı koruyucu kıskançlık göstermeyen erkeği yerer.","gloss":"koruyucu kıskançlık eksikliği ile varlığı","neighbor_only":"Ailesine karşı koruyucu kıskançlık gösteren kişiyi niteler.","neighbor_ref":"root_001119/B004","relation_type":"polarity_pair","shared_zone":"İki dal da kişinin ailesine yönelik koruyucu kıskançlık niteliğini aynı eksende değerlendirir."},{"boundary_match":"field_only","distinction":"Bu dal yerginin hedefini koruyucu kıskançlık eksikliğiyle sınırlar; komşu dal herhangi bir kusura yönelen genel ayıplamadır.","focus_only":"Belirli bir ailevi tutum eksikliğini hedef alan yergidir.","gloss":"özel yergi ile genel ayıplama","neighbor_only":"Kusurun türünü sınırlamadan ayıplama, yerme ve utandırma eylemlerini genel olarak kapsar.","neighbor_ref":"root_001066/B012","relation_type":"same_field","shared_zone":"Her iki dal da kişiyi kusuru nedeniyle aşağılayıp yerme alanındadır."},{"boundary_match":"field_only","distinction":"Bu dal belirli davranış eksikliğini ve alaycı hitabı anlatır; komşu dal kusurun kendisini ve doğurduğu genel yerilmeyi daha geniş biçimde kapsar.","focus_only":"Belirli bir erkeği ailevi tutumu nedeniyle alaya alır.","gloss":"belirli alaycı yergi ile genel kusur","neighbor_only":"Kişiye utanç ve küçümsenme getiren kusur ile genel yerme sonucunu kapsar.","neighbor_ref":"root_000506/B001","relation_type":"same_field","shared_zone":"İki dal da kusur, yerme ve küçümseme alanında buluşur."}],"source_phrase_ar":"الأليس: الديوثي الذي لا يغار ويتهزأ به؛ فيقال: هو أليس بورك فيه؛ فالليس يدخل في المعنيين: في المدح والذم (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, ailesine karşı koruyucu kıskançlık göstermeyen erkeğin alayla yerildiğini ve aynı biçimin başka bağlamda övgü de taşıyabildiğini bildirir."}],"source_summary":"Bu dal için kaynaklar arasında ortaklaştırılacak ayrı bir anlatım yoktur; aşağılayıcı kişi niteliği ve alaycı söz tek tanıklıkla sınırlıdır.","sources":["TA"],"what_is_ar":"يدخل فيه قول بعض الأعراب الأليس الديوثي الذي لا يغار، وما يتصل بالتهزؤ والذم في قولهم هو أليس بورك فيه.","what_is_not_ar":"لا يدخل فيه الشجاع الممدوح، ولا الملازم للمكان إلا إذا أريد ذمه من جهة لزوم البيت، ولا استعمال ليس النحوي."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["95:8:1"],"branch_refs":[],"candidate_id":"cand_d22eca5bfe344289d091","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001390"],"scope":"focus_ayah","source_local_id":"95:8:1:boundary-verdict-shift","source_type":"word_analysis","support_ids":["sup_6d0604bc571db88ae690","sup_cdce904c05810b707f17"],"title":"denial is moved before judgment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:1","qac_refs":["95:8:1:1","95:8:1:2"],"status":"accepted"}},{"anchor_refs":["95:8:1"],"branch_refs":[],"candidate_id":"cand_e0bc8d45f29c766ad85b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001390"],"scope":"focus_ayah","source_local_id":"95:8:1:compact-capstone-formula","source_type":"word_analysis","support_ids":["sup_13efd381b29f4737fc84","sup_cdce904c05810b707f17"],"title":"short ayah carries a formulaic closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:1","qac_refs":["95:8:1:1","95:8:1:2"],"status":"accepted"}},{"anchor_refs":["95:8:1"],"branch_refs":[],"candidate_id":"cand_87264681329aea7799de","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001390"],"scope":"focus_ayah","source_local_id":"95:8:1:lam-sound-link","source_type":"word_analysis","support_ids":["sup_cdce904c05810b707f17","sup_f4fb7a8be69d4c765dd6"],"title":"sound links negator and divine name","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:1","qac_refs":["95:8:1:1","95:8:1:2"],"status":"accepted"}},{"anchor_refs":["95:8:1"],"branch_refs":[],"candidate_id":"cand_372a3bbd2092aeace62c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001390"],"scope":"focus_ayah","source_local_id":"95:8:1:laysa-predicate-scope","source_type":"word_analysis","support_ids":["sup_cdce904c05810b707f17","sup_e6e2395c8c501c25a22d"],"title":"copular negation scopes over the full predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:1","qac_refs":["95:8:1:1","95:8:1:2"],"status":"accepted"}},{"anchor_refs":["95:8:1"],"branch_refs":[],"candidate_id":"cand_5322f291dee55f6ececc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001390"],"scope":"focus_ayah","source_local_id":"95:8:1:rhetorical-affirmation","source_type":"word_analysis","support_ids":["sup_2f4ec6a596255f77c469","sup_cdce904c05810b707f17"],"title":"negative question demands assent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:1","qac_refs":["95:8:1:1","95:8:1:2"],"status":"accepted"}},{"anchor_refs":["95:8:1"],"branch_refs":[],"candidate_id":"cand_ab569fafba07d4c2e9fa","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001390"],"scope":"focus_ayah","source_local_id":"95:8:1:surah-closing-turn","source_type":"word_analysis","support_ids":["sup_7f2fcc3513a32fbfd550","sup_cdce904c05810b707f17"],"title":"accusation becomes universal recognition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:1","qac_refs":["95:8:1:1","95:8:1:2"],"status":"accepted"}},{"anchor_refs":["95:8:1"],"branch_refs":[],"candidate_id":"cand_cd13d3d836c74f9b8f81","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001390"],"scope":"focus_ayah","source_local_id":"95:8:1:uninflected-timeless-frame","source_type":"word_analysis","support_ids":["sup_863d8448e6279c163df2","sup_cdce904c05810b707f17"],"title":"uninflected form avoids event-tense framing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:1","qac_refs":["95:8:1:1","95:8:1:2"],"status":"accepted"}},{"anchor_refs":["95:8:2"],"branch_refs":[],"candidate_id":"cand_c4000c0da40f415b17dc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:8:2:creator-named-as-judge","source_type":"word_analysis","support_ids":["sup_3e3a4ba7de797f9ca3e9","sup_e3bea557a634347bdb01"],"title":"earlier creator is named at judgment close","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:2","qac_refs":["95:8:2:1"],"status":"accepted"}},{"anchor_refs":["95:8:2"],"branch_refs":[],"candidate_id":"cand_ba09bbbaf09eeddfad5f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:8:2:judgment-predicate-selection","source_type":"word_analysis","support_ids":["sup_0d2fa6ca57c5c4556f52","sup_e3bea557a634347bdb01"],"title":"divine name is qualified by judgment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:2","qac_refs":["95:8:2:1"],"status":"accepted"}},{"anchor_refs":["95:8:2"],"branch_refs":[],"candidate_id":"cand_4fd6eaae5032c8c5f96c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:8:2:named-subject-of-laysa","source_type":"word_analysis","support_ids":["sup_d046ec2fd6c22c4d2c42","sup_e3bea557a634347bdb01"],"title":"proper name anchors the predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:2","qac_refs":["95:8:2:1"],"status":"accepted"}},{"anchor_refs":["95:8:2"],"branch_refs":[],"candidate_id":"cand_ad8475db517f9e4c05b2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:8:2:proper-name-not-common-deity","source_type":"word_analysis","support_ids":["sup_9b632081f80c37f1a219","sup_e3bea557a634347bdb01"],"title":"proper name blocks generic deity reading","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:2","qac_refs":["95:8:2:1"],"status":"accepted"}},{"anchor_refs":["95:8:2"],"branch_refs":[],"candidate_id":"cand_4e6b7c90586469deee2e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:8:2:root-background-pressure","source_type":"word_analysis","support_ids":["sup_b7999273ec332ac347b4","sup_e3bea557a634347bdb01"],"title":"root dispute remains background only","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:2","qac_refs":["95:8:2:1"],"status":"accepted"}},{"anchor_refs":["95:8:2"],"branch_refs":[],"candidate_id":"cand_01bc9769a0cac15c82fc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:8:2:trustworthy-judgment-frame","source_type":"word_analysis","support_ids":["sup_97161b80ed255c035742","sup_e3bea557a634347bdb01"],"title":"trustworthy opening meets named judge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:2","qac_refs":["95:8:2:1"],"status":"accepted"}},{"anchor_refs":["95:8:3"],"branch_refs":[],"candidate_id":"cand_377ac239a915f405aa30","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:8:3:genitive-government","source_type":"word_analysis","support_ids":["sup_1527f2b7cc1f6ad5b130","sup_9c653b433c272c6d0168"],"title":"semantic lightness still governs case","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:3","qac_refs":["95:8:3:1"],"status":"accepted"}},{"anchor_refs":["95:8:3"],"branch_refs":[],"candidate_id":"cand_1ca0e03663632ba37aac","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:8:3:proclitic-fusion","source_type":"word_analysis","support_ids":["sup_9c653b433c272c6d0168","sup_b7ab0839c93307e6145e"],"title":"particle fuses to the elative","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:3","qac_refs":["95:8:3:1"],"status":"accepted"}},{"anchor_refs":["95:8:3"],"branch_refs":[],"candidate_id":"cand_7a9f914bdc4dc3be0c23","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:8:3:reinforcing-bāʾ-predicate","source_type":"word_analysis","support_ids":["sup_9c653b433c272c6d0168","sup_e051ad868fbfef107e60"],"title":"bāʾ reinforces the laysa predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:3","qac_refs":["95:8:3:1"],"status":"accepted"}},{"anchor_refs":["95:8:3"],"branch_refs":[],"candidate_id":"cand_66aa447cff00d7fcb6be","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:8:3:subject-to-predicate-pivot","source_type":"word_analysis","support_ids":["sup_9c653b433c272c6d0168","sup_c3dfad1ff2947f4f9326"],"title":"particle pivots from subject to attribute","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:3","qac_refs":["95:8:3:1"],"status":"accepted"}},{"anchor_refs":["95:8:4"],"branch_refs":[],"candidate_id":"cand_4c8963ad7365fcf298ff","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000348"],"scope":"focus_ayah","source_local_id":"95:8:4:class-apex-elative","source_type":"word_analysis","support_ids":["sup_9deb4ac64fa8384fdc65","sup_e50089fb135d43f72bff"],"title":"elative makes an apex-of-class claim","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:4","qac_refs":["95:8:3:2"],"status":"accepted"}},{"anchor_refs":["95:8:4"],"branch_refs":[],"candidate_id":"cand_a1d56ac66ec12be2d997","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000348"],"scope":"focus_ayah","source_local_id":"95:8:4:judicial-discourse-closure","source_type":"word_analysis","support_ids":["sup_e50089fb135d43f72bff","sup_ffc5edaaf0c58492170c"],"title":"final predicate turns denial into verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:4","qac_refs":["95:8:3:2"],"status":"accepted"}},{"anchor_refs":["95:8:4"],"branch_refs":[],"candidate_id":"cand_d807d92ffdce2a6c1ad5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000348"],"scope":"focus_ayah","source_local_id":"95:8:4:nested-genitive-dependency","source_type":"word_analysis","support_ids":["sup_6f5e4eeb61cb94044008","sup_e50089fb135d43f72bff"],"title":"governed and governing at once","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:4","qac_refs":["95:8:3:2"],"status":"accepted"}},{"anchor_refs":["95:8:4"],"branch_refs":[],"candidate_id":"cand_0ee33fde025524b54c72","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000348"],"scope":"focus_ayah","source_local_id":"95:8:4:rare-elative-profile","source_type":"word_analysis","support_ids":["sup_1d2b3edb26b2f2beda02","sup_e50089fb135d43f72bff"],"title":"rare elative sharpens the close","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:4","qac_refs":["95:8:3:2"],"status":"accepted"}},{"anchor_refs":["95:8:4"],"branch_refs":[],"candidate_id":"cand_c47da8d56f4e8df90b58","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000348"],"scope":"focus_ayah","source_local_id":"95:8:4:root-form-echo","source_type":"word_analysis","support_ids":["sup_a2f695200de1e2f4dd0e","sup_e50089fb135d43f72bff"],"title":"same root shifts from degree to class","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:4","qac_refs":["95:8:3:2"],"status":"accepted"}},{"anchor_refs":["95:8:4"],"branch_refs":[],"candidate_id":"cand_d4d4e4d6b6b77a217250","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000348"],"scope":"focus_ayah","source_local_id":"95:8:4:semantic-compression","source_type":"word_analysis","support_ids":["sup_35ea3a64ca537c1fe4a4","sup_e50089fb135d43f72bff"],"title":"judgment gathers wisdom, precision, and restraint","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:4","qac_refs":["95:8:3:2"],"status":"accepted"}},{"anchor_refs":["95:8:5"],"branch_refs":[],"candidate_id":"cand_b04852b52ff5d4f5c5af","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000348"],"scope":"focus_ayah","source_local_id":"95:8:5:definite-active-agent-class","source_type":"word_analysis","support_ids":["sup_b266ac13cc4f59857163","sup_bfeb01377850aedbdfef"],"title":"definite plural names active judges","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:5","qac_refs":["95:8:4:1","95:8:4:2"],"status":"accepted"}},{"anchor_refs":["95:8:5"],"branch_refs":[],"candidate_id":"cand_27d4b153b71d9d446479","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000348"],"scope":"focus_ayah","source_local_id":"95:8:5:final-attribute-seal","source_type":"word_analysis","support_ids":["sup_b266ac13cc4f59857163","sup_cf2e7205eb40d929c371"],"title":"surah lands on judgment authority","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:5","qac_refs":["95:8:4:1","95:8:4:2"],"status":"accepted"}},{"anchor_refs":["95:8:5"],"branch_refs":[],"candidate_id":"cand_061f01d44b61c1cdd62c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000348"],"scope":"focus_ayah","source_local_id":"95:8:5:governance-and-restraint-range","source_type":"word_analysis","support_ids":["sup_34acc2c1c2babc02a58f","sup_b266ac13cc4f59857163"],"title":"judges broaden to rulers and limit-setters","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:5","qac_refs":["95:8:4:1","95:8:4:2"],"status":"accepted"}},{"anchor_refs":["95:8:5"],"branch_refs":[],"candidate_id":"cand_c46b69cb7d2f652b1390","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000348"],"scope":"focus_ayah","source_local_id":"95:8:5:idafa-class-complement","source_type":"word_analysis","support_ids":["sup_9599429a4a1c3ecc3adc","sup_b266ac13cc4f59857163"],"title":"genitive tail completes the superlative","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:5","qac_refs":["95:8:4:1","95:8:4:2"],"status":"accepted"}},{"anchor_refs":["95:8:5"],"branch_refs":[],"candidate_id":"cand_83fe5fd51aadc90d9068","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000348"],"scope":"focus_ayah","source_local_id":"95:8:5:recognized-divine-judgment-pairing","source_type":"word_analysis","support_ids":["sup_b266ac13cc4f59857163","sup_d756b17f96d0272e3ff6"],"title":"limited participle carries familiar affirmation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:5","qac_refs":["95:8:4:1","95:8:4:2"],"status":"accepted"}},{"anchor_refs":["95:8:5"],"branch_refs":[],"candidate_id":"cand_f905240cd79b16509dd2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000348"],"scope":"focus_ayah","source_local_id":"95:8:5:root-echo-quality-to-class","source_type":"word_analysis","support_ids":["sup_8c7ecc2de3991ea0e065","sup_b266ac13cc4f59857163"],"title":"root echo moves into agent-class","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:8:5","qac_refs":["95:8:4:1","95:8:4:2"],"status":"accepted"}},{"anchor_refs":["95:8:1"],"branch_refs":[],"candidate_id":"cand_f8b19d60a8ebd7d4d9d1","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001390"],"scope":"focus_ayah","source_local_id":"95:8:1:2","source_type":"qac_morpheme","support_ids":["sup_6560e14dcba310094930"],"title":"QAC root occurrence: ل ي س","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["95:8:2"],"branch_refs":[],"candidate_id":"cand_104c2bfbea7a7371a700","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000047"],"scope":"focus_ayah","source_local_id":"95:8:2:1","source_type":"qac_morpheme","support_ids":["sup_5bd22b196ae10682d203"],"title":"QAC root occurrence: ء ل ه","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["95:8:3"],"branch_refs":[],"candidate_id":"cand_8dc6c01b806ac3a8d942","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000348"],"scope":"focus_ayah","source_local_id":"95:8:3:2","source_type":"qac_morpheme","support_ids":["sup_0409f70397442653a34c"],"title":"QAC root occurrence: ح ك م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["95:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"95:8","branch_refs":["root_000047/B002","root_000348/B002","root_001390/B001"],"candidate_id":"cand_5f7ec71ec2a78a45509d","commentary_obligation":"review","hft_ref":"hft_e7e85370288a0fda07aa","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_emphatic_adjudication","source_type":"hft","support_ids":["sup_9591c7e41a55ecca2efb"],"title":"baseline_emphatic_adjudication","trust":"legacy_unbound"},{"anchor_refs":["95:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"95:8","branch_refs":["root_000348/B001","root_000348/B006"],"candidate_id":"cand_5d5b596d8050b161ed4a","commentary_obligation":"review","hft_ref":"hft_9ddb70be16f27c7f17cd","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_corrective_restraint","source_type":"hft","support_ids":["sup_894381612f755e3fff01"],"title":"baseline_corrective_restraint","trust":"legacy_unbound"},{"anchor_refs":["95:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"95:8","branch_refs":["root_000348/B003","root_000348/B004"],"candidate_id":"cand_1bd3cf21390948048637","commentary_obligation":"review","hft_ref":"hft_828e07c5d8f3bdfff430","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_decisive_perfection","source_type":"hft","support_ids":["sup_6651a80eed86d23a341f"],"title":"baseline_decisive_perfection","trust":"legacy_unbound"},{"anchor_refs":["95:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"95:8","branch_refs":["root_000348/B005","root_001390/B001"],"candidate_id":"cand_04abacf600b6ffea90ce","commentary_obligation":"review","hft_ref":"hft_2d8a93246788633b72f1","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_entrusted_decision","source_type":"hft","support_ids":["sup_0cddc03f956e5a2a9f09"],"title":"baseline_entrusted_decision","trust":"legacy_unbound"},{"anchor_refs":["95:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"95:8","branch_refs":["root_000348/B003","root_001390/B006"],"candidate_id":"cand_aaa916deb478185bf2df","commentary_obligation":"review","hft_ref":"hft_eada79673d9c284071d5","kind":"surprising_outlier","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:outlier_forbearing_load_bearing_judge","source_type":"hft","support_ids":["sup_e27ec30ec80adc276402"],"title":"outlier_forbearing_load_bearing_judge","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"أَلَيْسَ ٱللَّهُ بِأَحْكَمِ ٱلْحَٰكِمِينَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|A:INTG+","morpheme_role":"PREFIX","pos":"INTG","qac_ref":"95:8:1:1","qac_word_ref":"95:8:1","root_ar":"","surface_ar":"أَ"},{"lemma_ar":"لَّيْسَ","morph_features":"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"95:8:1:2","qac_word_ref":"95:8:1","root_ar":"ل ي س","surface_ar":"لَيْسَ"},{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|NOM","morpheme_role":"STEM","pos":"PN","qac_ref":"95:8:2:1","qac_word_ref":"95:8:2","root_ar":"ء ل ه","surface_ar":"ٱللَّهُ"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"95:8:3:1","qac_word_ref":"95:8:3","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"أَحْكَم","morph_features":"STEM|POS:N|LEM:>aHokam|ROOT:Hkm|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:8:3:2","qac_word_ref":"95:8:3","root_ar":"ح ك م","surface_ar":"أَحْكَمِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"95:8:4:1","qac_word_ref":"95:8:4","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"حَٰكِمِين","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ha`kimiyn|ROOT:Hkm|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:8:4:2","qac_word_ref":"95:8:4","root_ar":"ح ك م","surface_ar":"حَٰكِمِينَ"}],"word_analysis_qac_refs":[["95:8:1:1","95:8:1:2"],["95:8:2:1"],["95:8:3:1"],["95:8:3:2"],["95:8:4:1","95:8:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["95:8:1","95:8:2","95:8:3","95:8:4","95:8:5"]},"focus_surface_evidence":{"arabic_uthmani":"أَلَيْسَ ٱللَّهُ بِأَحْكَمِ ٱلْحَٰكِمِينَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|A:INTG+","morpheme_role":"PREFIX","pos":"INTG","qac_ref":"95:8:1:1","qac_word_ref":"95:8:1","root_ar":"","surface_ar":"أَ"},{"lemma_ar":"لَّيْسَ","morph_features":"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"95:8:1:2","qac_word_ref":"95:8:1","root_ar":"ل ي س","surface_ar":"لَيْسَ"},{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|NOM","morpheme_role":"STEM","pos":"PN","qac_ref":"95:8:2:1","qac_word_ref":"95:8:2","root_ar":"ء ل ه","surface_ar":"ٱللَّهُ"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"95:8:3:1","qac_word_ref":"95:8:3","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"أَحْكَم","morph_features":"STEM|POS:N|LEM:>aHokam|ROOT:Hkm|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:8:3:2","qac_word_ref":"95:8:3","root_ar":"ح ك م","surface_ar":"أَحْكَمِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"95:8:4:1","qac_word_ref":"95:8:4","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"حَٰكِمِين","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ha`kimiyn|ROOT:Hkm|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:8:4:2","qac_word_ref":"95:8:4","root_ar":"ح ك م","surface_ar":"حَٰكِمِينَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["95:8:1:1","95:8:1:2"],["95:8:2:1"],["95:8:3:1"],["95:8:3:2"],["95:8:4:1","95:8:4:2"]],"word_analysis_refs":["95:8:1","95:8:2","95:8:3","95:8:4","95:8:5"],"word_rows":[{"analysis_record_ref":"95:8:1","analytic_gloss_range_en":"rhetorical negative interrogative built on the copular negator laysa, governing a subject and bāʾ-marked predicate","analytic_root_gloss_range_en":"local branch is the fixed negating copular verb; other lexical branches such as exception, bravery, remaining in place, forbearance, or weak judgment are not active here","qac_refs":["95:8:1:1","95:8:1:2"],"root":{"arabic":"ل ي س","transliteration":"l-y-s"},"surface":{"arabic":"أَلَيْسَ","transliteration":"ʾa-laysa"}},{"analysis_record_ref":"95:8:2","analytic_gloss_range_en":"proper divine name functioning as the nominative subject of the laysa clause and bearer of the final judgment predicate","analytic_root_gloss_range_en":"proper-name usage fixes the referent; proposed worship and bewilderment root pressures may remain as background but do not replace the local proper-name function","qac_refs":["95:8:2:1"],"root":{"arabic":"أ ل ه","transliteration":"ʾ-l-h"},"surface":{"arabic":"ٱللَّهُ","transliteration":"allāhu"}},{"analysis_record_ref":"95:8:3","analytic_gloss_range_en":"bāʾ zāʾida in the laysa predicate, reinforcing negation while governing the following superlative as genitive","analytic_root_gloss_range_en":null,"qac_refs":["95:8:3:1"],"root":{},"surface":{"arabic":"بِ","transliteration":"bi"}},{"analysis_record_ref":"95:8:4","analytic_gloss_range_en":"genitive elative/superlative construct head, locally the apex term in the phrase 'most/firmest/most wisely judging of judges'","analytic_root_gloss_range_en":"root range includes judging, wisdom, firm making, restraint, and delegation; local construction selects the judgment-class superlative while allowing wisdom, precision, and restraint pressure","qac_refs":["95:8:3:2"],"root":{"arabic":"ح ك م","transliteration":"ḥ-k-m"},"surface":{"arabic":"أَحْكَمِ","transliteration":"ʾaḥkami"}},{"analysis_record_ref":"95:8:5","analytic_gloss_range_en":"definite masculine plural active participle in genitive, naming the judging/ruling agent-class surpassed by the elative","analytic_root_gloss_range_en":"root range includes judges, rulers, arbiters, governors, wise adjudicators, and limit-setters; local form selects active judging agents as the class complement","qac_refs":["95:8:4:1","95:8:4:2"],"root":{"arabic":"ح ك م","transliteration":"ḥ-k-m"},"surface":{"arabic":"ٱلْحَٰكِمِينَ","transliteration":"al-ḥākimīna"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["95:8"],"branch_refs":["root_000047/B002","root_000348/B002","root_001390/B001"],"candidate_id":"cand_5f7ec71ec2a78a45509d","evidence_scope":"focus_ayah","hft_ref":"hft_e7e85370288a0fda07aa","item_id":"baseline_emphatic_adjudication","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_emphatic_adjudication","support_id":"sup_9591c7e41a55ecca2efb"},{"anchor_refs":["95:8"],"branch_refs":["root_000348/B001","root_000348/B006"],"candidate_id":"cand_5d5b596d8050b161ed4a","evidence_scope":"focus_ayah","hft_ref":"hft_9ddb70be16f27c7f17cd","item_id":"baseline_corrective_restraint","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_corrective_restraint","support_id":"sup_894381612f755e3fff01"},{"anchor_refs":["95:8"],"branch_refs":["root_000348/B003","root_000348/B004"],"candidate_id":"cand_1bd3cf21390948048637","evidence_scope":"focus_ayah","hft_ref":"hft_828e07c5d8f3bdfff430","item_id":"baseline_decisive_perfection","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_decisive_perfection","support_id":"sup_6651a80eed86d23a341f"},{"anchor_refs":["95:8"],"branch_refs":["root_000348/B005","root_001390/B001"],"candidate_id":"cand_04abacf600b6ffea90ce","evidence_scope":"focus_ayah","hft_ref":"hft_2d8a93246788633b72f1","item_id":"baseline_entrusted_decision","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_entrusted_decision","support_id":"sup_0cddc03f956e5a2a9f09"},{"anchor_refs":["95:8"],"branch_refs":["root_000348/B003","root_001390/B006"],"candidate_id":"cand_aaa916deb478185bf2df","evidence_scope":"focus_ayah","hft_ref":"hft_eada79673d9c284071d5","item_id":"outlier_forbearing_load_bearing_judge","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_forbearing_load_bearing_judge","support_id":"sup_e27ec30ec80adc276402"}],"diagnostics":[],"lane_counts":{"global":9,"macro":12,"micro":5},"packet_summary":{"ayah_count":8,"focus_ref":"95:8","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ر د د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000555","furuq_root_norm":"ر د د","furuq_source_root_norm":"ر د د","is_dominant":true,"target_occurrences":52,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001413","furuq_root_norm":"م ر د","furuq_source_root_norm":"م ر د","is_dominant":false,"target_occurrences":5,"target_rank":2}]}],"window":["95:1","95:2","95:3","95:4","95:5","95:6","95:7","95:8"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"95:8","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":17,"unstructured_record_count":0},"identity":{"ayah_ref":"95:8","lane":"micro","linguistic_source_ref":"95:8","surface_ref":"95:8","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"95:8","target_tokens":[["Allah",["95:8:2"]],["hüküm",["95:8:4"]],["verenlerin",["95:8:4"]],["en",["95:8:3"]],["iyi",["95:8:3"]],["hüküm",["95:8:4"]],["vereni",["95:8:4"]],["değil",["95:8:1"]],["midir",["95:8:1"]]],"text":"Allah hüküm verenlerin en iyi hüküm vereni değil midir?"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":8,"id":"s095-p01-001-008","label":"Whole surah","number":1,"refs":["95:1","95:2","95:3","95:4","95:5","95:6","95:7","95:8"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"95:8:3:2","source_type":"qac_morpheme","support_id":"sup_0409f70397442653a34c","text":"{\"lemma_ar\":\"أَحْكَم\",\"morph_features\":\"STEM|POS:N|LEM:>aHokam|ROOT:Hkm|MS|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"95:8:3:2\",\"qac_word_ref\":\"95:8:3\",\"root_ar\":\"ح ك م\",\"surface_ar\":\"أَحْكَمِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:2:judgment-predicate-selection","source_type":"word_analysis","support_id":"sup_0d2fa6ca57c5c4556f52","text":"{\"blocking_evidence\":null,\"headline\":\"divine name is qualified by judgment\",\"reader_payoff\":\"The reader notices that the divine name is locally presented through the judgment-and-wisdom field rather than through another divine attribute.\",\"reason\":\"The predicate governed by the laysa frame is the {{ar:ح ك م}} ({{tr:ḥ-k-m}}) superlative expression; co-occurrence claims support the field as familiar while the exact elative construction remains distinctive.\",\"representative_source_ids\":[\"QS-52e5942a\",\"MS-af5813da\",\"QI-05a2cc71\",\"QI-e686b070\",\"MI-2c2271a1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:1:compact-capstone-formula","source_type":"word_analysis","support_id":"sup_13efd381b29f4737fc84","text":"{\"blocking_evidence\":null,\"headline\":\"short ayah carries a formulaic closure\",\"reader_payoff\":\"The reader notices that the five-word ayah uses a recognizable divine-attribute question formula as a compact capstone.\",\"reason\":\"The formula claim is consistent with the laysa-plus-divine-name frame; the concrete parallels must remain parallels rather than controls over the local parse (11:90; 75:40).\",\"representative_source_ids\":[\"QS-c6c2ce7f\",\"MI-5d53ffd3\",\"MT-48fc3a28\",\"QE-70a551e1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:3:genitive-government","source_type":"word_analysis","support_id":"sup_1527f2b7cc1f6ad5b130","text":"{\"blocking_evidence\":null,\"headline\":\"semantic lightness still governs case\",\"reader_payoff\":\"The reader notices that a one-letter particle can be semantically light while visibly controlling the case-form of the superlative.\",\"reason\":\"The preposition governs {{ar:أَحْكَمِ}} ({{tr:ʾaḥkami}}) as genitive even when its semantic function is reinforcement.\",\"representative_source_ids\":[\"MG-765474c7\",\"QF-f2a68d4c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:4:rare-elative-profile","source_type":"word_analysis","support_id":"sup_1d2b3edb26b2f2beda02","text":"{\"blocking_evidence\":null,\"headline\":\"rare elative sharpens the close\",\"reader_payoff\":\"The reader notices that a common judgment field culminates here in a constrained elative form rather than a routine divine-name formula.\",\"reason\":\"The contextual profile marks the ADJ_COMP form for {{ar:ح ك م}} ({{tr:ḥ-k-m}}) as low-occurrence, and the paired participle class is also limited.\",\"representative_source_ids\":[\"QI-291ddce3\",\"QH-1b1805fd\",\"QH-6cdd92a4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:1:rhetorical-affirmation","source_type":"word_analysis","support_id":"sup_2f4ec6a596255f77c469","text":"{\"blocking_evidence\":null,\"headline\":\"negative question demands assent\",\"reader_payoff\":\"The reader notices that the ayah is not asking for information; the negative interrogative turns denial-form into emphatic affirmation.\",\"reason\":\"The interrogative hamza is prefixed to the copular negator, matching the attachment note that the surface force should be preserved as a rhetorical question.\",\"representative_source_ids\":[\"MG-beb20dfb\",\"QS-b536cdd0\",\"QF-4846cdbd\",\"QI-c56bd486\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:5:governance-and-restraint-range","source_type":"word_analysis","support_id":"sup_34acc2c1c2babc02a58f","text":"{\"blocking_evidence\":null,\"headline\":\"judges broaden to rulers and limit-setters\",\"reader_payoff\":\"The reader notices that the class is broader than courtroom judges, extending to agents who rule, arbitrate, govern, and set limits.\",\"reason\":\"V4 supports judgment, governance-adjacent adjudication, and restraint branches for {{ar:ح ك م}} ({{tr:ḥ-k-m}}), while the local active participle keeps the selected sense tied to judging agents.\",\"representative_source_ids\":[\"QS-a00aad10\",\"QS-e71a7d5d\",\"QT-e3af2477\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:4:semantic-compression","source_type":"word_analysis","support_id":"sup_35ea3a64ca537c1fe4a4","text":"{\"blocking_evidence\":null,\"headline\":\"judgment gathers wisdom, precision, and restraint\",\"reader_payoff\":\"The reader notices that the judgment word is not flatly legal; it also brings wisdom, firm precision, and restraint into the final attribute.\",\"reason\":\"V4 accepts judgment, wisdom, firming, and restraint branches for {{ar:ح ك م}} ({{tr:ḥ-k-m}}), but the local construct with the active-participle class narrows these pressures into the judgment-class superlative rather than free polysemy.\",\"representative_source_ids\":[\"QS-1bc30c4e\",\"QS-933f5df1\",\"QS-affaa16c\",\"QS-c4b6ccee\",\"QS-f417e8d3\",\"MS-2d0daac9\",\"MS-cc2d31d0\",\"QF-2a0e6d14\",\"QY-0deef4cd\",\"QY-4573ffb7\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:2:creator-named-as-judge","source_type":"word_analysis","support_id":"sup_3e3a4ba7de797f9ca3e9","text":"{\"blocking_evidence\":null,\"headline\":\"earlier creator is named at judgment close\",\"reader_payoff\":\"The reader notices a same-surah movement from divine creative action in 95:4 to explicit divine judicial identity in 95:8.\",\"reason\":\"The explicit subject in 95:8 can coherently be compared with the earlier creation claim in 95:4 without changing the local parse.\",\"representative_source_ids\":[\"MI-a0e30e5b\",\"QE-c7a94c73\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"95:8:2:1","source_type":"qac_morpheme","support_id":"sup_5bd22b196ae10682d203","text":"{\"lemma_ar\":\"ٱللَّه\",\"morph_features\":\"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"PN\",\"qac_ref\":\"95:8:2:1\",\"qac_word_ref\":\"95:8:2\",\"root_ar\":\"ء ل ه\",\"surface_ar\":\"ٱللَّهُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"95:8:1:2","source_type":"qac_morpheme","support_id":"sup_6560e14dcba310094930","text":"{\"lemma_ar\":\"لَّيْسَ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"95:8:1:2\",\"qac_word_ref\":\"95:8:1\",\"root_ar\":\"ل ي س\",\"surface_ar\":\"لَيْسَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:1:boundary-verdict-shift","source_type":"word_analysis","support_id":"sup_6d0604bc571db88ae690","text":"{\"blocking_evidence\":null,\"headline\":\"denial is moved before judgment\",\"reader_payoff\":\"The reader notices the boundary shift from a denier's challenge in 95:7 to the authority before whom that denial fails in 95:8.\",\"reason\":\"The prior ayah's challenge and the final ayah's rhetorical predicate form a coherent discourse turn from accusation to verdict closure.\",\"representative_source_ids\":[\"QB-017d8505\",\"QB-a8641c68\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:4:nested-genitive-dependency","source_type":"word_analysis","support_id":"sup_6f5e4eeb61cb94044008","text":"{\"blocking_evidence\":null,\"headline\":\"governed and governing at once\",\"reader_payoff\":\"The reader notices that the single genitive form carries both external prepositional government and internal construct dependency.\",\"reason\":\"Attachment evidence identifies {{ar:أَحْكَمِ}} ({{tr:ʾaḥkami}}) as governed by {{ar:بِ}} ({{tr:bi}}) and as the construct head for {{ar:ٱلْحَٰكِمِينَ}} ({{tr:al-ḥākimīna}}).\",\"representative_source_ids\":[\"QG-3f190c81\",\"QG-852d918c\",\"QG-b516542f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:1:surah-closing-turn","source_type":"word_analysis","support_id":"sup_7f2fcc3513a32fbfd550","text":"{\"blocking_evidence\":null,\"headline\":\"accusation becomes universal recognition\",\"reader_payoff\":\"The reader notices that after the direct accusation in 95:7, the final question makes the listener supply assent to the divine-judgment conclusion.\",\"reason\":\"Attachment evidence recommends reading 95:8 with 95:7, and the CRITICAL rows coherently connect the prior challenge and suspended after-all-this pressure to the final question.\",\"representative_source_ids\":[\"QI-a116a379\",\"QT-28f9d865\",\"QT-6c734d79\",\"QB-8028619d\",\"QY-1a2331fd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:1:uninflected-timeless-frame","source_type":"word_analysis","support_id":"sup_863d8448e6279c163df2","text":"{\"blocking_evidence\":null,\"headline\":\"uninflected form avoids event-tense framing\",\"reader_payoff\":\"The reader notices that the predication is framed as a standing nominal judgment, not as a one-time event.\",\"reason\":\"The local form is tagged as an uninflected verb, but the evidence supports a tense-light copular frame rather than a broad claim that the morphology itself enacts permanence.\",\"representative_source_ids\":[\"MG-3c5442df\",\"QF-c528755a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:5:root-echo-quality-to-class","source_type":"word_analysis","support_id":"sup_8c7ecc2de3991ea0e065","text":"{\"blocking_evidence\":null,\"headline\":\"root echo moves into agent-class\",\"reader_payoff\":\"The reader notices that the repeated root creates a local movement from superlative quality to the class that quality surpasses.\",\"reason\":\"The final phrase repeats {{ar:ح ك م}} ({{tr:ḥ-k-m}}) across different forms, giving both semantic closure and local phonetic recurrence.\",\"representative_source_ids\":[\"QE-6fd4a677\",\"QE-c77efe8e\",\"ME-bba8a321\",\"QP-526aecf0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:5:idafa-class-complement","source_type":"word_analysis","support_id":"sup_9599429a4a1c3ecc3adc","text":"{\"blocking_evidence\":null,\"headline\":\"genitive tail completes the superlative\",\"reader_payoff\":\"The reader notices that the final word is required by the construct; it supplies the class without which the superlative would be less defined.\",\"reason\":\"QAC and attachment evidence identify the word as the genitive second term of the construct headed by {{ar:أَحْكَمِ}} ({{tr:ʾaḥkami}}).\",\"representative_source_ids\":[\"QG-01f3868a\",\"QF-ddbf9f67\",\"QT-277242cc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:2:trustworthy-judgment-frame","source_type":"word_analysis","support_id":"sup_97161b80ed255c035742","text":"{\"blocking_evidence\":null,\"headline\":\"trustworthy opening meets named judge\",\"reader_payoff\":\"The reader notices that the trustworthy city in 95:3 and the named judge in 95:8 bracket the surah's moral argument with reliability and judgment.\",\"reason\":\"The same-surah echo is a thematic frame, not a grammatical dependency; it survives as a commentary candidate with concrete reference to 95:3.\",\"representative_source_ids\":[\"QE-f0f4e1f0\",\"ME-61e1fb25\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:2:proper-name-not-common-deity","source_type":"word_analysis","support_id":"sup_9b632081f80c37f1a219","text":"{\"blocking_evidence\":null,\"headline\":\"proper name blocks generic deity reading\",\"reader_payoff\":\"The reader notices that the clause is a named predication about God, not a general statement about a class of deities.\",\"reason\":\"The local form is tagged as a proper noun, and the missing V4 root data for {{ar:أ ل ه}} ({{tr:ʾ-l-h}}) is not negative evidence against the proper-name distinction.\",\"representative_source_ids\":[\"QF-36c91f6d\",\"QF-eff60849\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:3","source_type":"word_analysis","support_id":"sup_9c653b433c272c6d0168","text":"{\"gloss_range\":\"bāʾ zāʾida in the laysa predicate, reinforcing negation while governing the following superlative as genitive\",\"prose\":\"{{ar:بِ}} ({{tr:bi}}) is small on the page but heavy in the syntax. In the laysa construction it functions as bāʾ zāʾida: it does not mean ordinary instrument, location, or accompaniment, yet it reinforces the negated predicate that the rhetorical question then reverses into affirmation. At the same time it is not syntactically empty, because it governs {{ar:أَحْكَمِ}} ({{tr:ʾaḥkami}}) as genitive and makes the predicate arrive as {{ar:بِأَحْكَمِ}} ({{tr:bi-ʾaḥkami}}), one fused written unit. This lets the ayah name {{ar:ٱللَّهُ}} ({{tr:allāhu}}) first, then pivot through the short particle into the full superlative claim.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:بِ}} ({{tr:bi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:4:class-apex-elative","source_type":"word_analysis","support_id":"sup_9deb4ac64fa8384fdc65","text":"{\"blocking_evidence\":null,\"headline\":\"elative makes an apex-of-class claim\",\"reader_payoff\":\"The reader notices that the form does not merely name an attribute; it places the divine predicate at the ceiling of the class named by the following plural.\",\"reason\":\"QAC tags the word as an elative adjective and attachment evidence makes the following active participle its class complement; the 23:14 comparison remains a formulaic parallel.\",\"representative_source_ids\":[\"QF-73eb9eb1\",\"MF-beeaafd6\",\"QI-9a36134a\",\"MT-0e678c61\",\"MI-ab928fc5\",\"QE-32b4cda5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:4:root-form-echo","source_type":"word_analysis","support_id":"sup_a2f695200de1e2f4dd0e","text":"{\"blocking_evidence\":null,\"headline\":\"same root shifts from degree to class\",\"reader_payoff\":\"The reader notices that the repeated root is not mere repetition: the elative gives degree and the participle supplies the agent-class.\",\"reason\":\"The two adjacent words share {{ar:ح ك م}} ({{tr:ḥ-k-m}}) but differ in form, allowing a local sound-and-sense echo tied to the construct structure.\",\"representative_source_ids\":[\"QF-4e245204\",\"QE-0c14d2ca\",\"ME-23423f4e\",\"QP-672aa69f\",\"QY-1818677d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:5","source_type":"word_analysis","support_id":"sup_b266ac13cc4f59857163","text":"{\"gloss_range\":\"definite masculine plural active participle in genitive, naming the judging/ruling agent-class surpassed by the elative\",\"prose\":\"{{ar:ٱلْحَٰكِمِينَ}} ({{tr:al-ḥākimīna}}) supplies the class that {{ar:أَحْكَمِ}} ({{tr:ʾaḥkami}}) surpasses, so the final word is not an ornamental plural. Its genitive case closes the idāfa, and its definite sound masculine plural form names rational judging agents as a whole. The active participle presents the class through ongoing agency: judges, rulers, arbiters, governors, and limit-setters are gathered as the field over which God's judgment stands supreme. Although this active-participle group is limited, it appears inside the familiar final-question frame, so the rare class term carries a broadly recognizable divine-judgment affirmation. As the surah's last word, it refuses to let the close land on the denier from 95:7; the long -īn cadence makes the sound and sense land instead on the universal judging class and the authority that upholds denied accountability. Its shared {{ar:ح ك م}} ({{tr:ḥ-k-m}}) root with {{ar:أَحْكَمِ}} ({{tr:ʾaḥkami}}) moves from superlative quality to agent-class, while the trustworthy frame in 95:3 is answered by judicial closure in 95:8.\",\"root_display\":\"{{ar:ح ك م}} ({{tr:ḥ-k-m}})\",\"root_gloss_range\":\"root range includes judges, rulers, arbiters, governors, wise adjudicators, and limit-setters; local form selects active judging agents as the class complement\",\"surface_display\":\"{{ar:ٱلْحَٰكِمِينَ}} ({{tr:al-ḥākimīna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:2:root-background-pressure","source_type":"word_analysis","support_id":"sup_b7999273ec332ac347b4","text":"{\"blocking_evidence\":null,\"headline\":\"root dispute remains background only\",\"reader_payoff\":\"The reader notices that worship and awe can color the named subject, while the clause itself still works through the proper divine name.\",\"reason\":\"The CRITICAL row's root-dispute pressure is meaningful but must be limited because the local word is a lexicalized proper name and V4 provides no root guardrail rows for {{ar:أ ل ه}} ({{tr:ʾ-l-h}}).\",\"representative_source_ids\":[\"QS-35441bd1\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:3:proclitic-fusion","source_type":"word_analysis","support_id":"sup_b7ab0839c93307e6145e","text":"{\"blocking_evidence\":null,\"headline\":\"particle fuses to the elative\",\"reader_payoff\":\"The reader notices that reinforcement and the superlative are encountered as one written unit.\",\"reason\":\"The particle is a proclitic attached directly to the following superlative in the written surface.\",\"representative_source_ids\":[\"QF-05013801\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:5:definite-active-agent-class","source_type":"word_analysis","support_id":"sup_bfeb01377850aedbdfef","text":"{\"blocking_evidence\":null,\"headline\":\"definite plural names active judges\",\"reader_payoff\":\"The reader notices that the comparison is against a definite plural class of active judging agents, not an abstract system or an indefinite sample.\",\"reason\":\"The word is a definite masculine plural active participle in genitive, marking rational agenthood and dependent class role.\",\"representative_source_ids\":[\"QG-534320a7\",\"QG-5660720a\",\"MG-e570633c\",\"MS-432ad7bf\",\"QF-df0530bc\",\"QS-f8cc72dd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:3:subject-to-predicate-pivot","source_type":"word_analysis","support_id":"sup_c3dfad1ff2947f4f9326","text":"{\"blocking_evidence\":null,\"headline\":\"particle pivots from subject to attribute\",\"reader_payoff\":\"The reader notices the short particle as the hinge between the named subject and the heavier judgment-root predicate.\",\"reason\":\"The local sequence places {{ar:ٱللَّهُ}} ({{tr:allāhu}}) before the particle-prefixed predicate, and the phonetic claim is local to that transition.\",\"representative_source_ids\":[\"QT-47f8454d\",\"QP-e8adfe30\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:1","source_type":"word_analysis","support_id":"sup_cdce904c05810b707f17","text":"{\"gloss_range\":\"rhetorical negative interrogative built on the copular negator laysa, governing a subject and bāʾ-marked predicate\",\"prose\":\"{{ar:أَلَيْسَ}} ({{tr:ʾa-laysa}}) opens the ayah by placing the whole divine-judgment predicate under a negative question whose expected answer is yes. The word is not merely a denial: {{ar:لَيْسَ}} ({{tr:laysa}}) first builds a copular proposition with {{ar:ٱللَّهُ}} ({{tr:allāhu}}) as subject and {{ar:بِأَحْكَمِ ٱلْحَٰكِمِينَ}} ({{tr:bi-ʾaḥkami l-ḥākimīna}}) as predicate, then the prefixed interrogative turns that scoped negation into compelled affirmation. Because {{ar:لَيْسَ}} ({{tr:laysa}}) is uninflected here, the predication is not cast as a past or future event but as a standing nominal judgment. Because the predicate is bāʾ-marked, the opening word controls the full phrase rather than only a single adjective. Coming after the direct challenge of 95:7, it shifts the register from accusing the denier to making every listener complete the omitted after-all-this argument by assenting to God's supreme judgment. The same formulaic movement is visible in divine-attribute closures such as 11:90 and 75:40, while here its compactness makes the whole final ayah one tight question. The repeated l-sounds from {{ar:لَيْسَ}} ({{tr:laysa}}) into {{ar:ٱللَّهُ}} ({{tr:allāhu}}) also make the negating frame and named subject feel audibly continuous.\",\"root_display\":\"{{ar:ل ي س}} ({{tr:l-y-s}})\",\"root_gloss_range\":\"local branch is the fixed negating copular verb; other lexical branches such as exception, bravery, remaining in place, forbearance, or weak judgment are not active here\",\"surface_display\":\"{{ar:أَلَيْسَ}} ({{tr:ʾa-laysa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:5:final-attribute-seal","source_type":"word_analysis","support_id":"sup_cf2e7205eb40d929c371","text":"{\"blocking_evidence\":null,\"headline\":\"surah lands on judgment authority\",\"reader_payoff\":\"The reader notices that the surah ends not on denial but on the universal judging class and the authority that answers denied accountability.\",\"reason\":\"The final word closes the predicate in 95:8, answers the denial of {{ar:ٱلدِّينِ}} ({{tr:al-dīn}}) in 95:7, and can be read as a same-surah bookend with {{ar:ٱلْأَمِينِ}} ({{tr:al-amīn}}) in 95:3.\",\"representative_source_ids\":[\"QT-ae2c59c6\",\"QP-54d0713a\",\"QB-45ffd798\",\"QB-a6d00cfa\",\"QE-87dc3122\",\"QE-8daf835c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:2:named-subject-of-laysa","source_type":"word_analysis","support_id":"sup_d046ec2fd6c22c4d2c42","text":"{\"blocking_evidence\":null,\"headline\":\"proper name anchors the predicate\",\"reader_payoff\":\"The reader notices that the supreme-judgment claim is predicated of the named divine subject, not left as an abstract maxim.\",\"reason\":\"QAC and attachment evidence identify {{ar:ٱللَّهُ}} ({{tr:allāhu}}) as the nominative ism of {{ar:أَلَيْسَ}} ({{tr:ʾa-laysa}}).\",\"representative_source_ids\":[\"QG-423bc858\",\"QG-6eb0ab4e\",\"QG-dc4f1b04\",\"QT-afb29636\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:5:recognized-divine-judgment-pairing","source_type":"word_analysis","support_id":"sup_d756b17f96d0272e3ff6","text":"{\"blocking_evidence\":null,\"headline\":\"limited participle carries familiar affirmation\",\"reader_payoff\":\"The reader notices that a limited active-participle form is placed inside a familiar divine-judgment affirmation.\",\"reason\":\"The contextual profile shows a small active-participle group, and the broader divine-name plus judgment field is recognized without making distribution alone create the topic.\",\"representative_source_ids\":[\"QI-2318574d\",\"QI-87c45328\",\"QH-6e1a389c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:3:reinforcing-bāʾ-predicate","source_type":"word_analysis","support_id":"sup_e051ad868fbfef107e60","text":"{\"blocking_evidence\":null,\"headline\":\"bāʾ reinforces the laysa predicate\",\"reader_payoff\":\"The reader notices that the particle strengthens the predicate under negation without adding an ordinary spatial or instrumental meaning.\",\"reason\":\"QAC and attachment evidence explicitly describe the particle as bāʾ zāʾida in the laysa predicate, with translation support warning against lexicalizing it independently.\",\"representative_source_ids\":[\"QG-a35ade9c\",\"QG-c60b4485\",\"QG-df1e1b17\",\"MG-46a5c0a7\",\"QS-3c86b2fb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:2","source_type":"word_analysis","support_id":"sup_e3bea557a634347bdb01","text":"{\"gloss_range\":\"proper divine name functioning as the nominative subject of the laysa clause and bearer of the final judgment predicate\",\"prose\":\"{{ar:ٱللَّهُ}} ({{tr:allāhu}}) is the nominative subject of the laysa clause, so the final predicate is anchored in the named divine referent rather than in an abstract idea of judgment or a generic deity category. Its placement before the bāʾ-marked predicate lets the listener identify the authority first and then hear the attribute: God is the one being affirmed as {{ar:أَحْكَمِ ٱلْحَٰكِمِينَ}} ({{tr:ʾaḥkami l-ḥākimīna}}). The name is locally qualified by the judgment-and-wisdom field, not by mercy, power, justice-only wording, or decree-only wording; the broader divine-name pairing is familiar in Quranic judgment discourse, while this exact elative construction is narrower and more pointed. The proper-name form narrows the local work of the root: worship-reference and bewilderment-pressure can stand behind the name, but the grammar here selects the lexicalized divine name as subject. Within the surah, the explicit naming also matters: the creator implied in the first-person creation claim of 95:4 is now named at the judicial close, and the trustworthy-city frame in 95:3 is answered by named divine judgment in 95:8.\",\"root_display\":\"{{ar:أ ل ه}} ({{tr:ʾ-l-h}})\",\"root_gloss_range\":\"proper-name usage fixes the referent; proposed worship and bewilderment root pressures may remain as background but do not replace the local proper-name function\",\"surface_display\":\"{{ar:ٱللَّهُ}} ({{tr:allāhu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:4","source_type":"word_analysis","support_id":"sup_e50089fb135d43f72bff","text":"{\"gloss_range\":\"genitive elative/superlative construct head, locally the apex term in the phrase 'most/firmest/most wisely judging of judges'\",\"prose\":\"{{ar:أَحْكَمِ}} ({{tr:ʾaḥkami}}) is the predicate's core word, but its grammar is deliberately compressed. It is governed from the left by {{ar:بِ}} ({{tr:bi}}), so it appears in genitive form, and it governs to the right as a construct head whose class is supplied by {{ar:ٱلْحَٰكِمِينَ}} ({{tr:al-ḥākimīna}}). The elative pattern makes the claim more than 'God judges': it places God at the highest degree within the class of judging agents. The {{ar:ح ك م}} ({{tr:ḥ-k-m}}) field lets the phrase hold adjudication, wisdom, firm precision, and concrete restraint together, so divine judgment feels like boundary-setting control and not only a courtroom verdict; the idāfa with {{ar:ٱلْحَٰكِمِينَ}} ({{tr:al-ḥākimīna}}) still keeps the local sense centered on the judging class. That makes the word answer the denial of judgment in 95:7 with a concise judicial conclusion and helps ground the uncut reward of 95:6 in divine judgment. Its rare elative profile, doubled root with the following participle, and broader superlative-of-class pattern comparable to 23:14 make the close sound like a formal verdict rather than an isolated adjective.\",\"root_display\":\"{{ar:ح ك م}} ({{tr:ḥ-k-m}})\",\"root_gloss_range\":\"root range includes judging, wisdom, firm making, restraint, and delegation; local construction selects the judgment-class superlative while allowing wisdom, precision, and restraint pressure\",\"surface_display\":\"{{ar:أَحْكَمِ}} ({{tr:ʾaḥkami}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:1:laysa-predicate-scope","source_type":"word_analysis","support_id":"sup_e6e2395c8c501c25a22d","text":"{\"blocking_evidence\":null,\"headline\":\"copular negation scopes over the full predicate\",\"reader_payoff\":\"The reader notices that the opening word governs a complete proposition, with the named subject and the whole bāʾ-marked superlative predicate inside its scope.\",\"reason\":\"QAC and attachment evidence identify a laysa-class copular clause with {{ar:ٱللَّهُ}} ({{tr:allāhu}}) as subject and the bāʾ-marked superlative phrase as predicate.\",\"representative_source_ids\":[\"QG-82d6a5bd\",\"QG-9e32247a\",\"QG-d0ad8c5f\",\"QS-b480ee62\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:1:lam-sound-link","source_type":"word_analysis","support_id":"sup_f4fb7a8be69d4c765dd6","text":"{\"blocking_evidence\":null,\"headline\":\"sound links negator and divine name\",\"reader_payoff\":\"The reader notices that the opening negator and the divine name are audibly tied by repeated l-sounds.\",\"reason\":\"The phonetic observation is local to adjacent words and does not alter grammar or lexical sense.\",\"representative_source_ids\":[\"QP-30d9b4e2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:8:4:judicial-discourse-closure","source_type":"word_analysis","support_id":"sup_ffc5edaaf0c58492170c","text":"{\"blocking_evidence\":null,\"headline\":\"final predicate turns denial into verdict\",\"reader_payoff\":\"The reader notices that the superlative predicate answers the denial of judgment in 95:7 and seals the surah's sequence with divine judicial authority.\",\"reason\":\"The rhetorical-question frame follows 95:7, and the {{ar:ح ك م}} ({{tr:ḥ-k-m}}) superlative coherently closes the sequence that includes reward in 95:6 and denial of judgment in 95:7.\",\"representative_source_ids\":[\"QI-9191495c\",\"MI-51bd6c66\",\"MT-b1d31029\",\"QT-1ec33e69\",\"QT-411b2e24\",\"QT-529db5f4\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"أَلَيْسَ ٱللَّهُ بِأَحْكَمِ ٱلْحَٰكِمِينَ","ayah_ref":"95:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000047/B002","root_000348/B002","root_001390/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001390","role":"Fixed present-state negation supplies the proposition whose denial the rhetorical question makes untenable.","root":"ل ي س","source_ref":"95:8","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000047","role":"The fixed divine name identifies the subject whose judicial supremacy is put directly to the hearer.","root":"ء ل ه","source_ref":"95:8","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000348","role":"Adjudication among people supplies the literal court-domain comparison intensified by the repeated root.","root":"ح ك م","source_ref":"95:8","source_word_indices":["3","4"]}],"changed_reading":{"after":"An emphatically framed demand for assent that Allah is the unsurpassed adjudicator, with denial itself placed under pressure.","before":"A flat question about whether Allah is a better judge than other judges."},"confidence":"strong","focus_anchor":"The negative interrogative أَلَيْسَ, the reinforcing bāʾ in بِأَحْكَمِ, and the doubled ح ك م construction أَحْكَمِ ٱلْحَٰكِمِينَ.","mechanism":"Fixed present-state negation is turned by the interrogative into demanded assent, while the superlative and agent plural rank Allah above every other adjudicator.","model_id":"baseline_emphatic_adjudication"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_emphatic_adjudication","source_type":"hft","support_id":"sup_9591c7e41a55ecca2efb","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَلَيْسَ ٱللَّهُ بِأَحْكَمِ ٱلْحَٰكِمِينَ","ayah_ref":"95:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000348/B001","root_000348/B006"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000348","role":"Restraining and turning back corruption supplies judgment's corrective action rather than merely its declaration.","root":"ح ك م","source_ref":"95:8","source_word_indices":["3","4"]},{"branch_id":"B006","mapped_root_id":"root_000348","role":"The bridle-piece makes the corrective mechanism concrete as force checked and redirected.","root":"ح ك م","source_ref":"95:8","source_word_indices":["3","4"]}],"changed_reading":{"after":"Best judging means most effectively arresting injustice and redirecting destructive motion toward right order.","before":"Best judging means issuing the best verdict."},"confidence":"medium","focus_anchor":"The two ح ك م forms in أَحْكَمِ ٱلْحَٰكِمِينَ retain a root-image of checking motion and preventing corruption.","mechanism":"Judgment is not only a verdict but an effective restraint: it blocks injustice, turns harmful intention, and functions like a bridle that converts force into governed motion.","model_id":"baseline_corrective_restraint"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_corrective_restraint","source_type":"hft","support_id":"sup_894381612f755e3fff01","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَلَيْسَ ٱللَّهُ بِأَحْكَمِ ٱلْحَٰكِمِينَ","ayah_ref":"95:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000348/B003","root_000348/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000348","role":"Making a thing firm, perfected, and decisive supplies the result produced by the superlative judge.","root":"ح ك م","source_ref":"95:8","source_word_indices":["3","4"]},{"branch_id":"B003","mapped_root_id":"root_000348","role":"Rightly guided knowledge supplies the truth-sensitive intelligence by which firmness avoids becoming mere force.","root":"ح ك م","source_ref":"95:8","source_word_indices":["3","4"]}],"changed_reading":{"after":"It also names the one whose judging most fully firms an unsettled matter and brings it to a truth-responsive completion.","before":"The phrase only ranks one judge above a class of judges."},"confidence":"medium","focus_anchor":"The comparative أَحْكَمِ and the agent noun حَٰكِمِينَ repeat one root while allowing perfective and juridical senses to overlap.","mechanism":"The phrase compares judges while also hearing judgment as the craft of making a matter firm, complete, and truth-hitting; decisiveness is therefore constructed, not merely announced.","model_id":"baseline_decisive_perfection"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_decisive_perfection","source_type":"hft","support_id":"sup_6651a80eed86d23a341f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَلَيْسَ ٱللَّهُ بِأَحْكَمِ ٱلْحَٰكِمِينَ","ayah_ref":"95:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000348/B005","root_001390/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001390","role":"Present-state negation frames refusal to entrust the decision as the position the question challenges.","root":"ل ي س","source_ref":"95:8","source_word_indices":["1"]},{"branch_id":"B005","mapped_root_id":"root_000348","role":"Delegation and acceptance of another's decision supply the transfer-of-jurisdiction mechanism.","root":"ح ك م","source_ref":"95:8","source_word_indices":["3","4"]}],"changed_reading":{"after":"The hearer is also asked whether any authority is more fit to be entrusted with the case.","before":"The hearer is asked to acknowledge a ranking among judges."},"confidence":"exploratory","focus_anchor":"أَحْكَمِ ٱلْحَٰكِمِينَ can profile not only the winner of a comparison but the one most fit to receive delegated decision.","mechanism":"The question becomes jurisdictional: it presses the hearer to recognize where decision may finally be lodged and whose ruling can be accepted without appeal.","model_id":"baseline_entrusted_decision"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_entrusted_decision","source_type":"hft","support_id":"sup_0cddc03f956e5a2a9f09","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَلَيْسَ ٱللَّهُ بِأَحْكَمِ ٱلْحَٰكِمِينَ","ayah_ref":"95:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000348/B003","root_001390/B006"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_001390","role":"Forbearing, overlooking, and carrying a load supply the affective and load-bearing side of the exploratory judicial posture.","root":"ل ي س","source_ref":"95:8","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000348","role":"Wisdom that hits truth while including forbearance keeps overlooking answerable to knowledge rather than indifference.","root":"ح ك م","source_ref":"95:8","source_word_indices":["3","4"]}],"changed_reading":{"after":"As a contained root-shadow, judicial excellence may include the capacity to bear, forbear, and overlook while still striking truth.","before":"Judicial excellence is maximally exact and therefore maximally severe."},"confidence":"exploratory","containment":"This is surprising because it activates derived nominal senses around ل ي س rather than the syntax of لَيْسَ itself; it remains focus-anchored because those senses pair load-bearing forbearance with the ح ك م branch that includes wise forbearance. Downstream prose should present it only as a root-shadow: the finest judge can bear and overlook without losing truth, not as a replacement gloss for أَلَيْسَ.","focus_anchor":"The focus juxtaposes ل ي س and repeated ح ك م, whose branch inventories independently meet in forbearance.","outlier_id":"outlier_forbearing_load_bearing_judge"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:outlier_forbearing_load_bearing_judge","source_type":"hft","support_id":"sup_e27ec30ec80adc276402","trust":"legacy_unbound"}]}
</lane_packet_json>
