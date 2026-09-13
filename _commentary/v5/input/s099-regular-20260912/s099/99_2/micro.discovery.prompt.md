# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **99:2**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s099-regular-20260912/s099/99_2/micro.discovery.json` and modify nothing
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
  "ayah_ref": "99:2",
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
{"branch_registry":[{"boundary":"Temel yer anlamı ile yalnız tamlamalarda beliren alt bölüm ve hayvan ayağı anlamları birbirinden ayrılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000025/B001","candidate_links":[{"candidate_id":"cand_fd4bbfaa69ddab402681","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:2:2","qac_word_ref":"99:2:2","surface_ar":"أَرْضُ"}],"gloss":"yer ve yere bakan alt bölüm","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Göğün karşısında aşağıda bulunan ve üzerinde yaşanan yer küresidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyin yere bakan alt bölümü, belirli bir tamlama içinde bu adla anılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hayvanın tırnağı veya ayağının yere değen alt bölümü için kullanılan özel bir tamlama vardır."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer küresi anlamını ve ona bağlı alt bölüm yönelimini birlikte özetleyen en kısa doğal karşılıktır.","boundary_detail":"Temel yer anlamı ile yalnız tamlamalarda beliren alt bölüm ve hayvan ayağı anlamları birbirinden ayrılmalıdır.","branch_image_ar":"السفل المقابل للسماء","concept_gloss":"yer ve yere bakan alt bölüm","contextual_glosses":[{"applicability":"Üzerinde yaşanan ve göğün karşısında bulunan yer küresi söz konusu olduğunda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesnelerin altı ile hayvan ayağının alt bölümüne bağlı kullanımları dışarıda bırakır.","preserves":"Üzerinde yaşanan aşağı yer ve göğe karşıt konum anlamını korur."},"facet_ids":["F001"],"text":"yeryüzü","usage_role":"contextual"}],"definition":"Göğün karşısında aşağıda bulunan, üzerinde yaşadığımız yer küresini belirtir. Belirli tamlamalarda bir şeyin yere bakan altını ve hayvanın tırnağını ya da ayağının alt bölümünü de anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Göğün karşısında aşağıda bulunan ve üzerinde yaşanan yer küresidir."},{"facet_id":"F002","role":"extension","statement":"Bir şeyin yere bakan alt bölümü, belirli bir tamlama içinde bu adla anılır."},{"facet_id":"F003","role":"specialization","statement":"Hayvanın tırnağı veya ayağının yere değen alt bölümü için kullanılan özel bir tamlama vardır."}],"identity_rationale":"Kaynak ifadesi, göğün karşısında aşağıda bulunan ve üzerinde yaşanan yeri temel anlam olarak verir; nesnelerin yere bakan altı ile hayvan ayağının alt bölümü de buna bağlı kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yer, yeryüzü"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yerler, ülkeler"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyin yere bakan altı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"hayvanın tırnağı veya ayaklarının altı"}],"lexicalization_note":"Tanım yalın yer anlamını kapsar; alt bölüm ve hayvan ayağı anlamlarını ise yalnız belirtilen tamlamalara bağlı yan yüzler olarak tutar.","neighbor_coverage_note":"Sağlanan bütün komşu kartları değerlendirildi; yer yüzeyiyle doğrudan karışabilecek en yararlı sınır karşılaştırması yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği aşağıda ve göğün karşısında bulunan yerdir; komşu dal ise yüzeyin genişliği ve düzlüğü ile serilmiş eşya fikrini öne çıkarır.","focus_only":"Göğün karşısındaki yer küresini ve tamlamalardaki alt bölüm anlamlarını kapsar.","gloss":"geniş düz yer veya yaygı","neighbor_only":"Geniş ve düz araziyi, ayrıca serilip yayılan eşyayı anlatır.","neighbor_ref":"root_000116/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da yayılmış bir yüzey olarak yer alanına dokunur."}],"source_phrase_ar":"كل شيء يسفل ويقابل السماء (maqayis)؛ الأرض التي نحن عليها (maqayis)؛ الأرض الجرم المقابل للسماء (mufradat)؛ كل ما سفل فهو أرض (sihah)؛ الأرض حافر الدابة (ayn)؛ أسفل قوائم الدابة (sihah)","source_summary":"Kaynaklar, anlamın merkezinde göğün karşısındaki aşağı yerin bulunduğunu; alt bölüm ve hayvan ayağı kullanımlarının bu mekansal çekirdeğe dayandığını birlikte gösterir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"الأرض التي نحن عليها؛ كل ما سفل وقابل السماء؛ أسفل الشيء وقوائم الدابة وما يلي الأرض منها","what_is_not_ar":"ليس الزكام ولا الرعدة ولا الدودة ولا البساط"},"support_links":["sup_d17130fa1cecf805d0ab"]},{"boundary":"Toprağın niteliği çekirdektir; bitkinin gelişmesi ve oğlağın beslenmesi sonuç ya da ilişkili kullanım olarak kalmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000025/B002","candidate_links":[{"candidate_id":"cand_3084439aee38e29309b3","lane":"micro"},{"candidate_id":"cand_53710bdd9cdb1fc279bf","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:2:2","qac_word_ref":"99:2:2","surface_ar":"أَرْضُ"}],"gloss":"yumuşak ve verimli toprak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Toprak veya çayırlık yumuşak, verimli ve iyi bitki yetiştirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bitki toprağa iyice yerleşir, çoğalır veya biçilecek olgunluğa ulaşır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Oğlak yer bitkisini yer."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir kaynakta ilgili niteleme semiz oğlağı belirtir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın toprak niteliğine dayanan çekirdeğini eksiksiz ve doğal biçimde karşılar.","boundary_detail":"Toprağın niteliği çekirdektir; bitkinin gelişmesi ve oğlağın beslenmesi sonuç ya da ilişkili kullanım olarak kalmalıdır.","branch_image_ar":"الأرض اللينة المنبتة","concept_gloss":"yumuşak ve verimli toprak","contextual_glosses":[{"applicability":"Bitkinin toprağa yerleşerek çoğalması anlatılan bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Toprağın genel niteliğini ve oğlağın bu bitkiyle beslenmesi yüzünü dışarıda bırakır.","preserves":"Bitkinin toprağa yerleşmesi ve gelişerek çoğalması sürecini korur."},"facet_ids":["F002"],"text":"iyice köklenip çoğalmak","usage_role":"contextual"}],"definition":"Belirtilen yapılarda yumuşak, iyi, verimli ve bol bitki yetiştiren toprağı anlatır. Buna bağlı yapılarda bitkinin toprağa iyice yerleşip çoğalması veya biçilebilir olması, köklü fidan ve yer bitkisini yiyen oğlak; ayrı bir kaynak kullanımında ise semiz oğlak ifade edilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Toprak veya çayırlık yumuşak, verimli ve iyi bitki yetiştirir."},{"facet_id":"F002","role":"extension","statement":"Bitki toprağa iyice yerleşir, çoğalır veya biçilecek olgunluğa ulaşır."},{"facet_id":"F003","role":"associated_use","statement":"Oğlak yer bitkisini yer."},{"facet_id":"F004","role":"source_variant","statement":"Bir kaynakta ilgili niteleme semiz oğlağı belirtir."}],"identity_rationale":"Kaynak ifadesi yumuşak, iyi ve verimli toprağı merkez alır; bitkinin köklenip çoğalması veya biçilecek duruma gelmesi ile oğlağın bu ottan yiyip semirmesi buna bağlı gelişmelerdir.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yumuşak, verimli ve bol bitkili toprak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yumuşak tabanlı geniş çayırlık"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"toprak verimlileşti"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bitki iyice köklendi, çoğaldı veya biçilecek duruma geldi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"toprakta kök salmış fidan"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"oğlak yer bitkisini yedi veya onunla semirdi"}],"lexicalization_note":"Tanım, nitelikli toprak anlamını yalnız kanıtlanan tamlamalara; bitki, fidan ve oğlakla ilgili anlamları da kendi kanıtlanmış yapılarına bağlar.","neighbor_coverage_note":"Bütün adaylar incelendi; verimli toprak çekirdeğine en yakın olup kapsam farkı taşıyan kart seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yumuşaklık ve iyi bitkilenmeyle birlikte belirli bitki ve oğlak yapılarını taşır; komşu dal kolaylık ve hızlı yetişme niteliğine uzanır.","focus_only":"Bitkinin yerleşmesi, biçilebilir olması ve oğlağın bitkiyle beslenmesi gibi bağlı kullanımları vardır.","gloss":"kolay işlenen verimli toprak","neighbor_only":"Kolay işlenen yer ve bitkinin hızlı yetişmesi özelliklerini daha genel biçimde kapsar.","neighbor_ref":"root_000058/B004","relation_type":"near_synonym","shared_zone":"İki dal da verimli, iyi bitki yetiştiren toprağı anlatır."}],"source_phrase_ar":"أرض أريضة لينة طيبة (maqayis;ayn)؛ أرض أريضة أي زكية (sihah)؛ حسنة النبت (mufradat)؛ تأرض النبت إذا أمكن أن يجز (maqayis;sihah)؛ تأرض النبت تمكن على الأرض فكثر (mufradat)؛ تأرض الجدي إذا تناول نبت الأرض (mufradat)؛ جدي أريض أي سمين (sihah)","source_summary":"Birleşik kanıt, verimli ve yumuşak toprağı; bu toprakta gelişen bitkiyi ve bitkiden yararlanan oğlağı aynı üretkenlik ilişkisi içinde toplar.","sources":["MQ","AY","SI","MU"],"what_is_ar":"الأرض الأريضة والروضة الأريضة؛ الأرض الزاكية الحسنة النبت؛ النبات المتأرض إذا تمكن في الأرض وكثر أو أمكن جزه؛ الجدي الأريض إذا تناول نبت الأرض أو سمن","what_is_not_ar":"ليس أسفل الشيء مطلقا ولا الرعدة ولا الزكام"},"support_links":["sup_82bbad2e93d869d8e71f","sup_8b6e75f36708cb4fb7a9"]},{"boundary":"Anlam yalnız verilen kişi ve eylem yapılarında geçerlidir; genel bir kök anlamı veya doğrudan ahlaki iyilik adı değildir.","branch_kind":"collocation","branch_ref":"root_000025/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:2:2","qac_word_ref":"99:2:2","surface_ar":"أَرْضُ"}],"gloss":"iyiliğe yatkın ve layık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi iyiliğe yatkın ve ona layıktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karşılaştırmalı yapıda kişi, belirli bir işi yapmaya grubun en uygun üyesidir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kaynak bu kişi niteliğini alçak gönüllülükle birlikte verir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kişi hakkında kurulan belirtilmiş yapıda dalın temel niteliğini karşılar.","boundary_detail":"Anlam yalnız verilen kişi ve eylem yapılarında geçerlidir; genel bir kök anlamı veya doğrudan ahlaki iyilik adı değildir.","branch_image_ar":"الخليق بالخير كالأرض الأريضة","concept_gloss":"iyiliğe yatkın ve layık","contextual_glosses":[{"applicability":"Bir topluluk içinden belirli işi yapmaya en uygun kişi seçildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İyiliğe yatkın ve alçak gönüllü kişi niteliğini dışarıda bırakır.","preserves":"Belirli eyleme başkalarından daha uygun ve layık olma karşılaştırmasını korur."},"facet_ids":["F002"],"text":"bunu yapmaya en uygunları","usage_role":"contextual"}],"definition":"Belirli yapılarda bir kişinin iyiliğe yatkın ve ona layık olmasını anlatır; bir kaynak bu niteliği alçak gönüllülükle birlikte verir. Karşılaştırmalı kullanımda ise bir işi yapmaya başkalarından daha uygun olmayı bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi iyiliğe yatkın ve ona layıktır."},{"facet_id":"F002","role":"specialization","statement":"Karşılaştırmalı yapıda kişi, belirli bir işi yapmaya grubun en uygun üyesidir."},{"facet_id":"F003","role":"source_variant","statement":"Bir kaynak bu kişi niteliğini alçak gönüllülükle birlikte verir."}],"identity_rationale":"Kaynak ifadesi belirli yapılarda bir kişinin iyiliğe yatkın, ona layık ve alçak gönüllü oluşunu; karşılaştırmalı yapıda ise bir işi yapmaya en uygun kişi sayılmasını bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"iyiliğe yatkın, layık ve alçak gönüllü kişi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bunu yapmaya en uygunları"}],"lexicalization_note":"Tanım bütünüyle belirtilen kişi ve eylem tamlamalarına bağlıdır; yalın biçime bağımsız bir uygunluk anlamı yüklenmez.","neighbor_coverage_note":"Tüm komşular değerlendirildi; genel layıklık alanıyla karışma olasılığı en yüksek olan karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal iyilik alanına ve iki belirli yapıya bağlıdır; komşu dalın uygunluk ve hazır oluş kapsamı daha geneldir.","focus_only":"İyiliğe yatkınlıkla birlikte alçak gönüllülük çağrışımı ve belirli kalıplara bağlılık taşır.","gloss":"bir şeye layık ve hazır","neighbor_only":"Herhangi bir şeye hazır, uygun veya layık olmayı daha geniş biçimde anlatır.","neighbor_ref":"root_000434/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişi ile uygun görüldüğü nitelik veya eylem arasındaki yatkınlık ilişkisini bildirir."}],"source_phrase_ar":"رجل أريض للخير أي خليق له شبه بالأرض الأريضة (maqayis)؛ رجل أريض أي متواضع خليق للخير (sihah)؛ هو آرضهم أن يفعل ذلك أي أخلقهم (sihah)","source_summary":"Kaynaklar, iyiliğe yatkınlık ve layıklık ile belirli bir eyleme en uygun olma yargısını yapı bağımlı tek bir uygunluk alanında birleştirir.","sources":["MQ","SI"],"what_is_ar":"الرجل الأريض للخير؛ آرض القوم أن يفعل الشيء أي أخلقهم به","what_is_not_ar":"ليس الأرض الحسية ولا الزكام ولا الرعدة"},"support_links":[]},{"boundary":"Bu anlam yalnız sabit adlandırmaya aittir ve genel olarak yeryüzünde yaşayan kişiyi anlatmaz.","branch_kind":"non_bare","branch_ref":"root_000025/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:2:2","qac_word_ref":"99:2:2","surface_ar":"أَرْضُ"}],"gloss":"yabancı kimse","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sabit söz birimi, bir yerde yabancı olan kimseyi adlandırır."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kanıtlanan sabit adlandırmanın kişi anlamını doğal biçimde karşılar.","boundary_detail":"Bu anlam yalnız sabit adlandırmaya aittir ve genel olarak yeryüzünde yaşayan kişiyi anlatmaz.","branch_image_ar":"ابن الأرض الغريب","concept_gloss":"yabancı kimse","definition":"Belirli bir sabit adlandırmada, bulunduğu çevreye dışarıdan gelen veya oraya ait olmayan yabancı kimseyi belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sabit söz birimi, bir yerde yabancı olan kimseyi adlandırır."}],"identity_rationale":"Tek kaynak ifadesi, sabit bir adlandırmanın doğrudan yabancı kimse anlamına geldiğini belirtir; yer sakini veya soy bağına ilişkin daha ayrıntılı bir koşul kurmaz.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yabancı kimse"}],"lexicalization_note":"Tanım yalnız kanıtlanan sabit söz birimine bağlanır; parçaların yalın anlamlarından yeni bir kişi sınıfı türetilmez.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi; genel yabancı anlamına en yakın, fakat topluluk koşuluyla ayrılan komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kanıtı yalnız yabancı olmayı söyler; komşu dal yabancının başka bir topluluk içinde bulunması koşulunu açıkça taşır.","focus_only":"Yabancılığı herhangi bir ek topluluk koşulu vermeden sabit bir adlandırmayla bildirir.","gloss":"başka bir topluluğa girmiş yabancı","neighbor_only":"Kişinin kendisinden olmayan bir topluluğun içine girmiş bulunmasını özellikle belirtir.","neighbor_ref":"root_000009/B006","relation_type":"near_synonym","shared_zone":"İki dal da bulunduğu insan çevresine aslen ait olmayan kişiyi anlatır."}],"source_phrase_ar":"فلان ابن أرض أي غريب (maqayis)","source_summary":"Tek kanıt, söz biriminin yabancı kimseyi belirten kısıtlı ve kalıplaşmış bir adlandırma olduğunu gösterir.","sources":["MQ"],"what_is_ar":"ابن أرض إذا أريد الغريب","what_is_not_ar":"ليس ساكن الأرض مطلقا ولا الأرض التي نحن عليها"},"support_links":[]},{"boundary":"Bu dal genel yer, hasır, döşek veya süslü kumaş değil; malzemesi ve kalınlığı belirtilmiş bir yaygıdır.","branch_kind":"bare","branch_ref":"root_000025/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:2:2","qac_word_ref":"99:2:2","surface_ar":"أَرْضُ"}],"gloss":"kalın yün veya kıl yaygı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne, yün ya da hayvan kılından yapılmış kalın bir yaygıdır."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesnenin türünü, belirleyici kalınlığını ve iki olası malzemesini birlikte karşılar.","boundary_detail":"Bu dal genel yer, hasır, döşek veya süslü kumaş değil; malzemesi ve kalınlığı belirtilmiş bir yaygıdır.","branch_image_ar":"الإراض البساط الضخم","concept_gloss":"kalın yün veya kıl yaygı","definition":"Yünden veya hayvan kılından yapılmış kalın ve büyükçe bir yaygıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne, yün ya da hayvan kılından yapılmış kalın bir yaygıdır."}],"identity_rationale":"Kaynak ifadesi nesneyi kalın, büyükçe bir yaygı olarak tanımlar ve malzemesini yün ya da hayvan kılıyla sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kalın yün veya kıl yaygı"}],"lexicalization_note":"Tanım yalın adın kanıtlanan nesne anlamıyla sınırlıdır ve komşu döşeme türlerinin özelliklerini içeri almaz.","neighbor_coverage_note":"Sağlanan kartların tümü değerlendirildi; nesne türü bakımından en yakın fakat kapsamı daha geniş döşeme komşusu yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal malzeme ve kalınlıkla tanımlanan belirli bir yaygıdır; komşu dal işlevi bakımından daha geniş bir döşeme sınıfıdır.","focus_only":"Yaygının kalın ve özellikle yün ya da hayvan kılından yapılmış olmasını gerektirir.","gloss":"döşek veya alta serilen örtü","neighbor_only":"Döşek, yatak örtüsü ve genel olarak alta serilen nesneleri kapsar.","neighbor_ref":"root_001397/B007","relation_type":"same_field","shared_zone":"Her iki dal da zemine ya da yatma yerine serilen ev eşyalarını adlandırır."}],"source_phrase_ar":"الإراض بساط ضخم من وبر أو صوف (maqayis)؛ الإراض بالكسر بساط ضخم من صوف أو وبر (sihah)","source_summary":"Kaynaklar nesnenin yaygı oluşunda, kalınlığında ve yün ya da hayvan kılından yapılmasında birleşir.","sources":["MQ","SI"],"what_is_ar":"الإراض بالكسر؛ بساط ضخم من وبر أو صوف","what_is_not_ar":"ليس الأرض ولا الأرضة ولا الأريضة"},"support_links":[]},{"boundary":"Dal, yere yönelen ağırlık ve kalma durumudur; tembellik, geri kayma veya bir başkasına karşı çıkma değildir.","branch_kind":"bare","branch_ref":"root_000025/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:2:2","qac_word_ref":"99:2:2","surface_ar":"أَرْضُ"}],"gloss":"yere çökercesine ağırlaşıp oyalanmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi yerden ayrılmayarak yere bağlı kalır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yere doğru ağırlaşma, oyalanma ve gecikme olarak gerçekleşebilir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yere bağlılık, ağırlaşma ve gecikme bileşenlerini tek bir eylem karşılığında toplar.","boundary_detail":"Dal, yere yönelen ağırlık ve kalma durumudur; tembellik, geri kayma veya bir başkasına karşı çıkma değildir.","branch_image_ar":"لزوم الأرض والتثاقل إليها","concept_gloss":"yere çökercesine ağırlaşıp oyalanmak","contextual_glosses":[{"applicability":"Kişinin doğrudan yere bağlı kalması öne çıktığında kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yere doğru ağırlaşma ile oyalanıp gecikme görünüşlerini dışarıda bırakır.","preserves":"Yere bağlı kalma ve bulunduğu noktadan ayrılmama durumunu korur."},"facet_ids":["F001"],"text":"yerinden ayrılmamak","usage_role":"contextual"}],"definition":"Kişinin yere bağlı kalmasını veya yere çökercesine ağırlaşmasını ve bu yüzden bir süre oyalanıp gecikmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi yerden ayrılmayarak yere bağlı kalır."},{"facet_id":"F002","role":"extension","statement":"Yere doğru ağırlaşma, oyalanma ve gecikme olarak gerçekleşebilir."}],"identity_rationale":"Kaynak ifadesi kişinin yere bağlı kalmasını, yere doğru ağırlaşmasını ve bunun sonucu oyalanıp gecikmesini aynı hareket durumu içinde verir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yere bağlı kalmak, ağırlaşıp oyalanmak"}],"lexicalization_note":"Tanım yalın eylem dalının yere bağlı kalma, ağırlaşma ve gecikme bileşenleriyle sınırlıdır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yere bağlı kalma çekirdeğini en doğrudan paylaşan ve kapsam farkını gösteren komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişinin yere doğru ağırlaşıp gecikmesini anlatır; komşu dal farklı canlı ve nesnelerde yere yapışma ya da sabit kalma alanına daha geniş yayılır.","focus_only":"İnsan için yere doğru ağırlaşma ve bununla birlikte oyalanma anlamını taşır.","gloss":"yere yapışıp yerinde kalmak","neighbor_only":"İnsan dışında kuş ve yırtıcıları, ayrıca yuva ve yerinde ağır duran nesne örneklerini de kapsar.","neighbor_ref":"root_000222/B001","relation_type":"near_synonym","shared_zone":"İki dalda da yere yakın durma ve bulunulan yerden ayrılmama durumu vardır."}],"source_phrase_ar":"تأرض فلان إذا لزم الأرض (maqayis)؛ فقام عجلان وما تأرضا أي ما تلبث (sihah)؛ التأرض أيضا التثاقل إلى الأرض (sihah)","source_summary":"Kanıt, yere bağlı kalmayı çekirdek alır ve yere doğru ağırlaşma ile oyalanmayı bu durumun görünüşleri olarak birleştirir.","sources":["MQ","SI"],"what_is_ar":"تأرض فلان إذا لزم الأرض؛ التأرض بمعنى التثاقل والتلبث إلى الأرض","what_is_not_ar":"ليس التصدي والتعرض للغير ولا النبات المتأرض"},"support_links":[]},{"boundary":"Bu dal bir başkasına yönelmiş karşı duruşu anlatır; yere çökme, ağırlaşma veya yalnızca yüz yüze bulunma değildir.","branch_kind":"bare","branch_ref":"root_000025/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:2:2","qac_word_ref":"99:2:2","surface_ar":"أَرْضُ"}],"gloss":"karşısına çıkıp kendini ortaya koymak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir başkasına yönelir, karşısına çıkar ve kendini ona karşı ortaya koyar."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiye yönelmiş karşı duruşu ve görünür biçimde ortaya çıkmayı birlikte karşılar.","boundary_detail":"Bu dal bir başkasına yönelmiş karşı duruşu anlatır; yere çökme, ağırlaşma veya yalnızca yüz yüze bulunma değildir.","branch_image_ar":"التعرض والتصدي","concept_gloss":"karşısına çıkıp kendini ortaya koymak","definition":"Birine doğru yönelip onun karşısına çıkmayı, kendini ortaya koyarak ona karşı durmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir başkasına yönelir, karşısına çıkar ve kendini ona karşı ortaya koyar."}],"identity_rationale":"Tek kaynak ifadesi eylemi, birine doğru çıkıp onun karşısında kendini ortaya koymak ve ona karşı durmak biçiminde açıklar.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"birinin karşısına çıkıp kendini ortaya koymak"}],"lexicalization_note":"Tanım yalın eylem dalını, bir hedefe yönelme ve karşısına çıkma koşullarıyla sınırlar.","neighbor_coverage_note":"Tüm komşular değerlendirildi; yönelme ve karşıya çıkma çekirdeğini en yakından paylaşan aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişiler arası karşıya çıkışı öne çıkarır; komşu dal bakma, gözetme ve genel yüzünü dönme kullanımlarını da kapsar.","focus_only":"Bir kişiye doğru gelerek onun karşısında kendini ortaya koyma hareketini bildirir.","gloss":"bir şeye yönelip karşısına çıkmak","neighbor_only":"Bir şeye bakmak üzere yükselme, onu gözetme veya yalnızca yüzünü ona çevirme kapsamına uzanır.","neighbor_ref":"root_000853/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da bir hedefe yönelme ve onun karşısında konum alma anlamını taşır."}],"source_phrase_ar":"جاء فلان يتأرض إلي أي يتصدى ويتعرض (sihah)","source_summary":"Tek kanıt, eylemin hedefe yönelmiş bir karşıya çıkma ve kendini ortaya koyma hareketi olduğunu gösterir.","sources":["SI"],"what_is_ar":"جاء فلان يتأرض إلى غيره أي يتصدى ويتعرض له","what_is_not_ar":"ليس التثاقل إلى الأرض ولا لزومها"},"support_links":[]},{"boundary":"Dal genel şiddetli sarsıntı veya belirli bir ateş nöbeti değil, insanda görülen titreme durumudur.","branch_kind":"bare","branch_ref":"root_000025/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:2:2","qac_word_ref":"99:2:2","surface_ar":"أَرْضُ"}],"gloss":"titreme veya ürperme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan bedenini tutan bir titreme veya ürperme meydana gelir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan bedenindeki kısa ya da süren sarsıntı durumunu doğrudan karşılar.","boundary_detail":"Dal genel şiddetli sarsıntı veya belirli bir ateş nöbeti değil, insanda görülen titreme durumudur.","branch_image_ar":"الأَرْض الرعدة","concept_gloss":"titreme veya ürperme","definition":"Bir insanın bedeninde beliren titreme, sarsılma veya ürperme durumudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan bedenini tutan bir titreme veya ürperme meydana gelir."}],"identity_rationale":"Kaynak ifadesi bu dalı insanda görülen titreme, sarsılma veya ürperme olarak açıkça tanımlar ve yer ya da hastalık anlamlarından ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"insanı tutan titreme veya ürperme"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"titreme ve sarsılma"}],"lexicalization_note":"Tanım yalın biçimlerin insandaki titreme ve ürperme anlamıyla sınırlıdır; komşu hastalık nedenleri eklenmez.","neighbor_coverage_note":"Sağlanan bütün kartlar incelendi; genel titreme çekirdeğine en yakın ve kapsam farkı belirgin olan komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalın bir insan titremesidir; komşu dal nedeni ve öznesi bakımından daha geniştir, ayrıca korkaklık ve gevşeklik nitelemelerine uzanır.","focus_only":"İnsan bedenindeki titreme durumunu herhangi bir özel neden belirtmeden adlandırır.","gloss":"korku veya hastalıktan sarsılma","neighbor_only":"Korku, hastalık veya gevşeklik nedeniyle insan ya da başka bir şeyin sarsılmasını ve kişilik nitelemelerini kapsar.","neighbor_ref":"root_000573/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da insan bedenindeki titreme ve sarsılma alanında örtüşür."}],"source_phrase_ar":"الأرض الرعدة (maqayis;ayn)؛ بفلان أرض أي رعدة (maqayis)؛ الأرْص النفضة والرعدة (sihah)","source_summary":"Kaynaklar bu adın insanda görülen titreme ve ürperme durumunu bildirdiğinde birleşir.","sources":["MQ","AY","SI"],"what_is_ar":"الأَرْض بمعنى الرعدة أو النفضة في الإنسان","what_is_not_ar":"ليس الأرض التي تقابل السماء ولا الزكام"},"support_links":[]},{"boundary":"Dal solunumla ilgili başka hastalıkları veya genel beden titremesini değil, soğuk algınlığı durumunu ve ilgili türevleri kapsar.","branch_kind":"bare","branch_ref":"root_000025/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:2:2","qac_word_ref":"99:2:2","surface_ar":"أَرْضُ"}],"gloss":"soğuk algınlığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Soğuk algınlığı durumudur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Türemiş biçim, soğuk algınlığına yakalanmış kişiyi niteler."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen biçim, birini soğuk algınlığına uğratmayı bildirir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hastalık çekirdeğini Türkçede en doğal ve ayırt edici biçimde karşılar.","boundary_detail":"Dal solunumla ilgili başka hastalıkları veya genel beden titremesini değil, soğuk algınlığı durumunu ve ilgili türevleri kapsar.","branch_image_ar":"الأَرْض الزكام","concept_gloss":"soğuk algınlığı","contextual_glosses":[{"applicability":"Hastalığın kendisi değil, bu hastalığa tutulmuş kişi nitelendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hastalık adını ve birini hastalığa uğratma eylemini bağımsız olarak karşılamaz.","preserves":"Soğuk algınlığı ile kişi arasındaki etkilenme ilişkisini korur."},"facet_ids":["F002"],"text":"soğuk algınlığına yakalanmış","usage_role":"contextual"}],"definition":"Soğuk algınlığı hastalığını, bu hastalığa yakalanmış kişiyi ve birini bu hastalığa uğratma eylemini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Soğuk algınlığı durumudur."},{"facet_id":"F002","role":"specialization","statement":"Türemiş biçim, soğuk algınlığına yakalanmış kişiyi niteler."},{"facet_id":"F003","role":"associated_use","statement":"Ettirgen biçim, birini soğuk algınlığına uğratmayı bildirir."}],"identity_rationale":"Kaynak ifadesi hastalığı soğuk algınlığı olarak, etkilenen kişiyi bu hastalığa yakalanmış olarak ve ettirgen biçimi hastalığa uğratmak olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"soğuk algınlığı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"soğuk algınlığına yakalanmış"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"soğuk algınlığına uğratmak"}],"lexicalization_note":"Tanım yalın hastalık adını ve aynı dalda kanıtlanan hasta kişi ile hastalığa uğratma türevlerini korur.","neighbor_coverage_note":"Bütün komşu kartları değerlendirildi; aynı hastalık ve hasta kişi alanını en doğrudan paylaşan aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın türetim dizisinde hastalığa uğratma da vardır; komşu dalın kanıtı ise bir kaynakta daha genel hastalık yorumu içerir.","focus_only":"Hastalık adı, hastaya ilişkin niteleme ve hastalığa uğratma eylemini birlikte kapsar.","gloss":"soğuk algınlığı ve hasta olma","neighbor_only":"Soğuk algınlığı yanında daha genel bir hastalık alanına açılan ayrı bir kaynak yorumunu da taşır.","neighbor_ref":"root_000916/B003","relation_type":"near_synonym","shared_zone":"Her iki dal soğuk algınlığını ve bu hastalığa yakalanmış kişiyi ifade eder."}],"source_phrase_ar":"الأرض الزكمة رجل مأروض أي مزكوم (maqayis)؛ الأرض الزكام وأرض فهو مأروض (ayn)؛ الأرض الزكام وقد آرضه الله إيراضا أي أزكمه فهو مأروض (sihah)","source_summary":"Kaynaklar hastalık adı ile hasta kişi nitelemesinde birleşir; kanıt ayrıca hastalığa uğratma eylemini aynı türetim alanında gösterir.","sources":["MQ","AY","SI"],"what_is_ar":"الأَرْض بمعنى الزكمة أو الزكام؛ مأروض لمن أصابه الزكام","what_is_not_ar":"ليس الرعدة ولا الأرض الحسية"},"support_links":[]},{"boundary":"Canlının kendisi çekirdektir; odunun yenmiş duruma gelmesi yalnız belirtilen eylem yapısına bağlı sonuçtur.","branch_kind":"mixed_non_bare","branch_ref":"root_000025/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:2:2","qac_word_ref":"99:2:2","surface_ar":"أَرْضُ"}],"gloss":"odun yiyen küçük canlı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Küçük canlı odunla beslenir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Canlı odunu yiyerek onu aşınmış ve zarar görmüş hale getirir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kaynak canlıyı beyaz ve karıncaya benzer olarak niteler."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Canlıyı kanıtlanan boyutu ve onu ayırt eden beslenme davranışıyla kısa ve doğal biçimde karşılar.","boundary_detail":"Canlının kendisi çekirdektir; odunun yenmiş duruma gelmesi yalnız belirtilen eylem yapısına bağlı sonuçtur.","branch_image_ar":"الأَرَضَة آكلة الخشب","concept_gloss":"odun yiyen küçük canlı","contextual_glosses":[{"applicability":"Bir odunun bu canlı tarafından yenerek zarar görmüş olduğu bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Canlının beyaz ve karıncaya benzer oluşunu bağımsız bir tanım olarak vermez.","preserves":"Odunun canlı tarafından yenmiş ve zarar görmüş olma sonucunu korur."},"facet_ids":["F002"],"text":"odun yiyen küçük canlı tarafından yenmiş","usage_role":"contextual"}],"definition":"Odun yiyen küçük bir canlıyı belirtir. İlgili eylem yapısı, bu canlının bir odunu yiyip zarar görmüş hale getirmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Küçük canlı odunla beslenir."},{"facet_id":"F002","role":"associated_use","statement":"Canlı odunu yiyerek onu aşınmış ve zarar görmüş hale getirir."},{"facet_id":"F003","role":"source_variant","statement":"Bir kaynak canlıyı beyaz ve karıncaya benzer olarak niteler."}],"identity_rationale":"Kaynak ifadesi beyaz, karıncaya benzeyen ve odun yiyen küçük canlıyı tanımlar; ayrıca bu canlının odunu yiyerek onu zarar görmüş hale getirmesini verir.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"odun yiyen küçük canlı"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"odunu bu canlı yedi ve zarar verdi"}],"lexicalization_note":"Tanım canlı adını yalın çekirdek olarak verir ve odunun yenmesini yalnız kanıtlanan tamlamaya bağlı sonuç yüzü olarak ayırır.","neighbor_coverage_note":"Tüm aday kartlar değerlendirildi; odun yiyen canlı çekirdeğine en yakın fakat canlı ve nesne kapsamı farklı olan komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal odun yiyen küçük canlı ve onun oduna etkisidir; komşu dal ağaç, yaprak ve gövde üzerinde beslenen başka bir canlıya özgüdür.","focus_only":"Odun yiyen küçük canlıyı ve bu canlının yediği odunun sonucunu belirtir.","gloss":"ağacı delen ve yiyen küçük canlı","neighbor_only":"Özellikle ağaçta delik açan, yaprak veya odun yiyen başka bir küçük canlıyı ve ağacın uğradığı durumu kapsar.","neighbor_ref":"root_000699/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da odunsu bitki maddesini yiyerek zarar veren küçük canlıları anlatır."}],"source_phrase_ar":"الأرضة دويبة بيضاء تشبه النمل تأكل الخشب (ayn)؛ الأرضة بالتحريك دويبة تأكل الخشب (sihah)؛ أرضت الخشبة تؤرض أرضا فهي مأروضة إذا أكلتها (sihah)؛ الأرضة الدودة التي تقع في الخشب من الأرض (mufradat)؛ أرضت الخشبة فهي مأروضة (mufradat)","source_summary":"Kaynaklar odun yiyen küçük canlı ile onun odunda oluşturduğu yenme ve zarar görme sonucunu aynı anlam alanında birleştirir.","sources":["AY","SI","MU"],"what_is_ar":"الأَرَضَة؛ دويبة تأكل الخشب؛ أرضت الخشبة فهي مأروضة إذا أكلتها الأرضة","what_is_not_ar":"ليس الأرض ولا الأرض الأريضة ولا الزكام"},"support_links":[]},{"boundary":"Anlam yalnız yara ile kurulan yapıda geçerlidir ve irinlenmenin yol açtığı bozulmayı zorunlu olarak içerir.","branch_kind":"collocation","branch_ref":"root_000025/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:2:2","qac_word_ref":"99:2:2","surface_ar":"أَرْضُ"}],"gloss":"yaranın irinlenip bozulması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yara irin toplayarak kabarır ve irinlenme sonucunda bozulur."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız yara bağlamında irin toplama ile ortaya çıkan bozulma sürecini eksiksiz karşılar.","boundary_detail":"Anlam yalnız yara ile kurulan yapıda geçerlidir ve irinlenmenin yol açtığı bozulmayı zorunlu olarak içerir.","branch_image_ar":"فساد القرحة بالمدة","concept_gloss":"yaranın irinlenip bozulması","definition":"Bir yaranın irin toplaması, kabarıp su toplaması ve bu irinlenme yüzünden bozulmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yara irin toplayarak kabarır ve irinlenme sonucunda bozulur."}],"identity_rationale":"Tek kaynak ifadesi, yaranın irin toplamasıyla kabarıp bozulmasını bir süreç olarak verir; yalnız irin maddesini veya genel deri şişliğini adlandırmaz.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yara irinlenip kabardı ve bozuldu"}],"lexicalization_note":"Tanım yalnız yara öznesiyle kurulan kanıtlanmış tamlamaya bağlıdır; yalın biçime genel bozulma anlamı verilmez.","neighbor_coverage_note":"Bütün komşular incelendi; irin birikmesi çekirdeğini en yakından paylaşan ve sonuç bakımından ayrılan kart yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal irin birikimini yaranın kabarıp bozulmasına bağlar; komşu dal yalnız irin toplanması ya da dışarı çıkmasıyla yetinebilir.","focus_only":"Yaranın irinlenmeyle kabarıp bozulması sürecini zorunlu olarak içerir.","gloss":"yarada irin toplanması","neighbor_only":"İrinin yarada toplanmasını veya yaradan çıkmasını, bozulma sonucu aramadan kapsar.","neighbor_ref":"root_001664/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da yaranın içinde irin birikmesi durumunu anlatır."}],"source_phrase_ar":"أرضت القرحة تأرض أرضا أي مجلت وفسدت بالمدة (sihah)","source_summary":"Tek kanıt, yara içindeki irinlenme ile kabarma ve bozulmayı birbirine bağlı tek bir hastalık süreci olarak gösterir.","sources":["SI"],"what_is_ar":"أرضت القرحة إذا مجلت وفسدت بالمدة","what_is_not_ar":"ليس الزكام ولا الأرضة ولا الرعدة"},"support_links":[]},{"boundary":"Dal yalnız akıl karışıklığı değildir; doğaüstü nedene bağlanma ve istemsiz baş-gövde hareketi birlikte korunmalıdır.","branch_kind":"bare","branch_ref":"root_000025/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:2:2","qac_word_ref":"99:2:2","surface_ar":"أَرْضُ"}],"gloss":"doğaüstü etkiye bağlanan istemsiz sarsıntılı akıl bozukluğu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin akıl ve beden durumu görünmez varlıkların etkisine bağlanır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Etkilenen kişi başını ve gövdesini bilinçli bir amaç olmadan hareket ettirir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Neden yorumunu, akıl durumunu ve belirleyici istemsiz beden hareketini birlikte açıklar.","boundary_detail":"Dal yalnız akıl karışıklığı değildir; doğaüstü nedene bağlanma ve istemsiz baş-gövde hareketi birlikte korunmalıdır.","branch_image_ar":"المأروض المخبول من أهل الأرض","concept_gloss":"doğaüstü etkiye bağlanan istemsiz sarsıntılı akıl bozukluğu","contextual_glosses":[{"applicability":"Kişinin gözlenebilir beden hareketi ön plana çıkarıldığında açıklayıcı karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Akıl bozukluğunu ve durumun görünmez varlıkların etkisine bağlanmasını dışarıda bırakır.","preserves":"Baş ve gövdenin bilinçli amaç olmadan hareket etmesi belirtisini korur."},"facet_ids":["F002"],"text":"başıyla gövdesini istemsizce sarsan kişi","usage_role":"explanatory"}],"definition":"Yerle ilişkilendirilen görünmez varlıkların etkisine bağlanan bir akıl ve beden bozukluğudur; etkilenen kişi başını ve gövdesini isteği dışında hareket ettirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin akıl ve beden durumu görünmez varlıkların etkisine bağlanır."},{"facet_id":"F002","role":"specialization","statement":"Etkilenen kişi başını ve gövdesini bilinçli bir amaç olmadan hareket ettirir."}],"identity_rationale":"Kaynak ifadesi, görünmez varlıkların etkisine bağlanan bir akıl ve beden bozukluğunu; kişinin başını ve gövdesini istemeden hareket ettirmesiyle birlikte tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"görünmez varlıkların etkisine bağlanan, başını ve gövdesini istemsizce hareket ettiren kişi"}],"lexicalization_note":"Tanım yalın kişi nitelemesinin doğaüstü açıklama, akıl bozukluğu ve istemsiz beden hareketi bileşenleriyle sınırlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; doğaüstü etkiye bağlanan akıl bozukluğu çekirdeğini en doğrudan paylaşan komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir kaynak ilişkilendirmesi ve istemsiz baş-gövde hareketi gerektirir; komşu dal daha genel bir doğaüstü dokunuş açıklamasıdır.","focus_only":"Yerle ilişkilendirilen görünmez varlıklar açıklamasını ve istemsiz baş-gövde hareketini birlikte taşır.","gloss":"doğaüstü dokunuşa bağlanan akıl karışıklığı","neighbor_only":"Doğaüstü bir dokunuşla açıklanan akıl karışıklığını beden hareketi koşulu olmadan daha genel verir.","neighbor_ref":"root_001423/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da akıl bozukluğunu görünmez bir varlığın etkisiyle açıklayan geleneksel anlayışta buluşur."}],"source_phrase_ar":"المأروض الذي به خبل من الجن وأهل الأرض وهو الذي يحرك رأسه وجسده على غير عمد (sihah)","source_summary":"Tek kanıt, doğaüstü varlıklara bağlanan akıl karışıklığını ve istemsiz baş-gövde hareketini aynı kişi durumunun ayrılmaz parçaları olarak verir.","sources":["SI"],"what_is_ar":"المأروض الذي به خبل من الجن وأهل الأرض ويحرك رأسه وجسده على غير عمد","what_is_not_ar":"ليس المزكوم المأروض ولا الخشبة المأروضة"},"support_links":[]},{"boundary":"Bu dal çıplak ağırlık karşıtlığını anlatır; taşınan eşya, günah yükü ve ölçü adı ayrı dallardır.","branch_kind":"bare","branch_ref":"root_000202/B001","candidate_links":[{"candidate_id":"cand_fd4bbfaa69ddab402681","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ثَّقَلَان","morph_features":"STEM|POS:N|LEM:v~aqalaAn|ROOT:vql|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:3:1","qac_word_ref":"99:2:3","surface_ar":"أَثْقَالَ"}],"gloss":"ağırlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, hafifliğin karşıtı olan ağırlık ve ağır gelmedir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Cisimlerdeki ağırlık çekirdeği, soyut durumlara ve değer yargılarına da taşınabilir."}}],"root_ar":"ث ق ل","root_id":"root_000202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çıplak dalın maddi veya soyut hafiflik karşıtı çekirdeğini doğal biçimde verir.","boundary_detail":"Bu dal çıplak ağırlık karşıtlığını anlatır; taşınan eşya, günah yükü ve ölçü adı ayrı dallardır.","branch_image_ar":"الثقل ضد الخفة","concept_gloss":"ağırlık","contextual_glosses":[{"applicability":"Bir şeyin tartıda, bedende veya değerlendirmede hafif sayılmayacak biçimde baskın geldiği bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Baskın gelme ve hafiflik karşıtlığını korur."},"facet_ids":["F001"],"text":"ağır gelme","usage_role":"contextual"},{"applicability":"Maddi ağırlık modelinin soyut değer, söz veya sorumluluk alanına taşındığı yerlerde açıklayıcıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Maddi cisimlerdeki temel ağırlık kullanımını dışarıda bırakır.","preserves":"Soyut alana taşınan ağırlık fikrini korur."},"facet_ids":["F002"],"text":"manevi ağırlık","usage_role":"explanatory"}],"definition":"Bir şeyin hafifliğe karşı ağır gelmesi, tartıda veya değerlendirmede baskın bir ağırlık taşımasıdır; önce cisimler için, sonra soyut nitelikler için kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, hafifliğin karşıtı olan ağırlık ve ağır gelmedir."},{"facet_id":"F002","role":"extension","statement":"Cisimlerdeki ağırlık çekirdeği, soyut durumlara ve değer yargılarına da taşınabilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Taşınan eşya veya yük nesnesi anlamı ekler.","collision":"Ayrı yük ve eşya dalıyla çakışır.","fit":"displacement","loses":"Hafifliğin genel karşıtı olan çıplak ağırlık çekirdeğini kaydırır.","preserves":"Ağırlıkla ilişkili taşınabilir nesne fikrini kısmen korur."},"text":"yük"}],"identity_rationale":"Kaynak ifadesi ağırlığı hafifliğin karşıtı olarak kurar; temel alan cisimlerdeki tartı veya baskın gelme duygusudur, sonra anlam alanlarına da taşınır. Geçici çerçeve bu çekirdeği yük, günah, ölçü birimi veya özel adlandırmalarla karıştırmadan verir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyin ağır gelmesi, hafif olmaması"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ağırlık, maddi ya da soyut ağır gelme niteliği"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"ağır, ağırlık taşıyan"}],"lexicalization_note":"Bare kapsam, tanımı çıplak ağırlık ve hafiflik karşıtlığıyla sınırlar; özel birleşim anlamları içeri alınmaz.","neighbor_coverage_note":"Komşular içinden ağırlık eksenini gerçekten keskinleştirenler yayımlandı; sertlik, doluluk veya soyut benzerlik taşıyan uzak adaylar sınırı belirginleştirmediği için dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal eksenin ağır tarafını, komşu dal ise hafif veya hafifletilmiş tarafını verir; bu yüzden aynı sahayı paylaşırlar ama yönleri karşıttır.","focus_only":"Odak dal, hafifliğe karşı ağır gelme ve baskın ağırlık alanıdır.","gloss":"ağırlık karşısında hafiflik","neighbor_only":"Komşu dal, hafiflik, yükün azalması veya ağırlaştırmanın kaldırılması alanıdır.","neighbor_ref":"root_000427/B001","relation_type":"polarity_pair","shared_zone":"İki dal aynı ağırlık ekseninde yer alır."},{"boundary_match":"partial","distinction":"Odak dal ağırlığın nitelik olarak kendisini anlatır; komşu dal bu niteliğin belirli ölçü, tartı aracı veya ağırlık miktarı olarak işlem görmesini anlatır.","focus_only":"Odak dal genel ağır gelme niteliğidir.","gloss":"ağırlık ile ölçü ağırlığı","neighbor_only":"Komşu dal ölçü, tartı birimi veya ağırlığı verme işlemiyle sınırlıdır.","neighbor_ref":"root_000202/B004","relation_type":"near_neighbor","shared_zone":"Her ikisi de ağırlığı tartı ve ölçme alanına bağlayabilir."},{"boundary_match":"partial","distinction":"Odak dal genel nitelik düzeyindedir; komşu dal bu niteliğin halsizlik, uyku baskısı, hastalık veya yavaş hareket olarak yaşanmasına bağlıdır.","focus_only":"Odak dal şeyin ağır olma niteliğini verir.","gloss":"ağırlık ile ağırlık hissi","neighbor_only":"Komşu dal bedende, uykuda, hastalıkta veya davranışta hissedilen ağırlık ve yavaşlamadır.","neighbor_ref":"root_000202/B006","relation_type":"near_neighbor","shared_zone":"Her ikisi de hafiflikten uzak ağırlaşma duygusuyla ilgilidir."}],"source_phrase_ar":"ضد الخفة (maqayis;sihah)؛ ثقل ثقلا فهو ثقيل والثقل رجحان الثقيل (ayn;tahdhib)؛ الثقل والخفة متقابلان وأصله في الأجسام ثم في المعاني (mufradat)","source_summary":"Kaynaklar bu dalda ağırlığı hafifliğin karşıtı ve ağır olanın baskın gelişi olarak toplar; maddi alanın asıl, soyut kullanımın genişletilmiş alan olduğunu bildirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"ثقل الشيء ورجحانه على ما يوزن أو يقدر به، في الأجسام ثم في المعاني","what_is_not_ar":"الأمتعة المحمولة؛ الأوزار؛ المثقال؛ الثقلان"},"support_links":["sup_d17130fa1cecf805d0ab"]},{"boundary":"Dal yük ve çıkarılan ağır nesnelerle sınırlıdır; ahlaki yük ve ölçü ağırlığı ayrı tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_000202/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ثَّقَلَان","morph_features":"STEM|POS:N|LEM:v~aqalaAn|ROOT:vql|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:3:1","qac_word_ref":"99:2:3","surface_ar":"أَثْقَالَ"}],"gloss":"ağır yükler","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel alan, taşınan eşya, yolcu yükü ve ağır yüktür."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yerin dışarı çıkardığı gömü, beden veya ölüler de ağır çıkarılanlar olarak aynı alana katılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli taşıma ifadesinde yükleri bir yere götürme işlemi anlatılır."}}],"root_ar":"ث ق ل","root_id":"root_000202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Taşınan eşya ve yerden çıkarılan ağır nesneleri birlikte kapsayan en kısa doğal karşılıktır.","boundary_detail":"Dal yük ve çıkarılan ağır nesnelerle sınırlıdır; ahlaki yük ve ölçü ağırlığı ayrı tutulur.","branch_image_ar":"الأثقال المحمولة والمخرجة","concept_gloss":"ağır yükler","contextual_glosses":[{"applicability":"Yolcu malı ve taşınır eşya bağlamlarında doğal Türkçe karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yerden çıkarılan gömü veya beden alanını dışarıda bırakır.","preserves":"Taşınan mal ve eşya alanını korur."},"facet_ids":["F001"],"text":"eşyalar","usage_role":"contextual"},{"applicability":"Taşıma fiiliyle gelen birleşimsel kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ağır yüklerin taşınması bağlamını korur."},"facet_ids":["F003"],"text":"yüklerinizi taşır","usage_role":"contextual"}],"definition":"Taşınan ağır eşya ve yükler ile yerin içinden çıkardığı gömü, beden veya ölü gibi ağır nesnelerdir; taşıma bağlamında yüklenip götürülen şeyler öne çıkar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel alan, taşınan eşya, yolcu yükü ve ağır yüktür."},{"facet_id":"F002","role":"extension","statement":"Yerin dışarı çıkardığı gömü, beden veya ölüler de ağır çıkarılanlar olarak aynı alana katılır."},{"facet_id":"F003","role":"associated_use","statement":"Belirli taşıma ifadesinde yükleri bir yere götürme işlemi anlatılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Ahlaki sorumluluk ve suç anlamı ekler.","collision":"Ayrı günah yükü dalıyla çakışır.","fit":"displacement","loses":"Taşınan eşya ve yerden çıkarılan nesne çekirdeğini kaybeder.","preserves":"Ağırlık yapan şey fikrini mecazi olarak korur."},"text":"günahlar"}],"identity_rationale":"Kaynak ifadesi hem yolcunun eşyası ve ağır yüklerini hem de yerin çıkardığı gömü, beden veya ölüleri aynı taşınan ya da çıkarılan ağırlık alanında toplar. Bu çerçeve günah yükü ve ölçü birimi anlamlarını dışarıda tutarak kullanılabilir.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yolcunun eşyası ve beraberindeki taşınır yük"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yükler, eşyalar veya yerin çıkardığı ağır şeyler"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yüklerinizi taşır"}],"lexicalization_note":"Mixed_non_bare kapsam, hem biçimsel çoğul kullanımları hem de belirli taşıma birleşimini ayırarak tanımlamayı gerektirir.","neighbor_coverage_note":"Taşıma, yer, gömme ve yük alanını paylaşan adaylar değerlendirildi; yol aşınması veya toprak yüzeyi gibi adaylar dalın nesne sınırını açıklamadığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal taşınan nesneyi anlatır; komşu dal o nesneyi taşıyan vasıta veya binek tarafında kalır.","focus_only":"Odak dal taşınan yük ve eşyadır.","gloss":"yük ile yük taşıyan binek","neighbor_only":"Komşu dal yük taşıyan binek veya taşıma aracı alanındadır.","neighbor_ref":"root_000970/B005","relation_type":"same_field","shared_zone":"İki dal taşıma ve yüklenme sahasını paylaşır."},{"boundary_match":"thematic_only","distinction":"Odak dal çıkma veya taşınma nesnesini verir; komşu dal gömme yeri ve yerleştirme işlemini verir.","focus_only":"Odak dal yerden çıkan veya taşınan ağır nesneleri kapsar.","gloss":"yerin çıkardığılar ile gömme","neighbor_only":"Komşu dal ölünün gömüldüğü yer ve gömme eylemidir.","neighbor_ref":"root_001195/B001","relation_type":"thematic","shared_zone":"İki dal ölü beden ve toprakla ilişkili sahnede karşılaşabilir."},{"boundary_match":"partial","distinction":"Odak dal ağırlığı taşınan nesne olarak somutlaştırır; komşu dal böyle bir eşya veya taşıma koşulu olmadan ağırlık niteliğini anlatır.","focus_only":"Odak dal taşınan maddi yük ve eşyalardır.","gloss":"yük ile ağırlık","neighbor_only":"Komşu dal hafifliğin karşıtı olan genel ağırlık niteliğidir.","neighbor_ref":"root_000202/B001","relation_type":"near_neighbor","shared_zone":"Her ikisi de ağır olma ve hafiflikten uzaklık fikrini paylaşır."}],"source_phrase_ar":"أثقال الأرض كنوزها وأجساد بني آدم (maqayis;sihah;mufradat)؛ متاع المسافر وحشمه وجمعه أثقال (ayn;sihah;tahdhib)؛ تحمل أثقالكم أي أحمالكم الثقيلة (mufradat)","source_summary":"Kaynaklar dalı yolcunun eşyası, yüklenen ağır mallar ve yerin dışarı çıkardığı saklı veya gömülü nesneler çevresinde toplar; taşıma örneği bu nesne alanının eylem bağlamıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الأمتعة والأحمال الثقيلة، وما في الأرض من كنوز أو أجساد أو موتى","what_is_not_ar":"الأوزار والآثام؛ المثقال؛ الثقلان؛ ثقل السمع"},"support_links":[]},{"boundary":"Dal ahlaki yük ve günah sorumluluğudur; maddi yük veya tartı anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000202/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ثَّقَلَان","morph_features":"STEM|POS:N|LEM:v~aqalaAn|ROOT:vql|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:3:1","qac_word_ref":"99:2:3","surface_ar":"أَثْقَالَ"}],"gloss":"günah yükü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Günah ve suçlar sahibine yüklenen ağır sorumluluklar gibi düşünülür."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ağırlaştırılmış kişi, günahlarının yükünü taşımaya çağıran kimse olarak betimlenir."}}],"root_ar":"ث ق ل","root_id":"root_000202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ahlaki sorumlulukların yük gibi ağırlaştırdığı bağlamları tam karşılar.","boundary_detail":"Dal ahlaki yük ve günah sorumluluğudur; maddi yük veya tartı anlamı değildir.","branch_image_ar":"الأوزار المثقلة","concept_gloss":"günah yükü","contextual_glosses":[{"applicability":"Çoğul ahlaki sorumluluk bağlamında doğal ve kısa çeviridir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yük gibi ağırlaştırma imgesini açıkça söylemez.","preserves":"Suç ve günah içeriğini korur."},"facet_ids":["F001"],"text":"günahları","usage_role":"contextual"},{"applicability":"Günahlarıyla ağırlaşmış kişinin betimlendiği yerde açıklayıcıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin günah yüküyle ağırlaşmasını korur."},"facet_ids":["F002"],"text":"yükü ağır olan kişi","usage_role":"explanatory"}],"definition":"Kişiyi yük gibi ağırlaştıran günahlar, suçlar ve sorumluluklardır; kişi bunları taşır ya da bunların ağırlığıyla yardım çağırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Günah ve suçlar sahibine yüklenen ağır sorumluluklar gibi düşünülür."},{"facet_id":"F002","role":"associated_use","statement":"Ağırlaştırılmış kişi, günahlarının yükünü taşımaya çağıran kimse olarak betimlenir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Maddi taşınır nesne anlamı ekler.","collision":"Ayrı maddi yük dalıyla çakışır.","fit":"displacement","loses":"Ahlaki günah ve sorumluluk içeriğini kaybeder.","preserves":"Yük fikrini korur."},"text":"eşyalar"}],"identity_rationale":"Kaynak ifadesi bu dalı günah, suç ve sorumlulukların kişiyi ağırlaştırması olarak verir. Çerçeve maddi eşya, gebelik veya ölçü alanını dışarıda bıraktığı sürece kaynağa uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kişiyi ağırlaştıran günahlar ve sorumluluklar"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"günah yüküyle ağırlaşmış kimse"}],"lexicalization_note":"Mixed_non_bare kapsam, çoğul yük biçimini ve ağırlaştırılmış kişi kullanımını ahlaki sorumluluk sınırında tutar.","neighbor_coverage_note":"Ahlaki yük, insan hali ve sorumluluk alanındaki adaylar gözden geçirildi; övgü, erkeklik veya genel huy gibi adaylar odak anlamla yalnızca uzak tematik bağ kurdu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ağırlık imgesini ahlaki sorumluluğa bağlar; komşu dal bu özel günah koşulu olmadan genel ağırlık niteliğini verir.","focus_only":"Odak dal günah ve sorumlulukların yük oluşudur.","gloss":"günah yükü ile ağırlık","neighbor_only":"Komşu dal hafifliğin karşıtı olan genel ağırlık niteliğidir.","neighbor_ref":"root_000202/B001","relation_type":"near_neighbor","shared_zone":"İki dal ağır gelme modelini paylaşır."},{"boundary_match":"partial","distinction":"Odak dal ahlaki sorumluluk eksenindedir; komşu dal bedensel veya davranışsal ağırlık ve yavaşlama eksenindedir.","focus_only":"Odak dal suç ve günah ağırlığıdır.","gloss":"günah yükü ile halsizlik","neighbor_only":"Komşu dal hastalık, uyku, yemek veya yavaşlık kaynaklı ağırlık halidir.","neighbor_ref":"root_000202/B006","relation_type":"near_neighbor","shared_zone":"Her ikisi de kişinin üzerinde ağırlık oluşmasını anlatır."},{"boundary_match":"field_only","distinction":"Odak dal yüklenen günaha odaklanır; komşu dal kişinin izlediği yol veya karakter haliyle ilgilidir.","focus_only":"Odak dal ahlaki yükün kendisidir.","gloss":"sorumluluk yükü ile gidişat","neighbor_only":"Komşu dal kişinin gidişatı, yolu veya hali anlamındaki yaşam biçimidir.","neighbor_ref":"root_000769/B002","relation_type":"same_field","shared_zone":"İki dal insan davranışı ve ahlaki durum alanında buluşabilir."}],"source_phrase_ar":"الأثقال الآثام (ayn)؛ حاملة أوزار وخطايا (ayn)؛ أوزارهم وأوزار من أضلوا وهي الآثام (tahdhib)؛ أثقالهم آثامهم التي تثقلهم وتثبطهم (mufradat)","source_summary":"Kaynaklar dalı günah, suç ve sapıtmanın kişiye yüklediği manevi ağırlık olarak açıklar; ağırlık burada maddi nesne değil, ahlaki sorumluluğun baskısıdır.","sources":["AY","TA","MU"],"what_is_ar":"الآثام والأوزار والخطايا التي تثقل صاحبها أو تدعى نفس مثقلة إلى حملها","what_is_not_ar":"الأمتعة الحسية؛ كنوز الأرض؛ الوزن بالمثقال؛ حمل المرأة"},"support_links":[]},{"boundary":"Dal tartı ve ölçü ağırlığıdır; genel ağırlık veya değer yüceliği değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000202/B004","candidate_links":[{"candidate_id":"cand_3084439aee38e29309b3","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ثَّقَلَان","morph_features":"STEM|POS:N|LEM:v~aqalaAn|ROOT:vql|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:3:1","qac_word_ref":"99:2:3","surface_ar":"أَثْقَالَ"}],"gloss":"ölçü ağırlığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel alan, bilinen ağırlık ölçüsü veya tartıda kullanılan ağırlıktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyin kendi ağırlık miktarı veya ona denk tartı karşılığı ifade edilebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ağırlığını vermek veya bir hayvanı tartmak, ölçme alanının eylem kullanımlarıdır."}}],"root_ar":"ث ق ل","root_id":"root_000202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tartı aracı, ağırlık birimi ve ölçülen miktar çekirdeğini birlikte karşılar.","boundary_detail":"Dal tartı ve ölçü ağırlığıdır; genel ağırlık veya değer yüceliği değildir.","branch_image_ar":"المثقال والوزن","concept_gloss":"ölçü ağırlığı","contextual_glosses":[{"applicability":"Bir şeyin denk ağırlık miktarının anlatıldığı bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Denk tartı miktarı fikrini korur."},"facet_ids":["F002"],"text":"ağırlığı kadar","usage_role":"contextual"},{"applicability":"Tartıda kullanılan ağırlık veya ölçü birimi bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölçme ve tartı aracını korur."},"facet_ids":["F001"],"text":"tartı ağırlığı","usage_role":"general"}],"definition":"Bilinen ağırlık ölçüsü, tartıda kullanılan ağırlık veya bir şeyin ölçülen ağırlık miktarıdır; ayrıca bir şeye ağırlığını vermek ya da tartarak ağır-hafif durumunu belirlemek bu alana girer.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel alan, bilinen ağırlık ölçüsü veya tartıda kullanılan ağırlıktır."},{"facet_id":"F002","role":"specialization","statement":"Bir şeyin kendi ağırlık miktarı veya ona denk tartı karşılığı ifade edilebilir."},{"facet_id":"F003","role":"associated_use","statement":"Ağırlığını vermek veya bir hayvanı tartmak, ölçme alanının eylem kullanımlarıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Saygınlık veya kıymet alanı ekler.","collision":"Ayrı değer ağırlığı dalıyla çakışır.","fit":"displacement","loses":"Ölçü, tartı ve nicelik belirleme çekirdeğini kaybeder.","preserves":"Ağırlığın önemle ilişkilendirilebilmesini kısmen korur."},"text":"değer"}],"identity_rationale":"Kaynak ifadesi belirli ağırlık ölçüsü, tartı aracı, bir şeyin ağırlık miktarı ve ağırlığını verme işlemini birlikte sunar. Çerçeve bu teknik ölçme alanını yük, günah ve değer ağırlığından ayırdığı için uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bilinen ağırlık ölçüsü veya tartı ağırlığı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bir şeyin ağırlığı kadar ölçü"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ona ağırlığını ver"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"hayvanı tartıp ağırlığını yokladı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ağırlığı eksik olmayan dinar"}],"lexicalization_note":"Mixed_non_bare kapsam, ölçü adını ve ölçme birleşimlerini aynı tartı sınırı içinde fakat ayrı işlevlerle açıklar.","neighbor_coverage_note":"Tartı, ölçü, eksiltme ve belirli ölçü adayları değerlendirildi; sayı artışı veya küçük mıkdara ilişkin uzak adaylar dal sınırını yeterince açıklamadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ağırlık birimi veya miktar üzerinde durur; komşu dal tartı aleti ve bunun adaletle ilişkili geniş kullanımını taşır.","focus_only":"Odak dal belirli ağırlık ölçüsü ve tartı miktarıdır.","gloss":"ölçü ağırlığı ile terazi","neighbor_only":"Komşu dal tartı aracını adalet, denge ve hesap sahasına da genişletir.","neighbor_ref":"root_001645/B002","relation_type":"near_synonym","shared_zone":"Her ikisi de tartı ve ölçme alanında kullanılabilir."},{"boundary_match":"field_only","distinction":"Odak dal ölçü ağırlığı türünü ve işlem alanını kapsar; komşu dal belli bir ölçü adında daha dar kalır.","focus_only":"Odak dal genel tartı ağırlığı ve ölçülen miktardır.","gloss":"ölçü ağırlığı ile belirli ölçü","neighbor_only":"Komşu dal belirli bir bilinen ağırlık adıdır.","neighbor_ref":"root_001677/B004","relation_type":"same_field","shared_zone":"İki dal ağırlık ölçüleri alanına aittir."},{"boundary_match":"partial","distinction":"Odak dal nicel ölçü ve tartı düzenine bağlıdır; komşu dal böyle bir teknik ölçme kısıtı olmadan ağırlık niteliğini anlatır.","focus_only":"Odak dal ölçülmüş ya da ölçen ağırlıktır.","gloss":"ölçü ağırlığı ile ağırlık","neighbor_only":"Komşu dal genel ağır olma niteliğidir.","neighbor_ref":"root_000202/B001","relation_type":"near_neighbor","shared_zone":"Tartı ve ağır gelme ortak zemindir."}],"source_phrase_ar":"المثقال وزن معلوم قدره ومثقال الشيء ميزانه من مثله (ayn;tahdhib)؛ أعطه ثقله أي وزنه وثقلت الشاة (sihah;tahdhib)؛ المثقال ما يوزن به وهو اسم لكل سنج (mufradat)","source_summary":"Kaynaklar dalı ölçü, tartı aracı, ağırlık miktarı ve tartma işlemi çevresinde toplar; kullanım teknik ve nicelik belirleyicidir, yük veya soyut değer anlamını kendiliğinden taşımaz.","sources":["AY","SI","TA","MU"],"what_is_ar":"المثقال والميزان والوزن المعلوم، وإعطاء الشيء ثقله ووزنه","what_is_not_ar":"الأحمال والأمتعة؛ الأوزار؛ الثقل بمعنى النفاسة؛ الثقلة في البدن"},"support_links":["sup_8b6e75f36708cb4fb7a9"]},{"boundary":"Dal kıymet ve itibar ağırlığıdır; taşınan yük ya da tartı birimi değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000202/B005","candidate_links":[{"candidate_id":"cand_3084439aee38e29309b3","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ثَّقَلَان","morph_features":"STEM|POS:N|LEM:v~aqalaAn|ROOT:vql|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:3:1","qac_word_ref":"99:2:3","surface_ar":"أَثْقَالَ"}],"gloss":"değer ağırlığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ağırlık, değerli ve korunmaya layık şeyin kıymetini anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Saygın kişi veya övülen insan için ağırlık, itibar ve mevki bildirir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ağır söz, etkisi, doğruluğu, yararı veya yüce değeri sebebiyle önemli sözdür."}}],"root_ar":"ث ق ل","root_id":"root_000202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kıymet, saygınlık ve söze verilen büyük önem alanını tek ifadede toplar.","boundary_detail":"Dal kıymet ve itibar ağırlığıdır; taşınan yük ya da tartı birimi değildir.","branch_image_ar":"الثقل النفيس ذو القدر","concept_gloss":"değer ağırlığı","contextual_glosses":[{"applicability":"Korunmuş veya değerli nesne bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Saygın kişi ve ağır söz kullanımlarını dışarıda bırakır.","preserves":"Kıymet ve korunmuşluk alanını korur."},"facet_ids":["F001"],"text":"kıymetli şey","usage_role":"contextual"},{"applicability":"Sözün yüce değer, doğruluk, açıklık veya fayda sebebiyle önemli olduğu bağlamda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözün değer ve etki ağırlığını korur."},"facet_ids":["F003"],"text":"ağır söz","usage_role":"contextual"}],"definition":"Kıymetli, korunmuş, itibarlı veya etkisi büyük olan şeyin taşıdığı değer ağırlığıdır; seçkin kimse, önemli söz ve büyük sayılan ikili adlandırmalar bu alanda yer alır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ağırlık, değerli ve korunmaya layık şeyin kıymetini anlatır."},{"facet_id":"F002","role":"extension","statement":"Saygın kişi veya övülen insan için ağırlık, itibar ve mevki bildirir."},{"facet_id":"F003","role":"associated_use","statement":"Ağır söz, etkisi, doğruluğu, yararı veya yüce değeri sebebiyle önemli sözdür."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Teknik ölçme ve tartı alanı ekler.","collision":"Ayrı ölçü ağırlığı dalıyla çakışır.","fit":"displacement","loses":"Kıymet, itibar ve sözün değeri alanını kaybeder.","preserves":"Ağırlık sözcüğünün temel alanını korur."},"text":"tartı ağırlığı"}],"identity_rationale":"Kaynak ifadesi ağırlığı fiziksel yükten çıkarıp kıymet, korunmuşluk, saygınlık ve sözü ağır kılan değer alanına taşır. Çerçeve bu değer alanını yük, hastalık ve teknik ölçü anlamlarından ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kıymetli, korunmuş veya itibarlı şey"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"büyük önemleri sebebiyle birlikte anılan iki varlık ya da değerli iki emanet"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"büyük değeri ve etkisi olan söz"}],"lexicalization_note":"Mixed_non_bare kapsam, değer bildiren biçimleri ve belirli söz birleşimini aynı mecazi değer sınırında tutar.","neighbor_coverage_note":"Yücelik, mevki, kıymet ve değer adayları değerlendirildi; takip, mal biriktirme veya genel güzellik gibi adaylar daha uzak tematik ilişkide kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kıymeti ağır olma imgesiyle anlatır; komşu dal ağırlık imgesine bağlı olmadan yücelik ve büyüklük bildirir.","focus_only":"Odak dal değeri ağırlık imgesiyle kurar.","gloss":"değer ağırlığı ile yücelik","neighbor_only":"Komşu dal doğrudan yücelik, azamet ve gözde büyüklük bildirir.","neighbor_ref":"root_000227/B001","relation_type":"near_synonym","shared_zone":"İki dal yüksek değer ve saygınlık alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal daha geniş bir kıymet ve korunmuşluk alanı taşır; komşu dal kişinin ya da şeyin değer ve mevki ölçüsüne yoğunlaşır.","focus_only":"Odak dal kıymetli şey, saygın kişi ve ağır söz alanlarını kapsar.","gloss":"değer ağırlığı ile mevki","neighbor_only":"Komşu dal değer veya mevkiyi tartı ve ağırlık imgesinden hareketle belirtir.","neighbor_ref":"root_001645/B007","relation_type":"near_synonym","shared_zone":"İki dal değeri ağırlık veya tartı mecazıyla anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal ağırlığı kıymet ve önem olarak yorumlar; komşu dal bu özel değer yorumu olmadan ağırlık niteliğini verir.","focus_only":"Odak dal kıymet ve itibar ağırlığıdır.","gloss":"değer ağırlığı ile ağırlık","neighbor_only":"Komşu dal genel maddi ya da soyut ağırlık niteliğidir.","neighbor_ref":"root_000202/B001","relation_type":"near_neighbor","shared_zone":"Odak dal, genel ağırlık fikrinin soyut değer alanına taşınmasıyla kurulur."}],"source_phrase_ar":"سمي الجن والإنس الثقلين (maqayis;sihah;tahdhib)؛ كل شيء نفيس مصون ثقل ويقال للسيد العزيز ثقل (tahdhib)؛ قولا ثقيلا يعني عظم قدره وجلالة خطره وقول له وزن (tahdhib)؛ الثقيل في الإنسان يستعمل في المدح (mufradat)","source_summary":"Kaynaklar dalı kıymetli ve korunmuş şey, itibarlı kişi, ağır ve değerli söz, ayrıca büyüklükleri sebebiyle birlikte anılan varlıklar etrafında toplar; fiziksel ağırlık burada değer ve önem metaforuna dönüşür.","sources":["MQ","SI","TA","MU"],"what_is_ar":"كل شيء نفيس مصون أو علق خطير، والسيد العزيز، والقول ذو الوزن والقدر، وما سمي ثقلين لعظم شأنه","what_is_not_ar":"الثقل بمعنى المتاع؛ الأوزار؛ ثقل المرض والنوم؛ المثقال الحسابي"},"support_links":["sup_8b6e75f36708cb4fb7a9"]},{"boundary":"Dal yaşanan ağırlık, halsizlik ve yavaşlamadır; gebelik veya ahlaki yük değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000202/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ثَّقَلَان","morph_features":"STEM|POS:N|LEM:v~aqalaAn|ROOT:vql|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:3:1","qac_word_ref":"99:2:3","surface_ar":"أَثْقَالَ"}],"gloss":"ağırlık ve halsizlik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bedende, nefiste veya yemekten sonra hissedilen ağırlık ve gevşeklik vardır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Uyku veya hastalık kişiyi baskılayıp ağırlaştırabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yavaşlama, ayak sürüme ve yere doğru ağır davranma bu alana girer."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Sözün dinleyene hoş gelmemesi, kabulde ağır gelme olarak bağlı bir kullanımdır."}}],"root_ar":"ث ق ل","root_id":"root_000202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Beden, iç hal, uyku, hastalık ve yavaşlama alanlarını birlikte karşılar.","boundary_detail":"Dal yaşanan ağırlık, halsizlik ve yavaşlamadır; gebelik veya ahlaki yük değildir.","branch_image_ar":"الثقلة والبطء","concept_gloss":"ağırlık ve halsizlik","contextual_glosses":[{"applicability":"Bedende veya içte duyulan ağırlık ve gevşeklik bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uyku, hastalık, yavaşlama ve sözün ağır gelişi ayrıntılarını dışarıda bırakır.","preserves":"Bedensel ve içsel gevşeme halini korur."},"facet_ids":["F001"],"text":"halsizlik","usage_role":"contextual"},{"applicability":"Uykunun kişiyi ağırlaştırdığı kullanımda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Baskın uykunun ağırlaştırmasını korur."},"facet_ids":["F002"],"text":"uyku bastırdı","usage_role":"contextual"},{"applicability":"Yavaşlama ve ayak sürüme bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tembelce yavaşlama ve davranışta ağırlaşmayı korur."},"facet_ids":["F003"],"text":"ağırdan aldı","usage_role":"contextual"}],"definition":"Kişinin bedeni, iç hali, uykusu, hastalığı, yediği şey veya davranışı sebebiyle ağırlaşması, gevşemesi ve yavaşlamasıdır; bazı kullanımlarda sözün kulağa hoş gelmemesi de bu ağır gelme alanına bağlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bedende, nefiste veya yemekten sonra hissedilen ağırlık ve gevşeklik vardır."},{"facet_id":"F002","role":"specialization","statement":"Uyku veya hastalık kişiyi baskılayıp ağırlaştırabilir."},{"facet_id":"F003","role":"extension","statement":"Yavaşlama, ayak sürüme ve yere doğru ağır davranma bu alana girer."},{"facet_id":"F004","role":"associated_use","statement":"Sözün dinleyene hoş gelmemesi, kabulde ağır gelme olarak bağlı bir kullanımdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Rahimde çocuk taşıma koşulu ekler.","collision":"Ayrı gebelikte ağırlaşma dalıyla çakışır.","fit":"displacement","loses":"Halsizlik, uyku, hastalık ve yavaşlama alanını kaybeder.","preserves":"Bedende ağırlaşma fikrini korur."},"text":"gebelik"}],"identity_rationale":"Kaynak ifadesi bedende, nefiste, yemekte, uykuda, hastalıkta ve davranışta ortaya çıkan ağırlık, gevşeme, baskılanma ve yavaşlamayı toplar. Çerçeve gebelik, günah yükü ve kıymet ağırlığıyla karışmadığı sürece doğrudur.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"içte, bedende veya yemekten sonra duyulan ağırlık ve gevşeklik"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bastıran uyku hali"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"hastalık onu ağırlaştırdı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"uyku ona ağır bastı"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"ağırlaşmış, yavaş veya gücünü aşan yük altında kalmış"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"ağırdan alma, yavaşlama ve ayak sürüme"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"sözün kulağa hoş gelmemesi veya kabulünün ağır gelmesi"}],"lexicalization_note":"Mixed_non_bare kapsam, çıplak hal bildiren biçimleri ve hastalık, uyku, söz gibi birleşimsel kullanımları ayrı tutar.","neighbor_coverage_note":"Yavaşlık, uyku, hastalık ve yere ağırlaşma adayları değerlendirildi; bağırsak, titreme veya zayıflama gibi adaylar odak sınırı için daha dolaylı kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal daha geniş bir yaşanan ağırlık alanı taşır; komşu dal özellikle görevden geri duran tembellik yönünü belirginleştirir.","focus_only":"Odak dal bedensel, uykusal, hastalıklı veya davranışsal ağırlaşmayı kapsar.","gloss":"ağırlık ve halsizlik ile tembellik","neighbor_only":"Komşu dal yapılması gereken şeyden geri durma anlamındaki tembellik ve üşenmeye odaklanır.","neighbor_ref":"root_001299/B001","relation_type":"near_synonym","shared_zone":"İki dal yavaşlama ve isteksiz hareket alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal uykuyu daha geniş ağırlaşma alanının bir gerçekleşmesi yapar; komşu dal uyku çokluğu ve uyku baskısında daralır.","focus_only":"Odak dal uyku dışında hastalık, yemek, beden ve davranış ağırlaşmasını da kapsar.","gloss":"halsizlik ile çok uyuma","neighbor_only":"Komşu dal çok uyuma veya uyku basması alanında kalır.","neighbor_ref":"root_001568/B002","relation_type":"near_neighbor","shared_zone":"İki dal baskın uyku haliyle kesişir."},{"boundary_match":"partial","distinction":"Odak dal yorgunluk, hastalık, uyku ve yavaşlık kaynaklarını kapsar; komşu dal yalnızca gebelik yüküne bağlıdır.","focus_only":"Odak dal genel bedensel veya davranışsal ağırlaşmadır.","gloss":"halsizlik ile gebelikte ağırlaşma","neighbor_only":"Komşu dal kadının gebeliği sebebiyle ağırlaşmasıdır.","neighbor_ref":"root_000202/B007","relation_type":"near_neighbor","shared_zone":"Her ikisi de bedende ağırlık oluşmasını anlatır."}],"source_phrase_ar":"أجد في نفسي ثقلة (maqayis)؛ الثقلة نعسة غالبة وأثقله المرض واستثقله النوم والمثقل البطيء والتثاقل من التباطؤ (ayn)؛ وجدت ثقلة في جسدي أي ثقلا وفتورا (sihah)؛ الثقلة ما وجد الإنسان من ثقل الطعام وأصبح ثاقلاء أثقله المرض (tahdhib)؛ اثاقلتم إلى الأرض (mufradat)","source_summary":"Kaynaklar dalı içte veya bedende duyulan ağırlık, yemek sonrası ağırlık, baskın uyku, hastalığın ağırlaştırması, yavaş hareket ve ağır gelen söz çevresinde toplar; ortak nokta kişinin hafif ve çevik halden uzaklaşmasıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الثقلة في النفس أو الجسد أو الطعام، وغلبة النعاس، وإثقال المرض أو النوم، والبطء والتباطؤ والتحامل في الوطء","what_is_not_ar":"الحمل في البطن؛ الأوزار الشرعية؛ المثقال؛ النفاسة والقدر"},"support_links":[]},{"boundary":"Dal yalnızca gebelik yüküyle ağırlaşmadır; genel halsizlik ya da beden biçimi değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000202/B007","candidate_links":[{"candidate_id":"cand_53710bdd9cdb1fc279bf","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ثَّقَلَان","morph_features":"STEM|POS:N|LEM:v~aqalaAn|ROOT:vql|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:3:1","qac_word_ref":"99:2:3","surface_ar":"أَثْقَالَ"}],"gloss":"gebelikte ağırlaşma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadın, karnındaki gebelik yükü sebebiyle ağırlaşır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu hal, gebeliği ağırlaşmış kadın için bir niteleme oluşturur."}}],"root_ar":"ث ق ل","root_id":"root_000202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kadının hamilelik yüküyle ağırlaşması çekirdeğini açıkça verir.","boundary_detail":"Dal yalnızca gebelik yüküyle ağırlaşmadır; genel halsizlik ya da beden biçimi değildir.","branch_image_ar":"إثقال الحمل","concept_gloss":"gebelikte ağırlaşma","contextual_glosses":[{"applicability":"Kadının gebelik yükünün belirginleştiği fiil bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gebeliğe bağlı ağırlaşma olayını korur."},"facet_ids":["F001"],"text":"hamileliği ağırlaştı","usage_role":"contextual"},{"applicability":"Gebeliği ilerlemiş ve yükü ağırlaşmış kadını niteleyen kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gebeliğin kişiyi ağırlaştıran niteliğini korur."},"facet_ids":["F002"],"text":"ağır hamile kadın","usage_role":"contextual"}],"definition":"Kadının karnındaki gebelik yükü sebebiyle ağırlaşması ve bu yükle ağırlaşmış kadın olarak nitelenmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadın, karnındaki gebelik yükü sebebiyle ağırlaşır."},{"facet_id":"F002","role":"specialization","statement":"Bu hal, gebeliği ağırlaşmış kadın için bir niteleme oluşturur."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Gebelik dışı hastalık, uyku veya yorgunluk sebeplerini ekler.","collision":"Ayrı halsizlik ve yavaşlama dalıyla çakışır.","fit":"broadening","loses":null,"preserves":"Bedensel ağırlaşma hissini kısmen korur."},"text":"halsizlik"}],"identity_rationale":"Kaynak ifadesi kadının karnındaki hamilelik yükü sebebiyle ağırlaşmasına ve bu haldeki kadının nitelenmesine odaklanır. Çerçeve bunu genel hastalık ağırlığı veya iri beden betimlemesiyle karıştırmaz.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kadının gebelik yüküyle ağırlaşması"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"gebeliği ağırlaşmış kadın"}],"lexicalization_note":"Mixed_non_bare kapsam, gebelik birleşimini ve bu haldeki kişi niteliğini aynı koşula bağlı tutar.","neighbor_coverage_note":"Gebelik, doğum, rahimde yerleşme ve kadın bedeni adayları değerlendirildi; boyun ağrısı veya benzer uzak bedensel adaylar sınırı güçlendirmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal gebeliğin oluşturduğu ağırlık sonucuna odaklanır; komşu dal gebelik durumunun kendisini ve süresini anlatır.","focus_only":"Odak dal gebelik yükünün kadını ağırlaştırmasıdır.","gloss":"gebelikte ağırlaşma ile gebelik","neighbor_only":"Komşu dal gebeliğin kendisi, karındaki çocuk ve gebelik süresi alanıdır.","neighbor_ref":"root_000291/B006","relation_type":"near_synonym","shared_zone":"İki dal kadının karnındaki gebelik alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal ağırlığın artışını söyler; komşu dal zayıflama ve yıpranma sonucunu öne çıkarır.","focus_only":"Odak dal gebelik yüküyle ağırlaşmadır.","gloss":"ağır hamilelik ile gebelik zayıflığı","neighbor_only":"Komşu dal gebeliğin kadını zayıflatması veya yıpratmasıdır.","neighbor_ref":"root_000341/B007","relation_type":"near_neighbor","shared_zone":"İki dal hamileliğin bedende oluşturduğu etkiyi paylaşır."},{"boundary_match":"field_only","distinction":"Odak dal gebelik koşuluna bağlıdır; komşu dal gebelikten bağımsız beden biçimi veya vakar betimlemesidir.","focus_only":"Odak dal hamilelik yükünden doğan ağırlaşmadır.","gloss":"hamile ağırlığı ile kadın betimi","neighbor_only":"Komşu dal kadının beden biçimi veya oturuşta ağırbaşlılığıdır.","neighbor_ref":"root_000202/B008","relation_type":"same_field","shared_zone":"İki dal kadın bedeni veya kadın niteliği alanında buluşur."}],"source_phrase_ar":"اثقلت المرأة فيه مثقل (ayn)؛ أثقلت المرأة فهي مثقل أي ثقل حملها في بطنها (sihah)؛ المثقل من النساء التي قد ثقلت من حملها (tahdhib)","source_summary":"Kaynaklar dalı kadının hamileliği nedeniyle karnında ağırlık taşıması ve bu sebeple ağırlaşmış kadın diye nitelenmesi olarak verir; anlamın belirleyici koşulu gebeliktir.","sources":["AY","SI","TA"],"what_is_ar":"إثقال المرأة بحملها في بطنها، والمثقل من النساء بسبب الحمل","what_is_not_ar":"الأوزار والخطايا؛ الأمتعة؛ ثقل المرض؛ امرأة ثقال ذات كفل"},"support_links":["sup_82bbad2e93d869d8e71f"]},{"boundary":"Dal belirli kadın betimidir; hamilelik veya işitme ağırlığı değildir.","branch_kind":"collocation","branch_ref":"root_000202/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ثَّقَلَان","morph_features":"STEM|POS:N|LEM:v~aqalaAn|ROOT:vql|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:3:1","qac_word_ref":"99:2:3","surface_ar":"أَثْقَالَ"}],"gloss":"dolgun kalçalı ağırbaşlı kadın","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kadın, kalça ve oturak dolgunluğu sebebiyle böyle nitelenir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı niteleme mecliste ağırbaşlı ve vakur duruşa yakın açıklanabilir."}}],"root_ar":"ث ق ل","root_id":"root_000202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem beden betimini hem de bağlı vakar açıklamasını doğal Türkçeyle verir.","boundary_detail":"Dal belirli kadın betimidir; hamilelik veya işitme ağırlığı değildir.","branch_image_ar":"امرأة ثقال","concept_gloss":"dolgun kalçalı ağırbaşlı kadın","contextual_glosses":[{"applicability":"Beden biçimi açıklamasının öne çıktığı bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadına özgü beden dolgunluğu betimini korur."},"facet_ids":["F001"],"text":"dolgun kalçalı kadın","usage_role":"contextual"},{"applicability":"Mecliste vakur duruşun öne çıktığı açıklama bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Beden dolgunluğu çekirdeğini dışarıda bırakır.","preserves":"Vakur duruş uzantısını korur."},"facet_ids":["F002"],"text":"ağırbaşlı kadın","usage_role":"contextual"}],"definition":"Kadın için kullanılan, kalça ve oturak dolgunluğunu bildiren nitelemedir; bazı açıklamalarda mecliste ağırbaşlı ve vakur duruşa da yaklaşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kadın, kalça ve oturak dolgunluğu sebebiyle böyle nitelenir."},{"facet_id":"F002","role":"extension","statement":"Aynı niteleme mecliste ağırbaşlı ve vakur duruşa yakın açıklanabilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Gebelik koşulu ekler.","collision":"Ayrı gebelikte ağırlaşma dalıyla çakışır.","fit":"displacement","loses":"Kalça dolgunluğu ve vakur duruş betimini kaybeder.","preserves":"Kadınla ilgili bedensel ağırlık fikrini kısmen korur."},"text":"hamile kadın"}],"identity_rationale":"Kaynak ifadesi belirli bir kadın betimini verir: kalça ve oturak dolgunluğu, ayrıca mecliste ağırbaşlı duruşa yakın bir kullanım. Çerçeve bunu gebelikle değil beden biçimi ve vakar niteliğiyle sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"dolgun kalçalı veya mecliste ağırbaşlı kadın"}],"lexicalization_note":"Collocation kapsam, tanımı yalnızca verilen kadın nitelemesine bağlar; çıplak ağırlık anlamına genelleştirilmez.","neighbor_coverage_note":"Kadın bedeni, dolgunluk, tavır ve kadın betimi adayları değerlendirildi; at bedeni veya genç kız betimi gibi adaylar odak nitelemeyle daha uzak kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli kadın betimine bağlıdır; komşu dal cinsiyete ve belirli beden bölgesine bağlı olmayan genel semizlik alanındadır.","focus_only":"Odak dal kadın için belirli kalça ve oturak dolgunluğu nitelemesidir.","gloss":"kadın dolgunluğu ile semizlik","neighbor_only":"Komşu dal genel şişmanlık, semizlik veya semirtme alanıdır.","neighbor_ref":"root_000744/B001","relation_type":"near_neighbor","shared_zone":"İki dal bedensel dolgunluk alanında örtüşür."},{"boundary_match":"field_only","distinction":"Odak dal ağırlık ve dolgunluk imgesine bağlıdır; komşu dal naz, tavır güzelliği ve duruş çekiciliğine odaklanır.","focus_only":"Odak dal dolgunluk ve ağırbaşlı kadın betimidir.","gloss":"ağırbaşlı kadın ile tavır güzelliği","neighbor_only":"Komşu dal görünüşte zarafet, tavır ve çekicilik alanını anlatır.","neighbor_ref":"root_000484/B003","relation_type":"same_field","shared_zone":"İki dal kadın tavrı ve görünüş betiminde buluşabilir."},{"boundary_match":"field_only","distinction":"Odak dal beden biçimi veya meclis vakarını anlatır; komşu dal yalnızca gebelik yükünden doğan ağırlaşmayı anlatır.","focus_only":"Odak dal gebelikten bağımsız kadın betimidir.","gloss":"kadın betimi ile hamilelik ağırlığı","neighbor_only":"Komşu dal hamilelik yüküyle ağırlaşmadır.","neighbor_ref":"root_000202/B007","relation_type":"same_field","shared_zone":"İki dal kadın bedeniyle ilgili nitelemelerdir."}],"source_phrase_ar":"امرأة ثقال أي ذات مآكم وكفل (ayn;sihah;tahdhib)؛ هذه امرأة ثقال وهذه امرأة رزان أي رزينة في مجلسها (tahdhib)","source_summary":"Kaynaklar bu dalı kadın için bedensel dolgunluk betimi olarak verir ve bir açıklamada oturuş ya da meclis vakarına yaklaştırır; belirleyici olan gebelik değil niteleme bağlamıdır.","sources":["AY","SI","TA"],"what_is_ar":"وصف المرأة بالثقال لذات المآكم والكفل، ويقارب الرزانة في المجلس","what_is_not_ar":"المرأة المثقل من الحمل؛ الثقل في السمع؛ المتاع؛ الأوزار"},"support_links":[]},{"boundary":"Dal işitme duyusundaki ağırlık ve kabul zayıflığıdır; genel ağırlık değildir.","branch_kind":"collocation","branch_ref":"root_000202/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ثَّقَلَان","morph_features":"STEM|POS:N|LEM:v~aqalaAn|ROOT:vql|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:3:1","qac_word_ref":"99:2:3","surface_ar":"أَثْقَالَ"}],"gloss":"işitme ağırlığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kulak, kendisine gelen şeyi kabul etmekte zorlanır ve işitme zayıflar."}}],"root_ar":"ث ق ل","root_id":"root_000202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kulakta ağırlık ve işitme kabulünün zayıflaması çekirdeğini açıkça karşılar.","boundary_detail":"Dal işitme duyusundaki ağırlık ve kabul zayıflığıdır; genel ağırlık değildir.","branch_image_ar":"ثقل السمع","concept_gloss":"işitme ağırlığı","contextual_glosses":[{"applicability":"Kişinin işitmesinin zayıf olduğu doğal Türkçe bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kulakta ağırlık ve işitme zayıflığını korur."},"facet_ids":["F001"],"text":"kulağı ağır işitir","usage_role":"contextual"},{"applicability":"Ağırlık imgesi yerine sonucu açıklamak gereken bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kulağın geleni kabul etmekte ağırlaşması imgesini açıkça vermez.","preserves":"İşitmenin zayıflaması sonucunu korur."},"facet_ids":["F001"],"text":"işitmesi zayıf","usage_role":"contextual"}],"definition":"Kulakta veya işitmede ağırlık, yani kulağın kendisine yöneltilen sesi veya sözü almakta zorlanması ve işitmenin zayıflamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kulak, kendisine gelen şeyi kabul etmekte zorlanır ve işitme zayıflar."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Sözün hoş karşılanmaması anlamı ekler.","collision":"Sözün ağır gelmesi, halsizlik ve ağır gelme dalındaki bağlı kullanımla çakışır.","fit":"displacement","loses":"Kulak ve işitme zayıflığı koşulunu kaybeder.","preserves":"Kabulde zorlanma fikrini kısmen korur."},"text":"söz ağır geldi"}],"identity_rationale":"Kaynak ifadesi kulakta ağırlığı, kulağın kendisine yöneltileni kabul etmekte zorlanması veya işitmenin zayıflaması olarak tanımlar. Çerçeve bunu sözün hoş gelmemesi, genel beden ağırlığı veya ölçü alanıyla karıştırmaz.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"kulağında ağırlık var, işitmesi zayıf"}],"lexicalization_note":"Collocation kapsam, anlamı kulakta ağırlık birleşimine bağlar ve çıplak ağırlık anlamına genelleştirmez.","neighbor_coverage_note":"İşitme, dinleme, sağırlaşma ve kulak verme adayları değerlendirildi; konuşma bozukluğu veya cevap verememe adayları farklı duyusal veya ifade alanlarında kaldı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Odak dal ve komşu dal aynı işitme ağırlığı sınırında kullanılabilir; komşu kartta kapanma vurgusu olsa da dal çekirdeği odak kullanımla örtüşür.","focus_only":null,"gloss":"işitme ağırlığı","neighbor_only":null,"neighbor_ref":"root_001674/B001","relation_type":"synonym","shared_zone":"İki dal kulakta ağırlık ve işitmenin kapanması ya da zorlaşması alanını paylaşır."},{"boundary_match":"partial","distinction":"Odak dal zayıflama veya ağırlık düzeyinde kalabilir; komşu dal tam sağırlığa ve mecazi dinlememe tavrına kadar genişler.","focus_only":"Odak dal işitmenin ağırlaşması ve geleni almakta zorlanmasıdır.","gloss":"ağır işitme ile sağırlık","neighbor_only":"Komşu dal işitmenin gitmesi, sağırlık ve bazen dinlememe tavrıdır.","neighbor_ref":"root_000884/B001","relation_type":"near_synonym","shared_zone":"İki dal işitme eksikliğinde örtüşür."},{"boundary_match":"opposed","distinction":"Odak dal alımın zayıflığını belirtir; komşu dal alıma yönelme ve dikkatli dinleme yönündedir.","focus_only":"Odak dal kulağın kabulde ağırlaşmasıdır.","gloss":"ağır işitme ile kulak verme","neighbor_only":"Komşu dal kulağı bir söze yöneltip dikkatle dinlemedir.","neighbor_ref":"root_000574/B004","relation_type":"polarity_pair","shared_zone":"İki dal kulağın söze yönelmesi ve sesi alma sahasını paylaşır."}],"source_phrase_ar":"في أذنه ثقل إذا لم يجد سمعه كأنه يثقل عن قبول ما يلقى إليه (mufradat)","source_summary":"Kaynak dalı tek bir işitme bağlamında verir: kulakta ağırlık vardır ve bu ağırlık, işitmenin kendisine geleni kolayca alamaması şeklinde anlaşılır.","sources":["MU"],"what_is_ar":"الثقل في الأذن، أي ضعف قبول السمع لما يلقى إليه","what_is_not_ar":"ثقل القول لسوء سماعه؛ ثقل الجسم؛ الأوزار؛ المثقال"},"support_links":[]},{"boundary":"Dal, mali ödeme, renk örüntüsü, yara ve öteki özelleşmiş kullanımları kapsamaz.","branch_kind":"bare","branch_ref":"root_000400/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:2:1:2","qac_word_ref":"99:2:1","surface_ar":"أَخْرَجَتِ"}],"gloss":"bir yerden ya da durumdan dışarı çıkma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yerden, kapsayıcıdan veya durumdan dışarıya geçme hareketi gerçekleşir."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın hareket veya durum değişikliği anlamının tamamı için kullanılır.","boundary_detail":"Dal, mali ödeme, renk örüntüsü, yara ve öteki özelleşmiş kullanımları kapsamaz.","branch_image_ar":"النفاذ إلى خارج الشيء","concept_gloss":"bir yerden ya da durumdan dışarı çıkma","contextual_glosses":[{"applicability":"Bir kişinin veya nesnenin bulunduğu yerden ayrıldığı doğal cümlelerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yer veya durum dışına geçme hareketini doğal biçimde korur."},"facet_ids":["F001"],"text":"dışarı çıkmak","usage_role":"general"}],"definition":"Bir varlığın bulunduğu yerden, içinde olduğu şeyden veya sürmekte olan bir durumdan dışarıya geçmesidir; içeri girmenin karşıtıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yerden, kapsayıcıdan veya durumdan dışarıya geçme hareketi gerçekleşir."}],"identity_rationale":"Kaynak ifadesi, bir yerden veya durumdan dışarı çıkmayı ve bunun içeri girmenin karşıtı oluşunu açıkça kurar. Geçici dal çerçevesi bu çekirdeği doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"dışarı çıktı; bir yerden veya durumdan ayrıldı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"dışarı çıkma; bir durumdan ayrılma"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"dışarı çıkan veya ayrılan"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"çıkış yeri veya çıkış yönü"}],"lexicalization_note":"Tanım yalın çıkma anlamıyla sınırlıdır; başka dallardaki kalıplaşmış kullanımlar buraya taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sınırı en iyi açıklayan yakın anlamlı karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu kullanım çıkma eyleminin belirli bir söyleyişine bağlıdır; odak dal ise yer, kapsayıcı ve durum değişikliğini kapsayan yalın ve daha genel çekirdektir.","focus_only":"Odak dal, yerden çıkmanın yanında bir durumdan ayrılmayı ve içeri girme karşıtlığını da kapsar.","gloss":"bir şeyden çıkma","neighbor_only":"Komşu dal, belirli bir kişi öznesiyle bir şeyden çıkmayı anlatan daha dar bir kullanımdır.","neighbor_ref":"root_001158/B004","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir sınırın veya kapsayıcının dışına geçiş vardır."}],"source_phrase_ar":"النفاذ عن الشيء (maqayis)؛ الخروج نقيض الدخول (ayn;jamhara;tahdhib)؛ خرج خروجا برز من مقره أو حاله (mufradat)","source_summary":"Kaynaklar, dışarıya geçme ve içeri girmenin karşıtı olma çekirdeğinde birleşir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"كل بروز أو انفصال عن مقر أو حال، والدخول نقيضه","what_is_not_ar":"الخراج المالي؛ الخرج اللوني؛ الخراج الجسدي"},"support_links":[]},{"boundary":"Yalın çıkma bu dalın çekirdeği değildir; burada bir etken başka bir şeyi çıkarır, elde eder veya yetiştirir.","branch_kind":"mixed_non_bare","branch_ref":"root_000400/B002","candidate_links":[{"candidate_id":"cand_fd4bbfaa69ddab402681","lane":"micro"},{"candidate_id":"cand_53710bdd9cdb1fc279bf","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:2:1:2","qac_word_ref":"99:2:1","surface_ar":"أَخْرَجَتِ"}],"gloss":"bir şeyi çıkarma, elde etme veya yetiştirme","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir etken, başka bir varlığı bulunduğu yerden çıkarır veya görünür duruma getirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İşlem, saklı ya da örtük bir şeyi çıkarıp elde etme biçiminde gerçekleşebilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Eğitimde kişi bilgisizlikten çıkarılarak yetişmiş bir duruma geçirilir."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ettirgen çekirdeği ve kanıtlanan işlem ile eğitim uzantılarını birlikte temsil eder.","boundary_detail":"Yalın çıkma bu dalın çekirdeği değildir; burada bir etken başka bir şeyi çıkarır, elde eder veya yetiştirir.","branch_image_ar":"إخراج الشيء من خفائه","concept_gloss":"bir şeyi çıkarma, elde etme veya yetiştirme","contextual_glosses":[{"applicability":"Bir nesnenin dışarı çıkarıldığı veya görünür kılındığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başka bir varlığı görünür duruma getiren ettirgen işlemi korur."},"facet_ids":["F001"],"text":"ortaya çıkarmak","usage_role":"contextual"},{"applicability":"Saklı veya örtük bir sonucun işlem yoluyla elde edildiği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çıkarma yoluyla bir sonuca ulaşma işlemini bütünüyle korur."},"facet_ids":["F002"],"text":"çıkarıp elde etmek","usage_role":"contextual"},{"applicability":"Bir kişinin eğitimle bilgisizlikten çıkarıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eğitim veren etkeni ve öğrenende oluşan durum değişikliğini korur."},"facet_ids":["F003"],"text":"eğitip yetiştirmek","usage_role":"contextual"}],"definition":"Bir etkenin bir şeyi bulunduğu yerden dışarı çıkarması, görünür kılması veya işleyerek elde etmesidir. Eğitim bağlamında kişiyi bilgisizlik sınırından çıkarıp yetiştirmeyi de anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir etken, başka bir varlığı bulunduğu yerden çıkarır veya görünür duruma getirir."},{"facet_id":"F002","role":"specialization","statement":"İşlem, saklı ya da örtük bir şeyi çıkarıp elde etme biçiminde gerçekleşebilir."},{"facet_id":"F003","role":"extension","statement":"Eğitimde kişi bilgisizlikten çıkarılarak yetişmiş bir duruma geçirilir."}],"identity_rationale":"Kaynak ifadesi yalnızca gizlenmiş bir şeyi görünür kılmayı değil, bir şeyi dışarı çıkarmayı, çıkarıp elde etmeyi ve eğitimle bilgisizlik sınırından geçirmeyi de içerir. Bu nedenle dal, gizlilikle sınırlı olmayan ettirgen ve elde edici bir süreç olarak yeniden çerçevelenmiştir.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"dışarı çıkardı veya ortaya koydu"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"nesneleri dışarı çıkarma veya görünür kılma"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"çıkarıp elde etti"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"işleyip ortaya çıkarma veya çeşitlere ayırma"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"eğitim görüp yetişti"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"birinin elinde yetişmiş öğrenci"}],"lexicalization_note":"Tanım, ettirgen çıkarma ile kalıba bağlı elde etme ve eğitim kullanımlarını ayırır; bunları yalın çıkma anlamında birleştirmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; görünür kılma ile çıkarıp elde etme arasındaki sınır en yararlı karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşunun merkezi görünürlüktür; odak dalda ise yerden çıkarma, işlemle elde etme ve kişiyi bilgisizlikten çıkarma gibi görünürlükten daha geniş ettirgen geçişler bulunur.","focus_only":"Odak dal çıkarıp elde etmeyi ve eğitimle yetiştirmeyi de kapsar.","gloss":"gizlilikten sonra belirme veya gösterme","neighbor_only":"Komşu dal, bir şeyin gizlilikten sonra görünür olması ile görünür kılınmasına odaklanır.","neighbor_ref":"root_000097/B001","relation_type":"near_synonym","shared_zone":"İki dal da görünür olmayan bir şeyin ortaya gelmesini veya getirilmesini içerebilir."}],"source_phrase_ar":"اخترجت الرجل واستخرجته سواء (ayn)؛ الاستخراج كالاستنباط (sihah)؛ الإخراج أكثر ما يقال في الأعيان (mufradat)؛ خريج فلان كأنه أخرجه من حد الجهل (maqayis)","source_summary":"Ortak çerçeve, bir şeyi dışarı çıkarma veya elde etme işlemidir; insan eğitimindeki kullanım bu geçişi bilgisizlikten yetişmişliğe taşır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"إخراج الشيء أو استخراجه أو تخريجه، ومنه إظهار الأعيان وإخراج المتعلم من الجهل","what_is_not_ar":"الخروج اللازم؛ الخراج المالي؛ الخرج اللوني"},"support_links":["sup_82bbad2e93d869d8e71f","sup_d17130fa1cecf805d0ab"]},{"boundary":"Dal, fiziksel çıkışı değil; ödeme, yükümlülük, getiri ve gider olarak hesaplanan mali değeri anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000400/B003","candidate_links":[{"candidate_id":"cand_3084439aee38e29309b3","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:2:1:2","qac_word_ref":"99:2:1","surface_ar":"أَخْرَجَتِ"}],"gloss":"düzenli mali yükümlülük, getiri veya gider","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yükümlü tarafından belirli ölçü veya döneme göre çıkarılan mali değer söz konusudur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Mali değer bazı kullanımlarda ürün getirisi, bazı kullanımlarda gelirin karşıtı olan giderdir."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın ödeme, ürün getirisi ve gelir karşıtı gider kapsamını birlikte temsil eder.","boundary_detail":"Dal, fiziksel çıkışı değil; ödeme, yükümlülük, getiri ve gider olarak hesaplanan mali değeri anlatır.","branch_image_ar":"مال يخرج على جهة معلومة","concept_gloss":"düzenli mali yükümlülük, getiri veya gider","contextual_glosses":[{"applicability":"Belirli miktarda ve dönemde ödenen mali yükümlülük bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ödeme niteliğini, yükümlüyü ve düzenli ölçüyü korur."},"facet_ids":["F001"],"text":"vergi veya düzenli ödeme","usage_role":"contextual"},{"applicability":"Mali değerin getiri ya da gelirin karşı kalemi olarak geçtiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Getiri ile gider arasındaki bağlama bağlı yön değişimini korur."},"facet_ids":["F002"],"text":"ürün getirisi veya gider","usage_role":"contextual"}],"definition":"Belirli bir dönem veya ölçüye göre ödenen para, ürün ya da mali yükümlülüktür. Bağlama göre elde edilen ürün getirisi veya gelirin karşısındaki gideri de gösterebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yükümlü tarafından belirli ölçü veya döneme göre çıkarılan mali değer söz konusudur."},{"facet_id":"F002","role":"source_variant","statement":"Mali değer bazı kullanımlarda ürün getirisi, bazı kullanımlarda gelirin karşıtı olan giderdir."}],"identity_rationale":"Kaynak ifadesi, verenin çıkardığı para, belirli dönem ve miktara bağlı mali yük, ürün getirisi ve gelirin karşısındaki gider anlamlarını birlikte destekler. Geçici çerçeve bu mali alanı doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"mali ödeme, vergi veya ürün getirisi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ürün getirisi, vergi veya zorunlu ödeme"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"hizmetindeki kişiyle aylık ödeme üzerinde anlaştı"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"efendisine düzenli ödeme yapmakla yükümlü köle"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"sorumluluk karşılığında elde edilen ürün getirisi"}],"lexicalization_note":"Mali çekirdek korunur; yalın ödeme ve gelir kullanımları, sözleşmeye bağlı özel ödeme kalıplarından ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel vergi ile genel mali yük ve getiri alanı arasındaki karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu kavram ödeyen topluluğu ve hukuki nedeni bakımından özeldir; odak dal ise ödeme, getiri ve gider yönleri bulunan daha geniş bir mali söz varlığı alanıdır.","focus_only":"Odak dal ürün getirisini, genel mali gideri ve farklı türde düzenli ödemeleri kapsar.","gloss":"belirli bir topluluğa yüklenen vergi","neighbor_only":"Komşu dal, belirli bir topluluktan hukuki statüsü nedeniyle alınan özel mali yükümlülüktür.","neighbor_ref":"root_000244/B004","relation_type":"near_neighbor","shared_zone":"Her iki dalda da yükümlüden alınan ve hukukça ya da düzenle belirlenen mali ödeme bulunur."}],"source_phrase_ar":"الخراج والخرج الإتاوة لأنه مال يخرجه المعطي (maqayis)؛ الخرج والخراج ما يخرج من المال في السنة بقدر معلوم (ayn;tahdhib)؛ الخراج الغلة (tahdhib)؛ الخرج بإزاء الدخل (mufradat)","source_summary":"Kaynakların ortak mali alanı, ölçülü bir ödeme veya yükümlülük ile ürün getirisi ve gider yönlerini bir arada içerir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"ما يخرجه المرء من مال أو غلة أو ضريبة أو وظيفة معلومة","what_is_not_ar":"الخروج المكاني؛ الخراج الجسدي؛ الخرج الوعاء"},"support_links":["sup_8b6e75f36708cb4fb7a9"]},{"boundary":"Dal yalnızca bedensel oluşumu kapsar; mali ödeme ve yerden çıkma anlamları dışarıda kalır.","branch_kind":"bare","branch_ref":"root_000400/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:2:1:2","qac_word_ref":"99:2:1","surface_ar":"أَخْرَجَتِ"}],"gloss":"bedende çıkan irinli şişlik veya yara","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Beden yüzeyinde şişlik, çıban veya yara biçiminde dışa vuran bir oluşum bulunur."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan ya da hayvanda dışa vuran çıban, şişlik ve yara türlerinin ortak adı olarak uygundur.","boundary_detail":"Dal yalnızca bedensel oluşumu kapsar; mali ödeme ve yerden çıkma anlamları dışarıda kalır.","branch_image_ar":"قُرْح يخرج في الجسد","concept_gloss":"bedende çıkan irinli şişlik veya yara","contextual_glosses":[{"applicability":"Oluşumun şiş ve irinli bir beden lezyonu olduğu bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Şişlik biçimini, bedensel yeri ve irinli oluşum niteliğini korur."},"facet_ids":["F001"],"text":"irinli şişlik","usage_role":"contextual"}],"definition":"İnsan veya hayvan bedeninde kendiliğinden beliren, şişlik, çıban ya da irinli yara niteliğindeki oluşumdur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Beden yüzeyinde şişlik, çıban veya yara biçiminde dışa vuran bir oluşum bulunur."}],"identity_rationale":"Kaynak ifadesi, insan veya hayvan bedeninde kendiliğinden beliren şişlik, irinli yara ve benzeri oluşumları açıkça tanımlar. Geçici dal kimliği bu bedensel çekirdekle uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bedende çıkan şişlik, çıban veya irinli yara"}],"lexicalization_note":"Tanım yalın bedensel lezyon anlamıyla sınırlıdır ve başka dallardaki mecazi çıkışları içermez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; belirli kabarcık ile geniş lezyon sınıfı arasındaki sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu, görünüşü ve hastalık türü belirlenmiş dar bir kabarcıktır; odak dal ise şişlikten irinli yaraya uzanan daha geniş bir bedensel oluşumdur.","focus_only":"Odak dal farklı büyüklük ve biçimlerdeki şişlik, çıban ve yaraları kapsar.","gloss":"mercimek tanesi biçiminde hastalık kabarcığı","neighbor_only":"Komşu dal mercimek tanesine benzeyen ve salgın hastalık türü sayılan belirli bir kabarcıktır.","neighbor_ref":"root_000990/B002","relation_type":"near_neighbor","shared_zone":"Her ikisi de bedende dışa vuran kabarık bir lezyonu gösterebilir."}],"source_phrase_ar":"الخراج بالجسد (maqayis)؛ الخراج ورم وقرح يخرج من ذاته (ayn)؛ ما خرج على الجسد من دمل ونحوه (jamhara)؛ ما يخرج في البدن من القروح (sihah)؛ ورم وقرح يخرج بدابة أو غيرها من الحيوان (tahdhib)","source_summary":"Kaynaklar, insan ve hayvan bedeninde beliren şişlik veya irinli yara anlamında birleşir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"الدمل والورم والقرح الخارج في الجسد أو الحيوان","what_is_not_ar":"الخراج المالي؛ الخروج من مكان؛ الخرج اللوني"},"support_links":[]},{"boundary":"Dal bulutun belirmesine bağlıdır; göğün açılması yalnızca ilgili sözcük biriminin ayrı karşılığında gösterilir.","branch_kind":"collocation","branch_ref":"root_000400/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:2:1:2","qac_word_ref":"99:2:1","surface_ar":"أَخْرَجَتِ"}],"gloss":"bulutun ilk kez oluşup belirmesi","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bulut, oluşumunun başlangıç evresinde görünür hale gelir."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bulutun doğuş ve ilk görünme evresini anlatan kalıba bağlı kullanım için geçerlidir.","boundary_detail":"Dal bulutun belirmesine bağlıdır; göğün açılması yalnızca ilgili sözcük biriminin ayrı karşılığında gösterilir.","branch_image_ar":"ظهور السحاب وانكشاف السماء","concept_gloss":"bulutun ilk kez oluşup belirmesi","contextual_glosses":[{"applicability":"Gökyüzünde yeni bulutların oluşmaya başladığını anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bulutun ilk oluşumunu ve görünür hale gelişini korur."},"facet_ids":["F001"],"text":"bulut belirmeye başladı","usage_role":"contextual"}],"definition":"Bulutun ilk kez oluşmaya başlaması ve gökyüzünde belirmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bulut, oluşumunun başlangıç evresinde görünür hale gelir."}],"identity_rationale":"Yetkili dal iddiası, bulutun ilk kez oluşup görünmeye başlamasını destekler; göğün buluttan arınması bu iddianın parçası değildir. Bu ikinci anlam yalnızca ayrı bir sözcük biriminde bulunduğundan dal tanımına taşınmamıştır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bulut oluşmaya veya belirmeye başladı"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"gökyüzü bulutlandıktan sonra açıldı"}],"lexicalization_note":"Tanım yalnızca bulut öznesiyle kurulan belirme kalıbını kapsar ve bunu genel bir yalın çıkma anlamına genişletmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bulutun belirmesi ile dağılması arasındaki karşıt süreç en açıklayıcı sınırdır.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal bulutluluğun başlangıç yönünü, komşu ise bulutluluğun ve yağışın sona erme yönünü işaretler; aynı hava durumu ekseninde karşıt aşamalardır.","focus_only":"Odak dal bulutun oluşup görünmeye başlamasını anlatır.","gloss":"bulutun dağılması ve yağışın kesilmesi","neighbor_only":"Komşu dal bulutun dağılmasını, yıldızların görünmesini veya yağışın kesilmesini anlatır.","neighbor_ref":"root_001475/B007","relation_type":"polarity_pair","shared_zone":"İki dal da gökyüzündeki bulutluluk durumunun değişmesini konu alır."}],"source_phrase_ar":"الخروج خروج السحابة (maqayis)؛ الخروج السحاب أول ما يبدأ (ayn)؛ السحاب أول ما ينشأ (sihah)؛ أول ما ينشأ السحاب فهو نشء وقد خرج له خروج حسن (tahdhib)؛ الخرج أيضا من السحاب (mufradat)","source_summary":"Kaynaklar, bulutun oluşumunun ilk aşamasında belirmesi anlamında birleşir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"نشوء السحاب وخروجه، وصحو السماء بعد الإغام","what_is_not_ar":"الخروج من بيت أو بلد؛ الخراج المالي؛ الخرج اللوني"},"support_links":[]},{"boundary":"Dal fiziksel çıkışı anlatmaz; öz kazanımla öne çıkma ve siyasal itaatten ayrılma yüzleri ayrı tutulmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000400/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:2:1:2","qac_word_ref":"99:2:1","surface_ar":"أَخْرَجَتِ"}],"gloss":"yerleşik konumdan ayrılarak öne çıkma veya itaatten kopma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, atalarından gelen bir üstünlük olmadan kendi değeriyle seçkinleşir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"At, seçkin bir soydan gelmediği halde üstün koşu niteliği gösterir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Topluluk, yöneticinin buyruğuna bağlı kalmayıp itaat düzeninin dışına çıkar."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalıtsal ölçüyü aşan seçkinleşme ile siyasal bağlılıktan ayrılma yüzlerini birlikte temsil eder.","boundary_detail":"Dal fiziksel çıkışı anlatmaz; öz kazanımla öne çıkma ve siyasal itaatten ayrılma yüzleri ayrı tutulmalıdır.","branch_image_ar":"خروج عن الأصل أو الطاعة","concept_gloss":"yerleşik konumdan ayrılarak öne çıkma veya itaatten kopma","contextual_glosses":[{"applicability":"Kalıtsal bir üstünlüğü olmadan kendi yeteneğiyle öne çıkan kişi için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kalıtsal dayanak yokluğunu ve kişinin kendi niteliğiyle yükselmesini korur."},"facet_ids":["F001"],"text":"kendi değeriyle seçkinleşen","usage_role":"contextual"},{"applicability":"Bir topluluğun yöneticinin buyruğunu terk ettiği siyasal bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluk katılımcısını ve yönetsel itaatten ayrılma ilişkisini korur."},"facet_ids":["F003"],"text":"itaatten ayrılan topluluk","usage_role":"contextual"}],"definition":"Kalıtsal bir üstünlüğe dayanmadan kendi niteliğiyle benzerlerinden ayrılıp öne çıkmayı anlatır. Başka bir kullanımda, bir topluluğun yöneticinin itaatinden ayrılmasını belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, atalarından gelen bir üstünlük olmadan kendi değeriyle seçkinleşir."},{"facet_id":"F002","role":"example","statement":"At, seçkin bir soydan gelmediği halde üstün koşu niteliği gösterir."},{"facet_id":"F003","role":"extension","statement":"Topluluk, yöneticinin buyruğuna bağlı kalmayıp itaat düzeninin dışına çıkar."}],"identity_rationale":"Kaynak ifadesi, kalıtsal üstünlüğü olmadan kendi değeriyle öne çıkan kişi ve at ile yöneticinin itaatinden ayrılan topluluğu aynı dalda toplar. Bunlar ortak bir yerleşik sınırdan ayrılma görüntüsünü paylaşsa da övgü ve itaatsizlik anlamları birbirine indirgenemez.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kendi değeriyle seçkinleşen kimse"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"soyu seçkin olmadığı halde üstün çıkan at"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yöneticinin itaatinden ayrılan topluluk"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"birinin yeteneğinin ve iş bilirliğinin ortaya çıkması"}],"lexicalization_note":"Kişi, at ve toplulukla kurulan özel kullanımlar ayrı yüzlerdir; bunlardan genel bir yalın çıkma anlamı türetilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; itaatten ayrılma yüzünü taşkın başkaldırıdan ayıran karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal itaatsizliğin kibirli ve taşkın tutumuna odaklanır; odak dalın siyasal yüzü ayrılma ilişkisini adlandırır ve ayrıca övgü bildiren seçkinleşme yüzleri vardır.","focus_only":"Odak dal, itaatten ayrılmanın yanında kalıtsal dayanak olmadan seçkinleşmeyi de kapsar.","gloss":"büyüklük taslayarak itaatten çıkma","neighbor_only":"Komşu dalda itaatsizlik, büyüklük taslama ve sınırı aşan başkaldırı niteliği taşır.","neighbor_ref":"root_000981/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da kabul edilen bir otoriteye bağlılığın terk edilmesi bulunabilir."}],"source_phrase_ar":"الخارجي الرجل المسود بنفسه من غير أن يكون له قديم (maqayis)؛ الخارجي الذي لم يكن له شرف في آبائه فيخرج ويشرف بنفسه (ayn)؛ فرس خارجي إذا خرج جوادا بين مقرفين (jamhara)؛ الخارجية من الخيل التي ليس لها عرق في الجودة فتخرج سوابق (tahdhib)؛ الخوارج خارجين عن طاعة الإمام (mufradat)","source_summary":"Toplu kanıt, kalıtsal ölçüyü kendi niteliğiyle aşma ile siyasal itaatten ayrılmayı ortak bir sınır dışına çıkma görüntüsü altında birleştirir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"من يخرج عن مرتبة أصله أو جماعته، مدحا بالشرف الذاتي أو السبق، أو ذما بالخروج على الطاعة","what_is_not_ar":"مجرد الخروج المكاني؛ الخرج اللوني؛ الخراج المالي"},"support_links":[]},{"boundary":"Renk karşıtlığı çekirdektir; bitki ve yazı örnekleri aynı yer yer değişme örüntüsünün kalıba bağlı uzantılarıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000400/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:2:1:2","qac_word_ref":"99:2:1","surface_ar":"أَخْرَجَتِ"}],"gloss":"iki renkli ya da yer yer kesintili görünüm","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tek bir yüzeyde iki farklı renk, özellikle siyah ve beyaz, birlikte görünür."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bitkili ve çıplak ya da yazılı ve boş alanlar yüzey üzerinde kesintili biçimde dağılır."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Renk karşıtlığını ve farklı dolulukta alanların düzensiz dağılımını birlikte karşılar.","boundary_detail":"Renk karşıtlığı çekirdektir; bitki ve yazı örnekleri aynı yer yer değişme örüntüsünün kalıba bağlı uzantılarıdır.","branch_image_ar":"اختلاف لونين في الشيء","concept_gloss":"iki renkli ya da yer yer kesintili görünüm","contextual_glosses":[{"applicability":"Hayvan veya nesne yüzeyinde iki belirgin rengin birlikte bulunduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aynı varlıkta iki ayrı rengin birlikte bulunmasını korur."},"facet_ids":["F001"],"text":"iki renkli","usage_role":"contextual"},{"applicability":"Bitki, yazı veya benzeri bir kaplamanın bazı yerlerde bulunup bazılarında bulunmadığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dolu ve boş alanların kesintili biçimde dağılmasını korur."},"facet_ids":["F002"],"text":"yer yer boşluklu","usage_role":"contextual"}],"definition":"Bir şeyde iki rengin veya birbirinden farklı görünüşteki alanların yer yer bulunmasıdır. Arazi ve yazı gibi bağlamlarda, dolu ile boş bölümlerin kesintili dağılımı olarak gerçekleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tek bir yüzeyde iki farklı renk, özellikle siyah ve beyaz, birlikte görünür."},{"facet_id":"F002","role":"extension","statement":"Bitkili ve çıplak ya da yazılı ve boş alanlar yüzey üzerinde kesintili biçimde dağılır."}],"identity_rationale":"Kaynak ifadesi iki rengin bir aradalığını, siyahın beyaza baskınlığını, bitkinin yer yer çıkmasını ve yazıda boş bırakılan bölümleri destekler. Dalın çekirdeği yalnızca iki renk değil, dolu ile boş veya farklı görünüşlü alanların kesintili dağılımıdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir işi çeşitlendirme veya yer yer farklılaştırma"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"iki renkli veya kesintili görünüm"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"siyahı beyazından çok olan iki renkli"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"iki renkli dişi hayvan veya iki renkli yer"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"bitkisi yer yer çıkan arazi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"otlağın bir bölümünü yiyip bir bölümünü bıraktı"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"yazı yüzeyinde bazı yerleri boş bıraktı"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"verimli ve verimsiz yerleri bir arada bulunan yıl"}],"lexicalization_note":"Yalın iki renkli görünüm ile arazi, otlak, yazı ve yıl kalıplarındaki kesintili dağılım açıkça ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; iki renk çekirdeğindeki en yakın sınır karşılaştırması yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Renkli varlıklar bakımından yakın anlamlıdırlar; odak dal yüzeydeki kesintili doluluk örüntüsüne uzanırken komşu dal karma hayvan topluluklarına uzanır.","focus_only":"Odak dal, renklerin yanında bitkili ve çıplak ya da yazılı ve boş alanların kesintili dağılımını da kapsar.","gloss":"siyah beyaz veya iki renkli olma","neighbor_only":"Komşu dal iki renkli hayvan ve nesnelerin yanında iki farklı hayvan türünden oluşan karma sürüyü de kapsar.","neighbor_ref":"root_001003/B004","relation_type":"near_synonym","shared_zone":"Her iki dalın merkezinde aynı varlıkta siyah ile beyazın ya da iki rengin birlikte bulunması vardır."}],"source_phrase_ar":"الخرج لونان بين سواد وبياض (maqayis)؛ الأخرج لون سواده أكثر من بياضه (ayn;tahdhib)؛ أرض مخرجة نبتها في مكان دون مكان (ayn;sihah;tahdhib;mufradat)؛ خرج الغلام لوحه إذا ترك فيه مواضع لم يكتبها (tahdhib)","source_summary":"Kaynaklar iki renkli görünümü, baskın siyahı ve arazi ile yazıdaki yer yer dolu veya boş örüntüyü birlikte destekler.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"اختلاف لونين أو تقطع المواضع بين بياض وخضرة أو سواد وبياض، وما شبه به من كتابة وعمل وعام","what_is_not_ar":"الخروج من مكان؛ الخراج المالي؛ الخراج الجسدي"},"support_links":[]},{"boundary":"Dal yalnızca dişi devenin doğuştan erkek deve yapısı göstermesidir; üreme isteği veya genel cinsiyet ayrımı değildir.","branch_kind":"collocation","branch_ref":"root_000400/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:2:1:2","qac_word_ref":"99:2:1","surface_ar":"أَخْرَجَتِ"}],"gloss":"erkek deve yapısında doğmuş dişi deve","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişi deve, yaratılışı bakımından erkek devenin beden biçimini gösterir."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca dişi devenin doğuştan gelen beden biçimini niteleyen özel kullanım için geçerlidir.","boundary_detail":"Dal yalnızca dişi devenin doğuştan erkek deve yapısı göstermesidir; üreme isteği veya genel cinsiyet ayrımı değildir.","branch_image_ar":"خروج الخلقة عن نوعها","concept_gloss":"erkek deve yapısında doğmuş dişi deve","contextual_glosses":[{"applicability":"Bir dişi devenin beden kuruluşunun erkek deveye benzediği anlatımlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dişi özneyi ve erkek deveye benzeyen beden yapısını korur."},"facet_ids":["F001"],"text":"erkek yapılı dişi deve","usage_role":"contextual"}],"definition":"Dişi bir devenin doğuştan erkek devenin beden yapısına sahip olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dişi deve, yaratılışı bakımından erkek devenin beden biçimini gösterir."}],"identity_rationale":"Kaynak ifadesi, dişi devenin erkek devenin beden yapısında doğmuş olmasını doğrudan belirtir. Geçici dal kimliği bu dar hayvan niteliğini eksiksiz yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"erkek deve yapısında doğmuş dişi deve"}],"lexicalization_note":"Tanım dişi deveyle kurulan özel niteleme kalıbına bağlıdır ve genel bir biçim değişikliğine genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; anatomik yapı ile üreme durumu arasındaki alan ayrımı yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Ortaklık yalnızca hayvan ve cinsiyet alanındadır; odak anatomik yapı, komşu ise geçici üreme isteğidir.","focus_only":"Odak dal dişi devenin doğuştan gelen beden yapısını niteler.","gloss":"dişi devenin erkeği istemesi","neighbor_only":"Komşu dal dişi devenin çiftleşme isteğini ve erkeğe yönelmesini anlatır.","neighbor_ref":"root_000009/B012","relation_type":"same_field","shared_zone":"İki dal da dişi deveye özgü bir durumu anlatır."}],"source_phrase_ar":"ناقة مخترجة إذا خرجت على خلقة الجمل (maqayis;ayn;sihah)؛ المخترجة أنها جبلت على خلقة الجمل (tahdhib)","source_summary":"Kaynaklar, dişi devenin erkek deve yapısında doğması biçimindeki dar nitelemede birleşir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"الناقة المخلوقة على خلقة الجمل","what_is_not_ar":"الخروج المكاني؛ الخرج اللوني؛ الخارجي في الشرف أو الطاعة"},"support_links":[]},{"boundary":"Dal bir taşıma kabını anlatır; mali yük, yara ve iki renkli görünüm anlamları dışarıda kalır.","branch_kind":"bare","branch_ref":"root_000400/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:2:1:2","qac_word_ref":"99:2:1","surface_ar":"أَخْرَجَتِ"}],"gloss":"iki gözlü taşıma torbası","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kap, taşımaya yarayan torba biçimindedir ve iki ayrı bölmesi bulunur."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki bölmeli torba biçimindeki somut taşıma kabının genel karşılığıdır.","boundary_detail":"Dal bir taşıma kabını anlatır; mali yük, yara ve iki renkli görünüm anlamları dışarıda kalır.","branch_image_ar":"خرج الوعاء ذو الأونين","concept_gloss":"iki gözlü taşıma torbası","contextual_glosses":[{"applicability":"Yük hayvanında veya elde eşya taşımaya yarayan iki bölmeli torba için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taşıma işlevini ve torbanın iki ayrı gözünü korur."},"facet_ids":["F001"],"text":"iki gözlü yük torbası","usage_role":"general"}],"definition":"Yük veya eşya taşımak için kullanılan, iki ayrı gözü bulunan torba biçiminde bir kaptır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kap, taşımaya yarayan torba biçimindedir ve iki ayrı bölmesi bulunur."}],"identity_rationale":"Kaynak ifadesi, iki bölmeli bir taşıma torbasını ve onun sayı biçimini açıkça tanımlar. Geçici dal kimliği bu somut kap anlamıyla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"iki gözlü taşıma torbası"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"iki gözlü taşıma torbaları"}],"lexicalization_note":"Tanım yalın kap adına bağlıdır ve başka dallardaki eylem ya da nitelik anlamlarını içermez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel torba ile iki bölmeli taşıma kabı arasındaki sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu genel bir torbayı anlatır; odak dal ise yapısal olarak iki bölmeli olan belirli taşıma torbasıdır.","focus_only":"Odak dalın ayırt edici özelliği iki ayrı göze sahip olmasıdır.","gloss":"eşya konan torba","neighbor_only":"Komşu dal, içine istenen şeyin konduğu genel bir torba veya kılıftır.","neighbor_ref":"root_000403/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da içine eşya konup taşınabilen esnek bir kaptır."}],"source_phrase_ar":"الخرج والخرجة جمعه جوالق ذو أونين (ayn)؛ الخرج من الأوعية معروف والجمع خرجة (sihah)؛ الخرج هذا الوعاء ثلاثة خرجة وهو جوالق ذو أونين (tahdhib)","source_summary":"Kaynaklar, iki gözlü torba biçimindeki taşıma kabı ve onun çoğul kullanımı üzerinde birleşir.","sources":["AY","SI","TA"],"what_is_ar":"الوعاء الجوالق ذو الأونين","what_is_not_ar":"الإتاوة؛ الدمل؛ اختلاف اللونين"},"support_links":[]},{"boundary":"Dal geleneksel oyunun kimliğini taşır; ayrıntılı oyun düzeni dal tanımının kurucu parçası sayılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000400/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:2:1:2","qac_word_ref":"99:2:1","surface_ar":"أَخْرَجَتِ"}],"gloss":"özel çağrılı geleneksel çocuk oyunu","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Oyun, erkek çocuklar arasında oynanır ve kendine özgü yinelenen bir çağrıyla tanınır."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kuralları ayrıntılandırılmayan, erkek çocuklara özgü geleneksel oyunun kısa karşılığıdır.","boundary_detail":"Dal geleneksel oyunun kimliğini taşır; ayrıntılı oyun düzeni dal tanımının kurucu parçası sayılmaz.","branch_image_ar":"لعبة إخراج ما في اليد","concept_gloss":"özel çağrılı geleneksel çocuk oyunu","contextual_glosses":[{"applicability":"Oyunun özgün adı yerine kaynakça desteklenen genel açıklama gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çocuk oyunu oluşunu ve ayırt edici çağrı unsurunu korur."},"facet_ids":["F001"],"text":"çağrıyla oynanan çocuk oyunu","usage_role":"explanatory"}],"definition":"Erkek çocukların oynadığı ve oyun sırasında yinelenen özel bir çağrıyla tanınan geleneksel bir oyundur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Oyun, erkek çocuklar arasında oynanır ve kendine özgü yinelenen bir çağrıyla tanınır."}],"identity_rationale":"Dal iddiası, erkek çocukların oynadığı ve belirli bir çağrıyla anılan geleneksel bir oyunu doğrular; ancak oyunun kuralları dal düzeyindeki kaynak ifadesinde açıklanmaz. Eldekini çıkartma açıklaması bu nedenle yalnızca ilgili sözcük biriminin karşılığında korunmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"erkek çocukların oynadığı geleneksel oyun"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"çocukların oynadığı geleneksel oyun"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"oyunda eldekini çıkarmayı isteyen çağrı"}],"lexicalization_note":"Oyun adları ile oyun içi çağrı ayrı sözcük birimleridir; bunlardan yalın çıkma anlamı üretilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; komşu oyun kartları kuralları açıklamadığından güvenilir bir anlam sınırı yayımlanmadı.","source_phrase_ar":"الخريج لعبة لفتيان العرب يقال فيها خراج خراج (maqayis;sihah)؛ الخراج والخريج مخارجة لعبة لفتيان العرب (ayn)؛ الخراج لعبة يلعب بها الصبيان (jamhara)؛ خراج اسم لعبة لهم معروفة (tahdhib)","source_summary":"Kaynaklar, erkek çocukların oynadığı ve özel bir oyun çağrısıyla anılan geleneksel oyun kimliğinde birleşir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"لعبة الخراج والخريج التي يطلب فيها إخراج ما في اليد","what_is_not_ar":"الخراج المالي؛ الخراج الجسدي؛ الخروج المكاني"},"support_links":[]},{"boundary":"Dal yalnızca uyak yapısındaki belirli son sesi anlatır; genel çıkma eylemiyle ilişkili değildir.","branch_kind":"bare","branch_ref":"root_000400/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:2:1:2","qac_word_ref":"99:2:1","surface_ar":"أَخْرَجَتِ"}],"gloss":"uyakta bağlantı sesinden sonraki elif harfi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Elif harfi, uyak dizisinde bağlantı sesinin hemen ardından yer alır."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Şiir ölçüsü ve uyak çözümlemesinde bağlantı sesini izleyen elif için kullanılır.","boundary_detail":"Dal yalnızca uyak yapısındaki belirli son sesi anlatır; genel çıkma eylemiyle ilişkili değildir.","branch_image_ar":"ألف الخروج بعد الصلة","concept_gloss":"uyakta bağlantı sesinden sonraki elif harfi","contextual_glosses":[{"applicability":"Teknik terimin elif harfi oluşu ve uyaktaki yeri kısa biçimde açıklanırken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uyak alanını, elif harfini ve bağlantı sesinin ardından gelme koşulunu korur."},"facet_ids":["F001"],"text":"uyak sonunda bağlantı sesini izleyen elif","usage_role":"explanatory"}],"definition":"Şiir uyağında bağlantı sesinden sonra gelen elif harfidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Elif harfi, uyak dizisinde bağlantı sesinin hemen ardından yer alır."}],"identity_rationale":"Kaynak ifadesi, uyakta bağlantı sesinden sonra gelen elif harfini açık ve tek bir teknik görevle tanımlar. Geçici dal çerçevesi bu konumu doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"uyakta bağlantı sesinden sonra gelen elif harfi"}],"lexicalization_note":"Tanım yalın bir şiir ve uyak terimine bağlıdır; başka teknik ses konumları buraya katılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; uyak içindeki konumu farklı olan en yakın teknik ses öğesiyle karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak öğe elif harfidir ve bağlantı sesinden sonra gelir; komşu öğe ise uyak harfinden önce bulunur. Ses dizisindeki konumları ve görevleri farklıdır.","focus_only":"Odak dal, bağlantı sesinden sonra gelen elif harfidir.","gloss":"uyak harfinden önceki uzun veya kayıcı ses","neighbor_only":"Komşu dal, uyak harfinden önce bulunan hareketsiz bir uzun veya kayıcı sestir.","neighbor_ref":"root_000556/B006","relation_type":"same_field","shared_zone":"İki dal da şiir uyağında belirli konumu olan ses öğeleridir."}],"source_phrase_ar":"الخروج الألف التي بعد الصلة في القافية (ayn;tahdhib)","source_summary":"Kaynaklar, uyakta bağlantı sesinden sonra gelen elif harfinin teknik adı üzerinde birleşir.","sources":["AY","TA"],"what_is_ar":"ألف الخروج في القافية بعد الصلة","what_is_not_ar":"الخروج المكاني؛ الإخراج؛ الخرج المالي"},"support_links":[]},{"boundary":"Dal tek yanlı vergi veya ödeme değildir; ortak hak sahipleri arasında karşılıklı bölüşme ve tasfiye gerektirir.","branch_kind":"mixed_non_bare","branch_ref":"root_000400/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:2:1:2","qac_word_ref":"99:2:1","surface_ar":"أَخْرَجَتِ"}],"gloss":"ortak payları karşılıklı bölüşüp tasfiye etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Taraflar ortak değer üzerinde karşılıklı katkıda bulunur, bölüşür veya hesaplaşır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ortaklar veya mirasçılar malı, alacağı ve payları denkleştirerek ortak ilişkiden ayrılır."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Karşılıklı katkıdan ortaklık veya miras paylarının anlaşmalı tasfiyesine uzanan çekirdeği karşılar.","boundary_detail":"Dal tek yanlı vergi veya ödeme değildir; ortak hak sahipleri arasında karşılıklı bölüşme ve tasfiye gerektirir.","branch_image_ar":"تخارج الشركاء في النصيب","concept_gloss":"ortak payları karşılıklı bölüşüp tasfiye etme","contextual_glosses":[{"applicability":"Ortakların veya mirasçıların paylarını anlaşmayla ayırdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı anlaşmayı, pay ayrımını ve ortak ilişkinin sona ermesini korur."},"facet_ids":["F002"],"text":"paylaşıp ortaklıktan ayrılmak","usage_role":"contextual"},{"applicability":"Tarafların ortak değere katkı verip bunu aralarında paylaştığı genel bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Birden çok tarafı, karşılıklı katkıyı ve bölüşme işlemini korur."},"facet_ids":["F001"],"text":"karşılıklı katkı ve bölüşme","usage_role":"explanatory"}],"definition":"Birden çok hak sahibinin ortak değerleri karşılıklı katkı ve bölüşmeyle düzenlemesidir. Ortaklar veya mirasçılar bakımından pay, mal ve alacakları anlaşarak denkleştirip ortak ilişkiden ayrılmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Taraflar ortak değer üzerinde karşılıklı katkıda bulunur, bölüşür veya hesaplaşır."},{"facet_id":"F002","role":"specialization","statement":"Ortaklar veya mirasçılar malı, alacağı ve payları denkleştirerek ortak ilişkiden ayrılır."}],"identity_rationale":"Kaynak ifadesi, karşılıklı katkı ve bölüşme ile ortakların veya mirasçıların mal, alacak ve paylar üzerinde anlaşarak ayrılmasını destekler. Geçici çerçeve bu karşılıklı hesaplaşma alanını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"karşılıklı katkı ve bölüşme"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"ortakların veya mirasçıların paylarını tasfiye etmesi"},{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"iki ortağın mal ve alacak üzerinde karşılıklı hesaplaşması"}],"lexicalization_note":"Genel karşılıklı katkı ve bölüşme, ortaklık ile miras tasfiyesine bağlı özel kalıplardan ayrı gösterilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel ortak ayrışması ile payların karşılıklı tasfiyesi arasındaki sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu daha genel bir ortak ayrışmasıdır; odak dal karşılıklı katkı, miras payı, mal ve alacak gibi belirli tasfiye ilişkilerini birlikte taşır.","focus_only":"Odak dal karşılıklı katkıyı ve ortaklar ya da mirasçılar arasında mal ile alacağın tasfiyesini açıkça kapsar.","gloss":"ortakla ayrışma veya bölüşme","neighbor_only":"Komşu dal, ortak bir işteki ortağın genel olarak ayrılması, paylaştırılması veya eşitlenmesidir.","neighbor_ref":"root_001159/B014","relation_type":"near_synonym","shared_zone":"Her iki dal da ortak bir değer veya ilişki üzerinde tarafların ayrışmasını ve hesaplaşmasını anlatır."}],"source_phrase_ar":"المخارجة المناهدة بالأصابع والتخارج التناهد (sihah)؛ يتخارج الشريكان وأهل الميراث (tahdhib)؛ لا بأس أن يتخارجا يعني العين والدين (tahdhib)","source_summary":"Kaynaklar karşılıklı katkı ve bölüşme çekirdeğini, ortaklar ile mirasçıların mal ve alacak üzerindeki uzlaşmalı tasfiyesine bağlar.","sources":["SI","TA"],"what_is_ar":"تخارج الشركاء أو الورثة، والمخارجة بمعنى المناهدة والمقاسمة","what_is_not_ar":"الخراج المالي المفروض؛ الخروج المكاني؛ لعبة الخراج"},"support_links":[]},{"boundary":"Dal yalnızca atın uzun boyunlu oluşuna bağlı nitelemedir; genel uzunluk veya fiziksel çıkış anlamı değildir.","branch_kind":"non_bare","branch_ref":"root_000400/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:2:1:2","qac_word_ref":"99:2:1","surface_ar":"أَخْرَجَتِ"}],"gloss":"uzun boyunlu at niteliği","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"At, belirgin biçimde uzun bir boyna sahiptir."}}],"root_ar":"خ ر ج","root_id":"root_000400","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca atın belirgin boyun uzunluğunu anlatan özel nitelemede kullanılır.","boundary_detail":"Dal yalnızca atın uzun boyunlu oluşuna bağlı nitelemedir; genel uzunluk veya fiziksel çıkış anlamı değildir.","branch_image_ar":"عنق خارج يغتال العنان","concept_gloss":"uzun boyunlu at niteliği","contextual_glosses":[{"applicability":"Atın belirgin boyun uzunluğunu açıklayan betimleyici bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Atı ve belirgin boyun uzunluğunu korur."},"facet_ids":["F001"],"text":"uzun boyunlu at","usage_role":"explanatory"}],"definition":"Atın uzun boyunlu oluşunu belirten özel bir niteliktir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"At, belirgin biçimde uzun bir boyna sahiptir."}],"identity_rationale":"Kaynak ifadesi, atın boynunun uzun oluşunu belirli bir at niteliği olarak doğrular; dizginin erişimini aşma ayrıntısı ise yalnızca ilgili sözcük biriminin karşılığında korunur.","lexical_glosses":[{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"uzun boynuyla dizginin erişimini aşan at"}],"lexicalization_note":"Tanım at niteliği olarak sözlükselleşmiş özel kullanıma bağlıdır ve yalın kök anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel at niteliği ile genel uzunluk alanı arasındaki karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak yalnızca atın uzun boyunlu oluşuna bağlı bir niteliktir; komşu ise farklı nesne ve beden ölçülerine yayılan genel uzunluk alanıdır.","focus_only":"Odak dal yalnızca atın belirgin boyun uzunluğunu anlatır.","gloss":"uzunluk, uzaklık ve el erişimi","neighbor_only":"Komşu dal genel uzaklık, boy uzunluğu ve kol uzatılarak ölçülen erişim mesafesini kapsar.","neighbor_ref":"root_000116/B011","relation_type":"same_field","shared_zone":"Her iki dal da belirgin bir uzunluk niteliğini konu alır."}],"source_phrase_ar":"الخروج من صفات الخيل وهو الذي يطول عنقه (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tekil tanıklık, uzun boyunlu at niteliğini tanımlar."}],"source_summary":"Dal, at anatomisine bağlı dar bir uzun boyun nitelemesi olarak anlaşılır.","sources":["TA"],"what_is_ar":"الخيل الطويلة الأعناق التي تغتال كل عنان","what_is_not_ar":"الخارجي في الشرف؛ الخرج اللوني؛ الخروج المكاني"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["99:2:1"],"branch_refs":[],"candidate_id":"cand_51de3e89dd1b9bafd4cb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:2:1:bound-sequel","source_type":"word_analysis","support_ids":["sup_4da0da27887d64331794","sup_f754f495088e02ee4fcb"],"title":"connector makes expulsion a bound sequel","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:1","qac_refs":["99:2:1:1"],"status":"accepted"}},{"anchor_refs":["99:2:1"],"branch_refs":[],"candidate_id":"cand_bb5896cdd9f4eff8a773","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:2:1:fused-surface-onset","source_type":"word_analysis","support_ids":["sup_4da0da27887d64331794","sup_66039d6b14c4155a3a3b"],"title":"clitic fusion makes the transition audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:1","qac_refs":["99:2:1:1"],"status":"accepted"}},{"anchor_refs":["99:2:1"],"branch_refs":[],"candidate_id":"cand_da1cf2eadf06179bfda3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:2:1:opening-hinge","source_type":"word_analysis","support_ids":["sup_4da0da27887d64331794","sup_f63352c90f95845c67a4"],"title":"ayah begins with a hinge, not a new subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:1","qac_refs":["99:2:1:1"],"status":"accepted"}},{"anchor_refs":["99:2:2"],"branch_refs":[],"candidate_id":"cand_fd57a70c9f1aa977ebf7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000400"],"scope":"focus_ayah","source_local_id":"99:2:2:causative-extraction","source_type":"word_analysis","support_ids":["sup_2d2b17491236b0d0f24b","sup_d07217053bc5ee602b5a"],"title":"Form IV selects causative extraction","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:2","qac_refs":["99:2:1:2"],"status":"accepted"}},{"anchor_refs":["99:2:2"],"branch_refs":[],"candidate_id":"cand_0183144eccc288a07439","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000400"],"scope":"focus_ayah","source_local_id":"99:2:2:completed-event","source_type":"word_analysis","support_ids":["sup_22a18670d3afb27496d5","sup_d07217053bc5ee602b5a"],"title":"perfect aspect makes expulsion an accomplished stage","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:2","qac_refs":["99:2:1:2"],"status":"accepted"}},{"anchor_refs":["99:2:2"],"branch_refs":[],"candidate_id":"cand_5daffd2e421d61c4ac2d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000400"],"scope":"focus_ayah","source_local_id":"99:2:2:earth-agency-agreement","source_type":"word_analysis","support_ids":["sup_c15b27fd18b6e97abe9e","sup_d07217053bc5ee602b5a"],"title":"agreement routes agency through the earth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:2","qac_refs":["99:2:1:2"],"status":"accepted"}},{"anchor_refs":["99:2:2"],"branch_refs":[],"candidate_id":"cand_42d3aa894cdcdc21ae6b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000400"],"scope":"focus_ayah","source_local_id":"99:2:2:earth-emergence-recast","source_type":"word_analysis","support_ids":["sup_50b8ca0904035ac982a4","sup_d07217053bc5ee602b5a"],"title":"earth-emergence field is recast as burden exposure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:2","qac_refs":["99:2:1:2"],"status":"accepted"}},{"anchor_refs":["99:2:2"],"branch_refs":[],"candidate_id":"cand_5797f5025be564063084","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000400"],"scope":"focus_ayah","source_local_id":"99:2:2:extraction-disclosure-range","source_type":"word_analysis","support_ids":["sup_47b614e3172b9e33175a","sup_d07217053bc5ee602b5a"],"title":"emergence range narrows to disclosure from within","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:2","qac_refs":["99:2:1:2"],"status":"accepted"}},{"anchor_refs":["99:2:2"],"branch_refs":[],"candidate_id":"cand_c1325c526d2146762893","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000400"],"scope":"focus_ayah","source_local_id":"99:2:2:sound-texture","source_type":"word_analysis","support_ids":["sup_00296dcc57d336b72499","sup_d07217053bc5ee602b5a"],"title":"rough onset suits forceful extraction","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:2","qac_refs":["99:2:1:2"],"status":"accepted"}},{"anchor_refs":["99:2:2"],"branch_refs":[],"candidate_id":"cand_8388d5bfec29480aeb72","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000400"],"scope":"focus_ayah","source_local_id":"99:2:2:verb-first-boundary-pivot","source_type":"word_analysis","support_ids":["sup_88a4bdad1227cb353e31","sup_d07217053bc5ee602b5a"],"title":"verb-first clause turns continuation into action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:2","qac_refs":["99:2:1:2"],"status":"accepted"}},{"anchor_refs":["99:2:3"],"branch_refs":[],"candidate_id":"cand_3ae9b146b2e63f7bb9b7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:2:3:earth-collocation-recast","source_type":"word_analysis","support_ids":["sup_28d4ecc9dd257546fd25","sup_2e768e10e2835476366c"],"title":"earth pairings are recast locally","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:3","qac_refs":["99:2:2:1","99:2:2:2"],"status":"accepted"}},{"anchor_refs":["99:2:3"],"branch_refs":[],"candidate_id":"cand_b1497090834f7f8caef4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:2:3:known-earth-role-reversal","source_type":"word_analysis","support_ids":["sup_28d4ecc9dd257546fd25","sup_ab7c359898b6d76e6ced"],"title":"known earth changes from patient to agent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:3","qac_refs":["99:2:2:1","99:2:2:2"],"status":"accepted"}},{"anchor_refs":["99:2:3"],"branch_refs":[],"candidate_id":"cand_c84e36c335dae869e686","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:2:3:sound-and-subject-entry","source_type":"word_analysis","support_ids":["sup_28d4ecc9dd257546fd25","sup_f6dafadb1592ae677747"],"title":"sound marks the subject's entry","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:3","qac_refs":["99:2:2:1","99:2:2:2"],"status":"accepted"}},{"anchor_refs":["99:2:3"],"branch_refs":[],"candidate_id":"cand_5d1d0ae94e05c9e82d5c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:2:3:subject-and-antecedent","source_type":"word_analysis","support_ids":["sup_066bfaafadbf5f06bbb0","sup_28d4ecc9dd257546fd25"],"title":"earth is subject and pronoun antecedent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:3","qac_refs":["99:2:2:1","99:2:2:2"],"status":"accepted"}},{"anchor_refs":["99:2:3"],"branch_refs":[],"candidate_id":"cand_47b459a635ac8bf02c41","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:2:3:substrate-range","source_type":"word_analysis","support_ids":["sup_28d4ecc9dd257546fd25","sup_bf909f0eb08af446bf5d"],"title":"earth range narrows to containing substrate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:3","qac_refs":["99:2:2:1","99:2:2:2"],"status":"accepted"}},{"anchor_refs":["99:2:3"],"branch_refs":[],"candidate_id":"cand_7be7ac35db7920d07599","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:2:3:visible-bearer-turned-expeller","source_type":"word_analysis","support_ids":["sup_28d4ecc9dd257546fd25","sup_c96594af982444b11016"],"title":"container becomes visible expeller","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:3","qac_refs":["99:2:2:1","99:2:2:2"],"status":"accepted"}},{"anchor_refs":["99:2:4"],"branch_refs":[],"candidate_id":"cand_4686d03113c2bbdb5cd6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"99:2:4:closure-and-sound","source_type":"word_analysis","support_ids":["sup_3c95b2f48bb25740ad63","sup_8c30a8c81333951f1929"],"title":"closure gives the burdens maximum weight","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:4","qac_refs":["99:2:3:1","99:2:3:2"],"status":"accepted"}},{"anchor_refs":["99:2:4"],"branch_refs":[],"candidate_id":"cand_43e16616bd0b5974ee88","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"99:2:4:concrete-plural-loads","source_type":"word_analysis","support_ids":["sup_0c80f49326d0cd9ddb58","sup_8c30a8c81333951f1929"],"title":"plural form turns heaviness into concrete loads","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:4","qac_refs":["99:2:3:1","99:2:3:2"],"status":"accepted"}},{"anchor_refs":["99:2:4"],"branch_refs":[],"candidate_id":"cand_e5b2d82daf8422563467","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"99:2:4:direct-object-completion","source_type":"word_analysis","support_ids":["sup_8c30a8c81333951f1929","sup_99ee6d02d358e7ec05b5"],"title":"object names what the verb expels","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:4","qac_refs":["99:2:3:1","99:2:3:2"],"status":"accepted"}},{"anchor_refs":["99:2:4"],"branch_refs":[],"candidate_id":"cand_eaf2879f3d6c4c26a9fa","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"99:2:4:earth-owned-pronoun-circuit","source_type":"word_analysis","support_ids":["sup_68f642fdeb1850614fdf","sup_8c30a8c81333951f1929"],"title":"suffix makes the burdens earth-owned","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:4","qac_refs":["99:2:3:1","99:2:3:2"],"status":"accepted"}},{"anchor_refs":["99:2:4"],"branch_refs":[],"candidate_id":"cand_be680927d2942481daaa","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"99:2:4:marked-extraction-of-heaviness","source_type":"word_analysis","support_ids":["sup_7dd1401f0f991e05afc0","sup_8c30a8c81333951f1929"],"title":"extraction is aimed at weight-bearing contents","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:4","qac_refs":["99:2:3:1","99:2:3:2"],"status":"accepted"}},{"anchor_refs":["99:2:4"],"branch_refs":[],"candidate_id":"cand_b10a98b08766e919e4e7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"99:2:4:polyvalent-heavy-contents","source_type":"word_analysis","support_ids":["sup_191d44f7c925e66a8e89","sup_8c30a8c81333951f1929"],"title":"burden senses gather as disclosure payload","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:4","qac_refs":["99:2:3:1","99:2:3:2"],"status":"accepted"}},{"anchor_refs":["99:2:4"],"branch_refs":[],"candidate_id":"cand_010031890d1c6f8432a7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"99:2:4:pregnancy-delivery-image","source_type":"word_analysis","support_ids":["sup_16caefba574ea7240a0a","sup_8c30a8c81333951f1929"],"title":"pregnancy heaviness adds delivery pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:4","qac_refs":["99:2:3:1","99:2:3:2"],"status":"accepted"}},{"anchor_refs":["99:2:4"],"branch_refs":[],"candidate_id":"cand_fa57fc4a46273989196a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"99:2:4:weight-thread-to-measure","source_type":"word_analysis","support_ids":["sup_3cc6229dcefc06412351","sup_8c30a8c81333951f1929"],"title":"macro-burdens anticipate micro-weight","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:2:4","qac_refs":["99:2:3:1","99:2:3:2"],"status":"accepted"}},{"anchor_refs":["99:2:1"],"branch_refs":[],"candidate_id":"cand_1c2643c673d1dc1d7cf7","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000400"],"scope":"focus_ayah","source_local_id":"99:2:1:2","source_type":"qac_morpheme","support_ids":["sup_5b4a25a8830cfd8bff5d"],"title":"QAC root occurrence: خ ر ج","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["99:2:2"],"branch_refs":[],"candidate_id":"cand_7598f9bb2a6f8378adea","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000025"],"scope":"focus_ayah","source_local_id":"99:2:2:2","source_type":"qac_morpheme","support_ids":["sup_f9c29f9e4e16e893a217"],"title":"QAC root occurrence: ء ر ض","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["99:2:3"],"branch_refs":[],"candidate_id":"cand_a1b51dfe96ceecbdb28f","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"99:2:3:1","source_type":"qac_morpheme","support_ids":["sup_03427810945742c3963d"],"title":"QAC root occurrence: ث ق ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["99:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"99:2","branch_refs":["root_000025/B001","root_000202/B001","root_000400/B002"],"candidate_id":"cand_fd4bbfaa69ddab402681","commentary_obligation":"review","hft_ref":"hft_f30a811b936c5671875e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_physical_extraction","source_type":"hft","support_ids":["sup_d17130fa1cecf805d0ab"],"title":"b_physical_extraction","trust":"legacy_unbound"},{"anchor_refs":["99:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"99:2","branch_refs":["root_000025/B002","root_000202/B004","root_000202/B005","root_000400/B003"],"candidate_id":"cand_3084439aee38e29309b3","commentary_obligation":"review","hft_ref":"hft_03e5f0687583280e2e5d","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_assessed_yield","source_type":"hft","support_ids":["sup_8b6e75f36708cb4fb7a9"],"title":"b_assessed_yield","trust":"legacy_unbound"},{"anchor_refs":["99:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"99:2","branch_refs":["root_000025/B002","root_000202/B007","root_000400/B002"],"candidate_id":"cand_53710bdd9cdb1fc279bf","commentary_obligation":"review","hft_ref":"hft_3dfc3358077883e1f4fa","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_gravid_delivery","source_type":"hft","support_ids":["sup_82bbad2e93d869d8e71f"],"title":"b_gravid_delivery","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"99:2:1:1","qac_word_ref":"99:2:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:2:1:2","qac_word_ref":"99:2:1","root_ar":"خ ر ج","surface_ar":"أَخْرَجَتِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"99:2:2:1","qac_word_ref":"99:2:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:2:2","qac_word_ref":"99:2:2","root_ar":"ء ر ض","surface_ar":"أَرْضُ"},{"lemma_ar":"ثَّقَلَان","morph_features":"STEM|POS:N|LEM:v~aqalaAn|ROOT:vql|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:3:1","qac_word_ref":"99:2:3","root_ar":"ث ق ل","surface_ar":"أَثْقَالَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"99:2:3:2","qac_word_ref":"99:2:3","root_ar":"","surface_ar":"هَا"}],"word_analysis_qac_refs":[["99:2:1:1"],["99:2:1:2"],["99:2:2:1","99:2:2:2"],["99:2:3:1","99:2:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["99:2:1","99:2:2","99:2:3","99:2:4"]},"focus_surface_evidence":{"arabic_uthmani":"وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"99:2:1:1","qac_word_ref":"99:2:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"أَخْرَجَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:2:1:2","qac_word_ref":"99:2:1","root_ar":"خ ر ج","surface_ar":"أَخْرَجَتِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"99:2:2:1","qac_word_ref":"99:2:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:2:2","qac_word_ref":"99:2:2","root_ar":"ء ر ض","surface_ar":"أَرْضُ"},{"lemma_ar":"ثَّقَلَان","morph_features":"STEM|POS:N|LEM:v~aqalaAn|ROOT:vql|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:2:3:1","qac_word_ref":"99:2:3","root_ar":"ث ق ل","surface_ar":"أَثْقَالَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"99:2:3:2","qac_word_ref":"99:2:3","root_ar":"","surface_ar":"هَا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["99:2:1:1"],["99:2:1:2"],["99:2:2:1","99:2:2:2"],["99:2:3:1","99:2:3:2"]],"word_analysis_refs":["99:2:1","99:2:2","99:2:3","99:2:4"],"word_rows":[{"analysis_record_ref":"99:2:1","analytic_gloss_range_en":"opening conjunction with boundary-continuation force, linking the prior shaking to the expulsion as a bound sequel within the same scene","analytic_root_gloss_range_en":null,"qac_refs":["99:2:1:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"99:2:2","analytic_gloss_range_en":"completed causative bringing-out by the earth, locally selecting extraction and disclosure of its own heavy contents rather than simple emergence","analytic_root_gloss_range_en":"broad root range around going out, causing to come out, output, eruption, and other branch-specific extensions; this ayah selects the Form IV causative extraction branch","qac_refs":["99:2:1:2"],"root":{"arabic":"خ ر ج","transliteration":"kh-r-j"},"surface":{"arabic":"أَخْرَجَتِ","transliteration":"akhrajat"}},{"analysis_record_ref":"99:2:3","analytic_gloss_range_en":"the definite earth or ground as the same known terrestrial substrate from 99:1, now functioning as explicit subject and possessor of what is expelled","analytic_root_gloss_range_en":"earth, ground, land, territory, lower surface, and substrate; this ayah selects the known containing ground as acting subject","qac_refs":["99:2:2:1","99:2:2:2"],"root":{"arabic":"أ ر ض","transliteration":"ʾ-r-ḍ"},"surface":{"arabic":"ٱلْأَرْضُ","transliteration":"al-arḍu"}},{"analysis_record_ref":"99:2:4","analytic_gloss_range_en":"the earth's possessed heavy loads or contents, concrete and plural, with room for buried bodies, deposits, and disclosure-laden burdens while remaining the direct object of expulsion","analytic_root_gloss_range_en":"heaviness, loads, burdens, earth contents, moral liabilities, measured weight, worth, sluggishness, and pregnancy heaviness; this ayah selects concrete possessed loads with disclosure and later weight-measure resonance","qac_refs":["99:2:3:1","99:2:3:2"],"root":{"arabic":"ث ق ل","transliteration":"th-q-l"},"surface":{"arabic":"أَثْقَالَهَا","transliteration":"athqālahā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["99:2"],"branch_refs":["root_000025/B001","root_000202/B001","root_000400/B002"],"candidate_id":"cand_fd4bbfaa69ddab402681","evidence_scope":"focus_ayah","hft_ref":"hft_f30a811b936c5671875e","item_id":"b_physical_extraction","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_physical_extraction","support_id":"sup_d17130fa1cecf805d0ab"},{"anchor_refs":["99:2"],"branch_refs":["root_000025/B002","root_000202/B004","root_000202/B005","root_000400/B003"],"candidate_id":"cand_3084439aee38e29309b3","evidence_scope":"focus_ayah","hft_ref":"hft_03e5f0687583280e2e5d","item_id":"b_assessed_yield","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_assessed_yield","support_id":"sup_8b6e75f36708cb4fb7a9"},{"anchor_refs":["99:2"],"branch_refs":["root_000025/B002","root_000202/B007","root_000400/B002"],"candidate_id":"cand_53710bdd9cdb1fc279bf","evidence_scope":"focus_ayah","hft_ref":"hft_3dfc3358077883e1f4fa","item_id":"b_gravid_delivery","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_gravid_delivery","support_id":"sup_82bbad2e93d869d8e71f"}],"diagnostics":[],"lane_counts":{"global":7,"macro":11,"micro":3},"packet_summary":{"ayah_count":8,"focus_ref":"99:2","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ذ ر ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000511","furuq_root_norm":"ذ ر ر","furuq_source_root_norm":"ذ ر ر","is_dominant":true,"target_occurrences":2,"target_rank":1}]},{"qac_root":"ش ر ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000787","furuq_root_norm":"ش ر ر","furuq_source_root_norm":"ش ر ر","is_dominant":true,"target_occurrences":19,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000792","furuq_root_norm":"ش ر ي","furuq_source_root_norm":"ش ر ي","is_dominant":false,"target_occurrences":11,"target_rank":2}]}],"window":["99:1","99:2","99:3","99:4","99:5","99:6","99:7","99:8"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"99:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":7,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"99:2","lane":"micro","linguistic_source_ref":"99:2","surface_ref":"99:2","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"99:2","target_tokens":[["Ve",["99:2:1"]],["yer",["99:2:2"]],["ağırlıklarını",["99:2:3"]],["dışarı",["99:2:1"]],["çıkardığında",["99:2:1"]]],"text":"Ve yer ağırlıklarını dışarı çıkardığında,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":8,"id":"s099-p01-001-008","label":"Whole surah","number":1,"refs":["99:1","99:2","99:3","99:4","99:5","99:6","99:7","99:8"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:2:sound-texture","source_type":"word_analysis","support_id":"sup_00296dcc57d336b72499","text":"{\"blocking_evidence\":null,\"headline\":\"rough onset suits forceful extraction\",\"reader_payoff\":\"The reader notices a sharp audible launch from the light connector into the forceful extraction verb.\",\"reason\":\"The local surface begins with hamza after the connector and includes the guttural consonant named by the phonetic rows.\",\"representative_source_ids\":[\"QF-399dc0ec\",\"QP-35687e70\",\"QP-e7bd62cb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"99:2:3:1","source_type":"qac_morpheme","support_id":"sup_03427810945742c3963d","text":"{\"lemma_ar\":\"ثَّقَلَان\",\"morph_features\":\"STEM|POS:N|LEM:v~aqalaAn|ROOT:vql|MP|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"99:2:3:1\",\"qac_word_ref\":\"99:2:3\",\"root_ar\":\"ث ق ل\",\"surface_ar\":\"أَثْقَالَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:3:subject-and-antecedent","source_type":"word_analysis","support_id":"sup_066bfaafadbf5f06bbb0","text":"{\"blocking_evidence\":null,\"headline\":\"earth is subject and pronoun antecedent\",\"reader_payoff\":\"The reader notices that the earth is both the grammatical actor and the referent to which the final possessive suffix returns.\",\"reason\":\"Attachment evidence marks the word as the explicit subject of the verb and the suffix in {{ar:أَثْقَالَهَا}} ({{tr:athqālaha}}) as possessed by the same feminine referent.\",\"representative_source_ids\":[\"QG-1bd859de\",\"QG-23451942\",\"QG-ef69d786\",\"MG-492354ad\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:4:concrete-plural-loads","source_type":"word_analysis","support_id":"sup_0c80f49326d0cd9ddb58","text":"{\"blocking_evidence\":null,\"headline\":\"plural form turns heaviness into concrete loads\",\"reader_payoff\":\"The reader notices heaviness as multiple concrete loads or contents, not merely as the abstract idea of weight.\",\"reason\":\"The local noun is a concrete plural object, and V4 supports a branch for loads and earth contents.\",\"representative_source_ids\":[\"MG-a208f5d1\",\"QF-8c24db35\",\"QF-9e92a68d\",\"QF-c3b81068\",\"QI-9b3f1b09\",\"QH-78f874e0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:4:pregnancy-delivery-image","source_type":"word_analysis","support_id":"sup_16caefba574ea7240a0a","text":"{\"blocking_evidence\":null,\"headline\":\"pregnancy heaviness adds delivery pressure\",\"reader_payoff\":\"The reader notices a delivery-like image: the earth had carried heaviness and now brings it out, while the local noun remains heavy contents rather than a literal pregnancy term.\",\"reason\":\"V4 includes pregnancy becoming heavy as an accepted {{ar:ث ق ل}} ({{tr:th-q-l}}) branch, and the CRITICAL row gives 7:189 as an echo; local grammar narrows this to image-pressure on the earth's carried contents.\",\"representative_source_ids\":[\"QS-13f0f762\",\"QI-46fb0e41\",\"MI-fb0f1590\",\"QE-bc0dff16\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:4:polyvalent-heavy-contents","source_type":"word_analysis","support_id":"sup_191d44f7c925e66a8e89","text":"{\"blocking_evidence\":null,\"headline\":\"burden senses gather as disclosure payload\",\"reader_payoff\":\"The reader notices that the word can hold physical loads, buried bodies, deposits, and disclosure-laden contents together while the clause keeps them tied to the earth.\",\"reason\":\"V4 supports loads and earth contents as a local branch, and moral or archival burden pressure is narrowed by the direct-object and possessive frame rather than treated as a replacement for concrete contents.\",\"representative_source_ids\":[\"QS-1082d0e8\",\"QS-e2470d37\",\"QS-f557a201\",\"MS-fbfba9c5\",\"QB-e1fbd53f\",\"QY-2e155c99\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:2:completed-event","source_type":"word_analysis","support_id":"sup_22a18670d3afb27496d5","text":"{\"blocking_evidence\":null,\"headline\":\"perfect aspect makes expulsion an accomplished stage\",\"reader_payoff\":\"The reader notices the expulsion as a completed eschatological stage following the shaking, not as an open-ended process.\",\"reason\":\"QAC identifies the verb as perfect, and the boundary rows place it after the previous perfect event.\",\"representative_source_ids\":[\"QG-67128531\",\"QY-ed99ee8a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:3","source_type":"word_analysis","support_id":"sup_28d4ecc9dd257546fd25","text":"{\"gloss_range\":\"the definite earth or ground as the same known terrestrial substrate from 99:1, now functioning as explicit subject and possessor of what is expelled\",\"prose\":\"{{ar:ٱلْأَرْضُ}} ({{tr:al-arḍu}}) is not a location phrase here; it is the nominative subject that performs {{ar:أَخْرَجَتِ}} ({{tr:akhrajat}}). The definite article resumes the same earth shaken in 99:1, so the reader sees a role reversal: the patient of shaking becomes the agent of expulsion. Its semantic range can cover planet, land, ground, floor, and substrate, but the local grammar selects the known containing ground as one singular subject. Positioned between verb and object, the earth becomes the hinge between action and {{ar:أَثْقَالَهَا}} ({{tr:athqālaha}}), whose suffix routes the expelled burdens back to it. The usual earth-heaven pairing is absent; the earth alone carries the clause as the visible bearer turned expeller, and the familiar earth-emergence field is redirected from provision toward burden exposure. Recitationally, liaison from the verb carries into the subject, then the subject's glottal and emphatic entry gives the load-bearing ground an audible body before the burden word arrives.\",\"root_display\":\"{{ar:أ ر ض}} ({{tr:ʾ-r-ḍ}})\",\"root_gloss_range\":\"earth, ground, land, territory, lower surface, and substrate; this ayah selects the known containing ground as acting subject\",\"surface_display\":\"{{ar:ٱلْأَرْضُ}} ({{tr:al-arḍu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:2:causative-extraction","source_type":"word_analysis","support_id":"sup_2d2b17491236b0d0f24b","text":"{\"blocking_evidence\":null,\"headline\":\"Form IV selects causative extraction\",\"reader_payoff\":\"The reader notices that the verb makes the earth cause its contents to come out, not merely report that something emerged from it.\",\"reason\":\"The aligned form is perfect Form IV with an explicit object; V4 supports the causative bringing-out branch, while unrelated {{ar:خ ر ج}} ({{tr:kh-r-j}}) branches are not locally selected.\",\"representative_source_ids\":[\"QG-92ac154b\",\"QS-3240f75c\",\"QF-b4d6e23d\",\"MF-35d0afe7\",\"QY-5eda189e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:3:earth-collocation-recast","source_type":"word_analysis","support_id":"sup_2e768e10e2835476366c","text":"{\"blocking_evidence\":null,\"headline\":\"earth pairings are recast locally\",\"reader_payoff\":\"The reader notices that ordinary earth associations are redirected: the earth acts without a heaven counterpart and its emergence field leads to burdens rather than provision.\",\"reason\":\"Contextual profiles show common earth collocations, especially with heaven and emergence fields, but the local clause contains only the earth as subject with its own burdens as object.\",\"representative_source_ids\":[\"QI-624f6a03\",\"QI-65be72c9\",\"QI-7c85e6cc\",\"MI-2bec9873\",\"QE-826ed836\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:4:closure-and-sound","source_type":"word_analysis","support_id":"sup_3c95b2f48bb25740ad63","text":"{\"blocking_evidence\":null,\"headline\":\"closure gives the burdens maximum weight\",\"reader_payoff\":\"The reader notices that the ayah lands on the earth's own burdens, with the repeated final suffix and heavy cadence tying this closure back to the prior ayah and setting up the question in 99:3.\",\"reason\":\"The word is final in the ayah, contains the possessive suffix, and echoes the prior ayah's possessive closure while also carrying the sound texture named by the phonetic rows.\",\"representative_source_ids\":[\"QT-85c82125\",\"QE-186d897f\",\"QP-658dd550\",\"QP-c5b32398\",\"QP-f195adaf\",\"MP-4cc7d6a4\",\"QB-3e8dc84f\",\"QB-49ad5675\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:4:weight-thread-to-measure","source_type":"word_analysis","support_id":"sup_3cc6229dcefc06412351","text":"{\"blocking_evidence\":null,\"headline\":\"macro-burdens anticipate micro-weight\",\"reader_payoff\":\"The reader notices the surah's scale shift: the earth first expels large burdens, then deeds are seen at the level of measured tiny weight (99:7-8).\",\"reason\":\"The CRITICAL rows identify the same-root recurrence within the surah, and V4 supports both load and measured-weight branches of {{ar:ث ق ل}} ({{tr:th-q-l}}).\",\"representative_source_ids\":[\"QS-5ec4f322\",\"QS-7c21e619\",\"QI-bb8a070b\",\"QE-3af07b60\",\"ME-2ef0a34b\",\"QY-5f1c64b3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:2:extraction-disclosure-range","source_type":"word_analysis","support_id":"sup_47b614e3172b9e33175a","text":"{\"blocking_evidence\":null,\"headline\":\"emergence range narrows to disclosure from within\",\"reader_payoff\":\"The reader notices that physical extraction and disclosure work together: buried contents come out and hidden reality becomes readable.\",\"reason\":\"The root family supports emergence and causative bringing out, while the local object limits the claim to extraction-disclosure rather than activating every derivative domain.\",\"representative_source_ids\":[\"QS-1e073209\",\"QS-9a97398a\",\"MS-c3a1478c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:1","source_type":"word_analysis","support_id":"sup_4da0da27887d64331794","text":"{\"gloss_range\":\"opening conjunction with boundary-continuation force, linking the prior shaking to the expulsion as a bound sequel within the same scene\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) makes 99:2 begin as continuation before any new lexical content appears. The particle binds the expulsion to the prior shaking, so the reader hears the second perfect verb as a sequel inside the same boundary event rather than as a detached report. Its range allows coordination, sequence, and circumstance, but the local ayah boundary and conditional chain narrow that range toward bound consequence: the shaking turns into disclosure. Because the connector is written onto {{ar:أَخْرَجَتِ}} ({{tr:akhrajat}}), linkage and action arrive together in the first surface beat.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:2:earth-emergence-recast","source_type":"word_analysis","support_id":"sup_50b8ca0904035ac982a4","text":"{\"blocking_evidence\":null,\"headline\":\"earth-emergence field is recast as burden exposure\",\"reader_payoff\":\"The reader notices that a familiar earth-emergence association is redirected from provision or ordinary emergence toward buried weight and judgment exposure.\",\"reason\":\"Contextual evidence confirms {{ar:خ ر ج}} ({{tr:kh-r-j}}) with explicit objects and earth-emergence associations, but the local object narrows the echo away from produce scenes such as 7:57 and 2:22 toward the earth's burdens.\",\"representative_source_ids\":[\"QI-4503f1d3\",\"QI-90c3d6c5\",\"QI-9603847a\",\"QI-d2b42052\",\"MI-f5388ab4\",\"QE-10cd53d4\",\"QE-750a880a\",\"ME-4335cfb0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"99:2:1:2","source_type":"qac_morpheme","support_id":"sup_5b4a25a8830cfd8bff5d","text":"{\"lemma_ar\":\"أَخْرَجَ\",\"morph_features\":\"STEM|POS:V|PERF|(IV)|LEM:>axoraja|ROOT:xrj|3FS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"99:2:1:2\",\"qac_word_ref\":\"99:2:1\",\"root_ar\":\"خ ر ج\",\"surface_ar\":\"أَخْرَجَتِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:1:fused-surface-onset","source_type":"word_analysis","support_id":"sup_66039d6b14c4155a3a3b","text":"{\"blocking_evidence\":null,\"headline\":\"clitic fusion makes the transition audible\",\"reader_payoff\":\"The reader notices that the light connector is not a detached marker; it is fused to the extraction verb, so linkage and action are heard as one launch.\",\"reason\":\"The local written surface joins {{ar:وَ}} ({{tr:wa}}) directly to {{ar:أَخْرَجَتِ}} ({{tr:akhrajat}}), licensing the fused onset observation.\",\"representative_source_ids\":[\"QF-2c6d0016\",\"QF-af70c7bd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:4:earth-owned-pronoun-circuit","source_type":"word_analysis","support_id":"sup_68f642fdeb1850614fdf","text":"{\"blocking_evidence\":null,\"headline\":\"suffix makes the burdens earth-owned\",\"reader_payoff\":\"The reader notices that the final object belongs to the same earth that expels it, closing the clause in a self-returning circuit.\",\"reason\":\"The attached feminine suffix is a genitive possessor whose local antecedent is the explicit feminine earth subject.\",\"representative_source_ids\":[\"QG-53f78b68\",\"QG-777f3015\",\"QG-b20aa210\",\"QG-c88829b4\",\"QF-97d8a1f7\",\"QI-50534ad4\",\"QT-3da12794\",\"MT-6ba31069\",\"QY-7a0b7821\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:4:marked-extraction-of-heaviness","source_type":"word_analysis","support_id":"sup_7dd1401f0f991e05afc0","text":"{\"blocking_evidence\":null,\"headline\":\"extraction is aimed at weight-bearing contents\",\"reader_payoff\":\"The reader notices that the bringing-out frame is sharpened by its object: extraction here targets weight-bearing contents.\",\"reason\":\"The contextual evidence marks the local pairing of extraction and heaviness as sparse, and the attachment evidence makes the burden word the direct object.\",\"representative_source_ids\":[\"QI-ecf23b4e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:2:verb-first-boundary-pivot","source_type":"word_analysis","support_id":"sup_88a4bdad1227cb353e31","text":"{\"blocking_evidence\":null,\"headline\":\"verb-first clause turns continuation into action\",\"reader_payoff\":\"The reader notices the action before the actor is named, so the ayah moves from the boundary connector straight into eruptive event.\",\"reason\":\"The clause begins with the coordinated perfect verb before naming the subject, and the prior passive shaking gives way to active causative expulsion.\",\"representative_source_ids\":[\"QT-3d9ceec5\",\"QT-524a90ca\",\"QT-f96150c2\",\"QB-4225ca36\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:4","source_type":"word_analysis","support_id":"sup_8c30a8c81333951f1929","text":"{\"gloss_range\":\"the earth's possessed heavy loads or contents, concrete and plural, with room for buried bodies, deposits, and disclosure-laden burdens while remaining the direct object of expulsion\",\"prose\":\"{{ar:أَثْقَالَهَا}} ({{tr:athqālahā}}) completes the clause by naming the direct object: what the earth brings out is not an abstract event but its own heavy contents. The attached {{ar:هَا}} ({{tr:hā}}) makes the burdens definite and earth-owned, sending the reader back to {{ar:ٱلْأَرْضُ}} ({{tr:al-ardu}}) at the ayah's close. The plural form gives heaviness object-shape: multiple loads, bodies, deposits, or records can be imagined as expelled contents rather than one vague mass. V4 supports the load and earth-content branch, while moral burden and pregnancy heaviness survive as narrowed pressure: the word can carry disclosure and delivery imagery, especially beside the pregnancy-heaviness echo (7:189), without ceasing to be the concrete object of extraction. The same root later returns in the measured-weight climax (99:7-8), so the surah moves from macro-burdens forced out of the earth to micro-weight accountability. The extraction frame is sharpened by this object because it targets weight-bearing contents specifically. The rough dental, deep-stop, and liquid cadence make the closing burden feel acoustically loaded; the repeated final {{ar:هَا}} ({{tr:hā}}) also binds 99:2 back to the prior possessive closure in 99:1 and leaves the exposed burdens as the disturbance that prompts the question in 99:3.\",\"root_display\":\"{{ar:ث ق ل}} ({{tr:th-q-l}})\",\"root_gloss_range\":\"heaviness, loads, burdens, earth contents, moral liabilities, measured weight, worth, sluggishness, and pregnancy heaviness; this ayah selects concrete possessed loads with disclosure and later weight-measure resonance\",\"surface_display\":\"{{ar:أَثْقَالَهَا}} ({{tr:athqālahā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:4:direct-object-completion","source_type":"word_analysis","support_id":"sup_99ee6d02d358e7ec05b5","text":"{\"blocking_evidence\":null,\"headline\":\"object names what the verb expels\",\"reader_payoff\":\"The reader notices that the expulsion is not left abstract; the final word names the affected contents brought out by the earth.\",\"reason\":\"Attachment evidence marks {{ar:أَثْقَالَهَا}} ({{tr:athqālahā}}) as the explicit accusative object of the causative verb.\",\"representative_source_ids\":[\"QG-53194d7a\",\"QT-ad037889\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:3:known-earth-role-reversal","source_type":"word_analysis","support_id":"sup_ab7c359898b6d76e6ced","text":"{\"blocking_evidence\":null,\"headline\":\"known earth changes from patient to agent\",\"reader_payoff\":\"The reader notices that the definite noun resumes the same earth from 99:1 and reverses its role from shaken patient to expelling subject.\",\"reason\":\"The definite form and adjacent ayah recurrence support continuity of referent, while local case and agreement make that referent the subject in 99:2.\",\"representative_source_ids\":[\"QG-be4f2311\",\"QF-b78a8127\",\"QI-2bacd5ee\",\"QT-9e590e94\",\"MT-0a39b600\",\"QE-8f451d11\",\"QB-fa5d5a46\",\"QY-582939e6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:3:substrate-range","source_type":"word_analysis","support_id":"sup_bf909f0eb08af446bf5d","text":"{\"blocking_evidence\":null,\"headline\":\"earth range narrows to containing substrate\",\"reader_payoff\":\"The reader notices the subject as the whole containing ground or substrate, not as one local plot, while the local syntax keeps it a single acting subject.\",\"reason\":\"The lexical range can include earth, land, ground, territory, and lower surface, but the local subject role narrows it to the known terrestrial substrate from which burdens are expelled.\",\"representative_source_ids\":[\"QS-234c7671\",\"QS-c730da72\",\"QS-da62caa9\",\"QF-775714be\",\"QF-cf276c5b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:2:earth-agency-agreement","source_type":"word_analysis","support_id":"sup_c15b27fd18b6e97abe9e","text":"{\"blocking_evidence\":null,\"headline\":\"agreement routes agency through the earth\",\"reader_payoff\":\"The reader notices that the visible syntax makes the earth the acting subject of the expulsion, even though the larger scene has divine eschatological force behind it.\",\"reason\":\"Attachment evidence marks {{ar:ٱلْأَرْضُ}} ({{tr:al-ardu}}) as the explicit subject, and the feminine verbal form agrees with it.\",\"representative_source_ids\":[\"QG-22372097\",\"QG-ebd5066a\",\"MG-7b610f8c\",\"QF-7f802154\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:3:visible-bearer-turned-expeller","source_type":"word_analysis","support_id":"sup_c96594af982444b11016","text":"{\"blocking_evidence\":null,\"headline\":\"container becomes visible expeller\",\"reader_payoff\":\"The reader notices the ground as a former container that now discharges what it held.\",\"reason\":\"The earth stands between the causative verb and its possessed object, making it the visible bearer that becomes the expelling subject.\",\"representative_source_ids\":[\"QS-689a547d\",\"QS-fc76b064\",\"MS-5b9aad96\",\"QT-36c8e4fa\",\"QT-c907ef36\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:2","source_type":"word_analysis","support_id":"sup_d07217053bc5ee602b5a","text":"{\"gloss_range\":\"completed causative bringing-out by the earth, locally selecting extraction and disclosure of its own heavy contents rather than simple emergence\",\"prose\":\"{{ar:أَخْرَجَتِ}} ({{tr:akhrajat}}) is a completed Form IV causative: the earth does not merely have contents emerge from it, but causes its own loads to come out. Its perfect aspect presents that extraction as an accomplished stage after the shaking, and because the verb comes before the actor, the reader meets the eruptive action before the earth is named. The feminine agreement and liaison into {{ar:ٱلْأَرْضُ}} ({{tr:al-ardu}}) route agency through the earth as the visible subject, while the direct object {{ar:أَثْقَالَهَا}} ({{tr:athqālaha}}) keeps the verb from becoming abstract. The broader {{ar:خ ر ج}} ({{tr:kh-r-j}}) family can describe emergence, production, and disclosure, but the local frame narrows that range to forced opening and extraction-disclosure from a containing ground, where buried contents come out and hidden reality becomes readable. That familiar earth-emergence field is also recast: passages where earth-emergence yields provision (7:57; 2:22) stand behind the association, but here the object is burden rather than produce. The sharp hamza and guttural movement in the verb give the transition from light connector to forceful action an audible edge.\",\"root_display\":\"{{ar:خ ر ج}} ({{tr:kh-r-j}})\",\"root_gloss_range\":\"broad root range around going out, causing to come out, output, eruption, and other branch-specific extensions; this ayah selects the Form IV causative extraction branch\",\"surface_display\":\"{{ar:أَخْرَجَتِ}} ({{tr:akhrajat}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:1:opening-hinge","source_type":"word_analysis","support_id":"sup_f63352c90f95845c67a4","text":"{\"blocking_evidence\":null,\"headline\":\"ayah begins with a hinge, not a new subject\",\"reader_payoff\":\"The reader notices that the first sound keeps the previous shaking active while turning the scene toward what the earth brings out.\",\"reason\":\"The particle stands at the start of 99:2 and links two complete verbal clauses across the ayah boundary.\",\"representative_source_ids\":[\"QT-4899611e\",\"QT-c2159a96\",\"MT-45cab670\",\"QB-bd9cdcb5\",\"QY-c2eb7c2f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:3:sound-and-subject-entry","source_type":"word_analysis","support_id":"sup_f6dafadb1592ae677747","text":"{\"blocking_evidence\":null,\"headline\":\"sound marks the subject's entry\",\"reader_payoff\":\"The reader notices the subject arrive audibly after the verb, with liaison and dense consonants matching its load-bearing role.\",\"reason\":\"The surface phrase links the verb into the article and then gives the subject a marked consonantal entry before the burden word.\",\"representative_source_ids\":[\"QP-43a938c2\",\"QP-473850d6\",\"QP-6157163a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:2:1:bound-sequel","source_type":"word_analysis","support_id":"sup_f754f495088e02ee4fcb","text":"{\"blocking_evidence\":null,\"headline\":\"connector makes expulsion a bound sequel\",\"reader_payoff\":\"The reader notices that the ayah opens inside the prior event-chain, so the expulsion is heard as the shaking's bound sequel and not as an isolated second scene.\",\"reason\":\"QAC identifies the word as a conjunction, and the local boundary evidence supports continuation under the earlier conditional frame; the broad timing range is narrowed because {{ar:وَ}} ({{tr:wa}}) itself does not force only one temporal value.\",\"representative_source_ids\":[\"QG-1ee5a4bb\",\"QG-9dec9cf0\",\"QS-9a2c64cd\",\"QT-2f8967c8\",\"QB-59f3121f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"99:2:2:2","source_type":"qac_morpheme","support_id":"sup_f9c29f9e4e16e893a217","text":"{\"lemma_ar\":\"أَرْض\",\"morph_features\":\"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"99:2:2:2\",\"qac_word_ref\":\"99:2:2\",\"root_ar\":\"ء ر ض\",\"surface_ar\":\"أَرْضُ\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا","ayah_ref":"99:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000025/B001","root_000202/B001","root_000400/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000400","role":"Causing a hidden thing to emerge supplies the outward transfer and makes the earth the extracting agent.","root":"خ ر ج","source_ref":"99:2","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000025","role":"The lower ground opposite the sky supplies the spatial container and point of origin.","root":"ء ر ض","source_ref":"99:2","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000202","role":"Heaviness against lightness makes the emitted contents resistant mass rather than neutral contents.","root":"ث ق ل","source_ref":"99:2","source_word_indices":["3"]}],"changed_reading":{"after":"The lower ground behaves as a loaded container that forces its weighty interior cargo out of concealment.","before":"The earth simply brings out unspecified burdens."},"confidence":"strong","focus_anchor":"The causative verb أخرجت, the subject الأرض, and the possessed plural أثقالها form a source-transfer-load construction.","mechanism":"The lower ground acts as a containing body and agent that transfers physically weighty contents from concealment to the outside.","model_id":"b_physical_extraction"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_physical_extraction","source_type":"hft","support_id":"sup_d17130fa1cecf805d0ab","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا","ayah_ref":"99:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000025/B002","root_000202/B004","root_000202/B005","root_000400/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000400","role":"A known due output of wealth or yield recasts emergence as rendering what is owed.","root":"خ ر ج","source_ref":"99:2","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000025","role":"Soft fertile ground supplies the productive source from which a yield can be rendered.","root":"ء ر ض","source_ref":"99:2","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_000202","role":"Standard weight and weighing make the output assessable rather than merely massive.","root":"ث ق ل","source_ref":"99:2","source_word_indices":["3"]},{"branch_id":"B005","mapped_root_id":"root_000202","role":"Weight as preciousness permits the burdens to be valuables or matters of consequence.","root":"ث ق ل","source_ref":"99:2","source_word_indices":["3"]}],"changed_reading":{"after":"The earth renders its stored yield for assessment, exposing both the measure and the worth of what it contained.","before":"The burdens are heavy objects removed from the ground."},"confidence":"medium","focus_anchor":"أخرجت can denote a due yield, الأرض can be productive ground, and أثقالها can invoke measured weight and value.","mechanism":"The earth renders an assessable yield: what it has held becomes a due output whose weight and worth can be determined.","model_id":"b_assessed_yield"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_assessed_yield","source_type":"hft","support_id":"sup_8b6e75f36708cb4fb7a9","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا","ayah_ref":"99:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000025/B002","root_000202/B007","root_000400/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000400","role":"Extraction from concealment supplies the transition from an enclosed interior to exposed arrival.","root":"خ ر ج","source_ref":"99:2","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000025","role":"Fertile established ground supplies a generative body rather than an inert container.","root":"ء ر ض","source_ref":"99:2","source_word_indices":["2"]},{"branch_id":"B007","mapped_root_id":"root_000202","role":"Pregnancy becoming heavy supplies the carried internal load and the delivery analogy.","root":"ث ق ل","source_ref":"99:2","source_word_indices":["3"]}],"changed_reading":{"after":"The earth delivers a load it has carried and developed within itself.","before":"The earth ejects cargo that happened to be inside it."},"confidence":"exploratory","focus_anchor":"The feminine earth possesses plural أثقال, while the focus inventories join fertile ground, hidden extraction, and pregnancy made heavy.","mechanism":"The earth is modeled as a gravid body: its burdens are an internally developed load, and bringing them out is delivery rather than disposal.","model_id":"b_gravid_delivery"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_gravid_delivery","source_type":"hft","support_id":"sup_82bbad2e93d869d8e71f","trust":"legacy_unbound"}]}
</lane_packet_json>
