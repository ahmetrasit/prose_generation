# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **19:94**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s019-regular-20260912/s019/19_94/micro.discovery.json` and modify nothing
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
  "ayah_ref": "19:94",
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
{"analysis_context":{"analysis_id":"s019-regular-20260912","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"19:94","host_surah":19,"lane_context_refs":[],"ordered_context_refs":["19:77","19:78","19:79","19:80","19:81","19:82","19:83","19:84","19:85","19:86","19:87","19:88","19:89","19:90","19:91","19:92","19:93","19:95","19:96","19:97","19:98","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal küçük taşları ve bunlarla kaplı araziyi kapsar; sayma, zihinsel nitelik, kokulu madde parçası ve mesane hastalığı anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000332/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحْصَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aHoSaY`|ROOT:HSy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"19:94:2:1","qac_word_ref":"19:94:2","surface_ar":"أَحْصَىٰ"}],"gloss":"çakıl taşı, çakıllar ve çakıllı arazi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim, küçük taşların topluluğudur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tek bir küçük taş ve bunun çoğul biçimi ayrıca adlandırılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bir arazi yapısı, üzerinde küçük taşlar bulunması bakımından nitelenir."}}],"root_ar":"ح ص ي","root_id":"root_000332","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Küçük taşların toplu ve tekil gönderimini, ayrıca yalnız ilgili yapıda çakıllı arazi niteliğini birlikte temsil eder.","boundary_detail":"Dal küçük taşları ve bunlarla kaplı araziyi kapsar; sayma, zihinsel nitelik, kokulu madde parçası ve mesane hastalığı anlamlarını kapsamaz.","branch_image_ar":"الحصى والحصاة","concept_gloss":"çakıl taşı, çakıllar ve çakıllı arazi","contextual_glosses":[{"applicability":"Küçük taşların madde ya da topluluk olarak anıldığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çakıllı araziyi bildiren yapıya bağlı niteliği açıkça taşımaz.","preserves":"Küçük taşlar topluluğu anlamını korur."},"facet_ids":["F001","F002"],"text":"çakıl","usage_role":"general"},{"applicability":"Yalnız küçük taşlarla kaplı bir yerin nitelendiği yapı için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Küçük taşın kendisini ve taşlar topluluğunu adlandırmaz.","preserves":"Arazinin küçük taşlarla kaplı oluşunu korur."},"facet_ids":["F003"],"text":"çakıllı arazi","usage_role":"contextual"}],"definition":"Bir arada düşünülen küçük taşları, bunlardan tek bir taşı ve çoğulunu anlatır. Ayrı bir yapıda ise bu küçük taşlarla kaplı araziyi niteler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim, küçük taşların topluluğudur."},{"facet_id":"F002","role":"specialization","statement":"Tek bir küçük taş ve bunun çoğul biçimi ayrıca adlandırılır."},{"facet_id":"F003","role":"associated_use","statement":"Belirli bir arazi yapısı, üzerinde küçük taşlar bulunması bakımından nitelenir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Küçük olmayan her türlü taşı da kapsayan daha geniş bir sınıf ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Sert ve taş niteliğindeki nesne gönderimini korur."},"text":"taş"}],"identity_rationale":"Kaynak ifadesi küçük taşların toplu adıyla tek bir taşı ve çoğul biçimini açıkça verir; ayrıca çakıllı arazi kullanımını ayrı bir yapıya bağlar. Bu çerçeve, nesne anlamıyla arazi niteliğini birbirine karıştırmadan dal kimliğini destekler.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"küçük taşlar, çakıl"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"tek bir çakıl taşı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"çakıl taşları"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"çakıllı arazi"}],"lexicalization_note":"Tanım, küçük taşa ait yalın biçimleri çakıllı arazi bildiren kalıplaşmış yapıdan ayırır; arazi anlamı yalın sözcüğün bütün kullanımlarına yayılmaz.","neighbor_coverage_note":"Verilen bütün komşular taş, zemin veya aynı kökün ayrı anlamları bakımından değerlendirildi; yalnız boyut, zemin kapsamı ya da taş benzerliği üzerinden sınırı belirginleştiren adaylar yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yakın örtüşmeye rağmen komşu dal boyut bakımından daha geniştir ve taşları yere serme eylemine uzanır; odak dal ise küçük taşın tekil, çoğul ve araziye bağlı kullanımlarını sınırlar.","focus_only":"Tek bir küçük taşı, çoğulunu ve çakıllı arazi yapısını belirgin biçimde ayırır.","gloss":"çakıl ve çakıllı yer","neighbor_only":"Küçük ve büyük taşları birlikte kapsayabilir ve bir yeri bu taşlarla döşeme eylemini de içerir.","neighbor_ref":"root_000325/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da çakıl türü taşları ve bu taşların bulunduğu zemini kapsar."},{"boundary_match":"partial","distinction":"Odak dalın boyut özelliği küçüklüktür; komşu dal ise iri, sert ve kalın taş ya da kaya görünümünü esas alır.","focus_only":"Küçük taşları ve bunlarla kaplı araziyi anlatır.","gloss":"iri taş ve taşlık zemin","neighbor_only":"İri, sert taş kütlelerini ve kalın kayalık zemini öne çıkarır.","neighbor_ref":"root_000840/B005","relation_type":"near_neighbor","shared_zone":"İki dal da taşlı arazi ve taş parçaları alanında buluşur."},{"boundary_match":"partial","distinction":"Komşu dalın diş ve diş gıcırdatma uzantıları odak dalda yoktur; odak dalın küçük taş ve çakıllı zemin ayrımı da komşunun çekirdeğini oluşturmaz.","focus_only":"Küçük taş topluluğunu ve çakıllı araziyi düzenli biçimde adlandırır.","gloss":"taş ve sert azı dişi","neighbor_only":"Taş anlamının yanında azı dişlerini ve öfkeyle diş gıcırdatmayı da kapsar.","neighbor_ref":"root_000075/B005","relation_type":"near_neighbor","shared_zone":"Taş ya da çakıl niteliğindeki sert nesne gönderiminde sınırlı örtüşme vardır."},{"boundary_match":"partial","distinction":"Odak dal gerçek küçük taşları gösterirken komşu dal, taş benzerliğine dayanan bedensel bir hastalık ve oluşum sürecidir.","focus_only":"Dış dünyadaki küçük taşları ve taşlı zemini anlatır.","gloss":"mesane taşı hastalığı","neighbor_only":"Mesanede idrarın koyulaşıp taş benzeri sert bir oluşuma dönüşmesiyle ilgili hastalığı anlatır.","neighbor_ref":"root_000332/B006","relation_type":"near_neighbor","shared_zone":"Her iki dalda da küçük ve sert taş görünümü anlam bağını sağlar."}],"source_phrase_ar":"الحصى صغار الحجارة والواحدة حصاة وثلاث حصيات (ayn;tahdhib)؛ الحصاة واحدة الحصى وتجمع على حصيات (sihah)؛ أرض محصاة ذات حصى (sihah)","source_summary":"Kaynaklar küçük taşlar topluluğu ile bunun tekil ve çoğul adlandırmalarında birleşir; ayrıca küçük taşlı araziyi bildiren bağımlı yapı kaydedilir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه الحصى صغار الحجارة، والحصاة الواحدة، والحصيات، والأرض المحصاة ذات الحصى.","what_is_not_ar":"لا يدخل فيه العد والإحصاء، ولا حصاة العقل، ولا حصاة المسك، ولا داء الحصاة في المثانة."},"support_links":[]},{"boundary":"Dal kesin sayma ve sayıyı eksiksiz belirleme alanındadır; tahmin, genel hesap işlemleri ve yalnız çokluk bildiren kullanımlar çekirdeğin tamamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000332/B002","candidate_links":[{"candidate_id":"cand_dd433011ceaad84831fb","lane":"micro"},{"candidate_id":"cand_e2e332880fc30828c229","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحْصَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aHoSaY`|ROOT:HSy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"19:94:2:1","qac_word_ref":"19:94:2","surface_ar":"أَحْصَىٰ"}],"gloss":"sayıp sayısını eksiksiz belirleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin birimleri sayılarak sayısı belirlenir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sayım, bütün birimlerin eksiksiz kapsanması ve sayının bilgiyle kuşatılması düzeyine ulaşabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çakılın sayıca çokluğu, çok büyük bir sayıyı anlatan benzetmeye kaynak olur."}}],"root_ar":"ح ص ي","root_id":"root_000332","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sayma eylemiyle birlikte sayılanların tümünü kapsama ve sonucu eksiksiz bilme çekirdeğini temsil eder.","boundary_detail":"Dal kesin sayma ve sayıyı eksiksiz belirleme alanındadır; tahmin, genel hesap işlemleri ve yalnız çokluk bildiren kullanımlar çekirdeğin tamamı değildir.","branch_image_ar":"الإحصاء بالعدد والاستقصاء","concept_gloss":"sayıp sayısını eksiksiz belirleme","contextual_glosses":[{"applicability":"Bir şeyin birimlerini tek tek sayarak miktarını bulma bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eksiksiz bilgiyle bütün sayıyı kuşatma vurgusunu zorunlu olarak taşımaz.","preserves":"Birimleri sayarak miktarı belirleme işlemini korur."},"facet_ids":["F001"],"text":"saymak","usage_role":"general"},{"applicability":"Sayımın hiçbir birimi dışarıda bırakmadan kesin sonuca ulaştığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sayma, tam kapsam ve kesin nicelik bilgisi bileşenlerini birlikte korur."},"facet_ids":["F001","F002"],"text":"sayısını eksiksiz saptamak","usage_role":"explanatory"},{"applicability":"Sayının çakıl çokluğuna benzetilerek büyüklüğünün anlatıldığı bağlama özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gerçek sayma işlemini ve sayının eksiksiz bilgisini ifade etmez.","preserves":"Çok büyük sayı bildiren benzetmeli uzantıyı korur."},"facet_ids":["F003"],"text":"çakıl kadar çok","usage_role":"contextual"}],"definition":"Bir şeyi sayarak miktarını belirlemek ve sayısal ayrıntıların tamamını eksiksiz bilgiyle kuşatmaktır. Çakılın çokluğuna benzetilen büyük sayı anlatımı bunun bağımlı bir uzantısıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin birimleri sayılarak sayısı belirlenir."},{"facet_id":"F002","role":"specialization","statement":"Sayım, bütün birimlerin eksiksiz kapsanması ve sayının bilgiyle kuşatılması düzeyine ulaşabilir."},{"facet_id":"F003","role":"extension","statement":"Çakılın sayıca çokluğu, çok büyük bir sayıyı anlatan benzetmeye kaynak olur."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Saymadan yapılabilen aritmetik işlemleri, değerlendirmeyi ve tahmini de kapsar.","collision":"Genel hesap alanıyla karışarak eksiksiz sayma sınırını belirsizleştirir.","fit":"broadening","loses":null,"preserves":"Nicel bir sonuca ulaşma yönünü korur."},"text":"hesaplamak"},{"category":"confusable","error_profile":{"adds":"Kesin sayım yerine varsayıma ve yaklaşık belirlemeye dayanma özelliği ekler.","collision":"Kesin sayma ile yaklaşık kestirim arasındaki temel karşıtlığı siler.","fit":"displacement","loses":"Birimleri gerçekten saymayı ve bütün sayıyı eksiksiz kapsamayı yitirir.","preserves":"Bir nicelik hakkında sonuca varma amacını korur."},"text":"tahmin etmek"}],"identity_rationale":"Kaynak ifadesi bir şeyi saymayı, sayıyı eksiksiz elde etmeyi ve sayısal ayrıntıların tümünü bilgiyle kuşatmayı aynı çekirdekte toplar. Çakıl çokluğuna dayanan büyük sayı anlatımı bu çekirdeğin mecazlı uzantısıdır, çekirdeğin yerine geçmez.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"çakıl kadar çok sayı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"onlardan sayıca daha çok"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"şeyi saydı"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"sayarak miktarı belirleme ve sayısını eksiksiz bilme"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"her şeyin sayısını eksiksiz belirleyip bilgisiyle kuşattı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"onu koruyamayacak, ona güç yetiremeyecek ya da onu elde edemeyeceksiniz"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"onları bilgiyle, inanarak ve kesin bir kanaatle kavradı"}],"lexicalization_note":"Tanım, sayma çekirdeğini korurken büyük sayı, tam kuşatma ve bağlama özgü koruma ya da güç yetirme yorumlarını ayrı tutar; kalıplı okumalar yalın anlama genellenmez.","neighbor_coverage_note":"Bütün adaylar sayı, hesap, tahmin, eksiksizlik veya aynı kökün ayrı anlamları bakımından incelendi; saymanın kesinlik ve kapsam sınırını doğrudan açıklayan dört karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal eksiksiz sayma ve bilgiyle kuşatma sonucunu öne çıkarır; komşu dal ise sayı, sayılan şey ve sayılabilirlik gibi daha geniş sayım alanını kapsar.","focus_only":"Eksiksiz sayımın bütün sayıyı bilgiyle kuşatması ve çakıl çokluğuna dayalı sayı uzantısı bulunur.","gloss":"sayılanı sayma","neighbor_only":"Sayı adı, sayılan nesne, sayılabilirlik ve sayıların bir araya getirilmesi gibi daha geniş adlandırmalar bulunur.","neighbor_ref":"root_000989/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın çekirdeğinde bir topluluğun birimlerini sayarak nicelik belirleme vardır."},{"boundary_match":"partial","distinction":"Odak dal doğrudan sayma ve tam kapsamla sınırlıdır; komşu dal sayma dışındaki hesaplama, değerlendirme ve ölçüm işlemlerini de içerir.","focus_only":"Bir sayıyı bütün birimleriyle eksiksiz belirleyip bilgiyle kuşatmayı gerektirir.","gloss":"sayma ve hesap","neighbor_only":"Aritmetik hesap, muhasebe, ölçü belirleme ve gök cisimlerinin hesabı gibi işlemlere uzanır.","neighbor_ref":"root_000318/B001","relation_type":"near_synonym","shared_zone":"İki dal da niceliği sayısal işlem yoluyla belirleme alanında örtüşür."},{"boundary_match":"opposed","distinction":"Ortak nicelik ekseninde odak dal kesin ve kapsayıcı sayıma, komşu dal ise doğrudan kuşatma olmadan yapılan tahmine dayanır.","focus_only":"Birimleri sayarak kesin ve eksiksiz nicelik bilgisine ulaşır.","gloss":"tahmin ve kestirim","neighbor_only":"Niceliği doğrudan saymadan sezgi, varsayım veya yaklaşık ölçümle kestirir.","neighbor_ref":"root_000403/B001","relation_type":"polarity_pair","shared_zone":"Her iki dal da bir nesnenin sayı ya da miktarını belirleme amacını paylaşır."},{"boundary_match":"partial","distinction":"Odak dalın kapsamı sayısal birimlere bağlıdır; komşu dalın eksiksizlik anlamı ise sayma gerektirmeyen genel bir işlemdir.","focus_only":"Eksiksizliği sayılan birimlerin toplamı ve bunların sayısal bilgisi üzerinden kurar.","gloss":"eksiksiz inceleme","neighbor_only":"Eksiksiz inceleme ya da sonuna kadar gitme anlamını sayı alanıyla sınırlamadan anlatır.","neighbor_ref":"root_000316/B009","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir konuyu hiçbir kısmını bırakmadan bütünüyle ele alma fikrini taşır."}],"source_phrase_ar":"والحصى العدد الكثير شبه بحصى الحجارة لكثرتها (ayn)؛ الحصى كثرة العدد شبه بحصى الحجارة في الكثرة (tahdhib)؛ أحصيت الشيء عددته (sihah)؛ الإحصاء إحاطة العلم باستقصاء العدد (ayn)؛ أحاط علمه باستيفاء عدد كل شيء (tahdhib)؛ الإحصاء التحصيل بالعدد (mufradat)","source_summary":"Kaynakların ortak çekirdeği sayma yoluyla miktarı elde etmektir; daha güçlü anlatımlarda bütün birimleri eksiksiz sayma ve sayının tamamını bilgiyle kuşatma vurgulanır. Çakıl çokluğu da büyük sayının benzetmeli ifadesini sağlar.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه أحصيت الشيء بمعنى عددته، والإحصاء بمعنى التحصيل بالعدد، واستيفاء العدد وإحاطة العلم به، والكثرة الموصوفة بأنها أكثر حصى، وما قيل في لن تحصوه من الحفظ أو الطاقة أو تحصيل الثواب.","what_is_not_ar":"لا يدخل فيه الحصى الحسي، ولا حصاة المسك أو المثانة، ولا حصاة العقل إلا من جهة تعليلها بالإحصاء."},"support_links":["sup_0e94df48c4b7335b436f","sup_64f6aab1c4ba2834e1cf"]},{"boundary":"Dal yalnız zihinsel kapasiteyi değil ağırbaşlı, tedbirli ve gerektiğinde ketum davranışı kapsar; söz keskinliği ve sayma anlamı bunun parçası değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000332/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحْصَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aHoSaY`|ROOT:HSy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"19:94:2:1","qac_word_ref":"19:94:2","surface_ar":"أَحْصَىٰ"}],"gloss":"sağlam akıl, ağırbaşlılık ve ketum sağduyu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, kişinin sağlam ve güçlü bir akla sahip olmasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu zihinsel sağlamlık ağırbaşlılık ve ölçülü davranış olarak görünür."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli kişi nitelemelerinde tedbirli, ketum ve sır saklayan olma vurgusu eklenir."}}],"root_ar":"ح ص ي","root_id":"root_000332","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Zihinsel sağlamlığı, bunun ölçülü davranıştaki görünümünü ve özel yapılardaki ketumluk sonucunu birlikte temsil eder.","boundary_detail":"Dal yalnız zihinsel kapasiteyi değil ağırbaşlı, tedbirli ve gerektiğinde ketum davranışı kapsar; söz keskinliği ve sayma anlamı bunun parçası değildir.","branch_image_ar":"حصاة العقل والرزانة","concept_gloss":"sağlam akıl, ağırbaşlılık ve ketum sağduyu","contextual_glosses":[{"applicability":"Kişinin güçlü aklıyla birlikte ölçülü ve dengeli davranmasının anlatıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ketumluk ve sırrını koruma özelliğini zorunlu olarak bildirmez.","preserves":"Sağlam akıl ve ağırbaşlı davranış özelliklerini korur."},"facet_ids":["F001","F002"],"text":"aklı başında ve ağırbaşlı","usage_role":"general"},{"applicability":"Aklını kullanarak kendini denetleyen ve sırrını saklayan kişinin nitelendiği yapılara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel zihinsel güç ve ağırbaşlılık alanının tamamını açıkça göstermez.","preserves":"Tedbir, kendini denetleme ve sır saklama sonuçlarını korur."},"facet_ids":["F003"],"text":"tedbirli ve ketum","usage_role":"contextual"}],"definition":"Sağlam ve güçlü aklın ağırbaşlılık, sağduyu ve kendini denetleme olarak görünmesidir. Bazı kişi nitelemelerinde bu nitelik tedbirli olmayı, ketumluğu ve sırrını korumayı da içerir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, kişinin sağlam ve güçlü bir akla sahip olmasıdır."},{"facet_id":"F002","role":"specialization","statement":"Bu zihinsel sağlamlık ağırbaşlılık ve ölçülü davranış olarak görünür."},{"facet_id":"F003","role":"specialization","statement":"Belirli kişi nitelemelerinde tedbirli, ketum ve sır saklayan olma vurgusu eklenir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Genel bilişsel yetenekle karışarak davranışsal olgunluk sınırını görünmez kılar.","fit":"narrowing","loses":"Ağırbaşlılık, kendini denetleme, tedbir ve ketumluk bileşenlerini yitirir.","preserves":"Zihinsel güç ve anlama yetisi yönünü korur."},"text":"zekâ"}],"identity_rationale":"Kaynak ifadesi akıl ve zihinsel sağlamlığı ağırbaşlılıkla birleştirir; bazı yapılarda buna tedbirli davranma, ketumluk ve sırrını koruma eklenir. Bunlar ilgisiz anlamlar değil, sağlam aklın davranışta görülen özel sonuçlarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kişinin ağırbaşlılığı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"kişinin kendini denetlemesini sağlayan akıl"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"akıllı ve sağduyulu; tedbirli ve ketum"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"tedbirli, ketum ve sırrını koruyan"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"aklı güçlü"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"aklı güçlü"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"aklı güçlü"}],"lexicalization_note":"Tanım, akıl ve ağırbaşlılık çekirdeğini korur; ketumluk ve sırrını saklama yalnız bunları açıkça bildiren kişi nitelemelerine bağlanır.","neighbor_coverage_note":"Tüm adaylar akıl, görüş, ağırbaşlılık, özdenetim ve aynı kökün başka anlamları açısından karşılaştırıldı; genel zekâ ile davranışsal olgunluk sınırını gösteren dört aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ketumluk ve sır saklamaya uzanabilir; komşu dal ise görüşün ağırlığına, kararın sağlamlığına ve sebatına yoğunlaşır.","focus_only":"Sağlam aklın yanında ketumluk ve sırrını koruma sonucunu belirli yapılarda içerir.","gloss":"sağlam ve isabetli görüş","neighbor_only":"Görüşün isabeti, kararda sebat ve kişinin kendini bir işe kesin biçimde hazırlaması daha belirgindir.","neighbor_ref":"root_001645/B005","relation_type":"near_synonym","shared_zone":"Her iki dal güçlü akıl, ağırbaşlılık ve düşüncede sağlamlık alanında büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal zihinsel güçle ağırbaşlı ve ketum kişiliği birleştirir; komşu dalın ayırıcı yönü aklın yanlış davranışı engellemesidir.","focus_only":"Ağırbaşlılık, tedbir ve bazı yapılarda ketumlukla sır saklama özelliklerini içerir.","gloss":"davranışı dizginleyen akıl","neighbor_only":"Aklın kişiyi uygun olmayan davranıştan alıkoyan engelleyici işlevini merkez alır.","neighbor_ref":"root_000296/B002","relation_type":"near_synonym","shared_zone":"İki dal da aklı kişinin davranışını düzenleyen sağlam bir yeti olarak gösterir."},{"boundary_match":"partial","distinction":"Odak dal kişinin daha geniş zihinsel ve davranışsal niteliğidir; komşu dal belirli olarak görüşün kalitesini anlatır.","focus_only":"Kişinin genel akıl gücünü, ağırbaşlılığını ve kendini denetlemesini anlatır.","gloss":"iyi ve sağlam görüş","neighbor_only":"Özellikle görüşün iyi, sağlam ve isabetli oluşunu niteler.","neighbor_ref":"root_000599/B008","relation_type":"near_neighbor","shared_zone":"Sağlam düşünme ve yerinde yargıya varma özelliklerinde örtüşme bulunur."},{"boundary_match":"partial","distinction":"Odak dal akıl ve zihinsel sağlamlık temellidir; komşu dal ise özellikle duygusal taşkınlık karşısındaki sabır ve özdenetimi anlatır.","focus_only":"Sağlam akıl ve sağduyu, ağırbaşlı davranışın iç dayanağıdır.","gloss":"sabır ve kendini tutma","neighbor_only":"Öfke yükseldiğinde sabretme, taşkınlığı bastırma ve kendini tutma eylemini merkez alır.","neighbor_ref":"root_000352/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal ölçülü davranma, taşkınlıktan kaçınma ve kendini denetleme alanında buluşur."}],"source_phrase_ar":"حصاة الرجل رزانته (ayn)؛ حصاة العقل لأن المرء يحصي بها على نفسه (ayn)؛ فلان ذو حصاة أي ذو عقل ولب (sihah)؛ فلان ذو حصاة وأصاة إذا كان حازما كتوما على نفسه يحفظ سره (tahdhib)؛ فلان حصي وحصيف ومستحص إذا كان شديد العقل (tahdhib)","source_summary":"Kaynaklar anlamı akıl, zihinsel güç ve ağırbaşlılık çevresinde kurar; kişi niteleyen bazı yapılarda sağlam aklın sonucu olarak tedbir, ketumluk ve sırrını koruma özellikleri de belirtilir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه حصاة الرجل بمعنى رزانته وعقله ولبه، وذو حصاة أو أصاة بمعنى الحازم الكتوم، وحصي وحصيف ومستحص بمعنى شديد العقل.","what_is_not_ar":"لا يدخل فيه مجرد العد، ولا الحجارة الحسية، ولا ذرابة اللسان إلا إذا نصت العبارة عليها."},"support_links":[]},{"boundary":"Dal yalnız dilin sivri ve keskin oluşunu bildiren yapıya bağlıdır; tartışmalı metin biçimi yeni bir anlam oluşturmaz ve genel konuşma yeteneğine genişletilemez.","branch_kind":"collocation","branch_ref":"root_000332/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحْصَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aHoSaY`|ROOT:HSy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"19:94:2:1","qac_word_ref":"19:94:2","surface_ar":"أَحْصَىٰ"}],"gloss":"dilin sivri ve keskin oluşu","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yapı, dilin söz söylerken sivri ve keskin oluşunu niteler."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Benzer görünen bir metin biçimi aktarılmış, ancak başka aktarımda doğru okuma farklı kabul edilmiştir."}}],"root_ar":"ح ص ي","root_id":"root_000332","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kişinin dilini sözdeki sivrilik ve keskinlik bakımından niteleyen yapının bütün çekirdeğini karşılar.","boundary_detail":"Dal yalnız dilin sivri ve keskin oluşunu bildiren yapıya bağlıdır; tartışmalı metin biçimi yeni bir anlam oluşturmaz ve genel konuşma yeteneğine genişletilemez.","branch_image_ar":"حصاة اللسان وذرابته","concept_gloss":"dilin sivri ve keskin oluşu","contextual_glosses":[{"applicability":"Kişinin sözlerinde keskin ve sert bir dil kullandığının kısa biçimde anlatıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin dilindeki sivrilik ve sözdeki keskinlik niteliğini korur."},"facet_ids":["F001"],"text":"sivri dillilik","usage_role":"general"},{"applicability":"Yapının kişiye yüklediği keskin konuşma niteliğinin açıklanması gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dilin keskinliğini kişi niteliği olarak açık biçimde korur."},"facet_ids":["F001"],"text":"keskin dilli olma","usage_role":"explanatory"}],"definition":"Belirli bir dil yapısında, kişinin sözlerinin sivri, sert ve keskin oluşunu anlatır. Benzer biçimli tartışmalı bir metin aktarımı bu yapının anlamını genişletmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yapı, dilin söz söylerken sivri ve keskin oluşunu niteler."},{"facet_id":"F002","role":"source_variant","statement":"Benzer görünen bir metin biçimi aktarılmış, ancak başka aktarımda doğru okuma farklı kabul edilmiştir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Olumlu estetik değer ve düzgün anlatım niteliği ekler.","collision":"Keskin söz söyleme ile olumlu söz ustalığını birbirine karıştırır.","fit":"displacement","loses":"Sivrilik, sertlik ve keskinlik niteliğini yitirir.","preserves":"Konuşma ve dil kullanımı alanını korur."},"text":"güzel konuşma"}],"identity_rationale":"Kaynak ifadesi belirli dil yapısında sözdeki sivrilik ve keskinliği doğrudan destekler. Bunun yanında aktarılan bir sözdeki benzer biçim başka bir aktarımda doğru okuma sayılmadığından, o metin dal için bağımsız bir anlam kanıtı olarak kullanılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"dilin sivriliği ve sözdeki keskinliği"}],"lexicalization_note":"Tanım yalnız dilin sivriliğini bildiren sabit yapıya bağlıdır; bu anlam yalın biçime veya benzer görünen tartışmalı metin aktarımına taşınmaz.","neighbor_coverage_note":"Bütün adaylar dil keskinliği, konuşma yeteneği, susma ve aynı kökün ayrı anlamları bakımından değerlendirildi; yalnız sivrilik ile söz ustalığı veya incitme arasındaki sınırı açıklayan üç aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız sivrilik ve keskinlik çekirdeğindedir; komşu dal konuşma gücü, akıcılık ve gürültücülük gibi ek boyutlara uzanır.","focus_only":"Sabit bir yapıda dilin sivri ve keskin niteliğine odaklanır.","gloss":"sivri ve güçlü dil","neighbor_only":"Keskinliğin yanında söz ustalığı, uzun konuşma, gürültücülük ve söz söyleme gücünü de kapsar.","neighbor_ref":"root_000732/B004","relation_type":"near_synonym","shared_zone":"Her iki dal kişinin dilini keskin, güçlü ve çoğu zaman olumsuz bir nitelikle betimler."},{"boundary_match":"partial","distinction":"Odak dal dilin niteliğini adlandırır; komşu dal bu niteliğin karşıdakini inciten eylemsel sonucunu ve aşırı söz söylemeyi öne çıkarır.","focus_only":"Dilin sürekli ya da belirgin bir sivrilik niteliğini bildirir.","gloss":"incitici keskin söz","neighbor_only":"Sözle acı verme eylemini ve hoş görülmeyen sözde aşırılığı doğrudan içerir.","neighbor_ref":"root_000734/B001","relation_type":"near_synonym","shared_zone":"Keskin ve sert dil kullanımı iki dalın ortak anlam alanıdır."},{"boundary_match":"partial","distinction":"Odak dal sözün sivri niteliğiyle sınırlıdır; komşu dal olumlu söz ustalığını ve dil dışındaki fiziksel keskinliği de kapsayabilir.","focus_only":"Sözdeki sivriliği ve sert keskinliği temel alır.","gloss":"keskin ve akıcı dil","neighbor_only":"Dil keskinliğine açık söz ustalığı ve akıcılık ekler; ayrıca fiziksel keskinlik kullanımına uzanır.","neighbor_ref":"root_000349/B004","relation_type":"near_synonym","shared_zone":"İki dal keskin dilli kişi nitelemesinde önemli ölçüde örtüşür."}],"source_phrase_ar":"حصاة اللسان ذرابته (ayn;tahdhib)؛ وهل يكب الناس على مناخرهم في جهنم إلا حصا ألسنتهم ويقال حصائد (ayn)؛ والرواية الصحيحة إلا حصائد ألسنتهم (tahdhib)","source_summary":"Toplu kanıt, dilin sözdeki sivriliğini ve keskinliğini bildiren yapıyı destekler. Benzer biçimli bir metin aktarımının doğru okumasına ilişkin kaynak farkı, bu dal için bağımsız bir anlam kanıtı oluşturmaz.","sources":["AY","TA"],"what_is_ar":"يدخل فيه التعبير عن حصاة اللسان بمعنى ذرابته وحدته في الكلام.","what_is_not_ar":"لا يدخل فيه حصاة العقل التي تضبط اللسان، ولا يعتمد حديث حصا ألسنتهم فرعا مستقلا لأن تهذيب اللغة يصرح بأن الرواية الصحيحة حصائد ألسنتهم."},"support_links":[]},{"boundary":"Dal yalnız misk maddesinin katı parçasını bildiren yapıya bağlıdır; genel taş, başka maddelerin parçası veya kokunun kendisi anlamına genişletilemez.","branch_kind":"collocation","branch_ref":"root_000332/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحْصَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aHoSaY`|ROOT:HSy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"19:94:2:1","qac_word_ref":"19:94:2","surface_ar":"أَحْصَىٰ"}],"gloss":"misk kesesindeki katı koku maddesi parçası","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderim, misk maddesinden oluşan tek ve katı bir parçadır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Parça, misk maddesini taşıyan kesenin içinde bulunan katı oluşum olarak belirtilir."}}],"root_ar":"ح ص ي","root_id":"root_000332","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Misk maddesinden oluşan katı parçayı ve özellikle bu parçanın kese içindeki konumunu birlikte belirtir.","boundary_detail":"Dal yalnız misk maddesinin katı parçasını bildiren yapıya bağlıdır; genel taş, başka maddelerin parçası veya kokunun kendisi anlamına genişletilemez.","branch_image_ar":"حصاة المسك","concept_gloss":"misk kesesindeki katı koku maddesi parçası","contextual_glosses":[{"applicability":"Kokulu maddenin tek bir katı parçasından söz edilen bağlamlarda doğal ve kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Parçanın misk kesesinin içinde bulunduğunu açıkça bildirmez.","preserves":"Misk maddesi ve onun katı parça niteliğini korur."},"facet_ids":["F001"],"text":"katı misk parçası","usage_role":"general"},{"applicability":"Parçanın taşıyıcı kese içindeki yeri özellikle belirtilmek istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Misk maddesini, katı parçayı ve kese içindeki konumu birlikte korur."},"facet_ids":["F001","F002"],"text":"misk kesesindeki katı parça","usage_role":"explanatory"}],"definition":"Misk adı verilen kokulu maddeden oluşan katı bir parçadır; özellikle bu maddenin bulunduğu kesenin içindeki parça anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderim, misk maddesinden oluşan tek ve katı bir parçadır."},{"facet_id":"F002","role":"specialization","statement":"Parça, misk maddesini taşıyan kesenin içinde bulunan katı oluşum olarak belirtilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Parçanın bağımsız bir taş türü olduğu izlenimini ekler.","collision":"Gerçek taş adlarıyla karışarak parçanın kokulu maddeden oluştuğunu belirsizleştirir.","fit":"broadening","loses":null,"preserves":"Misk maddesiyle katı ve taş benzeri parça bağlantısını korur."},"text":"misk taşı"}],"identity_rationale":"Kaynak ifadesi, misk adı verilen kokulu maddeden oluşan katı bir parçayı ve bunun söz konusu maddenin kesesinde bulunduğunu açıkça belirtir. Parçanın katılığı taş anlamıyla benzerlik kurar, ancak gönderim gerçek bir taş değildir.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"misk kesesinde bulunan katı misk parçası"}],"lexicalization_note":"Tanım yalnız misk maddesinin katı parçasını adlandıran yapıya bağlıdır; parça anlamı yalın biçime veya bütün kokulu maddelere genellenmez.","neighbor_coverage_note":"Tüm adaylar katı parça, kütle, misk ve güzel koku alanları bakımından incelendi; yalnız madde türü, parça yapısı veya koku niteliğiyle sınırı açıklayan dört aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Parça biçimi ortaktır, fakat odak dal kokulu misk maddesine ve kesesine; komşu dal ise kurutulmuş süt ürününe bağlıdır.","focus_only":"Misk maddesinden oluşan ve onun kesesinde bulunan katı parçayı anlatır.","gloss":"katı süt ürünü parçası","neighbor_only":"Kurutulmuş süt ürününden oluşan, özellikle büyük bir katı parçayı anlatır.","neighbor_ref":"root_000210/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal belirli bir maddeden kopmuş ya da oluşmuş tek bir katı parçayı adlandırır."},{"boundary_match":"partial","distinction":"Odak dal madde ve konum bakımından dar bir yapıdır; komşu dal çeşitli maddelerde ve benzetmeli alanlarda kullanılabilen genel bir kütle kavramıdır.","focus_only":"Belirli bir kokulu maddenin kesedeki katı parçasıyla sınırlıdır.","gloss":"toplu parça veya kütle","neighbor_only":"Demir, saç ve beden bölgesi gibi farklı alanlardaki yığın, kütle ve iri parça anlamlarına uzanır.","neighbor_ref":"root_000621/B002","relation_type":"near_neighbor","shared_zone":"İki dalın ortak noktası, maddenin toplu ve yoğun bir parça oluşturmasıdır."},{"boundary_match":"field_only","distinction":"Odak dal belirli bir maddenin fiziksel parçasıdır; komşu dal ise güzel kokulu maddelerin işlevsel ve genel adıdır.","focus_only":"Kokulu maddenin katı ve tekil parçasını adlandırır.","gloss":"hoş kokulu madde","neighbor_only":"Sürünmek veya güzel koku vermek için kullanılan hoş kokulu maddelerin genel sınıfını anlatır.","neighbor_ref":"root_000961/B007","relation_type":"same_field","shared_zone":"Her iki dal güzel koku amacıyla kullanılan maddeler alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal maddenin parça ve konum özelliğine, komşu dal ise kokusunun bulunmamasına dayanır; çekirdekleri birbirinin yerine geçmez.","focus_only":"Misk maddesinin kesede bulunan katı parçasını anlatır.","gloss":"kokusuz misk","neighbor_only":"Miskin kokusuz veya kokusunu yitirmiş bir niteliğini anlatır.","neighbor_ref":"root_001289/B009","relation_type":"same_field","shared_zone":"İki dal aynı kokulu maddeyi konu edinir."}],"source_phrase_ar":"لكل قطعة من المسك حصاة (ayn;tahdhib)؛ حصاة المسك قطعة صلبة توجد في فأرة المسك (sihah)","source_summary":"Kaynaklar misk maddesinin her bir katı parçasını bu yapıyla adlandırır ve parçanın söz konusu kokulu maddenin kesesinde bulunduğunu belirtir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه حصاة المسك، أي القطعة الصلبة من المسك أو القطعة الموجودة في فأرة المسك.","what_is_not_ar":"لا يدخل فيه الحصى من الحجارة، ولا حصاة المثانة، ولا العد."},"support_links":[]},{"boundary":"Dal mesanedeki taşlaşma hastalığı ve buna tutulma durumudur; sıradan çakıl, yalnız idrar tutulması veya başka bir bedensel hastalık bunun yerine geçmez.","branch_kind":"bare","branch_ref":"root_000332/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحْصَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aHoSaY`|ROOT:HSy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"19:94:2:1","qac_word_ref":"19:94:2","surface_ar":"أَحْصَىٰ"}],"gloss":"idrarın koyulaşıp taşlaşmasına bağlı mesane taşı hastalığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, mesanede ortaya çıkan bir hastalıktır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hastalıkta idrar koyulaşır, sertleşir ve taş benzeri bir oluşuma dönüşür."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Türetilmiş kişi biçimleri hastalığa tutulmayı ve bu durumda bulunan kişiyi anlatır."}}],"root_ar":"ح ص ي","root_id":"root_000332","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hastalığın mesanedeki yerini, idrarın koyulaşıp sertleşme sürecini ve taş benzeri sonucunu birlikte temsil eder.","boundary_detail":"Dal mesanedeki taşlaşma hastalığı ve buna tutulma durumudur; sıradan çakıl, yalnız idrar tutulması veya başka bir bedensel hastalık bunun yerine geçmez.","branch_image_ar":"الحصاة في المثانة","concept_gloss":"idrarın koyulaşıp taşlaşmasına bağlı mesane taşı hastalığı","contextual_glosses":[{"applicability":"Hastalığın taş benzeri sert sonucunun kısa biçimde adlandırıldığı sağlık bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İdrarın koyulaşıp sertleşme sürecini ve hastalık çerçevesini tam açıklamaz.","preserves":"Mesanede oluşan taş benzeri sert sonucu korur."},"facet_ids":["F001","F002"],"text":"mesane taşı","usage_role":"general"},{"applicability":"Bir kişinin söz konusu hastalığa yakalandığını bildiren türemiş biçimin geçtiği bağlama özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İdrarın koyulaşması ve taşlaşması sürecini kendi başına açıklamaz.","preserves":"Kişinin mesane taşı hastalığından etkilenmesi durumunu korur."},"facet_ids":["F003"],"text":"mesane taşı hastalığına tutulmak","usage_role":"contextual"}],"definition":"Mesanede idrarın koyulaşıp sertleşerek taş benzeri bir oluşuma dönüşmesiyle ortaya çıkan hastalıktır. İlgili kişi biçimleri bu hastalığa tutulma ve tutulmuş olma durumunu bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, mesanede ortaya çıkan bir hastalıktır."},{"facet_id":"F002","role":"core","statement":"Hastalıkta idrar koyulaşır, sertleşir ve taş benzeri bir oluşuma dönüşür."},{"facet_id":"F003","role":"associated_use","statement":"Türetilmiş kişi biçimleri hastalığa tutulmayı ve bu durumda bulunan kişiyi anlatır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"İdrarın dışarı atılamaması durumunu ayrı bir hastalık çekirdeği olarak ekler.","collision":"Taş oluşumu ile boşaltımın engellenmesini birbirine karıştırır.","fit":"displacement","loses":"İdrarın koyulaşıp sertleşmesini ve taş benzeri oluşumu yitirir.","preserves":"Mesane ve idrar yollarıyla ilgili bir rahatsızlık alanını korur."},"text":"idrar tutulması"}],"identity_rationale":"Kaynak ifadesi mesanede görülen bir hastalığı, idrarın koyulaşıp sertleşerek taş benzeri bir oluşuma dönüşmesi süreciyle birlikte tanımlar. Kişinin bu hastalığa tutulmasını ve tutulmuş kişiyi bildiren biçimler aynı hastalık çekirdeğine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"idrarın koyulaşıp sertleşmesiyle oluşan mesane taşı hastalığı"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"mesane taşı hastalığına tutuldu"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"mesane taşı hastalığına tutulmuş kişi"}],"lexicalization_note":"Tanım, yalın biçimin mesane hastalığı anlamını doğrudan verir; başka dallardaki taş, koku maddesi veya kalıplaşmış kullanımlar bu yalın anlama katılmaz.","neighbor_coverage_note":"Bütün adaylar üriner hastalık, genel hastalanma, bedensel akıntı ve aynı kökün taş anlamı açısından değerlendirildi; yalnız taşlaşma sürecini idrar tutulması, genel hastalık ve gerçek taştan ayıran adaylar yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dalın çekirdeği taşlaşan sert oluşumdur; komşu dalın çekirdeği ise idrar akışının engellenmesi ve tutulmasıdır.","focus_only":"Mesanede idrarın koyulaşıp sertleşerek taş benzeri bir oluşum meydana getirmesini anlatır.","gloss":"idrar tutulması","neighbor_only":"İdrarın dışarı çıkamayıp tutulmasını ve bu duruma uygulanan bir tedavi aracını anlatır.","neighbor_ref":"root_000030/B004","relation_type":"same_field","shared_zone":"Her iki dal mesane ve idrar yollarında ortaya çıkan hastalık durumları alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal belirli organ, madde ve oluşum sürecine sahiptir; komşu dal ise hastalığın bedeni tutmasına ilişkin genel bir çerçevedir.","focus_only":"Belirli olarak mesanedeki koyulaşma ve taşlaşma sürecini tanımlar.","gloss":"hastalığın bedeni tutması","neighbor_only":"Çeşitli hastalıkların bedeni etkisi altına almasını ve hastalık karşısındaki düşkünlüğü genel biçimde anlatır.","neighbor_ref":"root_000018/B007","relation_type":"same_field","shared_zone":"İki dal da kişinin bir hastalığın etkisi altına girmesini ifade edebilir."},{"boundary_match":"partial","distinction":"Odak dal bedensel bir hastalık ve oluşum sürecidir; komşu dal ise gerçek küçük taşların nesne ve arazi anlamıdır.","focus_only":"Mesanede gelişen hastalık ile idrarın taş benzeri sert bir oluşuma dönüşmesini içerir.","gloss":"çakıl taşı ve çakıllı zemin","neighbor_only":"Doğada bulunan küçük taşları ve bunlarla kaplı zemini anlatır.","neighbor_ref":"root_000332/B001","relation_type":"near_neighbor","shared_zone":"Taş benzeri küçük ve sert oluşum fikri iki dal arasında biçimsel bir bağ kurar."}],"source_phrase_ar":"الحصاة داء يقع في المثانة يخثر البول فيشتد حتى يصير كالحصاة (ayn)؛ الحصاة داء في المثانة وهو أن يخثر البول فيشتد حتى يصير كالحصاة يقال حصي الرجل فهو محصي (tahdhib)","source_summary":"Kaynaklar hastalığı mesanede idrarın koyulaşması, sertleşmesi ve taş benzeri bir oluşuma dönmesiyle açıklar; ayrıca kişinin bu hastalığa tutulmasını ve tutulmuş kişiyi bildiren biçimleri verir.","sources":["AY","TA"],"what_is_ar":"يدخل فيه الحصاة داء المثانة، وخثور البول حتى يشتد ويصير كالحصاة، وقولهم حصي الرجل فهو محصي.","what_is_not_ar":"لا يدخل فيه الحصى العادي ولا حصاة المسك ولا العد والإحصاء."},"support_links":[]},{"boundary":"Çekirdek sayma ve sayıyla belirlemedir; hazırlama, zaman bekleme, kalıcı su ve dönemsel yineleme bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000989/B001","candidate_links":[{"candidate_id":"cand_dd433011ceaad84831fb","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَدَّ","morph_features":"STEM|POS:V|PERF|LEM:Ead~a|ROOT:Edd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"19:94:3:2","qac_word_ref":"19:94:3","surface_ar":"عَدَّ"},{"lemma_ar":"عَدّ","morph_features":"STEM|POS:N|LEM:Ead~|ROOT:Edd|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"19:94:4:1","qac_word_ref":"19:94:4","surface_ar":"عَدًّا"}],"gloss":"sayma, sayı ve sayıya göre bir topluluğa katma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin birimlerini sayıp toplam miktarını belirleme işlemi."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sayma sonucundaki miktar, sayı ve sayılmış ya da sınırlandırılmış varlık."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sayıca çokluğu belirtme veya birini belirli bir topluluğun üyeleri arasında sayma."}}],"root_ar":"ع د د","root_id":"root_000989","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sayma işlemiyle onun doğrudan sonuçlarını ve sayıya dayalı topluluk üyeliğini birlikte anlatan kapsayıcı karşılıktır.","boundary_detail":"Çekirdek sayma ve sayıyla belirlemedir; hazırlama, zaman bekleme, kalıcı su ve dönemsel yineleme bu dala girmez.","branch_image_ar":"إحصاء المعدود","concept_gloss":"sayma, sayı ve sayıya göre bir topluluğa katma","contextual_glosses":[{"applicability":"Bir nesne topluluğunun kaç birimden oluştuğunun belirlenmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sayma eylemini ve miktarı belirleme sonucunu birlikte korur."},"facet_ids":["F001"],"text":"sayıp miktarını belirlemek","usage_role":"general"},{"applicability":"Eylemden çok sayma sonucunu veya sayıyla sınırlandırılmış varlığı anlatan bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sayma sonucundaki sayı ve miktar değerini korur."},"facet_ids":["F002"],"text":"sayı ve sayılan miktar","usage_role":"contextual"},{"applicability":"Bir kişinin belirli bir topluluğa dahil kabul edildiği kalıplaşmış bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir topluluğun üyeleri içinde sayılma ilişkisini korur."},"facet_ids":["F003"],"text":"arasında sayılmak","usage_role":"contextual"}],"definition":"Bir şeyi tek tek sayarak miktarını belirleme; bu işlemin sonucu olan sayı, sayılan varlıkların sayıca niteliği ve bir kimseyi ya da şeyi belirli bir topluluk içinde sayma alanıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin birimlerini sayıp toplam miktarını belirleme işlemi."},{"facet_id":"F002","role":"extension","statement":"Sayma sonucundaki miktar, sayı ve sayılmış ya da sınırlandırılmış varlık."},{"facet_id":"F003","role":"associated_use","statement":"Sayıca çokluğu belirtme veya birini belirli bir topluluğun üyeleri arasında sayma."}],"identity_rationale":"Kaynak ifadesi, bir şeyi tek tek sayıp miktarını belirleme çekirdeğini; sayı, sayılan şey, sayıca çokluk ve bir topluluk içinde sayılma kullanımlarıyla birlikte açıkça destekler. Geçici çerçeve bu kapsamı başka dallardaki hazırlama, bekleme süresi, su ve zaman anlamlarından doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi sayıp miktarını belirlemek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"sayı; sayılanın miktarı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"sayıca çokluk"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sayılmış veya sayıyla sınırlandırılmış"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"iyiler arasında sayılmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"az ya da çok sayıda topluluk"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"sayıları on bini aşmak"}],"lexicalization_note":"Tanım sayma çekirdeğini temel alır; topluluk içinde sayılma ve belli bir sayıyı aşma yalnızca kendi kalıplarıyla sınırlı tutulur.","neighbor_coverage_note":"Verilen komşu adaylarının tümü incelendi; sayma ile hesap, bütünleme ve karşılıklı sayılma arasındaki en açıklayıcı üç sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı saymanın kendisiyle sayı ve üyelik sonuçlarını birlikte taşır; komşu dal ise hesabı, hesaplaşmayı ve tahmini de içerdiği için bütünüyle birbirinin yerine geçmez.","focus_only":"Sayı, sayılan varlık, sayıca çokluk ve bir topluluğun içinde sayılma kullanımlarını da kapsar.","gloss":"sayma ve hesaplama","neighbor_only":"Hesaplaşma, tahmin ve gök cisimlerinin hesabı gibi daha geniş hesap alanlarına uzanır.","neighbor_ref":"root_000318/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da nesneleri sayma ve sayısal bir sonuç elde etme alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dalında birimleri sayma belirleyicidir; komşuda ise sayma gerekmeksizin parçaları topluca ve ayrıntısız biçimde kapsama esastır.","focus_only":"Tek tek sayma, sayısal miktar ve sayıya göre topluluğa katma işlemlerini bildirir.","gloss":"toplam ve bütün","neighbor_only":"Dağınık parçaları ayrıntılandırmadan tek bir bütün veya genel toplam halinde birleştirir.","neighbor_ref":"root_000260/B003","relation_type":"near_neighbor","shared_zone":"Sayılmış parçaların bir sonuçta toplanması iki alan arasında sınırlı bir temas kurar."},{"boundary_match":"partial","distinction":"Odak dalının çekirdeği sayısal belirlemedir; komşu dalın çekirdeği ise paydaşlar veya denkler arasında kurulan karşılıklı ilişkidir.","focus_only":"Varlıkları sayıp miktar belirlemeyi ve bir topluluk içinde saymayı kapsar.","gloss":"sayma ile karşılıklı sayılma","neighbor_only":"Karşılıklı paydaşlık, pay veya iki kişinin birbirine denk sayılması ilişkisini kapsar.","neighbor_ref":"root_000989/B006","relation_type":"near_neighbor","shared_zone":"İki dalda da bir kişi ya da şey başkalarıyla birlikte değerlendirilip sayılabilir."}],"source_phrase_ar":"عددت الشيء عدا أي أحصيته (maqayis;ayn;sihah;tahdhib)؛ العدد مقدار ما يعد (maqayis)؛ العديد الكثرة (maqayis;ayn;sihah;tahdhib)؛ فلان في عداد الصالحين (maqayis;ayn;sihah)؛ العدد آحاد مركبة (mufradat)","source_summary":"Toplu tanıklık, sayma işlemini temel alır ve bundan sayı, sayılan şey, sayıca çokluk ve bir topluluğa dahil sayılma kullanımlarını geliştirir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"الإحصاء وضم الأعداد واسم العدد والمعدود والكثرة أو القلة من جهة كون الشيء يحصى أو يعد في جماعة","what_is_not_ar":"ليس إعداد الشيء وتهيئته ولا عدة المرأة ولا الماء العد ولا العداد الزماني"},"support_links":["sup_0e94df48c4b7335b436f"]},{"boundary":"Bu dal gelecekteki ihtiyaç için hazırlamadır; sayısal sayma, hukuki bekleme süresi veya yalnızca mevcut bulunma anlamı değildir.","branch_kind":"bare","branch_ref":"root_000989/B002","candidate_links":[{"candidate_id":"cand_e2e332880fc30828c229","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَدَّ","morph_features":"STEM|POS:V|PERF|LEM:Ead~a|ROOT:Edd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"19:94:3:2","qac_word_ref":"19:94:3","surface_ar":"عَدَّ"},{"lemma_ar":"عَدّ","morph_features":"STEM|POS:N|LEM:Ead~|ROOT:Edd|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"19:94:4:1","qac_word_ref":"19:94:4","surface_ar":"عَدًّا"}],"gloss":"gelecekteki bir iş için hazırlama ve hazır bulundurma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi gelecekteki belirli bir iş veya olay için önceden hazırlamak."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İhtiyaç anı için mal, silah veya başka bir gereci ayırıp hazır tutmak."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hazırlanan şeyi gerektiğinde erişilip alınabilecek bir durumda bulundurmak."}}],"root_ar":"ع د د","root_id":"root_000989","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel hazırlama eylemini, ihtiyaç için kaynak ayırmayı ve kullanılabilir durumda tutmayı birlikte karşılar.","boundary_detail":"Bu dal gelecekteki ihtiyaç için hazırlamadır; sayısal sayma, hukuki bekleme süresi veya yalnızca mevcut bulunma anlamı değildir.","branch_image_ar":"تهيئة العدة","concept_gloss":"gelecekteki bir iş için hazırlama ve hazır bulundurma","contextual_glosses":[{"applicability":"Bir şeyin ilerideki belirli bir iş için uygun duruma getirilmesini anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gelecekteki işe yönelik ön hazırlama işlemini korur."},"facet_ids":["F001"],"text":"önceden hazırlamak","usage_role":"general"},{"applicability":"Hazırlanan şeyin ihtiyaç anında erişilebilir ve kullanılabilir tutulduğu bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hazırlanan şeyin erişilebilir ve kullanıma hazır tutulmasını korur."},"facet_ids":["F003"],"text":"gerektiğinde kullanmak üzere hazır tutmak","usage_role":"contextual"},{"applicability":"İlerideki olaylar için mal, silah veya başka araçların önceden ayrılması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İhtiyaca yönelik somut araç ve kaynak ayırma işlemini korur."},"facet_ids":["F002"],"text":"gereç ve kaynak ayırmak","usage_role":"contextual"}],"definition":"Bir şeyi ileride doğacak bir iş veya ihtiyaç için önceden hazırlamak, gerektiğinde kullanılabilecek biçimde hazır tutmak ve bu amaçla mal, silah ya da başka gereç ayırmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi gelecekteki belirli bir iş veya olay için önceden hazırlamak."},{"facet_id":"F002","role":"specialization","statement":"İhtiyaç anı için mal, silah veya başka bir gereci ayırıp hazır tutmak."},{"facet_id":"F003","role":"extension","statement":"Hazırlanan şeyi gerektiğinde erişilip alınabilecek bir durumda bulundurmak."}],"identity_rationale":"Kaynak ifadesi bir şeyi gelecekteki bir iş veya olay için hazırlamayı, hazır ve erişilebilir duruma getirmeyi, ayrıca ihtiyaç anı için mal, silah ve gereç ayırmayı ortak bir çekirdekte birleştirir. Geçici dal kimliği bu işlemi sayma ve öteki dallardan doğru biçimde ayırmaktadır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir şeyi ilerideki iş için hazırlamak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ilerideki ihtiyaç için hazırlanmış mal, silah veya gereç"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bir işe hazırlanmak ve donanmak"}],"lexicalization_note":"Tanım çıplak hazırlama anlamını verir; belirli bir kalıba özgü kapsam eklemez ve hazırlanan araçları yalnızca desteklenen örnekler olarak tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel hazırlama, amaç için ayırma, hazır bulunma ve ek güvence arasındaki en yararlı üç karşıtlık seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı genel hazırlama ve donanım alanıdır; komşu dalda hazırlanan şeyin belirli bir alıcıya, borca veya karşılığa bağlanması daha belirleyicidir.","focus_only":"Her türlü gelecek iş için hazırlama ile araç ve kaynakları hazır tutmayı genel olarak kapsar.","gloss":"hazırlama ve belirli amaç için ayırma","neighbor_only":"Bir şeyi belirli bir kişi, borç veya karşılık için özellikle ayırıp gözetme anlamını taşır.","neighbor_ref":"root_000566/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi ilerideki kullanım için önceden hazır hale getirmeyi içerir."},{"boundary_match":"partial","distinction":"Odak dalında amaçlı hazırlama işlemi merkezdeyken komşuda hazır bulunma durumu ve el altındaki donanım daha geniş bir yer tutar.","focus_only":"Hazırlama eylemini ve gelecekteki olay için kaynak ayırmayı öne çıkarır.","gloss":"hazırlamak ve hazır bulunmak","neighbor_only":"Hazır, yakın ve elde bulunan durum ile sürekli el altında tutulan donanımı da adlandırır.","neighbor_ref":"root_000978/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin ihtiyaç anında kullanılmaya hazır olmasını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalı nötr hazırlamayı anlatır; komşu dal ise belirsizlik veya tehlikeye karşı fazladan güvence sağlama amacını gerektirir.","focus_only":"Beklenen iş için gerekli şeyi hazırlayıp kullanıma hazır hale getirir.","gloss":"hazırlık ve güvence önlemi","neighbor_only":"Güvenceyi artırmak için gereğinden fazla önlem veya yedek edinmeyi içerir.","neighbor_ref":"root_000970/B021","relation_type":"near_neighbor","shared_zone":"Gelecekteki bir gereksinime karşı önceden araç edinme iki dalın ortak alanıdır."}],"source_phrase_ar":"أعددت الشيء إعدادا (maqayis)؛ أعددت الشيء هيأته (ayn)؛ العدة من السلاح ما اعتددته (jamhara)؛ أعده لأمر كذا هيأه له (sihah)؛ العدة ما أعد لأمر يحدث مثل الأهبة (tahdhib)؛ أعددت هذا لك أي جعلته بحيث تعده وتتناوله (mufradat)","source_summary":"Toplu tanıklık, önceden hazırlama ve hazır tutma çekirdeğinde birleşir; ayrılan mal, silah ve gereçler yaklaşan ihtiyaçlara yönelik somut uygulamalardır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"تهيئة الشيء لأمر حادث واتخاذ العدة والأهبة والذخيرة والسلاح والمال لما يحتاج إليه","what_is_not_ar":"ليست الإحصاء نفسه ولا عدة المرأة ولا الماء العد"},"support_links":["sup_64f6aab1c4ba2834e1cf"]},{"boundary":"Ortak sınır sayıyla belirlenmiş zaman dilimidir; bekleme, sonradan yerine getirme ve belirli günler birbirinden ayrı bağlamsal gerçekleşmelerdir.","branch_kind":"mixed_non_bare","branch_ref":"root_000989/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَدَّ","morph_features":"STEM|POS:V|PERF|LEM:Ead~a|ROOT:Edd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"19:94:3:2","qac_word_ref":"19:94:3","surface_ar":"عَدَّ"},{"lemma_ar":"عَدّ","morph_features":"STEM|POS:N|LEM:Ead~|ROOT:Edd|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"19:94:4:1","qac_word_ref":"19:94:4","surface_ar":"عَدًّا"}],"gloss":"sayılı zaman dilimi ve bağlama bağlı bekleme ya da tamamlama süresi","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gün, ay, dönemsel çevrim veya olay sonuyla ölçülüp sınırlandırılmış zaman dilimi."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kadının belirli çevrimler, aylar veya gebeliğin sona ermesiyle ölçülen bekleme süresi."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kaçırılmış günlerin sayısına eşit sayıda günü daha sonra yerine getirme yükümlülüğü."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Belirli ve az sayıdaki günlerin adlandırılması."}}],"root_ar":"ع د د","root_id":"root_000989","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sayılı süre çekirdeğini ve bu sürenin farklı bağlamlarda bekleme veya eksik günleri tamamlama işlevini birlikte açıklar.","boundary_detail":"Ortak sınır sayıyla belirlenmiş zaman dilimidir; bekleme, sonradan yerine getirme ve belirli günler birbirinden ayrı bağlamsal gerçekleşmelerdir.","branch_image_ar":"مدة العدة المعدودة","concept_gloss":"sayılı zaman dilimi ve bağlama bağlı bekleme ya da tamamlama süresi","contextual_glosses":[{"applicability":"Kadın için çevrim, ay veya doğumla ölçülen hukuki bekleme bağlamına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölçülmüş süreyi ve yeniden evlenmeden önce bekleme koşulunu korur."},"facet_ids":["F001","F002"],"text":"yeniden evlenmeden önceki bekleme süresi","usage_role":"contextual"},{"applicability":"Yerine getirilemeyen günlerin aynı sayıda başka günle tamamlanması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kaçırılan ve sonradan tamamlanan günler arasındaki sayı eşitliğini korur."},"facet_ids":["F001","F003"],"text":"kaçırılan günler kadar sonradan tamamlama","usage_role":"contextual"},{"applicability":"Özel olarak belirlenmiş, sınırlı sayıdaki günlerden söz edilen bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Günlerin belirli ve sayıca sınırlı oluşunu korur."},"facet_ids":["F001","F004"],"text":"sayılı ve belirli günler","usage_role":"contextual"}],"definition":"Sayısı veya bitiş ölçütü belirlenmiş bir zaman dilimidir. Bağlama göre bu dilim kadın için bekleme süresi, kaçırılan günler kadar sonradan yerine getirme süresi ya da özellikle belirlenmiş sınırlı günler olabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gün, ay, dönemsel çevrim veya olay sonuyla ölçülüp sınırlandırılmış zaman dilimi."},{"facet_id":"F002","role":"specialization","statement":"Bir kadının belirli çevrimler, aylar veya gebeliğin sona ermesiyle ölçülen bekleme süresi."},{"facet_id":"F003","role":"specialization","statement":"Kaçırılmış günlerin sayısına eşit sayıda günü daha sonra yerine getirme yükümlülüğü."},{"facet_id":"F004","role":"example","statement":"Belirli ve az sayıdaki günlerin adlandırılması."}],"identity_rationale":"Kaynak ifadesi yalnızca zorunlu bir bekleme süresini değil, kadın için ölçülen bekleme dönemini, kaçırılan günler kadar sonradan yerine getirme süresini ve belirli sayıda günleri birlikte içerir. Dal korunabilir, ancak bütün örnekleri tek bir bekleme yükümlülüğü gibi sunmak yerine sayıyla sınırlandırılmış zaman dilimleri ve bağlama göre üstlendikleri görevler üzerinden tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kadının yeniden evlenmeden önce beklemesi gereken süre"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kaçırılan günler kadar başka günlerde yerine getirmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"sayılı ve belirli günler"}],"lexicalization_note":"Tanım, sayılı süre çekirdeğini korurken kadınla ilgili bekleme, kaçırılan günleri tamamlama ve belirli günler kalıplarını ayrı tutar.","neighbor_coverage_note":"Bütün adaylar incelendi; ölçülmüş bekleme süresini dönemsel çevrimden, genel saymadan ve sıradan ertelemeden ayıran üç ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı ölçülen toplam süre ve yükümlülükle ilgilidir; komşu dal ise bu sürenin ölçütü olabilen bedensel çevrimin evrelerini adlandırır.","focus_only":"Kadının toplam bekleme süresini, eksik günlerin tamamlanmasını ve başka sayılı günleri kapsar.","gloss":"bekleme süresi ve dönemsel çevrim","neighbor_only":"Kadın bedenindeki kanama ve temizlik evrelerinin kendisini, geçişlerini ve aralarındaki çevrimi adlandırır.","neighbor_ref":"root_001210/B003","relation_type":"near_neighbor","shared_zone":"Kadının bekleme süresi dönemsel bedensel çevrimlerle ölçülebildiği için alanlar kesişir."},{"boundary_match":"partial","distinction":"Odak dalında sayma zaman dilimini ve bağlamsal görevi sınırlar; komşu dalda ise nesnesi zaman olmak zorunda olmayan genel sayma çekirdektir.","focus_only":"Sayının belirlediği zaman dilimini ve bu dilime bağlı bekleme veya tamamlama görevini kapsar.","gloss":"sayılı süre ve genel sayma","neighbor_only":"Her tür varlığı sayma, sayıyı adlandırma ve bir topluluk içinde sayma işlemlerini kapsar.","neighbor_ref":"root_000989/B001","relation_type":"near_neighbor","shared_zone":"Bir sürenin kaç gün veya dönemden oluştuğunu belirleme, genel sayma işlemine dayanır."},{"boundary_match":"partial","distinction":"Odak dalında sayıyla veya bitiş ölçütüyle sınırlandırılmış süre esastır; komşu dalda belirleyici olan yalnızca sonraya bırakmadır.","focus_only":"Ölçüsü belirli bir bekleme veya sonradan tamamlama süresini gerektirir.","gloss":"ölçülü bekleme ve erteleme","neighbor_only":"Bir işi ya da ödemeyi daha sonraki bir zamana bırakma eylemini genel olarak bildirir.","neighbor_ref":"root_000019/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir işlemin daha sonraki bir zamanda gerçekleşmesini içerebilir."}],"source_phrase_ar":"عدة المرأة أيام قروئها (ayn)؛ عدة المرأة معروفة (jamhara)؛ عدة المرأة أيام أقرائها (sihah)؛ العدة عدة المرأة شهورا كانت أو أقراء أو وضع حمل (tahdhib)؛ فعدة من أيام أخر أي عليه أيام بعدد ما فاته (mufradat)؛ الأيام المعدودات أيام التشريق (sihah;tahdhib;mufradat)","source_summary":"Toplu tanıklık, sayıyla veya belirli bir bitiş ölçütüyle sınırlandırılmış zaman dilimlerini; bekleme, eksik günleri tamamlama ve belirli günleri adlandırma bağlamlarında gösterir.","sources":["AY","JA","SI","TA","MU"],"what_is_ar":"المدة المعدودة الواجبة انتظارا أو قضاء كعدة المرأة وعدة الأيام الفائتة والأيام المعدودات","what_is_not_ar":"ليست الأهبة والسلاح ولا مجرد كثرة العدد"},"support_links":[]},{"boundary":"Dalın ayırıcı niteliği suyun kalıcı veya sürekli beslenen oluşudur; geçici yağmur suyu ve kısa ömürlü birikintiler kapsam dışındadır.","branch_kind":"mixed_non_bare","branch_ref":"root_000989/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَدَّ","morph_features":"STEM|POS:V|PERF|LEM:Ead~a|ROOT:Edd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"19:94:3:2","qac_word_ref":"19:94:3","surface_ar":"عَدَّ"},{"lemma_ar":"عَدّ","morph_features":"STEM|POS:N|LEM:Ead~|ROOT:Edd|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"19:94:4:1","qac_word_ref":"19:94:4","surface_ar":"عَدًّا"}],"gloss":"kaynağı kesilmeyen kalıcı su ve su yeri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Doğal olarak bir yerde toplanmış su veya bu suyun bulunduğu yer."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eskiden beri var olan ve su çekildikçe tükenmeyen kalıcı su."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Besleyici kaynağı kesilmediği için akışı veya varlığı sürekli kalan su."}}],"root_ar":"ع د د","root_id":"root_000989","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem sürekli suyu hem de onun doğal olarak toplandığı veya çıkarıldığı kalıcı yeri karşılar.","boundary_detail":"Dalın ayırıcı niteliği suyun kalıcı veya sürekli beslenen oluşudur; geçici yağmur suyu ve kısa ömürlü birikintiler kapsam dışındadır.","branch_image_ar":"الماء العد","concept_gloss":"kaynağı kesilmeyen kalıcı su ve su yeri","contextual_glosses":[{"applicability":"Çekilmesine rağmen besleyici kaynağı sürdüğü için tükenmeyen suyu anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Suyun sürekliliğini ve çekmekle tükenmemesini korur."},"facet_ids":["F002","F003"],"text":"tükenmeyen sürekli su","usage_role":"general"},{"applicability":"Suyun kendisinden çok onu sürekli sağlayan yer veya kaynak kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Suyun bulunduğu yeri ve kaynağın sürekliliğini korur."},"facet_ids":["F001","F003"],"text":"kalıcı su kaynağı","usage_role":"contextual"}],"definition":"Doğal olarak birikmiş, eski veya besleyici kaynağı kesilmediği için çekmekle tükenmeyen sürekli su ve bu suyun bulunduğu kalıcı su yeridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Doğal olarak bir yerde toplanmış su veya bu suyun bulunduğu yer."},{"facet_id":"F002","role":"specialization","statement":"Eskiden beri var olan ve su çekildikçe tükenmeyen kalıcı su."},{"facet_id":"F003","role":"source_variant","statement":"Besleyici kaynağı kesilmediği için akışı veya varlığı sürekli kalan su."}],"identity_rationale":"Kaynak ifadesi doğal su birikimini ve özellikle eski, besleyici kaynağı kesilmeyen, çekmekle tükenmeyen sürekli suyu aynı dalda açıkça tanımlar. Geçici çerçeve hem suyu hem de onun bulunduğu kalıcı su yerini kapsayarak tanıklığa uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"eskiden beri var olan, tükenmeyen sürekli su"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"sürekli sular veya kalıcı su yerleri"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"köklü ve eski saygınlık"}],"lexicalization_note":"Tanım kalıcı su çekirdeğini verir; su yerleri ve eski, köklü olma benzetmesi yalnızca tanıklanan biçim ve kalıpların sınırında tutulur.","neighbor_coverage_note":"Bütün adaylar gözden geçirildi; kalıcı suyu yapılmış havuz suyundan, doğal göletten ve geçici su çukurundan ayıran üç sınır seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında kalıcılık suyun kesilmeyen beslenmesine bağlıdır; komşuda ise suyun bir yapı içinde tutulması esastır ve yenilenmesi gerekmez.","focus_only":"Doğal, eski veya sürekli beslenen ve çekmekle tükenmeyen suyu gerektirir.","gloss":"sürekli kaynak suyu ve havuz suyu","neighbor_only":"Suyun yapılmış bir havuz, sarnıç veya düzeltilmiş su kabında sabit durmasını kapsar.","neighbor_ref":"root_000109/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da belirli bir yerde duran veya toplanan suyu anlatır."},{"boundary_match":"partial","distinction":"Odak dalını belirleyen kesintisiz kaynak ve tükenmezliktir; komşu dalı belirleyen ise birikintinin biçimi ve bol su içermesidir.","focus_only":"Suyun eskiliğini, sürekliliğini ve çekmekle tükenmemesini öne çıkarır.","gloss":"kalıcı su ve gölet","neighbor_only":"Vadi içindeki bol su birikintisini, göleti veya bataklık benzeri su alanını adlandırır.","neighbor_ref":"root_001292/B003","relation_type":"near_neighbor","shared_zone":"Doğal bir çukurda veya arazide toplanan su iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dalı süreklilik ve tükenmezlik gerektirir; komşu dal geçici olarak su tutan yerle sınırlıdır.","focus_only":"Sürekli beslenen veya eskiden beri tükenmeyen suyu ve yerini bildirir.","gloss":"tükenmeyen su ve geçici su çukuru","neighbor_only":"Suyu yalnızca birkaç gün tutabilen çukur, havuz veya gölet benzeri yeri bildirir.","neighbor_ref":"root_000018/B006","relation_type":"near_neighbor","shared_zone":"İki dalda da suyun bir yerde toplanması ve tutulması söz konusudur."}],"source_phrase_ar":"العد مجتمع الماء وجمعه أعداد (maqayis;ayn)؛ العد من الماء القديم الذي لا ينتزح (jamhara)؛ العد بالكسر الماء الذي له مادة لا تنقطع (sihah)؛ الماء العد الدائم الذي لا انقطاع له (tahdhib)؛ ماء عد (mufradat)","source_summary":"Toplu tanıklık, birikmiş su anlamını eski, tükenmeyen ve sürekli beslenen su özellikleriyle açıklar; süreklilik dalın geçici su birikintilerinden ayrılan temel sınırıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"الماء العد ومجتمع الماء والركية القديمة أو الدائمة التي لا ينقطع ماؤها","what_is_not_ar":"ليس ماء السماء ولا ماء الغدران المنقطع ولا العداد الزماني"},"support_links":[]},{"boundary":"Çekirdek belirli zaman ve düzenli geri geliştir; yay ve özel gün kullanımları yalnızca kendi kalıplarında ilişkili anlamlar olarak tutulmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000989/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَدَّ","morph_features":"STEM|POS:V|PERF|LEM:Ead~a|ROOT:Edd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"19:94:3:2","qac_word_ref":"19:94:3","surface_ar":"عَدَّ"},{"lemma_ar":"عَدّ","morph_features":"STEM|POS:N|LEM:Ead~|ROOT:Edd|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"19:94:4:1","qac_word_ref":"19:94:4","surface_ar":"عَدًّا"}],"gloss":"belirli zaman ve bilinen aralıklarla geri gelme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin belirlenmiş zamanı, dönemi veya en güçlü evresi."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir olayın bilinen veya sayılı zaman aralıklarında yeniden ortaya çıkması."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Zehirlenme veya sokulma ağrısının belirli aralıklarla yeniden alevlenmesi."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yayın aralıklı titreşimini veya bu titreşimden çıkan sesi adlandırma."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Dağıtım, yoklama veya geçici toplanma için belirlenmiş günü adlandırma."}}],"root_ar":"ع د د","root_id":"root_000989","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın zaman ve yineleme çekirdeğini verir; kalıba bağlı yay ve özel gün kullanımlarını genel anlama katmaz.","boundary_detail":"Çekirdek belirli zaman ve düzenli geri geliştir; yay ve özel gün kullanımları yalnızca kendi kalıplarında ilişkili anlamlar olarak tutulmalıdır.","branch_image_ar":"عداد الوقت ومعاودته","concept_gloss":"belirli zaman ve bilinen aralıklarla geri gelme","contextual_glosses":[{"applicability":"Bir olayın veya ağrının bilinen zaman aralıklarında tekrar belirdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Zaman aralıklarını ve olayın yeniden ortaya çıkmasını korur."},"facet_ids":["F002","F003"],"text":"belirli aralıklarla yeniden ortaya çıkmak","usage_role":"general"},{"applicability":"Bir kişinin, yönetimin veya başka bir şeyin belirli zamanı ya da en güçlü evresi kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli dönemi ve o dönemin en güçlü evresini korur."},"facet_ids":["F001"],"text":"dönem veya en parlak çağ","usage_role":"contextual"},{"applicability":"Yayın belli aralıklarla titreştirilmesi ya da çıkardığı ses için kullanılan kalıba özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaya özgü tekrarlı titreşim ile ses seçeneklerini korur."},"facet_ids":["F004"],"text":"yayın aralıklı titreşimi veya sesi","usage_role":"contextual"},{"applicability":"Dağıtım, yoklama ya da geçici toplantı için ayrılmış günü anlatan kalıba özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirlenmiş gün ile dağıtım veya toplanma işlevini korur."},"facet_ids":["F005"],"text":"dağıtım veya toplanma günü","usage_role":"contextual"}],"definition":"Bir şeyin belirli zamanı veya dönemi ile belli aralıklarda yeniden ortaya çıkmasıdır. Zehir ağrısının alevlenmesi bunun özel gerçekleşmesiyken yayın sesi ve titreşimi ile dağıtım ya da toplanma günü kalıba bağlı ilişkili kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin belirlenmiş zamanı, dönemi veya en güçlü evresi."},{"facet_id":"F002","role":"core","statement":"Bir olayın bilinen veya sayılı zaman aralıklarında yeniden ortaya çıkması."},{"facet_id":"F003","role":"specialization","statement":"Zehirlenme veya sokulma ağrısının belirli aralıklarla yeniden alevlenmesi."},{"facet_id":"F004","role":"associated_use","statement":"Yayın aralıklı titreşimini veya bu titreşimden çıkan sesi adlandırma."},{"facet_id":"F005","role":"associated_use","statement":"Dağıtım, yoklama veya geçici toplanma için belirlenmiş günü adlandırma."}],"identity_rationale":"Kaynak ifadesi belirli zaman veya dönem ile bilinen aralıklarda geri gelme anlamlarını destekler; zehir ağrısının yeniden alevlenmesi bu çekirdeğin belirgin gerçekleşmesidir. Bununla birlikte yayın sesi veya aralıklı titreşimi ve dağıtım ya da toplanma günü, genel zaman çekirdeğiyle eşitlenmemesi gereken kalıba bağlı ilişkili kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"sokulma ağrısının belirli aralıklarla alevlenmesi"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bana belirli zamanlarda yeniden baş göstermek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"zaman, dönem veya en parlak çağ"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"yayın tekrarlanan titreşimi veya sesi"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"ayda bir gerçekleşen buluşma"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"dağıtım, yoklama veya geçici toplanma günü"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"belirli aralıklarla gelen akıl bulanıklığı"}],"lexicalization_note":"Tanım zaman ve aralıklı geri geliş çekirdeğini ayırır; yay sesi, aylık buluşma ve özel gün anlamlarını kendi kalıplarının dışına genellemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel aralıklı geri gelişi kısa buluşma aralığından, özel dördüncü dönüşten ve yalnızca uygun zamandan ayıran ilişkiler seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı belirli zamanı ve yeniden ortaya çıkmayı genel olarak kapsar; komşu dal iki buluşmayı ayıran kısa süreye özgüdür.","focus_only":"Belirli dönemi, yinelenen ağrıyı ve kalıba bağlı yay veya özel gün kullanımlarını da kapsar.","gloss":"yinelenme zamanı ve buluşmalar arası süre","neighbor_only":"Özellikle iki buluşma arasında kalan kısa ve tekrarlanan zaman aralığını bildirir.","neighbor_ref":"root_001145/B007","relation_type":"near_synonym","shared_zone":"İki dal da olayların belli aralıklarla gerçekleşmesi ve aradaki zamanın sınırlı olması alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dalında aralık bağlama göre değişebilir; komşu dalda ise dördüncü zamana bağlı özel dönüş düzeni belirleyicidir.","focus_only":"Yinelemenin aralığını genel bırakabilir ve dönem, yay sesi veya özel gün kullanımlarına uzanabilir.","gloss":"aralıklı geri geliş ve dördüncü zaman dönüşü","neighbor_only":"Hayvanların sulanması veya ateşli hastalık için her dördüncü zamandaki belirli dönüş düzenini gerektirir.","neighbor_ref":"root_000536/B004","relation_type":"near_neighbor","shared_zone":"Hastalık belirtisinin veya başka bir olayın düzenli zaman aralıklarında geri gelmesi ortak alandır."},{"boundary_match":"partial","distinction":"Odak dalında yineleme önemli bir çekirdektir; komşu dalda olayın zamanı vardır fakat düzenli geri geliş koşulu yoktur.","focus_only":"Belirli aralıklarla yeniden ortaya çıkma ve buna bağlı özel kalıpları kapsar.","gloss":"yinelenen zaman ve uygun an","neighbor_only":"Bir şeyin yalnızca uygun zamanı veya gerçekleşme anını bildirir.","neighbor_ref":"root_000039/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir olayın belirli zamanı veya dönemini gösterebilir."}],"source_phrase_ar":"العداد اهتياج وجع اللديغ (maqayis;ayn;sihah)؛ العداد الشيء الذي يأتيك لوقت (tahdhib)؛ عدان الشيء عهده وزمانه (mufradat)؛ كان ذلك في عدان شبابه (ayn;sihah;tahdhib)؛ عداد القوس أن تنبض بها ساعة بعد ساعة (maqayis)؛ عداد القوس صوتها (sihah;tahdhib)؛ يوم العداد يوم العطاء (maqayis;tahdhib)","source_summary":"Toplu tanıklık, belirli zaman ve belli aralıklarla geri gelme çekirdeğini; ağrının yeniden alevlenmesi, dönemin en güçlü evresi, yayın tekrarlı hareketi veya sesi ve özel bir gün gibi kullanımlarla gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الوقت المعدود المحدد ومعاودة الشيء في أوقات معلومة وما يلحق به من العداد والعدان","what_is_not_ar":"ليس العدد الحسابي وحده ولا العدة الشرعية ولا الماء العد"},"support_links":[]},{"boundary":"Dal sayısal miktardan çok kişiler arasındaki karşılıklı paydaşlık, pay veya denklik ilişkisini bildirir.","branch_kind":"mixed_non_bare","branch_ref":"root_000989/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَدَّ","morph_features":"STEM|POS:V|PERF|LEM:Ead~a|ROOT:Edd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"19:94:3:2","qac_word_ref":"19:94:3","surface_ar":"عَدَّ"},{"lemma_ar":"عَدّ","morph_features":"STEM|POS:N|LEM:Ead~|ROOT:Edd|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"19:94:4:1","qac_word_ref":"19:94:4","surface_ar":"عَدًّا"}],"gloss":"karşılıklı paydaşlık, pay ve denk sayılma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişilerin sayılabilir bir mal, değer veya üstünlükte karşılıklı paydaş olması."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ortaklıktan doğan payları veya özellikle mirasta karşılıklı paydaşları adlandırma."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişiyi başka bir kişinin karşılığı, eşi veya dengi sayma."}}],"root_ar":"ع د د","root_id":"root_000989","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Paylaşılan değer üzerindeki ortaklığı, ortaya çıkan payı ve kişiler arasında kurulan denkliği birlikte karşılar.","boundary_detail":"Dal sayısal miktardan çok kişiler arasındaki karşılıklı paydaşlık, pay veya denklik ilişkisini bildirir.","branch_image_ar":"نظير يعد مع غيره","concept_gloss":"karşılıklı paydaşlık, pay ve denk sayılma","contextual_glosses":[{"applicability":"Kişilerin mal, değer veya üstünlük bakımından birbirine karşı pay sahibi olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Katılımcılar arasındaki karşılıklı ortaklık ve pay ilişkisini korur."},"facet_ids":["F001"],"text":"karşılıklı paydaş olmak","usage_role":"general"},{"applicability":"Ortaklıktaki bölüşüm payları ya da özellikle mirasta birbirine karşı pay sahibi kişiler kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bölüşülen payı ve pay sahipleri arasındaki karşılıklılığı korur."},"facet_ids":["F002"],"text":"paylar veya karşılıklı paydaşlar","usage_role":"contextual"},{"applicability":"Bir kişinin başka biriyle eş düzeyde veya ona karşılık sayıldığı kalıba özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki kişi arasında kurulan denklik ve karşılıklılık ilişkisini korur."},"facet_ids":["F003"],"text":"onun dengi ve karşılığı","usage_role":"contextual"}],"definition":"Birden çok kişinin sayılabilir bir mal, değer veya üstünlük bakımından karşılıklı paydaş olması; bundan doğan payların ya da birbirine karşılık ve denk sayılan kişilerin adlandırılmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişilerin sayılabilir bir mal, değer veya üstünlükte karşılıklı paydaş olması."},{"facet_id":"F002","role":"extension","statement":"Ortaklıktan doğan payları veya özellikle mirasta karşılıklı paydaşları adlandırma."},{"facet_id":"F003","role":"extension","statement":"Bir kişiyi başka bir kişinin karşılığı, eşi veya dengi sayma."}],"identity_rationale":"Kaynak ifadesi karşılıklı olarak sayılabilen mal veya değerlerde ortaklığı, bundan doğan payları ve bir kişinin başka biriyle denk ya da karşılık sayılmasını birlikte verir. Geçici çerçeve, sayma fikrinin bu dalda yalın miktar belirleme değil katılımcılar arasındaki pay ve karşılıklılık ilişkisini kurduğunu doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"mal veya değer bakımından karşılıklı paydaş olmak"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"paylar, denkler veya mirastaki karşılıklı paydaşlar"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"onun dengi ve karşılığı"}],"lexicalization_note":"Tanım paydaşlık, pay ve denk sayılma yüzlerini ayırır; belirli kişi karşılaştırmasını veya miras bağlamını çıplak bir genel sayma anlamına dönüştürmez.","neighbor_coverage_note":"Tüm komşu adayları değerlendirildi; genel paydaşlık ve denkliği salt benzerlikten, genel saymadan ve güç bakımından denk rakipten ayıran üç ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında denklik, daha geniş karşılıklı pay ve katılım alanının bir yüzüdür; komşu dalın çekirdeği doğrudan benzerlik ve eşdeğerliktir.","focus_only":"Paylaşılan mal veya değerde ortaklığı, payları ve mirastaki karşılıklı paydaşları da kapsar.","gloss":"paydaş ve denk","neighbor_only":"İki şeyi benzerlik bakımından birbirinin tam eşi veya örneği olarak karşı karşıya koyar.","neighbor_ref":"root_001520/B006","relation_type":"near_neighbor","shared_zone":"Bir kişinin başka bir kişinin dengi veya karşılığı sayılması iki dalda örtüşür."},{"boundary_match":"partial","distinction":"Odak dalında sayma katılımcılar arasındaki karşılıklı ilişkiyi düzenler; komşu dalda saymanın kendisi ve sayısal sonuç merkezde bulunur.","focus_only":"Sayılabilir bir değer üzerinde karşılıklı pay, paydaşlık veya denklik ilişkisi kurar.","gloss":"karşılıklı pay ve genel sayma","neighbor_only":"Varlıkları tek tek sayıp miktarını belirler ve bir topluluğa dahil sayar.","neighbor_ref":"root_000989/B001","relation_type":"near_neighbor","shared_zone":"Kişilerin başkalarıyla birlikte değerlendirilip sayılması iki dal arasında bağlantı kurar."},{"boundary_match":"partial","distinction":"Odak dalındaki denklik farklı ilişki ve paylaşım bağlamlarına açıktır; komşu dal dengeyi özellikle yaş ve mücadele gücü ekseninde kurar.","focus_only":"Pay, ortaklık ve genel biçimde bir başkasına denk sayılmayı kapsar.","gloss":"genel denk ve güç bakımından denk","neighbor_only":"Özellikle yaş, yiğitlik, güç veya dayanıklılık bakımından birbirine denk rakibi bildirir.","neighbor_ref":"root_001221/B003","relation_type":"near_neighbor","shared_zone":"Bir kişinin başka bir kişiye denk veya eş sayılması ortak alandır."}],"source_phrase_ar":"هم يتعادون إذا اشتركوا فيما يعدد به بعضهم على بعض (ayn;tahdhib)؛ العدائد النظراء (tahdhib)؛ العدائد الحصص (tahdhib)؛ من يعاده في الميراث (sihah)؛ فلان عد فلان أي قرنه (tahdhib)","source_summary":"Toplu tanıklık, karşılıklı paydaş olmayı; pay, mirastaki paydaş ve iki kişi arasında kurulan denklik ya da karşılıklılık kullanımlarıyla aynı ilişki alanında birleştirir.","sources":["AY","SI","TA"],"what_is_ar":"المشاركة والمقارنة والحصة أو النظير حين يعد الشيء مع غيره أو يقابل به","what_is_not_ar":"ليس مجرد كثرة العدد ولا الاستعداد ولا العداد الزماني"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["19:94:1"],"branch_refs":[],"candidate_id":"cand_5cc9fc9dfe09c01b8876","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:94:1:laqad-fusion","source_type":"word_analysis","support_ids":["sup_48ba66ac219c95ef9b54","sup_de56d88b2ca0760eba74"],"title":"compact fusion with completion particle","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:1","qac_refs":["19:94:1:1"],"status":"accepted"}},{"anchor_refs":["19:94:1"],"branch_refs":[],"candidate_id":"cand_45447bba5225f8b05c06","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:94:1:oath-answer-assertion","source_type":"word_analysis","support_ids":["sup_de56d88b2ca0760eba74","sup_f372f3f964055855ec74"],"title":"suppressed-oath assertion frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:1","qac_refs":["19:94:1:1"],"status":"accepted"}},{"anchor_refs":["19:94:2"],"branch_refs":[],"candidate_id":"cand_720605cc5f576fbb676a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:94:2:boundary-verification","source_type":"word_analysis","support_ids":["sup_7fd4841f86073f271ab8","sup_ccc1b61b7d379e3a6bed"],"title":"verification of the prior universal set","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:2","qac_refs":["19:94:1:2"],"status":"accepted"}},{"anchor_refs":["19:94:2"],"branch_refs":[],"candidate_id":"cand_228c05869ed0964c7fd3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:94:2:completed-certainty-scope","source_type":"word_analysis","support_ids":["sup_9ceb4abf7affa0939612","sup_ccc1b61b7d379e3a6bed"],"title":"completed-certainty over the counting sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:2","qac_refs":["19:94:1:2"],"status":"accepted"}},{"anchor_refs":["19:94:2"],"branch_refs":[],"candidate_id":"cand_ae40438f59618d6de484","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:94:2:stacked-laqad-emphasis","source_type":"word_analysis","support_ids":["sup_316ec3314469f2e81eda","sup_ccc1b61b7d379e3a6bed"],"title":"stacked confirmation before the verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:2","qac_refs":["19:94:1:2"],"status":"accepted"}},{"anchor_refs":["19:94:3"],"branch_refs":[],"candidate_id":"cand_4c7f1b5ed686cb7ff4b7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000332"],"scope":"focus_ayah","source_local_id":"19:94:3:active-perfect-object","source_type":"word_analysis","support_ids":["sup_3661f14cb31adad1f3ce","sup_ccfa80ea3b31817705d0"],"title":"active completed enumeration of the prior group","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:3","qac_refs":["19:94:2:2"],"status":"accepted"}},{"anchor_refs":["19:94:3"],"branch_refs":[],"candidate_id":"cand_57b87860574f058eaf8c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000332"],"scope":"focus_ayah","source_local_id":"19:94:3:boundary-inventory","source_type":"word_analysis","support_ids":["sup_3661f14cb31adad1f3ce","sup_8a25679e725e1d2b185f"],"title":"servitude becomes individual accounting","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:3","qac_refs":["19:94:2:2"],"status":"accepted"}},{"anchor_refs":["19:94:3"],"branch_refs":[],"candidate_id":"cand_219778b2dc07dd539bd6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000332"],"scope":"focus_ayah","source_local_id":"19:94:3:comprehensive-to-sequential","source_type":"word_analysis","support_ids":["sup_3661f14cb31adad1f3ce","sup_f70989066b0618c3d2bd"],"title":"first verb sets total inclusion before tally","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:3","qac_refs":["19:94:2:2"],"status":"accepted"}},{"anchor_refs":["19:94:3"],"branch_refs":[],"candidate_id":"cand_c3b9792e74a75d4b166b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000332"],"scope":"focus_ayah","source_local_id":"19:94:3:exhaustive-form-iv","source_type":"word_analysis","support_ids":["sup_3661f14cb31adad1f3ce","sup_db744cdd7148268cb827"],"title":"exhaustive Form IV with pebble-counting pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:3","qac_refs":["19:94:2:2"],"status":"accepted"}},{"anchor_refs":["19:94:3"],"branch_refs":[],"candidate_id":"cand_060d655ef5a08a5c3a3f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000332"],"scope":"focus_ayah","source_local_id":"19:94:3:marked-accounting-register","source_type":"word_analysis","support_ids":["sup_3661f14cb31adad1f3ce","sup_7b005be7de883aa28180"],"title":"rare accounting register and root pairing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:3","qac_refs":["19:94:2:2"],"status":"accepted"}},{"anchor_refs":["19:94:3"],"branch_refs":[],"candidate_id":"cand_34c85e5fc56d7f5a7df9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000332"],"scope":"focus_ayah","source_local_id":"19:94:3:sound-density","source_type":"word_analysis","support_ids":["sup_3661f14cb31adad1f3ce","sup_f3f6192e1fb1c8750e33"],"title":"dense sound suits exhaustive constriction","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:3","qac_refs":["19:94:2:2"],"status":"accepted"}},{"anchor_refs":["19:94:4"],"branch_refs":[],"candidate_id":"cand_10f5809a2d3205f72c99","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:94:4:bound-transition","source_type":"word_analysis","support_ids":["sup_b5ca86e4ec0a1a4bc82b","sup_f060fff2de497ad1cc98"],"title":"bound connector at the counting hinge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:4","qac_refs":["19:94:3:1"],"status":"accepted"}},{"anchor_refs":["19:94:4"],"branch_refs":[],"candidate_id":"cand_664de32f165086e49eb2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:94:4:coordination-not-hal","source_type":"word_analysis","support_ids":["sup_274083edb0137f9dcefd","sup_b5ca86e4ec0a1a4bc82b"],"title":"coordination creates a second completed act","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:4","qac_refs":["19:94:3:1"],"status":"accepted"}},{"anchor_refs":["19:94:4"],"branch_refs":[],"candidate_id":"cand_c1d69211f40735c52989","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:94:4:loose-19-80-backdrop","source_type":"word_analysis","support_ids":["sup_b5ca86e4ec0a1a4bc82b","sup_eeb76c48ed8ec18b996f"],"title":"19:80 contrast kept as backdrop","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:4","qac_refs":["19:94:3:1"],"status":"accepted"}},{"anchor_refs":["19:94:4"],"branch_refs":[],"candidate_id":"cand_57f32cc0b47183a06f28","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:94:4:same-surah-reckoning-echo","source_type":"word_analysis","support_ids":["sup_6ea5a25666253315e494","sup_b5ca86e4ec0a1a4bc82b"],"title":"same-surah counting motif","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:4","qac_refs":["19:94:3:1"],"status":"accepted"}},{"anchor_refs":["19:94:5"],"branch_refs":[],"candidate_id":"cand_c0ef114d0c2b5107d77b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:94:5:cognate-echo-launch","source_type":"word_analysis","support_ids":["sup_b61aad76bcb4a207b2a6","sup_cea356b8bda604d8a501"],"title":"verb launches its own closing echo","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:5","qac_refs":["19:94:3:2","19:94:3:3"],"status":"accepted"}},{"anchor_refs":["19:94:5"],"branch_refs":[],"candidate_id":"cand_6222757feed301e6c9cf","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:94:5:form-branch-guardrail","source_type":"word_analysis","support_ids":["sup_9b2065ded0952be790b5","sup_cea356b8bda604d8a501"],"title":"Form I count, not preparation or causation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:5","qac_refs":["19:94:3:2","19:94:3:3"],"status":"accepted"}},{"anchor_refs":["19:94:5"],"branch_refs":[],"candidate_id":"cand_9fb55dc9de114ffa1c3c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:94:5:marked-root-pair","source_type":"word_analysis","support_ids":["sup_9df9f7eaf82924324505","sup_cea356b8bda604d8a501"],"title":"marked pairing with exhaustive-counting root","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:5","qac_refs":["19:94:3:2","19:94:3:3"],"status":"accepted"}},{"anchor_refs":["19:94:5"],"branch_refs":[],"candidate_id":"cand_9770a1fd6796072c941e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:94:5:reckon-assess-pressure","source_type":"word_analysis","support_ids":["sup_bbf7edc0169a01ad6b53","sup_cea356b8bda604d8a501"],"title":"reckon or assess pressure remains secondary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:5","qac_refs":["19:94:3:2","19:94:3:3"],"status":"accepted"}},{"anchor_refs":["19:94:5"],"branch_refs":[],"candidate_id":"cand_76d184069f9e934f8b05","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:94:5:same-subject-object","source_type":"word_analysis","support_ids":["sup_91114f7d977409159bbe","sup_cea356b8bda604d8a501"],"title":"same actor and same object continue","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:5","qac_refs":["19:94:3:2","19:94:3:3"],"status":"accepted"}},{"anchor_refs":["19:94:5"],"branch_refs":[],"candidate_id":"cand_95bdeed49e050944ecb5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:94:5:sequential-tally","source_type":"word_analysis","support_ids":["sup_c3d0cd195d52c99420b3","sup_cea356b8bda604d8a501"],"title":"sequential tally added to exhaustive enumeration","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:5","qac_refs":["19:94:3:2","19:94:3:3"],"status":"accepted"}},{"anchor_refs":["19:94:5"],"branch_refs":[],"candidate_id":"cand_aaf8fb667fba69537199","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:94:5:sound-compression","source_type":"word_analysis","support_ids":["sup_cea356b8bda604d8a501","sup_e26a3e6ef1d0d3a481f7"],"title":"sound binds target and tally","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:5","qac_refs":["19:94:3:2","19:94:3:3"],"status":"accepted"}},{"anchor_refs":["19:94:6"],"branch_refs":[],"candidate_id":"cand_9400f40d003ce3532bee","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:94:6:act-not-resulting-number","source_type":"word_analysis","support_ids":["sup_2aec0f7fa7f9c861bd43","sup_ba550bdeb2d31bca4f71"],"title":"act named, not numeral displayed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:6","qac_refs":["19:94:4:1"],"status":"accepted"}},{"anchor_refs":["19:94:6"],"branch_refs":[],"candidate_id":"cand_0296ba9d5674b880d975","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:94:6:boundary-granularity","source_type":"word_analysis","support_ids":["sup_2aec0f7fa7f9c861bd43","sup_3349e08ab144a86acfd6"],"title":"cosmic totality contracts into granular count","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:6","qac_refs":["19:94:4:1"],"status":"accepted"}},{"anchor_refs":["19:94:6"],"branch_refs":[],"candidate_id":"cand_d2eec23e0a9bcb315953","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:94:6:closure-architecture","source_type":"word_analysis","support_ids":["sup_165a2ce0800a1a3706e9","sup_2aec0f7fa7f9c861bd43"],"title":"final word completes the tripled count","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:6","qac_refs":["19:94:4:1"],"status":"accepted"}},{"anchor_refs":["19:94:6"],"branch_refs":[],"candidate_id":"cand_bca5871c17cc564b344f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:94:6:cognate-accusative-not-object","source_type":"word_analysis","support_ids":["sup_2aec0f7fa7f9c861bd43","sup_7a0352ebd60b6ba170d1"],"title":"cognate accusative, not a new object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:6","qac_refs":["19:94:4:1"],"status":"accepted"}},{"anchor_refs":["19:94:6"],"branch_refs":[],"candidate_id":"cand_c7e211205e0f21620689","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:94:6:indefinite-thoroughness","source_type":"word_analysis","support_ids":["sup_2aec0f7fa7f9c861bd43","sup_386ad6c5791efc4db813"],"title":"indefinite form magnifies count quality","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:6","qac_refs":["19:94:4:1"],"status":"accepted"}},{"anchor_refs":["19:94:6"],"branch_refs":[],"candidate_id":"cand_0f5ee43521f188b61982","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:94:6:inter-ayah-echoes","source_type":"word_analysis","support_ids":["sup_2aec0f7fa7f9c861bd43","sup_73a7409907ff550740fd"],"title":"same-surah and cross-surah counting echoes","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:6","qac_refs":["19:94:4:1"],"status":"accepted"}},{"anchor_refs":["19:94:6"],"branch_refs":[],"candidate_id":"cand_32a88e781f2585b94788","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:94:6:made-countable-totality","source_type":"word_analysis","support_ids":["sup_2aec0f7fa7f9c861bd43","sup_47fd755fe50f35fe0f3a"],"title":"immeasurable total made countable","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:6","qac_refs":["19:94:4:1"],"status":"accepted"}},{"anchor_refs":["19:94:6"],"branch_refs":[],"candidate_id":"cand_51c3ee375047fa30dc3c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:94:6:marked-gerund-and-root-pair","source_type":"word_analysis","support_ids":["sup_2aec0f7fa7f9c861bd43","sup_79d06b56c07094dfa49f"],"title":"marked gerund slot in the accounting pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:6","qac_refs":["19:94:4:1"],"status":"accepted"}},{"anchor_refs":["19:94:6"],"branch_refs":[],"candidate_id":"cand_11e208dbd6dd0b25d3d9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:94:6:sound-seal","source_type":"word_analysis","support_ids":["sup_2aec0f7fa7f9c861bd43","sup_bccb1cee27041dd58686"],"title":"audible closure of the count","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:94:6","qac_refs":["19:94:4:1"],"status":"accepted"}},{"anchor_refs":["19:94:2"],"branch_refs":[],"candidate_id":"cand_0e7894677627eb32f141","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000332"],"scope":"focus_ayah","source_local_id":"19:94:2:1","source_type":"qac_morpheme","support_ids":["sup_b062318027dfc6430d52"],"title":"QAC root occurrence: ح ص ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["19:94:3"],"branch_refs":[],"candidate_id":"cand_5f4ab43a9f25fe2355d2","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"19:94:3:2","source_type":"qac_morpheme","support_ids":["sup_101f9e3ef776256c9ef4"],"title":"QAC root occurrence: ع د د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["19:94"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"19:94","branch_refs":["root_000332/B002","root_000989/B001"],"candidate_id":"cand_dd433011ceaad84831fb","commentary_obligation":"review","hft_ref":"hft_e8072610af46942946a5","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_exhaustive_individuation","source_type":"hft","support_ids":["sup_0e94df48c4b7335b436f"],"title":"baseline_exhaustive_individuation","trust":"legacy_unbound"},{"anchor_refs":["19:94"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"19:94","branch_refs":["root_000332/B002","root_000989/B002"],"candidate_id":"cand_e2e332880fc30828c229","commentary_obligation":"review","hft_ref":"hft_f288343a648e31206e29","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_prepared_roster","source_type":"hft","support_ids":["sup_64f6aab1c4ba2834e1cf"],"title":"baseline_prepared_roster","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"لَّقَدْ أَحْصَىٰهُمْ وَعَدَّهُمْ عَدًّۭا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"19:94:1:1","qac_word_ref":"19:94:1","root_ar":"","surface_ar":"لَّ"},{"lemma_ar":"قَد","morph_features":"STEM|POS:CERT|LEM:qad","morpheme_role":"STEM","pos":"CERT","qac_ref":"19:94:1:2","qac_word_ref":"19:94:1","root_ar":"","surface_ar":"قَدْ"},{"lemma_ar":"أَحْصَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aHoSaY`|ROOT:HSy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"19:94:2:1","qac_word_ref":"19:94:2","root_ar":"ح ص ي","surface_ar":"أَحْصَىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"19:94:2:2","qac_word_ref":"19:94:2","root_ar":"","surface_ar":"هُمْ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"19:94:3:1","qac_word_ref":"19:94:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"عَدَّ","morph_features":"STEM|POS:V|PERF|LEM:Ead~a|ROOT:Edd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"19:94:3:2","qac_word_ref":"19:94:3","root_ar":"ع د د","surface_ar":"عَدَّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"19:94:3:3","qac_word_ref":"19:94:3","root_ar":"","surface_ar":"هُمْ"},{"lemma_ar":"عَدّ","morph_features":"STEM|POS:N|LEM:Ead~|ROOT:Edd|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"19:94:4:1","qac_word_ref":"19:94:4","root_ar":"ع د د","surface_ar":"عَدًّا"}],"word_analysis_qac_refs":[["19:94:1:1"],["19:94:1:2"],["19:94:2:2"],["19:94:3:1"],["19:94:3:2","19:94:3:3"],["19:94:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["19:94:1","19:94:2","19:94:3","19:94:4","19:94:5","19:94:6"]},"focus_surface_evidence":{"arabic_uthmani":"لَّقَدْ أَحْصَىٰهُمْ وَعَدَّهُمْ عَدًّۭا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"19:94:1:1","qac_word_ref":"19:94:1","root_ar":"","surface_ar":"لَّ"},{"lemma_ar":"قَد","morph_features":"STEM|POS:CERT|LEM:qad","morpheme_role":"STEM","pos":"CERT","qac_ref":"19:94:1:2","qac_word_ref":"19:94:1","root_ar":"","surface_ar":"قَدْ"},{"lemma_ar":"أَحْصَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aHoSaY`|ROOT:HSy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"19:94:2:1","qac_word_ref":"19:94:2","root_ar":"ح ص ي","surface_ar":"أَحْصَىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"19:94:2:2","qac_word_ref":"19:94:2","root_ar":"","surface_ar":"هُمْ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"19:94:3:1","qac_word_ref":"19:94:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"عَدَّ","morph_features":"STEM|POS:V|PERF|LEM:Ead~a|ROOT:Edd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"19:94:3:2","qac_word_ref":"19:94:3","root_ar":"ع د د","surface_ar":"عَدَّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"19:94:3:3","qac_word_ref":"19:94:3","root_ar":"","surface_ar":"هُمْ"},{"lemma_ar":"عَدّ","morph_features":"STEM|POS:N|LEM:Ead~|ROOT:Edd|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"19:94:4:1","qac_word_ref":"19:94:4","root_ar":"ع د د","surface_ar":"عَدًّا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["19:94:1:1"],["19:94:1:2"],["19:94:2:2"],["19:94:3:1"],["19:94:3:2","19:94:3:3"],["19:94:4:1"]],"word_analysis_refs":["19:94:1","19:94:2","19:94:3","19:94:4","19:94:5","19:94:6"],"word_rows":[{"analysis_record_ref":"19:94:1","analytic_gloss_range_en":"assertive oath-answer particle in the compact opening assertion","analytic_root_gloss_range_en":null,"qac_refs":["19:94:1:1"],"root":{"note":"no lexical root (particle or function word)"},"surface":{"arabic":"لَ","transliteration":"la-"}},{"analysis_record_ref":"19:94:2","analytic_gloss_range_en":"certainty and realized completion with the following perfect verb, carried across the coordinated predicate","analytic_root_gloss_range_en":null,"qac_refs":["19:94:1:2"],"root":{"note":"no lexical root (particle or function word)"},"surface":{"arabic":"قَدْ","transliteration":"qad"}},{"analysis_record_ref":"19:94:3","analytic_gloss_range_en":"Form IV perfect exhaustive enumeration with a direct plural object suffix","analytic_root_gloss_range_en":"broad root range includes pebbles, exhaustive counting, judgment, sharp speech, musk-pebble, and bladder-stone branches; the local Form IV verb selects exhaustive enumeration, with pebble-counting imagery as etymological pressure rather than a separate concrete sense","qac_refs":["19:94:2:2"],"root":{"arabic":"ح ص ي","transliteration":"ḥ-ṣ-y"},"surface":{"arabic":"أَحْصَاهُمْ","transliteration":"aḥṣāhum"}},{"analysis_record_ref":"19:94:4","analytic_gloss_range_en":"coordinating conjunction that binds the second completed counting act to the first","analytic_root_gloss_range_en":null,"qac_refs":["19:94:3:1"],"root":{"note":"no lexical root (particle or function word)"},"surface":{"arabic":"وَ","transliteration":"wa-"}},{"analysis_record_ref":"19:94:5","analytic_gloss_range_en":"Form I perfect direct tally of the same plural object, with reckon/assess pressure kept secondary to counting","analytic_root_gloss_range_en":"broad root range includes counting, preparing, prescribed counted terms, perennial water, recurrent timing, and counterparts; the local Form I verb selects counting/reckoning, not preparation or waiting-period branches","qac_refs":["19:94:3:2","19:94:3:3"],"root":{"arabic":"ع د د","transliteration":"ʿ-d-d"},"surface":{"arabic":"عَدَّهُمْ","transliteration":"ʿaddahum"}},{"analysis_record_ref":"19:94:6","analytic_gloss_range_en":"indefinite accusative verbal noun functioning as cognate accusative for the preceding counting verb","analytic_root_gloss_range_en":"broad root range includes counting, preparing, prescribed counted terms, perennial water, recurrent timing, and counterparts; this local gerund selects the counting verbal-noun branch as an intensifying cognate accusative","qac_refs":["19:94:4:1"],"root":{"arabic":"ع د د","transliteration":"ʿ-d-d"},"surface":{"arabic":"عَدًّا","transliteration":"ʿaddā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":6,"words_total":6,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":2,"assigned_records":[{"anchor_refs":["19:94"],"branch_refs":["root_000332/B002","root_000989/B001"],"candidate_id":"cand_dd433011ceaad84831fb","evidence_scope":"focus_ayah","hft_ref":"hft_e8072610af46942946a5","item_id":"baseline_exhaustive_individuation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_exhaustive_individuation","support_id":"sup_0e94df48c4b7335b436f"},{"anchor_refs":["19:94"],"branch_refs":["root_000332/B002","root_000989/B002"],"candidate_id":"cand_e2e332880fc30828c229","evidence_scope":"focus_ayah","hft_ref":"hft_f288343a648e31206e29","item_id":"baseline_prepared_roster","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_prepared_roster","support_id":"sup_64f6aab1c4ba2834e1cf"}],"diagnostics":[],"lane_counts":{"global":7,"macro":10,"micro":2},"packet_summary":{"ayah_count":22,"focus_ref":"19:94","protocol":"focus-trace-pericope-lean-v1","split_root_mappings":[],"window":["19:77","19:78","19:79","19:80","19:81","19:82","19:83","19:84","19:85","19:86","19:87","19:88","19:89","19:90","19:91","19:92","19:93","19:94","19:95","19:96","19:97","19:98"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"valid_pericope_packet_unbound_response"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"19:94","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":7,"source_present":true,"structured_insight_count":12,"unstructured_record_count":0},"identity":{"ayah_ref":"19:94","lane":"micro","linguistic_source_ref":"19:94","surface_ref":"19:94","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"19:94","target_tokens":[["O",["19:94:1"]],["onların",["19:94:1"]],["hepsini",["19:94:2"]],["kuşatmış",["19:94:2"]],["ve",["19:94:3"]],["bir",["19:94:3"]],["bir",["19:94:4"]],["saymıştır",["19:94:4"]]],"text":"O, onların hepsini kuşatmış ve bir bir saymıştır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":2,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":77,"ayah_to":98,"id":"s019-p05-077-098","label":"Boastful deniers and divine inheritance","number":5,"refs":["19:77","19:78","19:79","19:80","19:81","19:82","19:83","19:84","19:85","19:86","19:87","19:88","19:89","19:90","19:91","19:92","19:93","19:94","19:95","19:96","19:97","19:98"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"19:94:3:2","source_type":"qac_morpheme","support_id":"sup_101f9e3ef776256c9ef4","text":"{\"lemma_ar\":\"عَدَّ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:Ead~a|ROOT:Edd|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"19:94:3:2\",\"qac_word_ref\":\"19:94:3\",\"root_ar\":\"ع د د\",\"surface_ar\":\"عَدَّ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:6:closure-architecture","source_type":"word_analysis","support_id":"sup_165a2ce0800a1a3706e9","text":"{\"blocking_evidence\":null,\"headline\":\"final word completes the tripled count\",\"reader_payoff\":\"The reader notices that the ayah lands on a third counting unit, turning two verbs into a closed architecture of total accounting.\",\"reason\":\"The final position, cognate accusative grammar, and two-root sequence support the structural closure payoff.\",\"representative_source_ids\":[\"QT-a60ac443\",\"QT-ca7a6ba9\",\"MT-2ab8ce40\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:4:coordination-not-hal","source_type":"word_analysis","support_id":"sup_274083edb0137f9dcefd","text":"{\"blocking_evidence\":null,\"headline\":\"coordination creates a second completed act\",\"reader_payoff\":\"The reader notices that the second verb is an added predicated act, not a mere circumstance attached to the first.\",\"reason\":\"The attachment layer explicitly coordinates the two perfect verbs, supporting additive force and blocking a circumstantial reading.\",\"representative_source_ids\":[\"QG-abc2f59b\",\"QG-b4d5d847\",\"QS-a321d334\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:6","source_type":"word_analysis","support_id":"sup_2aec0f7fa7f9c861bd43","text":"{\"gloss_range\":\"indefinite accusative verbal noun functioning as cognate accusative for the preceding counting verb\",\"prose\":\"{{ar:عَدًّا}} ({{tr:ʿaddā}}) is not another counted entity after {{ar:هُمْ}} ({{tr:-hum}}); it is the cognate accusative governed by {{ar:عَدَّهُمْ}} ({{tr:ʿaddahum}}). The final noun turns the action back onto itself, naming the act of counting and intensifying it as a thorough counting rather than displaying a resulting numeral; in the larger sequence, the apparently immeasurable total has been made countable. Its indefinite accusative and tanwīn leave the count's quality open and emphatic, while the lack of a suffix keeps the object fixed on the preceding verb. As the last word, it makes the ayah land on a three-part architecture: exhaustive enumeration, direct tally, and the count named again. The adjacent echo {{ar:عَدَّهُمْ عَدًّا}} ({{tr:ʿaddahum ʿaddā}}), the same-surah recurrence in 19:84, and the parallel with 72:28 all make the closure both semantic and audible: the repeated doubled dāl carries the verb's compressed tallying sound into the maṣdar, and the final tanwīn gives the count its nasal endpoint.\",\"root_display\":\"{{ar:ع د د}} ({{tr:ʿ-d-d}})\",\"root_gloss_range\":\"broad root range includes counting, preparing, prescribed counted terms, perennial water, recurrent timing, and counterparts; this local gerund selects the counting verbal-noun branch as an intensifying cognate accusative\",\"surface_display\":\"{{ar:عَدًّا}} ({{tr:ʿaddā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:2:stacked-laqad-emphasis","source_type":"word_analysis","support_id":"sup_316ec3314469f2e81eda","text":"{\"blocking_evidence\":null,\"headline\":\"stacked confirmation before the verb\",\"reader_payoff\":\"The reader notices two confirmers stacked before any counting verb appears.\",\"reason\":\"The local opening combines the assertive lām and {{ar:قَدْ}} ({{tr:qad}}), so the compound emphasis is a surface feature rather than an inferred embellishment.\",\"representative_source_ids\":[\"MG-b2da3b64\",\"QI-b11942b6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:6:boundary-granularity","source_type":"word_analysis","support_id":"sup_3349e08ab144a86acfd6","text":"{\"blocking_evidence\":null,\"headline\":\"cosmic totality contracts into granular count\",\"reader_payoff\":\"The reader notices that the universal scene from 19:93 ends as individually complete accounting in the final word.\",\"reason\":\"The boundary rows coherently connect the prior universal scope to the local closing cognate accusative without changing its grammar.\",\"representative_source_ids\":[\"QB-3c940264\",\"QB-d093e4a1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:3","source_type":"word_analysis","support_id":"sup_3661f14cb31adad1f3ce","text":"{\"gloss_range\":\"Form IV perfect exhaustive enumeration with a direct plural object suffix\",\"prose\":\"{{ar:أَحْصَاهُمْ}} ({{tr:aḥṣāhum}}) is an active 3ms perfect with {{ar:هُمْ}} ({{tr:-hum}}) as its direct object, so the first counting act is completed, active, and aimed immediately at the same universal group carried from 19:93. The Form IV verb selects exhaustive enumeration and retained accounting knowledge; the root's pebble-counting image makes that totality feel individually registered, while local grammar keeps the concrete pebble branch from replacing the enumerating sense. Placed before {{ar:عَدَّهُمْ}} ({{tr:ʿaddahum}}), it starts a movement from comprehensive inclusion into sequential tallying. Its rare Qur'anic accounting register and links with {{ar:ع د د}} ({{tr:ʿ-d-d}}) in 72:28 and 65:1 make the verb more specialized than a routine count, and its constricted ḥāʾ plus emphatic ṣād give the exhaustive verb dense acoustic weight.\",\"root_display\":\"{{ar:ح ص ي}} ({{tr:ḥ-ṣ-y}})\",\"root_gloss_range\":\"broad root range includes pebbles, exhaustive counting, judgment, sharp speech, musk-pebble, and bladder-stone branches; the local Form IV verb selects exhaustive enumeration, with pebble-counting imagery as etymological pressure rather than a separate concrete sense\",\"surface_display\":\"{{ar:أَحْصَاهُمْ}} ({{tr:aḥṣāhum}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:6:indefinite-thoroughness","source_type":"word_analysis","support_id":"sup_386ad6c5791efc4db813","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite form magnifies count quality\",\"reader_payoff\":\"The reader notices that the indefinite accusative points to the quality and thoroughness of the counting act, not to a known named count.\",\"reason\":\"The local form is indefinite accusative with tanwīn in cognate accusative position, matching the CRITICAL claim of qualitative intensification.\",\"representative_source_ids\":[\"QS-2c1e6fb6\",\"QF-0ad22bca\",\"QF-747f021d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:6:made-countable-totality","source_type":"word_analysis","support_id":"sup_47fd755fe50f35fe0f3a","text":"{\"blocking_evidence\":null,\"headline\":\"immeasurable total made countable\",\"reader_payoff\":\"The reader notices the pressure that the vast prior total has been made countable, while the local noun still functions as verbal intensifier.\",\"reason\":\"The innumerability contrast survives as semantic pressure from the larger sequence, but grammar keeps {{ar:عَدًّا}} ({{tr:ʿaddā}}) as a cognate accusative rather than an independent quantifier.\",\"representative_source_ids\":[\"QS-2c483f73\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:1:laqad-fusion","source_type":"word_analysis","support_id":"sup_48ba66ac219c95ef9b54","text":"{\"blocking_evidence\":null,\"headline\":\"compact fusion with completion particle\",\"reader_payoff\":\"The reader notices that the oath-force is not free-standing; it is heard and written as part of the compact {{ar:لَقَدْ}} ({{tr:laqad}}) certainty cluster.\",\"reason\":\"The particle is locally bound to the following certainty particle in the surface opening, so the formal and audible fusion is a valid reader-facing payoff.\",\"representative_source_ids\":[\"QF-e499c41f\",\"QP-710e26fb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:4:same-surah-reckoning-echo","source_type":"word_analysis","support_id":"sup_6ea5a25666253315e494","text":"{\"blocking_evidence\":null,\"headline\":\"same-surah counting motif\",\"reader_payoff\":\"The reader notices that the conjunction leads into a counting phrase that recalls the same-surah reckoning pattern in 19:84.\",\"reason\":\"The rows supply the concrete same-surah reference, and the local connector introduces the count phrase where that motif returns.\",\"representative_source_ids\":[\"QE-880eb936\",\"ME-75cc39ba\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:6:inter-ayah-echoes","source_type":"word_analysis","support_id":"sup_73a7409907ff550740fd","text":"{\"blocking_evidence\":null,\"headline\":\"same-surah and cross-surah counting echoes\",\"reader_payoff\":\"The reader notices that the closing count echoes the same-surah cognate-counting phrase in 19:84 and the broader accounting formula in 72:28.\",\"reason\":\"The CRITICAL rows give concrete references, and the local cognate accusative supplies the formal basis for the echo.\",\"representative_source_ids\":[\"QE-5351d858\",\"QE-60456889\",\"QE-6bf55908\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:6:marked-gerund-and-root-pair","source_type":"word_analysis","support_id":"sup_79d06b56c07094dfa49f","text":"{\"blocking_evidence\":null,\"headline\":\"marked gerund slot in the accounting pair\",\"reader_payoff\":\"The reader notices that a common root becomes marked by being funneled into the rare closing gerund slot of the {{ar:ح ص ي}} ({{tr:ḥ-ṣ-y}}) and {{ar:ع د د}} ({{tr:ʿ-d-d}}) pair.\",\"reason\":\"The contextual profiles mark the local gerund as low-occurrence and tied to cognate-accusative behavior, while the row set connects it to the root pair.\",\"representative_source_ids\":[\"QI-0d9c0728\",\"QI-724ff4f1\",\"QH-02001000\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:6:cognate-accusative-not-object","source_type":"word_analysis","support_id":"sup_7a0352ebd60b6ba170d1","text":"{\"blocking_evidence\":null,\"headline\":\"cognate accusative, not a new object\",\"reader_payoff\":\"The reader notices that the final noun intensifies the preceding verb rather than adding another participant to the clause.\",\"reason\":\"The attachment layer forces a cognate accusative relation to the previous verb, so the final noun is verbal intensification rather than a second object.\",\"representative_source_ids\":[\"QG-1f9ef9e2\",\"QG-99b6420c\",\"QG-af5a7122\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:3:marked-accounting-register","source_type":"word_analysis","support_id":"sup_7b005be7de883aa28180","text":"{\"blocking_evidence\":null,\"headline\":\"rare accounting register and root pairing\",\"reader_payoff\":\"The reader notices that this is a specialized Qur'anic accounting register, reinforced by parallels where exhaustive counting and number language meet.\",\"reason\":\"The contextual profiles show a limited Form IV accounting distribution, and the CRITICAL rows provide concrete cross-references, including 72:28 and 65:1.\",\"representative_source_ids\":[\"QI-bd5f1a7d\",\"QI-d03a1ebb\",\"MI-8b53eff7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:2:boundary-verification","source_type":"word_analysis","support_id":"sup_7fd4841f86073f271ab8","text":"{\"blocking_evidence\":null,\"headline\":\"verification of the prior universal set\",\"reader_payoff\":\"The reader notices that 19:94 functions as verification after the universal statement in 19:93.\",\"reason\":\"The pronoun-chain rows and boundary rows support reading the completed assertion as answering the prior universal group, while the local grammar keeps the claim inside 19:94's perfect verbal sequence.\",\"representative_source_ids\":[\"QB-15d2822a\",\"QB-83247109\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:3:boundary-inventory","source_type":"word_analysis","support_id":"sup_8a25679e725e1d2b185f","text":"{\"blocking_evidence\":null,\"headline\":\"servitude becomes individual accounting\",\"reader_payoff\":\"The reader notices the movement from universal servant-status in 19:93 to individually accounted belonging in 19:94.\",\"reason\":\"The attached object suffix and boundary rows make the previous ayah's total group the local object of enumeration.\",\"representative_source_ids\":[\"QB-236af99c\",\"QB-4a69623f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:5:same-subject-object","source_type":"word_analysis","support_id":"sup_91114f7d977409159bbe","text":"{\"blocking_evidence\":null,\"headline\":\"same actor and same object continue\",\"reader_payoff\":\"The reader notices that the second verb neither changes agent nor shifts object; it repeats the completed action grammar over the same group.\",\"reason\":\"The QAC and attachment data show a coordinated active perfect with the same direct object suffix pattern.\",\"representative_source_ids\":[\"QG-1a44478c\",\"QG-800b2c17\",\"QG-8afdfdf1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:5:form-branch-guardrail","source_type":"word_analysis","support_id":"sup_9b2065ded0952be790b5","text":"{\"blocking_evidence\":null,\"headline\":\"Form I count, not preparation or causation\",\"reader_payoff\":\"The reader notices that the selected form keeps the root on direct enumeration, while preparation-family associations only suggest fixed apportionment in the background.\",\"reason\":\"V4 lists a preparation branch, but the local Form I verb plus direct object and cognate continuation select the counting branch; the gemination is root-internal.\",\"representative_source_ids\":[\"QF-63b7336a\",\"QF-9a4fd01e\",\"QS-ebd047de\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:2:completed-certainty-scope","source_type":"word_analysis","support_id":"sup_9ceb4abf7affa0939612","text":"{\"blocking_evidence\":null,\"headline\":\"completed-certainty over the counting sequence\",\"reader_payoff\":\"The reader notices that completion and certainty govern the whole paired-counting report, not only the first verb.\",\"reason\":\"QAC marks {{ar:قَدْ}} ({{tr:qad}}) with a perfect verb as certainty and completion, and the attachment layer coordinates the second perfect clause under the same assertion.\",\"representative_source_ids\":[\"QG-3800418a\",\"QG-b007ab16\",\"QT-8e08dac9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:5:marked-root-pair","source_type":"word_analysis","support_id":"sup_9df9f7eaf82924324505","text":"{\"blocking_evidence\":null,\"headline\":\"marked pairing with exhaustive-counting root\",\"reader_payoff\":\"The reader notices a marked accounting pair: common {{ar:ع د د}} ({{tr:ʿ-d-d}}) becomes sharpened by being yoked to rarer {{ar:ح ص ي}} ({{tr:ḥ-ṣ-y}}).\",\"reason\":\"Contextual rows and CRITICAL cross-references support the root-pair payoff, including the explicit parallel in 72:28.\",\"representative_source_ids\":[\"QI-b5a46979\",\"QI-cf2386b2\",\"QE-01ebade3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"19:94:2:1","source_type":"qac_morpheme","support_id":"sup_b062318027dfc6430d52","text":"{\"lemma_ar\":\"أَحْصَىٰ\",\"morph_features\":\"STEM|POS:V|PERF|(IV)|LEM:>aHoSaY`|ROOT:HSy|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"19:94:2:1\",\"qac_word_ref\":\"19:94:2\",\"root_ar\":\"ح ص ي\",\"surface_ar\":\"أَحْصَىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:4","source_type":"word_analysis","support_id":"sup_b5ca86e4ec0a1a4bc82b","text":"{\"gloss_range\":\"coordinating conjunction that binds the second completed counting act to the first\",\"prose\":\"{{ar:وَ}} ({{tr:wa-}}) is coordination, not a circumstantial aside, so {{ar:عَدَّهُمْ}} ({{tr:ʿaddahum}}) stands as a second completed act beside {{ar:أَحْصَاهُمْ}} ({{tr:aḥṣāhum}}). The bound connector carries the reader from exhaustive enumeration into sequential tally, keeping the second verb additive rather than merely repetitive. Its surface fusion in {{ar:وَعَدَّهُمْ}} ({{tr:wa-ʿaddahum}}) makes the joining visible and audible, and the same-surah echo with the counting pattern in 19:84 reinforces the reckoning motif; a looser contrast with 19:80 remains only a backdrop, not a control on this conjunction's parse.\",\"root_display\":\"no lexical root (particle or function word)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa-}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:5:cognate-echo-launch","source_type":"word_analysis","support_id":"sup_b61aad76bcb4a207b2a6","text":"{\"blocking_evidence\":null,\"headline\":\"verb launches its own closing echo\",\"reader_payoff\":\"The reader notices that the second verb receives its own structural completion when the next word repeats its root as a cognate accusative.\",\"reason\":\"The attachment layer marks the following word as a cognate accusative of this verb, so the immediate echo is structurally forced.\",\"representative_source_ids\":[\"QT-5275f299\",\"QE-0a4f3b3f\",\"QY-b56bb001\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:6:act-not-resulting-number","source_type":"word_analysis","support_id":"sup_ba550bdeb2d31bca4f71","text":"{\"blocking_evidence\":null,\"headline\":\"act named, not numeral displayed\",\"reader_payoff\":\"The reader notices that the ayah closes on the completed process of counting rather than on a visible numeral.\",\"reason\":\"The word is an unsuffixed verbal noun governed by the prior verb; it names the counting action while the object remains on {{ar:عَدَّهُمْ}} ({{tr:ʿaddahum}}).\",\"representative_source_ids\":[\"QS-ee474905\",\"QF-fd72aeaa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:5:reckon-assess-pressure","source_type":"word_analysis","support_id":"sup_bbf7edc0169a01ad6b53","text":"{\"blocking_evidence\":null,\"headline\":\"reckon or assess pressure remains secondary\",\"reader_payoff\":\"The reader notices that the counted beings are also reckonable or assessable, while the local verb remains a counting verb.\",\"reason\":\"The reckon/consider nuance belongs to the accepted counting branch, but the direct cognate-counting construction keeps literal tallying primary.\",\"representative_source_ids\":[\"QS-3fd96c86\",\"QS-7ac458bc\",\"MS-93ade0a0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:6:sound-seal","source_type":"word_analysis","support_id":"sup_bccb1cee27041dd58686","text":"{\"blocking_evidence\":null,\"headline\":\"audible closure of the count\",\"reader_payoff\":\"The reader notices that the repeated doubled consonant and final nasal ending make the semantic closure audible.\",\"reason\":\"The sound rows are locally grounded in the final surface form and reinforce the word's role as semantic closure.\",\"representative_source_ids\":[\"QP-5dd18557\",\"QP-bcb09902\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:5:sequential-tally","source_type":"word_analysis","support_id":"sup_c3d0cd195d52c99420b3","text":"{\"blocking_evidence\":null,\"headline\":\"sequential tally added to exhaustive enumeration\",\"reader_payoff\":\"The reader notices that the second verb refines total inclusion into unit-by-unit tally rather than merely repeating the first verb.\",\"reason\":\"The coordinated order and lexical ranges support a distinction between comprehensive enumeration and sequential counting.\",\"representative_source_ids\":[\"QS-a37befac\",\"MS-c7cac52b\",\"QT-9e2bdc1a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:2","source_type":"word_analysis","support_id":"sup_ccc1b61b7d379e3a6bed","text":"{\"gloss_range\":\"certainty and realized completion with the following perfect verb, carried across the coordinated predicate\",\"prose\":\"{{ar:قَدْ}} ({{tr:qad}}) turns the first perfect verb into completed certainty, not a future possibility or bare report. Because the clause continues through the coordinated second perfect verb and final cognate accusative, the {{ar:لَقَدْ}} ({{tr:laqad}}) frame covers the whole two-verb counting architecture. It also answers the prior universal claim by shifting from what every being is in 19:93 to what has already been done to them in 19:94.\",\"root_display\":\"no lexical root (particle or function word)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:قَدْ}} ({{tr:qad}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:3:active-perfect-object","source_type":"word_analysis","support_id":"sup_ccfa80ea3b31817705d0","text":"{\"blocking_evidence\":null,\"headline\":\"active completed enumeration of the prior group\",\"reader_payoff\":\"The reader notices that the counted group is not an abstraction; it is the direct object attached to a completed active verb.\",\"reason\":\"The local morphology and attachment evidence force an active perfect verb with direct object suffix, and the boundary rows identify the suffix's prior universal antecedent.\",\"representative_source_ids\":[\"QG-03e762a4\",\"QG-5088b958\",\"QG-6b90836f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:5","source_type":"word_analysis","support_id":"sup_cea356b8bda604d8a501","text":"{\"gloss_range\":\"Form I perfect direct tally of the same plural object, with reckon/assess pressure kept secondary to counting\",\"prose\":\"{{ar:عَدَّهُمْ}} ({{tr:ʿaddahum}}) repeats the active perfect grammar and repeats {{ar:هُمْ}} ({{tr:-hum}}), so the same implied subject counts the same group already encompassed by {{ar:أَحْصَاهُمْ}} ({{tr:aḥṣāhum}}). Its Form I shape keeps the root in direct tallying, not Form IV preparation, with any preparation-family pressure limited to a fixed apportioned total; the geminated consonant is lexical rather than a Form II causative, but it still presses the tallying verb audibly. Beside the exhaustive first verb, this second verb adds sequential unit-by-unit reckoning; the reckon-as-assess nuance survives as secondary pressure on the counted group's status, but it does not replace literal counting. The word also launches the immediate echo {{ar:عَدَّهُمْ عَدًّا}} ({{tr:ʿaddahum ʿaddā}}), tying the rare {{ar:ح ص ي}} ({{tr:ḥ-ṣ-y}}) and {{ar:ع د د}} ({{tr:ʿ-d-d}}) accounting pair to parallels such as 72:28 and the same-surah pattern in 19:84, while the nasal object ending leads into the final tanwīn as a sound bridge from target to intensifier.\",\"root_display\":\"{{ar:ع د د}} ({{tr:ʿ-d-d}})\",\"root_gloss_range\":\"broad root range includes counting, preparing, prescribed counted terms, perennial water, recurrent timing, and counterparts; the local Form I verb selects counting/reckoning, not preparation or waiting-period branches\",\"surface_display\":\"{{ar:عَدَّهُمْ}} ({{tr:ʿaddahum}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:3:exhaustive-form-iv","source_type":"word_analysis","support_id":"sup_db744cdd7148268cb827","text":"{\"blocking_evidence\":null,\"headline\":\"exhaustive Form IV with pebble-counting pressure\",\"reader_payoff\":\"The reader notices exhaustive enumeration as the selected sense, enriched by the root's concrete counting image without turning the word into a literal pebble scene.\",\"reason\":\"V4 distinguishes the pebble branch from the exhaustive-counting branch; the CRITICAL root-image payoff survives as imagery, while the local Form IV verb selects enumeration.\",\"representative_source_ids\":[\"QS-61003030\",\"QS-ac358a1b\",\"QF-7e80c651\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:1","source_type":"word_analysis","support_id":"sup_de56d88b2ca0760eba74","text":"{\"gloss_range\":\"assertive oath-answer particle in the compact opening assertion\",\"prose\":\"{{ar:لَ}} ({{tr:la-}}) opens the ayah before the verb, so the reader first hears verification rather than a neutral narrative start. Its force is the suppressed-oath or assertive frame of {{ar:لَقَدْ}} ({{tr:laqad}}): the coming enumeration is presented as certified fact, and the compact fusion with {{ar:قَدْ}} ({{tr:qad}}) makes oath-force and completed certainty arrive as one onset.\",\"root_display\":\"no lexical root (particle or function word)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَ}} ({{tr:la-}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:5:sound-compression","source_type":"word_analysis","support_id":"sup_e26a3e6ef1d0d3a481f7","text":"{\"blocking_evidence\":null,\"headline\":\"sound binds target and tally\",\"reader_payoff\":\"The reader notices the compressed sound of the tallying verb and its nasal movement toward the final cognate noun.\",\"reason\":\"The sound rows are tied to the local surface and reinforce, rather than replace, the grammar of direct tallying.\",\"representative_source_ids\":[\"QP-1fd0471f\",\"QP-ca714625\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:4:loose-19-80-backdrop","source_type":"word_analysis","support_id":"sup_eeb76c48ed8ec18b996f","text":"{\"blocking_evidence\":null,\"headline\":\"19:80 contrast kept as backdrop\",\"reader_payoff\":\"The reader can keep 19:80 as a same-surah backdrop about solitary return and inherited speech, while the local word still functions simply as coordination.\",\"reason\":\"The concrete reference may survive as a broad same-surah contrast, but the local grammar gives {{ar:وَ}} ({{tr:wa-}}) no more than coordinating force.\",\"representative_source_ids\":[\"MI-e471cd75\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:4:bound-transition","source_type":"word_analysis","support_id":"sup_f060fff2de497ad1cc98","text":"{\"blocking_evidence\":null,\"headline\":\"bound connector at the counting hinge\",\"reader_payoff\":\"The reader notices the hinge from comprehensive enumeration to tally as a bound surface transition, not a loose discourse marker.\",\"reason\":\"The conjunction is written and recited as a proclitic on the second verb, so the form supports the transition payoff.\",\"representative_source_ids\":[\"QF-307992ec\",\"QT-61046628\",\"QP-dd62a1d2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:1:oath-answer-assertion","source_type":"word_analysis","support_id":"sup_f372f3f964055855ec74","text":"{\"blocking_evidence\":null,\"headline\":\"suppressed-oath assertion frame\",\"reader_payoff\":\"The reader notices that the ayah begins inside a verification frame before it names the act of counting.\",\"reason\":\"QAC identifies the lām as assertive or oath-answer force, and nothing in the guardrails weakens that scope over the following perfect clause.\",\"representative_source_ids\":[\"QG-919ad1cf\",\"QS-1adb8d0d\",\"QT-64b78e03\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:3:sound-density","source_type":"word_analysis","support_id":"sup_f3f6192e1fb1c8750e33","text":"{\"blocking_evidence\":null,\"headline\":\"dense sound suits exhaustive constriction\",\"reader_payoff\":\"The reader notices that the verb's constricted sounds give the exhaustive-counting word a compressed acoustic weight.\",\"reason\":\"The sound observation is locally tied to the surface word and does not require a semantic branch beyond the selected exhaustive-counting sense.\",\"representative_source_ids\":[\"QP-0de7ab43\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:94:3:comprehensive-to-sequential","source_type":"word_analysis","support_id":"sup_f70989066b0618c3d2bd","text":"{\"blocking_evidence\":null,\"headline\":\"first verb sets total inclusion before tally\",\"reader_payoff\":\"The reader notices that the first verb establishes total coverage before the next verb adds unit-by-unit tally.\",\"reason\":\"The coordinated clause order and lexical distinction between the two roots support a progression rather than simple synonym doubling.\",\"representative_source_ids\":[\"MS-f97baea0\",\"QT-8c04db50\",\"QT-8e4631ed\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"لَّقَدْ أَحْصَىٰهُمْ وَعَدَّهُمْ عَدًّۭا","ayah_ref":"19:94"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000332/B002","root_000989/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000332","role":"Exhaustive enumeration and encompassed knowledge supply complete coverage of the plural object.","root":"ح ص ي","source_ref":"19:94","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000989","role":"Counting the enumerated and gathering numbers make that coverage an explicit item-by-item tally.","root":"ع د د","source_ref":"19:94","source_word_indices":["3","4"]}],"changed_reading":{"after":"He has exhaustively brought every member of them within an explicit tally, leaving no unregistered remainder.","before":"He knows or counts them collectively."},"confidence":"strong","focus_anchor":"The sequence at 19:94 joins أَحْصَىٰهُمْ to the intensified وَعَدَّهُمْ عَدًّا.","mechanism":"Exhaustive encompassment is followed by explicit counting and a cognate accusative, turning an undifferentiated plural into a completed itemized total.","model_id":"baseline_exhaustive_individuation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_exhaustive_individuation","source_type":"hft","support_id":"sup_0e94df48c4b7335b436f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَّقَدْ أَحْصَىٰهُمْ وَعَدَّهُمْ عَدًّۭا","ayah_ref":"19:94"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000332/B002","root_000989/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000332","role":"Exhaustive enumeration guarantees that the roster lacks no member.","root":"ح ص ي","source_ref":"19:94","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000989","role":"Preparing equipment or provision changes the count from a statistic into readiness for what follows.","root":"ع د د","source_ref":"19:94","source_word_indices":["3","4"]}],"changed_reading":{"after":"The verse presents a complete roster already inventoried and readied for a coming operation.","before":"The verse reports a static census."},"confidence":"medium","focus_anchor":"The same ع د د occurrence can carry both counting and the preparation of an عُدَّة.","mechanism":"Once أَحْصَىٰ establishes completeness, عَدَّهُمْ can image the total not only as known but as made into a ready roster for an event.","model_id":"baseline_prepared_roster"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_prepared_roster","source_type":"hft","support_id":"sup_64f6aab1c4ba2834e1cf","trust":"legacy_unbound"}]}
</lane_packet_json>
