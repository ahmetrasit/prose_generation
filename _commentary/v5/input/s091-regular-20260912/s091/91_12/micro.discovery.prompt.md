# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **91:12**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s091-regular-20260912/s091/91_12/micro.discovery.json` and modify nothing
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
  "ayah_ref": "91:12",
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
{"branch_registry":[{"boundary":"Bu dal dışarıdan harekete geçirmeyi anlatır; salt gönderme ve öznenin kendiliğinden yola koyulması ayrı dallardadır.","branch_kind":"mixed_non_bare","branch_ref":"root_000129/B001","candidate_links":[{"candidate_id":"cand_04ed7a4291c3ed4a5fb8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ٱنۢبَعَثَ","morph_features":"STEM|POS:V|PERF|(VII)|LEM:{n[baEava|ROOT:bEv|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:12:2:1","qac_word_ref":"91:12:2","surface_ar":"ٱنۢبَعَثَ"}],"gloss":"durgun olanı harekete geçirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dışarıdaki bir etken, durgun durumdaki varlığı uyararak etkin duruma geçirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bağlı ya da çökmüş bir hayvanın bağı çözülür veya hayvan kaldırılarak harekete yöneltilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Uyuyan kişi uyarılarak uykudan çıkarılır ve uyanması sağlanır."}}],"root_ar":"ب ع ث","root_id":"root_000129","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dışarıdaki bir etkenin durağan bir varlığı uyararak etkin duruma geçirdiği dalın bütünü için kullanılır.","boundary_detail":"Bu dal dışarıdan harekete geçirmeyi anlatır; salt gönderme ve öznenin kendiliğinden yola koyulması ayrı dallardadır.","branch_image_ar":"إثارة الساكن من ركوده","concept_gloss":"durgun olanı harekete geçirme","contextual_glosses":[{"applicability":"Uyuyan bir kişinin uyarılıp uykudan çıkarıldığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvanı bağından çözüp kaldırma ve başka durağan varlıkları harekete geçirme kapsamını dışarıda bırakır.","preserves":"Durgun bir durumdan dış etkiyle çıkarılma ve etkinleşme sonucunu korur."},"facet_ids":["F001","F003"],"text":"uyandırma","usage_role":"contextual"},{"applicability":"Bağlı ya da çökmüş bir hayvanın serbest bırakılıp hareket ettirildiği bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uyuyanı uyandırma ve hayvan dışındaki varlıkları genel olarak harekete geçirme kapsamını vermez.","preserves":"Dışarıdan müdahaleyle durgunluğu sona erdirme ve harekete başlatma işlemini korur."},"facet_ids":["F001","F002"],"text":"çözüp ayağa kaldırma","usage_role":"contextual"}],"definition":"Durgun, bağlı, çökmüş ya da uyuyan bir varlığı dışarıdan uyarıp bulunduğu durumdan çıkmasını, hareket etmesini, doğrulmasını veya uyanmasını sağlamaktır. Bağlama göre bu harekete geçirme, varlığı bir yöne sevk etmeyi de içerir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dışarıdaki bir etken, durgun durumdaki varlığı uyararak etkin duruma geçirir."},{"facet_id":"F002","role":"specialization","statement":"Bağlı ya da çökmüş bir hayvanın bağı çözülür veya hayvan kaldırılarak harekete yöneltilir."},{"facet_id":"F003","role":"specialization","statement":"Uyuyan kişi uyarılarak uykudan çıkarılır ve uyanması sağlanır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Belirli bir görev veya hedef için yola çıkarma anlamını öne çıkarır.","collision":"Aynı kökün gönderme ve görevlendirme dalıyla karışır.","fit":"displacement","loses":"Durgunluğu bozma, uyandırma ve harekete geçirme işlemlerini vermez.","preserves":"Bir varlığın dışarıdaki bir etken tarafından bir yöne sevk edilmesi yanını kısmen korur."},"text":"gönderme"}],"identity_rationale":"Kaynak ifadesi, temel anlamı durağan bir şeyi dışarıdan uyararak bulunduğu durumdan çıkarmak olarak verir. Bağlı ya da çökmüş deveyi çözüp kaldırma ve uyuyanı uyandırma örnekleri bu çekirdeğin farklı gerçekleşmeleridir; yöneltme ise harekete geçirmenin bağlama bağlı bir devamıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"harekete geçirmek; uyandırmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"devenin bağını çözüp onu ayağa kaldırmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"uyuyanı uyandırmak"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kargaşanın kabarmaları ve alevlenmeleri"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"neredeyse hiç uyumayan adam"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"neredeyse hiç çökmeyen dişi deve"}],"lexicalization_note":"Tanım genel harekete geçirme çekirdeğini korur; deve, uyuyan, kargaşa ve sürekli uyanık kalma anlatımları yalnızca kendi yapılarına bağlı özel kullanımlardır.","neighbor_coverage_note":"Verilen bütün komşular değerlendirildi; yalnızca dıştan harekete geçirme sınırını gönderme, öznenin ilerlemesi, genel hareket ettirme, uyanıklık ve canlılıktan ayıran beş karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda kurucu işlem durgunluğu bozup etkinleştirmektir; komşu dalda ise katılımcının önceden durgun olup olmamasından bağımsız olarak görev veya hedef doğrultusunda gönderilmesi kurucudur.","focus_only":"Durgun, bağlı, çökmüş veya uyuyan varlığı uyararak etkin duruma çıkarır.","gloss":"göndermek ve görevlendirmek","neighbor_only":"Bir kişi, nesne veya birliği belirli bir görev ya da hedef için gönderir.","neighbor_ref":"root_000129/B002","relation_type":"near_neighbor","shared_zone":"Her ikisinde de dışarıdaki bir etken başka bir katılımcıyı harekete ve bir yöne sevk edebilir."},{"boundary_match":"partial","distinction":"Bu dal geçişi yaptıran dış etkeni öne çıkarır; komşu dal ise hareket eden öznenin kendi ilerleyişini anlatır ve dışarıdan bir uyarıcı gerektirmez.","focus_only":"Hareketi başlatan dış etkeni ve onun uyarıcı müdahalesini içerir.","gloss":"yola koyulup ilerlemek","neighbor_only":"Öznenin hareketini yola koyulma, art arda ilerleme veya hızlanma olarak sunar.","neighbor_ref":"root_000129/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da durgunluktan harekete geçişi ve ardından ortaya çıkan ilerlemeyi kapsayabilir."},{"boundary_match":"partial","distinction":"Komşu anlam genel bir hareket ettirmedir; bu dal ise özellikle durgun, bağlı, çökmüş veya uyuyan varlığın o durumdan çıkarılmasını gerektirir.","focus_only":"Durgunluğu sona erdirme, uyandırma veya ayağa kaldırma gibi başlangıç durumu ve sonuç sınırları taşır.","gloss":"hareket ettirmek","neighbor_only":"Başlangıçtaki durgunluk ya da sonucun etkinleşme olması şart olmadan genel bir kıpırdatmayı anlatır.","neighbor_ref":"root_000003/B006","relation_type":"near_synonym","shared_zone":"İki dal da dışarıdaki bir etkenin bir şeyi hareketli duruma getirmesini ifade eder."},{"boundary_match":"partial","distinction":"Bu dalın uykuya ilişkin kullanımı ettirgendir ve uyandırma eylemine bağlıdır; komşu dal uyanma ile uyanık olma durumlarını kendi başına kapsar.","focus_only":"Bir başkasını uyandıran dış etkiyi ve uykudan çıkarma işlemini anlatır.","gloss":"uyanıklık ve uyanma","neighbor_only":"Uyanıklık durumunu, kişinin uyanmasını ve uyku karşıtı genel alanı da kapsar.","neighbor_ref":"root_001695/B001","relation_type":"near_neighbor","shared_zone":"Uyuyan kişinin uykudan çıkıp uyanık duruma geçmesi iki anlam alanında da yer alır."},{"boundary_match":"field_only","distinction":"Bu dal nedensel bir harekete geçirme olayıdır; komşu dal ise hareketin nedeni olabilen içsel istek ve canlılık durumudur.","focus_only":"Dış etkiyle durgunluğu bozup hareketi başlatan olayı bildirir.","gloss":"canlılık ve çalışma isteği","neighbor_only":"İçten gelen istek, dinçlik ve çalışmaya hazır olma niteliğini bildirir.","neighbor_ref":"root_001505/B001","relation_type":"same_field","shared_zone":"Her iki alan da hareketsizlikten etkinliğe geçiş ve çalışma ya da hareket etme durumuyla ilişkilidir."}],"source_phrase_ar":"الباء والعين والثاء أصل واحد وهو الإثارة (maqayis)؛ بعثت الناقة إذا أثرتها (maqayis;sihah)؛ بعثت البعير أرسلته وحللت عقاله أو كان باركا فهجته (ayn)؛ بعثت البعير فانبعث إذا حللت عقاله وأرسلته لو كان باركا فأثرته (tahdhib)؛ بعثته من نومه فانبعث وبعثت النائم إذا أهببته (sihah;tahdhib)؛ أصل البعث إثارة الشيء وتوجيهه (mufradat)","source_summary":"Kaynaklar, anlamın ortak çekirdeğini durağan olanı uyarmak ve harekete yöneltmek olarak sunar; bağlı veya çökmüş hayvanı kaldırma ile uyuyanı uyandırma bu çekirdeği görünür kılar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه إثارة البعير البارك أو المقيد، وإهابة النائم، وكل شيء يثار فيثور أو يهتاج.","what_is_not_ar":"ليس مجرد إرسال إلى جهة إلا إذا صرح بالإثارة؛ ولا إحياء الموتى للحشر."},"support_links":["sup_1c7fc6154f1a05447e6d"]},{"boundary":"Bu dal dışarıdaki bir göndericinin görev veya hedef verdiği yöneltmedir; uyandırma ile öznenin kendiliğinden ilerlemesi kapsam dışıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000129/B002","candidate_links":[{"candidate_id":"cand_18293f7ae42e34ddee49","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ٱنۢبَعَثَ","morph_features":"STEM|POS:V|PERF|(VII)|LEM:{n[baEava|ROOT:bEv|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:12:2:1","qac_word_ref":"91:12:2","surface_ar":"ٱنۢبَعَثَ"}],"gloss":"gönderme veya yöneltme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir gönderici, başka bir katılımcıyı belirli bir ihtiyaç, görev, yön veya hedef doğrultusunda yollar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gönderme, bir kişiyi belirli bir işi yapmaya isteklendirip o işe yöneltme biçiminde gerçekleşebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Eylemin sonucu olarak göreve veya hedefe gönderilmiş topluluk, asker birliği ya da ordular adlandırılabilir."}}],"root_ar":"ب ع ث","root_id":"root_000129","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir göndericinin kişi, nesne veya topluluğu ihtiyaç, görev, hedef ya da yön doğrultusunda yolladığı çekirdek anlam için kullanılır.","boundary_detail":"Bu dal dışarıdaki bir göndericinin görev veya hedef verdiği yöneltmedir; uyandırma ile öznenin kendiliğinden ilerlemesi kapsam dışıdır.","branch_image_ar":"إرسال المبعوث وتوجيهه","concept_gloss":"gönderme veya yöneltme","contextual_glosses":[{"applicability":"Bir kişi veya topluluk belirli bir iş ya da hedef için yola çıkarıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Birini yalnızca bir işi yapmaya isteklendirip yöneltme ile gönderilmiş topluluk adı kullanımını vermez.","preserves":"Dış göndericiyi, görevi ve hedefe doğru yollama işlemini korur."},"facet_ids":["F001"],"text":"görevlendirip gönderme","usage_role":"general"},{"applicability":"Bir kişi bir şeyi yapmaya isteklendirilip o eyleme yöneltildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir hedefe fiziksel olarak gönderme ile gönderilmiş topluluk ve birlik adlarını dışarıda bırakır.","preserves":"Dışarıdaki etkenin başka bir katılımcıyı belirli bir iş doğrultusunda yöneltmesini korur."},"facet_ids":["F002"],"text":"bir işe sevk etme","usage_role":"contextual"},{"applicability":"Bir görev veya hedef için yollanmış asker topluluğunun adlandırıldığı bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gönderme eylemini, asker olmayan katılımcıları ve birini işe yöneltme kullanımını vermez.","preserves":"Gönderme sonucunda ortaya çıkan görevlendirilmiş topluluk anlamını korur."},"facet_ids":["F003"],"text":"gönderilmiş birlik","usage_role":"contextual"}],"definition":"Bir kişi, nesne veya topluluğu belirli bir ihtiyaç, görev, hedef ya da yön için göndermek veya yöneltmektir. Bu işlem birini bir işi yapmaya yöneltme biçimini alabilir; gönderilmiş topluluk veya birlik adı ise işlemin sonucuna bağlı bir kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir gönderici, başka bir katılımcıyı belirli bir ihtiyaç, görev, yön veya hedef doğrultusunda yollar."},{"facet_id":"F002","role":"specialization","statement":"Gönderme, bir kişiyi belirli bir işi yapmaya isteklendirip o işe yöneltme biçiminde gerçekleşebilir."},{"facet_id":"F003","role":"associated_use","statement":"Eylemin sonucu olarak göreve veya hedefe gönderilmiş topluluk, asker birliği ya da ordular adlandırılabilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Uyku durumunu ve uykudan çıkarma sonucunu gereksiz biçimde ekler.","collision":"Aynı kökün durgun olanı harekete geçirme dalıyla karışır.","fit":"displacement","loses":"Görev, hedef, yön ve gönderme ilişkilerinin tümünü kaybeder.","preserves":"Dışarıdaki bir etkenin başka bir katılımcıda hareket başlatması yanını kısmen korur."},"text":"uyandırma"}],"identity_rationale":"Kaynak ifadesi, bir kişi, nesne veya topluluğu bir ihtiyaç, görev ya da hedef doğrultusunda göndermeyi ortak çekirdek olarak gösterir. Birini bir işi yapmaya yöneltme bu çekirdeğin etkileyici kullanımı, gönderilmiş topluluk ve birlik adları ise eylemin sonucuna dayanan adlandırmalardır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"göndermek; yöneltmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"görevle göndermek; yola çıkarmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"birini bir iş için göndermek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birini bir işi yapmaya isteklendirip yöneltmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"asker birliğini düşmana karşı göndermek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"göreve gönderilmiş topluluk veya birlik"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"gönderilmiş ordular"}],"lexicalization_note":"Tanım genel gönderme çekirdeğini, bir işe yöneltme yapısını ve gönderilmiş topluluk adlarını ayırır; yapıya bağlı askeri ve görevsel kapsamı bütün dala yaymaz.","neighbor_coverage_note":"Verilen bütün komşular değerlendirildi; gönderme çekirdeğini özel haberci yollama, savaşa gönderme, dürtme, öznenin amaçlı yönelişi ve durgunluğu bozma anlamlarından ayıran beş karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal özel bir habercinin bir ihtiyaç için gönderilmesidir; bu dal ise haberci olma ve tek kişi olma şartı olmadan nesne, topluluk ve birliklerin gönderilmesini de kapsar.","focus_only":"Kişi, nesne, topluluk ve asker birliği dahil daha geniş bir gönderilenler ve görevler alanını kapsar.","gloss":"özel haberci gönderme","neighbor_only":"Özellikle bir ihtiyaç için yollanan tek ve özel bir haberciyle sınırlıdır.","neighbor_ref":"root_001145/B011","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir gönderici, bir kişiyi belirli bir ihtiyacı karşılamak üzere görevlendirip yollar."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği genel amaçlı göndermedir; komşu dal askeri hedefle sınırlıdır ve gönderme yanında donatma ya da araç sağlama işlemlerini de kapsayabilir.","focus_only":"Savaş dışındaki ihtiyaç ve görevleri, nesneleri ve gönderilmiş topluluk adlarını da kapsar.","gloss":"savaşa gönderip donatmak","neighbor_only":"Gönderileni savaşa hazırlama, donatma veya ona binek sağlama işlemlerini ayrıca içerir.","neighbor_ref":"root_001085/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir kişiyi veya birliği düşmana karşı savaşmak üzere dışarıdan görevlendirip gönderebilir."},{"boundary_match":"partial","distinction":"Bu dalda yöneltme genel gönderme çekirdeğine bağlıdır; komşu dalda ise kurucu işlem kişiyi teşvik etmek veya acele ettirmektir ve bir hedefe yollama gerekmez.","focus_only":"Katılımcıyı bir görev veya hedef doğrultusunda gerçekten gönderme sonucunu içerir.","gloss":"dürtme ve acele ettirme","neighbor_only":"Gönderme gerçekleşmeden de birini dürtme, acele ettirme ve güçlü biçimde özendirmeyi anlatır.","neighbor_ref":"root_000293/B001","relation_type":"near_neighbor","shared_zone":"Bir kişiyi belirli bir işi yapmaya yöneltme ve eyleme geçmesi için etkileme iki alanda da bulunur."},{"boundary_match":"partial","distinction":"Bu dal gönderici ile gönderilen arasında ettirgen bir ilişki kurar; komşu dal ise hareket eden öznenin kendi amacını ve yönelişini ifade eder.","focus_only":"Başka bir katılımcıyı dışarıdan görevlendirip hedefe yollar.","gloss":"amaçlayıp yönelmek","neighbor_only":"Öznenin kendi niyetini, hedef seçimini ve bir şeye yönelmesini anlatır.","neighbor_ref":"root_000053/B012","relation_type":"near_neighbor","shared_zone":"Her iki dalda da belirli bir hedef veya yön, hareketin düzenleyici unsurudur."},{"boundary_match":"partial","distinction":"Bu dalda görev veya hedef doğrultusunda yollama kurucudur; komşu dalda ise katılımcının önceki durgunluğunu bozup onu etkinleştirmek kurucudur.","focus_only":"Katılımcıyı belirli bir görev, ihtiyaç, yön veya hedef için gönderir.","gloss":"durgun olanı harekete geçirmek","neighbor_only":"Durgun, bağlı, çökmüş veya uyuyan varlığı uyarıp etkin duruma çıkarır.","neighbor_ref":"root_000129/B001","relation_type":"near_neighbor","shared_zone":"Her ikisinde de dışarıdaki bir etken başka bir katılımcının harekete başlamasına neden olabilir."}],"source_phrase_ar":"البعث الإرسال كبعث الله من في القبور (ayn)؛ بعثت الرجل في الحاجة وبعثته على الشيء إذا أرغته أن يفعله (jamhara)؛ ابتعثه بمعنى أي أرسله (sihah)؛ البعث بعث الجند إلى العدو والقوم المبعوثون المشخصون (tahdhib)؛ بعث الإنسان في حاجة وفبعث الله غرابا أي قيضه ولقد بعثنا في كل أمة رسولا نحو أرسلنا رسلنا (mufradat)","source_summary":"Kaynaklar, bir kişi ya da topluluğu bir ihtiyaç veya hedef doğrultusunda gönderme anlamında birleşir; bir işi yaptırmaya yöneltme ile gönderilmiş topluluğun adı bu çekirdekten gelişen kullanımlardır.","sources":["AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه إرسال الرجل أو الرسول أو البعير أو الجند إلى حاجة أو وجه، والقوم أو الجيوش المبعوثون.","what_is_not_ar":"ليس إحياء الموتى؛ ولا الانبعاث الذاتي في السير إلا إذا كان المقصود إرسالا من باعث."},"support_links":["sup_31a285eb0e42c6aa5667"]},{"boundary":"Bu dal hareket eden öznenin yola koyulup ilerlemesini anlatır; dışarıdan uyandırma veya görevle gönderme şartı taşımaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000129/B004","candidate_links":[{"candidate_id":"cand_799f693bf34de874f5aa","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ٱنۢبَعَثَ","morph_features":"STEM|POS:V|PERF|(VII)|LEM:{n[baEava|ROOT:bEv|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:12:2:1","qac_word_ref":"91:12:2","surface_ar":"ٱنۢبَعَثَ"}],"gloss":"yola koyulup ilerleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hareket eden özne yola koyulur, bir yöne yönelir ve ilerler."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir topluluğun iyi veya kötü bir iş doğrultusunda üyeleri art arda harekete geçip ilerleyebilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yolculuk bağlamında ilerleme hız kazanma ve çabuk gitme biçiminde gerçekleşebilir."}}],"root_ar":"ب ع ث","root_id":"root_000129","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Öznenin harekete geçerek bir yöne yöneldiği, ilerlediği ve bağlama göre art arda ya da hızlı hareket ettiği dalın bütünü için kullanılır.","boundary_detail":"Bu dal hareket eden öznenin yola koyulup ilerlemesini anlatır; dışarıdan uyandırma veya görevle gönderme şartı taşımaz.","branch_image_ar":"اندفاع القوم ومضيهم","concept_gloss":"yola koyulup ilerleme","contextual_glosses":[{"applicability":"Bir topluluğun iyi ya da kötü bir iş doğrultusunda üyeleri art arda ilerlediğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek öznenin genel yönelip gitmesi ile yolculukta hızlanma kullanımlarını dışarıda bırakır.","preserves":"Topluca harekete başlama ve birbirini izleyerek ilerleme özelliklerini korur."},"facet_ids":["F001","F002"],"text":"peş peşe harekete geçme","usage_role":"contextual"},{"applicability":"Bir kişi veya topluluğun yolculuk sırasında çabuk gittiği bağlamda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hız şartı taşımayan genel yola koyulmayı ve topluluğun art arda hareketini vermez.","preserves":"Yönlü hareketi, ilerlemeyi ve hız kazanmayı korur."},"facet_ids":["F001","F003"],"text":"hızla ilerleme","usage_role":"contextual"}],"definition":"Bir kişi ya da topluluğun harekete geçip belirli bir yönde yola koyulması ve ilerlemesidir. Bağlama göre toplulukların iyi veya kötü bir işte art arda harekete geçmesini, yönelip gitmesini ya da yolculukta hızlanmasını kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hareket eden özne yola koyulur, bir yöne yönelir ve ilerler."},{"facet_id":"F002","role":"specialization","statement":"Bir topluluğun iyi veya kötü bir iş doğrultusunda üyeleri art arda harekete geçip ilerleyebilir."},{"facet_id":"F003","role":"specialization","statement":"Yolculuk bağlamında ilerleme hız kazanma ve çabuk gitme biçiminde gerçekleşebilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Hareketi başlatan dışarıdaki bir göndericiyi ve edilgen görevlendirme ilişkisini ekler.","collision":"Aynı kökün görevle gönderme dalıyla karışır.","fit":"displacement","loses":"Öznenin kendi hareketi olarak yola koyulma, art arda ilerleme ve hızlanma özelliklerini vermez.","preserves":"Bir yöne doğru hareket etme sonucunu kısmen korur."},"text":"gönderilme"}],"identity_rationale":"Kaynak ifadesi, hareket eden öznenin yola koyulmasını ve ilerlemesini ortaklaştırır; topluluğun iyi ya da kötü bir işte art arda harekete geçmesi, yolculukta hızlanma ve bir yöne dönüp ilerleme bu hareketin bağlamsal biçimleridir. Bu nedenle dal dışarıdan gönderilme olarak değil, öznenin gerçekleşen hareketi olarak tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"harekete geçip ilerlemek; hızlanmak"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yola koyulma ve ilerleme"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"şiir benden akıp geldi"}],"lexicalization_note":"Tanım ilerleme çekirdeğini korurken topluca art arda hareket etme ve yolculukta hızlanma özelliklerini kendi kullanımlarına bağlar; şiirin akışı ayrı bir aktarmalı birimdir.","neighbor_coverage_note":"Verilen bütün komşular değerlendirildi; yola koyulup ilerleme sınırını dıştan gönderme, hedefe atılma, genel gitme, hızlı geri dönüş ve dıştan harekete geçirmeden ayıran beş karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal hareketi öznenin ilerleyişi açısından kurar; komşu dal ise gönderici ile gönderilen arasındaki ettirgen görev ilişkisini kurar.","focus_only":"Hareket eden öznenin yola koyulmasını ve gerçekleşen ilerleyişini anlatır.","gloss":"görevlendirip göndermek","neighbor_only":"Bir göndericinin başka bir katılımcıyı görev veya hedef için yollamasını anlatır.","neighbor_ref":"root_000129/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir katılımcının belirli bir yöne doğru hareket etmesiyle sonuçlanabilir."},{"boundary_match":"partial","distinction":"Bu dal yola koyulma ve süren ilerleyiş üzerinde durur; komşu dal ise atılma yanında hedefe ulaşma ve yolun sona ermesi gibi sonuçları da içeren daha geniş bir hareket alanına sahiptir.","focus_only":"Topluluğun iyi veya kötü bir işte art arda harekete geçmesi özelliğini kapsar.","gloss":"bir hedefe doğru atılıp ilerleme","neighbor_only":"Bir hedefe varma, yolun bir yerde sona ermesi ve hareketin başka nesnelere aktarılması gibi sonuç kapsamları taşır.","neighbor_ref":"root_000480/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da harekete geçmeyi, bir yönde ilerlemeyi ve yolculukta hızlanmayı anlatabilir."},{"boundary_match":"partial","distinction":"Komşu dal genel gitme ve geçmedir; bu dal ise yola koyulma başlangıcını ve kimi bağlamlarda birbirini izleyen ya da hızlanan hareketi belirginleştirir.","focus_only":"Harekete başlama ile bağlama göre art arda ilerleme veya hızlanmayı belirtir.","gloss":"gitme ve geçip ilerleme","neighbor_only":"Başlangıç, sıra veya hız şartı olmadan genel olarak gitme, geçme ve geride kalmayı kapsar.","neighbor_ref":"root_000522/B006","relation_type":"near_synonym","shared_zone":"Her iki dalda da özne bulunduğu yerden ayrılarak hareketini sürdürür ve ilerler."},{"boundary_match":"partial","distinction":"Bu dalda geri dönüş kurucu değildir ve hareket ileri yönlü ilerleme olarak sunulur; komşu dal hızlı gidişi geri dönme veya yön değiştirme sonucuyla birleştirebilir.","focus_only":"İyi veya kötü bir işte art arda ilerlemeyi ve yönelip gitmeyi kapsar.","gloss":"hızla gidip geri dönme","neighbor_only":"Hızlı gidiş yanında geri dönme veya boyun eğerek yön değiştirme anlamını taşıyabilir.","neighbor_ref":"root_000892/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişi veya topluluğun çabuk biçimde hareket edip gitmesini anlatabilir."},{"boundary_match":"partial","distinction":"Bu dal başlayan hareketi öznenin ilerleyişi olarak anlatır; komşu dal ise bu başlangıcı yaptıran dış etkeni ve onun uyarıcı müdahalesini gerektirir.","focus_only":"Öznenin kendisinin yola koyulup ilerlemesini bildirir.","gloss":"dışarıdan harekete geçirme","neighbor_only":"Dışarıdaki bir etkenin durgun, bağlı, çökmüş veya uyuyan varlığı etkinleştirmesini bildirir.","neighbor_ref":"root_000129/B001","relation_type":"near_neighbor","shared_zone":"Durgunluktan hareketli duruma geçiş ve hareketin başlaması her iki dalda da bulunabilir."}],"source_phrase_ar":"انبعث القوم في الخير والشر انبعاثا إذا تتابعوا (jamhara)؛ انبعث في السير أي أسرع (sihah)؛ كره الله انبعاثهم أي توجههم ومضيهم (mufradat)","source_summary":"Kaynaklar, öznenin yönelip ilerlemesi anlamında birleşir; topluluğun art arda harekete geçmesi ve yolculukta hızlanma, bu ilerleme çekirdeğinin belirgin bağlamsal biçimleridir.","sources":["JA","SI","MU"],"what_is_ar":"يدخل فيه انبعاث القوم في خير أو شر، والإسراع في السير، والتوجه والمضي.","what_is_not_ar":"ليس إرسالا من باعث خارجي؛ ولا بعث الموتى؛ ولا إثارة بعير أو نائم إلا إذا وصف الانبعاث الناتج."},"support_links":["sup_fcdfd00ae2b0ea1c1510"]},{"boundary":"Dal, her türlü yorgunluğu değil, mutluluğun karşıtı sayılan mutsuzluk durumunu anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000808/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَشْقَى","morph_features":"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"91:12:3:1","qac_word_ref":"91:12:3","surface_ar":"أَشْقَىٰ"}],"gloss":"mutluluğun karşıtı olan mutsuzluk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, mutluluğun karşıtı olan mutsuzluk ve bahtsızlık durumudur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu durum hem bu dünyadaki yaşam hem de ölümden sonraki yaşam bakımından değerlendirilebilir."}}],"root_ar":"ش ق و","root_id":"root_000808","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın temel durum anlamını, sıradan yorgunlukla karıştırmadan genel olarak karşılar.","boundary_detail":"Dal, her türlü yorgunluğu değil, mutluluğun karşıtı sayılan mutsuzluk durumunu anlatır.","branch_image_ar":"الشقاء ضد السعادة","concept_gloss":"mutluluğun karşıtı olan mutsuzluk","contextual_glosses":[{"applicability":"Mutsuzluk durumunun bu dünyadaki yaşam ve yaşantılar bakımından ele alındığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ölümden sonraki yaşama ilişkin kapsamı dışarıda bırakır.","preserves":"Mutluluğun karşıtı olan olumsuz yaşam durumu korunur."},"facet_ids":["F001","F002"],"text":"bu dünyadaki bahtsızlık","usage_role":"contextual"},{"applicability":"Mutsuzluk durumunun ölümden sonraki yaşam bakımından değerlendirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bu dünyadaki yaşama ilişkin kapsamı dışarıda bırakır.","preserves":"Mutluluğun karşıtı olma ve ölüm sonrası kapsam birlikte korunur."},"facet_ids":["F001","F002"],"text":"ölümden sonraki yaşamda mutsuzluk","usage_role":"contextual"}],"definition":"Mutluluğun karşıtı olan mutsuzluk ya da bahtsızlık durumudur. Bu durum kişinin bu dünyadaki yaşamına da ölümden sonraki yaşamına da ilişkin olabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, mutluluğun karşıtı olan mutsuzluk ve bahtsızlık durumudur."},{"facet_id":"F002","role":"extension","statement":"Bu durum hem bu dünyadaki yaşam hem de ölümden sonraki yaşam bakımından değerlendirilebilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Mutluluğun karşıtı olmayan sıradan bedensel ya da zihinsel yorulmayı da kapsar.","collision":"Güçlük ve yorucu uğraş dalıyla anlam karışmasına yol açar.","fit":"broadening","loses":null,"preserves":"Olumsuz ve güçlük içeren bir yaşantı çağrışımını korur."},"text":"yorgunluk"}],"identity_rationale":"Yetkili kaynak ifadesi bu dalı doğrudan mutluluğun karşıtı olan durum diye belirler ve bu durumun hem bu dünyadaki yaşamda hem de ölümden sonraki yaşamda söz konusu olabileceğini bildirir. Bu nedenle verilen dal kimliği kaynak ifadesinin çekirdeğini ve kapsam ayrımını doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"mutsuzluk, bahtsızlık"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"mutsuz, bahtsız kimse"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"Tanrı onu mutsuzluğa düşürdü"}],"lexicalization_note":"Tanım, durum bildiren biçimlerin ortak anlamını temel alır; birini bu duruma sokma anlamı ise yalnızca ilgili ettirgen söyleyişe bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca güçlük dalı okur açısından doğrudan ve anlamlı bir sınır karşılaştırması sağladı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın ölçütü mutluluğun karşıtı bir durumda bulunmaktır; komşu dalın ölçütü ise bir zorlukla uğraşmak, yorulmak ya da ona dayanmaktır. Bu yüzden her güçlük mutsuzluk sayılmaz.","focus_only":"Mutluluğun karşıtı olan genel yaşam durumunu ve iki yaşam alanındaki kapsamını belirtir.","gloss":"mutsuzluk ile güçlük çekme","neighbor_only":"Güçlük, yorulma, dayanma ve zorlu bir işle ya da kişiyle uğraşma anlamlarını kapsar.","neighbor_ref":"root_000808/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da olumsuz, yorucu ve kişiyi zorlayan bir yaşantı alanında buluşur."}],"source_phrase_ar":"الشقوة خلاف السعادة (maqayis)؛ الشقاء والشقاوة بالفتح: نقيض السعادة (sihah)؛ الشقاوة: خلاف السعادة، والشقاوة الأخروية والدنيوية (mufradat)","source_summary":"Kaynakların ortak çizgisi, anlamı mutluluğun karşıtı olan bir durum olarak kurar; kapsam, bu dünyadaki ve ölümden sonraki yaşamda görülen mutsuzluğu içerir.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه الشقاء والشقوة والشقاوة بمعنى نقيض السعادة، وما يذكر في الشقاوة الأخروية والدنيوية.","what_is_not_ar":"لا يدخل مجرد التعب من حيث هو تعب أعم من الشقاوة، ولا المعنى المهموز شقأ ناب البعير."},"support_links":[]},{"boundary":"Dal, güçlük çekme çekirdeğiyle karşılıklı uğraşma kullanımlarını ayırır; her yorgunluğu ya da sonradan gelen yenme sonucunu kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000808/B002","candidate_links":[{"candidate_id":"cand_04ed7a4291c3ed4a5fb8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَشْقَى","morph_features":"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"91:12:3:1","qac_word_ref":"91:12:3","surface_ar":"أَشْقَىٰ"}],"gloss":"güçlük çekme ve zorluğa dayanma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, kolaylığın karşıtı olan güçlüğü çekmek ve zorluğa katlanmaktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Anlam yorgunluk yerine kullanılabilir; ancak her yorgunluk bu ölçüde bir güçlük çekme değildir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişiyle sabırla uğraşma, bir işi göğüsleme veya savaşta boğuşma yapıya bağlı kullanımlardır."}}],"root_ar":"ش ق و","root_id":"root_000808","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kolaylığın karşıtı olan uğraşma çekirdeğini, yapıya bağlı özel kullanımları genelleştirmeden karşılar.","boundary_detail":"Dal, güçlük çekme çekirdeğiyle karşılıklı uğraşma kullanımlarını ayırır; her yorgunluğu ya da sonradan gelen yenme sonucunu kapsamaz.","branch_image_ar":"مشقة العسر والمعاناة","concept_gloss":"güçlük çekme ve zorluğa dayanma","contextual_glosses":[{"applicability":"Güçlüğün kişide belirgin bir yorgunluk ve sıkıntı doğurduğu bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişiyle ya da işle sabırla uğraşma ve savaşta boğuşma kapsamını vermez.","preserves":"Güçlük çekmenin yorucu ve sıkıntılı yönünü korur."},"facet_ids":["F001","F002"],"text":"sıkıntı çekip yorulma","usage_role":"contextual"},{"applicability":"Bir kişiyle veya zorlu bir işle sürdürülmüş uğraşı ve sabrı öne çıkaran bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel güçlük durumu ile sırf yorulma kullanımını geri plana iter.","preserves":"Süreğen uğraşma ve zorluğa dayanma yönlerini korur."},"facet_ids":["F001","F003"],"text":"uğraşıp dayanma","usage_role":"contextual"},{"applicability":"Karşılıklı zorlu uğraşın savaş alanında gerçekleştiği özel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Savaş dışındaki güçlük, yorulma ve dayanma kullanımlarını dışarıda bırakır.","preserves":"Karşılıklı uğraşma ve güçlüğü göğüsleme yönlerini korur."},"facet_ids":["F003"],"text":"savaşta boğuşma","usage_role":"contextual"}],"definition":"Kolaylığın karşıtı olan güçlükle uğraşma, bunun sıkıntısını çekme ve ona dayanma durumudur. Kişiyle, işle ya da savaş gibi zorlu bir süreçle karşılıklı ve sürekli uğraşma bu çekirdeğin yapıya bağlı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, kolaylığın karşıtı olan güçlüğü çekmek ve zorluğa katlanmaktır."},{"facet_id":"F002","role":"specialization","statement":"Anlam yorgunluk yerine kullanılabilir; ancak her yorgunluk bu ölçüde bir güçlük çekme değildir."},{"facet_id":"F003","role":"associated_use","statement":"Bir kişiyle sabırla uğraşma, bir işi göğüsleme veya savaşta boğuşma yapıya bağlı kullanımlardır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Güçlükle bağlı olmayan sıradan bedensel ya da zihinsel yorulmayı da kapsar.","collision":"Dalın kolaylığın karşıtı olan uğraşma ve dayanma ölçütünü belirsizleştirir.","fit":"broadening","loses":null,"preserves":"Güçlüğün kişide bıraktığı yorucu etkiyi korur."},"text":"yalnızca yorgunluk"},{"category":"confusable","error_profile":{"adds":"Sürecin ardından gelen üstün gelme sonucunu temel anlam yapar.","collision":"Aynı kökün üstün gelme dalıyla karışır.","fit":"displacement","loses":"Güçlük çekme, uğraşma ve dayanma sürecini ortadan kaldırır.","preserves":"Karşılıklı bir uğraş veya çekişme ortamını dolaylı olarak çağrıştırır."},"text":"yenme"}],"identity_rationale":"Yetkili kaynak ifadesi anlam çekirdeğini uğraşma ve kolaylığın karşıtı olarak verir; ayrıca şiddetli güçlük, yorulma, dayanma, bir işi göğüsleme ve savaşta boğuşma kullanımlarını açıkça sıralar. Verilen dal kimliği bu öğeleri korur ve sıradan yorgunluk ile daha dar kapsamlı mutsuzluk arasındaki sınırı belirtmeye elverişlidir.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"güçlük, sıkıntı ve yorucu uğraş"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bu işte yoruldum ve güçlük çektim"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"zorluğa katlanma, uğraşıp dayanma ve savaşta boğuşma"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"onunla uğraştım ve güçlüğüne katlandım"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"o işle uğraşıp güçlüğünü çektim"}],"lexicalization_note":"Genel güçlük ve yorulma anlamı biçim düzeyinde korunur; kişiyle çekişme, bir işe katlanma ve savaşta boğuşma anlamları yalnızca ilgili yapılı söyleyişlere bağlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; eş anlamlı olan dal ile süreç, kapsam veya sonuç sınırını aydınlatan üç aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kartlarda çekirdek, katılımcılar ve kapsam bakımından ayırıcı bir sınır görünmez; bu nedenle iki dal eş anlamlı değerlendirilir.","focus_only":null,"gloss":"güçlük, sıkıntı ve uğraşma","neighbor_only":null,"neighbor_ref":"root_000809/B002","relation_type":"synonym","shared_zone":"İki dal da şiddetli güçlük, yorulma ve bir işi uğraşarak göğüsleme alanını aynı sınırlarla kapsar."},{"boundary_match":"partial","distinction":"Bu dal güçlüğe katlanmayı ve kimi yapılarda karşılıklı uğraşmayı kapsar; komşu dal ise bir işin ya da yolun kişiye ağır gelmesini ve yoğun çabayla aşılmasını öne çıkarır.","focus_only":"Kişiyle karşılıklı uğraşma, sabırla dayanma ve savaşta boğuşma gibi yapıya bağlı kullanımları da kapsar.","gloss":"güçlük çekme ile ağır çaba","neighbor_only":"Yolda, işte veya bir amaca ulaşmada kişinin iç dünyasına ağır gelen yük ve çabayı öne çıkarır.","neighbor_ref":"root_000807/B003","relation_type":"near_synonym","shared_zone":"Her iki dalda da işin kolay olmayışı, çaba ve kişiye yük olan güçlük bulunur."},{"boundary_match":"partial","distinction":"Bu dal kolaylığın karşıtı olan daha geniş güçlük alanını ve karşılıklı uğraşı da içerir; komşu dalın odağı ise özellikle çetin bir işi göğüslemektir.","focus_only":"Genel güçlük ve yorulma durumuyla kişiyle karşılıklı uğraşma kapsamını içerir.","gloss":"zorluğa dayanma ile çetin işi göğüsleme","neighbor_only":"Özellikle şiddetli bir işi göğüsleyip onun eziyetine dayanmayı merkez alır.","neighbor_ref":"root_001227/B003","relation_type":"near_synonym","shared_zone":"İki dal da zor bir işi yaşayarak sürdürme ve onun yüküne katlanma anlamında örtüşür."},{"boundary_match":"partial","distinction":"Bu dal sürecin güçlüğünü ve dayanmayı, komşu dal ise o süreçte üstün gelme sonucunu kodlar; süreç sonucu zorunlu olarak içermez.","focus_only":"Zorlu uğraşın sürmesi, çekilmesi ve ona dayanılması sürecini anlatır.","gloss":"uğraşma süreci ile yenme sonucu","neighbor_only":"Karşılıklı uğraşın sonunda öteki kişiyi yenme sonucunu anlatır.","neighbor_ref":"root_000808/B003","relation_type":"near_neighbor","shared_zone":"İki dal aynı karşılıklı ve zorlu uğraş senaryosunun farklı aşamalarına bağlanır."}],"source_phrase_ar":"أصل يدل على المعاناة وخلاف السهولة (maqayis)؛ المشاقاة المعاناة والممارسة (maqayis;sihah)؛ الشقاء: الشدة والعسر، وشاقيته أي صابرته، وشاقيت ذلك الأمر بمعنى عانيته، والمشاقاة: المعالجة في الحرب وغيرها (tahdhib)؛ يوضع الشقاء موضع التعب، وكل شقاوة تعب وليس كل تعب شقاوة (mufradat)","source_summary":"Kaynakların birleşen anlatımı, kolaylığın karşısındaki güçlük ve uğraşma çekirdeğini; yorulma, dayanma, işi göğüsleme ve savaşta boğuşma gibi bağlı gerçekleşmelerle birlikte verir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الشقاء بمعنى الشدة والعسر والتعب، والمشاقاة بمعنى المعاناة والممارسة والصبر والمعالجة في الحرب وغيرها، وعشرة المرء غيره في هذا الباب.","what_is_not_ar":"لا يدخل نقيض السعادة إذا كان المقصود حكما وجوديا أو أخرويا خالصا، ولا الغلبة بعد المشاقاة."},"support_links":["sup_1c7fc6154f1a05447e6d"]},{"boundary":"Anlam, herhangi bir yenmeye değil, belirtilen karşılıklı uğraş yapısında ötekine üstün gelmeye bağlıdır.","branch_kind":"collocation","branch_ref":"root_000808/B003","candidate_links":[{"candidate_id":"cand_18293f7ae42e34ddee49","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَشْقَى","morph_features":"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"91:12:3:1","qac_word_ref":"91:12:3","surface_ar":"أَشْقَىٰ"}],"gloss":"karşılıklı uğraşta ötekini yenme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Karşılıklı uğraşın sonunda konuşan, öteki kişiye aynı uğraş alanında üstün gelir."}}],"root_ar":"ش ق و","root_id":"root_000808","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kaynakta verilen ardışık karşılıklı uğraş ve üstün gelme yapısını tam olarak karşılar.","boundary_detail":"Anlam, herhangi bir yenmeye değil, belirtilen karşılıklı uğraş yapısında ötekine üstün gelmeye bağlıdır.","branch_image_ar":"الغلبة في المشاقاة","concept_gloss":"karşılıklı uğraşta ötekini yenme","contextual_glosses":[{"applicability":"Yapının iki katılımcısını ve uğraştan üstün gelmeye uzanan sırasını açıkça göstermek gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki katılımcı, karşılıklı çekişme ve konuşanın yenmesi tam olarak korunur."},"facet_ids":["F001"],"text":"benimle çekişti, ben de onu yendim","usage_role":"explanatory"}],"definition":"Bir kişinin konuşanla belirli bir uğraş alanında çekişmesinin ardından konuşanın onu aynı alanda yenmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Karşılıklı uğraşın sonunda konuşan, öteki kişiye aynı uğraş alanında üstün gelir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Aynı kökün güçlük ve uğraşma dalıyla karışır.","fit":"narrowing","loses":"Konuşanın öteki kişiyi aynı alanda yenmesi sonucunu vermez.","preserves":"Karşılıklı sürecin uğraş ve çekişme yönünü korur."},"text":"uğraşma"}],"identity_rationale":"Yetkili kaynak ifadesi, bir kişinin konuşana aynı uğraş alanında karşılık vermesini ve konuşanın onu o alanda yenmesini açıkça ardışık bir yapı içinde verir. Verilen dal kimliği bu sonucu doğru biçimde yakalar ve onu yalnızca uğraşma sürecinden ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"benimle çekişti, ben de o işte onu yendim"}],"lexicalization_note":"Tanım yalnızca birinin konuşanla belirli bir alanda uğraşması ve konuşanın onu aynı alanda yenmesi biçimindeki yapıya bağlıdır; yalın kök anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; süreç dalı, tam eş anlamlı yapı ve daha genel üstün gelme dalı sınırı açıklayan adaylar olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal uğraşın üstün gelmeyle biten sonucudur; komşu dal ise uğraşın ve dayanmanın kendisidir, dolayısıyla yenmeyi gerektirmez.","focus_only":"Karşılıklı uğraşta konuşanın öteki kişiyi yenmesi sonucunu kodlar.","gloss":"yenme sonucu ile uğraşma süreci","neighbor_only":"Güçlük çekme, karşılıklı uğraşma ve zorluğa dayanma sürecini sonuçtan bağımsız anlatır.","neighbor_ref":"root_000808/B002","relation_type":"near_neighbor","shared_zone":"İki dal da aynı zorlu ve karşılıklı uğraş senaryosuna katılır."},{"boundary_match":"exact","distinction":"Verilen kartlara göre işlem sırası, katılımcılar ve sonuç bakımından ayırıcı bir sınır yoktur; iki yapı aynı kavramsal içeriği taşır.","focus_only":null,"gloss":"karşılıklı uğraşta yenme","neighbor_only":null,"neighbor_ref":"root_000569/B005","relation_type":"synonym","shared_zone":"İki dal da belirli bir alandaki karşılıklı uğraşın konuşanın ötekini yenmesiyle sonuçlanmasını anlatır."},{"boundary_match":"partial","distinction":"Bu dal yalnızca belirtilen karşılıklı uğraş yapısında işler; komşu dal ise üstün gelmeyi ve kazanmayı böyle bir ön koşul olmadan daha genel biçimde kapsar.","focus_only":"Yenme anlamını belirli bir karşılıklı uğraşı önceleyen ve konuşanı galip yapan yapıya bağlar.","gloss":"yapıya bağlı yenme ile genel zafer","neighbor_only":"Zafer, ele geçirme ve rakibi alt etme sonucunu daha genel bir kapsamda anlatır.","neighbor_ref":"root_000965/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir rakibe üstün gelme ve onu yenme sonucu vardır."}],"source_phrase_ar":"شاقاني فلان فشقوته أشقوه، أي غلبته فيه (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak tanıklığı, birinin konuşanla uğraşmasını ve konuşanın onu aynı alanda yenmesini ardışık olarak verir."}],"source_summary":"Dal, karşılıklı uğraşın kendisini değil, bu uğraşın konuşanın üstün gelmesiyle sonuçlanan aşamasını anlatır.","sources":["SI"],"what_is_ar":"يدخل فيه قولهم شاقاني فلان فشقوته، أي غلبته في ذلك الباب.","what_is_not_ar":"لا يدخل أصل المعاناة والممارسة بلا معنى الغلبة."},"support_links":["sup_31a285eb0e42c6aa5667"]},{"boundary":"Dal genel olarak her yüksek dağı değil, uzun, kolay çıkılan ve oturmaya elverişli belirli bir dağ sırtını anlatır.","branch_kind":"bare","branch_ref":"root_000808/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَشْقَى","morph_features":"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"91:12:3:1","qac_word_ref":"91:12:3","surface_ar":"أَشْقَىٰ"}],"gloss":"uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderge, dağın yükselen ve uzun bir sırtıdır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Uzunluğuna karşın bu sırtın çıkışı görece kolaydır."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sırt, insanın oturmasına daha elverişli bir yer sağlar."}}],"root_ar":"ش ق و","root_id":"root_000808","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yer biçimini, uzunluğunu, çıkılabilirliğini ve oturma elverişliliğini birlikte karşılar.","boundary_detail":"Dal genel olarak her yüksek dağı değil, uzun, kolay çıkılan ve oturmaya elverişli belirli bir dağ sırtını anlatır.","branch_image_ar":"شاقي الجبل الطالع الطويل","concept_gloss":"uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı","contextual_glosses":[{"applicability":"Yol alma ve tırmanma kolaylığının öne çıktığı bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsanın oturmasına elverişli olma niteliğini belirtmez.","preserves":"Dağ sırtı olma, uzunluk ve kolay çıkış niteliklerini korur."},"facet_ids":["F001","F002"],"text":"çıkması kolay uzun dağ sırtı","usage_role":"contextual"},{"applicability":"Bir insanın durup oturabileceği yer niteliğinin öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sırtın uzunluğunu ve çıkışının görece kolay oluşunu tam belirtmez.","preserves":"Dağ sırtı olma, yükselme ve oturmaya elverişlilik niteliklerini korur."},"facet_ids":["F001","F003"],"text":"oturmaya elverişli yüksek dağ sırtı","usage_role":"contextual"}],"definition":"Dağın yükselen ve uzun bir sırtıdır; uzun olmasına karşın çıkılması görece kolaydır ve insana oturmak için elverişli bir yer sağlar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderge, dağın yükselen ve uzun bir sırtıdır."},{"facet_id":"F002","role":"core","statement":"Uzunluğuna karşın bu sırtın çıkışı görece kolaydır."},{"facet_id":"F003","role":"core","statement":"Sırt, insanın oturmasına daha elverişli bir yer sağlar."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Sırt olmayan ve çıkışı ya da oturma elverişliliği belirtilmeyen her yüksek dağı kapsar.","collision":"Genel yükseklik bildiren dağ dallarıyla karışır.","fit":"broadening","loses":null,"preserves":"Dağlık yer ve yükselti özelliklerini genel olarak korur."},"text":"yüksek dağ"}],"identity_rationale":"Yetkili kaynak ifadesi dağ sırtının yükselen ve uzun olduğunu, uzunluğuna karşın çıkışının daha kolay ve insanın oturmasına daha elverişli bulunduğunu açıkça belirtir. Verilen dal kimliği bu dört kurucu niteliği ve yer biçimini doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı; bu tür dağ sırtları"}],"lexicalization_note":"Tanım, tek başına kullanılan dağ sırtı adının niteliklerini verir; başka bir yapıya bağlı anlam veya öteki dalların soyut anlamları içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eş anlamlı dal, genel yükseklik ve dağın bütünü ya da orta kesimi en açıklayıcı karşılaştırmaları sağladı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kartlarda gönderge, nitelikler ve kapsam bakımından ayırıcı bir sınır bulunmadığından iki dal eş anlamlıdır.","focus_only":null,"gloss":"uzun ve kolay çıkılan dağ sırtı","neighbor_only":null,"neighbor_ref":"root_000809/B004","relation_type":"synonym","shared_zone":"İki dal da uzun, yükselen, çıkışı kolay ve insanın oturmasına elverişli aynı dağ sırtı türünü anlatır."},{"boundary_match":"partial","distinction":"Bu dal somut bir dağ sırtı türüdür ve erişim ile oturma niteliklerini gerektirir; komşu dal ise nesne türünü ve bu ek nitelikleri sınırlamayan genel yüksekliktir.","focus_only":"Belirli bir dağ sırtını uzunluk, kolay çıkış ve oturma elverişliliğiyle birlikte tanımlar.","gloss":"özel dağ sırtı ile genel yükseklik","neighbor_only":"Dağ veya başka bir varlıktaki yükselme ve uzunluğu genel olarak belirtir.","neighbor_ref":"root_000824/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da yükselme ve uzunluk niteliği bulunur."},{"boundary_match":"field_only","distinction":"Bu dal biçimi ve kullanım elverişliliği belirlenmiş bir sırtı anlatır; komşu dal ise bütün dağı ya da dağın orta kesimini gösterir.","focus_only":"Uzun, çıkışı kolay ve oturmaya elverişli bir dağ sırtı türünü gösterir.","gloss":"dağ sırtı ile dağ ve orta kesimi","neighbor_only":"Dağın kendisini veya dağların orta kesimini adlandırır.","neighbor_ref":"root_000840/B017","relation_type":"same_field","shared_zone":"İki dal da dağlık araziyi ve dağın bölümlerini adlandıran aynı kavram alanındadır."}],"source_phrase_ar":"الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان والجميع شاقيات وشواقي (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak tanıklığı bu sırtı yükselen ve uzun, fakat çıkışı kolay ve insanın oturmasına elverişli olarak niteler."}],"source_summary":"Dal, biçimsel ve kullanımsal nitelikleri birlikte verilen özel bir dağ sırtı türünü anlatır.","sources":["AY"],"what_is_ar":"يدخل فيه الشاقي من حيود الجبال: الطالع الطويل الذي، مع طوله، يكون أيسر صعودا وأقدر مقعدا للإنسان، وجمعه شاقيات وشواقي.","what_is_not_ar":"لا يدخل الشقاء بمعنى ضد السعادة، ولا المشاقاة والمعاناة."},"support_links":[]},{"boundary":"Dal, her türlü yorgunluğu veya güçlüğü değil, mutluluğun karşıtı olan durumu ve bu duruma düşürmeyi anlatır.","branch_kind":"bare","branch_ref":"root_000809/B001","candidate_links":[{"candidate_id":"cand_799f693bf34de874f5aa","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَشْقَى","morph_features":"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"91:12:3:1","qac_word_ref":"91:12:3","surface_ar":"أَشْقَىٰ"}],"gloss":"bedbahtlık ve bedbaht duruma düşürme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kimsenin mutluluğun karşıtı olan bedbaht bir durumda bulunmasıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ettirgen kullanımda bir kimseyi bedbaht duruma düşürmeyi anlatır."}}],"root_ar":"ش ق و","root_id":"root_000809","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem durum bildiren çekirdeğini hem de aynı anlam alanındaki ettirgen uzantısını birlikte karşılar.","boundary_detail":"Dal, her türlü yorgunluğu veya güçlüğü değil, mutluluğun karşıtı olan durumu ve bu duruma düşürmeyi anlatır.","branch_image_ar":"الشقاوة وخلاف السعادة","concept_gloss":"bedbahtlık ve bedbaht duruma düşürme","contextual_glosses":[{"applicability":"Bir kişinin mutluluğun karşıtı olan durumunu adlandıran bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin mutluluğun karşıtı olan durumunu tam olarak korur."},"facet_ids":["F001"],"text":"bedbahtlık","usage_role":"general"},{"applicability":"Birinin başka birini bu olumsuz duruma soktuğu ettirgen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir kimseyi bedbaht duruma sokma işlemini açıkça korur."},"facet_ids":["F002"],"text":"bedbaht duruma düşürmek","usage_role":"contextual"}],"definition":"Mutluluğun karşıtı olan bedbahtlık durumu ve bir kimseyi bu duruma düşürmedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kimsenin mutluluğun karşıtı olan bedbaht bir durumda bulunmasıdır."},{"facet_id":"F002","role":"extension","statement":"Ettirgen kullanımda bir kimseyi bedbaht duruma düşürmeyi anlatır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bedensel veya zihinsel yorulmanın genel anlamını ekler.","collision":"Güçlük ve yorulma dalıyla karışır.","fit":"displacement","loses":"Mutluluğun karşıtı olan kalıcı durum ile ettirgen uzantıyı kaybeder.","preserves":"Olumsuz bir insan deneyimini adlandırma özelliğini korur."},"text":"yorgunluk"}],"identity_rationale":"Kaynak ifadesi bu dalı mutluluğun karşıtı olan bedbahtlık durumu etrafında kurar; kişinin bu durumda bulunmasını ve bir başkasının onu bu duruma düşürmesini de aynı anlam alanına bağlar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bedbaht olmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bedbahtlık"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bedbahtlık"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bu dünyada veya ölümden sonraki yaşamda bedbahtlık"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"onu bedbaht duruma düşürmek"}],"lexicalization_note":"Yalın dal, bedbaht olma durumunu ve aynı kökten gelen ettirgen biçimi kapsar; güçlük ve yorulma dalındaki kullanımlar buraya taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca bedbahtlıkla anlam, neden veya sonuç bakımından gerçek karışma ihtimali taşıyan üç karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal mutluluğun karşıtı olan bedbahtlık durumudur; komşu dal ise özellikle üzüntüye, hoşnutsuzluğa ve istenmeyen bir sonuca yönelir.","focus_only":"Bedbahtlığı mutluluğun karşıtı olan genel bir durum olarak ve ettirgen uzantısıyla kapsar.","gloss":"üzüntü ve bedbahtlık","neighbor_only":"Üzüntü, hoşnutsuzluk ve istenmeyen bir durumun başa gelmesi üzerinde durur.","neighbor_ref":"root_000079/B003","relation_type":"near_synonym","shared_zone":"İkisi de kişinin ağır ve olumsuz ruhsal ya da yaşamsal durumunu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal bir kişinin mutluluk karşısındaki durumunu belirtir; komşu dal ise yaşanan işin zorluğunu ve harcanan çabayı öne çıkarır.","focus_only":"Mutluluğun karşıtı olan bedbahtlık durumunu ve birini bu duruma düşürmeyi anlatır.","gloss":"bedbahtlık ile güçlük","neighbor_only":"Güçlük, zorluk, yorulma ve bir işle uğraşıp ona katlanmayı anlatır.","neighbor_ref":"root_000809/B002","relation_type":"near_neighbor","shared_zone":"Ağır güçlükler bedbahtlıkla birlikte görülebilir ve iki dal bazı bağlamlarda birbirini çağrıştırır."},{"boundary_match":"field_only","distinction":"Bedbahtlık umut bulunup bulunmamasına bağlı değildir; komşu dalın çekirdeği ise beklentinin ve umudun sona ermesidir.","focus_only":"Mutluluğun karşıtı olan genel bedbahtlık durumunu kapsar.","gloss":"bedbahtlık ve umutsuzluk","neighbor_only":"Bir şeyden, iyilikten veya merhametten umut kesmeyi bildirir.","neighbor_ref":"root_001261/B001","relation_type":"same_field","shared_zone":"Her ikisi de kişinin olumsuz bir yaşamsal ya da ruhsal durumda bulunmasıyla ilgilidir."}],"source_phrase_ar":"الشقوة خلاف السعادة (maqayis)؛ شقي شقاء وشقوة وأصل الشقاء والشقوة (ayn)؛ الشقاء والشقاوة نقيض السعادة وأشقاه الله (sihah)؛ شقي شقاء وشقاوة وشقوة (tahdhib)؛ الشقاوة خلاف السعادة (mufradat)","source_summary":"Kaynakların ortak çekirdeği, mutluluğun karşıtı olan bedbahtlık ve bu durumda bulunan kişidir; ettirgen biçim de birini bu duruma düşürür.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الشقاء والشقوة والشقاوة وحال الشقي وإشقاؤه","what_is_not_ar":"ليس مطلق التعب الأعم ولا المعنى المهموز في شقأ ناب البعير"},"support_links":["sup_fcdfd00ae2b0ea1c1510"]},{"boundary":"Yalın güçlük anlamı ile belirli bir işte yorulma veya o işle uğraşma biçimleri ayrı tutulmalı; dal genel yorgunlukla özdeşleştirilmemelidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000809/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَشْقَى","morph_features":"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"91:12:3:1","qac_word_ref":"91:12:3","surface_ar":"أَشْقَىٰ"}],"gloss":"zorluk ve yorucu uğraş","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kolaylığın karşıtı olan güçlük, zorluk ve sıkıntıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yorgunluk anlamında da kullanılabilir, ancak genel olarak her yorgunluğu kapsamaz."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yalın olmayan biçimlerde belirli bir işi yaşayarak sürdürme, onunla uğraşma ve ona katlanmadır."}}],"root_ar":"ش ق و","root_id":"root_000809","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın güçlük çekirdeğini ve belirli bir işe bağlanan uğraşma ile katlanma biçimlerini birlikte özetler.","boundary_detail":"Yalın güçlük anlamı ile belirli bir işte yorulma veya o işle uğraşma biçimleri ayrı tutulmalı; dal genel yorgunlukla özdeşleştirilmemelidir.","branch_image_ar":"الشدة والعسر والعناء","concept_gloss":"zorluk ve yorucu uğraş","contextual_glosses":[{"applicability":"Yalın biçimin kolaylığın karşıtı olan durum veya deneyimi anlattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kolaylığın karşıtı olan zorlu ve sıkıntılı durumu korur."},"facet_ids":["F001"],"text":"güçlük ve sıkıntı","usage_role":"general"},{"applicability":"Belirli bir iş yüzünden yorulmayı veya o işte güçlük çekmeyi anlatan kullanımlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yorgunluğu belirli bir işte yaşanan güçlüğe bağlı olarak korur."},"facet_ids":["F002"],"text":"bir işte yorulmak","usage_role":"contextual"},{"applicability":"Yalın olmayan biçimin bir işi yaşayarak sürdürme ve onun güçlüğünü çekme anlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli bir işle uğraşma, onu sürdürme ve güçlüğüne katlanma öğelerini korur."},"facet_ids":["F003"],"text":"bir işle uğraşıp ona katlanmak","usage_role":"explanatory"}],"definition":"Kolaylığın karşıtı olan güçlük, zorluk ve bunların doğurduğu yorucu yaşantıdır. Yalın olmayan kullanımlarda belirli bir işle uğraşmayı, onu yaşayarak sürdürmeyi ve ona katlanmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kolaylığın karşıtı olan güçlük, zorluk ve sıkıntıdır."},{"facet_id":"F002","role":"source_variant","statement":"Yorgunluk anlamında da kullanılabilir, ancak genel olarak her yorgunluğu kapsamaz."},{"facet_id":"F003","role":"specialization","statement":"Yalın olmayan biçimlerde belirli bir işi yaşayarak sürdürme, onunla uğraşma ve ona katlanmadır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Her türlü yorgunluğun bu dala girdiği izlenimini verebilir.","fit":"narrowing","loses":"Kolaylık karşıtı güçlüğü ve belirli bir işle uğraşıp ona katlanma kapsamını kaybeder.","preserves":"Zorlu yaşantının yorucu yönünü korur."},"text":"yorgunluk"}],"identity_rationale":"Kaynak ifadesi güçlük, zorluk ve kolaylığın karşıtı olan yaşantıyı doğrular; ayrıca bir işle uğraşma ve ona katlanma biçimlerini verir. Bununla birlikte yorgunluk kullanımı sınırlıdır: bu kapsamdaki her durum yorucu olabilir, fakat her yorgunluk bu dala girmez.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"güçlük, zorluk ve yorucu sıkıntı"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir işte yorulmak veya güçlük çekmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"uğraşma, yaşayarak sürdürme ve katlanma"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bir işle uğraşmak ve ona katlanmak"}],"lexicalization_note":"Dal, yalın biçimde güçlük ve zorluğu; yalın olmayan biçimlerde ise belirli bir işte yorulmayı, o işi yaşayarak sürdürmeyi ve ona katlanmayı ayrı yüzler olarak kapsar.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yayımlanan üç yakın anlamlı dal, genel zorluk, kişiye ağır gelme ve ağır işe katlanma sınırlarını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel güçlükten belirli bir işle uğraşmaya uzanır; komşu dalın belirleyici yanı ise işin kişiye ağır gelmesi ve büyük güçlükle yapılmasıdır.","focus_only":"Güçlüğün yanı sıra belirli bir işle uğraşma, onu sürdürme ve ona katlanma biçimlerini kapsar.","gloss":"zorluk ve ağır gelme","neighbor_only":"Yürüyüşte veya işte insanın iç dünyasına ağır gelen yükü ve işi büyük güçlükle başarmayı vurgular.","neighbor_ref":"root_000807/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da çaba gerektiren, yorucu ve kolay olmayan bir deneyimi anlatır."},{"boundary_match":"partial","distinction":"Odak dal daha genel bir kolaylık karşıtlığına sahiptir; komşu dal ise ağır işin bizzat çekilmesini ve ona dayanmayı merkezleştirir.","focus_only":"Kolaylığın karşıtı olan genel güçlüğü ve bazı biçimlerde yorgunluğu kapsar.","gloss":"güçlük ve çetin işe katlanma","neighbor_only":"Ağır bir işi çekip katlanma ve onunla boğuşma yönünü daha belirgin taşır.","neighbor_ref":"root_001280/B002","relation_type":"near_synonym","shared_zone":"İki dal da zorluk, sıkıntı ve bir işi yaşayarak sürdürme alanında geniş ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Komşu dal genel zorluğu doğrudan niteler; odak dal ise bu zorluğun yaşanmasını, yorgunluğu ve işle uğraşmayı da kapsayan karma bir yapıya sahiptir.","focus_only":"Yorucu yaşantı ile belirli bir işle uğraşma ve ona katlanma uzantılarını içerir.","gloss":"güçlük ve zorluk","neighbor_only":"Zor bir işi veya zor bir günü, yaşanan çaba ve katlanma sürecini gerektirmeden niteleyebilir.","neighbor_ref":"root_001012/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın çekirdeğinde kolaylığın karşıtı olan güçlük ve zorluk bulunur."}],"source_phrase_ar":"أصل يدل على المعاناة وخلاف السهولة (maqayis)؛ المشاقاة المعاناة والممارسة (sihah)؛ الشقاء الشدة والعسر وشاقيت ذلك الأمر بمعنى عانيته (tahdhib)؛ يوضع الشقاء موضع التعب وكل شقاوة تعب وليس كل تعب شقاوة (mufradat)","source_summary":"Kaynakların ortak çerçevesi kolaylığın karşıtı olan güçlük ve zorluktur; buna yorucu yaşantı ile belirli bir işle uğraşma, onu sürdürme ve ona katlanma kullanımları eklenir. Yorgunlukla bağ kurulsa da her yorgunluk bu anlamı taşımaz.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الشدة والعسر والتعب الذي يسمى شقاء ومعاناة الأمر وممارسته","what_is_not_ar":"ليس التعب الأعم كله شقاوة ولا المعنى المهموز في شقأ ناب البعير"},"support_links":[]},{"boundary":"Dal yalnızca bir kişinin bedbahtlığı veya genel yorgunluk değildir; mutlaka başka bir kişiyle kurulan ilişki, dayanışma ya da karşılaşma yapısına bağlıdır.","branch_kind":"non_bare","branch_ref":"root_000809/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَشْقَى","morph_features":"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"91:12:3:1","qac_word_ref":"91:12:3","surface_ar":"أَشْقَىٰ"}],"gloss":"biriyle karşılıklı uğraşıp mücadele etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başka bir kişiyle karşılıklı ilişki ve uğraş içinde olmaktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karşı tarafa dayanma, onunla mücadele etme ve özellikle savaşta onunla uğraşmadır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Rekabetli kullanımda karşı tarafla çekişip onu söz konusu işte alt etmeye uzanır."}}],"root_ar":"ش ق و","root_id":"root_000809","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişiye bağlı biçimlerin karşılıklı ilişki, dayanma ve mücadele çekirdeğini karşılar; yenme sonucu bunun rekabetli uzantısıdır.","boundary_detail":"Dal yalnızca bir kişinin bedbahtlığı veya genel yorgunluk değildir; mutlaka başka bir kişiyle kurulan ilişki, dayanışma ya da karşılaşma yapısına bağlıdır.","branch_image_ar":"المشاقاة مصابرة ومعالجة","concept_gloss":"biriyle karşılıklı uğraşıp mücadele etme","contextual_glosses":[{"applicability":"İki kişinin ilişki veya işlem içinde birbirleriyle uğraştığı genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başka bir kişiyle kurulan karşılıklı ilişki ve uğraş yapısını korur."},"facet_ids":["F001"],"text":"biriyle karşılıklı uğraşmak","usage_role":"general"},{"applicability":"Karşı tarafa dayanma ve özellikle çatışmada onunla mücadele etme bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşı tarafa dayanma ve onunla mücadele etme yönlerini korur."},"facet_ids":["F002"],"text":"birine karşı direnip mücadele etmek","usage_role":"contextual"},{"applicability":"Karşılıklı çekişmenin odak kişisinin üstün gelmesiyle sonuçlandığı kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşı tarafla çekişme ve onu söz konusu işte alt etme sonucunu korur."},"facet_ids":["F003"],"text":"çekişmede onu yenmek","usage_role":"contextual"}],"definition":"Bir kişiyle karşılıklı ilişki içinde olma, ona karşı dayanma ve özellikle savaş gibi ortamlarda onunla uğraşıp mücadele etmedir. Rekabetli kullanımda bu süreç karşı tarafı bir işte alt etme sonucuna ulaşabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başka bir kişiyle karşılıklı ilişki ve uğraş içinde olmaktır."},{"facet_id":"F002","role":"specialization","statement":"Karşı tarafa dayanma, onunla mücadele etme ve özellikle savaşta onunla uğraşmadır."},{"facet_id":"F003","role":"extension","statement":"Rekabetli kullanımda karşı tarafla çekişip onu söz konusu işte alt etmeye uzanır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Her türlü galibiyetin bu dala girdiği izlenimini verebilir.","fit":"narrowing","loses":"Karşılıklı ilişkiyi, uğraşmayı, dayanmayı ve mücadele sürecini kaybeder.","preserves":"Rekabetli kullanımın üstün gelme sonucunu korur."},"text":"yenmek"}],"identity_rationale":"Kaynak ifadesi bir kişiyle karşılıklı ilişki ve uğraş içinde olmayı, ona karşı sabretmeyi ve özellikle çatışma ortamında onunla mücadele etmeyi birlikte verir; rekabetli kullanımda karşı tarafı yenme sonucu da açıkça tanıklanır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"biriyle ilişki kurup ona karşı direnmek veya onunla uğraşmak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"benimle çekişti, ben de onu o işte yendim"}],"lexicalization_note":"Anlam, kişi alan biçimlere bağlıdır: biriyle karşılıklı ilişki kurma, ona karşı dayanma veya mücadele etme ve çekişmede onu yenme kullanımları yalın kök anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan üç karşılaştırma, dalın genel uğraşmadan, çetin işe katlanmadan ve düzenli yarışmadan ayrılan kişiler arası yapısını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişiyle kurulan karşılıklı ilişki ve direnme yapısına bağlıdır; komşu dal ise daha genel biçimde bir şeyi işlemeyi, denemeyi veya başkasıyla çekişmeyi kapsar.","focus_only":"Başka bir kişiyle karşılıklı ilişki kurmayı ve ona karşı dayanmayı açıkça içerir.","gloss":"karşılıklı uğraşma ve bir şeyi işleme","neighbor_only":"Bir şeyi deneme ve onunla uğraşma, karşılıklı bir kişi ilişkisi bulunmadan da gerçekleşebilir.","neighbor_ref":"root_000655/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişi veya işle uğraşmayı, onu sürdürmeyi ve kimi bağlamlarda karşı tarafı aşmayı anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal kişiler arası karşılıklılığı merkez alır; komşu dalın çekirdeği ise ağır işin kendisini çekmek ve onun güçlüğüne katlanmaktır.","focus_only":"Başka bir kişiyle karşılıklı ilişki, direnme ve çekişme yapısını gerektirir.","gloss":"kişiye karşı mücadele ve çetin işle uğraşma","neighbor_only":"Çetin bir işi çekip onunla uğraşmayı, başka bir kişi bulunmadan da anlatabilir.","neighbor_ref":"root_001227/B003","relation_type":"near_neighbor","shared_zone":"İki dalda da zorlu bir süreçle uğraşma, dayanma ve işi sürdürme düşüncesi vardır."},{"boundary_match":"partial","distinction":"Odak dal genel karşılıklı ilişki ve mücadeleden bir tarafın üstün gelmesine uzanır; komşu dal ise gidip gelen üstünlükle kurulan yarışmayı belirginleştirir.","focus_only":"İlişki kurma ve karşı tarafa dayanma gibi rekabet dışı kullanımlara da sahiptir.","gloss":"karşılıklı mücadele ve yarışma","neighbor_only":"Tarafların sırayla üstün geldiği düzenli yarışma ve karşılıklı övünme görünümlerini kapsar.","neighbor_ref":"root_000677/B002","relation_type":"near_neighbor","shared_zone":"Her ikisi de iki tarafın birbirine karşı çaba gösterdiği mücadele veya yarışma ortamında kullanılabilir."}],"source_phrase_ar":"المشاقاة المعاناة والممارسة (maqayis;sihah)؛ شاقاني فلان فشقوته أي غلبته فيه (sihah)؛ شاقيت فلانا مشاقاة إذا عاشرته وعاشرك (tahdhib)؛ شاقيته أي صابرته والمشاقاة المعالجة في الحرب وغيرها (tahdhib)","source_summary":"Kaynaklar karşılıklı uğraşma ve işi birlikte ya da karşı karşıya yaşayarak sürdürme çekirdeğinde birleşir. Kişiyle ilişki kurma, ona karşı dayanma, savaşta mücadele etme ve çekişmenin sonunda onu alt etme bu çekirdeğin bağlama bağlı görünümleridir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه مشاقاة الإنسان معاشرة ومصابرة ومعالجة في الحرب وغيرها ومغالبة الآخر في الأمر","what_is_not_ar":"ليس مجرد الشقاء خلاف السعادة ولا الشقاء بمعنى التعب العام"},"support_links":[]},{"boundary":"Dal genel olarak dağı, yükseltiyi veya geçidi değil, belirtilen çıkış ve oturma özelliklerine sahip uzun bir dağ sırtını adlandırır.","branch_kind":"bare","branch_ref":"root_000809/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَشْقَى","morph_features":"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"91:12:3:1","qac_word_ref":"91:12:3","surface_ar":"أَشْقَىٰ"}],"gloss":"kolay çıkılan, oturmaya elverişli uzun dağ sırtı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dağın yükselen ve uzun bir sırtıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Uzunluğuna rağmen çıkılması daha kolay ve insanın oturmasına daha elverişlidir."}}],"root_ar":"ش ق و","root_id":"root_000809","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yeryüzü biçimini uzunluk, yükseliş, çıkış kolaylığı ve oturmaya elverişlilik özellikleriyle birlikte karşılar.","boundary_detail":"Dal genel olarak dağı, yükseltiyi veya geçidi değil, belirtilen çıkış ve oturma özelliklerine sahip uzun bir dağ sırtını adlandırır.","branch_image_ar":"الشاقي من حيود الجبال","concept_gloss":"kolay çıkılan, oturmaya elverişli uzun dağ sırtı","contextual_glosses":[{"applicability":"Bir dağ üzerindeki belirli yeryüzü biçiminin özelliklerini açıklayan coğrafi bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uzun sırt biçimini, tırmanma kolaylığını ve oturmaya uygunluğu korur."},"facet_ids":["F001","F002"],"text":"kolay tırmanılan ve oturmaya uygun uzun sırt","usage_role":"explanatory"}],"definition":"Dağın yükselen ve uzun, fakat uzunluğuna rağmen çıkılması daha kolay ve insanın oturmasına daha elverişli sırtıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dağın yükselen ve uzun bir sırtıdır."},{"facet_id":"F002","role":"specialization","statement":"Uzunluğuna rağmen çıkılması daha kolay ve insanın oturmasına daha elverişlidir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Bu özellikleri taşımayan bütün dağları kapsama katar.","collision":"Genel dağ adıyla karışır.","fit":"broadening","loses":"Uzun sırt biçimini, çıkış kolaylığını ve oturmaya elverişliliği kaybeder.","preserves":"Yükseltili bir yeryüzü biçimi olma özelliğini korur."},"text":"dağ"}],"identity_rationale":"Tek kaynaklı ifade, dağın yükselen ve uzun bir sırtını; uzunluğuna rağmen çıkılması daha kolay ve insanın oturmasına daha elverişli oluşuyla birlikte açıkça tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kolay çıkılan ve oturmaya elverişli uzun dağ sırtı"}],"lexicalization_note":"Yalın dal doğrudan belirli bir dağ sırtı türünü adlandırır; bedbahtlık, güçlük veya karşılıklı uğraşma dallarından anlam aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eşleşen dağ sırtı dalı ile biçimsel çıkıntı ve çıkış yeri bakımından en yakın iki coğrafi komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Odak dal ile komşu dalın çekirdeği, kapsamı ve ayırt edici koşulları aynıdır; olağan bağlamlarda birbirinin yerine kullanılabilir.","focus_only":null,"gloss":"kolay çıkılan, oturmaya elverişli uzun dağ sırtı","neighbor_only":null,"neighbor_ref":"root_000808/B004","relation_type":"synonym","shared_zone":"Her iki dal da aynı uzun dağ sırtını çıkış kolaylığı ve oturmaya elverişliliğiyle tanımlar."},{"boundary_match":"partial","distinction":"Odak dalın çıkış kolaylığı ve oturma elverişliliği zorunlu sınırdır; komşu dal biçimsel çıkıntıyı veya büyük dağı daha geniş biçimde kapsar.","focus_only":"Çıkılması daha kolay ve oturmaya daha elverişli olan uzun bir dağ sırtını belirtir.","gloss":"uzun dağ sırtı ve çıkıntılı dağ parçası","neighbor_only":"Büyük dağın kendisini veya dağdan uzunlamasına çıkan bir parçayı, çıkış ve oturma koşulları olmadan belirtebilir.","neighbor_ref":"root_001179/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da dağın uzunlamasına uzanan ya da dışarı çıkan bir bölümünü adlandırabilir."},{"boundary_match":"field_only","distinction":"Odak dal somut bir sırt türüdür; komşu dal ise çıkma eylemine, çıkış güzergahına veya yüksekten bakılan yere odaklanır.","focus_only":"Belirli özelliklere sahip uzun bir dağ sırtını adlandırır.","gloss":"dağ sırtı ve çıkış yeri","neighbor_only":"Dağa çıkma eylemini, çıkış yerini veya yüksekten bakılan bir konumu anlatır.","neighbor_ref":"root_000945/B006","relation_type":"same_field","shared_zone":"İki dal da dağlık bir yerde yükselme, çıkma ve yüksek konumla ilişkilidir."}],"source_phrase_ar":"الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان والجميع شاقيات وشواقي (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Dalın tek tanıklığı, uzun dağ sırtını hem kolay çıkılır hem de oturmaya elverişli oluşuyla sınırlar."}],"source_summary":"Bu coğrafi ad, yükselen uzun bir dağ sırtını çıkış kolaylığı ve oturmaya elverişliliğiyle birlikte tanımlar.","sources":["AY"],"what_is_ar":"يدخل فيه الحيد الطالع الطويل من الجبل إذا كان أيسر صعودا وأقدر مقعدا للإنسان وجمعه شاقيات وشواقي","what_is_not_ar":"ليس الشقاء ولا المشاقاة"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["91:12:1"],"branch_refs":[],"candidate_id":"cand_a68d4b1b8b4ea748ac45","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:12:1:dependent-past-time","source_type":"word_analysis","support_ids":["sup_0115c6c802e0a597592e","sup_1bb6532f5a8e5796c65f"],"title":"dependent past moment tied to 91:11","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:1","qac_refs":["91:12:1:1"],"status":"accepted"}},{"anchor_refs":["91:12:1"],"branch_refs":[],"candidate_id":"cand_6e957bd2583c4f5fcf5b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:12:1:opening-frame-and-compression","source_type":"word_analysis","support_ids":["sup_0115c6c802e0a597592e","sup_d8af9ffaa78faed0087d"],"title":"first beat of the compressed clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:1","qac_refs":["91:12:1:1"],"status":"accepted"}},{"anchor_refs":["91:12:1"],"branch_refs":[],"candidate_id":"cand_37b735ad749ddd3f4380","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:12:1:trigger-moment","source_type":"word_analysis","support_ids":["sup_0115c6c802e0a597592e","sup_c67d298accc0639e080a"],"title":"moment where transgression becomes event","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:1","qac_refs":["91:12:1:1"],"status":"accepted"}},{"anchor_refs":["91:12:2"],"branch_refs":[],"candidate_id":"cand_0444decdd19a33a98ef1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000129"],"scope":"focus_ayah","source_local_id":"91:12:2:agency-on-culprit","source_type":"word_analysis","support_ids":["sup_0287b6fbe22c3d63a95e","sup_7ed8736a60ecde7aa80c"],"title":"agency lands on the delayed culprit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:2","qac_refs":["91:12:2:1"],"status":"accepted"}},{"anchor_refs":["91:12:2"],"branch_refs":[],"candidate_id":"cand_f7fd171cc8d28170c036","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000129"],"scope":"focus_ayah","source_local_id":"91:12:2:boundary-bridge","source_type":"word_analysis","support_ids":["sup_14c63b1cecd9a37c6235","sup_7ed8736a60ecde7aa80c"],"title":"abstract transgression becomes embodied motion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:2","qac_refs":["91:12:2:1"],"status":"accepted"}},{"anchor_refs":["91:12:2"],"branch_refs":[],"candidate_id":"cand_7ddc9c437e7d9b3e7b6b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000129"],"scope":"focus_ayah","source_local_id":"91:12:2:compressed-action-hinge","source_type":"word_analysis","support_ids":["sup_6c8e6776ddad3e84bb20","sup_7ed8736a60ecde7aa80c"],"title":"middle action beat in compressed narration","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:2","qac_refs":["91:12:2:1"],"status":"accepted"}},{"anchor_refs":["91:12:2"],"branch_refs":[],"candidate_id":"cand_5f54ff8d0e17aa23753f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000129"],"scope":"focus_ayah","source_local_id":"91:12:2:form-vii-not-commissioned-dispatch","source_type":"word_analysis","support_ids":["sup_7ed8736a60ecde7aa80c","sup_fc9a1ae7700441793530"],"title":"Form VII internalizes the motion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:2","qac_refs":["91:12:2:1"],"status":"accepted"}},{"anchor_refs":["91:12:2"],"branch_refs":[],"candidate_id":"cand_2b4a0fd292078f86ea34","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000129"],"scope":"focus_ayah","source_local_id":"91:12:2:forward-narrative-chain","source_type":"word_analysis","support_ids":["sup_534313839ee4721119d0","sup_7ed8736a60ecde7aa80c"],"title":"rising triggers the following sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:2","qac_refs":["91:12:2:1"],"status":"accepted"}},{"anchor_refs":["91:12:2"],"branch_refs":[],"candidate_id":"cand_065b31dc2cb8fdcae271","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000129"],"scope":"focus_ayah","source_local_id":"91:12:2:intertextual-root-contrast","source_type":"word_analysis","support_ids":["sup_7ed8736a60ecde7aa80c","sup_c591830aa1e22b900eb3"],"title":"sending and resurrection fields become contrast","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:2","qac_refs":["91:12:2:1"],"status":"accepted"}},{"anchor_refs":["91:12:2"],"branch_refs":[],"candidate_id":"cand_d62cd0712273417febd5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000129"],"scope":"focus_ayah","source_local_id":"91:12:2:nasal-prefix-sound","source_type":"word_analysis","support_ids":["sup_7ed8736a60ecde7aa80c","sup_bac8e06a2ded4d53fb46"],"title":"prefix-root boundary heard in recitation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:2","qac_refs":["91:12:2:1"],"status":"accepted"}},{"anchor_refs":["91:12:2"],"branch_refs":[],"candidate_id":"cand_78f3fd2069afe10e478e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000129"],"scope":"focus_ayah","source_local_id":"91:12:2:perfect-intransitive-self-rising","source_type":"word_analysis","support_ids":["sup_0d69c7e7fc7abff27106","sup_7ed8736a60ecde7aa80c"],"title":"completed self-propelled rising","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:2","qac_refs":["91:12:2:1"],"status":"accepted"}},{"anchor_refs":["91:12:2"],"branch_refs":[],"candidate_id":"cand_d07825bbd83e9e358141","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000129"],"scope":"focus_ayah","source_local_id":"91:12:2:rare-form-markedness","source_type":"word_analysis","support_ids":["sup_5255c8b18b169ab2e3e4","sup_7ed8736a60ecde7aa80c"],"title":"marked narrative Form VII choice","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:2","qac_refs":["91:12:2:1"],"status":"accepted"}},{"anchor_refs":["91:12:2"],"branch_refs":[],"candidate_id":"cand_9f9ad889317826aa2e44","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000129"],"scope":"focus_ayah","source_local_id":"91:12:2:root-motion-pressure","source_type":"word_analysis","support_ids":["sup_7ed8736a60ecde7aa80c","sup_83bd31150ab651bbc138"],"title":"rousing and dispatch pressure narrowed to rising","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:2","qac_refs":["91:12:2:1"],"status":"accepted"}},{"anchor_refs":["91:12:3"],"branch_refs":[],"candidate_id":"cand_ab1f7994b29d94c383b0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"91:12:3:anonymized-moral-rank","source_type":"word_analysis","support_ids":["sup_b7c4dd6dd983fcf11e32","sup_f48d68d34341ddc156ee"],"title":"moral rank replaces biography","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:3","qac_refs":["91:12:3:1","91:12:3:2"],"status":"accepted"}},{"anchor_refs":["91:12:3"],"branch_refs":[],"candidate_id":"cand_0d360a66d26bb43b74d0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"91:12:3:controlled-forward-ambiguity","source_type":"word_analysis","support_ids":["sup_b7c4dd6dd983fcf11e32","sup_f46a6dac9462bb0ebfaf"],"title":"forward pressure toward the she-camel","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:3","qac_refs":["91:12:3:1","91:12:3:2"],"status":"accepted"}},{"anchor_refs":["91:12:3"],"branch_refs":[],"candidate_id":"cand_791ade7807d8058b3222","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"91:12:3:delayed-closure-identity","source_type":"word_analysis","support_ids":["sup_b7c4dd6dd983fcf11e32","sup_f7544cad71a5be50e486"],"title":"final position makes moral identity land","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:3","qac_refs":["91:12:3:1","91:12:3:2"],"status":"accepted"}},{"anchor_refs":["91:12:3"],"branch_refs":[],"candidate_id":"cand_bd2805238f0042052a74","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"91:12:3:feminine-suffix-to-collective","source_type":"word_analysis","support_ids":["sup_2ecbc05181c67ac18901","sup_b7c4dd6dd983fcf11e32"],"title":"suffix ties the culprit to the prior collective","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:3","qac_refs":["91:12:3:1","91:12:3:2"],"status":"accepted"}},{"anchor_refs":["91:12:3"],"branch_refs":[],"candidate_id":"cand_673a835d55c4400d4efb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"91:12:3:hard-final-sound","source_type":"word_analysis","support_ids":["sup_06034a4cee1fc531ef52","sup_b7c4dd6dd983fcf11e32"],"title":"hard sound makes the label land","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:3","qac_refs":["91:12:3:1","91:12:3:2"],"status":"accepted"}},{"anchor_refs":["91:12:3"],"branch_refs":[],"candidate_id":"cand_b7e4b1fd32c518feab1e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"91:12:3:intertextual-wretchedness-rank","source_type":"word_analysis","support_ids":["sup_2c0a18e51c9ce138f56d","sup_b7c4dd6dd983fcf11e32"],"title":"wretchedness rank echoes refusal and fate contexts","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:3","qac_refs":["91:12:3:1","91:12:3:2"],"status":"accepted"}},{"anchor_refs":["91:12:3"],"branch_refs":[],"candidate_id":"cand_209148c682e4e8ae6157","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"91:12:3:local-subject-not-causative-verb","source_type":"word_analysis","support_ids":["sup_01a8e9b6c2646b9c3110","sup_b7c4dd6dd983fcf11e32"],"title":"elative subject, not causative predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:3","qac_refs":["91:12:3:1","91:12:3:2"],"status":"accepted"}},{"anchor_refs":["91:12:3"],"branch_refs":[],"candidate_id":"cand_7ca9572575e2cfd666ea","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"91:12:3:moral-ruin-field","source_type":"word_analysis","support_ids":["sup_a4fb4d099a2019556b59","sup_b7c4dd6dd983fcf11e32"],"title":"misery and hardship converge as moral ruin","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:3","qac_refs":["91:12:3:1","91:12:3:2"],"status":"accepted"}},{"anchor_refs":["91:12:3"],"branch_refs":[],"candidate_id":"cand_74c28d75a3265c9d4813","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"91:12:3:partitive-superlative","source_type":"word_analysis","support_ids":["sup_5a816a0ab9fbd8e879ea","sup_b7c4dd6dd983fcf11e32"],"title":"superlative selects one from the group","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:3","qac_refs":["91:12:3:1","91:12:3:2"],"status":"accepted"}},{"anchor_refs":["91:12:3"],"branch_refs":[],"candidate_id":"cand_f6da31f2864063c62949","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"91:12:3:plural-execution-tension","source_type":"word_analysis","support_ids":["sup_3d40c27cb60da856fb36","sup_b7c4dd6dd983fcf11e32"],"title":"one instigator before plural crime","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:3","qac_refs":["91:12:3:1","91:12:3:2"],"status":"accepted"}},{"anchor_refs":["91:12:3"],"branch_refs":[],"candidate_id":"cand_272ea54f7d9578946990","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"91:12:3:prior-transgression-echo","source_type":"word_analysis","support_ids":["sup_2ed125a48b27645f1514","sup_b7c4dd6dd983fcf11e32"],"title":"suffix cadence binds transgression to culprit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:3","qac_refs":["91:12:3:1","91:12:3:2"],"status":"accepted"}},{"anchor_refs":["91:12:3"],"branch_refs":[],"candidate_id":"cand_01f52d5ce1d6eba64481","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"91:12:3:ruin-cause-and-result","source_type":"word_analysis","support_ids":["sup_b7c4dd6dd983fcf11e32","sup_ecf5237bfe0fafe233b7"],"title":"wretchedness before and through the act","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:3","qac_refs":["91:12:3:1","91:12:3:2"],"status":"accepted"}},{"anchor_refs":["91:12:3"],"branch_refs":[],"candidate_id":"cand_582e98bd432ad327545f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"91:12:3:singular-representative-culprit","source_type":"word_analysis","support_ids":["sup_9d4e903048cf2d578d99","sup_b7c4dd6dd983fcf11e32"],"title":"one executor represents collective failure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:12:3","qac_refs":["91:12:3:1","91:12:3:2"],"status":"accepted"}},{"anchor_refs":["91:12:2"],"branch_refs":[],"candidate_id":"cand_3943ad849a9a86757af7","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000129"],"scope":"focus_ayah","source_local_id":"91:12:2:1","source_type":"qac_morpheme","support_ids":["sup_f5e040feb69c4b698dd7"],"title":"QAC root occurrence: ب ع ث","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:12:3"],"branch_refs":[],"candidate_id":"cand_7159278b92bfb9b9a61b","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000808","root_000809"],"scope":"focus_ayah","source_local_id":"91:12:3:1","source_type":"qac_morpheme","support_ids":["sup_7568a60040ca341f638f"],"title":"QAC root occurrence: ش ق و","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:12"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:12","branch_refs":["root_000129/B004","root_000809/B001"],"candidate_id":"cand_799f693bf34de874f5aa","commentary_obligation":"review","hft_ref":"hft_2f2f79ed21f6e54b1cbc","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_kinetic_extreme","source_type":"hft","support_ids":["sup_fcdfd00ae2b0ea1c1510"],"title":"baseline_kinetic_extreme","trust":"legacy_unbound"},{"anchor_refs":["91:12"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:12","branch_refs":["root_000129/B001","root_000808/B002"],"candidate_id":"cand_04ed7a4291c3ed4a5fb8","commentary_obligation":"review","hft_ref":"hft_a02afd49d9fa42d12187","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_roused_hardship","source_type":"hft","support_ids":["sup_1c7fc6154f1a05447e6d"],"title":"baseline_roused_hardship","trust":"legacy_unbound"},{"anchor_refs":["91:12"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:12","branch_refs":["root_000129/B002","root_000808/B003"],"candidate_id":"cand_18293f7ae42e34ddee49","commentary_obligation":"review","hft_ref":"hft_da28b40f98faf76a9a5a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_dispatched_contestant","source_type":"hft","support_ids":["sup_31a285eb0e42c6aa5667"],"title":"baseline_dispatched_contestant","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا","qac_morphemes":[{"lemma_ar":"إِذ","morph_features":"STEM|POS:T|LEM:<i*","morpheme_role":"STEM","pos":"T","qac_ref":"91:12:1:1","qac_word_ref":"91:12:1","root_ar":"","surface_ar":"إِذِ"},{"lemma_ar":"ٱنۢبَعَثَ","morph_features":"STEM|POS:V|PERF|(VII)|LEM:{n[baEava|ROOT:bEv|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:12:2:1","qac_word_ref":"91:12:2","root_ar":"ب ع ث","surface_ar":"ٱنۢبَعَثَ"},{"lemma_ar":"أَشْقَى","morph_features":"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"91:12:3:1","qac_word_ref":"91:12:3","root_ar":"ش ق و","surface_ar":"أَشْقَىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:12:3:2","qac_word_ref":"91:12:3","root_ar":"","surface_ar":"هَا"}],"word_analysis_qac_refs":[["91:12:1:1"],["91:12:2:1"],["91:12:3:1","91:12:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["91:12:1","91:12:2","91:12:3"]},"focus_surface_evidence":{"arabic_uthmani":"إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا","qac_morphemes":[{"lemma_ar":"إِذ","morph_features":"STEM|POS:T|LEM:<i*","morpheme_role":"STEM","pos":"T","qac_ref":"91:12:1:1","qac_word_ref":"91:12:1","root_ar":"","surface_ar":"إِذِ"},{"lemma_ar":"ٱنۢبَعَثَ","morph_features":"STEM|POS:V|PERF|(VII)|LEM:{n[baEava|ROOT:bEv|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:12:2:1","qac_word_ref":"91:12:2","root_ar":"ب ع ث","surface_ar":"ٱنۢبَعَثَ"},{"lemma_ar":"أَشْقَى","morph_features":"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"91:12:3:1","qac_word_ref":"91:12:3","root_ar":"ش ق و","surface_ar":"أَشْقَىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:12:3:2","qac_word_ref":"91:12:3","root_ar":"","surface_ar":"هَا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["91:12:1:1"],["91:12:2:1"],["91:12:3:1","91:12:3:2"]],"word_analysis_refs":["91:12:1","91:12:2","91:12:3"],"word_rows":[{"analysis_record_ref":"91:12:1","analytic_gloss_range_en":"past temporal subordinator marking the decisive moment by which the prior denial becomes a visible event","analytic_root_gloss_range_en":null,"qac_refs":["91:12:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"إِذِ","transliteration":"idh"}},{"analysis_record_ref":"91:12:2","analytic_gloss_range_en":"completed Form VII intransitive rising or springing forth by the culprit, with dispatch and rousing pressure narrowed by local self-activation","analytic_root_gloss_range_en":"root range includes rousing from stillness, dispatching, setting out, resurrection, and divine bringing into existence; the local Form VII clause selects self-activated rising within a guilty collective","qac_refs":["91:12:2:1"],"root":{"arabic":"ب ع ث","transliteration":"b-ʿ-th"},"surface":{"arabic":"ٱنۢبَعَثَ","transliteration":"inbaʿatha"}},{"analysis_record_ref":"91:12:3","analytic_gloss_range_en":"elative/superlative subject with a feminine suffix, selecting the group's most wretched member as the delayed agent","analytic_root_gloss_range_en":"root range includes misery, wretchedness, hardship, strenuous suffering, and related contest or terrain branches; the local elative selects maximal moral wretchedness within the group","qac_refs":["91:12:3:1","91:12:3:2"],"root":{"arabic":"ش ق و","transliteration":"sh-q-w"},"surface":{"arabic":"أَشْقَىٰهَا","transliteration":"ashqāhā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["91:12"],"branch_refs":["root_000129/B004","root_000809/B001"],"candidate_id":"cand_799f693bf34de874f5aa","evidence_scope":"focus_ayah","hft_ref":"hft_2f2f79ed21f6e54b1cbc","item_id":"baseline_kinetic_extreme","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_kinetic_extreme","support_id":"sup_fcdfd00ae2b0ea1c1510"},{"anchor_refs":["91:12"],"branch_refs":["root_000129/B001","root_000808/B002"],"candidate_id":"cand_04ed7a4291c3ed4a5fb8","evidence_scope":"focus_ayah","hft_ref":"hft_a02afd49d9fa42d12187","item_id":"baseline_roused_hardship","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_roused_hardship","support_id":"sup_1c7fc6154f1a05447e6d"},{"anchor_refs":["91:12"],"branch_refs":["root_000129/B002","root_000808/B003"],"candidate_id":"cand_18293f7ae42e34ddee49","evidence_scope":"focus_ayah","hft_ref":"hft_da28b40f98faf76a9a5a","item_id":"baseline_dispatched_contestant","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_dispatched_contestant","support_id":"sup_31a285eb0e42c6aa5667"}],"diagnostics":[],"lane_counts":{"global":9,"macro":10,"micro":3},"packet_summary":{"ayah_count":15,"focus_ref":"91:12","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ت ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000186","furuq_root_norm":"ت ل و","furuq_source_root_norm":"ت ل و","is_dominant":true,"target_occurrences":39,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000185","furuq_root_norm":"ت ل ل","furuq_source_root_norm":"ت ل ل","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["91:1","91:2","91:3","91:4","91:5","91:6","91:7","91:8","91:9","91:10","91:11","91:12","91:13","91:14","91:15"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"91:12","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":13,"unstructured_record_count":0},"identity":{"ayah_ref":"91:12","lane":"micro","linguistic_source_ref":"91:12","surface_ref":"91:12","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"91:12","target_tokens":[["İçlerindeki",["91:12:3"]],["en",["91:12:3"]],["kötü",["91:12:3"]],["kişi",["91:12:3"]],["harekete",["91:12:2"]],["geçtiğinde",["91:12:1","91:12:2"]]],"text":"İçlerindeki en kötü kişi harekete geçtiğinde,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":15,"id":"s091-p01-001-015","label":"Whole surah","number":1,"refs":["91:1","91:2","91:3","91:4","91:5","91:6","91:7","91:8","91:9","91:10","91:11","91:12","91:13","91:14","91:15"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:1","source_type":"word_analysis","support_id":"sup_0115c6c802e0a597592e","text":"{\"gloss_range\":\"past temporal subordinator marking the decisive moment by which the prior denial becomes a visible event\",\"prose\":\"{{ar:إِذِ}} ({{tr:idh}}) opens the ayah as a dependent time-marker, so 91:12 is not a detached new report. It keeps the denial of 91:11 active and names the moment in which that denial became concrete: first the time-frame, then the rising, then the culprit. Because the particle stands first, the reader is asked to hear the whole three-word clause as the timed specification of the preceding transgression, not merely as chronology after it.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِذِ}} ({{tr:idh}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:3:local-subject-not-causative-verb","source_type":"word_analysis","support_id":"sup_01a8e9b6c2646b9c3110","text":"{\"blocking_evidence\":null,\"headline\":\"elative subject, not causative predicate\",\"reader_payoff\":\"The reader notices that wretchedness is turned into the identity of the actor who rises, not into a second action in the clause.\",\"reason\":\"The supplied family includes a causative derivative, but local attachment and QAC evidence make {{ar:أَشْقَىٰهَا}} ({{tr:ashqāhā}}) the delayed elative subject of {{ar:ٱنۢبَعَثَ}} ({{tr:inbaʿatha}}).\",\"representative_source_ids\":[\"QG-bc31c592\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:2:agency-on-culprit","source_type":"word_analysis","support_id":"sup_0287b6fbe22c3d63a95e","text":"{\"blocking_evidence\":null,\"headline\":\"agency lands on the delayed culprit\",\"reader_payoff\":\"The reader notices that morphology prepares a singular masculine actor before the final word identifies him, so the deed is heard before biography.\",\"reason\":\"The third masculine singular verb precedes its explicit subject {{ar:أَشْقَىٰهَا}} ({{tr:ashqāhā}}), producing action-before-agent order without weakening agency.\",\"representative_source_ids\":[\"QG-a111bfb0\",\"QS-4f9e1e51\",\"QT-9ed1b8bd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:3:hard-final-sound","source_type":"word_analysis","support_id":"sup_06034a4cee1fc531ef52","text":"{\"blocking_evidence\":null,\"headline\":\"hard sound makes the label land\",\"reader_payoff\":\"The reader hears the final moral label close with a harder texture at the point the culprit is identified.\",\"reason\":\"The sound note is limited to the local surface and final position of {{ar:أَشْقَىٰهَا}} ({{tr:ashqāhā}}).\",\"representative_source_ids\":[\"QP-4105a462\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:2:perfect-intransitive-self-rising","source_type":"word_analysis","support_id":"sup_0d69c7e7fc7abff27106","text":"{\"blocking_evidence\":null,\"headline\":\"completed self-propelled rising\",\"reader_payoff\":\"The reader notices the action as a decisive completed eruption by the subject, not as an attempt, process, object-taking action, or passive dispatch.\",\"reason\":\"The local verb is perfect Form VII, intransitive, and takes {{ar:أَشْقَىٰهَا}} ({{tr:ashqāhā}}) as its explicit subject with no object or destination.\",\"representative_source_ids\":[\"QG-1c33b5d1\",\"QG-2d4716e8\",\"QG-6053d9d2\",\"MG-34600f2d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:2:boundary-bridge","source_type":"word_analysis","support_id":"sup_14c63b1cecd9a37c6235","text":"{\"blocking_evidence\":null,\"headline\":\"abstract transgression becomes embodied motion\",\"reader_payoff\":\"The reader notices the scene narrow from collective moral excess in 91:11 to one embodied motion in 91:12.\",\"reason\":\"The boundary rows coherently link the current motion word to 91:11's prior transgression and to the singular subject that completes the clause.\",\"representative_source_ids\":[\"QE-b055380a\",\"QB-6a80f619\",\"QB-e5de6183\",\"QY-ec46082f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:1:dependent-past-time","source_type":"word_analysis","support_id":"sup_1bb6532f5a8e5796c65f","text":"{\"blocking_evidence\":null,\"headline\":\"dependent past moment tied to 91:11\",\"reader_payoff\":\"The reader notices that the ayah begins inside the grammar of 91:11, naming a definite past moment rather than an open condition or independent event.\",\"reason\":\"QAC and attachment evidence identify {{ar:إِذِ}} ({{tr:idh}}) as the temporal adverbial subordinator for the clause governed by the prior denial context.\",\"representative_source_ids\":[\"QG-8e13cd0a\",\"QG-a1dec461\",\"QG-cea15f4d\",\"MG-1fb2ba5e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:3:intertextual-wretchedness-rank","source_type":"word_analysis","support_id":"sup_2c0a18e51c9ce138f56d","text":"{\"blocking_evidence\":null,\"headline\":\"wretchedness rank echoes refusal and fate contexts\",\"reader_payoff\":\"The reader notices that the culprit's rank belongs to a broader refusal, punishment, and fate vocabulary, not an isolated local insult.\",\"reason\":\"The source rows give concrete links to warning-refusal and punishment contexts (87:11; 92:15), eschatological wretchedness (11:105-106), and prophetic non-wretchedness contrasts (19:4; 19:48).\",\"representative_source_ids\":[\"QI-b3dc4bf7\",\"QI-d0d5952d\",\"QI-e3f9ee30\",\"MI-d996a967\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:3:feminine-suffix-to-collective","source_type":"word_analysis","support_id":"sup_2ecbc05181c67ac18901","text":"{\"blocking_evidence\":null,\"headline\":\"suffix ties the culprit to the prior collective\",\"reader_payoff\":\"The reader sees the grammar split the singular male culprit from the feminine collective source out of which he is selected.\",\"reason\":\"Attachment evidence strongly licenses the feminine suffix as resuming the prior collective from 91:11 while the elative subject remains masculine singular.\",\"representative_source_ids\":[\"QG-59d933f9\",\"QG-6be62f2c\",\"QF-d8b84d0f\",\"QB-1f012065\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:3:prior-transgression-echo","source_type":"word_analysis","support_id":"sup_2ed125a48b27645f1514","text":"{\"blocking_evidence\":null,\"headline\":\"suffix cadence binds transgression to culprit\",\"reader_payoff\":\"The reader hears 91:11's transgression and 91:12's culprit linked by repeated suffix shape while the roots change from condition to person.\",\"reason\":\"The rows explicitly tie the suffix and cadence of 91:11 to the current elative, making the prior transgression and selected culprit audible as a sequence.\",\"representative_source_ids\":[\"QE-39663693\",\"QE-fe477817\",\"ME-d9ad5778\",\"QP-07bb0ac9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:3:plural-execution-tension","source_type":"word_analysis","support_id":"sup_3d40c27cb60da856fb36","text":"{\"blocking_evidence\":null,\"headline\":\"one instigator before plural crime\",\"reader_payoff\":\"The reader notices the tension between a singled-out instigator in 91:12 and plural execution of the crime in 91:14.\",\"reason\":\"The row explicitly contrasts the singular culprit here with the plural action in 91:14, preserving individual instigation and communal participation.\",\"representative_source_ids\":[\"QB-22fe6c75\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:2:rare-form-markedness","source_type":"word_analysis","support_id":"sup_5255c8b18b169ab2e3e4","text":"{\"blocking_evidence\":null,\"headline\":\"marked narrative Form VII choice\",\"reader_payoff\":\"The reader notices that this common root appears here in a marked compact Form VII narrative use, making the single eruption stand out.\",\"reason\":\"The contextual profile lists only this exact Form VII instance, and the comparison to prepared mobilization at 9:46 sharpens the local suddenness without changing the parse.\",\"representative_source_ids\":[\"QI-95603187\",\"QH-bada27da\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:2:forward-narrative-chain","source_type":"word_analysis","support_id":"sup_534313839ee4721119d0","text":"{\"blocking_evidence\":null,\"headline\":\"rising triggers the following sequence\",\"reader_payoff\":\"The reader notices that the rising is not static description; it becomes the narrative condition for the speech in 91:13 and the collective action in 91:14.\",\"reason\":\"The source rows explicitly point from the current motion to the following sequential narration in 91:13 and 91:14.\",\"representative_source_ids\":[\"QE-79ca63f0\",\"QB-e4f018d4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:3:partitive-superlative","source_type":"word_analysis","support_id":"sup_5a816a0ab9fbd8e879ea","text":"{\"blocking_evidence\":null,\"headline\":\"superlative selects one from the group\",\"reader_payoff\":\"The reader notices that the word does not label a generic wretched person; it identifies the extreme member within a known collective.\",\"reason\":\"The local form is an elative/superlative adjective with a suffix, functioning as the subject of the verb and selecting one member from the group.\",\"representative_source_ids\":[\"QG-57b5acc5\",\"MG-9eb82884\",\"QS-ad5bcb87\",\"QF-9560f366\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:2:compressed-action-hinge","source_type":"word_analysis","support_id":"sup_6c8e6776ddad3e84bb20","text":"{\"blocking_evidence\":null,\"headline\":\"middle action beat in compressed narration\",\"reader_payoff\":\"The reader feels the whole event compressed into a time-action-agent sequence, with the verb as the hinge between dependence and culprit identity.\",\"reason\":\"The verb sits between the opening temporal particle and final subject in a three-word clause, creating a clipped trigger-action-agent sequence.\",\"representative_source_ids\":[\"QT-096ef44a\",\"QT-f29ba17a\",\"QP-d69006f3\",\"QY-94962d8f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"91:12:3:1","source_type":"qac_morpheme","support_id":"sup_7568a60040ca341f638f","text":"{\"lemma_ar\":\"أَشْقَى\",\"morph_features\":\"STEM|POS:N|LEM:>a$oqaY|ROOT:$qw|M|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"91:12:3:1\",\"qac_word_ref\":\"91:12:3\",\"root_ar\":\"ش ق و\",\"surface_ar\":\"أَشْقَىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:2","source_type":"word_analysis","support_id":"sup_7ed8736a60ecde7aa80c","text":"{\"gloss_range\":\"completed Form VII intransitive rising or springing forth by the culprit, with dispatch and rousing pressure narrowed by local self-activation\",\"prose\":\"{{ar:ٱنۢبَعَثَ}} ({{tr:inbaʿatha}}) is the clause's central action beat. As a perfect Form VII verb, it presents the rising as a completed fact and makes the culprit himself the one who springs forth, without an object, destination, or formal commissioning frame. The visible nasal prefix is compressed into the root onset, so the Form VII self-activation is heard as well as parsed. The wider {{ar:ب ع ث}} ({{tr:b-ʿ-th}}) field includes rousing, dispatching, and resurrection, but local grammar narrows that range to self-activated emergence from within the guilty collective. That narrowing matters: 91:11's abstract transgression becomes a body in motion, while the verb-before-subject order lets the deed arrive before {{ar:أَشْقَىٰهَا}} ({{tr:ashqāhā}}) is named. Against the prepared mobilization context at 9:46, this single perfect verb feels compact and sudden, and it launches the rapid sequence of warning speech (91:13) and collective action (91:14). The root's messenger-sending uses (2:129; 62:2) and resurrection uses (17:49; 22:7; 36:52) remain contrastive pressure, not the local sense; here the same motion-field is lowered into a destructive human rising.\",\"root_display\":\"{{ar:ب ع ث}} ({{tr:b-ʿ-th}})\",\"root_gloss_range\":\"root range includes rousing from stillness, dispatching, setting out, resurrection, and divine bringing into existence; the local Form VII clause selects self-activated rising within a guilty collective\",\"surface_display\":\"{{ar:ٱنۢبَعَثَ}} ({{tr:inbaʿatha}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:2:root-motion-pressure","source_type":"word_analysis","support_id":"sup_83bd31150ab651bbc138","text":"{\"blocking_evidence\":null,\"headline\":\"rousing and dispatch pressure narrowed to rising\",\"reader_payoff\":\"The reader feels dormant transgression turn kinetic, while the local frame keeps rousing and dispatch pressure subordinate to self-activated rising.\",\"reason\":\"V4 supports a broad {{ar:ب ع ث}} ({{tr:b-ʿ-th}}) field, but the intransitive Form VII clause selects a self-rising event rather than all root branches as local meanings.\",\"representative_source_ids\":[\"QS-38a4c77f\",\"QS-50e0789d\",\"QS-f5f01978\",\"MS-61ec7315\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:3:singular-representative-culprit","source_type":"word_analysis","support_id":"sup_9d4e903048cf2d578d99","text":"{\"blocking_evidence\":null,\"headline\":\"one executor represents collective failure\",\"reader_payoff\":\"The reader notices the narrative narrowing from a tribe's denial to one body whose moral rank represents the group's failure.\",\"reason\":\"The singular elative subject with a collective suffix concentrates agency in one executor while the antecedent keeps communal guilt in view.\",\"representative_source_ids\":[\"QF-ca99224f\",\"QB-3351d192\",\"QB-5690873a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:3:moral-ruin-field","source_type":"word_analysis","support_id":"sup_a4fb4d099a2019556b59","text":"{\"blocking_evidence\":null,\"headline\":\"misery and hardship converge as moral ruin\",\"reader_payoff\":\"The reader hears the label as maximum moral ruin, not mere bad luck or a neutral identifier.\",\"reason\":\"V4 supports misery, hardship, and wretchedness branches for {{ar:ش ق و}} ({{tr:sh-q-w}}), while the local elative subject selects the moral-wretchedness maximum within the group.\",\"representative_source_ids\":[\"QS-4909f98b\",\"QS-893e9b3a\",\"QS-b97bd9d5\",\"QI-030dd8c4\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:3","source_type":"word_analysis","support_id":"sup_b7c4dd6dd983fcf11e32","text":"{\"gloss_range\":\"elative/superlative subject with a feminine suffix, selecting the group's most wretched member as the delayed agent\",\"prose\":\"{{ar:أَشْقَىٰهَا}} ({{tr:ashqāhā}}) closes the clause by naming the delayed subject of {{ar:ٱنۢبَعَثَ}} ({{tr:inbaʿatha}}). It is not a second verb meaning to make someone wretched; local grammar makes it an elative subject, the group's most wretched one. The feminine suffix points back primarily to the prior collective in 91:11, so the word selects one extreme agent from the collective while keeping the group implicated. The repeated final suffix shape also links 91:11's transgression to this culprit, shifting from possessed excess to selected person. The {{ar:ش ق و}} ({{tr:sh-q-w}}) field makes that label more than misfortune: hardship, misery, and moral ruin converge in a maximum within the tribe, so the actor's wretchedness reads as both the ruined condition behind the act and the ruin exposed by it. That rank resonates with refusal and punishment contexts (87:11; 92:15), the fate division of the wretched (11:105-106), and prophetic non-wretchedness contrasts (19:4; 19:48). Its final position matters too; the ayah lets the rising be heard first, then lands on moral identity rather than personal biography, with a harder final texture at the point the culprit is identified. The suffix can also prepare the ear for {{ar:نَاقَةَ}} ({{tr:nāqata}}) in 91:13, but that is forward pressure only, not the primary antecedent; 91:14 then preserves the tension between one singled-out instigator and plural execution of the crime.\",\"root_display\":\"{{ar:ش ق و}} ({{tr:sh-q-w}})\",\"root_gloss_range\":\"root range includes misery, wretchedness, hardship, strenuous suffering, and related contest or terrain branches; the local elative selects maximal moral wretchedness within the group\",\"surface_display\":\"{{ar:أَشْقَىٰهَا}} ({{tr:ashqāhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:2:nasal-prefix-sound","source_type":"word_analysis","support_id":"sup_bac8e06a2ded4d53fb46","text":"{\"blocking_evidence\":null,\"headline\":\"prefix-root boundary heard in recitation\",\"reader_payoff\":\"The reader hears the Form VII prefix compressed at the root onset, making internal activation audible at the moment of rising.\",\"reason\":\"The written and recited surface of {{ar:ٱنۢبَعَثَ}} ({{tr:inbaʿatha}}) preserves the Form VII prefix boundary before the root onset.\",\"representative_source_ids\":[\"QF-17d081a2\",\"QP-46f9d828\",\"MP-a118c753\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:2:intertextual-root-contrast","source_type":"word_analysis","support_id":"sup_c591830aa1e22b900eb3","text":"{\"blocking_evidence\":null,\"headline\":\"sending and resurrection fields become contrast\",\"reader_payoff\":\"The reader notices that a root field used for sending messengers and raising the dead is redirected here into a destructive human rising.\",\"reason\":\"Messenger-sending references (2:129; 62:2) and resurrection references (17:49; 22:7; 36:52) are valid contrastive background, while the local Form VII verb remains the culprit's rising.\",\"representative_source_ids\":[\"QI-9500acd8\",\"QI-ecad0027\",\"MI-09ebb50f\",\"ME-db4883ce\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:1:trigger-moment","source_type":"word_analysis","support_id":"sup_c67d298accc0639e080a","text":"{\"blocking_evidence\":null,\"headline\":\"moment where transgression becomes event\",\"reader_payoff\":\"The reader notices that the particle does more than date the action; it pinpoints the instant when a moral condition becomes enacted movement.\",\"reason\":\"The temporal function is locally forced, and the boundary rows coherently connect the time-marker to the preceding abstract transgression in 91:11.\",\"representative_source_ids\":[\"QS-970ba8c9\",\"QS-a3547fbd\",\"QB-c51cc192\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:1:opening-frame-and-compression","source_type":"word_analysis","support_id":"sup_d8af9ffaa78faed0087d","text":"{\"blocking_evidence\":null,\"headline\":\"first beat of the compressed clause\",\"reader_payoff\":\"The reader feels the clause begin with dependence before action or actor, making the short sequence move as time, motion, and agent.\",\"reason\":\"The particle is the first word of a three-word temporal clause, and the following verb and subject fill the frame it opens.\",\"representative_source_ids\":[\"QT-3689419a\",\"QT-aff6844a\",\"QB-7c970f81\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:3:ruin-cause-and-result","source_type":"word_analysis","support_id":"sup_ecf5237bfe0fafe233b7","text":"{\"blocking_evidence\":null,\"headline\":\"wretchedness before and through the act\",\"reader_payoff\":\"The reader notices that the word can describe the ruined condition behind the act and the ruin exposed or activated by the act.\",\"reason\":\"The local word remains an elative subject, while related causative and abstract-state evidence can survive as pressure around how ruin leads into and is confirmed by the action.\",\"representative_source_ids\":[\"QS-c7095741\",\"QS-fa2815b2\",\"MS-2c363cbc\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:3:controlled-forward-ambiguity","source_type":"word_analysis","support_id":"sup_f46a6dac9462bb0ebfaf","text":"{\"blocking_evidence\":null,\"headline\":\"forward pressure toward the she-camel\",\"reader_payoff\":\"The reader can hear a secondary forward pull toward the she-camel in 91:13 while keeping the prior collective as the primary referent.\",\"reason\":\"The primary antecedent is the prior collective in 91:11, but the later feminine referent {{ar:نَاقَةَ}} ({{tr:nāqata}}) in 91:13 can create controlled forward pressure without replacing the local antecedent.\",\"representative_source_ids\":[\"QG-f82f44b7\",\"MG-b92cb352\",\"QS-8fc9a5b4\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:3:anonymized-moral-rank","source_type":"word_analysis","support_id":"sup_f48d68d34341ddc156ee","text":"{\"blocking_evidence\":null,\"headline\":\"moral rank replaces biography\",\"reader_payoff\":\"The reader notices that the ayah explains the act by moral extremity rather than by naming the culprit's biography.\",\"reason\":\"The final word is an elative person-label with a suffix, not a personal name or abstract noun.\",\"representative_source_ids\":[\"QT-96284b88\",\"QF-dc37f426\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"91:12:2:1","source_type":"qac_morpheme","support_id":"sup_f5e040feb69c4b698dd7","text":"{\"lemma_ar\":\"ٱنۢبَعَثَ\",\"morph_features\":\"STEM|POS:V|PERF|(VII)|LEM:{n[baEava|ROOT:bEv|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"91:12:2:1\",\"qac_word_ref\":\"91:12:2\",\"root_ar\":\"ب ع ث\",\"surface_ar\":\"ٱنۢبَعَثَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:3:delayed-closure-identity","source_type":"word_analysis","support_id":"sup_f7544cad71a5be50e486","text":"{\"blocking_evidence\":null,\"headline\":\"final position makes moral identity land\",\"reader_payoff\":\"The reader feels the action before the actor and then receives the culprit's moral rank as the clause's landing.\",\"reason\":\"The verb precedes the subject, and the ayah ends on the elative subject, making the final word both grammatical resolution and moral closure.\",\"representative_source_ids\":[\"QT-2e871d98\",\"QT-abd42551\",\"MT-bc0902f1\",\"QY-674f3ed9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:12:2:form-vii-not-commissioned-dispatch","source_type":"word_analysis","support_id":"sup_fc9a1ae7700441793530","text":"{\"blocking_evidence\":null,\"headline\":\"Form VII internalizes the motion\",\"reader_payoff\":\"The reader notices that the chosen form makes the motion arise from the actor, while excluding a grammar of mutual rousing or formal commissioning.\",\"reason\":\"The local surface is Form VII {{ar:ٱنۢبَعَثَ}} ({{tr:inbaʿatha}}), not simple Form I dispatch, Form IV commissioning, or a mutual rousing form.\",\"representative_source_ids\":[\"QF-0bd4fc16\",\"QF-4b702a70\",\"QF-79452d9d\",\"QF-ffa4a7ac\",\"MF-e61a2b7b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا","ayah_ref":"91:12"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000129/B004","root_000809/B001"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000129","role":"Setting out and pressing onward gives the event a self-propelled kinetic onset.","root":"ب ع ث","source_ref":"91:12","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000809","role":"Wretchedness opposed to happiness supplies the qualitative extreme carried by the moving subject.","root":"ش ق و","source_ref":"91:12","source_word_indices":["3"]}],"changed_reading":{"after":"When the collective's wretched extreme turned from a rank within it into its advancing edge.","before":"When its most wretched one rose."},"confidence":"strong","focus_anchor":"ٱنۢبَعَثَ supplies an intransitive onset of motion, while أَشْقَىٰهَا selects a superlative extreme belonging to the collective.","mechanism":"The subject is first a ranked quality within a group and then becomes its moving edge: the collective's wretched extreme converts from latent status into self-propelled action.","model_id":"baseline_kinetic_extreme"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_kinetic_extreme","source_type":"hft","support_id":"sup_fcdfd00ae2b0ea1c1510","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا","ayah_ref":"91:12"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000129/B001","root_000808/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000129","role":"Rousing a still or restrained thing supplies the transition from latency to agitation.","root":"ب ع ث","source_ref":"91:12","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000808","role":"Hardship, fatigue, and strenuous handling make the activated extreme hardship-formed rather than merely morally labeled.","root":"ش ق و","source_ref":"91:12","source_word_indices":["3"]}],"changed_reading":{"after":"A dormant, hardship-formed capacity was roused into consequential motion.","before":"A bad individual simply stood up."},"confidence":"medium","focus_anchor":"The reflexive motion of ٱنۢبَعَثَ is read against the focus inventory's waking-from-stillness image, and أَشْقَىٰهَا against strenuous hardship.","mechanism":"The event is activation rather than mere standing: something dormant or restrained is stirred, and what is stirred is the member or capacity most formed by difficulty and struggle.","model_id":"baseline_roused_hardship"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_roused_hardship","source_type":"hft","support_id":"sup_1c7fc6154f1a05447e6d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا","ayah_ref":"91:12"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000129/B002","root_000808/B003"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000129","role":"Dispatch and direction toward a task keep a mission-shaped reading available beneath the intransitive form.","root":"ب ع ث","source_ref":"91:12","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000808","role":"Prevailing in a hardship contest recasts the superlative as a perverse champion or selected extreme.","root":"ش ق و","source_ref":"91:12","source_word_indices":["3"]}],"changed_reading":{"after":"A hardship-contest extreme set out as though directed toward a role or task.","before":"An isolated villain acted on private impulse."},"confidence":"exploratory","focus_anchor":"ٱنۢبَعَثَ can retain an echo of being directed toward a task, while the dominant ش ق و mapping carries prevailing in a contest of hardship.","mechanism":"The focus alone permits a social-role possibility: the extreme actor is not just impulsive but resembles a contestant who has prevailed in harsh struggle and now goes out as a task-directed agent.","model_id":"baseline_dispatched_contestant"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_dispatched_contestant","source_type":"hft","support_id":"sup_31a285eb0e42c6aa5667","trust":"legacy_unbound"}]}
</lane_packet_json>
