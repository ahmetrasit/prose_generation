# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **93:9**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s093-regular-20260912/s093/93_9/micro.discovery.json` and modify nothing
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
  "ayah_ref": "93:9",
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
{"branch_registry":[{"boundary":"Dalın çekirdeği üstün gelme ile boyun eğdirmeyi birlikte gerektirir; salt kazanma, yönetme ya da güç sahibi olma yeterli değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001266/B001","candidate_links":[{"candidate_id":"cand_d108c9cf1c90617f75d2","lane":"micro"},{"candidate_id":"cand_2fef02847711972219db","lane":"micro"},{"candidate_id":"cand_8cd2bbf9c3611744b95a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَقْهَرْ","morph_features":"STEM|POS:V|IMPF|LEM:taqoharo|ROOT:qhr|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"93:9:4:1","qac_word_ref":"93:9:4","surface_ar":"تَقْهَرْ"}],"gloss":"üstün gelerek boyun eğdirme ve zorla alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Üstün olan taraf karşısındakini aşar ve onu boyun eğmiş, güçsüz bir duruma getirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birini ya da bir şeyi sahibinin onayı bulunmadan güç kullanarak alma anlamı bu çekirdeğe bağlıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Türemiş biçimler birini ezilmiş duruma sokmayı, onu ezecek birini başına getirmeyi veya onu yenik durumda bulmayı bildirir."}}],"root_ar":"ق ه ر","root_id":"root_001266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Üstün gelme, boyun eğdirme ve onay dışı alma çekirdeğinin birlikte kastedildiği genel açıklamalarda uygundur.","boundary_detail":"Dalın çekirdeği üstün gelme ile boyun eğdirmeyi birlikte gerektirir; salt kazanma, yönetme ya da güç sahibi olma yeterli değildir.","branch_image_ar":"غلبة من علو تقهر المقهور وتذلله","concept_gloss":"üstün gelerek boyun eğdirme ve zorla alma","contextual_glosses":[{"applicability":"Bir kişi ya da şeyin sahibinin onayı dışında güç kullanılarak alınması bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel üstün gelme ve karşıdakini boyun eğmiş duruma sokma çekirdeğini dışarıda bırakır.","preserves":"Onay dışı ve güce dayalı alma yönünü korur."},"facet_ids":["F002"],"text":"zorla almak","usage_role":"contextual"},{"applicability":"Türemiş biçimin birini zaten yenilmiş ve güçsüz durumda bulmayı bildirdiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Üstün gelme eylemini, boyun eğdirmeyi ve diğer türemiş kullanımları kapsamaz.","preserves":"Birini mevcut yenik durumuyla saptama yönünü korur."},"facet_ids":["F003"],"text":"yenik durumda bulmak","usage_role":"contextual"}],"definition":"Bir kişi ya da gücün daha üstün bir konumdan başkasına üstün gelerek onu boyun eğmiş duruma sokması veya bir şeyi sahibinin onayı olmadan zorla almasıdır. Türemiş kullanımlar birini bu duruma sokmayı, başına onu ezecek birini getirmeyi ya da onu zaten yenik durumda bulmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Üstün olan taraf karşısındakini aşar ve onu boyun eğmiş, güçsüz bir duruma getirir."},{"facet_id":"F002","role":"specialization","statement":"Birini ya da bir şeyi sahibinin onayı bulunmadan güç kullanarak alma anlamı bu çekirdeğe bağlıdır."},{"facet_id":"F003","role":"extension","statement":"Türemiş biçimler birini ezilmiş duruma sokmayı, onu ezecek birini başına getirmeyi veya onu yenik durumda bulmayı bildirir."}],"identity_rationale":"Kaynak ifadesi, daha yüksek ya da güçlü konumdan üstün gelmeyi, karşıdakini boyun eğmiş duruma sokmayı ve onayı olmadan zorla almayı aynı çekirdekte birleştirir. Ettirgen ve durum bildiren türevler de birini bu duruma sokma, başına onu ezecek birini getirme veya onu yenik durumda bulma yönlerini açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ona üstün geldi ve onu boyun eğdirdi"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"üstün gelme ve boyun eğdirme"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"üstün gelen ve boyun eğdiren"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"karşı konulamaz biçimde üstün gelen"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"başına onu ezecek birini getirdi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"onu yenik ve ezilmiş durumda buldu"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yenik ve aşağılanmış duruma düştü"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"onayı dışında zorla aldı"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"zorunlu bırakarak aldı"}],"lexicalization_note":"Tanım yalın üstün gelme ve boyun eğdirme çekirdeğini, zorla alma kalıbından ve ettirgen ya da durum bildiren türevlerden ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan üç karşılaştırma üstün gelme, ezilmişlik ve köleleştirme sınırlarını doğrudan keskinleştirir, öteki adaylar ise yalnızca ortak güç senaryosunu paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda üstünlük karşı tarafın ezilmesi, boyun eğmesi veya bir şeyin zorla alınması sonucuna bağlanır; komşu dal ise bu sonuçları gerektirmeyen daha geniş bir çekişme ve kazanma alanını kapsar.","focus_only":"Bu dal üstün gelmenin karşıdakini boyun eğmiş duruma sokmasını ve onay dışı almayı özellikle içerir.","gloss":"üstün gelme ile boyun eğdirme","neighbor_only":"Komşu dal çekişme, karşılıklı üstünlük arayışı ve üstün ya da yenik tarafı niteleyen daha geniş bir kazanma alanı taşır.","neighbor_ref":"root_001098/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir tarafın diğerine üstün gelmesi ve güç üstünlüğü kurması alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal güçlü tarafın gerçekleştirdiği üstün gelme ve boyun eğdirme olayını, komşu ise bu olayın gerçekleşme nedeninden bağımsız olarak güçsüz tarafta bulunan düşkünlük durumunu anlatır.","focus_only":"Bu dal güçlü tarafın üstün gelerek karşıdakini boyun eğdirmesini eylem açısından kurar.","gloss":"boyun eğdirme ve boyun eğmişlik","neighbor_only":"Komşu dal güçsüz tarafın aşağılanma, uysunma ve korunaksızlık durumunu sonuç ya da nitelik olarak öne çıkarır.","neighbor_ref":"root_000519/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da güç farkı altında aşağı konuma düşme ve direnç kaybı vardır."},{"boundary_match":"partial","distinction":"Odak dalın gerçekleşmesi için üstün gelme ve boyun eğdirme yeterlidir; komşu dal ise kalıcı sahiplik, kulluk ya da zorunlu hizmet gibi kurumsallaşmış ilişkileri de içine alır.","focus_only":"Bu dalın çekirdeği daha güçlü konumdan üstün gelip karşıdakini ezmek ve gerektiğinde zorla almaktır.","gloss":"boyun eğdirme ile köleleştirme","neighbor_only":"Komşu dal sahiplik, köleleştirme, istemediği işe zorlama ve bağlılık ilişkilerini ayrıca kapsar.","neighbor_ref":"root_000504/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir insanı güç kullanarak aşağı konuma indirme alanında buluşur."}],"source_phrase_ar":"تدل على غلبة وعلو (maqayis)؛ القاهر الغالب (maqayis)؛ القهر الغلبة والأخذ من فوق (ayn;tahdhib)؛ أخذهم قهرا أي من غير رضاهم (ayn)؛ أخذوا دون رضاهم على سبيل الغلبة (tahdhib)؛ الغلبة والتذليل معا (mufradat)؛ فلا تقهر أي لا تذلل (mufradat)؛ أقهره سلط عليه من يقهره (mufradat)؛ أقهرته وجدته مقهورا (sihah)؛ أقهر الرجل إذا صير في حال يذل فيها (maqayis)","source_summary":"Kaynakların ortak çekirdeği, yukarıdan ya da daha güçlü bir konumdan üstün gelme ile karşı tarafı boyun eğdirmeyi bir arada verir. Zorla alma ve türemiş biçimlerdeki ettirme ya da yenik bulma yönleri bu çekirdeğin bağımlı kullanımlarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه قهره إذا غلبه، والقاهر والقهار، والأخذ قهرا بغير رضا، والتذليل والإكراه، وأقهره إذا وجده مقهورا أو سلط عليه من يقهره.","what_is_not_ar":"لا يدخل فيه رجوع القهقرى، ولا قهر اللحم بالنار، ولا القهقر للحجر أو الطعام أو الدويبة إلا في فروعها المستقلة."},"support_links":["sup_15df0278960ea7dac528","sup_1d706927f2fd98049969","sup_c5e1860a46c73db2e482"]},{"boundary":"Anlam yalnızca etin ateş ya da pişirme etkisiyle suyunu salıp değiştiği yapıya aittir; genel ısıtma veya genel pişirme anlamına genişletilemez.","branch_kind":"collocation","branch_ref":"root_001266/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَقْهَرْ","morph_features":"STEM|POS:V|IMPF|LEM:taqoharo|ROOT:qhr|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"93:9:4:1","qac_word_ref":"93:9:4","surface_ar":"تَقْهَرْ"}],"gloss":"etin ateşte suyunu salıp değişmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ateş ya da pişirme ısısı eti etkiler ve et suyunu dışarı salar."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bazı anlatımlarda sürecin özellikle ateşin ilk etkisi olduğu, bazılarında ise etin değişmesi olduğu belirtilir."}}],"root_ar":"ق ه ر","root_id":"root_001266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Etin pişirme ateşiyle ilk kez etkilenip suyunu dışarı verdiği ve değiştiği sürecin tamamını karşılar.","boundary_detail":"Anlam yalnızca etin ateş ya da pişirme etkisiyle suyunu salıp değiştiği yapıya aittir; genel ısıtma veya genel pişirme anlamına genişletilemez.","branch_image_ar":"لحم تأخذه النار فيسيل ماؤه ويتغير","concept_gloss":"etin ateşte suyunu salıp değişmesi","contextual_glosses":[{"applicability":"Pişirme sırasında ateşin ilk etkisinin ve etten su çıkmasının anlatıldığı bir cümlede doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Etin yapısında meydana gelen daha genel değişmeyi açıkça söylemez.","preserves":"Etin ısıyla karşılaşıp suyunu dışarı salması aşamasını korur."},"facet_ids":["F001"],"text":"et suyunu salmaya başladı","usage_role":"contextual"}],"definition":"Etin pişirilmesi sırasında ateşin onu ilk kez etkilemesi, böylece suyunun akması ve yapısının değişmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ateş ya da pişirme ısısı eti etkiler ve et suyunu dışarı salar."},{"facet_id":"F002","role":"source_variant","statement":"Bazı anlatımlarda sürecin özellikle ateşin ilk etkisi olduğu, bazılarında ise etin değişmesi olduğu belirtilir."}],"identity_rationale":"Kaynak ifadesi anlamı açıkça etin pişirilmesine ve ateşin ilk etkisiyle suyunun akıp değişmesine bağlar. Bu nedenle dal bağımsız bir genel değişme anlamı değil, etle kurulan belirli bir pişirme anlatımıdır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"eti ateşte suyunu salıp değişinceye kadar pişirdi"}],"lexicalization_note":"Tanım yalnızca etle kurulan kaynak yapısına bağlıdır ve yalın biçime genel bir pişirme anlamı yüklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen iki komşu, dalı hem kızgın taşla et pişirmeden hem de ateşle genel madde dönüştürmeden ayırır, kalanlar daha uzak pişirme ya da süt işleme alanındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir araçtan çok etin ateşle ilk değişimini ve suyunun akmasını tanımlar; komşu dal ise kızgın taş kullanılan belirli pişirme yöntemlerini ve tamamlanmış oldurma sonucunu tanımlar.","focus_only":"Bu dal etin ateşin ilk etkisiyle suyunu salması ve değişmesi evresini öne çıkarır.","gloss":"etin ısıyla suyunu salması","neighbor_only":"Komşu dal kızgın taşlarla, iki taş arasında ya da kapalı sıcak yerde eti tümüyle oldurma yöntemlerini kapsar.","neighbor_ref":"root_000361/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da etin ısı uygulanarak yenebilir duruma getirilmesi sürecindedir."},{"boundary_match":"partial","distinction":"Odak dal etle sınırlı bir pişirme evresidir ve suyun salınmasını gerektirir; komşu dal madde türü ve sonuç bakımından daha geniştir, erimeyi ya da renk ve tat değişmesini de kapsar.","focus_only":"Bu dalın konusu ettir ve ayırt edici sonucu et suyunun ateş etkisiyle dışarı akmasıdır.","gloss":"ateşle değişme","neighbor_only":"Komşu dal farklı maddeleri ateşle eritme ya da işleyerek renklerini ve tatlarını değiştirme alanına uzanır.","neighbor_ref":"root_000862/B009","relation_type":"near_neighbor","shared_zone":"İki dal da ateşin bir madde üzerinde gözlenebilir değişiklik oluşturmasını içerir."}],"source_phrase_ar":"قهر اللحم طبخ حتى يسيل ماؤه (maqayis)؛ قهر اللحم إذا أخذته النار وسال ماؤه (sihah)؛ قهرنا اللحم وذلك أول ما تأخذ فيه النار فيسيل ماؤه (tahdhib)؛ ضبحته النار وضبته وقهرته إذا غيرته (tahdhib)","source_summary":"Ortak anlatım eti ateş ya da pişirme etkisine sokar ve bunun sonucunda etin suyunu salmasını verir. Bir anlatım ilk temas evresini, bir diğeri meydana gelen değişmeyi öne çıkarsa da bunlar aynı pişirme sürecinin görünümleridir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه قهر اللحم إذا طبخ أو أخذته النار حتى يسيل ماؤه ويتغير.","what_is_not_ar":"لا يدخل فيه قهر الناس بالغلبة ولا القهقرى ولا أسماء الحجر والطعام."},"support_links":[]},{"boundary":"Dal genel bir unlu süt yemeğini değil, sütün kızgın taşla kaynatıldığı ve ardından unla karıştırıldığı belirli hazırlama biçimini anlatır.","branch_kind":"bare","branch_ref":"root_001266/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَقْهَرْ","morph_features":"STEM|POS:V|IMPF|LEM:taqoharo|ROOT:qhr|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"93:9:4:1","qac_word_ref":"93:9:4","surface_ar":"تَقْهَرْ"}],"gloss":"kızgın taşla kaynatılıp un katılan süt yemeği","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Süt, içine bırakılan kızgın taşların ısısıyla kaynama noktasına getirilir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Süt kaynadıktan sonra üzerine un serpilir ve un sütle karıştırılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hazırlanan karışım yemek olarak tüketilir."}}],"root_ar":"ق ه ر","root_id":"root_001266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yemeğin ayırt edici ısıtma yöntemi ile un ekleme aşamasının birlikte belirtilmesi gereken genel adlandırmada uygundur.","boundary_detail":"Dal genel bir unlu süt yemeğini değil, sütün kızgın taşla kaynatıldığı ve ardından unla karıştırıldığı belirli hazırlama biçimini anlatır.","branch_image_ar":"قهيرة من محض تسخنه الرضف ويذر عليه الدقيق","concept_gloss":"kızgın taşla kaynatılıp un katılan süt yemeği","contextual_glosses":[{"applicability":"Yemeğin bilinmediği bir bağlamda hazırlama yolunu doğal bir açıklama olarak vermek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ayırt edici kaynatma ve karıştırma aşamalarını doğal cümle düzeninde korur."},"facet_ids":["F001","F002","F003"],"text":"kızgın taşlarla kaynatılıp unla karıştırılan süt yemeği","usage_role":"explanatory"}],"definition":"Süte kızgın taşlar atılarak kaynatılan, kaynayınca üzerine un serpilip karıştırılan ve sonra yenen bir yemektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Süt, içine bırakılan kızgın taşların ısısıyla kaynama noktasına getirilir."},{"facet_id":"F002","role":"core","statement":"Süt kaynadıktan sonra üzerine un serpilir ve un sütle karıştırılır."},{"facet_id":"F003","role":"associated_use","statement":"Hazırlanan karışım yemek olarak tüketilir."}],"identity_rationale":"Kaynak ifadesi yemeği ve hazırlanış sırasını ayrıntılı biçimde verir: süt içine kızgın taşlar bırakılır, kaynayınca üzerine un serpilir, karıştırılır ve yenir. Geçici dal çerçevesi bu bileşenleri doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kızgın taşla kaynatılıp un katılan süt yemeği"}],"lexicalization_note":"Yalın ad, kaynakta verilen belirli yemeği ve onun kurucu hazırlama aşamalarını birlikte karşılar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; iki yemek komşusu süt, un ve pişirme ortaklığını paylaşırken kızgın taşla kaynatma sırasını taşımadıkları için en yararlı sınırları sağlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ayırt edici yanı sütün doğrudan ocak yerine kızgın taşlarla kaynatılması ve unun kaynamadan sonra eklenmesidir; komşu dalda kurucu ilişki unun sütle pişirilmesidir.","focus_only":"Bu yemekte süt önce içine atılan kızgın taşlarla kaynatılır, un daha sonra serpilip karıştırılır.","gloss":"sütle pişirilen un yemeği","neighbor_only":"Komşu yemek unu sütle pişirmeye dayanır ve kızgın taşla ısıtma aşamasını gerektirmez.","neighbor_ref":"root_000306/B012","relation_type":"near_neighbor","shared_zone":"Her iki dal da süt ve unun pişirilerek bir yemek oluşturmasını içerir."},{"boundary_match":"partial","distinction":"Odak dalın kimliği kızgın taş, kaynama ve sonradan un ekleme sırasına bağlıdır; komşu dal bu yöntemi gerektirmeyen, yağlı ya da unlu süt karışımlarını daha geniş biçimde adlandırır.","focus_only":"Bu dal belirli aşamalarla hazırlanan tek bir süt yemeğini ve kızgın taşla kaynatmayı anlatır.","gloss":"unlu süt karışımı","neighbor_only":"Komşu dal süt, yağ ve unun karışmasıyla oluşan daha geniş yiyecek ve karışım alanını kapsar.","neighbor_ref":"root_000576/B003","relation_type":"near_neighbor","shared_zone":"İki dal süt ile unun pişmiş ya da koyu bir yiyecekte birleşmesi bakımından örtüşür."}],"source_phrase_ar":"القهيرة محض يلقى فيه الرضف فإذا غلى ذر عليه الدقيق وسيط به ثم أكل (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, sütü kızgın taşla kaynatma, üzerine un serpme, karıştırma ve yeme aşamalarını eksiksiz sıralar."}],"source_summary":"Bu dal için kaynaklar arası bir ortaklık kurulamaz; eldeki ayrıntılı yemek açıklaması tek bir tanıklığa dayanır.","sources":["TA"],"what_is_ar":"يدخل فيه القهيرة: محض تلقى فيه الرضف فإذا غلى ذر عليه الدقيق وسيط به ثم أكل.","what_is_not_ar":"لا يدخل فيه قهر اللحم ولا القهقر الطعام الكثير المنضود."},"support_links":[]},{"boundary":"Dal hem taşın sert ya da pürüzsüz niteliğini hem de ezme aracı olabilmesini kapsar; geri gitme ve kapta yiyecek anlamları bu daldan ayrıdır.","branch_kind":"bare","branch_ref":"root_001266/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَقْهَرْ","morph_features":"STEM|POS:V|IMPF|LEM:taqoharo|ROOT:qhr|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"93:9:4:1","qac_word_ref":"93:9:4","surface_ar":"تَقْهَرْ"}],"gloss":"sert ya da pürüzsüz öğütme taşı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne, sertliği veya pürüzsüz yüzeyiyle tanımlanan bir taştır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Taş, bir şeyi ezmek ya da öğütmek için araç olarak kullanılabilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı kaynak kümesindeki ayrı bir biçim, bu taştan daha büyük olan taşı belirtir."}}],"root_ar":"ق ه ر","root_id":"root_001266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Taşın fiziksel niteliği ile bir şeyi ezme ya da öğütme aracı olmasının birlikte kastedildiği yerde uygundur.","boundary_detail":"Dal hem taşın sert ya da pürüzsüz niteliğini hem de ezme aracı olabilmesini kapsar; geri gitme ve kapta yiyecek anlamları bu daldan ayrıdır.","branch_image_ar":"حجر قهقر صلب أو أملس يسحق به","concept_gloss":"sert ya da pürüzsüz öğütme taşı","contextual_glosses":[{"applicability":"Taşın bir şeyi ezmek ya da öğütmek için kullanılan araç yönünün bağlamdan açık olduğu cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Taşın sert ya da pürüzsüz olabileceğini ve ayrı büyük türü açıkça belirtmez.","preserves":"Taşın ezme ve öğütme aracı olarak kullanılmasını korur."},"facet_ids":["F002"],"text":"öğütme taşı","usage_role":"contextual"}],"definition":"Sert ya da pürüzsüz olabilen bir taş ve özellikle bir şeyi ezmek ya da öğütmek için kullanılan taş araçtır. Kaynakta ayrı bir biçim, bunun daha büyük türü olarak gösterilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne, sertliği veya pürüzsüz yüzeyiyle tanımlanan bir taştır."},{"facet_id":"F002","role":"associated_use","statement":"Taş, bir şeyi ezmek ya da öğütmek için araç olarak kullanılabilir."},{"facet_id":"F003","role":"source_variant","statement":"Aynı kaynak kümesindeki ayrı bir biçim, bu taştan daha büyük olan taşı belirtir."}],"identity_rationale":"Kaynak ifadesi nesneyi taş olarak tanımlar, sertlik ya da pürüzsüzlük niteliklerini verir ve bir şeyi ezmede kullanılan biçimini ayrıca belirtir. Aynı tanıklıkta farklı bir biçimin bu taştan daha büyük olduğu da açıkça söylenir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"sert ya da pürüzsüz taş"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bir şeyi ezmekte kullanılan taşlar"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"aynı kümedeki daha büyük taş"}],"lexicalization_note":"Yalın dal sert ya da pürüzsüz taşı ve bu taşın ezme aracı kullanımını kapsar; başka dallardaki benzer sesli biçimlerin anlamları içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler taşı doğal yüzey, üzerinde dövme yapılan taş ve kap biçimli dövme aracıyla karşılaştırır, diğer adaylar nitelik ya da işlev bakımından daha uzaktır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal taşın sertlik veya pürüzsüzlüğünü ve daha genel ezme kullanımını korur; komşu dal ise üzerinde dövme yapılan geniş taş biçimini ve belirli dövülen maddeleri öne çıkarır.","focus_only":"Bu dal sert ya da pürüzsüz taşı genel nesne olarak ve ezme aracına dönüşebilen biçimiyle kapsar.","gloss":"üzerinde dövme yapılan taş","neighbor_only":"Komşu dal özellikle üzerine güzel kokulu madde ya da kurutulmuş yem konup dövülen geniş taşı anlatır.","neighbor_ref":"root_000880/B009","relation_type":"near_synonym","shared_zone":"Her iki dal da maddeleri ezmek ya da dövmek için kullanılan genişçe taş aracını kapsayabilir."},{"boundary_match":"partial","distinction":"Odak dal araçsal ezme kullanımına açıktır ve temiz yüzey koşulu koymaz; komşu dal doğal taşın genişliği ve toprak ya da çamurdan arınmışlığı üzerinde durur.","focus_only":"Bu dalda taşın bir şeyi ezmekte araç olarak kullanılabilmesi kurucu bir ayırt edicidir.","gloss":"sert ve pürüzsüz taş","neighbor_only":"Komşu dal taşın geniş, sert, pürüzsüz ve toprakla çamurdan arınmış doğal yüzeyini, ayrıca belirli bir yer adını kapsar.","neighbor_ref":"root_000873/B006","relation_type":"near_neighbor","shared_zone":"İki dal da sert ve pürüzsüz olabilen taş ya da kaya nesnesinde örtüşür."},{"boundary_match":"field_only","distinction":"Odak nesne taşın kendisi ve onun yüzeyidir; komşu nesne ise içine malzeme konan ya da onunla vurulan kap biçimli dövme aracıdır, dolayısıyla nesne yapıları birbirinin yerine geçmez.","focus_only":"Bu dal ezmede kullanılan nesneyi sert ya da pürüzsüz bir taş olarak tanımlar.","gloss":"ezme ve dövme aracı","neighbor_only":"Komşu dal dövmenin içinde ya da onunla yapıldığı kap biçimli aracı tanımlar ve aracın işlev yönü tartışmalıdır.","neighbor_ref":"root_001608/B004","relation_type":"same_field","shared_zone":"Her iki dal da sert maddeleri ezme veya dövme işinde kullanılan araçlar alanındadır."}],"source_phrase_ar":"القهقر الحجر الصلب (maqayis)؛ القهقر الحجر (ayn)؛ القهقرى بتشديد الراء الحجر الصلب (sihah)؛ القهقر الحجر الأملس (tahdhib)؛ القهقر والقهاقر وهو ما سهكت به الشيء والقهر أعظم منه (tahdhib)","source_summary":"Ortak tanım taş olma özelliğini korurken niteleme sertlik ile pürüzsüzlük arasında değişir. Ezme aracı kullanımı ve ayrı biçimle belirtilen daha büyük taş, temel nesne tanımını ayrıntılandırır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه القهقر أو القهاقر للحجر الصلب أو الأملس، وما يسحق به الشيء، ومعه قول تهذيب اللغة إن القهر أعظم منه.","what_is_not_ar":"لا يدخل فيه القهقرى بمعنى الرجوع إلى الخلف، ولا القهقر الطعام الكثير، ولا القهيقران الدويبة."},"support_links":[]},{"boundary":"Çekirdek hareket geriye doğrudur; genel geri dönme, yineleme veya azalmanın tümü bu dala alınamaz, önceki tutumdan dönme ise bağımlı bir genişlemedir.","branch_kind":"mixed_non_bare","branch_ref":"root_001266/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَقْهَرْ","morph_features":"STEM|POS:V|IMPF|LEM:taqoharo|ROOT:qhr|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"93:9:4:1","qac_word_ref":"93:9:4","surface_ar":"تَقْهَرْ"}],"gloss":"topukları üzerinde geriye çekilme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi geriye doğru gider veya topukları üzerinde geri çekilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Fiziksel geriye gidiş, önceki durumdan ya da benimsenmiş tutumdan dönmeyi anlatacak biçimde genişleyebilir."}}],"root_ar":"ق ه ر","root_id":"root_001266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel hareketin geriye doğru ve topuklar üzerinde gerçekleştiği çekirdek kullanımın en kısa tam karşılığıdır.","boundary_detail":"Çekirdek hareket geriye doğrudur; genel geri dönme, yineleme veya azalmanın tümü bu dala alınamaz, önceki tutumdan dönme ise bağımlı bir genişlemedir.","branch_image_ar":"رجوع القهقرى إلى خلف","concept_gloss":"topukları üzerinde geriye çekilme","contextual_glosses":[{"applicability":"Bir kişinin daha önce benimsediği tutum ya da durumdan vazgeçip geri dönmesinin açıkça kastedildiği yerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Topuklar üzerinde gerçekleşen fiziksel geriye gidiş çekirdeğini kapsamaz.","preserves":"Önceden benimsenmiş durumdan geri dönüş yönünü korur."},"facet_ids":["F002"],"text":"eski tutumundan geri dönmek","usage_role":"contextual"}],"definition":"Yüzün yönünü koruyarak topuklar üzerinde geriye doğru gitme ya da geri çekilmedir. Açık bir düşünsel bağlamda, daha önce benimsenen durum veya tutumdan geri dönmeyi de anlatabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi geriye doğru gider veya topukları üzerinde geri çekilir."},{"facet_id":"F002","role":"extension","statement":"Fiziksel geriye gidiş, önceki durumdan ya da benimsenmiş tutumdan dönmeyi anlatacak biçimde genişleyebilir."}],"identity_rationale":"Kaynak ifadesi fiziksel çekirdeği geriye doğru gitme, özellikle topukları üzerinde geri çekilme olarak açıkça kurar. Önceki durumdan ya da tutumdan dönme anlamı da yalnızca açıkça belirtilen mecazlı genişleme olarak desteklenir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"geriye doğru gitme; topukları üzerinde geri çekilme"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"topukları üzerinde geriye gitti"}],"lexicalization_note":"Tanım yalın geriye gidiş adını ve eylem biçimini ayırır; önceki durumdan dönme yönünü fiziksel çekirdeğe bağlı bir genişleme olarak tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan üç karşılaştırma yönlü geri çekilme, genel geri dönüş ve ilk duruma dönüş ayrımlarını gösterir, kalan adaylar yalnızca uzak hareket ya da değişim alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hareketin geriye doğru ve topuklar üzerinde oluşunu belirtir; komşu dal ise bu beden biçimini gerektirmeden dönmeyi, vazgeçmeyi veya ilerlemeden sonra çekilmeyi kapsar.","focus_only":"Bu dal geriye doğru hareketi ve özellikle topuklar üzerinde geri çekilmeyi biçimsel olarak sınırlar.","gloss":"geriye çekilme","neighbor_only":"Komşu dal ilerlemeden sonra dönme, çekilme, yön değiştirme ve kimi bağlamlarda dönüp bakmama gibi daha geniş davranışları kapsar.","neighbor_ref":"root_001033/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da ilerleme yönünün tersine hareket etme ve geri çekilme alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal yönlü bir geri hareketten doğar ve düşünsel genişlemesini buna bağlar; komşu dal fiziksel geriye yürümeyi gerektirmeyen eksilme, yineleme ve durum değişikliklerine uzanır.","focus_only":"Bu dalın fiziksel çekirdeği belirli yönlü geriye yürüme ya da çekilmedir.","gloss":"geri dönme ve eksilme","neighbor_only":"Komşu dal geri dönmenin yanında eksilme, kararsızlık ve bir durumdan başka bir duruma geçişi de kapsar.","neighbor_ref":"root_000369/B005","relation_type":"near_neighbor","shared_zone":"İki dal bir önceki yönden veya durumdan geri dönme düşüncesini paylaşır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği bedensel olarak geriye gitmektir; komşu dalın çekirdeği ise belirli bir ilk duruma ya da başlangıç noktasına yeniden varmaktır ve geriye yürüme biçimini gerektirmez.","focus_only":"Bu dal hareket biçimini topuklar üzerinde geriye gitme olarak belirler ve eski tutumdan dönüşe genişleyebilir.","gloss":"önceki duruma geri dönme","neighbor_only":"Komşu dal başlangıçtaki işe, yaratılışa, gelinen yola ya da yaşlılık durumuna yeniden dönmeyi belirtir.","neighbor_ref":"root_000341/B003","relation_type":"near_neighbor","shared_zone":"Her ikisi de önceki yön veya durumla yeniden ilişki kuran bir geri dönüş içerir."}],"source_phrase_ar":"رجع القهقرى إذا رجع إلى خلفه (maqayis)؛ القهقرى الرجوع إلى خلف (sihah)؛ القهقرى التراجع إلى الخلف (tahdhib)؛ رجع فلان القهقرى إذا رجع على عقبه (tahdhib)؛ القهقرى المشي إلى خلف (mufradat)؛ معناه الارتداد عما كانوا عليه (tahdhib)","source_summary":"Kaynakların ortak çekirdeği geriye doğru hareket etmek ve topuklar üzerinde geri çekilmektir. Önceki durumdan dönme yorumu, bu yönlü hareketten gelişen ve bağlamda açık edilmesi gereken düşünsel bir genişlemedir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه رجع القهقرى، والتراجع أو المشي إلى الخلف على العقب، واستعماله في معنى الارتداد عما كان عليه إذا صرح به المصدر.","what_is_not_ar":"لا يدخل فيه القهر بمعنى الغلبة والتذليل، ولا القهقر الحجر أو الطعام."},"support_links":[]},{"boundary":"Salt bol yiyecek veya salt dolu kap yeterli değildir; yiyeceğin çok ve bir kap içinde düzenlenmiş ya da istiflenmiş olması birlikte aranır.","branch_kind":"bare","branch_ref":"root_001266/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَقْهَرْ","morph_features":"STEM|POS:V|IMPF|LEM:taqoharo|ROOT:qhr|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"93:9:4:1","qac_word_ref":"93:9:4","surface_ar":"تَقْهَرْ"}],"gloss":"kapta istiflenmiş bol yiyecek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Söz konusu yiyecek tek bir parça değil, çok miktarda bulunan bir erzak bütünüdür."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yiyecek kapların ya da bir erzak torbasının içinde düzenli biçimde yerleştirilmiş veya istiflenmiştir."}}],"root_ar":"ق ه ر","root_id":"root_001266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yiyeceğin hem çokluğunu hem de bir kap içinde düzenlenmiş olmasını birlikte belirten en kısa doğal karşılıktır.","boundary_detail":"Salt bol yiyecek veya salt dolu kap yeterli değildir; yiyeceğin çok ve bir kap içinde düzenlenmiş ya da istiflenmiş olması birlikte aranır.","branch_image_ar":"قهقر طعام كثير منضود في وعاء","concept_gloss":"kapta istiflenmiş bol yiyecek","contextual_glosses":[{"applicability":"Birden çok kapta saklanan veya taşınan çok miktardaki yiyeceğin anlatıldığı cümlede doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yiyecek bolluğunu ve kaplar içinde düzenlenmiş olma koşulunu birlikte korur."},"facet_ids":["F001","F002"],"text":"kaplara düzenlenmiş bol erzak","usage_role":"contextual"}],"definition":"Kaplarda ya da bir erzak torbasında düzenli biçimde yerleştirilmiş, istiflenmiş çok miktarda yiyecektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Söz konusu yiyecek tek bir parça değil, çok miktarda bulunan bir erzak bütünüdür."},{"facet_id":"F002","role":"core","statement":"Yiyecek kapların ya da bir erzak torbasının içinde düzenli biçimde yerleştirilmiş veya istiflenmiştir."}],"identity_rationale":"Kaynak ifadesi hem yiyeceğin çokluğunu hem de kaplarda ya da erzak torbasında düzenli biçimde yerleştirilmiş olmasını belirtir. Dal çerçevesi bu iki kurucu özelliği korur ve taş anlamından açıkça ayrılır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kapta istiflenmiş bol yiyecek"}],"lexicalization_note":"Yalın ad, kapta düzenlenmiş bol yiyecek bütününü karşılar ve benzer biçimli taş ya da geriye gidiş anlamlarını içermez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen üç komşu yiyecek bolluğu, erzağı kaba doldurma ve dolu kabın kendisi arasındaki göndergesel sınırları en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bolluğu kap içindeki düzenli yerleşimle birlikte tanımlar; komşu dal ise yiyecek bolluğunu sunum ya da miktar bakımından verir ve kap koşulu koymaz.","focus_only":"Bu dal yiyeceğin kap ya da torba içinde düzenlenmiş ve istiflenmiş olmasını zorunlu kılar.","gloss":"bol yiyecek","neighbor_only":"Komşu dal çok ve bol sunulan yiyeceği anlatır, fakat belirli bir kapta düzenlenmiş olmasını gerektirmez.","neighbor_ref":"root_000098/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da çok miktarda bulunan yiyecek veya erzak düşüncesini taşır."},{"boundary_match":"partial","distinction":"Odak dal kapta duran bol yiyeceğin adı ve durumudur; komşu dal ise belirli ürünleri gelecekte kullanmak üzere kaplara doldurma işlemini ve zamanını öne çıkarır.","focus_only":"Bu dalın gösterdiği şey, kap içinde düzenlenmiş çok miktardaki yiyecek bütünüdür.","gloss":"kapta saklanan erzak","neighbor_only":"Komşu dal hurma ve tahılı kış için kaplara doldurup saklama eylemini ve bu saklama dönemini anlatır.","neighbor_ref":"root_001322/B002","relation_type":"near_neighbor","shared_zone":"İki dal da yiyeceğin kaplara yerleştirilmesi ve toplu biçimde korunması alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal içeriği, yani bol yiyeceği adlandırır; komşu dal ise içeriğin türünden bağımsız olarak kabın kendisini ve doluluk durumunu adlandırır.","focus_only":"Bu dalın göndergesi kap değil, kabın içindeki çok ve düzenlenmiş yiyecektir.","gloss":"dolu kaplar","neighbor_only":"Komşu dal dolu ya da taşacak ölçüde dolgun kapları, havuzları ve geniş çanakları adlandırır.","neighbor_ref":"root_000639/B004","relation_type":"near_neighbor","shared_zone":"Her iki dalda da kap ve onun dolu görünümü birlikte yer alabilir."}],"source_phrase_ar":"القهقر بالتخفيف الطعام الكثير الذي في الأوعية منضودا (tahdhib)؛ القهقر الطعام الكثير الذي في العيبة (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, çok miktardaki yiyeceği kaplarda düzenlenmiş ya da bir erzak torbasına yerleştirilmiş olarak tanımlar."}],"source_summary":"Bu dal için kaynaklar arası bir ortaklık kurulamaz; bol yiyeceğin kap içinde düzenlenmiş olması tek bir tanıklıkla aktarılır.","sources":["TA"],"what_is_ar":"يدخل فيه القهقر بمعنى الطعام الكثير في الأوعية أو في العيبة منضودا.","what_is_not_ar":"لا يدخل فيه القهقر الحجر ولا القهقرى الرجوع إلى الخلف."},"support_links":[]},{"boundary":"Dal türü bilinmeyen küçük bir hayvan adıyla sınırlıdır; böcek, kuş, sürüngen ya da başka belirli bir tür olduğu söylenemez.","branch_kind":"bare","branch_ref":"root_001266/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَقْهَرْ","morph_features":"STEM|POS:V|IMPF|LEM:taqoharo|ROOT:qhr|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"93:9:4:1","qac_word_ref":"93:9:4","surface_ar":"تَقْهَرْ"}],"gloss":"türü belirtilmeyen küçük hayvan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderge küçük boyutlu bir hayvandır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvanın türü, görünüşü veya davranışı hakkında ek bir bilgi verilmez."}}],"root_ar":"ق ه ر","root_id":"root_001266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kanıtın izin verdiği ölçüde hayvan oluşu ve küçüklüğü belirtilirken tür kimliği açık bırakılmalıdır.","boundary_detail":"Dal türü bilinmeyen küçük bir hayvan adıyla sınırlıdır; böcek, kuş, sürüngen ya da başka belirli bir tür olduğu söylenemez.","branch_image_ar":"قهيقران دويبة","concept_gloss":"türü belirtilmeyen küçük hayvan","contextual_glosses":[{"applicability":"Tür bilgisinin gerekmediği ve yalnızca kaynak açıklamasının doğal cümle içinde aktarılacağı yerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tür kimliğinin kaynakta açıklanmadığına ilişkin sınırı açıkça söylemez.","preserves":"Göndergenin küçük bir hayvan olduğu bilgisini korur."},"facet_ids":["F001"],"text":"küçük bir hayvan","usage_role":"contextual"}],"definition":"Kaynakta yalnızca küçük bir hayvan olarak açıklanan, hangi türe ait olduğu belirtilmeyen bir canlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderge küçük boyutlu bir hayvandır."},{"facet_id":"F002","role":"source_variant","statement":"Hayvanın türü, görünüşü veya davranışı hakkında ek bir bilgi verilmez."}],"identity_rationale":"Kaynak ifadesi sözcüğü yalnızca küçük bir hayvan olarak açıklar; geçici dal çerçevesi bundan daha dar bir tür kimliği ileri sürmez. Bu nedenle dal korunabilir, ancak hayvanın hangi türe ait olduğu kanıttan belirlenemez.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"türü belirtilmeyen küçük bir hayvan"}],"lexicalization_note":"Yalın ad yalnızca türü belirtilmemiş küçük hayvanı gösterir; kanıt bulunmadan belirli bir hayvan sınıfına daraltılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; türü bilinmeyen göndergenin küçük karınca ya da sinek gibi belirli hayvan adlarıyla özdeşleştirilemeyeceğini gösteren iki alan karşılaştırması yeterlidir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dalın hayvanı tür bakımından belirsizdir; komşu dal ise göndergesini açıkça küçük karınca olarak sınırlar, bu yüzden yalnız küçüklük ortaklığı özdeşlik kurmaz.","focus_only":"Bu dal küçük bir hayvanı adlandırır, ancak onun hangi türden olduğunu belirtmez.","gloss":"küçük hayvan ve küçük karınca","neighbor_only":"Komşu dal belirli bir dil çevresinde küçük karıncaya verilen adı açıkça tanımlar.","neighbor_ref":"root_001557/B009","relation_type":"same_field","shared_zone":"Her iki dal da küçük boyutlu bir hayvana verilen söz varlığı adları alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal yalnızca küçük hayvan düzeyinde kalır; komşu dal sinek türüne kadar belirlenmiştir, dolayısıyla odak göndergenin böcek sayılması kanıtsız bir daraltma olur.","focus_only":"Bu dalın hayvan türü bilinmez ve onun böcek olduğuna dair kanıt yoktur.","gloss":"küçük hayvan ve sinek türü","neighbor_only":"Komşu dal belirli bir sinek türünü açıkça adlandırır.","neighbor_ref":"root_000338/B005","relation_type":"same_field","shared_zone":"İki dal da küçük hayvanlara ilişkin özel söz varlığı alanında karşılaştırılabilir."}],"source_phrase_ar":"القهيقران دويبة (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık sözcüğü küçük bir hayvan adı olarak verir, fakat hayvanın türünü veya ayırt edici özelliklerini açıklamaz."}],"source_summary":"Bu dal için kaynaklar arası bir ortaklık kurulamaz; küçük hayvan tanımı tek ve ayrıntı vermeyen bir tanıklığa dayanır.","sources":["TA"],"what_is_ar":"يدخل فيه القهيقران اسم دويبة كما في تهذيب اللغة.","what_is_not_ar":"لا يدخل فيه القهقر للحجر أو الطعام ولا القهقرى للرجوع."},"support_links":[]},{"boundary":"İnsan çocuğu için baba kaybı ve ergenlik sınırı, hayvan yavrusu için anne kaybı esastır; genel yalnızlık bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001692/B001","candidate_links":[{"candidate_id":"cand_d108c9cf1c90617f75d2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:9:2:2","qac_word_ref":"93:9:2","surface_ar":"يَتِيمَ"}],"gloss":"babasını yitirmiş çocuk veya annesini yitirmiş hayvan yavrusu olma","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanlarda durum, bir çocuğun ergenliğe ulaşmadan babasını yitirmesiyle oluşur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsan dışındaki hayvanlarda karşılık gelen durum, yavrunun annesini yitirmesidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Türemiş eylemler, bir çocuğu babasız bırakmayı veya çocukları topluca bu duruma düşürmeyi anlatır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bazı türemiş kadın adları, çocukları babasız kalmış olan anneyi niteler."}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan ve hayvan için farklı ebeveyn koşullarını birlikte belirtmek gereken genel açıklamada kullanılır.","boundary_detail":"İnsan çocuğu için baba kaybı ve ergenlik sınırı, hayvan yavrusu için anne kaybı esastır; genel yalnızlık bu dala girmez.","branch_image_ar":"انقطاع الولد عن كافله","concept_gloss":"babasını yitirmiş çocuk veya annesini yitirmiş hayvan yavrusu olma","contextual_glosses":[{"applicability":"Ergenliğe ulaşmadan babası ölen bir insan çocuğundan söz edilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan çocuğunu ve belirleyici baba kaybını açık biçimde korur."},"facet_ids":["F001"],"text":"babasını yitirmiş çocuk","usage_role":"contextual"},{"applicability":"İnsan dışındaki bir hayvanın annesini yitirmiş yavrusundan söz edilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvan yavrusunu ve belirleyici anne kaybını açık biçimde korur."},"facet_ids":["F002"],"text":"annesini yitirmiş hayvan yavrusu","usage_role":"contextual"}],"definition":"İnsanlarda ergenliğe ulaşmadan babasını yitirmiş çocuk olma, öteki hayvanlarda ise annesini yitirmiş yavru olma durumudur. Bir çocuğu bu duruma düşürme ve çocukları babasız kalan kadını niteleme gibi türev kullanımlar bu çekirdeğe bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanlarda durum, bir çocuğun ergenliğe ulaşmadan babasını yitirmesiyle oluşur."},{"facet_id":"F002","role":"specialization","statement":"İnsan dışındaki hayvanlarda karşılık gelen durum, yavrunun annesini yitirmesidir."},{"facet_id":"F003","role":"extension","statement":"Türemiş eylemler, bir çocuğu babasız bırakmayı veya çocukları topluca bu duruma düşürmeyi anlatır."},{"facet_id":"F004","role":"associated_use","statement":"Bazı türemiş kadın adları, çocukları babasız kalmış olan anneyi niteler."}],"identity_rationale":"Kaynak ifadesi genel olarak bakımı üstlenen kişiden ayrılmayı değil, insan çocuğunda ergenlikten önce babanın, öteki hayvanlarda ise annenin ölümünü belirleyici sayar. Bu nedenle dal, bu iki katılımcı ayrımı açıkça korunarak tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"insanda babasız, hayvanda annesiz kalma"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"babasını yitirmiş çocuk veya annesini yitirmiş hayvan yavrusu"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"çocuk babasını yitirip babasız kaldı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"Tanrı onu babasız bıraktı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"çocukları babasız bıraktı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"babasını yitirmiş çocuklar"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"babasını yitirmiş çocuklar"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"çocukları babasız kalmış kadın"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"çocukları babasız kalmış kadın"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"onları babasız bıraktı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"çocukken kendisini yetiştiren kişiye nispetle, büyüdüğünde de babasını yitirmiş çocuk diye anılan kişi"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"babasını yitirmiş çocuklar topluluğu"}],"lexicalization_note":"Tanım, yalın durum ve kişi adlandırmalarını temel alır; çocukları babasız kalan kadın ile büyüdükten sonra da sürdürülen adlandırma yalnız kendi kalıpları içinde tutulur.","neighbor_coverage_note":"Sunulan bütün komşu adaylar değerlendirildi; ebeveyn ölümü, bırakılma, bakım bağı ve tek kalma arasındaki sınırı en açık gösteren üç karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ölümden doğan ve türe göre baba ya da anne üzerinden tanımlanan statüdür; komşu dal ise ölüm gerektirmeyen bırakılma ve bulunma olayını anlatır.","focus_only":"Odak dalda ebeveynin ölümü, insan ve hayvan için ayrı ebeveyn rolleriyle belirleyicidir.","gloss":"ebeveynini yitirmiş yavru ile bırakılmış çocuk","neighbor_only":"Komşu dalda çocuk annesi tarafından bırakılır ve başka biri tarafından bulunur.","neighbor_ref":"root_001466/B007","relation_type":"near_neighbor","shared_zone":"Her ikisi de bir çocuğun veya yavrunun doğal ebeveyn bakımından yoksun kalabildiği durumları anlatır."},{"boundary_match":"field_only","distinction":"Bakıma muhtaçlık odak dalın tanımı değildir ve her bakmakla yükümlü olunan kişi ebeveynini yitirmiş değildir.","focus_only":"Odak dal, insan çocuğunda baba ve hayvan yavrusunda anne ölümüyle sınırlı bir durumdur.","gloss":"ebeveyn kaybı ile bakıma muhtaç olma","neighbor_only":"Komşu dal bakmakla yükümlü olunanları, yük sayılan kişileri ve çocuğu olmayanları da kapsar.","neighbor_ref":"root_001315/B002","relation_type":"same_field","shared_zone":"İki dal da başkasının bakımına veya desteğine ihtiyaç duyan kişilerin alanına değebilir."},{"boundary_match":"partial","distinction":"Odak dalın koşulları ebeveyn türü ve insanlarda ergenlik sınırıyla belirlenir; komşu dal bu koşulları taşımaz ve nadir nesnelere de uygulanır.","focus_only":"Odak dal canlılarda belirli bir ebeveynin ölümüne bağlı statüyü bildirir.","gloss":"ebeveyn kaybı ile tek kalma","neighbor_only":"Komşu dal canlı ya da cansız herhangi bir şeyin tek kalmasını veya benzerinin zor bulunmasını bildirir.","neighbor_ref":"root_001692/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da önceki bir bağdan veya eşlikten yoksun kalma düşüncesi bulunabilir."}],"source_phrase_ar":"اليتم في الناس من قبل الأب وفي سائر الحيوان من جهة الأم (maqayis)؛ يتم الصبي إذا صار يتيما وأيتمه الله (jamhara)؛ أيتمت المرأة فهي موتم (jamhara;sihah)؛ يتمهم الله تيتيما (sihah)؛ اليتيم الذي مات أبوه حتى يبلغ (tahdhib)؛ انقطاع الصبي عن أبيه قبل بلوغه وفي سائر الحيوانات من قبل أمه (mufradat)","source_summary":"Kanıt bütünü, insan çocuğunda baba kaybını, hayvan yavrusunda anne kaybını ve bu durumla ilgili türemiş biçimleri verir. Ergenlik sınırı bazı aktarımlarda açıkça belirtilir; ettirgen ve topluluk bildiren biçimler ayrı tanıklamalar olarak bu çekirdeğe bağlanır.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الصبي الذي مات أبوه قبل بلوغه، والبهيمة التي ماتت أمها، وجعل الأولاد أيتاما","what_is_not_ar":"ليس مجرد الانفراد في الأشياء النفيسة ولا الإبطاء في السير ولا الغفلة والتقصير"},"support_links":["sup_c5e1860a46c73db2e482"]},{"boundary":"Dal, ebeveyn kaybını değil tekliği veya benzer azlığını anlatır; değerli nesne ve şiir örnekleri çekirdeğin kendisi değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001692/B002","candidate_links":[{"candidate_id":"cand_2fef02847711972219db","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:9:2:2","qac_word_ref":"93:9:2","surface_ar":"يَتِيمَ"}],"gloss":"tek kalmış ya da benzeri zor bulunan şey","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Canlı ya da cansız bir varlık, başka bir eşlikçi olmadan tek başına bulunduğunda bu nitelemeyi alabilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Niteleme, benzeri veya dengi zor bulunan seçkin bir varlığa da uygulanabilir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tek başına duran şiir dizesi, eşi zor bulunan inci ve ayrı kumluk kaynaklarda örneklenir."}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tek başına bulunma ile eşine az rastlanma kapsamlarının ikisini de taşıyan genel niteleme için kullanılır.","boundary_detail":"Dal, ebeveyn kaybını değil tekliği veya benzer azlığını anlatır; değerli nesne ve şiir örnekleri çekirdeğin kendisi değildir.","branch_image_ar":"انفراد الشيء وانقطاع نظيره","concept_gloss":"tek kalmış ya da benzeri zor bulunan şey","contextual_glosses":[{"applicability":"Varlığın eşlikçisiz veya çevresindekilerden ayrı bulunmasının öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Varlığın başka bir eşlikçi olmadan tek kalması özelliğini korur."},"facet_ids":["F001"],"text":"tek başına kalmış","usage_role":"contextual"},{"applicability":"Bir nesnenin veya söz ürününün benzerinin az bulunması vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Benzer azlığını ve bundan doğan eşsizlik niteliğini korur."},"facet_ids":["F002"],"text":"eşi zor bulunan","usage_role":"contextual"}],"definition":"Bir varlığın tek başına kalması veya benzerinin zor bulunmasıdır; şiir dizesi, inci ve tek başına duran kumluk bu niteliğin özel örnekleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Canlı ya da cansız bir varlık, başka bir eşlikçi olmadan tek başına bulunduğunda bu nitelemeyi alabilir."},{"facet_id":"F002","role":"extension","statement":"Niteleme, benzeri veya dengi zor bulunan seçkin bir varlığa da uygulanabilir."},{"facet_id":"F003","role":"example","statement":"Tek başına duran şiir dizesi, eşi zor bulunan inci ve ayrı kumluk kaynaklarda örneklenir."}],"identity_rationale":"Kaynak ifadesi, tek başına kalan şeyi ve benzeri zor bulunan şeyi aynı dalda açıkça toplar; şiir dizesi, inci ve tek kumluk bu çekirdeğin örnekleridir. Geçici çerçeve bu kapsamı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"tek başına veya eşi zor bulunan"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"tek başına duran veya benzeri olmayan şiir dizesi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"tek ve eşi zor bulunan inci"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"tek başına duran kumluk veya dişil varlık"}],"lexicalization_note":"Yalın niteleme tekliği veya benzer azlığını bildirir; şiir dizesi ve inci okumaları yalnız tanıklanmış ad öbeklerinin özel uygulamalarıdır.","neighbor_coverage_note":"Bütün adaylar incelendi; genel teklik, nadirlik, belirli bir nitelikte rakipsizlik ve ebeveyn kaybı ile en güçlü sınırları kuran dört aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal tek kalmayı benzer azlığına kadar genişletirken komşu dal sayısal birlik ve tekleştirme işlemlerine de uzanır; bu yüzden kapsamları bütünüyle örtüşmez.","focus_only":"Odak dal, benzeri zor bulunan nesne ile şiir dizesi ve inci gibi kalıplaşmış uygulamaları özellikle kapsar.","gloss":"tek kalmış ve bir olan","neighbor_only":"Komşu dal bir olma, teklik, birer birer gelme ve tek başına gönderme gibi daha geniş işlemleri de kapsar.","neighbor_ref":"root_001141/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir varlığın tek başına ve eşlikçisiz bulunmasını doğrudan anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği tek kalmadır; komşu dalın çekirdeği ise kıtlık ve erişim güçlüğüdür, dolayısıyla yalnızlığın kendisini gerektirmez.","focus_only":"Odak dalda tek başına bulunma yeterlidir ve erişim güçlüğü gerekli değildir.","gloss":"eşi zor bulunan ile nadir ve güç erişilen","neighbor_only":"Komşu dal az bulunmanın yanında bir şeye erişmenin veya benzerini bulmanın güçlüğünü bildirir.","neighbor_ref":"root_001008/B003","relation_type":"near_neighbor","shared_zone":"Benzeri az bulunan bir nesne iki dalın kapsamına da girebilir."},{"boundary_match":"partial","distinction":"Komşu dal belirli insani niteliklerle sınırlı bir üstünlük veya uçluk bildirirken odak dal tek başına bulunmayı da kapsayan daha genel bir nesne niteliğidir.","focus_only":"Odak dal her tür canlı veya cansız varlığın tekliğine ve benzer azlığına uygulanabilir.","gloss":"genel eşsizlik ile bir nitelikte rakipsizlik","neighbor_only":"Komşu dal cömertlik, erdem, iyilik ya da kötülük gibi belirli değerlendirme alanlarında dengi olmayan kişiyi niteler.","neighbor_ref":"root_001240/B018","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir varlığın belli bakımdan denginin bulunmamasını anlatabilir."},{"boundary_match":"partial","distinction":"Bu çağrışım iki dalı özdeş kılmaz; odak dal genel teklik ve eşsizlik, komşu dal ise canlılara özgü ve koşulları belirli bir ebeveyn kaybı statüsüdür.","focus_only":"Odak dal ebeveyn ölümü olmadan da tek kalan veya benzeri az bulunan her şeye uygulanabilir.","gloss":"tek kalma ile ebeveynini yitirme","neighbor_only":"Komşu dal insan çocuğunda baba, hayvan yavrusunda anne ölümünü ve insan için ergenlik sınırını gerektirir.","neighbor_ref":"root_001692/B001","relation_type":"near_neighbor","shared_zone":"Ebeveynini yitiren çocuk veya yavru, tek kalma düşüncesiyle ilişkilendirilebilir."}],"source_phrase_ar":"لكل منفرد يتيم وبيت من الشعر يتيم (maqayis)؛ اليتيم الفرد (jamhara)؛ كل شيء مفرد يعز نظيره فهو يتيم ودرة يتيمة (sihah)؛ الرملة المنفردة وكل منفرد ومنفردة يتيم ويتيمة (tahdhib)؛ كل منفرد يتيم ودرة يتيمة وبيت يتيم (mufradat)","source_summary":"Kaynaklar tek kalma anlamında birleşir ve bir şeyin benzerinin az bulunmasını buna bağlı bir kapsam olarak verir. Şiir dizesi, inci ve kumluk bu ortak anlamı görünür kılan örneklerdir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه كل منفرد أو منفردة، وما عز نظيره كالدرة اليتيمة وبيت الشعر اليتيم والرملة المنفردة","what_is_not_ar":"ليس خصوص موت الأب عن الصبي ولا موت الأم عن البهيمة ولا الإبطاء في السير"},"support_links":["sup_1d706927f2fd98049969"]},{"boundary":"Buradaki anlam zihinsel dikkatsizlik ile görevde eksik bırakmayı birlikte kapsar; salt yavaşlama ayrı daldadır.","branch_kind":"mixed_non_bare","branch_ref":"root_001692/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:9:2:2","qac_word_ref":"93:9:2","surface_ar":"يَتِيمَ"}],"gloss":"dalgınlık ve gerekeni eksik yapma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Anlam, dikkat göstermeme ile bir işi veya yükümlülüğü gerektiği kadar yerine getirmemeyi birlikte kapsar."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yol alış hakkında kullanılan olumsuz kalıp, gidişte dalgınlık veya eksik davranış bulunmadığını bildirir."}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dikkat eksikliği ile görevde yetersiz kalmanın birlikte anlatıldığı genel bağlamlarda kullanılır.","boundary_detail":"Buradaki anlam zihinsel dikkatsizlik ile görevde eksik bırakmayı birlikte kapsar; salt yavaşlama ayrı daldadır.","branch_image_ar":"غفلة وتقصير","concept_gloss":"dalgınlık ve gerekeni eksik yapma","contextual_glosses":[{"applicability":"Bir kişinin yol alışında dikkatsizlik veya kusurlu davranış bulunmadığını söyleyen tanıklanmış kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Olumsuzluğu, yol alış bağlamını ve iki kusurun yokluğunu korur."},"facet_ids":["F002"],"text":"gidişinde dalgınlık veya eksiklik yok","usage_role":"contextual"}],"definition":"Bir şeyi yeterince gözetmeyerek dalgın davranma ve yapılması gerekeni eksik bırakmadır; yol alışa ilişkin kalıpta bu özelliklerin bulunmadığı söylenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Anlam, dikkat göstermeme ile bir işi veya yükümlülüğü gerektiği kadar yerine getirmemeyi birlikte kapsar."},{"facet_id":"F002","role":"associated_use","statement":"Yol alış hakkında kullanılan olumsuz kalıp, gidişte dalgınlık veya eksik davranış bulunmadığını bildirir."}],"identity_rationale":"Kaynak ifadesi dalı açıkça dalgınlık ve gerekeni eksik yapma olarak tanımlar; yol alış kalıbı da bu iki niteliğin bulunmadığını söyleyen bir uygulamadır. Geçici çerçeve kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"dalgınlık ve gerekeni eksik yapma"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"gidişinde dalgınlık veya eksik davranış yok"}],"lexicalization_note":"Yalın biçim dalgınlık ve eksik davranmayı anlatır; yol alışa ilişkin olumsuz okuma yalnız tanıklanmış cümle kalıbının kapsamındadır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dikkatsizlik, savsaklama, mazeretli eksiklik ve yavaşlama arasındaki ayrımları en iyi gösteren dört aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dikkatsizlik ile kusuru birleştirir; komşu dal ise bilinçli oyalanma, tembellik ve güçsüz değerlendirme gibi nedenleri de kapsar.","focus_only":"Odak dal dalgınlığı ve eksik yapmayı yalın bir anlam olarak, ayrıca yol alış kalıbındaki olumsuz uygulamayla verir.","gloss":"dalgınlık ve eksik yapma ile savsaklama","neighbor_only":"Komşu dal işi savsaklama, oyalanma, tembellikten yatma ve görüş zayıflığı gibi daha geniş davranışları kapsar.","neighbor_ref":"root_000902/B003","relation_type":"near_synonym","shared_zone":"İki dal da kişinin üstlendiği işi yeterince yerine getirmemesini anlatabilir."},{"boundary_match":"partial","distinction":"Komşu dal dikkat dışına çıkma olayında yoğunlaşır; odak dal ise bunun yanında görev veya davranıştaki yetersizliği de kurucu sayar.","focus_only":"Odak dal dikkat eksikliğinin yanında yapılması gerekeni eksik bırakmayı da doğrudan içerir.","gloss":"dalgınlık ve eksik yapma ile gözden kaçırma","neighbor_only":"Komşu dal bir şeyi uyanıklık ve koruma azlığından dolayı unutma veya gözden kaçırma yönünü öne çıkarır.","neighbor_ref":"root_001097/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak alanı, yeterli dikkat göstermemektir."},{"boundary_match":"partial","distinction":"Odak dal dikkatsizlik ve eksikliktir; komşu dal ise eksikliği mazeret gösterme tavrıyla birlikte tanımlar.","focus_only":"Odak dalda sahte mazeret gösterme veya kendini haklı çıkarma koşulu yoktur.","gloss":"eksik yapma ile mazeretli savsaklama","neighbor_only":"Komşu dal eksik davranışa gerçek olmayan bir mazeret gösterme veya özür görüntüsü verme boyutunu ekler.","neighbor_ref":"root_000995/B005","relation_type":"near_neighbor","shared_zone":"İki dal da bir işin gerektiği gibi yerine getirilmemesini kapsayabilir."},{"boundary_match":"partial","distinction":"Ortak kalıp anlam özdeşliği yaratmaz; bu dal davranış kusurunu, komşu dal ise hızın düşmesini veya gecikmeyi anlatır.","focus_only":"Odak dal dikkatsizlik ve gerekeni eksik yapma kusurlarını bildirir.","gloss":"dikkatsizlik ile yavaşlama","neighbor_only":"Komşu dal hareketin veya yol alışın ağırlaşmasını ve iyiliğin gecikmesini bildirir.","neighbor_ref":"root_001692/B004","relation_type":"near_neighbor","shared_zone":"Aynı yol alış ifadesi kaynaklarda iki ayrı yorumun bağlamı olabilir."}],"source_phrase_ar":"اليتم الغفلة والتقصير وما في سيره يتم أي ما فيه غفلة ولا تقصير (jamhara)؛ أصل اليتم الغفلة وبه يسمى اليتيم لأنه يتغافل عن بره (tahdhib)","source_summary":"Kaynakların ortak alanı dalgınlıktır. Eksik davranma ve yol alışta dalgınlık ya da eksiklik bulunmadığını bildiren kalıp, bunları açıkça birlikte veren aktarımın ek ayrıntılarıdır.","sources":["JA","TA"],"what_is_ar":"يدخل فيه اليتم بمعنى الغفلة والتقصير، وما نفي عن السير في قولهم ما في سيره يتم عند من فسره بذلك","what_is_not_ar":"ليس اليتم بمعنى اليتيم الذي مات أبوه ولا الانفراد النفيس ولا الإبطاء الخالص"},"support_links":[]},{"boundary":"Çekirdek hareketin ağırlaşması veya gecikmesidir; çocuğa iyiliğin geç ulaşması yalnız açıklayıcı bir bağlantıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001692/B004","candidate_links":[{"candidate_id":"cand_8cd2bbf9c3611744b95a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:9:2:2","qac_word_ref":"93:9:2","surface_ar":"يَتِيمَ"}],"gloss":"yavaşlama veya gecikme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, hareketin olağan hızından daha ağır ilerlemesi veya gecikmesidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tanıklanmış yol alış kalıbında, bir kimsenin gidişinde yavaşlama bulunduğu anlatılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Babasını yitirmiş çocuğa iyiliğin geç ulaşması, ebeveyn kaybı adlandırmasıyla kurulan açıklayıcı bağ olarak verilir."}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hareketin ya da ilerleyişin olağan hızından daha ağır sürmesini anlatan genel bağlamlarda kullanılır.","boundary_detail":"Çekirdek hareketin ağırlaşması veya gecikmesidir; çocuğa iyiliğin geç ulaşması yalnız açıklayıcı bir bağlantıdır.","branch_image_ar":"إبطاء السير والبر","concept_gloss":"yavaşlama veya gecikme","contextual_glosses":[{"applicability":"Tanıklanmış yol alış kalıbında kişinin ilerleyişinin ağır olduğunu belirtmek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yol alış bağlamını ve hareket hızının düşmesini açıkça korur."},"facet_ids":["F002"],"text":"gidişinde yavaşlama var","usage_role":"contextual"},{"applicability":"Babasını yitirmiş çocuğa gösterilen iyiliğin gecikmesini adlandırma gerekçesi olarak açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İyilik alanını, gecikmeyi ve açıklayıcı bağlantının yönünü korur."},"facet_ids":["F003"],"text":"iyiliğin geç ulaşması","usage_role":"explanatory"}],"definition":"Bir şeyin yavaşlaması veya gecikmesidir. Yol alışın ağırlaşması bunun özel uygulamasıdır; babasını yitirmiş çocuğa iyiliğin geç ulaşması ise açıklayıcı bir bağlantıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, hareketin olağan hızından daha ağır ilerlemesi veya gecikmesidir."},{"facet_id":"F002","role":"specialization","statement":"Tanıklanmış yol alış kalıbında, bir kimsenin gidişinde yavaşlama bulunduğu anlatılır."},{"facet_id":"F003","role":"associated_use","statement":"Babasını yitirmiş çocuğa iyiliğin geç ulaşması, ebeveyn kaybı adlandırmasıyla kurulan açıklayıcı bağ olarak verilir."}],"identity_rationale":"Kaynak ifadesi yavaşlama anlamını ve yol alış uygulamasını doğrudan destekler; babasını yitirmiş çocuğa iyiliğin geç ulaşması ise adlandırmayı açıklayan bağımlı bir gerekçedir. Bu açıklama çekirdekle eş düzeye çıkarılmadan dal korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"gidişinde yavaşlama var"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yavaşlama ve gecikme"}],"lexicalization_note":"Yalın biçim yavaşlama anlamını taşır; yol alış okuması kendi kalıbında tutulur ve iyiliğin geç ulaşması bağımsız bir yalın anlam sayılmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; çaba eksikliği, güçten düşme, isteksiz ağırlaşma ve dikkatsizlikten ayrımı en belirgin dört komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hız ve zaman bakımından ağırlaşmayı temel alır; komşu dal ise görevde yetersiz çaba gösterme anlamına da uzanır.","focus_only":"Odak dal yalın yavaşlamayı ve babasını yitirmiş çocuğa iyiliğin geç ulaşmasına ilişkin açıklamayı içerir.","gloss":"yavaşlama ile çabada geri kalma","neighbor_only":"Komşu dal bir işte, özellikle öğüt vermede, gereken çabayı göstermeyip geri kalmayı da içerir.","neighbor_ref":"root_000048/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir işin veya ilerleyişin beklenenden geç gerçekleşmesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal gözlenen hız düşüşüdür; komşu dal ise hareketin altında yatan gevşeme ve güç azalması durumunu öne çıkarır.","focus_only":"Odak dal yavaşlamayı nedenine bakmadan bildirir ve iyiliğin gecikmesine ilişkin açıklayıcı bir bağlantı taşır.","gloss":"yavaşlama ile güçten düşme","neighbor_only":"Komşu dal işte veya yol alışta güç ve canlılığın azalmasından doğan gevşemeyi anlatır.","neighbor_ref":"root_001621/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal yol alışın veya işin daha ağır sürmesine uygulanabilir."},{"boundary_match":"partial","distinction":"Odak dal sonucun hız boyutunu adlandırır; komşu dal bedensel veya ruhsal gevşekliği kurucu unsur yapar.","focus_only":"Odak dal gecikmeyi ve ilerleyişin ağırlaşmasını bedensel bir neden gerektirmeden anlatır.","gloss":"gecikme ile gevşek ve isteksiz davranma","neighbor_only":"Komşu dal tembellik, ateşli hastalık veya beden gevşekliğiyle bağlantılı isteksizlik ve ağır davranmayı kapsar.","neighbor_ref":"root_000392/B001","relation_type":"near_neighbor","shared_zone":"Ağır yürüyen veya işini yavaş yapan kişi iki alanın görünür sonucunu paylaşabilir."},{"boundary_match":"partial","distinction":"Bu dal zamansal ve devinimsel ağırlaşmadır; komşu dal ise davranış ve dikkat kusurudur.","focus_only":"Odak dal hareket hızının düşmesini veya bir şeyin geç ulaşmasını anlatır.","gloss":"yavaşlama ile dikkatsizlik","neighbor_only":"Komşu dal dikkat göstermemeyi ve yapılması gerekeni eksik bırakmayı anlatır.","neighbor_ref":"root_001692/B003","relation_type":"near_neighbor","shared_zone":"Yol alışa ilişkin aynı kalıp iki anlam için kaynaklarda yorumlanmıştır."}],"source_phrase_ar":"في سيره يتم أي إبطاء (sihah)؛ اليتم الإبطاء ومنه أخذ اليتيم لأن البر يبطىء عنه (tahdhib)","source_summary":"Kaynakların ortak alanı genel yavaşlama ve gecikmedir. Yol alıştaki ağırlaşma bir aktarımdaki özel uygulama, iyiliğin babasını yitirmiş çocuğa geç ulaşması ise diğer aktarımdaki adlandırma açıklamasıdır.","sources":["SI","TA"],"what_is_ar":"يدخل فيه اليتم بمعنى الإبطاء، وخاصة قولهم في سيره يتم، وتعليل تسمية اليتيم بأن البر يبطئ عنه","what_is_not_ar":"ليس الغفلة والتقصير إلا حيث جعلها المصدر تفسيرا آخر، وليس الانفراد في الشيء"},"support_links":["sup_15df0278960ea7dac528"]},{"boundary":"Kullanım yalnız kadınlara yönelik tanıklanmış adlandırma kalıplarıyla sınırlıdır; gerçek bir eş kaybı veya genel eşsizlik anlamı çıkarılamaz.","branch_kind":"collocation","branch_ref":"root_001692/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:9:2:2","qac_word_ref":"93:9:2","surface_ar":"يَتِيمَ"}],"gloss":"evlilikle sona erip ermediği tartışmalı kadın adlandırması","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kullanım, babasını yitirmiş çocuklara verilen adın kadın hakkında da söylenmesinden oluşur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir aktarımda kadın evlenince bu adlandırma sona erer; karşıt aktarımda ise kadın bu adı hiçbir zaman yitirmez."}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kadına yönelik bu özel adın evlilikten sonra sürüp sürmediğine ilişkin iki aktarımı birlikte özetlerken kullanılır.","boundary_detail":"Kullanım yalnız kadınlara yönelik tanıklanmış adlandırma kalıplarıyla sınırlıdır; gerçek bir eş kaybı veya genel eşsizlik anlamı çıkarılamaz.","branch_image_ar":"انفراد المرأة عن الزوج","concept_gloss":"evlilikle sona erip ermediği tartışmalı kadın adlandırması","contextual_glosses":[{"applicability":"Adlandırmanın kadının evlenmesiyle sona erdiğini kabul eden aktarımın bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadına yönelik kullanımı ve evlilikte sona erme sınırını korur."},"facet_ids":["F001","F002"],"text":"evlenene dek bu adla anılan kadın","usage_role":"contextual"},{"applicability":"Adlandırmanın evlilikten sonra da sürdüğünü kabul eden karşıt aktarımın bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadına yönelik kullanımı ve evlilikten sonra sürme bilgisini korur."},"facet_ids":["F001","F002"],"text":"evlendikten sonra da bu adla anılan kadın","usage_role":"contextual"}],"definition":"Kadına, babasını yitirmiş çocuklara verilen adla seslenilen kalıplaşmış bir kullanımdır. Bir aktarım bu adın evlilikle sona erdiğini, diğeri ise evlilikten sonra da sürdüğünü bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kullanım, babasını yitirmiş çocuklara verilen adın kadın hakkında da söylenmesinden oluşur."},{"facet_id":"F002","role":"source_variant","statement":"Bir aktarımda kadın evlenince bu adlandırma sona erer; karşıt aktarımda ise kadın bu adı hiçbir zaman yitirmez."}],"identity_rationale":"Kaynak ifadesi kocasından ayrılmış kadını tanımlamaz; kadına belirli bir adın verilmesini ve bu adın evlilikle sona erip ermediğine ilişkin iki karşıt aktarımı bildirir. Dal korunabilir, ancak tanımı eşten ayrılma yerine bu kalıplaşmış ve tartışmalı adlandırmaya bağlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"evlenene dek, başka bir aktarıma göre ise evlendikten sonra da babasını yitirmiş çocuk adıyla anılan kadın"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kadınların babasını yitirmiş çocuk adıyla anılabileceğini bildiren söz"}],"lexicalization_note":"Tanım yalnız kadın hakkında kullanılan iki tanıklanmış söz kalıbına bağlıdır; buradan yalın biçime genel bir evlenmemişlik veya eşten ayrılma anlamı aktarılamaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel kadın adlandırmasını eşsiz olma, eşten kopma, ebeveyn kaybı ve eş olma alanlarından ayıran dört aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal gerçek medeni durumu tanımlamak yerine özel bir adlandırmayı aktarır; komşu dal ise kişinin eşinin bulunmamasını cinsiyet ayrımı olmadan bildirir.","focus_only":"Odak dal kadınlara verilen özel bir addır ve bir aktarımda evlilikten sonra da sürebilir.","gloss":"kadına verilen özel ad ile eşsiz olma","neighbor_only":"Komşu dal kadın veya erkeğin fiilen eşsiz olmasını ve evlenmeden kalmasını doğrudan anlatır.","neighbor_ref":"root_000073/B001","relation_type":"near_neighbor","shared_zone":"Evlenmemiş kadın, bir aktarımda iki kullanımın ortak bağlamında bulunabilir."},{"boundary_match":"partial","distinction":"Odak dal eşten ayrılmayı gerektirmez; komşu dalın çekirdeği ise eş bağının bulunmaması veya kesilmesidir.","focus_only":"Odak dal evlilik öncesinde kullanılan ve bazı aktarımlarda evlilik sonrasında da süren bir kadın adlandırmasıdır.","gloss":"kadın adlandırması ile eşten kopma","neighbor_only":"Komşu dal eşten kopma, uzun süre eşsiz kalma ve evlenmeme durumunu anlatır.","neighbor_ref":"root_001252/B009","relation_type":"near_neighbor","shared_zone":"Her iki dal kadın ve evlilik durumu çevresinde kullanılabilir."},{"boundary_match":"partial","distinction":"Biçim ortaklığına rağmen odak dalda ebeveyn ölümü kurucu değildir; komşu dalda ise ebeveynin ölümü ve katılımcı ayrımı anlamın temelidir.","focus_only":"Odak dal kadın hakkındaki kalıplaşmış adlandırmayı ve süresine ilişkin aktarım ayrılığını içerir.","gloss":"kadına verilen ad ile ebeveyn kaybı","neighbor_only":"Komşu dal insan çocuğunun babasını ergenlikten önce, hayvan yavrusunun ise annesini yitirmesiyle oluşan gerçek durumu bildirir.","neighbor_ref":"root_001692/B001","relation_type":"near_neighbor","shared_zone":"Kadına verilen ad, babasını yitirmiş çocuk için kullanılan adlandırmayla biçimsel olarak ortaktır."},{"boundary_match":"thematic_only","distinction":"Odak dalın içeriği adlandırmanın süresidir; komşu dalın içeriği ise eşin kendisi ve eş olma bağıdır, bu nedenle anlamsal örtüşme çok sınırlıdır.","focus_only":"Odak dal, kadına yönelik özel bir adın evlilikle sona erip ermediğini tartışır.","gloss":"kadın adlandırması ve eş olma","neighbor_only":"Komşu dal eş olan erkeği, eş olan kadını ve eş olma ilişkisini doğrudan adlandırır.","neighbor_ref":"root_000134/B001","relation_type":"thematic","shared_zone":"İki dal da evlilik ilişkisini çevreleyen söz varlığında yer alır."}],"source_phrase_ar":"المرأة تدعى يتيما ما لم تتزوج فإذا تزوجت زال عنها اسم اليتم؛ يقال للمرأة يتيمة لا يزول عنها اسم اليتم أبدا (tahdhib)","source_qualifications":[{"kind":"disagreement","summary":"Bir aktarım adlandırmayı evlenene kadar sürdürürken diğeri evliliğin bu adı sona erdirmediğini bildirir."}],"source_summary":"Kanıt, kadınlara özgü bu kalıplaşmış adlandırmanın evlilikle ilişkili olduğunu, ancak kullanım süresinin tek biçimde aktarılmadığını gösterir.","sources":["TA"],"what_is_ar":"يدخل فيه إطلاق يتيمة على المرأة عند من يجعله قبل الزواج أو لا يزيله الزواج","what_is_not_ar":"ليس اليتيم من الصبيان ولا كل منفرد من الأشياء ولا أم الأيتام"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["93:9:1"],"branch_refs":[],"candidate_id":"cand_63479c742ed57ef1a438","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:9:1:benefaction-to-command-link","source_type":"word_analysis","support_ids":["sup_642752aff0d424f03271","sup_f48cc1503e24125394ff"],"title":"prior benefaction becomes ethical consequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:1","qac_refs":["93:9:1:1"],"status":"accepted"}},{"anchor_refs":["93:9:1"],"branch_refs":[],"candidate_id":"cand_46616145a8ea0cd766cc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:9:1:compact-section-pivot","source_type":"word_analysis","support_ids":["sup_13f80d6ec4a8f0cc4f85","sup_f48cc1503e24125394ff"],"title":"compact launch into the case frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:1","qac_refs":["93:9:1:1"],"status":"accepted"}},{"anchor_refs":["93:9:1"],"branch_refs":[],"candidate_id":"cand_1dc5d1db6643a6e6cc7f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:9:1:fa-reprise-sequence","source_type":"word_analysis","support_ids":["sup_67537c9e8d15d9fa1b98","sup_f48cc1503e24125394ff"],"title":"repeated particle cadence frames the section","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:1","qac_refs":["93:9:1:1"],"status":"accepted"}},{"anchor_refs":["93:9:2"],"branch_refs":[],"candidate_id":"cand_3c0eff2fd92185fbcfab","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:9:2:case-response-frame","source_type":"word_analysis","support_ids":["sup_b8ed947c657083a987f9","sup_ec0b2657999b36c17caf"],"title":"case frame requires a response","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:2","qac_refs":["93:9:1:2"],"status":"accepted"}},{"anchor_refs":["93:9:2"],"branch_refs":[],"candidate_id":"cand_d8422f942cb9248b66fc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:9:2:ethical-scene-change","source_type":"word_analysis","support_ids":["sup_198de5ca3a09dbfc565b","sup_b8ed947c657083a987f9"],"title":"new ethical scene opens","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:2","qac_refs":["93:9:1:2"],"status":"accepted"}},{"anchor_refs":["93:9:2"],"branch_refs":[],"candidate_id":"cand_df95cc7ec64c41bcc59b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:9:2:fronted-object-licensing","source_type":"word_analysis","support_ids":["sup_09338da81da06e8ca4a0","sup_b8ed947c657083a987f9"],"title":"fronted protected object licensed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:2","qac_refs":["93:9:1:2"],"status":"accepted"}},{"anchor_refs":["93:9:2"],"branch_refs":[],"candidate_id":"cand_ce3121d4fae0ded23801","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:9:2:threefold-distributive-sequence","source_type":"word_analysis","support_ids":["sup_b8ed947c657083a987f9","sup_c493c448056b9120198b"],"title":"first member of the 93:9-11 distribution","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:2","qac_refs":["93:9:1:2"],"status":"accepted"}},{"anchor_refs":["93:9:3"],"branch_refs":[],"candidate_id":"cand_87c20782ab731f39b9cc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"93:9:3:audible-topic-binding","source_type":"word_analysis","support_ids":["sup_8c2615d7eb63cbb41c95","sup_c011651d6230d8775c9d"],"title":"sound binds frame to topic before force arrives","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:3","qac_refs":["93:9:2:1","93:9:2:2"],"status":"accepted"}},{"anchor_refs":["93:9:3"],"branch_refs":[],"candidate_id":"cand_b353f6511d1cabb898aa","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"93:9:3:boundary-lack-sequence","source_type":"word_analysis","support_ids":["sup_8c2615d7eb63cbb41c95","sup_bba903f1ab329b4e2ae1"],"title":"lack field enters the command unit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:3","qac_refs":["93:9:2:1","93:9:2:2"],"status":"accepted"}},{"anchor_refs":["93:9:3"],"branch_refs":[],"candidate_id":"cand_790260afe1218b920e50","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"93:9:3:definite-substantive-status","source_type":"word_analysis","support_ids":["sup_8c2615d7eb63cbb41c95","sup_ff897d2c72225f976fb7"],"title":"definite singular status-name","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:3","qac_refs":["93:9:2:1","93:9:2:2"],"status":"accepted"}},{"anchor_refs":["93:9:3"],"branch_refs":[],"candidate_id":"cand_99e2df571e18af4283b2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"93:9:3:fronted-accusative-object","source_type":"word_analysis","support_ids":["sup_1f2fa074b5303d788796","sup_8c2615d7eb63cbb41c95"],"title":"fronted object remains governed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:3","qac_refs":["93:9:2:1","93:9:2:2"],"status":"accepted"}},{"anchor_refs":["93:9:3"],"branch_refs":[],"candidate_id":"cand_581f42f74e23e71d2449","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"93:9:3:patient-beneficiary-asymmetry","source_type":"word_analysis","support_ids":["sup_62050278cf0bdd92d379","sup_8c2615d7eb63cbb41c95"],"title":"potential patient becomes protected beneficiary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:3","qac_refs":["93:9:2:1","93:9:2:2"],"status":"accepted"}},{"anchor_refs":["93:9:3"],"branch_refs":[],"candidate_id":"cand_7ccd6a1c3527a81864f6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"93:9:3:same-surah-orphan-echo","source_type":"word_analysis","support_ids":["sup_21f0b20e262d064c9aeb","sup_8c2615d7eb63cbb41c95"],"title":"93:6 orphanhood returns as responsibility","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:3","qac_refs":["93:9:2:1","93:9:2:2"],"status":"accepted"}},{"anchor_refs":["93:9:3"],"branch_refs":[],"candidate_id":"cand_545b0a2f0b53f6c3a273","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"93:9:3:vulnerability-and-singularity-pressure","source_type":"word_analysis","support_ids":["sup_8c2615d7eb63cbb41c95","sup_def70ab39e4e810f5193"],"title":"orphanhood with isolation and preciousness pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:3","qac_refs":["93:9:2:1","93:9:2:2"],"status":"accepted"}},{"anchor_refs":["93:9:4"],"branch_refs":[],"candidate_id":"cand_495e3b9fe4f14e2a1527","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:9:4:apodotic-answer-marker","source_type":"word_analysis","support_ids":["sup_11d7b743546559ee3076","sup_14917672fb786322bfdf"],"title":"required answer to the case frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:4","qac_refs":["93:9:3:1"],"status":"accepted"}},{"anchor_refs":["93:9:4"],"branch_refs":[],"candidate_id":"cand_fcf1fbbb7faa446501cc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:9:4:compressed-prohibition-onset","source_type":"word_analysis","support_ids":["sup_14917672fb786322bfdf","sup_d7096ef67b639003a71a"],"title":"response fused to the ban","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:4","qac_refs":["93:9:3:1"],"status":"accepted"}},{"anchor_refs":["93:9:4"],"branch_refs":[],"candidate_id":"cand_6a53183dc8c43e00cfa5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:9:4:same-form-different-function","source_type":"word_analysis","support_ids":["sup_0bfe24e1665839e41daf","sup_14917672fb786322bfdf"],"title":"same particle form, new local function","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:4","qac_refs":["93:9:3:1"],"status":"accepted"}},{"anchor_refs":["93:9:5"],"branch_refs":[],"candidate_id":"cand_33892bc7ac1b1d670c64","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:9:5:paired-prohibition-template","source_type":"word_analysis","support_ids":["sup_84ed960268d00858aa79","sup_a4fc5671717c2eec8ab2"],"title":"first negative member of 93:9-11","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:5","qac_refs":["93:9:3:2"],"status":"accepted"}},{"anchor_refs":["93:9:5"],"branch_refs":[],"candidate_id":"cand_e5723029b4bf1d0bef0d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:9:5:prohibitive-la-jussive","source_type":"word_analysis","support_ids":["sup_3a7ef8f571c926f1a60e","sup_a4fc5671717c2eec8ab2"],"title":"prohibitive particle governs jussive","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:5","qac_refs":["93:9:3:2"],"status":"accepted"}},{"anchor_refs":["93:9:5"],"branch_refs":[],"candidate_id":"cand_3cd9ba9bd9467f43585e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:9:5:response-fused-to-negation","source_type":"word_analysis","support_ids":["sup_8b59eb6562845c90ac8b","sup_a4fc5671717c2eec8ab2"],"title":"answer marker enters prohibition directly","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:5","qac_refs":["93:9:3:2"],"status":"accepted"}},{"anchor_refs":["93:9:5"],"branch_refs":[],"candidate_id":"cand_5df01e08ac9478e5bb93","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:9:5:scope-and-ethical-boundary","source_type":"word_analysis","support_ids":["sup_0a6aaf6c5c9c11a09d1c","sup_a4fc5671717c2eec8ab2"],"title":"verb barred, object affirmed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:5","qac_refs":["93:9:3:2"],"status":"accepted"}},{"anchor_refs":["93:9:5"],"branch_refs":[],"candidate_id":"cand_44c8558862ec5cdeb7ec","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:9:5:vocal-delay-before-force-word","source_type":"word_analysis","support_ids":["sup_88cede8403247877ae5f","sup_a4fc5671717c2eec8ab2"],"title":"open negation before clipped force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:5","qac_refs":["93:9:3:2"],"status":"accepted"}},{"anchor_refs":["93:9:6"],"branch_refs":[],"candidate_id":"cand_fee80c0c787380dbf0fa","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001266"],"scope":"focus_ayah","source_local_id":"93:9:6:agency-and-moral-valence","source_type":"word_analysis","support_ids":["sup_08e974b2fb57a321f55f","sup_c8c7021157eb90e4ed9c"],"title":"power holder restrained for the vulnerable patient","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:6","qac_refs":["93:9:4:1"],"status":"accepted"}},{"anchor_refs":["93:9:6"],"branch_refs":[],"candidate_id":"cand_e1f99964fddac79cdd20","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001266"],"scope":"focus_ayah","source_local_id":"93:9:6:closure-and-delay","source_type":"word_analysis","support_ids":["sup_2510a456f056a87b8ada","sup_c8c7021157eb90e4ed9c"],"title":"delayed final verb lands as hard stop","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:6","qac_refs":["93:9:4:1"],"status":"accepted"}},{"anchor_refs":["93:9:6"],"branch_refs":[],"candidate_id":"cand_91d5144973489c6d61ac","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001266"],"scope":"focus_ayah","source_local_id":"93:9:6:convergent-form-root-distribution","source_type":"word_analysis","support_ids":["sup_c8c7021157eb90e4ed9c","sup_e5ede81a288d22296c6a"],"title":"root sense, form, and rarity converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:6","qac_refs":["93:9:4:1"],"status":"accepted"}},{"anchor_refs":["93:9:6"],"branch_refs":[],"candidate_id":"cand_6d2816b2e3ea9024df5b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001266"],"scope":"focus_ayah","source_local_id":"93:9:6:divine-human-boundary","source_type":"word_analysis","support_ids":["sup_c5a61d1a937c1684ae17","sup_c8c7021157eb90e4ed9c"],"title":"divine overpowering field barred as human act","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:6","qac_refs":["93:9:4:1"],"status":"accepted"}},{"anchor_refs":["93:9:6"],"branch_refs":[],"candidate_id":"cand_36215c7747c674e024f6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001266"],"scope":"focus_ayah","source_local_id":"93:9:6:finite-verb-shift","source_type":"word_analysis","support_ids":["sup_c8c7021157eb90e4ed9c","sup_df3276a28c02674c111c"],"title":"narrative recipient becomes restrained actor","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:6","qac_refs":["93:9:4:1"],"status":"accepted"}},{"anchor_refs":["93:9:6"],"branch_refs":[],"candidate_id":"cand_7028d8e6c45f2266c51f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001266"],"scope":"focus_ayah","source_local_id":"93:9:6:form-i-low-threshold","source_type":"word_analysis","support_ids":["sup_af8fd6c440831a56577d","sup_c8c7021157eb90e4ed9c"],"title":"simple Form I lowers the threshold","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:6","qac_refs":["93:9:4:1"],"status":"accepted"}},{"anchor_refs":["93:9:6"],"branch_refs":[],"candidate_id":"cand_118b299279e6d609cb17","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001266"],"scope":"focus_ayah","source_local_id":"93:9:6:fronted-object-valency","source_type":"word_analysis","support_ids":["sup_9f567ff64195c72fdb48","sup_c8c7021157eb90e4ed9c"],"title":"object gap supplied by fronting","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:6","qac_refs":["93:9:4:1"],"status":"accepted"}},{"anchor_refs":["93:9:6"],"branch_refs":[],"candidate_id":"cand_f75c426cbd19ad53eb4f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001266"],"scope":"focus_ayah","source_local_id":"93:9:6:jussive-second-person-prohibition","source_type":"word_analysis","support_ids":["sup_c8c7021157eb90e4ed9c","sup_f8d562379e170ffa80a1"],"title":"jussive address regulates possible conduct","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:6","qac_refs":["93:9:4:1"],"status":"accepted"}},{"anchor_refs":["93:9:6"],"branch_refs":[],"candidate_id":"cand_7597ae77a9a9a8bfdd50","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001266"],"scope":"focus_ayah","source_local_id":"93:9:6:paired-prohibition-projection","source_type":"word_analysis","support_ids":["sup_a035b731e74f490f5f51","sup_c8c7021157eb90e4ed9c"],"title":"current verb anticipates the next prohibition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:6","qac_refs":["93:9:4:1"],"status":"accepted"}},{"anchor_refs":["93:9:6"],"branch_refs":[],"candidate_id":"cand_4e69e49838ce09a9cd06","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001266"],"scope":"focus_ayah","source_local_id":"93:9:6:qahr-overpowering-sense","source_type":"word_analysis","support_ids":["sup_94be4026120e26eacf13","sup_c8c7021157eb90e4ed9c"],"title":"overpowering, compulsion, and humiliation selected","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:6","qac_refs":["93:9:4:1"],"status":"accepted"}},{"anchor_refs":["93:9:6"],"branch_refs":[],"candidate_id":"cand_ba974f347177c7b45bd9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001266"],"scope":"focus_ayah","source_local_id":"93:9:6:response-clause-completion","source_type":"word_analysis","support_ids":["sup_c8c7021157eb90e4ed9c","sup_f052f6fda42d0b002c5f"],"title":"verbal core completes the apodosis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:6","qac_refs":["93:9:4:1"],"status":"accepted"}},{"anchor_refs":["93:9:6"],"branch_refs":[],"candidate_id":"cand_a6777795e5b3a43ecfb6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001266"],"scope":"focus_ayah","source_local_id":"93:9:6:same-surah-role-reversal","source_type":"word_analysis","support_ids":["sup_822ba18ff34a19849c39","sup_c8c7021157eb90e4ed9c"],"title":"received care becomes restraint toward another","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:6","qac_refs":["93:9:4:1"],"status":"accepted"}},{"anchor_refs":["93:9:6"],"branch_refs":[],"candidate_id":"cand_045b0c647584a5e4b4d5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001266"],"scope":"focus_ayah","source_local_id":"93:9:6:variant-and-sound-gradient","source_type":"word_analysis","support_ids":["sup_4dc1d63ade62e6a886f9","sup_c8c7021157eb90e4ed9c"],"title":"variant pressure broadens harshness gradient","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:9:6","qac_refs":["93:9:4:1"],"status":"accepted"}},{"anchor_refs":["93:9:2"],"branch_refs":[],"candidate_id":"cand_97d7ea7db9db9980d2b1","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"93:9:2:2","source_type":"qac_morpheme","support_ids":["sup_01c75f26a4a34f34f693"],"title":"QAC root occurrence: ي ت م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["93:9:4"],"branch_refs":[],"candidate_id":"cand_ff30d0fbb857a32c5d28","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001266"],"scope":"focus_ayah","source_local_id":"93:9:4:1","source_type":"qac_morpheme","support_ids":["sup_dba39ec5e81e97ac1eba"],"title":"QAC root occurrence: ق ه ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["93:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:9","branch_refs":["root_001266/B001","root_001692/B001"],"candidate_id":"cand_d108c9cf1c90617f75d2","commentary_obligation":"review","hft_ref":"hft_f7ac44a586a12a66b15a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_protection_gap_not_power_license","source_type":"hft","support_ids":["sup_c5e1860a46c73db2e482"],"title":"b_protection_gap_not_power_license","trust":"legacy_unbound"},{"anchor_refs":["93:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:9","branch_refs":["root_001266/B001","root_001692/B002"],"candidate_id":"cand_2fef02847711972219db","commentary_obligation":"review","hft_ref":"hft_cc2dbac611447aa5e69c","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_solitude_not_social_lowliness","source_type":"hft","support_ids":["sup_1d706927f2fd98049969"],"title":"b_solitude_not_social_lowliness","trust":"legacy_unbound"},{"anchor_refs":["93:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:9","branch_refs":["root_001266/B001","root_001692/B004"],"candidate_id":"cand_8cd2bbf9c3611744b95a","commentary_obligation":"review","hft_ref":"hft_393d417a33642f41108b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_withheld_care_as_quiet_qahr","source_type":"hft","support_ids":["sup_15df0278960ea7dac528"],"title":"b_withheld_care_as_quiet_qahr","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"93:9:1:1","qac_word_ref":"93:9:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"أَمَّا","morph_features":"STEM|POS:EXL|LEM:>am~aA","morpheme_role":"STEM","pos":"EXL","qac_ref":"93:9:1:2","qac_word_ref":"93:9:1","root_ar":"","surface_ar":"أَمَّا"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"93:9:2:1","qac_word_ref":"93:9:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:9:2:2","qac_word_ref":"93:9:2","root_ar":"ي ت م","surface_ar":"يَتِيمَ"},{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"93:9:3:1","qac_word_ref":"93:9:3","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:PRO|LEM:laA","morpheme_role":"STEM","pos":"PRO","qac_ref":"93:9:3:2","qac_word_ref":"93:9:3","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"تَقْهَرْ","morph_features":"STEM|POS:V|IMPF|LEM:taqoharo|ROOT:qhr|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"93:9:4:1","qac_word_ref":"93:9:4","root_ar":"ق ه ر","surface_ar":"تَقْهَرْ"}],"word_analysis_qac_refs":[["93:9:1:1"],["93:9:1:2"],["93:9:2:1","93:9:2:2"],["93:9:3:1"],["93:9:3:2"],["93:9:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["93:9:1","93:9:2","93:9:3","93:9:4","93:9:5","93:9:6"]},"focus_surface_evidence":{"arabic_uthmani":"فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"93:9:1:1","qac_word_ref":"93:9:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"أَمَّا","morph_features":"STEM|POS:EXL|LEM:>am~aA","morpheme_role":"STEM","pos":"EXL","qac_ref":"93:9:1:2","qac_word_ref":"93:9:1","root_ar":"","surface_ar":"أَمَّا"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"93:9:2:1","qac_word_ref":"93:9:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:9:2:2","qac_word_ref":"93:9:2","root_ar":"ي ت م","surface_ar":"يَتِيمَ"},{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"93:9:3:1","qac_word_ref":"93:9:3","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:PRO|LEM:laA","morpheme_role":"STEM","pos":"PRO","qac_ref":"93:9:3:2","qac_word_ref":"93:9:3","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"تَقْهَرْ","morph_features":"STEM|POS:V|IMPF|LEM:taqoharo|ROOT:qhr|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"93:9:4:1","qac_word_ref":"93:9:4","root_ar":"ق ه ر","surface_ar":"تَقْهَرْ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["93:9:1:1"],["93:9:1:2"],["93:9:2:1","93:9:2:2"],["93:9:3:1"],["93:9:3:2"],["93:9:4:1"]],"word_analysis_refs":["93:9:1","93:9:2","93:9:3","93:9:4","93:9:5","93:9:6"],"word_rows":[{"analysis_record_ref":"93:9:1","analytic_gloss_range_en":"resumptive and consequential opening particle that links the remembered benefactions of 93:6-8 to the ethical commands of 93:9-11","analytic_root_gloss_range_en":null,"qac_refs":["93:9:1:1"],"root":{},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"93:9:2","analytic_gloss_range_en":"conditional-distributive case marker that sets the orphan before the response and requires a later apodotic particle","analytic_root_gloss_range_en":null,"qac_refs":["93:9:1:2"],"root":{},"surface":{"arabic":"أَمَّا","transliteration":"ammā"}},{"analysis_record_ref":"93:9:3","analytic_gloss_range_en":"the definite singular orphan as a protected class representative and fronted direct object; the local sense is bereft-of-protector vulnerability, with singularity or preciousness only as secondary pressure","analytic_root_gloss_range_en":"root range includes orphanhood through loss of the protecting parent, isolated or peerless singleness, and more remote shortcoming, delay, or marriage-related usages; the local ayah selects orphaned vulnerability while allowing isolation and preciousness pressure","qac_refs":["93:9:2:1","93:9:2:2"],"root":{"arabic":"ي ت م","transliteration":"y-t-m"},"surface":{"arabic":"ٱلْيَتِيمَ","transliteration":"al-yatīma"}},{"analysis_record_ref":"93:9:4","analytic_gloss_range_en":"required apodotic response particle after the case frame, fused to the prohibition onset","analytic_root_gloss_range_en":null,"qac_refs":["93:9:3:1"],"root":{},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"93:9:5","analytic_gloss_range_en":"prohibitive negation governing the following jussive verb; it bars the act of overpowering while leaving the fronted orphan affirmed as the case","analytic_root_gloss_range_en":null,"qac_refs":["93:9:3:2"],"root":{},"surface":{"arabic":"لَا","transliteration":"lā"}},{"analysis_record_ref":"93:9:6","analytic_gloss_range_en":"jussive second-person Form I prohibition against overpowering, subduing, humiliating, or harshly imposing force on the fronted orphan object","analytic_root_gloss_range_en":"root range includes overpowering from above, subduing, compelling, humiliation, and unrelated lexical branches such as cooking, stones, backward retreat, packed food, and a named creature; the local ayah selects the overpowering and humbling branch under prohibition","qac_refs":["93:9:4:1"],"root":{"arabic":"ق ه ر","transliteration":"q-h-r"},"surface":{"arabic":"تَقْهَرْ","transliteration":"taqhar"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":6,"words_total":6,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["93:9"],"branch_refs":["root_001266/B001","root_001692/B001"],"candidate_id":"cand_d108c9cf1c90617f75d2","evidence_scope":"focus_ayah","hft_ref":"hft_f7ac44a586a12a66b15a","item_id":"b_protection_gap_not_power_license","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_protection_gap_not_power_license","support_id":"sup_c5e1860a46c73db2e482"},{"anchor_refs":["93:9"],"branch_refs":["root_001266/B001","root_001692/B002"],"candidate_id":"cand_2fef02847711972219db","evidence_scope":"focus_ayah","hft_ref":"hft_cc2dbac611447aa5e69c","item_id":"b_solitude_not_social_lowliness","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_solitude_not_social_lowliness","support_id":"sup_1d706927f2fd98049969"},{"anchor_refs":["93:9"],"branch_refs":["root_001266/B001","root_001692/B004"],"candidate_id":"cand_8cd2bbf9c3611744b95a","evidence_scope":"focus_ayah","hft_ref":"hft_393d417a33642f41108b","item_id":"b_withheld_care_as_quiet_qahr","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_withheld_care_as_quiet_qahr","support_id":"sup_15df0278960ea7dac528"}],"diagnostics":[],"lane_counts":{"global":9,"macro":13,"micro":3},"packet_summary":{"ayah_count":11,"focus_ref":"93:9","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"و ج د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001626","furuq_root_norm":"و ج د","furuq_source_root_norm":"و ج د","is_dominant":true,"target_occurrences":61,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000227","furuq_root_norm":"ج د د","furuq_source_root_norm":"ج د د","is_dominant":false,"target_occurrences":10,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ء ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000661","furuq_root_norm":"س ء ل","furuq_source_root_norm":"س أ ل","is_dominant":true,"target_occurrences":118,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000736","furuq_root_norm":"س ل ل","furuq_source_root_norm":"س ل ل","is_dominant":false,"target_occurrences":2,"target_rank":2}]}],"window":["93:1","93:2","93:3","93:4","93:5","93:6","93:7","93:8","93:9","93:10","93:11"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"93:9","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":16,"unstructured_record_count":0},"identity":{"ayah_ref":"93:9","lane":"micro","linguistic_source_ref":"93:9","surface_ref":"93:9","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"93:9","target_tokens":[["Öyleyse",["93:9:1"]],["yetimi",["93:9:2"]],["ezme",["93:9:3","93:9:4"]]],"text":"Öyleyse yetimi ezme."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s093-p01-001-011","label":"Whole surah","number":1,"refs":["93:1","93:2","93:3","93:4","93:5","93:6","93:7","93:8","93:9","93:10","93:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"93:9:2:2","source_type":"qac_morpheme","support_id":"sup_01c75f26a4a34f34f693","text":"{\"lemma_ar\":\"يَتِيم\",\"morph_features\":\"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"93:9:2:2\",\"qac_word_ref\":\"93:9:2\",\"root_ar\":\"ي ت م\",\"surface_ar\":\"يَتِيمَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:6:agency-and-moral-valence","source_type":"word_analysis","support_id":"sup_08e974b2fb57a321f55f","text":"{\"blocking_evidence\":null,\"headline\":\"power holder restrained for the vulnerable patient\",\"reader_payoff\":\"The reader notices the moral asymmetry: the addressee has agency, the orphan is exposed to the act, and the prohibition converts that power into a boundary.\",\"reason\":\"The second-person subject is the potential agent, the fronted orphan is the patient, and prohibitive grammar makes the selected q-h-r act barred conduct.\",\"representative_source_ids\":[\"QS-cbfa779b\",\"QS-f05cc111\",\"MS-2ef346e4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:2:fronted-object-licensing","source_type":"word_analysis","support_id":"sup_09338da81da06e8ca4a0","text":"{\"blocking_evidence\":null,\"headline\":\"fronted protected object licensed\",\"reader_payoff\":\"The reader notices that the construction lets the vulnerable party stand first while remaining grammatically tied to the later verb.\",\"reason\":\"Attachment evidence marks {{ar:ٱلْيَتِيمَ}} ({{tr:al-yatīma}}) as the fronted direct object of the later verb, not as an isolated topic outside the prohibition.\",\"representative_source_ids\":[\"QT-0d887f66\",\"QT-45873acd\",\"QT-74b77998\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:5:scope-and-ethical-boundary","source_type":"word_analysis","support_id":"sup_0a6aaf6c5c9c11a09d1c","text":"{\"blocking_evidence\":null,\"headline\":\"verb barred, object affirmed\",\"reader_payoff\":\"The reader notices that the prohibition creates a boundary around the addressee's agency while keeping the orphan visibly present as the protected case.\",\"reason\":\"Attachment evidence places the negator over the verb and identifies the second-person subject as the direct addressee, while the fronted noun remains the object.\",\"representative_source_ids\":[\"QG-40e1a67b\",\"QS-1c586055\",\"QS-9b9efe88\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:4:same-form-different-function","source_type":"word_analysis","support_id":"sup_0bfe24e1665839e41daf","text":"{\"blocking_evidence\":null,\"headline\":\"same particle form, new local function\",\"reader_payoff\":\"The reader notices that repeated particle shape is constructionally controlled: the first opens the consequence section, the second answers the case.\",\"reason\":\"The two particles share surface form, but QAC assigns the second a response role after {{ar:أَمَّا}} ({{tr:ammā}}).\",\"representative_source_ids\":[\"QS-35e8f996\",\"QE-15fb6e97\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:4:apodotic-answer-marker","source_type":"word_analysis","support_id":"sup_11d7b743546559ee3076","text":"{\"blocking_evidence\":null,\"headline\":\"required answer to the case frame\",\"reader_payoff\":\"The reader notices exactly where the ayah turns from the orphan-case to the binding answer.\",\"reason\":\"QAC identifies the particle as apodotic, and the attachment evidence confirms the {{ar:أَمَّا}} ({{tr:ammā}}) construction with the prohibition as the response.\",\"representative_source_ids\":[\"QG-669182a4\",\"QG-be2f9809\",\"MG-e5f9313a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:1:compact-section-pivot","source_type":"word_analysis","support_id":"sup_13f80d6ec4a8f0cc4f85","text":"{\"blocking_evidence\":null,\"headline\":\"compact launch into the case frame\",\"reader_payoff\":\"The reader notices the abrupt economy of the transition: a small bound particle carries the discourse from proof into command without a heavy preface.\",\"reason\":\"The particle is a short proclitic at the first position of the ayah, so the form supports the compact transition topic.\",\"representative_source_ids\":[\"QF-d581a4d4\",\"QT-734fce0b\",\"QT-d23096f6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:4","source_type":"word_analysis","support_id":"sup_14917672fb786322bfdf","text":"{\"gloss_range\":\"required apodotic response particle after the case frame, fused to the prohibition onset\",\"prose\":\"The second {{ar:فَ}} ({{tr:fa}}) is the answer-marker required by {{ar:أَمَّا}} ({{tr:ammā}}). It is therefore not a duplicate of the opening particle: it marks the point where the named case turns into its ruling. Because it is bound directly to {{ar:لَا}} ({{tr:lā}}), the response does not pause for explanation; it enters the prohibition in one clipped onset.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:2:ethical-scene-change","source_type":"word_analysis","support_id":"sup_198de5ca3a09dbfc565b","text":"{\"blocking_evidence\":null,\"headline\":\"new ethical scene opens\",\"reader_payoff\":\"The reader notices the shift from the addressee as recipient in 93:6-8 to the addressee as responsible actor in 93:9.\",\"reason\":\"The local construction begins the command unit, and attachment evidence identifies the following second-person verb as addressed to the singular addressee.\",\"representative_source_ids\":[\"QB-321ea45c\",\"QB-3c50b50e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:3:fronted-accusative-object","source_type":"word_analysis","support_id":"sup_1f2fa074b5303d788796","text":"{\"blocking_evidence\":null,\"headline\":\"fronted object remains governed\",\"reader_payoff\":\"The reader notices that the orphan is foregrounded first but still receives the full force of the later direct-object relation.\",\"reason\":\"Attachment evidence marks the noun as an explicit direct object of {{ar:تَقْهَرْ}} ({{tr:taqhar}}), fronted through the {{ar:أَمَّا}} ({{tr:ammā}}) construction.\",\"representative_source_ids\":[\"QG-ce37575e\",\"QG-d5811269\",\"MG-f48a4232\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:3:same-surah-orphan-echo","source_type":"word_analysis","support_id":"sup_21f0b20e262d064c9aeb","text":"{\"blocking_evidence\":null,\"headline\":\"93:6 orphanhood returns as responsibility\",\"reader_payoff\":\"The reader notices that the remembered orphanhood of the addressee in 93:6 returns in 93:9 as a rule for protecting others.\",\"reason\":\"The attachment translation support explicitly recommends the reading window linking the orphan term in 93:9 with the earlier orphan benefaction clause in 93:6.\",\"representative_source_ids\":[\"QI-d7d08083\",\"MI-9f6361da\",\"QE-3f2abd63\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:6:closure-and-delay","source_type":"word_analysis","support_id":"sup_2510a456f056a87b8ada","text":"{\"blocking_evidence\":null,\"headline\":\"delayed final verb lands as hard stop\",\"reader_payoff\":\"The reader notices that the protected party is heard first and the ayah ends abruptly on the barred act.\",\"reason\":\"The verb appears after its fronted object and is the final word of the ayah in jussive form.\",\"representative_source_ids\":[\"QT-5c64ad4a\",\"QT-ea2b2154\",\"QP-48dd1255\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:5:prohibitive-la-jussive","source_type":"word_analysis","support_id":"sup_3a7ef8f571c926f1a60e","text":"{\"blocking_evidence\":null,\"headline\":\"prohibitive particle governs jussive\",\"reader_payoff\":\"The reader notices that the wording is a binding prohibition, not ordinary negation or moral description.\",\"reason\":\"QAC and attachment evidence identify prohibitive {{ar:لَا}} ({{tr:lā}}) governing the jussive verb {{ar:تَقْهَرْ}} ({{tr:taqhar}}).\",\"representative_source_ids\":[\"QG-0fb2ca14\",\"QG-37e613d1\",\"MG-ce749ec3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:6:variant-and-sound-gradient","source_type":"word_analysis","support_id":"sup_4dc1d63ade62e6a886f9","text":"{\"blocking_evidence\":null,\"headline\":\"variant pressure broadens harshness gradient\",\"reader_payoff\":\"The reader notices that apparatus and sound pressure keep harsh rebuke near the semantic edge, while the canonical word still selects overpowering domination.\",\"reason\":\"The shawadhdh-style variant can be retained as contrast and sound-near pressure, but QAC alignment keeps canonical {{ar:تَقْهَرْ}} ({{tr:taqhar}}) as the governing surface.\",\"representative_source_ids\":[\"QE-e4d46028\",\"QP-26be065c\",\"QY-650293f7\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:3:patient-beneficiary-asymmetry","source_type":"word_analysis","support_id":"sup_62050278cf0bdd92d379","text":"{\"blocking_evidence\":null,\"headline\":\"potential patient becomes protected beneficiary\",\"reader_payoff\":\"The reader notices the ethical asymmetry: the one who could be directly overpowered is precisely the one the prohibition protects.\",\"reason\":\"The noun fills the direct object slot for the q-h-r verb, and the selected root fields create the local collision between exposed vulnerability and overpowering force.\",\"representative_source_ids\":[\"QS-04c6c8bf\",\"QS-64e86c76\",\"QE-77243828\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:1:benefaction-to-command-link","source_type":"word_analysis","support_id":"sup_642752aff0d424f03271","text":"{\"blocking_evidence\":null,\"headline\":\"prior benefaction becomes ethical consequence\",\"reader_payoff\":\"The reader notices that the command grows out of the divine benefaction sequence in 93:6-8 instead of beginning as an isolated instruction.\",\"reason\":\"QAC marks the opening particle as resumptive/connective, and the local clause begins the visible imperative section after the retrospective unit.\",\"representative_source_ids\":[\"QG-4db20fe0\",\"QG-5846da0d\",\"MG-e10a4d79\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:1:fa-reprise-sequence","source_type":"word_analysis","support_id":"sup_67537c9e8d15d9fa1b98","text":"{\"blocking_evidence\":null,\"headline\":\"repeated particle cadence frames the section\",\"reader_payoff\":\"The reader notices that repeated particle openings help organize the first command and anticipate the matched case-response pattern in 93:9-11.\",\"reason\":\"The local grammar confirms the {{ar:أَمَّا}} ({{tr:ammā}}) construction, and the row family ties the initial particle to the following response particle and the 93:9-11 sequence.\",\"representative_source_ids\":[\"MT-5e96bb04\",\"QP-487dc358\",\"QB-5cab2144\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:6:same-surah-role-reversal","source_type":"word_analysis","support_id":"sup_822ba18ff34a19849c39","text":"{\"blocking_evidence\":null,\"headline\":\"received care becomes restraint toward another\",\"reader_payoff\":\"The reader notices the role reversal: the one remembered as cared for in 93:6-8 is now addressed as the one who must not overpower another vulnerable person in 93:9.\",\"reason\":\"Attachment support explicitly links the orphan prohibition to the earlier 93:6 scene, and the local verb's second-person agreement makes the addressee the restrained agent.\",\"representative_source_ids\":[\"QE-36311cdf\",\"QB-17a4c5b5\",\"QB-c7499170\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:5:paired-prohibition-template","source_type":"word_analysis","support_id":"sup_84ed960268d00858aa79","text":"{\"blocking_evidence\":null,\"headline\":\"first negative member of 93:9-11\",\"reader_payoff\":\"The reader notices that this prohibition begins a forward pattern: matched restraints in 93:9 and 93:10 before positive proclamation in 93:11.\",\"reason\":\"The CRITICAL rows provide the concrete 93:9-11 sequence, and the local grammar supports the first negative-jussive member.\",\"representative_source_ids\":[\"QT-9bea436e\",\"MT-8ea9897e\",\"QE-da33517e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:5:vocal-delay-before-force-word","source_type":"word_analysis","support_id":"sup_88cede8403247877ae5f","text":"{\"blocking_evidence\":null,\"headline\":\"open negation before clipped force\",\"reader_payoff\":\"The reader notices an audible pause of negating force before the harder consonants of the barred verb arrive.\",\"reason\":\"The sound observation matches the visible sequence from the long open negator into the following q-h-r verb, without changing the grammatical scope.\",\"representative_source_ids\":[\"QP-696bd84e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:5:response-fused-to-negation","source_type":"word_analysis","support_id":"sup_8b59eb6562845c90ac8b","text":"{\"blocking_evidence\":null,\"headline\":\"answer marker enters prohibition directly\",\"reader_payoff\":\"The reader notices that the case-response structure lands immediately as direct restraint with no explanatory interval.\",\"reason\":\"The local sequence is the apodotic particle followed by prohibitive {{ar:لَا}} ({{tr:lā}}) and the governed verb, completing the second beat of the clause.\",\"representative_source_ids\":[\"QI-a7f05966\",\"QT-3459524e\",\"QT-c40e5a38\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:3","source_type":"word_analysis","support_id":"sup_8c2615d7eb63cbb41c95","text":"{\"gloss_range\":\"the definite singular orphan as a protected class representative and fronted direct object; the local sense is bereft-of-protector vulnerability, with singularity or preciousness only as secondary pressure\",\"prose\":\"{{ar:ٱلْيَتِيمَ}} ({{tr:al-yatīma}}) is placed before the prohibited act, but it remains the direct object of {{ar:تَقْهَرْ}} ({{tr:taqhar}}). The definite singular makes one recognizable orphan carry the protected class, while the adjectival noun presents orphanhood as an identity-state to be recognized rather than an event being narrated. The root field selects loss of a protecting parent here; its isolation and peerless-preciousness pressure makes the object feel both exposed and irreplaceable, while the case and word order make the potential patient of overpowering become the beneficiary of the ban. In recitation, the joining onset and nasal texture bind {{ar:أَمَّا}} ({{tr:ammā}}) to {{ar:ٱلْيَتِيمَ}} ({{tr:al-yatīma}}) before the harsher q-h-r force-word arrives. The same root's return from 93:6 turns received care into commanded restraint in 93:9, and the lack-field from 93:8 carries into the first matched imperative of 93:9-11.\",\"root_display\":\"{{ar:ي ت م}} ({{tr:y-t-m}})\",\"root_gloss_range\":\"root range includes orphanhood through loss of the protecting parent, isolated or peerless singleness, and more remote shortcoming, delay, or marriage-related usages; the local ayah selects orphaned vulnerability while allowing isolation and preciousness pressure\",\"surface_display\":\"{{ar:ٱلْيَتِيمَ}} ({{tr:al-yatīma}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:6:qahr-overpowering-sense","source_type":"word_analysis","support_id":"sup_94be4026120e26eacf13","text":"{\"blocking_evidence\":null,\"headline\":\"overpowering, compulsion, and humiliation selected\",\"reader_payoff\":\"The reader notices that the ban names domination that subdues, compels, or humiliates, not only abstract wrongdoing.\",\"reason\":\"V4 accepts the overpowering-from-above branch for {{ar:ق ه ر}} ({{tr:q-h-r}}), and the local direct-object frame with the orphan selects that branch while excluding unrelated food, stone, retreat, and named-creature branches.\",\"representative_source_ids\":[\"QS-3153ef7d\",\"QS-38721eb6\",\"QS-52507b38\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:6:fronted-object-valency","source_type":"word_analysis","support_id":"sup_9f567ff64195c72fdb48","text":"{\"blocking_evidence\":null,\"headline\":\"object gap supplied by fronting\",\"reader_payoff\":\"The reader notices that the verb's patient has already been named, so the harm is construed as direct pressure on the orphan rather than vague harshness.\",\"reason\":\"Attachment and valency evidence mark the fronted noun as the explicit object of the transitive verb.\",\"representative_source_ids\":[\"QG-cd6eeaec\",\"QG-d35b7ee7\",\"MG-2ab2f843\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:6:paired-prohibition-projection","source_type":"word_analysis","support_id":"sup_a035b731e74f490f5f51","text":"{\"blocking_evidence\":null,\"headline\":\"current verb anticipates the next prohibition\",\"reader_payoff\":\"The reader notices that this barred act begins a gradient that continues with the paired prohibition in 93:10.\",\"reason\":\"The row gives the concrete 93:10 continuation, and the local verb has the same negative-jussive architecture as the next paired command.\",\"representative_source_ids\":[\"QB-3f5c4ed6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:5","source_type":"word_analysis","support_id":"sup_a4fc5671717c2eec8ab2","text":"{\"gloss_range\":\"prohibitive negation governing the following jussive verb; it bars the act of overpowering while leaving the fronted orphan affirmed as the case\",\"prose\":\"{{ar:لَا}} ({{tr:lā}}) is prohibitive here, not a report that something happens not to occur. It governs {{ar:تَقْهَرْ}} ({{tr:taqhar}}) into jussive force, so the grammar itself bars the addressee's possible act. Its scope falls on the verb, not on {{ar:ٱلْيَتِيمَ}} ({{tr:al-yatīma}}): the orphan remains the affirmed case, and only overpowering is excluded. As the first negative member of the 93:9-11 command sequence, this particle begins the paired restraint of 93:9 and 93:10 before the positive proclamation of 93:11. Its long open vowel also lets the negating force sound before the harder q-h-r closure of the barred verb.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَا}} ({{tr:lā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:6:form-i-low-threshold","source_type":"word_analysis","support_id":"sup_af8fd6c440831a56577d","text":"{\"blocking_evidence\":null,\"headline\":\"simple Form I lowers the threshold\",\"reader_payoff\":\"The reader notices that the prohibition does not wait for intensified crushing; the simple act of qahr itself is barred.\",\"reason\":\"QAC identifies the local verb as Form I, so the contrast with intensified or nominal forms is kept as form-specific payoff rather than as a replacement parse.\",\"representative_source_ids\":[\"QF-43ccda98\",\"QF-e1f1a7c9\",\"MF-4330f6d6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:2","source_type":"word_analysis","support_id":"sup_b8ed947c657083a987f9","text":"{\"gloss_range\":\"conditional-distributive case marker that sets the orphan before the response and requires a later apodotic particle\",\"prose\":\"{{ar:أَمَّا}} ({{tr:ammā}}) turns the orphan into a named case before the ruling is delivered. Its constructional force requires the later {{ar:فَ}} ({{tr:fa}}), so the ayah is heard as case and answer: as for {{ar:ٱلْيَتِيمَ}} ({{tr:al-yatīma}}), then the prohibition follows. That same case-frame also starts the ordered ethical sequence of 93:9-11, where the orphan, requester, and blessing cases answer the remembered sheltering, guidance, and enrichment of 93:6-8.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:أَمَّا}} ({{tr:ammā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:3:boundary-lack-sequence","source_type":"word_analysis","support_id":"sup_bba903f1ab329b4e2ae1","text":"{\"blocking_evidence\":null,\"headline\":\"lack field enters the command unit\",\"reader_payoff\":\"The reader notices that the new command continues the vulnerability field from 93:8 and begins the ordered imperative sequence of 93:9-11.\",\"reason\":\"The row family supplies concrete references to 93:8 and 93:9-11, and the local noun is the first protected case in the sequence.\",\"representative_source_ids\":[\"QB-3dfd59f5\",\"QY-43b72123\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:3:audible-topic-binding","source_type":"word_analysis","support_id":"sup_c011651d6230d8775c9d","text":"{\"blocking_evidence\":null,\"headline\":\"sound binds frame to topic before force arrives\",\"reader_payoff\":\"The reader notices that the softer linkage of the case frame and noun precedes the harsher force-word, making the protected topic arrive before the pressure of the ban.\",\"reason\":\"The sound rows cohere with the visible sequence from {{ar:أَمَّا}} ({{tr:ammā}}) into the noun and then into the later q-h-r verb, without overriding grammar.\",\"representative_source_ids\":[\"QP-49799b71\",\"QP-d61535c6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:2:threefold-distributive-sequence","source_type":"word_analysis","support_id":"sup_c493c448056b9120198b","text":"{\"blocking_evidence\":null,\"headline\":\"first member of the 93:9-11 distribution\",\"reader_payoff\":\"The reader notices that this is the first case in an ordered ethical sequence that mirrors the remembered benefactions of 93:6-8.\",\"reason\":\"The construction is locally present in 93:9 and the CRITICAL rows give the concrete 93:9-11 sequence, so the distributive pattern can be preserved without making it control the local parse.\",\"representative_source_ids\":[\"QT-cfc86f11\",\"MT-a3ef7550\",\"QE-afc72668\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:6:divine-human-boundary","source_type":"word_analysis","support_id":"sup_c5a61d1a937c1684ae17","text":"{\"blocking_evidence\":null,\"headline\":\"divine overpowering field barred as human act\",\"reader_payoff\":\"The reader notices a distributional contrast: a root field associated with divine overpowering (6:18; 6:61) is used as a human finite act only to be prohibited toward the orphan.\",\"reason\":\"The contextual data shows this local finite Form I verb as low-occurrence, while the CRITICAL rows supply concrete divine-name contrasts including 6:18 and 6:61; the topic is preserved as distributional pressure, not as a claim that divine titles govern the local morphology.\",\"representative_source_ids\":[\"QS-21d7abdd\",\"MS-2eb126b8\",\"MI-812645cb\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:6","source_type":"word_analysis","support_id":"sup_c8c7021157eb90e4ed9c","text":"{\"gloss_range\":\"jussive second-person Form I prohibition against overpowering, subduing, humiliating, or harshly imposing force on the fronted orphan object\",\"prose\":\"{{ar:تَقْهَرْ}} ({{tr:taqhar}}) closes the ayah on the act that must be withheld. It is a second-person jussive Form I verb under {{ar:لَا}} ({{tr:lā}}), so the form regulates possible future conduct by the addressee rather than reporting a past event. Its object is not missing: {{ar:ٱلْيَتِيمَ}} ({{tr:al-yatīma}}) has been fronted, making the vulnerable patient visible before the force-word lands. The selected {{ar:ق ه ر}} ({{tr:q-h-r}}) branch is concrete overpowering, subduing, compelling, and humiliating; the direct-object frame makes that force bear immediately on one without protection. Because the supplied occurrence pressure is dominated by divine overpowering language (6:18; 6:61), the human finite verb becomes especially sharp: what belongs to divine power is here barred as human conduct toward the orphan. The simple Form I threshold and clipped final position keep the ban broad and hard: do not exercise even ordinary qahr against this vulnerable person. The sound-near q-to-k variant keeps rough rebuke near the semantic edge without replacing the canonical overpowering sense, and the verb points forward to the paired restraint of 93:10, where the sequence moves from overpowering the orphan toward rebuking the requester.\",\"root_display\":\"{{ar:ق ه ر}} ({{tr:q-h-r}})\",\"root_gloss_range\":\"root range includes overpowering from above, subduing, compelling, humiliation, and unrelated lexical branches such as cooking, stones, backward retreat, packed food, and a named creature; the local ayah selects the overpowering and humbling branch under prohibition\",\"surface_display\":\"{{ar:تَقْهَرْ}} ({{tr:taqhar}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:4:compressed-prohibition-onset","source_type":"word_analysis","support_id":"sup_d7096ef67b639003a71a","text":"{\"blocking_evidence\":null,\"headline\":\"response fused to the ban\",\"reader_payoff\":\"The reader notices the ruling tighten immediately from response marker into prohibitive negation.\",\"reason\":\"The particle is followed directly by the prohibitive negator that governs the jussive verb, creating the compact {{ar:فَلَا}} ({{tr:fa-lā}}) onset.\",\"representative_source_ids\":[\"QF-5cd54b0b\",\"QT-01a1c171\",\"QP-840145fc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"93:9:4:1","source_type":"qac_morpheme","support_id":"sup_dba39ec5e81e97ac1eba","text":"{\"lemma_ar\":\"تَقْهَرْ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:taqoharo|ROOT:qhr|2MS|MOOD:JUS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"93:9:4:1\",\"qac_word_ref\":\"93:9:4\",\"root_ar\":\"ق ه ر\",\"surface_ar\":\"تَقْهَرْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:3:vulnerability-and-singularity-pressure","source_type":"word_analysis","support_id":"sup_def70ab39e4e810f5193","text":"{\"blocking_evidence\":null,\"headline\":\"orphanhood with isolation and preciousness pressure\",\"reader_payoff\":\"The reader notices that the local orphan sense is sharpened by exposure from lost protection and, secondarily, by singular preciousness rather than pity alone.\",\"reason\":\"V4 supports orphanhood and isolated uniqueness as distinct branches, while the local object of the prohibition selects bereft-of-protector vulnerability as the operative sense and keeps preciousness as narrowed pressure.\",\"representative_source_ids\":[\"QS-05f51f5e\",\"QS-a88691d1\",\"MS-adb00438\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:6:finite-verb-shift","source_type":"word_analysis","support_id":"sup_df3276a28c02674c111c","text":"{\"blocking_evidence\":null,\"headline\":\"narrative recipient becomes restrained actor\",\"reader_payoff\":\"The reader notices the register shift from what God did for the addressee in 93:6-8 to what the addressee must not do in 93:9.\",\"reason\":\"The local form is a second-person finite verb, and the surrounding ayah movement shifts from retrospective divine action to direct command.\",\"representative_source_ids\":[\"QF-65ba456c\",\"QI-b54b4f77\",\"QB-ab5cad55\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:6:convergent-form-root-distribution","source_type":"word_analysis","support_id":"sup_e5ede81a288d22296c6a","text":"{\"blocking_evidence\":null,\"headline\":\"root sense, form, and rarity converge\",\"reader_payoff\":\"The reader notices the combined effect: simple jussive form, final placement, and rare human q-h-r usage all sharpen the prohibition.\",\"reason\":\"The contextual profile marks the exact root-form as a single negated occurrence, and QAC confirms the simple jussive final verb.\",\"representative_source_ids\":[\"QH-5b5b9047\",\"QY-748fae20\",\"QY-eda6cc6f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:2:case-response-frame","source_type":"word_analysis","support_id":"sup_ec0b2657999b36c17caf","text":"{\"blocking_evidence\":null,\"headline\":\"case frame requires a response\",\"reader_payoff\":\"The reader notices that the orphan is not merely appended to the verb; the construction first isolates the case and then demands a formal answer.\",\"reason\":\"QAC and attachment identify an {{ar:أَمَّا}} ({{tr:ammā}}) construction whose visible predicate is the later prohibition, with the response introduced by the required apodotic particle.\",\"representative_source_ids\":[\"QG-128d5a40\",\"QG-4d8123c5\",\"MG-37728e23\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:6:response-clause-completion","source_type":"word_analysis","support_id":"sup_f052f6fda42d0b002c5f","text":"{\"blocking_evidence\":null,\"headline\":\"verbal core completes the apodosis\",\"reader_payoff\":\"The reader notices that the verb supplies the actionable core of the case-response structure.\",\"reason\":\"Attachment evidence identifies the whole ayah as an {{ar:أَمَّا}} ({{tr:ammā}}) construction whose visible predicate is the prohibition headed by this verb.\",\"representative_source_ids\":[\"QI-42c6d163\",\"QT-b09dc534\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:1","source_type":"word_analysis","support_id":"sup_f48cc1503e24125394ff","text":"{\"gloss_range\":\"resumptive and consequential opening particle that links the remembered benefactions of 93:6-8 to the ethical commands of 93:9-11\",\"prose\":\"{{ar:فَ}} ({{tr:fa}}) makes the ayah begin as consequence, not as a detached rule. It carries the remembered sheltering, guidance, and enrichment of 93:6-8 into the first ethical response, then attaches tightly to {{ar:أَمَّا}} ({{tr:ammā}}) so the shift from narrative evidence to command feels immediate. This first {{ar:فَ}} ({{tr:fa}}) plus {{ar:أَمَّا}} ({{tr:ammā}}) opening also belongs to the three-case pattern of orphan, requester, and blessing in 93:9-11. The repeated particle sound later in {{ar:فَلَا}} ({{tr:fa-lā}}) lets the listener hear a two-step structure: first the section opens, then the prohibition answers the named case.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:6:jussive-second-person-prohibition","source_type":"word_analysis","support_id":"sup_f8d562379e170ffa80a1","text":"{\"blocking_evidence\":null,\"headline\":\"jussive address regulates possible conduct\",\"reader_payoff\":\"The reader notices that the verb directly restrains the addressee's possible future agency rather than describing an event.\",\"reason\":\"QAC and attachment identify the verb as second-person masculine singular, jussive under prohibitive {{ar:لَا}} ({{tr:lā}}), with an implicit addressed subject.\",\"representative_source_ids\":[\"QG-3473e0b7\",\"QG-88731a7c\",\"MG-5caa7cd4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:9:3:definite-substantive-status","source_type":"word_analysis","support_id":"sup_ff897d2c72225f976fb7","text":"{\"blocking_evidence\":null,\"headline\":\"definite singular status-name\",\"reader_payoff\":\"The reader notices that the wording treats orphanhood as a recognizable protected status, not as an incidental modifier or anonymous example.\",\"reason\":\"QAC identifies a definite accusative adjective functioning substantively, and the contextual profile confirms a recurring adjectival noun pattern for this root.\",\"representative_source_ids\":[\"QG-b2446cd1\",\"QG-c9780ee4\",\"QF-0be59850\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ","ayah_ref":"93:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001266/B001","root_001692/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001692","role":"Cut-off offspring supplies the missing-protector condition that exposes the orphan to another's unchecked power.","root":"ي ت م","source_ref":"93:9","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001266","role":"Overpowering from above supplies the prohibited operation: making vulnerability answer to force, humiliation, or nonconsensual taking.","root":"ق ه ر","source_ref":"93:9","source_word_indices":["4"]}],"changed_reading":{"after":"Do not turn the orphan's missing protection into a license for vertical power; the very asymmetry that enables coercion intensifies the duty of restraint.","before":"Do not mistreat an orphan."},"confidence":"strong","focus_anchor":"ٱلْيَتِيمَ at word 2 names one cut off from a protecting parent, while تَقْهَرْ at word 4 names superior power used to subdue.","mechanism":"Loss of the ordinary protector creates an asymmetry in which coercion is unusually easy. The prohibition blocks the conversion of that protection gap into permission to compel, humiliate, or take without consent.","model_id":"b_protection_gap_not_power_license"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_protection_gap_not_power_license","source_type":"hft","support_id":"sup_c5e1860a46c73db2e482","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ","ayah_ref":"93:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001266/B001","root_001692/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001692","role":"Isolated or peerless singleness supplies the social exposure of one who stands without an equivalent beside them.","root":"ي ت م","source_ref":"93:9","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001266","role":"Subduing from above turns horizontal aloneness into an imposed vertical inferiority, the move the prohibition interrupts.","root":"ق ه ر","source_ref":"93:9","source_word_indices":["4"]}],"changed_reading":{"after":"It also exposes a mechanism: never convert someone's aloneness or lack of peers into evidence that they may be made socially lower.","before":"The verse protects a fixed legal-social class called the orphan."},"confidence":"medium","focus_anchor":"The focus noun can image isolated singleness as well as bereavement, and the prohibited verb images downward subjugation.","mechanism":"Social isolation removes peers and witnesses. The command therefore resists a second injury in which being alone is interpreted as being lower, disposable, or available for domination.","model_id":"b_solitude_not_social_lowliness"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_solitude_not_social_lowliness","source_type":"hft","support_id":"sup_1d706927f2fd98049969","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ","ayah_ref":"93:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001266/B001","root_001692/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001692","role":"Delayed motion or delayed kindness makes lateness of care an internal feature of the orphan's exposure.","root":"ي ت م","source_ref":"93:9","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001266","role":"Superior coercive power supplies the function of strategic delay: maintaining dependence until the weaker party yields.","root":"ق ه ر","source_ref":"93:9","source_word_indices":["4"]}],"changed_reading":{"after":"Do not dominate quietly by postponing needed care and making the orphan wait beneath another's controlling discretion.","before":"Do not actively overpower the orphan."},"confidence":"medium","focus_anchor":"A focus branch of ي ت م links orphanhood with kindness arriving slowly, while ق ه ر supplies control from above.","mechanism":"Domination need not be an overt blow. A guardian can preserve leverage by delaying care that the dependent cannot obtain elsewhere; withholding then performs qahr through time.","model_id":"b_withheld_care_as_quiet_qahr"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_withheld_care_as_quiet_qahr","source_type":"hft","support_id":"sup_15df0278960ea7dac528","trust":"legacy_unbound"}]}
</lane_packet_json>
