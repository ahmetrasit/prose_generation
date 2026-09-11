# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **109:6**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s109-regular-20260911/s109/109_6/micro.discovery.json` and modify nothing
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
  "ayah_ref": "109:6",
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
{"analysis_context":{"analysis_id":"s109-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"109:6","host_surah":109,"lane_context_refs":[],"ordered_context_refs":["109:0","109:1","109:2","109:3","109:4","109:5","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Genel olarak buyruğa uyma çekirdektir; kulluk ve inanç düzeni bu çekirdeğin özel alanlarıdır, hesap, borç ve zorla egemenlik bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000504/B001","candidate_links":[{"candidate_id":"cand_8882b9eec0590aa63da3","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:6:2:1","qac_word_ref":"109:6:2","surface_ar":"دِينُ"},{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:6:4:1","qac_word_ref":"109:6:4","surface_ar":"دِينِ"}],"gloss":"boyun eğerek uyma ve buna dayalı inanç düzeni","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir üstün iradesine boyun eğme ve onun buyruğuna uyma."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tanrı söz konusu olduğunda bağlılığın kulluk etme biçimini alması."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnanç yolu ve kurallar bütününün, onlara uyma ve bağlanma ilişkisi açısından adlandırılması."}}],"root_ar":"د ي ن","root_id":"root_000504","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel bağlılık çekirdeğini ve bunun kulluk ile inanç düzenine uzanan kapsamını birlikte anlatan en kısa doğal karşılıktır.","boundary_detail":"Genel olarak buyruğa uyma çekirdektir; kulluk ve inanç düzeni bu çekirdeğin özel alanlarıdır, hesap, borç ve zorla egemenlik bu dala girmez.","branch_image_ar":"الطاعة والانقياد","concept_gloss":"boyun eğerek uyma ve buna dayalı inanç düzeni","contextual_glosses":[{"applicability":"Bir kişiye veya üstün iradeye bağlılığın doğrudan anlatıldığı genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kulluk ile inanç ve kurallar düzenine uzanan özel kapsamı söylemez.","preserves":"Boyun eğme ve buyruğa uyma ilişkisini korur."},"facet_ids":["F001"],"text":"boyun eğip buyruğuna uyma","usage_role":"general"},{"applicability":"Tanrı'ya bağlılık, kulluk ve benimsenen inanç yolunun birlikte öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tanrısal alan dışındaki genel boyun eğme ve buyruğa uyma kapsamını dışarıda bırakır.","preserves":"Kulluk ile inanç ve kurallar bütününe bağlılığı korur."},"facet_ids":["F002","F003"],"text":"inanç ve kulluk düzeni","usage_role":"contextual"}],"definition":"Bir üstün iradesine boyun eğerek buyruğuna uyma ve bağlı kalma; Tanrı'ya yöneldiğinde kulluk, bir inanç yolu ve onun kurallarına bağlılık biçimini alabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir üstün iradesine boyun eğme ve onun buyruğuna uyma."},{"facet_id":"F002","role":"specialization","statement":"Tanrı söz konusu olduğunda bağlılığın kulluk etme biçimini alması."},{"facet_id":"F003","role":"extension","statement":"İnanç yolu ve kurallar bütününün, onlara uyma ve bağlanma ilişkisi açısından adlandırılması."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":null,"collision":"Türkçede çoğunlukla yalnızca kurumsal inanç sistemini düşündürür.","fit":"drifted_loanword","loses":"Boyun eğme ve buyruğa uyma çekirdeğini kendi başına açıklamaz.","preserves":"Yerleşik bir inanç ve kulluk alanına gönderme yapar."},"text":"din"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Boyun eğme, kulluk ve inanç düzeni kapsamının tümünü vermez.","preserves":"Buyruğa uyma ve bağlılık yönünü korur."},"text":"itaat"}],"identity_rationale":"Kaynak ifadesi dalın merkezine boyun eğme, uyma ve bağlılığı koyar; Tanrı'ya yönelik kulluğu, inanç yolunu ve kurallar bütününü de bu temel ilişkinin özel görünümleri olarak açıklar. Bu nedenle verilen dal kimliği kanıtla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"boyun eğme, kulluk ve inanç düzeni"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ona boyun eğdi ve buyruğuna uydu"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"gerçek inanç yolu"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"hükümdarın buyruğu ya da yargısı"}],"lexicalization_note":"Dal hem yalın biçimleri hem de belirli söz öbeklerini içerir; söz öbeklerine özgü hükümdarlık ve gerçek inanç yolu anlamları yalın biçimin bütün kullanımlarına yayılmaz.","neighbor_coverage_note":"Sunulan komşuların tümü değerlendirildi; en açıklayıcı üç sınır yayımlandı. Namaz, yemin ve karşı gelme gibi adaylar aynı sahneyi paylaşsa da doğrudan anlam karışıklığı yaratmadığından, kardeş dallar ise aşağıda ayrıca işlendiğinden eklenmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği genel boyun eğme ve uyma olup kulluk ile inanç düzenine genişler; komşu dal ise dinsel nitelikli, alçak gönüllü uyma alanını merkez alır.","focus_only":"Bu dal genel buyruğa uymayı ve bundan gelişen inanç düzenini de kapsar.","gloss":"genel bağlılık ile dinsel bağlılık","neighbor_only":"Komşu dal bağlılığı özellikle dinsel yolda doğruluk ve belirli kişiler arası uyma örnekleriyle sınırlar.","neighbor_ref":"root_001260/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da üstün bir buyruğa boyun eğerek uyma vardır."},{"boundary_match":"partial","distinction":"Odak dal kulluğu daha geniş bir uyma ve bağlılık haritasının özel biçimi sayar; komşu dalda ise kulluk ve alçalış doğrudan tanımlayıcı eylemdir.","focus_only":"Odak dal genel uyma ilişkisini ve inanç ile kurallar düzenini kapsar.","gloss":"bağlılık ile kulluk","neighbor_only":"Komşu dal kulluk eylemini ve bu eylemdeki alçalışı doğrudan çekirdek yapar.","neighbor_ref":"root_000973/B003","relation_type":"near_synonym","shared_zone":"Kulluk bağlamında boyun eğme ve üstün iradeye uyma iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği uyma ve bağlılık ilişkisidir; komşu dalın çekirdeği ise kişinin benimsediği belirli inanç yolu veya gelenektir.","focus_only":"Odak dal inanç yolunun dayandığı boyun eğme ve buyruğa uyma ilişkisini açıklar.","gloss":"uyma ilişkisi ile benimsenen inanç yolu","neighbor_only":"Komşu dal benimsenen belirli inanç topluluğu veya öğreti geleneğini adlandırır.","neighbor_ref":"root_001445/B003","relation_type":"near_neighbor","shared_zone":"İki dal da bir inanç yoluna bağlanma alanında buluşur."}],"source_phrase_ar":"أصل واحد إليه يرجع فروعه كلها وهو جنس من الانقياد والذل (maqayis)؛ فالدين الطاعة (maqayis;sihah)؛ الدين لله طاعته والتعبد له (tahdhib)؛ الدين كالملة اعتبارا بالطاعة والانقياد للشريعة (mufradat)","source_summary":"Kanıt, bütün kullanımları boyun eğme ve uyma ekseninde birleştirir; kulluk ile inanç ve kural düzenini bu ilişkinin özel ve genişlemiş görünümleri olarak sunar.","sources":["MQ","SI","TA","MU"],"what_is_ar":"الدين بمعنى الطاعة والانقياد والتعبد والملة والشريعة وما يتدين به","what_is_not_ar":"ليس الحساب والجزاء ولا الدين المالي ولا المدينة المصر"},"support_links":["sup_2e34bf38722ea59f979a"]},{"boundary":"Bu dal, bir eylem veya kişi hakkında hesap ve karşılık sonucuna varmayı anlatır; inanç düzeni, mali borç ve zorla boyun eğdirme bunun dışında kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000504/B002","candidate_links":[{"candidate_id":"cand_d4e94cca58249ed19e7a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:6:2:1","qac_word_ref":"109:6:2","surface_ar":"دِينُ"},{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:6:4:1","qac_word_ref":"109:6:4","surface_ar":"دِينِ"}],"gloss":"yargılayıp hesap görerek karşılığını verme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya eylem hakkında hükme varıp hesabını görmek."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hesabın sonucuna göre yapılanın karşılığını vermek."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hüküm, hesap ve karşılığın gerçekleşeceği özel günü adlandırmak."}}],"root_ar":"د ي ن","root_id":"root_000504","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hüküm, hesap ve eylemin sonucuna göre karşılık verme aşamalarını birlikte taşıyan genel kavram karşılığıdır.","boundary_detail":"Bu dal, bir eylem veya kişi hakkında hesap ve karşılık sonucuna varmayı anlatır; inanç düzeni, mali borç ve zorla boyun eğdirme bunun dışında kalır.","branch_image_ar":"الحساب والجزاء","concept_gloss":"yargılayıp hesap görerek karşılığını verme","contextual_glosses":[{"applicability":"Hüküm ve karşılık sürecinin gerçekleşeceği özel günün adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kavramın gün adı dışındaki genel yargılama ve karşılık kullanımlarını dışarıda bırakır.","preserves":"Hesap görme ve karşılık verme olayını korur."},"facet_ids":["F001","F002","F003"],"text":"hesap ve karşılık günü","usage_role":"contextual"},{"applicability":"Bir kişinin veya eylemin değerlendirilip sonucuna göre karşılık gördüğü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hesap görme ile sonuca göre karşılık verme sırasını korur."},"facet_ids":["F001","F002"],"text":"hesaba çekilip karşılığının verilmesi","usage_role":"general"}],"definition":"Bir eylemi veya kişiyi hükme bağlayıp hesabını görmek ve sonucuna göre karşılığını vermek; belirli bir gün adı olarak bu sürecin gerçekleşeceği zamanı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya eylem hakkında hükme varıp hesabını görmek."},{"facet_id":"F002","role":"core","statement":"Hesabın sonucuna göre yapılanın karşılığını vermek."},{"facet_id":"F003","role":"specialization","statement":"Hüküm, hesap ve karşılığın gerçekleşeceği özel günü adlandırmak."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hükme varma ve sonuca göre karşılık verme aşamalarını açıkça taşımaz.","preserves":"Eylemlerin değerlendirilmesi ve hesabının görülmesi yönünü korur."},"text":"hesap"},{"category":"confusable","error_profile":{"adds":"Karşılığın mutlaka olumsuz ve yaptırım niteliğinde olduğu izlenimini ekler.","collision":"Genel karşılık sürecini yalnızca yaptırımla karıştırır.","fit":"narrowing","loses":"Hesap, hüküm ve olumlu ya da olumsuz her tür karşılık kapsamını kaybeder.","preserves":"Olumsuz bir eyleme verilen karşılık yönünü koruyabilir."},"text":"ceza"}],"identity_rationale":"Kaynak ifadesi hüküm verme, hesap görme, yapılanın karşılığını verme ve bunların gerçekleşeceği özel günü aynı anlam örgüsünde açıkça birleştirir. Verilen hesap ve karşılık çerçevesi bu kanıtı doğru temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"hesap, yargı ve yapılanın karşılığı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"hesap ve karşılık günü"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"hesaba çekilip karşılığı verilecek olanlar"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yargılayan ve karşılığını veren"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"hükümdarın buyruğu ya da yargısı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kendini alçalttı ya da hesaba çekti"}],"lexicalization_note":"Dal yalın biçimler, türemiş biçimler ve belirli bir gün adını içeren söz öbeğini birlikte taşır; günle sınırlı kullanım bütün dala genellenmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; karşılık verme ve hüküm alanındaki en yakın üç sınır seçildi. Salt yaptırım, pay, borç veya kardeş dal ilişkisi sunan adaylar ya daha dar kaldı ya da yayımlanan ayrımları yineledi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hesap ve hüküm aşamalarını karşılıkla birlikte kurar; komşu dal ise karşılıklı ödül, yaptırım veya ödeşme eylemini öne çıkarır.","focus_only":"Odak dal karşılıktan önce hükme varma ve hesabı görme aşamalarını da içerir.","gloss":"hesaplı yargı ile eyleme karşılık","neighbor_only":"Komşu dal bir eyleme iyilik veya kötülükle denk karşılık vermeyi doğrudan merkez alır.","neighbor_ref":"root_000244/B001","relation_type":"near_synonym","shared_zone":"Her iki dal yapılan bir eylemin sonucuna göre karşılık verilmesini kapsar."},{"boundary_match":"partial","distinction":"Odak dal kurumsal veya sonul bir hüküm ve hesap sürecini içerir; komşu dalda asıl vurgu yapılan işin sahibine dönen sonucundadır.","focus_only":"Odak dal yargılama, hesap görme ve özel gün kullanımını birlikte taşır.","gloss":"hesap ve karşılık ile işin geri dönüşü","neighbor_only":"Komşu dal karşılığı, kişinin yaptığı işin kendisine geri dönen sonucu olarak kurar.","neighbor_ref":"root_000209/B002","relation_type":"near_synonym","shared_zone":"İki dalda da kişinin yaptığı iş nedeniyle bir sonuç veya karşılık görmesi vardır."},{"boundary_match":"partial","distinction":"Odak dal kişinin veya eylemin hesabını ve karşılığını konu edinir; komşu dal iki taraf arasındaki çekişmeyi yargısal kararla sona erdirir.","focus_only":"Odak dal hesap sonucunda karşılık vermeyi ve özel gün kullanımını kapsar.","gloss":"hesap verdirme ile uyuşmazlığı hükme bağlama","neighbor_only":"Komşu dal çekişen taraflar arasında uyuşmazlığı kararla kapatan yargı eylemine odaklanır.","neighbor_ref":"root_001124/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal bir değerlendirme sonunda bağlayıcı hükme varma alanındadır."}],"source_phrase_ar":"يوم الدين أي يوم الحكم والحساب والجزاء (maqayis)؛ الدين الجزاء والمكافأة (sihah)؛ الدين الحساب ومنه مالك يوم الدين ومالك يوم الجزاء (tahdhib)؛ غير مدينين أي غير مجزيين (mufradat)","source_summary":"Kanıt hüküm, hesap ve karşılık vermeyi tek bir süreçte toplar; özel gün kullanımı ile hesaba çekilip karşılığı verilen kişi biçimleri de bu sürece bağlanır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"الدين بمعنى الحكم والحساب والجزاء والمكافأة والقضاء","what_is_not_ar":"ليس الطاعة والشريعة ولا القرض والمداينة"},"support_links":["sup_968c8cfa281ad0d77160"]},{"boundary":"Dal, malın şimdi verilip yükümlülüğün ileride yerine getirildiği mali ilişkiyle sınırlıdır; hesap günü, inanç bağlılığı ve genel alışveriş bununla özdeş değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000504/B003","candidate_links":[{"candidate_id":"cand_863d13f6f886afccca62","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:6:2:1","qac_word_ref":"109:6:2","surface_ar":"دِينُ"},{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:6:4:1","qac_word_ref":"109:6:4","surface_ar":"دِينِ"}],"gloss":"borç alıp verme ve vadeli ödeme ilişkisi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Mal veya paranın borç olarak alınması ya da verilmesiyle mali yükümlülük doğması."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birine ödünç vererek onu geri ödeme yükümlüsü kılmak."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başkasından ödünç alarak geri ödeme yükümlülüğü altına girmek."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Alışverişte bedelin ileri bir tarihe bırakılması."}}],"root_ar":"د ي ن","root_id":"root_000504","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Borç nesnesini, iki taraflı işlemi ve ileride ödeme yükümlülüğünü birlikte anlatan genel karşılıktır.","boundary_detail":"Dal, malın şimdi verilip yükümlülüğün ileride yerine getirildiği mali ilişkiyle sınırlıdır; hesap günü, inanç bağlılığı ve genel alışveriş bununla özdeş değildir.","branch_image_ar":"الدين المالي","concept_gloss":"borç alıp verme ve vadeli ödeme ilişkisi","contextual_glosses":[{"applicability":"Tarafların borç veren ve borç alan olarak kurduğu genel mali bağ anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Vadeli alışveriş ile alma ve verme işlemlerinin ayrı yönlerini açıkça göstermez.","preserves":"Mali yükümlülük ve iki taraflı borç bağını korur."},"facet_ids":["F001"],"text":"borç ilişkisi","usage_role":"general"},{"applicability":"Bir kişinin başkasına geri ödenmek üzere mal veya para sağladığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Borç alma yönünü ve vadeli alışveriş kapsamını dışarıda bırakır.","preserves":"Borç ilişkisinin veren tarafını ve geri ödeme beklentisini korur."},"facet_ids":["F001","F002"],"text":"ödünç verme","usage_role":"contextual"},{"applicability":"Bir kişinin ödünç alarak geri ödeme yükümlülüğü altına girdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Borç verme yönünü ve vadeli satışın özel yapısını dışarıda bırakır.","preserves":"Borç alan tarafı ve üstlenilen mali yükümlülüğü korur."},"facet_ids":["F001","F003"],"text":"borçlanma","usage_role":"contextual"}],"definition":"Bir mal veya paranın borç olarak alınıp verilmesiyle, taraflardan biri için ileride ödeme ya da geri verme yükümlülüğü doğuran mali ilişki; vadeli alışveriş de bu ilişkinin özel bir biçimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Mal veya paranın borç olarak alınması ya da verilmesiyle mali yükümlülük doğması."},{"facet_id":"F002","role":"specialization","statement":"Birine ödünç vererek onu geri ödeme yükümlüsü kılmak."},{"facet_id":"F003","role":"specialization","statement":"Başkasından ödünç alarak geri ödeme yükümlülüğü altına girmek."},{"facet_id":"F004","role":"extension","statement":"Alışverişte bedelin ileri bir tarihe bırakılması."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kurumsal finansman veya banka ürünü çağrışımını gereksiz biçimde ekler.","collision":"Genel borç ilişkisini modern bir finans ürünüyle karıştırır.","fit":"narrowing","loses":"Kişiler arası ödünç verme ile her tür vadeli alışverişi kapsamaz.","preserves":"Sonradan geri ödeme yükümlülüğü doğuran mali kaynak yönünü koruyabilir."},"text":"kredi"},{"category":"alternative","error_profile":{"adds":"Peşin ve borç doğurmayan bütün alım satım işlemlerini kapsama ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Vadeli satış örneğinde taraflar arasındaki mali işlemi korur."},"text":"alışveriş"}],"identity_rationale":"Kaynak ifadesi mali borcu, vadeli alıp vermeyi, borçla alışverişi ve ödünç alma ya da verme yönlerini açıkça aynı dalda toplar. Verilen mali ilişki çerçevesi bu karşılıklı tarafları doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"borç ve vadeli ödeme yükümlülüğü"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"onunla borç alıp verme işlemi yaptı"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ona ödünç verdi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ödünç aldı ve borçlandı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"borçlu veya çok borçlanmış kişi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"onu vadeli olarak sattım"}],"lexicalization_note":"Yalın borç adı, borç alma ve verme eylemleri ile vadeli satış söz öbeği ayrı ayrı korunur; vadeli satışa özgü anlam bütün yalın kullanımlara yüklenmez.","neighbor_coverage_note":"Bütün komşular değerlendirildi; avans, borç aktarımı ve genel satışla olan üç temel sınır seçildi. Borç bakiyesi, güvence, ödünç satış türü ve para adı adayları bu ayrımları dar bir örnekle yinelediği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal taraflar arasında doğan borç bağının iki yönünü anlatır; komşu dal ise işlemin başında öne sürülen para veya bedele odaklanır.","focus_only":"Odak dal ödünç alma, borçlanma ve ileride ödeme yükümlülüğünü de kapsar.","gloss":"borç ilişkisi ile önceden verilen para","neighbor_only":"Komşu dal özellikle önceden verilen para veya satış bedelini nesne olarak öne çıkarır.","neighbor_ref":"root_000733/B005","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir mal veya para, daha sonraki karşılıkla bağlantılı olarak verilir."},{"boundary_match":"field_only","distinction":"Odak dalda borç ilişkisi kurulur veya üstlenilir; komşu dalda ise önceden var olan borcun muhatabı değiştirilir.","focus_only":"Odak dal borcu doğuran alma, verme ve vadeli işlem sürecini anlatır.","gloss":"borç kurma ile borcu aktarma","neighbor_only":"Komşu dal var olan borcun başka bir kişiye veya borçluya aktarılmasını anlatır.","neighbor_ref":"root_000373/B010","relation_type":"same_field","shared_zone":"İki dal da alacaklı ve borçlu arasındaki mali yükümlülük alanındadır."},{"boundary_match":"field_only","distinction":"Odak dalın ayırıcı özelliği borç veya vade doğurmasıdır; komşu dalın çekirdeği ise vade şartı olmaksızın satış ve satın almadır.","focus_only":"Odak dal ödemenin veya geri vermenin ileri tarihe bırakıldığı yükümlülüğü gerektirir.","gloss":"vadeli borç işlemi ile genel satış","neighbor_only":"Komşu dal peşin ya da vadeli olabilen genel mal ve bedel değişimini kapsar.","neighbor_ref":"root_000169/B001","relation_type":"same_field","shared_zone":"Her iki dal mal ile bedelin taraflar arasında değiştiği işlemleri kapsayabilir."}],"source_phrase_ar":"الدين وداينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء (maqayis)؛ الدين واحد الديون وتداينوا تبايعوا بالدين (sihah)؛ دنت الرجل أقرضته وأدنت الرجل إذا أقرضته (tahdhib)؛ التداين والمداينة دفع الدين (mufradat)","source_summary":"Kanıt borcu tek taraflı bir nesne olarak değil, alma ve verme yönleri bulunan bir mali işlem olarak açıklar; ödünç verme, ödünç alma ve vadeli alışveriş bu ortak yapının görünümleridir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"الدين المالي والقرض والاستقراض والمداينة والبيع إلى أجل وما يؤخذ أو يعطى دينا","what_is_not_ar":"ليس الطاعة الدينية ولا الجزاء الأخروي ولا الذل المجرد"},"support_links":["sup_38c769067c21d02a15d7"]},{"boundary":"Zorlama, alçaltma ve sahiplik bu dalı gönüllü uyma dalından ayırır; mali borçlu olma ya da hesap verme tek başına bu anlama girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000504/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:6:2:1","qac_word_ref":"109:6:2","surface_ar":"دِينُ"},{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:6:4:1","qac_word_ref":"109:6:4","surface_ar":"دِينِ"}],"gloss":"zorla alçaltıp egemenliği altına alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birini zor kullanarak alçaltmak ve egemenlik altına almak."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Egemenlik altına alınan kişiyi köleleştirmek veya mülk edinmek."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Egemenlik altındaki erkek veya kadını köleleştirilmiş kişi olarak adlandırmak."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir deyimde kalbi alçaltan veya kişiyi istemediği şeye zorlayan etkeni anlatmak."}}],"root_ar":"د ي ن","root_id":"root_000504","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Alçaltma, zorlama ve sahiplik sonucunu tek bir egemenlik ilişkisi içinde anlatan genel karşılıktır.","boundary_detail":"Zorlama, alçaltma ve sahiplik bu dalı gönüllü uyma dalından ayırır; mali borçlu olma ya da hesap verme tek başına bu anlama girmez.","branch_image_ar":"الإذلال والملك","concept_gloss":"zorla alçaltıp egemenliği altına alma","contextual_glosses":[{"applicability":"Bir topluluk veya kişinin zorla egemenlik altına sokulduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Mülk edinme ile köleleştirilmiş kişi adlarını açıkça taşımaz.","preserves":"Zorlama, alçaltma ve egemenlik kurma yönlerini korur."},"facet_ids":["F001"],"text":"boyunduruk altına alma","usage_role":"general"},{"applicability":"Bir insanın mülk ve bağımlı kişi durumuna getirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Köleliğe varmayan genel alçaltma ve zorlama kullanımlarını dışarıda bırakır.","preserves":"Egemenlik altına alma, mülk edinme ve bağımlı kılma yönlerini korur."},"facet_ids":["F001","F002","F003"],"text":"köleleştirme","usage_role":"contextual"},{"applicability":"Fiziksel sahiplikten çok kişinin onurunu kırıp onu aşağı duruma düşürmenin öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Egemenlik, köleleştirme ve mülk edinme sonuçlarını vermez.","preserves":"Kişiyi alçaltma ve güç altında bırakma yönünü korur."},"facet_ids":["F001"],"text":"aşağılama","usage_role":"contextual"}],"definition":"Birini zorla alçaltıp egemenlik altına almak, köleleştirmek veya mülk edinmek; bu işlemin sonucunda kişi bağımlı ve başkasının buyruğu altında sayılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birini zor kullanarak alçaltmak ve egemenlik altına almak."},{"facet_id":"F002","role":"extension","statement":"Egemenlik altına alınan kişiyi köleleştirmek veya mülk edinmek."},{"facet_id":"F003","role":"associated_use","statement":"Egemenlik altındaki erkek veya kadını köleleştirilmiş kişi olarak adlandırmak."},{"facet_id":"F004","role":"example","statement":"Bir deyimde kalbi alçaltan veya kişiyi istemediği şeye zorlayan etkeni anlatmak."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Eylemi uygulayan yerine buna uyan kişinin gönüllü davranışı izlenimini ekler.","collision":"Bu kökün gönüllü uyma dalıyla karışır.","fit":"displacement","loses":"Başkasını zorla alçaltma, köleleştirme ve mülk edinme eylemlerini kaybeder.","preserves":"Güç ilişkisi içinde aşağı konumda bulunma yönünü kısmen korur."},"text":"boyun eğme"},{"category":"confusable","error_profile":{"adds":"Kanıtta bu dal için bulunmayan mali ödeme yükümlülüğünü ekler.","collision":"Ayrı mali borç dalıyla karışır.","fit":"displacement","loses":"Alçaltma, egemenlik, köleleştirme ve sahiplik çekirdeğini bütünüyle kaybeder.","preserves":"Bir kişiyi bağımlı bir yükümlülük altına sokma çağrışımını koruyabilir."},"text":"borçlandırma"}],"identity_rationale":"Kaynak ifadesi birini alçaltma, zorla egemenlik altına alma, köleleştirme ve mülk edinme eylemlerini; ayrıca bu duruma sokulmuş erkek ve kadın adlarını aynı dalda birleştirir. Verilen zorlayıcı egemenlik çerçevesi bu yapıyı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"onu alçalttı, boyunduruk altına aldı ve köleleştirdi"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"topluluğu alçalttım ve köleleştirdim"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"onu mülk edindim veya buyruğum altına aldım"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"köleleştirilmiş erkek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"köleleştirilmiş kadın"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kendini alçalttı ya da hesaba çekti"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"kalbini alçaltan şey; ayrıca alışkanlık, istemediği şeye zorlama veya eski gönül derdi diye yorumlanan tartışmalı söz"}],"lexicalization_note":"Dal eylem biçimleri, köleleştirilmiş kişiyi gösteren adlar ve tartışmalı bir deyim içerir; deyimdeki yorumlar yalın eylemin tek anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; zorla yenme, doğrudan köleleştirme ve kölelik durumu arasındaki üç sınır seçildi. Öteki güç, yönetim ve vurma adayları aynı ayrımı daha dolaylı kurduğu için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal zorlayıcı üstünlüğü sahiplik ve köleleştirme sonucuna bağlar; komşu dal ise böyle bir sonuç gerektirmeden güçle yenme ve zorlama çekirdeğinde kalır.","focus_only":"Odak dal köleleştirme, mülk edinme ve köleleştirilmiş kişi adlarını da içerir.","gloss":"köleleştirici egemenlik ile zorla yenme","neighbor_only":"Komşu dal üstün konumdan güç kullanarak yenme ve istem dışı ele geçirmeyi genel biçimde kapsar.","neighbor_ref":"root_001266/B001","relation_type":"near_synonym","shared_zone":"Her iki dal birini zorla yenip aşağı ve bağımlı duruma sokmayı kapsar."},{"boundary_match":"partial","distinction":"Odak dal köleleştirmeyi daha geniş alçaltma, sahiplik ve egemenlik alanına yerleştirir; komşu dalın çekirdeği doğrudan köle edinme veya köle gibi çalıştırmadır.","focus_only":"Odak dal genel alçaltma ve egemenlik kurmayı, ayrıca köleleştirilmiş kişi adlarını kapsar.","gloss":"egemenlik altına alma ile köleleştirme","neighbor_only":"Komşu dal birini özellikle köle durumuna getirip köle işi yaptırma eylemini merkez alır.","neighbor_ref":"root_000973/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir insanı zorla bağımlı ve köle durumuna getirebilir."},{"boundary_match":"field_only","distinction":"Odak dalın çekirdeği uygulanan alçaltıcı egemenliktir; komşu dalın çekirdeği bunun kurduğu kölelik statüsü ve mülkiyet durumudur.","focus_only":"Odak dal birini alçaltıp köleleştiren eylemi ve bu sonuca yol açan gücü anlatır.","gloss":"köleleştirme eylemi ile kölelik durumu","neighbor_only":"Komşu dal kölelik durumunu, köle mülkiyetini ve köleleştirilmiş insanlar sınıfını adlandırır.","neighbor_ref":"root_000586/B003","relation_type":"same_field","shared_zone":"Her iki dal kölelik, sahiplik ve insanın bağımlı duruma sokulması alanındadır."}],"source_phrase_ar":"العبد مدين كأنهما أذلهما العمل ويا دين قلبك أي أذل (maqayis)؛ دانه دينا أي أذله واستعبده ودينته ملكته (sihah)؛ غير مدينين غير مملوكين ودنت القوم أدينهم إذا أذللتهم (tahdhib)؛ المدين والمدينة العبد والأمة (mufradat)","source_summary":"Kanıt alçaltma ve zorla egemenlik kurmayı köleleştirme ve sahiplikle birleştirir; egemenlik altındaki erkek ve kadın adları sonuç durumunu, deyimsel kullanım ise alçaltma yönünü örnekler.","sources":["MQ","SI","TA","MU"],"what_is_ar":"الإذلال والقهر والملك والاستعباد والحمل على المكروه والعبد المدين والأمة المدينة","what_is_not_ar":"ليس الطاعة الاختيارية ولا الحساب والجزاء ولا الدين المالي نفسه"},"support_links":[]},{"boundary":"Tekrarlanarak yerleşen davranış veya alışılmış durum çekirdektir; inanç sistemi, mali borç ve zorlayıcı egemenlik bu dala ait değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000504/B005","candidate_links":[{"candidate_id":"cand_e47b50c54e45b0d58ce0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:6:2:1","qac_word_ref":"109:6:2","surface_ar":"دِينُ"},{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:6:4:1","qac_word_ref":"109:6:4","surface_ar":"دِينِ"}],"gloss":"alışılmış davranış ve öteden beri bilinen hal","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tekrarlanarak yerleşmiş alışkanlık veya sürekli yapılan iş."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi veya topluluk için öteden beri bilinen hal, tutum ve gidiş."}}],"root_ar":"د ي ن","root_id":"root_000504","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tekrarlanan davranışı ve bundan oluşan yerleşik durum veya tutumu birlikte anlatan genel karşılıktır.","boundary_detail":"Tekrarlanarak yerleşen davranış veya alışılmış durum çekirdektir; inanç sistemi, mali borç ve zorlayıcı egemenlik bu dala ait değildir.","branch_image_ar":"العادة والشأن","concept_gloss":"alışılmış davranış ve öteden beri bilinen hal","contextual_glosses":[{"applicability":"Tekrarlanan ve kişide ya da toplulukta yerleşmiş davranışın öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Davranıştan daha geniş olan bilinen hal ve genel tutum kapsamını açıkça vermez.","preserves":"Tekrarlanarak yerleşen davranış ve olağan işi korur."},"facet_ids":["F001"],"text":"alışkanlık","usage_role":"general"},{"applicability":"Bir kişinin öteden beri bilinen durumu veya olağan gidişi anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tekrarlı davranış olarak alışkanlık anlamını doğrudan belirtmez.","preserves":"Bilinen durum, olağan tutum ve süreklilik yönlerini korur."},"facet_ids":["F002"],"text":"süregelen hal ve tutum","usage_role":"contextual"}],"definition":"Bir kişinin veya topluluğun tekrarla yerleşmiş alışkanlığı, süregelen işi ya da öteden beri bilinen hali ve tutumu.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tekrarlanarak yerleşmiş alışkanlık veya sürekli yapılan iş."},{"facet_id":"F002","role":"extension","statement":"Bir kişi veya topluluk için öteden beri bilinen hal, tutum ve gidiş."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":"Güncel Türkçede kurumsal inanç sistemi anlamını baskın biçimde ekler.","collision":"Aynı kökün inanç ve bağlılık dalıyla karışır.","fit":"drifted_loanword","loses":"Alışkanlık ve öteden beri bilinen hal anlamını güncel kullanımda göstermez.","preserves":"Tarihsel kullanımda yerleşik yol veya tutum çağrışımını kısmen koruyabilir."},"text":"din"},{"category":"alternative","error_profile":{"adds":"Fiziksel güzergah, yöntem ve araç gibi ilgisiz anlamları kapsama ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Yerleşik davranış biçimi ve olağan gidiş yönünü kısmen korur."},"text":"yol"}],"identity_rationale":"Kaynak ifadesi sözcüğü alışkanlık, süregelen iş, bilinen hal ve kişinin öteden beri tanınan durumu olarak açıklar. Verilen alışkanlık ve durum çerçevesi bu ortak anlamı eksiksiz karşılar.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"alışkanlık, olağan iş ve öteden beri bilinen hal"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"kalbinin alışkanlığı; ayrıca alçaltma, istemediği şeye zorlama veya eski gönül derdi diye yorumlanan tartışmalı söz"}],"lexicalization_note":"Dal yalın alışkanlık adını ve yorumları ayrışan bir deyimi içerir; deyimin alçaltma, zorlama veya gönül derdi yorumları yalın alışkanlık anlamına eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sürekli alışkanlık, ısrarlı uğraş ve izlenen yol ile kurulan üç sınır seçildi. Öbür adaylar huy, örnek alma veya düzgün gidiş gibi daha dar örnekler sunduğundan eklenmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yerleşik alışkanlıktan bilinen hale genişler; komşu dalın ayırıcı yönü işin kesintisiz veya düzenli biçimde aynı halde sürmesidir.","focus_only":"Odak dal alışkanlığın yanında kişinin bilinen hali ve genel tutumunu da kapsar.","gloss":"yerleşik alışkanlık ile sürekli gidiş","neighbor_only":"Komşu dal bir işin aynı durumda durmadan sürdürülmesini daha belirgin biçimde öne çıkarır.","neighbor_ref":"root_000456/B002","relation_type":"near_synonym","shared_zone":"Her iki dal tekrarlanarak olağanlaşan davranış ve süregelen işi anlatır."},{"boundary_match":"partial","distinction":"Odak dal nötr bir alışkanlık ve durum adıdır; komşu dal belirli bir söz veya uğraş üzerinde sürekli durma ve düşkünlük yönünü de taşır.","focus_only":"Odak dal genel alışkanlığı ve öteden beri bilinen hali kapsar.","gloss":"genel alışkanlık ile sürekli uğraş","neighbor_only":"Komşu dal bir şeyi sürekli anma veya ona düşkünlük gibi ısrarlı uğraşıları da içerir.","neighbor_ref":"root_001578/B009","relation_type":"near_synonym","shared_zone":"İki dalda da kişiye yerleşen ve yinelenen davranış veya uğraş vardır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği alışkanlık ve bilinen durumdur; komşu dal bu alanı kişinin izlediği yöntem veya yön olarak da kurar.","focus_only":"Odak dal kişinin yerleşik davranışını ve bilinen halini adlandırır.","gloss":"alışkanlık ile izlenen yol","neighbor_only":"Komşu dal alışılmış davranışın yanında izlenen yöntem, yön veya güzergah anlamını da taşır.","neighbor_ref":"root_000240/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal yerleşmiş davranış biçimi veya olağan gidiş için kullanılabilir."}],"source_phrase_ar":"العادة يقال لها دين (maqayis)؛ الدين بالكسر العادة والشأن (sihah)؛ الدين أيضا العادة (tahdhib)؛ الحال والأمر الذي تعهده (maqayis)","source_summary":"Kanıt alışkanlık ile süregelen işi ortak çekirdek sayar ve bu anlamı kişinin bilinen hali, olağan tutumu veya öteden beri tanınan durumu yönünde genişletir.","sources":["MQ","SI","TA"],"what_is_ar":"الدين بمعنى العادة والشأن والحال المعهود والدأب","what_is_not_ar":"ليس الشريعة والطاعة ولا الحساب ولا الدين المالي"},"support_links":["sup_0d044233a4749f947e97"]},{"boundary":"Kent temel anlamdır; yönetime uyma yalnızca kaynaklarda verilen adlandırma açıklamasıdır. Köleleştirilmiş kadın adı ve genel bağlılık anlamı bu dala aktarılmaz.","branch_kind":"bare","branch_ref":"root_000504/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:6:2:1","qac_word_ref":"109:6:2","surface_ar":"دِينُ"},{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:6:4:1","qac_word_ref":"109:6:4","surface_ar":"دِينِ"}],"gloss":"kent","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanların toplu yaşadığı büyük ve düzenli yerleşim olan kent."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kent adının, yöneticilerin buyruklarına uyulan yer olmasıyla kökensel olarak açıklanması."}}],"root_ar":"د ي ن","root_id":"root_000504","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın doğrudan gösterdiği büyük ve düzenli yerleşim için eksiksiz doğal karşılıktır; adlandırma gerekçesi ayrıca açıklanır.","boundary_detail":"Kent temel anlamdır; yönetime uyma yalnızca kaynaklarda verilen adlandırma açıklamasıdır. Köleleştirilmiş kadın adı ve genel bağlılık anlamı bu dala aktarılmaz.","branch_image_ar":"مدينة الطاعة","concept_gloss":"kent","contextual_glosses":[{"applicability":"Kent sözcüğünün yerleşim türü olarak açıklanmasının gerektiği bağlamlarda kullanılır.","error_profile":{"adds":"Kent düzeyinde örgütlenmemiş büyük yerleşimleri de kapsayabilir.","collision":null,"fit":"broadening","loses":null,"preserves":"İnsanların toplu yaşadığı geniş yerleşim olma yönünü korur."},"facet_ids":["F001"],"text":"büyük yerleşim","usage_role":"explanatory"}],"definition":"İnsanların toplu yaşadığı büyük ve düzenli yerleşim, yani kent. Adlandırılması, o yerde yöneticilerin buyruklarına uyulmasıyla açıklanır; bu ilişki kentin zorunlu özelliği değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanların toplu yaşadığı büyük ve düzenli yerleşim olan kent."},{"facet_id":"F002","role":"source_variant","statement":"Kent adının, yöneticilerin buyruklarına uyulan yer olmasıyla kökensel olarak açıklanması."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yalnızca belirli bir yönetim biçimine bağlı özel kent türü olduğu izlenimini ekler.","collision":"Adlandırma açıklamasını tanımlayıcı bir kent alt türüyle karıştırır.","fit":"displacement","loses":"Her tür kenti karşılayan yalın ve genel yerleşim anlamını kaybeder.","preserves":"Kent adıyla yönetime uyma arasında kurulan kökensel bağı korur."},"text":"buyruk kenti"}],"identity_rationale":"Kaynak ifadesinin doğrudan gösterdiği varlık kent veya büyük yerleşimdir. Yöneticilerin buyruğuna uyulması, bu yer adının neden aynı kök ailesinde açıklandığına ilişkin bir adlandırma gerekçesidir; her kentin tanımlayıcı koşulu değildir. Dal korunabilir, ancak tanım bu ayrımı açıkça yapmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kent; yöneticilerin buyruğuna uyulan yer olarak açıklanan büyük yerleşim"}],"lexicalization_note":"Mekanik sınıf yalındır; tanım kent biçiminin yerleşim anlamıyla sınırlı tutulur ve adlandırma açıklaması bağımsız bir anlam gibi genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel kent, köyleri toplayan bölge ve yönetici rolüyle kurulan üç sınır seçildi. Özel yer adları yalnızca örnek, karşı gelme ve kardeş dallar ise kökensel ya da tematik bağ sunduğundan yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalın kent anlamını belirli bir adlandırma açıklamasıyla verir; komşu dalın kapsamı kentten ülkeye ve surlu yapılaşmış alana kadar genişler.","focus_only":"Odak dal kent adını yöneticilerin buyruğuna uyulan yer biçimindeki kökensel açıklamayla ilişkilendirir.","gloss":"kent ile yapılaşmış ve surlu yer","neighbor_only":"Komşu dal kentle birlikte ülke, yapılaşmış toprak ve surlu yer gibi daha geniş yer türlerini kapsar.","neighbor_ref":"root_001408/B001","relation_type":"near_synonym","shared_zone":"Her iki dal insanların toplu yaşadığı yapılaşmış büyük yerleşimi adlandırır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği kentin kendisidir; komşu dalda kent, çevredeki küçük yerleşimleri kapsayan daha geniş bir bölgesel birimin merkezi olabilir.","focus_only":"Odak dal kendi başına büyük ve düzenli yerleşim olan kenti anlatır.","gloss":"kent ile köyleri toplayan bölge","neighbor_only":"Komşu dal çevresindeki köy ve mahalleleri bir araya getiren bölge veya yönetim çevresini de anlatır.","neighbor_ref":"root_001330/B005","relation_type":"near_neighbor","shared_zone":"İki dal da yerleşimlerin toplandığı büyük bir merkez için kullanılabilir."},{"boundary_match":"field_only","distinction":"Odak dal fiziksel yerleşimdir ve yönetim yalnızca adlandırma açıklamasında görünür; komşu dal ise topluluk üzerinde görev ve yetki taşıyan kişiyi anlatır.","focus_only":"Odak dal yönetimin gerçekleştiği fiziksel yerleşimi adlandırır.","gloss":"yönetilen yer ile yöneten görevli","neighbor_only":"Komşu dal bir topluluğun işini yürüten yönetici, görevli veya başkan rolünü adlandırır.","neighbor_ref":"root_000709/B003","relation_type":"same_field","shared_zone":"Her iki dal kent veya topluluk yönetimi sahnesinde yer alabilir."}],"source_phrase_ar":"المدينة كأنها مفعلة سميت بذلك لأنها تقام فيها طاعة ذوي الأمر (maqayis)؛ ومنه سمى المصر مدينة (sihah)؛ جعل بعضهم المدينة من هذا الباب (mufradat)","source_summary":"Kanıt yerleşim anlamını kent olarak verir ve bu adın yöneticilerin buyruklarına uyulan yer düşüncesiyle açıklandığını bildirir; kökensel açıklama yerleşim tanımından ayrı tutulmalıdır.","sources":["MQ","SI","MU"],"what_is_ar":"المدينة بمعنى المصر والموضع الذي تقام فيه طاعة ذوي الأمر","what_is_not_ar":"ليست المدينة الأمة المملوكة ولا العبد المدين في هذا الفرع"},"support_links":[]},{"boundary":"Anlam yalnızca verilen kişi, yargı ve yemin yapılarında geçerlidir; genel inanma, yönetim yetkisi devretme, borçlandırma veya hüküm verme anlamına genişletilmez.","branch_kind":"non_bare","branch_ref":"root_000504/B007","candidate_links":[{"candidate_id":"cand_1f721da6c6045ede9489","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:6:2:1","qac_word_ref":"109:6:2","surface_ar":"دِينُ"},{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:6:4:1","qac_word_ref":"109:6:4","surface_ar":"دِينِ"}],"gloss":"kişiyi sözüne ve vicdani sorumluluğuna göre değerlendirme","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiyi kendi vicdani yükümlülüğüyle baş başa bırakmak."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yargıda veya kişiyle Tanrı arasındaki konuda onun sözünü doğru kabul etmek."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yemin edenin sözünü ve yükümlülüğünü kendi niyetine göre değerlendirmek."}}],"root_ar":"د ي ن","root_id":"root_000504","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin sözünü doğru sayma, sorumluluğu ona bırakma ve yeminini kendi niyetine göre yorumlama yönlerini birlikte anlatır.","boundary_detail":"Anlam yalnızca verilen kişi, yargı ve yemin yapılarında geçerlidir; genel inanma, yönetim yetkisi devretme, borçlandırma veya hüküm verme anlamına genişletilmez.","branch_image_ar":"التصديق والتفويض","concept_gloss":"kişiyi sözüne ve vicdani sorumluluğuna göre değerlendirme","contextual_glosses":[{"applicability":"Bir kişinin yükümlülüğünün kendisiyle Tanrı arasındaki bağına bırakıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yargıda sözünü doğru kabul etme ve yemini niyetine göre değerlendirme yönlerini dışarıda bırakır.","preserves":"Sorumluluğu kişinin kendisine bırakma yönünü korur."},"facet_ids":["F001"],"text":"vicdani sorumluluğuyla baş başa bırakma","usage_role":"contextual"},{"applicability":"Bir kişinin yargıda veya vicdani konuda doğru söylediğinin kabul edildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sorumluluğu kişiye bırakma ile yemin niyetini ölçü alma yönlerini dışarıda bırakır.","preserves":"Kişinin sözüne güvenme ve onu doğru sayma yönünü korur."},"facet_ids":["F002"],"text":"sözünü doğru kabul etme","usage_role":"contextual"},{"applicability":"Yemin sözünün kapsamı belirlenirken söyleyen kişinin niyetinin esas alındığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel vicdani sorumluluk ve yargıda söze güvenme kullanımlarını dışarıda bırakır.","preserves":"Yeminin söyleyen kişinin niyetine bağlanması yönünü korur."},"facet_ids":["F003"],"text":"yemini söyleyenin niyetine göre yorumlama","usage_role":"contextual"}],"definition":"Bir kişiyi kendi vicdani yükümlülüğü ve sözüyle baş başa bırakmak veya yargıda sözünü doğru kabul etmek; yemin edenin sözünü de onun kendi niyetine göre değerlendirmek.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiyi kendi vicdani yükümlülüğüyle baş başa bırakmak."},{"facet_id":"F002","role":"specialization","statement":"Yargıda veya kişiyle Tanrı arasındaki konuda onun sözünü doğru kabul etmek."},{"facet_id":"F003","role":"specialization","statement":"Yemin edenin sözünü ve yükümlülüğünü kendi niyetine göre değerlendirmek."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Karar veya yönetim yetkisinin resmen başka kişiye verildiği anlamını ekler.","collision":"Genel görevlendirme ve temsil ilişkisiyle karışır.","fit":"displacement","loses":"Kişinin sözüne güvenme ve vicdani yükümlülüğünü ölçü alma yönlerini kaybeder.","preserves":"Bir işi veya sorumluluğu başka kişiye bırakma yönünü kısmen korur."},"text":"yetki devri"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Vicdani sorumluluğu kişiye bırakma ve yemini niyetine göre değerlendirme kapsamını kaybeder.","preserves":"Bir kişinin sözünü doğru kabul etme yönünü korur."},"text":"doğrulama"},{"category":"confusable","error_profile":{"adds":"Kanıtta bulunmayan, kişiye yeni bir yemin söyletme eylemini ekler.","collision":"Yeminin yorumlanmasını yemin isteme eylemiyle karıştırır.","fit":"displacement","loses":"Söylenmiş yemini söyleyenin niyetine göre değerlendirme işlemini kaybeder.","preserves":"Yemin sahnesiyle olan bağlantıyı korur."},"text":"yemin ettirme"}],"identity_rationale":"Kaynak ifadesi genel bir yetki devrinden çok, kişiyi kendi vicdani yükümlülüğüyle baş başa bırakmayı, yargıda veya kişiyle Tanrı arasındaki konuda sözünü doğru kabul etmeyi ve yemini söyleyenin niyetine göre değerlendirmeyi anlatır. Dal korunabilir, ancak genel görevlendirme anlamından bu güven ve sorumluluk ilişkisine çekilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"onu vicdani yükümlülüğüyle baş başa bıraktı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yargıda veya Tanrı'yla arasındaki konuda sözünü doğru kabul etti"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"yeminini kendi niyetine göre değerlendirdi"}],"lexicalization_note":"Dal yalnızca kanıtta verilen kişi, yargı ve yemin yapılarıyla sözlükselleşmiştir; bunlardan bağımsız bir yalın kök anlamı varsayılmaz.","neighbor_coverage_note":"Sunulan bütün adaylar değerlendirildi; genel doğrulama, işi başkasına bırakma ve karar yetkisi verme ile oluşan üç sınır seçildi. Yemin sunma, yemini bozma, suç yükleme ve benzer görevlendirme adayları bu sınırları yinelediği için eklenmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yargı, vicdani yükümlülük ve yemin yapılarıyla sınırlıdır; komşu dal ise bu yapılara bağlı olmadan genel doğrulama ve inanmayı anlatır.","focus_only":"Odak dal sorumluluğu kişiye bırakmayı ve yemin niyetini ölçü almayı da içerir.","gloss":"sınırlı bağlamda söze güvenme ile genel inanma","neighbor_only":"Komşu dal haber veya sözü doğru saymaktan dinsel inanca kadar uzanan genel inanmayı kapsar.","neighbor_ref":"root_000054/B002","relation_type":"near_synonym","shared_zone":"Her iki dal bir kişinin sözünü doğru ve güvenilir kabul etme alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dalda kişi kendi iç yükümlülüğü ve beyanıyla baş başa bırakılır; komşu dalda ise işi yapma veya kararı yürütme yetkisi başka birine aktarılır.","focus_only":"Odak dal kişiyi kendi sözüne ve vicdani sorumluluğuna bırakır.","gloss":"vicdana bırakma ile işi başkasına bırakma","neighbor_only":"Komşu dal bir işi veya kararı başka bir kişiye verip onun yürütmesine dayanmayı anlatır.","neighbor_ref":"root_001187/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da bir konunun başka bir kişinin sorumluluğuna bırakılması vardır."},{"boundary_match":"partial","distinction":"Odak dal güveni kişinin beyanı ve vicdani sorumluluğuyla sınırlar; komşu dal kişiyi karar veren makam durumuna getirir.","focus_only":"Odak dal yargıda kişinin sözünü doğru sayar, ancak ona hüküm verme yetkisi tanımaz.","gloss":"söze güvenme ile karar yetkisi verme","neighbor_only":"Komşu dal uyuşmazlıkta karar verme yetkisini seçilen kişiye bırakır ve onun hükmünü geçerli kılar.","neighbor_ref":"root_000348/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal bir yargı veya uyuşmazlık bağlamında başka bir kişiye güvenmeyi içerir."}],"source_phrase_ar":"دينت الرجل تديينا إذا وكلته إلى دينه (sihah)؛ دينت الرجل في القضاء وفيما بينه وبين الله أي صدقته (tahdhib)؛ دينت الحالف أي نويته فيما حلف وهو التديين (tahdhib)","source_summary":"Kanıt, kişiyi kendi vicdani sorumluluğuna bırakma ile belirli yargı ve yemin bağlamlarında onun sözüne güvenmeyi birleştirir; yemin kullanımında belirleyici olan söyleyenin niyetidir.","sources":["SI","TA"],"what_is_ar":"التديين بمعنى تصديق الرجل في القضاء أو الحلف أو تفويضه إلى دينه","what_is_not_ar":"ليس الطاعة العامة ولا الدين المالي ولا الحكم والجزاء"},"support_links":["sup_2ab10a84ab4c68f5cc53"]}],"candidate_inventory":[{"anchor_refs":["109:6:1"],"branch_refs":[],"candidate_id":"cand_08b6ad93dfbd320883fb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:6:1:addressee-pronoun","source_type":"word_analysis","support_ids":["sup_26fea27f698ed734ef5a","sup_b238ef97d261119fdc6a"],"title":"plural addressees are built into the predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:1","qac_refs":["109:6:1:1","109:6:1:2"],"status":"accepted"}},{"anchor_refs":["109:6:1"],"branch_refs":[],"candidate_id":"cand_ac3857fba7ee23334bc1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:6:1:boundary-domain-verdict","source_type":"word_analysis","support_ids":["sup_6af25727571f402cd7b5","sup_b238ef97d261119fdc6a"],"title":"worship dispute becomes domain verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:1","qac_refs":["109:6:1:1","109:6:1:2"],"status":"accepted"}},{"anchor_refs":["109:6:1"],"branch_refs":[],"candidate_id":"cand_86f7ecf4044c16dbb76b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:6:1:fronted-assignment","source_type":"word_analysis","support_ids":["sup_1d2fcbbce201c09d4d44","sup_b238ef97d261119fdc6a"],"title":"fronted lām assigns the addressee domain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:1","qac_refs":["109:6:1:1","109:6:1:2"],"status":"accepted"}},{"anchor_refs":["109:6:1"],"branch_refs":[],"candidate_id":"cand_b88552b3f09d03f9a605","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:6:1:mirror-and-sound-frame","source_type":"word_analysis","support_ids":["sup_0c7679f545bf2a2d396e","sup_b238ef97d261119fdc6a"],"title":"first half closes and prepares the mirror","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:1","qac_refs":["109:6:1:1","109:6:1:2"],"status":"accepted"}},{"anchor_refs":["109:6:1"],"branch_refs":[],"candidate_id":"cand_d251fe9a5399946a13b5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:6:1:restriction-before-noun","source_type":"word_analysis","support_ids":["sup_5e332b1226e5d74daf7a","sup_b238ef97d261119fdc6a"],"title":"fronting restricts before the noun appears","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:1","qac_refs":["109:6:1:1","109:6:1:2"],"status":"accepted"}},{"anchor_refs":["109:6:2"],"branch_refs":[],"candidate_id":"cand_55769821124a219f1589","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:2:abstract-singular-form","source_type":"word_analysis","support_ids":["sup_82c628090fa22e6f3aa1","sup_98b1f3731adc3e0db936"],"title":"singular abstract noun gathers the plural side","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:2","qac_refs":["109:6:2:1","109:6:2:2"],"status":"accepted"}},{"anchor_refs":["109:6:2"],"branch_refs":[],"candidate_id":"cand_8a7b877c1a54639e26cf","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:2:boundary-from-worship-to-domain","source_type":"word_analysis","support_ids":["sup_3923859fb90fadf4520e","sup_82c628090fa22e6f3aa1"],"title":"dīn names the field behind worship","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:2","qac_refs":["109:6:2:1","109:6:2:2"],"status":"accepted"}},{"anchor_refs":["109:6:2"],"branch_refs":[],"candidate_id":"cand_ec435c06fa114b14c9ab","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:2:delayed-subject-predication","source_type":"word_analysis","support_ids":["sup_82c628090fa22e6f3aa1","sup_f6ab8e5b168f1c07b85d"],"title":"delayed subject completes the verbless assignment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:2","qac_refs":["109:6:2:1","109:6:2:2"],"status":"accepted"}},{"anchor_refs":["109:6:2"],"branch_refs":[],"candidate_id":"cand_f3b4207a0c6ce55fc2e8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:2:derivative-images-narrowed","source_type":"word_analysis","support_ids":["sup_82c628090fa22e6f3aa1","sup_e1955bfc6c228b71ff17"],"title":"debt and governance images are pressure, not replacement","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:2","qac_refs":["109:6:2:1","109:6:2:2"],"status":"accepted"}},{"anchor_refs":["109:6:2"],"branch_refs":[],"candidate_id":"cand_d2bc0646435a758931d6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:2:distribution-and-sound","source_type":"word_analysis","support_ids":["sup_82c628090fa22e6f3aa1","sup_96c91b2c13b1e7fe21cd"],"title":"common root channel and sound-core support the mirror","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:2","qac_refs":["109:6:2:1","109:6:2:2"],"status":"accepted"}},{"anchor_refs":["109:6:2"],"branch_refs":[],"candidate_id":"cand_859f023d0820560fa289","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:2:double-addressee-marking","source_type":"word_analysis","support_ids":["sup_82c628090fa22e6f3aa1","sup_c06f479cef39c5dc9c09"],"title":"the addressee is marked twice","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:2","qac_refs":["109:6:2:1","109:6:2:2"],"status":"accepted"}},{"anchor_refs":["109:6:2"],"branch_refs":[],"candidate_id":"cand_cd35b043bd5b08093929","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:2:possessed-definite-domain","source_type":"word_analysis","support_ids":["sup_5eda8684e6493a9fddc0","sup_82c628090fa22e6f3aa1"],"title":"possession makes the dīn definite","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:2","qac_refs":["109:6:2:1","109:6:2:2"],"status":"accepted"}},{"anchor_refs":["109:6:2"],"branch_refs":[],"candidate_id":"cand_a772f54c6b2aa64bc4c6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:2:possessor-shift-mirror","source_type":"word_analysis","support_ids":["sup_562137bbd0dbefde83ca","sup_82c628090fa22e6f3aa1"],"title":"same noun returns with a new possessor","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:2","qac_refs":["109:6:2:1","109:6:2:2"],"status":"accepted"}},{"anchor_refs":["109:6:2"],"branch_refs":[],"candidate_id":"cand_e6922ba3d85370b4d50f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:2:restricted-nontransferable-domain","source_type":"word_analysis","support_ids":["sup_82c628090fa22e6f3aa1","sup_bb660343d435f30666f2"],"title":"fronting and possession lock the domain to its side","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:2","qac_refs":["109:6:2:1","109:6:2:2"],"status":"accepted"}},{"anchor_refs":["109:6:2"],"branch_refs":[],"candidate_id":"cand_8a3334b2e7be9e0586c3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:2:root-breadth-binding-system","source_type":"word_analysis","support_ids":["sup_3611926c64fbc2cb1c7f","sup_82c628090fa22e6f3aa1"],"title":"root breadth names a binding system","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:2","qac_refs":["109:6:2:1","109:6:2:2"],"status":"accepted"}},{"anchor_refs":["109:6:3"],"branch_refs":[],"candidate_id":"cand_a5c54f9b504e56e56863","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:6:3:complete-clause-hinge","source_type":"word_analysis","support_ids":["sup_d73dc29f3dfba0a72e63","sup_e3ab7f876415f53fd8a4"],"title":"wāw links two complete clauses","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:3","qac_refs":["109:6:3:1"],"status":"accepted"}},{"anchor_refs":["109:6:3"],"branch_refs":[],"candidate_id":"cand_19ac0f4563290ed7be18","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:6:3:coordination-and-contrast","source_type":"word_analysis","support_ids":["sup_d73dc29f3dfba0a72e63","sup_d8befcd46a09c949ab0c"],"title":"coordination and contrast stay live","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:3","qac_refs":["109:6:3:1"],"status":"accepted"}},{"anchor_refs":["109:6:3"],"branch_refs":[],"candidate_id":"cand_862b715e6df8c8f54bae","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:6:3:surface-fusion-pivot","source_type":"word_analysis","support_ids":["sup_34a92303be39b2e86d39","sup_d73dc29f3dfba0a72e63"],"title":"wa-liya makes the pivot audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:3","qac_refs":["109:6:3:1"],"status":"accepted"}},{"anchor_refs":["109:6:4"],"branch_refs":[],"candidate_id":"cand_aa88df01d277a573fe3a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:6:4:compact-wa-liya-cluster","source_type":"word_analysis","support_ids":["sup_6b6c2f93e3796f665b62","sup_a7b3bf2452ddb24e09ac"],"title":"connector, lām, and pronoun compress the turn","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:4","qac_refs":["109:6:3:2","109:6:3:3"],"status":"accepted"}},{"anchor_refs":["109:6:4"],"branch_refs":[],"candidate_id":"cand_cbd9d19893a28c1acdc7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:6:4:first-person-assignment","source_type":"word_analysis","support_ids":["sup_6b6c2f93e3796f665b62","sup_d9f8f075e87a7ea0cddb"],"title":"speaker is built into the second predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:4","qac_refs":["109:6:3:2","109:6:3:3"],"status":"accepted"}},{"anchor_refs":["109:6:4"],"branch_refs":[],"candidate_id":"cand_d6f89cc05a4d4c0b5f67","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:6:4:mirror-restriction","source_type":"word_analysis","support_ids":["sup_3600e625b69799718f2e","sup_6b6c2f93e3796f665b62"],"title":"the second half mirrors the first with changed person","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:4","qac_refs":["109:6:3:2","109:6:3:3"],"status":"accepted"}},{"anchor_refs":["109:6:4"],"branch_refs":[],"candidate_id":"cand_fd1c748b1befbf8427ed","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:6:4:qiraat-first-person-sound","source_type":"word_analysis","support_ids":["sup_6b6c2f93e3796f665b62","sup_f24ce7e784243b924374"],"title":"qiraat vary the sound, not the assignment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:4","qac_refs":["109:6:3:2","109:6:3:3"],"status":"accepted"}},{"anchor_refs":["109:6:4"],"branch_refs":[],"candidate_id":"cand_8a95fbf224a72c05d412","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"109:6:4:soft-speaker-cadence","source_type":"word_analysis","support_ids":["sup_6b6c2f93e3796f665b62","sup_b95839a08b6523b63a58"],"title":"speaker-side cadence differs from kum closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:4","qac_refs":["109:6:3:2","109:6:3:3"],"status":"accepted"}},{"anchor_refs":["109:6:5"],"branch_refs":[],"candidate_id":"cand_2f40feea2e2f96610944","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:5:abstract-final-domain","source_type":"word_analysis","support_ids":["sup_17d1f5df6101423400b1","sup_53b5f65c7d3f102d1fd7"],"title":"the surah closes on a domain, not an action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:5","qac_refs":["109:6:4:1","109:6:4:2"],"status":"accepted"}},{"anchor_refs":["109:6:5"],"branch_refs":[],"candidate_id":"cand_a9b2206110686be479f5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:5:balanced-binary-closure","source_type":"word_analysis","support_ids":["sup_2dce244755c14f644143","sup_53b5f65c7d3f102d1fd7"],"title":"second dīn completes the binary frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:5","qac_refs":["109:6:4:1","109:6:4:2"],"status":"accepted"}},{"anchor_refs":["109:6:5"],"branch_refs":[],"candidate_id":"cand_2e0815f765ef3885d1a0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:5:boundary-demarcation","source_type":"word_analysis","support_ids":["sup_53b5f65c7d3f102d1fd7","sup_5c25b038d4a73aaff85b"],"title":"argument scene becomes demarcation scene","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:5","qac_refs":["109:6:4:1","109:6:4:2"],"status":"accepted"}},{"anchor_refs":["109:6:5"],"branch_refs":[],"candidate_id":"cand_e9c586d65fec10fa2d7b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:5:closing-sound-weight","source_type":"word_analysis","support_ids":["sup_53b5f65c7d3f102d1fd7","sup_6cd66e1ce45b61eef165"],"title":"variant endings alter the closing weight","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:5","qac_refs":["109:6:4:1","109:6:4:2"],"status":"accepted"}},{"anchor_refs":["109:6:5"],"branch_refs":[],"candidate_id":"cand_36b112a0eb8e9988b85b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:5:compact-hafs-possession","source_type":"word_analysis","support_ids":["sup_4c462e3de438b4e59d77","sup_53b5f65c7d3f102d1fd7"],"title":"Hafs closes with compact ownership","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:5","qac_refs":["109:6:4:1","109:6:4:2"],"status":"accepted"}},{"anchor_refs":["109:6:5"],"branch_refs":[],"candidate_id":"cand_2aec39ecd08a8ff0cd26","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:5:derivative-pressure","source_type":"word_analysis","support_ids":["sup_53b5f65c7d3f102d1fd7","sup_5b3d798bc7f7d263948a"],"title":"obligation and jurisdiction color the final noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:5","qac_refs":["109:6:4:1","109:6:4:2"],"status":"accepted"}},{"anchor_refs":["109:6:5"],"branch_refs":[],"candidate_id":"cand_01e6f459da25d5ce89c0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:5:double-first-person-marking","source_type":"word_analysis","support_ids":["sup_53b5f65c7d3f102d1fd7","sup_fdf5b64bf4f530841d41"],"title":"speaker occupies predicate and noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:5","qac_refs":["109:6:4:1","109:6:4:2"],"status":"accepted"}},{"anchor_refs":["109:6:5"],"branch_refs":[],"candidate_id":"cand_493b2baac7ecc394281f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:5:final-possessed-subject","source_type":"word_analysis","support_ids":["sup_53b5f65c7d3f102d1fd7","sup_89f5f9ce51be0c3ad8a5"],"title":"final noun is possessed and syntactically central","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:5","qac_refs":["109:6:4:1","109:6:4:2"],"status":"accepted"}},{"anchor_refs":["109:6:5"],"branch_refs":[],"candidate_id":"cand_0bb3a315f23d1d76f240","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:5:lived-social-domain","source_type":"word_analysis","support_ids":["sup_53b5f65c7d3f102d1fd7","sup_8973c5bfea31ce690d2c"],"title":"custom and social order remain bounded pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:5","qac_refs":["109:6:4:1","109:6:4:2"],"status":"accepted"}},{"anchor_refs":["109:6:5"],"branch_refs":[],"candidate_id":"cand_44c45ad2aa079cc8beba","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:5:speaker-root-breadth","source_type":"word_analysis","support_ids":["sup_53b5f65c7d3f102d1fd7","sup_9152df926a1a051bf19c"],"title":"speaker's dīn carries comprehensive accountable breadth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:5","qac_refs":["109:6:4:1","109:6:4:2"],"status":"accepted"}},{"anchor_refs":["109:6:5"],"branch_refs":[],"candidate_id":"cand_acd77ab45264cbbdfaa9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:5:unnamed-context-defined-din","source_type":"word_analysis","support_ids":["sup_03d9b71a40d8b3ea347a","sup_53b5f65c7d3f102d1fd7"],"title":"standard final dīn remains unnamed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:5","qac_refs":["109:6:4:1","109:6:4:2"],"status":"accepted"}},{"anchor_refs":["109:6:5"],"branch_refs":[],"candidate_id":"cand_71f41daf2a9c4d8d00ea","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:5:variant-explicitness","source_type":"word_analysis","support_ids":["sup_44481decc554b5178016","sup_53b5f65c7d3f102d1fd7"],"title":"variants expose explicitness without replacing Hafs","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"109:6:5","qac_refs":["109:6:4:1","109:6:4:2"],"status":"accepted"}},{"anchor_refs":["109:6:2"],"branch_refs":[],"candidate_id":"cand_ac71048b7d7d56283c61","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000504"],"scope":"focus_ayah","source_local_id":"109:6:2:1","source_type":"qac_morpheme","support_ids":["sup_642f4ca073332d7389fe"],"title":"QAC root occurrence: د ي ن","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["109:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"109:6","branch_refs":["root_000504/B001"],"candidate_id":"cand_8882b9eec0590aa63da3","commentary_obligation":"review","hft_ref":"hft_f57e11f24f541e503649","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_partitioned_allegiance","source_type":"hft","support_ids":["sup_2e34bf38722ea59f979a"],"title":"base_partitioned_allegiance","trust":"legacy_unbound"},{"anchor_refs":["109:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"109:6","branch_refs":["root_000504/B002"],"candidate_id":"cand_d4e94cca58249ed19e7a","commentary_obligation":"review","hft_ref":"hft_0bb7590d7db46426a6f6","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_separate_reckonings","source_type":"hft","support_ids":["sup_968c8cfa281ad0d77160"],"title":"base_separate_reckonings","trust":"legacy_unbound"},{"anchor_refs":["109:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"109:6","branch_refs":["root_000504/B003"],"candidate_id":"cand_863d13f6f886afccca62","commentary_obligation":"review","hft_ref":"hft_c81836c14fd257f88446","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_nontransferable_obligations","source_type":"hft","support_ids":["sup_38c769067c21d02a15d7"],"title":"base_nontransferable_obligations","trust":"legacy_unbound"},{"anchor_refs":["109:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"109:6","branch_refs":["root_000504/B005"],"candidate_id":"cand_e47b50c54e45b0d58ce0","commentary_obligation":"review","hft_ref":"hft_c1d5a490186abd853a7e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_customary_courses","source_type":"hft","support_ids":["sup_0d044233a4749f947e97"],"title":"base_customary_courses","trust":"legacy_unbound"},{"anchor_refs":["109:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"109:6","branch_refs":["root_000504/B007"],"candidate_id":"cand_1f721da6c6045ede9489","commentary_obligation":"review","hft_ref":"hft_90319ed603f350848286","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_delegated_responsibility","source_type":"hft","support_ids":["sup_2ab10a84ab4c68f5cc53"],"title":"base_delegated_responsibility","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"لَكُمْ دِينُكُمْ وَلِىَ دِينِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"109:6:1:1","qac_word_ref":"109:6:1","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|2MP","morpheme_role":"STEM","pos":"PRON","qac_ref":"109:6:1:2","qac_word_ref":"109:6:1","root_ar":"","surface_ar":"كُمْ"},{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:6:2:1","qac_word_ref":"109:6:2","root_ar":"د ي ن","surface_ar":"دِينُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"109:6:2:2","qac_word_ref":"109:6:2","root_ar":"","surface_ar":"كُمْ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"109:6:3:1","qac_word_ref":"109:6:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"109:6:3:2","qac_word_ref":"109:6:3","root_ar":"","surface_ar":"لِ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|1S","morpheme_role":"STEM","pos":"PRON","qac_ref":"109:6:3:3","qac_word_ref":"109:6:3","root_ar":"","surface_ar":"ىَ"},{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:6:4:1","qac_word_ref":"109:6:4","root_ar":"د ي ن","surface_ar":"دِينِ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1S","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"109:6:4:2","qac_word_ref":"109:6:4","root_ar":"","surface_ar":""}],"word_analysis_qac_refs":[["109:6:1:1","109:6:1:2"],["109:6:2:1","109:6:2:2"],["109:6:3:1"],["109:6:3:2","109:6:3:3"],["109:6:4:1","109:6:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["109:6:1","109:6:2","109:6:3","109:6:4","109:6:5"]},"focus_surface_evidence":{"arabic_uthmani":"لَكُمْ دِينُكُمْ وَلِىَ دِينِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"109:6:1:1","qac_word_ref":"109:6:1","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|2MP","morpheme_role":"STEM","pos":"PRON","qac_ref":"109:6:1:2","qac_word_ref":"109:6:1","root_ar":"","surface_ar":"كُمْ"},{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:6:2:1","qac_word_ref":"109:6:2","root_ar":"د ي ن","surface_ar":"دِينُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"109:6:2:2","qac_word_ref":"109:6:2","root_ar":"","surface_ar":"كُمْ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"109:6:3:1","qac_word_ref":"109:6:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"109:6:3:2","qac_word_ref":"109:6:3","root_ar":"","surface_ar":"لِ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|1S","morpheme_role":"STEM","pos":"PRON","qac_ref":"109:6:3:3","qac_word_ref":"109:6:3","root_ar":"","surface_ar":"ىَ"},{"lemma_ar":"دِين","morph_features":"STEM|POS:N|LEM:diyn|ROOT:dyn|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"109:6:4:1","qac_word_ref":"109:6:4","root_ar":"د ي ن","surface_ar":"دِينِ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1S","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"109:6:4:2","qac_word_ref":"109:6:4","root_ar":"","surface_ar":""}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["109:6:1:1","109:6:1:2"],["109:6:2:1","109:6:2:2"],["109:6:3:1"],["109:6:3:2","109:6:3:3"],["109:6:4:1","109:6:4:2"]],"word_analysis_refs":["109:6:1","109:6:2","109:6:3","109:6:4","109:6:5"],"word_rows":[{"analysis_record_ref":"109:6:1","analytic_gloss_range_en":"fronted lām predicate with second-person plural suffix, assigning the following dīn to the addressed group with restrictive force","analytic_root_gloss_range_en":null,"qac_refs":["109:6:1:1","109:6:1:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَكُمْ","transliteration":"lakum"}},{"analysis_record_ref":"109:6:2","analytic_gloss_range_en":"the addressees' possessed dīn as delayed subject: a definite, singular, owned domain of accountable practice rather than an unowned abstraction","analytic_root_gloss_range_en":"religion, obedience, lived way, judgment, recompense, debt, obligation, governance, subjection, custom, and ordering; local noun selects a comprehensive possessed system while concrete debt or civic images remain narrowed pressure","qac_refs":["109:6:2:1","109:6:2:2"],"root":{"arabic":"د ي ن","transliteration":"d-y-n"},"surface":{"arabic":"دِينُكُمْ","transliteration":"dīnukum"}},{"analysis_record_ref":"109:6:3","analytic_gloss_range_en":"connector between two complete nominal clauses, carrying coordination, contrast, and possible resumption without collapsing the two assignments","analytic_root_gloss_range_en":null,"qac_refs":["109:6:3:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"109:6:4","analytic_gloss_range_en":"fronted first-person lām predicate, mirrored against the addressee-side lām and assigning the following dīn to the quoted speaker","analytic_root_gloss_range_en":null,"qac_refs":["109:6:3:2","109:6:3:3"],"root":{"note":"no lexical root"},"surface":{"arabic":"لِيَ","transliteration":"liya"}},{"analysis_record_ref":"109:6:5","analytic_gloss_range_en":"the speaker's possessed dīn as the final delayed subject, compactly carrying first-person possession through the ending and closing the surah on an owned accountable domain","analytic_root_gloss_range_en":"religion, obedience, lived way, judgment, recompense, debt, obligation, governance, subjection, custom, and ordering; local final noun selects the speaker's possessed comprehensive domain while variant and derivative evidence remain bounded by the standard clause","qac_refs":["109:6:4:1","109:6:4:2"],"root":{"arabic":"د ي ن","transliteration":"d-y-n"},"surface":{"arabic":"دِينِ","transliteration":"dīni"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["109:6"],"branch_refs":["root_000504/B001"],"candidate_id":"cand_8882b9eec0590aa63da3","evidence_scope":"focus_ayah","hft_ref":"hft_f57e11f24f541e503649","item_id":"base_partitioned_allegiance","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_partitioned_allegiance","support_id":"sup_2e34bf38722ea59f979a"},{"anchor_refs":["109:6"],"branch_refs":["root_000504/B002"],"candidate_id":"cand_d4e94cca58249ed19e7a","evidence_scope":"focus_ayah","hft_ref":"hft_0bb7590d7db46426a6f6","item_id":"base_separate_reckonings","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_separate_reckonings","support_id":"sup_968c8cfa281ad0d77160"},{"anchor_refs":["109:6"],"branch_refs":["root_000504/B003"],"candidate_id":"cand_863d13f6f886afccca62","evidence_scope":"focus_ayah","hft_ref":"hft_c81836c14fd257f88446","item_id":"base_nontransferable_obligations","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_nontransferable_obligations","support_id":"sup_38c769067c21d02a15d7"},{"anchor_refs":["109:6"],"branch_refs":["root_000504/B005"],"candidate_id":"cand_e47b50c54e45b0d58ce0","evidence_scope":"focus_ayah","hft_ref":"hft_c1d5a490186abd853a7e","item_id":"base_customary_courses","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_customary_courses","support_id":"sup_0d044233a4749f947e97"},{"anchor_refs":["109:6"],"branch_refs":["root_000504/B007"],"candidate_id":"cand_1f721da6c6045ede9489","evidence_scope":"focus_ayah","hft_ref":"hft_90319ed603f350848286","item_id":"base_delegated_responsibility","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_delegated_responsibility","support_id":"sup_2ab10a84ab4c68f5cc53"}],"diagnostics":[],"lane_counts":{"global":10,"macro":11,"micro":5},"packet_summary":{"ayah_count":6,"focus_ref":"109:6","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]}],"window":["109:1","109:2","109:3","109:4","109:5","109:6"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"109:6","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":16,"unstructured_record_count":0},"identity":{"ayah_ref":"109:6","lane":"micro","linguistic_source_ref":"109:6","surface_ref":"109:6","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"109:6","target_tokens":[["Sizin",["109:6:2"]],["dininiz",["109:6:2"]],["size",["109:6:1"]],["benim",["109:6:4"]],["dinim",["109:6:4"]],["de",["109:6:3"]],["bana",["109:6:3"]]],"text":"Sizin dininiz size, benim dinim de bana."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":6,"id":"s109-p01-001-006","label":"Whole surah","number":1,"refs":["109:1","109:2","109:3","109:4","109:5","109:6"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:5:unnamed-context-defined-din","source_type":"word_analysis","support_id":"sup_03d9b71a40d8b3ea347a","text":"{\"blocking_evidence\":null,\"headline\":\"standard final dīn remains unnamed\",\"reader_payoff\":\"The reader notices that the final noun is defined by the preceding worship-refusal sequence rather than by an added label.\",\"reason\":\"The standard wording ends with unqualified {{ar:دِينِ}} ({{tr:dīni}}), while the preceding ayahs supply the worship context that gives the speaker's domain its content.\",\"representative_source_ids\":[\"QF-521e892f\",\"QB-f83d0439\",\"MS-b83a42f9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:1:mirror-and-sound-frame","source_type":"word_analysis","support_id":"sup_0c7679f545bf2a2d396e","text":"{\"blocking_evidence\":null,\"headline\":\"first half closes and prepares the mirror\",\"reader_payoff\":\"The reader hears the first half as a self-contained addressee-side beat that will be mirrored by the speaker-side half.\",\"reason\":\"The repeated local dīn pair and the nasal pattern in {{ar:لَكُمْ دِينُكُمْ}} ({{tr:lakum dīnukum}}) support the first half as a closed member of the later binary pairing.\",\"representative_source_ids\":[\"MT-2684450b\",\"QP-1c3031d7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:5:abstract-final-domain","source_type":"word_analysis","support_id":"sup_17d1f5df6101423400b1","text":"{\"blocking_evidence\":null,\"headline\":\"the surah closes on a domain, not an action\",\"reader_payoff\":\"The reader notices that the final landing is a domain noun after the earlier worship actions.\",\"reason\":\"The last word is a noun and the final word of the surah, so closure falls on the speaker's owned dīn rather than on another verb of worship, judging, or owing.\",\"representative_source_ids\":[\"QF-6530c72c\",\"QT-83639f08\",\"QT-87336536\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:1:fronted-assignment","source_type":"word_analysis","support_id":"sup_1d2fcbbce201c09d4d44","text":"{\"blocking_evidence\":null,\"headline\":\"fronted lām assigns the addressee domain\",\"reader_payoff\":\"The reader notices that the ayah begins by assigning the domain to the addressees before naming the domain itself.\",\"reason\":\"QAC and attachment evidence identify {{ar:لَكُمْ}} ({{tr:lakum}}) as a fronted prepositional predicate of {{ar:دِينُكُمْ}} ({{tr:dīnukum}}), so the lām relation is assignment or specification rather than a loose locative filler.\",\"representative_source_ids\":[\"QG-57871944\",\"MG-040e07f3\",\"QS-5eb69fd0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:1:addressee-pronoun","source_type":"word_analysis","support_id":"sup_26fea27f698ed734ef5a","text":"{\"blocking_evidence\":null,\"headline\":\"plural addressees are built into the predicate\",\"reader_payoff\":\"The reader notices that the addressed group is not merely implied; the plural suffix is fused to the very word that assigns the domain.\",\"reason\":\"The suffix in {{ar:لَكُمْ}} ({{tr:lakum}}) is resolved to the plural addressees, and the surface word compresses lām plus the second-person plural pronoun.\",\"representative_source_ids\":[\"QG-7a076c7e\",\"MG-4e4b80d0\",\"QF-025d9242\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:5:balanced-binary-closure","source_type":"word_analysis","support_id":"sup_2dce244755c14f644143","text":"{\"blocking_evidence\":null,\"headline\":\"second dīn completes the binary frame\",\"reader_payoff\":\"The reader notices that the same noun returns with a changed possessor, producing symmetry rather than escalation.\",\"reason\":\"{{ar:دِينِ}} ({{tr:dīni}}) answers {{ar:دِينُكُمْ}} ({{tr:dīnukum}}) with the same lexical core and noun class while changing the possessor.\",\"representative_source_ids\":[\"QI-1eaf79c0\",\"QT-852587d2\",\"QE-96214fa3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:3:surface-fusion-pivot","source_type":"word_analysis","support_id":"sup_34a92303be39b2e86d39","text":"{\"blocking_evidence\":null,\"headline\":\"wa-liya makes the pivot audible\",\"reader_payoff\":\"The reader hears the turn into the speaker-side assignment as one recited cluster, not as a detached pause.\",\"reason\":\"The conjunction is pronounced into the following lām phrase as {{ar:وَلِيَ}} ({{tr:wa-liya}}), placing the sound hinge exactly at the shift from addressee side to speaker side.\",\"representative_source_ids\":[\"QF-4ec0828e\",\"QT-b021c018\",\"QP-fb3839cf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:4:mirror-restriction","source_type":"word_analysis","support_id":"sup_3600e625b69799718f2e","text":"{\"blocking_evidence\":null,\"headline\":\"the second half mirrors the first with changed person\",\"reader_payoff\":\"The reader notices that the speaker's side receives the same restrictive grammar as the addressee side, with person changed rather than structure weakened.\",\"reason\":\"The second nominal clause repeats the fronted lām plus possessed dīn architecture of the first clause, but changes from second-person plural to first-person singular.\",\"representative_source_ids\":[\"MG-7f3db225\",\"QI-8105a9d4\",\"QT-e3255d5e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:2:root-breadth-binding-system","source_type":"word_analysis","support_id":"sup_3611926c64fbc2cb1c7f","text":"{\"blocking_evidence\":null,\"headline\":\"root breadth names a binding system\",\"reader_payoff\":\"The reader notices that dīn here is thicker than a label: it names an accountable way, obligation, judgment, and ordering system.\",\"reason\":\"V4 accepts branches around worship or obedience, recompense, debt, subjection, and custom, but local grammar selects the abstract possessed noun {{ar:دِينُكُمْ}} ({{tr:dīnukum}}), so the branches survive as comprehensive binding pressure rather than separate activated senses.\",\"representative_source_ids\":[\"QS-a4ad86a4\",\"QS-f06eb5ad\",\"MS-4c855258\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:2:boundary-from-worship-to-domain","source_type":"word_analysis","support_id":"sup_3923859fb90fadf4520e","text":"{\"blocking_evidence\":null,\"headline\":\"dīn names the field behind worship\",\"reader_payoff\":\"The reader notices that the final ayah names the broader domain after the earlier worship-action refusals.\",\"reason\":\"The closing ayah moves from repeated worship vocabulary into the paired dīn nouns, making domain-language the surah's final answer.\",\"representative_source_ids\":[\"QB-6fa5465f\",\"QE-42428687\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:5:variant-explicitness","source_type":"word_analysis","support_id":"sup_44481decc554b5178016","text":"{\"blocking_evidence\":null,\"headline\":\"variants expose explicitness without replacing Hafs\",\"reader_payoff\":\"The reader notices a scale from compact possession to explicit naming, while the standard clause keeps the final noun brief.\",\"reason\":\"Readings such as {{ar:دِينِي}} ({{tr:dīnī}}), {{ar:دِينْ دِينِي}} ({{tr:dīn dīnī}}), and supplied {{ar:دِينِي الْإِسْلَامُ}} ({{tr:dīnī l-Islāmu}}) make possession or identification more explicit, but they serve as apparatus against the local standard {{ar:دِينِ}} ({{tr:dīni}}).\",\"representative_source_ids\":[\"QF-4042650e\",\"QF-7070d743\",\"QF-813d6561\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:5:compact-hafs-possession","source_type":"word_analysis","support_id":"sup_4c462e3de438b4e59d77","text":"{\"blocking_evidence\":null,\"headline\":\"Hafs closes with compact ownership\",\"reader_payoff\":\"The reader notices that possession is grammatically active even when the final first-person yā is not fully visible in the Hafs surface.\",\"reason\":\"The Hafs form {{ar:دِينِ}} ({{tr:dīni}}) carries first-person possession compactly through the ending, and the parallel with {{ar:لِيَ}} ({{tr:liya}}) resolves the ownership.\",\"representative_source_ids\":[\"QF-ddf86105\",\"QF-f3d984b9\",\"QG-47e179c3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:5","source_type":"word_analysis","support_id":"sup_53b5f65c7d3f102d1fd7","text":"{\"gloss_range\":\"the speaker's possessed dīn as the final delayed subject, compactly carrying first-person possession through the ending and closing the surah on an owned accountable domain\",\"prose\":\"{{ar:دِينِ}} ({{tr:dīni}}) closes the ayah and the surah as the delayed subject of {{ar:لِيَ}} ({{tr:liya}}). Its final -i is doing dense work: the noun remains the subject of the second nominal clause while first-person possession makes it the speaker's own assigned domain. The same broad {{ar:د ي ن}} ({{tr:d-y-n}}) field returns from {{ar:دِينُكُمْ}} ({{tr:dīnukum}}), so the closure is not a private label but a complete accountable order of way, obligation, judgment, jurisdiction, practiced state, social ordering, and allegiance. Hafs keeps this possession compact, while readings with full dīnī, repeated dīn dīnī, and supplied dīnī l-Islāmu show a scale from compact ownership to explicit naming and heavier final sound; the standard form leaves the dīn unnamed and lets the preceding worship-refusal sequence define it. The final paired noun therefore marks where the domains stand after the argument over shared worship, rather than escalating into another worship action.\",\"root_display\":\"{{ar:د ي ن}} ({{tr:d-y-n}})\",\"root_gloss_range\":\"religion, obedience, lived way, judgment, recompense, debt, obligation, governance, subjection, custom, and ordering; local final noun selects the speaker's possessed comprehensive domain while variant and derivative evidence remain bounded by the standard clause\",\"surface_display\":\"{{ar:دِينِ}} ({{tr:dīni}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:2:possessor-shift-mirror","source_type":"word_analysis","support_id":"sup_562137bbd0dbefde83ca","text":"{\"blocking_evidence\":null,\"headline\":\"same noun returns with a new possessor\",\"reader_payoff\":\"The reader notices the controlled mirror: the lexical core stays the same while ownership changes from plural addressees to singular speaker.\",\"reason\":\"{{ar:دِينُكُمْ}} ({{tr:dīnukum}}) is paired locally with {{ar:دِينِ}} ({{tr:dīni}}), matching root and noun class while changing possessor.\",\"representative_source_ids\":[\"QI-5b31820e\",\"QT-1e97b212\",\"QE-54e54371\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:5:derivative-pressure","source_type":"word_analysis","support_id":"sup_5b3d798bc7f7d263948a","text":"{\"blocking_evidence\":null,\"headline\":\"obligation and jurisdiction color the final noun\",\"reader_payoff\":\"The reader notices obligation, judgment, and jurisdictional pressure inside the speaker's owned domain without turning the word into debt or government alone.\",\"reason\":\"Debt, judgment, subjection, custom, and governance branches remain valid pressure, but the local surface is the possessed abstract noun {{ar:دِينِ}} ({{tr:dīni}}).\",\"representative_source_ids\":[\"QS-0b3f0421\",\"QS-a08d169b\",\"QS-ba896c23\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:5:boundary-demarcation","source_type":"word_analysis","support_id":"sup_5c25b038d4a73aaff85b","text":"{\"blocking_evidence\":null,\"headline\":\"argument scene becomes demarcation scene\",\"reader_payoff\":\"The reader notices that the surah ends by marking where the domains stand, not by continuing the argument over shared worship.\",\"reason\":\"The mirrored structure makes ownership stable across compact and expanded forms, so the final scene is demarcation of domains after the negated worship sequence.\",\"representative_source_ids\":[\"QB-a4591fdd\",\"QY-ad139fe7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:1:restriction-before-noun","source_type":"word_analysis","support_id":"sup_5e332b1226e5d74daf7a","text":"{\"blocking_evidence\":null,\"headline\":\"fronting restricts before the noun appears\",\"reader_payoff\":\"The reader notices the restrictive route: the statement opens with the holder-side and only then names what is held.\",\"reason\":\"The nominal clause has a fronted predicate and delayed subject, with no overt verb, so the order itself creates a restrictive allocation frame.\",\"representative_source_ids\":[\"QI-877cf8f7\",\"QT-271ff162\",\"QT-c785f60b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:2:possessed-definite-domain","source_type":"word_analysis","support_id":"sup_5eda8684e6493a9fddc0","text":"{\"blocking_evidence\":null,\"headline\":\"possession makes the dīn definite\",\"reader_payoff\":\"The reader notices that the noun is not a generic religious category; it is made definite and owned by the addressees.\",\"reason\":\"QAC marks {{ar:دِينُكُمْ}} ({{tr:dīnukum}}) as a possessive construct with the second-person plural suffix, and attachment evidence resolves that suffix to the addressed group.\",\"representative_source_ids\":[\"QG-8305cebd\",\"QF-9409bbf4\",\"QF-69b2b264\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"109:6:2:1","source_type":"qac_morpheme","support_id":"sup_642f4ca073332d7389fe","text":"{\"lemma_ar\":\"دِين\",\"morph_features\":\"STEM|POS:N|LEM:diyn|ROOT:dyn|M|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"109:6:2:1\",\"qac_word_ref\":\"109:6:2\",\"root_ar\":\"د ي ن\",\"surface_ar\":\"دِينُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:1:boundary-domain-verdict","source_type":"word_analysis","support_id":"sup_6af25727571f402cd7b5","text":"{\"blocking_evidence\":null,\"headline\":\"worship dispute becomes domain verdict\",\"reader_payoff\":\"The reader notices the turn from repeated worship refusals in 109:2-5 to a final allocation of domains in 109:6.\",\"reason\":\"The ayah's first word begins a verbless nominal declaration after the preceding worship-verb sequence, making the boundary movement structural as well as lexical.\",\"representative_source_ids\":[\"MI-290dc00c\",\"QB-c9af97fd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:4","source_type":"word_analysis","support_id":"sup_6b6c2f93e3796f665b62","text":"{\"gloss_range\":\"fronted first-person lām predicate, mirrored against the addressee-side lām and assigning the following dīn to the quoted speaker\",\"prose\":\"{{ar:لِيَ}} ({{tr:liya}}) repeats the lām-assignment grammar of {{ar:لَكُمْ}} ({{tr:lakum}}), but now the attached pronoun routes the domain to the singular quoted speaker. With the preceding connector, the recited cluster compresses hinge, lām, and first-person pronoun before {{ar:دِينِ}} ({{tr:dīni}}), so the second half is not a fragment but a full mirrored nominal clause. Its qiraat pressure is acoustic rather than lexical: open wa-liya and closed wa-lī expose how strongly the first-person ending is sounded while keeping the assignment stable. In Hafs, liya dīni gives the speaker-side phrase a softer ī-ya-ī cadence against the heavier addressee-side -kum closure.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لِيَ}} ({{tr:liya}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:5:closing-sound-weight","source_type":"word_analysis","support_id":"sup_6cd66e1ce45b61eef165","text":"{\"blocking_evidence\":null,\"headline\":\"variant endings alter the closing weight\",\"reader_payoff\":\"The reader hears that compact finality and expanded possession are alternate recitational textures around the same speaker-side assignment.\",\"reason\":\"Variant evidence can lengthen or repeat the final possession, but the local Hafs ending stays compact and the reference does not change.\",\"representative_source_ids\":[\"QI-57a7080a\",\"QP-3d3b69d2\",\"QP-e8b9ed52\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:2","source_type":"word_analysis","support_id":"sup_82c628090fa22e6f3aa1","text":"{\"gloss_range\":\"the addressees' possessed dīn as delayed subject: a definite, singular, owned domain of accountable practice rather than an unowned abstraction\",\"prose\":\"{{ar:دِينُكُمْ}} ({{tr:dīnukum}}) is the delayed subject that completes the first nominal clause: not an object pulled under the lām, but the thing whose ownership is being predicated. The attached second-person plural suffix makes the abstract noun definite through its holders, while the matching addressee marking in {{ar:لَكُمْ}} ({{tr:lakum}}) locks the same group into both recipient and possessor positions. The singular noun gathers the plural addressees into one assigned system, enclosed on their side rather than offered as a shared or transferable field. The root range keeps the noun broad in the root's main abstract-noun channel: lived way, obligation, judgment, jurisdictional order, custom, submission, and social-order pressure can press on the word, but the local form selects a possessed comprehensive domain, not a financial debt or a separate city image. After the earlier worship-action refusals, this noun names the broader domain those acts belong to; because the same noun returns as {{ar:دِينِ}} ({{tr:dīni}}), the ayah holds the lexical field steady while the possessors change.\",\"root_display\":\"{{ar:د ي ن}} ({{tr:d-y-n}})\",\"root_gloss_range\":\"religion, obedience, lived way, judgment, recompense, debt, obligation, governance, subjection, custom, and ordering; local noun selects a comprehensive possessed system while concrete debt or civic images remain narrowed pressure\",\"surface_display\":\"{{ar:دِينُكُمْ}} ({{tr:dīnukum}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:5:lived-social-domain","source_type":"word_analysis","support_id":"sup_8973c5bfea31ce690d2c","text":"{\"blocking_evidence\":null,\"headline\":\"custom and social order remain bounded pressure\",\"reader_payoff\":\"The reader notices that the speaker-side dīn is socially and habitually comprehensive, while the final word remains the local abstract noun.\",\"reason\":\"Custom, civic ordering, and derivational-dispute evidence sharpen the sense of being bound under an order, but they do not override the local first-person possessed noun.\",\"representative_source_ids\":[\"QS-9f3a5d87\",\"QS-acbf10c0\",\"QS-c9a83685\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:5:final-possessed-subject","source_type":"word_analysis","support_id":"sup_89f5f9ce51be0c3ad8a5","text":"{\"blocking_evidence\":null,\"headline\":\"final noun is possessed and syntactically central\",\"reader_payoff\":\"The reader notices that the last word is not dangling: it is the subject of the speaker-side assignment and is possessed by the speaker.\",\"reason\":\"QAC marks {{ar:دِينِ}} ({{tr:dīni}}) as the delayed subject of the second nominal clause, and attachment evidence licenses the first-person possessive relation.\",\"representative_source_ids\":[\"QG-47e179c3\",\"QG-c81bdfab\",\"QG-cf121389\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:5:speaker-root-breadth","source_type":"word_analysis","support_id":"sup_9152df926a1a051bf19c","text":"{\"blocking_evidence\":null,\"headline\":\"speaker's dīn carries comprehensive accountable breadth\",\"reader_payoff\":\"The reader notices that the speaker's dīn is a complete accountable order, not merely an inward preference or label.\",\"reason\":\"V4 supports the broad {{ar:د ي ن}} ({{tr:d-y-n}}) field, but the local final noun is still the abstract possessed {{ar:دِينِ}} ({{tr:dīni}}), so the breadth is realized as accountable domain rather than separate branch replacement.\",\"representative_source_ids\":[\"QS-21001218\",\"QS-7ae71bf5\",\"QY-253e742d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:2:distribution-and-sound","source_type":"word_analysis","support_id":"sup_96c91b2c13b1e7fe21cd","text":"{\"blocking_evidence\":null,\"headline\":\"common root channel and sound-core support the mirror\",\"reader_payoff\":\"The reader hears the shared long sound-core and sees the local form as part of the root's main abstract-noun channel.\",\"reason\":\"Contextual profiles treat the abstract noun as the root's common Quranic channel, and the two local dīn nouns share the long ī sound before suffix divergence.\",\"representative_source_ids\":[\"QI-c82ffce4\",\"QP-52df0590\",\"QP-8e911731\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:2:abstract-singular-form","source_type":"word_analysis","support_id":"sup_98b1f3731adc3e0db936","text":"{\"blocking_evidence\":null,\"headline\":\"singular abstract noun gathers the plural side\",\"reader_payoff\":\"The reader notices that the plural addressees are assigned one singular domain rather than scattered into many acts or debts.\",\"reason\":\"The word is a singular abstract noun with a plural possessive suffix, and it follows a worship-verb sequence as a domain noun rather than another event-form.\",\"representative_source_ids\":[\"QF-2e5e3890\",\"QF-38f5d90d\",\"QF-d81422c3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:4:compact-wa-liya-cluster","source_type":"word_analysis","support_id":"sup_a7b3bf2452ddb24e09ac","text":"{\"blocking_evidence\":null,\"headline\":\"connector, lām, and pronoun compress the turn\",\"reader_payoff\":\"The reader notices a compact grammatical turn from the plural addressees to the singular worshipping speaker.\",\"reason\":\"The surface cluster {{ar:وَلِيَ}} ({{tr:wa-liya}}) carries conjunction, lām, and first-person suffix before the noun, and the first-person referent is the quoted speaker already active in the surah's worship statements.\",\"representative_source_ids\":[\"QF-51490ac3\",\"QT-b6ec7bf4\",\"QB-79f2a412\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:1","source_type":"word_analysis","support_id":"sup_b238ef97d261119fdc6a","text":"{\"gloss_range\":\"fronted lām predicate with second-person plural suffix, assigning the following dīn to the addressed group with restrictive force\",\"prose\":\"{{ar:لَكُمْ}} ({{tr:lakum}}) begins the closing declaration as a fronted assignment: the addressee-side comes before the noun, so the clause first says where the domain belongs. The attached plural suffix keeps the addressed group inside the predicate, and the following {{ar:دِينُكُمْ}} ({{tr:dīnukum}}) completes a verbless allocation rather than a new action. This opening also shifts the surah from the worship-refusal sequence of 109:2-5 into a settled domain verdict: the first half starts with allocation, sounds closed through its m-n-m nasality, and prepares the mirror in {{ar:لِيَ}} ({{tr:liya}}).\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَكُمْ}} ({{tr:lakum}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:4:soft-speaker-cadence","source_type":"word_analysis","support_id":"sup_b95839a08b6523b63a58","text":"{\"blocking_evidence\":null,\"headline\":\"speaker-side cadence differs from kum closure\",\"reader_payoff\":\"The reader hears the speaker-side phrase as a softer first-person cadence against the heavier addressee-side closure.\",\"reason\":\"The Hafs phrase {{ar:لِيَ دِينِ}} ({{tr:liya dīni}}) produces an ī-ya-ī movement, while the broader topic also converges grammar, restriction, and qiraat surface at the speaker-side close.\",\"representative_source_ids\":[\"QP-4fdb2cf8\",\"QY-9d41f6f9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:2:restricted-nontransferable-domain","source_type":"word_analysis","support_id":"sup_bb660343d435f30666f2","text":"{\"blocking_evidence\":null,\"headline\":\"fronting and possession lock the domain to its side\",\"reader_payoff\":\"The reader notices that the addressees' domain is enclosed on their side, not offered as a shared or transferable space.\",\"reason\":\"The fronted {{ar:لَكُمْ}} ({{tr:lakum}}) and the suffix of {{ar:دِينُكُمْ}} ({{tr:dīnukum}}) point to the same addressees, giving the first half a restrictive, non-transferable assignment.\",\"representative_source_ids\":[\"QI-857d9519\",\"QB-a5e2b741\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:2:double-addressee-marking","source_type":"word_analysis","support_id":"sup_c06f479cef39c5dc9c09","text":"{\"blocking_evidence\":null,\"headline\":\"the addressee is marked twice\",\"reader_payoff\":\"The reader notices that the addressees occupy both the predicate-side recipient and the noun-side possessor positions.\",\"reason\":\"The suffix in {{ar:لَكُمْ}} ({{tr:lakum}}) and the suffix in {{ar:دِينُكُمْ}} ({{tr:dīnukum}}) are both second-person plural and both resolve to the addressed group.\",\"representative_source_ids\":[\"QG-bca05bea\",\"QY-14a19bb3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:3","source_type":"word_analysis","support_id":"sup_d73dc29f3dfba0a72e63","text":"{\"gloss_range\":\"connector between two complete nominal clauses, carrying coordination, contrast, and possible resumption without collapsing the two assignments\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) is the hinge between two complete nominal clauses. It connects the declarations without making one subordinate to the other: the first half remains the addressee-side assignment, and the second half opens as the speaker-side counterpart. Because the connector is recited into {{ar:لِيَ دِينِ}} ({{tr:liya dīni}}), the turn is both grammatical and audible, a controlled pivot from plural holders to the singular speaker.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:3:coordination-and-contrast","source_type":"word_analysis","support_id":"sup_d8befcd46a09c949ab0c","text":"{\"blocking_evidence\":null,\"headline\":\"coordination and contrast stay live\",\"reader_payoff\":\"The reader notices that the hinge balances equivalence and separation: the halves correspond, but they do not merge.\",\"reason\":\"QAC allows coordination, contrast, and resumption, and the mirrored restrictive clauses make the local force contrastive coordination rather than simple addition alone.\",\"representative_source_ids\":[\"MG-e63440bb\",\"QS-8cb5d13b\",\"QI-49779148\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:4:first-person-assignment","source_type":"word_analysis","support_id":"sup_d9f8f075e87a7ea0cddb","text":"{\"blocking_evidence\":null,\"headline\":\"speaker is built into the second predicate\",\"reader_payoff\":\"The reader notices that the speaker is grammatically placed inside the assignment word before the speaker's dīn is named.\",\"reason\":\"QAC and attachment evidence identify {{ar:لِيَ}} ({{tr:liya}}) as a preposition plus first-person pronoun functioning as the fronted predicate of {{ar:دِينِ}} ({{tr:dīni}}).\",\"representative_source_ids\":[\"QG-a2a32313\",\"QG-eaafca7c\",\"QS-226e2046\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:2:derivative-images-narrowed","source_type":"word_analysis","support_id":"sup_e1955bfc6c228b71ff17","text":"{\"blocking_evidence\":null,\"headline\":\"debt and governance images are pressure, not replacement\",\"reader_payoff\":\"The reader notices concrete obligation, jurisdiction, and social-order pressure inside the abstract noun without replacing it with debt, rule, or city vocabulary.\",\"reason\":\"The local form is the abstract noun {{ar:دِينُكُمْ}} ({{tr:dīnukum}}); debt, governance, custom, and civic derivatives can color the binding-system payoff but do not become the local lexical replacement.\",\"representative_source_ids\":[\"QS-3a8cc55d\",\"QS-70436a2b\",\"QS-9c274bc7\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:3:complete-clause-hinge","source_type":"word_analysis","support_id":"sup_e3ab7f876415f53fd8a4","text":"{\"blocking_evidence\":null,\"headline\":\"wāw links two complete clauses\",\"reader_payoff\":\"The reader notices that the second half has equal clausal standing rather than trailing as an appended phrase.\",\"reason\":\"Attachment evidence marks {{ar:لَكُمْ دِينُكُمْ}} ({{tr:lakum dīnukum}}) and {{ar:لِيَ دِينِ}} ({{tr:liya dīni}}) as parallel nominal clauses, so the connector joins complete declarations.\",\"representative_source_ids\":[\"QG-553ab749\",\"QG-963651e1\",\"QT-58bcf1af\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:4:qiraat-first-person-sound","source_type":"word_analysis","support_id":"sup_f24ce7e784243b924374","text":"{\"blocking_evidence\":null,\"headline\":\"qiraat vary the sound, not the assignment\",\"reader_payoff\":\"The reader hears that the first-person ending can be opened into the following noun or tightened before it, while the meaning stays assigned to the speaker.\",\"reason\":\"The supplied readings contrast {{ar:وَلِيَ}} ({{tr:wa-liya}}) with {{ar:وَلِي}} ({{tr:wa-lī}}); this affects recitational texture and pronoun release, not the local predicate relation.\",\"representative_source_ids\":[\"MG-e6bbf355\",\"QF-7a6a8447\",\"QP-96c14517\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:2:delayed-subject-predication","source_type":"word_analysis","support_id":"sup_f6ab8e5b168f1c07b85d","text":"{\"blocking_evidence\":null,\"headline\":\"delayed subject completes the verbless assignment\",\"reader_payoff\":\"The reader notices that the dīn stands as the subject of a verbless assignment, not as a genitive object of the preposition.\",\"reason\":\"The word is marked as nominative delayed subject after the fronted predicate {{ar:لَكُمْ}} ({{tr:lakum}}), so the clause predicates assignment without an overt verb.\",\"representative_source_ids\":[\"QG-d8e6adeb\",\"QG-e8dbcfc1\",\"QT-5d08de4f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"109:6:5:double-first-person-marking","source_type":"word_analysis","support_id":"sup_fdf5b64bf4f530841d41","text":"{\"blocking_evidence\":null,\"headline\":\"speaker occupies predicate and noun\",\"reader_payoff\":\"The reader notices the grammatical shift from plural addressee possession to singular speaker possession at the close.\",\"reason\":\"The first-person relation appears in {{ar:لِيَ}} ({{tr:liya}}) and again in {{ar:دِينِ}} ({{tr:dīni}}), while the first half used the second-person plural suffix.\",\"representative_source_ids\":[\"QG-663ff6bf\",\"QI-aadee970\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"لَكُمْ دِينُكُمْ وَلِىَ دِينِ","ayah_ref":"109:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000504/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000504","role":"Obedience and submission supplies the allegiance-content that the mirrored possessives allocate to separate parties.","root":"د ي ن","source_ref":"109:6","source_word_indices":["2","4"]}],"changed_reading":{"after":"Your governing allegiance remains yours, while my governing allegiance remains mine; grammatical balance marks a boundary, not equivalence.","before":"Each side simply has a religion."},"confidence":"strong","focus_anchor":"The mirrored allocations لكم ... ولي frame two occurrences of دين at words 2 and 4.","mechanism":"The same noun is assigned to two pronominal domains. The obedience branch makes each دين a governing allegiance, so the symmetry separates commitments without making them interchangeable.","model_id":"base_partitioned_allegiance"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_partitioned_allegiance","source_type":"hft","support_id":"sup_2e34bf38722ea59f979a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَكُمْ دِينُكُمْ وَلِىَ دِينِ","ayah_ref":"109:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000504/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000504","role":"Reckoning and recompense turns the repeated noun into two separately assigned trajectories of accounting and return.","root":"د ي ن","source_ref":"109:6","source_word_indices":["2","4"]}],"changed_reading":{"after":"The line can also partition reckonings: your course carries its account, and mine carries mine.","before":"The line partitions religious identities."},"confidence":"medium","focus_anchor":"The doubled دين is distributively possessed, once by the plural addressees and once by the speaker.","mechanism":"If دين activates reckoning and recompense, the two possessive slots resemble distinct accounts: neither party's judgment or return is grammatically transferred to the other.","model_id":"base_separate_reckonings"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_separate_reckonings","source_type":"hft","support_id":"sup_968c8cfa281ad0d77160","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَكُمْ دِينُكُمْ وَلِىَ دِينِ","ayah_ref":"109:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000504/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000504","role":"Debt and credit supplies the ledger-like obligation that each pronominal side bears separately.","root":"د ي ن","source_ref":"109:6","source_word_indices":["2","4"]}],"changed_reading":{"after":"The possessives can allocate nontransferable religious obligations: what is due from you is yours to bear, and what is due from me is mine.","before":"The possessives merely label two affiliations."},"confidence":"exploratory","focus_anchor":"لكم and لي place each occurrence of دين against a different holder.","mechanism":"The debt branch materializes دين as something owed or carried. Possessive symmetry then functions like two ledgers whose liabilities cannot be assumed, discharged, or exchanged by the other side.","model_id":"base_nontransferable_obligations"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_nontransferable_obligations","source_type":"hft","support_id":"sup_38c769067c21d02a15d7","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَكُمْ دِينُكُمْ وَلِىَ دِينِ","ayah_ref":"109:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000504/B005"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000504","role":"Habit and customary state supplies the repeated course of conduct assigned to each side.","root":"د ي ن","source_ref":"109:6","source_word_indices":["2","4"]}],"changed_reading":{"after":"دين can denote each side's accustomed way of living and recurring conduct.","before":"دين denotes a static confessional label."},"confidence":"medium","focus_anchor":"One lexeme is repeated across a balanced you/me construction rather than replaced by two different labels.","mechanism":"The habit branch makes دين a settled manner of proceeding. The line thus contrasts durable customary courses, not only stated creeds.","model_id":"base_customary_courses"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_customary_courses","source_type":"hft","support_id":"sup_0d044233a4749f947e97","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَكُمْ دِينُكُمْ وَلِىَ دِينِ","ayah_ref":"109:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000504/B007"],"payload":{"activation_trace":[{"branch_id":"B007","mapped_root_id":"root_000504","role":"Crediting and leaving to conscience supplies a bounded delegation of responsibility rather than approval of the other's position.","root":"د ي ن","source_ref":"109:6","source_word_indices":["2","4"]}],"changed_reading":{"after":"The line may instead decline to vouch across the boundary: you answer within your responsibility, and I within mine.","before":"The line grants two religions equal endorsement."},"confidence":"medium","focus_anchor":"The terminal balance gives the addressees their دين and the speaker his, with no shared possessive domain.","mechanism":"The crediting-and-delegation branch turns the allocation into a release of vouching: each party is left to its own religious responsibility and conscience.","model_id":"base_delegated_responsibility"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_delegated_responsibility","source_type":"hft","support_id":"sup_2ab10a84ab4c68f5cc53","trust":"legacy_unbound"}]}
</lane_packet_json>
