# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **89:29**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s089-regular-20260912/s089/89_29/micro.discovery.json` and modify nothing
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
  "ayah_ref": "89:29",
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
{"branch_registry":[{"boundary":"Bu dal içeriye geçişi temel alır; gizli iç yüz, içten bozukluk ve kalıplaşmış eşlik kullanımları ayrı dallarda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000464/B001","candidate_links":[{"candidate_id":"cand_8bb69e263144bebd1b35","lane":"micro"},{"candidate_id":"cand_f9427fd9b198285eba55","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:29:1:2","qac_word_ref":"89:29:1","surface_ar":"ٱدْخُلِ"}],"gloss":"içeri girmek veya içeri sokmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi ya da şey dışarıdaki bir konum veya durumdan içerideki konum veya duruma geçer."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ettirgen kullanım, başka bir kişi ya da şeyin içeriye geçmesini sağlamayı bildirir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Geçiş yer, zaman veya iş alanında gerçekleşebilir ve kimi kullanımda azar azar ilerleyen bir süreç olarak sunulur."}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer, zaman ya da bir işe katılma alanında dışarıdan içeriye geçişi ve bunun ettirgen karşılığını birlikte anlatmak için uygundur.","boundary_detail":"Bu dal içeriye geçişi temel alır; gizli iç yüz, içten bozukluk ve kalıplaşmış eşlik kullanımları ayrı dallarda kalır.","branch_image_ar":"الولوج إلى داخل","concept_gloss":"içeri girmek veya içeri sokmak","contextual_glosses":[{"applicability":"Bir yere veya sınırları belirli başka bir alana dışarıdan geçiş anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ettirgen içeri sokma ve zaman ya da iş alanına girme uzantılarını tek başına göstermez.","preserves":"Dışarıdan içeriye yönelen temel geçişi korur."},"facet_ids":["F001"],"text":"içeri girmek","usage_role":"general"},{"applicability":"Geçiş fiziksel bir yere değil zamansal bir evreye ya da yürütülen bir işe yöneldiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Fiziksel yer değişimini ve ettirgen kullanımı dışarıda bırakır.","preserves":"İçeri geçiş düzeninin soyut alanlara uygulanmasını korur."},"facet_ids":["F001","F003"],"text":"bir döneme veya işe girmek","usage_role":"contextual"},{"applicability":"Özne başka bir kişi ya da şeyin içeriye geçmesini sağladığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öznenin kendisinin içeri girdiği yalın kullanımı kapsamaz.","preserves":"Geçişin ettirgen ve yönlü oluşunu korur."},"facet_ids":["F002"],"text":"içeri sokmak","usage_role":"contextual"}],"definition":"Bir kişi ya da şey bir yerin, zamanın veya işin dışından içine geçer. Aynı çekirdek, bir başkasını içeri sokma ve bir şeyin içine aşamalı biçimde ilerleme yönleriyle genişler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi ya da şey dışarıdaki bir konum veya durumdan içerideki konum veya duruma geçer."},{"facet_id":"F002","role":"extension","statement":"Ettirgen kullanım, başka bir kişi ya da şeyin içeriye geçmesini sağlamayı bildirir."},{"facet_id":"F003","role":"specialization","statement":"Geçiş yer, zaman veya iş alanında gerçekleşebilir ve kimi kullanımda azar azar ilerleyen bir süreç olarak sunulur."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"İçeri geçiş bulunmayan her türlü grup üyeliğini ve ortak faaliyeti kapsar.","collision":"Sıradan birlikte hareket etme anlamıyla karışır.","fit":"broadening","loses":"Dışarıdan içeriye yönelen fiziksel geçişi ve ettirgen kullanımı siler.","preserves":"Bir işe dahil olma bağlamındaki soyut geçişi kısmen korur."},"text":"katılmak"}],"identity_rationale":"Kaynak ifadesi, temel anlamı dışarıdan içeriye geçiş olarak kuruyor; yerin yanı sıra zaman ve işe girmeyi, ayrıca bir şeyi içeri sokmayı ve aşamalı biçimde içine ilerlemeyi de bu çekirdeğe bağlıyor.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir yere, zamana veya işe girmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"içeri girme veya giriş"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"başkasını ya da bir şeyi içeri sokmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir şeyin içine azar azar girmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"girme eylemi veya giriş yeri"}],"lexicalization_note":"Tanım yalın içeri girme çekirdeğini, bir başkasını içeri sokan ettirgen kullanımdan ve özel türemiş kullanımlardan açıkça ayırır.","neighbor_coverage_note":"On yedi adayın tamamı karşılaştırıldı; çekirdeğe en yakın iki giriş dalı ile yön karşıtını gösteren dal seçildi, yalnızca aynı sahneyi paylaşan veya ayrı kardeş anlamları temsil eden adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekleri çok yakındır, ancak odak dalın kullanım alanı yer, zaman ve iş boyunca düzenlenirken komşu dal bazı özel geçit ve zaman eklenmesi örnekleriyle farklılaşır.","focus_only":"Odak dal zaman ve işe girmeyi, giriş yerini ve aşamalı ilerlemeyi de açıkça kapsar.","gloss":"içine geçme","neighbor_only":"Komşu dal dar geçitleri ve gecenin gündüze ya da gündüzün geceye eklenmesi gibi özel görünümleri öne çıkarır.","neighbor_ref":"root_001682/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin başka bir şeyin içine yönlü biçimde geçmesini temel alır."},{"boundary_match":"opposed","distinction":"Paylaşılan eksen geçiş yönüdür; odak dal içeriye, komşu dal dışarıya yönelir.","focus_only":"Odak dal sınırın dışından içine doğru geçişi bildirir.","gloss":"girme ve çıkma","neighbor_only":"Komşu dal içerideki yerden dışarı çıkmayı veya bir durumdan ayrılmayı bildirir.","neighbor_ref":"root_000400/B001","relation_type":"antonym","shared_zone":"İki dal da bir sınırın iki yanı arasında yönlü geçişi anlatır."},{"boundary_match":"partial","distinction":"Komşu dal yer ve giriş koşulu bakımından daha dardır; odak dal ise farklı alanlara taşınabilen genel geçiş çekirdeğidir.","focus_only":"Odak dal yer dışında zaman ve işe girmeyi, ayrıca ettirgen kullanımı kapsar.","gloss":"bir yere girme","neighbor_only":"Komşu dal özellikle bir eve, topluluğun yanına veya saklanma yerine girmeyi ve kimi zaman izinsizliği öne çıkarır.","neighbor_ref":"root_000487/B001","relation_type":"near_synonym","shared_zone":"Her ikisi de fiziksel bir yerin içine geçiş bağlamında kullanılabilir."}],"source_phrase_ar":"أصل مطرد منقاس وهو الولوج (maqayis)؛ دخل يدخل دخولا (maqayis)؛ ادخل في غار وتدخل فيه (ayn)؛ دخلت الدار وغيرها وأدخلت غيري (jamhara)؛ دخلت البيت وادخل وتدخل الشيء (sihah)؛ الدخول نقيض الخروج ويستعمل في المكان والزمان والأعمال (mufradat)","source_summary":"Ortak anlatım, dışarıdan içeriye yönelen geçişi esas alır; yer, zaman ve iş alanlarını, ettirgen içeri sokmayı ve aşamalı ilerlemeyi bu esasın düzenli görünümleri sayar.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الدخول في مكان أو زمان أو عمل، والإدخال والتدخل والمدخل من جهة الولوج أو الإيلاج.","what_is_not_ar":"لا يدخل فيه اسم الموضع دخول إذا أريد علما، ولا الكناية الزوجية الخاصة."},"support_links":["sup_25fc6d9bc5a8de9d221a","sup_abc1d398ce5770bb7c7a"]},{"boundary":"Anlam yalnızca eşli kalıpta geçerlidir; sıradan bir yere girme veya genel evlenme anlamına genişletilemez.","branch_kind":"collocation","branch_ref":"root_000464/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:29:1:2","qac_word_ref":"89:29:1","surface_ar":"ٱدْخُلِ"}],"gloss":"eşiyle cinsel birleşmede bulunmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Erkeğin eşiyle cinsel birleşmesi örtülü bir sözle anlatılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu anlam yalnızca eşin söz diziminde açıkça yer aldığı kalıplaşmış kullanımda doğar."}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli kalıbın örtülü olarak anlattığı, erkeğin eşiyle cinsel birleşmesi bağlamında kullanılmalıdır.","boundary_detail":"Anlam yalnızca eşli kalıpta geçerlidir; sıradan bir yere girme veya genel evlenme anlamına genişletilemez.","branch_image_ar":"الإفضاء الزوجي","concept_gloss":"eşiyle cinsel birleşmede bulunmak","contextual_glosses":[{"applicability":"Cinsel birleşmenin hedef metinde de örtülü ve ölçülü biçimde anlatılması gerektiğinde doğal karşılıktır.","error_profile":{"adds":"Bağlam yetersizse cinsel olmayan beraberlik olarak da anlaşılabilir.","collision":"Gündelik olarak aynı yerde bulunma anlamıyla karışabilir.","fit":"broadening","loses":null,"preserves":"Eşler arasındaki yakın birlikteliği ve örtülü anlatımı korur."},"facet_ids":["F001","F002"],"text":"eşiyle birlikte olmak","usage_role":"contextual"}],"definition":"Belirli eşli söz kalıbı, erkeğin eşiyle cinsel birleşmesini doğrudan söylemeden anlatır. Anlam, bu kalıbın dışındaki genel girme kullanımlarına taşınmaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Erkeğin eşiyle cinsel birleşmesi örtülü bir sözle anlatılır."},{"facet_id":"F002","role":"specialization","statement":"Bu anlam yalnızca eşin söz diziminde açıkça yer aldığı kalıplaşmış kullanımda doğar."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Evlilik bağının kurulması gibi daha geniş ve farklı bir olayı ekler.","collision":"Evlilik sözleşmesi veya düğün olayıyla karışır.","fit":"displacement","loses":"Cinsel birleşmenin gerçekleşmesi ve örtülü anlatım işlevi kaybolur.","preserves":"Eşler arasındaki ilişki alanını korur."},"text":"evlenmek"}],"identity_rationale":"Kaynak ifadesi, belirli bir eşli söz dizimini erkeğin eşiyle cinsel birleşmesini örtülü biçimde anlatan bir kullanım olarak sınırlar; hazırlanan dal bu kalıp ve katılımcı sınırını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"eşiyle cinsel birleşmede bulunmak"}],"lexicalization_note":"Tanım yalnızca verilen eşli söz kalıbına bağlıdır ve bu örtülü cinsel birleşme anlamını yalın kökün genel anlamı gibi sunmaz.","neighbor_coverage_note":"On yedi adayın tamamı değerlendirildi; aynı olayı ve örtülü anlatım işlevini paylaşan üç dal seçildi, yalnızca evlilik çevresini paylaşanlar ve bu kökün başka dalları sınırı keskinleştirmediği için dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Sağlanan sınırlar katılımcı, olay ve örtülü anlatım bakımından örtüşür; kartlardaki ifade farkı ayrı bir kavramsal sınır oluşturmuyor.","focus_only":null,"gloss":"eşle cinsel birleşmeyi örtülü anlatma","neighbor_only":null,"neighbor_ref":"root_001164/B003","relation_type":"synonym","shared_zone":"Her iki dal da erkeğin eşiyle cinsel birleşmesini doğrudan söylemeden anlatır."},{"boundary_match":"partial","distinction":"Olay örtüşür, fakat odak dalın anlamı tek bir örtülü kalıba bağlıyken komşu dal daha genel ve doğrudan anlatımları da içerir.","focus_only":"Odak dal yalnızca belirli bir eşli girme kalıbının örtülü anlamıdır.","gloss":"eşler arası birleşme","neighbor_only":"Komşu dal evlenme ve cinsel birleşmeyi doğrudan karşılayan daha geniş bir söz ailesini kapsar.","neighbor_ref":"root_000259/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da eşler arasındaki cinsel birleşmeyi gösterebilir."},{"boundary_match":"partial","distinction":"İletilen olay aynı olsa da örtülü anlatımı kuran eylem ve söz kalıbı farklıdır; bu nedenle her bağlamda biçimsel olarak birbirinin yerine geçmezler.","focus_only":"Odak dal eşle girme biçimindeki belirli söz dizimine bağlıdır.","gloss":"örtülü cinsel birleşme","neighbor_only":"Komşu dal dokunma sözlerinin cinsel birleşme için örtülü kullanılmasını temel alır.","neighbor_ref":"root_001423/B002","relation_type":"near_synonym","shared_zone":"İki dal da cinsel birleşmeyi başka bir eylem üzerinden örtülü biçimde anlatır."}],"source_phrase_ar":"دخل بامرأته كناية عن الإفضاء إليها (mufradat)","source_summary":"Verilen tek tanıklık, eşle cinsel birleşmeyi doğrudan adlandırmayan ve yalnızca belirli bir söz diziminde işleyen örtülü kullanımı bildirir.","sources":["MU"],"what_is_ar":"يدخل فيه قولهم دخل بامرأته كناية عن الإفضاء إليها.","what_is_not_ar":"لا يدخل فيه مطلق دخول مكان أو مدخل."},"support_links":[]},{"boundary":"İçte veya gizli kalan yan burada kendi başına kötü değildir; kusur, aldatma ve içten bozukluk bir sonraki dalın sınırıdır.","branch_kind":"bare","branch_ref":"root_000464/B003","candidate_links":[{"candidate_id":"cand_b64278801ac82d99c5da","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:29:1:2","qac_word_ref":"89:29:1","surface_ar":"ٱدْخُلِ"}],"gloss":"içte kalan yan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya işin dışarıdan görünmeyen iç durumu ve saklı yönü anlatılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Giysinin bedene bakan iç kenarı, aynı içte kalma ilişkisinin somut bir görünümüdür."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birine gizli bir işi açmak veya onun saklı iç yüzünü bilmek de bu iç alanla ilişkilidir."}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin veya işin görünmeyen iç yüzü ile bir nesnenin bedene ya da merkeze bakan iç yanı birlikte düşünülürken uygundur.","boundary_detail":"İçte veya gizli kalan yan burada kendi başına kötü değildir; kusur, aldatma ve içten bozukluk bir sonraki dalın sınırıdır.","branch_image_ar":"الباطن والسريرة","concept_gloss":"içte kalan yan","contextual_glosses":[{"applicability":"Kişinin eğilimi, niyeti ya da bir işin dışarıdan görünmeyen gerçek durumu anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Giysinin bedene bakan somut iç kenarını kapsamaz.","preserves":"Kişi veya işin görünmeyen iç durumunu korur."},"facet_ids":["F001","F003"],"text":"birinin veya bir işin iç yüzü","usage_role":"general"},{"applicability":"Söz konusu olan giysinin doğrudan bedene dönük olan kenarıysa tam ve doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişi ve işlerin saklı iç yüzünü dışarıda bırakır.","preserves":"Somut iç yan ile bedene yakınlık ilişkisini korur."},"facet_ids":["F002"],"text":"giysinin bedene bakan iç kenarı","usage_role":"contextual"}],"definition":"Bir kişinin, işin veya nesnenin dışarıdan görünmeyen, içeride kalan yanı söz konusudur. Bu yan kişinin iç yüzü ve saklı işleri olabileceği gibi giysinin bedene değen iç kenarı da olabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya işin dışarıdan görünmeyen iç durumu ve saklı yönü anlatılır."},{"facet_id":"F002","role":"specialization","statement":"Giysinin bedene bakan iç kenarı, aynı içte kalma ilişkisinin somut bir görünümüdür."},{"facet_id":"F003","role":"associated_use","statement":"Birine gizli bir işi açmak veya onun saklı iç yüzünü bilmek de bu iç alanla ilişkilidir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Yalnızca gizli bilgi adı olarak anlaşılabilir.","fit":"narrowing","loses":"Kişi veya işin genel iç yüzünü ve giysinin somut iç kenarını siler.","preserves":"Başkalarından saklanan bilgi yönünü korur."},"text":"sır"}],"identity_rationale":"Kaynak ifadesi kişinin veya işin görünmeyen iç yüzünü, gizli tutulan bilgiyi ve giysinin bedene bakan iç kenarını aynı içte kalma düzeninde toplar; dalın tarafsız iç yüz vurgusu bu kapsamı karşılar.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir işin veya kişinin iç yüzü"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"giysinin bedene bakan iç kenarı"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"saklı tutulan iş veya açılan gizli iç yüz"}],"lexicalization_note":"Tanım yalın dalın içte kalan yan anlamını verir; başka dallardaki kalıplaşmış veya bozukluk bildiren kullanımları buraya taşımaz.","neighbor_coverage_note":"On yedi adayın tamamı incelendi; iç yüz, gizleme ve olumsuz iç bozuklukla en açıklayıcı üç karşılaştırma seçildi, yalnızca örtme eylemini veya uzak kardeş anlamlarını paylaşan adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Soyut iç yüz alanında güçlü biçimde örtüşürler; odak dal somut iç kenara uzanırken komşu dal gizli olanı öğrenme ve bilme yönünde genişler.","focus_only":"Odak dal giysinin bedene bakan iç kenarı gibi somut bir iç yanı da kapsar.","gloss":"gizli iç yüz","neighbor_only":"Komşu dal bir şeyin iç yapısını öğrenme ve gizli olanı bilme sürecini daha açık biçimde kapsar.","neighbor_ref":"root_000128/B002","relation_type":"near_synonym","shared_zone":"Her iki dal kişi veya işin görünmeyen iç tarafını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal bir iç durum veya iç yan adıdır; komşu dal ise gizleme ve gizli iletişim eylemlerini merkez alır.","focus_only":"Odak dal gizli ya da içte kalan şeyin kendisini ve iç konumunu bildirir.","gloss":"iç yüz ve gizleme","neighbor_only":"Komşu dal bir şeyi gizleme, gizlice konuşma veya saklı biçimde iletme eylemini bildirir.","neighbor_ref":"root_000697/B001","relation_type":"near_neighbor","shared_zone":"İki dal da başkalarından görünmeyen bilgi ve iç durum alanında buluşur."},{"boundary_match":"partial","distinction":"İçte bulunma ortak olsa da odak dal tarafsızdır; komşu dal olumsuz bir kusur ya da bozulmayı zorunlu kılar.","focus_only":"Odak dal içte kalan yanı değer yargısı taşımadan anlatabilir.","gloss":"iç yüz ve içten bozukluk","neighbor_only":"Komşu dal içteki şeyin kusur, bozukluk, kuşku veya aldatma niteliği taşımasını gerektirir.","neighbor_ref":"root_000464/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal görünmeyen veya içeride bulunan bir niteliğe yönelir."}],"source_phrase_ar":"الدخلة باطن أمر الرجل وأنا عالم بدخلته (maqayis)؛ الدخلة بطانة من الأمر وعالم بدخلة أمرهم (ayn)؛ دخلل أمري إذا بثثته مكتومك (jamhara)؛ داخلة الإزار طرفه الذي يلي الجسد وداخلة الرجل باطن أمره (sihah)","source_summary":"Toplu kanıt, kişi ve işlerin saklı iç yüzünü merkeze alır; gizli bilginin açılmasını ve giysinin bedene bakan kenarını bu içte kalma ilişkisinin soyut ve somut görünümleri olarak birleştirir.","sources":["MQ","AY","JA","SI"],"what_is_ar":"يدخل فيه باطن الأمر والسريرة والدخلة والداخلة، وطرف الإزار الذي يلي الجسد، وما يطلع عليه من مكتوم الأمر.","what_is_not_ar":"لا يدخل فيه الفساد أو المكر من حيث هو عيب، إلا إذا دل السياق على الباطن فقط."},"support_links":["sup_01d456b25c95b81e9f96"]},{"boundary":"Yalnızca içeride veya gizli olmak yetmez; bu dalda içteki nitelik kusur, bozulma, kuşku, aldatma ya da gizli düşmanlık taşımalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000464/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:29:1:2","qac_word_ref":"89:29:1","surface_ar":"ٱدْخُلِ"}],"gloss":"içten bozan kusur","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi, iş, köken veya nesnede içeride yer alan kusur ya da bozulma bulunur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İç bozukluk kuşku, hile, aldatma veya gizli düşmanlık olarak davranış ve ilişki alanına uzanır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişide zihinsel yetersizlik ya da kökende bozukluk bulunması özel bir görünüm oluşturur."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İçi çürümüş bir palmiye veya böcekçe yenmiş yiyecek, nesnedeki iç bozulmanın somut örnekleridir."}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kusurun veya bozulmanın kişi, iş, köken ya da nesnenin içinde bulunması ve dışarıdan hemen görünmemesi temel olduğunda uygundur.","boundary_detail":"Yalnızca içeride veya gizli olmak yetmez; bu dalda içteki nitelik kusur, bozulma, kuşku, aldatma ya da gizli düşmanlık taşımalıdır.","branch_image_ar":"فساد مستبطن","concept_gloss":"içten bozan kusur","contextual_glosses":[{"applicability":"Bir işte, kişide, kökende veya nesnede saklı bir kusur ve bozulma bulunduğunda genel karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aldatma ve gizli düşmanlık gibi amaçlı davranış görünümlerini açıkça belirtmez.","preserves":"İçte yer alan kusur ve bozulma çekirdeğini korur."},"facet_ids":["F001","F003","F004"],"text":"içten bozukluk","usage_role":"general"},{"applicability":"İç bozukluk antları veya güven ilişkisini aldatma aracı yapma biçiminde ortaya çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Zihinsel kusur, köken bozukluğu ve nesnelerdeki çürüme görünümlerini kapsamaz.","preserves":"Olumsuzluğun gizli ve amaçlı aldatma yönünü korur."},"facet_ids":["F002"],"text":"gizli hile ve aldatma","usage_role":"contextual"}],"definition":"Bir kişinin, soyun, işin veya şeyin içinde dışarıdan hemen görünmeyen bir kusur ya da bozulma bulunur. Bu iç bozukluk kuşku, aldatma, gizli düşmanlık, zihinsel yetersizlik, çürüme veya yenme zararı biçiminde gerçekleşebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi, iş, köken veya nesnede içeride yer alan kusur ya da bozulma bulunur."},{"facet_id":"F002","role":"extension","statement":"İç bozukluk kuşku, hile, aldatma veya gizli düşmanlık olarak davranış ve ilişki alanına uzanır."},{"facet_id":"F003","role":"specialization","statement":"Kişide zihinsel yetersizlik ya da kökende bozukluk bulunması özel bir görünüm oluşturur."},{"facet_id":"F004","role":"example","statement":"İçi çürümüş bir palmiye veya böcekçe yenmiş yiyecek, nesnedeki iç bozulmanın somut örnekleridir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Dışarıdan açıkça görülen sıradan eksikliklerle karışır.","fit":"narrowing","loses":"Kusurun içte veya gizli oluşunu, aldatma ve iç çürüme uzantılarını göstermez.","preserves":"Olumsuz eksiklik ve bozukluk yönünü korur."},"text":"kusur"}],"identity_rationale":"Kaynak ifadesi soydaki veya işteki kusurdan zihinsel bozukluğa, içten çürümüş bitkiye, bozulmuş yiyeceğe, kuşkuya ve gizli aldatmaya uzanan olumsuz bir iç bozukluk alanı kurar; hazırlanan dal bu ortak niteliği korur.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"içteki kusur, bozukluk veya kuşku"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"antları hile ve aldatma aracı yapmak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"içten kusurlu, zayıf veya zihni bozuk"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"içi çürümüş palmiye"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"böcekçe yenmiş veya kurtlanmış yiyecek"}],"lexicalization_note":"Yalın iç kusur çekirdeği, antları aldatma aracı yapma, içi çürümüş bitki ve bozulmuş yiyecek gibi kalıba bağlı özel kullanımlardan ayrı tutulur.","neighbor_coverage_note":"On yedi adayın tamamı karşılaştırıldı; iç bozulma, genel kusur ve güvene aykırı davranış sınırlarını gösteren üçü seçildi, yalnızca hile örneğini ya da başka kardeş anlamları paylaşanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bozucu iç kusurda örtüşürler; odak dal farklı taşıyıcılardaki gizli bozukluğu genişçe toplarken komşu dal arılığın bozulması çevresinde başka olumsuz niteliklere açılır.","focus_only":"Odak dal zihinsel bozukluğu, köken kusurunu, gizli aldatmayı ve nesnelerde iç çürümeyi kapsar.","gloss":"içe karışan bozukluk","neighbor_only":"Komşu dal arılığa karışan bozulmanın yanı sıra eğrilik, sertlik ve ağır sıkıntı görünümlerine uzanır.","neighbor_ref":"root_000977/B003","relation_type":"near_synonym","shared_zone":"Her iki dal bir şeyin iç bütünlüğünü bozan kusur veya bozulmayı anlatır."},{"boundary_match":"partial","distinction":"Komşu dal genel kusur alanıdır; odak dal ise kusuru içte bulunma ve içeriden bozma ilişkisiyle sınırlar.","focus_only":"Odak dal kusurun içeride, saklı veya içten bozucu olmasını gerektirir.","gloss":"iç kusur ve genel kusur","neighbor_only":"Komşu dal görünür ya da görünmez her türlü eksiklik, eleştiri noktası, suçlama ve zayıflığı kapsar.","neighbor_ref":"root_001106/B003","relation_type":"near_neighbor","shared_zone":"İki dal da eksiklik ve bozukluk değerlendirmesi taşır."},{"boundary_match":"field_only","distinction":"Odak dalın çekirdeği iç kusurdur; komşu dalın çekirdeği kişinin güvene aykırı davranışı olduğundan sıradan kullanımda birbirlerinin yerine geçmezler.","focus_only":"Odak dal kusur, bozulma, kuşku ve çürümeyi davranış dışındaki taşıyıcılarda da kapsar.","gloss":"gizli bozukluk ve ihanet","neighbor_only":"Komşu dal özellikle kişiyi hain sayan bir niteleme ve bağlılık karşısındaki ihanet üzerinde durur.","neighbor_ref":"root_000841/B005","relation_type":"same_field","shared_zone":"Her iki dal güveni zedeleyen gizli olumsuzluk alanında buluşabilir."}],"source_phrase_ar":"الدخل العيب في الحسب وكالدغل (maqayis)؛ دخل فلان وهو مدخول إذا كان في عقله دخل ونخلة مدخولة عفنة الجوف (maqayis)؛ عيب في الحسب وفي هذا الأمر دخل ودغل ودخل حسبه أو عقله (ayn)؛ في أمره دخل أي فساد (jamhara)؛ الدخل العيب والريبة ومكرا وخديعة ومدخول في عقله ونخلة مدخولة (sihah)؛ الدخل كناية عن الفساد والعداوة المستبطنة كالدغل ومدخول كناية عن بله في عقله وفساد في أصله (mufradat)","source_summary":"Toplu anlatım, içeride bulunan olumsuz kusuru ortak çekirdek sayar; soy ve akıldaki bozukluğu, işteki kuşkuyu, aldatmayı, gizli düşmanlığı, iç çürümeyi ve yiyecek zararını bu çekirdeğin farklı görünümleri olarak sıralar.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الدخل بمعنى العيب والفساد والدغل والريبة والمكر والخديعة والعداوة المستبطنة، وما وصف بمدخول لخلل في العقل أو الأصل أو الجوف أو الطعام.","what_is_not_ar":"لا يدخل فيه مجرد السريرة الباطنة بلا عيب، ولا مجرد الانتساب الداخل بلا فساد."},"support_links":[]},{"boundary":"Kişi veya topluluk ilişkisine sonradan girme esastır; mali gelir ve iç kusur anlamları bu dala ait değildir.","branch_kind":"bare","branch_ref":"root_000464/B005","candidate_links":[{"candidate_id":"cand_a19b0a1f12282f0ead07","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:29:1:2","qac_word_ref":"89:29:1","surface_ar":"ٱدْخُلِ"}],"gloss":"sonradan araya katılan kimse","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi başka birinin özel işlerine veya köken bakımından ait olmadığı bir topluluğa girer."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Topluluğa katılma, gerçek kökenden değil sonradan kurulan bir bağlılıktan doğar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bilmediği işlere kendini sokan kişi, araya girmenin uygunsuz ve gösterişli biçimini temsil eder."}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin özel işlerine alınan, bir topluluğa dışarıdan bağlanan veya bilmediği işe kendini sokan kişi için kullanılabilir.","boundary_detail":"Kişi veya topluluk ilişkisine sonradan girme esastır; mali gelir ve iç kusur anlamları bu dala ait değildir.","branch_image_ar":"دخيل يخالط القوم أو الأمر","concept_gloss":"sonradan araya katılan kimse","contextual_glosses":[{"applicability":"Kişinin bir topluluğun gerçek kökeninden gelmediği halde ona bağlanması anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir kişinin özel işlerine alınma ve bilgisizce işe karışma görünümlerini kapsamaz.","preserves":"Dışarıdan gelme ve topluluğa sonradan bağlanma yönünü korur."},"facet_ids":["F001","F002"],"text":"topluluğa dışarıdan katılmış kimse","usage_role":"contextual"},{"applicability":"Kişi yeterli bilgisi olmadığı halde bir işi sahiplenerek araya girdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yakın sırdaş ve topluluğa sonradan bağlanan kişi anlamlarını dışarıda bırakır.","preserves":"Uygunsuz biçimde işe aradan girme yönünü korur."},"facet_ids":["F003"],"text":"bilmediği işe zorla karışan kimse","usage_role":"contextual"}],"definition":"Bir kimse, başka bir kişinin özel işlerine alınır veya köken olarak kendilerinden olmadığı bir topluluğa katılır. Bilgisi olmadığı halde işlere zorla karışan kişi de aynı araya girme düzeninin olumsuz bir görünümüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi başka birinin özel işlerine veya köken bakımından ait olmadığı bir topluluğa girer."},{"facet_id":"F002","role":"specialization","statement":"Topluluğa katılma, gerçek kökenden değil sonradan kurulan bir bağlılıktan doğar."},{"facet_id":"F003","role":"associated_use","statement":"Bilmediği işlere kendini sokan kişi, araya girmenin uygunsuz ve gösterişli biçimini temsil eder."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Hiçbir ilişki kurmamış tanınmayan kişiyle karışır.","fit":"narrowing","loses":"Topluluğa veya kişinin özel işlerine gerçekten katılmış olma ilişkisini siler.","preserves":"Topluluğun asıl kökeninden gelmeme yönünü korur."},"text":"yabancı"}],"identity_rationale":"Kaynak ifadesi hem bir kişinin özel işlerine alınan kimseyi hem de köken olarak kendilerinden olmadığı halde bir topluluğa katılanı, ayrıca bilmediği işe zorla karışanı anlatır; dal bu sonradan araya girme bağını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"özel işlere alınan veya bir topluluğa dışarıdan katılan kimse"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"kişinin özel işlerine aldığı yakın kimse"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bilmediği işlere zorla karışan kimse"}],"lexicalization_note":"Tanım, kişi ve topluluk ilişkisine giren kimseyi yalın dal olarak açıklar; bozuk soy yargısını veya başka kalıplara bağlı anlamları kendiliğinden eklemez.","neighbor_coverage_note":"On yedi adayın tümü değerlendirildi; dışarıdan topluluğa bağlanma ve araya girme sınırlarını en iyi gösteren üçü seçildi, yalnızca akrabalık alanını veya başka kardeş dalları paylaşanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Topluluğa dışarıdan katılma alanında örtüşürler; odak dal daha tarafsız ve ilişki bakımından geniş, komşu dal ise damgalayıcı ve soy bağına daha sıkı bağlıdır.","focus_only":"Odak dal bir kişinin özel işlerine alınan yakın kimseyi ve bilgisizce işe karışanı da kapsar.","gloss":"topluluğa dışarıdan eklenen kimse","neighbor_only":"Komşu dal topluluğa yapıştırılmış kişinin kötü tanınması ve düşük görülmesi gibi olumsuz değerlendirmeleri de taşır.","neighbor_ref":"root_000647/B002","relation_type":"near_synonym","shared_zone":"Her iki dal köken olarak topluluktan olmadığı halde ona bağlanan kişiyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal bağlı kişinin durumunu daha geniş ilişkilerle anlatır; komşu dal ise bağlama veya soy iddiası kurma işlemini merkez alır.","focus_only":"Odak dal kişinin özel işlerine girme ve bilmediği işe karışma görünümlerini de içerir.","gloss":"sonradan topluluğa bağlanma","neighbor_only":"Komşu dal birini bir topluluğa veya gerçek babasından başkasına bağlama eylemini öne çıkarır.","neighbor_ref":"root_001347/B002","relation_type":"near_synonym","shared_zone":"İki dal da gerçek kökenden farklı bir topluluğa sonradan bağlanma durumunu kapsar."},{"boundary_match":"field_only","distinction":"Odak dalın katılma ilişkisi tarafsız veya yakın olabilir; komşu dalda çıkarcılık ve istenmeme belirleyicidir.","focus_only":"Odak dal dışarıdan katılan kişinin yakın ve kabul edilmiş olmasına da izin verir.","gloss":"araya katılan ve asalak","neighbor_only":"Komşu dal topluluğun işine çıkar için sızan asalak ve istenmeyen kişiyi zorunlu kılar.","neighbor_ref":"root_001216/B009","relation_type":"same_field","shared_zone":"Her iki dal bir gruba dışarıdan giren kişiyi konu eder."}],"source_phrase_ar":"دخيلك الذي يداخلك في أمورك وبنو فلان في بني فلان دخيل (maqayis)؛ دخيلك الذي تدخله في أمورك ودخلل والمتدخل في الأمور المتكلف فيها (ayn)؛ فلان دخيل في بني فلان إذا كان من غيرهم (jamhara)؛ هم دخل في بني فلان ودخيل الرجل ودخلله الذي يداخله في أموره (sihah)؛ وعن الدعوة في النسب (mufradat)","source_summary":"Toplu kanıt, dışarıdan gelip bir kişinin özel işlerine veya bir topluluğun bağına giren kimseyi ortaklaştırır; sonradan soy bağı iddiasını ve bilgisizce işe karışmayı bu ilişkinin özel görünümleri olarak verir.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الدخيل والدخلل ومن يداخل الشخص في أموره، والقوم المنتسبون في غيرهم، والمتدخل المتكلف في الأمور.","what_is_not_ar":"لا يدخل فيه الدخل المالي ولا العيب إلا إذا صرح بفساد النسب أو الأصل."},"support_links":["sup_75d44d48f421df9e872b"]},{"boundary":"Bu dal parasal veya mal niteliğindeki girişi anlatır; genel içeri girme ile gizli kusur anlamlarını kapsamaz.","branch_kind":"bare","branch_ref":"root_000464/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:29:1:2","qac_word_ref":"89:29:1","surface_ar":"ٱدْخُلِ"}],"gloss":"gelir","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kazanç veya getiri olarak kişinin mülküne ya da işine giren mal anlatılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu mali giriş, hesap düzeninde dışarı çıkan malın karşıtı olarak belirlenir."}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi, mülk veya iş bakımından içeri giren kazanç ve bunun gider karşıtı oluşu anlatıldığında tam karşılıktır.","boundary_detail":"Bu dal parasal veya mal niteliğindeki girişi anlatır; genel içeri girme ile gizli kusur anlamlarını kapsamaz.","branch_image_ar":"ما يدخل من كسب","concept_gloss":"gelir","contextual_glosses":[{"applicability":"Tarihsel mülk veya işletme bağlamında mali girişin açıkça anlatılması gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek başına kullanıldığında gider karşıtlığını doğrudan belirtmez.","preserves":"Kazancın bir işe veya mülke girişini açıkça korur."},"facet_ids":["F001"],"text":"işletmeye giren kazanç","usage_role":"explanatory"}],"definition":"Bir kişinin mülküne veya yürüttüğü işe kazanç ya da getiri olarak giren maldır. Hesap ilişkisinde dışarı çıkan malın karşı kutbunu oluşturur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kazanç veya getiri olarak kişinin mülküne ya da işine giren mal anlatılır."},{"facet_id":"F002","role":"specialization","statement":"Bu mali giriş, hesap düzeninde dışarı çıkan malın karşıtı olarak belirlenir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Henüz tahsil edilmemiş değer artışı veya genel başarıyla karışabilir.","fit":"narrowing","loses":"Değerin mülke giren akış ve giderin karşıtı olma yönünü zayıflatır.","preserves":"Elde edilen mali değeri korur."},"text":"kazanç"}],"identity_rationale":"Kaynak ifadesi, kişinin mülküne veya işletmesine kazanç olarak giren şeyi ve bunun dışarı çıkan malın karşıtı oluşunu açıkça bildirir; hazırlanan mali giriş dalı bu iki unsuru korur.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"gelir veya içeri giren kazanç"}],"lexicalization_note":"Tanım, yalın mali giriş ve gelir anlamıyla sınırlıdır; kazancın özel elde edilme yollarını veya başka dalların kullanımlarını eklemez.","neighbor_coverage_note":"On yedi adayın tamamı karşılaştırıldı; gelir-gider karşıtını, kazanma eylemini ve ticari artışı ayıran üçü seçildi, fiyat, mal edinme ve genel geçim alanındaki daha uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Paylaşılan mali akış ekseninde yönleri karşıttır; odak dal giriş, komşu dal çıkış tarafıdır.","focus_only":"Odak dal mülke veya işe giren mali değeri bildirir.","gloss":"gelir ve gider","neighbor_only":"Komşu dal belirli bir amaçla dışarı çıkarılan malı bildirir.","neighbor_ref":"root_000400/B003","relation_type":"antonym","shared_zone":"İki dal aynı mali hesabın içeri ve dışarı yönlü akışlarını gösterir."},{"boundary_match":"partial","distinction":"Odak dal sonuçta oluşan mali giriştir; komşu dal bu değeri elde etme eylemidir.","focus_only":"Odak dal elde edilmiş değerin içeri giren mali kalem oluşunu bildirir.","gloss":"gelir ve kazanma","neighbor_only":"Komşu dal malı kazanma veya kazanca ulaşma eylemini bildirir.","neighbor_ref":"root_000580/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal ekonomik değer ve kazanç alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal genel mali giriştir; komşu dal özellikle alım satım sonucundaki artışı anlatır.","focus_only":"Odak dal kaynağı ne olursa olsun içeri giren kazanç kalemini kapsar.","gloss":"gelir ve ticaret artısı","neighbor_only":"Komşu dal alışveriş ve ticaret sonunda oluşan artışla sınırlıdır.","neighbor_ref":"root_000533/B001","relation_type":"near_neighbor","shared_zone":"Ticari artış bir işin gelirine dönüşebildiği için iki alan kesişebilir."}],"source_phrase_ar":"الدخل ما دخل ضيعة الإنسان من المنالة (ayn)؛ الدخل خلاف الخرج (sihah)","source_summary":"Kanıt, kişinin mülküne kazanç olarak giren malı ortak çekirdek sayar ve onu dışarı çıkan malın karşısına yerleştirir.","sources":["AY","SI"],"what_is_ar":"يدخل فيه الدخل بمعنى مقابل الخرج، وما يدخل ضيعة الإنسان من المنالة.","what_is_not_ar":"لا يدخل فيه الدخول المكاني ولا الدخل بمعنى الفساد."},"support_links":[]},{"boundary":"Bu dal genel sulama değil, develerin su başındaki ikinci girişini veya sürüye aradan katılarak içmesini düzenleyen özel işlemdir.","branch_kind":"bare","branch_ref":"root_000464/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:29:1:2","qac_word_ref":"89:29:1","surface_ar":"ٱدْخُلِ"}],"gloss":"develeri yeniden ya da araya katarak sulama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Su içmiş develer ikinci kez su başına döndürülerek yeniden içirilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Susuz develer henüz içmemiş develerin arasına katılır ve onlarla birlikte içmeleri sağlanır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başka bir görünümde sürü, aralarında sıkışıklık olacak biçimde bir kerede su başına sürülür."}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Develerin ikinci kez su başına götürülmesi veya susuz hayvanların içen sürünün arasına katılması anlatıldığında kullanılmalıdır.","boundary_detail":"Bu dal genel sulama değil, develerin su başındaki ikinci girişini veya sürüye aradan katılarak içmesini düzenleyen özel işlemdir.","branch_image_ar":"إدخال الإبل في الشرب مرة أخرى","concept_gloss":"develeri yeniden ya da araya katarak sulama","contextual_glosses":[{"applicability":"Sürü daha önce içmişken yeniden su başına döndürülüyorsa bu açık karşılık kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Susuz hayvanları başka develerin arasına katma ve tek seferlik sıkışık sulama çeşitlerini kapsamaz.","preserves":"Develerin yeniden su başına götürülmesi işlemini korur."},"facet_ids":["F001"],"text":"develeri ikinci kez suya götürmek","usage_role":"contextual"},{"applicability":"İkinci içişin, susuz hayvanların öteki develerin arasına sokulmasıyla sağlandığı durumda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bütün sürüyü yeniden suya döndürme ve sıkışık biçimde bir kerede sürme çeşitlerini dışarıda bırakır.","preserves":"Susuz deveyi sürü arasına katma ve içmesini sağlama yönünü korur."},"facet_ids":["F002"],"text":"susuz develeri içen sürünün arasına katmak","usage_role":"explanatory"}],"definition":"Develer su içtikten sonra yeniden su başına götürülür veya susuz develer içmekte olanların arasına katılarak ikinci kez içmeleri sağlanır. Bir kaynak anlatımı, sürünün bir kerede sıkışık biçimde suya sürülmesini de aynı düzenin başka bir yüzü sayar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Su içmiş develer ikinci kez su başına döndürülerek yeniden içirilir."},{"facet_id":"F002","role":"specialization","statement":"Susuz develer henüz içmemiş develerin arasına katılır ve onlarla birlikte içmeleri sağlanır."},{"facet_id":"F003","role":"source_variant","statement":"Başka bir görünümde sürü, aralarında sıkışıklık olacak biçimde bir kerede su başına sürülür."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Her hayvanı ve her türlü su verme işlemini kapsar.","collision":"Sıradan ilk sulama işlemiyle karışır.","fit":"broadening","loses":"İkinci kez götürme veya sürünün arasına katma düzenini siler.","preserves":"Hayvana su içirme amacını korur."},"text":"sulamak"}],"identity_rationale":"Kaynak ifadesi develerin içtikten sonra yeniden su başına götürülmesini temel görünüm olarak verir; ayrıca susuz develeri henüz içmemiş olanların arasına katma ve sürüyü bir kerede sıkışık biçimde sulama çeşitlemelerini de açıkça kaydeder.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"develeri ikinci kez suya götürme veya susuz deveyi sürüye katma"}],"lexicalization_note":"Tanım, yalın dalın deve sulama düzenini verir ve bu özel hayvancılık anlamını genel içeri girme ya da her türlü sulama anlamına genişletmez.","neighbor_coverage_note":"On yedi adayın tamamı değerlendirildi; su başından geçirme, suya doyma ve sırada bekleme ile en açıklayıcı üç sınır seçildi, gün aralığına dayalı sulama adları ve uzak kardeş dallar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın amacı ve sonucu içmedir; komşu dalda temel işlem yalnızca su yalağı boyunca geçirmektir.","focus_only":"Odak dal develeri ikinci kez içirmek veya susuz deveyi içenlerin arasına katmak için su başına sokar.","gloss":"yeniden içirme ve su başından geçirme","neighbor_only":"Komşu dal develeri su yalağının yanından ya da üzerinden geçirmekle sınırlıdır ve içirme sonucu gerektirmez.","neighbor_ref":"root_000867/B010","relation_type":"near_neighbor","shared_zone":"Her iki dal develerin su yalağı çevresindeki yönlendirilmesini anlatır."},{"boundary_match":"field_only","distinction":"Odak dal düzenleme işlemidir; komşu dal ise içmenin tamamlanıp hayvanın suya doyması sonucudur.","focus_only":"Odak dal sürünün suya hangi sırayla veya kaçıncı kez sokulduğunu düzenler.","gloss":"sulama düzeni ve suya doyma","neighbor_only":"Komşu dal develerin yeterince su içmiş ve susuzluğunu gidermiş olma sonucunu bildirir.","neighbor_ref":"root_001509/B004","relation_type":"same_field","shared_zone":"İki dal deve sulama sürecinin farklı yönlerini konu eder."},{"boundary_match":"partial","distinction":"Odak dalda araya sokma veya geri döndürme vardır; komşu dalda hayvanlar sıranın açılmasını bekler.","focus_only":"Odak dal susuz develerin içenlerin arasına etkin biçimde katılmasını veya yeniden götürülmesini bildirir.","gloss":"araya katma ve sırada bekleme","neighbor_only":"Komşu dal su başındaki içenlerin arkasında bekleyip onların ayrılmasından sonra girecek develeri adlandırır.","neighbor_ref":"root_000851/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal bazı develerin su başındaki başka develere göre konumunu ve içme sırasını düzenler."}],"source_phrase_ar":"الدخال في الورد أن تشرب الإبل ثم ترد إلى الحوض (maqayis)؛ سقيت الإبل دخالا إذا حملتها على الحوض ثانية والدخال في وجه آخر أن تحملها على الحوض بمرة واحدة عراكا (ayn)؛ أورد الرجل إبله دخالا (jamhara)؛ الدخال في الورد أن يشرب البعير ثم يرد من العطن إلى الحوض (sihah)؛ الدخال في الإبل أن يدخل إبل في أثناء ما لم تشرب لتشرب معها ثانيا (mufradat)","source_summary":"Toplu anlatım, develeri su başına yeniden sokarak içirmeyi merkez alır; susuz hayvanları sürünün arasına katma ile sürüyü bir kerede sıkışık götürme biçimlerini aynı ad altında farklı uygulamalar olarak korur.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الدخال في الورد: أن ترد الإبل إلى الحوض ثانية أو يدخل بعير عطشان بين بعيرين ليتم شربه، وكذلك إيرادها عراكا في وجه آخر.","what_is_not_ar":"لا يدخل فيه مطلق الدخول ولا الدخل المالي."},"support_links":[]},{"boundary":"Dal, parçaların birbirine geçmesi veya başka parçaların arasında kalmasıyla sınırlıdır; küçük kuş adı ve örme kap adı ayrı dallardır.","branch_kind":"bare","branch_ref":"root_000464/B008","candidate_links":[{"candidate_id":"cand_a19b0a1f12282f0ead07","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:29:1:2","qac_word_ref":"89:29:1","surface_ar":"ٱدْخُلِ"}],"gloss":"iç içe geçme ve arada kalma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir parçanın başka parçaların arasına girmesi veya onlarla iç içe birleşmesi temel ilişkidir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eklemlerin birbirine geçmesi ve etin bir sinir üzerinde toplanması yapısal örneklerdir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir ana rengin içinde başka renklerin dağınık biçimde bulunması görsel alandaki uzantıdır."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kuşun sırtıyla karnı arasındaki tüyler ve ağaç kökleri arasına giren ot, ara konum örnekleridir."}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Parçalar birbirine geçtiğinde, bir çekirdek çevresinde toplandığında veya iki bölüm arasındaki iç konumu doldurduğunda uygundur.","boundary_detail":"Dal, parçaların birbirine geçmesi veya başka parçaların arasında kalmasıyla sınırlıdır; küçük kuş adı ve örme kap adı ayrı dallardır.","branch_image_ar":"تداخل الأجزاء وما بين الداخل","concept_gloss":"iç içe geçme ve arada kalma","contextual_glosses":[{"applicability":"Eklemler veya başka yapısal parçalar birbirinin arasına girerek bağlandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Renk karışımını ve iki bölge arasında bulunan tüy ya da ot örneklerini kapsamaz.","preserves":"Yapısal iç içe geçme ve birleşme ilişkisini korur."},"facet_ids":["F001","F002"],"text":"parçaların birbirine geçmesi","usage_role":"general"},{"applicability":"Tek bir ana görünüm içinde başka renkler dağınık biçimde bulunduğunda açıklayıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eklemler, et, tüy ve otla ilgili yapısal örnekleri dışarıda bırakır.","preserves":"Renk parçalarının ana renk içinde yer almasını korur."},"facet_ids":["F003"],"text":"bir rengin içine başka renklerin karışması","usage_role":"contextual"},{"applicability":"Tüy veya ot gibi bir parça iki bölgenin arasında ya da başka yapıların kökünde yer aldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Karşılıklı geçme ve renklerin birbirine karışması süreçlerini göstermez.","preserves":"Parçanın içteki ara konumunu korur."},"facet_ids":["F004"],"text":"iki bölüm arasında kalan parça","usage_role":"explanatory"}],"definition":"Parçalar birbirinin arasına girerek birleşir, bir ana bölüm çevresinde toplanır veya iki bölüm arasında yer alır. Bu düzen eklem, et, renk, tüy ve bitki örtüsü gibi farklı maddelerde görülebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir parçanın başka parçaların arasına girmesi veya onlarla iç içe birleşmesi temel ilişkidir."},{"facet_id":"F002","role":"example","statement":"Eklemlerin birbirine geçmesi ve etin bir sinir üzerinde toplanması yapısal örneklerdir."},{"facet_id":"F003","role":"extension","statement":"Bir ana rengin içinde başka renklerin dağınık biçimde bulunması görsel alandaki uzantıdır."},{"facet_id":"F004","role":"example","statement":"Kuşun sırtıyla karnı arasındaki tüyler ve ağaç kökleri arasına giren ot, ara konum örnekleridir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Düzensiz birleşme, bulanma ve toplumsal müdahale gibi ilgisiz anlamları kapsar.","collision":"Genel karışıklık veya bir işe müdahale anlamıyla karışır.","fit":"broadening","loses":"Birbirinin arasına girme, belirli bir çevrede toplanma ve ara konum ayrımlarını siler.","preserves":"Renklerin veya parçaların bir arada bulunma yönünü kısmen korur."},"text":"karışmak"}],"identity_rationale":"Kaynak ifadesi eklemlerin birbirine geçmesini, sinir çevresinde toplanan eti, bir renge karışan başka renkleri ve iki bölge arasında veya ağaç köklerinde kalan tüy ile otu ortak bir iç içelik ve ara konum düzeninde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"eklemlerin birbirine geçmesi"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir sinir üzerinde toplanmış et parçası"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bir ana renge karışmış başka renkler"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kuşun sırtıyla karnı arasındaki tüyler"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"ağaç köklerinin arasına girmiş ot"}],"lexicalization_note":"Tanım yalın iç içelik ve ara konum dalını açıklar; özel kuş ve kap adlarını ya da kalıba bağlı başka kullanımları buraya taşımaz.","neighbor_coverage_note":"On yedi adayın tamamı değerlendirildi; genel karışma, basınçlı iç içe geçme ve renk ayrımıyla üç yararlı sınır seçildi, yalnızca benzer maddi örnekleri veya uzak kardeş anlamlarını paylaşanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal iç yapı ve ara konumu ayrıntılandırır; komşu dal ise iki taraflı karışma ilişkisini örnek sınırı koymadan verir.","focus_only":"Odak dal yapısal geçme, ara konum, renk dağılımı ve belirli maddi örnekleri kapsar.","gloss":"iç içelik ve karşılıklı karışma","neighbor_only":"Komşu dal iki tarafın karşılıklı karışmasını genel ve daha soyut biçimde bildirir.","neighbor_ref":"root_000370/B006","relation_type":"near_synonym","shared_zone":"Her iki dal iki veya daha çok unsurun birbirinin alanına girmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dalın belirleyicisi iç konumdur; komşu dalda buna ek olarak güçlü baskı ve sıkışıklık zorunludur.","focus_only":"Odak dalda iç içelik baskı bulunmadan da oluşabilir ve renk, tüy veya ot gibi örneklere uzanır.","gloss":"iç içe geçme ve sıkışma","neighbor_only":"Komşu dal parçaların güçlü basınç altında sıkıca birbirine girmesini gerektirir.","neighbor_ref":"root_000495/B002","relation_type":"near_neighbor","shared_zone":"İki dal da parçaların birbirinin arasına girip yakın bağ kurmasını anlatabilir."},{"boundary_match":"field_only","distinction":"Odak dal renklerin ana renk içine karışmasını genel iç içelik düzenine bağlar; komşu dal ise belirli canlılardaki iki renkli veya çizgili görünüşü adlandırır.","focus_only":"Odak dal renk dışında eklem, et, tüy ve bitki parçalarındaki iç konumu da kapsar.","gloss":"renk karışımı ve iki renkli görünüş","neighbor_only":"Komşu dal hayvan ve bitkilerde iki rengin ayrımlı görünüşünü ve çizgili yapıyı merkez alır.","neighbor_ref":"root_000421/B004","relation_type":"same_field","shared_zone":"Her iki dal tek bir görünümde birden çok rengin bulunmasını konu edebilir."}],"source_phrase_ar":"كل لحمة مجتمعة دخلة والدخل من ريش الطائر ما بين الظهران والبطنان والدخل من الكلأ ما دخل منه في أصول الشجر (maqayis)؛ الدخلة في اللون تحليط من ألوان في لون والدخال مداخلة المفاصل بعضها في بعض (ayn)؛ كل لحمة مجتمعة على عصب فهي دخلة (jamhara)؛ الدخل من الكلأ ما دخل منه في أصول الشجر (sihah)","source_summary":"Toplu kanıt, parçaların iç içe geçmesi ve arada yer alması düzenini eklem, sinir çevresindeki et, renk karışımı, kuş tüyleri ve ağaç köklerindeki ot üzerinden farklı maddi görünümlerle açıklar.","sources":["MQ","AY","JA","SI"],"what_is_ar":"يدخل فيه مداخلة المفاصل، واللحمة المجتمعة على عصب، والدخلة في اللون، وريش ما بين الظهر والبطن، والكلأ الداخل في أصول الشجر.","what_is_not_ar":"لا يدخل فيه الطائر المسمى دخلا ولا الوعاء الدوخلة."},"support_links":["sup_75d44d48f421df9e872b"]},{"boundary":"Bu dal belirli küçük kuş adıdır; her küçük kuşa, kuşun yaşadığı çalılığa veya örme kaba genellenemez.","branch_kind":"bare","branch_ref":"root_000464/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:29:1:2","qac_word_ref":"89:29:1","surface_ar":"ٱدْخُلِ"}],"gloss":"sık ağaçlıkta barınan küçük kuş","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir küçük kuş ve bu kuşun oyuklar ile sık ağaç altlarındaki barınma alanı anlatılır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuş adının, hayvanın sık ağaçların arasına girme davranışından doğduğu açıklanır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kuş adının iki farklı çoğul biçimi aktarılır."}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Adı bilinmeyen genel bir kuş türü gibi değil, kanıtta oyuk ve sık ağaçlık yaşamıyla tanımlanan belirli küçük kuş için kullanılmalıdır.","boundary_detail":"Bu dal belirli küçük kuş adıdır; her küçük kuşa, kuşun yaşadığı çalılığa veya örme kaba genellenemez.","branch_image_ar":"طائر يدخل الغيران والشجر","concept_gloss":"sık ağaçlıkta barınan küçük kuş","contextual_glosses":[{"applicability":"Tür adının hedef dilde yerleşik bir karşılığı verilmeden yaşam alanıyla açıklanması gerektiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Adın içeri girme davranışından türetilmesi ve çoğul biçimleri açıklamada görünmez.","preserves":"Kuşun küçüklüğünü ve oyuklarla sık bitki örtüsündeki yaşamını korur."},"facet_ids":["F001"],"text":"oyuklarda ve çalılıkta yaşayan küçük kuş","usage_role":"explanatory"}],"definition":"Oyuklarda, vadi içlerinde ve sık ağaçların altında barınan belirli bir küçük kuştur. Adı, sık ağaçların arasına girmesiyle açıklanır ve iki ayrı çoğul biçimi vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir küçük kuş ve bu kuşun oyuklar ile sık ağaç altlarındaki barınma alanı anlatılır."},{"facet_id":"F002","role":"source_variant","statement":"Kuş adının, hayvanın sık ağaçların arasına girme davranışından doğduğu açıklanır."},{"facet_id":"F003","role":"source_variant","statement":"Kuş adının iki farklı çoğul biçimi aktarılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kanıtın belirlemediği ayrı bir kuş türü kimliği ekler.","collision":"Bilinen serçe türleriyle yanlış özdeşlik kurar.","fit":"displacement","loses":"Oyuk ve sık ağaçlık yaşam alanını, içeri girme açıklamasını ve özgül adı siler.","preserves":"Küçük bir kuş olma yönünü korur."},"text":"serçe"}],"identity_rationale":"Kaynak ifadesi, oyuklarda, vadi içlerinde ve sık ağaçların altında barınan küçük bir kuş adını verir; adın kuşun sık ağaçların arasına girmesiyle açıklanmasını ve iki çoğul biçimini de kaydeder.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"oyuklarda ve sık ağaç altında barınan küçük kuş"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"bu küçük kuş adının bir çoğul biçimi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bu küçük kuş adının öteki çoğul biçimi"}],"lexicalization_note":"Tanım yalın dalda kaydedilen kuş adını ve onun çoğullarını verir; yaşam alanını ayrı bir bitki anlamına dönüştürmez.","neighbor_coverage_note":"On yedi adayın tamamı karşılaştırıldı; başka bir küçük kuş, farklı özellikte bir kuş ve yaşam alanı olan sık koruluk seçildi, avlanma, başka kuş türleri ve uzak kardeş dallar ek sınır sağlamadığı için elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Küçüklük ortak bir niteliktir, fakat adlandırılan kuşlar ve onları belirleyen özellikler ayrıdır; birbirlerinin yerine kullanılamazlar.","focus_only":"Odak dal oyuk ve sık ağaç altında barınmayı ve içeri girme davranışıyla açıklanan adı içerir.","gloss":"iki küçük kuş adı","neighbor_only":"Komşu dal yalnızca başka bir adla anılan, serçeden de küçük ayrı bir kuşu bildirir.","neighbor_ref":"root_000187/B007","relation_type":"near_neighbor","shared_zone":"Her iki dal belirli bir küçük kuş adını verir."},{"boundary_match":"field_only","distinction":"Ortak alan kuş adlarıdır; boyut, yaşam alanı ve benzetilen kuş farklı olduğundan kavramsal çekirdekleri örtüşmez.","focus_only":"Odak dal küçük oluş, oyuk ve sık ağaçlık yaşamı ile tanımlanır.","gloss":"küçük kuş ve güvercine benzeyen kuş","neighbor_only":"Komşu dal yüksek bölgelerde yaşayan ve güvercine benzeyen başka bir kuşu bildirir.","neighbor_ref":"root_001066/B009","relation_type":"same_field","shared_zone":"İki dal da görünüş veya yaşam alanıyla açıklanan kuş adlarıdır."},{"boundary_match":"thematic_only","distinction":"Bağ yalnızca yaşam alanı düzeyindedir; biri kuş, öteki bitki örtüsü olduğu için anlam bakımından birbirlerinin yerine geçmezler.","focus_only":"Odak dal sık ağaçların arasında barınan kuşun kendisini adlandırır.","gloss":"çalılık kuşu ve sık koruluk","neighbor_only":"Komşu dal çok ve birbirine geçmiş ağaçlardan oluşan koruluğu adlandırır.","neighbor_ref":"root_000072/B001","relation_type":"thematic","shared_zone":"Sık ve birbirine geçmiş ağaçlık, odak kuşunun barınma sahnesini oluşturabilir."}],"source_phrase_ar":"بذلك سمي هذا الطائر دخلا (maqayis)؛ الدخل صغار الطير مأواها الغيران وبطون الأودية تحت شجر ملتف والجميع الدخاخيل (ayn)؛ الدخل طائر صغير وجمع دخل دخاخيل (jamhara)؛ الدخل طائر صغير والجمع الدخاليل (sihah)؛ الدخل طائر سمي بذلك لدخوله فيما بين الأشجار الملتفة (mufradat)","source_summary":"Toplu anlatım küçük bir kuşu, onun oyuk ve sık ağaç altı yaşam alanını, adın ağaçların arasına girme davranışıyla açıklanmasını ve iki çoğul biçimini birlikte kaydeder.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الدخل اسم الطائر الصغير، وجمعه دخاخيل أو دخاليل، مع تعليل دخوله بين الأشجار الملتفة.","what_is_not_ar":"لا يدخل فيه كل طائر صغير إذا لم يسم دخلا، ولا الوعاء الدوخلة."},"support_links":[]},{"boundary":"Bu dal belirli küçük örme kaptır; genel sepet, deri kap, kuş adı veya yalın içeri girme anlamına genişletilemez.","branch_kind":"bare","branch_ref":"root_000464/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:29:1:2","qac_word_ref":"89:29:1","surface_ar":"ٱدْخُلِ"}],"gloss":"taze palmiye meyvesi için küçük örgü sepet","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kap, palmiye yaprağından örülmüş küçük bir taşıma veya saklama nesnesidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kabın özgül kullanımı, içine taze palmiye meyvesi koymaktır."}}],"root_ar":"د خ ل","root_id":"root_000464","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Palmiye yaprağından örülmüş ve özellikle taze palmiye meyvesi koymak için kullanılan küçük kap anlatıldığında uygundur.","boundary_detail":"Bu dal belirli küçük örme kaptır; genel sepet, deri kap, kuş adı veya yalın içeri girme anlamına genişletilemez.","branch_image_ar":"دوخلة الخوص للرطب","concept_gloss":"taze palmiye meyvesi için küçük örgü sepet","contextual_glosses":[{"applicability":"Kabın geleneksel adını aktarmak yerine malzeme, boyut ve kullanımını açıklamak gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Meyvenin özellikle taze palmiye meyvesi oluşunu daha genel ifade eder.","preserves":"Palmiye yaprağını, küçük sepet biçimini ve meyve taşıma işlevini korur."},"facet_ids":["F001","F002"],"text":"palmiye yaprağından örülmüş küçük meyve sepeti","usage_role":"explanatory"}],"definition":"Palmiye yaprağından örülen küçük bir kaptır ve içine taze palmiye meyvesi konur. Kabın malzemesi, küçük oluşu ve kullanım amacı birlikte belirleyicidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kap, palmiye yaprağından örülmüş küçük bir taşıma veya saklama nesnesidir."},{"facet_id":"F002","role":"specialization","statement":"Kabın özgül kullanımı, içine taze palmiye meyvesi koymaktır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Her boyutta, her malzemeden ve her amaçla kullanılan sepetleri kapsar.","collision":"Genel taşıma ve saklama kaplarıyla karışır.","fit":"broadening","loses":"Palmiye yaprağı malzemesini, küçük boyutu ve taze meyve kullanımını siler.","preserves":"İçine ürün konan örme kap oluşunu kısmen korur."},"text":"sepet"}],"identity_rationale":"Kaynak ifadesi, palmiye yaprağından örülmüş küçük bir kabı ve içine taze palmiye meyvesi konmasını bildirir; hazırlanan dal malzeme, biçim ve kullanım amacını doğru biçimde bir arada tutar.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"taze palmiye meyvesi konan küçük örgü sepet"}],"lexicalization_note":"Tanım yalın dalda kaydedilen küçük örme kap adını verir; başka malzemeden kapları veya içine konan meyvenin genel adını kapsamaz.","neighbor_coverage_note":"On yedi adayın tamamı değerlendirildi; genel örgü kap, geniş yaprak örgüsü alanı ve deri taşıma kabıyla üç yararlı sınır seçildi, yalnızca içerik olarak meyveyi veya uzak kardeş dalları paylaşanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal malzeme, boyut ve meyve kullanımıyla dardır; komşu dal farklı örgü araç türlerine açılır.","focus_only":"Odak dal palmiye yaprağından yapılan küçük bir kap ve taze meyve kullanımını gerektirir.","gloss":"küçük meyve sepeti ve genel örgü araç","neighbor_only":"Komşu dal genel bir örgü kap ile örgü oturak parçasını aynı ad alanında kapsar.","neighbor_ref":"root_001658/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal örülerek yapılan kap benzeri bir aracı anlatabilir."},{"boundary_match":"field_only","distinction":"Odak dal tek bir küçük kap türüdür; komşu dal biçim ve işlev bakımından birbirinden farklı daha geniş bir örme nesne kümesidir.","focus_only":"Odak dal küçük olup taze palmiye meyvesi koymak için kullanılır.","gloss":"küçük meyve kabı ve çeşitli yaprak örgüleri","neighbor_only":"Komşu dal büyük meyve küfeleri, hasırlar, kalın dokumalar ve ayakkabı onarım parçası gibi çeşitli örmeleri kapsar.","neighbor_ref":"root_000415/B002","relation_type":"same_field","shared_zone":"İki dal palmiye yaprağı benzeri malzemelerin örülmesiyle yapılan nesneler alanındadır."},{"boundary_match":"field_only","distinction":"Kap işlevi ortaktır; malzeme, tipik içerik ve yapım biçimi tamamen farklıdır.","focus_only":"Odak dal palmiye yaprağından örülür ve taze meyve için kullanılır.","gloss":"örgü meyve kabı ve deri taşıma kabı","neighbor_only":"Komşu dal deriden yapılır ve toprak, et, yağ veya başka taşınan maddeleri toplar.","neighbor_ref":"root_000214/B005","relation_type":"same_field","shared_zone":"Her iki dal içine bir şey konup taşınabilen kapları anlatır."}],"source_phrase_ar":"الدوخلة سفيفة من خوص صغيرة يجعل فيها الرطب (ayn)؛ الدوخلة هذا المنسوج من الخوص يجعل فيه الرطب (sihah)؛ الدوخلة معروفة (mufradat)","source_summary":"Kanıt, küçük ve palmiye yaprağından örülmüş kabı ortaklaştırır; belirgin kullanımını taze palmiye meyvesini içine koymak olarak verir.","sources":["AY","SI","MU"],"what_is_ar":"يدخل فيه الدوخلة: سفيفة أو منسوج من خوص يجعل فيه الرطب.","what_is_not_ar":"لا يدخل فيه الدخل الطائر ولا مطلق الدخول."},"support_links":[]},{"boundary":"Anlam, köle edinme eylemini ve dinsel bağlılığı değil, özgür olmayan kişinin statüsünü bildirir.","branch_kind":"bare","branch_ref":"root_000973/B001","candidate_links":[{"candidate_id":"cand_f9427fd9b198285eba55","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَبْد","morph_features":"STEM|POS:N|LEM:Eabod|ROOT:Ebd|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:29:3:1","qac_word_ref":"89:29:3","surface_ar":"عِبَٰدِ"}],"gloss":"özgür olmayan, sahip olunan kişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi özgürün karşıtı olarak bir başkasının mülkiyetinde bulunur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hukuki ölçüt, kişinin alım satıma konu edilebilmesidir."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kölelik statüsündeki kişiyi hem toplumsal hem de eski hukuki sınırıyla karşılar.","boundary_detail":"Anlam, köle edinme eylemini ve dinsel bağlılığı değil, özgür olmayan kişinin statüsünü bildirir.","branch_image_ar":"الرق والملك","concept_gloss":"özgür olmayan, sahip olunan kişi","contextual_glosses":[{"applicability":"Bağlam tarihsel mülkiyet statüsünü zaten açıkça gösterdiğinde doğal ve kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Özgürün karşıtı olan ve bir başkasına ait sayılan kişiyi belirtir."},"facet_ids":["F001","F002"],"text":"köle","usage_role":"general"}],"definition":"Özgür olmayan, bir başkasının mülkiyetinde sayılan ve eski hukuk düzeninde alınıp satılabilen insandır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi özgürün karşıtı olarak bir başkasının mülkiyetinde bulunur."},{"facet_id":"F002","role":"specialization","statement":"Hukuki ölçüt, kişinin alım satıma konu edilebilmesidir."}],"identity_rationale":"Kaynak ifadesi, özgür kişinin karşıtı olan ve hukuken sahip olunup alınıp satılabilen insanı açıkça tanımlar. Bu nedenle dalın çekirdeği tapınma ya da boyun eğme eylemi değil, kölelik durumundaki kişidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"özgür olmayan, sahip olunan kişi"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"köleler"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"köle doğmuş veya kuşaklar boyunca köle kalmış kişiler"}],"lexicalization_note":"Dal yalın bir ad anlamıdır; tanım herhangi bir özel söz öbeğine bağlı ek anlam taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kişi ile kölelik alanını ayıran ve kölelik ile özgürleşme karşıtlığını gösteren iki ilişki sınırı en iyi açıklayan adaylardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın göndergesi köle durumundaki insandır; komşu dal ise bu insanı da içeren daha geniş bir statü, mülkiyet ve köleleştirme alanı kurar.","focus_only":"Odak dal doğrudan kölelik statüsündeki kişiyi adlandırır.","gloss":"köle kişi ile kölelik düzeni","neighbor_only":"Komşu dal kölelik durumunu, köle mülkiyetini ve köleleştirme eylemini de kapsar.","neighbor_ref":"root_000586/B003","relation_type":"near_synonym","shared_zone":"İki dal da insanın özgürlükten yoksun bırakılıp sahip olunması alanındadır."},{"boundary_match":"opposed","distinction":"Odak dal özgürlükten yoksun statüyü adlandırırken komşu dal o statünün sona erdirilmesini ve kişinin özgür kılınmasını anlatır.","focus_only":"Kişi özgür değildir ve bir başkasının mülkiyetinde sayılır.","gloss":"kölelik durumu ve özgürleşme","neighbor_only":"Kişi kölelik bağından çıkarılarak özgürlüğüne kavuşur.","neighbor_ref":"root_000979/B001","relation_type":"polarity_pair","shared_zone":"İki dal kişinin hukuki ve toplumsal özgürlük durumunu karşıt yönlerden ele alır."}],"source_phrase_ar":"العبد وهو المملوك (maqayis)؛ العبد المملوك وجمعه عبيد (ayn)؛ العبد ضد الحر (jamhara)؛ العبد خلاف الحر والجمع عبيد (sihah)؛ العبيد مماليك (tahdhib)؛ عبد بحكم الشرع الإنسان الذي يصح بيعه وابتياعه (mufradat)","source_summary":"Kaynaklar, bu kişiyi özgürün karşıtı ve sahip olunan insan olarak ortak biçimde tanımlar; hukuki açıklama alınıp satılabilmeyi belirleyici sayar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه العبد المملوك وخلاف الحر ومن يصح بيعه وابتياعه وجموع العبيد والأعبد والعبدى والمعبدة","what_is_not_ar":"ليس عبادة الله ولا الطاعة الخاضعة ولا تعبيد الطريق أو البعير"},"support_links":["sup_25fc6d9bc5a8de9d221a"]},{"boundary":"Dal, insanın Tanrı'ya nispet edilen konumunu anlatır; kişinin hukuki statüsünü veya yaptığı tapınmayı tek başına bildirmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000973/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَبْد","morph_features":"STEM|POS:N|LEM:Eabod|ROOT:Ebd|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:29:3:1","qac_word_ref":"89:29:3","surface_ar":"عِبَٰدِ"}],"gloss":"Tanrı'ya ait sayılan insan veya topluluk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Her insan yaratılmışlık ve aitlik bakımından Tanrı'nın kulu sayılabilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Çoğul adlandırma, Tanrı'ya bağlı topluluğu veya onun tarafında bulunanları gösterebilir."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaratılmışlık, aitlik ve topluluk bağlılığını hukuki kölelikle karıştırmadan birlikte karşılar.","boundary_detail":"Dal, insanın Tanrı'ya nispet edilen konumunu anlatır; kişinin hukuki statüsünü veya yaptığı tapınmayı tek başına bildirmez.","branch_image_ar":"الانتساب إلى الله عبدا","concept_gloss":"Tanrı'ya ait sayılan insan veya topluluk","contextual_glosses":[{"applicability":"Tek bir insanın yaratılmışlık ve aitlik yönünden Tanrı'ya nispet edildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çoğul kullanımın bağlı topluluk veya taraf anlamını göstermez.","preserves":"Tek kişinin Tanrı'ya ait sayılma yönünü korur."},"facet_ids":["F001"],"text":"Tanrı'nın kulu","usage_role":"contextual"},{"applicability":"Çoğul adlandırmanın bir topluluğu veya Tanrı'nın tarafında bulunanları gösterdiği yerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek tek bütün insanların yaratılmışlık temelindeki kulluğunu göstermez.","preserves":"Topluluk bağlılığını ve Tanrı'ya nispeti korur."},"facet_ids":["F002"],"text":"Tanrı'ya bağlı topluluk","usage_role":"contextual"}],"definition":"Özgür ya da köle ayrımı olmaksızın insanın, yaratılmış ve ona ait olması bakımından Tanrı'nın kulu sayılmasıdır; çoğul kullanım ona bağlı topluluğu da gösterebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Her insan yaratılmışlık ve aitlik bakımından Tanrı'nın kulu sayılabilir."},{"facet_id":"F002","role":"extension","statement":"Çoğul adlandırma, Tanrı'ya bağlı topluluğu veya onun tarafında bulunanları gösterebilir."}],"identity_rationale":"Kaynak ifadesi, özgür ya da köle her insanın yaratılmışlık ve aitlik bakımından Tanrı'nın kulu sayılmasını, ayrıca ona bağlı topluluğu bildirir. Bu kimlik, hukuki kölelikten ve tapınma eyleminden ayrı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"Tanrı'nın kulu"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"Tanrı'nın kulları veya ona bağlı topluluk"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"Tanrı'ya ait sayılan bütün kullar"}],"lexicalization_note":"Yalın insan adlandırması ile Tanrı'ya aitliği bildiren ad öbekleri birlikte bulunur; tanım bu kullanımları birbirine karıştırmadan kapsar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dalın sınırını en açık biçimde hukuki kölelik statüsü ve etkin tapınma davranışıyla yapılan karşılaştırmalar gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bütün insanlara uzanabilen dinsel ve yaratılışsal bir nispet kurar; komşu dal ise insanlar arasındaki somut kölelik statüsünü adlandırır.","focus_only":"Özgür veya köle her insan yaratılmışlık bakımından Tanrı'ya ait sayılabilir.","gloss":"Tanrı'ya kulluk nispeti ve hukuki kölelik","neighbor_only":"Komşu dal yalnızca özgür olmayan ve insanlar arasında mülkiyet konusu sayılan kişiyi anlatır.","neighbor_ref":"root_000973/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir insanın başka bir varlığa ait sayılması düşüncesini paylaşır."},{"boundary_match":"partial","distinction":"Bir insan eylemden bağımsız olarak Tanrı'nın kulu sayılabilir; tapınma dalı ise öznenin boyun eğme ve yönelme davranışını gerektirir.","focus_only":"Odak dal kişinin yaratılmışlık veya bağlılık temelindeki konumunu bildirir.","gloss":"kul sayılma ve tapınma","neighbor_only":"Komşu dal boyun eğerek tapınma ve itaat etme eylemini bildirir.","neighbor_ref":"root_000973/B003","relation_type":"near_neighbor","shared_zone":"İki dal Tanrı ile insan arasındaki bağlılık alanında buluşur."}],"source_phrase_ar":"تفرقة ما بين عباد الله والعبيد المملوكين (maqayis)؛ العبد الإنسان حرا أو رقيقا هو عبد الله (ayn)؛ فادخلي في عبادي أي في حزبي (sihah)؛ عبد بالإيجاد وذلك ليس إلا لله (mufradat)","source_summary":"Kaynaklar, bu nispetin özgür ve köle bütün insanları kapsayabildiğini, yaratılmış olmaya dayandığını ve çoğul kullanımda Tanrı'ya bağlı topluluğu gösterebildiğini bildirir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه إطلاق العبد على الإنسان حرا أو رقيقا منسوبا إلى الله وعلى الخلق عبيدا لله بالإيجاد وعلى جماعة عباد الله أو حزبه","what_is_not_ar":"ليس العبد المملوك بحكم الشرع وحده ولا فعل العبادة نفسه"},"support_links":[]},{"boundary":"Dal hukuki köleliği değil, bir öznenin boyun eğerek itaat veya tapınma göstermesini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000973/B003","candidate_links":[{"candidate_id":"cand_8bb69e263144bebd1b35","lane":"micro"},{"candidate_id":"cand_b64278801ac82d99c5da","lane":"micro"},{"candidate_id":"cand_a19b0a1f12282f0ead07","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَبْد","morph_features":"STEM|POS:N|LEM:Eabod|ROOT:Ebd|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:29:3:1","qac_word_ref":"89:29:3","surface_ar":"عِبَٰدِ"}],"gloss":"boyun eğerek itaat ve tapınma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eylem, sıradan itaati aşan bir boyun eğme ve alçalma tutumu içerir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Merkezî dinsel kullanım, Tanrı'ya yönelen tapınma ve kendini bu yönelişe vermedir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Boyun eğme, özel kullanımlarda bir insana veya sahte tanrısal güce yöneltilebilir."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem davranışsal boyun eğme çekirdeğini hem de dinsel tapınma yönünü birlikte verir.","boundary_detail":"Dal hukuki köleliği değil, bir öznenin boyun eğerek itaat veya tapınma göstermesini anlatır.","branch_image_ar":"العبادة والطاعة الخاضعة","concept_gloss":"boyun eğerek itaat ve tapınma","contextual_glosses":[{"applicability":"Eylemin Tanrı'ya yöneldiği dinsel bağlamlarda en doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsana veya sahte tanrısal güce yönelen özel itaat kullanımlarını dışarıda bırakır.","preserves":"Dinsel yönelişi ve boyun eğerek tapınmayı korur."},"facet_ids":["F001","F002"],"text":"Tanrı'ya tapınmak","usage_role":"contextual"},{"applicability":"Bir insan veya sahte güç karşısındaki alçaltıcı itaati anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tanrı'ya yönelen tapınma ve kendini tapınmaya verme yönünü tek başına taşımaz.","preserves":"Boyun eğme ve itaat çekirdeğini korur."},"facet_ids":["F001","F003"],"text":"boyun eğip itaat etmek","usage_role":"contextual"}],"definition":"Bir varlığa en ileri ölçüde boyun eğerek itaat etmek ve tapınma yönelişi göstermektir; dinsel kullanım Tanrı'ya, bazı özel söz öbekleri ise sahte tanrısal güçlere yönelir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eylem, sıradan itaati aşan bir boyun eğme ve alçalma tutumu içerir."},{"facet_id":"F002","role":"specialization","statement":"Merkezî dinsel kullanım, Tanrı'ya yönelen tapınma ve kendini bu yönelişe vermedir."},{"facet_id":"F003","role":"extension","statement":"Boyun eğme, özel kullanımlarda bir insana veya sahte tanrısal güce yöneltilebilir."}],"identity_rationale":"Kaynak ifadesi, çekirdeği boyun eğmeyle birlikte itaat ve tapınma olarak kurar; Tanrı'ya yönelen kullanım merkezde olsa da bir insana veya sahte tanrısal güce boyun eğme kullanımları da belirtilir. Bu nedenle tapınma, uysal itaat ve en ileri boyun eğme birlikte korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"Tanrı'ya boyun eğerek tapındı"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"boyun eğerek tapınma"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kendini tapınmaya verme"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"sahte tanrısal güce boyun eğip itaat etti"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"sahte tanrısal güçlere veya putlara tapan topluluk"}],"lexicalization_note":"Yalın eylem ve adlar ile belirli nesnelere yönelen söz öbekleri birlikte bulunur; özel nesneli kullanımlar bütün dalın tek sınırı yapılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tapınma ile genel dinsel itaat arasındaki sınırı gösteren iki yakın anlamlı dal en yararlı karşılaştırmaları sağlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın sınırı boyun eğmeyle birlikte itaat üzerinden daha geniştir; komşu dal ise Tanrı'ya yakınlaşma amacı ve dinsel yöneliş üzerinde yoğunlaşır.","focus_only":"Odak dal boyun eğen itaati ve sahte güçlere yönelen özel kullanımları da kapsar.","gloss":"boyun eğerek tapınma ve Tanrı'ya yönelme","neighbor_only":"Komşu dal Tanrı'ya yakınlaşma amacı taşıyan dinsel yönelişi ve bu yönelişteki kişiyi özellikle kapsar.","neighbor_ref":"root_001498/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın merkezinde Tanrı'ya tapınma ve kendini dinsel yönelişe verme bulunur."},{"boundary_match":"partial","distinction":"Odak dal tapınma yönelişini kurucu unsur yapar; komşu dal ise tapınma şartı olmadan dinsel doğrultuda itaat ve görev yerine getirmeye uzanır.","focus_only":"Odak dal tapınma ve boyun eğmenin en ileri derecesini içerir.","gloss":"tapınma ve dinsel itaat","neighbor_only":"Komşu dal dinsel yolda doğru davranmayı ve buyruğu yerine getirmeyi de kapsar.","neighbor_ref":"root_001260/B001","relation_type":"near_synonym","shared_zone":"İki dal dinsel bağlamdaki itaat ve boyun eğme alanını paylaşır."}],"source_phrase_ar":"عبد يعبد عبادة فلا يقال إلا لمن يعبد الله (maqayis;ayn)؛ تعبدت للرجل إذا تذللت له (jamhara)؛ العبادة الطاعة والتعبد التنسك (sihah)؛ إياك نعبد إياك نطيع الطاعة التي نخضع معها (tahdhib)؛ العبودية إظهار التذلل والعبادة غاية التذلل (mufradat)","source_summary":"Kaynaklar tapınmayı boyun eğmeyle birlikte itaat ve en ileri alçalma olarak açıklar; dinsel yöneliş merkezdeyken insanlara veya sahte güçlere yönelen bağımlı kullanımlar da vardır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه عبادة الله والتنسك والطاعة مع الخضوع والتوحيد وعبادة الطاغوت بمعنى طاعته والخضوع لملك أو دنيا","what_is_not_ar":"ليس الرق الشرعي ولا مجرد الانتساب إلى الله بالإيجاد ولا تذليل الطريق أو البعير"},"support_links":["sup_01d456b25c95b81e9f96","sup_75d44d48f421df9e872b","sup_abc1d398ce5770bb7c7a"]},{"boundary":"Anlam insanı köleleştiren veya köle gibi boyunduruk altına alan eylemdir; tapınma ya da nesneleri kullanıma hazırlama değildir.","branch_kind":"bare","branch_ref":"root_000973/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَبْد","morph_features":"STEM|POS:N|LEM:Eabod|ROOT:Ebd|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:29:3:1","qac_word_ref":"89:29:3","surface_ar":"عِبَٰدِ"}],"gloss":"köleleştirmek veya köle gibi boyunduruk altına almak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eyleyen, başka bir insanı köle edinir veya köle durumuna getirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hukuki statü değişmese bile kişiyi köle gibi çalıştıracak ölçüde ezme ve boyunduruk altına alma da kapsama girer."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem gerçek köle edinmeyi hem de özgür kişiyi köle gibi çalıştıracak ölçüde ezmeyi karşılar.","boundary_detail":"Anlam insanı köleleştiren veya köle gibi boyunduruk altına alan eylemdir; tapınma ya da nesneleri kullanıma hazırlama değildir.","branch_image_ar":"التعبيد والاستعباد","concept_gloss":"köleleştirmek veya köle gibi boyunduruk altına almak","contextual_glosses":[{"applicability":"Kişinin gerçekten köle edinildiği veya köle durumuna getirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Özgür kişiyi hukuken köle yapmadan köle gibi boyunduruk altına alma uzantısını belirtmez.","preserves":"Gerçek köle edinme ve statüye sokma eylemini korur."},"facet_ids":["F001"],"text":"köleleştirmek","usage_role":"general"},{"applicability":"Özgür bir kişinin köle gibi boyunduruk altına alındığı bağlamı açıklar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişiyi hukuken köle edinme veya köle statüsüne sokma sonucunu zorunlu kılmaz.","preserves":"Köle gibi boyunduruk altına alma ve çalıştırma yönünü korur."},"facet_ids":["F002"],"text":"köle gibi ezip çalıştırmak","usage_role":"explanatory"}],"definition":"Bir insanı köle edinmek, köle durumuna getirmek ya da özgür olsa bile köle gibi çalışacak ölçüde boyunduruk altına almaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eyleyen, başka bir insanı köle edinir veya köle durumuna getirir."},{"facet_id":"F002","role":"extension","statement":"Hukuki statü değişmese bile kişiyi köle gibi çalıştıracak ölçüde ezme ve boyunduruk altına alma da kapsama girer."}],"identity_rationale":"Kaynak ifadesi bir kişiyi köle edinme, köle durumuna getirme veya özgür olsa bile köle gibi çalışacak ölçüde boyunduruk altına alma eylemlerini ortak bir ettirgen çekirdekte birleştirir. Dal bu eylemi, kişinin mevcut kölelik statüsünden ayrı olarak tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"onu köleleştirdi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"kişiyi ezip köleleştirdi; topluluğu köle edindi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"onu köle durumuna getirdi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"özgür olsa da onu köle gibi boyunduruk altına aldı"}],"lexicalization_note":"Dal yalın eylem anlamını taşır; tanım belirli bir söz öbeğine özgü kapsam eklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel baskı alanıyla ve ortaya çıkan kölelik statüsüyle yapılan iki karşılaştırma eylemin özel sonucunu açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kurucu sonucu köle edinme ya da köle gibi çalıştırmadır; komşu dal bu sonuca varmayan genel baskı ve zorlamaya da uzanır.","focus_only":"Odak dal insanı özellikle köle edinme veya köle gibi çalıştırma sonucuna bağlar.","gloss":"köleleştirme ve zorla boyunduruk altına alma","neighbor_only":"Komşu dal mülkiyetin yanı sıra genel zorlama, aşağılama ve istenmeyen işe sürüklemeyi de kapsar.","neighbor_ref":"root_000504/B004","relation_type":"near_synonym","shared_zone":"İki dal insan üzerinde egemenlik kurma, aşağılama ve mülkiyet alanında önemli ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal süreç ve ettirgen işlemdir; komşu dal ise bu işlemin olası sonucundaki kişiyi ve statüsünü gösterir.","focus_only":"Odak dal bir insanı köle yapan veya köle gibi boyunduruk altına alan eylemi bildirir.","gloss":"köleleştirme eylemi ve köle kişi","neighbor_only":"Komşu dal eylemi değil, kölelik durumunda bulunan kişiyi adlandırır.","neighbor_ref":"root_000973/B001","relation_type":"near_neighbor","shared_zone":"İki dal aynı kölelik ilişkisinin neden olan eylemi ile ortaya çıkan kişi durumunu ele alır."}],"source_phrase_ar":"استعبدت فلانا اتخذته عبدا (maqayis;ayn)؛ عبدت الرجل إذا ذللته وعبدت القوم اتخذتهم عبيدا (jamhara)؛ التعبيد الاستعباد (sihah)؛ عبدت العبيد وأعبدتهم أي صيرتهم عبيدا (tahdhib)؛ عبدت فلانا إذا ذللته وإذا اتخذته عبدا (mufradat)","source_summary":"Kaynaklar eylemi köle edinme, köle durumuna getirme ve kişiyi köle gibi çalışacak ölçüde boyunduruk altına alma yönleriyle ortaklaştırır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه عبدت الرجل واستعبدته وأعبدته وتعبدت فلانا إذا اتخذته عبدا أو صيرته كالعبد أو ذللته حتى يعمل عمل العبد","what_is_not_ar":"ليس العبادة لله ولا الطريق المعبد ولا البعير المعبد"},"support_links":[]},{"boundary":"Tanım yalnızca verilen yol, deve ve gemi yapılarıyla sınırlıdır; insanı köleleştirme anlamına genellenemez.","branch_kind":"mixed_non_bare","branch_ref":"root_000973/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَبْد","morph_features":"STEM|POS:N|LEM:Eabod|ROOT:Ebd|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:29:3:1","qac_word_ref":"89:29:3","surface_ar":"عِبَٰدِ"}],"gloss":"düzleşmiş yol, katranlanmış deve veya kaplanmış gemi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yol kullanımı, sık geçişle basılıp düzleşmiş ve geçişe elverişli hâle gelmiş yolu niteler."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Deve kullanımı, derisi baştan başa katranlanmış ve bununla birlikte uysallaştırılmış hayvanı niteler."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gemi kullanımı, dışı katran, yağ veya benzeri koruyucu maddeyle kaplanmış tekneyi niteler."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Üç yapıdaki ayrı nesne ve işlemleri yalın bir kök anlamına genellemeden birlikte temsil eder.","boundary_detail":"Tanım yalnızca verilen yol, deve ve gemi yapılarıyla sınırlıdır; insanı köleleştirme anlamına genellenemez.","branch_image_ar":"التذليل والتسوية","concept_gloss":"düzleşmiş yol, katranlanmış deve veya kaplanmış gemi","contextual_glosses":[{"applicability":"Nitelemenin yol için kullanıldığı ve sık geçiş sonucu düzleşmeyi anlattığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Devenin katranlanması ile geminin kaplanması kullanımlarını dışarıda bırakır.","preserves":"Yolun basılıp düzleşerek geçişe elverişli olmasını korur."},"facet_ids":["F001"],"text":"çok geçilerek düzleşmiş yol","usage_role":"contextual"},{"applicability":"Nitelemenin derisi bütünüyle katranlanmış ve uysallaştırılmış deve için kullanıldığı yerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Düzleşmiş yol ve kaplanmış gemi kullanımlarını göstermez.","preserves":"Devenin katranla kaplanması ve uysallaştırılması yönünü korur."},"facet_ids":["F002"],"text":"derisi katranlanmış deve","usage_role":"contextual"},{"applicability":"Gemi yüzeyinin katran veya benzeri bir maddeyle kaplandığı kullanımda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yol ve deve kullanımlarını dışarıda bırakır.","preserves":"Geminin koruyucu bir maddeyle kaplanmış olmasını korur."},"facet_ids":["F003"],"text":"katranla kaplanmış gemi","usage_role":"contextual"}],"definition":"Verilen yapılarda yolun çok geçilerek düzleşip kolay kullanılır olması, devenin derisinin katranla kaplanıp uysallaştırılması veya geminin katran, yağ ya da benzeri bir maddeyle kaplanması anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yol kullanımı, sık geçişle basılıp düzleşmiş ve geçişe elverişli hâle gelmiş yolu niteler."},{"facet_id":"F002","role":"source_variant","statement":"Deve kullanımı, derisi baştan başa katranlanmış ve bununla birlikte uysallaştırılmış hayvanı niteler."},{"facet_id":"F003","role":"source_variant","statement":"Gemi kullanımı, dışı katran, yağ veya benzeri koruyucu maddeyle kaplanmış tekneyi niteler."}],"identity_rationale":"Kaynak ifadesi tek bir genel eylemden çok üç yapıya bağlı kullanımı yan yana verir: çok geçilerek düzleşmiş yol, katranlanmış ve uysallaştırılmış deve, katran veya yağla kaplanmış gemi. Dal korunabilir, ancak bu kullanımlar tek bir yalın anlammış gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"çok geçilerek düzleşmiş yol"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"derisi baştan başa katranlanmış ve uysallaştırılmış deve"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"katranla kaplanmış gemi"}],"lexicalization_note":"Dal söz öbeğine bağlı yol ve deve anlamlarıyla bir gemi adlandırmasını birlikte taşır; her kullanım kendi nesnesi ve işlemiyle ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yumuşatma alanı ve aynı kökün insanı köleleştirme dalı, yapıların nesne ve işlem sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız verilen yol, deve ve gemi yapılarına bağlıdır; komşu dal ise nesneyi yumuşatma ve kullanıma hazırlama yönünde daha genel bir kapsama sahiptir.","focus_only":"Odak dal yol dışındaki kullanımlarda devenin veya geminin bir maddeyle kaplanmasını da içerir.","gloss":"basılıp düzleşmiş yol ve genel yumuşatma","neighbor_only":"Komşu dal yer, döşek, oturak, hayvan ve insan için genel yumuşatma ve kolaylaştırmaya uzanır.","neighbor_ref":"root_001659/B002","relation_type":"near_neighbor","shared_zone":"İki dal yol veya başka bir yüzeyin kullanıma elverişli ve kolay hâle gelmesi alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dalın belirlenmiş nesneleri yol, deve ve gemidir; insan üzerinde mülkiyet ve zor kullanma sonucu kuran anlam yalnız komşu daldadır.","focus_only":"Odak dal yolun düzleşmesini ve hayvan ya da geminin yüzeyinin işlenmesini anlatır.","gloss":"nesneyi kullanıma hazırlama ve insanı köleleştirme","neighbor_only":"Komşu dal bir insanı köle edinme veya köle gibi boyunduruk altına alma eylemidir.","neighbor_ref":"root_000973/B004","relation_type":"near_neighbor","shared_zone":"İki dalda da bir varlığı denetim veya kullanım için elverişli hâle getirme çağrışımı bulunur."}],"source_phrase_ar":"الطريق المعبد وهو المسلوك المذلل (maqayis)؛ طريق معبد أي مذلل (jamhara;mufradat)؛ البعير المعبد المهنوء بالقطران المذلل (maqayis;sihah)؛ المعبدة السفينة المقيرة (sihah;tahdhib)؛ المعبد من الإبل الذي عم جلده بالقطران (tahdhib)","source_summary":"Toplu kaynak ifadesi, yol için basılıp düzleşmeyi; deve için katranlanma ve uysallaşmayı; gemi içinse katran ya da yağla kaplanmayı ayrı gerçekleşmeler olarak verir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الطريق المعبد المسلوك المذلل والبعير أو الجمل المعبد المهنوء بالقطران والسفينة المعبدة المقيرة","what_is_not_ar":"ليس استعباد الإنسان ولا العبادة ولا التكريم"},"support_links":[]},{"boundary":"Dal, saygı ve hizmet gören kişiyi niteler; alçaltma, köleleştirme veya nesneyi işleme anlamı taşımaz.","branch_kind":"bare","branch_ref":"root_000973/B006","candidate_links":[{"candidate_id":"cand_f9427fd9b198285eba55","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَبْد","morph_features":"STEM|POS:N|LEM:Eabod|ROOT:Ebd|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:29:3:1","qac_word_ref":"89:29:3","surface_ar":"عِبَٰدِ"}],"gloss":"saygı gösterilip hizmet edilen kişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi çevresindekilerce saygıdeğer ve yüce tutulur."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu yüksek konumun sonucu olarak kişiye hizmet edilir."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin hem yüce tutulmasını hem de bu konum nedeniyle hizmet görmesini birlikte karşılar.","boundary_detail":"Dal, saygı ve hizmet gören kişiyi niteler; alçaltma, köleleştirme veya nesneyi işleme anlamı taşımaz.","branch_image_ar":"التكريم والتعظيم","concept_gloss":"saygı gösterilip hizmet edilen kişi","contextual_glosses":[{"applicability":"Bir kişinin yüksek saygınlığı ile kendisine sunulan hizmet birlikte vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yüceltilme ve hizmet görme yönlerini birlikte korur."},"facet_ids":["F001","F002"],"text":"yüceltilip hizmet edilen","usage_role":"contextual"}],"definition":"Kendisine saygı gösterilen, yüceltilen ve hizmet edilen kişidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi çevresindekilerce saygıdeğer ve yüce tutulur."},{"facet_id":"F002","role":"associated_use","statement":"Bu yüksek konumun sonucu olarak kişiye hizmet edilir."}],"identity_rationale":"Kaynak ifadesi nitelenen kişinin saygı gösterilen, yüceltilen ve hizmet edilen biri olduğunu açıkça belirtir. Bu anlam, benzer biçimin ezilmiş veya kullanıma hazırlanmış nesneyi nitelediği daldan karşıt bir değerle ayrılır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"saygı gösterilen, yüceltilen ve hizmet edilen kişi"}],"lexicalization_note":"Dal yalın bir niteleme anlamıdır; özel bir söz öbeğine bağlı ek kapsam gerektirmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yüksek değer kazanma ve sözle yüceltme dalları, kişi niteliği ile ettirgen eylem arasındaki sınırı gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yüksek tutulup hizmet edilen kişiyi niteler; komşu dal ise bir kişi, anı veya makamı yükseltme eylemini daha geniş kapsamda anlatır.","focus_only":"Odak dal kişinin saygı görmesi yanında kendisine hizmet edilmesini de içerir.","gloss":"saygı gören kişi ve değerini yükseltme","neighbor_only":"Komşu dal bir kişinin, anının veya makamın değerini yükseltme eylemine uzanır.","neighbor_ref":"root_000582/B002","relation_type":"near_synonym","shared_zone":"İki dal kişi veya makamın yüksek değer ve saygınlık kazanması alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal bir kişinin niteliği ve gördüğü muameledir; komşu dal ise övgü sözleriyle yüceltme eylemidir.","focus_only":"Odak dal kişinin saygın konumunu ve gördüğü hizmeti bildirir.","gloss":"saygın kişi ve sözle yüceltme","neighbor_only":"Komşu dal güzel nitelikleri sözle anıp yücelik yükleme eylemini bildirir.","neighbor_ref":"root_001398/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal birini yüksek ve değerli gösterme alanına bağlıdır."}],"source_phrase_ar":"المعبد المكرم والمعظم كأنه يعبد (jamhara)؛ المعبد أي معظما مخدوما (tahdhib)","source_summary":"Kaynaklar nitelemeyi saygı görme, yüceltilme ve hizmet edilme özelliklerini bir arada taşıyan kişi için kullanır.","sources":["JA","TA"],"what_is_ar":"يدخل فيه المعبد بمعنى المكرم والمعظم والمخدوم","what_is_not_ar":"ليس المعبد المذلل ولا الطريق الموطوء ولا البعير المطلي بالقطران"},"support_links":["sup_25fc6d9bc5a8de9d221a"]},{"boundary":"Dal fiziksel güç, sağlamlık ve dayanıklılığı anlatır; toplumsal kölelik ya da duygusal öfke anlamı taşımaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000973/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَبْد","morph_features":"STEM|POS:N|LEM:Eabod|ROOT:Ebd|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:29:3:1","qac_word_ref":"89:29:3","surface_ar":"عِبَٰدِ"}],"gloss":"güç, sağlamlık ve dayanıklılık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel nitelik fiziksel güç ve sağlamlıktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kumaş bağlamında güç, kullanıma karşı dayanma ve kalıcılık olarak görünür."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dişi deve bağlamında güçlü yapıya semizlik de eklenir."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın niteliği, kumaştaki kalıcılığı ve devedeki güçlü yapıyı ortak çekirdekte karşılar.","boundary_detail":"Dal fiziksel güç, sağlamlık ve dayanıklılığı anlatır; toplumsal kölelik ya da duygusal öfke anlamı taşımaz.","branch_image_ar":"القوة والصلابة","concept_gloss":"güç, sağlamlık ve dayanıklılık","contextual_glosses":[{"applicability":"Niteliğin dişi deve için kullanıldığı ve güçle semizliğin birlikte anlatıldığı bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kumaşın dayanıklılığını ve yalın sağlamlık adını göstermez.","preserves":"Canlıdaki güçlü yapı ve semizlik görünümünü korur."},"facet_ids":["F001","F003"],"text":"güçlü ve semiz dişi deve","usage_role":"contextual"},{"applicability":"Bir kumaşın kullanım ve zaman karşısındaki gücünün sorgulandığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dişi deveye özgü güç ve semizlik görünümünü dışarıda bırakır.","preserves":"Gücün kalıcılık ve dayanma yönünü korur."},"facet_ids":["F001","F002"],"text":"kumaşın dayanıklılığı","usage_role":"contextual"}],"definition":"Bir varlığın güçlü, sağlam ve zaman içinde dayanıklı olmasıdır; dişi deve bağlamında bu sağlamlığa semizlik de eşlik eder.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel nitelik fiziksel güç ve sağlamlıktır."},{"facet_id":"F002","role":"extension","statement":"Kumaş bağlamında güç, kullanıma karşı dayanma ve kalıcılık olarak görünür."},{"facet_id":"F003","role":"specialization","statement":"Dişi deve bağlamında güçlü yapıya semizlik de eklenir."}],"identity_rationale":"Kaynak ifadesi çekirdeği güç ve sağlamlık olarak verir; dayanıklılık ve kalıcılık bunun zaman içindeki görünümü, dişi devedeki semizlik ise canlıya özgü belirti olarak sunulur. Bunlar kölelik veya boyun eğmeyle ilişkili değildir.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"güç, sağlamlık ve dayanıklılık"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"güçlü ve semiz dişi deve"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kumaşının hiç dayanıklılığı yok"}],"lexicalization_note":"Yalın güç adı ile deve ve kumaşa bağlı söz öbekleri birlikte bulunur; canlıya özgü semizlik bütün dalın genel anlamı yapılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; geniş güç alanı ve sert nesne niteliği, bu dalın dayanıklılık ile özel deve ve kumaş sınırını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal nesnenin veya hayvanın dayanıklı yapısıyla sınırlıdır; komşu dal ruhsal cesaretten zorlu koşullara kadar çok daha geniş bir güç alanı kurar.","focus_only":"Odak dal kumaşın kalıcılığına ve dişi devenin semiz gücüne bağlı özel kullanımları içerir.","gloss":"dayanıklı sağlamlık ve geniş güç alanı","neighbor_only":"Komşu dal cesaret, yürek sağlamlığı, zorlu durum, çaba ve acı gibi daha geniş güç ve şiddet alanlarına uzanır.","neighbor_ref":"root_000782/B002","relation_type":"near_synonym","shared_zone":"İki dal fiziksel güç, sertlik ve sağlamlık çekirdeğinde belirgin biçimde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal süre boyunca dayanmayı ve özel bağlamsal görünümleri kapsar; komşu dal doğrudan sert veya güçlü nesne niteliğidir.","focus_only":"Odak dal güçle birlikte dayanıklılık ve kalıcılığı, deve bağlamında semizliği içerir.","gloss":"dayanıklılık ve sert nesne","neighbor_only":"Komşu dal tek bir şeyi sert, güçlü veya kimi aktarımda uzun diye niteler.","neighbor_ref":"root_000188/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal somut bir varlığın güçlü ve sağlam oluşunu anlatabilir."}],"source_phrase_ar":"العبدة وهي القوة والصلابة (maqayis)؛ ناقة ذات عبدة أي ذات قوة وسمن وما لثوبك عبدة أي قوة (sihah)؛ العبدة البقاء وقيل الشدة (tahdhib)","source_summary":"Kaynaklar güç ve sağlamlık çekirdeğinde birleşir; bunu kumaşın dayanması ve dişi devenin güçlü, semiz yapısı üzerinden somutlaştırır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه العبدة بمعنى القوة والصلابة والشدة والبقاء والسمن في الناقة وقوة الثوب","what_is_not_ar":"ليس الذل والرق ولا الأنفة والغضب"},"support_links":[]},{"boundary":"Dal incinmiş gururdan yükselen öfke ile kederli iç duygulanımı kapsar; güç ve sağlamlık anlamından ayrıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000973/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَبْد","morph_features":"STEM|POS:N|LEM:Eabod|ROOT:Ebd|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:29:3:1","qac_word_ref":"89:29:3","surface_ar":"عِبَٰدِ"}],"gloss":"incinmiş gurur, öfke veya kederli iç duygulanım","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Duygu incinmiş gurur, onurunu koruma isteği ve öfke çevresinde oluşur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynak ifadesi anlamı keder ve yoğun iç sıkıntısına da uzatır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özel söz öbeğinde gururu incinen kişinin tepkisi susmak olur."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gurur ve öfke çekirdeğiyle kaynakta verilen kederli iç duygulanım uzantısını birlikte karşılar.","boundary_detail":"Dal incinmiş gururdan yükselen öfke ile kederli iç duygulanımı kapsar; güç ve sağlamlık anlamından ayrıdır.","branch_image_ar":"الأنفة والغضب","concept_gloss":"incinmiş gurur, öfke veya kederli iç duygulanım","contextual_glosses":[{"applicability":"Onur kırılmasının öfke ve kendini koruma tepkisi doğurduğu bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Keder ve yoğun iç sıkıntısı uzantısını tek başına göstermez.","preserves":"İncinmiş gurur ve öfke çekirdeğini korur."},"facet_ids":["F001"],"text":"gururu incinip öfkelenmek","usage_role":"contextual"},{"applicability":"İncinme tepkisinin susma olarak gerçekleştiği özel söz bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel öfke ve keder alanının tamamını kapsamaz.","preserves":"Gurur incinmesini ve bunun sonucundaki susmayı korur."},"facet_ids":["F001","F003"],"text":"gururu incindiği için sustu","usage_role":"contextual"}],"definition":"İncinmiş gurur ve kendini koruma duygusuyla yükselen öfke ya da içe çöken kederli duygulanımdır; özel kullanımda kişi bu incinme yüzünden susar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Duygu incinmiş gurur, onurunu koruma isteği ve öfke çevresinde oluşur."},{"facet_id":"F002","role":"extension","statement":"Kaynak ifadesi anlamı keder ve yoğun iç sıkıntısına da uzatır."},{"facet_id":"F003","role":"example","statement":"Özel söz öbeğinde gururu incinen kişinin tepkisi susmak olur."}],"identity_rationale":"Kaynak ifadesi incinmiş gurur, öfke ve kendini koruma duygusunu merkezde verir; ayrıca keder ve yoğun iç duygulanımı aktarır. Geçici çerçevedeki kaçırılmış şey için pişmanlık ayrıntısı kaynak cümlesinde açık değildir, bu yüzden tanım bu ek koşula bağlanmadan kurulmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"incinmiş gurur, öfke, keder veya iç sıkıntısı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"gururu incindiği için sustu"}],"lexicalization_note":"Yalın duygu adı ile gururu incindiği için susmayı anlatan söz öbeği birlikte bulunur; susma yalnız özel kullanımın sonucudur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; öfke ve onur çekirdeğine en yakın dal ile daha geniş duygulanım dalı, keder uzantısının sınırını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kaynak aktarımında kedere ve iç sıkıntısına açılır; komşu dalın merkezi daha sıkı biçimde gurur ve kızgınlıktır.","focus_only":"Odak dal öfkenin yanı sıra keder ve yoğun iç duygulanımı da kapsar.","gloss":"incinmiş gurur ve kabaran öfke","neighbor_only":"Komşu dal burunla ilişkilendirilen kendini koruma gururunu ve içte kabaran kızgınlığı özellikle vurgular.","neighbor_ref":"root_000358/B003","relation_type":"near_synonym","shared_zone":"İki dal incinmiş onur, kendini koruma duygusu ve öfke alanında büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dalın duygusal çekirdeği onur ve öfkeyle sınırlanır; komşu dal sevgiye ve özleme de uzanan daha genel bir duygulanım alanıdır.","focus_only":"Odak dal kederi incinmiş gurur ve öfke alanıyla birlikte taşır.","gloss":"gururlu öfke ve duygusal keder","neighbor_only":"Komşu dal kederin yanında sevgi, özlem ve başka duygusal yönelimleri de kapsar.","neighbor_ref":"root_001626/B004","relation_type":"near_neighbor","shared_zone":"İki dal yoğun iç duygulanım ve keder alanında kesişir."}],"source_phrase_ar":"العبد مثل الأنف والحمية (maqayis)؛ العبد الأنفة وعبدت فصمت أي أنفت فسكت (jamhara)؛ العبد بالتحريك الغضب والأنف والاسم العبدة (sihah)؛ العبد الأنف والحمية ويقال عبد عليه أي غضب والعبد الحزن والوجد (tahdhib)","source_summary":"Kaynaklar incinmiş gurur, öfke ve kendini koruma duygusunu ortak çekirdek yapar; bazı aktarımlar keder ve yoğun iç duygulanımı da aynı ad altında verir.","sources":["MQ","JA","SI","TA"],"what_is_ar":"يدخل فيه العبد والعبدة بمعنى الأنفة والحمية والغضب والحزن والوجد والندم عند فوات الشيء","what_is_not_ar":"ليس العبادة والطاعة الخاضعة ولا القوة والصلابة"},"support_links":[]},{"boundary":"Dal yalnız verilen iki söz öbeğinde gecikmeme veya biraz hızlanma bildirir; genel bir hız kökü gibi yorumlanmaz.","branch_kind":"collocation","branch_ref":"root_000973/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَبْد","morph_features":"STEM|POS:N|LEM:Eabod|ROOT:Ebd|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:29:3:1","qac_word_ref":"89:29:3","surface_ar":"عِبَٰدِ"}],"gloss":"gecikmeden yapmak veya koşuda biraz hızlanmak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İlk yapı, belirtilen işi yapmak için beklememeyi ve kısa sürede harekete geçmeyi bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İkinci yapı, koşunun hızını bir miktar artırmayı bildirir."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki yapıdaki farklı eylemleri yapı sınırlarını koruyarak birlikte temsil eder.","boundary_detail":"Dal yalnız verilen iki söz öbeğinde gecikmeme veya biraz hızlanma bildirir; genel bir hız kökü gibi yorumlanmaz.","branch_image_ar":"قلة اللبث وسرعة العدو","concept_gloss":"gecikmeden yapmak veya koşuda biraz hızlanmak","contextual_glosses":[{"applicability":"Bir kişinin belirtilen işi beklemeden gerçekleştirdiğini bildiren yapı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Koşuda biraz hızlanma okumasını dışarıda bırakır.","preserves":"İşi yapmak için oyalanmama ve gecikmeme yönünü korur."},"facet_ids":["F001"],"text":"yapmakta gecikmedi","usage_role":"contextual"},{"applicability":"Koşunun bir miktar hızlandığını anlatan yapı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir işi yapmakta gecikmeme okumasını dışarıda bırakır.","preserves":"Koşuda sınırlı hız artışı yönünü korur."},"facet_ids":["F002"],"text":"koşarken biraz hızlandı","usage_role":"contextual"}],"definition":"Verilen bir söz öbeğinde bir işi yapmakta hiç gecikmemeyi, diğerinde ise koşarken bir ölçü hızlanmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İlk yapı, belirtilen işi yapmak için beklememeyi ve kısa sürede harekete geçmeyi bildirir."},{"facet_id":"F002","role":"source_variant","statement":"İkinci yapı, koşunun hızını bir miktar artırmayı bildirir."}],"identity_rationale":"Kaynak ifadesi iki ayrı söz öbeğine bağlı anlam verir: bir işi yapmakta gecikmemek ve koşarken bir ölçü hızlanmak. Bunlar tek bir yalın eylem anlamına indirgenemez, fakat dal iki yapı açıkça ayrılarak korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"yapmakta gecikmedi"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"koşarken biraz hızlandı"}],"lexicalization_note":"Bütün anlam söz öbeklerine bağlıdır; gecikmeme ve koşuda biraz hızlanma okumaları yalın biçime genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hızlanma yönünü aynı ölçülülükle veren komşu, söz öbeğine bağlı kapsamı açıklayan en keskin karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Hızlanma yönü bakımından yakındırlar, ancak odak dal iki özel yapıya bağlıdır ve ayrıca gecikmeme anlamı taşır; komşu dal doğrudan hızlı hareket alanındadır.","focus_only":"Odak dal hızlanma yapısının yanında bir işi yapmakta gecikmeme yapısını da içerir.","gloss":"biraz hızlanma ve hızlı hareket","neighbor_only":"Komşu dal hızlı geçip gitme kullanımını da doğrudan hareket hızı alanında taşır.","neighbor_ref":"root_001445/B008","relation_type":"near_synonym","shared_zone":"İki dal koşuda veya geçişte belirli ölçüde hız kazanmayı anlatır."}],"source_phrase_ar":"ما عبد أن فعل ذاك أي ما لبث (sihah;tahdhib)؛ عبد يعدو إذا أسرع بعض الإسراع (tahdhib)","source_summary":"Toplu kaynak ifadesi, gecikmeden yapma ile koşuda biraz hızlanma okumalarını iki ayrı yapıya bağlar; ortak bir yalın anlam ileri sürmez.","sources":["SI","TA"],"what_is_ar":"يدخل فيه ما عبد أن فعل أي ما لبث وعبد يعدو إذا أسرع بعض الإسراع","what_is_not_ar":"ليس العبادة ولا الغضب ولا العطب"},"support_links":[]},{"boundary":"Dal insan, nesne veya yolların ayrı yönlere dağılmışlığını bildirir; kölelerin çoğul adı değildir.","branch_kind":"bare","branch_ref":"root_000973/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَبْد","morph_features":"STEM|POS:N|LEM:Eabod|ROOT:Ebd|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:29:3:1","qac_word_ref":"89:29:3","surface_ar":"عِبَٰدِ"}],"gloss":"her yana dağılmış kümeler, nesneler veya yollar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birlik oluşturan öğeler birbirinden ayrılır ve değişik yönlere dağılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dağılmış öğeler insan kümeleri, nesneler, uzak uçlar veya farklı yollar olabilir."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dağılma yönünü ve kaynakta sayılan insan, nesne ve yol türlerini birlikte karşılar.","boundary_detail":"Dal insan, nesne veya yolların ayrı yönlere dağılmışlığını bildirir; kölelerin çoğul adı değildir.","branch_image_ar":"التفرق في الوجوه","concept_gloss":"her yana dağılmış kümeler, nesneler veya yollar","contextual_glosses":[{"applicability":"Adlandırmanın farklı yönlere gitmiş insan grupları için kullanıldığı bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesneler, uzak uçlar ve farklı yollar için kullanımı göstermez.","preserves":"İnsan kümelerinin birbirinden ayrılarak her yana gitmesini korur."},"facet_ids":["F001","F002"],"text":"her yöne dağılmış insan kümeleri","usage_role":"contextual"},{"applicability":"Adlandırmanın çeşitli yönlere uzanan yolları gösterdiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan kümeleri ve dağınık nesneler için kullanımı dışarıda bırakır.","preserves":"Yolların birbirinden ayrılıp farklı yönlere uzanmasını korur."},"facet_ids":["F001","F002"],"text":"birbirinden ayrılan farklı yollar","usage_role":"contextual"}],"definition":"İnsan kümelerinin, nesnelerin, uzak uçların veya yolların birbirinden ayrılarak çeşitli yönlere dağılmış olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birlik oluşturan öğeler birbirinden ayrılır ve değişik yönlere dağılır."},{"facet_id":"F002","role":"extension","statement":"Dağılmış öğeler insan kümeleri, nesneler, uzak uçlar veya farklı yollar olabilir."}],"identity_rationale":"Kaynak ifadesi insan kümeleri, nesneler, uzak uçlar ve farklı yollar için ortak olarak birbirinden ayrılıp çeşitli yönlere dağılma görüntüsünü verir. Bunlar köle adının çoğulları değil, dağınıklığı anlatan ayrı adlandırmalardır.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"her yana dağılmış insan kümeleri, nesneler veya yollar"}],"lexicalization_note":"Dal yalın bir çoğul adlandırmadır; özel bir söz öbeğinden alınmış ek kapsam içermez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel olarak her yöne dağılan topluluk ile daha geniş ayrışma dalı, bu adlandırmanın sonuç ve kapsam sınırını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sonuçtaki dağınık kümeleri ve insan dışı öğeleri adlandırabilir; komşu dal topluluğun dağılma olayına bağlı özel bir anlatımdır.","focus_only":"Odak dal insan kümeleri yanında nesneleri, uzak uçları ve farklı yolları da adlandırır.","gloss":"her yana dağılmış öğeler ve dağılan topluluk","neighbor_only":"Komşu dal belirli bir kalıp içinde bir topluluğun her yöne gitme olayını anlatır.","neighbor_ref":"root_000231/B006","relation_type":"near_synonym","shared_zone":"İki dal insanların her yönde birbirinden ayrılıp dağılması görüntüsünde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal yönlere yayılmış insan, nesne ve yolların durumudur; komşu dal ettirgen dağıtmadan soyut farklılaşmaya kadar daha geniştir.","focus_only":"Odak dal uzak uçlar ve farklı yönlere uzanan yollar gibi somut dağınık öğeleri özellikle kapsar.","gloss":"yönlere dağılmışlık ve genel ayrışma","neighbor_only":"Komşu dal topluluğu dağıtma eylemine, türlerin ve gönüllerin farklılaşmasına kadar uzanır.","neighbor_ref":"root_000775/B001","relation_type":"near_synonym","shared_zone":"İki dal bir bütünün parçalarının ayrılması ve dağılması alanını paylaşır."}],"source_phrase_ar":"العباديد الفرق من الناس الذاهبون في كل وجه وكذلك العبابيد (sihah)؛ العباديد والعبابيد الأطراف البعيدة والأشياء المتفرقة والطرق المختلفة (tahdhib)","source_summary":"Kaynaklar ortak biçimde her yana dağılma ve birbirinden uzaklaşma görüntüsünü verir; kapsam insan topluluklarından nesnelere ve yollara kadar uzanır.","sources":["SI","TA"],"what_is_ar":"يدخل فيه العباديد والعبابيد للفرق من الناس أو الأشياء أو الطرق المتفرقة الذاهبة في كل وجه","what_is_not_ar":"ليس جمع العبد المملوك ولا أسماء القبائل"},"support_links":[]},{"boundary":"Dal bineğe bağlı yolda kalma ve güçlükle direnen deve kullanımlarıyla sınırlıdır; genel yorgunluk veya nesneyi uysallaştırma anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000973/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَبْد","morph_features":"STEM|POS:N|LEM:Eabod|ROOT:Ebd|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:29:3:1","qac_word_ref":"89:29:3","surface_ar":"عِبَٰدِ"}],"gloss":"bineği yüzünden yolda kalma veya güçlükle direnen deve","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yolcunun ilerleyememesi, bineğinin yorulması, zarar görmesi veya ortadan kaybolması sonucudur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Deve nitelemesi, hayvanın insanlara karşı güçlükle direnip kolayca boyun eğmemesini bildirir."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yolcu sonucunu ve deve niteliğini iki yapı sınırını koruyarak birlikte temsil eder.","boundary_detail":"Dal bineğe bağlı yolda kalma ve güçlükle direnen deve kullanımlarıyla sınırlıdır; genel yorgunluk veya nesneyi uysallaştırma anlamı değildir.","branch_image_ar":"العطب والانقطاع","concept_gloss":"bineği yüzünden yolda kalma veya güçlükle direnen deve","contextual_glosses":[{"applicability":"Bineğin yorulması, zarar görmesi veya kaybı yüzünden yolculuğun kesildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsanlara güçlük çıkararak direnen deve nitelemesini dışarıda bırakır.","preserves":"Binek kaynaklı ilerleyememe ve yolda kalma sonucunu korur."},"facet_ids":["F001"],"text":"bineği elden çıkınca yolda kaldı","usage_role":"contextual"},{"applicability":"Hayvanın insanlara karşı dirençli ve kolay yönetilemez oluşunu bildiren yapıda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Binek kaybı veya tükenmesi yüzünden yolda kalma olayını göstermez.","preserves":"Devenin güçlük çıkarma ve direnme niteliğini korur."},"facet_ids":["F002"],"text":"insanlara güçlükle direnen deve","usage_role":"contextual"}],"definition":"Bir yapıda yolcunun bineği yorulduğu, zarar gördüğü veya elden çıktığı için yolda kalması; diğerinde ise devenin insanlara güçlük çıkararak direnmesi anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yolcunun ilerleyememesi, bineğinin yorulması, zarar görmesi veya ortadan kaybolması sonucudur."},{"facet_id":"F002","role":"source_variant","statement":"Deve nitelemesi, hayvanın insanlara karşı güçlükle direnip kolayca boyun eğmemesini bildirir."}],"identity_rationale":"Kaynak ifadesi, yolcunun bineği yorulduğu, zarar gördüğü veya ortadan kaybolduğu için yolda kalmasını anlatan yapı ile insanlara güçlük çıkararak direnen deve nitelemesini birlikte verir. Bu iki kullanım aynı dalda tutulabilir, ancak genel bir bozulma veya yorgunluk anlamı gibi birleştirilemez.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"bineği yorulduğu, zarar gördüğü veya kaybolduğu için yolda kaldı"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"insanlara güçlük çıkararak direnen deve"}],"lexicalization_note":"Yolda kalmayı anlatan kalıpla güç deve nitelemesi birlikte bulunur; iki yapı kendi katılımcıları ve sonuçlarıyla ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel binek tükenmesi ile geride kalan yorgun binek dalları, yolcu sonucu ve dirençli deve uzantısının sınırını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli yapıda binek kaybı sonucunu ve güç deveyi taşır; komşu dal yorgunluk, arıza ve soyut yetersizlikleri daha geniş kapsamda anlatır.","focus_only":"Odak dal ayrıca insanlara güçlük çıkararak direnen deve nitelemesini içerir.","gloss":"binek yüzünden yolda kalma ve genel tükenme","neighbor_only":"Komşu dal bineğin topallaması, zayıflaması ve çeşitli soyut yetersizlikler gibi daha geniş kesilme alanlarına uzanır.","neighbor_ref":"root_000094/B004","relation_type":"near_synonym","shared_zone":"İki dal bineğin yorulması veya zarar görmesi yüzünden yolculuğun kesilmesinde belirgin biçimde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal yolcunun yolda kalmasına odaklanır ve kayıp ile dirençli deveyi de içerir; komşu dal doğrudan bineklerin geride kalma durumudur.","focus_only":"Odak dal bineğin kaybolması veya zarar görmesini ve ayrı bir dirençli deve nitelemesini de kapsar.","gloss":"yolda kalma ve geride kalan yorgun binek","neighbor_only":"Komşu dal yorgun bineklerin geride kalması ve sürüye yetişememesi sonucunu özellikle bildirir.","neighbor_ref":"root_000520/B006","relation_type":"near_neighbor","shared_zone":"İki dal yorgunluk nedeniyle bineğin ilerleyememesi alanında kesişir."}],"source_phrase_ar":"أعبد بفلان بمعنى أبدع به إذا كلت راحلته أو عطبت (sihah)؛ أعبد به إذا ذهبت راحلته وكذلك أبدع به (tahdhib)؛ بعير متعبد ومتأبد إذا امتنع على الناس صعوبة (tahdhib)","source_summary":"Toplu kaynak ifadesi, bineğin yorulması, zarar görmesi veya kaybıyla yolculuğun kesilmesini; ayrıca insanlara güçlük çıkaran dirençli deveyi ayrı yapılarda aktarır.","sources":["SI","TA"],"what_is_ar":"يدخل فيه أعبد بفلان أو أعبد به بمعنى أبدع به إذا كلت راحلته أو عطبت أو ذهبت ويدخل فيه البعير المتعبد الممتنع صعوبة","what_is_not_ar":"ليس التعبيد بمعنى التذليل ولا عبد يعدو بمعنى أسرع"},"support_links":[]},{"boundary":"Dal güzel koku hazırlamada kullanılan ezme aracını adlandırır; koku maddesinin kendisini, kokuyu veya güç niteliğini bildirmez.","branch_kind":"bare","branch_ref":"root_000973/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَبْد","morph_features":"STEM|POS:N|LEM:Eabod|ROOT:Ebd|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:29:3:1","qac_word_ref":"89:29:3","surface_ar":"عِبَٰدِ"}],"gloss":"güzel koku maddesi ezme taşı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Araç, güzel koku maddelerini ezme ve hazırlama işinde kullanılır."}}],"root_ar":"ع ب د","root_id":"root_000973","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Aracın biçiminden çok güzel koku hazırlamadaki ezme işlevini açık ve doğal biçimde belirtir.","boundary_detail":"Dal güzel koku hazırlamada kullanılan ezme aracını adlandırır; koku maddesinin kendisini, kokuyu veya güç niteliğini bildirmez.","branch_image_ar":"صَلاءة الطيب","concept_gloss":"güzel koku maddesi ezme taşı","contextual_glosses":[{"applicability":"Güzel koku maddelerinin ezilip karıştırıldığı araç bağlamında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Koku maddelerini ezme ve hazırlama işlevini araç niteliğiyle birlikte korur."},"facet_ids":["F001"],"text":"koku hazırlama havanı","usage_role":"contextual"}],"definition":"Güzel koku maddelerinin ezilip karıştırılarak hazırlanmasında kullanılan taş ya da havandır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Araç, güzel koku maddelerini ezme ve hazırlama işinde kullanılır."}],"identity_rationale":"Tek kaynak ifadesi sözcüğü güzel koku maddelerinin ezilip hazırlanmasında kullanılan taş veya havan olarak adlandırır. Bu araç anlamı, aynı biçimin güç ve duygulanım dallarından bütünüyle ayrıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"güzel koku maddelerini ezme taşı"}],"lexicalization_note":"Dal yalın bir araç adıdır; özel bir söz öbeğine bağlı ek anlam taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; koku maddeleri ile tütsü odunu ve kabı, ezme aracının aynı alandaki farklı işlevini en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal işleme aracıdır; komşu dal ise o araçla işlenebilecek kokulu maddeler ve karışım bileşenleridir.","focus_only":"Odak dal güzel koku maddelerini ezip hazırlamaya yarayan aracı adlandırır.","gloss":"koku hazırlama aracı ve koku maddeleri","neighbor_only":"Komşu dal güzel koku karışımına giren maddeleri ve kokulu malzemeleri adlandırır.","neighbor_ref":"root_001190/B005","relation_type":"same_field","shared_zone":"İki dal güzel koku hazırlama işi ve bu işte kullanılan nesneler alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal ezme ve karıştırma aşamasına aittir; komşu dal kokulu odunun yakılması ve dumanının çıkarılması aşamasına aittir.","focus_only":"Odak dal koku maddelerini ezmeye yarayan taş veya havandır.","gloss":"koku ezme taşı ve tütsü aracı","neighbor_only":"Komşu dal yakılan güzel kokulu odunu ve onun konduğu tütsü kabını kapsar.","neighbor_ref":"root_001238/B007","relation_type":"same_field","shared_zone":"İki dal kokulu madde hazırlama veya kullanma araçları çevresinde yer alır."}],"source_phrase_ar":"العبدة صلاءة الطيب (jamhara)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu adlandırma yalnız bir kaynakta, güzel koku maddelerini ezmeye yarayan araç anlamıyla aktarılır."}],"source_summary":"Tek kaynak aktarımı, sözcüğü güzel koku maddelerinin hazırlanmasında kullanılan ezme taşı veya havan olarak verir.","sources":["JA"],"what_is_ar":"يدخل فيه العبدة اسما لصَلاءة الطيب","what_is_not_ar":"ليس العبدة بمعنى القوة ولا الأنفة"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["89:29:1"],"branch_refs":[],"candidate_id":"cand_5042fdfb1786003a3cbe","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:29:1:prefixed-compression","source_type":"word_analysis","support_ids":["sup_003f050e25841561616f","sup_2b18bef72843cb95a9f4"],"title":"prefixed command compression","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:1","qac_refs":["89:29:1:1"],"status":"accepted"}},{"anchor_refs":["89:29:1"],"branch_refs":[],"candidate_id":"cand_7e16a8edae70f9b42a00","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:29:1:resultive-command-sequence","source_type":"word_analysis","support_ids":["sup_003f050e25841561616f","sup_b6340deae2518a1486cf"],"title":"resultive command sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:1","qac_refs":["89:29:1:1"],"status":"accepted"}},{"anchor_refs":["89:29:1"],"branch_refs":[],"candidate_id":"cand_a811343ab8ee2ee13c5b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:29:1:return-to-incorporation","source_type":"word_analysis","support_ids":["sup_003f050e25841561616f","sup_3f2d80c4967198537eae"],"title":"return becomes incorporation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:1","qac_refs":["89:29:1:1"],"status":"accepted"}},{"anchor_refs":["89:29:2"],"branch_refs":[],"candidate_id":"cand_409ec1a75f18c4c805c3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000464"],"scope":"focus_ayah","source_local_id":"89:29:2:completed-entry-frame","source_type":"word_analysis","support_ids":["sup_603fee0c793a0afae6f6","sup_6cc96ff57d50edccfd82"],"title":"completed entry frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:2","qac_refs":["89:29:1:2","89:29:1:3"],"status":"accepted"}},{"anchor_refs":["89:29:2"],"branch_refs":[],"candidate_id":"cand_cc1fd5568cc7bff44690","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000464"],"scope":"focus_ayah","source_local_id":"89:29:2:direct-form-not-causative","source_type":"word_analysis","support_ids":["sup_603fee0c793a0afae6f6","sup_b584d0043bfeac89d90a"],"title":"direct form, not causative","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:2","qac_refs":["89:29:1:2","89:29:1:3"],"status":"accepted"}},{"anchor_refs":["89:29:2"],"branch_refs":[],"candidate_id":"cand_8d0fe483e073adbac969","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000464"],"scope":"focus_ayah","source_local_id":"89:29:2:feminine-singular-addressee","source_type":"word_analysis","support_ids":["sup_33e2285f8b25b16d4a25","sup_603fee0c793a0afae6f6"],"title":"same feminine singular addressee","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:2","qac_refs":["89:29:1:2","89:29:1:3"],"status":"accepted"}},{"anchor_refs":["89:29:2"],"branch_refs":[],"candidate_id":"cand_6b647c1bc95e6d3915d4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000464"],"scope":"focus_ayah","source_local_id":"89:29:2:fulfilled-access-echo","source_type":"word_analysis","support_ids":["sup_249b993b5c979ecc67fd","sup_603fee0c793a0afae6f6"],"title":"fulfilled access echo","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:2","qac_refs":["89:29:1:2","89:29:1:3"],"status":"accepted"}},{"anchor_refs":["89:29:2"],"branch_refs":[],"candidate_id":"cand_406fc71c23168c531ffc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000464"],"scope":"focus_ayah","source_local_id":"89:29:2:joined-recitation-onset","source_type":"word_analysis","support_ids":["sup_603fee0c793a0afae6f6","sup_b0d8987624d92be5f443"],"title":"joined recitation onset","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:2","qac_refs":["89:29:1:2","89:29:1:3"],"status":"accepted"}},{"anchor_refs":["89:29:2"],"branch_refs":[],"candidate_id":"cand_cc338e808b0bd6cb5e67","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000464"],"scope":"focus_ayah","source_local_id":"89:29:2:relational-access-pressure","source_type":"word_analysis","support_ids":["sup_603fee0c793a0afae6f6","sup_7e85a09b155143e13560"],"title":"relational access pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:2","qac_refs":["89:29:1:2","89:29:1:3"],"status":"accepted"}},{"anchor_refs":["89:29:2"],"branch_refs":[],"candidate_id":"cand_05813fc4c0f7174e4526","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000464"],"scope":"focus_ayah","source_local_id":"89:29:2:threshold-sound","source_type":"word_analysis","support_ids":["sup_603fee0c793a0afae6f6","sup_aa017e06c37dd0b24af4"],"title":"threshold sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:2","qac_refs":["89:29:1:2","89:29:1:3"],"status":"accepted"}},{"anchor_refs":["89:29:2"],"branch_refs":[],"candidate_id":"cand_fde8f3c9c1c9fad96a96","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000464"],"scope":"focus_ayah","source_local_id":"89:29:2:two-threshold-closure","source_type":"word_analysis","support_ids":["sup_603fee0c793a0afae6f6","sup_8adf568673550541dc3d"],"title":"two threshold closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:2","qac_refs":["89:29:1:2","89:29:1:3"],"status":"accepted"}},{"anchor_refs":["89:29:3"],"branch_refs":[],"candidate_id":"cand_1bde1f858ead1602e557","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:29:3:approach-to-containment","source_type":"word_analysis","support_ids":["sup_0ee68da7298c6ee4aeed","sup_3b9058617a40afe44a35"],"title":"approach becomes containment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:3","qac_refs":["89:29:2:1"],"status":"accepted"}},{"anchor_refs":["89:29:3"],"branch_refs":[],"candidate_id":"cand_4cf6eff78c862c9f6b31","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:29:3:governed-inclusion-sphere","source_type":"word_analysis","support_ids":["sup_0ee68da7298c6ee4aeed","sup_4d5d4c7cec3b1083bc71"],"title":"governed inclusion sphere","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:3","qac_refs":["89:29:2:1"],"status":"accepted"}},{"anchor_refs":["89:29:3"],"branch_refs":[],"candidate_id":"cand_c0c59f4045dafc29af2a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:29:3:light-hinge-sound","source_type":"word_analysis","support_ids":["sup_0ee68da7298c6ee4aeed","sup_fa0d8bed871f57547c3a"],"title":"light hinge sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:3","qac_refs":["89:29:2:1"],"status":"accepted"}},{"anchor_refs":["89:29:3"],"branch_refs":[],"candidate_id":"cand_3a59504c99d0540d2a3f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:29:3:servants-before-garden-contrast","source_type":"word_analysis","support_ids":["sup_00924eddb7cb6ab71a2d","sup_0ee68da7298c6ee4aeed"],"title":"servant sphere before garden object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:3","qac_refs":["89:29:2:1"],"status":"accepted"}},{"anchor_refs":["89:29:4"],"branch_refs":[],"candidate_id":"cand_c79a2a823c0cf1fef5e6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"89:29:4:conduct-shaped-servants","source_type":"word_analysis","support_ids":["sup_89327bc34e59c15886f9","sup_f1497113f2eaf6f11dd6"],"title":"conduct-shaped servants","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:4","qac_refs":["89:29:3:1","89:29:3:2"],"status":"accepted"}},{"anchor_refs":["89:29:4"],"branch_refs":[],"candidate_id":"cand_99153127164c8d04e462","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"89:29:4:devotional-domain-pressure","source_type":"word_analysis","support_ids":["sup_d3f6840eb8d5588d289f","sup_f1497113f2eaf6f11dd6"],"title":"devotional domain pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:4","qac_refs":["89:29:3:1","89:29:3:2"],"status":"accepted"}},{"anchor_refs":["89:29:4"],"branch_refs":[],"candidate_id":"cand_77a7fd991b9e4afc81d7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"89:29:4:entry-servant-collocation-specificity","source_type":"word_analysis","support_ids":["sup_7faf1fa484ae0651227f","sup_f1497113f2eaf6f11dd6"],"title":"entry-servant specificity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:4","qac_refs":["89:29:3:1","89:29:3:2"],"status":"accepted"}},{"anchor_refs":["89:29:4"],"branch_refs":[],"candidate_id":"cand_d62e98dfc1b49c838823","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"89:29:4:final-sound-landing","source_type":"word_analysis","support_ids":["sup_ecb635e9595760c5e966","sup_f1497113f2eaf6f11dd6"],"title":"final sound landing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:4","qac_refs":["89:29:3:1","89:29:3:2"],"status":"accepted"}},{"anchor_refs":["89:29:4"],"branch_refs":[],"candidate_id":"cand_8b41b80702212b7f7865","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"89:29:4:governed-servant-sphere","source_type":"word_analysis","support_ids":["sup_e054bb57092f39018d75","sup_f1497113f2eaf6f11dd6"],"title":"governed servant sphere","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:4","qac_refs":["89:29:3:1","89:29:3:2"],"status":"accepted"}},{"anchor_refs":["89:29:4"],"branch_refs":[],"candidate_id":"cand_253dc29b3d507124c6e9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"89:29:4:lord-to-servants-relation-shift","source_type":"word_analysis","support_ids":["sup_f1497113f2eaf6f11dd6","sup_fabd166b8a2c21664719"],"title":"Lord to servants relation shift","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:4","qac_refs":["89:29:3:1","89:29:3:2"],"status":"accepted"}},{"anchor_refs":["89:29:4"],"branch_refs":[],"candidate_id":"cand_21f325b4c695c6d9904a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"89:29:4:plural-and-variant-scale","source_type":"word_analysis","support_ids":["sup_26d0fdf5696620b1358a","sup_f1497113f2eaf6f11dd6"],"title":"plural and variant scale","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:4","qac_refs":["89:29:3:1","89:29:3:2"],"status":"accepted"}},{"anchor_refs":["89:29:4"],"branch_refs":[],"candidate_id":"cand_4f5752f404b2be17d0c8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"89:29:4:possessed-definite-community","source_type":"word_analysis","support_ids":["sup_c181316ebc04fe78b541","sup_f1497113f2eaf6f11dd6"],"title":"possessed definite community","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:4","qac_refs":["89:29:3:1","89:29:3:2"],"status":"accepted"}},{"anchor_refs":["89:29:4"],"branch_refs":[],"candidate_id":"cand_01a076151a2deb4d2df5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"89:29:4:possessive-mercy-echo","source_type":"word_analysis","support_ids":["sup_dd5a5da8152ea5ef985c","sup_f1497113f2eaf6f11dd6"],"title":"possessive mercy echo","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:4","qac_refs":["89:29:3:1","89:29:3:2"],"status":"accepted"}},{"anchor_refs":["89:29:4"],"branch_refs":[],"candidate_id":"cand_918254c2e6d50b4983a2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"89:29:4:servants-before-garden","source_type":"word_analysis","support_ids":["sup_51c75c15db11804fd9ca","sup_f1497113f2eaf6f11dd6"],"title":"servants before garden","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:4","qac_refs":["89:29:3:1","89:29:3:2"],"status":"accepted"}},{"anchor_refs":["89:29:4"],"branch_refs":[],"candidate_id":"cand_d4e0d5b5c525c1b74d61","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"89:29:4:worship-service-identity","source_type":"word_analysis","support_ids":["sup_d37a77bdb569ddd32e7e","sup_f1497113f2eaf6f11dd6"],"title":"worship-service identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:4","qac_refs":["89:29:3:1","89:29:3:2"],"status":"accepted"}},{"anchor_refs":["89:29:1"],"branch_refs":[],"candidate_id":"cand_e60d213446d2dd96d19a","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000464"],"scope":"focus_ayah","source_local_id":"89:29:1:2","source_type":"qac_morpheme","support_ids":["sup_d071641ae68dbdc552fe"],"title":"QAC root occurrence: د خ ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:29:3"],"branch_refs":[],"candidate_id":"cand_c374c2407e3b91d7956c","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"89:29:3:1","source_type":"qac_morpheme","support_ids":["sup_d6dd56c7e5693748eb5a"],"title":"QAC root occurrence: ع ب د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:29:4"],"branch_refs":[],"candidate_id":"cand_6fd5e89e38ea81b5526b","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000973"],"scope":"focus_ayah","source_local_id":"89:29:4:smooth-road-overread","source_type":"word_analysis","support_ids":["sup_3773802ec6e14f4e8b17","sup_f1497113f2eaf6f11dd6"],"title":"smooth-road branch as local activation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:29:4","qac_refs":["89:29:3:1","89:29:3:2"],"status":"accepted"}},{"anchor_refs":["89:29"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:29","branch_refs":["root_000464/B001","root_000973/B003"],"candidate_id":"cand_8bb69e263144bebd1b35","commentary_obligation":"review","hft_ref":"hft_9dccd79cc64db35c04d8","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_boundary_membership","source_type":"hft","support_ids":["sup_abc1d398ce5770bb7c7a"],"title":"baseline_boundary_membership","trust":"legacy_unbound"},{"anchor_refs":["89:29"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:29","branch_refs":["root_000464/B003","root_000973/B003"],"candidate_id":"cand_b64278801ac82d99c5da","commentary_obligation":"review","hft_ref":"hft_cec5ac0635dc0e48b0da","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_interiorized_service","source_type":"hft","support_ids":["sup_01d456b25c95b81e9f96"],"title":"baseline_interiorized_service","trust":"legacy_unbound"},{"anchor_refs":["89:29"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:29","branch_refs":["root_000464/B005","root_000464/B008","root_000973/B003"],"candidate_id":"cand_a19b0a1f12282f0ead07","commentary_obligation":"review","hft_ref":"hft_fad861886499968f1a2e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_interleaved_belonging","source_type":"hft","support_ids":["sup_75d44d48f421df9e872b"],"title":"baseline_interleaved_belonging","trust":"legacy_unbound"},{"anchor_refs":["89:29"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:29","branch_refs":["root_000464/B001","root_000973/B001","root_000973/B006"],"candidate_id":"cand_f9427fd9b198285eba55","commentary_obligation":"review","hft_ref":"hft_7bb9699afd7c14ef523b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_honored_servant_paradox","source_type":"hft","support_ids":["sup_25fc6d9bc5a8de9d221a"],"title":"baseline_honored_servant_paradox","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فَٱدْخُلِى فِى عِبَٰدِى","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"89:29:1:1","qac_word_ref":"89:29:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:29:1:2","qac_word_ref":"89:29:1","root_ar":"د خ ل","surface_ar":"ٱدْخُلِ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:29:1:3","qac_word_ref":"89:29:1","root_ar":"","surface_ar":"ى"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"89:29:2:1","qac_word_ref":"89:29:2","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"عَبْد","morph_features":"STEM|POS:N|LEM:Eabod|ROOT:Ebd|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:29:3:1","qac_word_ref":"89:29:3","root_ar":"ع ب د","surface_ar":"عِبَٰدِ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1S","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:29:3:2","qac_word_ref":"89:29:3","root_ar":"","surface_ar":"ى"}],"word_analysis_qac_refs":[["89:29:1:1"],["89:29:1:2","89:29:1:3"],["89:29:2:1"],["89:29:3:1","89:29:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["89:29:1","89:29:2","89:29:3","89:29:4"]},"focus_surface_evidence":{"arabic_uthmani":"فَٱدْخُلِى فِى عِبَٰدِى","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"89:29:1:1","qac_word_ref":"89:29:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"دَخَلَ","morph_features":"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:29:1:2","qac_word_ref":"89:29:1","root_ar":"د خ ل","surface_ar":"ٱدْخُلِ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:29:1:3","qac_word_ref":"89:29:1","root_ar":"","surface_ar":"ى"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"89:29:2:1","qac_word_ref":"89:29:2","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"عَبْد","morph_features":"STEM|POS:N|LEM:Eabod|ROOT:Ebd|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:29:3:1","qac_word_ref":"89:29:3","root_ar":"ع ب د","surface_ar":"عِبَٰدِ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1S","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:29:3:2","qac_word_ref":"89:29:3","root_ar":"","surface_ar":"ى"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["89:29:1:1"],["89:29:1:2","89:29:1:3"],["89:29:2:1"],["89:29:3:1","89:29:3:2"]],"word_analysis_refs":["89:29:1","89:29:2","89:29:3","89:29:4"],"word_rows":[{"analysis_record_ref":"89:29:1","analytic_gloss_range_en":"resultive conjunction that carries the previous return-command into a new commanded entry","analytic_root_gloss_range_en":null,"qac_refs":["89:29:1:1"],"root":{},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"89:29:2","analytic_gloss_range_en":"second-person feminine singular command to enter, locally framed as authorized access into the servant community through the following prepositional phrase","analytic_root_gloss_range_en":"entering, going inside, access, and related interior or mixed-in branches; the local imperative selects commanded entry/access, while unrelated branches such as defect, income, and object names are not active","qac_refs":["89:29:1:2","89:29:1:3"],"root":{"arabic":"د خ ل","transliteration":"d-kh-l"},"surface":{"arabic":"ٱدْخُلِى","transliteration":"udkhulī"}},{"analysis_record_ref":"89:29:3","analytic_gloss_range_en":"preposition marking the entered sphere, company, or domain, not a direct-object relation","analytic_root_gloss_range_en":null,"qac_refs":["89:29:2:1"],"root":{},"surface":{"arabic":"فِى","transliteration":"fī"}},{"analysis_record_ref":"89:29:4","analytic_gloss_range_en":"possessed plural servant collective, locally the community into which the addressed soul is admitted","analytic_root_gloss_range_en":"servanthood, worship, service, dependence, belonging, and related subjection branches; the local noun selects the divine-servant collective, while physical smoothing and other remote branches are not local senses","qac_refs":["89:29:3:1","89:29:3:2"],"root":{"arabic":"ع ب د","transliteration":"ʿ-b-d"},"surface":{"arabic":"عِبَٰدِى","transliteration":"ʿibādī"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["89:29"],"branch_refs":["root_000464/B001","root_000973/B003"],"candidate_id":"cand_8bb69e263144bebd1b35","evidence_scope":"focus_ayah","hft_ref":"hft_9dccd79cc64db35c04d8","item_id":"baseline_boundary_membership","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_boundary_membership","support_id":"sup_abc1d398ce5770bb7c7a"},{"anchor_refs":["89:29"],"branch_refs":["root_000464/B003","root_000973/B003"],"candidate_id":"cand_b64278801ac82d99c5da","evidence_scope":"focus_ayah","hft_ref":"hft_cec5ac0635dc0e48b0da","item_id":"baseline_interiorized_service","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_interiorized_service","support_id":"sup_01d456b25c95b81e9f96"},{"anchor_refs":["89:29"],"branch_refs":["root_000464/B005","root_000464/B008","root_000973/B003"],"candidate_id":"cand_a19b0a1f12282f0ead07","evidence_scope":"focus_ayah","hft_ref":"hft_fad861886499968f1a2e","item_id":"baseline_interleaved_belonging","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_interleaved_belonging","support_id":"sup_75d44d48f421df9e872b"},{"anchor_refs":["89:29"],"branch_refs":["root_000464/B001","root_000973/B001","root_000973/B006"],"candidate_id":"cand_f9427fd9b198285eba55","evidence_scope":"focus_ayah","hft_ref":"hft_7bb9699afd7c14ef523b","item_id":"baseline_honored_servant_paradox","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_honored_servant_paradox","support_id":"sup_25fc6d9bc5a8de9d221a"}],"diagnostics":[],"lane_counts":{"global":12,"macro":6,"micro":4},"packet_summary":{"ayah_count":30,"focus_ref":"89:29","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000702","furuq_root_norm":"س ر ي","furuq_source_root_norm":"س ر ي","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000697","furuq_root_norm":"س ر ر","furuq_source_root_norm":"س ر ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ع و د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":true,"target_occurrences":35,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ج و ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000273","furuq_root_norm":"ج و ب","furuq_source_root_norm":"ج و ب","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000283","furuq_root_norm":"ج ي ب","furuq_source_root_norm":"ج ي ب","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000220","furuq_root_norm":"ج ب ي","furuq_source_root_norm":"ج ب ي","is_dominant":false,"target_occurrences":2,"target_rank":3},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000214","furuq_root_norm":"ج ب ب","furuq_source_root_norm":"ج ب ب","is_dominant":false,"target_occurrences":1,"target_rank":4}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ب ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000153","furuq_root_norm":"ب ل و","furuq_source_root_norm":"ب ل و","is_dominant":true,"target_occurrences":28,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000154","furuq_root_norm":"ب ل ي","furuq_source_root_norm":"ب ل ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ه و ن","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001453","furuq_root_norm":"م ه ن","furuq_source_root_norm":"م ه ن","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001608","furuq_root_norm":"ه و ن","furuq_source_root_norm":"ه و ن","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001687","furuq_root_norm":"و ه ن","furuq_source_root_norm":"و ه ن","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14","89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"89:29","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":13,"unstructured_record_count":0},"identity":{"ayah_ref":"89:29","lane":"micro","linguistic_source_ref":"89:29","surface_ref":"89:29","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"89:29","target_tokens":[["Kullarımın",["89:29:3"]],["arasına",["89:29:2"]],["gir",["89:29:1"]]],"text":"Kullarımın arasına gir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":15,"ayah_to":30,"id":"s089-p02-015-030","label":"The wealth test, judgment, and tranquil soul","number":2,"refs":["89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:1","source_type":"word_analysis","support_id":"sup_003f050e25841561616f","text":"{\"gloss_range\":\"resultive conjunction that carries the previous return-command into a new commanded entry\",\"prose\":\"{{ar:فَ}} ({{tr:fa}}) makes the ayah begin mid-sequence. The entry command is heard as the ordered consequence of the prior return in 89:28, not as a detached reward scene. Because the particle is prefixed onto the command surface, discourse link and authorization feel compressed into one opening movement: return to the Lord, therefore enter among His servants. The boundary also shifts the result from approach to the Lord into social incorporation among those who belong to Him.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:3:servants-before-garden-contrast","source_type":"word_analysis","support_id":"sup_00924eddb7cb6ab71a2d","text":"{\"blocking_evidence\":null,\"headline\":\"servant sphere before garden object\",\"reader_payoff\":\"The reader notices that social inclusion is grammatically marked before the garden is named in 89:30.\",\"reason\":\"The local phrase is explicitly prepositional, while the next ayah changes the endpoint frame around the garden.\",\"representative_source_ids\":[\"QE-3664ea7d\",\"QB-836f9601\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:3","source_type":"word_analysis","support_id":"sup_0ee68da7298c6ee4aeed","text":"{\"gloss_range\":\"preposition marking the entered sphere, company, or domain, not a direct-object relation\",\"prose\":\"{{ar:فِى}} ({{tr:fī}}) turns the endpoint into an inclusion sphere. The command does not make {{ar:عِبَٰدِى}} ({{tr:ʿibādī}}) a bare object; it places the soul within or among the speaker's servants, making the collective syntactically necessary rather than ornamental. That prepositional logic also marks the boundary from the prior movement toward {{ar:إِلَىٰ رَبِّكِ}} ({{tr:ilā rabbiki}}) in 89:28 to containment within a plural servant domain. In 89:30 the garden endpoint can be named more directly as {{ar:جَنَّتِى}} ({{tr:jannatī}}), so this small preposition gives 89:29 its specifically social inclusion. As a brief hinge, it also lets the line pivot audibly from command to domain before the possessed plural lands.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فِى}} ({{tr:fī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:2:fulfilled-access-echo","source_type":"word_analysis","support_id":"sup_249b993b5c979ecc67fd","text":"{\"blocking_evidence\":null,\"headline\":\"fulfilled access echo\",\"reader_payoff\":\"The reader notices 89:29 as granted access when set beside the entry-request of 17:80.\",\"reason\":\"The concrete reference is a valid contrast: 17:80 is petitionary, while 89:29 is an imperative from the speaker who owns the entered servant community.\",\"representative_source_ids\":[\"QI-3d186508\",\"MI-d5fb8692\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:4:plural-and-variant-scale","source_type":"word_analysis","support_id":"sup_26d0fdf5696620b1358a","text":"{\"blocking_evidence\":null,\"headline\":\"plural and variant scale\",\"reader_payoff\":\"The reader notices that the canonical endpoint is a possessed community, not a single servant relation.\",\"reason\":\"The local QAC row supports the plural construct noun; the variants clarify what changes in number or locus but do not replace the canonical parse.\",\"representative_source_ids\":[\"QF-12a61e65\",\"QF-adcf6cb5\",\"MF-f53d9279\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:1:prefixed-compression","source_type":"word_analysis","support_id":"sup_2b18bef72843cb95a9f4","text":"{\"blocking_evidence\":null,\"headline\":\"prefixed command compression\",\"reader_payoff\":\"The reader hears and sees the transition rush straight into the command rather than pausing before a new sentence.\",\"reason\":\"The particle is analytically split but prefixed to the following imperative surface, supporting the compressed transition noted by the CRITICAL rows.\",\"representative_source_ids\":[\"QF-747606e7\",\"MT-1d90d7a7\",\"QP-f9178e03\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:2:feminine-singular-addressee","source_type":"word_analysis","support_id":"sup_33e2285f8b25b16d4a25","text":"{\"blocking_evidence\":null,\"headline\":\"same feminine singular addressee\",\"reader_payoff\":\"The reader keeps one addressed soul in view across the command sequence instead of shifting to a crowd or impersonal recipient.\",\"reason\":\"The local morphology is a second-person feminine singular imperative with an implicit subject continuing the vocative addressee from 89:27.\",\"representative_source_ids\":[\"QG-ff5a6a7d\",\"MG-5f813219\",\"QF-5b00088e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:4:smooth-road-overread","source_type":"word_analysis","support_id":"sup_3773802ec6e14f4e8b17","text":"{\"blocking_evidence\":\"The local word is a possessed plural servant noun governed by {{ar:فِى}} ({{tr:fī}}); V4 places the smooth or passable sense in physical-object uses such as road or camel expressions, not in this construct.\",\"headline\":\"smooth-road branch as local activation\",\"reader_payoff\":null,\"reason\":\"Entry language nearby does not license replacing the local servant collective with a physical smooth-road branch.\",\"representative_source_ids\":[\"QS-cd87e171\"],\"status\":\"rejected\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:3:approach-to-containment","source_type":"word_analysis","support_id":"sup_3b9058617a40afe44a35","text":"{\"blocking_evidence\":null,\"headline\":\"approach becomes containment\",\"reader_payoff\":\"The reader notices the boundary changing from approach to containment and company.\",\"reason\":\"The local preposition licenses the range of in, into, within, or among, and the governed plural servant noun makes the inclusion social as well as spatial.\",\"representative_source_ids\":[\"QS-046cce9e\",\"QS-7e53de13\",\"MS-97292f85\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:1:return-to-incorporation","source_type":"word_analysis","support_id":"sup_3f2d80c4967198537eae","text":"{\"blocking_evidence\":null,\"headline\":\"return becomes incorporation\",\"reader_payoff\":\"The reader notices that the accepted return immediately takes social form as incorporation among the speaker's servants.\",\"reason\":\"The following prepositional complement names the servant community as the resultive destination of the command sequence.\",\"representative_source_ids\":[\"QB-45238152\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:3:governed-inclusion-sphere","source_type":"word_analysis","support_id":"sup_4d5d4c7cec3b1083bc71","text":"{\"blocking_evidence\":null,\"headline\":\"governed inclusion sphere\",\"reader_payoff\":\"The reader notices that the servants are an enclosing sphere of inclusion, not a direct object consumed by the verb.\",\"reason\":\"Attachment evidence marks the following noun as a syntactically forced prepositional complement of the entry command.\",\"representative_source_ids\":[\"QG-0d6c4710\",\"QG-64913ac8\",\"MG-0f0875cd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:4:servants-before-garden","source_type":"word_analysis","support_id":"sup_51c75c15db11804fd9ca","text":"{\"blocking_evidence\":null,\"headline\":\"servants before garden\",\"reader_payoff\":\"The reader notices that communal belonging is the first named reward, before the garden appears in 89:30.\",\"reason\":\"The final word of 89:29 is the possessed servant collective, while 89:30 follows with the possessed garden endpoint.\",\"representative_source_ids\":[\"QT-efb3f46c\",\"MT-af3a36b2\",\"QE-01dfe6f9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:2","source_type":"word_analysis","support_id":"sup_603fee0c793a0afae6f6","text":"{\"gloss_range\":\"second-person feminine singular command to enter, locally framed as authorized access into the servant community through the following prepositional phrase\",\"prose\":\"{{ar:ٱدْخُلِى}} ({{tr:udkhulī}}) is a direct feminine singular imperative, so the addressed soul remains the same one summoned in 89:27 and is not replaced by a crowd or impersonal recipient. Its Form I command addresses the soul's own crossing while the speaker's authority grants the access; a causative admission frame would move attention toward an outside admitting agent. The verb is not bare motion: {{ar:فِى عِبَٰدِى}} ({{tr:fī ʿibādī}}) completes it as authorized access into a servant-sphere, so the entry-request of 17:80 is answered here as granted access. The root's access and interior pressure helps the reader feel threshold-crossing into a community relation, while the local grammar keeps the sense to commanded entry rather than importing unrelated dictionary branches. The same entry command returns in 89:30 with {{ar:جَنَّتِى}} ({{tr:jannatī}}), so the close has two thresholds: first relational inclusion, then garden entry, with the compact sound of the command fitting that boundary-crossing force.\",\"root_display\":\"{{ar:د خ ل}} ({{tr:d-kh-l}})\",\"root_gloss_range\":\"entering, going inside, access, and related interior or mixed-in branches; the local imperative selects commanded entry/access, while unrelated branches such as defect, income, and object names are not active\",\"surface_display\":\"{{ar:ٱدْخُلِى}} ({{tr:udkhulī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:2:completed-entry-frame","source_type":"word_analysis","support_id":"sup_6cc96ff57d50edccfd82","text":"{\"blocking_evidence\":null,\"headline\":\"completed entry frame\",\"reader_payoff\":\"The reader notices that the command grants entry into a defined sphere of belonging, not movement with no named destination.\",\"reason\":\"Attachment evidence identifies {{ar:فِى عِبَٰدِى}} ({{tr:fī ʿibādī}}) as the governed complement of the imperative, and V4 supports the basic entering/access branch.\",\"representative_source_ids\":[\"QG-9ce9c664\",\"QS-7a5ff80a\",\"QY-d09f88a8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:2:relational-access-pressure","source_type":"word_analysis","support_id":"sup_7e85a09b155143e13560","text":"{\"blocking_evidence\":null,\"headline\":\"relational access pressure\",\"reader_payoff\":\"The reader feels entry as access into a community relation, not merely crossing a physical line.\",\"reason\":\"The local prepositional frame licenses relational admission, but broader mixed-in or inner-affair branches remain background pressure rather than separate local senses.\",\"representative_source_ids\":[\"QS-63e8d1a3\",\"QS-9e83c2be\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:4:entry-servant-collocation-specificity","source_type":"word_analysis","support_id":"sup_7faf1fa484ae0651227f","text":"{\"blocking_evidence\":null,\"headline\":\"entry-servant specificity\",\"reader_payoff\":\"The reader notices that this is not generic entry language but entry specified by a servant community.\",\"reason\":\"The local attachment directly joins the entry command to the prepositional servant complement.\",\"representative_source_ids\":[\"QI-48d02804\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:4:conduct-shaped-servants","source_type":"word_analysis","support_id":"sup_89327bc34e59c15886f9","text":"{\"blocking_evidence\":null,\"headline\":\"conduct-shaped servants\",\"reader_payoff\":\"The reader notices that the admitted group is a relational and conduct-shaped category, not a simple population marker.\",\"reason\":\"The concrete comparison to servant-language in 25:63 is compatible with the local possessed servant collective.\",\"representative_source_ids\":[\"QI-333a49e0\",\"MI-bc7ef94a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:2:two-threshold-closure","source_type":"word_analysis","support_id":"sup_8adf568673550541dc3d","text":"{\"blocking_evidence\":null,\"headline\":\"two threshold closure\",\"reader_payoff\":\"The reader notices that belonging among servants is named before the garden, making the closing ascent relational before it is spatial.\",\"reason\":\"The same imperative root recurs in the next ayah, while the complement frame changes from the servant prepositional sphere in 89:29 to the garden endpoint in 89:30.\",\"representative_source_ids\":[\"MT-5903e287\",\"QE-6203ad0a\",\"ME-b42d2d3a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:2:threshold-sound","source_type":"word_analysis","support_id":"sup_aa017e06c37dd0b24af4","text":"{\"blocking_evidence\":null,\"headline\":\"threshold sound\",\"reader_payoff\":\"The reader hears the command as a compact push through a threshold rather than a soft descriptive state.\",\"reason\":\"The sound observation is local to the surface form and supports, rather than replaces, the grammatical threshold reading.\",\"representative_source_ids\":[\"QP-93f39087\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:2:joined-recitation-onset","source_type":"word_analysis","support_id":"sup_b0d8987624d92be5f443","text":"{\"blocking_evidence\":null,\"headline\":\"joined recitation onset\",\"reader_payoff\":\"The reader hears the result particle run straight into the threshold command, reinforcing immediacy.\",\"reason\":\"The written command begins with a joining onset after the prefixed result particle, matching the CRITICAL sound observation.\",\"representative_source_ids\":[\"QF-386cf1ea\",\"QP-cdedb77f\",\"MP-b4593b48\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:2:direct-form-not-causative","source_type":"word_analysis","support_id":"sup_b584d0043bfeac89d90a","text":"{\"blocking_evidence\":null,\"headline\":\"direct form, not causative\",\"reader_payoff\":\"The reader notices that the command addresses the soul's crossing directly while the speaker's authority grants that crossing.\",\"reason\":\"QAC and attachment tag the local verb as a direct Form I imperative, not a causative admission form.\",\"representative_source_ids\":[\"QG-c58343d0\",\"MF-146fd203\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:1:resultive-command-sequence","source_type":"word_analysis","support_id":"sup_b6340deae2518a1486cf","text":"{\"blocking_evidence\":null,\"headline\":\"resultive command sequence\",\"reader_payoff\":\"The reader notices that entry is the next ordered step after return in 89:28, not a separate reward scene.\",\"reason\":\"QAC identifies the word as a prefixed conjunction/result particle, and the local clause continues the imperative sequence from 89:28.\",\"representative_source_ids\":[\"QG-11dcad99\",\"MG-3afa9ff9\",\"QT-fc00d9f3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:4:possessed-definite-community","source_type":"word_analysis","support_id":"sup_c181316ebc04fe78b541","text":"{\"blocking_evidence\":null,\"headline\":\"possessed definite community\",\"reader_payoff\":\"The reader notices that the reward is not generic company but a specific community claimed by the speaker.\",\"reason\":\"The possessive suffix is in construct with the noun and marks the direct-speech speaker as possessor.\",\"representative_source_ids\":[\"QG-3c828af9\",\"QG-ac7dd47a\",\"QF-d3934066\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:29:1:2","source_type":"qac_morpheme","support_id":"sup_d071641ae68dbdc552fe","text":"{\"lemma_ar\":\"دَخَلَ\",\"morph_features\":\"STEM|POS:V|IMPV|LEM:daxala|ROOT:dxl|2FS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"89:29:1:2\",\"qac_word_ref\":\"89:29:1\",\"root_ar\":\"د خ ل\",\"surface_ar\":\"ٱدْخُلِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:4:worship-service-identity","source_type":"word_analysis","support_id":"sup_d37a77bdb569ddd32e7e","text":"{\"blocking_evidence\":null,\"headline\":\"worship-service identity\",\"reader_payoff\":\"The reader notices that entry is into a relational identity of service, worship, obedience, and dependence.\",\"reason\":\"V4 supports servanthood to God and worship/submissive obedience branches, and local possession selects the divine servant collective.\",\"representative_source_ids\":[\"QS-02b7f41d\",\"QS-2fc1d679\",\"MS-f470272e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:4:devotional-domain-pressure","source_type":"word_analysis","support_id":"sup_d3f6840eb8d5588d289f","text":"{\"blocking_evidence\":null,\"headline\":\"devotional domain pressure\",\"reader_payoff\":\"The reader feels worship as the domain into which the soul is admitted, while still reading the word as people.\",\"reason\":\"The prepositional frame permits domain language, but the local surface is the plural servant noun, not a place noun.\",\"representative_source_ids\":[\"QS-67e6d4a4\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:29:3:1","source_type":"qac_morpheme","support_id":"sup_d6dd56c7e5693748eb5a","text":"{\"lemma_ar\":\"عَبْد\",\"morph_features\":\"STEM|POS:N|LEM:Eabod|ROOT:Ebd|MP|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"89:29:3:1\",\"qac_word_ref\":\"89:29:3\",\"root_ar\":\"ع ب د\",\"surface_ar\":\"عِبَٰدِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:4:possessive-mercy-echo","source_type":"word_analysis","support_id":"sup_dd5a5da8152ea5ef985c","text":"{\"blocking_evidence\":null,\"headline\":\"possessive mercy echo\",\"reader_payoff\":\"The reader hears possessive intimacy here as final inclusion when set beside the mercy summons in 39:53.\",\"reason\":\"The row gives a concrete possessive-plural echo in 39:53, and the local suffix likewise marks the speaker's servant claim.\",\"representative_source_ids\":[\"QI-9fd47584\",\"MI-c7761655\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:4:governed-servant-sphere","source_type":"word_analysis","support_id":"sup_e054bb57092f39018d75","text":"{\"blocking_evidence\":null,\"headline\":\"governed servant sphere\",\"reader_payoff\":\"The reader sees the servants as the community entered among, while the addressed soul remains grammatically distinct.\",\"reason\":\"Attachment evidence marks the noun as the object of the preposition, and the verb's feminine singular subject differs from the masculine plural endpoint.\",\"representative_source_ids\":[\"QG-1cb901f1\",\"QG-1cc41b45\",\"QG-b3528fd6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:4:final-sound-landing","source_type":"word_analysis","support_id":"sup_ecb635e9595760c5e966","text":"{\"blocking_evidence\":null,\"headline\":\"final sound landing\",\"reader_payoff\":\"The reader hears the command and the possessed servant endpoint land together through their matching long ending.\",\"reason\":\"The sound observation is tied to the local surface and supports the noun's role as the ayah's relational landing.\",\"representative_source_ids\":[\"QP-0b72bd70\",\"QP-372b408a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:4","source_type":"word_analysis","support_id":"sup_f1497113f2eaf6f11dd6","text":"{\"gloss_range\":\"possessed plural servant collective, locally the community into which the addressed soul is admitted\",\"prose\":\"{{ar:عِبَٰدِى}} ({{tr:ʿibādī}}) is the governed endpoint of {{ar:فِى}} ({{tr:fī}}), so the servants are not a second addressee but the collective into which the soul enters. The construct and final possessive make the group definite as the speaker's own, turning reward first into claimed belonging rather than generic company. The root keeps worship, service, obedience, and dependence in view; it makes the entered group a relational and conduct-shaped identity, comparable to servant conduct in 25:63, while the possessed plural also recalls the mercy summons of 39:53 now as final inclusion. The plural form makes that identity communal, many in membership but one in belonging; the singular variant {{ar:عَبْدِي}} ({{tr:ʿabdī}}) shows how much would change if the endpoint were individualized, while the local noun remains people rather than a place noun or a smooth-road image. The relation also shifts from {{ar:رَبِّكِ}} ({{tr:rabbiki}}) in 89:28 to My servants here, and then to {{ar:جَنَّتِى}} ({{tr:jannatī}}) in 89:30, so belonging comes before place, with the matching long ending of command and endpoint making the relational landing audible.\",\"root_display\":\"{{ar:ع ب د}} ({{tr:ʿ-b-d}})\",\"root_gloss_range\":\"servanthood, worship, service, dependence, belonging, and related subjection branches; the local noun selects the divine-servant collective, while physical smoothing and other remote branches are not local senses\",\"surface_display\":\"{{ar:عِبَٰدِى}} ({{tr:ʿibādī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:3:light-hinge-sound","source_type":"word_analysis","support_id":"sup_fa0d8bed871f57547c3a","text":"{\"blocking_evidence\":null,\"headline\":\"light hinge sound\",\"reader_payoff\":\"The reader hears the small hinge that moves the line from action into the inclusion phrase.\",\"reason\":\"The sound note is local to the one-syllable preposition and reinforces the grammar of the governed phrase.\",\"representative_source_ids\":[\"QP-650d581f\",\"QP-dbd8fdba\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:29:4:lord-to-servants-relation-shift","source_type":"word_analysis","support_id":"sup_fabd166b8a2c21664719","text":"{\"blocking_evidence\":null,\"headline\":\"Lord to servants relation shift\",\"reader_payoff\":\"The reader notices that private return to the Lord opens into communal incorporation under the same divine speaker.\",\"reason\":\"The local first-person suffix names the speaker as possessor of the servants after 89:28 names the addressee's Lord.\",\"representative_source_ids\":[\"MI-c9e24086\",\"QE-08b8a6ac\",\"ME-07ebc1e5\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَٱدْخُلِى فِى عِبَٰدِى","ayah_ref":"89:29"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000464/B001","root_000973/B003"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000464","role":"Going inside supplies the boundary crossing and makes the imperative an admission rather than mere proximity.","root":"د خ ل","source_ref":"89:29","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000973","role":"Worship and submissive obedience supply the relation that constitutes the destination collective.","root":"ع ب د","source_ref":"89:29","source_word_indices":["3"]}],"changed_reading":{"after":"A command to cross into belonging among those constituted by service and obedience to the speaker.","before":"A command to go inside an unspecified place near some servants."},"confidence":"strong","focus_anchor":"`فَٱدْخُلِى فِى عِبَٰدِى` joins a singular imperative of entry to `فِى` and the possessed plural `عِبَٰدِى`.","mechanism":"The command moves the addressee across a boundary into a collective whose shared principle is submissive service to the speaker. Entry therefore changes location and affiliation at once.","model_id":"baseline_boundary_membership"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_boundary_membership","source_type":"hft","support_id":"sup_abc1d398ce5770bb7c7a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱدْخُلِى فِى عِبَٰدِى","ayah_ref":"89:29"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000464/B003","root_000973/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000464","role":"The hidden interior turns entry toward an inward state rather than limiting it to physical relocation.","root":"د خ ل","source_ref":"89:29","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000973","role":"Submissive worship names the inward orientation that the addressee is invited to inhabit.","root":"ع ب د","source_ref":"89:29","source_word_indices":["3"]}],"changed_reading":{"after":"The addressee enters a lived interior condition of service whose outward form is membership among the servants.","before":"The addressee is externally relocated among a group."},"confidence":"medium","focus_anchor":"The inward branch of `د خ ل` remains attached to the imperative, while `عِبَٰدِى` names the mode entered.","mechanism":"Entry can be inward as well as spatial: the addressee is summoned to inhabit servanthood as an interior disposition that becomes socially visible through belonging among servants.","model_id":"baseline_interiorized_service"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_interiorized_service","source_type":"hft","support_id":"sup_01d456b25c95b81e9f96","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱدْخُلِى فِى عِبَٰدِى","ayah_ref":"89:29"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000464/B005","root_000464/B008","root_000973/B003"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000464","role":"An entrant mixed into a group supplies the social transition from outsider to insider.","root":"د خ ل","source_ref":"89:29","source_word_indices":["1"]},{"branch_id":"B008","mapped_root_id":"root_000464","role":"Interleaving parts supplies a model of close incorporation in which distinguishable parts form one body.","root":"د خ ل","source_ref":"89:29","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000973","role":"Shared obedient service provides the binding relation of the interleaved body.","root":"ع ب د","source_ref":"89:29","source_word_indices":["3"]}],"changed_reading":{"after":"The addressee ceases to be an outsider and becomes an interleaved, still distinguishable member of their body.","before":"The addressee merely stands beside a set of servants."},"confidence":"medium","focus_anchor":"`فِى عِبَٰدِى` can mark inclusion within a plural body, and the entry root carries images of an entrant mixing with a group and of interleaved parts.","mechanism":"The command changes the addressee from an outsider into a constituent part of an existing servant body. Interleaving implies cohesion without requiring the entrant to disappear.","model_id":"baseline_interleaved_belonging"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_interleaved_belonging","source_type":"hft","support_id":"sup_75d44d48f421df9e872b","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱدْخُلِى فِى عِبَٰدِى","ayah_ref":"89:29"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000464/B001","root_000973/B001","root_000973/B006"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000464","role":"Literal entry makes the paradox a conferred status into which the addressee is admitted.","root":"د خ ل","source_ref":"89:29","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000973","role":"Owned or enslaved status supplies the lowering pole inherent in servant language.","root":"ع ب د","source_ref":"89:29","source_word_indices":["3"]},{"branch_id":"B006","mapped_root_id":"root_000973","role":"Being honored and magnified supplies the unexpected elevating pole within the same root.","root":"ع ب د","source_ref":"89:29","source_word_indices":["3"]}],"changed_reading":{"after":"The speaker's possessive summons admits the addressee into a status where lowly service and special honor coexist.","before":"Entry into servanthood lowers the addressee into an owned class."},"confidence":"exploratory","focus_anchor":"The possessed noun `عِبَٰدِى` is capable of activating both owned status and the root's counter-image of being honored and magnified.","mechanism":"The possessive invitation holds abasement and elevation together: entry into the speaker's servants is not simply degradation, because the same root inventory lets service coexist with being specially honored.","model_id":"baseline_honored_servant_paradox"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_honored_servant_paradox","source_type":"hft","support_id":"sup_25fc6d9bc5a8de9d221a","trust":"legacy_unbound"}]}
</lane_packet_json>
