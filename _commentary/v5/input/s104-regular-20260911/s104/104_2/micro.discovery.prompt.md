# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **104:2**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s104-regular-20260911/s104/104_2/micro.discovery.json` and modify nothing
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
  "ayah_ref": "104:2",
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
{"analysis_context":{"analysis_id":"s104-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"104:2","host_surah":104,"lane_context_refs":[],"ordered_context_refs":["104:0","104:1","104:3","104:4","104:5","104:6","104:7","104:8","104:9","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Çekirdek toplama eylemidir; mal biriktirme ve yağma malını derleme gibi özel kullanımlar bütün dala yayılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000259/B001","candidate_links":[{"candidate_id":"cand_917b63e73e3876d74363","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَمَعَ","morph_features":"STEM|POS:V|PERF|LEM:jamaEa|ROOT:jmE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:2:1","qac_word_ref":"104:2:2","surface_ar":"جَمَعَ"}],"gloss":"dağınık parçaları bir araya toplama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ayrı parçalar birbirine yaklaştırılır ve dağınıklık sona erdirilir."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dağınık öğelerin yaklaştırılıp tek bir topluluk durumuna getirildiği genel çekirdeği karşılar.","boundary_detail":"Çekirdek toplama eylemidir; mal biriktirme ve yağma malını derleme gibi özel kullanımlar bütün dala yayılmaz.","branch_image_ar":"ضم المتفرق حتى يصير شيئا مجموعا","concept_gloss":"dağınık parçaları bir araya toplama","contextual_glosses":[{"applicability":"Nesnelerin veya kişilerin ayrı yerlerden tek yerde toplandığı cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ayrı olanları yaklaştırıp birlikte bulundurma sonucunu korur."},"facet_ids":["F001"],"text":"bir araya getirmek","usage_role":"general"}],"definition":"Önceden ayrı veya dağınık duran parçaları birbirine yaklaştırarak bir araya getirme eylemidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ayrı parçalar birbirine yaklaştırılır ve dağınıklık sona erdirilir."}],"identity_rationale":"Kaynak ifadesi, dağınık parçaların birbirine yaklaştırılıp bir araya getirilmesini açıkça ortak anlam çekirdeği olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"dağınık şeyi bir araya toplamak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"mal biriktirmek ve saymak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"ayrı yerlerdeki şeyleri bütünüyle bir araya getirmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"çeşitli yerlerden toplanmış şey"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"çeşitli yerlerden toplanıp götürülen yağma malı"}],"lexicalization_note":"Tanım genel toplama çekirdeğini korur; mal ve yağma malıyla ilgili anlamları yalnız kendi özel birimlerinde tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; işlem ile ortaya çıkan insan topluluğu arasındaki ayrım en yararlı karşılaştırma olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal birleştirme işlemini anlatır; komşu dal ise özellikle insanların oluşturduğu topluluğu adlandırır.","focus_only":"Dağınık parçaları birbirine yaklaştıran eylem ve süreçtir.","gloss":"bir araya gelmiş insan topluluğu","neighbor_only":"Eylemin sonucu olarak bir arada bulunan insan topluluğudur.","neighbor_ref":"root_000259/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da ayrılığın yerini bir arada bulunma durumu alır."}],"source_phrase_ar":"أصل واحد يدل على تضام الشيء (maqayis)؛ الجمع مصدر جمعت الشيء (ayn)؛ الجمع خلاف التفريق جمعت الشيء إذا ضممت بعضه إلى بعض (jamhara)؛ جمعت الشئ المتفرق فاجتمع (sihah)؛ الجمع أن تجمع شيئا إلى شيء (tahdhib)؛ الجمع ضم الشيء بتقريب بعضه من بعض (mufradat)","source_summary":"Kaynakların ortak anlatımı, toplamanın karşıtını dağıtma olarak görür ve eylemi bir şeyi başka bir şeye katıp parçaları yakınlaştırma biçiminde açıklar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه جمع الشيء أو المال أو القوم، وجعل المتفرق جميعا، وما جمع من مواضع شتى كنهب مجمع.","what_is_not_ar":"لا يدخل فيه عزم الرأي وحده ولا أسماء الأزمنة والمواضع إلا من جهة سبب التسمية."},"support_links":["sup_b514cf3087189c74b36c"]},{"boundary":"Dal, toplama eylemini değil bir araya gelmiş insanları; cinsel birleşme anlamını değil insan topluluğunu gösterir.","branch_kind":"bare","branch_ref":"root_000259/B002","candidate_links":[{"candidate_id":"cand_22cd05023d5dcbb1f72e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَمَعَ","morph_features":"STEM|POS:V|PERF|LEM:jamaEa|ROOT:jmE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:2:1","qac_word_ref":"104:2:2","surface_ar":"جَمَعَ"}],"gloss":"bir araya gelmiş insan topluluğu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birden çok insan bir arada bulunan bir topluluk oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Topluluk farklı boylardan veya kesimlerden gelen karışık insanlardan oluşabilir."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsanların birlikte bir küme oluşturduğu genel anlamı ve karışık kökenli topluluk özel durumunu kapsar.","boundary_detail":"Dal, toplama eylemini değil bir araya gelmiş insanları; cinsel birleşme anlamını değil insan topluluğunu gösterir.","branch_image_ar":"جماعة اجتمعت أو أخلاط ضمتها الجهة","concept_gloss":"bir araya gelmiş insan topluluğu","contextual_glosses":[{"applicability":"Farklı boy veya kesimlerden gelen kişilerin oluşturduğu topluluk anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluk olmayı ve üyelerin farklı kökenlerden gelmesini birlikte korur."},"facet_ids":["F002"],"text":"karışık bir insan topluluğu","usage_role":"contextual"}],"definition":"Bir araya gelerek topluluk oluşturan insanlar, özellikle farklı boylardan veya kesimlerden gelmiş karışık bir insan kümesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birden çok insan bir arada bulunan bir topluluk oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Topluluk farklı boylardan veya kesimlerden gelen karışık insanlardan oluşabilir."}],"identity_rationale":"Kaynak ifadesi hem genel insan topluluğunu hem de farklı boylardan gelmiş karışık insan kümesini doğrudan tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"insan topluluğu veya çokluk"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"farklı boylardan karışık insan topluluğu"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"toplanmış topluluk veya ordu"}],"lexicalization_note":"Tanım çıplak dalın insan topluluğu anlamıyla sınırlıdır ve başka dallardaki eylem ya da cinsellik anlamlarını içermez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; insan grubu çekirdeğini paylaşırken üye türü ve karışık köken bakımından ayrılan aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Örtüşme insan topluluğundadır; bu dal karışık kökeni de anlatabilirken komşu dal hayvan sürülerine uzanır.","focus_only":"Farklı boylardan gelen karışık insan topluluğunu da kapsar.","gloss":"insan veya sürü topluluğu","neighbor_only":"İnsanların yanı sıra çok sayıdaki koyun veya keçi topluluğunu da kapsar.","neighbor_ref":"root_001184/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir arada bulunan insan grubunu adlandırabilir."}],"source_phrase_ar":"الجماع الأشابة من قبائل شتى (maqayis)؛ الجمع اسم لجماعة الناس والجموع اسم لجماعة الناس (ayn)؛ الجماع ما تجمع من أشابة الناس وأخلاطهم (jamhara)؛ جماع الناس أخلاطهم وهم الأشابة من قبائل شتى (sihah)؛ الجماع يقال في أقوام متفاوتة اجتمعوا (mufradat)","source_summary":"Ortak anlatım, sözü bir insan topluluğunun adı olarak verir; bazı anlatımlarda bu topluluğun farklı boylardan gelen karışık kişilerden oluştuğu özellikle belirtilir.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الجمع والجموع والجميع والجماعة والجماع إذا أريد بها جماعة الناس أو أخلاطهم أو الجيش.","what_is_not_ar":"لا يدخل فيه فعل الجمع نفسه، ولا الجماع بمعنى النكاح."},"support_links":["sup_f2abf7bb10381f8f7a58"]},{"boundary":"Dalın çekirdeği kesin yöneliş ve sağlamlaştırmadır; birden çok kişinin görüş birliği bütün kullanımlara genellenmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000259/B003","candidate_links":[{"candidate_id":"cand_e6ef28d6527586d5e78e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَمَعَ","morph_features":"STEM|POS:V|PERF|LEM:jamaEa|ROOT:jmE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:2:1","qac_word_ref":"104:2:2","surface_ar":"جَمَعَ"}],"gloss":"düşünüp kesin bir tutuma bağlanma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Düşünme ve hazırlığın ardından bir işi yapma yönünde kesin tutum alınır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İş veya düzen, dağınık düşünceler bir sonuca bağlanarak sağlamlaştırılır."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir işin düşünme ve hazırlık sonrasında kesinleştirildiği çekirdeği karşılar.","boundary_detail":"Dalın çekirdeği kesin yöneliş ve sağlamlaştırmadır; birden çok kişinin görüş birliği bütün kullanımlara genellenmez.","branch_image_ar":"عزم محكم جمع الرأي بعد تفرقه","concept_gloss":"düşünüp kesin bir tutuma bağlanma","contextual_glosses":[{"applicability":"Bir iş veya tasarı üzerinde düşünüldükten sonra geri dönülmez bir tutum alındığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Düşünme sonunda kararı ve işi sağlamlaştırma yönünü korur."},"facet_ids":["F001","F002"],"text":"iyice düşünüp kesinleştirmek","usage_role":"general"}],"definition":"Bir işi düşünüp hazırladıktan sonra onu yapmaya kesin biçimde bağlanma ve tutumu sağlamlaştırmadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Düşünme ve hazırlığın ardından bir işi yapma yönünde kesin tutum alınır."},{"facet_id":"F002","role":"specialization","statement":"İş veya düzen, dağınık düşünceler bir sonuca bağlanarak sağlamlaştırılır."}],"identity_rationale":"Kaynak ifadesi düşünme sonunda bir işe kesin biçimde yönelmeyi, hazırlanmayı ve işi sağlamlaştırmayı destekler; görüş birliği ise yalnız ayrı bir söz biriminde belirgindir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bir işi yapmaya kesin biçimde karar vermek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"hazırlık, kesin karar veya görüş birliği"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"işi veya düzeni sağlamlaştırıp kesinleştirmek"}],"lexicalization_note":"Genel kesin yöneliş ile işi veya düzeni sağlamlaştıran özel yapılar ayrılır; görüş birliği yalnız ilgili birimde tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kesin karar ile başkasıyla ortak davranma arasındaki sınır en güçlü karışma noktasıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kararın kesinleşmesine odaklanır; komşu dal ise ikinci bir katılımcıyla birlikte davranma ilişkisini zorunlu kılar.","focus_only":"Kişinin veya kurulun düşünüp kesin bir tutuma varmasını anlatır.","gloss":"bir işte başkasıyla güç birliği yapma","neighbor_only":"Başka biriyle aynı iş üzerinde birleşip ona destek olmayı gerektirir.","neighbor_ref":"root_000259/B013","relation_type":"near_neighbor","shared_zone":"Her iki dalda da belirli bir iş üzerinde birleşme ve dağınıklığı giderme vardır."}],"source_phrase_ar":"أجمعت على الأمر إجماعا وأجمعته (maqayis)؛ أجمعت على الأمر إجماعا إذا عزمت عليه (jamhara)؛ أجمعت الأمر وعلى الأمر إذا عزمت عليه (sihah)؛ الإجماع الإعداد والعزيمة على الأمر (tahdhib)؛ أجمعت كذا فيما يكون جمعا يتوصل إليه بالفكرة (mufradat)","source_summary":"Kaynaklar bir işe yönelmeyi kesin karar, hazırlık ve sağlamlaştırma yönleriyle açıklar; düşünerek bir sonuca varma bu anlatımları birbirine bağlar.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه أجمع على الأمر، أجمع الأمر أو الكيد، الإجماع بمعنى الإعداد والعزيمة والإحكام، واجتماع الآراء على تدبير.","what_is_not_ar":"لا يدخل فيه مجرد جمع الأجسام أو اجتماع الناس في مكان."},"support_links":["sup_953f1ed2d7f138323bde"]},{"boundary":"Dal çekirdeği toplanmayla belirlenen yer veya gündür; ibadet çağrısı ve ıssız alan kullanımları genel tanımı genişletmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000259/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمَعَ","morph_features":"STEM|POS:V|PERF|LEM:jamaEa|ROOT:jmE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:2:1","qac_word_ref":"104:2:2","surface_ar":"جَمَعَ"}],"gloss":"toplanmayla belirlenen yer veya gün","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yer, insanların orada toplanması nedeniyle bu anlamla adlandırılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir gün, insanların ibadet veya yeniden bir araya geliş için toplanmasıyla belirlenir."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsanların bir araya gelmesinin bir yerin ya da günün adı ve işlevi için belirleyici olduğu kullanımları kapsar.","boundary_detail":"Dal çekirdeği toplanmayla belirlenen yer veya gündür; ibadet çağrısı ve ıssız alan kullanımları genel tanımı genişletmez.","branch_image_ar":"موضع أو يوم أو نداء يجمع الناس","concept_gloss":"toplanmayla belirlenen yer veya gün","contextual_glosses":[{"applicability":"Bir yerin insanları bir araya getirme işlevi öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yer ile insanların orada toplanması arasındaki bağı korur."},"facet_ids":["F001"],"text":"insanların toplandığı yer","usage_role":"contextual"}],"definition":"İnsanların bir araya gelmesi nedeniyle adı veya işlevi belirlenen bir yer ya da gündür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yer, insanların orada toplanması nedeniyle bu anlamla adlandırılır."},{"facet_id":"F002","role":"specialization","statement":"Bir gün, insanların ibadet veya yeniden bir araya geliş için toplanmasıyla belirlenir."}],"identity_rationale":"Kaynak ifadesi insanların toplanması nedeniyle adlandırılmış yerleri ve günleri açıkça destekler; çağrı ve başka özel yapılar yalnız ayrı söz birimlerinde bulunur.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"insanların toplandığı yer"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"insanların bir araya geldiği kutsal yer veya günler için kullanılan ad"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"insanların ibadet veya yeniden diriliş için toplandığı gün"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"haftalık toplu ibadete katılıp namazı kılmak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"halkı toplu ibadet için bir araya getiren ibadet yeri"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ibadet için toplanma çağrısı"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yolunu yitirme korkusuyla insanların ayrılmadığı ıssız alan"}],"lexicalization_note":"Yer ve gün çekirdeği korunur; ibadet yeri, çağrı ve ayrılmama anlatan özel yapılar kendi birimleriyle sınırlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; toplantı yeriyle olan yakınlık ve günlere uzanan kapsam farkı en açıklayıcı karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yer veya günün toplanmayla adlandırılmasına odaklanır; komşu dal toplantı yerini, oradaki etkinliği ve topluluğu kapsar.","focus_only":"Toplanma nedeniyle adlandırılmış günleri ve özel yerleri birlikte kapsar.","gloss":"toplantı yeri ve topluluğu","neighbor_only":"Toplantı yerindeki konuşma, danışma ve orada bulunan topluluğu da kapsar.","neighbor_ref":"root_001487/B003","relation_type":"near_neighbor","shared_zone":"İki dal da insanların bir araya geldiği yeri anlatabilir."}],"source_phrase_ar":"جمع مكة سمي لاجتماع الناس به وكذلك يوم الجمعة (maqayis)؛ المجمع حيث يجمع الناس (ayn)؛ أيام جمع أيام منى والجمعة مشتقة من اجتماع الناس فيها للصلاة (jamhara)؛ يقال للمزدلفة جمع لاجتماع الناس فيها (sihah)؛ يوم الجمع ويوم يجمعكم ليوم الجمع (mufradat)","source_summary":"Kaynakların ortak noktası, belirli yer ve gün adlarını insanların oralarda veya o zamanlarda toplanmasıyla açıklamalarıdır.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه المجمع والموضع الذي يجتمع فيه الناس، وجمع للمزدلفة أو أيام منى، ويوم الجمعة ويوم الجمع، والمسجد الجامع، ونداء الصلاة جامعة، وفلاة مجمعة.","what_is_not_ar":"لا يدخل فيه الجماعة نفسها إذا لم يكن اللفظ زمنا أو موضعا أو نداء."},"support_links":[]},{"boundary":"Anlam genel sayısal çokluk değildir; sıkılmış avucun biçimi, vuruşu veya alabildiği miktarla sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000259/B005","candidate_links":[{"candidate_id":"cand_f61c7111d334cc9cf9cf","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَمَعَ","morph_features":"STEM|POS:V|PERF|LEM:jamaEa|ROOT:jmE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:2:1","qac_word_ref":"104:2:2","surface_ar":"جَمَعَ"}],"gloss":"sıkılmış avuç veya bir avuçluk miktar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Parmakların kapanmasıyla el sıkılmış bir avuç biçimi alır ve bu biçimle vurulabilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sıkılmış avucun aldığı şey bir avuçluk miktar olarak ölçülür."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Elin kapanmış biçimini, onunla vurmayı ve bu elin aldığı miktarı birlikte kapsar.","boundary_detail":"Anlam genel sayısal çokluk değildir; sıkılmış avucun biçimi, vuruşu veya alabildiği miktarla sınırlıdır.","branch_image_ar":"قبضة الكف إذا ضمت الأصابع","concept_gloss":"sıkılmış avuç veya bir avuçluk miktar","contextual_glosses":[{"applicability":"Meyve, para veya benzeri bir şeyin avucun alacağı miktarı anlatırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Miktarın kapalı avucun kapasitesiyle belirlenmesini korur."},"facet_ids":["F002"],"text":"bir avuç dolusu","usage_role":"contextual"}],"definition":"Parmaklar içe kapanınca oluşan sıkılmış avuç ve bu avucun kavrayabildiği miktardır; aynı el biçimiyle vurma da buna bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Parmakların kapanmasıyla el sıkılmış bir avuç biçimi alır ve bu biçimle vurulabilir."},{"facet_id":"F002","role":"extension","statement":"Sıkılmış avucun aldığı şey bir avuçluk miktar olarak ölçülür."}],"identity_rationale":"Kaynak ifadesi parmaklar kapanınca oluşan sıkılmış avucu, onunla vurmayı ve avuç miktarını aynı somut biçim çevresinde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"sıkılmış avuç veya bu avuçla vurma"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bir avuç dolusu"}],"lexicalization_note":"Sıkılmış avuç çekirdeği ile avuç dolusu miktar ve bu avuçla vurma kullanımları birbirinden açıkça ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; avucun biçimi ile avuçlayarak alma eylemi arasındaki ayrım okuyucu için en yararlı sınırdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal el biçimi ve ondan doğan ölçüdür; komşu dal ise o elle bir şeyi tutup alma eylemidir.","focus_only":"Kapalı avucun biçimini, vuruşunu ve aldığı miktarı adlandırır.","gloss":"avuçlayarak almak","neighbor_only":"Bir şeyi bütün avuçla kavrayıp alma eylemini anlatır.","neighbor_ref":"root_001197/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da parmakların bir şey çevresinde kapanması belirleyicidir."}],"source_phrase_ar":"ضربته بجمع كفي وجمع كفي (maqayis)؛ ضربته بجمع كفي وأعطيته من الدراهم جمع الكف (ayn)؛ ضربته بجمع يدي إذا ضممت كفك ثم ضربته بها (jamhara)؛ جمع الكف وهو حين تقبضها وجمعة من تمر أي قبضة منه (sihah)","source_summary":"Ortak anlatım sıkılmış avucu temel alır; bu avuçla vurmayı ve avucun doldurduğu para ya da meyve miktarını aynı biçime bağlar.","sources":["MQ","AY","JA","SI"],"what_is_ar":"يدخل فيه جمع الكف، الضرب بجمع الكف، ملء الجمع، والقبضة أو جمعة التمر.","what_is_not_ar":"لا يدخل فيه مطلق الجمع العددي إلا إذا كان بمقدار الكف."},"support_links":["sup_e1c1edb9f0088e300aa6"]},{"boundary":"Dal yalnız cinsel birleşmeyi anlatır; insan topluluğu ya da gebelikle birlikte kalma anlamları bu sınıra girmez.","branch_kind":"bare","branch_ref":"root_000259/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمَعَ","morph_features":"STEM|POS:V|PERF|LEM:jamaEa|ROOT:jmE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:2:1","qac_word_ref":"104:2:2","surface_ar":"جَمَعَ"}],"gloss":"cinsel birleşme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadınla erkek arasında cinsel birleşme gerçekleşir ve söz bunu doğrudan ya da örtülü biçimde anlatır."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kadınla erkek arasındaki cinsel birleşmenin doğrudan veya örtülü biçimde anlatıldığı kullanımları karşılar.","boundary_detail":"Dal yalnız cinsel birleşmeyi anlatır; insan topluluğu ya da gebelikle birlikte kalma anlamları bu sınıra girmez.","branch_image_ar":"اتصال الجماع والمجامعة","concept_gloss":"cinsel birleşme","contextual_glosses":[{"applicability":"Eylemin doğal ve açık bir Türkçe yüklemle verilmesi gereken cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki kişi arasındaki cinsel birleşme eylemini korur."},"facet_ids":["F001"],"text":"cinsel ilişkide bulunmak","usage_role":"general"}],"definition":"Kadınla erkek arasındaki cinsel birleşme veya bu birleşmeyi anlatan örtülü söyleyiştir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadınla erkek arasında cinsel birleşme gerçekleşir ve söz bunu doğrudan ya da örtülü biçimde anlatır."}],"identity_rationale":"Kaynak ifadesi iki biçimi de kadınla erkek arasındaki cinsel birleşmenin dolaylı veya doğrudan anlatımı olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"cinsel birleşme için kullanılan örtülü söz"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"cinsel ilişkide bulunma"}],"lexicalization_note":"Tanım çıplak dalın cinsel birleşme anlamını verir ve aynı ses dizisine bağlı topluluk anlamını dışarıda bırakır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı çekirdek ve sınıra sahip örtülü cinsel birleşme dalı eş anlamlı olarak seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek olay ve anlam sınırı aynıdır; ayrılık yalnız bu olayı adlandıran sözlerin görüntüsündedir.","focus_only":null,"gloss":"cinsel birleşme","neighbor_only":null,"neighbor_ref":"root_001423/B002","relation_type":"synonym","shared_zone":"Her iki dal da kadınla erkek arasındaki cinsel birleşmeyi, örtülü söyleyişe açık biçimde anlatır."}],"source_phrase_ar":"الجماع كناية عن النكاح (jamhara)؛ المجامعة المباضعة (sihah)","source_summary":"Kaynaklar iki söz biçimini aynı cinsel birleşme anlamında buluşturur; bunlardan biri özellikle örtülü anlatım olarak nitelenir.","sources":["JA","SI"],"what_is_ar":"يدخل فيه الجماع كناية عن النكاح، والمجامعة بمعنى المباضعة.","what_is_not_ar":"لا يدخل فيه جماع الناس بمعنى أخلاطهم، ولا المرأة بجمع إذا أريد موتها مع حملها."},"support_links":[]},{"boundary":"Çekirdek kadınla ilgili ölüm veya el değmemişlik durumudur; hayvanın ilk gebeliği genel tanıma katılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000259/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمَعَ","morph_features":"STEM|POS:V|PERF|LEM:jamaEa|ROOT:jmE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:2:1","qac_word_ref":"104:2:2","surface_ar":"جَمَعَ"}],"gloss":"çocuğu karnındayken ölen veya el değmemiş kalan kadın","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadın, çocuğu hâlâ karnındayken ölür."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kadın ölünceye dek ya da kocasının yanında bulunduğu sırada cinsel birleşme yaşamamıştır."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kadının karnındaki çocukla ölmesi veya cinsel birleşme yaşamamış durumda kalması anlamlarını birlikte gösterir.","boundary_detail":"Çekirdek kadınla ilgili ölüm veya el değmemişlik durumudur; hayvanın ilk gebeliği genel tanıma katılmaz.","branch_image_ar":"حال المرأة أو الأنثى التي بقي حملها أو عذرها معها","concept_gloss":"çocuğu karnındayken ölen veya el değmemiş kalan kadın","contextual_glosses":[{"applicability":"Kadının doğum gerçekleşmeden, karnındaki çocukla birlikte öldüğü anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölüm sırasında çocuğun hâlâ kadının karnında bulunması koşulunu korur."},"facet_ids":["F001"],"text":"çocuğu karnındayken ölmek","usage_role":"contextual"}],"definition":"Bir kadının çocuğu karnındayken ölmesi veya evlilikte cinsel birleşme yaşamadan el değmemiş durumda kalmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadın, çocuğu hâlâ karnındayken ölür."},{"facet_id":"F002","role":"source_variant","statement":"Kadın ölünceye dek ya da kocasının yanında bulunduğu sırada cinsel birleşme yaşamamıştır."}],"identity_rationale":"Kaynak ifadesi kadının çocuğu karnındayken ölmesini ve el değmemiş durumda kalmasını birlikte destekler; ilk gebeliğindeki dişi eşek yalnız ayrı söz biriminde tanıklanır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"çocuğu karnındayken veya el değmemişken ölmek"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"kocasıyla cinsel birleşme yaşamamış kadın"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"ilk kez gebe kalan dişi eşek"}],"lexicalization_note":"Kadının gebeyken ölmesi ile birleşme yaşamamış olması ayrılır; dişi eşeğin ilk gebeliği yalnız kendi biriminde tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gebelik alanıyla özel ölüm veya el değmemişlik koşulunun ayrımı yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal ölüm ya da el değmemişlik gibi özel bir durumu gerektirir; komşu dal gebeliği ve ana karnındaki çocuğu genel olarak anlatır.","focus_only":"Gebelik sürerken ölme veya el değmemiş durumda kalma koşulunu anlatır.","gloss":"gebelik ve karındaki çocuk","neighbor_only":"Kadın ya da dişinin gebeliğini ve karnındaki çocuğun bulunduğu yeri genel olarak adlandırır.","neighbor_ref":"root_000291/B006","relation_type":"same_field","shared_zone":"İki dal da gebelik sırasında çocuğun ana karnında bulunması alanına girer."}],"source_phrase_ar":"ماتت بجمع أي في بطنها ولد (maqayis)؛ ماتت المرأة بجمع أي مع ما في بطنها وكذلك إذا ماتت عذراء (ayn)؛ ماتت المرأة بجمع إذا ماتت وولدها في بطنها (jamhara)؛ أمر بني فلان بجمع أي لم يقتضها وماتت فلانة بجمع أي ماتت وولدها في بطنها (sihah)","source_summary":"Kaynakların çoğu kadının karnındaki çocukla birlikte ölmesini verir; anlatım ayrıca el değmemiş olarak ölme veya evlilikte henüz birleşme yaşamamış olma durumuna uzanır.","sources":["MQ","AY","JA","SI"],"what_is_ar":"يدخل فيه ماتت المرأة بجمع أي وولدها في بطنها، أو عذراء لم تمسس، وفلانة عند زوجها بجمع إذا لم يصل إليها، وأتان جامع إذا حملت أول ما تحمل.","what_is_not_ar":"لا يدخل فيه الجماع بمعنى المباضعة نفسها."},"support_links":[]},{"boundary":"Dal genel olarak her türlü bağ veya tutukluluk değil, elleri boyna bağlayan belirli kelepçe türüdür.","branch_kind":"bare","branch_ref":"root_000259/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمَعَ","morph_features":"STEM|POS:V|PERF|LEM:jamaEa|ROOT:jmE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:2:1","qac_word_ref":"104:2:2","surface_ar":"جَمَعَ"}],"gloss":"elleri boyna bağlayan kelepçe","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bağ, iki eli boyunla bir araya getirerek hareketi engeller."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ellerin boyunla birlikte bağlanıp hareketin kısıtlandığı özel bağ aracını karşılar.","boundary_detail":"Dal genel olarak her türlü bağ veya tutukluluk değil, elleri boyna bağlayan belirli kelepçe türüdür.","branch_image_ar":"القيد الذي يجمع اليدين إلى العنق","concept_gloss":"elleri boyna bağlayan kelepçe","contextual_glosses":[{"applicability":"Tarihsel bağ aracının biçiminin açıkça anlatılması gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aracın demir bağ oluşunu ve el ile boynu birleştirmesini korur."},"facet_ids":["F001"],"text":"elleri boyna bağlayan demir bağ","usage_role":"explanatory"}],"definition":"Elleri boyna doğru bağlayarak kişinin hareketini kısıtlayan kelepçe veya demir bağdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bağ, iki eli boyunla bir araya getirerek hareketi engeller."}],"identity_rationale":"Kaynak ifadesi tekil ve çoğul biçimleri, elleri boyna doğru birleştirerek hareketi kısıtlayan demir bağ olarak açıklar.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"elleri boyna bağlayan kelepçe veya demir bağ"}],"lexicalization_note":"Tanım çıplak dalın özel kelepçe anlamını korur ve aynı biçimin topluluk ya da ibadet yeri anlamlarını dışlar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; elleri boyna bağlama biçimini eksiksiz paylaşan dal eş anlamlı olarak seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek araç, bağlama biçimi ve kısıtlama sınırı bakımından anlamlı bir ayrım yoktur.","focus_only":null,"gloss":"elleri boyna bağlayan kelepçe","neighbor_only":null,"neighbor_ref":"root_000995/B020","relation_type":"synonym","shared_zone":"Her iki dal da elleri boyna doğru bağlayan kelepçe türünü anlatır."}],"source_phrase_ar":"الجوامع الأغلال (maqayis)؛ الجوامع الأغلال الواحدة جامعة (jamhara)؛ الجامعة الغل لأنها تجمع اليدين إلى العنق (sihah)","source_summary":"Kaynaklar sözü kelepçe ve demir bağ olarak açıklar; adlandırma, iki elin boyna doğru bağlanarak bir araya getirilmesine dayanır.","sources":["MQ","JA","SI"],"what_is_ar":"يدخل فيه الجامعة والجوامع بمعنى الأغلال.","what_is_not_ar":"لا يدخل فيه المسجد الجامع ولا الجماعة."},"support_links":[]},{"boundary":"Çekirdek eksiksiz bütünlüktür; büyüyüp belirli giysileri giyme kullanımı bütün dala ait kurucu bir özellik değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000259/B009","candidate_links":[{"candidate_id":"cand_8c1b705ebfff2fd9f386","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَمَعَ","morph_features":"STEM|POS:V|PERF|LEM:jamaEa|ROOT:jmE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:2:1","qac_word_ref":"104:2:2","surface_ar":"جَمَعَ"}],"gloss":"eksiksiz bütünlük","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Canlının bedeninden hiçbir parça eksilmemiştir ve varlık bütündür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi bedence derli toplu bir yapıya ulaşmış veya gelişimini tamamlamıştır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir topluluğun üyeleri eksiksiz biçimde hep birlikte bulunur."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedenin parçasız eksiksizliğini, gelişimin tamamlanmasını ve üyelerin tümünün birlikte bulunmasını kapsar.","boundary_detail":"Çekirdek eksiksiz bütünlüktür; büyüyüp belirli giysileri giyme kullanımı bütün dala ait kurucu bir özellik değildir.","branch_image_ar":"اكتمال الشيء كله بلا تفرق أو نقص","concept_gloss":"eksiksiz bütünlük","contextual_glosses":[{"applicability":"Bir topluluğun bütün üyelerinin birlikte bulunduğunu pekiştiren cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluğun hiçbir üyesinin dışarıda kalmaması anlamını korur."},"facet_ids":["F003"],"text":"bütünüyle, eksiksiz olarak","usage_role":"contextual"}],"definition":"Bir varlığın hiçbir parçası eksilmeden bütün olması, kişinin yapıca gelişimini tamamlaması veya bir topluluğun tüm üyeleriyle birlikte bulunmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Canlının bedeninden hiçbir parça eksilmemiştir ve varlık bütündür."},{"facet_id":"F002","role":"specialization","statement":"Kişi bedence derli toplu bir yapıya ulaşmış veya gelişimini tamamlamıştır."},{"facet_id":"F003","role":"extension","statement":"Bir topluluğun üyeleri eksiksiz biçimde hep birlikte bulunur."}],"identity_rationale":"Kaynak ifadesi bedenin eksiksizliğini, kişinin gelişmiş yapısını ve herkesin birlikte bulunmasını destekler; genç kızın giysi çağı yalnız ayrı söz birimindedir.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bedeni eksiksiz hayvan veya varlık"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"bedence derli toplu veya gelişimini tamamlamış adam"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"büyüyüp bütün dış giysileri giyecek çağa gelmek"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"bütünlük bildiren pekiştirme sözleri"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"dağılmamış bütün veya hepsi"}],"lexicalization_note":"Bütünlük çekirdeği korunur; beden, pekiştirme ve giysi çağıyla ilgili özel gerçekleşmeler ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; durum olarak bütünlük ile süreç ve yükümlülük olarak tamamlama arasındaki ayrım seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal varlığın veya topluluğun bütün durumuna odaklanır; komşu dal süreç tamamlamaya ve yükümlülüğü eksiksiz yerine getirmeye uzanır.","focus_only":"Bedenin eksiksiz yapısını ve topluluğun tüm üyeleriyle bulunmasını da anlatır.","gloss":"tamamlama ve eksiksiz yerine getirme","neighbor_only":"Söz, ölçü, hak veya anlaşma yükümlülüğünü tam yerine getirmeyi de kapsar.","neighbor_ref":"root_001669/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyde eksik kalmaması ve bütünün tamamlanması düşüncesini taşır."}],"source_phrase_ar":"الجمعاء من البهائم وغيرها التي لم يذهب من بدنها شيء (maqayis)؛ رجل جميع أي مجتمع في خلقه (ayn)؛ الرجل المجتمع الذي بلغ أشده (sihah)؛ جميع لدينا محضرون (mufradat)","source_summary":"Kaynak anlatımı eksiksiz bedeni, olgunlaşmış insan yapısını ve herkesin birlikte hazır bulunmasını aynı bütünlük düşüncesinde birleştirir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه جمعاء للبهيمة التي لم يذهب من بدنها شيء، وجميع وأجمعون وجمع في التوكيد والكلية، والرجل المجتمع أو الجميع في خلقه، والجارية جمعت الثياب.","what_is_not_ar":"لا يدخل فيه مجرد جماعة الناس إلا إذا كان المقصود الكل أو تمام الذات."},"support_links":["sup_a23c9210126b6f32d6ca"]},{"boundary":"Bu anlam yalnız belirtilen yapılarda geçerlidir; genel toplama eylemi veya salt kesin karar anlamı değildir.","branch_kind":"collocation","branch_ref":"root_000259/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمَعَ","morph_features":"STEM|POS:V|PERF|LEM:jamaEa|ROOT:jmE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:2:1","qac_word_ref":"104:2:2","surface_ar":"جَمَعَ"}],"gloss":"parçaları toplanıp tamamlanma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yalnız belirtilen yapılarda parçalar veya güçler bir araya gelerek tamamlanmış bir duruma ulaşır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Atın koşusu ve gücü toparlanarak bütün hızına erişir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sel çeşitli yerlerden gelen suların birleşmesiyle toplanır."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kişinin işleri onun yararına hazırlanıp yoluna girer."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız atın koşusu, sel ve kişinin işleriyle ilgili belirtilen yapılarda toparlanıp tam işlerliğe erişmeyi karşılar.","boundary_detail":"Bu anlam yalnız belirtilen yapılarda geçerlidir; genel toplama eylemi veya salt kesin karar anlamı değildir.","branch_image_ar":"استجماع القوة أو السير حتى تتلاحق أجزاؤه","concept_gloss":"parçaları toplanıp tamamlanma","contextual_glosses":[{"applicability":"Atın koşusunun toparlanıp tam hız ve güce eriştiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Koşunun ayrı güçlerinin birleşip tam düzeye erişmesini korur."},"facet_ids":["F002"],"text":"bütün gücünü toplayıp koşmak","usage_role":"contextual"}],"definition":"Belirtilen yapılarda ayrı güçlerin veya parçaların toplanarak tam işlerlik kazanmasıdır: koşu bütün gücüne erişir, sel birleşir ya da işler hazır hâle gelir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yalnız belirtilen yapılarda parçalar veya güçler bir araya gelerek tamamlanmış bir duruma ulaşır."},{"facet_id":"F002","role":"specialization","statement":"Atın koşusu ve gücü toparlanarak bütün hızına erişir."},{"facet_id":"F003","role":"specialization","statement":"Sel çeşitli yerlerden gelen suların birleşmesiyle toplanır."},{"facet_id":"F004","role":"specialization","statement":"Kişinin işleri onun yararına hazırlanıp yoluna girer."}],"identity_rationale":"Kaynak ifadesi atın koşusunun güçlenmesi, selin çeşitli yerlerden birleşmesi ve işlerin kişi için hazırlanmasını aynı toparlanıp tamamlanma görüntüsünde verir.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"koşusunu ve gücünü bütünüyle toplamak"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"çeşitli yerlerden birleşip büyümek"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"işlerin kişi için yoluna girip hazır duruma gelmesi"}],"lexicalization_note":"Tanım yalnız atın koşusu, sel ve kişinin işleriyle kurulan üç özel yapıya bağlıdır; çıplak kök anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel yapılardaki sonuçsal toparlanma ile genel toplama eylemi arasındaki sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal koşu, sel ve işler için sonuçsal toparlanmaya bağlıdır; komşu dal genel ve etkili bir toplama eylemidir.","focus_only":"Yalnız belirli yapılarda güçlerin veya parçaların kendiliğinden toparlanıp tamamlanmasını anlatır.","gloss":"dağınık parçaları bir araya toplama","neighbor_only":"Bir öznenin dağınık şeyleri yaklaştırıp bir araya getirdiği genel eylemdir.","neighbor_ref":"root_000259/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da ayrı parçaların bir araya gelmesi ortak görüntüdür."}],"source_phrase_ar":"استجمع الفرس جريا (maqayis)؛ استجمع للمرء أموره (ayn)؛ استجمع السيل اجتمع من كل موضع واستجمع الفرس جريا (sihah)","source_summary":"Kaynaklar aynı yapıyı üç alanda tanıklar: koşunun güç toplaması, suyun çeşitli yönlerden birleşmesi ve işlerin kişi için hazırlanması.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه استجمع الفرس جريا، واستجمع السيل، واستجمع الأمر للمرء أي تهيأ له واجتمع.","what_is_not_ar":"لا يدخل فيه العزم الإرادي المحكم إذا عبر عنه بأجمع الأمر."},"support_links":[]},{"boundary":"Dal bir avuç meyve veya ağaçların bir yerde toplanması değil, adı bilinmeyen çekirdekten yetişme hurma türüdür.","branch_kind":"bare","branch_ref":"root_000259/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمَعَ","morph_features":"STEM|POS:V|PERF|LEM:jamaEa|ROOT:jmE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:2:1","qac_word_ref":"104:2:2","surface_ar":"جَمَعَ"}],"gloss":"adı bilinmeyen çekirdekten yetişme hurma ağacı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ağaç çekirdekten yetişir ve türünün özel adı bilinmez."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çekirdekten yetiştiği için belirli çeşidi veya özel adı bilinmeyen hurma ağacını karşılar.","boundary_detail":"Dal bir avuç meyve veya ağaçların bir yerde toplanması değil, adı bilinmeyen çekirdekten yetişme hurma türüdür.","branch_image_ar":"نخل دقل اجتمع من النوى لا يعرف اسمه","concept_gloss":"adı bilinmeyen çekirdekten yetişme hurma ağacı","contextual_glosses":[{"applicability":"Ağacın yetişme biçimi ile çeşidinin bilinmemesi birlikte açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çekirdekten çıkma ve özel bir çeşit adı taşımama yönlerini korur."},"facet_ids":["F001"],"text":"çekirdekten çıkmış adsız hurma ağacı","usage_role":"explanatory"}],"definition":"Çekirdekten yetişmiş ve özel adı ya da çeşidi bilinmeyen, düşük nitelikli sayılabilen hurma ağacı türüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ağaç çekirdekten yetişir ve türünün özel adı bilinmez."}],"identity_rationale":"Kaynak ifadesi çekirdekten kendiliğinden yetişmiş, adı veya çeşidi bilinmeyen düşük nitelikli hurma ağacını doğrudan tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"adı bilinmeyen çekirdekten yetişme hurma ağacı"}],"lexicalization_note":"Tanım çıplak dalın hurma ağacı türü anlamıyla sınırlıdır ve miktar bildiren bir avuç meyve anlamını içermez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı ağaç türü alanındaki yetişme yolu ve adsızlık farkı en güçlü karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal çekirdekten yetişme ve adının bilinmemesiyle sınırlıdır; komşu dal daha genel bir ağaç ve meyve türünü anlatır.","focus_only":"Çekirdekten yetişmiş olmayı ve özel çeşit adının bilinmemesini birlikte gerektirir.","gloss":"düşük nitelikli hurma ağacı ve meyvesi","neighbor_only":"Düşük nitelikli hurma ağacı veya meyvesini, yetişme yoluna ve adsızlığa bağlamadan kapsar.","neighbor_ref":"root_001387/B005","relation_type":"near_synonym","shared_zone":"İki dal da düşük nitelikli sayılan bir hurma ağacı türünü gösterebilir."}],"source_phrase_ar":"الجمع كل لون من النخل لا يعرف اسمه لنخل خرج من النوى (maqayis)؛ الجمع أيضا الدقل لنخل يخرج من النوى ولا يعرف اسمه (sihah)","source_summary":"Kaynaklar sözü çekirdekten çıkan, adı bilinmeyen hurma ağacı çeşidi olarak açıklar ve bunu düşük nitelikli hurma sınıfıyla ilişkilendirir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه الجمع بمعنى الدقل أو كل لون من النخل خرج من النوى ولا يعرف اسمه.","what_is_not_ar":"لا يدخل فيه جمعة من تمر بمعنى قبضة، ولا مطلق جمع النخل في مكان."},"support_links":[]},{"boundary":"Dal her türlü kap veya doluluk değil, özellikle büyük bir kazanı niteleyen boyut anlamıdır.","branch_kind":"bare","branch_ref":"root_000259/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمَعَ","morph_features":"STEM|POS:V|PERF|LEM:jamaEa|ROOT:jmE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:2:1","qac_word_ref":"104:2:2","surface_ar":"جَمَعَ"}],"gloss":"büyük kazan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kazan, ayırt edici biçimde büyük bir boyuta sahiptir."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kazanın türünden veya yapıldığı maddeden çok olağandışı büyüklüğünün öne çıktığı kullanımı karşılar.","boundary_detail":"Dal her türlü kap veya doluluk değil, özellikle büyük bir kazanı niteleyen boyut anlamıdır.","branch_image_ar":"عظم الشيء كأنه جامع ممتلئ","concept_gloss":"büyük kazan","contextual_glosses":[{"applicability":"Kısa ve doğal bir nitelemeyle kazanın büyük boyutunun anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesnenin kazan oluşunu ve büyük boyutunu birlikte korur."},"facet_ids":["F001"],"text":"iri kazan","usage_role":"contextual"}],"definition":"Boyutu olağandan büyük olan bir kazandır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kazan, ayırt edici biçimde büyük bir boyuta sahiptir."}],"identity_rationale":"Kaynak ifadesi iki söz biçiminin de büyük boyutlu kazanı nitelediğini açık ve ortak biçimde bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"büyük kazan"}],"lexicalization_note":"Tanım çıplak dalda tanıklanan büyük kazan anlamını korur ve komşu kökün benzer sesli biçimlerini içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kap türünü paylaşan fakat boyut ile malzeme bakımından ayrılan aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal boyuta göre belirlenir; komşu dal ise taş malzemeye ve bunun işçiliğine göre belirlenir.","focus_only":"Kazanın büyük boyutlu olmasını belirtir, yapıldığı maddeyi sınırlamaz.","gloss":"taş kazan ve yapımcısı","neighbor_only":"Kabın taştan yapılmış olmasını ve bu kapların üreticisini de kapsar.","neighbor_ref":"root_000110/B006","relation_type":"same_field","shared_zone":"İki dal da yemek veya sıvı için kullanılan kazan türünü adlandırır."}],"source_phrase_ar":"قدر جماع وجامعة وهي العظيمة (maqayis)؛ قدر جامعة وهي العظيمة وقدر جماع أيضا للعظيمة (sihah)","source_summary":"Kaynaklar iki niteleme biçimini aynı açıklamayla verir ve her ikisini de büyük kazan anlamında birleştirir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه قدر جماع أو جامعة بمعنى القدر العظيمة.","what_is_not_ar":"لا يدخل فيه جمل أو جمال من الجذر المجاور ج م ل."},"support_links":[]},{"boundary":"Dal ikinci bir katılımcı ve ortak bir iş gerektirir; cinsel birleşme veya tek başına karar verme anlamı taşımaz.","branch_kind":"collocation","branch_ref":"root_000259/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمَعَ","morph_features":"STEM|POS:V|PERF|LEM:jamaEa|ROOT:jmE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:2:1","qac_word_ref":"104:2:2","surface_ar":"جَمَعَ"}],"gloss":"bir işte başkasıyla birleşip destek olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi başka biriyle aynı iş üzerinde birleşir ve onun yanında yer alır."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin başka biriyle belirli bir iş üzerinde aynı yönde davranıp onun yanında yer aldığı durumları karşılar.","boundary_detail":"Dal ikinci bir katılımcı ve ortak bir iş gerektirir; cinsel birleşme veya tek başına karar verme anlamı taşımaz.","branch_image_ar":"ممالأة واجتماع مع غيرك على أمر","concept_gloss":"bir işte başkasıyla birleşip destek olma","contextual_glosses":[{"applicability":"İki kişinin aynı iş için birlikte hareket edip birbirini desteklediği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ortak iş üzerinde birleşme ve birlikte davranma ilişkisini korur."},"facet_ids":["F001"],"text":"bir işte güç birliği yapmak","usage_role":"general"}],"definition":"Belirli bir işte başka biriyle birleşip aynı yönde davranma ve ona destek olmadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi başka biriyle aynı iş üzerinde birleşir ve onun yanında yer alır."}],"identity_rationale":"Kaynak ifadesi bir kişinin başka biriyle belirli bir iş üzerinde birleşmesini ve ona destek vermesini iki anlatımla doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"bir işte başkasıyla birleşip ona destek olmak"}],"lexicalization_note":"Tanım yalnız bir kişiyle belirli bir iş üzerinde birleşme yapısına bağlıdır; çıplak köke genel ortaklık anlamı verilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ortak işte birleşme çekirdeğini paylaşan fakat kapsamı daha geniş olan aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kişi ve iş ilişkisini açıkça kuran özel yapıdır; komşu dal yardım ve yandaşlığı daha geniş biçimde anlatır.","focus_only":"Belirli bir kişiyle belirli bir iş üzerinde birleşme yapısına sıkıca bağlıdır.","gloss":"yardımlaşıp aynı yanda birleşme","neighbor_only":"Yardım etme ve bir görüşün yanında yer alma anlamlarını daha genel biçimde kapsar.","neighbor_ref":"root_001441/B003","relation_type":"near_synonym","shared_zone":"İki dal da ortak bir işte aynı yönde davranma ve destek olma alanında buluşur."}],"source_phrase_ar":"جامعت الرجل على الأمر مجامعة وجماعا إذا مالأته عليه (jamhara)؛ جامعه على أمر كذا أي اجتمع معه (sihah)","source_summary":"Kaynaklar yapıyı belirli bir iş üzerinde başka biriyle birleşmek, aynı yönde davranmak ve ona destek olmak biçiminde açıklar.","sources":["JA","SI"],"what_is_ar":"يدخل فيه جامعت الرجل على الأمر إذا مالأته عليه، وجامعه على أمر إذا اجتمع معه.","what_is_not_ar":"لا يدخل فيه المجامعة بمعنى المباضعة، ولا إجماع الرأي إذا لم يذكر المشاركة مع شخص آخر."},"support_links":[]},{"boundary":"Çekirdek sayma ve sayıyla belirlemedir; hazırlama, zaman bekleme, kalıcı su ve dönemsel yineleme bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000989/B001","candidate_links":[{"candidate_id":"cand_917b63e73e3876d74363","lane":"micro"},{"candidate_id":"cand_f61c7111d334cc9cf9cf","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَدَّدَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Ead~ada|ROOT:Edd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:4:2","qac_word_ref":"104:2:4","surface_ar":"عَدَّدَ"}],"gloss":"sayma, sayı ve sayıya göre bir topluluğa katma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin birimlerini sayıp toplam miktarını belirleme işlemi."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sayma sonucundaki miktar, sayı ve sayılmış ya da sınırlandırılmış varlık."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sayıca çokluğu belirtme veya birini belirli bir topluluğun üyeleri arasında sayma."}}],"root_ar":"ع د د","root_id":"root_000989","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sayma işlemiyle onun doğrudan sonuçlarını ve sayıya dayalı topluluk üyeliğini birlikte anlatan kapsayıcı karşılıktır.","boundary_detail":"Çekirdek sayma ve sayıyla belirlemedir; hazırlama, zaman bekleme, kalıcı su ve dönemsel yineleme bu dala girmez.","branch_image_ar":"إحصاء المعدود","concept_gloss":"sayma, sayı ve sayıya göre bir topluluğa katma","contextual_glosses":[{"applicability":"Bir nesne topluluğunun kaç birimden oluştuğunun belirlenmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sayma eylemini ve miktarı belirleme sonucunu birlikte korur."},"facet_ids":["F001"],"text":"sayıp miktarını belirlemek","usage_role":"general"},{"applicability":"Eylemden çok sayma sonucunu veya sayıyla sınırlandırılmış varlığı anlatan bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sayma sonucundaki sayı ve miktar değerini korur."},"facet_ids":["F002"],"text":"sayı ve sayılan miktar","usage_role":"contextual"},{"applicability":"Bir kişinin belirli bir topluluğa dahil kabul edildiği kalıplaşmış bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir topluluğun üyeleri içinde sayılma ilişkisini korur."},"facet_ids":["F003"],"text":"arasında sayılmak","usage_role":"contextual"}],"definition":"Bir şeyi tek tek sayarak miktarını belirleme; bu işlemin sonucu olan sayı, sayılan varlıkların sayıca niteliği ve bir kimseyi ya da şeyi belirli bir topluluk içinde sayma alanıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin birimlerini sayıp toplam miktarını belirleme işlemi."},{"facet_id":"F002","role":"extension","statement":"Sayma sonucundaki miktar, sayı ve sayılmış ya da sınırlandırılmış varlık."},{"facet_id":"F003","role":"associated_use","statement":"Sayıca çokluğu belirtme veya birini belirli bir topluluğun üyeleri arasında sayma."}],"identity_rationale":"Kaynak ifadesi, bir şeyi tek tek sayıp miktarını belirleme çekirdeğini; sayı, sayılan şey, sayıca çokluk ve bir topluluk içinde sayılma kullanımlarıyla birlikte açıkça destekler. Geçici çerçeve bu kapsamı başka dallardaki hazırlama, bekleme süresi, su ve zaman anlamlarından doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi sayıp miktarını belirlemek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"sayı; sayılanın miktarı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"sayıca çokluk"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sayılmış veya sayıyla sınırlandırılmış"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"iyiler arasında sayılmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"az ya da çok sayıda topluluk"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"sayıları on bini aşmak"}],"lexicalization_note":"Tanım sayma çekirdeğini temel alır; topluluk içinde sayılma ve belli bir sayıyı aşma yalnızca kendi kalıplarıyla sınırlı tutulur.","neighbor_coverage_note":"Verilen komşu adaylarının tümü incelendi; sayma ile hesap, bütünleme ve karşılıklı sayılma arasındaki en açıklayıcı üç sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı saymanın kendisiyle sayı ve üyelik sonuçlarını birlikte taşır; komşu dal ise hesabı, hesaplaşmayı ve tahmini de içerdiği için bütünüyle birbirinin yerine geçmez.","focus_only":"Sayı, sayılan varlık, sayıca çokluk ve bir topluluğun içinde sayılma kullanımlarını da kapsar.","gloss":"sayma ve hesaplama","neighbor_only":"Hesaplaşma, tahmin ve gök cisimlerinin hesabı gibi daha geniş hesap alanlarına uzanır.","neighbor_ref":"root_000318/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da nesneleri sayma ve sayısal bir sonuç elde etme alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dalında birimleri sayma belirleyicidir; komşuda ise sayma gerekmeksizin parçaları topluca ve ayrıntısız biçimde kapsama esastır.","focus_only":"Tek tek sayma, sayısal miktar ve sayıya göre topluluğa katma işlemlerini bildirir.","gloss":"toplam ve bütün","neighbor_only":"Dağınık parçaları ayrıntılandırmadan tek bir bütün veya genel toplam halinde birleştirir.","neighbor_ref":"root_000260/B003","relation_type":"near_neighbor","shared_zone":"Sayılmış parçaların bir sonuçta toplanması iki alan arasında sınırlı bir temas kurar."},{"boundary_match":"partial","distinction":"Odak dalının çekirdeği sayısal belirlemedir; komşu dalın çekirdeği ise paydaşlar veya denkler arasında kurulan karşılıklı ilişkidir.","focus_only":"Varlıkları sayıp miktar belirlemeyi ve bir topluluk içinde saymayı kapsar.","gloss":"sayma ile karşılıklı sayılma","neighbor_only":"Karşılıklı paydaşlık, pay veya iki kişinin birbirine denk sayılması ilişkisini kapsar.","neighbor_ref":"root_000989/B006","relation_type":"near_neighbor","shared_zone":"İki dalda da bir kişi ya da şey başkalarıyla birlikte değerlendirilip sayılabilir."}],"source_phrase_ar":"عددت الشيء عدا أي أحصيته (maqayis;ayn;sihah;tahdhib)؛ العدد مقدار ما يعد (maqayis)؛ العديد الكثرة (maqayis;ayn;sihah;tahdhib)؛ فلان في عداد الصالحين (maqayis;ayn;sihah)؛ العدد آحاد مركبة (mufradat)","source_summary":"Toplu tanıklık, sayma işlemini temel alır ve bundan sayı, sayılan şey, sayıca çokluk ve bir topluluğa dahil sayılma kullanımlarını geliştirir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"الإحصاء وضم الأعداد واسم العدد والمعدود والكثرة أو القلة من جهة كون الشيء يحصى أو يعد في جماعة","what_is_not_ar":"ليس إعداد الشيء وتهيئته ولا عدة المرأة ولا الماء العد ولا العداد الزماني"},"support_links":["sup_b514cf3087189c74b36c","sup_e1c1edb9f0088e300aa6"]},{"boundary":"Bu dal gelecekteki ihtiyaç için hazırlamadır; sayısal sayma, hukuki bekleme süresi veya yalnızca mevcut bulunma anlamı değildir.","branch_kind":"bare","branch_ref":"root_000989/B002","candidate_links":[{"candidate_id":"cand_e6ef28d6527586d5e78e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَدَّدَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Ead~ada|ROOT:Edd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:4:2","qac_word_ref":"104:2:4","surface_ar":"عَدَّدَ"}],"gloss":"gelecekteki bir iş için hazırlama ve hazır bulundurma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi gelecekteki belirli bir iş veya olay için önceden hazırlamak."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İhtiyaç anı için mal, silah veya başka bir gereci ayırıp hazır tutmak."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hazırlanan şeyi gerektiğinde erişilip alınabilecek bir durumda bulundurmak."}}],"root_ar":"ع د د","root_id":"root_000989","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel hazırlama eylemini, ihtiyaç için kaynak ayırmayı ve kullanılabilir durumda tutmayı birlikte karşılar.","boundary_detail":"Bu dal gelecekteki ihtiyaç için hazırlamadır; sayısal sayma, hukuki bekleme süresi veya yalnızca mevcut bulunma anlamı değildir.","branch_image_ar":"تهيئة العدة","concept_gloss":"gelecekteki bir iş için hazırlama ve hazır bulundurma","contextual_glosses":[{"applicability":"Bir şeyin ilerideki belirli bir iş için uygun duruma getirilmesini anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gelecekteki işe yönelik ön hazırlama işlemini korur."},"facet_ids":["F001"],"text":"önceden hazırlamak","usage_role":"general"},{"applicability":"Hazırlanan şeyin ihtiyaç anında erişilebilir ve kullanılabilir tutulduğu bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hazırlanan şeyin erişilebilir ve kullanıma hazır tutulmasını korur."},"facet_ids":["F003"],"text":"gerektiğinde kullanmak üzere hazır tutmak","usage_role":"contextual"},{"applicability":"İlerideki olaylar için mal, silah veya başka araçların önceden ayrılması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İhtiyaca yönelik somut araç ve kaynak ayırma işlemini korur."},"facet_ids":["F002"],"text":"gereç ve kaynak ayırmak","usage_role":"contextual"}],"definition":"Bir şeyi ileride doğacak bir iş veya ihtiyaç için önceden hazırlamak, gerektiğinde kullanılabilecek biçimde hazır tutmak ve bu amaçla mal, silah ya da başka gereç ayırmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi gelecekteki belirli bir iş veya olay için önceden hazırlamak."},{"facet_id":"F002","role":"specialization","statement":"İhtiyaç anı için mal, silah veya başka bir gereci ayırıp hazır tutmak."},{"facet_id":"F003","role":"extension","statement":"Hazırlanan şeyi gerektiğinde erişilip alınabilecek bir durumda bulundurmak."}],"identity_rationale":"Kaynak ifadesi bir şeyi gelecekteki bir iş veya olay için hazırlamayı, hazır ve erişilebilir duruma getirmeyi, ayrıca ihtiyaç anı için mal, silah ve gereç ayırmayı ortak bir çekirdekte birleştirir. Geçici dal kimliği bu işlemi sayma ve öteki dallardan doğru biçimde ayırmaktadır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir şeyi ilerideki iş için hazırlamak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ilerideki ihtiyaç için hazırlanmış mal, silah veya gereç"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bir işe hazırlanmak ve donanmak"}],"lexicalization_note":"Tanım çıplak hazırlama anlamını verir; belirli bir kalıba özgü kapsam eklemez ve hazırlanan araçları yalnızca desteklenen örnekler olarak tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel hazırlama, amaç için ayırma, hazır bulunma ve ek güvence arasındaki en yararlı üç karşıtlık seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı genel hazırlama ve donanım alanıdır; komşu dalda hazırlanan şeyin belirli bir alıcıya, borca veya karşılığa bağlanması daha belirleyicidir.","focus_only":"Her türlü gelecek iş için hazırlama ile araç ve kaynakları hazır tutmayı genel olarak kapsar.","gloss":"hazırlama ve belirli amaç için ayırma","neighbor_only":"Bir şeyi belirli bir kişi, borç veya karşılık için özellikle ayırıp gözetme anlamını taşır.","neighbor_ref":"root_000566/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi ilerideki kullanım için önceden hazır hale getirmeyi içerir."},{"boundary_match":"partial","distinction":"Odak dalında amaçlı hazırlama işlemi merkezdeyken komşuda hazır bulunma durumu ve el altındaki donanım daha geniş bir yer tutar.","focus_only":"Hazırlama eylemini ve gelecekteki olay için kaynak ayırmayı öne çıkarır.","gloss":"hazırlamak ve hazır bulunmak","neighbor_only":"Hazır, yakın ve elde bulunan durum ile sürekli el altında tutulan donanımı da adlandırır.","neighbor_ref":"root_000978/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin ihtiyaç anında kullanılmaya hazır olmasını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalı nötr hazırlamayı anlatır; komşu dal ise belirsizlik veya tehlikeye karşı fazladan güvence sağlama amacını gerektirir.","focus_only":"Beklenen iş için gerekli şeyi hazırlayıp kullanıma hazır hale getirir.","gloss":"hazırlık ve güvence önlemi","neighbor_only":"Güvenceyi artırmak için gereğinden fazla önlem veya yedek edinmeyi içerir.","neighbor_ref":"root_000970/B021","relation_type":"near_neighbor","shared_zone":"Gelecekteki bir gereksinime karşı önceden araç edinme iki dalın ortak alanıdır."}],"source_phrase_ar":"أعددت الشيء إعدادا (maqayis)؛ أعددت الشيء هيأته (ayn)؛ العدة من السلاح ما اعتددته (jamhara)؛ أعده لأمر كذا هيأه له (sihah)؛ العدة ما أعد لأمر يحدث مثل الأهبة (tahdhib)؛ أعددت هذا لك أي جعلته بحيث تعده وتتناوله (mufradat)","source_summary":"Toplu tanıklık, önceden hazırlama ve hazır tutma çekirdeğinde birleşir; ayrılan mal, silah ve gereçler yaklaşan ihtiyaçlara yönelik somut uygulamalardır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"تهيئة الشيء لأمر حادث واتخاذ العدة والأهبة والذخيرة والسلاح والمال لما يحتاج إليه","what_is_not_ar":"ليست الإحصاء نفسه ولا عدة المرأة ولا الماء العد"},"support_links":["sup_953f1ed2d7f138323bde"]},{"boundary":"Ortak sınır sayıyla belirlenmiş zaman dilimidir; bekleme, sonradan yerine getirme ve belirli günler birbirinden ayrı bağlamsal gerçekleşmelerdir.","branch_kind":"mixed_non_bare","branch_ref":"root_000989/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَدَّدَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Ead~ada|ROOT:Edd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:4:2","qac_word_ref":"104:2:4","surface_ar":"عَدَّدَ"}],"gloss":"sayılı zaman dilimi ve bağlama bağlı bekleme ya da tamamlama süresi","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gün, ay, dönemsel çevrim veya olay sonuyla ölçülüp sınırlandırılmış zaman dilimi."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kadının belirli çevrimler, aylar veya gebeliğin sona ermesiyle ölçülen bekleme süresi."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kaçırılmış günlerin sayısına eşit sayıda günü daha sonra yerine getirme yükümlülüğü."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Belirli ve az sayıdaki günlerin adlandırılması."}}],"root_ar":"ع د د","root_id":"root_000989","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sayılı süre çekirdeğini ve bu sürenin farklı bağlamlarda bekleme veya eksik günleri tamamlama işlevini birlikte açıklar.","boundary_detail":"Ortak sınır sayıyla belirlenmiş zaman dilimidir; bekleme, sonradan yerine getirme ve belirli günler birbirinden ayrı bağlamsal gerçekleşmelerdir.","branch_image_ar":"مدة العدة المعدودة","concept_gloss":"sayılı zaman dilimi ve bağlama bağlı bekleme ya da tamamlama süresi","contextual_glosses":[{"applicability":"Kadın için çevrim, ay veya doğumla ölçülen hukuki bekleme bağlamına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölçülmüş süreyi ve yeniden evlenmeden önce bekleme koşulunu korur."},"facet_ids":["F001","F002"],"text":"yeniden evlenmeden önceki bekleme süresi","usage_role":"contextual"},{"applicability":"Yerine getirilemeyen günlerin aynı sayıda başka günle tamamlanması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kaçırılan ve sonradan tamamlanan günler arasındaki sayı eşitliğini korur."},"facet_ids":["F001","F003"],"text":"kaçırılan günler kadar sonradan tamamlama","usage_role":"contextual"},{"applicability":"Özel olarak belirlenmiş, sınırlı sayıdaki günlerden söz edilen bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Günlerin belirli ve sayıca sınırlı oluşunu korur."},"facet_ids":["F001","F004"],"text":"sayılı ve belirli günler","usage_role":"contextual"}],"definition":"Sayısı veya bitiş ölçütü belirlenmiş bir zaman dilimidir. Bağlama göre bu dilim kadın için bekleme süresi, kaçırılan günler kadar sonradan yerine getirme süresi ya da özellikle belirlenmiş sınırlı günler olabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gün, ay, dönemsel çevrim veya olay sonuyla ölçülüp sınırlandırılmış zaman dilimi."},{"facet_id":"F002","role":"specialization","statement":"Bir kadının belirli çevrimler, aylar veya gebeliğin sona ermesiyle ölçülen bekleme süresi."},{"facet_id":"F003","role":"specialization","statement":"Kaçırılmış günlerin sayısına eşit sayıda günü daha sonra yerine getirme yükümlülüğü."},{"facet_id":"F004","role":"example","statement":"Belirli ve az sayıdaki günlerin adlandırılması."}],"identity_rationale":"Kaynak ifadesi yalnızca zorunlu bir bekleme süresini değil, kadın için ölçülen bekleme dönemini, kaçırılan günler kadar sonradan yerine getirme süresini ve belirli sayıda günleri birlikte içerir. Dal korunabilir, ancak bütün örnekleri tek bir bekleme yükümlülüğü gibi sunmak yerine sayıyla sınırlandırılmış zaman dilimleri ve bağlama göre üstlendikleri görevler üzerinden tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kadının yeniden evlenmeden önce beklemesi gereken süre"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kaçırılan günler kadar başka günlerde yerine getirmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"sayılı ve belirli günler"}],"lexicalization_note":"Tanım, sayılı süre çekirdeğini korurken kadınla ilgili bekleme, kaçırılan günleri tamamlama ve belirli günler kalıplarını ayrı tutar.","neighbor_coverage_note":"Bütün adaylar incelendi; ölçülmüş bekleme süresini dönemsel çevrimden, genel saymadan ve sıradan ertelemeden ayıran üç ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı ölçülen toplam süre ve yükümlülükle ilgilidir; komşu dal ise bu sürenin ölçütü olabilen bedensel çevrimin evrelerini adlandırır.","focus_only":"Kadının toplam bekleme süresini, eksik günlerin tamamlanmasını ve başka sayılı günleri kapsar.","gloss":"bekleme süresi ve dönemsel çevrim","neighbor_only":"Kadın bedenindeki kanama ve temizlik evrelerinin kendisini, geçişlerini ve aralarındaki çevrimi adlandırır.","neighbor_ref":"root_001210/B003","relation_type":"near_neighbor","shared_zone":"Kadının bekleme süresi dönemsel bedensel çevrimlerle ölçülebildiği için alanlar kesişir."},{"boundary_match":"partial","distinction":"Odak dalında sayma zaman dilimini ve bağlamsal görevi sınırlar; komşu dalda ise nesnesi zaman olmak zorunda olmayan genel sayma çekirdektir.","focus_only":"Sayının belirlediği zaman dilimini ve bu dilime bağlı bekleme veya tamamlama görevini kapsar.","gloss":"sayılı süre ve genel sayma","neighbor_only":"Her tür varlığı sayma, sayıyı adlandırma ve bir topluluk içinde sayma işlemlerini kapsar.","neighbor_ref":"root_000989/B001","relation_type":"near_neighbor","shared_zone":"Bir sürenin kaç gün veya dönemden oluştuğunu belirleme, genel sayma işlemine dayanır."},{"boundary_match":"partial","distinction":"Odak dalında sayıyla veya bitiş ölçütüyle sınırlandırılmış süre esastır; komşu dalda belirleyici olan yalnızca sonraya bırakmadır.","focus_only":"Ölçüsü belirli bir bekleme veya sonradan tamamlama süresini gerektirir.","gloss":"ölçülü bekleme ve erteleme","neighbor_only":"Bir işi ya da ödemeyi daha sonraki bir zamana bırakma eylemini genel olarak bildirir.","neighbor_ref":"root_000019/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir işlemin daha sonraki bir zamanda gerçekleşmesini içerebilir."}],"source_phrase_ar":"عدة المرأة أيام قروئها (ayn)؛ عدة المرأة معروفة (jamhara)؛ عدة المرأة أيام أقرائها (sihah)؛ العدة عدة المرأة شهورا كانت أو أقراء أو وضع حمل (tahdhib)؛ فعدة من أيام أخر أي عليه أيام بعدد ما فاته (mufradat)؛ الأيام المعدودات أيام التشريق (sihah;tahdhib;mufradat)","source_summary":"Toplu tanıklık, sayıyla veya belirli bir bitiş ölçütüyle sınırlandırılmış zaman dilimlerini; bekleme, eksik günleri tamamlama ve belirli günleri adlandırma bağlamlarında gösterir.","sources":["AY","JA","SI","TA","MU"],"what_is_ar":"المدة المعدودة الواجبة انتظارا أو قضاء كعدة المرأة وعدة الأيام الفائتة والأيام المعدودات","what_is_not_ar":"ليست الأهبة والسلاح ولا مجرد كثرة العدد"},"support_links":[]},{"boundary":"Dalın ayırıcı niteliği suyun kalıcı veya sürekli beslenen oluşudur; geçici yağmur suyu ve kısa ömürlü birikintiler kapsam dışındadır.","branch_kind":"mixed_non_bare","branch_ref":"root_000989/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَدَّدَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Ead~ada|ROOT:Edd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:4:2","qac_word_ref":"104:2:4","surface_ar":"عَدَّدَ"}],"gloss":"kaynağı kesilmeyen kalıcı su ve su yeri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Doğal olarak bir yerde toplanmış su veya bu suyun bulunduğu yer."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eskiden beri var olan ve su çekildikçe tükenmeyen kalıcı su."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Besleyici kaynağı kesilmediği için akışı veya varlığı sürekli kalan su."}}],"root_ar":"ع د د","root_id":"root_000989","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem sürekli suyu hem de onun doğal olarak toplandığı veya çıkarıldığı kalıcı yeri karşılar.","boundary_detail":"Dalın ayırıcı niteliği suyun kalıcı veya sürekli beslenen oluşudur; geçici yağmur suyu ve kısa ömürlü birikintiler kapsam dışındadır.","branch_image_ar":"الماء العد","concept_gloss":"kaynağı kesilmeyen kalıcı su ve su yeri","contextual_glosses":[{"applicability":"Çekilmesine rağmen besleyici kaynağı sürdüğü için tükenmeyen suyu anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Suyun sürekliliğini ve çekmekle tükenmemesini korur."},"facet_ids":["F002","F003"],"text":"tükenmeyen sürekli su","usage_role":"general"},{"applicability":"Suyun kendisinden çok onu sürekli sağlayan yer veya kaynak kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Suyun bulunduğu yeri ve kaynağın sürekliliğini korur."},"facet_ids":["F001","F003"],"text":"kalıcı su kaynağı","usage_role":"contextual"}],"definition":"Doğal olarak birikmiş, eski veya besleyici kaynağı kesilmediği için çekmekle tükenmeyen sürekli su ve bu suyun bulunduğu kalıcı su yeridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Doğal olarak bir yerde toplanmış su veya bu suyun bulunduğu yer."},{"facet_id":"F002","role":"specialization","statement":"Eskiden beri var olan ve su çekildikçe tükenmeyen kalıcı su."},{"facet_id":"F003","role":"source_variant","statement":"Besleyici kaynağı kesilmediği için akışı veya varlığı sürekli kalan su."}],"identity_rationale":"Kaynak ifadesi doğal su birikimini ve özellikle eski, besleyici kaynağı kesilmeyen, çekmekle tükenmeyen sürekli suyu aynı dalda açıkça tanımlar. Geçici çerçeve hem suyu hem de onun bulunduğu kalıcı su yerini kapsayarak tanıklığa uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"eskiden beri var olan, tükenmeyen sürekli su"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"sürekli sular veya kalıcı su yerleri"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"köklü ve eski saygınlık"}],"lexicalization_note":"Tanım kalıcı su çekirdeğini verir; su yerleri ve eski, köklü olma benzetmesi yalnızca tanıklanan biçim ve kalıpların sınırında tutulur.","neighbor_coverage_note":"Bütün adaylar gözden geçirildi; kalıcı suyu yapılmış havuz suyundan, doğal göletten ve geçici su çukurundan ayıran üç sınır seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında kalıcılık suyun kesilmeyen beslenmesine bağlıdır; komşuda ise suyun bir yapı içinde tutulması esastır ve yenilenmesi gerekmez.","focus_only":"Doğal, eski veya sürekli beslenen ve çekmekle tükenmeyen suyu gerektirir.","gloss":"sürekli kaynak suyu ve havuz suyu","neighbor_only":"Suyun yapılmış bir havuz, sarnıç veya düzeltilmiş su kabında sabit durmasını kapsar.","neighbor_ref":"root_000109/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da belirli bir yerde duran veya toplanan suyu anlatır."},{"boundary_match":"partial","distinction":"Odak dalını belirleyen kesintisiz kaynak ve tükenmezliktir; komşu dalı belirleyen ise birikintinin biçimi ve bol su içermesidir.","focus_only":"Suyun eskiliğini, sürekliliğini ve çekmekle tükenmemesini öne çıkarır.","gloss":"kalıcı su ve gölet","neighbor_only":"Vadi içindeki bol su birikintisini, göleti veya bataklık benzeri su alanını adlandırır.","neighbor_ref":"root_001292/B003","relation_type":"near_neighbor","shared_zone":"Doğal bir çukurda veya arazide toplanan su iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dalı süreklilik ve tükenmezlik gerektirir; komşu dal geçici olarak su tutan yerle sınırlıdır.","focus_only":"Sürekli beslenen veya eskiden beri tükenmeyen suyu ve yerini bildirir.","gloss":"tükenmeyen su ve geçici su çukuru","neighbor_only":"Suyu yalnızca birkaç gün tutabilen çukur, havuz veya gölet benzeri yeri bildirir.","neighbor_ref":"root_000018/B006","relation_type":"near_neighbor","shared_zone":"İki dalda da suyun bir yerde toplanması ve tutulması söz konusudur."}],"source_phrase_ar":"العد مجتمع الماء وجمعه أعداد (maqayis;ayn)؛ العد من الماء القديم الذي لا ينتزح (jamhara)؛ العد بالكسر الماء الذي له مادة لا تنقطع (sihah)؛ الماء العد الدائم الذي لا انقطاع له (tahdhib)؛ ماء عد (mufradat)","source_summary":"Toplu tanıklık, birikmiş su anlamını eski, tükenmeyen ve sürekli beslenen su özellikleriyle açıklar; süreklilik dalın geçici su birikintilerinden ayrılan temel sınırıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"الماء العد ومجتمع الماء والركية القديمة أو الدائمة التي لا ينقطع ماؤها","what_is_not_ar":"ليس ماء السماء ولا ماء الغدران المنقطع ولا العداد الزماني"},"support_links":[]},{"boundary":"Çekirdek belirli zaman ve düzenli geri geliştir; yay ve özel gün kullanımları yalnızca kendi kalıplarında ilişkili anlamlar olarak tutulmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000989/B005","candidate_links":[{"candidate_id":"cand_8c1b705ebfff2fd9f386","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَدَّدَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Ead~ada|ROOT:Edd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:4:2","qac_word_ref":"104:2:4","surface_ar":"عَدَّدَ"}],"gloss":"belirli zaman ve bilinen aralıklarla geri gelme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin belirlenmiş zamanı, dönemi veya en güçlü evresi."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir olayın bilinen veya sayılı zaman aralıklarında yeniden ortaya çıkması."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Zehirlenme veya sokulma ağrısının belirli aralıklarla yeniden alevlenmesi."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yayın aralıklı titreşimini veya bu titreşimden çıkan sesi adlandırma."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Dağıtım, yoklama veya geçici toplanma için belirlenmiş günü adlandırma."}}],"root_ar":"ع د د","root_id":"root_000989","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın zaman ve yineleme çekirdeğini verir; kalıba bağlı yay ve özel gün kullanımlarını genel anlama katmaz.","boundary_detail":"Çekirdek belirli zaman ve düzenli geri geliştir; yay ve özel gün kullanımları yalnızca kendi kalıplarında ilişkili anlamlar olarak tutulmalıdır.","branch_image_ar":"عداد الوقت ومعاودته","concept_gloss":"belirli zaman ve bilinen aralıklarla geri gelme","contextual_glosses":[{"applicability":"Bir olayın veya ağrının bilinen zaman aralıklarında tekrar belirdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Zaman aralıklarını ve olayın yeniden ortaya çıkmasını korur."},"facet_ids":["F002","F003"],"text":"belirli aralıklarla yeniden ortaya çıkmak","usage_role":"general"},{"applicability":"Bir kişinin, yönetimin veya başka bir şeyin belirli zamanı ya da en güçlü evresi kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli dönemi ve o dönemin en güçlü evresini korur."},"facet_ids":["F001"],"text":"dönem veya en parlak çağ","usage_role":"contextual"},{"applicability":"Yayın belli aralıklarla titreştirilmesi ya da çıkardığı ses için kullanılan kalıba özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaya özgü tekrarlı titreşim ile ses seçeneklerini korur."},"facet_ids":["F004"],"text":"yayın aralıklı titreşimi veya sesi","usage_role":"contextual"},{"applicability":"Dağıtım, yoklama ya da geçici toplantı için ayrılmış günü anlatan kalıba özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirlenmiş gün ile dağıtım veya toplanma işlevini korur."},"facet_ids":["F005"],"text":"dağıtım veya toplanma günü","usage_role":"contextual"}],"definition":"Bir şeyin belirli zamanı veya dönemi ile belli aralıklarda yeniden ortaya çıkmasıdır. Zehir ağrısının alevlenmesi bunun özel gerçekleşmesiyken yayın sesi ve titreşimi ile dağıtım ya da toplanma günü kalıba bağlı ilişkili kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin belirlenmiş zamanı, dönemi veya en güçlü evresi."},{"facet_id":"F002","role":"core","statement":"Bir olayın bilinen veya sayılı zaman aralıklarında yeniden ortaya çıkması."},{"facet_id":"F003","role":"specialization","statement":"Zehirlenme veya sokulma ağrısının belirli aralıklarla yeniden alevlenmesi."},{"facet_id":"F004","role":"associated_use","statement":"Yayın aralıklı titreşimini veya bu titreşimden çıkan sesi adlandırma."},{"facet_id":"F005","role":"associated_use","statement":"Dağıtım, yoklama veya geçici toplanma için belirlenmiş günü adlandırma."}],"identity_rationale":"Kaynak ifadesi belirli zaman veya dönem ile bilinen aralıklarda geri gelme anlamlarını destekler; zehir ağrısının yeniden alevlenmesi bu çekirdeğin belirgin gerçekleşmesidir. Bununla birlikte yayın sesi veya aralıklı titreşimi ve dağıtım ya da toplanma günü, genel zaman çekirdeğiyle eşitlenmemesi gereken kalıba bağlı ilişkili kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"sokulma ağrısının belirli aralıklarla alevlenmesi"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bana belirli zamanlarda yeniden baş göstermek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"zaman, dönem veya en parlak çağ"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"yayın tekrarlanan titreşimi veya sesi"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"ayda bir gerçekleşen buluşma"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"dağıtım, yoklama veya geçici toplanma günü"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"belirli aralıklarla gelen akıl bulanıklığı"}],"lexicalization_note":"Tanım zaman ve aralıklı geri geliş çekirdeğini ayırır; yay sesi, aylık buluşma ve özel gün anlamlarını kendi kalıplarının dışına genellemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel aralıklı geri gelişi kısa buluşma aralığından, özel dördüncü dönüşten ve yalnızca uygun zamandan ayıran ilişkiler seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı belirli zamanı ve yeniden ortaya çıkmayı genel olarak kapsar; komşu dal iki buluşmayı ayıran kısa süreye özgüdür.","focus_only":"Belirli dönemi, yinelenen ağrıyı ve kalıba bağlı yay veya özel gün kullanımlarını da kapsar.","gloss":"yinelenme zamanı ve buluşmalar arası süre","neighbor_only":"Özellikle iki buluşma arasında kalan kısa ve tekrarlanan zaman aralığını bildirir.","neighbor_ref":"root_001145/B007","relation_type":"near_synonym","shared_zone":"İki dal da olayların belli aralıklarla gerçekleşmesi ve aradaki zamanın sınırlı olması alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dalında aralık bağlama göre değişebilir; komşu dalda ise dördüncü zamana bağlı özel dönüş düzeni belirleyicidir.","focus_only":"Yinelemenin aralığını genel bırakabilir ve dönem, yay sesi veya özel gün kullanımlarına uzanabilir.","gloss":"aralıklı geri geliş ve dördüncü zaman dönüşü","neighbor_only":"Hayvanların sulanması veya ateşli hastalık için her dördüncü zamandaki belirli dönüş düzenini gerektirir.","neighbor_ref":"root_000536/B004","relation_type":"near_neighbor","shared_zone":"Hastalık belirtisinin veya başka bir olayın düzenli zaman aralıklarında geri gelmesi ortak alandır."},{"boundary_match":"partial","distinction":"Odak dalında yineleme önemli bir çekirdektir; komşu dalda olayın zamanı vardır fakat düzenli geri geliş koşulu yoktur.","focus_only":"Belirli aralıklarla yeniden ortaya çıkma ve buna bağlı özel kalıpları kapsar.","gloss":"yinelenen zaman ve uygun an","neighbor_only":"Bir şeyin yalnızca uygun zamanı veya gerçekleşme anını bildirir.","neighbor_ref":"root_000039/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir olayın belirli zamanı veya dönemini gösterebilir."}],"source_phrase_ar":"العداد اهتياج وجع اللديغ (maqayis;ayn;sihah)؛ العداد الشيء الذي يأتيك لوقت (tahdhib)؛ عدان الشيء عهده وزمانه (mufradat)؛ كان ذلك في عدان شبابه (ayn;sihah;tahdhib)؛ عداد القوس أن تنبض بها ساعة بعد ساعة (maqayis)؛ عداد القوس صوتها (sihah;tahdhib)؛ يوم العداد يوم العطاء (maqayis;tahdhib)","source_summary":"Toplu tanıklık, belirli zaman ve belli aralıklarla geri gelme çekirdeğini; ağrının yeniden alevlenmesi, dönemin en güçlü evresi, yayın tekrarlı hareketi veya sesi ve özel bir gün gibi kullanımlarla gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الوقت المعدود المحدد ومعاودة الشيء في أوقات معلومة وما يلحق به من العداد والعدان","what_is_not_ar":"ليس العدد الحسابي وحده ولا العدة الشرعية ولا الماء العد"},"support_links":["sup_a23c9210126b6f32d6ca"]},{"boundary":"Dal sayısal miktardan çok kişiler arasındaki karşılıklı paydaşlık, pay veya denklik ilişkisini bildirir.","branch_kind":"mixed_non_bare","branch_ref":"root_000989/B006","candidate_links":[{"candidate_id":"cand_22cd05023d5dcbb1f72e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَدَّدَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Ead~ada|ROOT:Edd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:4:2","qac_word_ref":"104:2:4","surface_ar":"عَدَّدَ"}],"gloss":"karşılıklı paydaşlık, pay ve denk sayılma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişilerin sayılabilir bir mal, değer veya üstünlükte karşılıklı paydaş olması."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ortaklıktan doğan payları veya özellikle mirasta karşılıklı paydaşları adlandırma."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişiyi başka bir kişinin karşılığı, eşi veya dengi sayma."}}],"root_ar":"ع د د","root_id":"root_000989","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Paylaşılan değer üzerindeki ortaklığı, ortaya çıkan payı ve kişiler arasında kurulan denkliği birlikte karşılar.","boundary_detail":"Dal sayısal miktardan çok kişiler arasındaki karşılıklı paydaşlık, pay veya denklik ilişkisini bildirir.","branch_image_ar":"نظير يعد مع غيره","concept_gloss":"karşılıklı paydaşlık, pay ve denk sayılma","contextual_glosses":[{"applicability":"Kişilerin mal, değer veya üstünlük bakımından birbirine karşı pay sahibi olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Katılımcılar arasındaki karşılıklı ortaklık ve pay ilişkisini korur."},"facet_ids":["F001"],"text":"karşılıklı paydaş olmak","usage_role":"general"},{"applicability":"Ortaklıktaki bölüşüm payları ya da özellikle mirasta birbirine karşı pay sahibi kişiler kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bölüşülen payı ve pay sahipleri arasındaki karşılıklılığı korur."},"facet_ids":["F002"],"text":"paylar veya karşılıklı paydaşlar","usage_role":"contextual"},{"applicability":"Bir kişinin başka biriyle eş düzeyde veya ona karşılık sayıldığı kalıba özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki kişi arasında kurulan denklik ve karşılıklılık ilişkisini korur."},"facet_ids":["F003"],"text":"onun dengi ve karşılığı","usage_role":"contextual"}],"definition":"Birden çok kişinin sayılabilir bir mal, değer veya üstünlük bakımından karşılıklı paydaş olması; bundan doğan payların ya da birbirine karşılık ve denk sayılan kişilerin adlandırılmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişilerin sayılabilir bir mal, değer veya üstünlükte karşılıklı paydaş olması."},{"facet_id":"F002","role":"extension","statement":"Ortaklıktan doğan payları veya özellikle mirasta karşılıklı paydaşları adlandırma."},{"facet_id":"F003","role":"extension","statement":"Bir kişiyi başka bir kişinin karşılığı, eşi veya dengi sayma."}],"identity_rationale":"Kaynak ifadesi karşılıklı olarak sayılabilen mal veya değerlerde ortaklığı, bundan doğan payları ve bir kişinin başka biriyle denk ya da karşılık sayılmasını birlikte verir. Geçici çerçeve, sayma fikrinin bu dalda yalın miktar belirleme değil katılımcılar arasındaki pay ve karşılıklılık ilişkisini kurduğunu doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"mal veya değer bakımından karşılıklı paydaş olmak"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"paylar, denkler veya mirastaki karşılıklı paydaşlar"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"onun dengi ve karşılığı"}],"lexicalization_note":"Tanım paydaşlık, pay ve denk sayılma yüzlerini ayırır; belirli kişi karşılaştırmasını veya miras bağlamını çıplak bir genel sayma anlamına dönüştürmez.","neighbor_coverage_note":"Tüm komşu adayları değerlendirildi; genel paydaşlık ve denkliği salt benzerlikten, genel saymadan ve güç bakımından denk rakipten ayıran üç ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında denklik, daha geniş karşılıklı pay ve katılım alanının bir yüzüdür; komşu dalın çekirdeği doğrudan benzerlik ve eşdeğerliktir.","focus_only":"Paylaşılan mal veya değerde ortaklığı, payları ve mirastaki karşılıklı paydaşları da kapsar.","gloss":"paydaş ve denk","neighbor_only":"İki şeyi benzerlik bakımından birbirinin tam eşi veya örneği olarak karşı karşıya koyar.","neighbor_ref":"root_001520/B006","relation_type":"near_neighbor","shared_zone":"Bir kişinin başka bir kişinin dengi veya karşılığı sayılması iki dalda örtüşür."},{"boundary_match":"partial","distinction":"Odak dalında sayma katılımcılar arasındaki karşılıklı ilişkiyi düzenler; komşu dalda saymanın kendisi ve sayısal sonuç merkezde bulunur.","focus_only":"Sayılabilir bir değer üzerinde karşılıklı pay, paydaşlık veya denklik ilişkisi kurar.","gloss":"karşılıklı pay ve genel sayma","neighbor_only":"Varlıkları tek tek sayıp miktarını belirler ve bir topluluğa dahil sayar.","neighbor_ref":"root_000989/B001","relation_type":"near_neighbor","shared_zone":"Kişilerin başkalarıyla birlikte değerlendirilip sayılması iki dal arasında bağlantı kurar."},{"boundary_match":"partial","distinction":"Odak dalındaki denklik farklı ilişki ve paylaşım bağlamlarına açıktır; komşu dal dengeyi özellikle yaş ve mücadele gücü ekseninde kurar.","focus_only":"Pay, ortaklık ve genel biçimde bir başkasına denk sayılmayı kapsar.","gloss":"genel denk ve güç bakımından denk","neighbor_only":"Özellikle yaş, yiğitlik, güç veya dayanıklılık bakımından birbirine denk rakibi bildirir.","neighbor_ref":"root_001221/B003","relation_type":"near_neighbor","shared_zone":"Bir kişinin başka bir kişiye denk veya eş sayılması ortak alandır."}],"source_phrase_ar":"هم يتعادون إذا اشتركوا فيما يعدد به بعضهم على بعض (ayn;tahdhib)؛ العدائد النظراء (tahdhib)؛ العدائد الحصص (tahdhib)؛ من يعاده في الميراث (sihah)؛ فلان عد فلان أي قرنه (tahdhib)","source_summary":"Toplu tanıklık, karşılıklı paydaş olmayı; pay, mirastaki paydaş ve iki kişi arasında kurulan denklik ya da karşılıklılık kullanımlarıyla aynı ilişki alanında birleştirir.","sources":["AY","SI","TA"],"what_is_ar":"المشاركة والمقارنة والحصة أو النظير حين يعد الشيء مع غيره أو يقابل به","what_is_not_ar":"ليس مجرد كثرة العدد ولا الاستعداد ولا العداد الزماني"},"support_links":["sup_f2abf7bb10381f8f7a58"]},{"boundary":"Dal yalnızca para ya da birikmiş değer değildir; varlığın kendisini, edinilmesini, artmasını, varlıklı duruma geçişi ve başkasına varlık kazandırmayı ayırarak kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001457/B001","candidate_links":[{"candidate_id":"cand_917b63e73e3876d74363","lane":"micro"},{"candidate_id":"cand_e6ef28d6527586d5e78e","lane":"micro"},{"candidate_id":"cand_8c1b705ebfff2fd9f386","lane":"micro"},{"candidate_id":"cand_22cd05023d5dcbb1f72e","lane":"micro"},{"candidate_id":"cand_f61c7111d334cc9cf9cf","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"104:2:3:1","qac_word_ref":"104:2:3","surface_ar":"مَالًا"}],"gloss":"varlık; edinme, çoğalma ve başkasına kazandırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin sahip olduğu ve değer taşıyan varlıkların bütünü bu dalın ad çekirdeğini oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Göçebe toplulukların varlığına ilişkin belirli kullanımda bu varlık, hayvan sürüleriyle somutlaşır."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişinin kendisi için değerli varlık edinmesi ve onu kalıcı sahiplik konusu yapması eylem çekirdeğidir."}},{"facet_id":"F004","role":"core","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kişinin varlığının çoğalması ya da onun varlık sahibi bir duruma geçmesi ayrı bir süreç görünümüdür."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Bir başkasına değerli varlık vererek onu varlık sahibi duruma getirmek, çekirdeğin ettirgen uzantısıdır."}},{"facet_id":"F006","role":"associated_use","source_fields":["distinctive_facets[F006]"],"statements":{"statement":"Bir kimsenin varlığının çokluğuna şaşma bildiren söyleyiş, artış ve bolluk görünümüne bağlı bir kullanımdır."}}],"root_ar":"م و ل","root_id":"root_001457","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın sahip olunan varlık, onu edinme, varlıklı duruma gelme ve başkasını varlık sahibi kılma çekirdeklerini birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Dal yalnızca para ya da birikmiş değer değildir; varlığın kendisini, edinilmesini, artmasını, varlıklı duruma geçişi ve başkasına varlık kazandırmayı ayırarak kapsar.","branch_image_ar":"اتخاذ المال وكثرته","concept_gloss":"varlık; edinme, çoğalma ve başkasına kazandırma","contextual_glosses":[{"applicability":"Bir kişinin elindeki değer taşıyan şeylerin bütünü ya da bunların çoğulu ad olarak anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Edinme, çoğalma, varlıklı duruma gelme ve başkasına varlık kazandırma süreçlerini karşılamaz.","preserves":"Dalın kişiye ait değerli varlıklar bildiren ad çekirdeğini korur."},"facet_ids":["F001"],"text":"sahip olunan değerli varlıklar","usage_role":"general"},{"applicability":"Kişinin değerli bir şeyi kendisi için edinip sahipliğinde tutması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Varlık adını, varlığın kendiliğinden artmasını ve başkasına varlık kazandırmayı dışarıda bırakır.","preserves":"Kendisi için varlık edinme ve onu kalıcı sahiplik konusu yapma sürecini korur."},"facet_ids":["F003"],"text":"kendine kalıcı varlık edinmek","usage_role":"contextual"},{"applicability":"Bir kişinin sahip olduklarının artması ya da kişinin varlık sahibi hale gelmesi anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Varlığın ad çekirdeğini, bilinçli edinmeyi ve başkasını varlık sahibi kılmayı karşılamaz.","preserves":"Varlık artışını ve kişinin varlıklı duruma geçişini açıkça korur."},"facet_ids":["F004"],"text":"varlığı çoğalmak veya varlıklı duruma gelmek","usage_role":"contextual"},{"applicability":"Bir kişinin başkasına değerli varlık vererek onun sahiplik durumunu değiştirmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Varlığın kendisini, kişinin kendisi için edinmesini ve kendi varlığının artmasını karşılamaz.","preserves":"Başkasına varlık kazandıran ettirgen katılımcı değişimini korur."},"facet_ids":["F005"],"text":"birini varlık sahibi yapmak","usage_role":"contextual"}],"definition":"Kişinin sahip olduğu değerli varlıkların bütünü ile bunları edinme, çoğaltma ya da bunlara sahip duruma gelme alanıdır. Ayrıca başkasını varlık sahibi kılmayı kapsar; göçebe topluluklara özgü kullanımda sahip olunan varlık özellikle hayvan sürüleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin sahip olduğu ve değer taşıyan varlıkların bütünü bu dalın ad çekirdeğini oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Göçebe toplulukların varlığına ilişkin belirli kullanımda bu varlık, hayvan sürüleriyle somutlaşır."},{"facet_id":"F003","role":"core","statement":"Kişinin kendisi için değerli varlık edinmesi ve onu kalıcı sahiplik konusu yapması eylem çekirdeğidir."},{"facet_id":"F004","role":"core","statement":"Kişinin varlığının çoğalması ya da onun varlık sahibi bir duruma geçmesi ayrı bir süreç görünümüdür."},{"facet_id":"F005","role":"extension","statement":"Bir başkasına değerli varlık vererek onu varlık sahibi duruma getirmek, çekirdeğin ettirgen uzantısıdır."},{"facet_id":"F006","role":"associated_use","statement":"Bir kimsenin varlığının çokluğuna şaşma bildiren söyleyiş, artış ve bolluk görünümüne bağlı bir kullanımdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Dalın bütün sahip olunan varlıkları kapsayan alanını yalnızca ödeme aracına indirger.","fit":"narrowing","loses":"Nakit dışındaki varlıkları, hayvan sürüsü özelleşmesini ve edinme, artma, varlıklılaşma ile kazandırma süreçlerini siler.","preserves":"Değer taşıyan ve sahip olunabilen bir şey düşüncesinin yalnızca nakit yönünü korur."},"text":"para"}],"identity_rationale":"Kaynak ifadesi, sahip olunan değerli varlıkları ve bunların çoğulunu; kişinin kendisi için varlık edinmesini, varlığının çoğalmasını ya da varlıklı duruma gelmesini ve başkasını varlık sahibi kılmasını birlikte aktarır. Göçebe toplulukların varlığının hayvan sürüleriyle somutlaşması bu çekirdeğin bağlama bağlı bir özelleşmesidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kişinin sahip olduğu değerli varlık"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kişinin sahip olduğu değerli varlıklar"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"göçebe toplulukların başlıca varlığı sayılan hayvan sürüleri"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"varlık sahibi veya çok varlıklı kimse"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kendine kalıcı varlık edinmek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"varlığı çoğalmak veya varlık sahibi duruma gelmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birini varlık sahibi yapmak veya ona değerli varlık vermek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"mal sözcüğünün küçültme biçimi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ne çok varlığı var!"}],"lexicalization_note":"Tanım, genel varlık ve varlık edinme çekirdeğini ayrı tutar; göçebe toplulukların hayvan sürülerini varlık sayan kullanımını yalnızca belirli bir söz öbeğine bağlı özelleşme olarak sınırlar.","neighbor_coverage_note":"Sekiz adayın tümü karşılaştırıldı. Edinme ve varlık artışıyla doğrudan sınır paylaşan üç aday yayımlandı; para yönetimi, belirli varlık türleri, geçim ve sürü adlandırmalarıyla yalnızca uzak alan ortaklığı kuran ötekiler dal sınırını keskinleştirmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın edinme görünümü komşuya yaklaşır, fakat odak daha geniş bir sahip olunan varlık ve varlıklılaşma ailesidir. Komşu ise edinimin amacı ve saklama biçimiyle sınırlı, daha özel bir sahiplik türünü belirtir.","focus_only":"Odak dal, sahip olunan varlığın adını, varlığın artmasını, varlıklı duruma gelmeyi ve başkasını varlık sahibi kılmayı da kapsar.","gloss":"kendisi için edinilen ve saklanan varlık","neighbor_only":"Komşu dal, kişinin kendisi için satış ve ticaret amacı dışında edindiği, gereksinim sonrasında sakladığı ya da temel dayanak yaptığı varlığa özgü koşullar taşır.","neighbor_ref":"root_001265/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin kendisi için değerli varlık edinmesi ve bunu sahipliğinde tutması alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşunun çekirdeği belirli bir mülk ve taşınmaz türüne yönelirken odak dal varlığın türünü sınırlandırmaz; ayrıca artış, varlıklı duruma geçiş ve ettirgen kazandırma anlamlarını içerir.","focus_only":"Odak dal taşınır ya da taşınmaz ayrımı yapmadan varlığı, varlık artışını ve başkasına varlık kazandırmayı kapsar.","gloss":"taşınmaz edinme ve elde tutma","neighbor_only":"Komşu dal özellikle taşınmazı, gelir getiren yeri ve bunları edinip kalıcı sahiplik konusu yapmayı öne çıkarır.","neighbor_ref":"root_001034/B004","relation_type":"near_synonym","shared_zone":"İki dal, değer taşıyan bir şeyi edinme ve kalıcı sahiplik altında bulundurma düşüncesinde birleşir."},{"boundary_match":"partial","distinction":"Örtüşme varlık artışıyla sınırlıdır. Odak dal sahiplik ve edinme ailesini kurarken komşu, büyüyen varlık ile onun bakımı ve artışına ilişkin değerlendirmeleri ayrı bir çekirdek yapar.","focus_only":"Odak dal varlığın genel adını, edinilmesini ve başkasının varlık sahibi yapılmasını da içerir.","gloss":"artan varlık ve onu iyi yönetme","neighbor_only":"Komşu dal büyüyen ya da çok olan varlığı, onun iyi yönetilmesini ve artması yönündeki iyi dileği özellikle öne çıkarır.","neighbor_ref":"root_000205/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da sahip olunan varlığın çokluğu veya artışı belirgin bir ortak alandır."}],"source_phrase_ar":"تمول الرجل اتخذ مالا؛ مال يمال كثر ماله (maqayis)؛ المال معروف وجمعه أموال؛ كانت أموال العرب أنعامهم؛ رجل مال أي ذو مال والفعل تمول (ayn)؛ مال الرجل يمول ويمال إذا صار ذا مال؛ تمول مثله؛ موله غيره (sihah)؛ مال أهل البادية النعم؛ تمول فلان مالا إذا اتخذ قنية من المال؛ ما أموله أي ما أكثر ماله (tahdhib)","source_summary":"Kaynakların toplu anlatımı, sahip olunan değerli varlıkları ve bunların çoğulunu temel alır; varlık edinme, varlığın çoğalması, varlıklı duruma gelme ve başkasını varlık sahibi kılma süreçlerini bu temel çevresinde birleştirir. Hayvan sürüleri göçebe topluluklara özgü somutlaşma, çokluk karşısındaki şaşma söyleyişi ise bağlı bir kullanım olarak aktarılır. Mal adının küçültme biçimi de ayrıca kaydedilir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه المال والأموال واتخاذ المال قنية وكثرة المال وصيرورة الرجل ذا مال وتمويل غيره ونعم أهل البادية","what_is_not_ar":"ليس للمولة العنكبوت ولا للميل عن الوسط ولا لميل الحائط"},"support_links":["sup_953f1ed2d7f138323bde","sup_a23c9210126b6f32d6ca","sup_b514cf3087189c74b36c","sup_e1c1edb9f0088e300aa6","sup_f2abf7bb10381f8f7a58"]},{"boundary":"Dal, örümceğin özelliklerini tanımlamaz; yalnızca örümcek için aktarılan ve güvenilirliği açıkça tartışılan bir adlandırmayı temsil eder.","branch_kind":"unresolved","branch_ref":"root_001457/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"104:2:3:1","qac_word_ref":"104:2:3","surface_ar":"مَالًا"}],"gloss":"örümcek için tartışmalı bir ad","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcük, bazı sözlük aktarımlarında örümceği gösteren bir hayvan adı olarak verilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırmanın doğruluğu ve güvenilir aktarımı açıkça sorgulandığı için bu gönderim kesin kabul edilemez."}}],"root_ar":"م و ل","root_id":"root_001457","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözcüğün örümceğe gönderimi aktarılırken bu adlandırmanın güvenilirliğine ilişkin açık kuşkunun da korunması gereken her durumda uygundur.","boundary_detail":"Dal, örümceğin özelliklerini tanımlamaz; yalnızca örümcek için aktarılan ve güvenilirliği açıkça tartışılan bir adlandırmayı temsil eder.","branch_image_ar":"المُولة العنكبوت","concept_gloss":"örümcek için tartışmalı bir ad","contextual_glosses":[{"applicability":"Tartışmalı hayvan adının bir metinde doğrudan canlıya gönderim yaptığı bağlamda akıcı karşılık olarak kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bu adlandırmanın güvenilirliği ve yerleşikliği üzerindeki açık kaynak kuşkusunu görünmez kılar.","preserves":"Adlandırmanın gönderimde bulunduğu hayvanı doğru biçimde korur."},"facet_ids":["F001"],"text":"örümcek","usage_role":"contextual"}],"definition":"Örümceğe verilen bir ad olarak aktarılır; ancak bu adlandırmanın güvenilirliği kaynak anlatımının kendi içinde açıkça tartışmalıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcük, bazı sözlük aktarımlarında örümceği gösteren bir hayvan adı olarak verilir."},{"facet_id":"F002","role":"source_variant","statement":"Adlandırmanın doğruluğu ve güvenilir aktarımı açıkça sorgulandığı için bu gönderim kesin kabul edilemez."}],"identity_rationale":"Kaynak ifadesi sözcüğü örümceğe verilen bir ad olarak aktarır, fakat aynı ifadenin içinde bu aktarımın kuşkuyla karşılandığını ve güvenilir bir aktarıcıdan işitilmediğini de açıkça bildirir. Bu nedenle hayvanla kurulan bağ korunabilir, ancak yerleşik ve tartışmasız bir ad gibi sunulamaz.","lexicalization_note":"Kanıt, bu tartışmalı adlandırmanın bağımsız ve yerleşik bir yalın sözlük birimi olup olmadığını mekanik olarak çözmez; tanım bu yüzden yalın kullanım varsaymaz.","neighbor_coverage_note":"Dokuz adayın tümü değerlendirildi. Aynı canlıya yönelen iki adlandırma gerçek bir sınır karşılaştırması sağladı; öteki hayvan adları yalnızca geniş canlılar alanını paylaştı, varlık dalı ise ortak köke rağmen anlamsal örtüşme göstermedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Gönderim ortak olsa da odak dalın sözlüksel kimliği kuşkulu bir ad aktarımına bağlıdır. Komşu dal ise canlının doğrudan adını ve onu tanıtan özellikleri kapsadığı için iki adın kullanım sınırları tam olarak eşleşmez.","focus_only":"Odak dal, aynı canlıya yönelen fakat güvenilirliği açıkça tartışılan özel bir ad aktarımıdır.","gloss":"ağ ören örümcek","neighbor_only":"Komşu dal canlının olağan adını, ağ örme niteliğini, ad çeşitlerini ve dil bilgisel biçimlerini kapsar.","neighbor_ref":"root_001054/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın hayvansal gönderimi aynı canlıya, yani örümceğe yönelir."},{"boundary_match":"partial","distinction":"Odak dal yalnızca kuşkulu hayvan adı aktarımıyla sınırlıdır; komşu dalın kendi ayrı adı ve yuvayı gösteren bağlı kullanımı vardır. Bu ek kapsam ve odaktaki güvenilirlik çekincesi tam eşdeğerliği engeller.","focus_only":"Odak dalın örümcek adı sayılması kaynak anlatımında açık kuşku ve güven sorunu taşır.","gloss":"örümcek ve yuvası için özel ad","neighbor_only":"Komşu dal başka bir örümcek adının yanı sıra o örümceğin yuvasını gösteren bağlı bir söz öbeğini de kapsar.","neighbor_ref":"root_001326/B008","relation_type":"near_synonym","shared_zone":"İki dal da örümceğe verilen alışılmadık bir adlandırma üzerinden aynı canlıya gönderimde bulunur."}],"source_phrase_ar":"إن المولة العنكبوت وفيه نظر (maqayis)؛ المولة اسم العنكبوت (ayn)؛ زعم قوم أن المول العنكبوت الواحدة مولة ولم أسمعه عن ثقة (sihah)؛ هي العنكبوت والمولة (tahdhib)","source_summary":"Toplu kaynak kaydı sözcüğü örümceğin adı olarak aktarır, fakat aynı kayıtta bu eşleştirmenin kuşkulu olduğu ve güvenilir bir kaynaktan işitilmediği yönünde açık çekinceler bulunur. Bu yüzden hayvana gönderim ile aktarımın belirsizliği birlikte korunmalıdır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه إطلاق المولة أو المول على العنكبوت إذا ثبتت النسبة","what_is_not_ar":"ليس للمال والأموال ولا لاتخاذ القنية ولا لكثرة المال"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["104:2:1"],"branch_refs":[],"candidate_id":"cand_88294d216e88d25fd8fc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:2:1:dense-reference-routing","source_type":"word_analysis","support_ids":["sup_82414db21c5de54a4066","sup_cbbb8c96d7671a007e47"],"title":"pronoun routing compresses actor and object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:1","qac_refs":["104:2:1:1"],"status":"accepted"}},{"anchor_refs":["104:2:1"],"branch_refs":[],"candidate_id":"cand_f63a821883b9fc674c21","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:2:1:relative-boundary-specification","source_type":"word_analysis","support_ids":["sup_9470a5558cdbad733d39","sup_cbbb8c96d7671a007e47"],"title":"relative pronoun specifies the prior type","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:1","qac_refs":["104:2:1:1"],"status":"accepted"}},{"anchor_refs":["104:2:1"],"branch_refs":[],"candidate_id":"cand_b23ea9ece150db30ca72","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:2:1:verdict-to-behavior","source_type":"word_analysis","support_ids":["sup_68822ba4fbb549ee9fc4","sup_cbbb8c96d7671a007e47"],"title":"verdict becomes behavioral evidence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:1","qac_refs":["104:2:1:1"],"status":"accepted"}},{"anchor_refs":["104:2:2"],"branch_refs":[],"candidate_id":"cand_6711e082b33dc40a1fcf","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000259"],"scope":"focus_ayah","source_local_id":"104:2:2:concentration-root-image","source_type":"word_analysis","support_ids":["sup_c2a40f5e355b0efdd744","sup_e447fefd188f86019273"],"title":"gathering image becomes economic concentration","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:2","qac_refs":["104:2:2:1"],"status":"accepted"}},{"anchor_refs":["104:2:2"],"branch_refs":[],"candidate_id":"cand_9a10406222db21a4c62c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000259"],"scope":"focus_ayah","source_local_id":"104:2:2:established-first-beat","source_type":"word_analysis","support_ids":["sup_b933f7b5cc1a4309e81b","sup_c2a40f5e355b0efdd744"],"title":"perfect verb opens the conduct sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:2","qac_refs":["104:2:2:1"],"status":"accepted"}},{"anchor_refs":["104:2:2"],"branch_refs":[],"candidate_id":"cand_3febdbfbc3df3e8cff51","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000259"],"scope":"focus_ayah","source_local_id":"104:2:2:hoarding-echo-specialized","source_type":"word_analysis","support_ids":["sup_47055d64d919a43d36b9","sup_c2a40f5e355b0efdd744"],"title":"hoarding echo moves toward quantification","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:2","qac_refs":["104:2:2:1"],"status":"accepted"}},{"anchor_refs":["104:2:2"],"branch_refs":[],"candidate_id":"cand_c3043371afa5abd87c13","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000259"],"scope":"focus_ayah","source_local_id":"104:2:2:objectful-accumulation","source_type":"word_analysis","support_ids":["sup_c2a40f5e355b0efdd744","sup_d92b757e7ec5d68217b3"],"title":"explicit object fixes material accumulation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:2","qac_refs":["104:2:2:1"],"status":"accepted"}},{"anchor_refs":["104:2:2"],"branch_refs":[],"candidate_id":"cand_810233b0bd2e718bfc4c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000259"],"scope":"focus_ayah","source_local_id":"104:2:2:qiraat-intensity-contrast","source_type":"word_analysis","support_ids":["sup_9a6559076d2c5b658794","sup_c2a40f5e355b0efdd744"],"title":"variant intensifies gathering without displacing Form I","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:2","qac_refs":["104:2:2:1"],"status":"accepted"}},{"anchor_refs":["104:2:3"],"branch_refs":[],"candidate_id":"cand_d8b4198c75c140794b1b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"104:2:3:concrete-inclination-pressure","source_type":"word_analysis","support_ids":["sup_02864b629508634ae13e","sup_08e0dc2f6979e214ccd5"],"title":"property sense carries concrete pull","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:3","qac_refs":["104:2:3:1"],"status":"accepted"}},{"anchor_refs":["104:2:3"],"branch_refs":[],"candidate_id":"cand_9cf27920aeef40b96035","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"104:2:3:object-and-suffix-loop","source_type":"word_analysis","support_ids":["sup_02864b629508634ae13e","sup_71e7e5895de06e58ce3f"],"title":"wealth is gathered, then resumed by suffix","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:3","qac_refs":["104:2:3:1"],"status":"accepted"}},{"anchor_refs":["104:2:3"],"branch_refs":[],"candidate_id":"cand_5044e9f5a09a5628aae7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"104:2:3:open-wealth-category","source_type":"word_analysis","support_ids":["sup_02864b629508634ae13e","sup_ebfe4dc51650a7cdadef"],"title":"indefinite mass noun opens the wealth category","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:3","qac_refs":["104:2:3:1"],"status":"accepted"}},{"anchor_refs":["104:2:3"],"branch_refs":[],"candidate_id":"cand_04a9a42886d4d99ce30c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"104:2:3:ownership-progression","source_type":"word_analysis","support_ids":["sup_02864b629508634ae13e","sup_d902add99f9862a3f383"],"title":"indefinite wealth becomes possessed wealth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:3","qac_refs":["104:2:3:1"],"status":"accepted"}},{"anchor_refs":["104:2:3"],"branch_refs":[],"candidate_id":"cand_c6b664f18b43d198df49","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"104:2:3:wealth-counting-field","source_type":"word_analysis","support_ids":["sup_02864b629508634ae13e","sup_70bb31fdc583ed352d08"],"title":"wealth-counting pairing is locally sharp","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:3","qac_refs":["104:2:3:1"],"status":"accepted"}},{"anchor_refs":["104:2:4"],"branch_refs":[],"candidate_id":"cand_6dd21d2cff290f8feb49","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:2:4:audible-hinge","source_type":"word_analysis","support_ids":["sup_b11fa29fffa38b2b5fce","sup_beb4e0fd6521f4bf53bf"],"title":"proclitic hinge launches enumeration","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:4","qac_refs":["104:2:4:1"],"status":"accepted"}},{"anchor_refs":["104:2:4"],"branch_refs":[],"candidate_id":"cand_83e3880beef381a02dbb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:2:4:coordination-over-subordination","source_type":"word_analysis","support_ids":["sup_a1a91c373680232a340d","sup_beb4e0fd6521f4bf53bf"],"title":"coordination makes counting a second act","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:4","qac_refs":["104:2:4:1"],"status":"accepted"}},{"anchor_refs":["104:2:5"],"branch_refs":[],"candidate_id":"cand_573a3b20f44b8f0d884c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"104:2:5:bounded-counted-wealth","source_type":"word_analysis","support_ids":["sup_9143306b9866c85103e8","sup_b29d355dcddf93441758"],"title":"numbering makes the wealth bounded","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:5","qac_refs":["104:2:4:2","104:2:4:3"],"status":"accepted"}},{"anchor_refs":["104:2:5"],"branch_refs":[],"candidate_id":"cand_60c4867ac1a54f5a21e9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"104:2:5:finite-form-ii-enumeration","source_type":"word_analysis","support_ids":["sup_9143306b9866c85103e8","sup_91d054ef17f14e7b1ecc"],"title":"Form II makes counting repeated action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:5","qac_refs":["104:2:4:2","104:2:4:3"],"status":"accepted"}},{"anchor_refs":["104:2:5"],"branch_refs":[],"candidate_id":"cand_e90db044c78d97c1b3aa","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"104:2:5:forward-suffix-claim","source_type":"word_analysis","support_ids":["sup_84c7434a11c782febcac","sup_9143306b9866c85103e8"],"title":"closing suffix feeds the next claim","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:5","qac_refs":["104:2:4:2","104:2:4:3"],"status":"accepted"}},{"anchor_refs":["104:2:5"],"branch_refs":[],"candidate_id":"cand_b99723633a701cf36fe7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"104:2:5:marked-wealth-counting-pair","source_type":"word_analysis","support_ids":["sup_9143306b9866c85103e8","sup_b6ce1700b02b5c5d28fe"],"title":"wealth-counting pair is marked","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:5","qac_refs":["104:2:4:2","104:2:4:3"],"status":"accepted"}},{"anchor_refs":["104:2:5"],"branch_refs":[],"candidate_id":"cand_0fa4608be6417449212c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"104:2:5:object-suffix-loop","source_type":"word_analysis","support_ids":["sup_9143306b9866c85103e8","sup_c49e09cf7721fc2504dc"],"title":"suffix closes the wealth loop","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:5","qac_refs":["104:2:4:2","104:2:4:3"],"status":"accepted"}},{"anchor_refs":["104:2:5"],"branch_refs":[],"candidate_id":"cand_3f74c969c7b4f1432be2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"104:2:5:percussive-counting-sound","source_type":"word_analysis","support_ids":["sup_9143306b9866c85103e8","sup_b5a743b751a363573b3a"],"title":"doubled sound enacts itemized counting","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:5","qac_refs":["104:2:4:2","104:2:4:3"],"status":"accepted"}},{"anchor_refs":["104:2:5"],"branch_refs":[],"candidate_id":"cand_b502149b7a4cf644e257","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"104:2:5:qiraat-action-number-contrast","source_type":"word_analysis","support_ids":["sup_9143306b9866c85103e8","sup_f2579f6fa97fe7515408"],"title":"variant exposes action versus number","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:5","qac_refs":["104:2:4:2","104:2:4:3"],"status":"accepted"}},{"anchor_refs":["104:2:5"],"branch_refs":[],"candidate_id":"cand_f4469f18a18a01a61a82","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"104:2:5:reckoning-readiness-pressure","source_type":"word_analysis","support_ids":["sup_9143306b9866c85103e8","sup_923ba90acb4f8a0cc913"],"title":"counting shades into reckoning and readiness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:5","qac_refs":["104:2:4:2","104:2:4:3"],"status":"accepted"}},{"anchor_refs":["104:2:5"],"branch_refs":[],"candidate_id":"cand_dda5dd001869af87a8dd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"104:2:5:shared-agent-sequence","source_type":"word_analysis","support_ids":["sup_9143306b9866c85103e8","sup_b6b413376c37804dfe75"],"title":"same agent completes the second beat","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:2:5","qac_refs":["104:2:4:2","104:2:4:3"],"status":"accepted"}},{"anchor_refs":["104:2:2"],"branch_refs":[],"candidate_id":"cand_c9ddf18266ded21dfe53","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000259"],"scope":"focus_ayah","source_local_id":"104:2:2:1","source_type":"qac_morpheme","support_ids":["sup_8b96301f7758802be215"],"title":"QAC root occurrence: ج م ع","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["104:2:3"],"branch_refs":[],"candidate_id":"cand_ba71019962a3d4163da9","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"104:2:3:1","source_type":"qac_morpheme","support_ids":["sup_265d9dbc292c31f9e066"],"title":"QAC root occurrence: م و ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["104:2:4"],"branch_refs":[],"candidate_id":"cand_70fc4741c710905eb192","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000989"],"scope":"focus_ayah","source_local_id":"104:2:4:2","source_type":"qac_morpheme","support_ids":["sup_ad2715ba4273ac630db0"],"title":"QAC root occurrence: ع د د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["104:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:2","branch_refs":["root_000259/B001","root_000989/B001","root_001457/B001"],"candidate_id":"cand_917b63e73e3876d74363","commentary_obligation":"review","hft_ref":"hft_68b8baa018a464ba66b3","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-aggregation-ledger","source_type":"hft","support_ids":["sup_b514cf3087189c74b36c"],"title":"baseline-aggregation-ledger","trust":"legacy_unbound"},{"anchor_refs":["104:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:2","branch_refs":["root_000259/B003","root_000989/B002","root_001457/B001"],"candidate_id":"cand_e6ef28d6527586d5e78e","commentary_obligation":"review","hft_ref":"hft_2d1fb584105e5ff63100","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-contingency-stockpile","source_type":"hft","support_ids":["sup_953f1ed2d7f138323bde"],"title":"baseline-contingency-stockpile","trust":"legacy_unbound"},{"anchor_refs":["104:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:2","branch_refs":["root_000259/B009","root_000989/B005","root_001457/B001"],"candidate_id":"cand_8c1b705ebfff2fd9f386","commentary_obligation":"review","hft_ref":"hft_c023017646a8f92f79e3","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-totality-recurrence","source_type":"hft","support_ids":["sup_a23c9210126b6f32d6ca"],"title":"baseline-totality-recurrence","trust":"legacy_unbound"},{"anchor_refs":["104:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:2","branch_refs":["root_000259/B002","root_000989/B006","root_001457/B001"],"candidate_id":"cand_22cd05023d5dcbb1f72e","commentary_obligation":"review","hft_ref":"hft_4028f6427c23e49280f8","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-comparative-score","source_type":"hft","support_ids":["sup_f2abf7bb10381f8f7a58"],"title":"baseline-comparative-score","trust":"legacy_unbound"},{"anchor_refs":["104:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:2","branch_refs":["root_000259/B005","root_000989/B001","root_001457/B001"],"candidate_id":"cand_f61c7111d334cc9cf9cf","commentary_obligation":"review","hft_ref":"hft_a756ec76b82c9d71e7af","kind":"surprising_outlier","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:outlier-clenched-palm-ledger","source_type":"hft","support_ids":["sup_e1c1edb9f0088e300aa6"],"title":"outlier-clenched-palm-ledger","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ","qac_morphemes":[{"lemma_ar":"ٱلَّذِى","morph_features":"STEM|POS:REL|LEM:{l~a*iY|MS","morpheme_role":"STEM","pos":"REL","qac_ref":"104:2:1:1","qac_word_ref":"104:2:1","root_ar":"","surface_ar":"ٱلَّذِى"},{"lemma_ar":"جَمَعَ","morph_features":"STEM|POS:V|PERF|LEM:jamaEa|ROOT:jmE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:2:1","qac_word_ref":"104:2:2","root_ar":"ج م ع","surface_ar":"جَمَعَ"},{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"104:2:3:1","qac_word_ref":"104:2:3","root_ar":"م و ل","surface_ar":"مَالًا"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"104:2:4:1","qac_word_ref":"104:2:4","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"عَدَّدَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Ead~ada|ROOT:Edd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:4:2","qac_word_ref":"104:2:4","root_ar":"ع د د","surface_ar":"عَدَّدَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"104:2:4:3","qac_word_ref":"104:2:4","root_ar":"","surface_ar":"هُۥ"}],"word_analysis_qac_refs":[["104:2:1:1"],["104:2:2:1"],["104:2:3:1"],["104:2:4:1"],["104:2:4:2","104:2:4:3"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["104:2:1","104:2:2","104:2:3","104:2:4","104:2:5"]},"focus_surface_evidence":{"arabic_uthmani":"ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ","qac_morphemes":[{"lemma_ar":"ٱلَّذِى","morph_features":"STEM|POS:REL|LEM:{l~a*iY|MS","morpheme_role":"STEM","pos":"REL","qac_ref":"104:2:1:1","qac_word_ref":"104:2:1","root_ar":"","surface_ar":"ٱلَّذِى"},{"lemma_ar":"جَمَعَ","morph_features":"STEM|POS:V|PERF|LEM:jamaEa|ROOT:jmE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:2:1","qac_word_ref":"104:2:2","root_ar":"ج م ع","surface_ar":"جَمَعَ"},{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"104:2:3:1","qac_word_ref":"104:2:3","root_ar":"م و ل","surface_ar":"مَالًا"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"104:2:4:1","qac_word_ref":"104:2:4","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"عَدَّدَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Ead~ada|ROOT:Edd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:2:4:2","qac_word_ref":"104:2:4","root_ar":"ع د د","surface_ar":"عَدَّدَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"104:2:4:3","qac_word_ref":"104:2:4","root_ar":"","surface_ar":"هُۥ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["104:2:1:1"],["104:2:2:1"],["104:2:3:1"],["104:2:4:1"],["104:2:4:2","104:2:4:3"]],"word_analysis_refs":["104:2:1","104:2:2","104:2:3","104:2:4","104:2:5"],"word_rows":[{"analysis_record_ref":"104:2:1","analytic_gloss_range_en":"masculine singular relative pronoun that resumes the condemned type from 104:1 and introduces the defining action-clause in 104:2","analytic_root_gloss_range_en":null,"qac_refs":["104:2:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"ٱلَّذِى","transliteration":"alladhī"}},{"analysis_record_ref":"104:2:2","analytic_gloss_range_en":"Form I perfect verb, locally transitive with wealth as object; the selected sense is gathered or amassed, with concentration pressure sharpened by the object and the following counting verb","analytic_root_gloss_range_en":"broad root range of gathering scattered things, assembling groups, places of gathering, resolve, wholeness, and distant branches; the local object selects wealth-amassing from the gathering branch","qac_refs":["104:2:2:1"],"root":{"arabic":"ج م ع","transliteration":"j-m-ʿ"},"surface":{"arabic":"جَمَعَ","transliteration":"jamaʿa"}},{"analysis_record_ref":"104:2:3","analytic_gloss_range_en":"indefinite accusative singular mass noun meaning wealth or property; locally the gathered object that is then resumed and counted","analytic_root_gloss_range_en":"wealth/property branch, including possessible value and livestock-as-wealth background; review-only distant branches do not affect the local noun","qac_refs":["104:2:3:1"],"root":{"arabic":"م و ل","transliteration":"m-w-l"},"surface":{"arabic":"مَالًۭا","transliteration":"mālan"}},{"analysis_record_ref":"104:2:4","analytic_gloss_range_en":"proclitic conjunction coordinating the second perfect verb with the first; main force is coordination, with sequence and close coupling available from context","analytic_root_gloss_range_en":null,"qac_refs":["104:2:4:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa-"}},{"analysis_record_ref":"104:2:5","analytic_gloss_range_en":"perfect Form II verb with object suffix, locally repeated or intensive counting/reckoning of the gathered wealth; preparation and numbered-limit branches add pressure but do not replace enumeration","analytic_root_gloss_range_en":"broad root range including counting, number, reckoning, preparation, appointed counted terms, recurrent times, and counterparts; the local Form II verb with suffix selects enumerating or repeatedly reckoning the wealth","qac_refs":["104:2:4:2","104:2:4:3"],"root":{"arabic":"ع د د","transliteration":"ʿ-d-d"},"surface":{"arabic":"عَدَّدَهُۥ","transliteration":"ʿaddadahū"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["104:2"],"branch_refs":["root_000259/B001","root_000989/B001","root_001457/B001"],"candidate_id":"cand_917b63e73e3876d74363","evidence_scope":"focus_ayah","hft_ref":"hft_68b8baa018a464ba66b3","item_id":"baseline-aggregation-ledger","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-aggregation-ledger","support_id":"sup_b514cf3087189c74b36c"},{"anchor_refs":["104:2"],"branch_refs":["root_000259/B003","root_000989/B002","root_001457/B001"],"candidate_id":"cand_e6ef28d6527586d5e78e","evidence_scope":"focus_ayah","hft_ref":"hft_2d1fb584105e5ff63100","item_id":"baseline-contingency-stockpile","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-contingency-stockpile","support_id":"sup_953f1ed2d7f138323bde"},{"anchor_refs":["104:2"],"branch_refs":["root_000259/B009","root_000989/B005","root_001457/B001"],"candidate_id":"cand_8c1b705ebfff2fd9f386","evidence_scope":"focus_ayah","hft_ref":"hft_c023017646a8f92f79e3","item_id":"baseline-totality-recurrence","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-totality-recurrence","support_id":"sup_a23c9210126b6f32d6ca"},{"anchor_refs":["104:2"],"branch_refs":["root_000259/B002","root_000989/B006","root_001457/B001"],"candidate_id":"cand_22cd05023d5dcbb1f72e","evidence_scope":"focus_ayah","hft_ref":"hft_4028f6427c23e49280f8","item_id":"baseline-comparative-score","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-comparative-score","support_id":"sup_f2abf7bb10381f8f7a58"},{"anchor_refs":["104:2"],"branch_refs":["root_000259/B005","root_000989/B001","root_001457/B001"],"candidate_id":"cand_f61c7111d334cc9cf9cf","evidence_scope":"focus_ayah","hft_ref":"hft_a756ec76b82c9d71e7af","item_id":"outlier-clenched-palm-ledger","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier-clenched-palm-ledger","support_id":"sup_e1c1edb9f0088e300aa6"}],"diagnostics":[],"lane_counts":{"global":11,"macro":18,"micro":5},"packet_summary":{"ayah_count":9,"focus_ref":"104:2","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"و ص د","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000036","furuq_root_norm":"ء ص د","furuq_source_root_norm":"أ ص د","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001653","furuq_root_norm":"و ص د","furuq_source_root_norm":"و ص د","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:8","104:9"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"104:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":11,"source_present":true,"structured_insight_count":23,"unstructured_record_count":0},"identity":{"ayah_ref":"104:2","lane":"micro","linguistic_source_ref":"104:2","surface_ref":"104:2","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"104:2","target_tokens":[["Mal",["104:2:3"]],["toplayan",["104:2:1","104:2:2"]],["ve",["104:2:4"]],["onu",["104:2:4"]],["sayandır",["104:2:1","104:2:4"]]],"text":"Mal toplayan ve onu sayandır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":9,"id":"s104-p01-001-009","label":"Whole surah","number":1,"refs":["104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:8","104:9"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:3","source_type":"word_analysis","support_id":"sup_02864b629508634ae13e","text":"{\"gloss_range\":\"indefinite accusative singular mass noun meaning wealth or property; locally the gathered object that is then resumed and counted\",\"prose\":\"{{ar:مَالًۭا}} ({{tr:mālan}}) gives the first verb its tangible object. As an indefinite accusative mass noun, it keeps the category open: wealth of any kind is what gets gathered. The noun then becomes the antecedent of the suffix in {{ar:عَدَّدَهُۥ}} ({{tr:ʿaddadahū}}), so the same wealth moves from gathered object to counted object. Its non-possessive form also prepares the shift in 104:3, where the next occurrence makes the wealth possessed. Root-family evidence keeps the property sense concrete and possessible, almost herd-like, while inclination pressure makes wealth the thing the subject leans toward before repeated measurement. Distributional pressure also keeps this from being generic possession: the wealth is immediately pulled into a marked accumulation-and-counting frame.\",\"root_display\":\"{{ar:م و ل}} ({{tr:m-w-l}})\",\"root_gloss_range\":\"wealth/property branch, including possessible value and livestock-as-wealth background; review-only distant branches do not affect the local noun\",\"surface_display\":\"{{ar:مَالًۭا}} ({{tr:mālan}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:3:concrete-inclination-pressure","source_type":"word_analysis","support_id":"sup_08e0dc2f6979e214ccd5","text":"{\"blocking_evidence\":null,\"headline\":\"property sense carries concrete pull\",\"reader_payoff\":\"The reader feels wealth as possessible, gathered value that draws the subject toward repeated attention.\",\"reason\":\"The accepted V4 branch is wealth/property; camel-property and inclination notes can enrich concreteness and desire-pressure but do not replace the local noun sense.\",\"representative_source_ids\":[\"QS-0d20cd80\",\"QS-1975d81e\",\"QS-3e456c94\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"104:2:3:1","source_type":"qac_morpheme","support_id":"sup_265d9dbc292c31f9e066","text":"{\"lemma_ar\":\"مَال\",\"morph_features\":\"STEM|POS:N|LEM:maAl|ROOT:mwl|M|INDEF|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"104:2:3:1\",\"qac_word_ref\":\"104:2:3\",\"root_ar\":\"م و ل\",\"surface_ar\":\"مَالًا\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:2:hoarding-echo-specialized","source_type":"word_analysis","support_id":"sup_47055d64d919a43d36b9","text":"{\"blocking_evidence\":null,\"headline\":\"hoarding echo moves toward quantification\",\"reader_payoff\":\"The reader links the gathering verb to a broader hoarding warning while noticing that 104:2 turns storage into repeated measurement.\",\"reason\":\"The 70:18 parallel supports a hoarding-field echo, but the local second verb narrows the comparison to gathered wealth being counted rather than simply stored.\",\"representative_source_ids\":[\"QI-e31aef6b\",\"QE-ae4efb3d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:1:verdict-to-behavior","source_type":"word_analysis","support_id":"sup_68822ba4fbb549ee9fc4","text":"{\"blocking_evidence\":null,\"headline\":\"verdict becomes behavioral evidence\",\"reader_payoff\":\"The reader notices the movement from the prior nominal judgment to a concrete record of conduct that explains it.\",\"reason\":\"The local clause begins with a relative pronoun and then supplies two coordinated perfect verbs, so the behavioral sequence functions as the specification of the prior verdict.\",\"representative_source_ids\":[\"QT-1f8c88ce\",\"QB-107f24ec\",\"QB-e0d5b680\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:3:wealth-counting-field","source_type":"word_analysis","support_id":"sup_70bb31fdc583ed352d08","text":"{\"blocking_evidence\":null,\"headline\":\"wealth-counting pairing is locally sharp\",\"reader_payoff\":\"The reader notices that this wealth is immediately pulled into a marked counting frame, not left as a generic possession topic.\",\"reason\":\"The co-occurrence and warning-context rows support pressure around wealth and counting, while local grammar narrows that pressure to accumulation plus quantification.\",\"representative_source_ids\":[\"QI-f7ce66fa\",\"QE-5dc8b488\",\"QH-c3ac3654\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:3:object-and-suffix-loop","source_type":"word_analysis","support_id":"sup_71e7e5895de06e58ce3f","text":"{\"blocking_evidence\":null,\"headline\":\"wealth is gathered, then resumed by suffix\",\"reader_payoff\":\"The reader follows one object through two actions: the wealth gathered first is the wealth counted at the end.\",\"reason\":\"Attachment evidence makes the noun the direct object of the first verb and resolves the final object suffix back to it.\",\"representative_source_ids\":[\"QG-3be16fef\",\"QG-60e30a0e\",\"QT-1c64dadb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:1:dense-reference-routing","source_type":"word_analysis","support_id":"sup_82414db21c5de54a4066","text":"{\"blocking_evidence\":null,\"headline\":\"pronoun routing compresses actor and object\",\"reader_payoff\":\"The reader sees how a five-word ayah stays cohesive through one relative subject, two understood verb subjects, and one object suffix.\",\"reason\":\"Attachment evidence links the relative pronoun as subject of both verbs and resolves the final suffix back to the wealth object.\",\"representative_source_ids\":[\"QG-66a81480\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:5:forward-suffix-claim","source_type":"word_analysis","support_id":"sup_84c7434a11c782febcac","text":"{\"blocking_evidence\":null,\"headline\":\"closing suffix feeds the next claim\",\"reader_payoff\":\"The reader follows the final suffix into 104:3, where counted wealth becomes possessed wealth and then the object of a larger claim.\",\"reason\":\"The current suffix resolves to the wealth object, and the next ayah repeats suffixal possession and effect language.\",\"representative_source_ids\":[\"QE-196f8d97\",\"QB-1535cf64\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"104:2:2:1","source_type":"qac_morpheme","support_id":"sup_8b96301f7758802be215","text":"{\"lemma_ar\":\"جَمَعَ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:jamaEa|ROOT:jmE|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"104:2:2:1\",\"qac_word_ref\":\"104:2:2\",\"root_ar\":\"ج م ع\",\"surface_ar\":\"جَمَعَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:5","source_type":"word_analysis","support_id":"sup_9143306b9866c85103e8","text":"{\"gloss_range\":\"perfect Form II verb with object suffix, locally repeated or intensive counting/reckoning of the gathered wealth; preparation and numbered-limit branches add pressure but do not replace enumeration\",\"prose\":\"{{ar:عَدَّدَهُۥ}} ({{tr:ʿaddadahū}}) closes the ayah by acting again on the wealth already gathered. As a finite Form II perfect, it makes enumeration an agency-bearing trait, not a detached tally; the doubled consonant and the form's iterative force make the counting feel repeated. The suffix {{ar:هُۥ}} ({{tr:-hū}}) loops back to {{ar:مَالًۭا}} ({{tr:mālan}}), so the wealth is compressed into the final verb and becomes the last audible object of the ayah. Root-family evidence lets counting shade into reckoning, boundedness, and readiness, but the local form selects repeated enumeration rather than the Form IV preparation branch. The variant {{ar:وَعَدَدَهُ}} ({{tr:wa-ʿadadahu}}) exposes how much the doubling controls the difference between repeated action and a simpler number-reading; 104:3 then continues the suffix chain from counted wealth to possessed wealth and its claimed effect.\",\"root_display\":\"{{ar:ع د د}} ({{tr:ʿ-d-d}})\",\"root_gloss_range\":\"broad root range including counting, number, reckoning, preparation, appointed counted terms, recurrent times, and counterparts; the local Form II verb with suffix selects enumerating or repeatedly reckoning the wealth\",\"surface_display\":\"{{ar:عَدَّدَهُۥ}} ({{tr:ʿaddadahū}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:5:finite-form-ii-enumeration","source_type":"word_analysis","support_id":"sup_91d054ef17f14e7b1ecc","text":"{\"blocking_evidence\":null,\"headline\":\"Form II makes counting repeated action\",\"reader_payoff\":\"The reader notices that the final word presents counting as a performed, repeated trait rather than a static number attached to wealth.\",\"reason\":\"QAC identifies a perfect Form II verb with object suffix; the local form and V4 counting branch support repeated enumeration.\",\"representative_source_ids\":[\"QG-1d6e58ed\",\"QG-7d68f749\",\"QF-a3c06430\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:5:reckoning-readiness-pressure","source_type":"word_analysis","support_id":"sup_923ba90acb4f8a0cc913","text":"{\"blocking_evidence\":null,\"headline\":\"counting shades into reckoning and readiness\",\"reader_payoff\":\"The reader sees the counting as mental valuation and provisioning pressure, while still reading the surface action as enumeration.\",\"reason\":\"V4 separates enumerating from preparing; the local Form II verb and object suffix select counting/reckoning, while preparation and readiness remain root-family pressure.\",\"representative_source_ids\":[\"QS-3e709aa0\",\"QS-aef2b995\",\"QI-dd85138a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:1:relative-boundary-specification","source_type":"word_analysis","support_id":"sup_9470a5558cdbad733d39","text":"{\"blocking_evidence\":null,\"headline\":\"relative pronoun specifies the prior type\",\"reader_payoff\":\"The reader notices that 104:2 is not a new sentence about a new person but a relative specification of the condemned type in 104:1.\",\"reason\":\"The prior-ayah antecedent is strongly licensed, and the relative form makes the following verbs identifying conduct; the naʿt/badal and universal-type claims are kept as attachment pressure, not as competing referents.\",\"representative_source_ids\":[\"QG-c6511473\",\"QG-e34cc72b\",\"MG-6972e84e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:2:qiraat-intensity-contrast","source_type":"word_analysis","support_id":"sup_9a6559076d2c5b658794","text":"{\"blocking_evidence\":null,\"headline\":\"variant intensifies gathering without displacing Form I\",\"reader_payoff\":\"The reader sees that an intensive gathering reading is available in the reading tradition, while the local surface lets the following counting verb carry the clearest iteration.\",\"reason\":\"The accepted variant is useful contrast, but the aligned QAC surface is Form I, so the variant sharpens the profile without governing the canonical local parse.\",\"representative_source_ids\":[\"QF-e3d7644b\",\"QF-e934b2dd\",\"QE-4b72f2c8\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:4:coordination-over-subordination","source_type":"word_analysis","support_id":"sup_a1a91c373680232a340d","text":"{\"blocking_evidence\":null,\"headline\":\"coordination makes counting a second act\",\"reader_payoff\":\"The reader notices that counting is not merely a circumstance of gathering but a second coordinated action by the same figure.\",\"reason\":\"Attachment evidence syntactically forces coordination of the two finite verbs; possible circumstantial coloring is kept as closeness, not as the main parse.\",\"representative_source_ids\":[\"QG-6adfc507\",\"QG-8dbeb148\",\"QT-b33466f1\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"104:2:4:2","source_type":"qac_morpheme","support_id":"sup_ad2715ba4273ac630db0","text":"{\"lemma_ar\":\"عَدَّدَ\",\"morph_features\":\"STEM|POS:V|PERF|(II)|LEM:Ead~ada|ROOT:Edd|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"104:2:4:2\",\"qac_word_ref\":\"104:2:4\",\"root_ar\":\"ع د د\",\"surface_ar\":\"عَدَّدَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:4:audible-hinge","source_type":"word_analysis","support_id":"sup_b11fa29fffa38b2b5fce","text":"{\"blocking_evidence\":null,\"headline\":\"proclitic hinge launches enumeration\",\"reader_payoff\":\"The reader hears the small connector run into the heavy second verb as the same wealth shifts from acquired material to measured material.\",\"reason\":\"The conjunction is written as a proclitic on the second verb and its attachment role links the two local verbal beats.\",\"representative_source_ids\":[\"QF-cc355fce\",\"QT-db7d3d70\",\"QP-ce0010b8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:5:bounded-counted-wealth","source_type":"word_analysis","support_id":"sup_b29d355dcddf93441758","text":"{\"blocking_evidence\":null,\"headline\":\"numbering makes the wealth bounded\",\"reader_payoff\":\"The reader notices the irony that wealth treated as control becomes finite precisely because it is countable.\",\"reason\":\"The counted/number branch licenses boundedness and reckoning as pressure, but the local grammar keeps wealth as the object being enumerated.\",\"representative_source_ids\":[\"QS-42d71887\",\"QS-6a0a3825\",\"QS-68671df6\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:5:percussive-counting-sound","source_type":"word_analysis","support_id":"sup_b5a743b751a363573b3a","text":"{\"blocking_evidence\":null,\"headline\":\"doubled sound enacts itemized counting\",\"reader_payoff\":\"The reader hears the repeated dental stop as a measured, item-by-item texture matching the counting sense.\",\"reason\":\"The sound claim is anchored in the local doubled consonant and supports the already licensed Form II enumeration.\",\"representative_source_ids\":[\"QP-4d30cfdc\",\"QP-fb6325ab\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:5:shared-agent-sequence","source_type":"word_analysis","support_id":"sup_b6b413376c37804dfe75","text":"{\"blocking_evidence\":null,\"headline\":\"same agent completes the second beat\",\"reader_payoff\":\"The reader sees accumulation and enumeration as two acts of one subject, with counting following from gathering.\",\"reason\":\"Attachment evidence coordinates the second verb with the first and recovers the same relative pronoun as subject.\",\"representative_source_ids\":[\"QG-73e6eca6\",\"QT-dc496f82\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:5:marked-wealth-counting-pair","source_type":"word_analysis","support_id":"sup_b6ce1700b02b5c5d28fe","text":"{\"blocking_evidence\":null,\"headline\":\"wealth-counting pair is marked\",\"reader_payoff\":\"The reader recognizes counting wealth as a salient pairing and as material itemization that mirrors the prior social itemizing profile.\",\"reason\":\"The co-occurrence evidence is sparse enough to mark the pair locally, but it does not by itself create a broad formula beyond the ayah's sequence.\",\"representative_source_ids\":[\"QI-631bfbb7\",\"QH-3b6fefdd\",\"QB-8e99acfa\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:2:established-first-beat","source_type":"word_analysis","support_id":"sup_b933f7b5cc1a4309e81b","text":"{\"blocking_evidence\":null,\"headline\":\"perfect verb opens the conduct sequence\",\"reader_payoff\":\"The reader sees gathering as the first completed beat in a behavioral profile controlled by the relative pronoun.\",\"reason\":\"The verb is perfect 3ms with its subject recovered from the relative pronoun, and the coordinated second verb completes the same verbal frame.\",\"representative_source_ids\":[\"QG-667ee638\",\"QG-a78096a1\",\"QT-3a3e8422\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:4","source_type":"word_analysis","support_id":"sup_beb4e0fd6521f4bf53bf","text":"{\"gloss_range\":\"proclitic conjunction coordinating the second perfect verb with the first; main force is coordination, with sequence and close coupling available from context\",\"prose\":\"{{ar:وَ}} ({{tr:wa-}}) is the hinge between acquisition and enumeration. It coordinates {{ar:عَدَّدَهُۥ}} ({{tr:ʿaddadahū}}) with {{ar:جَمَعَ}} ({{tr:jamaʿa}}), keeping both actions inside the same relative clause and under the same subject from {{ar:ٱلَّذِى}} ({{tr:alladhī}}). The main force is not a subordinate while-clause: counting becomes a second finite act. Still, the short proclitic is fused to the doubled verb in recitation, so the two actions feel tightly coupled as gathered wealth turns into measured wealth.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa-}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:2","source_type":"word_analysis","support_id":"sup_c2a40f5e355b0efdd744","text":"{\"gloss_range\":\"Form I perfect verb, locally transitive with wealth as object; the selected sense is gathered or amassed, with concentration pressure sharpened by the object and the following counting verb\",\"prose\":\"{{ar:جَمَعَ}} ({{tr:jamaʿa}}) is not left as generic assembly. Its explicit object, {{ar:مَالًۭا}} ({{tr:mālan}}), makes the action material accumulation, and the perfect form presents that accumulation as part of the relative figure's established profile. The root's image of drawing scattered things into one collected whole remains active as concentration: wealth is pulled inward instead of dispersed. Variant and sound evidence can intensify that picture through {{ar:جَمَّعَ}} ({{tr:jammaʿa}}), but the aligned surface remains Form I, so the strongest visible iteration is reserved for {{ar:عَدَّدَهُۥ}} ({{tr:ʿaddadahū}}). The echo with 70:18 helps mark gathering as a hoarding-field verb, while 104:2 specializes that field by moving from gathered wealth to counted wealth.\",\"root_display\":\"{{ar:ج م ع}} ({{tr:j-m-ʿ}})\",\"root_gloss_range\":\"broad root range of gathering scattered things, assembling groups, places of gathering, resolve, wholeness, and distant branches; the local object selects wealth-amassing from the gathering branch\",\"surface_display\":\"{{ar:جَمَعَ}} ({{tr:jamaʿa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:5:object-suffix-loop","source_type":"word_analysis","support_id":"sup_c49e09cf7721fc2504dc","text":"{\"blocking_evidence\":null,\"headline\":\"suffix closes the wealth loop\",\"reader_payoff\":\"The reader hears the ayah land on the counted wealth itself, compressed into the final suffix.\",\"reason\":\"The object suffix is syntactically forced as the direct object and is resolved to the previous wealth noun.\",\"representative_source_ids\":[\"QG-d44b1c45\",\"QF-51403a21\",\"QT-46d12fac\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:1","source_type":"word_analysis","support_id":"sup_cbbb8c96d7671a007e47","text":"{\"gloss_range\":\"masculine singular relative pronoun that resumes the condemned type from 104:1 and introduces the defining action-clause in 104:2\",\"prose\":\"{{ar:ٱلَّذِى}} ({{tr:alladhī}}) makes 104:2 dependent on the prior verdict and epithet in 104:1. The pronoun does not introduce a new actor; it resumes that prior type (104:1) and turns it into a behavioral profile: the one who gathered wealth and counted it. Its definite relative form can specify an indefinite universal type without making the referent a named individual, while the possible attachment analyses tighten or restate the same referent rather than changing it. The result is compact cohesion: the relative pronoun controls both pro-dropped verb subjects, and the object suffix later returns to the same wealth.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:ٱلَّذِى}} ({{tr:alladhī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:3:ownership-progression","source_type":"word_analysis","support_id":"sup_d902add99f9862a3f383","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite wealth becomes possessed wealth\",\"reader_payoff\":\"The reader notices a grammatical progression from open wealth in 104:2 to possessed wealth in 104:3.\",\"reason\":\"The local noun is non-possessive and indefinite, then the same wealth is resumed by suffix and echoed as possessed wealth in 104:3.\",\"representative_source_ids\":[\"QG-d9e53a54\",\"QE-e4afe845\",\"QY-0669e14e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:2:objectful-accumulation","source_type":"word_analysis","support_id":"sup_d92b757e7ec5d68217b3","text":"{\"blocking_evidence\":null,\"headline\":\"explicit object fixes material accumulation\",\"reader_payoff\":\"The reader notices that the verb is not abstract gathering but wealth-directed amassing.\",\"reason\":\"QAC and attachment evidence make the verb transitive with an explicit accusative wealth object, which selects the local amassing sense.\",\"representative_source_ids\":[\"QG-82aa8bef\",\"QG-fd5cce53\",\"QS-99232a61\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:2:concentration-root-image","source_type":"word_analysis","support_id":"sup_e447fefd188f86019273","text":"{\"blocking_evidence\":null,\"headline\":\"gathering image becomes economic concentration\",\"reader_payoff\":\"The reader pictures the action as pulling dispersed value inward, not merely acquiring an item.\",\"reason\":\"V4 licenses the gathered-whole branch and the wealth-collocation sense; other root branches remain background and do not replace the local wealth-amassing reading.\",\"representative_source_ids\":[\"QS-7158d002\",\"QS-d919aec6\",\"QB-580f448c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:3:open-wealth-category","source_type":"word_analysis","support_id":"sup_ebfe4dc51650a7cdadef","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite mass noun opens the wealth category\",\"reader_payoff\":\"The reader sees that the object is not one named asset but wealth as an open class of possessible value.\",\"reason\":\"QAC marks the noun as indefinite accusative, and V4's local branch supports the ordinary wealth/property sense.\",\"representative_source_ids\":[\"QF-4f8fb64a\",\"QF-96103114\",\"QS-851d2f3b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:2:5:qiraat-action-number-contrast","source_type":"word_analysis","support_id":"sup_f2579f6fa97fe7515408","text":"{\"blocking_evidence\":null,\"headline\":\"variant exposes action versus number\",\"reader_payoff\":\"The reader sees how one doubled consonant controls whether the second beat sounds like repeated counting or a simpler number/tally reading.\",\"reason\":\"The variant is valid contrast for segmentation and intensity, but the aligned local surface remains the Form II finite verb.\",\"representative_source_ids\":[\"QF-07d25a90\",\"QF-455d28bf\",\"QE-c4901a3c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ","ayah_ref":"104:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000259/B001","root_000989/B001","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000259","role":"The consolidation of scattered parts supplies the inward motion by which separate assets become one controlled stock.","root":"ج م ع","source_ref":"104:2","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Acquired and abundant property supplies the substance being consolidated and controlled.","root":"م و ل","source_ref":"104:2","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000989","role":"Enumeration turns the collected stock into discrete, reviewable units and closes the control loop.","root":"ع د د","source_ref":"104:2","source_word_indices":["4"]}],"changed_reading":{"after":"The verse depicts an operation: he converts dispersed assets into a controlled whole and keeps that whole present to himself by tallying it.","before":"The verse merely identifies someone who has much money."},"confidence":"strong","focus_anchor":"The sequence جَمَعَ مَالًا وَعَدَّدَهُ makes wealth the product of one active operation and the pronominal object of a second.","mechanism":"Dispersed assets are consolidated into a possessed whole and then rendered repeatedly inspectable through enumeration; gathering makes the stock, while counting maintains cognitive and practical control over it.","model_id":"baseline-aggregation-ledger"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-aggregation-ledger","source_type":"hft","support_id":"sup_b514cf3087189c74b36c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ","ayah_ref":"104:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000259/B003","root_000989/B002","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000259","role":"Concerted resolve supplies the purposeful planning that organizes the stockpile.","root":"ج م ع","source_ref":"104:2","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Possessed wealth supplies the reserve through which the plan expects to meet future need.","root":"م و ل","source_ref":"104:2","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000989","role":"Readied equipment and stores recast the tally as prospective provisioning rather than retrospective arithmetic.","root":"ع د د","source_ref":"104:2","source_word_indices":["4"]}],"changed_reading":{"after":"He inventories wealth as preparedness, treating stored means as protection against whatever may arrive.","before":"He counts what he already owns."},"confidence":"medium","focus_anchor":"جَمَعَ and the intensive عَدَّدَ can be read prospectively around مَالًا, not only as a report of completed possession.","mechanism":"Gathering concentrates intention, wealth supplies stored means, and counting functions as preparing an inventory for a coming need. The hoard is therefore an imagined defense against contingency.","model_id":"baseline-contingency-stockpile"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-contingency-stockpile","source_type":"hft","support_id":"sup_953f1ed2d7f138323bde","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ","ayah_ref":"104:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000259/B009","root_000989/B005","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B009","mapped_root_id":"root_000259","role":"Intact wholeness supplies the desired state that the repeated audit tries to preserve.","root":"ج م ع","source_ref":"104:2","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"The acquired stock gives the recurring assurance ritual a material object.","root":"م و ل","source_ref":"104:2","source_word_indices":["3"]},{"branch_id":"B005","mapped_root_id":"root_000989","role":"Counted time and recurrence make the tally a returning practice rather than a single completed act.","root":"ع د د","source_ref":"104:2","source_word_indices":["4"]}],"changed_reading":{"after":"Counting is a recurring reassurance ritual by which the possessor repeatedly reconstructs the hoard as intact.","before":"Counting confirms a stable quantity once."},"confidence":"medium","focus_anchor":"The joined verbs around the same wealth-object permit counting to be a recurrent practice that preserves the collection's felt wholeness.","mechanism":"A desire for an intact total requires recurrent return to the ledger. Enumeration does not finish possession; it periodically renews the assurance that nothing has scattered or gone missing.","model_id":"baseline-totality-recurrence"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-totality-recurrence","source_type":"hft","support_id":"sup_a23c9210126b6f32d6ca","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ","ayah_ref":"104:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000259/B002","root_000989/B006","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000259","role":"An assembled group supplies the social field within which a total can acquire comparative force.","root":"ج م ع","source_ref":"104:2","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Acquired wealth supplies the measurable medium of distinction.","root":"م و ل","source_ref":"104:2","source_word_indices":["3"]},{"branch_id":"B006","mapped_root_id":"root_000989","role":"The counted counterpart turns quantity into a relation of comparison rather than a self-contained sum.","root":"ع د د","source_ref":"104:2","source_word_indices":["4"]}],"changed_reading":{"after":"The total matters because it can rank its possessor against others and make social difference numerically legible.","before":"The total matters because it is large."},"confidence":"exploratory","focus_anchor":"مَالًا is gathered and then counted in a construction that can make the total meaningful relative to other totals, not solely in isolation.","mechanism":"Wealth is assembled into a socially legible score: a collection becomes a count, and a count becomes a counterpart against which persons or shares can be compared.","model_id":"baseline-comparative-score"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-comparative-score","source_type":"hft","support_id":"sup_f2abf7bb10381f8f7a58","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ","ayah_ref":"104:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000259/B005","root_000989/B001","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000259","role":"The closed palm supplies a bodily model of possession as gripping and containing.","root":"ج م ع","source_ref":"104:2","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Wealth supplies what the imagined grip tries to retain.","root":"م و ل","source_ref":"104:2","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000989","role":"Enumeration breaks the mass into mentally handled units, like repeated palmfuls.","root":"ع د د","source_ref":"104:2","source_word_indices":["4"]}],"changed_reading":{"after":"The hoard acquires a bodily posture: value is repeatedly gathered into an imagined fist and handled unit by unit.","before":"The hoard is an abstract financial total."},"confidence":"exploratory","containment":"The bodily image is surprising because جَمَعَ does not lexically mean clenching here, yet the focus inventory explicitly supplies the gathered palm and the count remains directly anchored in عَدَّدَهُ. Carry this only as a tactile material analogy: the hoard is mentally reduced to graspable palmfuls, not as a replacement translation.","focus_anchor":"The adjacent gathering, wealth, and counting operations permit a bodily picture of possession as grasp plus tactile enumeration.","outlier_id":"outlier-clenched-palm-ledger"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:outlier-clenched-palm-ledger","source_type":"hft","support_id":"sup_e1c1edb9f0088e300aa6","trust":"legacy_unbound"}]}
</lane_packet_json>
