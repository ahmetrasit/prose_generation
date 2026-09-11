# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **112:4**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s112-regular-20260911/s112/112_4/micro.discovery.json` and modify nothing
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
  "ayah_ref": "112:4",
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
{"analysis_context":{"analysis_id":"s112-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"112:4","host_surah":112,"lane_context_refs":[],"ordered_context_refs":["112:0","112:1","112:2","112:3","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Bu dal tekliği ve eşsizliği anlatır; olumsuzlukta kişi kapsamını, onlu sayı kuruluşlarını, gün adını ve dağ adını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000017/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:4:5:1","qac_word_ref":"112:4:5","surface_ar":"أَحَدٌۢ"}],"gloss":"tek ve eşi olmayan olma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığı bir tane, tek veya eşi bulunmayan olarak gösterir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Mutlak niteleme olarak kullanıldığında Tanrı'nın ortağı ve benzeri bulunmadığını bildirir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı sözün art arda yinelenmesi tek olma bildirimini pekiştirir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kaynak ifadesi sözcüğü saymanın başlangıcındaki bir sayısıyla da ilişkilendirir; düzenli sayı kuruluşları ayrı dalda ele alınır."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tek olma çekirdeğini, mutlak eşsizliği ve yinelemeli pekiştirmeyi birlikte temsil eden dal düzeyi karşılıktır.","boundary_detail":"Bu dal tekliği ve eşsizliği anlatır; olumsuzlukta kişi kapsamını, onlu sayı kuruluşlarını, gün adını ve dağ adını kapsamaz.","branch_image_ar":"الأَحَدِيَّة والوَحْدَة","concept_gloss":"tek ve eşi olmayan olma","contextual_glosses":[{"applicability":"Sayılabilir bir varlığın tek örnek olduğunu bildiren genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Mutlak eşsizlik ile yinelemeli pekiştirme yüzlerini taşımaz.","preserves":"Bir tane olma çekirdeğini korur."},"facet_ids":["F001","F004"],"text":"bir tane","usage_role":"contextual"},{"applicability":"Tanrı'nın ortağı ve benzeri olmadığını bildiren mutlak niteleme bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel sayısal birliği ve yinelemeli söyleyiş biçimini kapsamaz.","preserves":"Mutlak tekliği ve eşsizliği korur."},"facet_ids":["F002"],"text":"tek ve eşsiz","usage_role":"contextual"},{"applicability":"Teklik bildiren sözün yinelenerek güçlü biçimde vurgulandığı söyleyiş için açıklayıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yinelenmeyen genel kullanımın bütün kapsamını taşımaz.","preserves":"Yineleme yoluyla yapılan tek olma vurgusunu korur."},"facet_ids":["F003"],"text":"yalnız bir, yalnız bir","usage_role":"explanatory"}],"definition":"Bir varlığın bir tane, tek ya da eşi olmayan olmasıdır; mutlak kullanımda Tanrı'nın ortağı ve benzeri bulunmadığını bildirir. Sözcüğün yinelenmesi bu tekliği güçlü biçimde vurgular.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığı bir tane, tek veya eşi bulunmayan olarak gösterir."},{"facet_id":"F002","role":"specialization","statement":"Mutlak niteleme olarak kullanıldığında Tanrı'nın ortağı ve benzeri bulunmadığını bildirir."},{"facet_id":"F003","role":"associated_use","statement":"Aynı sözün art arda yinelenmesi tek olma bildirimini pekiştirir."},{"facet_id":"F004","role":"source_variant","statement":"Kaynak ifadesi sözcüğü saymanın başlangıcındaki bir sayısıyla da ilişkilendirir; düzenli sayı kuruluşları ayrı dalda ele alınır."}],"identity_rationale":"Kaynak ifadesi tek olma, mutlak biçimde eşsiz sayılma ve yinelemeyle bu niteliği pekiştirme çekirdeğini destekler. Aynı ifade saymanın ilk basamağına da değindiği için dal korunabilir, ancak düzenli sayı kurma kullanımları ayrı sayı dalına bırakılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir tane; tek ve eşsiz"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yalnız bir, yalnız bir"}],"lexicalization_note":"Tanım yalın biçimdeki tek olma anlamını ve yinelemeli pekiştirmeyi ayrı yüzler olarak tutar; yinelemeyi yalın biçimin zorunlu anlamı yapmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en güçlü sınırlar mutlak birlik, alana bağlı eşsizlik, sayısal bir ve tek başına kalma dallarıyla kuruldu, kalanlar yalnız uzak konu ortaklığı taşıdığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal yalnız Tanrı'nın birliği çevresinde kuruludur; odak dal ise genel tek olmayı ve yinelemeli vurguyu da taşıdığı için bütünüyle onun yerine geçmez.","focus_only":"Odak dal genel tekliği, sayı başlangıcına değen kullanımı ve yinelemeli pekiştirmeyi de içerir.","gloss":"Tanrı'nın ortak ve benzerden uzak tekliği","neighbor_only":"Komşu dal Tanrı'nın birliği inancını, ortak bulunmamasını ve bölünmezliği daha geniş bir inanç alanı olarak işler.","neighbor_ref":"root_001631/B004","relation_type":"near_synonym","shared_zone":"İki dal da Tanrı için mutlak tekliği ve ortak bulunmamasını bildirir."},{"boundary_match":"partial","distinction":"Odak dalın tekliği varlığın bir tane veya mutlak eşsiz olmasıdır; komşu dalın eşsizliği ise belirli bir nitelik alanındaki karşılaştırmaya bağlıdır.","focus_only":"Odak dal sayısal birlik ve mutlak tek olma bildirebilir.","gloss":"belirli bir alanda benzeri bulunmayan","neighbor_only":"Komşu dal belirli bir üstünlük ya da kötülük alanında benzeri bulunmayan kişiyi anlatır.","neighbor_ref":"root_001240/B018","relation_type":"near_synonym","shared_zone":"İki dal da eş ya da benzer bulunmaması düşüncesinde buluşur."},{"boundary_match":"partial","distinction":"Odak dal nitelik olarak tekliği merkez alır; komşu dal ise birin sayı dizisindeki ve birleşik sayılardaki görevini merkez alır.","focus_only":"Odak dal varlığın tek ve eşi olmayan oluşunu, ayrıca bu niteliğin vurgulanmasını anlatır.","gloss":"bir sayısı ve onlu sayı kuruluşları","neighbor_only":"Komşu dal sayma dizisini, onlu sayı kuruluşlarını ve bir kümeyi on bire çıkarma işlemini kapsar.","neighbor_ref":"root_000017/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir tane olma düşüncesi ve sayının ilk basamağıyla bağ vardır."},{"boundary_match":"partial","distinction":"Odak dal bir nitelik bildirirken komşu dal tek başına kalma ya da ayrı ayrı hareket etme sürecini ve sonucunu bildirir.","focus_only":"Odak dal bir varlığın tek ya da eşsiz olma niteliğini bildirir.","gloss":"tek başına kalma ve birer birer dağılma","neighbor_only":"Komşu dal kişinin tek başına kalması veya bir topluluğun birer birer gelmesi gibi değişme ve dağılım olaylarını bildirir.","neighbor_ref":"root_000017/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da birlikten veya topluluktan ayrı tek olma görünümüne dokunur."}],"source_phrase_ar":"أحد فرع والأصل الواو وحد (maqayis); أحد بمعنى الواحد وهو أول العدد (sihah); قل هو الله أحد (sihah;mufradat); يستعمل مطلقا وصفا في وصف الله تعالى وأصله وحد (mufradat); أحد أحد (sihah)","source_summary":"Kaynakların ortak çizgisi tek olma düşüncesidir. Bu çizgi genel olarak bir tane olmayı, Tanrı için mutlak eşsizliği ve yineleme yoluyla yapılan güçlü vurguyu bir araya getirir; sayı başlangıcına ilişkin kayıt ise komşu sayı dalıyla sınır oluşturur.","sources":["MQ","SI","MU"],"what_is_ar":"أحد بمعنى الواحد، والوصف المطلق بأحد، وتكرار أحد أحد للتأكيد","what_is_not_ar":"ليس نفي الجنس ولا أحد عشر ولا يوم الأحد ولا جبل أُحُد"},"support_links":[]},{"boundary":"Bu dal yalnız olumsuz bağlamdaki kişi kapsamıdır; olumlu tekliği, sayı kuruluşlarını, gün adını ve dağ adını içermez.","branch_kind":"bare","branch_ref":"root_000017/B002","candidate_links":[{"candidate_id":"cand_acbf995d107174207efd","lane":"micro"},{"candidate_id":"cand_2dadd5d457a2a8844e4e","lane":"micro"},{"candidate_id":"cand_3143897e5b81be86df74","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:4:5:1","qac_word_ref":"112:4:5","surface_ar":"أَحَدٌۢ"}],"gloss":"hiç kimse","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Olumsuzluk altında konuşmaya konu olabilecek kişiler türünün tamamını kapsar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin yanı sıra iki veya daha çok kişinin varlığını ya da katılımını da dışlar."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir yerde hiç kimsenin bulunmadığını veya bir eylemi hiç kimsenin yapmadığını söyleyen cümlelerde gerçekleşir."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Olumsuzluk altında kişi türünün tamamını, sayı ayrımı yapmadan dışlayan doğal dal karşılığıdır.","boundary_detail":"Bu dal yalnız olumsuz bağlamdaki kişi kapsamıdır; olumlu tekliği, sayı kuruluşlarını, gün adını ve dağ adını içermez.","branch_image_ar":"استغراق النفي","concept_gloss":"hiç kimse","contextual_glosses":[{"applicability":"Bir yerde kişi bulunmadığını bildiren varlık cümlelerinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir eyleme katılmama gibi yer bildirmeyen olumsuz bağlamları kapsamaz.","preserves":"Kişilerin tümünü olumsuzluk altında dışlama kapsamını korur."},"facet_ids":["F001","F002","F003"],"text":"hiç kimse yok","usage_role":"contextual"},{"applicability":"Belirli bir insan topluluğunun hiçbir üyesinin eyleme katılmadığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Belirsiz bir yerde insan bulunmaması gibi topluluğu belirtilmeyen bağlamları kapsamaz.","preserves":"Belirli bir topluluğun bütün üyelerini olumsuzluk kapsamına alır."},"facet_ids":["F001","F002"],"text":"aranızdan hiç kimse","usage_role":"contextual"}],"definition":"Olumsuz bir cümlede, söz konusu olabilecek kişilerden bir tekinin bile bulunmadığını ya da eyleme katılmadığını bildirir. Kapsam yalnız bir kişiyi değil, iki ve daha çok kişiyi de dışarıda bırakır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Olumsuzluk altında konuşmaya konu olabilecek kişiler türünün tamamını kapsar."},{"facet_id":"F002","role":"specialization","statement":"Bir kişinin yanı sıra iki veya daha çok kişinin varlığını ya da katılımını da dışlar."},{"facet_id":"F003","role":"example","statement":"Bir yerde hiç kimsenin bulunmadığını veya bir eylemi hiç kimsenin yapmadığını söyleyen cümlelerde gerçekleşir."}],"identity_rationale":"Kaynak ifadesi, sözcüğün olumsuzluk içinde konuşmaya konu olabilecek kişilerin bütün türünü kapsadığını ve yalnız tek kişiyi değil iki ya da daha çok kişiyi de dışladığını açıkça belirtir. Hazırlanan dal çerçevesi bu kapsamı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"olumsuzlukta hiç kimse"}],"lexicalization_note":"Tanım yalın birimin olumsuz cümledeki kapsamına bağlıdır ve başka bir söz öbeğine özgü anlamı bu dala taşımaz.","neighbor_coverage_note":"Adayların tümü gözden geçirildi; yer boşluğunu bildiren kalıplar, daha geniş yokluk kalıbı ve olumlu teklik dalı okur açısından en yararlı karşıtlıkları verdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişi türünü olumsuzlukla kapsayan genel birimdir; komşu dal ise belirli kalıplaşmış sözlerle yerin boşluğunu, bazen de iz yokluğunu anlatır.","focus_only":"Odak dal olumsuzluk altında kişi türünün tamamını düzenli bir dil bilgisel kapsamla dışlar.","gloss":"bir yerde kimse ya da iz bulunmaması","neighbor_only":"Komşu dal, bir yerde insanın ya da kimi kullanımlarda herhangi bir izin bulunmadığını bildiren kalıplaşmış sözleri kapsar.","neighbor_ref":"root_000075/B008","relation_type":"near_neighbor","shared_zone":"İki dal da bir yerde kişinin bulunmadığını söyleyebilir."},{"boundary_match":"partial","distinction":"Odak dalın alanı kişilerdir; komşu dalın kalıplaşmış kullanımı kişi dışındaki şeylere ve suya kadar genişleyebilir.","focus_only":"Odak dal yalnız konuşmaya konu olabilecek kişilerin tümünü dışlar.","gloss":"en küçük kişi ya da şeyin bile yokluğu","neighbor_only":"Komşu dal kalıplaşmış bir sözle kişi, herhangi bir şey veya su gibi farklı varlıkların en küçüğünü bile dışlayabilir.","neighbor_ref":"root_000187/B005","relation_type":"near_neighbor","shared_zone":"İki dal da olumsuzlukta en küçük bir örneğin bile bulunmadığını bildirebilir."},{"boundary_match":"partial","distinction":"Odak dalın anlamı olumsuzluk ve bütün kişileri kapsama koşuluna bağlıdır; komşu dal olumlu tekliği veya eşsizliği anlatır.","focus_only":"Odak dal olumsuzluk altında herhangi bir kişinin varlığını ya da katılımını dışlar.","gloss":"bir tane, tek ve eşsiz","neighbor_only":"Komşu dal olumlu biçimde bir tane, tek veya eşi olmayan olmayı bildirir.","neighbor_ref":"root_000017/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalın biçiminde bir kişiye ya da varlığa ilişkin birlik düşüncesi bulunur."}],"source_phrase_ar":"لا أحد في الدار؛ ما في الدار أحد (sihah); أحد في النفي لاستغراق جنس الناطقين ولا واحد ولا اثنان فصاعدا (mufradat); فما منكم من أحد عنه حاجزين (sihah;mufradat)","source_summary":"Kaynaklar olumsuzluk içindeki kullanımın kişi türünü bütünüyle kapsadığı konusunda birleşir. Böylece söz yalnız tek bir kişinin yokluğunu değil, o türe giren herhangi bir sayıda kişinin bulunmamasını da bildirir.","sources":["SI","MU"],"what_is_ar":"أحد في سياق النفي لاستغراق جنس من يصلح أن يخاطب، فيشمل الواحد وما فوقه","what_is_not_ar":"ليس إثبات الواحد ولا العدد المركب ولا علم الجبل"},"support_links":["sup_8b63b4d4bf8d151a57c1","sup_8dab2f8db81abb1c6df8","sup_c22e2afcdd54078053f2"]},{"boundary":"Bu dal sayı ve sayı kurma alanındadır; olumsuz kişi kapsamını, mutlak eşsizliği, gün adını ve özel dağ adını içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_000017/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:4:5:1","qac_word_ref":"112:4:5","surface_ar":"أَحَدٌۢ"}],"gloss":"bir sayısı, onlu kuruluşları ve on bire çıkarma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sayma dizisinin başlangıcındaki bir sayısını bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir sayısı on veya yirmi gibi onluklarla birleşerek on bir ve yirmi bir türü sayıları kurar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Eylem biçimi, bir topluluğun sayısını on bire çıkarma işlemini bildirir."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın sayıyı, onluklarla kurulan sayı biçimlerini ve on bire çıkarma eylemini birlikte temsil eder.","boundary_detail":"Bu dal sayı ve sayı kurma alanındadır; olumsuz kişi kapsamını, mutlak eşsizliği, gün adını ve özel dağ adını içermez.","branch_image_ar":"الواحد في العد والتركيب","concept_gloss":"bir sayısı, onlu kuruluşları ve on bire çıkarma","contextual_glosses":[{"applicability":"Sayma dizisinin ilk sayısını yalın olarak bildiren bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Onluklarla kurulan sayıları ve on bire çıkarma eylemini kapsamaz.","preserves":"Bir sayısının sayma başlangıcındaki değerini korur."},"facet_ids":["F001"],"text":"bir","usage_role":"contextual"},{"applicability":"Bir sayısının on veya yirmiyle kurduğu birleşik ya da bağlı sayı örneklerinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalın bir sayısını ve bir topluluğu on bire çıkarma eylemini kapsamaz.","preserves":"Bir sayısının onluklarla birleşerek sayı kurmasını korur."},"facet_ids":["F002"],"text":"on bir ya da yirmi bir","usage_role":"contextual"},{"applicability":"Bir topluluğun sayısını on bire ulaştıran eylem biçiminin doğal karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalın sayıyı ve onluklarla kurulan sayı adlarını kapsamaz.","preserves":"Bir topluluğu on bire ulaştırma işlemini ve sonucunu korur."},"facet_ids":["F003"],"text":"on bire çıkarmak","usage_role":"contextual"}],"definition":"Saymanın başlangıcındaki bir sayısını, bu sayının on ve yirmi gibi onluklarla birleşerek kurduğu sayıları ve bir topluluğu on bire çıkarma işlemini kapsar. Yalın sayı, birleşik sayı ve yapma eylemi birbirinden ayrı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sayma dizisinin başlangıcındaki bir sayısını bildirir."},{"facet_id":"F002","role":"extension","statement":"Bir sayısı on veya yirmi gibi onluklarla birleşerek on bir ve yirmi bir türü sayıları kurar."},{"facet_id":"F003","role":"associated_use","statement":"Eylem biçimi, bir topluluğun sayısını on bire çıkarma işlemini bildirir."}],"identity_rationale":"Kaynak ifadesi bir sayısını saymanın başlangıcı olarak, on ve yirmi gibi onluklarla kurulan sayılarda bir bileşen olarak ve bir kümeyi on bire çıkaran eylem biçiminde açıkça sunar. Dal çerçevesi bu üç kullanımı doğru biçimde ayırarak bir arada tutar.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"saymanın başlangıcındaki bir"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"on bir, on bir dişil biçimi ve yirmi bir"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"onları on bire çıkarmak"}],"lexicalization_note":"Tanım yalın bir sayısını, onluklarla kurulan söz öbeklerini ve on bire çıkarma biçimini ayrı yüzler olarak gösterir; söz öbeği anlamını yalın biçime yaymaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; onluklar, üç sayısı, teklik dalı ve üçe tamamlama dalı sayı alanının en açıklayıcı sınırlarını verdi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal kuruluş içindeki bir bileşenini ve on bire çıkarma eylemini izler; komşu dal ise onluk sayıların kendisini ve çevresindeki biçimleri izler.","focus_only":"Odak dal bir sayısını, onluklara eklenmesini ve on bire çıkarma işlemini merkez alır.","gloss":"on ve onluk sayılar","neighbor_only":"Komşu dal on, yirmi ve bunlara komşu onluk sayı sözlerini merkez alır.","neighbor_ref":"root_001016/B001","relation_type":"same_field","shared_zone":"İki dal on bir ve yirmi bir gibi sayı kuruluşlarında birlikte görünür."},{"boundary_match":"field_only","distinction":"Ortak alan sayı sistemidir, ancak merkez sayılar ve bunlardan kurulan biçimler farklıdır; birbirlerinin yerine kullanılamazlar.","focus_only":"Odak dal bir sayısını ve onun onluklarla kurduğu biçimleri kapsar.","gloss":"üç sayısı ve bağlı biçimleri","neighbor_only":"Komşu dal üç sayısını, onun sıra, dağıtma, yüzlük ve binlik gibi geniş türevlerini kapsar.","neighbor_ref":"root_000203/B001","relation_type":"same_field","shared_zone":"İki dal sayı adlarını ve bu adların düzenli kuruluşlarını işler."},{"boundary_match":"partial","distinction":"Odak dal sayı dizisi ve sayı kuruluşuyla sınırlıdır; komşu dal nitelik olarak tekliği ve eşsizliği merkez alır.","focus_only":"Odak dal sayma, onluklarla sayı kurma ve bir kümeyi on bire çıkarma görevlerini kapsar.","gloss":"tek ve eşi olmayan olma","neighbor_only":"Komşu dal tek ve eşi olmayan olmayı, mutlak nitelemeyi ve yinelemeli pekiştirmeyi kapsar.","neighbor_ref":"root_000017/B001","relation_type":"near_neighbor","shared_zone":"İki dal bir tane olma ve saymanın ilk basamağı çevresinde temas eder."},{"boundary_match":"partial","distinction":"Odak dalın merkez sayısı bir ve onlu kuruluşlarıdır; komşu dalın merkez sayısı beş, sıra değeri beşinci ve tamamlama sonucu beştir.","focus_only":"Odak dal bir sayısını, onun onluklarla kurduğu sayıları ve bir topluluğu on bire çıkarma işlemini bildirir.","gloss":"beş, beşinci ve beşe tamamlama","neighbor_only":"Komşu dal beş sayısını, beşinci olmayı, beş kişiden birini ve bir topluluğu beşe tamamlamayı bildirir.","neighbor_ref":"root_000439/B001","relation_type":"near_neighbor","shared_zone":"İki dal sayı adı, sıra içindeki yer ve bir topluluğu belirli sayıya ulaştırma alanlarında temas eder."}],"source_phrase_ar":"أحد واثنان وأحد عشر وإحدى عشرة (sihah); الواحد المضموم إلى العشرات نحو أحد عشر وأحد وعشرين (mufradat); فأحدهن أي صيرهن أحد عشر (sihah)","source_summary":"Kaynakların ortak kaydı bir sayısının hem sayma dizisindeki yalın yerini hem de onluklarla kurduğu sayıları gösterir. Aynı kanıt, ayrı bir eylem biçiminde bir kümeyi on bire çıkarma sonucunu da korur.","sources":["SI","MU"],"what_is_ar":"أحد في العد، وتركيبه مع العشرات، وتصْيير المعدود أحد عشر","what_is_not_ar":"ليس نفي الجنس ولا الأحدية المطلقة ولا يوم الأحد"},"support_links":[]},{"boundary":"Ad öbeğindeki seçme veya ilk olma kullanımı ile haftanın gün adı ayrı yüzlerdir; sayı kuruluşları ve dağ adı bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000017/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:4:5:1","qac_word_ref":"112:4:5","surface_ar":"أَحَدٌۢ"}],"gloss":"iki kişiden biri, ilk olan ve haftanın ilk günü","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir ad öbeği içinde iki kişiden birini ayırır veya bağlama göre ilk olanı gösterir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gün sözüyle kurulan söz öbeği haftanın ilk gününü ve o günün özel adını bildirir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kaynak ifadesi haftanın bu gününe verilen adın çoğul biçimini de kaydeder."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ad öbeğindeki seçme ya da ilk olma işlevini ve gün adıyla sınırlı takvim kullanımını birlikte temsil eder.","boundary_detail":"Ad öbeğindeki seçme veya ilk olma kullanımı ile haftanın gün adı ayrı yüzlerdir; sayı kuruluşları ve dağ adı bu dala girmez.","branch_image_ar":"الأول والإضافة","concept_gloss":"iki kişiden biri, ilk olan ve haftanın ilk günü","contextual_glosses":[{"applicability":"İki kişilik bir topluluktan herhangi bir üyeyi ad öbeği içinde ayıran bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sıra bakımından ilk olmayı, gün adını ve gün adının çoğulunu kapsamaz.","preserves":"İki kişiden birini seçme işlevini korur."},"facet_ids":["F001"],"text":"ikinizden biri","usage_role":"contextual"},{"applicability":"Haftanın ilk gününün Türkçedeki yerleşik adını gerektiren takvim bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İki kişiden birini ayırma işlevini ve çoğul gün adı biçimini kapsamaz.","preserves":"Haftanın ilk gününün özel gün adı olma işlevini korur."},"facet_ids":["F002"],"text":"Pazar günü","usage_role":"contextual"},{"applicability":"Gün adının çoğul ya da yinelenen günler anlamındaki kullanımını karşılar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir günü ve iki kişiden birini ayırma işlevini kapsamaz.","preserves":"Gün adının çoğul kullanımını korur."},"facet_ids":["F003"],"text":"Pazar günleri","usage_role":"contextual"}],"definition":"Bir ad öbeğinin parçası olduğunda iki kişiden birini seçer veya bağlama göre ilk olanı bildirir. Gün adıyla kurulan kullanımda haftanın ilk gününü ve bu günün özel adını, ayrıca gün adının çoğul biçimini kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir ad öbeği içinde iki kişiden birini ayırır veya bağlama göre ilk olanı gösterir."},{"facet_id":"F002","role":"specialization","statement":"Gün sözüyle kurulan söz öbeği haftanın ilk gününü ve o günün özel adını bildirir."},{"facet_id":"F003","role":"source_variant","statement":"Kaynak ifadesi haftanın bu gününe verilen adın çoğul biçimini de kaydeder."}],"identity_rationale":"Kaynak ifadesi bir ad öbeği içinde bir kişiyi ayıran ya da ilk olanı bildiren kullanımla haftanın ilk gününün adını birlikte verir ve gün adının çoğulunu da kaydeder. Hazırlanan çerçeve kullanılabilir, ancak iki kişiden birini seçme anlamı her bağlamda sıra bakımından ilk olmayı zorunlu kılmaz.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ikinizden biri"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"Pazar günü"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"Pazar günleri"}],"lexicalization_note":"Tanım ad öbeğine bağlı seçme kullanımını, gün adı söz öbeğini ve gün adının çoğul biçimini ayırır; bunları yalın kökün tek bir genel anlamına dönüştürmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ilk olma alanındaki komşu ile üç farklı gün adı ve sayı dalı, dalın hem sıra hem takvim sınırlarını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ilk olma yüzü belirli ad öbeklerine ve gün adına bağlıdır; komşu dal ise nesnelerin ön, üst ve başlangıç bölümlerine uzanan daha geniş bir öncelik alanıdır.","focus_only":"Odak dal ad öbeğinde iki kişiden birini ayırmayı ve haftanın ilk gününün adını da kapsar.","gloss":"ön, üst ve ilk bölüm","neighbor_only":"Komşu dal bir nesnenin önü, üstü ya da başlangıcı gibi uzamsal ve sıralı öncelikleri geniş biçimde kapsar.","neighbor_ref":"root_000849/B002","relation_type":"near_neighbor","shared_zone":"İki dal sıra bakımından ilk veya önde olanı gösterebilir."},{"boundary_match":"field_only","distinction":"Ortak alan haftanın günleridir, ancak gösterdikleri günler farklıdır ve gün adları birbirinin yerine geçmez.","focus_only":"Odak dal haftanın ilk gününün adını ve bu adın çoğulunu kapsar.","gloss":"Salı günü","neighbor_only":"Komşu dal Salı gününün adını ve onun tekil ile çoğul biçimlerini kapsar.","neighbor_ref":"root_000203/B006","relation_type":"same_field","shared_zone":"İki dal haftanın belirli bir gününe verilen adı ve adın sayı biçimlerini işler."},{"boundary_match":"field_only","distinction":"Odak dal ilk güne, komşu dal beşinci güne işaret eder; ortak takvim alanına karşın gösterdikleri gün ayrıdır.","focus_only":"Odak dal haftanın ilk gününü ve adını bildirir.","gloss":"Perşembe günü","neighbor_only":"Komşu dal haftanın beşinci gününün yerleşik adını bildirir.","neighbor_ref":"root_000439/B004","relation_type":"same_field","shared_zone":"İki dal haftanın gün adları dizgesine aittir."},{"boundary_match":"field_only","distinction":"Aynı takvim alanındadırlar, fakat haftanın farklı günlerini gösterirler ve odak dal ayrıca ad öbeğinde birini ayırma işlevi taşır.","focus_only":"Odak dal haftanın ilk gününü, adını ve çoğul biçimini kapsar.","gloss":"Çarşamba günü","neighbor_only":"Komşu dal Çarşamba gününün adını, söyleniş ayrıntısını ve çoğulunu kapsar.","neighbor_ref":"root_000536/B010","relation_type":"same_field","shared_zone":"İki dal bir hafta gününün adı ve çoğul kullanımı çevresinde buluşur."},{"boundary_match":"partial","distinction":"Odak dal seçme, sıra ve gün adı yapılarıyla sınırlıdır; komşu dal sayma ve sayı oluşturma işlemleriyle sınırlıdır.","focus_only":"Odak dal ad öbeğinde bir kişiyi ayırma ve haftanın ilk gününü adlandırma işlevlerini taşır.","gloss":"bir sayısı ve onlu sayı kuruluşları","neighbor_only":"Komşu dal bir sayısını, onluklarla sayı kurmayı ve bir topluluğu on bire çıkarmayı taşır.","neighbor_ref":"root_000017/B003","relation_type":"near_neighbor","shared_zone":"İki dal bir ve ilk düşüncelerinde temas eder."}],"source_phrase_ar":"أن يستعمل مضافا أو مضافا إليه بمعنى الأول (mufradat); أما أحدكما (mufradat); يوم الأحد أي يوم الأول (mufradat); يوم الأحد يجمع على آحاد (sihah)","source_summary":"Kaynakların birleşik kaydı, ad öbeği içindeki birini ayırma veya ilk sayma işlevini haftanın ilk gününün adıyla ilişkilendirir. Gün adının çoğul biçimi de aynı kanıt içinde korunur.","sources":["SI","MU"],"what_is_ar":"أحد مضافا أو مضافا إليه بمعنى الأول، واسم يوم الأحد","what_is_not_ar":"ليس أحد عشر ولا لا أحد ولا جبل أُحُد"},"support_links":[]},{"boundary":"Bu dal tek başına kalma ve ayrı ayrı hareket etme olaylarıdır; sayısal biri, olumsuz kişi kapsamını ve özel adları içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_000017/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:4:5:1","qac_word_ref":"112:4:5","surface_ar":"أَحَدٌۢ"}],"gloss":"tek başına kalma ve birer birer gelme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin bir işi başkalarından ayrı olarak üstlenmesini veya tek başına kalmasını bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir topluluğun üyelerinin toplu halde değil, ayrı ayrı ve birer birer gelmesini bildirir."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bireyin yalnızlaşmasını veya işi yalnız üstlenmesini ve topluluğun ayrı ayrı gelişini birlikte temsil eder.","boundary_detail":"Bu dal tek başına kalma ve ayrı ayrı hareket etme olaylarıdır; sayısal biri, olumsuz kişi kapsamını ve özel adları içermez.","branch_image_ar":"الانفراد والتفرق آحادا","concept_gloss":"tek başına kalma ve birer birer gelme","contextual_glosses":[{"applicability":"Bir kişinin başkalarından ayrılarak yalnız kalmasını bildiren bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir işi yalnız üstlenme ayrıntısını ve topluluğun birer birer gelişini kapsamaz.","preserves":"Bireyin başkalarından ayrı ve yalnız duruma gelmesini korur."},"facet_ids":["F001"],"text":"tek başına kalmak","usage_role":"contextual"},{"applicability":"Bir kişinin belirli bir işi başkalarının katılımı olmadan üstlendiği bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel tek başına kalmayı ve topluluğun ayrı ayrı gelişini kapsamaz.","preserves":"Bir işi başkalarından ayrı olarak üstlenme ilişkisini korur."},"facet_ids":["F001"],"text":"işi yalnız üstlenmek","usage_role":"contextual"},{"applicability":"Bir topluluğun üyelerinin toplu halde değil, ayrı ayrı geldiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bireyin bir işi yalnız üstlenmesini veya tek başına kalmasını kapsamaz.","preserves":"Ayrı ayrı ve birer birer geliş biçimini korur."},"facet_ids":["F002"],"text":"birer birer gelmek","usage_role":"contextual"}],"definition":"Bir kişinin bir işi başkalarından ayrı olarak yalnız üstlenmesi ya da tek başına kalmasıdır. Topluluk için kullanıldığında kişilerin toplu değil, ayrı ayrı ve birer birer gelmesini bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin bir işi başkalarından ayrı olarak üstlenmesini veya tek başına kalmasını bildirir."},{"facet_id":"F002","role":"extension","statement":"Bir topluluğun üyelerinin toplu halde değil, ayrı ayrı ve birer birer gelmesini bildirir."}],"identity_rationale":"Kaynak ifadesi kişinin bir işi yalnız üstlenmesi ya da tek başına kalması ile insanların ayrı ayrı, birer birer gelmesini açıkça birbirine bağlı iki kullanım olarak verir. Hazırlanan dal bu eylem ve dağılım ayrımını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"tek başına kalmak; işi yalnız üstlenmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"birer birer, ayrı ayrı"}],"lexicalization_note":"Tanım türemiş eylem biçimindeki yalnızlaşmayı ve yinelemeli dağılım sözündeki birer birer gelişi ayrı yüzler olarak tutar; ikisini yalın kök anlamı saymaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; yana çekilme, dağınık bulunma, yönlere dağılma ve benzeri az tek örnek dalları süreç ile nitelik sınırlarını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız üstlenme ile birer birer gelişe uzanır; komşu dal ise yana çekilme ve konumsal ayrılmayı daha belirgin biçimde taşır.","focus_only":"Odak dal bir işi yalnız üstlenmeyi ve topluluğun birer birer gelişini de kapsar.","gloss":"yana çekilme ve topluluktan ayrılma","neighbor_only":"Komşu dal topluluktan yana çekilmeyi, yer değiştirmeyi ve ayrı bir konumda bulunmayı kapsar.","neighbor_ref":"root_000305/B004","relation_type":"near_synonym","shared_zone":"İki dal bir kişinin topluluktan ayrılıp tek başına bulunmasını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal birer birer geliş biçimini ve bireysel yalnızlaşmayı belirtir; komşu dal yalnız topluluğun dağılmış durumunu kalıplaşmış biçimde bildirir.","focus_only":"Odak dal bireyin yalnızlaşmasını ve kişilerin birer birer gelişini kapsar.","gloss":"insanların dağılıp darmadağın olması","neighbor_only":"Komşu dal insanların genel olarak dağılmış ve darmadağın durumda bulunmasını anlatan kalıplaşmış bir sözdür.","neighbor_ref":"root_000154/B008","relation_type":"near_synonym","shared_zone":"İki dal bir topluluğun üyelerinin birlikte değil, dağınık durumda bulunmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal gelişin birer birer oluşunu ve bireysel yalnızlaşmayı da içerir; komşu dal yönlere dağılıp gitme olayına bağlıdır.","focus_only":"Odak dal tek başına kalmayı ve ayrı ayrı gelmeyi bildirir.","gloss":"farklı yönlere dağılıp gitmek","neighbor_only":"Komşu dal topluluğun farklı yönlere giderek dağılmasını bildiren kalıplaşmış bir anlatımdır.","neighbor_ref":"root_001331/B008","relation_type":"near_synonym","shared_zone":"İki dal bir topluluğun üyelerinin birbirinden ayrılarak dağılmasını kapsar."},{"boundary_match":"partial","distinction":"Odak dal insanların yalnızlaşma ya da ayrı ayrı hareket etme sürecini bildirir; komşu dal ise belirli bir hayvanın tek başına oluşunu adlandıran türle sınırlı bir kullanımdır.","focus_only":"Odak dal yalnızlaşma sürecini veya kişilerin ayrı ayrı hareket etmesini anlatır.","gloss":"topluluktan ayrı duran tek hayvan","neighbor_only":"Komşu dal belirli yaban hayvanlarının topluluktan ayrı duran tek üyesini adlandırır.","neighbor_ref":"root_000877/B009","relation_type":"near_neighbor","shared_zone":"İki dal bir canlının başkalarından ayrı ve tek başına bulunması düşüncesinde buluşur."}],"source_phrase_ar":"ما استأحدت بهذا الأمر أي ما انفردت به (maqayis); استأحد الرجل انفرد (sihah); جاءوا آحاد أحاد (sihah)","source_summary":"Kaynaklar tek başına kalma veya bir işi yalnız üstlenme anlamını birlikte destekler. Aynı kayıt, topluluğun üyelerinin ayrı ayrı ve birer birer gelişiyle bu çekirdeğin dağılımsal uzantısını da gösterir.","sources":["MQ","SI"],"what_is_ar":"الانفراد بالفعل، والمجيء آحادا أفرادا","what_is_not_ar":"ليس الواحد في العدد ولا نفي الجنس ولا علم الجبل"},"support_links":[]},{"boundary":"Bu dal yalnız belirli bir dağın özel adıdır; tek olma, olumsuz kişi kapsamı, sayı, gün adı ve yalnızlaşma anlamlarını taşımaz.","branch_kind":"non_bare","branch_ref":"root_000017/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:4:5:1","qac_word_ref":"112:4:5","surface_ar":"أَحَدٌۢ"}],"gloss":"Medine'deki belirli bir dağın özel adı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir dağın özel adı olarak tek bir coğrafi varlığı gösterir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dağın yeri kaynakta Medine ile ilişkilendirilmiştir."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel dağ anlamı yüklemeden, kaynakta Medine'de bulunduğu belirtilen tek coğrafi varlığın özel ad işlevini açıklar.","boundary_detail":"Bu dal yalnız belirli bir dağın özel adıdır; tek olma, olumsuz kişi kapsamı, sayı, gün adı ve yalnızlaşma anlamlarını taşımaz.","branch_image_ar":"جبل أُحُد","concept_gloss":"Medine'deki belirli bir dağın özel adı","contextual_glosses":[{"applicability":"Dağın kimliği bağlamdan zaten biliniyorsa, adı yeniden üretmeden özel ad işlevini açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kaynakta belirtilen kentle kurulan yer bağını açıkça taşımaz.","preserves":"Belirli bir dağın özel adı olma işlevini korur."},"facet_ids":["F001"],"text":"o dağın özel adı","usage_role":"explanatory"}],"definition":"Medine'de bulunan belirli bir dağa verilen özel addır. Genel olarak dağ türünü ya da dağın bir niteliğini değil, tek bir coğrafi varlığın kimliğini gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir dağın özel adı olarak tek bir coğrafi varlığı gösterir."},{"facet_id":"F002","role":"specialization","statement":"Dağın yeri kaynakta Medine ile ilişkilendirilmiştir."}],"identity_rationale":"Kaynak ifadesi bu birimi genel bir dağ türü olarak değil, belirli bir kentteki tek bir dağın özel adı olarak tanımlar. Hazırlanan dalın özel yer adı çerçevesi bu kanıtla doğrudan uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"Medine'deki dağın özel adı"}],"lexicalization_note":"Tanım yalnız kaynakta belirlenen özel dağ adına bağlıdır ve bu yer adı kullanımından genel bir dağ ya da yalın kök anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; başka dağ ve yer adları yalnız alan ortaklığı düzeyinde karşılaştırıldı, anlamdaşlık kurulmadı ve en açıklayıcı üç özel ad adayı yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Özel ad işlevleri aynı olsa da gösterdikleri coğrafi varlıklar ayrıdır; adlar birbirinin yerine kullanılamaz.","focus_only":"Odak dal kaynakta belirtilen kentteki belirli bir dağı adlandırır.","gloss":"başka bir dağın özel adı","neighbor_only":"Komşu dal başka bir belirli dağa verilen ayrı özel adı kapsar.","neighbor_ref":"root_000706/B006","relation_type":"same_field","shared_zone":"İki dal da genel dağ türünü değil, belirli bir dağın özel adını bildirir."},{"boundary_match":"field_only","distinction":"Aynı özel ad türüne girseler de farklı kentlerdeki farklı dağları gösterirler; kimlikleri ortak değildir.","focus_only":"Odak dal kaynakta belirtilen kentteki belirli dağı gösterir.","gloss":"başka bir kentteki tanınmış dağın adı","neighbor_only":"Komşu dal başka bir kentteki tanınmış dağı gösteren ayrı bir özel addır.","neighbor_ref":"root_000314/B006","relation_type":"same_field","shared_zone":"İki dal da bir kentle ilişkilendirilen tanınmış dağın özel adıdır."},{"boundary_match":"field_only","distinction":"Odak dal tek bir dağa bağlıdır; komşu dalın adı birden çok yer biçimine ve birden çok coğrafi varlığa uygulanabilir.","focus_only":"Odak dal yalnız tek bir belirli dağın özel adıdır.","gloss":"dağ ve tepeler için kullanılan başka bir yer adı","neighbor_only":"Komşu dal aynı adla anılan birden çok yer, dağ veya tepeyi kapsayabilir.","neighbor_ref":"root_000602/B002","relation_type":"same_field","shared_zone":"İki dal coğrafi varlıkları gösteren özel yer adları alanındadır."}],"source_phrase_ar":"أحد جبل بالمدينة (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak tanıklığı, birimi Medine'deki belirli dağın özel adı olarak kaydeder."}],"source_summary":"Bu dal genel bir sözlük anlamından çok, tek bir coğrafi varlığı gösteren özel ad kullanımını kapsar. Kaynak kaydı, gösterilen varlığın Medine'de bulunan dağ olduğunu bildirir.","sources":["SI"],"what_is_ar":"اسم جبل بالمدينة","what_is_not_ar":"ليس معنى الواحد ولا النفي ولا الاستئحاد"},"support_links":[]},{"boundary":"Denklik ve aynı ölçüde karşılık verme çekirdektir; art arda yönelme ile siper tutma yalnızca belirli yapılarda geçerlidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001305/B001","candidate_links":[{"candidate_id":"cand_acbf995d107174207efd","lane":"micro"},{"candidate_id":"cand_2dadd5d457a2a8844e4e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كُفُو","morph_features":"STEM|POS:N|LEM:kufuw|ROOT:kfA|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"112:4:4:1","qac_word_ref":"112:4:4","surface_ar":"كُفُوًا"}],"gloss":"denk olma ve aynı ölçüde karşılık verme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki kişi ya da şey arasında eşitlik, denklik veya birbirinin karşılığı olma ilişkisi kurar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Evlilikte uygunluk, toplumsal konum, mal varlığı veya savaş gücü bakımından denkliği anlatabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir iyiliğe ya da davranışa, yapılanla aynı ölçüde bir karşılık vermeyi anlatır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Belirli yapılarda iki hedefe art arda yönelme veya güneşin karşısına koruyucu bir şey koyma anlamı taşır."}}],"root_ar":"ك ف ء","root_id":"root_001305","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Denklik ile yapılanın dengiyle karşılanmasını birlikte taşıyan branch çekirdeğinin en kapsamlı kısa karşılığıdır.","boundary_detail":"Denklik ve aynı ölçüde karşılık verme çekirdektir; art arda yönelme ile siper tutma yalnızca belirli yapılarda geçerlidir.","branch_image_ar":"المماثلة والمقابلة بالمثل","concept_gloss":"denk olma ve aynı ölçüde karşılık verme","contextual_glosses":[{"applicability":"Kişilerin konum, evlilik uygunluğu, mal varlığı veya savaş gücü bakımından karşılaştırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir davranışa onun dengiyle karşılık verme anlamını dışarıda bırakır.","preserves":"İki taraf arasındaki denklik ve ölçü bakımından eşitlik ilişkisini korur."},"facet_ids":["F001","F002"],"text":"denk ve eşdeğer","usage_role":"contextual"},{"applicability":"Bir iyiliğin ya da davranışın, ona denk bir eylemle karşılandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişi veya şeylerin durağan biçimde birbirine denk olması anlamını dışarıda bırakır.","preserves":"Eylem ile karşılığı arasındaki ölçülü benzerliği ve karşılıklılığı korur."},"facet_ids":["F003"],"text":"aynı ölçüde karşılık vermek","usage_role":"contextual"},{"applicability":"Yalnızca iki hedefe art arda yönelmeyi veya güneşi bir nesneyle kesmeyi anlatan belirli yapılarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel denklik ve yapılanın dengiyle karşılık görmesi anlamlarını dışarıda bırakır.","preserves":"Belirli yapılardaki karşı karşıya gelme ve sırayla yönelme görüntüsünü korur."},"facet_ids":["F004"],"text":"sırayla yönelmek veya karşısına siper koymak","usage_role":"explanatory"}],"definition":"Bir kişi ya da şeyin konum, değer, güç veya başka bir ölçü bakımından bir başkasına denk olmasını ve bir davranışa onun dengiyle karşılık verilmesini anlatır. Belirli yapılarda iki hedefe sırayla yönelmeyi ya da güneşin karşısına bir siper koymayı da belirtebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki kişi ya da şey arasında eşitlik, denklik veya birbirinin karşılığı olma ilişkisi kurar."},{"facet_id":"F002","role":"specialization","statement":"Evlilikte uygunluk, toplumsal konum, mal varlığı veya savaş gücü bakımından denkliği anlatabilir."},{"facet_id":"F003","role":"extension","statement":"Bir iyiliğe ya da davranışa, yapılanla aynı ölçüde bir karşılık vermeyi anlatır."},{"facet_id":"F004","role":"associated_use","statement":"Belirli yapılarda iki hedefe art arda yönelme veya güneşin karşısına koruyucu bir şey koyma anlamı taşır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yapılana benzeriyle karşılık verme ve özel uygunluk anlamlarını dışarıda bırakır.","preserves":"İki tarafın aynı ölçüde olması yönündeki temel denklik ilişkisini korur."},"text":"eşitlik"}],"identity_rationale":"Kaynak ifadesi denklik, eşitlik ve yapılanın dengiyle karşılık görmesi çekirdeğini açıkça destekler. İki hedefe art arda yönelme ve güneşin karşısına siper koyma ise bu çekirdekle ilişkili, belirli yapılara bağlı kullanımlardır; genel anlamın kurucu parçaları sayılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"konum, soy, mal veya savaş gücü bakımından denk ve eş"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"denk, eş, aynı düzeyde olan"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"özellikle evlilikte düzey ve durum uygunluğu, denklik"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"denk ya da karşı koyabilecek güç"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bir davranışa veya iyiliğe dengiyle karşılık verme"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"eşitlik ve karşılıklı denklik"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kan bedeli ve karşılık cezası bakımından eşit sayılmak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"değer ve yaş bakımından birbirine eşit iki koyun"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"mızrakla iki atlıya birbiri ardınca yönelmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"güneşin karşısına gölge sağlayan bir siper koymak"}],"lexicalization_note":"Tanım yalın denklik ve karşılıklılık anlamını, yalnızca belirli söz öbeklerinde görülen art arda yönelme ve siperleme kullanımlarından ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en güçlü üç sınır karşılaştırması yayımlandı. Aynı kökün öteki branchleri anlamdaş değil, biçim ortaklığı taşıyan ayrı anlamlardır; kalan adaylar daha dar veya yinelenen denklik örnekleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu branch denklikten karşılıklılık ve uygun eş olma yönlerine uzanır; komşu branch ise daha genel bir eşitlik ve ölçü paralelliği alanına sahiptir.","focus_only":"Uygun eş olma, bir davranışa dengiyle karşılık verme ve belirli yapılardaki karşı karşıya getirme kullanımları vardır.","gloss":"genel eşitlik ve ölçü denkliği","neighbor_only":"Genel eşitliğin yanında değer veya fiyat bakımından paralelliği ve kendi özel kalıplarını kapsar.","neighbor_ref":"root_000766/B001","relation_type":"near_synonym","shared_zone":"Her iki branch iki kişi ya da şeyin ortak bir ölçüde eşit veya denk oluşunu anlatır."},{"boundary_match":"partial","distinction":"Komşu branch karşılık verme eylemine daha sıkı bağlıdır; bu branch aynı ilişkiyi kapsamakla birlikte kişiler ve şeyler arasındaki genel denkliği de kurar.","focus_only":"Durağan denklik, eş olma ve ölçü bakımından eşitlik anlamlarını da içerir.","gloss":"yapılana benzeriyle karşılık verme","neighbor_only":"Özellikle bir kişiye onun davranışının benzeriyle karşılık verme eylemine odaklanır.","neighbor_ref":"root_000853/B011","relation_type":"near_synonym","shared_zone":"İki branch bir davranışın benzer bir davranışla karşılanması alanında örtüşür."},{"boundary_match":"partial","distinction":"Ortak denklik çekirdeğine rağmen bu branch karşılık verme eylemine de açılır; komşu branch ise aynı durumda ve aynı düzeyde bulunmaya daha yakındır.","focus_only":"Yapılan iyiliğin veya davranışın dengiyle karşılanmasını ve bazı yapıya bağlı karşı karşıya getirme kullanımlarını içerir.","gloss":"birbirine denk sayılma","neighbor_only":"Aynı durumda bulunma ve belirli toplumsal ilişkilerde denkliği gözetme yönleri daha belirgindir.","neighbor_ref":"root_000161/B003","relation_type":"near_synonym","shared_zone":"Her iki branch eşdeğer taraflar arasında denklik ve karşılıklı ölçü birliği kurar."}],"source_phrase_ar":"الكفء المثل (maqayis)؛ التكافؤ التساوي (maqayis)؛ هذا كفء له أي مثله في الحسب والمال والحرب (ayn)؛ المكافأة مجازاة النعم (ayn)؛ الكفئ النظير (sihah)؛ كل شيء ساوى شيئا حتى يكون مثله فهو مكافئ له (sihah;tahdhib)؛ كافأت الرجل أي فعلت به مثل ما فعل بي (tahdhib)؛ فلان كفء لفلان في المناكحة أو في المحاربة (mufradat)؛ نكافىء بهما عنا عين الشمس (tahdhib)؛ كافأ الرجل بين فارسين برمحه (tahdhib)","source_summary":"Aktarılan kullanımlar, bir şeyin ötekine denk sayılması ile eylemin benzeriyle karşılanmasını ortak eksen yapar. Evlilik ve savaş denkliği bu eksenin özel uygulamalarıdır; iki hedefe sırayla yönelme ve güneşe karşı siper tutma ise belirli söz öbeklerinde ortaya çıkan ilişkili kullanımlardır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الكفء والمثل والنظير؛ التساوي والتكافؤ؛ الكفاءة في المناكحة والحرب والمضادة؛ المكافأة والمجازاة بالمثل؛ المقابلة والموالاة بين شيئين","what_is_not_ar":"ليس قلب الإناء ولا إمالة الشيء؛ وليس الإكفاء في الشعر؛ وليس كفاء الخباء؛ وليس كفأة النتاج"},"support_links":["sup_8b63b4d4bf8d151a57c1","sup_c22e2afcdd54078053f2"]},{"boundary":"Fiziksel eğme, devirme ve yön değiştirme çekirdektir; sallanma ve görünüş değişmesi bağımlı uzantılardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001305/B002","candidate_links":[{"candidate_id":"cand_3143897e5b81be86df74","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كُفُو","morph_features":"STEM|POS:N|LEM:kufuw|ROOT:kfA|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"112:4:4:1","qac_word_ref":"112:4:4","surface_ar":"كُفُوًا"}],"gloss":"eğmek, ters çevirmek veya yönünden döndürmek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesneyi eğme, kabı ters çevirme veya bir topluluğu gitmek istediği yönden döndürme işlemini anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yürüyen kişinin sağa sola sallanmasını yön değişiminin süreklileşmiş biçimi olarak anlatır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yüzün düşmesi veya rengin değişmesi için kullanılır."}}],"root_ar":"ك ف ء","root_id":"root_001305","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesnenin duruşunu ya da kişinin ve topluluğun yönünü değiştiren branch çekirdeğini birlikte karşılar.","boundary_detail":"Fiziksel eğme, devirme ve yön değiştirme çekirdektir; sallanma ve görünüş değişmesi bağımlı uzantılardır.","branch_image_ar":"الإمالة والقلب والصرف","concept_gloss":"eğmek, ters çevirmek veya yönünden döndürmek","contextual_glosses":[{"applicability":"Kap, yay, tabak ve benzeri somut nesnelerin duruşunun değiştirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Topluluğu başka yöne çevirme ile yürüyüş ve görünüş değişmesi uzantılarını dışarıda bırakır.","preserves":"Somut bir nesnenin düz konumundan çıkarılması ve yönünün değiştirilmesini korur."},"facet_ids":["F001"],"text":"ters çevirmek veya eğmek","usage_role":"contextual"},{"applicability":"Bir kişinin yürüyüş sırasında sağa sola eğilip salındığı bağlamlara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir nesneyi devirmeyi, başkasını yönünden çevirmeyi ve görünüş değişimini dışarıda bırakır.","preserves":"Sürekli yön değişimi ve bir yandan öbür yana eğilme görüntüsünü korur."},"facet_ids":["F002"],"text":"iki yana sallanarak yürümek","usage_role":"contextual"},{"applicability":"Bir kişinin yüzünün önceki görünüşünden uzaklaşıp düşkün veya solgun görünmesi ya da renginin değişmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesne eğme ve devirme ile yönünden çevirme ve sallanma anlamlarını dışarıda bırakır.","preserves":"Yüzün düşmesi ve rengin önceki durumundan değişmesi anlamını korur."},"facet_ids":["F003"],"text":"yüzü düşmek veya rengi değişmek","usage_role":"contextual"}],"definition":"Bir şeyi düz veya amaçlanan yönünden eğmeyi, ters çevirmeyi ya da başka bir yöne döndürmeyi anlatır. Belirli yapılarda yürürken iki yana sallanma ya da yüzün ve rengin değişmesi anlamlarına uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesneyi eğme, kabı ters çevirme veya bir topluluğu gitmek istediği yönden döndürme işlemini anlatır."},{"facet_id":"F002","role":"extension","statement":"Yürüyen kişinin sağa sola sallanmasını yön değişiminin süreklileşmiş biçimi olarak anlatır."},{"facet_id":"F003","role":"associated_use","statement":"Yüzün düşmesi veya rengin değişmesi için kullanılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalnız eğme, başka yöne çevirme ve yapıya bağlı uzantıların tümünü dışarıda bırakır.","preserves":"Bir nesnenin önceki duruşundan çıkarılıp ters konuma getirilmesini korur."},"text":"devirmek"}],"identity_rationale":"Kaynak ifadesi eğme, devirme ve başka yöne çevirme çekirdeğini doğrudan destekler. Yürürken sallanma, yüzün düşmesi ve rengin değişmesi bu yön değişikliği görüntüsünden gelişen ayrı kullanımlardır; hepsini tek bir fiziksel işlem gibi sunmak sınırı bozar.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kabı baş aşağı çevirip içindekini dökmek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bir şeyi düz konumundan eğmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yayın ucunu eğip onu atış için dik tutmamak"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"tabağı kendine doğru eğerek içindekini dökmek"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"bir topluluğu gitmek istediği yönden başka yöne çevirmek"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yürürken sağa sola sallanmak"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yüzü düşmüş ve rengi solmuş olmak"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"rengi değişmiş olmak"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"geri dönmek veya bozguna uğrayıp çekilmek"}],"lexicalization_note":"Tanım genel yön değiştirme çekirdeğini korur, ancak kap, yay, yürüyüş, yüz ve topluluğa bağlı anlamları kendi söz öbeği sınırları içinde gösterir.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; geri çevirme, yüzü üzerine devirme ve bir yana eğilme en açıklayıcı üç sınırı verdi. Aynı kökün diğer branchleri ayrı anlamlardır; kalan adaylar bu karşılaştırmaları yineler veya yalnızca aynı hareket alanına uzaktan katılır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu branch geri çevirme ve dönüşe daha sıkı bağlıdır; bu branch fiziksel eğme ve devirmenin yanında sallanma ile görünüş değişimini de kapsar.","focus_only":"Nesneyi eğme, kabı devirme, yürürken sallanma ve yüz renginin değişmesi kullanımlarını içerir.","gloss":"yönünden çevirip geri döndürmek","neighbor_only":"Bir şeyin yönünden geri çevrilmesi ve bir topluluğun yurduna dönmesi ekseni daha belirgindir.","neighbor_ref":"root_001306/B002","relation_type":"near_synonym","shared_zone":"İki branch bir şeyi bulunduğu doğrultudan başka yöne çevirme alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu branch yüzü üzerine düşürme sonucunu gerektirir; bu branch ise sonuçtan bağımsız eğmeyi ve yalnızca yön değiştirmeyi de kapsar.","focus_only":"Hafifçe eğme, kişiyi başka yöne çevirme ve mecazlaşmış sallanma ile görünüş kullanımları vardır.","gloss":"yüzü üzerine devirmek","neighbor_only":"Bir şeyi ya da canlıyı özellikle yüzü üzerine düşürme ve yere serme sonucuna odaklanır.","neighbor_ref":"root_001278/B001","relation_type":"near_synonym","shared_zone":"Her iki branch kabı veya başka bir varlığı önceki dik duruşundan çıkarıp devirmeyi anlatabilir."},{"boundary_match":"partial","distinction":"Komşu branch yönelme ve amaç edinmeye kadar uzanır; bu branch ise eğme, devirme veya mevcut yönü bozma işlemini temel alır.","focus_only":"Ters çevirme, başkasını yönünden döndürme ve bunlardan gelişen görünüş kullanımlarını içerir.","gloss":"bir yöne eğilmek","neighbor_only":"Bir yöne yönelme, amaç edinme ve iki yön arasında geçiş anlamlarını kendi başına kapsar.","neighbor_ref":"root_000362/B002","relation_type":"near_synonym","shared_zone":"İki branch düz doğrultudan bir yana eğilme veya yön değiştirme alanında örtüşür."}],"source_phrase_ar":"أكفأت الشيء إذا أملته (maqayis;tahdhib)؛ كفأت القصعة والإناء (ayn)؛ كفأت الإناء إذا كببته (sihah;tahdhib)؛ كفأت القوم إذا صرفتهم إلى غيره (sihah;tahdhib)؛ تكفأت المرأة في مشيتها (sihah)؛ تكفأ تكفؤا (tahdhib)؛ مكفأ الوجه كاسف اللون (ayn;tahdhib)؛ الإكفاء قلب الشيء كأنه إزالة المساواة (mufradat)","source_summary":"Ortak eksen, bir şeyin doğal ya da amaçlanan doğrultusundan çıkarılmasıdır: nesne eğilir veya devrilir, topluluk başka yöne çevrilir. Yürüyüşte sallanma ve görünüşteki bozulma, bu eksenin belirli yapılarda kazandığı uzantılardır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه إمالة الشيء وقلبه وكبه؛ إمالة القوس والصحفة؛ صرف القوم عن وجهتهم؛ التمايل في المشي أو كالسفينة؛ انكسار الوجه وتغير اللون","what_is_not_ar":"ليس الكفء بمعنى المثل؛ وليس المكافأة بالمثل؛ وليس الإكفاء العروضي إلا من جهة تسميته الفنية؛ وليس كفأة النتاج"},"support_links":["sup_8dab2f8db81abb1c6df8"]},{"boundary":"Anlam yalnız şiirde birbirine karşılık gelmesi gereken dize sonlarının harf, ses veya çekim bakımından uyuşmamasıdır.","branch_kind":"bare","branch_ref":"root_001305/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كُفُو","morph_features":"STEM|POS:N|LEM:kufuw|ROOT:kfA|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"112:4:4:1","qac_word_ref":"112:4:4","surface_ar":"كُفُوًا"}],"gloss":"şiirde dize sonu uyumsuzluğu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Şiirde karşılıklı dize sonları arasında beklenen ses ve biçim uyumunun bozulmasını anlatır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Uyumsuzluk farklı son harflerinden, farklı sesletimlerden veya farklı dilbilgisel sonlardan doğabilir."}}],"root_ar":"ك ف ء","root_id":"root_001305","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Harf, sesletim ve dilbilgisel son farklılıklarını tek teknik kusur altında kapsayan kısa karşılıktır.","boundary_detail":"Anlam yalnız şiirde birbirine karşılık gelmesi gereken dize sonlarının harf, ses veya çekim bakımından uyuşmamasıdır.","branch_image_ar":"اختلاف القوافي","concept_gloss":"şiirde dize sonu uyumsuzluğu","contextual_glosses":[{"applicability":"Dize sonlarının farklı harf veya seslerle kurulması nedeniyle uyak düzeninin bozulduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalnızca dilbilgisel sonların farklılaşmasından doğan biçimsel türü açıkça belirtmez.","preserves":"Dize sonları arasındaki işitsel uyuşmazlığı ve bunun şiirsel bir kusur oluşunu korur."},"facet_ids":["F001","F002"],"text":"uyak tutarsızlığı","usage_role":"contextual"},{"applicability":"Karşılıklı dize sonlarının farklı dilbilgisel biçimlerde kurulduğu özel durumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Harf veya salt sesletim farklılığından doğan öteki gerçekleşme biçimlerini dışarıda bırakır.","preserves":"Dilbilgisel sonların farklılaşmasıyla oluşan uyuşmazlığı açık biçimde korur."},"facet_ids":["F002"],"text":"dize sonlarında çekim uyuşmazlığı","usage_role":"explanatory"}],"definition":"Şiirde birbirine uyması gereken dize sonlarının harf, sesletim veya dilbilgisel son bakımından farklı kurulmasıdır. Bir dize sonunun başka harfle bitmesi ya da benzer sonların farklı çekimlenmesi bu kusurun gerçekleşme biçimleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Şiirde karşılıklı dize sonları arasında beklenen ses ve biçim uyumunun bozulmasını anlatır."},{"facet_id":"F002","role":"source_variant","statement":"Uyumsuzluk farklı son harflerinden, farklı sesletimlerden veya farklı dilbilgisel sonlardan doğabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Dize sonları arasındaki belirtilen uyumsuzluk dışında kalan her türlü uyak kusurunu da çağrıştırır.","collision":null,"fit":"broadening","loses":null,"preserves":"Şiirde uyak düzenine ilişkin bir kusur bulunduğunu genel olarak korur."},"text":"uyak bozukluğu"}],"identity_rationale":"Kaynak ifadesi şiirde dizelerin uyakları arasında harf, sesletim veya dilbilgisel son bakımından tutarsızlık bulunmasını açıkça tanımlar. Verilen branch çerçevesi bu teknik kusuru başka eğme ya da denklik anlamlarıyla karıştırmadan doğru biçimde sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"şiirde dize sonlarının harf, ses veya çekim bakımından uyuşmaması"}],"lexicalization_note":"Mekanik sınıflandırma yalındır; tanım bu yalın teknik anlamı korur ve komşu şiir terimlerinin özel yapılarını ona eklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yakın adlandırma ayrılığı ile dize sonu ve teknik ses konumu kavramları yayımlandı. Öteki adaylar şiirin ölçü veya uyak alanını paylaşsa da bu özel uyumsuzluğun sınırını daha fazla keskinleştirmiyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu branch daha geniş bir tamamlama anlamı taşır ve uyak alanındaki türü daha dar olabilir; bu branch ise dize sonlarındaki harf, ses ve çekim uyuşmazlığını başlı başına tanımlar.","focus_only":"Harf farkının yanında sesletim ve dilbilgisel son uyuşmazlıklarını da kapsayan bağımsız teknik kusurdur.","gloss":"şiirde tamamlama veya belirli uyak ayrılığı","neighbor_only":"Başkasının yarım bıraktığı dizeyi tamamlama eylemini de kapsar ve uyak kullanımında belirli son harf değişimleriyle sınırlanabilir.","neighbor_ref":"root_000276/B012","relation_type":"near_synonym","shared_zone":"İki branch bazı şiir geleneklerinde dize sonlarının farklı harflerle kurulması kusurunda örtüşür."},{"boundary_match":"field_only","distinction":"Komşu branch yapısal bir bölümü ve genel uyak olgusunu adlandırır; bu branch ise o bölümler arasındaki belirli uyumsuzluğu adlandırır.","focus_only":"Dize sonları arasında beklenen uyumun bozulmasını ve bunun kusur sayılmasını anlatır.","gloss":"dize sonu ve uyak","neighbor_only":"Dize sonunun kendisini, şiirin son bölümünü ve uyaklı söz üretme eylemini anlatır.","neighbor_ref":"root_001247/B003","relation_type":"same_field","shared_zone":"Her iki branch şiirde dize sonlarının kuruluşu ve birbirleriyle ilişkisi alanındadır."},{"boundary_match":"field_only","distinction":"Komşu branch dize sonunun bir bileşenini tanımlar; bu branch bileşenlerin dizeler arasında uyuşmamasıyla ortaya çıkan kusuru tanımlar.","focus_only":"Karşılıklı dize sonlarının harf, ses veya çekim bakımından tutarsız olmasını anlatır.","gloss":"dize sonundaki belirli ses konumu","neighbor_only":"Dize sonundaki belirli bir harf veya sesin teknik konumunu ve niteliğini anlatır.","neighbor_ref":"root_001630/B011","relation_type":"same_field","shared_zone":"İki branch şiir dizesinin sonundaki seslerin teknik düzenlenişiyle ilgilidir."}],"source_phrase_ar":"الإكفاء في الشعر (maqayis;ayn;sihah;tahdhib;mufradat)؛ أن ترفع قافية وتخفض أخرى (maqayis)؛ الاختلاط في القوافي (ayn)؛ يخالف بين قوافيه بعضها ميم وبعضها نون (sihah)؛ اختلاف إعراب القوافي (tahdhib)","source_summary":"Aktarılan açıklamaların ortak noktası, şiirde karşılık beklenen dize sonlarının birbirine uymamasıdır. Açıklamalar bu uyumsuzluğu son harfin değişmesi, sesletimin farklılaşması veya dilbilgisel sonların ayrı kurulması biçimlerinde somutlaştırır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الإكفاء في الشعر باختلاف القوافي في الحروف أو الحركات أو الإعراب","what_is_not_ar":"ليس كل إمالة أو قلب؛ وليس التكافؤ والتساوي؛ وليس كفاء الخباء"},"support_links":[]},{"boundary":"Bu branch genel olarak çadırı değil, onun arka bölümüne dikilip yerleştirilen belirli kumaş parçasını ve onu yapma eylemini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001305/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كُفُو","morph_features":"STEM|POS:N|LEM:kufuw|ROOT:kfA|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"112:4:4:1","qac_word_ref":"112:4:4","surface_ar":"كُفُوًا"}],"gloss":"çadırın arkasına dikilen kumaş örtü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir veya iki parçadan dikilen ve çadırın arka tarafını örten belirli kumaş bölümünü adlandırır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli bir yapıda çadır için bu arka örtüyü yapma ve yerine yerleştirme eylemini anlatır."}}],"root_ar":"ك ف ء","root_id":"root_001305","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesnenin malzemesini, çadırdaki yerini ve örtme işlevini birlikte veren en kısa doğal karşılıktır.","boundary_detail":"Bu branch genel olarak çadırı değil, onun arka bölümüne dikilip yerleştirilen belirli kumaş parçasını ve onu yapma eylemini anlatır.","branch_image_ar":"كِفاء الخباء","concept_gloss":"çadırın arkasına dikilen kumaş örtü","contextual_glosses":[{"applicability":"Parçanın çadırdaki yeri ve işlevi bağlamdan açıkça anlaşıldığında kısa nesne adı olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir veya iki kumaş parçasının birbirine dikilmesiyle yapılma özelliğini açıkça belirtmez.","preserves":"Parçanın çadırın arkasını kapatan bir örtü olması özelliğini korur."},"facet_ids":["F001"],"text":"çadırın arka örtüsü","usage_role":"contextual"},{"applicability":"Çadır için özel arka parçanın hazırlanıp yerleştirildiği eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Örtü parçasının bağımsız nesne adı olarak kullanımını dışarıda bırakır.","preserves":"Belirli örtünün dikilmesi ve çadıra eklenmesi işlemini korur."},"facet_ids":["F002"],"text":"çadıra arka örtü dikmek","usage_role":"contextual"}],"definition":"Bir ya da iki kumaş parçasının birbirine dikilmesiyle yapılan ve çadırın arka bölümünü kaplayan örtü parçasıdır. Belirli bir eylem yapısında, çadıra böyle bir arka örtü hazırlayıp yerleştirmeyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir veya iki parçadan dikilen ve çadırın arka tarafını örten belirli kumaş bölümünü adlandırır."},{"facet_id":"F002","role":"associated_use","statement":"Belirli bir yapıda çadır için bu arka örtüyü yapma ve yerine yerleştirme eylemini anlatır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Çadırın başka bölümlerindeki kumaşları da kapsar ve parçanın arka bölüme özgü yerini siler.","collision":"Genel çadır kumaşıyla karışır.","fit":"broadening","loses":null,"preserves":"Çadırda kullanılan bir kumaş parçası olma özelliğini korur."},"text":"çadır bezi"}],"identity_rationale":"Kaynak ifadesi bir ya da iki kumaş parçasının birbirine dikilerek çadırın arka bölümünü örtmesini ve bu parçanın eve takılmasını açıkça anlatır. Verilen çerçeve nesneyi, yapım ilişkisini ve yerini doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir veya iki parçadan dikilip çadırın arkasına konan kumaş örtü"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"çadıra arka örtü hazırlayıp yerleştirmek"}],"lexicalization_note":"Tanım nesne adını temel alır; çadıra bu parçayı yapıp takma eylemini yalnızca ilgili söz öbeğine bağlı bir uygulama olarak ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dikili kumaş barınak, deri örtü ve genel dikiş alanları sınırı en iyi gösterdi. Diğer adaylar yalnız barınak yapımını veya çevreleme işlevini paylaşır ve aynı ayrımları yineler.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu branch bağımsız bir örtü veya küçük barınaktır; bu branch ise daha büyük çadırın yalnız arka bölümünü oluşturan parçadır.","focus_only":"Çadırın arka bölümünü kaplayan, bir veya iki parçadan dikilmiş belirli yapısal örtüdür.","gloss":"dikili koruyucu kumaş barınak","neighbor_only":"Böceklere karşı koruyucu, başlı başına küçük bir kumaş barınak veya kubbemsi örtü olabilir.","neighbor_ref":"root_001315/B006","relation_type":"near_neighbor","shared_zone":"İki branch dikilerek yapılan ve korunma ya da örtme işlevi gören kumaş yapıları anlatır."},{"boundary_match":"partial","distinction":"Komşu branch malzeme ve işlev bakımından daha geniş, bağımsız bir nesnedir; bu branch konumu çadırın arka tarafıyla belirlenmiş yapısal parçadır.","focus_only":"Bir çadırın arka yüzüne özgü dikili kumaş parçasıdır.","gloss":"deri örtü veya küçük barınak","neighbor_only":"Deriden yapılabilen bağımsız bir örtü, yaygı, kap veya kubbemsi barınak niteliği taşıyabilir.","neighbor_ref":"root_000156/B004","relation_type":"near_neighbor","shared_zone":"Her iki branch ev veya barınakla ilişkili, örtme amacı taşıyan esnek bir parçayı anlatabilir."},{"boundary_match":"thematic_only","distinction":"Komşu branch üretim işleminin genel adıdır; bu branch o işlemle yapılan, yeri ve işlevi belirli tek bir çadır parçasıdır.","focus_only":"Dikme işlemiyle ortaya çıkan ve çadırda belirli yere takılan nesneyi adlandırır.","gloss":"dikmek ve dikiş","neighbor_only":"Genel dikiş eylemini, dikilmiş nesneyi ve dikiş aracını kapsar.","neighbor_ref":"root_000453/B006","relation_type":"thematic","shared_zone":"Bu branchteki örtü bir veya iki kumaş parçasının dikilmesiyle hazırlanır."}],"source_phrase_ar":"الكفاء شقتان تنصح إحداهما بالأخرى (maqayis)؛ الكفاء شقة أو ثنتان ينصح إحداهما بالأخرى (ayn)؛ الكفاء بالكسر والمد شقة أو شقتان (sihah)؛ أكفأت البيت فهو مكفأ إذا عملت له كفاء (tahdhib)؛ الكفاء لشقة تنصح بالأخرى فيجلل بها مؤخر البيت (mufradat)","source_summary":"Ortak tanım, bir veya iki kumaş parçasının dikilmesiyle oluşan ve çadırın arka bölümünü kaplayan özel bir örtüdür. Eylem kullanımı, genel bir ev yapmayı değil, çadıra tam olarak bu parçayı hazırlayıp eklemeyi belirtir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الكِفاء بمعنى شقة أو شقتين تخاطان ويجعل بهما مؤخر الخباء أو البيت","what_is_not_ar":"ليس الكفء بمعنى النظير؛ وليس قلب الإناء؛ وليس الإكفاء في الشعر؛ وليس كفأة النتاج"},"support_links":[]},{"boundary":"Bir yıllık ürün veya hayvansal yarar çekirdektir; sürüyü dönüşümlü yavrulayan iki gruba ayırma ayrı bir düzenleme işlemidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001305/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كُفُو","morph_features":"STEM|POS:N|LEM:kufuw|ROOT:kfA|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"112:4:4:1","qac_word_ref":"112:4:4","surface_ar":"كُفُوًا"}],"gloss":"bir yıllık ürün, yavru ve hayvansal yarar payı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ağacın bir yıldaki ürünü veya deve sürüsünün bir yıldaki yavru ve diğer yararlarının toplamını anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir ağacın ürününü ya da develerin yavru, süt ve yününü bir yıllığına isteme veya birine verme işlemini anlatır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Deve sürüsünü iki gruba ayırıp her yıl yalnız bir grubun yavrulamasını sağlayan dönüşümlü düzeni anlatır."}}],"root_ar":"ك ف ء","root_id":"root_001305","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bitki ürününü ve develerden bir yıl içinde elde edilen yavru, süt ve yün gibi yararları ortak dönem sınırıyla kapsar.","boundary_detail":"Bir yıllık ürün veya hayvansal yarar çekirdektir; sürüyü dönüşümlü yavrulayan iki gruba ayırma ayrı bir düzenleme işlemidir.","branch_image_ar":"كفأة السنة والنتاج","concept_gloss":"bir yıllık ürün, yavru ve hayvansal yarar payı","contextual_glosses":[{"applicability":"Bir hurma ağacının yıllık ürünü ya da deve sürüsünün o yıl doğan yavruları söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Süt ve yün gibi diğer yararları ve sürüyü dönüşümlü gruplama işlemini dışarıda bırakır.","preserves":"Ürün veya yavrunun bir yıllık dönem içinde hesaplanan pay olmasını korur."},"facet_ids":["F001"],"text":"bir yıllık ürün veya yavru payı","usage_role":"contextual"},{"applicability":"Ağacın ürünü ya da develerin yavru, süt ve yününün bir yıllığına talep edildiği veya birine bırakıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yıllık ürünün nesne adı oluşunu ve sürünün iki gruba ayrılmasını dışarıda bırakır.","preserves":"Belirli yararın bir yıllık süreyle bir kişiye ayrılması işlemini korur."},"facet_ids":["F002"],"text":"bir yıllık yararını istemek veya vermek","usage_role":"contextual"},{"applicability":"Develerin iki gruba bölünüp her yıl gruplardan yalnız birinin çiftleştirildiği özel yetiştiricilik düzeninde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir yıllık ürün ve yarar payını adlandırma, isteme veya verme anlamlarını dışarıda bırakır.","preserves":"İki gruplu yapıyı ve yavrulamanın yıllar arasında dönüşümlü düzenlenmesini korur."},"facet_ids":["F003"],"text":"sürüyü dönüşümlü yavrulayan iki gruba ayırmak","usage_role":"explanatory"}],"definition":"Bir hurma ağacının bir yıllık ürününü veya deve sürüsünün bir yıllık yavruları ile süt, yün ve yavru gibi bir yıl boyunca sağlanan yararlarını anlatır. Belirli yapılarda bu yıllık yararı isteme ya da verme ve sürüyü her yıl bir grubu yavrulayacak biçimde ikiye ayırma işlemlerini belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ağacın bir yıldaki ürünü veya deve sürüsünün bir yıldaki yavru ve diğer yararlarının toplamını anlatır."},{"facet_id":"F002","role":"extension","statement":"Bir ağacın ürününü ya da develerin yavru, süt ve yününü bir yıllığına isteme veya birine verme işlemini anlatır."},{"facet_id":"F003","role":"specialization","statement":"Deve sürüsünü iki gruba ayırıp her yıl yalnız bir grubun yavrulamasını sağlayan dönüşümlü düzeni anlatır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yararın birine ayrılan pay oluşunu, isteme ve verme işlemlerini ve dönüşümlü sürü düzenini dışarıda bırakır.","preserves":"Ürün ve yararların bir yıllık dönemle ölçülmesini korur."},"text":"yıllık verim"}],"identity_rationale":"Kaynak ifadesi hurma ağacının bir yıllık ürünü, devenin bir yıllık yavruları ve hayvandan bir yıl boyunca sağlanan süt, yün ve yavru payını aynı yıllık yarar ekseninde toplar. Sürüyü iki gruba ayırıp yavrulamayı yıllara göre dönüşümlü düzenlemek ise aynı yıllık döngüyle ilişkili fakat ayrı bir işlem olduğu için tanımda bağımlı bir uzmanlaşma olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"hurmanın bir yıllık ürünü veya develerin bir yıllık yavru, süt ve yün yararı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"develerin bir yıllık yavru ve diğer yararlarını sahibinden istemek"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bir hurma ağacının bir yıllık ürününü istemek"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"develerin süt, yün veya yavrularını bir yıllığına birine vermek"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"deve sürüsünü yıllara göre dönüşümlü yavrulayan iki gruba ayırmak"}],"lexicalization_note":"Tanım yıllık ürün ve yarar adını, bunları bir yıllığına isteme ya da verme yapılarını ve sürüyü dönüşümlü gruplama yapısını birbirine karıştırmadan ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; deve yararları, genel bitki ürünü ve ürünün ortaya çıkışı en yararlı sınırları verdi. Kalan adaylar hasat, olgun meyve veya yetiştiricilik eylemlerini paylaşır fakat yıllık pay ve dönüşümlü sürü düzenini açıklamaz.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu branch yararların genel toplamını anlatır; bu branch onları bir yıllık dönem ve pay ilişkisiyle sınırlar, ayrıca sürü yönetimine uzanır.","focus_only":"Deve yararını bir yıllık pay olarak sınırlar, isteme ve verme işlemlerini ve dönüşümlü yavrulama düzenini kapsar.","gloss":"develerin ürünleri ve yararları","neighbor_only":"Devenin sağladığı yavru, süt ve benzeri yararları süre veya tahsis koşulu olmadan genel olarak adlandırır.","neighbor_ref":"root_000479/B002","relation_type":"near_synonym","shared_zone":"İki branch deve yavruları, süt ve başka hayvansal yararlar alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu branch bitkisel ürünü genel olarak anlatır; bu branch ürünün bir yıllık pay oluşunu öne çıkarır ve hayvansal yararlara da uzanır.","focus_only":"Ağaç ürününü bir yıllık pay olarak ele alır ve aynı branchte deve yavrusu ile diğer hayvansal yararları da kapsar.","gloss":"ağaç ve ekin ürünü","neighbor_only":"Ağaç, ekin ve toprağın verdiği ürünü süre veya yararlanma tahsisi olmadan genel biçimde adlandırır.","neighbor_ref":"root_000043/B002","relation_type":"near_neighbor","shared_zone":"İki branch bir ağacın, özellikle hurmanın verdiği ürün alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu branch büyüme ve ürünün ortaya çıkışına odaklanır; bu branch ortaya çıkan şeyin bir yıllık pay ve yarar olarak hesaplanmasına odaklanır.","focus_only":"Ortaya çıkan ürünü bir yıllık yarar veya tahsis birimi olarak sınırlar ve sürü yavrularına da uygular.","gloss":"büyüme ve ürünün ortaya çıkması","neighbor_only":"Bitkinin büyüyüp ürün vermesi sürecini ve ürünün ortaya çıkışını genel olarak anlatır.","neighbor_ref":"root_000009/B007","relation_type":"near_neighbor","shared_zone":"İki branch hurma veya ekin gibi bitkilerin ürün vermesi alanında buluşur."}],"source_phrase_ar":"الكفأة وهي حمل النخلة سنتها (maqayis)؛ يقال ذلك في نتاج الإبل أيضا (maqayis)؛ سألته نتاج إبله سنة (maqayis;ayn;tahdhib)؛ الكفأة من الإبل نتاج سنة (ayn)؛ أكفأت إبلي كفأتين (sihah;tahdhib)؛ أعطاني لبنها ووبرها وأولادها سنة (sihah)؛ سألته ثمرها سنة (tahdhib)؛ يقال لنتاج الإبل ليست تامة كفأة (mufradat)","source_summary":"Aktarılan kullanımların ortak ekseni, bitki ürünü ile deve yavrusu, sütü ve yünü gibi yararların bir yıllık dönemle sınırlandırılmasıdır. Bu yararın istenmesi veya verilmesi aynı dönemsel birime dayanır; sürünün iki gruba ayrılması ise yavrulamayı yıllar arasında dönüşümlü kılan özel bir düzenlemedir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الكفأة لحمل النخلة أو نتاج الإبل سنة؛ سؤال نتاج الإبل أو ثمر النخل سنة؛ إعطاء اللبن والوبر والأولاد سنة؛ جعل الإبل كفأتين يتناوب نتاجهما","what_is_not_ar":"ليس الكفء بمعنى المثل؛ وليس كفاء الخباء؛ وليس قلب الإناء ولا الإكفاء في الشعر"},"support_links":[]},{"boundary":"Dal, gerçekleşme ve bulunma çekirdeğiyle sınırlıdır; yer, konum, üstlenme ve boyun eğme ayrı dallardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001332/B001","candidate_links":[{"candidate_id":"cand_acbf995d107174207efd","lane":"micro"},{"candidate_id":"cand_3143897e5b81be86df74","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَانَ","morph_features":"STEM|POS:V|IMPF|LEM:kaAna|ROOT:kwn|SP:kaAn|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:4:2:1","qac_word_ref":"112:4:2","surface_ar":"يَكُن"}],"gloss":"gerçekleşme, bulunma ve olma bildirimi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin gerçekleşmesi, ortaya çıkması ve bulunur halde olması çekirdektir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Olma ve oluş adları bu çekirdeğin adlaştırılmış biçimleridir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Geçmişteki bir durumun haber verilmesi veya şimdiki olmanın bildirilmesi bu alana bağlıdır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Pekiştirme ve gelen kişiyi kapsam dışı bırakma gibi bağlı söz dizimleri çekirdeğe ek kullanımlardır."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Bir şeyi oldurmak, onun gerçekleşmesini sağlama yönünde ettirgen bir uzantıdır."}}],"root_ar":"ك و ن","root_id":"root_001332","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çekirdeği ve ona bağlı bildirme yönünü birlikte verir; daha dar söz dizimleri ayrıca açıklanmalıdır.","boundary_detail":"Dal, gerçekleşme ve bulunma çekirdeğiyle sınırlıdır; yer, konum, üstlenme ve boyun eğme ayrı dallardır.","concept_gloss":"gerçekleşme, bulunma ve olma bildirimi","contextual_glosses":[{"applicability":"Bir şeyin var ya da gerçekleşmiş olduğunu bildiren akıcı bağlamlarda kullanılır.","error_profile":{"adds":"Günlük Türkçede durum bildiren daha geniş kullanımları da çağırabilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Olma ve gerçekleşme çekirdeğini doğal Türkçe içinde korur."},"facet_ids":["F001","F003"],"text":"olmak","usage_role":"contextual"},{"applicability":"Bir işin ortaya çıkması veya sonradan olması vurgulandığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hazır bulunma ve dilbilgisel bildirme yönlerini dışarıda bırakır.","preserves":"Sonradan olma ve meydana çıkma yönünü korur."},"facet_ids":["F001"],"text":"gerçekleşmek","usage_role":"contextual"},{"applicability":"Sözün asıl yükünü taşımayıp anlatımı güçlendiren bağlı kullanım için açıklayıcıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Pekiştirme görevini doğrudan korur."},"facet_ids":["F004"],"text":"pekiştirme sözü","usage_role":"explanatory"},{"applicability":"Gelmesi beklenen kişiyi belirli bir ad dışında tutan bağlı söz dizimi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ayırma ve dışarıda tutma görevini korur."},"facet_ids":["F004"],"text":"kapsam dışında saymak","usage_role":"explanatory"}],"definition":"Bu dal, bir şeyin gerçekleşip bulunur hale gelmesini ve bu olmanın geçmiş ya da şimdiki anda bildirilmesini anlatır. Olma adları, pekiştirme ya da ayırma işlevli bağlı sözler ve bir şeyi oldurup oluşmasını sağlama buna bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin gerçekleşmesi, ortaya çıkması ve bulunur halde olması çekirdektir."},{"facet_id":"F002","role":"source_variant","statement":"Olma ve oluş adları bu çekirdeğin adlaştırılmış biçimleridir."},{"facet_id":"F003","role":"associated_use","statement":"Geçmişteki bir durumun haber verilmesi veya şimdiki olmanın bildirilmesi bu alana bağlıdır."},{"facet_id":"F004","role":"associated_use","statement":"Pekiştirme ve gelen kişiyi kapsam dışı bırakma gibi bağlı söz dizimleri çekirdeğe ek kullanımlardır."},{"facet_id":"F005","role":"extension","statement":"Bir şeyi oldurmak, onun gerçekleşmesini sağlama yönünde ettirgen bir uzantıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Ayrı yer ve konum dalının kapsamını getirir.","collision":"Aynı kökün yer dalıyla karışır.","fit":"displacement","loses":"Gerçekleşme, olma bildirimi ve bağlı dil kullanımlarını siler.","preserves":"Bulunma çevresine zayıf bir yakınlık taşır."},"text":"yer"}],"identity_rationale":"Kaynak anlatımı, bir şeyin gerçekleşip bulunur hale gelmesini çekirdek kabul eder ve buna olma adları ile geçmiş ya da şimdiki bildirme kullanımlarını bağlar. Pekiştirme, ayırma ve ettirgen oluşturma kullanımları aynı dal içinde bağımlı kullanımlar olarak durur; yer, konum ve üstlenme dalları bu çekirdeğin yerine geçirilmez.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"gerçekleşip ortaya çıkmak veya hazır bulunmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"geçmişte bir durumu bildirmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"oluş; gerçekleşme"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"olma, oluş"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"sonradan gerçekleşen iş"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yüklemi pekiştiren ek söz"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birini geliş kapsamı dışında tutan bağlı söz"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"var edip gerçekleşmesini sağlamak"}],"lexicalization_note":"Mekanik kapsam hem yalın hem bağlı kullanımlar verdiği için tanım çekirdeği ayrı, bağlı sözleri ayrı tutar.","neighbor_coverage_note":"Bütün aday komşular karşılaştırıldı; yayımlananlar okurun en kolay karıştırabileceği sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal daha geniştir: gerçekleşme ve bulunma çekirdeğine bildirme ve bağlı söz kullanımlarını ekler. Komşu dal ise yeni oluşu, yani daha önce yokken sonradan olmayı merkez yapar.","focus_only":"Olmanın bildirilmesi, pekiştirme, ayırma ve olma adları bu dalda ayrıca yer alır.","gloss":"olma ile yeni ortaya çıkma","neighbor_only":"Komşu dal özellikle yokluktan sonra yeni duruma gelmeyi öne çıkarır.","neighbor_ref":"root_000299/B001","relation_type":"near_synonym","shared_zone":"İkisi de bir şeyin sonradan gerçekleşmesi veya var hale gelmesi alanında buluşur."},{"boundary_match":"partial","distinction":"Komşu dalda hareket ve varış daha belirgindir; bu dalda ise bir şeyin olması, bulunması veya olmanın haber verilmesi belirleyicidir.","focus_only":"Bu dal olma ve bulunur hale gelme çekirdeğine bağlıdır.","gloss":"olmak ile gelmek","neighbor_only":"Komşu dal gelme, varma ve bir yere ya da işe yönelme hareketini taşır.","neighbor_ref":"root_000281/B001","relation_type":"near_neighbor","shared_zone":"Gerçekleşen veya elde edilen bir durumdan söz edildiğinde yakınlaşırlar."},{"boundary_match":"field_only","distinction":"B001 bir şeyin olması ya da bulunur hale gelmesidir; B002 bu olma çevresinden türetilmiş yer ve konum adlarını anlatır.","focus_only":"Bu dal zaman içinde olma, gerçekleşme ve bildirme alanındadır.","gloss":"olma ile yer","neighbor_only":"Komşu dal yer, bulunulan nokta ve kişinin konum değeriyle ilgilidir.","neighbor_ref":"root_001332/B002","relation_type":"same_field","shared_zone":"İkisi de aynı kökün olma ve bulunma çevresinden beslenir."},{"boundary_match":"thematic_only","distinction":"Anlam çekirdekleri yer değiştirmez: B001 bir şeyin olmasıdır, B003 ise bir kişi için güvence ve sorumluluk üstlenmedir.","focus_only":"Bu dal gerçekleşme ve olma bildirimi taşır.","gloss":"olma ile üstlenme","neighbor_only":"Komşu dal bir kişi adına sorumluluk üstlenmeyi anlatır.","neighbor_ref":"root_001332/B003","relation_type":"thematic","shared_zone":"İkisi aynı kök ailesinde anılır."},{"boundary_match":"thematic_only","distinction":"B006, genel olma anlamına genişletilemez; belirli kötü-durum deyişinde kalır. B001 ise bağlı kötü geceleme kullanımını içermez.","focus_only":"Bu dal genel olma, gerçekleşme ve bildirme alanını kapsar.","gloss":"olma ile kötü durumda geceleme","neighbor_only":"Komşu dal yalnız kötü durum içinde gece geçirme deyişine bağlıdır.","neighbor_ref":"root_001332/B006","relation_type":"thematic","shared_zone":"Kötü durum adı, olma çevresinden kurulmuş sayıldığı için kök bağı vardır."}],"source_summary":"Kaynaklar, dalı bir şeyin olması, gerçekleşmesi ve hazır bulunması etrafında toplar. Aynı bildirim içinde olma adları, geçmiş ya da şimdiki haber verme, pekiştirme, ayırma ve ettirgen oldurma kullanımları da bu çekirdeğe bağlanır."},"support_links":["sup_8dab2f8db81abb1c6df8","sup_c22e2afcdd54078053f2"]},{"boundary":"Dal yer, bulunulan nokta ve konum değeriyle sınırlıdır; genel olma ya da üstlenme anlamına açılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001332/B002","candidate_links":[{"candidate_id":"cand_2dadd5d457a2a8844e4e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَانَ","morph_features":"STEM|POS:V|IMPF|LEM:kaAna|ROOT:kwn|SP:kaAn|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:4:2:1","qac_word_ref":"112:4:2","surface_ar":"يَكُن"}],"gloss":"bulunma yeri ve konum değeri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin bulunduğu yer veya durduğu nokta çekirdek alandır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin bir başkası yanındaki konumu veya değeri yer anlamından genişler."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çok kullanım yüzünden baştaki m sesi kökten sanılarak türevler kurulmuştur."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Birinin başka birine göre belirli bir yerde veya düzeyde sayılması örnek kullanımdır."}}],"root_ar":"ك و ن","root_id":"root_001332","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer çekirdeğini ve kişisel değer uzantısını birlikte vermek gerektiğinde en uygundur.","boundary_detail":"Dal yer, bulunulan nokta ve konum değeriyle sınırlıdır; genel olma ya da üstlenme anlamına açılmaz.","concept_gloss":"bulunma yeri ve konum değeri","contextual_glosses":[{"applicability":"Somut bulunulan nokta ya da durulan alan anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişisel konum değeri ve türetim açıklamasını dışarıda bırakır.","preserves":"Bulunulan nokta çekirdeğini korur."},"facet_ids":["F001"],"text":"yer","usage_role":"contextual"},{"applicability":"Bir kişinin başkası yanındaki yeri veya düzeyi anlatıldığında uygundur.","error_profile":{"adds":"Güncel Türkçede her türlü durum ve düzen içindeki yeri de çağırabilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Düzey ve başkasına göre yer anlamını korur."},"facet_ids":["F002","F004"],"text":"konum","usage_role":"contextual"},{"applicability":"Baştaki m sesinin kökten sanılmasıyla kurulan türev fiil için açıklayıcıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yerleşme ve sağlam konum kazanma yönünü korur."},"facet_ids":["F003"],"text":"yerleşip güç kazanmak","usage_role":"explanatory"}],"definition":"Bu dal, olma kökünden türetilmiş sayılan bulunulan yeri, durulan noktayı ve kişinin başkası yanındaki konum değerini kapsar. Bazı türevlerde baştaki m sesi kökten sanıldığı için yerleşmiş biçimler ortaya çıkar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin bulunduğu yer veya durduğu nokta çekirdek alandır."},{"facet_id":"F002","role":"extension","statement":"Kişinin bir başkası yanındaki konumu veya değeri yer anlamından genişler."},{"facet_id":"F003","role":"source_variant","statement":"Çok kullanım yüzünden baştaki m sesi kökten sanılarak türevler kurulmuştur."},{"facet_id":"F004","role":"example","statement":"Birinin başka birine göre belirli bir yerde veya düzeyde sayılması örnek kullanımdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Ayrı gerçekleşme dalının alanını getirir.","collision":"B001 ile karışır.","fit":"displacement","loses":"Yer, bulunulan nokta ve konum değeri çekirdeğini siler.","preserves":"Olma köküyle uzak bir bağ taşır."},"text":"gerçekleşme"}],"identity_rationale":"Kaynak anlatımı, yer adını olma kökünden türetilmiş sayar ve aynı alanda yer, konum değeri, birinin yanındaki yer ve baştaki m sesinin kökten sanılmasıyla kurulan türevleri bir arada verir. Bu çerçeve, gerçekleşme çekirdeğini değil ondan türemiş yer ve değer alanını anlatır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bulunulan yer"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yerler"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"konum, düzey veya bulunulan yer"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"birinin yanında güçlü konumu olan"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yerleşmek veya güç kazanmak"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"birinin yanında şu yer veya düzeyde bulunmak"}],"lexicalization_note":"Mekanik kapsam hem ad biçimleri hem bağlı örnek verdiği için yer ve konum değerini bağlı örneklerden ayırır.","neighbor_coverage_note":"Bütün adaylar gözden geçirildi; yayımlanan ayrımlar yer ve konum alanındaki yakın komşuları seçer.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Somut yer için yakın dururlar; fakat B002 aynı zamanda kişinin başkası yanındaki değerini ve türetim açıklamasını taşır.","focus_only":"Bu dal ayrıca konum değeri ve m sesine dayalı türetim açıklamasını içerir.","gloss":"yer ve bulunma yeri","neighbor_only":"Komşu dal şeyin içinde bulunduğu yer anlamını daha yalın tutar.","neighbor_ref":"root_001439/B003","relation_type":"near_synonym","shared_zone":"İkisi de bir şeyin bulunduğu yer ya da durduğu nokta alanındadır."},{"boundary_match":"partial","distinction":"B002 yer ve konum değerini birlikte tutar; komşu dal kişisel hal ve değer alanına daha fazla yaslanır.","focus_only":"Bu dal bulunulan yeri de açıkça kapsar.","gloss":"konum değeri","neighbor_only":"Komşu dal yerden çok kişinin hali, değeri veya yerleşmiş durumunu öne çıkarır.","neighbor_ref":"root_001439/B004","relation_type":"near_synonym","shared_zone":"İkisi de kişinin başkaları yanındaki değerini veya durumdaki yerini anlatabilir."},{"boundary_match":"partial","distinction":"B002 bir noktanın ya da kişinin yerini adlandırır; komşu dal o yerin yakın oluşunu veya yakınlık ilişkisini bildirir.","focus_only":"Bu dal yerin veya konum değerinin adıdır.","gloss":"yer ile yakınlık","neighbor_only":"Komşu dal yakınlık, yaklaşmışlık ve yanında bulunma ilişkisini taşır.","neighbor_ref":"root_001052/B004","relation_type":"near_neighbor","shared_zone":"Mekansal bulunma anlatımlarında yan yana gelebilirler."},{"boundary_match":"field_only","distinction":"B001 olma olayını veya bildirimini verir; B002 ise bu olma çevresinden türetilmiş yer ve konum değeridir.","focus_only":"Bu dal yer ve konum değerini anlatır.","gloss":"yer ile olma","neighbor_only":"Komşu dal bir şeyin gerçekleşmesi, bulunması ve olmanın bildirilmesidir.","neighbor_ref":"root_001332/B001","relation_type":"same_field","shared_zone":"İkisi aynı kökün bulunma çevresinde ilişkilidir."}],"source_summary":"Kaynaklar, yer ve konum değerini aynı dalda toplar. Ayrıca baştaki m sesinin sonradan kökten sanılmasıyla kurulan türevleri ve birinin başka biri yanındaki yeri anlatan örneği de bu alana bağlar."},"support_links":["sup_8b63b4d4bf8d151a57c1"]},{"boundary":"Dal bir kişi adına sorumluluk üstlenmeyle sınırlıdır; genel olma, yer veya güven duyma anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001332/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَانَ","morph_features":"STEM|POS:V|IMPF|LEM:kaAna|ROOT:kwn|SP:kaAn|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:4:2:1","qac_word_ref":"112:4:2","surface_ar":"يَكُن"}],"gloss":"birini güvenceyle üstlenme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başka biri için sorumluluğu üstlenme ve ona güvence olma çekirdektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birinin üzerine olma biçimindeki bağlı söz, onun sorumluluğunu üstlenmeyi bildirir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dönüşlü bağlı biçim de aynı şekilde birine güvence olmayı anlatır."}}],"root_ar":"ك و ن","root_id":"root_001332","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi adına sorumluluk alma çekirdeğini kısa ve açık biçimde verir.","boundary_detail":"Dal bir kişi adına sorumluluk üstlenmeyle sınırlıdır; genel olma, yer veya güven duyma anlamı değildir.","concept_gloss":"birini güvenceyle üstlenme","contextual_glosses":[{"applicability":"Birinin sorumluluğunu üzerine alma anlatımında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Açık güvence verme tonunu tek başına göstermeyebilir.","preserves":"Sorumluluk alma çekirdeğini korur."},"facet_ids":["F001","F002"],"text":"üstlenmek","usage_role":"contextual"},{"applicability":"Bir başkası için güvence olma yönü öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sorumluluğu üzerine alma yönünü ikincil bırakır.","preserves":"Güvence olma yönünü açıkça korur."},"facet_ids":["F001","F003"],"text":"güvence vermek","usage_role":"contextual"}],"definition":"Bu dal, bir kişi için sorumluluğu üzerine almayı ve onun adına güvence vermeyi anlatır. Ad biçimi ve bağlı sözler aynı üstlenme çekirdeğini paylaşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başka biri için sorumluluğu üstlenme ve ona güvence olma çekirdektir."},{"facet_id":"F002","role":"specialization","statement":"Birinin üzerine olma biçimindeki bağlı söz, onun sorumluluğunu üstlenmeyi bildirir."},{"facet_id":"F003","role":"associated_use","statement":"Dönüşlü bağlı biçim de aynı şekilde birine güvence olmayı anlatır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Genel olma dalının geniş alanını getirir.","collision":"B001 ile karışır.","fit":"displacement","loses":"Bir kişi adına sorumluluk ve güvence üstlenme çekirdeğini siler.","preserves":"Kök ailesiyle yüzeysel bağ taşır."},"text":"olmak"}],"identity_rationale":"Kaynak anlatımı, bu dalı bir kişi için sorumluluk üstlenme ve onun adına güvence verme olarak açıkça ayırır. Kullanımlar bağlı sözlerle verilse de hepsi aynı üstlenme çekirdeğine döner; gerçekleşme, yer ve boyun eğme dallarıyla karıştırılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"başkası için güvence üstlenme"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"birini üstlenmek"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"birine güvence olmak"}],"lexicalization_note":"Mekanik kapsam bir ad biçimi ve bağlı sözler verdiği için tanım üstlenme çekirdeğini bağlı kullanımlarla sınırlar.","neighbor_coverage_note":"Adayların hepsi değerlendirildi; yayımlananlar üstlenme, koruma ve dayanma sınırını açık tutar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yerine göre yakın çevrilebilirler; ancak komşu dal daha geniş ve kurumlaşmış sorumluluk alanlarını da taşır.","focus_only":"Bu dal belirli kök ailesindeki üstlenme sözleriyle sınırlıdır.","gloss":"güvenceyle üstlenme","neighbor_only":"Komşu dal borç, mal, iş, bakım ve geçindirme gibi daha geniş üstlenme alanlarını kapsar.","neighbor_ref":"root_001309/B005","relation_type":"near_synonym","shared_zone":"İkisi de bir kişi veya iş için sorumluluk ve güvence alma alanındadır."},{"boundary_match":"partial","distinction":"B003 kişiye güvence olmayı anlatır; komşu dal sorumluluğu bir yük gibi taşıma ve ödeme alanına daha yakındır.","focus_only":"Bu dal bir kişi için üstlenme sözlerine bağlıdır.","gloss":"üstlenme ve yük taşıma","neighbor_only":"Komşu dal yükümlülük, ödeme veya hak taşıma gibi ağır sorumlulukları öne çıkarır.","neighbor_ref":"root_000357/B004","relation_type":"near_synonym","shared_zone":"İkisi de başkası adına sorumluluk alma alanında buluşur."},{"boundary_match":"field_only","distinction":"B003 güvence ve üstlenmeyi merkez yapar; komşu dal koruma ve gözetme işini merkez yapar.","focus_only":"Bu dal sorumluluğu üstlenip güvence olmaktır.","gloss":"üstlenme ile koruma","neighbor_only":"Komşu dal koruma, gözetme ve emanet edilen şeyi saklama alanındadır.","neighbor_ref":"root_000342/B001","relation_type":"same_field","shared_zone":"Bir kişiye veya şeye karşı sorumluluk duyma alanında kesişirler."},{"boundary_match":"thematic_only","distinction":"B003 sorumluluğu alan kişiyi merkeze koyar; komşu dal desteğe yaslanan kişiyi veya şeyi merkeze alır.","focus_only":"Bu dal güvence veren tarafın üstlenmesini anlatır.","gloss":"güvence olmak ile dayanmak","neighbor_only":"Komşu dal başkasına dayanma veya ondan yardım isteme tarafını anlatır.","neighbor_ref":"root_001062/B006","relation_type":"thematic","shared_zone":"İkisi aynı yardımlaşma ve destek sahnesinde bulunabilir."},{"boundary_match":"thematic_only","distinction":"Yüzey bağına rağmen anlam çekirdekleri ayrıdır: B003 üstlenmedir, B001 bir şeyin olması veya olmanın bildirilmesidir.","focus_only":"Bu dal bir kişi için sorumluluk üstlenmektir.","gloss":"üstlenme ile olma","neighbor_only":"Komşu dal olma, gerçekleşme ve bildirme alanındadır.","neighbor_ref":"root_001332/B001","relation_type":"thematic","shared_zone":"İkisi aynı kök ailesinde yer alır."}],"source_summary":"Kaynaklar, bu dalı bir kişi için güvence ve sorumluluk üstlenme anlamında birleştirir. Ad biçimi, üzerine alma sözü ve dönüşlü bağlı biçim aynı çekirdeğin ayrı anlatımlarıdır."},"support_links":[]},{"boundary":"Dal boyun eğme ve direnç göstermeme anlamındadır; güvence, yer veya kötü durum anlamı değildir.","branch_kind":"bare","branch_ref":"root_001332/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَانَ","morph_features":"STEM|POS:V|IMPF|LEM:kaAna|ROOT:kwn|SP:kaAn|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:4:2:1","qac_word_ref":"112:4:2","surface_ar":"يَكُن"}],"gloss":"boyun eğme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Boyun eğme ve direnç göstermeme bu dalın çekirdeğidir."}}],"root_ar":"ك و ن","root_id":"root_001332","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yalın çekirdeğini en kısa ve doğal biçimde verir.","boundary_detail":"Dal boyun eğme ve direnç göstermeme anlamındadır; güvence, yer veya kötü durum anlamı değildir.","concept_gloss":"boyun eğme","contextual_glosses":[{"applicability":"Davranış olarak alçalma ve direnç göstermeme anlatıldığında kullanılır.","error_profile":{"adds":"Uysallık tonu kaynak bildiriminde ayrıca zorunlu değildir.","collision":null,"fit":"broadening","loses":null,"preserves":"Boyun eğme çekirdeğini korur."},"facet_ids":["F001"],"text":"uysalca boyun eğmek","usage_role":"contextual"}],"definition":"Bu dal, boyun eğme ve direnç göstermeden alçalma durumunu bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Boyun eğme ve direnç göstermeme bu dalın çekirdeğidir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yer ve konum dalının alanını getirir.","collision":"B002 ile karışır.","fit":"displacement","loses":"Boyun eğme ve alçalma çekirdeğini kaybettirir.","preserves":"Yüzeyde aynı kök ailesinden uzak çağrışım taşır."},"text":"yerleşme"}],"identity_rationale":"Kaynak anlatımı, bu dalı açık biçimde boyun eğme olarak verir. Bu tek çekirdek, üstlenme, yer ya da genel olma alanlarından bağımsızdır ve başka bir yapı gerektirmez.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"boyun eğme"}],"lexicalization_note":"Mekanik kapsam çıplak geldiği için tanım bağlı sözlerden bağımsız boyun eğme çekirdeğini verir.","neighbor_coverage_note":"Adaylar içinden yalnız boyun eğme alanındaki yakın sınırlar yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B004 kısa ve genel bir boyun eğme çekirdeğidir; komşu dal daha görünür tutum ve beden belirtileriyle genişler.","focus_only":"Bu dal yalın boyun eğme anlamıyla sınırlıdır.","gloss":"boyun eğme","neighbor_only":"Komşu dal başı eğme, sessizlik ve organların alçalması gibi davranış ayrıntılarını da taşır.","neighbor_ref":"root_000412/B001","relation_type":"near_synonym","shared_zone":"İkisi de alçalma ve boyun eğme alanında buluşur."},{"boundary_match":"partial","distinction":"B004 daha nötr bir eğilme çekirdeği verir; komşu dalda aşağılanma ve eziklik belirginleşir.","focus_only":"Bu dal sade boyun eğme bildirir.","gloss":"boyun eğme ve eziklik","neighbor_only":"Komşu dal aşağılanma, eziklik ve buna razı olma yönünü daha güçlü taşır.","neighbor_ref":"root_000419/B001","relation_type":"near_synonym","shared_zone":"İkisi de kişinin kendini alçaltması veya boyun eğmesi alanındadır."},{"boundary_match":"partial","distinction":"B004 çekirdek eylemi kısa tutar; komşu dal buyruğa uyma ve korku gibi ek koşullara açılabilir.","focus_only":"Bu dal yalnız boyun eğme çekirdeğini taşır.","gloss":"boyun eğme ile uyma","neighbor_only":"Komşu dal boyun eğmeye korku, buyruğa uyma ve düşkünlük tonları ekleyebilir.","neighbor_ref":"root_001594/B004","relation_type":"near_synonym","shared_zone":"İkisi de karşı koymadan eğilme alanında kesişir."},{"boundary_match":"partial","distinction":"B004 sadece eğilme durumudur; komşu dal bu eğilmeyi istek belirtme ve yardım dileme sahnesine taşır.","focus_only":"Bu dal boyun eğme durumunu bildirir.","gloss":"boyun eğme ile yakarma","neighbor_only":"Komşu dal ihtiyaç gösterme, yalvarma ve dilekte bulunma sahnesini de içerir.","neighbor_ref":"root_000908/B002","relation_type":"near_neighbor","shared_zone":"İkisi de kendini alçaltma alanını paylaşır."}],"source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak bildirimi dalı doğrudan boyun eğme olarak verir."}],"source_summary":"Bu dal tek bir kısa bildirimle boyun eğme anlamına bağlanır. Başka dallardaki yer, üstlenme veya olma kullanımları bu çekirdeğe taşınmaz."},"support_links":[]},{"boundary":"Dal, yaşlanan kişinin gençlik anılarını dile getirmesine dayalı nitelemeyle sınırlıdır.","branch_kind":"bare","branch_ref":"root_001332/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَانَ","morph_features":"STEM|POS:V|IMPF|LEM:kaAna|ROOT:kwn|SP:kaAn|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:4:2:1","qac_word_ref":"112:4:2","surface_ar":"يَكُن"}],"gloss":"gençliğini anan yaşlı kişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yaşlı kişiye geçmiş gençliğini anlatması yüzünden verilen ad çekirdektir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Niteleme, kişinin gençken şöyleydim diye söz etmesine bağlanır."}}],"root_ar":"ك و ن","root_id":"root_001332","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaşlılık ile geçmiş gençliği anma bağını birlikte vermek gerektiğinde uygundur.","boundary_detail":"Dal, yaşlanan kişinin gençlik anılarını dile getirmesine dayalı nitelemeyle sınırlıdır.","concept_gloss":"gençliğini anan yaşlı kişi","contextual_glosses":[{"applicability":"Kişi erkek olarak belirtildiğinde ve gençlikten söz etme yönü gerektiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaşlı kişi ve geçmiş gençlik anlatısı yönlerini korur."},"facet_ids":["F001","F002"],"text":"geçmişini anlatan yaşlı adam","usage_role":"contextual"},{"applicability":"Yalnız yaşlılık yönünün akıcı verilmesi gerektiğinde kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gençken şöyleydim diye söz etme bağını dışarıda bırakır.","preserves":"Yaşlanmış kişi yönünü korur."},"facet_ids":["F001"],"text":"yaşlı kişi","usage_role":"contextual"}],"definition":"Bu dal, yaşlanan kişiye gençliğinde nasıl olduğunu anlatmasına bağlanarak verilen nitelemeyi bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yaşlı kişiye geçmiş gençliğini anlatması yüzünden verilen ad çekirdektir."},{"facet_id":"F002","role":"associated_use","statement":"Niteleme, kişinin gençken şöyleydim diye söz etmesine bağlanır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Gerçek yaş durumunu tersine çevirir.","collision":"Yaşlılık komşularıyla karışır.","fit":"displacement","loses":"Yaşlı kişi çekirdeğini ve geçmişe dönük söz bağını siler.","preserves":"Gençlik sözünü yalnız yüzeysel olarak çağırır."},"text":"genç adam"}],"identity_rationale":"Kaynak anlatımı, yaşlanmış kişi için, gençken şöyleydim diye geçmişini anmasına bağlanan bir niteleme verir. Bu, genel yaşlılık adından çok belirli bir söz ve yaşlılık tasviri olduğu için ayrı dal olarak korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"gençken şöyleydim diye anlatan yaşlı kişi"}],"lexicalization_note":"Mekanik kapsam çıplak geldiği için tanım tek niteleme biçimini bağlı başka kullanımlara genişletmez.","neighbor_coverage_note":"Aday komşulardan yaş evresiyle doğrudan sınır kuranlar yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B005 genel yaşlılık değildir; yaşlı kişinin gençlik sözüne bağlanan özel addır. Komşu dal yaşlanmanın kendisini anlatır.","focus_only":"Bu dal yaşlı kişinin gençliğini anmasına dayalı özel nitelemedir.","gloss":"özel yaşlı nitelemesi","neighbor_only":"Komşu dal kadın veya erkek için genel yaşlanma ve eskime alanını taşır.","neighbor_ref":"root_000985/B003","relation_type":"near_neighbor","shared_zone":"İkisi de ileri yaş ve yaşlanmış kişi alanındadır."},{"boundary_match":"field_only","distinction":"Komşu dal yaşam evresini ve bedensel belirtiyi anlatır; B005 ise bu evredeki kişiye söz alışkanlığı üzerinden verilen addır.","focus_only":"Bu dal yaşlı kişinin geçmiş gençliğinden söz etmesine bağlıdır.","gloss":"yaşlılık nitelemesi","neighbor_only":"Komşu dal gençliği aşma, gücün tamamlanması ve saçta aklık belirmesi alanındadır.","neighbor_ref":"root_001326/B001","relation_type":"same_field","shared_zone":"İkisi de yaş evresiyle ilgilidir."},{"boundary_match":"field_only","distinction":"B005 ileri yaştaki kişiyi anlatır; komşu dal henüz yaşlılık değil, gençlikten çıkmış ara evredir.","focus_only":"Bu dal yaşlı kişiye bağlıdır.","gloss":"yaşlılık ile orta yaş","neighbor_only":"Komşu dal gençlik ile yaşlılık arasındaki orta evreyi anlatır.","neighbor_ref":"root_001511/B005","relation_type":"same_field","shared_zone":"İkisi de ömür evrelerini adlandırır."},{"boundary_match":"field_only","distinction":"B005 insana ve gençlik sözünü anmaya bağlı özel nitelemedir; komşu dal tür ve cinsiyet ayrımlarıyla yaşlı varlığı adlandırır.","focus_only":"Bu dal yaşlı kişinin gençlik sözünü merkeze alır.","gloss":"yaşlı kişi adları","neighbor_only":"Komşu dal yaşlı deve veya yaşlı kadın için ayrı adlar verir.","neighbor_ref":"root_001010/B006","relation_type":"same_field","shared_zone":"İkisi de yaşlı varlıkları adlandırma alanındadır."}],"source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak bildirimi nitelemeyi yaşlı kişinin gençlik sözüne bağlar."}],"source_summary":"Bu dal, yaşlanmış kişi için kullanılan özel bir nitelemeyi açıklar. Açıklama, kişinin gençliğine dönük kendi sözünü anmasına dayanır ve genel yaşlılık adlarıyla özdeş değildir."},"support_links":[]},{"boundary":"Dal yalnız kötü durum içinde gece geçirme deyişiyle sınırlıdır; genel hal veya bela adı değildir.","branch_kind":"collocation","branch_ref":"root_001332/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَانَ","morph_features":"STEM|POS:V|IMPF|LEM:kaAna|ROOT:kwn|SP:kaAn|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:4:2:1","qac_word_ref":"112:4:2","surface_ar":"يَكُن"}],"gloss":"kötü durumda gece geçirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin geceyi kötü bir durumda geçirmesi çekirdek kullanımdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Deyişteki durum adı olma kökünden yapılmış bir biçim olarak açıklanır."}}],"root_ar":"ك و ن","root_id":"root_001332","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bağlı deyişin bütün sınırını kısa biçimde verir.","boundary_detail":"Dal yalnız kötü durum içinde gece geçirme deyişiyle sınırlıdır; genel hal veya bela adı değildir.","concept_gloss":"kötü durumda gece geçirme","contextual_glosses":[{"applicability":"Deyişi akıcı Türkçe cümle içinde karşılamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geceyi kötü durumda geçirme çekirdeğini korur."},"facet_ids":["F001"],"text":"geceyi kötü halde geçirmek","usage_role":"contextual"},{"applicability":"Geceleme ayrıntısı bağlamdan belliyse daha kısa karşılık olarak kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Geceyi geçirme koşulunu açıkça söylemez.","preserves":"Kötü durumda bulunma yönünü korur."},"facet_ids":["F001"],"text":"kötü halde kalmak","usage_role":"contextual"}],"definition":"Bu dal, belirli deyiş içinde bir kişinin geceyi kötü bir durum içinde geçirmesini bildirir. Kullanılan durum adı olma kökünden kurulmuş sayılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin geceyi kötü bir durumda geçirmesi çekirdek kullanımdır."},{"facet_id":"F002","role":"source_variant","statement":"Deyişteki durum adı olma kökünden yapılmış bir biçim olarak açıklanır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Deyişe bağlı gece geçirme sınırının dışına taşan genel sıkıntı alanını getirir.","collision":"Kötü olay ve afet komşularıyla karışır.","fit":"broadening","loses":null,"preserves":"Kötülük ve sıkıntı çağrışımını korur."},"text":"bela"}],"identity_rationale":"Kaynak anlatımı, dalı belirli kötü-durum deyişiyle sınırlar ve kullanılan durum adını olma kökünden kurulmuş sayar. Bu nedenle anlam genel kötü hal adı ya da genel olma dalı değildir; geceyi kötü durumda geçirme sözünde kalır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"geceyi kötü durumda geçirmek"}],"lexicalization_note":"Mekanik kapsam bağlı söz verdiği için tanım yalnız bu deyişe bağlı kalır ve yalın kök anlamına genişlemez.","neighbor_coverage_note":"Adayların hepsi kontrol edildi; yayımlananlar kötü durum deyişiyle genel kötü hal komşularını ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B006 belirli deyişte gece geçirmeyi de ister; komşu dal daha yalın kötü durum adıdır.","focus_only":"Bu dal geceyi kötü durumda geçirme deyişiyle sınırlıdır.","gloss":"kötü durum","neighbor_only":"Komşu dal kötü durum adını geceleme koşulu olmadan verir.","neighbor_ref":"root_000185/B008","relation_type":"near_synonym","shared_zone":"İkisi de kötü hal veya sıkıntılı durum alanındadır."},{"boundary_match":"partial","distinction":"B006 belirli geceleme deyişidir; komşu dal kötü halin şiddetini ve uzun süren zor zamanları öne çıkarır.","focus_only":"Bu dal kötü durumda gece geçirmeyi anlatır.","gloss":"kötü hal ve şiddet","neighbor_only":"Komşu dal kötü durumun yanında şiddetli yıl veya kıtlık gibi süreli sıkıntıları da taşır.","neighbor_ref":"root_000321/B010","relation_type":"near_neighbor","shared_zone":"İkisi de kötü hal ve sıkıntı alanında kesişir."},{"boundary_match":"partial","distinction":"B006 durum içinde kalmayı verir; komşu dal dıştan gelen veya başa gelen büyük olayı merkez yapar.","focus_only":"Bu dal kişinin içinde bulunduğu kötü durumu anlatır.","gloss":"kötü hal ile kötü olay","neighbor_only":"Komşu dal kişiye gelen büyük kötü olay veya beklenmedik zarar alanındadır.","neighbor_ref":"root_000498/B001","relation_type":"near_neighbor","shared_zone":"İkisi de insanı üzen kötü durum çevresinde buluşur."},{"boundary_match":"partial","distinction":"B006 küçük ve deyişe bağlı bir kötü haldir; komşu dal çevreleyen kötü dönüş veya yenilgi gibi daha olaylı alanlara açılır.","focus_only":"Bu dal tek kişinin geceyi kötü durumda geçirmesine bağlıdır.","gloss":"kötü durum ve ters dönüş","neighbor_only":"Komşu dal yenilgi, ters dönen durum veya kuşatan kötü gidişi anlatır.","neighbor_ref":"root_000499/B004","relation_type":"near_neighbor","shared_zone":"Kötü hal anlatımında yakınlaşırlar."},{"boundary_match":"thematic_only","distinction":"B006, B001'in genel olma alanına çevrilmez; yalnız kötü durum içinde gece geçirme sözünde kalır.","focus_only":"Bu dal kötü durumda gece geçirme deyişidir.","gloss":"kötü durumda geceleme ile olma","neighbor_only":"Komşu dal genel olma, gerçekleşme ve olmanın bildirilmesidir.","neighbor_ref":"root_001332/B001","relation_type":"thematic","shared_zone":"Deyişteki durum adı olma kökünden açıklanır."}],"source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak bildirimi kullanımı kötü durumda gece geçirme deyişiyle sınırlar."}],"source_summary":"Bu dal tek bir kötü-durum deyişine bağlıdır. Kaynak anlatımı, kişinin geceyi kötü bir durumda geçirmesini ve deyişteki durum adının olma kökünden açıklanmasını birlikte verir."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["112:4:1"],"branch_refs":[],"candidate_id":"cand_276e82429016e197f170","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:1:connector-negator-sound","source_type":"word_analysis","support_ids":["sup_07b339a4c967b4d256bf","sup_ff869008c1838ecbe84c"],"title":"bound connector repeats the negation sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:1","qac_refs":["112:4:1:1"],"status":"accepted"}},{"anchor_refs":["112:4:1"],"branch_refs":[],"candidate_id":"cand_4d023a88fdfd92fe02c7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:1:coordinated-final-negation","source_type":"word_analysis","support_ids":["sup_c192c0b647d849d32ad8","sup_ff869008c1838ecbe84c"],"title":"connector joins the final denial","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:1","qac_refs":["112:4:1:1"],"status":"accepted"}},{"anchor_refs":["112:4:1"],"branch_refs":[],"candidate_id":"cand_26c98bd799969c3d766c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:1:dual-backward-reach","source_type":"word_analysis","support_ids":["sup_a94b36516d236481f0c4","sup_ff869008c1838ecbe84c"],"title":"continuation and seal both remain audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:1","qac_refs":["112:4:1:1"],"status":"accepted"}},{"anchor_refs":["112:4:2"],"branch_refs":[],"candidate_id":"cand_2b8dc6552886e84400e1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:2:clipped-negation-rhythm","source_type":"word_analysis","support_ids":["sup_2888342aee26bec046a1","sup_3613b004c1628ed6ff7a"],"title":"closed particle tightens the cadence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:2","qac_refs":["112:4:1:2"],"status":"accepted"}},{"anchor_refs":["112:4:2"],"branch_refs":[],"candidate_id":"cand_d789f6e2a5bb9256a221","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:2:jussive-governance","source_type":"word_analysis","support_ids":["sup_2888342aee26bec046a1","sup_3d14509a3e072ecf2d58"],"title":"the verb enters under governance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:2","qac_refs":["112:4:1:2"],"status":"accepted"}},{"anchor_refs":["112:4:2"],"branch_refs":[],"candidate_id":"cand_a3c58ef5fd8c7b860dfc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:2:negative-triad","source_type":"word_analysis","support_ids":["sup_18a8b920d0827a9b566e","sup_2888342aee26bec046a1"],"title":"third negation expands the series","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:2","qac_refs":["112:4:1:2"],"status":"accepted"}},{"anchor_refs":["112:4:2"],"branch_refs":[],"candidate_id":"cand_23ec7de5654fc90974eb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:2:whole-clause-negation","source_type":"word_analysis","support_ids":["sup_2888342aee26bec046a1","sup_4fd072f763a3fbe3d0ff"],"title":"negation covers the whole clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:2","qac_refs":["112:4:1:2"],"status":"accepted"}},{"anchor_refs":["112:4:3"],"branch_refs":[],"candidate_id":"cand_662b43aee1f70e46923c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001332"],"scope":"focus_ayah","source_local_id":"112:4:3:copular-frame","source_type":"word_analysis","support_ids":["sup_29d4f70510c1a57efdc0","sup_cf84004e4e63e65404a9"],"title":"verb opens a required predicate-subject frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:3","qac_refs":["112:4:2:1"],"status":"accepted"}},{"anchor_refs":["112:4:3"],"branch_refs":[],"candidate_id":"cand_be4f51ee08debca23911","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001332"],"scope":"focus_ayah","source_local_id":"112:4:3:creative-command-contrast","source_type":"word_analysis","support_ids":["sup_12fb440ebad308c7ae5a","sup_cf84004e4e63e65404a9"],"title":"creative being is reversed into denial","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:3","qac_refs":["112:4:2:1"],"status":"accepted"}},{"anchor_refs":["112:4:3"],"branch_refs":[],"candidate_id":"cand_9226186bc30a73133a1a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001332"],"scope":"focus_ayah","source_local_id":"112:4:3:divine-relation-formula","source_type":"word_analysis","support_ids":["sup_75c93d2487be2b911a9a","sup_cf84004e4e63e65404a9"],"title":"formula targets equivalence here","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:3","qac_refs":["112:4:2:1"],"status":"accepted"}},{"anchor_refs":["112:4:3"],"branch_refs":[],"candidate_id":"cand_259ea5dcef3b4dcb8539","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001332"],"scope":"focus_ayah","source_local_id":"112:4:3:existence-root-denial","source_type":"word_analysis","support_ids":["sup_2112f2dba4d1ccb5fd2f","sup_cf84004e4e63e65404a9"],"title":"the being-root denies any equal's obtaining","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:3","qac_refs":["112:4:2:1"],"status":"accepted"}},{"anchor_refs":["112:4:3"],"branch_refs":[],"candidate_id":"cand_a1db3bf87a418898a03f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001332"],"scope":"focus_ayah","source_local_id":"112:4:3:jussive-negated-form","source_type":"word_analysis","support_ids":["sup_8890c8bf136fe52f53b5","sup_cf84004e4e63e65404a9"],"title":"negation clips the verb form","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:3","qac_refs":["112:4:2:1"],"status":"accepted"}},{"anchor_refs":["112:4:3"],"branch_refs":[],"candidate_id":"cand_5ff7493c48fc0845a4cc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001332"],"scope":"focus_ayah","source_local_id":"112:4:3:place-standing-pressure","source_type":"word_analysis","support_ids":["sup_423865157885c82de4cc","sup_cf84004e4e63e65404a9"],"title":"no standing for equivalence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:3","qac_refs":["112:4:2:1"],"status":"accepted"}},{"anchor_refs":["112:4:3"],"branch_refs":[],"candidate_id":"cand_29e0d2cef17cb739928d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001332"],"scope":"focus_ayah","source_local_id":"112:4:3:root-pair-boundary","source_type":"word_analysis","support_ids":["sup_0cea2a29fb2b4b6e54dc","sup_cf84004e4e63e65404a9"],"title":"existence pairs with not-one","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:3","qac_refs":["112:4:2:1"],"status":"accepted"}},{"anchor_refs":["112:4:4"],"branch_refs":[],"candidate_id":"cand_b525cc8dfd0f25c99e73","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:4:attachment-emphasis-narrowed","source_type":"word_analysis","support_ids":["sup_2decd88c9d2feda98d62","sup_4494c5dced7c238a45a8"],"title":"attachment variation shifts emphasis, not the core parse","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:4","qac_refs":["112:4:3:1"],"status":"accepted"}},{"anchor_refs":["112:4:4"],"branch_refs":[],"candidate_id":"cand_04dfea87d3d2a209c51e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:4:bound-prepositional-unit","source_type":"word_analysis","support_ids":["sup_2decd88c9d2feda98d62","sup_595d1d1c7acd8f0059cd"],"title":"preposition and pronoun arrive as one unit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:4","qac_refs":["112:4:3:1"],"status":"accepted"}},{"anchor_refs":["112:4:4"],"branch_refs":[],"candidate_id":"cand_0201275e7600c8b08db9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:4:boundary-pronoun-surfacing","source_type":"word_analysis","support_ids":["sup_2decd88c9d2feda98d62","sup_ceb3ab0497403b4a25da"],"title":"hidden subject becomes explicit suffix","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:4","qac_refs":["112:4:3:1"],"status":"accepted"}},{"anchor_refs":["112:4:4"],"branch_refs":[],"candidate_id":"cand_4edfa7093e0a5e9a2637","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:4:divine-pronoun-resumption","source_type":"word_analysis","support_ids":["sup_2decd88c9d2feda98d62","sup_4c71bd22664b0e10af79"],"title":"suffix resumes the established referent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:4","qac_refs":["112:4:3:1"],"status":"accepted"}},{"anchor_refs":["112:4:4"],"branch_refs":[],"candidate_id":"cand_dde9b82d31bc5e03390f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:4:fixed-comparison-standard","source_type":"word_analysis","support_ids":["sup_2decd88c9d2feda98d62","sup_7f5d187ae86232a2af18"],"title":"the standard is fixed before the candidate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:4","qac_refs":["112:4:3:1"],"status":"accepted"}},{"anchor_refs":["112:4:4"],"branch_refs":[],"candidate_id":"cand_ad7af762e6237c719742","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:4:variant-reordering-apparatus","source_type":"word_analysis","support_ids":["sup_2decd88c9d2feda98d62","sup_e0f699d1abbf164bfea3"],"title":"reordered variants expose movable emphasis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:4","qac_refs":["112:4:3:1"],"status":"accepted"}},{"anchor_refs":["112:4:5"],"branch_refs":[],"candidate_id":"cand_c0be3fbb0158d8a10b52","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:5:comparison-standard","source_type":"word_analysis","support_ids":["sup_6100310057837c0158c1","sup_b0b8e271d4db8acefb11"],"title":"the pronoun supplies the standard","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:5","qac_refs":["112:4:4:1"],"status":"accepted"}},{"anchor_refs":["112:4:5"],"branch_refs":[],"candidate_id":"cand_dda105eab1e3ac58d462","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:5:delayed-candidate-reveal","source_type":"word_analysis","support_ids":["sup_6100310057837c0158c1","sup_cf6be40c9f4adf7c8b44"],"title":"predicate comes before the candidate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:5","qac_refs":["112:4:4:1"],"status":"accepted"}},{"anchor_refs":["112:4:5"],"branch_refs":[],"candidate_id":"cand_8fee8841498ac63af81c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:5:formula-contrast-17-111","source_type":"word_analysis","support_ids":["sup_076b2a1736771a644f90","sup_6100310057837c0158c1"],"title":"formula is specialized toward equivalence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:5","qac_refs":["112:4:4:1"],"status":"accepted"}},{"anchor_refs":["112:4:5"],"branch_refs":[],"candidate_id":"cand_0d9a866e975cdf7f5a32","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:5:genealogical-to-equivalence-boundary","source_type":"word_analysis","support_ids":["sup_6100310057837c0158c1","sup_db937d453012714b410a"],"title":"genealogical denial widens into peer denial","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:5","qac_refs":["112:4:4:1"],"status":"accepted"}},{"anchor_refs":["112:4:5"],"branch_refs":[],"candidate_id":"cand_60c691fdf6acba3b8a7b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:5:hapax-burden","source_type":"word_analysis","support_ids":["sup_6100310057837c0158c1","sup_a95cab956b62d6325c05"],"title":"single occurrence carries the denial","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:5","qac_refs":["112:4:4:1"],"status":"accepted"}},{"anchor_refs":["112:4:5"],"branch_refs":[],"candidate_id":"cand_8aa72f0a008a7b870aeb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:5:overturning-image-narrowed","source_type":"word_analysis","support_ids":["sup_6100310057837c0158c1","sup_a4af6330edde776ed097"],"title":"overturned balance remains secondary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:5","qac_refs":["112:4:4:1"],"status":"accepted"}},{"anchor_refs":["112:4:5"],"branch_refs":[],"candidate_id":"cand_08ef777455fe5cd77030","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:5:predicate-equivalence-denial","source_type":"word_analysis","support_ids":["sup_6100310057837c0158c1","sup_ddf4acb6d08b0b171555"],"title":"equivalence is the denied predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:5","qac_refs":["112:4:4:1"],"status":"accepted"}},{"anchor_refs":["112:4:5"],"branch_refs":[],"candidate_id":"cand_d85af745369467d38664","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:5:predicate-subject-cadence","source_type":"word_analysis","support_ids":["sup_543f76d1bb30ec3f00a2","sup_6100310057837c0158c1"],"title":"paired indefinite nouns close together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:5","qac_refs":["112:4:4:1"],"status":"accepted"}},{"anchor_refs":["112:4:5"],"branch_refs":[],"candidate_id":"cand_0aff2180f731fa67bcf9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:5:root-family-parity","source_type":"word_analysis","support_ids":["sup_590ccdd18ea5a64bd10b","sup_6100310057837c0158c1"],"title":"root family sharpens peerhood","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:5","qac_refs":["112:4:4:1"],"status":"accepted"}},{"anchor_refs":["112:4:5"],"branch_refs":[],"candidate_id":"cand_bbe5b3d51e8cf9a30838","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:5:unbounded-indefinite-parity","source_type":"word_analysis","support_ids":["sup_6100310057837c0158c1","sup_6da3596245afc2cba235"],"title":"indefiniteness makes parity unbounded","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:5","qac_refs":["112:4:4:1"],"status":"accepted"}},{"anchor_refs":["112:4:5"],"branch_refs":[],"candidate_id":"cand_9e04566ec55a977b4bb9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:5:variant-form-pressure","source_type":"word_analysis","support_ids":["sup_6100310057837c0158c1","sup_f4d994a5a446163b3769"],"title":"variant forms adjust sound and abstraction","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:5","qac_refs":["112:4:4:1"],"status":"accepted"}},{"anchor_refs":["112:4:6"],"branch_refs":[],"candidate_id":"cand_bcfbf283f888a2d8532e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:6:delayed-subject-role","source_type":"word_analysis","support_ids":["sup_50719f0abdcbe16c3dc4","sup_5a6b4f3d5f7b51402582"],"title":"final word is the delayed subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:6","qac_refs":["112:4:5:1"],"status":"accepted"}},{"anchor_refs":["112:4:6"],"branch_refs":[],"candidate_id":"cand_47b540f47bbc051a2392","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:6:existence-root-pair","source_type":"word_analysis","support_ids":["sup_50719f0abdcbe16c3dc4","sup_bf66ef49f0f0a05ca36a"],"title":"being and not-one form the local mechanism","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:6","qac_refs":["112:4:5:1"],"status":"accepted"}},{"anchor_refs":["112:4:6"],"branch_refs":[],"candidate_id":"cand_59be1127937699932b94","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:6:final-cadence","source_type":"word_analysis","support_ids":["sup_50719f0abdcbe16c3dc4","sup_f67b6bee6c0c4ca9a5b5"],"title":"final sound binds and denies the pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:6","qac_refs":["112:4:5:1"],"status":"accepted"}},{"anchor_refs":["112:4:6"],"branch_refs":[],"candidate_id":"cand_05d07727646baf3907c2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:6:form-shift-opening-closing","source_type":"word_analysis","support_ids":["sup_02f11539b37fb9897902","sup_50719f0abdcbe16c3dc4"],"title":"form shift turns attribute into candidate class","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:6","qac_refs":["112:4:5:1"],"status":"accepted"}},{"anchor_refs":["112:4:6"],"branch_refs":[],"candidate_id":"cand_622e1a0cea42447c82e5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:6:negative-polarity-anyone","source_type":"word_analysis","support_ids":["sup_2755f8f375a18b981330","sup_50719f0abdcbe16c3dc4"],"title":"indefinite subject excludes every candidate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:6","qac_refs":["112:4:5:1"],"status":"accepted"}},{"anchor_refs":["112:4:6"],"branch_refs":[],"candidate_id":"cand_c2cfebe056e05b11a740","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:6:non-counting-unicity-pressure","source_type":"word_analysis","support_ids":["sup_50719f0abdcbe16c3dc4","sup_62f80c90e353b6973ea8"],"title":"not one blocks a countable peer series","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:6","qac_refs":["112:4:5:1"],"status":"accepted"}},{"anchor_refs":["112:4:6"],"branch_refs":[],"candidate_id":"cand_e8233cffb362af9c1445","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:6:opening-root-return","source_type":"word_analysis","support_ids":["sup_50719f0abdcbe16c3dc4","sup_846af69d8c85792ded26"],"title":"opening oneness returns as final exclusion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:6","qac_refs":["112:4:5:1"],"status":"accepted"}},{"anchor_refs":["112:4:6"],"branch_refs":[],"candidate_id":"cand_75d98cf09dd5cfe5c500","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:6:variant-final-placement","source_type":"word_analysis","support_ids":["sup_50719f0abdcbe16c3dc4","sup_b029b0359a6fa87f9ffc"],"title":"variant order highlights final placement","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:6","qac_refs":["112:4:5:1"],"status":"accepted"}},{"anchor_refs":["112:4:2"],"branch_refs":[],"candidate_id":"cand_ab5ed650425cc63ca195","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001332"],"scope":"focus_ayah","source_local_id":"112:4:2:1","source_type":"qac_morpheme","support_ids":["sup_49e858eae6e42567aa3b"],"title":"QAC root occurrence: ك و ن","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["112:4:4"],"branch_refs":[],"candidate_id":"cand_6b6d57091b1942e4ea63","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001305"],"scope":"focus_ayah","source_local_id":"112:4:4:1","source_type":"qac_morpheme","support_ids":["sup_e9c208f5b7548891677d"],"title":"QAC root occurrence: ك ف ء","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["112:4:5"],"branch_refs":[],"candidate_id":"cand_769650bb069b89399d3f","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000017"],"scope":"focus_ayah","source_local_id":"112:4:5:1","source_type":"qac_morpheme","support_ids":["sup_dbe32e52256a97b35f1a"],"title":"QAC root occurrence: ء ح د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["112:4:5"],"branch_refs":[],"candidate_id":"cand_3f3b667d50bdd5320aea","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"112:4:5:hal-reading-rejected","source_type":"word_analysis","support_ids":["sup_13f91c28d04c1da35682","sup_6100310057837c0158c1"],"title":"circumstantial reading is blocked locally","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"112:4:5","qac_refs":["112:4:4:1"],"status":"accepted"}},{"anchor_refs":["112:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:4","branch_refs":["root_000017/B002","root_001305/B001","root_001332/B001"],"candidate_id":"cand_acbf995d107174207efd","commentary_obligation":"review","hft_ref":"hft_818b57d77760fc573fb2","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_exhaustive_counterpart_noninstantiation","source_type":"hft","support_ids":["sup_c22e2afcdd54078053f2"],"title":"baseline_exhaustive_counterpart_noninstantiation","trust":"legacy_unbound"},{"anchor_refs":["112:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:4","branch_refs":["root_000017/B002","root_001305/B001","root_001332/B002"],"candidate_id":"cand_2dadd5d457a2a8844e4e","commentary_obligation":"review","hft_ref":"hft_d940329cb021310bc4a5","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_no_comparable_station","source_type":"hft","support_ids":["sup_8b63b4d4bf8d151a57c1"],"title":"baseline_no_comparable_station","trust":"legacy_unbound"},{"anchor_refs":["112:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:4","branch_refs":["root_000017/B002","root_001305/B002","root_001332/B001"],"candidate_id":"cand_3143897e5b81be86df74","commentary_obligation":"review","hft_ref":"hft_ff8ef9105889086490ec","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_no_overturning_counterforce","source_type":"hft","support_ids":["sup_8dab2f8db81abb1c6df8"],"title":"baseline_no_overturning_counterforce","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"112:4:1:1","qac_word_ref":"112:4:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لَم","morph_features":"STEM|POS:NEG|LEM:lam","morpheme_role":"STEM","pos":"NEG","qac_ref":"112:4:1:2","qac_word_ref":"112:4:1","root_ar":"","surface_ar":"لَمْ"},{"lemma_ar":"كَانَ","morph_features":"STEM|POS:V|IMPF|LEM:kaAna|ROOT:kwn|SP:kaAn|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:4:2:1","qac_word_ref":"112:4:2","root_ar":"ك و ن","surface_ar":"يَكُن"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"112:4:3:1","qac_word_ref":"112:4:3","root_ar":"","surface_ar":"لَّ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|3MS","morpheme_role":"STEM","pos":"PRON","qac_ref":"112:4:3:2","qac_word_ref":"112:4:3","root_ar":"","surface_ar":"هُۥ"},{"lemma_ar":"كُفُو","morph_features":"STEM|POS:N|LEM:kufuw|ROOT:kfA|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"112:4:4:1","qac_word_ref":"112:4:4","root_ar":"ك ف ء","surface_ar":"كُفُوًا"},{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:4:5:1","qac_word_ref":"112:4:5","root_ar":"ء ح د","surface_ar":"أَحَدٌۢ"}],"word_analysis_qac_refs":[["112:4:1:1"],["112:4:1:2"],["112:4:2:1"],["112:4:3:1"],["112:4:4:1"],["112:4:5:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["112:4:1","112:4:2","112:4:3","112:4:4","112:4:5","112:4:6"]},"focus_surface_evidence":{"arabic_uthmani":"وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"112:4:1:1","qac_word_ref":"112:4:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لَم","morph_features":"STEM|POS:NEG|LEM:lam","morpheme_role":"STEM","pos":"NEG","qac_ref":"112:4:1:2","qac_word_ref":"112:4:1","root_ar":"","surface_ar":"لَمْ"},{"lemma_ar":"كَانَ","morph_features":"STEM|POS:V|IMPF|LEM:kaAna|ROOT:kwn|SP:kaAn|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:4:2:1","qac_word_ref":"112:4:2","root_ar":"ك و ن","surface_ar":"يَكُن"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"112:4:3:1","qac_word_ref":"112:4:3","root_ar":"","surface_ar":"لَّ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|3MS","morpheme_role":"STEM","pos":"PRON","qac_ref":"112:4:3:2","qac_word_ref":"112:4:3","root_ar":"","surface_ar":"هُۥ"},{"lemma_ar":"كُفُو","morph_features":"STEM|POS:N|LEM:kufuw|ROOT:kfA|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"112:4:4:1","qac_word_ref":"112:4:4","root_ar":"ك ف ء","surface_ar":"كُفُوًا"},{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:4:5:1","qac_word_ref":"112:4:5","root_ar":"ء ح د","surface_ar":"أَحَدٌۢ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["112:4:1:1"],["112:4:1:2"],["112:4:2:1"],["112:4:3:1"],["112:4:4:1"],["112:4:5:1"]],"word_analysis_refs":["112:4:1","112:4:2","112:4:3","112:4:4","112:4:5","112:4:6"],"word_rows":[{"analysis_record_ref":"112:4:1","analytic_gloss_range_en":"coordinating connector that joins the whole final negated clause to the prior negation chain","analytic_root_gloss_range_en":null,"qac_refs":["112:4:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"112:4:2","analytic_gloss_range_en":"governing negation particle with full-clause scope and past-continuing force","analytic_root_gloss_range_en":null,"qac_refs":["112:4:1:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَمْ","transliteration":"lam"}},{"analysis_record_ref":"112:4:3","analytic_gloss_range_en":"negated jussive copular/existential verb requiring a predicate and delayed subject","analytic_root_gloss_range_en":"being, occurrence, and predication are locally active; place or standing can be a narrowed family pressure, while suretyship, humbling, idiom, and bad-condition branches are not locally activated","qac_refs":["112:4:2:1"],"root":{"arabic":"ك و ن","transliteration":"k-w-n"},"surface":{"arabic":"يَكُنْ","transliteration":"yakun"}},{"analysis_record_ref":"112:4:4","analytic_gloss_range_en":"prepositional-pronominal unit fixing the divine referent as the comparison standard and relation target","analytic_root_gloss_range_en":null,"qac_refs":["112:4:3:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَّهُۥ","transliteration":"lahu"}},{"analysis_record_ref":"112:4:5","analytic_gloss_range_en":"accusative indefinite predicate denying any peer, counterpart, or relation of full equivalence to Him","analytic_root_gloss_range_en":"equality, matching, peerhood, parity, and reciprocal correspondence are relevant; secondary overturning imagery is only narrowed background pressure","qac_refs":["112:4:4:1"],"root":{"arabic":"ك ف أ","transliteration":"k-f-ʾ"},"surface":{"arabic":"كُفُوًا","transliteration":"kufuwan"}},{"analysis_record_ref":"112:4:6","analytic_gloss_range_en":"indefinite nominative delayed subject meaning not one, no one, not anyone under the negated copular frame","analytic_root_gloss_range_en":"oneness and anyone/no-one polarity are both relevant locally; the final word converts the surah's opening unicity root into universal exclusion of any equal","qac_refs":["112:4:5:1"],"root":{"arabic":"أ ح د","transliteration":"ʾ-ḥ-d"},"surface":{"arabic":"أَحَدٌۢ","transliteration":"ahadun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":6,"words_total":6,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["112:4"],"branch_refs":["root_000017/B002","root_001305/B001","root_001332/B001"],"candidate_id":"cand_acbf995d107174207efd","evidence_scope":"focus_ayah","hft_ref":"hft_818b57d77760fc573fb2","item_id":"baseline_exhaustive_counterpart_noninstantiation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_exhaustive_counterpart_noninstantiation","support_id":"sup_c22e2afcdd54078053f2"},{"anchor_refs":["112:4"],"branch_refs":["root_000017/B002","root_001305/B001","root_001332/B002"],"candidate_id":"cand_2dadd5d457a2a8844e4e","evidence_scope":"focus_ayah","hft_ref":"hft_d940329cb021310bc4a5","item_id":"baseline_no_comparable_station","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_no_comparable_station","support_id":"sup_8b63b4d4bf8d151a57c1"},{"anchor_refs":["112:4"],"branch_refs":["root_000017/B002","root_001305/B002","root_001332/B001"],"candidate_id":"cand_3143897e5b81be86df74","evidence_scope":"focus_ayah","hft_ref":"hft_ff8ef9105889086490ec","item_id":"baseline_no_overturning_counterforce","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_no_overturning_counterforce","support_id":"sup_8dab2f8db81abb1c6df8"}],"diagnostics":[],"lane_counts":{"global":8,"macro":9,"micro":3},"packet_summary":{"ayah_count":4,"focus_ref":"112:4","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]}],"window":["112:1","112:2","112:3","112:4"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"112:4","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":12,"unstructured_record_count":0},"identity":{"ayah_ref":"112:4","lane":"micro","linguistic_source_ref":"112:4","surface_ref":"112:4","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"112:4","target_tokens":[["Ve",["112:4:1"]],["hiç",["112:4:1","112:4:5"]],["kimse",["112:4:5"]],["O'na",["112:4:3"]],["denk",["112:4:4"]],["olmamıştır",["112:4:1","112:4:2"]]],"text":"Ve hiç kimse O'na denk olmamıştır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":4,"id":"s112-p01-001-004","label":"Whole surah","number":1,"refs":["112:1","112:2","112:3","112:4"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:6:form-shift-opening-closing","source_type":"word_analysis","support_id":"sup_02f11539b37fb9897902","text":"{\"blocking_evidence\":null,\"headline\":\"form shift turns attribute into candidate class\",\"reader_payoff\":\"The reader notices that the same root moves from an affirmed divine attribute at the opening to an indefinite negated subject class at the close.\",\"reason\":\"The local form is indefinite nominative under negation, unlike the opening use in 112:1 where the same root bears the surah's affirmed uniqueness claim.\",\"representative_source_ids\":[\"QF-ce4a73f1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:5:formula-contrast-17-111","source_type":"word_analysis","support_id":"sup_076b2a1736771a644f90","text":"{\"blocking_evidence\":null,\"headline\":\"formula is specialized toward equivalence\",\"reader_payoff\":\"The reader notices that the same kind of divine-relation denial frame can exclude different relation nouns, and here the excluded relation is equivalence itself.\",\"reason\":\"The CRITICAL rows provide the concrete contrast with 17:111, where partnership and protective need are denied; 112:4 fills the relation slot with {{ar:كُفُوًا}} ({{tr:kufuwan}}).\",\"representative_source_ids\":[\"QI-4ca6dc60\",\"QI-68568d23\",\"QE-eb3a24f6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:1:connector-negator-sound","source_type":"word_analysis","support_id":"sup_07b339a4c967b4d256bf","text":"{\"blocking_evidence\":null,\"headline\":\"bound connector repeats the negation sound\",\"reader_payoff\":\"The reader hears the connector and negator as one compact opening beat that resumes the sound pattern of the previous denials.\",\"reason\":\"The written and recited sequence binds {{ar:وَ}} ({{tr:wa}}) directly to {{ar:لَمْ}} ({{tr:lam}}), matching the repeated negation thread across 112:3-4.\",\"representative_source_ids\":[\"QF-66313d07\",\"QP-fd569272\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:3:root-pair-boundary","source_type":"word_analysis","support_id":"sup_0cea2a29fb2b4b6e54dc","text":"{\"blocking_evidence\":null,\"headline\":\"existence pairs with not-one\",\"reader_payoff\":\"The reader notices the boundary shift from denied generation to denied existence of any candidate equal.\",\"reason\":\"The local clause pairs {{ar:يَكُنْ}} ({{tr:yakun}}) with the delayed subject {{ar:أَحَدٌۢ}} ({{tr:ahadun}}), and the boundary rows correctly identify a move from genealogy to existential comparison.\",\"representative_source_ids\":[\"QI-ede28684\",\"QB-b0efe889\",\"QB-cccd6530\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:3:creative-command-contrast","source_type":"word_analysis","support_id":"sup_12fb440ebad308c7ae5a","text":"{\"blocking_evidence\":null,\"headline\":\"creative being is reversed into denial\",\"reader_payoff\":\"The reader notices the contrast between the root's wider association with bringing-to-be and this local use denying any equal's being.\",\"reason\":\"The contrast is meaningful at root-family level, but the local surface is the jussive imperfect {{ar:يَكُنْ}} ({{tr:yakun}}), not the imperative {{ar:كُنْ}} ({{tr:kun}}).\",\"representative_source_ids\":[\"QF-863fbd47\",\"MI-7df9217d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:5:hal-reading-rejected","source_type":"word_analysis","support_id":"sup_13f91c28d04c1da35682","text":"{\"blocking_evidence\":\"Attachment evidence marks {{ar:كُفُوًا}} ({{tr:kufuwan}}) as the accusative predicate of {{ar:يَكُنْ}} ({{tr:yakun}}), while {{ar:أَحَدٌۢ}} ({{tr:ahadun}}) is the delayed subject.\",\"headline\":\"circumstantial reading is blocked locally\",\"reader_payoff\":null,\"reason\":\"The alternative circumstantial analysis would make {{ar:لَّهُۥ}} ({{tr:lahu}}) carry the main predicate force, but the provided attachment guardrail syntactically forces {{ar:كُفُوًا}} ({{tr:kufuwan}}) as predicate.\",\"representative_source_ids\":[\"QG-f9211477\"],\"status\":\"rejected\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:2:negative-triad","source_type":"word_analysis","support_id":"sup_18a8b920d0827a9b566e","text":"{\"blocking_evidence\":null,\"headline\":\"third negation expands the series\",\"reader_payoff\":\"The reader notices the third negative beat carrying the surah from denied birth-relations into denied peerhood.\",\"reason\":\"The connector and QAC grammar place this particle in the same coordinated negation sequence as the two denials in 112:3.\",\"representative_source_ids\":[\"MG-b5589eaa\",\"QS-d6c8dc9c\",\"QT-5436106d\",\"QE-5cd5acca\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:3:existence-root-denial","source_type":"word_analysis","support_id":"sup_2112f2dba4d1ccb5fd2f","text":"{\"blocking_evidence\":null,\"headline\":\"the being-root denies any equal's obtaining\",\"reader_payoff\":\"The reader notices the force of using the basic being-root to say that no comparable being ever obtains.\",\"reason\":\"V4 supports the local branch of being, occurrence, and predication for {{ar:ك و ن}} ({{tr:k-w-n}}), and contextual valency shows this form overwhelmingly functioning in copular frames.\",\"representative_source_ids\":[\"QS-6c259ad1\",\"QS-c6fbc3a4\",\"QS-d279f14b\",\"QI-16e25c81\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:6:negative-polarity-anyone","source_type":"word_analysis","support_id":"sup_2755f8f375a18b981330","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite subject excludes every candidate\",\"reader_payoff\":\"The reader notices that the final noun does not leave the subject vague; under negation it empties the candidate set completely.\",\"reason\":\"QAC explicitly gives the negative-context sense as not one, no one, or not anyone, and contextual polarity marks this form as a negative-polarity item.\",\"representative_source_ids\":[\"QG-fd845e07\",\"QS-079bd0e9\",\"QS-8f764315\",\"QF-c041b4f5\",\"QI-e1190abc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:2","source_type":"word_analysis","support_id":"sup_2888342aee26bec046a1","text":"{\"gloss_range\":\"governing negation particle with full-clause scope and past-continuing force\",\"prose\":\"{{ar:لَمْ}} ({{tr:lam}}) governs {{ar:يَكُنْ}} ({{tr:yakun}}) and scopes over the whole copular clause, not just over the verb or the equality noun. That makes the denial a full existential-equivalence denial: no candidate has ever stood in the relation expressed by {{ar:كُفُوًا}} ({{tr:kufuwan}}) to Him, and the past-continuing force keeps that absence from being only momentary. The same negative particle also completes the repeated pattern from 112:3 into 112:4, extending the sequence from denied generation to denied comparison. Its closed sound before the clipped verb gives the final denial a compact beat.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَمْ}} ({{tr:lam}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:3:copular-frame","source_type":"word_analysis","support_id":"sup_29d4f70510c1a57efdc0","text":"{\"blocking_evidence\":null,\"headline\":\"verb opens a required predicate-subject frame\",\"reader_payoff\":\"The reader notices that the verb creates a frame waiting for predicate and subject, so the remaining words are syntactically bound into one denied existence claim.\",\"reason\":\"Attachment evidence marks {{ar:يَكُنْ}} ({{tr:yakun}}) as the head of a negated copular clause with {{ar:كُفُوًا}} ({{tr:kufuwan}}) as predicate and {{ar:أَحَدٌۢ}} ({{tr:ahadun}}) as subject.\",\"representative_source_ids\":[\"QG-00898fa6\",\"QT-c60b76a6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:4","source_type":"word_analysis","support_id":"sup_2decd88c9d2feda98d62","text":"{\"gloss_range\":\"prepositional-pronominal unit fixing the divine referent as the comparison standard and relation target\",\"prose\":\"{{ar:لَّهُۥ}} ({{tr:lahu}}) brings the established divine referent into the comparison without repeating the name. The suffix points back to the divine name in 112:1-2, so the final clause keeps one subject in view while shifting from affirmation to denied relation. Across the boundary, what had been implicit in the prior negated verbs surfaces here as an attached pronoun anchoring the final comparison. As a single bound preposition-plus-pronoun unit, it makes the relation target arrive compactly as for Him or to Him. Placed before {{ar:كُفُوًا}} ({{tr:kufuwan}}) and {{ar:أَحَدٌۢ}} ({{tr:ahadun}}), the phrase fixes the standard before any possible candidate is named: the denied equal would have to be equal to Him. The attachment evidence most strongly links the pronoun phrase to the equality noun, so broader attachment claims survive only as a local ambiguity of affected-party versus comparison-standard emphasis, not as a replacement for the predicate analysis. Reordered variants are kept as apparatus for movable emphasis, while the received order foregrounds the standard before equality and subject.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَّهُۥ}} ({{tr:lahu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:2:clipped-negation-rhythm","source_type":"word_analysis","support_id":"sup_3613b004c1628ed6ff7a","text":"{\"blocking_evidence\":null,\"headline\":\"closed particle tightens the cadence\",\"reader_payoff\":\"The reader hears a short closed negation beat that groups the final clause with the earlier compact denials.\",\"reason\":\"The surface particle closes before the jussive verb, matching the compressed negative rhythm of the surrounding sequence.\",\"representative_source_ids\":[\"QF-7c4c4d00\",\"QP-005ec461\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:2:jussive-governance","source_type":"word_analysis","support_id":"sup_3d14509a3e072ecf2d58","text":"{\"blocking_evidence\":null,\"headline\":\"the verb enters under governance\",\"reader_payoff\":\"The reader sees that the form of the following verb is grammatically shaped by negation before the predicate and subject appear.\",\"reason\":\"QAC and attachment evidence both identify {{ar:يَكُنْ}} ({{tr:yakun}}) as the jussive/apocopated imperfect governed by {{ar:لَمْ}} ({{tr:lam}}).\",\"representative_source_ids\":[\"QG-842e6985\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:3:place-standing-pressure","source_type":"word_analysis","support_id":"sup_423865157885c82de4cc","text":"{\"blocking_evidence\":null,\"headline\":\"no standing for equivalence\",\"reader_payoff\":\"The reader notices a secondary pressure that no peer has even a place or standing from which equivalence could be occupied.\",\"reason\":\"V4 recognizes a place-or-rank branch for {{ar:ك و ن}} ({{tr:k-w-n}}), but the local verb instance is a negated copula; the branch survives only as family pressure, not as the selected sense.\",\"representative_source_ids\":[\"QS-357d02ac\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:4:attachment-emphasis-narrowed","source_type":"word_analysis","support_id":"sup_4494c5dced7c238a45a8","text":"{\"blocking_evidence\":null,\"headline\":\"attachment variation shifts emphasis, not the core parse\",\"reader_payoff\":\"The reader notices that the phrase can pull attention toward affected party or comparison standard, while local syntax still anchors it to the equality noun.\",\"reason\":\"The CRITICAL ambiguity has interpretive payoff, but attachment evidence specifically marks the pronoun in {{ar:لَّهُۥ}} ({{tr:lahu}}) as complement of {{ar:كُفُوًا}} ({{tr:kufuwan}}), so competing head choices cannot govern the local parse.\",\"representative_source_ids\":[\"QG-7c319132\",\"QY-0c1d12bb\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"112:4:2:1","source_type":"qac_morpheme","support_id":"sup_49e858eae6e42567aa3b","text":"{\"lemma_ar\":\"كَانَ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:kaAna|ROOT:kwn|SP:kaAn|3MS|MOOD:JUS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"112:4:2:1\",\"qac_word_ref\":\"112:4:2\",\"root_ar\":\"ك و ن\",\"surface_ar\":\"يَكُن\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:4:divine-pronoun-resumption","source_type":"word_analysis","support_id":"sup_4c71bd22664b0e10af79","text":"{\"blocking_evidence\":null,\"headline\":\"suffix resumes the established referent\",\"reader_payoff\":\"The reader notices that the final clause keeps the same divine referent active by pronoun rather than restarting with a repeated name.\",\"reason\":\"Attachment cross-reference and translation support resolve the suffix in {{ar:لَّهُۥ}} ({{tr:lahu}}) to the established divine discourse participant named earlier in the surah.\",\"representative_source_ids\":[\"QG-13c4eded\",\"QF-9158ef28\",\"QE-dccb082a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:2:whole-clause-negation","source_type":"word_analysis","support_id":"sup_4fd072f763a3fbe3d0ff","text":"{\"blocking_evidence\":null,\"headline\":\"negation covers the whole clause\",\"reader_payoff\":\"The reader notices that the particle denies the entire existence-and-equivalence construction, not merely one local word.\",\"reason\":\"Attachment evidence marks {{ar:لَمْ}} ({{tr:lam}}) as governing {{ar:يَكُنْ}} ({{tr:yakun}}), and translation support warns that the negation must cover the whole copular clause.\",\"representative_source_ids\":[\"QG-3c732591\",\"QT-fca1cb47\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:6","source_type":"word_analysis","support_id":"sup_50719f0abdcbe16c3dc4","text":"{\"gloss_range\":\"indefinite nominative delayed subject meaning not one, no one, not anyone under the negated copular frame\",\"prose\":\"{{ar:أَحَدٌۢ}} ({{tr:ahadun}}) is the delayed nominative subject, not another predicate joined loosely to {{ar:كُفُوًا}} ({{tr:kufuwan}}). Its case separates the two indefinite nouns: {{ar:كُفُوًا}} ({{tr:kufuwan}}) is the denied predicate, while {{ar:أَحَدٌۢ}} ({{tr:ahadun}}) is the candidate class revealed at the end. Under {{ar:لَمْ}} ({{tr:lam}}), the indefinite subject becomes universal negative polarity: not one, not anyone. That not-one pressure denies even the first member of any comparable series, not merely a later rival. The final position makes the word answer the whole buildup from connector, negator, verb, pronoun, and predicate; variant ordering is useful chiefly because it highlights how much force the received wording gains by saving the subject for the close. It also returns to the root used in 112:1, so the surah closes on the same lexical material with reversed polarity: first divine oneness is affirmed, then every possible equivalent is excluded. Across the boundary from the prior hidden divine subject, the explicit subject here is the empty class of any possible equal. The paired indefinite cadence with {{ar:كُفُوًا}} ({{tr:kufuwan}}) makes the last two words sound joined while grammar and negation deny that any match exists.\",\"root_display\":\"{{ar:أ ح د}} ({{tr:ʾ-ḥ-d}})\",\"root_gloss_range\":\"oneness and anyone/no-one polarity are both relevant locally; the final word converts the surah's opening unicity root into universal exclusion of any equal\",\"surface_display\":\"{{ar:أَحَدٌۢ}} ({{tr:ahadun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:5:predicate-subject-cadence","source_type":"word_analysis","support_id":"sup_543f76d1bb30ec3f00a2","text":"{\"blocking_evidence\":null,\"headline\":\"paired indefinite nouns close together\",\"reader_payoff\":\"The reader hears the predicate and subject paired by indefinite nasal cadence at the very point where their equivalence is denied.\",\"reason\":\"The adjacent nouns {{ar:كُفُوًا}} ({{tr:kufuwan}}) and {{ar:أَحَدٌۢ}} ({{tr:ahadun}}) are both indefinite, while case and attachment keep their grammatical roles distinct.\",\"representative_source_ids\":[\"QE-095b1116\",\"QP-8e8997e9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:5:root-family-parity","source_type":"word_analysis","support_id":"sup_590ccdd18ea5a64bd10b","text":"{\"blocking_evidence\":null,\"headline\":\"root family sharpens peerhood\",\"reader_payoff\":\"The reader notices that the word denies not loose similarity but a counterpart capable of balanced, reciprocal parity.\",\"reason\":\"QAC gives equality, equivalence, and matching for the local root, and no guardrail contradicts the CRITICAL parity field.\",\"representative_source_ids\":[\"QS-15fc5f13\",\"QS-291e59f8\",\"QS-31c8cc24\",\"QS-99fc4222\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:4:bound-prepositional-unit","source_type":"word_analysis","support_id":"sup_595d1d1c7acd8f0059cd","text":"{\"blocking_evidence\":null,\"headline\":\"preposition and pronoun arrive as one unit\",\"reader_payoff\":\"The reader notices the compactness of the relational phrase: the preposition and pronoun enter together as the clause's comparison target.\",\"reason\":\"The surface form is a bound prepositional-pronominal unit, so the relation target is carried in a single compact word.\",\"representative_source_ids\":[\"QF-0d9a0edd\",\"MG-5575c87b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:6:delayed-subject-role","source_type":"word_analysis","support_id":"sup_5a6b4f3d5f7b51402582","text":"{\"blocking_evidence\":null,\"headline\":\"final word is the delayed subject\",\"reader_payoff\":\"The reader notices that the last word resolves the clause as the subject slot, not as a second predicate or loose intensifier.\",\"reason\":\"Attachment evidence marks {{ar:أَحَدٌۢ}} ({{tr:ahadun}}) as the delayed nominative subject of {{ar:يَكُنْ}} ({{tr:yakun}}), while {{ar:كُفُوًا}} ({{tr:kufuwan}}) is the accusative predicate.\",\"representative_source_ids\":[\"QG-0045f4d4\",\"QG-80e46883\",\"QT-9984bc41\",\"QT-e265f805\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:5","source_type":"word_analysis","support_id":"sup_6100310057837c0158c1","text":"{\"gloss_range\":\"accusative indefinite predicate denying any peer, counterpart, or relation of full equivalence to Him\",\"prose\":\"{{ar:كُفُوًا}} ({{tr:kufuwan}}) is the accusative predicate of the negated copular clause, so equivalence is the quality directly denied. Its indefinite ending makes the denial unbounded: not a known equal, and not any possible mode of peerhood. The comparison is fixed by {{ar:لَّهُۥ}} ({{tr:lahu}}), so the word does not mean loose resemblance but parity to Him. Because the predicate comes before the delayed subject, the listener hears the criterion of equivalence first and only then reaches the absent candidate. The root-family field of {{ar:ك ف أ}} ({{tr:k-f-ʾ}}) presses toward matching, peerhood, and reciprocal parity; social or exchange registers sharpen the notion of point-for-point equivalence while the local clause negates it completely. Coming after the birth-denials of 112:3, the peer noun names the broader correspondence those generative roles had already been dismantling. Because this root appears here as a corpus-unique equality noun, the whole burden of Quranic peer-denial is concentrated in this one predicate. The secondary overturning image can suggest balance collapsing, but only as narrowed background while peer-equivalence remains the selected sense. Variant vocalizations and hamza visibility show the word as a sound-pressure point: sukun clipping shortens the equality noun, while explicit hamza makes the root catch more sharply in recitation; both preserve the same core denial. The related formula in 17:111 helps by contrast: that passage denies partnership and protective need, while 112:4 uses {{ar:كُفُوًا}} ({{tr:kufuwan}}) to deny equivalent counterpartship itself.\",\"root_display\":\"{{ar:ك ف أ}} ({{tr:k-f-ʾ}})\",\"root_gloss_range\":\"equality, matching, peerhood, parity, and reciprocal correspondence are relevant; secondary overturning imagery is only narrowed background pressure\",\"surface_display\":\"{{ar:كُفُوًا}} ({{tr:kufuwan}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:6:non-counting-unicity-pressure","source_type":"word_analysis","support_id":"sup_62f80c90e353b6973ea8","text":"{\"blocking_evidence\":null,\"headline\":\"not one blocks a countable peer series\",\"reader_payoff\":\"The reader notices that the final not-one does not invite a series of comparable ones; it denies even the first candidate in such a series.\",\"reason\":\"The lexical contrast survives as root-family pressure, while local grammar selects the negative-polarity subject sense under {{ar:لَمْ}} ({{tr:lam}}).\",\"representative_source_ids\":[\"QS-397854b2\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:5:unbounded-indefinite-parity","source_type":"word_analysis","support_id":"sup_6da3596245afc2cba235","text":"{\"blocking_evidence\":null,\"headline\":\"indefiniteness makes parity unbounded\",\"reader_payoff\":\"The reader notices that the indefinite predicate under negation denies every possible kind of equivalent, not merely a known equal.\",\"reason\":\"The surface is indefinite accusative, and the whole predicate is under the scope of {{ar:لَمْ}} ({{tr:lam}}).\",\"representative_source_ids\":[\"QG-5255b994\",\"QF-44285aee\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:3:divine-relation-formula","source_type":"word_analysis","support_id":"sup_75c93d2487be2b911a9a","text":"{\"blocking_evidence\":null,\"headline\":\"formula targets equivalence here\",\"reader_payoff\":\"The reader notices that a familiar divine-relation denial frame is filled here with equivalence rather than partnership or protective need.\",\"reason\":\"The CRITICAL rows give the concrete comparison with 17:111, and the local construction shares the negated copular-plus-pronoun frame while changing the denied relation noun.\",\"representative_source_ids\":[\"QI-a5f5f887\",\"QE-43de2052\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:4:fixed-comparison-standard","source_type":"word_analysis","support_id":"sup_7f5d187ae86232a2af18","text":"{\"blocking_evidence\":null,\"headline\":\"the standard is fixed before the candidate\",\"reader_payoff\":\"The reader notices that the clause names the comparison standard before revealing that no candidate can fill the subject slot.\",\"reason\":\"The local order places {{ar:لَّهُۥ}} ({{tr:lahu}}) before the predicate and delayed subject, and attachment evidence links the suffix phrase with {{ar:كُفُوًا}} ({{tr:kufuwan}}) as its complement.\",\"representative_source_ids\":[\"QG-bf6267a5\",\"QS-8d43a42e\",\"QI-c59ccb96\",\"QT-3bbb47da\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:6:opening-root-return","source_type":"word_analysis","support_id":"sup_846af69d8c85792ded26","text":"{\"blocking_evidence\":null,\"headline\":\"opening oneness returns as final exclusion\",\"reader_payoff\":\"The reader notices the surah-scale return: the root that affirms divine oneness in 112:1 becomes the final word that excludes every peer in 112:4.\",\"reason\":\"The CRITICAL rows give the concrete intra-surah reference to 112:1, and local polarity evidence supports the shift from affirmed uniqueness to negated candidate.\",\"representative_source_ids\":[\"QS-5c98eaad\",\"QS-dc979af8\",\"QI-2659b75b\",\"MI-bdc75b71\",\"QT-59736040\",\"QE-50189232\",\"QE-fe923787\",\"MH-271d5b66\",\"QY-cfe29649\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:3:jussive-negated-form","source_type":"word_analysis","support_id":"sup_8890c8bf136fe52f53b5","text":"{\"blocking_evidence\":null,\"headline\":\"negation clips the verb form\",\"reader_payoff\":\"The reader sees and hears that the verb of being is formally dependent on the negator, with the clipped form matching the denial it carries.\",\"reason\":\"QAC and attachment evidence identify the surface as the jussive/apocopated imperfect governed by {{ar:لَمْ}} ({{tr:lam}}), not an ungoverned form.\",\"representative_source_ids\":[\"QG-1f949475\",\"QF-9185e7cb\",\"QP-e0e21d1a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:5:overturning-image-narrowed","source_type":"word_analysis","support_id":"sup_a4af6330edde776ed097","text":"{\"blocking_evidence\":null,\"headline\":\"overturned balance remains secondary\",\"reader_payoff\":\"The reader notices a secondary image of balance collapsing, while the selected local sense remains peer-equivalence.\",\"reason\":\"The root-image claim has explanatory value only as background pressure; the local QAC and syntax select equality, equivalence, and matching, not an overturning action.\",\"representative_source_ids\":[\"QS-0a36a94d\",\"MG-c1408982\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:1:dual-backward-reach","source_type":"word_analysis","support_id":"sup_a94b36516d236481f0c4","text":"{\"blocking_evidence\":null,\"headline\":\"continuation and seal both remain audible\",\"reader_payoff\":\"The reader notices that the connector reaches backward while also launching the closing seal, so the ayah feels both continuous and final.\",\"reason\":\"The local evidence strongly supports coordination, while the ayah-initial position still lets the final clause land as a closing declaration.\",\"representative_source_ids\":[\"QG-c52d3e71\",\"QS-079f7a81\",\"QT-0227e11b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:5:hapax-burden","source_type":"word_analysis","support_id":"sup_a95cab956b62d6325c05","text":"{\"blocking_evidence\":null,\"headline\":\"single occurrence carries the denial\",\"reader_payoff\":\"The reader notices that the Quranic force of this equality-root is concentrated in one negated predicate.\",\"reason\":\"The contextual profile marks {{ar:ك ف أ}} ({{tr:k-f-ʾ}}) as a low-occurrence root/form appearing here under negation as a predicate.\",\"representative_source_ids\":[\"QI-9cad3dbb\",\"QH-85865017\",\"QY-35340915\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:6:variant-final-placement","source_type":"word_analysis","support_id":"sup_b029b0359a6fa87f9ffc","text":"{\"blocking_evidence\":null,\"headline\":\"variant order highlights final placement\",\"reader_payoff\":\"The reader notices how much force the received order gains by delaying the subject to the final word.\",\"reason\":\"The variant order is useful as apparatus, but the received local attachment evidence keeps {{ar:أَحَدٌۢ}} ({{tr:ahadun}}) after the predicate as the delayed subject.\",\"representative_source_ids\":[\"QF-90020a37\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:5:comparison-standard","source_type":"word_analysis","support_id":"sup_b0b8e271d4db8acefb11","text":"{\"blocking_evidence\":null,\"headline\":\"the pronoun supplies the standard\",\"reader_payoff\":\"The reader notices that the equality noun receives its measure from the pronoun phrase, so the denied parity is specifically parity to Him.\",\"reason\":\"Attachment evidence marks the pronoun in {{ar:لَّهُۥ}} ({{tr:lahu}}) as governed by the preposition and linked as complement of {{ar:كُفُوًا}} ({{tr:kufuwan}}).\",\"representative_source_ids\":[\"QG-980de1a0\",\"QT-5f7e2dfe\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:6:existence-root-pair","source_type":"word_analysis","support_id":"sup_bf66ef49f0f0a05ca36a","text":"{\"blocking_evidence\":null,\"headline\":\"being and not-one form the local mechanism\",\"reader_payoff\":\"The reader notices that the explicit subject in ayah 4 is no longer the divine actor of denied genealogy but the empty class of any possible equal.\",\"reason\":\"The local construction pairs {{ar:يَكُنْ}} ({{tr:yakun}}) with {{ar:أَحَدٌۢ}} ({{tr:ahadun}}), and the boundary row correctly identifies the shift from divine subject in prior verbal clauses to absent candidate class here.\",\"representative_source_ids\":[\"QI-696c915e\",\"QB-24ef1122\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:1:coordinated-final-negation","source_type":"word_analysis","support_id":"sup_c192c0b647d849d32ad8","text":"{\"blocking_evidence\":null,\"headline\":\"connector joins the final denial\",\"reader_payoff\":\"The reader notices that the final clause is syntactically added to the preceding negations, so the surah closes by completing a denial chain rather than starting a detached statement.\",\"reason\":\"QAC and attachment evidence mark {{ar:وَ}} ({{tr:wa}}) as coordination linking the negated clause in 112:4 with the negated clauses in 112:3.\",\"representative_source_ids\":[\"QG-b2a75221\",\"MG-13e8c6d8\",\"QB-576e7f0e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:4:boundary-pronoun-surfacing","source_type":"word_analysis","support_id":"sup_ceb3ab0497403b4a25da","text":"{\"blocking_evidence\":null,\"headline\":\"hidden subject becomes explicit suffix\",\"reader_payoff\":\"The reader notices the shift from the prior hidden subject of the negated verbs to an explicit pronoun anchoring the final comparison.\",\"reason\":\"The suffix in {{ar:لَّهُۥ}} ({{tr:lahu}}) explicitly resumes the same referent active across the preceding clauses.\",\"representative_source_ids\":[\"QB-f930f6f1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:5:delayed-candidate-reveal","source_type":"word_analysis","support_id":"sup_cf6be40c9f4adf7c8b44","text":"{\"blocking_evidence\":null,\"headline\":\"predicate comes before the candidate\",\"reader_payoff\":\"The reader hears the criterion of equivalence before the final word reveals that no subject fills it.\",\"reason\":\"Local word order places the predicate {{ar:كُفُوًا}} ({{tr:kufuwan}}) before the delayed subject {{ar:أَحَدٌۢ}} ({{tr:ahadun}}).\",\"representative_source_ids\":[\"QT-116d3aea\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:3","source_type":"word_analysis","support_id":"sup_cf84004e4e63e65404a9","text":"{\"gloss_range\":\"negated jussive copular/existential verb requiring a predicate and delayed subject\",\"prose\":\"{{ar:يَكُنْ}} ({{tr:yakun}}) supplies the copular frame that the rest of the ayah must complete. As a deficient verb under {{ar:لَمْ}} ({{tr:lam}}), it requires {{ar:كُفُوًا}} ({{tr:kufuwan}}) as predicate and {{ar:أَحَدٌۢ}} ({{tr:ahadun}}) as delayed subject, so the clause is a denied existence construction rather than a list of descriptions. Its clipped jussive shape makes the verb of being formally dependent on the negator before the predicate is even supplied. The being-root {{ar:ك و ن}} ({{tr:k-w-n}}) is used at the point where the ayah refuses any equal the status of obtaining at all; against the wider creative-command association of bringing-to-be, this local form blocks any peer from coming-to-be as an equal. Its wider place-and-standing branch can be heard only as narrowed pressure: the local grammar selects being or existing, while the payoff is that no peer has even a standing from which equivalence could be occupied. Across the boundary from denied generation, the clause shifts into existential comparison, where not one entity has being as an equal. The recurring divine-relation formula also recalls 17:111, where similar wording denies partnership or protective need; here the same frame is specialized toward equivalence.\",\"root_display\":\"{{ar:ك و ن}} ({{tr:k-w-n}})\",\"root_gloss_range\":\"being, occurrence, and predication are locally active; place or standing can be a narrowed family pressure, while suretyship, humbling, idiom, and bad-condition branches are not locally activated\",\"surface_display\":\"{{ar:يَكُنْ}} ({{tr:yakun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:5:genealogical-to-equivalence-boundary","source_type":"word_analysis","support_id":"sup_db937d453012714b410a","text":"{\"blocking_evidence\":null,\"headline\":\"genealogical denial widens into peer denial\",\"reader_payoff\":\"The reader notices that the final word-family of peerhood names the broader correspondence already dismantled by the prior birth-denials.\",\"reason\":\"The coordinated boundary from 112:3 to 112:4 supports the move from denied generative relation to denied equivalence relation.\",\"representative_source_ids\":[\"QB-98d3a861\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"112:4:5:1","source_type":"qac_morpheme","support_id":"sup_dbe32e52256a97b35f1a","text":"{\"lemma_ar\":\"أَحَد\",\"morph_features\":\"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"112:4:5:1\",\"qac_word_ref\":\"112:4:5\",\"root_ar\":\"ء ح د\",\"surface_ar\":\"أَحَدٌۢ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:5:predicate-equivalence-denial","source_type":"word_analysis","support_id":"sup_ddf4acb6d08b0b171555","text":"{\"blocking_evidence\":null,\"headline\":\"equivalence is the denied predicate\",\"reader_payoff\":\"The reader notices that the ayah directly predicates and negates equivalence, rather than treating peerhood as a side condition.\",\"reason\":\"QAC and attachment evidence force {{ar:كُفُوًا}} ({{tr:kufuwan}}) as the accusative predicate of {{ar:يَكُنْ}} ({{tr:yakun}}), with {{ar:أَحَدٌۢ}} ({{tr:ahadun}}) as delayed subject.\",\"representative_source_ids\":[\"QG-4dc4aa13\",\"QG-fe3fbe8d\",\"QS-d8c72ba3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:4:variant-reordering-apparatus","source_type":"word_analysis","support_id":"sup_e0f699d1abbf164bfea3","text":"{\"blocking_evidence\":null,\"headline\":\"reordered variants expose movable emphasis\",\"reader_payoff\":\"The reader notices that variant ordering can shift emphasis, while the received order foregrounds the standard before equality and subject.\",\"reason\":\"The variants are useful as apparatus, but they do not override the received local order or the forced predicate-subject analysis.\",\"representative_source_ids\":[\"QF-8fd38a9a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"112:4:4:1","source_type":"qac_morpheme","support_id":"sup_e9c208f5b7548891677d","text":"{\"lemma_ar\":\"كُفُو\",\"morph_features\":\"STEM|POS:N|LEM:kufuw|ROOT:kfA|M|INDEF|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"112:4:4:1\",\"qac_word_ref\":\"112:4:4\",\"root_ar\":\"ك ف ء\",\"surface_ar\":\"كُفُوًا\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:5:variant-form-pressure","source_type":"word_analysis","support_id":"sup_f4d994a5a446163b3769","text":"{\"blocking_evidence\":null,\"headline\":\"variant forms adjust sound and abstraction\",\"reader_payoff\":\"The reader notices that variant vocalization and hamza treatment make the equality noun a formal pressure point without changing the core denial.\",\"reason\":\"Canonical variants preserve the same equality-root denial while changing sound and hamza visibility; irregular variants are kept only as apparatus and do not govern the local parse.\",\"representative_source_ids\":[\"QF-1b508d32\",\"QF-464a50d7\",\"QF-b9da0e7c\",\"QF-efad644a\",\"QF-fb3e3062\",\"QP-d50a560d\",\"QP-f4013215\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:6:final-cadence","source_type":"word_analysis","support_id":"sup_f67b6bee6c0c4ca9a5b5","text":"{\"blocking_evidence\":null,\"headline\":\"final sound binds and denies the pair\",\"reader_payoff\":\"The reader hears the last two indefinite nouns paired by sound while their case and negation prevent any real pairing in meaning.\",\"reason\":\"The phrase {{ar:كُفُوًا أَحَدٌۢ}} ({{tr:kufuwan ahadun}}) closes with adjacent indefinite nouns, but attachment and case keep predicate and subject distinct.\",\"representative_source_ids\":[\"QE-ce846691\",\"QP-6a876769\",\"QP-c9ed785e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"112:4:1","source_type":"word_analysis","support_id":"sup_ff869008c1838ecbe84c","text":"{\"gloss_range\":\"coordinating connector that joins the whole final negated clause to the prior negation chain\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) opens the final ayah as continuation before it becomes closure. Its scope reaches over the whole clause, so {{ar:وَلَمْ يَكُنْ لَّهُۥ كُفُوًا أَحَدٌۢ}} ({{tr:wa-lam yakun lahu kufuwan ahadun}}) is not an isolated sentence but the next member of the negated sequence after 112:3. The connector can be heard as joining the immediately prior negation or the whole two-part denial before it; either way, the final denial functions as the third coordinated relation: no offspring, no origin, no peer. Because the connector fuses prosodically with {{ar:لَمْ}} ({{tr:lam}}), the reader hears coordination and negation arrive together.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ","ayah_ref":"112:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000017/B002","root_001305/B001","root_001332/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001332","role":"Being or temporal occurrence supplies the relation whose instantiation is denied.","root":"ك و ن","source_ref":"112:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001305","role":"Equal counterpart and matching response make the denied relation reciprocal, suitable, or oppositional rather than merely similar.","root":"ك ف ء","source_ref":"112:4","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000017","role":"Negative exhaustive anyone ranges the denial over every possible claimant.","root":"ء ح د","source_ref":"112:4","source_word_indices":["5"]}],"changed_reading":{"after":"At no time can any candidate enter a reciprocal matching, suitability, or oppositional relation with Him; the counterpart relation itself never obtains.","before":"No one resembles Him."},"confidence":"strong","focus_anchor":"The negated temporal predicate at word 2, the counterpart noun at word 4, and the exhaustive indefinite at word 5.","mechanism":"Temporal predication opens a possible relation of equal matching or reciprocal opposition, while negative exhaustive 'anyone' closes that relation over every candidate. The negation targets not only a resembling object but the occurrence of a peer relation at all.","model_id":"baseline_exhaustive_counterpart_noninstantiation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_exhaustive_counterpart_noninstantiation","source_type":"hft","support_id":"sup_c22e2afcdd54078053f2","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ","ayah_ref":"112:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000017/B002","root_001305/B001","root_001332/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001332","role":"Place, position, or rank turns being into occupancy of a station.","root":"ك و ن","source_ref":"112:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001305","role":"Equal counterpart specifies the prohibited station as one of parity.","root":"ك ف ء","source_ref":"112:4","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000017","role":"Exhaustive anyone prevents every candidate from occupying that parity-position.","root":"ء ح د","source_ref":"112:4","source_word_indices":["5"]}],"changed_reading":{"after":"There is no station of parity beside Him that anyone could occupy.","before":"There is no being with the same attributes."},"confidence":"medium","focus_anchor":"The word-2 being root also carries place, position, and rank, which meets the word-4 equal-counterpart branch under exhaustive negation.","mechanism":"The denied copular relation can be spatialized or socialized as occupying a station. Equality is then exclusion from a comparable position or rank, not only denial of shared qualities.","model_id":"baseline_no_comparable_station"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_no_comparable_station","source_type":"hft","support_id":"sup_8b63b4d4bf8d151a57c1","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ","ayah_ref":"112:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000017/B002","root_001305/B002","root_001332/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001332","role":"Occurrence supplies the possible arising of a counter-force.","root":"ك و ن","source_ref":"112:4","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001305","role":"Tilting, overturning, and diverting recast a counterpart as an effective turning force.","root":"ك ف ء","source_ref":"112:4","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000017","role":"Exhaustive anyone extends the denial to every imagined counter-force.","root":"ء ح د","source_ref":"112:4","source_word_indices":["5"]}],"changed_reading":{"after":"No one can arise as an overturning or diverting counter-force against Him.","before":"No one is His equal."},"confidence":"exploratory","focus_anchor":"The word-4 root has a live branch of tilting, overturning, and diverting, while words 2 and 5 deny occurrence for anyone.","mechanism":"A branch-distant reading hears the counterpart term as a facing force capable of turning or diverting. Exhaustive negation then blocks not only an equal peer but any counter-force that could overturn or redirect Him.","model_id":"baseline_no_overturning_counterforce"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_no_overturning_counterforce","source_type":"hft","support_id":"sup_8dab2f8db81abb1c6df8","trust":"legacy_unbound"}]}
</lane_packet_json>
