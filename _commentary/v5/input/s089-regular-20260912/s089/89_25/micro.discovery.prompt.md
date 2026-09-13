# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **89:25**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s089-regular-20260912/s089/89_25/micro.discovery.json` and modify nothing
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
  "ayah_ref": "89:25",
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
{"branch_registry":[{"boundary":"Bu dal tekliği ve eşsizliği anlatır; olumsuzlukta kişi kapsamını, onlu sayı kuruluşlarını, gün adını ve dağ adını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000017/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:5:1","qac_word_ref":"89:25:5","surface_ar":"أَحَدٌ"}],"gloss":"tek ve eşi olmayan olma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığı bir tane, tek veya eşi bulunmayan olarak gösterir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Mutlak niteleme olarak kullanıldığında Tanrı'nın ortağı ve benzeri bulunmadığını bildirir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı sözün art arda yinelenmesi tek olma bildirimini pekiştirir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kaynak ifadesi sözcüğü saymanın başlangıcındaki bir sayısıyla da ilişkilendirir; düzenli sayı kuruluşları ayrı dalda ele alınır."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tek olma çekirdeğini, mutlak eşsizliği ve yinelemeli pekiştirmeyi birlikte temsil eden dal düzeyi karşılıktır.","boundary_detail":"Bu dal tekliği ve eşsizliği anlatır; olumsuzlukta kişi kapsamını, onlu sayı kuruluşlarını, gün adını ve dağ adını kapsamaz.","branch_image_ar":"الأَحَدِيَّة والوَحْدَة","concept_gloss":"tek ve eşi olmayan olma","contextual_glosses":[{"applicability":"Sayılabilir bir varlığın tek örnek olduğunu bildiren genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Mutlak eşsizlik ile yinelemeli pekiştirme yüzlerini taşımaz.","preserves":"Bir tane olma çekirdeğini korur."},"facet_ids":["F001","F004"],"text":"bir tane","usage_role":"contextual"},{"applicability":"Tanrı'nın ortağı ve benzeri olmadığını bildiren mutlak niteleme bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel sayısal birliği ve yinelemeli söyleyiş biçimini kapsamaz.","preserves":"Mutlak tekliği ve eşsizliği korur."},"facet_ids":["F002"],"text":"tek ve eşsiz","usage_role":"contextual"},{"applicability":"Teklik bildiren sözün yinelenerek güçlü biçimde vurgulandığı söyleyiş için açıklayıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yinelenmeyen genel kullanımın bütün kapsamını taşımaz.","preserves":"Yineleme yoluyla yapılan tek olma vurgusunu korur."},"facet_ids":["F003"],"text":"yalnız bir, yalnız bir","usage_role":"explanatory"}],"definition":"Bir varlığın bir tane, tek ya da eşi olmayan olmasıdır; mutlak kullanımda Tanrı'nın ortağı ve benzeri bulunmadığını bildirir. Sözcüğün yinelenmesi bu tekliği güçlü biçimde vurgular.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığı bir tane, tek veya eşi bulunmayan olarak gösterir."},{"facet_id":"F002","role":"specialization","statement":"Mutlak niteleme olarak kullanıldığında Tanrı'nın ortağı ve benzeri bulunmadığını bildirir."},{"facet_id":"F003","role":"associated_use","statement":"Aynı sözün art arda yinelenmesi tek olma bildirimini pekiştirir."},{"facet_id":"F004","role":"source_variant","statement":"Kaynak ifadesi sözcüğü saymanın başlangıcındaki bir sayısıyla da ilişkilendirir; düzenli sayı kuruluşları ayrı dalda ele alınır."}],"identity_rationale":"Kaynak ifadesi tek olma, mutlak biçimde eşsiz sayılma ve yinelemeyle bu niteliği pekiştirme çekirdeğini destekler. Aynı ifade saymanın ilk basamağına da değindiği için dal korunabilir, ancak düzenli sayı kurma kullanımları ayrı sayı dalına bırakılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir tane; tek ve eşsiz"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yalnız bir, yalnız bir"}],"lexicalization_note":"Tanım yalın biçimdeki tek olma anlamını ve yinelemeli pekiştirmeyi ayrı yüzler olarak tutar; yinelemeyi yalın biçimin zorunlu anlamı yapmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en güçlü sınırlar mutlak birlik, alana bağlı eşsizlik, sayısal bir ve tek başına kalma dallarıyla kuruldu, kalanlar yalnız uzak konu ortaklığı taşıdığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal yalnız Tanrı'nın birliği çevresinde kuruludur; odak dal ise genel tek olmayı ve yinelemeli vurguyu da taşıdığı için bütünüyle onun yerine geçmez.","focus_only":"Odak dal genel tekliği, sayı başlangıcına değen kullanımı ve yinelemeli pekiştirmeyi de içerir.","gloss":"Tanrı'nın ortak ve benzerden uzak tekliği","neighbor_only":"Komşu dal Tanrı'nın birliği inancını, ortak bulunmamasını ve bölünmezliği daha geniş bir inanç alanı olarak işler.","neighbor_ref":"root_001631/B004","relation_type":"near_synonym","shared_zone":"İki dal da Tanrı için mutlak tekliği ve ortak bulunmamasını bildirir."},{"boundary_match":"partial","distinction":"Odak dalın tekliği varlığın bir tane veya mutlak eşsiz olmasıdır; komşu dalın eşsizliği ise belirli bir nitelik alanındaki karşılaştırmaya bağlıdır.","focus_only":"Odak dal sayısal birlik ve mutlak tek olma bildirebilir.","gloss":"belirli bir alanda benzeri bulunmayan","neighbor_only":"Komşu dal belirli bir üstünlük ya da kötülük alanında benzeri bulunmayan kişiyi anlatır.","neighbor_ref":"root_001240/B018","relation_type":"near_synonym","shared_zone":"İki dal da eş ya da benzer bulunmaması düşüncesinde buluşur."},{"boundary_match":"partial","distinction":"Odak dal nitelik olarak tekliği merkez alır; komşu dal ise birin sayı dizisindeki ve birleşik sayılardaki görevini merkez alır.","focus_only":"Odak dal varlığın tek ve eşi olmayan oluşunu, ayrıca bu niteliğin vurgulanmasını anlatır.","gloss":"bir sayısı ve onlu sayı kuruluşları","neighbor_only":"Komşu dal sayma dizisini, onlu sayı kuruluşlarını ve bir kümeyi on bire çıkarma işlemini kapsar.","neighbor_ref":"root_000017/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir tane olma düşüncesi ve sayının ilk basamağıyla bağ vardır."},{"boundary_match":"partial","distinction":"Odak dal bir nitelik bildirirken komşu dal tek başına kalma ya da ayrı ayrı hareket etme sürecini ve sonucunu bildirir.","focus_only":"Odak dal bir varlığın tek ya da eşsiz olma niteliğini bildirir.","gloss":"tek başına kalma ve birer birer dağılma","neighbor_only":"Komşu dal kişinin tek başına kalması veya bir topluluğun birer birer gelmesi gibi değişme ve dağılım olaylarını bildirir.","neighbor_ref":"root_000017/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da birlikten veya topluluktan ayrı tek olma görünümüne dokunur."}],"source_phrase_ar":"أحد فرع والأصل الواو وحد (maqayis); أحد بمعنى الواحد وهو أول العدد (sihah); قل هو الله أحد (sihah;mufradat); يستعمل مطلقا وصفا في وصف الله تعالى وأصله وحد (mufradat); أحد أحد (sihah)","source_summary":"Kaynakların ortak çizgisi tek olma düşüncesidir. Bu çizgi genel olarak bir tane olmayı, Tanrı için mutlak eşsizliği ve yineleme yoluyla yapılan güçlü vurguyu bir araya getirir; sayı başlangıcına ilişkin kayıt ise komşu sayı dalıyla sınır oluşturur.","sources":["MQ","SI","MU"],"what_is_ar":"أحد بمعنى الواحد، والوصف المطلق بأحد، وتكرار أحد أحد للتأكيد","what_is_not_ar":"ليس نفي الجنس ولا أحد عشر ولا يوم الأحد ولا جبل أُحُد"},"support_links":[]},{"boundary":"Bu dal yalnız olumsuz bağlamdaki kişi kapsamıdır; olumlu tekliği, sayı kuruluşlarını, gün adını ve dağ adını içermez.","branch_kind":"bare","branch_ref":"root_000017/B002","candidate_links":[{"candidate_id":"cand_b89460301149fc06534a","lane":"micro"},{"candidate_id":"cand_368099526a33a85262e9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:5:1","qac_word_ref":"89:25:5","surface_ar":"أَحَدٌ"}],"gloss":"hiç kimse","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Olumsuzluk altında konuşmaya konu olabilecek kişiler türünün tamamını kapsar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin yanı sıra iki veya daha çok kişinin varlığını ya da katılımını da dışlar."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir yerde hiç kimsenin bulunmadığını veya bir eylemi hiç kimsenin yapmadığını söyleyen cümlelerde gerçekleşir."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Olumsuzluk altında kişi türünün tamamını, sayı ayrımı yapmadan dışlayan doğal dal karşılığıdır.","boundary_detail":"Bu dal yalnız olumsuz bağlamdaki kişi kapsamıdır; olumlu tekliği, sayı kuruluşlarını, gün adını ve dağ adını içermez.","branch_image_ar":"استغراق النفي","concept_gloss":"hiç kimse","contextual_glosses":[{"applicability":"Bir yerde kişi bulunmadığını bildiren varlık cümlelerinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir eyleme katılmama gibi yer bildirmeyen olumsuz bağlamları kapsamaz.","preserves":"Kişilerin tümünü olumsuzluk altında dışlama kapsamını korur."},"facet_ids":["F001","F002","F003"],"text":"hiç kimse yok","usage_role":"contextual"},{"applicability":"Belirli bir insan topluluğunun hiçbir üyesinin eyleme katılmadığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Belirsiz bir yerde insan bulunmaması gibi topluluğu belirtilmeyen bağlamları kapsamaz.","preserves":"Belirli bir topluluğun bütün üyelerini olumsuzluk kapsamına alır."},"facet_ids":["F001","F002"],"text":"aranızdan hiç kimse","usage_role":"contextual"}],"definition":"Olumsuz bir cümlede, söz konusu olabilecek kişilerden bir tekinin bile bulunmadığını ya da eyleme katılmadığını bildirir. Kapsam yalnız bir kişiyi değil, iki ve daha çok kişiyi de dışarıda bırakır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Olumsuzluk altında konuşmaya konu olabilecek kişiler türünün tamamını kapsar."},{"facet_id":"F002","role":"specialization","statement":"Bir kişinin yanı sıra iki veya daha çok kişinin varlığını ya da katılımını da dışlar."},{"facet_id":"F003","role":"example","statement":"Bir yerde hiç kimsenin bulunmadığını veya bir eylemi hiç kimsenin yapmadığını söyleyen cümlelerde gerçekleşir."}],"identity_rationale":"Kaynak ifadesi, sözcüğün olumsuzluk içinde konuşmaya konu olabilecek kişilerin bütün türünü kapsadığını ve yalnız tek kişiyi değil iki ya da daha çok kişiyi de dışladığını açıkça belirtir. Hazırlanan dal çerçevesi bu kapsamı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"olumsuzlukta hiç kimse"}],"lexicalization_note":"Tanım yalın birimin olumsuz cümledeki kapsamına bağlıdır ve başka bir söz öbeğine özgü anlamı bu dala taşımaz.","neighbor_coverage_note":"Adayların tümü gözden geçirildi; yer boşluğunu bildiren kalıplar, daha geniş yokluk kalıbı ve olumlu teklik dalı okur açısından en yararlı karşıtlıkları verdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişi türünü olumsuzlukla kapsayan genel birimdir; komşu dal ise belirli kalıplaşmış sözlerle yerin boşluğunu, bazen de iz yokluğunu anlatır.","focus_only":"Odak dal olumsuzluk altında kişi türünün tamamını düzenli bir dil bilgisel kapsamla dışlar.","gloss":"bir yerde kimse ya da iz bulunmaması","neighbor_only":"Komşu dal, bir yerde insanın ya da kimi kullanımlarda herhangi bir izin bulunmadığını bildiren kalıplaşmış sözleri kapsar.","neighbor_ref":"root_000075/B008","relation_type":"near_neighbor","shared_zone":"İki dal da bir yerde kişinin bulunmadığını söyleyebilir."},{"boundary_match":"partial","distinction":"Odak dalın alanı kişilerdir; komşu dalın kalıplaşmış kullanımı kişi dışındaki şeylere ve suya kadar genişleyebilir.","focus_only":"Odak dal yalnız konuşmaya konu olabilecek kişilerin tümünü dışlar.","gloss":"en küçük kişi ya da şeyin bile yokluğu","neighbor_only":"Komşu dal kalıplaşmış bir sözle kişi, herhangi bir şey veya su gibi farklı varlıkların en küçüğünü bile dışlayabilir.","neighbor_ref":"root_000187/B005","relation_type":"near_neighbor","shared_zone":"İki dal da olumsuzlukta en küçük bir örneğin bile bulunmadığını bildirebilir."},{"boundary_match":"partial","distinction":"Odak dalın anlamı olumsuzluk ve bütün kişileri kapsama koşuluna bağlıdır; komşu dal olumlu tekliği veya eşsizliği anlatır.","focus_only":"Odak dal olumsuzluk altında herhangi bir kişinin varlığını ya da katılımını dışlar.","gloss":"bir tane, tek ve eşsiz","neighbor_only":"Komşu dal olumlu biçimde bir tane, tek veya eşi olmayan olmayı bildirir.","neighbor_ref":"root_000017/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalın biçiminde bir kişiye ya da varlığa ilişkin birlik düşüncesi bulunur."}],"source_phrase_ar":"لا أحد في الدار؛ ما في الدار أحد (sihah); أحد في النفي لاستغراق جنس الناطقين ولا واحد ولا اثنان فصاعدا (mufradat); فما منكم من أحد عنه حاجزين (sihah;mufradat)","source_summary":"Kaynaklar olumsuzluk içindeki kullanımın kişi türünü bütünüyle kapsadığı konusunda birleşir. Böylece söz yalnız tek bir kişinin yokluğunu değil, o türe giren herhangi bir sayıda kişinin bulunmamasını da bildirir.","sources":["SI","MU"],"what_is_ar":"أحد في سياق النفي لاستغراق جنس من يصلح أن يخاطب، فيشمل الواحد وما فوقه","what_is_not_ar":"ليس إثبات الواحد ولا العدد المركب ولا علم الجبل"},"support_links":["sup_ce21ccf4a2b54adc02c3","sup_e913edbee7a1d3f489d2"]},{"boundary":"Bu dal sayı ve sayı kurma alanındadır; olumsuz kişi kapsamını, mutlak eşsizliği, gün adını ve özel dağ adını içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_000017/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:5:1","qac_word_ref":"89:25:5","surface_ar":"أَحَدٌ"}],"gloss":"bir sayısı, onlu kuruluşları ve on bire çıkarma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sayma dizisinin başlangıcındaki bir sayısını bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir sayısı on veya yirmi gibi onluklarla birleşerek on bir ve yirmi bir türü sayıları kurar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Eylem biçimi, bir topluluğun sayısını on bire çıkarma işlemini bildirir."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın sayıyı, onluklarla kurulan sayı biçimlerini ve on bire çıkarma eylemini birlikte temsil eder.","boundary_detail":"Bu dal sayı ve sayı kurma alanındadır; olumsuz kişi kapsamını, mutlak eşsizliği, gün adını ve özel dağ adını içermez.","branch_image_ar":"الواحد في العد والتركيب","concept_gloss":"bir sayısı, onlu kuruluşları ve on bire çıkarma","contextual_glosses":[{"applicability":"Sayma dizisinin ilk sayısını yalın olarak bildiren bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Onluklarla kurulan sayıları ve on bire çıkarma eylemini kapsamaz.","preserves":"Bir sayısının sayma başlangıcındaki değerini korur."},"facet_ids":["F001"],"text":"bir","usage_role":"contextual"},{"applicability":"Bir sayısının on veya yirmiyle kurduğu birleşik ya da bağlı sayı örneklerinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalın bir sayısını ve bir topluluğu on bire çıkarma eylemini kapsamaz.","preserves":"Bir sayısının onluklarla birleşerek sayı kurmasını korur."},"facet_ids":["F002"],"text":"on bir ya da yirmi bir","usage_role":"contextual"},{"applicability":"Bir topluluğun sayısını on bire ulaştıran eylem biçiminin doğal karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalın sayıyı ve onluklarla kurulan sayı adlarını kapsamaz.","preserves":"Bir topluluğu on bire ulaştırma işlemini ve sonucunu korur."},"facet_ids":["F003"],"text":"on bire çıkarmak","usage_role":"contextual"}],"definition":"Saymanın başlangıcındaki bir sayısını, bu sayının on ve yirmi gibi onluklarla birleşerek kurduğu sayıları ve bir topluluğu on bire çıkarma işlemini kapsar. Yalın sayı, birleşik sayı ve yapma eylemi birbirinden ayrı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sayma dizisinin başlangıcındaki bir sayısını bildirir."},{"facet_id":"F002","role":"extension","statement":"Bir sayısı on veya yirmi gibi onluklarla birleşerek on bir ve yirmi bir türü sayıları kurar."},{"facet_id":"F003","role":"associated_use","statement":"Eylem biçimi, bir topluluğun sayısını on bire çıkarma işlemini bildirir."}],"identity_rationale":"Kaynak ifadesi bir sayısını saymanın başlangıcı olarak, on ve yirmi gibi onluklarla kurulan sayılarda bir bileşen olarak ve bir kümeyi on bire çıkaran eylem biçiminde açıkça sunar. Dal çerçevesi bu üç kullanımı doğru biçimde ayırarak bir arada tutar.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"saymanın başlangıcındaki bir"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"on bir, on bir dişil biçimi ve yirmi bir"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"onları on bire çıkarmak"}],"lexicalization_note":"Tanım yalın bir sayısını, onluklarla kurulan söz öbeklerini ve on bire çıkarma biçimini ayrı yüzler olarak gösterir; söz öbeği anlamını yalın biçime yaymaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; onluklar, üç sayısı, teklik dalı ve üçe tamamlama dalı sayı alanının en açıklayıcı sınırlarını verdi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal kuruluş içindeki bir bileşenini ve on bire çıkarma eylemini izler; komşu dal ise onluk sayıların kendisini ve çevresindeki biçimleri izler.","focus_only":"Odak dal bir sayısını, onluklara eklenmesini ve on bire çıkarma işlemini merkez alır.","gloss":"on ve onluk sayılar","neighbor_only":"Komşu dal on, yirmi ve bunlara komşu onluk sayı sözlerini merkez alır.","neighbor_ref":"root_001016/B001","relation_type":"same_field","shared_zone":"İki dal on bir ve yirmi bir gibi sayı kuruluşlarında birlikte görünür."},{"boundary_match":"field_only","distinction":"Ortak alan sayı sistemidir, ancak merkez sayılar ve bunlardan kurulan biçimler farklıdır; birbirlerinin yerine kullanılamazlar.","focus_only":"Odak dal bir sayısını ve onun onluklarla kurduğu biçimleri kapsar.","gloss":"üç sayısı ve bağlı biçimleri","neighbor_only":"Komşu dal üç sayısını, onun sıra, dağıtma, yüzlük ve binlik gibi geniş türevlerini kapsar.","neighbor_ref":"root_000203/B001","relation_type":"same_field","shared_zone":"İki dal sayı adlarını ve bu adların düzenli kuruluşlarını işler."},{"boundary_match":"partial","distinction":"Odak dal sayı dizisi ve sayı kuruluşuyla sınırlıdır; komşu dal nitelik olarak tekliği ve eşsizliği merkez alır.","focus_only":"Odak dal sayma, onluklarla sayı kurma ve bir kümeyi on bire çıkarma görevlerini kapsar.","gloss":"tek ve eşi olmayan olma","neighbor_only":"Komşu dal tek ve eşi olmayan olmayı, mutlak nitelemeyi ve yinelemeli pekiştirmeyi kapsar.","neighbor_ref":"root_000017/B001","relation_type":"near_neighbor","shared_zone":"İki dal bir tane olma ve saymanın ilk basamağı çevresinde temas eder."},{"boundary_match":"partial","distinction":"Odak dalın merkez sayısı bir ve onlu kuruluşlarıdır; komşu dalın merkez sayısı beş, sıra değeri beşinci ve tamamlama sonucu beştir.","focus_only":"Odak dal bir sayısını, onun onluklarla kurduğu sayıları ve bir topluluğu on bire çıkarma işlemini bildirir.","gloss":"beş, beşinci ve beşe tamamlama","neighbor_only":"Komşu dal beş sayısını, beşinci olmayı, beş kişiden birini ve bir topluluğu beşe tamamlamayı bildirir.","neighbor_ref":"root_000439/B001","relation_type":"near_neighbor","shared_zone":"İki dal sayı adı, sıra içindeki yer ve bir topluluğu belirli sayıya ulaştırma alanlarında temas eder."}],"source_phrase_ar":"أحد واثنان وأحد عشر وإحدى عشرة (sihah); الواحد المضموم إلى العشرات نحو أحد عشر وأحد وعشرين (mufradat); فأحدهن أي صيرهن أحد عشر (sihah)","source_summary":"Kaynakların ortak kaydı bir sayısının hem sayma dizisindeki yalın yerini hem de onluklarla kurduğu sayıları gösterir. Aynı kanıt, ayrı bir eylem biçiminde bir kümeyi on bire çıkarma sonucunu da korur.","sources":["SI","MU"],"what_is_ar":"أحد في العد، وتركيبه مع العشرات، وتصْيير المعدود أحد عشر","what_is_not_ar":"ليس نفي الجنس ولا الأحدية المطلقة ولا يوم الأحد"},"support_links":[]},{"boundary":"Ad öbeğindeki seçme veya ilk olma kullanımı ile haftanın gün adı ayrı yüzlerdir; sayı kuruluşları ve dağ adı bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000017/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:5:1","qac_word_ref":"89:25:5","surface_ar":"أَحَدٌ"}],"gloss":"iki kişiden biri, ilk olan ve haftanın ilk günü","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir ad öbeği içinde iki kişiden birini ayırır veya bağlama göre ilk olanı gösterir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gün sözüyle kurulan söz öbeği haftanın ilk gününü ve o günün özel adını bildirir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kaynak ifadesi haftanın bu gününe verilen adın çoğul biçimini de kaydeder."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ad öbeğindeki seçme ya da ilk olma işlevini ve gün adıyla sınırlı takvim kullanımını birlikte temsil eder.","boundary_detail":"Ad öbeğindeki seçme veya ilk olma kullanımı ile haftanın gün adı ayrı yüzlerdir; sayı kuruluşları ve dağ adı bu dala girmez.","branch_image_ar":"الأول والإضافة","concept_gloss":"iki kişiden biri, ilk olan ve haftanın ilk günü","contextual_glosses":[{"applicability":"İki kişilik bir topluluktan herhangi bir üyeyi ad öbeği içinde ayıran bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sıra bakımından ilk olmayı, gün adını ve gün adının çoğulunu kapsamaz.","preserves":"İki kişiden birini seçme işlevini korur."},"facet_ids":["F001"],"text":"ikinizden biri","usage_role":"contextual"},{"applicability":"Haftanın ilk gününün Türkçedeki yerleşik adını gerektiren takvim bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İki kişiden birini ayırma işlevini ve çoğul gün adı biçimini kapsamaz.","preserves":"Haftanın ilk gününün özel gün adı olma işlevini korur."},"facet_ids":["F002"],"text":"Pazar günü","usage_role":"contextual"},{"applicability":"Gün adının çoğul ya da yinelenen günler anlamındaki kullanımını karşılar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir günü ve iki kişiden birini ayırma işlevini kapsamaz.","preserves":"Gün adının çoğul kullanımını korur."},"facet_ids":["F003"],"text":"Pazar günleri","usage_role":"contextual"}],"definition":"Bir ad öbeğinin parçası olduğunda iki kişiden birini seçer veya bağlama göre ilk olanı bildirir. Gün adıyla kurulan kullanımda haftanın ilk gününü ve bu günün özel adını, ayrıca gün adının çoğul biçimini kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir ad öbeği içinde iki kişiden birini ayırır veya bağlama göre ilk olanı gösterir."},{"facet_id":"F002","role":"specialization","statement":"Gün sözüyle kurulan söz öbeği haftanın ilk gününü ve o günün özel adını bildirir."},{"facet_id":"F003","role":"source_variant","statement":"Kaynak ifadesi haftanın bu gününe verilen adın çoğul biçimini de kaydeder."}],"identity_rationale":"Kaynak ifadesi bir ad öbeği içinde bir kişiyi ayıran ya da ilk olanı bildiren kullanımla haftanın ilk gününün adını birlikte verir ve gün adının çoğulunu da kaydeder. Hazırlanan çerçeve kullanılabilir, ancak iki kişiden birini seçme anlamı her bağlamda sıra bakımından ilk olmayı zorunlu kılmaz.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ikinizden biri"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"Pazar günü"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"Pazar günleri"}],"lexicalization_note":"Tanım ad öbeğine bağlı seçme kullanımını, gün adı söz öbeğini ve gün adının çoğul biçimini ayırır; bunları yalın kökün tek bir genel anlamına dönüştürmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ilk olma alanındaki komşu ile üç farklı gün adı ve sayı dalı, dalın hem sıra hem takvim sınırlarını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ilk olma yüzü belirli ad öbeklerine ve gün adına bağlıdır; komşu dal ise nesnelerin ön, üst ve başlangıç bölümlerine uzanan daha geniş bir öncelik alanıdır.","focus_only":"Odak dal ad öbeğinde iki kişiden birini ayırmayı ve haftanın ilk gününün adını da kapsar.","gloss":"ön, üst ve ilk bölüm","neighbor_only":"Komşu dal bir nesnenin önü, üstü ya da başlangıcı gibi uzamsal ve sıralı öncelikleri geniş biçimde kapsar.","neighbor_ref":"root_000849/B002","relation_type":"near_neighbor","shared_zone":"İki dal sıra bakımından ilk veya önde olanı gösterebilir."},{"boundary_match":"field_only","distinction":"Ortak alan haftanın günleridir, ancak gösterdikleri günler farklıdır ve gün adları birbirinin yerine geçmez.","focus_only":"Odak dal haftanın ilk gününün adını ve bu adın çoğulunu kapsar.","gloss":"Salı günü","neighbor_only":"Komşu dal Salı gününün adını ve onun tekil ile çoğul biçimlerini kapsar.","neighbor_ref":"root_000203/B006","relation_type":"same_field","shared_zone":"İki dal haftanın belirli bir gününe verilen adı ve adın sayı biçimlerini işler."},{"boundary_match":"field_only","distinction":"Odak dal ilk güne, komşu dal beşinci güne işaret eder; ortak takvim alanına karşın gösterdikleri gün ayrıdır.","focus_only":"Odak dal haftanın ilk gününü ve adını bildirir.","gloss":"Perşembe günü","neighbor_only":"Komşu dal haftanın beşinci gününün yerleşik adını bildirir.","neighbor_ref":"root_000439/B004","relation_type":"same_field","shared_zone":"İki dal haftanın gün adları dizgesine aittir."},{"boundary_match":"field_only","distinction":"Aynı takvim alanındadırlar, fakat haftanın farklı günlerini gösterirler ve odak dal ayrıca ad öbeğinde birini ayırma işlevi taşır.","focus_only":"Odak dal haftanın ilk gününü, adını ve çoğul biçimini kapsar.","gloss":"Çarşamba günü","neighbor_only":"Komşu dal Çarşamba gününün adını, söyleniş ayrıntısını ve çoğulunu kapsar.","neighbor_ref":"root_000536/B010","relation_type":"same_field","shared_zone":"İki dal bir hafta gününün adı ve çoğul kullanımı çevresinde buluşur."},{"boundary_match":"partial","distinction":"Odak dal seçme, sıra ve gün adı yapılarıyla sınırlıdır; komşu dal sayma ve sayı oluşturma işlemleriyle sınırlıdır.","focus_only":"Odak dal ad öbeğinde bir kişiyi ayırma ve haftanın ilk gününü adlandırma işlevlerini taşır.","gloss":"bir sayısı ve onlu sayı kuruluşları","neighbor_only":"Komşu dal bir sayısını, onluklarla sayı kurmayı ve bir topluluğu on bire çıkarmayı taşır.","neighbor_ref":"root_000017/B003","relation_type":"near_neighbor","shared_zone":"İki dal bir ve ilk düşüncelerinde temas eder."}],"source_phrase_ar":"أن يستعمل مضافا أو مضافا إليه بمعنى الأول (mufradat); أما أحدكما (mufradat); يوم الأحد أي يوم الأول (mufradat); يوم الأحد يجمع على آحاد (sihah)","source_summary":"Kaynakların birleşik kaydı, ad öbeği içindeki birini ayırma veya ilk sayma işlevini haftanın ilk gününün adıyla ilişkilendirir. Gün adının çoğul biçimi de aynı kanıt içinde korunur.","sources":["SI","MU"],"what_is_ar":"أحد مضافا أو مضافا إليه بمعنى الأول، واسم يوم الأحد","what_is_not_ar":"ليس أحد عشر ولا لا أحد ولا جبل أُحُد"},"support_links":[]},{"boundary":"Bu dal tek başına kalma ve ayrı ayrı hareket etme olaylarıdır; sayısal biri, olumsuz kişi kapsamını ve özel adları içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_000017/B005","candidate_links":[{"candidate_id":"cand_368099526a33a85262e9","lane":"micro"},{"candidate_id":"cand_d7c42754a4625ca99dd6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:5:1","qac_word_ref":"89:25:5","surface_ar":"أَحَدٌ"}],"gloss":"tek başına kalma ve birer birer gelme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin bir işi başkalarından ayrı olarak üstlenmesini veya tek başına kalmasını bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir topluluğun üyelerinin toplu halde değil, ayrı ayrı ve birer birer gelmesini bildirir."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bireyin yalnızlaşmasını veya işi yalnız üstlenmesini ve topluluğun ayrı ayrı gelişini birlikte temsil eder.","boundary_detail":"Bu dal tek başına kalma ve ayrı ayrı hareket etme olaylarıdır; sayısal biri, olumsuz kişi kapsamını ve özel adları içermez.","branch_image_ar":"الانفراد والتفرق آحادا","concept_gloss":"tek başına kalma ve birer birer gelme","contextual_glosses":[{"applicability":"Bir kişinin başkalarından ayrılarak yalnız kalmasını bildiren bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir işi yalnız üstlenme ayrıntısını ve topluluğun birer birer gelişini kapsamaz.","preserves":"Bireyin başkalarından ayrı ve yalnız duruma gelmesini korur."},"facet_ids":["F001"],"text":"tek başına kalmak","usage_role":"contextual"},{"applicability":"Bir kişinin belirli bir işi başkalarının katılımı olmadan üstlendiği bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel tek başına kalmayı ve topluluğun ayrı ayrı gelişini kapsamaz.","preserves":"Bir işi başkalarından ayrı olarak üstlenme ilişkisini korur."},"facet_ids":["F001"],"text":"işi yalnız üstlenmek","usage_role":"contextual"},{"applicability":"Bir topluluğun üyelerinin toplu halde değil, ayrı ayrı geldiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bireyin bir işi yalnız üstlenmesini veya tek başına kalmasını kapsamaz.","preserves":"Ayrı ayrı ve birer birer geliş biçimini korur."},"facet_ids":["F002"],"text":"birer birer gelmek","usage_role":"contextual"}],"definition":"Bir kişinin bir işi başkalarından ayrı olarak yalnız üstlenmesi ya da tek başına kalmasıdır. Topluluk için kullanıldığında kişilerin toplu değil, ayrı ayrı ve birer birer gelmesini bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin bir işi başkalarından ayrı olarak üstlenmesini veya tek başına kalmasını bildirir."},{"facet_id":"F002","role":"extension","statement":"Bir topluluğun üyelerinin toplu halde değil, ayrı ayrı ve birer birer gelmesini bildirir."}],"identity_rationale":"Kaynak ifadesi kişinin bir işi yalnız üstlenmesi ya da tek başına kalması ile insanların ayrı ayrı, birer birer gelmesini açıkça birbirine bağlı iki kullanım olarak verir. Hazırlanan dal bu eylem ve dağılım ayrımını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"tek başına kalmak; işi yalnız üstlenmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"birer birer, ayrı ayrı"}],"lexicalization_note":"Tanım türemiş eylem biçimindeki yalnızlaşmayı ve yinelemeli dağılım sözündeki birer birer gelişi ayrı yüzler olarak tutar; ikisini yalın kök anlamı saymaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; yana çekilme, dağınık bulunma, yönlere dağılma ve benzeri az tek örnek dalları süreç ile nitelik sınırlarını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız üstlenme ile birer birer gelişe uzanır; komşu dal ise yana çekilme ve konumsal ayrılmayı daha belirgin biçimde taşır.","focus_only":"Odak dal bir işi yalnız üstlenmeyi ve topluluğun birer birer gelişini de kapsar.","gloss":"yana çekilme ve topluluktan ayrılma","neighbor_only":"Komşu dal topluluktan yana çekilmeyi, yer değiştirmeyi ve ayrı bir konumda bulunmayı kapsar.","neighbor_ref":"root_000305/B004","relation_type":"near_synonym","shared_zone":"İki dal bir kişinin topluluktan ayrılıp tek başına bulunmasını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal birer birer geliş biçimini ve bireysel yalnızlaşmayı belirtir; komşu dal yalnız topluluğun dağılmış durumunu kalıplaşmış biçimde bildirir.","focus_only":"Odak dal bireyin yalnızlaşmasını ve kişilerin birer birer gelişini kapsar.","gloss":"insanların dağılıp darmadağın olması","neighbor_only":"Komşu dal insanların genel olarak dağılmış ve darmadağın durumda bulunmasını anlatan kalıplaşmış bir sözdür.","neighbor_ref":"root_000154/B008","relation_type":"near_synonym","shared_zone":"İki dal bir topluluğun üyelerinin birlikte değil, dağınık durumda bulunmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal gelişin birer birer oluşunu ve bireysel yalnızlaşmayı da içerir; komşu dal yönlere dağılıp gitme olayına bağlıdır.","focus_only":"Odak dal tek başına kalmayı ve ayrı ayrı gelmeyi bildirir.","gloss":"farklı yönlere dağılıp gitmek","neighbor_only":"Komşu dal topluluğun farklı yönlere giderek dağılmasını bildiren kalıplaşmış bir anlatımdır.","neighbor_ref":"root_001331/B008","relation_type":"near_synonym","shared_zone":"İki dal bir topluluğun üyelerinin birbirinden ayrılarak dağılmasını kapsar."},{"boundary_match":"partial","distinction":"Odak dal insanların yalnızlaşma ya da ayrı ayrı hareket etme sürecini bildirir; komşu dal ise belirli bir hayvanın tek başına oluşunu adlandıran türle sınırlı bir kullanımdır.","focus_only":"Odak dal yalnızlaşma sürecini veya kişilerin ayrı ayrı hareket etmesini anlatır.","gloss":"topluluktan ayrı duran tek hayvan","neighbor_only":"Komşu dal belirli yaban hayvanlarının topluluktan ayrı duran tek üyesini adlandırır.","neighbor_ref":"root_000877/B009","relation_type":"near_neighbor","shared_zone":"İki dal bir canlının başkalarından ayrı ve tek başına bulunması düşüncesinde buluşur."}],"source_phrase_ar":"ما استأحدت بهذا الأمر أي ما انفردت به (maqayis); استأحد الرجل انفرد (sihah); جاءوا آحاد أحاد (sihah)","source_summary":"Kaynaklar tek başına kalma veya bir işi yalnız üstlenme anlamını birlikte destekler. Aynı kayıt, topluluğun üyelerinin ayrı ayrı ve birer birer gelişiyle bu çekirdeğin dağılımsal uzantısını da gösterir.","sources":["MQ","SI"],"what_is_ar":"الانفراد بالفعل، والمجيء آحادا أفرادا","what_is_not_ar":"ليس الواحد في العدد ولا نفي الجنس ولا علم الجبل"},"support_links":["sup_0ac2d4fc8ca44a7567d4","sup_e913edbee7a1d3f489d2"]},{"boundary":"Bu dal yalnız belirli bir dağın özel adıdır; tek olma, olumsuz kişi kapsamı, sayı, gün adı ve yalnızlaşma anlamlarını taşımaz.","branch_kind":"non_bare","branch_ref":"root_000017/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:5:1","qac_word_ref":"89:25:5","surface_ar":"أَحَدٌ"}],"gloss":"Medine'deki belirli bir dağın özel adı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir dağın özel adı olarak tek bir coğrafi varlığı gösterir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dağın yeri kaynakta Medine ile ilişkilendirilmiştir."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel dağ anlamı yüklemeden, kaynakta Medine'de bulunduğu belirtilen tek coğrafi varlığın özel ad işlevini açıklar.","boundary_detail":"Bu dal yalnız belirli bir dağın özel adıdır; tek olma, olumsuz kişi kapsamı, sayı, gün adı ve yalnızlaşma anlamlarını taşımaz.","branch_image_ar":"جبل أُحُد","concept_gloss":"Medine'deki belirli bir dağın özel adı","contextual_glosses":[{"applicability":"Dağın kimliği bağlamdan zaten biliniyorsa, adı yeniden üretmeden özel ad işlevini açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kaynakta belirtilen kentle kurulan yer bağını açıkça taşımaz.","preserves":"Belirli bir dağın özel adı olma işlevini korur."},"facet_ids":["F001"],"text":"o dağın özel adı","usage_role":"explanatory"}],"definition":"Medine'de bulunan belirli bir dağa verilen özel addır. Genel olarak dağ türünü ya da dağın bir niteliğini değil, tek bir coğrafi varlığın kimliğini gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir dağın özel adı olarak tek bir coğrafi varlığı gösterir."},{"facet_id":"F002","role":"specialization","statement":"Dağın yeri kaynakta Medine ile ilişkilendirilmiştir."}],"identity_rationale":"Kaynak ifadesi bu birimi genel bir dağ türü olarak değil, belirli bir kentteki tek bir dağın özel adı olarak tanımlar. Hazırlanan dalın özel yer adı çerçevesi bu kanıtla doğrudan uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"Medine'deki dağın özel adı"}],"lexicalization_note":"Tanım yalnız kaynakta belirlenen özel dağ adına bağlıdır ve bu yer adı kullanımından genel bir dağ ya da yalın kök anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; başka dağ ve yer adları yalnız alan ortaklığı düzeyinde karşılaştırıldı, anlamdaşlık kurulmadı ve en açıklayıcı üç özel ad adayı yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Özel ad işlevleri aynı olsa da gösterdikleri coğrafi varlıklar ayrıdır; adlar birbirinin yerine kullanılamaz.","focus_only":"Odak dal kaynakta belirtilen kentteki belirli bir dağı adlandırır.","gloss":"başka bir dağın özel adı","neighbor_only":"Komşu dal başka bir belirli dağa verilen ayrı özel adı kapsar.","neighbor_ref":"root_000706/B006","relation_type":"same_field","shared_zone":"İki dal da genel dağ türünü değil, belirli bir dağın özel adını bildirir."},{"boundary_match":"field_only","distinction":"Aynı özel ad türüne girseler de farklı kentlerdeki farklı dağları gösterirler; kimlikleri ortak değildir.","focus_only":"Odak dal kaynakta belirtilen kentteki belirli dağı gösterir.","gloss":"başka bir kentteki tanınmış dağın adı","neighbor_only":"Komşu dal başka bir kentteki tanınmış dağı gösteren ayrı bir özel addır.","neighbor_ref":"root_000314/B006","relation_type":"same_field","shared_zone":"İki dal da bir kentle ilişkilendirilen tanınmış dağın özel adıdır."},{"boundary_match":"field_only","distinction":"Odak dal tek bir dağa bağlıdır; komşu dalın adı birden çok yer biçimine ve birden çok coğrafi varlığa uygulanabilir.","focus_only":"Odak dal yalnız tek bir belirli dağın özel adıdır.","gloss":"dağ ve tepeler için kullanılan başka bir yer adı","neighbor_only":"Komşu dal aynı adla anılan birden çok yer, dağ veya tepeyi kapsayabilir.","neighbor_ref":"root_000602/B002","relation_type":"same_field","shared_zone":"İki dal coğrafi varlıkları gösteren özel yer adları alanındadır."}],"source_phrase_ar":"أحد جبل بالمدينة (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak tanıklığı, birimi Medine'deki belirli dağın özel adı olarak kaydeder."}],"source_summary":"Bu dal genel bir sözlük anlamından çok, tek bir coğrafi varlığı gösteren özel ad kullanımını kapsar. Kaynak kaydı, gösterilen varlığın Medine'de bulunan dağ olduğunu bildirir.","sources":["SI"],"what_is_ar":"اسم جبل بالمدينة","what_is_not_ar":"ليس معنى الواحد ولا النفي ولا الاستئحاد"},"support_links":[]},{"boundary":"Çekirdek tat ve tüketim hoşluğudur; cezalandırma, yeme içmeden kesilme ve sudaki yabancı madde bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","surface_ar":"عَذَابَ"}],"gloss":"tatlı ve kolay tüketilen yiyecek ya da içecek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yiyecek veya içeceğin damakta hoş, tatlı ve kolay tüketilir olmasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Su söz konusu olduğunda hoş içimin yanında tuzlu olmama niteliği belirgindir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli yapılarda tatlı su edinme veya arama ve bir şeyi tatlı sayma anlatılır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir ikili adlandırma tükürük ile şarabı birlikte bu hoşluk niteliği altında anar."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yiyecek ve içeceklerdeki ortak tat ve tüketim hoşluğu çekirdeğini, suyun tuzlu olmaması dahil, birlikte karşılar.","boundary_detail":"Çekirdek tat ve tüketim hoşluğudur; cezalandırma, yeme içmeden kesilme ve sudaki yabancı madde bu dala girmez.","branch_image_ar":"العذوبة والطيب في الماء والمطعوم","concept_gloss":"tatlı ve kolay tüketilen yiyecek ya da içecek","contextual_glosses":[{"applicability":"Suyun tuzlu olmayıp hoş ve kolay içilmesini anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka yiyecek ve içeceklere uzanan genel kapsamı dışarıda bırakır.","preserves":"Suyun tatlılığını ve hoş içimini eksiksiz korur."},"facet_ids":["F002"],"text":"tatlı ve içimi hoş su","usage_role":"contextual"},{"applicability":"Tatlı içme suyu bulma veya bir yerden böyle su sağlama yapılarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tatlı suyu amaç edinme ve onu sağlama işlemini korur."},"facet_ids":["F003"],"text":"tatlı su aramak","usage_role":"contextual"}],"definition":"Su başta olmak üzere bir yiyecek veya içeceğin tatlı, hoş ve kolay tüketilir olması; su için ayrıca tuzlu olmama niteliğini taşır. Bu niteliğe bağlı yapılar tatlı su edinmeyi, aramayı ya da bir şeyi tatlı saymayı anlatabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yiyecek veya içeceğin damakta hoş, tatlı ve kolay tüketilir olmasıdır."},{"facet_id":"F002","role":"specialization","statement":"Su söz konusu olduğunda hoş içimin yanında tuzlu olmama niteliği belirgindir."},{"facet_id":"F003","role":"associated_use","statement":"Belirli yapılarda tatlı su edinme veya arama ve bir şeyi tatlı sayma anlatılır."},{"facet_id":"F004","role":"source_variant","statement":"Bir ikili adlandırma tükürük ile şarabı birlikte bu hoşluk niteliği altında anar."}],"identity_rationale":"Yetkili ifade, suyun tatlı, hoş ve tuzlu olmayan niteliğini merkeze alırken kolay tüketilen başka yiyecek ve içecekleri de kapsar. Tatlı su arama, suyu tatlı bulma ve iki belirli sıvıyı birlikte adlandırma kullanımları bu niteliğe bağlı yan kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tatlı, hoş ve kolay tüketilir"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"tatlılık ve içim hoşluğu"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"suları tatlılaştı veya tatlı suya kavuştular"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"tatlı içme suyu aradılar veya sağladılar"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"onu tatlı saydı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"onun için şu kuyudan su çekilir"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birlikte anılan tükürük ve şarap"}],"lexicalization_note":"Tanım hem yalın nitelik bildiren biçimleri hem de tatlı su edinme, arama veya öyle sayma yapılarıyla sınırlı kullanımları ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tatlı su ve berrak içme suyu adayları sınırı en iyi gösterdiği için yayımlandı, ötekiler örnek, uzak alan veya aynı kökün ayrı dalıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal yalnız tatlı su alanında odak dalıyla örtüşür; odak dalının yiyecek-içecek genellemesi ve niteliğe bağlı işlemleri komşunun sınırını aşar.","focus_only":"Odak dalı su dışındaki kolay tüketilen yiyecek ve içecekleri, ayrıca tatlı su edinme ve değerlendirme yapılarını da kapsar.","gloss":"tatlı su","neighbor_only":null,"neighbor_ref":"root_001137/B001","relation_type":"near_synonym","shared_zone":"Her ikisi de tatlı, tuzlu olmayan ve hoş içilen suyu adlandırır."},{"boundary_match":"partial","distinction":"Odak dalında belirleyici eksen tatlılık ve tuzlu olmamadır; komşuda ise berraklıktan doğan içim kolaylığı öne çıkar.","focus_only":"Odak dalı berraklık şartı koymaz ve hoş tüketilen başka yiyecek ve içecekleri de kapsar.","gloss":"berrak ve kolay içilen su","neighbor_only":"Komşu dal içim kolaylığını özellikle suyun berraklığına bağlar.","neighbor_ref":"root_000638/B003","relation_type":"near_synonym","shared_zone":"Her ikisi de suyun zorlanmadan içilmesini ve damakta hoş olmasını kapsar."}],"source_phrase_ar":"عذب الماء عذوبة فهو عذب طيب (maqayis;ayn;tahdhib)؛ العذب ضد الملح وكل مستسيغ من طعام أو شراب (jamhara)؛ ماء عذب طيب بارد (mufradat)؛ استعذب القوم ماءهم إذا استقوه عذبا (sihah)","source_summary":"Kaynakların ortak çekirdeği tatlı, hoş ve kolay tüketilen su, yiyecek veya içecektir; su edinme, arama ve tatlı sayma kullanımları bu çekirdeğe bağlanır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الماء العذب الطيب والمستساغ من طعام أو شراب، والاستعذاب بمعنى طلب الماء العذب أو عده عذبا، وما ألحقته المصادر بالريق والخمر.","what_is_not_ar":"ليس العذاب والعقوبة، ولا الامتناع عن الأكل والشرب."},"support_links":[]},{"boundary":"Bu dal başkasını engellemekten değil, kişinin veya hayvanın fiilen yemeyip içmemesinden söz eder.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B002","candidate_links":[{"candidate_id":"cand_03799390abd25d641f25","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","surface_ar":"عَذَابَ"}],"gloss":"yemeden içmeden durma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan veya hayvan fiilen yiyecek ve içecek tüketmeden durur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvanda yememenin nedeni özellikle şiddetli susuzluk olabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hal, geceyi hiçbir şey yemeden ve içmeden geçirmek biçiminde anlatılabilir."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan veya hayvanın tüketmeme halini, nedeni ve süresi ayrıca belirtilebilen genel bir karşılıkla verir.","boundary_detail":"Bu dal başkasını engellemekten değil, kişinin veya hayvanın fiilen yemeyip içmemesinden söz eder.","branch_image_ar":"العذوب امتناع الجسد عن الأكل والشرب","concept_gloss":"yemeden içmeden durma","contextual_glosses":[{"applicability":"Şiddetli susuzluk yüzünden yemeyen hayvanın anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İçmeme bileşenini ve neden belirtilmeyen kullanımları açıkça söylemez.","preserves":"Susuzluğun yol açtığı yememe durumunu korur."},"facet_ids":["F002"],"text":"susuzluktan yemiyor","usage_role":"contextual"},{"applicability":"Tüketmeme halinin gece boyunca sürdüğünü anlatan yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yememeyi, içmemeyi ve gece boyunca sürmeyi birlikte korur."},"facet_ids":["F001","F003"],"text":"geceyi yemeden içmeden geçirdi","usage_role":"contextual"}],"definition":"Bir insanın veya hayvanın, çoğu kez şiddetli susuzluk yüzünden, hiçbir şey yemeden ve içmeden durmasıdır. Bu hal bir gece boyunca sürme veya yemek karşısında belirsiz bir ara durumda kalma biçiminde de anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan veya hayvan fiilen yiyecek ve içecek tüketmeden durur."},{"facet_id":"F002","role":"specialization","statement":"Hayvanda yememenin nedeni özellikle şiddetli susuzluk olabilir."},{"facet_id":"F003","role":"associated_use","statement":"Hal, geceyi hiçbir şey yemeden ve içmeden geçirmek biçiminde anlatılabilir."}],"identity_rationale":"Yetkili ifade hayvan ya da insanın yemeden ve içmeden durduğu bir hali açıkça bildirir. Şiddetli susuzluk sık bir neden olsa da tüm tanıklarda zorunlu değildir; bu yüzden hal, açlık duygusuna veya dinî oruca indirgenmez.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"susuzluktan yemedi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yiyip içmeden duran"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yiyip içmeden duran"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yemekten kaçınır"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"geceyi yemeden içmeden geçirdi"}],"lexicalization_note":"Tanım, hal bildiren biçimleri ve hayvanın, insanın ya da gecenin özne olduğu belirli yapıları ayırarak birlikte kapsar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; oruç, açlık ve aynı kökün alıkoyma dalı en olası karışmaları gösterir, öteki adaylar neden, sonuç veya daha uzak bedensel alanlardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bir canlıda gözlenen yememe-içmeme halidir; komşu ise iradeli veya kurallı bir kaçınma uygulamasını ve daha geniş yasak alanını anlatır.","focus_only":"Odak, hayvanda susuzluktan doğabilen ve amaç ya da kural gerektirmeyen bir tüketmeme halini de kapsar.","gloss":"oruç tutma","neighbor_only":"Komşu, amaçlı veya kurallı perhizde yiyecek ve içecek dışındaki yasaklardan da kaçınmayı kapsar.","neighbor_ref":"root_000894/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da belirli bir süre yiyecek ve içecekten uzak durma vardır."},{"boundary_match":"partial","distinction":"Açlık mide boşluğu ve duyumdur; odak ise açlık duyulsun ya da duyulmasın, yememe ve içmeme davranışının sürmesidir.","focus_only":"Odak, içmemeyi ve özellikle susuzluğun yemeyi durdurduğu hayvan davranışını da içerir.","gloss":"açlık","neighbor_only":"Komşu, boş midenin yarattığı açlık duyusunu ve aç kişi halini merkez alır.","neighbor_ref":"root_000278/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal yiyecek tüketilmemesiyle bağlantılı bedensel bir durumu anlatır."},{"boundary_match":"partial","distinction":"Odak sonucu oluşan yeme-içmeme halini adlandırır; komşu ise yönelinen şeyden çekilme veya birini çekme işlemini anlatır.","focus_only":"Odak, belirli bir nesneye yönelik iradeli vazgeçiş olmadan da görülen bedensel tüketmeme halidir.","gloss":"vazgeçme veya alıkoyma","neighbor_only":"Komşu, herhangi bir işten vazgeçmeyi veya başkasını o işten alıkoymayı kapsar.","neighbor_ref":"root_000994/B003","relation_type":"near_neighbor","shared_zone":"Yemekten uzak durma bağlamında iki dal yüzeyde birbirine yaklaşabilir."}],"source_phrase_ar":"عذب الحمار يعذب عذبا وعذوبا فهو عاذب وعذوب لا يأكل من شدة العطش (maqayis;ayn)؛ العذوب من الدواب وغيرها القائم الذي لا يأكل ولا يشرب (sihah)؛ بات عذوبا إذا لم يأكل شيئا ولم يشرب (tahdhib)","source_summary":"Tanıklıklar, insan veya hayvanın yemeyip içmediği hali ortaklaştırır; şiddetli susuzluk bunun belirgin fakat her kullanım için zorunlu olmayan nedenidir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه عذوب الحمار أو الفرس أو الرجل إذا لم يأكل ولم يشرب، خاصة من شدة العطش أو بوصف قائم لا يذوق شيئا.","what_is_not_ar":"ليس منع الغير عن الشيء ولا العذاب بمعنى العقوبة."},"support_links":["sup_42b4b708b9d33b2e7aba"]},{"boundary":"Dal, tüketmeme halini değil bir hedefe yönelişin kesilmesini veya kestirilmesini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B003","candidate_links":[{"candidate_id":"cand_03799390abd25d641f25","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","surface_ar":"عَذَابَ"}],"gloss":"vazgeçme veya alıkoyma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Özne yöneldiği bir şeyden vazgeçer veya geri durur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi başkasını bir işten uzak tutar veya o işi ona bıraktırır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Alıkoyma, birini bir işten sütten keser gibi kesme biçiminde anlatılabilir."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın dönüşlü ve ettirgen iki katılımcı düzenini kısa ve doğal biçimde birlikte karşılar.","boundary_detail":"Dal, tüketmeme halini değil bir hedefe yönelişin kesilmesini veya kestirilmesini anlatır.","branch_image_ar":"الكف والمنع والفطام عن الشيء","concept_gloss":"vazgeçme veya alıkoyma","contextual_glosses":[{"applicability":"Öznenin bir konuyu veya davranışı kendi isteğiyle bıraktığı yapılarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öznenin yöneldiği şeyden geri durmasını korur."},"facet_ids":["F001"],"text":"ondan vazgeçti","usage_role":"contextual"},{"applicability":"Bir kişinin başka bir kişiyi belirli bir işten uzak tuttuğu yapılarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ettirgen katılımcı düzenini ve engellenen işi korur."},"facet_ids":["F002"],"text":"onu bu işten alıkoydu","usage_role":"contextual"}],"definition":"Bir şeyden vazgeçip ona yönelmeyi bırakmak veya bir başkasını o şeyden uzak tutup alıkoymaktır. Sütten kesmeye benzer biçimde bir alışkanlığı ya da işi kestirmek bu ikinci yönün özel bir anlatımıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Özne yöneldiği bir şeyden vazgeçer veya geri durur."},{"facet_id":"F002","role":"core","statement":"Bir kişi başkasını bir işten uzak tutar veya o işi ona bıraktırır."},{"facet_id":"F003","role":"specialization","statement":"Alıkoyma, birini bir işten sütten keser gibi kesme biçiminde anlatılabilir."}],"identity_rationale":"Yetkili ifade hem öznenin bir şeyden vazgeçmesini hem de bir başkasını ondan alıkoymasını açıkça bir araya getirir. Bir işten kesme ve sütten kesmeye benzetilen uzaklaştırma bu yön değişiminin özel gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"o şeyden vazgeçti"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kadınlardan söz etmekten kaçının"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"onu o işten alıkoydu"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"onu o işten kesti"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"senden vazgeçtim"}],"lexicalization_note":"Anlam belirli edatlı ve ettirgen yapılara bağlıdır; öznenin vazgeçmesi ile başkasını alıkoyması tanımda ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel geri durma ile geniş engelleme alanları yayımlandı, daha dar tutma ve ayırma adayları bunlara göre yinelenen ya da uzak kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak, belirli yapılarda kendi vazgeçişiyle başkasını alıkoymayı eşler; komşu daha genel geri çekilme ve yüz çevirme alanına yayılır.","focus_only":"Odak, başkasını bir işten kesme ve sütten kesmeye benzer ettirgen alıkoyma kullanımını açıkça içerir.","gloss":"geri durma ve bırakma","neighbor_only":"Komşu, geri çekilmenin yanında bir işi bir yana bırakma ve evde kalma gibi daha geniş uzak durma görünümlerine uzanır.","neighbor_ref":"root_000906/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir şeye yönelişi kesme, ondan geri durma veya onu bırakma alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak yönelişin kesilmesine odaklanır; komşu ise fiziksel, hukuki veya kurumsal engel ve yasağı daha geniş bir çekirdek olarak taşır.","focus_only":"Odak, kişinin kendi isteğiyle vazgeçmesini ve kişisel bir ettirgen alıkoymayı kapsar.","gloss":"engelleme ve yasaklama","neighbor_only":"Komşu, giriş, çıkış veya eylem üzerinde engel, yasak, görevli ve yaptırım gibi kurumsal sınırlar da kurar.","neighbor_ref":"root_000002/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal bir kişinin belirli bir eylemi yapmasını önleme alanında buluşur."}],"source_phrase_ar":"أعذب عن الشيء إذا لها عنه وتركه (maqayis)؛ أعذب عن الشيء إذا امتنع عنه (jamhara;tahdhib)؛ أعذبته عن الأمر إذا منعته عنه (sihah)؛ عذبته تعذيبا كقولك فطمته عن هذا الأمر (ayn;tahdhib)","source_summary":"Ortak anlam, bir şeye yönelişi kesmektir; bu kesilme öznenin kendi vazgeçişi veya başka bir kişinin onu engellemesi biçiminde gerçekleşir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه أعذب عن الشيء إذا تركه أو امتنع عنه، وأعذب غيره أو عذبه إذا منعه، والفطام عن أمر، وصيغة أعذبوا عن النساء في الذكر.","what_is_not_ar":"ليس العذوبة في الماء، ولا العقوبة والإيجاع."},"support_links":["sup_42b4b708b9d33b2e7aba"]},{"boundary":"Genel çıplaklıktan daha dardır: belirleyici koşul, varlıkla gökyüzü arasındaki üst örtünün yokluğudur.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B004","candidate_links":[{"candidate_id":"cand_d7c42754a4625ca99dd6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","surface_ar":"عَذَابَ"}],"gloss":"gökyüzüne karşı örtüsüz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Varlık ile gökyüzü arasında onu örten hiçbir engel bulunmaz."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu durum geceyi gökyüzüne açık ve örtüsüz geçirme örneğiyle anlatılır."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Üstünde hiçbir örtü olmadan doğrudan gökyüzüne açık kalan kişi veya nesne için kullanılır.","boundary_detail":"Genel çıplaklıktan daha dardır: belirleyici koşul, varlıkla gökyüzü arasındaki üst örtünün yokluğudur.","branch_image_ar":"العذوب المكشوف للسماء","concept_gloss":"gökyüzüne karşı örtüsüz","contextual_glosses":[{"applicability":"Birinin geceyi üstünde dam veya örtü bulunmadan geçirdiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geceleme olayını ve gökyüzüne açık kalmayı korur."},"facet_ids":["F001","F002"],"text":"geceyi açıkta geçirdi","usage_role":"contextual"}],"definition":"Bir varlığın kendisiyle gökyüzü arasında hiçbir dam, örtü veya siper bulunmadan açıkta kalmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Varlık ile gökyüzü arasında onu örten hiçbir engel bulunmaz."},{"facet_id":"F002","role":"example","statement":"Bu durum geceyi gökyüzüne açık ve örtüsüz geçirme örneğiyle anlatılır."}],"identity_rationale":"Yetkili ifade, bir varlık ile gökyüzü arasında hiçbir örtü bulunmamasını doğrudan bildirir. Aynı biçimlerin yememe-içmeme dalında da bulunması bu mekânsal anlamı değiştirmez.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"gökyüzüne karşı örtüsüz olan"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"gökyüzüne karşı örtüsüz olan"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"geceyi gökyüzüne açık geçirdi"}],"lexicalization_note":"Yalın durum bildiren biçimler ile geceyi gökyüzüne açık geçirme yapısı aynı mekânsal çekirdek altında, yapı sınırları korunarak verilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel örtüsüzlük ile açık alan adayları sınırı en iyi gösterdi, öteki adaylar belirli yüzeyler, görünürlük veya uzak mekân ilişkileridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dikey olarak gökyüzüne açık kalma durumudur; komşu beden, yer ve hayvan üzerinde çok daha genel bir örtüsüzlük alanı kurar.","focus_only":"Odak özellikle üst örtünün yokluğunu ve gökyüzüne doğrudan açık olmayı şart koşar.","gloss":"çıplaklık ve örtüsüzlük","neighbor_only":"Komşu giysisizliği, genel örtüsüzlüğü, açık araziyi ve eyersiz hayvanı da kapsar.","neighbor_ref":"root_001004/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir varlığı örten veya gizleyen bir katmanın bulunmaması vardır."},{"boundary_match":"partial","distinction":"Odak kişinin veya nesnenin örtüsüz durumudur; komşu ise bulunulan yerin geniş ve açık oluşunu merkez alır.","focus_only":"Odak, yerdeki genişlikten bağımsız olarak bir varlığın üstünde örtü bulunmamasını anlatır.","gloss":"açık alan","neighbor_only":"Komşu, geniş ve açık bir alanı ve kişinin o alana çıkmasını adlandırır.","neighbor_ref":"root_000105/B002","relation_type":"near_neighbor","shared_zone":"Açık gökyüzü altında bulunma sahnesinde iki dal birlikte gerçekleşebilir."}],"source_phrase_ar":"العذوب الذي ليس بينه وبين السماء ستر وكذلك العاذب (maqayis;tahdhib)؛ فبات عذوبا للسماء كأنه سهيل (maqayis;tahdhib)","source_summary":"Tanıklıklar, gökyüzüyle kişi veya nesne arasında örtü bulunmayan açıkta kalma durumunda birleşir ve bunu geceleme örneğiyle gösterir.","sources":["MQ","TA"],"what_is_ar":"يدخل فيه العذوب أو العاذب الذي لا ستر بينه وبين السماء.","what_is_not_ar":"ليس مجرد الامتناع عن الطعام والشراب إلا حيث احتملته الشواهد."},"support_links":["sup_0ac2d4fc8ca44a7567d4"]},{"boundary":"Çekirdek ağır acı çektirme veya cezadır; her güçlük kendiliğinden bu dala girmez ve bildirilen dayak kökeni tanımın şartı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B005","candidate_links":[{"candidate_id":"cand_b89460301149fc06534a","lane":"micro"},{"candidate_id":"cand_368099526a33a85262e9","lane":"micro"},{"candidate_id":"cand_03799390abd25d641f25","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","surface_ar":"عَذَابَ"}],"gloss":"ağır acı çektirme ve cezalandırma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiye ağır acı verilir veya ağır bir ceza uygulanır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli bir yapı, bütünüyle yok etmeye yönelik cezayı anlatır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bildirilen bir görüş anlamı dayaktan başlatır ve sonra her ağır sıkıntıya genişletir."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem uygulanan ağır cezayı hem de birine şiddetli acı verme eylemini karşılayan çekirdek ifadedir.","boundary_detail":"Çekirdek ağır acı çektirme veya cezadır; her güçlük kendiliğinden bu dala girmez ve bildirilen dayak kökeni tanımın şartı değildir.","branch_image_ar":"العذاب إيلام وعقوبة","concept_gloss":"ağır acı çektirme ve cezalandırma","contextual_glosses":[{"applicability":"Eyleyenin başka bir kişiye şiddetli acı verdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eyleyeni, etkileneni ve ağır acının verilmesini korur."},"facet_ids":["F001"],"text":"ona ağır acı çektirdi","usage_role":"contextual"},{"applicability":"Cezanın hedefi bütünüyle ortadan kaldırmak olduğunda kullanılan özel karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Cezalandırmayı ve yok etmeye yönelik özel sonucu korur."},"facet_ids":["F002"],"text":"yok edici ceza","usage_role":"contextual"}],"definition":"Birine ağır acı çektirme veya onu ağır biçimde cezalandırmadır. Dayak kökeni ve anlamın her türlü ağır sıkıntıya yayılması, çekirdeğin parçası değil aktarılan bir açıklamadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiye ağır acı verilir veya ağır bir ceza uygulanır."},{"facet_id":"F002","role":"specialization","statement":"Belirli bir yapı, bütünüyle yok etmeye yönelik cezayı anlatır."},{"facet_id":"F003","role":"source_variant","statement":"Bildirilen bir görüş anlamı dayaktan başlatır ve sonra her ağır sıkıntıya genişletir."}],"identity_rationale":"Yetkili ifade ağır acı verme ve cezalandırma çekirdeğini doğrular. Bunun dayaktan türediği ve sonra her ağır sıkıntıya aktarıldığı açıklaması ortak zorunlu anlam değil, bildirilen bir köken ve genişleme görüşüdür; dal ancak bu kayıtla kabul edilebilir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"ağır acı ve ceza"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"ona ağır acı çektirdi veya ceza verdi"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yok edici ceza"}],"lexicalization_note":"Tanım ad, eylem ve yok etmeye yönelik ceza yapısını ayırır; yapıya bağlı özel ceza bütün dala genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; acı verme, acı duyma ve sınanma adayları temel sınırları gösterdi, diğerleri belirli ceza türleri veya daha uzak şiddet sahneleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak ağır acı ve ceza eksenindedir; komşu ise şiddet veya ceza şartı olmadan acı verme eylemini ve acı verici niteliği kapsar.","focus_only":"Odak, acı vermenin yanında ağır ceza uygulamayı ve cezayı ad olarak da kapsar.","gloss":"acı verme veya acı verici olma","neighbor_only":"Komşu, bir şeyin veya kişinin acı verici olduğunu nitelemeyi de kapsar.","neighbor_ref":"root_000046/B002","relation_type":"near_synonym","shared_zone":"İki dal da başka bir kişide acı meydana getirme alanında doğrudan örtüşür."},{"boundary_match":"partial","distinction":"Odak acının uygulanması ve cezalandırma yönündedir; komşu ise etkilenen kişinin acıyı hissetmesi durumudur.","focus_only":"Odak, acının bir başkasına uygulanmasını ve bunun ceza niteliği taşımasını içerir.","gloss":"acı duyma","neighbor_only":"Komşu, acıyı yaşayan kişinin bedensel veya ruhsal duyumunu merkez alır.","neighbor_ref":"root_000046/B001","relation_type":"near_neighbor","shared_zone":"Uygulanan ağır acı, etkilenen kişide acı duyumuna yol açar."},{"boundary_match":"partial","distinction":"Odakta acı verme ve ceza vardır; komşuda belirleyici unsur iyi veya kötü bir durumun sınama işlevi görmesidir.","focus_only":"Odak, birine ağır acı veya ceza uygulanmasını çekirdek edinir.","gloss":"sınanma ve sıkıntı","neighbor_only":"Komşu, sınanma niteliğindeki sıkıntıların yanında rahatlığı ve mal ya da çocuklarla sınanmayı da kapsar.","neighbor_ref":"root_001128/B004","relation_type":"near_neighbor","shared_zone":"Ağır sıkıntı veya ceza, iki dalın kesiştiği deneyim alanıdır."}],"source_phrase_ar":"العذاب يقال منه عذب تعذيبا وناس يقولون أصل العذاب الضرب ثم استعير ذلك في كل شدة (maqayis)؛ عذبت الرجل وغيره تعذيبا والاسم العذاب (jamhara)؛ العذاب العقوبة وقد عذبته تعذيبا (sihah)؛ العذاب هو الإيجاع الشديد (mufradat)","source_summary":"Ortak çekirdek ağır acı verme ve cezalandırmadır; dayak kökeni ile her ağır sıkıntıya yayılma ise zorunlu anlamdan ayrı, aktarılan bir açıklamadır.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه العذاب والعقوبة والإيجاع الشديد، والتعذيب، وما يذكره المصدر من أصل الضرب ثم استعارة كل شدة.","what_is_not_ar":"ليس الماء العذب ولا طرف السوط المسمى عذبة."},"support_links":["sup_42b4b708b9d33b2e7aba","sup_ce21ccf4a2b54adc02c3","sup_e913edbee7a1d3f489d2"]},{"boundary":"Dal, bir şeyin ince ucu veya ona bağlı sarkan parçadır; su kirliliği, ceza ve hayvanın ayakları bu kapsama girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","surface_ar":"عَذَابَ"}],"gloss":"ince uç veya sarkan bağlı parça","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kamçı veya dil gibi bir şeyin ince, dışa uzanan son bölümüdür."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir nesneye bağlanan veya ondan sarkan ip, kayış, bez ya da deri parçasıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ağaçta aynı biçimsel alan dışa uzanan dalı karşılar."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem doğal uçlarını hem de bir araca bağlanan ip, kayış, bez veya deri parçalarını kapsar.","boundary_detail":"Dal, bir şeyin ince ucu veya ona bağlı sarkan parçadır; su kirliliği, ceza ve hayvanın ayakları bu kapsama girmez.","branch_image_ar":"العذبة طرف أو علاقة متدلية","concept_gloss":"ince uç veya sarkan bağlı parça","contextual_glosses":[{"applicability":"Kamçının son bölümü ya da ona takılmış sarkan bağ anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kamçıya ait uç ve sarkan bağ seçeneklerini korur."},"facet_ids":["F001","F002"],"text":"kamçının ucu veya askısı","usage_role":"contextual"},{"applicability":"Ayakkabı bağı, eyer veya başka bir kayışın serbestçe sarkan ucunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kayışa bağlı olmayı, uç konumunu ve sarkmayı korur."},"facet_ids":["F002"],"text":"sarkan kayış ucu","usage_role":"contextual"}],"definition":"Bir nesnenin ince veya dışa uzanan ucu ya da ona bağlanıp sarkan ip, kayış, bez, deri veya dal parçasıdır. Belirli araç ve beden bölümlerinde parçanın yeri ve işlevi ayrıca belirlenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kamçı veya dil gibi bir şeyin ince, dışa uzanan son bölümüdür."},{"facet_id":"F002","role":"core","statement":"Bir nesneye bağlanan veya ondan sarkan ip, kayış, bez ya da deri parçasıdır."},{"facet_id":"F003","role":"extension","statement":"Ağaçta aynı biçimsel alan dışa uzanan dalı karşılar."}],"identity_rationale":"Yetkili ifade kamçı ve dil ucu gibi uçları; mızrağa bağlanan bez, teraziyi kaldıran ip, ayakkabı bağı ucu ve dal gibi uzanan ya da sarkan parçaları birlikte verir. Geçici çerçeve bu ortak biçimsel alanı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"kamçının ucu veya askısı"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"mızrak başına bağlanan bez"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"dilin ince ucu"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"teraziyi kaldıran ip"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"ağaç dalı"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"deve kamışının öndeki sivri ucu"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"ayakkabı bağının serbest ucu"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"kayışların uçları"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"eyerin arkasından sarkan deri parçası"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"ağıtçı kadının bezi"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"kamçıya askı yaptı"}],"lexicalization_note":"Anlam çoğunlukla belirtilen nesneyle kurulan yapılara bağlıdır; uç, bağ, bez, ip ve dal gerçekleşmeleri tek bir yalın ada indirgenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kamçı ve dil ucunu paylaşan aday ile sarkan bağ adayının ayrımı yayımlandı, diğerleri yalnız biçimsel benzerlik veya uzak parça ilişkisi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu uç ve çıkıntı çevresinde kalır; odak bu alanı aşarak çeşitli nesnelere bağlı veya onlardan sarkan ince parçaları da adlandırır.","focus_only":"Odak, uçların yanında mızrağa bağlanan bez, terazi ipi, dal ve sarkan kayış gibi bağlı parçaları da kapsar.","gloss":"uç veya uçtaki çıkıntı","neighbor_only":"Komşu, uçtaki belirgin düğüm veya çıkıntıyı özellikle öne çıkarır.","neighbor_ref":"root_000205/B005","relation_type":"near_synonym","shared_zone":"Kamçı ucu ve ona benzetilen dil ucu iki dalın doğrudan ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak uç ve bağlı ince parça düzenine dayanır; komşu saç örgüsü, en üst bölüm ve sarkan eklenti arasında daha geniş bir biçim alanı kurar.","focus_only":"Odak, araçların işlevli uçlarını ve terazi ipi ya da mızrak bezi gibi özel bağlı parçaları içerir.","gloss":"örgü, üst bölüm veya sarkan bağ","neighbor_only":"Komşu, saç örgüsünü ve bir şeyin en üst bölümünü de kapsar.","neighbor_ref":"root_000505/B009","relation_type":"near_neighbor","shared_zone":"Ayakkabı, kılıç veya eyerden sarkan bağ ve uzantılar iki dalda kesişir."}],"source_phrase_ar":"عذبة السوط طرفه (maqayis;tahdhib)؛ عذبة الرمح الخرقة التي تشد على رأسه (jamhara)؛ عذبة اللسان طرفه (jamhara;sihah;tahdhib)؛ عذبة الميزان الخيط الذي يرفع به (sihah;tahdhib)؛ عذبة الشجر غصنه (sihah;tahdhib)؛ عذبة شراك النعل المرسلة من الشراك (tahdhib)","source_summary":"Tanıklıklar uçta bulunan veya bir şeye bağlanıp sarkan ince parçaları ortaklaştırır; kamçı, dil, mızrak, terazi, ağaç ve ayakkabı bağı bunun belirli gerçekleşmeleridir.","sources":["MQ","JA","SI","TA"],"what_is_ar":"يدخل فيه طرف السوط واللسان، والخرقة أو السير المشدود، والخيط، والغصن، وأطراف السيور والشراك، وما كان من علاقة أو ذوابة متدلية.","what_is_not_ar":"ليس العذاب ولا العذوبة في الماء، ولا القوائم المسماة عذوبات الناقة."},"support_links":[]},{"boundary":"Bu dalın öğeleri genel kök anlamı gibi genişletilmemeli, birbirinin yerine geçebilen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtta verilen biçim veya bağlam sınırı içinde tutulmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","surface_ar":"عَذَابَ"}],"gloss":"yalıtık adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Suyun içinde çer çöp bulunur veya havuzun yüzeyini yosunsu bir tabaka kaplar."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Havuzdaki çer çöpü çıkarmak ya da yüzey tabakasını kırıp suyu görünür kılmak anlatılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ayrı bir yapı, su başının çevresinde otlak veya ot bulunmamasını bildirir."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki dağınık veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu dalın öğeleri genel kök anlamı gibi genişletilmemeli, birbirinin yerine geçebilen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtta verilen biçim veya bağlam sınırı içinde tutulmalıdır.","branch_image_ar":"العذبة شوائب الماء أو سطحه","concept_gloss":"yalıtık adlandırmalar","contextual_glosses":[{"applicability":"Suda bulunan küçük yabancı maddeler veya bunların çokluğu anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Suyun içindeki küçük yabancı maddeyi ve çokluk olasılığını korur."},"facet_ids":["F001"],"text":"sudaki çer çöp","usage_role":"contextual"},{"applicability":"Suyun kendisini değil, çevresinde hayvanların otlayacağı bitki bulunmamasını anlatan ayrı yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Su başını ve çevresindeki otlak yokluğunu birlikte korur."},"facet_ids":["F003"],"text":"çevresinde otlak bulunmayan su başı","usage_role":"explanatory"}],"definition":"Bir kullanım kümesi sudaki çer çöpü veya havuz yüzeyindeki yosunsu tabakayı ve bunların temizlenmesini anlatır. Ayrı bir kullanım ise bir su başının çevresinde otlak ve ot bulunmadığını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Suyun içinde çer çöp bulunur veya havuzun yüzeyini yosunsu bir tabaka kaplar."},{"facet_id":"F002","role":"associated_use","statement":"Havuzdaki çer çöpü çıkarmak ya da yüzey tabakasını kırıp suyu görünür kılmak anlatılır."},{"facet_id":"F003","role":"source_variant","statement":"Ayrı bir yapı, su başının çevresinde otlak veya ot bulunmamasını bildirir."}],"identity_rationale":"Bu dal packet düzeyinde inceleme statüsünde tutulmuş sınır-riskli malzemeyi taşır. Kanıt, tek bir yalın kök imgesinden çok biçime veya özel kullanıma bağlı dağınık adlandırmaları gösterdiği için dal yapısal bölme şartı koşmadan sınırlı bir adlandırma kümesi olarak okunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"sudaki çer çöp veya yüzey tabakası"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"çer çöpü bol su"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"havuzundaki çer çöpü çıkar"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"havuzun yüzey tabakasını kır"},{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"çevresinde otlak bulunmayan su başı"}],"lexicalization_note":"Kapsam verilen biçim veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"العذبة القذاة وماء ذو عذب أي كثير القذى (sihah)؛ أعذب حوضك أي انزع ما فيه من القذى (sihah)؛ اضرب عذبة الحوض حتى يظهر الماء أي اضرب عرمضه (tahdhib)؛ ماء ما به عذبة أي لا رعي فيه ولا كلأ (tahdhib)","source_summary":"İnceleme statüsündeki kanıt, tek bir birleşik anlamdan çok biçime veya özel bağlama bağlı sınırlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["SI","TA"],"what_is_ar":"يدخل فيه العذبة بمعنى القذاة في الماء، وكثرة القذى، وإزالة ما في الحوض من القذى أو عرمضه، مع شاهد تهذيب عن ماء لا رعي فيه ولا كلأ.","what_is_not_ar":"ليس الماء العذب الطيب؛ بل مادة غير مرغوبة أو محيطة بالماء."},"support_links":[]},{"boundary":"Dal tat, su veya içim hoşluğu değil, kişinin iyi ve cömert karakterini bildirir.","branch_kind":"bare","branch_ref":"root_000994/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","surface_ar":"عَذَابَ"}],"gloss":"iyi ve cömert huylu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi iyi, cömert ve değerli bir karakter taşır."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin ahlaki karakterinin iyi, cömert ve değerli olduğunu bildiren genel karşılıktır.","boundary_detail":"Dal tat, su veya içim hoşluğu değil, kişinin iyi ve cömert karakterini bildirir.","branch_image_ar":"العذبي كريم الأخلاق","concept_gloss":"iyi ve cömert huylu","contextual_glosses":[{"applicability":"Kişinin karakterini doğal bir ad öbeği içinde anlatmak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İyi huyu, cömertliği ve kişi niteliğini korur."},"facet_ids":["F001"],"text":"iyi huylu ve cömert biri","usage_role":"general"}],"definition":"İyi, cömert ve değerli huylara sahip kişi niteliğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi iyi, cömert ve değerli bir karakter taşır."}],"identity_rationale":"Yetkili ifade tek ve açık biçimde iyi, cömert ve değerli huylara sahip kişiyi niteler. Geçici çerçeve bu ahlaki kişilik niteliğini eksiksiz yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"iyi ve cömert huylu"}],"lexicalization_note":"Tanım yalnız yalın kişi niteliğini verir; komşu erdem adları veya belirli davranış kalıpları bu dala taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eşleşen iyi karakter dalı ile daha geniş erdemli olgunluk alanı yayımlandı, diğerleri cömertliğin özel görünümleri veya uzak kişi tipleridir.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kanıt sınırlarında iki dal arasında kapsam, katılımcı veya koşul farkı görünmez.","focus_only":null,"gloss":"iyi ve cömert huylu kişi","neighbor_only":null,"neighbor_ref":"root_001075/B003","relation_type":"synonym","shared_zone":"Her iki dal da kişiyi iyi ve cömert karakterli olması bakımından niteler."},{"boundary_match":"partial","distinction":"Odak yalın bir iyi ve cömert huy sıfatıdır; komşu daha geniş bir kişilik ve toplumsal olgunluk idealini adlandırır.","focus_only":"Odak doğrudan kişinin iyi ve cömert huylu oluşunu bildiren bir niteliktir.","gloss":"erdemli olgunluk","neighbor_only":"Komşu, toplumsal olarak kabul edilen insanlık ve olgunluk idealini ve bu niteliği edinme çabasını da kapsar.","neighbor_ref":"root_001409/B002","relation_type":"near_neighbor","shared_zone":"İyi karakter ve toplumca değer verilen davranış niteliği iki dalda kesişir."}],"source_phrase_ar":"العذبي الكريم الأخلاق (sihah)","source_summary":"Tek tanıklık kişiyi iyi ve cömert karakterli olarak niteleyen yalın bir sıfat anlamı verir.","sources":["SI"],"what_is_ar":"يدخل فيه وصف العذبي بمعنى الكريم الأخلاق.","what_is_not_ar":"ليس العذب بمعنى الطيب من الماء إلا من جهة اللفظ المشترك في المادة."},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_000994/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","surface_ar":"عَذَابَ"}],"gloss":"biçime bağlı adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Doğumdan sonra çocuğun ardından döl yatağından bir madde çıkar."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı bir biçim kadının döl yatağını, yani doğacak çocuğun geliştiği organı adlandırır."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"العذابة والرحم والخرج بعد الولد","concept_gloss":"biçime bağlı adlandırmalar","contextual_glosses":[{"applicability":"Çocuğun doğumunu izleyerek döl yatağından çıkan madde anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Maddenin doğumdan sonra ve döl yatağından çıkmasını korur."},"facet_ids":["F001"],"text":"doğumdan sonra çıkan madde","usage_role":"explanatory"},{"applicability":"Doğacak çocuğun geliştiği kadın organının doğrudan adlandırıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadına ait anatomik organ referentini korur."},"facet_ids":["F002"],"text":"kadının döl yatağı","usage_role":"contextual"}],"definition":"Bir anlam doğumdan sonra çocuğun ardından döl yatağından çıkan maddeyi bildirir. Ayrı bir anlam ise kadının döl yatağının kendisini adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Doğumdan sonra çocuğun ardından döl yatağından bir madde çıkar."},{"facet_id":"F002","role":"core","statement":"Ayrı bir biçim kadının döl yatağını, yani doğacak çocuğun geliştiği organı adlandırır."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_041","rendering_kind":"ordinary","target_gloss":"doğumdan sonra döl yatağından çıkan madde"},{"lexical_unit_id":"lu_042","rendering_kind":"ordinary","target_gloss":"kadının döl yatağı"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"العذب ما يخرج على أثر الولد من الرحم (tahdhib)؛ العذابة رحم المرأة (tahdhib)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["TA"],"what_is_ar":"يدخل فيه العذب الخارج على أثر الولد من الرحم، والعذابة بمعنى الرحم.","what_is_not_ar":"ليس العذاب ولا العذوبة ولا العذبة الطرفية."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["89:25:1"],"branch_refs":[],"candidate_id":"cand_86e5d2100f4d8462d909","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:1:boundary-shift","source_type":"word_analysis","support_ids":["sup_2203eb2a34f44baa074c","sup_411fe54e020f8b4ee718"],"title":"speech becomes judgment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:1","qac_refs":["89:25:1:1"],"status":"accepted"}},{"anchor_refs":["89:25:1"],"branch_refs":[],"candidate_id":"cand_6f1c60caee534f43fedb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:1:resultive-answer","source_type":"word_analysis","support_ids":["sup_411fe54e020f8b4ee718","sup_8c41d4024b20d5ef7647"],"title":"resultive answer","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:1","qac_refs":["89:25:1:1"],"status":"accepted"}},{"anchor_refs":["89:25:1"],"branch_refs":[],"candidate_id":"cand_3331ad58e4621a2ebd78","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:1:sequence-reprise","source_type":"word_analysis","support_ids":["sup_411fe54e020f8b4ee718","sup_b06747d7658d7e2cc22b"],"title":"judgment sequence reprise","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:1","qac_refs":["89:25:1:1"],"status":"accepted"}},{"anchor_refs":["89:25:1"],"branch_refs":[],"candidate_id":"cand_ce202688c94f17a55253","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:1:split-particle-fusion","source_type":"word_analysis","support_ids":["sup_411fe54e020f8b4ee718","sup_7896f7e0b220a9a9e4c9"],"title":"split particle fused to time","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:1","qac_refs":["89:25:1:1"],"status":"accepted"}},{"anchor_refs":["89:25:2"],"branch_refs":[],"candidate_id":"cand_9fa3abb7f8a547cfccc1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:2:deictic-known-day","source_type":"word_analysis","support_ids":["sup_b5435ea7ea3d7e21c896","sup_c9caa8c30d9d33ea513f"],"title":"known day by deixis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:2","qac_refs":["89:25:1:2"],"status":"accepted"}},{"anchor_refs":["89:25:2"],"branch_refs":[],"candidate_id":"cand_17980200d20968be0ce1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:2:earlier-reprise","source_type":"word_analysis","support_ids":["sup_70f7ee3958aad1233dfd","sup_c9caa8c30d9d33ea513f"],"title":"reprise from the arrival scene","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:2","qac_refs":["89:25:1:2"],"status":"accepted"}},{"anchor_refs":["89:25:2"],"branch_refs":[],"candidate_id":"cand_0f538b7a22b3fb952766","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:2:event-time-narrowing","source_type":"word_analysis","support_ids":["sup_20cd24721128fe32fe4a","sup_c9caa8c30d9d33ea513f"],"title":"day narrowed to event-time","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:2","qac_refs":["89:25:1:2"],"status":"accepted"}},{"anchor_refs":["89:25:2"],"branch_refs":[],"candidate_id":"cand_bc125a62e42f7428ff7f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:2:fronted-threshold","source_type":"word_analysis","support_ids":["sup_8a1054bc307cdbd61924","sup_c9caa8c30d9d33ea513f"],"title":"fronted threshold before negation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:2","qac_refs":["89:25:1:2"],"status":"accepted"}},{"anchor_refs":["89:25:2"],"branch_refs":[],"candidate_id":"cand_f4bd64437ecc460c622a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:2:judgment-field-concentration","source_type":"word_analysis","support_ids":["sup_7b42fdd120b637299681","sup_c9caa8c30d9d33ea513f"],"title":"judgment fields concentrate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:2","qac_refs":["89:25:1:2"],"status":"accepted"}},{"anchor_refs":["89:25:2"],"branch_refs":[],"candidate_id":"cand_138f3c620fecb076c810","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:2:sound-compressed-negation","source_type":"word_analysis","support_ids":["sup_c9caa8c30d9d33ea513f","sup_caeeb5e3c344c2501d5e"],"title":"sound compresses time into denial","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:2","qac_refs":["89:25:1:2"],"status":"accepted"}},{"anchor_refs":["89:25:2"],"branch_refs":[],"candidate_id":"cand_e819dd0574c4ffe7ee9d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:2:temporal-adverbial-frame","source_type":"word_analysis","support_ids":["sup_a924410ce4055fe8ccb9","sup_c9caa8c30d9d33ea513f"],"title":"temporal frame for punishment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:2","qac_refs":["89:25:1:2"],"status":"accepted"}},{"anchor_refs":["89:25:3"],"branch_refs":[],"candidate_id":"cand_6ff153f804de693d1c31","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:3:declarative-negated-predicate","source_type":"word_analysis","support_ids":["sup_246d08e6399679759a45","sup_596a0b9d1fc1c659ca5b"],"title":"declarative negated predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:3","qac_refs":["89:25:2:1"],"status":"accepted"}},{"anchor_refs":["89:25:3"],"branch_refs":[],"candidate_id":"cand_ccffe3cb36c02f3c4b93","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:3:incomparability-through-negation","source_type":"word_analysis","support_ids":["sup_246d08e6399679759a45","sup_a686ae37c5e1710db50d"],"title":"negated incomparability","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:3","qac_refs":["89:25:2:1"],"status":"accepted"}},{"anchor_refs":["89:25:3"],"branch_refs":[],"candidate_id":"cand_8ae74179acdf0dc6921b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:3:tightened-sound-onset","source_type":"word_analysis","support_ids":["sup_03bde9b83240275bc6df","sup_246d08e6399679759a45"],"title":"tightened negation onset","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:3","qac_refs":["89:25:2:1"],"status":"accepted"}},{"anchor_refs":["89:25:3"],"branch_refs":[],"candidate_id":"cand_5ad0a5af81f1e9e4f5fc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:3:whole-clause-scope","source_type":"word_analysis","support_ids":["sup_246d08e6399679759a45","sup_7f45ae05fa6a28cde0b1"],"title":"scope over act and measure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:3","qac_refs":["89:25:2:1"],"status":"accepted"}},{"anchor_refs":["89:25:4"],"branch_refs":[],"candidate_id":"cand_ac6c13ac1bd04f48aeff","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000994"],"scope":"focus_ayah","source_local_id":"89:25:4:cognate-measure-focus","source_type":"word_analysis","support_ids":["sup_d31cc2c9a3035665d6ac","sup_e02188a59b7868572df3"],"title":"act measured by its noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:4","qac_refs":["89:25:3:1"],"status":"accepted"}},{"anchor_refs":["89:25:4"],"branch_refs":[],"candidate_id":"cand_9ba3fcd3036b791f7eaf","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000994"],"scope":"focus_ayah","source_local_id":"89:25:4:form-cue-and-sound","source_type":"word_analysis","support_ids":["sup_7792df510e543a087d2b","sup_e02188a59b7868572df3"],"title":"doubling cue reinforces act","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:4","qac_refs":["89:25:3:1"],"status":"accepted"}},{"anchor_refs":["89:25:4"],"branch_refs":[],"candidate_id":"cand_043f0c15de859a58ec7a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000994"],"scope":"focus_ayah","source_local_id":"89:25:4:form-ii-punitive-act","source_type":"word_analysis","support_ids":["sup_919eb9e961d9a0f281bc","sup_e02188a59b7868572df3"],"title":"Form II punitive act","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:4","qac_refs":["89:25:3:1"],"status":"accepted"}},{"anchor_refs":["89:25:4"],"branch_refs":[],"candidate_id":"cand_2cd9eeb5447c35daa01b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000994"],"scope":"focus_ayah","source_local_id":"89:25:4:imperfect-at-that-day","source_type":"word_analysis","support_ids":["sup_a60ca68a4a910443a8d0","sup_e02188a59b7868572df3"],"title":"imperfect within the day","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:4","qac_refs":["89:25:3:1"],"status":"accepted"}},{"anchor_refs":["89:25:4"],"branch_refs":[],"candidate_id":"cand_972686c501cf90449d53","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000994"],"scope":"focus_ayah","source_local_id":"89:25:4:judgment-field-handoff","source_type":"word_analysis","support_ids":["sup_cb77831aa4df234f6651","sup_e02188a59b7868572df3"],"title":"life regret answered by punishment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:4","qac_refs":["89:25:3:1"],"status":"accepted"}},{"anchor_refs":["89:25:4"],"branch_refs":[],"candidate_id":"cand_8017ead274b1ebecbc31","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000994"],"scope":"focus_ayah","source_local_id":"89:25:4:paired-and-contrastive-formula","source_type":"word_analysis","support_ids":["sup_2fa0681d050cb252a1fb","sup_e02188a59b7868572df3"],"title":"paired judgment formula","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:4","qac_refs":["89:25:3:1"],"status":"accepted"}},{"anchor_refs":["89:25:4"],"branch_refs":[],"candidate_id":"cand_8d2bbc45956001e874eb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000994"],"scope":"focus_ayah","source_local_id":"89:25:4:qiraat-voice-pivot","source_type":"word_analysis","support_ids":["sup_e02188a59b7868572df3","sup_e4075c0a16fa6fadfda7"],"title":"voice pivot preserves measure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:4","qac_refs":["89:25:3:1"],"status":"accepted"}},{"anchor_refs":["89:25:4"],"branch_refs":[],"candidate_id":"cand_625aa7722b355479815b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000994"],"scope":"focus_ayah","source_local_id":"89:25:4:sweetness-branch-narrowed","source_type":"word_analysis","support_ids":["sup_aeb4be72aac47de49b5b","sup_e02188a59b7868572df3"],"title":"sweet branch inverted by context","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:4","qac_refs":["89:25:3:1"],"status":"accepted"}},{"anchor_refs":["89:25:5"],"branch_refs":[],"candidate_id":"cand_dd536c74d06df3dc8bb9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000994"],"scope":"focus_ayah","source_local_id":"89:25:5:cognate-accusative-measure","source_type":"word_analysis","support_ids":["sup_a26ac5745cb768f1a344","sup_c381dec0d14954a83761"],"title":"cognate measure not victim","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:5","qac_refs":["89:25:4:1","89:25:4:2"],"status":"accepted"}},{"anchor_refs":["89:25:5"],"branch_refs":[],"candidate_id":"cand_5f273f328eaafa49d5a3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000994"],"scope":"focus_ayah","source_local_id":"89:25:5:cross-ayah-measure-shift","source_type":"word_analysis","support_ids":["sup_a26ac5745cb768f1a344","sup_f5ceeeae55303d8d44e2"],"title":"instrument becomes measure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:5","qac_refs":["89:25:4:1","89:25:4:2"],"status":"accepted"}},{"anchor_refs":["89:25:5"],"branch_refs":[],"candidate_id":"cand_3f1bfafd2a2f5ae78ba2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000994"],"scope":"focus_ayah","source_local_id":"89:25:5:internal-root-recursion","source_type":"word_analysis","support_ids":["sup_1e96140b171a06718dca","sup_a26ac5745cb768f1a344"],"title":"punishment becomes its scale","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:5","qac_refs":["89:25:4:1","89:25:4:2"],"status":"accepted"}},{"anchor_refs":["89:25:5"],"branch_refs":[],"candidate_id":"cand_ac0a05977fa70a7c6307","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000994"],"scope":"focus_ayah","source_local_id":"89:25:5:life-horizon-answer","source_type":"word_analysis","support_ids":["sup_15f91673e4a4ff39ccda","sup_a26ac5745cb768f1a344"],"title":"life horizon answered","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:5","qac_refs":["89:25:4:1","89:25:4:2"],"status":"accepted"}},{"anchor_refs":["89:25:5"],"branch_refs":[],"candidate_id":"cand_b05cffb9e6869c39ad16","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000994"],"scope":"focus_ayah","source_local_id":"89:25:5:measure-before-closure","source_type":"word_analysis","support_ids":["sup_a26ac5745cb768f1a344","sup_c3ee1a8d716dc1a79bf2"],"title":"measure before universal closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:5","qac_refs":["89:25:4:1","89:25:4:2"],"status":"accepted"}},{"anchor_refs":["89:25:5"],"branch_refs":[],"candidate_id":"cand_b13a5c060b29a8bcdd37","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000994"],"scope":"focus_ayah","source_local_id":"89:25:5:paired-judgment-measures","source_type":"word_analysis","support_ids":["sup_5951e0390b17ed218969","sup_a26ac5745cb768f1a344"],"title":"paired judgment measures","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:5","qac_refs":["89:25:4:1","89:25:4:2"],"status":"accepted"}},{"anchor_refs":["89:25:5"],"branch_refs":[],"candidate_id":"cand_b460dd430ee8988fe9cb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000994"],"scope":"focus_ayah","source_local_id":"89:25:5:penal-branch-selected","source_type":"word_analysis","support_ids":["sup_a26ac5745cb768f1a344","sup_eac8b04492b051ae298c"],"title":"penal branch selected","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:5","qac_refs":["89:25:4:1","89:25:4:2"],"status":"accepted"}},{"anchor_refs":["89:25:5"],"branch_refs":[],"candidate_id":"cand_9fc2c9eb55425dda24d1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000994"],"scope":"focus_ayah","source_local_id":"89:25:5:possessed-standard","source_type":"word_analysis","support_ids":["sup_282916bab4b60e0c34b8","sup_a26ac5745cb768f1a344"],"title":"possessed punishment standard","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:5","qac_refs":["89:25:4:1","89:25:4:2"],"status":"accepted"}},{"anchor_refs":["89:25:5"],"branch_refs":[],"candidate_id":"cand_ef556e872481baae101d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000994"],"scope":"focus_ayah","source_local_id":"89:25:5:singular-measure","source_type":"word_analysis","support_ids":["sup_2646fae31aff3ace04cb","sup_a26ac5745cb768f1a344"],"title":"singular concentrated measure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:5","qac_refs":["89:25:4:1","89:25:4:2"],"status":"accepted"}},{"anchor_refs":["89:25:5"],"branch_refs":[],"candidate_id":"cand_1fd2752b0b04ac75c55c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000994"],"scope":"focus_ayah","source_local_id":"89:25:5:suffix-referent-pressure","source_type":"word_analysis","support_ids":["sup_a26ac5745cb768f1a344","sup_b15c36b28e8c905391e7"],"title":"suffix referent pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:5","qac_refs":["89:25:4:1","89:25:4:2"],"status":"accepted"}},{"anchor_refs":["89:25:5"],"branch_refs":[],"candidate_id":"cand_331821bc965a9f3f8d19","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000994"],"scope":"focus_ayah","source_local_id":"89:25:5:voice-stable-measure","source_type":"word_analysis","support_ids":["sup_a26ac5745cb768f1a344","sup_caece718f072bfdf477b"],"title":"measure stable across voice","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:5","qac_refs":["89:25:4:1","89:25:4:2"],"status":"accepted"}},{"anchor_refs":["89:25:6"],"branch_refs":[],"candidate_id":"cand_0b74d2d6a5eca7d42ed7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:6:acoustic-finality","source_type":"word_analysis","support_ids":["sup_2405f419703d04bd3de4","sup_a256e4a7903f5c6d03de"],"title":"acoustic finality","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:6","qac_refs":["89:25:5:1"],"status":"accepted"}},{"anchor_refs":["89:25:6"],"branch_refs":[],"candidate_id":"cand_7ebc455a9267df37438e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:6:delayed-final-closure","source_type":"word_analysis","support_ids":["sup_248a524398e96a337788","sup_a256e4a7903f5c6d03de"],"title":"delayed final closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:6","qac_refs":["89:25:5:1"],"status":"accepted"}},{"anchor_refs":["89:25:6"],"branch_refs":[],"candidate_id":"cand_99bfad18eafc6b451ac5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:6:distributive-singleness","source_type":"word_analysis","support_ids":["sup_a256e4a7903f5c6d03de","sup_f9277a93e0e3ce4ad236"],"title":"one-by-one exclusion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:6","qac_refs":["89:25:5:1"],"status":"accepted"}},{"anchor_refs":["89:25:6"],"branch_refs":[],"candidate_id":"cand_0db6e499049bb0e465ac","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:6:incomparability-after-measure","source_type":"word_analysis","support_ids":["sup_a256e4a7903f5c6d03de","sup_dfd5aa56e443de3b1646"],"title":"no comparator survives","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:6","qac_refs":["89:25:5:1"],"status":"accepted"}},{"anchor_refs":["89:25:6"],"branch_refs":[],"candidate_id":"cand_7b64f76548714b540f7e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:6:indefinite-under-negation","source_type":"word_analysis","support_ids":["sup_841e45fc49e6bbeccffc","sup_a256e4a7903f5c6d03de"],"title":"indefinite singular becomes total","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:6","qac_refs":["89:25:5:1"],"status":"accepted"}},{"anchor_refs":["89:25:6"],"branch_refs":[],"candidate_id":"cand_f911ec38edcbd9851678","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:6:paired-final-seal","source_type":"word_analysis","support_ids":["sup_a256e4a7903f5c6d03de","sup_d8f96ee9b71460fe2f1a"],"title":"paired final seal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:6","qac_refs":["89:25:5:1"],"status":"accepted"}},{"anchor_refs":["89:25:6"],"branch_refs":[],"candidate_id":"cand_6fc23b369ac28dd25321","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:6:regret-widened-to-universal","source_type":"word_analysis","support_ids":["sup_18a18c072a3b7000a174","sup_a256e4a7903f5c6d03de"],"title":"personal regret widened","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:6","qac_refs":["89:25:5:1"],"status":"accepted"}},{"anchor_refs":["89:25:6"],"branch_refs":[],"candidate_id":"cand_0726f15e7fbec519f4d6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:6:role-shifts-by-reading","source_type":"word_analysis","support_ids":["sup_3a70d0a2b49c0795c626","sup_a256e4a7903f5c6d03de"],"title":"role shifts while scope remains","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:6","qac_refs":["89:25:5:1"],"status":"accepted"}},{"anchor_refs":["89:25:6"],"branch_refs":[],"candidate_id":"cand_9f1de6dfc88b5a822863","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:25:6:uniqueness-field-inverted","source_type":"word_analysis","support_ids":["sup_a256e4a7903f5c6d03de","sup_bb469943e512f440326a"],"title":"uniqueness field inverted","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:25:6","qac_refs":["89:25:5:1"],"status":"accepted"}},{"anchor_refs":["89:25:3"],"branch_refs":[],"candidate_id":"cand_a48d7b3a9099dc6bbb1a","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000994"],"scope":"focus_ayah","source_local_id":"89:25:3:1","source_type":"qac_morpheme","support_ids":["sup_24b286d51d9b594ac6dc"],"title":"QAC root occurrence: ع ذ ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:25:5"],"branch_refs":[],"candidate_id":"cand_4d00b95737568445af77","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000017"],"scope":"focus_ayah","source_local_id":"89:25:5:1","source_type":"qac_morpheme","support_ids":["sup_57de24445af637293b46"],"title":"QAC root occurrence: ء ح د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:25"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:25","branch_refs":["root_000017/B002","root_000994/B005"],"candidate_id":"cand_b89460301149fc06534a","commentary_obligation":"review","hft_ref":"hft_cb9a310c82e1116e5b3c","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_incomparable_punishment","source_type":"hft","support_ids":["sup_ce21ccf4a2b54adc02c3"],"title":"baseline_incomparable_punishment","trust":"legacy_unbound"},{"anchor_refs":["89:25"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:25","branch_refs":["root_000017/B002","root_000017/B005","root_000994/B005"],"candidate_id":"cand_368099526a33a85262e9","commentary_obligation":"review","hft_ref":"hft_1a9f692669230044761f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_individual_exposure","source_type":"hft","support_ids":["sup_e913edbee7a1d3f489d2"],"title":"baseline_individual_exposure","trust":"legacy_unbound"},{"anchor_refs":["89:25"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:25","branch_refs":["root_000994/B002","root_000994/B003","root_000994/B005"],"candidate_id":"cand_03799390abd25d641f25","commentary_obligation":"review","hft_ref":"hft_5dc3bf083fd81d1ddb84","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_punishment_as_withholding","source_type":"hft","support_ids":["sup_42b4b708b9d33b2e7aba"],"title":"baseline_punishment_as_withholding","trust":"legacy_unbound"},{"anchor_refs":["89:25"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:25","branch_refs":["root_000017/B005","root_000994/B004"],"candidate_id":"cand_d7c42754a4625ca99dd6","commentary_obligation":"review","hft_ref":"hft_419ca9578176bc1b9ef6","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_uncovered_punishment","source_type":"hft","support_ids":["sup_0ac2d4fc8ca44a7567d4"],"title":"baseline_uncovered_punishment","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"89:25:1:1","qac_word_ref":"89:25:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"يَوْمَئِذ","morph_features":"STEM|POS:T|LEM:yawoma}i*","morpheme_role":"STEM","pos":"T","qac_ref":"89:25:1:2","qac_word_ref":"89:25:1","root_ar":"","surface_ar":"يَوْمَئِذٍ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"89:25:2:1","qac_word_ref":"89:25:2","root_ar":"","surface_ar":"لَّا"},{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","root_ar":"ع ذ ب","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","root_ar":"ع ذ ب","surface_ar":"عَذَابَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:25:4:2","qac_word_ref":"89:25:4","root_ar":"","surface_ar":"هُۥٓ"},{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:5:1","qac_word_ref":"89:25:5","root_ar":"ء ح د","surface_ar":"أَحَدٌ"}],"word_analysis_qac_refs":[["89:25:1:1"],["89:25:1:2"],["89:25:2:1"],["89:25:3:1"],["89:25:4:1","89:25:4:2"],["89:25:5:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["89:25:1","89:25:2","89:25:3","89:25:4","89:25:5","89:25:6"]},"focus_surface_evidence":{"arabic_uthmani":"فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"89:25:1:1","qac_word_ref":"89:25:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"يَوْمَئِذ","morph_features":"STEM|POS:T|LEM:yawoma}i*","morpheme_role":"STEM","pos":"T","qac_ref":"89:25:1:2","qac_word_ref":"89:25:1","root_ar":"","surface_ar":"يَوْمَئِذٍ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"89:25:2:1","qac_word_ref":"89:25:2","root_ar":"","surface_ar":"لَّا"},{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","root_ar":"ع ذ ب","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","root_ar":"ع ذ ب","surface_ar":"عَذَابَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:25:4:2","qac_word_ref":"89:25:4","root_ar":"","surface_ar":"هُۥٓ"},{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:5:1","qac_word_ref":"89:25:5","root_ar":"ء ح د","surface_ar":"أَحَدٌ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["89:25:1:1"],["89:25:1:2"],["89:25:2:1"],["89:25:3:1"],["89:25:4:1","89:25:4:2"],["89:25:5:1"]],"word_analysis_refs":["89:25:1","89:25:2","89:25:3","89:25:4","89:25:5","89:25:6"],"word_rows":[{"analysis_record_ref":"89:25:1","analytic_gloss_range_en":"resultive boundary particle joining the prior regret and judgment scene to the punishment clause","analytic_root_gloss_range_en":null,"qac_refs":["89:25:1:1"],"root":{},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"89:25:2","analytic_gloss_range_en":"deictic event-time, functioning as an accusative temporal frame for the punishment clause","analytic_root_gloss_range_en":"day can range from ordinary daylight to a marked event-time or the day-then construction; here the deictic judgment-event branch is selected","qac_refs":["89:25:1:2"],"root":{"arabic":"ي و م","transliteration":"y-w-m"},"surface":{"arabic":"يَوْمَئِذٍۢ","transliteration":"yawmaʾidhin"}},{"analysis_record_ref":"89:25:3","analytic_gloss_range_en":"declarative negator scoping over the imperfect punishment relation and the final indefinite","analytic_root_gloss_range_en":null,"qac_refs":["89:25:2:1"],"root":{},"surface":{"arabic":"لَّا","transliteration":"lā"}},{"analysis_record_ref":"89:25:4","analytic_gloss_range_en":"Form II imperfect punishment act under negation, with active agency in the standard reading and a passive qirāʾah contrast","analytic_root_gloss_range_en":"the root includes sweet freshness, abstention, withholding, exposedness, punishment, appendage, and other branches; the local Form II predicate selects the punishment and torment branch","qac_refs":["89:25:3:1"],"root":{"arabic":"ع ذ ب","transliteration":"ʿ-dh-b"},"surface":{"arabic":"يُعَذِّبُ","transliteration":"yuʿadhdhibu"}},{"analysis_record_ref":"89:25:5","analytic_gloss_range_en":"possessed verbal noun functioning as cognate measure or punishment standard, not an ordinary victim object","analytic_root_gloss_range_en":"the broad root includes sweet freshness and other branches, but this possessed verbal noun selects the punishment and penal consequence branch","qac_refs":["89:25:4:1","89:25:4:2"],"root":{"arabic":"ع ذ ب","transliteration":"ʿ-dh-b"},"surface":{"arabic":"عَذَابَهُۥٓ","transliteration":"ʿadhābahū"}},{"analysis_record_ref":"89:25:6","analytic_gloss_range_en":"indefinite singular under negation, functioning as final universal closure over possible participants","analytic_root_gloss_range_en":"oneness and single-individual range; under negation here it becomes distributive universal exclusion","qac_refs":["89:25:5:1"],"root":{"arabic":"أ ح د","transliteration":"ʾ-ḥ-d"},"surface":{"arabic":"أَحَدٌۭ","transliteration":"aḥadun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":6,"words_total":6,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["89:25"],"branch_refs":["root_000017/B002","root_000994/B005"],"candidate_id":"cand_b89460301149fc06534a","evidence_scope":"focus_ayah","hft_ref":"hft_cb9a310c82e1116e5b3c","item_id":"baseline_incomparable_punishment","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_incomparable_punishment","support_id":"sup_ce21ccf4a2b54adc02c3"},{"anchor_refs":["89:25"],"branch_refs":["root_000017/B002","root_000017/B005","root_000994/B005"],"candidate_id":"cand_368099526a33a85262e9","evidence_scope":"focus_ayah","hft_ref":"hft_1a9f692669230044761f","item_id":"baseline_individual_exposure","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_individual_exposure","support_id":"sup_e913edbee7a1d3f489d2"},{"anchor_refs":["89:25"],"branch_refs":["root_000994/B002","root_000994/B003","root_000994/B005"],"candidate_id":"cand_03799390abd25d641f25","evidence_scope":"focus_ayah","hft_ref":"hft_5dc3bf083fd81d1ddb84","item_id":"baseline_punishment_as_withholding","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_punishment_as_withholding","support_id":"sup_42b4b708b9d33b2e7aba"},{"anchor_refs":["89:25"],"branch_refs":["root_000017/B005","root_000994/B004"],"candidate_id":"cand_d7c42754a4625ca99dd6","evidence_scope":"focus_ayah","hft_ref":"hft_419ca9578176bc1b9ef6","item_id":"baseline_uncovered_punishment","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_uncovered_punishment","support_id":"sup_0ac2d4fc8ca44a7567d4"}],"diagnostics":[],"lane_counts":{"global":13,"macro":6,"micro":4},"packet_summary":{"ayah_count":30,"focus_ref":"89:25","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000702","furuq_root_norm":"س ر ي","furuq_source_root_norm":"س ر ي","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000697","furuq_root_norm":"س ر ر","furuq_source_root_norm":"س ر ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ع و د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":true,"target_occurrences":35,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ج و ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000273","furuq_root_norm":"ج و ب","furuq_source_root_norm":"ج و ب","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000283","furuq_root_norm":"ج ي ب","furuq_source_root_norm":"ج ي ب","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000220","furuq_root_norm":"ج ب ي","furuq_source_root_norm":"ج ب ي","is_dominant":false,"target_occurrences":2,"target_rank":3},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000214","furuq_root_norm":"ج ب ب","furuq_source_root_norm":"ج ب ب","is_dominant":false,"target_occurrences":1,"target_rank":4}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ب ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000153","furuq_root_norm":"ب ل و","furuq_source_root_norm":"ب ل و","is_dominant":true,"target_occurrences":28,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000154","furuq_root_norm":"ب ل ي","furuq_source_root_norm":"ب ل ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ه و ن","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001453","furuq_root_norm":"م ه ن","furuq_source_root_norm":"م ه ن","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001608","furuq_root_norm":"ه و ن","furuq_source_root_norm":"ه و ن","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001687","furuq_root_norm":"و ه ن","furuq_source_root_norm":"و ه ن","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14","89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"89:25","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"89:25","lane":"micro","linguistic_source_ref":"89:25","surface_ref":"89:25","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"89:25","target_tokens":[["O",["89:25:1"]],["gün",["89:25:1"]],["hiç",["89:25:5"]],["kimse",["89:25:5"]],["onun",["89:25:4"]],["azabı",["89:25:4"]],["gibi",["89:25:4"]],["azap",["89:25:3"]],["edemez",["89:25:2","89:25:3"]]],"text":"O gün hiç kimse onun azabı gibi azap edemez."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":15,"ayah_to":30,"id":"s089-p02-015-030","label":"The wealth test, judgment, and tranquil soul","number":2,"refs":["89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:3:tightened-sound-onset","source_type":"word_analysis","support_id":"sup_03bde9b83240275bc6df","text":"{\"blocking_evidence\":null,\"headline\":\"tightened negation onset\",\"reader_payoff\":\"The reader hears the negation clamp onto the clause immediately after the time-marker.\",\"reason\":\"The surface form records assimilation at the onset of the negator, reinforcing the transition from temporal threshold to denial.\",\"representative_source_ids\":[\"QF-b765fe1a\",\"QP-a2b2828d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:5:life-horizon-answer","source_type":"word_analysis","support_id":"sup_15f91673e4a4ff39ccda","text":"{\"blocking_evidence\":null,\"headline\":\"life horizon answered\",\"reader_payoff\":\"The reader notices that the life the human failed to prepare for is answered by the punishment measure now disclosed.\",\"reason\":\"The punishment measure follows immediately after the quoted regret about life in 89:24.\",\"representative_source_ids\":[\"QB-244e644d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:6:regret-widened-to-universal","source_type":"word_analysis","support_id":"sup_18a18c072a3b7000a174","text":"{\"blocking_evidence\":null,\"headline\":\"personal regret widened\",\"reader_payoff\":\"The reader notices the scene expand from one regretful human voice in 89:24 to a universal comparison in 89:25.\",\"reason\":\"The local final indefinite closes a judgment-day punishment clause after the individual quoted regret.\",\"representative_source_ids\":[\"QI-74738eeb\",\"QB-f331e443\",\"QT-5cdaec7f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:5:internal-root-recursion","source_type":"word_analysis","support_id":"sup_1e96140b171a06718dca","text":"{\"blocking_evidence\":null,\"headline\":\"punishment becomes its scale\",\"reader_payoff\":\"The reader hears the act and its measure answer each other before the clause reaches any possible rival.\",\"reason\":\"The same root appears in the governing verb and the following verbal noun, giving the comparison internal cognate force.\",\"representative_source_ids\":[\"QS-7c70e968\",\"QF-a5c40713\",\"ME-e29d6577\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:2:event-time-narrowing","source_type":"word_analysis","support_id":"sup_20cd24721128fe32fe4a","text":"{\"blocking_evidence\":null,\"headline\":\"day narrowed to event-time\",\"reader_payoff\":\"The reader notices a bounded occasion of accountability, not ordinary daylight duration.\",\"reason\":\"V4 preserves ordinary day, open time-span, event-day, and day-then branches; local punishment context and the deictic compound select the judgment-event branch.\",\"representative_source_ids\":[\"QS-05df5d22\",\"QS-2c6dd4d0\",\"MS-c993fb3f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:1:boundary-shift","source_type":"word_analysis","support_id":"sup_2203eb2a34f44baa074c","text":"{\"blocking_evidence\":null,\"headline\":\"speech becomes judgment\",\"reader_payoff\":\"The reader notices the scene change from the condemned person's private wish in 89:24 to an impersonal judgment assertion in 89:25.\",\"reason\":\"The particle links across the ayah boundary while the following clause changes from quoted regret to external judgment narration.\",\"representative_source_ids\":[\"QT-6dbb013e\",\"QB-df265655\",\"QS-13bbc24a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:6:acoustic-finality","source_type":"word_analysis","support_id":"sup_2405f419703d04bd3de4","text":"{\"blocking_evidence\":null,\"headline\":\"acoustic finality\",\"reader_payoff\":\"The reader hears the final indefinite ending as part of the paired closure across 89:25-26.\",\"reason\":\"The local noun ends with tanwīn and the next ayah repeats the same closure pattern.\",\"representative_source_ids\":[\"QP-963ea7ad\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:3","source_type":"word_analysis","support_id":"sup_246d08e6399679759a45","text":"{\"gloss_range\":\"declarative negator scoping over the imperfect punishment relation and the final indefinite\",\"prose\":\"{{ar:لَّا}} ({{tr:lā}}) negates the punishment relation as a declaration, not as a command or prohibition. Its scope reaches {{ar:يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ}} ({{tr:yuʿadhdhibu ʿadhābahū aḥadun}}) as one relation: act, owned measure, and possible participant all fall inside the denial. Because the final {{ar:أَحَدٌۭ}} ({{tr:aḥadun}}) is indefinite, the particle does more than deny ordinary occurrence; it empties the field of any comparable punisher in the active reading, and the accepted passive reading keeps the same universal exclusion with the role reassigned. Its tightened surface after the preceding time-marker makes the negation sound like a clamp on the whole punishment clause.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَّا}} ({{tr:lā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:6:delayed-final-closure","source_type":"word_analysis","support_id":"sup_248a524398e96a337788","text":"{\"blocking_evidence\":null,\"headline\":\"delayed final closure\",\"reader_payoff\":\"The reader waits until the last word for the possible candidate, only to hear that candidate erase every rival or comparable case.\",\"reason\":\"QAC and attachment identify the word as delayed nominative subject in the active reading, closing the verb-noun sequence.\",\"representative_source_ids\":[\"QG-812d5b01\",\"QT-cecc69a8\",\"MT-83f48355\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:25:3:1","source_type":"qac_morpheme","support_id":"sup_24b286d51d9b594ac6dc","text":"{\"lemma_ar\":\"عَذَّبَ\",\"morph_features\":\"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"89:25:3:1\",\"qac_word_ref\":\"89:25:3\",\"root_ar\":\"ع ذ ب\",\"surface_ar\":\"يُعَذِّبُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:5:singular-measure","source_type":"word_analysis","support_id":"sup_2646fae31aff3ace04cb","text":"{\"blocking_evidence\":null,\"headline\":\"singular concentrated measure\",\"reader_payoff\":\"The reader notices a single incomparable punishment standard rather than a plural list of penalties.\",\"reason\":\"The local noun is a singular possessed verbal noun.\",\"representative_source_ids\":[\"QF-e01d322c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:5:possessed-standard","source_type":"word_analysis","support_id":"sup_282916bab4b60e0c34b8","text":"{\"blocking_evidence\":null,\"headline\":\"possessed punishment standard\",\"reader_payoff\":\"The reader notices that the comparison turns on a possessed standard, not an unspecified kind of torment.\",\"reason\":\"QAC and attachment evidence mark the verbal noun with an attached third-person possessive suffix in an iḍāfa relation.\",\"representative_source_ids\":[\"QG-0c4ab785\",\"QG-936309aa\",\"MS-1a85d8be\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:4:paired-and-contrastive-formula","source_type":"word_analysis","support_id":"sup_2fa0681d050cb252a1fb","text":"{\"blocking_evidence\":null,\"headline\":\"paired judgment formula\",\"reader_payoff\":\"The reader sees that 89:25 measures punishment through verb-noun repetition and then sets up the matched binding clause of 89:26.\",\"reason\":\"The CRITICAL rows provide concrete references to 88:24 and 89:26, and the local word order supports the matched negative formula.\",\"representative_source_ids\":[\"QI-8ebebcca\",\"QI-d3cb477b\",\"MT-c59b664b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:6:role-shifts-by-reading","source_type":"word_analysis","support_id":"sup_3a70d0a2b49c0795c626","text":"{\"blocking_evidence\":null,\"headline\":\"role shifts while scope remains\",\"reader_payoff\":\"The reader notices that the same final word can exclude a rival punisher in the active reading or a comparable punished case in the passive reading.\",\"reason\":\"QAC notes the passive qirāʾah and gives the active reading as standard; the role contrast is therefore retained as a qualified apparatus payoff.\",\"representative_source_ids\":[\"QG-c1d61d6c\",\"QS-0e4feeb4\",\"MF-cf8160df\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:1","source_type":"word_analysis","support_id":"sup_411fe54e020f8b4ee718","text":"{\"gloss_range\":\"resultive boundary particle joining the prior regret and judgment scene to the punishment clause\",\"prose\":\"{{ar:فَ}} ({{tr:fa}}) makes the ayah arrive as consequence, not as a detached doctrine about punishment. It carries the human regret of 89:24 and the wider judgment sequence of 89:21-24 into the timed denial that follows. Because the particle is split analytically from {{ar:يَوْمَئِذٍۢ}} ({{tr:yawmaʾidhin}}) while fused at the surface, the opening lets consequence and time-marker move together: the lament gives way to a public judgment statement before the punishment comparison is even named.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:25:5:1","source_type":"qac_morpheme","support_id":"sup_57de24445af637293b46","text":"{\"lemma_ar\":\"أَحَد\",\"morph_features\":\"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"89:25:5:1\",\"qac_word_ref\":\"89:25:5\",\"root_ar\":\"ء ح د\",\"surface_ar\":\"أَحَدٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:5:paired-judgment-measures","source_type":"word_analysis","support_id":"sup_5951e0390b17ed218969","text":"{\"blocking_evidence\":null,\"headline\":\"paired judgment measures\",\"reader_payoff\":\"The reader notices that punishment and binding become matched measures across 89:25-26.\",\"reason\":\"The local noun sits between the day-marker and final universal exclusion, and the next ayah repeats the same formula with binding.\",\"representative_source_ids\":[\"QB-481ddc2a\",\"QY-9a35435d\",\"QI-e6ac5be3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:3:declarative-negated-predicate","source_type":"word_analysis","support_id":"sup_596a0b9d1fc1c659ca5b","text":"{\"blocking_evidence\":null,\"headline\":\"declarative negated predicate\",\"reader_payoff\":\"The reader notices that the ayah is declaring the impossibility of comparable punishment at that day, not commanding anyone not to punish.\",\"reason\":\"QAC marks a negative particle governing the imperfect verb, and the time value is supplied by the temporal frame and predicate context.\",\"representative_source_ids\":[\"QG-0507fd8a\",\"MG-796f31ff\",\"QS-c549c000\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:2:earlier-reprise","source_type":"word_analysis","support_id":"sup_70f7ee3958aad1233dfd","text":"{\"blocking_evidence\":null,\"headline\":\"reprise from the arrival scene\",\"reader_payoff\":\"The reader sees 89:25 tied back to the bringing of Hell in 89:23, so regret and punishment comparison remain one judgment threshold.\",\"reason\":\"The input cross-reference marks this formulaic time-marker as a reprise, and the CRITICAL rows give the concrete 89:23 anchor.\",\"representative_source_ids\":[\"QI-631cddcc\",\"MI-9acbc471\",\"QE-7c95a6de\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:4:form-cue-and-sound","source_type":"word_analysis","support_id":"sup_7792df510e543a087d2b","text":"{\"blocking_evidence\":null,\"headline\":\"doubling cue reinforces act\",\"reader_payoff\":\"The reader hears and sees the punitive root tighten in the verb before it returns as the punishment measure.\",\"reason\":\"The local Form II stem supplies the visible doubling, and the following cognate noun repeats the same root.\",\"representative_source_ids\":[\"QF-e9d88479\",\"QP-d015ec4f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:1:split-particle-fusion","source_type":"word_analysis","support_id":"sup_7896f7e0b220a9a9e4c9","text":"{\"blocking_evidence\":null,\"headline\":\"split particle fused to time\",\"reader_payoff\":\"The reader sees that the opening is not merely a date phrase; consequence is carried by the particle and time is carried by the following compound.\",\"reason\":\"The alignment splits the prefixed particle from the temporal noun, while the surface unit keeps them adjacent.\",\"representative_source_ids\":[\"MG-6270bdc5\",\"QF-2e877f73\",\"QT-3dee7d40\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:2:judgment-field-concentration","source_type":"word_analysis","support_id":"sup_7b42fdd120b637299681","text":"{\"blocking_evidence\":null,\"headline\":\"judgment fields concentrate\",\"reader_payoff\":\"The reader notices that the day-marker transfers authority from the human's speech to the judgment-time that discloses consequence.\",\"reason\":\"Distributional evidence supports a recurrent day-punishment field, while the local syntax directly joins the time-marker to the punishment verb.\",\"representative_source_ids\":[\"QI-c7af9ab4\",\"QB-43a92314\",\"QB-bce2aac7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:3:whole-clause-scope","source_type":"word_analysis","support_id":"sup_7f45ae05fa6a28cde0b1","text":"{\"blocking_evidence\":null,\"headline\":\"scope over act and measure\",\"reader_payoff\":\"The reader notices that the denial covers the whole comparison, not merely the existence of a punisher or a bare act.\",\"reason\":\"The attachment evidence treats the ayah as one negated verbal clause, with the final indefinite completing universal negation.\",\"representative_source_ids\":[\"QG-3c83417f\",\"QS-3dd3de32\",\"QT-15134b05\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:6:indefinite-under-negation","source_type":"word_analysis","support_id":"sup_841e45fc49e6bbeccffc","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite singular becomes total\",\"reader_payoff\":\"The reader notices that the phrase means not any single candidate, not merely not one named rival.\",\"reason\":\"The negator combines with an indefinite singular final noun, and attachment support flags universal negation.\",\"representative_source_ids\":[\"QG-15ada8d1\",\"MG-e1340522\",\"QS-55a3a889\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:2:fronted-threshold","source_type":"word_analysis","support_id":"sup_8a1054bc307cdbd61924","text":"{\"blocking_evidence\":null,\"headline\":\"fronted threshold before negation\",\"reader_payoff\":\"The reader first enters consequence-time, then hears negation empty the punishment comparison.\",\"reason\":\"The surface order places the temporal frame before the negated verb relation and delayed indefinite subject.\",\"representative_source_ids\":[\"QT-fd6d7796\",\"QT-ebc8a573\",\"QY-5492a34a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:1:resultive-answer","source_type":"word_analysis","support_id":"sup_8c41d4024b20d5ef7647","text":"{\"blocking_evidence\":null,\"headline\":\"resultive answer\",\"reader_payoff\":\"The reader notices that the punishment clause is grammatically triggered by the preceding regret and judgment sequence, not introduced as an isolated theological statement.\",\"reason\":\"QAC identifies a prefixed conjunction or result particle, and the local clause evidence supports one negated verbal clause following it.\",\"representative_source_ids\":[\"QG-ef338da4\",\"MT-777d9844\",\"QB-a01d65b0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:4:form-ii-punitive-act","source_type":"word_analysis","support_id":"sup_919eb9e961d9a0f281bc","text":"{\"blocking_evidence\":null,\"headline\":\"Form II punitive act\",\"reader_payoff\":\"The reader notices that the verb names intensified imposed chastisement, so the denial targets comparable punitive agency.\",\"reason\":\"QAC identifies the local verb as Form II imperfect active in the standard reading, and V4 includes the punishment and torment branch for the root.\",\"representative_source_ids\":[\"QG-444df014\",\"QF-d72ee173\",\"MF-9f2ab728\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:6","source_type":"word_analysis","support_id":"sup_a256e4a7903f5c6d03de","text":"{\"gloss_range\":\"indefinite singular under negation, functioning as final universal closure over possible participants\",\"prose\":\"{{ar:أَحَدٌۭ}} ({{tr:aḥadun}}) closes the clause by making the negation exhaustive. As an indefinite singular under {{ar:لَّا}} ({{tr:lā}}), it does not merely name one person; it tests possible participants one by one and excludes every candidate. Its delayed position matters: the verb and owned measure fill the middle first, then the final word retroactively seals the whole comparison and widens the scene from one regretful voice in 89:24 to universal exclusion. In the active reading it is the delayed subject-agent, while the passive reading reassigns it to the affected nominative; either way, the universal closure remains. The singleness field also creates a pointed contrast with 112:1, where the same word-form marks unique oneness rather than negative exclusion. The same final seal recurs in the paired binding clause of 89:26, so the ending is not isolated: its nunated finality helps make universal exclusion the shared closure of punishment and restraint.\",\"root_display\":\"{{ar:أ ح د}} ({{tr:ʾ-ḥ-d}})\",\"root_gloss_range\":\"oneness and single-individual range; under negation here it becomes distributive universal exclusion\",\"surface_display\":\"{{ar:أَحَدٌۭ}} ({{tr:aḥadun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:5","source_type":"word_analysis","support_id":"sup_a26ac5745cb768f1a344","text":"{\"gloss_range\":\"possessed verbal noun functioning as cognate measure or punishment standard, not an ordinary victim object\",\"prose\":\"{{ar:عَذَابَهُۥٓ}} ({{tr:ʿadhābahū}}) is the clause's owned punishment measure. As a same-root verbal noun after {{ar:يُعَذِّبُ}} ({{tr:yuʿadhdhibu}}), it specifies the mode and scale of the act rather than naming a victim as an ordinary object. The suffix makes the punishment definite by possession or source, while the local context leaves a real pressure between divine source-standard and the human's experienced punishment measure; even when the accepted passive reading shifts agency, this noun remains the severity-standard. Its singular form concentrates comparison on one incomparable standard, and its placement before {{ar:أَحَدٌۭ}} ({{tr:aḥadun}}) lets that standard fill the middle of the clause before every possible comparator is excluded. The noun marks penal consequence rather than generic pain or the root's sweet-fresh branch, turns the lash imagery of 89:13 into an owned measure, answers the failed life horizon of 89:24, and prepares the matched binding measure of 89:26.\",\"root_display\":\"{{ar:ع ذ ب}} ({{tr:ʿ-dh-b}})\",\"root_gloss_range\":\"the broad root includes sweet freshness and other branches, but this possessed verbal noun selects the punishment and penal consequence branch\",\"surface_display\":\"{{ar:عَذَابَهُۥٓ}} ({{tr:ʿadhābahū}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:4:imperfect-at-that-day","source_type":"word_analysis","support_id":"sup_a60ca68a4a910443a8d0","text":"{\"blocking_evidence\":null,\"headline\":\"imperfect within the day\",\"reader_payoff\":\"The reader notices that the verb is denied within the judgment-time frame rather than as a loose lexical possibility.\",\"reason\":\"The temporal adverbial attaches to the imperfect punishment verb, and the negator governs that predicate.\",\"representative_source_ids\":[\"MG-66e2624a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:3:incomparability-through-negation","source_type":"word_analysis","support_id":"sup_a686ae37c5e1710db50d","text":"{\"blocking_evidence\":null,\"headline\":\"negated incomparability\",\"reader_payoff\":\"The reader sees that the clause is not simply saying punishment is severe; it excludes every possible comparator after the owned measure is stated.\",\"reason\":\"The negator combines with the delayed indefinite to create universal negative force over the punishment comparison.\",\"representative_source_ids\":[\"QS-9b81817f\",\"QI-ab9fff3a\",\"MT-571fb2e6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:2:temporal-adverbial-frame","source_type":"word_analysis","support_id":"sup_a924410ce4055fe8ccb9","text":"{\"blocking_evidence\":null,\"headline\":\"temporal frame for punishment\",\"reader_payoff\":\"The reader notices that the punishment comparison is anchored to the disclosed judgment-time rather than stated as an abstract timeless maxim.\",\"reason\":\"QAC and attachment evidence both mark the word as a temporal adverbial dependent of the punishment verb.\",\"representative_source_ids\":[\"QG-43d9d53f\",\"QG-9f54a7f2\",\"MG-6c8af2b8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:4:sweetness-branch-narrowed","source_type":"word_analysis","support_id":"sup_aeb4be72aac47de49b5b","text":"{\"blocking_evidence\":null,\"headline\":\"sweet branch inverted by context\",\"reader_payoff\":\"The reader notices the severity of the selected punishment branch against the root's broader sweet-fresh range, while local grammar prevents that branch from becoming the gloss.\",\"reason\":\"V4 attests a sweet-fresh branch and a punishment branch, but the local Form II verb with same-root punishment noun selects the penal branch.\",\"representative_source_ids\":[\"QS-17ab7cd2\",\"QS-1a2541c9\",\"MS-2d8c02f5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:1:sequence-reprise","source_type":"word_analysis","support_id":"sup_b06747d7658d7e2cc22b","text":"{\"blocking_evidence\":null,\"headline\":\"judgment sequence reprise\",\"reader_payoff\":\"The reader hears the ayah as the payoff of the escalating judgment chain in 89:21-24.\",\"reason\":\"The particle is compatible with a resultive answer function and the contextual cross-reference keeps the opening inside the established eschatological scene.\",\"representative_source_ids\":[\"QE-b6926fd9\",\"QG-571ca769\",\"QP-06f37018\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:5:suffix-referent-pressure","source_type":"word_analysis","support_id":"sup_b15c36b28e8c905391e7","text":"{\"blocking_evidence\":null,\"headline\":\"suffix referent pressure\",\"reader_payoff\":\"The reader notices that ownership or source is built into the word itself, while target interpretation may have to choose more explicitly than the Arabic does.\",\"reason\":\"Attachment evidence marks the suffix antecedent as grammatically ambiguous, so the surviving claim is source-standard pressure rather than a forced referent.\",\"representative_source_ids\":[\"QG-8c2bfba5\",\"QF-b46336ce\",\"QB-c04de6bc\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:2:deictic-known-day","source_type":"word_analysis","support_id":"sup_b5435ea7ea3d7e21c896","text":"{\"blocking_evidence\":null,\"headline\":\"known day by deixis\",\"reader_payoff\":\"The reader carries the staged events of 89:21-24 into the compact time-marker instead of treating the word as a newly introduced day.\",\"reason\":\"Attachment cross-references explicitly resume the established eschatological day, and V4 includes the day-then construction as a recognized unit.\",\"representative_source_ids\":[\"QG-f5181cb3\",\"QF-038fb4c8\",\"MT-ecad9fd5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:6:uniqueness-field-inverted","source_type":"word_analysis","support_id":"sup_bb469943e512f440326a","text":"{\"blocking_evidence\":null,\"headline\":\"uniqueness field inverted\",\"reader_payoff\":\"The reader sees the singleness field turned from affirming unique oneness in 112:1 to denying any rival in 89:25.\",\"reason\":\"The CRITICAL rows provide the concrete 112:1 contrast, and the local negated indefinite grammar licenses the inversion.\",\"representative_source_ids\":[\"QI-d89cba40\",\"MI-48ea3edb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:5:cognate-accusative-measure","source_type":"word_analysis","support_id":"sup_c381dec0d14954a83761","text":"{\"blocking_evidence\":null,\"headline\":\"cognate measure not victim\",\"reader_payoff\":\"The reader notices that the object-like noun is a punishment measure, so the comparison is about kind and scale of punishment.\",\"reason\":\"Attachment marks the noun as a same-root accusative under the verb and explicitly warns against treating it as an ordinary patient object.\",\"representative_source_ids\":[\"QG-f039403f\",\"MG-4556164d\",\"QS-fc530a08\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:5:measure-before-closure","source_type":"word_analysis","support_id":"sup_c3ee1a8d716dc1a79bf2","text":"{\"blocking_evidence\":null,\"headline\":\"measure before universal closure\",\"reader_payoff\":\"The reader experiences the punishment standard first, then hears every possible rival closed out at the final word.\",\"reason\":\"The surface sequence places the verbal noun between the verb and final indefinite subject.\",\"representative_source_ids\":[\"QT-0bb126d6\",\"QT-89a85f73\",\"QP-891f0379\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:2","source_type":"word_analysis","support_id":"sup_c9caa8c30d9d33ea513f","text":"{\"gloss_range\":\"deictic event-time, functioning as an accusative temporal frame for the punishment clause\",\"prose\":\"{{ar:يَوْمَئِذٍۢ}} ({{tr:yawmaʾidhin}}) is the clause's event-time, not a free-floating calendar note. As an accusative temporal frame, it attaches to {{ar:يُعَذِّبُ}} ({{tr:yuʿadhdhibu}}), so the unmatched punishment is located in the already staged judgment moment. The attached then-element makes the day identifiable from 89:21-24, especially the earlier reprise in 89:23, while the root's ordinary daylight range is narrowed here to a decisive accountability occasion. Placed before {{ar:لَّا}} ({{tr:lā}}), the word makes the reader enter consequence-time before hearing the field of comparison emptied, and it shifts authority from the human's speech to the day that discloses consequence.\",\"root_display\":\"{{ar:ي و م}} ({{tr:y-w-m}})\",\"root_gloss_range\":\"day can range from ordinary daylight to a marked event-time or the day-then construction; here the deictic judgment-event branch is selected\",\"surface_display\":\"{{ar:يَوْمَئِذٍۢ}} ({{tr:yawmaʾidhin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:5:voice-stable-measure","source_type":"word_analysis","support_id":"sup_caece718f072bfdf477b","text":"{\"blocking_evidence\":null,\"headline\":\"measure stable across voice\",\"reader_payoff\":\"The reader notices that the severity-standard remains fixed even when the qirāʾah shifts agency offstage.\",\"reason\":\"QAC notes both active and passive possibilities, while the accusative punishment measure remains the same local noun.\",\"representative_source_ids\":[\"QF-01f50007\",\"MF-cad53144\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:2:sound-compressed-negation","source_type":"word_analysis","support_id":"sup_caeeb5e3c344c2501d5e","text":"{\"blocking_evidence\":null,\"headline\":\"sound compresses time into denial\",\"reader_payoff\":\"The reader hears the time-marker pass immediately into negation rather than pausing before the denial.\",\"reason\":\"The local surface joins the compound to the following negator, while the compound itself packages noun and deictic particle.\",\"representative_source_ids\":[\"QP-a32963dc\",\"MP-d45e74d6\",\"QF-66a3e46d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:4:judgment-field-handoff","source_type":"word_analysis","support_id":"sup_cb77831aa4df234f6651","text":"{\"blocking_evidence\":null,\"headline\":\"life regret answered by punishment\",\"reader_payoff\":\"The reader notices the semantic turn from the life the human failed to prepare for in 89:24 to the punishment disclosed in 89:25.\",\"reason\":\"The local clause concentrates punishment, day-language, and universal exclusion immediately after the quoted regret.\",\"representative_source_ids\":[\"QB-f13791e3\",\"QB-f916e71e\",\"QI-43b27bf0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:4:cognate-measure-focus","source_type":"word_analysis","support_id":"sup_d31cc2c9a3035665d6ac","text":"{\"blocking_evidence\":null,\"headline\":\"act measured by its noun\",\"reader_payoff\":\"The reader notices that the verb moves first into its same-root measure, so unmatchedness is expressed by internal root repetition rather than a separate severity adjective.\",\"reason\":\"Attachment marks the following verbal noun as a cognate accusative or punishment measure rather than an ordinary direct object.\",\"representative_source_ids\":[\"QG-82739483\",\"QT-be479365\",\"QE-ae29177a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:6:paired-final-seal","source_type":"word_analysis","support_id":"sup_d8f96ee9b71460fe2f1a","text":"{\"blocking_evidence\":null,\"headline\":\"paired final seal\",\"reader_payoff\":\"The reader notices that universal exclusion becomes the shared seal of the paired punishment and binding clauses in 89:25-26.\",\"reason\":\"The next ayah repeats the same final exclusion pattern after the matched binding measure.\",\"representative_source_ids\":[\"QE-f2ab062d\",\"ME-048ab8f6\",\"QB-8378015c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:6:incomparability-after-measure","source_type":"word_analysis","support_id":"sup_dfd5aa56e443de3b1646","text":"{\"blocking_evidence\":null,\"headline\":\"no comparator survives\",\"reader_payoff\":\"The reader notices that every possible comparator is excluded only after the punishment measure has occupied the clause's middle.\",\"reason\":\"The final indefinite answers the earlier negation across the intervening verb and cognate measure.\",\"representative_source_ids\":[\"QS-41d20d1c\",\"QI-bc950e6c\",\"QE-84c6bc06\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:4","source_type":"word_analysis","support_id":"sup_e02188a59b7868572df3","text":"{\"gloss_range\":\"Form II imperfect punishment act under negation, with active agency in the standard reading and a passive qirāʾah contrast\",\"prose\":\"{{ar:يُعَذِّبُ}} ({{tr:yuʿadhdhibu}}) is a Form II imperfect, so the selected sense is an imposed punitive act at that judgment-time rather than generic pain. In the standard active reading, {{ar:لَّا}} ({{tr:lā}}) denies any agent capable of inflicting the owned measure that immediately follows. The same-root noun {{ar:عَذَابَهُۥٓ}} ({{tr:ʿadhābahū}}) keeps the focus on punishment as its own scale, not on an ordinary object-victim; unlike the adjective of greater punishment in 88:24, 89:25 makes unmatchedness through verb-noun repetition. The root's sweet-fresh branch remains a real lexical branch, but local grammar, Form II use, and the cognate noun narrow the live sense to punishment, and the doubled Form II cue tightens before the root returns in the noun. The accepted passive reading {{ar:يُعَذَّبُ}} ({{tr:yuʿadhdhabu}}) shifts the final {{ar:أَحَدٌۭ}} ({{tr:aḥadun}}) from punisher to punished one while preserving the same incomparable punishment measure. That pattern also answers the failed life-preparation of 89:24 and sets up the matched binding formula of 89:26.\",\"root_display\":\"{{ar:ع ذ ب}} ({{tr:ʿ-dh-b}})\",\"root_gloss_range\":\"the root includes sweet freshness, abstention, withholding, exposedness, punishment, appendage, and other branches; the local Form II predicate selects the punishment and torment branch\",\"surface_display\":\"{{ar:يُعَذِّبُ}} ({{tr:yuʿadhdhibu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:4:qiraat-voice-pivot","source_type":"word_analysis","support_id":"sup_e4075c0a16fa6fadfda7","text":"{\"blocking_evidence\":null,\"headline\":\"voice pivot preserves measure\",\"reader_payoff\":\"The reader notices that agency can shift between active and passive readings, but the incomparable owned punishment standard remains fixed.\",\"reason\":\"QAC notes the passive qirāʾah while the standard local parsing remains active; both readings preserve the same root frame and cognate measure.\",\"representative_source_ids\":[\"QF-e5c92eea\",\"QY-d492425e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:5:penal-branch-selected","source_type":"word_analysis","support_id":"sup_eac8b04492b051ae298c","text":"{\"blocking_evidence\":null,\"headline\":\"penal branch selected\",\"reader_payoff\":\"The reader notices punishment as calibrated consequence, not generic pain or the root's sweet-fresh branch.\",\"reason\":\"V4 attests multiple root branches, but the possessed punishment noun after the same-root verb selects the penal branch.\",\"representative_source_ids\":[\"QS-19b58b06\",\"QS-9fad9aae\",\"QS-d525a392\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:5:cross-ayah-measure-shift","source_type":"word_analysis","support_id":"sup_f5ceeeae55303d8d44e2","text":"{\"blocking_evidence\":null,\"headline\":\"instrument becomes measure\",\"reader_payoff\":\"The reader sees the punishment field intensify from the lash image of 89:13 into the owned measure of 89:25.\",\"reason\":\"The CRITICAL rows supply the concrete 89:13 reference and the local noun supplies the owned measure.\",\"representative_source_ids\":[\"QI-4fce4d37\",\"MI-8363e798\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:25:6:distributive-singleness","source_type":"word_analysis","support_id":"sup_f9277a93e0e3ce4ad236","text":"{\"blocking_evidence\":null,\"headline\":\"one-by-one exclusion\",\"reader_payoff\":\"The reader notices that universality is achieved through singleness: each imagined participant is considered and denied.\",\"reason\":\"The local noun is singular and indefinite, and the contextual profile shows this form often appears in negated or scoped environments.\",\"representative_source_ids\":[\"QS-1fc2409f\",\"QF-847a1364\",\"QF-d94ec30f\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ","ayah_ref":"89:25"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000017/B002","root_000994/B005"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000994","role":"Severe penal pain gives the repeated verb-noun construction its primary punitive force.","root":"ع ذ ب","source_ref":"89:25","source_word_indices":["3","4"]},{"branch_id":"B002","mapped_root_id":"root_000017","role":"Exhaustive scope under negation excludes every candidate who might match the punishing act.","root":"ء ح د","source_ref":"89:25","source_word_indices":["5"]}],"changed_reading":{"after":"The clause asserts punishment whose agency and measure admit no peer.","before":"A generic prediction that punishment will occur on that day."},"confidence":"strong","focus_anchor":"The focus repeats ع ذ ب as an active verb and cognate noun, then closes with indefinite أَحَد under negation.","mechanism":"The penal branch supplies severe inflicted pain, while exhaustive أَحَد removes every possible rival punisher; the possessive punishment is therefore marked as unmatched in source and measure.","model_id":"baseline_incomparable_punishment"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_incomparable_punishment","source_type":"hft","support_id":"sup_ce21ccf4a2b54adc02c3","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ","ayah_ref":"89:25"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000017/B002","root_000017/B005","root_000994/B005"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000994","role":"The penal branch keeps the isolated encounter anchored in actual punishment rather than abstract singularity.","root":"ع ذ ب","source_ref":"89:25","source_word_indices":["3","4"]},{"branch_id":"B005","mapped_root_id":"root_000017","role":"Isolation and distribution by separate individuals turn the final noun into a cue of unshared encounter.","root":"ء ح د","source_ref":"89:25","source_word_indices":["5"]},{"branch_id":"B002","mapped_root_id":"root_000017","role":"Negative exhaustion extends that isolation across every possible person rather than selecting only one.","root":"ء ح د","source_ref":"89:25","source_word_indices":["5"]}],"changed_reading":{"after":"The punishment is also non-transferable and undiffused, confronting each case without a sharing other.","before":"No other punisher reaches the same severity."},"confidence":"medium","focus_anchor":"Sentence-final أَحَد stands after the doubled punishment expression and can activate both exhaustive negation and individual-by-individual isolation.","mechanism":"Alongside excluding a rival agent, the clause can isolate the punitive encounter: no collective, substitute, or second party diffuses it, and the affected case stands as a singular exposure.","model_id":"baseline_individual_exposure"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_individual_exposure","source_type":"hft","support_id":"sup_e913edbee7a1d3f489d2","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ","ayah_ref":"89:25"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000994/B002","root_000994/B003","root_000994/B005"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000994","role":"The ordinary punishment branch supplies the controlling sense that the adjacent branches modify.","root":"ع ذ ب","source_ref":"89:25","source_word_indices":["3","4"]},{"branch_id":"B002","mapped_root_id":"root_000994","role":"Bodily abstention from food and drink supplies deprivation as a concrete mode of suffering.","root":"ع ذ ب","source_ref":"89:25","source_word_indices":["3","4"]},{"branch_id":"B003","mapped_root_id":"root_000994","role":"Withholding and weaning supply the causal operation that removes access to a desired good.","root":"ع ذ ب","source_ref":"89:25","source_word_indices":["3","4"]}],"changed_reading":{"after":"Punishment can also be the decisive withholding of sustenance, access, or attachment.","before":"Punishment means pain added to the sufferer."},"confidence":"exploratory","focus_anchor":"The doubled ع ذ ب form permits the punitive branch to remain primary while activating neighboring branches of abstention and forcible withholding.","mechanism":"Punishment may work subtractively as well as additively: the body is made to go without, or is weaned away from what it seeks, so torment includes deprivation rather than only imposed sensation.","model_id":"baseline_punishment_as_withholding"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_punishment_as_withholding","source_type":"hft","support_id":"sup_42b4b708b9d33b2e7aba","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ","ayah_ref":"89:25"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000017/B005","root_000994/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000994","role":"Absence of any covering toward the sky supplies the spatial condition of exposure.","root":"ع ذ ب","source_ref":"89:25","source_word_indices":["3","4"]},{"branch_id":"B005","mapped_root_id":"root_000017","role":"Individual isolation makes the uncovered condition something borne without protective company.","root":"ء ح د","source_ref":"89:25","source_word_indices":["5"]}],"changed_reading":{"after":"Punishment also appears as a condition of solitary unsheltering.","before":"Punishment is an act performed upon someone."},"confidence":"exploratory","focus_anchor":"A branch of ع ذ ب names being left with no cover between oneself and the sky, while أَحَد can mark isolation.","mechanism":"The focus can carry a spatial shadow in which punishment strips cover and leaves a person singly exposed; this does not replace penal pain but gives it an environmental form.","model_id":"baseline_uncovered_punishment"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_uncovered_punishment","source_type":"hft","support_id":"sup_0ac2d4fc8ca44a7567d4","trust":"legacy_unbound"}]}
</lane_packet_json>
