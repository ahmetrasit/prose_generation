# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **100:8**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s100-regular-20260911/s100/100_8/micro.discovery.json` and modify nothing
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
  "ayah_ref": "100:8",
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
{"analysis_context":{"analysis_id":"s100-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"100:8","host_surah":100,"lane_context_refs":[],"ordered_context_refs":["100:0","100:1","100:2","100:3","100:4","100:5","100:6","100:7","100:9","100:10","100:11","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Temel anlam yenebilir ya da ekilebilir tane ve tohumdur; parça, dolu ve küpe kullanımları benzer biçime dayalı uzantılardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000286/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:2:2","qac_word_ref":"100:8:2","surface_ar":"حُبِّ"}],"gloss":"tane, tohum ve taneye benzeyen tek parça","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tahıl, baklagil ve kokulu bitkilerde yenebilen veya ekilebilen tane ya da tohum."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir tane veya bir şeyin taneye benzeyen tek parçası."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Biçim benzerliğiyle dolu tanesine ve tek taneli küpeye verilen ad."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bitkisel çekirdeği ve kaynak ifadesindeki biçimsel uzantıları birlikte temsil eden üst düzey karşılıktır.","boundary_detail":"Temel anlam yenebilir ya da ekilebilir tane ve tohumdur; parça, dolu ve küpe kullanımları benzer biçime dayalı uzantılardır.","branch_image_ar":"الحبة التي تنبت وتحمل الحب","concept_gloss":"tane, tohum ve taneye benzeyen tek parça","contextual_glosses":[{"applicability":"Bu karşılık buğday, arpa ve benzeri yenebilir ürünlerden söz edilen bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Diğer bitki tohumlarını, genel tek parçayı, doluyu ve küpe uzantısını dışarıda bırakır.","preserves":"Yenebilir tahıl tanesi anlamını açık biçimde korur."},"facet_ids":["F001"],"text":"tahıl tanesi","usage_role":"contextual"}],"definition":"Tahılın, baklagilin veya kokulu bitkinin ekilebilen ya da yenebilen tanesi ve bunun tek birimidir. Taneye benzetilen parça, dolu tanesi ve tek taneli küpe bu çekirdeğe bağlı uzantılardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tahıl, baklagil ve kokulu bitkilerde yenebilen veya ekilebilen tane ya da tohum."},{"facet_id":"F002","role":"specialization","statement":"Bir tane veya bir şeyin taneye benzeyen tek parçası."},{"facet_id":"F003","role":"extension","statement":"Biçim benzerliğiyle dolu tanesine ve tek taneli küpeye verilen ad."}],"identity_rationale":"Kaynak ifadesi tahıl ve bitki tanelerini temel alırken tek taneyi, taneye benzeyen parçayı, dolu tanesini ve tek taneli küpeyi de aynı kayıtta toplar. Dal korunabilir, ancak benzetmeye dayalı kullanımlar temel bitkisel anlamla özdeşleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tahıl tanesi ve yenebilir bitki tohumu"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"tek tane, tohum veya taneye benzeyen parça"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"dolu tanesi"}],"lexicalization_note":"Dal yalın tane biçimleriyle birlikte doluya özgü bir söz öbeği içerir; söz öbeğinin anlamı genel tane anlamına yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; belirli bir bitki tanesiyle genel tane arasındaki sınırı en iyi gösteren karşılaştırma yayımlandı, yalnızca konu veya kök biçimi paylaşan adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal biçim ve birim bakımından genel bir tane kavramıdır; komşu ise belirli bir bitki türüne ve onun tanesine bağlıdır, bu yüzden olağan kullanımda birbirlerinin yerine geçmezler.","focus_only":"Odak dal bütün tahıl ve bitki tanelerini, ayrıca taneye benzeyen parçaları kapsar.","gloss":"genel tane ile hardal tanesi","neighbor_only":"Komşu dal özellikle hardal bitkisini ve onun tek tanesini adlandırır.","neighbor_ref":"root_000401/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da ekilebilir küçük bir bitki tanesini kapsar."}],"source_phrase_ar":"الحبة واحد الحب (jamhara;sihah)؛ الحب والحبة في الحنطة والشعير وبزور الرياحين (maqayis;tahdhib;mufradat)؛ الحبة من الشيء القطعة منه وحب الغمام وحب المزن وحب قر والحب القرط من حبة واحدة (sihah;tahdhib)","source_summary":"Ortak kayıt, bitkisel taneyi ve tek taneyi merkez alır; parça, dolu ve tek taneli küpe kullanımlarını biçim benzerliğine bağlı olarak ekler.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحب والحبة للحنطة والشعير والبقول والرياحين، والحبة الواحدة، وما شبه بها كالقطعة والبرد والقرط من حبة.","what_is_not_ar":"ليس المحبة ولا حبذا ولا حباب الماء ولا حبة القلب إذا أريد سويداء القلب."},"support_links":[]},{"boundary":"Dal sevgi duygusunu, sevme eylemini ve bir şeyi başkasına yeğlemeyi kapsar; tahıl tanesi veya övgü kalıbı anlamlarını kapsamaz.","branch_kind":"bare","branch_ref":"root_000286/B002","candidate_links":[{"candidate_id":"cand_f5c5c8be459cd50c8e1f","lane":"micro"},{"candidate_id":"cand_53710b73a4633474b3a4","lane":"micro"},{"candidate_id":"cand_69eb74cb192c7f238c85","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:2:2","qac_word_ref":"100:8:2","surface_ar":"حُبِّ"}],"gloss":"sevgi ve yeğleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiye veya şeye yönelen sevgi ve olumlu bağlılık; nefretin karşıtı."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İyi olduğu görülen veya sanılan şeyi güçlü biçimde isteme."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sevilen veya istenen bir şeyi başka bir seçeneğe üstün tutma."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Duygusal bağlılık çekirdeği ile seçimde üstün tutma uzantısını birlikte karşılayan kısa ifadedir.","boundary_detail":"Dal sevgi duygusunu, sevme eylemini ve bir şeyi başkasına yeğlemeyi kapsar; tahıl tanesi veya övgü kalıbı anlamlarını kapsamaz.","branch_image_ar":"المحبة الملازمة للقلب","concept_gloss":"sevgi ve yeğleme","contextual_glosses":[{"applicability":"Bir kişiye veya şeye duyulan olumlu bağlılığın öne çıktığı genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir şeyi başka bir şeye bilinçli olarak yeğleme uzantısını açıkça vermez.","preserves":"Duygusal bağlılık ve nefretin karşıtı olma çekirdeğini korur."},"facet_ids":["F001","F002"],"text":"sevgi","usage_role":"general"}],"definition":"Bir kişiyi veya iyi görülen bir şeyi gönülden isteme ve ona olumlu bağlanma duygusudur; nefretin karşıtıdır. Bu yönelim, bir şeyi başka bir şeye yeğleme biçiminde seçime de dönüşebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiye veya şeye yönelen sevgi ve olumlu bağlılık; nefretin karşıtı."},{"facet_id":"F002","role":"specialization","statement":"İyi olduğu görülen veya sanılan şeyi güçlü biçimde isteme."},{"facet_id":"F003","role":"extension","statement":"Sevilen veya istenen bir şeyi başka bir seçeneğe üstün tutma."}],"identity_rationale":"Kaynak ifadesi sevgiyi nefretin karşıtı olarak verir, onu iyi görülen şeye yönelen güçlü istekle açıklar ve yeğleme kullanımını ayrıca belirtir. Sağlanan dal çerçevesi bu duygusal ve seçimsel alanı doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sevgi; nefretin karşıtı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"iyi görülen şeye yönelen güçlü sevgi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"sevmek veya sevdirmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yeğlemek veya sevmeye yönelmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"birbirini sevmek"}],"lexicalization_note":"Dal yalın kök anlamını verir; taneye, övgü kalıbına veya başka özel söz öbeklerine ait anlamlar tanıma taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sevgi çekirdeğine en yakın komşu yayımlandı. Arzu, düşmanlık, kur yapma ve aynı kökün diğer anlamları ikame sağlamadığı için alınmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Duygusal çekirdekte büyük ölçüde örtüşürler; odak dal seçimsel yeğlemeye uzanırken komşu dal karşılıklı yakınlık ve ilişki boyutunu daha geniş tuttuğu için sınırları tam değildir.","focus_only":"Odak dal iyi görülene yönelen isteği ve bir seçeneği ötekine yeğlemeyi açıkça kapsar.","gloss":"sevgi ile gönül yakınlığı","neighbor_only":"Komşu dal karşılıklı yakınlık, sevgi gösterisi ve sevginin doğmasına yol açan ilişkileri daha belirgin kapsar.","neighbor_ref":"root_001634/B001","relation_type":"near_synonym","shared_zone":"İki dalın ortak alanı kişiye veya şeye duyulan olumlu bağlılık ve sevgidir."}],"source_phrase_ar":"الحب والمحبة اشتقاقه من أحبه إذا لزمه (maqayis)؛ أحببته نقيض أبغضته (ayn)؛ المحبة إرادة ما تراه أو تظنه خيرا (mufradat)؛ استحبوا أي آثروه عليه (mufradat)","source_summary":"Ortak kayıt sevgiyi nefretin karşıtı ve iyi görülene yönelen güçlü istek olarak kurar; aynı yönelimin seçimde yeğleme anlamı kazandığını da belirtir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الحب والمحبة ونقيض البغض، والتحبيب، والمحبوب، والاستحباب بمعنى الإيثار، والمودة المتبادلة.","what_is_not_ar":"ليس الحب بمعنى الحبوب، ولا حبذا وصيغ المدح، ولا لزوم البعير مكانه إلا من جهة الأصل اللغوي."},"support_links":["sup_1e619313e930c2a0d7fe","sup_8db776420fd3a411d98e","sup_9b9822cca3123cbbe210"]},{"boundary":"Bu dal genel sevgi duygusunu değil, övgü, en güçlü istek veya nazik kabul bildiren belirli kalıpları kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000286/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:2:2","qac_word_ref":"100:8:2","surface_ar":"حُبِّ"}],"gloss":"övgü, güçlü istek ve kabul bildiren kalıplar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli söz kalıplarıyla övgü, güçlü istek veya hoşnut kabul bildirme."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi veya şeyi öven ve iyi bulduğunu bildiren kalıp."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir işi yapmayı isteğin son noktası olarak sunan ya da öneriyi memnuniyetle kabul eden kalıp."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Birbirinden farklı üç kalıplaşmış söylem işlevini genel sevgiyle karıştırmadan birlikte temsil eder.","boundary_detail":"Bu dal genel sevgi duygusunu değil, övgü, en güçlü istek veya nazik kabul bildiren belirli kalıpları kapsar.","branch_image_ar":"صيغة المدح وغاية الرغبة","concept_gloss":"övgü, güçlü istek ve kabul bildiren kalıplar","contextual_glosses":[{"applicability":"Bir kişi veya şey hakkında doğrudan övgü ve beğeni bildirilen kalıp bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"En güçlü istek bildirimini ve memnuniyetle kabul cevabını dışarıda bırakır.","preserves":"Övgü ve beğeni bildiren kalıplaşmış işlevi korur."},"facet_ids":["F001","F002"],"text":"ne güzel","usage_role":"contextual"}],"definition":"Belirli kalıplarla bir kişiyi ya da şeyi övme, bir eylemi en güçlü istek olarak sunma veya öneriyi hoşnutlukla kabul etme işlevidir. Bu işlevler genel sevgi anlamı değil, kalıba bağlı söylem kullanımlarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli söz kalıplarıyla övgü, güçlü istek veya hoşnut kabul bildirme."},{"facet_id":"F002","role":"specialization","statement":"Bir kişi veya şeyi öven ve iyi bulduğunu bildiren kalıp."},{"facet_id":"F003","role":"specialization","statement":"Bir işi yapmayı isteğin son noktası olarak sunan ya da öneriyi memnuniyetle kabul eden kalıp."}],"identity_rationale":"Kaynak ifadesi tek bir yalın anlam değil, övgü bildiren kalıbı, bir işi yapmaya yönelik en güçlü isteği ve hoş bir kabul cevabını birlikte verir. Dal ancak bu üç kullanımın ayrı kalıplar olduğu açıkça belirtilirse korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ne güzel; ne iyi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"en büyük isteğin bunu yapmaktır"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"peki, memnuniyetle ve baş üstüne"}],"lexicalization_note":"Dal iki söz öbeği ile bir kalıplaşmış cevap birimini içerir; bunların işlevleri yalın kökün genel anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; övgü işlevini doğrudan karşılaştıran aday yayımlandı. Genel övme eylemleri, cevap kalıpları ve aynı kökün ilgisiz anlamları ikincil kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Övgü işlevinde yaklaşırlar, fakat odak dal belirli bir yapıyla sınırlıdır ve ayrıca istek ile kabul kalıplarını içerir; komşu dalın övgü yapısı bu ek işlevleri taşımaz.","focus_only":"Odak dal övgünün yanında güçlü istek ve nazik kabul bildiren başka kalıpları da kapsar.","gloss":"kalıpla övgü bildirme","neighbor_only":"Komşu dal, karşıt bir yergi kalıbıyla eşleşen genel övgü ve beğeni yapısını kapsar.","neighbor_ref":"root_001525/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir kişi veya şeyi kalıplaşmış sözle iyi ve övgüye değer gösterir."}],"source_phrase_ar":"حبذا حرفان حب وذا تقول حبذا زيد (ayn;sihah;tahdhib)؛ حبابك أن تفعل ذاك معناه غاية محبتك (ayn;sihah;tahdhib;mufradat)؛ الحبة بالضم الحب يقال نعم وحبة وكرامة (sihah)","source_summary":"Ortak kayıt, övgü kalıbını, bir eyleme yönelik en yüksek istek bildirimini ve olumlu kabul cevabını aynı kalıplaşmış kullanım alanında toplar.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه حبذا، وحبابك أن تفعل، ونعم وحبة وكرامة، وما جاء بصيغة مدح أو بلوغ الغاية في المحبة.","what_is_not_ar":"ليس مطلق المحبة ولا الحبوب ولا لزوم البعير."},"support_links":[]},{"boundary":"Anlam yalnızca kalbin içindeki kara nokta veya öz için kullanılan söz öbeğine bağlıdır; genel sevgi ya da bitkisel tane anlamı değildir.","branch_kind":"collocation","branch_ref":"root_000286/B004","candidate_links":[{"candidate_id":"cand_eb5f6311162b51421299","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:2:2","qac_word_ref":"100:8:2","surface_ar":"حُبِّ"}],"gloss":"kalbin içindeki kara öz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kalbin içindeki kara nokta veya kara doku."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kalbin özü ya da meyvesi olarak açıklanan iç bölüm."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İç bölümün biçim bakımından taneye benzetilmesi."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalbin kara iç dokusu ile öz veya meyve açıklamasını birlikte taşıyan söz öbeği karşılığıdır.","boundary_detail":"Anlam yalnızca kalbin içindeki kara nokta veya öz için kullanılan söz öbeğine bağlıdır; genel sevgi ya da bitkisel tane anlamı değildir.","branch_image_ar":"حبة القلب سويداؤه","concept_gloss":"kalbin içindeki kara öz","contextual_glosses":[{"applicability":"İçteki kara doku fiziksel bir bölüm olarak açıklanırken kullanılabilecek açık karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kalbin özü veya meyvesi biçimindeki açıklayıcı değişkeleri geri plana iter.","preserves":"Kalbin içindeki kara bölümün fiziksel görünümünü korur."},"facet_ids":["F001","F003"],"text":"kalbin kara noktası","usage_role":"explanatory"}],"definition":"Kalbin içindeki kara nokta, kara doku veya kalbin özü sayılan bölümdür. Tane adı bu bölüme biçim benzerliğiyle verilmiştir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kalbin içindeki kara nokta veya kara doku."},{"facet_id":"F002","role":"source_variant","statement":"Kalbin özü ya da meyvesi olarak açıklanan iç bölüm."},{"facet_id":"F003","role":"extension","statement":"İç bölümün biçim bakımından taneye benzetilmesi."}],"identity_rationale":"Kaynak ifadesi kalbin içindeki kara bölümü, çekirdeği ya da meyvesi olarak adlandırılan kısmı ve bunun taneye biçimce benzetilmesini açıkça verir. Sağlanan dal çerçevesi bu anatomik ve benzetmeli sınırı doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kalbin kara iç noktası veya özü"}],"lexicalization_note":"Tanım yalnızca kalbin iç bölümünü adlandıran söz öbeğine bağlıdır ve yalın tane ya da sevgi anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kalbin kara iç bölümünü doğrudan paylaşan aday yayımlandı. Ağız, boyun, diş ve yalnızca genel içlik bildiren adaylar daha uzaktı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Kalp bağlamında büyük ölçüde örtüşürler; komşu dal ayrıca çörek otu tanesini kapsadığı, odak dal ise iç dokunun öz ve meyve açıklamalarını belirginleştirdiği için sınır kısmen eşleşir.","focus_only":"Odak dal kalbin içindeki kara dokuyu ayrıca kalbin özü veya meyvesi olarak açıklar.","gloss":"kalbin kara iç bölümü","neighbor_only":"Komşu dal aynı kalp bölgesinin yanında çörek otu tanesini de aynı adlandırma alanına alır.","neighbor_ref":"root_000757/B009","relation_type":"near_synonym","shared_zone":"Her iki dal kalbin kara iç noktasını ve öz sayılan bölümünü adlandırır."}],"source_phrase_ar":"حبة القلب سويداؤه ويقال ثمرته (maqayis;sihah)؛ حبة القلب هي العلقة السوداء التي تكون داخل القلب (tahdhib)؛ حبة القلب تشبيها بالحبة في الهيئة (mufradat)","source_summary":"Ortak kayıt kalbin kara iç bölümünü temel alır; bu bölümün kalbin özü veya meyvesi diye açıklanmasını ve taneye biçimce benzetilmesini birleştirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه حبة القلب بمعنى سويدائه أو ثمرته أو العلقة السوداء داخله، وما صيغ كإصابة حبة القلب.","what_is_not_ar":"ليس مطلق المحبة إلا إذا صرحت العبارة بحبة القلب، وليس الحبة النباتية."},"support_links":["sup_de16f7c0c8d9cb80ad47"]},{"boundary":"Bu anlam devenin güçsüzlük veya direnme nedeniyle bulunduğu yerde kalmasına özgüdür; sevgi veya suyla dolma anlamı değildir.","branch_kind":"bare","branch_ref":"root_000286/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:2:2","qac_word_ref":"100:8:2","surface_ar":"حُبِّ"}],"gloss":"devenin güçsüzlükten yerinden ayrılamaması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Devenin durup veya çöküp bulunduğu yerde kalması."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hareketsizliğin bitkinlik, hastalık, kırık veya direnmeden doğması."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Katılımcıyı, nedeni ve yerinde kalma sonucunu birlikte veren tam açıklayıcı karşılıktır.","boundary_detail":"Bu anlam devenin güçsüzlük veya direnme nedeniyle bulunduğu yerde kalmasına özgüdür; sevgi veya suyla dolma anlamı değildir.","branch_image_ar":"البعير يلزم مكانه من عجز","concept_gloss":"devenin güçsüzlükten yerinden ayrılamaması","contextual_glosses":[{"applicability":"Nedenin hastalık olduğu ve devenin çöktüğü anlatı bağlamında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bitkinlik, kırık veya direnme gibi öteki nedenleri dışarıda bırakır.","preserves":"Hastalık yüzünden devenin çöküp yerinde kalmasını korur."},"facet_ids":["F001","F002"],"text":"hastalıktan çöküp kalan deve","usage_role":"contextual"}],"definition":"Bir devenin bitkinlik, hastalık, kırık veya direnme nedeniyle durması, çökmesi ve bulunduğu yerden ayrılamamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Devenin durup veya çöküp bulunduğu yerde kalması."},{"facet_id":"F002","role":"specialization","statement":"Hareketsizliğin bitkinlik, hastalık, kırık veya direnmeden doğması."}],"identity_rationale":"Kaynak ifadesi devenin yorgunluk, hastalık, kırık veya direnme yüzünden durup yerinden ayrılamamasını tutarlı biçimde anlatır. Dal çerçevesi hem katılımcıyı hem nedeni hem de kalıcı durma sonucunu doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"devenin güçsüzlükten durup yerinden ayrılamaması"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"devenin hastalık veya güçsüzlükten çökmesi"}],"lexicalization_note":"Dal devenin durup yerinde kalmasıyla ilgili yalın eylem alanıdır; komşu söz öbeklerinin anlamları tanıma eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; güçsüzlük ile yerinde kalma bağını en iyi paylaşan aday yayımlandı. Yalnızca hayvan türü, gecikme veya genel yatma bildirenler elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal devenin gerçek durma ve yerinden ayrılamama olayını bildirir; komşu dal ise aşırı zayıflığı, hareketsizliğe benzer görünümüyle niteler ve insanı da kapsar.","focus_only":"Odak dal özellikle devenin hastalık, kırık, bitkinlik veya direnme yüzünden yerinden ayrılamamasını anlatır.","gloss":"güçsüzlükten hareketsiz kalma","neighbor_only":"Komşu dal insanı veya deveyi aşırı zayıflayıp sanki sabit kalmış görünmesi bakımından niteler.","neighbor_ref":"root_000607/B005","relation_type":"near_neighbor","shared_zone":"İki dalda da bedensel güç kaybı hareket edememe veya yerinde kalma sonucuna yaklaşır."}],"source_phrase_ar":"المحب البعير الذي يحسر فيلزم مكانه (maqayis)؛ بعير محب وقد أحب إحبابا وهو أن يصيبه مرض أو كسر فلا يبرح من مكانه (sihah;tahdhib)؛ أحب البعير إذا حرن ولزم مكانه (mufradat)","source_summary":"Ortak kayıt devenin durup yerini terk edememesini temel alır ve bu durumu bitkinlik, hastalık, kırık ya da direnmeye bağlar.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه أحب البعير، والبعير المحب، والإحباب في الإبل إذا وقف أو برك أو لزم مكانه من حسر أو مرض أو كسر.","what_is_not_ar":"ليس المحبة القلبية، ولا الامتلاء من الماء، ولا صغر الجسم."},"support_links":[]},{"boundary":"Hayvanın suyla doyması ve kabın doldurulması aynı doluluk alanındadır; hasta devenin çökmesi veya büyük küp anlamı bu dala girmez.","branch_kind":"bare","branch_ref":"root_000286/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:2:2","qac_word_ref":"100:8:2","surface_ar":"حُبِّ"}],"gloss":"suyla dolmak veya doldurup dolulaştırmak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eşek veya devenin su içerek dolması ya da suya kanmanın ilk aşamasına ulaşması."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tulum veya benzeri bir kabı doldurup dolu hale getirme."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanın su içerek dolmasıyla kabın ettirgen biçimde doldurulmasını katılımcı farkını koruyarak birleştirir.","boundary_detail":"Hayvanın suyla doyması ve kabın doldurulması aynı doluluk alanındadır; hasta devenin çökmesi veya büyük küp anlamı bu dala girmez.","branch_image_ar":"الري حتى الامتلاء","concept_gloss":"suyla dolmak veya doldurup dolulaştırmak","contextual_glosses":[{"applicability":"Eşek veya develerin yeterince su içtiği hayvan bağlamında kullanılabilecek doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir tulumun veya başka kabın dışarıdan doldurulması kullanımını dışarıda bırakır.","preserves":"Hayvanın su içerek dolması ve doygunluğa yaklaşması anlamını korur."},"facet_ids":["F001"],"text":"suya kanmak","usage_role":"contextual"}],"definition":"Bir hayvanın su içerek dolması veya suya kanma aşamasına ulaşmasıdır. Ettirgen kullanımda tulum gibi bir kabı doldurup dolu hale getirmeyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eşek veya devenin su içerek dolması ya da suya kanmanın ilk aşamasına ulaşması."},{"facet_id":"F002","role":"extension","statement":"Tulum veya benzeri bir kabı doldurup dolu hale getirme."}],"identity_rationale":"Kaynak ifadesi hayvanın su içerek dolmasını veya suya kanmanın ilk aşamasını, ayrıca tulum gibi bir kabı doldurup dolu hale getirmeyi birlikte verir. Dal korunabilir, ancak içenin doyması ile bir kabın doldurulması ayrı katılımcı yapıları olarak gösterilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"su içip dolmak veya suya kanmak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"doldurup dolu hale getirmek"}],"lexicalization_note":"Dal su içerek dolma ve bir şeyi doldurma eylemlerinin yalın alanıdır; kap adı veya hayvanın güçsüzlükten çökmesi tanıma katılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ortak doldurma işlemini katılımcı farkıyla gösteren aday yayımlandı. Genel susuzluk, içme veya aynı kökün ilgisiz dalları daha zayıf kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal canlı bir içenin suya kanmasını ve taşınabilir kabı da kapsarken komşu dal sabit bir yalak ya da havuzun doldurulmasına bağlıdır; katılımcı sınırları farklıdır.","focus_only":"Odak dal su içen hayvanın doymasını ve tulum gibi bir kabın doldurulmasını kapsar.","gloss":"suyla doldurma","neighbor_only":"Komşu dal özellikle bir yalak veya havuzun doldurulmasını ve dolu durumunu anlatır.","neighbor_ref":"root_000642/B008","relation_type":"near_neighbor","shared_zone":"İki dal da bir alıcıyı suyla doldurma ve doluluk sonucuna ulaştırma alanındadır."}],"source_phrase_ar":"تحبب الحمار إذا امتلأ من الماء وشربت الإبل حتى حببت (sihah)؛ أول الري التحبب وحببته فتحبب إذا ملأته للسقاء وغيره (tahdhib)","source_summary":"Ortak kayıt su içen hayvanın dolmasını ve suya kanma aşamasını, ayrıca bir kabın doldurularak dolu hale getirilmesini aynı eylem ailesinde verir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه تحبب الحمار أو الإبل من الماء، وأول الري، وملء السقاء ونحوه حتى يمتلئ.","what_is_not_ar":"ليس الإحباب بمعنى بروك البعير من مرض، ولا الحب بمعنى الجرة."},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_000286/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:2:2","qac_word_ref":"100:8:2","surface_ar":"حُبِّ"}],"gloss":"iri küp ve iki kulplu küpün dört parçalı desteği","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İri küp veya büyük saklama kabı."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İki kulplu küpün altına konan dört parçalı ahşap destek."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kanıttaki iki göndergenin ikisini de, iri saklama kabını ve bu kabın altına konan ahşap desteği, tek bir üretken anlam varsaymadan temsil eder.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"الحب جرة عظيمة أو موضعها","concept_gloss":"iri küp ve iki kulplu küpün dört parçalı desteği","definition":"Kayıt, iri bir küp ile iki kulplu küpün altına konan dört parçalı desteği aynı dalda birleştirir. Bu iki ayrı nesne yapısal olarak ayrılmadan tek bir kavram tanımı kurulamaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İri küp veya büyük saklama kabı."},{"facet_id":"F002","role":"source_variant","statement":"İki kulplu küpün altına konan dört parçalı ahşap destek."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"iri küp veya büyük saklama kabı"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"iki kulplu küpün dört parçalı ayağı"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"الحب الجرة الضخمة ويجمع على حببة وحباب (ayn;tahdhib)؛ الحب الخابية فارسي معرب والجمع حباب وحببة (sihah)؛ الحب الخشبات الأربع التي توضع عليها الجرة ذات العروتين (ayn;tahdhib)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه الحب بمعنى الجرة الضخمة أو الخابية، وجمعه حباب وحببة، وما قيل في الخشبات التي توضع عليها الجرة.","what_is_not_ar":"ليس الحب بمعنى المحبة ولا الحبة النباتية."},"support_links":[]},{"boundary":"Su kabarcığı, su kütlesi ve yüzey izi söz öbeğine bağlı değişkelerdir; ağaç üzerindeki çiy ayrı bir uzantıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000286/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:2:2","qac_word_ref":"100:8:2","surface_ar":"حُبِّ"}],"gloss":"su kabarcıkları, su yüzeyi ve ağaç üzerindeki çiy","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Su yüzeyinde yüzen kabarcıklar."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Suyun ana kütlesi, dalgası veya yüzeyindeki çizgiler."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ağaçların üzerinde sabah görülen çiy."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Su söz öbeğinin değişkenlerini ve ayrı çiy uzantısını kapsam ayrılığını koruyarak temsil eder.","boundary_detail":"Su kabarcığı, su kütlesi ve yüzey izi söz öbeğine bağlı değişkelerdir; ağaç üzerindeki çiy ayrı bir uzantıdır.","branch_image_ar":"حباب الماء فقاقيعه وطرائقه","concept_gloss":"su kabarcıkları, su yüzeyi ve ağaç üzerindeki çiy","contextual_glosses":[{"applicability":"Suyun üzerinde yüzen küçük hava keseciklerinin anlatıldığı fiziksel bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Suyun ana kütlesi, dalgaları, yüzey çizgileri ve ağaç üzerindeki çiy kullanımlarını dışarıda bırakır.","preserves":"Suyun yüzeyindeki yüzen kabarcıklar anlamını tam korur."},"facet_ids":["F001"],"text":"su kabarcıkları","usage_role":"contextual"}],"definition":"Suya bağlı söz öbeğinde yüzeyde yüzen kabarcıkları, suyun ana kütlesini veya dalga ve çizgilerini anlatır. Ayrı bir yalın kullanımda ağaçların üzerinde sabah görülen çiyi belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Su yüzeyinde yüzen kabarcıklar."},{"facet_id":"F002","role":"source_variant","statement":"Suyun ana kütlesi, dalgası veya yüzeyindeki çizgiler."},{"facet_id":"F003","role":"extension","statement":"Ağaçların üzerinde sabah görülen çiy."}],"identity_rationale":"Kaynak ifadesi su yüzeyindeki kabarcıkları, suyun ana kütlesini, dalga ve çizgilerini, ayrıca ağaç üzerindeki çiyi birlikte verir. Dal kullanılabilir, ancak suya bağlı söz öbeğinin değişkenleri ile ayrı çiy kullanımı tek bir fiziksel olgu gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"su kabarcıkları, suyun ana kütlesi, dalgası veya yüzey çizgileri"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"ağaç üzerindeki çiy"}],"lexicalization_note":"Dal suya bağlı bir söz öbeği ile yalın çiy kullanımını içerir; söz öbeğinin bütün değişkeleri genel yalın anlama dönüştürülmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; su yüzeyindeki çizgileri doğrudan paylaşan aday yayımlandı. Köpük, rüzgâr, dalga ve aynı kökün başka anlamları yalnızca alan komşuluğu sağladı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yüzey çizgileri bakımından yakınlaşırlar; odak dal çok anlamlı söz öbeği içinde kabarcık, su kütlesi ve çiyi de içerdiği için komşunun daha dar görsel alanıyla tam örtüşmez.","focus_only":"Odak dal yüzey çizgilerinin yanında kabarcıkları, su kütlesini, dalgayı ve ağaç üzerindeki çiyi de kapsar.","gloss":"suyun yüzey çizgileri","neighbor_only":"Komşu dal özellikle suyun süslü görünüm veren çizgi ve biçimlerine odaklanır.","neighbor_ref":"root_000628/B004","relation_type":"near_synonym","shared_zone":"İki dal su yüzeyinde görülen çizgileri ve düzenli görünüşleri kapsar."}],"source_phrase_ar":"حباب الماء فقاقيعه الطافية (ayn;tahdhib)؛ حباب الماء معظمه (maqayis;ayn;sihah;tahdhib)؛ حباب الماء موجه والطرائق التي في الماء (tahdhib)؛ الحباب من الماء النفاخات تشبيها به (mufradat)؛ الحباب الطل على الشجر (tahdhib)","source_summary":"Ortak kayıt su bağlamında kabarcık, ana su kütlesi, dalga ve yüzey çizgisi değişkelerini toplar; ayrıca ağaç üzerindeki çiyi ayrı bir kullanım olarak ekler.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه حباب الماء بمعنى الفقاقيع الطافية أو معظم الماء أو موجه وطرائقه، وما ألحق به من الطل على الشجر.","what_is_not_ar":"ليس الحب الحبوب، ولا حبب الأسنان، ولا الحباب بمعنى الحية."},"support_links":[]},{"boundary":"Dal diş dizilişi ve üzerindeki beyaz tükürük görünüşüyle sınırlıdır; su kabarcığı veya bitkisel tane anlamı değildir.","branch_kind":"bare","branch_ref":"root_000286/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:2:2","qac_word_ref":"100:8:2","surface_ar":"حُبِّ"}],"gloss":"düzenli diş dizisi ve beyaz tükürük parıltısı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişlerin taneler gibi düzenli ve yan yana dizilmesi."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişlerin üzerinde beyaz tükürüğün tanecikli ve parlak görünmesi."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişlerin hem düzenini hem de üzerlerindeki beyaz görünüşü taşıyan açıklayıcı karşılıktır.","boundary_detail":"Dal diş dizilişi ve üzerindeki beyaz tükürük görünüşüyle sınırlıdır; su kabarcığı veya bitkisel tane anlamı değildir.","branch_image_ar":"حبب الأسنان انتظام كالدرر","concept_gloss":"düzenli diş dizisi ve beyaz tükürük parıltısı","contextual_glosses":[{"applicability":"Dişlerin düzenli ve güzel dizilişinin betimlendiği bağlamda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dişlerin üzerinde görülen beyaz tükürük tanecikleri ve parıltısını açıkça vermez.","preserves":"Dişlerin küçük taneler gibi düzenli dizilişini korur."},"facet_ids":["F001"],"text":"inci gibi dizilmiş dişler","usage_role":"contextual"}],"definition":"Dişlerin taneler gibi düzenli biçimde yan yana dizilmesi ve üzerlerinde beyaz tükürüğün tanecikli bir parlaklık oluşturmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dişlerin taneler gibi düzenli ve yan yana dizilmesi."},{"facet_id":"F002","role":"extension","statement":"Dişlerin üzerinde beyaz tükürüğün tanecikli ve parlak görünmesi."}],"identity_rationale":"Kaynak ifadesi dişlerin düzenli dizilişini ve dişlerin üzerinde tanecikler halinde görünen beyaz tükürük parıltısını açıkça birleştirir. Sağlanan dal çerçevesi düzen ile beyaz görünüşü doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"düzenli diş dizisi veya dişlerdeki beyaz tükürük parıltısı"}],"lexicalization_note":"Dal dişlerin düzeni ve beyaz görünüşüne ait yalın biçimi tanımlar; başka nesnelerdeki tane veya kabarcık anlamları eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; diş düzeni ve beyazlığını birlikte paylaşan aday yayımlandı. Yalnızca parlaklık, belirli diş türü veya yüz güzelliği bildirenler elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Düzen ve beyazlıkta yakın anlamlıdırlar; odak dal tanecikli tükürük görünüşüne özgüyken komşu dal diş yapısının düzgünlük, aralık ve genel güzellik özelliklerini daha geniş tutar.","focus_only":"Odak dal taneye benzer düzenin yanında dişler üzerindeki beyaz tükürük parıltısını özellikle kapsar.","gloss":"düzgün ve beyaz dişler","neighbor_only":"Komşu dal dişlerin düzgün çıkışını, aralıklı oluşunu, beyazlığını ve genel güzelliğini daha geniş biçimde kapsar.","neighbor_ref":"root_000540/B003","relation_type":"near_synonym","shared_zone":"İki dal dişlerin düzenli dizilişini, beyazlığını ve güzel görünüşünü paylaşır."}],"source_phrase_ar":"الحبب تنضد الأسنان (maqayis;ayn;sihah;tahdhib)؛ الحبب تنضد الأسنان تشبيها بالحب (mufradat)؛ حبب الفم ما يتحبب من بياض الريق على الأسنان (tahdhib)","source_summary":"Ortak kayıt dişlerin düzenli dizilişini temel alır ve bu görünüşü taneye benzetir; dişler üzerindeki beyaz tükürük parıltısını da aynı alana bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الحبب وحبب الأسنان، أي تنضد الأسنان وظهور بياض الريق عليها.","what_is_not_ar":"ليس حباب الماء، ولا الحبة النباتية إلا من جهة التشبيه."},"support_links":[]},{"boundary":"Temel alan kısa veya küçük beden yapısıdır; develerdeki cılızlık ayrı ve türemiş bir kullanım olarak tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_000286/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:2:2","qac_word_ref":"100:8:2","surface_ar":"حُبِّ"}],"gloss":"kısa veya küçük yapılı; develerde cılız","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanın kısa boylu veya küçük bedenli olması."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Küçük kişileri topluca niteleyen çoğul kullanım."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Develerin cılız ve zayıf oluşunu bildiren söz öbeği."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan için temel beden ölçüsünü ve deve söz öbeğindeki zayıflık uzantısını ayrı tutan karşılıktır.","boundary_detail":"Temel alan kısa veya küçük beden yapısıdır; develerdeki cılızlık ayrı ve türemiş bir kullanım olarak tutulur.","branch_image_ar":"الحبحاب الصغير القصير","concept_gloss":"kısa veya küçük yapılı; develerde cılız","contextual_glosses":[{"applicability":"Bir insanın boyunun kısa olduğu doğrudan niteleme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel küçük beden anlamını ve develere özgü cılızlık kullanımını dışarıda bırakır.","preserves":"İnsan için kısa boy nitelemesini açık biçimde korur."},"facet_ids":["F001"],"text":"kısa boylu","usage_role":"contextual"}],"definition":"Bir insanın kısa boylu veya küçük bedenli olmasıdır. Develere bağlı söz öbeğinde ise kısa boydan çok cılız ve zayıf oluşu bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanın kısa boylu veya küçük bedenli olması."},{"facet_id":"F002","role":"specialization","statement":"Küçük kişileri topluca niteleyen çoğul kullanım."},{"facet_id":"F003","role":"extension","statement":"Develerin cılız ve zayıf oluşunu bildiren söz öbeği."}],"identity_rationale":"Kaynak ifadesi kısa veya küçük yapılı insanı ve küçükleri temel alırken zayıf develeri ayrıca aynı türemiş biçim alanında verir. Dal korunabilir, ancak insanın kısa ve küçük oluşu ile develerin zayıflığı tek bedensel özellik gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kısa boylu veya küçük bedenli kimse"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"cılız develer"}],"lexicalization_note":"Dal yalın kısa veya küçük beden nitelemesiyle develere bağlı bir söz öbeğini içerir; deve cılızlığı genel kısa boy anlamına yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kısa ve küçük beden çekirdeğini en doğrudan paylaşan aday yayımlandı. Yalnızca zayıflık, irilik veya hayvan türü paylaşanlar daha uzaktı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"İnsan nitelemesinde yakın anlamlıdırlar; odak dalın deve cılızlığına özgü uzantısı, komşunun ise daha genel küçüklük ve alçaklık kapsamı bulunduğu için sınırlar kısmen eşleşir.","focus_only":"Odak dal insanın kısa veya küçük bedenini ve söz öbeğinde develerin cılızlığını kapsar.","gloss":"kısa ve küçük yapılı","neighbor_only":"Komşu dal insan dışındaki küçük varlıkları ve fiziksel alçaklığı da kapsayan daha genel bir küçüklük alanına uzanır.","neighbor_ref":"root_000336/B005","relation_type":"near_synonym","shared_zone":"İki dal insan için kısa boy ve küçük beden nitelemesinde örtüşür."}],"source_phrase_ar":"الحبحاب الرجل القصير (maqayis)؛ الحباحب الصغار (maqayis;sihah)؛ الحبحاب الصغير الجسم (tahdhib)؛ إبل حبحبة مهازيل (tahdhib)","source_summary":"Ortak kayıt insan için kısa boy ve küçük beden nitelemesini verir; aynı biçim ailesindeki deve söz öbeğini ise cılızlık ve zayıflık anlamıyla ekler.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الحبحاب والحباحب بمعنى القصير أو الصغير الجسم، وما وصف به من هزال الإبل.","what_is_not_ar":"ليس البعير المحب الذي يبرك من عجز، ولا نار الحباحب."},"support_links":[]},{"boundary":"Çekirdek zayıf ve işe yaramayan kıvılcımdır; gece ışıldayan böcek, ışık görünüşüne bağlı ayrı bir değişkedir.","branch_kind":"mixed_non_bare","branch_ref":"root_000286/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:2:2","qac_word_ref":"100:8:2","surface_ar":"حُبِّ"}],"gloss":"yararsız zayıf kıvılcım veya gece ışıldayan böcek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Taş çarpışmasından veya at toynağından çıkan, işe yaramayan zayıf kıvılcım."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Geceleri uçarken kandil gibi ışık saçan böcek."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu tür zayıf kıvılcımın veya ateşin tutuşması."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kıvılcım çekirdeğini ve ışık benzerliğine dayalı böcek değişkesini birlikte karşılar.","boundary_detail":"Çekirdek zayıf ve işe yaramayan kıvılcımdır; gece ışıldayan böcek, ışık görünüşüne bağlı ayrı bir değişkedir.","branch_image_ar":"نار الحباحب شرر لا ينتفع به","concept_gloss":"yararsız zayıf kıvılcım veya gece ışıldayan böcek","contextual_glosses":[{"applicability":"Taşların veya toynakların çarpışmasıyla çıkan ve ateş yakmaya yetmeyen kıvılcım bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Geceleri ışık saçan böcek değişkesini ve tutuşma eylemini dışarıda bırakır.","preserves":"Kıvılcımın zayıf ve yararlanılamaz oluşunu korur."},"facet_ids":["F001"],"text":"boşuna çıkan zayıf kıvılcım","usage_role":"contextual"}],"definition":"Taşların çarpışmasından veya atların toynaklarından havaya saçılan, ateş yakmaya yaramayan zayıf kıvılcımdır. Aynı adlandırma, geceleri kandil gibi ışık saçarak uçan böcek için de kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Taş çarpışmasından veya at toynağından çıkan, işe yaramayan zayıf kıvılcım."},{"facet_id":"F002","role":"source_variant","statement":"Geceleri uçarken kandil gibi ışık saçan böcek."},{"facet_id":"F003","role":"associated_use","statement":"Bu tür zayıf kıvılcımın veya ateşin tutuşması."}],"identity_rationale":"Kaynak ifadesi taşların çarpışmasından veya atların toynaklarından çıkan yararsız kıvılcımları ve geceleri ışık saçan uçucu böceği birlikte verir. Dal korunabilir, ancak böcek kıvılcımın bir aşaması değil, ışık benzerliğiyle aynı adlandırma alanına giren ayrı bir referanstır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yararsız zayıf kıvılcım veya gece ışıldayan böcek"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"zayıf kıvılcımın tutuşması"}],"lexicalization_note":"Dal bir kalıplaşmış birim ile onun tutuşma biçimini içerir; kıvılcım ve ışıldayan böcek değişkeleri yalın köke genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel kıvılcım alanını doğrudan paylaşan aday yayımlandı. Taş, parlama, tutuşma ve kanat çırpma adayları yalnızca senaryo bağı kurdu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Kıvılcım alanında yakın anlamlıdırlar; odak dal kaynak ve yararsızlık koşullarıyla daralır, ayrıca ışıldayan böceğe uzanır, komşu ise genel kıvılcım adıdır.","focus_only":"Odak dal belirli çarpışmalardan doğan yararsız zayıf kıvılcımı ve ayrıca ışıldayan gece böceğini kapsar.","gloss":"ateşten sıçrayan kıvılcım","neighbor_only":"Komşu dal kaynağına, yararına veya gücüne bakmadan ateşten sıçrayan kıvılcımı genel olarak kapsar.","neighbor_ref":"root_000787/B003","relation_type":"near_synonym","shared_zone":"İki dal da havaya saçılan küçük ateş parçalarını ve kıvılcımları kapsar."}],"source_phrase_ar":"نار الحباحب ما اقتدحت من شرار النار في الهواء من تصادم الحجارة (ayn;tahdhib)؛ نار الحباحب ما أورت الخيل لا ينتفع به (maqayis;sihah;tahdhib)؛ ذباب يطير بالليل له شعاع كالسراج (ayn;sihah;tahdhib)","source_summary":"Ortak kayıt çarpışma veya toynak vuruşuyla çıkan yararsız kıvılcımı temel alır ve geceleri ışık saçan uçucu böceği görünüş benzerliğiyle aynı adlandırmaya bağlar.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه نار الحباحب، الشرر الضعيف من الحجارة أو حوافر الخيل، والذباب أو الطائر المضيء ليلا، والنار التي لا ينتفع بها.","what_is_not_ar":"ليس الحباحب بمعنى الصغار، ولا الحب بمعنى المحبة."},"support_links":[]},{"boundary":"Temel anlam yılandır; kötücül ruh adı, yılanla kurulan adlandırma ilişkisine bağlı ikincil kullanımdır.","branch_kind":"bare","branch_ref":"root_000286/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:2:2","qac_word_ref":"100:8:2","surface_ar":"حُبِّ"}],"gloss":"yılan; yılanla ilişkilendirilen kötücül ruh adı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yılanı adlandıran yalın sözlük anlamı."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yılanla kurulan adlandırma ilişkisi üzerinden kötücül bir ruhun adı olarak kullanım."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Temel hayvan referansını ve ondan türeyen ad kullanımını hiyerarşisini bozmadan karşılar.","boundary_detail":"Temel anlam yılandır; kötücül ruh adı, yılanla kurulan adlandırma ilişkisine bağlı ikincil kullanımdır.","branch_image_ar":"الحباب الحية أو الشيطان","concept_gloss":"yılan; yılanla ilişkilendirilen kötücül ruh adı","contextual_glosses":[{"applicability":"Sözün doğrudan hayvanı adlandırdığı temel sözlük bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yılanla ilişkilendirilerek kurulan kötücül ruh adı kullanımını dışarıda bırakır.","preserves":"Dalın temel hayvan referansı olan yılan anlamını tam korur."},"facet_ids":["F001"],"text":"yılan","usage_role":"general"}],"definition":"Bir yılanı adlandırır. Yılanın kötücül ruhla özdeşleştirildiği adlandırma geleneği üzerinden aynı söz bir kötücül ruhun adı olarak da kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yılanı adlandıran yalın sözlük anlamı."},{"facet_id":"F002","role":"associated_use","statement":"Yılanla kurulan adlandırma ilişkisi üzerinden kötücül bir ruhun adı olarak kullanım."}],"identity_rationale":"Kaynak ifadesi sözün temel referansını yılan olarak verir ve kötücül ruh adı kullanımını yılanın da böyle adlandırılmasıyla açıklar. Dal korunabilir, ancak yılan ile kötücül ruh eş anlamlı iki temel anlam gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"yılan veya yılanla ilişkilendirilen kötücül ruh adı"}],"lexicalization_note":"Dal yalın biçimin yılan anlamını ve buna bağlı kötücül ruh adı kullanımını kapsar; su veya sevgi söz öbekleri tanıma girmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yılan referansını en doğrudan paylaşan aday yayımlandı. Belirli yılan türleri, özel adlar ve yalnızca kötücül ruh alanı paylaşanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Temel hayvan referansında yakın anlamlıdırlar; odak dal kötücül ruh adına uzanırken komşu dal yılanın cinsiyet ve türeme alanını genişletir, bu yüzden sınırları tam eşleşmez.","focus_only":"Odak dal yılan anlamının yanında yılanla ilişkilendirilen kötücül ruh adı kullanımını kapsar.","gloss":"yılan adı","neighbor_only":"Komşu dal yılanın erkeğini, dişisini ve yılanlarla uğraşan kişiye bağlı türemiş adları daha geniş biçimde kapsar.","neighbor_ref":"root_000383/B004","relation_type":"near_synonym","shared_zone":"İki dalın temel referansı cinsiyet ayrımı yapılmadan yılan hayvanıdır."}],"source_phrase_ar":"ومما شذ عن الباب الحباب وهو الحية (maqayis)؛ الحباب أيضا الحية (sihah)؛ الحباب الحية وإنما قيل الحباب اسم شيطان لأن الحية يقال لها شيطان (tahdhib)","source_summary":"Ortak kayıt yalın anlamı yılan olarak verir; kötücül ruh adı kullanımını ise yılanın da kötücül ruh sayılmasına dayanan bir adlandırma ilişkisiyle açıklar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الحباب بمعنى الحية، وما قيل في اسم الشيطان لكون الحية شيطانا.","what_is_not_ar":"ليس حباب الماء، ولا حبابك بمعنى غاية محبتك، ولا الحب بمعنى المحبة."},"support_links":[]},{"boundary":"Bu dal genel iyilik değeridir; seçme eylemi, özel olarak mal, cömertlik veya belirli bir kullanım kalıbı bu çekirdeğin yerine geçirilmez.","branch_kind":"bare","branch_ref":"root_000452/B001","candidate_links":[{"candidate_id":"cand_f5c5c8be459cd50c8e1f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَيْر","morph_features":"STEM|POS:N|LEM:xayor|ROOT:xyr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:3:2","qac_word_ref":"100:8:3","surface_ar":"خَيْرِ"}],"gloss":"arzulanan iyilik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Herkesçe arzu edilen ve kötülüğün karşısında duran genel olumlu değeri bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bağlama göre yarar yönü belirginleşebilir ve kavram zararın karşısına da yerleştirilebilir."}}],"root_ar":"خ ي ر","root_id":"root_000452","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel olumlu değerin kötülüğe karşı konduğu ve insanların ona yöneldiği yalın kullanımlar için uygundur.","boundary_detail":"Bu dal genel iyilik değeridir; seçme eylemi, özel olarak mal, cömertlik veya belirli bir kullanım kalıbı bu çekirdeğin yerine geçirilmez.","branch_image_ar":"الميل إلى الخير النافع","concept_gloss":"arzulanan iyilik","contextual_glosses":[{"applicability":"Olumlu değerin doğrudan kötülüğün karşıtı olarak kullanıldığı genel bağlamlara uyar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Herkesçe arzulanma ile yarar ve üstünlük yönlerini tek başına belirtmez.","preserves":"Kötülüğün karşıtı olan olumlu değer yönünü korur."},"facet_ids":["F001"],"text":"iyilik","usage_role":"general"},{"applicability":"Olumlu değerin özellikle zararın karşısında ve fayda sağlayan yönüyle öne çıktığı bağlamlara uyar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kötülüğün karşıtı olan daha geniş ahlaki ve değer bildiren kapsamı dışarıda bırakır.","preserves":"Zararın karşısındaki fayda sağlayan yönü korur."},"facet_ids":["F002"],"text":"yarar","usage_role":"contextual"}],"definition":"İnsanların yöneldiği ve arzu ettiği, kötülüğün karşıtı olan genel olumlu değerdir; bağlama göre yarar yönü öne çıkabilir ve zarara da karşı konabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Herkesçe arzu edilen ve kötülüğün karşısında duran genel olumlu değeri bildirir."},{"facet_id":"F002","role":"extension","statement":"Bağlama göre yarar yönü belirginleşebilir ve kavram zararın karşısına da yerleştirilebilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Birden çok seçenek arasında karar verme eylemini anlamın merkezine ekler.","collision":"Aynı kökün seçme ve seçilme dalıyla karışır.","fit":"displacement","loses":"Genel olumlu değer, kötülüğe karşıtlık ve yarar kapsamını kaybeder.","preserves":"Daha iyi olana yönelme düşüncesini dolaylı olarak çağrıştırabilir."},"text":"seçim"}],"identity_rationale":"Kaynak ifadesi, herkesin yöneldiği ve arzuladığı genel olumlu değeri kötülüğün karşıtı olarak kurar; ayrıca bağlama göre kötülüğe ya da zarara karşı konabildiğini belirtir. Verilen dal çerçevesi bu genel çekirdeği ve yarar yönünü doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"iyilik; yarar veya üstünlük taşıyan olumlu şey"}],"lexicalization_note":"Tanım yalın dalın genel değer anlamıyla sınırlıdır; seçim, mal veya armağanla ilgili özel dalların anlamları buraya taşınmaz.","neighbor_coverage_note":"Gösterilen bütün adaylar değerlendirildi. Yarar, erdemli davranış, üstün nitelik ve cömertlik sınırı en açıklayıcı karşılaştırmaları verdi; yalnızca ortak olumlu çağrışım, örnek veya uzak konu bağı taşıyan diğer adaylar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yararı içine alabilen daha geniş bir iyilik değeridir; komşu dal ise doğrudan fayda sağlama ilişkisini anlatır.","focus_only":"Kötülüğün karşıtı olan genel olumlu değeri ve arzu edilirliği kapsar.","gloss":"genel iyilik ile yarar","neighbor_only":"Fayda sağlama ve zararın karşıtı olma ilişkisini anlamın doğrudan çekirdeği yapar.","neighbor_ref":"root_001536/B001","relation_type":"near_synonym","shared_zone":"Her ikisi de olumlu sonuç, fayda ve zarardan uzaklık alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal genel değer kategorisidir; komşu dal bu değeri inanç ve davranıştaki düzgünlük ve bağlılıkla somutlaştırır.","focus_only":"Yarar yönü öne çıkabilen her türlü genel olumlu değeri kapsayabilir.","gloss":"genel iyilik ile erdemli davranış","neighbor_only":"Düzgünlük, sakınma ve yaratıcıya bağlılıkla ilgili davranış alanını özellikle kapsar.","neighbor_ref":"root_000104/B002","relation_type":"near_synonym","shared_zone":"İki dal da iyilik ve olumlu davranış değeri alanında kesişir."},{"boundary_match":"partial","distinction":"Odak dal soyut ve genel iyiliktir; komşu dal bu değeri taşıdığı düşünülen kişi veya şeyin niteliğidir.","focus_only":"Bir kişi veya nesneye yüklenmeden de var olan genel iyilik değerini bildirir.","gloss":"iyilik ile üstün nitelik","neighbor_only":"Belirli bir kişi veya şeyin üstün, iyi ya da seçkin oluşunu niteleme konusu yapar.","neighbor_ref":"root_000452/B002","relation_type":"near_neighbor","shared_zone":"Her ikisi de olumlu değer değerlendirmesi alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal üst kavram niteliğindeki genel iyiliktir; komşu dal bunun verme ve armağanla belirlenen özel görünümüdür.","focus_only":"Cömertlikten bağımsız olarak arzu edilen her türlü olumlu değeri kapsar.","gloss":"iyilik ile cömertlik","neighbor_only":"İyiliği verme, armağan etme ve kişide cömertlik bolluğu olarak somutlaştırır.","neighbor_ref":"root_000452/B005","relation_type":"near_neighbor","shared_zone":"Cömertlik olumlu ve arzu edilen bir iyilik türü olduğundan iki dal kesişir."}],"source_phrase_ar":"فالخير خلاف الشر لأن كل أحد يميل إليه (maqayis)؛ الخير ضد الشر (jamhara;sihah)؛ الخير ما يرغب فيه الكل وضده الشر (mufradat)؛ يقابل به الشر مرة والضر مرة (mufradat)","source_summary":"Kaynakların ortak çekirdeği, insanların yöneldiği genel olumlu değerin kötülüğün karşıtı olmasıdır. Bu değer bazı bağlamlarda yarar yönüyle belirginleşerek zararla karşıtlık da kurar.","sources":["MQ","JA","SI","MU"],"what_is_ar":"يدخل فيه الخير العام المرغوب فيه، وضد الشر، وما فيه نفع أو فضل أو صلاح، والخير المطلق والمقيد، ومقابلته للشر أو الضر.","what_is_not_ar":"لا يدخل خصوص الاختيار والاستخارة، ولا خصوص المال، ولا ألفاظ الخيار المعربة للنبات."},"support_links":["sup_8db776420fd3a411d98e"]},{"boundary":"Bu dal salt karşılaştırma derecesi değil, kişi veya şeyde bulunan iyilik ve üstünlük niteliğidir; genel iyilik ile seçme eyleminden ayrıdır.","branch_kind":"bare","branch_ref":"root_000452/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَيْر","morph_features":"STEM|POS:N|LEM:xayor|ROOT:xyr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:3:2","qac_word_ref":"100:8:3","surface_ar":"خَيْرِ"}],"gloss":"iyi ve seçkin olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi veya şeyi iyilik ve değer bakımından üstün, iyi ve seçkin olarak niteler."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsanlarda düzgünlük ve erdemin yanı sıra güzellik ve hoş görünüş yönünü de belirginleştirebilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir topluluk veya tür içinden düşük nitelikli olmayan üstün ve seçilmiş üyeleri gösterebilir."}}],"root_ar":"خ ي ر","root_id":"root_000452","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi veya şeyin değer, düzgünlük, güzellik ya da seçkinlik bakımından üstün nitelenmesini kapsayan genel karşılıktır.","boundary_detail":"Bu dal salt karşılaştırma derecesi değil, kişi veya şeyde bulunan iyilik ve üstünlük niteliğidir; genel iyilik ile seçme eyleminden ayrıdır.","branch_image_ar":"فضل الصلاح والاصطفاء","concept_gloss":"iyi ve seçkin olma","contextual_glosses":[{"applicability":"Kişi, hayvan veya nesnenin kendi türü içinde değerli ve iyi sayıldığı niteleme bağlamlarına uyar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Düzgünlük, güzellik ve seçilmişlik yönlerinden hangisinin öne çıktığını belirtmez.","preserves":"Değer ve nitelik bakımından üstünlük çekirdeğini korur."},"facet_ids":["F001"],"text":"üstün nitelikli","usage_role":"general"},{"applicability":"Bir topluluk içinden iyi ve düşük nitelikten uzak üyelerin çoğul olarak gösterildiği bağlamlara uyar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir kişi veya şeyde bulunan genel iyilik ve güzellik niteliğini kapsamaz.","preserves":"Üstün üyelerin diğerlerinden ayrılması ve seçkinlik yönünü korur."},"facet_ids":["F003"],"text":"seçkinler","usage_role":"contextual"}],"definition":"Bir kişi veya şeyin iyilik, düzgünlük, güzellik ya da başka bir değer yönünden üstün ve seçkin olmasıdır. Çoğul ve seçme bağlamlarında sıradan veya düşük sayılanlardan ayrılmış iyi üyeleri de gösterebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi veya şeyi iyilik ve değer bakımından üstün, iyi ve seçkin olarak niteler."},{"facet_id":"F002","role":"specialization","statement":"İnsanlarda düzgünlük ve erdemin yanı sıra güzellik ve hoş görünüş yönünü de belirginleştirebilir."},{"facet_id":"F003","role":"extension","statement":"Bir topluluk veya tür içinden düşük nitelikli olmayan üstün ve seçilmiş üyeleri gösterebilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Açık bir karşılaştırma ölçüsü ve ikinci bir karşılaştırılan öğe gerektirir.","collision":"Salt karşılaştırma derecesiyle karışır.","fit":"displacement","loses":"Kişi veya şeyde yerleşik iyilik, düzgünlük ve seçkinlik niteliğini zayıflatır.","preserves":"Bir değer üstünlüğü bulunduğu düşüncesini korur."},"text":"daha iyi"}],"identity_rationale":"Kaynak ifadesi insanı, hayvanı veya başka bir şeyi iyilik, düzgünlük, güzellik ya da seçkinlik bakımından üstün niteleyen kullanımları birlikte verir. Verilen çerçeve bu niteleme çekirdeğini ve sıradanlıktan uzak seçkinlik sınırını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"iyi ve üstün nitelikli"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"üstün, güzel veya seçkin olan"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"üstün veya seçkin kimse ya da şey"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"iyi ve erdemli kişiler"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"üstün, güzel veya seçilmiş olanlar"}],"lexicalization_note":"Tanım yalın niteleme dalına bağlıdır; seçim işlemi veya yalnızca belirli bir söz kalıbında doğan anlam buraya genellenmez.","neighbor_coverage_note":"Bütün aday komşular incelendi. Seçilmiş üst kesim, yüksek nitelik, genel iyilik ve seçme süreciyle kurulan dört sınır yayımlandı; güzellik, övgü, benzersizlik veya cömertlikle yalnızca dolaylı kesişen adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal seçme işlemi bulunmadan da üstün niteliği bildirir; komşu dal ise seçilip ayrılmış üst kesimi daha belirgin biçimde öne çıkarır.","focus_only":"Seçilmiş olmanın yanı sıra iyilik, düzgünlük veya güzellik bakımından üstün niteliği de kapsar.","gloss":"üstün nitelik ile seçilmiş seçkinler","neighbor_only":"Bir topluluğun doruğundaki üyelerin özellikle seçilip ayrılması ve öncü sayılması üzerinde durur.","neighbor_ref":"root_001512/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir topluluk içindeki üstün ve seçkin üyeleri gösterebilir."},{"boundary_match":"partial","distinction":"Odak dal iyilik ve seçkinliği merkez alır; komşu dal soyluluk, incelik ve uç derece gibi daha farklı kalite ölçülerine de açılır.","focus_only":"Düzgünlük ve seçilmişlik yönünü, düşük nitelikten uzak iyi üyeleri kapsar.","gloss":"seçkinlik ile yüksek nitelik","neighbor_only":"İncelik, soyluluk ve bir niteliğin iyi ya da kötü uç noktasına varması gibi ek kapsamlar taşır.","neighbor_ref":"root_000979/B002","relation_type":"near_synonym","shared_zone":"Kişi, hayvan veya şeyin kendi türü içinde iyi ve üstün sayılmasında kesişirler."},{"boundary_match":"partial","distinction":"Odak dal nitelenen varlığın özelliğidir; komşu dal bu tür nitelemelere ölçü olabilen genel olumlu değerdir.","focus_only":"Belirli bir kişi veya şeyde bulunan üstün ve seçkin niteliği bildirir.","gloss":"üstün olan ile genel iyilik","neighbor_only":"Herhangi bir taşıyıcıya bağlı olmadan genel ve arzu edilen iyilik değerini bildirir.","neighbor_ref":"root_000452/B001","relation_type":"near_neighbor","shared_zone":"Üstün sayılan kişi veya şeyin değerlendirilmesi genel iyilik ölçüsüne dayanabilir."},{"boundary_match":"partial","distinction":"Odak dal sonuçta bulunan üstün niteliktir; komşu dal bu niteliğe göre karar verme veya seçme sürecidir.","focus_only":"Bir varlığın seçme gerçekleşmeden de iyi ve üstün olmasını kapsar.","gloss":"seçkin olma ile seçme","neighbor_only":"Daha iyi görüleni ayırıp seçme, seçim hakkı verme veya iyi sonucu isteme işlemini kapsar.","neighbor_ref":"root_000452/B003","relation_type":"near_neighbor","shared_zone":"Bir şeyin üstün görülmesi onu seçmenin ölçüsü olabilir."}],"source_phrase_ar":"رجل خير وامرأة خيرة فاضلة وقوم خيار وأخيار في صلاحها وامرأة خيرة في جمالها وميسمها (maqayis;ayn)؛ رجل خير إذا كان فيه خير ورجل خيار من قوم خيار وأخيار والأخيار خلاف الأشرار (jamhara)؛ الخيرات جمع خيرة وهي الفاضلة من كل شيء (sihah)؛ فيهن مختارات لا رذل فيهن والخير الفاضل المختص بالخير (mufradat)","source_summary":"Kaynakların ortak çerçevesi, kişi veya şeyde iyilik ve üstünlük bulunmasıdır. Bu üstünlük düzgünlük, güzellik veya seçkinlik olarak belirginleşebilir; çoğul kullanımlar iyi ve düşük nitelikten uzak üyeleri gösterebilir.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه وصف الإنسان أو الشيء بأنه خير أو خيرة أو خيار أو أخيار، بمعنى الفضل والصلاح والجمال والميسم والاختيار من غير رذالة.","what_is_not_ar":"لا يدخل خير التفضيل المحض إذا كان مجرد صيغة أفعل، ولا أسماء الأعلام والقبائل إلا من جهة التسمية."},"support_links":[]},{"boundary":"Dal, daha iyi olanı belirleme ve seçme çevresinde örgütlenir; hayvanı yuvasından çıkarma anlamındaki ayrı kullanım yalnızca biçim benzerliği taşır.","branch_kind":"mixed_non_bare","branch_ref":"root_000452/B003","candidate_links":[{"candidate_id":"cand_69eb74cb192c7f238c85","lane":"micro"},{"candidate_id":"cand_eb5f6311162b51421299","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَيْر","morph_features":"STEM|POS:N|LEM:xayor|ROOT:xyr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:3:2","qac_word_ref":"100:8:3","surface_ar":"خَيْرِ"}],"gloss":"daha iyi olanı seçme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Olasılıklar arasından daha iyi görüleni arayıp ayırmayı, seçmeyi ve seçilmiş sonucu bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi için iki olasılıktan daha iyi olanı Yaratıcıdan dileme ve iyi sonucun belirlenmesini isteme anlamını taşır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Seçim hakkını bir başkasına bırakma veya birini seçim bakımından üstün gelmiş sayma gibi ilişki biçimlerini kapsar."}}],"root_ar":"خ ي ر","root_id":"root_000452","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Seçenekler arasından üstün veya daha yararlı görüleni belirleyip alma çekirdeğini anlatan genel kullanımlara uyar.","boundary_detail":"Dal, daha iyi olanı belirleme ve seçme çevresinde örgütlenir; hayvanı yuvasından çıkarma anlamındaki ayrı kullanım yalnızca biçim benzerliği taşır.","branch_image_ar":"طلب الخير بالاختيار والاستخارة","concept_gloss":"daha iyi olanı seçme","contextual_glosses":[{"applicability":"Bir kişiye iki şey arasında karar verme yetkisinin bırakıldığı veya bu yetkinin adlandırıldığı bağlamlara uyar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Daha iyi olanı arama, seçilmiş sonuç ve iyi sonucu dileme kullanımlarını dışarıda bırakır.","preserves":"Seçenekler arasında karar verebilme yetkisini korur."},"facet_ids":["F003"],"text":"seçim hakkı","usage_role":"contextual"},{"applicability":"İki olasılık arasından kişi için iyi olan sonucun Yaratıcı tarafından belirlenmesinin istendiği bağlama uyar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel seçme eylemini, seçim hakkını ve seçimde üstün gelmeyi kapsamaz.","preserves":"Kişi için daha iyi olanı isteme yönünü korur."},"facet_ids":["F002"],"text":"iyi sonucu dileme","usage_role":"explanatory"},{"applicability":"Bir kişinin seçim veya karşılaştırma bakımından diğerini geçtiğinin anlatıldığı özel bağlama uyar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Daha iyi olanı seçme, seçim hakkı ve iyi sonuç isteme alanlarını dışarıda bırakır.","preserves":"Seçim alanındaki üstünlük ilişkisini korur."},"facet_ids":["F003"],"text":"seçimde üstün gelme","usage_role":"contextual"}],"definition":"Birden çok olasılık arasından daha iyi görüleni arayıp ayırma, seçme veya seçim yetkisine sahip olma alanıdır. Belirli kullanımlarda iyi sonucu Yaratıcıdan dileme, seçim hakkını başkasına bırakma ya da seçimde üstün gelme anlamları bu çekirdeğe bağlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Olasılıklar arasından daha iyi görüleni arayıp ayırmayı, seçmeyi ve seçilmiş sonucu bildirir."},{"facet_id":"F002","role":"specialization","statement":"Kişi için iki olasılıktan daha iyi olanı Yaratıcıdan dileme ve iyi sonucun belirlenmesini isteme anlamını taşır."},{"facet_id":"F003","role":"associated_use","statement":"Seçim hakkını bir başkasına bırakma veya birini seçim bakımından üstün gelmiş sayma gibi ilişki biçimlerini kapsar."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Karar verememe ve tereddüt durumunu anlamın merkezine ekler.","collision":"İki seçenek arasında tartma bildiren komşu alanla karışır.","fit":"displacement","loses":"Daha iyi olanı belirleme, seçme ve seçim yetkisi çekirdeğini kaybeder.","preserves":"Birden çok olasılığın bulunduğunu dolaylı olarak korur."},"text":"kararsızlık"}],"identity_rationale":"Kaynak ifadesi daha iyi olanı arayıp seçme çekirdeğini; seçim hakkı, seçilmiş sonuç, iki seçenekten iyisini dileme, seçimi başkasına bırakma ve seçimde üstün gelme kullanımlarıyla birlikte verir. Dal çerçevesi bu çok parçalı fakat seçim merkezli alanı doğru tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"seçim veya seçim hakkı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"seçim, seçilmiş şey veya seçim sonucu"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"daha iyi olanı arayıp seçme"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"seçmek veya üstün tutmak"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"Yaratıcıdan kişi için iyi sonucu dilemek"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"Yaratıcının kişi için iyi olanı seçip vermesi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"iki şey arasında seçim hakkını ona bırakmak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"seçimde üstün gelmek veya diğerini geçmek"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"seçen ya da seçilmiş olan"}],"lexicalization_note":"Tanım yalın seçme çekirdeğiyle söz kalıplarına bağlı seçim hakkı, iyi sonuç dileme ve üstün gelme kullanımlarını ayrı yüzler olarak korur.","neighbor_coverage_note":"Bütün adaylar, aynı kökün diğer dalları da dahil olmak üzere değerlendirildi. Seçkin olanı ayırma, doğruyu arama, iki seçenek arasında tartma ve genel iyilik sınırları yayımlandı; geri kalanlar uzak süreç ortaklığı taşıdı veya hayvanı yuvasından çıkaran ayrı kullanımla yalnızca biçimsel olarak çakıştı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal seçim sürecinin ve yetkisinin daha geniş alanını kapsar; komşu dal seçkin bölümün ayrılıp yeğlenmesini merkez alır.","focus_only":"İyi sonucu dileme, seçim hakkını başkasına bırakma ve seçimde üstün gelme alanlarını da kapsar.","gloss":"seçme ile seçkin olanı ayırma","neighbor_only":"Bir topluluk veya nesne grubunun seçkin bölümünü ayırma ve onu özellikle yeğleme üzerinde yoğunlaşır.","neighbor_ref":"root_000873/B002","relation_type":"near_synonym","shared_zone":"İki dal da seçenekler arasından üstün görüleni ayırıp alma eyleminde buluşur."},{"boundary_match":"partial","distinction":"Odak dal seçimin yapılmasına ve sonucuna uzanır; komşu dal doğruyu araştırma ve ona yönelme aşamasında kalabilir.","focus_only":"Seçim yapmayı, seçim hakkını ve seçilmiş sonucu doğrudan kapsar.","gloss":"daha iyiyi seçme ile doğruyu arama","neighbor_only":"Doğruyu, en uygun yönü veya öncelikli olanı araştırıp ona yönelmeyi kararın önüne çıkarır.","neighbor_ref":"root_000314/B004","relation_type":"near_synonym","shared_zone":"Her ikisi de seçenekler içinde daha doğru veya daha iyi olana yönelmeyi içerir."},{"boundary_match":"partial","distinction":"Odak dal karşılaştırmayı seçimle sonuçlandırır; komşu dal seçenekleri tartmayı anlatır ve zorunlu olarak seçim bildirmez.","focus_only":"Daha iyi görüleni seçerek karara ve seçilmiş sonuca ulaşır.","gloss":"seçme ile iki seçenek arasında tartma","neighbor_only":"İki seçenek arasında hangisinin ağır bastığını tartma veya kararsız kalma sürecini bildirir.","neighbor_ref":"root_000991/B008","relation_type":"near_neighbor","shared_zone":"İki olasılığın karşılaştırılması her iki dalda da bulunabilir."},{"boundary_match":"partial","distinction":"Odak dal iyiliğe göre yapılan eylem ve karardır; komşu dal bu karara ölçü olabilen genel değerdir.","focus_only":"İyi sayılan seçenekler arasında arama, ayırma ve karar verme işlemini bildirir.","gloss":"iyiyi seçme ile iyilik","neighbor_only":"Herhangi bir seçim yapılmadan da var olan genel ve arzu edilen olumlu değeri bildirir.","neighbor_ref":"root_000452/B001","relation_type":"near_neighbor","shared_zone":"Seçimin ölçüsü, bir seçeneğin iyi ve arzu edilir sayılması olabilir."}],"source_phrase_ar":"الخيرة الخيار والاستخارة أن تسأل خير الأمرين لك ويقال خايرت فلانا فخرته وتقول اختر (maqayis)؛ خايرت فلانا فخرته والله يخير للعبد إذا استخاره وهذا وهذه وهؤلاء خيرتي وهو ما تختاره (ayn)؛ الخيار الاسم من الاختيار والخيرة من قولك خار الله لك والاختيار الاصطفياء والاستخارة الخيرة وخيرته بين الشيئين (sihah)؛ الاختيار طلب ما هو خير وفعله واستخار الله العبد فخار له وخايرت فلانا كذا فخرته (mufradat)","source_summary":"Kaynaklar daha iyi olanı arayıp seçme çekirdeğinde birleşir. Seçim hakkı ve seçilmiş şey, iyi sonucu Yaratıcıdan dileme, iki şey arasında yetki verme ve seçimde üstün gelme bu çekirdeğin farklı dilsel gerçekleşmeleridir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الخيار والاختيار والتخير والاستخارة وخار الله لك وخيرته بين شيئين، أي طلب ما هو خير، أو الاصطفاء، أو تفويض الخيار.","what_is_not_ar":"لا يدخل الخيار المعرب بمعنى القثاء، ولا الخيري المعرب، ولا خصوص استخراج الحيوان من جحره إلا في فرعه الخاص."},"support_links":["sup_9b9822cca3123cbbe210","sup_de16f7c0c8d9cb80ad47"]},{"boundary":"Çekirdek, sözcüğün malı adlandırmasıdır; çokluk ve övülen yoldan edinilme bazı kullanımların belirgin kısıtıdır, bütün mal kullanımlarına zorunlu şart yapılmaz.","branch_kind":"bare","branch_ref":"root_000452/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَيْر","morph_features":"STEM|POS:N|LEM:xayor|ROOT:xyr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:3:2","qac_word_ref":"100:8:3","surface_ar":"خَيْرِ"}],"gloss":"mal, özellikle çok veya övülen bir yoldan edinilmiş servet","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcük, kişinin sahip olduğu malı veya serveti adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bazı açıklamalarda kapsam, çok olan ve övülen bir yoldan edinilmiş mala daraltılır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Miras bırakma ve mala güçlü bağlılık bağlamları bu adlandırmanın örnekleridir."}}],"root_ar":"خ ي ر","root_id":"root_000452","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Malın doğrudan adlandırıldığı, özellikle çokluğu veya övülen bir yoldan edinilmiş oluşunun öne çıktığı kullanımları birlikte karşılar.","boundary_detail":"Çekirdek, sözcüğün malı adlandırmasıdır; çokluk ve övülen yoldan edinilme bazı kullanımların belirgin kısıtıdır, bütün mal kullanımlarına zorunlu şart yapılmaz.","branch_image_ar":"المال المسمى خيرا","concept_gloss":"mal, özellikle çok veya övülen bir yoldan edinilmiş servet","contextual_glosses":[{"applicability":"Sahip olunan veya miras bırakılan varlığın nicelik şartı açıkça öne çıkarılmadan adlandırıldığı bağlamlara uyar.","error_profile":{"adds":"Çokluk veya övülen edinme yolu şartı bulunan bağlamlarda bu şartları taşımayan malları da kapsayabilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Sahip olunan ekonomik varlık çekirdeğini korur."},"facet_ids":["F001","F003"],"text":"mal","usage_role":"general"},{"applicability":"Malın çokluğu ve değeri özellikle vurgulandığında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nicelik vurgusu bulunmayan genel mal ve tekil miras varlığı kullanımlarını dışarıda bırakabilir.","preserves":"Çok ve değerli mal yönünü açık biçimde korur."},"facet_ids":["F002"],"text":"servet","usage_role":"contextual"}],"definition":"Malı veya serveti adlandıran kullanımdır; bazı bağlamlarda özellikle çok ya da övülen bir yoldan edinilmiş malı belirtir. Miras bırakılan veya güçlü biçimde sevilen mal da bu adlandırmayla anılabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcük, kişinin sahip olduğu malı veya serveti adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Bazı açıklamalarda kapsam, çok olan ve övülen bir yoldan edinilmiş mala daraltılır."},{"facet_id":"F003","role":"example","statement":"Miras bırakma ve mala güçlü bağlılık bağlamları bu adlandırmanın örnekleridir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Soyut ahlaki değer anlamını merkeze taşır.","collision":"Aynı kökün genel olumlu değer dalıyla karışır.","fit":"displacement","loses":"Ekonomik varlık ve sahip olunan mal çekirdeğini ortadan kaldırır.","preserves":"Malın değerli veya övülen oluşunu çağrıştırabilir."},"text":"iyilik"}],"identity_rationale":"Kaynak ifadesi sözcüğün mal anlamında kullanılmasını açıkça destekler; ancak kapsam bir anlatımda genel malı gösterirken başka anlatımlarda çokluk ve övülen bir edinme yolu şartıyla daraltılır. Dal korunabilir, fakat bu değişken sınır tanımda açıkça belirtilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"mal, özellikle çok veya iyi yoldan edinilmiş servet"}],"lexicalization_note":"Tanım yalın sözcüğün malı adlandıran anlamına bağlıdır; genel iyilik veya cömertlik anlamları malın kendisiyle özdeşleştirilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Genel iyilik, cömertçe verme ve mal üzerinde işlem yapma karşılaştırmaları dal sınırını en açık biçimde gösterdi; çokluk, savurganlık, gecikme veya yön değiştirme gibi daha uzak bağlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir ekonomik varlık türünü adlandırır; komşu dal ise bu varlığın yalnızca bir örneği olabildiği genel olumlu değerdir.","focus_only":"Doğrudan sahip olunan malı ve serveti adlandırır.","gloss":"mal ile genel iyilik","neighbor_only":"Mal dışında da arzu edilen her türlü olumlu değeri ve iyiliği kapsar.","neighbor_ref":"root_000452/B001","relation_type":"near_neighbor","shared_zone":"Değerli veya yararlı mal genel iyilik düşüncesiyle ilişkilendirilebilir."},{"boundary_match":"partial","distinction":"Odak dal verilen ya da elde tutulan varlıktır; komşu dal o varlığı verme niteliği veya verme sonucudur.","focus_only":"Kişinin elinde bulunan malı, verilmemiş olsa bile kapsar.","gloss":"servet ile cömertçe verme","neighbor_only":"Verme niteliğini, armağanı ve kişideki cömertlik bolluğunu bildirir.","neighbor_ref":"root_000452/B005","relation_type":"near_neighbor","shared_zone":"Mal, armağan ve cömertlik eyleminin konusu olabilir."},{"boundary_match":"field_only","distinction":"Odak dal bir varlık adıdır; komşu dal bu varlık üzerinde gerçekleştirilen tüketme, harcama veya alma eylemidir.","focus_only":"Malın kendisini ve bazı kullanımlarda onun çokluk niteliğini adlandırır.","gloss":"mal ile malı tüketme veya alma","neighbor_only":"Malı tüketme, harcama, ele geçirme veya başkasının malından yararlanma eylemlerini bildirir.","neighbor_ref":"root_000043/B004","relation_type":"same_field","shared_zone":"Her iki dalın ortak katılımcısı ekonomik varlık olan maldır."}],"source_phrase_ar":"إن ترك خيرا أي مالا (sihah;mufradat)؛ لا يقال للمال خير حتى يكون كثيرا ومن مكان طيب (mufradat)؛ وإنه لحب الخير لشديد أي المال الكثير (mufradat)؛ ما كان مجموعا من المال من وجه محمود (mufradat)","source_summary":"Kullanım malı göstermekle birlikte açıklamaların bir bölümü kapsamı çokluk ve övülen bir edinme yolu şartıyla daraltır. Miras bırakılan veya güçlü biçimde sevilen mal da ortak claim içinde örneklenir.","sources":["SI","MU"],"what_is_ar":"يدخل فيه إطلاق الخير على المال، وبخاصة المال الكثير أو المجتمع من وجه محمود، وما يوصى به أو ينفق.","what_is_not_ar":"لا يدخل كل مال مطلقا عند من قيده بالكثرة أو بالوجه المحمود، ولا يدخل الخير الأخلاقي العام إلا بوصفه أصلا أوسع."},"support_links":[]},{"boundary":"Bu dal malın kendisini değil, cömertlik niteliğini ve onun armağan ya da verme biçimindeki sonucunu bildirir.","branch_kind":"bare","branch_ref":"root_000452/B005","candidate_links":[{"candidate_id":"cand_53710b73a4633474b3a4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَيْر","morph_features":"STEM|POS:N|LEM:xayor|ROOT:xyr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:3:2","qac_word_ref":"100:8:3","surface_ar":"خَيْرِ"}],"gloss":"cömertlik ve armağan verme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişide bulunan cömertlik ve bolca verme niteliğini bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Cömertliğin somut sonucu olan armağanı, bağışı veya verme eylemini gösterebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişide iyiliğin çok olması, onun cömert ve yararlı oluşunun göstergesi olarak kullanılır."}}],"root_ar":"خ ي ر","root_id":"root_000452","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem kişideki verme niteliğini hem de bu niteliğin armağan veya bağış olarak gerçekleşmesini kapsayan genel karşılıktır.","boundary_detail":"Bu dal malın kendisini değil, cömertlik niteliğini ve onun armağan ya da verme biçimindeki sonucunu bildirir.","branch_image_ar":"الكرم والهبة","concept_gloss":"cömertlik ve armağan verme","contextual_glosses":[{"applicability":"Bir kişinin bolca veren ve iyiliği çok olan niteliğinin öne çıktığı bağlamlara uyar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir armağanı veya somut verme sonucunu doğrudan adlandırmaz.","preserves":"Kişideki verme isteği ve iyilik bolluğu niteliğini korur."},"facet_ids":["F001","F003"],"text":"cömertlik","usage_role":"general"},{"applicability":"Cömertliğin somut olarak verilen bir şey biçiminde gerçekleştiği bağlamlara uyar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin sürekli cömertlik niteliğini ve genel iyilik bolluğunu kapsamaz.","preserves":"Verme sonucunda alıcıya ulaşan somut yararı korur."},"facet_ids":["F002"],"text":"armağan","usage_role":"contextual"}],"definition":"Cömert olma niteliği ve bunun armağan ya da verme olarak görünmesidir; kişi için kullanıldığında onda iyiliğin ve verme isteğinin bol bulunduğunu da bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişide bulunan cömertlik ve bolca verme niteliğini bildirir."},{"facet_id":"F002","role":"extension","statement":"Cömertliğin somut sonucu olan armağanı, bağışı veya verme eylemini gösterebilir."},{"facet_id":"F003","role":"associated_use","statement":"Bir kişide iyiliğin çok olması, onun cömert ve yararlı oluşunun göstergesi olarak kullanılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Elde tutulan ekonomik varlığı anlamın merkezine ekler.","collision":"Aynı kökün mal ve servet dalıyla karışır.","fit":"displacement","loses":"Cömertlik niteliğini, verme eylemini ve armağan sonucunu kaybeder.","preserves":"Verilebilecek malın bolluğunu dolaylı biçimde çağrıştırır."},"text":"servet"}],"identity_rationale":"Kaynak ifadesi cömertlik niteliğini, armağanı ve vermeyi aynı dalda birleştirir; ayrıca kişide iyiliğin çok oluşunu bu niteliğin göstergesi sayar. Verilen dal çerçevesi, sahip olunan maldan farklı olarak verme ve bolluk yönünü doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"cömertlik, armağan ve verme"}],"lexicalization_note":"Tanım yalın cömertlik ve armağan alanıyla sınırlıdır; yalnızca belirli bir nesneye sahip olma durumu veya genel iyilik bütünü buraya taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Cömertçe verme, bol bağış, karşılıksız iyilik, esirgeme karşıtlığı ve malın kendisiyle ayrım yayımlandı; yalnızca genel değer, kişisel üstünlük veya uzak bolluk çağrışımı taşıyan adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal nitelik ile armağan sonucunu birlikte kapsar; komşu dal verme davranışının sürekliliğini ve bolluğunu daha belirgin işler.","focus_only":"Armağanın kendisini ve kişide genel iyiliğin çok oluşunu da adlandırabilir.","gloss":"cömertlik ve bolca verme","neighbor_only":"El açıklığını ve arkadaş çevresine bolca verme davranışını daha eylemli biçimde öne çıkarır.","neighbor_ref":"root_001487/B008","relation_type":"near_synonym","shared_zone":"İki dal da cömertlik, armağan, yararlı davranış ve bolca verme alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal armağan ve genel iyilik bolluğuna uzanır; komşu dal çeşitli değerleri bolca bağışlama davranışını daha açık sınırlar.","focus_only":"Armağanı ve kişide iyiliğin bol oluşunu bağımsız anlamlar olarak da kapsar.","gloss":"cömertlik ile bol bağış","neighbor_only":"Malın yanı sıra bilginin de bolca verilmesini ve bağışta geniş davranmayı açıkça kapsar.","neighbor_ref":"root_000274/B001","relation_type":"near_synonym","shared_zone":"Her ikisi de eli açıklık ve elindekini başkasına verme niteliğini anlatır."},{"boundary_match":"partial","distinction":"Odak dal genel cömertlik ve armağandır; komşu dal verilmesi zorunlu olmayan fazladan iyiliği ve karşılıksız yararı özellikle belirtir.","focus_only":"Cömertliği kişinin niteliği ve armağanı doğrudan adlandıracak biçimde kapsar.","gloss":"cömertlik ile karşılıksız iyilik","neighbor_only":"Hak edilmiş bir borç olmadan fazladan iyilikte bulunma ve lütufta bulunma koşulunu öne çıkarır.","neighbor_ref":"root_001163/B003","relation_type":"near_synonym","shared_zone":"Armağan verme ve başkasına yarar sağlama iki dalın ortak alanıdır."},{"boundary_match":"opposed","distinction":"Odak dal verme yönündeki olumlu kutuptur; komşu dal aynı eksende vermeme ve engelleme yönündeki karşıt kutuptur.","focus_only":"Elindekini verme, armağan etme ve cömert davranma yönünü taşır.","gloss":"verme ile esirgeme","neighbor_only":"Vermeyi engelleme, eli sıkı davranma ve iyiliği esirgeme yönünü taşır.","neighbor_ref":"root_001448/B001","relation_type":"antonym","shared_zone":"İki dal, kişinin elindeki yararı başkasına verip vermemesi ekseninde karşılaşır."}],"source_phrase_ar":"والخير الكرم (maqayis)؛ الخير الهبة (ayn)؛ رجل ذو خير إذا كان كثير الخير (jamhara)؛ الخير بالكسر الكرم (sihah)","source_summary":"Kaynaklar cömertlik, armağan ve verme anlamlarını ortak bir alanda toplar. Bir kişide iyiliğin çok olduğunun söylenmesi de cömertlik ve yarar bolluğunun kişiye yüklenen niteliğidir.","sources":["MQ","AY","JA","SI"],"what_is_ar":"يدخل فيه الخير بمعنى الكرم، والهبة والعطاء، وكثرة الخير في الشخص.","what_is_not_ar":"لا يدخل المال المملوك بمجرده إلا إذا نظر إليه من جهة العطاء والكرم."},"support_links":["sup_1e619313e930c2a0d7fe"]},{"boundary":"Bu anlam yalnızca hayvan, yuva, bir geçidin engellenmesi ve başka çıkıştan çıkma bileşenlerini taşıyan özel kullanıma aittir; iyi olanı seçme anlamına genellenmez.","branch_kind":"collocation","branch_ref":"root_000452/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَيْر","morph_features":"STEM|POS:N|LEM:xayor|ROOT:xyr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:3:2","qac_word_ref":"100:8:3","surface_ar":"خَيْرِ"}],"gloss":"bir geçidi tıkayıp hayvanı yuvasından çıkarma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hayvanın yuvasındaki bir geçide engel yerleştirerek onu başka bir çıkışa yöneltme işlemini bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İşlemin katılımcısı sırtlan veya çöl sıçanı, aracı ise geçidi tıkayan çubuk ya da benzeri bir engeldir."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir yuva geçidinin engellenmesi sonucunda hayvanın öteki geçitten çıkması işlemin kurucu sonucudur."}}],"root_ar":"خ ي ر","root_id":"root_000452","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sırtlan veya çöl sıçanının yuvasındaki bir yolun engellenip hayvanın başka çıkıştan çıkarıldığı özel işlemi tam olarak karşılar.","boundary_detail":"Bu anlam yalnızca hayvan, yuva, bir geçidin engellenmesi ve başka çıkıştan çıkma bileşenlerini taşıyan özel kullanıma aittir; iyi olanı seçme anlamına genellenmez.","branch_image_ar":"استدراج الحيوان من جحره","concept_gloss":"bir geçidi tıkayıp hayvanı yuvasından çıkarma","contextual_glosses":[{"applicability":"Yuvadaki bir geçidin kapatılmasıyla hayvanın alternatif çıkışa yöneltildiği anlatımda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çubuk veya benzeri engelin belirli bir yuva geçidine yerleştirilmesi aşamasını açıkça söylemez.","preserves":"Hayvanın başka bir çıkışa yöneltilmesi ve dışarı çıkarılması sonucunu korur."},"facet_ids":["F001","F003"],"text":"hayvanı öteki çıkışa sürme","usage_role":"explanatory"}],"definition":"Sırtlanı veya çöl sıçanını yuvasındaki bir geçide çubuk ya da başka bir engel koyarak başka bir çıkıştan dışarı çıkarmaktır. İşlem, bir yolu kapatma ile hayvanın alternatif yola yönelmesi sırasını zorunlu olarak içerir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hayvanın yuvasındaki bir geçide engel yerleştirerek onu başka bir çıkışa yöneltme işlemini bildirir."},{"facet_id":"F002","role":"specialization","statement":"İşlemin katılımcısı sırtlan veya çöl sıçanı, aracı ise geçidi tıkayan çubuk ya da benzeri bir engeldir."},{"facet_id":"F003","role":"core","statement":"Bir yuva geçidinin engellenmesi sonucunda hayvanın öteki geçitten çıkması işlemin kurucu sonucudur."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"İki olasılık arasından iyi olanı isteme düşüncesini ekler.","collision":"Aynı kökün seçme ve iyi sonucu isteme dalıyla karışır.","fit":"displacement","loses":"Hayvanı, yuvayı, engel koymayı ve başka çıkıştan çıkarmayı bütünüyle kaybeder.","preserves":"Aynı kökteki başka bir kullanımın çağrışımını taşır."},"text":"iyi sonucu dileme"}],"identity_rationale":"Kaynak ifadesi, sırtlan veya çöl sıçanının yuvasındaki bir geçide çubuk ya da engel yerleştirip hayvanı başka bir çıkıştan çıkarmayı açık bir işlem dizisiyle anlatır. Verilen çerçeve hem aracı hem yer değişimini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"sırtlanı, yuvasının bir geçidini tıkayarak başka çıkıştan çıkarma"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"çöl sıçanını, yuvasının bir geçidini tıkayarak başka çıkıştan çıkarma"}],"lexicalization_note":"Tanım yalnızca sırtlan veya çöl sıçanıyla kurulan özel kullanıma bağlıdır; bu işlem yalın kökün genel anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar ve aynı kökün diğer dalları değerlendirildi. Çıkış geçidi, yuva içindeki hayvan hareketi, genel avlanma ve yuvanın kendisiyle kurulan sınırlar yayımlandı; tuzak, hayvan adı veya toprağa gizlenme gibi yalnızca sahneyi paylaşan adaylar elendi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal geçit üzerinde yapılan bir işlem ve bunun sonucudur; komşu dal işlemin gerçekleştiği geçidin kendisini adlandırır.","focus_only":"Yuvanın bir geçidini engelleyerek hayvanın hareketini ve çıkışını yönlendirir.","gloss":"hayvanı çıkarmak ile çıkış geçidi","neighbor_only":"İki ucu bulunan geçidi ve çöl sıçanının kullandığı giriş çıkış yolunu adlandırır.","neighbor_ref":"root_001537/B003","relation_type":"near_neighbor","shared_zone":"İki dal da çöl sıçanının yer altı yuvası ve alternatif çıkış düzeniyle ilgilidir."},{"boundary_match":"field_only","distinction":"Odak dal dışarı çıkarma amacı taşıyan insan müdahalesidir; komşu dal hayvanın boynunu sokma veya çıkarma biçimindeki hareketidir.","focus_only":"Bir geçidi tıkayarak hayvanı başka çıkıştan bütünüyle dışarı yöneltir.","gloss":"yuvadan çıkarma ile boyun hareketi","neighbor_only":"Hayvanın boynunu çamura veya yuva toprağına sokması ya da oradan çıkarması hareketini anlatır.","neighbor_ref":"root_001053/B007","relation_type":"same_field","shared_zone":"Her iki dal hayvanın toprak veya yuva içindeki yönlendirilmiş hareketini konu alır."},{"boundary_match":"thematic_only","distinction":"Odak dal tek ve ayrıntılı bir çıkarma tekniğidir; komşu dal çok sayıda yöntem ve aracı kapsayan genel avlanma etkinliğidir.","focus_only":"Belirli yuva düzeninde bir geçidi kapatıp hayvanı başka çıkıştan çıkarma yöntemini bildirir.","gloss":"yuvadan çıkarma yöntemi ile avlanma","neighbor_only":"Sahipsiz ve yakalanması güç hayvanı arama, yakalama, araç kullanma ve avlanma alanının tamamını kapsar.","neighbor_ref":"root_000896/B001","relation_type":"thematic","shared_zone":"Hayvanı saklandığı yerden çıkarma işlemi daha geniş bir avlanma senaryosunda kullanılabilir."},{"boundary_match":"field_only","distinction":"Odak dal yuvada gerçekleştirilen yönlendirme işlemidir; komşu dal bu işlemin mekânı olan yuva yapısı veya toprağıdır.","focus_only":"Yuvaya engel koyup içindeki hayvanı alternatif çıkışa sevk eden eylemi anlatır.","gloss":"yuva üzerinde işlem ile yuvanın kendisi","neighbor_only":"Çöl sıçanının yuvasını veya yuva ağzına yığdığı toprağı adlandırır.","neighbor_ref":"root_000605/B003","relation_type":"same_field","shared_zone":"İki dal da çöl sıçanının yuvasını ve yuva ağzını ortak sahne olarak paylaşır."}],"source_phrase_ar":"استخاره الضبع وهو أن تجعل خشبة في ثقبة بيتها حتى تخرج من مكان إلى آخر (maqayis)؛ يستخير الضبع واليربوع إذا جعل في موضع النافقاء فخرج من القاصعاء (ayn)","source_summary":"Kaynakların ortak anlatımı, sırtlan veya çöl sıçanının yuvasındaki bir geçidin çubuk ya da engelle kapatılması ve hayvanın bunun sonucunda başka bir çıkıştan dışarı çıkmasıdır.","sources":["MQ","AY"],"what_is_ar":"يدخل فيه استخارة الضبع أو اليربوع بجعل خشبة أو نحوها في موضع من جحره حتى يخرج من موضع آخر.","what_is_not_ar":"لا يدخل طلب الخير في الأمرين إلا من جهة اللفظ المشترك والاستخارة العامة."},"support_links":[]},{"boundary":"Somut bağlama çekirdeği, yalnız belirli söz öbeklerinde görülen destek ve yönetim güçlendirme kullanımlarıyla karıştırılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000782/B001","candidate_links":[{"candidate_id":"cand_f5c5c8be459cd50c8e1f","lane":"micro"},{"candidate_id":"cand_eb5f6311162b51421299","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَدِيد","morph_features":"STEM|POS:N|LEM:$adiyd|ROOT:$dd|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:4:2","qac_word_ref":"100:8:4","surface_ar":"شَدِيدٌ"}],"gloss":"bağlayıp sağlamlaştırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesne bağlanır, düğümü sıkılır ve bağlantısı sağlamlaştırılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birinin gücüne destek olmak, onun dayanma ve iş görme gücünü artırmak olarak anlatılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir yönetimin gücü ve sağlamlığı artırılır."}}],"root_ar":"ش د د","root_id":"root_000782","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin bağlanıp düğümünün sıkı ve güvenilir duruma getirildiği temel kullanım için uygundur.","boundary_detail":"Somut bağlama çekirdeği, yalnız belirli söz öbeklerinde görülen destek ve yönetim güçlendirme kullanımlarıyla karıştırılmaz.","branch_image_ar":"شد العقد والوثاق","concept_gloss":"bağlayıp sağlamlaştırma","contextual_glosses":[{"applicability":"Bir kişiye destek vererek onun gücünü artıran söz öbeğine bağlı kullanımda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dışarıdan verilen desteği ve bunun kişide doğurduğu güç artışını korur."},"facet_ids":["F002"],"text":"gücüne güç katmak","usage_role":"contextual"},{"applicability":"Bir yönetimin gücünü ve dayanıklılığını artırmayı anlatan sınırlı kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yönetim alanındaki güç ve sağlamlık artışını açık biçimde korur."},"facet_ids":["F003"],"text":"yönetimi güçlendirmek","usage_role":"contextual"}],"definition":"Bir şeyi bağlamak, düğümünü sıkılaştırmak ve çözülmeyecek kadar sağlam duruma getirmektir. Belirli söz öbeklerinde bu işlem, birine destek verip gücünü artırma ya da bir yönetimi sağlamlaştırma yönünde genişler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesne bağlanır, düğümü sıkılır ve bağlantısı sağlamlaştırılır."},{"facet_id":"F002","role":"specialization","statement":"Birinin gücüne destek olmak, onun dayanma ve iş görme gücünü artırmak olarak anlatılır."},{"facet_id":"F003","role":"extension","statement":"Bir yönetimin gücü ve sağlamlığı artırılır."}],"identity_rationale":"Kaynak ifadesi, bir şeyi bağlayıp düğümünü sağlamlaştırmayı temel anlam olarak verir; birinin gücünü destekleme ve yönetimi güçlendirme kullanımlarını da açıkça buna bağlar. Bu nedenle dal kimliği kanıtla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi bağlayıp sağlamlaştırmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"gücüne güç katmak, desteklemek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"Tanrı onun yönetimini güçlendirsin"}],"lexicalization_note":"Nesneyi bağlayıp sağlamlaştıran temel kullanım ile söz öbeğine bağlı destek ve yönetim güçlendirme kullanımları ayrı tutulur.","neighbor_coverage_note":"Listelenen bütün komşular karşılaştırıldı; yayımlanan üçü bağlama, sağlamlaştırma ve destek sınırlarını en açık biçimde gösterirken diğerleri yalnız uzak alan ortaklığı kuruyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bağlama işleminin sağlamlaştırıcı yönünü ve bundan gelişen güç verme kullanımlarını öne çıkarır; komşu dal ise bağlama eylemi yanında bağın aracını, yerini ve kimi sonuçlarını adlandırır.","focus_only":"Düğümü güçlendirme ile kişiye destek ve yönetime güç verme uzantıları bulunur.","gloss":"bağlama ve sağlamlaştırma","neighbor_only":"Bağ, ip, bağlama yeri ve kesilmiş tuzak gibi araç, yer ve sonuç adları da kapsanır.","neighbor_ref":"root_000535/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir şeyi bağlama ve bağlı duruma getirme çekirdeği vardır."},{"boundary_match":"partial","distinction":"Odak dal daha genel bir bağlama ve sağlamlaştırma işlemini kapsar; komşu dal giysi, kuşak, çevrili alan ve düğüm gibi daha belirli bağlama alanlarında yoğunlaşır.","focus_only":"Genel nesne bağlama ile kişiyi veya yönetimi güçlendiren uzantılar vardır.","gloss":"sıkıca bağlama","neighbor_only":"Giysi, kuşak, çevrili alan ve belirli düğüm türleriyle sınırlı örnekler öne çıkar.","neighbor_ref":"root_000290/B003","relation_type":"near_synonym","shared_zone":"İki dal da bağı sıkılaştırıp çözülmeye karşı sağlam kılmayı anlatır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği bağlayıp sağlamlaştırmaktır ve destek anlamı buna bağlıdır; komşu dalın çekirdeği ise dayanma, dayandırma ve dayanak ilişkisi kurmadır.","focus_only":"Somut bağlama, düğümü sıkma ve yönetimi güçlendirme anlamları bulunur.","gloss":"destekleyip güçlendirme","neighbor_only":"Bir şeye yaslanma, onu dayanak edinme ve bir şeyi başka bir şeye dayandırma anlamları bulunur.","neighbor_ref":"root_000747/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir varlığın başka bir destek sayesinde daha sağlam durması söz konusudur."}],"source_phrase_ar":"شددت العقد شدا (maqayis)؛ شد الحبل أو غيره (jamhara)؛ شده أي أوثقه (sihah)؛ شددت الشيء إذا أوثقته (tahdhib)؛ الشد العقد القوي وقويت عقده (mufradat)؛ شد عضده أي قواه (sihah)؛ شد الله ملكه وشدده أي قواه (sihah)؛ اشدد به أزرى (tahdhib)","source_summary":"Kaynakların ortak çizgisi, bağlama ve düğümü sağlamlaştırma işlemidir. Destek verilen kişinin gücünü ve bir yönetimin dayanıklılığını artıran kullanımlar bu somut çekirdeğin genişlemeleri olarak sunulur.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"عقد الشيء وإيثاقه وتقوية عقده وتقوية العضد والملك","what_is_not_ar":"الشدة في البدن والحال؛ الحملة والعدو؛ بلوغ الأشد؛ البخل"},"support_links":["sup_8db776420fd3a411d98e","sup_de16f7c0c8d9cb80ad47"]},{"boundary":"Temel güç ve katılık niteliği, çetin durumlar ile belirli yapılardaki artırma, güç yetirme ve çaba anlamlarından ayrılır.","branch_kind":"mixed_non_bare","branch_ref":"root_000782/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَدِيد","morph_features":"STEM|POS:N|LEM:$adiyd|ROOT:$dd|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:4:2","qac_word_ref":"100:8:4","surface_ar":"شَدِيدٌ"}],"gloss":"güç, katılık ve çetinlik","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir beden, nesne ya da kişi güçlü, katı, dayanıklı, yürekli ve sarsılmaz olarak nitelenir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir zaman, açlık ya da eziyet ağır ve katlanılması güç bir durum olarak anlatılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bir ad, hafifletmenin karşıtı olan artırma ve ağırlaştırma işlemini bildirir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Karşıt iki eylemi yapamama kalıbı, kişinin hiçbir şeye gücünün yetmediğini bildirir."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Şarkı söyleyen kişinin sesini yükseltirken bütün gücünü harcaması anlatılır."}},{"facet_id":"F006","role":"associated_use","source_fields":["distinctive_facets[F006]"],"statements":{"statement":"Bir kişinin ya da topluluğun güçlü bir bineğe veya güçlü binekler topluluğuna sahip olması anlatılır."}}],"root_ar":"ش د د","root_id":"root_000782","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın varlıklardaki güç ve katılık çekirdeğiyle durumların ağır ve çetin oluşunu birlikte anlatmak gerektiğinde uygundur.","boundary_detail":"Temel güç ve katılık niteliği, çetin durumlar ile belirli yapılardaki artırma, güç yetirme ve çaba anlamlarından ayrılır.","branch_image_ar":"شدة القوة والصلابة","concept_gloss":"güç, katılık ve çetinlik","contextual_glosses":[{"applicability":"Bir kişinin, bedenin, hayvanın ya da nesnenin güç ve sağlamlık niteliği öne çıktığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Güç, sağlamlık ve dayanıklılık niteliklerini doğal bir sıfat öbeğiyle korur."},"facet_ids":["F001"],"text":"güçlü ve dayanıklı","usage_role":"contextual"},{"applicability":"Zamanın, açlığın, eziyetin ya da başka bir yaşantının katlanılması güç oluşu anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Durumun ağırlığını ve kişiyi zorlayan çetinliğini birlikte korur."},"facet_ids":["F002"],"text":"ağır ve çetin durum","usage_role":"contextual"},{"applicability":"Hafifletmenin karşıtı olarak bir niteliğin derecesini yükseltme anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dereceyi yükseltme işlemini ve bunun hafifletmeye karşıt yönünü korur."},"facet_ids":["F003"],"text":"artırıp ağırlaştırma","usage_role":"contextual"}],"definition":"Bir varlıkta bedensel güç, katılık, dayanıklılık ya da yürek sağlamlığı olarak görülen yüksek yoğunluk; durumlarda ise çetinlik, kıtlık ve eziyetin ağırlığıdır. Aynı kökten gelen sınırlı yapılarda bir şeyi hafifletmenin karşıtı olarak artırma, bir işe gücü yetme ya da yetmeme, bütün gücünü harcama ve güçlü bir bineğe sahip olma anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir beden, nesne ya da kişi güçlü, katı, dayanıklı, yürekli ve sarsılmaz olarak nitelenir."},{"facet_id":"F002","role":"extension","statement":"Bir zaman, açlık ya da eziyet ağır ve katlanılması güç bir durum olarak anlatılır."},{"facet_id":"F003","role":"specialization","statement":"Belirli bir ad, hafifletmenin karşıtı olan artırma ve ağırlaştırma işlemini bildirir."},{"facet_id":"F004","role":"associated_use","statement":"Karşıt iki eylemi yapamama kalıbı, kişinin hiçbir şeye gücünün yetmediğini bildirir."},{"facet_id":"F005","role":"associated_use","statement":"Şarkı söyleyen kişinin sesini yükseltirken bütün gücünü harcaması anlatılır."},{"facet_id":"F006","role":"associated_use","statement":"Bir kişinin ya da topluluğun güçlü bir bineğe veya güçlü binekler topluluğuna sahip olması anlatılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bedensel güç, yüreklilik, dayanıklılık ve ağır durumlara ilişkin çetinlik anlamlarını dışarıda bırakır.","preserves":"Nesnelerdeki katılık ve kolay biçim değiştirmeme yönünü korur."},"text":"sertlik"}],"identity_rationale":"Kaynak ifadesi güç, katılık, yüreklilik ve dayanıklılığı dalın çekirdeği olarak destekler; çetin zaman, kıtlık, eziyet, artırma, güç yetirme ve çaba harcama kullanımlarını da ayrıca verir. Dal korunabilir, ancak bu yapıya bağlı kullanımlar yalın güç anlamıyla özdeşleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"güç, katılık, dayanıklılık ve çetinlik"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"güçlü ve yürekli"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"ağır sıkıntı, çetin sınanma"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"büyük sarsıntılar ve ağır sıkıntılar"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"artırma ve ağırlaştırma"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"bir konuda çok sıkı davranma"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"hiçbir şeye gücü yetmemek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"şarkı söylerken sesini yükseltmek için var gücünü kullanmak"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"güçlü bir bineğe sahip olmak"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"güçlü ve sert"}],"lexicalization_note":"Genel güç, katılık ve çetinlik anlamları ile yalnız belirli biçim ve söz öbeklerinde görülen artırma, güç yetirme ve çaba kullanımları ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen dört komşu güç, katılık, dayanıklılık ve durum zorluğu sınırlarını gösteriyor, kalanlar ise yalnız dar örnek veya uzak alan ortaklığı sunuyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal gücü kişilik, ağır yaşantı ve derece artırma alanlarına genişletir; komşu dal ise yumuşaklığın karşıtı olan sertliği nesne, yer ve başka somut görünümler üzerinden daha geniş işler.","focus_only":"Yüreklilik, ağır zaman, açlık, eziyet, artırma ve güç yetirme kullanımları bulunur.","gloss":"güç ve katılık","neighbor_only":"Yumuşaklığın karşıtı olma, sert yer ve taş, kuruma, koşu ve kişisel sıkılaşma gibi alanlar bulunur.","neighbor_ref":"root_000875/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da güç, katılık, sağlamlık ve kolay eğilip bozulmama niteliklerini anlatır."},{"boundary_match":"partial","distinction":"Odak dal güç niteliğini ruhsal sağlamlığa ve ağır durumlara taşır; komşu dal güç ve katılığı süreklilik, hayvan ve kumaş gibi özel alanlarla sınırlar.","focus_only":"Yüreklilik, çetin zaman, eziyet ve hafifletmenin karşıtı olan artırma anlamları bulunur.","gloss":"güçlü ve sağlam olma","neighbor_only":"Süreklilik, hayvanın semizliği ve kumaşın dayanıklılığı gibi özel uygulamalar bulunur.","neighbor_ref":"root_000973/B007","relation_type":"near_synonym","shared_zone":"İki dalda da bir varlığın güçlü, katı ve dayanıklı olması temel ortak alandır."},{"boundary_match":"partial","distinction":"Odak dalda güç ve katılık doğrudan bir nitelik ve durum yoğunluğu olarak verilir; komşu dalda bu nitelik sınanarak ortaya çıkan dayanıklılık çerçevesindedir.","focus_only":"Genel güç ve katılık yanında yüreklilik, ağır yaşantı ve artırma kullanımları vardır.","gloss":"dayanıklı ve sağlam","neighbor_only":"Gücün özellikle sınama sonucunda ortaya çıkması ve belirli insan, hayvan ya da nesne türlerinde görülmesi öne çıkar.","neighbor_ref":"root_000988/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal bir kişinin, hayvanın veya nesnenin güçlü ve sağlam oluşunu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalın çetinlik anlamı daha geniş güç ve yoğunluk alanının bir uzantısıdır; komşu dalın çekirdeği doğrudan kolaylığın karşıtı olan zorluktur.","focus_only":"Bedensel güç, katılık, yüreklilik ve derece artırma anlamları bulunur.","gloss":"çetinlik","neighbor_only":"Kolaylığın karşıtı olarak işin yapılmasını güçleştiren zorluk çekirdeği bulunur.","neighbor_ref":"root_001012/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir zamanın ya da durumun ağır, zor ve katlanılması güç oluşunda buluşur."}],"source_phrase_ar":"أصل واحد يدل على قوة في الشيء (maqayis)؛ الشدة الصلابة والنجدة وثبات القلب والمجاعة (ayn;tahdhib)؛ الشدة القوة في الجسم وصعوبة الزمن (jamhara)؛ الشدة القوة والجلادة والشديد الرجل القوي (tahdhib)؛ الشدة تستعمل في العقد وفي البدن وفي قوى النفس وفي العذاب (mufradat)؛ أصابتني شدى أي شدة (maqayis;sihah;tahdhib)؛ التشديد خلاف التخفيف (sihah)؛ ما أملك شدا ولا إرخاء لا أقدر على شيء (tahdhib)؛ تشددت القينة إذا جهدت نفسها (tahdhib)؛ كانت دوابهم شدادا وأشد الرجل إذا كانت معه دابة شديدة (maqayis;sihah)","source_summary":"Ortak çekirdek, bedende, nesnede veya kişilikte güç, katılık ve dayanıklılıktır; ağır zaman, açlık ve eziyet bu yoğunluğun durumlara uzanmasıdır. Ayrıca hafifletmenin karşıtı olan artırma, güç yetirememeyi bildiren kalıp, var gücüyle ses çıkarma ve güçlü bineğe sahip olma gibi sınırlı kullanımlar aktarılır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"القوة والصلابة والشجاعة وثبات القلب وشدة الحال والجوع والعذاب والتشديد وبذل الجهد والقدرة","what_is_not_ar":"عقد الشيء وإيثاقه؛ الحملة والعدو؛ بلوغ الأشد؛ ارتفاع النهار؛ البخل"},"support_links":[]},{"boundary":"Düşmana saldırma belirli yapıya bağlıdır; koşma ve hızlı ilerleme biçimleriyle aynı kapsamda eritilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000782/B003","candidate_links":[{"candidate_id":"cand_69eb74cb192c7f238c85","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَدِيد","morph_features":"STEM|POS:N|LEM:$adiyd|ROOT:$dd|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:4:2","qac_word_ref":"100:8:4","surface_ar":"شَدِيدٌ"}],"gloss":"saldırıya atılma ve hızla koşma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Savaşta düşmana doğru atılınır ve onun üzerine saldırılır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı biçimler koşmayı, hızlı koşuyu veya hızla ilerlemeyi bildirir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir saldırı tek bir hamle olarak sayılabilir veya birçok saldırı ardı ardına yapılabilir."}}],"root_ar":"ش د د","root_id":"root_000782","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın savaşta düşmana saldırma çekirdeğiyle ayrı biçimlerdeki koşma anlamını birlikte göstermek gerektiğinde uygundur.","boundary_detail":"Düşmana saldırma belirli yapıya bağlıdır; koşma ve hızlı ilerleme biçimleriyle aynı kapsamda eritilmez.","branch_image_ar":"شد الحملة والعدو","concept_gloss":"saldırıya atılma ve hızla koşma","contextual_glosses":[{"applicability":"Savaşta bir düşmana doğru atılıp doğrudan saldırma anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Savaş bağlamını, düşmana yönelmeyi ve saldırı eylemini eksiksiz korur."},"facet_ids":["F001"],"text":"düşmanın üzerine saldırmak","usage_role":"contextual"},{"applicability":"Savaş yapısından bağımsız olarak koşma ya da hızlı ilerleme bildiren biçimlerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Koşma eylemini ve hareketin hızlı oluşunu açık biçimde korur."},"facet_ids":["F002"],"text":"hızla koşmak","usage_role":"contextual"},{"applicability":"Savaşta yapılan saldırının bir kez gerçekleşen sayılabilir bir hamle olduğu bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Saldırı olayını ve bunun tek bir kez gerçekleştiği ayrımını korur."},"facet_ids":["F003"],"text":"tek saldırı hamlesi","usage_role":"explanatory"}],"definition":"Savaşta düşmana doğru hızla atılıp üzerine saldırmaktır; ayrı biçimlerde koşma ya da hızla ilerleme de anlatılır. Saldırının tek bir hamle oluşu veya birçok kez yinelenmesi ayrıca belirtilebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Savaşta düşmana doğru atılınır ve onun üzerine saldırılır."},{"facet_id":"F002","role":"source_variant","statement":"Ayrı biçimler koşmayı, hızlı koşuyu veya hızla ilerlemeyi bildirir."},{"facet_id":"F003","role":"specialization","statement":"Bir saldırı tek bir hamle olarak sayılabilir veya birçok saldırı ardı ardına yapılabilir."}],"identity_rationale":"Kaynak ifadesi savaşta düşmanın üzerine atılıp saldırmayı, koşmayı ve hızla ilerlemeyi açıkça birlikte aktarır; tek saldırı ile yinelenen saldırıların biçimsel ayrımını da gösterir. Dal kimliği bu çok parçalı kanıtla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"düşmanın üzerine saldırmak"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"koşma, hızlı koşu"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"koşmak, hızla ilerlemek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"tek bir saldırı hamlesi"}],"lexicalization_note":"Düşmanın üzerine saldırmayı bildiren söz öbeği, koşma ve hızlı ilerleme bildiren biçimlerden ve tek saldırı adından ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar gözden geçirildi; seçilen dört komşu saldırı, yenilgi sonucu, savaş topluluğu ve hızlı koşu niteliği arasındaki ayrımları gösteriyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal düşmana saldırma eylemini ve onun hareket yönünü anlatır, ancak yenilgi sonucunu gerektirmez; komşu dal saldırının karşı tarafı yenmesiyle tanımlanır.","focus_only":"Saldırı eylemi sonuçtan bağımsızdır; ayrıca koşma ve saldırının tek ya da yinelenmiş oluşu anlatılır.","gloss":"saldırı hamlesi","neighbor_only":"Tek bir güçlü saldırıyla karşı tarafı yenme sonucu zorunlu olarak bulunur.","neighbor_ref":"root_000003/B007","relation_type":"near_neighbor","shared_zone":"Her iki dal savaşta karşı tarafa doğru yapılan güçlü ve doğrudan bir saldırı hamlesini içerir."},{"boundary_match":"partial","distinction":"Odak dal tek yönlü saldırı hamlesi ve koşma üzerinde durur; komşu dal atlılar arasındaki karşılıklı kovalamayı ve yanıltıcı geri çekilme düzenini kapsar.","focus_only":"Doğrudan düşmana atılma yanında genel koşma ve tek saldırı hamlesi anlamları vardır.","gloss":"savaşta üzerine atılma","neighbor_only":"Atlıların birbirini kovalaması, karşılıklı saldırması ve savaş oyunu için geri çekilmesi vardır.","neighbor_ref":"root_000930/B003","relation_type":"near_neighbor","shared_zone":"İki dal savaşta karşı tarafa yönelen hızlı hareket ve saldırı alanını paylaşır."},{"boundary_match":"field_only","distinction":"Odak dal bir hareket ve saldırı eylemidir; komşu dal ise bu sahnede birlikte hareket eden insan topluluğunu adlandırır.","focus_only":"Bir kişinin düşmana saldırması, koşması ve saldırı sayısı anlatılır.","gloss":"savaşta ileri atılma","neighbor_only":"Savaşta saldıran veya yük taşıyan insan topluluğu adlandırılır.","neighbor_ref":"root_001282/B002","relation_type":"same_field","shared_zone":"Her iki dal savaşta ileri yönelen bir saldırı sahnesine katılır."},{"boundary_match":"field_only","distinction":"Odak dal gerçekleşen koşu veya saldırı eylemini bildirir; komşu dal bir atın bu eylemi hızlı yapabilme niteliğini bildirir.","focus_only":"Düşmana yönelen saldırı ve genel koşma eylemi anlatılır.","gloss":"hızlı koşu","neighbor_only":"Bir atın hızlı koşmaya elverişli olması bir nitelik olarak anlatılır.","neighbor_ref":"root_000270/B004","relation_type":"same_field","shared_zone":"Her iki dal hızlı ileri hareket ve koşu alanında buluşur."}],"source_phrase_ar":"في الحرب أيضا يشد شدا (maqayis)؛ الشد الحمل وشد عليه في القتال (ayn;tahdhib)؛ شد على العدو إذا حمل عليه (jamhara;sihah)؛ الشد العدو والفعل اشتد (ayn;sihah)؛ الشد الحضر والفعل اشتد (tahdhib)؛ شد فلان على العدو شدة واحدة وشد شدات كثيرة (tahdhib)","source_summary":"Ortak anlatım, savaşta düşmanın üzerine hızla atılıp saldırmayı verir. Bunun yanında koşma ve hızlı ilerleme anlamı ile tek bir saldırı hamlesini çoğul saldırılardan ayıran kullanım da aktarılır.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"الحمل على العدو في القتال والعدو والحضر","what_is_not_ar":"إيثاق الشيء؛ الصلابة والشدة؛ بلوغ الأشد؛ البخل"},"support_links":["sup_9b9822cca3123cbbe210"]},{"boundary":"Bu dal yalnız bedensel güç veya yalnız biyolojik ergenlik değildir; güç, yetişkinlik, sağduyu ve deneyimin birleştiği olgunluğu anlatır.","branch_kind":"bare","branch_ref":"root_000782/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَدِيد","morph_features":"STEM|POS:N|LEM:$adiyd|ROOT:$dd|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:4:2","qac_word_ref":"100:8:4","surface_ar":"شَدِيدٌ"}],"gloss":"güç ve sağduyu bakımından olgunluğa erişme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan bedensel güç, yetişkinlik, sağduyu ve deneyim bakımından olgunluk düzeyine erişir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gençlik tamamlanır, kişinin gücü ve işleri bir düzene girer ve orta yaşa yaklaşılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Olgunluğa erişme yaşı bir aktarımda yirmi, başka bir aktarımda kırk olarak verilir."}}],"root_ar":"ش د د","root_id":"root_000782","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin yalnız büyümesini değil, bedensel güç, yetişkinlik, sağduyu ve deneyim bakımından tamamlanmasını anlatmak için uygundur.","boundary_detail":"Bu dal yalnız bedensel güç veya yalnız biyolojik ergenlik değildir; güç, yetişkinlik, sağduyu ve deneyimin birleştiği olgunluğu anlatır.","branch_image_ar":"بلوغ الأشد","concept_gloss":"güç ve sağduyu bakımından olgunluğa erişme","contextual_glosses":[{"applicability":"Bedensel gelişimle sağduyu ve deneyimin birlikte tamamlandığı yaşam aşaması anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir yaşam aşamasına erişmeyi ve bu aşamanın genel olgunluk niteliğini korur."},"facet_ids":["F001","F002"],"text":"olgunluk çağına ulaşmak","usage_role":"general"},{"applicability":"Yaş sayısından çok kişinin yetişkin ve güvenilir karar verebilir oluşunun vurgulandığı bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yetişkinlik ile güvenilir karar verme yeterliğinin birlikte bulunmasını korur."},"facet_ids":["F001"],"text":"yetişkinlik ve sağduyu düzeyi","usage_role":"explanatory"}],"definition":"Bir insanın bedensel gücünün, yetişkinliğinin, sağduyusunun ve deneyiminin birleşerek olgunluk düzeyine ulaşmasıdır. Yaş sınırı yirmi ya da kırk diye değişik verilir; temel ölçüt yalnız sayı değil, yetişkinlik ile güvenilir karar verme yeterliğinin görünmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan bedensel güç, yetişkinlik, sağduyu ve deneyim bakımından olgunluk düzeyine erişir."},{"facet_id":"F002","role":"specialization","statement":"Gençlik tamamlanır, kişinin gücü ve işleri bir düzene girer ve orta yaşa yaklaşılır."},{"facet_id":"F003","role":"source_variant","statement":"Olgunluğa erişme yaşı bir aktarımda yirmi, başka bir aktarımda kırk olarak verilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Sözcük çoğunlukla biyolojik gelişimin daha erken bir aşamasını düşündürür.","fit":"narrowing","loses":"Tam güce, sağduyuya, deneyime ve gençliğin tamamlanmasına erişme ölçütlerini dışarıda bırakır.","preserves":"Çocukluktan yetişkinliğe geçişin başlangıç yönünü kısmen korur."},"text":"ergenlik"}],"identity_rationale":"Kaynak ifadesi yetişkinliğe ulaşmayı bedensel güç, sağduyu, deneyim ve gençliğin tamamlanmasıyla birlikte verir. Ancak yaş sınırı yirmi ve kırk olarak değiştiği için dal sabit bir yaş sayısıyla değil, bu yetilerin birleştiği olgunluk düzeyiyle tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"güç, sağduyu ve deneyimin olgunluk düzeyi"}],"lexicalization_note":"Dal bağımsız olgunluk anlamıyla tanımlanır; başka yapılara özgü anlamlar içeri alınmaz ve belirli bir yaş tek sınır sayılmaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; seçilen dört komşu biyolojik yetişkinlik, genel hedefe varma, genel olgunlaşma ve hayvansal tamamlanma sınırlarını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal daha ileri bir güç, sağduyu ve deneyim bütünlüğünü gerektirir; komşu dal biyolojik yetişkinlik eşiğine ulaşmayı anlatır.","focus_only":"Bedensel gücün yanında sağduyu, deneyim ve gençliğin tamamlanması gerekir.","gloss":"yetişkinliğe erişme","neighbor_only":"Biyolojik yetişkinlik eşiğine varmak yeterlidir ve gerçek bir gece olayı zorunlu değildir.","neighbor_ref":"root_000352/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal çocukluktan çıkıp yetişkin sayılmaya yönelen yaşam aşamasını anlatır."},{"boundary_match":"partial","distinction":"Odak dalın ulaşılan son noktası insan olgunluğudur; komşu dal ise yer, zaman ve iş dahil her türlü hedefe varmayı kapsar.","focus_only":"İnsanda güç, yetişkinlik, sağduyu ve deneyimin tamamlanmasıyla belirlenen özel bir son nokta vardır.","gloss":"olgunluğa ulaşma","neighbor_only":"Yer, zaman veya herhangi bir belirlenmiş işteki sona ulaşmayı kapsayan genel bir erişme anlamı vardır.","neighbor_ref":"root_000151/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir gelişme veya ilerleme sonunda belirli bir düzeye erişmeyi içerir."},{"boundary_match":"partial","distinction":"Odak dal insanın yetişkinlik ve sağduyu bütünlüğüne özgüdür; komşu dal nesne, zaman ve başka süreçlerdeki genel olgunlaşmayı kapsar.","focus_only":"İnsanın gücü, sağduyusu ve deneyimiyle tamamlanması zorunludur.","gloss":"olgunlaşma","neighbor_only":"Herhangi bir şeyin vaktine, olgunluğuna veya ısısının son noktasına ulaşması kapsanır.","neighbor_ref":"root_000063/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal bir şeyin gelişip uygun son düzeyine veya vaktine erişmesini anlatabilir."},{"boundary_match":"field_only","distinction":"Odak dal insanın zihinsel ve toplumsal olgunluğunu da içerir; komşu dal hayvanın bedensel ve üremeye ilişkin tamamlanmasına yöneliktir.","focus_only":"İnsanın sağduyu, deneyim, yetişkinlik ve güç bakımından tamamlanması anlatılır.","gloss":"tam güce erişme","neighbor_only":"Hayvanın veya sürünün semizlik ve üreme bakımından tamamlanması anlatılır.","neighbor_ref":"root_000347/B013","relation_type":"same_field","shared_zone":"İki dal canlı bir varlığın gelişerek güç ve tamlık düzeyine ulaşması alanında buluşur."}],"source_phrase_ar":"الأشد العشرون ويقال أربعون سنة (maqayis)؛ الأشد مبلغ الرجل الحنكة والمعرفة (ayn;tahdhib)؛ بلغ الرجل أشده والواحد شد (jamhara)؛ حتى يبلغ أشده أي قوته (sihah)؛ معناه الإدراك والبلوغ وأن يؤنس منه الرشد مع أن يكون بالغا (tahdhib)؛ يجتمع أمره وقوته ويكتهل وينتهي شبابه (tahdhib)","source_summary":"Ortak anlam, kişinin gücünün, yetişkinliğinin, sağduyusunun ve deneyiminin birleştiği olgunluk aşamasına ulaşmasıdır. Yaş için yirmi ve kırk sınırları aktarılır; bunun yanında yetişkinlik, güvenilir karar verme ve gençliğin tamamlanması nitel ölçütlerdir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"بلوغ الأشد من القوة والرشد والحنكة والمعرفة واكتمال الشباب","what_is_not_ar":"مجرد القوة في الشيء؛ إيثاق الوثاق؛ الحملة؛ ارتفاع النهار؛ البخل"},"support_links":[]},{"boundary":"Anlam yalnız günün ilerleyip yükselmesini bildiren belirli söz öbeğine aittir; genel bir yükselme anlamı değildir.","branch_kind":"collocation","branch_ref":"root_000782/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَدِيد","morph_features":"STEM|POS:N|LEM:$adiyd|ROOT:$dd|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:4:2","qac_word_ref":"100:8:4","surface_ar":"شَدِيدٌ"}],"gloss":"günün ilerleyip yükselmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gün ilerler ve gündüz vakti yükselmiş bir aşamaya ulaşır."}}],"root_ar":"ش د د","root_id":"root_000782","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gündüz vaktinin başlangıçtan sonra ilerleyerek yüksek ve belirgin bir aşamaya varmasını anlatan söz öbeğinde uygundur.","boundary_detail":"Anlam yalnız günün ilerleyip yükselmesini bildiren belirli söz öbeğine aittir; genel bir yükselme anlamı değildir.","branch_image_ar":"شد النهار وارتفاعه","concept_gloss":"günün ilerleyip yükselmesi","contextual_glosses":[{"applicability":"Gündüzün başlangıç aşamasını geçip daha ileri ve yüksek bir vakte ulaştığı cümlelerde doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Günün ilerlemiş ve yükselmiş olduğu durumu doğal bir cümleyle korur."},"facet_ids":["F001"],"text":"gün iyice yükseldi","usage_role":"contextual"}],"definition":"Günün başlangıçtan sonra ilerleyerek yükselmesi, yani gündüz vaktinin daha yüksek ve belirgin bir aşamaya varmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gün ilerler ve gündüz vakti yükselmiş bir aşamaya ulaşır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Gün dışındaki her türlü nesne, kişi veya düzey için genel yükselme anlamını ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Aşağıdan daha yüksek bir düzeye geçme yönünü korur."},"text":"yükselmek"}],"identity_rationale":"Kaynak ifadesi yalnız günün yükselmesini bildirir ve dalın geçici açıklaması da bu sınırlı anlamı doğru yansıtır. Başka güç, bağlama veya hareket anlamlarını bu dala taşımak için kanıt yoktur.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"günün ilerleyip yükselmesi"}],"lexicalization_note":"Tanım yalnız günün ilerleyip yükselmesini bildiren söz öbeğine bağlıdır ve yalın kökün genel anlamı olarak genişletilmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; seçilen dört komşu yükselme süreci, yükselmiş zaman kesiti, kuşluk sınırı ve günün başlangıcı arasındaki ayrımları gösteriyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız günün yükselmesini verir; komşu dal yükselmeye yayılma görünümünü ekler ve günün sınırı konusunda farklı bir aktarımı da barındırır.","focus_only":"Yalnız günün ilerleyip yüksek bir aşamaya varması anlatılır.","gloss":"günün yükselmesi","neighbor_only":"Gündüzün yayılması ve bazı aktarımlarda güneşin duvarlardan aşağı inmesi gibi ek sınırlar bulunur.","neighbor_ref":"root_000546/B012","relation_type":"near_synonym","shared_zone":"Her iki dal gündüzün başlangıçtan sonra yükselip ilerlediği aşamayı anlatır."},{"boundary_match":"partial","distinction":"Odak dal yalnız günün yükselme durumuna bağlıdır; komşu dal bunu kuşluk vaktine bağlar ve nesnelerin dikilmesiyle aynı dalda toplar.","focus_only":"Günün genel olarak ilerleyip yükselmesi anlatılır.","gloss":"gündüzün yükselmesi","neighbor_only":"Kuşluk vaktinin yükselmesi ve nesnelerin dikilip doğrulması anlamları da vardır.","neighbor_ref":"root_000642/B012","relation_type":"near_synonym","shared_zone":"İki dalda da gündüzün ilerleyerek daha yüksek bir aşamaya çıkması bulunur."},{"boundary_match":"partial","distinction":"Odak dal günün yükselme sürecini bildirir; komşu dal bu sürecin ulaştığı yüksek ve canlı zaman kesitini adlandırır.","focus_only":"Günün ilerleyerek yükselmesi bir değişim süreci olarak anlatılır.","gloss":"günün yüksek vakti","neighbor_only":"Günün yükselmiş genç ve büyük bölümü bir zaman kesiti olarak adlandırılır.","neighbor_ref":"root_001281/B013","relation_type":"near_neighbor","shared_zone":"Her iki dal günün başlangıcı geçip yükselmiş olduğu gündüz bölümüne yönelir."},{"boundary_match":"field_only","distinction":"Odak dal başlangıçtan sonraki yükselmeyi bildirir; komşu dal ise yükselmeden önceki sabahı ve günün ilk vaktini adlandırır.","focus_only":"Günün başlangıçtan sonra ilerleyip yükselmesi anlatılır.","gloss":"gündüz vakti","neighbor_only":"Sabah, tan ve gündüzün ilk bölümü adlandırılır.","neighbor_ref":"root_000839/B001","relation_type":"same_field","shared_zone":"İki dal da günün içindeki bir zaman aşamasını anlatır."}],"source_phrase_ar":"شد النهار ارتفاعه (maqayis;sihah)","source_summary":"Aktarılan ortak ve tek anlam, günün başlangıçtan sonra ilerleyip yükselmesidir. Kanıt bu anlamı belirli söz öbeği içinde verir.","sources":["MQ","SI"],"what_is_ar":"ارتفاع النهار","what_is_not_ar":"القوة والصلابة؛ إيثاق الشيء؛ الحملة والعدو؛ بلوغ الأشد"},"support_links":[]},{"boundary":"Dal, vermekten kaçınan eli sıkı kişiyi niteleyen anlamla sınırlıdır; genel güç veya sıkılık anlamı buraya taşınmaz.","branch_kind":"bare","branch_ref":"root_000782/B006","candidate_links":[{"candidate_id":"cand_53710b73a4633474b3a4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَدِيد","morph_features":"STEM|POS:N|LEM:$adiyd|ROOT:$dd|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:4:2","qac_word_ref":"100:8:4","surface_ar":"شَدِيدٌ"}],"gloss":"eli sıkılık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi elindekini vermekten kaçınan ve eli sıkı biri olarak nitelenir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı eli sıkılık niteliği iki ayrı sıfat biçimiyle anlatılır."}}],"root_ar":"ش د د","root_id":"root_000782","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin elindekini vermeye yanaşmayan biri olarak nitelenmesini anlatmak için uygundur.","boundary_detail":"Dal, vermekten kaçınan eli sıkı kişiyi niteleyen anlamla sınırlıdır; genel güç veya sıkılık anlamı buraya taşınmaz.","branch_image_ar":"شدة البخل","concept_gloss":"eli sıkılık","contextual_glosses":[{"applicability":"Elindekini vermekten kaçınan bir kişiyi doğal ve doğrudan biçimde nitelemek için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişi niteliğini ve vermekten kaçınan eli sıkı tutumu birlikte korur."},"facet_ids":["F001"],"text":"eli sıkı kişi","usage_role":"general"}],"definition":"Bir kişinin elindekini vermekten kaçınan, eli sıkı biri oluşudur. Kaynak ifadesindeki iki sıfat biçimi kişiyi bu niteliğiyle tanımlar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi elindekini vermekten kaçınan ve eli sıkı biri olarak nitelenir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı eli sıkılık niteliği iki ayrı sıfat biçimiyle anlatılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Davranışta acımasızlık veya nesnede katılık gibi ilgisiz anlamlar ekler.","collision":"Güç ve katılık dalındaki niteliklerle kolayca karışır.","fit":"displacement","loses":"Elindekini vermekten kaçınma ve eli sıkılık niteliğini belirtmez.","preserves":"Kişinin yumuşak davranmayan katı görünümünü çağrıştırabilir."},"text":"sert"}],"identity_rationale":"Kaynak ifadesi iki sıfat biçimini açıkça eli sıkı kişi anlamında verir. Dalın geçici çerçevesi bu kullanımı doğru yansıtır ve güç, bağlama, koşma ya da olgunluk anlamlarından ayrıdır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"eli sıkı"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"eli sıkı"}],"lexicalization_note":"Dal bağımsız eli sıkılık anlamıyla tanımlanır; başka dallardaki güç, katılık ve bağlama anlamları bu tanıma alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bir tam eş anlamlı ile malı tutma, daha çoğunu isteme, iyiliği esirgeme ve vermeyi engelleme sınırlarını gösteren dört yakın komşu seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"İki dalın verilen çekirdekleri ve kişi niteliği sınırları aynıdır; olağan kullanımda birbirinin yerine geçebilir.","focus_only":null,"gloss":"eli sıkı","neighbor_only":null,"neighbor_ref":"root_000915/B007","relation_type":"synonym","shared_zone":"Her iki dal da kişiyi elindekini vermekten kaçınan eli sıkı biri olarak niteler."},{"boundary_match":"partial","distinction":"Odak dal belirli sıfatların kişi niteliği olarak kullanımına dayanır; komşu dal malı tutma eylemini ve bu tutumun daha geniş adlandırmalarını da kapsar.","focus_only":"Kişiyi iki belirli sıfat biçimiyle genel olarak eli sıkı diye niteleme öne çıkar.","gloss":"eli sıkı olma","neighbor_only":"Malı elinde tutma eylemi ve eli sıkı kişiyi anlatan ek adlandırmalar açıkça kapsanır.","neighbor_ref":"root_001424/B002","relation_type":"near_synonym","shared_zone":"Her iki dal elindekini vermekten kaçınan ve malını sıkı tutan kişiyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal yalın eli sıkılık niteliğidir; komşu dal bu niteliği daha çoğunu isteme ve eldekine aşırı bağlanma ile birleştirir.","focus_only":"Elindekini vermekten kaçınan kişi niteliği, ek bir istek koşulu olmadan verilir.","gloss":"vermekten kaçınma","neighbor_only":"Eli sıkılığa daha çoğunu isteme ve eldekini tutkuyla koruma yönü eklenir.","neighbor_ref":"root_000778/B001","relation_type":"near_synonym","shared_zone":"İki dal da elindekini vermeyen, sıkı tutan kişiyi niteleyebilir."},{"boundary_match":"partial","distinction":"Odak dal genel kişi niteliğini verir; komşu dal bu tutumu iyilik azlığı ve verilmesi gereken payı esirgeme üzerinden daha belirli kılar.","focus_only":"Genel olarak elindekini vermekten kaçınan kişi niteliği anlatılır.","gloss":"eli sıkılık","neighbor_only":"İyilik azlığı ve verilmesi gereken bir payı yerine getirmeme yönü açıkça bulunur.","neighbor_ref":"root_000258/B003","relation_type":"near_synonym","shared_zone":"Her iki dal kişide verme isteksizliğini ve iyiliği esirgeme tutumunu anlatır."},{"boundary_match":"partial","distinction":"Odak dal eli sıkılığı bir kişi niteliği olarak adlandırır; komşu dal vermeyi engelleyen eylemi ve iyiliğin karşı tarafa ulaşmamasını daha geniş kapsar.","focus_only":"Eli sıkılık iki sıfatla yerleşik bir kişi niteliği olarak anlatılır.","gloss":"vermemek ve elinde tutmak","neighbor_only":"Vermenin karşıtı olarak engelleme eylemi ve bir başkasına ulaşacak iyiliği durdurma açıkça kapsanır.","neighbor_ref":"root_001448/B001","relation_type":"near_synonym","shared_zone":"İki dalda da kişinin elindekini başkasına vermemesi ve iyiliği kendinde tutması vardır."}],"source_phrase_ar":"الشديد والمتشدد البخيل (maqayis)؛ المتشدد البخيل (sihah)؛ لشديد أي لبخيل (tahdhib)","source_summary":"Ortak aktarım, iki sıfat biçiminin de elindekini vermekten kaçınan eli sıkı kişiyi nitelemesidir. Bu kullanım başka güç ve katılık anlamlarından ayrı bir dal oluşturur.","sources":["MQ","SI","TA"],"what_is_ar":"الشديد والمتشدد بمعنى البخيل","what_is_not_ar":"القوة البدنية؛ إيثاق الشيء؛ العدو والحملة؛ بلوغ الأشد"},"support_links":["sup_1e619313e930c2a0d7fe"]}],"candidate_inventory":[{"anchor_refs":["100:8:1"],"branch_refs":[],"candidate_id":"cand_b12341e09ea15885f6e5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:8:1:fused-particle-subject","source_type":"word_analysis","support_ids":["sup_0bd546c017e978a87ab4","sup_534b2472b6c9a00da7f2"],"title":"relation, assertion, and subject are fused","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:1","qac_refs":["100:8:1:1","100:8:1:2","100:8:1:3"],"status":"accepted"}},{"anchor_refs":["100:8:1"],"branch_refs":[],"candidate_id":"cand_e267508845e500c84b9d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:8:1:parallel-emphatic-diagnosis","source_type":"word_analysis","support_ids":["sup_534b2472b6c9a00da7f2","sup_f3931b51ec569a35783f"],"title":"repeated opening makes a paired diagnosis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:1","qac_refs":["100:8:1:1","100:8:1:2","100:8:1:3"],"status":"accepted"}},{"anchor_refs":["100:8:1"],"branch_refs":[],"candidate_id":"cand_3f1487dc0000c6d0eade","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:8:1:pronoun-human-referent","source_type":"word_analysis","support_ids":["sup_534b2472b6c9a00da7f2","sup_e9f64de2ba9a5208255e"],"title":"suffix keeps the human referent in view","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:1","qac_refs":["100:8:1:1","100:8:1:2","100:8:1:3"],"status":"accepted"}},{"anchor_refs":["100:8:2"],"branch_refs":[],"candidate_id":"cand_9aa479cf4c94530f937e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:8:2:fronted-pivot","source_type":"word_analysis","support_ids":["sup_06d7a85ecacc324a3791","sup_b6130e40e4ce7c5b41f3"],"title":"fronted phrase prepares the verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:2","qac_refs":["100:8:2:1"],"status":"accepted"}},{"anchor_refs":["100:8:2"],"branch_refs":[],"candidate_id":"cand_57329a9cf81062398597","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:8:2:governed-dependent-phrase","source_type":"word_analysis","support_ids":["sup_06d7a85ecacc324a3791","sup_e8a4052aab918e9caac3"],"title":"proclitic lam makes love dependent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:2","qac_refs":["100:8:2:1"],"status":"accepted"}},{"anchor_refs":["100:8:2"],"branch_refs":[],"candidate_id":"cand_50f0a167c40d5367672e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:8:2:lam-scope-polyvalence","source_type":"word_analysis","support_ids":["sup_06601aa9aa9158e06270","sup_06d7a85ecacc324a3791"],"title":"lam leaves cause, domain, and direction live","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:2","qac_refs":["100:8:2:1"],"status":"accepted"}},{"anchor_refs":["100:8:3"],"branch_refs":[],"candidate_id":"cand_20b6f5aab2a9841388f2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"100:8:3:attachment-preference-branch","source_type":"word_analysis","support_ids":["sup_3b2d8f4f43fb03765d96","sup_a500adbdf9dd6c227243"],"title":"love branch becomes forceful preference","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:3","qac_refs":["100:8:2:2"],"status":"accepted"}},{"anchor_refs":["100:8:3"],"branch_refs":[],"candidate_id":"cand_06a7cb96addaba64d035","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"100:8:3:governed-hidden-experiencer","source_type":"word_analysis","support_ids":["sup_9bbb6877fe0fc6753013","sup_a500adbdf9dd6c227243"],"title":"human experiencer is compressed into the phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:3","qac_refs":["100:8:2:2"],"status":"accepted"}},{"anchor_refs":["100:8:3"],"branch_refs":[],"candidate_id":"cand_9118f9f37f6f1cddede7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"100:8:3:hidden-attachment-forward","source_type":"word_analysis","support_ids":["sup_582369fd727a9dea5632","sup_a500adbdf9dd6c227243"],"title":"inner love anticipates later exposure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:3","qac_refs":["100:8:2:2"],"status":"accepted"}},{"anchor_refs":["100:8:3"],"branch_refs":[],"candidate_id":"cand_3cc63b61bb564c781b8c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"100:8:3:love-value-parallels","source_type":"word_analysis","support_ids":["sup_a500adbdf9dd6c227243","sup_d53ea00a4ee68230bff9"],"title":"rare love-value wording has Quranic pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:3","qac_refs":["100:8:2:2"],"status":"accepted"}},{"anchor_refs":["100:8:3"],"branch_refs":[],"candidate_id":"cand_a8cf738064a50cccfe3a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"100:8:3:masdar-construct-condition","source_type":"word_analysis","support_ids":["sup_439ce19321e811400c00","sup_a500adbdf9dd6c227243"],"title":"verbal noun makes love a standing condition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:3","qac_refs":["100:8:2:2"],"status":"accepted"}},{"anchor_refs":["100:8:4"],"branch_refs":[],"candidate_id":"cand_27aff378ceb5ce4426e6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000452"],"scope":"focus_ayah","source_local_id":"100:8:4:chosen-generic-category","source_type":"word_analysis","support_ids":["sup_aeb0ccbb1274ddd10834","sup_fa4ae4653764423e774e"],"title":"singular definite form universalizes the object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:4","qac_refs":["100:8:3:1","100:8:3:2"],"status":"accepted"}},{"anchor_refs":["100:8:4"],"branch_refs":[],"candidate_id":"cand_504e3375be777654187b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000452"],"scope":"focus_ayah","source_local_id":"100:8:4:definite-value-range","source_type":"word_analysis","support_ids":["sup_25cf66c042ae97100115","sup_aeb0ccbb1274ddd10834"],"title":"definite khayr gathers wealth, good, and chosen value","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:4","qac_refs":["100:8:3:1","100:8:3:2"],"status":"accepted"}},{"anchor_refs":["100:8:4"],"branch_refs":[],"candidate_id":"cand_9dade9c239084639a595","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000452"],"scope":"focus_ayah","source_local_id":"100:8:4:fronted-object-field","source_type":"word_analysis","support_ids":["sup_aeb0ccbb1274ddd10834","sup_ee3a469573febb6208f9"],"title":"object-field arrives before the verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:4","qac_refs":["100:8:3:1","100:8:3:2"],"status":"accepted"}},{"anchor_refs":["100:8:4"],"branch_refs":[],"candidate_id":"cand_79c10bd6c7e2f6305486","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000452"],"scope":"focus_ayah","source_local_id":"100:8:4:genitive-loved-object","source_type":"word_analysis","support_ids":["sup_aeb0ccbb1274ddd10834","sup_db7d00c9d7eba8e9c975"],"title":"genitive complement names the loved object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:4","qac_refs":["100:8:3:1","100:8:3:2"],"status":"accepted"}},{"anchor_refs":["100:8:4"],"branch_refs":[],"candidate_id":"cand_813a31c29a843ebeb453","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000452"],"scope":"focus_ayah","source_local_id":"100:8:4:love-value-echoes","source_type":"word_analysis","support_ids":["sup_15aa6eb8858ee2230aa0","sup_aeb0ccbb1274ddd10834"],"title":"love-of-khayr has phrase-level recurrence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:4","qac_refs":["100:8:3:1","100:8:3:2"],"status":"accepted"}},{"anchor_refs":["100:8:4"],"branch_refs":[],"candidate_id":"cand_d825fa88e954c980cf90","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000452"],"scope":"focus_ayah","source_local_id":"100:8:4:recitational-pressure-point","source_type":"word_analysis","support_ids":["sup_aeb0ccbb1274ddd10834","sup_bdb31ad8979410773f58"],"title":"variant closure marks the object boundary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:4","qac_refs":["100:8:3:1","100:8:3:2"],"status":"accepted"}},{"anchor_refs":["100:8:4"],"branch_refs":[],"candidate_id":"cand_7a6d4f5301c62e3c5d6f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000452"],"scope":"focus_ayah","source_local_id":"100:8:4:surah-arc-hinge","source_type":"word_analysis","support_ids":["sup_aeb0ccbb1274ddd10834","sup_b4aedf5803dc7ccdc21e"],"title":"loved value explains and anticipates disclosure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:4","qac_refs":["100:8:3:1","100:8:3:2"],"status":"accepted"}},{"anchor_refs":["100:8:5"],"branch_refs":[],"candidate_id":"cand_9286f10c4b6bb06f2b7c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000782"],"scope":"focus_ayah","source_local_id":"100:8:5:emphatic-predicate-verdict","source_type":"word_analysis","support_ids":["sup_8a74778e3f2ec264b1be","sup_a2d432f9b0c98d1393af"],"title":"final adjective completes the emphatic verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:5","qac_refs":["100:8:4:1","100:8:4:2"],"status":"accepted"}},{"anchor_refs":["100:8:5"],"branch_refs":[],"candidate_id":"cand_7995e2a6c26c0dda8e8a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000782"],"scope":"focus_ayah","source_local_id":"100:8:5:indefinite-sound-closure","source_type":"word_analysis","support_ids":["sup_8a74778e3f2ec264b1be","sup_f905ede921df4ca9ff05"],"title":"indefinite ending leaves intensity open","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:5","qac_refs":["100:8:4:1","100:8:4:2"],"status":"accepted"}},{"anchor_refs":["100:8:5"],"branch_refs":[],"candidate_id":"cand_23fe5d7c7dd2079dad80","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000782"],"scope":"focus_ayah","source_local_id":"100:8:5:orientation-and-exposure","source_type":"word_analysis","support_ids":["sup_8a74778e3f2ec264b1be","sup_f826ed37506e352e496b"],"title":"intensity is judged by orientation and exposure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:5","qac_refs":["100:8:4:1","100:8:4:2"],"status":"accepted"}},{"anchor_refs":["100:8:5"],"branch_refs":[],"candidate_id":"cand_9192500e8008e5b0375a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000782"],"scope":"focus_ayah","source_local_id":"100:8:5:severity-directed-to-love","source_type":"word_analysis","support_ids":["sup_09370b437ee4ff6baa48","sup_8a74778e3f2ec264b1be"],"title":"severity word is redirected into desire","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:5","qac_refs":["100:8:4:1","100:8:4:2"],"status":"accepted"}},{"anchor_refs":["100:8:5"],"branch_refs":[],"candidate_id":"cand_553e3bd2f4029fdf6ca1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000782"],"scope":"focus_ayah","source_local_id":"100:8:5:standing-nominal-diagnosis","source_type":"word_analysis","support_ids":["sup_7054eed83f510c43c586","sup_8a74778e3f2ec264b1be"],"title":"verbless clause makes intensity diagnostic","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:5","qac_refs":["100:8:4:1","100:8:4:2"],"status":"accepted"}},{"anchor_refs":["100:8:5"],"branch_refs":[],"candidate_id":"cand_1382d65c5dd073a08953","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000782"],"scope":"focus_ayah","source_local_id":"100:8:5:witness-vehemence-echo","source_type":"word_analysis","support_ids":["sup_8a74778e3f2ec264b1be","sup_fcb39261a082cf690bf4"],"title":"sound echo pairs witness and vehemence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:8:5","qac_refs":["100:8:4:1","100:8:4:2"],"status":"accepted"}},{"anchor_refs":["100:8:2"],"branch_refs":[],"candidate_id":"cand_59e70e5f346143142bcb","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"100:8:2:2","source_type":"qac_morpheme","support_ids":["sup_21dafff625f15b807c0e"],"title":"QAC root occurrence: ح ب ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["100:8:3"],"branch_refs":[],"candidate_id":"cand_54085da72184e22c18a2","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000452"],"scope":"focus_ayah","source_local_id":"100:8:3:2","source_type":"qac_morpheme","support_ids":["sup_39c7ab10b5e5c9802672"],"title":"QAC root occurrence: خ ي ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["100:8:4"],"branch_refs":[],"candidate_id":"cand_7261e77a833fa252b55b","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000782"],"scope":"focus_ayah","source_local_id":"100:8:4:2","source_type":"qac_morpheme","support_ids":["sup_e37698d754799460a90e"],"title":"QAC root occurrence: ش د د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["100:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:8","branch_refs":["root_000286/B002","root_000452/B001","root_000782/B001"],"candidate_id":"cand_f5c5c8be459cd50c8e1f","commentary_obligation":"review","hft_ref":"hft_030642b0c42fb2078967","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b01-bound-attachment","source_type":"hft","support_ids":["sup_8db776420fd3a411d98e"],"title":"b01-bound-attachment","trust":"legacy_unbound"},{"anchor_refs":["100:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:8","branch_refs":["root_000286/B002","root_000452/B005","root_000782/B006"],"candidate_id":"cand_53710b73a4633474b3a4","commentary_obligation":"review","hft_ref":"hft_4fdb341fec646fb7c52f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b02-miserly-gift","source_type":"hft","support_ids":["sup_1e619313e930c2a0d7fe"],"title":"b02-miserly-gift","trust":"legacy_unbound"},{"anchor_refs":["100:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:8","branch_refs":["root_000286/B002","root_000452/B003","root_000782/B003"],"candidate_id":"cand_69eb74cb192c7f238c85","commentary_obligation":"review","hft_ref":"hft_3257c2c4c1dfaa71be02","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b03-forceful-pursuit","source_type":"hft","support_ids":["sup_9b9822cca3123cbbe210"],"title":"b03-forceful-pursuit","trust":"legacy_unbound"},{"anchor_refs":["100:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:8","branch_refs":["root_000286/B004","root_000452/B003","root_000782/B001"],"candidate_id":"cand_eb5f6311162b51421299","commentary_obligation":"review","hft_ref":"hft_2ba0f826bf115a39c3b4","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b04-hidden-heart-core","source_type":"hft","support_ids":["sup_de16f7c0c8d9cb80ad47"],"title":"b04-hidden-heart-core","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"100:8:1:1","qac_word_ref":"100:8:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"100:8:1:2","qac_word_ref":"100:8:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"100:8:1:3","qac_word_ref":"100:8:1","root_ar":"","surface_ar":"هُۥ"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"100:8:2:1","qac_word_ref":"100:8:2","root_ar":"","surface_ar":"لِ"},{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:2:2","qac_word_ref":"100:8:2","root_ar":"ح ب ب","surface_ar":"حُبِّ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"100:8:3:1","qac_word_ref":"100:8:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"خَيْر","morph_features":"STEM|POS:N|LEM:xayor|ROOT:xyr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:3:2","qac_word_ref":"100:8:3","root_ar":"خ ي ر","surface_ar":"خَيْرِ"},{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"100:8:4:1","qac_word_ref":"100:8:4","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"شَدِيد","morph_features":"STEM|POS:N|LEM:$adiyd|ROOT:$dd|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:4:2","qac_word_ref":"100:8:4","root_ar":"ش د د","surface_ar":"شَدِيدٌ"}],"word_analysis_qac_refs":[["100:8:1:1","100:8:1:2","100:8:1:3"],["100:8:2:1"],["100:8:2:2"],["100:8:3:1","100:8:3:2"],["100:8:4:1","100:8:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["100:8:1","100:8:2","100:8:3","100:8:4","100:8:5"]},"focus_surface_evidence":{"arabic_uthmani":"وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"100:8:1:1","qac_word_ref":"100:8:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"100:8:1:2","qac_word_ref":"100:8:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"100:8:1:3","qac_word_ref":"100:8:1","root_ar":"","surface_ar":"هُۥ"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"100:8:2:1","qac_word_ref":"100:8:2","root_ar":"","surface_ar":"لِ"},{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:2:2","qac_word_ref":"100:8:2","root_ar":"ح ب ب","surface_ar":"حُبِّ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"100:8:3:1","qac_word_ref":"100:8:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"خَيْر","morph_features":"STEM|POS:N|LEM:xayor|ROOT:xyr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:3:2","qac_word_ref":"100:8:3","root_ar":"خ ي ر","surface_ar":"خَيْرِ"},{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"100:8:4:1","qac_word_ref":"100:8:4","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"شَدِيد","morph_features":"STEM|POS:N|LEM:$adiyd|ROOT:$dd|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"100:8:4:2","qac_word_ref":"100:8:4","root_ar":"ش د د","surface_ar":"شَدِيدٌ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["100:8:1:1","100:8:1:2","100:8:1:3"],["100:8:2:1"],["100:8:2:2"],["100:8:3:1","100:8:3:2"],["100:8:4:1","100:8:4:2"]],"word_analysis_refs":["100:8:1","100:8:2","100:8:3","100:8:4","100:8:5"],"word_rows":[{"analysis_record_ref":"100:8:1","analytic_gloss_range_en":"coordinating and emphatic particle stack with a 3ms suffix continuing the human subject from 100:6 through the parallel diagnosis of 100:7-8","analytic_root_gloss_range_en":null,"qac_refs":["100:8:1:1","100:8:1:2","100:8:1:3"],"root":{"note":"— (no root)"},"surface":{"arabic":"وَإِنَّهُۥ","transliteration":"wa-innahu"}},{"analysis_record_ref":"100:8:2","analytic_gloss_range_en":"prepositional lam governing the following verbal noun, with causal, specificative, and directional readings still live in relation to the final predicate","analytic_root_gloss_range_en":null,"qac_refs":["100:8:2:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"لِ","transliteration":"li"}},{"analysis_record_ref":"100:8:3","analytic_gloss_range_en":"verbal-noun love, desire, or attachment in construct with the object of value; local context selects forceful attachment rather than neutral approval","analytic_root_gloss_range_en":"broad root range includes love and preference, seed or grain, inner kernel, and several unrelated concrete branches; locally the love/preference branch is selected, with seed and kernel imagery only as controlled resonance","qac_refs":["100:8:2:2"],"root":{"arabic":"ح ب ب","transliteration":"h-b-b"},"surface":{"arabic":"حُبِّ","transliteration":"hubbi"}},{"analysis_record_ref":"100:8:4","analytic_gloss_range_en":"the loved value object: wealth, benefit, good, advantage, or chosen value; local context foregrounds material attachment while retaining the positive and evaluative tension of the word","analytic_root_gloss_range_en":"broad root range includes good, better, chosen excellence, choosing, wealth treated as good, beneficence, and unrelated idioms; locally the noun names the loved value category, with wealth strongly licensed but not the only pressure","qac_refs":["100:8:3:1","100:8:3:2"],"root":{"arabic":"خ ي ر","transliteration":"kh-y-r"},"surface":{"arabic":"ٱلْخَيْرِ","transliteration":"al-khayri"}},{"analysis_record_ref":"100:8:5","analytic_gloss_range_en":"emphatic qualitative predicate: intense, severe, firm, vehement, or hard-set; local attachment to love of value selects vehement severity rather than neutral strength","analytic_root_gloss_range_en":"broad root range includes fastening, firmness, strength, severity, forceful charge, maturity, and miserliness; locally the adjective activates intensity, firmness, and severity as the human's diagnostic predicate","qac_refs":["100:8:4:1","100:8:4:2"],"root":{"arabic":"ش د د","transliteration":"sh-d-d"},"surface":{"arabic":"لَشَدِيدٌ","transliteration":"la-shadidun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["100:8"],"branch_refs":["root_000286/B002","root_000452/B001","root_000782/B001"],"candidate_id":"cand_f5c5c8be459cd50c8e1f","evidence_scope":"focus_ayah","hft_ref":"hft_030642b0c42fb2078967","item_id":"b01-bound-attachment","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b01-bound-attachment","support_id":"sup_8db776420fd3a411d98e"},{"anchor_refs":["100:8"],"branch_refs":["root_000286/B002","root_000452/B005","root_000782/B006"],"candidate_id":"cand_53710b73a4633474b3a4","evidence_scope":"focus_ayah","hft_ref":"hft_4fdb341fec646fb7c52f","item_id":"b02-miserly-gift","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b02-miserly-gift","support_id":"sup_1e619313e930c2a0d7fe"},{"anchor_refs":["100:8"],"branch_refs":["root_000286/B002","root_000452/B003","root_000782/B003"],"candidate_id":"cand_69eb74cb192c7f238c85","evidence_scope":"focus_ayah","hft_ref":"hft_3257c2c4c1dfaa71be02","item_id":"b03-forceful-pursuit","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b03-forceful-pursuit","support_id":"sup_9b9822cca3123cbbe210"},{"anchor_refs":["100:8"],"branch_refs":["root_000286/B004","root_000452/B003","root_000782/B001"],"candidate_id":"cand_eb5f6311162b51421299","evidence_scope":"focus_ayah","hft_ref":"hft_2ba0f826bf115a39c3b4","item_id":"b04-hidden-heart-core","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b04-hidden-heart-core","support_id":"sup_de16f7c0c8d9cb80ad47"}],"diagnostics":[{"warning":"Unrecognized HFT reader field is preserved as a global review record"},{"warning":"Unrecognized HFT reader field is preserved as a global review record"}],"lane_counts":{"global":11,"macro":11,"micro":4},"packet_summary":{"ayah_count":11,"focus_ref":"100:8","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ع د و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000993","furuq_root_norm":"ع د و","furuq_source_root_norm":"ع د و","is_dominant":true,"target_occurrences":68,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":5,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":false,"target_occurrences":4,"target_rank":3}]},{"qac_root":"ث و ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000210","furuq_root_norm":"ث و ر","furuq_source_root_norm":"ث و ر","is_dominant":true,"target_occurrences":4,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000011","furuq_root_norm":"ء ث ر","furuq_source_root_norm":"أ ث ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["100:1","100:2","100:3","100:4","100:5","100:6","100:7","100:8","100:9","100:10","100:11"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"100:8","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v3","reader_id":"reader_hft_a","trace_kind":null}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":15,"unstructured_record_count":2},"identity":{"ayah_ref":"100:8","lane":"micro","linguistic_source_ref":"100:8","surface_ref":"100:8","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"100:8","target_tokens":[["O",["100:8:1"]],["da",["100:8:1"]],["mal",["100:8:3"]],["sevgisine",["100:8:2"]],["gerçekten",["100:8:1","100:8:4"]],["çok",["100:8:4"]],["düşkündür",["100:8:4"]]],"text":"O da mal sevgisine gerçekten çok düşkündür."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s100-p01-001-011","label":"Whole surah","number":1,"refs":["100:1","100:2","100:3","100:4","100:5","100:6","100:7","100:8","100:9","100:10","100:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:2:lam-scope-polyvalence","source_type":"word_analysis","support_id":"sup_06601aa9aa9158e06270","text":"{\"blocking_evidence\":null,\"headline\":\"lam leaves cause, domain, and direction live\",\"reader_payoff\":\"The reader notices that a single preposition keeps several diagnostic relations alive between love of value and the final intensity verdict.\",\"reason\":\"The input explicitly marks causal, specificative, and directional possibilities, while attachment evidence only fixes the phrase as related to the predicate; the topic is narrowed away from choosing one exclusive English preposition.\",\"representative_source_ids\":[\"QG-e7ef50ee\",\"MG-7bb533c0\",\"QS-1fb8b4d1\",\"QY-6b945db7\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:2","source_type":"word_analysis","support_id":"sup_06d7a85ecacc324a3791","text":"{\"gloss_range\":\"prepositional lam governing the following verbal noun, with causal, specificative, and directional readings still live in relation to the final predicate\",\"prose\":\"{{ar:لِ}} ({{tr:li}}) is the clause's small scope hinge. It governs {{ar:حُبِّ}} ({{tr:hubbi}}), so the love phrase is not a second subject but the frame through which {{ar:لَشَدِيدٌ}} ({{tr:la-shadidun}}) is measured. Its local force remains usefully polyvalent: the love of {{ar:ٱلْخَيْرِ}} ({{tr:al-khayri}}) can be the cause of intensity, the domain where intensity is assessed, or the direction toward which intensity moves. Because the phrase stands before the delayed predicate, the reader receives the object-field first and hears the final verdict through that frame. In the matching pre-predicate slot after 100:7, the movement shifts from witness over evidence to a human bound by attachment, so apparent oversight gives way to desire. The brief proclitic also contrasts with the later emphatic {{ar:لَ}} ({{tr:la}}): the ayah repeats the lam sound while assigning the two lams different grammatical jobs.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لِ}} ({{tr:li}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:5:severity-directed-to-love","source_type":"word_analysis","support_id":"sup_09370b437ee4ff6baa48","text":"{\"blocking_evidence\":null,\"headline\":\"severity word is redirected into desire\",\"reader_payoff\":\"The reader notices that a word of firmness, tightness, and severity evaluates love itself as hard-set and excessive.\",\"reason\":\"V4 supports firmness, strength, and severity branches; local attachment to {{ar:حُبِّ ٱلْخَيْرِ}} ({{tr:hubbi al-khayri}}) narrows the adjective toward emotional and behavioral vehemence, not physical force or unrelated branches.\",\"representative_source_ids\":[\"QS-01fbdbf9\",\"QS-46b7ce67\",\"QS-4dcd2f41\",\"QS-675a36cc\",\"QI-40846fef\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:1:fused-particle-subject","source_type":"word_analysis","support_id":"sup_0bd546c017e978a87ab4","text":"{\"blocking_evidence\":null,\"headline\":\"relation, assertion, and subject are fused\",\"reader_payoff\":\"The reader notices that the first word compresses the ayah's connective force, emphasis, and subject into a single audible unit.\",\"reason\":\"The surface form visibly combines the coordinator, the emphatic particle, and the suffix; the repeated cadence across 100:7-8 supports the sound-frame observation.\",\"representative_source_ids\":[\"QF-5963a471\",\"QP-26bca2f4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:4:love-value-echoes","source_type":"word_analysis","support_id":"sup_15aa6eb8858ee2230aa0","text":"{\"blocking_evidence\":null,\"headline\":\"love-of-khayr has phrase-level recurrence\",\"reader_payoff\":\"The reader notices that the value object is sharpened by the rare love-of-value configuration in 38:32 and by its immediate placement beside severity here.\",\"reason\":\"The concrete 38:32 recurrence and local adjacency to {{ar:لَشَدِيدٌ}} ({{tr:la-shadidun}}) support phrase-level pressure without turning the intertext into the governing parse.\",\"representative_source_ids\":[\"QI-11808043\",\"QI-7db9e1ce\",\"QE-1fc080d8\",\"QH-476a5ac8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"100:8:2:2","source_type":"qac_morpheme","support_id":"sup_21dafff625f15b807c0e","text":"{\"lemma_ar\":\"حُبّ\",\"morph_features\":\"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"100:8:2:2\",\"qac_word_ref\":\"100:8:2\",\"root_ar\":\"ح ب ب\",\"surface_ar\":\"حُبِّ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:4:definite-value-range","source_type":"word_analysis","support_id":"sup_25cf66c042ae97100115","text":"{\"blocking_evidence\":null,\"headline\":\"definite khayr gathers wealth, good, and chosen value\",\"reader_payoff\":\"The reader notices that the critique is not aimed at a random object but at an attractive value category where wealth, benefit, goodness, and chosen preference overlap.\",\"reason\":\"V4 supports good, chosen excellence, choice, wealth, and beneficence branches; local grammar and the severe predicate narrow the active reading toward loved value or wealth while preserving the positive lexical tension.\",\"representative_source_ids\":[\"QG-d277651c\",\"QS-0c95dc4e\",\"QS-5aac3757\",\"MS-0365f3dc\",\"QY-394452c2\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"100:8:3:2","source_type":"qac_morpheme","support_id":"sup_39c7ab10b5e5c9802672","text":"{\"lemma_ar\":\"خَيْر\",\"morph_features\":\"STEM|POS:N|LEM:xayor|ROOT:xyr|MS|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"100:8:3:2\",\"qac_word_ref\":\"100:8:3\",\"root_ar\":\"خ ي ر\",\"surface_ar\":\"خَيْرِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:3:attachment-preference-branch","source_type":"word_analysis","support_id":"sup_3b2d8f4f43fb03765d96","text":"{\"blocking_evidence\":null,\"headline\":\"love branch becomes forceful preference\",\"reader_payoff\":\"The reader notices that the word names more than mild approval: it is a tightened attachment to what the human has treated as preferable.\",\"reason\":\"V4 supports the love/preference branch for the local sense and also records seed or inner-kernel branches; those images survive only as resonance because local grammar selects the verbal-noun love sense.\",\"representative_source_ids\":[\"QS-47c53230\",\"QS-5ae94708\",\"QS-9ff1e289\",\"QP-f581a8dc\",\"QY-ff781c4f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:3:masdar-construct-condition","source_type":"word_analysis","support_id":"sup_439ce19321e811400c00","text":"{\"blocking_evidence\":null,\"headline\":\"verbal noun makes love a standing condition\",\"reader_payoff\":\"The reader notices that the ayah does not narrate one act of loving; it names love as the inner condition through which the human is diagnosed.\",\"reason\":\"QAC identifies {{ar:حُبِّ}} ({{tr:hubbi}}) as a genitive verbal noun and construct head, and attachment evidence forces {{ar:ٱلْخَيْرِ}} ({{tr:al-khayri}}) as its genitive complement.\",\"representative_source_ids\":[\"QG-2d7939df\",\"QG-e11d386e\",\"QF-59b1e701\",\"QT-43053f3f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:1","source_type":"word_analysis","support_id":"sup_534b2472b6c9a00da7f2","text":"{\"gloss_range\":\"coordinating and emphatic particle stack with a 3ms suffix continuing the human subject from 100:6 through the parallel diagnosis of 100:7-8\",\"prose\":\"{{ar:وَإِنَّهُۥ}} ({{tr:wa-innahu}}) launches the ayah as a coordinated emphatic diagnosis, not as a new scene. The same opening shape as the previous verse makes 100:8 a structural twin of 100:7: the human remains under the same diagnostic gaze, first as witness and then as vehemently attached. The suffix {{ar:هُ}} ({{tr:hu}}) is locally narrowed by the predicate and the prior discourse to the generic human from 100:6, even though the raw pronoun itself could invite broader referential possibilities. Because coordination, assertion, and subject are fused into one surface word, the reader hears relation, emphasis, and referent before the love phrase is even named.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَإِنَّهُۥ}} ({{tr:wa-innahu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:3:hidden-attachment-forward","source_type":"word_analysis","support_id":"sup_582369fd727a9dea5632","text":"{\"blocking_evidence\":null,\"headline\":\"inner love anticipates later exposure\",\"reader_payoff\":\"The reader notices that the inward attachment named here sits before the later exposure of what is hidden in 100:9-10.\",\"reason\":\"The forward boundary claim is coherent with the ayah sequence, and the 2:165 contrast remains a directional parallel rather than a claim that the same object is active locally.\",\"representative_source_ids\":[\"MT-ee62b559\",\"QE-391aedd8\",\"MI-375fd479\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:5:standing-nominal-diagnosis","source_type":"word_analysis","support_id":"sup_7054eed83f510c43c586","text":"{\"blocking_evidence\":null,\"headline\":\"verbless clause makes intensity diagnostic\",\"reader_payoff\":\"The reader notices that the ayah presents intensity as a standing trait in the same diagnostic register as 100:7.\",\"reason\":\"Both 100:7 and 100:8 use nominal emphatic clauses, and the two local lams have different functions: prepositional governance earlier and emphatic assertion here.\",\"representative_source_ids\":[\"MG-4a2464bd\",\"QT-e2fb2ff4\",\"QE-498bc1a2\",\"QB-88f64f1d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:5","source_type":"word_analysis","support_id":"sup_8a74778e3f2ec264b1be","text":"{\"gloss_range\":\"emphatic qualitative predicate: intense, severe, firm, vehement, or hard-set; local attachment to love of value selects vehement severity rather than neutral strength\",\"prose\":\"{{ar:لَشَدِيدٌ}} ({{tr:la-shadidun}}) is the ayah's final verdict. The prefixed emphatic lam closes the inna frame, and the nominative adjective functions as the predicate, not as a modifier of the genitive love phrase. That grammar identifies the human as vehemently intense in relation to {{ar:حُبِّ ٱلْخَيْرِ}} ({{tr:hubbi al-khayri}}), rather than merely describing the love phrase itself. The root {{ar:ش د د}} ({{tr:sh-d-d}}) brings firmness, tightening, strength, and severity into the judgment, so the love of a positive-sounding object becomes excessive and hard-set. The indefinite ending leaves the degree open while the final cadence lets the verdict land as a self-contained close, and the doubled d pressure makes the tightening audible at the ayah's end. Across the boundary, the 100:8 predicate near-echoes the witness predicate in 100:7 through shared initial sound, fa'il shape, and close terminal cadence: the one who is witness is also vehemently attached. The contrast with 2:165 shows that intensity of love is evaluated by orientation, and the inward intensity named here points forward to the exposure of what is in breasts in 100:10.\",\"root_display\":\"{{ar:ش د د}} ({{tr:sh-d-d}})\",\"root_gloss_range\":\"broad root range includes fastening, firmness, strength, severity, forceful charge, maturity, and miserliness; locally the adjective activates intensity, firmness, and severity as the human's diagnostic predicate\",\"surface_display\":\"{{ar:لَشَدِيدٌ}} ({{tr:la-shadidun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:3:governed-hidden-experiencer","source_type":"word_analysis","support_id":"sup_9bbb6877fe0fc6753013","text":"{\"blocking_evidence\":null,\"headline\":\"human experiencer is compressed into the phrase\",\"reader_payoff\":\"The reader notices that the human subject remains grammatically outside the love phrase while still being the experiencer of the attachment.\",\"reason\":\"The governed masdar has no overt agent inside the phrase, but the pronominal subject of {{ar:إِنَّ}} ({{tr:inna}}) and the antecedent from 100:6 supply the human experiencer.\",\"representative_source_ids\":[\"QG-e76fc178\",\"QS-d61f359f\",\"QF-502d5172\",\"QT-12256c92\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:5:emphatic-predicate-verdict","source_type":"word_analysis","support_id":"sup_a2d432f9b0c98d1393af","text":"{\"blocking_evidence\":null,\"headline\":\"final adjective completes the emphatic verdict\",\"reader_payoff\":\"The reader notices that the last word is the asserted predicate about the human, not an adjective attached to the love phrase.\",\"reason\":\"QAC and attachment evidence identify {{ar:لَشَدِيدٌ}} ({{tr:la-shadidun}}) as the predicate of {{ar:إِنَّ}} ({{tr:inna}}); its nominative case prevents treating it as a genitive modifier of the love phrase.\",\"representative_source_ids\":[\"QG-56dabf5c\",\"QG-6459f946\",\"QG-b7b67ea6\",\"QF-52d16899\",\"QT-d89ce39b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:3","source_type":"word_analysis","support_id":"sup_a500adbdf9dd6c227243","text":"{\"gloss_range\":\"verbal-noun love, desire, or attachment in construct with the object of value; local context selects forceful attachment rather than neutral approval\",\"prose\":\"{{ar:حُبِّ}} ({{tr:hubbi}}) turns loving into a nominal condition inside the diagnosis. As a verbal noun governed by {{ar:لِ}} ({{tr:li}}), it is not a finite report that the human loves once; it is the standing frame through which the final predicate is heard. The construct {{ar:حُبِّ ٱلْخَيْرِ}} ({{tr:hubbi al-khayri}}) compresses lover, attachment, and valued object into one phrase: the human is supplied by the suffix, while {{ar:ٱلْخَيْرِ}} ({{tr:al-khayri}}) receives the love as the chosen value. The selected branch is love, desire, and preference; the seed and inner-kernel imagery from {{ar:ح ب ب}} ({{tr:h-b-b}}) can make the attachment feel planted inwardly, but it should not replace the local sense. The phrase also resonates with 38:32, where love of {{ar:ٱلْخَيْرِ}} ({{tr:al-khayri}}) competes with remembrance, and with 2:165, where intensified love is oriented to God rather than to the local value object. Placed before 100:9-10, this inward attachment is also positioned ahead of the resurrection scene and the exposure of what has been stored inside.\",\"root_display\":\"{{ar:ح ب ب}} ({{tr:h-b-b}})\",\"root_gloss_range\":\"broad root range includes love and preference, seed or grain, inner kernel, and several unrelated concrete branches; locally the love/preference branch is selected, with seed and kernel imagery only as controlled resonance\",\"surface_display\":\"{{ar:حُبِّ}} ({{tr:hubbi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:4","source_type":"word_analysis","support_id":"sup_aeb0ccbb1274ddd10834","text":"{\"gloss_range\":\"the loved value object: wealth, benefit, good, advantage, or chosen value; local context foregrounds material attachment while retaining the positive and evaluative tension of the word\",\"prose\":\"{{ar:ٱلْخَيْرِ}} ({{tr:al-khayri}}) supplies the object-field of the diagnosis. It is genitive as the complement of {{ar:حُبِّ}} ({{tr:hubbi}}), so it is not a second predicate or an independent subject; it is the value object around which love gathers. Its definiteness and singular abstract form make the object category-level: not one possession, but wealth, benefit, good, advantage, or chosen value as a whole. Local context strongly foregrounds wealth and advantage, yet the word's positive sense keeps the line sharper: a lexically attractive object receives a severe verdict because of the human's tightened attachment. A supplied sukun variant can make the object of love sound briefly closed before the predicate delivers the verdict, marking the end of the love phrase without changing its sense. The horse sense is possible as a controlled bridge back to the charging opening of 100:1-5, not as a replacement for the local value-object reading. The phrase also echoes 38:32, where love of {{ar:ٱلْخَيْرِ}} ({{tr:al-khayri}}) is textually marked, and it helps explain the prior diagnosis of ingratitude in 100:6-7 while pointing forward to the exposure of inner contents in 100:9-10.\",\"root_display\":\"{{ar:خ ي ر}} ({{tr:kh-y-r}})\",\"root_gloss_range\":\"broad root range includes good, better, chosen excellence, choosing, wealth treated as good, beneficence, and unrelated idioms; locally the noun names the loved value category, with wealth strongly licensed but not the only pressure\",\"surface_display\":\"{{ar:ٱلْخَيْرِ}} ({{tr:al-khayri}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:4:surah-arc-hinge","source_type":"word_analysis","support_id":"sup_b4aedf5803dc7ccdc21e","text":"{\"blocking_evidence\":null,\"headline\":\"loved value explains and anticipates disclosure\",\"reader_payoff\":\"The reader notices that the loved value both explains the earlier human diagnosis in 100:6-7 and prepares the later exposure of what is hidden in 100:9-10.\",\"reason\":\"The bridge to 100:6-10 is locally coherent; the horse-image link to 100:1-5 is narrowed to a possible lexical and thematic resonance because the local construct primarily names the loved value object.\",\"representative_source_ids\":[\"MI-90275760\",\"QT-a65697dd\",\"QE-7c312c52\",\"QB-24488278\",\"QB-cb5b5e6c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:2:fronted-pivot","source_type":"word_analysis","support_id":"sup_b6130e40e4ce7c5b41f3","text":"{\"blocking_evidence\":null,\"headline\":\"fronted phrase prepares the verdict\",\"reader_payoff\":\"The reader notices that the clause moves through the love phrase before reaching the verdict, so intensity is heard as already scoped by attachment.\",\"reason\":\"The prepositional phrase occupies the pre-predicate slot between the suffix and {{ar:لَشَدِيدٌ}} ({{tr:la-shadidun}}), and the contrast with the prior prepositional slot in 100:7 is structurally coherent.\",\"representative_source_ids\":[\"QT-6971fa59\",\"QT-77b9ffca\",\"QB-5e589c39\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:4:recitational-pressure-point","source_type":"word_analysis","support_id":"sup_bdb31ad8979410773f58","text":"{\"blocking_evidence\":null,\"headline\":\"variant closure marks the object boundary\",\"reader_payoff\":\"The reader notices that the object of love can sound momentarily closure-like before the final predicate delivers the verdict.\",\"reason\":\"The supplied qiraat note changes recitational pressure rather than local meaning, so it survives as a sound-boundary observation only.\",\"representative_source_ids\":[\"QF-614493e5\",\"QF-efe223b4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:3:love-value-parallels","source_type":"word_analysis","support_id":"sup_d53ea00a4ee68230bff9","text":"{\"blocking_evidence\":null,\"headline\":\"rare love-value wording has Quranic pressure\",\"reader_payoff\":\"The reader notices that this love of value belongs to a small phrase-level field, especially the marked recurrence with 38:32 and the contrasting love-intensity orientation in 2:165.\",\"reason\":\"The CRITICAL rows give concrete references at 38:32 and 2:165; these parallels illuminate orientation and phrase pressure without overriding the local parse.\",\"representative_source_ids\":[\"QI-8dfaee95\",\"QI-a2b6976a\",\"QI-cf286785\",\"QE-71aafa81\",\"QH-97ece934\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:4:genitive-loved-object","source_type":"word_analysis","support_id":"sup_db7d00c9d7eba8e9c975","text":"{\"blocking_evidence\":null,\"headline\":\"genitive complement names the loved object\",\"reader_payoff\":\"The reader notices that the word is bound inside the love construct, making it the value object or source of attraction rather than a free-standing claim.\",\"reason\":\"Attachment evidence forces {{ar:ٱلْخَيْرِ}} ({{tr:al-khayri}}) as the genitive complement of {{ar:حُبِّ}} ({{tr:hubbi}}); the subjective-source possibility is kept as nuance but narrowed by the human subject and love predicate.\",\"representative_source_ids\":[\"QG-0bef8a6e\",\"QG-478f5d3e\",\"QP-36217278\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"100:8:4:2","source_type":"qac_morpheme","support_id":"sup_e37698d754799460a90e","text":"{\"lemma_ar\":\"شَدِيد\",\"morph_features\":\"STEM|POS:N|LEM:$adiyd|ROOT:$dd|MS|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"100:8:4:2\",\"qac_word_ref\":\"100:8:4\",\"root_ar\":\"ش د د\",\"surface_ar\":\"شَدِيدٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:2:governed-dependent-phrase","source_type":"word_analysis","support_id":"sup_e8a4052aab918e9caac3","text":"{\"blocking_evidence\":null,\"headline\":\"proclitic lam makes love dependent\",\"reader_payoff\":\"The reader notices that love is grammatically governed and bound into the predicate frame rather than standing as an independent topic.\",\"reason\":\"QAC marks {{ar:لِ}} ({{tr:li}}) as the preposition prefixed to the genitive verbal noun, and attachment evidence relates the resulting phrase to the final predicate.\",\"representative_source_ids\":[\"QG-ffffed10\",\"QF-9f8280ec\",\"QP-e8518abc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:1:pronoun-human-referent","source_type":"word_analysis","support_id":"sup_e9f64de2ba9a5208255e","text":"{\"blocking_evidence\":null,\"headline\":\"suffix keeps the human referent in view\",\"reader_payoff\":\"The reader notices that the compact suffix carries the same human subject forward from 100:6 into the repeated diagnosis of 100:7-8.\",\"reason\":\"The CRITICAL rows raise referential possibilities, but the attachment evidence explicitly resolves the suffix toward the generic human from 100:6 and the local predicate supports that narrowing.\",\"representative_source_ids\":[\"QG-e6621edb\",\"MG-f558bd95\",\"QS-7ea353d8\",\"QB-60c602e7\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:4:fronted-object-field","source_type":"word_analysis","support_id":"sup_ee3a469573febb6208f9","text":"{\"blocking_evidence\":null,\"headline\":\"object-field arrives before the verdict\",\"reader_payoff\":\"The reader notices that the phrase completes the domain of attachment before the final adjective lands, so the verdict is already framed by the loved object.\",\"reason\":\"The word completes the preposed construct phrase immediately before the final predicate.\",\"representative_source_ids\":[\"QT-ebedca40\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:1:parallel-emphatic-diagnosis","source_type":"word_analysis","support_id":"sup_f3931b51ec569a35783f","text":"{\"blocking_evidence\":null,\"headline\":\"repeated opening makes a paired diagnosis\",\"reader_payoff\":\"The reader notices that 100:8 is heard as the matching second diagnosis beside 100:7, not as a detached moral comment.\",\"reason\":\"QAC and attachment evidence identify a coordinated {{ar:إِنَّ}} ({{tr:inna}}) clause whose predicate is completed at {{ar:لَشَدِيدٌ}} ({{tr:la-shadidun}}), matching the emphatic diagnostic frame of 100:7.\",\"representative_source_ids\":[\"QG-f6cb276f\",\"MG-534d7d88\",\"QT-515b6c14\",\"QT-a0808094\",\"QB-da9d034c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:5:orientation-and-exposure","source_type":"word_analysis","support_id":"sup_f826ed37506e352e496b","text":"{\"blocking_evidence\":null,\"headline\":\"intensity is judged by orientation and exposure\",\"reader_payoff\":\"The reader notices that the problem is not intensity alone: intensity is judged by the value it clings to here and is positioned before disclosure in 100:10.\",\"reason\":\"The 2:165 love-intensity contrast and the forward movement to 100:10 are concrete references that clarify orientation and disclosure without changing the local predicate grammar.\",\"representative_source_ids\":[\"QI-02f21509\",\"QI-c95327ff\",\"QI-f65b6539\",\"QB-16925863\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:5:indefinite-sound-closure","source_type":"word_analysis","support_id":"sup_f905ede921df4ca9ff05","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite ending leaves intensity open\",\"reader_payoff\":\"The reader notices that the final indefinite predicate sounds closed as an ayah ending while leaving the degree of intensity unmeasured.\",\"reason\":\"The tanwin and final position support closure, while the geminate root shape supports the sound-pressure observation without making phonetics the primary sense.\",\"representative_source_ids\":[\"QG-36e32166\",\"QF-9973a5e3\",\"MF-7a521ddd\",\"QP-c5469371\",\"QY-f81de857\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:4:chosen-generic-category","source_type":"word_analysis","support_id":"sup_fa4ae4653764423e774e","text":"{\"blocking_evidence\":null,\"headline\":\"singular definite form universalizes the object\",\"reader_payoff\":\"The reader notices that the ayah gathers many desired goods into one selected category rather than listing possessions one by one.\",\"reason\":\"The article, singular noun form, and root evidence for choice and preference support a generic chosen-value reading within the local construct.\",\"representative_source_ids\":[\"QS-4b374238\",\"QS-794b549c\",\"QF-19604074\",\"QI-56fe7f2f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:8:5:witness-vehemence-echo","source_type":"word_analysis","support_id":"sup_fcb39261a082cf690bf4","text":"{\"blocking_evidence\":null,\"headline\":\"sound echo pairs witness and vehemence\",\"reader_payoff\":\"The reader notices that the closing sound of 100:8 answers the closing sound of 100:7, pairing awareness with forceful attachment.\",\"reason\":\"The near-echo between {{ar:شَهِيدٌ}} ({{tr:shahidun}}) in 100:7 and {{ar:شَدِيدٌ}} ({{tr:shadidun}}) in 100:8 is concrete, adjacent, and form-linked, though it does not amount to root recurrence.\",\"representative_source_ids\":[\"QE-d0994efe\",\"QP-5bf9ad91\",\"QB-037ed412\",\"QB-db94a2e1\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ","ayah_ref":"100:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000286/B002","root_000452/B001","root_000782/B001"],"payload":{"activation_trace":[{"assigned_role":"Supplies the persistent attachment in the focus relation.","branch_id":"B002","branch_image_ar":"المحبة الملازمة للقلب","literal_contribution":"Love is an attachment that remains with the heart.","mapped_root_id":"root_000286","mapped_root_norm":"ح ب ب","root":"ح ب ب","source_phrase_ar":"حُبِّ","source_ref":"100:8"},{"assigned_role":"Supplies the attachment's positively valued object.","branch_id":"B001","branch_image_ar":"الميل إلى الخير النافع","literal_contribution":"The good is what is inclined toward as beneficial.","mapped_root_id":"root_000452","mapped_root_norm":"خ ي ر","root":"خ ي ر","source_phrase_ar":"خَيْرِ","source_ref":"100:8"},{"assigned_role":"Turns intensity into the firmness of the subject-object bond.","branch_id":"B001","branch_image_ar":"شد العقد والوثاق","literal_contribution":"A bond is tied and made firm.","mapped_root_id":"root_000782","mapped_root_norm":"ش د د","root":"ش د د","source_phrase_ar":"شَدِيدٌ","source_ref":"100:8"}],"changed_reading":{"after":"He is tightly fastened to what he takes to be good; the verse profiles the tenacity of the bond, not merely a large quantity of affection.","before":"He loves the good very intensely."},"confidence":"strong","focus_anchor":"The construction لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ joins ح ب ب as clinging attachment, خ ي ر as desired benefit, and ش د د as a fastened bond.","mechanism":"The three focus roots yield a relational mechanism: something judged beneficial attracts preference, preference clings, and the doubled lām construction culminates in a predicate of tight fastening. شَدِيدٌ therefore describes not only degree but how firmly the subject is bound to the desired good.","model_id":"b01-bound-attachment","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b01-bound-attachment","source_type":"hft","support_id":"sup_8db776420fd3a411d98e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ","ayah_ref":"100:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000286/B002","root_000452/B005","root_000782/B006"],"payload":{"activation_trace":[{"assigned_role":"Makes possession emotionally adhesive.","branch_id":"B002","branch_image_ar":"المحبة الملازمة للقلب","literal_contribution":"Preference clings to the heart.","mapped_root_id":"root_000286","mapped_root_norm":"ح ب ب","root":"ح ب ب","source_phrase_ar":"حُبِّ","source_ref":"100:8"},{"assigned_role":"Recasts the object from abstract goodness as transferable bounty.","branch_id":"B005","branch_image_ar":"الكرم والهبة","literal_contribution":"Khayr can image beneficence, giving, or a gift.","mapped_root_id":"root_000452","mapped_root_norm":"خ ي ر","root":"خ ي ر","source_phrase_ar":"خَيْرِ","source_ref":"100:8"},{"assigned_role":"Makes withholding, rather than emotional volume alone, the predicate's function.","branch_id":"B006","branch_image_ar":"شدة البخل","literal_contribution":"Severity can denote miserliness.","mapped_root_id":"root_000782","mapped_root_norm":"ش د د","root":"ش د د","source_phrase_ar":"شَدِيدٌ","source_ref":"100:8"}],"changed_reading":{"after":"He clings severely to bounty and is tight-fisted with what could circulate as a gift.","before":"He has an intense love of goodness."},"confidence":"medium","focus_anchor":"حُبِّ can be clinging preference, خَيْرِ can be beneficence or gift, and شَدِيدٌ has a branch explicitly naming miserliness.","mechanism":"A received or available gift becomes an object of possessive attachment. Because the ش د د inventory permits severity as miserliness, the predicate can diagnose retention: love of giving-as-object becomes unwillingness to let the gift pass onward.","model_id":"b02-miserly-gift","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b02-miserly-gift","source_type":"hft","support_id":"sup_1e619313e930c2a0d7fe","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ","ayah_ref":"100:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000286/B002","root_000452/B003","root_000782/B003"],"payload":{"activation_trace":[{"assigned_role":"Acts as the motive force.","branch_id":"B002","branch_image_ar":"المحبة الملازمة للقلب","literal_contribution":"Love supplies a durable preference.","mapped_root_id":"root_000286","mapped_root_norm":"ح ب ب","root":"ح ب ب","source_phrase_ar":"حُبِّ","source_ref":"100:8"},{"assigned_role":"Supplies the pursued target.","branch_id":"B003","branch_image_ar":"طلب الخير بالاختيار والاستخارة","literal_contribution":"Khayr includes selecting or seeking the better option.","mapped_root_id":"root_000452","mapped_root_norm":"خ ي ر","root":"خ ي ر","source_phrase_ar":"خَيْرِ","source_ref":"100:8"},{"assigned_role":"Converts preference into vigorous directed motion.","branch_id":"B003","branch_image_ar":"شد الحملة والعدو","literal_contribution":"Shidda can image a forceful charge or run.","mapped_root_id":"root_000782","mapped_root_norm":"ش د د","root":"ش د د","source_phrase_ar":"شَدِيدٌ","source_ref":"100:8"}],"changed_reading":{"after":"He drives hard toward the option he prefers; شَدِيدٌ can profile pursuit as well as feeling.","before":"He feels strongly about the good."},"confidence":"exploratory","focus_anchor":"Within the focus inventories, خَيْرِ can be the better option selected, حُبِّ can be preference, and شَدِيدٌ can image a forceful charge.","mechanism":"Selection supplies a target, attachment supplies directional preference, and the charge branch of ش د د converts that preference into pursuit. The predicate can therefore be kinetic: desire does not merely sit in the subject but drives him toward the preferred outcome.","model_id":"b03-forceful-pursuit","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b03-forceful-pursuit","source_type":"hft","support_id":"sup_9b9822cca3123cbbe210","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ","ayah_ref":"100:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000286/B004","root_000452/B003","root_000782/B001"],"payload":{"activation_trace":[{"assigned_role":"Locates love as a compact interior motive.","branch_id":"B004","branch_image_ar":"حبة القلب سويداؤه","literal_contribution":"The root can image the heart's innermost kernel.","mapped_root_id":"root_000286","mapped_root_norm":"ح ب ب","root":"ح ب ب","source_phrase_ar":"حُبِّ","source_ref":"100:8"},{"assigned_role":"Names the value lodged at the center.","branch_id":"B003","branch_image_ar":"طلب الخير بالاختيار والاستخارة","literal_contribution":"Khayr can be what is selected as the better option.","mapped_root_id":"root_000452","mapped_root_norm":"خ ي ر","root":"خ ي ر","source_phrase_ar":"خَيْرِ","source_ref":"100:8"},{"assigned_role":"Explains why the inner valuation is difficult to dislodge.","branch_id":"B001","branch_image_ar":"شد العقد والوثاق","literal_contribution":"The bond is made firm.","mapped_root_id":"root_000782","mapped_root_norm":"ش د د","root":"ش د د","source_phrase_ar":"شَدِيدٌ","source_ref":"100:8"}],"changed_reading":{"after":"The verse locates a tightly bound valuation in the heart's kernel, presenting love as a hidden causal core.","before":"The verse reports an observable intensity of love."},"confidence":"medium","focus_anchor":"The focus noun حُبِّ activates the branch حبة القلب سويداؤه, while خَيْرِ activates selection and شَدِيدٌ activates a firm bond.","mechanism":"The selected good is lodged at the heart's inner kernel and held there by a tightened bond. This produces an inward-causal reading: the verse identifies a compact motive at the subject's core from which conduct can issue.","model_id":"b04-hidden-heart-core","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b04-hidden-heart-core","source_type":"hft","support_id":"sup_de16f7c0c8d9cb80ad47","trust":"legacy_unbound"}]}
</lane_packet_json>
