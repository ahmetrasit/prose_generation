# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **90:13**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s090-regular-20260912/s090/90_13/micro.discovery.json` and modify nothing
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
  "ayah_ref": "90:13",
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
{"analysis_context":{"analysis_id":"s090-regular-20260912","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"90:13","host_surah":90,"lane_context_refs":[],"ordered_context_refs":["90:1","90:2","90:3","90:4","90:5","90:6","90:7","90:8","90:9","90:10","90:11","90:12","90:14","90:15","90:16","90:17","90:18","90:19","90:20","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Genel bekleme çekirdeği ile Tanrı buyruğunu gözetmeye bağlı özel çekinme kullanımı birbirine karıştırılmamalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000584/B001","candidate_links":[{"candidate_id":"cand_db8c2f3de428fbe0d723","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"رَقَبَة","morph_features":"STEM|POS:N|LEM:raqabap|ROOT:rqb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:2:1","qac_word_ref":"90:13:2","surface_ar":"رَقَبَةٍ"}],"gloss":"gözeterek beklemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi izleyerek ve sonucunu bekleyerek dikkat altında tutma."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin gelişini, sözünü veya beklenen bir olayın ortaya çıkmasını kollama."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tanrı'nın buyruğunu gözetme temelinde duyulan çekinme."}}],"root_ar":"ر ق ب","root_id":"root_000584","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi, nesne, söz veya olay dikkatle izlenerek beklendiğinde genel çekirdeği karşılar.","boundary_detail":"Genel bekleme çekirdeği ile Tanrı buyruğunu gözetmeye bağlı özel çekinme kullanımı birbirine karıştırılmamalıdır.","branch_image_ar":"المراقبة والانتظار","concept_gloss":"gözeterek beklemek","contextual_glosses":[{"applicability":"Bir gelişin, sözün veya sonucun dikkatle beklendiği anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hem gözlemeyi hem de beklentiyi açıkça korur."},"facet_ids":["F001","F002"],"text":"gözleyip beklemek","usage_role":"general"},{"applicability":"Tanrı karşısındaki dikkat ve çekinmeyi anlatan özel söz öbeğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çekinme ile davranışı gözetme bağını korur."},"facet_ids":["F003"],"text":"çekinip buyruğunu gözetmek","usage_role":"contextual"}],"definition":"Bir şeyi ya da kişiyi göz önünde tutarak onun gerçekleşmesini, gelmesini veya sözünü beklemektir. Belirli bir kullanımda bu dikkat, Tanrı'dan çekinip buyruğunu gözetme anlamına gelir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi izleyerek ve sonucunu bekleyerek dikkat altında tutma."},{"facet_id":"F002","role":"specialization","statement":"Bir kişinin gelişini, sözünü veya beklenen bir olayın ortaya çıkmasını kollama."},{"facet_id":"F003","role":"associated_use","statement":"Tanrı'nın buyruğunu gözetme temelinde duyulan çekinme."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dikkatle izleme ve gözetme işlemini dışarıda bırakır.","preserves":"Bir sonucun gerçekleşmesini bekleme yönünü korur."},"text":"yalnızca beklemek"}],"identity_rationale":"Yetkili ifade, bir şeyi ya da kişiyi gözeterek beklemeyi, gelişini veya sözünü ummayı ve bu izlemeye dayalı çekinme kullanımını birlikte destekler.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi gözleyip beklemek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"beklemek, gözlemek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"gerçekleşmesini gözleyerek beklemek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"Tanrı'dan çekinip buyruğunu gözetmek"}],"lexicalization_note":"Yalın eylem biçimleri bekleme ve gözlemeyi anlatır; çekinme anlamı ise yalnızca belirli söz öbeğine bağlıdır.","neighbor_coverage_note":"Sunulan bütün komşular değerlendirildi; görsel bekleme, koruyucu gözetleme ve nöbet sınırlarını en açık gösteren üç karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal görsel izlemeyi kurucu sınır yaparken bu dal daha genel dikkatli beklemeyi ve özel bir çekinme kullanımını kapsar.","focus_only":"Bekleme görsel olmak zorunda değildir ve söz ya da geliş gibi sonuçlara da yönelebilir.","gloss":"görerek bekleme","neighbor_only":"Bekleme özellikle gözle bakma ve görsel izleme üzerinden sınırlandırılır.","neighbor_ref":"root_000142/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi izleyip gerçekleşmesini bekleme alanında örtüşür."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği beklenen şeyi dikkatle izlemektir; komşu dal ise koruma ve pusu gibi görevsel gözetlemeyi de kurucu kapsamına alır.","focus_only":"Beklenen söz veya gelişe yönelik genel beklenti ile özel çekinme kullanımı bulunur.","gloss":"gözetleme ve nöbet","neighbor_only":"Koruma görevi, pusuya yatma ve toplu gözcülük anlamları da bulunur.","neighbor_ref":"root_000566/B001","relation_type":"near_synonym","shared_zone":"İki dal da izleme, kollama ve bekleme etkinliklerini paylaşır."},{"boundary_match":"field_only","distinction":"İzleme bu dalda beklentinin yöntemidir; komşu dalda ise koruma görevinin aracıdır.","focus_only":"Bir olayın ya da kişinin gerçekleşmesini bekleme eylemi merkezde yer alır.","gloss":"beklemek ile korumak","neighbor_only":"Korunan kimse veya topluluk için güvenlik sağlayan görevli merkezde yer alır.","neighbor_ref":"root_000584/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda dikkatli izleme ortak bir etkinliktir."}],"source_phrase_ar":"رقبت أرقب رقبة ورقبانا (maqayis); رقبت الشيء أرقبه أي انتظرت والترقب تنظر الشيء وتوقعه (ayn;tahdhib); ارتقبته ارتقابا إذا انتظرته (jamhara); الرقيب المنتظر ورصدته والترقب الانتظار والارتقاب (sihah); راقب الله في أمره أي خافه (sihah)","source_summary":"Kanıt, dikkatli bekleme ile gözlemeyi ortak çekirdek sayar; çekinme anlamını belirli bir davranış bağlamına bağlı olarak ekler.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه رقب الشيء وارتقابه وترقبه ورصده وانتظار قوله أو مجيئه، ويدخل فيه الخوف المبني على المراقبة","what_is_not_ar":"ليس حفظ المحروس ولا موضع الرصد ولا الرقبة العضو"},"support_links":["sup_ff6b296e47bc6cef9f81"]},{"boundary":"Dal, bekleme eylemini değil koruma amaçlı gözetim görevini ve bu görevi üstlenen kişiyi tanımlar.","branch_kind":"mixed_non_bare","branch_ref":"root_000584/B002","candidate_links":[{"candidate_id":"cand_db8c2f3de428fbe0d723","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"رَقَبَة","morph_features":"STEM|POS:N|LEM:raqabap|ROOT:rqb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:2:1","qac_word_ref":"90:13:2","surface_ar":"رَقَبَةٍ"}],"gloss":"koruyup gözeten görevli","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gözetim yoluyla koruma ve muhafaza etme görevi."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir topluluğu veya geride bırakılmış eşyayı koruyan bekçi."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ordunun önünden giderek çevreyi gözetleyen öncü."}}],"root_ar":"ر ق ب","root_id":"root_000584","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gözetimin amacı bir kişiyi, topluluğu veya eşyayı korumak olduğunda kullanılır.","boundary_detail":"Dal, bekleme eylemini değil koruma amaçlı gözetim görevini ve bu görevi üstlenen kişiyi tanımlar.","branch_image_ar":"الحفظ والحراسة","concept_gloss":"koruyup gözeten görevli","contextual_glosses":[{"applicability":"Bir topluluğun veya eşyasının başında koruma görevi yapan kişi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Koruma ve gözetim görevini doğal biçimde karşılar."},"facet_ids":["F001","F002"],"text":"bekçi","usage_role":"contextual"},{"applicability":"Ordunun önünde çevreyi denetleyen görevli anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önden gözetleme ile askerî görevi birlikte korur."},"facet_ids":["F003"],"text":"öncü gözcü","usage_role":"contextual"}],"definition":"Bir kişiyi, topluluğu veya eşyayı gözeterek koruyan görevli ya da muhafızdır. Orduda bu görev, önden gidip çevreyi denetleyen öncüye kadar genişler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gözetim yoluyla koruma ve muhafaza etme görevi."},{"facet_id":"F002","role":"specialization","statement":"Bir topluluğu veya geride bırakılmış eşyayı koruyan bekçi."},{"facet_id":"F003","role":"extension","statement":"Ordunun önünden giderek çevreyi gözetleyen öncü."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Gerçekleşmesi umulan bir olaya yönelik beklenti ekler.","collision":"Bekleme dalıyla karışır.","fit":"displacement","loses":"Koruma ve muhafaza görevini bütünüyle kaybeder.","preserves":"Dikkatli biçimde bir yerde durma çağrışımını korur."},"text":"bekleyen kişi"}],"identity_rationale":"Yetkili ifade, koruyan ve muhafaza eden görevliyi temel alır; topluluk bekçisi ile ordunun önden gözetleyen öncüsünü bu görevsel çekirdeğin özel türleri olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"koruyucu, muhafız"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"topluluğun bekçisi"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ordunun öncü gözcüsü"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"topluluğun geride kalan eşyasını bekleyen değersiz görevli"}],"lexicalization_note":"Yalın görevli adı koruyucuyu anlatır; topluluk bekçisi, ordu öncüsü ve eşya bekçisi anlamları belirli söz öbeklerine bağlıdır.","neighbor_coverage_note":"Bütün adaylar incelendi; genel koruma, bekleme eylemi ve gözetleme yeriyle kurulabilecek başlıca karışıklıklar seçilen üç karşılaştırmada kapsandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel koruma alanını daha geniş tutar; bu dal gözetleyen görevliyi ve onun belirli görev türlerini öne çıkarır.","focus_only":"Ordu öncüsü ve belirli topluluk ya da eşya bekçisi rolleri açıkça kapsanır.","gloss":"koruma ve bekçilik","neighbor_only":"Korunma, sakınma ve genel güvenlik örgütlenmesi daha geniş biçimde kapsanır.","neighbor_ref":"root_000307/B001","relation_type":"near_synonym","shared_zone":"İki dal da bekçilik yoluyla koruma ve muhafaza etme çekirdeğini paylaşır."},{"boundary_match":"field_only","distinction":"Bu dalda izleme, koruma görevini yerine getirir; komşu dalda ise beklenen sonuca yönelir.","focus_only":"Koruma sorumluluğu ve görevli kişi dalın kurucu unsurudur.","gloss":"koruyucu gözetim","neighbor_only":"Bir sözün, gelişin veya olayın gerçekleşmesini bekleme dalın kurucu unsurudur.","neighbor_ref":"root_000584/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda dikkatli izleme bulunur."},{"boundary_match":"field_only","distinction":"Bu dal görevliyi, komşu dal ise görevlinin kullandığı yüksek gözetleme yerini adlandırır.","focus_only":"Gözetleme ve koruma işini yapan kişi ya da görev öne çıkar.","gloss":"gözcü ve gözetleme yeri","neighbor_only":"Gözetleyenin üzerinde durduğu yüksek yer öne çıkar.","neighbor_ref":"root_000584/B003","relation_type":"same_field","shared_zone":"İki dal aynı koruma ve gözetleme sahnesinin kişi ve yer bileşenleridir."}],"source_phrase_ar":"الرقيب وهو الحافظ (maqayis;ayn;sihah;mufradat); رقيب القوم حارسهم يحرس القوم (tahdhib); رقيب الجيش طليعتهم (tahdhib)","source_summary":"Kanıt, koruma ve muhafazayı ortak çekirdek olarak verir; topluluk bekçisini ve ordu öncüsünü görev alanına göre ayırır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الرقيب الحافظ والحارس والطليعة التي تراقب للقوم","what_is_not_ar":"ليس مجرد الانتظار ولا موضع الحراسة ولا سهم الميسر"},"support_links":["sup_ff6b296e47bc6cef9f81"]},{"boundary":"Tanım gözcü kişiye değil, gözlem için kullanılan yüksek ve açık görüşlü yere aittir.","branch_kind":"bare","branch_ref":"root_000584/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَقَبَة","morph_features":"STEM|POS:N|LEM:raqabap|ROOT:rqb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:2:1","qac_word_ref":"90:13:2","surface_ar":"رَقَبَةٍ"}],"gloss":"yüksek gözetleme yeri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çevreyi izlemek için kullanılan yüksek ve görüşe hâkim yer."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dağ başında veya kalede bulunan gözetleme noktası."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gözetleme amacıyla yararlanılan doğal yüksek araziler."}}],"root_ar":"ر ق ب","root_id":"root_000584","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çevreyi izlemek için çıkılan yüksek bir yer veya yapı bölümü anlatıldığında kullanılır.","boundary_detail":"Tanım gözcü kişiye değil, gözlem için kullanılan yüksek ve açık görüşlü yere aittir.","branch_image_ar":"موضع الرصد المرتفع","concept_gloss":"yüksek gözetleme yeri","contextual_glosses":[{"applicability":"Yükseklik bağlamdan açık olduğunda doğal ve yapılı yerler için kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Söz öbeği tek başına yerin yüksek olduğunu açıkça söylemez.","preserves":"Yerin gözetleme amacıyla kullanılmasını korur."},"facet_ids":["F001","F002","F003"],"text":"gözetleme noktası","usage_role":"general"}],"definition":"Bir gözcünün çevreyi izlemek veya koruma yapmak için çıktığı, görüşe hâkim yüksek yerdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çevreyi izlemek için kullanılan yüksek ve görüşe hâkim yer."},{"facet_id":"F002","role":"specialization","statement":"Dağ başında veya kalede bulunan gözetleme noktası."},{"facet_id":"F003","role":"extension","statement":"Gözetleme amacıyla yararlanılan doğal yüksek araziler."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yer yerine işi yapan kişiyi gösterir.","collision":"Koruyucu görevli dalıyla karışır.","fit":"displacement","loses":"Yüksek yer olma niteliğini kaybeder.","preserves":"Gözetleme sahnesini ve işlevini çağrıştırır."},"text":"gözcü"}],"identity_rationale":"Yetkili ifade, gözcünün üzerinde durduğu yüksek ve çevreye hâkim yeri ortak çekirdek yapar; dağ başı, kale ve yükselti örnekleri bu yer anlamını destekler.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yüksek gözetleme yeri"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"dağ başı veya kale gözetleme yeri"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yüksek gözetleme yerleri"}],"lexicalization_note":"Dal yalın yer adlarını kapsar ve herhangi bir söz öbeğine özgü ek anlam tanıma taşınmaz.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; yüksek olmayan gözetleme yeri, yüksekten bakma eylemi ve gözcü kişiyle sınırı gösteren üç aday yeterli bulundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yalnızca yüksek ve görüşe hâkim yerleri kapsar; komşu dal gözetleme için ayrılmış yolu veya tuzak yerini de içerebilir.","focus_only":"Yükseklik ve görüşe hâkim olma yer anlamının zorunlu sınırıdır.","gloss":"gözetleme yeri","neighbor_only":"Yol, pusu noktası ve hazırlanmış tuzak gibi yüksek olmayan yerleri de kapsar.","neighbor_ref":"root_000566/B003","relation_type":"near_synonym","shared_zone":"İki dal da gözetleyenin beklediği veya çevreyi izlediği yeri adlandırır."},{"boundary_match":"field_only","distinction":"Bu dal işlevsel bir gözetleme yeridir; komşu dal ise yüksekliğe erişme veya oradan bakma eylemidir.","focus_only":"Gözetleme işlevi bulunan yüksek yer adlandırılır.","gloss":"yüksekten gözetleme","neighbor_only":"Bir yüksekliğe çıkma ve oradan aşağıya bakma eylemi adlandırılır.","neighbor_ref":"root_001669/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal yükseklik ile geniş görüş alanını bir araya getirir."},{"boundary_match":"field_only","distinction":"Bu dal gözetleme noktasını, komşu dal o noktada görev yapabilen koruyucuyu anlatır.","focus_only":"Gözetleme için kullanılan fiziksel yer öne çıkar.","gloss":"yer ve görevli","neighbor_only":"Koruma ve gözetleme işini yapan görevli öne çıkar.","neighbor_ref":"root_000584/B002","relation_type":"same_field","shared_zone":"İki dal aynı gözetleme ve koruma düzeninin bileşenleridir."}],"source_phrase_ar":"المرقب المكان العالي يقف عليه الناظر (maqayis); يشرف على رقبة يحرس القوم (ayn); المراقب واحدها مرقب وهي المرابي (jamhara); المرقب والمرقبة الموضع المشرف يرتفع عليه الرقيب (sihah); المرقبة هي المنظرة في رأس جبل أو حصن والمراقب ما ارتفع من الأرض (tahdhib)","source_summary":"Kanıt, yüksekliği ve çevreyi görmeye elverişliliği ortaklaştırır; yapılı gözetleme noktaları ile doğal yükseltileri aynı yer anlamında toplar.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه المرقب والمرقبة والمراقب والمرابي، وهي المواضع العالية التي يقف أو يقعد عليها الناظر والحارس","what_is_not_ar":"ليس الرقيب الشخص ولا الرقبة العضو"},"support_links":[]},{"boundary":"Organ anlamı yalın çekirdektir; kişi, köleleştirilmiş kişi, bağlama ve özgürleştirme anlamları türemiş ya da söz öbeğine bağlı kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000584/B004","candidate_links":[{"candidate_id":"cand_d0a75656dc7218d3891b","lane":"micro"},{"candidate_id":"cand_0b94d2c52cf84cc13eac","lane":"micro"},{"candidate_id":"cand_47bc2041da7a9ecc37e4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"رَقَبَة","morph_features":"STEM|POS:N|LEM:raqabap|ROOT:rqb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:2:1","qac_word_ref":"90:13:2","surface_ar":"رَقَبَةٍ"}],"gloss":"boyun ve kişi yerine kullanılan boyun","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Boynun arka tabanındaki organ bölümü."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Organ adının bütün kişi veya köleleştirilmiş kişi yerine kullanılması."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Boynu kalın olan kişi için kullanılan niteleme."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir insanın veya hayvanın boynuna ip geçirme eylemi."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Kişi aktarması üzerinden köleleştirilmiş birini özgür bırakma, sözleşmeli özgürleşmeye yardım etme veya tutsağı salıverme."}}],"root_ar":"ر ق ب","root_id":"root_000584","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem organ çekirdeğini hem de organ adının bütün kişiyi göstermesini birlikte anlatmak gerektiğinde kullanılır.","boundary_detail":"Organ anlamı yalın çekirdektir; kişi, köleleştirilmiş kişi, bağlama ve özgürleştirme anlamları türemiş ya da söz öbeğine bağlı kullanımlardır.","branch_image_ar":"الرَّقَبَة والرقاب","concept_gloss":"boyun ve kişi yerine kullanılan boyun","contextual_glosses":[{"applicability":"İnsan veya hayvan bedenindeki organ bölümü doğrudan anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Organın temel anatomik anlamını korur."},"facet_ids":["F001"],"text":"boyun","usage_role":"general"},{"applicability":"Organ adı bütün kişi ve özellikle köleleştirilmiş kimse yerine kullanıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiye yönelen ad aktarmasının toplumsal referansını korur."},"facet_ids":["F002"],"text":"köleleştirilmiş kişi","usage_role":"contextual"},{"applicability":"Köleleştirilmiş birinin veya tutsağın serbest bırakılması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bağlı kişiyi özgür duruma getirme sonucunu korur."},"facet_ids":["F005"],"text":"özgürlüğüne kavuşturmak","usage_role":"contextual"}],"definition":"Boynun arka tabanındaki bilinen organ bölümüdür. Bu organ adı, bütün kişi veya köleleştirilmiş kişi için kullanılabilir ve bağlama, özgür bırakma ya da tutsaklıktan çıkarma yapılarına temel olur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Boynun arka tabanındaki organ bölümü."},{"facet_id":"F002","role":"extension","statement":"Organ adının bütün kişi veya köleleştirilmiş kişi yerine kullanılması."},{"facet_id":"F003","role":"specialization","statement":"Boynu kalın olan kişi için kullanılan niteleme."},{"facet_id":"F004","role":"associated_use","statement":"Bir insanın veya hayvanın boynuna ip geçirme eylemi."},{"facet_id":"F005","role":"extension","statement":"Kişi aktarması üzerinden köleleştirilmiş birini özgür bırakma, sözleşmeli özgürleşmeye yardım etme veya tutsağı salıverme."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bir kişinin durumu yerine kurum ve statü anlamı ekler.","collision":"Kölelik durumunu tanımlayan ayrı dalla karışır.","fit":"displacement","loses":"Organ çekirdeğini ve belirli kişi gönderimini kaybeder.","preserves":"Bazı türemiş kullanımların toplumsal alanını çağrıştırır."},"text":"kölelik"}],"identity_rationale":"Yetkili ifade, boynun arka tabanındaki organı çekirdek alır; buradan bütün kişiye ve köleleştirilmiş kişiye uzanan ad aktarmasını, bağlama ve özgür bırakma kullanımlarını açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"boynun arka tabanı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"kişi veya köleleştirilmiş kimse"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kalın boyunlu"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"insanın veya hayvanın boynuna ip geçirmek"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"köleleştirilmiş birini özgür bırakmak"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"özgürlük sözleşmesi yapan köleleştirilmiş kişiler için"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"tutsağı serbest bırakmak"}],"lexicalization_note":"Yalın biçimler organı ve kişi aktarmasını taşır; bağlama, özgür bırakma ve özgürlük sözleşmesiyle ilgili anlamlar belirli yapılara bağlıdır.","neighbor_coverage_note":"Bütün adaylar incelendi; genel boyun adı, bağdan kurtarma ve kölelik statüsüyle en açıklayıcı üç sınır yayıma alındı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel bir boyun adıdır; bu dal organın arka tabanını ve ondan gelişen kişi, bağlama ve özgürleştirme kullanımlarını taşır.","focus_only":"Boynun arka tabanı ile kişi ve köleleştirilmiş kişi aktarmaları kapsanır.","gloss":"boyun","neighbor_only":"Boyun genel olarak, bu özel anatomik sınır ve türemiş kullanımlar olmadan adlandırılır.","neighbor_ref":"root_000185/B002","relation_type":"near_synonym","shared_zone":"İki dal insan bedenindeki boyun bölgesini gösterir."},{"boundary_match":"field_only","distinction":"Bu dal kişi için kullanılan organ adını temel alır; komşu dal ise farklı bağlılık türlerinden kurtarma eylemini temel alır.","focus_only":"Boyun adından bütün kişiye uzanan aktarım ve özgür bırakma yapıları bulunur.","gloss":"bağdan kurtarma","neighbor_only":"Rehin, tutsak veya bağlı nesneyi kapanmadan ve bağdan kurtarma süreci geneldir.","neighbor_ref":"root_001173/B002","relation_type":"near_neighbor","shared_zone":"İki dal tutsak veya köleleştirilmiş birini serbest bırakma bağlamında buluşur."},{"boundary_match":"field_only","distinction":"Bu dal belirli kişiyi ad aktarımıyla gösterirken komşu dal kölelik kurumunu ve statüsünü anlatır.","focus_only":"Köleleştirilmiş kişi, organ adının kişiye aktarılmasıyla gösterilir.","gloss":"kişi ve kölelik durumu","neighbor_only":"Kölelik statüsü, sahiplik ve insanı köleleştirme doğrudan tanımlanır.","neighbor_ref":"root_000586/B003","relation_type":"near_neighbor","shared_zone":"İki dal köleleştirilmiş insanı gösteren kullanımlarda kesişir."}],"source_phrase_ar":"اشتقاق الرقبة لأنها منتصبة (maqayis); الرقبة أصل مؤخر العنق والأرقب والرقباني الغليظ الرقبة والإعطاء في الرقاب أي في المكاتبين (ayn); الرقبة معروفة وأعتق رقبة وفككت رقبة ورقبت الرجل والدابة إذا طرحت في رقبته حبلا (jamhara); الرقبة مؤخر أصل العنق والرقبة المملوك (sihah); في الرقاب هم المكاتبون وأعتق الله رقبته (tahdhib); الرقبة اسم للعضو المعروف ثم يعبر بها عن الجملة واسما للمماليك (mufradat)","source_summary":"Kanıt, organ anlamından bütün kişiye uzanan ad aktarmasını ortaklaştırır; kalın boyun, iple bağlama, kölelikten çıkarma ve tutsak salıverme kullanımlarını bu ağda konumlandırır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الرقبة عضو العنق، وغليظ الرقبة، وربط الحبل في الرقبة، واستعمال الرقبة للجملة والمملوك والمكاتب والتحرير وفك الأسير","what_is_not_ar":"ليس الانتظار ولا الرقبى ولا الرقيب الحافظ"},"support_links":["sup_49d022c5d355ee805a34","sup_93392234eeda524a562c","sup_b04130cf9f2d4b2b5fd5"]},{"boundary":"Bu dal genel bağış değildir; mülkün geleceğini tarafların yaşamına bağlayan açık koşul zorunludur.","branch_kind":"mixed_non_bare","branch_ref":"root_000584/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَقَبَة","morph_features":"STEM|POS:N|LEM:raqabap|ROOT:rqb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:2:1","qac_word_ref":"90:13:2","surface_ar":"رَقَبَةٍ"}],"gloss":"sağ kalma koşullu taşınmaz bağışı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ev veya arazi üzerinde koşullu bir bağış kurma."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Mülkün sağ kalana geçmesi veya ölümle geri dönmesi koşulu."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tarafların birbirinin ölümünü gözetmesi üzerinden açıklanan adlandırma ilişkisi."}}],"root_ar":"ر ق ب","root_id":"root_000584","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ev veya arazi bağışının mülkiyet sonucu tarafların hangisinin sağ kaldığına bağlandığında kullanılır.","boundary_detail":"Bu dal genel bağış değildir; mülkün geleceğini tarafların yaşamına bağlayan açık koşul zorunludur.","branch_image_ar":"الرُّقبى وهبة الباقي","concept_gloss":"sağ kalma koşullu taşınmaz bağışı","contextual_glosses":[{"applicability":"Koşulun taraflardan birinin ölümüyle doğurduğu sonucu vurgulamak gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bağış ile ölüm koşulu arasındaki kurucu bağı korur."},"facet_ids":["F001","F002"],"text":"ölüme bağlı koşullu bağış","usage_role":"explanatory"}],"definition":"Bir evin veya arazinin, taraflardan sağ kalana ait olması ya da taraflardan birinin ölümüyle geri dönmesi koşuluyla verilmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ev veya arazi üzerinde koşullu bir bağış kurma."},{"facet_id":"F002","role":"specialization","statement":"Mülkün sağ kalana geçmesi veya ölümle geri dönmesi koşulu."},{"facet_id":"F003","role":"associated_use","statement":"Tarafların birbirinin ölümünü gözetmesi üzerinden açıklanan adlandırma ilişkisi."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bağışın yalnızca belirli bir yaşam süresi boyunca geçerli olduğu izlenimini ekler.","collision":"Yaşam süresiyle sınırlı bağış dalıyla karışır.","fit":"displacement","loses":"Sağ kalana geçme veya ölümle geri dönme koşulunu belirsizleştirir.","preserves":"Bağışın tarafların yaşamıyla ilişkili oluşunu korur."},"text":"ömür boyu bağış"}],"identity_rationale":"Yetkili ifade, ev veya arazi bağışını taraflardan sağ kalana kalma ya da ölümle geri dönme koşuluna bağlar ve adlandırmanın karşılıklı ölüm beklentisiyle ilişkisini açıklar.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"sağ kalma veya geri dönüş koşullu taşınmaz bağışı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bir evi sağ kalma koşuluyla vermek"}],"lexicalization_note":"Yalın ad koşullu bağış türünü, söz öbeği ise evi bu koşulla verme eylemini anlatır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yaşam süresine bağlı bağış ile genel bağış, bu özel mülkiyet koşulunun sınırını en iyi açıklayan iki karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal sağ kalma yarışına benzeyen mülkiyet koşulunu kurar; komşu dal öncelikle bağıştan yararlanma süresini bir ömre bağlar.","focus_only":"Mülkün sağ kalana ait olması veya taraflardan birinin ölümüyle geri dönmesi koşulu belirleyicidir.","gloss":"yaşama bağlı bağış","neighbor_only":"Bağışın kullanım süresi taraflardan birinin ömrüyle sınırlandırılır ve geri dönüş ayrıca tartışılabilir.","neighbor_ref":"root_001044/B008","relation_type":"near_synonym","shared_zone":"İki dal da ev veya arazi bağışını bir kişinin yaşam süresi ve ölüm sonucuyla ilişkilendirir."},{"boundary_match":"field_only","distinction":"Bu dal belirli bir taşınmaz ve sağ kalma koşulu ister; komşu dal genel bağış eylemidir.","focus_only":"Taşınmazın geleceğini yaşam ve ölüm sonucuna bağlayan koşul bulunur.","gloss":"koşullu ve genel bağış","neighbor_only":"Herhangi bir nesne veya yararın koşulsuz verilmesi yeterlidir.","neighbor_ref":"root_000076/B012","relation_type":"near_neighbor","shared_zone":"Her iki dal bir malın başkasına verilmesini anlatır."}],"source_phrase_ar":"أرقبت فلانا هذه الدار (maqayis); الرقبى أن يعطي الرجل دارا أو أرضا (jamhara); أرقبته دارا أو أرضا إذا أعطيته إياها فكانت للباقي منكما (sihah); أصل الرقبى من المراقبة كأن كل واحد منهما يرقب موت صاحبه (tahdhib)","source_summary":"Kanıt, taşınmaz bağışını ortaklaştırır ve onu sıradan bağıştan ayıran yaşam koşulunu iki sonuçla açıklar: sağ kalana geçiş veya ölümle geri dönüş.","sources":["MQ","JA","SI","TA"],"what_is_ar":"يدخل فيه إرقاب الدار أو الأرض، وهي عطية مشروطة بأن تكون للباقي أو ترجع بموت أحدهما","what_is_not_ar":"ليست العمرى المطلقة ولا مطلق المراقبة"},"support_links":[]},{"boundary":"Görevli kişi ile üçüncü oyun oku birbirinden ayrı iki adlandırmadır; ortaklıkları yalnızca aynı oyun düzenine aittir.","branch_kind":"bare","branch_ref":"root_000584/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَقَبَة","morph_features":"STEM|POS:N|LEM:raqabap|ROOT:rqb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:2:1","qac_word_ref":"90:13:2","surface_ar":"رَقَبَةٍ"}],"gloss":"oyun denetçisi veya üçüncü oyun oku","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Oklarla yürütülen paylaştırmalı talih oyunu içindeki özel adlandırma."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Paylaştırmayı veya oyuncuları denetleyen güvenilir görevli."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Oyun okları dizisindeki üçüncü ok."}}],"root_ar":"ر ق ب","root_id":"root_000584","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tarihî ok oyununda görevli kişi ile numaralı ok anlamlarının ikisini birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Görevli kişi ile üçüncü oyun oku birbirinden ayrı iki adlandırmadır; ortaklıkları yalnızca aynı oyun düzenine aittir.","branch_image_ar":"رقيب الميسر وسهمه","concept_gloss":"oyun denetçisi veya üçüncü oyun oku","contextual_glosses":[{"applicability":"Paylaştırmayı ve oyuncuları denetleyen görevli kişi kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Görevli kişiyi ve denetim işlevini korur."},"facet_ids":["F002"],"text":"oyunun pay denetçisi","usage_role":"contextual"},{"applicability":"Talih oyununda kullanılan okların üçüncüsü kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Oyun aracını ve sıra numarasını korur."},"facet_ids":["F003"],"text":"üçüncü oyun oku","usage_role":"contextual"}],"definition":"Oklarla oynanan paylaştırmalı talih oyununda ya payları ve oyuncuları denetleyen görevlinin ya da oyun oklarının üçüncüsünün adıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Oklarla yürütülen paylaştırmalı talih oyunu içindeki özel adlandırma."},{"facet_id":"F002","role":"source_variant","statement":"Paylaştırmayı veya oyuncuları denetleyen güvenilir görevli."},{"facet_id":"F003","role":"source_variant","statement":"Oyun okları dizisindeki üçüncü ok."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Koruyucu görevli dalıyla karışır.","fit":"narrowing","loses":"Özel oyun bağlamını ve üçüncü ok anlamını kaybeder.","preserves":"Görevli kişinin denetim yönünü kısmen korur."},"text":"gözcü"}],"identity_rationale":"Yetkili ifade aynı talih oyunu alanında iki ayrı gönderimi, paylaştırmayı denetleyen görevliyi ve oyunun üçüncü okunu birlikte kaydeder; dal korunabilir ancak tek bir nesneymiş gibi tanımlanamaz.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"oklarla oynanan talih oyununun pay denetçisi"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"talih oyununun üçüncü oku"}],"lexicalization_note":"İki yalın ad kullanımı korunur; söz öbeğine dayalı yeni bir genel anlam türetilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; üçüncü okun diğer oyun oklarından ve oyun denetçisinin koruyucu görevlerden farkını gösteren üç karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal üçüncü oku ve ayrıca bir görevliyi kapsar; komşu dal yalnızca altıncı oku gösterir.","focus_only":"Üçüncü oyun oku ve payları denetleyen görevli birlikte adlandırılır.","gloss":"üçüncü ve altıncı oyun oku","neighbor_only":"Aynı oyun dizisinin altıncı oku tek başına adlandırılır.","neighbor_ref":"root_000867/B011","relation_type":"near_neighbor","shared_zone":"İki dal aynı tarihî talih oyununun numaralı oklarını içerir."},{"boundary_match":"field_only","distinction":"Bu dal belirli sıradaki oku adlandırır; komşu dal aracın genel türünü anlatır.","focus_only":"Ok, oyun dizisindeki üçüncü konumuyla özelleşir.","gloss":"numaralı ve genel oyun oku","neighbor_only":"Ok veya çubuk, henüz uç ve tüy takılmamış genel oyun aracı olarak ele alınır.","neighbor_ref":"root_001203/B007","relation_type":"near_neighbor","shared_zone":"İki dal talih oyununda kullanılan ok veya çubuk aracını paylaşır."},{"boundary_match":"field_only","distinction":"Bu dalın kişi anlamı oyun düzenine özgüdür; komşu dalın görevlisi güvenlik ve koruma sağlar.","focus_only":"Görevli yalnızca paylaştırmalı talih oyununun düzenini denetler.","gloss":"oyun denetçisi ve muhafız","neighbor_only":"Görevli kişi, topluluğu veya eşyayı tehlikeye karşı korur.","neighbor_ref":"root_000584/B002","relation_type":"near_neighbor","shared_zone":"İki dalda gözetim yapan bir görevli anlamı bulunur."}],"source_phrase_ar":"الرقيب الموكل في الميسر بالضريب والرقيب السهم الثالث (maqayis); رقيب الميسر الأمين الموكل بالضريب والرقيب السهم الثالث (ayn;tahdhib); الرقيب الرجل المشرف على أصحاب الميسر (jamhara); الرقيب الموكل بالضريب والثالث من سهام الميسر (sihah)","source_summary":"Kanıt, aynı oyun alanında kişi ve nesne gönderimlerini yan yana korur: pay denetçisi ile üçüncü ok birbirine indirgenmez.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه رقيب الميسر، والموكل بالضريب، والسهم الثالث من سهام الميسر","what_is_not_ar":"ليس الرقيب الحافظ ولا رقيب النجم"},"support_links":[]},{"boundary":"Dal herhangi bir yıldızı veya yıldızın batışını değil, karşılıklı doğuş ve batış ilişkisi içindeki eş yıldızı tanımlar.","branch_kind":"mixed_non_bare","branch_ref":"root_000584/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَقَبَة","morph_features":"STEM|POS:N|LEM:raqabap|ROOT:rqb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:2:1","qac_word_ref":"90:13:2","surface_ar":"رَقَبَةٍ"}],"gloss":"karşı yıldız","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yıldızın doğuşunun karşı yıldızın batışına denk gelmesi."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ülker batarken doğan Taç yıldız grubunun başındaki yıldız."}}],"root_ar":"ر ق ب","root_id":"root_000584","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir yıldızın doğuşu başka bir yıldızın batışına düzenli olarak karşılık geldiğinde kullanılır.","boundary_detail":"Dal herhangi bir yıldızı veya yıldızın batışını değil, karşılıklı doğuş ve batış ilişkisi içindeki eş yıldızı tanımlar.","branch_image_ar":"رقيب النجم","concept_gloss":"karşı yıldız","contextual_glosses":[{"applicability":"Terimin teknik gökbilimsel ilişkisini açıkça anlatmak gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğuş ile karşı yıldızın batışı arasındaki eşleşmeyi korur."},"facet_ids":["F001"],"text":"biri doğarken batan yıldız","usage_role":"explanatory"}],"definition":"Başka bir yıldız doğduğunda batan ya da o batarken doğan, gökyüzündeki karşılıklı doğuş ve batış ilişkisiyle belirlenen yıldızdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yıldızın doğuşunun karşı yıldızın batışına denk gelmesi."},{"facet_id":"F002","role":"example","statement":"Ülker batarken doğan Taç yıldız grubunun başındaki yıldız."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Yıldızın bilinçli olarak gözetleme yaptığı yönünde işlevsel bir anlam ekler.","collision":"Koruyucu gözcü dalını çağrıştırır.","fit":"broadening","loses":null,"preserves":"Yıldızın başka bir yıldızla ilişkili özel konumunu sezdirir."},"text":"gözcü yıldız"}],"identity_rationale":"Yetkili ifade, bir yıldız doğarken karşısındaki yıldızın batması ilişkisini temel alır ve Ülker'in karşılığı olarak Taç yıldız grubunun başını örnekler.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"başka bir yıldız doğarken batan karşı yıldız"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"Ülker batarken doğan karşı yıldız"}],"lexicalization_note":"Yalın ad karşıt doğuşlu yıldız türünü anlatır; Ülker'e ilişkin örnek belirli söz öbeğine bağlı tutulur.","neighbor_coverage_note":"Bütün komşular değerlendirildi; karşı yıldızın göksel olaydan ve ardından gelen yıldızdan farkını açıklayan iki aday yayıma değer bulundu.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal ilişkideki yıldızı adlandırır; komşu dal göksel olayı, dönemini ve ona bağlanan hava sonuçlarını anlatır.","focus_only":"Karşılıklı doğuş ve batış düzenindeki eş yıldız adlandırılır.","gloss":"karşı yıldız ve yıldız dönemi","neighbor_only":"Bir yıldızın batışı, karşı yıldızın doğuşu ve bunlarla ilişkilendirilen hava olayı veya dönem birlikte anlatılır.","neighbor_ref":"root_001561/B002","relation_type":"near_neighbor","shared_zone":"İki dal bir yıldız batarken karşısındakinin doğması olayını paylaşır."},{"boundary_match":"field_only","distinction":"Bu dal karşılıklı doğuş ve batışa, komşu dal ise gökyüzünde ardından gelme ilişkisine dayanır.","focus_only":"Yıldız, diğerinin doğuşuna karşılık batması veya batışına karşılık doğmasıyla belirlenir.","gloss":"karşıt ve izleyen yıldız","neighbor_only":"Belirli yıldız ya da yıldız grubu Ülker'i gökyüzünde izlemesiyle belirlenir.","neighbor_ref":"root_000458/B013","relation_type":"near_neighbor","shared_zone":"İki dal yıldızları Ülker'e göre kurulan konumsal ve zamansal ilişkiyle tanımlar."}],"source_phrase_ar":"الرقيب النجم الذي ينوء من المشرق فيغيب رقيبه في المغرب ورقيب الثريا (jamhara); رقيب النجم الذي يغيب بطلوعه (sihah); رقيب الثريا رأس الإكليل لا يطلع أبدا حتى تغيب (tahdhib)","source_summary":"Kanıt, yıldızları karşılıklı doğuş ve batış düzeninde eşler; Ülker ile Taç yıldız grubunun başı bu ilişkinin belirli örneğidir.","sources":["JA","SI","TA"],"what_is_ar":"يدخل فيه النجم الذي يقابل نجما آخر في الطلوع أو الغيبوبة، مثل رقيب الثريا","what_is_not_ar":"ليس رقيب الميسر ولا الحارس"},"support_links":[]},{"boundary":"Çocuk kaybı ana tarihî kullanımdır, ancak kanıttaki çocuğunu hiç kaybetmemiş kişi biçimindeki karşıt yorum ayrı bir kaynak çeşitlemesi olarak korunmalıdır.","branch_kind":"bare","branch_ref":"root_000584/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَقَبَة","morph_features":"STEM|POS:N|LEM:raqabap|ROOT:rqb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:2:1","qac_word_ref":"90:13:2","surface_ar":"رَقَبَةٍ"}],"gloss":"çocukları yaşamayan ebeveyn","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çocukları yaşamayan veya çocuk kaybıyla tanımlanan ebeveyn."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Çocuğu ve geçimini sağlayacak kazancı olmayan dul ya da yaşlı kişi."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çocuklarından hiçbirini kendinden önce ölüme göndermemiş kişi."}}],"root_ar":"ر ق ب","root_id":"root_000584","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Terimin çoğunlukla tanıklanan çocuk kaybı anlamında kullanıldığı bağlamlara uygundur.","boundary_detail":"Çocuk kaybı ana tarihî kullanımdır, ancak kanıttaki çocuğunu hiç kaybetmemiş kişi biçimindeki karşıt yorum ayrı bir kaynak çeşitlemesi olarak korunmalıdır.","branch_image_ar":"الرَّقوب وفقد الولد","concept_gloss":"çocukları yaşamayan ebeveyn","contextual_glosses":[{"applicability":"Çocukların doğduktan sonra yaşamaması veya ölmesi vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ebeveynin çocuk kaybıyla tanımlanmasını korur."},"facet_ids":["F001"],"text":"çocuğunu yitirmiş ebeveyn","usage_role":"contextual"},{"applicability":"Kanıttaki karşıt yorum özellikle kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin hiçbir çocuğunun kendisinden önce ölmemiş olması koşulunu korur."},"facet_ids":["F003"],"text":"hiç çocuk kaybetmemiş kişi","usage_role":"contextual"}],"definition":"Başlıca kullanımda çocukları yaşamayan ebeveyni belirtir. Kanıt ayrıca çocuğu ve kazancı olmayan dul ya da yaşlı kişiyi ve karşıt bir yorumla çocuklarından hiçbirini kendinden önce kaybetmemiş kişiyi de kaydeder.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çocukları yaşamayan veya çocuk kaybıyla tanımlanan ebeveyn."},{"facet_id":"F002","role":"source_variant","statement":"Çocuğu ve geçimini sağlayacak kazancı olmayan dul ya da yaşlı kişi."},{"facet_id":"F003","role":"source_variant","statement":"Çocuklarından hiçbirini kendinden önce ölüme göndermemiş kişi."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çocuk doğurup onları kaybetme ile hiç çocuk kaybetmemiş olma arasındaki kaynak ayrımını siler.","preserves":"Kişinin yaşayan çocuğunun bulunmaması durumunu kısmen korur."},"text":"çocuksuz kişi"}],"identity_rationale":"Yetkili ifade çoğunlukla çocuğu yaşamayan ebeveyni gösterir; ayrıca çocuğu ve kazancı olmayan dul veya yaşlı kişiyi ve ters yönde, çocuklarından hiçbirini kendinden önce kaybetmemiş kişiyi kaydeder.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"çocukları yaşamayan veya hiçbir çocuğunu kendinden önce kaybetmemiş kişi"}],"lexicalization_note":"Dal yalın kişi adını kapsar; birbirine karşıt kaynak yorumları tek bir söz öbeği anlamına indirgenmez.","neighbor_coverage_note":"Adayların tümü incelendi; doğrudan çocuk ölümü ile hayvandaki yavru kaybı, dalın ana kullanımı ve kaynak çeşitleri için en yararlı iki sınırı verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal çocuk kaybıyla tanımlanan kişi adıdır ve ek yorumlar taşır; komşu dal çocuk ölümü olayını doğrudan bildirir.","focus_only":"Çocuğu yaşamayan ebeveyn için yerleşik bir kişi adı ve ayrıca karşıt kaynak yorumları bulunur.","gloss":"çocuk kaybıyla anılan ebeveyn","neighbor_only":"Bir çocuğun ölmesi olayı kadın, erkek veya dişi deve için doğrudan bildirilir.","neighbor_ref":"root_001454/B005","relation_type":"near_synonym","shared_zone":"İki dal ebeveynin çocuğunun ölmesi durumunu anlatır."},{"boundary_match":"field_only","distinction":"Bu dal insan ebeveyn için kullanılan adı merkez alır; komşu dal yalnızca yavrusunu yitiren dişi deveyi tanımlar.","focus_only":"Başlıca gönderim insan ebeveyndir ve kaynaklarda farklı insan durumları da bulunur.","gloss":"çocuğunu ve yavrusunu yitiren","neighbor_only":"Gönderim, yavrusu ölen, alınan veya düşen dişi devedir.","neighbor_ref":"root_000727/B002","relation_type":"near_neighbor","shared_zone":"İki dal yavru veya çocuk kaybıyla tanımlanan ebeveyni konu eder."}],"source_phrase_ar":"الرقوب المرأة التي لا يعيش لها ولد (maqayis;jamhara;sihah); الرقوب من الأرامل والشيوخ الذي لا ولد له ولا يستطيع الكسب ولم يقدم من ولده شيئا (ayn); الرقوب الذي لم يقدم من ولده شيئا ومعناه في كلامهم على فقد الأولاد (tahdhib)","source_summary":"Kanıtın çoğu çocukları yaşamayan ebeveyni tanımlar; diğer ifadeler çocuksuz ve kazançsız kişiyi veya çocuk kaybı yaşamamış kişiyi ayrı yorumlar olarak korur.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه الرقوب الذي لا يعيش له ولد، أو لم يقدم من ولده شيئا، وما قيل في الأرملة والشيخ بلا ولد ولا كسب","what_is_not_ar":"ليست المرأة التي ترقب موت الزوج ولا الناقة المتأخرة عن الماء"},"support_links":[]},{"boundary":"Kadın ve deve kullanımları ortak bekleme ilişkisini paylaşır, ancak biri diğerinin örneği değildir ve katılımcı sınırları ayrı tutulmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000584/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَقَبَة","morph_features":"STEM|POS:N|LEM:raqabap|ROOT:rqb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:2:1","qac_word_ref":"90:13:2","surface_ar":"رَقَبَةٍ"}],"gloss":"belirli bir sonucu bekleyen","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir sonucu bekleme."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eşinin ölümünü miras için veya başkasının yardımını bekleyen kadın."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kalabalık develer çekilene kadar suya yaklaşmayan dişi deve."}}],"root_ar":"ر ق ب","root_id":"root_000584","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kadın eşinin ölümünü ya da yardımı, bir dişi deve kalabalığın sudan çekilmesini beklediğinde genel üst anlatım olarak kullanılır.","boundary_detail":"Kadın ve deve kullanımları ortak bekleme ilişkisini paylaşır, ancak biri diğerinin örneği değildir ve katılımcı sınırları ayrı tutulmalıdır.","branch_image_ar":"الرَّقوب المنتظرة أو المتأخرة","concept_gloss":"belirli bir sonucu bekleyen","contextual_glosses":[{"applicability":"Kadının miras veya geçim desteği beklentisi özellikle anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadın katılımcıyı ve iki ayrı beklenti nedenini korur."},"facet_ids":["F002"],"text":"eşinin ölümünü veya yardımı bekleyen kadın","usage_role":"explanatory"},{"applicability":"Dişi devenin kalabalık yüzünden diğerleri çekilene kadar suya yanaşmaması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanı, su bağlamını ve gecikme koşulunu korur."},"facet_ids":["F003"],"text":"kalabalık çekilene kadar suya yaklaşmayan dişi deve","usage_role":"contextual"}],"definition":"Beklemesiyle nitelenen kadın veya dişi devedir: kadın eşinin ölümünü ya da bir yardımı bekler; dişi deve ise kalabalık çekilene kadar suya yaklaşmaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir sonucu bekleme."},{"facet_id":"F002","role":"specialization","statement":"Eşinin ölümünü miras için veya başkasının yardımını bekleyen kadın."},{"facet_id":"F003","role":"specialization","statement":"Kalabalık develer çekilene kadar suya yaklaşmayan dişi deve."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Çocuk kaybı anlamını ekler.","collision":"Çocukları yaşamayan ebeveyn dalıyla karışır.","fit":"displacement","loses":"Eş, yardım veya suyla ilgili bekleme davranışını bütünüyle kaybeder.","preserves":"Kadın için kullanılan aynı tarihî adın başka bir bağlamını çağrıştırır."},"text":"çocuğunu yitirmiş kadın"}],"identity_rationale":"Yetkili ifade, bekleme çekirdeğini iki farklı katılımcıda korur: eşinin ölümünü veya bir yardımı bekleyen kadın ve kalabalık çekilene kadar suya yaklaşmayan dişi deve.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"eşinin ölümünü veya bir yardımı bekleyen kadın"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"kalabalık çekilene kadar suya yaklaşmayan dişi deve"}],"lexicalization_note":"Yalın kişi adı kadın kullanımını taşır; deveye özgü bekleme anlamı belirli isim öbeğine bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel bekleme, develerin sudan geciktirilmesi ve evlilik bağlamındaki belirli süre en açıklayıcı üç sınırı sağladı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli kadın ve deve tiplerini adlandırır; komşu dal genel bekleme ve izleme eylemidir.","focus_only":"Kadın ve dişi deve için yerleşmiş, katılımcıya bağlı adlandırmalar bulunur.","gloss":"genel ve katılımcıya bağlı bekleme","neighbor_only":"Her türlü kişi, nesne, söz veya olay dikkatle beklenebilir.","neighbor_ref":"root_000584/B001","relation_type":"near_neighbor","shared_zone":"İki dal beklenen bir sonuç gerçekleşene kadar dikkatle durmayı paylaşır."},{"boundary_match":"field_only","distinction":"Bu dal kalabalığa bağlı davranışsal geri durmadır; komşu dal sulamanın zamanını bilinçli olarak ertelemektir.","focus_only":"Dişi deve kalabalık çekilene kadar kendi davranışıyla suya yaklaşmaz.","gloss":"suya yaklaşmayı geciktiren deve","neighbor_only":"Develerin susuzluk süresi dışarıdan bir veya daha fazla gün uzatılır.","neighbor_ref":"root_001493/B004","relation_type":"near_neighbor","shared_zone":"İki dal develerin suya erişmesindeki gecikmeyi anlatır."},{"boundary_match":"field_only","distinction":"Bu dal kadının durumunu adlandırır ve ölüm ya da yardım beklentisine dayanır; komşu dal hukukî nitelikte belirlenmiş bir bekleme süresidir.","focus_only":"Kadın eşinin ölümünü miras için veya başkasının yardımını bekler.","gloss":"kadının evlilik bağlamında beklemesi","neighbor_only":"Kadın, eşinin iktidarsızlığı durumunda belirlenen evlilik süresini bekler.","neighbor_ref":"root_000534/B003","relation_type":"same_field","shared_zone":"İki dal evli bir kadının eşle bağlantılı bir sonucu beklemesini içerir."}],"source_phrase_ar":"المرأة التي ترقب موت زوجها لترثه الرقوب والناقة التي ترقب متى تنصرف الإبل عن الماء (maqayis); الأرملة رقوب لأنها تترقب معروفا (ayn); الرقوب المرأة التي ترقب موت زوجها لترثه والرقوب من الإبل التي لا تدنو من الحوض (sihah); الرقوب الناقة التي لا تدنو إلى الحوض مع الزحام (tahdhib)","source_summary":"Kanıt, bekleme çekirdeğini kadın ve dişi deve kullanımlarında ortaklaştırır; beklenen sonuç ile davranış koşulu her kullanımda farklıdır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه المرأة التي ترقب موت زوجها أو معروفا، والناقة التي تترقب انصراف الإبل عن الماء أو لا تدنو من الحوض مع الزحام","what_is_not_ar":"ليس فقد الولد بذاته ولا الرقيب الحافظ"},"support_links":[]},{"boundary":"Dal genel olarak bütün yılanları değil, kaynakta ayrı bir tür adıyla gösterilen zararlı yılanı kapsar.","branch_kind":"bare","branch_ref":"root_000584/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَقَبَة","morph_features":"STEM|POS:N|LEM:raqabap|ROOT:rqb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:2:1","qac_word_ref":"90:13:2","surface_ar":"رَقَبَةٍ"}],"gloss":"zararlı bir yılan türü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Zararlı sayılan belirli bir yılan türü."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tür adının kaynakta iki ayrı çoğul biçimle kaydedilmesi."}}],"root_ar":"ر ق ب","root_id":"root_000584","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynakta ayrı bir tür adı olarak verilen kötü ve zararlı yılan anlatıldığında kullanılır.","boundary_detail":"Dal genel olarak bütün yılanları değil, kaynakta ayrı bir tür adıyla gösterilen zararlı yılanı kapsar.","branch_image_ar":"الرقيب من الحيات","concept_gloss":"zararlı bir yılan türü","contextual_glosses":[{"applicability":"Türün zararlı ve tehlikeli niteliği anlatıda öne çıkarıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yılan gönderimini ve olumsuz niteliğini korur."},"facet_ids":["F001"],"text":"kötücül yılan","usage_role":"contextual"}],"definition":"Kötü ve zararlı sayılan belirli bir yılan türünün adıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Zararlı sayılan belirli bir yılan türü."},{"facet_id":"F002","role":"source_variant","statement":"Tür adının kaynakta iki ayrı çoğul biçimle kaydedilmesi."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Koruma görevi yapan kişi anlamını ekler.","collision":"Koruyucu görevli dalıyla karışır.","fit":"displacement","loses":"Yılan türü gönderimini bütünüyle kaybeder.","preserves":"Aynı tarihî biçimin başka bir dalını çağrıştırır."},"text":"muhafız"}],"identity_rationale":"Yetkili ifade, adı kötü ve zararlı sayılan belirli bir yılan türüne verir ve bu adın iki çoğul biçimini kaydeder.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"zararlı bir yılan türü"}],"lexicalization_note":"Dal yalın hayvan adını kapsar; koruyucu kişi veya oyun görevlisi anlamları tanıma taşınmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; iri zararlı yılan ile deniz yılanı, türün niteliğini ve yaşam alanı sınırını karşılaştırmak için yeterli bulundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli bir tarihî tür adıdır; komşu dal irilik niteliğini ve daha geniş hayvan kullanımlarını da kapsar.","focus_only":"Kaynakta ayrı adı bulunan zararlı yılan türü belirtilir.","gloss":"iri ve zararlı yılan","neighbor_only":"Özellikle iri ve kötü yılanlar ile yılan-akrep ikilisi gibi daha geniş kullanımlar bulunur.","neighbor_ref":"root_000757/B007","relation_type":"near_synonym","shared_zone":"İki dal zararlı veya kötü sayılan yılan türlerini gösterir."},{"boundary_match":"field_only","distinction":"Bu dal zararlılık niteliğiyle, komşu dal ise deniz yaşam alanıyla sınırlandırılır.","focus_only":"Yaşam ortamı belirtilmeyen zararlı bir yılan türüdür.","gloss":"zararlı yılan ve deniz yılanı","neighbor_only":"Denizde yaşayan bir yılan türü olmakla sınırlandırılır.","neighbor_ref":"root_001037/B016","relation_type":"same_field","shared_zone":"İki dal ayrı yılan türlerini adlandırır."}],"source_phrase_ar":"الرقيب ضرب من الحيات وجمعه رقب ورقيبات (ayn); الرقيب ضرب من الحيات خبيث والجمع الرقيبات والرقب (tahdhib)","source_summary":"Kanıt, gönderimi zararlı bir yılan türü olarak ortaklaştırır ve adın iki ayrı çoğul biçimini birlikte kaydeder.","sources":["AY","TA"],"what_is_ar":"يدخل فيه الرقيب ضرب من الحيات الخبيث وجمعه رقب ورقيبات","what_is_not_ar":"ليس الرقيب الحافظ ولا رقيب الميسر"},"support_links":[]},{"boundary":"Dal genel örtüyü veya av tuzağını değil, atıcının avdan gizlenmek için kullandığı siperi adlandırır.","branch_kind":"bare","branch_ref":"root_000584/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَقَبَة","morph_features":"STEM|POS:N|LEM:raqabap|ROOT:rqb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:2:1","qac_word_ref":"90:13:2","surface_ar":"رَقَبَةٍ"}],"gloss":"avcı siperi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Avcıyı avdan gizleyen fiziksel siper."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gizlenmenin avı ok veya başka bir atışla vurma amacına bağlı olması."}}],"root_ar":"ر ق ب","root_id":"root_000584","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Avcının görünmeden atış yapmak için arkasına saklandığı nesne veya düzenek anlatıldığında kullanılır.","boundary_detail":"Dal genel örtüyü veya av tuzağını değil, atıcının avdan gizlenmek için kullandığı siperi adlandırır.","branch_image_ar":"الرقيبة ستر الصائد","concept_gloss":"avcı siperi","contextual_glosses":[{"applicability":"Siperin atıştan önce avcıyı görünmez kılma işlevi vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gizlenme aracını ve avlanma bağlamını korur."},"facet_ids":["F001","F002"],"text":"avlanma gizlenme siperi","usage_role":"explanatory"}],"definition":"Avcının avı vurabilmek için arkasına saklanıp kendini gizlediği siper veya örtüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Avcıyı avdan gizleyen fiziksel siper."},{"facet_id":"F002","role":"specialization","statement":"Gizlenmenin avı ok veya başka bir atışla vurma amacına bağlı olması."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Avı doğrudan yakalayan veya kıstıran düzenek anlamını ekler.","collision":"Av için kurulan kapanlarla karışır.","fit":"displacement","loses":"Avcının kendisini gizlemesi işlevini kaybeder.","preserves":"Avlanma amacını korur."},"text":"tuzak"}],"identity_rationale":"Tek kaynaklı yetkili ifade, avcı veya atıcının avı vurabilmek için arkasına saklandığı her türlü siperi açıkça tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"avcının arkasına saklandığı siper"}],"lexicalization_note":"Dal yalın araç adını kapsar ve başka avlanma araçlarının işlevleri tanıma eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eş anlamlı çiftlerden yalnız biri seçildi, genel örtü ve hayvan arkasında gizlenme de sınırı açıklamak için eklendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal atış sırasında kullanılabilen her türlü siperi kapsar; komşu dal özel olarak avcının gizlenme yerini veya hazırlanmış siperini adlandırır.","focus_only":"Avcının atış yapmak için kullandığı her türlü siper veya örtü kapsanır.","gloss":"avcı gizlenme yeri","neighbor_only":"Avcının gizlenmesi için hazırlanmış özel bir avcı siperi veya gizlenme yeri adlandırılır.","neighbor_ref":"root_000099/B007","relation_type":"near_synonym","shared_zone":"İki dal da avcının avdan saklanarak atış yaptığı siper veya gizlenme yerini tanımlar."},{"boundary_match":"partial","distinction":"Bu dal gizlenme aracını siper olarak adlandırır; komşu dal yaklaşma tekniğini ve hayvanın perde olarak kullanılmasını anlatır.","focus_only":"Avcı sabit veya taşınabilir bir siperin arkasına saklanır.","gloss":"siperle veya hayvanla gizlenme","neighbor_only":"Avcı bir hayvanı perde gibi kullanarak ava gizlice yaklaşır.","neighbor_ref":"root_000473/B003","relation_type":"near_neighbor","shared_zone":"İki dal avı ürkütmeden yaklaşmak veya vurmak için avcının görünmesini engeller."},{"boundary_match":"partial","distinction":"Bu dal avlanma ve atış amacıyla sınırlıdır; komşu dal genel örtme ve saklanma alanını kapsar.","focus_only":"Örtü özellikle avcının atış yaparken gizlenmesine yarar.","gloss":"özel av siperi ve genel örtü","neighbor_only":"Her türlü nesneyi örtme, kapatma veya kişinin genel olarak saklanması kapsanır.","neighbor_ref":"root_000674/B001","relation_type":"near_synonym","shared_zone":"İki dal görünmeyi engelleyen bir örtü veya siper işlevini paylaşır."}],"source_phrase_ar":"الرقيبة كل ما استترت به لترمي صيدا (jamhara)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, avcıyı atış sırasında gizleyen her türlü siperi kapsar."}],"source_summary":"Kanıt, aracın biçiminden çok işlevini belirler: avcı arkasına saklanır ve gizlenerek atış yapar.","sources":["JA"],"what_is_ar":"يدخل فيه الرقيبة، وهي ما يستتر به الرامي لرمي الصيد","what_is_not_ar":"ليست الرقبة العضو ولا المرقبة الموضع العالي"},"support_links":[]},{"boundary":"Anlam yalın bir öz veya boyun adına genellenemez; maldan verme söz öbeğine bağlıdır.","branch_kind":"collocation","branch_ref":"root_000584/B012","candidate_links":[{"candidate_id":"cand_0b94d2c52cf84cc13eac","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"رَقَبَة","morph_features":"STEM|POS:N|LEM:raqabap|ROOT:rqb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:2:1","qac_word_ref":"90:13:2","surface_ar":"رَقَبَةٍ"}],"gloss":"öz malından vermek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Verilen şeyin malın öz veya seçkin kısmından çıkması."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Anlamın maldan verme yapısına bağlı kalması."}}],"root_ar":"ر ق ب","root_id":"root_000584","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Verilen şeyin kişinin malının öz veya seçkin kısmından çıktığı yapıda kullanılır.","boundary_detail":"Anlam yalın bir öz veya boyun adına genellenemez; maldan verme söz öbeğine bağlıdır.","branch_image_ar":"رَقَبَة المال وخالصه","concept_gloss":"öz malından vermek","contextual_glosses":[{"applicability":"Malın öz veya seçkin kısmından yapılan verme özellikle açıklanmak istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişisel mülkiyet ile öz kısımdan verme ilişkisini korur."},"facet_ids":["F001","F002"],"text":"malının öz veya seçkin kısmından vermek","usage_role":"explanatory"}],"definition":"Bir şeyi, kişinin malının öz veya seçkin kısmından vermesini anlatan kalıplaşmış kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Verilen şeyin malın öz veya seçkin kısmından çıkması."},{"facet_id":"F002","role":"specialization","statement":"Anlamın maldan verme yapısına bağlı kalması."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Türkçede desteklenmeyen bir mal türü ekler.","collision":"Organ dalıyla karışır.","fit":"displacement","loses":"Malın öz ve kişiye ait kısmı anlamını bütünüyle kaybeder.","preserves":"Kaynak biçimin yüzeydeki organ çağrışımını yansıtır."},"text":"boyun malı"}],"identity_rationale":"Tek kaynaklı yetkili ifade, yalnızca bir kişinin malının öz veya seçkin kısmından verme yapısını destekler.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"malının öz kısmından"}],"lexicalization_note":"Tanım yalnızca kişinin malının öz kısmından verme yapısına bağlı tutulur ve yalın köke aktarılmaz.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; genel öz anlamı ile malın en iyi kısmı, kalıplaşmış yapının sahiplik ve verme sınırını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal maldan verme yapısına bağlıdır; komşu dal öz ve temel anlamını farklı varlıklara genelleyebilir.","focus_only":"Anlam yalnızca maldan verme yapısında kişinin öz varlığına bağlanır.","gloss":"öz mal ve genel öz","neighbor_only":"Bir şeyin özü, dayanağı veya bir topluluğun aslı genel olarak adlandırılabilir.","neighbor_ref":"root_000884/B007","relation_type":"near_synonym","shared_zone":"İki dal bir bütünün öz, seçkin veya temel kısmını gösterir."},{"boundary_match":"partial","distinction":"Bu dal sahiplik ve verme yapısını öne çıkarır; komşu dal malın üstün kalitesini öne çıkarır.","focus_only":"Malın sahibine ait öz kısmından verme eylemi belirtilir.","gloss":"öz mal ve en iyi mal","neighbor_only":"Malın en değerli ve en iyi parçaları seçim ve nitelik bakımından belirtilir.","neighbor_ref":"root_000432/B003","relation_type":"near_synonym","shared_zone":"İki dal malın sıradan olmayan, seçilmiş veya öz kısmını gösterir."}],"source_phrase_ar":"أعطى من رقبة ماله أي من خالصه (jamhara)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, vermenin kişinin malının öz kısmından yapıldığını belirtir."}],"source_summary":"Kanıt, malın herhangi bir bölümünü değil, öz veya seçkin kısmından yapılan vermeyi ifade eden dar bir yapıyı tanımlar.","sources":["JA"],"what_is_ar":"يدخل فيه قولهم من رقبة ماله أي من خالصه","what_is_not_ar":"ليس الرقبة العضو ولا الرقيق"},"support_links":["sup_b04130cf9f2d4b2b5fd5"]},{"boundary":"Dal, doğrudan ve seçkin baba çizgisinden mirası değil, yan akrabalıktan gelen malı veya doğrudan babalara dayanmayan saygınlığı anlatan yapıyla sınırlandırılmalıdır.","branch_kind":"collocation","branch_ref":"root_000584/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَقَبَة","morph_features":"STEM|POS:N|LEM:raqabap|ROOT:rqb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:2:1","qac_word_ref":"90:13:2","surface_ar":"رَقَبَةٍ"}],"gloss":"doğrudan baba çizgisi dışından miras almak","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Mirasın doğrudan ve seçkin baba çizgisi dışındaki bir kaynaktan gelmesi."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Malın yan akrabalık yoluyla miras alınması."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Saygınlığın doğrudan babalar seçkin olmadığı hâlde miras alınması."}}],"root_ar":"ر ق ب","root_id":"root_000584","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Miras kalan mal veya saygınlık doğrudan ve seçkin babalara bağlanmadığında üst anlatım olarak kullanılır.","boundary_detail":"Dal, doğrudan ve seçkin baba çizgisinden mirası değil, yan akrabalıktan gelen malı veya doğrudan babalara dayanmayan saygınlığı anlatan yapıyla sınırlandırılmalıdır.","branch_image_ar":"الإرث عن رقبة","concept_gloss":"doğrudan baba çizgisi dışından miras almak","contextual_glosses":[{"applicability":"Malın üstsoy yerine yan akrabalık yoluyla geçtiği durumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Malı ve yan akrabalık yoluyla mirası korur."},"facet_ids":["F002"],"text":"yan akrabadan mal miras almak","usage_role":"contextual"},{"applicability":"Kişinin miras sayılan saygınlığı doğrudan babalarının seçkinliğine dayanmadığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Saygınlık ile doğrudan baba çizgisi arasındaki olumsuz sınırı korur."},"facet_ids":["F003"],"text":"saygınlığı babalarından almamış olmak","usage_role":"explanatory"}],"definition":"Malın yan akrabalık yoluyla miras alınmasını veya saygınlığın kişinin doğrudan babaları seçkin olmadığı hâlde başka bir soy kaynağından gelmesini anlatan kalıplaşmış kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Mirasın doğrudan ve seçkin baba çizgisi dışındaki bir kaynaktan gelmesi."},{"facet_id":"F002","role":"specialization","statement":"Malın yan akrabalık yoluyla miras alınması."},{"facet_id":"F003","role":"specialization","statement":"Saygınlığın doğrudan babalar seçkin olmadığı hâlde miras alınması."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Mirasın seçkin doğrudan atalardan geldiği yönünde ters bir anlam ekler.","collision":"Yüksek soy ve ata saygınlığı dallarıyla karışır.","fit":"displacement","loses":"Doğrudan babaların seçkin olmaması ve yan akrabalık koşulunu kaybeder.","preserves":"Soy ile miras arasındaki ilişkiyi korur."},"text":"soylu atalardan miras almak"}],"identity_rationale":"Yetkili ifade, malın yan akrabalık yoluyla miras alınmasını ve saygınlığın doğrudan babalardan gelmemesini söyler; geçici çerçevenin uzak geçmişten kesintisiz saygınlık aktarımı iması bu karşıtlığı bulanıklaştırır.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"yan akrabadan mal veya doğrudan babalar dışından saygınlık miras almak"}],"lexicalization_note":"İki miras yorumu yalnızca verilen kalıplaşmış yapı içinde korunur ve yalın kök anlamına dönüştürülmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ata saygınlığı, iki yandan seçkin soy ve yüksek soy merkezi, yeniden çerçevelenen miras sınırını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal doğrudan baba çizgisinin saygınlık kaynağı olmadığını belirtir; komşu dal saygınlığı doğrudan ata birikimiyle tanımlar.","focus_only":"Saygınlık, doğrudan babalar seçkin olmadığı hâlde başka bir kaynaktan miras kalır.","gloss":"miras saygınlığı ve ata saygınlığı","neighbor_only":"Kişinin veya topluluğun saygınlığı doğrudan ataların başarıları, ahlakı, malı ve cömertliğiyle ölçülür.","neighbor_ref":"root_000318/B004","relation_type":"near_neighbor","shared_zone":"İki dal soy, ata ve toplumsal saygınlık ilişkisini konu eder."},{"boundary_match":"opposed","distinction":"Bu dal saygınlığı doğrudan seçkin babalara dayandırmaz; komşu dal seçkinliği her iki yakın soy çizgisinde de doğrular.","focus_only":"Doğrudan babaların seçkin olmadığı bir miras ilişkisi belirtilir.","gloss":"dolaylı ve doğrudan seçkin soy","neighbor_only":"Kişinin hem anne hem baba tarafından arı ve seçkin soydan geldiği belirtilir.","neighbor_ref":"root_000458/B011","relation_type":"polarity_pair","shared_zone":"İki dal saygınlığın yakın soy çizgisindeki konumunu karşıt yönlerden belirler."},{"boundary_match":"field_only","distinction":"Bu dal mirasın geliş yolunu sınırlar; komşu dal yüksek soyun kendisini ve kabile içindeki yerini anlatır.","focus_only":"Mirasın doğrudan baba çizgisi dışındaki kaynağı vurgulanır.","gloss":"dolaylı miras ve yüksek soy","neighbor_only":"Kabilenin yüksek soy ve şeref merkezi doğrudan adlandırılır.","neighbor_ref":"root_000166/B008","relation_type":"same_field","shared_zone":"İki dal soy ile toplumsal saygınlığın bağını işler."}],"source_phrase_ar":"ورث فلان مالا عن رقبة أي عن كلالة وورث مجدا عن رقبة إذا لم يكن آباؤه أمجادا (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, yan akrabadan gelen mal ile doğrudan babalara dayanmayan saygınlığı aynı kalıpta ayırır."}],"source_summary":"Kanıt, mal ve saygınlık nesnelerini ayırırken ikisinde de doğrudan baba çizgisinin dışından gelen miras ilişkisini korur.","sources":["TA"],"what_is_ar":"يدخل فيه ورث عن رقبة، أي عن كلالة أو من غير آباء أمجاد، وما جاء في المجد الموروث من وراء وراء","what_is_not_ar":"ليس تحرير الرقبة ولا خالص المال"},"support_links":[]},{"boundary":"Dal genel gözetleme değildir; iki harfin aynı anda bulunmasını veya düşmesini engelleyen teknik ölçü kuralıyla sınırlıdır.","branch_kind":"bare","branch_ref":"root_000584/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَقَبَة","morph_features":"STEM|POS:N|LEM:raqabap|ROOT:rqb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:2:1","qac_word_ref":"90:13:2","surface_ar":"رَقَبَةٍ"}],"gloss":"iki harften birini düşürme kuralı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki ölçü harfinden yalnız birinin düşüp diğerinin kalması."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İki harfin birlikte kalmasının veya birlikte düşmesinin dışlanması."}}],"root_ar":"ر ق ب","root_id":"root_000584","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Şiir ölçüsünde eşlenmiş iki harften yalnız birinin korunabildiği teknik durumda kullanılır.","boundary_detail":"Dal genel gözetleme değildir; iki harfin aynı anda bulunmasını veya düşmesini engelleyen teknik ölçü kuralıyla sınırlıdır.","branch_image_ar":"المراقبة في العروض","concept_gloss":"iki harften birini düşürme kuralı","contextual_glosses":[{"applicability":"Teknik terim yerine iki harf arasındaki karşılıklı kısıtı açıklamak gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Şiir ölçüsü bağlamını ve seçenekli düşme işlemini korur."},"facet_ids":["F001","F002"],"text":"ölçüde seçenekli harf düşmesi","usage_role":"explanatory"}],"definition":"Şiir ölçüsünde birlikte değerlendirilen iki harften birinin düşmesi, diğerinin kalması; ikisinin birden kalmaması veya düşmemesi kuralıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki ölçü harfinden yalnız birinin düşüp diğerinin kalması."},{"facet_id":"F002","role":"specialization","statement":"İki harfin birlikte kalmasının veya birlikte düşmesinin dışlanması."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bir nesneyi izleme eylemini ekler.","collision":"Bekleme ve izleme dalıyla karışır.","fit":"displacement","loses":"Şiir ölçüsü, iki harf ve seçenekli düşme kuralını bütünüyle kaybeder.","preserves":"Aynı tarihî biçimin gündelik çağrışımını korur."},"text":"gözetleme"}],"identity_rationale":"Tek kaynaklı yetkili ifade, şiir ölçüsünde yan yana değerlendirilen iki harften birinin düşüp diğerinin kalması kuralını açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"şiir ölçüsünde iki harften birinin düşüp diğerinin kalması"}],"lexicalization_note":"Yalın teknik ad yalnızca şiir ölçüsündeki iki harfli değişim kuralını taşır; gündelik izleme anlamı eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel harf düşmesi, belirli kalıp eksilmesi ve daha geniş ölçü kusuru, teknik kuralın sınırını yeterince açıklıyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal iki belirli harf arasında karşılıklı seçim kuralı kurar; komşu dal aradaki harfin düşmesiyle oluşan genel ölçü kaymasını anlatır.","focus_only":"Belirlenmiş iki harften yalnız biri düşebilir ve diğeri kalmak zorundadır.","gloss":"ölçüde harf düşmesi","neighbor_only":"İki harf arasındaki tek bir harfin düşmesiyle komşu seslerin yaklaşması yeterlidir.","neighbor_ref":"root_000627/B005","relation_type":"near_synonym","shared_zone":"İki dal şiir ölçüsünde bir harfin düşmesiyle oluşan yapısal değişimi anlatır."},{"boundary_match":"field_only","distinction":"Bu dal iki harfli karşılıklı kısıttır; komşu dal belirli kalıptaki tek ve önceden belirli harfin düşmesidir.","focus_only":"İki harf arasında hangisinin düşeceğini sınırlayan karşılıklı bir kural vardır.","gloss":"seçenekli ve belirli harf düşmesi","neighbor_only":"Belirli bir ölçü kalıbının sonundaki tek bir harfin düşmesi anlatılır.","neighbor_ref":"root_001308/B015","relation_type":"near_neighbor","shared_zone":"İki dal şiir ölçüsünde harf eksilmesini teknik bir değişim olarak ele alır."},{"boundary_match":"field_only","distinction":"Bu dal tanımlı ve seçenekli bir ölçü işlemidir; komşu dal farklı eksiklik ve uyak bozukluğu türlerini kapsar.","focus_only":"Kurallı biçimde iki harften biri düşer, diğeri kalır.","gloss":"ölçü kuralı ve ölçü kusuru","neighbor_only":"Şiir dizesinde eksiklik, ölçü gücü kaybı veya uyak hareketinde uyuşmazlık görülebilir.","neighbor_ref":"root_001274/B002","relation_type":"same_field","shared_zone":"İki dal şiirde ses veya ölçü yapısındaki değişiklikleri konu eder."}],"source_phrase_ar":"المراقبة في أجزاء الشعر عند التجزئة بين حرفين هو أن يسقط أحدهما ويثبت الآخر (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, şiir ölçüsünde iki harften birinin düşmesi ve ötekinin kalması koşulunu verir."}],"source_summary":"Kanıt, iki harf arasında seçenekli bir ölçü değişimi tanımlar: düşme ve kalma işlemleri aynı anda aynı yönde gerçekleşmez.","sources":["TA"],"what_is_ar":"يدخل فيه المراقبة في أجزاء الشعر، وهي سقوط أحد حرفين وثبوت الآخر دون اجتماعهما أو سقوطهما معا","what_is_not_ar":"ليس مراقبة الشيء ولا الرقيب الحارس"},"support_links":[]},{"boundary":"Dal önden giden öncüyü veya sürekli sıralanma sürecini değil, bir bütünün en son ya da geride kalan parçasını gösterir.","branch_kind":"mixed_non_bare","branch_ref":"root_000584/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَقَبَة","morph_features":"STEM|POS:N|LEM:raqabap|ROOT:rqb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:2:1","qac_word_ref":"90:13:2","surface_ar":"رَقَبَةٍ"}],"gloss":"sonda veya arkada kalan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bütünün en son veya geride kalan bölümü."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin ardından kalan çocukları veya akrabaları."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hareket eden bir şeyin arkasında kalan toz kuyruğu."}}],"root_ar":"ر ق ب","root_id":"root_000584","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin son bölümü, arkadaki izi veya bir kişinin ardından kalan yakınları için üst anlatım olarak kullanılır.","boundary_detail":"Dal önden giden öncüyü veya sürekli sıralanma sürecini değil, bir bütünün en son ya da geride kalan parçasını gösterir.","branch_image_ar":"رقيب الشيء آخره وخلفه","concept_gloss":"sonda veya arkada kalan","contextual_glosses":[{"applicability":"Bir nesnenin veya sürecin en arkadaki ve son kısmı kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bütün içindeki son konumu korur."},"facet_ids":["F001"],"text":"bir şeyin son bölümü","usage_role":"general"},{"applicability":"Bir kişinin sonrasında yaşayan aile üyeleri kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiden sonra kalan aile ardıllarını korur."},"facet_ids":["F002"],"text":"ardından kalan çocukları veya akrabaları","usage_role":"explanatory"}],"definition":"Bir şeyin en son veya geride kalan bölümü, izi ya da ardılıdır. Kişi için, ardından kalan çocuklarını veya akrabalarını gösterebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bütünün en son veya geride kalan bölümü."},{"facet_id":"F002","role":"extension","statement":"Kişinin ardından kalan çocukları veya akrabaları."},{"facet_id":"F003","role":"example","statement":"Hareket eden bir şeyin arkasında kalan toz kuyruğu."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Önden gitme yönünü ekler.","collision":"Ordunun öncü gözcüsü dalıyla karışır.","fit":"displacement","loses":"Sonda ve arkada kalma yönünü kaybeder.","preserves":"Bir topluluk içindeki göreli sıra konumunu korur."},"text":"öncü"}],"identity_rationale":"Tek kaynaklı yetkili ifade, bir şeyin son veya arkada kalan bölümünü temel alır; kişinin ardından kalan çocuk ve akrabaları ile tozun kuyruğunu bu ilişkinin özel kullanımları olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"bir şeyin sonu veya arkada kalan bölümü"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"kişinin ardından kalan çocukları veya akrabaları"}],"lexicalization_note":"Yalın ve tamlamalı kullanımlar şeyin sonunu, toz kuyruğunu ve kişinin ardında kalan yakınlarını ayrı bağlamlarda korur.","neighbor_coverage_note":"Bütün komşular değerlendirildi; kuyruk, genel arka bölüm ve art arda geliş, dalın sonluk ve ardıllık sınırlarını en iyi gösteren üç karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal sonluk ve ardıllık ilişkisini insan yakınlarına ve ize genişletir; komşu dal somut kuyruk biçimini ve ona benzeyen parçaları da kapsar.","focus_only":"Kişinin ardından kalan çocuk veya akrabalar ile toz kuyruğu da kapsanır.","gloss":"son bölüm ve kuyruk","neighbor_only":"Hayvanın gerçek kuyruğu ve kuyruğa benzeyen uzun ya da sarkık biçimler kapsanır.","neighbor_ref":"root_000521/B002","relation_type":"near_synonym","shared_zone":"İki dal bir şeyin arkada kalan son bölümünü gösterebilir."},{"boundary_match":"partial","distinction":"Bu dal en son kalan parça ve ardıl ilişkisini öne çıkarır; komşu dal nesnelerin ön-arka yönsel bölümlerini daha genel biçimde kapsar.","focus_only":"Son bölüm, ardından kalan yakın veya toz izi olabilir.","gloss":"son ve arka bölüm","neighbor_only":"Göz, eyer veya dişi devenin ön ve arka bölümleri gibi somut yönsel parçalar da adlandırılır.","neighbor_ref":"root_000019/B003","relation_type":"near_synonym","shared_zone":"İki dal bir bütünün arka veya son kısmını anlatır."},{"boundary_match":"field_only","distinction":"Bu dal son veya ardıl öğeyi adlandırır; komşu dal bütün dizinin art arda ilerleyişini anlatır.","focus_only":"Dizinin veya bütünün son ve arkada kalan öğesi belirtilir.","gloss":"son öğe ve art arda geliş","neighbor_only":"Birden çok öğenin aynı iz üzerinde art arda ilerleme süreci belirtilir.","neighbor_ref":"root_000762/B012","relation_type":"near_neighbor","shared_zone":"İki dal öğelerin birbirinin arkasında bulunması ilişkisini paylaşır."}],"source_phrase_ar":"رقيب الرجل خلفه من ولده أو عشيرته ورقيب كل شيء آخره ورقيب الغبار (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, şeyin sonunu, toz kuyruğunu ve kişinin ardından kalan çocuk ya da akrabaları birlikte kaydeder."}],"source_summary":"Kanıt, son ve geride kalma ilişkisini nesnenin bölümü, hareket izi ve kişinin ardından kalan yakınları üzerinde ortaklaştırır.","sources":["TA"],"what_is_ar":"يدخل فيه رقيب الرجل خلفه من ولده أو عشيرته، ورقيب كل شيء آخره، ورقيب الغبار","what_is_not_ar":"ليس الطليعة التي تتقدم الجيش ولا رقيب النجم"},"support_links":[]},{"boundary":"Bu dal genel açma ve ayırma eylemidir; rehin, kölelik, eklem ve çene adı gibi özel dallar onun tanımına katılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001173/B001","candidate_links":[{"candidate_id":"cand_db8c2f3de428fbe0d723","lane":"micro"},{"candidate_id":"cand_47bc2041da7a9ecc37e4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فَكّ","morph_features":"STEM|POS:N|LEM:fak~|ROOT:fkk|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:1:1","qac_word_ref":"90:13:1","surface_ar":"فَكُّ"}],"gloss":"kapalıyı açıp iç içe geçmişi ayırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kapalı veya mühürlü bir şeyi açma işlemini bildirir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birbirine geçmiş iki parçayı aralarını açarak ayırmayı bildirir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Açma ve ayırmanın sonucu olarak bağlı olanı kurtarma veya serbest bırakma yönüne genişler."}}],"root_ar":"ف ك ك","root_id":"root_001173","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın açma, ayırma ve bunun sonucunda serbest bırakma çekirdeğini birlikte karşılayan genel açıklamadır.","boundary_detail":"Bu dal genel açma ve ayırma eylemidir; rehin, kölelik, eklem ve çene adı gibi özel dallar onun tanımına katılmaz.","branch_image_ar":"فتح المغلق وفصل المشتبك","concept_gloss":"kapalıyı açıp iç içe geçmişi ayırma","contextual_glosses":[{"applicability":"Mühürlü veya kapalı bir nesnenin kapanmasını giderme bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kapalı durumun giderilmesi ve nesnenin açılması korunur."},"facet_ids":["F001"],"text":"açmak","usage_role":"contextual"},{"applicability":"Birbirine geçmiş iki parça arasındaki bağlantının çözülmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki bağlı parçanın aralarının açılarak ayrılması korunur."},"facet_ids":["F002"],"text":"birbirinden ayırmak","usage_role":"contextual"},{"applicability":"Bir bağın veya engelin kaldırılmasıyla bir şeyin serbest kalması öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Engellenmiş olanın bağdan kurtarılması sonucu korunur."},"facet_ids":["F003"],"text":"serbest bırakmak","usage_role":"contextual"}],"definition":"Kapalı ya da mühürlü bir şeyi açmak, birbirine geçmiş iki şeyi ayırmak ve böylece bağlı veya engellenmiş olanı serbest duruma getirmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kapalı veya mühürlü bir şeyi açma işlemini bildirir."},{"facet_id":"F002","role":"core","statement":"Birbirine geçmiş iki parçayı aralarını açarak ayırmayı bildirir."},{"facet_id":"F003","role":"extension","statement":"Açma ve ayırmanın sonucu olarak bağlı olanı kurtarma veya serbest bırakma yönüne genişler."}],"identity_rationale":"Kaynak ifadesi, kapalı bir şeyi açma ve birbirine geçmiş iki şeyi ayırma çekirdeğini açıkça doğrular; ayrıca bu işlemin bağlı olanı kurtarma ve serbest bırakma yönüne genişlediğini gösterir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kapalı şeyi açmak, kurtarmak veya serbest bırakmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"birbirine geçmiş iki şeyi ayırma"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"iki çeneyi birbirinden ayırmak"}],"lexicalization_note":"Tanım genel eylem çekirdeğini verir; iki çeneyi ayırma anlamı ise yalnız kendi yapısına bağlı özel bir gerçekleşme olarak tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan dört karşıtlık açma, yarma, düğüm çözme, kapatma ve özel kurtarma sınırlarını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bağlantıyı çözerek açma ve serbest bırakmayı bildirir; komşu dal ise nesneyi yarma, çatlatma veya iki parçaya bölme yönüyle sınırlandırılmıştır.","focus_only":"Kapalıyı açma, iç içe geçmişi çözme ve bağlı olanı serbest bırakma kapsamları vardır.","gloss":"açıp ayırma ile yarıp bölme","neighbor_only":"Bir bütünü yarıp parçalarını birbirinden ayıracak biçimde çatlatma veya bölme öne çıkar.","neighbor_ref":"root_001176/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir bütünün veya bağlı parçaların arasını açma sonucunu paylaşır."},{"boundary_match":"partial","distinction":"Odak dal kapatma, mühürleme ve iç içe geçme gibi farklı engelleri kapsar; komşu dalın çekirdeği düğümün ya da bağlanmış şeyin çözülmesidir.","focus_only":"Kapanmış nesneleri ve birbirine geçmiş her tür parçayı açıp ayırabilir.","gloss":"bağlantıyı ayırma ile düğüm çözme","neighbor_only":"Önceden bağlanmış bir düğümün çözülmesine özgü bir bağlanma geçmişi gerektirir.","neighbor_ref":"root_000351/B001","relation_type":"near_neighbor","shared_zone":"Her ikisi de sıkı bir bağlantıyı gevşetip parçaları ayrılabilir duruma getirir."},{"boundary_match":"opposed","distinction":"Odak dal kapalılığı ve bağlantıyı giderirken komşu dal açıklığı kapatıp kapalı durumu sağlamlaştırır.","focus_only":"Kapalı durumu giderip nesneyi açar veya bağlı parçaları ayırır.","gloss":"açma ve sıkıca kapatma","neighbor_only":"Kapıyı sıkıca kapatır ve yeniden açılmasını engelleyecek biçimde sağlamlaştırır.","neighbor_ref":"root_001653/B001","relation_type":"polarity_pair","shared_zone":"İki dal da bir açıklığın açık veya kapalı duruma getirilmesi ekseninde yer alır."},{"boundary_match":"partial","distinction":"Odak dal genel açma ve ayırma eylemidir; komşu dal bu sonucu rehin, esaret, kölelik ve tuzaktan kurtulma bağlamlarıyla sınırlar.","focus_only":"Her tür kapalı veya iç içe geçmiş nesneyi açıp ayıran genel işlem çekirdeğine sahiptir.","gloss":"genel çözme ile belirli bağdan kurtarma","neighbor_only":"Rehin, tutsaklık, kölelik veya tuzak gibi belirli bir bağdan kurtulmayı bildirir.","neighbor_ref":"root_001173/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir engelin giderilmesiyle serbest duruma geçme sonucu bulunur."}],"source_phrase_ar":"أصل صحيح يدل على تفتح وانفراج (maqayis)؛ فككت الشيء فانفك ككتاب مختوم تفك خاتمه وكما تفك الحنكين تفصل بينهما (ayn;tahdhib)؛ فككت الشئ خلصته وكل مشتبكين فصلتهما فقد فككتهما (sihah)؛ الفكك التفريج (mufradat)؛ كل شيء أطلقته فقد فككته (tahdhib)","source_summary":"Kaynaklar kapalı şeyi açma, birbirine geçmiş parçaları ayırma ve engellenmiş olanı serbest bırakma eksenlerinde birleşir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه فك الشيء المختوم أو المنغلق وفصل الحنكين أو كل شيئين مشتَبكين وإطلاق الشيء عموما","what_is_not_ar":"ليس فكاك الرهن والرقبة خاصة ولا لزوم ما انفك ولا اسم الفكّين"},"support_links":["sup_49d022c5d355ee805a34","sup_ff6b296e47bc6cef9f81"]},{"boundary":"Dal yalnız belirli bir hukuki, kişisel veya fiziksel bağdan kurtulmayı kapsar; genel ayırma eylemi ya da özgürlük durumu değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001173/B002","candidate_links":[{"candidate_id":"cand_d0a75656dc7218d3891b","lane":"micro"},{"candidate_id":"cand_0b94d2c52cf84cc13eac","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فَكّ","morph_features":"STEM|POS:N|LEM:fak~|ROOT:fkk|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:1:1","qac_word_ref":"90:13:1","surface_ar":"فَكُّ"}],"gloss":"rehni veya esaret altındakini bağından kurtarma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Rehni, üzerinde bulunan bağlayıcı durumdan çıkararak geri alınabilir hale getirmeyi bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tutsağı veya köleleştirilmiş kişiyi esaret bağından çıkarıp özgürleştirmeyi bildirir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tuzağa düşen bir hayvanın daha sonra tuzaktan sıyrılıp kurtulmasına uzanır."}}],"root_ar":"ف ك ك","root_id":"root_001173","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Rehin, tutsaklık, kölelik ve tuzakla sınırlı kurtulma alanını topluca karşılayan açıklamadır.","boundary_detail":"Dal yalnız belirli bir hukuki, kişisel veya fiziksel bağdan kurtulmayı kapsar; genel ayırma eylemi ya da özgürlük durumu değildir.","branch_image_ar":"تخليص الرهن والرقبة من الغلق والإسار","concept_gloss":"rehni veya esaret altındakini bağından kurtarma","contextual_glosses":[{"applicability":"Bir rehni üzerindeki bağlayıcı durumdan çıkarıp geri alma bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Rehnin bağlayıcı durumunun giderilip serbest hale gelmesi korunur."},"facet_ids":["F001"],"text":"rehni çözmek","usage_role":"contextual"},{"applicability":"Bir insanın esaret veya kölelik bağından çıkarılması bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin esaret bağından çıkarılıp özgür duruma getirilmesi korunur."},"facet_ids":["F002"],"text":"özgürlüğüne kavuşturmak","usage_role":"contextual"},{"applicability":"Hayvanın tuzağa düştükten sonra oradan sıyrılması bağlamıyla sınırlıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önce tuzağa düşme, ardından bağdan sıyrılıp kurtulma aşamaları korunur."},"facet_ids":["F003"],"text":"tuzaktan kurtulmak","usage_role":"contextual"}],"definition":"Bir rehni onu bağlı tutan yükümlülükten çıkarmak, bir insanı esaret veya kölelik bağından özgürleştirmek ya da tuzağa düşmüş bir hayvanın kurtulmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Rehni, üzerinde bulunan bağlayıcı durumdan çıkararak geri alınabilir hale getirmeyi bildirir."},{"facet_id":"F002","role":"specialization","statement":"Tutsağı veya köleleştirilmiş kişiyi esaret bağından çıkarıp özgürleştirmeyi bildirir."},{"facet_id":"F003","role":"extension","statement":"Tuzağa düşen bir hayvanın daha sonra tuzaktan sıyrılıp kurtulmasına uzanır."}],"identity_rationale":"Kaynak ifadesi rehni bağlılığından çıkarma, tutsağı veya köleleştirilmiş kişiyi özgürleştirme ve tuzağa düşmüş hayvanın kurtulması örneklerini aynı kurtarma alanında açıkça toplar.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"rehni bağlılığından kurtarmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"rehni çözme veya onu çözmek için verilen şey"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"rehni ya da tutsağı kurtarmaya yarayan şey"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kölelikten özgürlüğüne kavuşturmak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"ceylanın tuzağa düştükten sonra kurtulması"}],"lexicalization_note":"Tanım, rehin ve özgürleştirme yapılarıyla tuzaktan kurtulma birimini ayrı tutar; bunlardan genel bir yalın kök anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen dört karşıtlık dalı genel kurtulma, kölelikten özgürleşme, köleleştirme ve genel ayırma alanlarından sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal rehin, esaret, kölelik ve tuzak gibi belirli bağlara dayanır; komşu dal takılıp kalınan her tür durumdan kurtulmayı daha genel biçimde anlatır.","focus_only":"Rehni çözme ile bir insanı kölelik veya esaret bağından özgürleştirme kapsamları vardır.","gloss":"belirli bağdan kurtarma ve takıldığı yerden sıyrılma","neighbor_only":"Bir şeye takılıp kalmış kişi veya nesnenin genel olarak sıyrılıp selamete çıkmasını kapsar.","neighbor_ref":"root_000430/B002","relation_type":"near_synonym","shared_zone":"İki dal da önceden bağlanmış veya yakalanmış olanın engelden kurtulmasını bildirir."},{"boundary_match":"partial","distinction":"Odak dal özgürleştirmeyi farklı bağ çözme türlerinden biri olarak içerir; komşu dal bütünüyle kölelikten özgürlüğe geçiş ve özgür statüsü çevresinde kurulur.","focus_only":"Rehni çözme, tutsağı kurtarma ve tuzaktan sıyrılma gibi kölelik dışı kapsamları da vardır.","gloss":"bağdan kurtarma ve kölelikten özgürleşme","neighbor_only":"Kölelikten çıkmış kişinin özgür statüsünü ve bu statüye bağlı adlandırmaları da kapsar.","neighbor_ref":"root_000979/B001","relation_type":"near_synonym","shared_zone":"Köleleştirilmiş bir insanın özgürlüğüne kavuşturulması iki dalda da ortaktır."},{"boundary_match":"opposed","distinction":"Odak dal kölelik bağını sona erdirir; komşu dal o bağı kurar veya kölelik durumunu adlandırır.","focus_only":"Kişiyi kölelik bağından çıkarıp özgür duruma getirme işlemini bildirir.","gloss":"özgürleştirme ve köleleştirme","neighbor_only":"İnsanı mülk sayılan köle durumuna sokmayı veya bu durumda tutmayı bildirir.","neighbor_ref":"root_000586/B003","relation_type":"polarity_pair","shared_zone":"İki dal da kişinin kölelik bağı karşısındaki durumunu aynı eksende ele alır."},{"boundary_match":"partial","distinction":"Odak dal belirli bir bağ altında bulunan rehin, insan veya hayvanın kurtulmasını anlatır; komşu dal nesneler üzerindeki genel açma ve ayırma işlemini anlatır.","focus_only":"Rehin, esaret, kölelik ve tuzaktan kurtulma gibi belirli bağ türlerine bağlıdır.","gloss":"özel kurtarma ve genel açıp ayırma","neighbor_only":"Kapalı nesneyi açma ve iç içe geçmiş her tür parçayı ayırma genel kapsamına sahiptir.","neighbor_ref":"root_001173/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir bağlantının giderilmesiyle serbestlik sonucu ortaya çıkar."}],"source_phrase_ar":"فكاك الرهن وهو فتحه من الانغلاق (maqayis)؛ الفكاك الشيء الذي تفك به رهنا أو أسيرا وفككت رقبة فلان أعتقته (ayn)؛ فك الرهن وافتكه وفك الرقبة أي أعتقها (sihah)؛ فك الرقبة تخليصها من إسار الرق وفك الرهن وفكاكه تخليصه من غلق الرهن (tahdhib)؛ فك الرهن تخليصه وفك الرقبة عتقها (mufradat)؛ أفك الظبي من الحبالة إذا وقع فيه ثم انفلت (tahdhib)","source_summary":"Kaynaklar rehni çözme ile insanı esaret veya kölelikten kurtarma anlamlarında birleşir; tuzaktan kurtulan hayvan da aynı bağdan çıkma yönünü taşır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه فكاك الرهن والأسير والرقبة والعتق والانفلات من الحبالة","what_is_not_ar":"ليس مطلق فصل المشتبكين ولا اسم الفكّين ولا حمق الفَكّة"},"support_links":["sup_93392234eeda524a562c","sup_b04130cf9f2d4b2b5fd5"]},{"boundary":"Olumlu kullanım ayrılma veya sona ermeyi, olumsuz yardımcı yapı ise kesintisiz sürmeyi bildirir.","branch_kind":"mixed_non_bare","branch_ref":"root_001173/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"فَكّ","morph_features":"STEM|POS:N|LEM:fak~|ROOT:fkk|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:1:1","qac_word_ref":"90:13:1","surface_ar":"فَكُّ"}],"gloss":"ayrılma; olumsuz yapıda sürüp gitme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyden ayrılma, uzaklaşma veya onunla birlikteliği sona erdirme anlamını taşır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Olumsuz yardımcı yapıda eylem veya durumun kesilmeden sürmesini bildirir."}}],"root_ar":"ف ك ك","root_id":"root_001173","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın olumlu ayrılma anlamıyla olumsuz yapıya bağlı süreklilik anlamını birbirine karıştırmadan birlikte gösterir.","boundary_detail":"Olumlu kullanım ayrılma veya sona ermeyi, olumsuz yardımcı yapı ise kesintisiz sürmeyi bildirir.","branch_image_ar":"مفارقة الشيء أو نفي زواله","concept_gloss":"ayrılma; olumsuz yapıda sürüp gitme","contextual_glosses":[{"applicability":"Bir kişi veya şeyin bağlı bulunduğu şeyden uzaklaşması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Birlikteliğin sona ermesi ve tarafların birbirinden uzaklaşması korunur."},"facet_ids":["F001"],"text":"ayrılmak","usage_role":"contextual"},{"applicability":"Bir durumun veya bağlılığın artık devam etmemesi öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Durumun kesilmesi veya sona ulaşması anlamı korunur."},"facet_ids":["F001"],"text":"sona ermek","usage_role":"contextual"},{"applicability":"Yalnız olumsuz yardımcı yapıda bir eylemin kesilmeden devam ettiğini anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemin kesilmemesi ve zaman içinde devam etmesi korunur."},"facet_ids":["F002"],"text":"yapmayı sürdürmek","usage_role":"contextual"}],"definition":"Bir şeyden ayrılmak, uzaklaşmak veya bir durumu sona erdirmektir. Olumsuz yardımcı yapıda ise ayrılmanın ya da kesilmenin gerçekleşmediğini, eylem veya durumun sürdüğünü bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyden ayrılma, uzaklaşma veya onunla birlikteliği sona erdirme anlamını taşır."},{"facet_id":"F002","role":"specialization","statement":"Olumsuz yardımcı yapıda eylem veya durumun kesilmeden sürmesini bildirir."}],"identity_rationale":"Kaynak ifadesi bir şeyden ayrılma, uzaklaşma veya sona erme anlamını doğrular; ancak olumsuz yapıda aynı biçim ayrılmanın gerçekleşmediğini ve eylemin sürdüğünü bildirir. Bu iki kullanım tek ve çelişkisiz bir sonuç gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bir şeyden ayrılmak veya uzaklaşmak"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ayrılan, uzaklaşan veya sona erenler"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yapmayı sürdürmek, bırakmamak"}],"lexicalization_note":"Tanım ayrılma bildiren kullanımla yalnız olumsuz yapıda süreklilik bildiren kalıbı açıkça ayırır; kalıbın anlamını yalın biçime yaymaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen üç karşıtlık ayrılma, yer değiştirme, olumsuz süreklilik ve tamamlanma arasındaki temel sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bağlı olunan şeyden ayrılma ve sona ermeyi kapsar; komşu dalın olumlu çekirdeği bir yerden hareket edip ayrılmadır.","focus_only":"Bir şeyden ayrılma ve olumlu kullanımda sona erme kapsamını taşır.","gloss":"ayrılma ve yerinden ayrılma","neighbor_only":"Belirli bir yerden hareket edip uzaklaşma anlamını daha açık ve merkezi biçimde taşır.","neighbor_ref":"root_000102/B001","relation_type":"near_synonym","shared_zone":"Her iki dal olumlu kullanımda uzaklaşmayı, olumsuz yapıda ise sürmeyi bildirebilir."},{"boundary_match":"partial","distinction":"Odak dal süreklilik yanında olumlu ayrılma anlamını da taşır; komşu dal ise kanıtta yalnız olumsuz yapıyla kurulan süreklilik işlevine sahiptir.","focus_only":"Olumlu kullanımda ayrılma, uzaklaşma veya sona erme anlamı da vardır.","gloss":"olumsuz yapıda sürme","neighbor_only":"Süreklilik anlamı yalnız olumsuzlukla kullanılan kendi yardımcı yapısına bütünüyle bağlıdır.","neighbor_ref":"root_001123/B001","relation_type":"near_synonym","shared_zone":"İki dal da olumsuz yardımcı yapıda eylemin kesilmeden devam ettiğini bildirir."},{"boundary_match":"partial","distinction":"Odak dal ayrılma veya kesilmeyi anlatır ve olumsuz yapıda tersine süreklilik kazanır; komşu dal tamamlanma, tükenme veya sürenin dolması sonucunu gerektirir.","focus_only":"Bir şeyden ayrılma ile olumsuz yapıda devam etme karşıtlığını barındırır.","gloss":"sona erme ve tamamlanıp bitme","neighbor_only":"Bir işin tamamlanması, bir ihtiyacın görülmesi veya belirlenmiş sürenin dolması sonuçlarını taşır.","neighbor_ref":"root_001237/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da belirli bağlamlarda bir sürecin artık sürmemesi sonucuna yaklaşır."}],"source_phrase_ar":"لا ينفك يفعل ذلك بمعنى لا يزال (maqayis)؛ ما انفك فلان قائما أي ما زال قائما (sihah)؛ منفكين أي منتهين أو زائلين أو مفارقين (tahdhib)؛ منفكين أي لم يكونوا متفرقين وما انفك يفعل كذا نحو ما زال (mufradat)","source_summary":"Kaynaklar olumlu kullanımda ayrılma, uzaklaşma ve sona erme; olumsuz yardımcı kullanımda ise devam etme anlamlarını birlikte kaydeder.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الانفكاك عن الشيء بمعنى الزوال والمفارقة، وصيغ ما انفك ولا ينفك بمعنى لا يزال","what_is_not_ar":"ليس عتق الرقبة ولا انفراج المفصل ولا كواكب الفَكّة"},"support_links":[]},{"boundary":"Dal anatomik bir addır; çeneleri ayırma eylemi, eklem çıkması ve yaşlı kişiye ilişkin özel söz kalıbı çekirdek tanımı genişletmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001173/B004","candidate_links":[{"candidate_id":"cand_47bc2041da7a9ecc37e4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فَكّ","morph_features":"STEM|POS:N|LEM:fak~|ROOT:fkk|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:1:1","qac_word_ref":"90:13:1","surface_ar":"فَكُّ"}],"gloss":"çene kemiği ve çenelerin birleşme bölgesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ağzın alt ve üst bölümlerini oluşturan çene kemiğini veya iki çeneyi adlandırır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ağzın iki yanında çene ile ağız kenarının birleştiği bölgeleri bildirir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ağız-burun çıkıntısında iki çenenin bir araya geldiği noktayı adlandırır."}}],"root_ar":"ف ك ك","root_id":"root_001173","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çene kemiğiyle iki çenenin ağız çevresinde birleştiği anatomik bölgeleri birlikte karşılar.","boundary_detail":"Dal anatomik bir addır; çeneleri ayırma eylemi, eklem çıkması ve yaşlı kişiye ilişkin özel söz kalıbı çekirdek tanımı genişletmez.","branch_image_ar":"الفكّان وما بين الشدقين","concept_gloss":"çene kemiği ve çenelerin birleşme bölgesi","contextual_glosses":[{"applicability":"Tek bir çene kemiğinin veya iki çeneden birinin kastedildiği anatomik bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ağzın kemiksi çene bölümünün adlandırılması korunur."},"facet_ids":["F001"],"text":"çene kemiği","usage_role":"general"},{"applicability":"Ağız kenarlarının veya ağız-burun çıkıntısının çenelerle birleştiği nokta anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki çenenin ağız çevresinde bir araya geldiği anatomik yer korunur."},"facet_ids":["F002","F003"],"text":"çenelerin birleşme yeri","usage_role":"explanatory"}],"definition":"Çene kemiği ile ağzın iki yanında çene ve ağız kenarlarının birleştiği bölgedir; ayrıca ağız-burun çıkıntısında iki çenenin toplandığı yeri adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ağzın alt ve üst bölümlerini oluşturan çene kemiğini veya iki çeneyi adlandırır."},{"facet_id":"F002","role":"specialization","statement":"Ağzın iki yanında çene ile ağız kenarının birleştiği bölgeleri bildirir."},{"facet_id":"F003","role":"specialization","statement":"Ağız-burun çıkıntısında iki çenenin bir araya geldiği noktayı adlandırır."}],"identity_rationale":"Kaynak ifadesi çene kemiğini, ağzın iki yanındaki birleşme bölgelerini ve ağız-burun çıkıntısında iki çenenin toplandığı yeri aynı anatomik dal içinde doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"çene kemiği"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"iki çene ve ağzın iki yanındaki birleşme bölgeleri"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"ağız-burun çıkıntısında iki çenenin birleştiği yer"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yaşlılıktan çeneleri ayrılmış ihtiyar"}],"lexicalization_note":"Tanım anatomik adları kapsar; yaşlılıktan çenelerin ayrılmasını bildiren özel söz yalnız kendi yapısında lexical gloss olarak tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen dört anatomik karşıtlık çene kemiğini çene ucu, çeneler arası açıklık, çiğneme bölgesi ve damaktan ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal çene kemiği ve yan birleşme bölgelerini kapsar; komşu dal özellikle iki çenenin önde birleştiği çene ucudur.","focus_only":"Çene kemiğinin kendisini ve ağzın iki yanındaki çene birleşme bölgelerini kapsar.","gloss":"çene kemiği ve çene ucu","neighbor_only":"Alt çenenin ön-alt bölümünde iki çenenin birleştiği çıkıntıyı adlandırır.","neighbor_ref":"root_000515/B001","relation_type":"near_neighbor","shared_zone":"İki dal da iki çenenin yapısını ve birleştiği ağız altı bölgesini adlandırır."},{"boundary_match":"partial","distinction":"Odak dal kemik ve birleşme bölgesidir; komşu dal çenelerin arasında kalan açıklığı ya da o açıklığın açılmasını anlatır.","focus_only":"Çene kemiklerini ve onların ağız kenarlarıyla birleştiği bölgeleri adlandırır.","gloss":"çene yapısı ve çeneler arası açıklık","neighbor_only":"İki çene arasındaki boşluğu veya ağız açıklığını ve bu açıklığı açma işlemini bildirir.","neighbor_ref":"root_000777/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal çenelerin çevrelediği ağız bölgesine ilişkin anatomik bir alanı paylaşır."},{"boundary_match":"field_only","distinction":"Odak dal çene kemiği ve birleşme noktasıdır; komşu dal ağız yanındaki çiğneme bölgesine veya o bölgedeki damarlara özgüdür.","focus_only":"Çene kemiğinin tamamını ve iki çenenin birleşme bölgelerini kapsar.","gloss":"çene kemiği ve çiğneme bölgesi","neighbor_only":"Azı dişlerinin kökleri yakınındaki çiğneme bölgelerini veya oralardaki iki damarı adlandırır.","neighbor_ref":"root_001429/B003","relation_type":"same_field","shared_zone":"İki dal da yanağın ve çenenin ağız yanındaki anatomik yapılarını konu edinir."},{"boundary_match":"field_only","distinction":"Odak dal ağzın kemiksi çene çerçevesidir; komşu dal ağız boşluğunun içindeki damak bölgesidir.","focus_only":"Ağzı çevreleyen çene kemikleri ve bunların birleşme bölgeleridir.","gloss":"çene ve damak","neighbor_only":"Ağız boşluğunun üst-alt iç yüzünü ve en gerideki iç bölümünü adlandırır.","neighbor_ref":"root_000363/B001","relation_type":"same_field","shared_zone":"İki dal da ağız anatomisinin birbirine komşu yapılarını adlandırır."}],"source_phrase_ar":"الفكان ملتقى الشدقين (maqayis;ayn;mufradat)؛ الفك اللحي (sihah)؛ انكسر أحد فكيه أي لحييه (tahdhib)؛ الأفك مجمع الخطم وهو مجمع الفكين (ayn;tahdhib)","source_summary":"Kaynaklar çene kemiği ve iki çenenin birleşme bölgeleri üzerinde birleşir; farklı anlatımlar aynı ağız çevresi anatomisini değişik odaklarla tarif eder.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الفك واللحي والفكّان ملتقى الشدقين ومجمع الخطم والفكّين","what_is_not_ar":"ليس فعل الفصل ولا فكاك الرهن ولا الفَكّة الكوكبية"},"support_links":["sup_49d022c5d355ee805a34"]},{"boundary":"Dal eklem bağlantısının gevşemesi veya yerinden ayrılmasıdır; genel bedensel yumuşaklık, ayak eğriliği ve çene anatomisi değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001173/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"فَكّ","morph_features":"STEM|POS:N|LEM:fak~|ROOT:fkk|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:1:1","qac_word_ref":"90:13:1","surface_ar":"فَكُّ"}],"gloss":"eklemin gevşeyip yerinden ayrılması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ayak veya parmak ekleminin açılıp kemiğin olağan yerinden ayrılmasını bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Omuzun güçsüzlük veya gevşeklik yüzünden ekleminden ayrılmasını bildirir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişinin elini ekleminden çıkararak ayrılmaya neden olmayı bildirir."}}],"root_ar":"ف ك ك","root_id":"root_001173","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kendiliğinden veya dış etkiyle oluşan eklem açılması ve yerinden çıkma çekirdeğini karşılar.","boundary_detail":"Dal eklem bağlantısının gevşemesi veya yerinden ayrılmasıdır; genel bedensel yumuşaklık, ayak eğriliği ve çene anatomisi değildir.","branch_image_ar":"انفراج المفصل واسترخاء العضو","concept_gloss":"eklemin gevşeyip yerinden ayrılması","contextual_glosses":[{"applicability":"Ayak, parmak veya omuzun eklem bağlantısından kendiliğinden ayrılması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uzvun eklemdeki olağan yerinden ayrılması korunur."},"facet_ids":["F001","F002"],"text":"ekleminden çıkmak","usage_role":"general"},{"applicability":"Dışarıdan bir etkiyle el gibi bir uzvun eklem bağlantısını ayırma bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir etkenin uzvu eklemindeki yerinden ayırması korunur."},"facet_ids":["F003"],"text":"ekleminden çıkarmak","usage_role":"contextual"}],"definition":"Ayak, parmak, el veya omuz gibi bir uzvun eklem bağlantısının gevşeyip açılması ya da kemiğin eklemdeki yerinden ayrılmasıdır; geçişli kullanım bu ayrılmaya neden olmayı bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ayak veya parmak ekleminin açılıp kemiğin olağan yerinden ayrılmasını bildirir."},{"facet_id":"F002","role":"specialization","statement":"Omuzun güçsüzlük veya gevşeklik yüzünden ekleminden ayrılmasını bildirir."},{"facet_id":"F003","role":"extension","statement":"Bir kişinin elini ekleminden çıkararak ayrılmaya neden olmayı bildirir."}],"identity_rationale":"Kaynak ifadesi ayağın veya parmağın yerinden ayrılmasını, omuzun güçsüzlük ya da gevşeklikle ekleminden açılmasını ve el ekleminin yerinden çıkarılmasını aynı eklem ayrılması alanında doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"ayağı ekleminden ayrıldı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"omuz ekleminin gevşeyip ayrılması veya ayağın çıkması"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"elini ekleminden çıkardım"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"omzu gevşeyip ekleminden ayrılmış kimse"}],"lexicalization_note":"Tanım kendiliğinden eklem ayrılmasıyla bir uzvu ekleminden çıkarma yapısını ayırır; özel uzuv örneklerini bütün köke yaymaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen dört karşıtlık eklem çıkmasını genel uzuv çözülmesi, bitişikten ayrılma, sarkma ve özel kalça bağlantısından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli eklemlerin açılması ve çıkarılmasıdır; komşu dal eklem kaybı yanında gevşek yürüyüş ve daha geniş uzuv çözülmesi belirtilerini de kapsar.","focus_only":"Ayak, parmak, el ve özellikle gevşemiş omuz ekleminin ayrılmasına odaklanır.","gloss":"eklem çıkması ve uzuvların çözülmesi","neighbor_only":"Bozuk yürüyüşü, genel uzuv gevşekliğini ve bazı hayvan ya da yaşlılık durumlarını da kapsar.","neighbor_ref":"root_000432/B008","relation_type":"near_synonym","shared_zone":"İki dal da uzvun gevşemesi veya kemiğin eklemdeki yerinden ayrılmasını bildirir."},{"boundary_match":"partial","distinction":"Odak dal eklem bağlantısının bozulmasına özgüdür; komşu dal temas eden parçaların genel aralanmasını anlatır ve eklem çıkmasını gerektirmez.","focus_only":"Bir kemiğin eklem bağlantısında gevşeyip olağan yerinden ayrılmasını gerektirir.","gloss":"eklemden çıkma ve bitişikten ayrılma","neighbor_only":"Bir uzvun veya nesne parçasının bitişiğinden uzaklaşmasını eklem koşulu olmadan kapsar.","neighbor_ref":"root_000170/B008","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir beden parçasının komşu olduğu yapıdan aralanması sonucu vardır."},{"boundary_match":"field_only","distinction":"Odak dal gevşekliğin eklem çıkmasına yol açtığı anatomik durumdur; komşu dal alt kısmın sarkması veya salınmasıdır.","focus_only":"Gevşeklik eklem bağlantısını açar ve kemiği olağan konumundan ayırır.","gloss":"eklem gevşemesi ve sarkma","neighbor_only":"Bir şeyin alt bölümünün gevşeyip sarkmasını eklem ayrılması olmadan bildirir.","neighbor_ref":"root_000763/B001","relation_type":"same_field","shared_zone":"İki dal da yapısal sıkılığın azalması ve gevşeme alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal birden çok uzvun eklemden çıkmasını bildirir; komşu dal kalçadaki özel anatomik bağlantı ve onun kopmasıyla sınırlıdır.","focus_only":"Ayak, parmak, el ve omuz gibi farklı eklemlerin ayrılmasını kapsar.","gloss":"genel eklem çıkması ve kalça bağlantısı","neighbor_only":"Kalça çevresindeki belirli sinir veya kemik başlarına ve bunların kopmasına özgüdür.","neighbor_ref":"root_000311/B007","relation_type":"near_neighbor","shared_zone":"İki dal da bir uzvun eklem veya bağlantı bölgesindeki ayrılmasını konu edinir."}],"source_phrase_ar":"انفكت قدمه أي انفرجت (maqayis)؛ الفك انفراج المنكب عن مفصله ضعفا (maqayis)؛ الفكك انفراج المنكب عن مفصله ضعفا أو استرخاء (ayn)؛ انفكت قدمه أو إصبعه إذا انفرجت وزالت والفكك انفساخ القدم (sihah)؛ فككت يده فكا إذا أزال المفصل (tahdhib)؛ الفكك انفراج المنكب عن مفصله ضعفا (mufradat)","source_summary":"Kaynaklar eklemin gevşeyip açılması ve kemiğin yerinden ayrılması üzerinde birleşir; ayak, parmak, omuz ve el bu durumun farklı gerçekleşmeleridir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه انفكاك القدم أو الإصبع أو اليد، وانفراج المنكب عن مفصله ضعفا أو استرخاء","what_is_not_ar":"ليس الفكّين اسما للحيين ولا الفَكّة بمعنى الحمق ولا الرهن والرقبة"},"support_links":[]},{"boundary":"Çekirdek düşünce ve davranışta gevşeklik, tutarsızlık ve aptallıktır; kadınsılık bağlantısı yalnız kayıtlı bir yan nitelemedir.","branch_kind":"mixed_non_bare","branch_ref":"root_001173/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"فَكّ","morph_features":"STEM|POS:N|LEM:fak~|ROOT:fkk|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:1:1","qac_word_ref":"90:13:1","surface_ar":"فَكُّ"}],"gloss":"düşünce ve davranışta gevşek, tutarsız aptallık","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Düşünce veya davranışta gevşeklik, tutarsızlık ve aptallık bulunmasını bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin bildiğiyle bilmediğini ayırmadan konuşması ve yanlışlarının doğrularından çok olmasıyla belirginleşir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bazı kullanımlarda kişideki gevşeklik, kadınsı sayılan tavır veya görünüşle ilişkilendirilir."}}],"root_ar":"ف ك ك","root_id":"root_001173","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın zihinsel sağlamlık eksikliği, tutarsızlık ve aptallık çekirdeğini karşılayan genel açıklamadır.","boundary_detail":"Çekirdek düşünce ve davranışta gevşeklik, tutarsızlık ve aptallıktır; kadınsılık bağlantısı yalnız kayıtlı bir yan nitelemedir.","branch_image_ar":"فَكَّة الرأي والحمق والرخاوة","concept_gloss":"düşünce ve davranışta gevşek, tutarsız aptallık","contextual_glosses":[{"applicability":"Kişinin düşünce ve davranışında sağlamlık bulunmadığı genel niteleme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aptallık ile düşünce ve davranıştaki tutarsızlık birlikte korunur."},"facet_ids":["F001"],"text":"aptal ve tutarsız","usage_role":"general"},{"applicability":"Kişinin doğru bilgisini bilgisizliğinden ayırmadan konuşması ve çok yanılması öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Denetimsiz konuşma ve yanlışın doğrudan fazla olması korunur."},"facet_ids":["F002"],"text":"bilip bilmeden konuşan","usage_role":"explanatory"},{"applicability":"Yalnız tarihsel kullanımın gevşekliği kadınsı kabul edilen tavırla ilişkilendirdiği bağlamı açıklar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kaynakta kayıtlı kadınsılık bağlantısı ve gevşek tavır nitelemesi korunur."},"facet_ids":["F003"],"text":"kadınsı sayılan gevşek tavırlı","usage_role":"explanatory"}],"definition":"Bir kişinin düşüncesinde veya davranışında yeterli tutarlılık ve sağlamlık bulunmaması, bunun aptallık, gevşeklik ve doğruyla yanlışı ayıramayan konuşma olarak görünmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Düşünce veya davranışta gevşeklik, tutarsızlık ve aptallık bulunmasını bildirir."},{"facet_id":"F002","role":"specialization","statement":"Kişinin bildiğiyle bilmediğini ayırmadan konuşması ve yanlışlarının doğrularından çok olmasıyla belirginleşir."},{"facet_id":"F003","role":"source_variant","statement":"Bazı kullanımlarda kişideki gevşeklik, kadınsı sayılan tavır veya görünüşle ilişkilendirilir."}],"identity_rationale":"Kaynak ifadesi aptallık, düşüncede gevşeklik ve tutarlılık eksikliğini açıkça destekler; bir kayıt bu gevşekliği kadınsı sayılan tavırla da ilişkilendirir. Bu tarihsel niteleme dalın zihinsel çekirdeğiyle özdeşleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"onda kadınsı sayılan bir gevşeklik var"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"düşünce veya tavırda gevşeklik ve aptallık"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"aptal"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"aptalca ve tutarsız davranmak"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bilip bilmeden konuşan, yanlışı doğrusundan çok aptal"}],"lexicalization_note":"Tanım zihinsel ve davranışsal gevşeklik çekirdeğini verir; kişi nitelemeleri ile kalıplaşmış aptallık ifadeleri kendi kapsamlarında tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen dört karşıtlık bu dalı zayıf görüş, ağır aptallık ve genel yumuşaklık alanlarından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal zihinsel ve davranışsal tutarsızlığı genişçe betimler; komşu dal aptallık ile zayıf görüşe odaklanan daha dar bir nitelemedir.","focus_only":"Davranışta gevşeklik, tutarsız konuşma ve kadınsı sayılan tavır bağlantısını da kapsar.","gloss":"aptallık ve zayıf görüş","neighbor_only":"Belirli bir dil anlatısı içinde zayıf görüş nitelemesine dayanan özel kullanım taşır.","neighbor_ref":"root_001360/B003","relation_type":"near_synonym","shared_zone":"İki dal da kişide aptallık veya düşünce gücünün zayıflığını bildirir."},{"boundary_match":"partial","distinction":"Odak dal aptallığı davranışsal tutarsızlık ve denetimsiz konuşmayla birleştirir; komşu dal düşünce ile bedenin birlikte gevşeyip güçsüzleşmesini öne çıkarır.","focus_only":"Aptallık, tutarsız davranış ve denetimsiz konuşma anlamlarını birlikte taşır.","gloss":"tutarsız aptallık ve düşünce-beden gevşekliği","neighbor_only":"Düşüncedeki zayıflıkla birlikte bedensel gevşeklik ve uyuşukluğu da kapsar.","neighbor_ref":"root_001522/B003","relation_type":"near_synonym","shared_zone":"Her iki dal kişinin düşünme gücündeki gevşeklik ve zayıflığı bildirir."},{"boundary_match":"partial","distinction":"Odak dalda ayırıcı nitelik zihinsel gevşeklik ve tutarsızlıktır; komşu dalda aptallığa ağırlık ve hantallık eşlik eder.","focus_only":"Gevşeklik, tutarsızlık ve düşünmeden konuşma gibi belirtileri kapsar.","gloss":"gevşek aptallık ve ağır aptallık","neighbor_only":"Aptallığı ayrıca ağır ve hantal olma niteliğiyle birleştirir.","neighbor_ref":"root_000983/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir kişiyi aptallıkla niteleyen yakın anlamlı bir alan paylaşır."},{"boundary_match":"partial","distinction":"Odak dal insanın aptal ve tutarsız tutumudur; komşu dal fiziksel nesnelerden zihinsel zayıflığa uzanan genel yumuşaklık ve gevşeklik niteliğidir.","focus_only":"Bir kişinin düşünce ve davranışındaki aptallık ve tutarsızlığı gerektirir.","gloss":"zihinsel gevşeklik ve genel yumuşaklık","neighbor_only":"Nesnelerdeki fiziksel yumuşaklık ve gevreklik dahil daha genel bir gevşeklik alanına sahiptir.","neighbor_ref":"root_000553/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal soyut olarak zihinsel sağlamlığın azalmasını ve gevşekliği anlatabilir."}],"source_phrase_ar":"في فلان فكك أي أناثة واستراخاء (ayn)؛ الفكة الحمق والاسترخاء وما كنت فاكا فأنت فاك تاك أي أحمق (sihah)؛ فلان فكة أي استرخاء في رأيه وأحمق فاك وهاك (tahdhib)","source_summary":"Kaynaklar aptallık ve düşüncede gevşeklik üzerinde birleşir; tutarsız konuşma bu çekirdeği somutlaştırır, kadınsı sayılan tavır ise sınırlı bir yan nitelemedir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه وصف الإنسان بالحمق وقلة التماسك والاسترخاء في الرأي أو الهيئة والأنوثة","what_is_not_ar":"ليس انفراج المفصل المحسوس ولا تفكك الدابة ولا الفَكّة من الكواكب"},"support_links":[]},{"boundary":"Dal yalnız kanıtlanan hayvan nitelemelerine bağlıdır; doğuma yaklaşma, çiftleşme isteği ve zayıflık ayrı alt kullanımlardır.","branch_kind":"collocation","branch_ref":"root_001173/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"فَكّ","morph_features":"STEM|POS:N|LEM:fak~|ROOT:fkk|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:1:1","qac_word_ref":"90:13:1","surface_ar":"فَكُّ"}],"gloss":"hayvanda doğum, çiftleşme isteği veya zayıflığa bağlı çözülme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Doğumu yaklaşan dişi devenin sağrı bağlarının gevşemesi, memesinin büyümesi ve doğum vaktinin yaklaşmasını bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişi devenin veya kısrağın çiftleşme isteğinin çok güçlü olmasına ve erkeği geri çevirmemesine ilişkin bir nitelemedir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dişi veya erkek devenin zayıflık yüzünden güçten düşüp bitkin olmasını bildirir."}}],"root_ar":"ف ك ك","root_id":"root_001173","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız üç kanıtlı hayvan yapısını ortak gevşeme ve güçten düşme yönleriyle özetleyen açıklamadır.","boundary_detail":"Dal yalnız kanıtlanan hayvan nitelemelerine bağlıdır; doğuma yaklaşma, çiftleşme isteği ve zayıflık ayrı alt kullanımlardır.","branch_image_ar":"تفكك الدابة عند النتاج أو الضبعة والهزال","concept_gloss":"hayvanda doğum, çiftleşme isteği veya zayıflığa bağlı çözülme","contextual_glosses":[{"applicability":"Sağrı bağları gevşeyen, memesi büyüyen ve doğumu yaklaşan dişi deve için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğuma yaklaşma, sağrıdaki gevşeme ve memenin büyümesi birlikte korunur."},"facet_ids":["F001"],"text":"doğumu yaklaşmış ve bedeni gevşemiş","usage_role":"explanatory"},{"applicability":"Erkek hayvanı geri çevirmeyen dişi deve veya kısrağın çiftleşme isteğini bildirir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dişi hayvanın çiftleşme isteği ve erkeği geri çevirmemesi korunur."},"facet_ids":["F002"],"text":"çiftleşmeye istekli","usage_role":"contextual"},{"applicability":"Dişi veya erkek devenin aşırı zayıflık yüzünden güçten düşmesini anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Zayıflık nedeniyle oluşan güçsüzlük ve bitkinlik korunur."},"facet_ids":["F003"],"text":"zayıflıktan bitkin","usage_role":"contextual"}],"definition":"Hayvanlara ilişkin yapılarda, dişi devenin doğum yaklaşınca sağrı bağlarının gevşeyip memesinin büyümesini, kısrağın çiftleşmeye istekli olup aygırı geri çevirmemesini veya devenin zayıflıktan bitkin düşmesini bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Doğumu yaklaşan dişi devenin sağrı bağlarının gevşemesi, memesinin büyümesi ve doğum vaktinin yaklaşmasını bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Dişi devenin veya kısrağın çiftleşme isteğinin çok güçlü olmasına ve erkeği geri çevirmemesine ilişkin bir nitelemedir."},{"facet_id":"F003","role":"specialization","statement":"Dişi veya erkek devenin zayıflık yüzünden güçten düşüp bitkin olmasını bildirir."}],"identity_rationale":"Kaynak ifadesi hayvanlara bağlı üç ayrı nitelemeyi destekler: doğumu yaklaşan dişi devenin bedensel gevşemesi, çiftleşmeye istekli kısrağın aygırı geri çevirmemesi ve zayıflıktan bitkin deve. Bunlar tek bir fizyolojik süreç gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"doğumu yaklaşmış, sağrı bağları gevşeyip memesi büyümüş dişi deve"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"çiftleşmeye istekli olup aygırı geri çevirmeyen kısrak"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"zayıflıktan bitkin dişi veya erkek deve"}],"lexicalization_note":"Tanım bütünüyle hayvan adlarıyla kurulan yapılara bağlıdır; bu üç nitelemeden yalın ve genel bir kök anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen dört karşıtlık zayıflık, gebeliğin zayıflatması, çiftleşme eylemi ve gebelik durumu sınırlarını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda zayıflık üç hayvan yapısından yalnız biridir; komşu dalın çekirdeği bedendeki yağın azalmasıyla oluşan genel zayıflıktır.","focus_only":"Doğum öncesi gevşeme ve çiftleşmeye istekli dişi hayvan nitelemelerini de kapsar.","gloss":"bitkin hayvan ve genel zayıflık","neighbor_only":"Zayıflığı yağın ve etin azalması olarak genel biçimde adlandırır ve buna neden olmayı da kapsar.","neighbor_ref":"root_001589/B002","relation_type":"near_synonym","shared_zone":"İki dal da dişi veya erkek bir hayvanın zayıflayıp güçten düşmesini bildirebilir."},{"boundary_match":"partial","distinction":"Odak dal doğuma yaklaşmanın bedensel belirtilerini verir ve gebeliği zayıflığın zorunlu nedeni saymaz; komşu dal doğrudan gebeliğin hayvanı zayıflatmasıdır.","focus_only":"Doğum yaklaşınca bedensel gevşemeyi ve ayrıca çiftleşme isteği ile genel bitkinliği kapsar.","gloss":"doğum öncesi gevşeme ve gebeliğin zayıflatması","neighbor_only":"Zayıflığın özellikle gebeliğin bedeni tüketmesinden kaynaklanmasını gerektirir.","neighbor_ref":"root_000341/B007","relation_type":"near_neighbor","shared_zone":"İki dal gebe dişi hayvanın doğum süreci çevresindeki bedensel zayıflamaya yaklaşır."},{"boundary_match":"thematic_only","distinction":"Odak dal dişinin çiftleşme isteğine açık durumudur; komşu dal erkeğin dişiyle gerçekleştirdiği fiziksel çiftleşme eylemidir.","focus_only":"Dişi hayvanın çiftleşmeye hazır ve erkeği geri çevirmeyen durumunu niteler.","gloss":"çiftleşmeye açıklık ve çiftleşme eylemi","neighbor_only":"Erkek hayvanın dişiyle çiftleşme eylemini ve bu eylemde zorlanmasını bildirir.","neighbor_ref":"root_000431/B005","relation_type":"thematic","shared_zone":"İki dal aynı hayvan çiftleşmesi senaryosunda dişi ve erkek katılımcıları içerir."},{"boundary_match":"field_only","distinction":"Odak dal gebeliğin sonundaki doğum belirtilerine özgüdür; komşu dal yalnız gebe olma durumunu adlandırır.","focus_only":"Doğumun yaklaşmasına eşlik eden gevşeme ve meme büyümesi gibi belirtileri bildirir.","gloss":"doğumu yaklaşan ve gebe dişi deve","neighbor_only":"Dişi devenin gebe olduğunu adlandırır, doğumun yakınlığını veya bedensel gevşemeyi gerektirmez.","neighbor_ref":"root_000884/B018","relation_type":"same_field","shared_zone":"İki dal gebelik ve doğum süreci içindeki dişi deveyi konu edinir."}],"source_phrase_ar":"ناقة متفككة إذا أقربت فاسترخى صلواها وعظم ضرعها ودنا نتاجها؛ ذهب بعضهم بتفكك الناقة إلى شدة ضبعتها؛ المتفككة من الخيل الوديق التي لا تمتنع على الفحل؛ الفاك المعيي هزالا ناقة فاكة وجمل فاك","source_qualifications":[{"kind":"sole_attestation","summary":"Kayıt, doğumu yaklaşan dişi devenin gevşemesini aktarır; bazıları aynı deve ifadesini güçlü çiftleşme isteğiyle yorumlar. Ayrıca çiftleşmeye istekli kısrağı ve zayıflıktan bitkin deveyi ayrı kullanımlar olarak tanıklar."}],"source_summary":"Bu dalın kanıtı tek bir kaynak kaydına dayanır; üç ayrı hayvan nitelemesi aşağıda tekil tanıklık olarak birlikte belirtilir.","sources":["TA"],"what_is_ar":"يدخل فيه تفكك الناقة والخيل عند قرب النتاج أو الضبعة، ووصف الناقة والجمل بالهزال","what_is_not_ar":"ليس حمق الإنسان ولا انفراج مفصل المنكب ولا فكاك الرهن"},"support_links":[]},{"boundary":"Dal belirli bir yuvarlak yıldız kümesinin adıdır; genel yıldız, gök bölgesi, halka veya her türlü dairesel düzen değildir.","branch_kind":"bare","branch_ref":"root_001173/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"فَكّ","morph_features":"STEM|POS:N|LEM:fak~|ROOT:fkk|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:1:1","qac_word_ref":"90:13:1","surface_ar":"فَكُّ"}],"gloss":"Yoksulların Tası denen yuvarlak yıldız kümesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gökyüzünde yuvarlak biçimde dizilmiş belirli bir yıldız topluluğunu adlandırır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yıldız topluluğunun yuvarlak görünümü tas benzetmesine dayanan geleneksel bir adla da belirtilir."}}],"root_ar":"ف ك ك","root_id":"root_001173","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli yıldız topluluğunu biçimi ve geleneksel adıyla tanıtan en kısa açıklamadır.","boundary_detail":"Dal belirli bir yuvarlak yıldız kümesinin adıdır; genel yıldız, gök bölgesi, halka veya her türlü dairesel düzen değildir.","branch_image_ar":"الفَكّة من الكواكب المستديرة","concept_gloss":"Yoksulların Tası denen yuvarlak yıldız kümesi","contextual_glosses":[{"applicability":"Geleneksel adı kullanmadan yıldızların yuvarlak dizilişini açıklamak gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli gök cisimleri topluluğunun yuvarlak görünümü korunur."},"facet_ids":["F001"],"text":"yuvarlak yıldız kümesi","usage_role":"explanatory"},{"applicability":"Yuvarlak yıldız topluluğunun kanıtlanan geleneksel adının gerektiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yıldız kümesine verilen tas benzetmeli geleneksel ad korunur."},"facet_ids":["F002"],"text":"Yoksulların Tası","usage_role":"contextual"}],"definition":"Gökyüzünde yuvarlak bir düzen oluşturan ve geleneksel olarak Yoksulların Tası diye adlandırılan belirli yıldız kümesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gökyüzünde yuvarlak biçimde dizilmiş belirli bir yıldız topluluğunu adlandırır."},{"facet_id":"F002","role":"associated_use","statement":"Yıldız topluluğunun yuvarlak görünümü tas benzetmesine dayanan geleneksel bir adla da belirtilir."}],"identity_rationale":"Kaynak ifadesi gökyüzünde yuvarlak bir düzen oluşturan belirli yıldız topluluğunu ve bu topluluğun geleneksel tas benzetmeli adını tutarlı biçimde doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"Yoksulların Tası denen yuvarlak yıldız kümesi"}],"lexicalization_note":"Tanım yalın yıldız kümesi adını verir ve komşu yıldız topluluklarının ya da genel dairesellik anlamının kapsamını içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen dört karşıtlık bu özel kümeyi genel dairesellikten, başka yıldız topluluklarından ve çevreleyen halkalardan ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal adı olan belirli bir yıldız topluluğudur; komşu dal nesne türünden bağımsız genel dönme, kıvrılma ve dairesel diziliş biçimidir.","focus_only":"Yuvarlak dizilmiş tek ve geleneksel olarak adlandırılmış bir yıldız kümesine özgüdür.","gloss":"belirli yıldız kümesi ve genel dairesel diziliş","neighbor_only":"Yılanın kıvrımı dahil her tür nesnenin dairesel biçim almasını ve yıldızların genel yuvarlak dizilişini kapsar.","neighbor_ref":"root_000374/B002","relation_type":"near_neighbor","shared_zone":"İki dal da yıldızların yuvarlak veya dairesel bir sıra oluşturmasını bildirebilir."},{"boundary_match":"field_only","distinction":"Odak dalın ayırıcı özelliği yıldızların yuvarlak dizilişi ve küme kimliğidir; komşu dal yalnız başka bir ad taşıyan küçük yıldızlardır.","focus_only":"Yuvarlak düzeni ve tas benzetmeli adıyla belirlenmiş bir yıldız topluluğudur.","gloss":"yuvarlak yıldız kümesi ve küçük yıldızlar","neighbor_only":"Başka bir ad altında anılan küçük yıldızları belirtir ve yuvarlak düzen gerektirmez.","neighbor_ref":"root_000965/B009","relation_type":"same_field","shared_zone":"İki dal da özel adla anılan birden çok yıldızı konu edinir."},{"boundary_match":"field_only","distinction":"Odak dal yuvarlak biçimli tas benzetmeli kümedir; komşu dal farklı gök bölgeleriyle ilişkilendirilen başka yıldız topluluklarıdır.","focus_only":"Yuvarlak dizilişi ve tas benzetmeli adı olan belirli yıldız kümesidir.","gloss":"iki ayrı adlandırılmış yıldız kümesi","neighbor_only":"Taht adıyla anılan başka yıldız topluluklarını belirtir.","neighbor_ref":"root_001000/B008","relation_type":"same_field","shared_zone":"Her iki dal gökyüzünde özel bir topluluk adıyla bilinen yıldızları adlandırır."},{"boundary_match":"partial","distinction":"Odak dal yuvarlak dizilmiş yıldızların kendisidir; komşu dal bir şeyi çevreleyen daire veya daireye benzeyen izdir.","focus_only":"Daireyi yıldızların birlikte oluşturduğu belirli bir küme olarak adlandırır.","gloss":"yuvarlak yıldız kümesi ve çevreleyen daire","neighbor_only":"Ay çevresindeki halka, hayvan üzerindeki yuvarlak damga ve göz çukuru gibi genel daireleri kapsar.","neighbor_ref":"root_000296/B006","relation_type":"near_neighbor","shared_zone":"İki dal görsel olarak yuvarlak ya da dairesel bir şekil taşır."}],"source_phrase_ar":"الفكة النجوم المستديرة التي إلى جانب بنات نعش وهي قصعة المساكين (ayn)؛ الفكة كواكب مستديرة خلف السماك الرامح (sihah)؛ الفكة النجوم المستديرة التي يسميها الصبيان قصعة المساكين (tahdhib)","source_summary":"Kaynaklar yuvarlak dizili belirli yıldız kümesinde ve bu kümenin tas benzetmeli geleneksel adında birleşir; gökteki konum anlatımları birbirini tamamlayan tariflerdir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه الفَكّة، وهي كواكب أو نجوم مستديرة تسمى قصعة المساكين","what_is_not_ar":"ليس الفكّين ولا فَكَّة الحمق ولا فكاك الرهن"},"support_links":[]},{"boundary":"Dal çocuk, ağız ve ilaç katılımcılarını birlikte gerektirir; genel tedavi, ağız ovma veya ağza herhangi bir şey koyma değildir.","branch_kind":"collocation","branch_ref":"root_001173/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"فَكّ","morph_features":"STEM|POS:N|LEM:fak~|ROOT:fkk|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:1:1","qac_word_ref":"90:13:1","surface_ar":"فَكُّ"}],"gloss":"çocuğun ağzına ilaç koyma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İlacın tedavi amacıyla bir çocuğun ağzına doğrudan konmasını bildirir."}}],"root_ar":"ف ك ك","root_id":"root_001173","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çocuk, ağız ve ilaç katılımcılarını koruyan, yalnız bu özel yapıya uygun kısa açıklamadır.","boundary_detail":"Dal çocuk, ağız ve ilaç katılımcılarını birlikte gerektirir; genel tedavi, ağız ovma veya ağza herhangi bir şey koyma değildir.","branch_image_ar":"جعل الدواء في فم الصبي","concept_gloss":"çocuğun ağzına ilaç koyma","contextual_glosses":[{"applicability":"İlacın doğrudan çocuğun ağzına konduğu tedavi bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çocuğa ilacın ağız yoluyla ve doğrudan verilmesi korunur."},"facet_ids":["F001"],"text":"çocuğa ağızdan ilaç vermek","usage_role":"contextual"}],"definition":"Tedavi amacıyla ilacı doğrudan bir çocuğun ağzının içine koyma eylemidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İlacın tedavi amacıyla bir çocuğun ağzına doğrudan konmasını bildirir."}],"identity_rationale":"Kaynak ifadesi yalnızca çocuğun ağzına ilaç koyma eylemini bildirir ve geçici dal çerçevesi bu dar, katılımcıları belirli kullanımı eksiksiz yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"çocuğun ağzına ilaç koymak"}],"lexicalization_note":"Tanım yalnız çocukla kurulan ve ilacın ağza konmasını bildiren yapıya bağlıdır; bundan genel bir verme veya tedavi anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen üç karşıtlık işlemi damak ovma, boğaz müdahalesi ve genel yara tedavisinden ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ilacı ağza koyma işlemidir; komşu dal damağı hurma ya da parmakla ovma işlemidir ve hayvana uygulanan biçimi de vardır.","focus_only":"Tedavi maddesinin ilaç olması ve doğrudan çocuğun ağzına konması gerekir.","gloss":"ağza ilaç koyma ve damak ovma","neighbor_only":"Çocuğun damağını hurma veya parmakla ovmayı ve hayvan damağına çubuk uygulamayı da kapsar.","neighbor_ref":"root_000363/B002","relation_type":"near_neighbor","shared_zone":"İki dal da çocuğun ağız içine tedavi veya bakım amacıyla müdahaleyi içerir."},{"boundary_match":"partial","distinction":"Odak dal ilaç maddesini ağza yerleştirir; komşu dal boğaz dokusuna parmakla müdahale eder ve ayrıca kan çekme uygulamasını kapsar.","focus_only":"İlacın çocuğun ağzına konmasına özgüdür ve başka tedavi tekniği içermez.","gloss":"ağızdan ilaç verme ve boğaz müdahalesi","neighbor_only":"Çocuğun boğazındaki dokuyu parmakla bastırıp kaldırmayı ve kan emici canlı uygulamasını kapsar.","neighbor_ref":"root_001039/B012","relation_type":"near_neighbor","shared_zone":"İki dal çocukta ağız ve boğaz çevresine yönelik geleneksel tedavi işlemleridir."},{"boundary_match":"field_only","distinction":"Odak dal belirli katılımcıları ve uygulama yerini gerektiren dar bir işlemdir; komşu dal yaranın ilaçla veya dikişle genel tedavisidir.","focus_only":"Yalnız bir çocuğun ağzına ilaç koyma işlemini bildirir.","gloss":"özel ağızdan ilaç verme ve genel yara tedavisi","neighbor_only":"Yara bakımı, dikiş ve tedaviyi yapan kişi dahil genel yara tedavisi alanını kapsar.","neighbor_ref":"root_000034/B001","relation_type":"same_field","shared_zone":"Her iki dal hastalığı veya bedensel sorunu ilaç ve bakım yoluyla giderme alanındadır."}],"source_phrase_ar":"فككت الصبي جعلت الدواء في فيه","source_qualifications":[{"kind":"sole_attestation","summary":"Kayıt, tedavi için ilacı bir çocuğun ağzına koymayı bu özel söz yapısının tek anlamı olarak tanıklar."}],"source_summary":"Bu dar kullanım tek bir kaynak kaydına dayanır; çocuk, ilaç ve ağız katılımcılarının tümü tekil tanıklığın zorunlu parçalarıdır.","sources":["SI"],"what_is_ar":"يدخل فيه قولهم فككت الصبي إذا جعلت الدواء في فيه","what_is_not_ar":"ليس عتقا ولا فصل مشتَبكين ولا اسم الفكّين"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["90:13:1"],"branch_refs":[],"candidate_id":"cand_2cb4ce6c2fc7c0b828af","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001173"],"scope":"focus_ayah","source_local_id":"90:13:1:boundary-answer-delivery","source_type":"word_analysis","support_ids":["sup_526a3e7852e483552837","sup_eee91f326aa12ad7e601"],"title":"boundary turns question into answer","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:13:1","qac_refs":["90:13:1:1"],"status":"accepted"}},{"anchor_refs":["90:13:1"],"branch_refs":[],"candidate_id":"cand_a3b8f24208a5ac65233c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001173"],"scope":"focus_ayah","source_local_id":"90:13:1:compressed-sound-answer","source_type":"word_analysis","support_ids":["sup_575d29ded483141ee298","sup_eee91f326aa12ad7e601"],"title":"clipped sound makes release stark","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:13:1","qac_refs":["90:13:1:1"],"status":"accepted"}},{"anchor_refs":["90:13:1"],"branch_refs":[],"candidate_id":"cand_9c76c901083f1c12870e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001173"],"scope":"focus_ayah","source_local_id":"90:13:1:construct-binds-patient","source_type":"word_analysis","support_ids":["sup_c1996b503cb72fefc02b","sup_eee91f326aa12ad7e601"],"title":"construct form fastens action to patient","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:13:1","qac_refs":["90:13:1:1"],"status":"accepted"}},{"anchor_refs":["90:13:1"],"branch_refs":[],"candidate_id":"cand_65d22a9896387ee79430","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001173"],"scope":"focus_ayah","source_local_id":"90:13:1:finite-variant-contrast","source_type":"word_analysis","support_ids":["sup_61793f5724d7f90c00cb","sup_eee91f326aa12ad7e601"],"title":"variant clarifies deed versus definition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:13:1","qac_refs":["90:13:1:1"],"status":"accepted"}},{"anchor_refs":["90:13:1"],"branch_refs":[],"candidate_id":"cand_74f64a784a3270e861f2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001173"],"scope":"focus_ayah","source_local_id":"90:13:1:nominal-predicate-answer","source_type":"word_analysis","support_ids":["sup_53a8eaa2f42dd43458d9","sup_eee91f326aa12ad7e601"],"title":"nominal predicate defines the pass","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:13:1","qac_refs":["90:13:1:1"],"status":"accepted"}},{"anchor_refs":["90:13:1"],"branch_refs":[],"candidate_id":"cand_8d29d8318acd74eb8186","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001173"],"scope":"focus_ayah","source_local_id":"90:13:1:ransom-extrication-pressure","source_type":"word_analysis","support_ids":["sup_96d3d6601d31dcd455aa","sup_eee91f326aa12ad7e601"],"title":"ransom family gives costly release pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:13:1","qac_refs":["90:13:1:1"],"status":"accepted"}},{"anchor_refs":["90:13:1"],"branch_refs":[],"candidate_id":"cand_e8865c53aacee8ba9dc0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001173"],"scope":"focus_ayah","source_local_id":"90:13:1:rare-root-and-98-1-contrast","source_type":"word_analysis","support_ids":["sup_bc3d36483afecec70383","sup_eee91f326aa12ad7e601"],"title":"rare disengagement root becomes freeing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:13:1","qac_refs":["90:13:1:1"],"status":"accepted"}},{"anchor_refs":["90:13:1"],"branch_refs":[],"candidate_id":"cand_65a2d88600f0e4378a32","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001173"],"scope":"focus_ayah","source_local_id":"90:13:1:unfastening-over-charity","source_type":"word_analysis","support_ids":["sup_bf55aa259833c977b846","sup_eee91f326aa12ad7e601"],"title":"virtue is undoing constraint","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:13:1","qac_refs":["90:13:1:1"],"status":"accepted"}},{"anchor_refs":["90:13:1"],"branch_refs":[],"candidate_id":"cand_a695995ef6bd0174f3b8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001173"],"scope":"focus_ayah","source_local_id":"90:13:1:unnamed-liberating-agent","source_type":"word_analysis","support_ids":["sup_2ece27f0b544ffa0e4ed","sup_eee91f326aa12ad7e601"],"title":"act foregrounded before the freer","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:13:1","qac_refs":["90:13:1:1"],"status":"accepted"}},{"anchor_refs":["90:13:2"],"branch_refs":[],"candidate_id":"cand_e528d8ca6b28da37ff1b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000584"],"scope":"focus_ayah","source_local_id":"90:13:2:anonymous-singular-neck","source_type":"word_analysis","support_ids":["sup_3bea51a365d6dfcda848","sup_a0997659ae53a7caa51c"],"title":"one unnamed neck generalizes duty","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:13:2","qac_refs":["90:13:2:1"],"status":"accepted"}},{"anchor_refs":["90:13:2"],"branch_refs":[],"candidate_id":"cand_9068e30c286375e705db","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000584"],"scope":"focus_ayah","source_local_id":"90:13:2:control-point-specificity","source_type":"word_analysis","support_ids":["sup_3bea51a365d6dfcda848","sup_5f621bf1b5fb53e5fcbc"],"title":"release touches the control point","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:13:2","qac_refs":["90:13:2:1"],"status":"accepted"}},{"anchor_refs":["90:13:2"],"branch_refs":[],"candidate_id":"cand_b2ae793371140fa5553b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000584"],"scope":"focus_ayah","source_local_id":"90:13:2:emancipation-context-stripped","source_type":"word_analysis","support_ids":["sup_3bea51a365d6dfcda848","sup_f165daa55123a466a6bc"],"title":"legal field becomes immediate definition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:13:2","qac_refs":["90:13:2:1"],"status":"accepted"}},{"anchor_refs":["90:13:2"],"branch_refs":[],"candidate_id":"cand_a7723c7195dc3b9a0789","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000584"],"scope":"focus_ayah","source_local_id":"90:13:2:embodied-neck-metonymy","source_type":"word_analysis","support_ids":["sup_3bea51a365d6dfcda848","sup_a09b554b05cd241c2334"],"title":"neck names the bound person","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:13:2","qac_refs":["90:13:2:1"],"status":"accepted"}},{"anchor_refs":["90:13:2"],"branch_refs":[],"candidate_id":"cand_2080c009a6002b88fdab","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000584"],"scope":"focus_ayah","source_local_id":"90:13:2:final-patient-weight","source_type":"word_analysis","support_ids":["sup_0f54f98b50949e1e0f4b","sup_3bea51a365d6dfcda848"],"title":"answer ends with the vulnerable human","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:13:2","qac_refs":["90:13:2:1"],"status":"accepted"}},{"anchor_refs":["90:13:2"],"branch_refs":[],"candidate_id":"cand_93a060616ab1c3cc594c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000584"],"scope":"focus_ayah","source_local_id":"90:13:2:genitive-patient-role","source_type":"word_analysis","support_ids":["sup_3bea51a365d6dfcda848","sup_87d4d404a351cd0840f9"],"title":"genitive noun bears patient force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:13:2","qac_refs":["90:13:2:1"],"status":"accepted"}},{"anchor_refs":["90:13:2"],"branch_refs":[],"candidate_id":"cand_4456876cab837a2b700b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000584"],"scope":"focus_ayah","source_local_id":"90:13:2:phrase-cadence-fusion","source_type":"word_analysis","support_ids":["sup_3bea51a365d6dfcda848","sup_c62acf8acd66ab6cdd11"],"title":"recitation fuses action and object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:13:2","qac_refs":["90:13:2:1"],"status":"accepted"}},{"anchor_refs":["90:13:2"],"branch_refs":[],"candidate_id":"cand_ef222a9d471c002fe27f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000584"],"scope":"focus_ayah","source_local_id":"90:13:2:sound-handoff-from-pass","source_type":"word_analysis","support_ids":["sup_3627f178e95febde38d8","sup_3bea51a365d6dfcda848"],"title":"near-sound converts pass to neck","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:13:2","qac_refs":["90:13:2:1"],"status":"accepted"}},{"anchor_refs":["90:13:2"],"branch_refs":[],"candidate_id":"cand_bc4b300bd62abbd93238","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000584"],"scope":"focus_ayah","source_local_id":"90:13:2:watcher-field-reversed","source_type":"word_analysis","support_ids":["sup_3bea51a365d6dfcda848","sup_929ba288b0f825f6f8d6"],"title":"watching field turns toward vulnerability","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:13:2","qac_refs":["90:13:2:1"],"status":"accepted"}},{"anchor_refs":["90:13:1"],"branch_refs":[],"candidate_id":"cand_fdc0299281548f95ea23","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001173"],"scope":"focus_ayah","source_local_id":"90:13:1:1","source_type":"qac_morpheme","support_ids":["sup_ea06529348995a7308c1"],"title":"QAC root occurrence: ف ك ك","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["90:13:2"],"branch_refs":[],"candidate_id":"cand_6b57c229e2dc46677ab8","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000584"],"scope":"focus_ayah","source_local_id":"90:13:2:1","source_type":"qac_morpheme","support_ids":["sup_e3177a8a75ebe13f945f"],"title":"QAC root occurrence: ر ق ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["90:13"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:13","branch_refs":["root_000584/B004","root_001173/B002"],"candidate_id":"cand_d0a75656dc7218d3891b","commentary_obligation":"review","hft_ref":"hft_5f6c3107fb8363f7cf0f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_release_bound_person","source_type":"hft","support_ids":["sup_93392234eeda524a562c"],"title":"baseline_release_bound_person","trust":"legacy_unbound"},{"anchor_refs":["90:13"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:13","branch_refs":["root_000584/B001","root_000584/B002","root_001173/B001"],"candidate_id":"cand_db8c2f3de428fbe0d723","commentary_obligation":"review","hft_ref":"hft_270bbe62e691f1b5550a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_dismantle_custody","source_type":"hft","support_ids":["sup_ff6b296e47bc6cef9f81"],"title":"baseline_dismantle_custody","trust":"legacy_unbound"},{"anchor_refs":["90:13"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:13","branch_refs":["root_000584/B004","root_000584/B012","root_001173/B002"],"candidate_id":"cand_0b94d2c52cf84cc13eac","commentary_obligation":"review","hft_ref":"hft_09078c9b29c729872b1a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_extinguish_human_collateral","source_type":"hft","support_ids":["sup_b04130cf9f2d4b2b5fd5"],"title":"baseline_extinguish_human_collateral","trust":"legacy_unbound"},{"anchor_refs":["90:13"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:13","branch_refs":["root_000584/B004","root_001173/B001","root_001173/B004"],"candidate_id":"cand_47bc2041da7a9ecc37e4","commentary_obligation":"review","hft_ref":"hft_6640dae92e03cdba908b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_restore_articulation","source_type":"hft","support_ids":["sup_49d022c5d355ee805a34"],"title":"baseline_restore_articulation","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فَكُّ رَقَبَةٍ","qac_morphemes":[{"lemma_ar":"فَكّ","morph_features":"STEM|POS:N|LEM:fak~|ROOT:fkk|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:1:1","qac_word_ref":"90:13:1","root_ar":"ف ك ك","surface_ar":"فَكُّ"},{"lemma_ar":"رَقَبَة","morph_features":"STEM|POS:N|LEM:raqabap|ROOT:rqb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:2:1","qac_word_ref":"90:13:2","root_ar":"ر ق ب","surface_ar":"رَقَبَةٍ"}],"word_analysis_qac_refs":[["90:13:1:1"],["90:13:2:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["90:13:1","90:13:2"]},"focus_surface_evidence":{"arabic_uthmani":"فَكُّ رَقَبَةٍ","qac_morphemes":[{"lemma_ar":"فَكّ","morph_features":"STEM|POS:N|LEM:fak~|ROOT:fkk|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:1:1","qac_word_ref":"90:13:1","root_ar":"ف ك ك","surface_ar":"فَكُّ"},{"lemma_ar":"رَقَبَة","morph_features":"STEM|POS:N|LEM:raqabap|ROOT:rqb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:13:2:1","qac_word_ref":"90:13:2","root_ar":"ر ق ب","surface_ar":"رَقَبَةٍ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["90:13:1:1"],["90:13:2:1"]],"word_analysis_refs":["90:13:1","90:13:2"],"word_rows":[{"analysis_record_ref":"90:13:1","analytic_gloss_range_en":"a bound verbal noun of unfastening and release, locally defining the steep path as freeing a constrained human rather than as generic charity or detached legal payment","analytic_root_gloss_range_en":"broad root range of opening, separating, releasing, disengaging, ransom-like extrication, jaw or joint looseness, and other specialized branches; the local construction selects release from constraint while unrelated body, animal, star, and slackness branches remain outside the local sense","qac_refs":["90:13:1:1"],"root":{"arabic":"ف ك ك","transliteration":"f-k-k"},"surface":{"arabic":"فَكُّ","transliteration":"fakku"}},{"analysis_record_ref":"90:13:2","analytic_gloss_range_en":"an indefinite singular concrete neck functioning as metonymy for an unspecified bound human, formally genitive yet semantically the patient and beneficiary of release","analytic_root_gloss_range_en":"broad root range of neck, person in bondage, watching, guarding, waiting, lookout, and several specialized branches; the local noun selects the neck/person-in-bondage branch while watch-and-custody associations survive only as narrowed background pressure","qac_refs":["90:13:2:1"],"root":{"arabic":"ر ق ب","transliteration":"r-q-b"},"surface":{"arabic":"رَقَبَةٍ","transliteration":"raqabatin"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":2,"words_total":2,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["90:13"],"branch_refs":["root_000584/B004","root_001173/B002"],"candidate_id":"cand_d0a75656dc7218d3891b","evidence_scope":"focus_ayah","hft_ref":"hft_5f6c3107fb8363f7cf0f","item_id":"baseline_release_bound_person","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_release_bound_person","support_id":"sup_93392234eeda524a562c"},{"anchor_refs":["90:13"],"branch_refs":["root_000584/B001","root_000584/B002","root_001173/B001"],"candidate_id":"cand_db8c2f3de428fbe0d723","evidence_scope":"focus_ayah","hft_ref":"hft_270bbe62e691f1b5550a","item_id":"baseline_dismantle_custody","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_dismantle_custody","support_id":"sup_ff6b296e47bc6cef9f81"},{"anchor_refs":["90:13"],"branch_refs":["root_000584/B004","root_000584/B012","root_001173/B002"],"candidate_id":"cand_0b94d2c52cf84cc13eac","evidence_scope":"focus_ayah","hft_ref":"hft_09078c9b29c729872b1a","item_id":"baseline_extinguish_human_collateral","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_extinguish_human_collateral","support_id":"sup_b04130cf9f2d4b2b5fd5"},{"anchor_refs":["90:13"],"branch_refs":["root_000584/B004","root_001173/B001","root_001173/B004"],"candidate_id":"cand_47bc2041da7a9ecc37e4","evidence_scope":"focus_ayah","hft_ref":"hft_6640dae92e03cdba908b","item_id":"baseline_restore_articulation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_restore_articulation","support_id":"sup_49d022c5d355ee805a34"}],"diagnostics":[],"lane_counts":{"global":16,"macro":5,"micro":4},"packet_summary":{"ayah_count":20,"focus_ref":"90:13","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ح ل ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000351","furuq_root_norm":"ح ل ل","furuq_source_root_norm":"ح ل ل","is_dominant":true,"target_occurrences":39,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000353","furuq_root_norm":"ح ل ي","furuq_source_root_norm":"ح ل ي","is_dominant":false,"target_occurrences":6,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"و ص د","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000036","furuq_root_norm":"ء ص د","furuq_source_root_norm":"أ ص د","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001653","furuq_root_norm":"و ص د","furuq_source_root_norm":"و ص د","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["90:1","90:2","90:3","90:4","90:5","90:6","90:7","90:8","90:9","90:10","90:11","90:12","90:13","90:14","90:15","90:16","90:17","90:18","90:19","90:20"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"90:13","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":11,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"90:13","lane":"micro","linguistic_source_ref":"90:13","surface_ref":"90:13","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"90:13","target_tokens":[["Bir",["90:13:2"]],["köleyi",["90:13:2"]],["özgür",["90:13:1"]],["bırakmaktır",["90:13:1"]]],"text":"Bir köleyi özgür bırakmaktır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":11,"ayah_to":20,"id":"s090-p02-011-020","label":"The steep path and the two companies","number":2,"refs":["90:11","90:12","90:13","90:14","90:15","90:16","90:17","90:18","90:19","90:20"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:13:2:final-patient-weight","source_type":"word_analysis","support_id":"sup_0f54f98b50949e1e0f4b","text":"{\"blocking_evidence\":null,\"headline\":\"answer ends with the vulnerable human\",\"reader_payoff\":\"The reader notices the answer moving from the act to the human affected by it, leaving the vulnerable person with the final weight.\",\"reason\":\"The local two-word nominal phrase places the verbal noun first and closes the ayah on its governed patient.\",\"representative_source_ids\":[\"QT-994cc7fb\",\"QT-d22cb80e\",\"QB-7adcd687\",\"QB-f17b1351\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:13:1:unnamed-liberating-agent","source_type":"word_analysis","support_id":"sup_2ece27f0b544ffa0e4ed","text":"{\"blocking_evidence\":null,\"headline\":\"act foregrounded before the freer\",\"reader_payoff\":\"The reader notices that freeing implies a human agent, but the wording keeps prestige away from the freer and centers the release.\",\"reason\":\"The verbal noun carries action semantics without an overt subject, so the implied liberator remains grammatically backgrounded.\",\"representative_source_ids\":[\"QG-5cb2053c\",\"MG-3718743c\",\"QS-87b94398\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:13:2:sound-handoff-from-pass","source_type":"word_analysis","support_id":"sup_3627f178e95febde38d8","text":"{\"blocking_evidence\":null,\"headline\":\"near-sound converts pass to neck\",\"reader_payoff\":\"The reader hears the question's pass-language give way to a near-sounding neck-word, making the obstacle feel transformed into embodied captivity.\",\"reason\":\"The CRITICAL sound rows make a concrete question-answer boundary claim, and attachment support keeps the prior question active as the reading window.\",\"representative_source_ids\":[\"QE-1f4eaf0f\",\"QE-7824b8a2\",\"QB-58141191\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:13:2","source_type":"word_analysis","support_id":"sup_3bea51a365d6dfcda848","text":"{\"gloss_range\":\"an indefinite singular concrete neck functioning as metonymy for an unspecified bound human, formally genitive yet semantically the patient and beneficiary of release\",\"prose\":\"{{ar:رَقَبَةٍ}} ({{tr:raqabatin}}) is genitive in form but patient in function: it is the human affected by the release, and the accusative variant makes the same patient role more overt without replacing the local construct route. The tanwīn and singular form matter because the phrase does not name a prestigious recipient or a broad plural category; it places one anonymous neck before the listener and lets that anonymity generalize the duty. The body-part image remains active even when the intended referent is a bound person, so captivity is felt at the exposed control point before it becomes a legal formula. The wider root can name watching and guarding, yet this concrete noun reverses that field into the watched body under domination; the divine-watcher contrast (5:117) therefore remains a controlled contrast, not the local sense. Legal and righteousness settings (4:92; 2:177) show the familiar emancipation field, but this ayah strips it to a two-word definition and closes on the vulnerable person. The near-sound handoff from the pass-question in 90:12 to the neck-word turns the obstacle into embodied captivity, and the phrase cadence keeps action and patient fused as one compact formula rather than a loose description.\",\"root_display\":\"{{ar:ر ق ب}} ({{tr:r-q-b}})\",\"root_gloss_range\":\"broad root range of neck, person in bondage, watching, guarding, waiting, lookout, and several specialized branches; the local noun selects the neck/person-in-bondage branch while watch-and-custody associations survive only as narrowed background pressure\",\"surface_display\":\"{{ar:رَقَبَةٍ}} ({{tr:raqabatin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:13:1:boundary-answer-delivery","source_type":"word_analysis","support_id":"sup_526a3e7852e483552837","text":"{\"blocking_evidence\":null,\"headline\":\"boundary turns question into answer\",\"reader_payoff\":\"The reader keeps the previous question active, so this word is heard as answer delivery rather than as a new independent topic.\",\"reason\":\"Attachment translation support warns that the nominal phrase begins the answer list to the preceding question, preserving the cross-ayah predicate relation.\",\"representative_source_ids\":[\"QT-5c245e25\",\"QT-d96ebca5\",\"QB-1e1b0b69\",\"QB-ead7ee92\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:13:1:nominal-predicate-answer","source_type":"word_analysis","support_id":"sup_53a8eaa2f42dd43458d9","text":"{\"blocking_evidence\":null,\"headline\":\"nominal predicate defines the pass\",\"reader_payoff\":\"The reader notices that the steep path is identified with release as a defining action-kind before the wording reports any actor or event.\",\"reason\":\"QAC and attachment evidence mark a gerund or verbal noun with nominative predicate force in a nominal answer phrase, so the CRITICAL definition claim is locally licensed.\",\"representative_source_ids\":[\"QG-0a788021\",\"QG-ef32ad2b\",\"QT-83e16452\",\"QY-26a41393\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:13:1:compressed-sound-answer","source_type":"word_analysis","support_id":"sup_575d29ded483141ee298","text":"{\"blocking_evidence\":null,\"headline\":\"clipped sound makes release stark\",\"reader_payoff\":\"The reader hears the first answer as brief and forceful, with the doubled stop and two-word compression reinforcing the tight release-action.\",\"reason\":\"The sound rows cohere with the compact two-word construct, but they support rather than prove the lexical sense.\",\"representative_source_ids\":[\"QP-7c2dd350\",\"QP-91c5e254\",\"QE-c1b4a414\",\"MP-b5c35d2d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:13:2:control-point-specificity","source_type":"word_analysis","support_id":"sup_5f621bf1b5fb53e5fcbc","text":"{\"blocking_evidence\":null,\"headline\":\"release touches the control point\",\"reader_payoff\":\"The reader notices that captivity is localized at the vulnerable neck or throat-region, so release touches the bodily site of control.\",\"reason\":\"The neck gloss and bondage metonymy support a concrete control-point image without requiring a separate literal-only reading.\",\"representative_source_ids\":[\"QS-7a410888\",\"QS-fd285aa8\",\"MS-225da401\",\"MT-770d1e0e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:13:1:finite-variant-contrast","source_type":"word_analysis","support_id":"sup_61793f5724d7f90c00cb","text":"{\"blocking_evidence\":null,\"headline\":\"variant clarifies deed versus definition\",\"reader_payoff\":\"The reader sees that the accepted finite-verb reading would make the same content a completed proof, while the local surface keeps it as the nominal definition.\",\"reason\":\"The variant is valid contrastive evidence for form and case, but it does not replace the canonical verbal-noun surface or its construct grammar.\",\"representative_source_ids\":[\"QG-709a70d5\",\"QF-edba1396\",\"MF-e86beb88\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:13:2:genitive-patient-role","source_type":"word_analysis","support_id":"sup_87d4d404a351cd0840f9","text":"{\"blocking_evidence\":null,\"headline\":\"genitive noun bears patient force\",\"reader_payoff\":\"The reader notices that the noun is formally genitive but semantically the affected human released by the act, with the accusative variant clarifying rather than replacing that role.\",\"reason\":\"Attachment evidence forces the genitive construct relation, and the variant case rows are valid contrast for patienthood but do not govern the canonical surface.\",\"representative_source_ids\":[\"QG-a8a93750\",\"QG-de31626b\",\"QS-806b639c\",\"MF-6b0c6b7b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:13:2:watcher-field-reversed","source_type":"word_analysis","support_id":"sup_929ba288b0f825f6f8d6","text":"{\"blocking_evidence\":null,\"headline\":\"watching field turns toward vulnerability\",\"reader_payoff\":\"The reader notices that a root field able to name watching and guarding is locally bent toward the body watched, held, and controlled.\",\"reason\":\"The broader root has watcher and guard branches, including the 5:117 contrast, but the local concrete noun selects the vulnerable body rather than the observing agent.\",\"representative_source_ids\":[\"QS-772e8b31\",\"QS-e989a428\",\"QF-4d9c05e6\",\"MI-debe4e7c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:13:1:ransom-extrication-pressure","source_type":"word_analysis","support_id":"sup_96d3d6601d31dcd455aa","text":"{\"blocking_evidence\":null,\"headline\":\"ransom family gives costly release pressure\",\"reader_payoff\":\"The reader feels the freeing as extrication from captivity, while local form keeps the named act as unfastening rather than seeking, motive, or payment.\",\"reason\":\"The dictionary family includes pledge-release, ransom, rescue, and disengagement evidence, but the surface is the simpler verbal noun rather than a derived seeking or ransom form.\",\"representative_source_ids\":[\"QS-b5f30ffc\",\"QS-e1fc97e3\",\"QF-563d20a2\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:13:2:anonymous-singular-neck","source_type":"word_analysis","support_id":"sup_a0997659ae53a7caa51c","text":"{\"blocking_evidence\":null,\"headline\":\"one unnamed neck generalizes duty\",\"reader_payoff\":\"The reader sees obligation widened through one unnamed concrete neck rather than through a named beneficiary or an abstract plural label.\",\"reason\":\"QAC marks an indefinite feminine singular genitive concrete noun, and the contextual referent profile supports human-generic deployment.\",\"representative_source_ids\":[\"QG-ed4e186e\",\"MG-b493c26d\",\"QF-d5620a32\",\"QF-e0bf1841\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:13:2:embodied-neck-metonymy","source_type":"word_analysis","support_id":"sup_a09b554b05cd241c2334","text":"{\"blocking_evidence\":null,\"headline\":\"neck names the bound person\",\"reader_payoff\":\"The reader feels bondage through an exposed body part before treating the person as only a legal or economic category.\",\"reason\":\"V4 includes the neck and person-in-bondage branch, and the release construction selects that metonymic sense while preserving the concrete body image.\",\"representative_source_ids\":[\"QS-1def7984\",\"QS-3f33e2ed\",\"QS-c1bf4227\",\"QS-d1b4bc89\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:13:1:rare-root-and-98-1-contrast","source_type":"word_analysis","support_id":"sup_bc3d36483afecec70383","text":"{\"blocking_evidence\":null,\"headline\":\"rare disengagement root becomes freeing\",\"reader_payoff\":\"The reader notices a rare root placed first in the answer and turned from non-disengagement contrast (98:1) into active liberation of a bound person.\",\"reason\":\"The contextual profile marks the local gerund as low occurrence, and the supplied 98:1 row provides a concrete contrast without controlling the local parse.\",\"representative_source_ids\":[\"QI-c7bc1a41\",\"QI-f20b37a1\",\"MI-82bfc167\",\"QH-69bc16d7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:13:1:unfastening-over-charity","source_type":"word_analysis","support_id":"sup_bf55aa259833c977b846","text":"{\"blocking_evidence\":null,\"headline\":\"virtue is undoing constraint\",\"reader_payoff\":\"The reader notices that the first ascent is measured by loosening a real bond, not by charity stated as generic benevolence.\",\"reason\":\"V4 supports opening, unfastening, and freeing branches, and the local object selects bondage-release rather than a general giving sense.\",\"representative_source_ids\":[\"QS-16014b09\",\"QS-3d100125\",\"QS-ce426fbe\",\"MS-26930b40\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:13:1:construct-binds-patient","source_type":"word_analysis","support_id":"sup_c1996b503cb72fefc02b","text":"{\"blocking_evidence\":null,\"headline\":\"construct form fastens action to patient\",\"reader_payoff\":\"The reader sees that the release cannot float as a slogan; its construct form is completed by the constrained person it affects.\",\"reason\":\"Attachment evidence makes the following genitive noun a syntactically forced complement of the construct verbal noun, preserving the action-patient bond.\",\"representative_source_ids\":[\"QG-7b38f8fe\",\"QF-39445034\",\"QE-3ca35fb5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:13:2:phrase-cadence-fusion","source_type":"word_analysis","support_id":"sup_c62acf8acd66ab6cdd11","text":"{\"blocking_evidence\":null,\"headline\":\"recitation fuses action and object\",\"reader_payoff\":\"The reader hears the action and patient as one compact formula rather than as a loose descriptive phrase.\",\"reason\":\"The cadence rows align with the syntactically forced construct relation, while remaining secondary to grammar and lexical meaning.\",\"representative_source_ids\":[\"QP-1a8b4740\",\"QP-9c771e81\",\"QP-efb8beba\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"90:13:2:1","source_type":"qac_morpheme","support_id":"sup_e3177a8a75ebe13f945f","text":"{\"lemma_ar\":\"رَقَبَة\",\"morph_features\":\"STEM|POS:N|LEM:raqabap|ROOT:rqb|F|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"90:13:2:1\",\"qac_word_ref\":\"90:13:2\",\"root_ar\":\"ر ق ب\",\"surface_ar\":\"رَقَبَةٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"90:13:1:1","source_type":"qac_morpheme","support_id":"sup_ea06529348995a7308c1","text":"{\"lemma_ar\":\"فَكّ\",\"morph_features\":\"STEM|POS:N|LEM:fak~|ROOT:fkk|M|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"90:13:1:1\",\"qac_word_ref\":\"90:13:1\",\"root_ar\":\"ف ك ك\",\"surface_ar\":\"فَكُّ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:13:1","source_type":"word_analysis","support_id":"sup_eee91f326aa12ad7e601","text":"{\"gloss_range\":\"a bound verbal noun of unfastening and release, locally defining the steep path as freeing a constrained human rather than as generic charity or detached legal payment\",\"prose\":\"{{ar:فَكُّ}} ({{tr:fakku}}) gives the suspended question from 90:12 a nominal answer: the pass is first defined as release itself, not narrated as someone else's performed deed. The accepted finite-verb variant helps by contrast; it would present freeing as a completed act with a recoverable actor, while this surface keeps the act as the definition and leaves the freer unnamed. The construct form also refuses to drift into an abstract virtue, because it requires the following patient and binds the act directly to the human under constraint; the compact contact between the two words joins undoing to the vulnerable site/person. Lexically, the word is not mere generosity: it pictures a fastening being undone, and the ransom-rescue family makes that release feel like costly extrication while the local Form I verbal noun still names unfastening before request, motive, or payment. Its rarity and sound tighten the first answer: after the prior question, the clipped doubled stop makes the phrase land as a compact release formula, and the contrast with non-disengagement (98:1) turns the root toward actively freeing a bound person.\",\"root_display\":\"{{ar:ف ك ك}} ({{tr:f-k-k}})\",\"root_gloss_range\":\"broad root range of opening, separating, releasing, disengaging, ransom-like extrication, jaw or joint looseness, and other specialized branches; the local construction selects release from constraint while unrelated body, animal, star, and slackness branches remain outside the local sense\",\"surface_display\":\"{{ar:فَكُّ}} ({{tr:fakku}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:13:2:emancipation-context-stripped","source_type":"word_analysis","support_id":"sup_f165daa55123a466a6bc","text":"{\"blocking_evidence\":null,\"headline\":\"legal field becomes immediate definition\",\"reader_payoff\":\"The reader sees the known emancipation field from 4:92 and 2:177 compressed into the first face of the steep path, with unfastening emphasized over formula.\",\"reason\":\"Contextual evidence supports recurring bondage and manumission settings, while the named parallels remain contrastive rather than controlling the local wording.\",\"representative_source_ids\":[\"QI-d7169c19\",\"QI-e223b5c6\",\"MI-310c26c6\",\"MI-3460c18a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَكُّ رَقَبَةٍ","ayah_ref":"90:13"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000584/B004","root_001173/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001173","role":"Freeing a pledge, captive, or neck from closure supplies the concrete release operation and its juridical force.","root":"ف ك ك","source_ref":"90:13","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_000584","role":"The anatomical neck extended to a slave, captive, or whole person supplies the embodied object of release.","root":"ر ق ب","source_ref":"90:13","source_word_indices":["2"]}],"changed_reading":{"after":"It names the concrete release of a whole embodied person from a relation of bondage.","before":"The phrase could be heard as an unspecified loosening involving a neck."},"confidence":"strong","focus_anchor":"The nominal construction فَكُّ رَقَبَةٍ joins an act of release to the neck as a metonym for a whole person.","mechanism":"The release branch explicitly overlaps pledge, captive, and neck, while the neck branch extends the body part to a person held in bondage. Their intersection names termination of an actual hold over a human being, not merely an inward feeling of relief.","model_id":"baseline_release_bound_person"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_release_bound_person","source_type":"hft","support_id":"sup_93392234eeda524a562c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَكُّ رَقَبَةٍ","ayah_ref":"90:13"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000584/B001","root_000584/B002","root_001173/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001173","role":"Opening what is locked and separating what is interlaced supplies the dismantling action.","root":"ف ك ك","source_ref":"90:13","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000584","role":"Watching and expectant waiting expose surveillance as one strand of the condition being undone.","root":"ر ق ب","source_ref":"90:13","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000584","role":"Guarding and keeping supply the retaining function that turns watchfulness into custody.","root":"ر ق ب","source_ref":"90:13","source_word_indices":["2"]}],"changed_reading":{"after":"Freedom also requires taking apart the watch-and-guard system by which a person is kept capturable.","before":"Freedom is a single change of legal status."},"confidence":"medium","focus_anchor":"فَكُّ contributes opening and separation, while the root of رَقَبَةٍ also carries watching and guarding.","mechanism":"A captive condition is maintained not only by a bond but by an interlaced apparatus of watch, guard, and retention. On this branch pairing, release dismantles the custody mechanism that continually reproduces captivity.","model_id":"baseline_dismantle_custody"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_dismantle_custody","source_type":"hft","support_id":"sup_ff6b296e47bc6cef9f81","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَكُّ رَقَبَةٍ","ayah_ref":"90:13"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000584/B004","root_000584/B012","root_001173/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001173","role":"The single release branch's overlap of pledge and captive supplies the collateral-to-person conversion.","root":"ف ك ك","source_ref":"90:13","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_000584","role":"Neck as whole bonded person keeps the economic model attached to an embodied human.","root":"ر ق ب","source_ref":"90:13","source_word_indices":["2"]},{"branch_id":"B012","mapped_root_id":"root_000584","role":"The core portion of property supplies the asset-register from which the person must be removed.","root":"ر ق ب","source_ref":"90:13","source_word_indices":["2"]}],"changed_reading":{"after":"Release cancels the very claim by which an embodied person can function as collateral or core property.","before":"Release is an expense that changes who owns a person."},"confidence":"medium","focus_anchor":"Within the two focus roots, release of a pledge overlaps release of a neck, and رَقَبَة can also mark the core portion of property.","mechanism":"The phrase exposes a conversion between body and asset: a human has been made collateral or property, and فَكّ extinguishes that proprietary claim. The result is not simply purchasing a new status but removing the person from the grammar of holdings.","model_id":"baseline_extinguish_human_collateral"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_extinguish_human_collateral","source_type":"hft","support_id":"sup_b04130cf9f2d4b2b5fd5","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَكُّ رَقَبَةٍ","ayah_ref":"90:13"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000584/B004","root_001173/B001","root_001173/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001173","role":"The two jaws and their meeting points supply the movable articulation that can be opened.","root":"ف ك ك","source_ref":"90:13","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001173","role":"Opening a lock or separating an interlace turns the anatomical contact into a release mechanism.","root":"ف ك ك","source_ref":"90:13","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_000584","role":"Neck as body part and whole captive person joins physical articulation to recovered human agency.","root":"ر ق ب","source_ref":"90:13","source_word_indices":["2"]}],"changed_reading":{"after":"It can additionally image reopening the captive body's capacity for breath, speech, orientation, and self-directed action.","before":"The phrase effects a juridical transfer out of bondage."},"confidence":"exploratory","focus_anchor":"The ف ك ك inventory includes the jaws, and رَقَبَةٍ directly names the neck before extending to the person.","mechanism":"Jaw and neck form a bodily articulation around speech, breath, and head movement. Their conjunction lets release image the reopening of a human bottleneck: agency is restored through an embodied articulation, not only through an abstract status.","model_id":"baseline_restore_articulation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_restore_articulation","source_type":"hft","support_id":"sup_49d022c5d355ee805a34","trust":"legacy_unbound"}]}
</lane_packet_json>
