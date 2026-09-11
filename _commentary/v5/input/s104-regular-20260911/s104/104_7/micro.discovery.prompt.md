# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **104:7**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s104-regular-20260911/s104/104_7/micro.discovery.json` and modify nothing
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
  "ayah_ref": "104:7",
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
{"analysis_context":{"analysis_id":"s104-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"104:7","host_surah":104,"lane_context_refs":[],"ordered_context_refs":["104:0","104:1","104:2","104:3","104:4","104:5","104:6","104:8","104:9","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, gök varlıkları ile tanın doğuşuna bağlıdır; bir insanın belirmesini, bitkinin çıkmasını veya bir işe erişme yolunu kapsamaz.","branch_kind":"collocation","branch_ref":"root_000945/B001","candidate_links":[{"candidate_id":"cand_e1df5c3a8a59383c8023","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طَّلَعَ","morph_features":"STEM|POS:V|IMPF|(VIII)|LEM:T~alaEa|ROOT:TlE|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"104:7:2:1","qac_word_ref":"104:7:2","surface_ar":"تَطَّلِعُ"}],"gloss":"güneşin, ayın, yıldızın veya tanın doğması; doğuş olayı ve yeri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Güneş, ay ve yıldız gibi ışık veren gök varlıkları görünür duruma gelerek doğar."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tan yerinin aydınlanıp belirmesi de aynı doğuş olayı içinde anlatılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı ad, kaynaklardaki biçim ayrımına göre doğuş olayını veya doğuş yerini gösterebilir."}}],"root_ar":"ط ل ع","root_id":"root_000945","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gök varlığının ya da tanın belirmesi ile bu doğuşun olayı veya yeri birlikte anlatılmak istendiğinde kullanılır.","boundary_detail":"Dal, gök varlıkları ile tanın doğuşuna bağlıdır; bir insanın belirmesini, bitkinin çıkmasını veya bir işe erişme yolunu kapsamaz.","branch_image_ar":"طلوع النير وموضعه","concept_gloss":"güneşin, ayın, yıldızın veya tanın doğması; doğuş olayı ve yeri","contextual_glosses":[{"applicability":"Özne güneş olduğunda doğuş olayını doğal bir cümle içinde karşılar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ay, yıldız ve tan kapsamı ile doğuş yeri anlamını dışarıda bırakır.","preserves":"Güneşin görünür duruma gelmesi olayını korur."},"facet_ids":["F001"],"text":"güneş doğdu","usage_role":"contextual"}],"definition":"Güneşin, ayın, yıldızın veya tanın görünür duruma gelerek doğmasıdır; aynı ad doğuş olayını ve doğuşun gerçekleştiği yeri de gösterebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Güneş, ay ve yıldız gibi ışık veren gök varlıkları görünür duruma gelerek doğar."},{"facet_id":"F002","role":"extension","statement":"Tan yerinin aydınlanıp belirmesi de aynı doğuş olayı içinde anlatılır."},{"facet_id":"F003","role":"source_variant","statement":"Aynı ad, kaynaklardaki biçim ayrımına göre doğuş olayını veya doğuş yerini gösterebilir."}],"identity_rationale":"Kaynak sözü, güneşin yanı sıra tanın, yıldızın ve ayın doğmasını; ayrıca bu doğuşun kendisini ve gerçekleştiği yeri aynı dalda açıkça toplar. Bu nedenle dalın ışık veren gök varlıklarının belirmesi ve doğuş yeri biçimindeki çerçevesi kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"güneşin, tanın, yıldızın ya da ayın doğması"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"güneşin doğduğu yer veya yön"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"tanın sökmesi; tan vakti ya da tanın belirdiği yer"}],"lexicalization_note":"Anlam yalnızca verilen gök varlığı ve tan ifadelerine bağlı olarak tanımlanır; genel bir yükselme ya da görünme anlamına genişletilmez.","neighbor_coverage_note":"Verilen bütün komşular karşılaştırıldı; yalnızca doğma alanıyla doğrudan örtüşen ve doğuş-batış karşıtlığını belirginleştiren iki komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal doğan gök varlığına ve doğuşun olay ya da yer olmasına bağlıdır; komşu dal ise ışık yayma ile doğu yönünü bağımsız kapsam öğeleri yapar.","focus_only":"Bu dal tanı da kapsar ve doğuş olayının yanında doğuş yerini adlandırabilir.","gloss":"gök varlığının doğması","neighbor_only":"Komşu dal aydınlanmayı, doğu yönünü ve o yöne yönelmeyi ayrıca kapsar.","neighbor_ref":"root_000790/B001","relation_type":"near_synonym","shared_zone":"Her iki dal güneş, ay ve yıldızların görünür biçimde doğmasını anlatır."},{"boundary_match":"opposed","distinction":"Biri görünürlük başlangıcı olan doğuşu, öteki görünürlüğün sonu olan batışı gösterir.","focus_only":"Bu dal güneşin görünür duruma gelerek doğmasını anlatır.","gloss":"doğuş ve batış","neighbor_only":"Komşu dal güneşin batıya yönelip gözden kaybolmasını anlatır.","neighbor_ref":"root_000065/B007","relation_type":"antonym","shared_zone":"İki dal da güneşin günlük gökyüzü hareketindeki bir sınır olayını anlatır."}],"source_phrase_ar":"المطلع الموضع الذي تطلع عليه الشمس؛ والمطلع مصدر من طلع (ayn)؛ طلعت الشمس والكوكب طلوعا ومطلعا؛ والمطلع موضع طلوعها (sihah)؛ طلعت الشمس؛ وكذلك طلع الفجر والنجم والقمر؛ المطلع بالفتح هو الطلوع والمطلع بالكسر هو الموضع (tahdhib)؛ طلع الشمس طلوعا ومطلعا؛ والمطلع موضع الطلوع (mufradat)؛ أصل واحد صحيح يدل على ظهور وبروز؛ طلعت الشمس طلوعا ومطلعا؛ والمطلع موضع طلوعها (maqayis)","source_summary":"Aktarımlar güneşin, ayın, yıldızın ve tanın doğuşunda birleşir. Ayrıca aynı sözün hem doğma olayına hem de gök varlığının doğduğu yere uygulanabildiğini birlikte gösterir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه طلوع الشمس والفجر والنجم والقمر، والمطلع مصدرا أو موضعا أو وقتا للطلوع","what_is_not_ar":"لا يدخل فيه طلوع الشخص على القوم، ولا الطلع النباتي، ولا مطلع الأمر بمعنى مأتى الأمر"},"support_links":["sup_59bf448e19e2f7b95ddd"]},{"boundary":"Karşıya çıkma ve yanına gelme çekirdektir; gözden kaybolma yalnızca onu bildiren ayrı kuruluşun sınırlı karşıt okumasıdır.","branch_kind":"collocation","branch_ref":"root_000945/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَّلَعَ","morph_features":"STEM|POS:V|IMPF|(VIII)|LEM:T~alaEa|ROOT:TlE|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"104:7:2:1","qac_word_ref":"104:7:2","surface_ar":"تَطَّلِعُ"}],"gloss":"bir topluluğun karşısına çıkmak; ayrı kuruluşta onlardan gözden kaybolmak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi uzaktan gelip bir topluluğun karşısında görünür veya onların yanına varır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirme, beklenmedik bir geliş ya da baskın biçimini alabilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yön ilişkisi ters kurulduğunda kişiyi topluluktan ayrılıp görünmez olma sonucuyla anlatan bir aktarım da vardır."}}],"root_ar":"ط ل ع","root_id":"root_000945","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin topluluğa gelişi ve görünmesi ya da yön ilişkisi ters olduğunda onlardan ayrılıp kaybolması anlatılırken kullanılır.","boundary_detail":"Karşıya çıkma ve yanına gelme çekirdektir; gözden kaybolma yalnızca onu bildiren ayrı kuruluşun sınırlı karşıt okumasıdır.","branch_image_ar":"ظهور المقبل على القوم","concept_gloss":"bir topluluğun karşısına çıkmak; ayrı kuruluşta onlardan gözden kaybolmak","contextual_glosses":[{"applicability":"Bir kişinin topluluğa gelip beklenmedik biçimde görünmesi bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sıradan geliş ile topluluktan ayrılıp gözden kaybolma okumasını dışarıda bırakır.","preserves":"Topluluğa yönelen beklenmedik geliş ve görünmeyi korur."},"facet_ids":["F001","F002"],"text":"karşılarına birdenbire çıktı","usage_role":"contextual"}],"definition":"Bir kişinin bir topluluğun karşısına çıkması, yanına gelmesi veya birdenbire baskın verir gibi belirmesidir. Ayrı bir yön kuruluşunda ise topluluktan uzaklaşıp gözden kaybolma anlamı aktarılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi uzaktan gelip bir topluluğun karşısında görünür veya onların yanına varır."},{"facet_id":"F002","role":"specialization","statement":"Belirme, beklenmedik bir geliş ya da baskın biçimini alabilir."},{"facet_id":"F003","role":"source_variant","statement":"Yön ilişkisi ters kurulduğunda kişiyi topluluktan ayrılıp görünmez olma sonucuyla anlatan bir aktarım da vardır."}],"identity_rationale":"Kaynak sözü temel olarak bir kişinin topluluğun karşısına çıkmasını, yanına gelmesini veya baskın verircesine belirmesini destekler. Bunun yanında yön bildiren farklı kuruluşlarla gözden kaybolma aktarımı bulunduğundan, dal ancak yaklaşma ile uzaklaşma okumaları birbirine karıştırılmadan korunursa kullanılabilir.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"topluluğun karşısına çıkmak, yanına gelmek ya da baskın verircesine belirmek; sınırlı bir aktarımda gözden kaybolmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"onların yanından ayrılıp gözden kaybolmak"}],"lexicalization_note":"Anlam kişi ile topluluk arasındaki yön ilişkisini kuran ifadelerle sınırlıdır; genel gelme, görünme veya kaybolma anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; görünmenin beklenmedikliği ile genel varıştan ayrılan sınırı en iyi gösteren iki yakın komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kişi ile topluluk arasındaki yön kuruluşuna bağlıdır; komşu dalın çekirdeği ise öznenin bilinmeyen bir yerden beklenmedik biçimde ortaya çıkmasıdır.","focus_only":"Bu dal sıradan gelişi ve ayrı bir kuruluşta topluluktan kaybolmayı da kapsar.","gloss":"birdenbire ortaya çıkma","neighbor_only":"Komşu dal beklenmedikliği temel koşul yapar ve sel gibi insan dışı özneleri de kapsar.","neighbor_ref":"root_000467/B002","relation_type":"near_synonym","shared_zone":"Her iki dal bir kişinin ansızın görünmesini ve baskın verir gibi gelişini anlatabilir."},{"boundary_match":"partial","distinction":"Bu dal topluluğun görüş alanına çıkmayı öne çıkarır; komşu dal ise görünür olmayı gerektirmeyen genel varış ve ulaşma alanındadır.","focus_only":"Bu dal karşıda görünme, olası baskın ve ayrı kaybolma okumasını taşır.","gloss":"gelme ve varma","neighbor_only":"Komşu dal bir şeye varmayı ve özellikle su başına ulaşmayı daha geniş biçimde kapsar.","neighbor_ref":"root_001640/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir kişinin bir yere ya da topluluğa ulaşmasını anlatabilir."}],"source_phrase_ar":"طلع علينا فلان يطلع طلوعا إذا هجم (ayn)؛ طلعت على القوم إذا أتيتهم؛ طلعت عنهم إذا غبت عنهم (sihah)؛ يقال طلع فلان علينا من بعيد؛ طلعت على صاحبي إذا أقبلت عليه؛ طلعت على القوم إذا غبت عنهم حتى لا يروك (tahdhib)؛ وعنه استعير طلع علينا فلان واطلع؛ وطلعت عنه غبت (mufradat)؛ طلع علينا فلان إذا هجم (maqayis)","source_summary":"Ortak çizgi, kişinin topluluğa doğru gelip karşılarında görünmesidir; bazı anlatımlarda bu geliş baskın niteliği taşır. Aynı söz ailesi, ayrı bir yön kuruluşunda topluluktan uzaklaşıp gözden kaybolmayı da bildirir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه أن يطلع فلان على القوم أو علينا بمعنى يظهر أو يأتي أو يهجم، ومعه ضدية الغياب في بعض النقل","what_is_not_ar":"لا يدخل فيه طلوع الشمس، ولا الإشراف المعرفي على السر أو الأمر، ولا استطلاع رأي"},"support_links":[]},{"boundary":"Kişinin kendisinin öğrenmesi, başkasını bilgilendirmesi, bir nesneyi göstermesi ve görüş yoklaması ayrı alt kullanımlardır.","branch_kind":"collocation","branch_ref":"root_000945/B003","candidate_links":[{"candidate_id":"cand_ad302f8ba4c2b6a17cf3","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طَّلَعَ","morph_features":"STEM|POS:V|IMPF|(VIII)|LEM:T~alaEa|ROOT:TlE|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"104:7:2:1","qac_word_ref":"104:7:2","surface_ar":"تَطَّلِعُ"}],"gloss":"bir şeyi öğrenmek ya da başkasına gösterip bildirmek; görüşünü yoklamak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gözlemleyen kişi bir şeye yukarıdan bakar ya da iç yüzüne erişerek onu bütünüyle öğrenir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bilgiyi bilen kişi, bir işi veya saklı sözü başkasına göstererek onun da bilmesini sağlar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişinin başını dışarı çıkarıp görünür kılması, fiziksel gösterme alt kullanımını oluşturur."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Birinin ne düşündüğünü anlamak için görüşünü araştırmak, bilgi edinme işleminin özel bir uzantısıdır."}}],"root_ar":"ط ل ع","root_id":"root_000945","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir işin iç yüzüne erişme, onu başka bir kişiye açma veya birinin düşüncesini araştırma kuruluşlarında kullanılır.","boundary_detail":"Kişinin kendisinin öğrenmesi, başkasını bilgilendirmesi, bir nesneyi göstermesi ve görüş yoklaması ayrı alt kullanımlardır.","branch_image_ar":"الإشراف والكشف على الأمر","concept_gloss":"bir şeyi öğrenmek ya da başkasına gösterip bildirmek; görüşünü yoklamak","contextual_glosses":[{"applicability":"Kişinin bir işin iç yüzüne erişip onu öğrendiği bağlamda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkasına gösterme, başı görünür kılma ve görüş yoklama alt kullanımlarını dışarıda bırakır.","preserves":"Gözlemleyenin bir iş hakkında kapsamlı bilgi edinmesini korur."},"facet_ids":["F001"],"text":"konuyu bütün yönleriyle öğrendi","usage_role":"contextual"}],"definition":"Bir şeye bakarak onun iç yüzünü öğrenmek veya onu başkasına görünür ya da bilinir kılmaktır; birinin görüşünü araştırma ve başı dışarı çıkarıp gösterme de bu kuruluşlara bağlı özel işlemlerdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gözlemleyen kişi bir şeye yukarıdan bakar ya da iç yüzüne erişerek onu bütünüyle öğrenir."},{"facet_id":"F002","role":"core","statement":"Bilgiyi bilen kişi, bir işi veya saklı sözü başkasına göstererek onun da bilmesini sağlar."},{"facet_id":"F003","role":"specialization","statement":"Bir kişinin başını dışarı çıkarıp görünür kılması, fiziksel gösterme alt kullanımını oluşturur."},{"facet_id":"F004","role":"extension","statement":"Birinin ne düşündüğünü anlamak için görüşünü araştırmak, bilgi edinme işleminin özel bir uzantısıdır."}],"identity_rationale":"Kaynak sözü bakıp öğrenme, başkasına gösterip bildirme, başı görünür kılma ve birinin görüşünü yoklama işlemlerini aynı dalda verir. Bunlar tek bir katılımcı düzenine indirgenemeyeceği için dal, görünür veya bilinir kılma ortaklığı korunarak ve katılımcı değişimleri açıkça ayrılarak kabul edilebilir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bir şeye yukarıdan bakmak veya iç yüzünü bütünüyle öğrenmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"başkasına bir işi ya da saklı sözü gösterip bildirmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"başını dışarı çıkarıp görünür kılmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"birinin görüşünü öğrenmek için ne düşündüğünü araştırmak"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bir şeyi inceleyip içinde ne bulunduğunu öğrenmek"}],"lexicalization_note":"Tanım yalnızca verilen bakma, öğrenme, gösterme ve görüş yoklama kuruluşlarına bağlıdır; genel bilgi edinme ya da açıklama anlamına yayılmaz.","neighbor_coverage_note":"Bütün komşular incelendi; gizli bilgiye erişme ile soruşturma alanları, dalın öğrenme ve gösterme sınırlarını en açık biçimde ayırdığı için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın kuruluşları fiziksel gösterme ile görüş araştırmaya kadar uzanır; komşu dal ise gizli bilgiye erişme sınırına daha sıkı bağlıdır.","focus_only":"Bu dal başı göstermeyi, görüş yoklamayı ve açık bir şeyi incelemeyi de kapsar.","gloss":"gizliyi öğrenip bildirme","neighbor_only":"Komşu dal bilginin özellikle gizli olmasını ve gizliye birden erişme yönünü öne çıkarır.","neighbor_ref":"root_000982/B001","relation_type":"near_synonym","shared_zone":"Her iki dal saklı bir işi öğrenmeyi ve başkasının da öğrenmesini sağlamayı kapsar."},{"boundary_match":"partial","distinction":"Bu dal bakarak iç yüze erişme ve görünür kılma düzenindedir; komşu dalın çekirdeği soruşturma ve haber aramadır.","focus_only":"Bu dal öğrenilmiş şeyi başkasına gösterip bildirme ve başı görünür kılma işlemlerini içerir.","gloss":"bilgi edinme","neighbor_only":"Komşu dal soru sormayı, haber aramayı ve geniş çaplı araştırmayı temel işlem yapar.","neighbor_ref":"root_000085/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bilinmeyen bir iş hakkında bilgi edinmeye yönelebilir."}],"source_phrase_ar":"أطلع فلان رأسه أظهره؛ اطلع أشرف على الشيء؛ أطلع غيره إطلاعا؛ أطلعني طلع هذا الأمر حتى علمته كله؛ استطلعت رأيه (ayn)؛ اطلعت على باطن أمره؛ طالعت الشيء أي اطلعت عليه؛ أطلعتك على سري؛ استطلعت رأي فلان (sihah)؛ اطلع فلان إذا أشرف على شيء؛ أطلع غيره؛ استطلعت رأي فلان إذا نظرت ما رأيه؛ أطلعني فلان (tahdhib)؛ اطلع؛ أطلع الغيب؛ أطلعتك على كذا؛ واستطلعت رأيه (mufradat)؛ أطلعتك على الأمر إطلاعا؛ أطلعتك طلعه؛ استطلعت رأي فلان إذا نظرت ما الذي يبرز إليك منه (maqayis)","source_summary":"Aktarımlar bir şeyi gözleyip iç yüzünü öğrenme ile bilinen şeyi başkasına gösterip bildirme yönlerini birlikte verir. Başı görünür kılma, bir metni inceleme ve birinin görüşünü yoklama bu ortak görünürlük ve bilgi edinme düzeninin özel gerçekleşmeleridir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الاطلاع على الشيء أو باطن الأمر، وإظهار الرأس، وإطلاع غيرك على السر أو الأمر، واستطلاع الرأي","what_is_not_ar":"لا يدخل فيه الطليعة العسكرية إلا من جهة الاستكشاف، ولا طلوع النير، ولا الطلعة بمعنى هيئة الرؤية"},"support_links":["sup_98e597d3e35b9f3560e7"]},{"boundary":"Çekirdek, düşman hakkında bilgi toplamak üzere önden gönderilen kişi veya birliktir; genel gözetleme ya da sır öğrenme değildir.","branch_kind":"bare","branch_ref":"root_000945/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَّلَعَ","morph_features":"STEM|POS:V|IMPF|(VIII)|LEM:T~alaEa|ROOT:TlE|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"104:7:2:1","qac_word_ref":"104:7:2","surface_ar":"تَطَّلِعُ"}],"gloss":"düşmanı gözlemek için önden gönderilen gözcü veya gözcü birliği","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi, düşman hakkında bilgi toplamak için asker topluluğundan önce gönderilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı görevle gönderilen birden çok kişiden oluşan gözcü toplulukları da adlandırılır."}}],"root_ar":"ط ل ع","root_id":"root_000945","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Asker topluluğundan önce ilerleyip düşmanın durumunu öğrenen kişi ya da grup için kullanılır.","boundary_detail":"Çekirdek, düşman hakkında bilgi toplamak üzere önden gönderilen kişi veya birliktir; genel gözetleme ya da sır öğrenme değildir.","branch_image_ar":"طليعة تستكشف العدو","concept_gloss":"düşmanı gözlemek için önden gönderilen gözcü veya gözcü birliği","contextual_glosses":[{"applicability":"Birden çok kişinin düşmanı gözlemek üzere asker topluluğunun önüne yollandığı bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir gözcünün adlandırılması olasılığını dışarıda bırakır.","preserves":"Önden gönderilen gözcü grubunu ve bilgi toplama görevini korur."},"facet_ids":["F002"],"text":"önden gözcüler gönderildi","usage_role":"contextual"}],"definition":"Düşmanın yerini ve durumunu öğrenmek için asker topluluğunun önünden gönderilen gözcü kişi veya gözcü birliğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi, düşman hakkında bilgi toplamak için asker topluluğundan önce gönderilir."},{"facet_id":"F002","role":"extension","statement":"Aynı görevle gönderilen birden çok kişiden oluşan gözcü toplulukları da adlandırılır."}],"identity_rationale":"Kaynak sözü, düşmanın durumunu öğrenmek için asker topluluğunun önünden gönderilen kişi veya grupları doğrudan tanımlar. Dalın önden giden gözcü çerçevesi, görevi ve hedefiyle birlikte kaynak tarafından eksiksiz desteklenir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"düşmanı gözlemek için önden gönderilen gözcü kişi veya birlik"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"önden gönderilen gözcü toplulukları"}],"lexicalization_note":"Tanım bağımsız kişi ve grup adlarını kapsar; başka dallardaki genel bakma veya bilgi edinme kuruluşları buraya taşınmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; önden giden kişinin görevi ile kişiyi gönderme işlemi arasındaki iki temel sınırı gösteren komşular yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda önden gitmenin amacı düşmanı gözleyip bilgi toplamaktır; komşu dalda öncü konum daha belirleyicidir.","focus_only":"Bu dal düşmanın durumunu öğrenmek için gönderilme görevini açıkça kurar.","gloss":"önden giden gözcü","neighbor_only":"Komşu dal asker topluluğundan önce bulunmayı öne çıkarır, bilgi toplama işlemini zorunlu kılmaz.","neighbor_ref":"root_000138/B008","relation_type":"near_synonym","shared_zone":"Her iki dal asker topluluğundan önce ilerleyen kişi veya kişileri adlandırır."},{"boundary_match":"partial","distinction":"Bu dal görevli kişi ya da grubun adı, komşu dal ise bu kişileri gönderme işlemidir.","focus_only":"Bu dal görevi yapan gözcü kişi veya birliğin kendisini adlandırır.","gloss":"gözcü gönderme","neighbor_only":"Komşu dal gözcüleri başka bir topluluğun üzerine gönderme eylemini adlandırır.","neighbor_ref":"root_000517/B006","relation_type":"near_neighbor","shared_zone":"İki dal da karşı taraf hakkında bilgi toplamak üzere gözcü kullanımını içerir."}],"source_phrase_ar":"الطليعة قوم يبعثون ليطلعوا طلع العدو؛ الطلائع الجماعات في السرية (ayn)؛ طليعة الجيش من يبعث ليطلع طلع العدو (sihah)؛ طليعة القوم الذين يبعثون ليطلعوا طلع العدو (tahdhib)؛ وطليعة الجيش أول من يطلع (mufradat)؛ وطليعة الجيش من يطلع طلع العدو (maqayis)","source_summary":"Aktarımlar, düşmanın durumunu araştırmak için önden gönderilen kişi üzerinde birleşir. Tek kişi adı topluluk için de kullanılabilir; ayrı çoğul anlatım ise bu görevdeki gözcü gruplarını belirtir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الطليعة والطلائع الذين يبعثون لينظروا طلع العدو","what_is_not_ar":"لا يدخل فيه مطلق الاطلاع على السر أو الأمر، ولا طلوع الشمس، ولا الطلعة بمعنى الرؤية"},"support_links":[]},{"boundary":"Açılmamış palmiye çiçek salkımı bağımsız çekirdektir; ağacın onu vermesi ve ekinin belirmesi kuruluşlara bağlı olaylardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000945/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَّلَعَ","morph_features":"STEM|POS:V|IMPF|(VIII)|LEM:T~alaEa|ROOT:TlE|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"104:7:2:1","qac_word_ref":"104:7:2","surface_ar":"تَطَّلِعُ"}],"gloss":"palmiye ağacının kapalı çiçek salkımı; salkımın veya ekinin belirmesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Palmiye ağacının çiçek salkımı, kılıfı yarılmadan önceki kapalı durumuyla adlandırılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kapalı salkımın tek bir örneği için ayrı tekillik anlatımı bulunur."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Palmiye ağacının çiçek salkımını çıkarması, ürün adından türeyen olay kullanımını oluşturur."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Ekinin topraktan belirip görünmeye başlaması da bitkisel ortaya çıkış olarak anlatılır."}}],"root_ar":"ط ل ع","root_id":"root_000945","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kapalı palmiye çiçek salkımı adlandırılırken ya da ağacın salkım vermesi ve ekinin belirmesi anlatılırken kullanılır.","boundary_detail":"Açılmamış palmiye çiçek salkımı bağımsız çekirdektir; ağacın onu vermesi ve ekinin belirmesi kuruluşlara bağlı olaylardır.","branch_image_ar":"خروج الطلع والنبات","concept_gloss":"palmiye ağacının kapalı çiçek salkımı; salkımın veya ekinin belirmesi","contextual_glosses":[{"applicability":"Ekili bitkinin ilk sürgününün görünür duruma geldiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Palmiye çiçek salkımının adı ile ağacın bu salkımı vermesini dışarıda bırakır.","preserves":"Ekili bitkinin ilk kez görünür olmasını korur."},"facet_ids":["F004"],"text":"ekin topraktan belirdi","usage_role":"contextual"}],"definition":"Meyvesi yenilen palmiye ağacının henüz yarılmamış kılıf içindeki çiçek salkımıdır. Ayrı kuruluşlarda ağacın bu salkımı çıkarması ve ekinin topraktan belirip görünmesi anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Palmiye ağacının çiçek salkımı, kılıfı yarılmadan önceki kapalı durumuyla adlandırılır."},{"facet_id":"F002","role":"specialization","statement":"Kapalı salkımın tek bir örneği için ayrı tekillik anlatımı bulunur."},{"facet_id":"F003","role":"extension","statement":"Palmiye ağacının çiçek salkımını çıkarması, ürün adından türeyen olay kullanımını oluşturur."},{"facet_id":"F004","role":"extension","statement":"Ekinin topraktan belirip görünmeye başlaması da bitkisel ortaya çıkış olarak anlatılır."}],"identity_rationale":"Kaynak sözü, meyvesi yenilen palmiye ağacının açılmamış çiçek salkımını bağımsız bir ad olarak; ağacın bu salkımı vermesini ve ekinin belirmesini ise ayrı kuruluşlar olarak destekler. Dal korunabilir, ancak ürün adı ile bitkinin ortaya çıkma olayı tek bir yalın anlam gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"palmiye ağacının henüz açılmamış çiçek salkımı"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kılıf içindeki tek bir palmiye çiçek salkımı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"palmiye ağacının çiçek salkımını çıkarması"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"ekinin belirip görünmesi"}],"lexicalization_note":"Bağımsız salkım adı ile palmiye ağacının salkım vermesi ve ekinin belirmesi ayrı tutulur; olay kullanımları yalın ada yüklenmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel bitkisel çıkış ile önceki ürün sürerken yeni salkım verme koşulu, dalın iki önemli sınırını gösterdiği için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli palmiye ürünü ile ekinin belirmesine bağlıdır; komşu dal bitkide dışarı doğru çıkan bölümleri daha geniş biçimde anlatır.","focus_only":"Bu dal palmiye ağacının kapalı çiçek salkımını bağımsız olarak adlandırır.","gloss":"bitkinin baş vermesi","neighbor_only":"Komşu dal kök, yaprak, baş veya meyve gibi çok çeşitli bitki çıkıntılarını kapsar.","neighbor_ref":"root_000228/B004","relation_type":"near_synonym","shared_zone":"Her iki dal bitkinin ya da bir bölümünün görünür biçimde ortaya çıkmasını kapsar."},{"boundary_match":"partial","distinction":"Bu dal genel salkım verme olayıdır; komşu dal aynı olayı önceki ürünün hâlâ bulunması koşuluyla sınırlar.","focus_only":"Bu dal ilk ürünün kalıp kalmadığına bakmadan salkım çıkarmayı anlatır.","gloss":"yeni çiçek salkımı verme","neighbor_only":"Komşu dal yeni salkım çıkarken önceki ürünün ağaçta kalmasını zorunlu koşul yapar.","neighbor_ref":"root_001358/B006","relation_type":"near_synonym","shared_zone":"İki dal da palmiye ağacının yeni bir çiçek salkımı çıkarmasını anlatır."}],"source_phrase_ar":"الطلع طلع النخلة الواحدة طلعة؛ وأطلعت النخلة؛ وطلع الزرع بدا (ayn)؛ والطلع طلع النخلة؛ واطلع النخل إذا خرج طلعه (sihah)؛ طلع الزرع إذا بدا؛ وأطلعت النخلة إذا أخرجت طلعها؛ الطلع كفراها قبل أن تنشق (tahdhib)؛ تشبيها بالطلوع قيل طلع النخل؛ لها طلع نضيد؛ وقد أطلعت النخل (mufradat)؛ والطلع طلع النخلة؛ وقد أطلعت النخلة (maqayis)","source_summary":"Aktarımlar palmiye ağacının kapalı çiçek salkımını ve ağacın bu salkımı çıkarmasını birlikte verir. Ekinin ilk kez görünmesi de aynı görünür duruma gelme çizgisinde, fakat ayrı bir bitki kuruluşu olarak yer alır.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه طلع النخلة وطلعتها، وإطلاع النخل، وظهور الزرع إذا بدا","what_is_not_ar":"لا يدخل فيه طلوع الشمس، ولا الامتلاء، ولا الطلعة بمعنى رؤية الإنسان"},"support_links":[]},{"boundary":"Dağa yükselme çekirdektir; çıkış yolu, bir işe giriş yönü ve ürkütücü karşılaşma yalnızca verilen kuruluşlara bağlı uzantılardır.","branch_kind":"collocation","branch_ref":"root_000945/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَّلَعَ","morph_features":"STEM|POS:V|IMPF|(VIII)|LEM:T~alaEa|ROOT:TlE|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"104:7:2:1","qac_word_ref":"104:7:2","surface_ar":"تَطَّلِعُ"}],"gloss":"dağa çıkma ve çıkış yolu; bir işin yaklaşım yönü veya ürkütücü eşiği","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi dağın üst bölümüne doğru yükselerek çıkar."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dağa çıkılan yol, yükselme noktası veya dağa erişilen yön aynı adla gösterilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir işin kendisine yaklaşılacak yüzü veya giriş yolu, fiziksel erişimden soyutlanarak anlatılır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yüksek bir yerden aşağıya bakarken önünde açılan ağır ve ürkütücü durum özel bir kullanım oluşturur."}}],"root_ar":"ط ل ع","root_id":"root_000945","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dağa yükselme, dağa erişim yolu, bir işi ele alma yönü ya da yüksekten görülen ürkütücü karşılaşma anlatılırken kullanılır.","boundary_detail":"Dağa yükselme çekirdektir; çıkış yolu, bir işe giriş yönü ve ürkütücü karşılaşma yalnızca verilen kuruluşlara bağlı uzantılardır.","branch_image_ar":"مصعد ومأتى مشرف","concept_gloss":"dağa çıkma ve çıkış yolu; bir işin yaklaşım yönü veya ürkütücü eşiği","contextual_glosses":[{"applicability":"Bir kişinin dağın üstüne doğru yükseldiği fiziksel hareket bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çıkış yolu, bir işin yaklaşım yönü ve ürkütücü eşik anlamlarını dışarıda bırakır.","preserves":"Dağa doğru yükselerek çıkma hareketini korur."},"facet_ids":["F001"],"text":"dağa tırmanıp çıktı","usage_role":"contextual"}],"definition":"Dağa yükselip çıkmak veya dağa çıkılan erişim yoludur; buradan bir işin ele alınacağı yön ve yüksekten aşağıya bakıldığında karşılaşılan ürkütücü eşik anlamları gelişir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi dağın üst bölümüne doğru yükselerek çıkar."},{"facet_id":"F002","role":"extension","statement":"Dağa çıkılan yol, yükselme noktası veya dağa erişilen yön aynı adla gösterilir."},{"facet_id":"F003","role":"extension","statement":"Bir işin kendisine yaklaşılacak yüzü veya giriş yolu, fiziksel erişimden soyutlanarak anlatılır."},{"facet_id":"F004","role":"associated_use","statement":"Yüksek bir yerden aşağıya bakarken önünde açılan ağır ve ürkütücü durum özel bir kullanım oluşturur."}],"identity_rationale":"Kaynak sözü dağa çıkmayı, dağın çıkış ve erişim yolunu, bir işin yaklaşılabilir yönünü ve yüksekten aşağıya bakılan ürkütücü eşiği aynı kuruluş ailesinde verir. Dal korunabilir, ancak fiziksel çıkış, erişim noktası ve soyut yaklaşım yönü ayrı alt anlamlar olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"dağa tırmanıp çıkmak"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"dağa çıkılan yol veya dağa erişilen yön"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"bir işin ele alınacağı yön veya giriş yolu"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"yüksekten bakınca önünde açılan ağır durumun ürkütücülüğü"}],"lexicalization_note":"Tanım dağ, erişim yolu, işin yaklaşım yönü ve ürkütücü eşik kuruluşlarıyla sınırlıdır; genel yükselme anlamına yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yukarı çıkma alanı ve dağın alt bölümüyle kurulan karşıtlık, dalın yön ve erişim sınırlarını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal dağ ve erişim kuruluşlarına bağlıdır; komşu dal basamaklı yükselmeyi fiziksel ve soyut alanlarda daha genel biçimde kurar.","focus_only":"Bu dal dağın çıkış yolunu ve bir işin yaklaşım yönünü de adlandırır.","gloss":"yukarı çıkma","neighbor_only":"Komşu dal merdiven, gökyüzü ve bilgi basamaklarında aşamalı ilerlemeyi kapsar.","neighbor_ref":"root_000588/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bir kişinin dağa doğru yükselerek çıkmasını anlatabilir."},{"boundary_match":"opposed","distinction":"Bu dal yukarı yönelen çıkış ve üstten bakış kutbundadır; komşu dal dağın aşağıdaki taban ve etek kutbundadır.","focus_only":"Bu dal dağın üstüne yönelen çıkışı ve erişim yolunu anlatır.","gloss":"dağın çıkışı ve eteği","neighbor_only":"Komşu dal dağın altını, eteğini veya aşağı inen bölümünü adlandırır.","neighbor_ref":"root_000235/B014","relation_type":"polarity_pair","shared_zone":"İki dal da dağı düşey bölümleri ve ulaşım yönleri bakımından kavrar."}],"source_phrase_ar":"طلعت الجبل أي علوته؛ المطلع المأتى؛ موضع الإطلاع من إشراف إلى انحدار (sihah)؛ طلعت الجبل إذا علوته؛ المطلع موضع الاطلاع من إشراف إلى الانحدار؛ وقد يكون المطلع المصعد؛ مطلع هذا الجبل مصعده ومأتاه؛ ما لهذا الأمر مطلع أي وجه ولا مأتى (tahdhib)؛ والمطلع المأتى؛ أين مطلع هذا الأمر أي مأتاه؛ هول المطلع (maqayis)","source_summary":"Aktarımlar dağa çıkma ile dağın çıkış ve erişim yerini temel alır. Bu fiziksel düzen, bir işin ele alınacağı yönü anlatmaya genişler; yüksekten aşağıya bakışta karşılaşılan ürkütücü durum da aynı erişim eşiğine bağlanır.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه طلوع الجبل وعلوه، والمطلع مصعدا أو موضع إشراف أو مأتى ووجها للأمر","what_is_not_ar":"لا يدخل فيه موضع طلوع الشمس إلا إذا كان المراد مكان النير، ولا الامتلاء، ولا مجاوزة السهم للغرض"},"support_links":[]},{"boundary":"Bir sınırı bütünüyle doldurma temel okumadır; güneşin gördüğü yeryüzü okuması bu çekirdekle özdeşleştirilmemelidir.","branch_kind":"collocation","branch_ref":"root_000945/B007","candidate_links":[{"candidate_id":"cand_caf4e4e414bb796a9b72","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طَّلَعَ","morph_features":"STEM|POS:V|IMPF|(VIII)|LEM:T~alaEa|ROOT:TlE|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"104:7:2:1","qac_word_ref":"104:7:2","surface_ar":"تَطَّلِعُ"}],"gloss":"bir alanı sınırına kadar doldurma; ayrı aktarımda güneşin gördüğü yeryüzü","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey belirli bir alanı veya kabı sınırına kadar doldurur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yeryüzünün dolusu, avucu dolduran yay gövdesi, dolu kap ve dolu su gözü bu ölçülü doluluğun örnekleridir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yeryüzüyle kurulan söz, bazı aktarımlarda güneşin üzerine doğup gördüğü bütün alanı belirtir."}}],"root_ar":"ط ل ع","root_id":"root_000945","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer, avuç, yay, kap veya su gözü ölçüsünde tam doluluk ya da yeryüzüne bağlı güneş kapsamı anlatılırken kullanılır.","boundary_detail":"Bir sınırı bütünüyle doldurma temel okumadır; güneşin gördüğü yeryüzü okuması bu çekirdekle özdeşleştirilmemelidir.","branch_image_ar":"امتلاء مستوعب","concept_gloss":"bir alanı sınırına kadar doldurma; ayrı aktarımda güneşin gördüğü yeryüzü","contextual_glosses":[{"applicability":"Bir kabın kendi sınırına kadar dolduğu veya doldurulduğu bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yer, avuç ve yay ölçülerini ve güneşin gördüğü yeryüzü okumasını dışarıda bırakır.","preserves":"Belirli bir kabın sınırına kadar dolmasını korur."},"facet_ids":["F001","F002"],"text":"kabı ağzına kadar doldurdu","usage_role":"contextual"}],"definition":"Bir yeri, kabı veya avuç içi gibi sınırlı bir alanı bütünüyle dolduran çokluk ve doluluktur. Yeryüzüyle kurulan özel ifadede, ayrı bir aktarıma göre güneşin gördüğü bütün alan da kastedilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey belirli bir alanı veya kabı sınırına kadar doldurur."},{"facet_id":"F002","role":"specialization","statement":"Yeryüzünün dolusu, avucu dolduran yay gövdesi, dolu kap ve dolu su gözü bu ölçülü doluluğun örnekleridir."},{"facet_id":"F003","role":"source_variant","statement":"Yeryüzüyle kurulan söz, bazı aktarımlarda güneşin üzerine doğup gördüğü bütün alanı belirtir."}],"identity_rationale":"Kaynak sözü yeri, avucu, kabı veya su gözünü dolduran çokluğu güçlü biçimde destekler; ancak yeryüzüyle kurulan ifadeyi bazı aktarımlar doluluk, bazıları güneşin gördüğü alan olarak açıklar. Bu nedenle kapsayıcı doluluk çerçevesi, güneşin gördüğü yeryüzü okuması ayrı bir kaynak değişkesi olarak belirtilirse korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yeryüzünü dolduracak çokluk; başka bir aktarımda güneşin gördüğü yeryüzü"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"avucu dolduran şey; özellikle gövdesi avucu dolduran yay"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"ağzına kadar dolu kap veya su gözü"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"ölçü kabını taşacak kadar doldurmak"}],"lexicalization_note":"Doluluk yalnızca yer, avuç, yay, kap, su gözü ve ölçü ifadelerinde tanımlanır; genel bir dolma anlamı olarak yalınlaştırılmaz.","neighbor_coverage_note":"Tüm adaylar karşılaştırıldı; tam doluluğun genel komşularından, bu dalın yer ve avuçla sınırlı kapsamını en açık gösteren ikisi yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli yer, avuç ve kap kuruluşlarıyla sınırlıdır; komşu dal son sınıra varmış doluluğu daha geniş nesne ve canlı örneklerine taşır.","focus_only":"Bu dal yeryüzü ve avuç ölçüsünü, ayrıca güneşin gördüğü alan değişkesini kapsar.","gloss":"son sınıra kadar doluluk","neighbor_only":"Komşu dal nehir doluluğunu ve yükü ağırlaşan dişiyi de son sınıra varma örnekleri arasında sayar.","neighbor_ref":"root_000926/B003","relation_type":"near_synonym","shared_zone":"Her iki dal bir kap veya alanın daha fazlasını alamayacak ölçüde dolmasını anlatır."},{"boundary_match":"partial","distinction":"Bu dal yer ve avuçla kurulan belirli sözlere bağlıdır; komşu dal doluluğu insanın iç durumlarına ve çekme eylemine kadar genişletir.","focus_only":"Bu dal güneşin gördüğü yeryüzü değişkesini ve avucu dolduran yay gövdesini içerir.","gloss":"kabın ölçüsünü doldurma","neighbor_only":"Komşu dal insanın yiyecek, içecek veya öfkeyle dolmasını ve yayı sonuna dek çekmeyi kapsar.","neighbor_ref":"root_001441/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin kendi kabı veya ölçüsüyle eşit düzeyde dolmasını anlatır."}],"source_phrase_ar":"الطلاع ما طلعت عليه الشمس؛ وطلاع الأرض ملء الأرض؛ وقوس طلاع إذا كان عجسها يملأ الكف (ayn)؛ طلاع الشيء ملؤه؛ طلاع الأرض ملؤها؛ قوس طلاع الكف (sihah)؛ طلاع الأرض ملؤها حتى يطالع أعلى الأرض؛ طلاع الأرض ما طلعت عليه الشمس؛ قدح طلاع ممتلىء؛ عين طلاعة ممتلئة (tahdhib)؛ الطلاع ما طلعت عليه الشمس والإنسان؛ وقوس طلاع الكف ملء الكف (mufradat)؛ الطلاع ما طلعت عليه الشمس من الأرض؛ قوس طلاع الكف إذا كان عجسها يملأ الكف (maqayis)","source_summary":"Kaynak kümesi, bir alanı veya kabı sınırına kadar kaplayan doluluk anlamını yer, avuç, yay, kap ve su gözü örnekleriyle verir. Yeryüzüne ilişkin sözde ise doluluk açıklaması ile güneşin gördüğü alan açıklaması yan yana bulunur.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه طلاع الأرض بمعنى ملئها أو ما استوعبته الشمس، وطلاع الكف، والقدح أو العين الممتلئة","what_is_not_ar":"لا يدخل فيه طلوع النير نفسه، ولا طلع النخلة، ولا الإشراف المعرفي"},"support_links":["sup_3a87576985803bb9eeaa"]},{"boundary":"İstekle yönelme ve görünüp gizlenerek bakma ayrı kuruluşlardır; genel bilgi edinme veya yalnızca görünüş anlamı değildir.","branch_kind":"collocation","branch_ref":"root_000945/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَّلَعَ","morph_features":"STEM|POS:V|IMPF|(VIII)|LEM:T~alaEa|ROOT:TlE|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"104:7:2:1","qac_word_ref":"104:7:2","surface_ar":"تَطَّلِعُ"}],"gloss":"bir şeye istekle yönelme; bir görünüp bakıp bir gizlenme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin iç isteği belirli bir şeyi görmeye, öğrenmeye veya elde etmeye güçlü biçimde yönelir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kadın başını çıkarıp bakar, sonra geri çekilip gizlenir ve bu davranışı yineler."}}],"root_ar":"ط ل ع","root_id":"root_000945","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İç isteğin bir şeye yönelmesi veya belirli bir kişinin görünme ile gizlenme arasında gidip gelerek bakması anlatılırken kullanılır.","boundary_detail":"İstekle yönelme ve görünüp gizlenerek bakma ayrı kuruluşlardır; genel bilgi edinme veya yalnızca görünüş anlamı değildir.","branch_image_ar":"تطلع النفس وكثرة النظر","concept_gloss":"bir şeye istekle yönelme; bir görünüp bakıp bir gizlenme","contextual_glosses":[{"applicability":"Kişinin belirli bir işi bilmeye veya ona erişmeye içten yöneldiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir görünüp bakıp bir gizlenen kadın betimlemesini dışarıda bırakır.","preserves":"İç isteğin belirli bir işe güçlü biçimde yönelmesini korur."},"facet_ids":["F001"],"text":"o işi öğrenmeye güçlü bir istek duydu","usage_role":"contextual"}],"definition":"İç isteğin bir şeye güçlü biçimde yönelmesi veya bir kadının başını çıkarıp bakarak bir görünüp bir gizlenmesidir; iki kullanım yönelme ve bakma ortaklığı taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin iç isteği belirli bir şeyi görmeye, öğrenmeye veya elde etmeye güçlü biçimde yönelir."},{"facet_id":"F002","role":"specialization","statement":"Bir kadın başını çıkarıp bakar, sonra geri çekilip gizlenir ve bu davranışı yineler."}],"identity_rationale":"Kaynak sözü bir iç isteğin bir şeye yönelmesini ve bir kadının bir görünüp bakıp bir gizlenmesini aynı dalda verir. Bu iki kullanım, yönelerek bakma bağıyla ilişkilidir; ancak içsel istek ile yinelemeli görünme davranışı birbirinin tanımı yapılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bir şeye sürekli ve güçlü biçimde yönelen iç istek"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"bir görünüp bakıp bir geri çekilerek gizlenen kadın"}],"lexicalization_note":"Anlam iç isteği veya belirli kadın betimlemesini kuran sözlerle sınırlıdır; genel isteme, bakma ya da gizlenme anlamına yayılmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; içsel yönelmenin elde etme beklentisinden ve kesintili bakmanın gizlice bakmaktan ayrıldığı iki komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda yönelme görme, bilme ve bakmayla bağlantılıdır; komşu dalda elde etme umudu ve beklenti belirleyicidir.","focus_only":"Bu dal görme ve öğrenme isteğini ve ayrıca görünüp gizlenen kadın betimlemesini içerir.","gloss":"bir şeye içten yönelme","neighbor_only":"Komşu dal elde etme umudunu, beklentiyi ve istenen şeye karşı duyulan iştahı öne çıkarır.","neighbor_ref":"root_000951/B001","relation_type":"near_synonym","shared_zone":"Her iki dal kişinin iç dünyasının istenen bir şeye doğru çekilmesini anlatır."},{"boundary_match":"partial","distinction":"Bu dalda bakan kişi görünme ile gizlenme arasında gidip gelir; komşu dalda bakan gizli kalır ve karşı tarafın dalgınlığını kullanır.","focus_only":"Bu dal bakan kişinin kendisinin bir görünüp bir gizlenmesini anlatır.","gloss":"gizlenerek bakma","neighbor_only":"Komşu dal bakılan kişinin dalgınlığından yararlanarak gizlice bakmayı gerektirir.","neighbor_ref":"root_000700/B006","relation_type":"near_neighbor","shared_zone":"İki dal da bakışın açıkça sürdürülmeyip gizlilikle kesintiye uğramasını içerir."}],"source_phrase_ar":"إن نفسك لطلعة إلى هذا الأمر؛ أي تتطلع إليه؛ وامرأة طلعة قبعة تنظر ساعة وتتنحى أخرى (ayn)؛ وتطلعت إلى ورود كتابك؛ ونفس طلعة؛ وامرأة طلعة (sihah)؛ نفسك لطلعة إلى هذا الأمر؛ وإنها لتطلع إليه أي لتنازع إليه؛ وامرأة طلعة قبعة تنظر ساعة ثم تختبىء ساعة (tahdhib)؛ امرأة طلعة قبعة تظهر رأسها مرة وتستر أخرى (mufradat)؛ ونفس طلعة تتطلع للشيء؛ وامرأة طلعة إذا كانت تكثر الإطلاع (maqayis)","source_summary":"Aktarımlar bir şeye yönelen güçlü iç isteği açıkça verir. Kadın betimlemesinde ise bu yönelme, başını çıkarıp bakma ile geri çekilip gizlenmenin sırayla yinelenmesi biçiminde somutlaşır.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه النفس الطلعة التي تتطلع إلى الشيء، والمرأة الطلعة القبعة التي تظهر وتنظر ثم تختبىء","what_is_not_ar":"لا يدخل فيه مجرد الاطلاع على سر أو أمر، ولا الطليعة العسكرية، ولا الطلعة بمعنى الرؤية"},"support_links":[]},{"boundary":"Dal insanın görülen görünüşüne bağlıdır; bakma isteğini, gök varlığının doğuşunu veya bir nesnenin biçimini değiştirmeyi kapsamaz.","branch_kind":"bare","branch_ref":"root_000945/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَّلَعَ","morph_features":"STEM|POS:V|IMPF|(VIII)|LEM:T~alaEa|ROOT:TlE|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"104:7:2:1","qac_word_ref":"104:7:2","surface_ar":"تَطَّلِعُ"}],"gloss":"bir insanın görülüşü ve göz önündeki görünüşü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir insanın göz önünde beliren yüzü ve genel görünüşü adlandırılır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Görünüş, karşılaşmada güzel bulunabilir veya kişiyi görmeye yönelik bir karşılama sözü içinde anılabilir."}}],"root_ar":"ط ل ع","root_id":"root_000945","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin yüzüyle ve genel görünümüyle başkasının gözüne nasıl göründüğü adlandırılırken kullanılır.","boundary_detail":"Dal insanın görülen görünüşüne bağlıdır; bakma isteğini, gök varlığının doğuşunu veya bir nesnenin biçimini değiştirmeyi kapsamaz.","branch_image_ar":"طلعة مرئية","concept_gloss":"bir insanın görülüşü ve göz önündeki görünüşü","contextual_glosses":[{"applicability":"Bir insanın görülen yüzü ve genel görünüşü beğenildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Değer yargısı içermeyen sıradan görülüş ve karşılama kullanımlarını dışarıda bırakır.","preserves":"İnsanın göz önündeki görünüşünü ve olumlu değerlendirmeyi korur."},"facet_ids":["F001","F002"],"text":"ne hoş bir görünüşü var","usage_role":"contextual"}],"definition":"Bir insanın başkası tarafından görüldüğü andaki yüzü, görünüşü veya genel görülüş biçimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir insanın göz önünde beliren yüzü ve genel görünüşü adlandırılır."},{"facet_id":"F002","role":"associated_use","statement":"Görünüş, karşılaşmada güzel bulunabilir veya kişiyi görmeye yönelik bir karşılama sözü içinde anılabilir."}],"identity_rationale":"Kaynak sözü bağımsız adı bir insanın görülüşü olarak açıklar ve güzel bulunabilen görünüş ile karşılaşma sırasında görülen yüzü aynı kullanımda örnekler. Dalın insanın göz önündeki görünüşü biçimindeki çerçevesi bu kanıtı doğrudan karşılar.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bir insanın yüzü, genel görünüşü veya görülüşü"}],"lexicalization_note":"Tanım bağımsız görünüş adını kapsar; başka kuruluşlardaki bakma, belirme ya da gösterme işlemleri buraya eklenmez.","neighbor_coverage_note":"Tüm komşular değerlendirildi; insanın görülüşünü genel görünüş ve ayna alanlarından ayıran iki yakın komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın gösterileni insandır; komşu dal görünüşü nesnelere, hoş ya da kötü biçimlere ve toprağın bitki vermesine kadar genişletir.","focus_only":"Bu dal özellikle bir insanın görülüşüne ve karşılaşmada beliren yüzüne bağlıdır.","gloss":"göz önündeki görünüş","neighbor_only":"Komşu dal her tür şeyin görünüşünü ve toprağın bitki göstermesini de kapsar.","neighbor_ref":"root_001520/B004","relation_type":"near_synonym","shared_zone":"Her iki dal bir şeyin bakana nasıl göründüğünü ve görünüşünün değerlendirilmesini anlatır."},{"boundary_match":"partial","distinction":"Bu dal görülen kişinin görünüşüyle sınırlıdır; komşu dal görmeyi sağlayan aynayı ve yüzdeki belirtileri de ayrı kapsam öğeleri yapar.","focus_only":"Bu dal bir insanın doğrudan görülüşünü bağımsız ad olarak belirtir.","gloss":"insanın görünüşü","neighbor_only":"Komşu dal ayna nesnesini, yüzde beliren işareti ve daha geniş görünüm sözlerini kapsar.","neighbor_ref":"root_000531/B006","relation_type":"near_synonym","shared_zone":"İki dal bir insanın yüzü ve genel görünüşünün göze gelmesi alanında örtüşür."}],"source_phrase_ar":"والطلعة الرؤية؛ ما أحسن طلعته أي رؤيته؛ حيا الله طلعتك (ayn)؛ والطلعة الرؤية (sihah)؛ طلعته رؤيته؛ يقال حيا الله طلعتك (tahdhib)؛ وطلعة الإنسان رؤيته لأنها تطلع (maqayis)","source_summary":"Aktarımlar bağımsız adı bir insanın görülüşü ve göz önündeki görünüşü olarak açıklar. Güzel görünüşü övme ve kişinin görünmesini karşılayan sözler, bu temel görülüş anlamının kullanımlarıdır.","sources":["AY","SI","TA","MQ"],"what_is_ar":"يدخل فيه الطلعة بمعنى الرؤية أو هيئة الإنسان حين ترى","what_is_not_ar":"لا يدخل فيه التطلع الشهوى أو كثرة النظر، ولا طلوع الشمس، ولا الطلع النباتي"},"support_links":[]},{"boundary":"Dal yalnızca okun nişan alınan yerin üstünden geçmesine bağlıdır; genel yükselme, her türlü ıskalama veya başka bir aracın aşması değildir.","branch_kind":"collocation","branch_ref":"root_000945/B010","candidate_links":[{"candidate_id":"cand_203f9396538e8f231cd2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طَّلَعَ","morph_features":"STEM|POS:V|IMPF|(VIII)|LEM:T~alaEa|ROOT:TlE|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"104:7:2:1","qac_word_ref":"104:7:2","surface_ar":"تَطَّلِعُ"}],"gloss":"okun nişan alınan yerin üstünden geçip arkasına düşmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ok, nişan alınan yerin üst bölümünü aşacak kadar yükselir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Üstten geçen ok nişan alınan yerin arkasına düşebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı olay, oku atan kişinin atışının üstten aşması biçiminde de anlatılır."}}],"root_ar":"ط ل ع","root_id":"root_000945","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir okun atış sırasında fazla yükselerek nişan alınan yeri üstten aştığı durumda kullanılır.","boundary_detail":"Dal yalnızca okun nişan alınan yerin üstünden geçmesine bağlıdır; genel yükselme, her türlü ıskalama veya başka bir aracın aşması değildir.","branch_image_ar":"سهم يطلع فوق الغرض","concept_gloss":"okun nişan alınan yerin üstünden geçip arkasına düşmesi","contextual_glosses":[{"applicability":"Atılan okun üst kenarı aşıp arka tarafa geçtiği atış bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Okun mutlaka arka tarafa düşmesi sonucunu açıkça belirtmez.","preserves":"Okun nişan alınan yeri üstten aşmasını korur."},"facet_ids":["F001"],"text":"oku nişan tahtasının üstünden geçti","usage_role":"contextual"}],"definition":"Atılan okun yükselerek nişan alınan yerin üst kenarından geçmesi ve çoğu anlatımda onun arkasına düşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ok, nişan alınan yerin üst bölümünü aşacak kadar yükselir."},{"facet_id":"F002","role":"extension","statement":"Üstten geçen ok nişan alınan yerin arkasına düşebilir."},{"facet_id":"F003","role":"associated_use","statement":"Aynı olay, oku atan kişinin atışının üstten aşması biçiminde de anlatılır."}],"identity_rationale":"Kaynak sözü, atılan okun nişan alınan noktanın üstünden geçmesini, yükselmesini ve arkasına düşmesini doğrudan bildirir. Dalın okun yukarıdan aşması biçimindeki çerçevesi hareketin yönünü ve sonucunu eksiksiz korur.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"yükselip nişan alınan yerin üstünden geçerek arkasına düşen ok"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"attığı ok nişan alınan yerin üstünden geçmek"}],"lexicalization_note":"Anlam ok, atıcı ve nişan alınan yerle kurulan ifadelerle sınırlıdır; genel aşma veya sapma anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; üstten aşmanın göğe yükselmeden ve yönü belirtilmeyen arkaya geçişten ayrıldığı iki komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal üst kenardan geçiş ve arka tarafa düşme çizgisini korur; komşu dal göğe doğru yükselmeyi daha bağımsız bir sonuç olarak da içerir.","focus_only":"Bu dal üstten geçen okun arka tarafa düşmesi sonucunu da belirtir.","gloss":"okun üstten aşması","neighbor_only":"Komşu dal okun gökyüzüne doğru yükselmesini, belirli bir yere düşme şartı olmadan kapsar.","neighbor_ref":"root_000781/B006","relation_type":"near_synonym","shared_zone":"Her iki dal okun nişan alınan yerin üstüne yükselerek onu aşmasını anlatır."},{"boundary_match":"partial","distinction":"Bu dal aşma yolunu üst kenarla sınırlar; komşu dal yalnızca arka tarafa geçiş sonucunu belirler.","focus_only":"Bu dal okun özellikle nişan alınan yerin üst kenarından geçmesini gerektirir.","gloss":"okun arkaya geçmesi","neighbor_only":"Komşu dal okun hangi yandan geçtiğini belirtmeden arka tarafa çıkmasını veya düşmesini kapsar.","neighbor_ref":"root_000458/B018","relation_type":"near_synonym","shared_zone":"İki dal da okun nişan alınan yeri geçip arka tarafında kalabildiğini anlatır."}],"source_phrase_ar":"وأطلع الرامي أي جاز سهمه من فوق الغرض (sihah)؛ والطالع من السهام الذي يقع وراء الهدف؛ يسجد للطالع؛ شخص سهمه فارتفع عن الرمية (tahdhib)؛ ورمى فلان فأطلع وأشخص إذا مر سهمه برأس الغرض (maqayis)","source_summary":"Aktarımlar okun yükselip nişan alınan yerin üstünden veya üst kenarından geçmesinde birleşir. Okun arka tarafa düşmesi, bu üstten aşma hareketinin belirtilen sonucudur.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه السهم الطالع أو إطلاع الرامي إذا ارتفع السهم وجاوز الغرض أو وقع وراءه","what_is_not_ar":"لا يدخل فيه علو الجبل، ولا طلوع الشمس، ولا الطول في الشخص أو النخلة"},"support_links":["sup_346ed1969d08296d679a"]},{"boundary":"Dal mide içeriğinin ağızdan çıkarılması ve çıkan maddeyle sınırlıdır; bulantı, ishal veya başka boşaltım olayları bunun parçası değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000945/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَّلَعَ","morph_features":"STEM|POS:V|IMPF|(VIII)|LEM:T~alaEa|ROOT:TlE|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"104:7:2:1","qac_word_ref":"104:7:2","surface_ar":"تَطَّلِعُ"}],"gloss":"kusmak ve kusmuk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi mide içeriğini ağız yoluyla dışarı çıkarır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dışarı çıkarılan mide içeriği, eylemin sonucu olan madde adıyla anılır."}}],"root_ar":"ط ل ع","root_id":"root_000945","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Mide içeriğinin ağızdan çıkarılması veya çıkarılan maddenin kendisi anlatılırken kullanılır.","boundary_detail":"Dal mide içeriğinin ağızdan çıkarılması ve çıkan maddeyle sınırlıdır; bulantı, ishal veya başka boşaltım olayları bunun parçası değildir.","branch_image_ar":"قيء يطلع","concept_gloss":"kusmak ve kusmuk","contextual_glosses":[{"applicability":"Bir kişinin mide içeriğini ağızdan dışarı çıkardığı olay için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dışarı çıkan maddenin bağımsız adını dışarıda bırakır.","preserves":"Mide içeriğini ağızdan çıkarma eylemini korur."},"facet_ids":["F001"],"text":"kustu","usage_role":"contextual"}],"definition":"Mide içeriğini ağızdan dışarı çıkarma eylemi ve bu eylemle dışarı çıkan kusmuktur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi mide içeriğini ağız yoluyla dışarı çıkarır."},{"facet_id":"F002","role":"extension","statement":"Dışarı çıkarılan mide içeriği, eylemin sonucu olan madde adıyla anılır."}],"identity_rationale":"Kaynak sözü hem kişinin kusma eylemini hem de dışarı çıkardığı kusmuğun adını açık biçimde verir. Dalın kusma olayı ve sonucu çerçevesi, eylem ile ürün ayrımını koruyarak kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"kusmak"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"kusmuk"}],"lexicalization_note":"Kuruluşla verilen kusma eylemi ile bağımsız kusmuk adı ayrı tutulur; ikisi genel bedensel boşaltım anlamına genişletilmez.","neighbor_coverage_note":"Adayların tümü karşılaştırıldı; kusmuk adıyla örtüşme ve bulantıyla süreç komşuluğu, dalın eylem-sonuç sınırını en iyi açıkladığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal madde adının yanında onu çıkarma eylemini de içerir; komşu dalın verilen sınırı madde adıdır.","focus_only":"Bu dal kusma eylemini ve kusmuk adını birlikte kapsar.","gloss":"kusmuk","neighbor_only":"Komşu dal yalnızca kusmuğu adlandıran bağımsız bir söz değerindedir.","neighbor_ref":"root_001334/B007","relation_type":"near_synonym","shared_zone":"İki dal da mideden ağız yoluyla çıkarılan maddeyi adlandırır."},{"boundary_match":"partial","distinction":"Bu dal gerçekleşen dışarı atma olayıdır; komşu dal dışarı atma gerçekleşmese de bulunabilen öncül bulantı durumudur.","focus_only":"Bu dal mide içeriğinin gerçekten dışarı çıkarılması ve çıkan maddeyi anlatır.","gloss":"bulantı ve kusma","neighbor_only":"Komşu dal kusma gerçekleşmeden önceki bulantı ve midenin bulanıp kabarması durumunu anlatır.","neighbor_ref":"root_001073/B003","relation_type":"near_neighbor","shared_zone":"İki dal aynı bedensel süreçte mide rahatsızlığı ve ağızdan çıkarma çevresinde yer alır."}],"source_phrase_ar":"وأطلع أي قاء؛ والطلعاء القيء (sihah)؛ أطلع الرجل إطلاعا إذا قاء؛ الطولع الطلعاء وهو القيء (tahdhib)؛ ومن الباب الطلعاء القيء؛ يقال أطلع إذا قاء (maqayis)","source_summary":"Aktarımlar kişinin kusması ile kusmuk adını birlikte ve tutarlı biçimde verir. Biri bedensel eylemi, diğeri o eylem sonucunda dışarı çıkan maddeyi gösterir.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه أطلع إذا قاء، والطلعاء أو الطولع بمعنى القيء","what_is_not_ar":"لا يدخل فيه خروج الطلع النباتي، ولا ظهور الشخص، ولا الامتلاء"},"support_links":[]},{"boundary":"Palmiye kullanımında komşu ağaçları aşma ilişkisi zorunludur; uzun erkek adı ise ayrı ve biçimce sınırlı bir türetmedir.","branch_kind":"mixed_non_bare","branch_ref":"root_000945/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَّلَعَ","morph_features":"STEM|POS:V|IMPF|(VIII)|LEM:T~alaEa|ROOT:TlE|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"104:7:2:1","qac_word_ref":"104:7:2","surface_ar":"تَطَّلِعُ"}],"gloss":"çevresindeki palmiye ağaçlarını boyca aşma; uzun boylu erkek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Palmiye ağacı, yanında bulunan diğer palmiye ağaçlarından daha uzun duruma gelir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Biçimce genişletilmiş ayrı bir ad, uzun boylu erkeği belirtir."}}],"root_ar":"ط ل ع","root_id":"root_000945","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir palmiye ağacının komşularından uzun olması veya ayrı türemiş adla uzun boylu bir erkeğin belirtilmesi durumunda kullanılır.","boundary_detail":"Palmiye kullanımında komşu ağaçları aşma ilişkisi zorunludur; uzun erkek adı ise ayrı ve biçimce sınırlı bir türetmedir.","branch_image_ar":"طول بارز","concept_gloss":"çevresindeki palmiye ağaçlarını boyca aşma; uzun boylu erkek","contextual_glosses":[{"applicability":"Bir palmiye ağacının aynı yerdeki öteki palmiye ağaçlarını boyca aştığı bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uzun boylu erkeği belirten ayrı türemiş adı dışarıda bırakır.","preserves":"Palmiye ağacının komşu ağaçlara göre daha uzun olmasını korur."},"facet_ids":["F001"],"text":"yanındaki ağaçlardan daha uzun bir palmiye","usage_role":"contextual"}],"definition":"Bir palmiye ağacının yanındaki ağaçları boyca aşarak onlardan uzun olmasıdır; ayrı bir türemiş ad da uzun boylu erkeği belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Palmiye ağacı, yanında bulunan diğer palmiye ağaçlarından daha uzun duruma gelir."},{"facet_id":"F002","role":"extension","statement":"Biçimce genişletilmiş ayrı bir ad, uzun boylu erkeği belirtir."}],"identity_rationale":"Kaynak sözü çevresindeki palmiye ağaçlarını boyca aşan bir ağacı ve ayrı bir türemiş biçimde uzun boylu erkeği destekler. Dal uzunluk ortaklığıyla korunabilir, ancak palmiye için göreli üstünlük ile insan için yalın boy niteliği birbirine karıştırılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"yanındaki palmiye ağaçlarından daha uzun olan palmiye"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"uzun boylu adam"}],"lexicalization_note":"Palmiye betimlemesi ile uzun erkek adı ayrı birimlerdir; bunlardan genel ve serbest bir uzunluk anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün komşular değerlendirildi; palmiye uzunluğundaki göreli sınırı ve uzunluk-kısalık karşıtlığını en açık gösteren iki komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal palmiye uzunluğunu komşu ağaçlarla karşılaştırmalı kurar; komşu dal göreli aşma şartı olmadan uzunluğu ve başka hayvanları kapsar.","focus_only":"Bu dal palmiye ağacının yanındakileri boyca aşmasını ve uzun erkek adını birlikte içerir.","gloss":"uzun palmiye","neighbor_only":"Komşu dal uzunluğu palmiye dışında dişi eşek ve erkek eşek için de bağımsız bir nitelik olarak kullanır.","neighbor_ref":"root_000683/B003","relation_type":"near_synonym","shared_zone":"Her iki dal uzun boylu bir palmiye ağacını adlandırabilir."},{"boundary_match":"opposed","distinction":"Bu dal ölçünün uzun kutbunu, komşu dal ise aynı boy ekseninin kısa kutbunu gösterir.","focus_only":"Bu dal palmiye veya erkeğin belirgin uzunluğunu anlatır.","gloss":"uzunluk ve kısalık","neighbor_only":"Komşu dal canlıların ve nesnelerin kısa oluşunu, kısa kılınmasını veya kısa sayılmasını anlatır.","neighbor_ref":"root_001231/B001","relation_type":"antonym","shared_zone":"İki dal canlıların boyunu düşey ölçü bakımından değerlendirir."}],"source_phrase_ar":"نخلة مطلعة إذا طالت النخيل (sihah)؛ نخلة مطلعة إذا طالت النخلة التي بحذائها فكانت أطول منها (tahdhib)؛ الهطلع الرجل الطويل زيدت فيه الهاء من طلع (maqayis)","source_summary":"Kaynak sözü palmiye ağacının çevresindekileri boyca aşmasını göreli bir uzunluk olarak verir. Ayrı bir türemiş insan adı, aynı uzunluk özelliğini erkeğin boyuna uygular.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه النخلة المطلعة إذا طالت ما حولها، والهطلع الرجل الطويل مع الهاء الزائدة","what_is_not_ar":"لا يدخل فيه الصعود على جبل، ولا مجاوزة السهم، ولا مطلق ظهور الشخص على القوم"},"support_links":[]},{"boundary":"Yürek adı, yüreğin yaralanması veya hastalanması ve korkaklık bu dalın dışında kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_001122/B001","candidate_links":[{"candidate_id":"cand_e1df5c3a8a59383c8023","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فُؤَاد","morph_features":"STEM|POS:N|LEM:fu&aAd|ROOT:fAd|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:7:4:2","qac_word_ref":"104:7:4","surface_ar":"أَفْـِٔدَةِ"}],"gloss":"yüksek ateş ısısı; ateşte pişirme, ateş yakma ve bunların ürün, araç ve yerleri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Anlam alanının çekirdeği, ateşin yakıcı derecedeki yüksek ısısıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Et, ateşe tutularak kızartılır veya ateşin ısısıyla pişirilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ekmek, sıcak kül ve közün içine yerleştirilerek pişirilir; bunun için kül ile ateş içinde bir yuva da hazırlanabilir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Topluluğun ateş yakması ve ateşin kendisi aynı ısı merkezinden adlandırılır."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Ateşte pişmiş yiyecek, kızartma veya pişirme aracı ve ateş yakılan ya da pişirme yapılan yer sonuç, araç ve yer uzantılarıdır."}}],"root_ar":"ف ء د","root_id":"root_001122","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yüksek ısı çekirdeğini, başlıca işlemlerini ve bunlara bağlı sonuç, araç ve yer uzantılarını birlikte göstermek için uygundur.","boundary_detail":"Yürek adı, yüreğin yaralanması veya hastalanması ve korkaklık bu dalın dışında kalır.","branch_image_ar":"حمى النار التي تشوي وتخبز وتوقد","concept_gloss":"yüksek ateş ısısı; ateşte pişirme, ateş yakma ve bunların ürün, araç ve yerleri","contextual_glosses":[{"applicability":"Etin doğrudan ateş ısısıyla kızartıldığı veya pişirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yüksek ısı çekirdeğinin öteki kullanımlarını, kül içinde ekmek pişirmeyi, ateş yakmayı ve ad uzantılarını dışarıda bırakır.","preserves":"Etin ateş ısısıyla pişirilmesi işlemini korur."},"facet_ids":["F001","F002"],"text":"ateşte kızartmak","usage_role":"contextual"},{"applicability":"Ekmeğin sıcak kül ile köz içine gömülerek pişirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Et kızartma, ateş yakma, ateşin kendisi ve araç, ürün ile yer uzantıları bu anlatımda yer almaz.","preserves":"Ekmeğin sıcak kül ve köz içinde pişirilmesi işlemini korur."},"facet_ids":["F001","F003"],"text":"kül ve köz içinde pişirmek","usage_role":"contextual"},{"applicability":"Bir topluluğun ateşi tutuşturduğu eylem bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Pişirme işlemleri, yüksek ısının kendisi ve ürün, araç ile yer adlandırmaları bu karşılıkta bulunmaz.","preserves":"Ateşi tutuşturma eylemini açık biçimde korur."},"facet_ids":["F004"],"text":"ateş yakmak","usage_role":"contextual"}],"definition":"Yüksek ateş ısısını ve bu ısıyla eti kızartma, ekmeği sıcak kül ile köz içinde pişirme ve ateş yakma işlemlerini anlatır. Ateşin kendisini, bu yolla pişmiş ürünü, pişirme aracını ve ateş yakılan ya da pişirme yapılan yeri de adlandırabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Anlam alanının çekirdeği, ateşin yakıcı derecedeki yüksek ısısıdır."},{"facet_id":"F002","role":"specialization","statement":"Et, ateşe tutularak kızartılır veya ateşin ısısıyla pişirilir."},{"facet_id":"F003","role":"specialization","statement":"Ekmek, sıcak kül ve közün içine yerleştirilerek pişirilir; bunun için kül ile ateş içinde bir yuva da hazırlanabilir."},{"facet_id":"F004","role":"extension","statement":"Topluluğun ateş yakması ve ateşin kendisi aynı ısı merkezinden adlandırılır."},{"facet_id":"F005","role":"extension","statement":"Ateşte pişmiş yiyecek, kızartma veya pişirme aracı ve ateş yakılan ya da pişirme yapılan yer sonuç, araç ve yer uzantılarıdır."}],"identity_rationale":"Kaynak ifadesi, anlam alanının merkezine yüksek ısıyı koyar; eti ateşte kızartmayı, ekmeği sıcak kül ve köz içinde pişirmeyi, ateş yakmayı, ateşin kendisini, pişmiş ürünü ve bu işlemlerde kullanılan araçlarla yerleri de açıkça bu alana bağlar. Verilen dal çerçevesi bu işlemleri ve sonuçları birbirine karıştırmadan kapsar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"eti ateşte kızartmak veya pişirmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ateşte kızartılmış ya da pişirilmiş"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"kızartma veya közde pişirme aracı; şiş ya da fırını karıştırma çubuğu"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kızartma ya da ateş yakma yeri"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ekmeği sıcak kül ve köz içinde pişirmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ekmek için kül ve ateş içinde pişirme yuvası açmak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ekmeğin yerleştirildiği sıcak kül ve ateş yuvası"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"fırını karıştırma veya kızartma araçları"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"kızartma şişi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"onu ateşte kızarttı"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kızartma şişi veya ateşte pişirme aracı"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"ateş"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"topluluk ateş yaktı"}],"lexicalization_note":"Dal, yüksek ısı ve ateşle ilgili yalın adlandırmaların yanında et kızartma, kül içinde ekmek pişirme ve ateş yakma gibi belirli yapılara bağlı kullanımları ayrı ayrı kapsar.","neighbor_coverage_note":"Adayların tümü değerlendirildi; yayımlanan dört karşılaştırma ateş yakma, farklı pişirme yöntemleri, etin ateşte değişmesi ve iç ısıyla adlandırılan yürek arasındaki en yararlı sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal, yüksek ısı çekirdeğinden pişmiş ürüne, araca ve yere uzanan daha geniş bir aile kurar; komşu dal ise ısınma ateşini ve ateşte çubuk doğrultmayı kendi sınırına alır.","focus_only":"Bu dal yüksek ısıyı, kül içinde ekmek pişirmeyi, ateşi, pişmiş ürünü, araçları ve pişirme ya da yakma yerini de kapsar.","gloss":"ateş yakma ve ateşte pişirme","neighbor_only":"Komşu dal ısınmak için yakılan ateşi ve bir çubuğu ateşte çevirerek doğrultmayı ayrıca kapsar.","neighbor_ref":"root_000880/B004","relation_type":"near_synonym","shared_zone":"İki dal da ateş yakma ile eti ateş ısısında pişirme alanlarında örtüşür."},{"boundary_match":"partial","distinction":"Bu dalda ısı kaynağı doğrudan ateş, kül ve közdür; komşu dalın ayırıcı koşulu ise yiyeceğin tava üzerinde pişirilmesidir.","focus_only":"Bu dal doğrudan ateşte kızartmayı, kül içinde pişirmeyi, ateş yakmayı ve bunlara bağlı adları kapsar.","gloss":"kuru ısıyla yiyecek pişirme","neighbor_only":"Komşu dal yiyeceğin tava üzerinde kavrulup pişmesini, tavayı ve bu işe bağlı kişi ile yer adlarını kapsar.","neighbor_ref":"root_001253/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da yiyeceği yüksek ve kuru ısıyla pişirme alanına girer."},{"boundary_match":"partial","distinction":"Bu dal işlemi kızartma ve ateş ısısı açısından kurar; komşu dal ise etin suyunun akması ve yapısının değişmesiyle belirlenen pişme sonucuna odaklanır.","focus_only":"Bu dal et dışındaki ekmek pişirmeyi, ateş yakmayı, ateşi ve araç, ürün ile yer adlarını da içerir.","gloss":"ateşin eti pişirip değiştirmesi","neighbor_only":"Komşu dal özellikle etin pişerken suyunu salıp yapısının değişmesi sonucunu öne çıkarır.","neighbor_ref":"root_001266/B002","relation_type":"near_neighbor","shared_zone":"İki dal da etin ateşin etkisiyle pişip değişmesini anlatabilir."},{"boundary_match":"thematic_only","distinction":"Buradaki ısı dış dünyadaki ateş ve onun işlemleridir; komşu dalda ise ısı, bir beden organının adlandırılmasını açıklayan içsel bir özellik olarak kalır.","focus_only":"Bu dal gerçek ateş ısısını, pişirmeyi, ateş yakmayı ve bunların ürün, araç ile yerlerini anlatır.","gloss":"gerçek ateş ile iç ısı bağı","neighbor_only":"Komşu dal, iç ısısı ve yanışı düşünülerek adlandırılan yürek organını anlatır.","neighbor_ref":"root_001122/B002","relation_type":"thematic","shared_zone":"Dallar, yüksek ısı düşüncesi üzerinden tarihsel ve kavramsal bir bağ taşır."}],"source_phrase_ar":"أصل صحيح يدل على حمى وشدة حرارة (maqayis)؛ فأدت اللحم شويته ولحم فئيد أي مشوي (maqayis;sihah;mufradat)؛ فأدت الخبزة مللتها أو خبزتها في الملة (maqayis;sihah;tahdhib)؛ افتأد القوم إذا أوقدوا نارا والفئيد النار نفسها (tahdhib)؛ المفأد السفود أو ما يخبز ويشوى به والمفتأد موضع الوقود (maqayis;sihah;tahdhib)","source_summary":"Kaynaklar yüksek ısı çekirdeğini; et kızartma, kül içinde ekmek pişirme, ateş yakma, ateş, pişmiş ürün, araç ve yer anlamlarıyla birlikte sunar.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الحمى وشدة الحرارة، وشوي اللحم وخبز الخبزة في الملة، وإيقاد النار والنار نفسها، والفئيد المشوي أو المخبوز، وما به أو فيه الشوي والخبز من مفأد وسفود وموضع وقود.","what_is_not_ar":"لا يدخل فيه الفؤاد بوصفه القلب إلا من جهة تعليل التسمية بالحرارة، ولا إصابة الفؤاد أو داؤه، ولا وصف الجبان بضعف الفؤاد."},"support_links":["sup_59bf448e19e2f7b95ddd"]},{"boundary":"Gerçek ateşle pişirme, yüreği yaralama veya hastalık ve korkaklık bu organ anlamının parçası değildir.","branch_kind":"bare","branch_ref":"root_001122/B002","candidate_links":[{"candidate_id":"cand_e1df5c3a8a59383c8023","lane":"micro"},{"candidate_id":"cand_caf4e4e414bb796a9b72","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فُؤَاد","morph_features":"STEM|POS:N|LEM:fu&aAd|ROOT:fAd|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:7:4:2","qac_word_ref":"104:7:4","surface_ar":"أَفْـِٔدَةِ"}],"gloss":"iç ısısı gözetilen yürek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Göğüste bulunan organ, yürek olarak adlandırılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu adlandırmada organın iç ısısı veya içten yanıyormuş gibi düşünülmesi özellikle gözetilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çoğul biçim, aynı organın birden çok kişideki örneklerini yani yürekleri anlatır."}}],"root_ar":"ف ء د","root_id":"root_001122","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yürek organını ve bu adın iç ısı ya da yanış düşüncesiyle kurulan açıklayıcı özelliğini birlikte verir.","boundary_detail":"Gerçek ateşle pişirme, yüreği yaralama veya hastalık ve korkaklık bu organ anlamının parçası değildir.","branch_image_ar":"الفؤاد قلب منظور إليه كتوقد داخلي","concept_gloss":"iç ısısı gözetilen yürek","contextual_glosses":[{"applicability":"Metin yalnızca beden organını gösteriyorsa doğal ve kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Adlandırmada gözetilen iç ısı veya yanış açıklamasını görünür kılmaz.","preserves":"Söz konusu beden organının yürek olduğu bilgisini korur."},"facet_ids":["F001"],"text":"yürek","usage_role":"general"},{"applicability":"Organ adının çoğul olduğu ve birden çok yüreği gösterdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Adın iç ısı veya yanış düşüncesiyle açıklanan yönünü belirtmez.","preserves":"Yürek organının çoğul olarak belirtilmesini korur."},"facet_ids":["F001","F003"],"text":"yürekler","usage_role":"contextual"}],"definition":"Bedendeki yüreği, özellikle içinde bir ısı veya yanış bulunduğu düşünülerek adlandırır; çoğul biçim de birden çok yüreği belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Göğüste bulunan organ, yürek olarak adlandırılır."},{"facet_id":"F002","role":"specialization","statement":"Bu adlandırmada organın iç ısısı veya içten yanıyormuş gibi düşünülmesi özellikle gözetilir."},{"facet_id":"F003","role":"extension","statement":"Çoğul biçim, aynı organın birden çok kişideki örneklerini yani yürekleri anlatır."}],"identity_rationale":"Kaynak ifadesi organı doğrudan yürek olarak tanımlar ve bu adlandırmayı organın iç ısısı ya da yanışı düşüncesiyle açıklar. Verilen dal çerçevesi organ kimliğini korurken ısı bağlantısını tanımın gerekçesi olarak doğru yerde tutar.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yürek; iç ısısı veya yanışı gözetilerek adlandırılan organ"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yürekler"}],"lexicalization_note":"Dal yalın yürek adını tanımlar; belirli bir söz dizimine bağlı ateş, yaralanma, hastalık veya korkaklık anlamı tanıma taşınmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; organı en çok karıştırabilecek iç merkez adı, gerçek ateş ve organ yaralanması alanlarıyla üç sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal bedensel organı iç ısı düşüncesiyle sınırlar; komşu dal ise aynı organ adından gizli iç benlik ve korku alanına uzanır.","focus_only":"Bu dal yüreğin adlandırılmasında organın iç ısısını veya yanışını özellikle gözetir.","gloss":"yürek ve iç merkez","neighbor_only":"Komşu dal yüreğin yanında iç benliği, iç korkuyu ve göğüste saklı olanı da kapsar.","neighbor_ref":"root_000266/B010","relation_type":"near_synonym","shared_zone":"Her iki dal da göğüsteki yüreği adlandırabilir."},{"boundary_match":"thematic_only","distinction":"Bu dalda ısı organ adının açıklayıcı özelliğidir; komşu dalda ise ateş ve ısının gerçek etkileri doğrudan anlamın merkezindedir.","focus_only":"Bu dal, iç ısısı düşünülerek adlandırılan beden organını anlatır.","gloss":"iç ısı ve gerçek ateş","neighbor_only":"Komşu dal gerçek ateş ısısını, pişirmeyi, ateş yakmayı ve bunlara bağlı nesne ile yerleri anlatır.","neighbor_ref":"root_001122/B001","relation_type":"thematic","shared_zone":"İki dal yalnızca yüksek ısı düşüncesi üzerinden kavramsal olarak bağlanır."},{"boundary_match":"thematic_only","distinction":"Organın kendisini adlandırmak, o organı vurup yaralama eylemiyle veya organda oluşan hastalıkla aynı anlam değildir.","focus_only":"Bu dal sağlıklı ya da durumu belirtilmemiş yürek organının adıdır.","gloss":"yürek ve yüreğin zarar görmesi","neighbor_only":"Komşu dal yüreğin hedef alınarak yaralanmasını veya yürekte hastalık oluşmasını anlatır.","neighbor_ref":"root_001122/B003","relation_type":"thematic","shared_zone":"İki dalın ortak katılımcısı yürek organıdır."}],"source_phrase_ar":"الفؤاد القلب والجمع الأفئدة (sihah)؛ الفؤاد كالقلب لكن يقال له فؤاد إذا اعتبر فيه معنى التفؤد أي التوقد (mufradat)؛ الفؤاد سمي بذلك لحرارته أو لتفؤده (maqayis;tahdhib)","source_summary":"Kaynaklar sözcüğü yürek organıyla özdeşleştirir; adın gerekçesini de organın ısısı veya içten yanışı düşüncesine bağlar ve çoğulunu belirtir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الفؤاد بمعنى القلب أو كالقلب، وجمعه أفئدة، عندما يلحظ فيه معنى التفؤد أو التوقد والحرارة.","what_is_not_ar":"لا يدخل فيه شوي اللحم والخبز، ولا أدوات النار، ولا إصابة الفؤاد أو مرضه إلا إذا كان الكلام على القلب نفسه."},"support_links":["sup_3a87576985803bb9eeaa","sup_59bf448e19e2f7b95ddd"]},{"boundary":"Yüreğin yalnızca organ adı olarak kullanılması ve yürek zayıflığına bağlanan korkaklık bu dalın dışında kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_001122/B003","candidate_links":[{"candidate_id":"cand_ad302f8ba4c2b6a17cf3","lane":"micro"},{"candidate_id":"cand_203f9396538e8f231cd2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فُؤَاد","morph_features":"STEM|POS:N|LEM:fu&aAd|ROOT:fAd|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:7:4:2","qac_word_ref":"104:7:4","surface_ar":"أَفْـِٔدَةِ"}],"gloss":"yüreği vurup yaralama veya yürekte hastalık oluşması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir canlının yüreği hedef alınarak vurulur ve organ yaralanır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı anlam alanı, vurma eylemi olmadan kişinin yüreğinde hastalık oluşması durumuna da uzanır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Eylemin sonucu olan kişi veya canlı, yüreğinden vurulmuş ya da yüreği hastalanmış olarak nitelenir."}}],"root_ar":"ف ء د","root_id":"root_001122","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yüreği hedef alan yaralama eylemini ve eylemsiz biçimde yürekte oluşan hastalık durumunu birlikte kapsar.","boundary_detail":"Yüreğin yalnızca organ adı olarak kullanılması ve yürek zayıflığına bağlanan korkaklık bu dalın dışında kalır.","branch_image_ar":"إصابة الفؤاد أو حلول دائه","concept_gloss":"yüreği vurup yaralama veya yürekte hastalık oluşması","contextual_glosses":[{"applicability":"Bir insanın veya av hayvanının yüreği hedef alınarak vurulduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Vurma olmadan yürekte hastalık oluşması kullanımını kapsamaz.","preserves":"Yüreğin hedef alınmasını ve vurma yoluyla yaralanmasını korur."},"facet_ids":["F001"],"text":"yüreğinden vurmak","usage_role":"contextual"},{"applicability":"Kişinin yüreğinde bir hastalık ortaya çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yüreği hedef alarak vurma ve organı yaralama eylemini kapsamaz.","preserves":"Yürekte hastalık oluşması durumunu açıkça korur."},"facet_ids":["F002"],"text":"yürek hastalığına tutulmak","usage_role":"contextual"},{"applicability":"Yüreği hedef alan eylemin sonucunda yaralanan kişi veya canlıyı niteler.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eylemin etkin biçimini ve yürekte kendiliğinden oluşan hastalık durumunu kapsamaz.","preserves":"Eylemin yürekte bıraktığı yaralanma sonucunu korur."},"facet_ids":["F001","F003"],"text":"yüreğinden vurulmuş","usage_role":"contextual"}],"definition":"Bir insanın ya da av hayvanının yüreğini hedef alıp vurmayı ve böylece yüreğini yaralamayı anlatır; ayrıca bir kişinin yüreğinde hastalık oluşması durumunu da belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir canlının yüreği hedef alınarak vurulur ve organ yaralanır."},{"facet_id":"F002","role":"extension","statement":"Aynı anlam alanı, vurma eylemi olmadan kişinin yüreğinde hastalık oluşması durumuna da uzanır."},{"facet_id":"F003","role":"extension","statement":"Eylemin sonucu olan kişi veya canlı, yüreğinden vurulmuş ya da yüreği hastalanmış olarak nitelenir."}],"identity_rationale":"Kaynak ifadesi iki bağlı ancak ayrı durumu açıkça verir: bir canlıyı yüreğinden vurup yaralamak ve kişinin yüreğinde hastalık oluşması. Verilen dal çerçevesi eylem ile hastalık durumunu korur ve bunları organ adının kendisiyle ya da korkaklıkla karıştırmaz.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yüreğe vurup yaralama eylemi"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"yüreğine vurmak veya yüreğinde hastalık oluşturmak"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yüreğinden vurulmuş veya yüreği hastalanmış kimse"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"adamın yüreği hastalandı"}],"lexicalization_note":"Dal, yüreği hedef alan vurma eylemiyle yürek hastalığını ayrı kullanımlar olarak içerir; bu yapıların anlamı yalın yürek adına genellenmez.","neighbor_coverage_note":"Adayların tümü değerlendirildi; yüreğe isabet etme, başka yaşamsal yapının yaralanması, genel hastalık ve ağrılı yara alanlarıyla en açıklayıcı dört karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal yalnızca yüreğe isabet etme çekirdeğini verir; bu dal aynı çekirdeğe ek olarak yürek hastalığı durumunu ve yaralanmış ya da hastalanmış sonucu da taşır.","focus_only":"Bu dal yüreği vurup yaralamanın yanında yürekte hastalık oluşmasını ve etkilenen kişiyi de kapsar.","gloss":"yüreği hedef alıp vurma","neighbor_only":null,"neighbor_ref":"root_001248/B016","relation_type":"near_synonym","shared_zone":"İki dal da bir kişinin yüreğini hedef alıp organa zarar verme eyleminde örtüşür."},{"boundary_match":"partial","distinction":"Eylem türleri yakın olsa da yaralanan yapı aynı değildir: bu dalda yürek, komşu dalda ise ana atardamar hedeflenir.","focus_only":"Bu dal hedef olarak yüreği alır ve ayrıca yürek hastalığını kapsar.","gloss":"yaşamsal bir iç yapıyı vurma","neighbor_only":"Komşu dal hedef olarak ana atardamarı alır ve o damarın vurulmasını ya da kesilmesini kapsar.","neighbor_ref":"root_001622/B003","relation_type":"near_neighbor","shared_zone":"İki dal da yaşamsal bir iç yapının hedef alınarak ağır biçimde yaralanmasını anlatır."},{"boundary_match":"field_only","distinction":"Bu dal belirli bir organı ve ayrıca o organa yönelik darbeyi şart koşar; komşu dalın hastalık alanı çok daha geniştir ve hedefli yaralama çekirdeği yoktur.","focus_only":"Bu dal yüreğe yöneltilen darbeyi veya yalnızca yürekte oluşan hastalığı belirtir.","gloss":"bedende hastalık veya zarar","neighbor_only":"Komşu dal göz hastalığı, genel bedensel hastalık, deliliğe benzer durum ve hazımsızlık gibi çok çeşitli rahatsızlıkları kapsar.","neighbor_ref":"root_000018/B007","relation_type":"same_field","shared_zone":"Her iki dal da bedenin bir rahatsızlıktan etkilenmesi alanına girer."},{"boundary_match":"partial","distinction":"Bu dal anatomik hedef olarak yüreği zorunlu kılar; komşu dal ise yaranın türüne ve ağrısına odaklanır, yüreğe ancak mecazi üzüntü bağlamında uzanır.","focus_only":"Bu dal yüreğin hedef alınmasını ve yürek hastalığını belirtir.","gloss":"ağrılı yaralanma","neighbor_only":"Komşu dal ağrılı yara, deri yarası, yaralı kişi, iğneyle işlenen iz ve üzüntünün yürekte açtığı mecazi yarayı kapsar.","neighbor_ref":"root_001213/B001","relation_type":"near_neighbor","shared_zone":"İki dal da acı veren bir yaralanma ve bundan etkilenen kişi alanında buluşur."}],"source_phrase_ar":"الفأد مصدر فأدته إذا أصبت فؤاده (maqayis)؛ فأدته فهو مفؤود أصبت فؤاده وكذلك إذا أصابه داء فؤاده (sihah)؛ فأدت الصيد إذا أصبت فؤاده وفئد الرجل أصابه داء في فؤاده (tahdhib)","source_summary":"Kaynaklar yüreği hedef alıp vurma eylemini ve bunun yaralanmış sonucunu birlikte verir; ayrıca yürekte hastalık oluşmasını aynı alanın ayrı bir kullanımı olarak kaydeder.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه فأدته أو فأدت الصيد بمعنى أصبت فؤاده، والمفؤود من جهة إصابة الفؤاد، وفئد الرجل إذا أصابه داء في فؤاده.","what_is_not_ar":"لا يدخل فيه الفؤاد اسما للقلب مجردا، ولا الشوي والخبز، ولا وصف الجبان بضعف الفؤاد إلا إذا نص السياق على الداء أو الإصابة."},"support_links":["sup_346ed1969d08296d679a","sup_98e597d3e35b9f3560e7"]},{"boundary":"Gerçek organ yokluğu, yüreğin yaralanması veya hastalanması ve yalın organ adı bu dalın anlamına girmez.","branch_kind":"bare","branch_ref":"root_001122/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"فُؤَاد","morph_features":"STEM|POS:N|LEM:fu&aAd|ROOT:fAd|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:7:4:2","qac_word_ref":"104:7:4","surface_ar":"أَفْـِٔدَةِ"}],"gloss":"yüreksiz ve korkak kişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, korku karşısında cesaret gösteremeyen ve geri duran biri olarak nitelenir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Korkaklık, kişinin yüreği yokmuş veya yüreği güçsüzmüş gibi kurulan bir anlatımla belirtilir."}}],"root_ar":"ف ء د","root_id":"root_001122","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin cesaret eksikliğini, yüreği yokmuş veya zayıfmış gibi kurulan nitelemeyle birlikte verir.","boundary_detail":"Gerçek organ yokluğu, yüreğin yaralanması veya hastalanması ve yalın organ adı bu dalın anlamına girmez.","branch_image_ar":"ضعف الفؤاد حتى كأنه لا فؤاد له","concept_gloss":"yüreksiz ve korkak kişi","contextual_glosses":[{"applicability":"Kişinin korkaklığını yürek yokluğu anlatımıyla kısa biçimde nitelemek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Cesaret eksikliğini ve yürek yokluğu üzerinden kurulan anlatımı korur."},"facet_ids":["F001","F002"],"text":"yüreksiz","usage_role":"general"},{"applicability":"Bağlam yalnızca kişinin korkaklığını öne çıkarıyorsa doğal bir nitelemedir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yüreğin yokluğu veya zayıflığı üzerinden kurulan özgün anlatımı görünür kılmaz.","preserves":"Kişinin belirgin korkaklık ve cesaretsizlik özelliğini korur."},"facet_ids":["F001"],"text":"ödlek","usage_role":"contextual"}],"definition":"Bir kişiyi yüreği yokmuş ya da yüreği zayıfmış gibi düşünerek cesaretsiz ve korkak diye niteler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, korku karşısında cesaret gösteremeyen ve geri duran biri olarak nitelenir."},{"facet_id":"F002","role":"specialization","statement":"Korkaklık, kişinin yüreği yokmuş veya yüreği güçsüzmüş gibi kurulan bir anlatımla belirtilir."}],"identity_rationale":"Kaynak ifadesi kişiyi yüreği yokmuş veya yüreği zayıfmış gibi niteleyerek korkaklık anlamına ulaşır. Verilen dal çerçevesi bu nitelemeyi bedensel organ kaybı ya da hastalık diye yorumlamadan, kişilik ve davranış özelliği olarak doğru biçimde sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yüreği zayıf, yüreksiz ve korkak kimse"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yüreksiz veya yüreği zayıf kimse"}],"lexicalization_note":"Dal, kişiyi yüreksiz veya yüreği zayıf sayan yalın nitelemeyi tanımlar; organ yaralanması ve hastalık anlamları buraya aktarılmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; genel korkaklık, yaygın korku, ani korku sarsıntısı ve geniş güçsüzlük alanlarıyla en yararlı dört sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal korkak kişiye yönelik yürek temelli nitelemeyle sınırlıdır; komşu dal korkaklık özelliğini ve bu özelliğin kişiye yüklenmesini daha genel biçimde kapsar.","focus_only":"Bu dal korkak kişiyi yüreği yokmuş veya yüreği zayıfmış gibi kurulan özel bir anlatımla niteler.","gloss":"korkaklık ve korkak kişi","neighbor_only":"Komşu dal korkaklık özelliğini, kişiye korkak deme eylemini ve çocuğun kişiyi korkaklaştırması düşüncesini de kapsar.","neighbor_ref":"root_000218/B002","relation_type":"near_synonym","shared_zone":"İki dal da kişinin cesaret eksikliğini ve korkak oluşunu anlatır."},{"boundary_match":"partial","distinction":"Bu dal yerleşik bir kişilik niteliğini yürek temelli anlatır; komşu dal ise belirli bir şey karşısında duyulan korku ve ürkmeyi de kapsayan daha geniş bir durum alanıdır.","focus_only":"Bu dal kişiyi yüreği yokmuş veya zayıfmış gibi niteleyen adlandırmayı öne çıkarır.","gloss":"korkaklık ve korku","neighbor_only":"Komşu dal herhangi bir şey karşısındaki korku ve ürkmeyi genel olarak kapsar.","neighbor_ref":"root_001625/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da korku karşısında cesaret gösterememe alanında örtüşür."},{"boundary_match":"partial","distinction":"Bu dal kişiyi korkak diye niteler; komşu dal ise ani korku sarsıntısı ve buna eşlik edebilen şaşkınlık ya da düşünce bozukluğu durumlarını anlatır.","focus_only":"Bu dal sürekli bir cesaret eksikliğini, yürek yokluğu veya zayıflığı üzerinden kişiye yükler.","gloss":"korku karşısında yürek zayıflığı","neighbor_only":"Komşu dal korkudan yüreğin yerinden çıkması gibi ani sarsılmayı, şaşkınlığı ve düşünce bozukluğunu da kapsar.","neighbor_ref":"root_000432/B009","relation_type":"near_neighbor","shared_zone":"İki dal da korkunun yürek üzerindeki etkisi üzerinden korkaklık alanına yaklaşır."},{"boundary_match":"partial","distinction":"Bu dalın zayıflığı cesaret alanındadır; komşu dal ise bedensel güçsüzlük, incelik ve düşkünlük gibi daha geniş zayıflık türlerini de içerir.","focus_only":"Bu dal yalnızca kişideki cesaret eksikliğini yürek temelli bir nitelemeyle anlatır.","gloss":"güçsüzlük ve korkaklık","neighbor_only":"Komşu dal insan, topluluk ve devenin bedensel güçsüzlüğünü, inceliğini ve ihtiyaçtan düşkünlüğü de kapsar.","neighbor_ref":"root_000908/B003","relation_type":"near_neighbor","shared_zone":"İki dal korkaklığı bir tür güçsüzlük olarak anlatabilir."}],"source_phrase_ar":"رجل مفؤود وفئيد لا فؤاد له (sihah)؛ المفؤود الضعيف الفؤاد الجبان مثل المنخوب (tahdhib)","source_summary":"Kaynaklar kişiyi yüreği yokmuş ya da yüreği zayıfmış gibi niteleyen biçimleri korkak ve cesaretsiz kimse anlamında birleştirir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه المفؤود أو الفئيد بمعنى لا فؤاد له، أو الضعيف الفؤاد الجبان.","what_is_not_ar":"لا يدخل فيه إصابة الصيد في فؤاده، ولا داء الفؤاد الجسدي، ولا الفؤاد بوصفه اسما للقلب."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["104:7:1"],"branch_refs":[],"candidate_id":"cand_3589131a1658e2f9079b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:7:1:defining-relative-action","source_type":"word_analysis","support_ids":["sup_75d4a528d25cdb6c356e","sup_e65802ea15faf9f59173"],"title":"the relative clause defines the fire","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:7:1","qac_refs":["104:7:1:1"],"status":"accepted"}},{"anchor_refs":["104:7:1"],"branch_refs":[],"candidate_id":"cand_267dfd45eee46fadb424","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:7:1:feminine-cross-ayah-antecedent","source_type":"word_analysis","support_ids":["sup_35430d919cb5dc3bcd26","sup_e65802ea15faf9f59173"],"title":"feminine agreement carries the fire forward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:7:1","qac_refs":["104:7:1:1"],"status":"accepted"}},{"anchor_refs":["104:7:2"],"branch_refs":[],"candidate_id":"cand_6ec56cdbef735a356e16","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000945"],"scope":"focus_ayah","source_local_id":"104:7:2:feminine-fire-agency","source_type":"word_analysis","support_ids":["sup_4f73d859ed3a4a8bd8cf","sup_d50d116dd438ddc854cb"],"title":"the fire acts through hidden agreement","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:7:2","qac_refs":["104:7:2:1"],"status":"accepted"}},{"anchor_refs":["104:7:2"],"branch_refs":[],"candidate_id":"cand_48f43fbc5581d01d3441","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000945"],"scope":"focus_ayah","source_local_id":"104:7:2:form-viii-self-directed-pressure","source_type":"word_analysis","support_ids":["sup_a9c1e4c998d4adcab861","sup_d50d116dd438ddc854cb"],"title":"derived form makes the motion deliberate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:7:2","qac_refs":["104:7:2:1"],"status":"accepted"}},{"anchor_refs":["104:7:2"],"branch_refs":[],"candidate_id":"cand_5870499a8db7c8db5e7a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000945"],"scope":"focus_ayah","source_local_id":"104:7:2:inner-to-enclosing-bridge","source_type":"word_analysis","support_ids":["sup_d50d116dd438ddc854cb","sup_e996577f164ed8549b37"],"title":"inner exposure anticipates enclosure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:7:2","qac_refs":["104:7:2:1"],"status":"accepted"}},{"anchor_refs":["104:7:2"],"branch_refs":[],"candidate_id":"cand_428e788bf58ceef1cb29","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000945"],"scope":"focus_ayah","source_local_id":"104:7:2:lexical-images-of-exposure","source_type":"word_analysis","support_ids":["sup_3e10d504a4665bbcb9c2","sup_d50d116dd438ddc854cb"],"title":"root images sharpen exposure without replacing the frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:7:2","qac_refs":["104:7:2:1"],"status":"accepted"}},{"anchor_refs":["104:7:2"],"branch_refs":[],"candidate_id":"cand_cbd8f96b6b3b28acb196","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000945"],"scope":"focus_ayah","source_local_id":"104:7:2:ongoing-verbal-animation","source_type":"word_analysis","support_ids":["sup_01ad7505cc069fd7c91b","sup_d50d116dd438ddc854cb"],"title":"the named fire becomes ongoing action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:7:2","qac_refs":["104:7:2:1"],"status":"accepted"}},{"anchor_refs":["104:7:2"],"branch_refs":[],"candidate_id":"cand_0e39c1ef60d9d82ea1f0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000945"],"scope":"focus_ayah","source_local_id":"104:7:2:rising-inspection-frame","source_type":"word_analysis","support_ids":["sup_1480fcdfaf17aee95219","sup_d50d116dd438ddc854cb"],"title":"rising and knowing work together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:7:2","qac_refs":["104:7:2:1"],"status":"accepted"}},{"anchor_refs":["104:7:2"],"branch_refs":[],"candidate_id":"cand_c5661774ca31265e6d14","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000945"],"scope":"focus_ayah","source_local_id":"104:7:2:sound-pressure-path","source_type":"word_analysis","support_ids":["sup_942d828b44e863eab9d3","sup_d50d116dd438ddc854cb"],"title":"the sound path presses toward the target","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:7:2","qac_refs":["104:7:2:1"],"status":"accepted"}},{"anchor_refs":["104:7:3"],"branch_refs":[],"candidate_id":"cand_56c3c175cd16f1e16a48","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:7:3:audible-bound-preposition","source_type":"word_analysis","support_ids":["sup_0f3506e818f6d1920c3b","sup_c51ff26e32636f812ff4"],"title":"sound and liaison bind the phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:7:3","qac_refs":["104:7:3:1"],"status":"accepted"}},{"anchor_refs":["104:7:3"],"branch_refs":[],"candidate_id":"cand_e9314a0dfb5884dc38a3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:7:3:forward-upon-reprise","source_type":"word_analysis","support_ids":["sup_496ccb82c2416a534b32","sup_c51ff26e32636f812ff4"],"title":"uponness continues into 104:8","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:7:3","qac_refs":["104:7:3:1"],"status":"accepted"}},{"anchor_refs":["104:7:3"],"branch_refs":[],"candidate_id":"cand_89444699576a022ca437","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:7:3:upon-domain-dominance","source_type":"word_analysis","support_ids":["sup_b3a5658bbc9275a77e18","sup_c51ff26e32636f812ff4"],"title":"uponness makes the hearts a governed domain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:7:3","qac_refs":["104:7:3:1"],"status":"accepted"}},{"anchor_refs":["104:7:3"],"branch_refs":[],"candidate_id":"cand_5a13319aed4a65fe0b2f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:7:3:verb-target-hinge","source_type":"word_analysis","support_ids":["sup_c51ff26e32636f812ff4","sup_d74a34476ea01e3b6aea"],"title":"the preposition completes the verb's reach","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:7:3","qac_refs":["104:7:3:1"],"status":"accepted"}},{"anchor_refs":["104:7:4"],"branch_refs":[],"candidate_id":"cand_7752bb7f5e16d6ea2bd7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:7:4:audible-caught-closure","source_type":"word_analysis","support_ids":["sup_b0b762c9cd7e93d8d10b","sup_bdcbec4e0a4c4aa47314"],"title":"the final target catches in recitation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:7:4","qac_refs":["104:7:4:1","104:7:4:2"],"status":"accepted"}},{"anchor_refs":["104:7:4"],"branch_refs":[],"candidate_id":"cand_d62442711d903560c462","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:7:4:final-target-structure","source_type":"word_analysis","support_ids":["sup_15b4bcb7f536929f3d9c","sup_b0b762c9cd7e93d8d10b"],"title":"the clause ends on the inner target","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:7:4","qac_refs":["104:7:4:1","104:7:4:2"],"status":"accepted"}},{"anchor_refs":["104:7:4"],"branch_refs":[],"candidate_id":"cand_852c4962c2164ebc7931","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:7:4:governed-definite-broken-plural","source_type":"word_analysis","support_ids":["sup_b0b762c9cd7e93d8d10b","sup_ffb7490a7ae2772d4321"],"title":"the hearts are governed, plural, and definite","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:7:4","qac_refs":["104:7:4:1","104:7:4:2"],"status":"accepted"}},{"anchor_refs":["104:7:4"],"branch_refs":[],"candidate_id":"cand_6ea7676a736653228082","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:7:4:heat-root-fire-echo","source_type":"word_analysis","support_ids":["sup_957c3977bd54960404ad","sup_b0b762c9cd7e93d8d10b"],"title":"the heart term answers the kindled fire","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:7:4","qac_refs":["104:7:4:1","104:7:4:2"],"status":"accepted"}},{"anchor_refs":["104:7:4"],"branch_refs":[],"candidate_id":"cand_cad95e225d4125359c61","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:7:4:inner-perceptive-core","source_type":"word_analysis","support_ids":["sup_85bf9e1c01f9b97caba2","sup_b0b762c9cd7e93d8d10b"],"title":"fuʾād names the inner truth-processing core","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:7:4","qac_refs":["104:7:4:1","104:7:4:2"],"status":"accepted"}},{"anchor_refs":["104:7:4"],"branch_refs":[],"candidate_id":"cand_c142480e1d20f4988bbd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:7:4:inner-to-whole-person-bridge","source_type":"word_analysis","support_ids":["sup_77b9ac0f1ab041ed0c58","sup_b0b762c9cd7e93d8d10b"],"title":"inner exposure opens toward enclosure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:7:4","qac_refs":["104:7:4:1","104:7:4:2"],"status":"accepted"}},{"anchor_refs":["104:7:4"],"branch_refs":[],"candidate_id":"cand_0ae1f1fb43246ae0dd15","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:7:4:upon-surface-and-inner-core","source_type":"word_analysis","support_ids":["sup_9dea79a7304e02eda4a3","sup_b0b762c9cd7e93d8d10b"],"title":"uponness reaches surface and interior","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:7:4","qac_refs":["104:7:4:1","104:7:4:2"],"status":"accepted"}},{"anchor_refs":["104:7:2"],"branch_refs":[],"candidate_id":"cand_b4ce1b5ecaba909f0311","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000945"],"scope":"focus_ayah","source_local_id":"104:7:2:1","source_type":"qac_morpheme","support_ids":["sup_446e2aacc6ad3401ede4"],"title":"QAC root occurrence: ط ل ع","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["104:7:4"],"branch_refs":[],"candidate_id":"cand_8aff9d3e4f9b76557384","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001122"],"scope":"focus_ayah","source_local_id":"104:7:4:2","source_type":"qac_morpheme","support_ids":["sup_7038e718ebce28029b6a"],"title":"QAC root occurrence: ف ء د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["104:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:7","branch_refs":["root_000945/B003","root_001122/B003"],"candidate_id":"cand_ad302f8ba4c2b6a17cf3","commentary_obligation":"review","hft_ref":"hft_07fd357d1b66a4f96fe3","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_inner_overlook","source_type":"hft","support_ids":["sup_98e597d3e35b9f3560e7"],"title":"baseline_inner_overlook","trust":"legacy_unbound"},{"anchor_refs":["104:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:7","branch_refs":["root_000945/B001","root_001122/B001","root_001122/B002"],"candidate_id":"cand_e1df5c3a8a59383c8023","commentary_obligation":"review","hft_ref":"hft_2226c9e886c5215ea536","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_rising_inner_kindling","source_type":"hft","support_ids":["sup_59bf448e19e2f7b95ddd"],"title":"baseline_rising_inner_kindling","trust":"legacy_unbound"},{"anchor_refs":["104:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:7","branch_refs":["root_000945/B007","root_001122/B002"],"candidate_id":"cand_caf4e4e414bb796a9b72","commentary_obligation":"review","hft_ref":"hft_8f47314d6be6c19c45d3","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_exhaustive_saturation","source_type":"hft","support_ids":["sup_3a87576985803bb9eeaa"],"title":"baseline_exhaustive_saturation","trust":"legacy_unbound"},{"anchor_refs":["104:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:7","branch_refs":["root_000945/B010","root_001122/B003"],"candidate_id":"cand_203f9396538e8f231cd2","commentary_obligation":"review","hft_ref":"hft_01e5e8073db113275c29","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_overshot_heart_target","source_type":"hft","support_ids":["sup_346ed1969d08296d679a"],"title":"baseline_overshot_heart_target","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ","qac_morphemes":[{"lemma_ar":"ٱلَّذِى","morph_features":"STEM|POS:REL|LEM:{l~a*iY|FS","morpheme_role":"STEM","pos":"REL","qac_ref":"104:7:1:1","qac_word_ref":"104:7:1","root_ar":"","surface_ar":"ٱلَّتِى"},{"lemma_ar":"طَّلَعَ","morph_features":"STEM|POS:V|IMPF|(VIII)|LEM:T~alaEa|ROOT:TlE|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"104:7:2:1","qac_word_ref":"104:7:2","root_ar":"ط ل ع","surface_ar":"تَطَّلِعُ"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"104:7:3:1","qac_word_ref":"104:7:3","root_ar":"","surface_ar":"عَلَى"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"104:7:4:1","qac_word_ref":"104:7:4","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"فُؤَاد","morph_features":"STEM|POS:N|LEM:fu&aAd|ROOT:fAd|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:7:4:2","qac_word_ref":"104:7:4","root_ar":"ف ء د","surface_ar":"أَفْـِٔدَةِ"}],"word_analysis_qac_refs":[["104:7:1:1"],["104:7:2:1"],["104:7:3:1"],["104:7:4:1","104:7:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["104:7:1","104:7:2","104:7:3","104:7:4"]},"focus_surface_evidence":{"arabic_uthmani":"ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ","qac_morphemes":[{"lemma_ar":"ٱلَّذِى","morph_features":"STEM|POS:REL|LEM:{l~a*iY|FS","morpheme_role":"STEM","pos":"REL","qac_ref":"104:7:1:1","qac_word_ref":"104:7:1","root_ar":"","surface_ar":"ٱلَّتِى"},{"lemma_ar":"طَّلَعَ","morph_features":"STEM|POS:V|IMPF|(VIII)|LEM:T~alaEa|ROOT:TlE|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"104:7:2:1","qac_word_ref":"104:7:2","root_ar":"ط ل ع","surface_ar":"تَطَّلِعُ"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"104:7:3:1","qac_word_ref":"104:7:3","root_ar":"","surface_ar":"عَلَى"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"104:7:4:1","qac_word_ref":"104:7:4","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"فُؤَاد","morph_features":"STEM|POS:N|LEM:fu&aAd|ROOT:fAd|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:7:4:2","qac_word_ref":"104:7:4","root_ar":"ف ء د","surface_ar":"أَفْـِٔدَةِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["104:7:1:1"],["104:7:2:1"],["104:7:3:1"],["104:7:4:1","104:7:4:2"]],"word_analysis_refs":["104:7:1","104:7:2","104:7:3","104:7:4"],"word_rows":[{"analysis_record_ref":"104:7:1","analytic_gloss_range_en":"feminine singular relative pronoun carrying the prior fire description into a defining verbal clause","analytic_root_gloss_range_en":null,"qac_refs":["104:7:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"ٱلَّتِى","transliteration":"allatī"}},{"analysis_record_ref":"104:7:2","analytic_gloss_range_en":"Form VIII imperfect action of rising upon and becoming aware of the hearts through the preposition","analytic_root_gloss_range_en":"root range includes rising, appearing, overlooking, scouting, and emergence; the local verb selects the rising-inspection branch and narrows other images to secondary pressure","qac_refs":["104:7:2:1"],"root":{"arabic":"ط ل ع","transliteration":"ṭ-l-ʿ"},"surface":{"arabic":"تَطَّلِعُ","transliteration":"taṭṭaliʿu"}},{"analysis_record_ref":"104:7:3","analytic_gloss_range_en":"preposition of uponness, dominance, directed contact, and inspected domain","analytic_root_gloss_range_en":null,"qac_refs":["104:7:3:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"عَلَى","transliteration":"ʿalā"}},{"analysis_record_ref":"104:7:4","analytic_gloss_range_en":"definite broken plural of fuʾād, the inner cognitive-emotional cores, governed by the preposition as the fire's target","analytic_root_gloss_range_en":"root-family evidence supplied in CRITICAL links the heart term with inner perception, emotion, and heat/kindling imagery; V4 has no available rows for this root, so root images are retained where locally supported but not made to replace the noun's heart sense","qac_refs":["104:7:4:1","104:7:4:2"],"root":{"arabic":"ف أ د","transliteration":"f-ʾ-d"},"surface":{"arabic":"ٱلْأَفْـِٔدَةِ","transliteration":"al-afʾidati"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["104:7"],"branch_refs":["root_000945/B003","root_001122/B003"],"candidate_id":"cand_ad302f8ba4c2b6a17cf3","evidence_scope":"focus_ayah","hft_ref":"hft_07fd357d1b66a4f96fe3","item_id":"baseline_inner_overlook","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_inner_overlook","support_id":"sup_98e597d3e35b9f3560e7"},{"anchor_refs":["104:7"],"branch_refs":["root_000945/B001","root_001122/B001","root_001122/B002"],"candidate_id":"cand_e1df5c3a8a59383c8023","evidence_scope":"focus_ayah","hft_ref":"hft_2226c9e886c5215ea536","item_id":"baseline_rising_inner_kindling","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_rising_inner_kindling","support_id":"sup_59bf448e19e2f7b95ddd"},{"anchor_refs":["104:7"],"branch_refs":["root_000945/B007","root_001122/B002"],"candidate_id":"cand_caf4e4e414bb796a9b72","evidence_scope":"focus_ayah","hft_ref":"hft_8f47314d6be6c19c45d3","item_id":"baseline_exhaustive_saturation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_exhaustive_saturation","support_id":"sup_3a87576985803bb9eeaa"},{"anchor_refs":["104:7"],"branch_refs":["root_000945/B010","root_001122/B003"],"candidate_id":"cand_203f9396538e8f231cd2","evidence_scope":"focus_ayah","hft_ref":"hft_01e5e8073db113275c29","item_id":"baseline_overshot_heart_target","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_overshot_heart_target","support_id":"sup_346ed1969d08296d679a"}],"diagnostics":[],"lane_counts":{"global":9,"macro":13,"micro":4},"packet_summary":{"ayah_count":9,"focus_ref":"104:7","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"و ص د","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000036","furuq_root_norm":"ء ص د","furuq_source_root_norm":"أ ص د","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001653","furuq_root_norm":"و ص د","furuq_source_root_norm":"و ص د","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:8","104:9"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"104:7","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":17,"unstructured_record_count":0},"identity":{"ayah_ref":"104:7","lane":"micro","linguistic_source_ref":"104:7","surface_ref":"104:7","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"104:7","target_tokens":[["Yüreklere",["104:7:3","104:7:4"]],["ulaşan",["104:7:1","104:7:2"]]],"text":"Yüreklere ulaşan."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":9,"id":"s104-p01-001-009","label":"Whole surah","number":1,"refs":["104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:8","104:9"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:2:ongoing-verbal-animation","source_type":"word_analysis","support_id":"sup_01ad7505cc069fd7c91b","text":"{\"blocking_evidence\":null,\"headline\":\"the named fire becomes ongoing action\",\"reader_payoff\":\"The reader notices the movement from the prior named fire to an imperfect verb that keeps the fire's exposing action in progress.\",\"reason\":\"The verb is finite imperfect inside the relative clause, so the CRITICAL rows about the shift from nominal identification to continuing action are locally supported.\",\"representative_source_ids\":[\"QF-d25ce54c\",\"QT-1f40ca6d\",\"QB-f29f20da\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:3:audible-bound-preposition","source_type":"word_analysis","support_id":"sup_0f3506e818f6d1920c3b","text":"{\"blocking_evidence\":null,\"headline\":\"sound and liaison bind the phrase\",\"reader_payoff\":\"The reader notices that the repeated guttural and recitational liaison make the preposition sound joined both to the verb before it and to the heart noun after it.\",\"reason\":\"The adjacent forms place {{ar:ع}} ({{tr:ʿ}}) at the verb-preposition boundary and join {{ar:عَلَى}} ({{tr:ʿalā}}) into the following definite noun in recitation.\",\"representative_source_ids\":[\"QE-25ae7778\",\"QP-7d2da355\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:2:rising-inspection-frame","source_type":"word_analysis","support_id":"sup_1480fcdfaf17aee95219","text":"{\"blocking_evidence\":null,\"headline\":\"rising and knowing work together\",\"reader_payoff\":\"The reader notices that {{ar:تَطَّلِعُ}} ({{tr:taṭṭaliʿu}}) does not choose between physical ascent and cognitive discovery; with {{ar:عَلَى}} ({{tr:ʿalā}}), it makes the fire mount over the hearts in order to inspect them.\",\"reason\":\"The local frame is intransitive with a {{ar:عَلَى}} ({{tr:ʿalā}})-governed complement, and V4 preserves branches for rising and looking into a matter; this supports a combined ascent-inspection reading without turning the hearts into a direct object.\",\"representative_source_ids\":[\"QG-b96a6dd5\",\"QS-d972a8d0\",\"QI-018a8815\",\"QY-4c635131\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:4:final-target-structure","source_type":"word_analysis","support_id":"sup_15b4bcb7f536929f3d9c","text":"{\"blocking_evidence\":null,\"headline\":\"the clause ends on the inner target\",\"reader_payoff\":\"The reader notices that the ayah delays its target until the final word, so the clause moves from the fire's identity to action to the inner human core.\",\"reason\":\"The full local clause runs from relative pronoun to verb to preposition and closes on {{ar:ٱلْأَفْـِٔدَةِ}} ({{tr:al-afʾidati}}), supporting the CRITICAL structural rows.\",\"representative_source_ids\":[\"QT-0b234de2\",\"QT-c0797d64\",\"QB-f636a8a8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:1:feminine-cross-ayah-antecedent","source_type":"word_analysis","support_id":"sup_35430d919cb5dc3bcd26","text":"{\"blocking_evidence\":null,\"headline\":\"feminine agreement carries the fire forward\",\"reader_payoff\":\"The reader notices that {{ar:ٱلَّتِى}} ({{tr:allatī}}) forces the previous feminine fire description to remain grammatically active across the ayah break.\",\"reason\":\"QAC and attachment evidence identify {{ar:ٱلَّتِى}} ({{tr:allatī}}) as a feminine singular relative pronoun whose antecedent is the immediately prior fire description, so the CRITICAL boundary and concord claims are locally licensed.\",\"representative_source_ids\":[\"QG-4a3f629f\",\"QG-8a505545\",\"QG-c61d662e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:2:lexical-images-of-exposure","source_type":"word_analysis","support_id":"sup_3e10d504a4665bbcb9c2","text":"{\"blocking_evidence\":null,\"headline\":\"root images sharpen exposure without replacing the frame\",\"reader_payoff\":\"The reader notices that scouting, emergence, and reading images make the fire's inspection feel like exposure of what was hidden, while the local grammar keeps ascent upon and awareness of the hearts as the selected sense.\",\"reason\":\"V4 accepts branches for overlooking, scouting, plant emergence, and access, but the local Form VIII plus {{ar:عَلَى}} ({{tr:ʿalā}}) frame selects inspection and rising; the extra images can color the exposure without becoming separate local senses.\",\"representative_source_ids\":[\"QS-4a8c9894\",\"QS-5da6b52c\",\"QS-f1c1f0d5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"104:7:2:1","source_type":"qac_morpheme","support_id":"sup_446e2aacc6ad3401ede4","text":"{\"lemma_ar\":\"طَّلَعَ\",\"morph_features\":\"STEM|POS:V|IMPF|(VIII)|LEM:T~alaEa|ROOT:TlE|3FS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"104:7:2:1\",\"qac_word_ref\":\"104:7:2\",\"root_ar\":\"ط ل ع\",\"surface_ar\":\"تَطَّلِعُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:3:forward-upon-reprise","source_type":"word_analysis","support_id":"sup_496ccb82c2416a534b32","text":"{\"blocking_evidence\":null,\"headline\":\"uponness continues into 104:8\",\"reader_payoff\":\"The reader notices that the relation placed upon the hearts in 104:7 expands to the people in {{ar:عَلَيْهِم}} ({{tr:ʿalayhim}}) (104:8).\",\"reason\":\"The CRITICAL forward bridge is coherent with the repeated {{ar:عَلَى}} ({{tr:ʿalā}})-base in the next ayah and does not alter the local parse.\",\"representative_source_ids\":[\"QB-84e7b4fa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:2:feminine-fire-agency","source_type":"word_analysis","support_id":"sup_4f73d859ed3a4a8bd8cf","text":"{\"blocking_evidence\":null,\"headline\":\"the fire acts through hidden agreement\",\"reader_payoff\":\"The reader notices that the verb itself carries the prior fire as acting subject, so the fire does not need to be renamed in order to remain the agent.\",\"reason\":\"The verb is third feminine singular and the attachment evidence links its subject role to {{ar:ٱلَّتِى}} ({{tr:allatī}}), whose antecedent is the prior fire description.\",\"representative_source_ids\":[\"QG-00ec3588\",\"QG-09f16cc4\",\"QG-8e286e10\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"104:7:4:2","source_type":"qac_morpheme","support_id":"sup_7038e718ebce28029b6a","text":"{\"lemma_ar\":\"فُؤَاد\",\"morph_features\":\"STEM|POS:N|LEM:fu&aAd|ROOT:fAd|MP|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"104:7:4:2\",\"qac_word_ref\":\"104:7:4\",\"root_ar\":\"ف ء د\",\"surface_ar\":\"أَفْـِٔدَةِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:1:defining-relative-action","source_type":"word_analysis","support_id":"sup_75d4a528d25cdb6c356e","text":"{\"blocking_evidence\":null,\"headline\":\"the relative clause defines the fire\",\"reader_payoff\":\"The reader notices that the clause does not merely add information after the fire; it identifies the fire as the one whose characteristic action is to rise and inspect.\",\"reason\":\"The local clause is a relative verbal span introduced by {{ar:ٱلَّتِى}} ({{tr:allatī}}), with {{ar:تَطَّلِعُ}} ({{tr:taṭṭaliʿu}}) as predicate; this supports the CRITICAL claim that action becomes identifying description.\",\"representative_source_ids\":[\"QS-e1c81cc3\",\"QT-4225f5f5\",\"QT-cf222d42\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:4:inner-to-whole-person-bridge","source_type":"word_analysis","support_id":"sup_77b9ac0f1ab041ed0c58","text":"{\"blocking_evidence\":null,\"headline\":\"inner exposure opens toward enclosure\",\"reader_payoff\":\"The reader notices that 104:7 ends on the inner hearts before 104:8 extends the same upon-relation to the people themselves.\",\"reason\":\"The CRITICAL bridge is concrete and local: {{ar:ٱلْأَفْـِٔدَةِ}} ({{tr:al-afʾidati}}) closes 104:7, and {{ar:عَلَيْهِم}} ({{tr:ʿalayhim}}) resumes the upon-relation in 104:8.\",\"representative_source_ids\":[\"QB-ed587dfd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:4:inner-perceptive-core","source_type":"word_analysis","support_id":"sup_85bf9e1c01f9b97caba2","text":"{\"blocking_evidence\":null,\"headline\":\"fuʾād names the inner truth-processing core\",\"reader_payoff\":\"The reader notices that the fire targets the innermost perceiving and feeling core, not a generic heart-container.\",\"reason\":\"The QAC grammar explicitly distinguishes fuʾād from a generic heart term as the innermost cognitive-emotional core; contextual evidence places the noun in perception-related distributions, while missing V4 rows for {{ar:ف أ د}} ({{tr:f-ʾ-d}}) do not block the CRITICAL lexical evidence.\",\"representative_source_ids\":[\"QS-85caeaa8\",\"QS-d8379b6c\",\"QI-20bb7d26\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:2:sound-pressure-path","source_type":"word_analysis","support_id":"sup_942d828b44e863eab9d3","text":"{\"blocking_evidence\":null,\"headline\":\"the sound path presses toward the target\",\"reader_payoff\":\"The reader notices that the doubled emphatic stop and guttural release make the verb sound compressed before it moves into the preposition and target.\",\"reason\":\"The surface form has a shaddah on {{ar:ط}} ({{tr:ṭ}}) and ends in {{ar:ع}} ({{tr:ʿ}}), matching the CRITICAL sound rows without requiring a new lexical sense.\",\"representative_source_ids\":[\"QF-aaaad616\",\"QP-2c37fb60\",\"QP-86001b1c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:4:heat-root-fire-echo","source_type":"word_analysis","support_id":"sup_957c3977bd54960404ad","text":"{\"blocking_evidence\":null,\"headline\":\"the heart term answers the kindled fire\",\"reader_payoff\":\"The reader notices that the fire reaches a heart word whose supplied root-family evidence carries heat and kindling, while the local noun still denotes inner hearts rather than roasted matter.\",\"reason\":\"The CRITICAL rows supply Lane and Lisan heat evidence and the nearby context is explicitly the kindled fire in 104:6; because V4 has no rows for {{ar:ف أ د}} ({{tr:f-ʾ-d}}) and the QAC sense is still hearts, the heat image survives as a narrowed lexical echo.\",\"representative_source_ids\":[\"QS-65c96f07\",\"QE-7db195ec\",\"QY-dbc45779\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:4:upon-surface-and-inner-core","source_type":"word_analysis","support_id":"sup_9dea79a7304e02eda4a3","text":"{\"blocking_evidence\":null,\"headline\":\"uponness reaches surface and interior\",\"reader_payoff\":\"The reader notices that {{ar:عَلَى}} ({{tr:ʿalā}}) can stage contact upon the heart while the fuʾād sense keeps the target deeply interior.\",\"reason\":\"The reported covering sense is not allowed to replace the local noun's inner-core meaning, but it coheres with the preposition's upon-relation and the noun's interior target.\",\"representative_source_ids\":[\"QS-fe5f4d4f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:2:form-viii-self-directed-pressure","source_type":"word_analysis","support_id":"sup_a9c1e4c998d4adcab861","text":"{\"blocking_evidence\":null,\"headline\":\"derived form makes the motion deliberate\",\"reader_payoff\":\"The reader notices that the fused Form VIII shape makes the fire itself the seeker or inspector, not merely something that rises or causes disclosure for someone else.\",\"reason\":\"QAC flags the local morphology as Form VIII despite a compact tag mismatch, with assimilation of the Form VIII marker into {{ar:ط}} ({{tr:ṭ}}); this licenses deliberate self-involved inspection and blocks a bare Form I or causative Form IV replacement.\",\"representative_source_ids\":[\"QS-0f2f855f\",\"QF-44d7cc0e\",\"QF-605d3f2a\",\"QF-b793fdfc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:4","source_type":"word_analysis","support_id":"sup_b0b762c9cd7e93d8d10b","text":"{\"gloss_range\":\"definite broken plural of fuʾād, the inner cognitive-emotional cores, governed by the preposition as the fire's target\",\"prose\":\"{{ar:ٱلْأَفْـِٔدَةِ}} ({{tr:al-afʾidati}}) is where the clause lands. It is genitive inside {{ar:عَلَى ٱلْأَفْـِٔدَةِ}} ({{tr:ʿalā al-afʾidati}}), so the hearts are reached through a preposition rather than seized as a direct object. The definite broken plural makes the target both multiple and gathered as a known class: many inner cores, not one archetypal heart and not a vague mass. The selected noun is fuʾād rather than a generic heart term, so the fire reaches the deepest cognitive-emotional core, the seat that feels and processes truth; the contrast with the broader heart-container is visible in 28:10, and the truth-validation use of fuʾād in 53:11 sharpens the diagnostic force here. The upon-relation stages contact at the surface while the fuʾād sense keeps the target deeply interior. The heat and kindling associations supplied for {{ar:ف أ د}} ({{tr:f-ʾ-d}}) remain a narrowed but real pressure: the word still denotes hearts, yet in the wake of {{ar:نَارُ ٱللَّهِ ٱلْمُوقَدَةُ}} ({{tr:nāru llāhi al-mūqadah}}) (104:6) the target itself carries an inner burning echo. Its final position and internal hamza make the ayah close on a caught, pierced-sounding inner target before 104:8 expands the upon-relation from hearts to persons.\",\"root_display\":\"{{ar:ف أ د}} ({{tr:f-ʾ-d}})\",\"root_gloss_range\":\"root-family evidence supplied in CRITICAL links the heart term with inner perception, emotion, and heat/kindling imagery; V4 has no available rows for this root, so root images are retained where locally supported but not made to replace the noun's heart sense\",\"surface_display\":\"{{ar:ٱلْأَفْـِٔدَةِ}} ({{tr:al-afʾidati}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:3:upon-domain-dominance","source_type":"word_analysis","support_id":"sup_b3a5658bbc9275a77e18","text":"{\"blocking_evidence\":null,\"headline\":\"uponness makes the hearts a governed domain\",\"reader_payoff\":\"The reader notices that {{ar:عَلَى}} ({{tr:ʿalā}}) makes the hearts a domain under the fire's superiority and inspection, not merely a location where fire exists.\",\"reason\":\"QAC and attachment evidence show {{ar:عَلَى}} ({{tr:ʿalā}}) governing {{ar:ٱلْأَفْـِٔدَةِ}} ({{tr:al-afʾidati}}) as the complement of {{ar:تَطَّلِعُ}} ({{tr:taṭṭaliʿu}}), while contextual valency allows this preposition with the exact root-form frame.\",\"representative_source_ids\":[\"QG-151c9537\",\"QG-f9c1b13f\",\"QS-6d61b174\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:4:audible-caught-closure","source_type":"word_analysis","support_id":"sup_bdcbec4e0a4c4aa47314","text":"{\"blocking_evidence\":null,\"headline\":\"the final target catches in recitation\",\"reader_payoff\":\"The reader notices that the internal hamza and hard consonants make the final heart word sound caught and impacted at the clause's endpoint.\",\"reason\":\"The written and recited form includes an internal hamza and a dāl before the ending, so the sound-shape claim is anchored in the local surface.\",\"representative_source_ids\":[\"QF-c70b06ae\",\"QP-2038d27f\",\"QP-e24a5ba6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:3","source_type":"word_analysis","support_id":"sup_c51ff26e32636f812ff4","text":"{\"gloss_range\":\"preposition of uponness, dominance, directed contact, and inspected domain\",\"prose\":\"{{ar:عَلَى}} ({{tr:ʿalā}}) is the hinge inside {{ar:تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ}} ({{tr:taṭṭaliʿu ʿalā al-afʾidati}}). It does not place the fire merely inside the hearts; it gives the action an upon-relation, with superiority, directed contact, and an inspected domain all present at once. The particle therefore holds the spatial and cognitive sides of the verb together: the fire is over or upon the hearts, and those hearts are what it comes to know. Its sound also binds the phrase locally, as the final guttural of the verb is answered by the opening guttural of the particle, and recitational liaison joins the particle to its definite heart-noun complement. The relation continues in {{ar:عَلَيْهِم}} ({{tr:ʿalayhim}}) (104:8).\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:عَلَى}} ({{tr:ʿalā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:2","source_type":"word_analysis","support_id":"sup_d50d116dd438ddc854cb","text":"{\"gloss_range\":\"Form VIII imperfect action of rising upon and becoming aware of the hearts through the preposition\",\"prose\":\"{{ar:تَطَّلِعُ}} ({{tr:taṭṭaliʿu}}) is the word that animates the prior fire. Its hidden feminine subject is recovered from the relative-pronoun frame, so the fire acts without being renamed. The Form VIII shape keeps two motions together: the fire rises upon the hearts and also inspects or becomes aware of them through {{ar:عَلَى ٱلْأَفْـِٔدَةِ}} ({{tr:ʿalā al-afʾidati}}). That derived shape makes the fire itself the seeker or inspector, not merely something that rises and not a causative disclosure to another party. That makes the punishment more than blind burning; the fire mounts over the inner target as a knowing, exposing force. The assimilated doubled emphatic stop and guttural release give the action weight and pressure, while the imperfect keeps it ongoing rather than finished. Wider root images of scouting, emergence, and reading sharpen the sense of inspection, but they remain secondary to the locally licensed rising-upon and looking-into frame.\",\"root_display\":\"{{ar:ط ل ع}} ({{tr:ṭ-l-ʿ}})\",\"root_gloss_range\":\"root range includes rising, appearing, overlooking, scouting, and emergence; the local verb selects the rising-inspection branch and narrows other images to secondary pressure\",\"surface_display\":\"{{ar:تَطَّلِعُ}} ({{tr:taṭṭaliʿu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:3:verb-target-hinge","source_type":"word_analysis","support_id":"sup_d74a34476ea01e3b6aea","text":"{\"blocking_evidence\":null,\"headline\":\"the preposition completes the verb's reach\",\"reader_payoff\":\"The reader notices that the preposition is not a detachable gloss; it completes the construction by carrying the verb into its inner target.\",\"reason\":\"The local verb instance has no direct object and is completed by a {{ar:عَلَى}} ({{tr:ʿalā}}) prepositional complement, so the CRITICAL hinge claim is grammatically forced.\",\"representative_source_ids\":[\"QT-1530385f\",\"QB-3145ca73\",\"QY-6ed36101\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:1","source_type":"word_analysis","support_id":"sup_e65802ea15faf9f59173","text":"{\"gloss_range\":\"feminine singular relative pronoun carrying the prior fire description into a defining verbal clause\",\"prose\":\"{{ar:ٱلَّتِى}} ({{tr:allatī}}) begins the ayah in dependence, not as a fresh subject. Its feminine singular form carries forward the prior fire description, the complex of {{ar:ٱلْحُطَمَةُ ... نَارُ ٱللَّهِ ٱلْمُوقَدَةُ}} ({{tr:al-ḥuṭamatu ... nāru llāhi al-mūqadah}}) (104:5-6). The reader has to bring that fire across the ayah break before the verb can be heard. The relative clause then defines the fire by what it does: {{ar:ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ}} ({{tr:allatī taṭṭaliʿu ʿalā al-afʾidati}}) makes the action of rising and inspecting part of the fire's identity, not a later incident.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:ٱلَّتِى}} ({{tr:allatī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:2:inner-to-enclosing-bridge","source_type":"word_analysis","support_id":"sup_e996577f164ed8549b37","text":"{\"blocking_evidence\":null,\"headline\":\"inner exposure anticipates enclosure\",\"reader_payoff\":\"The reader notices that the fire's movement upon the hearts in 104:7 prepares the next ayah's enclosure upon the persons in 104:8.\",\"reason\":\"The row's forward bridge is coherent with the local {{ar:عَلَى}} ({{tr:ʿalā}}) complement in 104:7 and the resumed upon-relation in 104:8.\",\"representative_source_ids\":[\"QB-b8f8fdd5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:7:4:governed-definite-broken-plural","source_type":"word_analysis","support_id":"sup_ffb7490a7ae2772d4321","text":"{\"blocking_evidence\":null,\"headline\":\"the hearts are governed, plural, and definite\",\"reader_payoff\":\"The reader notices that {{ar:ٱلْأَفْـِٔدَةِ}} ({{tr:al-afʾidati}}) is not a direct object or vague interior; it is a definite broken plural target governed through {{ar:عَلَى}} ({{tr:ʿalā}}).\",\"reason\":\"QAC and attachment evidence mark the noun as definite, broken plural, genitive, and governed by {{ar:عَلَى}} ({{tr:ʿalā}}), matching the CRITICAL grammar and plurality rows.\",\"representative_source_ids\":[\"QG-6f5e2df8\",\"QG-b70d1cac\",\"QF-b7d97bce\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ","ayah_ref":"104:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000945/B003","root_001122/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000945","role":"Overlooking and disclosure make the motion an access to hidden interiority rather than surface contact.","root":"ط ل ع","source_ref":"104:7","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_001122","role":"The struck or afflicted heart makes the disclosed interior the point of impact.","root":"ف ء د","source_ref":"104:7","source_word_indices":["4"]}],"changed_reading":{"after":"It gains an overlooking access to the inward center, exposing and striking what is normally hidden.","before":"An unspecified feminine subject comes up to the hearts."},"confidence":"strong","focus_anchor":"The construction joins an upward or overlooking motion directly to the definite plural hearts.","mechanism":"The verb can supply an elevated access that uncovers an interior, while the heart-root can supply a center actually struck or afflicted. The motion is therefore not mere arrival at an organ but acquisition of invasive vantage over a vulnerable inside.","model_id":"baseline_inner_overlook"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_inner_overlook","source_type":"hft","support_id":"sup_98e597d3e35b9f3560e7","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ","ayah_ref":"104:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000945/B001","root_001122/B001","root_001122/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000945","role":"Luminary-like rising supplies upward emergence and the onset of visible intensity.","root":"ط ل ع","source_ref":"104:7","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001122","role":"The heart understood as inward kindling gives the destination its own latent combustion.","root":"ف ء د","source_ref":"104:7","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001122","role":"Roasting and kindling heat makes the thermal relation materially forceful, not merely emotional.","root":"ف ء د","source_ref":"104:7","source_word_indices":["4"]}],"changed_reading":{"after":"A heat-bearing agency rises at hearts already lexically figured as inward kindling, allowing heat to meet and expose latent heat.","before":"Something rises over an inner human faculty."},"confidence":"strong","focus_anchor":"The rising verb is predicated of an agent whose path terminates at hearts, and the heart noun itself carries a heat-bearing branch.","mechanism":"A rising or dawning motion meets the heart as an inner kindling rather than a neutral container. Even before context identifies the feminine antecedent, the focus line permits a thermal resonance in which rising heat encounters latent inward heat.","model_id":"baseline_rising_inner_kindling"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_rising_inner_kindling","source_type":"hft","support_id":"sup_59bf448e19e2f7b95ddd","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ","ayah_ref":"104:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000945/B007","root_001122/B002"],"payload":{"activation_trace":[{"branch_id":"B007","mapped_root_id":"root_000945","role":"Fullness to the brim turns ascent into comprehensive range and saturation.","root":"ط ل ع","source_ref":"104:7","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001122","role":"The plural inner-kindling hearts provide the distributed field that is saturated.","root":"ف ء د","source_ref":"104:7","source_word_indices":["4"]}],"changed_reading":{"after":"The agent ranges through the whole field of hearts and fills their inward capacity without leaving a protected recess.","before":"The agent reaches each heart at one point."},"confidence":"medium","focus_anchor":"The motion governs the plural hearts through a preposition that can sustain ranging over a field.","mechanism":"The fullness branch of the rising-root changes a punctual touch into exhaustive occupation: the agent ranges across or fills the heart-field to capacity.","model_id":"baseline_exhaustive_saturation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_exhaustive_saturation","source_type":"hft","support_id":"sup_3a87576985803bb9eeaa","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ","ayah_ref":"104:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000945/B010","root_001122/B003"],"payload":{"activation_trace":[{"branch_id":"B010","mapped_root_id":"root_000945","role":"The overshooting projectile supplies a trajectory that rises past the expected stopping point.","root":"ط ل ع","source_ref":"104:7","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_001122","role":"The heart struck at its center supplies the target that is reached and exceeded.","root":"ف ء د","source_ref":"104:7","source_word_indices":["4"]}],"changed_reading":{"after":"The heart is both target and breached threshold: the force reaches the center but is not bounded by an ordinary hit.","before":"The heart is the terminal object of impact."},"confidence":"exploratory","focus_anchor":"The heart is the governed destination of a verb whose inventory includes a projectile rising beyond its target.","mechanism":"The projectile branch and the struck-heart branch produce a double relation: the heart is hit as a target yet also becomes a threshold the force exceeds. This keeps open a reading of transgressive reach rather than neatly bounded impact.","model_id":"baseline_overshot_heart_target"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_overshot_heart_target","source_type":"hft","support_id":"sup_346ed1969d08296d679a","trust":"legacy_unbound"}]}
</lane_packet_json>
