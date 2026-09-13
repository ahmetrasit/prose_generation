# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **19:89**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s019-regular-20260912/s019/19_89/micro.discovery.json` and modify nothing
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
  "ayah_ref": "19:89",
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
{"analysis_context":{"analysis_id":"s019-regular-20260912","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"19:89","host_surah":19,"lane_context_refs":[],"ordered_context_refs":["19:77","19:78","19:79","19:80","19:81","19:82","19:83","19:84","19:85","19:86","19:87","19:88","19:90","19:91","19:92","19:93","19:94","19:95","19:96","19:97","19:98","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Anlam yalnızca belirtilen yapılardaki ulaştırma veya ulaşma ilişkisini kapsar; borç ödeme gibi özel kullanımlara genişletilmez.","branch_kind":"collocation","branch_ref":"root_000021/B001","candidate_links":[{"candidate_id":"cand_2ad97897c006e96d4255","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"إِدّ","morph_features":"STEM|POS:ADJ|LEM:<id~|ROOT:Add|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"19:89:4:1","qac_word_ref":"19:89:4","surface_ar":"إِدًّا"}],"gloss":"ulaştırmak veya ulaşmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesne veya söz bir hedefe aktarılır ya da haber hedef kişiye kadar varır."}}],"root_ar":"ء د د","root_id":"root_000021","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesnenin bir alıcıya aktarılmasını ve haberin muhataba varmasını birlikte temsil eden genel karşılıktır.","boundary_detail":"Anlam yalnızca belirtilen yapılardaki ulaştırma veya ulaşma ilişkisini kapsar; borç ödeme gibi özel kullanımlara genişletilmez.","branch_image_ar":"إيصال ووصول","concept_gloss":"ulaştırmak veya ulaşmak","contextual_glosses":[{"applicability":"Bir nesne, selam veya sözün belirli bir alıcıya götürülüp aktarılması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aktarılan şeyin belirli bir hedefe erişmesini korur."},"facet_ids":["F001"],"text":"birine ulaştırmak","usage_role":"contextual"},{"applicability":"Bir haberin aktarım sonunda muhatabına vardığını bildiren bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Haberin muhatabına kadar varması yönünü korur."},"facet_ids":["F001"],"text":"haber kendisine ulaşmak","usage_role":"contextual"}],"definition":"Belirli söz öbeklerinde bir şeyi ya da sözü bir alıcıya ulaştırmak veya haberin o alıcıya varmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesne veya söz bir hedefe aktarılır ya da haber hedef kişiye kadar varır."}],"identity_rationale":"Kaynak ifadesi, bir şeyi başka bir şeye ya da kişiye ulaştırmayı ve bir haberin muhatabına varmasını aynı ulaşma ilişkisi içinde açıkça birleştirir. Hazırlanan çerçeve bu ortak çekirdeği doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"birine ulaştırmak veya teslim etmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"haber kendisine ulaşmak"}],"lexicalization_note":"Bu dal yalnızca tanıklanan söz öbeklerinde geçerlidir; yalın köke genel bir ulaştırma anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sınırı en açık gösteren genel varış dalı yayımlandı, diğerleri daha uzak alan ilişkileri veya aynı kökün ayrı dallarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel varış ve ulaştırmayı anlatırken odak dal, belirli söz öbekleriyle sınırlı aktarım ve haber ulaşması kullanımlarını temsil eder.","focus_only":"Tanıklanan söz öbeklerinde teslim etme ve haberin muhataba varması öne çıkar.","gloss":"genel varma ve ulaştırma","neighbor_only":"Kişi, nesne ve yazının bir yöne varmasını daha genel biçimde kapsar.","neighbor_ref":"root_001655/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir varlığın veya iletinin belirli bir hedefe erişmesi bulunur."}],"source_phrase_ar":"أصل واحد وهو إيصال الشيء إلى الشيء أو وصوله إليه (maqayis)؛ تأدى إليه الخبر أي انتهى (sihah)؛ أدوا إلي بمعنى سلموا إلي أو أدوا إلى ما أمركم الله به (tahdhib)","source_summary":"Kaynaklar, bir şeyin hedefe teslim edilmesi ile haberin muhataba ulaşmasını ortak bir varış ilişkisi altında toplar.","sources":["MQ","SI","TA"],"what_is_ar":"إيصال الشيء إلى غيره أو وصوله إليه، وانتهاء الخبر أو القول إلى المخاطب","what_is_not_ar":"أداء الحقوق الخاص؛ الأداة والعدة؛ الحيلة والاختتال"},"support_links":["sup_f1c8cf2edea977b6945e"]},{"boundary":"Dal, yükümlülük konusu bir hakkın ödenmesi veya sahibine verilmesiyle sınırlıdır; salt ulaşmayı anlatmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000021/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِدّ","morph_features":"STEM|POS:ADJ|LEM:<id~|ROOT:Add|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"19:89:4:1","qac_word_ref":"19:89:4","surface_ar":"إِدًّا"}],"gloss":"hakkı eksiksiz yerine getirmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yükümlülük konusu hak ödenir, sahibine verilir ve eksiksiz biçimde yerine getirilir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Borç, vergi, baş vergisi ve emanet bu yerine getirmenin örnekleridir."}}],"root_ar":"ء د د","root_id":"root_000021","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Borç, vergi, emanet ve benzeri yükümlülüklerin ödenmesi veya sahibine verilmesi için genel karşılıktır.","boundary_detail":"Dal, yükümlülük konusu bir hakkın ödenmesi veya sahibine verilmesiyle sınırlıdır; salt ulaşmayı anlatmaz.","branch_image_ar":"أداء الحق والأمانة","concept_gloss":"hakkı eksiksiz yerine getirmek","contextual_glosses":[{"applicability":"Üzerinde bulunan parasal borcu kapatma bağlamında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Emanet ve parasal olmayan hakların sahibine verilmesini kapsamaz.","preserves":"Yükümlü olunan hakkı ödeme ve kapatma işlemini korur."},"facet_ids":["F001","F002"],"text":"borcunu ödemek","usage_role":"contextual"},{"applicability":"Korunmak üzere bırakılan bir şeyi hak sahibine eksiksiz teslim etme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Borç ve vergi gibi ödeme yükümlülüklerini kapsamaz.","preserves":"Bir hakkı sahibine eksiksiz verme yönünü korur."},"facet_ids":["F001","F002"],"text":"emaneti sahibine vermek","usage_role":"contextual"}],"definition":"Kişinin üzerinde bulunan borç, vergi, emanet veya başka bir hakkı ödemesi, sahibine vermesi ve yükümlülüğü eksiksiz yerine getirmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yükümlülük konusu hak ödenir, sahibine verilir ve eksiksiz biçimde yerine getirilir."},{"facet_id":"F002","role":"example","statement":"Borç, vergi, baş vergisi ve emanet bu yerine getirmenin örnekleridir."}],"identity_rationale":"Kaynak ifadesi kişinin üzerindeki borcu veya hakkı ödemesini, yerine getirmesini ve eksiksiz vermesini açıkça ortak çekirdek yapar. Vergi ve emanet örnekleri bu çekirdeğin uygulamalarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"üzerindeki hakkı ödemek ve yerine getirmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"emaneti sahibine eksiksiz vermek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"birine hakkını ödemek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"birinden zorla para çıkarmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"hakkı ödeme ve eksiksiz yerine getirme"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"emaneti daha iyi yerine getiren"}],"lexicalization_note":"Dal hem çekimi yapılmış biçimleri hem de belirli söz öbeklerini içerir; söz öbeklerine özgü para çıkarma ve karşılaştırma anlamları genel tanıma katılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ödeme ile tahsil arasındaki katılımcı farkını gösteren en yakın dal seçildi, kalan adaylar yükümlülük, engelleme veya güvenilirlik gibi yan alanlardadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yükümlünün ödeme ve verme eylemine dayanır; komşu dal ise alacaklının isteme ve tahsil etme yönünü de içerir.","focus_only":"Yükümlünün hakkı ödeyip eksiksiz yerine getirmesi bakış açısını öne çıkarır.","gloss":"hakkı ödeme ve tahsil etme","neighbor_only":"Hakkın alacaklı tarafından istenmesi, tahsil edilmesi ve teslim alınmasını da kapsar.","neighbor_ref":"root_001237/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da borç veya başka bir hakkın gereğinin yerine gelmesiyle ilgilidir."}],"source_phrase_ar":"أدى فلان يؤدي ما عليه أداء وتأدية (maqayis;tahdhib)؛ أدى دينه تأدية أي قضاه والاسم الأداء (sihah)؛ الأداء دفع الحق دفعة وتوفيته كأداء الخراج والجزية وأداء الأمانة (mufradat)","source_summary":"Kaynaklar, kişinin üzerindeki hakkı ödemesi ve eksiksiz biçimde yerine getirmesi konusunda birleşir; borç, vergi ve emanet başlıca örneklerdir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"دفع الحق وقضاؤه وتوفيته، كالدين والخراج والجزية والأمانة","what_is_not_ar":"مجرد وصول الخبر؛ الأداة والعدة؛ قلة العدد"},"support_links":[]},{"boundary":"Elverişli duruma gelme çekirdeği yalnızca tanıklanan söz öbeklerine aittir; orta tempolu yürüyüş ayrı bir ilişkili kullanım olarak tutulur.","branch_kind":"collocation","branch_ref":"root_000021/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِدّ","morph_features":"STEM|POS:ADJ|LEM:<id~|ROOT:Add|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"19:89:4:1","qac_word_ref":"19:89:4","surface_ar":"إِدًّا"}],"gloss":"işlenmeye elverişli duruma gelmek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Süt, tulum veya meyve bir sonraki işlem için elverişli olgunluk ya da kıvam aşamasına gelir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yürüyüş bağlamında iki yürüyüş biçimi arasında orta bir tempoyla ilerleme anlatılır."}}],"root_ar":"ء د د","root_id":"root_000021","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Süt, tulum ve meyvenin sonraki işlem için uygun kıvam veya olgunluğa eriştiği ana kullanım için geçerlidir.","boundary_detail":"Elverişli duruma gelme çekirdeği yalnızca tanıklanan söz öbeklerine aittir; orta tempolu yürüyüş ayrı bir ilişkili kullanım olarak tutulur.","branch_image_ar":"بلوغ حالة الصلاح","concept_gloss":"işlenmeye elverişli duruma gelmek","contextual_glosses":[{"applicability":"Sütün mayalanabilecek ölçüde kıvam kazandığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tulumun hazır oluşunu, meyvenin olgunlaşmasını ve yürüyüş kullanımını kapsamaz.","preserves":"Sütün sonraki işleme uygun kıvama gelmesini korur."},"facet_ids":["F001"],"text":"süt koyulaşmak","usage_role":"contextual"},{"applicability":"İki yürüyüş biçimi arasında kalan orta bir yürüyüşü anlatan özel bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Orta hız ve biçimde yürüme kullanımını tam olarak korur."},"facet_ids":["F002"],"text":"orta tempoda yürümek","usage_role":"contextual"}],"definition":"Belirli söz öbeklerinde süt, tulum veya hurmanın sonraki işlem ya da kullanım için elverişli bir aşamaya gelmesidir. Aynı dalda, iki yürüyüş biçimi arasında orta tempoyla yürüme ayrıca tanıklanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Süt, tulum veya meyve bir sonraki işlem için elverişli olgunluk ya da kıvam aşamasına gelir."},{"facet_id":"F002","role":"associated_use","statement":"Yürüyüş bağlamında iki yürüyüş biçimi arasında orta bir tempoyla ilerleme anlatılır."}],"identity_rationale":"Kaynak ifadesi süt, tulum ve hurma için sonraki işleme elverişli bir duruma gelmeyi destekler; ayrıca orta tempolu yürüyüşü ayrı bir kullanım olarak verir. Yürüyüş, olgunlaşma çekirdeğinin parçası değil, aynı dalda korunması gereken bağımlı bir kullanımdır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"süt koyulaşıp mayalanmaya hazır olmak"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"tulum çalkalanmaya elverişli olmak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"hurma olgunlaşmak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"sütü tulumda çalkalamak"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"orta tempoda yürümek"}],"lexicalization_note":"Bütün anlamlar belirli söz öbeklerine bağlıdır; süt, tulum, hurma ve yürüyüş kullanımlarından yalın kök anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel olgunluğa erişme dalı temel sınırı en iyi gösterir, öteki adaylar meyveye özgü örnekler, erkenlik veya ilgisiz araç alanlarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel zaman ve olgunluk erişimini kapsar; odak dal ise belirli süt, tulum ve meyve söz öbekleriyle sınırlıdır ve ayrıca yürüyüş kullanımı taşır.","focus_only":"Süt ve tulumun belirli bir işleme hazır oluşunu ve ayrı bir orta yürüyüş kullanımını kapsar.","gloss":"vaktine ve olgunluğa erişmek","neighbor_only":"Bir şeyin vaktine, olgunluğuna veya belirlenmiş son aşamasına gelmesini daha genel anlatır.","neighbor_ref":"root_000063/B003","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir şeyin uygun veya tamamlanmış aşamaya erişmesi bulunur."}],"source_phrase_ar":"للبن إذا وصل إلى حال الرؤوب قد أدى يأدي أديا (maqayis)؛ أدى اللبن يأدي أديا أي خثر ليروب (sihah)؛ أدى السقاء يأدي أديا إذا أمكن أن يمخض (tahdhib)؛ أدت التمرة وهو الينوع والنضج وأدوت في مشيي وهو مشي بين المشيين (tahdhib)","source_summary":"Kaynaklar sütün mayalanmaya yaklaşmasını, tulumun çalkalanabilir olmasını ve hurmanın olgunlaşmasını elverişli aşamaya gelme altında verir; orta tempolu yürüyüş ayrıca kaydedilir.","sources":["MQ","SI","TA"],"what_is_ar":"بلوغ اللبن أو السقاء أو الثمرة حالة تصلح لما بعدها، ويلحق به المشي المتوسط بين مشيين","what_is_not_ar":"أداء الدين؛ الإعانة؛ الحيلة"},"support_links":[]},{"boundary":"Araç ve hazırlık çekirdeği ile su kabı adı birbirine karıştırılmaz; her kullanım kendi tanıklanan biçimiyle sınırlandırılır.","branch_kind":"mixed_non_bare","branch_ref":"root_000021/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِدّ","morph_features":"STEM|POS:ADJ|LEM:<id~|ROOT:Add|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"19:89:4:1","qac_word_ref":"19:89:4","surface_ar":"إِدًّا"}],"gloss":"araç, donanım ve hazırlık","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir meslek, yolculuk veya savaş için gereken araç ve donanım sağlanır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Araçları edinmiş olmak, yapılacak iş için hazır ve donanımlı olma durumuna uzanır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı biçim ailesindeki ayrı bir ad, su taşımaya yarayan kabı belirtir."}}],"root_ar":"ء د د","root_id":"root_000021","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir eylemi mümkün kılan araçlar ile bunları edinerek hazır olma çekirdeğini birlikte karşılar.","boundary_detail":"Araç ve hazırlık çekirdeği ile su kabı adı birbirine karıştırılmaz; her kullanım kendi tanıklanan biçimiyle sınırlandırılır.","branch_image_ar":"الأداة والعدة","concept_gloss":"araç, donanım ve hazırlık","contextual_glosses":[{"applicability":"Yolculuk için gerekli araç ve gereçleri edinip hazır duruma gelme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Meslek ve savaş araçlarını ve su kabı adını kapsamaz.","preserves":"Gerekli donanımı edinerek hazır olma yönünü korur."},"facet_ids":["F001","F002"],"text":"yolculuk için hazırlanmak","usage_role":"contextual"},{"applicability":"Suyu taşımaya veya saklamaya yarayan kabın özel adı için açıklayıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Suyu taşıyan kap anlamını doğrudan korur."},"facet_ids":["F003"],"text":"su kabı","usage_role":"contextual"}],"definition":"Bir işi yapmaya yarayan araç, donanım veya savaş gereci ile bunları edinerek işe hazırlanma durumudur. Su taşımaya yarayan kap adı ayrı bir biçimsel kullanım olarak bu dalda yer alır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir meslek, yolculuk veya savaş için gereken araç ve donanım sağlanır."},{"facet_id":"F002","role":"extension","statement":"Araçları edinmiş olmak, yapılacak iş için hazır ve donanımlı olma durumuna uzanır."},{"facet_id":"F003","role":"source_variant","statement":"Aynı biçim ailesindeki ayrı bir ad, su taşımaya yarayan kabı belirtir."}],"identity_rationale":"Kaynak ifadesi araç, meslek donanımı, savaş gereci ve bir iş için hazırlanmayı ortak bir araçlanma alanında destekler. Su kabı ise bu işlevsel çekirdeğin zorunlu parçası değil, ayrı bir adlandırma olarak korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"araç ve gereç"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"eyer takımının kayışları"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"su kabı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"silah ve donanımı eksiksiz olan"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yolculuk için hazırlanmak"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"iş için hazırlanıp gerekli donanımı almak"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bir iş veya namaz için hazırlık"}],"lexicalization_note":"Dal hem ad ve türemiş biçimleri hem de hazırlık bildiren söz öbeklerini içerir; yapıya özgü anlamlar yalın kökte birleştirilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel araç dalı çekirdek örtüşmeyi en iyi gösterir, diğerleri belirli araç türleri, araçsızlık veya farklı işlevlerle sınırlıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal somut aracın yanında donanımlı ve hazır olma durumuna uzanır; komşu dal araç ve taşıyıcı nesne adlarında daha geniştir.","focus_only":"Donanımlanma, işe hazırlanma ve ayrı bir su kabı adını da içerir.","gloss":"araç ve taşıyıcı düzenek","neighbor_only":"Taşıyıcı düzenek ve çadır direkleri gibi daha geniş araç türlerini adlandırır.","neighbor_ref":"root_000067/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da bir işi görmeye yarayan somut araçları kapsar."}],"source_phrase_ar":"أداة الرحل سيوره ونسوعه وأداة السرج (jamhara)؛ الأداة الآلة والجمع الأدوات (sihah)؛ آديت للسفر فأنا مؤد له إذا كنت متهيئا له (sihah;tahdhib)؛ لكل ذي حرفة أداة وهي آلته وأداة الحرب سلاحها ورجل مؤد كامل أداة السلاح والإداوة للماء (tahdhib)؛ الأداة التي بها يتوصل إليه (mufradat)","source_summary":"Kaynaklar aracı bir işe ulaşmayı sağlayan nesne, meslek donanımı ve savaş gereci olarak açıklar; yolculuğa veya işe hazırlanmayı ve su kabı adını da kaydeder.","sources":["JA","SI","TA","MU"],"what_is_ar":"الأداة والآلة والعدة والسلاح وما يتهيأ به للفعل، ويدخل فيه الإداوة وعاء الماء","what_is_not_ar":"أداء الحقوق؛ الاستعداء على الخصم؛ الحيلة"},"support_links":[]},{"boundary":"Dal açık yardım ve güçlendirmeyi kapsar; gizli aldatmayı veya yalnızca araç sahibi olmayı içermez.","branch_kind":"collocation","branch_ref":"root_000021/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِدّ","morph_features":"STEM|POS:ADJ|LEM:<id~|ROOT:Add|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"19:89:4:1","qac_word_ref":"19:89:4","surface_ar":"إِدًّا"}],"gloss":"güçlendirip yardım etmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi belirli bir işi yapabilsin diye güçlendirilir ve desteklenir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir hasma karşı yöneticiye başvurularak onun müdahalesi ve yardımı istenir."}}],"root_ar":"ء د د","root_id":"root_000021","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiye belirli bir işte veya karşılaşmada güç ve destek sağlama çekirdeğinin genel karşılığıdır.","boundary_detail":"Dal açık yardım ve güçlendirmeyi kapsar; gizli aldatmayı veya yalnızca araç sahibi olmayı içermez.","branch_image_ar":"إعانة وتقوية","concept_gloss":"güçlendirip yardım etmek","contextual_glosses":[{"applicability":"Bir hasma karşı yönetici veya yetkili makamın desteğini isteme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hasma karşı yetkili desteğine başvurma kullanımını korur."},"facet_ids":["F002"],"text":"yönetimden yardım istemek","usage_role":"contextual"}],"definition":"Bir kişiyi belirli bir iş veya kişiye karşı güçlendirmek ve ona yardım etmektir; bunun özel bir biçiminde kişi, hasmına karşı yöneticinin yardımını ister.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi belirli bir işi yapabilsin diye güçlendirilir ve desteklenir."},{"facet_id":"F002","role":"specialization","statement":"Bir hasma karşı yöneticiye başvurularak onun müdahalesi ve yardımı istenir."}],"identity_rationale":"Kaynak ifadesi birini belirli bir işte güçlendirme ve ona yardım etme çekirdeğini açıkça verir. Yöneticiye bir hasım hakkında başvurma kullanımı, bu yardımın otorite aracılığıyla sağlanan özel biçimidir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir işte güçlendirip yardım etmek"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"hasma karşı yöneticiden yardım istemek"}],"lexicalization_note":"Yardım ve otoriteden destek isteme anlamları yalnızca tanıklanan söz öbeklerinde geçerlidir; yalın köke taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel güç ve destek dalı en yakın karşılaştırmadır, kalanlar savunma, pekiştirme, otorite veya aynı kökün ayrı anlamlarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel güç ve dayanışma alanını kapsar; odak dal belirli söz öbeklerindeki yardım eylemi ile otoriteye başvurma kullanımına bağlıdır.","focus_only":"Belirli bir işte yardım etmeyi ve hasma karşı yöneticinin desteğini istemeyi içerir.","gloss":"güç ve destek sağlamak","neighbor_only":"Güç, dayanışma ve karşılıklı destek alanını daha genel biçimde kapsar.","neighbor_ref":"root_000027/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişinin gücünü artırma ve ona destek olma alanında buluşur."}],"source_phrase_ar":"آداه على كذا إذا قواه عليه وأعانه (sihah)؛ استأديت الأمير على فلان فآداني عليه بمعنى استعديته فأعداني عليه (sihah)؛ استأديت السلطان على فلان أي استعديت فآداني عليه أي أعداني وأعانني (tahdhib)؛ استأديت على فلان نحو استعديت (mufradat)","source_summary":"Kaynaklar güçlendirme ve yardım etme anlamında birleşir; yöneticiye hasım hakkında başvurma, bu yardım ilişkisinin özel uygulamasıdır.","sources":["SI","TA","MU"],"what_is_ar":"إعانة غيره وتقويته على أمر، ومنه الاستعداء بالسلطان على الخصم","what_is_not_ar":"الأداة المادية؛ أداء الحق؛ الحيلة الخفية"},"support_links":[]},{"boundary":"Dal gizli düzen ve aldatma yoluyla hedefe erişmeyle sınırlıdır; açık yardım veya araç kullanımı tek başına bu anlama girmez.","branch_kind":"collocation","branch_ref":"root_000021/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِدّ","morph_features":"STEM|POS:ADJ|LEM:<id~|ROOT:Add|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"19:89:4:1","qac_word_ref":"19:89:4","surface_ar":"إِدًّا"}],"gloss":"hileyle ele geçirmeye çalışmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hedefe erişmek için karşıdakinin fark etmeyeceği bir düzen veya aldatma yolu kullanılır."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir yırtıcının avını yiyebilmek için onu kandırması bu kullanımın örneğidir."}}],"root_ar":"ء د د","root_id":"root_000021","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir hedefe ulaşmak veya onu almak için gizli düzen ve aldatma kullanılan bağlamların genel karşılığıdır.","boundary_detail":"Dal gizli düzen ve aldatma yoluyla hedefe erişmeyle sınırlıdır; açık yardım veya araç kullanımı tek başına bu anlama girmez.","branch_image_ar":"حيلة واختتال","concept_gloss":"hileyle ele geçirmeye çalışmak","contextual_glosses":[{"applicability":"Bir avı veya kişiyi aldatma yoluyla ele geçirmeye çalışma bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aldatma yoluyla hedefi ele geçirme amacını korur."},"facet_ids":["F001","F002"],"text":"kandırıp yakalamaya çalışmak","usage_role":"contextual"}],"definition":"Bir şeyi elde etmek, birini ele geçirmek veya bir işi gerçekleştirmek için gizli bir düzen kurup karşıdakini aldatmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hedefe erişmek için karşıdakinin fark etmeyeceği bir düzen veya aldatma yolu kullanılır."},{"facet_id":"F002","role":"example","statement":"Bir yırtıcının avını yiyebilmek için onu kandırması bu kullanımın örneğidir."}],"identity_rationale":"Kaynak ifadesi bir hedefe erişmek veya onu ele geçirmek için hileye başvurmayı ve karşıdakini aldatmayı açıkça destekler. Verilen hayvan örneği çekirdeğin örneğidir, tanımın zorunlu katılımcısı değildir.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"birini kandırıp ele geçirmeye çalışmak"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bir işi hileyle gerçekleştirmeye çalışmak"}],"lexicalization_note":"Hile ve aldatma anlamı yalnızca tanıklanan söz öbeklerine bağlıdır; buradan yalın kök için genel bir anlam çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; geniş hile ve düzen dalı çekirdek yakınlığını en iyi gösterir, kalanlar belirli kandırma, fırsat kollama veya gizlice alma türleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hedefi elde etmeye yönelik hileyle sınırlıdır; komşu dal zarar verme niyeti ve aşamalı tuzak gibi daha geniş kötü düzenleri de içerir.","focus_only":"Bir şeyi almak veya bir işi yapmak için araçsal hileye başvurmayı öne çıkarır.","gloss":"hile ve kötü düzen kurmak","neighbor_only":"Kötülük tasarlama, karşıdakini oyalama ve cezaya sürükleyen erteleme gibi daha geniş düzenleri kapsar.","neighbor_ref":"root_001334/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda da karşıdakinin bilgisi dışında kurulan aldatıcı bir düzen vardır."}],"source_phrase_ar":"أدوت له أي ختلته والذئب يأدو للغزال أي يختله ليأكله (sihah)؛ أدوت أدوا إذا اختلت (tahdhib)؛ أدوت بفعل كذا أي احتلت وأصله تناولت الأداة (mufradat)","source_summary":"Kaynaklar bir hedefi elde etmek için hile kurma ve karşıdakini aldatma anlamında birleşir; avını kandıran yırtıcı bu çekirdeği örnekler.","sources":["SI","TA","MU"],"what_is_ar":"الاحتيال والاختتال للوصول إلى الشيء أو أخذه","what_is_not_ar":"الإعانة الصريحة؛ أداء الحقوق؛ قلة العدد"},"support_links":[]},{"boundary":"Dal, dikkati işitme yoluyla konuşana verme anlamındadır; anlama hızı, susma veya işitme zayıflığı bu çekirdeğe dahil değildir.","branch_kind":"collocation","branch_ref":"root_000021/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِدّ","morph_features":"STEM|POS:ADJ|LEM:<id~|ROOT:Add|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"19:89:4:1","qac_word_ref":"19:89:4","surface_ar":"إِدًّا"}],"gloss":"kulak verip dinlemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dinleyici işitme dikkatini konuşana verir ve onun sözünü dinler."}}],"root_ar":"ء د د","root_id":"root_000021","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Konuşan kişiye işitme dikkatini yöneltip sözünü takip etme bağlamında doğal genel karşılıktır.","boundary_detail":"Dal, dikkati işitme yoluyla konuşana verme anlamındadır; anlama hızı, susma veya işitme zayıflığı bu çekirdeğe dahil değildir.","branch_image_ar":"إداء السمع","concept_gloss":"kulak verip dinlemek","contextual_glosses":[{"applicability":"Konuşanın bir topluluktan dikkatini kendisine vermesini istediği emir bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Konuşana yöneltilen dikkatli dinleme isteğini korur."},"facet_ids":["F001"],"text":"beni dinleyin","usage_role":"contextual"}],"definition":"İşitme dikkatini konuşan kişiye yöneltip onun söylediklerini dinlemektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dinleyici işitme dikkatini konuşana verir ve onun sözünü dinler."}],"identity_rationale":"Tek kaynak ifadesi, kişinin işitmesini konuşana yöneltmesi ve onu dinlemesi anlamını doğrudan açıklar. Hazırlanan çerçeve bu dinleme eylemini ek bir anlam yüklemeden korur.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"kulak verip dinlemek"}],"lexicalization_note":"Dinleme anlamı yalnızca belirtilen yönelmeli söz öbeğinde geçerlidir; yalın biçime genel işitme anlamı verilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalın dinleme dalı kısmi örtüşmeyi en iyi gösterir, diğerleri gizli ses, susarak dinleme, işitme zayıflığı veya anlamayı kapsayan farklı alanlardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal muhataba yöneltilmiş dinleme söz öbeğiyle sınırlıdır; komşu dal ise genel dinleme anlamını daha geniş biçimde kapsar.","focus_only":"İşitme dikkatini muhataba yönelten belirli söz öbeğiyle sınırlıdır.","gloss":"dinlemek","neighbor_only":"Genel dinleme alanını bildirir; muhataba yöneltilmiş söz öbeği sınırını zorunlu kılmaz.","neighbor_ref":"root_000832/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da işitme dikkatini bir söze yöneltip onu dinleme eylemini bildirir."}],"source_phrase_ar":"أدوا إلي بمعنى استمعوا إلي كأنه يقول أدوا إلي سمعكم؛ أد إلى بعضهم أي استمع إلى بعض من سبعت","source_summary":"Tek kaynak, işitmeyi konuşana yöneltme açıklamasıyla bu söz öbeğini dikkatle dinlemek anlamında tanıklar.","sources":["TA"],"what_is_ar":"إلقاء السمع إلى المخاطب والاستماع إليه","what_is_not_ar":"تسليم الأشخاص؛ أداء الحقوق؛ الاستعداء"},"support_links":[]},{"boundary":"Dal koyun veya deve sayısının azlığını bildirir; süt azlığı, sürünün herhangi bir büyüklüğü ya da genel değer düşüşü değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000021/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِدّ","morph_features":"STEM|POS:ADJ|LEM:<id~|ROOT:Add|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"19:89:4:1","qac_word_ref":"19:89:4","surface_ar":"إِدًّا"}],"gloss":"az sayıda koyun veya deve topluluğu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Koyun ya da deve topluluğu sayı bakımından küçük ve azdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir ad biçimi, az sayıdaki develerden oluşan tahmini bir grubu belirtir."}}],"root_ar":"ء د د","root_id":"root_000021","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Koyunların sayıca az oluşunu ve az sayıdaki develerden oluşan grubu birlikte temsil eder.","boundary_detail":"Dal koyun veya deve sayısının azlığını bildirir; süt azlığı, sürünün herhangi bir büyüklüğü ya da genel değer düşüşü değildir.","branch_image_ar":"قلة عدد","concept_gloss":"az sayıda koyun veya deve topluluğu","contextual_glosses":[{"applicability":"Koyun topluluğunun sayıca küçük olduğunu niteleyen söz öbeğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Az sayıdaki develeri belirten ad kullanımını kapsamaz.","preserves":"Koyun topluluğunun sayısal azlığını korur."},"facet_ids":["F001"],"text":"az sayıda koyun","usage_role":"contextual"}],"definition":"Koyun topluluğunun az sayıda olması veya develerden oluşan küçük bir sayısal grubun belirtilmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Koyun ya da deve topluluğu sayı bakımından küçük ve azdır."},{"facet_id":"F002","role":"specialization","statement":"Bir ad biçimi, az sayıdaki develerden oluşan tahmini bir grubu belirtir."}],"identity_rationale":"Kaynak ifadesi koyunların az sayıda oluşunu ve develer için az bir sayıyı belirten adı ortak nicelik çekirdeğinde açıkça birleştirir. Çerçeve hayvan türlerini genelleştirmeden bu azlık niteliğini korur.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"az sayıda koyun"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"az sayıdaki develerden oluşan grup"}],"lexicalization_note":"Azlık bir koyun söz öbeğinde ve az sayıdaki develeri belirten bir ad biçiminde tanıklanır; iki yapı kendi kapsamlarıyla korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; küçük deve sürüsü dalı sayısal sınırı en iyi açıklar, kalanlar süt azlığı, büyük sürü, genel eksilme veya hayvan malı alanındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği sayısal azlıktır ve koyunları da kapsar; komşu dal ise belirli bir küçük deve sürüsünü adlandırır.","focus_only":"Koyunların azlığını niteleyebilir ve develer için yaklaşık küçük bir sayı bildirir.","gloss":"küçük deve sürüsü","neighbor_only":"Çoğunlukla dişi develerden oluşan belirli türde küçük bir sürü adıdır ve kaynaklar sayı sınırında ayrılır.","neighbor_ref":"root_000524/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da az sayıdaki develerden oluşan bir topluluk alanına değinir."}],"source_phrase_ar":"غنم أدية على فعيلة أي قليلة (sihah)؛ غنم أدية أي قليلة؛ الأدية تقدير عدة من الإبل القليلة العدد (tahdhib)","source_summary":"Kaynaklar koyun topluluğunun az sayıda olduğunu bildirir; ayrıca bir ad biçimi az sayıdaki develerden oluşan tahmini grubu belirtir.","sources":["SI","TA"],"what_is_ar":"القلة في عدد الغنم أو الإبل","what_is_not_ar":"الأداة؛ أداء الحق؛ تتابع الموت"},"support_links":[]},{"boundary":"Dal tek bir kişinin ölümü değil, aynı topluluktaki ölümlerin peş peşe gerçekleşmesidir.","branch_kind":"collocation","branch_ref":"root_000021/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِدّ","morph_features":"STEM|POS:ADJ|LEM:<id~|ROOT:Add|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"19:89:4:1","qac_word_ref":"19:89:4","surface_ar":"إِدًّا"}],"gloss":"birbiri ardınca ölmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Aynı topluluktaki birden çok kişinin ölümü zaman içinde birbirini izler."}}],"root_ar":"ء د د","root_id":"root_000021","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir topluluğun birden çok üyesinin zaman içinde sırayla hayatını kaybetmesini karşılar.","boundary_detail":"Dal tek bir kişinin ölümü değil, aynı topluluktaki ölümlerin peş peşe gerçekleşmesidir.","branch_image_ar":"تتابع موت","concept_gloss":"birbiri ardınca ölmek","contextual_glosses":[{"applicability":"Aynı topluluğun üyelerinin farklı zamanlarda birbirini izleyerek öldüğü anlatımlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölümlerin aynı topluluk içinde sırayla gerçekleşmesini korur."},"facet_ids":["F001"],"text":"peş peşe hayatını kaybetmek","usage_role":"general"}],"definition":"Bir topluluğun üyelerinin aynı anda değil, biri öldükten sonra bir başkasının ölmesi biçiminde peş peşe hayatını kaybetmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Aynı topluluktaki birden çok kişinin ölümü zaman içinde birbirini izler."}],"identity_rationale":"Tek kaynak ifadesi bir topluluktaki kişilerin birbiri ardınca ölmesini doğrudan bildirir. Hazırlanan çerçeve hem çoklu katılımcıyı hem de ölümlerin sıra halinde gerçekleşmesini korur.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"topluluk üyeleri birbiri ardınca ölmek"}],"lexicalization_note":"Ardışık ölüm anlamı yalnızca topluluğu ve ölümü birlikte belirten tanıklanmış söz öbeğine aittir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel ölüm dalı tekil olay ile ardışık topluluk ölümü arasındaki farkı en açık gösterir, diğerleri ölüm türü, ölüm adı veya kader alanındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal çoklu ve ardışık ölümleri gerektirir; komşu dal tek bir ölüm olayını anlatabilir ve sıra ilişkisi taşımaz.","focus_only":"Bir topluluktaki birden çok ölümün zaman içinde birbirini izlemesini zorunlu kılar.","gloss":"ölmek ve yok olmak","neighbor_only":"Tek bir kişinin ölmesini, yok olmasını veya dünyadan ayrılmasını anlatabilir.","neighbor_ref":"root_001186/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişinin hayatını kaybetmesi olayını içerir."}],"source_phrase_ar":"تآدى القوم وتعادوا إذا تتابعوا موتا","source_summary":"Tek kaynak, bir topluluğun üyelerinin ölüm bakımından birbirini izlemesini ve birbiri ardınca hayatını kaybetmesini tanıklar.","sources":["TA"],"what_is_ar":"تتابع القوم موتا واحدا بعد آخر","what_is_not_ar":"التأهب والعدة؛ القلة؛ أداء الحقوق"},"support_links":[]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000281/B001","candidate_links":[{"candidate_id":"cand_2924bc8f9a653fbc4aa0","lane":"micro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_7aa3a41395452a873280","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Coming and occurring supplies the threshold crossed by the perfect verb.","root":"ج ي ء","source_ref":"19:89","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000281","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_474efbd6b059351771af"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000281/B004","candidate_links":[{"candidate_id":"cand_2ad97897c006e96d4255","lane":"micro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a9857488df8a9f1d3d53","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Bringing or presenting an object makes the second-person perfect an accomplished act of presentation.","root":"ج ي ء","source_ref":"19:89","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000281","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_f1c8cf2edea977b6945e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000831/B001","candidate_links":[{"candidate_id":"cand_2ad97897c006e96d4255","lane":"micro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a9857488df8a9f1d3d53","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A thing that can be known and reported gives the indefinite object evidentiary contour.","root":"ش ي ء","source_ref":"19:89","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000831","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_f1c8cf2edea977b6945e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000831/B002","candidate_links":[{"candidate_id":"cand_2924bc8f9a653fbc4aa0","lane":"micro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_7aa3a41395452a873280","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The branch linking thing and volition supplies the movement from formulation toward determinate existence.","root":"ش ي ء","source_ref":"19:89","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000831","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_474efbd6b059351771af"]}],"candidate_inventory":[{"anchor_refs":["19:89:1"],"branch_refs":[],"candidate_id":"cand_c79be3565e1221b91922","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:1:fused-particle-pressure","source_type":"word_analysis","support_ids":["sup_05fa60256111836fc939","sup_5247d859d81d1f54d031"],"title":"fused particle pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:1","qac_refs":["19:89:1:1"],"status":"accepted"}},{"anchor_refs":["19:89:1"],"branch_refs":[],"candidate_id":"cand_94278758a62242a9f3fb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:1:solemn-assertion-scope","source_type":"word_analysis","support_ids":["sup_05fa60256111836fc939","sup_2a32244581566574564c"],"title":"solemn assertion scope","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:1","qac_refs":["19:89:1:1"],"status":"accepted"}},{"anchor_refs":["19:89:1"],"branch_refs":[],"candidate_id":"cand_f283f1ab2c4d255daf00","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:1:verdict-opening","source_type":"word_analysis","support_ids":["sup_05fa60256111836fc939","sup_c9e5e52b8b5b439e05c5"],"title":"verdict opening","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:1","qac_refs":["19:89:1:1"],"status":"accepted"}},{"anchor_refs":["19:89:2"],"branch_refs":[],"candidate_id":"cand_342513408197a179b1be","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:2:compressed-certifying-beat","source_type":"word_analysis","support_ids":["sup_1aaad8b4bfd35e583752","sup_45f3144175ae9d100649"],"title":"compressed certifying beat","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:2","qac_refs":["19:89:1:2"],"status":"accepted"}},{"anchor_refs":["19:89:2"],"branch_refs":[],"candidate_id":"cand_d682b2737715658e799b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:2:loaded-assertion-frame","source_type":"word_analysis","support_ids":["sup_45f3144175ae9d100649","sup_9f68b776f50b5f468be4"],"title":"loaded assertion frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:2","qac_refs":["19:89:1:2"],"status":"accepted"}},{"anchor_refs":["19:89:2"],"branch_refs":[],"candidate_id":"cand_4987487b2a4f8c4da9ce","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:2:verified-completion","source_type":"word_analysis","support_ids":["sup_45f3144175ae9d100649","sup_64b56803be8edd5579ec"],"title":"verified completion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:2","qac_refs":["19:89:1:2"],"status":"accepted"}},{"anchor_refs":["19:89:3"],"branch_refs":[],"candidate_id":"cand_9cbfadbaa1fe7eadd967","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:3:compressed-charge-sound","source_type":"word_analysis","support_ids":["sup_8fac6a82382611e47bc8","sup_e8029d749947fdea5009"],"title":"compressed charge sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:3","qac_refs":["19:89:2:1","19:89:2:2"],"status":"accepted"}},{"anchor_refs":["19:89:3"],"branch_refs":[],"candidate_id":"cand_7a5ca7b5323d0bf80f43","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:3:direct-plural-confrontation","source_type":"word_analysis","support_ids":["sup_8fac6a82382611e47bc8","sup_b868ad0ae28c6578305f"],"title":"direct plural confrontation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:3","qac_refs":["19:89:2:1","19:89:2:2"],"status":"accepted"}},{"anchor_refs":["19:89:3"],"branch_refs":[],"candidate_id":"cand_472f733a6ed0e9fff7b7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:3:legitimate-coming-contrast","source_type":"word_analysis","support_ids":["sup_8fac6a82382611e47bc8","sup_a75e66a77fa818be41ad"],"title":"legitimate coming contrast","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:3","qac_refs":["19:89:2:1","19:89:2:2"],"status":"accepted"}},{"anchor_refs":["19:89:3"],"branch_refs":[],"candidate_id":"cand_b1983d7fbc01b00875f8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:3:surah-internal-escalation","source_type":"word_analysis","support_ids":["sup_8fac6a82382611e47bc8","sup_b107eeda4bb6e6b33e64"],"title":"surah-internal escalation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:3","qac_refs":["19:89:2:1","19:89:2:2"],"status":"accepted"}},{"anchor_refs":["19:89:3"],"branch_refs":[],"candidate_id":"cand_112760cc8a2b2487c38e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:3:transitive-produced-thing","source_type":"word_analysis","support_ids":["sup_8fac6a82382611e47bc8","sup_907104d019df8a1876da"],"title":"transitive produced thing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:3","qac_refs":["19:89:2:1","19:89:2:2"],"status":"accepted"}},{"anchor_refs":["19:89:3"],"branch_refs":[],"candidate_id":"cand_a2b2c4d6b24c91656a35","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:3:verdict-formula-echo","source_type":"word_analysis","support_ids":["sup_430455852161f2bddaed","sup_8fac6a82382611e47bc8"],"title":"verdict formula echo","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:3","qac_refs":["19:89:2:1","19:89:2:2"],"status":"accepted"}},{"anchor_refs":["19:89:3"],"branch_refs":[],"candidate_id":"cand_c3129bf86516dfe4577b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:3:verified-perfect-action","source_type":"word_analysis","support_ids":["sup_8fac6a82382611e47bc8","sup_deb106a01cf6bdd0aab8"],"title":"verified perfect action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:3","qac_refs":["19:89:2:1","19:89:2:2"],"status":"accepted"}},{"anchor_refs":["19:89:4"],"branch_refs":[],"candidate_id":"cand_fa367a924e6f83635df4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:4:broad-thinghood-selected","source_type":"word_analysis","support_ids":["sup_ec9875f41861e721a06c","sup_ee96aa76f6328c114048"],"title":"broad thinghood selected","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:4","qac_refs":["19:89:3:1"],"status":"accepted"}},{"anchor_refs":["19:89:4"],"branch_refs":[],"candidate_id":"cand_fea14d50772449635b19","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:4:formula-and-surah-scale","source_type":"word_analysis","support_ids":["sup_ee96aa76f6328c114048","sup_ff9f012a98c702599d1a"],"title":"formula and surah scale","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:4","qac_refs":["19:89:3:1"],"status":"accepted"}},{"anchor_refs":["19:89:4"],"branch_refs":[],"candidate_id":"cand_e45a98da9e72991570d7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:4:indefinite-class-verdict","source_type":"word_analysis","support_ids":["sup_99f264143e72752ae0e2","sup_ee96aa76f6328c114048"],"title":"indefinite class verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:4","qac_refs":["19:89:3:1"],"status":"accepted"}},{"anchor_refs":["19:89:4"],"branch_refs":[],"candidate_id":"cand_2e2d8b94b496adc831b6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:4:inversion-and-contrast","source_type":"word_analysis","support_ids":["sup_c792b9cc56066b4993f4","sup_ee96aa76f6328c114048"],"title":"inversion and contrast","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:4","qac_refs":["19:89:3:1"],"status":"accepted"}},{"anchor_refs":["19:89:4"],"branch_refs":[],"candidate_id":"cand_52f8d853aa578c5ab87d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:4:object-attachment","source_type":"word_analysis","support_ids":["sup_6fe4b55c6f82fc1b587b","sup_ee96aa76f6328c114048"],"title":"object attachment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:4","qac_refs":["19:89:3:1"],"status":"accepted"}},{"anchor_refs":["19:89:4"],"branch_refs":[],"candidate_id":"cand_6a9475d03b0f7079f0c9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:4:sound-binding","source_type":"word_analysis","support_ids":["sup_ed193103d2b98df466c6","sup_ee96aa76f6328c114048"],"title":"sound binding","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:4","qac_refs":["19:89:3:1"],"status":"accepted"}},{"anchor_refs":["19:89:4"],"branch_refs":[],"candidate_id":"cand_11fa90aa96758f45f8a7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:4:thing-to-verdict-bond","source_type":"word_analysis","support_ids":["sup_ee96aa76f6328c114048","sup_ef20fde338f85866aed9"],"title":"thing-to-verdict bond","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:4","qac_refs":["19:89:3:1"],"status":"accepted"}},{"anchor_refs":["19:89:5"],"branch_refs":[],"candidate_id":"cand_d0bfa272d930126318fe","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:5:abstract-rare-form","source_type":"word_analysis","support_ids":["sup_01feabfaf036a9cc45ed","sup_41ae5a37cf3f14c1e326"],"title":"abstract rare form","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:5","qac_refs":["19:89:4:1"],"status":"accepted"}},{"anchor_refs":["19:89:5"],"branch_refs":[],"candidate_id":"cand_618fc31cdb8116b628e5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:5:accusative-qualifier-identity-pressure","source_type":"word_analysis","support_ids":["sup_3fab8ea46d2a442895d0","sup_41ae5a37cf3f14c1e326"],"title":"accusative qualifier identity pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:5","qac_refs":["19:89:4:1"],"status":"accepted"}},{"anchor_refs":["19:89:5"],"branch_refs":[],"candidate_id":"cand_1dded432f27f5960abb0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:5:boundary-and-forward-pressure","source_type":"word_analysis","support_ids":["sup_41ae5a37cf3f14c1e326","sup_b0bd33c47ee0e180fe28"],"title":"boundary and forward pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:5","qac_refs":["19:89:4:1"],"status":"accepted"}},{"anchor_refs":["19:89:5"],"branch_refs":[],"candidate_id":"cand_bcb28c93674cf7c8c24d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:5:catastrophic-verdict-sense","source_type":"word_analysis","support_ids":["sup_41ae5a37cf3f14c1e326","sup_4ef5fc8fd112942906f8"],"title":"catastrophic verdict sense","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:5","qac_refs":["19:89:4:1"],"status":"accepted"}},{"anchor_refs":["19:89:5"],"branch_refs":[],"candidate_id":"cand_5413eb476ad8af75ad94","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:5:final-closure-weight","source_type":"word_analysis","support_ids":["sup_41ae5a37cf3f14c1e326","sup_ed3223fac7468f63b861"],"title":"final closure weight","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:5","qac_refs":["19:89:4:1"],"status":"accepted"}},{"anchor_refs":["19:89:5"],"branch_refs":[],"candidate_id":"cand_1e5640e32cfb6ee815b1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:5:hard-pressure-sound","source_type":"word_analysis","support_ids":["sup_41ae5a37cf3f14c1e326","sup_e7bc41bc304d5db142e7"],"title":"hard pressure sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:5","qac_refs":["19:89:4:1"],"status":"accepted"}},{"anchor_refs":["19:89:5"],"branch_refs":[],"candidate_id":"cand_14534425858b711b489c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:5:indefinite-phrase-unit","source_type":"word_analysis","support_ids":["sup_41ae5a37cf3f14c1e326","sup_c972e251a089f78c60d1"],"title":"indefinite phrase unit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:5","qac_refs":["19:89:4:1"],"status":"accepted"}},{"anchor_refs":["19:89:5"],"branch_refs":[],"candidate_id":"cand_aeb1d6cb143cfa776062","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:5:qiraat-stable-pressure","source_type":"word_analysis","support_ids":["sup_30df3e6dc255bb708e6f","sup_41ae5a37cf3f14c1e326"],"title":"qiraat stable pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:5","qac_refs":["19:89:4:1"],"status":"accepted"}},{"anchor_refs":["19:89:5"],"branch_refs":[],"candidate_id":"cand_2ab83e33094c4be79386","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:5:rare-pairing-and-root-contrast","source_type":"word_analysis","support_ids":["sup_1a2a6909e72608345fd6","sup_41ae5a37cf3f14c1e326"],"title":"rare pairing and root contrast","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:5","qac_refs":["19:89:4:1"],"status":"accepted"}},{"anchor_refs":["19:89:5"],"branch_refs":[],"candidate_id":"cand_2b2213e228b4bb7d4667","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"19:89:5:verdict-series-escalation","source_type":"word_analysis","support_ids":["sup_26a8b9af1fa7ab77fb5f","sup_41ae5a37cf3f14c1e326"],"title":"verdict series escalation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"19:89:5","qac_refs":["19:89:4:1"],"status":"accepted"}},{"anchor_refs":["19:89:2"],"branch_refs":[],"candidate_id":"cand_f5cb5d2e0f1074400775","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000281"],"scope":"focus_ayah","source_local_id":"19:89:2:1","source_type":"qac_morpheme","support_ids":["sup_e677310070e53dc39ca1"],"title":"QAC root occurrence: ج ي ء","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["19:89:3"],"branch_refs":[],"candidate_id":"cand_f94619ba7ea0af3c79c0","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000831"],"scope":"focus_ayah","source_local_id":"19:89:3:1","source_type":"qac_morpheme","support_ids":["sup_b988e7cd35874d6400d1"],"title":"QAC root occurrence: ش ي ء","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["19:89:4"],"branch_refs":[],"candidate_id":"cand_7dbb03e91689b226c328","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000021"],"scope":"focus_ayah","source_local_id":"19:89:4:1","source_type":"qac_morpheme","support_ids":["sup_b3d0ad6526ac86a629c5"],"title":"QAC root occurrence: ء د د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["19:89"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"19:89","branch_refs":["root_000021/B001","root_000281/B004","root_000831/B001"],"candidate_id":"cand_2ad97897c006e96d4255","commentary_obligation":"review","hft_ref":"hft_a9857488df8a9f1d3d53","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_presented_object","source_type":"hft","support_ids":["sup_f1c8cf2edea977b6945e"],"title":"baseline_presented_object","trust":"legacy_unbound"},{"anchor_refs":["19:89"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"19:89","branch_refs":["root_000281/B001","root_000831/B002"],"candidate_id":"cand_2924bc8f9a653fbc4aa0","commentary_obligation":"review","hft_ref":"hft_7aa3a41395452a873280","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_arrived_possibility","source_type":"hft","support_ids":["sup_474efbd6b059351771af"],"title":"baseline_arrived_possibility","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"لَّقَدْ جِئْتُمْ شَيْـًٔا إِدًّۭا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"19:89:1:1","qac_word_ref":"19:89:1","root_ar":"","surface_ar":"لَّ"},{"lemma_ar":"قَد","morph_features":"STEM|POS:CERT|LEM:qad","morpheme_role":"STEM","pos":"CERT","qac_ref":"19:89:1:2","qac_word_ref":"19:89:1","root_ar":"","surface_ar":"قَدْ"},{"lemma_ar":"جَآءَ","morph_features":"STEM|POS:V|PERF|LEM:jaA^'a|ROOT:jyA|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"19:89:2:1","qac_word_ref":"19:89:2","root_ar":"ج ي ء","surface_ar":"جِئْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"19:89:2:2","qac_word_ref":"19:89:2","root_ar":"","surface_ar":"تُمْ"},{"lemma_ar":"شَىْء","morph_features":"STEM|POS:N|LEM:$aYo'|ROOT:$yA|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"19:89:3:1","qac_word_ref":"19:89:3","root_ar":"ش ي ء","surface_ar":"شَيْـًٔا"},{"lemma_ar":"إِدّ","morph_features":"STEM|POS:ADJ|LEM:<id~|ROOT:Add|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"19:89:4:1","qac_word_ref":"19:89:4","root_ar":"ء د د","surface_ar":"إِدًّا"}],"word_analysis_qac_refs":[["19:89:1:1"],["19:89:1:2"],["19:89:2:1","19:89:2:2"],["19:89:3:1"],["19:89:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["19:89:1","19:89:2","19:89:3","19:89:4","19:89:5"]},"focus_surface_evidence":{"arabic_uthmani":"لَّقَدْ جِئْتُمْ شَيْـًٔا إِدًّۭا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"19:89:1:1","qac_word_ref":"19:89:1","root_ar":"","surface_ar":"لَّ"},{"lemma_ar":"قَد","morph_features":"STEM|POS:CERT|LEM:qad","morpheme_role":"STEM","pos":"CERT","qac_ref":"19:89:1:2","qac_word_ref":"19:89:1","root_ar":"","surface_ar":"قَدْ"},{"lemma_ar":"جَآءَ","morph_features":"STEM|POS:V|PERF|LEM:jaA^'a|ROOT:jyA|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"19:89:2:1","qac_word_ref":"19:89:2","root_ar":"ج ي ء","surface_ar":"جِئْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"19:89:2:2","qac_word_ref":"19:89:2","root_ar":"","surface_ar":"تُمْ"},{"lemma_ar":"شَىْء","morph_features":"STEM|POS:N|LEM:$aYo'|ROOT:$yA|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"19:89:3:1","qac_word_ref":"19:89:3","root_ar":"ش ي ء","surface_ar":"شَيْـًٔا"},{"lemma_ar":"إِدّ","morph_features":"STEM|POS:ADJ|LEM:<id~|ROOT:Add|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"19:89:4:1","qac_word_ref":"19:89:4","root_ar":"ء د د","surface_ar":"إِدًّا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["19:89:1:1"],["19:89:1:2"],["19:89:2:1","19:89:2:2"],["19:89:3:1"],["19:89:4:1"]],"word_analysis_refs":["19:89:1","19:89:2","19:89:3","19:89:4","19:89:5"],"word_rows":[{"analysis_record_ref":"19:89:1","analytic_gloss_range_en":"emphatic prefixed particle that loads the following clause with solemn assertion","analytic_root_gloss_range_en":null,"qac_refs":["19:89:1:1"],"root":{"note":"no lexical root (particle or function word)"},"surface":{"arabic":"لَّ","transliteration":"la-"}},{"analysis_record_ref":"19:89:2","analytic_gloss_range_en":"certainty particle with perfect verb, marking the charge as completed and verified","analytic_root_gloss_range_en":null,"qac_refs":["19:89:1:2"],"root":{"note":"no lexical root (particle or function word)"},"surface":{"arabic":"قَدْ","transliteration":"qad"}},{"analysis_record_ref":"19:89:3","analytic_gloss_range_en":"perfect second-person plural transitive bringing or presenting within a direct accusation","analytic_root_gloss_range_en":"coming, arriving, or bringing; locally the explicit object selects bringing or presenting rather than intransitive arrival","qac_refs":["19:89:2:1","19:89:2:2"],"root":{"arabic":"ج ي أ","transliteration":"j-y-ʾ"},"surface":{"arabic":"جِئْتُمْ","transliteration":"jiʾtum"}},{"analysis_record_ref":"19:89:4","analytic_gloss_range_en":"indefinite accusative object, a broad thing or matter made available for the final qualifier","analytic_root_gloss_range_en":"general knowable or reportable thing, with other root branches such as willing, exclamation, listening, and young palms not locally activated by this noun-object frame","qac_refs":["19:89:3:1"],"root":{"arabic":"ش ي ء","transliteration":"sh-y-ʾ"},"surface":{"arabic":"شَيْئَاً","transliteration":"shayʾan"}},{"analysis_record_ref":"19:89:5","analytic_gloss_range_en":"rare accusative qualifier naming the brought thing as monstrous, calamitous, and weighty","analytic_root_gloss_range_en":"limited guardrail data for this root; CRITICAL evidence supports a rare verdict form with calamity, hard-pressure, and extreme severity locally selected as the qualifier of the object","qac_refs":["19:89:4:1"],"root":{"arabic":"أ د ي","transliteration":"ʾ-d-y"},"surface":{"arabic":"إِدًّۭا","transliteration":"iddan"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":2,"assigned_records":[{"anchor_refs":["19:89"],"branch_refs":["root_000021/B001","root_000281/B004","root_000831/B001"],"candidate_id":"cand_2ad97897c006e96d4255","evidence_scope":"focus_ayah","hft_ref":"hft_a9857488df8a9f1d3d53","item_id":"baseline_presented_object","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_presented_object","support_id":"sup_f1c8cf2edea977b6945e"},{"anchor_refs":["19:89"],"branch_refs":["root_000281/B001","root_000831/B002"],"candidate_id":"cand_2924bc8f9a653fbc4aa0","evidence_scope":"focus_ayah","hft_ref":"hft_7aa3a41395452a873280","item_id":"baseline_arrived_possibility","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_arrived_possibility","support_id":"sup_474efbd6b059351771af"}],"diagnostics":[],"lane_counts":{"global":7,"macro":8,"micro":2},"packet_summary":{"ayah_count":22,"focus_ref":"19:89","protocol":"focus-trace-pericope-lean-v1","split_root_mappings":[],"window":["19:77","19:78","19:79","19:80","19:81","19:82","19:83","19:84","19:85","19:86","19:87","19:88","19:89","19:90","19:91","19:92","19:93","19:94","19:95","19:96","19:97","19:98"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"valid_pericope_packet_unbound_response"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"19:89","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":7,"source_present":true,"structured_insight_count":10,"unstructured_record_count":0},"identity":{"ayah_ref":"19:89","lane":"micro","linguistic_source_ref":"19:89","surface_ref":"19:89","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"19:89","target_tokens":[["Gerçekten",["19:89:1"]],["çok",["19:89:1","19:89:2"]],["çirkin",["19:89:2"]],["bir",["19:89:2","19:89:3"]],["şey",["19:89:3"]],["ortaya",["19:89:3","19:89:4"]],["attınız",["19:89:4"]]],"text":"Gerçekten çok çirkin bir şey ortaya attınız."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":2,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":77,"ayah_to":98,"id":"s019-p05-077-098","label":"Boastful deniers and divine inheritance","number":5,"refs":["19:77","19:78","19:79","19:80","19:81","19:82","19:83","19:84","19:85","19:86","19:87","19:88","19:89","19:90","19:91","19:92","19:93","19:94","19:95","19:96","19:97","19:98"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:5:abstract-rare-form","source_type":"word_analysis","support_id":"sup_01feabfaf036a9cc45ed","text":"{\"blocking_evidence\":null,\"headline\":\"abstract rare form\",\"reader_payoff\":\"The reader notices that a rare abstract nominal form carries the whole closing verdict.\",\"reason\":\"QAC and contextual evidence mark the local item as a low-occurrence abstract noun used adjectivally after {{ar:شَيْئَاً}} ({{tr:shayʾan}}).\",\"representative_source_ids\":[\"QF-1f19b3ff\",\"QI-480bf659\",\"QH-c9bd2e17\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:1","source_type":"word_analysis","support_id":"sup_05fa60256111836fc939","text":"{\"gloss_range\":\"emphatic prefixed particle that loads the following clause with solemn assertion\",\"prose\":\"{{ar:لَّ}} ({{tr:la-}}) begins the response as verdict rather than narration. As the front half of {{ar:لَّقَدْ}} ({{tr:laqad}}), it gives the compact clause an emphatic, oath-answer force before the verb appears, so the charge is not introduced as another report of speech but as a certified counter-statement to 19:88. Its fusion onto the next particle makes assertion part of the opening sound, and the short movement into {{ar:قَدْ}} ({{tr:qad}}) tightens the clause before the direct accusation unfolds.\",\"root_display\":\"no lexical root (particle or function word)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَّ}} ({{tr:la-}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:5:rare-pairing-and-root-contrast","source_type":"word_analysis","support_id":"sup_1a2a6909e72608345fd6","text":"{\"blocking_evidence\":null,\"headline\":\"rare pairing and root contrast\",\"reader_payoff\":\"The reader notices that this rare form is tightly bound to the thing-word while wider root contrasts stay secondary.\",\"reason\":\"Contextual evidence marks the form as low occurrence, but V4 has no root rows for {{ar:أ د ي}} ({{tr:ʾ-d-y}}), so cross-root comparisons such as 2:178 are kept as contrast rather than as local sense activation.\",\"representative_source_ids\":[\"QI-62ddf0ac\",\"QI-bb54f16c\",\"MH-a26d4db2\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:2:compressed-certifying-beat","source_type":"word_analysis","support_id":"sup_1aaad8b4bfd35e583752","text":"{\"blocking_evidence\":null,\"headline\":\"compressed certifying beat\",\"reader_payoff\":\"The reader notices the brief recitational catch that turns the prior speech into an established charge.\",\"reason\":\"The CRITICAL pacing rows are coherent with the short closed particle and its position between assertion and verb.\",\"representative_source_ids\":[\"QF-2d054256\",\"QP-efb850e0\",\"QB-3b2589b5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:5:verdict-series-escalation","source_type":"word_analysis","support_id":"sup_26a8b9af1fa7ab77fb5f","text":"{\"blocking_evidence\":null,\"headline\":\"verdict series escalation\",\"reader_payoff\":\"The reader notices that 19:89 takes the evaluated-thing formula to a severe endpoint after parallels in 18:71, 18:74, and 19:27.\",\"reason\":\"The rows provide concrete inter-ayah references and remain comparative; they do not override the local syntax of {{ar:إِدًّۭا}} ({{tr:iddan}}).\",\"representative_source_ids\":[\"QE-d30d16b9\",\"QE-dc65b7a3\",\"MT-20c22e2c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:1:solemn-assertion-scope","source_type":"word_analysis","support_id":"sup_2a32244581566574564c","text":"{\"blocking_evidence\":null,\"headline\":\"solemn assertion scope\",\"reader_payoff\":\"The reader notices that the ayah opens with a solemn assertion whose force reaches across the whole verb-object-verdict clause.\",\"reason\":\"QAC identifies the word as emphatic lām and the attachment evidence treats the whole ayah as one emphatic verbal clause, so the CRITICAL oath-answer and assertion-scope claims are locally licensed.\",\"representative_source_ids\":[\"QG-c95d854a\",\"QG-d1e5fccf\",\"QS-ecf39b38\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:5:qiraat-stable-pressure","source_type":"word_analysis","support_id":"sup_30df3e6dc255bb708e6f","text":"{\"blocking_evidence\":null,\"headline\":\"qiraat stable pressure\",\"reader_payoff\":\"The reader notices that the cited variant changes vowel color while preserving the consonantal pressure of the verdict.\",\"reason\":\"The qiraat rows are useful apparatus, but the canonical local surface remains {{ar:إِدًّۭا}} ({{tr:iddan}}), so the variant is limited to contrast.\",\"representative_source_ids\":[\"QF-2e6f47c4\",\"QF-cf6048ed\",\"QP-941898a2\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:5:accusative-qualifier-identity-pressure","source_type":"word_analysis","support_id":"sup_3fab8ea46d2a442895d0","text":"{\"blocking_evidence\":null,\"headline\":\"accusative qualifier identity pressure\",\"reader_payoff\":\"The reader notices that the final word both qualifies the object and nearly lets the judgment become the object's identity.\",\"reason\":\"Attachment evidence strongly licenses adjective agreement, so badal pressure is preserved as interpretive pressure rather than allowed to displace the local qualifier relation.\",\"representative_source_ids\":[\"QG-0173e388\",\"QG-5e882775\",\"QG-d29f8e12\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:5","source_type":"word_analysis","support_id":"sup_41ae5a37cf3f14c1e326","text":"{\"gloss_range\":\"rare accusative qualifier naming the brought thing as monstrous, calamitous, and weighty\",\"prose\":\"{{ar:إِدًّۭا}} ({{tr:iddan}}) is the ayah's final verdict word. It agrees with {{ar:شَيْئَاً}} ({{tr:shayʾan}}) as an indefinite accusative qualifier, while the possible substitute-pressure lets the verdict almost identify the thing itself; the stronger guardrail remains adjectival attachment. The word supplies the only overt evaluative term, selecting catastrophic gravity rather than ordinary badness. Its rare form, doubled {{ar:د}} ({{tr:d}}), and end-position converge so the condemnation is understood, heard, and placed as weight. The cited {{ar:أَدًّا}} ({{tr:addan}}) variant changes the opening vowel but keeps the hamza, doubled {{ar:د}} ({{tr:d}}), and tanwīn, so the pressure rests in the consonantal shape rather than one vowel. The rare pairing with {{ar:شَيْئَاً}} ({{tr:shayʾan}}) is primary here, while the wider root contrast with legal fulfillment in 2:178 remains secondary apparatus. It also answers the evaluated-thing series in 18:71 and 18:74 and escalates the same-surah frame of 19:27, while its closing gravity presses forward into the rupture imagery of 19:90.\",\"root_display\":\"{{ar:أ د ي}} ({{tr:ʾ-d-y}})\",\"root_gloss_range\":\"limited guardrail data for this root; CRITICAL evidence supports a rare verdict form with calamity, hard-pressure, and extreme severity locally selected as the qualifier of the object\",\"surface_display\":\"{{ar:إِدًّۭا}} ({{tr:iddan}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:3:verdict-formula-echo","source_type":"word_analysis","support_id":"sup_430455852161f2bddaed","text":"{\"blocking_evidence\":null,\"headline\":\"verdict formula echo\",\"reader_payoff\":\"The reader notices that 19:89 joins a known bring-a-thing verdict formula while escalating its addressee and qualifier.\",\"reason\":\"The CRITICAL echo rows give concrete references, and no guardrail evidence contradicts a formulaic comparison when it remains a parallel rather than the local parse.\",\"representative_source_ids\":[\"QI-3a089366\",\"MI-05d0b7a1\",\"QE-335d5e44\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:2","source_type":"word_analysis","support_id":"sup_45f3144175ae9d100649","text":"{\"gloss_range\":\"certainty particle with perfect verb, marking the charge as completed and verified\",\"prose\":\"{{ar:قَدْ}} ({{tr:qad}}) completes the opening assertion frame. With the perfect verb {{ar:جِئْتُمْ}} ({{tr:jiʾtum}}), it makes the act a settled, verified completion, not a possibility, an ongoing process, or another quotation. Its short closed beat sits between the emphatic lām and the verb, so the ayah briefly loads certainty before naming what the addressees have brought.\",\"root_display\":\"no lexical root (particle or function word)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:قَدْ}} ({{tr:qad}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:5:catastrophic-verdict-sense","source_type":"word_analysis","support_id":"sup_4ef5fc8fd112942906f8","text":"{\"blocking_evidence\":null,\"headline\":\"catastrophic verdict sense\",\"reader_payoff\":\"The reader notices that the closing adjective names catastrophic gravity, not a mild or generic moral flaw.\",\"reason\":\"The CRITICAL semantic rows are coherent with the word's role as the sole overt evaluative qualifier and are not contradicted by the compact guardrails.\",\"representative_source_ids\":[\"QS-39542ded\",\"QS-5a1a6e4b\",\"QS-c5e198b5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:1:fused-particle-pressure","source_type":"word_analysis","support_id":"sup_5247d859d81d1f54d031","text":"{\"blocking_evidence\":null,\"headline\":\"fused particle pressure\",\"reader_payoff\":\"The reader notices that confirmation is stacked and heard before the accusation itself begins.\",\"reason\":\"The surface sequence combines emphatic lām with {{ar:قَدْ}} ({{tr:qad}}), and the sound row adds a local pacing observation without changing the grammar.\",\"representative_source_ids\":[\"QF-8bbaec92\",\"QI-a8070368\",\"QP-591489c6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:2:verified-completion","source_type":"word_analysis","support_id":"sup_64b56803be8edd5579ec","text":"{\"blocking_evidence\":null,\"headline\":\"verified completion\",\"reader_payoff\":\"The reader notices that the charge is treated as already completed and available for judgment.\",\"reason\":\"QAC marks {{ar:قَدْ}} ({{tr:qad}}) as a certainty particle before a perfect verb, supporting the CRITICAL completion and verification rows.\",\"representative_source_ids\":[\"QG-51b89c6c\",\"QG-8e91d494\",\"QS-8a5e4655\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:4:object-attachment","source_type":"word_analysis","support_id":"sup_6fe4b55c6f82fc1b587b","text":"{\"blocking_evidence\":null,\"headline\":\"object attachment\",\"reader_payoff\":\"The reader notices that the broad noun is grammatically attached to the addressees' action as produced content.\",\"reason\":\"The CRITICAL row allowing object or circumstantial force is narrowed because attachment evidence syntactically forces the direct-object relation.\",\"representative_source_ids\":[\"QG-81b92827\",\"QS-caa4f984\",\"QT-f7e33510\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:3","source_type":"word_analysis","support_id":"sup_8fac6a82382611e47bc8","text":"{\"gloss_range\":\"perfect second-person plural transitive bringing or presenting within a direct accusation\",\"prose\":\"{{ar:جِئْتُمْ}} ({{tr:jiʾtum}}) is the only finite verb in the ayah, so the whole action load is concentrated in one direct-address perfect. The suffix makes the third-person report of 19:88 face the claimants as plural addressees, and the explicit object {{ar:شَيْئَاً}} ({{tr:shayʾan}}) narrows the verb from simple arrival to bringing or presenting something for judgment. This keeps agency visible: the claim is treated as a produced thing, not just words that happened. The formula also recalls {{ar:جِئْتِ شَيْئَاً فَرِيًّا}} ({{tr:jiʾti shayʾan fariyyan}}) in 19:27 and the {{ar:جِئْتَ شَيْئَاً}} ({{tr:jiʾta shayʾan}}) verdict pattern in 18:71 and 18:74, but 19:89 shifts the address to plural and moves the scale to the heavier closing verdict. A further contrast with legitimate prophetic coming in 20:47 keeps the local use from sounding neutral: here the coming verb carries an illegitimate theological claim into judgment.\",\"root_display\":\"{{ar:ج ي أ}} ({{tr:j-y-ʾ}})\",\"root_gloss_range\":\"coming, arriving, or bringing; locally the explicit object selects bringing or presenting rather than intransitive arrival\",\"surface_display\":\"{{ar:جِئْتُمْ}} ({{tr:jiʾtum}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:3:transitive-produced-thing","source_type":"word_analysis","support_id":"sup_907104d019df8a1876da","text":"{\"blocking_evidence\":null,\"headline\":\"transitive produced thing\",\"reader_payoff\":\"The reader notices that the claim is treated as something the speakers have brought forward and are responsible for.\",\"reason\":\"Attachment evidence syntactically forces {{ar:شَيْئَاً}} ({{tr:shayʾan}}) as the direct object, so the local frame selects transitive presentation rather than bare intransitive coming.\",\"representative_source_ids\":[\"MG-242cde60\",\"QS-41f858c7\",\"QS-b1419935\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:4:indefinite-class-verdict","source_type":"word_analysis","support_id":"sup_99f264143e72752ae0e2","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite class verdict\",\"reader_payoff\":\"The reader notices that the indefinite object generalizes the condemnation into a class of such claims.\",\"reason\":\"QAC marks the noun as indefinite accusative, and the following agreeing indefinite qualifier supports the class-bearing payoff.\",\"representative_source_ids\":[\"QG-e242ca46\",\"MG-9da685fa\",\"QF-52fba76c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:2:loaded-assertion-frame","source_type":"word_analysis","support_id":"sup_9f68b776f50b5f468be4","text":"{\"blocking_evidence\":null,\"headline\":\"loaded assertion frame\",\"reader_payoff\":\"The reader notices that the two opening particles form a certifying threshold before the action is stated.\",\"reason\":\"The particle is explicitly paired with emphatic lām in the input, and the attachment support warns that omitting {{ar:لَّقَدْ}} ({{tr:laqad}}) weakens the rebuke.\",\"representative_source_ids\":[\"QI-4a3ab5ae\",\"QT-248b3420\",\"QT-da732c7a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:3:legitimate-coming-contrast","source_type":"word_analysis","support_id":"sup_a75e66a77fa818be41ad","text":"{\"blocking_evidence\":null,\"headline\":\"legitimate coming contrast\",\"reader_payoff\":\"The reader notices that the same broad coming verb can frame legitimate prophetic arrival in 20:47 and an illegitimate claim here.\",\"reason\":\"The row provides a concrete contrast at 20:47; it is kept as a lexical contrast, not as a claim that the local sense is prophetic coming.\",\"representative_source_ids\":[\"ME-767ea487\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:5:boundary-and-forward-pressure","source_type":"word_analysis","support_id":"sup_b0bd33c47ee0e180fe28","text":"{\"blocking_evidence\":null,\"headline\":\"boundary and forward pressure\",\"reader_payoff\":\"The reader notices that the final verdict completes the move from quoted claim to bare judgment and presses into the rupture imagery of 19:90.\",\"reason\":\"The boundary rows cohere with the local final position and with the prior claim in 19:88 and next-ayah rupture imagery in 19:90.\",\"representative_source_ids\":[\"QB-1bbd2b81\",\"QB-a1af50a2\",\"QB-a6492240\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:3:surah-internal-escalation","source_type":"word_analysis","support_id":"sup_b107eeda4bb6e6b33e64","text":"{\"blocking_evidence\":null,\"headline\":\"surah-internal escalation\",\"reader_payoff\":\"The reader notices that the accusation formula from 19:27 returns with a changed addressee and a harsher theological register.\",\"reason\":\"The rows give a concrete same-surah parallel at 19:27, and the local morphology supports the shift from singular feminine to plural masculine address.\",\"representative_source_ids\":[\"MI-1629b8b6\",\"MT-8ec1b682\",\"QE-12a207eb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"19:89:4:1","source_type":"qac_morpheme","support_id":"sup_b3d0ad6526ac86a629c5","text":"{\"lemma_ar\":\"إِدّ\",\"morph_features\":\"STEM|POS:ADJ|LEM:<id~|ROOT:Add|MS|INDEF|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"19:89:4:1\",\"qac_word_ref\":\"19:89:4\",\"root_ar\":\"ء د د\",\"surface_ar\":\"إِدًّا\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:3:direct-plural-confrontation","source_type":"word_analysis","support_id":"sup_b868ad0ae28c6578305f","text":"{\"blocking_evidence\":null,\"headline\":\"direct plural confrontation\",\"reader_payoff\":\"The reader notices the turn from reported third-person claim to face-to-face plural accusation.\",\"reason\":\"The verb carries second-person plural masculine agreement while attachment evidence keeps the subject morphologically present rather than separately named.\",\"representative_source_ids\":[\"QG-0ab12197\",\"MG-7c022148\",\"QI-7222bdaa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"19:89:3:1","source_type":"qac_morpheme","support_id":"sup_b988e7cd35874d6400d1","text":"{\"lemma_ar\":\"شَىْء\",\"morph_features\":\"STEM|POS:N|LEM:$aYo'|ROOT:$yA|M|INDEF|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"19:89:3:1\",\"qac_word_ref\":\"19:89:3\",\"root_ar\":\"ش ي ء\",\"surface_ar\":\"شَيْـًٔا\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:4:inversion-and-contrast","source_type":"word_analysis","support_id":"sup_c792b9cc56066b4993f4","text":"{\"blocking_evidence\":null,\"headline\":\"inversion and contrast\",\"reader_payoff\":\"The reader notices that the ordinary word for thing can move from divine creative or knowledge frames into the object of condemnation here.\",\"reason\":\"The contrast rows provide concrete references such as 19:9, 19:43, 24:39, and 8:19; they are useful lexical contrasts so long as they do not override the local direct-object sense.\",\"representative_source_ids\":[\"MS-08d9f164\",\"MI-4b7d1276\",\"MT-45d40a97\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:5:indefinite-phrase-unit","source_type":"word_analysis","support_id":"sup_c972e251a089f78c60d1","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite phrase unit\",\"reader_payoff\":\"The reader notices that matching indefiniteness and cadence make the object and qualifier one verdict phrase.\",\"reason\":\"Both words are marked accusative indefinite, and attachment evidence makes the phrase a construction unit rather than two separate objects.\",\"representative_source_ids\":[\"MG-ffb58d0a\",\"QF-f5d85a9d\",\"QP-e12035fd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:1:verdict-opening","source_type":"word_analysis","support_id":"sup_c9e5e52b8b5b439e05c5","text":"{\"blocking_evidence\":null,\"headline\":\"verdict opening\",\"reader_payoff\":\"The reader notices the discourse shift from quoted claim in 19:88 to direct prosecutorial response in 19:89.\",\"reason\":\"The opening particle precedes the sole verbal clause and matches the CRITICAL boundary rows that read the ayah as a formal counter-verdict after the reported claim.\",\"representative_source_ids\":[\"QT-9c4319cc\",\"QB-69ab1bc1\",\"QB-b277c5ff\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:3:verified-perfect-action","source_type":"word_analysis","support_id":"sup_deb106a01cf6bdd0aab8","text":"{\"blocking_evidence\":null,\"headline\":\"verified perfect action\",\"reader_payoff\":\"The reader notices that the action is completed and concentrated in the ayah's single finite verb.\",\"reason\":\"QAC marks the verb as perfect, and attachment evidence places it as the head of the only verbal clause with an explicit object.\",\"representative_source_ids\":[\"QG-038b3c5c\",\"QF-55c53553\",\"QT-624d6e54\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"19:89:2:1","source_type":"qac_morpheme","support_id":"sup_e677310070e53dc39ca1","text":"{\"lemma_ar\":\"جَآءَ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:jaA^'a|ROOT:jyA|2MP\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"19:89:2:1\",\"qac_word_ref\":\"19:89:2\",\"root_ar\":\"ج ي ء\",\"surface_ar\":\"جِئْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:5:hard-pressure-sound","source_type":"word_analysis","support_id":"sup_e7bc41bc304d5db142e7","text":"{\"blocking_evidence\":null,\"headline\":\"hard pressure sound\",\"reader_payoff\":\"The reader notices that the doubled consonant makes the severity feel compressed and weighty in the mouth.\",\"reason\":\"The shaddah on the local surface supports the phonetic pressure rows while the semantic rows keep the observation tied to calamitous gravity.\",\"representative_source_ids\":[\"QS-49ee8d56\",\"MS-af0c4980\",\"QP-a2f2fb1a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:3:compressed-charge-sound","source_type":"word_analysis","support_id":"sup_e8029d749947fdea5009","text":"{\"blocking_evidence\":null,\"headline\":\"compressed charge sound\",\"reader_payoff\":\"The reader notices an audible catch inside the verb as the clause turns from assertion to accusation.\",\"reason\":\"The internal hamza is present in the local surface and can support a sound-level observation without changing lexical sense.\",\"representative_source_ids\":[\"QF-694c616c\",\"QP-3565a3c7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:4:broad-thinghood-selected","source_type":"word_analysis","support_id":"sup_ec9875f41861e721a06c","text":"{\"blocking_evidence\":null,\"headline\":\"broad thinghood selected\",\"reader_payoff\":\"The reader notices that an ordinary broad noun becomes a grave matter only through the local object-and-qualifier frame.\",\"reason\":\"V4 preserves a general thing branch for {{ar:ش ي ء}} ({{tr:sh-y-ʾ}}), while other branch images are not activated by the local noun-object frame; the qualifier supplies the grave evaluative selection.\",\"representative_source_ids\":[\"QS-17792ade\",\"QS-307549dc\",\"QS-ac83138b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:4:sound-binding","source_type":"word_analysis","support_id":"sup_ed193103d2b98df466c6","text":"{\"blocking_evidence\":null,\"headline\":\"sound binding\",\"reader_payoff\":\"The reader notices that the object catches and then acoustically binds to the final qualifier through matching endings.\",\"reason\":\"The hamza and accusative tanwīn are visible in the local surface, and the sound observation reinforces the syntactic object-qualifier bond.\",\"representative_source_ids\":[\"QP-acc9b7d2\",\"QP-d0a1a298\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:5:final-closure-weight","source_type":"word_analysis","support_id":"sup_ed3223fac7468f63b861","text":"{\"blocking_evidence\":null,\"headline\":\"final closure weight\",\"reader_payoff\":\"The reader notices that the ayah lands on the verdict with no following mitigation or explanation.\",\"reason\":\"The word stands at the end of the compact clause after assertion, verb, and object, so the structural closure rows are locally visible.\",\"representative_source_ids\":[\"QT-26506f72\",\"MT-7a634b39\",\"QY-552b412b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:4","source_type":"word_analysis","support_id":"sup_ee96aa76f6328c114048","text":"{\"gloss_range\":\"indefinite accusative object, a broad thing or matter made available for the final qualifier\",\"prose\":\"{{ar:شَيْئَاً}} ({{tr:shayʾan}}) is the direct object of {{ar:جِئْتُمْ}} ({{tr:jiʾtum}}), so the addressees are made responsible for a thing they have brought forward. Its indefinite singular form keeps the object open-ended long enough for {{ar:إِدًّۭا}} ({{tr:iddan}}) to define the class: not merely this utterance, but anything of this kind receives the verdict. The word is broad enough to leave the claim unnamed and concrete enough to be handled as produced content. Its pairing with the rare qualifier turns a common thing-word into the host for an exceptional condemnation, echoing 19:27 and the evaluated-thing pattern in 18:71 and 18:74 while letting 19:89 sharpen the scale. Within Surah 19, the same noun also spans the not-yet-a-thing language of 19:9 and the accusation formula of 19:27 before reaching this monstrous verdict. The hamza catches inside the object word, and the matching -an cadence binds {{ar:شَيْئَاً إِدًّۭا}} ({{tr:shayʾan iddan}}) as one heard verdict unit.\",\"root_display\":\"{{ar:ش ي ء}} ({{tr:sh-y-ʾ}})\",\"root_gloss_range\":\"general knowable or reportable thing, with other root branches such as willing, exclamation, listening, and young palms not locally activated by this noun-object frame\",\"surface_display\":\"{{ar:شَيْئَاً}} ({{tr:shayʾan}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:4:thing-to-verdict-bond","source_type":"word_analysis","support_id":"sup_ef20fde338f85866aed9","text":"{\"blocking_evidence\":null,\"headline\":\"thing-to-verdict bond\",\"reader_payoff\":\"The reader notices that the common thing-word waits for and is locked to the rare final verdict-word.\",\"reason\":\"Attachment evidence strongly licenses {{ar:إِدًّۭا}} ({{tr:iddan}}) as the adjective of {{ar:شَيْئَاً}} ({{tr:shayʾan}}), preserving the constrained-pairing and delayed-verdict rows.\",\"representative_source_ids\":[\"QG-6a79e04e\",\"QI-6f9c8ca8\",\"QY-aa3a23e9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"19:89:4:formula-and-surah-scale","source_type":"word_analysis","support_id":"sup_ff9f012a98c702599d1a","text":"{\"blocking_evidence\":null,\"headline\":\"formula and surah scale\",\"reader_payoff\":\"The reader notices that {{ar:شَيْئَاً}} ({{tr:shayʾan}}) carries a same-surah and cross-surah scale from nonexistence or accusation to monstrous verdict.\",\"reason\":\"The CRITICAL rows cite concrete references, especially 19:9, 19:27, 18:71, and 18:74, and are kept as echo and scale observations rather than local sense replacements.\",\"representative_source_ids\":[\"QI-18ed6cb8\",\"QI-1add1083\",\"QE-f4451155\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"لَّقَدْ جِئْتُمْ شَيْـًٔا إِدًّۭا","ayah_ref":"19:89"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000021/B001","root_000281/B004","root_000831/B001"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000281","role":"Bringing or presenting an object makes the second-person perfect an accomplished act of presentation.","root":"ج ي ء","source_ref":"19:89","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000831","role":"A thing that can be known and reported gives the indefinite object evidentiary contour.","root":"ش ي ء","source_ref":"19:89","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000021","role":"The mapped delivery-and-reaching image makes the qualification register an effect that has reached beyond its producers.","root":"ء د د","source_ref":"19:89","source_word_indices":["4"]}],"changed_reading":{"after":"They have brought forth a determinate, confrontable object; the utterance is treated as an accomplished production with delivered force.","before":"The speakers have merely said something terrible."},"confidence":"strong","focus_anchor":"The perfect second-person جِئْتُمْ governs the indefinite object شَيْئًا, which is then qualified by إِدًّا.","mechanism":"The clause treats the offense as an accomplished presentation: a knowable, reportable object has been brought into the shared field, and its qualification registers force that has already reached an addressee.","model_id":"baseline_presented_object"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_presented_object","source_type":"hft","support_id":"sup_f1c8cf2edea977b6945e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَّقَدْ جِئْتُمْ شَيْـًٔا إِدًّۭا","ayah_ref":"19:89"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000281/B001","root_000831/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000281","role":"Coming and occurring supplies the threshold crossed by the perfect verb.","root":"ج ي ء","source_ref":"19:89","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000831","role":"The branch linking thing and volition supplies the movement from formulation toward determinate existence.","root":"ش ي ء","source_ref":"19:89","source_word_indices":["3"]}],"changed_reading":{"after":"The possibility has arrived as an actual public event for which the plural addressees are responsible.","before":"An objectionable idea remains a speaker's internal or verbal possibility."},"confidence":"medium","focus_anchor":"جِئْتُمْ marks arrival or occurrence, while شَيْئًا can activate the relation between a thing and willing it into determination.","mechanism":"The perfect arrival converts a formulated possibility into an event: what could remain inward intention or language has crossed into occurrence as a public thing.","model_id":"baseline_arrived_possibility"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_arrived_possibility","source_type":"hft","support_id":"sup_474efbd6b059351771af","trust":"legacy_unbound"}]}
</lane_packet_json>
