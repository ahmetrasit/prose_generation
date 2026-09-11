# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **114:5**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s114-regular-20260911/s114/114_5/micro.discovery.json` and modify nothing
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
  "ayah_ref": "114:5",
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
{"analysis_context":{"analysis_id":"s114-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"114:5","host_surah":114,"lane_context_refs":[],"ordered_context_refs":["114:0","114:1","114:2","114:3","114:4","114:6","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, insan türünü ve onun tekil ya da toplu üyelerini kapsar; yakınlık duygusunu, duyusal algıyı ve insana dönük yanı kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:5:5:2","qac_word_ref":"114:5:5","surface_ar":"نَّاسِ"}],"gloss":"insan türü ve bu türden bir kişi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan türünü, insanların oluşturduğu topluluğu veya bu türün tek bir üyesini görünmeyen varlıklar sınıfının karşısında adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırmanın insanların duyularla görünür oluşuna bağlanması, anlamın özü değil kökene ilişkin bir açıklamadır."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsanları bir tür veya topluluk olarak anlatırken de bu türün tek bir üyesini belirtirken de kullanılabilir.","boundary_detail":"Dal, insan türünü ve onun tekil ya da toplu üyelerini kapsar; yakınlık duygusunu, duyusal algıyı ve insana dönük yanı kapsamaz.","branch_image_ar":"ظهور الإنسان المخالف للتوحش والجن","concept_gloss":"insan türü ve bu türden bir kişi","contextual_glosses":[{"applicability":"Türün üyeleri topluca veya görünmeyen varlıklar sınıfının karşıtı olarak anıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan türünün toplu olarak adlandırılmasını açık ve doğal biçimde korur."},"facet_ids":["F001"],"text":"insanlar","usage_role":"general"},{"applicability":"Bağlam türün tek bir üyesini veya herhangi bir kimseyi gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan topluluğundan tek bir üyenin belirtilmesini korur."},"facet_ids":["F001"],"text":"bir kişi","usage_role":"contextual"}],"definition":"Görünmeyen varlıklar sınıfının karşısında yer alan insan türünü, bu türün topluluğunu ya da tek bir üyesini belirtir. İnsanların görünür oluşu, bu adlandırma için aktarılan bir gerekçedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan türünü, insanların oluşturduğu topluluğu veya bu türün tek bir üyesini görünmeyen varlıklar sınıfının karşısında adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Adlandırmanın insanların duyularla görünür oluşuna bağlanması, anlamın özü değil kökene ilişkin bir açıklamadır."}],"identity_rationale":"Kaynak ifadesi, görünmeyen varlıklar sınıfının karşısındaki insan türünü, bu türün topluluğunu ve tek bir üyesini birlikte gösterir. Görünür olma açıklaması adlandırma gerekçesidir; insan olmanın kurucu tanımı değildir. Evde kimsenin bulunmadığını bildiren kalıp ise dal çekirdeğine genellenemez ve yalnızca kendi sözcüksel biriminde korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"insanlar; insan topluluğu"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"insan; insan türü"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"insan topluluğunun bir üyesi; insana veya insanlara ait"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"insanlar; insan toplulukları"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"insanlar; halk"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"evde hiç kimse yok"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"belirli bir ağızda insan ve onun çoğulu"}],"lexicalization_note":"Çıplak biçimlerdeki insan ve insan topluluğu anlamı dal çekirdeğidir; evde hiç kimse bulunmadığını anlatan kalıp ayrı tutulur ve çekirdeğe yeni bir genel anlam katmaz.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı. Yalnız insanı adlandırma sınırını yaratılmışlar kapsamından ve yakınlık duygusundan ayıran, okuyucu için en yararlı üç karşıtlık yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yer değiştirme yalnız insanı genel olarak adlandıran bağlamlarda mümkündür. Odak dalın görünmeyen varlıklarla sınıf karşıtlığı, komşunun ise görünür beden yönü kendi sınırında kalır.","focus_only":"Odak dal, insanları görünmeyen varlıklar sınıfının karşısında bir tür olarak kurar ve görünürlüğe dayalı bir adlandırma açıklaması taşır.","gloss":"insan türünü iki ayrı yönden adlandırma","neighbor_only":"Komşu dal, insanı görünür ten ve yaratılmış beden yönüyle adlandırır; tekil, çoğul, erkek ve kadın kapsamını özellikle öne çıkarır.","neighbor_ref":"root_000120/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da insanı hem tür hem bu türün üyesi olarak gösterebilir."},{"boundary_match":"partial","distinction":"Komşunun genel yaratılmışlar kapsamı odak dala taşınamaz; odak dal da yalnız insanları belirttiği için bütün yaratılmışların yerine kullanılamaz.","focus_only":"Odak dal yalnız insan türünü ve bu türün tekil ya da toplu üyelerini belirtir.","gloss":"insan türü ile bütün yaratılmışlar ayrımı","neighbor_only":"Komşu dal yeryüzündeki bütün yaratılmışları kapsayabilir ve bazı yorumlarda insanlarla görünmeyen varlıkları birlikte içerir.","neighbor_ref":"root_000061/B001","relation_type":"near_neighbor","shared_zone":"İnsanlar iki dalın gönderim alanında da bulunabilir."},{"boundary_match":"field_only","distinction":"Birinde insanın kim olduğu adlandırılır, diğerinde bir kişi ya da şey karşısındaki duygusal durum anlatılır; sıradan bağlamlarda birbirlerinin yerine geçmezler.","focus_only":"Odak dal insan türünü ve bu türün üyelerini adlandırır.","gloss":"insan adı ile yakınlık duygusu ayrımı","neighbor_only":"Komşu dal yabancılık ve ürkme duygusunun kalkmasını, yakınlık ve rahatlık oluşmasını anlatır.","neighbor_ref":"root_000059/B003","relation_type":"same_field","shared_zone":"Her iki dalda da insan, temel gönderim noktası veya deneyim sahibi olabilir."}],"source_phrase_ar":"الإنس خلاف الجن وسموا لظهورهم (maqayis;mufradat)؛ الإنس البشر والواحد إنسي والجمع أناسي (sihah)؛ الإنس جماعة الناس والأناسي جماع (tahdhib)","source_summary":"Aktarımlar, dalın insan türünü hem topluluk hem tek kişi olarak gösterebildiğinde ve görünmeyen varlıklar sınıfıyla karşıtlık kurduğunda birleşir. Görünürlük, ortak anlamdan çok adlandırmanın gerekçesi olarak sunulur.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الإنس والبشر والناس والأناسي والإنسان من حيث الجماعة أو الواحد، وما بالدار أنيس بمعنى أحد.","what_is_not_ar":"لا يدخل مجرد الاستئناس النفسي ولا الإيناس بمعنى الإبصار ولا الجانب الإنسي إلا بدليل."},"support_links":[]},{"boundary":"Dal duyusal olarak fark etmeyi ve belirtilen bağlamlardaki işitme, sezme ve bakıp araştırma kullanımlarını kapsar; yakınlık ve rahatlık duygusunu kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B002","candidate_links":[{"candidate_id":"cand_9d8949e8b05a172f4f31","lane":"micro"},{"candidate_id":"cand_7451b057185aa50c0afa","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:5:5:2","qac_word_ref":"114:5:5","surface_ar":"نَّاسِ"}],"gloss":"görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi gözle görerek fark etmeyi veya seçmeyi anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli bir ses nesnesiyle kullanıldığında o sesi işitmeyi anlatır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kimsedeki olgunluk belirtisini bilip ayırt etmeyi veya kaygı veren bir durumu duyularla sezmeyi anlatabilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Çevreye bakıp dikkatle araştırarak birinin bulunup bulunmadığını anlamaya çalışma kullanımını taşır."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın görme çekirdeğiyle birlikte yalnız belirtilen bağlamlarda ortaya çıkan işitme, sezme ve çevreyi araştırma uzantılarını topluca verir.","boundary_detail":"Dal duyusal olarak fark etmeyi ve belirtilen bağlamlardaki işitme, sezme ve bakıp araştırma kullanımlarını kapsar; yakınlık ve rahatlık duygusunu kapsamaz.","branch_image_ar":"إيناس الشيء برؤية أو إحساس أو سماع","concept_gloss":"görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma","contextual_glosses":[{"applicability":"Nesnenin gözle seçildiği veya görüldüğü temel kullanımda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gözle görme ve görüleni fark etme işlemlerini birlikte korur."},"facet_ids":["F001"],"text":"görüp fark etmek","usage_role":"general"},{"applicability":"Nesne açıkça bir ses olduğunda kullanılan bağlama bağlı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sesin kulakla algılanması biçimindeki özel kullanımı korur."},"facet_ids":["F002"],"text":"sesi işitmek","usage_role":"contextual"},{"applicability":"Bir kimsedeki olgunluk veya kaygı uyandıran durum gibi bir belirtinin ayırt edildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Duyusal belirtiden bir durumun varlığını anlayıp ayırt etmeyi korur."},"facet_ids":["F003"],"text":"belirtiyi sezmek","usage_role":"contextual"},{"applicability":"Çevreyi gözleyip birinin bulunup bulunmadığını anlamaya çalışma kullanımında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dikkatle bakma ile birini bulmaya yönelik araştırmayı birlikte korur."},"facet_ids":["F004"],"text":"bakıp araştırmak","usage_role":"explanatory"}],"definition":"Bir şeyi görüp fark etmeyi anlatır. Belirli kullanımlarda bir sesi işitmeye, bir kimsedeki olgunluk belirtisini ya da kaygı veren bir durumu sezmeye ve çevreye bakarak birinin bulunup bulunmadığını araştırmaya uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi gözle görerek fark etmeyi veya seçmeyi anlatır."},{"facet_id":"F002","role":"extension","statement":"Belirli bir ses nesnesiyle kullanıldığında o sesi işitmeyi anlatır."},{"facet_id":"F003","role":"extension","statement":"Bir kimsedeki olgunluk belirtisini bilip ayırt etmeyi veya kaygı veren bir durumu duyularla sezmeyi anlatabilir."},{"facet_id":"F004","role":"associated_use","statement":"Çevreye bakıp dikkatle araştırarak birinin bulunup bulunmadığını anlamaya çalışma kullanımını taşır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Zamanla gelişen yakınlık ve yabancılığın kalkması anlamını ekler.","collision":"Yakınlık ve rahatlık bildiren ayrı dalla karışır.","fit":"displacement","loses":"Görme, işitme, belirtiyi sezme ve çevreye bakıp araştırma işlemlerini siler.","preserves":"Bir kişi veya şeye yönelen deneyim fikrini çok genel biçimde korur."},"text":"alışmak"}],"identity_rationale":"Kaynak ifadesi görmeyi temel alır, fakat belirli kullanımlarda işitmeyi, bir belirtiyi anlayıp ayırt etmeyi ve çevreye bakarak birini aramayı da aynı dalda aktarır. Bu yüzden dal genel ve sınırsız bir algı yetisi diye tanımlanamaz; her uzantı kendi bağlamına bağlı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir şeyi görmek ve fark etmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"sesi işitmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"onda olgunluk belirtisi görmek ve bunu anlamak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ürken yabani hayvanın birini sezip çevreye bakınması"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"çevreye bakıp birinin olup olmadığını araştırmak"}],"lexicalization_note":"Görüp fark etme çekirdeği ile ses işitme, olgunluk belirtisini ayırt etme ve çevreye bakıp araştırma kalıpları ayrı tutulur; kalıplardaki kapsam çıplak biçime genellenmez.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi. Görme, genel duyumsama ve yakınlık duygusuyla karışma olasılığı en yüksek üç sınır yayımlandı; diğer adaylar dalı açıklayan ek bir karşıtlık sağlamadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yalnız görsel algı bağlamında yakın karşılık olabilirler. Odak dalın işitme ve belirtiyi sezme uzantıları komşuya, komşunun göz organı anlamı da odak dala taşınamaz.","focus_only":"Odak dal, görmenin yanında belirli yapılarda işitme, belirti sezme ve çevreyi araştırma uzantılarını taşır.","gloss":"fark etme ile gözle görme ayrımı","neighbor_only":"Komşu dal göz organını, görme duyusunu ve göz açıp dikkatle bakma eylemini kendi başına kapsar.","neighbor_ref":"root_000121/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi göz yoluyla görüp seçme alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu daha genel bir duyu alanıdır; odak dalın uzantıları ise kanıtlanan nesne ve yapılara bağlıdır. Bu nedenle genel duyumsama her durumda odak ifadeyle karşılanamaz.","focus_only":"Odak dal görmeyi merkez alır ve yalnız belirli söz çevrelerinde işitme, sezme ve araştırmaya uzanır.","gloss":"belirli algı kullanımları ile genel duyumsama","neighbor_only":"Komşu dal herhangi bir duyu aracılığıyla algılama, bilme ve varlığını saptama alanını genel olarak kapsar.","neighbor_ref":"root_000321/B002","relation_type":"near_synonym","shared_zone":"Her ikisi de bir şeyin duyular aracılığıyla fark edilmesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal algısal saptamayı, komşu dal ise karşılaşma sonrasındaki duygusal rahatlığı bildirir. Algı gerçekleşebilir ama yakınlık doğmayabilir.","focus_only":"Odak dal bir nesneyi görme, işitme veya belirtilerinden sezme eylemini anlatır.","gloss":"duyusal fark etme ile yakınlık hissetme","neighbor_only":"Komşu dal bir kişi ya da şey karşısında yabancılık ve ürkme duymayıp yakınlık hissetmeyi anlatır.","neighbor_ref":"root_000059/B003","relation_type":"near_neighbor","shared_zone":"Bir kişi veya şeyle karşılaşma iki anlam alanının ortak başlangıç durumu olabilir."}],"source_phrase_ar":"آنست الشيء إذا رأيته وآنسته إذا سمعته (maqayis)؛ آنسته أبصرته وآنست الصوت سمعته وآنست منه رشدا علمته (sihah)؛ آنس من جانب يعني أبصر نارا والاستئناس النظر وأحس بما رابه (tahdhib)؛ فإن آنستم منهم رشدا أي أبصرتم وآنست نارا (mufradat)","source_summary":"Aktarılan anlam alanının merkezi görüp fark etmektir. Aynı ifade ailesi belirli nesne ve yapılarda işitme, bir belirtiyi anlayıp ayırt etme, kaygı veren şeyi sezme ve bakıp araştırma yönlerinde kullanılır; bunlar sınırsız bir genel algı anlamı oluşturmaz.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه آنس الشيء إذا أبصره أو رآه، وآنس الصوت إذا سمعه، وأحس الفزع أو وجد الشيء في نفسه، والاستئناس بمعنى النظر والتبصر.","what_is_not_ar":"لا يدخل الأنس بمعنى الراحة والمؤالفة ولا الإنس بمعنى البشر إلا بقرينة."},"support_links":["sup_0c8db3cf8704202747d7","sup_1b7f8f0ac53eb4f64837"]},{"boundary":"Dal duygusal yakınlık, rahatlık ve bunları sağlayan varlıkları kapsar; insan türünün adı, duyusal fark etme ve insana bakan yan anlamları dışarıda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B003","candidate_links":[{"candidate_id":"cand_aeba23498e823c5c102a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:5:5:2","qac_word_ref":"114:5:5","surface_ar":"نَّاسِ"}],"gloss":"yabancılık duymadan yakınlık ve rahatlık hissetme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi ya da şey karşısında yabancılık ve ürkme duygusunun kalkıp yakınlık, rahatlık veya sevinç oluşmasını anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişiye arkadaşlık ederek veya yanında bulunarak yabancılık duygusunu gideren kişi ya da şeyi adlandırır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsana alışık ve saldırgan olmayan hayvanı, özellikle bu nitelikteki köpeği anlatabilir."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi veya şeyin ürkütücü ve yabancı gelmemesi, tersine yakınlık ve iç rahatlığı vermesi anlatıldığında dalın çekirdeğini karşılar.","boundary_detail":"Dal duygusal yakınlık, rahatlık ve bunları sağlayan varlıkları kapsar; insan türünün adı, duyusal fark etme ve insana bakan yan anlamları dışarıda kalır.","branch_image_ar":"الأنس الذي يزيل الوحشة","concept_gloss":"yabancılık duymadan yakınlık ve rahatlık hissetme","contextual_glosses":[{"applicability":"Bir kişi veya şey karşısındaki yabancılık duygusunun kalktığı temel durumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alışma sonucunda yabancılığın kalkmasını ve yakınlık oluşmasını korur."},"facet_ids":["F001"],"text":"alışıp yakınlık duymak","usage_role":"general"},{"applicability":"Yalnızlığı veya ürkmeyi gideren bir arkadaş, nesne ya da başka bir dayanak adlandırıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakınlık ve güven veren kaynağın kişiyle sınırlı olmamasını korur."},"facet_ids":["F002"],"text":"yanında rahatlık veren kişi veya şey","usage_role":"explanatory"},{"applicability":"İnsandan kaçmayan ve ısırıp saldırmayan evcil ya da alışkın hayvan için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın insana alışıklığını ve saldırgan olmama sınırını birlikte korur."},"facet_ids":["F003"],"text":"insana alışık ve saldırgan olmayan","usage_role":"contextual"}],"definition":"Bir kişi ya da şey karşısında yabancılık, ürkme veya kaçınma duymayıp yakınlık, rahatlık ve sevinç hissetmeyi anlatır. Bu duyguyu veren kişi veya şeye ve insana alışık, saldırgan olmayan hayvana da aktarılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi ya da şey karşısında yabancılık ve ürkme duygusunun kalkıp yakınlık, rahatlık veya sevinç oluşmasını anlatır."},{"facet_id":"F002","role":"extension","statement":"Kişiye arkadaşlık ederek veya yanında bulunarak yabancılık duygusunu gideren kişi ya da şeyi adlandırır."},{"facet_id":"F003","role":"specialization","statement":"İnsana alışık ve saldırgan olmayan hayvanı, özellikle bu nitelikteki köpeği anlatabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Her türlü sevincin bu dala ait olduğu izlenimini verebilir.","fit":"narrowing","loses":"Yabancılığın ve ürkmenin kalkmasını, alışmayı ve rahatlık veren kişi ya da şey kapsamını kaybeder.","preserves":"Yakınlık durumunda ortaya çıkabilen olumlu duyguyu korur."},"text":"sevinç"}],"identity_rationale":"Kaynak ifadesi, bir kişi veya şey karşısında yabancılık ve ürkme duygusunun kalkmasını çekirdek anlam olarak verir. Yakınlık ve sevinç, rahatlık veren kişi ya da şey ve insana alışık saldırgan olmayan hayvan kullanımları bu çekirdekten bağımlı biçimde açıklanabilir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yakınlık ve rahatlık; yabancılık duymama"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"birine alışıp onun yanında sevinmek"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"biriyle yakınlık kurmak ve onsuz kendini yalnız hissetmek"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yakın arkadaş; rahatlık veren kişi veya şey"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yakınlıktan ve söyleşiden hoşlanan genç kadın"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"insana alışık, saldırgan olmayan köpek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"gece yolcusuna veya konaklayana güven veren ateş"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"sahibine güven veren bütün silahlar; zırh, miğfer, koruyucu örtü ve kalkan gibi savunma donanımları"}],"lexicalization_note":"Yabancılık duymama çekirdeği ile rahatlık veren kişi veya şey ve insana alışık hayvan gibi özelleşmiş biçimler ayrı katmanlarda tutulur; özel biçimler bütün dalı tanımlamaz.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı. Alışıp bağlanma, özel dostluk ve insan türünü adlandırma alanları dal sınırını en açık gösterdiği için yalnız bu üç ayrım yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın belirleyici yönü yabancılık ve ürkmenin karşıtı olan iç rahatlığıdır; komşu dal süreklilik, bağlanma ve alışkanlık yönlerini odaktan daha geniş taşır.","focus_only":"Odak dal yabancılık ve ürkmenin kalkmasıyla oluşan yakınlık ve rahatlığı, ayrıca bunu sağlayan varlığı öne çıkarır.","gloss":"yakınlık rahatlığı ile alışıp bağlanma","neighbor_only":"Komşu dal bir kişi, yer veya şeye alışmayı, ona bağlanmayı, onunla sürekli bulunmayı ve hayvanın evcilleşmesini daha geniş biçimde kapsar.","neighbor_ref":"root_000045/B005","relation_type":"near_synonym","shared_zone":"İki dal da bir kişi, yer, şey veya hayvana karşı yabancılığın azalmasını anlatabilir."},{"boundary_match":"partial","distinction":"Her rahatlık veren yakınlık özel ve arı bir dostluk değildir. Komşunun karşılıklı dostluk sınırı odak dalın nesne ve hayvan uzantılarına uygulanamaz.","focus_only":"Odak dal kişi dışındaki şeylerin verdiği rahatlığı ve insana alışık hayvanı da kapsayabilir.","gloss":"rahatlık veren yakınlık ile özel dostluk","neighbor_only":"Komşu dal seçilmiş kişiler arasındaki arı, özel ve karşılıklı dostluk bağını anlatır.","neighbor_ref":"root_000430/B007","relation_type":"near_neighbor","shared_zone":"İki dal da kişiler arasında yakınlık ve içtenlik bulunan durumlarda buluşur."},{"boundary_match":"field_only","distinction":"Odak dal bir duygusal ilişkiyi, komşu dal ise bir varlık sınıfını adlandırır. İnsan olmak yakınlık hissetmeyi gerektirmez ve iki ifade birbirinin yerine geçmez.","focus_only":"Odak dal yabancılığın kalkmasıyla doğan duygusal yakınlığı ve rahatlığı anlatır.","gloss":"yakınlık durumu ile insan adı ayrımı","neighbor_only":"Komşu dal insan türünü, insan topluluğunu veya bu türden tek bir kişiyi adlandırır.","neighbor_ref":"root_000059/B001","relation_type":"same_field","shared_zone":"İnsan, iki dalda da temel katılımcı veya gönderim noktasıdır."}],"source_phrase_ar":"الأنس أنس الإنسان بالشيء إذا لم يستوحش منه (maqayis)؛ الإيناس خلاف الإيحاش والإنس خلاف الوحشة والأنيس المؤانس وكل ما يؤنس به (sihah)؛ أنست بفلان أي فرحت به والأنس والاستئناس هو التأنس وكلب أنوس نقيض العقور (tahdhib)؛ الأنس خلاف النفور ولكل ما يؤنس به (mufradat)","source_summary":"Ortak çekirdek, yabancılık ve kaçınmanın karşıtı olan yakınlık ve rahatlıktır. Bu durum birine alışıp onun yanında sevinmeyi, rahatlık veren kişi veya şeyi ve insana alışık saldırgan olmayan hayvanı kapsayacak biçimde genişler.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه أنس الإنسان بالشيء أو بفلان، المؤانسة والتأنيس، الأنيس وكل ما يؤنس به، الفرح بالقرب والحديث، والحيوان الأنوس غير العقور.","what_is_not_ar":"لا يدخل الإنس بمعنى البشر ولا الإيناس بمعنى الإبصار ولا الجانب الإنسي إلا بدليل."},"support_links":["sup_56f18f1d10bff16cca6c"]},{"boundary":"Dal, bir nesnenin insana veya kullanıcıya bakan yanını belirtir; salt sol, salt sağ, genel ön taraf ya da insanın kendisi anlamına gelmez.","branch_kind":"bare","branch_ref":"root_000059/B004","candidate_links":[{"candidate_id":"cand_aeba23498e823c5c102a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:5:5:2","qac_word_ref":"114:5:5","surface_ar":"نَّاسِ"}],"gloss":"insana dönük yan","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin insana en yakın olan veya insana doğru bakan yanını belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvanda binicinin bulunduğu, binme ve sağma işlemlerinde insana yakın olan yanı anlatır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yayda okçuya doğru bakan ve kullanıcının karşısında bulunan yanı anlatır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İnsana yakın yan bazı aktarımda sol, başka bir aktarımda sağ diye belirlenir; yönün özü bu değişken tanımlardan bağımsızdır."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin yönü, ona yaklaşan veya onu kullanan insana göre belirlendiğinde dalın ortak çekirdeğini verir.","boundary_detail":"Dal, bir nesnenin insana veya kullanıcıya bakan yanını belirtir; salt sol, salt sağ, genel ön taraf ya da insanın kendisi anlamına gelmez.","branch_image_ar":"الجانب الإنسي المقبل على الإنسان","concept_gloss":"insana dönük yan","contextual_glosses":[{"applicability":"Hayvanın binme ve sağma sırasında insana yakın kalan yanı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın yanını biniciyle kurduğu işlevsel ilişkiye göre belirler."},"facet_ids":["F002"],"text":"biniciye yakın yan","usage_role":"contextual"},{"applicability":"Yayın kullanım sırasında okçuya doğru dönük olan yüzü belirtilirken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yay yüzünün yönünü okçunun konumuna göre belirleme özelliğini korur."},"facet_ids":["F003"],"text":"okçuya bakan yay yüzü","usage_role":"explanatory"}],"definition":"Bir nesnenin insana, kullanıcıya veya onun bulunduğu yöne bakan yanıdır. Hayvan ve yay üzerinde işlevsel ilişkiyle belirlenir; bu yanın sabit olarak sol ya da sağ sayılması konusunda aktarım uyuşmazlığı vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin insana en yakın olan veya insana doğru bakan yanını belirtir."},{"facet_id":"F002","role":"specialization","statement":"Hayvanda binicinin bulunduğu, binme ve sağma işlemlerinde insana yakın olan yanı anlatır."},{"facet_id":"F003","role":"specialization","statement":"Yayda okçuya doğru bakan ve kullanıcının karşısında bulunan yanı anlatır."},{"facet_id":"F004","role":"source_variant","statement":"İnsana yakın yan bazı aktarımda sol, başka bir aktarımda sağ diye belirlenir; yönün özü bu değişken tanımlardan bağımsızdır."}],"identity_rationale":"Kaynak ifadesinin güvenilir çekirdeği, bir şeyin insana veya onu kullanan kişiye dönük ve yakın olan yanıdır. Bu yanın solda mı sağda mı olduğu konusunda aktarımlar uyuşmaz; hayvan ve yay örnekleri yönü işlevsel ilişkiyle belirler. Bu nedenle sabit bir sağ-sol tanımı dalın özüne konamaz.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir şeyin insana bakan veya en yakın olan yanı"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yayın okçuya bakan yüzü"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"hayvanın biniciye yakın olan yanı"}],"lexicalization_note":"Tanım çıplak dalın insana dönük yan çekirdeğiyle sınırlıdır. Hayvan ve yay uygulamaları bu çekirdeğin örneklenmesidir; yalnız bu kullanımlardan yeni bir genel yön anlamı çıkarılmaz.","neighbor_coverage_note":"Adayların tamamı incelendi. Genel ön taraf, yönelme eylemi ve arka bölümle kurulan karşılaştırmalar insana göre belirlenen yanın sınırını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda yön, insanın nesneyle kurduğu konum veya kullanım ilişkisine bağlıdır. Komşu dalın genel ön ve yakın anlamları bu özel bağı gerektirmez.","focus_only":"Odak dal bir nesnenin insana veya onu kullanan kişiye dönük yanını ilişkiye göre belirler.","gloss":"insana dönük yan ile genel ön taraf","neighbor_only":"Komşu dal genel olarak ön, önde, yakın veya karşıda bulunma yönlerini kişiye bağlı bir kullanım ilişkisi gerektirmeden anlatır.","neighbor_ref":"root_000053/B011","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin bakana göre karşıda veya önde kalan bölümünü gösterebilir."},{"boundary_match":"partial","distinction":"Bir nesnenin insana dönük yanı bir bölüm adıdır; komşu ise dönme veya yönelme olayını anlatır. Sonuç konumu ile o konuma geçiş eylemi birbirinin yerine kullanılamaz.","focus_only":"Odak dal, yönelme tamamlandıktan sonra insana dönük olan sabit yanı adlandırır.","gloss":"dönük yan ile yönelme eylemi","neighbor_only":"Komşu dal yüz, baş, el, kap veya hayvanın bir hedefe doğru dönmesi ve yönelmesi eylemini anlatır.","neighbor_ref":"root_001263/B003","relation_type":"near_neighbor","shared_zone":"İki dal da bir kişi veya hedefe doğru bakma yönünü içerir."},{"boundary_match":"partial","distinction":"Bağlama göre karşıt görünebilseler de odak dal her zaman geometrik ön yüz değildir ve bu yüzden düzenli bir karşıt çift oluşturmaz; belirleyici ölçüt insana yakınlıktır.","focus_only":"Odak dal insana veya kullanıcıya yakın ve ona bakan yanı gösterir.","gloss":"insana bakan yan ile arka taraf","neighbor_only":"Komşu dal bir şeyin arkasında kalan, yüzünün karşıtı olan arka bölümünü gösterir.","neighbor_ref":"root_000458/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir nesnenin başka bir yöne göre belirlenen bölümünü adlandırır."}],"source_phrase_ar":"الإنسي الأيسر من كل شيء وقيل الأيمن وما أقبل منهما على الإنسان فهو إنسي وإنسي القوس ما أقبل عليك منها (sihah)؛ الإنسي من الدواب الجانب الأيسر الذي منه يركب ويحتلب ومن الإنسان الجانب الذي يلي الرجل الأخرى (tahdhib)؛ إنسي الدابة للجانب الذي يلي الراكب وإنسي القوس للجانب الذي يقبل على الرامي (mufradat)","source_summary":"Ortak anlam, nesnenin insana veya kullanıcıya dönük yanıdır; hayvanda biniciye, yayda okçuya göre belirlenir. İnsan bedenindeki tekil uygulamada öteki bacağa bakan yan kastedilir. Bu yanın solda mı sağda mı bulunduğuna ilişkin anlatımlar ayrıştığı için genel tanım sabit bir yön seçmez.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه إنسي الدابة والقوس وكل شيئين: ما يلي الإنسان أو يقبل على الراكب أو الرامي، في مقابلة الوحشي.","what_is_not_ar":"لا يدخل الإنسان نفسه ولا الأنس النفسي ولا الإبصار."},"support_links":["sup_56f18f1d10bff16cca6c"]},{"boundary":"Dal göz bebeğinde görülen küçük görüntüyü, ayrıca ayrı bir aktarım olarak parmak ucunu kapsar; gözün kendisini veya genel insan türünü belirtmez.","branch_kind":"bare","branch_ref":"root_000059/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:5:5:2","qac_word_ref":"114:5:5","surface_ar":"نَّاسِ"}],"gloss":"göz bebeğinde görülen küçük yansıma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Göz bebeğinin kara bölümünde görülen küçük insan biçimli görüntüyü veya yansımayı adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı bir aktarımda parmak ucu veya eldeki parmak ucunu anlatan kullanım da aynı adla verilir."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir bakanın göz bebeğinde beliren küçük insan biçimli görüntü adlandırıldığında dalın ortak ve temel anlamını karşılar.","boundary_detail":"Dal göz bebeğinde görülen küçük görüntüyü, ayrıca ayrı bir aktarım olarak parmak ucunu kapsar; gözün kendisini veya genel insan türünü belirtmez.","branch_image_ar":"إنسان العين وصورة الإنسان في السواد","concept_gloss":"göz bebeğinde görülen küçük yansıma","contextual_glosses":[{"applicability":"Yansımanın insan biçiminde algılanması özellikle belirtilmek istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Görüntünün göz bebeğinde bulunmasını ve küçük insan biçiminde görünmesini korur."},"facet_ids":["F001"],"text":"göz bebeğindeki küçük insan görüntüsü","usage_role":"explanatory"},{"applicability":"Yalnız parmak ucunu aynı adla veren ayrı kaynak kullanımında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Göz anlamından bağımsız olan parmak ucu kullanımını doğrudan korur."},"facet_ids":["F002"],"text":"parmak ucu","usage_role":"contextual"}],"definition":"Gözün kara bölümünde görülen küçük insan biçimli görüntü veya yansımadır. Ayrı bir kaynak kullanımında aynı ad parmak ucuna da verilir, ancak bu kullanım göz görüntüsü çekirdeğini değiştirmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Göz bebeğinin kara bölümünde görülen küçük insan biçimli görüntüyü veya yansımayı adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Ayrı bir aktarımda parmak ucu veya eldeki parmak ucunu anlatan kullanım da aynı adla verilir."}],"identity_rationale":"Kaynak ifadesinin ortak çekirdeği, gözün kara bölümünde görülen küçük insan biçimli görüntü veya yansımadır. Parmak ucu anlamı tek aktarım içinde eklenir ve gözdeki görüntünün kurucu parçası değildir; bağımlı bir kaynak varyantı olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"göz bebeğinde görülen küçük görüntü veya yansıma"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"göz bebeklerinde görülen küçük görüntüler"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"parmak ucu; eldeki parmak ucunu anlatan kullanım"}],"lexicalization_note":"Çıplak dalın çekirdeği gözün kara bölümündeki küçük görüntüdür. Parmak ucu aktarımı bağımlı bir varyanttır; gözle ilgili belirli biçimlerden genel görüntü veya genel insan anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi. Anatomik göz bebeği, genel tasvir ve göz organı karşılaştırmaları görüntünün yerini ve türünü en iyi sınırladığı için bu üçü yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Komşu anatomik bölümün kendisidir; odak dal ise o bölümde görülen görüntüdür. Taşıyıcı yapı ile üzerinde beliren yansıma birbirinin yerine kullanılamaz.","focus_only":"Odak dal göz bebeğinde görülen küçük insan biçimli görüntüyü veya yansımayı adlandırır.","gloss":"göz bebeği ile göz bebeğindeki yansıma","neighbor_only":"Komşu dal göz bebeğinin kendisini, onun kara bölümünü ve anatomik yapısını adlandırır.","neighbor_ref":"root_000300/B002","relation_type":"same_field","shared_zone":"İki dal aynı göz bölgesine gönderimde bulunur."},{"boundary_match":"partial","distinction":"Odak görüntü göz bebeğindeki belirli yansımadır; komşu ise konum ve oluşum biçimi bakımından çok daha genel tasvirleri kapsar. Her tasvir gözdeki yansıma değildir.","focus_only":"Odak dal yalnız göz bebeğinde beliren küçük insan biçimli görüntüyü ve ayrı bir parmak ucu varyantını kapsar.","gloss":"gözdeki yansıma ile genel tasvir","neighbor_only":"Komşu dal resim, model, heykel veya başka bir varlığa göre biçimlendirilmiş genel örnekleri kapsar.","neighbor_ref":"root_001397/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal başka bir varlığın görünüşünü taşıyan bir görüntüyü anlatabilir."},{"boundary_match":"field_only","distinction":"Göz, görmeyi sağlayan organdır; odak dal ise gözde görülen yansımadır. Organın adı yansımanın, yansımanın adı da organın genel karşılığı değildir.","focus_only":"Odak dal gören gözün içinde beliren küçük görüntüyü adlandırır.","gloss":"göz organı ile içindeki küçük görüntü","neighbor_only":"Komşu dal görme organı olan gözün kendisini ve onun görme işlevini adlandırır.","neighbor_ref":"root_001069/B001","relation_type":"same_field","shared_zone":"Her iki dal göz ve görme alanına aittir."}],"source_phrase_ar":"إنسان العين صبيها الذي في السواد (maqayis)؛ إنسان العين المثال الذي يرى في السواد أي سواد العين (sihah)؛ الإنسان أيضا إنسان العين وجمعه أناسي والإنسان الأنملة (tahdhib)","source_summary":"Ortak aktarım, göz bebeğinin kara bölümünde görülen küçük görüntüyü bir insan biçimi olarak tanımlar. Buna ek olarak parmak ucu anlamı da bildirilir, fakat bu ek kullanım gözdeki yansıma çekirdeğinden ayrı tutulur.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه إنسان العين: المثال أو الصبي الذي يرى في سواد العين، وما ألحقه تهذيب اللغة من الأنملة أو إنسان الكف.","what_is_not_ar":"لا يدخل الإنسان بمعنى البشر عموما ولا الأنس بمعنى الراحة."},"support_links":[]},{"boundary":"Dal yalnız belirtilen söz kuruluşlarında kişinin kendisini veya seçkin yakınını gösterir; genel insan, gerçek evlatlık ve her türlü arkadaşlık anlamına genişletilemez.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B006","candidate_links":[{"candidate_id":"cand_b95e4d1f7ff65b7fc9d2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:5:5:2","qac_word_ref":"114:5:5","surface_ar":"نَّاسِ"}],"gloss":"belirli sözlerde kişinin kendisi veya seçilmiş yakını","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiye kendi durumunu soran belirli kuruluşta muhatabın kendisini gösterir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişiye bağlanarak söylendiğinde onun seçilmiş yakınını, özel arkadaşını veya sırdaşını belirtir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı anlam çevresindeki paralel adlar yakın dostu, içten arkadaşı ve oturup konuşulan kişiyi gösterebilir."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kaynakta gösterilen soru ve kişi bağlantısı kuruluşlarını topluca açıklarken kullanılabilir; genel bir kişi ya da akraba adı değildir.","boundary_detail":"Dal yalnız belirtilen söz kuruluşlarında kişinin kendisini veya seçkin yakınını gösterir; genel insan, gerçek evlatlık ve her türlü arkadaşlık anlamına genişletilemez.","branch_image_ar":"ابن الإنس للنفس والصفوة","concept_gloss":"belirli sözlerde kişinin kendisi veya seçilmiş yakını","contextual_glosses":[{"applicability":"Muhataba kendi durumunun nasıl olduğu sorulduğunda doğal Türkçe karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sorunun muhatabın kendi durumuna yönelmesini korur."},"facet_ids":["F001"],"text":"kendin; nasılsın","usage_role":"contextual"},{"applicability":"Bir kişinin seçip özel tuttuğu yakın arkadaş veya sırdaş anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakın kişinin seçilmiş, özel ve güvenilen biri olmasını korur."},"facet_ids":["F002"],"text":"onun en yakını ve sırdaşı","usage_role":"contextual"},{"applicability":"Yakın dost, içten arkadaş ve birlikte oturup konuşulan kişi için sıralanan paralel adları açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakınlık, dostluk ve sürekli görüşme ilişkilerini birlikte korur."},"facet_ids":["F003"],"text":"yakın dostum ve görüşme arkadaşım","usage_role":"explanatory"}],"definition":"Belirli bir soru kuruluşunda muhatabın kendisini ve durumunu, başka bir kişiyle kurulan adlandırmada ise onun seçilmiş yakınını, sırdaşını veya sürekli görüştüğü arkadaşını belirtir. İki kullanım aynı kuruluş ailesinde bulunsa da katılımcı ilişkileri ayrıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiye kendi durumunu soran belirli kuruluşta muhatabın kendisini gösterir."},{"facet_id":"F002","role":"core","statement":"Bir kişiye bağlanarak söylendiğinde onun seçilmiş yakınını, özel arkadaşını veya sırdaşını belirtir."},{"facet_id":"F003","role":"associated_use","statement":"Aynı anlam çevresindeki paralel adlar yakın dostu, içten arkadaşı ve oturup konuşulan kişiyi gösterebilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Gerçek bir baba ile erkek çocuk arasındaki soy ilişkisini ekler.","collision":"Sözün amaçlanan kişi ilişkisini gerçek akrabalıkla karıştırır.","fit":"displacement","loses":"Kişinin kendisini veya seçilmiş yakınını gösteren kalıplaşmış gönderimi kaybeder.","preserves":"Kuruluşun yüzeyindeki çocuk ve soy ilişkisi çağrışımını korur."},"text":"oğlu"}],"identity_rationale":"Kaynak ifadesi iki ayrı kalıplaşmış ilişkiyi açıkça ayırır: kişiye kendi durumunu soran sözde kişinin kendisi, bir başkasına bağlanan sözde ise seçilmiş yakın ve sırdaş kastedilir. Yakın arkadaş ve oturup konuşulan kişi için verilen paralel adlar ikinci alanı destekler.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"kendin; kendi durumun nasıl"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"onun seçkin yakını ve sırdaşı"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"yakınım, içten dostum ve görüşme arkadaşım"}],"lexicalization_note":"Kişinin kendisini soran kuruluş, seçilmiş yakını belirten kuruluş ve yakın arkadaş adları ayrı tutulur. Bunların hiçbiri çıplak biçime genel kişi veya akrabalık anlamı olarak taşınmaz.","neighbor_coverage_note":"Aday kartların tamamı incelendi. Kişinin kendisini gösteren başka kuruluş, iç çevre ve genel dostluk alanları iki ayrı gönderimi en iyi sınırlandırdığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ortak gönderim yalnız benlik anlamındadır; kuruluşlar değiştirilemez. Odak dalın seçilmiş yakın ve sırdaş anlamı komşuda bulunmaz.","focus_only":"Odak dal kişinin kendisini belirli bir soru kuruluşunda gösterir ve ayrıca seçilmiş yakın anlamını da taşır.","gloss":"kişinin kendisini gösteren iki ayrı söz","neighbor_only":"Komşu dal şiirsel bir söyleyişte yalnız kişinin kendi benliğini başka bir kalıpla belirtir.","neighbor_ref":"root_001271/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal belirli bir söz kuruluşunda kişinin kendisine gönderimde bulunur."},{"boundary_match":"partial","distinction":"Odak dal çoğunlukla tek bir yakın veya sırdaşı gösterir; komşu kişinin iç çevresini ve işlerine alınan özel kişileri daha geniş kapsar.","focus_only":"Odak dal seçilmiş yakını ve sırdaşı gösterebilir, fakat kişinin kendisini soran ayrı bir kullanım da içerir.","gloss":"seçilmiş yakın ile iç çevre","neighbor_only":"Komşu dal bir kişinin işine ve sırrına alınan bütün iç çevreyi ve özel kişileri topluluk olarak kapsayabilir.","neighbor_ref":"root_000128/B004","relation_type":"near_neighbor","shared_zone":"Güvenilen ve özel tutulan kişi iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Her dost odak daldaki özel adlandırmanın taşıdığı seçilmiş yakın değildir; odak dalın kişinin kendisine gönderimi de genel dostluk alanının dışındadır.","focus_only":"Odak dal özel kuruluşlarla kişinin kendisini ya da seçilmiş yakınını belirtir.","gloss":"seçilmiş sırdaş ile genel dostluk","neighbor_only":"Komşu dal arkadaşlık ve dostluk ilişkisini açık ya da gizli yönleriyle genel olarak anlatır.","neighbor_ref":"root_000397/B001","relation_type":"near_neighbor","shared_zone":"Seçilmiş yakın kişi aynı zamanda dost veya arkadaş olabilir."}],"source_phrase_ar":"كيف ابن إنسك إذا سأله عن نفسه (maqayis)؛ كيف ابن إنسك يعني نفسه وفلان ابن إنس فلان أي صفيه وخاصته وهذا خدني وإنسي وخلصي وجلسي (sihah)؛ كيف ترى ابن إنسك إذا خاطبت الرجل عن نفسه وفلان ابن أنس فلان أي صفيه وأنيسه (tahdhib)؛ قيل ابن إنسك للنفس (mufradat)","source_summary":"Aktarımlar, doğrudan hitapta kişinin kendi durumunu soran kullanım ile birinin seçkin yakını ve sırdaşını gösteren kullanımı birlikte verir. Yakın dost ve sürekli görüşülen arkadaş anlamındaki paralel adlar ikinci ilişki alanını genişletir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه كيف ابن إنسك للسؤال عن النفس، وفلان ابن أنس فلان لصفيه وخاصته، وما قاربه من الخدن والأنيس والخلص والجليس.","what_is_not_ar":"لا يدخل مطلق الإنسان ولا مطلق المؤانسة إلا إذا جاء بصيغة هذا الباب أو قرينته."},"support_links":["sup_47182ebabb01fee7ab8a"]},{"boundary":"Dal eve girmeden önce izin ve kabul arama durumuyla sınırlıdır; genel görme, genel yakınlık, eve yerleşme veya barınma anlamına gelmez.","branch_kind":"unresolved","branch_ref":"root_000059/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:5:5:2","qac_word_ref":"114:5:5","surface_ar":"نَّاسِ"}],"gloss":"girişten önce izin ve kabul arama","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eve girmeden önce selam verip girmek için izin istemeyi ve kabul beklemeyi anlatır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı açıklama, girişten önce içeridekilerden yakınlık ve kabul işareti bulmayı öne çıkarır."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir eve girmeden önce selam, izin sorusu veya içeridekilerin kabulünü yoklama yoluyla girişe onay arandığında kullanılır.","boundary_detail":"Dal eve girmeden önce izin ve kabul arama durumuyla sınırlıdır; genel görme, genel yakınlık, eve yerleşme veya barınma anlamına gelmez.","branch_image_ar":"الاستئناس قبل دخول البيوت","concept_gloss":"girişten önce izin ve kabul arama","contextual_glosses":[{"applicability":"Giriş izninin selam ve açık bir izin sorusuyla istendiğini belirten açıklamada uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Selam verme, izin sorma ve girişten önce bekleme işlemlerini korur."},"facet_ids":["F001"],"text":"selam verip girebilir miyim diye sormak","usage_role":"explanatory"},{"applicability":"İçeridekilerin yakınlık ve kabul gösterdiğini anlayarak girişe elverişli ortam bulma yorumunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Girişten önce kabul ve yakınlık işareti bulma yönünü korur."},"facet_ids":["F002"],"text":"girişe açık bir karşılama bulmak","usage_role":"contextual"}],"definition":"Bir eve girmeden önce selam vererek izin istemeyi ve içeridekilerin girişe açık olduğunu anlamayı anlatır. Aktarımın bir yönü doğrudan izin sorusunu, diğer yönü girişe elverişli bir kabul ve yakınlık bulmayı öne çıkarır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eve girmeden önce selam verip girmek için izin istemeyi ve kabul beklemeyi anlatır."},{"facet_id":"F002","role":"source_variant","statement":"Ayrı açıklama, girişten önce içeridekilerden yakınlık ve kabul işareti bulmayı öne çıkarır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yalnız gözle inceleme ve bir şeyi görme anlamını ekler.","collision":"Duyusal fark etme ve çevreye bakıp araştırma dalıyla karışır.","fit":"displacement","loses":"Selam verme, izin isteme ve içeridekilerin kabulünü bekleme koşullarını kaybeder.","preserves":"Girişten önce çevreyi yoklama düşüncesine sınırlı ölçüde yaklaşır."},"text":"bakıp görmek"}],"identity_rationale":"Kaynak ifadesi yalnız eve giriş öncesindeki belirli söz çevresinde açıklanır. Bir aktarım bunu selam verip izin isteme ve girebilir miyim diye sorma olarak, diğeri ise girişe elverişli bir kabul ve yakınlık bulma olarak yorumlar. Dal bu iki açıklamayı korumalı, fakat çıplak biçime genel bakma veya genel rahatlık anlamı yüklememelidir.","lexicalization_note":"Mekanik kapsam çözümlenmemiştir ve eldeki kanıt yalnız giriş öncesi kuruluşu gösterir. Bu nedenle tanım bu söz çevresine bağlanır, çıplak bir genel anlam varsayılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı. Genel yakınlık, çevreyi gözleme ve barınma senaryosu giriş öncesi izin sınırını en iyi açıkladığı için bu üç ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir giriş davranışı ve onay koşuludur; komşu dal yer ve zamanla sınırlı olmayan duygusal durumdur. Genel yakınlık, giriş izninin yerine geçmez.","focus_only":"Odak dal eve girişten önce selam, izin sorusu ve kabul bekleme yoluyla yürütülen sınırlı bir davranışı anlatır.","gloss":"giriş kabulü ile genel yakınlık duygusu","neighbor_only":"Komşu dal kişi veya şey karşısında genel olarak yabancılık ve ürkme duymayıp yakınlık ve rahatlık hissetmeyi anlatır.","neighbor_ref":"root_000059/B003","relation_type":"near_neighbor","shared_zone":"Kabul gören kişi giriş öncesinde kendini yabancı hissetmeyebilir ve yakınlık işareti bulabilir."},{"boundary_match":"partial","distinction":"Çevreyi gözlemek yalnız bilgi edinir; odak dal içeridekilerden onay almayı amaçlar. Birini görmek veya sesini duymak, tek başına giriş izni değildir.","focus_only":"Odak dal girişten önce selam verip izin ve kabul aramayı gerektirir.","gloss":"izin arama ile çevreyi gözleme","neighbor_only":"Komşu dal görme, işitme, belirti sezme veya çevreye bakarak birini araştırma eylemlerini anlatır.","neighbor_ref":"root_000059/B002","relation_type":"near_neighbor","shared_zone":"Girişten önce içeride birinin bulunup bulunmadığını anlamaya çalışma iki alanı aynı durumda buluşturabilir."},{"boundary_match":"thematic_only","distinction":"Odak dal girişten önceki toplumsal onayı, komşu dal ise bir yere yönelip orada barınmayı anlatır; aralarında sıradan sözcüksel yer değiştirme yoktur.","focus_only":"Odak dal bir eve girmeden önce kabul ve izin arama davranışıdır.","gloss":"eve giriş izni ile barınma","neighbor_only":"Komşu dal bir yere sığınma, yerleşme, barınma veya başkasını barındırma hareketini anlatır.","neighbor_ref":"root_000070/B001","relation_type":"thematic","shared_zone":"İki dal da bir yerle insan arasındaki giriş ve bulunma senaryosunda yer alabilir."}],"source_phrase_ar":"حتى تستأنسوا معناه حتى تستأذنوا وإنما هو حتى تسلموا وتستأنسوا السلام عليكم أأدخل (tahdhib)؛ حتى تستأنسوا أي تجدوا إيناسا (mufradat)","source_summary":"Giriş öncesi davranış iki yönden açıklanır: selam verip açıkça izin istemek ve girebilir miyim diye sormak ya da içeridekilerden girişe elverişli bir kabul ve yakınlık bulmak. Her iki açıklama da eve izinsiz girmeme sınırında birleşir.","sources":["TA","MU"],"what_is_ar":"يدخل فيه تفسير حتى تستأنسوا بالاستئذان أو السلام وطلب الدخول، أو بإيجاد إيناس قبل الدخول.","what_is_not_ar":"لا يدخل مطلق الإبصار أو مطلق الأنس إلا في صيغة الدخول المذكورة."},"support_links":[]},{"boundary":"Dalın çekirdeği göğüs bölgesidir; giysi, damga, bağ, rahatsızlık ve güçlü göğüslü aslan kullanımları bu çekirdeğe bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000849/B001","candidate_links":[{"candidate_id":"cand_b95e4d1f7ff65b7fc9d2","lane":"micro"},{"candidate_id":"cand_aeba23498e823c5c102a","lane":"micro"},{"candidate_id":"cand_7451b057185aa50c0afa","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:5:4:1","qac_word_ref":"114:5:4","surface_ar":"صُدُورِ"}],"gloss":"göğüs bölgesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan ve hayvan gövdesinin boyun altındaki ön bölgesini belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsanda göğsün üstte belirgin biçimde çıkıntı yapan kesimini gösterebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Göğsün ağrıması, bu bölgeden rahatsız olma veya göğse bir şeyle vurma bu bedensel çekirdeğe bağlı kullanımlardır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Göğsü örten giysi, hayvanın göğsündeki damga ve yükü tutan göğüs bağı aynı beden bölgesine göre adlandırılır."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Aslana verilen ad, hayvanın güçlü göğüslü oluşuna dayanan bir nitelemedir."}}],"root_ar":"ص د ر","root_id":"root_000849","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan veya hayvan gövdesindeki temel anatomik bölgeyi karşılar; dalın öteki kullanımları bu anlamdan türemiştir.","boundary_detail":"Dalın çekirdeği göğüs bölgesidir; giysi, damga, bağ, rahatsızlık ve güçlü göğüslü aslan kullanımları bu çekirdeğe bağlıdır.","branch_image_ar":"الصدر الجارحة وما يتصل بها","concept_gloss":"göğüs bölgesi","contextual_glosses":[{"applicability":"İnsan göğsünün üstte belirginleşen özel kesiminden söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Göğsün üstte çıkıntı yapan kesimine yönelik dar bağlamı korur."},"facet_ids":["F002"],"text":"göğsün üst çıkıntısı","usage_role":"contextual"},{"applicability":"Bir kişinin göğsünde ağrı ya da rahatsızlık bulunmasını anlatan eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Rahatsızlığın göğüs bölgesinde bulunması bilgisini korur."},"facet_ids":["F003"],"text":"göğsü ağrımak","usage_role":"contextual"},{"applicability":"Bir hayvanda yükü sabitlemek üzere göğüs çevresinden geçirilen bağ veya kemer için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesnenin göğüste bulunmasını ve yükü sabitleme görevini korur."},"facet_ids":["F004"],"text":"göğüs bağı","usage_role":"contextual"}],"definition":"İnsan ya da hayvan gövdesinin boyun ile karın arasında kalan ön ve üst bölgesidir. Bu çekirdekten, üstte kabaran kesim, buradaki ağrı veya yaralanma, bölgeyi örten ya da bağlayan nesneler, üzerindeki damga ve güçlü göğsüyle nitelenen aslan kullanımları doğar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan ve hayvan gövdesinin boyun altındaki ön bölgesini belirtir."},{"facet_id":"F002","role":"specialization","statement":"İnsanda göğsün üstte belirgin biçimde çıkıntı yapan kesimini gösterebilir."},{"facet_id":"F003","role":"associated_use","statement":"Göğsün ağrıması, bu bölgeden rahatsız olma veya göğse bir şeyle vurma bu bedensel çekirdeğe bağlı kullanımlardır."},{"facet_id":"F004","role":"associated_use","statement":"Göğsü örten giysi, hayvanın göğsündeki damga ve yükü tutan göğüs bağı aynı beden bölgesine göre adlandırılır."},{"facet_id":"F005","role":"extension","statement":"Aslana verilen ad, hayvanın güçlü göğüslü oluşuna dayanan bir nitelemedir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Zamansal ya da sırasal ilk olma anlamını ekler.","collision":"Aynı kökün ön, üst ve ilk kesim dalıyla karışır.","fit":"displacement","loses":"Anatomik göğüs bölgesini ve bedensel sınırını bütünüyle kaybeder.","preserves":"Önde bulunma çağrışımını dolaylı olarak koruyabilir."},"text":"başlangıç"}],"identity_rationale":"Kaynak ifadesi, insanın göğsünü temel beden bölgesi olarak verir ve hayvandaki karşılığını, göğsün üstte çıkıntılı kesimini, bu bölgedeki ağrı ya da yaralanmayı ve göğüsle ilişkili nesne ile adlandırmaları aynı dalda toplar. Geçici çerçeve bu çekirdek ile ona bağlı kullanımların sırasını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"göğüs"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"göğüsler"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"göğsün üstte çıkıntılı kesimi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"göğsü örten kısa giysi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"devenin göğsündeki damga"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yükü sabitleyen göğüs bağı"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"göğsünden rahatsız olan kimse"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"birinin göğsüne bir şeyle vurmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"göğsü ağrımak"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"güçlü göğüslü aslan"}],"lexicalization_note":"Çıplak biçimin anatomik anlamı temel alınır; ağrı, yaralama, örtme, bağlama ve adlandırma anlamları yalnız kendi türemiş biçimleri içinde değerlendirilir.","neighbor_coverage_note":"Bütün adaylar anatomik kapsam ve bağımlı türetimler bakımından değerlendirildi; yalnız eşanlamlı göğüs çekirdeği ile et ve kemik sınırlarını açıklayan üç karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek anatomik sınır bakımından anlamlı bir ayrım yoktur; odak daldaki giysi, ağrı ve benzeri türemiş örnekler eşanlamlı çekirdeği değiştirmez.","focus_only":null,"gloss":"göğüs","neighbor_only":null,"neighbor_ref":"root_001315/B007","relation_type":"synonym","shared_zone":"Her iki dalın çekirdeği de gövdenin ön üst bölümündeki göğüs bölgesidir."},{"boundary_match":"partial","distinction":"Biri beden bölgesinin kendisini, öteki ise o bölgede bulunan belirli dokuyu adlandırır; bu nedenle olağan bağlamlarda birbirinin yerine geçmez.","focus_only":"Odak dalı göğüs bölgesinin tamamını anatomik bir yer olarak belirtir.","gloss":"göğüs eti","neighbor_only":"Komşu dal yalnız göğüs ve boyun çevresindeki eti belirtir.","neighbor_ref":"root_000095/B003","relation_type":"near_neighbor","shared_zone":"İki dal da göğüs çevresindeki aynı beden alanına yönelir."},{"boundary_match":"partial","distinction":"Odak geniş bir anatomik bölgedir; komşu ise bu bölgedeki kemiklere ve belirli bir yüzey konumuna özgüdür.","focus_only":"Odak dalı kemiklerle sınırlı olmayan bütün göğüs bölgesini kapsar.","gloss":"üst göğüs kemikleri","neighbor_only":"Komşu dal köprücük kemiği çevresindeki göğüs kemiklerini ve kolye yerini belirtir.","neighbor_ref":"root_000178/B005","relation_type":"near_neighbor","shared_zone":"Her ikisi de göğsün üst bölümünü bedensel konum olarak paylaşır."}],"source_phrase_ar":"الصدر للإنسان والجمع صدور (maqayis)؛ الصدر الجارحة (mufradat)؛ الصدرة من الإنسان ما أشرف من أعلى صدره (ayn;sihah;tahdhib)؛ صدر فلان إذا وجع صدره (ayn;tahdhib)؛ المصدور الذي يشتكي صدره (maqayis;sihah)؛ الصدار ثوب يغطي الصدر (maqayis;ayn;tahdhib;mufradat)؛ الصدار سمة على صدر البعير (maqayis;sihah;mufradat)؛ المصدر الأسد (maqayis;ayn;sihah)","source_summary":"Kaynakların ortak çizgisi göğsü anatomik merkez olarak kurar; üst çıkıntı, ağrı ve yaralama ile giysi, damga ve güçlü göğüslülüğe dayalı adlandırmalar bu merkezden açıklanır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"صدر الإنسان والحيوان وما أشرف من أعلاه، ووجع الصدر وإصابته، وما يغطى الصدر أو يسمه أو يشد عليه، وما سمي لقوة صدره","what_is_not_ar":"صدر الأمر؛ الصدور عن الماء؛ المصدر النحوي"},"support_links":["sup_1b7f8f0ac53eb4f64837","sup_47182ebabb01fee7ab8a","sup_56f18f1d10bff16cca6c"]},{"boundary":"Anatomik göğsün kendisi bu dalın çekirdeği değildir; beden bölgesinden taşınan ön, üst veya ilk konum ilişkisi belirleyicidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000849/B002","candidate_links":[{"candidate_id":"cand_9d8949e8b05a172f4f31","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:5:4:1","qac_word_ref":"114:5:4","surface_ar":"صُدُورِ"}],"gloss":"ön, üst ya da başlangıç bölümü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesne, oluş veya düzenin ön, üst ya da ilk kesimini belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Mızrak benzeri uzun bir nesnenin üst kısmını ve okun ortasından ucuna uzanan ön bölümünü gösterebilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir işin, toplantının, kitabın veya sözün ön ya da başlangıç bölümüne uygulanır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Atın göğsünü öne çıkararak rakiplerinden önce gelmesini anlatan yarış kullanımına temel olur."}}],"root_ar":"ص د ر","root_id":"root_000849","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın konumsal ve sırasal çekirdeğini birlikte vermek gereken genel açıklamalarda kullanılır.","boundary_detail":"Anatomik göğsün kendisi bu dalın çekirdeği değildir; beden bölgesinden taşınan ön, üst veya ilk konum ilişkisi belirleyicidir.","branch_image_ar":"المقدّم والأعلى والأول","concept_gloss":"ön, üst ya da başlangıç bölümü","contextual_glosses":[{"applicability":"Bir nesnenin ya da düzenlenmiş alanın öndeki kesimi söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bütün içindeki önde bulunma ilişkisini açık biçimde korur."},"facet_ids":["F001","F002"],"text":"ön kısım","usage_role":"contextual"},{"applicability":"Bir işin, kitabın veya sözün ilk bölümü anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sırasal olarak ilk bölüm olma anlamını eksiksiz korur."},"facet_ids":["F001","F003"],"text":"başlangıç","usage_role":"contextual"},{"applicability":"Bir atın yarışta göğsünü öne çıkararak önce gelmesini açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yarış üstünlüğünün atın göğsünün önde bulunmasıyla belirlenmesini korur."},"facet_ids":["F004"],"text":"göğüs farkıyla öne geçmek","usage_role":"explanatory"}],"definition":"Bir şeyin önde, üstte ya da başlangıçta bulunan kesimidir. Bu konumsal ve sırasal çekirdek uzun nesnelerin ön veya üst bölümlerinde, toplantı, kitap ve sözün başlangıcında ve atın göğsüyle öne geçmesinde özelleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesne, oluş veya düzenin ön, üst ya da ilk kesimini belirtir."},{"facet_id":"F002","role":"specialization","statement":"Mızrak benzeri uzun bir nesnenin üst kısmını ve okun ortasından ucuna uzanan ön bölümünü gösterebilir."},{"facet_id":"F003","role":"extension","statement":"Bir işin, toplantının, kitabın veya sözün ön ya da başlangıç bölümüne uygulanır."},{"facet_id":"F004","role":"associated_use","statement":"Atın göğsünü öne çıkararak rakiplerinden önce gelmesini anlatan yarış kullanımına temel olur."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Aynı kökün anatomik göğüs dalıyla karışır.","fit":"narrowing","loses":"Nesnelerin, işlerin ve metinlerin ön veya ilk bölümü olma kapsamını kaybeder.","preserves":"Önde ve üstte bulunma imgesinin bedensel kaynağını korur."},"text":"göğüs"}],"identity_rationale":"Kaynak ifadesi bir şeyin ön, üst veya ilk kesimini ortak çekirdek olarak açıkça verir; uzun nesnelerin bölümleri, işin başlangıcı, toplantı, kitap ve sözün ön kısmı ile atın göğsüyle öne geçmesi bu çekirdeğin düzenli özelleşmeleridir. Geçici çerçeve bu kapsamı doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ön, üst ya da başlangıç bölümü"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"mızrağın üst bölümü"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"işin başlangıcı"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"toplantının ön kısmı; kitabın veya sözün başlangıcı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"okun ortasından ucuna uzanan ön bölümü"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"ön gövdesi kalın ok"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"göğsüyle öne çıkıp yarışı geçmek"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kitaba giriş bölümü koymak"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"toplantının başköşesine oturmak"}],"lexicalization_note":"Çıplak biçimin ön, üst ve ilk kesim anlamı korunur; nesne, metin, toplantı ve yarış bağlamları kendi yapılarına bağlı özelleşmeler olarak tutulur.","neighbor_coverage_note":"Bütün adaylar konum, sıra ve hareket ayrımı üzerinden değerlendirildi; ön ve ilk bölümle en yakın iki dal, öne geçme olayı ve arka yön karşıtlığı sınırı en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Örtüşme ön ve ilk bölümde güçlüdür; odak dalının üstlük ve metinsel başlangıç kapsamı ile komşunun belirli beden ve nesne parçaları tam ikameyi engeller.","focus_only":"Odak dalı üst bölüm ve soyut başlangıç anlamlarını da genel çekirdeğe katar.","gloss":"ön veya ilk bölüm","neighbor_only":"Komşu dal yüz, baş, ordu, eyer, meme ve kuş tüyü gibi belirli ön parçaları ayrıca kapsar.","neighbor_ref":"root_001207/B007","relation_type":"near_synonym","shared_zone":"Her iki dal bir şeyin önde bulunan ya da ilk gelen bölümünü gösterebilir."},{"boundary_match":"partial","distinction":"Komşu başlangıç ve ilk görünüş üzerinde yoğunlaşırken odak dalı ayrıca uzamsal önlük ve üstlüğü kurucu seçenekler olarak taşır.","focus_only":"Odak dalı öndeki ve üstteki somut kesimleri de başlangıçla birlikte kapsar.","gloss":"ilk bölüm","neighbor_only":"Komşu dal bitkinin başı, yeni ay ve ayın ilk günleri gibi başlangıç örneklerine özgü uzanımlara sahiptir.","neighbor_ref":"root_001078/B005","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin başlangıcını veya ilk görünen kesimini anlatır."},{"boundary_match":"partial","distinction":"Odak ön konumu veya bölümü adlandırır; komşu ise o konuma doğru ilerleme ya da üstünlük kazanma olayını anlatır.","focus_only":"Odak dalı bir şeyin sabit ön, üst veya ilk bölümünü adlandırır.","gloss":"öne geçme","neighbor_only":"Komşu dal öne doğru ilerleme ve başkasını geçme hareketini temel alır.","neighbor_ref":"root_001207/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal önde bulunma ve başkalarından önce gelme alanında buluşur."},{"boundary_match":"opposed","distinction":"Uzamsal ön ve arka anlamları doğrudan karşıttır; odak dalındaki üst ve başlangıç uzanımları bu karşıtlığın dışında kalır.","focus_only":"Odak dalı ön tarafı ve buna bağlı üst veya ilk konumu kapsar.","gloss":"ön ve arka","neighbor_only":"Komşu dal arka tarafı ve önde olanın gerisinde kalma konumunu kapsar.","neighbor_ref":"root_000433/B002","relation_type":"antonym","shared_zone":"İki dal bir nesneye göre yön ve sıra belirleyen ortak bir eksen kurar."}],"source_phrase_ar":"الصدر أعلى مقدم كل شيء (ayn;tahdhib)؛ صدر القناة أعلاها (ayn;sihah;tahdhib;mufradat)؛ صدر الأمر أوله (ayn;tahdhib)؛ صدر كل شيء أوله (sihah)؛ صدر المجلس والكتاب والكلام (mufradat)؛ صدر السهم ما فوق نصفه إلى المراش (ayn;tahdhib)؛ صدر الفرس إذا جاء قد سبق بصدره (sihah;tahdhib;mufradat)","source_summary":"Kaynaklar ön, üst ve ilk olma ilişkisini ortak anlam olarak sunar; nesne bölümleri, metin ve toplantı başlangıçları ile göğsü öne çıkararak kazanılan yarış üstünlüğü bu ilişkinin bağlama göre görünüşleridir.","sources":["AY","SI","TA","MU"],"what_is_ar":"مقدّم الشيء وأعلاه وأوله، كصدر القناة والأمر والكتاب والمجلس والكلام، ومقدّم السهم، وسبق الفرس بصدره","what_is_not_ar":"الصدر الجارحة في نفسها؛ الانصراف عن الورد؛ المصادرة على مال"},"support_links":["sup_0c8db3cf8704202747d7"]},{"boundary":"Her ayrılma bu dala girmez; çekirdekte daha önce varılan yerden veya girilen durumdan ayrılma ve geri yönelme ilişkisi bulunur.","branch_kind":"mixed_non_bare","branch_ref":"root_000849/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:5:4:1","qac_word_ref":"114:5:4","surface_ar":"صُدُورِ"}],"gloss":"geldiği yerden ayrılıp dönme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Daha önce varılan bir yerden veya girilen bir durumdan ayrılıp geri yönelmeyi belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Su içmek için su başına gelen insan veya hayvanların oradan ayrılması temel örnektir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen biçim, bir başkasını geri çevirip onun dönmesini sağlama anlamı taşır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Belirli söz öbeğinde yol, insanlarını su başından uzaklaştırıp geri götüren güzergah olarak nitelenir."}}],"root_ar":"ص د ر","root_id":"root_000849","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Önceki varış ile sonraki ayrılış aşamalarını birlikte belirtmek gereken genel bağlamlarda kullanılır.","boundary_detail":"Her ayrılma bu dala girmez; çekirdekte daha önce varılan yerden veya girilen durumdan ayrılma ve geri yönelme ilişkisi bulunur.","branch_image_ar":"الصُّدور عن المورد","concept_gloss":"geldiği yerden ayrılıp dönme","contextual_glosses":[{"applicability":"Su içmek üzere gelmiş insan veya hayvanların daha sonra su başını terk etmesi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Su başına gelişten sonraki ayrılma aşamasını tam olarak korur."},"facet_ids":["F001","F002"],"text":"su başından ayrılmak","usage_role":"contextual"},{"applicability":"Bir başkasının geldiği yerden ayrılıp dönmesini sağlama bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemi başkasına yaptırma ve geri yöneltme ilişkisini korur."},"facet_ids":["F003"],"text":"geri döndürmek","usage_role":"contextual"},{"applicability":"İnsanları su başından uzaklaştırıp geri götüren yolun niteliğini açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yolun su başından ayrılışa aracılık etmesi anlamını korur."},"facet_ids":["F004"],"text":"su başından dönüş yolu","usage_role":"explanatory"}],"definition":"Bir su başına, ülkeye ya da bir işe vardıktan veya girdikten sonra oradan ayrılıp geri yönelme hareketidir. Başkasını bu dönüşe yöneltme ve insanları su başından uzaklaştıran yol, bu çekirdeğe bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Daha önce varılan bir yerden veya girilen bir durumdan ayrılıp geri yönelmeyi belirtir."},{"facet_id":"F002","role":"specialization","statement":"Su içmek için su başına gelen insan veya hayvanların oradan ayrılması temel örnektir."},{"facet_id":"F003","role":"associated_use","statement":"Ettirgen biçim, bir başkasını geri çevirip onun dönmesini sağlama anlamı taşır."},{"facet_id":"F004","role":"associated_use","statement":"Belirli söz öbeğinde yol, insanlarını su başından uzaklaştırıp geri götüren güzergah olarak nitelenir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Önceden varılmış bir yer ya da girilmiş bir durum bulunmayan her türlü ayrılmayı kapsama ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Bir yerden uzaklaşma hareketini genel düzeyde korur."},"text":"ayrılma"}],"identity_rationale":"Kaynak ifadesi, su başı, ülke veya başka bir işe varıştan sonra oradan ayrılmayı temel hareket olarak verir; bir başkasını geri çevirme ve insanlarını su başından uzaklaştıran yol da bu hareketin ettirgen ve yapıya bağlı uzanımlarıdır. Geçici çerçeve bu aşamaları birbirine karıştırmadan korur.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bir yerden ya da durumdan ayrılış"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"su başından, geldikten sonra ayrılmak"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"geri döndürmek"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"su başından dönüşü sağlayan yol"}],"lexicalization_note":"Ayrılıp dönme olayı temel alınır; başkasını döndürme yalnız ettirgen biçime, su başından uzaklaştıran yol ise verilen söz öbeğine bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar önceki varış, iç-dış geçiş, geri yönelme ve yolculuk koşulları bakımından değerlendirildi; bu dört aday dalın hareket sınırını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında varıştan sonraki dönüş kurucudur; komşu dalda genel gidiş veya hızlı uzaklaşma yeterlidir.","focus_only":"Odak dalı önceden varılan yerden ayrılıp geri yönelme aşamasını gerektirir.","gloss":"ayrılıp gitme","neighbor_only":"Komşu dal yeryüzünde gitmeyi ve bir kişiden hızla uzaklaşmayı önceki varış koşulu olmadan kapsar.","neighbor_ref":"root_000325/B007","relation_type":"near_synonym","shared_zone":"İki dal da bir yerden uzaklaşma ve orayı geride bırakma hareketini anlatır."},{"boundary_match":"partial","distinction":"Çıkış, iç-dış sınırının aşılmasına dayanır; odak ise önceki varış ve ardından dönüş düzenini gerektirir.","focus_only":"Odak dalı bir yere geldikten sonra oradan ayrılıp geri yönelmeyi içerir.","gloss":"dışarı çıkma","neighbor_only":"Komşu dal yalnız bir şeyin içinden dışarı çıkmayı bildirir.","neighbor_ref":"root_001158/B004","relation_type":"near_synonym","shared_zone":"Her iki dal bir başlangıç alanını geride bırakma hareketinde örtüşür."},{"boundary_match":"partial","distinction":"Odak, varılan yerden çıkış anını adlandırır; komşu ise geri gelişin kendisini ve daha geniş gidip gelme olaylarını kapsar.","focus_only":"Odak dalı varılan kaynaktan ayrılma evresini merkeze alır.","gloss":"geri dönme","neighbor_only":"Komşu dal geri gelme, yeniden dönme ve bazı şeylerin gidip gelmesi gibi yinelenen hareketleri kapsar.","neighbor_ref":"root_000618/B004","relation_type":"near_neighbor","shared_zone":"İki dalın ortak alanı geriye yönelme ve önceki konumla yeniden ilişki kurmadır."},{"boundary_match":"thematic_only","distinction":"Odak önceki varışın ardından dönüşü, komşu ise yeni bir hedefe yönelen yolculuğu anlatır; ortaklık olay alanıyla sınırlıdır.","focus_only":"Odak dalı varıştan sonra kaynaktan veya yerden ayrılma aşamasını belirtir.","gloss":"yola çıkma","neighbor_only":"Komşu dal bir hedefe doğru yolculuğa çıkmayı ve seyahat etmeyi belirtir.","neighbor_ref":"root_000551/B001","relation_type":"thematic","shared_zone":"Her ikisi de bir yerden ayrılmayı içeren hareket senaryosunda yer alır."}],"source_phrase_ar":"صدر عن الماء وصدر عن البلاد (maqayis;sihah)؛ الصدر الانصراف عن الورد وعن كل أمر (ayn;tahdhib)؛ صدرت الإبل عن الماء (mufradat)؛ أصدرته فصدر أي رجعته فرجع (sihah)؛ طريق صادر يصدر بأهله عن الماء (ayn;sihah;tahdhib)","source_summary":"Kaynakların ortak anlamı, varılan su başından, ülkeden veya girilen bir işten ayrılıp geri yönelmektir; ettirgen dönüş ve bu ayrılışı sağlayan yol aynı hareket şemasına bağlıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الانصراف عن الماء أو البلاد أو كل أمر بعد وروده، والإصدار بمعنى الإرجاع، والطريق الصادر بأهله","what_is_not_ar":"الصدر الجارحة؛ صدر الشيء بمعنى أوله؛ المصدر النحوي"},"support_links":[]},{"boundary":"Dil bilgisel temel ana kullanımdır; çıkış yeri ve çıkış zamanı, ortak çıkma ilişkisine dayanan ayrı adlandırma seçenekleridir.","branch_kind":"bare","branch_ref":"root_000849/B004","candidate_links":[{"candidate_id":"cand_9d8949e8b05a172f4f31","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:5:4:1","qac_word_ref":"114:5:4","surface_ar":"صُدُورِ"}],"gloss":"eylem türetme temeli; çıkış yeri veya zamanı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekimli eylem biçimlerinin türediği kabul edilen temel sözcük biçimini belirtir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı ad, çıkma olayının gerçekleştiği yer veya zamanı bildiren bir ad olarak da açıklanır."}}],"root_ar":"ص د ر","root_id":"root_000849","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın dil bilgisel çekirdeğiyle yer ve zaman uzanımını birlikte göstermek gereken sözlük açıklamasında kullanılır.","boundary_detail":"Dil bilgisel temel ana kullanımdır; çıkış yeri ve çıkış zamanı, ortak çıkma ilişkisine dayanan ayrı adlandırma seçenekleridir.","branch_image_ar":"الأصل الذي تصدر عنه الأفعال","concept_gloss":"eylem türetme temeli; çıkış yeri veya zamanı","contextual_glosses":[{"applicability":"Sözcük yapısında çekimli eylemlerin dayandırıldığı temel ad biçimi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Temel biçim ile ondan türeyen eylem biçimleri arasındaki yönü korur."},"facet_ids":["F001"],"text":"eylemlerin türediği temel biçim","usage_role":"explanatory"},{"applicability":"Bir çıkma olayının gerçekleştiği mekanın adı söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adlandırılan unsurun çıkma olayına ait yer olması bilgisini korur."},"facet_ids":["F002"],"text":"çıkış yeri","usage_role":"contextual"},{"applicability":"Bir çıkma olayının gerçekleştiği zamanın adı söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adlandırılan unsurun çıkma olayına ait zaman olması bilgisini korur."},"facet_ids":["F002"],"text":"çıkış zamanı","usage_role":"contextual"}],"definition":"Dil bilgisinde, çekimli eylem biçimlerinin kendisinden çıktığı kabul edilen temel sözcük biçimidir. Aynı ad, çıkma eyleminin gerçekleştiği yeri veya zamanı da gösterebilir; bu ikinci kullanım dil bilgisel temel ile özdeş değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekimli eylem biçimlerinin türediği kabul edilen temel sözcük biçimini belirtir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı ad, çıkma olayının gerçekleştiği yer veya zamanı bildiren bir ad olarak da açıklanır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Su kaynağı, bilgi belgesi ve genel köken gibi bu dala özgü olmayan çok sayıda anlamı kapsama ekler.","collision":"Genel köken ve maden ya da pınar komşularıyla kolayca karışır.","fit":"broadening","loses":null,"preserves":"Başka bir şeyin kendisinden çıkması ya da doğması ilişkisini korur."},"text":"kaynak"}],"identity_rationale":"Kaynak ifadesi, çekimli eylemlerin kendisinden çıktığı kabul edilen temel sözcük biçimi ile çıkmanın gerçekleştiği yer ve zamanı aynı ad altında anar. Geçici çerçeve kullanılabilir, ancak dil bilgisel türetme temeli ile olayın yeri veya zamanı tek bir kavrammış gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"eylemlerin türediği temel sözcük biçimi"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"çıkış yeri ya da zamanı"}],"lexicalization_note":"Dal, ad biçiminin çıplak anlam alanını tanımlar; dil bilgisel temel ile yer ve zaman anlamları ayrılır ve başka söz öbeklerinden kapsam aktarılmaz.","neighbor_coverage_note":"Bütün adaylar genel köken, somut kaynak, dil bilgisel işlev ve gerçek ayrılış bakımından değerlendirildi; seçilen dört karşılaştırma iki alt kullanımın sınırını doğrudan aydınlatır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak teknik bir sözcük biçimine ve çıkış olayının yer-zaman adlarına bağlıdır; komşu ise alan sınırlaması olmayan genel köken kavramıdır.","focus_only":"Odak dalı dil bilgisel temel biçimi ve çıkışın yer ya da zamanını adlandırır.","gloss":"köken","neighbor_only":"Komşu dal herhangi bir şeyin, kişinin veya olayın genel kökenini kapsar.","neighbor_ref":"root_000031/B002","relation_type":"near_synonym","shared_zone":"Her iki dal başka biçimlerin veya olayların kendisinden çıktığı başlangıç noktasını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dil bilgisel ve olay yapısına bağlı bir adlandırmadır; komşu somut üretim veya akış kaynağını temel alır.","focus_only":"Odak dalı dil bilgisel türetme temelini ve olayın çıkış yeri ya da zamanını kapsar.","gloss":"çıktığı yer","neighbor_only":"Komşu dal maddelerin çıkarıldığı maden veya bir şeyin doğduğu somut pınar ve menba alanını kapsar.","neighbor_ref":"root_001475/B008","relation_type":"near_neighbor","shared_zone":"İki dal bir şeyin ortaya çıktığı başlangıç yerini gösterme alanında örtüşür."},{"boundary_match":"field_only","distinction":"Biri türetme yönündeki temel biçimdir, öteki cümle içindeki durum işaretidir; çekirdek işlemleri farklıdır.","focus_only":"Odak dalı eylem biçimlerinin dayandırıldığı temel sözcük biçimini belirtir.","gloss":"dil bilgisel biçim","neighbor_only":"Komşu dal sözcüğün cümledeki durumunu gösteren belirli bir dil bilgisi işaretlemesini belirtir.","neighbor_ref":"root_000582/B012","relation_type":"same_field","shared_zone":"Her iki dal sözcüklerin dil bilgisel çözümlemesi alanında kullanılır."},{"boundary_match":"partial","distinction":"Odak bir temel biçim veya yer-zaman adıdır; komşu ise katılımcının gerçekleştirdiği hareketin kendisidir.","focus_only":"Odak dalı çıkmanın dil bilgisel temelini ve olayın yer ya da zaman adını belirtir.","gloss":"çıkış ve ayrılış","neighbor_only":"Komşu dal varılan yerden gerçekten ayrılıp geri yönelme hareketini belirtir.","neighbor_ref":"root_000849/B003","relation_type":"near_neighbor","shared_zone":"İki dal çıkma ve bir başlangıç noktasından uzaklaşma düşüncesini paylaşır."}],"source_phrase_ar":"المصدر أصل الكلمة الذي تصدر عنه الأفعال (ayn;tahdhib)؛ مصادر الأفعال (sihah)؛ المصدر في الحقيقة صدر عن الماء ولموضع المصدر ولزمانه (mufradat)","source_summary":"Toplu kaynak anlatımı iki bağlı fakat ayrı kullanımı içerir: eylem biçimlerinin türediği dil bilgisel temel ve bir çıkma olayının yeri ya da zamanı. Ortak bağ, başka bir biçim veya olayın buradan çıkması düşüncesidir.","sources":["AY","SI","TA","MU"],"what_is_ar":"المصدر بوصفه أصل الكلمة أو الفعل، وما يلحق به من اسم الموضع والزمان في الصدور","what_is_not_ar":"الصدر الجارحة؛ صدر الشيء أوله؛ الصدور الحسي عن الماء"},"support_links":["sup_0c8db3cf8704202747d7"]},{"boundary":"Anlam belirli yapılara bağlı bir ödeme ve güvence yükümlülüğüdür; malın zorla alınması tek başına bu dalı karşılamaz.","branch_kind":"non_bare","branch_ref":"root_000849/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:5:4:1","qac_word_ref":"114:5:4","surface_ar":"صُدُورِ"}],"gloss":"para ödeme ve güvence yükümlülüğü koyma","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kimseye belirli bir para tutarını ödeme ve o tutarın güvencesini üstlenme yükümlülüğü konur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yapı, kimi açıklamada tarafların güvence altındaki para tutarı üzerinde hesaplaşması veya anlaşması olarak yorumlanır."}}],"root_ar":"ص د ر","root_id":"root_000849","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli yapı içinde bir kişiye ödeyeceği tutar için sorumluluk yüklendiğini açıklamak üzere kullanılır.","boundary_detail":"Anlam belirli yapılara bağlı bir ödeme ve güvence yükümlülüğüdür; malın zorla alınması tek başına bu dalı karşılamaz.","branch_image_ar":"المصادرة على مال","concept_gloss":"para ödeme ve güvence yükümlülüğü koyma","contextual_glosses":[{"applicability":"Bir kişiye belirlenmiş para tutarını ödeme ve güvenceye alma sorumluluğu verildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yükümlü kılınan kişiyi, belirli tutarı ve ödeme sorumluluğunu korur."},"facet_ids":["F001"],"text":"belli bir tutarı ödemekle yükümlü kılmak","usage_role":"explanatory"},{"applicability":"Tarafların güvence altına alınacak para tutarını belirleyip ayrılması veya anlaşması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli para tutarı üzerinde anlaşma ve sorumluluğu üstlenme ilişkisini korur."},"facet_ids":["F002"],"text":"ödeme tutarı üzerinde hesaplaşmak","usage_role":"contextual"}],"definition":"Belirli yapılarda, bir kimseyi belirli bir parayı ödemek ve bu tutardan sorumlu olmakla yükümlü kılmayı; kimi bağlamlarda da bu yükümlülük üzerinde hesaplaşmayı anlatır. Doğrudan malına el koyma anlamı zorunlu değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kimseye belirli bir para tutarını ödeme ve o tutarın güvencesini üstlenme yükümlülüğü konur."},{"facet_id":"F002","role":"source_variant","statement":"Yapı, kimi açıklamada tarafların güvence altındaki para tutarı üzerinde hesaplaşması veya anlaşması olarak yorumlanır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Malın doğrudan alınması ve mülkiyetin kişiden çıkarılması sonucunu ekler.","collision":"Çağdaş zorla alma anlamıyla karışarak kaynak sınırını değiştirir.","fit":"displacement","loses":"Belirli tutarı ödeme ve bu tutardan sorumlu olma ilişkisini kaybeder.","preserves":"Bir kişinin mal varlığına yönelen zorlayıcı mali işlem çağrışımını korur."},"text":"malına el koymak"}],"identity_rationale":"Kaynak ifadesi modern anlamdaki doğrudan mala el koymayı zorunlu kılmaz; belirli yapılarda bir kimseye ödeyeceği ve güvencesini üstleneceği bir tutar yüklenmesini, kimi açıklamada da bu tutar üzerinde hesaplaşmayı anlatır. Bu nedenle dal korunabilir, fakat geçici el koyma çerçevesi mali yükümlülük olarak düzeltilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"birini belli bir parayı ödemek ve güvence altına almakla yükümlü kılmak"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"kendisine para ödeme ve güvence yükümlülüğü konmak"}],"lexicalization_note":"Anlam yalnız verilen kişi ve para yapılarında geçerlidir; çıplak köke genel el koyma, vergi alma veya ödeme anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar yükümlülük kurma, hakkı ödeme, alacak isteme ve belirli mali ödeme türleri bakımından değerlendirildi; seçilen dört aday işlem ile sonuç arasındaki sınırı gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak sorumluluğun kişiye yüklenmesini, komşu ise mevcut sorumluluğun ödeme yoluyla yerine getirilmesini temel alır.","focus_only":"Odak dalı belirli tutar için ödeme ve güvence yükümlülüğünü kurar.","gloss":"ödeme yükümlülüğü ve ödeme","neighbor_only":"Komşu dal önceden var olan borç, vergi veya emanet hakkının fiilen yerine getirilmesini anlatır.","neighbor_ref":"root_000021/B002","relation_type":"near_neighbor","shared_zone":"İki dal bir hakkın veya para borcunun ödenmesi alanında buluşur."},{"boundary_match":"partial","distinction":"Odak yükümlülüğün kurulmasına, komşu ise kurulmuş hakkın talep ve tahsiline dayanır.","focus_only":"Odak dalı kişiyi belirli bir tutardan sorumlu kılma işlemini belirtir.","gloss":"mali sorumluluk ve alacak isteme","neighbor_only":"Komşu dal hak sahibinin mevcut alacağını sürekli istemesi ve tahsil etmeye çalışmasını belirtir.","neighbor_ref":"root_000943/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal bir kişinin başkasından para veya hak istemesiyle ilişkili olabilir."},{"boundary_match":"field_only","distinction":"Odak kişi üzerinde kurulan sorumluluktur; komşu ise verilen veya çıkarılan mali değerin türünü adlandırır.","focus_only":"Odak dalı kişiye ödeme ve güvence sorumluluğu yükleyen işlemi anlatır.","gloss":"mali yükümlülük","neighbor_only":"Komşu dal belirli bir yolla çıkarılan para, ürün, vergi veya payın kendisini anlatır.","neighbor_ref":"root_000400/B003","relation_type":"same_field","shared_zone":"İki dal düzenlenmiş bir mali ödeme ve belirlenmiş tutar alanını paylaşır."},{"boundary_match":"field_only","distinction":"Odak bir yükümlü kılma işlemi ve güvencedir; komşu ise belirli hukuki bağlamdaki ödeme türüdür.","focus_only":"Odak dalı herhangi bir kişiye belirli yapı içinde yüklenen para sorumluluğunu belirtir.","gloss":"yüklenen mali ödeme","neighbor_only":"Komşu dal belirli bir topluluğa hukuki statüsü nedeniyle konan özel mali ödemeyi belirtir.","neighbor_ref":"root_000244/B004","relation_type":"same_field","shared_zone":"Her iki dal bir kişinin ya da topluluğun ödemek zorunda bırakıldığı para alanındadır."}],"source_phrase_ar":"صادره على كذا (sihah)؛ صودر فلان العامل على مال يؤديه أي فورق على مال ضمنه (tahdhib)","source_summary":"Toplu kaynak anlatımı, belirli bir para için ödeme ve güvence sorumluluğu kurulmasında birleşir; anlatım bu sorumluluğun yüklenmesi ile tarafların tutar üzerinde hesaplaşması arasında değişir.","sources":["SI","TA"],"what_is_ar":"مصادرة العامل أو غيره على مال يؤديه ويضمنه","what_is_not_ar":"الصدر الجارحة؛ الصدور عن الماء؛ صدر الشيء أوله"},"support_links":[]},{"boundary":"Dal, bütünün herhangi bir bölümünü veya kümesini belirtir; ilk bölüm, beden parçası ya da sabit oran koşulu taşımaz.","branch_kind":"bare","branch_ref":"root_000849/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:5:4:1","qac_word_ref":"114:5:4","surface_ar":"صُدُورِ"}],"gloss":"bir şeyin bölümü ya da kümesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin belirli olmayan bölümünü veya onun içindeki bir kümeyi belirtir."}}],"root_ar":"ص د ر","root_id":"root_000849","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bütünden ayrılan parçanın veya onun içindeki grubun oranı ve konumu belirtilmediğinde kullanılır.","boundary_detail":"Dal, bütünün herhangi bir bölümünü veya kümesini belirtir; ilk bölüm, beden parçası ya da sabit oran koşulu taşımaz.","branch_image_ar":"الطائفة من الشيء","concept_gloss":"bir şeyin bölümü ya da kümesi","contextual_glosses":[{"applicability":"Bir bütünün oranı belirtilmeyen kısmından söz edildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bütüne bağlı ve oranı belirtilmeyen parça anlamını korur."},"facet_ids":["F001"],"text":"bir bölüm","usage_role":"general"},{"applicability":"Bir şeyin içinden birlikte ele alınan topluluk veya grup kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bütün içindeki öğelerin birlikte bir grup oluşturması anlamını korur."},"facet_ids":["F001"],"text":"bir küme","usage_role":"contextual"}],"definition":"Bir bütünün içinden ayrılan veya onun kapsamında düşünülen bölüm ya da kümedir. Bölümün yeri, büyüklüğü ve oranı anlam tarafından belirlenmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin belirli olmayan bölümünü veya onun içindeki bir kümeyi belirtir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Bütünün dokuz eşit parçaya ayrılması koşulunu ekler.","collision":"Belirli kesir bildiren komşu dalla karışır.","fit":"narrowing","loses":"Bölümün herhangi bir büyüklükte veya küme niteliğinde olabilmesi kapsamını kaybeder.","preserves":"Bir bütünün parçası olma özelliğini korur."},"text":"dokuzda bir"}],"identity_rationale":"Kaynak ifadesi, biçimi doğrudan bir şeyin bölümü veya ondan ayrılan topluluk anlamında tanımlar. Geçici çerçeve bu kısa ve bağımsız anlamı ne bütünün başı anlamıyla ne de belirli bir kesirle karıştırır.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"bir şeyin bölümü ya da kümesi"}],"lexicalization_note":"Çıplak biçimin bölüm veya küme anlamı tanımlanır; bölme eylemi, belirli kesirler ve başka yapılara bağlı özel anlamlar kapsama alınmaz.","neighbor_coverage_note":"Bütün adaylar genel parça, özel organ veya pay, sabit kesir ve tam bütün sınırları bakımından değerlendirildi; yayımlanan üç karşılaştırma dalın oranı belirsiz bölüm anlamını yeterince ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ad olarak bölüm anlamında büyük ölçüde örtüşürler; komşunun bölme işlemi ve bütünün kuruluşuna ilişkin kapsamı tam eşanlamlılığı engeller.","focus_only":"Odak dalı yalnız bölümün veya kümenin adını verir ve bir işlem gerektirmez.","gloss":"bölüm veya parça","neighbor_only":"Komşu dal bölme işlemini ve parçaların bütünü kuran yapısal öğeler olmasını da kapsar.","neighbor_ref":"root_000241/B002","relation_type":"near_synonym","shared_zone":"Her iki dal bir bütünün bölümü veya içindeki topluluk anlamında kullanılabilir."},{"boundary_match":"partial","distinction":"Odak belirlenmemiş bölüm ya da kümedir; komşu organ, et parçası ve pay gibi özelleşmiş parça türlerine uzanır.","focus_only":"Odak dalı cansız veya soyut bir bütün içindeki kümeyi de genel olarak kapsar.","gloss":"parça","neighbor_only":"Komşu dal beden organı, et parçası ve kişiye düşen pay gibi daha özel bölüm türlerini kapsar.","neighbor_ref":"root_000024/B003","relation_type":"near_synonym","shared_zone":"İki dal bir bütünden ayrılan bölüm anlamında birbirine yaklaşır."},{"boundary_match":"opposed","distinction":"Odak kapsamı bütünün bir kesimiyle sınırlar; komşu aynı varlığın eksiksiz tamamını kapsar.","focus_only":"Odak dalı bütünün içindeki yalnız bir bölüm veya kümeyi belirtir.","gloss":"bölüm ve bütün","neighbor_only":"Komşu dal hiçbir bölüm dışarıda kalmadan şeyin tamamını belirtir.","neighbor_ref":"root_000030/B005","relation_type":"antonym","shared_zone":"İki dal aynı şeyin ne kadarının kapsandığını belirleyen parça-bütün eksenindedir."}],"source_phrase_ar":"الصدر الطائفة من الشيء (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu bölüm veya küme anlamı, sağlanan kanıtta tek bir sözlük tarafından kaydedilmiştir."}],"source_summary":"Dal, bir bütünün belirli olmayan bölümü veya onun içindeki bir küme anlamını taşır; konum ve oran bakımından ek koşul bildirmez.","sources":["SI"],"what_is_ar":"الصدر بمعنى طائفة من الشيء","what_is_not_ar":"صدر الشيء بمعنى أوله؛ الصدر الجارحة؛ الصدور عن الماء"},"support_links":[]},{"boundary":"Dal, duyulabilir hafif sesten ve telkini yapan varlığın adından ayrılır; burada tanımlanan şey insanın içinde beliren konuşma ya da telkindir.","branch_kind":"mixed_non_bare","branch_ref":"root_001651/B001","candidate_links":[{"candidate_id":"cand_b95e4d1f7ff65b7fc9d2","lane":"micro"},{"candidate_id":"cand_9d8949e8b05a172f4f31","lane":"micro"},{"candidate_id":"cand_aeba23498e823c5c102a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَسْوَسَ","morph_features":"STEM|POS:V|IMPF|LEM:wasowasa|ROOT:wsws|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"114:5:2:1","qac_word_ref":"114:5:2","surface_ar":"يُوَسْوِسُ"}],"gloss":"sessiz iç konuşma veya kötülüğe yönelten iç telkin","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanın kendi içinde, dışarıdan duyulan bir ses oluşturmadan beliren konuşmadır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İçerik, kötülüğe yönelten ve ansızın gelip geçen kötü bir düşünce niteliği taşıyabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İç konuşma kişinin kendisinden doğabilir ya da kötücül bir ayartıcının kalbe yönelttiği telkin olarak anlatılabilir."}}],"root_ar":"و س و س","root_id":"root_001651","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem kişinin kendi içinde doğan konuşma çekirdeğini hem de dış bir kötücül ayartıcıya bağlanan kötü telkin görünümünü birlikte karşılar.","boundary_detail":"Dal, duyulabilir hafif sesten ve telkini yapan varlığın adından ayrılır; burada tanımlanan şey insanın içinde beliren konuşma ya da telkindir.","branch_image_ar":"حديث النفس الخفي","concept_gloss":"sessiz iç konuşma veya kötülüğe yönelten iç telkin","contextual_glosses":[{"applicability":"Kişinin kendi içinde oluşan ve dışarıdan duyulmayan öz konuşmanın anlatıldığı bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kötücül bir kaynaktan kalbe yöneltilen telkin ile gelip geçici kötü düşünce ayrıntısını dışarıda bırakır.","preserves":"Kişinin içinde sessizce beliren konuşma yönünü korur."},"facet_ids":["F001"],"text":"içinden konuşma","usage_role":"contextual"},{"applicability":"Bir ayartıcının başka birinin içine kötülüğe yönelten bir telkin bıraktığı bağlamlarda eylem karşılığı olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin kendiliğinden oluşan genel iç konuşmasını ve telkinin yalnızca bir düşünce olarak belirmesini kapsamaz.","preserves":"Kötü telkinin bir kaynaktan kişiye yöneltilmesi ilişkisini korur."},"facet_ids":["F002","F003"],"text":"içine kötü bir düşünce düşürme","usage_role":"contextual"},{"applicability":"Kısa süreli kötü bir düşüncenin ansızın belirmesinin öne çıktığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Süregelen iç konuşma ile düşünceyi başka bir katılımcının yöneltmesi ihtimalini açıkça göstermez.","preserves":"Gelip geçici kötü düşüncenin insanın içinde belirmesini korur."},"facet_ids":["F002"],"text":"aklına kötü bir düşünce gelmesi","usage_role":"contextual"}],"definition":"İnsanın içinde duyulur bir ses olmadan beliren iç konuşma ya da kötü ve gelip geçici düşüncedir. Kişinin kendi içinden doğabilir veya kötülüğe çağıran görünmez bir varlığın kalbe yönelttiği telkin olarak tasarlanabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanın kendi içinde, dışarıdan duyulan bir ses oluşturmadan beliren konuşmadır."},{"facet_id":"F002","role":"specialization","statement":"İçerik, kötülüğe yönelten ve ansızın gelip geçen kötü bir düşünce niteliği taşıyabilir."},{"facet_id":"F003","role":"extension","statement":"İç konuşma kişinin kendisinden doğabilir ya da kötücül bir ayartıcının kalbe yönelttiği telkin olarak anlatılabilir."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":"Güncel kullanımda kaygı, kuşku ve sürekli kuruntu çağrışımlarını gereğinden fazla öne çıkarabilir.","collision":"Aynı kökün burada tanımlanmayan yerleşik Türkçe kullanımına doğrudan yaslanır.","fit":"drifted_loanword","loses":"Nötr iç konuşma çekirdeğini ve telkinin kişiden ya da dış bir ayartıcıdan gelebilmesi ayrımını belirsizleştirir.","preserves":"Yerleşik kullanımda kötü ve rahatsız edici iç düşünce çağrışımını korur."},"text":"vesvese"}],"identity_rationale":"Kaynak ifadesi bu dalı duyulur bir ses olarak değil, insanın içinde beliren konuşma ve kötü, gelip geçici düşünce olarak kurar. Bu içerik kişinin kendi içinden doğabildiği gibi kötülüğe çağıran görünmez bir varlığın kalbe yönelttiği telkin olarak da anlatılır; sağlanan dal çerçevesi bu ayrımları doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"sessiz iç konuşma; kötülüğe yönelten iç telkin"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"birinin içine kötü bir düşünce düşürmek veya ona içten telkinde bulunmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"insanın göğsünde sessiz bir iç konuşma belirmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"iç telkinlerin etkisine kapılmış, sürekli kuruntu duyan"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"sessiz iç konuşma veya iç fısıltı"}],"lexicalization_note":"Tanım, bağımsız biçimlerin iç konuşma anlamını kapsarken birine yöneltme ve göğüste belirme gibi bağıntılı kullanımları ayrı tutar; bu yapılar bütün dalın zorunlu kalıbı sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Duyulur hafif ses, ayartıcının adı, gizli kişiler arası konuşma ve akıl bozukluğu sınırı en yararlı karşıtlıkları verdi; kalan adaylar yalnızca kalp, gizlilik, aldatma veya kötülüğe yöneltme temasını paylaştığından ayrıca yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal zihinsel bir içerik ve telkin ilişkisi kurar; komşu dal ise rüzgâr, takı, avcı ya da hareket eden nesne gibi kaynaklardan çıkan gerçek bir sesi anlatır. Bu nedenle biri ötekinin yerine kullanılamaz.","focus_only":"İnsanın içinde beliren ve dışarıdan duyulmayan konuşma ya da kötü telkindir.","gloss":"belli belirsiz ses","neighbor_only":"Kulakla algılanabilen hafif ses veya bir nesnenin belli belirsiz hareket sesidir.","neighbor_ref":"root_001651/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da düşük belirginlik ve fısıltıyı andıran gizlilik niteliği bulunur."},{"boundary_match":"thematic_only","distinction":"Odak dal, kişinin içinde oluşan etkinin kendisini anlatır; komşu dal ise bu etkiyi oluşturduğu düşünülen varlığın adlandırılmasıdır. Eylem veya içerik ile katılımcının adı aynı anlam değildir.","focus_only":"Kalpte veya insanın kendi içinde beliren konuşma, dürtü ya da kötü düşüncedir.","gloss":"kötücül ayartıcının adı","neighbor_only":"Kötülüğe sürükleyen görünmez varlık için kullanılan sözlükleşmiş addır.","neighbor_ref":"root_001651/B003","relation_type":"thematic","shared_zone":"Kötücül ayartıcının kişiye kötü düşünce yönelttiği aynı anlatı düzeninde yer alırlar."},{"boundary_match":"partial","distinction":"Odak dalda konuşma zihnin içindedir ve işitsel bir olay olmak zorunda değildir; komşu dalda ise kişiler arasında gerçekten söylenen, yalnızca sesi kısılmış bir konuşma vardır.","focus_only":"Dışarıdan işitilen gizli konuşma değil, insanın içinde beliren sessiz konuşma ve telkindir.","gloss":"gizli konuşma","neighbor_only":"İki kişinin korku veya gizlilik nedeniyle birbirine alçak sesle söylediği özel konuşmadır.","neighbor_ref":"root_001497/B006","relation_type":"near_neighbor","shared_zone":"Her ikisi de başkalarınca işitilmeyen veya kolayca fark edilmeyen konuşma düşüncesini taşır."},{"boundary_match":"field_only","distinction":"Odak dal tekil bir iç konuşma, dürtü veya telkin olabilir ve kalıcı bir bozukluk bildirmez. Komşu dal ise düşünme yetisinin bozulmasını ya da buna benzetilen daha kapsamlı bir durumu çekirdek edinir.","focus_only":"Sessiz iç konuşma veya kısa süreli kötü telkin olup akıl yetisinin bozulmasını gerektirmez.","gloss":"akıl ve kalp bozukluğu","neighbor_only":"Akıl ve düşünme yetisinin bozulması, hastalık ya da taşkınlık durumunu anlatır.","neighbor_ref":"root_000390/B001","relation_type":"same_field","shared_zone":"İnsanın iç dünyasında düşünceyi ve davranışı etkileyebilen olumsuz durumlarla ilgilidirler."}],"source_phrase_ar":"الوسوسة حديث النفس؛ وسوس إلي ووسوس في صدري (ayn)؛ الوسوسة ما يلقيه الشيطان في القلب (jamhara)؛ الوسوسة حديث النفس؛ وسوست إليه نفسه؛ فوسوس لهما الشيطان (sihah)؛ الوسوسة الخطرة الرديئة؛ فوسوس إليه الشيطان (mufradat)","source_summary":"Tanıklıkların ortak çekirdeği sessiz iç konuşmadır; buna kişinin kendi içinde doğan telkin, kalbe yöneltilen kötücül dürtü ve gelip geçici kötü düşünce anlatımları eklenir.","sources":["AY","JA","SI","MU"],"what_is_ar":"حديث النفس والوسوسة في الصدر وما يلقيه الشيطان في القلب والخطرة الرديئة","what_is_not_ar":"ليس الصوت الحسي الخفي ولا اسم الشيطان"},"support_links":["sup_0c8db3cf8704202747d7","sup_47182ebabb01fee7ab8a","sup_56f18f1d10bff16cca6c"]},{"boundary":"Dalın zorunlu sınırı işitilebilir bir ses bulunmasıdır; sessiz iç konuşma ve kötücül ayartıcının adı bu anlamın dışında kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_001651/B002","candidate_links":[{"candidate_id":"cand_7451b057185aa50c0afa","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَسْوَسَ","morph_features":"STEM|POS:V|IMPF|LEM:wasowasa|ROOT:wsws|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"114:5:2:1","qac_word_ref":"114:5:2","surface_ar":"يُوَسْوِسُ"}],"gloss":"belli belirsiz ses veya hafif hareket sesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kulakla algılanan, ancak alçaklığı veya belirsizliği nedeniyle güç seçilen sestir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir nesnenin kendisi değil, hafif hareketi işitildiğinde ortaya çıkan ses bu dalın nesneye bağlı görünümüdür."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Takıların sesi, rüzgârın kamışları oynatırken çıkardığı ses ve avcının alçak fısıltısı örnekler arasındadır."}}],"root_ar":"و س و س","root_id":"root_001651","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın genel gizli ses çekirdeğini ve bir nesnenin duyulan hafif hareketine bağlı özel kullanımını birlikte karşılar.","boundary_detail":"Dalın zorunlu sınırı işitilebilir bir ses bulunmasıdır; sessiz iç konuşma ve kötücül ayartıcının adı bu anlamın dışında kalır.","branch_image_ar":"صوت خفي","concept_gloss":"belli belirsiz ses veya hafif hareket sesi","contextual_glosses":[{"applicability":"Rüzgârın kamışlarda veya hafifçe hareket eden bir nesnede çıkardığı belli belirsiz ses için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan fısıltısını ve hışırtı niteliği taşımayan hafif takı seslerini kapsamakta yetersiz kalır.","preserves":"Hafif hareketten doğan güç seçilir sesi doğal biçimde karşılar."},"facet_ids":["F001","F002","F003"],"text":"hafif hışırtı","usage_role":"contextual"},{"applicability":"Avcının veya başka bir konuşanın sesini duyurmadan yaptığı alçak konuşmanın öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Rüzgâr, takı ve başka nesnelerin hareketinden doğan insan dışı sesleri dışarıda bırakır.","preserves":"İnsan sesinin alçak ve güç seçilir olmasını korur."},"facet_ids":["F001","F003"],"text":"gizli fısıltı","usage_role":"contextual"},{"applicability":"Bir nesnenin hafif hareketinin doğrudan işitildiğini belirten yapıya bağlı kullanımın açık karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Belirli bir nesne hareketine bağlı olmayan genel hafif ses ve insan fısıltısı kullanımlarını kapsamaz.","preserves":"Nesne hareketi ile ondan çıkan hafif ses arasındaki bağı bütünüyle korur."},"facet_ids":["F002"],"text":"bir nesnenin belli belirsiz hareket sesi","usage_role":"explanatory"}],"definition":"Duyulabilen fakat alçak ve belli belirsiz kalan ses ya da bir nesnenin hafif hareketinden çıkan sestir. Takının sesi, kamışı titreten rüzgâr ve avcının fısıltısı bu çekirdeğin farklı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kulakla algılanan, ancak alçaklığı veya belirsizliği nedeniyle güç seçilen sestir."},{"facet_id":"F002","role":"specialization","statement":"Bir nesnenin kendisi değil, hafif hareketi işitildiğinde ortaya çıkan ses bu dalın nesneye bağlı görünümüdür."},{"facet_id":"F003","role":"example","statement":"Takıların sesi, rüzgârın kamışları oynatırken çıkardığı ses ve avcının alçak fısıltısı örnekler arasındadır."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":"Güncel Türkçede iç sıkıntısı, kötü düşünce ve kuruntu anlamlarını getirir.","collision":"Aynı kökün sessiz iç konuşma dalıyla karışmaya yol açar.","fit":"drifted_loanword","loses":"İşitilebilir hafif ses, fısıltı ve nesne hareketinden çıkan ses özelliklerinin tümünü kaybeder.","preserves":"Sözcüğün tarihsel biçim bağını korusa da ses anlamını açıklamaz."},"text":"vesvese"}],"identity_rationale":"Kaynak ifadesi dalı açıkça hafif ve gizli ses ile ancak sesi üzerinden fark edilen hareket çevresinde kurar. Rüzgârın kamışı oynatması, takı sesi ve avcının fısıltısı gibi örnekler duyulabilirlik çekirdeğini doğrular; sağlanan çerçeve iç konuşmayı bu daldan doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"gizli, hafif ses veya duyulabilen belli belirsiz hareket sesi"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir nesnenin duyulan hafif hareket sesi"}],"lexicalization_note":"Bağımsız biçim genel olarak belli belirsiz sesi adlandırırken, nesneyle kurulan yapı yalnız o nesnenin duyulan hafif hareketine bağlıdır; bu yapıya özgü sınır genel sese yüklenmez.","neighbor_coverage_note":"Adayların tamamı karşılaştırıldı. Sessiz iç konuşma, genel hafif ses, görülmeden sezilen hareket, hareket hışırtısı ve gizli ayak sesi en açıklayıcı sınırları sundu; yüksek ya da kırılan ses, gürültü, görünür yayılma ve adlaşmış kötücül varlık adayları çekirdeği daha fazla keskinleştirmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal rüzgâr, takı, avcı veya hareket eden nesne gibi bir ses kaynağı ve işitsel algı gerektirir. Komşu dalın olayı zihnin içindedir; dışarıdan işitilmesi anlamın parçası değildir.","focus_only":"Dış dünyada oluşan ve kulakla algılanabilen hafif ses ya da hareket sesidir.","gloss":"sessiz iç konuşma","neighbor_only":"Duyulur ses olmadan insanın içinde beliren konuşma veya kötü telkindir.","neighbor_ref":"root_001651/B001","relation_type":"near_neighbor","shared_zone":"İki dal da düşük belirginlik ve fısıltıyı andıran gizlilik niteliği taşır."},{"boundary_match":"partial","distinction":"Odak dal özellikle gizli işitimi ve kimi kullanımlarda nesne hareketinin duyulmasını öne çıkarır. Komşu dalın kapsamı genel ses ile yalnızca şiddetli olmayan sesi de içine aldığı için bütünüyle örtüşmez.","focus_only":"Takı, rüzgâr, avcı ve duyulan nesne hareketi gibi belirgin gerçekleşmeleri kapsar.","gloss":"hafif ve belirsiz ses","neighbor_only":"Yalnızca şiddetli olmayan sesi de kapsayabildiği için gizlilik ve hareket bağı daha gevşektir.","neighbor_ref":"root_001464/B006","relation_type":"near_synonym","shared_zone":"Her iki dalın çekirdeğinde alçak, gizli veya güç seçilir bir ses bulunur."},{"boundary_match":"partial","distinction":"Odak dalda algı işitseldir ve tanıklıklar sesi merkeze alır. Komşu dal ise gizli hareketin ses dışında duyumsanmasına da açıldığı için daha geniş bir algı alanına sahiptir.","focus_only":"Sesin rüzgâr, takı, fısıltı veya bir nesnenin hafif hareketinden çıkması gibi işitsel gerçekleşmeleri vardır.","gloss":"gizli ses veya hareket duyumu","neighbor_only":"Hareketin görülmeden başka bir duyu yoluyla sezilmesini de kapsayabilir.","neighbor_ref":"root_000321/B003","relation_type":"near_synonym","shared_zone":"İkisi de kaynağı açıkça görülmeden fark edilen hafif ses ya da hareket izlenimini kapsar."},{"boundary_match":"partial","distinction":"Odak dal için güç seçilirlik belirleyicidir ve insan fısıltısı gibi hareket hışırtısı olmayan sesleri de içerir. Komşu dal ise hareketin çıkardığı hışırtı türüne dayanır ve sesin mutlaka gizli olmasını gerektirmez.","focus_only":"İnsan fısıltısı ve hareket kaynağı belirtilmeyen belli belirsiz ses de kapsama girer.","gloss":"hareketten doğan hışırtı","neighbor_only":"Ağaç, kanat, at, yağmur veya ateş gibi bir kaynağın hareketinden çıkan hışırtıyı çekirdek edinir.","neighbor_ref":"root_000343/B002","relation_type":"near_neighbor","shared_zone":"Hafifçe hareket eden bir şeyin çıkardığı hışırtılı seste iki dal örtüşebilir."},{"boundary_match":"partial","distinction":"Odak dal ses türü bakımından geniş, kaynak bakımından serbesttir. Komşu dal ise yürüyenin ayak basışına ve adımlarını gizlemesine özgü bir hareket biçimini tanımlar.","focus_only":"Takı, rüzgâr, fısıltı ve çeşitli nesne hareketlerinden çıkan bütün belli belirsiz sesleri kapsar.","gloss":"gizli ayak sesi","neighbor_only":"Özellikle ayağın yere basışının ve yürüyüşün gizliliğine bağlıdır.","neighbor_ref":"root_001601/B002","relation_type":"near_neighbor","shared_zone":"Güç işitilen bir hareket sesinde, özellikle hafif adım sesinde anlam alanları kesişebilir."}],"source_phrase_ar":"الوسواس الصوت الخفي من ريح تهز قصبا ونحوه؛ صوت الحلي؛ همس الصائد وكلامه (ayn)؛ وسوسة الشيء إذا سمعت حركته (jamhara)؛ همس الصائد والكلاب وأصوات الحلى وسواس (sihah)؛ صوت الحلي والهمس الخفي؛ همس الصائد وسواس (mufradat)","source_summary":"Ortak tanıklık belli belirsiz fakat işitilebilir sesi merkeze alır; hafif nesne hareketi, takı sesi, rüzgârın oluşturduğu ses ve avcının alçak konuşması bu anlamın örnekleridir.","sources":["AY","JA","SI","MU"],"what_is_ar":"الصوت الخفي والحركة المسموعة الخفية مثل صوت الحلي والريح وهمس الصائد ونحوه","what_is_not_ar":"ليس حديث النفس ولا ما يلقيه الشيطان في القلب ولا اسم الشيطان"},"support_links":["sup_1b7f8f0ac53eb4f64837"]},{"boundary":"Dal bir olay ya da nitelik değil, belirli bir kötücül katılımcı için sözlükleşmiş ad kullanımıdır.","branch_kind":"bare","branch_ref":"root_001651/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَسْوَسَ","morph_features":"STEM|POS:V|IMPF|LEM:wasowasa|ROOT:wsws|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"114:5:2:1","qac_word_ref":"114:5:2","surface_ar":"يُوَسْوِسُ"}],"gloss":"kötülüğe sürükleyen görünmez varlığın sözlükleşmiş adı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözlük kullanımında kötülüğe yönelten görünmez varlığı adlandırır."}}],"root_ar":"و س و س","root_id":"root_001651","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözün bir iç telkini değil, o telkinin kötücül kaynağı sayılan varlığı ad olarak gösterdiği kullanımın tam açıklamasıdır.","boundary_detail":"Dal bir olay ya da nitelik değil, belirli bir kötücül katılımcı için sözlükleşmiş ad kullanımıdır.","branch_image_ar":"الوسواس الشيطان","concept_gloss":"kötülüğe sürükleyen görünmez varlığın sözlükleşmiş adı","contextual_glosses":[{"applicability":"Adın biçiminden çok anlatıdaki katılımcının işlevinin okura aktarılmasının gerektiği bağlamlarda kullanılabilir.","error_profile":{"adds":"Özel adlandırmayı genel bir işlev adı gibi gösterir.","collision":"Başka kötücül ayartıcıları da kapsayabilen genel bir nitelemeyle karışır.","fit":"displacement","loses":"Belirli bir sözün bu varlığa verilmiş sözlükleşmiş ad olması bilgisini kaybeder.","preserves":"Gösterilen varlığın insanı kötülüğe yönelten işlevini korur."},"facet_ids":["F001"],"text":"kötücül ayartıcı","usage_role":"explanatory"}],"definition":"Kötülüğe sürükleyen görünmez varlık için kullanılan sözlükleşmiş addır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözlük kullanımında kötülüğe yönelten görünmez varlığı adlandırır."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":"Güncel Türkçede kötü düşünce, iç sıkıntısı ve kuruntu anlamlarını getirir.","collision":"Kökün iç konuşma ve kötü telkin dalıyla doğrudan karışır.","fit":"drifted_loanword","loses":"Kötülüğe sürükleyen görünmez varlığın sözlükleşmiş adı olma özelliğini tümüyle kaybeder.","preserves":"Aynı tarihsel söz biçimini yansıtır ancak adlandırılan katılımcıyı korumaz."},"text":"vesvese"}],"identity_rationale":"Kaynak ifadesi sözü doğrudan kötülüğe sürükleyen görünmez varlığın adı olarak tanımlar. Bu, ne içte beliren telkinin kendisi ne de hafif bir sestir; sağlanan dal kimliği adlandırma işlevini doğru ve yeterli biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kötülüğe sürükleyen görünmez varlığın adı"}],"lexicalization_note":"Tanım yalnız bağımsız biçimin sözlükleşmiş ad işlevini verir; iç konuşmaya veya belirli bir söz dizimsel yapıya özgü anlam bu dala aktarılmaz.","neighbor_coverage_note":"Bütün komşu adayları incelendi. Geniş kötücül varlık sınıfı, iç telkin, eş biçimli hafif ses ve saptırma eylemi dalın adlandırma sınırını yeterince gösterdi; kapıp götüren varlık, iz, sapkınlık önderi, başkaldıran kişi ve ilgisiz özel ad adayları ek bir anlam örtüşmesi sağlamadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir adlandırma kullanımını tanımlar. Komşu dal ise azgınlık ve başkaldırma niteliğine göre çok daha geniş bir varlık sınıfı kurar; bu nedenle yalnız ortak gönderge bulunan bağlamlarda yaklaşırlar.","focus_only":"Kötülüğe sürükleyen görünmez varlık için kullanılan belirli bir sözlükleşmiş addır.","gloss":"azgın ve başkaldıran kötücül varlık","neighbor_only":"İnsan, görünmez varlık veya hayvan arasında azgın ve başkaldıran her tür varlığı kapsayabilir.","neighbor_ref":"root_000796/B004","relation_type":"near_synonym","shared_zone":"Kötülüğe yönelten görünmez varlık iki dalın ortak ve merkezi göndergesi olabilir."},{"boundary_match":"thematic_only","distinction":"Odak dal katılımcıyı adlandırır; komşu dal ise bu katılımcıya bağlanabilen iç etkiyi veya kişinin kendi iç konuşmasını anlatır. Kaynak ile ortaya çıkan içerik birbirinin yerine geçmez.","focus_only":"Kötü telkinin kaynağı kabul edilen varlığın sözlükleşmiş adıdır.","gloss":"sessiz iç telkin","neighbor_only":"İnsanın içinde beliren konuşma, kötü düşünce veya kalbe yöneltilen telkindir.","neighbor_ref":"root_001651/B001","relation_type":"thematic","shared_zone":"Adlandırılan varlığın insanın içinde kötü düşünce uyandırdığı aynı anlatı çerçevesini paylaşırlar."},{"boundary_match":"field_only","distinction":"Odak dal bir varlığın adıdır ve ses niteliği bildirmez. Komşu dal ise bütünüyle işitsel bir olayı tanımlar; biçim ortaklığı iki anlam arasında yerine geçebilirlik oluşturmaz.","focus_only":"Kötücül bir varlığın sözlükleşmiş adı olarak kişi benzeri bir gönderge taşır.","gloss":"belli belirsiz ses","neighbor_only":"Rüzgâr, takı, avcı veya nesne hareketinden çıkan belli belirsiz işitilebilir sestir.","neighbor_ref":"root_001651/B002","relation_type":"other","shared_zone":"Aynı söz biçiminin sözlükte kaydedilmiş farklı kullanımları olmaları dışında ortak çekirdekleri yoktur."},{"boundary_match":"thematic_only","distinction":"Odak dal eyleyen varlığın adıyla ilgilidir; komşu dal ise bu varlığın da gerçekleştirebileceği yön değiştirme ve saptırma eylemini tanımlar. Katılımcı adı eylemin anlamını taşımaz.","focus_only":"Kötülüğe yönelten varlığın kendisini belirli bir adla gösterir.","gloss":"doğru yoldan saptırma","neighbor_only":"Birini doğrudan doğru yoldan saptırma, ayartma veya önceki durumundan uzaklaştırma eylemidir.","neighbor_ref":"root_001128/B003","relation_type":"thematic","shared_zone":"Kötücül bir katılımcının insanı doğru olandan uzaklaştırdığı senaryoda birlikte bulunabilirler."}],"source_phrase_ar":"الوسواس اسم الشيطان (ayn;sihah)","source_summary":"Tanıklıklar bu kullanımı bir eylem veya iç düşünce olarak değil, kötülüğe yönelten görünmez varlığa verilen ad olarak ortak biçimde kaydeder.","sources":["AY","SI"],"what_is_ar":"إطلاق الوسواس اسما على الشيطان في الاستعمال المعجمي","what_is_not_ar":"ليس مطلق الصوت الخفي ولا مطلق حديث النفس"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["114:5:1"],"branch_refs":[],"candidate_id":"cand_be86cef05bcdd9efc1f1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:5:1:antecedent-bound-relative","source_type":"word_analysis","support_ids":["sup_582a902878fcedf8e71f","sup_ff43a5a1cc6f01a52e4a"],"title":"the relative pronoun carries the prior whisperer across the ayah boundary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:1","qac_refs":["114:5:1:1"],"status":"accepted"}},{"anchor_refs":["114:5:1"],"branch_refs":[],"candidate_id":"cand_c0867c68aaa500b056cc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:5:1:defining-relative-clause","source_type":"word_analysis","support_ids":["sup_31a40a2e842f8e0e2d84","sup_ff43a5a1cc6f01a52e4a"],"title":"the following clause defines the threat by action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:1","qac_refs":["114:5:1:1"],"status":"accepted"}},{"anchor_refs":["114:5:2"],"branch_refs":[],"candidate_id":"cand_2f5d81d67fd1afef0caf","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001651"],"scope":"focus_ayah","source_local_id":"114:5:2:compressed-subject-agency","source_type":"word_analysis","support_ids":["sup_345812fec3f8c4815a38","sup_3aa1bc8e35dfd2e8ba86"],"title":"the subject is compressed into the verb and relative chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:2","qac_refs":["114:5:2:1"],"status":"accepted"}},{"anchor_refs":["114:5:2"],"branch_refs":[],"candidate_id":"cand_1c7edc76d26acb3f146d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001651"],"scope":"focus_ayah","source_local_id":"114:5:2:inward-soundlike-insinuation","source_type":"word_analysis","support_ids":["sup_345812fec3f8c4815a38","sup_5ea068c85e9296a403b4"],"title":"audible whisper imagery is transferred into the chest","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:2","qac_refs":["114:5:2:1"],"status":"accepted"}},{"anchor_refs":["114:5:2"],"branch_refs":[],"candidate_id":"cand_22d5d6ab05e4557ee151","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001651"],"scope":"focus_ayah","source_local_id":"114:5:2:name-into-action-reprise","source_type":"word_analysis","support_ids":["sup_345812fec3f8c4815a38","sup_7d8f57b5e4bec179a4f0"],"title":"the prior whisperer noun becomes a verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:2","qac_refs":["114:5:2:1"],"status":"accepted"}},{"anchor_refs":["114:5:2"],"branch_refs":[],"candidate_id":"cand_af73427bc8725164ed45","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001651"],"scope":"focus_ayah","source_local_id":"114:5:2:objectless-locative-frame","source_type":"word_analysis","support_ids":["sup_123884bc4d822db7492e","sup_345812fec3f8c4815a38"],"title":"the verb leaves content unspoken and routes the action to an interior locus","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:2","qac_refs":["114:5:2:1"],"status":"accepted"}},{"anchor_refs":["114:5:2"],"branch_refs":[],"candidate_id":"cand_fa514698509bf56199da","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001651"],"scope":"focus_ayah","source_local_id":"114:5:2:rare-field-role-contrast","source_type":"word_analysis","support_ids":["sup_345812fec3f8c4815a38","sup_d152790a1000d2581167"],"title":"the rare whispering field contrasts external and internal sources","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:2","qac_refs":["114:5:2:1"],"status":"accepted"}},{"anchor_refs":["114:5:2"],"branch_refs":[],"candidate_id":"cand_1ef4339056e1e4effa39","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001651"],"scope":"focus_ayah","source_local_id":"114:5:2:reduplicated-imperfect-sound","source_type":"word_analysis","support_ids":["sup_345812fec3f8c4815a38","sup_b8e4630c0db56d3fe408"],"title":"form, aspect, and sound all repeat the whispering","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:2","qac_refs":["114:5:2:1"],"status":"accepted"}},{"anchor_refs":["114:5:3"],"branch_refs":[],"candidate_id":"cand_9bf124b397b6062342f6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:5:3:action-to-locus-architecture","source_type":"word_analysis","support_ids":["sup_997ea39cd3132804ab00","sup_a9bcf038ce1913d1acb6"],"title":"the preposition pivots the clause from act to landing-site","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:3","qac_refs":["114:5:3:1"],"status":"accepted"}},{"anchor_refs":["114:5:3"],"branch_refs":[],"candidate_id":"cand_93ede7c484351ee1f618","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:5:3:full-named-locus-slot","source_type":"word_analysis","support_ids":["sup_a9bcf038ce1913d1acb6","sup_ee5cd60b3a2699feb23d"],"title":"the standalone preposition opens a full named locus","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:3","qac_refs":["114:5:3:1"],"status":"accepted"}},{"anchor_refs":["114:5:3"],"branch_refs":[],"candidate_id":"cand_62749d451f3b435d9f38","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:5:3:locative-penetrative-containment","source_type":"word_analysis","support_ids":["sup_99153a56e919fe465884","sup_a9bcf038ce1913d1acb6"],"title":"the preposition places the whispering inside the chest-space","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:3","qac_refs":["114:5:3:1"],"status":"accepted"}},{"anchor_refs":["114:5:4"],"branch_refs":[],"candidate_id":"cand_82395e7afe6a6dd459ec","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"114:5:4:chest-echoes-and-role-boundary","source_type":"word_analysis","support_ids":["sup_390561d2f3317f3c6d02","sup_bd257e1af2d83da09a8f"],"title":"the same interior locus is vulnerable here and repairable elsewhere","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:4","qac_refs":["114:5:4:1"],"status":"accepted"}},{"anchor_refs":["114:5:4"],"branch_refs":[],"candidate_id":"cand_ef23df7751b0dac6409a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"114:5:4:embodied-hidden-interiority","source_type":"word_analysis","support_ids":["sup_390561d2f3317f3c6d02","sup_4393cf59614f61584d0d"],"title":"literal chest image becomes the hidden interior locus","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:4","qac_refs":["114:5:4:1"],"status":"accepted"}},{"anchor_refs":["114:5:4"],"branch_refs":[],"candidate_id":"cand_067be6b32374530e6066","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"114:5:4:governed-construct-hinge","source_type":"word_analysis","support_ids":["sup_02ada5b83e80f460dfab","sup_390561d2f3317f3c6d02"],"title":"the chest noun links the preposition to the human possessor","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:4","qac_refs":["114:5:4:1"],"status":"accepted"}},{"anchor_refs":["114:5:4"],"branch_refs":[],"candidate_id":"cand_d1c0f1a01e926e1cd303","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"114:5:4:plural-possessed-distribution","source_type":"word_analysis","support_ids":["sup_390561d2f3317f3c6d02","sup_991edac97339931e77c8"],"title":"the broken plural construct distributes many human interiors","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:4","qac_refs":["114:5:4:1"],"status":"accepted"}},{"anchor_refs":["114:5:4"],"branch_refs":[],"candidate_id":"cand_9860e6dccfdc162aeb24","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"114:5:4:sound-and-cadence-binding","source_type":"word_analysis","support_ids":["sup_390561d2f3317f3c6d02","sup_c4a80ab568c71e8e0cf7"],"title":"cadence and consonant weight bind the chest to the phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:4","qac_refs":["114:5:4:1"],"status":"accepted"}},{"anchor_refs":["114:5:4"],"branch_refs":[],"candidate_id":"cand_f82b6e4f62a3d33ad074","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"114:5:4:source-issuing-pressure","source_type":"word_analysis","support_ids":["sup_390561d2f3317f3c6d02","sup_88387cfb92fe8d10763e"],"title":"source and issuing imagery pressures the chest without replacing it","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:4","qac_refs":["114:5:4:1"],"status":"accepted"}},{"anchor_refs":["114:5:5"],"branch_refs":[],"candidate_id":"cand_d78be9632ee2cb263bbe","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:5:5:article-assimilation-closing-sound","source_type":"word_analysis","support_ids":["sup_a3d310ad54907598a835","sup_e2a458626dc7d8ce6168"],"title":"article assimilation makes the final class noun audibly fused","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:5","qac_refs":["114:5:5:1","114:5:5:2"],"status":"accepted"}},{"anchor_refs":["114:5:5"],"branch_refs":[],"candidate_id":"cand_5ecaa033e95888515abc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:5:5:construct-definiteness-and-distribution","source_type":"word_analysis","support_ids":["sup_06d167eb95f84edf5553","sup_a3d310ad54907598a835"],"title":"final definiteness reaches back through plural chests","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:5","qac_refs":["114:5:5:1","114:5:5:2"],"status":"accepted"}},{"anchor_refs":["114:5:5"],"branch_refs":[],"candidate_id":"cand_4936264e25eb1315e426","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:5:5:definite-collective-scope","source_type":"word_analysis","support_ids":["sup_5e8741278bca2d1bf0fe","sup_a3d310ad54907598a835"],"title":"the definite collective closes the phrase at human class scale","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:5","qac_refs":["114:5:5:1","114:5:5:2"],"status":"accepted"}},{"anchor_refs":["114:5:5"],"branch_refs":[],"candidate_id":"cand_98bdc70af33ab95e6268","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:5:5:genitive-affected-possessor","source_type":"word_analysis","support_ids":["sup_a3d310ad54907598a835","sup_be02a7f4c4bc34ba255c"],"title":"mankind is possessed genitive yet semantically affected","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:5","qac_refs":["114:5:5:1","114:5:5:2"],"status":"accepted"}},{"anchor_refs":["114:5:5"],"branch_refs":[],"candidate_id":"cand_d4007a1f9b0b368d67b6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:5:5:human-interiority-and-whisper-field","source_type":"word_analysis","support_ids":["sup_981d6721aa203207970f","sup_a3d310ad54907598a835"],"title":"the final noun joins humanity to chest and whisper fields","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:5","qac_refs":["114:5:5:1","114:5:5:2"],"status":"accepted"}},{"anchor_refs":["114:5:5"],"branch_refs":[],"candidate_id":"cand_d0a6e20cc53d86194028","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:5:5:perception-sociability-forgetfulness-pressure","source_type":"word_analysis","support_ids":["sup_23b711296c8387e39b9e","sup_a3d310ad54907598a835"],"title":"human perception and familiarity pressure the target class","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:5","qac_refs":["114:5:5:1","114:5:5:2"],"status":"accepted"}},{"anchor_refs":["114:5:5"],"branch_refs":[],"candidate_id":"cand_5685ba2ca144d1c3ffe4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:5:5:surah-refrain-role-shift","source_type":"word_analysis","support_ids":["sup_a3d310ad54907598a835","sup_de29e39048d8df4b2219"],"title":"the repeated human noun shifts from protected class to target and source","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:5:5","qac_refs":["114:5:5:1","114:5:5:2"],"status":"accepted"}},{"anchor_refs":["114:5:2"],"branch_refs":[],"candidate_id":"cand_59f0dbaa270590799b55","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001651"],"scope":"focus_ayah","source_local_id":"114:5:2:1","source_type":"qac_morpheme","support_ids":["sup_103664d1098af7b6d9e9"],"title":"QAC root occurrence: و س و س","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["114:5:4"],"branch_refs":[],"candidate_id":"cand_652deaa2c3540718e812","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"114:5:4:1","source_type":"qac_morpheme","support_ids":["sup_06fb61cb6008fffb199f"],"title":"QAC root occurrence: ص د ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["114:5:5"],"branch_refs":[],"candidate_id":"cand_d366721e4884c91b9526","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000059"],"scope":"focus_ayah","source_local_id":"114:5:5:2","source_type":"qac_morpheme","support_ids":["sup_633cb373df8803f9e9db"],"title":"QAC root occurrence: ن و س","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["114:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"114:5","branch_refs":["root_000059/B006","root_000849/B001","root_001651/B001"],"candidate_id":"cand_b95e4d1f7ff65b7fc9d2","commentary_obligation":"review","hft_ref":"hft_d7dea31a6b9364cd8a5e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_covert_self_speech","source_type":"hft","support_ids":["sup_47182ebabb01fee7ab8a"],"title":"baseline_covert_self_speech","trust":"legacy_unbound"},{"anchor_refs":["114:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"114:5","branch_refs":["root_000059/B002","root_000849/B002","root_000849/B004","root_001651/B001"],"candidate_id":"cand_9d8949e8b05a172f4f31","commentary_obligation":"review","hft_ref":"hft_60751efd955cf76fd525","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_preaction_source","source_type":"hft","support_ids":["sup_0c8db3cf8704202747d7"],"title":"baseline_preaction_source","trust":"legacy_unbound"},{"anchor_refs":["114:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"114:5","branch_refs":["root_000059/B003","root_000059/B004","root_000849/B001","root_001651/B001"],"candidate_id":"cand_aeba23498e823c5c102a","commentary_obligation":"review","hft_ref":"hft_0ac0d3b203bda681416f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_familiar_facing_access","source_type":"hft","support_ids":["sup_56f18f1d10bff16cca6c"],"title":"baseline_familiar_facing_access","trust":"legacy_unbound"},{"anchor_refs":["114:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"114:5","branch_refs":["root_000059/B002","root_000849/B001","root_001651/B002"],"candidate_id":"cand_7451b057185aa50c0afa","commentary_obligation":"review","hft_ref":"hft_284f170651423b0ba445","kind":"surprising_outlier","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:outlier_somatic_rustle","source_type":"hft","support_ids":["sup_1b7f8f0ac53eb4f64837"],"title":"outlier_somatic_rustle","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ","qac_morphemes":[{"lemma_ar":"ٱلَّذِى","morph_features":"STEM|POS:REL|LEM:{l~a*iY|MS","morpheme_role":"STEM","pos":"REL","qac_ref":"114:5:1:1","qac_word_ref":"114:5:1","root_ar":"","surface_ar":"ٱلَّذِى"},{"lemma_ar":"وَسْوَسَ","morph_features":"STEM|POS:V|IMPF|LEM:wasowasa|ROOT:wsws|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"114:5:2:1","qac_word_ref":"114:5:2","root_ar":"و س و س","surface_ar":"يُوَسْوِسُ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"114:5:3:1","qac_word_ref":"114:5:3","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:5:4:1","qac_word_ref":"114:5:4","root_ar":"ص د ر","surface_ar":"صُدُورِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"114:5:5:1","qac_word_ref":"114:5:5","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:5:5:2","qac_word_ref":"114:5:5","root_ar":"ن و س","surface_ar":"نَّاسِ"}],"word_analysis_qac_refs":[["114:5:1:1"],["114:5:2:1"],["114:5:3:1"],["114:5:4:1"],["114:5:5:1","114:5:5:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["114:5:1","114:5:2","114:5:3","114:5:4","114:5:5"]},"focus_surface_evidence":{"arabic_uthmani":"ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ","qac_morphemes":[{"lemma_ar":"ٱلَّذِى","morph_features":"STEM|POS:REL|LEM:{l~a*iY|MS","morpheme_role":"STEM","pos":"REL","qac_ref":"114:5:1:1","qac_word_ref":"114:5:1","root_ar":"","surface_ar":"ٱلَّذِى"},{"lemma_ar":"وَسْوَسَ","morph_features":"STEM|POS:V|IMPF|LEM:wasowasa|ROOT:wsws|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"114:5:2:1","qac_word_ref":"114:5:2","root_ar":"و س و س","surface_ar":"يُوَسْوِسُ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"114:5:3:1","qac_word_ref":"114:5:3","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:5:4:1","qac_word_ref":"114:5:4","root_ar":"ص د ر","surface_ar":"صُدُورِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"114:5:5:1","qac_word_ref":"114:5:5","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:5:5:2","qac_word_ref":"114:5:5","root_ar":"ن و س","surface_ar":"نَّاسِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["114:5:1:1"],["114:5:2:1"],["114:5:3:1"],["114:5:4:1"],["114:5:5:1","114:5:5:2"]],"word_analysis_refs":["114:5:1","114:5:2","114:5:3","114:5:4","114:5:5"],"word_rows":[{"analysis_record_ref":"114:5:1","analytic_gloss_range_en":"masculine singular relative pronoun that carries the prior named whisperer into a defining verbal clause","analytic_root_gloss_range_en":null,"qac_refs":["114:5:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"ٱلَّذِى","transliteration":"alladhī"}},{"analysis_record_ref":"114:5:2","analytic_gloss_range_en":"ongoing hidden whispering or insinuating, here without an explicit object and routed into the chest-locus","analytic_root_gloss_range_en":"hidden inward whisper, faint rustle or murmur, and nominal whisperer language; the local imperfect verb selects inward insinuating action while retaining sound-like repetition","qac_refs":["114:5:2:1"],"root":{"arabic":"و س و س","transliteration":"w-s-w-s"},"surface":{"arabic":"يُوَسْوِسُ","transliteration":"yūwaswisu"}},{"analysis_record_ref":"114:5:3","analytic_gloss_range_en":"locative-penetrative preposition marking the internal space where the whispering operates","analytic_root_gloss_range_en":null,"qac_refs":["114:5:3:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"فِى","transliteration":"fī"}},{"analysis_record_ref":"114:5:4","analytic_gloss_range_en":"plural chests as embodied inner loci of hidden thought and response, governed by the locative preposition and bound to mankind in construct","analytic_root_gloss_range_en":"chest or bodily front, foremost part, issuing/source imagery, departure-after-water, and other branches; the local plural selects the chest/interior branch while source and issuing pressure survives only as image-pressure","qac_refs":["114:5:4:1"],"root":{"arabic":"ص د ر","transliteration":"ṣ-d-r"},"surface":{"arabic":"صُدُورِ","transliteration":"ṣudūri"}},{"analysis_record_ref":"114:5:5","analytic_gloss_range_en":"the definite collective human class as possessor of the targeted chests, affected through possession rather than direct object case","analytic_root_gloss_range_en":"people, mankind, social familiarity and perception; the local definite collective selects humanity as a class, with disputed sociability or forgetfulness pressure kept cautious because V4 has no guardrail rows for this root","qac_refs":["114:5:5:1","114:5:5:2"],"root":{"arabic":"أ ن س","transliteration":"ʾ-n-s"},"surface":{"arabic":"ٱلنَّاسِ","transliteration":"al-nās"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["114:5"],"branch_refs":["root_000059/B006","root_000849/B001","root_001651/B001"],"candidate_id":"cand_b95e4d1f7ff65b7fc9d2","evidence_scope":"focus_ayah","hft_ref":"hft_d7dea31a6b9364cd8a5e","item_id":"baseline_covert_self_speech","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_covert_self_speech","support_id":"sup_47182ebabb01fee7ab8a"},{"anchor_refs":["114:5"],"branch_refs":["root_000059/B002","root_000849/B002","root_000849/B004","root_001651/B001"],"candidate_id":"cand_9d8949e8b05a172f4f31","evidence_scope":"focus_ayah","hft_ref":"hft_60751efd955cf76fd525","item_id":"baseline_preaction_source","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_preaction_source","support_id":"sup_0c8db3cf8704202747d7"},{"anchor_refs":["114:5"],"branch_refs":["root_000059/B003","root_000059/B004","root_000849/B001","root_001651/B001"],"candidate_id":"cand_aeba23498e823c5c102a","evidence_scope":"focus_ayah","hft_ref":"hft_0ac0d3b203bda681416f","item_id":"baseline_familiar_facing_access","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_familiar_facing_access","support_id":"sup_56f18f1d10bff16cca6c"},{"anchor_refs":["114:5"],"branch_refs":["root_000059/B002","root_000849/B001","root_001651/B002"],"candidate_id":"cand_7451b057185aa50c0afa","evidence_scope":"focus_ayah","hft_ref":"hft_284f170651423b0ba445","item_id":"outlier_somatic_rustle","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_somatic_rustle","support_id":"sup_1b7f8f0ac53eb4f64837"}],"diagnostics":[],"lane_counts":{"global":10,"macro":12,"micro":4},"packet_summary":{"ayah_count":6,"focus_ref":"114:5","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ش ر ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000787","furuq_root_norm":"ش ر ر","furuq_source_root_norm":"ش ر ر","is_dominant":true,"target_occurrences":19,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000792","furuq_root_norm":"ش ر ي","furuq_source_root_norm":"ش ر ي","is_dominant":false,"target_occurrences":11,"target_rank":2}]}],"window":["114:1","114:2","114:3","114:4","114:5","114:6"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"114:5","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":16,"unstructured_record_count":0},"identity":{"ayah_ref":"114:5","lane":"micro","linguistic_source_ref":"114:5","surface_ref":"114:5","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"114:5","target_tokens":[["O",["114:5:1"]],["insanların",["114:5:5"]],["göğüslerinde",["114:5:3","114:5:4"]],["vesvese",["114:5:2"]],["verir",["114:5:2"]]],"text":"O, insanların göğüslerinde vesvese verir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":6,"id":"s114-p01-001-006","label":"Whole surah","number":1,"refs":["114:1","114:2","114:3","114:4","114:5","114:6"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:4:governed-construct-hinge","source_type":"word_analysis","support_id":"sup_02ada5b83e80f460dfab","text":"{\"blocking_evidence\":null,\"headline\":\"the chest noun links the preposition to the human possessor\",\"reader_payoff\":\"The reader sees {{ar:صُدُورِ}} ({{tr:ṣudūri}}) as the grammatical bridge from interior location to mankind, not as an isolated body noun.\",\"reason\":\"Attachment evidence marks {{ar:صُدُورِ}} ({{tr:ṣudūri}}) as governed by {{ar:فِى}} ({{tr:fī}}) and as the construct head completed by {{ar:ٱلنَّاسِ}} ({{tr:al-nās}}).\",\"representative_source_ids\":[\"QG-865b51d1\",\"QT-1f0106f0\",\"QY-e0a36a7c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:5:construct-definiteness-and-distribution","source_type":"word_analysis","support_id":"sup_06d167eb95f84edf5553","text":"{\"blocking_evidence\":null,\"headline\":\"final definiteness reaches back through plural chests\",\"reader_payoff\":\"The reader notices the phrase joining one collective human class to many embodied chest-loci.\",\"reason\":\"The construct relation lets the definiteness of {{ar:ٱلنَّاسِ}} ({{tr:al-nās}}) determine the phrase while the plural {{ar:صُدُورِ}} ({{tr:ṣudūri}}) distributes the locus.\",\"representative_source_ids\":[\"QG-7c7a7fd3\",\"QF-5d9c292c\",\"QT-f248cc4f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"114:5:4:1","source_type":"qac_morpheme","support_id":"sup_06fb61cb6008fffb199f","text":"{\"lemma_ar\":\"صَدْر\",\"morph_features\":\"STEM|POS:N|LEM:Sador|ROOT:Sdr|MP|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"114:5:4:1\",\"qac_word_ref\":\"114:5:4\",\"root_ar\":\"ص د ر\",\"surface_ar\":\"صُدُورِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"114:5:2:1","source_type":"qac_morpheme","support_id":"sup_103664d1098af7b6d9e9","text":"{\"lemma_ar\":\"وَسْوَسَ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:wasowasa|ROOT:wsws|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"114:5:2:1\",\"qac_word_ref\":\"114:5:2\",\"root_ar\":\"و س و س\",\"surface_ar\":\"يُوَسْوِسُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:2:objectless-locative-frame","source_type":"word_analysis","support_id":"sup_123884bc4d822db7492e","text":"{\"blocking_evidence\":null,\"headline\":\"the verb leaves content unspoken and routes the action to an interior locus\",\"reader_payoff\":\"The reader notices that the ayah answers where whispering operates, not what sentence is whispered.\",\"reason\":\"The local verb instance is marked without an object and with {{ar:فِى}} ({{tr:fī}}) plus {{ar:صُدُورِ}} ({{tr:ṣudūri}}) as its governed locative complement.\",\"representative_source_ids\":[\"QG-093133fc\",\"QG-a85d357e\",\"MP-51622d70\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:5:perception-sociability-forgetfulness-pressure","source_type":"word_analysis","support_id":"sup_23b711296c8387e39b9e","text":"{\"blocking_evidence\":null,\"headline\":\"human perception and familiarity pressure the target class\",\"reader_payoff\":\"The reader feels mankind as socially aware and inwardly receptive, while the local noun remains the collective human class rather than an etymological argument.\",\"reason\":\"The bundle has no V4 rows for {{ar:أ ن س}} ({{tr:ʾ-n-s}}), so the proposed perception, sociability, and disputed forgetfulness pressures survive only as cautious background to the locally selected collective people sense.\",\"representative_source_ids\":[\"QS-200bb523\",\"QS-7faaf8f0\",\"QS-97517773\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:1:defining-relative-clause","source_type":"word_analysis","support_id":"sup_31a40a2e842f8e0e2d84","text":"{\"blocking_evidence\":null,\"headline\":\"the following clause defines the threat by action\",\"reader_payoff\":\"The reader sees the clause as a definition of the threat's characteristic act, not merely as extra description after a name.\",\"reason\":\"The local clause is relative-pronoun plus verbal predicate plus locative phrase, so {{ar:ٱلَّذِى}} ({{tr:alladhī}}) suspends the line until {{ar:يُوَسْوِسُ}} ({{tr:yūwaswisu}}) supplies the defining action.\",\"representative_source_ids\":[\"MG-611ac56f\",\"QT-e63402ac\",\"QT-f9651f5b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:2","source_type":"word_analysis","support_id":"sup_345812fec3f8c4815a38","text":"{\"gloss_range\":\"ongoing hidden whispering or insinuating, here without an explicit object and routed into the chest-locus\",\"prose\":\"{{ar:يُوَسْوِسُ}} ({{tr:yūwaswisu}}) turns the carried identity into action. The verb has a recoverable 3ms subject from {{ar:ٱلَّذِى}} ({{tr:alladhī}}), but no explicit object, so the clause leaves the whisper's content, recipient, and instrument unspecified while foregrounding the act itself and its place. Its imperfect aspect, reduplicated root body, and repeated sibilants make the insinuation feel recurring in time, structure, and sound. The chest-locative selects inward prompting, while the faint-rustle branch keeps the action sound-like; the adjacent reprise of {{ar:ٱلْوَسْوَاسِ}} ({{tr:al-waswās}}) in 114:4 makes the name act in 114:5. Within this tight whispering field, the contrast with 50:16 also matters: there the self is the whispering source, while here the prior external whisperer acts inside human chests.\",\"root_display\":\"{{ar:و س و س}} ({{tr:w-s-w-s}})\",\"root_gloss_range\":\"hidden inward whisper, faint rustle or murmur, and nominal whisperer language; the local imperfect verb selects inward insinuating action while retaining sound-like repetition\",\"surface_display\":\"{{ar:يُوَسْوِسُ}} ({{tr:yūwaswisu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:4","source_type":"word_analysis","support_id":"sup_390561d2f3317f3c6d02","text":"{\"gloss_range\":\"plural chests as embodied inner loci of hidden thought and response, governed by the locative preposition and bound to mankind in construct\",\"prose\":\"{{ar:صُدُورِ}} ({{tr:ṣudūri}}) is the noun where the clause lands. It is governed upward by {{ar:فِى}} ({{tr:fī}}) and governs downward to {{ar:ٱلنَّاسِ}} ({{tr:al-nās}}), making the chest noun the hinge between infiltration and human possession. The local sense is not a flat abstraction: the plural chest image stays embodied while Quranic usage and the whispering context make it the hidden locus of intentions, concealed states, and response. The broader {{ar:ص د ر}} ({{tr:ṣ-d-r}}) family also carries source and issuing pressure, but local grammar keeps that pressure as image, not as a replacement for the chest sense. The broken plural and construct distribute the threat across many human interiors, while 10:57 shows the same kind of chest-locus as a place of healing and 114:6 turns outward to source classes. The matching genitive -i cadence binds {{ar:صُدُورِ}} ({{tr:ṣudūri}}) to {{ar:ٱلنَّاسِ}} ({{tr:al-nās}}), and the heavier opening sound of the chest noun sets the target against the verb's thinner whispering texture.\",\"root_display\":\"{{ar:ص د ر}} ({{tr:ṣ-d-r}})\",\"root_gloss_range\":\"chest or bodily front, foremost part, issuing/source imagery, departure-after-water, and other branches; the local plural selects the chest/interior branch while source and issuing pressure survives only as image-pressure\",\"surface_display\":\"{{ar:صُدُورِ}} ({{tr:ṣudūri}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:2:compressed-subject-agency","source_type":"word_analysis","support_id":"sup_3aa1bc8e35dfd2e8ba86","text":"{\"blocking_evidence\":null,\"headline\":\"the subject is compressed into the verb and relative chain\",\"reader_payoff\":\"The reader tracks agency back to the prior singular whisperer without needing a repeated subject noun after the verb.\",\"reason\":\"The 3ms imperfect prefix and attachment evidence make the subject syntactically controlled by {{ar:ٱلَّذِى}} ({{tr:alladhī}}), preserving compression without losing agency.\",\"representative_source_ids\":[\"QG-31e8241e\",\"QF-a940f5bd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:4:embodied-hidden-interiority","source_type":"word_analysis","support_id":"sup_4393cf59614f61584d0d","text":"{\"blocking_evidence\":null,\"headline\":\"literal chest image becomes the hidden interior locus\",\"reader_payoff\":\"The reader notices that the ayah names an embodied chest-space while making that space the moral-cognitive interior where whispering operates.\",\"reason\":\"V4 supports the chest branch for {{ar:ص د ر}} ({{tr:ṣ-d-r}}), and contextual rows show this exact form recurring as a hidden-state locus; the local prepositional frame preserves spatial force.\",\"representative_source_ids\":[\"QS-2622c478\",\"QS-73c0d7f9\",\"QI-11be324a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:1:antecedent-bound-relative","source_type":"word_analysis","support_id":"sup_582a902878fcedf8e71f","text":"{\"blocking_evidence\":null,\"headline\":\"the relative pronoun carries the prior whisperer across the ayah boundary\",\"reader_payoff\":\"The reader notices that 114:5 depends on the named whisperer from 114:4, so the ayah begins by carrying a tracked threat forward rather than starting over.\",\"reason\":\"QAC and attachment evidence identify {{ar:ٱلَّذِى}} ({{tr:alladhī}}) as a masculine singular relative pronoun qualifying the immediately preceding whisperer expression from 114:4.\",\"representative_source_ids\":[\"QG-46f1094b\",\"QG-e0498268\",\"QB-290286a7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:5:definite-collective-scope","source_type":"word_analysis","support_id":"sup_5e8741278bca2d1bf0fe","text":"{\"blocking_evidence\":null,\"headline\":\"the definite collective closes the phrase at human class scale\",\"reader_payoff\":\"The reader sees the target as the definite human class, not a named subset or a single individual.\",\"reason\":\"QAC marks the noun as definite, genitive, and concrete, and contextual profiles identify the dominant referent as generic humans.\",\"representative_source_ids\":[\"QG-e564e42d\",\"QF-bc3f223a\",\"QF-df8357fb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:2:inward-soundlike-insinuation","source_type":"word_analysis","support_id":"sup_5ea068c85e9296a403b4","text":"{\"blocking_evidence\":null,\"headline\":\"audible whisper imagery is transferred into the chest\",\"reader_payoff\":\"The reader feels the inner suggestion as a low repeated disturbance, while the chest-locus keeps it from being merely ordinary audible speech.\",\"reason\":\"The hidden inward whisper branch is selected by {{ar:فِى صُدُورِ}} ({{tr:fī ṣudūri}}), while the faint murmur branch survives as sound-image pressure rather than as a separate physical noise event.\",\"representative_source_ids\":[\"QS-2ba7c4c6\",\"QS-9bc6fe91\",\"QS-9cf74f1e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"114:5:5:2","source_type":"qac_morpheme","support_id":"sup_633cb373df8803f9e9db","text":"{\"lemma_ar\":\"نَّاس\",\"morph_features\":\"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"114:5:5:2\",\"qac_word_ref\":\"114:5:5\",\"root_ar\":\"ن و س\",\"surface_ar\":\"نَّاسِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:2:name-into-action-reprise","source_type":"word_analysis","support_id":"sup_7d8f57b5e4bec179a4f0","text":"{\"blocking_evidence\":null,\"headline\":\"the prior whisperer noun becomes a verb\",\"reader_payoff\":\"The reader sees the root move from a title in 114:4 to an enacted process in 114:5.\",\"reason\":\"{{ar:ٱلْوَسْوَاسِ}} ({{tr:al-waswās}}) in 114:4 and {{ar:يُوَسْوِسُ}} ({{tr:yūwaswisu}}) in 114:5 share the same root field while shifting from nominal identity to imperfect verbal action.\",\"representative_source_ids\":[\"QS-a64b71e6\",\"QE-156d5404\",\"QB-b21cb809\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:4:source-issuing-pressure","source_type":"word_analysis","support_id":"sup_88387cfb92fe8d10763e","text":"{\"blocking_evidence\":null,\"headline\":\"source and issuing imagery pressures the chest without replacing it\",\"reader_payoff\":\"The reader feels the chest as a generative interior from which intentions and responses can issue, while the local noun still means chests.\",\"reason\":\"V4 separates chest/front and source/issuing branches, so the local plural governed by {{ar:فِى}} ({{tr:fī}}) selects the chest-interior branch while source imagery remains a limited lexical pressure.\",\"representative_source_ids\":[\"QS-2525e9be\",\"QS-830574b1\",\"QS-bb6c0c5b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:5:human-interiority-and-whisper-field","source_type":"word_analysis","support_id":"sup_981d6721aa203207970f","text":"{\"blocking_evidence\":null,\"headline\":\"the final noun joins humanity to chest and whisper fields\",\"reader_payoff\":\"The reader notices that humanity is not generic background here; it is the possessor of targeted interiors and part of the whispering field that also appears in 50:16.\",\"reason\":\"The contextual profiles show {{ar:أ ن س}} ({{tr:ʾ-n-s}}) as the partner root with {{ar:ص د ر}} ({{tr:ṣ-d-r}}), and CRITICAL evidence names 50:16 as the concrete whispering parallel.\",\"representative_source_ids\":[\"QI-c44d725d\",\"QI-d15f3fbd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:3:locative-penetrative-containment","source_type":"word_analysis","support_id":"sup_99153a56e919fe465884","text":"{\"blocking_evidence\":null,\"headline\":\"the preposition places the whispering inside the chest-space\",\"reader_payoff\":\"The reader notices the threat as already operating within the interior locus, not merely approaching or addressing people from outside.\",\"reason\":\"QAC marks {{ar:فِى}} ({{tr:fī}}) as a locative-penetrative preposition, and attachment evidence makes it govern {{ar:صُدُورِ}} ({{tr:ṣudūri}}) as the complement of {{ar:يُوَسْوِسُ}} ({{tr:yūwaswisu}}).\",\"representative_source_ids\":[\"QG-531a57a9\",\"MG-c1427ce7\",\"QS-22d9255e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:4:plural-possessed-distribution","source_type":"word_analysis","support_id":"sup_991edac97339931e77c8","text":"{\"blocking_evidence\":null,\"headline\":\"the broken plural construct distributes many human interiors\",\"reader_payoff\":\"The reader sees a distributed field of many embodied interiors rather than one abstract human chest.\",\"reason\":\"QAC identifies {{ar:صُدُورِ}} ({{tr:ṣudūri}}) as a broken plural in construct with {{ar:ٱلنَّاسِ}} ({{tr:al-nās}}), which distributes the locative target across human possessors.\",\"representative_source_ids\":[\"QF-1f6d4992\",\"QF-52298829\",\"QF-5574472f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:3:action-to-locus-architecture","source_type":"word_analysis","support_id":"sup_997ea39cd3132804ab00","text":"{\"blocking_evidence\":null,\"headline\":\"the preposition pivots the clause from act to landing-site\",\"reader_payoff\":\"The reader follows the clause's movement from naming the whispering act to mapping where it lands.\",\"reason\":\"The local clause would leave the content unspecified after {{ar:يُوَسْوِسُ}} ({{tr:yūwaswisu}}); {{ar:فِى}} ({{tr:fī}}) supplies the relation that makes the following chest phrase the meaningful frame.\",\"representative_source_ids\":[\"QT-17edd538\",\"QT-f927f0d9\",\"QB-963b91ec\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:5","source_type":"word_analysis","support_id":"sup_a3d310ad54907598a835","text":"{\"gloss_range\":\"the definite collective human class as possessor of the targeted chests, affected through possession rather than direct object case\",\"prose\":\"{{ar:ٱلنَّاسِ}} ({{tr:al-nās}}) closes the ayah by naming whose interiors are exposed. Grammatically it is a genitive possessor after {{ar:صُدُورِ}} ({{tr:ṣudūri}}), but semantically it is the affected human class because the whispering operates in their chests. Its definiteness reaches back through the construct phrase, making the target the human domain rather than an indefinite group. The collective noun keeps mankind at class scale while the plural chest noun distributes vulnerability across many interiors. The same word has already marked the refuge titles in 114:1-3, appears here as the vulnerable target, and returns in 114:6 as a possible source class; that repetition makes humanity the surah's lexical spine. Its pairing with the chest noun makes humanity the possessor of targeted interiors, and the whispering-field parallel in 50:16 keeps the human class tied to inner prompting rather than generic background. The root-pressure around perception, sociability, and the contested forgetfulness derivation is useful but narrowed: the local word means the human class, while that background sharpens how familiar perception can admit intrusive suggestion and how forgetfulness can be exploited. At the sound level, article assimilation fuses definiteness into the doubled nūn of the closing noun, giving the repeated surah keyword audible weight at the ayah's landing point.\",\"root_display\":\"{{ar:أ ن س}} ({{tr:ʾ-n-s}})\",\"root_gloss_range\":\"people, mankind, social familiarity and perception; the local definite collective selects humanity as a class, with disputed sociability or forgetfulness pressure kept cautious because V4 has no guardrail rows for this root\",\"surface_display\":\"{{ar:ٱلنَّاسِ}} ({{tr:al-nās}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:3","source_type":"word_analysis","support_id":"sup_a9bcf038ce1913d1acb6","text":"{\"gloss_range\":\"locative-penetrative preposition marking the internal space where the whispering operates\",\"prose\":\"{{ar:فِى}} ({{tr:fī}}) is the hinge that turns whispering into an interior event. It governs {{ar:صُدُورِ ٱلنَّاسِ}} ({{tr:ṣudūri l-nās}}), selecting containment rather than a recipient frame such as the contrasts in 7:20 and 20:120; the threat is already inside the chest-space, not merely at or near it. Because it stands as a full unsuffixed preposition, the ayah gives the locative relation its own beat and then names the full chest phrase instead of resolving it by pronoun. Across the boundary, refuge from a source in 114:4 becomes danger located inside a human interior in 114:5.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فِى}} ({{tr:fī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:2:reduplicated-imperfect-sound","source_type":"word_analysis","support_id":"sup_b8e4630c0db56d3fe408","text":"{\"blocking_evidence\":null,\"headline\":\"form, aspect, and sound all repeat the whispering\",\"reader_payoff\":\"The reader hears and sees persistence: the root repeats internally, the imperfect keeps the act ongoing, and the sibilants make the surface whisper-like.\",\"reason\":\"QAC identifies the form as an imperfect reduplicated quadriliteral verb, and V4 allows both hidden inward whisper and faint murmur branches without requiring a causative reading.\",\"representative_source_ids\":[\"QG-d1486bde\",\"QF-536583e4\",\"QY-c35527b2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:4:chest-echoes-and-role-boundary","source_type":"word_analysis","support_id":"sup_bd257e1af2d83da09a8f","text":"{\"blocking_evidence\":null,\"headline\":\"the same interior locus is vulnerable here and repairable elsewhere\",\"reader_payoff\":\"The reader notices that the chest-locus exposed to whispering in 114:5 is also the kind of locus that receives healing in 10:57, while 114:6 shifts attention to source classes.\",\"reason\":\"The CRITICAL rows give concrete same-locus contrasts with 10:57 and the immediate next-ayah role shift in 114:6, and local grammar confirms the chest phrase as the location of whispering.\",\"representative_source_ids\":[\"QI-66ec0ebc\",\"QE-7b1604ce\",\"MI-8f5dad55\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:5:genitive-affected-possessor","source_type":"word_analysis","support_id":"sup_be02a7f4c4bc34ba255c","text":"{\"blocking_evidence\":null,\"headline\":\"mankind is possessed genitive yet semantically affected\",\"reader_payoff\":\"The reader notices that mankind is affected through the chest-locus even though {{ar:ٱلنَّاسِ}} ({{tr:al-nās}}) is not the direct object of the verb.\",\"reason\":\"Attachment evidence makes {{ar:ٱلنَّاسِ}} ({{tr:al-nās}}) the genitive complement of {{ar:صُدُورِ}} ({{tr:ṣudūri}}), while the larger locative frame identifies human interiors as the affected site.\",\"representative_source_ids\":[\"QG-1a1a9ce5\",\"QG-99b538de\",\"QS-c3c7dc77\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:4:sound-and-cadence-binding","source_type":"word_analysis","support_id":"sup_c4a80ab568c71e8e0cf7","text":"{\"blocking_evidence\":null,\"headline\":\"cadence and consonant weight bind the chest to the phrase\",\"reader_payoff\":\"The reader hears the chest noun as both bound to {{ar:ٱلنَّاسِ}} ({{tr:al-nās}}) by genitive cadence and set against the thin whispering texture by its heavier opening sound.\",\"reason\":\"The genitive ending links {{ar:صُدُورِ}} ({{tr:ṣudūri}}) with {{ar:ٱلنَّاسِ}} ({{tr:al-nās}}), while the phonetic observation remains a surface payoff rather than a semantic branch claim.\",\"representative_source_ids\":[\"QP-7a48f705\",\"QP-a32d0925\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:2:rare-field-role-contrast","source_type":"word_analysis","support_id":"sup_d152790a1000d2581167","text":"{\"blocking_evidence\":null,\"headline\":\"the rare whispering field contrasts external and internal sources\",\"reader_payoff\":\"The reader notices that 114:5 belongs to a tight whispering field where 50:16 shows self-whispering and 114:5 shows an external whisperer acting inside the human locus.\",\"reason\":\"The contextual profiles mark {{ar:و س و س}} ({{tr:w-s-w-s}}) as low-occurrence and Satan-linked, while the CRITICAL contrast with 50:16 gives a concrete role comparison.\",\"representative_source_ids\":[\"QI-29bb1a12\",\"QH-f3af0ebe\",\"QI-894631ef\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:5:surah-refrain-role-shift","source_type":"word_analysis","support_id":"sup_de29e39048d8df4b2219","text":"{\"blocking_evidence\":null,\"headline\":\"the repeated human noun shifts from protected class to target and source\",\"reader_payoff\":\"The reader tracks {{ar:ٱلنَّاسِ}} ({{tr:al-nās}}) as the surah's repeated human noun: protected in 114:1-3, targeted in 114:5, and named among source classes in 114:6.\",\"reason\":\"The attachment cross-reference flags the repeated {{ar:ٱلنَّاسِ}} ({{tr:al-nās}}) refrain anchored at 114:1, and the CRITICAL rows give the concrete role sequence through 114:1-3, 114:5, and 114:6.\",\"representative_source_ids\":[\"QI-46879a30\",\"QE-9d23eaf6\",\"QY-d7fc931f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:5:article-assimilation-closing-sound","source_type":"word_analysis","support_id":"sup_e2a458626dc7d8ce6168","text":"{\"blocking_evidence\":null,\"headline\":\"article assimilation makes the final class noun audibly fused\",\"reader_payoff\":\"The reader hears definiteness and class identity fused in the closing noun rather than treating the article as a detachable detail.\",\"reason\":\"The recitational assimilation of the article before the sun-letter is a surface-level payoff that supports the definite closing force without creating a new lexical sense.\",\"representative_source_ids\":[\"QF-28d709b5\",\"QP-f50d6b42\",\"QP-fe3e0b12\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:3:full-named-locus-slot","source_type":"word_analysis","support_id":"sup_ee5cd60b3a2699feb23d","text":"{\"blocking_evidence\":null,\"headline\":\"the standalone preposition opens a full named locus\",\"reader_payoff\":\"The reader feels a separate prepositional beat before the chest phrase is named in full.\",\"reason\":\"{{ar:فِى}} ({{tr:fī}}) is a separate unsuffixed word, so the following phrase must supply the explicit interior locus.\",\"representative_source_ids\":[\"QF-1bc61dbd\",\"QF-44f30e44\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:5:1","source_type":"word_analysis","support_id":"sup_ff43a5a1cc6f01a52e4a","text":"{\"gloss_range\":\"masculine singular relative pronoun that carries the prior named whisperer into a defining verbal clause\",\"prose\":\"{{ar:ٱلَّذِى}} ({{tr:alladhī}}) opens the ayah as a dependent continuation, not as a new independent subject. Its masculine singular reference carries {{ar:ٱلْوَسْوَاسِ ٱلْخَنَّاسِ}} ({{tr:al-waswāsi al-khannās}}) forward from 114:4, so the prior threat is tracked as one identified referent before the next ayah broadens the source classes. The relative form also makes the following verb definitional: the whisperer is known by the specific act of whispering into chests, not by an added description loosely attached after the name.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:ٱلَّذِى}} ({{tr:alladhī}})\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ","ayah_ref":"114:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000059/B006","root_000849/B001","root_001651/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001651","role":"Hidden inward self-talk supplies the covert signal and lets an introduced thought resemble the recipient's own speech.","root":"و س و س","source_ref":"114:5","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000849","role":"The anatomical chest supplies a bodily chamber in which the covert signal is localized.","root":"ص د ر","source_ref":"114:5","source_word_indices":["4"]},{"branch_id":"B006","mapped_root_id":"root_000059","role":"The self or intimate companion image explains why the inward voice can pass as one's own or as trusted speech.","root":"ن و س","source_ref":"114:5","source_word_indices":["5"]}],"changed_reading":{"after":"An iterative covert signal is staged inside the human interior so that alien prompting can be misrecognized as self-speech or an intimate voice.","before":"A hostile speaker quietly tells people bad things."},"confidence":"strong","focus_anchor":"The iterative verb at 114:5 word 2 acts inside the plural chests at word 4 and upon the people at word 5.","mechanism":"Repeated hidden inward speech is placed in a bodily interior where its external source is no longer audible; because the human branch can denote one's own self or an intimate companion, the intrusion can be experienced as self-authored or familiarly voiced.","model_id":"baseline_covert_self_speech"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_covert_self_speech","source_type":"hft","support_id":"sup_47182ebabb01fee7ab8a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ","ayah_ref":"114:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000059/B002","root_000849/B002","root_000849/B004","root_001651/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001651","role":"Hidden inward speech provides a low-visibility input before a public word or act exists.","root":"و س و س","source_ref":"114:5","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000849","role":"The foremost or first part makes the chest a threshold at the front of an emerging response.","root":"ص د ر","source_ref":"114:5","source_word_indices":["4"]},{"branch_id":"B004","mapped_root_id":"root_000849","role":"The source from which actions issue turns that threshold into a production point for later conduct.","root":"ص د ر","source_ref":"114:5","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000059","role":"Perception into awareness supplies the transition by which a covert input becomes noticed, felt, or actionable.","root":"ن و س","source_ref":"114:5","source_word_indices":["5"]}],"changed_reading":{"after":"Whispering intervenes at the pre-action source, biasing what becomes salient and what can issue as thought, speech, or conduct.","before":"Whispering adds a proposition to an already formed mind."},"confidence":"strong","focus_anchor":"The preposition fi places the whispering in sudur, whose branches include both the foremost part and the source from which actions issue.","mechanism":"The whisper operates upstream of visible conduct: it perturbs what first reaches awareness at the action-generating source, so its effect may appear later as an apparently spontaneous judgment, intention, or act.","model_id":"baseline_preaction_source"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_preaction_source","source_type":"hft","support_id":"sup_0c8db3cf8704202747d7","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ","ayah_ref":"114:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000059/B003","root_000059/B004","root_000849/B001","root_001651/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001651","role":"Hidden inward speech supplies content whose provenance is difficult to inspect.","root":"و س و س","source_ref":"114:5","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000059","role":"Familiar comfort that removes estrangement supplies the trusted tone through which the signal can be admitted.","root":"ن و س","source_ref":"114:5","source_word_indices":["5"]},{"branch_id":"B004","mapped_root_id":"root_000059","role":"The near human-facing side supplies an exposed relational surface rather than an obviously alien point of attack.","root":"ن و س","source_ref":"114:5","source_word_indices":["5"]},{"branch_id":"B001","mapped_root_id":"root_000849","role":"The bodily front localizes that human-facing access at the person's presented yet inwardly vulnerable side.","root":"ص د ر","source_ref":"114:5","source_word_indices":["4"]}],"changed_reading":{"after":"The whisper succeeds through both quietness and familiarity, entering from the side that feels near, human, and already trusted.","before":"The whisper succeeds because it is quiet."},"confidence":"medium","focus_anchor":"The target noun at 114:5 word 5 carries branches of familiarity and the near human-facing side, while the action remains hidden inward speech.","mechanism":"The signal gains access through the side already turned toward relationship and comfort. Its efficacy is not only secrecy but resemblance to what is socially near, tame, and reassuring.","model_id":"baseline_familiar_facing_access"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_familiar_facing_access","source_type":"hft","support_id":"sup_56f18f1d10bff16cca6c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ","ayah_ref":"114:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000059/B002","root_000849/B001","root_001651/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001651","role":"A faint physical rustle or murmur supplies an almost subliminal sensory signal.","root":"و س و س","source_ref":"114:5","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000849","role":"The anatomical chest supplies the bodily resonant site where that faint signal may be felt.","root":"ص د ر","source_ref":"114:5","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000059","role":"Perceiving by sensing or hearing supplies the threshold at which bodily murmur enters awareness.","root":"ن و س","source_ref":"114:5","source_word_indices":["5"]}],"changed_reading":{"after":"The intrusion may first register as a faint bodily or acoustic disturbance that is only later interpreted into thought.","before":"The intrusion arrives as semantically formed inner language."},"confidence":"exploratory","containment":"This is surprising because it takes the physical murmur branch seriously beside the anatomical chest rather than immediately psychologizing both. It remains anchored in the focus verb and chest noun, but downstream prose should present it as a somatic or acoustic analogy, not as a claim that the verse reduces whispering to bodily noise.","focus_anchor":"The whisper verb at 114:5 word 2 and the anatomical chest at word 4 can jointly support a barely sensed bodily-rustle model.","outlier_id":"outlier_somatic_rustle"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:outlier_somatic_rustle","source_type":"hft","support_id":"sup_1b7f8f0ac53eb4f64837","trust":"legacy_unbound"}]}
</lane_packet_json>
