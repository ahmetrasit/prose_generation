# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **12:16**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s012-p01-with-fatiha/s012/12_16/micro.discovery.json` and modify nothing
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
  "ayah_ref": "12:16",
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
{"analysis_context":{"analysis_id":"s012-p01-with-fatiha","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"12:16","host_surah":12,"lane_context_refs":[],"ordered_context_refs":["12:1","12:2","12:3","12:4","12:5","12:6","12:7","12:8","12:9","12:10","12:11","12:12","12:13","12:14","12:15","12:17","12:18","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Babalık çekirdeği, besleyip yetiştirme eylemi ve sebep ya da kaynak sayılma genişlemesi birbirinden ayrılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000007/B001","candidate_links":[{"candidate_id":"cand_4cde9758ac8f9521d8ff","lane":"micro"},{"candidate_id":"cand_aa705fb29494114631ca","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَبٌ","morph_features":"STEM|POS:N|LEM:>abN|ROOT:Abw|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"12:16:2:1","qac_word_ref":"12:16:2","surface_ar":"أَبَا"}],"gloss":"babalık, besleyip yetiştirme ve oluşuma ya da iyileşmeye kaynaklık etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kimsenin baba olması, babalık ilişkisi taşıması veya baba soyunu temsil etmesidir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birini ebeveynin çocuğunu beslediği gibi besleyip büyütme ve yetiştirme eylemidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir şeyin meydana gelmesine, düzelmesine veya görünür hâle gelmesine sebep olan kimsenin baba benzeri kaynak sayılmasıdır."}}],"root_ar":"ء ب و","root_id":"root_000007","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Babalık çekirdeğini, ebeveyn gibi bakım verip büyütmeyi ve sebep olma yoluyla gelişen kaynaklık anlamını birlikte temsil eder.","boundary_detail":"Babalık çekirdeği, besleyip yetiştirme eylemi ve sebep ya da kaynak sayılma genişlemesi birbirinden ayrılmalıdır.","branch_image_ar":"الأبوة والتربية","concept_gloss":"babalık, besleyip yetiştirme ve oluşuma ya da iyileşmeye kaynaklık etme","contextual_glosses":[{"applicability":"Doğrudan ebeveynlik, baba olma veya baba soyu söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Baba olma ve baba soyuna bağlı ilişkiyi doğal biçimde karşılar."},"facet_ids":["F001"],"text":"baba ve babalık","usage_role":"contextual"},{"applicability":"Bir çocuğu veya bakıma muhtaç kimseyi ebeveyn gibi besleme ve yetiştirme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bakım verme, besleme ve gelişmesini sağlama eylemlerini korur."},"facet_ids":["F002"],"text":"besleyip büyütmek","usage_role":"contextual"},{"applicability":"Bir kişinin bir şeyin meydana gelmesini, iyileşmesini veya görünür olmasını sağladığı genişletilmiş kullanımda geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sebep olma ile kaynak sayılma arasındaki genişletilmiş ilişkiyi açıklar."},"facet_ids":["F003"],"text":"ortaya çıkmasına veya düzelmesine kaynak olan","usage_role":"explanatory"}],"definition":"Bir kimsenin baba olması veya baba soyunu temsil etmesi, ebeveyn gibi besleyip yetiştirmesi anlam alanının çekirdeğidir. Bundan hareketle, bir şeyin ortaya çıkmasına, düzelmesine ya da görünür olmasına sebep olan kimse de baba benzeri bir kaynak olarak adlandırılabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kimsenin baba olması, babalık ilişkisi taşıması veya baba soyunu temsil etmesidir."},{"facet_id":"F002","role":"core","statement":"Birini ebeveynin çocuğunu beslediği gibi besleyip büyütme ve yetiştirme eylemidir."},{"facet_id":"F003","role":"extension","statement":"Bir şeyin meydana gelmesine, düzelmesine veya görünür hâle gelmesine sebep olan kimsenin baba benzeri kaynak sayılmasıdır."}],"identity_rationale":"Kaynak ifadesi babayı, babalık ilişkisini ve ebeveyn gibi besleyip yetiştirmeyi aynı anlam alanında toplar; ayrıca bir şeyin ortaya çıkmasına, düzelmesine veya görünür olmasına sebep olan kimseye yönelik genişletilmiş kullanımı açıkça belirtir. Bu nedenle verilen çerçeve, çekirdek ile ona bağlı genişlemeyi koruduğu sürece kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"baba"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"babalar, atalar ve baba yönünden onlara katılanlar"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"anne ile baba; bağlama göre baba ile amca veya dede"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"babalık veya baba soyu"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"birinin ya da bir topluluğun babası olmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"ebeveyn gibi besleyip büyütmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birini baba edinmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir şeyin ortaya çıkmasına, düzelmesine veya görünür olmasına sebep olan kimse"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"konuklarla yakından ilgilenen kimse"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"savaşı kışkırtan kimse"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"bir kadının bekâretini bozan erkek"}],"lexicalization_note":"Tanım hem baba ve babalık bildiren yalın biçimleri hem de yalnız belirli yapılarda görülen besleme, baba olma ve baba edinme kullanımlarını ayrı yönler olarak korur.","neighbor_coverage_note":"Adayların tamamı karşılaştırıldı; ebeveynlik, besleme ve düzeltme sınırlarını açıklayan üç komşu seçildi, yalnız ortak senaryoya katılan veya ilgisiz olanlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ortak baba ve anne-baba kapsamını besleyip yetiştirme ve kaynaklık yönlerine genişletirken komşu dal anneyi tek başına adlandırmayı ve paylaşılan ebeveyn kapsamını doğum ilişkisi üzerinden kurmayı öne çıkarır.","focus_only":"Babalığı besleyip yetiştirme ve bir şeyin oluşumuna ya da düzelmesine kaynak olma yönlerine kadar genişletir.","gloss":"babalık ile doğum ebeveynliği","neighbor_only":"Anneyi tek başına doğum ebeveyni olarak adlandırma kapsamını içerir.","neighbor_ref":"root_001683/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da babayı ve anne ile babanın birlikte oluşturduğu ebeveyn çiftini kapsar."},{"boundary_match":"partial","distinction":"Odak dal bakım eylemini baba rolüne benzeterek kurar; komşu dal ise beslenme ve büyümeyi doğrudan gelişim süreci olarak anlatır.","focus_only":"Babalık ilişkisini ve baba benzeri kaynaklık genişlemesini içerir.","gloss":"ebeveyn gibi besleme ile büyüme","neighbor_only":"Büyüme, gelişme ve bir topluluk içinde yetişme süreçlerini baba rolünden bağımsız olarak kapsar.","neighbor_ref":"root_000537/B005","relation_type":"near_neighbor","shared_zone":"İki dal, beslenme ve yetişme yoluyla gelişmenin sağlanması alanında kesişir."},{"boundary_match":"partial","distinction":"Odak dalın merkezi baba ilişkisi ve ebeveyn benzeri beslemedir; komşu dalın merkezi ise bir işi üstlenerek düzeltmek, tamamlamak ve gözetmektir.","focus_only":"Baba olma, baba soyu ve baba gibi kaynak sayılma anlamlarını taşır.","gloss":"babalık bakımı ile düzeltip tamamlama","neighbor_only":"Bir şeyin işini üstlenip onu aşama aşama düzeltme, tamamlama ve yönetme anlamlarını taşır.","neighbor_ref":"root_000532/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal bakım verme, yetiştirme ve bir şeyin durumunu iyileştirme alanında buluşur."}],"source_phrase_ar":"يدل على التربية والغذو (maqayis)؛ أبوت الشيء آبوه أبوا إذا غذوته (maqayis)؛ فلان يأبو هذا اليتيم إباوة أي يغذوه كما يغذو الوالد ولده (ayn;tahdhib)؛ الأب أصله أبو (sihah)؛ الأب الوالد ويسمى كل من كان سببا في إيجاد شيء أو صلاحه أو ظهوره أبا (mufradat)","source_summary":"Kaynakların ortak çerçevesinde baba ve babalık, yalnız soy ilişkisini değil, ebeveyn gibi besleyip yetiştirmeyi de kapsar. Sebep olma ilişkisi üzerinden bir şeyin doğuşuna, düzelmesine veya ortaya çıkmasına kaynaklık eden kimseye kadar genişleyebilir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الأب والآباء والأبوان والأبوة ومن كان سببا في إيجاد أو صلاح ومن يأبو اليتيم أي يغذوه ويربيه","what_is_not_ar":"الإباء بمعنى الامتناع والقصب ووجع الأبواء وصيغ النداء والمثل"},"support_links":["sup_4ab61dc1ae9bc0f6043a","sup_c3cc1c10df9ea680f992"]},{"boundary":"Bu dal yalnız belirli hitap kalıplarına aittir; övgü ile ağır yergi arasındaki yorum farkı genelleştirilmemelidir.","branch_kind":"collocation","branch_ref":"root_000007/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَبٌ","morph_features":"STEM|POS:N|LEM:>abN|ROOT:Abw|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"12:16:2:1","qac_word_ref":"12:16:2","surface_ar":"أَبَا"}],"gloss":"babaya seslenme ve bağlama göre övgü ya da ağır yergi bildiren hitap kalıpları","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Babaya doğrudan seslenmek için kullanılan özel hitap biçimleridir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Baba yokluğunu dile getiren kalıplaşmış hitap, bir yorumda övgü sayılırken başka bir yorumda ağır yergi sayılır."}}],"root_ar":"ء ب و","root_id":"root_000007","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kanıtta verilen babaya seslenme biçimleri ile baba yokluğu üzerinden kurulan kalıplaşmış hitapları topluca gösterir.","boundary_detail":"Bu dal yalnız belirli hitap kalıplarına aittir; övgü ile ağır yergi arasındaki yorum farkı genelleştirilmemelidir.","branch_image_ar":"خطاب الأب ومثله","concept_gloss":"babaya seslenme ve bağlama göre övgü ya da ağır yergi bildiren hitap kalıpları","contextual_glosses":[{"applicability":"Babaya doğrudan ve yakınlık bildiren bir seslenme yapılırken doğal karşılık olarak kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Babaya doğrudan seslenme işlevini ve yakınlık tonunu korur."},"facet_ids":["F001"],"text":"babacığım","usage_role":"contextual"},{"applicability":"Baba yokluğu kalıbının övgü ve takdir bildirdiği yorumun bağlamsal karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hitabın övgü ve takdir işlevini doğal bir söyleyişle korur."},"facet_ids":["F002"],"text":"helal olsun sana","usage_role":"contextual"},{"applicability":"Aynı kalıbın ağır yergi olarak yorumlandığı bağlamdaki iletişim değerini verir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hitabın ağır kınama ve yergi işlevini doğal bir söyleyişle korur."},"facet_ids":["F002"],"text":"yazıklar olsun sana","usage_role":"contextual"}],"definition":"Babaya belirli biçimlerle seslenmeyi ve baba yokluğunu dile getiren kalıplaşmış hitapları kapsar. İkinci tür hitabın iletişim değeri bağlama ve yoruma göre övgüden çok ağır yergiye kadar değişebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Babaya doğrudan seslenmek için kullanılan özel hitap biçimleridir."},{"facet_id":"F002","role":"source_variant","statement":"Baba yokluğunu dile getiren kalıplaşmış hitap, bir yorumda övgü sayılırken başka bir yorumda ağır yergi sayılır."}],"identity_rationale":"Kaynak ifadesi babaya yönelik seslenme biçimlerini ve baba yokluğunu dile getiren kalıplaşmış hitapları birlikte verir. Ancak ikinci grubun yalnız övgü sayılması yeterli değildir; kanıt aynı kalıbın çok ağır bir yergi olarak da anlaşılabildiğini gösterdiği için dalın kullanım değeri bağlama göre iki kutuplu biçimde sınırlandırılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"babacığım diye seslenme"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bağlama göre övgü ya da ağır sövgü bildiren hitap kalıbı"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"seni çekemeyenin babası olmasın anlamında onurlandırıcı hitap"}],"lexicalization_note":"Tanım yalnız verilen seslenme ve kalıplaşmış hitap yapılarını kapsar; bunlardan bağımsız bir yalın anlam türetmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; doğrudan seslenme alanını veya ebeveyn adlarıyla kurulan hitapları açıklayan üç komşu seçildi, yalnız konu ortaklığı bulunan adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal belirli baba hitaplarına ve kalıplaşmış değerlendirme sözlerine bağlıdır; komşu dal ise muhatabın yakınlığına göre kullanılan genel seslenme araçlarını konu alır.","focus_only":"Babaya seslenme biçimlerini ve baba yokluğu üzerinden kurulan değerlendirme kalıplarını içerir.","gloss":"babaya hitap ile genel seslenme","neighbor_only":"Yakın veya uzaktaki kişiye seslenmekte kullanılan genel çağrı sözlerini içerir.","neighbor_ref":"root_000074/B008","relation_type":"same_field","shared_zone":"Her iki dal da bir muhataba doğrudan seslenme işlevi taşır."},{"boundary_match":"field_only","distinction":"Odak dalın sınırını baba anlamlı öğe ve onunla kurulan kalıplar belirler; komşu dalın sınırını ise kişi adının seslenmede kısaltılması belirler.","focus_only":"Baba kimliğini açıkça içeren özel hitap ve değerlendirme kalıplarını kapsar.","gloss":"babaya hitap ile kısaltılmış seslenme","neighbor_only":"Bir kişi adının kısaltılmış biçimiyle yapılan seslenmeyi ve buna bağlı biçim değişmelerini kapsar.","neighbor_ref":"root_001178/B003","relation_type":"same_field","shared_zone":"İki dal da kalıplaşmış doğrudan seslenme yapıları alanındadır."},{"boundary_match":"partial","distinction":"Odak dal yalnız baba öğesiyle kurulan belirli seslenme ve değerlendirme kalıplarını ele alır; komşu dal ise baba olma ilişkisini, bakımı ve kaynaklık genişlemesini kavramsal olarak kapsar.","focus_only":"Baba üzerinden kurulan seslenme ve bağlama göre övgü ya da yergi bildiren kalıpları içerir.","gloss":"baba hitapları ile babalık kavramı","neighbor_only":"Baba olmayı, baba soyunu, ebeveyn gibi besleyip yetiştirmeyi ve baba benzeri kaynaklığı içerir.","neighbor_ref":"root_000007/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal baba anlamlı öğe üzerinden kurulur ve baba kimliğine gönderimde bulunur."}],"source_phrase_ar":"يا أبة افعل (sihah)؛ يا أبت ويا أبت لغتان (sihah)؛ لا أبا لك كأنه يمدحه (ayn)؛ لا أبا لك ولا أب لك مدح (sihah)؛ لا أبا لك ولا أب لك مدح ولا أم لك ذم (tahdhib)","source_summary":"Kanıt, babaya yönelik özel seslenme biçimlerini ve baba yokluğunu ifade eden kalıplaşmış hitabı kaydeder. Toplu aktarımda ikinci kalıbın övgü sayıldığı görüş ile çok ağır bir yergi sayıldığı görüş birlikte bulunduğundan kullanım değeri tek kutba indirgenemez.","sources":["AY","SI","TA"],"what_is_ar":"يا أبت ويا أبة ولا أبا لك ولا أب لك وما جرى مجراها من تراكيب الأب","what_is_not_ar":"الأبوة العامة والتربية والإباء بمعنى الامتناع وأبيت اللعن"},"support_links":[]},{"boundary":"Anlam genel hastalık değildir; belirli keçilerde belirli bir koklama sebebine bağlanan hastalık durumudur.","branch_kind":"non_bare","branch_ref":"root_000007/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَبٌ","morph_features":"STEM|POS:N|LEM:>abN|ROOT:Abw|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"12:16:2:1","qac_word_ref":"12:16:2","surface_ar":"أَبَا"}],"gloss":"dağ keçisi idrarının kokusundan hastalanma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hastalığın tetikleyicisi dağ keçisi idrarının kokusunu almaktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ortaya çıkan hastalık durumu dişi keçi ve erkek keçi için ayrı kayıtlı nitelemelerle ifade edilir."}}],"root_ar":"ء ب و","root_id":"root_000007","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişi veya erkek keçinin belirtilen kokuyu aldıktan sonra hastalandığı sınırlı hayvan sağlığı bağlamında kullanılır.","boundary_detail":"Anlam genel hastalık değildir; belirli keçilerde belirli bir koklama sebebine bağlanan hastalık durumudur.","branch_image_ar":"داء الأَبْواء","concept_gloss":"dağ keçisi idrarının kokusundan hastalanma","contextual_glosses":[{"applicability":"Hayvanın dağ keçisi idrarını kokladıktan sonra hastalandığını akıcı metinde belirtmek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Koklama sebebini, hastalık sonucunu ve keçiye özgü kapsamı korur."},"facet_ids":["F001","F002"],"text":"idrar kokusundan hastalanmış keçi","usage_role":"contextual"}],"definition":"Dişi veya erkek bir keçinin dağ keçisi idrarının kokusunu alması ve bunun etkisiyle hastalanmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hastalığın tetikleyicisi dağ keçisi idrarının kokusunu almaktır."},{"facet_id":"F002","role":"specialization","statement":"Ortaya çıkan hastalık durumu dişi keçi ve erkek keçi için ayrı kayıtlı nitelemelerle ifade edilir."}],"identity_rationale":"Kaynak ifadesi hem dişi hem erkek keçi için, dağ keçisi idrarının kokusunu aldıktan sonra ortaya çıkan hastalığı açık bir sebep-sonuç bağıyla tanımlar. Verilen dal çerçevesi bu hayvan, tetikleyici ve sonuç sınırlarını doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"dağ keçisi idrarını koklayınca hastalanan dişi keçi"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"dağ keçisi idrarını koklayınca hastalanan erkek keçi"}],"lexicalization_note":"Tanım yalnız dişi ve erkek keçiye özgü kayıtlı niteleme biçimlerini kapsar; genel bir hastalanma anlamına genişletilmez.","neighbor_coverage_note":"Adayların tümü karşılaştırıldı; hastalık, hayvan türü ve çevresel sebep sınırlarını belirginleştiren üç komşu yayımlandı, yalnız tür veya senaryo ortaklığı taşıyanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal keçi türü ile belirli koklama sebebini birlikte şart koşar; komşu dal ise insanın genel hastalık durumunu anlatır.","focus_only":"Keçilerde dağ keçisi idrarının kokusunu almaya bağlanan özel hastalık durumunu belirtir.","gloss":"özel hayvan hastalığı ile genel beden hastalığı","neighbor_only":"İnsan bedenindeki hastalığı ve hasta olma durumunu sebep ya da hayvan türü sınırlaması olmadan belirtir.","neighbor_ref":"root_000721/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal bedensel hastalık ve sağlığın bozulması alanında kesişir."},{"boundary_match":"field_only","distinction":"Odak dalın hayvanı keçi, etkisi koku ve sonucu genel hastalanmadır; komşu dalın hayvanı deve, etkisi yenilen bitki ve sonucu karın rahatsızlığıdır.","focus_only":"Keçilerde idrar kokusunu almaktan doğan hastalık durumudur.","gloss":"kokudan hastalanma ile yemden karın ağrısı","neighbor_only":"Develerde belirli bir bitkiyi yemekten doğan karın rahatsızlığıdır.","neighbor_ref":"root_000026/B006","relation_type":"same_field","shared_zone":"İki dal da hayvanlarda belirli bir çevresel etkenden kaynaklanan rahatsızlığı anlatır."},{"boundary_match":"field_only","distinction":"Odak dal koklama yolunu ve keçiyi şart koşar; komşu dal yeme yolunu, karın şişmesini ve ağırlaşan ölüm tehlikesini öne çıkarır.","focus_only":"Keçinin belirli bir idrar kokusuna maruz kalınca hastalanmasını anlatır.","gloss":"kokudan hastalık ile zararlı ottan şişme","neighbor_only":"Deve veya başka otlayan hayvanın zararlı ot yemesiyle karnının şişmesini ve ölüm tehlikesini anlatır.","neighbor_ref":"root_000289/B001","relation_type":"same_field","shared_zone":"Her iki dal otlayan hayvanlarda dış bir etkene bağlanan hastalık hâlini konu alır."}],"source_phrase_ar":"عنز أبواء إذا أصابها وجع عن شم أبوال الأروى (maqayis)؛ عنز أبواء وتيس آبى إذا شم بول الأروى فمرض منه (sihah)","source_summary":"Kaynakların ortak anlatımı, dişi keçinin dağ keçisi idrarını kokladıktan sonra ağrı veya hastalığa tutulmasını bildirir; toplu kanıt erkek keçi için de aynı sebebe bağlı hastalık durumunu içerir.","sources":["MQ","SI"],"what_is_ar":"العنز الأَبْواء والتيس الآبى إذا مرضا من شم أبوال الأروى","what_is_not_ar":"الأب والآباء والتربية والإباء بمعنى الامتناع والقصب"},"support_links":[]},{"boundary":"Dal, akşam vaktinin kendisini ya da görme organındaki bir bozukluğu değil, karanlığı ve onun doğurduğu seçilemezliği anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001017/B001","candidate_links":[{"candidate_id":"cand_aa705fb29494114631ca","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عِشَآء","morph_features":"STEM|POS:N|LEM:Ei$aA^'|ROOT:E$w|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"12:16:3:1","qac_word_ref":"12:16:3","surface_ar":"عِشَآءً"}],"gloss":"karanlık ve görüş açıklığının azalması","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Karanlık, bir şeyin görünürlüğünü ve açıklığını azaltır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Geceye özgü kullanım, gecenin başlangıcından yaklaşık ilk dörtte birine kadar uzanan ilk karanlığı gösterebilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bilgisizlikle bir işe girişip yönünü görememe ve inançsızlığı karanlıkla anlatma, fiziksel seçilemezliğin aktarmalı uzantılarıdır."}}],"root_ar":"ع ش و","root_id":"root_001017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın fiziksel çekirdeğini, yani karanlık yüzünden bir şeyin açıkça seçilememesini karşılar.","boundary_detail":"Dal, akşam vaktinin kendisini ya da görme organındaki bir bozukluğu değil, karanlığı ve onun doğurduğu seçilemezliği anlatır.","branch_image_ar":"ظلام العِشاء وقلة الوضوح","concept_gloss":"karanlık ve görüş açıklığının azalması","contextual_glosses":[{"applicability":"Gecenin başlangıcı ile ilk dörtte biri arasındaki zamanla sınırlı kullanımda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karanlığın gece başlangıcına bağlı özel zaman sınırını korur."},"facet_ids":["F002"],"text":"gecenin ilk karanlığı","usage_role":"contextual"},{"applicability":"Karanlık ve görememe görüntüsünün bilgisizce girişilen işe aktarıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilgisizlik ile yönü seçememe arasındaki aktarmalı bağı açıkça korur."},"facet_ids":["F003"],"text":"ne yaptığını görmeden bilgisizce ilerleme","usage_role":"explanatory"}],"definition":"Bir şeyin karanlık olması ve bu yüzden açıkça seçilememesi durumudur. Gece bakımından başlangıçtaki karanlığı, aktarmalı olarak da bilgisizlik yüzünden bir işin doğru yönünü görememeyi kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Karanlık, bir şeyin görünürlüğünü ve açıklığını azaltır."},{"facet_id":"F002","role":"specialization","statement":"Geceye özgü kullanım, gecenin başlangıcından yaklaşık ilk dörtte birine kadar uzanan ilk karanlığı gösterebilir."},{"facet_id":"F003","role":"extension","statement":"Bilgisizlikle bir işe girişip yönünü görememe ve inançsızlığı karanlıkla anlatma, fiziksel seçilemezliğin aktarmalı uzantılarıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Salt bir zaman dilimi anlamı ekler.","collision":"Aynı kökün akşam vaktini anlatan ayrı dalıyla karışır.","fit":"displacement","loses":"Karanlık ve seçilemezlik çekirdeğini ortadan kaldırır.","preserves":"Gecenin başlangıcına yakın zaman bağlantısını kısmen korur."},"text":"akşam"}],"identity_rationale":"Kaynak ifadesi, dalın temelini karanlık ve bir şeyin seçilemez hale gelmesi olarak doğrular. Bunun yanında gecenin ilk bölümü için zamanla sınırlı kullanımlar ve bilgisizlik ya da inançsızlık için aktarmalı kullanımlar da verir; bu yan anlamlar temel çevresinde ayrı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"gecenin ilk karanlığı ve koyuluğu"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"gece karanlığı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"gecenin başlangıç karanlığı; bilgisizliğin karanlığı"}],"lexicalization_note":"Yalın biçimler gecenin ilk karanlığını adlandırırken belirli bir tamlama bütün gecenin karanlığına bağlanır; bu kapsamlar tek bir zaman adı gibi genellenmemiştir.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; yalnızca karanlık, akşam vakti ve görme zayıflığı sınırlarını doğrudan açıklayan karşılaştırmalar seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal karanlığın yanı sıra bir şeydeki açıklık kaybını ve ilk gece bölümünü kapsar; komşu ise gecenin karanlık hale gelmesini merkez alır.","focus_only":"Gecenin ilk bölümü ve bilgisizlik için aktarmalı seçilemezlik de bu dalın kapsamındadır.","gloss":"gecenin kararması","neighbor_only":"Komşu, özellikle gecenin karartılması ve karanlığın şiddetlenmesi üzerinde durur.","neighbor_ref":"root_001094/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da gece karanlığını ve ışığın azalmasını anlatır."},{"boundary_match":"field_only","distinction":"Aynı zaman çevresinde bulunsalar da biri algısal karanlığı, öteki takvimsel zaman aralığını gösterir.","focus_only":"Bu dal karanlık ve seçilemezlik durumunu anlatır.","gloss":"karanlık ile akşam vakti","neighbor_only":"Komşu, öğleden sonra ile gecenin başlangıcı arasındaki zaman dilimini adlandırır.","neighbor_ref":"root_001017/B004","relation_type":"same_field","shared_zone":"İki dal da günün geceye döndüğü dönemde kullanılabilir."},{"boundary_match":"partial","distinction":"Bu dal ortamın veya düşüncenin açıklığını, komşu ise gören kişinin duyusal yetisini niteler.","focus_only":"Burada seçilemezliğin nedeni çevredeki ya da kavramsal karanlıktır.","gloss":"karanlık ile görme zayıflığı","neighbor_only":"Komşuda neden, görme yetisinin körlüğe varmayan zayıflığıdır.","neighbor_ref":"root_001017/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da yeterince görememe sonucuna yaklaşır."}],"source_phrase_ar":"يدل على ظلام وقلة وضوح في الشيء؛ العشاء وهو أول ظلام الليل (maqayis)؛ عشواء الليل ظلمته (maqayis)؛ مضى من الليل عشوة وهو ما بين أوله إلى ربعه (sihah)؛ أخذت عليهم بالعشوة أي بالسواد من الليل (sihah)؛ العشوة ظلمة الكفر وكلما ركب الإنسان أمرا بجهل لا يبصر وجهه فهو عشوة (tahdhib)","source_summary":"Kaynaklar karanlık ve seçilemezlik çekirdeğinde birleşir; gecenin ilk karanlığını, gece karanlığını ve ne yaptığını bilmeden işe girişme benzetmesini aynı anlam alanında gösterir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه أول ظلام الليل وسواد الليل والعشوة بمعنى ظلمة أول الليل","what_is_not_ar":"ليس وقت العشي ولا طعام العشاء ولا ضعف البصر نفسه"},"support_links":["sup_c3cc1c10df9ea680f992"]},{"boundary":"Dal salt ateşi ya da geceyi değil, geceleyin ateşe yönelme olayını merkez alır; alev adı buna bağlı bir kullanımdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001017/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عِشَآء","morph_features":"STEM|POS:N|LEM:Ei$aA^'|ROOT:E$w|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"12:16:3:1","qac_word_ref":"12:16:3","surface_ar":"عِشَآءً"}],"gloss":"gece kılavuz ateşe yönelme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi gece karanlığında, kılavuzluk veya iyilik umduğu görünür bir ateşe yönelir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ateşin ışığı, karanlıkta ve görmenin zayıf olduğu durumda hedefi bulmaya yardımcı olur."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gece görünen alev ya da ateş ile geceleri onun ışığına gelen varlık, yönelme olayına bağlı adlandırmalardır."}}],"root_ar":"ع ش و","root_id":"root_001017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gece karanlığında ateş ışığını hedef ve kılavuz edinerek ona gitme çekirdeğini karşılar.","boundary_detail":"Dal salt ateşi ya da geceyi değil, geceleyin ateşe yönelme olayını merkez alır; alev adı buna bağlı bir kullanımdır.","branch_image_ar":"القصد إلى نار الليل","concept_gloss":"gece kılavuz ateşe yönelme","contextual_glosses":[{"applicability":"Ateşin gece karanlığında yön buldurduğu kullanımlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Işığın hedefi göstermesi ve kişinin ona doğru ilerlemesi ilişkisini korur."},"facet_ids":["F002"],"text":"ateş ışığını izleyerek yolunu bulma","usage_role":"contextual"},{"applicability":"Eylem yerine gecede beliren ateşin kendisinin adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alevin gece görünür olmasını ve yönelme olayındaki hedef rolünü korur."},"facet_ids":["F003"],"text":"gece görünen alev","usage_role":"contextual"}],"definition":"Gece karanlığında görünen bir ateşe, ışığından yol bulmak ya da yanında konukluk ve iyilik ummak için yönelme eylemidir. Gece görünen alevin kendisi ve ışığına gelen varlık da bu olay çevresinde adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi gece karanlığında, kılavuzluk veya iyilik umduğu görünür bir ateşe yönelir."},{"facet_id":"F002","role":"specialization","statement":"Ateşin ışığı, karanlıkta ve görmenin zayıf olduğu durumda hedefi bulmaya yardımcı olur."},{"facet_id":"F003","role":"associated_use","statement":"Gece görünen alev ya da ateş ile geceleri onun ışığına gelen varlık, yönelme olayına bağlı adlandırmalardır."}],"identity_rationale":"Kaynak ifadesi, gecenin karanlığında görünen bir ateşe ışığından yol bulmak, konukluk ya da iyilik ummak için yönelmeyi açıkça destekler. Aynı ifade gece görünen alevi ve bu ışığa gelen varlığı da adlandırdığı için eylem çekirdeği ile ateşin kendisini gösteren yan kullanım ayrılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"gece ateşe, ışığından yol bularak yönelmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"gecenin başında yerini bildiği ailesine yönelmek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"gece ateş ışığıyla yolunu bulmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"gece görünen alev ya da ateş"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"gece ateş ışığına gelen varlık"}],"lexicalization_note":"Ateşe, aileye veya ışığa yönelmeyi belirleyen yapılar ile gece görünen ateşi adlandıran biçimler ayrı tutulur; ateşe bağlı okuma yalın kök anlamı olarak genellenmez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; seçilenler ateş, karanlık ve görünürlük öğelerinin eylem içindeki sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal ışığa doğru yapılan amaçlı gece hareketini, komşu ise ışık veren nesnenin kendisini merkez alır.","focus_only":"Bu dal, gece ateşe doğru hareketi ve ışıkla yön bulmayı gerektirir.","gloss":"ateşe yönelme ile ışık kaynağı","neighbor_only":"Komşu, ışık veren aracı veya genel olarak parlak bir nesneyi adlandırır.","neighbor_ref":"root_000693/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da karanlığı gideren görünür bir ışık kaynağı vardır."},{"boundary_match":"thematic_only","distinction":"Karanlık bu dalda aşılmaya çalışılan ortamdır; komşuda ise doğrudan adlandırılan durumdur.","focus_only":"Bu dal karanlıkta ateşe ulaşmayı ve ondan yol bulmayı anlatır.","gloss":"karanlıkta ateşe yönelme","neighbor_only":"Komşu karanlığın ve seçilemezliğin kendisini anlatır.","neighbor_ref":"root_001017/B001","relation_type":"thematic","shared_zone":"Gece karanlığı, ateşe yönelme olayının koşulunu oluşturur."},{"boundary_match":"partial","distinction":"Komşu görünürlüğün ortaya çıkışını, bu dal ise görünen ateşi hedef alan hareketi bildirir.","focus_only":"Bu dal belirli bir ışık kaynağına geceleyin yönelme eylemini içerir.","gloss":"görünen ateşe yönelme","neighbor_only":"Komşu herhangi bir şeyin gizlilikten çıkıp görünür hale gelmesini anlatır.","neighbor_ref":"root_000256/B001","relation_type":"near_neighbor","shared_zone":"Hedefin görünür olması, karanlıkta onu bulmayı mümkün kılar."}],"source_phrase_ar":"عشوت إلى ناره ولا يكون ذلك إلا أن تخبط إليه الظلام (maqayis)؛ العاشية كل شيء يعشو بالليل إلى ضوء نار (maqayis)؛ عشوته قصدته ليلا (sihah)؛ عشوت إلى النار إذا استدللت عليها ببصر ضعيف (sihah)؛ عشا يعشو إذا أتى نارا للضيافة (tahdhib)؛ العشو إتيانك نارا ترجو عندها هدى أو خيرا (tahdhib)؛ استعشى فلان نارا إذا اهتدى بها (tahdhib)؛ العشوة أيضا الشعلة من النار (tahdhib)؛ عشوت النار قصدتها ليلا (mufradat)؛ النار التي تبدو بالليل عشوة (mufradat)","source_summary":"Kaynaklar, gece ateşe doğru gitme ile ateş ışığından yol bulma konusunda birleşir; konukluk veya iyilik beklentisini ve gece görünen alev adını da bu olayın çevresine yerleştirir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه قصد النار ليلا والاستدلال بضوئها والاهتداء بها والنار أو الشعلة التي تبدو في الليل","what_is_not_ar":"ليس الإعراض عنها ولا مجرد وقت العشاء ولا طعامه"},"support_links":[]},{"boundary":"Buradaki görmeme isteğe bağlı veya aktarmalıdır; duyusal görme zayıflığı ve ateşe yönelme bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001017/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عِشَآء","morph_features":"STEM|POS:N|LEM:Ei$aA^'|ROOT:E$w|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"12:16:3:1","qac_word_ref":"12:16:3","surface_ar":"عِشَآءً"}],"gloss":"görmezden gelip yüz çevirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bildiği ya da görebileceği bir şeyi bilmez veya görmez gibi davranır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dikkatini bir şeyden isteyerek çeker ve onu göz ardı ederek yüz çevirir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başkasının hakkını görmezden gelme, ona haksızlık etme sonucuna varabilir."}}],"root_ar":"ع ش و","root_id":"root_001017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyi isteyerek dikkate almama ve ondan uzak durma çekirdeğini birlikte karşılar.","boundary_detail":"Buradaki görmeme isteğe bağlı veya aktarmalıdır; duyusal görme zayıflığı ve ateşe yönelme bu dala girmez.","branch_image_ar":"التعامي والإعراض","concept_gloss":"görmezden gelip yüz çevirme","contextual_glosses":[{"applicability":"Kişinin bildiği bir işi veya durumu kasıtlı olarak tanımıyormuş gibi gösterdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilginin varlığına karşın bilgisizlik görünümü verme davranışını korur."},"facet_ids":["F001"],"text":"bilmiyormuş gibi davranma","usage_role":"contextual"},{"applicability":"Göz ardı etmenin başkasının hakkını çiğneme sonucunu doğurduğu kullanımlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hakkı dikkate almama ile ortaya çıkan haksızlık arasındaki ilişkiyi korur."},"facet_ids":["F003"],"text":"birinin hakkını görmezden gelerek ona haksızlık etme","usage_role":"explanatory"}],"definition":"Bir şeyi görmüyor veya bilmiyor gibi davranarak onu dikkate almamak ve ondan yüz çevirmektir. Birinin hakkını böylece göz ardı etmek, davranışın haksızlığa varan uzantısıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bildiği ya da görebileceği bir şeyi bilmez veya görmez gibi davranır."},{"facet_id":"F002","role":"core","statement":"Dikkatini bir şeyden isteyerek çeker ve onu göz ardı ederek yüz çevirir."},{"facet_id":"F003","role":"extension","statement":"Başkasının hakkını görmezden gelme, ona haksızlık etme sonucuna varabilir."}],"identity_rationale":"Kaynak ifadesi, bir şeyi bilmez veya görmez gibi davranmayı, ondan yüz çevirmeyi ve bir hakkı görmezden gelerek haksızlık etmeyi aynı davranış çizgisinde açıkça verir. Dal çerçevesi bu ortak çekirdeği ve onun sonuç doğuran uzantısını doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bilmezden gelme"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bir işi bilmez ve görmez gibi davranmak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"bir şeyden yüz çevirmek veya onu görmezden gelmek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"birinin hakkını görmezden gelip ona haksızlık etmek"}],"lexicalization_note":"Bilmezden gelme biçimi ile bir şeyden ya da bir haktan yüz çevirmeyi belirleyen yapılar ayrı bağlamlara bağlıdır; hepsi yalın bir görme kusuru olarak yorumlanmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yararlı ayrımlar kasıtlı görmezlik, dikkatin dağılması, susma ve gerçek görme kusuru çevresindedir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal isteyerek görmezlikten gelmeyi, komşu ise dikkatin başka bir uğraşla dağılmasını merkez alır.","focus_only":"Bu dal, bilerek görmezlikten gelme ve bilmiyormuş gibi davranma tutumunu içerir.","gloss":"yüz çevirme ve oyalanıp uzaklaşma","neighbor_only":"Komşu, başka bir şeyin kişiyi meşgul edip asıl şeyden uzaklaştırmasını da içerir.","neighbor_ref":"root_001382/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi bırakma ve ondan yüz çevirme sonucunda buluşur."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeğinde dikkati geri çekmek vardır; komşuda belirleyici davranış suskunluktur.","focus_only":"Bu dal yüz çevirme ve bilmez görünme davranışını genel olarak anlatır.","gloss":"görmezden gelme ve susma","neighbor_only":"Komşu, görmezden gelmeye özellikle susmayı eşlik ettirir.","neighbor_ref":"root_000393/B005","relation_type":"near_neighbor","shared_zone":"İki dalda da kişi bildiği bir şeye tepki vermemeyi seçer."},{"boundary_match":"thematic_only","distinction":"Biri kişinin tutumunu, diğeri görme duyusunun durumunu anlatır; normal bağlamda birbirinin yerine geçmez.","focus_only":"Bu dalda görmeme, iradi bir tutum veya davranış benzetmesidir.","gloss":"görmezden gelme ile az görme","neighbor_only":"Komşuda görmeme, duyusal yetinin gerçek ve körlüğe varmayan zayıflığıdır.","neighbor_ref":"root_001017/B006","relation_type":"thematic","shared_zone":"Her iki dal görmeme görüntüsünden yararlanır."}],"source_phrase_ar":"التعاشي التجاهل في الأمر (maqayis)؛ عشوت عنه (sihah)؛ ومن يعش عن ذكر الرحمن (sihah)؛ تعاشى الرجل في أمري إذا تجاهل (tahdhib)؛ عشي الرجل عن حق أصحابه إذا ظلمهم (tahdhib)؛ عشي علي فلان ظلمني (tahdhib)؛ عشوت عنها أي أعرضت عنها (tahdhib)؛ عشي عن كذا نحو عمي عنه (mufradat)؛ ومن يعش عن ذكر الرحمن (mufradat)","source_summary":"Kaynaklar bilmezden gelme, görmezden gelme ve yüz çevirme çekirdeğinde birleşir; başkasının hakkını göz ardı ederek ona haksızlık etmeyi bunun sonuç doğuran bir kullanımı olarak verir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه التعاشي والتجاهل والإعراض عن الشيء والتعامي عنه وما يتفرع عنه من العمى عن الحق والظلم به","what_is_not_ar":"ليس القصد إلى النار بقولهم عشا إلى ولا ضعف البصر الحسي وحده"},"support_links":[]},{"boundary":"Dalın zaman sınırı tek bir saate indirgenemez; öğle sonrası, gün sonu ve gece başlangıcını kaynaklardaki kullanıma göre ayırmak gerekir.","branch_kind":"mixed_non_bare","branch_ref":"root_001017/B004","candidate_links":[{"candidate_id":"cand_4cde9758ac8f9521d8ff","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عِشَآء","morph_features":"STEM|POS:N|LEM:Ei$aA^'|ROOT:E$w|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"12:16:3:1","qac_word_ref":"12:16:3","surface_ar":"عِشَآءً"}],"gloss":"öğle sonrasından gecenin başına uzanan akşam vakti","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Zaman aralığı öğle sonrasından gün sonuna ve gecenin başlangıcına kadar uzanabilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tek bir güne bağlanan biçim, o günün akşam bölümünü gösterir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Daha dar sınırlandırmada dönem gün batımından gecenin koyulaşmasına kadardır; başlangıç sınırı kaynaklar arasında değişir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Gün batımından sonraki gece namazı ve gün batımıyla gecenin koyulaşma vaktini birlikte anan adlar bu zaman alanına bağlıdır."}}],"root_ar":"ع ش و","root_id":"root_001017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Değişen kaynak sınırlarını tek bir saate indirmeden dalın geniş zaman çekirdeğini karşılar.","boundary_detail":"Dalın zaman sınırı tek bir saate indirgenemez; öğle sonrası, gün sonu ve gece başlangıcını kaynaklardaki kullanıma göre ayırmak gerekir.","branch_image_ar":"وقت العشي والعشاء","concept_gloss":"öğle sonrasından gecenin başına uzanan akşam vakti","contextual_glosses":[{"applicability":"Zaman adının yalnızca belirli bir günün akşam bölümüne bağlandığı kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Akşam zamanını tek bir güne özgü kılan sınırı korur."},"facet_ids":["F002"],"text":"bir günün akşamı","usage_role":"contextual"},{"applicability":"Zaman aralığının gün batımından gece karanlığının yerleşmesine kadar daraltıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dar kullanımın başlangıç ve bitiş sınırlarını açıkça korur."},"facet_ids":["F003"],"text":"gün batımı ile gecenin koyulaşması arası","usage_role":"contextual"},{"applicability":"Zaman adının gün batımı namazından sonra kılınan namazı belirttiği kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Namazın gece başlangıcındaki sırasını ve zamana bağlılığını korur."},"facet_ids":["F004"],"text":"gün batımından sonraki gece namazı","usage_role":"contextual"}],"definition":"Günün öğle sonrasından başlayıp son bölümüne ve gecenin başlangıcına uzanabilen zaman alanıdır; kaynaklara göre dar kullanım gün batımı ile gecenin koyulaşması arasındadır. Tek bir günün akşamını ve bu aralıktaki namaz vakitlerini adlandıran özel kullanımları da vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Zaman aralığı öğle sonrasından gün sonuna ve gecenin başlangıcına kadar uzanabilir."},{"facet_id":"F002","role":"specialization","statement":"Tek bir güne bağlanan biçim, o günün akşam bölümünü gösterir."},{"facet_id":"F003","role":"source_variant","statement":"Daha dar sınırlandırmada dönem gün batımından gecenin koyulaşmasına kadardır; başlangıç sınırı kaynaklar arasında değişir."},{"facet_id":"F004","role":"associated_use","statement":"Gün batımından sonraki gece namazı ve gün batımıyla gecenin koyulaşma vaktini birlikte anan adlar bu zaman alanına bağlıdır."}],"identity_rationale":"Kaynak ifadesi dalı günün son bölümü ve gece başlangıcındaki zaman alanı olarak doğrular, ancak başlangıç sınırını kimi yerde öğle sonrasına, kimi yerde gün batımına koyar. Tek bir günün akşamı, gün batımı ile gecenin koyulaşması arasındaki bölüm ve bu bölümdeki namaz adları, bu değişken zaman çekirdeğinin ayrı kullanımlarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"öğle sonrasından gecenin başına uzanan akşam vakti"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bir günün akşamı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"gün batımından gecenin koyulaşmasına kadarki vakit; bu vakitteki gece namazı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"gün batımı ve gecenin koyulaşma vakitleri"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"gün batımı namazından sonraki gece namazı"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"akşamcık; akşam sözünün küçültme biçimi"}],"lexicalization_note":"Yalın zaman adları ile belirli namaz adı ve iki vakti birlikte gösteren biçim aynı zaman alanına bağlıdır; namaza özgü okuma bütün dala yayılmaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; seçilen karşılaştırmalar gün sonu, gün batımı sonrası ışık, gecenin ilerleyen vakti ve karanlık arasındaki sınırları kapsar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın sınırı daha geniş ve değişkendir, gece başlangıcına taşabilir; komşu gün batımından önceki son bölümde yoğunlaşır.","focus_only":"Bu dal öğle sonrasından gece başlangıcına kadar uzanabilir ve gece namazı kullanımını içerir.","gloss":"akşam vakti ve gün sonu","neighbor_only":"Komşu, özellikle ikindi sonrası ile gün batımı arasındaki gün sonu vaktine bağlıdır.","neighbor_ref":"root_000038/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da günün son bölümünü adlandırabilir."},{"boundary_match":"partial","distinction":"Biri zamanı, öteki o sırada görülen ışık ve renk olayını adlandırır.","focus_only":"Bu dal, günün sonundan gece başlangıcına uzanan zaman aralığıdır.","gloss":"akşam vakti ile alacakaranlık kızıllığı","neighbor_only":"Komşu, güneş battıktan sonra gökte kalan kızıl ışık olgusudur.","neighbor_ref":"root_000803/B002","relation_type":"near_neighbor","shared_zone":"İki dal gün batımından sonraki aynı zaman aralığında örtüşebilir."},{"boundary_match":"field_only","distinction":"Bu dal geçiş ve başlangıç dönemindedir; komşu bu sınırın sonrasına yerleşir.","focus_only":"Bu dal gün sonundan gecenin koyulaşmasına kadar uzanan dönemi kapsar.","gloss":"akşam ile gecenin ilerleyen vakti","neighbor_only":"Komşu, gecenin koyulaşmasından sonraki daha geç bir vakti gösterir.","neighbor_ref":"root_001185/B004","relation_type":"same_field","shared_zone":"Her iki dal gece çevresindeki zaman bölümlerini adlandırır."},{"boundary_match":"field_only","distinction":"Zamanın kendisi ile o zamanda oluşan karanlık birbirinden ayrıdır.","focus_only":"Bu dal bir zaman aralığını adlandırır.","gloss":"akşam zamanı ile akşam karanlığı","neighbor_only":"Komşu o zaman çevresindeki karanlık ve seçilemezlik durumunu adlandırır.","neighbor_ref":"root_001017/B001","relation_type":"same_field","shared_zone":"İki dal gecenin başladığı dönemde birlikte görülebilir."}],"source_phrase_ar":"العشي آخر النهار (maqayis)؛ فإذا قلت عشية فهو ليوم واحد (maqayis)؛ كل ما كان بعد الزوال فهو عشي (maqayis)؛ العشي والعشية من صلاة المغرب إلى العتمة (sihah)؛ العشاء بالكسر والمد مثل العشي (sihah)؛ العشاءان المغرب والعتمة (sihah)؛ صلاة العشاء هي التي بعد صلاة المغرب (tahdhib)؛ إذا زالت الشمس دعي ذلك الوقت العشي (tahdhib)؛ العشاء من صلاة المغرب إلى العتمة (mufradat)","source_summary":"Kaynaklar günün son bölümü ile gece başlangıcını ortak alan olarak verir, fakat başlangıcı öğle sonrası veya gün batımı olarak farklı sınırlar. Tek günlük akşam, gün batımı ile gecenin koyulaşması arası ve bu aralıktaki namaz adları aynı geniş zaman alanında toplanır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه العشي والعشية وآخر النهار وما بعد الزوال والعشاء وقت المغرب إلى العتمة والعشاءان","what_is_not_ar":"ليس طعام العشاء ولا ظلمة العشاء من حيث هي ظلمة"},"support_links":["sup_4ab61dc1ae9bc0f6043a"]},{"boundary":"Dal iki paralel kullanım taşır: insanların akşam öğünü ve develerin akşam ya da öğleden sonra otlatılması.","branch_kind":"mixed_non_bare","branch_ref":"root_001017/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عِشَآء","morph_features":"STEM|POS:N|LEM:Ei$aA^'|ROOT:E$w|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"12:16:3:1","qac_word_ref":"12:16:3","surface_ar":"عِشَآءً"}],"gloss":"akşam yemeği ve akşam otlatması","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanlara ilişkin kullanım, günün sonunda veya gecenin başında yenen öğünü ve bu öğünü yeme ya da yedirme eylemlerini kapsar."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvanlara ilişkin kullanım, develerin akşam çevresinde otlamasını veya otlatılmasını anlatır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Otlatma zamanı gün batımından gecenin ilk üçte birine kadar ya da öğleden gün batımına kadar sınırlandırılabilir."}}],"root_ar":"ع ش و","root_id":"root_001017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Zaman bağıyla birleşen insan öğünü ve hayvan otlatma çizgilerini birbirine karıştırmadan birlikte gösterir.","boundary_detail":"Dal iki paralel kullanım taşır: insanların akşam öğünü ve develerin akşam ya da öğleden sonra otlatılması.","branch_image_ar":"طعام العشاء وتعشي الراعية","concept_gloss":"akşam yemeği ve akşam otlatması","contextual_glosses":[{"applicability":"İnsanların gün sonundaki öğünü yemesi ya da başkasına sunması anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öğünün zamanını ve yeme ile yedirme arasındaki katılımcı farkını korur."},"facet_ids":["F001"],"text":"akşam yemeği yeme veya yedirme","usage_role":"contextual"},{"applicability":"Hayvanların günün sonu veya gecenin ilk bölümündeki otlaması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Develeri, otlatma eylemini ve değişken akşam zamanını korur."},"facet_ids":["F002","F003"],"text":"develeri akşam çevresinde otlatma","usage_role":"contextual"}],"definition":"Günün sonunda veya gecenin başında yenen öğünü, bu öğünü yeme ve başkasına yedirme eylemlerini anlatır. Ayrı bir kullanım çizgisinde de develerin gün batımından gecenin ilk üçte birine dek, kimi kullanımda ise öğleden gün batımına dek otlatılmasını gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanlara ilişkin kullanım, günün sonunda veya gecenin başında yenen öğünü ve bu öğünü yeme ya da yedirme eylemlerini kapsar."},{"facet_id":"F002","role":"extension","statement":"Hayvanlara ilişkin kullanım, develerin akşam çevresinde otlamasını veya otlatılmasını anlatır."},{"facet_id":"F003","role":"source_variant","statement":"Otlatma zamanı gün batımından gecenin ilk üçte birine kadar ya da öğleden gün batımına kadar sınırlandırılabilir."}],"identity_rationale":"Kaynak ifadesi hem günün sonunda veya gecenin başında yenen öğünü ve onu yeme ya da yedirme eylemlerini, hem de develerin akşam çevresindeki otlamasını verir. Bu iki alan zaman bağlantısıyla bir aradadır, ancak yemek ile hayvan otlatma aynı eylem gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"günün sonunda veya gecenin başında yenen akşam yemeği"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"akşam yemeği yemek"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"birine akşam yemeği yedirmek"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"gece otlayan develer"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"develeri gece veya öğleden sonra otlatmak"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"Akşam otlayan sürü, otlamayanı da harekete geçirir."}],"lexicalization_note":"Yemek adı, yeme ve yedirme yapıları, hayvan otlatma biçimleri ve atasözü niteliğindeki tamlama ayrı kapsamlarını korur; otlatma anlamı yalın yemek adına taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sabah karşılığı, genel otlatma ve akşam zamanı, dalın iki kullanım çizgisini açıklayan en yararlı sınırlardır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Eylem alanları benzer olsa da onları ayıran temel sınır günün karşıt bölümleridir.","focus_only":"Bu dal akşam öğününü ve akşam çevresindeki otlatmayı içerir.","gloss":"akşam ve sabah beslenmesi","neighbor_only":"Komşu sabah öğününü ve günün ilk bölümündeki otlatmayı içerir.","neighbor_ref":"root_000904/B003","relation_type":"same_field","shared_zone":"İki dalda da belirli bir gündelik vakitte yemek veya otlamak vardır."},{"boundary_match":"partial","distinction":"Bu dalda zaman ve hayvan türü belirgindir; komşuda esas olan sürünün otlamaya bırakılmasıdır.","focus_only":"Bu dal otlatmayı akşam veya öğleden sonra zamanına ve özellikle develere bağlar.","gloss":"akşam otlatması ile serbest otlatma","neighbor_only":"Komşu, hayvanları genel olarak serbest otlamaya bırakmayı anlatır.","neighbor_ref":"root_000576/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal hayvanların otlaması için salınmasını kapsayabilir."},{"boundary_match":"thematic_only","distinction":"Biri o vakitte gerçekleşen beslenme eylemlerini, öteki vaktin kendisini gösterir.","focus_only":"Bu dal akşam vaktinde yapılan yemek ve otlatma etkinliklerini anlatır.","gloss":"akşam etkinliği ile akşam vakti","neighbor_only":"Komşu etkinlikten bağımsız olarak akşam zamanını adlandırır.","neighbor_ref":"root_001017/B004","relation_type":"thematic","shared_zone":"Akşam zamanı, yemek ve otlatma kullanımlarının ortak ortamıdır."}],"source_phrase_ar":"العشاء هو الطعام الذي يؤكل من آخر النهار وأول الليل (maqayis)؛ عشيت الإبل إذا تعشت فهي عاشية (sihah)؛ العواشي هي التي ترعى ليلا (sihah)؛ عشوت أي تعشيت (sihah)؛ عشوته فتعشى أي أطعمته عشاء (sihah)؛ عشيت الإبل إذا رعيتها بعد غروب الشمس إلى ثلث الليل (tahdhib)؛ عشيتها أيضا إذا رعيتها بعد الزوال إلى غروب الشمس (tahdhib)؛ عشيت الرجل إذا أطعمته العشاء (tahdhib)؛ العواشي الإبل التي ترعى ليلا (mufradat)؛ العشاء طعام العشاء (mufradat)","source_summary":"Kaynaklar akşam öğünü, bu öğünü yeme ve yedirme ile develerin gece otlamasını ortak biçimde verir. Otlatmanın zaman sınırı, gün batımı sonrasındaki ilk gece bölümü ile öğleden gün batımına kadarki dönem arasında değişir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه طعام العشاء والتعشي وإطعام العشاء ورعي الإبل ليلا أو بعد الزوال وما يتصل بالعواشي","what_is_not_ar":"ليس صلاة العشاء ولا وقت العشاء مجردا عن الطعام أو الرعي"},"support_links":[]},{"boundary":"Çekirdek tam körlük değil, görmenin zayıflamasıdır; geceye özgü yetersizlik bunun baskın fakat tek olmayan görünümüdür.","branch_kind":"mixed_non_bare","branch_ref":"root_001017/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عِشَآء","morph_features":"STEM|POS:N|LEM:Ei$aA^'|ROOT:E$w|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"12:16:3:1","qac_word_ref":"12:16:3","surface_ar":"عِشَآءً"}],"gloss":"körlüğe varmayan, özellikle gece belirginleşen görme zayıflığı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Görme yetisi zayıftır, ancak bütünüyle ortadan kalkmış değildir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yaygın görünümde kişi gündüz görürken gece göremez."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Durum genel görme zayıflığı veya gözün önüne karanlık çökmesi biçiminde de anlatılır."}}],"root_ar":"ع ش و","root_id":"root_001017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın genel duyusal çekirdeğini ve en belirgin gece koşulunu birlikte karşılar.","boundary_detail":"Çekirdek tam körlük değil, görmenin zayıflamasıdır; geceye özgü yetersizlik bunun baskın fakat tek olmayan görünümüdür.","branch_image_ar":"ضعف البصر والعشا","concept_gloss":"körlüğe varmayan, özellikle gece belirginleşen görme zayıflığı","contextual_glosses":[{"applicability":"Görme kaybının özellikle gece ortaya çıktığı dar kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gündüz ve gece arasındaki görme karşıtlığını eksiksiz korur."},"facet_ids":["F002"],"text":"gündüz görüp gece görememe","usage_role":"contextual"},{"applicability":"Görme zayıflığının gözde beliren karanlık görüntüsüyle anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Duyusal zayıflığın karanlık görüntüsü olarak algılanmasını korur."},"facet_ids":["F003"],"text":"gözün önüne karanlık çökmesi","usage_role":"explanatory"}],"definition":"Tam körlük olmayan bir görme zayıflığıdır; en belirgin biçiminde kişi gündüz görebildiği halde gece göremez. Gözün önüne karanlık çökmüş gibi olması, bu duyusal yetersizliğin anlatımıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Görme yetisi zayıftır, ancak bütünüyle ortadan kalkmış değildir."},{"facet_id":"F002","role":"specialization","statement":"Yaygın görünümde kişi gündüz görürken gece göremez."},{"facet_id":"F003","role":"source_variant","statement":"Durum genel görme zayıflığı veya gözün önüne karanlık çökmesi biçiminde de anlatılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Görmenin bütünüyle yok olması anlamını ekler.","collision":"Tam görme kaybını anlatan ayrı dallarla karışır.","fit":"broadening","loses":null,"preserves":"Görme yetisindeki ciddi yetersizlik alanını korur."},"text":"körlük"}],"identity_rationale":"Kaynak ifadesi körlükten ayrı bir görme zayıflığını ve özellikle gündüz görebildiği halde gece göremeyen kişiyi açıkça destekler. Bununla birlikte genel görme zayıflığı ve gözün önüne karanlık çökmesi anlatımları da bulunduğundan dal yalnızca tek bir gece görme bozukluğuna indirgenmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"özellikle geceleri görülen görme zayıflığı"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"görmesi zayıf veya geceleri göremeyen kişi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"görmesi zayıf kişiler"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"görmesi zayıfmış gibi davranmak"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"görmesi zayıf veya geceleri göremeyen kadın"}],"lexicalization_note":"Görme zayıflığını adlandıran biçimler, bundan etkilenen kişi adları ve öyleymiş gibi davranma yapısı ayrı işlevler taşır; davranış biçimi gerçek bozuklukla özdeşleştirilmez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; seçilenler genel görme zayıflığı, tam körlük ve sağlam görme eksenindeki temel sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal zaman koşuluyla, komşu ise gözdeki puslu ve donuk algıyla daha güçlü biçimde sınırlanır.","focus_only":"Bu dal özellikle gündüz görüp gece görememe örüntüsünü belirginleştirir.","gloss":"gece görme zayıflığı ile puslu görme","neighbor_only":"Komşu gözdeki puslanma ve donuk görme biçimlerini merkez alır.","neighbor_ref":"root_001094/B002","relation_type":"near_synonym","shared_zone":"Her iki dal körlüğe varmayan görme zayıflığını anlatır."},{"boundary_match":"partial","distinction":"Bu dal kalan görme yetisini korur; komşunun çekirdeği görmenin doğuştan ya da bütünüyle yokluğudur.","focus_only":"Bu dalda görme zayıftır ve özellikle geceleri kaybolabilir, fakat tam körlük zorunlu değildir.","gloss":"görme zayıflığı ile körlük","neighbor_only":"Komşu doğuştan körlüğü veya gözün bütünüyle görmez hale gelmesini merkez alır.","neighbor_ref":"root_001320/B001","relation_type":"near_neighbor","shared_zone":"İki dal da kişinin görme yetisindeki ciddi bir yetersizliği anlatır."},{"boundary_match":"opposed","distinction":"Komşu yetinin işlemesini, bu dal ise yetinin körlüğe varmayan eksilmesini gösterir.","focus_only":"Bu dal görme yetisinin zayıf veya gece etkisiz olmasını anlatır.","gloss":"görme yetisi ve görme yetersizliği","neighbor_only":"Komşu gözün görme ve bakarak algılama yetisini olumlu kutupta anlatır.","neighbor_ref":"root_000121/B001","relation_type":"polarity_pair","shared_zone":"Her iki dal aynı duyusal eksen olan gözle görme üzerinde yer alır."}],"source_phrase_ar":"العشا مقصور مصدر الأعشى والمرأة عشواء (maqayis)؛ الذي لا يبصر بالليل وهو بالنهار بصير (maqayis)؛ العشا مصدر الأعشى وهو الذي لا يبصر بالليل ويبصر بالنهار (sihah)؛ العشو جمع الأعشى (tahdhib)؛ العشا يكون سوء البصر من غير عمى (tahdhib)؛ يكون الذي لا يبصر بالليل ويبصر بالنهار (tahdhib)؛ عشا يعشو إذا ضعف بصره (tahdhib)؛ العشا ظلمة تعترض في العين (mufradat)؛ رجل أعشى وامرأة عشواء (mufradat)","source_summary":"Kaynaklar körlüğe varmayan görme zayıflığı üzerinde birleşir ve gündüz görebilip gece görememeyi başlıca görünüm olarak verir. Daha geniş anlatım, genel görme zayıflığını ve gözde beliren karanlığı da kapsar.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه العشا في العين والأعشى والعشواء ومن لا يبصر بالليل أو يضعف بصره","what_is_not_ar":"ليس التعاشي بمعنى التجاهل ولا خبط الأمر بلا بصيرة إلا من جهة التشبيه"},"support_links":[]},{"boundary":"Dal salt görme kusurunu değil, görememenin yol açtığı gelişigüzel çarpma ve düşüncesizce işe girişme davranışını anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001017/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عِشَآء","morph_features":"STEM|POS:N|LEM:Ei$aA^'|ROOT:E$w|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"12:16:3:1","qac_word_ref":"12:16:3","surface_ar":"عِشَآءً"}],"gloss":"önünü görmeden sonuç düşünmeksizin ilerleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Önünü göremeyen dişi deve, ön ayaklarıyla karşısına çıkan şeylere gelişigüzel çarpar."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsan için kullanım, ne yaptığını bilmeden ve sonucu önemsemeden bir işe girişmeyi anlatır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen kullanım, birini doğru yönü belli olmayan ve sonu kestirilemeyen bir işe sürüklemektir."}}],"root_ar":"ع ش و","root_id":"root_001017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem hayvanın fiziksel hareketini hem de insanın düşüncesizce işe girişmesini taşıyan ortak davranış görüntüsünü karşılar.","boundary_detail":"Dal salt görme kusurunu değil, görememenin yol açtığı gelişigüzel çarpma ve düşüncesizce işe girişme davranışını anlatır.","branch_image_ar":"خبط العشواء","concept_gloss":"önünü görmeden sonuç düşünmeksizin ilerleme","contextual_glosses":[{"applicability":"Kişinin bir işin yönünü ve sonucunu araştırmadan ona giriştiği aktarmalı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilgisizce girişmeyi ve sonucu önemsememe tutumunu korur."},"facet_ids":["F002"],"text":"körlemesine ve sonucu düşünmeden davranma","usage_role":"contextual"},{"applicability":"Eyleyenin başka bir kişiyi doğru yolu belli olmayan bir işe soktuğu kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ettirgen katılımcı değişimini ve işin belirsizliğini birlikte korur."},"facet_ids":["F003"],"text":"birini yönü belirsiz bir işe sürükleme","usage_role":"explanatory"}],"definition":"Önünü göremeyen dişi devenin ön ayaklarıyla çevresindeki şeylere gelişigüzel çarpmasıdır. Bu görüntü, ne yaptığını ve sonucunu bilmeden bir işe girişmeye veya birini doğru yönü belli olmayan bir işe sürüklemeye aktarılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Önünü göremeyen dişi deve, ön ayaklarıyla karşısına çıkan şeylere gelişigüzel çarpar."},{"facet_id":"F002","role":"extension","statement":"İnsan için kullanım, ne yaptığını bilmeden ve sonucu önemsemeden bir işe girişmeyi anlatır."},{"facet_id":"F003","role":"extension","statement":"Ettirgen kullanım, birini doğru yönü belli olmayan ve sonu kestirilemeyen bir işe sürüklemektir."}],"identity_rationale":"Kaynak ifadesi, önünü göremediği için ön ayaklarıyla çevresine çarpan dişi deveyi ve bu görüntünün ne yaptığını bilmeden, sonucu düşünmeden işe girişen kişiye aktarılmasını açıkça verir. Birini doğru yönü belli olmayan bir işe sürükleme de aynı aktarmalı yapı içinde desteklenir.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"önünü göremeyip karşısına çıkanlara çarpan dişi deve"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"körlemesine ve sonucunu düşünmeden davranmak"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"bir işi ne yaptığını bilmeden yürütmek"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"birini doğru yönü belli olmayan bir işe sürüklemek"}],"lexicalization_note":"Hayvan adı ile gelişigüzel davranmayı ve birini belirsiz işe sürüklemeyi anlatan kalıplaşmış yapılar ayrıdır; aktarmalı eylem yalın görme kusuru sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler bilgisizlik, karanlıkta ayırt edememe ve duyusal görme zayıflığıyla eylem çekirdeğinin farkını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu bilişsel yetersizliği, bu dal ise o yetersizliğin doğurduğu düşüncesiz eylemi merkez alır.","focus_only":"Bu dal, yönü görememenin sonucunda gelişigüzel ve düşüncesizce hareket etmeyi içerir.","gloss":"körlemesine davranma ve içgörü yoksunluğu","neighbor_only":"Komşu, doğruyu kavrayamama ve içsel yön bulma yetisinin yokluğunu durum olarak anlatır.","neighbor_ref":"root_001049/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da doğru yönü seçememe ve bilgisizlik bulunur."},{"boundary_match":"partial","distinction":"Bu dal yönsüz ilerlemeyi, komşu ise seçmeden toplama sonucu ortaya çıkan karışıklığı öne çıkarır.","focus_only":"Bu dal önünü görmeden işe girişme ve sonuçları önemsememe davranışıdır.","gloss":"körlemesine ilerleme ve seçmeden toplama","neighbor_only":"Komşu, karanlıkta ne topladığını seçemeyen kişinin iyiyle kötüyü karıştırması benzetmesidir.","neighbor_ref":"root_000335/B002","relation_type":"near_neighbor","shared_zone":"İki dal karanlıkta seçememe görüntüsünü düşüncesiz davranışa aktarır."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği hareket ve çarpmadır; komşunun çekirdeği görme yetisinin zayıflığıdır.","focus_only":"Bu dal görmemenin yol açtığı çarpma eylemini ve onun insan davranışına aktarımını içerir.","gloss":"göremeyerek çarpma ve görme zayıflığı","neighbor_only":"Komşu insanın körlüğe varmayan görme zayıflığını durum olarak anlatır.","neighbor_ref":"root_001017/B006","relation_type":"near_neighbor","shared_zone":"Her iki dalda da yeterince görememe fiziksel bir temel oluşturur."}],"source_phrase_ar":"العشواء من النوق التي كأنها لا تبصر ما أمامها فتخبط كل شيء بيديها (maqayis)؛ في عشواء من أمرهم (maqayis)؛ العشواء الناقة التي لا تبصر أمامها فهي تخبط بيديها كل شيء (sihah)؛ ركب فلان العشواء إذا خبط أمره على غير بصيرة (sihah)؛ العشوة أن تركب أمرا على غير بيات (sihah)؛ يخبط خبط عشواء يضرب مثلا للسادر الذي يركب رأسه ولا يهتم لعاقبته (tahdhib)؛ أوطأته عشوة حمله على أن يركب أمرا غير مستبين الرشد (tahdhib)؛ يخبط خبط عشواء (mufradat)","source_summary":"Kaynaklar önünü göremeyen dişi devenin çevresine çarpması görüntüsünde ve bunun düşünmeden işe girişen kişiye aktarılmasında birleşir. Sonucu umursamama ve başkasını yönü belirsiz bir işe sürükleme de bu aktarımın parçalarıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الناقة العشواء التي لا تبصر أمامها وخبطها واستعارة ذلك لمن يركب الأمر بغير بصيرة أو في أمر ملتبس","what_is_not_ar":"ليس ضعف البصر في الإنسان مجردا ولا ظلمة الليل المجردة"},"support_links":[]},{"boundary":"Anlam yalnızca belirli yapıda tanıklanır ve genel kök anlamı olarak genişletilemez.","branch_kind":"non_bare","branch_ref":"root_001017/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عِشَآء","morph_features":"STEM|POS:N|LEM:Ei$aA^'|ROOT:E$w|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"12:16:3:1","qac_word_ref":"12:16:3","surface_ar":"عِشَآءً"}],"gloss":"bir şeye yumuşak ve özenli davranma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir şeye sertlikten kaçınarak yumuşak ve özenli davranır."}}],"root_ar":"ع ش و","root_id":"root_001017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kanıtlanan yapıda, bir şeye sertlik göstermeden davranmayı karşılar.","boundary_detail":"Anlam yalnızca belirli yapıda tanıklanır ve genel kök anlamı olarak genişletilemez.","branch_image_ar":"الرفق بالشيء","concept_gloss":"bir şeye yumuşak ve özenli davranma","contextual_glosses":[{"applicability":"Davranışın yöneldiği şey bağlamda açıkça belli olduğunda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli hedefe yönelen yumuşak ve özenli tutumu korur."},"facet_ids":["F001"],"text":"ona nazikçe davranma","usage_role":"contextual"}],"definition":"Belirli bir yapıda bir şeye sertlik göstermeden, yumuşak ve özenli biçimde davranmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir şeye sertlikten kaçınarak yumuşak ve özenli davranır."}],"identity_rationale":"Kaynak ifadesi, belirli bir yapıda bir şeye yumuşak ve özenli davranma anlamını doğrudan verir. Dal çerçevesi bu tek ve yapıya bağlı tanıklığı doğru yansıtır; yüz çevirme veya bir şeye yönelme anlamlarıyla karıştırılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"bir şeye yumuşak ve özenli davranmak"}],"lexicalization_note":"Anlam belirli bir ilgeçli yapıya bağlıdır; yalın biçime veya aynı yapının yüz çevirme okumasına otomatik olarak taşınmaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; genel yumuşak davranış ile kişiyi ölçülü idare etme, tek tanıklı yapının sınırını en iyi açıklayan komşulardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Anlam çekirdekleri yakındır, ancak bu dal yapısal olarak dar ve hedefe bağlıdır; komşu genel bir davranış alanıdır.","focus_only":"Bu dal yalnızca belirli bir yapıda bir şeye yönelen yumuşak davranışı anlatır.","gloss":"bir şeye yumuşak davranma","neighbor_only":"Komşu, yumuşaklık ve incelik alanını kişi, iş ve davranış türleri bakımından daha geniş kapsar.","neighbor_ref":"root_000583/B001","relation_type":"near_synonym","shared_zone":"İki dal da sertliğin karşıtı olan yumuşak ve incelikli davranışı anlatır."},{"boundary_match":"partial","distinction":"Bu dalın hedefi genel olabilir; komşuda insan ilişkisi ve ölçülü idare etme öğesi daha belirgindir.","focus_only":"Bu dal herhangi bir şeye yumuşak ve özenli davranmayı belirli yapıda anlatır.","gloss":"yumuşak davranma ve ölçülü idare etme","neighbor_only":"Komşu özellikle bir kişiyi kırmadan, ölçülü biçimde idare etmeyi anlatır.","neighbor_ref":"root_000485/B006","relation_type":"near_synonym","shared_zone":"Her iki dal davranışta sertlikten kaçınmayı ve inceliği korur."}],"source_phrase_ar":"عشيت عنه أيضا رفقت به (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Belirli yapının bir şeye yumuşak ve özenli davranma anlamı tek başına tanıklanır."}],"source_summary":"Bu anlam yalnızca tek bir kaynakta ve belirli bir dil bilgisel yapı içinde tanıklanır.","sources":["TA"],"what_is_ar":"يدخل فيه عشي عنه بمعنى رفق به كما نقلته التهذيب","what_is_not_ar":"ليس الإعراض عنه ولا التعامي عنه ولا القصد إليه"},"support_links":[]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000147/B001","candidate_links":[{"candidate_id":"cand_4cde9758ac8f9521d8ff","lane":"micro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3db8bcc0f1d6b1e17206","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Sorrow, tears, and voice supply the manifest affect carried into the encounter.","root":"ب ك ي","source_ref":"12:16","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000147","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_4ab61dc1ae9bc0f6043a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000147/B004","candidate_links":[{"candidate_id":"cand_aa705fb29494114631ca","lane":"micro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ebf305bafe75b2511784","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Affected weeping supplies the exploratory possibility of performed rather than spontaneous grief.","root":"ب ك ي","source_ref":"12:16","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000147","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_c3cc1c10df9ea680f992"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000281/B001","candidate_links":[{"candidate_id":"cand_4cde9758ac8f9521d8ff","lane":"micro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3db8bcc0f1d6b1e17206","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Ordinary coming supplies the movement that culminates before the father.","root":"ج ي ء","source_ref":"12:16","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000281","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_4ab61dc1ae9bc0f6043a"]}],"candidate_inventory":[{"anchor_refs":["12:16:1"],"branch_refs":[],"candidate_id":"cand_c9263c3a66255acf9311","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:16:1:boundary-connector","source_type":"word_analysis","support_ids":["sup_62d650cea3fd5db3ab81","sup_864185bdecab595ff165"],"title":"connected scene launch without fixed motive","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:1","qac_refs":["12:16:1:1"],"status":"accepted"}},{"anchor_refs":["12:16:1"],"branch_refs":[],"candidate_id":"cand_db8c2bc5a9e35118cf8c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:16:1:fused-liaison","source_type":"word_analysis","support_ids":["sup_864185bdecab595ff165","sup_d0f08222c2cf2629be86"],"title":"fused connector carries arrival forward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:1","qac_refs":["12:16:1:1"],"status":"accepted"}},{"anchor_refs":["12:16:2"],"branch_refs":[],"candidate_id":"cand_ac2699a448c895af27db","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:16:2:arrival-presentation-narrowed","source_type":"word_analysis","support_ids":["sup_295d2df4685866faae92","sup_c3e015c1323063854a2a"],"title":"arrival selected while presentation remains a narrative shadow","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:2","qac_refs":["12:16:1:2","12:16:1:3"],"status":"accepted"}},{"anchor_refs":["12:16:2"],"branch_refs":[],"candidate_id":"cand_03e548635d46757fc0e3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:16:2:hamza-arrival-sound","source_type":"word_analysis","support_ids":["sup_295d2df4685866faae92","sup_40f1e1ffbb66e838ac1a"],"title":"glottal catch fits completed arrival","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:2","qac_refs":["12:16:1:2","12:16:1:3"],"status":"accepted"}},{"anchor_refs":["12:16:2"],"branch_refs":[],"candidate_id":"cand_eaf7968c6522362a0fbd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:16:2:relational-and-surah-echoes","source_type":"word_analysis","support_ids":["sup_295d2df4685866faae92","sup_e608ab6c9d3971a7086d"],"title":"deceptive coming answered by later arrivals","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:2","qac_refs":["12:16:1:2","12:16:1:3"],"status":"accepted"}},{"anchor_refs":["12:16:2"],"branch_refs":[],"candidate_id":"cand_0a9f0254e6ea3c08c8c2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:16:2:scene-order-and-speech-pressure","source_type":"word_analysis","support_ids":["sup_295d2df4685866faae92","sup_dec096ef957ad80ce121"],"title":"arrival sets recipient, time, manner, then speech","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:2","qac_refs":["12:16:1:2","12:16:1:3"],"status":"accepted"}},{"anchor_refs":["12:16:2"],"branch_refs":[],"candidate_id":"cand_5d5e74007aa0d08f67ef","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:16:2:unnamed-perfect-arrival","source_type":"word_analysis","support_ids":["sup_0ec85b21cbee244f5198","sup_295d2df4685866faae92"],"title":"unnamed plural arrival as completed public action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:2","qac_refs":["12:16:1:2","12:16:1:3"],"status":"accepted"}},{"anchor_refs":["12:16:3"],"branch_refs":[],"candidate_id":"cand_90448ef579db649563de","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:16:3:accusative-arrival-target","source_type":"word_analysis","support_ids":["sup_b1469341c8db245e4b7f","sup_eb75e891ccba2e2696c9"],"title":"case marks the father as reached recipient","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:3","qac_refs":["12:16:2:1","12:16:2:2"],"status":"accepted"}},{"anchor_refs":["12:16:3"],"branch_refs":[],"candidate_id":"cand_0b1c3f8b2b23ec6dd6a2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:16:3:father-network-and-restoration","source_type":"word_analysis","support_ids":["sup_8d0aa5e73c6ec89196a2","sup_b1469341c8db245e4b7f"],"title":"deceived father-position answered later","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:3","qac_refs":["12:16:2:1","12:16:2:2"],"status":"accepted"}},{"anchor_refs":["12:16:3"],"branch_refs":[],"candidate_id":"cand_cb1d61700e0dc50d08d3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:16:3:father-sense-narrowed","source_type":"word_analysis","support_ids":["sup_a129be2284cc34cbfb1a","sup_b1469341c8db245e4b7f"],"title":"immediate father, not ancestral abstraction","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:3","qac_refs":["12:16:2:1","12:16:2:2"],"status":"accepted"}},{"anchor_refs":["12:16:3"],"branch_refs":[],"candidate_id":"cand_9cbef5a276497840dcc1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:16:3:possessive-relational-definiteness","source_type":"word_analysis","support_ids":["sup_23677b684cadf7f83b04","sup_b1469341c8db245e4b7f"],"title":"their father is defined through the brothers","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:3","qac_refs":["12:16:2:1","12:16:2:2"],"status":"accepted"}},{"anchor_refs":["12:16:4"],"branch_refs":[],"candidate_id":"cand_15f26dfb7837caa6890e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001017"],"scope":"focus_ayah","source_local_id":"12:16:4:accusative-time-adverb","source_type":"word_analysis","support_ids":["sup_3ea47a6739f7dff4523e","sup_f39f4d3332c94a1194f3"],"title":"indefinite accusative evening frames the event","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:4","qac_refs":["12:16:3:1"],"status":"accepted"}},{"anchor_refs":["12:16:4"],"branch_refs":[],"candidate_id":"cand_840bd09642477d4ec134","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001017"],"scope":"focus_ayah","source_local_id":"12:16:4:dim-perception-nightfall","source_type":"word_analysis","support_ids":["sup_3ea47a6739f7dff4523e","sup_5630b14eb0a1b2761364"],"title":"nightfall becomes a perception condition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:4","qac_refs":["12:16:3:1"],"status":"accepted"}},{"anchor_refs":["12:16:4"],"branch_refs":[],"candidate_id":"cand_91374747b2b2ab6d50d0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001017"],"scope":"focus_ayah","source_local_id":"12:16:4:form-variant-and-sound","source_type":"word_analysis","support_ids":["sup_3ea47a6739f7dff4523e","sup_e87ac41d9b8d4e0f1496"],"title":"extended evening form lingers audibly","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:4","qac_refs":["12:16:3:1"],"status":"accepted"}},{"anchor_refs":["12:16:4"],"branch_refs":[],"candidate_id":"cand_9937f23cba21bbe7bb18","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001017"],"scope":"focus_ayah","source_local_id":"12:16:4:isolated-evening-formula","source_type":"word_analysis","support_ids":["sup_3ea47a6739f7dff4523e","sup_6a8fabddf945002d4e68"],"title":"evening side appears without morning balance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:4","qac_refs":["12:16:3:1"],"status":"accepted"}},{"anchor_refs":["12:16:4"],"branch_refs":[],"candidate_id":"cand_f534c4b614cff74c04b7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001017"],"scope":"focus_ayah","source_local_id":"12:16:4:middle-beat-between-father-and-tears","source_type":"word_analysis","support_ids":["sup_3ea47a6739f7dff4523e","sup_c5d1e56cf875981bc33c"],"title":"time mediates father and tears","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:4","qac_refs":["12:16:3:1"],"status":"accepted"}},{"anchor_refs":["12:16:5"],"branch_refs":[],"candidate_id":"cand_5d0a702e76e738e8dd05","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:16:5:final-position-display","source_type":"word_analysis","support_ids":["sup_9040a36ced463fc20b48","sup_f3e1c21652116de64a51"],"title":"final word makes tears the landing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:5","qac_refs":["12:16:4:1","12:16:4:2"],"status":"accepted"}},{"anchor_refs":["12:16:5"],"branch_refs":[],"candidate_id":"cand_43fe48bd1b4bcd033399","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:16:5:form-i-causative-shadow","source_type":"word_analysis","support_ids":["sup_4c9970988354e05cbe4e","sup_f3e1c21652116de64a51"],"title":"weepers, not grammatically causers","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:5","qac_refs":["12:16:4:1","12:16:4:2"],"status":"accepted"}},{"anchor_refs":["12:16:5"],"branch_refs":[],"candidate_id":"cand_5b27c993e323d2ff03dc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:16:5:imperfect-hal-process","source_type":"word_analysis","support_ids":["sup_f3e1c21652116de64a51","sup_fd60d277e351b5a15466"],"title":"ongoing circumstantial weeping","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:5","qac_refs":["12:16:4:1","12:16:4:2"],"status":"accepted"}},{"anchor_refs":["12:16:5"],"branch_refs":[],"candidate_id":"cand_d3b812d35b74c3997987","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:16:5:plural-subject-continuity","source_type":"word_analysis","support_ids":["sup_9af37af2cda2f61bd368","sup_f3e1c21652116de64a51"],"title":"same unnamed group keeps performing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:5","qac_refs":["12:16:4:1","12:16:4:2"],"status":"accepted"}},{"anchor_refs":["12:16:5"],"branch_refs":[],"candidate_id":"cand_985fbab51cbce6f048c6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:16:5:polarity-and-arrival-contrast","source_type":"word_analysis","support_ids":["sup_2ac712073c71a200a61d","sup_f3e1c21652116de64a51"],"title":"weeping pole and arrival-manner contrast","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:5","qac_refs":["12:16:4:1","12:16:4:2"],"status":"accepted"}},{"anchor_refs":["12:16:5"],"branch_refs":[],"candidate_id":"cand_4d325cd924a1b427ce2c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:16:5:rare-verbal-root-and-proper-name-limit","source_type":"word_analysis","support_ids":["sup_e38ec02b680219e3de0b","sup_f3e1c21652116de64a51"],"title":"sparse grief verb, not sacred-place import","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:5","qac_refs":["12:16:4:1","12:16:4:2"],"status":"accepted"}},{"anchor_refs":["12:16:5"],"branch_refs":[],"candidate_id":"cand_af1ddf3dbbd5df5df7dc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:16:5:surah-grief-echo","source_type":"word_analysis","support_ids":["sup_ab467de15061d0e4b8c6","sup_f3e1c21652116de64a51"],"title":"performed tears turn toward the father","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:5","qac_refs":["12:16:4:1","12:16:4:2"],"status":"accepted"}},{"anchor_refs":["12:16:5"],"branch_refs":[],"candidate_id":"cand_a41e060731fce22aa25a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:16:5:undirected-display-and-sincerity","source_type":"word_analysis","support_ids":["sup_416d82c36724b876c175","sup_f3e1c21652116de64a51"],"title":"observable crying without stated object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:5","qac_refs":["12:16:4:1","12:16:4:2"],"status":"accepted"}},{"anchor_refs":["12:16:1"],"branch_refs":[],"candidate_id":"cand_892dbe915d4083d081ce","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000281"],"scope":"focus_ayah","source_local_id":"12:16:1:2","source_type":"qac_morpheme","support_ids":["sup_8ef0cd94fc09d3e34004"],"title":"QAC root occurrence: ج ي ء","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["12:16:2"],"branch_refs":[],"candidate_id":"cand_0d74f3449ebf928af1b1","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000007"],"scope":"focus_ayah","source_local_id":"12:16:2:1","source_type":"qac_morpheme","support_ids":["sup_e4868c657608c7e07299"],"title":"QAC root occurrence: ء ب و","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["12:16:3"],"branch_refs":[],"candidate_id":"cand_618f46f821450ff1f221","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001017"],"scope":"focus_ayah","source_local_id":"12:16:3:1","source_type":"qac_morpheme","support_ids":["sup_205900f6fca6fe450b27"],"title":"QAC root occurrence: ع ش و","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["12:16:4"],"branch_refs":[],"candidate_id":"cand_d081d42be1d7402f2c65","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000147"],"scope":"focus_ayah","source_local_id":"12:16:4:1","source_type":"qac_morpheme","support_ids":["sup_63e45fa309bed3907df8"],"title":"QAC root occurrence: ب ك ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["12:16:5"],"branch_refs":[],"candidate_id":"cand_74c2c9a569da75e58718","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:16:5:bakkah-import-rejected","source_type":"word_analysis","support_ids":["sup_b95359d4934443aec61b","sup_f3e1c21652116de64a51"],"title":"proper-name adjacency cannot govern the verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:16:5","qac_refs":["12:16:4:1","12:16:4:2"],"status":"accepted"}},{"anchor_refs":["12:16"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"12:16","branch_refs":["root_000007/B001","root_000147/B001","root_000281/B001","root_001017/B004"],"candidate_id":"cand_4cde9758ac8f9521d8ff","commentary_obligation":"review","hft_ref":"hft_3db8bcc0f1d6b1e17206","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-paternal-grief-arrival","source_type":"hft","support_ids":["sup_4ab61dc1ae9bc0f6043a"],"title":"baseline-paternal-grief-arrival","trust":"legacy_unbound"},{"anchor_refs":["12:16"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"12:16","branch_refs":["root_000007/B001","root_000147/B004","root_001017/B001"],"candidate_id":"cand_aa705fb29494114631ca","commentary_obligation":"review","hft_ref":"hft_ebf305bafe75b2511784","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-obscured-display","source_type":"hft","support_ids":["sup_c3cc1c10df9ea680f992"],"title":"baseline-obscured-display","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَجَآءُوٓ أَبَاهُمْ عِشَآءًۭ يَبْكُونَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"12:16:1:1","qac_word_ref":"12:16:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"جَآءَ","morph_features":"STEM|POS:V|PERF|LEM:jaA^'a|ROOT:jyA|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"12:16:1:2","qac_word_ref":"12:16:1","root_ar":"ج ي ء","surface_ar":"جَآءُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"12:16:1:3","qac_word_ref":"12:16:1","root_ar":"","surface_ar":"وٓ"},{"lemma_ar":"أَبٌ","morph_features":"STEM|POS:N|LEM:>abN|ROOT:Abw|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"12:16:2:1","qac_word_ref":"12:16:2","root_ar":"ء ب و","surface_ar":"أَبَا"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"12:16:2:2","qac_word_ref":"12:16:2","root_ar":"","surface_ar":"هُمْ"},{"lemma_ar":"عِشَآء","morph_features":"STEM|POS:N|LEM:Ei$aA^'|ROOT:E$w|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"12:16:3:1","qac_word_ref":"12:16:3","root_ar":"ع ش و","surface_ar":"عِشَآءً"},{"lemma_ar":"بَكَتْ","morph_features":"STEM|POS:V|IMPF|LEM:bakato|ROOT:bky|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"12:16:4:1","qac_word_ref":"12:16:4","root_ar":"ب ك ي","surface_ar":"يَبْكُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"12:16:4:2","qac_word_ref":"12:16:4","root_ar":"","surface_ar":"ونَ"}],"word_analysis_qac_refs":[["12:16:1:1"],["12:16:1:2","12:16:1:3"],["12:16:2:1","12:16:2:2"],["12:16:3:1"],["12:16:4:1","12:16:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["12:16:1","12:16:2","12:16:3","12:16:4","12:16:5"]},"focus_surface_evidence":{"arabic_uthmani":"وَجَآءُوٓ أَبَاهُمْ عِشَآءًۭ يَبْكُونَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"12:16:1:1","qac_word_ref":"12:16:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"جَآءَ","morph_features":"STEM|POS:V|PERF|LEM:jaA^'a|ROOT:jyA|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"12:16:1:2","qac_word_ref":"12:16:1","root_ar":"ج ي ء","surface_ar":"جَآءُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"12:16:1:3","qac_word_ref":"12:16:1","root_ar":"","surface_ar":"وٓ"},{"lemma_ar":"أَبٌ","morph_features":"STEM|POS:N|LEM:>abN|ROOT:Abw|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"12:16:2:1","qac_word_ref":"12:16:2","root_ar":"ء ب و","surface_ar":"أَبَا"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"12:16:2:2","qac_word_ref":"12:16:2","root_ar":"","surface_ar":"هُمْ"},{"lemma_ar":"عِشَآء","morph_features":"STEM|POS:N|LEM:Ei$aA^'|ROOT:E$w|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"12:16:3:1","qac_word_ref":"12:16:3","root_ar":"ع ش و","surface_ar":"عِشَآءً"},{"lemma_ar":"بَكَتْ","morph_features":"STEM|POS:V|IMPF|LEM:bakato|ROOT:bky|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"12:16:4:1","qac_word_ref":"12:16:4","root_ar":"ب ك ي","surface_ar":"يَبْكُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"12:16:4:2","qac_word_ref":"12:16:4","root_ar":"","surface_ar":"ونَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["12:16:1:1"],["12:16:1:2","12:16:1:3"],["12:16:2:1","12:16:2:2"],["12:16:3:1"],["12:16:4:1","12:16:4:2"]],"word_analysis_refs":["12:16:1","12:16:2","12:16:3","12:16:4","12:16:5"],"word_rows":[{"analysis_record_ref":"12:16:1","analytic_gloss_range_en":"opening connector that can resume or coordinate the narrated return; it links without spelling out motive","analytic_root_gloss_range_en":null,"qac_refs":["12:16:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"12:16:2","analytic_gloss_range_en":"they came or arrived before their father, with the narrative pressure of presentation kept secondary","analytic_root_gloss_range_en":"coming, arrival, reaching presence, and event-emergence; local grammar selects completed plural arrival before a relational endpoint","qac_refs":["12:16:1:2","12:16:1:3"],"root":{"arabic":"ج ي أ","transliteration":"j-y-ʾ"},"surface":{"arabic":"جَاءُوا","transliteration":"jāʾū"}},{"analysis_record_ref":"12:16:3","analytic_gloss_range_en":"their father, the immediate relational recipient of the brothers' arrival","analytic_root_gloss_range_en":"father, paternal source, ancestor, or household origin; local suffix and singular form select the immediate father rather than an ancestral plural","qac_refs":["12:16:2:1","12:16:2:2"],"root":{"arabic":"أ ب و","transliteration":"ʾ-b-w"},"surface":{"arabic":"أَبَاهُمْ","transliteration":"abāhum"}},{"analysis_record_ref":"12:16:4","analytic_gloss_range_en":"at evening or nightfall, as an indefinite accusative time adverb","analytic_root_gloss_range_en":"evening, nightfall, dimness, weak sight, night-blindness, and related branches; local grammar selects the time branch while perception pressure remains relevant","qac_refs":["12:16:3:1"],"root":{"arabic":"ع ش و","transliteration":"ʿ-sh-w"},"surface":{"arabic":"عِشَاءًۭ","transliteration":"ʿishāʾan"}},{"analysis_record_ref":"12:16:5","analytic_gloss_range_en":"they were weeping, crying, or lamenting as an ongoing circumstantial state","analytic_root_gloss_range_en":"local verbal grief and weeping; wider root branches include pressing/crowding, subduing, and Bakkah as a place-name, but the proper-name branch is not active here","qac_refs":["12:16:4:1","12:16:4:2"],"root":{"arabic":"ب ك ك","transliteration":"b-k-k"},"surface":{"arabic":"يَبْكُونَ","transliteration":"yabkūna"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":2,"assigned_records":[{"anchor_refs":["12:16"],"branch_refs":["root_000007/B001","root_000147/B001","root_000281/B001","root_001017/B004"],"candidate_id":"cand_4cde9758ac8f9521d8ff","evidence_scope":"focus_ayah","hft_ref":"hft_3db8bcc0f1d6b1e17206","item_id":"baseline-paternal-grief-arrival","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-paternal-grief-arrival","support_id":"sup_4ab61dc1ae9bc0f6043a"},{"anchor_refs":["12:16"],"branch_refs":["root_000007/B001","root_000147/B004","root_001017/B001"],"candidate_id":"cand_aa705fb29494114631ca","evidence_scope":"focus_ayah","hft_ref":"hft_ebf305bafe75b2511784","item_id":"baseline-obscured-display","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-obscured-display","support_id":"sup_c3cc1c10df9ea680f992"}],"diagnostics":[],"lane_counts":{"global":7,"macro":9,"micro":2},"packet_summary":{"ayah_count":18,"focus_ref":"12:16","protocol":"focus-trace-pericope-lean-v1","split_root_mappings":[],"window":["12:1","12:2","12:3","12:4","12:5","12:6","12:7","12:8","12:9","12:10","12:11","12:12","12:13","12:14","12:15","12:16","12:17","12:18"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"valid_pericope_packet_unbound_response"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"12:16","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":7,"source_present":true,"structured_insight_count":11,"unstructured_record_count":0},"identity":{"ayah_ref":"12:16","lane":"micro","linguistic_source_ref":"12:16","surface_ref":"12:16","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"12:16","target_tokens":[["Akşamleyin",["12:16:1"]],["ağlayarak",["12:16:2"]],["babalarına",["12:16:3"]],["geldiler",["12:16:4"]]],"text":"Akşamleyin ağlayarak babalarına geldiler."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":2,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":18,"id":"s012-p01-001-018","label":"Joseph's dream and his brothers' plot","number":1,"refs":["12:1","12:2","12:3","12:4","12:5","12:6","12:7","12:8","12:9","12:10","12:11","12:12","12:13","12:14","12:15","12:16","12:17","12:18"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:2:unnamed-perfect-arrival","source_type":"word_analysis","support_id":"sup_0ec85b21cbee244f5198","text":"{\"blocking_evidence\":null,\"headline\":\"unnamed plural arrival as completed public action\",\"reader_payoff\":\"The reader notices that the brothers become a collective grammatical action rather than named individuals, and that their arrival is complete before the tears continue.\",\"reason\":\"The verb is perfect 3mp with pro-drop subject agreement, and the following imperfect circumstantial clause supports the completed-arrival versus ongoing-weeping contrast.\",\"representative_source_ids\":[\"QG-26222977\",\"QG-47cc4ea5\",\"QY-6b489839\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"12:16:3:1","source_type":"qac_morpheme","support_id":"sup_205900f6fca6fe450b27","text":"{\"lemma_ar\":\"عِشَآء\",\"morph_features\":\"STEM|POS:N|LEM:Ei$aA^'|ROOT:E$w|M|INDEF|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"12:16:3:1\",\"qac_word_ref\":\"12:16:3\",\"root_ar\":\"ع ش و\",\"surface_ar\":\"عِشَآءً\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:3:possessive-relational-definiteness","source_type":"word_analysis","support_id":"sup_23677b684cadf7f83b04","text":"{\"blocking_evidence\":null,\"headline\":\"their father is defined through the brothers\",\"reader_payoff\":\"The reader notices that the father enters the scene relationally, through the same unnamed plural group that has been carrying the action.\",\"reason\":\"The possessive suffix is syntactically forced and resolves to the brothers, so the relational definiteness and pronoun-chain payoff are locally secure.\",\"representative_source_ids\":[\"QG-09c590bc\",\"QG-42d3bc65\",\"QY-4cf31103\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:2","source_type":"word_analysis","support_id":"sup_295d2df4685866faae92","text":"{\"gloss_range\":\"they came or arrived before their father, with the narrative pressure of presentation kept secondary\",\"prose\":\"{{ar:جَاءُوا}} ({{tr:jāʾū}}) makes the brothers appear only as a plural verb ending: the group arrives, but no individual is named. Its perfect form completes the motion before the ongoing weeping of {{ar:يَبْكُونَ}} ({{tr:yabkūna}}), so the ayah moves from a bounded entrance to a prolonged display. The local sequence starts with arrival, then gives the father, then nightfall, then tears, setting up the spoken claim in the next ayah (12:17). The local syntax gives {{ar:أَبَاهُمْ}} ({{tr:abāhum}}) as the reached father, so any 'bringing' or 'presenting' sense must stay as narrative shadow: the fabricated account and shirt are not a separate local object in this word. The long ā and medial hamza make the sound catch before the plural ending, fitting arrival as motion that stops in presence. Within Surah 12, this first deceptive arrival before the father looks ahead to answering arrivals and restorations (12:93-96; 12:100).\",\"root_display\":\"{{ar:ج ي أ}} ({{tr:j-y-ʾ}})\",\"root_gloss_range\":\"coming, arrival, reaching presence, and event-emergence; local grammar selects completed plural arrival before a relational endpoint\",\"surface_display\":\"{{ar:جَاءُوا}} ({{tr:jāʾū}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:5:polarity-and-arrival-contrast","source_type":"word_analysis","support_id":"sup_2ac712073c71a200a61d","text":"{\"blocking_evidence\":null,\"headline\":\"weeping pole and arrival-manner contrast\",\"reader_payoff\":\"The reader notices that this arrival is framed by overt grief rather than restrained modesty, and that the weeping occupies one side of the Quranic laugh-weep polarity (28:25; 53:43).\",\"reason\":\"The comparisons are retained as contrastive echoes with concrete references, not as governors of the local grammar.\",\"representative_source_ids\":[\"QI-909bc202\",\"MI-75bf7270\",\"QE-e75f85be\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:4","source_type":"word_analysis","support_id":"sup_3ea47a6739f7dff4523e","text":"{\"gloss_range\":\"at evening or nightfall, as an indefinite accusative time adverb\",\"prose\":\"{{ar:عِشَاءًۭ}} ({{tr:ʿishāʾan}}) is not a decorative timestamp. As an indefinite accusative time adverb, it folds the evening hour directly into the arrival without a preposition and carries the ayah's only explicit timing, making this rare adverbial deployment structurally exposed. The selected sense is evening or nightfall, but the {{ar:ع ش و}} ({{tr:ʿ-sh-w}}) field also includes dimness and weak night-sight, so the father's reception is staged under constrained seeing. Its canonical extended form lets the evening word linger and then catch at the hamza before the ayah moves into weeping. The evening side also stands alone here, without the morning counterpart of morning-evening formulae (19:11; 19:62). That pressure is strengthened by the word's middle position between {{ar:أَبَاهُمْ}} ({{tr:abāhum}}) and {{ar:يَبْكُونَ}} ({{tr:yabkūna}}): the father is reached, the light drops, and the audible tears close the scene.\",\"root_display\":\"{{ar:ع ش و}} ({{tr:ʿ-sh-w}})\",\"root_gloss_range\":\"evening, nightfall, dimness, weak sight, night-blindness, and related branches; local grammar selects the time branch while perception pressure remains relevant\",\"surface_display\":\"{{ar:عِشَاءًۭ}} ({{tr:ʿishāʾan}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:2:hamza-arrival-sound","source_type":"word_analysis","support_id":"sup_40f1e1ffbb66e838ac1a","text":"{\"blocking_evidence\":null,\"headline\":\"glottal catch fits completed arrival\",\"reader_payoff\":\"The reader notices that the sound-shape of the arrival word catches before the plural ending, matching motion that comes to a stop in presence.\",\"reason\":\"The phonetic observation is local to the surface form and does not conflict with the grammar.\",\"representative_source_ids\":[\"QP-9e69fd3f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:5:undirected-display-and-sincerity","source_type":"word_analysis","support_id":"sup_416d82c36724b876c175","text":"{\"blocking_evidence\":null,\"headline\":\"observable crying without stated object\",\"reader_payoff\":\"The reader notices that the ayah shows tears as an emotional signal while withholding both their object and their sincerity.\",\"reason\":\"QAC and attachment evidence give no explicit object, and the rows' sincerity caution is not contradicted by the local form.\",\"representative_source_ids\":[\"QG-530cc731\",\"QS-9b4fad8a\",\"MS-e32adcb3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:5:form-i-causative-shadow","source_type":"word_analysis","support_id":"sup_4c9970988354e05cbe4e","text":"{\"blocking_evidence\":null,\"headline\":\"weepers, not grammatically causers\",\"reader_payoff\":\"The reader notices that the surface grammar lets the brothers wear the role of sufferers while the narrative keeps pressure on the grief they will cause.\",\"reason\":\"The causative idea is narrowed because the local surface is Form I imperfect; it survives only as contrast with an absent causative derivative and with later narrative effect.\",\"representative_source_ids\":[\"QF-8f8320bb\",\"MF-9796f999\",\"QY-92e44661\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:4:dim-perception-nightfall","source_type":"word_analysis","support_id":"sup_5630b14eb0a1b2761364","text":"{\"blocking_evidence\":null,\"headline\":\"nightfall becomes a perception condition\",\"reader_payoff\":\"The reader notices that evening is not merely when they arrive; it is the low-visibility condition in which the father receives the performance.\",\"reason\":\"The local sense remains temporal, but V4 accepts nightfall and weak-sight branches for the root, so the perception payoff survives as controlled coloring rather than a replacement sense.\",\"representative_source_ids\":[\"QS-44678466\",\"MS-9f81fd3a\",\"QY-80c369d8\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:1:boundary-connector","source_type":"word_analysis","support_id":"sup_62d650cea3fd5db3ab81","text":"{\"blocking_evidence\":null,\"headline\":\"connected scene launch without fixed motive\",\"reader_payoff\":\"The reader notices that the ayah begins by carrying the prior concealment into a new public return while leaving the exact discourse force and motive unstated.\",\"reason\":\"QAC allows either coordinating or resumptive force for the opening connector, so the exclusive labels must be narrowed to a connected boundary function rather than one fixed subtype.\",\"representative_source_ids\":[\"QG-3fdb611a\",\"QG-974666b0\",\"QS-292d93bc\",\"QT-e806fe5f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"12:16:4:1","source_type":"qac_morpheme","support_id":"sup_63e45fa309bed3907df8","text":"{\"lemma_ar\":\"بَكَتْ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:bakato|ROOT:bky|3MP\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"12:16:4:1\",\"qac_word_ref\":\"12:16:4\",\"root_ar\":\"ب ك ي\",\"surface_ar\":\"يَبْكُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:4:isolated-evening-formula","source_type":"word_analysis","support_id":"sup_6a8fabddf945002d4e68","text":"{\"blocking_evidence\":null,\"headline\":\"evening side appears without morning balance\",\"reader_payoff\":\"The reader notices that the evening term stands alone rather than as part of a morning-evening formula, so the scene isolates the dark side of the time field (19:11; 19:62).\",\"reason\":\"The morning-evening and worship-time references survive as contrastive apparatus; any non-canonical variant is not allowed to govern the local parse.\",\"representative_source_ids\":[\"QI-abfc3af3\",\"MI-58ebef32\",\"QE-13ea321d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:1","source_type":"word_analysis","support_id":"sup_864185bdecab595ff165","text":"{\"gloss_range\":\"opening connector that can resume or coordinate the narrated return; it links without spelling out motive\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) opens the ayah as a connected return, not as an isolated scene. The connector can be heard as resumption or coordination, so the prose should keep the boundary alive: the concealed well-scene has moved into public arrival, but the particle itself does not explain the brothers' motive. Because it is fused to {{ar:جَاءُوا}} ({{tr:jāʾū}}), the transition is visually and audibly carried straight into the arrival verb.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:3:father-network-and-restoration","source_type":"word_analysis","support_id":"sup_8d0aa5e73c6ec89196a2","text":"{\"blocking_evidence\":null,\"headline\":\"deceived father-position answered later\",\"reader_payoff\":\"The reader notices that this father-directed deception belongs to a larger Surah 12 father-relation network that later turns toward honor and restoration (12:100).\",\"reason\":\"The rows supply concrete same-surah father references, so the echo survives as a relational arc rather than as a new local lexical sense.\",\"representative_source_ids\":[\"QI-cf963339\",\"QE-72f7e65a\",\"ME-564832c5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"12:16:1:2","source_type":"qac_morpheme","support_id":"sup_8ef0cd94fc09d3e34004","text":"{\"lemma_ar\":\"جَآءَ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:jaA^'a|ROOT:jyA|3MP\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"12:16:1:2\",\"qac_word_ref\":\"12:16:1\",\"root_ar\":\"ج ي ء\",\"surface_ar\":\"جَآءُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:5:final-position-display","source_type":"word_analysis","support_id":"sup_9040a36ced463fc20b48","text":"{\"blocking_evidence\":null,\"headline\":\"final word makes tears the landing\",\"reader_payoff\":\"The reader notices that the ayah closes on the audible emotional display, setting up the brothers' spoken claim in the next ayah (12:17).\",\"reason\":\"The final circumstantial verb is the last word of the ayah and directly precedes the next ayah's speech opening.\",\"representative_source_ids\":[\"QT-1e92b4d4\",\"MT-9977fc6b\",\"QB-be48b2e5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:5:plural-subject-continuity","source_type":"word_analysis","support_id":"sup_9af37af2cda2f61bd368","text":"{\"blocking_evidence\":null,\"headline\":\"same unnamed group keeps performing\",\"reader_payoff\":\"The reader notices that the same plural group carried by the arrival verb reappears in the weeping ending without being renamed.\",\"reason\":\"The verb's 3mp agreement and attachment evidence link its implicit subject to the brothers already carried by the arrival clause.\",\"representative_source_ids\":[\"QG-2203801e\",\"QF-fc8cb391\",\"QB-16b80215\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:3:father-sense-narrowed","source_type":"word_analysis","support_id":"sup_a129be2284cc34cbfb1a","text":"{\"blocking_evidence\":null,\"headline\":\"immediate father, not ancestral abstraction\",\"reader_payoff\":\"The reader notices that a broad fatherhood and origin field is compressed into one household encounter with a specific deceived father.\",\"reason\":\"The broad father, ancestor, and source claims are narrowed because the local singular possessive form selects the immediate father; V4 has no root entry here to license additional branch expansion.\",\"representative_source_ids\":[\"QS-3805e35b\",\"QF-9289ee53\",\"QI-34384866\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:5:surah-grief-echo","source_type":"word_analysis","support_id":"sup_ab467de15061d0e4b8c6","text":"{\"blocking_evidence\":null,\"headline\":\"performed tears turn toward the father\",\"reader_payoff\":\"The reader notices that the brothers' performed tears become the seed of the father's later destructive grief in the same surah (12:84; 12:86).\",\"reason\":\"The source rows give concrete same-surah references, so the echo is preserved as directional narrative pressure.\",\"representative_source_ids\":[\"QI-325030aa\",\"MI-b8b085d7\",\"QE-88dc14d9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:3","source_type":"word_analysis","support_id":"sup_b1469341c8db245e4b7f","text":"{\"gloss_range\":\"their father, the immediate relational recipient of the brothers' arrival\",\"prose\":\"{{ar:أَبَاهُمْ}} ({{tr:abāhum}}) makes the father definite through the brothers' own suffix: he is not introduced by name, but as their father. The noun-five accusative shape, with its long ā case-marking, makes him the reached endpoint of {{ar:جَاءُوا}} ({{tr:jāʾū}}), and the suffix binds the unnamed plural subject to the person they are about to deceive. The broader father/ancestor range is narrowed here to the immediate household relation, while still letting the father stand as the vulnerable origin-point to which the sons return. Later Surah 12 scenes answer this deceived father-position with restored parental honor (12:100).\",\"root_display\":\"{{ar:أ ب و}} ({{tr:ʾ-b-w}})\",\"root_gloss_range\":\"father, paternal source, ancestor, or household origin; local suffix and singular form select the immediate father rather than an ancestral plural\",\"surface_display\":\"{{ar:أَبَاهُمْ}} ({{tr:abāhum}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:5:bakkah-import-rejected","source_type":"word_analysis","support_id":"sup_b95359d4934443aec61b","text":"{\"blocking_evidence\":\"V4 separates Bakkah as an accepted proper-name branch, while the local word is an IV imperfect grief verb; no same-form evidence licenses sacred-place meaning here.\",\"headline\":\"proper-name adjacency cannot govern the verb\",\"reader_payoff\":null,\"reason\":\"The row's structural coincidence overreads the root inventory. The proper-name branch may be noted as separated, but it should not shape the local prose for {{ar:يَبْكُونَ}} ({{tr:yabkūna}}).\",\"representative_source_ids\":[\"MS-cc223123\"],\"status\":\"rejected\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:2:arrival-presentation-narrowed","source_type":"word_analysis","support_id":"sup_c3e015c1323063854a2a","text":"{\"blocking_evidence\":null,\"headline\":\"arrival selected while presentation remains a narrative shadow\",\"reader_payoff\":\"The reader notices that the motion toward the father doubles as the delivery of a staged account, while the local parse still treats the father as the explicit reached endpoint.\",\"reason\":\"Rows that speak of a suppressed brought-object are narrowed because attachment evidence marks {{ar:أَبَاهُمْ}} ({{tr:abāhum}}) as the explicit object reached by the verb; the presentation payoff survives only as narrative pressure.\",\"representative_source_ids\":[\"QG-402d0fc1\",\"MG-30435d18\",\"QS-27f2cdfa\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:4:middle-beat-between-father-and-tears","source_type":"word_analysis","support_id":"sup_c5d1e56cf875981bc33c","text":"{\"blocking_evidence\":null,\"headline\":\"time mediates father and tears\",\"reader_payoff\":\"The reader notices the sequence as staged perception: father first, dim time next, audible crying last.\",\"reason\":\"The local order places the time marker between the father and the final circumstantial weeping clause, so the structural payoff is directly anchored.\",\"representative_source_ids\":[\"QT-011c1ab2\",\"QY-4987d770\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:1:fused-liaison","source_type":"word_analysis","support_id":"sup_d0f08222c2cf2629be86","text":"{\"blocking_evidence\":null,\"headline\":\"fused connector carries arrival forward\",\"reader_payoff\":\"The reader notices that the one-letter connector is not detached from the action; it is graphically and recitationally joined to the arrival.\",\"reason\":\"The particle is a proclitic attached to the following verb, preserving the source row's visual and audible continuity payoff.\",\"representative_source_ids\":[\"QF-588ce7f7\",\"QP-4397e162\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:2:scene-order-and-speech-pressure","source_type":"word_analysis","support_id":"sup_dec096ef957ad80ce121","text":"{\"blocking_evidence\":null,\"headline\":\"arrival sets recipient, time, manner, then speech\",\"reader_payoff\":\"The reader notices that the verb starts a staged sequence: arrival first, father next, nightfall and tears after, and only then the spoken claim in the following ayah (12:17).\",\"reason\":\"The local word order and the next-ayah reference support the staged movement without adding a new lexical sense.\",\"representative_source_ids\":[\"QT-258ae5b6\",\"QB-a2429be1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:5:rare-verbal-root-and-proper-name-limit","source_type":"word_analysis","support_id":"sup_e38ec02b680219e3de0b","text":"{\"blocking_evidence\":null,\"headline\":\"sparse grief verb, not sacred-place import\",\"reader_payoff\":\"The reader notices that the local grief verb is distributionally exposed within a small root field, while the proper-name branch is kept outside the local sense.\",\"reason\":\"The root's proper-name branch is accepted in V4 but is not the local IV verbal use; the distributional rarity survives without importing sacred-place meaning.\",\"representative_source_ids\":[\"QI-15936094\",\"QI-c45eba07\",\"QH-d8ea7444\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"12:16:2:1","source_type":"qac_morpheme","support_id":"sup_e4868c657608c7e07299","text":"{\"lemma_ar\":\"أَبٌ\",\"morph_features\":\"STEM|POS:N|LEM:>abN|ROOT:Abw|MS|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"12:16:2:1\",\"qac_word_ref\":\"12:16:2\",\"root_ar\":\"ء ب و\",\"surface_ar\":\"أَبَا\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:2:relational-and-surah-echoes","source_type":"word_analysis","support_id":"sup_e608ab6c9d3971a7086d","text":"{\"blocking_evidence\":null,\"headline\":\"deceptive coming answered by later arrivals\",\"reader_payoff\":\"The reader notices that this arrival is the negative pole of later Surah 12 arrival scenes where the family route and shirt motif are morally reversed (12:93-96; 12:100).\",\"reason\":\"The source rows give concrete same-surah and cross-surah references; they are preserved as echo and contrast, not as controls on the local parse.\",\"representative_source_ids\":[\"QI-0fbeb8c8\",\"MI-3d503381\",\"QE-ba838f59\",\"ME-ac914486\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:4:form-variant-and-sound","source_type":"word_analysis","support_id":"sup_e87ac41d9b8d4e0f1496","text":"{\"blocking_evidence\":null,\"headline\":\"extended evening form lingers audibly\",\"reader_payoff\":\"The reader notices that the canonical extended form makes the time-word linger and catch at the ending before the ayah moves into weeping.\",\"reason\":\"Variant and sound rows are kept as form pressure only; they do not relocate the event or override the canonical local surface.\",\"representative_source_ids\":[\"QF-09346ca7\",\"QF-aa80dd89\",\"QP-2ddd5a63\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:3:accusative-arrival-target","source_type":"word_analysis","support_id":"sup_eb75e891ccba2e2696c9","text":"{\"blocking_evidence\":null,\"headline\":\"case marks the father as reached recipient\",\"reader_payoff\":\"The reader notices that the father is placed immediately after the arrival verb as the person reached before the time and weeping details are added.\",\"reason\":\"QAC identifies the noun-five accusative form and attachment evidence marks the father as the explicit object or endpoint of the arrival.\",\"representative_source_ids\":[\"QG-9835f19b\",\"MG-76e32f82\",\"QT-7e853ec9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:4:accusative-time-adverb","source_type":"word_analysis","support_id":"sup_f39f4d3332c94a1194f3","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite accusative evening frames the event\",\"reader_payoff\":\"The reader notices that the word itself carries the whole temporal frame as a bare accusative, not as an external prepositional time note.\",\"reason\":\"QAC and attachment evidence confirm an accusative temporal adverb, and the contextual profile marks the adverbial deployment as locally salient.\",\"representative_source_ids\":[\"QG-1bfaba44\",\"QG-a1a9fcb0\",\"MH-da69aa60\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:5","source_type":"word_analysis","support_id":"sup_f3e1c21652116de64a51","text":"{\"gloss_range\":\"they were weeping, crying, or lamenting as an ongoing circumstantial state\",\"prose\":\"{{ar:يَبْكُونَ}} ({{tr:yabkūna}}) is the ayah's landing. As an imperfect circumstantial verb, it means the brothers came while weeping: the tears are simultaneous with the arrival and still unfolding after the perfect {{ar:جَاءُوا}} ({{tr:jāʾū}}). The plural ending keeps the same unnamed group onstage, now as emotional signalers before their father. Because the verb has no explicit object, the grief is displayed without saying whether it is over Yusuf, the story, or the performance itself, and the wording reports observable crying without proving sincerity. The Form I surface casts them as weepers rather than as makers of someone else weep, even though the same surah later turns the grief onto the father (12:84; 12:86). The arrival is framed by overt grief rather than restrained modesty (28:25), and the word occupies the weeping side of the laugh-weep polarity (53:43). Within the sparse local grief-root field, the proper-name branch remains outside the sense, so the rarity sharpens the verbal display without importing sacred-place meaning.\",\"root_display\":\"{{ar:ب ك ك}} ({{tr:b-k-k}})\",\"root_gloss_range\":\"local verbal grief and weeping; wider root branches include pressing/crowding, subduing, and Bakkah as a place-name, but the proper-name branch is not active here\",\"surface_display\":\"{{ar:يَبْكُونَ}} ({{tr:yabkūna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:16:5:imperfect-hal-process","source_type":"word_analysis","support_id":"sup_fd60d277e351b5a15466","text":"{\"blocking_evidence\":null,\"headline\":\"ongoing circumstantial weeping\",\"reader_payoff\":\"The reader notices that weeping is not a later event but the manner in which the brothers are arriving, still in process at the ayah's close.\",\"reason\":\"Attachment evidence explicitly marks the final verb as a circumstantial clause describing the arrival subject, and QAC supplies imperfect 3mp form.\",\"representative_source_ids\":[\"QG-19db32f9\",\"MG-f1ba456a\",\"QT-abf22f58\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَجَآءُوٓ أَبَاهُمْ عِشَآءًۭ يَبْكُونَ","ayah_ref":"12:16"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000007/B001","root_000147/B001","root_000281/B001","root_001017/B004"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000281","role":"Ordinary coming supplies the movement that culminates before the father.","root":"ج ي ء","source_ref":"12:16","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000007","role":"Fatherhood and nurture make the addressee the scene's receiving and protective authority.","root":"ء ب و","source_ref":"12:16","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_001017","role":"The evening-time image fixes the arrival at the late-day and night threshold.","root":"ع ش و","source_ref":"12:16","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000147","role":"Sorrow, tears, and voice supply the manifest affect carried into the encounter.","root":"ب ك ي","source_ref":"12:16","source_word_indices":["4"]}],"changed_reading":{"after":"Their return is an affective appeal delivered to the household's paternal protector at a vulnerable night threshold.","before":"They came home at night while crying."},"confidence":"strong","focus_anchor":"The construction joins جاءوا, أباهم, عشاء, and يبكون as movement, recipient, time, and manifest affect.","mechanism":"A collective movement terminates at the father-as-caregiver after nightfall, with crying supplying sorrow, tears, or voice; the event is an appeal for paternal reception rather than bare locomotion.","model_id":"baseline-paternal-grief-arrival"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-paternal-grief-arrival","source_type":"hft","support_id":"sup_4ab61dc1ae9bc0f6043a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَجَآءُوٓ أَبَاهُمْ عِشَآءًۭ يَبْكُونَ","ayah_ref":"12:16"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000007/B001","root_000147/B004","root_001017/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001017","role":"Night darkness and low clarity supply reduced inspectability as the display's condition.","root":"ع ش و","source_ref":"12:16","source_word_indices":["3"]},{"branch_id":"B004","mapped_root_id":"root_000147","role":"Affected weeping supplies the exploratory possibility of performed rather than spontaneous grief.","root":"ب ك ي","source_ref":"12:16","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000007","role":"The nurturing father is the intended evaluator and emotional audience of the surface.","root":"ء ب و","source_ref":"12:16","source_word_indices":["2"]}],"changed_reading":{"after":"Evening can function as reduced inspectability while possibly affected crying becomes an emotionally legible surface offered to the father; this remains a possibility, not an assertion.","before":"Evening is an incidental timestamp and the crying transparently reports grief."},"confidence":"exploratory","focus_anchor":"عشاء stands beside يبكون, and the display is directed to أباهم.","mechanism":"Reduced nocturnal visibility lets audible or visible grief dominate what the father can assess. The form-distant affected-weeping branch keeps open, without asserting, the possibility that the group presents a managed emotional surface.","model_id":"baseline-obscured-display"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-obscured-display","source_type":"hft","support_id":"sup_c3cc1c10df9ea680f992","trust":"legacy_unbound"}]}
</lane_packet_json>
