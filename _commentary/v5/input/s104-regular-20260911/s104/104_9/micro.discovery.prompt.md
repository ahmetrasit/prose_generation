# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **104:9**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s104-regular-20260911/s104/104_9/micro.discovery.json` and modify nothing
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
  "ayah_ref": "104:9",
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
{"analysis_context":{"analysis_id":"s104-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"104:9","host_surah":104,"lane_context_refs":[],"ordered_context_refs":["104:0","104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:8","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Anlam, fiziksel dayama ve dik direk anlamlarından ayrılır; özel kalıplar çıplak kullanıma genellenmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001043/B001","candidate_links":[{"candidate_id":"cand_190412a5e54578fafdb6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَمَد","morph_features":"STEM|POS:N|LEM:Eamad|ROOT:Emd|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:9:2:1","qac_word_ref":"104:9:2","surface_ar":"عَمَدٍ"}],"gloss":"isteyerek yönelme ve bilerek yapma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eylem, yanlışlıkla ya da dalgınlıkla değil, bilinçli bir seçimle gerçekleştirilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişiye veya şeye isteyerek yönelme, bu çekirdeğin yöneltili kullanımıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özel bir kalıp, işi ciddi, kesin ve bütünüyle bilerek yapmayı anlatır."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel çekirdeği, hem hedefe yönelmeyi hem de eylemin yanlışlıkla yapılmamasını belirtmek gerektiğinde karşılar.","boundary_detail":"Anlam, fiziksel dayama ve dik direk anlamlarından ayrılır; özel kalıplar çıplak kullanıma genellenmez.","branch_image_ar":"القصد المتعمد","concept_gloss":"isteyerek yönelme ve bilerek yapma","contextual_glosses":[{"applicability":"Bir eylemin yanlışlıkla değil, bilinçli olarak yapıldığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemin bilinçli ve isteyerek yapılmış olmasını korur."},"facet_ids":["F001"],"text":"bunu bile isteye yaptı","usage_role":"contextual"}],"definition":"Bir kişiye ya da şeye isteyerek yönelmek veya bir işi yanılma ve dalgınlık olmadan bilerek yapmaktır. Belirli bir kalıp, bu bilinçli yapışı ciddiyet ve kesinlikle güçlendirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eylem, yanlışlıkla ya da dalgınlıkla değil, bilinçli bir seçimle gerçekleştirilir."},{"facet_id":"F002","role":"specialization","statement":"Bir kişiye veya şeye isteyerek yönelme, bu çekirdeğin yöneltili kullanımıdır."},{"facet_id":"F003","role":"associated_use","statement":"Özel bir kalıp, işi ciddi, kesin ve bütünüyle bilerek yapmayı anlatır."}],"identity_rationale":"Kaynak anlatımı, bir kişiye ya da şeye isteyerek yönelmeyi ve bir işi dalgınlıkla veya yanlışlıkla değil bilerek yapmayı açıkça birlikte verir. Güçlü kararlılık bildiren kalıp ise bu çekirdeğin özel bir gerçekleşmesidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeye isteyerek yönelmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yanlışlıkla değil, bilerek yapılan eylem"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bile isteye, ciddiyetle ve kesinlikle"}],"lexicalization_note":"Tanım, genel bilerek yapma çekirdeğini yönelme ve güçlü kesinlik bildiren kalıba bağlı kullanımlardan ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sınırı en açık biçimde gösteren yönelme ve seçme komşusu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal, yönelmenin yanında eylemin bilinçli yapılmasını da kapsar; komşu dal ise seçenekler arasından birini ayırıp yalnız ona yönelmeyi öne çıkarır.","focus_only":"Bir işi yanlışlıkla değil bilerek yapma karşıtlığını da içerir.","gloss":"seçerek yönelme","neighbor_only":"Seçilen şeyden başkasını istememe ve yalnız ona gitme vurgusu taşır.","neighbor_ref":"root_001049/B009","relation_type":"near_synonym","shared_zone":"Her ikisi de belirli bir hedefe istek ve seçimle yönelmeyi anlatır."}],"source_phrase_ar":"عمدت فلانا إذا قصدت إليه (maqayis); عمدت فلانا أي قصدته وتعمدته (ayn); عمدت للشئ قصدت له وهو نقيض الخطاء (sihah); عمدت للشيء إذا قصدت له (tahdhib); العمد والتعمد خلاف السهو (mufradat)","source_summary":"Kaynaklar, isteyerek yönelme ile yanlışlık ve dalgınlığın karşıtı olan bilinçli yapma üzerinde birleşir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه قصد الشيء وتعمده وفعل الأمر عمدا أو معتمدا","what_is_not_ar":"ليس إسناد الشيء بعماد ولا العمود الحسي"},"support_links":["sup_881e018bd0267b81ad45"]},{"boundary":"Bu dal, desteğin kendisini adlandıran daldan ve istemli yönelme anlamından ayrılır.","branch_kind":"mixed_non_bare","branch_ref":"root_001043/B002","candidate_links":[{"candidate_id":"cand_3afc84ebba1f0f300469","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَمَد","morph_features":"STEM|POS:N|LEM:Eamad|ROOT:Emd|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:9:2:1","qac_word_ref":"104:9:2","surface_ar":"عَمَدٍ"}],"gloss":"dayanak koyarak destekleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesne, yaslandığı ya da altına konduğu dayanak aracılığıyla desteklenir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Türemiş biçim, nesnenin altına taşıyıcı destek koyma işlemini özellikle belirtir."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin başka bir taşıyıcıya yaslanarak veya altından desteklenerek ayakta tutulduğu durumları karşılar.","boundary_detail":"Bu dal, desteğin kendisini adlandıran daldan ve istemli yönelme anlamından ayrılır.","branch_image_ar":"إسناد الشيء بعماد","concept_gloss":"dayanak koyarak destekleme","contextual_glosses":[{"applicability":"Duvar gibi fiziksel bir nesnenin devrilmemesi için dıştan dayandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesnenin fiziksel bir dayanakla tutulmasını açıkça korur."},"facet_ids":["F001"],"text":"duvarı payandayla destekledi","usage_role":"contextual"}],"definition":"Bir nesneyi, dayandığı bir destekle ayakta tutmak veya altına onu taşıyacak bir dayanak yerleştirmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesne, yaslandığı ya da altına konduğu dayanak aracılığıyla desteklenir."},{"facet_id":"F002","role":"specialization","statement":"Türemiş biçim, nesnenin altına taşıyıcı destek koyma işlemini özellikle belirtir."}],"identity_rationale":"Kaynak anlatımı, bir nesneyi dayamak, ayakta tutmak ve altına onu taşıyan bir destek koymak işlemlerini doğrudan bildirir. Dalın kimliği destek nesnesinden çok bu destekleme eylemidir.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"nesneyi dayayıp desteklemek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"nesnenin altına dayanak koymak"}],"lexicalization_note":"Tanım, nesneyi destekleme eylemini ve altına destek koyduran biçimi kapsar; bunları destek nesnesinin adıyla karıştırmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; eylem olarak desteklemeye en çok yaklaşan komşu sınır karşılaştırması için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal fiziksel dayama işlemiyle sınırlıdır; komşu dal ise fiziksel desteğin yanı sıra yardım ve iş birliğini de kapsayan daha geniş bir destek alanına sahiptir.","focus_only":"Fiziksel bir nesneyi taşıyan desteğin yerleştirilmesini özellikle bildirir.","gloss":"destekleme ve yardım","neighbor_only":"Yardım etme, birlikte güç verme ve kişiler arası destek alanına da yayılır.","neighbor_ref":"root_000554/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da zayıf veya yük taşıyan bir şeyin güçlendirilmesi vardır."}],"source_phrase_ar":"تعمد الشيء بعماد يمسكه ويعتمد عليه (maqayis;ayn); عمدت الشيء أسندته (maqayis;mufradat); أقمته بعماد يعتمد عليه وأعمدته جعلت تحته عمدا (sihah); عمدت الحائط إذا دعمته (tahdhib)","source_summary":"Kaynaklar, nesneyi bir dayanağa yaslayarak destekleme ve altına destek yerleştirme işlemlerini ortak biçimde aktarır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه إقامة الشيء ودعمه بعماد يعتمد عليه وجعل العمد تحته","what_is_not_ar":"ليس القصد بالنية ولا العمود اسما للخشبة نفسها"},"support_links":["sup_9921d44f046a5d1673aa"]},{"boundary":"Dal, destekleme eylemini değil dik destek parçasını adlandırır; özel ateş kalıbı genel nesne anlamına katılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001043/B003","candidate_links":[{"candidate_id":"cand_bc7a63f862b504e6d208","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَمَد","morph_features":"STEM|POS:N|LEM:Eamad|ROOT:Emd|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:9:2:1","qac_word_ref":"104:9:2","surface_ar":"عَمَدٍ"}],"gloss":"taşıyıcı dik direk veya sütun","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne, bir yapıyı taşıyan veya ona dayanma sağlayan dik parçadır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Direk; ahşap, demir ya da mermer sütun gibi farklı maddi gerçekleşmelere sahip olabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özel bir kalıp, uzatılmış ateş sütunlarını veya ateşten çadır benzeri yapıları anlatır."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir yapıyı ya da çadırı dik tutan, çeşitli maddelerden yapılabilen taşıyıcı parça için uygundur.","boundary_detail":"Dal, destekleme eylemini değil dik destek parçasını adlandırır; özel ateş kalıbı genel nesne anlamına katılmaz.","branch_image_ar":"العمود والعماد","concept_gloss":"taşıyıcı dik direk veya sütun","contextual_glosses":[{"applicability":"Çadırın ortasında dik durup örtüyü taşıyan ahşap parça söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çadır bağlamını, orta konumu ve taşıyıcı işlevi korur."},"facet_ids":["F001"],"text":"çadırın orta direği","usage_role":"contextual"}],"definition":"Bir yapı, çadır veya başka bir düzenek için dik duran ve yükü taşıyan direk ya da sütundur. Belirli bir anlatımda uzatılmış ateş sütunlarına veya ateşten çadırı andıran yapılara da uygulanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne, bir yapıyı taşıyan veya ona dayanma sağlayan dik parçadır."},{"facet_id":"F002","role":"extension","statement":"Direk; ahşap, demir ya da mermer sütun gibi farklı maddi gerçekleşmelere sahip olabilir."},{"facet_id":"F003","role":"associated_use","statement":"Özel bir kalıp, uzatılmış ateş sütunlarını veya ateşten çadır benzeri yapıları anlatır."}],"identity_rationale":"Kaynak anlatımı, yapı veya çadır gibi bir şeyi taşıyan dik parçayı; bunun ahşap, demir, mermer ve benzeri maddelerden olabilen türlerini verir. Ateşten uzatılmış dik parçalar anlatımı bu nesne çekirdeğinin özel bir benzetmeli kullanımıdır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"dayanak veya taşıyıcı direk"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ahşap, demir ya da taş sütun"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"uzatılmış ateş sütunları içinde"}],"lexicalization_note":"Tanım, dik destek nesnesini temel alır ve uzatılmış ateş parçaları bildiren kalıbı ayrı bir özel kullanım olarak sınırlar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; taşıyıcı nesne sınırına en yakın sütun dalı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal malzeme ve kullanım bakımından daha geniştir ve çadır direğini de içerir; komşu dal daha çok taş ya da tuğladan yapılmış sütun türüne bağlıdır.","focus_only":"Çadır direğini ve demir, ahşap ya da ateş gibi daha geniş gerçekleşmeleri kapsar.","gloss":"taş veya tuğla sütun","neighbor_only":"Taş veya tuğladan yapılmış silindir biçimli sütunu özellikle öne çıkarır.","neighbor_ref":"root_000702/B005","relation_type":"near_synonym","shared_zone":"Her ikisi de dik duran sütun veya direk türü bir yapı parçasını adlandırır."}],"source_phrase_ar":"الشيء الذي يسند إليه عماد وجمع العماد عمد والعمود من خشب أو حديد (maqayis); عمود الخباء من خشب قائم في الوسط (ayn); العمود عمود البيت وجمعه أعمدة وعمد (sihah); العمد أساطين الرخام وفي عمد من النار (tahdhib); العمود خشب تعتمد عليه الخيمة وجمعه عمد (mufradat)","source_summary":"Kaynaklar, taşıyıcı dik parçayı ve onun yapı ile çadırdaki örneklerini ortaklaştırır; ateşten uzatılmış parçalar özel bir anlatımdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العمود والعماد والأعمدة والعمد من خشب أو حديد أو نار أو رخام وما يقوم عليه البيت أو الخباء","what_is_not_ar":"ليس فعل القصد ولا السيد المعتمد عليه"},"support_links":["sup_56ddf1c23818bcc9bf75"]},{"boundary":"Anlam yalnızca verilen topluluk adlandırmasına bağlıdır; her çadır sakini veya her çadır kümesi bununla karşılanmaz.","branch_kind":"non_bare","branch_ref":"root_001043/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَمَد","morph_features":"STEM|POS:N|LEM:Eamad|ROOT:Emd|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:9:2:1","qac_word_ref":"104:9:2","surface_ar":"عَمَدٍ"}],"gloss":"yalnız çadırlarda yaşayan topluluk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Topluluk, barınma ve konaklama biçimi olarak yalnızca çadırları kullanmasıyla tanımlanır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu topluluk otlaklara doğru yer değiştiren çadır sahipleri olarak da betimlenir."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çadırı sürekli barınma biçimi olarak kullanan ve başka konak türlerine yerleşmeyen topluluk için uygundur.","boundary_detail":"Anlam yalnızca verilen topluluk adlandırmasına bağlıdır; her çadır sakini veya her çadır kümesi bununla karşılanmaz.","branch_image_ar":"أهل العمود والعماد","concept_gloss":"yalnız çadırlarda yaşayan topluluk","contextual_glosses":[{"applicability":"Bağlam, başka konak türü kullanmayan çadır sahiplerini zaten belirtiyorsa kısa karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çadırlarda yaşayan insan topluluğu anlamını bağlam içinde korur."},"facet_ids":["F001"],"text":"çadır halkı","usage_role":"contextual"}],"definition":"Çadırlarda yaşayan ve başka tür konaklara yerleşmeyen çadır halkıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Topluluk, barınma ve konaklama biçimi olarak yalnızca çadırları kullanmasıyla tanımlanır."},{"facet_id":"F002","role":"associated_use","statement":"Bu topluluk otlaklara doğru yer değiştiren çadır sahipleri olarak da betimlenir."}],"identity_rationale":"Kaynak anlatımı, çadırlarda yaşayan ve başka tür konaklara yerleşmeyen topluluğu açıkça tanımlar. Bu nedenle dal, çadırın kendisine değil, bu yaşam biçimiyle belirlenen insan grubuna aittir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"başka yerde konaklamayan çadır halkı"}],"lexicalization_note":"Tanım, yalnızca çadır halkını bildiren yerleşik söz öbeğine bağlı kalır ve bağımsız bir kök anlamı varsaymaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; topluluk ile çadır yerleşimi arasındaki en olası karışıklık yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yerleşim düzenini değil, çadırdan başka yerde kalmayan insan topluluğunu anlatır; komşu dal ise insanların kimliğinden çok bir araya gelmiş barınakları anlatır.","focus_only":"İnsanları, yalnızca çadırlarda yaşamaları bakımından sınıflandırır.","gloss":"çadır ve ev kümesi","neighbor_only":"Birbirine yakın tek bir çadırı veya çadır ve ev kümesini yerleşim olarak adlandırır.","neighbor_ref":"root_000374/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da çadırlı yaşama ve yerleşme alanıyla ilişkilidir."}],"source_phrase_ar":"أهل عمود وأهل عماد أصحاب الأخبية لا ينزلون غيرها (maqayis;ayn); كانوا أهل عمد ينتقلون إلى الكلأ (tahdhib); أصحاب الأخبية الذين لا ينزلون غيرها (tahdhib)","source_summary":"Kaynaklar, başka tür konaklara yerleşmeyip çadırlarda yaşayan insanları belirten topluluk adında birleşir.","sources":["MQ","AY","TA"],"what_is_ar":"يدخل فيه أصحاب الأخبية وأهل العمود أو العماد الذين لا ينزلون غيرها","what_is_not_ar":"ليس كل عماد بمعنى أهل الخباء ولا تفسير ذات العماد بالطول"},"support_links":[]},{"boundary":"Anlam yalnızca verilen uzunluk ve yücelik kalıplarına bağlıdır; her direk veya her yükselme bu dala girmez.","branch_kind":"collocation","branch_ref":"root_001043/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَمَد","morph_features":"STEM|POS:N|LEM:Eamad|ROOT:Emd|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:9:2:1","qac_word_ref":"104:9:2","surface_ar":"عَمَدٍ"}],"gloss":"kalıba bağlı uzunluk ve yücelik","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Anlam, belirli söz öbeklerinde uzunluk veya yükseklik niteliğini bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Uzunluk bildiren kalıp, kişinin boyuna veya ziyaretçilere uzaktan görünen yüksek evine yorumlanabilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yücelik bildiren kalıp, kişinin başkalarınca güvenilir dayanak sayılan yüksek konumunu anlatabilir."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca sağlanan söz öbeklerinin kişi boyu, yüksek yapı veya dayanılan yüksek konum yorumlarını topluca göstermek için uygundur.","boundary_detail":"Anlam yalnızca verilen uzunluk ve yücelik kalıplarına bağlıdır; her direk veya her yükselme bu dala girmez.","branch_image_ar":"الطول والرفعة في العماد","concept_gloss":"kalıba bağlı uzunluk ve yücelik","contextual_glosses":[{"applicability":"Uzunluk kalıbının kişinin ziyaretçilerince kolay görülen yüksek konutunu anlattığı yorumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yüksekliği, görünürlüğü ve kişiyle bağlantılı konut yorumunu korur."},"facet_ids":["F002"],"text":"yüksek ve uzaktan görünen ev sahibi","usage_role":"explanatory"}],"definition":"Verilen söz öbeklerinde bir kişinin uzunluğunu, yüksek ve görünür yapısını ya da başkalarının dayandığı yüce konumunu anlatır; hangi yorumun geçerli olduğu kalıba ve bağlama bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Anlam, belirli söz öbeklerinde uzunluk veya yükseklik niteliğini bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Uzunluk bildiren kalıp, kişinin boyuna veya ziyaretçilere uzaktan görünen yüksek evine yorumlanabilir."},{"facet_id":"F003","role":"source_variant","statement":"Yücelik bildiren kalıp, kişinin başkalarınca güvenilir dayanak sayılan yüksek konumunu anlatabilir."}],"identity_rationale":"Kaynak anlatımı, verilen kalıplarda uzunluk, yüksek yapı ve bir kişinin dayanak olarak yüceliği gibi birbirine bağlı fakat aynı olmayan yorumlar aktarır. Dal korunabilir, ancak bunlar bağımsız bir genel yükselme anlamı olarak birleştirilemez.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"uzun boylu veya evi uzaktan görünen"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"dayanak sayılan yüce kişi"}],"lexicalization_note":"Tanım, uzunluk ve yücelik yorumlarını yalnızca sağlanan söz öbeklerine bağlar ve çıplak köke genellemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kalıba bağlı yüceliği genel fiziksel yükselmeden ayıran komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kalıba bağlı kişi, konut ve saygınlık yorumları taşır; komşu dal ise nesnelerin genel olarak yükselmesi ve uzamasıyla ilgilidir.","focus_only":"Uzunluk ve yüceliği yalnızca belirli kişi ve yapı kalıplarında bildirir.","gloss":"genel yükselme ve uzama","neighbor_only":"Nesnenin yükselmesi, boyun uzaması ve yukarı çıkma gibi genel fiziksel yükselmeyi kapsar.","neighbor_ref":"root_000742/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da uzunluk veya yukarıda bulunma düşüncesi vardır."}],"source_phrase_ar":"رجل معمد أي طويل والعماد الطول (maqayis); العماد الأبنية الرفيعة وفلان طويل العماد (sihah); ذات العماد أي ذات الطول وقيل ذات البناء الرفيع (tahdhib)","source_summary":"Kaynaklar, kalıpları uzunluk ve yükseklik çevresinde toplar; kişi boyu, yüksek yapı, görünür konut ve dayanılan yüce konum yorumları bağlama göre ayrışır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه العماد بمعنى الطول والبناء الرفيع والمنزل الظاهر العالي","what_is_not_ar":"ليس أصحاب الأخبية إلا في تفسير آخر وليس مجرد خشبة العمود"},"support_links":[]},{"boundary":"Bu dal fiziksel direği değil, bir topluluğun ya da işin güvenilir insanî veya soyut dayanağını anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001043/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَمَد","morph_features":"STEM|POS:N|LEM:Eamad|ROOT:Emd|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:9:2:1","qac_word_ref":"104:9:2","surface_ar":"عَمَدٍ"}],"gloss":"güvenilip dayanılan önder veya temel unsur","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi ya da unsur, başkalarının güvenip dayandığı başlıca başvuru noktasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Topluluk bağlamında bu dayanak, onların önderi ve işlerinde başvurduğu kişidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Daha genel biçim, güvenilen bir kişi yanında malı veya işi de dayanak olarak gösterebilir."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir topluluğun başvurduğu kişi veya bir işin güvenilir başlıca dayanağı anlatıldığında kullanılır.","boundary_detail":"Bu dal fiziksel direği değil, bir topluluğun ya da işin güvenilir insanî veya soyut dayanağını anlatır.","branch_image_ar":"المعتمد عليه في القوم","concept_gloss":"güvenilip dayanılan önder veya temel unsur","contextual_glosses":[{"applicability":"Bir grubun işlerinde başvurduğu ve kendisine dayandığı baş kişi söz konusu olduğunda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önderliği ve topluluğun ona güvenip dayanmasını korur."},"facet_ids":["F001","F002"],"text":"topluluğun güvendiği önder","usage_role":"contextual"}],"definition":"Bir topluluğun güvenip başvurduğu önder veya bir işte kendisine dayanılan kişi, mal ya da temel unsurdur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi ya da unsur, başkalarının güvenip dayandığı başlıca başvuru noktasıdır."},{"facet_id":"F002","role":"specialization","statement":"Topluluk bağlamında bu dayanak, onların önderi ve işlerinde başvurduğu kişidir."},{"facet_id":"F003","role":"extension","statement":"Daha genel biçim, güvenilen bir kişi yanında malı veya işi de dayanak olarak gösterebilir."}],"identity_rationale":"Kaynak anlatımı, topluluğun başındaki kişiyi yalnızca yönetici olarak değil, insanların güvenip başvurduğu dayanak olarak tanımlar. Daha genel biçim kişi, mal veya iş gibi güvenilen dayanaklara da uzanır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"topluluğun güvendiği önder"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"güvenilip dayanılan kişi, mal veya temel unsur"}],"lexicalization_note":"Tanım, topluluk önderini bildiren söz öbeğiyle kişi, mal veya iş için kullanılan daha genel dayanak biçimini ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; önderlik ile güvenilir dayanak arasındaki sınırı en iyi gösteren komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda önderlik, insanların o kişiye güvenip dayanmasıyla kurulur; komşu dal yalnızca topluluğun baş kişisi olma konumunu bildirir.","focus_only":"Önderi, topluluğun güvenip dayandığı başvuru kişisi olmasıyla tanımlar.","gloss":"topluluk başı","neighbor_only":"Topluluğun baş kişisini, güvenilir dayanak olma koşulunu belirtmeden adlandırır.","neighbor_ref":"root_001571/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da topluluğun başında bulunan kişiyi anlatabilir."}],"source_phrase_ar":"عميد القوم سيدهم ومعتمدهم (maqayis); عميد القوم سيدهم الذي يعتمدون عليه (ayn); عميد القوم وعمودهم سيدهم والعمدة ما يعتمد عليه (sihah); فلان عمدة قومه إذا كانوا يعتمدونه (tahdhib); العميد السيد الذي يعمده الناس (mufradat)","source_summary":"Kaynaklar, topluluğun güvendiği önder ile kişi, mal veya iş olarak dayanılan temel unsur düşüncesinde birleşir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العميد والعمدة والسيد ومن يعتمد عليه القوم عند الأمر","what_is_not_ar":"ليس العمود الحسي ولا الوجع الذي يعمد الإنسان"},"support_links":[]},{"boundary":"Her kullanım kendi söz öbeğine bağlıdır; bir örneğin özel özelliği bütün dala genellenmez.","branch_kind":"collocation","branch_ref":"root_001043/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَمَد","morph_features":"STEM|POS:N|LEM:Eamad|ROOT:Emd|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:9:2:1","qac_word_ref":"104:9:2","surface_ar":"عَمَدٍ"}],"gloss":"kalıba göre ana, orta veya uzunlamasına parça","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Söz öbeği, ilgili bütünün ana taşıyıcı, orta veya uzunlamasına uzanan bölümünü seçer."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İş ve görüş bağlamında, bütünün düzgün yürümesini sağlayan temel dayanağı belirtir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kulak, mızrak ucu, karın, sırt, karaciğer, ana damar ve kılıçta orta, ana veya uzanan yapısal parçayı belirtir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Tan ışığının ilk yayılışı ve erkek devekuşunun direğe benzetilen bacakları da bu adlandırmaya girer."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Verilen iş, organ, silah, tan ve hayvan söz öbeklerinin ortak yapısal benzerliğini belirtmek için uygundur.","boundary_detail":"Her kullanım kendi söz öbeğine bağlıdır; bir örneğin özel özelliği bütün dala genellenmez.","branch_image_ar":"قوام الشيء ووسطه","concept_gloss":"kalıba göre ana, orta veya uzunlamasına parça","contextual_glosses":[{"applicability":"Bir işin onsuz düzgün yürümeyeceği ana dayanağı anlatan söz öbeğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşin ayakta kalmasını sağlayan temel unsur anlamını korur."},"facet_ids":["F002"],"text":"işin belkemiği","usage_role":"contextual"}],"definition":"Verilen söz öbeklerinde bir şeyin ayakta kalmasını sağlayan ana unsurunu, orta ya da uzunlamasına bölümünü veya direğe benzetilen belirgin parçasını anlatır. Tam karşılık, iş, organ, silah, tan ışığı ya da hayvan bacağı bağlamına göre değişir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Söz öbeği, ilgili bütünün ana taşıyıcı, orta veya uzunlamasına uzanan bölümünü seçer."},{"facet_id":"F002","role":"specialization","statement":"İş ve görüş bağlamında, bütünün düzgün yürümesini sağlayan temel dayanağı belirtir."},{"facet_id":"F003","role":"specialization","statement":"Kulak, mızrak ucu, karın, sırt, karaciğer, ana damar ve kılıçta orta, ana veya uzanan yapısal parçayı belirtir."},{"facet_id":"F004","role":"extension","statement":"Tan ışığının ilk yayılışı ve erkek devekuşunun direğe benzetilen bacakları da bu adlandırmaya girer."}],"identity_rationale":"Kaynak anlatımı yalnızca tek bir genel orta parça anlamı vermez; işin ayakta kalmasını sağlayan ana unsur, organ ve araçların orta ya da uzunlamasına bölümü, tan ışığının başlangıcı ve benzetmeli bacak adları gibi kalıba bağlı kullanımları sıralar. Dal bu ortak dikey, orta veya taşıyıcı benzerlik altında korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"işin belkemiği ve ana dayanağı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kulağın ana ve büyük bölümü"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"mızrak ucunun iki ağzı arasındaki orta bölüm"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"karında uzanan damar veya gövdeyi taşıyan sırt"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"karaciğeri besleyen damar ve ana atardamar"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"tan ışığının ilk yayılışı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kılıç sırtının ortasındaki uzun çizgi"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"erkek devekuşunun direğe benzeyen iki bacağı"}],"lexicalization_note":"Tanım yalnızca verilen söz öbeklerini kapsar; orta, ana veya uzunlamasına bölüm anlamını bağımsız bir sözcük anlamına dönüştürmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; orta bölüm ile ana dayanak kapsamlarını ayıran en yakın komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal, orta bölüm yanında bir işin ana dayanağını ve başka benzetmeli kalıpları da içerir; komşu dal belirli beden ve silah bölümleriyle sınırlı ayrı bir adlandırmadır.","focus_only":"Ana dayanak, tan ışığı ve çok sayıda kalıba bağlı orta parça kullanımını kapsar.","gloss":"gövde veya sapın orta kesimi","neighbor_only":"Hayvan gövdesi ile ok veya mızrak sapının belirli orta kesimlerini kendi adlarıyla belirtir.","neighbor_ref":"root_000634/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir bedenin ya da uzun nesnenin orta bölümünü seçebilir."}],"source_phrase_ar":"عمود الأمر قوامه (maqayis;ayn); عمود الأذن معظمها وقوامها (maqayis;ayn;tahdhib); عمود السنان ما توسط شفرتيه (maqayis;ayn;tahdhib); عمود البطن شبه عرق ممدود (maqayis;ayn;tahdhib); عمود الكبد عرق يسقيها وعمود السحر الوتين (maqayis;ayn;tahdhib); عمود الصبح ابتداء ضوئه (sihah;mufradat); عمود السيف الشطيبة في وسط متنه (tahdhib)","source_summary":"Toplu anlatım, ana dayanak ile orta veya uzunlamasına parça düşüncesini çeşitli söz öbeklerinde birleştirir; organ, silah, tan ve hayvan örneklerinin kapsamı kendi bağlamlarıyla sınırlıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه عمود الأمر وقوامه وعمود الأذن والسنان والسيف والبطن والكبد والسحر والصبح وما شاكل ذلك من معظم الشيء أو وسطه","what_is_not_ar":"ليس السيد المعتمد عليه ولا الخباء نفسه"},"support_links":[]},{"boundary":"Dal, sıradan ağrıdan daha ağır biçimde güçten düşürme ve ezme sonucunu içerir; hayvan hörgücü yaralanması ayrı daldadır.","branch_kind":"mixed_non_bare","branch_ref":"root_001043/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَمَد","morph_features":"STEM|POS:N|LEM:Eamad|ROOT:Emd|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:9:2:1","qac_word_ref":"104:9:2","surface_ar":"عَمَدٍ"}],"gloss":"acıyla ezilip güçten düşme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Acı veren durum, kişiyi yalnız incitmekle kalmaz, onu ağırlaştırıp gücünü kırar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hasta kişi, destek almadan oturamayacak ölçüde güçsüz düşebilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı ezici etki, sevgi acısı veya derin üzüntüyle yıkılmış yürek için de kullanılır."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hastalık veya duygusal acının kişiyi ağır biçimde tükettiği ve olağan gücünü kırdığı durumları karşılar.","boundary_detail":"Dal, sıradan ağrıdan daha ağır biçimde güçten düşürme ve ezme sonucunu içerir; hayvan hörgücü yaralanması ayrı daldadır.","branch_image_ar":"وجع يهد ويفدح","concept_gloss":"acıyla ezilip güçten düşme","contextual_glosses":[{"applicability":"Hastalığın kişiyi ağır biçimde güçsüz ve bitkin bıraktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hastalığın sürüklediği ağır güç kaybını ve yıpranmayı korur."},"facet_ids":["F001","F002"],"text":"hastalık onu tüketti","usage_role":"contextual"}],"definition":"Hastalık, üzüntü veya sevgi acısının bir kişiyi ya da yüreğini ezip güçten düşürmesi ve ağır biçimde acıtmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Acı veren durum, kişiyi yalnız incitmekle kalmaz, onu ağırlaştırıp gücünü kırar."},{"facet_id":"F002","role":"specialization","statement":"Hasta kişi, destek almadan oturamayacak ölçüde güçsüz düşebilir."},{"facet_id":"F003","role":"extension","statement":"Aynı ezici etki, sevgi acısı veya derin üzüntüyle yıkılmış yürek için de kullanılır."}],"identity_rationale":"Kaynak anlatımı, hastalık yüzünden oturamayacak kadar güçten düşen kişiyi ve sevgi, üzüntü ya da hastalığın ezdiği kişiyi veya yüreği ortak bir ağır acı çekirdeğinde birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"oturamayacak kadar güçten düşmüş hasta"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"sevgi veya üzüntü acısıyla yıkılmış yürek"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"hastalık onu tüketip acıttı"}],"lexicalization_note":"Tanım, güçten düşmüş hasta biçimini, ezilmiş yürek kalıbını ve hastalığın kişiyi tüketmesi kullanımını ayrı görünümler olarak korur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ağır güç kaybını genel hastalık ve ağrıdan ayıran komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal ağır acının ezici ve güçten düşürücü sonucunu zorunlu kılar; komşu dal bu dereceyi gerektirmeyen genel hastalık ve ağrı alanıdır.","focus_only":"Acının kişiyi ezip destek almadan oturamayacak kadar güçten düşürmesini içerir.","gloss":"hastalık ve ağrı","neighbor_only":"Genel hastalık, ağrıdan yakınma ve ağrıyan organ anlatımlarını da kapsar.","neighbor_ref":"root_000814/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da hastalık ve bedensel acı yaşayan kişiyi anlatabilir."}],"source_phrase_ar":"العميد الرجل المعمود لا يستطيع الجلوس من مرضه (maqayis;ayn;tahdhib); القلب العميد المعمود المشعوف الذي هده العشق (maqayis;ayn); عمد المرض فدحه (sihah); المعمود الحزين الشديد الحزن وما يعمدك أي ما يوجعك (tahdhib); القلب الذي يعمده الحزن والسقيم الذي يعمده السقم (mufradat)","source_summary":"Kaynaklar, hastalık, üzüntü veya sevgi acısının kişiyi ya da yüreğini ağır biçimde ezmesi ve güçten düşürmesi üzerinde birleşir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه المريض المعمود والعميد والقلب الذي هده العشق أو الحزن والسقم الذي يضني صاحبه","what_is_not_ar":"ليس نية العمد ولا عماد الخباء ولا فساد سنام البعير نفسه"},"support_links":[]},{"boundary":"Dal yalnızca verilen hayvan ve yara kalıplarını kapsar; insanın hastalıkla güçten düşmesi bu dala girmez.","branch_kind":"collocation","branch_ref":"root_001043/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَمَد","morph_features":"STEM|POS:N|LEM:Eamad|ROOT:Emd|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:9:2:1","qac_word_ref":"104:9:2","surface_ar":"عَمَدٍ"}],"gloss":"baskıyla içten zedelenme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Baskı veya sıkma, dokuda dıştan hemen anlaşılmayabilen bir zedelenme oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Binme yükü, büyük hörgücün iç yapısını çökertip bozabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Olgunlaşmadan sıkılan yara, bu müdahalenin ardından şişer."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca hörgücün yükten içten çökmesi ve yaranın erken sıkılınca şişmesi biçimindeki iki sağlanmış bağlamı topluca karşılar.","boundary_detail":"Dal yalnızca verilen hayvan ve yara kalıplarını kapsar; insanın hastalıkla güçten düşmesi bu dala girmez.","branch_image_ar":"انشداح السنام والجرح","concept_gloss":"baskıyla içten zedelenme","contextual_glosses":[{"applicability":"Uzun süre binme veya yük baskısıyla hörgücün iç kısmı bozulmuş deve için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanı, yük nedenini ve hörgücün içten bozulmasını korur."},"facet_ids":["F001","F002"],"text":"yükten hörgücü içten çökmüş deve","usage_role":"contextual"}],"definition":"Verilen söz öbeklerinde baskı yüzünden içten zedelenmeyi anlatır: binme yükü bir devenin hörgücünü dışı sağlam görünürken içten çökertir ya da erken sıkılan yara şişer.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Baskı veya sıkma, dokuda dıştan hemen anlaşılmayabilen bir zedelenme oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Binme yükü, büyük hörgücün iç yapısını çökertip bozabilir."},{"facet_id":"F003","role":"specialization","statement":"Olgunlaşmadan sıkılan yara, bu müdahalenin ardından şişer."}],"identity_rationale":"Kaynak anlatımı, binme baskısıyla hörgücün içten çökmesi ile olgunlaşmadan sıkılan yaranın şişmesini iki ayrı söz öbeğinde verir. Bunların ortak noktası baskı sonucu oluşan iç zedelenmedir; tek bir genel yara türüymüş gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"binme yükünden hörgücü içten çökmüş deve"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"erken sıkıldığı için şişen yara"}],"lexicalization_note":"Tanım, hörgüç ve yara kullanımlarını kendi söz öbeklerine bağlar; ortak zedelenme çekirdeğini bağımsız bir çıplak anlama dönüştürmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; belirli baskı sonucunu genel deri şişliği ve izlerinden ayıran komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli bir baskı ya da sıkma sürecine ve onun sonucuna bağlıdır; komşu dal çok çeşitli deri çıkıntılarını ve izlerini daha geniş biçimde adlandırır.","focus_only":"Baskının hörgüçte iç çökme veya erken sıkılan yarada şişme oluşturmasını gerektirir.","gloss":"deri kabartısı ve yara izi","neighbor_only":"Çeşitli deri kabartıları, çıbanlar, deri bozulmaları ve darbe izlerini neden sınırlaması olmadan kapsar.","neighbor_ref":"root_000228/B005","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bedende beliren yara, şişlik veya doku bozulması bulunabilir."}],"source_phrase_ar":"السنام إذا كان ضخما فحمل عليه فكسر وبعير عمد وناقة عمدة (maqayis); عمد البعير إذا انفضح داخل سنامه من الركوب (sihah); العمد في السنام أن ينشدخ انشداخا والجرح العمد الذي يعصر فيرم (tahdhib); عمد البعير توجع من عقر ظهره (mufradat)","source_summary":"Toplu anlatım, binme baskısıyla içten bozulan hörgüç ile erken sıkıldıktan sonra şişen yarayı kalıba bağlı iki zedelenme olarak verir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه بعير عمد وناقة عمدة إذا فسد السنام من الركوب أو انشدخ وبقي ظاهره صحيحا ويدخل فيه الجرح العمد الذي يعصر فيرم","what_is_not_ar":"ليس مرض الإنسان أو حزنه إلا بالتشبيه عند بعض المصادر"},"support_links":[]},{"boundary":"Gerekli sınır, yağmurun derine işlemesi ve nemli toprağın birleşip topaklanmasıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001043/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَمَد","morph_features":"STEM|POS:N|LEM:Eamad|ROOT:Emd|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:9:2:1","qac_word_ref":"104:9:2","surface_ar":"عَمَدٍ"}],"gloss":"yağmurla derinden ıslanıp topaklanan toprak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yağmur suyu yalnız yüzeyi ıslatmaz, toprağın nemli alt katmanlarına kadar işler."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Islanan toprak parçaları üst üste gelir, birleşir ve avuçta topaklanır."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yağmurun derine işlediği ve nemli toprağın elde birleşip topaklandığı zemin için uygundur.","boundary_detail":"Gerekli sınır, yağmurun derine işlemesi ve nemli toprağın birleşip topaklanmasıdır.","branch_image_ar":"ثرى عمد","concept_gloss":"yağmurla derinden ıslanıp topaklanan toprak","contextual_glosses":[{"applicability":"Eylem, yağmur suyunun yüzeyden aşağı inip nemli toprak katmanına ulaşmasını anlatıyorsa kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yağmur suyunun toprağa derinlemesine işlemesini korur."},"facet_ids":["F001"],"text":"yağmur toprağın derinine işledi","usage_role":"contextual"}],"definition":"Yağmurun toprağın alt katmanlarına işlemesiyle nemli toprağın üst üste birikip elde topaklanacak ölçüde birleşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yağmur suyu yalnız yüzeyi ıslatmaz, toprağın nemli alt katmanlarına kadar işler."},{"facet_id":"F002","role":"core","statement":"Islanan toprak parçaları üst üste gelir, birleşir ve avuçta topaklanır."}],"identity_rationale":"Kaynak anlatımı, yağmur suyunun toprağın alt katmanlarına işlemesini, nemli toprağın üst üste yığılıp elde topaklanmasını açıkça bildirir. Dal yalnız yüzey ıslaklığına indirgenemez.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"yağmurla ıslanıp avuçta topaklanan toprak"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"yağmur toprağın derinine işledi"}],"lexicalization_note":"Tanım, nemli toprak söz öbeği ile yağmurun yere işlemesini bildiren kullanımı ayrı tutarak ortak sonucu açıklar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; derin ıslanma ve topaklanmayı genel nemli toprak alanından ayıran komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli bir derine işleme ve topaklanma sürecine bağlıdır; komşu dal nemli toprak ve ıslaklık için daha geniş, süreç belirtmeyen bir alana sahiptir.","focus_only":"Yağmurun derine işlemesi ve toprağın avuçta topaklanacak biçimde birleşmesini gerektirir.","gloss":"nemli toprak ve ıslaklık","neighbor_only":"Nemli toprak yanında genel ıslaklık, ter nemi ve başka ıslanmış maddeleri de kapsar.","neighbor_ref":"root_000198/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da nemli toprağı ve yağmurla oluşan ıslaklığı anlatabilir."}],"source_phrase_ar":"ثرى عمد إذا بلته الأمطار (maqayis); عمدت الأرض إذا رسخ فيها المطر إلى الثرى وتعقد في كفك (maqayis;tahdhib); عمد الثرى إذا بلله المطر وتعقد واجتمع من ندوته (sihah); عمد الثرى إذا كان تراكب بعضه على بعض وندي (tahdhib)","source_summary":"Kaynaklar, yağmurun toprağa derinlemesine işlemesi ve nemli toprağın birikip elde topaklanması sonucunda birleşir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الثرى أو الأرض إذا رسخ فيها المطر فاجتمع التراب وتعقد في الكف","what_is_not_ar":"ليس العمود ولا القصد ولا الوجع"},"support_links":[]},{"boundary":"Dal genel gençlikten ve genel şişmanlıktan daha dardır; gençlik dolgunluğu ile gelişkin beden birlikte önemlidir.","branch_kind":"bare","branch_ref":"root_001043/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَمَد","morph_features":"STEM|POS:N|LEM:Eamad|ROOT:Emd|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:9:2:1","qac_word_ref":"104:9:2","surface_ar":"عَمَدٍ"}],"gloss":"gençliğinin dolgun çağında, gelişkin bedenli","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, gençliğin olgun ve dolgun evresinde gelişkin bir bedene sahiptir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişil biçim, gövdeli ve dolgun yapılı kadını belirtir."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaşça genç olmanın yanında bedenin dolgun, gelişkin ve güçlü oluşu da anlatıldığında uygundur.","boundary_detail":"Dal genel gençlikten ve genel şişmanlıktan daha dardır; gençlik dolgunluğu ile gelişkin beden birlikte önemlidir.","branch_image_ar":"الشاب العمداني","concept_gloss":"gençliğinin dolgun çağında, gelişkin bedenli","contextual_glosses":[{"applicability":"Genç bir kişinin bedensel dolgunluğu ve gücü özellikle belirtilmek istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gençliği, bedensel gelişkinliği ve güçlülüğü korur."},"facet_ids":["F001"],"text":"güçlü ve gelişkin yapılı genç","usage_role":"contextual"}],"definition":"Gençliğinin dolgun çağında bulunan, bedeni gelişkin ve güçlü genç; dişil kullanımda ise gövdeli ve dolgun yapılı kadındır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, gençliğin olgun ve dolgun evresinde gelişkin bir bedene sahiptir."},{"facet_id":"F002","role":"extension","statement":"Dişil biçim, gövdeli ve dolgun yapılı kadını belirtir."}],"identity_rationale":"Kaynak anlatımı, gençliğinin dolgunluğundaki güçlü genci ve gövdeli, dolgun yapılı kadını aynı bedensel gelişkinlik altında verir. Anlam yalnız yaşça genç olmayı değil, bedenin dolgun ve güçlü oluşunu da gerektirir.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"gençliğinin dolgun çağında, gelişkin bedenli kişi"}],"lexicalization_note":"Tanım, çıplak dalın gençlik çağındaki dolgun ve güçlü beden niteliğini verir; başka dalların kalıp anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; gençliğe bağlı gelişkinliği genel beden dolgunluğundan ayıran komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal insanın gençlik çağındaki gelişkin bedenine bağlıdır; komşu dal yaş ve insan sınırı olmadan genel şişmanlık ve beden dolgunluğunu kapsar.","focus_only":"Gençlik çağını ve gelişkin, güçlü beden yapısını birlikte gerektirir.","gloss":"bedensel dolgunluk ve şişmanlık","neighbor_only":"Çocuk, kertenkele veya deve gibi farklı canlılarda yaş sınırı olmadan şişmanlık ve dolgunluk bildirir.","neighbor_ref":"root_000352/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da bedenin dolgunlaşmasını ve etlenmesini anlatabilir."}],"source_phrase_ar":"العمد الشاب الممتلئ شبابا وهو العمداني وامرأة عمدانية ذات جسم وعبالة (maqayis); العمد الشاب الشديد الممتلئ شبابا والمرأة عمدانية (ayn); العمد الشاب الممتلىء شبابا وامرأة عمدانية (tahdhib)","source_summary":"Kaynaklar, gençliğinin dolgun çağındaki güçlü genç ile gövdeli ve dolgun yapılı kadın kullanımını ortaklaştırır.","sources":["MQ","AY","TA"],"what_is_ar":"يدخل فيه العمد الشاب الممتلئ شبابا والعمداني والمرأة العمدانية ذات الجسم والعبالة","what_is_not_ar":"ليس العمود ولا تعمد الفعل ولا المرض"},"support_links":[]},{"boundary":"Anlam yalnızca sağlanan karşılaştırmalı kalıba bağlıdır ve iki kaynak yorumunun açıklıkla ayrı tutulmasını gerektirir.","branch_kind":"non_bare","branch_ref":"root_001043/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَمَد","morph_features":"STEM|POS:N|LEM:Eamad|ROOT:Emd|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:9:2:1","qac_word_ref":"104:9:2","surface_ar":"عَمَدٍ"}],"gloss":"bundan daha fazlası veya şaşırtıcısı var mı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sabit karşılaştırma kalıbı, verilen örneği değerlendirir ve iki farklı yorum taşır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir yorumda kalıp, verilen örnekten daha fazlasının bulunup bulunmadığını sorar."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Diğer yorumda kalıp, verilen örneğin olağanüstü şaşırtıcılığını dile getirir."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca verilen sabit karşılaştırma kalıbının iki aktarılan yorumunu birlikte görünür kılmak için uygundur.","boundary_detail":"Anlam yalnızca sağlanan karşılaştırmalı kalıba bağlıdır ve iki kaynak yorumunun açıklıkla ayrı tutulmasını gerektirir.","branch_image_ar":"صيغة أعمد من كذا","concept_gloss":"bundan daha fazlası veya şaşırtıcısı var mı","contextual_glosses":[{"applicability":"Kalıp, verilen örneğin şaşırtıcılığını soru biçiminde vurguladığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Soru biçimini ve güçlü şaşırma değerlendirmesini korur."},"facet_ids":["F003"],"text":"bundan daha şaşırtıcı ne olabilir","usage_role":"contextual"}],"definition":"Belirli bir karşılaştırmalı söz kalıbı, verilen örneği aşan bir şey olup olmadığını sorma veya o örneğin şaşırtıcılığını belirtme biçiminde iki türlü yorumlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sabit karşılaştırma kalıbı, verilen örneği değerlendirir ve iki farklı yorum taşır."},{"facet_id":"F002","role":"source_variant","statement":"Bir yorumda kalıp, verilen örnekten daha fazlasının bulunup bulunmadığını sorar."},{"facet_id":"F003","role":"source_variant","statement":"Diğer yorumda kalıp, verilen örneğin olağanüstü şaşırtıcılığını dile getirir."}],"identity_rationale":"Kaynak anlatımı, belirli kalıbın iki aktarılan açıklamasını verir: verilen örnekten daha fazla olup olmadığını sorma ve onu daha şaşırtıcı bulma. Dal korunabilir, ancak bu iki yorum tek ve kesin bir anlama indirgenemez.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"bundan daha fazlası mı, yoksa daha şaşırtıcısı mı"}],"lexicalization_note":"Tanım, artış sorusu ile şaşırma yorumunu yalnızca sabit karşılaştırmalı kalıpta tutar; bağımsız bir kök anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kalıplaşmış anlatım ortaklığını ama anlam ayrılığını en iyi gösteren komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal daha fazla olma ve şaşırtıcılık çevresinde yorumlanır; komşu dal yalnızca gerçekleşme hızını değerlendirir, bu nedenle anlam bakımından birbirinin yerine geçmez.","focus_only":"Artış sorusu ile şaşırma arasında iki aktarılan yoruma sahip özel bir karşılaştırma kalıbıdır.","gloss":"ne çabuk oldu","neighbor_only":"Bir olayın ne kadar çabuk gerçekleştiğini ünlemli ya da bildirmeli kalıpla anlatır.","neighbor_ref":"root_000698/B003","relation_type":"same_field","shared_zone":"Her ikisi de kalıplaşmış, güçlü değerlendirme veya şaşırma bildiren sözlerdir."}],"source_phrase_ar":"أعمد من سيد قتله قومه (maqayis;sihah;tahdhib); هل زاد على سيد قتله قومه (maqayis;tahdhib); أعجب من سيد قتله قومه (maqayis;tahdhib); أنا أعمد من كذا أي أعجب منه (sihah)","source_summary":"Toplu anlatım, aynı sabit kalıp için artış sorusu ile şaşırma bildiren iki açıklama aktarır; kanıt bunlardan birini tek geçerli yorum olarak seçmez.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه قولهم أعمد من سيد قتله قومه وأعمد من كذا على معنى هل زاد على هذا أو أعجب منه","what_is_not_ar":"ليس القصد ولا العماد الحسي ولا وجع المرض"},"support_links":[]},{"boundary":"Anlam, genel olarak bir boşluğu kapatmak değil, selin akış yönünü kapatıp suyu biriktirmektir.","branch_kind":"non_bare","branch_ref":"root_001043/B013","candidate_links":[{"candidate_id":"cand_8dfdd1ef449081def590","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَمَد","morph_features":"STEM|POS:N|LEM:Eamad|ROOT:Emd|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:9:2:1","qac_word_ref":"104:9:2","surface_ar":"عَمَدٍ"}],"gloss":"selin önünü kapatıp suyu biriktirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Selin aktığı yön, toprak ya da taşla fiziksel olarak kapatılır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kapatmanın sonucu, akışın durması ve suyun bir yerde birikmesidir."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sel akışının toprak veya taşla durdurulduğu ve suyun belirli bir yerde toplandığı işlem için uygundur.","boundary_detail":"Anlam, genel olarak bir boşluğu kapatmak değil, selin akış yönünü kapatıp suyu biriktirmektir.","branch_image_ar":"سد مجرى السيل","concept_gloss":"selin önünü kapatıp suyu biriktirme","contextual_glosses":[{"applicability":"Taş kullanılarak sel akışının kesildiği ve suyun bir yerde biriktirildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taşla kapatma işlemini ve suyu toplama sonucunu korur."},"facet_ids":["F001","F002"],"text":"sel yatağını taşla kapatıp suyu topladı","usage_role":"contextual"}],"definition":"Sel suyunun akış yönünü toprak veya taşla kapatarak suyun belirli bir yerde toplanmasını sağlamaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Selin aktığı yön, toprak ya da taşla fiziksel olarak kapatılır."},{"facet_id":"F002","role":"core","statement":"Kapatmanın sonucu, akışın durması ve suyun bir yerde birikmesidir."}],"identity_rationale":"Tek kaynak anlatımı, sel akışının önünü toprak veya taşla kapatıp suyu bir yerde toplama işlemini bütün aşamalarıyla açıkça verir.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"selin önünü kapatıp suyu bir yerde toplamak"}],"lexicalization_note":"Tanım, yalnızca sel akışını kapatma kullanımına bağlıdır ve bunu genel bir engelleme anlamına yaymaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kapatma eylemi ile sel bendinin kendisi arasındaki sınırı gösteren komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal toprak veya taşla yapılan kapatma işlemini ve birikme sonucunu anlatır; komşu dal ise suyu gerektiğinde geçirebilen yapısal engeli adlandırır.","focus_only":"Sel akışını kapatma eylemini ve suyun bir yerde birikmesi sonucunu bildirir.","gloss":"sel bendi","neighbor_only":"Seli geri çeviren ve gerektiği kadar su salabilen yapının kendisini adlandırır.","neighbor_ref":"root_000751/B007","relation_type":"near_neighbor","shared_zone":"Her ikisi de sel suyunu bir engelle tutma ve akışı denetleme durumuyla ilgilidir."}],"source_phrase_ar":"عمدت السيل تعميدا إذا سددت وجه جريته حتى يجتمع في موضع بتراب أو حجارة (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, selin önünü toprak veya taşla kapatma ve suyu bir yerde toplama sonucunu birlikte verir."}],"source_summary":"Bu dal yalnız bir kaynakta, sel yolunu toprak veya taşla kapatıp suyu bir yerde biriktirme işlemi olarak tanıklanmıştır.","sources":["TA"],"what_is_ar":"يدخل فيه تعميد السيل بسد وجه جريته بتراب أو حجارة حتى يجتمع في موضع","what_is_not_ar":"ليس عمود الشيء ولا قصد الشيء"},"support_links":["sup_34b036749dd7a638843f"]},{"boundary":"Anlam yalnızca verilen bağlı kullanımda geçerlidir; güvenip dayanma veya fiziksel direk anlamı taşımaz.","branch_kind":"non_bare","branch_ref":"root_001043/B014","candidate_links":[{"candidate_id":"cand_190412a5e54578fafdb6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَمَد","morph_features":"STEM|POS:N|LEM:Eamad|ROOT:Emd|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:9:2:1","qac_word_ref":"104:9:2","surface_ar":"عَمَدٍ"}],"gloss":"yanından ayrılmadan bağlı kalma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Özne, bağlandığı kişi veya şeyden ayrılmayıp onun yanında kalır."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi veya şeye sürekli eşlik etme ve ondan ayrılmama durumu sağlanan yapıyla anlatıldığında uygundur.","boundary_detail":"Anlam yalnızca verilen bağlı kullanımda geçerlidir; güvenip dayanma veya fiziksel direk anlamı taşımaz.","branch_image_ar":"لزوم الشيء","concept_gloss":"yanından ayrılmadan bağlı kalma","contextual_glosses":[{"applicability":"Öznenin bir kişi veya şeyle kalmayı sürdürdüğü bağlamlarda açık ve doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Süren bağlılığı ve yanından ayrılmama durumunu korur."},"facet_ids":["F001"],"text":"ona bağlı kaldı ve yanından ayrılmadı","usage_role":"contextual"}],"definition":"Bir kimseye veya şeye bağlı kalmak, yanından ayrılmamak ve onunla birlikte kalmayı sürdürmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Özne, bağlandığı kişi veya şeyden ayrılmayıp onun yanında kalır."}],"identity_rationale":"Tek kaynak anlatımı, belirli edatlı kullanımda bir kimseye veya şeye bağlı kalmayı ve ondan ayrılmamayı doğrudan bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"ona bağlı kalıp yanından ayrılmamak"}],"lexicalization_note":"Tanım, ayrılmadan yanında kalma anlamını yalnızca sağlanan edatlı yapıya bağlar ve çıplak köke genellemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kişiye veya şeye bağlı kalmayı genel yerleşme ve kalıcılıktan ayıran komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli yapıda bir kişi veya şeye bağlı kalmaya odaklanır; komşu dal yerleşme ve uzun süre bir yerde durma gibi daha geniş kullanımları da içerir.","focus_only":"Belirli edatlı yapıda bir kişi veya şeye bağlanıp yanından ayrılmamayı anlatır.","gloss":"kalma ve yerleşme","neighbor_only":"Bir yerde oturmayı ve bir bulutun uzun süre kalmasını da kapsayan daha geniş bir kalıcılık alanına sahiptir.","neighbor_ref":"root_000155/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir yerde veya bir şeyle kalmayı ve ayrılmamayı anlatabilir."}],"source_phrase_ar":"حلس به وعرس به وعمد به ولزب به إذا لزمه (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, bir kişi veya şeye bağlı kalma ve yanından ayrılmama anlamını verir."}],"source_summary":"Bu dal yalnız bir kaynakta, belirli edatlı yapıyla bir kişi veya şeye bağlı kalıp ondan ayrılmama anlamında tanıklanmıştır.","sources":["TA"],"what_is_ar":"يدخل فيه عمد به بمعنى لزمه أو أقام ملازما له","what_is_not_ar":"ليس الاعتماد على الشخص ولا عماد الخباء"},"support_links":["sup_881e018bd0267b81ad45"]},{"boundary":"Üstün gelme anlamı dışarıda bırakılır; öfke çekirdeği ile acı çekme uzantısı birbirinden ayrılır.","branch_kind":"bare","branch_ref":"root_001043/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَمَد","morph_features":"STEM|POS:N|LEM:Eamad|ROOT:Emd|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:9:2:1","qac_word_ref":"104:9:2","surface_ar":"عَمَدٍ"}],"gloss":"öfke ve onunla bağlantılı acılı sıkıntı","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çıplak adlandırmanın temel anlamı öfke ve kızgınlıktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İlgili eylem, üzüntü, öfke veya hastalık yüzünden acı çekmeyi de bildirebilir."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Öfke adını ve ilgili kullanımda öfke, üzüntü veya hastalık yüzünden çekilen acıyı birlikte göstermek için uygundur.","boundary_detail":"Üstün gelme anlamı dışarıda bırakılır; öfke çekirdeği ile acı çekme uzantısı birbirinden ayrılır.","branch_image_ar":"الغضب والغلبة بالغضب","concept_gloss":"öfke ve onunla bağlantılı acılı sıkıntı","contextual_glosses":[{"applicability":"Öfkenin yalnız duygu değil, kişiyi acı içinde bırakan bir sıkıntı olarak anlatıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öfkeyi ve onun doğurduğu acılı sıkıntıyı birlikte korur."},"facet_ids":["F001","F002"],"text":"öfke yüzünden acı çekti","usage_role":"contextual"}],"definition":"Öfke duygusudur; ilgili kullanım ayrıca üzüntü, öfke veya hastalık yüzünden acı çekmeyi anlatabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çıplak adlandırmanın temel anlamı öfke ve kızgınlıktır."},{"facet_id":"F002","role":"extension","statement":"İlgili eylem, üzüntü, öfke veya hastalık yüzünden acı çekmeyi de bildirebilir."}],"identity_rationale":"Kaynak anlatımı öfkeyi ve üzüntü, öfke veya hastalık yüzünden acı çekmeyi verir; geçici dal başlığındaki öfkeyle üstün gelme düşüncesini desteklemez. Dal, öfke ile ona veya başka ağır durumlara eşlik eden acılı sıkıntı olarak yeniden çerçevelenmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"öfke veya öfkenin verdiği acılı sıkıntı"}],"lexicalization_note":"Tanım, çıplak biçimdeki öfke anlamını temel alır ve acı çekme kullanımını bağlı bir uzantı olarak belirtir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; öfke çekirdeğini acılı sıkıntı ve hınç uzantıları üzerinden ayıran komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal öfkeyle bağlantılı acılı sıkıntıya uzanır; komşu dal ise hınç, kışkırtma ve öfkeli hayvan gibi farklı yönlere genişler.","focus_only":"Öfkenin yanında üzüntü veya hastalıktan doğan acı çekme kullanımını da içerir.","gloss":"öfke ve hınç","neighbor_only":"Kişiyi kışkırtan şeye yönelen hıncı ve öfkeli hayvan kullanımını da kapsar.","neighbor_ref":"root_000305/B003","relation_type":"near_synonym","shared_zone":"Her iki dalın temel alanında öfke ve kızgınlık duygusu bulunur."}],"source_phrase_ar":"العمد والضمد الغضب (tahdhib); عمد توجع من حزن أو غضب أو سقم (mufradat)","source_summary":"Toplu anlatım, temel olarak öfkeyi; ayrıca üzüntü, öfke veya hastalığın doğurduğu acılı sıkıntıyı aktarır. Üstün gelme anlamı desteklenmez.","sources":["TA","MU"],"what_is_ar":"يدخل فيه العمد بمعنى الغضب وما يتصل بتوجع الغضب","what_is_not_ar":"ليس القصد ولا العمود ولا مرض السقم"},"support_links":[]},{"boundary":"Bu dal yardım sağlama, suyun çoğalması, zaman süresi, irin ya da ölçü kabı anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001407/B001","candidate_links":[{"candidate_id":"cand_bc7a63f862b504e6d208","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُّمَدَّدَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|(II)|LEM:m~umad~adap|ROOT:mdd|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"104:9:3:1","qac_word_ref":"104:9:3","surface_ar":"مُّمَدَّدَةٍۭ"}],"gloss":"uzatma ve boyuna yayılma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel işlem, bir şeyi boyuna çekip uzunluğunu veya yayılımını artırarak uzatmak ya da bağlantılı hâle getirmektir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı çekirdek, bir şeyin kendiliğinden uzaması, bedenin gerinmesi, uzun boy ve uzağa erişen bakış için kullanılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gölgenin yayılması ve günün yükselip ilerlemesi, uzama görüntüsüne bağlı bağlamsal kullanımlardır."}}],"root_ar":"م د د","root_id":"root_001407","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin çekilerek uzatılmasını ve aynı uzama tasarımına bağlı fiziksel ya da algısal gerçekleşmeleri birlikte karşılar.","boundary_detail":"Bu dal yardım sağlama, suyun çoğalması, zaman süresi, irin ya da ölçü kabı anlamlarını kapsamaz.","branch_image_ar":"جر الشيء في طول حتى يتصل ويمتد","concept_gloss":"uzatma ve boyuna yayılma","contextual_glosses":[{"applicability":"Nesne, ip veya gölge gibi bir şeyin boyunu ya da yayılımını artırma bağlamlarında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kendiliğinden uzanma, bakış ve günle ilgili bağlı kullanımları kapsamaz.","preserves":"Bir şeyi çekerek daha uzun hâle getirme işlemini korur."},"facet_ids":["F001"],"text":"uzatmak","usage_role":"general"},{"applicability":"Bedenin ya da başka bir varlığın kendi ekseni boyunca yayılması ve gerilmesi söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir nesneyi dışarıdan çekip uzatma işlemini ve günle ilgili kullanımı dışarıda bırakır.","preserves":"Kendiliğinden gerçekleşen bedensel veya fiziksel uzamayı korur."},"facet_ids":["F002"],"text":"uzanmak veya gerinmek","usage_role":"contextual"}],"definition":"Bir şeyi boyuna çekerek uzunluğunu veya yayılımını artırmak, böylece onun uzanmasını ya da başka bir şeye ulaşarak bağlanmasını sağlamaktır. Bedenin gerinmesi, bakışın uzağa yönelmesi ve günün yükselmesi bu uzama tasarımına bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel işlem, bir şeyi boyuna çekip uzunluğunu veya yayılımını artırarak uzatmak ya da bağlantılı hâle getirmektir."},{"facet_id":"F002","role":"extension","statement":"Aynı çekirdek, bir şeyin kendiliğinden uzaması, bedenin gerinmesi, uzun boy ve uzağa erişen bakış için kullanılır."},{"facet_id":"F003","role":"associated_use","statement":"Gölgenin yayılması ve günün yükselip ilerlemesi, uzama görüntüsüne bağlı bağlamsal kullanımlardır."}],"identity_rationale":"Kaynak ifadesi, bir şeyi boyuna çekerek uzatma ve böylece uzanma ya da başka bir şeye bağlanma çekirdeğini açıkça verir. Gölge, bakış, boy, beden ve günle ilgili kullanımlar bu uzama çekirdeğinin farklı gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi boyuna çekip uzatmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"uzamak veya yayılmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"gölgeyi uzatıp yaymak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bakışı uzağa yöneltmek; görüş mesafesi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"günün yükselip ilerlemesi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"uzun boylu"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"gerinip uzanmak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"iplerle gerilip uzatılmış"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"birini oyalayıp çekiştirmek"}],"lexicalization_note":"Tanım genel uzatma çekirdeğini korur; gölge, bakış, gün ve boyla ilgili anlamları yalnız kendi kalıplaşmış bağlamlarında ele alır.","neighbor_coverage_note":"Adayların tümü değerlendirildi; fiziksel uzama ile en kolay karışan geniş uzama dalı ve destek ekleme dalı sınırı açıklamak için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekme ve boyuna uzatma işlemi belirgindir; komşu dal ise bu işlemi gerektirmeyen bedensel açılma ve hareket örneklerine daha geniş yer verir.","focus_only":"Odak dal, çekilen bir şeyin uzaması veya başka bir şeye bağlanması işlemini açıkça merkez alır.","gloss":"uzama ve gerilme","neighbor_only":"Komşu dal bedenin gerilmesi, yürürken ellerin hareketi ve gözlerin açılması gibi daha geniş özel gerçekleşmeleri de toplar.","neighbor_ref":"root_001432/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir varlığın uzunluk doğrultusunda açılması veya yayılması alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal boyut ve yayılım değişikliğidir; komşu dal ise alıcıya dışarıdan ek kaynak ya da destek ulaştırır.","focus_only":"Bir varlığın kendi uzunluğunu veya yayılımını artıran fiziksel uzatma söz konusudur.","gloss":"uzatma ve destek ekleme","neighbor_only":"Başka bir varlığa yardım, yiyecek, kişi veya mal gibi bir ek sağlayarak onu destekleme söz konusudur.","neighbor_ref":"root_001407/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da mevcut olana bir devam veya artış kazandırma tasarımı bulunur."}],"source_phrase_ar":"جر شيء في طول واتصال شيء بشيء في استطالة (maqayis)؛ مددت الشيء ومددت الحبل فامتد (maqayis;jamhara;sihah;tahdhib)؛ أصل المد الجر ومد الظل ومددت عيني (mufradat)؛ مد النهار ارتفاعه ومد البصر ورجل مديد القامة وتمدد الرجل (maqayis;sihah;tahdhib)","source_summary":"Kaynakların ortak çizgisi, boyuna çekme ile ortaya çıkan uzama, yayılma veya bağlantıdır; nesne, ip, gölge, bakış, boy, beden ve gün örnekleri bu çizgiyi somutlaştırır.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه مد الشيء والحبل والظل والبصر والقامة والتمدد وارتفاع النهار حيث يظهر معنى الطول أو الامتداد أو السعة.","what_is_not_ar":"لا يدخل فيه الإمداد بالعون أو الطعام، ولا القيح، ولا المكيال إلا بعلاقة اشتقاقية منفصلة."},"support_links":["sup_56ddf1c23818bcc9bf75"]},{"boundary":"Bu dal yalın fiziksel uzamayı değil, bir alıcıya eklenen ve onu besleyen yardım, kaynak veya miktarı anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001407/B002","candidate_links":[{"candidate_id":"cand_3afc84ebba1f0f300469","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُّمَدَّدَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|(II)|LEM:m~umad~adap|ROOT:mdd|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"104:9:3:1","qac_word_ref":"104:9:3","surface_ar":"مُّمَدَّدَةٍۭ"}],"gloss":"destekleyici ek sağlama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, bir alıcıya dışarıdan yardım, kaynak veya miktar ekleyerek onu desteklemek ve sürdürmektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Asker, yardımcı kişi, yiyecek ve mal sağlama, destekleyici ekin başlıca somut gerçekleşmeleridir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Toprağa verimi artıracak madde katmak ve bir söz dizisinin sayıca çokluğunu belirtmek aynı artış tasarımının uzantılarıdır."}}],"root_ar":"م د د","root_id":"root_001407","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yardım, insan, yiyecek, malzeme veya sayı ekleyerek bir alıcıyı güçlendirme ve sürdürme çekirdeğinin tamamına uygulanır.","boundary_detail":"Bu dal yalın fiziksel uzamayı değil, bir alıcıya eklenen ve onu besleyen yardım, kaynak veya miktarı anlatır.","branch_image_ar":"زيادة موصولة تمد غيرها بعون أو مادة","concept_gloss":"destekleyici ek sağlama","contextual_glosses":[{"applicability":"Bir orduya veya topluluğa yardımcı insan ya da kuvvet eklendiği bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yiyecek, toprak malzemesi ve sayısal çokluk gibi kuvvet dışı ekleri bütünüyle karşılamaz.","preserves":"Dışarıdan destek unsuru ekleyerek güçlendirme işlemini korur."},"facet_ids":["F001","F002"],"text":"takviye etmek","usage_role":"contextual"},{"applicability":"Bir kişi veya topluluğun devamını sağlayan yiyecek, mal ya da başka bir destek verildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Toprağa madde ekleme ve sözlerin sayısal çokluğu uzantılarını dışarıda bırakır.","preserves":"Alıcıyı sürdüren dış kaynak sağlama ilişkisini korur."},"facet_ids":["F001","F002"],"text":"kaynak sağlamak","usage_role":"general"}],"definition":"Bir kişi, topluluk veya şeyi sürdürmek ya da güçlendirmek için ona yardım, insan, yiyecek, malzeme veya miktar eklemektir. Eklenen unsur, alıcının devamını sağlayan bağlı bir kaynak veya çoğalma olabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, bir alıcıya dışarıdan yardım, kaynak veya miktar ekleyerek onu desteklemek ve sürdürmektir."},{"facet_id":"F002","role":"specialization","statement":"Asker, yardımcı kişi, yiyecek ve mal sağlama, destekleyici ekin başlıca somut gerçekleşmeleridir."},{"facet_id":"F003","role":"extension","statement":"Toprağa verimi artıracak madde katmak ve bir söz dizisinin sayıca çokluğunu belirtmek aynı artış tasarımının uzantılarıdır."}],"identity_rationale":"Kaynak ifadesi, bir topluluğa veya kişiye yardım, asker, yiyecek ya da başka bir madde ekleyerek onu destekleme anlamını; ayrıca bir şeye bağlı artış sağlayan malzemeyi açıkça bir araya getirir. Toprağa ekleme ve sayıca çoğaltma da bu destekleyici ek çekirdeğine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"orduya destek kuvvet göndermek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yardım veya takviye kuvvet"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"bir topluluğa destek olmak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yiyecek veya benzeri kaynak sağlamak"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bağlı ek; başka bir şeyi besleyen kaynak"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"toprağa toprak veya gübre eklemek"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"sözlerinin sayısı ve çokluğu"}],"lexicalization_note":"Tanım destekleyici ek çekirdeğini verir; ordu, yiyecek, toprak ve söz sayısıyla ilgili anlamlar yalnız belgelenmiş kuruluşları içinde korunur.","neighbor_coverage_note":"Adayların tümü karşılaştırıldı; yardım ve güçlendirme ile genel çokluk alanları, destekleyici ek koşulunu en açık gösteren iki sınır olarak yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ayırt edici yönü alıcıya somut veya sayısal bir ek ulaştırmaktır; komşu dalda güç ve yardım ilişkisi böyle bir ek gerektirmez.","focus_only":"Destek, insanın yanı sıra yiyecek, malzeme, toprak katkısı veya sayısal artış biçiminde olabilir.","gloss":"destek ve güçlendirme","neighbor_only":"Komşu dal doğrudan güç, sağlamlık, yardım ve dayanışmayı merkez alır.","neighbor_ref":"root_000027/B001","relation_type":"near_synonym","shared_zone":"İki dal da başka birini destekleme ve gücünü artırma bağlamında kullanılabilir."},{"boundary_match":"partial","distinction":"Odak dal artışı bir alıcıya sağlanan destek ilişkisine bağlar; komşu dal ise destek ilişkisi aramadan salt çokluğu kapsar.","focus_only":"Artış, belirli bir alıcıyı besleyen veya destekleyen bağlı bir ek olarak sunulur.","gloss":"destekleyici artış ve çokluk","neighbor_only":"Komşu dal genel olarak çokluk, sayının büyümesi ve azlığın karşıtını anlatır.","neighbor_ref":"root_001286/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda sayı ya da miktarın artması söz konusu olabilir."}],"source_phrase_ar":"أمددت الجيش بمدد (maqayis;jamhara;sihah;tahdhib;mufradat)؛ الاستمداد طلب المدد ومددنا القوم صرنا مددا لهم وأمددناهم بغيرنا (sihah;tahdhib)؛ أمددناهم بفاكهة وأمددت الإنسان بطعام (sihah;mufradat)؛ المدد ما أمددت به قومك من طعام أو أعوان والمادة كل شيء يكون مدادا لغيره (tahdhib)؛ مددت الأرض إذا زدت فيها ترابا أو سمادا ومداد كلماته أي عددها وكثرتها (tahdhib)","source_summary":"Kaynaklar, yardım veya kaynak istemeyi ve sağlamayı; asker, yiyecek ve yardımcılarla desteklemeyi; ayrıca başka bir şeyi besleyen bağlı madde ya da artışı ortak bir anlam alanında toplar.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه إمداد الجيش والقوم والإنسان بالمدد أو الطعام أو الأعوان أو المال والبنين، وأن يصير قوم مددا لغيرهم، وكل مادة تكون مدادا لغيرها أو زيادة في الأرض واللبن والعدد.","what_is_not_ar":"لا يدخل فيه مجرد طول الشيء في نفسه، ولا مد الدواة، ولا المكيال إلا إذا تكلم المصدر عن الزيادة أو المادة."},"support_links":["sup_9921d44f046a5d1673aa"]},{"boundary":"Bu dal genel sıvı dökme anlamı değil, akarsu veya kuyuda akma, dolma, çoğalma ve başka sudan beslenme durumudur.","branch_kind":"mixed_non_bare","branch_ref":"root_001407/B003","candidate_links":[{"candidate_id":"cand_8dfdd1ef449081def590","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُّمَدَّدَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|(II)|LEM:m~umad~adap|ROOT:mdd|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"104:9:3:1","qac_word_ref":"104:9:3","surface_ar":"مُّمَدَّدَةٍۭ"}],"gloss":"suyun akıp çoğalması ve başka sudan beslenmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Su kaynağının akması, dolması ve su miktarının artması dalın temel durumudur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir nehir, kuyu veya denizin başka bir su kaynağı tarafından beslenip suyunun artırılması özel bir gerçekleşmedir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Suyun bir çalının gövdesinde yürümesi, akış çekirdeğinin bitkiye bağlı uzantısıdır."}}],"root_ar":"م د د","root_id":"root_001407","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Akarsu veya kuyunun akması, dolması, suyunun artması ve başka bir su kaynağı tarafından beslenmesi durumlarının tamamını karşılar.","boundary_detail":"Bu dal genel sıvı dökme anlamı değil, akarsu veya kuyuda akma, dolma, çoğalma ve başka sudan beslenme durumudur.","branch_image_ar":"ماء يجري ويمتلئ ويمده ماء آخر","concept_gloss":"suyun akıp çoğalması ve başka sudan beslenmesi","contextual_glosses":[{"applicability":"Bir nehir veya kuyunun dolduğu ve su miktarının arttığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka bir su kaynağının etkin biçimde beslemesi ve bitki gövdesindeki akış belirtilmez.","preserves":"Su kaynağının dolmasını ve su miktarının artmasını korur."},"facet_ids":["F001"],"text":"suyu yükselip çoğalmak","usage_role":"contextual"},{"applicability":"Bir nehir, kuyu veya denizin başka bir su kaynağının suyunu artırdığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Besleyici dış kaynak bulunmadan gerçekleşen akma ve dolma durumlarını kapsamaz.","preserves":"Bir su kaynağının diğerine su sağlayarak onu artırması ilişkisini korur."},"facet_ids":["F002"],"text":"suyla beslemek","usage_role":"contextual"}],"definition":"Bir akarsu veya su kaynağının akması, dolması ve suyunun çoğalmasıdır; bu çoğalma başka bir nehir, kuyu ya da denizden gelen suyla beslenme sonucu da gerçekleşebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Su kaynağının akması, dolması ve su miktarının artması dalın temel durumudur."},{"facet_id":"F002","role":"specialization","statement":"Bir nehir, kuyu veya denizin başka bir su kaynağı tarafından beslenip suyunun artırılması özel bir gerçekleşmedir."},{"facet_id":"F003","role":"extension","statement":"Suyun bir çalının gövdesinde yürümesi, akış çekirdeğinin bitkiye bağlı uzantısıdır."}],"identity_rationale":"Kaynak ifadesi nehrin akması, dolması ve suyunun çoğalması ile bir su kaynağının başka birini beslemesini birlikte bildirir. Dal bu nedenle yalnız akışı değil, su artışı ve dış suyla beslenme ilişkisini de korumalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"nehrin akması veya dolup suyunun artması"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"başka bir akarsuyun suyunu artırıp onu beslemesi"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"taşkın; suyun arttığı dönemlerdeki bolluk"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"çalının gövdesinde su yürümek"}],"lexicalization_note":"Tanım suya özgü akma ve çoğalma çekirdeğini korur; nehir, kuyu, deniz ve bitki gövdesi kullanımlarını kendi kuruluşlarıyla sınırlar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yüzeyde akan su ile kanala açılıp boşalan su, akışın yanı sıra dolma ve beslenme koşulunu göstermek için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yüzey akışına ek olarak dolma, su düzeyinin artması ve kaynaklar arası beslenme gibi durumları da kapsar; komşu dalda yüzeyde akıyor olmak yeterlidir.","focus_only":"Suyun dolup çoğalması ve bir kaynağın başka bir su kaynağınca beslenmesi de çekirdeğe dahildir.","gloss":"akan ve beslenen su","neighbor_only":"Komşu dal, yeryüzünde açıkça akan suyu ve bu tür su kaynaklarının adlarını merkez alır.","neighbor_ref":"root_000768/B002","relation_type":"near_neighbor","shared_zone":"İki dal da görünür biçimde akan doğal suyu kapsayabilir."},{"boundary_match":"partial","distinction":"Odak dal kaynak içindeki artış ve beslenme ilişkisidir; komşu dal ise suyun açılarak dışarı akması ve geçtiği kanal üzerine kuruludur.","focus_only":"Bir su kütlesinin dolması, çoğalması veya başka bir su kaynağından beslenmesi öne çıkar.","gloss":"su artışı ve akış yoluna boşalma","neighbor_only":"Komşu dal suyun bir akış yoluna açılıp boşalmasını ve akış kanalını öne çıkarır.","neighbor_ref":"root_000199/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda suyun hareket edip bir yatakta akması görülebilir."}],"source_phrase_ar":"مد النهر ومده نهر آخر (maqayis;jamhara;sihah;tahdhib;mufradat)؛ المد السيل وكثرة الماء أيام المدود (sihah;tahdhib)؛ امتد النهر ومد إذا امتلأ وقل ماء ركيتنا فمدتها ركية أخرى (tahdhib)؛ أمد العرفج إذا جرى الماء في عوده (sihah;tahdhib)؛ البحر يمده من بعده سبعة أبحر (mufradat)","source_summary":"Kaynaklar su kaynağında akma, dolma, su artışı veya başka bir kaynakça beslenme durumlarını aynı akış alanında verir; bitki gövdesinde su yürümesi de bu tasarıma bağlanır.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه مد النهر والسيل وكثرة الماء أيام المدود، وأن يمد نهر نهرا أو تمد ركية أخرى ركية، وجريان الماء في العرفج، وما يشبهه من بحر يمده بحر.","what_is_not_ar":"لا يدخل فيه الإمدان المالح الشاذ، ولا مد الدواة إلا من جهة صورة المادة السائلة لا من هذا الفرع."},"support_links":["sup_34b036749dd7a638843f"]},{"boundary":"Buradaki artış zamanla sınırlıdır; asker, yiyecek veya başka bir maddi destek sağlama bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001407/B004","candidate_links":[{"candidate_id":"cand_190412a5e54578fafdb6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُّمَدَّدَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|(II)|LEM:m~umad~adap|ROOT:mdd|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"104:9:3:1","qac_word_ref":"104:9:3","surface_ar":"مُّمَدَّدَةٍۭ"}],"gloss":"uzamış süre ve süreyi uzatma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli veya belirsiz bir zaman aralığı, vade ya da zamanın ulaştığı son nokta temel anlamı oluşturur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir vadenin veya ömrün uzatılması ve bir kişiye belirli davranışında daha çok zaman tanınması süre çekirdeğinin ettirgen uzantısıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yolculuğun uzun sürmesi, zaman aralığının uzamasına bağlı bir olay kullanımıdır."}}],"root_ar":"م د د","root_id":"root_001407","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Zaman aralığı veya vadeyi, bunların uzamasını ve bir eylemle daha uzun hâle getirilmesini birlikte karşılar.","boundary_detail":"Buradaki artış zamanla sınırlıdır; asker, yiyecek veya başka bir maddi destek sağlama bu dala girmez.","branch_image_ar":"أجل أو زمن يطال ويمتد","concept_gloss":"uzamış süre ve süreyi uzatma","contextual_glosses":[{"applicability":"Bir zaman aralığı ya da belirlenmiş son zaman anlatıldığında doğal ad karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Süreyi uzatma işlemini ve uzun süren yolculuk olayını doğrudan anlatmaz.","preserves":"Zaman aralığı ve son tarih anlamlarını korur."},"facet_ids":["F001"],"text":"süre veya vade","usage_role":"general"},{"applicability":"Vade, ömür ya da bir davranış için mevcut zamanın artırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İşlemden bağımsız süre adını ve kendiliğinden uzun süren yolculuğu kapsamaz.","preserves":"Mevcut zaman sınırını ileriye taşıma işlemini korur."},"facet_ids":["F002"],"text":"süre tanımak veya uzatmak","usage_role":"contextual"}],"definition":"Bir zaman aralığı, vade veya son nokta ile bu sürenin uzaması ya da uzatılmasıdır. Ömrü uzatma, birine yanlışında süre tanıma ve yolculuğun uzun sürmesi bu zaman çekirdeğine bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli veya belirsiz bir zaman aralığı, vade ya da zamanın ulaştığı son nokta temel anlamı oluşturur."},{"facet_id":"F002","role":"extension","statement":"Bir vadenin veya ömrün uzatılması ve bir kişiye belirli davranışında daha çok zaman tanınması süre çekirdeğinin ettirgen uzantısıdır."},{"facet_id":"F003","role":"associated_use","statement":"Yolculuğun uzun sürmesi, zaman aralığının uzamasına bağlı bir olay kullanımıdır."}],"identity_rationale":"Kaynak ifadesi zaman aralığı, son tarih veya vade ile bunların uzatılmasını; ömrü uzatma, yanlışta süre tanıma ve yolculuğun uzaması örneklerini ortak zaman ekseninde verir. Çekirdek hem uzamış süreyi hem de süreyi uzatma işlemini kapsar.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"süre, zaman aralığı veya vade"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"vadeyi ertelemek veya uzatmak"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"ömrünü uzatmak"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yanlışında ona süre tanımak"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yolculuğun uzaması"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"birini oyalayıp çekiştirmek"}],"lexicalization_note":"Tanım zaman süresi çekirdeğini verir; ömür, vade, yanlışta oyalama ve yolculukla ilgili anlamları yalnız belgelenmiş kuruluşlarında korur.","neighbor_coverage_note":"Tüm adaylar incelendi; genel zaman uzaması ile belirlenmiş son zaman, süre ve vade sınırını en yararlı biçimde açıklayan iki karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda süre ve vade adı ile bunları uzatma aynı söz varlığı içinde belirgindir; komşu dal uzun zaman ve mühlet alanını daha genel kurar.","focus_only":"Odak dal zaman parçası ve vade adını, yolculuğun uzun sürmesini ve belirli davranışta süre tanımayı birlikte kapsar.","gloss":"sürenin uzaması ve mühlet","neighbor_only":"Komşu dal uzun zaman, tekrar eden zaman ve mühlet tasarımını daha genel biçimde toplar.","neighbor_ref":"root_001446/B001","relation_type":"near_synonym","shared_zone":"İki dal da zamanın uzamasını, mühlet verilmesini ve ömrün uzun tutulmasını kapsar."},{"boundary_match":"partial","distinction":"Odak dal zamanın yayılımını ve uzatılmasını kapsar; komşu dalın ayırt edici yönü önceden belirlenmiş son noktadır.","focus_only":"Sürenin kendisi ve zamanın uzatılması ya da uzaması çekirdeğe dahildir.","gloss":"uzayan süre ve belirlenmiş son zaman","neighbor_only":"Komşu dal bir borç, ölüm veya iş için önceden belirlenmiş son zamanı ve bunun ertelenmesini merkez alır.","neighbor_ref":"root_000016/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal vade ve zaman sınırı bağlamlarında buluşabilir."}],"source_phrase_ar":"أطال مدته (maqayis)؛ أمددت لك في الأجل أنسأتك فيه والمدة الأجل (jamhara)؛ مد الله في عمره ومده في غيه أمهله وطول له ومدة من الزمان برهة منه (sihah)؛ المدة الغاية وأمد الله في عمرك وامتد بهم السير (tahdhib)؛ المدة للوقت الممتد ومددته في غيه (mufradat)","source_summary":"Kaynaklar bir zaman parçası, vade ve son nokta anlamlarıyla süreyi uzatma, ömrü çoğaltma, yanlış davranışta mühlet verme ve yolculuğun uzun sürmesini aynı zaman ekseninde birleştirir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه المدة للوقت الممتد والغاية والأجل، وإطالة العمر، والإمهال في الغي أو الشر، وطول السير.","what_is_not_ar":"لا يدخل فيه مدد العسكر أو المال إلا إذا كان السياق إمدادا لا إمهالا زمنيا."},"support_links":["sup_881e018bd0267b81ad45"]},{"boundary":"Anlam yalnız yazı sıvısı, hokkanın yenilenmesi ve kaleme bir dolum alınmasıyla sınırlıdır; hacim ölçüsü bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001407/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُّمَدَّدَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|(II)|LEM:m~umad~adap|ROOT:mdd|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"104:9:3:1","qac_word_ref":"104:9:3","surface_ar":"مُّمَدَّدَةٍۭ"}],"gloss":"yazı sıvısı ve hokkadan kaleme aktarılması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kalemin iz bırakmasını sağlayan yazı sıvısı, dalın nesne çekirdeğidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hokkaya su, boya veya yazı sıvısı ekleyerek içeriğini yenilemek bu nesneye bağlı hazırlama işlemidir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kalemi hokkaya batırarak bir yazımlık sıvı almak, yazı sıvısının kaleme aktarılması aşamasıdır."}}],"root_ar":"م د د","root_id":"root_001407","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yazı sıvısının kendisini, hokkanın yenilenmesini ve kaleme bir dolum alınmasını aynı süreç içinde karşılar.","boundary_detail":"Anlam yalnız yazı sıvısı, hokkanın yenilenmesi ve kaleme bir dolum alınmasıyla sınırlıdır; hacim ölçüsü bu dala girmez.","branch_image_ar":"دواة تمد القلم بمداد","concept_gloss":"yazı sıvısı ve hokkadan kaleme aktarılması","contextual_glosses":[{"applicability":"Yazı yazmada kullanılan sıvının adı gerektiğinde en doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hokkayı yenileme ve kaleme bir dolum alma işlemlerini anlatmaz.","preserves":"Kalemin yazmasını sağlayan sıvı nesneyi korur."},"facet_ids":["F001"],"text":"mürekkep","usage_role":"general"},{"applicability":"Hokkaya su, boya veya yazı sıvısı eklenerek içeriği yenilendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yazı sıvısının adını ve kalemin tek dolumluk sıvı almasını kapsamaz.","preserves":"Hokkaya yazı için gerekli sıvıyı ekleme işlemini korur."},"facet_ids":["F002"],"text":"hokkayı doldurmak","usage_role":"contextual"}],"definition":"Yazı yazmak için kullanılan sıvı ile bu sıvıyı hokkaya su veya boya ekleyerek yenileme ve kaleme hokkadan bir dolum alma işlemleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kalemin iz bırakmasını sağlayan yazı sıvısı, dalın nesne çekirdeğidir."},{"facet_id":"F002","role":"associated_use","statement":"Hokkaya su, boya veya yazı sıvısı ekleyerek içeriğini yenilemek bu nesneye bağlı hazırlama işlemidir."},{"facet_id":"F003","role":"associated_use","statement":"Kalemi hokkaya batırarak bir yazımlık sıvı almak, yazı sıvısının kaleme aktarılması aşamasıdır."}],"identity_rationale":"Kaynak ifadesi yazıda kullanılan sıvıyı, hokkaya su veya boya ekleyerek onu yenilemeyi ve kalemle hokkadan bir dolum almayı aynı yazı düzeni içinde açıkça bağlar. Dal genel destek verme değil, hokka ile kalem arasındaki yazı sıvısı döngüsüdür.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"mürekkep"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"hokkaya su veya mürekkep eklemek"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"kalemi hokkaya batırıp bir dolumluk mürekkep almak"}],"lexicalization_note":"Tanım yazı sıvısı adını ve ona bağlı hokka-kalem işlemlerini ayırır; hokkayı yenileme kuruluşu genel bir ek sağlama anlamına genişletilmez.","neighbor_coverage_note":"Adayların tümü değerlendirildi; yazı sıvısı bakımından en yakın dal ve aynı olayın kalem dalı, nesne ile araç sınırını göstermek için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sıvıyı hokkada hazırlama ve kaleme aktarma sürecini içerir; komşu dal esas olarak sıvı ve kap adlarıyla sınırlıdır.","focus_only":"Odak dal yazı sıvısının yanı sıra hokkayı yenileme ve kaleme tek dolum alma işlemlerini de kapsar.","gloss":"mürekkep ve hokka","neighbor_only":"Komşu dal yazı sıvısı ile onu tutan kabı adlandırır, aktarma işlemini çekirdeğe katmaz.","neighbor_ref":"root_000287/B003","relation_type":"near_synonym","shared_zone":"İki dal da yazıda kullanılan sıvıyı doğrudan kapsar."},{"boundary_match":"thematic_only","distinction":"Biri iz bırakan sıvıyı ve aktarımını, diğeri bu sıvıyı taşıyarak yazan aracı adlandırır; anlamsal çekirdekleri ortak değildir.","focus_only":"Odak dal yazıda kullanılan sıvı ve bu sıvının hokkadan alınmasıdır.","gloss":"mürekkep ve kalem","neighbor_only":"Komşu dal yazının sivriltilmiş çubuk biçimindeki aracıdır.","neighbor_ref":"root_001252/B003","relation_type":"thematic","shared_zone":"İki dal aynı yazma olayında birbirini tamamlayan gereçleri içerir."}],"source_phrase_ar":"المداد ما يكتب به لأنه يمد بالماء ومددت الدواة وأمددتها (maqayis)؛ أمددت الدواة إذا زدت في مائها ونقسها والمدة استمدادك من الدواة (jamhara)؛ المداد النقس ومددت الدواة وأمددتها وأمددت الرجل مدة بقلم (sihah)؛ مدني يا غلام أي أعطني مدة من الدواة (tahdhib)؛ من قولهم مددت الدواة (mufradat)","source_summary":"Kaynaklar yazıda kullanılan sıvıyı, hokkaya su veya boya eklenmesini ve kalemle hokkadan tek dolumluk sıvı alınmasını ortak yazı sürecinin parçaları olarak verir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه المداد الذي يكتب به، ومد الدواة أو إمدادها بالماء أو النقس، والاستمداد من الدواة وأخذ مدة بالقلم.","what_is_not_ar":"لا يدخل فيه مدد الجيش أو الطعام إلا من جهة لفظ المدد العام، ولا يدخل المكيال."},"support_links":[]},{"boundary":"Bu dal yalnız belirli geleneksel hacim ölçüsüdür; fiziksel uzatma veya yardım ekleme anlamı tanıma dahil edilmez.","branch_kind":"non_bare","branch_ref":"root_001407/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُّمَدَّدَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|(II)|LEM:m~umad~adap|ROOT:mdd|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"104:9:3:1","qac_word_ref":"104:9:3","surface_ar":"مُّمَدَّدَةٍۭ"}],"gloss":"dörtte birlik geleneksel hacim ölçüsü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli miktarı ölçen geleneksel bir hacim birimidir ve dört tanesi kendisinden büyük ilgili ölçüyü oluşturur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kaynak, adın kökle ilişkisini ölçülen miktarın benzeriyle tamamlanması üzerinden açıklar; birim kimliği ölçü adıdır."}}],"root_ar":"م د د","root_id":"root_001407","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tahıl ve benzeri maddeler için kullanılan, daha büyük ilgili birimin dörtte birine eşit özel ölçü adını karşılar.","boundary_detail":"Bu dal yalnız belirli geleneksel hacim ölçüsüdür; fiziksel uzatma veya yardım ekleme anlamı tanıma dahil edilmez.","branch_image_ar":"مد يقدر به الكيل","concept_gloss":"dörtte birlik geleneksel hacim ölçüsü","contextual_glosses":[{"applicability":"Birim adının bilinmediği bağlamlarda işlevini açıklamak için kullanılabilir.","error_profile":{"adds":null,"collision":"Farklı büyüklükteki küçük tahıl ölçekleriyle karışabilir.","fit":"narrowing","loses":"Daha büyük ilgili ölçünün tam dörtte biri olma oranını belirtmez.","preserves":"Tahıl gibi maddeleri ölçen küçük bir hacim birimi oluşunu korur."},"facet_ids":["F001"],"text":"küçük tahıl ölçeği","usage_role":"explanatory"}],"definition":"Tahıl ve benzeri maddelerin miktarını belirlemekte kullanılan, daha büyük bir ölçü biriminin dörtte birine eşit geleneksel bir hacim ölçüsüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli miktarı ölçen geleneksel bir hacim birimidir ve dört tanesi kendisinden büyük ilgili ölçüyü oluşturur."},{"facet_id":"F002","role":"source_variant","statement":"Bir kaynak, adın kökle ilişkisini ölçülen miktarın benzeriyle tamamlanması üzerinden açıklar; birim kimliği ölçü adıdır."}],"identity_rationale":"Kaynak ifadesi belirli bir hacim ölçüsünü ve onun daha büyük bir ölçünün dörtte biri oluşunu açıkça bildirir. Bir kaynakta ölçülen miktarın benzeriyle tamamlanmasına dayalı açıklama bulunsa da dalın eşzamanlı çekirdeği ölçü birimidir.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"daha büyük bir ölçünün dörtte biri olan geleneksel hacim ölçüsü"}],"lexicalization_note":"Tanım yalnız adlaşmış ölçü birimine bağlıdır ve kökün genel uzatma ya da ekleme anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı ölçü sistemindeki büyük birim ile başka bir küçük ölçü, birimin oranını ve ayrı kimliğini açıklamak için seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak birim komşu birimin dörtte biridir; komşu birim daha büyüktür ve ayrıca kap işlevi taşıyabilir.","focus_only":"Odak dal daha küçük ölçüdür ve dört tanesi komşu ölçünün miktarına eşittir.","gloss":"küçük ve büyük hacim ölçüleri","neighbor_only":"Komşu dal dört odak birimine eşit daha büyük ölçüdür ve içme kabı olarak da kullanılabilir.","neighbor_ref":"root_000892/B004","relation_type":"same_field","shared_zone":"İki dal aynı geleneksel hacim ölçme sistemine aittir."},{"boundary_match":"field_only","distinction":"Aynı alana ait olsalar da ayrı ölçü birimleridir; odak dalın dörtte birlik sistem ilişkisi komşuda yoktur.","focus_only":"Odak ölçünün daha büyük ilgili birime karşı dörtte birlik oranı kaynaklarda belirlenmiştir.","gloss":"iki küçük hacim ölçüsü","neighbor_only":"Komşu dal yalnız başka bir küçük ölçü adını bildirir ve aynı oran ilişkisini taşımaz.","neighbor_ref":"root_000204/B009","relation_type":"same_field","shared_zone":"Her iki dal geleneksel küçük miktarları ölçen birim adlarıdır."}],"source_phrase_ar":"المد من المكاييل لأنه يمد المكيل بالمكيل مثله (maqayis)؛ المد مكيال معروف والجمع مداد (jamhara)؛ المد بالضم مكيال والصاع أربعة أمداد (sihah)؛ المد مكيال معلوم وهو ربع الصاع ومد وثلاثة أمداد ومدد ومداد كثيرة (tahdhib)؛ المد من المكاييل معروف (mufradat)","source_summary":"Kaynaklar bunun bilinen bir hacim ölçüsü olduğunu ortakça verir; bazı kaynaklar dört birimin daha büyük ilgili ölçüyü oluşturduğunu, bir kaynak da adın kökle ilişkisini ölçülen miktarın benzeriyle tamamlanması üzerinden açıklar.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه المد مكيالا معروفا وأمداده وجمعه مداد، وكونه ربع الصاع أو ما يقدره أهل الحجاز والعراق.","what_is_not_ar":"لا يدخل فيه مد الشيء طولا ولا مدد العسكر، وإن علله بعض المصادر بمد المكيل بمثله."},"support_links":[]},{"boundary":"Bu dal yalnız irin ile yaranın irinlenme durumudur; zaman aralığı ve yazı sıvısı anlamları dışarıda tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_001407/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُّمَدَّدَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|(II)|LEM:m~umad~adap|ROOT:mdd|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"104:9:3:1","qac_word_ref":"104:9:3","surface_ar":"مُّمَدَّدَةٍۭ"}],"gloss":"yarada biriken veya yaradan çıkan irin","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yarada biriken ya da yaradan dışarı çıkan irin, dalın temel nesnesidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yaranın irin oluşturması veya irinle dolması, temel nesneye bağlı durum değişikliğidir."}}],"root_ar":"م د د","root_id":"root_001407","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İrinin kendisini ve yaranın bu irin nedeniyle irinli hâle gelmesini kapsar.","boundary_detail":"Bu dal yalnız irin ile yaranın irinlenme durumudur; zaman aralığı ve yazı sıvısı anlamları dışarıda tutulur.","branch_image_ar":"جرح تمتد فيه مدة من قيح","concept_gloss":"yarada biriken veya yaradan çıkan irin","contextual_glosses":[{"applicability":"Yarada biriken veya yaradan çıkan yoğun iltihap sıvısının adı gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yaranın irinli hâle gelmesini bir süreç olarak tek başına anlatmaz.","preserves":"Yarada biriken ya da çıkan sıvı nesneyi tam olarak korur."},"facet_ids":["F001"],"text":"irin","usage_role":"general"},{"applicability":"Yaranın irin oluşturduğu veya irinle dolduğu durum değişikliğini anlatır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İrinin bağımsız adını ve yaradan çıkışını doğrudan karşılamaz.","preserves":"Yaranın irinli hâle gelmesi sürecini korur."},"facet_ids":["F002"],"text":"yara irinlenmek","usage_role":"contextual"}],"definition":"Bir yarada biriken veya yaradan çıkan irin ile yaranın bu sıvıyı oluşturup irinli hâle gelmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yarada biriken ya da yaradan dışarı çıkan irin, dalın temel nesnesidir."},{"facet_id":"F002","role":"associated_use","statement":"Yaranın irin oluşturması veya irinle dolması, temel nesneye bağlı durum değişikliğidir."}],"identity_rationale":"Kaynak ifadesi yarada biriken veya yaradan çıkan irini ve yaranın irinli hâle gelmesini açıkça aynı dalda verir. Zaman süresine benzeyen yazım bu tıbbi nesne ve durum anlamını değiştirmez.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"yara irinlenmek"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"yarada biriken veya yaradan çıkan irin"}],"lexicalization_note":"Tanım irin adını ve yaranın irinli hâle gelmesini ayırır; yara kuruluşu genel bir bozulma veya zaman anlamına genişletilmez.","neighbor_coverage_note":"Adayların tümü incelendi; tam örtüşen irinlenme dalı ile irin sonucunda bozulmayı anlatan dal, nesne ve sonuç sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kaynak kartlarında çekirdek ve sınır aynıdır; ikisi de irinin yarada toplanması, oluşması veya dışarı çıkmasını kapsar.","focus_only":null,"gloss":"yaranın irinlenmesi","neighbor_only":null,"neighbor_ref":"root_001664/B004","relation_type":"synonym","shared_zone":"İki dal da yarada irinin birikmesini veya yaradan çıkmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği irin ve irinlenmedir; komşu dalda ayırt edici sonuç dokunun bozulmasıdır.","focus_only":"Odak dal irinin kendisini ve yarada birikmesini ya da çıkmasını adlandırır.","gloss":"irin ve irinli bozulma","neighbor_only":"Komşu dal yaranın veya ülserin irin nedeniyle bozulmasını merkez alır.","neighbor_ref":"root_000025/B011","relation_type":"near_neighbor","shared_zone":"Her iki dal irin bulunan bir yara durumuyla ilgilidir."}],"source_phrase_ar":"أمد الجرح صارت فيه مدة وهي ما يخرج (maqayis)؛ أمد الجرح (jamhara;tahdhib)؛ المدة بالكسر ما يجتمع في الجرح من القيح وأمد الجرح صارت فيه مدة (sihah)؛ مدة الجرح (mufradat)","source_summary":"Kaynaklar yarada toplanan ya da ondan çıkan irini ve yaranın irinli hâle gelmesini ortak biçimde bildirir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه أمد الجرح وصارت فيه مدة، أي ما يخرج أو يجتمع فيه من القيح.","what_is_not_ar":"لا يدخل فيه مدة الزمان، ولا مداد الدواة، مع تشابه الرسم."},"support_links":[]},{"boundary":"Bu dal yalnız develere tahıl veya tohum karıştırılmış su içirme geleneğiyle sınırlıdır; yalın su verme kapsanmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001407/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُّمَدَّدَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|(II)|LEM:m~umad~adap|ROOT:mdd|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"104:9:3:1","qac_word_ref":"104:9:3","surface_ar":"مُّمَدَّدَةٍۭ"}],"gloss":"deveye içirilen tahıllı su","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel işlem, develere tahıl veya tohum karıştırılmış su içirmektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İçecek, suyla karıştırılan un, ezilmiş arpa, başka tahıl, tohum veya susamdan hazırlanabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Develere içirilmek üzere hazırlanmış bu sulu tahıl karışımı ayrıca bir nesne adı olarak kullanılır."}}],"root_ar":"م د د","root_id":"root_001407","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Develere tahıl veya tohum katılmış su içirme işlemini ve bu amaçla hazırlanan karışımı birlikte karşılar.","boundary_detail":"Bu dal yalnız develere tahıl veya tohum karıştırılmış su içirme geleneğiyle sınırlıdır; yalın su verme kapsanmaz.","branch_image_ar":"ماء الإبل يمد بدقيق ونحوه","concept_gloss":"deveye içirilen tahıllı su","contextual_glosses":[{"applicability":"Un, tohum veya ezilmiş tahıl suya katılıp develere içirildiğinde işlem karşılığı olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hazırlanan karışımın bağımsız nesne adını tek başına karşılamaz.","preserves":"Karışımı hazırlayıp develere içirme işlemini korur."},"facet_ids":["F001","F002"],"text":"develere tahıllı su içirmek","usage_role":"contextual"},{"applicability":"Develere içirilmek üzere hazırlanan su ve tahıl karışımının kendisi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":"İnsanlar için hazırlanan başka sulu tahıl karışımlarıyla bağlamsız kullanımda karışabilir.","fit":"narrowing","loses":"Karışımın özellikle develere içirilmesi işlemini tek başına bildirmez.","preserves":"Su ile tahıl veya tohumdan oluşan karışım nesnesini korur."},"facet_ids":["F002","F003"],"text":"sulu tahıl karışımı","usage_role":"explanatory"}],"definition":"Develere, içine un, ezilmiş tahıl, tohum veya susam katılmış su içirmek ve bu amaçla hazırlanan sulu tahıl karışımıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel işlem, develere tahıl veya tohum karıştırılmış su içirmektir."},{"facet_id":"F002","role":"specialization","statement":"İçecek, suyla karıştırılan un, ezilmiş arpa, başka tahıl, tohum veya susamdan hazırlanabilir."},{"facet_id":"F003","role":"associated_use","statement":"Develere içirilmek üzere hazırlanmış bu sulu tahıl karışımı ayrıca bir nesne adı olarak kullanılır."}],"identity_rationale":"Kaynak ifadesi develere un, ezilmiş tahıl, tohum veya susam karıştırılmış su içirme işlemini ve bu karışımın adını açıkça verir. Anlam genel hayvan sulama ya da genel yiyecek desteği değil, belirli karışımlı içecektir.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"develere unlu veya tohumlu su içirmek"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"develere içirilen suyla karıştırılmış ezme tahıl"}],"lexicalization_note":"Tanım deve, su ve tahıl ya da tohum karışımı koşullarını korur; kuruluş genel sulama veya besleme anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel deve sulama dalı karışım koşulunu, yem katkısı dalı ise içecek ile yem arasındaki sınırı en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal özel olarak besleyici katı madde karıştırılmış suyu gerektirir; komşu dal yalın sulamayı da kapsar.","focus_only":"Odak dalda suya un, tahıl, tohum veya susam karıştırılması zorunludur.","gloss":"develere karışımlı veya yalın su verme","neighbor_only":"Komşu dal develere herhangi bir su verme işlemini genel olarak anlatır.","neighbor_ref":"root_000505/B007","relation_type":"near_neighbor","shared_zone":"İki dal da develere su içirme olayında buluşur."},{"boundary_match":"thematic_only","distinction":"Odak dal içecek niteliğinde sulu karışımdır; komşu dal kuru yeme katılan çekirdeği ve yeme işlemini merkez alır.","focus_only":"Odak dal suya un, tahıl veya tohum katılarak hazırlanan ve içirilen bir karışımdır.","gloss":"deveye verilen karışımlı su ve yem","neighbor_only":"Komşu dal hurma çekirdeğinin kuru yeme katılıp hayvana yedirilmesini anlatır.","neighbor_ref":"root_001102/B010","relation_type":"thematic","shared_zone":"İki dal da develerin beslenmesinde başka bir maddeyle hazırlanmış karışımları içerir."}],"source_phrase_ar":"مددت الإبل مدا أسقيتها الماء بالدقيق أو بشيء تمده به والاسم المديد (maqayis)؛ مددت الإبل وأمددتها أن تنثر لها على الماء شيئا من الدقيق ونحوه فتسقيها (sihah)؛ مددت الإبل وهو أن يسقيها الماء بالبزر أو الدقيق أو السمسم والمديد شعير يجش (tahdhib)؛ مددت الإبل سقيتها المديد وهو بزر ودقيق يخلطان بماء (mufradat)","source_summary":"Kaynaklar develere suyla karıştırılmış un, tahıl veya tohum verilmesini ortak işlem olarak aktarır; karışımın malzemesi un, ezilmiş arpa, başka tohum ya da susam olabilir ve karışımın ayrı bir adı vardır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه مد الإبل أو إمدادها: أن يسقى البعير ماء خلط ببزر أو دقيق أو سمسم، والاسم المديد.","what_is_not_ar":"لا يدخل فيه مطلق إمداد الإنسان بالطعام، ولا ماء النهر."},"support_links":[]},{"boundary":"Dal yalnız belgelenmiş su kuruluşuna bağlıdır; nehir akışı, denizin başka denizden beslenmesi veya genel tuzluluk anlamına genişletilmez.","branch_kind":"collocation","branch_ref":"root_001407/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُّمَدَّدَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|(II)|LEM:m~umad~adap|ROOT:mdd|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"104:9:3:1","qac_word_ref":"104:9:3","surface_ar":"مُّمَدَّدَةٍۭ"}],"gloss":"tuzlalardaki çok tuzlu su","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kuruluşun çekirdeği, tuzluluk derecesi çok yüksek olan sudur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tuzla ve tuzlu düzlüklerdeki sular, bu çok tuzlu su adının başlıca çevresel gerçekleşmesidir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sözcüğün kökün olağan anlam örgüsünden ayrı sayılması, kuruluşun sözlüksel anlamına ilişkin bir sınıflandırma notudur."}}],"root_ar":"م د د","root_id":"root_001407","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız belgelenmiş su kuruluşunda, özellikle tuzla ortamındaki aşırı tuzlu suyu karşılar.","boundary_detail":"Dal yalnız belgelenmiş su kuruluşuna bağlıdır; nehir akışı, denizin başka denizden beslenmesi veya genel tuzluluk anlamına genişletilmez.","branch_image_ar":"ماء إمدان شديد الملوحة","concept_gloss":"tuzlalardaki çok tuzlu su","contextual_glosses":[{"applicability":"Suyun tuzla veya tuzlu düzlük ortamından geldiği açık olduğunda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tuzla dışında bulunabilecek çok yoğun tuzlu suyu kapsamayabilir.","preserves":"Suyun tuzla ortamına bağlı güçlü tuzluluğunu korur."},"facet_ids":["F001","F002"],"text":"tuzla suyu","usage_role":"contextual"},{"applicability":"Yer türü bilinmediğinde kuruluşun yüksek tuzluluk özelliğini açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tuzla sularıyla olan özel çevresel bağlantıyı belirtmez.","preserves":"Suyun olağan tuzlu sudan daha yüksek tuzluluğa sahip olmasını korur."},"facet_ids":["F001"],"text":"çok yoğun tuzlu su","usage_role":"explanatory"}],"definition":"Belirli bir su kuruluşunda adlandırılan, özellikle tuzlalarda bulunan çok yoğun tuzlu sudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kuruluşun çekirdeği, tuzluluk derecesi çok yüksek olan sudur."},{"facet_id":"F002","role":"specialization","statement":"Tuzla ve tuzlu düzlüklerdeki sular, bu çok tuzlu su adının başlıca çevresel gerçekleşmesidir."},{"facet_id":"F003","role":"source_variant","statement":"Sözcüğün kökün olağan anlam örgüsünden ayrı sayılması, kuruluşun sözlüksel anlamına ilişkin bir sınıflandırma notudur."}],"identity_rationale":"Kaynak ifadesi belirli kuruluşu çok tuzlu su ve özellikle tuzla suları olarak açıkça tanımlar. Bir kaynağın sözcüğü kökün olağan düzeninden ayrı sayması, bu kuruluşun belgelenmiş tuzlu su anlamını değiştirmez.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"tuzla suyu veya çok yoğun tuzlu su"}],"lexicalization_note":"Tanım yalnız çok tuzlu suyu, özellikle tuzla suyunu belirten kuruluş için geçerlidir; kökün yalın anlamı olarak sunulmaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; acılığı da içeren çok tuzlu su ile genel tuzluluk dalı, özel kuruluşun sınırını en iyi açıklayan karşılaştırmalardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal tuzla bağlantılı çok tuzlu su kuruluşudur; komşu dalda acılık ayrıca kurucu bir niteliktir.","focus_only":"Odak dal belirli bir su kuruluşuna bağlıdır ve tuzla sularını özellikle kapsar.","gloss":"çok tuzlu ve acı tuzlu su","neighbor_only":"Komşu dal yoğun tuzluluğa ek olarak belirgin acılığı da anlamın parçası yapar.","neighbor_ref":"root_000014/B003","relation_type":"near_synonym","shared_zone":"İki dal da içimi güçleştiren yüksek tuzluluktaki suyu kapsar."},{"boundary_match":"field_only","distinction":"Odak dal özel bir su türünü ve kuruluşu adlandırır; komşu dal ise herhangi bir suyun tuzluluk kazanmasını veya tuzlu niteliğini anlatır.","focus_only":"Odak dal belirli bir kuruluşla adlandırılan aşırı tuzlu su nesnesidir.","gloss":"özel çok tuzlu su ve genel tuzluluk","neighbor_only":"Komşu dal suyun tuzlanması ve tuzluluk niteliğini genel olarak kapsar.","neighbor_ref":"root_000086/B004","relation_type":"same_field","shared_zone":"Her iki dal suyun tuzlu olması alanındadır."}],"source_phrase_ar":"مما شذ عن الباب ماء إمدان شديد الملوحة (maqayis)؛ ماء إمدان شديد الملوحة (sihah)؛ الإمدان مياه السباخ والأمدان الماء الملح الشديد الملوحة (tahdhib)","source_summary":"Kaynaklar kuruluşu çok yoğun tuzlu su olarak tanımlar ve tuzla sularını bu ad altında toplar; ayrıca bu kullanımın kökün olağan anlam örgüsünün dışında değerlendirilebildiği belirtilir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه ماء إمدان أو الأمدان: الماء الملح أو الشديد الملوحة، وخاصة مياه السباخ.","what_is_not_ar":"لا يدخل فيه مد النهر أو البحر الجاري؛ هذا اللفظ جعله بعض المصادر شاذا عن الباب."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["104:9:1"],"branch_refs":[],"candidate_id":"cand_1739eed117ecc47734c1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:9:1:dependent-boundary-frame","source_type":"word_analysis","support_ids":["sup_33cd56a9bd270368fe13","sup_c05e20d1598bb8621069"],"title":"the final ayah completes the prior seal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:9:1","qac_refs":["104:9:1:1"],"status":"accepted"}},{"anchor_refs":["104:9:1"],"branch_refs":[],"candidate_id":"cand_2d01d9dba15a644d86fa","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:9:1:locative-instrumental-range","source_type":"word_analysis","support_ids":["sup_2c45f4fc1df3f709f765","sup_c05e20d1598bb8621069"],"title":"containment and means remain live","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:9:1","qac_refs":["104:9:1:1"],"status":"accepted"}},{"anchor_refs":["104:9:2"],"branch_refs":[],"candidate_id":"cand_ec96e7192e435fdbc8f9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001043"],"scope":"focus_ayah","source_local_id":"104:9:2:adjective-bound-columns","source_type":"word_analysis","support_ids":["sup_5ecc200a5259ba81a37e","sup_84c792b2f5ca819b8fef"],"title":"extension belongs to the columns","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:9:2","qac_refs":["104:9:2:1"],"status":"accepted"}},{"anchor_refs":["104:9:2"],"branch_refs":[],"candidate_id":"cand_7b9efce5db788f1e5f45","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001043"],"scope":"focus_ayah","source_local_id":"104:9:2:architectural-pivot","source_type":"word_analysis","support_ids":["sup_5ecc200a5259ba81a37e","sup_87f994a40f0402253dae"],"title":"middle noun gives the scene a frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:9:2","qac_refs":["104:9:2:1"],"status":"accepted"}},{"anchor_refs":["104:9:2"],"branch_refs":[],"candidate_id":"cand_47bc2076cd47df84c599","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001043"],"scope":"focus_ayah","source_local_id":"104:9:2:governed-frame-role","source_type":"word_analysis","support_ids":["sup_5ecc200a5259ba81a37e","sup_f79a0afb72c119b37e0d"],"title":"pillars specify the sealing frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:9:2","qac_refs":["104:9:2:1"],"status":"accepted"}},{"anchor_refs":["104:9:2"],"branch_refs":[],"candidate_id":"cand_cd86ece214e7677ca0e5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001043"],"scope":"focus_ayah","source_local_id":"104:9:2:indefinite-plural-variants","source_type":"word_analysis","support_ids":["sup_5ecc200a5259ba81a37e","sup_f877edafa5b900422a6b"],"title":"unspecified multiple pillars","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:9:2","qac_refs":["104:9:2:1"],"status":"accepted"}},{"anchor_refs":["104:9:2"],"branch_refs":[],"candidate_id":"cand_37e1e67786ae258ae46d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001043"],"scope":"focus_ayah","source_local_id":"104:9:2:local-sound-binding","source_type":"word_analysis","support_ids":["sup_5ecc200a5259ba81a37e","sup_6ddfb486a94bde9b4807"],"title":"sound binds noun to adjective","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:9:2","qac_refs":["104:9:2:1"],"status":"accepted"}},{"anchor_refs":["104:9:2"],"branch_refs":[],"candidate_id":"cand_b5a0608dedc164b333ac","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001043"],"scope":"focus_ayah","source_local_id":"104:9:2:no-pillar-creation-echo","source_type":"word_analysis","support_ids":["sup_5ecc200a5259ba81a37e","sup_72a0363a8c8232b235a0"],"title":"absent cosmic pillars become present confinement","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:9:2","qac_refs":["104:9:2:1"],"status":"accepted"}},{"anchor_refs":["104:9:2"],"branch_refs":[],"candidate_id":"cand_78fc5edb0464583fd3a5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001043"],"scope":"focus_ayah","source_local_id":"104:9:2:secondary-column-images","source_type":"word_analysis","support_ids":["sup_5ecc200a5259ba81a37e","sup_6c3cc9226dbbfe2baa57"],"title":"posts and light-columns add image pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:9:2","qac_refs":["104:9:2:1"],"status":"accepted"}},{"anchor_refs":["104:9:2"],"branch_refs":[],"candidate_id":"cand_59209d9160cb6a710385","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001043"],"scope":"focus_ayah","source_local_id":"104:9:2:support-root-infrastructure","source_type":"word_analysis","support_ids":["sup_0fb20cb6ec616a447d10","sup_5ecc200a5259ba81a37e"],"title":"support becomes punitive infrastructure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:9:2","qac_refs":["104:9:2:1"],"status":"accepted"}},{"anchor_refs":["104:9:3"],"branch_refs":[],"candidate_id":"cand_114a8db20f3182cad9ca","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001407"],"scope":"focus_ayah","source_local_id":"104:9:3:adjective-scope","source_type":"word_analysis","support_ids":["sup_760dc9c48a2dd8a160ae","sup_f3df2e26b6b179e76000"],"title":"extension stays inside the noun phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:9:3","qac_refs":["104:9:3:1"],"status":"accepted"}},{"anchor_refs":["104:9:3"],"branch_refs":[],"candidate_id":"cand_5a83a1635405cd1eba1d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001407"],"scope":"focus_ayah","source_local_id":"104:9:3:closure-extension-paradox","source_type":"word_analysis","support_ids":["sup_efa1a9d66d63463ef71b","sup_f3df2e26b6b179e76000"],"title":"closed yet stretched","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:9:3","qac_refs":["104:9:3:1"],"status":"accepted"}},{"anchor_refs":["104:9:3"],"branch_refs":[],"candidate_id":"cand_ee02ac2d3435f5dbd3c7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001407"],"scope":"focus_ayah","source_local_id":"104:9:3:extension-field-pressure","source_type":"word_analysis","support_ids":["sup_8fba77273b41fc12e44a","sup_f3df2e26b6b179e76000"],"title":"space, duration, and spread thicken extension","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:9:3","qac_refs":["104:9:3:1"],"status":"accepted"}},{"anchor_refs":["104:9:3"],"branch_refs":[],"candidate_id":"cand_412ff8dc279d5a9eec05","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001407"],"scope":"focus_ayah","source_local_id":"104:9:3:extension-reversal-echoes","source_type":"word_analysis","support_ids":["sup_0e1abce418f60807146a","sup_f3df2e26b6b179e76000"],"title":"reward and wealth extensions reverse into punishment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:9:3","qac_refs":["104:9:3:1"],"status":"accepted"}},{"anchor_refs":["104:9:3"],"branch_refs":[],"candidate_id":"cand_a23a4637c949147cd7a4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001407"],"scope":"focus_ayah","source_local_id":"104:9:3:form-ii-intensified-extension","source_type":"word_analysis","support_ids":["sup_6c2ec16227539e24187b","sup_f3df2e26b6b179e76000"],"title":"intensive stretching closes the word","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:9:3","qac_refs":["104:9:3:1"],"status":"accepted"}},{"anchor_refs":["104:9:3"],"branch_refs":[],"candidate_id":"cand_37ce346c081692d8ef60","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001407"],"scope":"focus_ayah","source_local_id":"104:9:3:ink-spread-pressure","source_type":"word_analysis","support_ids":["sup_c48d961d9009ecc63ebf","sup_f3df2e26b6b179e76000"],"title":"ink-like spread remains secondary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:9:3","qac_refs":["104:9:3:1"],"status":"accepted"}},{"anchor_refs":["104:9:3"],"branch_refs":[],"candidate_id":"cand_6990e018e43e599b88b8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001407"],"scope":"focus_ayah","source_local_id":"104:9:3:local-sound-expansion","source_type":"word_analysis","support_ids":["sup_decf4212ee27f62e372b","sup_f3df2e26b6b179e76000"],"title":"the adjective stretches the prior sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:9:3","qac_refs":["104:9:3:1"],"status":"accepted"}},{"anchor_refs":["104:9:3"],"branch_refs":[],"candidate_id":"cand_e3a24a0258c7a1378a3c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001407"],"scope":"focus_ayah","source_local_id":"104:9:3:passive-imposed-state","source_type":"word_analysis","support_ids":["sup_a49279fad0fd4eb02626","sup_f3df2e26b6b179e76000"],"title":"extended by an unstated agent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:9:3","qac_refs":["104:9:3:1"],"status":"accepted"}},{"anchor_refs":["104:9:3"],"branch_refs":[],"candidate_id":"cand_d7c339c8514c860a85f3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001407"],"scope":"focus_ayah","source_local_id":"104:9:3:surah-final-extension","source_type":"word_analysis","support_ids":["sup_02ec63c87ceca9e14824","sup_f3df2e26b6b179e76000"],"title":"the surah lands on extended quality","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:9:3","qac_refs":["104:9:3:1"],"status":"accepted"}},{"anchor_refs":["104:9:2"],"branch_refs":[],"candidate_id":"cand_3e029b01e46493a601f9","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001043"],"scope":"focus_ayah","source_local_id":"104:9:2:1","source_type":"qac_morpheme","support_ids":["sup_2ae2b8311d526b6b0e9c"],"title":"QAC root occurrence: ع م د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["104:9:3"],"branch_refs":[],"candidate_id":"cand_095f53558ed4c1cff194","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001407"],"scope":"focus_ayah","source_local_id":"104:9:3:1","source_type":"qac_morpheme","support_ids":["sup_cbb3c3f3529857ac08af"],"title":"QAC root occurrence: م د د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["104:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:9","branch_refs":["root_001043/B003","root_001407/B001"],"candidate_id":"cand_bc7a63f862b504e6d208","commentary_obligation":"review","hft_ref":"hft_8dc0d41c2940338563c3","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_extended_columnar_enclosure","source_type":"hft","support_ids":["sup_56ddf1c23818bcc9bf75"],"title":"baseline_extended_columnar_enclosure","trust":"legacy_unbound"},{"anchor_refs":["104:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:9","branch_refs":["root_001043/B002","root_001407/B002"],"candidate_id":"cand_3afc84ebba1f0f300469","commentary_obligation":"review","hft_ref":"hft_66407b99031d053dc5b6","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_self_reinforcing_support_system","source_type":"hft","support_ids":["sup_9921d44f046a5d1673aa"],"title":"baseline_self_reinforcing_support_system","trust":"legacy_unbound"},{"anchor_refs":["104:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:9","branch_refs":["root_001043/B001","root_001043/B014","root_001407/B004"],"candidate_id":"cand_190412a5e54578fafdb6","commentary_obligation":"review","hft_ref":"hft_2cff52dbd28573935dfa","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_intentional_prolongation","source_type":"hft","support_ids":["sup_881e018bd0267b81ad45"],"title":"baseline_intentional_prolongation","trust":"legacy_unbound"},{"anchor_refs":["104:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:9","branch_refs":["root_001043/B013","root_001407/B003"],"candidate_id":"cand_8dfdd1ef449081def590","commentary_obligation":"review","hft_ref":"hft_a81784f496bf7f3d9f8b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_banked_continuous_pressure","source_type":"hft","support_ids":["sup_34b036749dd7a638843f"],"title":"baseline_banked_continuous_pressure","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فِى عَمَدٍۢ مُّمَدَّدَةٍۭ","qac_morphemes":[{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"104:9:1:1","qac_word_ref":"104:9:1","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"عَمَد","morph_features":"STEM|POS:N|LEM:Eamad|ROOT:Emd|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:9:2:1","qac_word_ref":"104:9:2","root_ar":"ع م د","surface_ar":"عَمَدٍ"},{"lemma_ar":"مُّمَدَّدَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|(II)|LEM:m~umad~adap|ROOT:mdd|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"104:9:3:1","qac_word_ref":"104:9:3","root_ar":"م د د","surface_ar":"مُّمَدَّدَةٍۭ"}],"word_analysis_qac_refs":[["104:9:1:1"],["104:9:2:1"],["104:9:3:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["104:9:1","104:9:2","104:9:3"]},"focus_surface_evidence":{"arabic_uthmani":"فِى عَمَدٍۢ مُّمَدَّدَةٍۭ","qac_morphemes":[{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"104:9:1:1","qac_word_ref":"104:9:1","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"عَمَد","morph_features":"STEM|POS:N|LEM:Eamad|ROOT:Emd|MP|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:9:2:1","qac_word_ref":"104:9:2","root_ar":"ع م د","surface_ar":"عَمَدٍ"},{"lemma_ar":"مُّمَدَّدَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|(II)|LEM:m~umad~adap|ROOT:mdd|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"104:9:3:1","qac_word_ref":"104:9:3","root_ar":"م د د","surface_ar":"مُّمَدَّدَةٍۭ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["104:9:1:1"],["104:9:2:1"],["104:9:3:1"]],"word_analysis_refs":["104:9:1","104:9:2","104:9:3"],"word_rows":[{"analysis_record_ref":"104:9:1","analytic_gloss_range_en":"a prepositional frame of containment, circumstance, and possible means; locally dependent on the sealed state in 104:8 rather than an independent assertion","analytic_root_gloss_range_en":null,"qac_refs":["104:9:1:1"],"root":{"note":"no root (particle)"},"surface":{"arabic":"فِى","transliteration":"fī"}},{"analysis_record_ref":"104:9:2","analytic_gloss_range_en":"indefinite plural pillars, columns, posts, or supports forming the governed architecture of the sealed state; local grammar allows the columns to be read as place, means, or specifying frame","analytic_root_gloss_range_en":"a root range including pillars and supports, deliberate aiming, reliance, central support, and other branches; the local phrase selects the concrete support or column branch while allowing purposeful support-pressure to remain","qac_refs":["104:9:2:1"],"root":{"arabic":"ع م د","transliteration":"ʿ-m-d"},"surface":{"arabic":"عَمَدٍۢ","transliteration":"ʿamadin"}},{"analysis_record_ref":"104:9:3","analytic_gloss_range_en":"extended, stretched-out, or prolonged as a passive Form II adjectival quality of the pillars; the local sense is spatial extension with duration and imposedness as live pressure","analytic_root_gloss_range_en":"a root range of drawing out, stretching, supplying or reinforcing, swelling spread, time-extension, and related measures or substances; the local form selects intensified passive extension of the columns","qac_refs":["104:9:3:1"],"root":{"arabic":"م د د","transliteration":"m-d-d"},"surface":{"arabic":"مُّمَدَّدَةٍۭ","transliteration":"mumaddadah"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["104:9"],"branch_refs":["root_001043/B003","root_001407/B001"],"candidate_id":"cand_bc7a63f862b504e6d208","evidence_scope":"focus_ayah","hft_ref":"hft_8dc0d41c2940338563c3","item_id":"baseline_extended_columnar_enclosure","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_extended_columnar_enclosure","support_id":"sup_56ddf1c23818bcc9bf75"},{"anchor_refs":["104:9"],"branch_refs":["root_001043/B002","root_001407/B002"],"candidate_id":"cand_3afc84ebba1f0f300469","evidence_scope":"focus_ayah","hft_ref":"hft_66407b99031d053dc5b6","item_id":"baseline_self_reinforcing_support_system","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_self_reinforcing_support_system","support_id":"sup_9921d44f046a5d1673aa"},{"anchor_refs":["104:9"],"branch_refs":["root_001043/B001","root_001043/B014","root_001407/B004"],"candidate_id":"cand_190412a5e54578fafdb6","evidence_scope":"focus_ayah","hft_ref":"hft_2cff52dbd28573935dfa","item_id":"baseline_intentional_prolongation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_intentional_prolongation","support_id":"sup_881e018bd0267b81ad45"},{"anchor_refs":["104:9"],"branch_refs":["root_001043/B013","root_001407/B003"],"candidate_id":"cand_8dfdd1ef449081def590","evidence_scope":"focus_ayah","hft_ref":"hft_a81784f496bf7f3d9f8b","item_id":"baseline_banked_continuous_pressure","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_banked_continuous_pressure","support_id":"sup_34b036749dd7a638843f"}],"diagnostics":[],"lane_counts":{"global":10,"macro":13,"micro":4},"packet_summary":{"ayah_count":9,"focus_ref":"104:9","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"و ص د","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000036","furuq_root_norm":"ء ص د","furuq_source_root_norm":"أ ص د","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001653","furuq_root_norm":"و ص د","furuq_source_root_norm":"و ص د","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:8","104:9"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"104:9","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":17,"unstructured_record_count":0},"identity":{"ayah_ref":"104:9","lane":"micro","linguistic_source_ref":"104:9","surface_ref":"104:9","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"104:9","target_tokens":[["Uzatılmış",["104:9:3"]],["sütunlar",["104:9:2"]],["içinde",["104:9:1"]]],"text":"Uzatılmış sütunlar içinde."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":9,"id":"s104-p01-001-009","label":"Whole surah","number":1,"refs":["104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:8","104:9"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:3:surah-final-extension","source_type":"word_analysis","support_id":"sup_02ec63c87ceca9e14824","text":"{\"blocking_evidence\":null,\"headline\":\"the surah lands on extended quality\",\"reader_payoff\":\"The reader notices that the surah's final acoustic and semantic landing is the extended quality of the architecture, not the pillar noun alone.\",\"reason\":\"The word is the final word of the ayah and surah; the phrase is a verbless prepositional completion of the prior sealed predicate.\",\"representative_source_ids\":[\"QT-1201d4f5\",\"QT-849a0f50\",\"QT-aa2607d0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:3:extension-reversal-echoes","source_type":"word_analysis","support_id":"sup_0e1abce418f60807146a","text":"{\"blocking_evidence\":null,\"headline\":\"reward and wealth extensions reverse into punishment\",\"reader_payoff\":\"The reader notices that extension is morally contextual: shade in 56:30 and wealth in 74:12 become, here, surrounding punishment after wealth-counting in 104:2.\",\"reason\":\"The CRITICAL rows give concrete parallels in 56:30 and 74:12, and the local surah context includes wealth-counting in 104:2; these echoes illuminate contrast without changing the local adjectival parse.\",\"representative_source_ids\":[\"QI-62535019\",\"QE-59cc7665\",\"QE-93fb985e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:2:support-root-infrastructure","source_type":"word_analysis","support_id":"sup_0fb20cb6ec616a447d10","text":"{\"blocking_evidence\":null,\"headline\":\"support becomes punitive infrastructure\",\"reader_payoff\":\"The reader notices that a normally load-bearing support image has been turned into the physical logic of punishment.\",\"reason\":\"V4 supports a pillar or column branch and related support branches for {{ar:ع م د}} ({{tr:ʿ-m-d}}); local grammar selects the concrete pillar/support branch while keeping intention and reliance as pressure rather than separate senses.\",\"representative_source_ids\":[\"QS-0220c052\",\"QS-f3963254\",\"QS-db763b15\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"104:9:2:1","source_type":"qac_morpheme","support_id":"sup_2ae2b8311d526b6b0e9c","text":"{\"lemma_ar\":\"عَمَد\",\"morph_features\":\"STEM|POS:N|LEM:Eamad|ROOT:Emd|MP|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"104:9:2:1\",\"qac_word_ref\":\"104:9:2\",\"root_ar\":\"ع م د\",\"surface_ar\":\"عَمَدٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:1:locative-instrumental-range","source_type":"word_analysis","support_id":"sup_2c45f4fc1df3f709f765","text":"{\"blocking_evidence\":null,\"headline\":\"containment and means remain live\",\"reader_payoff\":\"The reader notices that the particle lets the pillars be both the place of confinement and the means by which confinement is fastened.\",\"reason\":\"QAC and translation-support evidence describe {{ar:فِى}} ({{tr:fī}}) as locative or instrumental and dependent on the sealed state in 104:8, so the broader prepositional range is locally licensed.\",\"representative_source_ids\":[\"QG-0d378941\",\"MG-a07ee0ee\",\"QS-eac781bf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:1:dependent-boundary-frame","source_type":"word_analysis","support_id":"sup_33cd56a9bd270368fe13","text":"{\"blocking_evidence\":null,\"headline\":\"the final ayah completes the prior seal\",\"reader_payoff\":\"The reader notices that 104:9 is syntactically hooked to 104:8, so the final phrase explains the already-declared closure rather than starting a separate scene.\",\"reason\":\"Attachment support warns that a single-ayah rendering may leave the prepositional phrase without its governor; the local phrase has no independent finite predicate and looks back to the sealed predicate in 104:8.\",\"representative_source_ids\":[\"QG-c401dc47\",\"QT-5dc685fe\",\"QB-e1066974\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:2","source_type":"word_analysis","support_id":"sup_5ecc200a5259ba81a37e","text":"{\"gloss_range\":\"indefinite plural pillars, columns, posts, or supports forming the governed architecture of the sealed state; local grammar allows the columns to be read as place, means, or specifying frame\",\"prose\":\"{{ar:عَمَدٍۢ}} ({{tr:ʿamadin}}) is the word that turns the previous sealed state into architecture. Its genitive position under {{ar:فِى}} ({{tr:fī}}) keeps it inside the prepositional frame, so the columns can be heard as prison-space, locking apparatus, or the clarifying measure of the sealed condition. The following adjective makes extension a property of the columns themselves, and its feminine singular agreement treats the many pillars as one enclosing system. The indefinite broken plural leaves the set multiple and unspecified, and the accepted vocalic variants keep that pillar sense while making the mass or compression of the plural audible. The root's support field makes the image load-bearing and purposeful, though local grammar selects concrete pillars or posts rather than the root's unrelated branches; the same column field can press toward restraining stakes or fire-lit shafts without replacing the pillar sense. The no-pillar creation formula in 13:2 and 31:10 is inverted here: what is absent from the raised heavens becomes present as confinement. The word also works as the ayah's pivot, receiving containment from {{ar:فِى}} ({{tr:fī}}), handing its m-d sound into {{ar:مُّمَدَّدَةٍ}} ({{tr:mumaddadah}}), and giving the carried sealed scenario a visible frame.\",\"root_display\":\"{{ar:ع م د}} ({{tr:ʿ-m-d}})\",\"root_gloss_range\":\"a root range including pillars and supports, deliberate aiming, reliance, central support, and other branches; the local phrase selects the concrete support or column branch while allowing purposeful support-pressure to remain\",\"surface_display\":\"{{ar:عَمَدٍۢ}} ({{tr:ʿamadin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:3:form-ii-intensified-extension","source_type":"word_analysis","support_id":"sup_6c2ec16227539e24187b","text":"{\"blocking_evidence\":null,\"headline\":\"intensive stretching closes the word\",\"reader_payoff\":\"The reader notices that the final adjective is not bare length but intensified, pressured stretching carried by the Form II pattern and doubled sound.\",\"reason\":\"QAC identifies the word as a Form II passive participle, and the contextual profile marks the exact form as low-occurrence; the doubled dāl audibly reinforces the intensive form.\",\"representative_source_ids\":[\"QS-fdd26d5b\",\"QH-448ef438\",\"QP-180a88ca\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:2:secondary-column-images","source_type":"word_analysis","support_id":"sup_6c3cc9226dbbfe2baa57","text":"{\"blocking_evidence\":null,\"headline\":\"posts and light-columns add image pressure\",\"reader_payoff\":\"The reader notices that the column word can feel like restraining posts or shafts in a fire-lit enclosure, while still meaning the pillars of the local phrase.\",\"reason\":\"The dictionary field includes concrete pillars, poles, and central supporting parts; the local sealed-fire frame permits image-pressure from stakes or light-shafts, but does not replace the selected pillar sense.\",\"representative_source_ids\":[\"QS-23d3c5fe\",\"QS-a301380c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:2:local-sound-binding","source_type":"word_analysis","support_id":"sup_6ddfb486a94bde9b4807","text":"{\"blocking_evidence\":null,\"headline\":\"sound binds noun to adjective\",\"reader_payoff\":\"The reader notices that the compact sound of the pillar word passes into the following extension word before analysis names the grammar.\",\"reason\":\"The surface sequence places the nasal ending of {{ar:عَمَدٍۢ}} ({{tr:ʿamadin}}) immediately before the mīm of {{ar:مُّمَدَّدَةٍ}} ({{tr:mumaddadah}}), matching the strongly licensed adjective attachment.\",\"representative_source_ids\":[\"QE-b8da9425\",\"QP-1afc1510\",\"QP-897320ce\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:2:no-pillar-creation-echo","source_type":"word_analysis","support_id":"sup_72a0363a8c8232b235a0","text":"{\"blocking_evidence\":null,\"headline\":\"absent cosmic pillars become present confinement\",\"reader_payoff\":\"The reader notices that the creation formula of raised heavens without visible pillars (13:2; 31:10) is answered by visible pillars in the punishment scene.\",\"reason\":\"The contextual supplement names 13:2 and 31:10 as low-occurrence comparanda for the same root-form field, so the inversion can be preserved as an echo without controlling the local parse.\",\"representative_source_ids\":[\"QI-4abfe538\",\"QE-45f79e33\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:3:adjective-scope","source_type":"word_analysis","support_id":"sup_760dc9c48a2dd8a160ae","text":"{\"blocking_evidence\":null,\"headline\":\"extension stays inside the noun phrase\",\"reader_payoff\":\"The reader notices that the final extension belongs to the pillars as one governed phrase, not to a separate event or unattached condition.\",\"reason\":\"Attachment evidence strongly licenses {{ar:مُّمَدَّدَةٍۭ}} ({{tr:mumaddadah}}) as the adjective of {{ar:عَمَدٍ}} ({{tr:ʿamadin}}); it remains inside the scope of {{ar:فِى}} ({{tr:fī}}).\",\"representative_source_ids\":[\"QG-06e47dbb\",\"QG-a55ece9a\",\"QG-bbc041c0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:2:adjective-bound-columns","source_type":"word_analysis","support_id":"sup_84c792b2f5ca819b8fef","text":"{\"blocking_evidence\":null,\"headline\":\"extension belongs to the columns\",\"reader_payoff\":\"The reader notices that extension is built into the pillars themselves, with many columns treated as one collective enclosing architecture.\",\"reason\":\"Attachment evidence strongly licenses {{ar:مُّمَدَّدَةٍ}} ({{tr:mumaddadah}}) as the adjective of {{ar:عَمَدٍۢ}} ({{tr:ʿamadin}}); the feminine singular adjective is expected with a non-rational broken plural.\",\"representative_source_ids\":[\"QG-96ba08c7\",\"QF-a1865f2a\",\"QP-897320ce\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:2:architectural-pivot","source_type":"word_analysis","support_id":"sup_87f994a40f0402253dae","text":"{\"blocking_evidence\":null,\"headline\":\"middle noun gives the scene a frame\",\"reader_payoff\":\"The reader notices that the middle word is the pivot from containment to visible structure and then to extension.\",\"reason\":\"The ayah's three-word sequence places {{ar:عَمَدٍۢ}} ({{tr:ʿamadin}}) between the preposition and its adjective, giving the dependent phrase its concrete architectural center.\",\"representative_source_ids\":[\"QT-3eceb9dd\",\"QT-627b39d1\",\"QB-ed72f87d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:3:extension-field-pressure","source_type":"word_analysis","support_id":"sup_8fba77273b41fc12e44a","text":"{\"blocking_evidence\":null,\"headline\":\"space, duration, and spread thicken extension\",\"reader_payoff\":\"The reader notices that the columns are not merely long; the root field makes their extension feel drawn out, sustained, and spreading.\",\"reason\":\"V4 supports stretching, supply, swelling spread, and extended time branches for {{ar:م د د}} ({{tr:m-d-d}}); local grammar selects the stretched-column sense, so duration, supply, and tide-like spread survive as image-pressure.\",\"representative_source_ids\":[\"QS-1915267a\",\"QS-22e7c0fa\",\"QS-aedbe00d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:3:passive-imposed-state","source_type":"word_analysis","support_id":"sup_a49279fad0fd4eb02626","text":"{\"blocking_evidence\":null,\"headline\":\"extended by an unstated agent\",\"reader_payoff\":\"The reader notices the columns as an imposed state: they do not stretch themselves, but are presented as already extended.\",\"reason\":\"The passive participle implies an extender, but the local surface suppresses the agent; contextual evidence can support divine-agency pressure, while the prose should not make that unstated agent grammatically explicit as the word's direct surface meaning.\",\"representative_source_ids\":[\"QG-bfd7a117\",\"QG-bfd9ab48\",\"MP-762b3240\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:1","source_type":"word_analysis","support_id":"sup_c05e20d1598bb8621069","text":"{\"gloss_range\":\"a prepositional frame of containment, circumstance, and possible means; locally dependent on the sealed state in 104:8 rather than an independent assertion\",\"prose\":\"{{ar:فِى}} ({{tr:fī}}) does not merely begin a fresh clause; it opens the frame that completes the sealed predicate of 104:8. Because the particle can hold location, circumstance, and means, the reader is not forced to choose only between being inside pillars and being sealed by pillars: the phrase makes the extended columns both the enclosing environment and the mechanism of closure. The ayah boundary therefore becomes grammatical suspense; the seal is announced first, and only then does {{ar:فِى}} ({{tr:fī}}) disclose the architecture that makes that seal concrete.\",\"root_display\":\"no root (particle)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فِى}} ({{tr:fī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:3:ink-spread-pressure","source_type":"word_analysis","support_id":"sup_c48d961d9009ecc63ebf","text":"{\"blocking_evidence\":null,\"headline\":\"ink-like spread remains secondary\",\"reader_payoff\":\"The reader notices a record-like undertone of extension after the surah's counting theme, while the local phrase still speaks of stretched pillars.\",\"reason\":\"The dictionary branch for ink is real but not the local selected sense; it may remain as a limited image-pressure because the CRITICAL row ties it to the surah's counting vocabulary.\",\"representative_source_ids\":[\"QS-6fdc1707\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"104:9:3:1","source_type":"qac_morpheme","support_id":"sup_cbb3c3f3529857ac08af","text":"{\"lemma_ar\":\"مُّمَدَّدَة\",\"morph_features\":\"STEM|POS:ADJ|PASS|PCPL|(II)|LEM:m~umad~adap|ROOT:mdd|F|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"104:9:3:1\",\"qac_word_ref\":\"104:9:3\",\"root_ar\":\"م د د\",\"surface_ar\":\"مُّمَدَّدَةٍۭ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:3:local-sound-expansion","source_type":"word_analysis","support_id":"sup_decf4212ee27f62e372b","text":"{\"blocking_evidence\":null,\"headline\":\"the adjective stretches the prior sound\",\"reader_payoff\":\"The reader notices that the m-d sound cluster of the pillar word expands into the heavier, doubled sound of the final adjective.\",\"reason\":\"The sequence places {{ar:عَمَدٍ}} ({{tr:ʿamadin}}) beside {{ar:مُّمَدَّدَةٍۭ}} ({{tr:mumaddadah}}), so the acoustic expansion tracks the grammatical head-adjective relation.\",\"representative_source_ids\":[\"QE-fb65182f\",\"QF-b5fe07f3\",\"QP-ac026c2d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:3:closure-extension-paradox","source_type":"word_analysis","support_id":"sup_efa1a9d66d63463ef71b","text":"{\"blocking_evidence\":null,\"headline\":\"closed yet stretched\",\"reader_payoff\":\"The reader notices the paradox that the punishment is sealed shut in 104:8 and then described through extension in 104:9.\",\"reason\":\"The CRITICAL rows tie the passive-participial rhyme and semantic contrast between the sealed predicate in 104:8 and {{ar:مُّمَدَّدَةٍۭ}} ({{tr:mumaddadah}}) in 104:9.\",\"representative_source_ids\":[\"QE-1dbebdad\",\"QB-d2040455\",\"QY-0df0bee1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:3","source_type":"word_analysis","support_id":"sup_f3df2e26b6b179e76000","text":"{\"gloss_range\":\"extended, stretched-out, or prolonged as a passive Form II adjectival quality of the pillars; the local sense is spatial extension with duration and imposedness as live pressure\",\"prose\":\"{{ar:مُّمَدَّدَةٍۭ}} ({{tr:mumaddadah}}) locks the final image onto the pillars: it is their adjective, not a floating state elsewhere. As a passive Form II participle, it presents the columns as already and intensively stretched, with the extender left implicit in the punishment frame. The root's physical stretching branch gives the word tactile force; duration, swelling spread, supply, and even ink-like record-spread after the surah's counting theme remain secondary pressure only insofar as they thicken the idea of extension. The last word of the surah therefore lands not simply on pillars, but on their stretched quality. It rhymes and argues with the sealed predicate in 104:8: closure and extension meet, so confinement is shut and yet vast. The wider passive-participle field also sharpens the reversal: extended shade is comfort in 56:30, extended wealth appears in 74:12 after this surah has condemned wealth-counting in 104:2, but here what was extended as comfort or possession becomes extended around as punishment. In sound, the m-d cluster of {{ar:عَمَدٍ}} ({{tr:ʿamadin}}) expands into the repeated mīm and doubled dāl of {{ar:مُّمَدَّدَةٍۭ}} ({{tr:mumaddadah}}), so extension feels dense and controlled rather than airy.\",\"root_display\":\"{{ar:م د د}} ({{tr:m-d-d}})\",\"root_gloss_range\":\"a root range of drawing out, stretching, supplying or reinforcing, swelling spread, time-extension, and related measures or substances; the local form selects intensified passive extension of the columns\",\"surface_display\":\"{{ar:مُّمَدَّدَةٍۭ}} ({{tr:mumaddadah}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:2:governed-frame-role","source_type":"word_analysis","support_id":"sup_f79a0afb72c119b37e0d","text":"{\"blocking_evidence\":null,\"headline\":\"pillars specify the sealing frame\",\"reader_payoff\":\"The reader notices that the pillars are not an independent subject but the governed frame that locates, instruments, or specifies the sealed condition.\",\"reason\":\"The noun is genitive because it is governed by {{ar:فِى}} ({{tr:fī}}); a tamyīz-like or instrumental explanation is useful only as specification of the sealed frame, not as a separate syntactic replacement for the prepositional complement.\",\"representative_source_ids\":[\"QG-b9516c8d\",\"QG-f9fd9423\",\"QS-ae30d0d0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:9:2:indefinite-plural-variants","source_type":"word_analysis","support_id":"sup_f877edafa5b900422a6b","text":"{\"blocking_evidence\":null,\"headline\":\"unspecified multiple pillars\",\"reader_payoff\":\"The reader notices a plural architecture whose number and identity are left open, while the variant forms make mass and compression part of the recitational pressure.\",\"reason\":\"The aligned word is an indefinite broken plural; the cited accepted variants preserve the same pillar referent and syntax while changing the vocalic weight.\",\"representative_source_ids\":[\"QG-fb624414\",\"QF-31b1a84b\",\"QF-922b0f78\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فِى عَمَدٍۢ مُّمَدَّدَةٍۭ","ayah_ref":"104:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001043/B003","root_001407/B001"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001043","role":"The concrete pillar branch supplies the rigid members from which the focus phrase builds an enclosing array.","root":"ع م د","source_ref":"104:9","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001407","role":"The lengthwise drawing-out branch turns the rigid members into continuous spans rather than isolated posts.","root":"م د د","source_ref":"104:9","source_word_indices":["3"]}],"changed_reading":{"after":"The phrase locates someone inside a lengthwise columnar grid whose span itself produces enclosure.","before":"The phrase merely locates someone among unspecified columns."},"confidence":"strong","focus_anchor":"The locative في places the occupant within عمد, and ممددة qualifies those supports as drawn out or extended.","mechanism":"Concrete pillars extended lengthwise cease to be isolated uprights and become a spanning array. The locative makes that array inhabitable as a gridded or barred enclosure.","model_id":"baseline_extended_columnar_enclosure"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_extended_columnar_enclosure","source_type":"hft","support_id":"sup_56ddf1c23818bcc9bf75","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِى عَمَدٍۢ مُّمَدَّدَةٍۭ","ayah_ref":"104:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001043/B002","root_001407/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001043","role":"The propping branch supplies members whose function is to hold a structure up.","root":"ع م د","source_ref":"104:9","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001407","role":"The connected-supply branch makes extension function as continuing reinforcement passed into the support system.","root":"م د د","source_ref":"104:9","source_word_indices":["3"]}],"changed_reading":{"after":"The columns are a linked support system continuously reinforced so that the enclosure does not fail.","before":"The columns are static pieces of architecture."},"confidence":"medium","focus_anchor":"عمد can name what props a structure up, while ممددة can activate a connected increment that keeps supplying another element.","mechanism":"The supports are not only long; they form a maintained system in which one member or added supply reinforces the next. The punishment-space can therefore be read as structurally self-sustaining.","model_id":"baseline_self_reinforcing_support_system"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_self_reinforcing_support_system","source_type":"hft","support_id":"sup_9921d44f046a5d1673aa","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِى عَمَدٍۢ مُّمَدَّدَةٍۭ","ayah_ref":"104:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001043/B001","root_001043/B014","root_001407/B004"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001043","role":"The deliberate-aiming branch supplies purposiveness, making the extension imposed rather than accidental.","root":"ع م د","source_ref":"104:9","source_word_indices":["2"]},{"branch_id":"B014","mapped_root_id":"root_001043","role":"The sticking-and-remaining branch supplies the occupant's inability to detach from the imposed condition.","root":"ع م د","source_ref":"104:9","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_001407","role":"The prolonged-term branch converts physical length into punitive duration.","root":"م د د","source_ref":"104:9","source_word_indices":["3"]}],"changed_reading":{"after":"The phrase also suggests deliberate adhesion to a punishment whose duration is made long.","before":"ممددة describes only the physical length of columns."},"confidence":"exploratory","focus_anchor":"The two focus roots also carry deliberate aiming, sticking fast, and an extended term; the locative can contain a state as well as a place.","mechanism":"A spatial phrase opens onto an affective-temporal reading: the occupant is deliberately held to a condition whose term is drawn out. This does not erase the columns reading; it coexists as a branch-led pressure beneath it.","model_id":"baseline_intentional_prolongation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_intentional_prolongation","source_type":"hft","support_id":"sup_881e018bd0267b81ad45","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِى عَمَدٍۢ مُّمَدَّدَةٍۭ","ayah_ref":"104:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001043/B013","root_001407/B003"],"payload":{"activation_trace":[{"branch_id":"B013","mapped_root_id":"root_001043","role":"The stream-blocking branch supplies a barrier that converts flow into accumulated pressure.","root":"ع م د","source_ref":"104:9","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_001407","role":"The water-fed-by-water branch supplies the continuing inflow that keeps pressure rising behind the barrier.","root":"م د د","source_ref":"104:9","source_word_indices":["3"]}],"changed_reading":{"after":"The roots also sketch an extended dam-like system whose force comes from continuously banked flow.","before":"The referents are dry, rigid columns."},"confidence":"exploratory","focus_anchor":"A remote branch of عمد blocks a stream, while a branch of مدد depicts water swelling because further water feeds it.","mechanism":"The two focus roots can form a hydraulic mechanism: an extended barrier arrests a continuously supplied flow, so being في it means being caught in the pressure pocket made by obstruction plus replenishment.","model_id":"baseline_banked_continuous_pressure"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_banked_continuous_pressure","source_type":"hft","support_id":"sup_34b036749dd7a638843f","trust":"legacy_unbound"}]}
</lane_packet_json>
