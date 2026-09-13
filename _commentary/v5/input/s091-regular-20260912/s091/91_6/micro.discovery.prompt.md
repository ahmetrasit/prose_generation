# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **91:6**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s091-regular-20260912/s091/91_6/micro.discovery.json` and modify nothing
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
  "ayah_ref": "91:6",
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
{"branch_registry":[{"boundary":"Temel yer anlamı ile yalnız tamlamalarda beliren alt bölüm ve hayvan ayağı anlamları birbirinden ayrılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000025/B001","candidate_links":[{"candidate_id":"cand_30f6aab9261096309a4b","lane":"micro"},{"candidate_id":"cand_dd8cb7695208438214a6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:6:1:3","qac_word_ref":"91:6:1","surface_ar":"أَرْضِ"}],"gloss":"yer ve yere bakan alt bölüm","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Göğün karşısında aşağıda bulunan ve üzerinde yaşanan yer küresidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyin yere bakan alt bölümü, belirli bir tamlama içinde bu adla anılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hayvanın tırnağı veya ayağının yere değen alt bölümü için kullanılan özel bir tamlama vardır."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer küresi anlamını ve ona bağlı alt bölüm yönelimini birlikte özetleyen en kısa doğal karşılıktır.","boundary_detail":"Temel yer anlamı ile yalnız tamlamalarda beliren alt bölüm ve hayvan ayağı anlamları birbirinden ayrılmalıdır.","branch_image_ar":"السفل المقابل للسماء","concept_gloss":"yer ve yere bakan alt bölüm","contextual_glosses":[{"applicability":"Üzerinde yaşanan ve göğün karşısında bulunan yer küresi söz konusu olduğunda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesnelerin altı ile hayvan ayağının alt bölümüne bağlı kullanımları dışarıda bırakır.","preserves":"Üzerinde yaşanan aşağı yer ve göğe karşıt konum anlamını korur."},"facet_ids":["F001"],"text":"yeryüzü","usage_role":"contextual"}],"definition":"Göğün karşısında aşağıda bulunan, üzerinde yaşadığımız yer küresini belirtir. Belirli tamlamalarda bir şeyin yere bakan altını ve hayvanın tırnağını ya da ayağının alt bölümünü de anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Göğün karşısında aşağıda bulunan ve üzerinde yaşanan yer küresidir."},{"facet_id":"F002","role":"extension","statement":"Bir şeyin yere bakan alt bölümü, belirli bir tamlama içinde bu adla anılır."},{"facet_id":"F003","role":"specialization","statement":"Hayvanın tırnağı veya ayağının yere değen alt bölümü için kullanılan özel bir tamlama vardır."}],"identity_rationale":"Kaynak ifadesi, göğün karşısında aşağıda bulunan ve üzerinde yaşanan yeri temel anlam olarak verir; nesnelerin yere bakan altı ile hayvan ayağının alt bölümü de buna bağlı kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yer, yeryüzü"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yerler, ülkeler"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyin yere bakan altı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"hayvanın tırnağı veya ayaklarının altı"}],"lexicalization_note":"Tanım yalın yer anlamını kapsar; alt bölüm ve hayvan ayağı anlamlarını ise yalnız belirtilen tamlamalara bağlı yan yüzler olarak tutar.","neighbor_coverage_note":"Sağlanan bütün komşu kartları değerlendirildi; yer yüzeyiyle doğrudan karışabilecek en yararlı sınır karşılaştırması yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği aşağıda ve göğün karşısında bulunan yerdir; komşu dal ise yüzeyin genişliği ve düzlüğü ile serilmiş eşya fikrini öne çıkarır.","focus_only":"Göğün karşısındaki yer küresini ve tamlamalardaki alt bölüm anlamlarını kapsar.","gloss":"geniş düz yer veya yaygı","neighbor_only":"Geniş ve düz araziyi, ayrıca serilip yayılan eşyayı anlatır.","neighbor_ref":"root_000116/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da yayılmış bir yüzey olarak yer alanına dokunur."}],"source_phrase_ar":"كل شيء يسفل ويقابل السماء (maqayis)؛ الأرض التي نحن عليها (maqayis)؛ الأرض الجرم المقابل للسماء (mufradat)؛ كل ما سفل فهو أرض (sihah)؛ الأرض حافر الدابة (ayn)؛ أسفل قوائم الدابة (sihah)","source_summary":"Kaynaklar, anlamın merkezinde göğün karşısındaki aşağı yerin bulunduğunu; alt bölüm ve hayvan ayağı kullanımlarının bu mekansal çekirdeğe dayandığını birlikte gösterir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"الأرض التي نحن عليها؛ كل ما سفل وقابل السماء؛ أسفل الشيء وقوائم الدابة وما يلي الأرض منها","what_is_not_ar":"ليس الزكام ولا الرعدة ولا الدودة ولا البساط"},"support_links":["sup_a2207e2ecbd8cd86ac7a","sup_b5b4b47a9990a0cc8a04"]},{"boundary":"Toprağın niteliği çekirdektir; bitkinin gelişmesi ve oğlağın beslenmesi sonuç ya da ilişkili kullanım olarak kalmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000025/B002","candidate_links":[{"candidate_id":"cand_31f9bd79256e03ceceba","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:6:1:3","qac_word_ref":"91:6:1","surface_ar":"أَرْضِ"}],"gloss":"yumuşak ve verimli toprak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Toprak veya çayırlık yumuşak, verimli ve iyi bitki yetiştirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bitki toprağa iyice yerleşir, çoğalır veya biçilecek olgunluğa ulaşır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Oğlak yer bitkisini yer."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir kaynakta ilgili niteleme semiz oğlağı belirtir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın toprak niteliğine dayanan çekirdeğini eksiksiz ve doğal biçimde karşılar.","boundary_detail":"Toprağın niteliği çekirdektir; bitkinin gelişmesi ve oğlağın beslenmesi sonuç ya da ilişkili kullanım olarak kalmalıdır.","branch_image_ar":"الأرض اللينة المنبتة","concept_gloss":"yumuşak ve verimli toprak","contextual_glosses":[{"applicability":"Bitkinin toprağa yerleşerek çoğalması anlatılan bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Toprağın genel niteliğini ve oğlağın bu bitkiyle beslenmesi yüzünü dışarıda bırakır.","preserves":"Bitkinin toprağa yerleşmesi ve gelişerek çoğalması sürecini korur."},"facet_ids":["F002"],"text":"iyice köklenip çoğalmak","usage_role":"contextual"}],"definition":"Belirtilen yapılarda yumuşak, iyi, verimli ve bol bitki yetiştiren toprağı anlatır. Buna bağlı yapılarda bitkinin toprağa iyice yerleşip çoğalması veya biçilebilir olması, köklü fidan ve yer bitkisini yiyen oğlak; ayrı bir kaynak kullanımında ise semiz oğlak ifade edilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Toprak veya çayırlık yumuşak, verimli ve iyi bitki yetiştirir."},{"facet_id":"F002","role":"extension","statement":"Bitki toprağa iyice yerleşir, çoğalır veya biçilecek olgunluğa ulaşır."},{"facet_id":"F003","role":"associated_use","statement":"Oğlak yer bitkisini yer."},{"facet_id":"F004","role":"source_variant","statement":"Bir kaynakta ilgili niteleme semiz oğlağı belirtir."}],"identity_rationale":"Kaynak ifadesi yumuşak, iyi ve verimli toprağı merkez alır; bitkinin köklenip çoğalması veya biçilecek duruma gelmesi ile oğlağın bu ottan yiyip semirmesi buna bağlı gelişmelerdir.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yumuşak, verimli ve bol bitkili toprak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yumuşak tabanlı geniş çayırlık"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"toprak verimlileşti"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bitki iyice köklendi, çoğaldı veya biçilecek duruma geldi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"toprakta kök salmış fidan"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"oğlak yer bitkisini yedi veya onunla semirdi"}],"lexicalization_note":"Tanım, nitelikli toprak anlamını yalnız kanıtlanan tamlamalara; bitki, fidan ve oğlakla ilgili anlamları da kendi kanıtlanmış yapılarına bağlar.","neighbor_coverage_note":"Bütün adaylar incelendi; verimli toprak çekirdeğine en yakın olup kapsam farkı taşıyan kart seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yumuşaklık ve iyi bitkilenmeyle birlikte belirli bitki ve oğlak yapılarını taşır; komşu dal kolaylık ve hızlı yetişme niteliğine uzanır.","focus_only":"Bitkinin yerleşmesi, biçilebilir olması ve oğlağın bitkiyle beslenmesi gibi bağlı kullanımları vardır.","gloss":"kolay işlenen verimli toprak","neighbor_only":"Kolay işlenen yer ve bitkinin hızlı yetişmesi özelliklerini daha genel biçimde kapsar.","neighbor_ref":"root_000058/B004","relation_type":"near_synonym","shared_zone":"İki dal da verimli, iyi bitki yetiştiren toprağı anlatır."}],"source_phrase_ar":"أرض أريضة لينة طيبة (maqayis;ayn)؛ أرض أريضة أي زكية (sihah)؛ حسنة النبت (mufradat)؛ تأرض النبت إذا أمكن أن يجز (maqayis;sihah)؛ تأرض النبت تمكن على الأرض فكثر (mufradat)؛ تأرض الجدي إذا تناول نبت الأرض (mufradat)؛ جدي أريض أي سمين (sihah)","source_summary":"Birleşik kanıt, verimli ve yumuşak toprağı; bu toprakta gelişen bitkiyi ve bitkiden yararlanan oğlağı aynı üretkenlik ilişkisi içinde toplar.","sources":["MQ","AY","SI","MU"],"what_is_ar":"الأرض الأريضة والروضة الأريضة؛ الأرض الزاكية الحسنة النبت؛ النبات المتأرض إذا تمكن في الأرض وكثر أو أمكن جزه؛ الجدي الأريض إذا تناول نبت الأرض أو سمن","what_is_not_ar":"ليس أسفل الشيء مطلقا ولا الرعدة ولا الزكام"},"support_links":["sup_05e42556c0e123b69aed"]},{"boundary":"Anlam yalnız verilen kişi ve eylem yapılarında geçerlidir; genel bir kök anlamı veya doğrudan ahlaki iyilik adı değildir.","branch_kind":"collocation","branch_ref":"root_000025/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:6:1:3","qac_word_ref":"91:6:1","surface_ar":"أَرْضِ"}],"gloss":"iyiliğe yatkın ve layık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi iyiliğe yatkın ve ona layıktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karşılaştırmalı yapıda kişi, belirli bir işi yapmaya grubun en uygun üyesidir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kaynak bu kişi niteliğini alçak gönüllülükle birlikte verir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kişi hakkında kurulan belirtilmiş yapıda dalın temel niteliğini karşılar.","boundary_detail":"Anlam yalnız verilen kişi ve eylem yapılarında geçerlidir; genel bir kök anlamı veya doğrudan ahlaki iyilik adı değildir.","branch_image_ar":"الخليق بالخير كالأرض الأريضة","concept_gloss":"iyiliğe yatkın ve layık","contextual_glosses":[{"applicability":"Bir topluluk içinden belirli işi yapmaya en uygun kişi seçildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İyiliğe yatkın ve alçak gönüllü kişi niteliğini dışarıda bırakır.","preserves":"Belirli eyleme başkalarından daha uygun ve layık olma karşılaştırmasını korur."},"facet_ids":["F002"],"text":"bunu yapmaya en uygunları","usage_role":"contextual"}],"definition":"Belirli yapılarda bir kişinin iyiliğe yatkın ve ona layık olmasını anlatır; bir kaynak bu niteliği alçak gönüllülükle birlikte verir. Karşılaştırmalı kullanımda ise bir işi yapmaya başkalarından daha uygun olmayı bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi iyiliğe yatkın ve ona layıktır."},{"facet_id":"F002","role":"specialization","statement":"Karşılaştırmalı yapıda kişi, belirli bir işi yapmaya grubun en uygun üyesidir."},{"facet_id":"F003","role":"source_variant","statement":"Bir kaynak bu kişi niteliğini alçak gönüllülükle birlikte verir."}],"identity_rationale":"Kaynak ifadesi belirli yapılarda bir kişinin iyiliğe yatkın, ona layık ve alçak gönüllü oluşunu; karşılaştırmalı yapıda ise bir işi yapmaya en uygun kişi sayılmasını bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"iyiliğe yatkın, layık ve alçak gönüllü kişi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bunu yapmaya en uygunları"}],"lexicalization_note":"Tanım bütünüyle belirtilen kişi ve eylem tamlamalarına bağlıdır; yalın biçime bağımsız bir uygunluk anlamı yüklenmez.","neighbor_coverage_note":"Tüm komşular değerlendirildi; genel layıklık alanıyla karışma olasılığı en yüksek olan karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal iyilik alanına ve iki belirli yapıya bağlıdır; komşu dalın uygunluk ve hazır oluş kapsamı daha geneldir.","focus_only":"İyiliğe yatkınlıkla birlikte alçak gönüllülük çağrışımı ve belirli kalıplara bağlılık taşır.","gloss":"bir şeye layık ve hazır","neighbor_only":"Herhangi bir şeye hazır, uygun veya layık olmayı daha geniş biçimde anlatır.","neighbor_ref":"root_000434/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişi ile uygun görüldüğü nitelik veya eylem arasındaki yatkınlık ilişkisini bildirir."}],"source_phrase_ar":"رجل أريض للخير أي خليق له شبه بالأرض الأريضة (maqayis)؛ رجل أريض أي متواضع خليق للخير (sihah)؛ هو آرضهم أن يفعل ذلك أي أخلقهم (sihah)","source_summary":"Kaynaklar, iyiliğe yatkınlık ve layıklık ile belirli bir eyleme en uygun olma yargısını yapı bağımlı tek bir uygunluk alanında birleştirir.","sources":["MQ","SI"],"what_is_ar":"الرجل الأريض للخير؛ آرض القوم أن يفعل الشيء أي أخلقهم به","what_is_not_ar":"ليس الأرض الحسية ولا الزكام ولا الرعدة"},"support_links":[]},{"boundary":"Bu anlam yalnız sabit adlandırmaya aittir ve genel olarak yeryüzünde yaşayan kişiyi anlatmaz.","branch_kind":"non_bare","branch_ref":"root_000025/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:6:1:3","qac_word_ref":"91:6:1","surface_ar":"أَرْضِ"}],"gloss":"yabancı kimse","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sabit söz birimi, bir yerde yabancı olan kimseyi adlandırır."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kanıtlanan sabit adlandırmanın kişi anlamını doğal biçimde karşılar.","boundary_detail":"Bu anlam yalnız sabit adlandırmaya aittir ve genel olarak yeryüzünde yaşayan kişiyi anlatmaz.","branch_image_ar":"ابن الأرض الغريب","concept_gloss":"yabancı kimse","definition":"Belirli bir sabit adlandırmada, bulunduğu çevreye dışarıdan gelen veya oraya ait olmayan yabancı kimseyi belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sabit söz birimi, bir yerde yabancı olan kimseyi adlandırır."}],"identity_rationale":"Tek kaynak ifadesi, sabit bir adlandırmanın doğrudan yabancı kimse anlamına geldiğini belirtir; yer sakini veya soy bağına ilişkin daha ayrıntılı bir koşul kurmaz.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yabancı kimse"}],"lexicalization_note":"Tanım yalnız kanıtlanan sabit söz birimine bağlanır; parçaların yalın anlamlarından yeni bir kişi sınıfı türetilmez.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi; genel yabancı anlamına en yakın, fakat topluluk koşuluyla ayrılan komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kanıtı yalnız yabancı olmayı söyler; komşu dal yabancının başka bir topluluk içinde bulunması koşulunu açıkça taşır.","focus_only":"Yabancılığı herhangi bir ek topluluk koşulu vermeden sabit bir adlandırmayla bildirir.","gloss":"başka bir topluluğa girmiş yabancı","neighbor_only":"Kişinin kendisinden olmayan bir topluluğun içine girmiş bulunmasını özellikle belirtir.","neighbor_ref":"root_000009/B006","relation_type":"near_synonym","shared_zone":"İki dal da bulunduğu insan çevresine aslen ait olmayan kişiyi anlatır."}],"source_phrase_ar":"فلان ابن أرض أي غريب (maqayis)","source_summary":"Tek kanıt, söz biriminin yabancı kimseyi belirten kısıtlı ve kalıplaşmış bir adlandırma olduğunu gösterir.","sources":["MQ"],"what_is_ar":"ابن أرض إذا أريد الغريب","what_is_not_ar":"ليس ساكن الأرض مطلقا ولا الأرض التي نحن عليها"},"support_links":[]},{"boundary":"Bu dal genel yer, hasır, döşek veya süslü kumaş değil; malzemesi ve kalınlığı belirtilmiş bir yaygıdır.","branch_kind":"bare","branch_ref":"root_000025/B005","candidate_links":[{"candidate_id":"cand_31f9bd79256e03ceceba","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:6:1:3","qac_word_ref":"91:6:1","surface_ar":"أَرْضِ"}],"gloss":"kalın yün veya kıl yaygı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne, yün ya da hayvan kılından yapılmış kalın bir yaygıdır."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesnenin türünü, belirleyici kalınlığını ve iki olası malzemesini birlikte karşılar.","boundary_detail":"Bu dal genel yer, hasır, döşek veya süslü kumaş değil; malzemesi ve kalınlığı belirtilmiş bir yaygıdır.","branch_image_ar":"الإراض البساط الضخم","concept_gloss":"kalın yün veya kıl yaygı","definition":"Yünden veya hayvan kılından yapılmış kalın ve büyükçe bir yaygıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne, yün ya da hayvan kılından yapılmış kalın bir yaygıdır."}],"identity_rationale":"Kaynak ifadesi nesneyi kalın, büyükçe bir yaygı olarak tanımlar ve malzemesini yün ya da hayvan kılıyla sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kalın yün veya kıl yaygı"}],"lexicalization_note":"Tanım yalın adın kanıtlanan nesne anlamıyla sınırlıdır ve komşu döşeme türlerinin özelliklerini içeri almaz.","neighbor_coverage_note":"Sağlanan kartların tümü değerlendirildi; nesne türü bakımından en yakın fakat kapsamı daha geniş döşeme komşusu yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal malzeme ve kalınlıkla tanımlanan belirli bir yaygıdır; komşu dal işlevi bakımından daha geniş bir döşeme sınıfıdır.","focus_only":"Yaygının kalın ve özellikle yün ya da hayvan kılından yapılmış olmasını gerektirir.","gloss":"döşek veya alta serilen örtü","neighbor_only":"Döşek, yatak örtüsü ve genel olarak alta serilen nesneleri kapsar.","neighbor_ref":"root_001397/B007","relation_type":"same_field","shared_zone":"Her iki dal da zemine ya da yatma yerine serilen ev eşyalarını adlandırır."}],"source_phrase_ar":"الإراض بساط ضخم من وبر أو صوف (maqayis)؛ الإراض بالكسر بساط ضخم من صوف أو وبر (sihah)","source_summary":"Kaynaklar nesnenin yaygı oluşunda, kalınlığında ve yün ya da hayvan kılından yapılmasında birleşir.","sources":["MQ","SI"],"what_is_ar":"الإراض بالكسر؛ بساط ضخم من وبر أو صوف","what_is_not_ar":"ليس الأرض ولا الأرضة ولا الأريضة"},"support_links":["sup_05e42556c0e123b69aed"]},{"boundary":"Dal, yere yönelen ağırlık ve kalma durumudur; tembellik, geri kayma veya bir başkasına karşı çıkma değildir.","branch_kind":"bare","branch_ref":"root_000025/B006","candidate_links":[{"candidate_id":"cand_c7682506b05f0e13906c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:6:1:3","qac_word_ref":"91:6:1","surface_ar":"أَرْضِ"}],"gloss":"yere çökercesine ağırlaşıp oyalanmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi yerden ayrılmayarak yere bağlı kalır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yere doğru ağırlaşma, oyalanma ve gecikme olarak gerçekleşebilir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yere bağlılık, ağırlaşma ve gecikme bileşenlerini tek bir eylem karşılığında toplar.","boundary_detail":"Dal, yere yönelen ağırlık ve kalma durumudur; tembellik, geri kayma veya bir başkasına karşı çıkma değildir.","branch_image_ar":"لزوم الأرض والتثاقل إليها","concept_gloss":"yere çökercesine ağırlaşıp oyalanmak","contextual_glosses":[{"applicability":"Kişinin doğrudan yere bağlı kalması öne çıktığında kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yere doğru ağırlaşma ile oyalanıp gecikme görünüşlerini dışarıda bırakır.","preserves":"Yere bağlı kalma ve bulunduğu noktadan ayrılmama durumunu korur."},"facet_ids":["F001"],"text":"yerinden ayrılmamak","usage_role":"contextual"}],"definition":"Kişinin yere bağlı kalmasını veya yere çökercesine ağırlaşmasını ve bu yüzden bir süre oyalanıp gecikmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi yerden ayrılmayarak yere bağlı kalır."},{"facet_id":"F002","role":"extension","statement":"Yere doğru ağırlaşma, oyalanma ve gecikme olarak gerçekleşebilir."}],"identity_rationale":"Kaynak ifadesi kişinin yere bağlı kalmasını, yere doğru ağırlaşmasını ve bunun sonucu oyalanıp gecikmesini aynı hareket durumu içinde verir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yere bağlı kalmak, ağırlaşıp oyalanmak"}],"lexicalization_note":"Tanım yalın eylem dalının yere bağlı kalma, ağırlaşma ve gecikme bileşenleriyle sınırlıdır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yere bağlı kalma çekirdeğini en doğrudan paylaşan ve kapsam farkını gösteren komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişinin yere doğru ağırlaşıp gecikmesini anlatır; komşu dal farklı canlı ve nesnelerde yere yapışma ya da sabit kalma alanına daha geniş yayılır.","focus_only":"İnsan için yere doğru ağırlaşma ve bununla birlikte oyalanma anlamını taşır.","gloss":"yere yapışıp yerinde kalmak","neighbor_only":"İnsan dışında kuş ve yırtıcıları, ayrıca yuva ve yerinde ağır duran nesne örneklerini de kapsar.","neighbor_ref":"root_000222/B001","relation_type":"near_synonym","shared_zone":"İki dalda da yere yakın durma ve bulunulan yerden ayrılmama durumu vardır."}],"source_phrase_ar":"تأرض فلان إذا لزم الأرض (maqayis)؛ فقام عجلان وما تأرضا أي ما تلبث (sihah)؛ التأرض أيضا التثاقل إلى الأرض (sihah)","source_summary":"Kanıt, yere bağlı kalmayı çekirdek alır ve yere doğru ağırlaşma ile oyalanmayı bu durumun görünüşleri olarak birleştirir.","sources":["MQ","SI"],"what_is_ar":"تأرض فلان إذا لزم الأرض؛ التأرض بمعنى التثاقل والتلبث إلى الأرض","what_is_not_ar":"ليس التصدي والتعرض للغير ولا النبات المتأرض"},"support_links":["sup_dc7698ab653ef6fd7627"]},{"boundary":"Bu dal bir başkasına yönelmiş karşı duruşu anlatır; yere çökme, ağırlaşma veya yalnızca yüz yüze bulunma değildir.","branch_kind":"bare","branch_ref":"root_000025/B007","candidate_links":[{"candidate_id":"cand_5f9419eca25aa1dab2f0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:6:1:3","qac_word_ref":"91:6:1","surface_ar":"أَرْضِ"}],"gloss":"karşısına çıkıp kendini ortaya koymak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir başkasına yönelir, karşısına çıkar ve kendini ona karşı ortaya koyar."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiye yönelmiş karşı duruşu ve görünür biçimde ortaya çıkmayı birlikte karşılar.","boundary_detail":"Bu dal bir başkasına yönelmiş karşı duruşu anlatır; yere çökme, ağırlaşma veya yalnızca yüz yüze bulunma değildir.","branch_image_ar":"التعرض والتصدي","concept_gloss":"karşısına çıkıp kendini ortaya koymak","definition":"Birine doğru yönelip onun karşısına çıkmayı, kendini ortaya koyarak ona karşı durmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir başkasına yönelir, karşısına çıkar ve kendini ona karşı ortaya koyar."}],"identity_rationale":"Tek kaynak ifadesi eylemi, birine doğru çıkıp onun karşısında kendini ortaya koymak ve ona karşı durmak biçiminde açıklar.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"birinin karşısına çıkıp kendini ortaya koymak"}],"lexicalization_note":"Tanım yalın eylem dalını, bir hedefe yönelme ve karşısına çıkma koşullarıyla sınırlar.","neighbor_coverage_note":"Tüm komşular değerlendirildi; yönelme ve karşıya çıkma çekirdeğini en yakından paylaşan aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişiler arası karşıya çıkışı öne çıkarır; komşu dal bakma, gözetme ve genel yüzünü dönme kullanımlarını da kapsar.","focus_only":"Bir kişiye doğru gelerek onun karşısında kendini ortaya koyma hareketini bildirir.","gloss":"bir şeye yönelip karşısına çıkmak","neighbor_only":"Bir şeye bakmak üzere yükselme, onu gözetme veya yalnızca yüzünü ona çevirme kapsamına uzanır.","neighbor_ref":"root_000853/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da bir hedefe yönelme ve onun karşısında konum alma anlamını taşır."}],"source_phrase_ar":"جاء فلان يتأرض إلي أي يتصدى ويتعرض (sihah)","source_summary":"Tek kanıt, eylemin hedefe yönelmiş bir karşıya çıkma ve kendini ortaya koyma hareketi olduğunu gösterir.","sources":["SI"],"what_is_ar":"جاء فلان يتأرض إلى غيره أي يتصدى ويتعرض له","what_is_not_ar":"ليس التثاقل إلى الأرض ولا لزومها"},"support_links":["sup_7d320ee9a06c2ff41d25"]},{"boundary":"Dal genel şiddetli sarsıntı veya belirli bir ateş nöbeti değil, insanda görülen titreme durumudur.","branch_kind":"bare","branch_ref":"root_000025/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:6:1:3","qac_word_ref":"91:6:1","surface_ar":"أَرْضِ"}],"gloss":"titreme veya ürperme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan bedenini tutan bir titreme veya ürperme meydana gelir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan bedenindeki kısa ya da süren sarsıntı durumunu doğrudan karşılar.","boundary_detail":"Dal genel şiddetli sarsıntı veya belirli bir ateş nöbeti değil, insanda görülen titreme durumudur.","branch_image_ar":"الأَرْض الرعدة","concept_gloss":"titreme veya ürperme","definition":"Bir insanın bedeninde beliren titreme, sarsılma veya ürperme durumudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan bedenini tutan bir titreme veya ürperme meydana gelir."}],"identity_rationale":"Kaynak ifadesi bu dalı insanda görülen titreme, sarsılma veya ürperme olarak açıkça tanımlar ve yer ya da hastalık anlamlarından ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"insanı tutan titreme veya ürperme"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"titreme ve sarsılma"}],"lexicalization_note":"Tanım yalın biçimlerin insandaki titreme ve ürperme anlamıyla sınırlıdır; komşu hastalık nedenleri eklenmez.","neighbor_coverage_note":"Sağlanan bütün kartlar incelendi; genel titreme çekirdeğine en yakın ve kapsam farkı belirgin olan komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalın bir insan titremesidir; komşu dal nedeni ve öznesi bakımından daha geniştir, ayrıca korkaklık ve gevşeklik nitelemelerine uzanır.","focus_only":"İnsan bedenindeki titreme durumunu herhangi bir özel neden belirtmeden adlandırır.","gloss":"korku veya hastalıktan sarsılma","neighbor_only":"Korku, hastalık veya gevşeklik nedeniyle insan ya da başka bir şeyin sarsılmasını ve kişilik nitelemelerini kapsar.","neighbor_ref":"root_000573/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da insan bedenindeki titreme ve sarsılma alanında örtüşür."}],"source_phrase_ar":"الأرض الرعدة (maqayis;ayn)؛ بفلان أرض أي رعدة (maqayis)؛ الأرْص النفضة والرعدة (sihah)","source_summary":"Kaynaklar bu adın insanda görülen titreme ve ürperme durumunu bildirdiğinde birleşir.","sources":["MQ","AY","SI"],"what_is_ar":"الأَرْض بمعنى الرعدة أو النفضة في الإنسان","what_is_not_ar":"ليس الأرض التي تقابل السماء ولا الزكام"},"support_links":[]},{"boundary":"Dal solunumla ilgili başka hastalıkları veya genel beden titremesini değil, soğuk algınlığı durumunu ve ilgili türevleri kapsar.","branch_kind":"bare","branch_ref":"root_000025/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:6:1:3","qac_word_ref":"91:6:1","surface_ar":"أَرْضِ"}],"gloss":"soğuk algınlığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Soğuk algınlığı durumudur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Türemiş biçim, soğuk algınlığına yakalanmış kişiyi niteler."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen biçim, birini soğuk algınlığına uğratmayı bildirir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hastalık çekirdeğini Türkçede en doğal ve ayırt edici biçimde karşılar.","boundary_detail":"Dal solunumla ilgili başka hastalıkları veya genel beden titremesini değil, soğuk algınlığı durumunu ve ilgili türevleri kapsar.","branch_image_ar":"الأَرْض الزكام","concept_gloss":"soğuk algınlığı","contextual_glosses":[{"applicability":"Hastalığın kendisi değil, bu hastalığa tutulmuş kişi nitelendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hastalık adını ve birini hastalığa uğratma eylemini bağımsız olarak karşılamaz.","preserves":"Soğuk algınlığı ile kişi arasındaki etkilenme ilişkisini korur."},"facet_ids":["F002"],"text":"soğuk algınlığına yakalanmış","usage_role":"contextual"}],"definition":"Soğuk algınlığı hastalığını, bu hastalığa yakalanmış kişiyi ve birini bu hastalığa uğratma eylemini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Soğuk algınlığı durumudur."},{"facet_id":"F002","role":"specialization","statement":"Türemiş biçim, soğuk algınlığına yakalanmış kişiyi niteler."},{"facet_id":"F003","role":"associated_use","statement":"Ettirgen biçim, birini soğuk algınlığına uğratmayı bildirir."}],"identity_rationale":"Kaynak ifadesi hastalığı soğuk algınlığı olarak, etkilenen kişiyi bu hastalığa yakalanmış olarak ve ettirgen biçimi hastalığa uğratmak olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"soğuk algınlığı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"soğuk algınlığına yakalanmış"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"soğuk algınlığına uğratmak"}],"lexicalization_note":"Tanım yalın hastalık adını ve aynı dalda kanıtlanan hasta kişi ile hastalığa uğratma türevlerini korur.","neighbor_coverage_note":"Bütün komşu kartları değerlendirildi; aynı hastalık ve hasta kişi alanını en doğrudan paylaşan aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın türetim dizisinde hastalığa uğratma da vardır; komşu dalın kanıtı ise bir kaynakta daha genel hastalık yorumu içerir.","focus_only":"Hastalık adı, hastaya ilişkin niteleme ve hastalığa uğratma eylemini birlikte kapsar.","gloss":"soğuk algınlığı ve hasta olma","neighbor_only":"Soğuk algınlığı yanında daha genel bir hastalık alanına açılan ayrı bir kaynak yorumunu da taşır.","neighbor_ref":"root_000916/B003","relation_type":"near_synonym","shared_zone":"Her iki dal soğuk algınlığını ve bu hastalığa yakalanmış kişiyi ifade eder."}],"source_phrase_ar":"الأرض الزكمة رجل مأروض أي مزكوم (maqayis)؛ الأرض الزكام وأرض فهو مأروض (ayn)؛ الأرض الزكام وقد آرضه الله إيراضا أي أزكمه فهو مأروض (sihah)","source_summary":"Kaynaklar hastalık adı ile hasta kişi nitelemesinde birleşir; kanıt ayrıca hastalığa uğratma eylemini aynı türetim alanında gösterir.","sources":["MQ","AY","SI"],"what_is_ar":"الأَرْض بمعنى الزكمة أو الزكام؛ مأروض لمن أصابه الزكام","what_is_not_ar":"ليس الرعدة ولا الأرض الحسية"},"support_links":[]},{"boundary":"Canlının kendisi çekirdektir; odunun yenmiş duruma gelmesi yalnız belirtilen eylem yapısına bağlı sonuçtur.","branch_kind":"mixed_non_bare","branch_ref":"root_000025/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:6:1:3","qac_word_ref":"91:6:1","surface_ar":"أَرْضِ"}],"gloss":"odun yiyen küçük canlı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Küçük canlı odunla beslenir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Canlı odunu yiyerek onu aşınmış ve zarar görmüş hale getirir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kaynak canlıyı beyaz ve karıncaya benzer olarak niteler."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Canlıyı kanıtlanan boyutu ve onu ayırt eden beslenme davranışıyla kısa ve doğal biçimde karşılar.","boundary_detail":"Canlının kendisi çekirdektir; odunun yenmiş duruma gelmesi yalnız belirtilen eylem yapısına bağlı sonuçtur.","branch_image_ar":"الأَرَضَة آكلة الخشب","concept_gloss":"odun yiyen küçük canlı","contextual_glosses":[{"applicability":"Bir odunun bu canlı tarafından yenerek zarar görmüş olduğu bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Canlının beyaz ve karıncaya benzer oluşunu bağımsız bir tanım olarak vermez.","preserves":"Odunun canlı tarafından yenmiş ve zarar görmüş olma sonucunu korur."},"facet_ids":["F002"],"text":"odun yiyen küçük canlı tarafından yenmiş","usage_role":"contextual"}],"definition":"Odun yiyen küçük bir canlıyı belirtir. İlgili eylem yapısı, bu canlının bir odunu yiyip zarar görmüş hale getirmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Küçük canlı odunla beslenir."},{"facet_id":"F002","role":"associated_use","statement":"Canlı odunu yiyerek onu aşınmış ve zarar görmüş hale getirir."},{"facet_id":"F003","role":"source_variant","statement":"Bir kaynak canlıyı beyaz ve karıncaya benzer olarak niteler."}],"identity_rationale":"Kaynak ifadesi beyaz, karıncaya benzeyen ve odun yiyen küçük canlıyı tanımlar; ayrıca bu canlının odunu yiyerek onu zarar görmüş hale getirmesini verir.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"odun yiyen küçük canlı"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"odunu bu canlı yedi ve zarar verdi"}],"lexicalization_note":"Tanım canlı adını yalın çekirdek olarak verir ve odunun yenmesini yalnız kanıtlanan tamlamaya bağlı sonuç yüzü olarak ayırır.","neighbor_coverage_note":"Tüm aday kartlar değerlendirildi; odun yiyen canlı çekirdeğine en yakın fakat canlı ve nesne kapsamı farklı olan komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal odun yiyen küçük canlı ve onun oduna etkisidir; komşu dal ağaç, yaprak ve gövde üzerinde beslenen başka bir canlıya özgüdür.","focus_only":"Odun yiyen küçük canlıyı ve bu canlının yediği odunun sonucunu belirtir.","gloss":"ağacı delen ve yiyen küçük canlı","neighbor_only":"Özellikle ağaçta delik açan, yaprak veya odun yiyen başka bir küçük canlıyı ve ağacın uğradığı durumu kapsar.","neighbor_ref":"root_000699/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da odunsu bitki maddesini yiyerek zarar veren küçük canlıları anlatır."}],"source_phrase_ar":"الأرضة دويبة بيضاء تشبه النمل تأكل الخشب (ayn)؛ الأرضة بالتحريك دويبة تأكل الخشب (sihah)؛ أرضت الخشبة تؤرض أرضا فهي مأروضة إذا أكلتها (sihah)؛ الأرضة الدودة التي تقع في الخشب من الأرض (mufradat)؛ أرضت الخشبة فهي مأروضة (mufradat)","source_summary":"Kaynaklar odun yiyen küçük canlı ile onun odunda oluşturduğu yenme ve zarar görme sonucunu aynı anlam alanında birleştirir.","sources":["AY","SI","MU"],"what_is_ar":"الأَرَضَة؛ دويبة تأكل الخشب؛ أرضت الخشبة فهي مأروضة إذا أكلتها الأرضة","what_is_not_ar":"ليس الأرض ولا الأرض الأريضة ولا الزكام"},"support_links":[]},{"boundary":"Anlam yalnız yara ile kurulan yapıda geçerlidir ve irinlenmenin yol açtığı bozulmayı zorunlu olarak içerir.","branch_kind":"collocation","branch_ref":"root_000025/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:6:1:3","qac_word_ref":"91:6:1","surface_ar":"أَرْضِ"}],"gloss":"yaranın irinlenip bozulması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yara irin toplayarak kabarır ve irinlenme sonucunda bozulur."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız yara bağlamında irin toplama ile ortaya çıkan bozulma sürecini eksiksiz karşılar.","boundary_detail":"Anlam yalnız yara ile kurulan yapıda geçerlidir ve irinlenmenin yol açtığı bozulmayı zorunlu olarak içerir.","branch_image_ar":"فساد القرحة بالمدة","concept_gloss":"yaranın irinlenip bozulması","definition":"Bir yaranın irin toplaması, kabarıp su toplaması ve bu irinlenme yüzünden bozulmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yara irin toplayarak kabarır ve irinlenme sonucunda bozulur."}],"identity_rationale":"Tek kaynak ifadesi, yaranın irin toplamasıyla kabarıp bozulmasını bir süreç olarak verir; yalnız irin maddesini veya genel deri şişliğini adlandırmaz.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yara irinlenip kabardı ve bozuldu"}],"lexicalization_note":"Tanım yalnız yara öznesiyle kurulan kanıtlanmış tamlamaya bağlıdır; yalın biçime genel bozulma anlamı verilmez.","neighbor_coverage_note":"Bütün komşular incelendi; irin birikmesi çekirdeğini en yakından paylaşan ve sonuç bakımından ayrılan kart yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal irin birikimini yaranın kabarıp bozulmasına bağlar; komşu dal yalnız irin toplanması ya da dışarı çıkmasıyla yetinebilir.","focus_only":"Yaranın irinlenmeyle kabarıp bozulması sürecini zorunlu olarak içerir.","gloss":"yarada irin toplanması","neighbor_only":"İrinin yarada toplanmasını veya yaradan çıkmasını, bozulma sonucu aramadan kapsar.","neighbor_ref":"root_001664/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da yaranın içinde irin birikmesi durumunu anlatır."}],"source_phrase_ar":"أرضت القرحة تأرض أرضا أي مجلت وفسدت بالمدة (sihah)","source_summary":"Tek kanıt, yara içindeki irinlenme ile kabarma ve bozulmayı birbirine bağlı tek bir hastalık süreci olarak gösterir.","sources":["SI"],"what_is_ar":"أرضت القرحة إذا مجلت وفسدت بالمدة","what_is_not_ar":"ليس الزكام ولا الأرضة ولا الرعدة"},"support_links":[]},{"boundary":"Dal yalnız akıl karışıklığı değildir; doğaüstü nedene bağlanma ve istemsiz baş-gövde hareketi birlikte korunmalıdır.","branch_kind":"bare","branch_ref":"root_000025/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:6:1:3","qac_word_ref":"91:6:1","surface_ar":"أَرْضِ"}],"gloss":"doğaüstü etkiye bağlanan istemsiz sarsıntılı akıl bozukluğu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin akıl ve beden durumu görünmez varlıkların etkisine bağlanır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Etkilenen kişi başını ve gövdesini bilinçli bir amaç olmadan hareket ettirir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Neden yorumunu, akıl durumunu ve belirleyici istemsiz beden hareketini birlikte açıklar.","boundary_detail":"Dal yalnız akıl karışıklığı değildir; doğaüstü nedene bağlanma ve istemsiz baş-gövde hareketi birlikte korunmalıdır.","branch_image_ar":"المأروض المخبول من أهل الأرض","concept_gloss":"doğaüstü etkiye bağlanan istemsiz sarsıntılı akıl bozukluğu","contextual_glosses":[{"applicability":"Kişinin gözlenebilir beden hareketi ön plana çıkarıldığında açıklayıcı karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Akıl bozukluğunu ve durumun görünmez varlıkların etkisine bağlanmasını dışarıda bırakır.","preserves":"Baş ve gövdenin bilinçli amaç olmadan hareket etmesi belirtisini korur."},"facet_ids":["F002"],"text":"başıyla gövdesini istemsizce sarsan kişi","usage_role":"explanatory"}],"definition":"Yerle ilişkilendirilen görünmez varlıkların etkisine bağlanan bir akıl ve beden bozukluğudur; etkilenen kişi başını ve gövdesini isteği dışında hareket ettirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin akıl ve beden durumu görünmez varlıkların etkisine bağlanır."},{"facet_id":"F002","role":"specialization","statement":"Etkilenen kişi başını ve gövdesini bilinçli bir amaç olmadan hareket ettirir."}],"identity_rationale":"Kaynak ifadesi, görünmez varlıkların etkisine bağlanan bir akıl ve beden bozukluğunu; kişinin başını ve gövdesini istemeden hareket ettirmesiyle birlikte tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"görünmez varlıkların etkisine bağlanan, başını ve gövdesini istemsizce hareket ettiren kişi"}],"lexicalization_note":"Tanım yalın kişi nitelemesinin doğaüstü açıklama, akıl bozukluğu ve istemsiz beden hareketi bileşenleriyle sınırlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; doğaüstü etkiye bağlanan akıl bozukluğu çekirdeğini en doğrudan paylaşan komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir kaynak ilişkilendirmesi ve istemsiz baş-gövde hareketi gerektirir; komşu dal daha genel bir doğaüstü dokunuş açıklamasıdır.","focus_only":"Yerle ilişkilendirilen görünmez varlıklar açıklamasını ve istemsiz baş-gövde hareketini birlikte taşır.","gloss":"doğaüstü dokunuşa bağlanan akıl karışıklığı","neighbor_only":"Doğaüstü bir dokunuşla açıklanan akıl karışıklığını beden hareketi koşulu olmadan daha genel verir.","neighbor_ref":"root_001423/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da akıl bozukluğunu görünmez bir varlığın etkisiyle açıklayan geleneksel anlayışta buluşur."}],"source_phrase_ar":"المأروض الذي به خبل من الجن وأهل الأرض وهو الذي يحرك رأسه وجسده على غير عمد (sihah)","source_summary":"Tek kanıt, doğaüstü varlıklara bağlanan akıl karışıklığını ve istemsiz baş-gövde hareketini aynı kişi durumunun ayrılmaz parçaları olarak verir.","sources":["SI"],"what_is_ar":"المأروض الذي به خبل من الجن وأهل الأرض ويحرك رأسه وجسده على غير عمد","what_is_not_ar":"ليس المزكوم المأروض ولا الخشبة المأروضة"},"support_links":[]},{"boundary":"Bu anlam uzaklara gitmeyi, kuşların dönmesini veya insanların birbirini itmesini kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000928/B001","candidate_links":[{"candidate_id":"cand_30f6aab9261096309a4b","lane":"micro"},{"candidate_id":"cand_31f9bd79256e03ceceba","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طَحَىٰ","morph_features":"STEM|POS:V|PERF|LEM:TaHaY`|ROOT:THw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:6:3:1","qac_word_ref":"91:6:3","surface_ar":"طَحَىٰ"}],"gloss":"yayma, uzatma ve genişletme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesneyi açarak yayma veya boylu boyunca uzatma eylemidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yeri yayma ve alanını genişletme uygulamasını da kapsar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yayılmış düz araziyi veya uzanmış ve yayılmış durumdaki şeyi niteleyebilir."}}],"root_ar":"ط ح و","root_id":"root_000928","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eylemi ve onun yayılmış sonuç durumunu birlikte temsil eden genel kavram karşılığıdır.","boundary_detail":"Bu anlam uzaklara gitmeyi, kuşların dönmesini veya insanların birbirini itmesini kapsamaz.","branch_image_ar":"البَسْط والمَدّ","concept_gloss":"yayma, uzatma ve genişletme","contextual_glosses":[{"applicability":"Bir nesne üzerinde yapılan temel eylemin aktarıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesnenin açılarak yayılması ve boylu boyunca uzatılması işlemini korur."},"facet_ids":["F001"],"text":"yayıp uzatmak","usage_role":"contextual"},{"applicability":"Eylemin araziye uygulanarak alanı açtığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yerin yayılması ile genişletilmesi arasındaki bağlantıyı korur."},"facet_ids":["F002"],"text":"yeri yayıp genişletmek","usage_role":"contextual"},{"applicability":"Eylemden çok ortaya çıkan yaygın veya uzanmış durumun nitelendiği bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yayma işleminin ortaya çıkardığı uzanmış sonuç durumunu korur."},"facet_ids":["F003"],"text":"yayılmış ve uzanmış","usage_role":"contextual"}],"definition":"Bir şeyi açıp yaymak, boylu boyunca uzatmak veya bir alanı genişletmektir; ayrıca bu işlemin sonucu olarak yerin yayılmış, şeyin ise uzanmış durumda olmasını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesneyi açarak yayma veya boylu boyunca uzatma eylemidir."},{"facet_id":"F002","role":"extension","statement":"Yeri yayma ve alanını genişletme uygulamasını da kapsar."},{"facet_id":"F003","role":"specialization","statement":"Yayılmış düz araziyi veya uzanmış ve yayılmış durumdaki şeyi niteleyebilir."}],"identity_rationale":"Kaynak ifadesi, bir şeyi ya da yeri yayma, uzatma ve genişletme çekirdeğini doğrudan destekler. Verilen çerçeve bu eylemle onun yayılmış veya uzanmış sonucunu doğru biçimde bir arada tutar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yayma ve uzatma"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yaymak veya uzatmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"onu yaydı veya uzattı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"onu yaydı veya genişletti"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yayılmış düz arazi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"uzanmış veya yayılmış"}],"lexicalization_note":"Tanım temel yayma eylemini, çekimli biçimleri ve yayılmış arazi ya da uzanmış şey bildiren türemiş kullanımları ayrı yüzler olarak korur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayıp uzatma sınırını en açık gösteren iki yakın anlam seçildi, yalnız ortak sahne paylaşan diğerleri yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yayma eylemiyle yayılmış arazi ve uzanmış sonuç biçimlerini birlikte taşır; komşu dal ise yayılma ile toplanma karşıtlığını ve genel genişletmeyi öne çıkarır.","focus_only":"Odak anlam yerin genişletilmesini ve yayılmış arazi sonucunu ayrıca belirginleştirir.","gloss":"yayılma ve uzama","neighbor_only":"Komşu anlam yayılmayı özellikle toplanmanın karşıtı olarak ve daha genel bir genişletme alanında kurar.","neighbor_ref":"root_000116/B001","relation_type":"near_synonym","shared_zone":"İki anlam da bir şeyin açılarak yayılması ve alan ya da uzunluk kazanması bölgesinde örtüşür."},{"boundary_match":"partial","distinction":"Odak anlamın çekirdeği yayma ve uzatmadır; komşu anlam bu işlemi hazırlama, döşeme ve yer düzenleme gibi özel amaçlara bağlar.","focus_only":"Odak dal yalın yayma, uzatma ve yerin genişlemesi çekirdeğini korur.","gloss":"serme ve hazırlama","neighbor_only":"Komşu dal serme yanında hazırlama, döşeme ve bütün bir işi düzenleme gibi amaçlı uygulamalar ekler.","neighbor_ref":"root_001143/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir şeyi yüzey üzerine açıp yayma işlemi bulunur."}],"source_phrase_ar":"الطحو وهو كالدحو وهو البسط (maqayis)؛ الطحو شبه الدحو وهو البسط (ayn)؛ طحوته مثل دحوته أي بسطته والطحا المنبسط من الأرض والطاحي الممتد (sihah)؛ الطحو كالدحو وهو البسط ودحاها وسعها وطحا إذا مد الشيء (tahdhib)؛ الطحو كالدحو وهو بسط الشيء (mufradat)","source_summary":"Kaynaklar anlamı yayma ekseninde birleştirir; nesnenin uzatılması, yerin genişletilmesi ve ortaya çıkan yayılmış durum bu çekirdeğin farklı gerçekleşmeleridir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه بسط الشيء والأرض ومد الشيء واتساعه وانبساطه","what_is_not_ar":"لا يدخل فيه الذهاب البعيد أو دوران النسور أو الدفع بين الناس"},"support_links":["sup_05e42556c0e123b69aed","sup_a2207e2ecbd8cd86ac7a"]},{"boundary":"Bu gidiş anlamı bir şeyi yüzeye yayma veya bir bedeni yere serme anlamlarından ayrıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000928/B002","candidate_links":[{"candidate_id":"cand_c7682506b05f0e13906c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طَحَىٰ","morph_features":"STEM|POS:V|PERF|LEM:TaHaY`|ROOT:THw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:6:3:1","qac_word_ref":"91:6:3","surface_ar":"طَحَىٰ"}],"gloss":"uzaklara gitme ve zihnen sürüklenme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin yeryüzünde bir yere, kimi zaman yeri bilinmeyecek kadar uzağa gitmesidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaygının kişiyi uzak bir meseleye götürmesi ve o mesele içinde sürüklemesidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gönlün kişiyi türlü yönlere veya uzak bir eğilime çekip götürmesidir."}}],"root_ar":"ط ح و","root_id":"root_000928","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel gidiş ile kaygı veya gönlün kişiyi uzak bir yöne çekmesini ortak çekirdekte toplar.","boundary_detail":"Bu gidiş anlamı bir şeyi yüzeye yayma veya bir bedeni yere serme anlamlarından ayrıdır.","branch_image_ar":"الذهاب المُمْتَدّ","concept_gloss":"uzaklara gitme ve zihnen sürüklenme","contextual_glosses":[{"applicability":"Bir insanın fiziksel olarak yola çıkıp uzaklaşmasını bildiren kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin yeryüzündeki fiziksel hareketini ve uzaklaşmasını korur."},"facet_ids":["F001"],"text":"yeryüzünde uzaklara gitmek","usage_role":"contextual"},{"applicability":"Kaygının kişiyi uzak bir mesele içinde uzun süre götürmesi bağlamına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kaygının kişiyi bir meseleye doğru çekip götürmesi ilişkisini korur."},"facet_ids":["F002"],"text":"kaygının uzağa sürüklemesi","usage_role":"contextual"},{"applicability":"Gönlün sahibini farklı eğilimlere çektiği anlatımlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gönlün tek bir yerde kalmayıp çeşitli yönlere gitmesi anlamını korur."},"facet_ids":["F003"],"text":"gönlün türlü yönlere gitmesi","usage_role":"contextual"}],"definition":"Bir kişinin yeryüzünde uzaklara doğru gitmesi veya kaygısının ya da gönlünün onu uzak bir konuya ve çeşitli yönlere sürüklemesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin yeryüzünde bir yere, kimi zaman yeri bilinmeyecek kadar uzağa gitmesidir."},{"facet_id":"F002","role":"extension","statement":"Kaygının kişiyi uzak bir meseleye götürmesi ve o mesele içinde sürüklemesidir."},{"facet_id":"F003","role":"extension","statement":"Gönlün kişiyi türlü yönlere veya uzak bir eğilime çekip götürmesidir."}],"identity_rationale":"Kaynak ifadesi hem insanın yeryüzünde uzaklaşarak gitmesini hem de kaygı ya da gönlün kişiyi uzak bir düşünce yönüne sürüklemesini açıkça bildirir. Dal çerçevesi, ortak uzun ve yönü açılan gidiş çekirdeğini korur.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kaygısı onu uzak bir meseleye sürükledi"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"gönlü onu her yana sürükledi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"adam yeryüzünde uzaklara gitti"}],"lexicalization_note":"Tanım, kişinin gitmesini bildiren biçim ile kaygı ya da gönül öznesine bağlı kalıplaşmış sürüklenme kullanımlarını birbirine karıştırmadan kapsar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; uzak yolculukla yakın örtüşen ve yönsüzlükle karışabilecek iki aday sınırı açıklamak üzere seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu anlam fiziksel yolculuğun süresini ve şiddetini öne çıkarır; odak anlam ise fiziksel gidiş yanında kaygı ve gönül aracılığıyla düşünsel sürüklenmeyi kapsar.","focus_only":"Odak dal kaygı ve gönlün kişiyi düşünsel olarak sürüklemesini de içerir.","gloss":"uzun ve uzak yolculuk","neighbor_only":"Komşu dal bütün gün süren, uzak ve şiddetli yolculuğu özellikle belirginleştirir.","neighbor_ref":"root_001396/B005","relation_type":"near_synonym","shared_zone":"İki dal da uzun bir mesafeye doğru gitme ve hedefi uzaklaştırma alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dalın ayırıcı yanı uzaklaşma ve zihinsel sürüklenmedir; komşu dalın zorunlu bileşeni ise şaşkınlık ve yolunu yitirmedir.","focus_only":"Odak gidiş uzak veya çeşitli yönlere açılır fakat şaşkınlık koşulu taşımaz.","gloss":"şaşkın biçimde dolaşma","neighbor_only":"Komşu anlamda kişi yönünü şaşırmış ve ne tarafa gideceğini bilemez durumdadır.","neighbor_ref":"root_000191/B001","relation_type":"near_neighbor","shared_zone":"Her ikisi de belirgin bir varış noktasından uzaklaşan yönsüz görünümlü hareketi anlatabilir."}],"source_phrase_ar":"طحا بك همك يطحو إذا ذهب بك في الأمر ومد بك فيه (maqayis)؛ طحا بك همك أي ذهب بك في مذهب بعيد (ayn;tahdhib)؛ طحا الرجل إذا ذهب في الأرض وما أدري أين طحا وطحا به قلبه إذا ذهب في كل شيء (sihah)؛ بسط الشيء والذهاب به وطحا بك قلب أي ذهب (mufradat)","source_summary":"Kaynakların ortak ekseni uzaklaşan gidiştir; bu hareket bazen insanın yeryüzündeki yolculuğu, bazen de kaygı veya gönlün kişiyi düşünsel olarak sürüklemesidir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه ذهاب الهم أو القلب بصاحبه في أمر بعيد وذهاب الرجل في الأرض","what_is_not_ar":"لا يدخل فيه بسط الأرض أو انبطاح الجسد"},"support_links":["sup_dc7698ab653ef6fd7627"]},{"boundary":"Anlam yalnız ölülerin çevresinde dönen akbabaları bildiren söz öbeğine bağlıdır.","branch_kind":"collocation","branch_ref":"root_000928/B003","candidate_links":[{"candidate_id":"cand_c7682506b05f0e13906c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طَحَىٰ","morph_features":"STEM|POS:V|PERF|LEM:TaHaY`|ROOT:THw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:6:3:1","qac_word_ref":"91:6:3","surface_ar":"طَحَىٰ"}],"gloss":"ölülerin çevresinde dönen akbabalar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Akbabaların ölülerin çevresinde dönerek daireler çizmesini bildirir."}}],"root_ar":"ط ح و","root_id":"root_000928","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli kuşları, çevresinde döndükleri ölülerle birlikte tanımlayan tam söz öbeği karşılığıdır.","boundary_detail":"Anlam yalnız ölülerin çevresinde dönen akbabaları bildiren söz öbeğine bağlıdır.","branch_image_ar":"دَوَران النسور","concept_gloss":"ölülerin çevresinde dönen akbabalar","contextual_glosses":[{"applicability":"Tek bir ölünün çevresindeki kuş hareketini akıcı biçimde aktaran bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kuş türünü, çevresel hareketi ve merkezdeki ölüyü eksiksiz korur."},"facet_ids":["F001"],"text":"ölünün çevresinde daire çizen akbabalar","usage_role":"contextual"}],"definition":"Ölülerin ya da bir ölünün çevresinde daireler çizerek dönen akbabaları bildiren söz öbeğine özgü nitelemedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Akbabaların ölülerin çevresinde dönerek daireler çizmesini bildirir."}],"identity_rationale":"Kaynak ifadesi belirli bir kuş topluluğunu, ölülerin ya da tek bir ölünün çevresinde daireler çizmesiyle tanımlar. Dal çerçevesi bu sınırlı görüntüyü genel dönme veya uçma anlamına genişletmeden doğru aktarır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ölülerin çevresinde dönen akbabalar"}],"lexicalization_note":"Tanım, akbabalar ile ölülerin çevresinde dönme ilişkisini birlikte taşıyan söz öbeğiyle sınırlıdır ve yalın bir dönme anlamı kurmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kuşların çevresel uçuşuyla doğrudan örtüşen iki aday seçildi, genel dönme ve yalnız aynı sahneyi paylaşan adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak söz öbeği kuş türünü ve merkezdeki ölüyü zorunlu kılar; komşu anlam farklı canlılara ve farklı merkezlere açık genel bir dolanmadır.","focus_only":"Odak yalnız akbabaları ve onların ölüler çevresindeki dönüşünü belirtir.","gloss":"bir şeyin çevresinde dolanma","neighbor_only":"Komşu dal kuşların su çevresinde ve yabani hayvanların herhangi bir şey çevresinde dolanmasını kapsar.","neighbor_ref":"root_000366/B003","relation_type":"near_neighbor","shared_zone":"Her iki anlamda da canlıların belirli bir merkezin çevresinde dönerek hareket etmesi vardır."},{"boundary_match":"partial","distinction":"Odak dal avcı kuşların ölüler çevresindeki dairesini bildirir; komşu dal ise merkezde ölü bulunmasını gerektirmeyen, havada dönüp durma hareketidir.","focus_only":"Odak akbabalar ile yerdeki ölüler arasındaki çevresel ilişkiyi zorunlu kılar.","gloss":"havada dönüp durma","neighbor_only":"Komşu dal havada dönmeyi bir noktada kalır görünme niteliğiyle ve güneş gibi başka öznelerle de anlatır.","neighbor_ref":"root_000501/B003","relation_type":"near_neighbor","shared_zone":"İki dal kuşun havada dairesel hareketini anlatabildiği ölçüde örtüşür."}],"source_phrase_ar":"المدومة الطواحي النسور تستدير حول القتلى (maqayis;sihah)؛ النسور تستدير حوالي القتلى (ayn)؛ النسور تستدير حوالي القتيل (tahdhib)","source_summary":"Kaynaklar, akbabaların bir veya birden çok ölünün çevresinde dönmesi görüntüsünde birleşir; sayı farkı kavramsal sınırı değiştirmez.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه وصف النسور الطواحي التي تستدير حول القتلى أو القتيل","what_is_not_ar":"لا يدخل فيه مطلق البسط أو الذهاب"},"support_links":["sup_dc7698ab653ef6fd7627"]},{"boundary":"Karşılıklı itişme bir eylemdir; aşağı görülen insanlar ise aynı kanıtta yer alan ayrı bir topluluk nitelemesidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000928/B004","candidate_links":[{"candidate_id":"cand_5f9419eca25aa1dab2f0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طَحَىٰ","morph_features":"STEM|POS:V|PERF|LEM:TaHaY`|ROOT:THw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:6:3:1","qac_word_ref":"91:6:3","surface_ar":"طَحَىٰ"}],"gloss":"karşılıklı itişme ve aşağı görülen insanlar","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluk içindeki kişilerin karşılıklı olarak birbirini itmesini bildirir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı kanıt kümesindeki ayrı bir biçim, aşağı görülen insanları topluluk olarak adlandırır."}}],"root_ar":"ط ح و","root_id":"root_000928","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tek kaynak iddiasındaki eylem ve topluluk nitelemesini eksiltmeden birlikte gösteren açıklayıcı karşılıktır.","boundary_detail":"Karşılıklı itişme bir eylemdir; aşağı görülen insanlar ise aynı kanıtta yer alan ayrı bir topluluk nitelemesidir.","branch_image_ar":"الدَّفْع بين الناس","concept_gloss":"karşılıklı itişme ve aşağı görülen insanlar","contextual_glosses":[{"applicability":"Topluluktaki kişilerin karşılıklı eylemini anlatan söz öbeğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemin karşılıklı oluşunu ve insanların birbirine yönelmesini korur."},"facet_ids":["F001"],"text":"birbirini itmek","usage_role":"contextual"},{"applicability":"Eylemden ayrı olarak insan topluluğunu küçültücü biçimde niteleyen kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluğa yöneltilen olumsuz değer yargısını ve insan gönderimini korur."},"facet_ids":["F002"],"text":"aşağı görülen insanlar","usage_role":"contextual"}],"definition":"Verilen biçimlerde, bir yandan aşağı görülen insanları adlandırır; öte yandan bir topluluktaki kişilerin birbirini itmesini bildiren karşılıklı eylemi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluk içindeki kişilerin karşılıklı olarak birbirini itmesini bildirir."},{"facet_id":"F002","role":"associated_use","statement":"Aynı kanıt kümesindeki ayrı bir biçim, aşağı görülen insanları topluluk olarak adlandırır."}],"identity_rationale":"Kaynak ifadesi yalnız insanların birbirini itmesini değil, ayrıca aşağı görülen insanları bildiren ayrı bir adlandırmayı da içerir. Bu nedenle dal korunabilir, ancak tanım geçici itişme başlığını iki kaynak yüzünü ayıracak biçimde genişletmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"aşağı görülen insanlar"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"birbirlerini itiyorlar"}],"lexicalization_note":"Tanım, topluluk nitelemesini bildiren biçim ile insanların birbirini ittiği söz öbeğini iki ayrı yüz olarak tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; itişme eylemiyle en yakın aday ve topluluk nitelemesiyle karışabilecek aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak eylem yalnız karşılıklı itmeyi bildirir ve ayrı bir topluluk nitelemesi taşır; komşu anlam kalabalıklaşma, sıkışma ve yoğunluk sonuçlarını da kapsar.","focus_only":"Odak dal karşılıklı itişmenin yanında aşağı görülen insanları bildiren ayrı bir biçim de içerir.","gloss":"kalabalıkta itişip sıkışma","neighbor_only":"Komşu dal itişmeyi kalabalık, yol ve çevresinde dönülen yer gibi sıkışık ortamlara ve başka yoğunluk benzetmelerine genişletir.","neighbor_ref":"root_000144/B001","relation_type":"near_synonym","shared_zone":"İki dalda da insanların birbirini itmesi ve topluluk içinde bedensel baskı oluşturması bulunur."},{"boundary_match":"field_only","distinction":"Odak adlandırma olumsuz bir toplumsal niteleme içerir; komşu adlandırma ise insanların çoğunluğunu veya ana kitlesini niceliksel olarak gösterir.","focus_only":"Odak topluluğu aşağılayıcı bir değerle niteler ve ayrıca karşılıklı itme eylemi taşır.","gloss":"insanların büyük kitlesi","neighbor_only":"Komşu dal insanların ana kitlesini veya geniş çoğunluğunu değer yargısı kurmadan bildirir.","neighbor_ref":"root_000266/B013","relation_type":"same_field","shared_zone":"Her iki dal insanları bireyler yerine toplu bir kesim olarak adlandırabilir."}],"source_phrase_ar":"الطحي من الناس الرذال والقوم يطحى بعضهم بعضا أي يدفع (ayn;tahdhib)","source_summary":"Kaynak ifadesi iki bağlı ama özdeş olmayan kullanımı yan yana verir: insanların birbirini itmesi ve aşağı görülen insanları bildiren topluluk adı.","sources":["AY","TA"],"what_is_ar":"يدخل فيه تَطاحي القوم إذا دفع بعضهم بعضا وما ذكر معه من الطحي من الناس الرذال","what_is_not_ar":"لا يدخل فيه بسط الأرض أو دوران النسور"},"support_links":["sup_7d320ee9a06c2ff41d25"]},{"boundary":"Çekirdek çokluk veya büyük hacimdir; tek bir şeyi sırf uzatmak bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000928/B005","candidate_links":[{"candidate_id":"cand_5f9419eca25aa1dab2f0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طَحَىٰ","morph_features":"STEM|POS:V|PERF|LEM:TaHaY`|ROOT:THw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:6:3:1","qac_word_ref":"91:6:3","surface_ar":"طَحَىٰ"}],"gloss":"çokluk ve iri büyüklük","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun sayıca çok veya bütünüyle büyük olmasını bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ordunun geniş uçlara yayılmış, büyük ve kalabalık oluşunu niteler."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir evin hacimce büyük, iri ve görkemli oluşuna uygulanır."}}],"root_ar":"ط ح و","root_id":"root_000928","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Topluluğun niceliğini ve ordu ya da evin geniş, hacimli büyüklüğünü birlikte karşılar.","boundary_detail":"Çekirdek çokluk veya büyük hacimdir; tek bir şeyi sırf uzatmak bu dala girmez.","branch_image_ar":"الكثرة والضخامة","concept_gloss":"çokluk ve iri büyüklük","contextual_glosses":[{"applicability":"İnsanlardan veya benzeri üyelerden oluşan kalabalık bir bütün nitelendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluğun sayıca çok ve bütün olarak büyük oluşunu korur."},"facet_ids":["F001"],"text":"çok ve büyük topluluk","usage_role":"contextual"},{"applicability":"Ordunun hem kalabalığını hem de alana genişçe yayılmasını anlatan söz öbeği içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ordunun büyüklüğünü ve geniş uçlara yayılan düzenini korur."},"facet_ids":["F002"],"text":"uçları geniş büyük ordu","usage_role":"contextual"},{"applicability":"Bir yapının hacimli ve büyük oluşunu bildiren adlandırma için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Evin hacimsel iriliğini ve belirgin büyüklüğünü korur."},"facet_ids":["F003"],"text":"iri ve büyük ev","usage_role":"contextual"}],"definition":"Bir topluluğun sayıca çok veya büyük olmasıdır; bu nitelik geniş uçlara yayılan büyük bir orduya ve hacimli, iri bir eve de uygulanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun sayıca çok veya bütünüyle büyük olmasını bildirir."},{"facet_id":"F002","role":"specialization","statement":"Ordunun geniş uçlara yayılmış, büyük ve kalabalık oluşunu niteler."},{"facet_id":"F003","role":"extension","statement":"Bir evin hacimce büyük, iri ve görkemli oluşuna uygulanır."}],"identity_rationale":"Kaynak ifadesi çok veya büyük bir topluluğu, geniş uçlara yayılan büyük bir orduyu ve iri bir evi aynı çokluk ve hacim ekseninde verir. Dal çerçevesi bu örnekleri tek bir nesneye yapılan yalın uzatma eylemine indirgemeden doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"çok ve büyük topluluk"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"uçları geniş büyük ordu"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"iri ve büyük ev"}],"lexicalization_note":"Tanım genel topluluk nitelemesini, ordu söz öbeğini ve büyük ev adlandırmasını ayrı gerçekleşmeler olarak gösterir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel büyüklük, ordu büyüklüğü ve insan çokluğu sınırlarını ayrı ayrı gösteren üç aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu anlam genel bir büyük ve çok karşıtlığı kurar; odak dal ise topluluk niceliğiyle ordu ve evin belirli büyük oluş biçimlerine bağlıdır.","focus_only":"Odak kullanım topluluk, geniş ordu ve iri ev gibi belirli gerçekleşmelerle sınırlıdır.","gloss":"büyüklük ve çokluk","neighbor_only":"Komşu dal büyüklük ve çokluğu nesneler, hayvanlar ve bağışlar gibi daha geniş bir alana uygular.","neighbor_ref":"root_000255/B002","relation_type":"near_synonym","shared_zone":"İki anlam da bir varlığın veya topluluğun küçük ya da az olmamasını bildirir."},{"boundary_match":"partial","distinction":"Odak dalın ev ve geniş yayılımlı ordu uygulamaları vardır; komşu dal ise aynı nicelik alanını iri veya çok develere doğru genişletir.","focus_only":"Odak dal büyük bir evi ve geniş uçlara yayılan orduyu ayrıca kapsar.","gloss":"çok ve iri topluluk","neighbor_only":"Komşu dal büyük veya çok ordunun yanı sıra iri ya da çok sayıdaki develeri de adlandırır.","neighbor_ref":"root_000235/B012","relation_type":"near_neighbor","shared_zone":"Her ikisi de bir ordunun veya topluluğun çokluğunu ve büyüklüğünü anlatabilir."}],"source_phrase_ar":"الطاحي الجمع الكثير (maqayis)؛ عسكر طاحي الضفاف عرمرم (sihah)؛ الطاحي الجمع العظيم والبيت العظيم مظلة مطحوة ومطحية وطاحية وهو الضخم (tahdhib)","source_summary":"Kaynaklar toplulukta çokluk ve büyüklük çekirdeğini paylaşır; ordu örneği geniş yayılımı, ev örneği ise hacimsel iriliği somutlaştırır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الجمع الكثير أو العظيم والعسكر الواسع الأطراف والبيت العظيم الضخم","what_is_not_ar":"لا يدخل فيه مجرد المد في الشيء المفرد ولا الدفع بين الناس"},"support_links":["sup_7d320ee9a06c2ff41d25"]},{"boundary":"Buradaki yayılma, genel bir yüzeyi genişletmek değil, canlı veya bitkinin yere serilip temas etmesidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000928/B006","candidate_links":[{"candidate_id":"cand_31f9bd79256e03ceceba","lane":"micro"},{"candidate_id":"cand_dd8cb7695208438214a6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طَحَىٰ","morph_features":"STEM|POS:V|PERF|LEM:TaHaY`|ROOT:THw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:6:3:1","qac_word_ref":"91:6:3","surface_ar":"طَحَىٰ"}],"gloss":"yere serilip yapışma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Canlının yere uzanması, yüzükoyun yatması veya zemine yapışmasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir darbenin ardından bedenin yere serilip boylu boyunca uzanmasıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Devenin açlık veya zayıflık yüzünden yere yapışacak biçimde çökmesidir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir bitkinin toprağın yüzüne yatay biçimde yayılıp zemini örtmesidir."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Birini yere devirmek ve devrilen kişinin yüzükoyun serilmesi biçimindeki katılımcı değişimini kapsar."}}],"root_ar":"ط ح و","root_id":"root_000928","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Canlıdaki uzanma ve çökme ile bitkideki zemine yayılma sonucunu ortak biçimde temsil eder.","boundary_detail":"Buradaki yayılma, genel bir yüzeyi genişletmek değil, canlı veya bitkinin yere serilip temas etmesidir.","branch_image_ar":"الانبطاح واللُّصوق بالأرض","concept_gloss":"yere serilip yapışma","contextual_glosses":[{"applicability":"Canlının kendi durumunu bildirerek yere serilip yattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Canlının yere uzanmasını ve yüzükoyun temas durumunu korur."},"facet_ids":["F001"],"text":"yere uzanıp yüzükoyun yatmak","usage_role":"contextual"},{"applicability":"Darbe sonucunda bedenin yerde uzanmış duruma gelmesini anlatan kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Darbeyi neden, yere serilmeyi sonuç olarak eksiksiz korur."},"facet_ids":["F002"],"text":"darbeyle yere serilmek","usage_role":"contextual"},{"applicability":"Bitkinin dik yükselmek yerine zemini örterek yatay büyüdüğü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bitkinin toprağa yatay biçimde yayılıp yüzeyi örtmesini korur."},"facet_ids":["F004"],"text":"toprağın yüzüne yayılmak","usage_role":"contextual"},{"applicability":"Bir kişinin başkasını devirdiği ve onun yere serildiği ettirgen kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eyleyenin devirmesini ve etkilenenin yere serilmesi sonucunu birlikte korur."},"facet_ids":["F005"],"text":"yere devirip sermek","usage_role":"contextual"}],"definition":"Bir canlının kendiliğinden, zayıflıkla, darbeyle veya devriltilerek yere serilip uzanması ve zemine yapışmasıdır; bitkide ise toprağın yüzüne yayılarak onu örtme biçiminde gerçekleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Canlının yere uzanması, yüzükoyun yatması veya zemine yapışmasıdır."},{"facet_id":"F002","role":"specialization","statement":"Bir darbenin ardından bedenin yere serilip boylu boyunca uzanmasıdır."},{"facet_id":"F003","role":"specialization","statement":"Devenin açlık veya zayıflık yüzünden yere yapışacak biçimde çökmesidir."},{"facet_id":"F004","role":"extension","statement":"Bir bitkinin toprağın yüzüne yatay biçimde yayılıp zemini örtmesidir."},{"facet_id":"F005","role":"associated_use","statement":"Birini yere devirmek ve devrilen kişinin yüzükoyun serilmesi biçimindeki katılımcı değişimini kapsar."}],"identity_rationale":"Kaynak ifadesi uzanma, yüzükoyun yere yapışma, darbe sonucu yere serilme, devenin yere çökmesi ve bitkinin zemini kaplaması örneklerini ortak bir yere yayılıp temas etme sonucunda birleştirir. Dal çerçevesi bu katılımcı ve neden ayrımlarını korur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yere uzandım"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bir darbeyle yere serildi"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yere yapışmış veya yüzükoyun yatmış"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"toprağın yüzüne yayılan bitki"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"deve açlıktan veya zayıflıktan yere çöktü"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"onu yere devirdim, o da yüzükoyun serildi"}],"lexicalization_note":"Tanım yalın uzanmayı, darbe sonucu ve ettirgen yere sermeyi, deve söz öbeğini ve yere yayılan bitki nitelemesini ayrı yüzler halinde korur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bedenin yere yayılması, boylu boyunca yatması ve yan yatmasıyla karışabilecek üç aday sınır karşılaştırmasına alındı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu anlam insanın darbe veya düşüş sonucu gevşemesine bağlıdır; odak anlam neden, canlı türü ve bitki uygulaması bakımından daha geniştir.","focus_only":"Odak dal kendiliğinden uzanmayı, devenin çökmesini, bitkinin yayılmasını ve ettirgen devirmeyi de kapsar.","gloss":"düşüp yere yayılma","neighbor_only":"Komşu dal özellikle darbe veya düşüş sonucu insan bedeninin gevşeyip yerde uzanmasını bildirir.","neighbor_ref":"root_000668/B002","relation_type":"near_synonym","shared_zone":"İki dal da darbe alan kişinin bedeninin yerde uzanmış ve yayılmış duruma gelmesini anlatır."},{"boundary_match":"partial","distinction":"Odak anlamın duruşu çoğu kez yüzükoyun ve zemine yapışıktır; komşu anlam sırtüstü duruşu ve güçsüzlük koşulunu belirginleştirir.","focus_only":"Odak yüzükoyun yapışmayı, deve ve bitki kullanımlarını ve devrilme sonucunu içerir.","gloss":"yerde boylu boyunca yatma","neighbor_only":"Komşu anlam sırtüstü uzanmayı, güçsüzlük veya süreğen rahatsızlık koşulunu ve özel bir adlandırmayı kapsar.","neighbor_ref":"root_000703/B002","relation_type":"near_synonym","shared_zone":"Her iki dal insan bedeninin yerde boylu boyunca uzanmış olmasını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal yerde uzanma ve yapışma sonucunu öne çıkarır; komşu dal yan tarafın yere gelmesini zorunlu bir duruş özelliği yapar.","focus_only":"Odak yüzükoyun serilme, darbe, deve ve bitki gibi farklı gerçekleşmelere açıktır.","gloss":"yanını yere vererek yatma","neighbor_only":"Komşu anlam özellikle yan tarafın yere gelmesini ve yan yatma ya da uyuma durumunu bildirir.","neighbor_ref":"root_000902/B001","relation_type":"near_neighbor","shared_zone":"İki anlam da bedenin dik duruştan çıkarak yere temas edip yatmasını anlatır."}],"source_phrase_ar":"طحيت اضطجعت (maqayis;sihah)؛ ضربه ضربة طحا منها أي امتد (sihah)؛ فتدحى أي اضطجع في سعة من الأرض والمطحي اللازق بالأرض متبطحا والبقلة المطحية النابتة على وجه الأرض قد افترشتها وطحى البعير إلى الأرض أي لزق بها (tahdhib)","source_summary":"Kaynaklar yere uzanma çekirdeğini paylaşır; darbe sonucu serilme, zemine yapışan deve, yere yayılan bitki ve birini devirme bu çekirdeğin neden ve katılımcı bakımından ayrılan gerçekleşmeleridir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الاضطجاع والانبطاح واللصوق بالأرض وامتداد المضروب أو البعير على الأرض وافتراش البقلة لوجه الأرض","what_is_not_ar":"لا يدخل فيه بسط الأرض على العموم أو الذهاب البعيد"},"support_links":["sup_05e42556c0e123b69aed","sup_b5b4b47a9990a0cc8a04"]},{"boundary":"Anlam yalnız verilen yok olma ifadesine dayanır; biçimsel kapsam veya başka ölüm sözleri buraya taşınamaz.","branch_kind":"unresolved","branch_ref":"root_000928/B007","candidate_links":[{"candidate_id":"cand_dd8cb7695208438214a6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طَحَىٰ","morph_features":"STEM|POS:V|PERF|LEM:TaHaY`|ROOT:THw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:6:3:1","qac_word_ref":"91:6:3","surface_ar":"طَحَىٰ"}],"gloss":"yok olup yaşamını yitirme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Öznenin yok olması veya yaşamını yitirmesi anlamını bildirir."}}],"root_ar":"ط ح و","root_id":"root_000928","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Biçimsel kapsamı belirsiz tek kanıttaki yok olma sonucunu ihtiyatla temsil eder.","boundary_detail":"Anlam yalnız verilen yok olma ifadesine dayanır; biçimsel kapsam veya başka ölüm sözleri buraya taşınamaz.","branch_image_ar":"الهلاك","concept_gloss":"yok olup yaşamını yitirme","contextual_glosses":[{"applicability":"Tek kanıttaki sonuç anlamını biçim türü hakkında ek varsayım kurmadan açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yok olma ile yaşamın sona ermesi anlamını birlikte korur."},"facet_ids":["F001"],"text":"yok olup yaşamını yitirmek","usage_role":"explanatory"}],"definition":"Verilen tek ifadede öznenin yok olması veya yaşamını yitirmesidir; kullanımın biçimsel kapsamı belirlenmemiştir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Öznenin yok olması veya yaşamını yitirmesi anlamını bildirir."}],"identity_rationale":"Kaynak ifadesi öznenin yok olması ya da ölmesi anlamını doğrudan verir, ancak hiçbir sözlük birimi ve biçim türü sağlanmadığı için bunun yalın kökün üretken bir anlamı olduğu varsayılamaz. Dal anlamca korunmalı, sözlüksel kapsamı ise çözümlenmemiş bırakılmalıdır.","lexicalization_note":"Sözlüksel birim bulunmadığından tanım kanıtlanan yok olma anlamını verir, fakat bunu yalın ya da kalıplaşmış kullanım diye sınıflandırmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; çözümlenmemiş kapsamı gereksiz yere genişletmemek için yalnız en açıklayıcı geniş yok olma dalı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dar ve biçimsel kapsamı belirsiz bir yok olma tanıklığıdır; komşu dal hem kendiliğinden yok olmayı hem de yok etmeyi ve cezayı kapsayan geniş bir alandır.","focus_only":"Odak dal yalnız öznenin yok olması veya yaşamını yitirmesi sonucunu kanıtlar.","gloss":"yok olma ve tükenme","neighbor_only":"Komşu dal bozulma, tükenme, öldürme, ceza ve geçişli yok etme gibi daha geniş sonuç ve nedenleri kapsar.","neighbor_ref":"root_001596/B001","relation_type":"near_synonym","shared_zone":"İki dal bir varlığın varlığını veya yaşamını yitirerek sona ermesi alanında örtüşür."}],"source_phrase_ar":"طحا إذا هلك (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu yok olma anlamı tek kaynaklı bir tanıklık olarak verilmiştir ve ayrıca sözlüksel birim kaydıyla desteklenmemiştir."}],"source_summary":"Kanıt, anlamı öznenin yok olması veya yaşamını yitirmesiyle sınırlar; daha geniş bir kullanım alanı göstermez.","sources":["TA"],"what_is_ar":"يدخل فيه قول طحا إذا هلك كما انفرد به تهذيب اللغة","what_is_not_ar":"لا يدخل فيه الطائح الهالك إلا من جهة المجاورة اللفظية"},"support_links":["sup_b5b4b47a9990a0cc8a04"]},{"boundary":"Yükselmiş olma yalnız ay nitelemesine bağlıdır; aynı niteleyicinin yayılmış anlamı bu dala katılmaz.","branch_kind":"collocation","branch_ref":"root_000928/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَحَىٰ","morph_features":"STEM|POS:V|PERF|LEM:TaHaY`|ROOT:THw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:6:3:1","qac_word_ref":"91:6:3","surface_ar":"طَحَىٰ"}],"gloss":"gökte yükselmiş ay","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli söz öbeğinde ayın gökte yükselmiş durumda oluşunu bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı niteleyicinin yayılmış anlamı ayrı bir kullanımdır ve yükselmiş ay okumasının sınırını gösterir."}}],"root_ar":"ط ح و","root_id":"root_000928","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız ayı yükselmiş olarak niteleyen söz öbeğinin tam kavramsal karşılığıdır.","boundary_detail":"Yükselmiş olma yalnız ay nitelemesine bağlıdır; aynı niteleyicinin yayılmış anlamı bu dala katılmaz.","branch_image_ar":"الارتفاع","concept_gloss":"gökte yükselmiş ay","contextual_glosses":[{"applicability":"Ayın yüksek konumunu akıcı bir niteleme olarak aktaran cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ayın gökte yüksek bir konumda oluşunu doğal bir nitelemeyle korur."},"facet_ids":["F001"],"text":"gökte yüksek konumdaki ay","usage_role":"contextual"}],"definition":"Ayı gökte yükselmiş olarak niteleyen belirli söz öbeğine özgü anlamdır; aynı niteleyicinin yayılmış anlamındaki ayrı kullanımı bu dala girmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli söz öbeğinde ayın gökte yükselmiş durumda oluşunu bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı niteleyicinin yayılmış anlamı ayrı bir kullanımdır ve yükselmiş ay okumasının sınırını gösterir."}],"identity_rationale":"Kaynak ifadesi yükselme anlamını yalnız ayı niteleyen belirli söz öbeğinde verir ve aynı niteleyicinin başka yerde yayılmış anlamına da gelebileceğini açıkça belirtir. Dal korunabilir, ancak yükselme yalın bir kök anlamı değil, bu söz öbeğine bağlı bir okuma olarak tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"gökte yükselmiş ay"}],"lexicalization_note":"Tanım yalnız ayı yükselmiş olarak niteleyen söz öbeğini kapsar ve niteleyiciyi genel bir yükselme anlamına genişletmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; söz öbeğine bağlı ay nitelemesiyle genel yükselme arasındaki kapsam farkını en açık gösteren aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ay nitelemesine bağlı durağan bir yüksek konum okumasıdır; komşu dal ise çok çeşitli öznelerdeki genel yükselme ve yükseltme alanını kapsar.","focus_only":"Odak anlam yalnız ayı niteleyen belirli söz öbeğinde gerçekleşir.","gloss":"genel yükselme","neighbor_only":"Komşu dal yer, beden, gün ve gökyüzü gibi çok farklı öznelerde genel yükselme hareketini kapsar.","neighbor_ref":"root_001042/B001","relation_type":"near_synonym","shared_zone":"İki dal bir varlığın aşağıya göre daha yüksek konuma gelmesini veya orada bulunmasını anlatır."}],"source_phrase_ar":"القمر الطاحي أي المرتفع والطاحي أيضا المنبسط (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Ayın yükselmiş oluşunu bildiren söz öbeği tek kaynaklıdır ve aynı niteleyicinin yayılmış anlamından açıkça ayrılır."}],"source_summary":"Kanıt, ay nitelemesinde yükselmiş olma anlamını verirken aynı biçimin yayılmış anlamındaki kullanımını karşıt sınır olarak belirtir.","sources":["TA"],"what_is_ar":"يدخل فيه وصف القمر الطاحي بمعنى المرتفع","what_is_not_ar":"لا يدخل فيه الطاحي بمعنى المنبسط"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["91:6:1"],"branch_refs":[],"candidate_id":"cand_a1a65e9aa1fea10681ac","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:1:fused-earth-opening","source_type":"word_analysis","support_ids":["sup_41882eaee2e57384f5fb","sup_970c920acb6f6c29531a"],"title":"particle fused to earth noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:1","qac_refs":["91:6:1:1"],"status":"accepted"}},{"anchor_refs":["91:6:1"],"branch_refs":[],"candidate_id":"cand_a454e2d9e524d15dbd2b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:1:oath-renewal","source_type":"word_analysis","support_ids":["sup_970c920acb6f6c29531a","sup_f3024c7b7f78a27affde"],"title":"fresh oath item in the chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:1","qac_refs":["91:6:1:1"],"status":"accepted"}},{"anchor_refs":["91:6:1"],"branch_refs":[],"candidate_id":"cand_6df10dcf722a01446f9e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:1:paired-wa-refrain","source_type":"word_analysis","support_ids":["sup_970c920acb6f6c29531a","sup_ce5577807455ec54fa6c"],"title":"outer and inner connectors","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:1","qac_refs":["91:6:1:1"],"status":"accepted"}},{"anchor_refs":["91:6:2"],"branch_refs":[],"candidate_id":"cand_17606ef36bc99fa406c9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:2:common-word-marked-place","source_type":"word_analysis","support_ids":["sup_0c199394de5e926f9d4c","sup_81257533478ff2dc89bc"],"title":"common word made marked","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:2","qac_refs":["91:6:1:2","91:6:1:3"],"status":"accepted"}},{"anchor_refs":["91:6:2"],"branch_refs":[],"candidate_id":"cand_1e7718f09becd20679c3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:2:definite-singular-earth","source_type":"word_analysis","support_ids":["sup_0c199394de5e926f9d4c","sup_4b3c8499b60354334158"],"title":"known singular earth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:2","qac_refs":["91:6:1:2","91:6:1:3"],"status":"accepted"}},{"anchor_refs":["91:6:2"],"branch_refs":[],"candidate_id":"cand_25d0ea5a2988555dddcc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:2:earth-oath-echo","source_type":"word_analysis","support_ids":["sup_0c199394de5e926f9d4c","sup_a521c7c8d92b35e86547"],"title":"earth oath by defining feature","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:2","qac_refs":["91:6:1:2","91:6:1:3"],"status":"accepted"}},{"anchor_refs":["91:6:2"],"branch_refs":[],"candidate_id":"cand_3cf6cba090aed02eedb4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:2:earth-sound-weight","source_type":"word_analysis","support_ids":["sup_0c199394de5e926f9d4c","sup_40b64f7f646f27ce4849"],"title":"dense ground-name sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:2","qac_refs":["91:6:1:2","91:6:1:3"],"status":"accepted"}},{"anchor_refs":["91:6:2"],"branch_refs":[],"candidate_id":"cand_17df9857420473b70f20","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:2:feminine-antecedent","source_type":"word_analysis","support_ids":["sup_0c199394de5e926f9d4c","sup_339d08d80f91aac39cca"],"title":"antecedent for the final suffix","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:2","qac_refs":["91:6:1:2","91:6:1:3"],"status":"accepted"}},{"anchor_refs":["91:6:2"],"branch_refs":[],"candidate_id":"cand_2f76d41e233a3f37ce8e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:2:oath-case","source_type":"word_analysis","support_ids":["sup_0c199394de5e926f9d4c","sup_92d25e71e35fe9f3ff4b"],"title":"genitive oath object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:2","qac_refs":["91:6:1:2","91:6:1:3"],"status":"accepted"}},{"anchor_refs":["91:6:2"],"branch_refs":[],"candidate_id":"cand_187f25468e03a4184cec","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:2:object-qualifier-architecture","source_type":"word_analysis","support_ids":["sup_0c199394de5e926f9d4c","sup_879d7d489c20a2411d14"],"title":"object before qualifier","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:2","qac_refs":["91:6:1:2","91:6:1:3"],"status":"accepted"}},{"anchor_refs":["91:6:2"],"branch_refs":[],"candidate_id":"cand_83cae8142b269962c4cd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:2:sky-earth-axis","source_type":"word_analysis","support_ids":["sup_0c199394de5e926f9d4c","sup_c77bfe7b889408363c08"],"title":"sky-to-earth axis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:2","qac_refs":["91:6:1:2","91:6:1:3"],"status":"accepted"}},{"anchor_refs":["91:6:2"],"branch_refs":[],"candidate_id":"cand_11aa0d96ef2036a7d1b9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:2:terrestrial-surface-range","source_type":"word_analysis","support_ids":["sup_0c199394de5e926f9d4c","sup_74aecbc3f7b364a5f8d5"],"title":"earth as spreadable surface","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:2","qac_refs":["91:6:1:2","91:6:1:3"],"status":"accepted"}},{"anchor_refs":["91:6:3"],"branch_refs":[],"candidate_id":"cand_03a218b9b0d02f58af53","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:3:internal-clause-hinge","source_type":"word_analysis","support_ids":["sup_16549fcb38958cdc9aa3","sup_4c3df6800a9f9eabb96e"],"title":"hinge into the spreading clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:3","qac_refs":["91:6:2:1"],"status":"accepted"}},{"anchor_refs":["91:6:3"],"branch_refs":[],"candidate_id":"cand_9cfb4cd35fc6559d11f3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:3:open-vowel-entry","source_type":"word_analysis","support_ids":["sup_4c3df6800a9f9eabb96e","sup_cb7eceffa0210f34e0f5"],"title":"open-vowel entry to the qualifier","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:3","qac_refs":["91:6:2:1"],"status":"accepted"}},{"anchor_refs":["91:6:3"],"branch_refs":[],"candidate_id":"cand_274de1ae62ae5f74f3e5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:3:same-form-different-force","source_type":"word_analysis","support_ids":["sup_4c3df6800a9f9eabb96e","sup_bb119636414c4ca805da"],"title":"same particle, different environment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:3","qac_refs":["91:6:2:1"],"status":"accepted"}},{"anchor_refs":["91:6:3"],"branch_refs":[],"candidate_id":"cand_8ec803e29cec928e230b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:3:wa-ma-template","source_type":"word_analysis","support_ids":["sup_3c4c6808fa84889bb6ee","sup_4c3df6800a9f9eabb96e"],"title":"repeated {{ar:وَمَا}} ({{tr:wa-ma}}) template","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:3","qac_refs":["91:6:2:1"],"status":"accepted"}},{"anchor_refs":["91:6:4"],"branch_refs":[],"candidate_id":"cand_11b68eaebeb418b71487","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:4:compact-dependent-clause","source_type":"word_analysis","support_ids":["sup_1dd15e7d5b6fadad4ccb","sup_3df84fb207c05f37133c"],"title":"compressed qualifier","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:4","qac_refs":["91:6:2:2"],"status":"accepted"}},{"anchor_refs":["91:6:4"],"branch_refs":[],"candidate_id":"cand_f9172b8d1df24ec55f2e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:4:neighboring-ma-pattern","source_type":"word_analysis","support_ids":["sup_3df84fb207c05f37133c","sup_c1d1b7f7936482f7da2a"],"title":"repeated {{ar:مَا}} ({{tr:ma}})-verb pattern","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:4","qac_refs":["91:6:2:2"],"status":"accepted"}},{"anchor_refs":["91:6:4"],"branch_refs":[],"candidate_id":"cand_73b739909cc572e3806d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:4:relative-or-masdariyya","source_type":"word_analysis","support_ids":["sup_3df84fb207c05f37133c","sup_9e160de5840e6f60c2f3"],"title":"agent/process ambiguity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:4","qac_refs":["91:6:2:2"],"status":"accepted"}},{"anchor_refs":["91:6:4"],"branch_refs":[],"candidate_id":"cand_a6a7154bbe79c352fc40","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:4:sound-suspension","source_type":"word_analysis","support_ids":["sup_3b3c12d2bbc087891a60","sup_3df84fb207c05f37133c"],"title":"suspended open syllable","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:4","qac_refs":["91:6:2:2"],"status":"accepted"}},{"anchor_refs":["91:6:4"],"branch_refs":[],"candidate_id":"cand_fa0dbbc5516c466b4028","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:6:4:unnamed-agent","source_type":"word_analysis","support_ids":["sup_2b8c3657c54191aed6df","sup_3df84fb207c05f37133c"],"title":"agent veiled through act","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:4","qac_refs":["91:6:2:2"],"status":"accepted"}},{"anchor_refs":["91:6:5"],"branch_refs":[],"candidate_id":"cand_4d0c98d7324851712a0d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000928"],"scope":"focus_ayah","source_local_id":"91:6:5:active-agent-slot","source_type":"word_analysis","support_ids":["sup_11582ee37b1587d9649a","sup_c45d650fa2b828d9f97a"],"title":"agent slot kept open","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:5","qac_refs":["91:6:3:1","91:6:3:2"],"status":"accepted"}},{"anchor_refs":["91:6:5"],"branch_refs":[],"candidate_id":"cand_38d92442dbacf6c7e14e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000928"],"scope":"focus_ayah","source_local_id":"91:6:5:cadence-and-articulation","source_type":"word_analysis","support_ids":["sup_c45d650fa2b828d9f97a","sup_e1d623631240fd012338"],"title":"pressure releasing into expanse","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:5","qac_refs":["91:6:3:1","91:6:3:2"],"status":"accepted"}},{"anchor_refs":["91:6:5"],"branch_refs":[],"candidate_id":"cand_6342ef14fc56978c6dc8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000928"],"scope":"focus_ayah","source_local_id":"91:6:5:completed-form-i-action","source_type":"word_analysis","support_ids":["sup_244ce8528fad595c2daa","sup_c45d650fa2b828d9f97a"],"title":"completed direct spreading","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:5","qac_refs":["91:6:3:1","91:6:3:2"],"status":"accepted"}},{"anchor_refs":["91:6:5"],"branch_refs":[],"candidate_id":"cand_be706b0254ac945c29a9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000928"],"scope":"focus_ayah","source_local_id":"91:6:5:creation-oath-architecture","source_type":"word_analysis","support_ids":["sup_326315d21cb815600f34","sup_c45d650fa2b828d9f97a"],"title":"horizontal counterpart in the oath series","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:5","qac_refs":["91:6:3:1","91:6:3:2"],"status":"accepted"}},{"anchor_refs":["91:6:5"],"branch_refs":[],"candidate_id":"cand_7e5a9e23ba4cbce3e72d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000928"],"scope":"focus_ayah","source_local_id":"91:6:5:hapax-concentration","source_type":"word_analysis","support_ids":["sup_c45d650fa2b828d9f97a","sup_e73431be7cd40cf08dfb"],"title":"locally concentrated hapax","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:5","qac_refs":["91:6:3:1","91:6:3:2"],"status":"accepted"}},{"anchor_refs":["91:6:5"],"branch_refs":[],"candidate_id":"cand_64774141c321ccf75f24","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000928"],"scope":"focus_ayah","source_local_id":"91:6:5:leveling-pressure-color","source_type":"word_analysis","support_ids":["sup_389a5d050bfecda43c1f","sup_c45d650fa2b828d9f97a"],"title":"tactile leveling and pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:5","qac_refs":["91:6:3:1","91:6:3:2"],"status":"accepted"}},{"anchor_refs":["91:6:5"],"branch_refs":[],"candidate_id":"cand_cab743c7fbf62e75cbc1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000928"],"scope":"focus_ayah","source_local_id":"91:6:5:modern-geology-limit","source_type":"word_analysis","support_ids":["sup_c45d650fa2b828d9f97a","sup_f40475d425f5d00c3e3f"],"title":"concrete extension without science claim","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:5","qac_refs":["91:6:3:1","91:6:3:2"],"status":"accepted"}},{"anchor_refs":["91:6:5"],"branch_refs":[],"candidate_id":"cand_d22503973dc53480eedb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000928"],"scope":"focus_ayah","source_local_id":"91:6:5:near-root-daḥā-contrast","source_type":"word_analysis","support_ids":["sup_334eadaf3daad00b6ea5","sup_c45d650fa2b828d9f97a"],"title":"near-root contrast with 79:30","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:5","qac_refs":["91:6:3:1","91:6:3:2"],"status":"accepted"}},{"anchor_refs":["91:6:5"],"branch_refs":[],"candidate_id":"cand_732909a0704086f83d36","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000928"],"scope":"focus_ayah","source_local_id":"91:6:5:object-agent-doublet","source_type":"word_analysis","support_ids":["sup_c45d650fa2b828d9f97a","sup_c9bafdd17e37a2fee641"],"title":"object plus spreader/process doublet","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:5","qac_refs":["91:6:3:1","91:6:3:2"],"status":"accepted"}},{"anchor_refs":["91:6:5"],"branch_refs":[],"candidate_id":"cand_dac847cc5791a661094f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000928"],"scope":"focus_ayah","source_local_id":"91:6:5:spread-extend-branch","source_type":"word_analysis","support_ids":["sup_9ebe0f7fd32bed9406d4","sup_c45d650fa2b828d9f97a"],"title":"spreading and extending branch","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:5","qac_refs":["91:6:3:1","91:6:3:2"],"status":"accepted"}},{"anchor_refs":["91:6:5"],"branch_refs":[],"candidate_id":"cand_a381dce9bca062199929","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000928"],"scope":"focus_ayah","source_local_id":"91:6:5:transitive-pronoun-binding","source_type":"word_analysis","support_ids":["sup_c45d650fa2b828d9f97a","sup_e4c8ebe113fb1688e1be"],"title":"earth bound as object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:5","qac_refs":["91:6:3:1","91:6:3:2"],"status":"accepted"}},{"anchor_refs":["91:6:5"],"branch_refs":[],"candidate_id":"cand_c5e9a5d256cc590b35b0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000928"],"scope":"focus_ayah","source_local_id":"91:6:5:weak-final-surface","source_type":"word_analysis","support_ids":["sup_81fab1fde1a1c333c6f8","sup_c45d650fa2b828d9f97a"],"title":"weak-final morphology visible in closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:6:5","qac_refs":["91:6:3:1","91:6:3:2"],"status":"accepted"}},{"anchor_refs":["91:6:1"],"branch_refs":[],"candidate_id":"cand_ebd0e6341383f1119147","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000025"],"scope":"focus_ayah","source_local_id":"91:6:1:3","source_type":"qac_morpheme","support_ids":["sup_3520c76ee81f3ff53162"],"title":"QAC root occurrence: ء ر ض","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:6:3"],"branch_refs":[],"candidate_id":"cand_c7001da72596752e60f3","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000928"],"scope":"focus_ayah","source_local_id":"91:6:3:1","source_type":"qac_morpheme","support_ids":["sup_d8f29fa48b79a5b7d8a5"],"title":"QAC root occurrence: ط ح و","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:6","branch_refs":["root_000025/B001","root_000928/B001"],"candidate_id":"cand_30f6aab9261096309a4b","commentary_obligation":"review","hft_ref":"hft_a3515054047dd33ca379","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b01_lower_expanse","source_type":"hft","support_ids":["sup_a2207e2ecbd8cd86ac7a"],"title":"b01_lower_expanse","trust":"legacy_unbound"},{"anchor_refs":["91:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:6","branch_refs":["root_000025/B002","root_000025/B005","root_000928/B001","root_000928/B006"],"candidate_id":"cand_31f9bd79256e03ceceba","commentary_obligation":"review","hft_ref":"hft_d5a111d9d75152b6a231","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b02_fertile_receptive_mat","source_type":"hft","support_ids":["sup_05e42556c0e123b69aed"],"title":"b02_fertile_receptive_mat","trust":"legacy_unbound"},{"anchor_refs":["91:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:6","branch_refs":["root_000025/B006","root_000928/B002","root_000928/B003"],"candidate_id":"cand_c7682506b05f0e13906c","commentary_obligation":"review","hft_ref":"hft_28fb03187889ad8f69e4","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b03_grounded_motion_field","source_type":"hft","support_ids":["sup_dc7698ab653ef6fd7627"],"title":"b03_grounded_motion_field","trust":"legacy_unbound"},{"anchor_refs":["91:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:6","branch_refs":["root_000025/B007","root_000928/B004","root_000928/B005"],"candidate_id":"cand_5f9419eca25aa1dab2f0","commentary_obligation":"review","hft_ref":"hft_e37f395a6ba0b8118251","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b04_social_pressure_arena","source_type":"hft","support_ids":["sup_7d320ee9a06c2ff41d25"],"title":"b04_social_pressure_arena","trust":"legacy_unbound"},{"anchor_refs":["91:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:6","branch_refs":["root_000025/B001","root_000928/B006","root_000928/B007"],"candidate_id":"cand_dd8cb7695208438214a6","commentary_obligation":"review","hft_ref":"hft_4296796a7ecb564ec1a7","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b05_reversible_flattening","source_type":"hft","support_ids":["sup_b5b4b47a9990a0cc8a04"],"title":"b05_reversible_flattening","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَٱلْأَرْضِ وَمَا طَحَىٰهَا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:6:1:1","qac_word_ref":"91:6:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"91:6:1:2","qac_word_ref":"91:6:1","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:6:1:3","qac_word_ref":"91:6:1","root_ar":"ء ر ض","surface_ar":"أَرْضِ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:6:2:1","qac_word_ref":"91:6:2","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:REL|LEM:maA","morpheme_role":"STEM","pos":"REL","qac_ref":"91:6:2:2","qac_word_ref":"91:6:2","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"طَحَىٰ","morph_features":"STEM|POS:V|PERF|LEM:TaHaY`|ROOT:THw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:6:3:1","qac_word_ref":"91:6:3","root_ar":"ط ح و","surface_ar":"طَحَىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:6:3:2","qac_word_ref":"91:6:3","root_ar":"","surface_ar":"هَا"}],"word_analysis_qac_refs":[["91:6:1:1"],["91:6:1:2","91:6:1:3"],["91:6:2:1"],["91:6:2:2"],["91:6:3:1","91:6:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["91:6:1","91:6:2","91:6:3","91:6:4","91:6:5"]},"focus_surface_evidence":{"arabic_uthmani":"وَٱلْأَرْضِ وَمَا طَحَىٰهَا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:6:1:1","qac_word_ref":"91:6:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"91:6:1:2","qac_word_ref":"91:6:1","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:6:1:3","qac_word_ref":"91:6:1","root_ar":"ء ر ض","surface_ar":"أَرْضِ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:6:2:1","qac_word_ref":"91:6:2","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:REL|LEM:maA","morpheme_role":"STEM","pos":"REL","qac_ref":"91:6:2:2","qac_word_ref":"91:6:2","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"طَحَىٰ","morph_features":"STEM|POS:V|PERF|LEM:TaHaY`|ROOT:THw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:6:3:1","qac_word_ref":"91:6:3","root_ar":"ط ح و","surface_ar":"طَحَىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:6:3:2","qac_word_ref":"91:6:3","root_ar":"","surface_ar":"هَا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["91:6:1:1"],["91:6:1:2","91:6:1:3"],["91:6:2:1"],["91:6:2:2"],["91:6:3:1","91:6:3:2"]],"word_analysis_refs":["91:6:1","91:6:2","91:6:3","91:6:4","91:6:5"],"word_rows":[{"analysis_record_ref":"91:6:1","analytic_gloss_range_en":"oath-and link; here it renews the oath chain and installs the earth as the next sworn item","analytic_root_gloss_range_en":null,"qac_refs":["91:6:1:1"],"root":{"note":"-"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"91:6:2","analytic_gloss_range_en":"the known earth, lower ground, or terrestrial surface; locally the definite singular oath object that is then spread","analytic_root_gloss_range_en":"broad earth/land/ground range; local grammar selects the familiar singular terrestrial surface while allowing world-scale and habitable-ground resonance","qac_refs":["91:6:1:2","91:6:1:3"],"root":{"arabic":"أ ر ض","transliteration":"ʾ-r-ḍ"},"surface":{"arabic":"ٱلْأَرْضِ","transliteration":"al-arḍi"}},{"analysis_record_ref":"91:6:3","analytic_gloss_range_en":"internal connector; here it joins the earth to the following ambiguous spreader/process clause inside the oath unit","analytic_root_gloss_range_en":null,"qac_refs":["91:6:2:1"],"root":{"note":"-"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"91:6:4","analytic_gloss_range_en":"ambiguous relative or maṣdariyya particle; here it leaves the spreader, instrument, or spreading-act reading open within the oath clause","analytic_root_gloss_range_en":null,"qac_refs":["91:6:2:2"],"root":{"note":"-"},"surface":{"arabic":"مَا","transliteration":"ma"}},{"analysis_record_ref":"91:6:5","analytic_gloss_range_en":"spread, extend, make broad or level; locally a completed transitive action with the earth as object","analytic_root_gloss_range_en":"accepted root branches include spreading/extending, being carried far away, circling, pushing, bulk, sprawling, and rising; the local earth-object frame selects the spreading/extending branch, with tactile leveling and outward force as constrained color","qac_refs":["91:6:3:1","91:6:3:2"],"root":{"arabic":"ط ح و","transliteration":"ṭ-ḥ-w"},"surface":{"arabic":"طَحَىٰهَا","transliteration":"ṭaḥāhā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["91:6"],"branch_refs":["root_000025/B001","root_000928/B001"],"candidate_id":"cand_30f6aab9261096309a4b","evidence_scope":"focus_ayah","hft_ref":"hft_a3515054047dd33ca379","item_id":"b01_lower_expanse","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b01_lower_expanse","support_id":"sup_a2207e2ecbd8cd86ac7a"},{"anchor_refs":["91:6"],"branch_refs":["root_000025/B002","root_000025/B005","root_000928/B001","root_000928/B006"],"candidate_id":"cand_31f9bd79256e03ceceba","evidence_scope":"focus_ayah","hft_ref":"hft_d5a111d9d75152b6a231","item_id":"b02_fertile_receptive_mat","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b02_fertile_receptive_mat","support_id":"sup_05e42556c0e123b69aed"},{"anchor_refs":["91:6"],"branch_refs":["root_000025/B006","root_000928/B002","root_000928/B003"],"candidate_id":"cand_c7682506b05f0e13906c","evidence_scope":"focus_ayah","hft_ref":"hft_28fb03187889ad8f69e4","item_id":"b03_grounded_motion_field","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b03_grounded_motion_field","support_id":"sup_dc7698ab653ef6fd7627"},{"anchor_refs":["91:6"],"branch_refs":["root_000025/B007","root_000928/B004","root_000928/B005"],"candidate_id":"cand_5f9419eca25aa1dab2f0","evidence_scope":"focus_ayah","hft_ref":"hft_e37f395a6ba0b8118251","item_id":"b04_social_pressure_arena","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b04_social_pressure_arena","support_id":"sup_7d320ee9a06c2ff41d25"},{"anchor_refs":["91:6"],"branch_refs":["root_000025/B001","root_000928/B006","root_000928/B007"],"candidate_id":"cand_dd8cb7695208438214a6","evidence_scope":"focus_ayah","hft_ref":"hft_4296796a7ecb564ec1a7","item_id":"b05_reversible_flattening","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b05_reversible_flattening","support_id":"sup_b5b4b47a9990a0cc8a04"}],"diagnostics":[],"lane_counts":{"global":9,"macro":14,"micro":5},"packet_summary":{"ayah_count":15,"focus_ref":"91:6","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ت ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000186","furuq_root_norm":"ت ل و","furuq_source_root_norm":"ت ل و","is_dominant":true,"target_occurrences":39,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000185","furuq_root_norm":"ت ل ل","furuq_source_root_norm":"ت ل ل","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["91:1","91:2","91:3","91:4","91:5","91:6","91:7","91:8","91:9","91:10","91:11","91:12","91:13","91:14","91:15"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"91:6","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":19,"unstructured_record_count":0},"identity":{"ayah_ref":"91:6","lane":"micro","linguistic_source_ref":"91:6","surface_ref":"91:6","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"91:6","target_tokens":[["Yere",["91:6:1"]],["ve",["91:6:2"]],["onu",["91:6:3"]],["yayana",["91:6:2","91:6:3"]]],"text":"Yere ve onu yayana,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":15,"id":"s091-p01-001-015","label":"Whole surah","number":1,"refs":["91:1","91:2","91:3","91:4","91:5","91:6","91:7","91:8","91:9","91:10","91:11","91:12","91:13","91:14","91:15"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:2","source_type":"word_analysis","support_id":"sup_0c199394de5e926f9d4c","text":"{\"gloss_range\":\"the known earth, lower ground, or terrestrial surface; locally the definite singular oath object that is then spread\",\"prose\":\"{{ar:ٱلْأَرْضِ}} ({{tr:al-arḍi}}) names the known earth in the singular, not an indefinite land or a plurality of worlds. Its genitive case makes it the sworn-by object under the opening {{ar:وَ}} ({{tr:wa}}), and its grammatical femininity lets the final suffix in {{ar:طَحَىٰهَا}} ({{tr:ṭaḥāhā}}) point back to this same earth. The word therefore enters as both witness-object and affected surface. After the sky in 91:5, it completes a height-to-ground axis; the following clause then explains the earth through its spreadness rather than leaving it as a bare place-name. That makes a frequent earth word rhetorically marked by oath placement and formative qualifier; another earth oath uses a defining epithet in 86:12, while this one uses a spreading clause. Its compact, consonant-heavy sound is also answered by the more open cadence of the final spreading verb.\",\"root_display\":\"{{ar:أ ر ض}} ({{tr:ʾ-r-ḍ}})\",\"root_gloss_range\":\"broad earth/land/ground range; local grammar selects the familiar singular terrestrial surface while allowing world-scale and habitable-ground resonance\",\"surface_display\":\"{{ar:ٱلْأَرْضِ}} ({{tr:al-arḍi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:5:active-agent-slot","source_type":"word_analysis","support_id":"sup_11582ee37b1587d9649a","text":"{\"blocking_evidence\":null,\"headline\":\"agent slot kept open\",\"reader_payoff\":\"The reader avoids reading the earth as self-spreading; the grammar keeps agency present but referentially veiled through {{ar:مَا}} ({{tr:ma}}).\",\"reason\":\"The attachment profile reads {{ar:مَا}} ({{tr:ma}}) as subject and the suffix as object, matching the active 3ms verb.\",\"representative_source_ids\":[\"QG-cdde770f\",\"QG-fdeae215\",\"QF-9a10a014\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:3:internal-clause-hinge","source_type":"word_analysis","support_id":"sup_16549fcb38958cdc9aa3","text":"{\"blocking_evidence\":null,\"headline\":\"hinge into the spreading clause\",\"reader_payoff\":\"The reader notices the pivot from naming the earth to interpreting it through the spreading agent or process.\",\"reason\":\"Attachment evidence binds the {{ar:مَا طَحَىٰهَا}} ({{tr:ma ṭaḥāhā}}) clause alongside the earth in the oath sequence.\",\"representative_source_ids\":[\"QG-4e6c29a0\",\"QG-6d06b391\",\"QT-ddff525f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:4:compact-dependent-clause","source_type":"word_analysis","support_id":"sup_1dd15e7d5b6fadad4ccb","text":"{\"blocking_evidence\":null,\"headline\":\"compressed qualifier\",\"reader_payoff\":\"The reader sees how little wording the ayah needs to turn the earth from named object into shaped expanse.\",\"reason\":\"The subordinate clause evidence binds {{ar:مَا}} ({{tr:ma}}) with the perfect verb as the dependent oath element.\",\"representative_source_ids\":[\"QT-9d4dff03\",\"QT-db29f03f\",\"QY-e44961b6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:5:completed-form-i-action","source_type":"word_analysis","support_id":"sup_244ce8528fad595c2daa","text":"{\"blocking_evidence\":null,\"headline\":\"completed direct spreading\",\"reader_payoff\":\"The reader notices that the oath rests on an accomplished formative act: the earth has been made a spread expanse.\",\"reason\":\"QAC marks a perfect Form I verb with a clitic object, supporting completed direct action.\",\"representative_source_ids\":[\"QG-c43f63f2\",\"MG-8ab5bcce\",\"QF-b0e3a466\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:4:unnamed-agent","source_type":"word_analysis","support_id":"sup_2b8c3657c54191aed6df","text":"{\"blocking_evidence\":null,\"headline\":\"agent veiled through act\",\"reader_payoff\":\"The reader feels the theological and rhetorical reserve: agency is present, but it is approached through the act of spreading rather than through an explicit name.\",\"reason\":\"Attachment evidence reads {{ar:مَا}} ({{tr:ma}}) as the visible subject while leaving its discourse value unnamed.\",\"representative_source_ids\":[\"QS-f1050414\",\"MS-6881ad02\",\"QI-a2f138b8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:5:creation-oath-architecture","source_type":"word_analysis","support_id":"sup_326315d21cb815600f34","text":"{\"blocking_evidence\":null,\"headline\":\"horizontal counterpart in the oath series\",\"reader_payoff\":\"The reader sees earth-spreading as one axis in a larger creation-oath sequence: sky built upward in 91:5, earth spread outward in 91:6, soul proportioned in 91:7.\",\"reason\":\"The attachment data flags the repeated oath construction with 91:5, and the CRITICAL rows provide the forward link to 91:7.\",\"representative_source_ids\":[\"MI-ab390570\",\"QE-2f567ffc\",\"QE-b2b90076\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:5:near-root-daḥā-contrast","source_type":"word_analysis","support_id":"sup_334eadaf3daad00b6ea5","text":"{\"blocking_evidence\":null,\"headline\":\"near-root contrast with 79:30\",\"reader_payoff\":\"The reader notices that 91:6 uses a distinct, heavier near-root for earth-spreading rather than simply repeating the form associated with 79:30.\",\"reason\":\"The supplied contrast names 79:30; it is useful as a near-root comparison, while V4 and local grammar keep the selected branch as spreading/extending.\",\"representative_source_ids\":[\"QS-54b2ce55\",\"MS-48bed2a4\",\"QE-5601e009\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:2:feminine-antecedent","source_type":"word_analysis","support_id":"sup_339d08d80f91aac39cca","text":"{\"blocking_evidence\":null,\"headline\":\"antecedent for the final suffix\",\"reader_payoff\":\"The reader tracks the earth from oath object into patient of the spreading action, so the second half of the ayah is bound back to this noun.\",\"reason\":\"The attachment evidence licenses the suffix on {{ar:طَحَىٰهَا}} ({{tr:ṭaḥāhā}}) as referring to the same-ayah earth noun.\",\"representative_source_ids\":[\"QG-85f2dc17\",\"QG-eda671a3\",\"QS-c66e05da\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"91:6:1:3","source_type":"qac_morpheme","support_id":"sup_3520c76ee81f3ff53162","text":"{\"lemma_ar\":\"أَرْض\",\"morph_features\":\"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"91:6:1:3\",\"qac_word_ref\":\"91:6:1\",\"root_ar\":\"ء ر ض\",\"surface_ar\":\"أَرْضِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:5:leveling-pressure-color","source_type":"word_analysis","support_id":"sup_389a5d050bfecda43c1f","text":"{\"blocking_evidence\":null,\"headline\":\"tactile leveling and pressure\",\"reader_payoff\":\"The reader can feel the spread earth as a surface pressed broad or made level, while the ayah is not turned into a technical grinding or engineering claim.\",\"reason\":\"The dictionary supports related flattening and sprawling imagery, but the local transitive earth frame keeps spreading/extending primary.\",\"representative_source_ids\":[\"QS-4541f2dd\",\"QS-46267159\",\"QS-7e74d91c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:4:sound-suspension","source_type":"word_analysis","support_id":"sup_3b3c12d2bbc087891a60","text":"{\"blocking_evidence\":null,\"headline\":\"suspended open syllable\",\"reader_payoff\":\"The reader hears the referent remain open for a moment before the spreading action resolves the clause.\",\"reason\":\"The sound claim is anchored in the local surface sequence from {{ar:مَا}} ({{tr:ma}}) into the following verb.\",\"representative_source_ids\":[\"QP-bd72a5db\",\"QP-fb11ce03\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:3:wa-ma-template","source_type":"word_analysis","support_id":"sup_3c4c6808fa84889bb6ee","text":"{\"blocking_evidence\":null,\"headline\":\"repeated {{ar:وَمَا}} ({{tr:wa-ma}}) template\",\"reader_payoff\":\"The reader sees earth-spreading as the middle member of a repeated object-plus-agent-or-process pattern across 91:5-91:7.\",\"reason\":\"The attachment evidence flags the repeated 91:5 pattern, and the CRITICAL rows explicitly extend that pattern to 91:7.\",\"representative_source_ids\":[\"MT-dc50efd3\",\"QE-877bdcba\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:4","source_type":"word_analysis","support_id":"sup_3df84fb207c05f37133c","text":"{\"gloss_range\":\"ambiguous relative or maṣdariyya particle; here it leaves the spreader, instrument, or spreading-act reading open within the oath clause\",\"prose\":\"{{ar:مَا}} ({{tr:ma}}) is the ayah's interpretive hinge. If read as a relative, it points to the one or that which spread the earth; if read as maṣdariyya, it turns the clause toward the act of spreading itself. The surface does not choose between those routes, and the attachment evidence also preserves that ambiguity. The result is a compressed oath phrase: the earth has just been named, and this particle opens the question of spreader, source, or process before {{ar:طَحَىٰهَا}} ({{tr:ṭaḥāhā}}) supplies the completed action. Its long open syllable keeps that referent suspended for a beat before the verb lands. The same {{ar:مَا}} ({{tr:ma}})-plus-perfect pattern connects 91:6 with the neighboring creation-oath clauses in 91:5 and 91:7.\",\"root_display\":\"-\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مَا}} ({{tr:ma}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:2:earth-sound-weight","source_type":"word_analysis","support_id":"sup_40b64f7f646f27ce4849","text":"{\"blocking_evidence\":null,\"headline\":\"dense ground-name sound\",\"reader_payoff\":\"The reader hears the movement from a dense ground-name into the more open sound of the spreading verb.\",\"reason\":\"The sound observation is local and is reinforced by the immediately following verb-plus-suffix closure.\",\"representative_source_ids\":[\"QF-d3e505c6\",\"QP-a013d7cb\",\"QP-e9a7393e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:1:fused-earth-opening","source_type":"word_analysis","support_id":"sup_41882eaee2e57384f5fb","text":"{\"blocking_evidence\":null,\"headline\":\"particle fused to earth noun\",\"reader_payoff\":\"The reader hears the oath force and the earth noun arrive as one compact opening unit, not as a detached preface followed by content.\",\"reason\":\"The surface and recitation profile support treating the particle plus noun as a single opening unit while preserving the analytic distinction between particle and complement.\",\"representative_source_ids\":[\"QF-87540e79\",\"QP-13a3e7f9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:2:definite-singular-earth","source_type":"word_analysis","support_id":"sup_4b3c8499b60354334158","text":"{\"blocking_evidence\":null,\"headline\":\"known singular earth\",\"reader_payoff\":\"The reader sees that the oath begins from the shared, familiar earth before any broader land or planet extension is considered.\",\"reason\":\"QAC marks a definite singular concrete feminine noun, supporting identifiable earth as the local starting point.\",\"representative_source_ids\":[\"QG-1a8a9060\",\"QG-8351f90c\",\"QF-707b1a5e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:3","source_type":"word_analysis","support_id":"sup_4c3df6800a9f9eabb96e","text":"{\"gloss_range\":\"internal connector; here it joins the earth to the following ambiguous spreader/process clause inside the oath unit\",\"prose\":\"The second {{ar:وَ}} ({{tr:wa}}) looks identical to the first, but its job shifts because it is followed by {{ar:مَا}} ({{tr:ma}}) rather than a genitive noun. It does not simply start another ordinary object; it hinges from the named earth into the clause that identifies what spread it or the act of its spreading. That makes the ayah read as earth plus formative qualifier, and the fused entry loosens into open vowels after the denser earth noun. The same {{ar:وَمَا}} ({{tr:wa-ma}}) pattern links 91:6 with 91:5 and 91:7, so the earth-spreading clause sits in the middle of a repeated creation-oath structure.\",\"root_display\":\"-\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:2:terrestrial-surface-range","source_type":"word_analysis","support_id":"sup_74aecbc3f7b364a5f8d5","text":"{\"blocking_evidence\":null,\"headline\":\"earth as spreadable surface\",\"reader_payoff\":\"The reader hears the familiar earth as ground made broad and habitable, while the local clause keeps the range centered on spreadable surface rather than every possible land sense.\",\"reason\":\"The broader earth range is real, but the local object suffix and spreading verb narrow the active value toward terrestrial surface.\",\"representative_source_ids\":[\"QS-1bcdc95b\",\"QS-94bb36f1\",\"MS-dc1f327b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:2:common-word-marked-place","source_type":"word_analysis","support_id":"sup_81257533478ff2dc89bc","text":"{\"blocking_evidence\":null,\"headline\":\"common word made marked\",\"reader_payoff\":\"The reader notices that familiar vocabulary becomes rhetorically charged because of its oath placement and attached formative qualifier.\",\"reason\":\"The contextual profile confirms the word is frequent, while the local oath construction gives this occurrence marked function.\",\"representative_source_ids\":[\"QI-fc89b4fb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:5:weak-final-surface","source_type":"word_analysis","support_id":"sup_81fab1fde1a1c333c6f8","text":"{\"blocking_evidence\":null,\"headline\":\"weak-final morphology visible in closure\",\"reader_payoff\":\"The reader notices that root shape and object binding are fused in the final written word, not added as explanatory commentary.\",\"reason\":\"QAC aligns the surface to root {{ar:ط ح و}} ({{tr:ṭ-ḥ-w}}), and the written form before the suffix reflects weak-final morphology.\",\"representative_source_ids\":[\"QF-252ff2eb\",\"QF-9d453e2f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:2:object-qualifier-architecture","source_type":"word_analysis","support_id":"sup_879d7d489c20a2411d14","text":"{\"blocking_evidence\":null,\"headline\":\"object before qualifier\",\"reader_payoff\":\"The reader notices that the earth is not left bare; the oath points to the earth specifically as a spread expanse.\",\"reason\":\"Attachment evidence binds {{ar:مَا طَحَىٰهَا}} ({{tr:ma ṭaḥāhā}}) to the earth within the oath sequence.\",\"representative_source_ids\":[\"QT-3e3d3e87\",\"QT-ed10fee0\",\"QY-cbd712ff\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:2:oath-case","source_type":"word_analysis","support_id":"sup_92d25e71e35fe9f3ff4b","text":"{\"blocking_evidence\":null,\"headline\":\"genitive oath object\",\"reader_payoff\":\"The reader notices that the earth is grammatically installed as sworn evidence, not merely introduced as scenery.\",\"reason\":\"Attachment evidence treats the opening particle as oath {{ar:وَ}} ({{tr:wa}}) and the earth noun as its genitive complement.\",\"representative_source_ids\":[\"QG-98ae926a\",\"QG-dafbe3ac\",\"MG-b2dafe9c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:1","source_type":"word_analysis","support_id":"sup_970c920acb6f6c29531a","text":"{\"gloss_range\":\"oath-and link; here it renews the oath chain and installs the earth as the next sworn item\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) does more than connect 91:6 to what came before. It keeps the suspended oath sequence moving while beginning a fresh sworn item, so the earth is not a loose appendix to the sky oath in 91:5. Because this particle governs the following genitive noun, the ayah starts inside oath force before the earth is even named, and in the surface opening the particle and earth noun arrive as one compact unit. Its short sound also returns before {{ar:مَا}} ({{tr:ma}}), pairing the earth and its spreading clause as two linked beats with different grammatical jobs.\",\"root_display\":\"-\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:4:relative-or-masdariyya","source_type":"word_analysis","support_id":"sup_9e160de5840e6f60c2f3","text":"{\"blocking_evidence\":null,\"headline\":\"agent/process ambiguity\",\"reader_payoff\":\"The reader notices that the oath does not force a single explicit target: it can foreground the spreader, the spreading act, or the source-like process.\",\"reason\":\"QAC permits relative or maṣdariyya analysis, and attachment evidence explicitly instructs preserving ambiguity.\",\"representative_source_ids\":[\"QG-c24ec814\",\"QG-ca111629\",\"MG-af9a957e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:5:spread-extend-branch","source_type":"word_analysis","support_id":"sup_9ebe0f7fd32bed9406d4","text":"{\"blocking_evidence\":null,\"headline\":\"spreading and extending branch\",\"reader_payoff\":\"The reader sees the earth as a made expanse, not as a neutral location or as the product of a generic making verb.\",\"reason\":\"V4 lists spreading/extending as the accepted root branch, and the local object is the earth.\",\"representative_source_ids\":[\"QS-1ce2e5c1\",\"QS-2cfff787\",\"QS-d604f125\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:2:earth-oath-echo","source_type":"word_analysis","support_id":"sup_a521c7c8d92b35e86547","text":"{\"blocking_evidence\":null,\"headline\":\"earth oath by defining feature\",\"reader_payoff\":\"The reader can compare how earth becomes oath-worthy through a defining quality in 86:12 and through formative spreading in 91:6.\",\"reason\":\"The supplied echo names 86:12, so it can survive as a comparison without controlling the local grammar.\",\"representative_source_ids\":[\"MI-f2d68b97\",\"QE-5444cabb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:3:same-form-different-force","source_type":"word_analysis","support_id":"sup_bb119636414c4ca805da","text":"{\"blocking_evidence\":null,\"headline\":\"same particle, different environment\",\"reader_payoff\":\"The reader avoids flattening the two particles into identical syntax: the first installs the oath noun, the second extends the sworn field.\",\"reason\":\"The first particle is followed by the earth noun, while this one is followed by {{ar:مَا}} ({{tr:ma}}), supporting differentiated function.\",\"representative_source_ids\":[\"MG-e59379cf\",\"QS-63653148\",\"QF-4a97e8b8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:4:neighboring-ma-pattern","source_type":"word_analysis","support_id":"sup_c1d1b7f7936482f7da2a","text":"{\"blocking_evidence\":null,\"headline\":\"repeated {{ar:مَا}} ({{tr:ma}})-verb pattern\",\"reader_payoff\":\"The reader tracks the same agent-or-act ambiguity across sky, earth, and soul clauses in 91:5-91:7.\",\"reason\":\"The bundle marks the 91:5 pattern, and the CRITICAL rows extend the same pattern through the neighboring clauses.\",\"representative_source_ids\":[\"MI-cb206fd3\",\"QE-c5d290f8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:5","source_type":"word_analysis","support_id":"sup_c45d650fa2b828d9f97a","text":"{\"gloss_range\":\"spread, extend, make broad or level; locally a completed transitive action with the earth as object\",\"prose\":\"{{ar:طَحَىٰهَا}} ({{tr:ṭaḥāhā}}) gives the earth oath its completed action. The perfect verb presents the spreading as already accomplished, and the attached feminine suffix binds the action back to {{ar:ٱلْأَرْضِ}} ({{tr:al-arḍi}}), making the earth the direct object acted upon rather than the actor. The root's local branch is spreading, extending, and making broad; tactile leveling, outward force, and even concrete earth-surface extension can illustrate that image, but they do not turn the ayah into a technical engineering, grinding, or modern science claim. The form also differs from the near-root earth-spreading wording in 79:30, so the contrast marks this oath's heavier local choice without replacing the spreading branch. Because {{ar:طَحَىٰهَا}} ({{tr:ṭaḥāhā}}) is a rare, locally concentrated form, the surrounding oath architecture matters: it answers sky-building in 91:5 as horizontal earth-spreading and prepares the next shaped-object clause in 91:7. Its weak-final root shape is hidden in the written closure while the object suffix remains fused to the word. Its heavy opening consonants release into the long {{ar:ـَاهَا}} ({{tr:-aha}}) cadence, so the sound itself moves from pressure into expanse.\",\"root_display\":\"{{ar:ط ح و}} ({{tr:ṭ-ḥ-w}})\",\"root_gloss_range\":\"accepted root branches include spreading/extending, being carried far away, circling, pushing, bulk, sprawling, and rising; the local earth-object frame selects the spreading/extending branch, with tactile leveling and outward force as constrained color\",\"surface_display\":\"{{ar:طَحَىٰهَا}} ({{tr:ṭaḥāhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:2:sky-earth-axis","source_type":"word_analysis","support_id":"sup_c77bfe7b889408363c08","text":"{\"blocking_evidence\":null,\"headline\":\"sky-to-earth axis\",\"reader_payoff\":\"The reader notices the descent from elevated structure in 91:5 to lower spread surface in 91:6, making the two oaths a vertical pair.\",\"reason\":\"The local sequence and contextual collocation profile support a sky-earth pairing without making the current word dependent on a nonlocal sense.\",\"representative_source_ids\":[\"QS-cac00c06\",\"QI-5656b1bf\",\"QY-89d98c7c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:5:object-agent-doublet","source_type":"word_analysis","support_id":"sup_c9bafdd17e37a2fee641","text":"{\"blocking_evidence\":null,\"headline\":\"object plus spreader/process doublet\",\"reader_payoff\":\"The reader sees that the take-away of the oath unit is the earth as spread by an agent or process, not the earth as a bare cosmic item.\",\"reason\":\"The clause structure makes the final verb-plus-suffix the qualifier of the earth within the same oath unit.\",\"representative_source_ids\":[\"QT-a5cad9f3\",\"QT-a85771c0\",\"QT-c159abec\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:3:open-vowel-entry","source_type":"word_analysis","support_id":"sup_cb7eceffa0210f34e0f5","text":"{\"blocking_evidence\":null,\"headline\":\"open-vowel entry to the qualifier\",\"reader_payoff\":\"The reader hears the qualifier loosen into open vowels after the denser earth noun, matching the movement toward spreadness.\",\"reason\":\"The surface fusion of {{ar:وَ}} ({{tr:wa}}) to {{ar:مَا}} ({{tr:ma}}) and the following verb make this a local sound observation.\",\"representative_source_ids\":[\"QF-9c6d96c3\",\"QT-75d91a36\",\"QP-b7a8a244\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:1:paired-wa-refrain","source_type":"word_analysis","support_id":"sup_ce5577807455ec54fa6c","text":"{\"blocking_evidence\":null,\"headline\":\"outer and inner connectors\",\"reader_payoff\":\"The reader notices that the two identical particles create an audible refrain while doing different work: one swears by the earth, the other brings in what spread it.\",\"reason\":\"The two particles have the same surface, but their following environments distinguish oath governance from internal coordination.\",\"representative_source_ids\":[\"QE-e2e9c56a\",\"QP-edeae008\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"91:6:3:1","source_type":"qac_morpheme","support_id":"sup_d8f29fa48b79a5b7d8a5","text":"{\"lemma_ar\":\"طَحَىٰ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:TaHaY`|ROOT:THw|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"91:6:3:1\",\"qac_word_ref\":\"91:6:3\",\"root_ar\":\"ط ح و\",\"surface_ar\":\"طَحَىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:5:cadence-and-articulation","source_type":"word_analysis","support_id":"sup_e1d623631240fd012338","text":"{\"blocking_evidence\":null,\"headline\":\"pressure releasing into expanse\",\"reader_payoff\":\"The reader hears the word move from constricted force into open cadence, matching the semantic movement toward spreadness.\",\"reason\":\"The sound claim is anchored in the local surface of the final word and its relation to the dense earth noun.\",\"representative_source_ids\":[\"QF-7393e8a3\",\"QP-6096260f\",\"QP-810aafd9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:5:transitive-pronoun-binding","source_type":"word_analysis","support_id":"sup_e4c8ebe113fb1688e1be","text":"{\"blocking_evidence\":null,\"headline\":\"earth bound as object\",\"reader_payoff\":\"The reader sees the earth move from sworn object to directly affected surface in the final word.\",\"reason\":\"Attachment evidence marks the suffix as the direct object and resolves it to the local earth noun.\",\"representative_source_ids\":[\"QG-3a69aeb4\",\"QG-843a3a5c\",\"QF-21961c82\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:5:hapax-concentration","source_type":"word_analysis","support_id":"sup_e73431be7cd40cf08dfb","text":"{\"blocking_evidence\":null,\"headline\":\"locally concentrated hapax\",\"reader_payoff\":\"The reader treats {{ar:طَحَىٰهَا}} ({{tr:ṭaḥāhā}}) as marked vocabulary whose force must be learned from this oath frame, not from routine recurrence.\",\"reason\":\"The contextual profile marks the root-form occurrence as low occurrence with one local frame, supporting local-context decisiveness.\",\"representative_source_ids\":[\"QI-ba87b0b3\",\"QH-f5cc9eaf\",\"MH-09d2d5e3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:1:oath-renewal","source_type":"word_analysis","support_id":"sup_f3024c7b7f78a27affde","text":"{\"blocking_evidence\":null,\"headline\":\"fresh oath item in the chain\",\"reader_payoff\":\"The reader notices that the ayah continues the cumulative oath pressure while giving the earth its own witness-status.\",\"reason\":\"QAC and attachment evidence mark the opening particle as oath {{ar:وَ}} ({{tr:wa}}) governing the genitive earth noun, so the continuation and oath force survive together.\",\"representative_source_ids\":[\"QG-39a73fb5\",\"QG-5e5d246f\",\"QI-0b80bd74\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:6:5:modern-geology-limit","source_type":"word_analysis","support_id":"sup_f40475d425f5d00c3e3f","text":"{\"blocking_evidence\":null,\"headline\":\"concrete extension without science claim\",\"reader_payoff\":\"The reader may recognize literal earth-surface extension as a concrete analogy, while the lexical point remains spreading and extending rather than a modern scientific assertion.\",\"reason\":\"The core spread/extend sense survives, but the modern geological framing is external and must not be allowed to determine the local meaning.\",\"representative_source_ids\":[\"QS-1b2bfe39\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْأَرْضِ وَمَا طَحَىٰهَا","ayah_ref":"91:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000025/B001","root_000928/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000025","role":"The lower ground opposite the sky supplies the spatial patient and its below-ward orientation.","root":"ء ر ض","source_ref":"91:6","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000928","role":"Spreading and extension supply the outward operation performed on that lower ground.","root":"ط ح و","source_ref":"91:6","source_word_indices":["3"]}],"changed_reading":{"after":"The oath isolates the making of an extended lower plane, defined relationally against what is above.","before":"The verse merely names the earth and says that it was spread."},"confidence":"strong","focus_anchor":"الأرض at word 1 is the patient of طحى at word 3 through the feminine suffix ها.","mechanism":"The two roots compose a spatial operation: the lower member of a sky-ground relation is extended outward into an expanse.","model_id":"b01_lower_expanse"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b01_lower_expanse","source_type":"hft","support_id":"sup_a2207e2ecbd8cd86ac7a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْأَرْضِ وَمَا طَحَىٰهَا","ayah_ref":"91:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000025/B002","root_000025/B005","root_000928/B001","root_000928/B006"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000025","role":"Soft fertile ground supplies a living, growth-bearing quality to the object being spread.","root":"ء ر ض","source_ref":"91:6","source_word_indices":["1"]},{"branch_id":"B005","mapped_root_id":"root_000025","role":"The thick mat supplies a laid-out, habitable material analogy for the ground.","root":"ء ر ض","source_ref":"91:6","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000928","role":"Spreading and widening turn the fertile material into an available surface.","root":"ط ح و","source_ref":"91:6","source_word_indices":["3"]},{"branch_id":"B006","mapped_root_id":"root_000928","role":"Sprawling along and adhering to the ground supplies the close surface-contact by which vegetation or bodies occupy it.","root":"ط ح و","source_ref":"91:6","source_word_indices":["3"]}],"changed_reading":{"after":"The act lays out a receptive, fertile mat whose extension enables rooting, dwelling, and use.","before":"The verb only enlarges inert terrain."},"confidence":"medium","focus_anchor":"The focus noun can be fertile ground or a thick mat, while its governing verb can spread and press growth along a surface.","mechanism":"Extension is functional rather than merely geometric: it lays out a soft, receptive substrate on which life can root, feed, and travel.","model_id":"b02_fertile_receptive_mat"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b02_fertile_receptive_mat","source_type":"hft","support_id":"sup_05e42556c0e123b69aed","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْأَرْضِ وَمَا طَحَىٰهَا","ayah_ref":"91:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000025/B006","root_000928/B002","root_000928/B003"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_000025","role":"Sticking to the ground and lingering supply the fixed pole from which motion departs.","root":"ء ر ض","source_ref":"91:6","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000928","role":"Extended going supplies long-range movement across the field.","root":"ط ح و","source_ref":"91:6","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_000928","role":"Circling vultures supply a recurrent, non-linear trajectory around a grounded center.","root":"ط ح و","source_ref":"91:6","source_word_indices":["3"]}],"changed_reading":{"after":"The spread earth is also a field that organizes rest, departure, distance, and return-like circulation.","before":"Spreading denotes a static increase of surface area."},"confidence":"exploratory","focus_anchor":"The focus inventories place ground-clinging, far-going, and circular motion around the same earth-spreading construction.","mechanism":"The earth functions as a reference field: bodies may rest against it, be carried far across it, or circle over it, so spreading organizes trajectories as well as area.","model_id":"b03_grounded_motion_field"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b03_grounded_motion_field","source_type":"hft","support_id":"sup_dc7698ab653ef6fd7627","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْأَرْضِ وَمَا طَحَىٰهَا","ayah_ref":"91:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000025/B007","root_000928/B004","root_000928/B005"],"payload":{"activation_trace":[{"branch_id":"B007","mapped_root_id":"root_000025","role":"Coming forward in confrontation converts ground from scenery into a site of encounter.","root":"ء ر ض","source_ref":"91:6","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_000928","role":"People pushing one another supplies the social force operating across the site.","root":"ط ح و","source_ref":"91:6","source_word_indices":["3"]},{"branch_id":"B005","mapped_root_id":"root_000928","role":"A great multitude or broad army supplies collective scale to the spreading.","root":"ط ح و","source_ref":"91:6","source_word_indices":["3"]}],"changed_reading":{"after":"Its extension can also be heard as making room for collective presence, pressure, and confrontation.","before":"The earth is an empty physical extension."},"confidence":"exploratory","focus_anchor":"Marginal branches of both focus roots turn ground and spreading toward confrontation, mutual pushing, and large human formations.","mechanism":"Making an expanse also makes an arena: collective bodies can assemble there, press against one another, and contest exposure or position.","model_id":"b04_social_pressure_arena"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b04_social_pressure_arena","source_type":"hft","support_id":"sup_7d320ee9a06c2ff41d25","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْأَرْضِ وَمَا طَحَىٰهَا","ayah_ref":"91:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000025/B001","root_000928/B006","root_000928/B007"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000025","role":"The lower ground supplies the terminal plane against which a body may be flattened.","root":"ء ر ض","source_ref":"91:6","source_word_indices":["1"]},{"branch_id":"B006","mapped_root_id":"root_000928","role":"A struck body or animal sprawling against the ground supplies the violent route to flat extension.","root":"ط ح و","source_ref":"91:6","source_word_indices":["3"]},{"branch_id":"B007","mapped_root_id":"root_000928","role":"The isolated perishing sense keeps destruction live at the far edge of the verb.","root":"ط ح و","source_ref":"91:6","source_word_indices":["3"]}],"changed_reading":{"after":"The creative expanse carries a latent reversible image of being leveled down to the ground.","before":"Spreading is exclusively a benign creative act."},"confidence":"exploratory","focus_anchor":"The focus verb includes bodies sprawled against the ground after force and an isolated perishing branch.","mechanism":"Spreading has a dangerous edge: the same low, extended profile can result from generative laying-out or from a body being pressed down and destroyed.","model_id":"b05_reversible_flattening"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b05_reversible_flattening","source_type":"hft","support_id":"sup_b5b4b47a9990a0cc8a04","trust":"legacy_unbound"}]}
</lane_packet_json>
