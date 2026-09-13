# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **18:85**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s018-regular-20260912/s018/18_85/micro.discovery.json` and modify nothing
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
  "ayah_ref": "18:85",
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
{"analysis_context":{"analysis_id":"s018-regular-20260912","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"18:85","host_surah":18,"lane_context_refs":[],"ordered_context_refs":["18:83","18:84","18:86","18:87","18:88","18:89","18:90","18:91","18:92","18:93","18:94","18:95","18:96","18:97","18:98","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Bu dal, geride kalmış birine yetişmeyi, adım adım araştırmayı ve bir hakkı istemeyi içermez.","branch_kind":"bare","branch_ref":"root_000175/B001","candidate_links":[{"candidate_id":"cand_6b15bf64ee4f971204a8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَتْبَعَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>atobaEa|ROOT:tbE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"18:85:1:2","qac_word_ref":"18:85:1","surface_ar":"أَتْبَعَ"}],"gloss":"ardından gitmek ve yolunu benimsemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiyle birlikte ya da onun arkasında ilerleyerek ardından gitmek."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir iz, örnek, buyruk veya öğreti doğrultusunda davranmak ve ona uymak."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ardından giden kişiyi ya da kişileri tekil veya toplu olarak adlandırmak."}}],"root_ar":"ت ب ع","root_id":"root_000175","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem birinin fiziksel olarak ardından ilerlemesini hem de onun buyruğunu, örneğini veya yolunu benimsemeyi kapsayan genel karşılıktır.","boundary_detail":"Bu dal, geride kalmış birine yetişmeyi, adım adım araştırmayı ve bir hakkı istemeyi içermez.","branch_image_ar":"التلو والقفو","concept_gloss":"ardından gitmek ve yolunu benimsemek","contextual_glosses":[{"applicability":"Bir kişi veya topluluğun yanında ya da arkasında fiziksel olarak ilerleme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Buyruğa, örneğe veya öğretiye uyma yönünü dışarıda bırakır.","preserves":"Fiziksel ardından gitme yönünü doğal biçimde korur."},"facet_ids":["F001"],"text":"arkasından gitmek","usage_role":"contextual"},{"applicability":"Bir kişinin örneğini, bir buyruğu veya bir öğretiyi davranışta benimseme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Somut olarak birinin arkasında yürüme ve izleyen kişi adı yönlerini dışarıda bırakır.","preserves":"Örnek ve yönlendirme doğrultusunda davranma yönünü korur."},"facet_ids":["F002"],"text":"yolunu izlemek","usage_role":"contextual"}],"definition":"Bir kişi, topluluk, iz, buyruk veya örneğin ardından gitmek; bunu bedensel olarak arkasından ilerleyerek ya da davranışını ve yönlendirmesini benimseyerek yapmak.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiyle birlikte ya da onun arkasında ilerleyerek ardından gitmek."},{"facet_id":"F002","role":"extension","statement":"Bir iz, örnek, buyruk veya öğreti doğrultusunda davranmak ve ona uymak."},{"facet_id":"F003","role":"extension","statement":"Ardından giden kişiyi ya da kişileri tekil veya toplu olarak adlandırmak."}],"identity_rationale":"Kaynak ifadesi, bir kimsenin yanında ya da arkasında gitmeyi, onun izini sürmeyi ve ayrıca bir buyruğa, örneğe veya öğretiye uymayı aynı temel izleme ilişkisi altında toplar. Verilen dal çerçevesi bu bedensel ve davranışsal yönleri doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"birlikte ya da arkasından yürümek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"izinden gitmek, örneğini veya buyruğunu benimsemek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"ardından giden kimse"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ardından giden kimse veya topluluk"}],"lexicalization_note":"Dal yalın kullanımı kapsar; tanım, özel bir söz öbeğine bağlı olmayan fiziksel izleme ve örnek ya da buyruğa uyma anlamlarıyla sınırlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan üç karşılaştırma uyma, dirençten sonra boyun eğme ve aşamalı iz araştırmasıyla en güçlü karışma noktalarını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, somut ardından gitmeden davranışsal benimsemeye uzanan daha geniş bir izleme ilişkisi kurar; komşu dal ise buyruğa uyma ve örneği uygulama yönünü çekirdeğe alır.","focus_only":"Bir kişinin veya izin fiziksel olarak ardından gitmeyi de kapsar.","gloss":"buyruğa ve örneğe uyma","neighbor_only":"Özellikle bir buyruğu yerine getirme ve bir örneğe göre davranma üzerinde yoğunlaşır.","neighbor_ref":"root_001397/B010","relation_type":"near_synonym","shared_zone":"Her ikisi de bir öncüyü, yönlendirmeyi veya örneği davranışta esas alma alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal nötr bir ardından gitme ve benimseme ilişkisidir; komşu dalda ise önceki güçlüğün ardından söz dinler duruma gelme belirgindir.","focus_only":"İzlenen kişiye karşı önceki bir direnç bulunmasını gerektirmez.","gloss":"uyup peşinden gelmek","neighbor_only":"Güçlük veya dirençten sonra yumuşayıp boyun eğme çağrışımı taşır.","neighbor_ref":"root_000844/B003","relation_type":"near_synonym","shared_zone":"İki dalda da bir kişi veya yönlendirme karşısında ardından gelme ve uyma ilişkisi vardır."},{"boundary_match":"partial","distinction":"Odak dalda genel ardından gitme yeterlidir; komşu dalda arama, zaman aralığı ve birbirini izleyen belirtileri tek tek inceleme kurucu niteliktedir.","focus_only":"Tek bir kişi, buyruk veya örneğin ardından doğrudan gitmeyi kapsar.","gloss":"adım adım iz araştırmak","neighbor_only":"Bir şeyi zaman içinde parça parça arayıp her izini incelemeyi gerektirir.","neighbor_ref":"root_000175/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da önde bulunanın bıraktığı yön veya iz üzerinden ilerlemeyi içerir."}],"source_phrase_ar":"التابع التالي؛ يتبعه يتلوه؛ تبعه يتبعه تبعا؛ هؤلاء تبع وأتباع (ayn)؛ تبعت الرجل إذا مشيت معه (jamhara)؛ تبعت القوم تبعا وتباعة إذا مشيت خلفهم؛ التبع يكون واحدا وجماعة (sihah)؛ التابع التالي؛ اتباع بالمعروف؛ اتبعوا القرآن (tahdhib)؛ تبعه واتبعه قفا أثره تارة بالجسم وتارة بالارتسام والائتمار (mufradat)","source_summary":"Ortak anlatım, önde bulunanın ardından gitme ilişkisini hem bedensel hareket hem de davranış, buyruk veya örneğe uyma düzleminde kurar; ardından giden kişi ve topluluk adları da bu çekirdeğe dayanır.","sources":["AY","JA","SI","TA","MU"],"what_is_ar":"اتباع الشخص أو الأمر أو الأثر؛ الائتمار والاقتداء؛ التابع والتبع والأتباع لمن يتبع غيره","what_is_not_ar":"ليس اللحوق بعد سبق ولا التتبع المتدرج ولا المطالبة بالحق"},"support_links":["sup_c1184877ef47aceeaea3"]},{"boundary":"Yetişme çekirdeği, başkasını peşinden sürükleme uzantısından ve gözle izleme söz öbeğinden açıkça ayrılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000175/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَتْبَعَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>atobaEa|ROOT:tbE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"18:85:1:2","qac_word_ref":"18:85:1","surface_ar":"أَتْبَعَ"}],"gloss":"geriden yetişmek veya peşine takmak","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Daha önce yola çıkmış kişiye ya da topluluğa geriden yetişip onu yakalamak."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kimseyi veya şeyi kendi ardından gelir duruma getirmek."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli söz öbeğinde, uzaklaşan topluluğu bıraktığı izlerden gözle izlemeyi sürdürmek."}}],"root_ar":"ت ب ع","root_id":"root_000175","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Önceden uzaklaşmış olana ulaşılan ya da bir başkasının ardından gelmesinin sağlandığı çekirdek kullanımları birlikte temsil eder.","boundary_detail":"Yetişme çekirdeği, başkasını peşinden sürükleme uzantısından ve gözle izleme söz öbeğinden açıkça ayrılmalıdır.","branch_image_ar":"اللَّحاق والإدراك","concept_gloss":"geriden yetişmek veya peşine takmak","contextual_glosses":[{"applicability":"Önden gitmiş kişi veya topluluğa sonradan ulaşıldığı hareket bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkasını peşine takma ve izleri gözle sürdürme kullanımlarını dışarıda bırakır.","preserves":"Gerideki kişinin öndekine ulaşıp onu yakalaması sonucunu korur."},"facet_ids":["F001"],"text":"yetişip yakalamak","usage_role":"contextual"},{"applicability":"Uzaklaşan bir topluluğa bakışın, onun bıraktığı belirtiler boyunca yöneltildiği söz öbeğine özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bedensel olarak yetişme ve bir başkasını peşine takma yönlerini dışarıda bırakır.","preserves":"Bakışla ve izler üzerinden sürdürülen izleme eylemini korur."},"facet_ids":["F003"],"text":"izlerini gözle sürdürmek","usage_role":"contextual"}],"definition":"Önden gitmiş birine geriden yetişip onu yakalamak veya bir başkasını kendi ardından gelir duruma getirmek. Belirli söz öbeğinde, uzaklaşan bir topluluğu bıraktığı izler üzerinden gözle sürdürmek de anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Daha önce yola çıkmış kişiye ya da topluluğa geriden yetişip onu yakalamak."},{"facet_id":"F002","role":"extension","statement":"Bir kimseyi veya şeyi kendi ardından gelir duruma getirmek."},{"facet_id":"F003","role":"associated_use","statement":"Belirli söz öbeğinde, uzaklaşan topluluğu bıraktığı izlerden gözle izlemeyi sürdürmek."}],"identity_rationale":"Kaynak ifadesinin ana ekseni önden gitmiş olana yetişip onu yakalamaktır; ancak bir başkasını peşine takma ve topluluğu bıraktığı izlerden gözle izleme kullanımları da açıkça yer alır. Bu yüzden dal korunabilir, fakat yalnızca yetişme olarak tanımlanamaz.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"önden gidene yetişmek veya başkasını peşine takmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"uzaklaşan topluluğun izlerini gözle sürdürmek"}],"lexicalization_note":"Dal hem çekimli bir biçimin yetişme ve peşine takma anlamını hem de yalnızca belirtilen gözle izleme söz öbeğinde görülen kullanımı ayrı tutar.","neighbor_coverage_note":"Tüm adaylar gözden geçirildi; seçilen ilişkiler genel ulaşma, hedefe varma ve yalnızca ardından gitme anlamlarından ayrımı en açık biçimde kurar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda önceden yola çıkmış olanı ardından giderek yakalama ilişkisi belirgindir; komşu dal ise ulaşma ve eklenmeyi daha genel biçimde kapsar.","focus_only":"Bir başkasını peşine takma ve özel olarak bakışla iz sürme kullanımlarını da içerir.","gloss":"öndekine ulaşıp yakalamak","neighbor_only":"Genel olarak bir şeyin başka bir şeye ulaşmasını ve ona eklenmesini daha geniş kapsamda anlatır.","neighbor_ref":"root_001347/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın merkezinde geridekinin önde bulunan kişiye veya şeye ulaşması vardır."},{"boundary_match":"partial","distinction":"Odak dal ilişkisel bir kovalamaca ve yetişme düzeni kurar; komşu dalda önden giden bir katılımcı bulunması gerekmez.","focus_only":"Önden giden bir katılımcının ardından hareket edip ona yetişmeyi gerektirir.","gloss":"bir sona ulaşmak","neighbor_only":"Bir yer, süre, gelişim aşaması veya herhangi bir belirlenmiş sona ulaşmayı kapsar.","neighbor_ref":"root_000151/B001","relation_type":"near_neighbor","shared_zone":"İki dal da hareketin veya ilerlemenin bir ulaşma sonucuyla tamamlanmasını içerir."},{"boundary_match":"partial","distinction":"Genel ardından gitme dalında mesafenin kapanması gerekmez; burada ise önceki ayrılık ve sonradan ulaşıp yakalama anlamın merkezindedir.","focus_only":"Öndekiyle aradaki uzaklığın kapanıp ona yetişilmesini kurucu sonuç sayar.","gloss":"ardından gitmek","neighbor_only":"Yetişme gerçekleşmeden yalnızca ardından gitmeyi veya yolunu benimsemeyi de kapsar.","neighbor_ref":"root_000175/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir katılımcı önde, diğeri onun ardından hareket eder."}],"source_phrase_ar":"وأتبعت القوم بصري إذا أتبعت النظر في آثارهم (jamhara)؛ أتبعت القوم إذا كانوا قد سبقوك فلحقتهم؛ أتبعت غيري؛ أتبعه الشيء فتبعه (sihah)؛ أتبعت القوم إذا كانوا قد سبقوك فلحقتهم؛ أتبعه يريد به شرا؛ ما زلت أتبعهم حتى أتبعتهم أي حتى أدركتهم (tahdhib)؛ أتبعه إذا لحقه (mufradat)","source_summary":"Toplu kanıt, önden gidenlere sonradan yetişme ve yakalama anlamını merkezde verir; bunun yanında bir başkasını peşine takma ve izleri gözle sürdürme kullanımlarını da kaydeder.","sources":["AY","JA","SI","TA","MU"],"what_is_ar":"اللَّحاق بمن سبق؛ الإتباع الذي يصير معه السابق مدركا أو يلحق به شيء يتبعه","what_is_not_ar":"ليس مطلق الاتباع والاقتداء ولا التتبع في مهلة"},"support_links":[]},{"boundary":"Sırf birinin arkasından yürümek ya da hızlıca yetişmek yeterli değildir; arama ve adım adım sürdürme gerekir.","branch_kind":"mixed_non_bare","branch_ref":"root_000175/B003","candidate_links":[{"candidate_id":"cand_ae5760fdf2c2a2b0b410","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَتْبَعَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>atobaEa|ROOT:tbE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"18:85:1:2","qac_word_ref":"18:85:1","surface_ar":"أَتْبَعَ"}],"gloss":"adım adım iz sürüp araştırmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Aranan şeyi zaman aralıkları içinde parça parça ve birbirini izleyen adımlarla araştırmak."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi, olay veya bilginin bıraktığı iz ve belirtileri tek tek inceleyerek ilerlemek."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kimsenin kusurlarını veya geride bıraktığı kayıt ve nesneleri ayrıntılı biçimde araştırmak."}}],"root_ar":"ت ب ع","root_id":"root_000175","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin kendisini veya bıraktığı belirtileri zaman içinde tek tek arayıp inceleme sürecinin genel karşılığıdır.","boundary_detail":"Sırf birinin arkasından yürümek ya da hızlıca yetişmek yeterli değildir; arama ve adım adım sürdürme gerekir.","branch_image_ar":"التقصي أثرا بعد أثر","concept_gloss":"adım adım iz sürüp araştırmak","contextual_glosses":[{"applicability":"Somut belirtiler, kayıtlar veya bir kişinin geride bıraktığı işaretler üzerinden ilerlenen araştırmalarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İz dışındaki bir nesneyi genel olarak parça parça arama kapsamını daraltır.","preserves":"Bir bulgudan ötekine geçerek ayrıntılı inceleme yönünü korur."},"facet_ids":["F002","F003"],"text":"izleri tek tek incelemek","usage_role":"contextual"}],"definition":"Bir şeyi, bilgiyi ya da bırakılmış izleri arayarak zaman içinde parça parça ilerlemek; her yeni belirtiyi öncekinin ardından inceleyip araştırmayı sürdürmek.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Aranan şeyi zaman aralıkları içinde parça parça ve birbirini izleyen adımlarla araştırmak."},{"facet_id":"F002","role":"specialization","statement":"Bir kişi, olay veya bilginin bıraktığı iz ve belirtileri tek tek inceleyerek ilerlemek."},{"facet_id":"F003","role":"example","statement":"Bir kimsenin kusurlarını veya geride bıraktığı kayıt ve nesneleri ayrıntılı biçimde araştırmak."}],"identity_rationale":"Kaynak ifadesi, bir şeyi veya onun bıraktığı belirtileri zaman içinde birbiri ardınca aramayı ve incelemeyi açıkça anlatır. Dalın aşamalı, araştırıcı ve iz odaklı çerçevesi bu kurucu özellikleri doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir şeyi zaman içinde parça parça aramak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"izleri adım adım araştırmak"}],"lexicalization_note":"Genel aşamalı arama biçimi ile özellikle iz ve belirtilerin tek tek incelendiği söz öbeği birbirine karıştırılmadan tanımlanır.","neighbor_coverage_note":"Bütün komşular değerlendirildi; dört seçim somut iz okuma, haber araştırma ve genel ardından gitmeyle olan sınırları gereksiz tekrar olmadan gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kapsamı aşamalı araştırmanın kendisidir ve nesnesi değişebilir; komşu dal somut yol ya da kişi izini izlemeye daha sıkı bağlıdır.","focus_only":"İz dışındaki bir şeyi de zaman içinde parça parça aramayı kapsar.","gloss":"izin ardından ilerlemek","neighbor_only":"Özellikle bir yolun veya kişinin somut izini okuyarak ilerlemeyi öne çıkarır.","neighbor_ref":"root_001232/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da önceki işaretten sonraki işarete geçerek iz üzerinden ilerleme vardır."},{"boundary_match":"partial","distinction":"Odak dalda parça parça araştırma yöntemi kurucudur; komşu dalda somut izin okunması ve bunu yapan uzman kişi daha belirgindir.","focus_only":"Zamana yayılmış arama sürecini ve farklı türde bulguların tek tek araştırılmasını kapsar.","gloss":"iz okuyarak peşinden gitmek","neighbor_only":"İzleri tanıma becerisine sahip iz okuyucusu rolünü de içerir.","neighbor_ref":"root_001271/B001","relation_type":"near_synonym","shared_zone":"İki dal da geride bırakılmış işaretleri okuyup bunların gösterdiği yönde ilerlemeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal yöntem olarak aşamalı iz sürmeye dayanır; komşu dalın nesnesi haberdir ve bilgi toplama yolları soru sorma ile duyup görmeyi içerir.","focus_only":"Somut izleri, kusurları veya kayıt parçalarını doğrudan inceleyebilir.","gloss":"haber araştırmak","neighbor_only":"Özellikle haber edinmek için soru sorma, dinleme veya gözetleme yollarını kullanır.","neighbor_ref":"root_000321/B004","relation_type":"near_neighbor","shared_zone":"Her ikisi de eksik bilgiyi birbirini izleyen bulgularla tamamlamaya yönelik araştırmadır."},{"boundary_match":"partial","distinction":"Genel ardından gitme tek ve kesintisiz bir hareket olabilir; odak dalda ise süre, arama ve bulguların birer birer izlenmesi zorunludur.","focus_only":"Arama amacıyla zaman içinde birbirini izleyen her bulguyu incelemeyi gerektirir.","gloss":"ardından gitmek","neighbor_only":"Araştırma yapmadan bir kişi, buyruk veya örneğin ardından gitmeyi de kapsar.","neighbor_ref":"root_000175/B001","relation_type":"near_neighbor","shared_zone":"İki dal da daha önce bulunan bir yön veya izin ardından ilerleme düşüncesini paylaşır."}],"source_phrase_ar":"التتبع فعلك شيئا بعد شيء؛ تتبعت علمه أي اتبعت آثاره (ayn)؛ تتبعت الشيء تتبعا أي تطلبته متتبعا له (sihah)؛ التتبع أن يتتبع في مهلة شيئا بعد شيء؛ يتتبع مساوىء فلان وأثره؛ أتتبعه من اللخاف والعسب (tahdhib)","source_summary":"Ortak kanıt, arama eyleminin tek hamlede değil, zaman tanıyarak ve bir bulgudan ötekine geçerek yürütüldüğünü vurgular; izler, kusurlar ve kayıt parçaları bu yöntemin uygulama alanlarıdır.","sources":["AY","SI","TA"],"what_is_ar":"التتبع في مهلة؛ طلب الشيء أو الأثر شيئا بعد شيء؛ استقصاء المواضع والآثار","what_is_not_ar":"ليس مجرد المشي خلف المتقدم ولا اللحوق السريع"},"support_links":["sup_1ae51219a8d5550a7019"]},{"boundary":"Buradaki çekirdek kesintisiz ardışıklıktır; işin özenli yapılması veya bir hakkın istenmesi bu dala ait değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000175/B004","candidate_links":[{"candidate_id":"cand_b3aef8fe101822c7bec7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَتْبَعَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>atobaEa|ROOT:tbE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"18:85:1:2","qac_word_ref":"18:85:1","surface_ar":"أَتْبَعَ"}],"gloss":"aralıksız peş peşe gelmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birden çok şeyin veya eylemin aralıksız biçimde birbirinin ardından gelmesi."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İki ibadet veya okuma eylemini araya boşluk koymadan peş peşe yapmak."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir anlatıyı bölmeden, bölümlerini birbirine bağlayarak sürdürmek."}}],"root_ar":"ت ب ع","root_id":"root_000175","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Şeylerin, eylemlerin veya anlatım parçalarının kesinti olmadan birbirini izlediği bütün çekirdek bağlamlarda kullanılır.","boundary_detail":"Buradaki çekirdek kesintisiz ardışıklıktır; işin özenli yapılması veya bir hakkın istenmesi bu dala ait değildir.","branch_image_ar":"الولاء والتتابع","concept_gloss":"aralıksız peş peşe gelmek","contextual_glosses":[{"applicability":"Okuma, anlatma veya birbirine bağlanan eylemleri kesintisiz yürütme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kendiliğinden ardışık biçimde gerçekleşen şeyleri doğrudan adlandırmaz.","preserves":"Eylemler arasındaki kesintisizliği ve sürdürme yönünü korur."},"facet_ids":["F002","F003"],"text":"ara vermeden sürdürmek","usage_role":"contextual"}],"definition":"Şeyleri, eylemleri veya anlatım bölümlerini araya kesinti koymadan birbirinin ardından getirmek ya da bunların bu biçimde peş peşe gerçekleşmesi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birden çok şeyin veya eylemin aralıksız biçimde birbirinin ardından gelmesi."},{"facet_id":"F002","role":"specialization","statement":"İki ibadet veya okuma eylemini araya boşluk koymadan peş peşe yapmak."},{"facet_id":"F003","role":"extension","statement":"Bir anlatıyı bölmeden, bölümlerini birbirine bağlayarak sürdürmek."}],"identity_rationale":"Kaynak ifadesi, eylem ve şeylerin araya boşluk girmeden birbirinin ardından gelmesini, anlatımın kesintisiz sürdürülmesini ve bir grubun ötekine ardışık biçimde eklenmesini anlatır. Dalın süreklilik ve ardışıklık çerçevesi bu ortak yapıyı doğru verir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kesintisiz ardışıklık"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"iki şeyi ara vermeden peş peşe yapmak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"aralıksız olarak peş peşe"}],"lexicalization_note":"Ardışıklık bildiren biçimler ile iki eylemi aralıksız bağlayan söz öbeği ayrı yüzler olarak korunur; kapsam yalın köke genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan karşılaştırmalar genel kesintisiz ardışıklığı, daha gevşek sürekliliği ve biçimce yakın fakat anlamca ayrı sağlamlaştırma kullanımını ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekler çok yakındır; odak dal belirli eylem ve anlatım yapılarını ayrıca sözlüksel olarak bağlarken komşu dal daha genel bir sıralama ilişkisi sunar.","focus_only":"Anlatıyı kesintisiz sürdürme ve belirli eylemleri birbirine bağlama kullanımlarını açıkça içerir.","gloss":"kesintisiz ardışıklık","neighbor_only":"Sıralı düzeni genel bir ilişki olarak daha geniş biçimde adlandırır.","neighbor_ref":"root_001684/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da şey veya eylemlerin araya kesinti girmeden birbirinin ardından gelmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal doğrudan ve aralıksız peş peşeliği gerektirir; komşu dal bağlantılı sürmeyi daha geniş zaman ölçeklerinde de kapsayabilir.","focus_only":"Öğeler arasında hiçbir bekleme olmamasını daha kesin bir koşul yapar.","gloss":"bağlantılı biçimde sürmek","neighbor_only":"Bağlantılı bir dizinin zaman içinde sürmesi ve ayların birbirini izlemesi gibi daha geniş süreklilikleri kapsar.","neighbor_ref":"root_000695/B001","relation_type":"near_synonym","shared_zone":"İki dalda da okuma, anlatım veya başka öğeler birbirine bağlı olarak art arda gelir."},{"boundary_match":"partial","distinction":"Burada düzen zamansal ardışıklıktır; komşu dalda ise yapılış kalitesi, tutarlılık veya parçalar arası uyum söz konusudur.","focus_only":"Eylem veya söz bölümlerinin araya boşluk girmeden sıralanmasını anlatır.","gloss":"sıralamak ile sağlamlaştırmak","neighbor_only":"İşin sağlam yapılmasını, sözün tutarlı kurulmasını veya parçaların uyumlu olmasını anlatır.","neighbor_ref":"root_000175/B012","relation_type":"near_neighbor","shared_zone":"Her iki dal bazı söz ve iş yapılarıyla kullanılır ve düzenli bir bütün ortaya çıkarabilir."}],"source_phrase_ar":"التباع الولاء؛ تابعه على كذا متباعة وتباعا (sihah)؛ تابع بين الصلاة وبين القراءة إذا والى بينهما؛ تباعا أي ولاء؛ يتابع الحديث إذا كان يسرده (tahdhib)؛ فأتبعنا بعضهم بعضا (mufradat)","source_summary":"Kanıtlar, ardışık öğeler arasında bekleme veya kopukluk bulunmamasını ortak özellik sayar; eylemleri peş peşe yapma, anlatıyı sürdürme ve grupları sırayla birbirine ekleme bu yapının görünümleridir.","sources":["SI","TA","MU"],"what_is_ar":"توالي الأشياء أو الأعمال بلا مهلة؛ وقوع بعض الشيء إثر بعض؛ السرد المتصل","what_is_not_ar":"ليس الإتقان وحده ولا المطالبة بالحق ولا ولد البقرة"},"support_links":["sup_beb64ee19cae5bb28311"]},{"boundary":"İstemde bulunan kişi ve alacağın başka ödeyene yöneltilmesi kapsamdadır; kişiye yüklenen olumsuz sonuç ayrı daldır.","branch_kind":"mixed_non_bare","branch_ref":"root_000175/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَتْبَعَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>atobaEa|ROOT:tbE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"18:85:1:2","qac_word_ref":"18:85:1","surface_ar":"أَتْبَعَ"}],"gloss":"hak istemek ve alacağı ödeyene yöneltmek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir hak, alacak, kan bedeli veya öç için karşı taraftan ödeme ya da karşılık istemek."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu istemi sürdüren hak veya alacak sahibini adlandırmak."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli yapıda alacağı, ödeme gücü olan başka bir kişiden alınmak üzere o kişiye yöneltmek."}}],"root_ar":"ت ب ع","root_id":"root_000175","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hak veya alacak talebi ile belirli yapıdaki ödeme yönlendirmesini birlikte temsil eden açıklayıcı karşılıktır.","boundary_detail":"İstemde bulunan kişi ve alacağın başka ödeyene yöneltilmesi kapsamdadır; kişiye yüklenen olumsuz sonuç ayrı daldır.","branch_image_ar":"المطالبة والطالب بالحق","concept_gloss":"hak istemek ve alacağı ödeyene yöneltmek","contextual_glosses":[{"applicability":"Para, kan bedeli veya başka bir hakkın karşı taraftan istendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ödeme sorumluluğunu başka kişiye yöneltme yapısını dışarıda bırakır.","preserves":"Hak sahibinin karşı taraftan ödeme veya karşılık istemesini korur."},"facet_ids":["F001","F002"],"text":"alacağını istemek","usage_role":"contextual"},{"applicability":"Alacak sahibinin tahsil için ödeme gücü olan başka bir kişiye gönderildiği özel yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel hak isteme ve istemde bulunan kişi anlamlarını dışarıda bırakır.","preserves":"Alacağın ödeme gücü olan başka bir kişiden alınması işlemini korur."},"facet_ids":["F003"],"text":"ödeyebilecek kişiye yönlendirmek","usage_role":"contextual"}],"definition":"Bir alacak, kan bedeli, öç veya başka bir hak için karşı taraftan ödeme ya da karşılık istemek ve bu istemi yürüten kişi olmak. Belirli yapıda alacak, ödeme gücü olan başka bir kişiden alınmak üzere ona yöneltilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir hak, alacak, kan bedeli veya öç için karşı taraftan ödeme ya da karşılık istemek."},{"facet_id":"F002","role":"extension","statement":"Bu istemi sürdüren hak veya alacak sahibini adlandırmak."},{"facet_id":"F003","role":"associated_use","statement":"Belirli yapıda alacağı, ödeme gücü olan başka bir kişiden alınmak üzere o kişiye yöneltmek."}],"identity_rationale":"Kaynak ifadesi bir alacak, kan bedeli veya öç için istemde bulunmayı ve bunu yapan kişiyi destekler; ayrıca alacağın ödeme gücü olan başka bir kişiden alınmak üzere yönlendirilmesini anlatır. İlk olumsuz örnekte geçen yükümlülük ise komşu dalın sınırına aittir ve bu dalın çekirdeğine katılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"hak, öç veya alacak isteyen kimse"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"alacak için ödeme gücü olan kişiye yönlendirilmek"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kan bedelini veya hakkı uygun biçimde istemek"}],"lexicalization_note":"Hak isteyen kişi biçimi, belirli ödeme yönlendirmesi söz öbeği ve yerleşik biçimde hak istemeyi anlatan birim ayrı tutulur.","neighbor_coverage_note":"Tüm adaylar incelendi; seçilen dört ilişki istem, tahsil, taraf rolü ve istem sonucunda kalan yük arasındaki temel ayrımları verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın nesnesi borçla sınırlı değildir ve ödeme yönlendirmesi uzantısı vardır; komşu dal borcun istenip alınmasını çekirdeğe yerleştirir.","focus_only":"Öç ve kan bedeli istemeyi ve alacağı başka ödeyene yöneltmeyi de kapsar.","gloss":"borcu isteyip tahsil etmek","neighbor_only":"Özellikle borcun istenmesi ve eksiksiz biçimde tahsil edilmesi üzerinde durur.","neighbor_ref":"root_000244/B003","relation_type":"near_synonym","shared_zone":"Her iki dalda da alacak sahibi borçlu taraftan hakkını ister."},{"boundary_match":"partial","distinction":"Odak dal istem ve istem sahibi merkezlidir; komşu dal borcun yerine getirilmesi veya hakkın fiilen alınması sonucunu öne çıkarır.","focus_only":"Hak sahibinin istemde bulunmasını ve alacak için başka ödeyene yönelmesini anlatır.","gloss":"hakkı ödemek veya almak","neighbor_only":"Borcun ödenmesi, hakkın teslim alınması ve gereken miktarın tamamlanması sonucunu kapsar.","neighbor_ref":"root_001237/B006","relation_type":"near_neighbor","shared_zone":"İki dal da borç, kan bedeli ve başka hakların taraflar arasında yerine getirilmesi alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal istem eylemi ve istem sahibine dayanır; komşu dal eylemden bağımsız olarak borç ilişkisindeki taraf rollerini adlandırır.","focus_only":"Hak isteme eylemini ve istemi yürüten alacak sahibini adlandırır.","gloss":"alacaklı ile borçlu taraf","neighbor_only":"Borç ilişkisine bağlı alacaklı veya borçlu tarafın kalıcı rolünü iki yönlü biçimde adlandırır.","neighbor_ref":"root_001081/B002","relation_type":"same_field","shared_zone":"Her iki dal bir borç veya alacak ilişkisindeki tarafları ve bunların karşılıklı bağını konu edinir."},{"boundary_match":"partial","distinction":"Burada odak, isteyen kişi ve istem eylemidir; komşu dalda odak, öteki kişinin üzerinde kalan yükümlülük veya olumsuz sonuçtur.","focus_only":"Bir hakkın peşine düşen kişiyi ve onun istemde bulunmasını anlatır.","gloss":"istem sahibi ile kalan yük","neighbor_only":"Bir olay nedeniyle kişinin üzerinde kalan hak, istem veya istenmeyen sonucu anlatır.","neighbor_ref":"root_000175/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal hak isteme ilişkisinin karşıt taraflarını ve bundan doğan bağı konu edinir."}],"source_phrase_ar":"ليس عليك من هذا الأمر تبيعة وتباعة وتبعة (jamhara)؛ التبيع الذي لك عليه مال (sihah)؛ التبيع تابع بالثأر أو مطالب؛ اتباع بالمعروف أي المطالبة بالدية؛ له عليك مال يتابعك به أي يطالبك به؛ إذا أتبع أحدكم على مليء فليتبع (tahdhib)؛ أتبعت عليه أي أحلت عليه؛ أتبع فلان بمال أي أحيل عليه (mufradat)","source_summary":"Toplu kanıt, hak veya alacak için istemde bulunma ile istem sahibini aynı alan içinde verir ve ödeme sorumluluğunun ödeme gücü bulunan başka bir kişiye yöneltildiği özel yapıyı da kaydeder. Yükümlülüğün kendisini anlatan olumsuz örnek, dal sınırını belirler.","sources":["JA","SI","TA","MU"],"what_is_ar":"المطالبة بالحق أو الثأر أو الدية أو المال؛ التبيع بمعنى الطالب أو صاحب المطالبة؛ الحوالة على مليء","what_is_not_ar":"ليس مطلق الاتباع ولا التبعة بمعنى ما يلحق الإنسان من مكروه"},"support_links":[]},{"boundary":"Bu dal hakkı isteyen kişiyi değil, olay nedeniyle kişinin üzerinde kalan istemi, yükü veya olumsuz sonucu anlatır.","branch_kind":"bare","branch_ref":"root_000175/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَتْبَعَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>atobaEa|ROOT:tbE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"18:85:1:2","qac_word_ref":"18:85:1","surface_ar":"أَتْبَعَ"}],"gloss":"üzerinde kalan yükümlülük veya olumsuz sonuç","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir olay nedeniyle kişinin üzerinde kalan ve yerine getirilmesi beklenen hak veya istem."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı olaydan kişiye ilişen hoş olmayan sonuç, yük veya haksızlık benzeri sorumluluk."}}],"root_ar":"ت ب ع","root_id":"root_000175","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir olayın ardından kişiye bağlanan hak istemini, sorumluluğu veya hoş olmayan sonucu birlikte kapsar.","boundary_detail":"Bu dal hakkı isteyen kişiyi değil, olay nedeniyle kişinin üzerinde kalan istemi, yükü veya olumsuz sonucu anlatır.","branch_image_ar":"التبعة اللازمة","concept_gloss":"üzerinde kalan yükümlülük veya olumsuz sonuç","contextual_glosses":[{"applicability":"Bir işten dolayı kişiden daha sonra hak, ödeme veya hesap sorulabileceği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yükün yalnızca hoş olmayan sonuç olarak belirdiği kullanımları daraltır.","preserves":"Olaydan sonra kişi üzerinde kalan yerine getirme yükünü korur."},"facet_ids":["F001"],"text":"doğacak sorumluluk","usage_role":"contextual"},{"applicability":"Bir işten kişiye hoşlanmayacağı bir şeyin ilişmeyeceği ya da ilişeceği söylenen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Belirli bir hak veya ödeme isteminin kişi üzerinde kalması yönünü dışarıda bırakır.","preserves":"Kişiye sonradan ilişen hoş olmayan sonuç yönünü korur."},"facet_ids":["F002"],"text":"başına gelecek istenmeyen sonuç","usage_role":"contextual"}],"definition":"Bir iş, davranış veya ilişki nedeniyle kişinin üzerinde kalan hak istemi, sorumluluk ya da ona sonradan ilişen istenmeyen sonuç.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir olay nedeniyle kişinin üzerinde kalan ve yerine getirilmesi beklenen hak veya istem."},{"facet_id":"F002","role":"extension","statement":"Aynı olaydan kişiye ilişen hoş olmayan sonuç, yük veya haksızlık benzeri sorumluluk."}],"identity_rationale":"Kaynak ifadesi, bir olay yüzünden kişinin üzerinde kalan hak, istem, haksızlık benzeri yük veya hoşlanmayacağı sonucu adlandırır. Dal çerçevesi bu sonradan ilişen yükümlülük ve olumsuz sonuç anlamını doğru biçimde sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kişinin üzerinde kalan hak, sorumluluk veya istenmeyen sonuç"}],"lexicalization_note":"Dal yalın ad biçimlerinin ortak anlamını tanımlar; istemde bulunma eylemi veya özel ödeme yapısı içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen karşılaştırmalar kalan yükü suç sonucu, genel ağırlık, bağlayıcı oluş ve hak isteme eyleminden ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kaynağı hak ilişkisi veya istenmeyen herhangi bir sonuç olabilir; komşu dal nedenselliği kişinin işlediği davranış ve suç üzerinde yoğunlaştırır.","focus_only":"Yükün bir alacak veya başka bir hak isteminden doğmasını da kapsar.","gloss":"eylemin doğurduğu yük","neighbor_only":"Yükü özellikle kişinin kendi suçu veya eylemiyle başına çektiği kötülük olarak kurar.","neighbor_ref":"root_000235/B004","relation_type":"near_synonym","shared_zone":"Her iki dalda da kişinin yaptığı veya bağlı olduğu bir olay ona sonradan bir sorumluluk ya da kötülük getirir."},{"boundary_match":"partial","distinction":"Odak dal bir olayın ardından kişi üzerinde kalan istem veya sonuçtur; komşu dal genel ağırlık ve olumsuz niteliklere de yayılır.","focus_only":"Belirli bir işten doğan hak istemi veya sonradan ilişen sonucu anlatır.","gloss":"ağır yük ve sorumluluk","neighbor_only":"Ağırlık, kötülük, ayıp ve güçlük gibi daha geniş olumsuz nitelikleri de kapsar.","neighbor_ref":"root_000006/B004","relation_type":"near_synonym","shared_zone":"Her iki dal kişiye yüklenen ağır, istenmeyen veya sorumluluk doğuran bir durumu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal kalan yükün kendisini adlandırır; komşu dal bu yükün bağlayıcı ve yerine getirilmesi gereken duruma gelmesini anlatır.","focus_only":"Hak dışında hoş olmayan bir sonucun kişiye ilişmesini de kapsar.","gloss":"yerine getirilmesi gerekir olmak","neighbor_only":"Borcun, cezanın veya başka bir sonucun hukuken ya da fiilen yerine getirilmesi gereken duruma gelmesini anlatır.","neighbor_ref":"root_000351/B004","relation_type":"near_neighbor","shared_zone":"İki dalda da kişi üzerinde yerine getirilmesi beklenen bir hak veya ceza bulunabilir."},{"boundary_match":"partial","distinction":"Odak dal borçlu tarafta kalan yük veya sonuçtur; komşu dal alacaklı taraftaki istem ve istem sahibidir.","focus_only":"İstem veya olumsuz sonucun kendisini ve bunun kişi üzerinde kalmasını anlatır.","gloss":"kalan yük ile hak isteme","neighbor_only":"Hakkın peşine düşen kişiyi, istem eylemini ve ödeme için başka kişiye yönelmeyi anlatır.","neighbor_ref":"root_000175/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal aynı hak ilişkisinin ve karşılık istemenin farklı taraflarını yansıtabilir."}],"source_phrase_ar":"ليس عليك من هذا الأمر تبيعة وتباعة وتبعة أي لا يلحقك منه شيء تكرهه (jamhara)؛ التباعة مثل التبعة (sihah)؛ التبعة والتباعة اسم للشيء الذي لك فيه بغية شبه ظلامة (tahdhib)","source_summary":"Ortak anlatım, kişinin yaptığı ya da içinde bulunduğu bir işten sonra üzerinde kalan istem veya yükü merkez alır; bunun bir hak talebi, haksızlık benzeri sorumluluk veya hoş karşılanmayan sonuç olması mümkündür.","sources":["JA","SI","TA"],"what_is_ar":"التبعة والتباعة والتبيعة؛ ما يلحق الإنسان من حق أو طلب أو مكروه بسبب أمر ما","what_is_not_ar":"ليس الطالب نفسه ولا الحوالة ولا ولد البقرة"},"support_links":[]},{"boundary":"Bu hayvan adı ve anne-yavru söz öbeği, insan izleyiciden, hak isteyenden ve genel küçükbaş yavru adlarından ayrıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000175/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَتْبَعَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>atobaEa|ROOT:tbE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"18:85:1:2","qac_word_ref":"18:85:1","surface_ar":"أَتْبَعَ"}],"gloss":"ilk yılındaki sığır yavrusu ve yavrusu ardındaki inek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İlk yaş yılı içindeki erkek sığır yavrusunu adlandırmak."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı yaştaki dişi sığır yavrusunu ayrı bir biçimle adlandırmak."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yavrusu arkasından gelen ineği belirli bir söz öbeğiyle nitelemek."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Otuz sığır üzerinden verilen yükümlülükte ilk yılındaki bir yavrunun alınması."}}],"root_ar":"ت ب ع","root_id":"root_000175","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaşı belirli erkek ve dişi sığır yavrularını ve bunların anneyle izleme ilişkisine dayalı inek söz öbeğini birlikte temsil eder.","boundary_detail":"Bu hayvan adı ve anne-yavru söz öbeği, insan izleyiciden, hak isteyenden ve genel küçükbaş yavru adlarından ayrıdır.","branch_image_ar":"ولد البقرة التابع لها","concept_gloss":"ilk yılındaki sığır yavrusu ve yavrusu ardındaki inek","contextual_glosses":[{"applicability":"Erkek yavrunun yaşı ve türü özellikle belirtildiğinde, sürü yükümlülüğü örneği dahil kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dişi yavruyu ve yavrusu arkasından gelen inek söz öbeğini dışarıda bırakır.","preserves":"Erkek sığır yavrusunun ilk yaş yılı içinde bulunmasını korur."},"facet_ids":["F001","F004"],"text":"ilk yaş yılındaki erkek sığır yavrusu","usage_role":"contextual"},{"applicability":"İneğin, onu izleyen yavrusuyla birlikte nitelendiği söz öbeğine özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Erkek ve dişi yavrunun bağımsız yaş adlarını dışarıda bırakır.","preserves":"Anne ineğin ardında ilerleyen yavruyla kurduğu ilişkiyi korur."},"facet_ids":["F003"],"text":"yavrusu arkasından gelen inek","usage_role":"contextual"}],"definition":"İlk yılındaki erkek veya dişi sığır yavrusu, özellikle annesinin ardından giden yavru; ayrıca yavrusu arkasından gelen inek için kullanılan bağlı adlandırma.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İlk yaş yılı içindeki erkek sığır yavrusunu adlandırmak."},{"facet_id":"F002","role":"specialization","statement":"Aynı yaştaki dişi sığır yavrusunu ayrı bir biçimle adlandırmak."},{"facet_id":"F003","role":"associated_use","statement":"Yavrusu arkasından gelen ineği belirli bir söz öbeğiyle nitelemek."},{"facet_id":"F004","role":"example","statement":"Otuz sığır üzerinden verilen yükümlülükte ilk yılındaki bir yavrunun alınması."}],"identity_rationale":"Kaynak ifadesi ilk yılındaki erkek ve dişi sığır yavrusunu, annesinin ardından giden yavruyu ve yavrusu ardında bulunan ineği birlikte açıklar; belirli bir sürü sayısında alınan yavru da uygulama örneğidir. Dal çerçevesi yaş, cinsiyet ve anne-yavru ilişkisini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"ilk yaş yılındaki erkek sığır yavrusu"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ilk yaş yılındaki dişi sığır yavrusu"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yavrusu arkasından gelen inek"}],"lexicalization_note":"Yavrunun erkek ve dişi adları ile yavrusu ardından gelen inek için kullanılan söz öbeği ayrı tutulur; sayı örneği çekirdeğe dönüştürülmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen dört komşu genel sığır yavrusu, başka bir sığır yavrusu adı, geniş yavru sınıfı ve annesini izleyen başka türleri ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yaş ve anne ardınca gitme gerekçesiyle daha sınırlıdır ve inek söz öbeğini de taşır; komşu dal genel yavru adıdır.","focus_only":"İlk yaş yılını, erkek ve dişi için ayrı biçimleri ve yavrusu ardındaki inek yapısını içerir.","gloss":"sığır yavrusu","neighbor_only":"Yaş sınırı koymadan evcil sığır yavrusunu genel olarak adlandırır.","neighbor_ref":"root_000987/B002","relation_type":"near_synonym","shared_zone":"İki dalın da temel göndergesi evcil sığırın erkek veya dişi yavrusudur."},{"boundary_match":"partial","distinction":"Odak adlandırma yaş ve anne ardınca gitme ilişkisine bağlıdır; komşu adlandırma hafiflik tasarımına dayanır.","focus_only":"Yavrunun ilk yaş yılını ve annesinin ardından gitmesini kurucu özellik sayar.","gloss":"hafif sığır yavrusu","neighbor_only":"Sığır yavrusunu hafiflik çağrışımıyla adlandırır ve belirli bir yaş sınırı vermez.","neighbor_ref":"root_001151/B003","relation_type":"near_synonym","shared_zone":"Her iki dal aynı hayvan türünün genç yavrusunu adlandırır."},{"boundary_match":"field_only","distinction":"Odak dal sığıra ve ilk yaş yılına özgüdür; komşu dal çeşitli küçükbaş ve yabani hayvan yavrularını daha geniş bir sınıfta toplar.","focus_only":"Yalnız sığır yavrusunu ve belirli ilk yaş yılını kapsar.","gloss":"küçük çiftlik hayvanları","neighbor_only":"Koyun, keçi, davar ve yabani sığırın küçük yavrularını topluca kapsar.","neighbor_ref":"root_000160/B004","relation_type":"same_field","shared_zone":"İki dal da yetişkinliğe erişmemiş çiftlik hayvanlarını yaş ve tür bakımından adlandırır."},{"boundary_match":"partial","distinction":"İzleme ilişkisi ortak olsa da odak dal sığır ve yaş sınıfına, komşu dal başka hayvan türlerinin yavrularına bağlıdır.","focus_only":"Sığır yavrusunu, cinsiyet biçimlerini ve ilk yaş yılını belirtir.","gloss":"annesini izleyen yavru","neighbor_only":"Özellikle deve veya koyun yavrusunun annesinin ardından gelmesini anlatır.","neighbor_ref":"root_000186/B006","relation_type":"near_neighbor","shared_zone":"İki dalda da yavrunun annesinin ardından yürümesi adlandırmanın gerekçesidir."}],"source_phrase_ar":"بقرة متبع إذا كان ولدها يتبعها والولد تبيع (jamhara)؛ التبيع ولد البقرة في أول سنة والأنثى تبيعة (sihah)؛ يأخذ من كل ثلاثين من البقر تبيعا؛ ولد البقرة أول سنة تبيع؛ بقرة متبع خلفها تبيع (tahdhib)؛ التبيع خص بولد البقر إذا تبع أمه؛ المتبع من البهائم التي يتبعها ولدها (mufradat)","source_summary":"Ortak kanıt, adlandırmayı sığır yavrusunun ilk yaş yılına ve annesinin ardından gitmesine bağlar, dişi yavru için ayrı biçimi belirtir ve yavrusu arkasında bulunan ineği aynı ilişki üzerinden niteler. Sürü sayısına bağlı alma örneği uygulama düzeyindedir.","sources":["JA","SI","TA","MU"],"what_is_ar":"التبيع والتبيعة لولد البقرة في سنه؛ البقرة المتبع التي يتبعها ولدها؛ ما اتصل بذلك من عدد الصدقة والحيوان","what_is_not_ar":"ليس التابع من الناس ولا الظل ولا المطالبة بالحق"},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_000175/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَتْبَعَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>atobaEa|ROOT:tbE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"18:85:1:2","qac_word_ref":"18:85:1","surface_ar":"أَتْبَعَ"}],"gloss":"biçime bağlı adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Güneşin hareketini izlediği düşüncesiyle gölgeyi adlandırmak."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir binek hayvanının ayağını veya bütün bacaklarını adlandırmak."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gökyüzündeki belirli bir yıldızı ve onun küçültmeli adını belirtmek."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Belirli bir kuş türünü aynı biçimle adlandırmak."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"İri ve güzel sayılan belirli bir kanatlı böcek türünü adlandırmak."}},{"facet_id":"F006","role":"source_variant","source_fields":["distinctive_facets[F006]"],"statements":{"statement":"Bir arı topluluğunun önderini aynı biçimle adlandırmak."}}],"root_ar":"ت ب ع","root_id":"root_000175","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"التابع الحسي","concept_gloss":"biçime bağlı adlandırmalar","contextual_glosses":[{"applicability":"Yalnız gölge göndergesinin, güneşin konumuna göre yer değiştirmesi açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvan bacağı, yıldız, kuş, böcek ve arı önderi göndergelerini dışarıda bırakır.","preserves":"Gölge göndergesini ve adlandırmadaki izleme gerekçesini korur."},"facet_ids":["F001"],"text":"güneşi izleyen gölge","usage_role":"explanatory"}],"definition":"Tek bir kavram değil, aynı yalın biçimle adlandırılan ayrı göndergeler dizisidir: gölge, hayvan ayağı veya bacakları, belirli bir yıldız, bir kuş, iri bir böcek ve arı topluluğunun önderi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Güneşin hareketini izlediği düşüncesiyle gölgeyi adlandırmak."},{"facet_id":"F002","role":"source_variant","statement":"Bir binek hayvanının ayağını veya bütün bacaklarını adlandırmak."},{"facet_id":"F003","role":"source_variant","statement":"Gökyüzündeki belirli bir yıldızı ve onun küçültmeli adını belirtmek."},{"facet_id":"F004","role":"source_variant","statement":"Belirli bir kuş türünü aynı biçimle adlandırmak."},{"facet_id":"F005","role":"source_variant","statement":"İri ve güzel sayılan belirli bir kanatlı böcek türünü adlandırmak."},{"facet_id":"F006","role":"source_variant","statement":"Bir arı topluluğunun önderini aynı biçimle adlandırmak."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"güneşin hareketini izleyen gölge"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"belirli bir yıldızın adı"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"belirli bir kuş veya iri kanatlı böcek türü"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"binek hayvanının ayağı veya bacakları"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"القوائم يقال لها تبع (ayn)؛ سمي الظل تبعا لاتباعه الشمس (jamhara)؛ التبع أيضا الظل؛ التبع أيضا ضرب من الطير (sihah)؛ التبع الطل؛ التبع هو الدبران؛ التابع والتويبع؛ التبع ضرب من اليعاسيب؛ التبع سيد النحل (tahdhib)؛ التبع رجل الدابة؛ التبع الظل (mufradat)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["AY","JA","SI","TA","MU"],"what_is_ar":"ما سمي تبعا من ظل أو رجل دابة أو قوائم أو نجم أو طير أو يعاسيب أو سيد نحل بحسب نصوص المصادر","what_is_not_ar":"ليس ملك تبع ولا ولد البقرة ولا الجنية التابعة"},"support_links":[]},{"boundary":"Bu dal genel hükümdarlığı değil, belirli tarihsel gelenekteki unvanı ve onun çoğul taşıyıcılarını anlatır.","branch_kind":"bare","branch_ref":"root_000175/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَتْبَعَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>atobaEa|ROOT:tbE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"18:85:1:2","qac_word_ref":"18:85:1","surface_ar":"أَتْبَعَ"}],"gloss":"eski güneybatı Arabistan hükümdar unvanı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir eski krallık geleneğinin tek bir hükümdarına verilen unvan."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu unvanı taşıyan hükümdar veya yöneticileri toplu ve çoğul olarak adlandırmak."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Adlandırmayı yöneticilerin birbirinin ardından gelmesine veya halkın yöneticiyi izlemesine bağlamak."}}],"root_ar":"ت ب ع","root_id":"root_000175","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli tarihsel krallık geleneğinin tek hükümdarını ve çoğul taşıyıcılarını adlandıran unvan için kullanılır.","boundary_detail":"Bu dal genel hükümdarlığı değil, belirli tarihsel gelenekteki unvanı ve onun çoğul taşıyıcılarını anlatır.","branch_image_ar":"تُبَّع وملوكه","concept_gloss":"eski güneybatı Arabistan hükümdar unvanı","contextual_glosses":[{"applicability":"Unvanı taşıyan hükümdarların çoğul topluluğu ve adlandırmanın ardışıklık açıklaması birlikte vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir hükümdarın unvan olarak adlandırılmasını doğrudan karşılamaz.","preserves":"Hükümdarların çoğulluğunu ve yönetimde birbirlerinin ardından gelmelerini korur."},"facet_ids":["F002","F003"],"text":"birbirinin ardından gelen eski hükümdarlar","usage_role":"explanatory"}],"definition":"Güneybatı Arabistan'daki belirli bir eski krallık geleneğinde hükümdara verilen unvan ve bu unvanı birbirinin ardından taşıyan hükümdar ya da yönetici topluluğu.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir eski krallık geleneğinin tek bir hükümdarına verilen unvan."},{"facet_id":"F002","role":"extension","statement":"Bu unvanı taşıyan hükümdar veya yöneticileri toplu ve çoğul olarak adlandırmak."},{"facet_id":"F003","role":"associated_use","statement":"Adlandırmayı yöneticilerin birbirinin ardından gelmesine veya halkın yöneticiyi izlemesine bağlamak."}],"identity_rationale":"Kaynak ifadesi, belirli bir eski krallık geleneğindeki hükümdar unvanını ve bu unvanı taşıyan hükümdarların ardışık topluluğunu açıkça verir; adlandırmayı da birbirinin ardından yönetmeye veya halkın hükümdarın ardından gitmesine bağlar. Dal çerçevesi unvan ile çoğul hükümdar sınıfını doğru bir arada tutar.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"eski güneybatı Arabistan krallık geleneğinde hükümdar"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"aynı gelenekte birbirinin ardından gelen hükümdarlar"}],"lexicalization_note":"Dal yalın unvan ve onun çoğul biçimiyle sınırlıdır; genel izleyici, gölge veya hayvan yavrusu anlamları tanıma alınmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; yayımlanan üç karşılaştırma aynı tarihsel alandaki iki ayrı hükümdar unvanı ve bir hükümdar topluluğuyla sınırı gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak unvan ardışık hükümdarlar sınıfına bağlanır; komşu unvan farklı bir sözlüksel addır ve buyurgan davranma uzantısı taşır.","focus_only":"Hükümdarların ardışık topluluğunu ve halkın yöneticiye bağlılığına dayalı açıklamayı içerir.","gloss":"bölgesel hükümdar unvanı","neighbor_only":"Aynı bölgesel gelenekte hükümdarlığın yanında başkası üzerinde buyurgan davranmayı da kapsar.","neighbor_ref":"root_001276/B001","relation_type":"near_synonym","shared_zone":"Her iki dal aynı geniş tarihsel bölgede hükümdar için kullanılan özel bir unvanı anlatır."},{"boundary_match":"partial","distinction":"Odak unvan kendi ardışık hükümdarlar dizisini kurar; komşu unvan açık bir derece sınırı ve ayrıca kadın yönetici biçimi taşır.","focus_only":"Halkın izlediği hükümdarı ve aynı unvanı taşıyan ardışık yöneticileri anlatır.","gloss":"daha alt derecedeki bölgesel hükümdar","neighbor_only":"Daha büyük hükümdarın altında bulunan bölgesel yönetici derecesini ve kadın biçimini de belirtir.","neighbor_ref":"root_001272/B004","relation_type":"near_synonym","shared_zone":"İki dal da aynı geniş tarihsel çevrede kullanılan hükümdar veya yönetici unvanlarıdır."},{"boundary_match":"field_only","distinction":"Odak dal bir unvanın sözlüksel anlamıdır; komşu dal yer ve topluluk adından türeyen belirli bir hükümdar hanesini anlatır.","focus_only":"Bir hükümdar unvanını ve o unvanın tarihsel taşıyıcılarını adlandırır.","gloss":"bölgesel hükümdar topluluğu","neighbor_only":"Bir yer, bir topluluk ve o topluluktan gelen başka bir hükümdar hanesini özel adlarla belirtir.","neighbor_ref":"root_000250/B004","relation_type":"same_field","shared_zone":"Her iki dal güneybatı Arabistan kökenli eski hükümdar topluluklarıyla ilişkilidir."}],"source_phrase_ar":"التبابعة سموا بذلك لاتباع بعضهم في الملك بعضا (jamhara)؛ التبابعة ملوك اليمن الواحد تبع (sihah)؛ تبع الملك؛ كان تبع ملكا من الملوك؛ فيهم تبابعة (tahdhib)؛ تبع كانوا رؤساء سموا بذلك لاتباع بعضهم بعضا في الرياسة والسياسة؛ تبع ملك يتبعه قومه (mufradat)","source_summary":"Ortak kanıt, sözcüğü belirli bir güneybatı Arabistan krallık geleneğinin hükümdar unvanı ve bu hükümdarların çoğul adı olarak tanımlar; unvanın gerekçesi yönetimde ardışıklık veya halkın yöneticiye bağlılığıyla açıklanır.","sources":["JA","SI","TA","MU"],"what_is_ar":"تبع الملك؛ التبابعة ملوك اليمن أو الرؤساء الذين يتبع بعضهم بعضا في الملك والسياسة","what_is_not_ar":"ليس التبع بمعنى الظل ولا التابع العام ولا ولد البقرة"},"support_links":[]},{"boundary":"Genel görünmeyen varlık sınıfı değil, belirli bir insanı her yerde izleyen dişi eşlikçi söz konusudur.","branch_kind":"bare","branch_ref":"root_000175/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَتْبَعَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>atobaEa|ROOT:tbE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"18:85:1:2","qac_word_ref":"18:85:1","surface_ar":"أَتْبَعَ"}],"gloss":"insanı her yerde izleyen dişi doğaüstü eşlikçi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir insana bağlı olarak onunla birlikte bulunan dişi doğaüstü varlık."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bağlı olduğu insanı gittiği her yerde sürekli olarak izlemek."}}],"root_ar":"ت ب ع","root_id":"root_000175","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli bir kişiye bağlı olduğuna ve onunla sürekli dolaştığına inanılan dişi varlığın eksiksiz açıklayıcı karşılığıdır.","boundary_detail":"Genel görünmeyen varlık sınıfı değil, belirli bir insanı her yerde izleyen dişi eşlikçi söz konusudur.","branch_image_ar":"الجنية التابعة","concept_gloss":"insanı her yerde izleyen dişi doğaüstü eşlikçi","contextual_glosses":[{"applicability":"Varlığın bir insanla birlikte bulunması öne çıktığında kullanılır; sürekli izleme bağlamdan anlaşılmalıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dişi oluşu ve kişinin gittiği her yere peşinden gitme koşulunu açıkça söylemez.","preserves":"Belirli kişiye bağlı doğaüstü eşlikçi olma yönünü korur."},"facet_ids":["F001"],"text":"kişiye bağlı doğaüstü eşlikçi","usage_role":"explanatory"}],"definition":"Belirli bir insanla birlikte bulunduğuna ve o insan nereye giderse peşinden gittiğine inanılan dişi doğaüstü varlık.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir insana bağlı olarak onunla birlikte bulunan dişi doğaüstü varlık."},{"facet_id":"F002","role":"core","statement":"Bağlı olduğu insanı gittiği her yerde sürekli olarak izlemek."}],"identity_rationale":"Kaynak ifadesi, bir insanla birlikte bulunduğuna ve nereye giderse onu izlediğine inanılan dişi doğaüstü varlığı açıkça tanımlar. Dal çerçevesi varlığın türünü, cinsiyetini, insana bağlılığını ve sürekli eşlik etmesini korur.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bir insanı gittiği her yerde izleyen dişi doğaüstü varlık"}],"lexicalization_note":"Dal yalın ad biçiminin bu özel doğaüstü varlık anlamıyla sınırlıdır; insan izleyici veya başka eşlikçi türleri içeri alınmaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; seçilen dört ilişki özel eşlikçi varlığı geniş doğaüstü varlık sınıfından, insan eşlikçilerden, etkilenme alanından ve genel izleyiciden ayırır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal belirli kişiye bağlanan tek bir dişi eşlikçidir; komşu dal geniş varlık sınıfını ve topluluğunu adlandırır.","focus_only":"Belirli bir insana bağlı, dişi ve sürekli eşlik eden tek varlığı anlatır.","gloss":"görünmeyen varlıklar topluluğu","neighbor_only":"Görünmeyen doğaüstü varlıkların bütün türünü ve onların çok bulunduğu yeri kapsar.","neighbor_ref":"root_000266/B005","relation_type":"same_field","shared_zone":"İki dal da insan dışı ve görünmeyen olduğuna inanılan doğaüstü varlıklar alanındadır."},{"boundary_match":"partial","distinction":"Odak eşlikçi doğaüstü ve izleyicidir; komşu eşlikçiler insan ilişkileri ve hizmet rolleri içinde tanımlanır.","focus_only":"Eşlikçinin doğaüstü, dişi ve kişiyi her yerde izleyen bir varlık olmasını gerektirir.","gloss":"sürekli yanında bulunan eşlikçi","neighbor_only":"Oturma ve birlikte bulunma ilişkisi üzerinden eş, hizmetçi veya sürekli insan yoldaşı gibi rolleri kapsar.","neighbor_ref":"root_001244/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal belirli bir kişinin yanında sürekli bulunan bir eşlikçi rolünü anlatabilir."},{"boundary_match":"field_only","distinction":"Odak dalın çekirdeği sürekli eşliktir; komşu dal tür adı, hayvan ilişkisi ve insandaki etkilenme durumlarına yayılır.","focus_only":"Bir insanı düzenli olarak izleyen dişi eşlikçi varlığı anlatır.","gloss":"doğaüstü varlık ve etkisi","neighbor_only":"Doğaüstü bir varlık türünü, ona bağlanan hayvanları ve etkilenmiş ya da aklı bozulmuş kişiyi kapsar.","neighbor_ref":"root_000364/B006","relation_type":"same_field","shared_zone":"İki dal da görünmeyen varlık inançları ve bu varlıkların insanla ilişkisi alanındadır."},{"boundary_match":"partial","distinction":"Odak dal genel izleme eylemini değil, bu eylemle tanımlanan belirli bir doğaüstü varlık türünü sözlükselleştirir.","focus_only":"İzleyenin belirli türde dişi doğaüstü bir varlık ve sürekli eşlikçi olmasını gerektirir.","gloss":"genel izleyici ile doğaüstü eşlikçi","neighbor_only":"İnsanların, toplulukların, izlerin, buyrukların ve örneklerin ardından gitmeyi genel olarak kapsar.","neighbor_ref":"root_000175/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir katılımcı başka bir kişinin gittiği yönde onun ardından hareket eder."}],"source_phrase_ar":"التابعة جنية تكون مع الإنسان تتبعه حيثما ذهب (ayn)؛ معه تابعة أي من الجن (sihah)","source_summary":"Ortak kanıt, dişi doğaüstü varlığı belirli bir insanın sürekli eşlikçisi olarak tanımlar ve bu varlığın kişinin gittiği her yere onun ardından gittiğini belirtir.","sources":["AY","SI"],"what_is_ar":"التابعة من الجن التي تكون مع الإنسان وتتبعه حيث ذهب","what_is_not_ar":"ليس التابع البشري ولا ملك تبع ولا التبع من الظل"},"support_links":[]},{"boundary":"Anlam belirtilen kadınlarla ilgili söz öbeklerine bağlıdır; genel ardından gitme veya buyruğa uyma anlamına genişletilemez.","branch_kind":"collocation","branch_ref":"root_000175/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَتْبَعَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>atobaEa|ROOT:tbE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"18:85:1:2","qac_word_ref":"18:85:1","surface_ar":"أَتْبَعَ"}],"gloss":"kadınların peşinden cinsel amaçla gitmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadınların peşinden cinsel yaklaşma amacıyla giden erkeği belirli söz öbeğiyle nitelemek."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kadın kölelerle evlilik dışı cinsel ilişki kurmayı veya bunun için peşlerinden gitmeyi anlatmak."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı kuruluş kalıbını kadınlarla konuşan veya onları ziyaret eden erkek nitelemeleriyle karşılaştırmak."}}],"root_ar":"ت ب ع","root_id":"root_000175","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız verilen kadın ve kadın köle söz öbeklerinde, erkeğin cinsel yaklaşma veya ilişki amacıyla peşlerinden gitmesini karşılar.","boundary_detail":"Anlam belirtilen kadınlarla ilgili söz öbeklerine bağlıdır; genel ardından gitme veya buyruğa uyma anlamına genişletilemez.","branch_image_ar":"اتباع النساء","concept_gloss":"kadınların peşinden cinsel amaçla gitmek","contextual_glosses":[{"applicability":"Kadın kölelerle cinsel ilişki anlamının açıkça amaçlandığı özel söz öbeğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel olarak kadınların peşinden cinsel yaklaşma amacıyla gitme kapsamını daraltır.","preserves":"Hedef grubunu ve evlilik dışı cinsel ilişki anlamını açıkça korur."},"facet_ids":["F002"],"text":"kadın kölelerle evlilik dışı ilişki kurmak","usage_role":"contextual"},{"applicability":"Erkeğin kadınlara yönelik sürekli cinsel ilgisi ve onları araması kişi niteliği olarak belirtildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kadın kölelerle fiilî evlilik dışı ilişki kurma anlamını zorunlu kılmaz.","preserves":"Erkek katılımcıyı ve kadınlara yönelik cinsel amaçlı arayışı korur."},"facet_ids":["F001"],"text":"kadınların peşinden koşan erkek","usage_role":"contextual"}],"definition":"Bir erkeğin kadınların veya kadın kölelerin peşinden cinsel ilişki ya da yaklaşma amacıyla gitmesi ve bu davranışla nitelenmesi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadınların peşinden cinsel yaklaşma amacıyla giden erkeği belirli söz öbeğiyle nitelemek."},{"facet_id":"F002","role":"specialization","statement":"Kadın kölelerle evlilik dışı cinsel ilişki kurmayı veya bunun için peşlerinden gitmeyi anlatmak."},{"facet_id":"F003","role":"source_variant","statement":"Aynı kuruluş kalıbını kadınlarla konuşan veya onları ziyaret eden erkek nitelemeleriyle karşılaştırmak."}],"identity_rationale":"Kaynak ifadesi, kadınların veya kadın kölelerin peşinden cinsel ilişki ya da yaklaşma amacıyla giden erkeği ve bu davranışı açıkça anlatır. Dal çerçevesi katılımcı yönünü, hedef grubunu ve cinsel amacı doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"kadın kölelerle evlilik dışı ilişki kurmak veya bunun için peşlerinden gitmek"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"kadınların peşinden cinsel amaçla giden erkek"}],"lexicalization_note":"Dal yalnızca verilen kadın ve kadın kölelerle kurulan söz öbeklerinde geçerlidir; bu cinsel amaçlı kullanım yalın kök anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen ilişkiler peşinden gitmeyi cinsel eşlikçilikten, birleşme eyleminden, genel aramadan ve karşı tarafın işaret davranışından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal peşinden gitme ve arama davranışıdır; komşu dal kurulmuş cinsel birliktelikteki eşlikçi rolünü adlandırır.","focus_only":"Erkeğin kadınların peşinden gitmesini ve arayışını tek yönlü davranış olarak anlatır.","gloss":"cinsel eşlikçi","neighbor_only":"Kadın veya erkeğin cinsel ilişki içindeki eşlikçisini ve karşılıklı birlikteliği adlandırır.","neighbor_ref":"root_000397/B002","relation_type":"near_neighbor","shared_zone":"İki dal da kadın ile erkek arasındaki cinsel amaçlı yakınlık alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal kişiyi ve peşinden gitme davranışını söz öbeğiyle niteler; komşu dal birleşme veya evlilik eyleminin kendisini anlatır.","focus_only":"Kadınların peşinden giden erkeğin arayışını veya kadın kölelerle evlilik dışı ilişkisini anlatır.","gloss":"evlilik ve cinsel birleşme","neighbor_only":"Evlilik veya cinsel birleşme eylemini doğrudan ve kimi zaman örtülü biçimde anlatır.","neighbor_ref":"root_000579/B002","relation_type":"same_field","shared_zone":"Her iki dal kadın ile erkek arasındaki cinsel ilişki bağlamında kullanılabilir."},{"boundary_match":"partial","distinction":"Odak dalın katılımcıları ve cinsel amacı söz öbeğiyle sabittir; komşu dal genel arama ve isteme eylemidir.","focus_only":"Arayışın hedefini kadınlarla ve amacını cinsel yakınlaşmayla sınırlar.","gloss":"bir şeyi tekrar tekrar aramak","neighbor_only":"Her tür nesneyi tekrar tekrar isteme ve aramayı amaç bakımından sınırsız biçimde kapsar.","neighbor_ref":"root_001377/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da bir hedefin peşinden gidip onu elde etmeye yönelik yinelenen arayış bulunabilir."},{"boundary_match":"thematic_only","distinction":"Odak dal erkek öznenin arayışıdır; komşu dal kadın öznenin işaret verme davranışı veya ona yakıştırılan niteliktir.","focus_only":"Kadınlara yönelen erkeğin peşlerinden gitmesini anlatır.","gloss":"cinsel çağrışımlı davranış","neighbor_only":"Bakış ve ağız hareketleriyle işaret veren kadını ve ona yüklenen cinsel niteliği anlatır.","neighbor_ref":"root_000599/B004","relation_type":"thematic","shared_zone":"İki dal kadın-erkek yakınlaşması ve evlilik dışı cinsel davranış senaryosunda yer alabilir."}],"source_phrase_ar":"فلان يتابع الإماء أي يزانيهن (ayn)؛ فلان تبع نساء أي يتبعهن؛ حدث نساء يحادثهن؛ وزير نساء يزورهن (tahdhib)","source_summary":"Kanıtlar, söz öbeklerini erkeğin kadınların peşinden cinsel amaçla gitmesi veya kadın kölelerle evlilik dışı ilişki kurması çevresinde toplar; konuşma ve ziyaret örnekleri kuruluş kalıbını açıklayan karşılaştırmalardır.","sources":["AY","TA"],"what_is_ar":"الرجل الذي يتبع النساء أو الإماء للمراودة أو الزنا كما نصت المصادر","what_is_not_ar":"ليس اتباع الأمر أو الاقتداء ولا التابعة من الجن"},"support_links":[]},{"boundary":"Bütün kullanımlar belirli biçim ve söz öbeklerine bağlıdır; zamansal peş peşelik bu dalın kurucu anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000175/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَتْبَعَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>atobaEa|ROOT:tbE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"18:85:1:2","qac_word_ref":"18:85:1","surface_ar":"أَتْبَعَ"}],"gloss":"sağlamlaştırmak, uyumlu olmak veya iyi duruma getirmek","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işi gereğini bilerek sağlam, eksiksiz ve ustaca yapmak."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sözü sağlam kurmak veya anlatıyı beceriyle ve bağlantılı biçimde sürdürmek."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir hayvanın beden yapısının düzgün ve parçalarının birbiriyle orantılı olması."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bilginin bölümlerinin birbirine uyması ve aralarında tutarsızlık bulunmaması."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"İyi otlağın hayvanları besleyip semirtmesi ve görünüşlerini iyileştirmesi."}}],"root_ar":"ت ب ع","root_id":"root_000175","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İş ve sözün iyi kurulmasını, parçaların tutarlılığını ve dış bir etkenle gelişmeyi birlikte gösteren açıklayıcı üst karşılıktır.","boundary_detail":"Bütün kullanımlar belirli biçim ve söz öbeklerine bağlıdır; zamansal peş peşelik bu dalın kurucu anlamı değildir.","branch_image_ar":"الإحكام والتناسب","concept_gloss":"sağlamlaştırmak, uyumlu olmak veya iyi duruma getirmek","contextual_glosses":[{"applicability":"Bir kişinin yaptığı işi iyi bilerek eksiksiz ve sağlam biçimde tamamlaması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Söz, beden yapısı, bilgi tutarlılığı ve otlağın hayvana etkisi yüzlerini dışarıda bırakır.","preserves":"İşi iyi bilme, sağlamlaştırma ve ustaca tamamlama yönünü korur."},"facet_ids":["F001"],"text":"işini sağlam ve ustaca yapmak","usage_role":"contextual"},{"applicability":"Beden bölümlerinin uyumu veya bilgi parçalarının birbirini doğrulaması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İşi veya sözü ustaca yapmayı ve otlağın hayvanı geliştirmesini dışarıda bırakır.","preserves":"Bir bütünün parçaları arasında uyum ve tutarsızlık bulunmaması yönünü korur."},"facet_ids":["F003","F004"],"text":"kendi içinde tutarlı olmak","usage_role":"contextual"},{"applicability":"Otlak ve beslenmenin sürüyü semirtip görünüşünü iyileştirdiği özel söz öbeğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İş, söz, beden yapısı ve bilgi tutarlılığı kullanımlarını dışarıda bırakır.","preserves":"Dış etken olan otlağın hayvanları semirtip iyi duruma getirmesini korur."},"facet_ids":["F005"],"text":"hayvanları besleyip güzelleştirmek","usage_role":"contextual"}],"definition":"Verilen biçim ve söz öbeklerinde bir işi veya sözü sağlam ve iyi kurmak, bir bütünün parçalarının düzgün ve tutarlı olması ya da bir etkenin canlıları iyi duruma getirmesi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işi gereğini bilerek sağlam, eksiksiz ve ustaca yapmak."},{"facet_id":"F002","role":"specialization","statement":"Sözü sağlam kurmak veya anlatıyı beceriyle ve bağlantılı biçimde sürdürmek."},{"facet_id":"F003","role":"extension","statement":"Bir hayvanın beden yapısının düzgün ve parçalarının birbiriyle orantılı olması."},{"facet_id":"F004","role":"extension","statement":"Bilginin bölümlerinin birbirine uyması ve aralarında tutarsızlık bulunmaması."},{"facet_id":"F005","role":"associated_use","statement":"İyi otlağın hayvanları besleyip semirtmesi ve görünüşlerini iyileştirmesi."}],"identity_rationale":"Kaynak ifadesi yalnızca işin ustaca yapılmasını değil, sözün sağlam kurulmasını, beden yapısının düzgünlüğünü, bilginin kendi içinde tutarlı olmasını ve iyi otlağın hayvanları semirtip güzelleştirmesini de içerir. Dal korunabilir, ancak tek bir ustalık anlamı yerine yapma, uyum ve iyi duruma getirme yüzleri açıkça ayrılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"işini sağlam ve ustaca yapmak"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"sözünü sağlam kurmak veya anlatıyı ustaca sürdürmek"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"beden yapısı düzgün ve orantılı"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"bilgisi kendi içinde tutarlı"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"otlak hayvanları besleyip semirtmek ve güzelleştirmek"}],"lexicalization_note":"İş, söz, beden yapısı, bilgi ve otlakla kurulan biçim ve söz öbekleri ayrı yüzler olarak tanımlanır; bunlardan yalın bir kök anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen beş ilişki ustalık, genel sağlam yapma, sözde sıkılık, parça orantısı ve zamansal ardışıklıkla en önemli sınırları kurar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli söz öbeklerinde bilgi, söz ve otlak etkisine uzanır; komşu dal genel yapım kalitesi ve yaratılış sağlamlığını merkez alır.","focus_only":"Bilgide iç tutarlılığı, sözün sağlam kuruluşunu ve otlağın hayvanı geliştirmesini de kapsar.","gloss":"iyi ve sağlam yapmak","neighbor_only":"Bir şeyin yaratılış veya yapılış bakımından güçlü ve iyi yapılmış olmasını daha genel biçimde anlatır.","neighbor_ref":"root_000290/B001","relation_type":"near_synonym","shared_zone":"Her iki dal işi sağlam ve ustaca yapmayı, ayrıca hayvan yapısındaki düzgünlük ve gücü anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalın çoklu söz öbekleri uyum ve iyi duruma gelme yönleri taşır; komşu dal kişinin ustalığı ve becerisi üzerinde yoğunlaşır.","focus_only":"Parçaların orantısını, bilginin tutarlılığını ve otlağın geliştirici etkisini içerir.","gloss":"işte ustalık ve sağlamlık","neighbor_only":"Beceriyi iş, konuşma, hazır cevaplılık ve iyi atış gibi ustalık göstergelerine genişletir.","neighbor_ref":"root_000184/B001","relation_type":"near_synonym","shared_zone":"İki dalda da işi iyi bilerek sağlam ve becerikli biçimde yapma anlamı vardır."},{"boundary_match":"partial","distinction":"Odak dal daha çeşitli bağlı yapılara dağılır; komşu dal dokuma ve sözde sıkılık ile doğrulama yönünü belirginleştirir.","focus_only":"Beden, bilgi ve otlak etkisi alanlarında da uyum veya iyileşme anlatır.","gloss":"söz veya dokumayı sağlam kurmak","neighbor_only":"Özellikle dokumanın sıkı, sözün ağırbaşlı ve bir şeyin doğrulanmış olmasını kapsar.","neighbor_ref":"root_000347/B010","relation_type":"near_synonym","shared_zone":"İki dal sözün sağlam ve tutarlı kurulması ile bir işin iyice yapılması alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal genel beden yapısı ve başka kalite alanlarını kapsar; komşu dal yüz güzelliğindeki parçalar arası dengeye özgüdür.","focus_only":"Orantıyı hayvanın bütün beden yapısına uygular ve ayrıca iş, söz ve bilgi alanlarına uzanır.","gloss":"güzellikte orantı","neighbor_only":"Özellikle yüzün güzel bölümlerinin birbirine denk düşmesini anlatır.","neighbor_ref":"root_001511/B009","relation_type":"near_synonym","shared_zone":"Her iki dalda bir bütünün parçalarının ölçülü ve birbirine uygun olması vardır."},{"boundary_match":"partial","distinction":"Odak dal kalite, tutarlılık ve uyum eksenindedir; komşu dal yalnız zamansal sıra ve kesintisiz devam eksenindedir.","focus_only":"İşi veya sözü sağlam kurmayı ve parçaların nitelikçe uyumlu olmasını anlatır.","gloss":"sağlam kurmak ile peş peşe getirmek","neighbor_only":"Eylem veya söz bölümlerini zaman bakımından aralıksız biçimde peş peşe getirir.","neighbor_ref":"root_000175/B004","relation_type":"near_neighbor","shared_zone":"İki dal aynı biçimlerin iş ve söz bağlamlarındaki farklı kullanımlarını içerir."}],"source_phrase_ar":"تابع الرجل عمله أي أتقنه وأحكمه (sihah)؛ تابعنا الأعمال أي أحكمناها وعرفناها؛ تابع فلان كلامه؛ فرس متتابع الخلق أي مستو؛ متتابع العلم إذا كان علمه يشاكل بعضه بعضا؛ تابع المرتع المال فتتابعت (tahdhib)","source_summary":"Toplu kanıt, işi ve sözü sağlam kurma kullanımlarını; beden yapısında oran, bilgide iç tutarlılık ve otlağın hayvanları iyi duruma getirmesiyle yan yana verir. Bu yüzler kalite ve uygunluk çevresinde bağlanabilse de kendi söz öbeklerine bağlı kalır.","sources":["SI","TA"],"what_is_ar":"إتقان العمل أو الكلام وإحكامه؛ استواء الخلق أو تشاكل العلم أو حسن المال بالمرتع","what_is_not_ar":"ليس مجرد توالي الأفعال بلا مهلة ولا اتباع شخص لشخص"},"support_links":[]},{"boundary":"Dal fiziksel kesmeyi ve bundan türeyen bağ koparmayı kapsar; sövme, ip, araç veya ince kumaş anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000664/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَبَب","morph_features":"STEM|POS:N|LEM:sabab|ROOT:sbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:85:2:1","qac_word_ref":"18:85:2","surface_ar":"سَبَبًا"}],"gloss":"kesme ve bağı koparma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel işlem, bir şeyi kesmek veya kesilmiş duruma getirmektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvan söz konusu olduğunda arka bacaklarını keserek onu yere düşürmeyi bildirir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Akrabalık bağını koparma ve iki tarafın birbirinden karşılıklı olarak kopması ilişkisel uzantılardır."}}],"root_ar":"س ب ب","root_id":"root_000664","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel kesme çekirdeğini ve bunun ilişki bağlarını sona erdiren uzantısını birlikte temsil eder.","boundary_detail":"Dal fiziksel kesmeyi ve bundan türeyen bağ koparmayı kapsar; sövme, ip, araç veya ince kumaş anlamlarını kapsamaz.","branch_image_ar":"القَطْع والعَقْر","concept_gloss":"kesme ve bağı koparma","contextual_glosses":[{"applicability":"Bir nesnenin fiziksel olarak kesilmesini anlatan yalın bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Fiziksel kesme işlemini eksiksiz biçimde korur."},"facet_ids":["F001"],"text":"kesmek","usage_role":"general"},{"applicability":"Aile veya akrabalık ilişkisinin bilerek kesildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İlişkisel bağın sona erdirilmesini açıkça korur."},"facet_ids":["F003"],"text":"akrabalık bağını koparmak","usage_role":"contextual"}],"definition":"Bir şeyi kesmek ya da kesilmiş duruma getirmektir. Hayvanın arka bacaklarını kesip yere düşürme ile akrabalık veya karşılıklı ilişki bağını koparma, bu çekirdeğin özel uzantılarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel işlem, bir şeyi kesmek veya kesilmiş duruma getirmektir."},{"facet_id":"F002","role":"specialization","statement":"Hayvan söz konusu olduğunda arka bacaklarını keserek onu yere düşürmeyi bildirir."},{"facet_id":"F003","role":"extension","statement":"Akrabalık bağını koparma ve iki tarafın birbirinden karşılıklı olarak kopması ilişkisel uzantılardır."}],"identity_rationale":"Kaynak ibaresi kesmeyi temel anlam olarak verir; hayvanın arka bacaklarını keserek yere düşürme, akrabalık bağını koparma ve karşılıklı ilişki kesme kullanımları da bu çekirdeğin özel gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kesmek veya kesilmiş duruma getirmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"dişi devenin arka bacaklarını kesip onu yere düşürmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"karşılıklı olarak ilişkiyi kesmek"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"akrabalık bağını koparmak"}],"lexicalization_note":"Tanım, yalın kesme çekirdeği ile hayvana, karşılıklılığa ve akrabalığa bağlı özel kullanımları birbirine karıştırmadan ayırır.","neighbor_coverage_note":"Önerilen bütün komşular gözden geçirildi; eşsesli dallar ve daha uzak kesme türleri elendi, sınırı en iyi açıklayan karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kesme çekirdeği belirli hayvan ve akrabalık kullanımlarıyla uzmanlaşırken komşu dal daha genel nesne kesilmesi ve kesintiye uğramayı kapsar.","focus_only":"Odak dal, hayvanın arka bacaklarını kesme ve akrabalık bağını koparma gibi özel gerçekleşmeleri de taşır.","gloss":"kesme ve ayrılma","neighbor_only":"Komşu dal, ipi, salkımı ve sözü kesme gibi daha geniş nesne ve söylem alanlarına yayılır.","neighbor_ref":"root_000861/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak alanı, bir bütünü keserek ayırma veya bağlantıyı sona erdirme işlemidir."}],"source_phrase_ar":"أصل هذا الباب القطع؛ السب العقر (maqayis)؛ أصل السب القطع (jamhara)؛ سبه أيضا بمعنى قطعه؛ التساب التقاطع (sihah)؛ السب القطع؛ سبسب إذا قطع رحمه (tahdhib)","source_summary":"Kaynaklar kesme çekirdeğinde birleşir; hayvanı arka bacaklarından yaralama, akrabalık bağını koparma ve karşılıklı kopuş bu çekirdeğe bağlanır.","sources":["MQ","JA","SI","TA"],"what_is_ar":"يدخل فيه القطع والعقر وقطع الرحم والتقاطع","what_is_not_ar":"ليس الحبل ولا الوسيلة ولا الثوب الرقيق"},"support_links":[]},{"boundary":"Dal sözlü aşağılama ve bundan doğan ayıp alanındadır; fiziksel kesme, ip, yol veya beden bölgesi anlamında değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000664/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَبَب","morph_features":"STEM|POS:N|LEM:sabab|ROOT:sbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:85:2:1","qac_word_ref":"18:85:2","surface_ar":"سَبَبًا"}],"gloss":"ağır sözlerle aşağılama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel eylem, ağır sözlerle bir kişiyi aşağılamak ve onuruna saldırmaktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylemin karşılıklı yapılması, iki tarafın birbirine sövüşmesini bildirir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sövmenin konusu olan ayıp ile çok söven veya çok sövülen kişi de aynı anlam alanında adlandırılır."}}],"root_ar":"س ب ب","root_id":"root_000664","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sövme eyleminin incitici söz ve onura saldırıdan oluşan çekirdeğini temsil eder.","boundary_detail":"Dal sözlü aşağılama ve bundan doğan ayıp alanındadır; fiziksel kesme, ip, yol veya beden bölgesi anlamında değildir.","branch_image_ar":"الشَّتْم والسِّباب","concept_gloss":"ağır sözlerle aşağılama","contextual_glosses":[{"applicability":"Bir kişinin ağır ve aşağılayıcı sözlerle hedef alındığı genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözlü aşağılama eylemini doğal Türkçeyle korur."},"facet_ids":["F001"],"text":"sövmek","usage_role":"general"},{"applicability":"İki tarafın birbirine ağır sözler söylediği karşılıklı eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemin karşılıklı oluşunu ve sövme niteliğini korur."},"facet_ids":["F002"],"text":"karşılıklı sövüşmek","usage_role":"contextual"}],"definition":"Bir kişiye ağır ve incitici sözler söyleyerek onu aşağılamak ve onuruna saldırmaktır. Karşılıklı sövüşme, çok söven ya da çok sövülen kişi ve sövmeye dayanak olan ayıp bu çekirdeğe bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel eylem, ağır sözlerle bir kişiyi aşağılamak ve onuruna saldırmaktır."},{"facet_id":"F002","role":"extension","statement":"Eylemin karşılıklı yapılması, iki tarafın birbirine sövüşmesini bildirir."},{"facet_id":"F003","role":"associated_use","statement":"Sövmenin konusu olan ayıp ile çok söven veya çok sövülen kişi de aynı anlam alanında adlandırılır."}],"identity_rationale":"Kaynak ibaresi doğrudan sövme ve onura sözle saldırma anlamını verir; karşılıklı sövüşme, insanı ayıplatan kusur ve söven ya da sövülen kişi adları bu çekirdeğe bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"sövmek ve onuruna saldırmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"karşılıklı sövüşmek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"insanlara çok söven kimse"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"çok sövülen veya çok söven adam"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kişinin yüzüne vurulan ayıp"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"insanların birbirine söverken kullandığı konu"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"çok çirkin biçimde sövmek"}],"lexicalization_note":"Tanım, sövme çekirdeği ile karşılıklı eylem, kişi nitelemesi ve ayıp adı olan türev kullanımları ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı kökün eşsesli dalları ile yalnız kavga veya teşhir alanını paylaşan uzak adaylar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın merkezi doğrudan sövme ve onura saldırıdır; komşu dal ise kötü söz işittirmeyi kamu önünde kınama ve rezil etmeye doğru genişletir.","focus_only":"Odak dal karşılıklı sövüşmeyi, sövmeye konu olan ayıbı ve söven ya da sövülen kişiyi de kapsar.","gloss":"sövme ve kötü söz işittirme","neighbor_only":"Komşu dal kötü söz işittirmenin yanında kınama, rezil etme ve adını kötüye çıkarma yönlerine de uzanır.","neighbor_ref":"root_000741/B006","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir kişiyi incitici ve aşağılayıcı sözlerle hedef alma vardır."}],"source_phrase_ar":"السب الشتم (maqayis)؛ سبه فلان سبا (ayn)؛ صار السب شتما لأن السب خرق الأعراض (jamhara)؛ السب الشتم؛ التساب التشاتم؛ السبة العار (sihah)؛ السب مصدر سببته سبا؛ عير بالبخل (tahdhib)؛ السب الشتم الوجيع؛ السبة ما يسب (mufradat)","source_summary":"Kaynaklar sövme ve onur kırmada birleşir; karşılıklı sövüşme, ayıp ve eyleme katılan kişileri adlandıran türevler de bu alanı tamamlar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الشتم والسباب والتساب والتعيير والعار الذي يسب به","what_is_not_ar":"ليس العقر ولا الحبل ولا الطريق"},"support_links":[]},{"boundary":"Dal hem somut ipi hem de bir hedefe ulaştıran bağ, yol veya aracı kapsar; sövme ve kesme anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000664/B003","candidate_links":[{"candidate_id":"cand_6b15bf64ee4f971204a8","lane":"micro"},{"candidate_id":"cand_ae5760fdf2c2a2b0b410","lane":"micro"},{"candidate_id":"cand_b3aef8fe101822c7bec7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَبَب","morph_features":"STEM|POS:N|LEM:sabab|ROOT:sbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:85:2:1","qac_word_ref":"18:85:2","surface_ar":"سَبَبًا"}],"gloss":"ulaştıran bağ veya araç","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Somut çekirdek, erişmek veya hareket etmek için tutunulan uzun iptir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Herhangi bir hedefe ulaştıran yol, araç veya dayanak soyut erişim uzantısıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Akrabalık, iyilik, inanç ve sevgi gibi insanlar arasında bağlantı kuran ilişkiler özel bağ türleridir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Göğün yönleri, katları veya girişleri, erişilecek yerler olarak aynı bağlantı tasarımıyla adlandırılır."}}],"root_ar":"س ب ب","root_id":"root_000664","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Somut ipten soyut ilişki ve yola kadar, bir şeyi başka bir şeye ulaştıran ortak işlevi temsil eder.","boundary_detail":"Dal hem somut ipi hem de bir hedefe ulaştıran bağ, yol veya aracı kapsar; sövme ve kesme anlamlarını kapsamaz.","branch_image_ar":"السَّبَب حبل ووصلة","concept_gloss":"ulaştıran bağ veya araç","contextual_glosses":[{"applicability":"Tırmanma, inme veya başka bir yere ulaşma için kullanılan somut ip bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Somut ipi ve onun erişim işlevini birlikte korur."},"facet_ids":["F001"],"text":"erişim ipi","usage_role":"contextual"},{"applicability":"Bir amaca varmayı mümkün kılan soyut araç, yöntem veya bağlantı bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir hedefe eriştiren araçsal ilişkiyi açıkça korur."},"facet_ids":["F002","F003"],"text":"ulaştıran yol veya dayanak","usage_role":"explanatory"}],"definition":"Somut olarak tırmanmayı, inmeyi veya erişmeyi sağlayan uzun bir iptir. Soyut olarak da kişiyi başka bir şeye ya da amaca ulaştıran bağ, ilişki, yol veya araçtır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Somut çekirdek, erişmek veya hareket etmek için tutunulan uzun iptir."},{"facet_id":"F002","role":"extension","statement":"Herhangi bir hedefe ulaştıran yol, araç veya dayanak soyut erişim uzantısıdır."},{"facet_id":"F003","role":"specialization","statement":"Akrabalık, iyilik, inanç ve sevgi gibi insanlar arasında bağlantı kuran ilişkiler özel bağ türleridir."},{"facet_id":"F004","role":"associated_use","statement":"Göğün yönleri, katları veya girişleri, erişilecek yerler olarak aynı bağlantı tasarımıyla adlandırılır."}],"identity_rationale":"Kaynak ibaresi somut çekirdeği uzun bir ip olarak verir ve ardından akrabalık, iyilik, inanç, sevgi, yol, kapı ve başka bir şeye ulaştıran her türlü bağı aynı eriştirme ilişkisi altında toplar.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"erişmek, tırmanmak veya inmek için kullanılan ip"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"başka bir şeye ulaştıran araç veya bağ"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"akrabalık, soy veya inanç bağı"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"istenen yere ulaştıran yol"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"göğün yönleri, katları veya girişleri"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir şeyi başka bir şeye ulaştıran araç kılma"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ip"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"ipler"}],"lexicalization_note":"Tanım, somut ip çekirdeğini yol, akrabalık ve erişim yapılarıyla bağlı uzantılardan ayırır; özel yapıları yalın anlama dönüştürmez.","neighbor_coverage_note":"Tüm komşu önerileri incelendi; salt yakınlık, merdiven veya belirli ip parçaları yerine genel yol sınırını gösteren karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal eriştiren her türlü bağa ve somut ipe dayanır; komşu dal ise öncelikle üzerinde gidilen yol ve oradan türeyen yöntem anlamındadır.","focus_only":"Odak dal somut ipi ve akrabalık, iyilik, inanç veya sevgi gibi bağlantıları da içerir.","gloss":"ulaştıran bağ ile yol","neighbor_only":"Komşu dalın çekirdeği yürünür ve uzanan yoldur; ayrıca yöntem ve çare yönüne genişler.","neighbor_ref":"root_000672/B001","relation_type":"near_synonym","shared_zone":"İki dal da kişiyi bir yere veya amaca ulaştıran yol ve araç alanında örtüşür."}],"source_phrase_ar":"الحبل فالسبب؛ أصل آخر يدل على طول وامتداد (maqayis)؛ السبب الحبل؛ كل ما تسببت به من رحم أو يد أو دين؛ سبب الأمر الذي يوصل به؛ الطريق (ayn)؛ السب بلغة هذيل الحبل (jamhara)؛ السبب الحبل؛ كل شئ يتوصل به إلى غيره؛ اعتلاق قرابة؛ أسباب السماء نواحيها (sihah)؛ السبب الحبل؛ المودة؛ تواصلهم؛ المنازل؛ أبوابها؛ كل شيء يتوصل به إلى شيء (tahdhib)؛ السبب الحبل الذي يصعد به النخل؛ كل ما يتوصل به إلى شيء سببا؛ ذريعة يتوصل بها (mufradat)","source_summary":"Kaynaklar ip ile bir hedefe ulaştıran araç arasındaki ilişkiyi ortaklaştırır; yol, yakınlık, sevgi, inanç ve göğe erişim tasarımları bu genel bağ fikrini çeşitlendirir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحبل وما يتوصل به إلى غيره من رحم أو يد أو دين أو مودة أو طريق أو أبواب أو ذرائع","what_is_not_ar":"ليس الشتم ولا العقر ولا الأرض القفر"},"support_links":["sup_1ae51219a8d5550a7019","sup_beb64ee19cae5bb28311","sup_c1184877ef47aceeaea3"]},{"boundary":"Dal ince kumaş, başörtüsü ve sarık türleriyle sınırlıdır; ip, erişim aracı veya sövme anlamına geçmez.","branch_kind":"bare","branch_ref":"root_000664/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَبَب","morph_features":"STEM|POS:N|LEM:sabab|ROOT:sbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:85:2:1","qac_word_ref":"18:85:2","surface_ar":"سَبَبًا"}],"gloss":"ince örtü veya kumaş parçası","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başörtüsü veya sarık olarak kullanılan örtü, dalın temel nesnesidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnce ve uzun kumaş parçası, özellikle ince keten dokuma, aynı nesne türünün özel biçimidir."}}],"root_ar":"س ب ب","root_id":"root_000664","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Başörtüsü, sarık ve ince uzun dokuma biçimlerini kapsayan nesne sınıfını temsil eder.","boundary_detail":"Dal ince kumaş, başörtüsü ve sarık türleriyle sınırlıdır; ip, erişim aracı veya sövme anlamına geçmez.","branch_image_ar":"السَّبّ ثوب رقيق وخمار","concept_gloss":"ince örtü veya kumaş parçası","contextual_glosses":[{"applicability":"Kumaşın başı örtme ya da başa sarılma işlevinin öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Baş örtme ve sarık olma işlevlerini korur."},"facet_ids":["F001"],"text":"başörtüsü veya sarık","usage_role":"contextual"},{"applicability":"Malzemenin ve ince dokumanın özellikle belirtildiği kumaş bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnce dokumayı ve keten parça niteliğini korur."},"facet_ids":["F002"],"text":"ince keten parçası","usage_role":"contextual"}],"definition":"Başı örtmek veya sarık yapmak için kullanılan örtü ya da ince, uzun bir kumaş parçasıdır. İnce keten parça ve bu tür ince kumaşların çoğulu da aynı dalda yer alır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başörtüsü veya sarık olarak kullanılan örtü, dalın temel nesnesidir."},{"facet_id":"F002","role":"specialization","statement":"İnce ve uzun kumaş parçası, özellikle ince keten dokuma, aynı nesne türünün özel biçimidir."}],"identity_rationale":"Kaynak ibaresi başörtüsü, sarık, uzun veya ince kumaş parçası ve ince keten dokuma anlamlarını birlikte verir; dalın kumaş ve örtü çerçevesi bu içeriği doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"başörtüsü veya sarık"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"ince keten kumaş parçası"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"ince kumaşlar"}],"lexicalization_note":"Tanım yalnız bu yalın kumaş ve örtü anlamını kurar; başka dallardaki yapı bağımlı anlamları buraya taşımaz.","neighbor_coverage_note":"Bütün aday kumaş ve örtü dalları değerlendirildi; yalnız incelik ortaklığının sınırı en açık olan malzeme karşılaştırması yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal biçim ve örtme işlevine dayanır; komşu dalın ayırıcı özelliği ise ipek malzemedir.","focus_only":"Odak dal başörtüsü, sarık ve keten gibi ince kumaş parçalarını işlevleriyle birlikte kapsar.","gloss":"ince kumaş türleri","neighbor_only":"Komşu dal kumaşı ipek oluşuna göre tanımlar ve başı örtme ya da sarık işlevini gerektirmez.","neighbor_ref":"root_000306/B010","relation_type":"near_neighbor","shared_zone":"Her iki dal da ince dokunmuş giysi veya kumaş alanında buluşur."}],"source_phrase_ar":"السب الخمار (maqayis)؛ السب الثوب الرقيق؛ السبيبة (ayn)؛ السب الشقة البيضاء من الثياب؛ العمامة؛ السبيبة (jamhara)؛ السب الخمار؛ العمامة؛ شقة كتان رقيقة؛ السبيبة (sihah)؛ السب الخمار؛ السبوب الثياب الرقاق؛ السبائب؛ السب العمامة (tahdhib)؛ سمي العمامة والخمار والثوب الطويل سببا (mufradat)","source_summary":"Kaynaklar başörtüsü ve sarık ile ince kumaş parçasını aynı nesne alanında birleştirir; incelik, uzunluk ve keten oluş bazı anlatımlarda belirginleşir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الخمار والعمامة والشقة الرقيقة والسبيبة والسبائب","what_is_not_ar":"ليس الحبل ولا الوسيلة ولا الشتم"},"support_links":[]},{"boundary":"Anlam yalnız zaman bildiren yerleşik yapıda geçerlidir; yalın biçime genel bir süre anlamı yüklenemez.","branch_kind":"collocation","branch_ref":"root_000664/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَبَب","morph_features":"STEM|POS:N|LEM:sabab|ROOT:sbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:85:2:1","qac_word_ref":"18:85:2","surface_ar":"سَبَبًا"}],"gloss":"uzunca bir zaman dilimi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yerleşik zaman yapısında, daha büyük bir süreden ayrılan zaman dilimini bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Soğuk gibi belirli bir durumun sürdüğü dönem, zaman dilimi anlamının bağlamsal uzantısıdır."}}],"root_ar":"س ب ب","root_id":"root_000664","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız bildirilen zaman yapısında, daha büyük bir süreden ayrılan dönemi karşılar.","boundary_detail":"Anlam yalnız zaman bildiren yerleşik yapıda geçerlidir; yalın biçime genel bir süre anlamı yüklenemez.","branch_image_ar":"سُبَّة من الدهر","concept_gloss":"uzunca bir zaman dilimi","contextual_glosses":[{"applicability":"Bir olaydan bu yana belirli fakat kesin ölçülmemiş bir zaman geçtiğini anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geçmiş zaman parçasını doğal bir anlatımla korur."},"facet_ids":["F001"],"text":"bir süredir","usage_role":"contextual"},{"applicability":"Sürenin soğuk hava gibi belirli bir durumla tanımlandığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Durumla nitelenen dönem anlamını açıkça korur."},"facet_ids":["F002"],"text":"bir soğuk dönemi","usage_role":"contextual"}],"definition":"Bildirilen zaman yapısı içinde, geçmişten veya yaşam süresinden ayrılan uzunca bir zaman dilimini anlatır. Soğuk gibi belirgin bir durumun sürdüğü dönem de aynı ölçülü zaman kullanımıyla ifade edilebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yerleşik zaman yapısında, daha büyük bir süreden ayrılan zaman dilimini bildirir."},{"facet_id":"F002","role":"extension","statement":"Soğuk gibi belirli bir durumun sürdüğü dönem, zaman dilimi anlamının bağlamsal uzantısıdır."}],"identity_rationale":"Kaynak ibaresi bir zaman parçasını ve uzunca süreyi açıkça destekler; ayrıca değişen dönemler ve soğukla belirlenen bir süre örneği verir. Bu nedenle dal yalnız belirsiz bir zaman parçası değil, belirli bir durumla nitelenebilen dönem olarak sınırlandırılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"geçmişten ayrılan uzunca bir zaman dilimi"}],"lexicalization_note":"Tanım, anlamı bildirilen zaman yapısına açıkça bağlar ve bu yapıdan bağımsız yalın bir zaman anlamı çıkarmaz.","neighbor_coverage_note":"Bütün zaman komşuları incelendi; yıl, uzun gece ve kalıplaşmış an anlatımları yerine genel zaman sınırını gösteren aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yapı bağımlı ve parça niteliğinde bir süredir; komşu dal ise yapı bağı olmadan hem anı hem daha geniş dönemi karşılayan genel zaman adıdır.","focus_only":"Odak dal yalnız belirli bir zaman yapısında geçen, daha büyük süreden ayrılmış dönem anlamıdır.","gloss":"zaman dilimi ile genel vakit","neighbor_only":"Komşu dal genel olarak vakti, anı, dönemi ve bir şeyin uygun zamanını adlandırabilir.","neighbor_ref":"root_000382/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da sınırları kesin ölçülmemiş bir zaman kesitini ifade edebilir."}],"source_phrase_ar":"مضت سبة من الدهر يريد مضت قطعة منه (maqayis)؛ مضت سبة من الدهر وسنبة من الدهر أي ملاوة (jamhara)؛ ما رأيته منذ سبه أي منذ زمن من الدهر؛ مضت سبة من الدهر (sihah)؛ سبة من الدهر؛ الدهر سبات أي أحوال؛ أصابتنا سبة من برد (tahdhib)","source_summary":"Kaynaklar bunu geçmişten ayrılan bir süre veya zaman parçası olarak açıklar; dönemlerin değişmesi ve bir soğuk devresi bu zamanlama işlevini somutlaştırır.","sources":["MQ","JA","SI","TA"],"what_is_ar":"يدخل فيه القطعة من الدهر والبرهة والحال التي تدوم أياما","what_is_not_ar":"ليس الشتم ولا الدبر ولا الحبل"},"support_links":[]},{"boundary":"Dal belirli bir beden bölgesi ve ona yönelik yaralama yapısıyla sınırlıdır; genel ayıp veya sövme anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000664/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَبَب","morph_features":"STEM|POS:N|LEM:sabab|ROOT:sbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:85:2:1","qac_word_ref":"18:85:2","surface_ar":"سَبَبًا"}],"gloss":"arka çıkış bölgesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim, bedenin arka çıkış bölgesidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Beden bölgesinin adı, utanılan yeri doğrudan söylememek için örtmece işlevi görür."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli yapı içinde birini arka tarafından yaralama eylemini bildirir."}}],"root_ar":"س ب ب","root_id":"root_000664","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Beden bölgesini açıklar ve kaynaklardaki örtmeceli adlandırmanın gönderimini korur.","boundary_detail":"Dal belirli bir beden bölgesi ve ona yönelik yaralama yapısıyla sınırlıdır; genel ayıp veya sövme anlamı değildir.","branch_image_ar":"السُّبَة الدبر","concept_gloss":"arka çıkış bölgesi","contextual_glosses":[{"applicability":"Beden bölgesinin utanma gözetilerek örtmeceli biçimde anıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Örtmeceli anlatımı ve arka bölge gönderimini korur."},"facet_ids":["F001","F002"],"text":"arka taraf","usage_role":"contextual"},{"applicability":"Belirli yapıda yaralamanın bedenin arka bölgesine yöneldiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemi, yöneldiği beden bölgesiyle birlikte korur."},"facet_ids":["F003"],"text":"arka tarafından yaralamak","usage_role":"contextual"}],"definition":"Utanılan bir beden bölgesi olarak arka çıkış yerinin örtmeceli adıdır. Birini bu bölgeden yaralamayı anlatan özel yapı da bu beden anlamına dayanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim, bedenin arka çıkış bölgesidir."},{"facet_id":"F002","role":"associated_use","statement":"Beden bölgesinin adı, utanılan yeri doğrudan söylememek için örtmece işlevi görür."},{"facet_id":"F003","role":"specialization","statement":"Belirli yapı içinde birini arka tarafından yaralama eylemini bildirir."}],"identity_rationale":"Kaynak ibaresi bedenin arka çıkış bölgesini açıkça adlandırır, bunun utanılan bir yeri örtmeceyle söylemek için kullanıldığını belirtir ve o bölgeden yaralama yapısını ayrıca tanıklar.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"örtmeceyle anılan arka çıkış bölgesi"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"arka tarafından yaralamak"}],"lexicalization_note":"Tanım, beden bölgesini bildiren ad ile o bölgeden yaralamayı anlatan yapı bağımlı kullanımı ayrı düzeylerde tutar.","neighbor_coverage_note":"Bütün beden bölgesi adayları incelendi; kadın bedeniyle sınırlı ya da başka organlara ait komşular yerine en genel mahremiyet sınırı seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal anatomik olarak belirli bir arka bölgedir; komşu dal ise tek bir bölgeye bağlı olmayan daha geniş mahremiyet sınıfıdır.","focus_only":"Odak dal doğrudan arka çıkış bölgesine gönderir ve bu bölgeden yaralama yapısını da taşır.","gloss":"belirli arka bölge ile örtülmesi gereken yer","neighbor_only":"Komşu dal görünmesi ayıp sayılan bütün özel beden bölgelerini ve özel kalınan zamanları kapsayan daha geniş bir örtülülük alanıdır.","neighbor_ref":"root_001060/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da utanma nedeniyle örtülen veya doğrudan söylenmeyen beden bölgeleriyle ilgilidir."}],"source_phrase_ar":"السبة الدبر؛ طعنته في السبة (jamhara)؛ السبة الاست؛ طعنه في السبة (sihah)؛ السب الطبيجات؛ السبة وهي الدبر (tahdhib)؛ السبة ما يسب وكني بها عن الدبر (mufradat)","source_summary":"Kaynaklar bedenin arka çıkış bölgesinde birleşir; örtmece işlevi ve bu bölgeden yaralamayı bildiren kullanım aynı gönderime dayanır.","sources":["JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الدبر والكناية به وما يتصل بالطعن في السُّبَة","what_is_not_ar":"ليس العار المجرد ولا الشتم ولا الحبل"},"support_links":[]},{"boundary":"Dal yalnız alın, yele ve kuyrukta uzanan saç veya kılı kapsar; ip ya da ince kumaş değildir.","branch_kind":"bare","branch_ref":"root_000664/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَبَب","morph_features":"STEM|POS:N|LEM:sabab|ROOT:sbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:85:2:1","qac_word_ref":"18:85:2","surface_ar":"سَبَبًا"}],"gloss":"sarkan perçem, yele veya kuyruk kılı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel nesne, bir beden bölümünden uzayıp sarkan saç veya kıl topluluğudur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Alın perçemi, yele ve kuyruk kılları bu topluluğun belirtilen yerleridir."}}],"root_ar":"س ب ب","root_id":"root_000664","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Saç ya da kılın alın, yele ve kuyruktaki uzayan topluluklarını birlikte temsil eder.","boundary_detail":"Dal yalnız alın, yele ve kuyrukta uzanan saç veya kılı kapsar; ip ya da ince kumaş değildir.","branch_image_ar":"السَّبيب شعر متدل","concept_gloss":"sarkan perçem, yele veya kuyruk kılı","contextual_glosses":[{"applicability":"Saçın alın üzerinde uzanan veya sarkan bölümü anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alın bölgesindeki saç topluluğunu açıkça korur."},"facet_ids":["F001","F002"],"text":"alın perçemi","usage_role":"contextual"},{"applicability":"Hayvanın boynunda ya da kuyruğunda uzayan kıl topluluğu anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvandaki yele ve kuyruk kılı gönderimini korur."},"facet_ids":["F001","F002"],"text":"yele veya kuyruk kılı","usage_role":"contextual"}],"definition":"Alın perçeminde, yelede veya kuyrukta uzayıp sarkan saç ya da kıl topluluğudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel nesne, bir beden bölümünden uzayıp sarkan saç veya kıl topluluğudur."},{"facet_id":"F002","role":"specialization","statement":"Alın perçemi, yele ve kuyruk kılları bu topluluğun belirtilen yerleridir."}],"identity_rationale":"Kaynak ibaresi alın perçemi, yele ve kuyruk kıllarını birlikte sayar. Ortak özellik, baştan, boyundan veya kuyruktan uzayıp sarkan saç ya da kıl topluluğudur.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"alın perçemi, yele veya kuyruk kılı"}],"lexicalization_note":"Tanım yalın saç ve kıl adını verir; başka dallardaki kesme, ip veya kumaş anlamlarını içeri almaz.","neighbor_coverage_note":"Önerilen bütün saç, perçem ve beden yeri adayları değerlendirildi; en yakın perçem karşılaştırması dışındaki uzak ilişkiler elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın alanı yele ve kuyruğa kadar uzanır; komşu dal ise saç tutamı ve alın perçemi çevresinde kalır.","focus_only":"Odak dal alın perçemine ek olarak yele ve kuyruk kıllarını da kapsar.","gloss":"perçem ve uzayan kıl topluluğu","neighbor_only":"Komşu dal genel bir saç tutamını veya özellikle atın alın perçemini adlandırır.","neighbor_ref":"root_000995/B015","relation_type":"near_synonym","shared_zone":"Her iki dal alın üzerinde bulunan saç veya kıl tutamını adlandırabilir."}],"source_phrase_ar":"السبيب شعر الناصية والعرف والذنب (sihah)؛ السبيب شعر الذنب؛ شعر الناصية (tahdhib)","source_summary":"Kaynaklar alın perçemi, yele ve kuyrukta bulunan saç ya da kılı aynı ad altında toplar.","sources":["SI","TA"],"what_is_ar":"يدخل فيه شعر الناصية والعرف والذنب","what_is_not_ar":"ليس الحبل ولا الثوب الرقيق"},"support_links":[]},{"boundary":"Dal geniş ve çorak ıssız araziyi anlatır; bayram günü, yumuşak ilerleme veya asılsız sözler anlamında değildir.","branch_kind":"bare","branch_ref":"root_000664/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَبَب","morph_features":"STEM|POS:N|LEM:sabab|ROOT:sbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:85:2:1","qac_word_ref":"18:85:2","surface_ar":"سَبَبًا"}],"gloss":"geniş ve çorak ıssız arazi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim, geniş ve ıssız bir açık arazi parçasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Uzaklık, çoraklık, susuzluk ve insansızlık arazinin belirgin nitelikleridir."}}],"root_ar":"س ب ب","root_id":"root_000664","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genişlik, uzaklık ve yaşam kaynaklarının yokluğuyla nitelenen açık araziyi temsil eder.","boundary_detail":"Dal geniş ve çorak ıssız araziyi anlatır; bayram günü, yumuşak ilerleme veya asılsız sözler anlamında değildir.","branch_image_ar":"السَّبْسَب أرض قفر","concept_gloss":"geniş ve çorak ıssız arazi","contextual_glosses":[{"applicability":"Arazinin genişliği ve verimsizliği anlatımın önünde olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Genişlik ve çoraklık niteliklerini birlikte korur."},"facet_ids":["F001","F002"],"text":"uçsuz bucaksız çoraklık","usage_role":"contextual"},{"applicability":"Su ve insan bulunmamasının özellikle vurgulandığı yolculuk bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Susuzluk ve ıssızlık özelliklerini açıkça korur."},"facet_ids":["F001","F002"],"text":"susuz ıssız arazi","usage_role":"contextual"}],"definition":"Geniş, uzak, çorak ve çoğu zaman su ile insan bulunmayan ıssız arazidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim, geniş ve ıssız bir açık arazi parçasıdır."},{"facet_id":"F002","role":"specialization","statement":"Uzaklık, çoraklık, susuzluk ve insansızlık arazinin belirgin nitelikleridir."}],"identity_rationale":"Kaynak ibaresi geniş ıssız araziyi, uzak çorak toprağı ve kurak boş alanı aynı yerde toplar. Dalın geniş, uzak ve yaşama elverişsiz arazi çerçevesi bu tanıklığa uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"geniş, uzak ve çorak ıssız arazi"}],"lexicalization_note":"Tanım yalnız yalın arazi anlamını kurar ve benzer sesli gün, hareket veya söz anlamlarını buraya taşımaz.","neighbor_coverage_note":"Bütün çöl ve boş arazi adayları incelendi; düz zemin, genel kır ve ölümcül geçit gibi ek çekirdekleri olanlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal susuzluk özelliğiyle daha dar tanımlanır; odak dal ise geniş ve uzak çorak arazi görünümünü daha kapsamlı biçimde taşır.","focus_only":"Odak dal susuzluğun yanında genişlik, uzaklık, çoraklık ve insansızlığı da belirginleştirir.","gloss":"susuz ve geniş ıssız arazi","neighbor_only":null,"neighbor_ref":"root_001614/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da su bulunmayan, geçilmesi güç ıssız araziyi adlandırır."}],"source_phrase_ar":"السبسب المفازة الواسعة (maqayis)؛ السبسب المفازة (ayn)؛ السبسب المفازة؛ بلد سبسب (sihah)؛ السبسب الأرض القفر البعيدة؛ القفار؛ الأرض الشأسبة الجدبة (tahdhib)","source_summary":"Kaynaklar geniş ıssız arazi anlamında birleşir; uzaklık, çoraklık ve kuraklık bu arazinin ayırıcı nitelikleri olarak belirtilir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه المفازة الواسعة والأرض القفر البعيدة التي لا ماء بها ولا أنيس","what_is_not_ar":"ليس يوم السَّباسِب ولا السير اللين ولا البسابس للأباطيل"},"support_links":[]},{"boundary":"Dal belirli bir bayram günü adıyla sınırlıdır; aynı ses yapısındaki çorak arazi veya başka kök anlamlarına bağlanamaz.","branch_kind":"non_bare","branch_ref":"root_000664/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَبَب","morph_features":"STEM|POS:N|LEM:sabab|ROOT:sbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:85:2:1","qac_word_ref":"18:85:2","surface_ar":"سَبَبًا"}],"gloss":"Hristiyanlara ait belirli bir bayram günü","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim, bir Hristiyan topluluğunca kutlanan belirli bir bayram günüdür."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir açıklama günü Dallar Bayramı olarak belirlerken diğerleri yalnız genel bayram kimliğini verir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Adın hangi kökten türediği kaynak anlatımında kesinleştirilmemiştir."}}],"root_ar":"س ب ب","root_id":"root_000664","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynakların ortak bayram günü tanımını korur, daha özel gün eşlemesini zorunlu kılmaz.","boundary_detail":"Dal belirli bir bayram günü adıyla sınırlıdır; aynı ses yapısındaki çorak arazi veya başka kök anlamlarına bağlanamaz.","branch_image_ar":"يوم السَّباسِب","concept_gloss":"Hristiyanlara ait belirli bir bayram günü","contextual_glosses":[{"applicability":"Günün daha özel olarak hurma veya başka ağaç dallarıyla kutlanan pazar günüyle eşlendiği tanıklıkta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kaynakta verilen özel bayram günü eşlemesini korur."},"facet_ids":["F001","F002"],"text":"Dallar Bayramı günü","usage_role":"contextual"}],"definition":"Bir Hristiyan topluluğuna ait bayram gününün adıdır. Kaynakların birinde Dallar Bayramı günüyle özdeşleştirilir; diğer tanıklıklar yalnız bayram olduğunu bildirir ve adın kökenini kesinleştirmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim, bir Hristiyan topluluğunca kutlanan belirli bir bayram günüdür."},{"facet_id":"F002","role":"source_variant","statement":"Bir açıklama günü Dallar Bayramı olarak belirlerken diğerleri yalnız genel bayram kimliğini verir."},{"facet_id":"F003","role":"associated_use","statement":"Adın hangi kökten türediği kaynak anlatımında kesinleştirilmemiştir."}],"identity_rationale":"Kaynak ibareleri bunun bir topluluğa ait bayram günü olduğunda birleşir; yalnız bir tanıklık günü Dallar Bayramı olarak belirler, bir başka tanıklık ise adın kökenini bilinmez sayar. Bu nedenle özel gün kimliği kesin ve tek biçimliymiş gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"Hristiyanlara ait bayram günü; özellikle Dallar Bayramı"}],"lexicalization_note":"Tanım yalnız kaynaklarda verilen bayram günü adını açıklar; bu adın parçalarından yalın ve üretken bir gün anlamı çıkarmaz.","neighbor_coverage_note":"Bütün gün ve bayram adayları incelendi; hafta günleri, ay ve kurban adı gibi yalnız takvim alanını paylaşan daha uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Takvim alanı ortak olsa da odak dal Dallar Bayramı ile ilişkilendirilen gündür; komşu dal ise Paskalya'dır ve ikisi aynı gün değildir.","focus_only":"Odak dal bazı kaynaklarda Dallar Bayramı olarak açıklanan ayrı bir bayram günüdür.","gloss":"iki ayrı Hristiyan bayramı","neighbor_only":"Komşu dal Paskalya bayramını ve o bayramın gelişini adlandırır.","neighbor_ref":"root_001158/B005","relation_type":"same_field","shared_zone":"Her iki dal Hristiyan takvimindeki bir bayramı veya bayram gününü adlandırır."}],"source_phrase_ar":"السباسب فيوم عيد لهم ولا أدري مم اشتقاقه (maqayis)؛ يوم السباسب يوم السعانين (ayn)؛ يوم السباسب يعني به عيدا لهم (sihah)","source_summary":"Ortak nokta bunun bir topluluğun bayram günü olmasıdır; daha özel açıklama günü Dallar Bayramı ile eşlerken adın kökeni belirsiz bırakılır.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه اليوم المسمى السَّباسِب أو يوم السعانين","what_is_not_ar":"ليس السَّبْسَب المفازة ولا الشتم"},"support_links":[]},{"boundary":"Dal yalnız seçkin develere yönelik övgü niteliğidir; başka hayvanlara genellenmez ve ip ya da sövme anlamıyla birleştirilmez.","branch_kind":"non_bare","branch_ref":"root_000664/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَبَب","morph_features":"STEM|POS:N|LEM:sabab|ROOT:sbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:85:2:1","qac_word_ref":"18:85:2","surface_ar":"سَبَبًا"}],"gloss":"övgüyle seçkin sayılan develer","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim, iyi ve seçkin sayılan develerin övgüyle nitelenmesidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Niteleme, develere bakınca onların değerini ve güzelliğini dile getiren hayranlık sözüyle açıklanır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Karınlarının toplu ve düzgün görünmesi, övülen develere verilen betimleyici ayrıntıdır."}}],"root_ar":"س ب ب","root_id":"root_000664","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kayıtlı deve nitelemesinde kaliteyi ve hayranlığı birlikte temsil eder.","boundary_detail":"Dal yalnız seçkin develere yönelik övgü niteliğidir; başka hayvanlara genellenmez ve ip ya da sövme anlamıyla birleştirilmez.","branch_image_ar":"إبل مُسَبَّبة ممدوحة","concept_gloss":"övgüyle seçkin sayılan develer","contextual_glosses":[{"applicability":"Develerin niteliğine hayranlık ve övgü bildiren ünlemli anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Deve kapsamını ve hayranlık bildiren övgüyü korur."},"facet_ids":["F001","F002"],"text":"ne seçkin develer","usage_role":"contextual"}],"definition":"Seçkin, değerli ve görünüşü beğenilen develeri niteleyen bir övgüdür. Bu niteleme, hayvana bakıldığında onun ne kadar iyi olduğunu belirten hayranlık sözüyle açıklanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim, iyi ve seçkin sayılan develerin övgüyle nitelenmesidir."},{"facet_id":"F002","role":"associated_use","statement":"Niteleme, develere bakınca onların değerini ve güzelliğini dile getiren hayranlık sözüyle açıklanır."},{"facet_id":"F003","role":"specialization","statement":"Karınlarının toplu ve düzgün görünmesi, övülen develere verilen betimleyici ayrıntıdır."}],"identity_rationale":"Kaynak ibaresi yalnız seçkin ve iyi develeri, onlara bakınca söylenen hayranlık sözünü ve karınlarının toplu görünüşünü tanıklar. Geçici çerçevedeki eşek kapsamı kaynak ibaresinde bulunmadığından tanım develerle sınırlandırılmıştır.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"övgüyle seçkin ve çok iyi sayılan develer"}],"lexicalization_note":"Tanım yalnız develeri niteleyen kayıtlı biçimi ve ona eşlik eden hayranlık söyleyişini korur; yalın bir övgü anlamı üretmez.","neighbor_coverage_note":"Bütün övgü, kalite ve deve adayları değerlendirildi; genel övgü kalıpları ile yaş veya uysallık ölçen deve nitelemeleri elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yapı bağımlı bir övgü nitelemesidir; komşu dal ise seçkin deve veya malı doğrudan adlandıran daha geniş bir isim alanına sahiptir.","focus_only":"Odak dal develeri hayranlık içeren bir söyleyişle över ve görünüşlerine ilişkin ayrıntı taşıyabilir.","gloss":"seçkin develer","neighbor_only":"Komşu dal seçkin develerin yanında seçkin mal varlığını da adlandırabilir.","neighbor_ref":"root_000001/B014","relation_type":"near_synonym","shared_zone":"Her iki dal iyi ve değerli sayılan develeri adlandırır."}],"source_phrase_ar":"الإبل مسببة؛ قاتلها الله فما أكرمها مالا (maqayis)؛ إبل مسببة أي خيار؛ قاتلها الله (sihah)؛ مسببة قب البطون؛ فمن نظر إليها سبها وقال لها قاتلها الله ما أجودها (tahdhib)","source_summary":"Kaynaklar seçkin develeri övgüyle nitelemede birleşir; hayranlık sözü ve karınların toplu görünüşü bu beğeniyi açıklar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه وصف الإبل أو الحمر بالجودة عند التعجب والمدح","what_is_not_ar":"ليس السبب الحبل ولا السباب"},"support_links":[]},{"boundary":"Dal yalnız sövüşme durumundaki karşı tarafı veya dengi bildirir; genel sövme eylemi ya da sınırsız benzerlik anlamı değildir.","branch_kind":"non_bare","branch_ref":"root_000664/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَبَب","morph_features":"STEM|POS:N|LEM:sabab|ROOT:sbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:85:2:1","qac_word_ref":"18:85:2","surface_ar":"سَبَبًا"}],"gloss":"sövüşmedeki karşı taraf ve denk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel katılımcı, karşılıklı sövüşmede kişinin karşısında yer alan kimsedir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu kişi, genel anlamda değil yalnız sövüşme gücü ve konumu bakımından denk sayılır."}}],"root_ar":"س ب ب","root_id":"root_000664","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Karşılıklı sövüşmede hem muhataplığı hem de bu alandaki denkliği birlikte temsil eder.","boundary_detail":"Dal yalnız sövüşme durumundaki karşı tarafı veya dengi bildirir; genel sövme eylemi ya da sınırsız benzerlik anlamı değildir.","branch_image_ar":"السَّبّ نظير في السباب","concept_gloss":"sövüşmedeki karşı taraf ve denk","contextual_glosses":[{"applicability":"Bir kimsenin karşılıklı sövüşmede başkasına denk olup olmadığı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Denkliği ve onun sövüşmeyle sınırlı oluşunu korur."},"facet_ids":["F001","F002"],"text":"sövüşme dengi","usage_role":"contextual"}],"definition":"Karşılıklı sövüşmede kişinin karşısında yer alan, ona sözle karşılık veren ve bu bakımdan onun dengi sayılan kimsedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel katılımcı, karşılıklı sövüşmede kişinin karşısında yer alan kimsedir."},{"facet_id":"F002","role":"specialization","statement":"Bu kişi, genel anlamda değil yalnız sövüşme gücü ve konumu bakımından denk sayılır."}],"identity_rationale":"Kaynak ibaresi kişiyi genel bir benzer olarak değil, karşılıklı sövüşmede muhatap olan ve aynı düzeyde karşılık verebilen kişi olarak tanımlar. Dalın sövüşme içindeki karşıt ve eş katılımcı sınırı uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"sövüşmede karşı taraf veya denk"}],"lexicalization_note":"Tanım, sövüşme durumunda kişiyi niteleyen kayıtlı biçimle sınırlıdır ve bunu genel bir eş veya benzer adına dönüştürmez.","neighbor_coverage_note":"Bütün denklik, aşağılama ve soy eleştirisi adayları incelendi; sövüşme bağlamıyla en açık karşıtlığı kuran genel rakip dalı seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ölçütü sözlü çatışmadır; komşu dalın ölçütleri yaş, güç ve yiğitlik gibi daha genel karşılaştırma alanlarıdır.","focus_only":"Odak dal denkliği yalnız karşılıklı sövüşmedeki taraflar arasında kurar.","gloss":"bağlama bağlı iki denklik türü","neighbor_only":"Komşu dal yaş, yiğitlik, güç veya dayanıklılık bakımından denk bir rakibi anlatır.","neighbor_ref":"root_001221/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal bir kişinin karşısında ona denk sayılan başka bir kişiyi adlandırır."}],"source_phrase_ar":"يقال للذي يساب سب؛ فلست بسبي (maqayis)؛ فلان سب فلان أي نظيره؛ فلست بسبي (jamhara)؛ سبك الذي يسابك؛ فلست بسبي (sihah)؛ سبك الذي يسابك؛ فلست بسبي (tahdhib)؛ السب المسابب؛ فلست بسبي (mufradat)","source_summary":"Kaynaklar sövüşen karşı taraf ile bu alandaki denkliği birleştirir; söz konusu benzerlik yalnız karşılıklı sözlü çatışma bağlamına bağlıdır.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه السَّبّ أو السَّبِيّ بمعنى الذي يسابك أو يكون نظيرك في مقام السباب","what_is_not_ar":"ليس مطلق الشتم ولا العار ولا السبب الحبل"},"support_links":[]},{"boundary":"Dal elin başparmak yanındaki belirli parmağıdır; sövme eyleminin kendisi veya genel olarak bütün parmaklar değildir.","branch_kind":"bare","branch_ref":"root_000664/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَبَب","morph_features":"STEM|POS:N|LEM:sabab|ROOT:sbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:85:2:1","qac_word_ref":"18:85:2","surface_ar":"سَبَبًا"}],"gloss":"işaret parmağı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim, elde başparmağın hemen yanında bulunan işaret parmağıdır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Parmağın işaret etme ve sayma sırasında kullanılması, ona verilen adların açıklamasına bağlanır."}}],"root_ar":"س ب ب","root_id":"root_000664","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Elin başparmak yanındaki ikinci parmağını doğal ve tam Türkçe karşılıkla belirtir.","boundary_detail":"Dal elin başparmak yanındaki belirli parmağıdır; sövme eyleminin kendisi veya genel olarak bütün parmaklar değildir.","branch_image_ar":"السَّبّابة إصبع الإشارة","concept_gloss":"işaret parmağı","contextual_glosses":[{"applicability":"Parmağın eldeki yerinin açıkça tarif edilmesi gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Parmağın anatomik konumunu eksiksiz biçimde korur."},"facet_ids":["F001"],"text":"başparmağın yanındaki parmak","usage_role":"explanatory"}],"definition":"Elde başparmağın hemen yanında bulunan işaret parmağıdır. İşaret ederken veya sayma sırasında kullanılması, ona verilen adlarla ilişkilendirilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim, elde başparmağın hemen yanında bulunan işaret parmağıdır."},{"facet_id":"F002","role":"associated_use","statement":"Parmağın işaret etme ve sayma sırasında kullanılması, ona verilen adların açıklamasına bağlanır."}],"identity_rationale":"Kaynak ibaresi başparmağın yanındaki parmağı doğrudan tanımlar ve ona işaret etme veya sayma işlevlerinden doğan adların verildiğini belirtir. Anatomik kimlik ile adlandırma açıklaması birbirinden ayrılabilir.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"işaret parmağı"}],"lexicalization_note":"Tanım yalın parmak adını verir; adlandırmayla ilişkili sövme ve işaret etme olaylarını parmağın kurucu anlamına dönüştürmez.","neighbor_coverage_note":"Bütün el, parmak, işaret ve secde adayları incelendi; anatomik üst sınıfla kurulan sınır en açıklayıcı karşılaştırma olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel sınıfın belirli bir üyesidir; komşu dal ise hangi parmak olduğu ayrımını yapmadan bütün sınıfı adlandırır.","focus_only":"Odak dal başparmağın yanındaki tek bir parmağa özgüdür ve işaret işleviyle tanınır.","gloss":"işaret parmağı ile genel parmak","neighbor_only":"Komşu dal eldeki bütün parmakları kapsayan genel sınıf adıdır.","neighbor_ref":"root_000841/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal insan elindeki parmaklardan söz eder."}],"source_phrase_ar":"السبابة الإصبع بعد الإبهام (ayn)؛ السبابة من الاصابع التي تلى الابهام (sihah)؛ السبابة الإصبع التي تلي الإبهام وهي المسبحة (tahdhib)؛ السبابة سميت للإشارة بها عند السب؛ المسبحة (mufradat)","source_summary":"Kaynaklar başparmağın yanındaki parmak tanımında birleşir; işaret etme ve sayma işlevleri bu parmağa verilen iki adın gerekçesini açıklar.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الإصبع التي تلي الإبهام وتسميتها بالسبابة أو المسبحة","what_is_not_ar":"ليس السباب نفسه ولا السبب الحبل"},"support_links":[]},{"boundary":"Dal yalnız yumuşak biçimde ilerleme eylemidir; çorak arazi, bayram günü veya hızlı ve sürekli yolculuk anlamı değildir.","branch_kind":"non_bare","branch_ref":"root_000664/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَبَب","morph_features":"STEM|POS:N|LEM:sabab|ROOT:sbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:85:2:1","qac_word_ref":"18:85:2","surface_ar":"سَبَبًا"}],"gloss":"yumuşak bir yürüyüşle ilerleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel eylem, yürüyerek veya yol alarak ilerlemektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İlerlemenin ayırıcı niteliği yumuşak ve rahat bir gidiş olmasıdır."}}],"root_ar":"س ب ب","root_id":"root_000664","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hareketin ilerleme yönünü ve sert olmayan rahat yapılış biçimini birlikte temsil eder.","boundary_detail":"Dal yalnız yumuşak biçimde ilerleme eylemidir; çorak arazi, bayram günü veya hızlı ve sürekli yolculuk anlamı değildir.","branch_image_ar":"سَبْسَب سير لين","concept_gloss":"yumuşak bir yürüyüşle ilerleme","contextual_glosses":[{"applicability":"Yürüyüşün sertlikten ve aceleden uzak oluşunun öne çıktığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İlerlemeyi ve yumuşak hareket biçimini doğal Türkçeyle korur."},"facet_ids":["F001","F002"],"text":"usulca ilerlemek","usage_role":"contextual"}],"definition":"Yumuşak, rahat ve sert olmayan bir yürüyüş biçimiyle ilerlemektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel eylem, yürüyerek veya yol alarak ilerlemektir."},{"facet_id":"F002","role":"specialization","statement":"İlerlemenin ayırıcı niteliği yumuşak ve rahat bir gidiş olmasıdır."}],"identity_rationale":"Tek kaynak ibaresi eylemi doğrudan yumuşak bir yürüyüşle ilerlemek olarak tanımlar. Geçici çerçeve bu hareketin hız veya kesintisizlik gibi ek nitelikler taşımadığını doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"yumuşak bir yürüyüşle ilerlemek"}],"lexicalization_note":"Tanım yalnız kaynakta tanıklanan eylem biçimini korur; bunu yalın bir yolculuk ya da hız anlamına genellemez.","neighbor_coverage_note":"Bütün hızlı, sürekli, yumuşak ve binek odaklı hareket adayları incelendi; en yakın rahat gidiş karşılaştırması yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kendiliğinden ilerleme eylemidir; komşu dal ise bir kişinin deveyi veya sürüyü belirli biçimde yürütmesini de içerir.","focus_only":"Odak dal ilerleyenin türünü ve onu yöneten bir kişiyi belirtmeden yumuşak gidişi anlatır.","gloss":"yumuşak ilerleme ile hayvanı usulca sürme","neighbor_only":"Komşu dal özellikle deve veya deve sürüsünü yavaş ve rahat biçimde sürmeyi kapsar.","neighbor_ref":"root_000485/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda da sert ve hızlı olmayan rahat bir yol alma biçimi vardır."}],"source_phrase_ar":"سبسب إذا سار سيرا لينا (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Yumuşak bir yürüyüşle ilerleme anlamı yalnız bu tanıklıkta verilir."}],"source_summary":"Tanıklık, ilerleme eylemini yumuşak bir yürüyüş biçimiyle sınırlar; hız, süreklilik veya belirli bir binek koşulu eklemez.","sources":["TA"],"what_is_ar":"يدخل فيه الفعل سبسب إذا سار سيرا لينا","what_is_not_ar":"ليس السَّبْسَب الأرض ولا يوم السَّباسِب"},"support_links":[]},{"boundary":"Dal asılsız veya saçma sözlerle sınırlıdır; çorak arazi, bayram günü ya da genel konuşma güçlüğü anlamı değildir.","branch_kind":"bare","branch_ref":"root_000664/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَبَب","morph_features":"STEM|POS:N|LEM:sabab|ROOT:sbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:85:2:1","qac_word_ref":"18:85:2","surface_ar":"سَبَبًا"}],"gloss":"asılsız sözler ve saçmalıklar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim, gerçek dayanağı olmayan asılsız sözlerdir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İçeriksiz ve değersiz saçmalıklar bu asılsız söz sınıfına girer."}}],"root_ar":"س ب ب","root_id":"root_000664","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gerçek dayanağı ve işe yarar içeriği olmayan sözlerin tamamını doğal biçimde temsil eder.","boundary_detail":"Dal asılsız veya saçma sözlerle sınırlıdır; çorak arazi, bayram günü ya da genel konuşma güçlüğü anlamı değildir.","branch_image_ar":"البَسابِس أباطيل","concept_gloss":"asılsız sözler ve saçmalıklar","contextual_glosses":[{"applicability":"Sözlerin hem gerçek dışı hem de değersiz olduğu gündelik anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözlerin boşluğunu ve asılsızlığını birlikte korur."},"facet_ids":["F001","F002"],"text":"boş ve asılsız laflar","usage_role":"contextual"}],"definition":"Gerçek bir temeli veya işe yarar içeriği bulunmayan asılsız sözler ve saçmalıklardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim, gerçek dayanağı olmayan asılsız sözlerdir."},{"facet_id":"F002","role":"specialization","statement":"İçeriksiz ve değersiz saçmalıklar bu asılsız söz sınıfına girer."}],"identity_rationale":"Tek kaynak ibaresi çoğul biçimi doğrudan asılsız sözler ve saçmalıklarla eşler. Dalın boş, gerçek dışı ve değersiz söz alanı bu tanıklığı tam olarak yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"asılsız sözler ve saçmalıklar"}],"lexicalization_note":"Tanım yalnız kaynakta verilen yalın çoğul söz anlamını kurar; benzer sesli arazi ve hareket dallarını içeri almaz.","neighbor_coverage_note":"Bütün yalan, boş söz ve anlaşılmaz konuşma adayları incelendi; tam eşleşen dal yayımlandı, ek içerik taşıyanlar elendi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Supplied evidence does not show a semantic boundary between the two branches; both denote baseless and nonsensical talk.","focus_only":null,"gloss":"asılsız sözler ve saçmalıklar","neighbor_only":null,"neighbor_ref":"root_000115/B004","relation_type":"synonym","shared_zone":"Her iki dal da gerçek temeli olmayan boş sözleri ve saçmalıkları aynı kapsamla adlandırır."}],"source_phrase_ar":"منه قيل للأباطيل الترهات البسابس (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Asılsız sözler ve saçmalıklar anlamı yalnız bu tanıklıkta verilir."}],"source_summary":"Tanıklık, bu çoğul adı gerçek dayanağı bulunmayan boş sözler ve saçmalıklar olarak açıklar.","sources":["TA"],"what_is_ar":"يدخل فيه البسابس بمعنى الأباطيل والترهات","what_is_not_ar":"ليس السَّبْسَب القفر ولا يوم السَّباسِب"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["18:85:1"],"branch_refs":[],"candidate_id":"cand_ad1befb47c65b699cb70","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:85:1:anti-reset-link","source_type":"word_analysis","support_ids":["sup_3c562fb0426c8a7375f7","sup_e936fb787a67be2555bd"],"title":"clause not isolated","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:1","qac_refs":["18:85:1:1"],"status":"accepted"}},{"anchor_refs":["18:85:1"],"branch_refs":[],"candidate_id":"cand_9bc79a4a5f57d8474991","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:85:1:causal-means-pairing","source_type":"word_analysis","support_ids":["sup_3c562fb0426c8a7375f7","sup_cf8fc56c032ceeeae51e"],"title":"causality meets named means","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:1","qac_refs":["18:85:1:1"],"status":"accepted"}},{"anchor_refs":["18:85:1"],"branch_refs":[],"candidate_id":"cand_dd67c223e9d32cad2718","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:85:1:first-launch-compression","source_type":"word_analysis","support_ids":["sup_3c562fb0426c8a7375f7","sup_f2ad316f086917df3811"],"title":"compressed first launch","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:1","qac_refs":["18:85:1:1"],"status":"accepted"}},{"anchor_refs":["18:85:1"],"branch_refs":[],"candidate_id":"cand_cb3c457b1a2e49cb17fd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:85:1:sequence-consequence","source_type":"word_analysis","support_ids":["sup_3c562fb0426c8a7375f7","sup_be799fd90b3cd7289527"],"title":"immediate consequence after enabling","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:1","qac_refs":["18:85:1:1"],"status":"accepted"}},{"anchor_refs":["18:85:2"],"branch_refs":[],"candidate_id":"cand_cb011d24d491d67f868e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000175"],"scope":"focus_ayah","source_local_id":"18:85:2:boundary-follow-up","source_type":"word_analysis","support_ids":["sup_3129821ff21504735f2d","sup_94e01aa7b28d2b59bc5f"],"title":"provision turns into follow-up","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:2","qac_refs":["18:85:1:2"],"status":"accepted"}},{"anchor_refs":["18:85:2"],"branch_refs":[],"candidate_id":"cand_ce21c6fed21b13905a57","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000175"],"scope":"focus_ayah","source_local_id":"18:85:2:executive-form","source_type":"word_analysis","support_ids":["sup_3129821ff21504735f2d","sup_ea3b0207459def990b34"],"title":"decisive Form IV pursuit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:2","qac_refs":["18:85:1:2"],"status":"accepted"}},{"anchor_refs":["18:85:2"],"branch_refs":[],"candidate_id":"cand_78cb241808b4f6cdc47b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000175"],"scope":"focus_ayah","source_local_id":"18:85:2:implicit-agent-shift","source_type":"word_analysis","support_ids":["sup_3129821ff21504735f2d","sup_51e7a56534517aec15e2"],"title":"beneficiary becomes agent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:2","qac_refs":["18:85:1:2"],"status":"accepted"}},{"anchor_refs":["18:85:2"],"branch_refs":[],"candidate_id":"cand_7cf5f624ee103fb1487b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000175"],"scope":"focus_ayah","source_local_id":"18:85:2:launch-refrain","source_type":"word_analysis","support_ids":["sup_3129821ff21504735f2d","sup_3ffc574381a60ae84de4"],"title":"journey-launch refrain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:2","qac_refs":["18:85:1:2"],"status":"accepted"}},{"anchor_refs":["18:85:2"],"branch_refs":[],"candidate_id":"cand_355460135097bbe7ae2e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000175"],"scope":"focus_ayah","source_local_id":"18:85:2:minimal-clause-motion","source_type":"word_analysis","support_ids":["sup_3129821ff21504735f2d","sup_d3f51b7d11acb1b53471"],"title":"compact action beat","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:2","qac_refs":["18:85:1:2"],"status":"accepted"}},{"anchor_refs":["18:85:2"],"branch_refs":[],"candidate_id":"cand_76e661794a461b896d8d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000175"],"scope":"focus_ayah","source_local_id":"18:85:2:object-narrows-following","source_type":"word_analysis","support_ids":["sup_3129821ff21504735f2d","sup_c6968323ebb288355551"],"title":"means-object pursuit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:2","qac_refs":["18:85:1:2"],"status":"accepted"}},{"anchor_refs":["18:85:2"],"branch_refs":[],"candidate_id":"cand_99a493dc161b9d21d39c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000175"],"scope":"focus_ayah","source_local_id":"18:85:2:qiraat-agency-contrast","source_type":"word_analysis","support_ids":["sup_3129821ff21504735f2d","sup_8841cb0465ad38a33f6a"],"title":"variant clarifies agency","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:2","qac_refs":["18:85:1:2"],"status":"accepted"}},{"anchor_refs":["18:85:2"],"branch_refs":[],"candidate_id":"cand_3d8bfa77db67d0d9126e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000175"],"scope":"focus_ayah","source_local_id":"18:85:2:root-pair-and-severance-contrast","source_type":"word_analysis","support_ids":["sup_0537e911427b8d7f75e9","sup_3129821ff21504735f2d"],"title":"following paired with means","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:2","qac_refs":["18:85:1:2"],"status":"accepted"}},{"anchor_refs":["18:85:2"],"branch_refs":[],"candidate_id":"cand_a76a75df4c91eae8cb87","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000175"],"scope":"focus_ayah","source_local_id":"18:85:2:sound-effort","source_type":"word_analysis","support_ids":["sup_3129821ff21504735f2d","sup_d746828687a47aafb7e8"],"title":"effortful sound contour","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:2","qac_refs":["18:85:1:2"],"status":"accepted"}},{"anchor_refs":["18:85:3"],"branch_refs":[],"candidate_id":"cand_24b98029fcbc2b36be46","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000664"],"scope":"focus_ayah","source_local_id":"18:85:3:cross-surah-access-field","source_type":"word_analysis","support_ids":["sup_7c4688ced30fe8d2fd05","sup_dec9727dcd3584ffb6c5"],"title":"access and severance echoes","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:3","qac_refs":["18:85:2:1"],"status":"accepted"}},{"anchor_refs":["18:85:3"],"branch_refs":[],"candidate_id":"cand_946f645101145dcab598","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000664"],"scope":"focus_ayah","source_local_id":"18:85:3:direct-object-connector","source_type":"word_analysis","support_ids":["sup_1ed4214ab61348a1076f","sup_dec9727dcd3584ffb6c5"],"title":"route-means as object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:3","qac_refs":["18:85:2:1"],"status":"accepted"}},{"anchor_refs":["18:85:3"],"branch_refs":[],"candidate_id":"cand_5e2afdc87cd2fabf4283","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000664"],"scope":"focus_ayah","source_local_id":"18:85:3:noun-form-specificity","source_type":"word_analysis","support_ids":["sup_6af5bc526c1b427594ef","sup_dec9727dcd3584ffb6c5"],"title":"nominal singular object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:3","qac_refs":["18:85:2:1"],"status":"accepted"}},{"anchor_refs":["18:85:3"],"branch_refs":[],"candidate_id":"cand_3646adfcddece2868964","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000664"],"scope":"focus_ayah","source_local_id":"18:85:3:repeated-sound-link","source_type":"word_analysis","support_ids":["sup_de1a95d709f18b658f4b","sup_dec9727dcd3584ffb6c5"],"title":"audible link","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:3","qac_refs":["18:85:2:1"],"status":"accepted"}},{"anchor_refs":["18:85:3"],"branch_refs":[],"candidate_id":"cand_f4b3cc7bd72730f3f338","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000664"],"scope":"focus_ayah","source_local_id":"18:85:3:rope-link-means","source_type":"word_analysis","support_ids":["sup_dec9727dcd3584ffb6c5","sup_e78df57ad40bfb013d6c"],"title":"concrete link image","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:3","qac_refs":["18:85:2:1"],"status":"accepted"}},{"anchor_refs":["18:85:3"],"branch_refs":[],"candidate_id":"cand_238be62070d46c52952c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000664"],"scope":"focus_ayah","source_local_id":"18:85:3:route-cause-split","source_type":"word_analysis","support_ids":["sup_dec9727dcd3584ffb6c5","sup_fdc51f8ebd0172ce3e5e"],"title":"route and means together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:3","qac_refs":["18:85:2:1"],"status":"accepted"}},{"anchor_refs":["18:85:3"],"branch_refs":[],"candidate_id":"cand_2188b00bb8dcaf30c08a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000664"],"scope":"focus_ayah","source_local_id":"18:85:3:same-surah-means-thread","source_type":"word_analysis","support_ids":["sup_58ac12918bd80673524e","sup_dec9727dcd3584ffb6c5"],"title":"provision-to-refrain handoff","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:3","qac_refs":["18:85:2:1"],"status":"accepted"}},{"anchor_refs":["18:85:3"],"branch_refs":[],"candidate_id":"cand_08f28335e95479a74663","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000664"],"scope":"focus_ayah","source_local_id":"18:85:3:selected-indefinite","source_type":"word_analysis","support_ids":["sup_0fb4e9b8a7cdec31e388","sup_dec9727dcd3584ffb6c5"],"title":"one selected unnamed means","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:3","qac_refs":["18:85:2:1"],"status":"accepted"}},{"anchor_refs":["18:85:3"],"branch_refs":[],"candidate_id":"cand_4c3d435c594f65d61a64","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000664"],"scope":"focus_ayah","source_local_id":"18:85:3:unresolved-destination","source_type":"word_analysis","support_ids":["sup_3e55d1b27d7e64c13793","sup_dec9727dcd3584ffb6c5"],"title":"destination withheld","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:85:3","qac_refs":["18:85:2:1"],"status":"accepted"}},{"anchor_refs":["18:85:1"],"branch_refs":[],"candidate_id":"cand_0aadef4f92b569376326","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000175"],"scope":"focus_ayah","source_local_id":"18:85:1:2","source_type":"qac_morpheme","support_ids":["sup_5ac221365ee22f1b6ff6"],"title":"QAC root occurrence: ت ب ع","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["18:85:2"],"branch_refs":[],"candidate_id":"cand_0b4cc03b99d36db56a9d","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000664"],"scope":"focus_ayah","source_local_id":"18:85:2:1","source_type":"qac_morpheme","support_ids":["sup_4a52cc47204c477f11da"],"title":"QAC root occurrence: س ب ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["18:85"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"18:85","branch_refs":["root_000175/B001","root_000664/B003"],"candidate_id":"cand_6b15bf64ee4f971204a8","commentary_obligation":"review","hft_ref":"hft_b53068fab291a31f314a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b1_connector_pursuit","source_type":"hft","support_ids":["sup_c1184877ef47aceeaea3"],"title":"b1_connector_pursuit","trust":"legacy_unbound"},{"anchor_refs":["18:85"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"18:85","branch_refs":["root_000175/B003","root_000664/B003"],"candidate_id":"cand_ae5760fdf2c2a2b0b410","commentary_obligation":"review","hft_ref":"hft_f2542ce67d86340b573f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b2_tracewise_advance","source_type":"hft","support_ids":["sup_1ae51219a8d5550a7019"],"title":"b2_tracewise_advance","trust":"legacy_unbound"},{"anchor_refs":["18:85"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"18:85","branch_refs":["root_000175/B004","root_000664/B003"],"candidate_id":"cand_b3aef8fe101822c7bec7","commentary_obligation":"review","hft_ref":"hft_b91a01861d72ac2747ff","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b3_linked_succession","source_type":"hft","support_ids":["sup_beb64ee19cae5bb28311"],"title":"b3_linked_succession","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فَأَتْبَعَ سَبَبًا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"18:85:1:1","qac_word_ref":"18:85:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"أَتْبَعَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>atobaEa|ROOT:tbE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"18:85:1:2","qac_word_ref":"18:85:1","root_ar":"ت ب ع","surface_ar":"أَتْبَعَ"},{"lemma_ar":"سَبَب","morph_features":"STEM|POS:N|LEM:sabab|ROOT:sbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:85:2:1","qac_word_ref":"18:85:2","root_ar":"س ب ب","surface_ar":"سَبَبًا"}],"word_analysis_qac_refs":[["18:85:1:1"],["18:85:1:2"],["18:85:2:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["18:85:1","18:85:2","18:85:3"]},"focus_surface_evidence":{"arabic_uthmani":"فَأَتْبَعَ سَبَبًا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"18:85:1:1","qac_word_ref":"18:85:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"أَتْبَعَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>atobaEa|ROOT:tbE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"18:85:1:2","qac_word_ref":"18:85:1","root_ar":"ت ب ع","surface_ar":"أَتْبَعَ"},{"lemma_ar":"سَبَب","morph_features":"STEM|POS:N|LEM:sabab|ROOT:sbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:85:2:1","qac_word_ref":"18:85:2","root_ar":"س ب ب","surface_ar":"سَبَبًا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["18:85:1:1"],["18:85:1:2"],["18:85:2:1"]],"word_analysis_refs":["18:85:1","18:85:2","18:85:3"],"word_rows":[{"analysis_record_ref":"18:85:1","analytic_gloss_range_en":"initial sequencing particle that makes the action follow immediately from the prior enabling, with causal consequence also locally live","analytic_root_gloss_range_en":null,"qac_refs":["18:85:1:1"],"root":{},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"18:85:2","analytic_gloss_range_en":"perfect active Form IV pursuit or follow-up of a route-means, with the subject carried by prior discourse and the endpoint left unstated","analytic_root_gloss_range_en":"root range of following after, pursuing, overtaking, succession, adherence, and consequence; the local clause selects active pursuit of a means rather than person-following or doctrinal adherence","qac_refs":["18:85:1:2"],"root":{"arabic":"ت ب ع","transliteration":"t-b-ʿ"},"surface":{"arabic":"أَتْبَعَ","transliteration":"atbaʿa"}},{"analysis_record_ref":"18:85:3","analytic_gloss_range_en":"an indefinite singular route-means, a concrete connector and selected share of provision followed as the direct object while its destination remains unstated","analytic_root_gloss_range_en":"root range of rope, link, means of access, cause, connection, route, and severable bond; the local noun selects the travel-access and means branch while preserving concrete connector pressure","qac_refs":["18:85:2:1"],"root":{"arabic":"س ب ب","transliteration":"s-b-b"},"surface":{"arabic":"سَبَبًا","transliteration":"sababā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["18:85"],"branch_refs":["root_000175/B001","root_000664/B003"],"candidate_id":"cand_6b15bf64ee4f971204a8","evidence_scope":"focus_ayah","hft_ref":"hft_b53068fab291a31f314a","item_id":"b1_connector_pursuit","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b1_connector_pursuit","support_id":"sup_c1184877ef47aceeaea3"},{"anchor_refs":["18:85"],"branch_refs":["root_000175/B003","root_000664/B003"],"candidate_id":"cand_ae5760fdf2c2a2b0b410","evidence_scope":"focus_ayah","hft_ref":"hft_f2542ce67d86340b573f","item_id":"b2_tracewise_advance","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b2_tracewise_advance","support_id":"sup_1ae51219a8d5550a7019"},{"anchor_refs":["18:85"],"branch_refs":["root_000175/B004","root_000664/B003"],"candidate_id":"cand_b3aef8fe101822c7bec7","evidence_scope":"focus_ayah","hft_ref":"hft_b91a01861d72ac2747ff","item_id":"b3_linked_succession","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b3_linked_succession","support_id":"sup_beb64ee19cae5bb28311"}],"diagnostics":[],"lane_counts":{"global":7,"macro":8,"micro":3},"packet_summary":{"ayah_count":16,"focus_ref":"18:85","protocol":"focus-trace-pericope-lean-v1","split_root_mappings":[],"window":["18:83","18:84","18:85","18:86","18:87","18:88","18:89","18:90","18:91","18:92","18:93","18:94","18:95","18:96","18:97","18:98"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"valid_pericope_packet_unbound_response"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"18:85","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":7,"source_present":true,"structured_insight_count":11,"unstructured_record_count":0},"identity":{"ayah_ref":"18:85","lane":"micro","linguistic_source_ref":"18:85","surface_ref":"18:85","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"18:85","target_tokens":[["O",["18:85:1"]],["da",["18:85:1"]],["bir",["18:85:1"]],["yol",["18:85:2"]],["izledi",["18:85:2"]]],"text":"O da bir yol izledi."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":83,"ayah_to":98,"id":"s018-p05-083-098","label":"Dhul-Qarnayn and Gog and Magog","number":5,"refs":["18:83","18:84","18:85","18:86","18:87","18:88","18:89","18:90","18:91","18:92","18:93","18:94","18:95","18:96","18:97","18:98"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:2:root-pair-and-severance-contrast","source_type":"word_analysis","support_id":"sup_0537e911427b8d7f75e9","text":"{\"blocking_evidence\":null,\"headline\":\"following paired with means\",\"reader_payoff\":\"The reader notices that following and means form a marked pair here, with the connection being pursued rather than cut as in 2:166.\",\"reason\":\"The local verb-object pair is repeated in the Dhu al-Qarnayn itinerary and can be contrasted with the severed connection field in 2:166 without making that contrast govern the local parse.\",\"representative_source_ids\":[\"QI-1373d9d3\",\"QE-9568a718\",\"ME-f26e1e8d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:3:selected-indefinite","source_type":"word_analysis","support_id":"sup_0fb4e9b8a7cdec31e388","text":"{\"blocking_evidence\":null,\"headline\":\"one selected unnamed means\",\"reader_payoff\":\"The reader notices that the noun selects one available means from prior provision while withholding its identity and destination.\",\"reason\":\"The noun is singular and indefinite with tanwīn, and the preceding context supplies broad means before this selected object.\",\"representative_source_ids\":[\"QG-13810811\",\"QG-f87663c5\",\"QF-65988f2c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:3:direct-object-connector","source_type":"word_analysis","support_id":"sup_1ed4214ab61348a1076f","text":"{\"blocking_evidence\":null,\"headline\":\"route-means as object\",\"reader_payoff\":\"The reader notices that the means is not background setting; grammar makes it the object directly taken up and pursued.\",\"reason\":\"The noun is accusative and syntactically forced as the direct object of {{ar:أَتْبَعَ}} ({{tr:atbaʿa}}).\",\"representative_source_ids\":[\"QG-08c67a19\",\"QG-b3519dd5\",\"QG-d08c0f20\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:2","source_type":"word_analysis","support_id":"sup_3129821ff21504735f2d","text":"{\"gloss_range\":\"perfect active Form IV pursuit or follow-up of a route-means, with the subject carried by prior discourse and the endpoint left unstated\",\"prose\":\"{{ar:أَتْبَعَ}} ({{tr:atbaʿa}}) is the first finite travel action after the grant of 18:84. Its implicit 3ms subject carries the prior beneficiary forward as the current agent, while the active perfect Form IV presents the route-taking as decisive executive pursuit that turns prior provision into a result-bearing follow-up. Because the verb governs {{ar:سَبَبًا}} ({{tr:sababā}}) directly, following is narrowed away from imitating a person or doctrine into pressing a means until it opens access; the endpoint is deliberately left for the next scene, so action and object launch movement before any destination is named. The phrase then becomes the journey-launch refrain answered at 18:89 and 18:92, with the accepted Form VIII variant preserving the same object frame while shifting the feel toward personal adoption of the path. The same following-means pair can also be heard against the severed-connection scene of 2:166: here the connection is pursued rather than cut. Even the compact stop-to-pharyngeal sound contour gives the pursuit an effortful feel, while the grammar remains the main evidence.\",\"root_display\":\"{{ar:ت ب ع}} ({{tr:t-b-ʿ}})\",\"root_gloss_range\":\"root range of following after, pursuing, overtaking, succession, adherence, and consequence; the local clause selects active pursuit of a means rather than person-following or doctrinal adherence\",\"surface_display\":\"{{ar:أَتْبَعَ}} ({{tr:atbaʿa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:1","source_type":"word_analysis","support_id":"sup_3c562fb0426c8a7375f7","text":"{\"gloss_range\":\"initial sequencing particle that makes the action follow immediately from the prior enabling, with causal consequence also locally live\",\"prose\":\"{{ar:فَ}} ({{tr:fa}}) makes the route-taking in {{ar:أَتْبَعَ}} ({{tr:atbaʿa}}) the immediate next beat after the enabling of 18:84. The particle is not a clean narrative reset: it carries sequence and consequence together, so the action feels like provision becoming use. Because the first launch is compressed into a one-letter connector while the connector changes at 18:89 and 18:92, this opening movement stays more tightly attached to the prior grant than the later renewed journey beats.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:3:unresolved-destination","source_type":"word_analysis","support_id":"sup_3e55d1b27d7e64c13793","text":"{\"blocking_evidence\":null,\"headline\":\"destination withheld\",\"reader_payoff\":\"The reader notices that the ayah ends on the means itself, creating forward dependence on the next beat for destination.\",\"reason\":\"The clause is syntactically complete with verb and object, but it names no endpoint; the object closes the ayah.\",\"representative_source_ids\":[\"QT-c41a5b3e\",\"QT-e41d7e47\",\"MT-81a354da\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:2:launch-refrain","source_type":"word_analysis","support_id":"sup_3ffc574381a60ae84de4","text":"{\"blocking_evidence\":null,\"headline\":\"journey-launch refrain\",\"reader_payoff\":\"The reader notices the verb as part of the repeated launch formula that segments the three-stage itinerary at 18:85, 18:89, and 18:92.\",\"reason\":\"The same verb-object phrase recurs at 18:89 and 18:92, making the current verb a structural refrain rather than a one-off travel verb.\",\"representative_source_ids\":[\"QI-93cdabde\",\"MI-64f35a47\",\"MT-617fa66c\",\"QY-d768524a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"18:85:2:1","source_type":"qac_morpheme","support_id":"sup_4a52cc47204c477f11da","text":"{\"lemma_ar\":\"سَبَب\",\"morph_features\":\"STEM|POS:N|LEM:sabab|ROOT:sbb|M|INDEF|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"18:85:2:1\",\"qac_word_ref\":\"18:85:2\",\"root_ar\":\"س ب ب\",\"surface_ar\":\"سَبَبًا\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:2:implicit-agent-shift","source_type":"word_analysis","support_id":"sup_51e7a56534517aec15e2","text":"{\"blocking_evidence\":null,\"headline\":\"beneficiary becomes agent\",\"reader_payoff\":\"The reader notices that the one just enabled in 18:84 becomes the acting subject without being renamed.\",\"reason\":\"The verb is active 3ms with an implicit subject, and attachment evidence resolves that subject through the preceding Dhu al-Qarnayn discourse.\",\"representative_source_ids\":[\"QG-05c7c8cf\",\"QG-71bfee11\",\"QB-269231e0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:3:same-surah-means-thread","source_type":"word_analysis","support_id":"sup_58ac12918bd80673524e","text":"{\"blocking_evidence\":null,\"headline\":\"provision-to-refrain handoff\",\"reader_payoff\":\"The reader notices the noun moving from grant in 18:84 to pursuit in 18:85 and then into the repeated launch pattern at 18:89 and 18:92.\",\"reason\":\"The same root and phrase recur in the Dhu al-Qarnayn sequence, giving the noun a structural role across the journey launches.\",\"representative_source_ids\":[\"QI-fb356d8b\",\"QE-fada4830\",\"QB-130d08cb\",\"QY-43115e44\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"18:85:1:2","source_type":"qac_morpheme","support_id":"sup_5ac221365ee22f1b6ff6","text":"{\"lemma_ar\":\"أَتْبَعَ\",\"morph_features\":\"STEM|POS:V|PERF|(IV)|LEM:>atobaEa|ROOT:tbE|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"18:85:1:2\",\"qac_word_ref\":\"18:85:1\",\"root_ar\":\"ت ب ع\",\"surface_ar\":\"أَتْبَعَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:3:noun-form-specificity","source_type":"word_analysis","support_id":"sup_6af5bc526c1b427594ef","text":"{\"blocking_evidence\":null,\"headline\":\"nominal singular object\",\"reader_payoff\":\"The reader notices one free, unqualified link rather than a plural network, construct-domain route, or new verbal act of causing.\",\"reason\":\"The local form is a singular indefinite noun, not a construct plural or causative verb, so it objectifies a means rather than naming a whole network.\",\"representative_source_ids\":[\"QF-30921c9c\",\"QF-d23dd5ab\",\"QF-eb90d1a8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:3:cross-surah-access-field","source_type":"word_analysis","support_id":"sup_7c4688ced30fe8d2fd05","text":"{\"blocking_evidence\":null,\"headline\":\"access and severance echoes\",\"reader_payoff\":\"The reader notices that the local means belongs to a wider Quranic field where connections can be cut (2:166) or sought as heavenly access (38:10; 40:36-37).\",\"reason\":\"The concrete references are useful echoes for access and severability, but the local singular direct object remains the selected route-means in 18:85.\",\"representative_source_ids\":[\"MS-3182d507\",\"MI-33348137\",\"QE-c5714b7a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:2:qiraat-agency-contrast","source_type":"word_analysis","support_id":"sup_8841cb0465ad38a33f6a","text":"{\"blocking_evidence\":null,\"headline\":\"variant clarifies agency\",\"reader_payoff\":\"The reader notices that the accepted variant keeps the same route-means object while exposing a contrast between executive pursuit and personal adoption.\",\"reason\":\"The variant is useful as form contrast, but the standard local surface remains {{ar:أَتْبَعَ}} ({{tr:atbaʿa}}), so the variant does not replace the local parse.\",\"representative_source_ids\":[\"QS-bad174b5\",\"QF-28279ed8\",\"QF-32da26b2\",\"MF-debaad69\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:2:boundary-follow-up","source_type":"word_analysis","support_id":"sup_94e01aa7b28d2b59bc5f","text":"{\"blocking_evidence\":null,\"headline\":\"provision turns into follow-up\",\"reader_payoff\":\"The reader notices the action as provision converted into follow-up, where the granted means becomes the next result-bearing step.\",\"reason\":\"The sequential boundary and the cause-means object let following, consequence, and enacted provision converge without replacing the local transitive frame.\",\"representative_source_ids\":[\"QS-291e5e7a\",\"QS-448f69de\",\"QB-59daf6a7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:1:sequence-consequence","source_type":"word_analysis","support_id":"sup_be799fd90b3cd7289527","text":"{\"blocking_evidence\":null,\"headline\":\"immediate consequence after enabling\",\"reader_payoff\":\"The reader notices that the journey begins as the immediate consequence of the prior enabling, not as an isolated travel notice.\",\"reason\":\"The QAC row identifies the particle as immediate sequencing, and the local clause follows directly after the provision frame of 18:84.\",\"representative_source_ids\":[\"QG-9ed6b499\",\"QS-4fd9ec43\",\"QB-9c46d3ba\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:2:object-narrows-following","source_type":"word_analysis","support_id":"sup_c6968323ebb288355551","text":"{\"blocking_evidence\":null,\"headline\":\"means-object pursuit\",\"reader_payoff\":\"The reader notices that following has become procedural pursuit of a means, with a telic press toward access rather than interpersonal imitation.\",\"reason\":\"The direct object {{ar:سَبَبًا}} ({{tr:sababā}}) selects route-means pursuit; broader adherence, person-following, and abstract succession remain root pressure but are not the free local sense.\",\"representative_source_ids\":[\"QG-8d250836\",\"QG-90945043\",\"QS-c270f0ba\",\"QS-b4d7e010\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:1:causal-means-pairing","source_type":"word_analysis","support_id":"sup_cf8fc56c032ceeeae51e","text":"{\"blocking_evidence\":null,\"headline\":\"causality meets named means\",\"reader_payoff\":\"The reader notices a double causality: the connector makes the action consequential, and the object names the means being activated.\",\"reason\":\"The particle's causal force coheres with the local object {{ar:سَبَبًا}} ({{tr:sababā}}), whose narrowed range includes means and route.\",\"representative_source_ids\":[\"QS-eb72d632\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:2:minimal-clause-motion","source_type":"word_analysis","support_id":"sup_d3f51b7d11acb1b53471","text":"{\"blocking_evidence\":null,\"headline\":\"compact action beat\",\"reader_payoff\":\"The reader notices how little the clause gives: action and object are enough to launch movement while direction and destination are withheld.\",\"reason\":\"The verbal clause has a finite verb and one explicit object, with no overt destination or subordinate expansion.\",\"representative_source_ids\":[\"QT-a75f1ac2\",\"QT-bf12bf38\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:2:sound-effort","source_type":"word_analysis","support_id":"sup_d746828687a47aafb7e8","text":"{\"blocking_evidence\":null,\"headline\":\"effortful sound contour\",\"reader_payoff\":\"The reader notices a compact acoustic pressure that fits deliberate pursuit without becoming the main grammatical evidence.\",\"reason\":\"The sound observation is local and modest; it supports the pursuit feel but does not create a separate lexical branch.\",\"representative_source_ids\":[\"QP-bd410ae9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:3:repeated-sound-link","source_type":"word_analysis","support_id":"sup_de1a95d709f18b658f4b","text":"{\"blocking_evidence\":null,\"headline\":\"audible link\",\"reader_payoff\":\"The reader notices a repeated b-sound that audibly binds the pursued object to the action.\",\"reason\":\"The sound observation stays local and supportive: it reinforces the link between verb and object without creating an independent semantic proof.\",\"representative_source_ids\":[\"MS-55781054\",\"QP-6dd79eb1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:3","source_type":"word_analysis","support_id":"sup_dec9727dcd3584ffb6c5","text":"{\"gloss_range\":\"an indefinite singular route-means, a concrete connector and selected share of provision followed as the direct object while its destination remains unstated\",\"prose\":\"{{ar:سَبَبًا}} ({{tr:sababā}}) is the thing followed, not a loose circumstance around the journey. As an accusative direct object after {{ar:أَتْبَعَ}} ({{tr:atbaʿa}}), it turns the route or means into a handleable connector, like a link one can take up and pursue. Its singular indefiniteness matters: after the broad enabling of 18:84, this is one selected share of means, still unnamed enough that 18:86 must disclose where it leads. The word therefore works as both a path to follow and a means by which prior provision becomes consequence, while the direct-object frame keeps it from collapsing into an abstract cause. As a free singular noun, it is one unqualified link rather than a plural network, a construct-bound heavenly access phrase, or a new verbal act of causing. The same noun then becomes a refrain at 18:89 and 18:92, while the wider plural field can evoke severed connections (2:166) or heavenly accesses (38:10; 40:36-37) without making those scenes control the local route-means sense. The repeated b-sound across the verb-object phrase audibly binds pursuit to means, matching the grammar without replacing it.\",\"root_display\":\"{{ar:س ب ب}} ({{tr:s-b-b}})\",\"root_gloss_range\":\"root range of rope, link, means of access, cause, connection, route, and severable bond; the local noun selects the travel-access and means branch while preserving concrete connector pressure\",\"surface_display\":\"{{ar:سَبَبًا}} ({{tr:sababā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:3:rope-link-means","source_type":"word_analysis","support_id":"sup_e78df57ad40bfb013d6c","text":"{\"blocking_evidence\":null,\"headline\":\"concrete link image\",\"reader_payoff\":\"The reader notices that the abstract means still feels like a concrete connector that carries movement across distance.\",\"reason\":\"The root range supports rope, link, means, and route, but the local direct-object frame narrows the payoff to travel-access and functional connection rather than activating every dictionary branch.\",\"representative_source_ids\":[\"QS-1be10f30\",\"QS-7f398df0\",\"QS-f34b761c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:1:anti-reset-link","source_type":"word_analysis","support_id":"sup_e936fb787a67be2555bd","text":"{\"blocking_evidence\":null,\"headline\":\"clause not isolated\",\"reader_payoff\":\"The reader notices that the ayah opens inside motion already linked to the previous ayah rather than restarting with a fresh subject or location.\",\"reason\":\"The connector governs the compact verbal clause and keeps it structurally dependent on the preceding grant.\",\"representative_source_ids\":[\"QG-ab13021c\",\"QT-421db3e2\",\"QT-a01a255f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:2:executive-form","source_type":"word_analysis","support_id":"sup_ea3b0207459def990b34","text":"{\"blocking_evidence\":null,\"headline\":\"decisive Form IV pursuit\",\"reader_payoff\":\"The reader notices that the verb frames the movement as an enacted course-setting decision, not a tentative search or mere state of being a follower.\",\"reason\":\"The local form is perfect active Form IV and transitive, so the causative or executive pressure is realized through taking up the route-means.\",\"representative_source_ids\":[\"QG-18107f1c\",\"QF-6bfbb8ce\",\"QF-e5c144f8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:1:first-launch-compression","source_type":"word_analysis","support_id":"sup_f2ad316f086917df3811","text":"{\"blocking_evidence\":null,\"headline\":\"compressed first launch\",\"reader_payoff\":\"The reader notices that the first journey launch is tighter than the later launches at 18:89 and 18:92, where the connector changes.\",\"reason\":\"The proclitic form fuses transition onto the verb, while the supplied same-surah evidence contrasts later launches with a different connector at 18:89 and 18:92.\",\"representative_source_ids\":[\"QG-eeec2307\",\"QF-8fd6aede\",\"QF-c8cf3ab2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:85:3:route-cause-split","source_type":"word_analysis","support_id":"sup_fdc51f8ebd0172ce3e5e","text":"{\"blocking_evidence\":null,\"headline\":\"route and means together\",\"reader_payoff\":\"The reader notices that the word is both a path to follow and a means by which provision becomes consequence.\",\"reason\":\"The preceding connector carries consequence while the governing verb and object case select route-following, allowing cause-means pressure without reducing the noun to an abstract cause.\",\"representative_source_ids\":[\"QS-152e875b\",\"QS-42662daa\",\"QS-e2e843a3\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَأَتْبَعَ سَبَبًا","ayah_ref":"18:85"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000175/B001","root_000664/B003"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000175","role":"Following contributes deliberate pursuit of a prior person, matter, or trace.","root":"ت ب ع","source_ref":"18:85","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000664","role":"The rope or connection contributes the traversable means that pursuit uses.","root":"س ب ب","source_ref":"18:85","source_word_indices":["2"]}],"changed_reading":{"after":"He deliberately pursued a connective route or means that could carry him beyond his present position.","before":"He went on."},"confidence":"strong","focus_anchor":"Words 1-2 join a following verb to sabab as its object.","mechanism":"Following supplies directed pursuit, while sabab supplies a rope-like connection, route, or means; the clause depicts taking hold of access rather than undirected motion.","model_id":"b1_connector_pursuit"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b1_connector_pursuit","source_type":"hft","support_id":"sup_c1184877ef47aceeaea3","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَأَتْبَعَ سَبَبًا","ayah_ref":"18:85"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000175/B003","root_000664/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000175","role":"Stepwise tracking contributes a measured, clue-by-clue mode of advance.","root":"ت ب ع","source_ref":"18:85","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000664","role":"The means or route organizes the traces into an actionable line of access.","root":"س ب ب","source_ref":"18:85","source_word_indices":["2"]}],"changed_reading":{"after":"He investigated his way forward by pursuing an ordered chain of traces or affordances.","before":"He selected a road."},"confidence":"medium","focus_anchor":"The verb at word 1 can denote tracing step after step, directed into the means at word 2.","mechanism":"The clause can describe an evidential procedure: successive traces are pursued along an enabling connection, so advance depends on reading and testing what leads onward.","model_id":"b2_tracewise_advance"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b2_tracewise_advance","source_type":"hft","support_id":"sup_1ae51219a8d5550a7019","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَأَتْبَعَ سَبَبًا","ayah_ref":"18:85"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000175/B004","root_000664/B003"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000175","role":"Unbroken succession contributes the transition into a next operational unit.","root":"ت ب ع","source_ref":"18:85","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000664","role":"Connection supplies what binds the new unit to a continuing sequence.","root":"س ب ب","source_ref":"18:85","source_word_indices":["2"]}],"changed_reading":{"after":"This is the opening of a connected next phase whose parts are meant to follow one another.","before":"This is one self-contained movement."},"confidence":"exploratory","focus_anchor":"The prefixed clause and the verb at word 1 permit succession, while word 2 supplies the linking medium.","mechanism":"Atba'a can mark one operation following another without a gap; paired with a connector, the short clause can open the next unit in a linked series rather than report an isolated trip.","model_id":"b3_linked_succession"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b3_linked_succession","source_type":"hft","support_id":"sup_beb64ee19cae5bb28311","trust":"legacy_unbound"}]}
</lane_packet_json>
