# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **111:4**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s111-regular-20260911/s111/111_4/micro.discovery.json` and modify nothing
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
  "ayah_ref": "111:4",
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
{"analysis_context":{"analysis_id":"s111-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"111:4","host_surah":111,"lane_context_refs":[],"ordered_context_refs":["111:0","111:1","111:2","111:3","111:5","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Gerçek yakacak odun ile onu toplama çekirdektir; konuşma, laf taşıma ve aşırı zayıflıkla ilgili mecazi dallar bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000335/B001","candidate_links":[{"candidate_id":"cand_f338f372d0dd70cf44f8","lane":"micro"},{"candidate_id":"cand_c3eb81b161ea6bb9b135","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَطَب","morph_features":"STEM|POS:N|LEM:HaTab|ROOT:HTb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:3:2","qac_word_ref":"111:4:3","surface_ar":"حَطَبِ"}],"gloss":"yakacak odun ve odun toplama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yakılmaya hazırlanan odun, dal ve benzeri bitkisel parçalar yakacak olarak adlandırılır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu yakacağı arayıp bir araya getirme eylemi dalın temel süreç anlamıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Odun, kişinin kendisi yerine bir başkası için toplanabilir veya o kişiye getirilebilir."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Belirli bir yer, orada çok miktarda odun bulunması bakımından nitelenebilir."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Belirli bir niteleme, kuru diken veya odun yiyen dişi deveyi anlatır."}},{"facet_id":"F006","role":"specialization","source_fields":["distinctive_facets[F006]"],"statements":{"statement":"Bağın üst dallarının odun olarak kesilecek duruma gelmesi ve kesilen odunluk dallar, bağcılığa özgü kullanımlardır."}}],"root_ar":"ح ط ب","root_id":"root_000335","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın gerçek nesne ve temel eylem çekirdeğini birlikte karşılayan genel açıklama olarak uygundur.","boundary_detail":"Gerçek yakacak odun ile onu toplama çekirdektir; konuşma, laf taşıma ve aşırı zayıflıkla ilgili mecazi dallar bu dala girmez.","branch_image_ar":"الحطب وقود يجمع ويحتطب","concept_gloss":"yakacak odun ve odun toplama","contextual_glosses":[{"applicability":"Yakılmak üzere hazırlanmış odunun nesne olarak geçtiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakılmak için hazırlanan odun anlamını eksiksiz korur."},"facet_ids":["F001"],"text":"yakacak odun","usage_role":"general"},{"applicability":"Yakacak odunu arayıp bir araya getirme eyleminin anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakacağı arayıp bir araya getirme sürecini korur."},"facet_ids":["F002"],"text":"odun toplamak","usage_role":"general"},{"applicability":"Toplama işinin yararlanıcısı başka bir kişi olduğunda ve odun ona ulaştırıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başka yararlanıcıyı, toplama işini ve odunun getirilmesini korur."},"facet_ids":["F003"],"text":"birisi için odun toplayıp getirmek","usage_role":"contextual"},{"applicability":"Bir yerin çok miktarda odun barındırdığını belirten niteleme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yeri ve oradaki odun bolluğunu birlikte korur."},"facet_ids":["F004"],"text":"odunu bol yer","usage_role":"contextual"}],"definition":"Yakılmak üzere hazırlanan odun ve bu odunu arayıp toplama işidir. Başkası için getirilen odun, odunu bol yer, kuru diken ya da odun yiyen dişi deve ve bağdan kesilen odunluk dallar yalnız kendilerine özgü biçimlerde bu çekirdeğe bağlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yakılmaya hazırlanan odun, dal ve benzeri bitkisel parçalar yakacak olarak adlandırılır."},{"facet_id":"F002","role":"core","statement":"Bu yakacağı arayıp bir araya getirme eylemi dalın temel süreç anlamıdır."},{"facet_id":"F003","role":"specialization","statement":"Odun, kişinin kendisi yerine bir başkası için toplanabilir veya o kişiye getirilebilir."},{"facet_id":"F004","role":"specialization","statement":"Belirli bir yer, orada çok miktarda odun bulunması bakımından nitelenebilir."},{"facet_id":"F005","role":"associated_use","statement":"Belirli bir niteleme, kuru diken veya odun yiyen dişi deveyi anlatır."},{"facet_id":"F006","role":"specialization","statement":"Bağın üst dallarının odun olarak kesilecek duruma gelmesi ve kesilen odunluk dallar, bağcılığa özgü kullanımlardır."}],"identity_rationale":"Kaynak ifadesi, yakılmak üzere hazırlanan odunu ve onu toplamayı temel alır; başkası için odun getirme, odunu bol yer, kuru diken yiyen dişi deve ve bağdan odunluk dal kesme kullanımlarını da ayrı kapsamlar olarak verir. Geçici dal çerçevesi bu çekirdeği ve ona bağlı kullanımları doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yakacak odun"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"odun toplamak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"kendisi için odun arayıp toplamak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"birisi için odun toplayıp getirmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"odun toplayan kişi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"odun toplayan kişi"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"odun toplayıp satan kişi"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"odun toplayanlar topluluğu"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"odunu bol yer"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kuru diken veya odun yiyen dişi deve"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"bağın odunluk dallarını kesme vakti gelmek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bağın üst dalları odun için kesilecek duruma gelmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bağdan kesilen odunluk üst dallar"}],"lexicalization_note":"Tanım, yalın yakacak odun ve odun toplama çekirdeğini; yalnız belirli biçim ve söz öbeklerinde görülen kişi, yer, hayvan ve bağ budama anlamlarından ayrı tutar.","neighbor_coverage_note":"Verilen bütün komşular değerlendirildi; yakıt ve ateşe atılan nesneyle ilgili en yakın iki sınır ile aynı kökün üç mecazi dalı, okuyucunun karıştırma olasılığı en yüksek karşılaştırmalar olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odun nesnesi bakımından örtüşürler; ancak odun toplama ve özel türevler yalnız odak dalda, daha genel yakıt kapsamı ise komşu dalda belirgindir.","focus_only":"Bu dal, odunun toplanmasını ve ona bağlı kişi, yer, hayvan ve bağ kullanımlarını da kapsar.","gloss":"yakıt maddesi","neighbor_only":"Komşu dal, odun dışındaki yakıt maddelerine ve aktarılan mecazi kapsamlara da açılır.","neighbor_ref":"root_001672/B002","relation_type":"near_synonym","shared_zone":"İki dal da ateşi yakmak veya sürdürmek için kullanılan odunu kapsar."},{"boundary_match":"partial","distinction":"Odak dal nesnenin türünü ve toplanmasını, komşu dal ise ateşe atılma ilişkisini tanımlar; bu yüzden olağan biçimde birbirlerinin yerine geçmezler.","focus_only":"Odak dal, odunu yakılmadan önce bir yakacak türü olarak ve onun toplanma süreciyle birlikte ele alır.","gloss":"ateşe atılan yakacak","neighbor_only":"Komşu dal, odun olsun olmasın bir şeyin ateşe atılması koşulunu öne çıkarır.","neighbor_ref":"root_000325/B004","relation_type":"near_neighbor","shared_zone":"Yakacak odun hem hazırlanmış bir yakıt hem de ateşe atılan bir nesne olabilir."},{"boundary_match":"thematic_only","distinction":"Ortaklık yalnız görüntü düzeyindedir; birinde somut yakacak ve toplama, ötekinde düzensiz ya da aşırı konuşma vardır.","focus_only":"Odak dal gerçek odunu, yakacak hazırlanmasını ve toplama işini bildirir.","gloss":"sözü karıştırıp uzatma","neighbor_only":"Komşu dal, sözünü karıştıran veya gereksizce uzatan kişiyi belirli bir benzetmeyle anlatır.","neighbor_ref":"root_000335/B002","relation_type":"thematic","shared_zone":"Komşu anlam, odun toplama görüntüsünü bir konuşma davranışını anlatmak için kullanır."},{"boundary_match":"thematic_only","distinction":"Somut yakacak bu dalın konusudur; söz taşıma ve toplumsal zarar ise ayrı bir mecazi çekirdek oluşturur.","focus_only":"Odak dal gerçek yakacak odun ile onu toplama işini ifade eder.","gloss":"laf taşıyıp kötülük körükleme","neighbor_only":"Komşu dal, insanlar arasında söz taşıma ve kötülüğü büyütme eylemini anlatır.","neighbor_ref":"root_000335/B003","relation_type":"thematic","shared_zone":"Komşu anlam, odun ve ateş görüntüsünden insanlar arasındaki zararı anlatırken yararlanır."},{"boundary_match":"thematic_only","distinction":"Odak dal somut nesneyi, komşu dal ise o nesnenin kuruluğuna dayanan insan niteliğini ifade eder.","focus_only":"Odak dal yakılacak odunun kendisini ve toplanmasını kapsar.","gloss":"kuru odun gibi çok zayıf","neighbor_only":"Komşu dal, kuru oduna benzetilen çok zayıf kişiyi niteler.","neighbor_ref":"root_000335/B004","relation_type":"thematic","shared_zone":"Kuru odun görüntüsü, komşu dalda beden görünüşü için benzetme kaynağıdır."}],"source_phrase_ar":"الحطب معروف (maqayis;ayn;jamhara;sihah;tahdhib)؛ ما يعد للإيقاد (mufradat)؛ حطبت واحتطبت إذا جمعته (sihah)؛ حطبت فلانا إذا احتطبت له (tahdhib)؛ مكان حطيب كثير الحطب (maqayis;jamhara;sihah;mufradat)؛ ناقة محاطبة تأكل الشوك اليابس (maqayis;sihah)؛ قد استحطب عنبكم فاحطبوه حطبا (tahdhib)","source_summary":"Ortak anlatım, yakacak odunu ve onu toplamayı merkezde tutar; başkası için toplama, odunca zengin yer, kuru bitki yiyen dişi deve ve bağdan kesilen odunluk dallar bu merkezin özel kullanımlarıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحطب المعروف وما يعد للإيقاد، وجمعه واحتطابه وحمله أو إحضاره للغير، والحطاب والحطابة، والمكان الكثير الحطب، وما يقطع من الكرم أو العنب حطبا، والناقة التي تأكل الشوك اليابس أو الحطب.","what_is_not_ar":"لا يدخل فيه خلط الكلام كحاطب ليل، ولا النميمة والسعاية بالحطب، ولا الهزال المشبه بالحطب اليابس، ولا الأعلام والأمثال التي يكون حاطب فيها اسما."},"support_links":["sup_02e67034803912d704c0","sup_228cf238a28dc4f1b0e2"]},{"boundary":"Bu dal yalnız belirli söz öbeğinin düzensiz, çok veya uzun konuşan kişiyi nitelemesine ilişkindir; gerçek odun toplama ve laf taşıma anlamları dışarıda kalır.","branch_kind":"collocation","branch_ref":"root_000335/B002","candidate_links":[{"candidate_id":"cand_1596ab352af9b9b588a8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَطَب","morph_features":"STEM|POS:N|LEM:HaTab|ROOT:HTb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:3:2","qac_word_ref":"111:4:3","surface_ar":"حَطَبِ"}],"gloss":"sözünü karıştırıp gereksizce uzatan kimse","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, konuşmasında farklı sözleri veya düşünceleri düzensiz biçimde birbirine karıştırır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı niteleme, gereğinden çok konuşan veya sözünü uzun uzadıya sürdüren kişi için de kullanılır."}}],"root_ar":"ح ط ب","root_id":"root_000335","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli söz öbeğinin karışık, aşırı veya uzun konuşan kişiyi nitelediği bütün bağlamları kapsar.","boundary_detail":"Bu dal yalnız belirli söz öbeğinin düzensiz, çok veya uzun konuşan kişiyi nitelemesine ilişkindir; gerçek odun toplama ve laf taşıma anlamları dışarıda kalır.","branch_image_ar":"حاطب الليل يخلط الرديء والجيد","concept_gloss":"sözünü karıştırıp gereksizce uzatan kimse","contextual_glosses":[{"applicability":"Vurgu konuşmanın düzensizliğinde ve farklı sözlerin birbirine karışmasında olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Konuşma içindeki düzensiz karıştırma niteliğini korur."},"facet_ids":["F001"],"text":"sözünü birbirine karıştıran kimse","usage_role":"contextual"},{"applicability":"Vurgu sözlerin sayıca çokluğunda veya konuşmanın gereğinden fazla uzamasında olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aşırı ve uzun konuşma niteliğini açıkça korur."},"facet_ids":["F002"],"text":"çok ve uzun konuşan kimse","usage_role":"contextual"}],"definition":"Belirli bir söz öbeği içinde, konuşurken düşünceleri ve sözleri birbirine karıştıran ya da gereğinden çok ve uzun konuşan kişiyi niteler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, konuşmasında farklı sözleri veya düşünceleri düzensiz biçimde birbirine karıştırır."},{"facet_id":"F002","role":"specialization","statement":"Aynı niteleme, gereğinden çok konuşan veya sözünü uzun uzadıya sürdüren kişi için de kullanılır."}],"identity_rationale":"Kaynak ifadesi, belirli söz öbeğini konuşmasını karıştıran kişi için verir ve çok ya da uzun konuşmayı aynı kullanımın kapsamları olarak ekler. Dal çerçevesi bu yapıya bağlı anlamı yalın bir kök anlamına dönüştürmeden korur.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"sözünü karıştıran, çok veya uzun konuşan kimse"}],"lexicalization_note":"Anlam yalnız verilen söz öbeğine bağlıdır; konuşmayı karıştırma veya uzatma, yalın biçimin genel anlamı olarak sunulmaz.","neighbor_coverage_note":"Bütün komşu adayları değerlendirildi; konuşmayı ayıklamadan sürdürme, karıştırma, çarpıtma, durum karmaşası ve zarar verici laf taşıma sınırlarını en iyi gösteren beş karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal konuşmanın düzeni ve miktarını, komşu dal ise söylenen şeyin akla gelmiş veya elde bulunmuş olmasını öne çıkarır.","focus_only":"Odak dalda konuşmanın karışık, aşırı veya uzun olması belirleyicidir.","gloss":"aklına geleni söyleme","neighbor_only":"Komşu dalda kişi, doğru ya da yanlış olmasına bakılmaksızın elindeki veya aklına gelen sözü dile getirir.","neighbor_ref":"root_000571/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişinin sözünü yeterince ayıklamadan konuşmasıyla ilgili olabilir."},{"boundary_match":"partial","distinction":"Odak dal bir konuşmacı niteliğidir; komşu dalın çekirdeği ise konuşmanın miktarına bağlı olmayan bozma veya karıştırmadır.","focus_only":"Odak dal, belirli bir söz öbeğiyle konuşan kişinin karışıklığını veya aşırılığını niteler.","gloss":"bozma ve karıştırma","neighbor_only":"Komşu dal, belirli bir anlatımın yorumunda bozma veya karıştırma eylemini bildirir.","neighbor_ref":"root_000197/B004","relation_type":"near_neighbor","shared_zone":"İki dalın ortak alanı, öğelerin düzenini bozacak biçimde karıştırılmasıdır."},{"boundary_match":"field_only","distinction":"Karışık veya uzun konuşma, sözü bilerek çarpıtma ve yalan üretmeyle aynı eylem değildir.","focus_only":"Odak dalda yalan veya kasıt şart değildir; düzensizlik ya da gereksiz uzunluk yeterlidir.","gloss":"sözü eğip çarpıtma","neighbor_only":"Komşu dal, sözü gerçeğinden saptırma, yalan uydurma veya anlaşılmaz kılma yönünü taşır.","neighbor_ref":"root_001388/B007","relation_type":"same_field","shared_zone":"Her iki dal sorunlu ve anlaşılması güç bir konuşma biçimini anlatabilir."},{"boundary_match":"field_only","distinction":"Biri konuşmacıya bağlı bir niteleme, öteki konuşma gerektirmeyen bir durum karışıklığıdır.","focus_only":"Odak dal bir kişinin konuşma davranışını ve söz miktarını niteler.","gloss":"işin karışıp belirsizleşmesi","neighbor_only":"Komşu dal, bir işin ya da durumun karışıp belirsizleşmesini anlatır.","neighbor_ref":"root_000543/B005","relation_type":"same_field","shared_zone":"İki dalda da düzenin bozulması ve öğelerin birbirine karışması düşüncesi vardır."},{"boundary_match":"field_only","distinction":"Sözleri karıştırmak ya da uzatmak ile bir kişi hakkında söz taşıyıp kötülük çıkarmak farklı çekirdeklere sahiptir.","focus_only":"Odak dal düzensiz, çok veya uzun konuşmayı anlatır ve başkasına zarar verme koşulu taşımaz.","gloss":"zarar verici laf taşıma","neighbor_only":"Komşu dal birinin sözünü başkasına taşıyarak onu kötülemeyi ve insanlar arasında zarar doğurmayı anlatır.","neighbor_ref":"root_000335/B003","relation_type":"same_field","shared_zone":"Her iki dal da olumsuz değerlendirilebilen konuşma davranışları alanındadır."}],"source_phrase_ar":"يقال للمخلط في كلامه حاطب ليل (maqayis;ayn;sihah;tahdhib;mufradat)؛ المسهب كحاطب الليل (jamhara)؛ المكثار كحاطب ليل (tahdhib)","source_summary":"Ortak anlam, belirli bir söz öbeğiyle konuşmasını karıştıran kişiyi niteler; çok konuşma ve sözü gereğinden fazla uzatma da bu yapıya bağlı kapsamlar olarak verilir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه المخلط أو المكثار أو المسهب في كلامه أو أمره، تشبيها بحاطب الليل الذي لا يبصر ما يجمع في حبله وربما أصابه مكروه.","what_is_not_ar":"لا يدخل فيه جمع الحطب الحقيقي، ولا السعاية بالنميمة، ولا المثل الذي يكون حاطب فيه علما لشخص."},"support_links":["sup_2c11658836d19a99e374"]},{"boundary":"Dalın çekirdeği insanlar arasında zarar verici söz taşımadır; gerçek yakacak odun ile yalnız karışık veya uzun konuşma bu kapsama girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000335/B003","candidate_links":[{"candidate_id":"cand_9c0924d3873387f55844","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَطَب","morph_features":"STEM|POS:N|LEM:HaTab|ROOT:HTb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:3:2","qac_word_ref":"111:4:3","surface_ar":"حَطَبِ"}],"gloss":"laf taşıyıp kötülük körükleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi hakkında başkasına söz götürülür ve o kişi kötülenerek zarar görmesine yol açılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsanlar arasında laf taşıma eylemi, taşınan bir yük görüntüsüyle adlandırılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı zarar verici eylem, kötülüğü ateş gibi tutuşturup büyütme görüntüsüyle ifade edilir."}}],"root_ar":"ح ط ب","root_id":"root_000335","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi hakkında zarar verici söz taşımayı ve bunun insanlar arasındaki kötülüğü büyütmesini birlikte karşılar.","boundary_detail":"Dalın çekirdeği insanlar arasında zarar verici söz taşımadır; gerçek yakacak odun ile yalnız karışık veya uzun konuşma bu kapsama girmez.","branch_image_ar":"حمل الحطب كناية عن النميمة والسعاية","concept_gloss":"laf taşıyıp kötülük körükleme","contextual_glosses":[{"applicability":"Eylemin hedefi ve sözün götürüldüğü başka kişi açıkça belirtilmek istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözü taşıyanı, hakkında konuşulan kişiyi ve kötüleme eylemini korur."},"facet_ids":["F001"],"text":"birinin sözünü başkasına taşıyıp onu kötülemek","usage_role":"explanatory"},{"applicability":"Kişiden kişiye zarar verici söz götürme eyleminin genel anlatımında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsanlar arasında zarar verici söz aktarma eylemini korur."},"facet_ids":["F002"],"text":"insanlar arasında laf taşımak","usage_role":"general"},{"applicability":"Vurgu, söz taşımanın insanlar arasındaki zararı tutuşturup büyütmesi üzerindeyse kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Zararın özellikle laf taşıma yoluyla doğduğunu tek başına belirtmez.","preserves":"Kötülüğün başlatılması ve büyütülmesi sonucunu korur."},"facet_ids":["F003"],"text":"kötülüğü körüklemek","usage_role":"contextual"}],"definition":"Bir kişi hakkında başkasına söz taşıyarak onu kötülemek ve insanlar arasında zarar doğurmaktır. Bazı kullanımlar bu eylemi yük taşıma veya kötülüğü ateş gibi tutuşturup büyütme görüntüsüyle anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi hakkında başkasına söz götürülür ve o kişi kötülenerek zarar görmesine yol açılır."},{"facet_id":"F002","role":"specialization","statement":"İnsanlar arasında laf taşıma eylemi, taşınan bir yük görüntüsüyle adlandırılır."},{"facet_id":"F003","role":"extension","statement":"Aynı zarar verici eylem, kötülüğü ateş gibi tutuşturup büyütme görüntüsüyle ifade edilir."}],"identity_rationale":"Kaynak ifadesi, bir kişi hakkında başkasına söz taşıyıp onu kötülemeyi açıkça verir; yük taşıma ve güçlü yakacakla ateş tutuşturma görüntülerini de bu eylemin anlatımları olarak gösterir. Dal çerçevesi gerçek odunu çekirdek anlam yapmadan bu mecazi kapsamı doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"laf taşıma ve birini başkasına kötüleme"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"birini başkasına çekiştirip hakkında söz taşımak"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"laf taşımanın kinayeli anlatımı"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"laf taşıyıp insanlar arasındaki kötülüğü körüklemek"}],"lexicalization_note":"Tek başına kullanılan adlandırmanın tanıklanmış mecazi anlamı ile söz taşıma ve kötülüğü körükleme bildiren yapıya bağlı kullanımlar ayrı tutulur.","neighbor_coverage_note":"Bütün komşu adayları değerlendirildi; doğrudan laf taşıma bildiren üç yakın dal, kötülüğü kışkırtan komşu ve söz taşımadan kötüleme bildiren dal sınırı en açık karşılaştırmalar olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Söz taşıma çekirdeğinde çok yakındırlar; odak dalın özel görüntüleri ile komşu dalın daha genel kışkırtma ve bozma kapsamı tam eşdeğerliği engeller.","focus_only":"Odak dal, bir kişi hakkında söz taşımayı yük ve ateş görüntüleriyle anlatan kullanımları da kapsar.","gloss":"laf taşıyıp arayı bozma","neighbor_only":"Komşu dal, insanlar arasını kışkırtıp bozmayı daha genel bir eylem ve kişi niteliği olarak kapsar.","neighbor_ref":"root_000043/B009","relation_type":"near_synonym","shared_zone":"İki dal da insanlar arasında laf taşıyarak veya kışkırtarak ilişkilere zarar verme alanında örtüşür."},{"boundary_match":"partial","distinction":"Eylem büyük ölçüde aynıdır; ancak odak dal zarar gören kişi ve kötülüğü körükleme yönünü, komşu dal ise dolaşma görüntüsünü taşır.","focus_only":"Odak dal, belirli bir kişi hakkında söz taşıma ve kötülüğü büyütme sonucunu öne çıkarır.","gloss":"laf taşıyarak dolaşma","neighbor_only":"Komşu dal, laf taşımayı insanlar arasında yürümek görüntüsüne bağlı olarak anlatır.","neighbor_ref":"root_001427/B004","relation_type":"near_synonym","shared_zone":"Her iki dalın çekirdeğinde insanlar arasında zarar verici söz götürmek vardır."},{"boundary_match":"partial","distinction":"Odak dalın eylem ve sonuç kapsamı, komşu dalın fail nitelemesinden daha geniştir.","focus_only":"Odak dal eylemi, hedef kişiyi ve kötülüğün büyümesini kapsar.","gloss":"laf taşıyan kişi","neighbor_only":"Komşu dal, laf taşıyan kişiyi insanlar arasında dolaşan bir fail olarak niteler.","neighbor_ref":"root_000457/B004","relation_type":"near_synonym","shared_zone":"İki dal da sözleri kişiler arasında taşıyarak zarar veren kimseyi veya eylemi anlatır."},{"boundary_match":"partial","distinction":"Sonuçları yakın olsa da odak dalın zorunlu aracı zarar verici sözdür; komşu dal bu araçla sınırlı değildir.","focus_only":"Odak dalda kötülük, bir kişi hakkında başkasına söz taşıma yoluyla doğar.","gloss":"birinin üzerine kötülük çekme","neighbor_only":"Komşu dal, söz taşıma şartı olmadan birinin üzerine kötülük çekmeyi veya kötülüğü kışkırtmayı kapsar.","neighbor_ref":"root_000016/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir kişiye zarar verecek kötülüğü başlatma veya büyütme sonucuna ulaşabilir."},{"boundary_match":"field_only","distinction":"Birini doğrudan çekiştirmek ile onun hakkında söz taşıyarak insanlar arasını bozmak aynı eylem değildir.","focus_only":"Odak dal sözü bir kişiden başkasına taşıyarak toplumsal zarar oluşturur.","gloss":"birini çekiştirip küçültme","neighbor_only":"Komşu dal bir kişi hakkında küçültücü veya ayıplayıcı biçimde konuşmayı bildirir; sözün başka birinden taşınması gerekmez.","neighbor_ref":"root_001542/B003","relation_type":"same_field","shared_zone":"Her iki dalda da bir kişi hakkında kötüleyici söz söyleme bulunabilir."}],"source_phrase_ar":"حطب فلان بفلان سعى به (maqayis;ayn;tahdhib;mufradat)؛ حمالة الحطب كناية عن النميمة (maqayis;tahdhib;mufradat)؛ الحطب في القرآن النميمة (ayn)؛ يوقد بالحطب الجزل كناية عن ذلك (mufradat)","source_summary":"Ortak anlatım, birini başkasına kötüleyerek hakkında söz taşımayı merkezde tutar; yük taşıma ve ateşi güçlü yakacakla büyütme görüntüleri bu toplumsal zararı anlatır.","sources":["MQ","AY","TA","MU"],"what_is_ar":"يدخل فيه حطب فلان بفلان بمعنى سعى به، وحمل الحطب كناية عن النميمة، وما يشبه إيقاد الشر بين الناس.","what_is_not_ar":"لا يدخل فيه الحطب المعد للإيقاد على الحقيقة إلا إذا كان في عبارة الكناية، ولا خلط الكلام كحاطب ليل."},"support_links":["sup_54c9ccb0d4c2ae467b9f"]},{"boundary":"Bu dal bütün bedene yayılan ileri derecede zayıflığı kuru odun görüntüsüyle niteler; sıradan incelik, yerel karın inceliği ve gerçek odun kapsam dışıdır.","branch_kind":"bare","branch_ref":"root_000335/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَطَب","morph_features":"STEM|POS:N|LEM:HaTab|ROOT:HTb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:3:2","qac_word_ref":"111:4:3","surface_ar":"حَطَبِ"}],"gloss":"kuru odun gibi çok zayıf kimse","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Niteleme, ileri derecede zayıflamış kişiyi veya adamı bildirir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Zayıf bedenin kuru ve ince görünüşü, kuru oduna benzetilerek belirginleştirilir."}}],"root_ar":"ح ط ب","root_id":"root_000335","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İleri derecede zayıf kişiyi ve nitelemenin kuru oduna dayanan görüntüsünü birlikte karşılar.","boundary_detail":"Bu dal bütün bedene yayılan ileri derecede zayıflığı kuru odun görüntüsüyle niteler; sıradan incelik, yerel karın inceliği ve gerçek odun kapsam dışıdır.","branch_image_ar":"الهزال كالحطب اليابس","concept_gloss":"kuru odun gibi çok zayıf kimse","contextual_glosses":[{"applicability":"Benzetme açıklanmadan yalnız kişinin ileri derecedeki zayıflığı aktarılmak istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kuru oduna dayanan görünüş benzetmesini açıkça aktaramaz.","preserves":"Kişinin ileri derecede zayıf olması niteliğini korur."},"facet_ids":["F001"],"text":"aşırı zayıf kimse","usage_role":"general"},{"applicability":"Çok ileri zayıflığı doğal bir Türkçe deyimle vurgulayan anlatı bağlamlarında kullanılır.","error_profile":{"adds":"Deri ve kemik üzerinden yeni bir görüntü ekler.","collision":null,"fit":"displacement","loses":"Kuru odun benzetmesini başka bir beden görüntüsüyle değiştirir.","preserves":"İleri derecede zayıflamış kişi görüntüsünü güçlü biçimde korur."},"facet_ids":["F001"],"text":"bir deri bir kemik kalmış kişi","usage_role":"contextual"}],"definition":"Bir kişinin, bedeni kuru odun gibi görünecek ölçüde ileri derecede zayıf ve kuru görünüşlü olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Niteleme, ileri derecede zayıflamış kişiyi veya adamı bildirir."},{"facet_id":"F002","role":"associated_use","statement":"Zayıf bedenin kuru ve ince görünüşü, kuru oduna benzetilerek belirginleştirilir."}],"identity_rationale":"Kaynak ifadesi iki yalın biçimin de ileri derecede zayıf kişi için kullanıldığını ve bu görünüşü kuru oduna benzettiğini açıkça belirtir. Geçici çerçeve, insanı niteleyen bu anlamı somut yakacak dalından doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"çok zayıf adam"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"çok zayıf kimse"}],"lexicalization_note":"Tanım yalnız yalın biçimlerle bildirilen çok zayıf kişi anlamına dayanır; başka dallardaki söz öbekleri veya mecazi konuşma anlamları buraya taşınmaz.","neighbor_coverage_note":"Bütün komşular değerlendirildi; genel ileri zayıflık, hareketsiz bırakacak zayıflık, hayvana özgü zayıflama, küçük beden ve yerel karın inceliği arasındaki sınırları gösteren beş aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"İleri zayıflıkta örtüşürler; odak dal kuru odun görüntülü insan nitelemesi, komşu dal ise daha geniş katılımcılı bedensel değişimdir.","focus_only":"Odak dal insanı kuru oduna benzeten yalın bir niteleme taşır.","gloss":"etin çekilmesiyle zayıflama","neighbor_only":"Komşu dal, insan veya hayvanda etin çekilmesi, azalması ya da buruşması gibi bedensel süreci de kapsar.","neighbor_ref":"root_000395/B003","relation_type":"near_synonym","shared_zone":"İki dal da etin azalmasıyla ortaya çıkan belirgin zayıflığı anlatır."},{"boundary_match":"partial","distinction":"Komşu dal zayıflığın hareketi engelleyen sonucunu ve deve kapsamını ekler; odak dalda bunlar yoktur.","focus_only":"Odak dal zayıf insanı kuru oduna benzetir ve hareketsizlik sonucu gerektirmez.","gloss":"zayıflıktan yerinde kalan","neighbor_only":"Komşu dal insan veya devenin zayıflıktan yerinde kalacak ölçüde güçsüzleşmesini bildirir.","neighbor_ref":"root_000607/B005","relation_type":"near_synonym","shared_zone":"Her iki dal ileri derecede zayıflamış bir varlığın durumunu niteler."},{"boundary_match":"partial","distinction":"Katılımcı ve görünüş farklıdır: biri kuru oduna benzetilen kişi durumu, öteki koyuna özgü zayıflama eylemidir.","focus_only":"Odak dal bir insanın ileri zayıflık durumunu adlandırır.","gloss":"koyunun zayıflaması","neighbor_only":"Komşu dal özellikle koyunun zayıflama sürecini bildirir.","neighbor_ref":"root_000599/B009","relation_type":"near_neighbor","shared_zone":"Her iki dal canlı bir varlığın belirgin biçimde zayıf hale gelmesiyle ilgilidir."},{"boundary_match":"field_only","distinction":"Kısa veya küçük olmak ileri derecede zayıf olmak değildir; komşunun deveye özgü uzantısı da odak dalın insan sınırını aşar.","focus_only":"Odak dal insandaki ileri zayıflığı kuru odun görünüşüyle niteler.","gloss":"küçük veya kısa beden","neighbor_only":"Komşu dal küçük veya kısa bedeni temel alır ve yalnız bazı kullanımlarda develerin zayıflığına uzanır.","neighbor_ref":"root_000286/B010","relation_type":"same_field","shared_zone":"İki dal bedensel küçüklük ya da zayıflık görüntülerinde yaklaşabilir."},{"boundary_match":"partial","distinction":"Yerel bir karın ya da bel niteliği, bütün bedene yayılan ileri zayıflıkla eşdeğer değildir.","focus_only":"Odak dal bütün kişinin ileri derecede zayıf görünmesini anlatır.","gloss":"ince bel ve çökük karın","neighbor_only":"Komşu dal özellikle karnın içeri çekik veya belin ince olmasını niteler.","neighbor_ref":"root_000440/B001","relation_type":"near_neighbor","shared_zone":"Çökük karın veya ince bel, zayıf bir beden görünüşünün parçası olabilir."}],"source_phrase_ar":"الأحطب الشديد الهزال وكذلك الحطب كأنه شبه بالحطب اليابس (maqayis)؛ يقال للشديد الهزال حطب (ayn)؛ الحطب الرجل الشديد الهزال والأحطب مثله (sihah)","source_summary":"Ortak anlam, bir kişiyi ileri derecede zayıf diye niteler ve bu zayıf, kuru beden görünüşünü kuru oduna benzetir.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه وصف الرجل أو الشخص بالشديد الهزال باسم الحطب أو الأحطب، تشبيها بالحطب اليابس.","what_is_not_ar":"لا يدخل فيه الحطب الحقيقي ولا الاحتطاب ولا كنايات الكلام أو النميمة."},"support_links":[]},{"boundary":"Fiziksel taşıma çekirdektir; ileti ve suç yükü soyut uzantı, sel ve taşıt kullanımları ise taşıyan öznenin değiştiği özel gerçekleşmelerdir.","branch_kind":"mixed_non_bare","branch_ref":"root_000357/B001","candidate_links":[{"candidate_id":"cand_f338f372d0dd70cf44f8","lane":"micro"},{"candidate_id":"cand_9c0924d3873387f55844","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَمَّالَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ham~aAlap|ROOT:Hml|FS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:2:1","qac_word_ref":"111:4:2","surface_ar":"حَمَّالَةَ"}],"gloss":"bir yükü kaldırıp götürme veya üstlenme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesne kaldırılır, bir taşıyıcının üzerinde tutulur ve gerektiğinde başka yere götürülür."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ağır iş, ileti veya suç gibi elle tutulmayan bir yük kişinin üzerine alınmış sayılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sel çer çöpü sürükler, bir gemi veya başka taşıt da içindeki insanları götürür."}}],"root_ar":"ح م ل","root_id":"root_000357","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Somut taşıma çekirdeğini ve kişiye yüklenen soyut sorumluluk uzantısını birlikte anlatan genel karşılıktır.","boundary_detail":"Fiziksel taşıma çekirdektir; ileti ve suç yükü soyut uzantı, sel ve taşıt kullanımları ise taşıyan öznenin değiştiği özel gerçekleşmelerdir.","branch_image_ar":"إقلال المحمول الظاهر","concept_gloss":"bir yükü kaldırıp götürme veya üstlenme","contextual_glosses":[{"applicability":"Nesnenin insanın sırtında veya başında fiziksel olarak götürüldüğü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Fiziksel yükü beden üzerinde tutup götürme işlemini açıkça korur."},"facet_ids":["F001"],"text":"yükü sırtında taşımak","usage_role":"contextual"},{"applicability":"Bir iletiyi ulaştırma, ağır bir işi üzerine alma veya suçun yükünü taşıma bağlamlarına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Soyut yükün kişinin üzerine geçmesi ve onda kalması anlamını korur."},"facet_ids":["F002"],"text":"sorumluluk yükünü üstlenmek","usage_role":"contextual"},{"applicability":"Selin çer çöpü veya benzeri maddeleri akışıyla birlikte götürdüğü bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Suyun taşıyıcı olması ve önündeki maddeleri hareket ettirmesi ilişkisini korur."},"facet_ids":["F003"],"text":"önüne kattığını sürüklemek","usage_role":"contextual"}],"definition":"Bir şeyi kaldırıp sırt, baş, hayvan veya taşıt üzerinde tutarak ya da götürerek yerini değiştirmektir. Aynı taşıma ilişkisi, ağır bir işi veya suç yükünü üstlenmeye ve suyun önüne kattığı maddeleri sürüklemesine uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesne kaldırılır, bir taşıyıcının üzerinde tutulur ve gerektiğinde başka yere götürülür."},{"facet_id":"F002","role":"extension","statement":"Ağır iş, ileti veya suç gibi elle tutulmayan bir yük kişinin üzerine alınmış sayılır."},{"facet_id":"F003","role":"associated_use","statement":"Sel çer çöpü sürükler, bir gemi veya başka taşıt da içindeki insanları götürür."}],"identity_rationale":"Kaynak ifadesi yalnızca sırtta ya da başta görünen bir yükü değil, bir şeyi kaldırıp götürmeyi, soyut bir yükü üstlenmeyi ve suyun ya da taşıtın içindekileri götürmesini birlikte kapsar. Bu nedenle görünür yük çerçevesi korunabilir, ancak dalın tamamını tek başına karşılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi kaldırıp taşımak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"sırtta, başta veya başka bir yerde dıştan taşınan yük"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"selin sürükleyip getirdiği çer çöp ve köpük"}],"lexicalization_note":"Tanım yalın taşıma çekirdeğiyle sınırlı kalır; selin sürüklediği şey ve taşıtla götürme gibi yapıya bağlı kullanımlar ayrı yüzler olarak gösterilir.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; yayımlanan üç karşılaştırma kaldırma, indirme ve taşıma aracıyla karışma ihtimalini en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal kaldırma eylemini ve kaldırabilme gücünü merkez alır; bu dal ise yükün taşıyıcı üzerinde tutulup götürülmesini, ayrıca soyut ve doğal taşıma uzantılarını içerir.","focus_only":"Taşıma, yükü kaldırdıktan sonra üzerinde tutmayı ve götürmeyi de kapsar.","gloss":"kaldırma ile taşıma","neighbor_only":"Komşu dal özellikle taşı veya yükü elle kaldırma, ortak kaldırma ve buna güç yetirme üzerinde durur.","neighbor_ref":"root_000536/B007","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir yük bulunduğu yerden yukarı alınır ve bir taşıyıcı tarafından tutulur."},{"boundary_match":"opposed","distinction":"Hareket yönü ve sonuç karşıttır: burada yük taşıyıcıya alınır ve taşınır, komşuda ise taşıyıcıdan çıkarılıp aşağı konur.","focus_only":"Bu dal yükü alıp taşıyıcının üzerine koymayı ve götürmeyi anlatır.","gloss":"yükleme ile indirme","neighbor_only":"Komşu dal yükü taşıyıcıdan indirmeyi veya yüksekten aşağı bırakmayı anlatır.","neighbor_ref":"root_000336/B001","relation_type":"polarity_pair","shared_zone":"İki dal da yükün taşıyıcıya göre konum değiştirmesini konu eder."},{"boundary_match":"field_only","distinction":"Buradaki çekirdek yükü alma ve götürmedir; komşu dal ise bu işi mümkün kılan araç veya hayvanı gösterir.","focus_only":"Bu dal taşıma eylemini ve taşınan yükü anlatır.","gloss":"taşıma ve taşıma aracı","neighbor_only":"Komşu dal kayış, binek düzeneği ve yük hayvanı gibi taşıma araçlarını adlandırır.","neighbor_ref":"root_000357/B006","relation_type":"same_field","shared_zone":"İki dal aynı yük taşıma durumunun eylem, yük ve araç katmanlarında buluşur."}],"source_phrase_ar":"حملت الشيء أحمله حملا (maqayis)؛ حملت الشئ على ظهرى أحمله حملا (sihah)؛ حمل الشيء يحمله حملا وحملانا (ayn;tahdhib)؛ حملت الثقل والرسالة والوزر حملا (mufradat)؛ حميل السيل ما يحمله من غثائه (maqayis)؛ حميل السيل ما يحمل من الغثاء (ayn;sihah)؛ حميل السيل ما حمله السيل (tahdhib)؛ حملناكم في الجارية (mufradat)","source_summary":"Toplu kaynak anlatımı, kaldırıp götürme çekirdeğini hem somut yüklere hem üstlenilen soyut yüklere uygular; ayrıca selin sürüklediği artıklar ile insanların taşıtta götürülmesini bu ilişkiye bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"حمل الشيء على الظهر أو الرأس أو الدابة؛ حمل الأثقال والرسالة؛ حمل السيل ما يجرفه؛ حمل الناس في مركب","what_is_not_ar":"الحبل في البطن؛ الكفالة؛ أسماء الخروف والبرج"},"support_links":["sup_228cf238a28dc4f1b0e2","sup_54c9ccb0d4c2ae467b9f"]},{"boundary":"Dal gebelikte rahimde gelişen yavruyu ve ağacın meyve vermesini kapsar; dış yük taşıma ya da gebelik olmadan süt gelmesi çekirdeğe dahil değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000357/B002","candidate_links":[{"candidate_id":"cand_c3eb81b161ea6bb9b135","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَمَّالَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ham~aAlap|ROOT:Hml|FS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:2:1","qac_word_ref":"111:4:2","surface_ar":"حَمَّالَةَ"}],"gloss":"gebelik veya ağacın meyve yükü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadın veya dişi hayvan, gelişmekte olan yavruyu rahminde taşır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ağaç, üzerinde oluşup gelişen meyveyi kendi ürünü olarak taşır."}}],"root_ar":"ح م ل","root_id":"root_000357","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem rahimde yavru bulunmasını hem de ağacın meyve taşımasını kapsaması gereken genel anlatımlarda kullanılır.","boundary_detail":"Dal gebelikte rahimde gelişen yavruyu ve ağacın meyve vermesini kapsar; dış yük taşıma ya da gebelik olmadan süt gelmesi çekirdeğe dahil değildir.","branch_image_ar":"الحَمْل الباطن والثمر","concept_gloss":"gebelik veya ağacın meyve yükü","contextual_glosses":[{"applicability":"Kadın veya dişi hayvanın rahminde gelişen yavru bulunduğu bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Rahimde gelişen yavrunun taşınması durumunu eksiksiz korur."},"facet_ids":["F001"],"text":"gebe olmak","usage_role":"general"},{"applicability":"Ağacın üzerinde meyve oluşup geliştiği bitki bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ağacın kendi ürünü olan meyveyi oluşturup üzerinde bulundurmasını korur."},"facet_ids":["F002"],"text":"meyve vermek","usage_role":"contextual"}],"definition":"Bir kadın veya dişinin rahminde yavru geliştirmesi ya da bir ağacın dalında meyve oluşturup taşımasıdır. İki kullanımda da canlı bir varlık kendi içinde veya üzerinde gelişen ürünü taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadın veya dişi hayvan, gelişmekte olan yavruyu rahminde taşır."},{"facet_id":"F002","role":"extension","statement":"Ağaç, üzerinde oluşup gelişen meyveyi kendi ürünü olarak taşır."}],"identity_rationale":"Kaynak ifadesi rahimde taşınan yavru ile ağacın üzerinde taşıdığı meyveyi açıkça aynı dalda verir. Geçici çerçeve bu iki içte veya bitki üzerinde gelişen ürünü doğru biçimde ayırır ve dıştan taşınan yükü kapsam dışında bırakır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"rahimdeki yavru veya ağacın üzerindeki meyve"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"gebe kadın"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"gebe olmadan sütü gelmek"}],"lexicalization_note":"Tanım rahim ve ağaç bağlamlarını ayrı yüzler olarak korur; gebelik olmadan süt gelmesini yalnızca kendi sözlüksel biriminin karşılığında gösterir.","neighbor_coverage_note":"Bütün adaylar incelendi; gebelik, meyve ve ürün taşımama eksenlerindeki üç karşılaştırma dal sınırını diğer adaylardan daha iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Gebelik alanında büyük ölçüde örtüşürler; bu dal ayrıca ağacın meyvesini içerirken komşu dal rahim ve gebelik çevresindeki daha ayrıntılı kullanımlara uzanır.","focus_only":"Bu dal ağaçta oluşan meyveyi de aynı taşıma görüntüsüne dahil eder.","gloss":"gebelik ve meyve","neighbor_only":"Komşu dal gebeliğin zamanı, yeri ve dişiye ilişkin daha geniş rahim söz varlığını içerir.","neighbor_ref":"root_000291/B006","relation_type":"near_synonym","shared_zone":"Her iki dal kadın veya dişi hayvanın rahminde gelişen yavrunun taşınmasını kapsar."},{"boundary_match":"partial","distinction":"Burada belirleyici ilişki ağacın ürünü üzerinde taşımasıdır; komşu dalda meyvenin kendisi ve gelişim evreleri çekirdektir.","focus_only":"Bu dal meyveyi ağacın üzerinde taşıdığı ürün olarak görür ve gebeliği de kapsar.","gloss":"meyve yükü ve olgun meyve","neighbor_only":"Komşu dal meyvenin çıkması, olgunlaşması ve meyveli ağacın adlandırılması üzerinde durur.","neighbor_ref":"root_000205/B001","relation_type":"near_neighbor","shared_zone":"İki dal ağacın üzerinde oluşan meyveyi ortak konu edinir."},{"boundary_match":"opposed","distinction":"Bu dal ürünün mevcut olduğu olumlu durumu, komşu dal ise gebelik ya da meyve bulunmayan karşıt durumu adlandırır.","focus_only":"Bu dal rahimde yavru veya ağaçta meyve bulunmasını bildirir.","gloss":"ürün taşıma ve taşımama","neighbor_only":"Komşu dal dişinin ya da ağacın belirli sürede yavru veya meyve taşımamasını bildirir.","neighbor_ref":"root_000373/B007","relation_type":"polarity_pair","shared_zone":"İki dal dişi canlı veya ağacın yavru ya da meyve taşıma durumunu değerlendirir."}],"source_phrase_ar":"الحمل ما كان في بطن أو على رأس شجر (maqayis;sihah)؛ الحمل ما في البطن (ayn)؛ حمل الشجر (ayn)؛ حملت المرأة والشجرة حملا (sihah)؛ حملت المرأة حبلت وكذا حملت الشجرة (mufradat)؛ حملت حملا خفيفا (mufradat)","source_summary":"Kaynakların ortak anlatımı rahimdeki yavru ile ağacın meyvesini, canlı taşıyıcının içinde veya üzerinde gelişen ürünler olarak aynı anlam alanında toplar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الحمل في بطن المرأة أو الناقة؛ حمل الشجرة وثمرها","what_is_not_ar":"الحمل على الظهر؛ الخروف؛ الحمالة"},"support_links":["sup_02e67034803912d704c0"]},{"boundary":"Bu dal yalnızca belirtilen görev, güven, ileti ve suç yapılarında geçerlidir; genel fiziksel taşıma anlamına genişletilmez.","branch_kind":"collocation","branch_ref":"root_000357/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَمَّالَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ham~aAlap|ROOT:Hml|FS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:2:1","qac_word_ref":"111:4:2","surface_ar":"حَمَّالَةَ"}],"gloss":"görev veya suç yükünü üstlenme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişiye bir iletiyi ulaştırma veya güvenilen bir işi yerine getirme görevi verilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yüklenen görevi gerçekten yerine getirmek ile onu terk ederek güveni bozmak karşıt sonuçlar olarak ayrılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İşlenen suçun sonucu, kişinin üzerinde kalan ağır ve kötü bir yük gibi kavranır."}}],"root_ar":"ح م ل","root_id":"root_000357","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiye güvenilen iş ya da ileti verildiğinde veya suçun sonucu onun üzerinde kaldığında kullanılan kapsayıcı karşılıktır.","boundary_detail":"Bu dal yalnızca belirtilen görev, güven, ileti ve suç yapılarında geçerlidir; genel fiziksel taşıma anlamına genişletilmez.","branch_image_ar":"تحمّل الأمانة والوزر","concept_gloss":"görev veya suç yükünü üstlenme","contextual_glosses":[{"applicability":"Bir iletiyi ulaştırma veya güvenilen işi yapma yükümlülüğünün kişiye verildiği bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Görevin kişiye verilmesini ve gereğini yerine getirme sorumluluğunu korur."},"facet_ids":["F001"],"text":"verilen görevi üstlenmek","usage_role":"general"},{"applicability":"Kişinin kendisine verilen işi yapmayıp sorumluluğunu terk ettiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yükümlülüğün yerine getirilmemesiyle güvenin bozulması sonucunu korur."},"facet_ids":["F002"],"text":"güveni boşa çıkarmak","usage_role":"contextual"},{"applicability":"İşlenen suçun kötü sonucunun kişiye bağlandığı anlatımlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Suçun sonucunun kişiden ayrılmayan ağır bir yük sayılmasını korur."},"facet_ids":["F003"],"text":"suçun yükünü taşımak","usage_role":"contextual"}],"definition":"Bir kişiye ileti, görev veya güvenilen bir iş yüklenmesi ve kişinin bunun gereklerini yerine getirmekle sorumlu olmasıdır. Görevi terk etmek güveni bozma, işlenen suç ise kişinin üzerinde kalan ağır bir yük olarak anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişiye bir iletiyi ulaştırma veya güvenilen bir işi yerine getirme görevi verilir."},{"facet_id":"F002","role":"source_variant","statement":"Yüklenen görevi gerçekten yerine getirmek ile onu terk ederek güveni bozmak karşıt sonuçlar olarak ayrılır."},{"facet_id":"F003","role":"extension","statement":"İşlenen suçun sonucu, kişinin üzerinde kalan ağır ve kötü bir yük gibi kavranır."}],"identity_rationale":"Kaynak ifadesi yalnızca görevi üstlenmeyi değil, onu yerine getirme yükümlülüğünü, yerine getirmeyerek güveni bozmayı ve işlenen suçun yükünü taşımayı da bildirir. Geçici başlık kullanılabilir, fakat başarıyla yerine getirme ile ihmal veya suç sonucu doğan yük birbirinden ayrılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"suçun ve kötülüğün yükünü üzerine almak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"güvenilerek verilen işi üstlenmek veya onu yerine getirmemek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"iletiyi ulaştırma görevini üstlenmek"}],"lexicalization_note":"Tanım verilen görev, güven ve suç yükü yapılarıyla açıkça bağlıdır; bunlardan bağımsız yalın bir taşıma anlamı çıkarılmaz.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; suç yükü, görevin yüklenmesi ve yükten arınma karşılaştırmaları bu yapıya bağlı dalın sınırlarını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Suç yükü bağlamında yakınlaşırlar; bu dal ayrıca verilen görevin yapılması veya terk edilmesi ilişkisini içerirken komşu dal yükün ağırlığını merkez alır.","focus_only":"Bu dal güvenilen iş ve ileti görevini üstlenme ile bunları yerine getirmemeyi de kapsar.","gloss":"sorumluluk yükü ve ağır suç yükü","neighbor_only":"Komşu dal ağır yük ve suç anlamındaki yükün kendisini daha doğrudan adlandırır.","neighbor_ref":"root_001643/B002","relation_type":"near_synonym","shared_zone":"İki dalda da suç veya ağır sorumluluk kişinin üzerinde taşınan bir yük olarak kavranır."},{"boundary_match":"partial","distinction":"Komşu dal yükümlülüğü veren işlemi, bu dal ise yükümlülüğü alan kişinin sorumluluğunu ve başarısızlığının sonucunu anlatır.","focus_only":"Bu dal yüklenmiş görevi kişinin üstlenmesi, yerine getirmesi veya terk etmesi sonucuna odaklanır.","gloss":"görevi üstlenme ve görevi yükleme","neighbor_only":"Komşu dal işi ya da buyruğu bir kişiye bağlayan yükleme ve zorunlu kılma eylemine odaklanır.","neighbor_ref":"root_001249/B004","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir iş veya yükümlülük belirli bir kişiye bağlanır."},{"boundary_match":"opposed","distinction":"Burada bağ ve yük sürer; komşu dalda kişi o bağdan çıkar ve üzerinde sorumluluk kalmaz.","focus_only":"Bu dal görev, güven veya suçtan doğan yükün kişi üzerinde kalmasını bildirir.","gloss":"yük altında olma ve yükten kurtulma","neighbor_only":"Komşu dal kişinin suçtan ya da yükümlülükten arınmış ve bağı kopmuş olmasını bildirir.","neighbor_ref":"root_000436/B006","relation_type":"polarity_pair","shared_zone":"İki dal kişinin bir sorumluluk veya suçla bağlı olup olmadığını değerlendirir."}],"source_phrase_ar":"حملت الثقل والرسالة والوزر حملا (mufradat)؛ كلفوا أن يتحملوها أي يقوموا بحقها فلم يحملوها (mufradat)؛ حمل الأمانة أي خيانتها وترك أدائها (tahdhib)؛ من باء بالإثم يسمى حاملا للإثم (tahdhib)؛ وساء لهم يوم القيامة حملا أي وزرا (sihah)","source_summary":"Toplu anlatım bir görevin kişiye verilmesini, onun hakkını yerine getirme zorunluluğunu ve bunun terk edilmesiyle doğan güven bozulmasını ayırır; suç da taşıyan kişiye bağlanan bir yük olarak sunulur.","sources":["SI","TA","MU"],"what_is_ar":"ما يحمَّله الإنسان من رسالة أو أمانة أو وزر أو إصر؛ القيام بحق المحمول أو خيانته","what_is_not_ar":"الحمل الحسي على الظهر؛ الحبل في البطن؛ الكفالة المالية"},"support_links":[]},{"boundary":"Çekirdek sıradan bir yük taşımak değil, başkasının ödeme veya hak borcunu güvence vererek kendi üzerine almaktır.","branch_kind":"mixed_non_bare","branch_ref":"root_000357/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَمَّالَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ham~aAlap|ROOT:Hml|FS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:2:1","qac_word_ref":"111:4:2","surface_ar":"حَمَّالَةَ"}],"gloss":"başkasının borcunu üstlenip güvence verme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya topluluk başkasına ait kan bedelini ya da mali yükü kendi üzerine alır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Üstlenme, borcun veya hakkın yerine getirileceğine dair güvence verme işlevi görür."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Güvence veren kişi, hakkın yükünü asıl borçluyla birlikte taşıyan sorumlu taraf sayılır."}}],"root_ar":"ح م ل","root_id":"root_000357","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kan bedeli, ödeme yükü veya başka bir hakkın başkası adına üstlenilip güvenceye bağlandığı durumları kapsar.","boundary_detail":"Çekirdek sıradan bir yük taşımak değil, başkasının ödeme veya hak borcunu güvence vererek kendi üzerine almaktır.","branch_image_ar":"الحمالة والكفالة","concept_gloss":"başkasının borcunu üstlenip güvence verme","contextual_glosses":[{"applicability":"Bir kişi veya topluluğun başkaları adına kan bedelini ödemeyi üzerine aldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kan bedelinin asıl yükümlü dışındaki kişi veya toplulukça üstlenilmesini korur."},"facet_ids":["F001"],"text":"kan bedelini üstlenmek","usage_role":"contextual"},{"applicability":"Bir borcun veya hakkın yerine getirileceğini başkası adına güvence altına alma bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yükün güvence veren kişiye bağlanmasını ve ödeme sorumluluğunu korur."},"facet_ids":["F002","F003"],"text":"ödeme için güvence vermek","usage_role":"general"}],"definition":"Bir kişinin veya topluluğun başkasına düşen kan bedelini ya da mali yükü üstlenip ödenmesini güvence altına almasıdır. Bu yükü borçluyla birlikte taşıyan kişi, hakkın yerine getirilmesinden sorumlu güvence verendir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya topluluk başkasına ait kan bedelini ya da mali yükü kendi üzerine alır."},{"facet_id":"F002","role":"specialization","statement":"Üstlenme, borcun veya hakkın yerine getirileceğine dair güvence verme işlevi görür."},{"facet_id":"F003","role":"extension","statement":"Güvence veren kişi, hakkın yükünü asıl borçluyla birlikte taşıyan sorumlu taraf sayılır."}],"identity_rationale":"Kaynak ifadesi bir kişinin ya da topluluğun başkası adına kan bedeli veya ödeme yükü üstlenmesini, buna güvence vermesini ve hak sahibiyle borçlu arasındaki yükü paylaşan güvence kişisini açıkça bir arada sunar. Geçici çerçeve bu hukuki ve mali ilişkiyi doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"uzlaşma için üstlenilen kan bedeli veya ödeme yükü"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"başkası adına güvence vermek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"borcun ödenmesini güvence altına alan kişi"}],"lexicalization_note":"Tanım kan bedeli, ödeme güvencesi ve güvence kişisi gibi belirtilmiş biçimlerle sınırlıdır; yalın fiziksel taşıma anlamına genişletilmez.","neighbor_coverage_note":"Tüm komşu adayları incelendi; genel güvence, kan bedelini ödeme ve mali yükümlülükle kurulan üç ayrım bu dalın işlem ve aşama sınırlarını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Genel güvence verme alanında örtüşürler; bu dalın ayırt edici yönü kan bedeli ve toplulukça üstlenilen mali yüklerdir.","focus_only":"Bu dal özellikle kan bedelini veya topluluk adına ödeme yükünü üstlenmeyi içerir.","gloss":"ödeme yükünü güvenceyle üstlenme","neighbor_only":"Komşu dal yazılı söz, başka biri adına kabul ve daha genel güvence türlerine uzanır.","neighbor_ref":"root_001198/B008","relation_type":"near_synonym","shared_zone":"İki dalda da bir kişi başkasıyla ilgili borç veya yükümlülüğün yerine getirilmesine güvence verir."},{"boundary_match":"partial","distinction":"Burada belirleyici aşama güvenceyle üstlenmedir; komşuda ise borcun fiilen ödenmesi veya tahsil edilmesi tamamlayıcı aşamadır.","focus_only":"Bu dal ödemeyi yapma sözünü ve yükü başkası adına üstlenmeyi merkez alır.","gloss":"kan bedelini üstlenme ve ödeme","neighbor_only":"Komşu dal kan bedelinin fiilen verilmesi veya alınması eylemini merkez alır.","neighbor_ref":"root_001637/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal kan bedelinin hak sahibine ulaştırılması gereken mali ilişkiyi konu eder."},{"boundary_match":"partial","distinction":"Bu dal başkası adına güvence vererek üstlenmeyi gerektirir; komşu dalda mali yük çeşitli nedenlerle doğabilir ve güvence ilişkisi şart değildir.","focus_only":"Bu dal başkasının mali yükünü gönüllü veya uzlaştırıcı biçimde güvenceyle üzerine alır.","gloss":"güvence ve mali yükümlülük","neighbor_only":"Komşu dal zarar, borç veya güvence nedeniyle kişiye ödeme zorunluluğu doğmasını daha geniş biçimde kapsar.","neighbor_ref":"root_001081/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da belirli bir paranın ödenmesi kişiye bağlanan zorunlu bir yük haline gelir."}],"source_phrase_ar":"الحمالة أن يحمل الرجل دية ثم يسعى عليها والضمان حمالة (maqayis)؛ الحمالة الدية يحملها قوم عن قوم (ayn)؛ الحمالة ما يحمله القوم من الديات (jamhara)؛ حملت به حمالة أي كفلت (sihah)؛ الحميل الكفيل (jamhara;tahdhib;mufradat)؛ الحميل لكونه حاملا للحق مع من عليه الحق (mufradat)","source_summary":"Kaynaklar kan bedelinin kişi veya toplulukça üstlenilmesini ödeme güvencesiyle birleştirir ve güvence veren kişiyi hakkın yükünü asıl sorumluyla paylaşan taraf olarak açıklar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"تحمل الديات والغرامات؛ الكفالة والضمان؛ حمل الحق مع صاحبه","what_is_not_ar":"مجرد الحمل على الظهر؛ حميل السيل؛ الحبل"},"support_links":[]},{"boundary":"Dal, taşınma, bulunma ya da sonradan bir aileye bağlanma nedeniyle soyu doğrulanamayan kişiyi kapsar; genel çocukluk veya sıradan akrabalık anlamı taşımaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000357/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَمَّالَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ham~aAlap|ROOT:Hml|FS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:2:1","qac_word_ref":"111:4:2","surface_ar":"حَمَّالَةَ"}],"gloss":"soy bağı doğrulanamayan getirilmiş çocuk","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bulunmuş, başka yerden getirilmiş veya bir aileye sonradan bağlanmış olduğu için soyu kesin olarak bilinmez."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynak anlatımı terk edilmiş çocuk, yabancı yerden getirilen çocuk, anne karnındayken annesiyle başka bir ülkeden getirilen çocuk ve başkasına ait sayılan çocuk görünümlerini birlikte verir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Soyun doğrulanamaması, kişinin miras hakkının nasıl belirleneceği sorununa bağlanır."}}],"root_ar":"ح م ل","root_id":"root_000357","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Terk edilme, başka yerden getirilme veya sonradan bir aileye bağlanma yüzünden gerçek soyu belirsiz kalan kişi için kullanılır.","boundary_detail":"Dal, taşınma, bulunma ya da sonradan bir aileye bağlanma nedeniyle soyu doğrulanamayan kişiyi kapsar; genel çocukluk veya sıradan akrabalık anlamı taşımaz.","branch_image_ar":"الحميل المحمول في النسب","concept_gloss":"soy bağı doğrulanamayan getirilmiş çocuk","contextual_glosses":[{"applicability":"Terk edilmişken bulunan ve onu bulanlar tarafından büyütülen çocuk görünümünde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çocuğun terk edilmişken bulunmasını ve yeni çevrede büyütülmesini korur."},"facet_ids":["F001","F002"],"text":"bulunup büyütülen çocuk","usage_role":"contextual"},{"applicability":"Küçükken ülkesinden getirildiği veya başka bir aileye bağlandığı için soyu kanıtlanamayan kişiye uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yer değiştirme ile doğrulanamayan soy arasındaki belirleyici bağı korur."},"facet_ids":["F001","F002"],"text":"soyu belirsiz getirilmiş kişi","usage_role":"explanatory"}],"definition":"Terk edilip bulunarak büyütülen, küçükken başka yerden getirilen, anne karnındayken annesiyle başka bir ülkeden getirilen veya sonradan bir aileye bağlanan ve bu yüzden gerçek soy bağı doğrulanamayan kişidir. Miras söz konusu olduğunda da belirleyici sorun bu soy belirsizliğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bulunmuş, başka yerden getirilmiş veya bir aileye sonradan bağlanmış olduğu için soyu kesin olarak bilinmez."},{"facet_id":"F002","role":"source_variant","statement":"Kaynak anlatımı terk edilmiş çocuk, yabancı yerden getirilen çocuk, anne karnındayken annesiyle başka bir ülkeden getirilen çocuk ve başkasına ait sayılan çocuk görünümlerini birlikte verir."},{"facet_id":"F003","role":"associated_use","statement":"Soyun doğrulanamaması, kişinin miras hakkının nasıl belirleneceği sorununa bağlanır."}],"identity_rationale":"Kaynak ifadesi terk edilip bulunarak büyütülen çocuğu, küçükken ülkesinden getirilen kişiyi, kökeni doğrulanamayan çocuğu ve başkasına ait sayılan çocuğu aynı ad altında toplar. Geçici çerçeve doğrudur, ancak ortak nokta yalnızca küçükken taşınmak değil, bu koşullar yüzünden soy bağının belirsiz veya tartışmalı kalmasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"terk edilmiş, başka yerden getirilmiş veya soyu doğrulanamayan çocuk"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"soyu doğrulanamayan kişinin mirası"}],"lexicalization_note":"Tanım belirli kişi adı ve miras yapısıyla sınırlı soy belirsizliğini korur; yalın taşıma veya genel çocuk anlamına genişletilmez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; bulunmuş çocuk, başka soya bağlanmış kişi ve soya bağlama eylemiyle yapılan karşılaştırmalar soy belirsizliğinin sınırını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bulunmuş çocuk görünümünde örtüşürler; bu dal yerinden getirilme ve sonradan aileye bağlanma gibi daha geniş soy belirsizliği nedenlerini de içerir.","focus_only":"Bu dal başka ülkeden getirilmiş veya başkasına ait sayılmış soyu belirsiz kişileri de kapsar.","gloss":"bulunmuş çocuk ve soyu belirsiz çocuk","neighbor_only":"Komşu dal annesi tarafından bırakılıp başkalarınca bulunan çocuğa özel olarak odaklanır.","neighbor_ref":"root_001466/B007","relation_type":"near_synonym","shared_zone":"İki dal terk edilmişken bulunan ve öz ailesi kesin bilinmeyen çocuğu kapsar."},{"boundary_match":"partial","distinction":"Komşuda yanlış veya sonradan kurulmuş bağ belirleyicidir; bu dalda ise bulunma ya da taşınma sonucunda kökenin yalnızca doğrulanamaması da yeterlidir.","focus_only":"Bu dal bulunmuş veya başka yerden getirilmiş olup soyu yalnızca belirsiz kalan kişiyi de içerir.","gloss":"soyu belirsiz ve başka soya bağlanmış çocuk","neighbor_only":"Komşu dal özellikle gerçek kökeni dışında bir aileye bağlanan kişiyi adlandırır.","neighbor_ref":"root_000747/B010","relation_type":"near_synonym","shared_zone":"Her iki dal kişinin gerçek aile kökeniyle toplumda bağlandığı kökenin uyuşmamasını kapsayabilir."},{"boundary_match":"partial","distinction":"Burada odak kişinin belirsiz konumudur; komşuda ise o kişiyi başka bir soya bağlayan işlem veya iddia çekirdektir.","focus_only":"Bu dal soy belirsizliği taşıyan kişinin durumunu ve bundan doğan miras sorununu anlatır.","gloss":"soy belirsizliği ve soya bağlama","neighbor_only":"Komşu dal bir kişiyi belirli bir topluluğa veya gerçek babasından başkasına bağlama eylemini anlatır.","neighbor_ref":"root_001347/B002","relation_type":"near_neighbor","shared_zone":"İki dal gerçek köken ile kişiye yakıştırılan aile bağı arasındaki uyuşmazlık alanında buluşur."}],"source_phrase_ar":"الحميل المنبوذ يحمل فيربى (ayn;tahdhib)؛ الحميل الولد في بطن الأم إذا أخذت من أرض الشرك (ayn;tahdhib)؛ الحميل الذي يحمل من بلده صغيرا ولم يولد في الإسلام (sihah)؛ الحميل الدعي (maqayis;sihah)؛ ميراث الحميل لمن لا يتحقق نسبه (mufradat)","source_summary":"Toplu kaynak anlatımı, terk edilmiş, küçükken başka yerden getirilmiş, anne karnındayken annesiyle başka bir ülkeden getirilmiş veya aileye sonradan bağlanmış kişileri doğrulanamayan soy ortaklığında toplar ve bunun miras bakımından sonuç doğurduğunu belirtir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"المنبوذ أو الغريب أو الولد المحمول صغيرا؛ الدعي أو من لا يتحقق نسبه","what_is_not_ar":"الكفيل؛ حميل السيل؛ الحمل في البطن على جهة الحبل المعتاد"},"support_links":[]},{"boundary":"Dal taşınan nesnenin kendisini değil, kılıcı, yolcuyu veya yükü taşıyan kayış, düzenek ve hayvanı adlandırır.","branch_kind":"mixed_non_bare","branch_ref":"root_000357/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَمَّالَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ham~aAlap|ROOT:Hml|FS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:2:1","qac_word_ref":"111:4:2","surface_ar":"حَمَّالَةَ"}],"gloss":"taşıma kayışı, binek düzeneği veya yük hayvanı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"specialization","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kılıç, omuzdan veya bedenden geçen bir kayışla taşınır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvanın üzerine yerleştirilen iki yanlı veya örtülü düzenek bir ya da daha çok yolcuyu taşır."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Deve, eşek veya başka bir hayvan yük taşımak üzere ayrılmış taşıyıcıdır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yüklü hayvanlar üzerlerindeki düzeneklerle birlikte veya armağan amacıyla verilen binek olarak adlandırılabilir."}}],"root_ar":"ح م ل","root_id":"root_000357","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Taşınan şeye göre kayış, hayvan üstü yolcu düzeneği veya yük taşımaya ayrılmış hayvan türlerini birlikte gösterir.","boundary_detail":"Dal taşınan nesnenin kendisini değil, kılıcı, yolcuyu veya yükü taşıyan kayış, düzenek ve hayvanı adlandırır.","branch_image_ar":"أداة الحمل ومركوبه","concept_gloss":"taşıma kayışı, binek düzeneği veya yük hayvanı","contextual_glosses":[{"applicability":"Kılıcı bedene bağlayıp taşımaya yarayan kayışın adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kılıcın kayışla asılarak bedende taşınması işlevini korur."},"facet_ids":["F001"],"text":"kılıç askısı","usage_role":"contextual"},{"applicability":"Deve veya başka bir hayvan üzerinde yolcu taşıyan iki yanlı ya da örtülü düzeneğe uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Düzeneğin hayvan üzerinde kurulmasını ve yolcu taşımasını korur."},"facet_ids":["F002"],"text":"hayvan üstü yolcu düzeneği","usage_role":"explanatory"},{"applicability":"Deve, eşek veya başka bir hayvanın eşya taşımak üzere ayrıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın yük taşımaya ayrılmış canlı taşıyıcı olmasını korur."},"facet_ids":["F003"],"text":"yük hayvanı","usage_role":"general"}],"definition":"Kılıcı bedene bağlayan kayış, hayvan üzerinde yolcu taşıyan düzenek veya yük taşımaya ayrılmış hayvan gibi taşıma işini sağlayan araçtır. Bazı biçimler yüklü hayvan topluluğunu ya da özellikle armağan edilen bineği de adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"specialization","statement":"Kılıç, omuzdan veya bedenden geçen bir kayışla taşınır."},{"facet_id":"F002","role":"core","statement":"Hayvanın üzerine yerleştirilen iki yanlı veya örtülü düzenek bir ya da daha çok yolcuyu taşır."},{"facet_id":"F003","role":"core","statement":"Deve, eşek veya başka bir hayvan yük taşımak üzere ayrılmış taşıyıcıdır."},{"facet_id":"F004","role":"extension","statement":"Yüklü hayvanlar üzerlerindeki düzeneklerle birlikte veya armağan amacıyla verilen binek olarak adlandırılabilir."}],"identity_rationale":"Kaynak ifadesi kılıcı taşımaya yarayan kayışı, hayvan üzerine kurulan yolcu düzeneğini, yük taşımaya ayrılan hayvanları ve bunların üzerindeki yük veya yolcu düzenini açıkça sıralar. Geçici araç ve binek çerçevesi bu ortak taşıma işlevini doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kılıç askısı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"deve üzerinde yolcu taşıyan iki yanlı düzenek"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yük taşımaya ayrılmış deve veya başka hayvan"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yükleri veya yolcu düzenekleriyle birlikte develer"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"armağan olarak verilen binek hayvanı"}],"lexicalization_note":"Tanım kayış, yolcu düzeneği, yük hayvanı ve armağan için verilen binek gibi ayrı biçimlere bağlıdır; bunlar tek bir yalın araç adı sayılmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; deve üzerindeki düzenek, örtülü binek ve semerle yapılan üç karşılaştırma araç türleri arasındaki sınırı yeterince açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Hayvan üstü düzenek görünümünde yakınlaşırlar; bu dalın kapsamı kayış ve taşıyıcı hayvanlara uzanırken komşu dal doğrudan deve üzerindeki düzeneğe yoğunlaşır.","focus_only":"Bu dal kılıç askısını, yük hayvanlarını ve armağan edilen bineği de kapsar.","gloss":"yolcu düzeneği ve deve semeri","neighbor_only":"Komşu dal özellikle devenin sırtındaki semer veya benzeri binek düzeneğini adlandırır.","neighbor_ref":"root_000551/B002","relation_type":"near_synonym","shared_zone":"İki dal deve üzerinde kurulan ve insan ya da yük taşımaya yarayan düzeneği kapsar."},{"boundary_match":"partial","distinction":"Komşu dal belirli bir örtülü binek türünü merkez alır; bu dal onu daha geniş taşıma aracı ailesinin yalnızca bir görünümü olarak içerir.","focus_only":"Bu dal taşıma araçlarını kılıç kayışı ve yük hayvanına kadar genişletir.","gloss":"genel taşıma aracı ve örtülü binek","neighbor_only":"Komşu dal yolcuyu ve devenin hörgücünü çevreleyen belirli örtülü binek düzeneklerini ayrıntılandırır.","neighbor_ref":"root_000374/B004","relation_type":"near_neighbor","shared_zone":"İki dal hayvan üzerinde yolcu taşımak için hazırlanan örtülü veya iki yanlı düzeneği içerir."},{"boundary_match":"field_only","distinction":"Bu dalın çekirdeği farklı taşıma araçlarının işlevsel ailesidir; komşu dal semerin kendisini ve ona bağlı işi adlandırır.","focus_only":"Bu dal yolcu düzeneğinin yanında kayış ve yük taşıyan hayvanı da kapsar.","gloss":"taşıma düzeneği ve semer","neighbor_only":"Komşu dal hayvan semerini, semerleme işini ve bunun yapım mesleğini kapsar.","neighbor_ref":"root_000693/B002","relation_type":"same_field","shared_zone":"İki dal hayvanın sırtına yerleştirilen taşıma veya binme donanımı alanında buluşur."}],"source_phrase_ar":"الحمالة والمحمل علاقة السيف (maqayis;ayn;sihah)؛ حمالة السيف وحميلته والجمع الحمائل (jamhara)؛ المحمل الشقان على البعير يحمل فيهما نفسان (ayn)؛ المحمل واحد محامل الحاج (sihah)؛ الحمولة الإبل تحمل عليها الأثقال (maqayis;ayn)؛ الحمولة ما احتمل عليه الحي من بعير أو حمار أو غيره (sihah;tahdhib)","source_summary":"Kaynaklar aynı taşıma işlevi çevresinde kılıç kayışını, yolcu düzeneğini ve yük hayvanını ayırır; ayrıca yüklü hayvan topluluğu ile armağan için verilen bineğe özgü adları belirtir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"علاقة السيف ومحمله وحمالته؛ الهودج والمحمل؛ الحمولة والحمول مما يحمل عليه","what_is_not_ar":"الأثقال المحمولة أنفسها؛ الحبل؛ الكفالة"},"support_links":[]},{"boundary":"Güçlük altında çabalama, birine doğru yüklenme ve güvenilir dayanak aynı biçim ailesindedir, fakat birbirinin yerine geçmeyen ayrı kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000357/B007","candidate_links":[{"candidate_id":"cand_1596ab352af9b9b588a8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَمَّالَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ham~aAlap|ROOT:Hml|FS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:2:1","qac_word_ref":"111:4:2","surface_ar":"حَمَّالَةَ"}],"gloss":"zorlanarak yüklenme, eğilme veya dayanak olma","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi güçlüğe rağmen bir işi üstlenir ve onu yapmak için kendini zorlar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yolculuk sırasında kişi gücünü zorlayarak kendini yorar."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bir yapıda kişi başkasına doğru eğilir veya onun üzerine yüklenir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Adlaşmış biçim, güvenilen ve gerektiğinde dayanılan kişi ya da şeyi gösterir."}}],"root_ar":"ح م ل","root_id":"root_000357","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu biçim ailesindeki güçlük altında çabalama, birine doğru yüklenme ve güvenilir dayanak yüzlerini birlikte özetler.","boundary_detail":"Güçlük altında çabalama, birine doğru yüklenme ve güvenilir dayanak aynı biçim ailesindedir, fakat birbirinin yerine geçmeyen ayrı kullanımlardır.","branch_image_ar":"التحامل والمشقة","concept_gloss":"zorlanarak yüklenme, eğilme veya dayanak olma","contextual_glosses":[{"applicability":"Kişinin güç bir işi yapmak veya yola devam etmek için kendi gücünü zorladığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşin güçlüğünü ve kişinin kendi gücünü bilinçli biçimde zorlamasını korur."},"facet_ids":["F001","F002"],"text":"güçlüğe rağmen kendini zorlamak","usage_role":"general"},{"applicability":"Kişinin bedenen veya yönelim bakımından başka birine doğru yüklendiği yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hareketin başka bir kişiye doğru yönelmesini ve ağırlık vermesini korur."},"facet_ids":["F003"],"text":"birinin üzerine doğru eğilmek","usage_role":"contextual"},{"applicability":"Bir kişi veya şeyin güvenilip dayanılacak destek olarak değerlendirildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Güvenme ve gerektiğinde destek alma işlevini korur."},"facet_ids":["F004"],"text":"güvenilir dayanak","usage_role":"contextual"}],"definition":"Kişinin güç bir işi zorlanarak yapması veya yolculukta kendini son sınırına kadar itmesidir. Başka yapılarda birine doğru eğilip yüklenmeyi ya da güvenilip dayanılan kişi veya şeyi bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi güçlüğe rağmen bir işi üstlenir ve onu yapmak için kendini zorlar."},{"facet_id":"F002","role":"specialization","statement":"Yolculuk sırasında kişi gücünü zorlayarak kendini yorar."},{"facet_id":"F003","role":"source_variant","statement":"Belirli bir yapıda kişi başkasına doğru eğilir veya onun üzerine yüklenir."},{"facet_id":"F004","role":"source_variant","statement":"Adlaşmış biçim, güvenilen ve gerektiğinde dayanılan kişi ya da şeyi gösterir."}],"identity_rationale":"Kaynak ifadesi güçlüğe rağmen bir işe girişme ve yolculukta kendini zorlama yanında, birine doğru eğilme ile güvenilip dayanılan şey anlamlarını da içerir. Bunları tek bir güçlük kavramında birleştirmek yanıltıcı olacağından dal, yapıya bağlı üç ayrı yüz olarak yeniden çerçevelenmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"güç bir işe zorlanarak girişmek"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yolculukta kendini sonuna kadar zorlamak"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"birinin üzerine doğru eğilmek veya yüklenmek"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"güvenilip dayanılan kişi veya şey"}],"lexicalization_note":"Tanım yalın bir kök anlamı varsaymaz; kendini zorlama, birine eğilme ve dayanak olma yüzlerini kendi yapıları içinde ayrı tutar.","neighbor_coverage_note":"Bütün adaylar gözden geçirildi; çaba, yaşanan güçlük ve kapasiteyi aşan dış yükle yapılan üç ayrım, dalın güçlük yüzünü en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çabalama yüzünde yakındırlar; bu dal belirli yapılarda kendini yükleme biçimini anlatır ve ayrıca çabayla ilgisiz eğilme ile dayanak yüzlerini taşır.","focus_only":"Bu dal ayrıca birine doğru eğilme ve güvenilir dayanak anlamlarını içerir.","gloss":"güçlük altında kendini zorlama","neighbor_only":"Komşu dal güç yetirme, bütün çabayı harcama ve yaşam darlığı gibi daha genel güçlük alanlarına uzanır.","neighbor_ref":"root_000268/B001","relation_type":"near_synonym","shared_zone":"İki dalda kişi güç bir işi tamamlamak için elindeki gücü kullanır ve sıkıntıya katlanır."},{"boundary_match":"partial","distinction":"Burada odak kişinin kendini zorlayarak harekete devam etmesidir; komşuda odak kişinin yaşadığı güçlük ve ağırlıktır.","focus_only":"Bu dal kişinin güçlüğe rağmen işi üstlenip kendini zorlamasını eylem olarak bildirir.","gloss":"kendini zorlama ve çekilen güçlük","neighbor_only":"Komşu dal yol veya işte hissedilen güçlük, ağırlık ve yorgunluk durumunun kendisini bildirir.","neighbor_ref":"root_000807/B003","relation_type":"near_neighbor","shared_zone":"İki dal zorlu iş veya yolculuk sırasında kişinin gücünün sınanması alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dal öznenin kendi çabasını artırmasını, komşu dal ise dışarıdan yüklenen işin öznenin kapasitesini aşmasını merkez alır.","focus_only":"Bu dal kişinin kendi isteğiyle güçlüğe girişip kendini zorlamasını kapsar.","gloss":"kendini zorlama ve gücü aşan yük","neighbor_only":"Komşu dal insan veya hayvana taşıyamayacağı kadar ağır yük bindirilmesini kapsar.","neighbor_ref":"root_000125/B004","relation_type":"near_neighbor","shared_zone":"Her iki dalda taşıma veya çalışma gücü sınırına yaklaşan bir zorlanma vardır."}],"source_phrase_ar":"تحاملت إذا تكلفت الشيء على مشقة (maqayis)؛ تحاملت في الشيء إذا تكلفته على مشقة (ayn)؛ حمل على نفسه في السير أي جهدها فيه (sihah)؛ تحامل عليه أي مال (sihah)؛ ما على فلان محمل أي معتمد (sihah;tahdhib)؛ المحمل بفتح الميم المعتمد (tahdhib)","source_summary":"Toplu kaynak anlatımı güçlük altında çabalamayı ve yolculukta kendini yormayı bir araya getirir; ayrıca birine doğru eğilme ile güvenilir dayanak anlamlarını ayrı yapısal kullanımlar olarak verir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"التكلف تحت مشقة؛ تحميل النفس في السير؛ الاعتماد والمحمل؛ الميل على غيره","what_is_not_ar":"الكفالة؛ الحبل؛ أدوات الحمل"},"support_links":["sup_2c11658836d19a99e374"]},{"boundary":"Dal yalnızca belirtilen türemiş biçimlerde geçerlidir ve öfkeye kapılma ile öfkeyi denetleyip katlanma anlamları kesin olarak ayrı tutulmalıdır.","branch_kind":"non_bare","branch_ref":"root_000357/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَمَّالَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ham~aAlap|ROOT:Hml|FS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:2:1","qac_word_ref":"111:4:2","surface_ar":"حَمَّالَةَ"}],"gloss":"öfkeye kapılma veya incinmeye ağırbaşlılıkla katlanma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Öfke kişiyi etkisi altına alır, onu huzursuz eder ve öfkeli tepkiye yöneltir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi kendisine yapılan incitici davranışı öfkesini denetleyerek ağırbaşlılıkla karşılar."}}],"root_ar":"ح م ل","root_id":"root_000357","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Aynı biçimin kaynaklarda aktarılan karşıt öfkelenme ve öfkeyi denetleyerek katlanma yönlerini birlikte belirtmek gerektiğinde kullanılır.","boundary_detail":"Dal yalnızca belirtilen türemiş biçimlerde geçerlidir ve öfkeye kapılma ile öfkeyi denetleyip katlanma anlamları kesin olarak ayrı tutulmalıdır.","branch_image_ar":"احتمال الغضب والحلم","concept_gloss":"öfkeye kapılma veya incinmeye ağırbaşlılıkla katlanma","contextual_glosses":[{"applicability":"Öfkenin kişiyi etkisi altına alıp onu huzursuz ettiği veya tepkiye yönelttiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öfkenin kişide baskın hale gelmesini ve davranışını harekete geçirmesini korur."},"facet_ids":["F001"],"text":"öfkeye kapılmak","usage_role":"contextual"},{"applicability":"Kişinin kendisine yönelen kötülüğe öfkeli karşılık vermeyip kendini tuttuğu bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İncinmeye rağmen öfkeyi denetleme ve karşılık vermeden dayanma tutumunu korur."},"facet_ids":["F002"],"text":"incitici davranışa ağırbaşlılıkla katlanmak","usage_role":"explanatory"}],"definition":"Belirli bir biçimde ya öfkeye kapılıp onun etkisiyle harekete geçmek ya da incitici davranışı öfkeyle karşılık vermeden ağırbaşlılıkla karşılamaktır. Kaynak anlatımı bu iki karşıt yönü aynı kullanım ailesinde verir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Öfke kişiyi etkisi altına alır, onu huzursuz eder ve öfkeli tepkiye yöneltir."},{"facet_id":"F002","role":"source_variant","statement":"Kişi kendisine yapılan incitici davranışı öfkesini denetleyerek ağırbaşlılıkla karşılar."}],"identity_rationale":"Kaynak ifadesi aynı biçimi bir yandan öfkelenmek veya öfkenin kişiyi yerinden oynatması, öte yandan incitici davranışa ağırbaşlılıkla katlanmak için aktarır. Geçici çerçeve iki yönü de yakalar, fakat bunlar tek süreç değil birbirine karşıt kaynak varyantlarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"öfkelenmek veya öfkenin etkisine kapılmak"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"incitici davranışa öfkesini tutarak katlanmak"}],"lexicalization_note":"Tanım iki karşıt anlamı belirtilen türemiş biçime bağlı tutar; bunlardan yalın bir öfke veya sabır anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel ağırbaşlılık, yoğun öfke ve öfkeyi içine atma karşılaştırmaları iki karşıt kaynak varyantını en iyi sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ağırbaşlılık yüzünde yakındırlar; bu dal belirli bir davranışa katlanma bağlamına bağlıdır ve aynı zamanda karşıt öfkelenme anlamını da taşır.","focus_only":"Bu dal ağırbaşlı katlanmanın karşıtı olan öfkeye kapılma anlamını da aynı biçimde taşır.","gloss":"öfkeyi denetleyerek katlanma","neighbor_only":"Komşu dal genel olarak aceleciliğin karşıtı olan ağırbaşlılık, sabır ve öfke denetimini kapsar.","neighbor_ref":"root_000352/B001","relation_type":"near_synonym","shared_zone":"İki dalda kişi öfkesini bastırır ve incitici davranış karşısında ölçülü kalır."},{"boundary_match":"partial","distinction":"Bu dalın öfke yüzü yoğun üzüntüyü gerektirmez ve karşıt katlanma yüzüyle birlikte aktarılır; komşu dalda iç yanması belirgin bir ektir.","focus_only":"Bu dal öfkenin yanı sıra ona karşı ağırbaşlılıkla katlanma anlamını da içerir.","gloss":"öfkeye kapılma ve iç yakan öfke","neighbor_only":"Komşu dal öfkeyi iç yanması ve yoğun üzüntüyle birleşen bir duygu olarak genişletir.","neighbor_ref":"root_000032/B002","relation_type":"near_synonym","shared_zone":"İki dal kişinin öfke duygusuna kapılması ve bundan etkilenmesi alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşuda belirleyici işlem öfkeyi içeride hapsetmektir; burada ise incitici kişiye ağırbaşlı davranma sonucu öndedir.","focus_only":"Bu dal incitici davranışa karşı genel ağırbaşlılıkla katlanmayı ve ayrıca öfkelenmeyi bildirir.","gloss":"katlanma ve öfkeyi içine atma","neighbor_only":"Komşu dal öfkeyi içte tutup dışa vurmama işlemini özellikle merkez alır.","neighbor_ref":"root_001303/B001","relation_type":"near_neighbor","shared_zone":"İki dal öfkenin davranışa dönüşmesini önleme ve kişinin kendini tutması alanında buluşur."}],"source_phrase_ar":"الاحتمال الغضب (maqayis)؛ احتمل إذا غضب (maqayis;tahdhib)؛ احتمله الغضب وأقله الغضب (maqayis)؛ حملت عنه أي حلمت عنه (ayn)؛ احتمل الرجل إذا غضب ويكون بمعنى حلم (tahdhib)","source_summary":"Kaynak anlatımı iki karşıt değer bildirir: öfkenin kişiyi etkisi altına alması ve kişinin incitici davranış karşısında öfkesini tutup ağırbaşlı davranması.","sources":["MQ","AY","TA"],"what_is_ar":"احتمال الأذى بالحلم؛ أو الاحتمل والغضب إذا أزعجه الغضب","what_is_not_ar":"الحمل الحسي؛ الكفالة؛ التحامل على المشقة"},"support_links":[]},{"boundary":"Dal koyun türünün genç yavrusuyla sınırlıdır; bütün küçük çiftlik hayvanlarını, yetişkin koyunu veya gökteki burcu kapsamaz.","branch_kind":"bare","branch_ref":"root_000357/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَمَّالَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ham~aAlap|ROOT:Hml|FS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:2:1","qac_word_ref":"111:4:2","surface_ar":"حَمَّالَةَ"}],"gloss":"kuzu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ad, koyun türüne ait genç yavruyu belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yaş bakımından bir yaşına yaklaşmış birey ve ondan daha küçük yavrular kapsama girer."}}],"root_ar":"ح م ل","root_id":"root_000357","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Koyunun genç yavrusunu, özellikle bir yaşına yaklaşmış veya daha küçük bireyi doğal Türkçeyle adlandırır.","boundary_detail":"Dal koyun türünün genç yavrusuyla sınırlıdır; bütün küçük çiftlik hayvanlarını, yetişkin koyunu veya gökteki burcu kapsamaz.","branch_image_ar":"الحَمَل من الضأن","concept_gloss":"kuzu","contextual_glosses":[{"applicability":"Yaşın özellikle vurgulandığı ve bir yaşına ulaşmamış koyun yavrusunun anlatıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın koyun yavrusu olmasını ve genç yaşta bulunmasını korur."},"facet_ids":["F001","F002"],"text":"genç kuzu","usage_role":"contextual"}],"definition":"Koyunun henüz genç olan yavrusu, özellikle bir yaşına yaklaşmış veya daha küçük bireyidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ad, koyun türüne ait genç yavruyu belirtir."},{"facet_id":"F002","role":"specialization","statement":"Yaş bakımından bir yaşına yaklaşmış birey ve ondan daha küçük yavrular kapsama girer."}],"identity_rationale":"Kaynak ifadesi bu adı açıkça koyunun küçük yavrusu, özellikle bir yaşına yaklaşmış veya daha küçük birey için verir. Geçici çerçeve hayvan türünü ve yaş sınırını doğru korur; göksel adla ya da genel taşıma anlamıyla karışmaz.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"kuzu"}],"lexicalization_note":"Tanım yalın adın genç koyun anlamını verir ve başka dallardaki göksel, gebelik ya da taşıma kullanımlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar incelendi; eş anlamlı genç koyun adı, genel koyun türü ve türler arası yavru adıyla yapılan karşılaştırmalar yeterli sınırı sağlar.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kaynak kartlarında kavramsal sınırı değiştiren bir ayrım görünmez; ek dişi biçimi yalnızca aynı genç koyun kavramının söz varlığına aittir.","focus_only":null,"gloss":"koyunun küçük yavrusu","neighbor_only":null,"neighbor_ref":"root_000051/B009","relation_type":"synonym","shared_zone":"İki dal da koyunun küçük yavrusunu aynı yaş ve tür çekirdeğiyle adlandırır."},{"boundary_match":"partial","distinction":"Burada yaş ve yavruluk kurucudur; komşu dal türün tamamını ve yetişkin bireyleri de kapsar.","focus_only":"Bu dal yalnızca koyunun genç yavrusunu adlandırır.","gloss":"kuzu ve koyun türü","neighbor_only":"Komşu dal yaş ayrımı yapmadan koyun türünü, dişi bireyi ve topluluk adlarını kapsar.","neighbor_ref":"root_000900/B001","relation_type":"near_neighbor","shared_zone":"Kuzu, komşu dalın adlandırdığı koyun türünün genç bireyidir."},{"boundary_match":"partial","distinction":"Bu dal tür bakımından dar, yaş bakımından belirgindir; komşu dal farklı hayvan türlerinin yavrularına yayılan üst kapsamlı bir addır.","focus_only":"Bu dal genç hayvanı koyun türüyle sınırlar.","gloss":"kuzu ve küçük çiftlik hayvanı","neighbor_only":"Komşu dal koyun, keçi, sığır ve yabani sığır gibi birden çok türün yavrularını kapsar.","neighbor_ref":"root_000160/B004","relation_type":"near_neighbor","shared_zone":"İki dal koyun yavrusunu kapsayan genç hayvan adlandırmalarında buluşur."}],"source_phrase_ar":"الحمل الخروف والجميع الحملان (ayn;tahdhib)؛ الحمل من الضأن معروف وهو الجذع فما دونه (jamhara)؛ خص الضأن الصغير بذلك لكونه محمولا (mufradat)","source_summary":"Kaynaklar adı koyunun genç yavrusu için ortak biçimde verir ve kapsamı bir yaşına yaklaşmış birey ile daha küçük dönemlere kadar açıklar.","sources":["AY","JA","TA","MU"],"what_is_ar":"الخروف الصغير من الضأن؛ الجذع فما دونه","what_is_not_ar":"برج الحمل؛ الحمل في البطن؛ حمل الأثقال"},"support_links":[]},{"boundary":"Göksel burç, ona bağlanan hava dönemi ve su yüklü bulut ya da şimşek ayrı tutulur; genç koyun anlamı bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000357/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَمَّالَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ham~aAlap|ROOT:Hml|FS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:2:1","qac_word_ref":"111:4:2","surface_ar":"حَمَّالَةَ"}],"gloss":"Koç burcu ve onunla ilişkilendirilen yağışlı gök olayı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ad, burçlar kuşağının ilk göksel bölümünü belirtir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı biçim çok su taşıyan veya kara görünen bulutu ve kimi anlatımda şimşeği adlandırır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli yağış veya hava dönemi göksel burcun doğuş ve batış çevrimine bağlanır."}}],"root_ar":"ح م ل","root_id":"root_000357","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Göksel burç ile ona bağlanan su yüklü bulut, şimşek ve yağış dönemi yüzlerini birlikte belirtmek gerektiğinde kullanılır.","boundary_detail":"Göksel burç, ona bağlanan hava dönemi ve su yüklü bulut ya da şimşek ayrı tutulur; genç koyun anlamı bu dala girmez.","branch_image_ar":"الحَمَل في السماء والسحاب","concept_gloss":"Koç burcu ve onunla ilişkilendirilen yağışlı gök olayı","contextual_glosses":[{"applicability":"Burçlar kuşağının ilk göksel bölümünün adlandırıldığı gökbilim bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Göksel bölümün burçlar kuşağındaki ilk burç olmasını korur."},"facet_ids":["F001"],"text":"Koç burcu","usage_role":"general"},{"applicability":"Bulutun koyu görünüşü ve içinde çok miktarda yağış suyu taşıması vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bulutun kara görünmesini ve bol su taşımasını birlikte korur."},"facet_ids":["F002"],"text":"bol su taşıyan kara bulut","usage_role":"contextual"},{"applicability":"Yağışın göksel burcun doğuş veya batış dönemine bağlandığı geleneksel hava anlatımında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yağış ile göksel dönem arasında kurulan geleneksel zaman bağını korur."},"facet_ids":["F003"],"text":"Koç dönemine bağlanan yağış","usage_role":"explanatory"}],"definition":"Gökte burçlar kuşağının ilk bölümü ve bununla ilişkilendirilen hava dönemidir. Aynı ad ailesi çok su taşıyan ya da kara bulutu, şimşeği ve bu göksel döneme bağlanan yağışı da gösterebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ad, burçlar kuşağının ilk göksel bölümünü belirtir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı biçim çok su taşıyan veya kara görünen bulutu ve kimi anlatımda şimşeği adlandırır."},{"facet_id":"F003","role":"associated_use","statement":"Belirli yağış veya hava dönemi göksel burcun doğuş ve batış çevrimine bağlanır."}],"identity_rationale":"Kaynak ifadesi gökteki ilk burcu, onunla ilişkilendirilen hava dönemini, çok su taşıyan veya kara bulutu ve şimşeği aynı ad ailesinde toplar. Geçici çerçeve öğeleri doğru sayar, ancak burç ile hava olayları tek bir nesne değil, göksel ad çevresinde birleşen ayrı yüzlerdir.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"Koç, burçlar kuşağının ilk burcu"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"bol su taşıyan kara bulut veya şimşek"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"bol su taşıyan bulut"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"Koç burcuna bağlanan yağış dönemi"}],"lexicalization_note":"Tanım göksel adın yalın kullanımını bulut ve şimşek adlarından, ayrıca burca bağlanan yağış yapısından ayırır; bu yüzleri tek nesneye indirgemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yıldız dönemine bağlı hava, çok sulu bulut ve şimşekle yapılan üç karşılaştırma göksel ve hava olaylı yüzleri yeterince ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal tek bir göksel ada ve onun bulut ya da şimşek uzantılarına özgüdür; komşu dal yıldız duraklarına bağlı hava olaylarının genel çerçevesidir.","focus_only":"Bu dal belirli bir burcu ve aynı adla anılan bulut ile şimşeği de kapsar.","gloss":"Koç dönemi ve yıldızlara bağlanan hava","neighbor_only":"Komşu dal farklı yıldız duraklarının doğuş ve batışlarına bağlanan yağmur, rüzgar, sıcak ve soğuk dönemlerinin genel sistemini kapsar.","neighbor_ref":"root_001561/B002","relation_type":"near_neighbor","shared_zone":"İki dal hava olaylarının bir yıldız veya göksel bölümün görünme dönemine bağlanması alanında buluşur."},{"boundary_match":"partial","distinction":"Bulut yüzünde yakınlaşırlar; bu dal bol su veya kara görünüşle yetinirken komşu dal damla büyüklüğü ve yağışın şiddetini sınırına ekler.","focus_only":"Bu dal göksel burcu, kara bulutu ve şimşeği de içerir.","gloss":"çok sulu bulut ve şiddetli yağmur bulutu","neighbor_only":"Komşu dal özellikle damlaları büyük ve düşüşü şiddetli yağmur bulutunu anlatır.","neighbor_ref":"root_000615/B014","relation_type":"near_synonym","shared_zone":"İki dal da çok miktarda yağış suyu taşıyan büyük bulutu adlandırır."},{"boundary_match":"partial","distinction":"Burada şimşek göksel ad ailesinin bir yüzüdür; komşu dalda şimşek ve gök gürültüsü doğrudan hava olayının çekirdeğidir.","focus_only":"Bu dal şimşeği belirli göksel ad ve yağışlı bulut çevresinde adlandırır.","gloss":"adlandırılmış şimşek ve gök gürültüsü","neighbor_only":"Komşu dal göğün gürlemesi, şimşek çakması ve gök gürültülü bulutu birlikte kapsar.","neighbor_ref":"root_000573/B003","relation_type":"near_neighbor","shared_zone":"İki dal yağışlı gökte görülen şimşek olayını ortak olarak içerir."}],"source_phrase_ar":"الحمل برج من البروج (ayn;tahdhib)؛ الحمل أول البروج (sihah)؛ البرق يقال له حمل (maqayis)؛ الحمل السحاب الكثير الماء (jamhara)؛ الحمل السحاب الأسود (tahdhib)؛ الحمل النوء وهو الطلي (tahdhib)؛ الحميل السحاب الكثير الماء لكونه حاملا للماء (mufradat)","source_summary":"Toplu kaynak anlatımı burçlar kuşağının ilk bölümünü temel göksel ad olarak verir; çok sulu veya kara bulut, şimşek ve bu göksel döneme bağlanan yağış kullanımlarını bunun çevresinde toplar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"برج الحمل ونوؤه؛ السحاب الكثير الماء أو الأسود الحامل للماء؛ البرق أو المطر المنسوب إليه","what_is_not_ar":"الخروف؛ الحمل في البطن؛ حمل الأثقال"},"support_links":[]},{"boundary":"Personal nouns for a human, man, woman, and their inflected or variant forms.","branch_kind":null,"branch_ref":"root_001409/B001","candidate_links":[{"candidate_id":"cand_f338f372d0dd70cf44f8","lane":"micro"},{"candidate_id":"cand_9c0924d3873387f55844","lane":"micro"},{"candidate_id":"cand_c3eb81b161ea6bb9b135","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ٱمْرَأَت","morph_features":"STEM|POS:N|LEM:{mora>at|ROOT:mrA|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:1:2","qac_word_ref":"111:4:1","surface_ar":"ٱمْرَأَتُ"}],"gloss":"person and woman","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"المرء والمرأة","image_en":"person and woman"}}],"root_ar":"م ر ء","root_id":"root_001409","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"المرء والمرأة","image_en":"person and woman","scope_ar":"أسماء الإنسان والذكر والأنثى وما يتصل بها من امرؤ وامرأة ومرء ومرأة ومرة","scope_en":"Personal nouns for a human, man, woman, and their inflected or variant forms."},"support_links":["sup_02e67034803912d704c0","sup_228cf238a28dc4f1b0e2","sup_54c9ccb0d4c2ae467b9f"]}],"candidate_inventory":[{"anchor_refs":["111:4:1"],"branch_refs":[],"candidate_id":"cand_0347d7f82f1513a8af6a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:4:1:continuation-with-new-focus","source_type":"word_analysis","support_ids":["sup_384d32e2e2798618efc0","sup_bf62596796f21a98730a"],"title":"continuation with fresh nominal focus","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:1","qac_refs":["111:4:1:1"],"status":"accepted"}},{"anchor_refs":["111:4:1"],"branch_refs":[],"candidate_id":"cand_37175674eea88fb260d5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:4:1:inherited-condemnation","source_type":"word_analysis","support_ids":["sup_a87b9b78924b1d3b1792","sup_bf62596796f21a98730a"],"title":"prior condemnation carried forward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:1","qac_refs":["111:4:1:1"],"status":"accepted"}},{"anchor_refs":["111:4:1"],"branch_refs":[],"candidate_id":"cand_bf12d61af2a18c959f21","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:4:1:structural-cumulative-link","source_type":"word_analysis","support_ids":["sup_bf62596796f21a98730a","sup_de5bfacc8ba1590b8d53"],"title":"addition stays structurally cumulative","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:1","qac_refs":["111:4:1:1"],"status":"accepted"}},{"anchor_refs":["111:4:1"],"branch_refs":[],"candidate_id":"cand_a0127ba3eca17b9bfff5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:4:1:surface-and-sound-fusion","source_type":"word_analysis","support_ids":["sup_6546beab156cc2866eed","sup_bf62596796f21a98730a"],"title":"connector fused to the wife-word","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:1","qac_refs":["111:4:1:1"],"status":"accepted"}},{"anchor_refs":["111:4:2"],"branch_refs":[],"candidate_id":"cand_bc8586bd185f6956f3bb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:4:2:annexed-feminine-form","source_type":"word_analysis","support_ids":["sup_e2a33a0156abdfdc7a3f","sup_ec86a76fc82119bdfec2"],"title":"feminine noun carries masculine possession","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:2","qac_refs":["111:4:1:2","111:4:1:3"],"status":"accepted"}},{"anchor_refs":["111:4:2"],"branch_refs":[],"candidate_id":"cand_be585f8f87ed40392940","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:4:2:forward-feminine-reference","source_type":"word_analysis","support_ids":["sup_59b226613af768a7ac52","sup_e2a33a0156abdfdc7a3f"],"title":"wife-reference continues into the neck image","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:2","qac_refs":["111:4:1:2","111:4:1:3"],"status":"accepted"}},{"anchor_refs":["111:4:2"],"branch_refs":[],"candidate_id":"cand_13d0ce6cb4dd4da7465a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:4:2:hamza-interruption","source_type":"word_analysis","support_ids":["sup_c8cf9df630adc19072e3","sup_e2a33a0156abdfdc7a3f"],"title":"internal glottal interruption","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:2","qac_refs":["111:4:1:2","111:4:1:3"],"status":"accepted"}},{"anchor_refs":["111:4:2"],"branch_refs":[],"candidate_id":"cand_1eb74680a5342be4df72","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:4:2:nominative-nominal-frame","source_type":"word_analysis","support_ids":["sup_960bcfb7f19ababeae84","sup_e2a33a0156abdfdc7a3f"],"title":"nominative subject in a verbless characterization","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:2","qac_refs":["111:4:1:2","111:4:1:3"],"status":"accepted"}},{"anchor_refs":["111:4:2"],"branch_refs":[],"candidate_id":"cand_f12bfdd91cef33b9f536","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:4:2:possessive-identity","source_type":"word_analysis","support_ids":["sup_01ee900452c63c1d626c","sup_e2a33a0156abdfdc7a3f"],"title":"identity routed through the condemned male","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:2","qac_refs":["111:4:1:2","111:4:1:3"],"status":"accepted"}},{"anchor_refs":["111:4:2"],"branch_refs":[],"candidate_id":"cand_76f8311b67b462054236","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:4:2:relational-anonymity-pattern","source_type":"word_analysis","support_ids":["sup_be811686ddbee156c3d2","sup_e2a33a0156abdfdc7a3f"],"title":"relation replaces a personal name","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:2","qac_refs":["111:4:1:2","111:4:1:3"],"status":"accepted"}},{"anchor_refs":["111:4:2"],"branch_refs":[],"candidate_id":"cand_e7bc842a2e1bf88a3022","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"111:4:2:wife-woman-personhood","source_type":"word_analysis","support_ids":["sup_e2a33a0156abdfdc7a3f","sup_f9d2717a89e019371e9d"],"title":"wife sense selected from woman/person range","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:2","qac_refs":["111:4:1:2","111:4:1:3"],"status":"accepted"}},{"anchor_refs":["111:4:3"],"branch_refs":[],"candidate_id":"cand_02fa9fe4c8abf2584d92","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000357"],"scope":"focus_ayah","source_local_id":"111:4:3:accusative-case-crux","source_type":"word_analysis","support_ids":["sup_2afcc91c6c291f659805","sup_ba916136e76f053070d7"],"title":"accusative case carries interpretive force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:3","qac_refs":["111:4:2:1"],"status":"accepted"}},{"anchor_refs":["111:4:3"],"branch_refs":[],"candidate_id":"cand_9537e2918d26cf514f99","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000357"],"scope":"focus_ayah","source_local_id":"111:4:3:boundary-fire-and-binding","source_type":"word_analysis","support_ids":["sup_2afcc91c6c291f659805","sup_9888cb362dc469c0d1c7"],"title":"fire scene turns toward carried burden and binding","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:3","qac_refs":["111:4:2:1"],"status":"accepted"}},{"anchor_refs":["111:4:3"],"branch_refs":[],"candidate_id":"cand_c47c9b7de2d0637c178c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000357"],"scope":"focus_ayah","source_local_id":"111:4:3:burden-and-idiom","source_type":"word_analysis","support_ids":["sup_2afcc91c6c291f659805","sup_f35ec805641eaa46e018"],"title":"literal burden and social harm remain together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:3","qac_refs":["111:4:2:1"],"status":"accepted"}},{"anchor_refs":["111:4:3"],"branch_refs":[],"candidate_id":"cand_985637a947a627ce5880","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000357"],"scope":"focus_ayah","source_local_id":"111:4:3:compressed-idafa-action","source_type":"word_analysis","support_ids":["sup_2afcc91c6c291f659805","sup_6495e13a1fa5c1701a14"],"title":"action compressed into a construct title","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:3","qac_refs":["111:4:2:1"],"status":"accepted"}},{"anchor_refs":["111:4:3"],"branch_refs":[],"candidate_id":"cand_85330e06108e687f1a34","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000357"],"scope":"focus_ayah","source_local_id":"111:4:3:convergence","source_type":"word_analysis","support_ids":["sup_01f265b03fe760fd0aea","sup_2afcc91c6c291f659805"],"title":"grammar, idiom, sound, and rarity converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:3","qac_refs":["111:4:2:1"],"status":"accepted"}},{"anchor_refs":["111:4:3"],"branch_refs":[],"candidate_id":"cand_b603a52c685eb2f4c4a4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000357"],"scope":"focus_ayah","source_local_id":"111:4:3:derivational-burden-pressure","source_type":"word_analysis","support_ids":["sup_2afcc91c6c291f659805","sup_53e022c81141225e04b7"],"title":"other carrying fields add burden pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:3","qac_refs":["111:4:2:1"],"status":"accepted"}},{"anchor_refs":["111:4:3"],"branch_refs":[],"candidate_id":"cand_f3a726563a3dab59867f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000357"],"scope":"focus_ayah","source_local_id":"111:4:3:feminine-anchoring-and-delay","source_type":"word_analysis","support_ids":["sup_1666210c3391aa6edbec","sup_2afcc91c6c291f659805"],"title":"epithet anchored to the wife after delay","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:3","qac_refs":["111:4:2:1"],"status":"accepted"}},{"anchor_refs":["111:4:3"],"branch_refs":[],"candidate_id":"cand_0d2fe0a862923e8426fb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000357"],"scope":"focus_ayah","source_local_id":"111:4:3:intensive-carrier-title","source_type":"word_analysis","support_ids":["sup_225276e0ee8aa0e69ad8","sup_2afcc91c6c291f659805"],"title":"habitual professionalized carrier-title","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:3","qac_refs":["111:4:2:1"],"status":"accepted"}},{"anchor_refs":["111:4:3"],"branch_refs":[],"candidate_id":"cand_e8824b41f25f31b0152a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000357"],"scope":"focus_ayah","source_local_id":"111:4:3:marked-form-rarity","source_type":"word_analysis","support_ids":["sup_2afcc91c6c291f659805","sup_f07334004e799172f797"],"title":"rare intensive form inside a common root","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:3","qac_refs":["111:4:2:1"],"status":"accepted"}},{"anchor_refs":["111:4:3"],"branch_refs":[],"candidate_id":"cand_47faccf2cbb529ba5f88","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000357"],"scope":"focus_ayah","source_local_id":"111:4:3:qiraat-case-contrast","source_type":"word_analysis","support_ids":["sup_2afcc91c6c291f659805","sup_e277eaec5622f85863b6"],"title":"variant case contrasts with received accusative","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:3","qac_refs":["111:4:2:1"],"status":"accepted"}},{"anchor_refs":["111:4:3"],"branch_refs":[],"candidate_id":"cand_c7b25cf2512fe92be566","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000357"],"scope":"focus_ayah","source_local_id":"111:4:3:sound-weight-and-local-reprise","source_type":"word_analysis","support_ids":["sup_2afcc91c6c291f659805","sup_ec1ee7897aab941471b6"],"title":"sound makes the load feel heavy","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:3","qac_refs":["111:4:2:1"],"status":"accepted"}},{"anchor_refs":["111:4:4"],"branch_refs":[],"candidate_id":"cand_1ea27c596416cdfbb48e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000335"],"scope":"focus_ayah","source_local_id":"111:4:4:case-variant-contrast","source_type":"word_analysis","support_ids":["sup_17f496d92f156a3b604e","sup_c72df9dc8bb3f5292ebd"],"title":"variant accusative contrasts with received genitive","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:4","qac_refs":["111:4:3:1","111:4:3:2"],"status":"accepted"}},{"anchor_refs":["111:4:4"],"branch_refs":[],"candidate_id":"cand_654fc9b65a5a11bb21cd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000335"],"scope":"focus_ayah","source_local_id":"111:4:4:closure-weight","source_type":"word_analysis","support_ids":["sup_17f496d92f156a3b604e","sup_30648dbe6a711de4d392"],"title":"ayah lands on the fuel object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:4","qac_refs":["111:4:3:1","111:4:3:2"],"status":"accepted"}},{"anchor_refs":["111:4:4"],"branch_refs":[],"candidate_id":"cand_5eed882966cb52d77a4a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000335"],"scope":"focus_ayah","source_local_id":"111:4:4:concrete-bounded-fuel","source_type":"word_analysis","support_ids":["sup_17f496d92f156a3b604e","sup_40183fda48f16d8502b1"],"title":"specific concrete fuel material","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:4","qac_refs":["111:4:3:1","111:4:3:2"],"status":"accepted"}},{"anchor_refs":["111:4:4"],"branch_refs":[],"candidate_id":"cand_55041648535a430d54e7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000335"],"scope":"focus_ayah","source_local_id":"111:4:4:convergence","source_type":"word_analysis","support_ids":["sup_17f496d92f156a3b604e","sup_c8d0c64dd186b0d738b3"],"title":"sense, rarity, boundary, and sound converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:4","qac_refs":["111:4:3:1","111:4:3:2"],"status":"accepted"}},{"anchor_refs":["111:4:4"],"branch_refs":[],"candidate_id":"cand_09d03fe06c8555bd9971","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000335"],"scope":"focus_ayah","source_local_id":"111:4:4:definite-genitive-construct","source_type":"word_analysis","support_ids":["sup_17f496d92f156a3b604e","sup_d5242eed7f6054b50233"],"title":"definite genitive completes the title","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:4","qac_refs":["111:4:3:1","111:4:3:2"],"status":"accepted"}},{"anchor_refs":["111:4:4"],"branch_refs":[],"candidate_id":"cand_76a8ba4f048913f49132","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000335"],"scope":"focus_ayah","source_local_id":"111:4:4:fire-field-and-material-cause","source_type":"word_analysis","support_ids":["sup_17f496d92f156a3b604e","sup_c86e453f66208fde565c"],"title":"fuel answers the prior fire","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:4","qac_refs":["111:4:3:1","111:4:3:2"],"status":"accepted"}},{"anchor_refs":["111:4:4"],"branch_refs":[],"candidate_id":"cand_68ad95b8fe79f1bba410","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000335"],"scope":"focus_ayah","source_local_id":"111:4:4:gathered-dangerous-material","source_type":"word_analysis","support_ids":["sup_17f496d92f156a3b604e","sup_b69e51d4a5e9e403fe21"],"title":"fuel feels gathered and dangerous","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:4","qac_refs":["111:4:3:1","111:4:3:2"],"status":"accepted"}},{"anchor_refs":["111:4:4"],"branch_refs":[],"candidate_id":"cand_9a324bdf40436f6b8a8b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000335"],"scope":"focus_ayah","source_local_id":"111:4:4:literal-social-hell-fuel","source_type":"word_analysis","support_ids":["sup_17f496d92f156a3b604e","sup_ee06c5936ebb21a4bf9b"],"title":"literal fuel with social and punishment resonance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:4","qac_refs":["111:4:3:1","111:4:3:2"],"status":"accepted"}},{"anchor_refs":["111:4:4"],"branch_refs":[],"candidate_id":"cand_10094eadb13b22656ed8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000335"],"scope":"focus_ayah","source_local_id":"111:4:4:material-field-to-binding","source_type":"word_analysis","support_ids":["sup_17f496d92f156a3b604e","sup_a857ae5500f3bad8077c"],"title":"fuel bridges flame and rope material","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:4","qac_refs":["111:4:3:1","111:4:3:2"],"status":"accepted"}},{"anchor_refs":["111:4:4"],"branch_refs":[],"candidate_id":"cand_632aaa87a5a2556b7866","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000335"],"scope":"focus_ayah","source_local_id":"111:4:4:near-hapax-rarity","source_type":"word_analysis","support_ids":["sup_17f496d92f156a3b604e","sup_71ce057b99d59605419b"],"title":"rare fuel root carries extra weight","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:4","qac_refs":["111:4:3:1","111:4:3:2"],"status":"accepted"}},{"anchor_refs":["111:4:4"],"branch_refs":[],"candidate_id":"cand_d729c0aba1071beefc99","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000335"],"scope":"focus_ayah","source_local_id":"111:4:4:sound-and-cadence","source_type":"word_analysis","support_ids":["sup_17f496d92f156a3b604e","sup_5581a35424c02c41be90"],"title":"rough sound and clipped cadence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:4","qac_refs":["111:4:3:1","111:4:3:2"],"status":"accepted"}},{"anchor_refs":["111:4:4"],"branch_refs":[],"candidate_id":"cand_05d5e3d5cd82c144bd79","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000335"],"scope":"focus_ayah","source_local_id":"111:4:4:surface-lexeme-weight","source_type":"word_analysis","support_ids":["sup_17f496d92f156a3b604e","sup_9baeaaf0debab6526546"],"title":"exact definite lexeme bears local weight","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"111:4:4","qac_refs":["111:4:3:1","111:4:3:2"],"status":"accepted"}},{"anchor_refs":["111:4:1"],"branch_refs":[],"candidate_id":"cand_c6bcc0481a56549f17a2","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001409"],"scope":"focus_ayah","source_local_id":"111:4:1:2","source_type":"qac_morpheme","support_ids":["sup_c5a90f79b233d608d989"],"title":"QAC root occurrence: م ر ء","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["111:4:2"],"branch_refs":[],"candidate_id":"cand_31ad396af14717bd48b1","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000357"],"scope":"focus_ayah","source_local_id":"111:4:2:1","source_type":"qac_morpheme","support_ids":["sup_acd4a757cbd0c6266c4b"],"title":"QAC root occurrence: ح م ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["111:4:3"],"branch_refs":[],"candidate_id":"cand_66b03413aeebed39ac81","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000335"],"scope":"focus_ayah","source_local_id":"111:4:3:2","source_type":"qac_morpheme","support_ids":["sup_fdcca1947d052b46eb27"],"title":"QAC root occurrence: ح ط ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["111:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"111:4","branch_refs":["root_000335/B001","root_000357/B001","root_001409/B001"],"candidate_id":"cand_f338f372d0dd70cf44f8","commentary_obligation":"review","hft_ref":"hft_2a32c6d3bc58934c87e7","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_outward_fuel_logistics","source_type":"hft","support_ids":["sup_228cf238a28dc4f1b0e2"],"title":"baseline_outward_fuel_logistics","trust":"legacy_unbound"},{"anchor_refs":["111:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"111:4","branch_refs":["root_000335/B003","root_000357/B001","root_001409/B001"],"candidate_id":"cand_9c0924d3873387f55844","commentary_obligation":"review","hft_ref":"hft_a05697cd2cae4d33b0db","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_social_ignition_bearer","source_type":"hft","support_ids":["sup_54c9ccb0d4c2ae467b9f"],"title":"baseline_social_ignition_bearer","trust":"legacy_unbound"},{"anchor_refs":["111:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"111:4","branch_refs":["root_000335/B002","root_000357/B007"],"candidate_id":"cand_1596ab352af9b9b588a8","commentary_obligation":"review","hft_ref":"hft_94efc337fd27338a1d91","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_indiscriminate_bundle","source_type":"hft","support_ids":["sup_2c11658836d19a99e374"],"title":"baseline_indiscriminate_bundle","trust":"legacy_unbound"},{"anchor_refs":["111:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"111:4","branch_refs":["root_000335/B001","root_000357/B002","root_001409/B001"],"candidate_id":"cand_c3eb81b161ea6bb9b135","commentary_obligation":"review","hft_ref":"hft_29e6ff983afbf64a2d93","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_inverted_fruition","source_type":"hft","support_ids":["sup_02e67034803912d704c0"],"title":"baseline_inverted_fruition","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"111:4:1:1","qac_word_ref":"111:4:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"ٱمْرَأَت","morph_features":"STEM|POS:N|LEM:{mora>at|ROOT:mrA|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:1:2","qac_word_ref":"111:4:1","root_ar":"م ر ء","surface_ar":"ٱمْرَأَتُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"111:4:1:3","qac_word_ref":"111:4:1","root_ar":"","surface_ar":"هُۥ"},{"lemma_ar":"حَمَّالَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ham~aAlap|ROOT:Hml|FS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:2:1","qac_word_ref":"111:4:2","root_ar":"ح م ل","surface_ar":"حَمَّالَةَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"111:4:3:1","qac_word_ref":"111:4:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"حَطَب","morph_features":"STEM|POS:N|LEM:HaTab|ROOT:HTb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:3:2","qac_word_ref":"111:4:3","root_ar":"ح ط ب","surface_ar":"حَطَبِ"}],"word_analysis_qac_refs":[["111:4:1:1"],["111:4:1:2","111:4:1:3"],["111:4:2:1"],["111:4:3:1","111:4:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["111:4:1","111:4:2","111:4:3","111:4:4"]},"focus_surface_evidence":{"arabic_uthmani":"وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"111:4:1:1","qac_word_ref":"111:4:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"ٱمْرَأَت","morph_features":"STEM|POS:N|LEM:{mora>at|ROOT:mrA|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:1:2","qac_word_ref":"111:4:1","root_ar":"م ر ء","surface_ar":"ٱمْرَأَتُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"111:4:1:3","qac_word_ref":"111:4:1","root_ar":"","surface_ar":"هُۥ"},{"lemma_ar":"حَمَّالَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:Ham~aAlap|ROOT:Hml|FS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:2:1","qac_word_ref":"111:4:2","root_ar":"ح م ل","surface_ar":"حَمَّالَةَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"111:4:3:1","qac_word_ref":"111:4:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"حَطَب","morph_features":"STEM|POS:N|LEM:HaTab|ROOT:HTb|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"111:4:3:2","qac_word_ref":"111:4:3","root_ar":"ح ط ب","surface_ar":"حَطَبِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["111:4:1:1"],["111:4:1:2","111:4:1:3"],["111:4:2:1"],["111:4:3:1","111:4:3:2"]],"word_analysis_refs":["111:4:1","111:4:2","111:4:3","111:4:4"],"word_rows":[{"analysis_record_ref":"111:4:1","analytic_gloss_range_en":"coordinating connector that carries the prior condemnation forward while allowing the ayah to open a focused nominal characterization","analytic_root_gloss_range_en":null,"qac_refs":["111:4:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"111:4:2","analytic_gloss_range_en":"wife or woman, locally narrowed by the attached masculine suffix to a particular wife identified through the prior male referent","analytic_root_gloss_range_en":"person and woman/wife range with broader personhood associations; local grammar selects the relational wife sense and does not license unrelated root-family senses as the main meaning","qac_refs":["111:4:1:2","111:4:1:3"],"root":{"arabic":"م ر أ","transliteration":"m-r-'"},"surface":{"arabic":"ٱمْرَأَتُهُۥ","transliteration":"mra'atuhu"}},{"analysis_record_ref":"111:4:3","analytic_gloss_range_en":"intensive feminine carrier-title in accusative, locally naming habitual burden-bearing while leaving live case analyses such as state, apposition, or censure","analytic_root_gloss_range_en":"broad carrying range including lifting, bearing burdens, pregnancy, liability, gear, and endurance; local construction selects load-bearing agency with idiomatic and moral burden pressure, not unrelated branches as direct senses","qac_refs":["111:4:2:1"],"root":{"arabic":"ح م ل","transliteration":"ḥ-m-l"},"surface":{"arabic":"حَمَّالَةَ","transliteration":"ḥammālata"}},{"analysis_record_ref":"111:4:4","analytic_gloss_range_en":"the definite firewood or fuel, genitive in construct with the carrier-title; literal combustible material is selected while idiomatic social fuel and punishment-fuel resonance remain bounded pressures","analytic_root_gloss_range_en":"firewood, fuel prepared for burning, wood-gathering, and idiomatic tale-bearing or kindling of hostility; local grammar selects definite carried fuel while allowing gathered, social, and punishment-fuel resonances","qac_refs":["111:4:3:1","111:4:3:2"],"root":{"arabic":"ح ط ب","transliteration":"ḥ-ṭ-b"},"surface":{"arabic":"ٱلْحَطَبِ","transliteration":"al-ḥaṭabi"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["111:4"],"branch_refs":["root_000335/B001","root_000357/B001","root_001409/B001"],"candidate_id":"cand_f338f372d0dd70cf44f8","evidence_scope":"focus_ayah","hft_ref":"hft_2a32c6d3bc58934c87e7","item_id":"baseline_outward_fuel_logistics","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_outward_fuel_logistics","support_id":"sup_228cf238a28dc4f1b0e2"},{"anchor_refs":["111:4"],"branch_refs":["root_000335/B003","root_000357/B001","root_001409/B001"],"candidate_id":"cand_9c0924d3873387f55844","evidence_scope":"focus_ayah","hft_ref":"hft_a05697cd2cae4d33b0db","item_id":"baseline_social_ignition_bearer","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_social_ignition_bearer","support_id":"sup_54c9ccb0d4c2ae467b9f"},{"anchor_refs":["111:4"],"branch_refs":["root_000335/B002","root_000357/B007"],"candidate_id":"cand_1596ab352af9b9b588a8","evidence_scope":"focus_ayah","hft_ref":"hft_94efc337fd27338a1d91","item_id":"baseline_indiscriminate_bundle","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_indiscriminate_bundle","support_id":"sup_2c11658836d19a99e374"},{"anchor_refs":["111:4"],"branch_refs":["root_000335/B001","root_000357/B002","root_001409/B001"],"candidate_id":"cand_c3eb81b161ea6bb9b135","evidence_scope":"focus_ayah","hft_ref":"hft_29e6ff983afbf64a2d93","item_id":"baseline_inverted_fruition","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_inverted_fruition","support_id":"sup_02e67034803912d704c0"}],"diagnostics":[],"lane_counts":{"global":10,"macro":14,"micro":4},"packet_summary":{"ayah_count":5,"focus_ref":"111:4","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ي د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001693","furuq_root_norm":"ي د ي","furuq_source_root_norm":"ي د ي","is_dominant":true,"target_occurrences":107,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000071","furuq_root_norm":"ء ي د","furuq_source_root_norm":"أ ي د","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]}],"window":["111:1","111:2","111:3","111:4","111:5"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"111:4","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":18,"unstructured_record_count":0},"identity":{"ayah_ref":"111:4","lane":"micro","linguistic_source_ref":"111:4","surface_ref":"111:4","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"111:4","target_tokens":[["Odun",["111:4:3"]],["taşıyan",["111:4:2"]],["karısı",["111:4:1"]],["da",["111:4:1"]]],"text":"Odun taşıyan karısı da."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":5,"id":"s111-p01-001-005","label":"Whole surah","number":1,"refs":["111:1","111:2","111:3","111:4","111:5"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:2:possessive-identity","source_type":"word_analysis","support_id":"sup_01ee900452c63c1d626c","text":"{\"blocking_evidence\":null,\"headline\":\"identity routed through the condemned male\",\"reader_payoff\":\"The reader sees that she is made definite and recognizable through the suffix relation to the prior male referent, not by an independent name.\",\"reason\":\"Attachment evidence strongly links the third-person masculine suffix to the proper-name span in 111:1, so the word's definiteness and reference are relational.\",\"representative_source_ids\":[\"QG-dba39c59\",\"QG-eca96a22\",\"QI-0dc6ee25\",\"QB-b78077c1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:3:convergence","source_type":"word_analysis","support_id":"sup_01f265b03fe760fd0aea","text":"{\"blocking_evidence\":null,\"headline\":\"grammar, idiom, sound, and rarity converge\",\"reader_payoff\":\"The reader sees the title's force as cumulative: grammar, habitual form, idiom, sound, and rarity all make carrying into identity.\",\"reason\":\"The synthesis row is preserved because its component payoffs survive after local grammar and dictionary guardrails are applied.\",\"representative_source_ids\":[\"QY-a7976506\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:3:feminine-anchoring-and-delay","source_type":"word_analysis","support_id":"sup_1666210c3391aa6edbec","text":"{\"blocking_evidence\":null,\"headline\":\"epithet anchored to the wife after delay\",\"reader_payoff\":\"The reader moves from relational identity to the delayed feminine epithet, so the title lands as her specific characterization.\",\"reason\":\"The feminine ending agrees with the wife-word, and the word order delays the decisive epithet until after the relational subject.\",\"representative_source_ids\":[\"QF-dc538bf4\",\"QT-e8975910\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:4","source_type":"word_analysis","support_id":"sup_17f496d92f156a3b604e","text":"{\"gloss_range\":\"the definite firewood or fuel, genitive in construct with the carrier-title; literal combustible material is selected while idiomatic social fuel and punishment-fuel resonance remain bounded pressures\",\"prose\":\"{{ar:ٱلْحَطَبِ}} ({{tr:al-ḥaṭabi}}) is the governed object that completes the carrier-title. Its genitive case binds it to {{ar:حَمَّالَةَ}} ({{tr:ḥammālata}}), while the definite article makes the phrase point to the firewood, not merely any fuel; an accusative-object variant would make the carrying more event-like, but the received genitive keeps the fuel annexed inside the title. The local fire in 111:3 selects literal combustible material first, but the root and idiom keep gathered harmful fuel, blind woodgathering, and social kindling in view, and the paired punishment-fuel occurrence at 72:15 gives the rare word a darker Quranic resonance. As the ayah's final word, it lands the scene on the material object: fuel heard as rough, specific, gathered, with the audible article boundary and clipped cadence placing it between the prior flame and the rope-material image of 111:5.\",\"root_display\":\"{{ar:ح ط ب}} ({{tr:ḥ-ṭ-b}})\",\"root_gloss_range\":\"firewood, fuel prepared for burning, wood-gathering, and idiomatic tale-bearing or kindling of hostility; local grammar selects definite carried fuel while allowing gathered, social, and punishment-fuel resonances\",\"surface_display\":\"{{ar:ٱلْحَطَبِ}} ({{tr:al-ḥaṭabi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:3:intensive-carrier-title","source_type":"word_analysis","support_id":"sup_225276e0ee8aa0e69ad8","text":"{\"blocking_evidence\":null,\"headline\":\"habitual professionalized carrier-title\",\"reader_payoff\":\"The reader hears carrying as a defining repeated role rather than a one-time act of holding firewood.\",\"reason\":\"QAC identifies the form as an intensive active participle, and contextual evidence marks this exact form as a low-occurrence, marked selection.\",\"representative_source_ids\":[\"QS-e4f67ece\",\"QF-59e5cdf4\",\"QF-e9b511de\",\"QI-e1d7d5e6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:3","source_type":"word_analysis","support_id":"sup_2afcc91c6c291f659805","text":"{\"gloss_range\":\"intensive feminine carrier-title in accusative, locally naming habitual burden-bearing while leaving live case analyses such as state, apposition, or censure\",\"prose\":\"{{ar:حَمَّالَةَ}} ({{tr:ḥammālata}}) turns the relational wife into a charged carrier-title. Its intensive feminine pattern makes carrying sound habitual and role-like, and its rarity inside a common carrying root makes the title feel specially selected rather than routine. The construct with {{ar:ٱلْحَطَبِ}} ({{tr:al-ḥaṭabi}}) compresses an action relation into a title without a finite verb. The accusative is not syntactically flat: it can mark state, appositional specification, or censure, and the censure reading lets the case ending itself participate in blame; by contrast, a nominative variant would make the epithet more directly predicate-like. The root's wider load-bearing field adds pressure from being made to bear, life-bearing, and burden-gear, while local grammar keeps fuel-carrying selected. The idiom keeps social harm present, and 111:3 keeps literal fuel in view; the doubled middle sound, the repeated rough onset with the fuel word, and the forward movement to 111:5 make the burden feel both audible and tightening.\",\"root_display\":\"{{ar:ح م ل}} ({{tr:ḥ-m-l}})\",\"root_gloss_range\":\"broad carrying range including lifting, bearing burdens, pregnancy, liability, gear, and endurance; local construction selects load-bearing agency with idiomatic and moral burden pressure, not unrelated branches as direct senses\",\"surface_display\":\"{{ar:حَمَّالَةَ}} ({{tr:ḥammālata}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:4:closure-weight","source_type":"word_analysis","support_id":"sup_30648dbe6a711de4d392","text":"{\"blocking_evidence\":null,\"headline\":\"ayah lands on the fuel object\",\"reader_payoff\":\"The reader feels the ayah close not on the wife or the act, but on the carried object that completes the verbless title.\",\"reason\":\"The word is the final genitive inside the compact nominal title, so it supplies both syntactic completion and acoustic closure.\",\"representative_source_ids\":[\"QG-77222936\",\"QT-3c3f6b4a\",\"QT-8a7198ae\",\"QT-bab22faa\",\"QB-3d73ae56\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:1:continuation-with-new-focus","source_type":"word_analysis","support_id":"sup_384d32e2e2798618efc0","text":"{\"blocking_evidence\":null,\"headline\":\"continuation with fresh nominal focus\",\"reader_payoff\":\"The reader can feel both dependency on what came before and a newly focused wife-description beginning at this ayah.\",\"reason\":\"The resumption claim is narrowed because local QAC favors coordination, but the nominal clause still creates fresh characterization after the connective.\",\"representative_source_ids\":[\"QG-e5cf9a42\",\"QS-9856ca11\",\"QT-c995515d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:4:concrete-bounded-fuel","source_type":"word_analysis","support_id":"sup_40183fda48f16d8502b1","text":"{\"blocking_evidence\":null,\"headline\":\"specific concrete fuel material\",\"reader_payoff\":\"The reader imagines a definite mass of combustible material, not an abstract idea or a single stray stick.\",\"reason\":\"The local noun is concrete, definite, and tied by V4 to firewood or fuel prepared for burning.\",\"representative_source_ids\":[\"QF-008c03b3\",\"QF-106f1a71\",\"QF-3f6b2ccf\",\"QF-49b93cab\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:3:derivational-burden-pressure","source_type":"word_analysis","support_id":"sup_53e022c81141225e04b7","text":"{\"blocking_evidence\":null,\"headline\":\"other carrying fields add burden pressure\",\"reader_payoff\":\"The reader senses the title as both active and weighed down, even though local grammar selects fuel-carrying rather than pregnancy, equipment, or other branch meanings.\",\"reason\":\"The wider root family supplies load-bearing pressure, but V4 branch separation keeps nonlocal pregnancy, gear, and similar branches from becoming direct local senses.\",\"representative_source_ids\":[\"QS-4d8716f7\",\"QS-701ed084\",\"QS-c678851b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:4:sound-and-cadence","source_type":"word_analysis","support_id":"sup_5581a35424c02c41be90","text":"{\"blocking_evidence\":null,\"headline\":\"rough sound and clipped cadence\",\"reader_payoff\":\"The reader can hear the definiteness boundary and rough consonants, then place the fuel-word inside the surah's clipped ending cadence.\",\"reason\":\"The phonetic rows are tied to the local surface and neighboring surah-end sound pattern.\",\"representative_source_ids\":[\"QP-a52d3c28\",\"QP-c1ab6ae4\",\"QP-c7030058\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:2:forward-feminine-reference","source_type":"word_analysis","support_id":"sup_59b226613af768a7ac52","text":"{\"blocking_evidence\":null,\"headline\":\"wife-reference continues into the neck image\",\"reader_payoff\":\"The reader tracks the same female referent from relational wife-language in 111:4 into the concrete neck image in 111:5.\",\"reason\":\"The forward rows give the concrete 111:5 reference, and the local feminine referent established here supplies the antecedent for that next image.\",\"representative_source_ids\":[\"QE-11baf89b\",\"QE-b5791cd6\",\"QB-df909af5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:3:compressed-idafa-action","source_type":"word_analysis","support_id":"sup_6495e13a1fa5c1701a14","text":"{\"blocking_evidence\":null,\"headline\":\"action compressed into a construct title\",\"reader_payoff\":\"The reader notices that the phrase works like a compact scene: carrier and fuel are bound into a title instead of expanded into a full verbal sentence.\",\"reason\":\"Attachment evidence makes {{ar:ٱلْحَطَبِ}} ({{tr:al-ḥaṭabi}}) the syntactically forced construct dependent of the intensive carrier form.\",\"representative_source_ids\":[\"QG-7df1188e\",\"QF-e83c4088\",\"QI-d4f337a7\",\"QT-9fe572e3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:1:surface-and-sound-fusion","source_type":"word_analysis","support_id":"sup_6546beab156cc2866eed","text":"{\"blocking_evidence\":null,\"headline\":\"connector fused to the wife-word\",\"reader_payoff\":\"The reader sees and hears the link as part of the wife-word's entry, so connection is built into the ayah's first beat.\",\"reason\":\"The proclitic form joins the connector to the following noun, and the recited liaison makes the syntactic joining audible.\",\"representative_source_ids\":[\"QF-d59d2c16\",\"QP-23e6b7e9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:4:near-hapax-rarity","source_type":"word_analysis","support_id":"sup_71ce057b99d59605419b","text":"{\"blocking_evidence\":null,\"headline\":\"rare fuel root carries extra weight\",\"reader_payoff\":\"The reader notices that this is not routine wood vocabulary; the near-hapax fuel root is concentrated between 111:4 and punishment-fuel usage at 72:15.\",\"reason\":\"Contextual evidence gives only two supplied occurrences for the root, including 111:4 and 72:15, making the distributional point locally relevant.\",\"representative_source_ids\":[\"QI-2790bf1a\",\"QE-dd32fd07\",\"QH-1a2b2644\",\"QH-370de224\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:2:nominative-nominal-frame","source_type":"word_analysis","support_id":"sup_960bcfb7f19ababeae84","text":"{\"blocking_evidence\":null,\"headline\":\"nominative subject in a verbless characterization\",\"reader_payoff\":\"The reader notices that the wife-word can carry both inherited coordination and nominal characterization without a finite verb in this ayah.\",\"reason\":\"QAC marks the noun nominative as subject under coordination, while attachment evidence keeps the following accusative epithet grammatically ambiguous enough to require careful predicational handling.\",\"representative_source_ids\":[\"QG-1f838357\",\"QG-6821e795\",\"QT-9014171e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:3:boundary-fire-and-binding","source_type":"word_analysis","support_id":"sup_9888cb362dc469c0d1c7","text":"{\"blocking_evidence\":null,\"headline\":\"fire scene turns toward carried burden and binding\",\"reader_payoff\":\"The reader sees the previous fire in 111:3 answered by a fuel-carrying role, then tightened toward bodily binding in 111:5.\",\"reason\":\"The boundary rows supply concrete references to 111:3 and 111:5, and the local carrier title mediates between fire and binding.\",\"representative_source_ids\":[\"QE-6a1ba806\",\"QB-a58376e7\",\"QB-b2c3290d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:4:surface-lexeme-weight","source_type":"word_analysis","support_id":"sup_9baeaaf0debab6526546","text":"{\"blocking_evidence\":null,\"headline\":\"exact definite lexeme bears local weight\",\"reader_payoff\":\"The reader sees the definite surface itself as significant: the word points to the known fuel inside this title and is not just a generic root occurrence.\",\"reason\":\"The definite article and low-occurrence profile make the exact local surface carry more than ordinary generic reference.\",\"representative_source_ids\":[\"QI-da1dc032\",\"QH-7ae8b07b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:4:material-field-to-binding","source_type":"word_analysis","support_id":"sup_a857ae5500f3bad8077c","text":"{\"blocking_evidence\":null,\"headline\":\"fuel bridges flame and rope material\",\"reader_payoff\":\"The reader follows the surah's material chain from fire and flame in 111:3, through carried fuel in 111:4, toward binding material in 111:5.\",\"reason\":\"The boundary evidence ties the fuel word to both the prior fire register and the forward rope-material image.\",\"representative_source_ids\":[\"QS-f2e530b2\",\"QB-1f4573a2\",\"QB-da1f45c9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:1:inherited-condemnation","source_type":"word_analysis","support_id":"sup_a87b9b78924b1d3b1792","text":"{\"blocking_evidence\":null,\"headline\":\"prior condemnation carried forward\",\"reader_payoff\":\"The reader notices that the wife enters the same doom-frame already established in 111:1-3, not an unrelated aside.\",\"reason\":\"QAC identifies the connector as coordination extending the preceding curse, and attachment evidence keeps the clause as a coordinated nominal description.\",\"representative_source_ids\":[\"QG-e1b333a7\",\"MG-686c4381\",\"QB-9a971f9e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"111:4:2:1","source_type":"qac_morpheme","support_id":"sup_acd4a757cbd0c6266c4b","text":"{\"lemma_ar\":\"حَمَّالَة\",\"morph_features\":\"STEM|POS:N|ACT|PCPL|LEM:Ham~aAlap|ROOT:Hml|FS|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"111:4:2:1\",\"qac_word_ref\":\"111:4:2\",\"root_ar\":\"ح م ل\",\"surface_ar\":\"حَمَّالَةَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:4:gathered-dangerous-material","source_type":"word_analysis","support_id":"sup_b69e51d4a5e9e403fe21","text":"{\"blocking_evidence\":null,\"headline\":\"fuel feels gathered and dangerous\",\"reader_payoff\":\"The reader sees the firewood as collected and harmful material, with the woodgatherer idiom sharpening the sense of blind or destructive gathering.\",\"reason\":\"The local noun selects fuel, while V4 preserves wood-gathering and idiomatic harmful collection as bounded pressures rather than the main grammatical sense.\",\"representative_source_ids\":[\"QS-0b2b6f4a\",\"QS-0cffe527\",\"QS-d14d9063\",\"QS-f8fd9e41\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:3:accusative-case-crux","source_type":"word_analysis","support_id":"sup_ba916136e76f053070d7","text":"{\"blocking_evidence\":null,\"headline\":\"accusative case carries interpretive force\",\"reader_payoff\":\"The reader notices that the accusative is part of the condemnation's grammar, not a disposable case detail.\",\"reason\":\"QAC and attachment evidence explicitly preserve the accusative debate among circumstantial, appositional, predicative, and censure analyses.\",\"representative_source_ids\":[\"QG-0976e788\",\"QG-2312cdaf\",\"QG-edb9b6c1\",\"MF-a2aa191c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:2:relational-anonymity-pattern","source_type":"word_analysis","support_id":"sup_be811686ddbee156c3d2","text":"{\"blocking_evidence\":null,\"headline\":\"relation replaces a personal name\",\"reader_payoff\":\"The reader notices a Quranic pattern of women identified by relation, here intensified because the ayah begins her story through his suffix before giving her epithet.\",\"reason\":\"Contextual profiles show frequent relational identification for this noun family, and the local suffix makes that distribution concrete in 111:4; the named examples remain comparative background at 28:9, 66:11, 12:51, 3:35, and 66:10.\",\"representative_source_ids\":[\"QI-6f748546\",\"QI-d6298ce0\",\"MI-04efd809\",\"QT-6f3655d7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:1","source_type":"word_analysis","support_id":"sup_bf62596796f21a98730a","text":"{\"gloss_range\":\"coordinating connector that carries the prior condemnation forward while allowing the ayah to open a focused nominal characterization\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) makes the ayah enter as continuation before the wife is named. The strongest local grammar treats it as coordination, drawing {{ar:ٱمْرَأَتُهُۥ}} ({{tr:mra'atuhu}}) into the condemnation already moving through 111:1-3, while the nominal opening still gives her description a fresh focus. Because the particle is fused onto the wife-word, the reader sees and hears connection before identity: the ayah does not float as a detached label, but carries the prior burning frame into {{ar:حَمَّالَةَ ٱلْحَطَبِ}} ({{tr:ḥammālata l-ḥaṭabi}}).\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"111:4:1:2","source_type":"qac_morpheme","support_id":"sup_c5a90f79b233d608d989","text":"{\"lemma_ar\":\"ٱمْرَأَت\",\"morph_features\":\"STEM|POS:N|LEM:{mora>at|ROOT:mrA|F|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"111:4:1:2\",\"qac_word_ref\":\"111:4:1\",\"root_ar\":\"م ر ء\",\"surface_ar\":\"ٱمْرَأَتُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:4:case-variant-contrast","source_type":"word_analysis","support_id":"sup_c72df9dc8bb3f5292ebd","text":"{\"blocking_evidence\":null,\"headline\":\"variant accusative contrasts with received genitive\",\"reader_payoff\":\"The reader sees how an accusative-object variant would make carrying more event-like, clarifying that the received genitive makes the phrase more title-like.\",\"reason\":\"The variant is useful as contrast, while the supplied local form remains genitive inside the construct.\",\"representative_source_ids\":[\"QG-cac64421\",\"QF-96078186\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:4:fire-field-and-material-cause","source_type":"word_analysis","support_id":"sup_c86e453f66208fde565c","text":"{\"blocking_evidence\":null,\"headline\":\"fuel answers the prior fire\",\"reader_payoff\":\"The reader notices the effect-before-cause movement: 111:3 gives fire and flame, then 111:4 names the fuel that sustains them.\",\"reason\":\"The boundary rows supply concrete same-surah references, and the local fuel noun naturally answers the fire field of 111:3.\",\"representative_source_ids\":[\"QS-c74ec585\",\"QI-cf9e6898\",\"QE-a2722e3e\",\"QB-4d69c4d6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:2:hamza-interruption","source_type":"word_analysis","support_id":"sup_c8cf9df630adc19072e3","text":"{\"blocking_evidence\":null,\"headline\":\"internal glottal interruption\",\"reader_payoff\":\"The reader can hear a small break inside the relational noun, matching the abrupt insertion of the second condemned figure.\",\"reason\":\"The sound observation is form-specific and does not conflict with the local morphology.\",\"representative_source_ids\":[\"QP-b6bd81ed\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:4:convergence","source_type":"word_analysis","support_id":"sup_c8d0c64dd186b0d738b3","text":"{\"blocking_evidence\":null,\"headline\":\"sense, rarity, boundary, and sound converge\",\"reader_payoff\":\"The reader sees the final noun as a compact convergence of fuel sense, rare distribution, fire-boundary logic, and rough sound.\",\"reason\":\"The synthesis row survives because each component payoff remains locally licensed after narrowing literal, idiomatic, distributional, and sound claims.\",\"representative_source_ids\":[\"QY-4b545f43\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:4:definite-genitive-construct","source_type":"word_analysis","support_id":"sup_d5242eed7f6054b50233","text":"{\"blocking_evidence\":null,\"headline\":\"definite genitive completes the title\",\"reader_payoff\":\"The reader notices that the fuel is not a loose noun after the epithet; it is the definite genitive object that completes the carrier-title.\",\"reason\":\"QAC and attachment evidence make the word genitive as the construct dependent of the carrier title, with definiteness carried by the fuel noun.\",\"representative_source_ids\":[\"QG-74aa0c8d\",\"QG-bd3b7049\",\"QG-efd28d89\",\"QG-e22154ff\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:1:structural-cumulative-link","source_type":"word_analysis","support_id":"sup_de5bfacc8ba1590b8d53","text":"{\"blocking_evidence\":null,\"headline\":\"addition stays structurally cumulative\",\"reader_payoff\":\"The reader notices that the conjunction makes the wife's mention a cumulative addition to the prior scene rather than a loose appositive fragment.\",\"reason\":\"The coordinated nominal construction prevents the wife phrase from becoming an unattached descriptive fragment.\",\"representative_source_ids\":[\"QT-f63db675\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:3:qiraat-case-contrast","source_type":"word_analysis","support_id":"sup_e277eaec5622f85863b6","text":"{\"blocking_evidence\":null,\"headline\":\"variant case contrasts with received accusative\",\"reader_payoff\":\"The reader can see how a nominative reading would make the epithet more directly predicate-like, clarifying what the received accusative leaves charged and debated.\",\"reason\":\"The variant is useful as contrast, while the local surface remains the accusative form supplied by QAC.\",\"representative_source_ids\":[\"QG-70d1bf8d\",\"QF-0ac1b2a5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:2","source_type":"word_analysis","support_id":"sup_e2a33a0156abdfdc7a3f","text":"{\"gloss_range\":\"wife or woman, locally narrowed by the attached masculine suffix to a particular wife identified through the prior male referent\",\"prose\":\"{{ar:ٱمْرَأَتُهُۥ}} ({{tr:mra'atuhu}}) identifies the woman through relation before action. The feminine noun is nominative and can participate in the inherited coordination or begin a nominal characterization, but the attached masculine suffix fixes her textual access through the condemned man from 111:1. That makes the word definite without naming her: one particular wife is introduced as his, matching a wider Quranic habit of identifying some women through relation (28:9, 66:11, 12:51, 3:35, 66:10), then recharacterized by {{ar:حَمَّالَةَ}} ({{tr:ḥammālata}}). The broader woman/person term remains audible, but local grammar narrows it to spouse-relation; the internal hamza gives the word a small audible break before the possessive ending. That relation is then carried forward into the body image of {{ar:جِيدِهَا}} ({{tr:jīdihā}}) in 111:5.\",\"root_display\":\"{{ar:م ر أ}} ({{tr:m-r-'}})\",\"root_gloss_range\":\"person and woman/wife range with broader personhood associations; local grammar selects the relational wife sense and does not license unrelated root-family senses as the main meaning\",\"surface_display\":\"{{ar:ٱمْرَأَتُهُۥ}} ({{tr:mra'atuhu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:3:sound-weight-and-local-reprise","source_type":"word_analysis","support_id":"sup_ec1ee7897aab941471b6","text":"{\"blocking_evidence\":null,\"headline\":\"sound makes the load feel heavy\",\"reader_payoff\":\"The reader can hear the carrier title as weighty, with the doubled middle sound and repeated rough onset binding the carrier to the fuel.\",\"reason\":\"The sound rows are form-specific and align with the local carrier-plus-fuel phrase.\",\"representative_source_ids\":[\"QE-ac2df661\",\"QP-0a18cd39\",\"QP-8ea95bc6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:2:annexed-feminine-form","source_type":"word_analysis","support_id":"sup_ec86a76fc82119bdfec2","text":"{\"blocking_evidence\":null,\"headline\":\"feminine noun carries masculine possession\",\"reader_payoff\":\"The reader notices the gendered compression inside one word: a feminine singular person is introduced with the masculine possessor fused to her form.\",\"reason\":\"The QAC noun analysis and attachment row for the possessive suffix support the fused feminine noun plus masculine possessor reading.\",\"representative_source_ids\":[\"QF-353c645b\",\"QF-49570558\",\"QF-9133064f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:4:literal-social-hell-fuel","source_type":"word_analysis","support_id":"sup_ee06c5936ebb21a4bf9b","text":"{\"blocking_evidence\":null,\"headline\":\"literal fuel with social and punishment resonance\",\"reader_payoff\":\"The reader keeps three bounded pressures together: material firewood, social kindling, and punishment-fuel resonance through 72:15.\",\"reason\":\"V4 supports both firewood and tale-bearing fuel senses, and contextual evidence preserves the paired 72:15 occurrence; local adjacency to fire keeps literal combustible fuel primary.\",\"representative_source_ids\":[\"QS-3018ab0a\",\"QS-94cf8649\",\"QS-c6dc9188\",\"MH-f0ad896f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:3:marked-form-rarity","source_type":"word_analysis","support_id":"sup_f07334004e799172f797","text":"{\"blocking_evidence\":null,\"headline\":\"rare intensive form inside a common root\",\"reader_payoff\":\"The reader notices that the text selects an unusual intensive title from a root that otherwise has many ordinary carrying forms.\",\"reason\":\"The contextual profile marks the exact intensive form as a single low-occurrence instance, so its selection is distributionally sharp.\",\"representative_source_ids\":[\"QI-5115f726\",\"QH-85f1a37f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:3:burden-and-idiom","source_type":"word_analysis","support_id":"sup_f35ec805641eaa46e018","text":"{\"blocking_evidence\":null,\"headline\":\"literal burden and social harm remain together\",\"reader_payoff\":\"The reader feels both the weight of carried fuel and the idiomatic force of carrying enmity or slander, with 111:3 preventing the phrase from becoming merely figurative.\",\"reason\":\"V4 supports carrying, burden, and related idiomatic pressure, while the local construct and prior fire-frame keep literal fuel selected.\",\"representative_source_ids\":[\"QS-0e22b447\",\"QS-75dd77c3\",\"QS-e2ae72a4\",\"QB-17c7fe17\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"111:4:2:wife-woman-personhood","source_type":"word_analysis","support_id":"sup_f9d2717a89e019371e9d","text":"{\"blocking_evidence\":null,\"headline\":\"wife sense selected from woman/person range\",\"reader_payoff\":\"The reader hears a standard woman/person term narrowed into spouse-relation, making the later harmful epithet sharper against ordinary personhood language.\",\"reason\":\"The suffix selects the wife sense locally; broader personhood and root-family associations are retained only as lexical pressure because no V4 guardrail rows are available for this root.\",\"representative_source_ids\":[\"QS-58e7c537\",\"QS-f9d481de\",\"QS-d96553e4\",\"QS-be9cc64a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"111:4:3:2","source_type":"qac_morpheme","support_id":"sup_fdcca1947d052b46eb27","text":"{\"lemma_ar\":\"حَطَب\",\"morph_features\":\"STEM|POS:N|LEM:HaTab|ROOT:HTb|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"111:4:3:2\",\"qac_word_ref\":\"111:4:3\",\"root_ar\":\"ح ط ب\",\"surface_ar\":\"حَطَبِ\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ","ayah_ref":"111:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000335/B001","root_000357/B001","root_001409/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001409","role":"The person-and-woman branch fixes the wife as the human operator of the mechanism.","root":"م ر ء","source_ref":"111:4","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000357","role":"The outward-load branch supplies recurrent lifting, transport, and delivery as her role.","root":"ح م ل","source_ref":"111:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000335","role":"The gathered-firewood branch identifies the cargo as prepared fuel rather than an inert object.","root":"ح ط ب","source_ref":"111:4","source_word_indices":["3"]}],"changed_reading":{"after":"The line depicts a repeated fuel-supply operation, with the wife as the active logistical hinge between gathering and ignition.","before":"A wife is labeled as someone carrying firewood."},"confidence":"strong","focus_anchor":"The agent noun حَمَّالَةَ governs the genitive cargo ٱلْحَطَبِ and is predicated of ٱمْرَأَتُهُ.","mechanism":"The intensive feminine carrier, outward-load branch, and gathered-fuel branch form a compact supply chain: a human agent repeatedly turns scattered wood into portable ignition stock.","model_id":"baseline_outward_fuel_logistics"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_outward_fuel_logistics","source_type":"hft","support_id":"sup_228cf238a28dc4f1b0e2","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ","ayah_ref":"111:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000335/B003","root_000357/B001","root_001409/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001409","role":"The woman branch retains a concrete accountable agent behind the figurative traffic.","root":"م ر ء","source_ref":"111:4","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000357","role":"The outward-bearing branch makes harmful material transferable from one social location to another.","root":"ح م ل","source_ref":"111:4","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000335","role":"The tale-bearing branch supplies the explicit social image of carrying material that kindles harm between people.","root":"ح ط ب","source_ref":"111:4","source_word_indices":["3"]}],"changed_reading":{"after":"The cargo can coexist as transported speech or agitation whose social effect is to furnish a fire.","before":"The cargo is physical wood for a physical fire."},"confidence":"medium","focus_anchor":"حَمَّالَةَ ٱلْحَطَبِ remains a carrying construction, while the cargo root itself contains the tale-bearing idiom.","mechanism":"The firewood branch converts reports, slander, or agitation into portable fuel; intensive carrying makes social harm a repeated traffic rather than a single utterance.","model_id":"baseline_social_ignition_bearer"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_social_ignition_bearer","source_type":"hft","support_id":"sup_54c9ccb0d4c2ae467b9f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ","ayah_ref":"111:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000335/B002","root_000357/B007"],"payload":{"activation_trace":[{"branch_id":"B007","mapped_root_id":"root_000357","role":"The strained self-burdening branch supplies the mounting cost of carrying what has been accumulated.","root":"ح م ل","source_ref":"111:4","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000335","role":"The night-gatherer branch contributes blind mixture, excess, and the risk that the gathered bundle harms its gatherer.","root":"ح ط ب","source_ref":"111:4","source_word_indices":["3"]}],"changed_reading":{"after":"The title also pictures compulsive, poorly discriminating accumulation whose burden and hidden contents recoil on the collector.","before":"The carrier knowingly assembles a uniform and useful load."},"confidence":"medium","focus_anchor":"The intensive حَمَّالَةَ is attached to حَطَب, whose inventory includes the night gatherer who cannot inspect the bundle.","mechanism":"Repeated gathering becomes indiscriminate accumulation: good and bad material are bundled together, the load grows through unexamined collection, and the collector is exposed to the danger inside it.","model_id":"baseline_indiscriminate_bundle"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_indiscriminate_bundle","source_type":"hft","support_id":"sup_2c11658836d19a99e374","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ","ayah_ref":"111:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000335/B001","root_000357/B002","root_001409/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001409","role":"The woman branch makes the gestational resonance embodied rather than merely botanical.","root":"م ر ء","source_ref":"111:4","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000357","role":"The inward-bearing and fruit branch supplies pregnancy and a tree carrying its yield as the latent positive pattern.","root":"ح م ل","source_ref":"111:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000335","role":"The fuel branch includes cut vine wood, replacing living yield with dry material prepared for burning.","root":"ح ط ب","source_ref":"111:4","source_word_indices":["3"]}],"changed_reading":{"after":"Her bearing can also register as inverted generativity: the expected fruit of woman or tree has become dead fuel.","before":"A woman bears an external load of wood."},"confidence":"exploratory","focus_anchor":"A woman is named by an intensive form from ح م ل, but what she bears is dead combustible wood.","mechanism":"The inward-bearing and tree-fruit branch of carrying activates gestation and fruition, while the cargo branch includes vine wood cut down for fuel. The result is an anti-fruit image: bearing yields combustible residue rather than life or nourishment.","model_id":"baseline_inverted_fruition"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_inverted_fruition","source_type":"hft","support_id":"sup_02e67034803912d704c0","trust":"legacy_unbound"}]}
</lane_packet_json>
