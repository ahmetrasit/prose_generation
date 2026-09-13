# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **90:16**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s090-regular-20260912/s090/90_16/micro.discovery.json` and modify nothing
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
  "ayah_ref": "90:16",
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
{"analysis_context":{"analysis_id":"s090-regular-20260912","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"90:16","host_surah":90,"lane_context_refs":[],"ordered_context_refs":["90:1","90:2","90:3","90:4","90:5","90:6","90:7","90:8","90:9","90:10","90:11","90:12","90:13","90:14","90:15","90:17","90:18","90:19","90:20","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Çekirdek toprak ve yerdir; yoksulluk, yaşıtlık, göğüs kemikleri, parmak uçları, bitki ve yer adları ayrı dallardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000178/B001","candidate_links":[{"candidate_id":"cand_16ac7270564b8253f787","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَتْرَبَة","morph_features":"STEM|POS:N|LEM:matorabap|ROOT:trb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:4:1","qac_word_ref":"90:16:4","surface_ar":"مَتْرَبَةٍ"}],"gloss":"toprak ve toprağa bağlı kullanımlar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Toprak maddesi ve onun adları bu dalın temel alanıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yerin kendisi veya toprağın görünen yüzü de aynı alana girer."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir nesnenin toprağa bulanması veya üzerine toprak gelmesi eylem alanını oluşturur."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Toprak taşıyan rüzgar ve ölünün gömü yeri, toprakla temas üzerinden bağlı kullanımlardır."}}],"root_ar":"ت ر ب","root_id":"root_000178","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Toprak maddesini, yer yüzeyini ve toprağa bulaşma ya da toprakla gelen yan kullanımları birlikte anlatırken uygundur.","boundary_detail":"Çekirdek toprak ve yerdir; yoksulluk, yaşıtlık, göğüs kemikleri, parmak uçları, bitki ve yer adları ayrı dallardır.","branch_image_ar":"التراب والأرض والغبار","concept_gloss":"toprak ve toprağa bağlı kullanımlar","contextual_glosses":[{"applicability":"Madde adı veya toprağın kendisi anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yer yüzeyi, bulaşma, rüzgar ve gömü yeri kullanımlarını dışarıda bırakır.","preserves":"Toprak maddesi çekirdeğini korur."},"facet_ids":["F001"],"text":"toprak","usage_role":"general"},{"applicability":"Bir şeyin üzerine toprak gelmesi veya toprağa kirlenmesi bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Toprak maddesi ve yer anlamını bağımsız ad olarak vermez.","preserves":"Bulaşma ve temas eylemini korur."},"facet_ids":["F003"],"text":"toprağa bulanmak","usage_role":"contextual"},{"applicability":"Rüzgarın toprak getirdiği özel bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Rüzgarın toprak getirmesi koşulunu korur."},"facet_ids":["F004"],"text":"toprak taşıyan rüzgar","usage_role":"contextual"}],"definition":"Toprak, yerin toprak yüzeyi ve bir şeyin toprağa bulaşması bu dalın çekirdeğidir; ayrıca toprak getiren rüzgar ve ölünün toprakla örtülü gömü yeri bu çekirdeğe bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Toprak maddesi ve onun adları bu dalın temel alanıdır."},{"facet_id":"F002","role":"extension","statement":"Yerin kendisi veya toprağın görünen yüzü de aynı alana girer."},{"facet_id":"F003","role":"associated_use","statement":"Bir nesnenin toprağa bulanması veya üzerine toprak gelmesi eylem alanını oluşturur."},{"facet_id":"F004","role":"associated_use","statement":"Toprak taşıyan rüzgar ve ölünün gömü yeri, toprakla temas üzerinden bağlı kullanımlardır."}],"identity_rationale":"Kaynak ifadesi toprağın kendi adlarını, yerin kendisini, bir şeyin toprağa bulaşmasını, toprak taşıyan rüzgarı ve ölünün gömü yerini birlikte verir. Bu yüzden dal yalnızca kuru madde adı değil, toprakla doğrudan temas eden birkaç kullanımı da kapsar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"toprak ve toprağın değişik adları"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yerin kendisi veya toprağın kendisi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yer toprağının yüzü veya toprak yapısı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir şeyin toprağa bulanması"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bir şeyi toprakla bulamak veya düzeltmek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bir şeyin üzerine toprak koymak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"toprak taşıyan rüzgar"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"ölünün toprakla örtülü gömü yeri"}],"lexicalization_note":"Tanım çıplak toprak ve yer anlamını korur; rüzgar ve ölünün gömü yeri gibi kullanımlar yapıya bağlı yan kullanımlar olarak tutulur.","neighbor_coverage_note":"Adayların tümü toprak, yer, madde, beden veya aynı kökün diğer dalları üzerinden gözden geçirildi; yalnızca sınırı belirginleştiren yakın toprak dalları ve yoksulluk dalı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Okur bunları toprak anlamında yakın görebilir, fakat bu dalın bağlı kullanımları toprağa bulaşma ve gömü yeri yönüne açılır; komşu dal ise yer yüzeyi ve yüzeyle temas yönünde örgütlenir.","focus_only":"Bu dal toprağa bulaşma, toprak getiren rüzgar ve ölünün gömü yeri gibi kullanımları da taşır.","gloss":"yer yüzü ve toprak","neighbor_only":"Komşu dalda yer yüzü, tozlu yüzey ve ayakların yere ulaşması gibi kendi özel uzantıları vardır.","neighbor_ref":"root_001030/B001","relation_type":"near_synonym","shared_zone":"İki dal da toprak ve yer yüzeyi alanında buluşur."},{"boundary_match":"thematic_only","distinction":"Paylaşım sadece imgeseldir: burada toprak gerçek madde veya yer alanıdır, komşuda ise geçim darlığının anlatımına dönüşür.","focus_only":"Bu dal toprağın maddesini ve yerle ilişkisini adlandırır.","gloss":"toprak ile yoksulluk","neighbor_only":"Komşu dal yoksulluğu, toprağa yapışmış olma imgesiyle anlatır.","neighbor_ref":"root_000178/B002","relation_type":"thematic","shared_zone":"İki dalda da toprak imgesi bulunur."},{"boundary_match":"partial","distinction":"Yakınlık toprağın kendisindedir; bu dal toprağa bulaşan nesne, toprak taşıyan rüzgar ve gömü yeri gibi kullanımlar kurarken komşu dal yüzey ve açık zemin yönünde genişler.","focus_only":"Bu dal toprağın adlarını ve toprağa bulaşma kullanımlarını içerir.","gloss":"toprak ve yer yüzü","neighbor_only":"Komşu dal belirgin biçimde yerin yüzeyi, açık veya düz yer ve yol alanına uzanır.","neighbor_ref":"root_000862/B004","relation_type":"near_synonym","shared_zone":"Toprak ve yer yüzeyi anlamları ortak alandır."}],"source_phrase_ar":"التراب وهو التيرب والتوراب (maqayis)؛ التراب والتيرب والتورب كله من أسماء التراب (jamhara)؛ الترباء الأرض نفسها (maqayis;sihah;mufradat)؛ ترب الشيء أصابه التراب (sihah)؛ تترب إذا تلوث في التراب (tahdhib)؛ ريح تربة جاءت بالتراب (maqayis;sihah;mufradat)؛ تربة الميت رمسه (jamhara)","source_summary":"Toplu kanıt, toprağın adlarını ve yerle ilişkisini ortak çekirdek olarak verir; bulaşma, toprak getiren rüzgar ve ölünün gömü yeri bu çekirdeğe bağlı kullanımlardır.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"التراب وأسماؤه والترباء والأرض والغبار والتلطخ بالتراب وريحه وتربة الميت","what_is_not_ar":"الفقر والغنى؛ الأتراب اللدات؛ الترائب والأنامل؛ النبات والمواضع"},"support_links":["sup_6c7bebbe0510e7ee6c6a"]},{"boundary":"Çekirdek yoksulluk ve düşkünlüktür; kalıplaşmış söz bu çekirdeğe bağlı söz kullanımıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000178/B002","candidate_links":[{"candidate_id":"cand_be651fe27538963c049a","lane":"micro"},{"candidate_id":"cand_36aa152bde7319a39696","lane":"micro"},{"candidate_id":"cand_9a5d0e08f611f381e4e7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَتْرَبَة","morph_features":"STEM|POS:N|LEM:matorabap|ROOT:trb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:4:1","qac_word_ref":"90:16:4","surface_ar":"مَتْرَبَةٍ"}],"gloss":"toprağa düşmüş yoksulluk","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yoksulluk ve geçim darlığı dalın temel anlamıdır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Toprağa yapışmış olma imgesi, yoksulluğun bedensel ve mekansal anlatımıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kalıplaşmış söz görünüşte yoksulluk dileği taşır, fakat her zaman gerçek dilek değildir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Az mal anlamı yanında aynı biçimin başka dalda çok mal anlamıyla karşılaşması ayrı tutulmalıdır."}}],"root_ar":"ت ر ب","root_id":"root_000178","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yoksulluğu toprağa yapışma veya yere düşmüşlük imgesiyle anlatan çekirdek için uygundur.","boundary_detail":"Çekirdek yoksulluk ve düşkünlüktür; kalıplaşmış söz bu çekirdeğe bağlı söz kullanımıdır.","branch_image_ar":"الفقر بلصوق التراب","concept_gloss":"toprağa düşmüş yoksulluk","contextual_glosses":[{"applicability":"Kişinin geçim darlığına düşmesi anlatıldığında doğal fiil karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Toprağa yapışma imgesini ve kalıplaşmış söz kullanımını vermez.","preserves":"Yoksulluk çekirdeğini korur."},"facet_ids":["F001"],"text":"yoksullaşmak","usage_role":"general"},{"applicability":"Görünüşte yoksulluk dileği olan kalıplaşmış söz için bağlamsal Türkçe karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Her zaman gerçek dilek olmayabileceği ayrıntısını tek başına göstermez.","preserves":"Sözün beddua görünen yönünü korur."},"facet_ids":["F003"],"text":"elin boş kalsın","usage_role":"contextual"}],"definition":"Yoksulluğa düşmek, geçim darlığı içinde toprağa yapışmış gibi olmak bu dalın çekirdeğidir. Kalıplaşmış söz kullanımı görünüşte yoksulluk dileği taşır, fakat bağlama göre uyarı veya vurgulama olarak da işler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yoksulluk ve geçim darlığı dalın temel anlamıdır."},{"facet_id":"F002","role":"associated_use","statement":"Toprağa yapışmış olma imgesi, yoksulluğun bedensel ve mekansal anlatımıdır."},{"facet_id":"F003","role":"associated_use","statement":"Kalıplaşmış söz görünüşte yoksulluk dileği taşır, fakat her zaman gerçek dilek değildir."},{"facet_id":"F004","role":"source_variant","statement":"Az mal anlamı yanında aynı biçimin başka dalda çok mal anlamıyla karşılaşması ayrı tutulmalıdır."}],"identity_rationale":"Kaynak ifadesi yoksulluğu toprağa yapışma imgesiyle açıklar ve ayrıca kalıplaşmış sözde görünen beddua ile gerçek dilek olmayan uyarı kullanımını birlikte anar. Dal kullanılabilir, fakat kalıplaşmış sözün bütün dalı gerçek beddua gibi göstermemesi gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"toprağa yapışmış gibi yoksullaşmak"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yoksulluk, düşkünlük ve geçim darlığı"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yoksulluktan toprağa yapışmış düşkün kimse"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"görünüşte yoksulluk dileği olan kalıplaşmış söz"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"az mal sahibi olma"}],"lexicalization_note":"Tanım çıplak yoksullaşma biçimlerini ve kalıplaşmış sözleri ayırır; söz kalıbını genel yoksulluk anlamı yerine koymaz.","neighbor_coverage_note":"Yoksulluk adaylarının tümü ve aynı kökün toprak, varlık ve diğer dalları karşılaştırıldı; yayımlananlar gerçek anlam sınırını gösterenlerdir.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Aynı alanın iki karşı yönüdür: bu dal eksilme ve yoksulluğa düşme, komşu dal ise çoğalma ve varlıklı hale gelme anlamı taşır.","focus_only":"Bu dal mal yokluğu ve düşkünlük yönündedir.","gloss":"yoksulluk ile varlıklılık","neighbor_only":"Komşu dal çok mal sahibi olma ve varlıklı hale gelme yönündedir.","neighbor_ref":"root_000178/B003","relation_type":"polarity_pair","shared_zone":"İki dal da kişinin mal durumu üzerinden anlaşılır."},{"boundary_match":"partial","distinction":"Yerine geçebilir oldukları yerler vardır, fakat bu dalın ayırt edici sınırı toprak imgesi ve kalıplaşmış söz kullanımıdır.","focus_only":"Bu dal yoksulluğu toprağa yapışma imgesi ve kalıplaşmış sözle bağlar.","gloss":"yoksulluk ve ihtiyaç","neighbor_only":"Komşu dal yoksullukla birlikte ihtiyaç, sıkıntı ve kötü hal alanını daha genel verir.","neighbor_ref":"root_000365/B002","relation_type":"near_synonym","shared_zone":"İki dalda yoksulluk ve ihtiyaç ortak alan oluşturur."},{"boundary_match":"partial","distinction":"Bu dalın ölçütü toprağa yapışmış yoksulluk imgesidir; komşu dal daha çok düşkün duruş ve güçsüzlük davranışını kapsar.","focus_only":"Bu dal toprakla ilişkilendirilen yoksulluk imgesini taşır.","gloss":"yoksulluk ve düşkünlük","neighbor_only":"Komşu dal yoksulluk yanında zayıflık, boyun eğme ve düşkün duruşu öne çıkarır.","neighbor_ref":"root_000726/B006","relation_type":"near_synonym","shared_zone":"İki dal geçim darlığı ve düşkünlük alanında yakınlaşır."}],"source_phrase_ar":"ترب الرجل إذا افتقر كأنه لصق بالتراب (maqayis;sihah;mufradat)؛ المتربة الفقر (jamhara)؛ مسكين ذو متربة أي لاصق بالتراب (sihah;mufradat)؛ رجل ترب فقير (tahdhib)؛ تربت يداك (sihah;tahdhib;mufradat)","source_summary":"Toplu kanıt yoksulluğu ve düşkünlüğü toprağa yapışma imgesiyle açıklar; kalıplaşmış söz ise kimi yerde gerçek beddua, kimi yerde konuşma vurgusu olarak değerlendirilir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"الفقر والمسكنة والحاجة واللصوق بالتراب وصيغة تربت يداك","what_is_not_ar":"الغنى وكثرة المال؛ التراب نفسه؛ الأتراب اللدات؛ الترائب"},"support_links":["sup_49916f564214d41f785d","sup_5f93873b9ef4550e8a28","sup_c0ee4e992d753eb99c0b"]},{"boundary":"Çekirdek varlıklı olmak ve malın çoğalmasıdır; toprak maddesi veya yoksulluk anlamı bu dala katılmaz.","branch_kind":"bare","branch_ref":"root_000178/B003","candidate_links":[{"candidate_id":"cand_9a5d0e08f611f381e4e7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَتْرَبَة","morph_features":"STEM|POS:N|LEM:matorabap|ROOT:trb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:4:1","qac_word_ref":"90:16:4","surface_ar":"مَتْرَبَةٍ"}],"gloss":"varlıklı hale gelmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin varlıklı olması ve malının çoğalması temel anlamdır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Toprak kadar çok olma imgesi, mal çokluğunu açıklayan bağımlı bir gerekçedir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı biçimin az mal anlamıyla karşılaşması yoksulluk dalında tutulur."}}],"root_ar":"ت ر ب","root_id":"root_000178","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin malının çoğalması ve geçim bakımından bolluğa erişmesi anlatıldığında uygundur.","boundary_detail":"Çekirdek varlıklı olmak ve malın çoğalmasıdır; toprak maddesi veya yoksulluk anlamı bu dala katılmaz.","branch_image_ar":"الغنى بكثرة التراب","concept_gloss":"varlıklı hale gelmek","contextual_glosses":[{"applicability":"Özellikle çok mala sahip olma yönü vurgulandığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mal çokluğu ve artış fikrini korur."},"facet_ids":["F001"],"text":"malca çoğalmak","usage_role":"contextual"}],"definition":"Kişinin varlıklı hale gelmesi veya malının çok olması bu dalın çekirdeğidir; toprak kadar çok olma imgesi yalnızca bolluğu açıklayan arka plandır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin varlıklı olması ve malının çoğalması temel anlamdır."},{"facet_id":"F002","role":"associated_use","statement":"Toprak kadar çok olma imgesi, mal çokluğunu açıklayan bağımlı bir gerekçedir."},{"facet_id":"F003","role":"source_variant","statement":"Aynı biçimin az mal anlamıyla karşılaşması yoksulluk dalında tutulur."}],"identity_rationale":"Kaynak ifadesi kişinin varlıklı olması ve malının çokluğu üzerinde birleşir; toprak kadar çok olma açıklaması yalnızca imgeleyici gerekçedir. Dal yoksulluk dalının karşı yönünde, çok mal sahibi olma anlamına oturur.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"varlıklı olmak ve malı çoğalmak"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"çok mal sahibi olma"}],"lexicalization_note":"Dal çıplak biçimlerde varlıklı olmayı anlatır; herhangi bir söz kalıbına veya özel bağlama bağlı değildir.","neighbor_coverage_note":"Varlık ve çokluk adayları ile aynı kökün yoksulluk dalı gözden geçirildi; yayımlanan ilişkiler karşıtlık ve en yakın çokluk ayrımlarını verir.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Bu dal bolluğa ve varlıklı hale gelmeye, komşu dal eksilmeye ve toprağa düşmüş yoksulluğa yönelir.","focus_only":"Bu dal çok mal sahibi olma yönündedir.","gloss":"varlık ile yoksulluk","neighbor_only":"Komşu dal geçim darlığı ve yoksulluğa düşme yönündedir.","neighbor_ref":"root_000178/B002","relation_type":"polarity_pair","shared_zone":"İki dal kişinin mal durumu ekseninde karşılaşır."},{"boundary_match":"partial","distinction":"Bu dal mal sahibi olma sonucuna daha dar bağlıdır; komşu dal hem mal hem sayı ve topluluk çoğalmasını daha geniş kapsar.","focus_only":"Bu dal özellikle kişinin mal bakımından varlıklı hale gelmesini anlatır.","gloss":"varlık ve çoğalma","neighbor_only":"Komşu dal mal, sayı ve topluluk bakımından daha geniş çoğalma alanına sahiptir.","neighbor_ref":"root_000198/B002","relation_type":"near_synonym","shared_zone":"İki dal varlık ve çokluk anlamında örtüşür."},{"boundary_match":"partial","distinction":"Bu dalın odağı kişinin varlıklı olmasıdır; komşu dal malın çokluğu ve birikimi üzerinde daha nesnel bir alan kurar.","focus_only":"Bu dal varlıklı hale gelme eylemini öne çıkarır.","gloss":"çok mal","neighbor_only":"Komşu dal birikmiş çok mal ve ona iyi bakma gibi alanları da taşır.","neighbor_ref":"root_000459/B001","relation_type":"near_synonym","shared_zone":"İki dal çok mal ve bolluk alanında buluşur."}],"source_phrase_ar":"أترب إذا استغنى كأنه صار له من المال بقدر التراب (maqayis;sihah;mufradat)؛ أترب الرجل إذا استغنى (jamhara)؛ أترب الرجل فهو مترب إذا كثر ماله (tahdhib)؛ التتريب كثرة المال (tahdhib)","source_summary":"Toplu kanıt, kişinin çok mala erişmesi veya varlıklı olması üzerinde birleşir; toprak imgesi çokluğu açıklayan mecazi dayanak olarak kalır.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"الغنى وكثرة المال بالفعل أترب وما قاربه","what_is_not_ar":"الفقر والمتربة؛ التراب نفسه؛ الأتراب والترائب"},"support_links":["sup_49916f564214d41f785d"]},{"boundary":"Dal yaşıt ve denk kişi ilişkisidir; toprak, yoksulluk, göğüs bölgesi ve beden parçalarıyla karıştırılmaz.","branch_kind":"bare","branch_ref":"root_000178/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَتْرَبَة","morph_features":"STEM|POS:N|LEM:matorabap|ROOT:trb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:4:1","qac_word_ref":"90:16:4","surface_ar":"مَتْرَبَةٍ"}],"gloss":"yaşıt ve denk arkadaş","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Aynı yaşta veya birlikte yetişmiş kişi temel anlamdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Denk, benzer veya eş düzeyde kimse anlamı yaşıtlık çekirdeğinden genişler."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Arkadaş veya yakın kişi anlamı, birlikte yetişme ve denklik bağından doğar."}}],"root_ar":"ت ر ب","root_id":"root_000178","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Aynı yaşta veya birlikte yetişmiş, bu yüzden denk sayılan kişi için uygundur.","boundary_detail":"Dal yaşıt ve denk kişi ilişkisidir; toprak, yoksulluk, göğüs bölgesi ve beden parçalarıyla karıştırılmaz.","branch_image_ar":"التساوي في السن والصحبة","concept_gloss":"yaşıt ve denk arkadaş","contextual_glosses":[{"applicability":"Yaş denkliği tek başına öne çıktığında en doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Arkadaşlık ve benzerlik uzantılarını belirtmez.","preserves":"Aynı yaşta olma çekirdeğini korur."},"facet_ids":["F001"],"text":"yaşıt","usage_role":"general"},{"applicability":"Benzerlik veya eş düzeylilik bağlamında, yaş ayrıntısı geri plandayken uygundur.","error_profile":{"adds":"Yaş veya birlikte yetişme koşulunu açıkça zorunlu kılmaz.","collision":null,"fit":"broadening","loses":null,"preserves":"Denklik ve benzerlik fikrini korur."},"facet_ids":["F002"],"text":"denk kişiler","usage_role":"contextual"}],"definition":"Aynı yaşta veya birlikte yetişmiş olup birbirine denk sayılan kişi, arkadaş ya da benzer bu dalın çekirdeğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Aynı yaşta veya birlikte yetişmiş kişi temel anlamdır."},{"facet_id":"F002","role":"extension","statement":"Denk, benzer veya eş düzeyde kimse anlamı yaşıtlık çekirdeğinden genişler."},{"facet_id":"F003","role":"associated_use","statement":"Arkadaş veya yakın kişi anlamı, birlikte yetişme ve denklik bağından doğar."}],"identity_rationale":"Kaynak ifadesi yaşıtlık, birlikte yetişme, arkadaşlık ve benzerlik alanlarını tek dalda toplar. Çekirdek, aynı yaş veya aynı yetişme düzeyinden gelen denk kişi ilişkisidir; sıradan arkadaşlık tek başına yeterli değildir.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yaşıt, birlikte yetişmiş arkadaş veya denk kişi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yaşıtlar veya denk kişiler"}],"lexicalization_note":"Dal çıplak ad ve çoğul biçimlerle işler; tanım özel bir kalıba bağlı değildir.","neighbor_coverage_note":"Benzerlik, denklik, arkadaşlık ve aynı kökün diğer dalları karşılaştırıldı; yayımlananlar yaşıtlık sınırını en iyi ayıran adaylardır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kanıta göre sınırlar örtüşür; iki dal yaşıt kişi için birbirinin yerine kullanılabilir.","focus_only":null,"gloss":"yaşıt","neighbor_only":null,"neighbor_ref":"root_001683/B006","relation_type":"synonym","shared_zone":"İki dal da doğum veya yaş denkliği üzerinden yaşıt kişiyi anlatır."},{"boundary_match":"partial","distinction":"Bu dalın okur sınırı yaşıtlık ve birlikte yetişmedir; komşu dal aynı işi, biçimi veya hali paylaşan benzerleri de içine alır.","focus_only":"Bu dal yaş veya birlikte yetişme denkliğini özellikle taşır.","gloss":"denk ve benzer","neighbor_only":"Komşu dal şekil, iş veya durum ortaklığıyla kurulan eş ve benzerleri daha geniş kapsar.","neighbor_ref":"root_000652/B005","relation_type":"near_synonym","shared_zone":"İki dal benzerlik ve denklik alanında buluşur."},{"boundary_match":"field_only","distinction":"Bu dal arkadaşlığı yaş ve denklikten türetir; komşu dal birlikte bulunma ve eşlik etme davranışını merkeze alır.","focus_only":"Bu dal denk yaşıt kişiyi belirtir.","gloss":"arkadaşlık","neighbor_only":"Komşu dal yolculuk, meclis veya birlikte bulunma arkadaşlığını anlatır.","neighbor_ref":"root_000583/B002","relation_type":"same_field","shared_zone":"İki dal kişiler arası yakınlık ve birliktelik alanındadır."}],"source_phrase_ar":"الترب الخدن والجمع أتراب (maqayis)؛ الترب اللدة الذي ينشأ معك والجمع أتراب (jamhara)؛ هذه ترب هذه أي لدتها وهن أتراب (sihah)؛ أترابا أي أمثالا وهما تربان (tahdhib)؛ أتراب أي لدات تنشأن معا (mufradat)","source_summary":"Toplu kanıt, aynı yaşta olma ve birlikte yetişme fikrini merkeze alır; arkadaş, denk ve benzer anlamları bu merkezden genişler.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"الترب بمعنى اللدة والخدن والمثل والأتراب الذين نشؤوا معا","what_is_not_ar":"التراب والغبار؛ الفقر والغنى؛ الترائب والأنامل"},"support_links":[]},{"boundary":"Dal göğüs ön bölgesidir; toprak, yaşıtlar, parmak uçları ve bitki anlamları dışarıda kalır.","branch_kind":"bare","branch_ref":"root_000178/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَتْرَبَة","morph_features":"STEM|POS:N|LEM:matorabap|ROOT:trb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:4:1","qac_word_ref":"90:16:4","surface_ar":"مَتْرَبَةٍ"}],"gloss":"göğsün kolye yeri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Göğsün ön kemikleri ve kaburga bölgesi temel anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kolyenin göğüste durduğu yer bu anatomik bölgenin özel tarifidir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Köprücük kemiği ile meme ucu arası gibi daha dar sınırlar aynı bölgeyi belirginleştirir."}}],"root_ar":"ت ر ب","root_id":"root_000178","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Göğsün ön kemikleri ve kolyenin durduğu bölge birlikte kastedildiğinde uygundur.","boundary_detail":"Dal göğüs ön bölgesidir; toprak, yaşıtlar, parmak uçları ve bitki anlamları dışarıda kalır.","branch_image_ar":"ترائب الصدر وموضع القلادة","concept_gloss":"göğsün kolye yeri","contextual_glosses":[{"applicability":"Bölge kemikler veya kaburgalar üzerinden anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kolye yeri tarifini geri plana iter.","preserves":"Göğüs önündeki kemik alanını korur."},"facet_ids":["F001"],"text":"göğüs kemikleri","usage_role":"general"},{"applicability":"Teknik anatomik sınır gerekmeyen açıklayıcı bağlamda uygundur.","error_profile":{"adds":"Kemikli veya kolye yeri olma sınırını daha gevşek bırakır.","collision":null,"fit":"broadening","loses":null,"preserves":"Göğüs önünde yer alma bilgisini korur."},"facet_ids":["F001","F002"],"text":"göğsün ön bölgesi","usage_role":"explanatory"}],"definition":"Göğsün ön tarafında, kolyenin durduğu yer veya köprücük kemiği çevresinden meme ucuna kadar uzanan kemikli bölge bu dalın çekirdeğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Göğsün ön kemikleri ve kaburga bölgesi temel anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Kolyenin göğüste durduğu yer bu anatomik bölgenin özel tarifidir."},{"facet_id":"F003","role":"specialization","statement":"Köprücük kemiği ile meme ucu arası gibi daha dar sınırlar aynı bölgeyi belirginleştirir."}],"identity_rationale":"Kaynak ifadesi göğüs bölgesindeki kemikler, kolye yeri ve köprücük ile meme ucu arası gibi yakın anatomik tanımları birlikte verir. Bu yüzden dal göğsün ön kısmındaki belirli kemikli veya kolye taşıyan bölge olarak tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"göğüs kemikleri veya göğüste kolye yeri"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"göğüste kemik uçlarının denk durduğu bölge"}],"lexicalization_note":"Dal çıplak adlarla göğüs bölgesini belirtir; tanım özel bir deyime bağlı değildir.","neighbor_coverage_note":"Göğüs, kemik, kolye yeri ve aynı kökün diğer dalları karşılaştırıldı; yayımlananlar anatomik sınırı belirginleştiren adaylardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kemik ve kolye yerini merkeze alır; komşu dal üst göğüs, boyun altı ve kesim yeri gibi daha geniş bir beden bölgesi kurar.","focus_only":"Bu dal göğüs önündeki kemikler ve kolye yeri üzerine daralır.","gloss":"göğüs ve boyun altı","neighbor_only":"Komşu dal kesim yeri, üst göğüs ve boyun altı alanını daha geniş kapsar.","neighbor_ref":"root_001479/B001","relation_type":"near_synonym","shared_zone":"İki dal göğsün ön ve üst bölgesi ile kolye yeri alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dal anatomik kemik bölgesine bağlıdır; komşu dal aynı yerden hareketle boyun altı ve ilgili eylemlere uzanır.","focus_only":"Bu dal göğüs kemikleri ve kolye yeri olarak tarif edilir.","gloss":"kolye yeri","neighbor_only":"Komşu dal boyun altı, kolye yeri ve tutma ya da vurma gibi eylem bağlantılarını da içerir.","neighbor_ref":"root_001338/B005","relation_type":"near_synonym","shared_zone":"İki dal kolyenin durduğu göğüs bölgesinde örtüşür."},{"boundary_match":"field_only","distinction":"Aynı anatomik alanda olsalar da bu dal göğüs önüne ve kolye yerine, komşu dal kaburgaların yan bağlantısına yönelir.","focus_only":"Bu dal göğüs önü ve kolye yerini belirtir.","gloss":"göğüs kaburgaları","neighbor_only":"Komşu dal göğüs kaburgalarının yan kısımlarını ve onların kırılmasıyla ilişkili kullanımı kapsar.","neighbor_ref":"root_000263/B005","relation_type":"same_field","shared_zone":"İki dal göğüs kemikleri alanındadır."}],"source_phrase_ar":"التريب الصدر عند تساوي رءوس العظام (maqayis)؛ التريبة مجال القلادة في الصدر والجمع الترائب (jamhara)؛ التريبة واحدة الترائب وهي عظام الصدر ما بين الترقوة إلى الثندؤة (sihah)؛ الترائب موضع القلادة من الصدر (tahdhib)؛ الترائب ضلوع الصدر الواحدة تريبة (mufradat)","source_summary":"Toplu kanıt, göğüs önündeki kemikli bölgeyi ve kolyenin durduğu yeri aynı dalda toplar; ayrıntılar bölgenin alt sınırlarını farklı biçimde tarif eder.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"الترائب والتريب والتريبة لعظام الصدر وموضع القلادة وما بين الترقوة والثندؤة","what_is_not_ar":"التراب والغبار؛ الأتراب اللدات؛ الأنامل؛ النبات"},"support_links":[]},{"boundary":"Dal parmak uçlarıyla sınırlıdır; göğüs bölgesi, toprak, yaşıtlık ve bitki anlamları ayrıdır.","branch_kind":"bare","branch_ref":"root_000178/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَتْرَبَة","morph_features":"STEM|POS:N|LEM:matorabap|ROOT:trb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:4:1","qac_word_ref":"90:16:4","surface_ar":"مَتْرَبَةٍ"}],"gloss":"parmak uçları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Parmak uçları dalın temel ve sınırlı anlamıdır."}}],"root_ar":"ت ر ب","root_id":"root_000178","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Parmakların uç kısımları veya tek tek parmak ucu kastedildiğinde uygundur.","boundary_detail":"Dal parmak uçlarıyla sınırlıdır; göğüs bölgesi, toprak, yaşıtlık ve bitki anlamları ayrıdır.","branch_image_ar":"تربات الأنامل","concept_gloss":"parmak uçları","contextual_glosses":[{"applicability":"Tekil bir parmak ucundan söz edildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tekil parmak ucu anlamını korur."},"facet_ids":["F001"],"text":"parmak ucu","usage_role":"contextual"}],"definition":"Parmakların uç kısımları veya her bir parmak ucu bu dalın tek çekirdeğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Parmak uçları dalın temel ve sınırlı anlamıdır."}],"identity_rationale":"Kaynak ifadesi dalı açık biçimde parmak uçları olarak verir ve tekil biçimin buna bağlı olduğunu belirtir. Başka beden parçaları veya toprak anlamları bu dalın içine girmez.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"parmak uçları; tekili parmak ucu"}],"lexicalization_note":"Dal çıplak adla parmak uçlarını anlatır; özel bir kalıp veya bağlama bağlı değildir.","neighbor_coverage_note":"Parmak, el ve beden ucu adayları ile aynı kökün diğer dalları değerlendirildi; yayımlananlar parmak ucu sınırını açıklayanlardır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kanıtlanan sınır aynı olduğundan parmak ucu bağlamında birbirinin yerine geçebilirler.","focus_only":null,"gloss":"parmak ucu","neighbor_only":null,"neighbor_ref":"root_001556/B005","relation_type":"synonym","shared_zone":"İki dal da parmakların uç kısmını veya her bir parmak ucunu anlatır."},{"boundary_match":"partial","distinction":"Bu dal dar olarak parmak uçlarını adlandırır; komşu dal parmak veya organ uçları anlamına genişleyebilir.","focus_only":"Bu dal parmak uçlarıyla sınırlıdır.","gloss":"parmaklar ve uçlar","neighbor_only":"Komşu dal parmaklar, uçlar ve daha geniş beden uçları alanına yayılabilir.","neighbor_ref":"root_000155/B003","relation_type":"near_synonym","shared_zone":"İki dal parmak ucu alanında örtüşür."},{"boundary_match":"field_only","distinction":"Bu dal parmağın uç kısmına bakar; komşu dal parmakların kemik ve eklem yapılarını adlandırır.","focus_only":"Bu dal parmak ucunu belirtir.","gloss":"parmak ucu ile eklem","neighbor_only":"Komşu dal parmak kemikleri ve eklemleri alanındadır.","neighbor_ref":"root_000737/B010","relation_type":"same_field","shared_zone":"İki dal el ve parmak anatomisi alanındadır."}],"source_phrase_ar":"التربات وهي الأنامل الواحدة تربة (maqayis)؛ التربات الأنامل الواحدة تربة (sihah)","source_summary":"Toplu kanıt, anlamı parmak uçları olarak sınırlar; tekil biçim her bir parmak ucunu gösterir.","sources":["MQ","SI"],"what_is_ar":"التربات بمعنى الأنامل والواحدة تربة","what_is_not_ar":"التراب والغبار؛ الترائب؛ الأتراب؛ النبات"},"support_links":[]},{"boundary":"Dal bir bitki adıdır; toprak, gömü yeri, yer adları ve yoksulluk anlamları buraya taşınmaz.","branch_kind":"bare","branch_ref":"root_000178/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَتْرَبَة","morph_features":"STEM|POS:N|LEM:matorabap|ROOT:trb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:4:1","qac_word_ref":"90:16:4","surface_ar":"مَتْرَبَةٍ"}],"gloss":"belirli bir bitki","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir bitki adı temel anlamdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kanıt bitki olduğunu söyler, fakat botanik ayrıntı sağlamaz."}}],"root_ar":"ت ر ب","root_id":"root_000178","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Adın bitki türü olarak kullanıldığı durumlarda uygundur.","boundary_detail":"Dal bir bitki adıdır; toprak, gömü yeri, yer adları ve yoksulluk anlamları buraya taşınmaz.","branch_image_ar":"نبت التُّرْبَة","concept_gloss":"belirli bir bitki","contextual_glosses":[{"applicability":"Tür özellikleri bilinmediğinde açıklayıcı karşılık olarak uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bitki olarak adlandırılma bilgisini korur."},"facet_ids":["F001","F002"],"text":"bitki adı","usage_role":"explanatory"}],"definition":"Belirli bir bitki türü veya bitki adı bu dalın tek çekirdeğidir; kanıt bitkinin ayrıntılı tür özelliklerini vermez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir bitki adı temel anlamdır."},{"facet_id":"F002","role":"source_variant","statement":"Kanıt bitki olduğunu söyler, fakat botanik ayrıntı sağlamaz."}],"identity_rationale":"Kaynak ifadesi bu dalı yalnızca belirli bir bitki adı olarak verir. Toprak veya yer anlamıyla biçim benzerliği olsa da kanıt dalın bitki adı olduğunu açıkça ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"belirli bir bitki adı"}],"lexicalization_note":"Dal çıplak ad biçimiyle bir bitkiyi belirtir; özel bir söz dizimine bağlı değildir.","neighbor_coverage_note":"Bitki adayları ve aynı kökün toprak ile yer adı dalları kontrol edildi; yayımlananlar yalnızca alan karışmasını önleyen ayrımlardır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Aynı alanı paylaşırlar, fakat kanıt aynı bitkiyi göstermez; bu dalın tür ayrıntısı verilmez.","focus_only":"Bu dal ayrıntısı verilmeyen belirli bir bitki adıdır.","gloss":"bitki adları","neighbor_only":"Komşu dal farklı ve bilinen bir bitki adını belirtir.","neighbor_ref":"root_000388/B003","relation_type":"same_field","shared_zone":"İki dal da bitki adlandırma alanındadır."},{"boundary_match":"field_only","distinction":"Bu dal özel ad gibi duran bir bitki adıdır; komşu dal bitkinin yapısal sınıfını anlatır.","focus_only":"Bu dal belirli bir bitki adıdır.","gloss":"bitki türü","neighbor_only":"Komşu dal sapsız bitki gibi daha sınıfsal bir bitki anlamı taşır.","neighbor_ref":"root_001475/B003","relation_type":"same_field","shared_zone":"İki dal bitki alanında buluşur."},{"boundary_match":"thematic_only","distinction":"Biçim benzerliği ve doğal alan ilişkisi anlam birliği kurmaz; bu dal bitki adıdır, komşu dal toprak ve yer adlandırmasıdır.","focus_only":"Bu dal bitki adıdır.","gloss":"bitki ile toprak","neighbor_only":"Komşu dal toprak ve yer anlamlarını taşır.","neighbor_ref":"root_000178/B001","relation_type":"thematic","shared_zone":"Bitki toprakla ilişkili bir alanda düşünülebilir."}],"source_phrase_ar":"التربة وهو نبت (maqayis)؛ التربة ضرب من النبت (jamhara)؛ التربة أيضا نبت (sihah)","source_summary":"Toplu kanıt, adı geçen biçimin bir bitki veya bitki türü olduğunu bildirir; daha ayrıntılı tür tanımı ortak kanıtta yer almaz.","sources":["MQ","JA","SI"],"what_is_ar":"التربة اسم نبت","what_is_not_ar":"التراب والأرض؛ تربة الميت؛ أسماء المواضع؛ الفقر"},"support_links":[]},{"boundary":"Dal adlandırılmış yerlerle sınırlıdır; toprak, gömü yeri, bitki ve durum anlamları dışarıda kalır.","branch_kind":"non_bare","branch_ref":"root_000178/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَتْرَبَة","morph_features":"STEM|POS:N|LEM:matorabap|ROOT:trb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:4:1","qac_word_ref":"90:16:4","surface_ar":"مَتْرَبَةٍ"}],"gloss":"belirli yer adları","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli yer adları dalın temel anlamıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kanıt bazı adlar için yakınlık veya vadi olma gibi coğrafi açıklama verir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Adlar birden çok yer biçimini kapsar; bunlar ortak bir genel isim anlamına indirgenmez."}}],"root_ar":"ت ر ب","root_id":"root_000178","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözcük biçimleri özel yer veya vadi adı olarak kullanıldığında uygundur.","boundary_detail":"Dal adlandırılmış yerlerle sınırlıdır; toprak, gömü yeri, bitki ve durum anlamları dışarıda kalır.","branch_image_ar":"مواضع تسمى بترب","concept_gloss":"belirli yer adları","contextual_glosses":[{"applicability":"Tek bir adın açıklayıcı karşılığı gerektiğinde, ad yüzeyi üretilmeden kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Birden çok adın bulunduğunu tek başına göstermez.","preserves":"Özel yer adı olma bilgisini korur."},"facet_ids":["F001"],"text":"bir yer adı","usage_role":"explanatory"},{"applicability":"Kanıtta vadi olarak açıklanan yer bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Vadi olmayan diğer yer adlarını kapsamaz.","preserves":"Coğrafi yer adı bilgisini korur."},"facet_ids":["F002"],"text":"vadi adı","usage_role":"contextual"}],"definition":"Belirli yerlerin veya vadilerin adı olarak kullanılan biçimler bu dalın çekirdeğidir; dal genel toprak ya da yer kavramı değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli yer adları dalın temel anlamıdır."},{"facet_id":"F002","role":"specialization","statement":"Kanıt bazı adlar için yakınlık veya vadi olma gibi coğrafi açıklama verir."},{"facet_id":"F003","role":"source_variant","statement":"Adlar birden çok yer biçimini kapsar; bunlar ortak bir genel isim anlamına indirgenmez."}],"identity_rationale":"Kaynak ifadesi birden çok yer adını ve bunların bazı coğrafi açıklamalarını verir. İlk yanıt yüzey biçimi üretmemeli; bu yüzden dal belirli yer adları olarak açıklanır, adların Türkçe biçimleri ise üretilmez.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"belirli bir yerin adı; yüzey biçimi burada üretilmez"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"belirli bir yer veya vadinin adı; yüzey biçimi burada üretilmez"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"belirli bir yerin adı; yüzey biçimi burada üretilmez"}],"lexicalization_note":"Tanım belirli ad biçimleriyle sınırlıdır; çıplak kök anlamı veya genel yer kavramı olarak genişletilmez.","neighbor_coverage_note":"Yer adı adayları, bitki ve toprak dalları değerlendirildi; yayımlananlar özel ad ile genel yer anlamını ayıran adaylardır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Aynı türden adlandırma alanındadırlar, fakat kanıt aynı yeri veya aynı ad ailesini göstermez.","focus_only":"Bu dal farklı belirli yer adlarını içerir ve yüzey biçimleri burada üretilmez.","gloss":"yer adları","neighbor_only":"Komşu dal başka bir şehir veya yer adını ve ona bağlı nispet biçimlerini kapsar.","neighbor_ref":"root_000197/B003","relation_type":"same_field","shared_zone":"İki dal özel coğrafi adlar alanındadır."},{"boundary_match":"field_only","distinction":"Alan ortaklığı dışında eş anlamlılık yoktur; her dal başka coğrafi adları taşır.","focus_only":"Bu dal kendi belirli yer adlarıyla sınırlıdır.","gloss":"özel yer adı","neighbor_only":"Komşu dal başka yer adlarını içerir.","neighbor_ref":"root_000006/B008","relation_type":"same_field","shared_zone":"İki dal yer adlandırması alanındadır."},{"boundary_match":"thematic_only","distinction":"Bu dal adlandırılmış coğrafi varlıkları verir; komşu dal yer veya toprak kavramını verir, özel ad üretmez.","focus_only":"Bu dal özel yer adlarıdır.","gloss":"yer adı ile yer","neighbor_only":"Komşu dal toprak ve yerin kendisini anlatır.","neighbor_ref":"root_000178/B001","relation_type":"thematic","shared_zone":"İki dalda yer alanı vardır."}],"source_phrase_ar":"يترب موضع قريب من اليمامة (jamhara;sihah)؛ تربة موضع لا تدخله الألف واللام (jamhara)؛ تربة واد من أودية اليمن (tahdhib)؛ تربان موضع معروف (jamhara)","source_summary":"Toplu kanıt, birkaç biçimin belirli yer veya vadi adı olarak kullanıldığını gösterir; ortak anlam genel yer değil, adlandırılmış coğrafi varlıklardır.","sources":["JA","SI","TA"],"what_is_ar":"أسماء المواضع يترب وتربة وتربان ونحوها","what_is_not_ar":"التراب والأرض؛ تربة الميت؛ النبات؛ الصفات والأحوال"},"support_links":[]},{"boundary":"Dal uysal deve niteliğidir; toprak, yoksulluk, yaşıtlık, göğüs bölgesi ve yer adları dışarıda kalır.","branch_kind":"bare","branch_ref":"root_000178/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَتْرَبَة","morph_features":"STEM|POS:N|LEM:matorabap|ROOT:trb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:4:1","qac_word_ref":"90:16:4","surface_ar":"مَتْرَبَةٍ"}],"gloss":"uysal deve","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Devenin uysal ve kolay yönetilir olması temel anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Nitelik hem erkek hem dişi deve için kullanılabilir."}}],"root_ar":"ت ر ب","root_id":"root_000178","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Erkek veya dişi devenin kolay yönetilir oluşu anlatıldığında uygundur.","boundary_detail":"Dal uysal deve niteliğidir; toprak, yoksulluk, yaşıtlık, göğüs bölgesi ve yer adları dışarıda kalır.","branch_image_ar":"التربوت الذلول","concept_gloss":"uysal deve","contextual_glosses":[{"applicability":"Hayvanın yönetilmesi veya sürülmesi bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kolay yönetilir deve niteliğini korur."},"facet_ids":["F001","F002"],"text":"kolay güdülen deve","usage_role":"contextual"}],"definition":"Erkek veya dişi devenin uysal, kolay güdülür ve yönetilir olması bu dalın çekirdeğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Devenin uysal ve kolay yönetilir olması temel anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Nitelik hem erkek hem dişi deve için kullanılabilir."}],"identity_rationale":"Kaynak ifadesi deve türünden hayvan için uysal ve kolay yönetilir olma niteliğini verir. Dal genel itaat veya bütün binek hayvanları değil, özellikle deveye uygulanan uysallık sıfatıdır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"uysal ve kolay yönetilir deve"}],"lexicalization_note":"Dal çıplak sıfat biçimiyle deve için uysallığı anlatır; özel bir kalıp şartı yoktur.","neighbor_coverage_note":"Deve, binek, itaat ve aynı kökün diğer dalları karşılaştırıldı; yayımlananlar hayvan adı ile uysallık niteliğini ayıran adaylardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal hayvan niteliği olarak deveyle sınırlıdır; komşu dal davranışsal itaat ve emre uyma anlamında daha geniştir.","focus_only":"Bu dal deveye uygulanan uysal sıfattır.","gloss":"uysallık ve itaat","neighbor_only":"Komşu dal insan veya şeyler için boyun eğme, itaat ve emre uyma alanını genel olarak kapsar.","neighbor_ref":"root_000956/B001","relation_type":"near_synonym","shared_zone":"İki dal kolay yönetilme ve karşı koymama alanında yakınlaşır."},{"boundary_match":"field_only","distinction":"Komşu dal hayvan adıdır; bu dal aynı hayvana uygulanabilen yönetilebilirlik niteliğidir.","focus_only":"Bu dal devenin uysal niteliğini anlatır.","gloss":"deve ve deve niteliği","neighbor_only":"Komşu dal devenin kendisini adlandırır.","neighbor_ref":"root_000132/B001","relation_type":"same_field","shared_zone":"İki dal deve alanındadır."},{"boundary_match":"field_only","distinction":"Bu dal davranış ve yönetilebilirliğe bakar; komşu dal yol gücü ve dayanıklılığa bakar.","focus_only":"Bu dal uysal ve kolay yönetilir deveyi belirtir.","gloss":"deve nitelikleri","neighbor_only":"Komşu dal yolculuğa dayanıklı ve güçlü yürüyüşlü deve alanındadır.","neighbor_ref":"root_000974/B006","relation_type":"same_field","shared_zone":"İki dal deveye verilen nitelikler alanındadır."}],"source_phrase_ar":"جمل تربوت وناقة تربوت أي ذلول (sihah)؛ بعير تربوت إذا كان ذلولا وناقة تربوت كذلك (tahdhib)","source_summary":"Toplu kanıt, erkek ve dişi deve için uysal, yumuşak huylu ve kolay yönetilir olma niteliğini ortak biçimde verir.","sources":["SI","TA"],"what_is_ar":"التربوت وصف للبعير أو الناقة الذلول","what_is_not_ar":"التراب والغبار؛ الفقر والغنى؛ الأتراب والترائب؛ المواضع"},"support_links":[]},{"boundary":"Bu dal yerleşme, ev halkı, yoksulluk ya da araç adlarını değil, hareketten sonra durma ve dinginleşmeyi anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000726/B001","candidate_links":[{"candidate_id":"cand_36aa152bde7319a39696","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:2:1","qac_word_ref":"90:16:2","surface_ar":"مِسْكِينًا"}],"gloss":"hareketin dinip durulması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Önceden hareket eden veya çalkalanan şeyin hareketi sona erer."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hareketin bitmesiyle şey durur, yerinde kalır veya dingin bir duruma geçer."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Susma ile rüzgarın, yağmurun ve öfkenin dinmesi aynı değişimin bağlama bağlı kullanımlarıdır."}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Önceki hareketin veya çalkantının sona erip ardından durma ve dinginlik oluştuğu genel çekirdeği karşılar.","boundary_detail":"Bu dal yerleşme, ev halkı, yoksulluk ya da araç adlarını değil, hareketten sonra durma ve dinginleşmeyi anlatır.","branch_image_ar":"ذهاب الحركة","concept_gloss":"hareketin dinip durulması","contextual_glosses":[{"applicability":"Rüzgar, yağmur veya öfke gibi hareketli ya da şiddetli bir durumun yatıştığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli bir hareket veya şiddet durumunun sona ererek yatışmasını korur."},"facet_ids":["F001","F002","F003"],"text":"dindi","usage_role":"contextual"},{"applicability":"Çalkantıdan sonra dengeli ve dingin duruma geçişin öne çıktığı anlatımlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çalkantının bitmesini ve ardından dengeli bir durum oluşmasını korur."},"facet_ids":["F001","F002"],"text":"duruldu","usage_role":"contextual"}],"definition":"Bir şeyin hareketi veya çalkantısı sona ererek durması, yerinde kalması ya da dinginleşmesidir. Susma ile rüzgarın, yağmurun ve öfkenin dinmesi bu değişimin belirli bağlamlardaki görünüşleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Önceden hareket eden veya çalkalanan şeyin hareketi sona erer."},{"facet_id":"F002","role":"core","statement":"Hareketin bitmesiyle şey durur, yerinde kalır veya dingin bir duruma geçer."},{"facet_id":"F003","role":"associated_use","statement":"Susma ile rüzgarın, yağmurun ve öfkenin dinmesi aynı değişimin bağlama bağlı kullanımlarıdır."}],"identity_rationale":"Kaynak sözü, önceki hareketin ya da çalkantının sona ermesini ve şeyin ardından durup dengelenmesini açıkça temel anlam olarak verir. Susma ile rüzgar, yağmur ve öfkenin dinmesi bu çekirdeğin bağlama bağlı gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"hareketin sona erip şeyin durması"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"hareketi veya çalkantısı dindi ve durdu"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"rüzgar, yağmur ya da öfke dindi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"hareketsiz, yerinde duran veya dingin"}],"lexicalization_note":"Tanım yalın durma çekirdeğini korur; rüzgar, yağmur ve öfke kullanımlarını yalnızca belirli bağlamlara bağlı uzantılar olarak ayırır.","neighbor_coverage_note":"Verilen bütün komşu kartları değerlendirildi. En keskin eşdeğerlik, yakınlık ve karşıtlık bu üçünde bulundu; öteki kartlar ayrı kök dallarına, özel araçlara veya uzak bağlamlara aittir.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Komşu karttaki su, rüzgar, gemi ve topluluk örnekleri sınırı değiştirmez; bunlar aynı durma ve dinginleşme çekirdeğinin örnekleridir.","focus_only":null,"gloss":"hareketten sonra durma ve dinginleşme","neighbor_only":null,"neighbor_ref":"root_000590/B001","relation_type":"synonym","shared_zone":"İki dal da hareket veya çalkantıdan sonra durmayı, yerinde kalmayı ve dinginleşmeyi aynı çekirdekte toplar."},{"boundary_match":"partial","distinction":"Odak dal bir durum değişimini, komşu dal ise bunun yanında yumuşak ve kaygısız oluş biçimini anlatır; bu yüzden her bağlamda birbirlerinin yerine geçmezler.","focus_only":"Odak dal, önceki hareketin veya çalkantının sona ermesini gerekli başlangıç noktası yapar.","gloss":"dingin durma ile yumuşaklık","neighbor_only":"Komşu dal yumuşaklık, kolaylık ve sertlikten uzak davranış biçimini de kapsar.","neighbor_ref":"root_000608/B001","relation_type":"near_synonym","shared_zone":"Her ikisi de çalkantısız, dingin ve zorlamasız bir durumu anlatabilir."},{"boundary_match":"opposed","distinction":"Odakta hareket sona erip denge oluşurken komşuda güçlü hareket ve dengesizlik belirginleşir; ortak eksende ters yönleri gösterirler.","focus_only":"Odak dal hareketin ve çalkantının biterek durulmasını anlatır.","gloss":"durulma ile şiddetli çalkantı","neighbor_only":"Komşu dal güçlü sarsıntı ve yoğun çalkantının sürmesini anlatır.","neighbor_ref":"root_000545/B001","relation_type":"antonym","shared_zone":"İki dal da bir şeyin hareket ve denge durumunu aynı eksende değerlendirir."}],"source_phrase_ar":"خلاف الاضطراب والحركة؛ سكن الشيء سكونا فهو ساكن؛ السكون ذهاب الحركة؛ استقر وثبت؛ هدأ بعد تحرك؛ ثبوت الشيء بعد تحرك","source_summary":"Kaynakların ortak çizgisi, hareket veya çalkantıdan sonra gelen durma, yerinde kalma ve dinginleşmedir; sessizlik ve doğa olaylarının ya da öfkenin yatışması da bu çizgide ele alınır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه السكون بعد الحركة والاستقرار والثبوت والهدوء والسكوت وسكون الريح والمطر والغضب","what_is_not_ar":"ليس السكنى ولا المسكنة ولا أسماء الآلة"},"support_links":["sup_c0ee4e992d753eb99c0b"]},{"boundary":"Burada odak, yerleşme eylemi ve yaşanan yerdir; orada yaşayan kişiler ya da iç dinginlik bu dala girmez.","branch_kind":"bare","branch_ref":"root_000726/B002","candidate_links":[{"candidate_id":"cand_16ac7270564b8253f787","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:2:1","qac_word_ref":"90:16:2","surface_ar":"مِسْكِينًا"}],"gloss":"bir yere yerleşip orada yaşama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir yere yerleşir ve orada yaşamını sürdürür."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yerleşilip yaşanan ev veya yer, bu eylemin yer adı olarak anlatılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birini bir yerde oturtma ve evi kira almadan kullanımına verme de bu alanın ettirgen ve hukuki uzantılarıdır."}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yalın eylem çekirdeğini, yani bir yeri sürekli veya yerleşik biçimde yaşanan yer edinmeyi karşılar.","boundary_detail":"Burada odak, yerleşme eylemi ve yaşanan yerdir; orada yaşayan kişiler ya da iç dinginlik bu dala girmez.","branch_image_ar":"استيطان المنزل","concept_gloss":"bir yere yerleşip orada yaşama","contextual_glosses":[{"applicability":"Eylemden çok kişinin yerleşip yaşadığı evin veya yerin kendisi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yerleşilip yaşanan yer olma niteliğini korur."},"facet_ids":["F002"],"text":"konut","usage_role":"contextual"},{"applicability":"Bir kişinin başka birini belirli bir evde veya yerde oturur duruma getirdiği ettirgen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başkasını bir yerde oturur ve yaşar duruma getirme işlemini korur."},"facet_ids":["F003"],"text":"yerleştirdi","usage_role":"contextual"}],"definition":"Bir yere yerleşip orada yaşama ve o yeri yaşanan yer edinmedir. Aynı alan, yaşanan yerin kendisini, birini oraya yerleştirmeyi ve bir evi kira almadan kullanımına vermeyi de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir yere yerleşir ve orada yaşamını sürdürür."},{"facet_id":"F002","role":"extension","statement":"Yerleşilip yaşanan ev veya yer, bu eylemin yer adı olarak anlatılır."},{"facet_id":"F003","role":"extension","statement":"Birini bir yerde oturtma ve evi kira almadan kullanımına verme de bu alanın ettirgen ve hukuki uzantılarıdır."}],"identity_rationale":"Kaynak sözü bir yerde yerleşip yaşamayı, yaşanan yeri, birini orada oturtmayı ve bir evi karşılıksız kullanıma bırakmayı birlikte bildirir. Dal çerçevesi bunları yerleşme ve konut ekseninde doğru biçimde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bir yere yerleşip orada yaşadı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"konut, ev veya yaşanan yer"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir evi kira almadan oturması için verme"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"onu bir evde veya yerde oturttu"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"konut olarak kullanılan ev veya yer"}],"lexicalization_note":"Tanım yalın yerleşip yaşama anlamını temel alır; konut, birini oturtma ve karşılıksız kullanım verme biçimlerini aynı söz ailesinin açık uzantıları olarak gösterir.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı. Seçilen üç komşu yerleşme, barınak ve sabit konum sınırlarını doğrudan aydınlatır; kalanlar dönemlik kalış, çadır, eşya veya uzak kök dallarıyla sınırlıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yaşama yerini yerleşme eylemiyle birlikte kurar; komşu dalın çekirdeği ise gecelemeye veya barınmaya yarayan yerin kendisidir.","focus_only":"Odak dal yerleşip yaşama eylemini, birini yerleştirmeyi ve karşılıksız kullanım vermeyi de içerir.","gloss":"yerleşip yaşama ile barınak","neighbor_only":"Komşu dal geceleme ve sığınma yerlerini, çadırı ve saray gibi farklı barınak adlarını da kapsar.","neighbor_ref":"root_000166/B001","relation_type":"near_synonym","shared_zone":"İki dal da insanın yaşadığı evi veya barındığı yeri gösterebilir."},{"boundary_match":"partial","distinction":"Odakta yerleşip yaşama ve konutlaşma belirgindir; komşuda yer seçme ve hazırlama işlemi ile hayvan barınağına uzanan daha geniş bir alan vardır.","focus_only":"Odak dal yerleşik yaşamı, konutu ve bir başkasını orada oturtmayı kapsar.","gloss":"yerleşme ile konak yeri edinme","neighbor_only":"Komşu dal insan veya hayvan için konak yeri seçme, hazırlama ve elverişli ya da elverişsiz çevre niteliğini kapsar.","neighbor_ref":"root_000162/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir yeri kalınacak veya yaşanacak yer olarak edinme vardır."},{"boundary_match":"partial","distinction":"Odak gündelik yerleşme ve konut alanıdır; komşu ise belirli kalıplara, özel bir yer adına ve başın boyundaki oturma noktasına bağlıdır.","focus_only":"Odak dal genel yerleşme eylemini ve yaşanan yeri anlatır.","gloss":"konut ile sabit konum","neighbor_only":"Komşu dal kalıplaşmış çoğul kullanımlarda konumları, düzeyleri veya alışılmış düzeni ve ayrıca bedensel bir yerleşme noktasını anlatır.","neighbor_ref":"root_000726/B009","relation_type":"near_neighbor","shared_zone":"İki dal da bir varlığın bulunduğu veya yerleştiği yeri gösterebilir."}],"source_phrase_ar":"يسكنون الدار؛ المنزل وهو المسكن؛ سكون البيت؛ سكنت داري وأسكنتها غيرى؛ سكنى المرأة المسكن؛ يستعمل في الاستيطان واسم المكان مسكن والجمع مساكن","source_summary":"Kaynaklar yerleşip yaşama eylemini, yaşanan ev veya yeri, bir başkasını oraya yerleştirmeyi ve bir evi kira karşılığı olmadan kullanımına bırakmayı aynı anlam alanında birleştirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه سكن المكان والمسكن والمنزل والبيت والمساكن والسكنى والإسكان وإعارة المنزل بلا كراء","what_is_not_ar":"ليس أهل الدار أنفسهم ولا السكينة القلبية"},"support_links":["sup_6c7bebbe0510e7ee6c6a"]},{"boundary":"Dal, evin kendisini değil evde yaşayanları ve ev halkını anlatır; genel akrabalık veya her tür topluluk bağı daha geniştir.","branch_kind":"mixed_non_bare","branch_ref":"root_000726/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:2:1","qac_word_ref":"90:16:2","surface_ar":"مِسْكِينًا"}],"gloss":"ev halkı ve orada yaşayanlar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderim, evin kendisine değil o evde yaşayan kişilere yönelir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı evin halkı ve bakmakla yükümlü olunan aile üyeleri bu grubun belirgin özel alanıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çoğul kullanım, bir evde veya başka bir yerde oturanların tümüne genişleyebilir."}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Evde yaşayan topluluğu hem aile halkı hem de daha genel oturanlar yönüyle karşılar.","boundary_detail":"Dal, evin kendisini değil evde yaşayanları ve ev halkını anlatır; genel akrabalık veya her tür topluluk bağı daha geniştir.","branch_image_ar":"أهل الدار","concept_gloss":"ev halkı ve orada yaşayanlar","contextual_glosses":[{"applicability":"Aynı evde yaşayan aile ve bakmakla yükümlü olunan kişiler özellikle kastedildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aynı evde yaşayan aile topluluğunu ve yakın ev bağını korur."},"facet_ids":["F001","F002"],"text":"ev halkı","usage_role":"contextual"},{"applicability":"Aile bağı aranmadan belirli bir evde veya yerde oturanların tümü kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli yerde oturan kişiler topluluğunu aile bağı eklemeden korur."},"facet_ids":["F001","F003"],"text":"orada yaşayanlar","usage_role":"contextual"}],"definition":"Bir evde yaşayan kişiler, özellikle aynı evin halkı ve aile yükümlülüğü içinde bulunan kimselerdir. Daha genel çoğul kullanım, belirli bir yerde oturanların tümünü gösterebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderim, evin kendisine değil o evde yaşayan kişilere yönelir."},{"facet_id":"F002","role":"specialization","statement":"Aynı evin halkı ve bakmakla yükümlü olunan aile üyeleri bu grubun belirgin özel alanıdır."},{"facet_id":"F003","role":"extension","statement":"Çoğul kullanım, bir evde veya başka bir yerde oturanların tümüne genişleyebilir."}],"identity_rationale":"Kaynak sözü evde yaşayanları, ev halkını ve bakmakla yükümlü olunan aile üyelerini açıkça dalın gönderimi yapar. Çerçeve, evi ya da yerleşme eylemini değil o yerde yaşayan insan topluluğunu doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ev halkı ve aile üyeleri"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"bir yerde yaşayanlar"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"evde yaşayanlar; özel anlatıda evde bulunduğu düşünülen görünmez varlıklar"}],"lexicalization_note":"Tanım ev halkını yalın çekirdek olarak verir; çoğul sakinler ve evde yaşayanları belirten kalıp kullanımı bu çekirdeğin ayrı gerçekleşmeleridir.","neighbor_coverage_note":"Tüm komşular değerlendirildi. Seçilenler ev halkı, daha geniş bağlı topluluk ve fiziksel konut arasındaki temel karışmaları gösterir; diğer adaylar tek kişi, eşlik veya uzak yan dallardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta belirleyici bağ fiilen evde yaşamaktır; komşuda aileye veya eve bağlanma, gerçek oturma bulunmadan da gönderimi kurabilir.","focus_only":"Odak dal evde oturanların tümüne uzanabilir ve aile bağını her kullanımda zorunlu tutmaz.","gloss":"ev halkı ve aile çevresi","neighbor_only":"Komşu dal aileye bağlanan kişileri ve kadın ya da topluluk için aktarmalı ev kullanımını da içerir.","neighbor_ref":"root_000166/B002","relation_type":"near_synonym","shared_zone":"İki dal da aynı eve bağlı aile halkını ve birlikte yaşayan kişileri gösterebilir."},{"boundary_match":"partial","distinction":"Odak için ortak yaşama yeri merkezdir; komşuda ortak ev yalnızca üyeliği kurabilen bağlardan biridir ve kapsam çok daha geniştir.","focus_only":"Odak dal belirli evde yaşayan kişilerle sınırlı bir topluluk kurar.","gloss":"ev halkı ile bağlı topluluk","neighbor_only":"Komşu dal eş, yakınlar, soy, din, iş ve ülke gibi çok farklı üyelik bağlarını da kapsar.","neighbor_ref":"root_000064/B001","relation_type":"near_synonym","shared_zone":"Her iki dal aynı evde yaşayan yakın kişiler topluluğunu anlatabilir."},{"boundary_match":"field_only","distinction":"Biri yaşayan kişilere, diğeri yaşama eylemine ve fiziksel yere yönelir; gönderimleri farklı olduğu için birbirlerinin yerine kullanılamaz.","focus_only":"Odak dal evde yaşayan insan topluluğunu gösterir.","gloss":"ev halkı ile konut","neighbor_only":"Komşu dal yerleşme eylemini, yaşanan evi ve birini oraya yerleştirmeyi gösterir.","neighbor_ref":"root_000726/B002","relation_type":"same_field","shared_zone":"İki dal aynı ev ve orada yaşama durumunun katılımcılarını paylaşır."}],"source_phrase_ar":"السكن الأهل الذين يسكنون الدار؛ السكن السكان؛ السكن جزم العيال وهم أهل البيت؛ السكن أهل الدار؛ سكان الدار","source_summary":"Kaynakların ortak anlatımı, sözü ev halkı, aile üyeleri ve evde ya da belirli bir yerde oturan kişiler için kullanır; fiziksel ev ile içindeki topluluk açıkça ayrılır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه السكن بمعنى أهل الدار والعيال وسكان الدار ومن يقيمون فيها","what_is_not_ar":"ليس نفس المنزل ولا مجرد فعل السكنى"},"support_links":[]},{"boundary":"Odak iç dinginliği sağlayan kişi veya şeydir; yalnız fiziksel durma, ağırbaşlı iç durum ya da salt sıcaklık değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000726/B004","candidate_links":[{"candidate_id":"cand_16ac7270564b8253f787","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:2:1","qac_word_ref":"90:16:2","surface_ar":"مِسْكِينًا"}],"gloss":"insanı rahatlatıp içini yatıştıran dayanak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi sevdiği veya yakın bulduğu birine ya da şeye yönelir ve onun yanında içi yatışır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gece ve destekleyici yakarış, dinlenme veya güven verme işlevleriyle aynı adlandırma alanına girer."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yanında oturulup yakınlık ve rahatlık bulunan ateş bu anlamın somut bir gerçekleşmesidir."}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi, zaman, sözlü destek veya ateşin insana yakınlık ve iç rahatlığı vermesi ortak çekirdeğini karşılar.","boundary_detail":"Odak iç dinginliği sağlayan kişi veya şeydir; yalnız fiziksel durma, ağırbaşlı iç durum ya da salt sıcaklık değildir.","branch_image_ar":"مأنس السكون","concept_gloss":"insanı rahatlatıp içini yatıştıran dayanak","contextual_glosses":[{"applicability":"Sevilen kişi ya da destekleyici söz gibi bir dayanağın ruhsal rahatlık sağladığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin bir dayanağa yönelmesini ve onunla iç rahatlığı bulmasını korur."},"facet_ids":["F001","F002"],"text":"içini rahatlatan","usage_role":"contextual"},{"applicability":"Ateşin yalnız ısısı değil, yanında bulunmanın verdiği yakınlık ve rahatlık özellikle anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ateşin somut varlığını ve yanında rahatlama işlevini birlikte korur."},"facet_ids":["F001","F003"],"text":"yanında iç ısıtan ateş","usage_role":"explanatory"}],"definition":"Kişinin yakınlık duyup yanında rahatladığı, içinin yatıştığı kişi veya şeydir. Gece, destekleyici yakarış ve yanında oturulan ateş bu rahatlatıcı işlevle adlandırılabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi sevdiği veya yakın bulduğu birine ya da şeye yönelir ve onun yanında içi yatışır."},{"facet_id":"F002","role":"extension","statement":"Gece ve destekleyici yakarış, dinlenme veya güven verme işlevleriyle aynı adlandırma alanına girer."},{"facet_id":"F003","role":"specialization","statement":"Yanında oturulup yakınlık ve rahatlık bulunan ateş bu anlamın somut bir gerçekleşmesidir."}],"identity_rationale":"Kaynak sözü kişinin içinin yöneldiği ve yanında dinginleştiği sevgiliyi ya da şeyi temel alır; gece, yakarış ve ateş bunun örnekleridir. Dal çerçevesi bu rahatlatıcı ve yakınlık veren dayanağı doğru yakalar.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"insanın yanında rahatlayıp içinin yatıştığı kişi veya şey"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yanında oturulup rahatlık bulunan ateş"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"senin yakarışların onları rahatlatır"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"geceyi dinlenme ve dinginleşme zamanı yaptı"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"eğri sırığı ateş ve yağla doğrultma"}],"lexicalization_note":"Tanım yalın olarak kişinin yanında rahatlayıp dinginleştiği dayanağı verir; gece, yakarış ve ateş kullanımları ile ateşle düzeltme ayrı bağlamlara bağlı tutulur.","neighbor_coverage_note":"Bütün aday kartlar incelendi. Seçilenler yakınlık, alışma ve sıcaklıkla en olası karışmaları açıklar; diğer adaylar selamlama, üzüntü, unutma veya özel ve uzak kullanımlardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta kişinin yöneldiği rahatlatıcı dayanak öne çıkar; komşuda yakınlık kurma ve yabancılık duygusunu giderme süreci daha geniştir.","focus_only":"Odak dal rahatlık veren kişi veya şeyi adlandırır ve gece ile ateş gibi insan olmayan dayanaklara uzanır.","gloss":"rahatlatan dayanak ile yakınlık","neighbor_only":"Komşu dal yakınlaşma, konuşma, sevinç ve ürkütücü olmayan hayvan niteliğini de kapsar.","neighbor_ref":"root_000059/B003","relation_type":"near_synonym","shared_zone":"İki dal da yalnızlık veya tedirginliğin yakınlık sayesinde azalmasını anlatabilir."},{"boundary_match":"partial","distinction":"Odakta sonuç olarak iç yatışması belirleyicidir; komşuda tekrar ve yakınlıkla oluşan alışma bağı belirleyicidir.","focus_only":"Odak dal kişinin yanında içinin yatıştığı dayanağı ve onun rahatlatıcı işlevini anlatır.","gloss":"iç rahatlığı ile alışkanlık","neighbor_only":"Komşu dal bir kişi, şey veya yere alışma, onu sürekli yanında tutma ve başkasını alıştırma eylemlerini kapsar.","neighbor_ref":"root_000045/B005","relation_type":"near_synonym","shared_zone":"Yakın bulunup sürekli yönelinen kişi veya yer iki dalda da rahatlık verebilir."},{"boundary_match":"field_only","distinction":"Odakta ateşin yanında bulunmanın rahatlatıcı ve yakınlık veren yönü, komşuda ise ölçülebilir sıcaklık ve ısıtma işlevi çekirdektir.","focus_only":"Odak dal ateşi insana yakınlık ve iç rahatlığı veren bir dayanak olarak ele alır.","gloss":"ateşle rahatlama ve sıcaklık","neighbor_only":"Komşu dal sıcaklığı ve sıcak tutan giysi, ev ya da duvarı doğrudan ısı bakımından ele alır.","neighbor_ref":"root_000479/B001","relation_type":"same_field","shared_zone":"Ateş ve ısınma deneyimi iki dalın somut kullanım alanında buluşur."}],"source_phrase_ar":"كل ما سكنت إليه من محبوب؛ السكن أيضا كل ما سكنت إليه؛ ما سكنت إليه؛ إن صلواتك سكن لهم؛ جعل الليل سكنا؛ السكن النار التي يسكن بها","source_summary":"Kaynaklar kişinin sevdiği veya yakın bulduğu şeyin yanında içinin yatışmasını ortak çekirdek yapar; geceyi, destekleyici yakarışı ve ateşi bu rahatlatıcı işlevin örnekleri olarak verir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه كل ما تسكن إليه النفس من محبوب أو بيت أو ليل أو صلاة أو نار سميت بذلك للأنس والسكون إليها","what_is_not_ar":"ليس الوقار الخاص باسم السكينة ولا فقر المسكين"},"support_links":["sup_6c7bebbe0510e7ee6c6a"]},{"boundary":"Bu dal dış hareketin yalnızca durmasını değil, güvenle birleşen ağırbaşlı ve dingin iç durumu anlatır; yoksulluk ve ezilmişlik ayrı kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000726/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:2:1","qac_word_ref":"90:16:2","surface_ar":"مِسْكِينًا"}],"gloss":"güven veren ağırbaşlı iç dinginlik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İç dünyada güven, dinginlik ve ağırbaşlılık birlikte belirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kalbin korkudan kurtulup güven duyması bu iç durumun belirgin gerçekleşmesidir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir sandığın içindeki güven verici şey, insanların kalplerini yatıştırıp onları bir arada tutması bakımından adlandırılır."}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Güven, kalp yatışması, yumuşak başlılık ve ağırbaşlılığın birlikte bulunduğu tam çekirdeği karşılar.","boundary_detail":"Bu dal dış hareketin yalnızca durmasını değil, güvenle birleşen ağırbaşlı ve dingin iç durumu anlatır; yoksulluk ve ezilmişlik ayrı kalır.","branch_image_ar":"طمأنينة الوقار","concept_gloss":"güven veren ağırbaşlı iç dinginlik","contextual_glosses":[{"applicability":"Korku veya tedirginlik içindeki kişinin kalben güvenli ve dingin duruma getirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kalpteki korkunun yerini güven ve dinginliğin almasını korur."},"facet_ids":["F001","F002"],"text":"kalbine güven ve dinginlik verdi","usage_role":"contextual"},{"applicability":"Sandıktaki şeyin topluluğa güven verip dağılmasını önleyen işlevi açıklandığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Somut bir dayanağın kalpleri yatıştırıp güven oluşturma işlevini korur."},"facet_ids":["F003"],"text":"kalpleri yatıştıran güvence","usage_role":"explanatory"}],"definition":"Korku ve taşkınlığın yerini güvenin, ağırbaşlılığın ve yumuşak bir iç dinginliğinin almasıdır. Kalbe verilen güven ile topluluğu bir arada tutan sandık içeriği bu durumun özel anlatımlarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İç dünyada güven, dinginlik ve ağırbaşlılık birlikte belirir."},{"facet_id":"F002","role":"specialization","statement":"Kalbin korkudan kurtulup güven duyması bu iç durumun belirgin gerçekleşmesidir."},{"facet_id":"F003","role":"associated_use","statement":"Bir sandığın içindeki güven verici şey, insanların kalplerini yatıştırıp onları bir arada tutması bakımından adlandırılır."}],"identity_rationale":"Kaynak sözü ağırbaşlılık, yumuşak başlılık, güven ve kalbin yatışmasını aynı iç durum çevresinde birleştirir. Sandık içindeki şeyin insanlara güven verip kaçmalarını önlemesi bu çekirdeğin özel anlatısıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ağırbaşlılık, yumuşak başlılık, güven ve kalp dinginliği"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"sandıktaki, kalpleri yatıştırıp güven veren şey"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"inananların kalplerine güven ve dinginlik verdi"}],"lexicalization_note":"Tanım ağırbaşlı iç dinginliği yalın çekirdek yapar; kalbe verilmesi ve sandıktaki güven verici şey yalnız kendi kalıpları içinde tutulur.","neighbor_coverage_note":"Verilen bütün komşular gözden geçirildi. Dış durma, rahatlatıcı dayanak ve ezilmişlik ile olan üç sınır en yararlı karşılaştırmaları verir; dış adaylar bu anlamla yeterli ortak çekirdek taşımaz.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak insanın iç dünyasında güven ve ağırbaşlılık içerir; komşu için iç dünya ve güven gerekli değildir, hareketin sona ermesi yeterlidir.","focus_only":"Odak dal güven, ağırbaşlılık ve kalp yatışmasını bir iç nitelik olarak birleştirir.","gloss":"iç güven ile hareketin dinmesi","neighbor_only":"Komşu dal herhangi bir şeyin hareket veya çalkantıdan sonra fiziksel ya da genel olarak durmasını anlatır.","neighbor_ref":"root_000726/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da çalkantının azalması ve dingin bir son durum bulunabilir."},{"boundary_match":"partial","distinction":"Odak oluşan iç durumdur; komşu ise çoğunlukla bu durumu doğuran veya yanında bulunan dayanağa yönelir.","focus_only":"Odak dal kişinin içinde oluşan güvenli, ağırbaşlı ve dingin durumu anlatır.","gloss":"iç dinginlik ile rahatlatan dayanak","neighbor_only":"Komşu dal kişiyi rahatlatan ve kendisine yönelinen kişi, zaman, söz veya ateşi adlandırır.","neighbor_ref":"root_000726/B004","relation_type":"near_synonym","shared_zone":"Bir dayanak kişide güven ve iç yatışması oluşturduğunda iki alan örtüşür."},{"boundary_match":"field_only","distinction":"Odakta güven ve dengeli ağırbaşlılık vardır; komşuda yoksunluk, güçsüzlük ya da baskı altında boyun eğme vardır, bu nedenle değer ve neden bakımından ayrılırlar.","focus_only":"Odak dal güvenli, ağırbaşlı ve dengeli bir iç durumu bildirir.","gloss":"ağırbaşlı dinginlik ile ezilmişlik","neighbor_only":"Komşu dal yoksulluk, güçsüzlük, ezilmişlik ve boyun eğme durumlarını bildirir.","neighbor_ref":"root_000726/B006","relation_type":"same_field","shared_zone":"İki dal da dış taşkınlığın bulunmadığı, alçak sesli veya çekingen bir görünüşle ilişkilendirilebilir."}],"source_phrase_ar":"السكينة وهو الوقار؛ السكينة الوداعة والوقار؛ لا يفرون عنه أبدا وتطمئن قلوبهم إليه؛ فيه ما تسكنون به؛ عليك الوقار والوداعة والأمن؛ أنزل السكينة في قلوب المؤمنين","source_summary":"Kaynaklar ağırbaşlılık, yumuşak başlılık, güven ve kalp dinginliğini ortak bir iç durum olarak sunar; kalbe güven verilmesi ve sandıktaki güven verici şey bunun özel anlatılarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه السكينة بمعنى الوقار والوداعة والأمن وطمأنينة القلب وما في التابوت الذي تسكن به القلوب","what_is_not_ar":"ليس مطلق السكون الحسي ولا المسكنة"},"support_links":[]},{"boundary":"Dal hem yoksulluğu hem ezilmiş ve güçsüz durumu kapsar; ağırbaşlı iç dinginlik ya da evde yaşama anlamları buna dahil değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000726/B006","candidate_links":[{"candidate_id":"cand_be651fe27538963c049a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:2:1","qac_word_ref":"90:16:2","surface_ar":"مِسْكِينًا"}],"gloss":"yoksulluk, güçsüzlük ve ezilmişlik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi geçim araçlarından yoksun ve yardıma gerek duyan durumda olabilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Söz, maddi yoksunluktan bağımsız olarak güçsüzlük, ezilmişlik ve aşağı durumda bulunmayı da anlatabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişinin boyun eğmesi, kendini aşağı koyması veya yoksul duruma gelmesi türemiş eylemlerle ifade edilir."}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Maddi yoksunluk ile aşağı ve güçsüz durumda bulunma yönlerini birlikte taşıyan dalın tam alanını karşılar.","boundary_detail":"Dal hem yoksulluğu hem ezilmiş ve güçsüz durumu kapsar; ağırbaşlı iç dinginlik ya da evde yaşama anlamları buna dahil değildir.","branch_image_ar":"ذل المسكنة","concept_gloss":"yoksulluk, güçsüzlük ve ezilmişlik","contextual_glosses":[{"applicability":"Bir kişinin geçim araçlarından yoksun oluşu ile zayıf toplumsal durumunun birlikte kastedildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin hem maddi yoksunluğunu hem güçsüz durumunu korur."},"facet_ids":["F001","F002"],"text":"yoksul ve güçsüz kişi","usage_role":"contextual"},{"applicability":"Kişinin baskı veya bağlılık karşısında kendini güçsüz ve aşağı konuma koyduğu eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Boyun eğme ile kendini aşağı konuma koyma eylemini birlikte korur."},"facet_ids":["F002","F003"],"text":"boyun eğip kendini alçalttı","usage_role":"contextual"}],"definition":"Geçim araçlarından yoksun olma veya güçsüz, ezilmiş ve aşağı durumda bulunmadır. Bu durumdan hareketle kişinin boyun eğmesi ya da kendini aşağı koyması da aynı söz ailesinde anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi geçim araçlarından yoksun ve yardıma gerek duyan durumda olabilir."},{"facet_id":"F002","role":"extension","statement":"Söz, maddi yoksunluktan bağımsız olarak güçsüzlük, ezilmişlik ve aşağı durumda bulunmayı da anlatabilir."},{"facet_id":"F003","role":"associated_use","statement":"Kişinin boyun eğmesi, kendini aşağı koyması veya yoksul duruma gelmesi türemiş eylemlerle ifade edilir."}],"identity_rationale":"Kaynak sözü yoksulluk halini, güçsüzlük ve ezilmişliği, ayrıca kişinin boyun eğip kendini aşağı koymasını aynı dalda açıkça sayar. Dal çerçevesi maddi yoksunluk ile toplumsal veya iradi boyun eğme arasındaki bağı korur.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"yoksul ya da ezilmiş ve güçsüz kişi"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yoksulluk veya ezilmişlik durumu"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yoksul duruma geldi ya da boyun eğip kendini alçalttı"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"boyun eğdi ve alçaldı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"Tanrı onu yoksul duruma düşürdü"}],"lexicalization_note":"Tanım yalın tek anlam varsaymaz; yoksul kişi ve yoksulluk durumunu, ezilmişlik ile boyun eğme bildiren türemiş eylemlerden açıkça ayırır.","neighbor_coverage_note":"Bütün komşu adaylar değerlendirildi. Seçilenler yoksulluk, aşağılanma ve ağır sürekli yoksulluk sınırlarını gösterir; diğerleri hor görülme, mal kaybı veya yalnız yoksullaşma sonucuna odaklanır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak yoksulluktan toplumsal ezilmişliğe ve boyun eğmeye genişler; komşunun sınırı yoksulluk ile ona bağlı toprak görüntüsünde kalır.","focus_only":"Odak dal yoksulluğun yanında güçsüzlük, ezilmişlik ve boyun eğme eylemlerini de kapsar.","gloss":"yoksulluk ve ezilmişlik","neighbor_only":"Komşu dal yoksulluğu toprağa yapışma görüntüsü ve belirli bir kalıp sözle anlatır.","neighbor_ref":"root_000178/B002","relation_type":"near_synonym","shared_zone":"İki dal da maddi yoksunluğu, gereksinimi ve yardıma muhtaç durumu anlatır."},{"boundary_match":"partial","distinction":"Odakta yoksulluk bu alanın temel parçasıdır; komşuda maddi yoksunluk gerekmez, aşağılanma ve düşük konuma razı olma belirleyicidir.","focus_only":"Odak dal maddi yoksulluğu ve yoksul kişiyi de doğrudan kapsar.","gloss":"ezilmişlik ile aşağılanma","neighbor_only":"Komşu dal baskıyla gelen aşağılanmayı, düşük konumu ve buna razı olmayı özellikle öne çıkarır.","neighbor_ref":"root_000865/B002","relation_type":"near_synonym","shared_zone":"İki dal da kişinin aşağı, güçsüz ve baskı altında bir durumda bulunmasını gösterebilir."},{"boundary_match":"partial","distinction":"Odak daha geniş nitelikler ve eylemler taşır; komşu ise yoksulluğun ağır ve süreğen derecesiyle daha dardır.","focus_only":"Odak dal yoksulluğun yanında güçsüzlük, ezilmişlik ve boyun eğmeyi içerir.","gloss":"genel yoksulluk ile sürekli ağır yoksulluk","neighbor_only":"Komşu dal yalnız eksiksiz ve sürekli yoksulluk derecesini bildirir.","neighbor_ref":"root_000132/B003","relation_type":"near_synonym","shared_zone":"Her iki dal geçim araçlarından yoksun olma durumunu anlatır."}],"source_phrase_ar":"المسكنة مصدر فعل المسكين؛ المسكين الفقير وقد يكون بمعنى الذلة والضعف؛ تمسكن إذا خضع لله وهي المسكنة للذلة؛ استكان أي خضع وذل","source_summary":"Kaynakların ortak çerçevesi yoksul kişiyi ve yoksulluk durumunu güçsüzlük, ezilmişlik ve boyun eğmeyle ilişkilendirir; türemiş eylemler kişinin yoksullaşmasını veya kendini aşağı koymasını anlatır.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه المسكين والمسكنة والفقر والذلة والضعف والخضوع والاستكانة والتمسكن","what_is_not_ar":"ليس السكينة بمعنى الوقار ولا السكنى في الدار"},"support_links":["sup_5f93873b9ef4550e8a28"]},{"boundary":"Dal kesici bıçak ile onu yapan kişiyi kapsar; gemi dengeleme parçası ya da kesme eyleminin kendisi değildir.","branch_kind":"bare","branch_ref":"root_000726/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:2:1","qac_word_ref":"90:16:2","surface_ar":"مِسْكِينًا"}],"gloss":"kesici bıçak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderim, kesmekte kullanılan ağızlı bıçaktır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adın kökeni, bıçağın kesilen hayvanın hareketini ölümle sona erdirmesine bağlanır."}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın araç gönderimini kısa ve doğal biçimde karşılar; adın köken açıklaması tanımda ayrıca korunur.","boundary_detail":"Dal kesici bıçak ile onu yapan kişiyi kapsar; gemi dengeleme parçası ya da kesme eyleminin kendisi değildir.","branch_image_ar":"إسكان الذبيحة بالسكين","concept_gloss":"kesici bıçak","contextual_glosses":[{"applicability":"Bıçağın kesilen hayvanın hareketini sona erdirme işlevi özellikle öne çıkarıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kesici aracı ve hayvan kesme bağlamındaki işlevini birlikte korur."},"facet_ids":["F001","F002"],"text":"hayvan kesme bıçağı","usage_role":"contextual"}],"definition":"Kesmekte kullanılan ağızlı bıçaktır. Kaynaklar adını, kesilen hayvanın hareketini ölümle sona erdirmesi üzerinden açıklar; aracı yapan kişi de ayrı bir türemiş adla gösterilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderim, kesmekte kullanılan ağızlı bıçaktır."},{"facet_id":"F002","role":"associated_use","statement":"Adın kökeni, bıçağın kesilen hayvanın hareketini ölümle sona erdirmesine bağlanır."}],"identity_rationale":"Kaynak sözü kesici bıçağı doğrudan adlandırır ve adlandırmayı kesilen hayvanın hareketini ölümle sona erdirmesine bağlar. Dal çerçevesi aracı ve verilen köken açıklamasını koruyarak gemi parçasından ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"kesici bıçak"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"bıçak yapan kimse"}],"lexicalization_note":"Tanım bıçak adını yalın araç anlamıyla verir; hayvanın hareketini sona erdirmeye dayalı ad açıklamasını çekirdeğin yerine geçirmeyen bağlı bir açıklama olarak tutar.","neighbor_coverage_note":"Tüm komşu kartları incelendi. Seçilenler araç, keskin kenar ve kesme işlemi ayrımını en açık biçimde kurar; kalanlar kılıç türleri, hayvan öldürme yolları veya uzak kök dallarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak belirli bıçak türünün genel adıdır; komşu farklı kesici araçları ve keskin ağız biçimlerini daha geniş bir kümede toplar.","focus_only":"Odak dal belirli bir bıçak adını ve hayvanın hareketini sona erdirmeye bağlanan ad açıklamasını içerir.","gloss":"bıçak ile kesici araç","neighbor_only":"Komşu dal kesme araçlarını, kılıcı, kısa geniş ağzı ve kesik oku kapsayan daha geniş bir araç ve ağız alanıdır.","neighbor_ref":"root_001240/B014","relation_type":"near_synonym","shared_zone":"Her iki dal keskin ağızla kesme işlevi gören elde kullanılan araçları kapsayabilir."},{"boundary_match":"field_only","distinction":"Odak araç bütünüdür, komşu ise aracın kesen kenarı veya ucudur; parça ile bütün aynı gönderime sahip değildir.","focus_only":"Odak dal bütün kesici bıçağın kendisini gösterir.","gloss":"bıçak ile keskin ağız","neighbor_only":"Komşu dal kılıç veya bıçağın keskin kenarını ve herhangi bir şeyin kesici ucunu gösterir.","neighbor_ref":"root_001078/B012","relation_type":"same_field","shared_zone":"Bıçak, kesme işini komşu dalın gösterdiği keskin kenar sayesinde yapar."},{"boundary_match":"thematic_only","distinction":"Odak olayda kullanılan nesnedir; komşu bu nesneyle yapılabilecek belirli bedensel işlemdir ve anlam çekirdekleri örtüşmez.","focus_only":"Odak dal kesme aracını adlandırır.","gloss":"kesme aracı ile boyun kesme işlemi","neighbor_only":"Komşu dal hayvanın boyun kemiğini kesme işlemini adlandırır.","neighbor_ref":"root_000088/B004","relation_type":"thematic","shared_zone":"İki dal hayvan kesme olayında araç ve işlem olarak birlikte yer alabilir."}],"source_phrase_ar":"السكين معروف؛ السكين المدية؛ السكين معروف يذكر ويؤنث؛ سمي سكينا لأنها تسكن الذبيحة؛ السكين سمي لإزالته حركة المذبوح","source_summary":"Kaynaklar kesici bıçağın bilinen araç olduğunu ortaklaşa belirtir ve adlandırılmasını, kesilen hayvanın hareketini sona erdirme sonucuyla açıklar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه السكين والمدية وتسميتها لأنها تسكن اضطراب المذبوح بالموت","what_is_not_ar":"ليس سكان السفينة ولا السكين بمعنى الحمار"},"support_links":[]},{"boundary":"Bu dal yalnız geminin kıçındaki dengeleyici ve yöneltici bölüm ya da araçla ilgilidir; geminin tamamını veya genel durma eylemini adlandırmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000726/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:2:1","qac_word_ref":"90:16:2","surface_ar":"مِسْكِينًا"}],"gloss":"geminin kıçındaki dengeleyici yöneltme aracı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderim geminin kıçında bulunan belirli bir bölüm veya araçtır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu bölüm veya araç gemiyi dengeler, yöneltir ve çalkantısını azaltır."}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Parçanın gemideki yerini ve gemiyi dengeleyip yöneltme işlevini birlikte karşılar.","boundary_detail":"Bu dal yalnız geminin kıçındaki dengeleyici ve yöneltici bölüm ya da araçla ilgilidir; geminin tamamını veya genel durma eylemini adlandırmaz.","branch_image_ar":"تسكين السفينة بالسكان","concept_gloss":"geminin kıçındaki dengeleyici yöneltme aracı","contextual_glosses":[{"applicability":"Tarihsel gemi bölümünün modern tek bir parça adıyla kesin eşleştirilmesi gerekmediğinde açıklayıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geminin kıçındaki yerini ve denge sağlama işlevini kesin olmayan tür eşleştirmesi yapmadan korur."},"facet_ids":["F001","F002"],"text":"gemiyi dengede tutan kıç parçası","usage_role":"explanatory"}],"definition":"Geminin kıçında bulunan, gemiyi dengede tutmaya, yöneltmeye ve çalkantısını azaltmaya yarayan bölüm veya araçtır. Adlandırma doğrudan bu dengeleme işlevine bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderim geminin kıçında bulunan belirli bir bölüm veya araçtır."},{"facet_id":"F002","role":"core","statement":"Bu bölüm veya araç gemiyi dengeler, yöneltir ve çalkantısını azaltır."}],"identity_rationale":"Kaynak sözü geminin kıçındaki, onu dengede tutup çalkantısını azaltan bölüm veya aracı açıkça verir. Dal çerçevesi bu gemiye özgü gönderimi ve dengeleme işlevini kesici bıçak anlamından doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"geminin kıçındaki, onu dengede tutup yönelten bölüm veya araç"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"gemiyi dengede tutup çalkantısını azaltan kıç parçası"}],"lexicalization_note":"Tanım gemi parçasının özel adını yalın biçimde korur; gemiyle kurulan kalıp ifade aynı parçayı işleviyle belirleyen kullanımdır ve genel durma anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Seçilen üç kart gemi donanımı, itme eylemi ve durma sonucu arasındaki sınırı gösterir; diğerleri gemi türleri, geminin bütünü veya uzak kök dallarıdır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odaktaki parça kıçta denge ve yön sağlar; komşudaki sırık dışarıdan su tabanına dayanarak gemiyi ileri iter.","focus_only":"Odak dal geminin kıçındaki sürekli dengeleme ve yöneltme bölümünü veya aracını gösterir.","gloss":"kıç dengeleyicisi ile itme sırığı","neighbor_only":"Komşu dal gemiyi itmek için suya dayanan uzun sırığı gösterir.","neighbor_ref":"root_000767/B006","relation_type":"same_field","shared_zone":"İki dal da geminin hareketini denetlemekte kullanılan donanımı adlandırır."},{"boundary_match":"thematic_only","distinction":"Odak bir gemi parçasıdır; komşu ise ayrı bir araçla yapılan itme hareketidir, bu nedenle yalnız aynı olay alanını paylaşırlar.","focus_only":"Odak dal gemiyi dengeleyen ve yönelten parçayı adlandırır.","gloss":"dengeleyici parça ile sırıkla itme","neighbor_only":"Komşu dal gemicinin bir sırıkla gemiyi itme eylemini adlandırır.","neighbor_ref":"root_001413/B006","relation_type":"thematic","shared_zone":"Her ikisi de geminin hareketinin insan eliyle denetlenmesi olayında yer alır."},{"boundary_match":"partial","distinction":"Odak bu sonucu sağlayan belirli araçtır; komşu ise aracın türünden bağımsız olarak ortaya çıkan durma veya az hareket durumudur.","focus_only":"Odak dal geminin çalkantısını azaltan belirli kıç bölümünü veya aracını gösterir.","gloss":"gemiyi dengeleme ile geminin durması","neighbor_only":"Komşu dal herhangi bir şeyin durmasını veya az hareket etmesini ve geminin denizde beklemesini anlatır.","neighbor_ref":"root_000114/B003","relation_type":"near_neighbor","shared_zone":"Geminin hareketinin azalması iki dalın gemi bağlamında buluştuğu sonuçtur."}],"source_phrase_ar":"سكان السفينة سمى لأنه يسكنها عن الاضطراب؛ السكان ذنب السفينة الذي به تعدل؛ السكان أيضا ذنب السفينة؛ السكان وهو الكوثل؛ سكان السفينة ما يسكن به","source_summary":"Kaynaklar geminin kıçındaki bu bölüm veya aracı ortaklaşa tanımlar; temel işlevi gemiyi ayarlamak, dengede tutmak ve çalkantısını azaltmaktır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه سكان السفينة وذنبها أو كوثلها الذي تعدل به وتسكن عن الاضطراب","what_is_not_ar":"ليس السكين المدية ولا السكن أهل الدار"},"support_links":[]},{"boundary":"Bu dal genel olarak evde yaşama anlamına genişletilemez; bedensel yerleşme noktası, kalıplaşmış konum anlatıları ve özel yer adıyla sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000726/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:2:1","qac_word_ref":"90:16:2","surface_ar":"مِسْكِينًا"}],"gloss":"sabit yer ve konum bildiren özel kullanımlar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başın boyuna oturduğu nokta, bedendeki belirli bir yerleşme yeri olarak adlandırılır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Çoğul kalıp ifadeler kişilerin yerlerini, konumlarını, düzeylerini, evlerini veya alışılmış düzenlerini gösterebilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı biçim, belirli bir bölgedeki özel yerin adı olarak da aktarılır."}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın tek bir yalın anlam olmadığını, bedensel yer, kalıplaşmış konum ve özel yer adı kullanımlarını bir şemsiye altında topladığını gösterir.","boundary_detail":"Bu dal genel olarak evde yaşama anlamına genişletilemez; bedensel yerleşme noktası, kalıplaşmış konum anlatıları ve özel yer adıyla sınırlıdır.","branch_image_ar":"موضع الاستقرار","concept_gloss":"sabit yer ve konum bildiren özel kullanımlar","contextual_glosses":[{"applicability":"Söz bedensel yapıda baş ile boynun birleştiği yerleşme noktasını gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başın boyun üzerindeki belirli oturma noktasını korur."},"facet_ids":["F001"],"text":"başın boyuna oturduğu yer","usage_role":"explanatory"},{"applicability":"Çoğul kalıp kişilerin yerlerinde, düzeylerinde veya olağan düzenlerinde kalmasını anlattığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hem fiziksel konum hem alışılmış düzen yorumunu açıkça korur."},"facet_ids":["F002"],"text":"yerlerinizde ve alışılmış düzeninizde","usage_role":"contextual"}],"definition":"Sabit yer veya konum düşüncesine bağlı birkaç özel kullanımdır: başın boyuna oturduğu nokta, çoğul kalıplarda kişilerin yerleri, konumları, düzeyleri ya da alışılmış düzenleri ve belirli bir yer adı. Bunlar genel yerleşip yaşama eylemi değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başın boyuna oturduğu nokta, bedendeki belirli bir yerleşme yeri olarak adlandırılır."},{"facet_id":"F002","role":"associated_use","statement":"Çoğul kalıp ifadeler kişilerin yerlerini, konumlarını, düzeylerini, evlerini veya alışılmış düzenlerini gösterebilir."},{"facet_id":"F003","role":"source_variant","statement":"Aynı biçim, belirli bir bölgedeki özel yerin adı olarak da aktarılır."}],"identity_rationale":"Kaynak sözü tek bir genel yer anlamından fazlasını içerir: özel bir yer adı, başın boyuna oturduğu nokta ve kalıplaşmış çoğul ifadelerde yerler, konumlar, düzeyler veya alışılmış düzen vardır. Dal korunabilir, ancak yalnız bu özel ve kalıplaşmış yerleşiklik kullanımlarının şemsiyesi olarak tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"başın boyuna oturduğu yer"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"yerlerinizde, konumlarınızda veya alışılmış düzeninizde"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"belirli bir bölgedeki özel yer adı"}],"lexicalization_note":"Tanım özel yer adını, bedensel yeri ve çoğul kalıp ifadeleri ayrı tutar; bunlardan genel bir yalın yerleşme anlamı çıkarmaz.","neighbor_coverage_note":"Bütün komşu adaylar değerlendirildi. Seçilenler genel yerleşme, bedensel bölüm ve özel yer adı sınırlarını açıklar; kalanlar yükseklik, başka yer adları veya yalnız mekanda kalma eylemidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak yalnız özel ad ve kalıplarda yaşayan yer-konum kullanımlarını toplar; komşu gündelik ve üretken yerleşme ile konut alanıdır.","focus_only":"Odak dal bedensel yerleşme noktası, kalıplaşmış konumlar ve özel bir yer adıyla sınırlıdır.","gloss":"özel sabit konum ile yerleşme","neighbor_only":"Komşu dal genel olarak bir yere yerleşip yaşamayı, konutu ve başkasını orada oturtmayı anlatır.","neighbor_ref":"root_000726/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da bir şeyin bulunduğu ya da kalıcı biçimde bağlı olduğu yer düşüncesi vardır."},{"boundary_match":"partial","distinction":"Odakta baş ile boynun birleştiği özel oturma noktası vardır; komşuda kuşak çevresindeki orta ve yan bölüm belirleyicidir.","focus_only":"Odak dal bedende özellikle başın boyuna oturduğu noktayı gösterir ve başka kalıplaşmış yer kullanımları da taşır.","gloss":"baş-boyun yerleşme noktası ile orta bölüm","neighbor_only":"Komşu dal bel, yan taraf ve çevreleyen kuşağın bulunduğu orta bölgeyi insan, hayvan, bitki ve yeryüzü biçimlerine yayar.","neighbor_ref":"root_001519/B004","relation_type":"near_neighbor","shared_zone":"İki dal bir bütünün bedensel veya biçimsel olarak belirlenmiş bölümünü yer bakımından gösterebilir."},{"boundary_match":"field_only","distinction":"Özel yer adları farklı gönderimlere sahiptir; ayrıca odaktaki bedensel ve toplumsal konum kullanımları komşunun at bekleme yeri anlamında bulunmaz.","focus_only":"Odak dal özel yer adının yanında bedensel ve kalıplaşmış konum anlamları taşır.","gloss":"özel yer ve bekleme konumu","neighbor_only":"Komşu dal başka bir özel yer adını ve atların salınmadan önce beklediği yeri gösterir.","neighbor_ref":"root_000291/B009","relation_type":"same_field","shared_zone":"Her iki dal belirli bir yer adı veya sabit duruş yeri olarak kullanılabilir."}],"source_phrase_ar":"موضع من أرض الكوفة؛ السكنة مقر الرأس من العنق؛ استقروا على سكناتكم أي على مواضعكم ومساكنكم؛ الناس على سكناتهم أي على استقامتهم؛ على طبقاتهم ومنازلهم","source_summary":"Toplu kaynak sözü sabit yer düşüncesine bağlı fakat birbirinden ayrılması gereken kullanımları verir: bedensel yerleşme noktası, çoğul kalıplarda yer ve düzen anlatımı ile belirli bir özel yer adı.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه السكنات بمعنى المواضع والمساكن والطبقات والمنازل ومقر الرأس من العنق","what_is_not_ar":"ليس فعل السكنى العام ولا أهل الدار"},"support_links":[]},{"boundary":"Dal her türlü yiyeceği veya otlağı değil, geçimi sürdürerek insanı ya da sürüyü bulunduğu yerde tutan yeterli besin kaynağını anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000726/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:2:1","qac_word_ref":"90:16:2","surface_ar":"مِسْكِينًا"}],"gloss":"yerinde kalmayı sağlayan geçimlik ve bol otlak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yiyecek veya geçimlik, kişinin yaşamını sürdürmesini ve bulunduğu yerde kalmasını sağlar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sürüyü göç ettirmeye gerek bırakmayacak kadar bol otlak, aynı yerinde tutma işleviyle nitelenir."}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan için geçimlik yiyeceği ve sürü için göçü gereksiz kılan bol otlağı ortak işlevleriyle birlikte karşılar.","boundary_detail":"Dal her türlü yiyeceği veya otlağı değil, geçimi sürdürerek insanı ya da sürüyü bulunduğu yerde tutan yeterli besin kaynağını anlatır.","branch_image_ar":"قوت يثبت المقام","concept_gloss":"yerinde kalmayı sağlayan geçimlik ve bol otlak","contextual_glosses":[{"applicability":"İnsanın geçimini sürdürmesine ve bulunduğu yerde yaşamaya devam etmesine yarayan besinler kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaşamı sürdürmeye yarayan yiyeceklerin geçimlik işlevini korur."},"facet_ids":["F001"],"text":"geçimlik yiyecekler","usage_role":"contextual"},{"applicability":"Sürünün besin bulmak için başka yere götürülmesine gerek bırakmayan otlak anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Otlak bolluğunu ve bunun göç gereğini kaldırma sonucunu birlikte korur."},"facet_ids":["F002"],"text":"göç gerektirmeyecek kadar bol otlak","usage_role":"explanatory"}],"definition":"İnsanın geçimini sürdürüp bulunduğu yerde kalmasını sağlayan yiyecek veya geçimliktir. Hayvancılık bağlamında, sürünün başka yere göç etmesini gerektirmeyecek kadar bol otlak aynı işlevle nitelenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yiyecek veya geçimlik, kişinin yaşamını sürdürmesini ve bulunduğu yerde kalmasını sağlar."},{"facet_id":"F002","role":"specialization","statement":"Sürüyü göç ettirmeye gerek bırakmayacak kadar bol otlak, aynı yerinde tutma işleviyle nitelenir."}],"identity_rationale":"Kaynak sözü yiyecek ve geçimlikleri, kişinin onların sayesinde yerinde kalabilmesiyle açıklar; bol otlak da topluluğu göç etmekten alıkoyduğu için aynı işlevsel çizgidedir. Dal çerçevesi besin ile yerinde kalma sonucunu doğru biçimde birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"bulunduğu yerde geçinmeyi sağlayan yiyecekler"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"yerinde kalmayı sağlayan bir geçimlik"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"sürüyü göç ettirmeye gerek bırakmayacak kadar bol otlak"}],"lexicalization_note":"Tanım geçimlik yiyecek biçimlerini yalın besin alanında, bol otlak kalıbını ise göçü gereksiz kılan özel hayvancılık bağlamında ayrı tutar.","neighbor_coverage_note":"Bütün komşu kartları değerlendirildi. Seçilenler genel temel yiyecek, az idarelik ve genel otlakla sınırı kurar; kalanlar pay, göçebe yaşam, otlatma eylemi veya yeterlilik sonucuna odaklanır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta yiyeceğin yer değiştirmeyi önleyip kalışı sağlaması belirgindir; komşuda temel sonuç bedenin ve yaşamın sürmesidir.","focus_only":"Odak dal besinin kişiyi bulunduğu yerde tutma işlevini ve bol otlak uzantısını içerir.","gloss":"yerinde tutan geçimlik ile yaşatan yiyecek","neighbor_only":"Komşu dal bedeni ayakta ve yaşamı sürer tutan yiyeceği, başkasını besleme eylemleriyle birlikte genel olarak kapsar.","neighbor_ref":"root_001268/B001","relation_type":"near_synonym","shared_zone":"İki dal da yaşamı sürdürmek için gereken temel yiyecek ve geçimliği anlatır."},{"boundary_match":"partial","distinction":"Odak yerinde kalmaya yetecek kaynak ve hatta bolluk içerir; komşu özellikle kıt, geçici ve ancak idare ettiren miktara yönelir.","focus_only":"Odak dal yeterli geçimliği ve göçü gereksiz kılan bol otlağı kapsar.","gloss":"yeterli geçimlik ile az idarelik","neighbor_only":"Komşu dal insan veya hayvanın bir süre idare etmesini sağlayan az yiyeceği ve bahara kadar yeten sınırlı otlamayı öne çıkarır.","neighbor_ref":"root_001039/B006","relation_type":"near_synonym","shared_zone":"Her iki dal insanın veya hayvanın yaşamını sürdürmesine yetecek besin kaynağını anlatabilir."},{"boundary_match":"partial","distinction":"Odak yalnız göç gereğini kaldıracak bolluktaki otlağı niteler; komşu her tür ot ve otlak için genel addır.","focus_only":"Odak dal otlağın bol olup sürüyü bulunduğu yerde tutması koşulunu taşır ve insan geçimliğine de uzanır.","gloss":"bol yerleşik otlak ile genel otlak","neighbor_only":"Komşu dal hayvanların yediği ot ve otlağı, bolluk veya yerinde tutma koşulu olmadan genel olarak adlandırır.","neighbor_ref":"root_000003/B001","relation_type":"near_neighbor","shared_zone":"İki dalın hayvancılık alanında ortak gönderimi otlayan hayvana besin sağlayan bitki ve otlaktır."}],"source_phrase_ar":"الأسكان الأقوات واحدها سكن؛ قيل للقوت سكن لأن المكان به يسكن؛ مرعى مسكن إذا كان كثيرا لا يخرج إلى الظعن عنه","source_summary":"Tek kaynaklı anlatım, yiyecek ve geçimliği kişinin yerinde kalmasını sağlayan destek olarak açıklar; bol otlağı da sürüyü başka yere götürme gereğini kaldırdığı için aynı çizgiye bağlar.","sources":["TA"],"what_is_ar":"يدخل فيه الأسكان بمعنى الأقوات والمرعى المسكن الكثير الذي لا يخرج عنه إلى الظعن","what_is_not_ar":"ليس المسكن بمعنى البيت ولا السكينة"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["90:16:1"],"branch_refs":[],"candidate_id":"cand_4e71b1593496806cef41","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:16:1:boundary-launch","source_type":"word_analysis","support_ids":["sup_e2f8c9fb98678e6874f8","sup_f700eff8246ca2cc1c60"],"title":"opening position bridges back before the noun appears","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:1","qac_refs":["90:16:1:1"],"status":"accepted"}},{"anchor_refs":["90:16:1"],"branch_refs":[],"candidate_id":"cand_4075fa56f56279b5fc45","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:16:1:continuing-alternative-object","source_type":"word_analysis","support_ids":["sup_e1f5941033bc34c46ef6","sup_f700eff8246ca2cc1c60"],"title":"alternative particle keeps the feeding frame open","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:1","qac_refs":["90:16:1:1"],"status":"accepted"}},{"anchor_refs":["90:16:1"],"branch_refs":[],"candidate_id":"cand_76064c6affe25b9e3040","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:16:1:matched-recipient-cadence","source_type":"word_analysis","support_ids":["sup_aa1d75a7cc7535036eef","sup_f700eff8246ca2cc1c60"],"title":"short particle resets into a matched recipient","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:1","qac_refs":["90:16:1:1"],"status":"accepted"}},{"anchor_refs":["90:16:1"],"branch_refs":[],"candidate_id":"cand_64c756538751317e9cf5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:16:1:widening-without-collapse","source_type":"word_analysis","support_ids":["sup_80a0af6936531fe24648","sup_f700eff8246ca2cc1c60"],"title":"real alternative widens the duty without merging recipients","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:1","qac_refs":["90:16:1:1"],"status":"accepted"}},{"anchor_refs":["90:16:2"],"branch_refs":[],"candidate_id":"cand_d4b912987db515de6019","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000726"],"scope":"focus_ayah","source_local_id":"90:16:2:agency-contrast","source_type":"word_analysis","support_ids":["sup_33644436ecb6f7f0b4d3","sup_bb093e352ef3a6e943d3"],"title":"dust exposure intensifies without erasing agency","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:2","qac_refs":["90:16:2:1"],"status":"accepted"}},{"anchor_refs":["90:16:2"],"branch_refs":[],"candidate_id":"cand_40274a6dbb8aab0f9474","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000726"],"scope":"focus_ayah","source_local_id":"90:16:2:human-claim-holder","source_type":"word_analysis","support_ids":["sup_11c9521410f32e43757f","sup_bb093e352ef3a6e943d3"],"title":"social descriptor becomes the claim-holder","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:2","qac_refs":["90:16:2:1"],"status":"accepted"}},{"anchor_refs":["90:16:2"],"branch_refs":[],"candidate_id":"cand_cb2cc963b56d0c2ff73b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000726"],"scope":"focus_ayah","source_local_id":"90:16:2:open-singular-durable-person","source_type":"word_analysis","support_ids":["sup_4c24dc65782e12534a1d","sup_bb093e352ef3a6e943d3"],"title":"indefinite singular makes need open and concrete","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:2","qac_refs":["90:16:2:1"],"status":"accepted"}},{"anchor_refs":["90:16:2"],"branch_refs":[],"candidate_id":"cand_1eaaaf87a327b8b79a43","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000726"],"scope":"focus_ayah","source_local_id":"90:16:2:person-before-condition-cadence","source_type":"word_analysis","support_ids":["sup_3fc18a07645199a7a252","sup_bb093e352ef3a6e943d3"],"title":"person is heard before and with the condition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:2","qac_refs":["90:16:2:1"],"status":"accepted"}},{"anchor_refs":["90:16:2"],"branch_refs":[],"candidate_id":"cand_7b667f3a2b75c5d9fe29","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000726"],"scope":"focus_ayah","source_local_id":"90:16:2:qualified-by-dust-phrase","source_type":"word_analysis","support_ids":["sup_767a1bf68f9d33cb7a39","sup_bb093e352ef3a6e943d3"],"title":"alternative covers the whole dust-qualified recipient","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:2","qac_refs":["90:16:2:1"],"status":"accepted"}},{"anchor_refs":["90:16:2"],"branch_refs":[],"candidate_id":"cand_530cdf18a47b9c0c9cb4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000726"],"scope":"focus_ayah","source_local_id":"90:16:2:recipient-sequence-shift","source_type":"word_analysis","support_ids":["sup_5eeecd344ad622899911","sup_bb093e352ef3a6e943d3"],"title":"recipient pair shifts from kin-loss to material deprivation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:2","qac_refs":["90:16:2:1"],"status":"accepted"}},{"anchor_refs":["90:16:2"],"branch_refs":[],"candidate_id":"cand_4b2d084959e4c1d3ed45","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000726"],"scope":"focus_ayah","source_local_id":"90:16:2:remote-accusative-recipient","source_type":"word_analysis","support_ids":["sup_166a1c626c29de1cbbe2","sup_bb093e352ef3a6e943d3"],"title":"accusative needy person remains governed by feeding","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:2","qac_refs":["90:16:2:1"],"status":"accepted"}},{"anchor_refs":["90:16:2"],"branch_refs":[],"candidate_id":"cand_c336009be87edf24ab0c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000726"],"scope":"focus_ayah","source_local_id":"90:16:2:settled-need-and-provision","source_type":"word_analysis","support_ids":["sup_5d7ea825115a468903a1","sup_bb093e352ef3a6e943d3"],"title":"settlement and lodging fields make need feel established","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:2","qac_refs":["90:16:2:1"],"status":"accepted"}},{"anchor_refs":["90:16:2"],"branch_refs":[],"candidate_id":"cand_30b371636e318309b6d4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000726"],"scope":"focus_ayah","source_local_id":"90:16:2:soft-need-to-dust-closure","source_type":"word_analysis","support_ids":["sup_9ac460f9d569a68e47a0","sup_bb093e352ef3a6e943d3"],"title":"sound moves from subdued need to harder dust","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:2","qac_refs":["90:16:2:1"],"status":"accepted"}},{"anchor_refs":["90:16:2"],"branch_refs":[],"candidate_id":"cand_295090b98815d27d6ad1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000726"],"scope":"focus_ayah","source_local_id":"90:16:2:stilled-capacity-pressure","source_type":"word_analysis","support_ids":["sup_bb093e352ef3a6e943d3","sup_bd8eb6e98c0f0d73398c"],"title":"poverty sense carries arrested-capacity pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:2","qac_refs":["90:16:2:1"],"status":"accepted"}},{"anchor_refs":["90:16:3"],"branch_refs":[],"candidate_id":"cand_3bea4cdadc762fe2a688","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:16:3:boundary-skeleton","source_type":"word_analysis","support_ids":["sup_3d9827a2d2fb2fe5fffc","sup_a8fd36f74819c316ed76"],"title":"possessor skeleton carries the sequence across hunger, kinship, and dust","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:3","qac_refs":["90:16:3:1"],"status":"accepted"}},{"anchor_refs":["90:16:3"],"branch_refs":[],"candidate_id":"cand_aac7098cbc45ed2f24de","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:16:3:characterization-not-property","source_type":"word_analysis","support_ids":["sup_59a0acd9b24f366901d5","sup_a8fd36f74819c316ed76"],"title":"possession means characterized by dust-poverty","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:3","qac_refs":["90:16:3:1"],"status":"accepted"}},{"anchor_refs":["90:16:3"],"branch_refs":[],"candidate_id":"cand_380a3ef52884408967a3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:16:3:compact-five-noun-form","source_type":"word_analysis","support_ids":["sup_a8fd36f74819c316ed76","sup_bcbea1c847a559514fe1"],"title":"small five-noun form carries agreement and dependency","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:3","qac_refs":["90:16:3:1"],"status":"accepted"}},{"anchor_refs":["90:16:3"],"branch_refs":[],"candidate_id":"cand_113fcb9d73a8ad430b8a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:16:3:construct-binding","source_type":"word_analysis","support_ids":["sup_9f88e2438f647c04bd68","sup_a8fd36f74819c316ed76"],"title":"construct head binds the dust complement","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:3","qac_refs":["90:16:3:1"],"status":"accepted"}},{"anchor_refs":["90:16:3"],"branch_refs":[],"candidate_id":"cand_54a53d59baad22cab19e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:16:3:delayed-genitive-bridge","source_type":"word_analysis","support_ids":["sup_a42731e85c722d9fd64b","sup_a8fd36f74819c316ed76"],"title":"construct bridge delays the final dust noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:3","qac_refs":["90:16:3:1"],"status":"accepted"}},{"anchor_refs":["90:16:3"],"branch_refs":[],"candidate_id":"cand_3fc4f624ae7a7ac29568","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:16:3:dependent-object-chain","source_type":"word_analysis","support_ids":["sup_219394049dfaabc8a7c6","sup_a8fd36f74819c316ed76"],"title":"qualifier remains inside the fed-object chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:3","qac_refs":["90:16:3:1"],"status":"accepted"}},{"anchor_refs":["90:16:3"],"branch_refs":[],"candidate_id":"cand_091ca9d7be851cbd4520","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:16:3:identity-state-convergence","source_type":"word_analysis","support_ids":["sup_8bd474c2951a19374e17","sup_a8fd36f74819c316ed76"],"title":"classification and state both intensify one recipient","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:3","qac_refs":["90:16:3:1"],"status":"accepted"}},{"anchor_refs":["90:16:3"],"branch_refs":[],"candidate_id":"cand_822ec10639462fba73b8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:16:3:phrase-hinge","source_type":"word_analysis","support_ids":["sup_5d0cfbdba172bf850020","sup_a8fd36f74819c316ed76"],"title":"central hinge converts person and dust into one identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:3","qac_refs":["90:16:3:1"],"status":"accepted"}},{"anchor_refs":["90:16:3"],"branch_refs":[],"candidate_id":"cand_8265004fc4d30eb619ff","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:16:3:repeated-possessor-frame","source_type":"word_analysis","support_ids":["sup_a8fd36f74819c316ed76","sup_c116fad4f3b3825fd15f"],"title":"same possessor frame changes the attached claim","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:3","qac_refs":["90:16:3:1"],"status":"accepted"}},{"anchor_refs":["90:16:4"],"branch_refs":[],"candidate_id":"cand_79004e11ef2a04fc3180","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000178"],"scope":"focus_ayah","source_local_id":"90:16:4:abstract-indefinite-form","source_type":"word_analysis","support_ids":["sup_1c4f8ae0c84bf4f5b727","sup_cc00e8ad5deb496c4880"],"title":"abstract indefinite form turns dust into a state","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:4","qac_refs":["90:16:4:1"],"status":"accepted"}},{"anchor_refs":["90:16:4"],"branch_refs":[],"candidate_id":"cand_368be44a5dd2b7550a73","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000178"],"scope":"focus_ayah","source_local_id":"90:16:4:abstract-qualifier-chain","source_type":"word_analysis","support_ids":["sup_6d1c4a42177882f9431c","sup_cc00e8ad5deb496c4880"],"title":"third abstract qualifier completes the feeding chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:4","qac_refs":["90:16:4:1"],"status":"accepted"}},{"anchor_refs":["90:16:4"],"branch_refs":[],"candidate_id":"cand_540ad37e8663d36adb82","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000178"],"scope":"focus_ayah","source_local_id":"90:16:4:condition-not-location","source_type":"word_analysis","support_ids":["sup_48be2dd64094075f8943","sup_cc00e8ad5deb496c4880"],"title":"dust is borne condition, not mere place","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:4","qac_refs":["90:16:4:1"],"status":"accepted"}},{"anchor_refs":["90:16:4"],"branch_refs":[],"candidate_id":"cand_cdf79ad7a8bc0f6ccce5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000178"],"scope":"focus_ayah","source_local_id":"90:16:4:condition-noun-choice","source_type":"word_analysis","support_ids":["sup_2a7683a2e769eb9e217d","sup_cc00e8ad5deb496c4880"],"title":"condition noun intensifies attachment to the person","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:4","qac_refs":["90:16:4:1"],"status":"accepted"}},{"anchor_refs":["90:16:4"],"branch_refs":[],"candidate_id":"cand_8c8008ed82ed60c025c6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000178"],"scope":"focus_ayah","source_local_id":"90:16:4:dust-origin-contrast","source_type":"word_analysis","support_ids":["sup_0aac658e5fd079a08663","sup_cc00e8ad5deb496c4880"],"title":"human origin dust contrasts with social dust-poverty","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:4","qac_refs":["90:16:4:1"],"status":"accepted"}},{"anchor_refs":["90:16:4"],"branch_refs":[],"candidate_id":"cand_252261de6891d4ced85b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000178"],"scope":"focus_ayah","source_local_id":"90:16:4:embodied-lowered-deprivation","source_type":"word_analysis","support_ids":["sup_71965e3769f01b5baed6","sup_cc00e8ad5deb496c4880"],"title":"dust image makes deprivation spatial and tactile","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:4","qac_refs":["90:16:4:1"],"status":"accepted"}},{"anchor_refs":["90:16:4"],"branch_refs":[],"candidate_id":"cand_d1b6d80f39e399acc8aa","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000178"],"scope":"focus_ayah","source_local_id":"90:16:4:genitive-construct-complement","source_type":"word_analysis","support_ids":["sup_911810c0db479d53f759","sup_cc00e8ad5deb496c4880"],"title":"genitive dust-condition completes the construct","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:4","qac_refs":["90:16:4:1"],"status":"accepted"}},{"anchor_refs":["90:16:4"],"branch_refs":[],"candidate_id":"cand_4654b8574aba467bd4e4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000178"],"scope":"focus_ayah","source_local_id":"90:16:4:marked-rare-final-noun","source_type":"word_analysis","support_ids":["sup_5c3917e92a81f16b3bb2","sup_cc00e8ad5deb496c4880"],"title":"marked noun carries the memorable final image","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:4","qac_refs":["90:16:4:1"],"status":"accepted"}},{"anchor_refs":["90:16:4"],"branch_refs":[],"candidate_id":"cand_754d8e73a9011dc5c158","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000178"],"scope":"focus_ayah","source_local_id":"90:16:4:nearness-to-dust-echo","source_type":"word_analysis","support_ids":["sup_cc00e8ad5deb496c4880","sup_fc5061c17234a40e439f"],"title":"nearness is answered by dust across the boundary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:4","qac_refs":["90:16:4:1"],"status":"accepted"}},{"anchor_refs":["90:16:4"],"branch_refs":[],"candidate_id":"cand_345c3523ee0efcf1f38e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000178"],"scope":"focus_ayah","source_local_id":"90:16:4:remote-body-register","source_type":"word_analysis","support_ids":["sup_cc00e8ad5deb496c4880","sup_da8ad9e24aab8b3d67e1"],"title":"body-register remains secondary image pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:4","qac_refs":["90:16:4:1"],"status":"accepted"}},{"anchor_refs":["90:16:4"],"branch_refs":[],"candidate_id":"cand_a727ec49fa977be266e0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000178"],"scope":"focus_ayah","source_local_id":"90:16:4:rough-cadence-closure","source_type":"word_analysis","support_ids":["sup_89b02d2ca2de0777c223","sup_cc00e8ad5deb496c4880"],"title":"rough terminal cadence reinforces dust exposure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:4","qac_refs":["90:16:4:1"],"status":"accepted"}},{"anchor_refs":["90:16:4"],"branch_refs":[],"candidate_id":"cand_f5847fafca8ce112a7b0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000178"],"scope":"focus_ayah","source_local_id":"90:16:4:selected-dust-poverty","source_type":"word_analysis","support_ids":["sup_74f6e8fc1943a309906e","sup_cc00e8ad5deb496c4880"],"title":"dust-poverty selected from the concrete dust field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:4","qac_refs":["90:16:4:1"],"status":"accepted"}},{"anchor_refs":["90:16:4"],"branch_refs":[],"candidate_id":"cand_be3760364de1b301bab0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000178"],"scope":"focus_ayah","source_local_id":"90:16:4:terminal-descent","source_type":"word_analysis","support_ids":["sup_0e2d057437a9912d374c","sup_cc00e8ad5deb496c4880"],"title":"final word lands the phrase at earth-level exposure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:16:4","qac_refs":["90:16:4:1"],"status":"accepted"}},{"anchor_refs":["90:16:2"],"branch_refs":[],"candidate_id":"cand_71365a7b1112df443543","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000726"],"scope":"focus_ayah","source_local_id":"90:16:2:1","source_type":"qac_morpheme","support_ids":["sup_b3974b4f141a9e439ad8"],"title":"QAC root occurrence: س ك ن","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["90:16:4"],"branch_refs":[],"candidate_id":"cand_0e70e064fa10c0be916b","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000178"],"scope":"focus_ayah","source_local_id":"90:16:4:1","source_type":"qac_morpheme","support_ids":["sup_2a894aa7dcb5b92eadcc"],"title":"QAC root occurrence: ت ر ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["90:16"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:16","branch_refs":["root_000178/B002","root_000726/B006"],"candidate_id":"cand_be651fe27538963c049a","commentary_obligation":"review","hft_ref":"hft_88dfd1d74ac9421244e3","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b01_doubled_destitution_ground_contact","source_type":"hft","support_ids":["sup_5f93873b9ef4550e8a28"],"title":"b01_doubled_destitution_ground_contact","trust":"legacy_unbound"},{"anchor_refs":["90:16"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:16","branch_refs":["root_000178/B001","root_000726/B002","root_000726/B004"],"candidate_id":"cand_16ac7270564b8253f787","commentary_obligation":"review","hft_ref":"hft_4bfd824d5343a3347964","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b02_dwelling_collapsed_to_earth","source_type":"hft","support_ids":["sup_6c7bebbe0510e7ee6c6a"],"title":"b02_dwelling_collapsed_to_earth","trust":"legacy_unbound"},{"anchor_refs":["90:16"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:16","branch_refs":["root_000178/B002","root_000726/B001"],"candidate_id":"cand_36aa152bde7319a39696","commentary_obligation":"review","hft_ref":"hft_f840aa578e408b476d1e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b03_need_as_arrested_motion","source_type":"hft","support_ids":["sup_c0ee4e992d753eb99c0b"],"title":"b03_need_as_arrested_motion","trust":"legacy_unbound"},{"anchor_refs":["90:16"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:16","branch_refs":["root_000178/B002","root_000178/B003"],"candidate_id":"cand_9a5d0e08f611f381e4e7","commentary_obligation":"review","hft_ref":"hft_e0c33b4db0c04cd505ac","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b04_possessor_without_possession","source_type":"hft","support_ids":["sup_49916f564214d41f785d"],"title":"b04_possessor_without_possession","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"أَوْ مِسْكِينًۭا ذَا مَتْرَبَةٍۢ","qac_morphemes":[{"lemma_ar":"أَو","morph_features":"STEM|POS:CONJ|LEM:>aw","morpheme_role":"STEM","pos":"CONJ","qac_ref":"90:16:1:1","qac_word_ref":"90:16:1","root_ar":"","surface_ar":"أَوْ"},{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:2:1","qac_word_ref":"90:16:2","root_ar":"س ك ن","surface_ar":"مِسْكِينًا"},{"lemma_ar":"ذَا","morph_features":"STEM|POS:N|LEM:*aA|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:3:1","qac_word_ref":"90:16:3","root_ar":"","surface_ar":"ذَا"},{"lemma_ar":"مَتْرَبَة","morph_features":"STEM|POS:N|LEM:matorabap|ROOT:trb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:4:1","qac_word_ref":"90:16:4","root_ar":"ت ر ب","surface_ar":"مَتْرَبَةٍ"}],"word_analysis_qac_refs":[["90:16:1:1"],["90:16:2:1"],["90:16:3:1"],["90:16:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["90:16:1","90:16:2","90:16:3","90:16:4"]},"focus_surface_evidence":{"arabic_uthmani":"أَوْ مِسْكِينًۭا ذَا مَتْرَبَةٍۢ","qac_morphemes":[{"lemma_ar":"أَو","morph_features":"STEM|POS:CONJ|LEM:>aw","morpheme_role":"STEM","pos":"CONJ","qac_ref":"90:16:1:1","qac_word_ref":"90:16:1","root_ar":"","surface_ar":"أَوْ"},{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:2:1","qac_word_ref":"90:16:2","root_ar":"س ك ن","surface_ar":"مِسْكِينًا"},{"lemma_ar":"ذَا","morph_features":"STEM|POS:N|LEM:*aA|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:3:1","qac_word_ref":"90:16:3","root_ar":"","surface_ar":"ذَا"},{"lemma_ar":"مَتْرَبَة","morph_features":"STEM|POS:N|LEM:matorabap|ROOT:trb|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:16:4:1","qac_word_ref":"90:16:4","root_ar":"ت ر ب","surface_ar":"مَتْرَبَةٍ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["90:16:1:1"],["90:16:2:1"],["90:16:3:1"],["90:16:4:1"]],"word_analysis_refs":["90:16:1","90:16:2","90:16:3","90:16:4"],"word_rows":[{"analysis_record_ref":"90:16:1","analytic_gloss_range_en":"coordinating alternative particle that carries the prior feeding frame into a second recipient option without starting a new command","analytic_root_gloss_range_en":null,"qac_refs":["90:16:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"أَوْ","transliteration":"aw"}},{"analysis_record_ref":"90:16:2","analytic_gloss_range_en":"an indefinite singular needy person as the accusative fed recipient, locally specified by dust-level exposure and colored by stilled-capacity pressure","analytic_root_gloss_range_en":"broad root range around stillness, dwelling, tranquility, provision that enables staying, and poverty or abasement; the local frame selects needy-person poverty while retaining arrested and settled need as pressure","qac_refs":["90:16:2:1"],"root":{"arabic":"س ك ن","transliteration":"s-k-n"},"surface":{"arabic":"مِسْكِينًۭا","transliteration":"miskīnan"}},{"analysis_record_ref":"90:16:3","analytic_gloss_range_en":"accusative five-noun construct meaning one characterized by or bearing the following dust-poverty condition as a qualifier of the needy person","analytic_root_gloss_range_en":"root range includes possessor or characterized-by forms, relative-pronoun uses, demonstrative uses, and interrogative-relative constructions; the local construct selects characterization by an attached genitive condition","qac_refs":["90:16:3:1"],"root":{"arabic":"ذ و و","transliteration":"dh-w-w"},"surface":{"arabic":"ذَا","transliteration":"dhā"}},{"analysis_record_ref":"90:16:4","analytic_gloss_range_en":"an indefinite genitive abstract noun naming dust-poverty as the condition borne by the needy person; locally poverty as earth-contact rather than neutral soil or remote root branches","analytic_root_gloss_range_en":"root range includes soil and dust, poverty as clinging to dust, wealth by dust-like abundance, equal-age companionship, body and fingertip terms, plant/place names, and other remote branches; the local construct selects dust-poverty while retaining concrete earth-contact pressure","qac_refs":["90:16:4:1"],"root":{"arabic":"ت ر ب","transliteration":"t-r-b"},"surface":{"arabic":"مَتْرَبَةٍۢ","transliteration":"matrabatin"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["90:16"],"branch_refs":["root_000178/B002","root_000726/B006"],"candidate_id":"cand_be651fe27538963c049a","evidence_scope":"focus_ayah","hft_ref":"hft_88dfd1d74ac9421244e3","item_id":"b01_doubled_destitution_ground_contact","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b01_doubled_destitution_ground_contact","support_id":"sup_5f93873b9ef4550e8a28"},{"anchor_refs":["90:16"],"branch_refs":["root_000178/B001","root_000726/B002","root_000726/B004"],"candidate_id":"cand_16ac7270564b8253f787","evidence_scope":"focus_ayah","hft_ref":"hft_4bfd824d5343a3347964","item_id":"b02_dwelling_collapsed_to_earth","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b02_dwelling_collapsed_to_earth","support_id":"sup_6c7bebbe0510e7ee6c6a"},{"anchor_refs":["90:16"],"branch_refs":["root_000178/B002","root_000726/B001"],"candidate_id":"cand_36aa152bde7319a39696","evidence_scope":"focus_ayah","hft_ref":"hft_f840aa578e408b476d1e","item_id":"b03_need_as_arrested_motion","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b03_need_as_arrested_motion","support_id":"sup_c0ee4e992d753eb99c0b"},{"anchor_refs":["90:16"],"branch_refs":["root_000178/B002","root_000178/B003"],"candidate_id":"cand_9a5d0e08f611f381e4e7","evidence_scope":"focus_ayah","hft_ref":"hft_e0c33b4db0c04cd505ac","item_id":"b04_possessor_without_possession","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b04_possessor_without_possession","support_id":"sup_49916f564214d41f785d"}],"diagnostics":[],"lane_counts":{"global":16,"macro":5,"micro":4},"packet_summary":{"ayah_count":20,"focus_ref":"90:16","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ح ل ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000351","furuq_root_norm":"ح ل ل","furuq_source_root_norm":"ح ل ل","is_dominant":true,"target_occurrences":39,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000353","furuq_root_norm":"ح ل ي","furuq_source_root_norm":"ح ل ي","is_dominant":false,"target_occurrences":6,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"و ص د","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000036","furuq_root_norm":"ء ص د","furuq_source_root_norm":"أ ص د","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001653","furuq_root_norm":"و ص د","furuq_source_root_norm":"و ص د","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["90:1","90:2","90:3","90:4","90:5","90:6","90:7","90:8","90:9","90:10","90:11","90:12","90:13","90:14","90:15","90:16","90:17","90:18","90:19","90:20"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"90:16","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"90:16","lane":"micro","linguistic_source_ref":"90:16","surface_ref":"90:16","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"90:16","target_tokens":[["ya",["90:16:1"]],["da",["90:16:1"]],["toprağa",["90:16:4"]],["bulanmış",["90:16:3","90:16:4"]],["bir",["90:16:2"]],["yoksula",["90:16:2"]]],"text":"ya da toprağa bulanmış bir yoksula."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":11,"ayah_to":20,"id":"s090-p02-011-020","label":"The steep path and the two companies","number":2,"refs":["90:11","90:12","90:13","90:14","90:15","90:16","90:17","90:18","90:19","90:20"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:4:dust-origin-contrast","source_type":"word_analysis","support_id":"sup_0aac658e5fd079a08663","text":"{\"blocking_evidence\":null,\"headline\":\"human origin dust contrasts with social dust-poverty\",\"reader_payoff\":\"The reader sees that dust here is not only origin or return material; in 90:16 it becomes social responsibility toward the exposed poor, with 30:20 as contrast.\",\"reason\":\"The concrete 30:20 row supplies contrast: dust as origin elsewhere does not control the local parse, but it sharpens the social use of dust-poverty here.\",\"representative_source_ids\":[\"QI-0f04701f\",\"QI-e04f58e4\",\"MI-5334f8d0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:4:terminal-descent","source_type":"word_analysis","support_id":"sup_0e2d057437a9912d374c","text":"{\"blocking_evidence\":null,\"headline\":\"final word lands the phrase at earth-level exposure\",\"reader_payoff\":\"The reader feels the recipient phrase descend from social category to visible ground-level condition at the ayah's close.\",\"reason\":\"The word is final in the ayah and final in the recipient phrase, so closure leaves dust-poverty as the last impression.\",\"representative_source_ids\":[\"QT-86ee5e99\",\"QT-ce8209f9\",\"QT-eb391bb7\",\"MT-b22d4134\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:2:human-claim-holder","source_type":"word_analysis","support_id":"sup_11c9521410f32e43757f","text":"{\"blocking_evidence\":null,\"headline\":\"social descriptor becomes the claim-holder\",\"reader_payoff\":\"The reader sees a human claimant generated by need, not an abstract poverty theme.\",\"reason\":\"The word functions as the fed object, and the adjective-noun form names a person characterized by need rather than an abstract state alone.\",\"representative_source_ids\":[\"QS-1600ae1e\",\"QS-26602d28\",\"QF-57d825c9\",\"QF-cb3ba849\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:2:remote-accusative-recipient","source_type":"word_analysis","support_id":"sup_166a1c626c29de1cbbe2","text":"{\"blocking_evidence\":null,\"headline\":\"accusative needy person remains governed by feeding\",\"reader_payoff\":\"The reader notices that the needy person is the object of the prior feeding act, not a standalone label of poverty.\",\"reason\":\"QAC marks the word as an indefinite masculine singular accusative adjective/noun, and attachment support keeps it under the feeding construction from 90:14-15.\",\"representative_source_ids\":[\"QG-479f3c70\",\"QG-506fc3a8\",\"QG-78b44484\",\"QG-92526b56\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:4:abstract-indefinite-form","source_type":"word_analysis","support_id":"sup_1c4f8ae0c84bf4f5b727","text":"{\"blocking_evidence\":null,\"headline\":\"abstract indefinite form turns dust into a state\",\"reader_payoff\":\"The reader sees dust packaged as a recognizable condition that can mark any exposed recipient.\",\"reason\":\"The local form is an indefinite feminine abstract noun, so it does not merely name physical dust or one known place.\",\"representative_source_ids\":[\"QF-0e127a5f\",\"QF-acdfbaf0\",\"QF-f3f6f673\",\"QF-f90edc86\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:3:dependent-object-chain","source_type":"word_analysis","support_id":"sup_219394049dfaabc8a7c6","text":"{\"blocking_evidence\":null,\"headline\":\"qualifier remains inside the fed-object chain\",\"reader_payoff\":\"The reader notices that the description remains dependent on feeding and cannot stand apart as a slogan.\",\"reason\":\"The qualifier inherits the accusative object relation through agreement with {{ar:مِسْكِينًۭا}} ({{tr:miskīnan}}), and the genitive complement supplies specification without a definite article.\",\"representative_source_ids\":[\"QG-11665446\",\"QG-8ffeb5b7\",\"MF-1cd0a888\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:4:condition-noun-choice","source_type":"word_analysis","support_id":"sup_2a7683a2e769eb9e217d","text":"{\"blocking_evidence\":null,\"headline\":\"condition noun intensifies attachment to the person\",\"reader_payoff\":\"The reader notices that the wording chooses a possessed condition noun, preserving concrete dust while joining the adjacent abstract-condition series.\",\"reason\":\"The form makes dust a social condition in the construct phrase and aligns with neighboring abstract qualifier forms rather than using a plain adjective or concrete dust noun.\",\"representative_source_ids\":[\"QF-d1c8a429\",\"QF-746bfe18\",\"QH-f68ff72a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"90:16:4:1","source_type":"qac_morpheme","support_id":"sup_2a894aa7dcb5b92eadcc","text":"{\"lemma_ar\":\"مَتْرَبَة\",\"morph_features\":\"STEM|POS:N|LEM:matorabap|ROOT:trb|F|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"90:16:4:1\",\"qac_word_ref\":\"90:16:4\",\"root_ar\":\"ت ر ب\",\"surface_ar\":\"مَتْرَبَةٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:2:agency-contrast","source_type":"word_analysis","support_id":"sup_33644436ecb6f7f0b4d3","text":"{\"blocking_evidence\":null,\"headline\":\"dust exposure intensifies without erasing agency\",\"reader_payoff\":\"The reader avoids mistaking need for total passivity; the dust qualifier heightens vulnerability while 18:79 shows needy people may still act and work.\",\"reason\":\"The contextual supplement preserves a concrete 18:79 reference; it qualifies the local vulnerability without overriding the dust-marked recipient in 90:16.\",\"representative_source_ids\":[\"QI-43c2fb8f\",\"QI-4d2f75b4\",\"QI-a91e2517\",\"MI-0321618d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:3:boundary-skeleton","source_type":"word_analysis","support_id":"sup_3d9827a2d2fb2fe5fffc","text":"{\"blocking_evidence\":null,\"headline\":\"possessor skeleton carries the sequence across hunger, kinship, and dust\",\"reader_payoff\":\"The reader notices a repeated grammatical skeleton that coordinates circumstance and recipients across 90:14-16.\",\"reason\":\"The rows track a shift from the genitive condition form in 90:14 to accusative recipient qualifiers in 90:15-16, preserving a repeated frame while changing the attached vulnerability.\",\"representative_source_ids\":[\"QF-ad815d91\",\"QE-85662836\",\"QB-1631cdcc\",\"QB-c1233198\",\"QY-4427b65d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:2:person-before-condition-cadence","source_type":"word_analysis","support_id":"sup_3fc18a07645199a7a252","text":"{\"blocking_evidence\":null,\"headline\":\"person is heard before and with the condition\",\"reader_payoff\":\"The reader first meets the person and then hears the dust-condition bound to him by the phrase's cadence.\",\"reason\":\"The noun precedes its possessor qualifier, and the tanwīn rows support an audible bond between recipient and condition.\",\"representative_source_ids\":[\"QT-a18fce84\",\"QT-a52c126a\",\"QP-2ca472d0\",\"QP-52074b8b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:4:condition-not-location","source_type":"word_analysis","support_id":"sup_48be2dd64094075f8943","text":"{\"blocking_evidence\":null,\"headline\":\"dust is borne condition, not mere place\",\"reader_payoff\":\"The reader understands dust-poverty as sufficient visible evidence of need without needing a named location, owner, or cause.\",\"reason\":\"The grammar makes the noun a possessed condition through the construct rather than a locative prepositional phrase or an external circumstance.\",\"representative_source_ids\":[\"QG-07e20577\",\"QG-b2ae0e72\",\"QS-d1a3bb3c\",\"QT-9c6bb5bd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:2:open-singular-durable-person","source_type":"word_analysis","support_id":"sup_4c24dc65782e12534a1d","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite singular makes need open and concrete\",\"reader_payoff\":\"The reader meets any such needy person, but as one concrete individual rather than an administrative class.\",\"reason\":\"The local form is indefinite singular and adjectival/substantive; the contextual profile treats the form as human-generic, supporting an open but personal recipient.\",\"representative_source_ids\":[\"MG-02875031\",\"QF-6c42eb2a\",\"QF-7968d8f8\",\"QF-b2653534\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:3:characterization-not-property","source_type":"word_analysis","support_id":"sup_59a0acd9b24f366901d5","text":"{\"blocking_evidence\":null,\"headline\":\"possession means characterized by dust-poverty\",\"reader_payoff\":\"The reader understands the construction as a visible attached condition, not literal ownership of dust.\",\"reason\":\"V4 separates possessor/characterization from relative-pronoun and demonstrative branches; the abstract genitive makes characterization the local branch rather than literal property.\",\"representative_source_ids\":[\"QG-c288746c\",\"QS-c6e29ccd\",\"QS-dc7a7b8f\",\"MS-919f0212\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:4:marked-rare-final-noun","source_type":"word_analysis","support_id":"sup_5c3917e92a81f16b3bb2","text":"{\"blocking_evidence\":null,\"headline\":\"marked noun carries the memorable final image\",\"reader_payoff\":\"The reader treats the final dust-poverty noun as a marked image that must carry force locally, not as routine vocabulary.\",\"reason\":\"Contextual evidence marks the local abstract noun as low-occurrence, and the CRITICAL rows press its rarity and terminal position as part of the payoff.\",\"representative_source_ids\":[\"MP-74e23397\",\"QH-b730c278\",\"MH-4971fa15\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:3:phrase-hinge","source_type":"word_analysis","support_id":"sup_5d0cfbdba172bf850020","text":"{\"blocking_evidence\":null,\"headline\":\"central hinge converts person and dust into one identity\",\"reader_payoff\":\"The reader feels the word's position between person and dust as the grammatical hinge that makes them one recipient description.\",\"reason\":\"The word sits between {{ar:مِسْكِينًۭا}} ({{tr:miskīnan}}) and {{ar:مَتْرَبَةٍۢ}} ({{tr:matrabatin}}); no conjunction separates the condition from the person.\",\"representative_source_ids\":[\"QI-b0ffa98e\",\"QT-049f6bc3\",\"QT-6c60a761\",\"QP-ca6801aa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:2:settled-need-and-provision","source_type":"word_analysis","support_id":"sup_5d7ea825115a468903a1","text":"{\"blocking_evidence\":null,\"headline\":\"settlement and lodging fields make need feel established\",\"reader_payoff\":\"The reader sees the need as settled and requiring provision, not as a passing shortage.\",\"reason\":\"Dwelling, tranquility, and provision branches are not the local lexical sense, but they support the CRITICAL pressure that this poverty is settled and answered by feeding.\",\"representative_source_ids\":[\"QS-0b5e0f30\",\"QS-595c1308\",\"QS-9203f8e3\",\"QS-eaed8ab0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:2:recipient-sequence-shift","source_type":"word_analysis","support_id":"sup_5eeecd344ad622899911","text":"{\"blocking_evidence\":null,\"headline\":\"recipient pair shifts from kin-loss to material deprivation\",\"reader_payoff\":\"The reader follows the feeding test as it widens from a near orphan in 90:15 to material deprivation in 90:16.\",\"reason\":\"The CRITICAL rows explicitly pair the prior recipient in 90:15 with the current one, and the local grammar keeps both under the same feeding sequence.\",\"representative_source_ids\":[\"MI-5966a003\",\"QE-f4ab7910\",\"ME-8c9a6867\",\"QB-3db5ee16\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:4:abstract-qualifier-chain","source_type":"word_analysis","support_id":"sup_6d1c4a42177882f9431c","text":"{\"blocking_evidence\":null,\"headline\":\"third abstract qualifier completes the feeding chain\",\"reader_payoff\":\"The reader hears the chain of famine, nearness, and dust reach its terminal dust endpoint across 90:14-16.\",\"reason\":\"The rows explicitly link {{ar:مَسْغَبَةٍ}} ({{tr:masghabatin}}), {{ar:مَقْرَبَةٍ}} ({{tr:maqrabatin}}), and {{ar:مَتْرَبَةٍۢ}} ({{tr:matrabatin}}) as a sound and abstract-condition chain.\",\"representative_source_ids\":[\"QE-5a90b49a\",\"QP-2f04d57a\",\"QP-b5b03055\",\"QY-53a676ac\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:4:embodied-lowered-deprivation","source_type":"word_analysis","support_id":"sup_71965e3769f01b5baed6","text":"{\"blocking_evidence\":null,\"headline\":\"dust image makes deprivation spatial and tactile\",\"reader_payoff\":\"The reader feels need as lowered exposure at ground level, not as an invisible account state.\",\"reason\":\"Concrete dust and dust-covered derivational pressure survive as image-pressure for the selected poverty condition without activating all root branches.\",\"representative_source_ids\":[\"QS-2a48f318\",\"QS-4f62299f\",\"QS-a76ce4bb\",\"QS-b976c68a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:4:selected-dust-poverty","source_type":"word_analysis","support_id":"sup_74f6e8fc1943a309906e","text":"{\"blocking_evidence\":null,\"headline\":\"dust-poverty selected from the concrete dust field\",\"reader_payoff\":\"The reader sees poverty as earth-contact and social lowering, while local grammar blocks neutral soil or unrelated root branches as the selected sense.\",\"reason\":\"V4 accepts both dust/soil and poverty-as-clinging-to-dust branches; the needy-person frame selects dust-poverty while retaining the concrete earth image.\",\"representative_source_ids\":[\"QS-1ee532be\",\"QS-5368d172\",\"QS-f615d348\",\"MS-bc031f94\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:2:qualified-by-dust-phrase","source_type":"word_analysis","support_id":"sup_767a1bf68f9d33cb7a39","text":"{\"blocking_evidence\":null,\"headline\":\"alternative covers the whole dust-qualified recipient\",\"reader_payoff\":\"The reader sees that the second option is not generic poverty but the needy person specifically fastened to dust-level exposure.\",\"reason\":\"Attachment evidence marks {{ar:ذَا}} ({{tr:dhā}}) as the adjectival qualifier of {{ar:مِسْكِينًۭا}} ({{tr:miskīnan}}) and {{ar:مَتْرَبَةٍۢ}} ({{tr:matrabatin}}) as the genitive complement.\",\"representative_source_ids\":[\"QG-2cd0e1f1\",\"QG-e27c33b3\",\"QG-e33e48fc\",\"MT-b91e6cbe\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:1:widening-without-collapse","source_type":"word_analysis","support_id":"sup_80a0af6936531fe24648","text":"{\"blocking_evidence\":null,\"headline\":\"real alternative widens the duty without merging recipients\",\"reader_payoff\":\"The reader sees the needy person and the prior orphan as distinct eligible beneficiaries under one act of feeding.\",\"reason\":\"The particle marks coordination and alternation; nothing in the guardrail evidence makes the current recipient an apposition or restatement of the previous one.\",\"representative_source_ids\":[\"QS-c812e14d\",\"QI-5e5fae0a\",\"MT-d62a7e28\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:4:rough-cadence-closure","source_type":"word_analysis","support_id":"sup_89b02d2ca2de0777c223","text":"{\"blocking_evidence\":null,\"headline\":\"rough terminal cadence reinforces dust exposure\",\"reader_payoff\":\"The reader hears person and condition bound by cadence while the final consonants make the dust endpoint feel rough.\",\"reason\":\"The sound rows point to tanwīn pairing and the terminal consonant texture; this supports the audible closure without altering the local meaning.\",\"representative_source_ids\":[\"QP-05847602\",\"QP-27170467\",\"QP-ec4ec773\",\"QP-fe17cd00\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:3:identity-state-convergence","source_type":"word_analysis","support_id":"sup_8bd474c2951a19374e17","text":"{\"blocking_evidence\":null,\"headline\":\"classification and state both intensify one recipient\",\"reader_payoff\":\"The reader sees the phrase as both identifying the kind of needy person and depicting the state in which he is encountered.\",\"reason\":\"The naʿt and ḥāl possibilities remain bound to the same recipient; they enrich the local phrase without multiplying referents.\",\"representative_source_ids\":[\"QG-e8981a31\",\"QS-03b69fd5\",\"QS-60b877fc\",\"QS-cfd13d31\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:4:genitive-construct-complement","source_type":"word_analysis","support_id":"sup_911810c0db479d53f759","text":"{\"blocking_evidence\":null,\"headline\":\"genitive dust-condition completes the construct\",\"reader_payoff\":\"The reader sees the final noun as the governed condition inside one recipient chain: action, person, qualifier, condition.\",\"reason\":\"QAC marks the word as genitive, and attachment evidence makes it the complement governed by {{ar:ذَا}} ({{tr:dhā}}).\",\"representative_source_ids\":[\"QG-538ed83f\",\"QG-54c98953\",\"QG-772256ad\",\"MG-616bfc74\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:2:soft-need-to-dust-closure","source_type":"word_analysis","support_id":"sup_9ac460f9d569a68e47a0","text":"{\"blocking_evidence\":null,\"headline\":\"sound moves from subdued need to harder dust\",\"reader_payoff\":\"The reader hears a formal and sonic movement from the recipient noun toward the rougher dust ending.\",\"reason\":\"The rows compare the recipient forms and describe the movement from the softer sound of {{ar:مِسْكِينًۭا}} ({{tr:miskīnan}}) toward the harder closure of {{ar:مَتْرَبَةٍۢ}} ({{tr:matrabatin}}).\",\"representative_source_ids\":[\"QE-c567a942\",\"QP-8352be27\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:3:construct-binding","source_type":"word_analysis","support_id":"sup_9f88e2438f647c04bd68","text":"{\"blocking_evidence\":null,\"headline\":\"construct head binds the dust complement\",\"reader_payoff\":\"The reader sees the dust-condition as grammatically fastened to the needy person through the construct, not floating as another object.\",\"reason\":\"QAC and attachment evidence show {{ar:ذَا}} ({{tr:dhā}}) agreeing with the accusative needy person and governing {{ar:مَتْرَبَةٍۢ}} ({{tr:matrabatin}}) as genitive complement.\",\"representative_source_ids\":[\"QG-0cff4813\",\"QG-4f534ab9\",\"QF-730be8d6\",\"MG-48cefbd9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:3:delayed-genitive-bridge","source_type":"word_analysis","support_id":"sup_a42731e85c722d9fd64b","text":"{\"blocking_evidence\":null,\"headline\":\"construct bridge delays the final dust noun\",\"reader_payoff\":\"The reader passes through characterization before the phrase lands on dust-poverty.\",\"reason\":\"The construct requires the following genitive, so connected recitation and syntax carry the listener from the person through {{ar:ذَا}} ({{tr:dhā}}) to the final condition.\",\"representative_source_ids\":[\"MT-3d8c0067\",\"QP-2422600e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:3","source_type":"word_analysis","support_id":"sup_a8fd36f74819c316ed76","text":"{\"gloss_range\":\"accusative five-noun construct meaning one characterized by or bearing the following dust-poverty condition as a qualifier of the needy person\",\"prose\":\"{{ar:ذَا}} ({{tr:dhā}}) is the compact hinge that makes the needy person one characterized by a condition. It agrees with {{ar:مِسْكِينًۭا}} ({{tr:miskīnan}}) as an accusative qualifier and governs {{ar:مَتْرَبَةٍۢ}} ({{tr:matrabatin}}) as the genitive complement, so dust-poverty is grammatically borne by the recipient rather than added as a separate topic. The phrase can classify the kind of needy person or depict the state in which he is encountered, but both readings intensify the same recipient. The local branch of {{ar:ذ و و}} ({{tr:dh-w-w}}) is characterized-by possession, not relative-pronoun or demonstrative use, and not literal ownership of dust. Its small five-noun form keeps the phrase light while carrying singular focus, agreement, and construct dependency, and the construct makes the listener pass through characterization before landing on dust. The repeated frame from {{ar:ذَا مَقْرَبَةٍ}} ({{tr:dhā maqrabatin}}) in 90:15 returns with dust instead of nearness, making kinship and exposed poverty parallel claims on the same feeding act. The frame also looks back to the hunger-day condition in 90:14, shifting the skeleton from circumstance to fed person across 90:14-16.\",\"root_display\":\"{{ar:ذ و و}} ({{tr:dh-w-w}})\",\"root_gloss_range\":\"root range includes possessor or characterized-by forms, relative-pronoun uses, demonstrative uses, and interrogative-relative constructions; the local construct selects characterization by an attached genitive condition\",\"surface_display\":\"{{ar:ذَا}} ({{tr:dhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:1:matched-recipient-cadence","source_type":"word_analysis","support_id":"sup_aa1d75a7cc7535036eef","text":"{\"blocking_evidence\":null,\"headline\":\"short particle resets into a matched recipient\",\"reader_payoff\":\"The reader can hear the quick reset into a second accusative recipient whose sound-form answers the prior one.\",\"reason\":\"The rows point to the clipped particle and the matched accusative recipient cadence across 90:15-16; this supports an audible pairing without changing the grammar.\",\"representative_source_ids\":[\"QE-5424832a\",\"QE-931b8629\",\"QP-b89c7af8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"90:16:2:1","source_type":"qac_morpheme","support_id":"sup_b3974b4f141a9e439ad8","text":"{\"lemma_ar\":\"مِسْكِين\",\"morph_features\":\"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|INDEF|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"90:16:2:1\",\"qac_word_ref\":\"90:16:2\",\"root_ar\":\"س ك ن\",\"surface_ar\":\"مِسْكِينًا\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:2","source_type":"word_analysis","support_id":"sup_bb093e352ef3a6e943d3","text":"{\"gloss_range\":\"an indefinite singular needy person as the accusative fed recipient, locally specified by dust-level exposure and colored by stilled-capacity pressure\",\"prose\":\"{{ar:مِسْكِينًۭا}} ({{tr:miskīnan}}) names the second recipient of the same feeding sequence, with its accusative form reaching back to the earlier act rather than starting a detached poverty statement. The indefinite singular keeps the claim open to any such person while forcing the scene to face one concrete beneficiary. The local sense from {{ar:س ك ن}} ({{tr:s-k-n}}) is poverty, yet the stillness, settlement, and lodging fields make that poverty feel like capacity arrested, need settled into place, and a condition requiring external provision. The following {{ar:ذَا مَتْرَبَةٍ}} ({{tr:dhā matrabatin}}) sharpens the noun further, so the alternative is not generic charity but a human recipient visibly marked by dust-level deprivation. The phrase first lets the person be heard before the condition, and the tanwīn cadence binds the softened needy-person sound to the rougher dust closure. Across the boundary, the feeding test moves from {{ar:يَتِيمًا}} ({{tr:yatīman}}) in 90:15 to this needy person, widening vulnerability from lost protection to material deprivation; the 18:79 contrast keeps need from being equated with total loss of agency.\",\"root_display\":\"{{ar:س ك ن}} ({{tr:s-k-n}})\",\"root_gloss_range\":\"broad root range around stillness, dwelling, tranquility, provision that enables staying, and poverty or abasement; the local frame selects needy-person poverty while retaining arrested and settled need as pressure\",\"surface_display\":\"{{ar:مِسْكِينًۭا}} ({{tr:miskīnan}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:3:compact-five-noun-form","source_type":"word_analysis","support_id":"sup_bcbea1c847a559514fe1","text":"{\"blocking_evidence\":null,\"headline\":\"small five-noun form carries agreement and dependency\",\"reader_payoff\":\"The reader notices how a very small form carries singular focus, accusative agreement, and construct dependency at once.\",\"reason\":\"The five-noun form is accusative singular and structurally compact, matching the local role as a light hinge between person and condition.\",\"representative_source_ids\":[\"QF-946f09d3\",\"QF-e09367a7\",\"QF-ea2eb6a1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:2:stilled-capacity-pressure","source_type":"word_analysis","support_id":"sup_bd8eb6e98c0f0d73398c","text":"{\"blocking_evidence\":null,\"headline\":\"poverty sense carries arrested-capacity pressure\",\"reader_payoff\":\"The reader feels the poverty as capacity stilled by need, while the local feeding frame keeps the selected sense as needy person.\",\"reason\":\"V4 preserves stillness and poverty branches for {{ar:س ك ن}} ({{tr:s-k-n}}); the local object frame selects poverty, while the stillness field survives as image-pressure.\",\"representative_source_ids\":[\"QS-1ce598b8\",\"QS-a73edb1e\",\"MS-35e198d6\",\"QY-e5eb47d5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:3:repeated-possessor-frame","source_type":"word_analysis","support_id":"sup_c116fad4f3b3825fd15f","text":"{\"blocking_evidence\":null,\"headline\":\"same possessor frame changes the attached claim\",\"reader_payoff\":\"The reader sees nearness in 90:15 and dust-poverty in 90:16 as parallel claims on feeding.\",\"reason\":\"The rows explicitly compare {{ar:ذَا مَقْرَبَةٍ}} ({{tr:dhā maqrabatin}}) in 90:15 with {{ar:ذَا مَتْرَبَةٍ}} ({{tr:dhā matrabatin}}) in 90:16.\",\"representative_source_ids\":[\"MI-59e96cf0\",\"MT-da531ef4\",\"QE-71c6745c\",\"ME-fcdb331d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:4","source_type":"word_analysis","support_id":"sup_cc00e8ad5deb496c4880","text":"{\"gloss_range\":\"an indefinite genitive abstract noun naming dust-poverty as the condition borne by the needy person; locally poverty as earth-contact rather than neutral soil or remote root branches\",\"prose\":\"{{ar:مَتْرَبَةٍۢ}} ({{tr:matrabatin}}) completes the construct of {{ar:ذَا}} ({{tr:dhā}}) as a genitive condition, so the ayah ends by fastening dust-poverty to the needy person. The noun does not merely locate someone in dust; it makes dust-level deprivation the condition by which the recipient is recognized. The local branch of {{ar:ت ر ب}} ({{tr:t-r-b}}) is poverty visible as earth-contact, not neutral soil, wealth, age-peers, or other remote branches, but the concrete dust field remains forceful: deprivation becomes spatial, tactile, and lowered to ground level. Even the narrowed body-register pressure stays secondary to the local sense while making the deprivation feel carried on the body. Its indefinite abstract form turns dust into a recognizable state that can mark any exposed recipient. As the terminal word, it answers {{ar:مَقْرَبَةٍ}} ({{tr:maqrabatin}}) in 90:15 and joins the 90:14-16 chain of {{ar:مَسْغَبَةٍ}} ({{tr:masghabatin}}), {{ar:مَقْرَبَةٍ}} ({{tr:maqrabatin}}), and {{ar:مَتْرَبَةٍۢ}} ({{tr:matrabatin}}). The rare final noun, tanwīn pairing, and rough terminal consonants make the feeding test land on visible exposure rather than routine vocabulary; 30:20 uses dust for human origin, while 90:16 turns dust into social responsibility.\",\"root_display\":\"{{ar:ت ر ب}} ({{tr:t-r-b}})\",\"root_gloss_range\":\"root range includes soil and dust, poverty as clinging to dust, wealth by dust-like abundance, equal-age companionship, body and fingertip terms, plant/place names, and other remote branches; the local construct selects dust-poverty while retaining concrete earth-contact pressure\",\"surface_display\":\"{{ar:مَتْرَبَةٍۢ}} ({{tr:matrabatin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:4:remote-body-register","source_type":"word_analysis","support_id":"sup_da8ad9e24aab8b3d67e1","text":"{\"blocking_evidence\":null,\"headline\":\"body-register remains secondary image pressure\",\"reader_payoff\":\"The reader may feel deprivation carried on the body, while the local word still means dust-poverty rather than an anatomical term.\",\"reason\":\"The breastbone or upper-chest branch is a remote dictionary branch; it can support embodied pressure only after being narrowed away from the local lexical sense.\",\"representative_source_ids\":[\"QS-b7ad89e0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:1:continuing-alternative-object","source_type":"word_analysis","support_id":"sup_e1f5941033bc34c46ef6","text":"{\"blocking_evidence\":null,\"headline\":\"alternative particle keeps the feeding frame open\",\"reader_payoff\":\"The reader notices that the ayah opens as a continuation of the prior feeding object list, not as a new command or detached phrase.\",\"reason\":\"QAC identifies the word as a coordinating conjunction, and attachment support ties the current accusative recipient back to the feeding sequence from 90:14-15.\",\"representative_source_ids\":[\"QG-1d85e7e2\",\"QG-46a91ec2\",\"MG-f3f86018\",\"QT-c5181c54\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:1:boundary-launch","source_type":"word_analysis","support_id":"sup_e2f8c9fb98678e6874f8","text":"{\"blocking_evidence\":null,\"headline\":\"opening position bridges back before the noun appears\",\"reader_payoff\":\"The reader hears continuation before hearing the recipient, so the ayah boundary itself becomes part of the list structure.\",\"reason\":\"The first word is the alternative marker, so the syntax announces a second list member before {{ar:مِسْكِينًۭا}} ({{tr:miskīnan}}) is named.\",\"representative_source_ids\":[\"QT-1b02d7d7\",\"QT-67fb8031\",\"QB-f3dad49b\",\"QY-d9805d49\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:1","source_type":"word_analysis","support_id":"sup_f700eff8246ca2cc1c60","text":"{\"gloss_range\":\"coordinating alternative particle that carries the prior feeding frame into a second recipient option without starting a new command\",\"prose\":\"{{ar:أَوْ}} ({{tr:aw}}) opens 90:16 by carrying the earlier feeding frame forward. Before the new recipient is named, the listener already knows that another object is being coordinated with {{ar:يَتِيمًا ذَا مَقْرَبَةٍ}} ({{tr:yatīman dhā maqrabatin}}) in 90:15. The particle therefore widens the steep-path deed without repeating the act: the feeder must recognize either the near orphan or {{ar:مِسْكِينًۭا}} ({{tr:miskīnan}}) as a valid recipient. It also prevents the two recipients from collapsing into one description; the clipped opening makes the second claim arrive quickly as the matched answer across the ayah boundary.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:أَوْ}} ({{tr:aw}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:16:4:nearness-to-dust-echo","source_type":"word_analysis","support_id":"sup_fc5061c17234a40e439f","text":"{\"blocking_evidence\":null,\"headline\":\"nearness is answered by dust across the boundary\",\"reader_payoff\":\"The reader hears 90:15 nearness and 90:16 dust-poverty as formally balanced but socially different grounds for feeding.\",\"reason\":\"The rows compare {{ar:مَقْرَبَةٍ}} ({{tr:maqrabatin}}) in 90:15 with {{ar:مَتْرَبَةٍۢ}} ({{tr:matrabatin}}) in 90:16, preserving the frame while shifting the claim.\",\"representative_source_ids\":[\"QE-0f190af8\",\"QE-7c076eca\",\"QB-06c0d99e\",\"QB-f42c6976\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"أَوْ مِسْكِينًۭا ذَا مَتْرَبَةٍۢ","ayah_ref":"90:16"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000178/B002","root_000726/B006"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_000726","role":"Poverty and humble abasement supply the person's condition of need and lowered social power.","root":"س ك ن","source_ref":"90:16","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000178","role":"Poverty figured as clinging to dust materializes abasement as ground-contact.","root":"ت ر ب","source_ref":"90:16","source_word_indices":["4"]}],"changed_reading":{"after":"A person whose need has lowered and ground-bound them, so poverty is encountered as an embodied relation to dust.","before":"A poor person in severe poverty."},"confidence":"strong","focus_anchor":"The two rooted terms in مِسْكِينًا ذَا مَتْرَبَةٍ converge on need, but the second gives the first a bodily location.","mechanism":"The س ك ن branch supplies poverty, weakness, and abasement, while the ت ر ب branch turns need into clinging contact with dust. The phrase therefore intensifies rather than merely repeats: a social condition acquires posture and material texture.","model_id":"b01_doubled_destitution_ground_contact"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b01_doubled_destitution_ground_contact","source_type":"hft","support_id":"sup_5f93873b9ef4550e8a28","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَوْ مِسْكِينًۭا ذَا مَتْرَبَةٍۢ","ayah_ref":"90:16"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000178/B001","root_000726/B002","root_000726/B004"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000726","role":"Dwelling and settlement supply the absent norm against which the person's location is read.","root":"س ك ن","source_ref":"90:16","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_000726","role":"An object or place of rest makes lodging and comfort the function that bare earth has failed to provide.","root":"س ك ن","source_ref":"90:16","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000178","role":"Soil, earth, and dust supply the exposed surface that has become the person's only resting place.","root":"ت ر ب","source_ref":"90:16","source_word_indices":["4"]}],"changed_reading":{"after":"An unhoused person for whom bare earth has become lodging and bed.","before":"A destitute person associated with dust."},"confidence":"medium","focus_anchor":"مِسْكِينًا retains latent س ك ن images of dwelling and rest beside مَتْرَبَةٍ as bare earth.","mechanism":"Dwelling and familiar rest remain audible behind the noun, but the only place supplied by its modifier is soil. The construction can thus stage failed architecture: habitation has collapsed to the ground itself.","model_id":"b02_dwelling_collapsed_to_earth"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b02_dwelling_collapsed_to_earth","source_type":"hft","support_id":"sup_6c7bebbe0510e7ee6c6a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَوْ مِسْكِينًۭا ذَا مَتْرَبَةٍۢ","ayah_ref":"90:16"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000178/B002","root_000726/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000726","role":"Cessation after movement supplies the arrest or inability to continue.","root":"س ك ن","source_ref":"90:16","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000178","role":"Clinging to dust gives that arrested condition a downward, adhesive force.","root":"ت ر ب","source_ref":"90:16","source_word_indices":["4"]}],"changed_reading":{"after":"A person whose poverty has stopped movement and narrowed the possibility of leaving the condition.","before":"A static label for an impoverished person."},"confidence":"medium","focus_anchor":"The cessation image in س ك ن and the clinging image in ت ر ب meet inside the focus construction.","mechanism":"Need appears as a loss of practical motion: one root removes movement and the other adheres the person to the ground. The noun is therefore not only a rank on an economic scale but a condition of constrained exit.","model_id":"b03_need_as_arrested_motion"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b03_need_as_arrested_motion","source_type":"hft","support_id":"sup_c0ee4e992d753eb99c0b","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَوْ مِسْكِينًۭا ذَا مَتْرَبَةٍۢ","ayah_ref":"90:16"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000178/B002","root_000178/B003"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000178","role":"Dust-clinging poverty supplies the actual possession named by the construction.","root":"ت ر ب","source_ref":"90:16","source_word_indices":["4"]},{"branch_id":"B003","mapped_root_id":"root_000178","role":"Wealth imagined as dust-like abundance supplies an excluded opposite and makes the possession of dust ironic.","root":"ت ر ب","source_ref":"90:16","source_word_indices":["4"]}],"changed_reading":{"after":"An ironic possessor whose only abundance is dust, with wealth present as the root's unavailable shadow.","before":"A person characterized by destitution."},"confidence":"exploratory","focus_anchor":"The ذَا construction marks possession while ت ر ب contains opposed branches of dust-bound poverty and dust-like abundance.","mechanism":"The phrase can carry a bitter internal reversal: the person is grammatically a possessor, yet what is possessed is dust. The same root's wealth branch remains as the excluded opposite, making the dust feel like a grotesque abundance.","model_id":"b04_possessor_without_possession"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b04_possessor_without_possession","source_type":"hft","support_id":"sup_49916f564214d41f785d","trust":"legacy_unbound"}]}
</lane_packet_json>
