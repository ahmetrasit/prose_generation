# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **104:3**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s104-regular-20260911/s104/104_3/micro.discovery.json` and modify nothing
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
  "ayah_ref": "104:3",
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
{"analysis_context":{"analysis_id":"s104-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"104:3","host_surah":104,"lane_context_refs":[],"ordered_context_refs":["104:0","104:1","104:2","104:4","104:5","104:6","104:7","104:8","104:9","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Çekirdek, sayı yoluyla nicelik belirlemektir; sanma, yeterlik ve yalnızca belirli söz öbeklerinde doğan sınırsız verme anlamları dışarıda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000318/B001","candidate_links":[{"candidate_id":"cand_93f1eda88186c0d94ece","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَسِبَ","morph_features":"STEM|POS:V|IMPF|LEM:Hasiba|ROOT:Hsb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:3:1:1","qac_word_ref":"104:3:1","surface_ar":"يَحْسَبُ"}],"gloss":"sayarak nicelik belirleme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesneler tek tek sayılır ve nicelikleri sayı kullanılarak belirlenir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Güneş ile ayın hareketleri, bilinen ve belirlenmiş bir sayı düzeni içinde ele alınır."}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesnelerin sayılması ve sayı düzeniyle ölçünün ortaya çıkarılması anlatılırken kullanılır.","boundary_detail":"Çekirdek, sayı yoluyla nicelik belirlemektir; sanma, yeterlik ve yalnızca belirli söz öbeklerinde doğan sınırsız verme anlamları dışarıda kalır.","branch_image_ar":"العد والحساب","concept_gloss":"sayarak nicelik belirleme","contextual_glosses":[{"applicability":"Tek tek nesnelerin kaç tane olduğunun bulunmasını anlatan cümlelerde doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güneş ile ayın belirli sayı ve zaman düzenine bağlı oluşunu belirtmez.","preserves":"Nesneleri sayma ve ulaşılan niceliği belirleme işlemini korur."},"facet_ids":["F001"],"text":"sayısını çıkarmak","usage_role":"contextual"},{"applicability":"Güneş ile ayın ölçülü ve düzenli hareketini açıklayan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gündelik nesnelerin tek tek sayılması işlemini kapsamaz.","preserves":"Gök cisimleri için belirlenmiş sayı düzeni yönünü açıkça korur."},"facet_ids":["F002"],"text":"belirli bir sayı düzenine bağlı olmak","usage_role":"explanatory"}],"definition":"Nesneleri sayı yoluyla tek tek belirlemek ve sayı kullanarak niceliği ortaya çıkarmaktır. Güneş ile ay için bu, hareketlerin önceden belirlenmiş bir sayı ve zaman düzenine bağlı oluşuna uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesneler tek tek sayılır ve nicelikleri sayı kullanılarak belirlenir."},{"facet_id":"F002","role":"specialization","statement":"Güneş ile ayın hareketleri, bilinen ve belirlenmiş bir sayı düzeni içinde ele alınır."}],"identity_rationale":"Kaynak sözü, nesneleri sayma, sayıyı işlemde kullanma ve güneş ile ayın belirli bir sayı düzenine bağlı oluşunu açıkça destekler. Geçici çerçevedeki her türlü denetleme ve kestirim bu çekirdeğin parçası sayılamaz; bunlar ancak belirli türevlerde veya kuruluşlarda geçerlidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"nesneyi saymak ve niceliğini çıkarmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"sayma ve nicelik belirleme işlemi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"sayma işlemi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sayı yoluyla belirleme"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"belirli sayı düzeni ve zaman ölçüsü"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ölçmeden, denetlemeden veya kısmadan; beklenenden fazla"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"sayıp değerlendiren ve gözeten"}],"lexicalization_note":"Tanım, yalın sayma çekirdeğini korur; gök cisimlerinin düzeni ve ölçüsüz verme gibi kurulu kullanımları bu çekirdekle birleştirmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; doğrudan sayma sınırını en iyi gösteren komşu yayımlandı, yalnızca aynı konu çevresinde duran veya başka dallara ait adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı sayma işlemiyle nicelik çıkarır ve belirli bir göksel düzene uzanabilir; komşu dal ise bütün öğeleri eksiksiz sayıp kuşatma sınırını öne çıkarır.","focus_only":"Saymanın yanında nicelik çıkarma ve gök cisimleri için belirli sayı düzeni kapsamı vardır.","gloss":"sayıyla belirleme ve eksiksiz sayıp dökme","neighbor_only":"Sayıyla eksiksiz kuşatma, bütün öğeleri tüketme ve bilgice kapsama vurgusu vardır.","neighbor_ref":"root_000332/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da çokluğu sayı yoluyla belirleme ve öğeleri tek tek ele alma alanında buluşur."}],"source_phrase_ar":"الأول العد؛ الحساب عدك الأشياء؛ حسبت الحساب؛ حسبته إذا عددته؛ الحساب استعمال العدد؛ الشمس والقمر بحسبان","source_summary":"Ortak anlatım, nesneleri saymayı ve sayıyı nicelik belirleme aracı olarak kullanmayı merkeze alır; güneş ile ayın düzeni de bilinen bir sayısal ölçüye bağlanır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه عد الأشياء والحساب والمحاسبة والتقدير والمقدار وحساب الشمس والقمر","what_is_not_ar":"ليس هو الظن ولا الكفاية ولا الحسب والشرف"},"support_links":["sup_4a78d971a33817b4ceb0"]},{"boundary":"Bu dal sayısal belirleme değil, kesin bilgi olmadan bir önermeyi zihinde daha olası görmedir.","branch_kind":"bare","branch_ref":"root_000318/B002","candidate_links":[{"candidate_id":"cand_677c82ef547a34a7806a","lane":"micro"},{"candidate_id":"cand_02f464379c2a0a55c3f9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَسِبَ","morph_features":"STEM|POS:V|IMPF|LEM:Hasiba|ROOT:Hsb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:3:1:1","qac_word_ref":"104:3:1","surface_ar":"يَحْسَبُ"}],"gloss":"öyle olduğunu sanmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, kesinlik bulunmadığı halde bir durumun öyle olduğuna zihnen yönelir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Zihinsel yargı, iki karşıt olasılıktan birini ötekine üstün tutma biçiminde kurulabilir."}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir durum hakkında kesin olmayan fakat belirli bir yöne eğilen zihinsel yargı anlatılırken kullanılır.","boundary_detail":"Bu dal sayısal belirleme değil, kesin bilgi olmadan bir önermeyi zihinde daha olası görmedir.","branch_image_ar":"الحسبان والظن","concept_gloss":"öyle olduğunu sanmak","contextual_glosses":[{"applicability":"Bir kişi veya durum hakkında kesin olmayan olumlu ya da olumsuz yargıda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kesin olmayan zihinsel yönelişi ve yargının belirli bir seçeneğe bağlanmasını korur."},"facet_ids":["F001","F002"],"text":"öyle sanmak","usage_role":"general"}],"definition":"Kesin bilgiye ulaşmadan, karşıt olasılıklardan birini zihinde doğruya daha yakın görüp o yönde yargıya varmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, kesinlik bulunmadığı halde bir durumun öyle olduğuna zihnen yönelir."},{"facet_id":"F002","role":"specialization","statement":"Zihinsel yargı, iki karşıt olasılıktan birini ötekine üstün tutma biçiminde kurulabilir."}],"identity_rationale":"Kaynak sözü, bir şeyi doğru kabul etmeye yönelik fakat kesinliğe ulaşmamış zihinsel yargıyı açıkça anlatır. İki karşıt olasılıktan birine yönelme, dalın sanma çekirdeğini sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"öyle sanmak ve zihnen öyle olduğuna hükmetmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"sanı ve kesin olmayan yargı"}],"lexicalization_note":"Tanım yalın sanma ve kesin olmayan yargı alanıyla sınırlıdır; başka kuruluşlara özgü sayma veya yeterlik anlamı içeri alınmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; kesin olmayan inanışla en yakın sınırı kuran dal seçildi, yalnızca kuşku, bilgi veya aynı kökün başka anlamlarını taşıyanlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı bir seçeneği doğruya daha yakın görerek yargı kurmayı öne çıkarır; komşu dalda ise kuşku ve zayıf dayanak belirleyici sınırdır.","focus_only":"İki karşıt olasılıktan biri lehine zihinsel hüküm kurma yönü açıkça bulunur.","gloss":"kesin olmadan sanma","neighbor_only":"Kesinsizlik, zayıf inanış ve güçsüz bir belirtiye dayanan kuruntu daha baskındır.","neighbor_ref":"root_000969/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da kesin bilgi düzeyine varmayan bir inanış veya zihinsel yöneliş bildirir."}],"source_phrase_ar":"الحسبان الظن؛ حسبت كذا في معنى ظننت؛ حسبته صالحا أي ظننته؛ حسبت الشيء ظننته؛ الحسبان أن يحكم لأحد النقيضين","source_summary":"Ortak kaynak anlatımı, bir şeyi kesin olarak bilmekten ayrı biçimde öyle sanmayı ve karşıt seçeneklerden biri lehine zihinsel yargı kurmayı bildirir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه حسب الشيء أو الأمر بمعنى ظنه وقدره في النفس وما يقاربه من توقع غير جازم","what_is_not_ar":"ليس هو الحساب العددي ولا الكفاية ولا الاحتساب للأجر"},"support_links":["sup_007498efdaabcfdfe43a","sup_a5d14fa88a405c5daf3c"]},{"boundary":"Çekirdek bir ihtiyacı karşılayacak ölçüye ulaşmaktır; bol armağan yalnızca belirtilen verme kuruluşlarında bu çekirdeği aşar.","branch_kind":"mixed_non_bare","branch_ref":"root_000318/B003","candidate_links":[{"candidate_id":"cand_51b1d1fc565bc4fd7ac4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَسِبَ","morph_features":"STEM|POS:V|IMPF|LEM:Hasiba|ROOT:Hsb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:3:1:1","qac_word_ref":"104:3:1","surface_ar":"يَحْسَبُ"}],"gloss":"gereksinimi karşılayacak kadar yetmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey, kişinin gereksinimini karşılar ve başka bir şeye yönelme ihtiyacını kaldırır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Verme bağlamında alıcıya yetecek, onu hoşnut edecek veya bol sayılacak miktar sunulur."}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin gerekli ölçüyü karşılaması veya verilenin alıcıya yeterli gelmesi anlatılırken kullanılır.","boundary_detail":"Çekirdek bir ihtiyacı karşılayacak ölçüye ulaşmaktır; bol armağan yalnızca belirtilen verme kuruluşlarında bu çekirdeği aşar.","branch_image_ar":"الكفاية والإغناء","concept_gloss":"gereksinimi karşılayacak kadar yetmek","contextual_glosses":[{"applicability":"Bir nesnenin, miktarın veya desteğin ihtiyacı karşılaması anlatıldığında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Verme kuruluşlarında görülen bol ve hoşnut edici miktar genişlemesini belirtmez.","preserves":"Gereksinimin karşılanması ve başka şeye ihtiyaç kalmaması yönünü korur."},"facet_ids":["F001"],"text":"yeterli gelmek","usage_role":"general"},{"applicability":"Bir kişiye onu doyuracak veya hoşnut edecek miktarda verme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir şeyin kendi başına yeterli olması biçimindeki genel kullanımı kapsamaz.","preserves":"Yeterli miktar verme ve bunun bolluğa uzanabilmesi yönlerini korur."},"facet_ids":["F002"],"text":"yetecek kadar, hatta bolca vermek","usage_role":"contextual"}],"definition":"Bir kişi veya durum için gereken miktara ulaşıp başka bir şeye ihtiyaç bırakmamaktır. Verme bağlamında, alıcıyı doyuracak kadar hatta kimi kullanımda beklenenden çok vermeye uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey, kişinin gereksinimini karşılar ve başka bir şeye yönelme ihtiyacını kaldırır."},{"facet_id":"F002","role":"extension","statement":"Verme bağlamında alıcıya yetecek, onu hoşnut edecek veya bol sayılacak miktar sunulur."}],"identity_rationale":"Kaynak sözü bir şeyin ihtiyacı karşılamasını, bir kimseye yeterli miktar verilmesini ve bazı verme kuruluşlarında bolluğu açıkça bir araya getirir. Yeterlik çekirdeği korunarak bol verme, kurulu kullanıma bağlı bir genişleme olarak tutulabilir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bu sana yeter; bununla yetin"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"Tanrı bize yeter"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bu bana yetti"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ona yetecek veya onu hoşnut edecek kadar vermek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yeterli ya da bol armağan"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ölçmeden, denetlemeden veya kısmadan; beklenenden fazla"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"soyluluk ile yeterlik arasında iki türlü yorumlanan şiir sözü"}],"lexicalization_note":"Yalın yeterlik çekirdeği ile belirli verme sözlerinde görülen yeterli ya da bol miktar ayrı yüzler olarak tanımlanır.","neighbor_coverage_note":"Bütün adaylar incelendi; genel yeterlik çekirdeğini en iyi sınayan komşu yayımlandı, yalnızca bolluk, hoşnutluk veya ilgisiz aynı-kök dalları elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı gereken miktarın yeterli oluşunu ve verme kapsamını öne çıkarır; komşu dal ise işi üstlenip sonucu sağlayan etkin yeterliği de içerir.","focus_only":"Yeterlik bildiren kalıpların yanında alıcıya yeterli veya bol miktarda verme genişlemesi vardır.","gloss":"gereksinimi karşılayıp yeterli olma","neighbor_only":"Bir işi üstlenip sonuna kadar götürerek açığı kapatma ve amacı gerçekleştirme yönü vardır.","neighbor_ref":"root_001310/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da gereksinimin karşılanması ve başka bir desteğe ihtiyaç bırakılmaması alanında buluşur."}],"source_phrase_ar":"الأصل الثاني الكفاية؛ حسبك هذا أي كفاك؛ حسبي كذا أي يكفيني؛ أحسبني الشيء أي كفاني؛ حسبنا الله أي كافينا هو؛ عطاء حسابا أي كافيا","source_summary":"Ortak anlatım, bir şeyin yeterli olmasını ve verilen miktarın alıcının gereksinimini karşılamasını temel alır; bazı verme örnekleri bu miktarı bolluk yönünde genişletir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه حسبك وحسبي وأحسبني وأحسبته وما يكون كافيا أو مرضيا أو واسعا في العطاء","what_is_not_ar":"ليس هو العد المحض ولا الظن ولا الحسب في المفاخر"},"support_links":["sup_b536e11f375c81d424b5"]},{"boundary":"Bu dal sayısal sayma değil, kişi ve ataları için sayılıp anılan iyi işler ile bunların sağladığı köklü saygınlıktır.","branch_kind":"mixed_non_bare","branch_ref":"root_000318/B004","candidate_links":[{"candidate_id":"cand_dcec01042f7f3fe6e960","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَسِبَ","morph_features":"STEM|POS:V|IMPF|LEM:Hasiba|ROOT:Hsb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:3:1:1","qac_word_ref":"104:3:1","surface_ar":"يَحْسَبُ"}],"gloss":"atalardan gelen saygınlık ve iyi işler birikimi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin ve atalarının iyi işleri ile övünülecek başarıları birlikte değerlendirilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu birikim kişiye veya topluluğuna kalıcı bir soyluluk ve saygınlık kazandırır."}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin veya topluluğun geçmişten gelen soyluluğu ve övünülecek eylemleri birlikte anlatıldığında kullanılır.","boundary_detail":"Bu dal sayısal sayma değil, kişi ve ataları için sayılıp anılan iyi işler ile bunların sağladığı köklü saygınlıktır.","branch_image_ar":"الحسب والمآثر","concept_gloss":"atalardan gelen saygınlık ve iyi işler birikimi","contextual_glosses":[{"applicability":"Ataların ve kişinin iyi işlerinden doğan yerleşik toplumsal değer öne çıktığında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Saygınlığı oluşturan tek tek iyi işler ve övünülecek başarılar geri planda kalır.","preserves":"İyi eylemlerden doğan ve kuşaklar boyunca süren saygınlık sonucunu korur."},"facet_ids":["F002"],"text":"köklü saygınlık","usage_role":"contextual"}],"definition":"Bir kişinin kendisine ve atalarına bağlanan iyi işler, övünülecek başarılar ve bunların oluşturduğu köklü saygınlık birikimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin ve atalarının iyi işleri ile övünülecek başarıları birlikte değerlendirilir."},{"facet_id":"F002","role":"extension","statement":"Bu birikim kişiye veya topluluğuna kalıcı bir soyluluk ve saygınlık kazandırır."}],"identity_rationale":"Kaynak sözü, kişinin ve atalarının iyi işleri ile bunlardan doğan kalıcı saygınlığı aynı çekirdekte toplar. Dal, salt soy çizgisinden daha geniştir; kişinin kendi güzel eylemleri de bu birikime dahildir.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"atalardan gelen saygınlık ve övünülecek işler"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"soylu, saygın veya eli açık kişi"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"soyluluk ya da yeterlik diye yorumlanan şiir sözü"}],"lexicalization_note":"Tanım ortak saygınlık çekirdeğini verir; kişiyi niteleyen türevler ve iki anlamlı şiir sözü ayrı lexical yüzler olarak tutulur.","neighbor_coverage_note":"Tüm adaylar karşılaştırıldı; birikmiş saygınlık ile tekil övgü değerini ayıran komşu yayımlandı, salt soy, yüksek konum veya karşıt düşüş adayları elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı iyi işleri soy ve geçmiş içinde biriken saygınlığın bütünü olarak ele alır; komşu dal ise tekil bir güzel özellik veya övgüye değer işi belirtir.","focus_only":"Kişinin ve atalarının eylemlerinden oluşan kuşaklar arası saygınlık birikimi vardır.","gloss":"saygınlık birikimi ve soylu özellik","neighbor_only":"Tek bir soylu özellik, güzel davranış veya yiğitçe iş ayrı bir değer olarak adlandırılır.","neighbor_ref":"root_001539/B010","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişiyi övgüye değer kılan iyi eylemler ve nitelikler alanındadır."}],"source_phrase_ar":"الحسب الذي يعد من الإنسان؛ الحسب الشرف الثابت في الآباء؛ حسب الرجل مآثر آبائه وأجداده؛ ما يعده الإنسان من مفاخر آبائه؛ الحسب الفعال الحسن له ولآبائه","source_summary":"Kaynaklar, kişi ve atalarının iyi eylemlerini, övünülecek başarılarını ve bunların kuşaklar boyunca oluşturduğu saygınlığı ortak içerik olarak sunar.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه شرف الآباء والمآثر والدين والمال والخلق والجود وما يعد للرجل أو قومه من مفاخر","what_is_not_ar":"ليس هو الحساب العددي ولا الكفاية ولا الوسادة"},"support_links":["sup_7997df843d843a7107ae"]},{"boundary":"Eylem veya kayıp Tanrı katındaki karşılık amacıyla değer hanesine yazılır; gündelik sayım ya da kamusal denetim amaç değildir.","branch_kind":"bare","branch_ref":"root_000318/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَسِبَ","morph_features":"STEM|POS:V|IMPF|LEM:Hasiba|ROOT:Hsb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:3:1:1","qac_word_ref":"104:3:1","surface_ar":"يَحْسَبُ"}],"gloss":"Tanrı katında karşılığını beklemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iş, iyilik veya kayıp Tanrı katında kişinin değer hanesine yazılmış sayılır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi bu değerlendirme karşılığında Tanrı'dan iyilik bekler."}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir işin, iyiliğin veya kaybın Tanrı katında değerli sayılarak karşılığının beklendiği durumlarda kullanılır.","boundary_detail":"Eylem veya kayıp Tanrı katındaki karşılık amacıyla değer hanesine yazılır; gündelik sayım ya da kamusal denetim amaç değildir.","branch_image_ar":"الاحتساب عند الله","concept_gloss":"Tanrı katında karşılığını beklemek","contextual_glosses":[{"applicability":"İyi bir iş yapılırken veya acı bir kayıp kabullenilirken göksel karşılık beklentisini anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylem ya da kaybın değerli sayılmasını ve karşılığın Tanrı'dan beklenmesini korur."},"facet_ids":["F001","F002"],"text":"karşılığını Tanrı'dan beklemek","usage_role":"general"}],"definition":"Yapılan bir işi, gerçekleşen bir iyiliği veya uğranan bir kaybı Tanrı katında değer hanesine yazıp bunun karşılığını beklemektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iş, iyilik veya kayıp Tanrı katında kişinin değer hanesine yazılmış sayılır."},{"facet_id":"F002","role":"core","statement":"Kişi bu değerlendirme karşılığında Tanrı'dan iyilik bekler."}],"identity_rationale":"Kaynak sözü, yapılan bir işi, bir iyiliği veya çocuk kaybını Tanrı katında değer hanesine yazıp karşılığını beklemeyi açıkça anlatır. Bu yön, iyi yönetim ve kötü davranışı denetleme dalından ayrıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bir işi veya kaybı Tanrı katında değer hanesine yazıp karşılığını beklemek"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"Tanrı katında karşılık umularak yapılan iş"}],"lexicalization_note":"Tanım, Tanrı katında karşılık bekleme çekirdeğini genel dal sınırı olarak korur ve yönetimle ilgili kurulu kullanımları içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; değer hanesine yazma ile gerçek sayma arasındaki ayrımı gösteren iç komşu yayımlandı, ilgisiz kişi ve miktar adayları elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalındaki değerlendirme inanç ve karşılık beklentisine yöneliktir; komşu dalda ise amaç nesnelerin sayısını ve niceliğini belirlemektir.","focus_only":"Bir iş veya kayıp Tanrı katında değerli sayılır ve bunun göksel karşılığı beklenir.","gloss":"değer hanesine yazma ve sayarak belirleme","neighbor_only":"Nesneler sayı yoluyla belirlenir ve nicelikleri çıkarılır.","neighbor_ref":"root_000318/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir şeyi kayda geçirip değerlendirme düşüncesi bulunur."}],"source_phrase_ar":"احتسب فلان ابنه؛ احتسابك الأجر؛ احتسب فلان عند الله خيرا؛ احتسبت بكذا أجرا عند الله؛ احتسب ابنا له أي اعتد به عند الله؛ الحسبة فعل ما يحتسب به عند الله تعالى","source_summary":"Ortak anlatım, bir işin veya çocuk kaybının Tanrı katında değerli sayılmasını ve kişinin bunun karşılığını beklemesini bir arada verir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه احتساب الأجر واعتداد الولد أو الخير عند الله تعالى","what_is_not_ar":"ليس هو حسن التدبير ولا الإنكار على القبيح ولا الظن"},"support_links":[]},{"boundary":"Dal, belirli kuruluşlara bağlı yönetme, kınama ve kamusal gözetim kullanımlarını kapsar; Tanrı katında karşılık beklemeyi kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000318/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَسِبَ","morph_features":"STEM|POS:V|IMPF|LEM:Hasiba|ROOT:Hsb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:3:1:1","qac_word_ref":"104:3:1","surface_ar":"يَحْسَبُ"}],"gloss":"işi gözetme, kötü davranışı sorgulama ve kamusal denetim","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iş dikkatle ele alınır ve iyi biçimde çekip çevrilir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kimsenin yaptığı kötü davranış kınanır ve o kişi bu davranış üzerinden sorgulanır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kentte davranışları ve kamu düzenini gözeten görevli bu işi kurumsal olarak yürütür."}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kaynakta verilen yönetme, birine karşı çıkma ve kent görevlisi kuruluşlarının ortak alanını anlatmak için kullanılır.","boundary_detail":"Dal, belirli kuruluşlara bağlı yönetme, kınama ve kamusal gözetim kullanımlarını kapsar; Tanrı katında karşılık beklemeyi kapsamaz.","branch_image_ar":"الحسبة والنظر في الأمر","concept_gloss":"işi gözetme, kötü davranışı sorgulama ve kamusal denetim","contextual_glosses":[{"applicability":"Bir işin dikkatli ve yerinde yönetilmesini bildiren kuruluşta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kötü davranışı kınama ve kamusal görevli yüzlerini kapsamaz.","preserves":"İşi dikkatle ele alma ve iyi yönetme yüzünü korur."},"facet_ids":["F001"],"text":"işi iyi çekip çevirmek","usage_role":"contextual"},{"applicability":"Bir kimseye yaptığı yanlış davranış nedeniyle karşı çıkılan kuruluşta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İyi yönetim ve kentteki kamusal görevli yüzlerini kapsamaz.","preserves":"Kötü davranışa karşı çıkma ve yapanı sorgulama yüzünü korur."},"facet_ids":["F002"],"text":"kötü davranışını kınayıp sorgulamak","usage_role":"contextual"}],"definition":"Belirli kuruluşlarda bir işi iyi çekip çevirmeyi, bir kimsenin kötü davranışını kınayıp sorgulamayı veya kentte bu tür kamusal gözetimi görev olarak yürütmeyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iş dikkatle ele alınır ve iyi biçimde çekip çevrilir."},{"facet_id":"F002","role":"associated_use","statement":"Bir kimsenin yaptığı kötü davranış kınanır ve o kişi bu davranış üzerinden sorgulanır."},{"facet_id":"F003","role":"specialization","statement":"Kentte davranışları ve kamu düzenini gözeten görevli bu işi kurumsal olarak yürütür."}],"identity_rationale":"Kaynak sözü tek bir yalın anlamdan çok, belirli kuruluşlarda iyi yönetme, kötü davranışı kınama ve kentte bu görevi üstlenen kişiyi birlikte verir. Bu kullanımlar yönetim ve gözetim çevresinde ilişkilidir, ancak biri ötekinin zorunlu parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kötü davranışından dolayı kınamak ve yaptığını sorgulamak"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"işi iyi çekip çevirmek ve gözetmek"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kentte kamu düzenini ve davranışları gözeten görevli"}],"lexicalization_note":"Tanım, iyi yönetme, birine karşı kötü işi kınama ve kamusal görevli kullanımlarını ayrı kuruluşlara bağlı yüzler olarak tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kamusal görev sınırını gösteren aday yayımlandı, adalet, hak ödeme, terbiye ve yalnızca aynı senaryoda yer alan dallar elendi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dalı kötü davranışı gözetme ve kınama gibi belirli bir görev alanına bağlıdır; komşu dal her tür kamu işine atanmayı ve o işi yürütmeyi daha genel biçimde kapsar.","focus_only":"İyi yönetme ve kötü davranışı kınama yanında belirli bir kent gözetimi görevi bulunur.","gloss":"kamusal gözetim ve kamu işine atanma","neighbor_only":"Yönetici tarafından herhangi bir kamu işine atanma ve o işi üstlenme genel olarak kapsanır.","neighbor_ref":"root_001046/B003","relation_type":"same_field","shared_zone":"Her iki dal da kamu adına bir işi üstlenen görevli ve görev yürütme alanında buluşur."}],"source_phrase_ar":"حسن الحسبة بالأمر إذا كان حسن التدبير؛ احتسب فلان على فلان أنكر عليه قبيحا عمله؛ احتسبت عليه كذا إذا أنكرته عليه؛ فلان محتسب البلد؛ حسن الحسبة في الأمر","source_summary":"Kaynak sözü, bir işi iyi yönetme, kötü bir davranışı yapan kişiye karşı çıkma ve kentte gözetim görevi üstlenme kullanımlarını aynı dalda fakat ayrı kuruluşlar halinde toplar.","sources":["MQ","JA","SI","TA"],"what_is_ar":"يدخل فيه حسن التدبير في الأمر والإنكار على القبيح والمحاسبة العملية ومحتسب البلد","what_is_not_ar":"ليس هو مجرد الأجر المحتسب عند الله ولا الظن ولا الكفاية"},"support_links":[]},{"boundary":"Kısa ok veya atılan küçük nesne çekirdektir; gökten gelen kullanım, kaynakların değişik yorumladığı yıkıcı bir gönderim olarak ayrı tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_000318/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَسِبَ","morph_features":"STEM|POS:V|IMPF|LEM:Hasiba|ROOT:Hsb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:3:1:1","qac_word_ref":"104:3:1","surface_ar":"يَحْسَبُ"}],"gloss":"kısa ok veya yukarıdan gelen yıkıcı gönderim","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kısa oklar veya bir hedefe fırlatılan küçük nesneler söz konusudur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gökten gelen kullanım, yukarıdan gönderilen yıkıcı bir şey ya da olay anlamına uzanır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu yıkıcı gönderimin dolu, ateş, çekirge veya genel bir yıkım olduğu konusunda farklı açıklamalar vardır."}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kısa fırlatma nesnesi ile gökten gelen değişken yıkım yorumlarını birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Kısa ok veya atılan küçük nesne çekirdektir; gökten gelen kullanım, kaynakların değişik yorumladığı yıkıcı bir gönderim olarak ayrı tutulur.","branch_image_ar":"المرامي والحسبان النازل","concept_gloss":"kısa ok veya yukarıdan gelen yıkıcı gönderim","contextual_glosses":[{"applicability":"Yayla atılan küçük ve kısa nesneler anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gökten gelen yıkıcı gönderime ilişkin değişken kullanımı kapsamaz.","preserves":"Fırlatılan kısa oklar biçimindeki somut çekirdeği korur."},"facet_ids":["F001"],"text":"kısa oklar","usage_role":"contextual"},{"applicability":"Dolu, ateş, çekirge veya genel yıkım arasında değişen göksel gönderim bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Somut küçük ok çekirdeğini ve yorumlar arasındaki ayrıntılı çeşitliliği kapsamaz.","preserves":"Yukarıdan gelme ve zarar verme ortak yönlerini korur."},"facet_ids":["F002","F003"],"text":"gökten gelen yıkıcı şey","usage_role":"explanatory"}],"definition":"Kısa okları veya fırlatılan küçük nesneleri bildirir. Gökten gelme kuruluşunda ise dolu, ateş, çekirge ya da başka bir yıkıcı gönderim olarak değişken biçimde yorumlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kısa oklar veya bir hedefe fırlatılan küçük nesneler söz konusudur."},{"facet_id":"F002","role":"extension","statement":"Gökten gelen kullanım, yukarıdan gönderilen yıkıcı bir şey ya da olay anlamına uzanır."},{"facet_id":"F003","role":"source_variant","statement":"Bu yıkıcı gönderimin dolu, ateş, çekirge veya genel bir yıkım olduğu konusunda farklı açıklamalar vardır."}],"identity_rationale":"Kaynak sözü kısa oklar ve atılan küçük nesneler çekirdeğini açıkça verir; gökten gelen kullanım ise dolu, ateş, çekirge veya genel yıkım olarak değişik biçimlerde açıklanır. Bu ikinci alan tek bir nesne türüymüş gibi daraltılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kısa oklar veya atılan küçük nesneler"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"gökten gönderilen dolu, ateş, çekirge ya da yıkıcı şey"}],"lexicalization_note":"Yalın küçük ok anlamı ile gökten gelme kuruluşundaki dolu, ateş, çekirge veya yıkım yorumları birbirine karıştırılmaz.","neighbor_coverage_note":"Tüm adaylar incelendi; gökten gelen yıkım alanındaki en yararlı sınır yayımlandı, ateş, ışık, sıcaklık ve aynı kökün ilgisiz dalları yalnızca tematik kaldığı için elendi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dalı kısa ok anlamından göksel yıkıcı gönderime uzanan değişken bir kapsama sahiptir; komşu dal ise şiddetli ses ve çarpma niteliğindeki belirli gök olayını merkez alır.","focus_only":"Kısa oklar çekirdeği ve gökten gelen çeşitli yıkıcı nesne yorumları bulunur.","gloss":"gökten gelen yıkım ve şiddetli gök olayı","neighbor_only":"Gök gürültüsüyle bağlantılı tek bir şiddetli çarpma, ses veya yıldırım olayı anlatılır.","neighbor_ref":"root_000864/B002","relation_type":"same_field","shared_zone":"Her iki dal gökten gelen, ateş veya yıkımla ilişkilendirilebilen korkutucu olay alanına girebilir."}],"source_phrase_ar":"الحسبان سهام صغار؛ حسبان من السماء بالبرد؛ حسبانا من السماء أي نارا تحرقها؛ حسبانا عذابا ولا أدري؛ الحسبان بالضم العذاب؛ أصاب الأرض حسبان أي جراد؛ الحسبان المرامي؛ نارا وعذابا","source_summary":"Ortak anlatım kısa okları ve fırlatılan küçük nesneleri verir; gökten gelen kullanımın dolu, ateş, çekirge veya genel bir yıkım sayılması konusunda tek bir nesneye indirgenemeyen açıklama çeşitliliği vardır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحسبان بمعنى السهام أو المرامي أو ما يرسل من السماء من عذاب أو برد أو نار أو جراد أو صاعقة","what_is_not_ar":"ليس هو الحساب المنظم للشمس والقمر ولا الكفاية ولا الوسادة"},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000318/B008","candidate_links":[{"candidate_id":"cand_51b1d1fc565bc4fd7ac4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَسِبَ","morph_features":"STEM|POS:V|IMPF|LEM:Hasiba|ROOT:Hsb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:3:1:1","qac_word_ref":"104:3:1","surface_ar":"يَحْسَبُ"}],"gloss":"yalıtık adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başın altına konan, kimi anlatımda deriden yapılmış küçük bir yastık söz konusudur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kimse bu yastığın üzerine oturtulur veya başı yastıkla desteklenir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı iddiada geçen kısa ok anlamı yastık çekirdeğiyle birleşmez ve ayrı dala bağlanmayı gerektirir."}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"المحسبة والوسادة","concept_gloss":"yalıtık adlandırmalar","contextual_glosses":[{"applicability":"Baş altına konan küçük veya deriden yapılmış destek nesnesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Birini yastığa oturtma eylemini ve karışmış kısa ok kaydını kapsamaz.","preserves":"Yastık nesnesinin küçüklüğünü ve baş desteği işlevini korur."},"facet_ids":["F001"],"text":"küçük yastık","usage_role":"contextual"}],"definition":"Bu dalın güvenli çekirdeği küçük yastık ve birini onun üzerine oturtma ya da başını onunla desteklemedir. Tek kaynak iddiasına kısa ok anlamı da karıştığı için dal ayrılmadan birleşik bir tanım kurulamaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başın altına konan, kimi anlatımda deriden yapılmış küçük bir yastık söz konusudur."},{"facet_id":"F002","role":"extension","statement":"Bir kimse bu yastığın üzerine oturtulur veya başı yastıkla desteklenir."},{"facet_id":"F003","role":"source_variant","statement":"Aynı iddiada geçen kısa ok anlamı yastık çekirdeğiyle birleşmez ve ayrı dala bağlanmayı gerektirir."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"küçük yastık"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"deriden yapılmış veya baş altına konan yastık"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"birini yastığa oturtmak veya başına yastık koymak"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"yastıksız; bazı açıklamalarda ölü sargısına sarılmamış, gömülmemiş ya da onurlandırılmamış"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"الحسبان جمع حسبانة وهي الوسادة الصغيرة؛ الحسبان سهام قصار؛ الحسبانة أيضا الوسادة الصغيرة؛ المحسبة وسادة من أدم؛ حسبته إذا وسدته؛ الحسبانة الوسادة الصغيرة","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه الحسبانة أو المحسبة بمعنى الوسادة الصغيرة وإجلاس الرجل عليها أو توسيده بها","what_is_not_ar":"ليس هو سهام الحسبان ولا الحسب الشريف ولا العد"},"support_links":["sup_b536e11f375c81d424b5"]},{"boundary":"Dal belirli bir deri veya tüy görünümüdür; soyluluk, sayma ve yastık anlamlarıyla ilişkili değildir.","branch_kind":"bare","branch_ref":"root_000318/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَسِبَ","morph_features":"STEM|POS:V|IMPF|LEM:Hasiba|ROOT:Hsb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:3:1:1","qac_word_ref":"104:3:1","surface_ar":"يَحْسَبُ"}],"gloss":"deri veya tüyde karışık ak, kızıl ve koyu görünüm","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan veya devenin derisi ya da tüyü alışılmıştan farklı bir renk görünümü taşır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Görünüm hastalığa bağlı aklık, aklıkla kızıllık, koyu bozluk veya kızıla çalan karalık olarak değişebilir."}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan veya devenin deri ve tüyündeki değişken renk karışımı ya da hastalıklı aklık anlatılırken kullanılır.","boundary_detail":"Dal belirli bir deri veya tüy görünümüdür; soyluluk, sayma ve yastık anlamlarıyla ilişkili değildir.","branch_image_ar":"لون الأحسب والأحسبية","concept_gloss":"deri veya tüyde karışık ak, kızıl ve koyu görünüm","contextual_glosses":[{"applicability":"Özellikle devenin tüyünde aklık ile kızıllığın birlikte görüldüğü bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsandaki hastalık aklığını ve koyu boz ya da kızıla çalan renkleri kapsamaz.","preserves":"Deve tüyündeki aklık ve kızıllık karışımını açıkça korur."},"facet_ids":["F001","F002"],"text":"aklık ve kızıllık karışımı tüylü","usage_role":"contextual"}],"definition":"İnsan ya da devenin derisinde veya tüyünde hastalığa bağlı aklık ya da aklık, kızıllık, koyuluk ve bozluğun değişik birleşimlerinden oluşan görünümdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan veya devenin derisi ya da tüyü alışılmıştan farklı bir renk görünümü taşır."},{"facet_id":"F002","role":"source_variant","statement":"Görünüm hastalığa bağlı aklık, aklıkla kızıllık, koyu bozluk veya kızıla çalan karalık olarak değişebilir."}],"identity_rationale":"Kaynak sözü, insan veya devenin derisi ve tüyünde görülen aklık, kızıllık, koyuluk ve bozluk karışımlarını; ayrıca hastalıkla oluşan aklığı aynı renk alanında verir. Geçici çerçeve bu değişkenliği doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"derisi hastalıkla beyazlamış ya da tüyünde aklık, kızıllık ve koyuluk karışmış kişi veya deve"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"koyu zemin üstünde bozluk ya da kızıla çalan karalık"}],"lexicalization_note":"Tanım, insan ve devede görülen yalın renk veya deri durumu alanıyla sınırlıdır; başka söz öbeklerinden anlam aktarılmaz.","neighbor_coverage_note":"Adayların tümü karşılaştırıldı; genel karışık renk alanıyla en yararlı sınır yayımlandı, yalnızca aklık, toprak tonu, beden kusuru veya hastalık alanında kalanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı insan ve devenin deri ya da tüyündeki belirli görünüşlere, ayrıca hastalık aklığına bağlıdır; komşu dal daha geniş taşıyıcılarla genel renk karışımını adlandırır.","focus_only":"İnsan ve deveyle sınırlı deri veya tüy görünümü, hastalık aklığını ve belirli koyu tonları içerir.","gloss":"belirli deri rengi ve genel karışık renk","neighbor_only":"Renk içinde renk bulunması göz, kan, koyun ve başka taşıyıcılara uzanan daha genel bir karışım alanıdır.","neighbor_ref":"root_000813/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal aklık, kızıllık, karalık veya bozluğun tek görünümde karışmasını anlatabilir."}],"source_phrase_ar":"الأحسب الذي ابيضت جلدته من داء؛ الأحسب من الناس والإبل وهو الأبرص؛ الحسبة غبرة في كدرة؛ الأحسب من الإبل فيه بياض وحمرة؛ الحسبة سواد يضرب إلى الحمرة","source_summary":"Kaynak anlatımı insan ve devede görülen ayırt edici deri ya da tüy rengini ortak alan olarak verir; bu görünüm hastalık aklığından ak-kızıl karışıma ve koyu boz ya da kızıla çalan tona kadar değişir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه الأحسب من الناس أو الإبل وما في الجلد أو الشعر من بياض وحمرة أو غبرة أو داء يشبه البرص","what_is_not_ar":"ليس هو الحسب في الشرف ولا الحساب ولا الوسادة"},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_000318/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَسِبَ","morph_features":"STEM|POS:V|IMPF|LEM:Hasiba|ROOT:Hsb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:3:1:1","qac_word_ref":"104:3:1","surface_ar":"يَحْسَبُ"}],"gloss":"yalıtık adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir haber sorulur, izlenir ve hakkında bilgi edinilmeye çalışılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin elinde ne bulunduğu veya ne sağlayabileceği sınanarak öğrenilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Alıcının verileceğini beklememesi yönündeki parça araştırma çekirdeğinden ayrıdır ve başka dala bağlanmayı gerektirir."}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"التحسب والاستخبار","concept_gloss":"yalıtık adlandırmalar","contextual_glosses":[{"applicability":"Bir olay hakkında bilgi toplamak için soru sorma ve haber arama bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir kişinin elindekini sınamayı ve karışmış beklenti parçasını kapsamaz.","preserves":"Haber isteme ve bilgi izini sürme işlemlerini korur."},"facet_ids":["F001"],"text":"haberi sorup izini sürmek","usage_role":"contextual"},{"applicability":"Bir kişinin neye sahip olduğunu veya ne sağlayabileceğini yoklama bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel haber aramayı ve karışmış beklenti parçasını kapsamaz.","preserves":"Kişide bulunanı sınama ve sonuçta öğrenme yönlerini korur."},"facet_ids":["F002"],"text":"elinde ne olduğunu sınayıp öğrenmek","usage_role":"contextual"}],"definition":"Bu dalın güvenli çekirdeği bir haberi sorup izini sürmek veya bir kişinin elinde ne bulunduğunu sınayarak öğrenmektir. Aynı iddiadaki beklememe parçası bu çekirdekle birleşmediği için yeniden bağlanmalıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir haber sorulur, izlenir ve hakkında bilgi edinilmeye çalışılır."},{"facet_id":"F002","role":"extension","statement":"Bir kişinin elinde ne bulunduğu veya ne sağlayabileceği sınanarak öğrenilir."},{"facet_id":"F003","role":"source_variant","statement":"Alıcının verileceğini beklememesi yönündeki parça araştırma çekirdeğinden ayrıdır ve başka dala bağlanmayı gerektirir."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"haberi sorup izini sürmek"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"birinin elinde ne olduğunu sınayıp öğrenmek"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"بغير أن حسب المعطى أنه يعطيه؛ تحسبت الخبر أي استخبرت؛ احتسبت فلانا اختبرت ما عنده؛ يتحسب الأخبار أي يتحسسها ويطلبها","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه تحسب الخبر واستخباره واختبار ما عند الإنسان وطلب الأخبار","what_is_not_ar":"ليس هو الظن المجرد ولا الحساب العددي ولا الحسبة في التدبير"},"support_links":[]},{"boundary":"Dal hem kesintisiz kalıcılığı hem de sonlu fakat olağandan uzun sürmeyi kapsar; her kullanım mutlak sonsuzluk bildirmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000429/B001","candidate_links":[{"candidate_id":"cand_677c82ef547a34a7806a","lane":"micro"},{"candidate_id":"cand_93f1eda88186c0d94ece","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَخْلَدَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axolada|ROOT:xld|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:3:4:1","qac_word_ref":"104:3:4","surface_ar":"أَخْلَدَ"}],"gloss":"kalıcı olma ve durumunu koruma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlık uzun süre ya da kesintisiz biçimde varlığını sürdürür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Varlığını sürdüren şey, bozulmaya karşı bulunduğu durumu da koruyabilir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ölümden sonraki yaşam yurdu, kalıcılığın kesintisiz gerçekleştiği yer olarak adlandırılır."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Saçın geç ağarması ve taşların yıkıntıdan sonra yerinde kalması, olağandan uzun sürme örnekleridir."}}],"root_ar":"خ ل د","root_id":"root_000429","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Uzun süre varlığını sürdürme ile aynı durumda kalma birlikte öne çıktığında dalın çekirdeğini bütünüyle karşılar.","boundary_detail":"Dal hem kesintisiz kalıcılığı hem de sonlu fakat olağandan uzun sürmeyi kapsar; her kullanım mutlak sonsuzluk bildirmez.","branch_image_ar":"ثبات وبقاء لا يسرع إليه الفناء","concept_gloss":"kalıcı olma ve durumunu koruma","contextual_glosses":[{"applicability":"Süre sonlu olabilse de olağandan uzun kalma ve durumunu koruma anlatılan genel bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uzun sürme ile aynı durumda kalma özelliklerini birlikte korur."},"facet_ids":["F001","F002","F004"],"text":"uzun süre olduğu gibi kalma","usage_role":"general"},{"applicability":"Kesintisiz kalıcılığın özellikle ölümden sonraki yaşam yurdu için anlatıldığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kesintisiz varlık sürdürme ve kalıcı yurt yönlerini eksiksiz taşır."},"facet_ids":["F001","F003"],"text":"sonsuza dek varlığını sürdürme","usage_role":"contextual"}],"definition":"Bir varlığın yok oluşa hemen uğramadan uzun süre ya da sürekli kalması ve bulunduğu durumu korumasıdır. Kalıcı yurt, geç ağarma ve yıkıntıdan sonra kalan taşlar bu sürekliliğin farklı örnekleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlık uzun süre ya da kesintisiz biçimde varlığını sürdürür."},{"facet_id":"F002","role":"specialization","statement":"Varlığını sürdüren şey, bozulmaya karşı bulunduğu durumu da koruyabilir."},{"facet_id":"F003","role":"example","statement":"Ölümden sonraki yaşam yurdu, kalıcılığın kesintisiz gerçekleştiği yer olarak adlandırılır."},{"facet_id":"F004","role":"example","statement":"Saçın geç ağarması ve taşların yıkıntıdan sonra yerinde kalması, olağandan uzun sürme örnekleridir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Anlamı yalnız canlı bir varlığın ölmemesine indirgeyebilir.","fit":"narrowing","loses":"Sonlu fakat olağandan uzun sürmeyi, cansız varlıkları ve aynı durumda kalmayı dışarıda bırakır.","preserves":"Kesintisiz yaşamı sürdürme yönünü güçlü biçimde korur."},"text":"ölümsüzlük"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Mutlak değişmezlik gerektirmeyen uzun süre varlığını sürdürme yönünü kaybeder.","preserves":"Bir şeyin bulunduğu durumu koruması yönünü taşır."},"text":"değişmezlik"},{"category":"confusable","error_profile":{"adds":"Kısa süreli bekleme ve yalnızca bir yerde bulunma gibi genel anlamları da içeri alır.","collision":"Yerleşme anlamıyla ikinci dalın yapılarına yaklaşabilir.","fit":"broadening","loses":"Olağandan uzun sürme ve bozulmaya karşı durumunu koruma sınırını belirtmez.","preserves":"Bir varlığın sürmesi ve bulunduğu yerde bulunmaya devam etmesi yönünü taşır."},"text":"kalmak"}],"identity_rationale":"Yetkili ifade, varlığını sürdürme ile bulunduğu durumda kalma çekirdeğini açıkça kurar; kalıcı yurt, geç ağarma ve yıkıntıdan sonra kalan taşlar bu çekirdeğin ayrı gerçekleşmeleridir. Hazırlanan çerçeve bu ortaklığı, öteki dallardaki yönelme, süs, düşünce ve küçük hayvan anlamlarına taşırmadan korur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kalmak; varlığını sürdürmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kalıcılık; bulunduğu durumda kalma"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"kalıcılık; kalıcı yaşam yurdu"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sonsuz yaşam bahçesi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"ölümden sonraki kalıcı yaşam yurdu"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kalıcı kılmak; kalacağına hükmetmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yaşlandığı halde saçına ak düşmeyen"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"ön kesici dişleri, yan kesici dişleri çıkana kadar düşmeyen hayvan"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yıkıntılar yok olduktan sonra kalan ocak taşları ve kayalar"}],"lexicalization_note":"Çıplak biçimlerdeki kalma çekirdeği ile yurt, kişi, hayvan ve taşlara bağlı özel kullanımlar ayrı tutulur; özel bir kullanım bütün dalın anlamı yapılmaz.","neighbor_coverage_note":"On iki adayın tümü karşılaştırıldı. En güçlü dört dış karşılaştırma ile aynı kökün ilişki sınırını gösteren ikinci dal seçildi; öteki süreklilik adayları seçilenlerle büyük ölçüde yinelendi, diğer kardeş dallar ise yalnız biçim ortaklığı taşıdı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, sürmenin yanında mevcut durumun korunmasını ve buna bağlı özel örnekleri öne çıkarır; komşu ise kalıcılığı etki, ödül ve yaşam süresi gibi daha geniş sonuçlara yayar.","focus_only":"Odak dal, aynı durumda kalmayı ve geç ağarma ile kalıcı taşlar gibi özel gerçekleşmeleri içerir.","gloss":"durumunu koruyan kalıcılık / genel kalıcılık","neighbor_only":"Komşu dal, kalan etki ve ödül ile uzun yaşam gibi daha genel kalıcılık alanlarını da kapsar.","neighbor_ref":"root_000142/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın çekirdeğinde yok oluşa karşı varlığını sürdürme ve uzun süre kalma bulunur."},{"boundary_match":"partial","distinction":"Odak dalın merkezi uzun süreli varlık ve durum devamlılığıdır; komşunun merkezi ise kalıcılığın yanında yer, duruş ve direnç bakımından sağlamlıktır.","focus_only":"Odak dal, kalıcı yaşam yurdu ve bozulmadan aynı durumda sürme yönlerini belirginleştirir.","gloss":"kalıcı kalma / sağlam durma","neighbor_only":"Komşu dal, bir yerde durma, savaşta direnme ve ayakların sağlam basması gibi konumsal ve eylemsel kullanımları içerir.","neighbor_ref":"root_000192/B001","relation_type":"near_synonym","shared_zone":"İki dal da sürme, yerinde kalma ve ortadan kalkmaya karşı direnme alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal süre içindeki varlığın kalmasına bakar; komşu dal ise kalan şeyden bağımsız olarak sürenin kendisini ve sonunun bulunmamasını öne çıkarır.","focus_only":"Odak dal, varlığın ya da durumun bozulmadan sürmesini adlandırır.","gloss":"kalıcılık / sonsuz zaman","neighbor_only":"Komşu dal, zamanın sonu olmayan ya da çok uzun olan ölçüsünü doğrudan adlandırır.","neighbor_ref":"root_000004/B001","relation_type":"near_neighbor","shared_zone":"Uzunluk ve kesintisizlik, iki dalın süre bildiren kullanımlarında ortaklaşır."},{"boundary_match":"partial","distinction":"Odak dal kalıcı varlık ve korunmuş durumla sınırlıdır; komşu, hareketsizlikten yinelenen işe kadar daha geniş bir devam etme alanına yayılır.","focus_only":"Odak dal, yok oluşa karşı kalıcılığı ve aynı durumda korunmayı merkez alır.","gloss":"kalıcılık / durmadan sürme","neighbor_only":"Komşu dal, suyun durulması, işin sürmesi ve sürekli yağmur gibi hareket ile zaman örneklerini de kapsar.","neighbor_ref":"root_000501/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir durumun kesintiye uğramadan devam etmesi düşüncesi vardır."},{"boundary_match":"partial","distinction":"Odak dal bağımsız bir süreklilik durumudur; komşu dal ise tamamlayıcısıyla kurulan yönelme, yapışma veya beraber kalma ilişkisine bağlıdır.","focus_only":"Odak dal, bir varlığın uzun süre ya da sürekli var olmasını ve durumunu korumasını bildirir.","gloss":"kalıcı olma / yönelip bağlı kalma","neighbor_only":"Komşu dal, bir şeye yönelme, yere yapışma, bir yerde oturma ya da birinin yanından ayrılmama bildirir.","neighbor_ref":"root_000429/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da ayrılmama ve bir durum ya da ilişki içinde kalma çağrışımı bulunur."}],"source_phrase_ar":"أصل واحد يدل على الثبات والملازمة (maqayis)؛ الخلود البقاء فيها (ayn)؛ دوام البقاء (jamhara;sihah)؛ دار الخلود والخلد الآخرة والجنة (jamhara)؛ بقاؤه على الحالة التي هو عليها (mufradat)؛ مخلد إذا أبطأ عنه الشيب (maqayis;jamhara;sihah;mufradat)؛ خوالد للأثافي والحجارة لطول مكثها (ayn;sihah;mufradat)","source_summary":"Ortak tanıklık, var olmayı sürdürme ve aynı durumda kalma çekirdeğini; kalıcı yurt, geç ağarma ve uzun süre yerinde duran taşlar gibi farklı uygulamalarla açıklar.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه دوام البقاء أو طول المكث وثبات الحالة، ومنه الخلد والجنة ودار الخلود، والخوالد للأثافي والحجارة، والمخلد لمن أبطأ عنه الشيب أو بقيت ثناياه، وإخلاد الشيء بمعنى جعله مبقى.","what_is_not_ar":"لا يدخل فيه الركون إلى الشيء، ولا تفسير مخلدون بالمقرطين أو المسورين، ولا الخلد بمعنى البال أو الدويبة."},"support_links":["sup_4a78d971a33817b4ceb0","sup_a5d14fa88a405c5daf3c"]},{"boundary":"Bu anlam yalnız belirtilen bağlı yapılarda geçerlidir; kökün tek başına kalıcı olma anlamı buraya genellenemez.","branch_kind":"collocation","branch_ref":"root_000429/B002","candidate_links":[{"candidate_id":"cand_51b1d1fc565bc4fd7ac4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَخْلَدَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axolada|ROOT:xld|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:3:4:1","qac_word_ref":"104:3:4","surface_ar":"أَخْلَدَ"}],"gloss":"yönelip bağlanma, yapışma ya da ayrılmadan kalma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir şeye ya da kimseye yönelir, ona bağlanır ve onu benimser."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yere yönelen şey, onun yüzeyine yapışıp kalabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir yerde bulunmayı sürdürmek ve oradan ayrılmamak anlatılabilir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir kimsenin yanında kalmak ve ondan ayrılmamak anlatılabilir."}}],"root_ar":"خ ل د","root_id":"root_000429","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bağlı yapı açık olduğunda yönelme, fiziksel yapışma, yerde kalma ve eşlik ederek ayrılmama okumalarının ortak yüzeyini verir.","boundary_detail":"Bu anlam yalnız belirtilen bağlı yapılarda geçerlidir; kökün tek başına kalıcı olma anlamı buraya genellenemez.","branch_image_ar":"ركون ولصوق وملازمة","concept_gloss":"yönelip bağlanma, yapışma ya da ayrılmadan kalma","contextual_glosses":[{"applicability":"Bir kişiye ya da şeye gönüllü biçimde yönelme ve onu benimseme anlatılan bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hedefe yönelme, bağlanma ve ondan hoşnut olma bileşenlerini korur."},"facet_ids":["F001"],"text":"ona yönelip razı olma","usage_role":"contextual"},{"applicability":"Bir varlığın yere temas edip yüzeyden ayrılmaması anlatılan fiziksel bağlama özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yere fiziksel temas ile ondan ayrılmama özelliklerini eksiksiz korur."},"facet_ids":["F002"],"text":"yere yapışıp kalma","usage_role":"contextual"},{"applicability":"Belirli bir yerde kalma ve oradan ayrılmama bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli bir yerde bulunmayı sürdürme ve ayrılmama yönünü taşır."},"facet_ids":["F003"],"text":"orada kalma","usage_role":"contextual"},{"applicability":"Bir kimseye eşlik etmeyi ve onun yanında kalmayı anlatan kişi ilişkisine özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir kimsenin yanında kalma ve onu bırakmama ilişkisini korur."},"facet_ids":["F004"],"text":"arkadaşının yanından ayrılmama","usage_role":"contextual"}],"definition":"Yalnız belirli tamamlayıcılarla kurulan yapılarda bir şeye ya da kişiye yönelip bağlanmayı, yere yapışmayı, bir yerde kalmayı veya birinin yanından ayrılmamayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir şeye ya da kimseye yönelir, ona bağlanır ve onu benimser."},{"facet_id":"F002","role":"specialization","statement":"Yere yönelen şey, onun yüzeyine yapışıp kalabilir."},{"facet_id":"F003","role":"extension","statement":"Bir yerde bulunmayı sürdürmek ve oradan ayrılmamak anlatılabilir."},{"facet_id":"F004","role":"extension","statement":"Bir kimsenin yanında kalmak ve ondan ayrılmamak anlatılabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yere fiziksel yapışmayı, bir yerde kalmayı ve bir kimsenin yanından ayrılmamayı tek başına karşılamaz.","preserves":"Bir hedefe yönelme ve onunla ilişkiyi sürdürme yönünü taşır."},"text":"bağlanmak"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir kişiye ya da şeye yönelip onu benimseme, yere yapışma ve birine eşlik etme okumalarını kaybeder.","preserves":"Bir yerde kalma ve oradan ayrılmama yönünü korur."},"text":"yerleşmek"},{"category":"confusable","error_profile":{"adds":"İlişkiden bağımsız genel bir varlığını sürdürme anlamı getirir.","collision":"Birinci dalın kalıcılık anlamıyla karışır.","fit":"displacement","loses":"Bir hedefle kurulan yönelme, temas, yer veya kişi ilişkisini bütünüyle kaybeder.","preserves":"Ayrılmama ve bir durumda sürme çağrışımını kısmen taşır."},"text":"kalıcı olmak"}],"identity_rationale":"Yetkili ifade, tamamlayıcısına göre bir şeye yönelip onu benimseme, yere yapışma, bir yerde kalma ve bir kimsenin yanından ayrılmama okumalarını açıkça sıralar. Hazırlanan dal bu ilişkisel okumaları kalıcılık anlamıyla özdeşleştirmeden doğru bir arada tutar.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yere yapışmak veya ona bağlanmak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ona yönelmek ve ondan hoşnut olmak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"o yerde kalmak"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"arkadaşının yanından ayrılmamak"}],"lexicalization_note":"Tanım yalnız tamamlayıcılı yapılara bağlıdır; yönelme, yapışma, yerde kalma ve birine eşlik etme okumalarından bağımsız bir çıplak kök anlamı çıkarılmaz.","neighbor_coverage_note":"On iki adayın tümü değerlendirildi. Yönelme, yapışma ve yerde kalma sınırlarını en açık gösteren dört dış komşu ile kalıcılık dalı seçildi; öteki adaylar duygusal yönelme, konumsal sağlamlık veya biçim ortaklığı bakımından bu karşılaştırmaları yineledi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın alanı fiziksel yapışma ve beraber kalmaya kadar uzanır; komşu dal ise hedefe doğru duygusal eğilim ve onda huzur bulma merkezlidir.","focus_only":"Odak dal, yere yapışma, bir yerde oturma ve bir kimsenin yanından ayrılmama okumalarını da içerir.","gloss":"yönelip bağlanma / yönelip huzur bulma","neighbor_only":"Komşu dal, yönelmenin yanında sakinleşme, güven duyma ve bir hedefte karar kılmayı öne çıkarır.","neighbor_ref":"root_000596/B002","relation_type":"near_synonym","shared_zone":"İki dalda da kişi bir hedefe yönelir, ona eğilim gösterir ve yanında kalmaya yatkınlaşır."},{"boundary_match":"partial","distinction":"Odak dal ilişkisel yönelme ile kişi beraberliğine de açılır; komşu dalın çekirdeği konumunu terk etmeme ve yüzeye fiziksel olarak yapışmadır.","focus_only":"Odak dal, kişiye ya da şeye yönelip onu benimsemeyi ve bir kimseye eşlik etmeyi içerir.","gloss":"bağlanıp kalma / yere yapışıp yerleşme","neighbor_only":"Komşu dal, yerinden ayrılmayan kişi ile yere çöken kuş ve sağım kabının yapıştırılması gibi somut örnekleri kapsar.","neighbor_ref":"root_001340/B003","relation_type":"near_synonym","shared_zone":"Bir yerde kalma ve yere yapışma, iki dalın doğrudan örtüşen bölümüdür."},{"boundary_match":"partial","distinction":"Odak dalın kalması çoğu kez bir hedefe veya eşlik edilen kişiye bağlıdır; komşu dal doğrudan bulunulan yerde kalmayı ve sürmeyi anlatır.","focus_only":"Odak dal, bir hedefe yönelme, onu benimseme ve yere yapışma okumalarını taşır.","gloss":"yönelip kalma / bir yerde kalma","neighbor_only":"Komşu dal, bulutun kalması ve sürmesi gibi hedefe yönelme gerektirmeyen devamlılık örneklerini içerir.","neighbor_ref":"root_000155/B001","relation_type":"near_synonym","shared_zone":"Bir yerde bulunmayı sürdürme ve oradan ayrılmama iki dalda da vardır."},{"boundary_match":"partial","distinction":"Odak dal ilişkisel yönelim ve kalma durumunu anlatır; komşu dalda merkez, nesneler arasındaki fiziksel tutunma, asılma ya da takılmadır.","focus_only":"Odak dal, gönüllü yönelme, benimseme, bir yerde kalma ve bir kimseye eşlik etme içerir.","gloss":"yönelip bağlanma / takılıp asılma","neighbor_only":"Komşu dal, bir nesnenin başka bir şeye takılması, asılması veya orada sıkışması gibi somut bağlantıları kapsar.","neighbor_ref":"root_001039/B001","relation_type":"near_neighbor","shared_zone":"Bir şeye bağlanma ve ondan kolayca ayrılmama iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal bir hedefe veya yere bağlı ilişkisel bir yapıdır; komşu dal ise ilişkinin niteliğinden bağımsız kalıcılık ve durum devamlılığıdır.","focus_only":"Odak dal, tamamlayıcısıyla kurulan yönelme, yapışma, yerleşme veya eşlik ilişkisini gerektirir.","gloss":"bağlı kalma / kalıcı olma","neighbor_only":"Komşu dal, herhangi bir hedef ilişkisi olmadan varlığın uzun süre sürmesini ve durumunu korumasını bildirir.","neighbor_ref":"root_000429/B001","relation_type":"near_neighbor","shared_zone":"Ayrılmama ve sürme düşüncesi, iki dalın sınırında ortak bir çağrışım oluşturur."}],"source_phrase_ar":"أخلد إلى الأرض إذا لصق بها (maqayis;jamhara)؛ أخلد إلى كذا أي ركن إليه ورضي به (ayn)؛ أخلدت إلى فلان أي ركنت إليه (sihah)؛ أخلد بالمكان أقام به وأخلد بصاحبه لزمه (sihah)؛ ركن إليها ظانا أنه يخلد فيها (mufradat)","source_summary":"Ortak tanıklık, bir hedefe yönelip bağlanma çekirdeğini yere yapışma, bir yerde oturma ve bir kimsenin yanından ayrılmama biçimlerinde genişletir; her okuma kendi bağlı yapısıyla sınırlıdır.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه أخلد إلى الأرض أو إلى فلان أو إلى كذا بمعنى ركن ورضي ولصق، وأخلد بالمكان بمعنى أقام، وأخلد بصاحبه بمعنى لزمه.","what_is_not_ar":"لا يدخل فيه الخلود بمعنى دوام البقاء نفسه، ولا الخلد بمعنى البال أو الدويبة، ولا الزينة بالقرط أو السوار."},"support_links":["sup_b536e11f375c81d424b5"]},{"boundary":"Dalın merkezi küpe ve küpeyle süslenmedir; bilezikle süslenme yalnız tanıklıkta belirtilen yöresel değişkedir.","branch_kind":"bare","branch_ref":"root_000429/B003","candidate_links":[{"candidate_id":"cand_dcec01042f7f3fe6e960","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَخْلَدَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axolada|ROOT:xld|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:3:4:1","qac_word_ref":"104:3:4","surface_ar":"أَخْلَدَ"}],"gloss":"küpe; küpe veya bilezikle süslenmiş olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel nesne, kulağa takılan halka biçimli bir süs olan küpedir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi, kulağında küpe ya da benzeri bir kulak süsü taşıdığı için bu biçimle nitelenebilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yöresel değişkede niteleme, kişinin el bileziği takmış olmasına bağlanır."}}],"root_ar":"خ ل د","root_id":"root_000429","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Küpe nesnesi, küpe takmış kişi ve ayrıca belirtilen bilezikli yöresel değişke birlikte gösterileceğinde kullanılır.","boundary_detail":"Dalın merkezi küpe ve küpeyle süslenmedir; bilezikle süslenme yalnız tanıklıkta belirtilen yöresel değişkedir.","branch_image_ar":"زينة ملازمة للأذن أو اليد","concept_gloss":"küpe; küpe veya bilezikle süslenmiş olma","contextual_glosses":[{"applicability":"Bir kişinin kulağında küpe ya da benzeri bir kulak süsü taşıdığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Küpeyle süslenmiş kişi niteliğini doğrudan ve doğal biçimde taşır."},"facet_ids":["F001","F002"],"text":"küpeli","usage_role":"contextual"},{"applicability":"Yalnız el bileziği takmış kişiyi anlatan yöresel değişkenin kastedildiği bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yöresel tanıklıkta belirtilen el bileziğiyle süslenmiş olma niteliğini korur."},"facet_ids":["F003"],"text":"bilezikli","usage_role":"contextual"}],"definition":"Kulağa takılan küpeyi ve bu tür bir süsle bezenmiş olmayı anlatır. El bileziğiyle süslenme, ana küpe anlamına denk sayılmayan yöresel bir değişkedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel nesne, kulağa takılan halka biçimli bir süs olan küpedir."},{"facet_id":"F002","role":"extension","statement":"Bir kişi, kulağında küpe ya da benzeri bir kulak süsü taşıdığı için bu biçimle nitelenebilir."},{"facet_id":"F003","role":"source_variant","statement":"Yöresel değişkede niteleme, kişinin el bileziği takmış olmasına bağlanır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Süsle ilgisiz biçimde yaşamın sona ermemesi anlamını getirir.","collision":"Birinci dalın kalıcılık yorumuyla doğrudan karışır.","fit":"displacement","loses":"Küpe nesnesini, küpeyle süslenmiş kişiyi ve bilezikli yöresel değişkeyi bütünüyle kaybeder.","preserves":"Yalnız aynı türemiş biçimle bağlantıyı korur; süs anlamını korumaz."},"text":"ölümsüz"},{"category":"alternative","error_profile":{"adds":"Kolye, yüzük ve başka her türlü süs eşyasını da kapsama alır.","collision":null,"fit":"broadening","loses":"Küpeyi merkez alan kulak sınırını ve kişiyi küpeli niteleme yönünü belirsizleştirir.","preserves":"Bedene takılan bir süs nesnesi olma yönünü korur."},"text":"takı"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dalın temel küpe nesnesini ve küpeli kişi yorumunu dışarıda bırakır.","preserves":"Yöresel değişkede bulunan el süsü yönünü doğru biçimde taşır."},"text":"bilezik"}],"identity_rationale":"Yetkili ifade, temel süs nesnesini küpe olarak verir ve kişiyi küpeli ya da kulak süsü takmış sayan yorumu açıkça destekler; el bileziğiyle süslenme ise yöresel bir değişke olarak ayrıca belirtilir. Hazırlanan çerçeve, bu değişkeyi ana küpe anlamının yerine geçirmeden doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"küpe; bir tür kulak süsü"}],"lexicalization_note":"Tanım çıplak biçimdeki küpe adını merkez alır; kalıcılık, yönelme, düşünce veya küçük hayvan dallarından anlam aktarmaz.","neighbor_coverage_note":"On iki adayın tümü değerlendirildi. Aynı biçimin kalıcılık yorumuyla temel karışması, en yakın küpe ve genel süs alanları, bilezik değişkesi ve takılı-takısız karşıtlığı seçildi; kalan adaylar daha uzak süs türleri ya da yalnız biçim ortaklığı sundu.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dalda biçim bedene takılan süsle açıklanır; komşu dalda ise süs bulunmaz ve aynı biçim süreklilik ya da değişmeden kalma bakımından yorumlanır.","focus_only":"Odak dal, küpeyi ve küpe ya da bilezik takmış kişiyi bildirir.","gloss":"süslenmiş olma / kalıcı olma","neighbor_only":"Komşu dal, uzun süre varlığını sürdürmeyi ve aynı durumda kalmayı bildirir.","neighbor_ref":"root_000429/B001","relation_type":"other","shared_zone":"Aynı türemiş biçim, sözlük tanıklıklarında iki ayrı yorumun taşıyıcısı olarak görünür."},{"boundary_match":"partial","distinction":"Odak dal küpeyi kişi üzerindeki süs niteliğine bağlar; komşu dal halka biçimini küpenin ötesindeki nesnelere ve izlere de yayar.","focus_only":"Odak dal, küpe takmış kişiyi ve yöresel olarak bilezikli kişiyi nitelemeye kadar uzanır.","gloss":"küpe / küçük süs halkası","neighbor_only":"Komşu dal, küçük halkadan zırh halkalarına ve halka biçimli yara izine kadar daha geniş nesne benzerlikleri içerir.","neighbor_ref":"root_000403/B003","relation_type":"near_synonym","shared_zone":"Kulağa takılan küçük halka biçimli süs, iki dalın doğrudan örtüşen çekirdeğidir."},{"boundary_match":"field_only","distinction":"Odak dal belirli bir kulak süsünü merkez alır; komşu dal nesne türünü sınırlamadan süs eşyası ve süslenme alanını bütünüyle kapsar.","focus_only":"Odak dal, özellikle küpeyi ve onu takmış kişiyi, ayrıca sınırlı bir bilezik değişkesini bildirir.","gloss":"küpe / genel süs eşyası","neighbor_only":"Komşu dal, kadın süslerini, kılıç süsünü ve genel olarak süs takınmayı kapsayan geniş bir alandır.","neighbor_ref":"root_000353/B001","relation_type":"same_field","shared_zone":"İki dal da bedene ya da bir nesneye takılan süs eşyaları alanında yer alır."},{"boundary_match":"partial","distinction":"Odak dal bileziği ikincil bir süslenmiş kişi yorumunda tutar; komşu dalın merkezi doğrudan bileğe takılan süs nesnesidir.","focus_only":"Odak dalın ana nesnesi küpedir ve bilezik yalnız yöresel kişi nitelemesinde görünür.","gloss":"küpe ve bilezikli olma / bilezik","neighbor_only":"Komşu dal, bilekte taşınan ve belirli maddelerden yapılabilen bileziği doğrudan nesne olarak adlandırır.","neighbor_ref":"root_001424/B006","relation_type":"near_neighbor","shared_zone":"El bileziği, odak dalın yöresel değişkesi ile komşu dalın nesne anlamında ortaklaşır."},{"boundary_match":"opposed","distinction":"Odak dal süsün varlığıyla kişiyi niteler; komşu dal aynı eksende süsün yokluğunu veya çıkarılmış olmasını bildirir.","focus_only":"Odak dal, küpe veya başka belirtilmiş süsün bedende bulunmasını bildirir.","gloss":"takıyla süslü / takısız","neighbor_only":"Komşu dal, boyun ve süs yerlerinin takıdan yoksun olmasını ya da takının çıkarılmasını bildirir.","neighbor_ref":"root_001027/B002","relation_type":"polarity_pair","shared_zone":"İki dal, bedende süs eşyasının bulunup bulunmaması eksenini paylaşır."}],"source_phrase_ar":"ولدان مخلدون مقرطون (ayn;mufradat)؛ من الخلد والخلد جمع خلدة وهي القرط (maqayis)؛ مقرطون مشنفون (maqayis)؛ مسورون لغة يمانية (jamhara)","source_summary":"Tanıklıkların ortak yüzeyi küpe ve küpe takmış kişi yorumudur; kulak süsü için eşdeğer açıklamalar verilirken, el bileziğiyle süslenme yöresel bir değişke olarak ayrılır.","sources":["MQ","AY","JA","MU"],"what_is_ar":"يدخل فيه تفسير مخلدون بالمقرطين أو المشنفين أو المسورين، وربطه بالخلدة بمعنى القرط.","what_is_not_ar":"لا يدخل فيه تفسير مخلدون بأنهم باقون لا يموتون أو مبقون بحالتهم، ولا معاني الركون أو البال أو الدويبة."},"support_links":["sup_7997df843d843a7107ae"]},{"boundary":"Dal bedensel organı değil zihinsel alanı ve orada beliren düşünceyi anlatır; kalıcılık anlamı yalnız adlandırmanın dayanağıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000429/B004","candidate_links":[{"candidate_id":"cand_02f464379c2a0a55c3f9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَخْلَدَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axolada|ROOT:xld|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:3:4:1","qac_word_ref":"104:3:4","surface_ar":"أَخْلَدَ"}],"gloss":"akıl ve akla gelen düşünce","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Akıl, düşüncenin insanın içinde yerleştiği ve korunduğu zihinsel alandır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu ad, zihinde yer eden ve orada sabit kalan düşüncenin kendisini de karşılar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bağlı kullanım, bir düşüncenin kişinin aklına gelmesini anlatır."}}],"root_ar":"خ ل د","root_id":"root_000429","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Zihinsel alan, orada yer eden içerik ve bu alana bir düşüncenin gelmesi birlikte özetleneceğinde uygundur.","boundary_detail":"Dal bedensel organı değil zihinsel alanı ve orada beliren düşünceyi anlatır; kalıcılık anlamı yalnız adlandırmanın dayanağıdır.","branch_image_ar":"بال مستقر في القلب","concept_gloss":"akıl ve akla gelen düşünce","contextual_glosses":[{"applicability":"Çıplak adın zihinde korunan düşünce içeriğini anlattığı bağlamlarda açıklayıcı bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Düşüncenin insanın içinde yerleşmesi ve orada sabit kalması yönlerini taşır."},"facet_ids":["F001","F002"],"text":"akılda yer eden düşünce","usage_role":"explanatory"},{"applicability":"Bir düşüncenin kişinin zihninde belirmesini bildiren bağlı kullanımın doğal Türkçe karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir şeyin kişinin zihinsel alanına gelmesi ve orada belirmesi yönünü korur."},"facet_ids":["F003"],"text":"aklıma geldi","usage_role":"contextual"}],"definition":"İnsanın içinde düşüncenin yerleşip korunduğu zihinsel alanı ya da orada bulunan düşünceyi anlatır. Bağlı kullanımda bir şeyin akla gelmesini bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Akıl, düşüncenin insanın içinde yerleştiği ve korunduğu zihinsel alandır."},{"facet_id":"F002","role":"specialization","statement":"Bu ad, zihinde yer eden ve orada sabit kalan düşüncenin kendisini de karşılar."},{"facet_id":"F003","role":"associated_use","statement":"Bağlı kullanım, bir düşüncenin kişinin aklına gelmesini anlatır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Duygu, istek, sevgi ve eğilim gibi bu dalda zorunlu olmayan duygusal anlamları getirir.","collision":null,"fit":"broadening","loses":"Düşüncenin zihinde belirmesi ve akıl alanında yer etmesi sınırını açıkça vermez.","preserves":"İnsanın iç dünyasını ve orada taşınan bir içeriği çağrıştırır."},"text":"gönül"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel akıl alanını ve yeni bir düşüncenin akla gelmesi kullanımını kaybeder.","preserves":"Zihinde bulunan ve korunabilen bir düşünce içeriğini taşır."},"text":"anı"},{"category":"confusable","error_profile":{"adds":"Zihinsel alanla sınırlı olmayan genel süreklilik anlamını getirir.","collision":"Birinci dalın varlığını sürdürme anlamıyla karışır.","fit":"displacement","loses":"Akıl alanını, düşüncenin kendisini ve bir şeyin akla gelmesi kullanımını kaybeder.","preserves":"Düşüncenin içeride sabit kalmasıyla kurulan açıklayıcı bağı korur."},"text":"kalıcılık"}],"identity_rationale":"Yetkili ifade, çıplak adı insanın iç dünyasındaki akıl ve düşünce alanı olarak tanımlar, adlandırmayı düşüncenin orada yerleşip sabit kalmasına bağlar ve bağlı kullanımda bir şeyin akla gelmesini açıklar. Hazırlanan çerçeve bu iki yüzeyi birbirine karıştırmadan korur.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"akıl; zihinde yer eden düşünce"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"aklıma geldi"}],"lexicalization_note":"Çıplak biçimdeki akıl ve yerleşmiş düşünce anlamı ile bir düşüncenin akla gelmesini bildiren bağlı kullanım ayrı tutulur.","neighbor_coverage_note":"On iki adayın tümü karşılaştırıldı. Akıl ve iç düşünce alanını paylaşan iki yakın komşu, gizleme ve zihinde yineleme süreçleri ile genel kalıcılık dalı seçildi; kalan adaylar şaşkınlık, bozulma veya yalnız biçim ortaklığı nedeniyle daha uzak kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal zihinsel yerleşme ve akla gelme çevresinde kalır; komşu dal bu alanı duygusal ilgi, kaygı ve önemsemeye doğru genişletir.","focus_only":"Odak dal, düşüncenin içeride yerleşip sabit kalmasını ve bir şeyin akla gelmesini belirginleştirir.","gloss":"akılda yer eden düşünce / iç dünya ve önemseme","neighbor_only":"Komşu dal, iç dünya ve aklın yanında önemseme, kaygılanma ve ilgilenme anlamlarına da uzanır.","neighbor_ref":"root_000165/B003","relation_type":"near_synonym","shared_zone":"Akıl, iç dünya ve orada beliren düşünce iki dalın doğrudan ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dalın ayırıcı yanı düşüncenin içeride yerleşip sabit kalmasıdır; komşu dal aynı alanı kavrayış ve dışarıdan içe bırakılan düşünce yönlerine açar.","focus_only":"Odak dal, düşüncenin zihinde sabit bir yer edinmesini adlandırmanın gerekçesi yapar.","gloss":"akıl ve yerleşmiş düşünce / akıl ve içe doğuş","neighbor_only":"Komşu dal, akıl ve kavrayışın yanında kişinin içine düşünce bırakılması yorumunu da içerir.","neighbor_ref":"root_000612/B002","relation_type":"near_synonym","shared_zone":"İnsanın akıl ve iç düşünce alanı ile oraya bir şeyin gelmesi iki dalda da bulunur."},{"boundary_match":"partial","distinction":"Odak dal içeriğin zihinsel konumunu ve akla gelişini anlatır; komşu dalda esas olan içeriği gizlemek ve dışarı vurmamaktır.","focus_only":"Odak dal, düşüncenin yerleştiği akıl alanını ve bir düşüncenin orada belirmesini anlatır.","gloss":"akılda bulunma / içte saklama","neighbor_only":"Komşu dal, bilinen veya düşünülen bir şeyi göğüste saklama ve başkasına açmama eylemini bildirir.","neighbor_ref":"root_001324/B002","relation_type":"near_neighbor","shared_zone":"Bir içeriğin insanın içinde, zihninde ya da göğsünde bulunması ortak alandır."},{"boundary_match":"partial","distinction":"Odak dal bir zihinsel alan veya içerik durumudur; komşu dal ise bu içerik üzerinde yinelenen etkin bir düşünme ve hatırlama işlemidir.","focus_only":"Odak dal, akıl alanının veya orada bulunan düşüncenin kendisini adlandırır.","gloss":"zihindeki düşünce / düşünceyi zihinde yineleme","neighbor_only":"Komşu dal, sözü zihinde tekrar tekrar çevirme ve hatırlamak için işleme sürecini bildirir.","neighbor_ref":"root_000562/B006","relation_type":"near_neighbor","shared_zone":"Düşüncenin zihinde bulunması ve korunması, iki dalın ortak zeminidir."},{"boundary_match":"partial","distinction":"Odak dal, sabitliği düşüncenin akıldaki konumuna dönüştürür; komşu dal ise her tür varlığın sürekliliğini ve korunmuş durumunu bildirir.","focus_only":"Odak dal, düşüncenin yerleştiği akıl alanına ve orada beliren içeriğe özgüdür.","gloss":"akılda yer etme / kalıcı olma","neighbor_only":"Komşu dal, zihinsel alanla sınırlanmadan varlıkların uzun süre kalmasını ve durumunu korumasını anlatır.","neighbor_ref":"root_000429/B001","relation_type":"near_neighbor","shared_zone":"İçeride sabit kalma düşüncesi, zihinsel dal ile genel kalıcılık dalını birbirine yaklaştırır."}],"source_phrase_ar":"الخلد البال وسمي بذلك لأنه مستقر في القلب ثابت (maqayis)؛ ما يقع ذلك في خلدي (ayn)؛ وقع ذلك في خلدي أي في قلبي (jamhara)؛ وقع ذلك في خلدي أي في ورعي وقلبي (sihah)","source_summary":"Tanıklıklar, aklı düşüncenin içeride yerleştiği alan olarak ortaklaştırır; düşüncenin orada sabit kalması adlandırmayı açıklar ve bağlı kullanım bu alana bir düşüncenin gelmesini bildirir.","sources":["MQ","AY","JA","SI"],"what_is_ar":"يدخل فيه الخلد بمعنى البال، وما يقع في الخلد أي في القلب أو الروع.","what_is_not_ar":"لا يدخل فيه دوام البقاء، ولا الركون، ولا القرط، ولا الدويبة."},"support_links":["sup_007498efdaabcfdfe43a"]},{"boundary":"Dal genel olarak bütün fareleri değil, kör veya gözsüz olduğu belirtilen faremsi küçük hayvanı adlandırır.","branch_kind":"bare","branch_ref":"root_000429/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْلَدَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axolada|ROOT:xld|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:3:4:1","qac_word_ref":"104:3:4","surface_ar":"أَخْلَدَ"}],"gloss":"gözsüz faremsi küçük hayvan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hayvanın gözleri yoktur ya da hayvan görme yetisinden yoksundur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Küçük hayvan, görünüş ve tür alanı bakımından fareye ya da sıçana benzetilir."}}],"root_ar":"خ ل د","root_id":"root_000429","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Körlük veya gözlerin bulunmaması ile fare ya da sıçan benzerliğinin birlikte korunduğu genel karşılıktır.","boundary_detail":"Dal genel olarak bütün fareleri değil, kör veya gözsüz olduğu belirtilen faremsi küçük hayvanı adlandırır.","branch_image_ar":"دويبة عمياء تشبه الجرذ","concept_gloss":"gözsüz faremsi küçük hayvan","contextual_glosses":[{"applicability":"Hayvanın sıçanlar içinde bir tür ve görme yetisinden yoksun olarak anlatıldığı bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sıçan türü olma ile körlük özelliklerini eksiksiz biçimde korur."},"facet_ids":["F001","F002"],"text":"kör bir sıçan türü","usage_role":"contextual"}],"definition":"Gözleri bulunmayan ya da görmeyen, fareye veya sıçana benzeyen küçük bir yer hayvanıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hayvanın gözleri yoktur ya da hayvan görme yetisinden yoksundur."},{"facet_id":"F002","role":"specialization","statement":"Küçük hayvan, görünüş ve tür alanı bakımından fareye ya da sıçana benzetilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Belirli bir çağdaş hayvan türü ve onun kazma davranışı gibi kanıtlanmamış özellikler getirir.","collision":"Açıklamayı kanıtın vermediği kesin bir tür adı sanılmasına yol açar.","fit":"displacement","loses":"Tanıklığın fare ve sıçan alanındaki açık sınıflandırmasını kesin olarak göstermez.","preserves":"Kör ve faremsi küçük yer hayvanı görünümünü kısmen çağrıştırır."},"text":"köstebek"},{"category":"alternative","error_profile":{"adds":"Gören farelerin tamamını da kapsayan çok daha geniş bir hayvan alanı getirir.","collision":null,"fit":"broadening","loses":"Körlük veya gözlerin hiç bulunmaması biçimindeki ayırıcı özelliği kaybeder.","preserves":"Hayvanın fareye benzeyen görünüşünü ve küçük oluşunu taşır."},"text":"fare"}],"identity_rationale":"Yetkili ifade, bu adı gözleri bulunmayan ya da görmeyen bir sıçan türü ve fareye benzeyen küçük bir yer hayvanı olarak ortaklaştırır. Hazırlanan çerçeve belirli bir çağdaş türü kanıtsız biçimde dayatmadan körlük ile fare ya da sıçan benzerliğini birlikte korur.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"gözleri olmayan, fareye veya sıçana benzeyen küçük hayvan"}],"lexicalization_note":"Tanım çıplak biçimin kör, faremsi küçük hayvan anlamıyla sınırlıdır; kökün kalıcılık, yönelme, süs ve düşünce dalları buraya taşınmaz.","neighbor_coverage_note":"On iki adayın tümü değerlendirildi. Fare ve sıçan alanındaki iki en yakın komşu, geniş küçük yer hayvanları sınıfı ve aynı biçimi taşıyan iki kardeş dal seçildi; kalan hayvan adayları farklı türler veya yalnız uzak bir canlılık alanı sundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ayırıcı sınırı körlük ve faremsi görünümdür; komşu dal bu nitelikleri zorunlu kılmadan yalnız sıçan adını bildirir.","focus_only":"Odak dal, hayvanın kör ya da gözsüz ve fareye benzer olduğunu açıkça belirtir.","gloss":"kör faremsi hayvan / sıçan","neighbor_only":"Komşu dal, körlük veya görünüş sınırı koymadan doğrudan bir sıçan adını verir.","neighbor_ref":"root_000596/B005","relation_type":"near_synonym","shared_zone":"İki dal da sıçan ya da fare alanındaki küçük bir hayvanı adlandırır."},{"boundary_match":"partial","distinction":"Odak dal körlüğü zorunlu ayırt edici özellik yapar; komşu dal cinsiyet ya da genel sıçan adı üzerinden sınıflar ve görme durumunu sınırlamaz.","focus_only":"Odak dal, gözleri olmayan ya da görmeyen özel bir faremsi hayvanı belirtir.","gloss":"kör faremsi tür / sıçan ya da erkek fare","neighbor_only":"Komşu dal, körlük belirtmeden sıçanı veya erkek fareyi adlandırır.","neighbor_ref":"root_001025/B008","relation_type":"near_synonym","shared_zone":"Fare ve sıçan alanındaki hayvan adlandırması iki dalda doğrudan örtüşür."},{"boundary_match":"field_only","distinction":"Odak dal körlük ve fare benzerliğiyle belirlenmiş tekil bir tür alanıdır; komşu dal kirpi ve başka küçük canlılara kadar uzanan toplu bir sınıftır.","focus_only":"Odak dal, kör ve fareye ya da sıçana benzeyen tek bir küçük hayvan türünü sınırlar.","gloss":"kör faremsi hayvan / küçük yer hayvanları","neighbor_only":"Komşu dal, çeşitli küçük yer hayvanlarını topluca kapsayan geniş bir sınıf adıdır.","neighbor_ref":"root_000324/B004","relation_type":"same_field","shared_zone":"İki dal da yerde yaşayan küçük hayvanların genel alanında bulunur."},{"boundary_match":"field_only","distinction":"Bu dal somut bir küçük hayvanı adlandırır; komşu dal ise bütünüyle zihinsel bir alan ve düşünce içeriğidir, aralarında anlam aktarımı yoktur.","focus_only":"Odak dal, kör ve faremsi küçük bir hayvanı adlandırır.","gloss":"kör faremsi hayvan / akıl ve düşünce","neighbor_only":"Komşu dal, insanın akıl alanını, orada bulunan düşünceyi ve bir şeyin akla gelmesini anlatır.","neighbor_ref":"root_000429/B004","relation_type":"other","shared_zone":"Aynı çıplak biçim sözlük tanıklıklarında iki bağımsız anlamın adı olarak kullanılır."},{"boundary_match":"field_only","distinction":"Odak dal bir hayvan adıdır; komşu dal süreklilik ve korunmuş durum kavramıdır, ortak biçim dışında kavramsal örtüşme bulunmaz.","focus_only":"Odak dal, gözsüz ve fareye benzeyen küçük hayvanla sınırlıdır.","gloss":"kör faremsi hayvan / kalıcılık","neighbor_only":"Komşu dal, varlığını uzun süre sürdürme ve aynı durumda kalma anlamını taşır.","neighbor_ref":"root_000429/B001","relation_type":"other","shared_zone":"İki bağımsız anlam, aynı kökün ayrı sözlük dalları olarak yan yana bulunur."}],"source_phrase_ar":"الخلد ضرب من الجرذان عمي لم يخلق لها عيون (ayn)؛ الخلد دويبة تشبه الفأرة (jamhara)؛ ضرب من الجرذان أعمى (sihah)","source_summary":"Tanıklıklar küçük hayvanı fare ya da sıçan alanına yerleştirir ve körlüğünü ayırıcı özellik olarak verir; kimi ifade gözlerin hiç yaratılmadığını özellikle belirtir.","sources":["AY","JA","SI"],"what_is_ar":"يدخل فيه الخلد اسما لدويبة أو ضرب من الجرذان العمي التي تشبه الفأرة.","what_is_not_ar":"لا يدخل فيه البقاء أو الجنة أو الركون أو القرط أو البال."},"support_links":[]},{"boundary":"Dal yalnızca para ya da birikmiş değer değildir; varlığın kendisini, edinilmesini, artmasını, varlıklı duruma geçişi ve başkasına varlık kazandırmayı ayırarak kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001457/B001","candidate_links":[{"candidate_id":"cand_677c82ef547a34a7806a","lane":"micro"},{"candidate_id":"cand_93f1eda88186c0d94ece","lane":"micro"},{"candidate_id":"cand_51b1d1fc565bc4fd7ac4","lane":"micro"},{"candidate_id":"cand_dcec01042f7f3fe6e960","lane":"micro"},{"candidate_id":"cand_02f464379c2a0a55c3f9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"104:3:3:1","qac_word_ref":"104:3:3","surface_ar":"مَالَ"}],"gloss":"varlık; edinme, çoğalma ve başkasına kazandırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin sahip olduğu ve değer taşıyan varlıkların bütünü bu dalın ad çekirdeğini oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Göçebe toplulukların varlığına ilişkin belirli kullanımda bu varlık, hayvan sürüleriyle somutlaşır."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişinin kendisi için değerli varlık edinmesi ve onu kalıcı sahiplik konusu yapması eylem çekirdeğidir."}},{"facet_id":"F004","role":"core","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kişinin varlığının çoğalması ya da onun varlık sahibi bir duruma geçmesi ayrı bir süreç görünümüdür."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Bir başkasına değerli varlık vererek onu varlık sahibi duruma getirmek, çekirdeğin ettirgen uzantısıdır."}},{"facet_id":"F006","role":"associated_use","source_fields":["distinctive_facets[F006]"],"statements":{"statement":"Bir kimsenin varlığının çokluğuna şaşma bildiren söyleyiş, artış ve bolluk görünümüne bağlı bir kullanımdır."}}],"root_ar":"م و ل","root_id":"root_001457","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın sahip olunan varlık, onu edinme, varlıklı duruma gelme ve başkasını varlık sahibi kılma çekirdeklerini birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Dal yalnızca para ya da birikmiş değer değildir; varlığın kendisini, edinilmesini, artmasını, varlıklı duruma geçişi ve başkasına varlık kazandırmayı ayırarak kapsar.","branch_image_ar":"اتخاذ المال وكثرته","concept_gloss":"varlık; edinme, çoğalma ve başkasına kazandırma","contextual_glosses":[{"applicability":"Bir kişinin elindeki değer taşıyan şeylerin bütünü ya da bunların çoğulu ad olarak anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Edinme, çoğalma, varlıklı duruma gelme ve başkasına varlık kazandırma süreçlerini karşılamaz.","preserves":"Dalın kişiye ait değerli varlıklar bildiren ad çekirdeğini korur."},"facet_ids":["F001"],"text":"sahip olunan değerli varlıklar","usage_role":"general"},{"applicability":"Kişinin değerli bir şeyi kendisi için edinip sahipliğinde tutması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Varlık adını, varlığın kendiliğinden artmasını ve başkasına varlık kazandırmayı dışarıda bırakır.","preserves":"Kendisi için varlık edinme ve onu kalıcı sahiplik konusu yapma sürecini korur."},"facet_ids":["F003"],"text":"kendine kalıcı varlık edinmek","usage_role":"contextual"},{"applicability":"Bir kişinin sahip olduklarının artması ya da kişinin varlık sahibi hale gelmesi anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Varlığın ad çekirdeğini, bilinçli edinmeyi ve başkasını varlık sahibi kılmayı karşılamaz.","preserves":"Varlık artışını ve kişinin varlıklı duruma geçişini açıkça korur."},"facet_ids":["F004"],"text":"varlığı çoğalmak veya varlıklı duruma gelmek","usage_role":"contextual"},{"applicability":"Bir kişinin başkasına değerli varlık vererek onun sahiplik durumunu değiştirmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Varlığın kendisini, kişinin kendisi için edinmesini ve kendi varlığının artmasını karşılamaz.","preserves":"Başkasına varlık kazandıran ettirgen katılımcı değişimini korur."},"facet_ids":["F005"],"text":"birini varlık sahibi yapmak","usage_role":"contextual"}],"definition":"Kişinin sahip olduğu değerli varlıkların bütünü ile bunları edinme, çoğaltma ya da bunlara sahip duruma gelme alanıdır. Ayrıca başkasını varlık sahibi kılmayı kapsar; göçebe topluluklara özgü kullanımda sahip olunan varlık özellikle hayvan sürüleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin sahip olduğu ve değer taşıyan varlıkların bütünü bu dalın ad çekirdeğini oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Göçebe toplulukların varlığına ilişkin belirli kullanımda bu varlık, hayvan sürüleriyle somutlaşır."},{"facet_id":"F003","role":"core","statement":"Kişinin kendisi için değerli varlık edinmesi ve onu kalıcı sahiplik konusu yapması eylem çekirdeğidir."},{"facet_id":"F004","role":"core","statement":"Kişinin varlığının çoğalması ya da onun varlık sahibi bir duruma geçmesi ayrı bir süreç görünümüdür."},{"facet_id":"F005","role":"extension","statement":"Bir başkasına değerli varlık vererek onu varlık sahibi duruma getirmek, çekirdeğin ettirgen uzantısıdır."},{"facet_id":"F006","role":"associated_use","statement":"Bir kimsenin varlığının çokluğuna şaşma bildiren söyleyiş, artış ve bolluk görünümüne bağlı bir kullanımdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Dalın bütün sahip olunan varlıkları kapsayan alanını yalnızca ödeme aracına indirger.","fit":"narrowing","loses":"Nakit dışındaki varlıkları, hayvan sürüsü özelleşmesini ve edinme, artma, varlıklılaşma ile kazandırma süreçlerini siler.","preserves":"Değer taşıyan ve sahip olunabilen bir şey düşüncesinin yalnızca nakit yönünü korur."},"text":"para"}],"identity_rationale":"Kaynak ifadesi, sahip olunan değerli varlıkları ve bunların çoğulunu; kişinin kendisi için varlık edinmesini, varlığının çoğalmasını ya da varlıklı duruma gelmesini ve başkasını varlık sahibi kılmasını birlikte aktarır. Göçebe toplulukların varlığının hayvan sürüleriyle somutlaşması bu çekirdeğin bağlama bağlı bir özelleşmesidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kişinin sahip olduğu değerli varlık"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kişinin sahip olduğu değerli varlıklar"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"göçebe toplulukların başlıca varlığı sayılan hayvan sürüleri"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"varlık sahibi veya çok varlıklı kimse"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kendine kalıcı varlık edinmek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"varlığı çoğalmak veya varlık sahibi duruma gelmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birini varlık sahibi yapmak veya ona değerli varlık vermek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"mal sözcüğünün küçültme biçimi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ne çok varlığı var!"}],"lexicalization_note":"Tanım, genel varlık ve varlık edinme çekirdeğini ayrı tutar; göçebe toplulukların hayvan sürülerini varlık sayan kullanımını yalnızca belirli bir söz öbeğine bağlı özelleşme olarak sınırlar.","neighbor_coverage_note":"Sekiz adayın tümü karşılaştırıldı. Edinme ve varlık artışıyla doğrudan sınır paylaşan üç aday yayımlandı; para yönetimi, belirli varlık türleri, geçim ve sürü adlandırmalarıyla yalnızca uzak alan ortaklığı kuran ötekiler dal sınırını keskinleştirmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın edinme görünümü komşuya yaklaşır, fakat odak daha geniş bir sahip olunan varlık ve varlıklılaşma ailesidir. Komşu ise edinimin amacı ve saklama biçimiyle sınırlı, daha özel bir sahiplik türünü belirtir.","focus_only":"Odak dal, sahip olunan varlığın adını, varlığın artmasını, varlıklı duruma gelmeyi ve başkasını varlık sahibi kılmayı da kapsar.","gloss":"kendisi için edinilen ve saklanan varlık","neighbor_only":"Komşu dal, kişinin kendisi için satış ve ticaret amacı dışında edindiği, gereksinim sonrasında sakladığı ya da temel dayanak yaptığı varlığa özgü koşullar taşır.","neighbor_ref":"root_001265/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin kendisi için değerli varlık edinmesi ve bunu sahipliğinde tutması alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşunun çekirdeği belirli bir mülk ve taşınmaz türüne yönelirken odak dal varlığın türünü sınırlandırmaz; ayrıca artış, varlıklı duruma geçiş ve ettirgen kazandırma anlamlarını içerir.","focus_only":"Odak dal taşınır ya da taşınmaz ayrımı yapmadan varlığı, varlık artışını ve başkasına varlık kazandırmayı kapsar.","gloss":"taşınmaz edinme ve elde tutma","neighbor_only":"Komşu dal özellikle taşınmazı, gelir getiren yeri ve bunları edinip kalıcı sahiplik konusu yapmayı öne çıkarır.","neighbor_ref":"root_001034/B004","relation_type":"near_synonym","shared_zone":"İki dal, değer taşıyan bir şeyi edinme ve kalıcı sahiplik altında bulundurma düşüncesinde birleşir."},{"boundary_match":"partial","distinction":"Örtüşme varlık artışıyla sınırlıdır. Odak dal sahiplik ve edinme ailesini kurarken komşu, büyüyen varlık ile onun bakımı ve artışına ilişkin değerlendirmeleri ayrı bir çekirdek yapar.","focus_only":"Odak dal varlığın genel adını, edinilmesini ve başkasının varlık sahibi yapılmasını da içerir.","gloss":"artan varlık ve onu iyi yönetme","neighbor_only":"Komşu dal büyüyen ya da çok olan varlığı, onun iyi yönetilmesini ve artması yönündeki iyi dileği özellikle öne çıkarır.","neighbor_ref":"root_000205/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da sahip olunan varlığın çokluğu veya artışı belirgin bir ortak alandır."}],"source_phrase_ar":"تمول الرجل اتخذ مالا؛ مال يمال كثر ماله (maqayis)؛ المال معروف وجمعه أموال؛ كانت أموال العرب أنعامهم؛ رجل مال أي ذو مال والفعل تمول (ayn)؛ مال الرجل يمول ويمال إذا صار ذا مال؛ تمول مثله؛ موله غيره (sihah)؛ مال أهل البادية النعم؛ تمول فلان مالا إذا اتخذ قنية من المال؛ ما أموله أي ما أكثر ماله (tahdhib)","source_summary":"Kaynakların toplu anlatımı, sahip olunan değerli varlıkları ve bunların çoğulunu temel alır; varlık edinme, varlığın çoğalması, varlıklı duruma gelme ve başkasını varlık sahibi kılma süreçlerini bu temel çevresinde birleştirir. Hayvan sürüleri göçebe topluluklara özgü somutlaşma, çokluk karşısındaki şaşma söyleyişi ise bağlı bir kullanım olarak aktarılır. Mal adının küçültme biçimi de ayrıca kaydedilir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه المال والأموال واتخاذ المال قنية وكثرة المال وصيرورة الرجل ذا مال وتمويل غيره ونعم أهل البادية","what_is_not_ar":"ليس للمولة العنكبوت ولا للميل عن الوسط ولا لميل الحائط"},"support_links":["sup_007498efdaabcfdfe43a","sup_4a78d971a33817b4ceb0","sup_7997df843d843a7107ae","sup_a5d14fa88a405c5daf3c","sup_b536e11f375c81d424b5"]},{"boundary":"Dal, örümceğin özelliklerini tanımlamaz; yalnızca örümcek için aktarılan ve güvenilirliği açıkça tartışılan bir adlandırmayı temsil eder.","branch_kind":"unresolved","branch_ref":"root_001457/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"104:3:3:1","qac_word_ref":"104:3:3","surface_ar":"مَالَ"}],"gloss":"örümcek için tartışmalı bir ad","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcük, bazı sözlük aktarımlarında örümceği gösteren bir hayvan adı olarak verilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırmanın doğruluğu ve güvenilir aktarımı açıkça sorgulandığı için bu gönderim kesin kabul edilemez."}}],"root_ar":"م و ل","root_id":"root_001457","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözcüğün örümceğe gönderimi aktarılırken bu adlandırmanın güvenilirliğine ilişkin açık kuşkunun da korunması gereken her durumda uygundur.","boundary_detail":"Dal, örümceğin özelliklerini tanımlamaz; yalnızca örümcek için aktarılan ve güvenilirliği açıkça tartışılan bir adlandırmayı temsil eder.","branch_image_ar":"المُولة العنكبوت","concept_gloss":"örümcek için tartışmalı bir ad","contextual_glosses":[{"applicability":"Tartışmalı hayvan adının bir metinde doğrudan canlıya gönderim yaptığı bağlamda akıcı karşılık olarak kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bu adlandırmanın güvenilirliği ve yerleşikliği üzerindeki açık kaynak kuşkusunu görünmez kılar.","preserves":"Adlandırmanın gönderimde bulunduğu hayvanı doğru biçimde korur."},"facet_ids":["F001"],"text":"örümcek","usage_role":"contextual"}],"definition":"Örümceğe verilen bir ad olarak aktarılır; ancak bu adlandırmanın güvenilirliği kaynak anlatımının kendi içinde açıkça tartışmalıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcük, bazı sözlük aktarımlarında örümceği gösteren bir hayvan adı olarak verilir."},{"facet_id":"F002","role":"source_variant","statement":"Adlandırmanın doğruluğu ve güvenilir aktarımı açıkça sorgulandığı için bu gönderim kesin kabul edilemez."}],"identity_rationale":"Kaynak ifadesi sözcüğü örümceğe verilen bir ad olarak aktarır, fakat aynı ifadenin içinde bu aktarımın kuşkuyla karşılandığını ve güvenilir bir aktarıcıdan işitilmediğini de açıkça bildirir. Bu nedenle hayvanla kurulan bağ korunabilir, ancak yerleşik ve tartışmasız bir ad gibi sunulamaz.","lexicalization_note":"Kanıt, bu tartışmalı adlandırmanın bağımsız ve yerleşik bir yalın sözlük birimi olup olmadığını mekanik olarak çözmez; tanım bu yüzden yalın kullanım varsaymaz.","neighbor_coverage_note":"Dokuz adayın tümü değerlendirildi. Aynı canlıya yönelen iki adlandırma gerçek bir sınır karşılaştırması sağladı; öteki hayvan adları yalnızca geniş canlılar alanını paylaştı, varlık dalı ise ortak köke rağmen anlamsal örtüşme göstermedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Gönderim ortak olsa da odak dalın sözlüksel kimliği kuşkulu bir ad aktarımına bağlıdır. Komşu dal ise canlının doğrudan adını ve onu tanıtan özellikleri kapsadığı için iki adın kullanım sınırları tam olarak eşleşmez.","focus_only":"Odak dal, aynı canlıya yönelen fakat güvenilirliği açıkça tartışılan özel bir ad aktarımıdır.","gloss":"ağ ören örümcek","neighbor_only":"Komşu dal canlının olağan adını, ağ örme niteliğini, ad çeşitlerini ve dil bilgisel biçimlerini kapsar.","neighbor_ref":"root_001054/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın hayvansal gönderimi aynı canlıya, yani örümceğe yönelir."},{"boundary_match":"partial","distinction":"Odak dal yalnızca kuşkulu hayvan adı aktarımıyla sınırlıdır; komşu dalın kendi ayrı adı ve yuvayı gösteren bağlı kullanımı vardır. Bu ek kapsam ve odaktaki güvenilirlik çekincesi tam eşdeğerliği engeller.","focus_only":"Odak dalın örümcek adı sayılması kaynak anlatımında açık kuşku ve güven sorunu taşır.","gloss":"örümcek ve yuvası için özel ad","neighbor_only":"Komşu dal başka bir örümcek adının yanı sıra o örümceğin yuvasını gösteren bağlı bir söz öbeğini de kapsar.","neighbor_ref":"root_001326/B008","relation_type":"near_synonym","shared_zone":"İki dal da örümceğe verilen alışılmadık bir adlandırma üzerinden aynı canlıya gönderimde bulunur."}],"source_phrase_ar":"إن المولة العنكبوت وفيه نظر (maqayis)؛ المولة اسم العنكبوت (ayn)؛ زعم قوم أن المول العنكبوت الواحدة مولة ولم أسمعه عن ثقة (sihah)؛ هي العنكبوت والمولة (tahdhib)","source_summary":"Toplu kaynak kaydı sözcüğü örümceğin adı olarak aktarır, fakat aynı kayıtta bu eşleştirmenin kuşkulu olduğu ve güvenilir bir kaynaktan işitilmediği yönünde açık çekinceler bulunur. Bu yüzden hayvana gönderim ile aktarımın belirsizliği birlikte korunmalıdır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه إطلاق المولة أو المول على العنكبوت إذا ثبتت النسبة","what_is_not_ar":"ليس للمال والأموال ولا لاتخاذ القنية ولا لكثرة المال"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["104:3:1"],"branch_refs":[],"candidate_id":"cand_6512df64666140083b9d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"104:3:1:boundary-diagnosis","source_type":"word_analysis","support_ids":["sup_47f0e4b15b0fcd941e66","sup_6a76e0075892c4ca8ffa"],"title":"action shifts into diagnosis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:1","qac_refs":["104:3:1:1"],"status":"accepted"}},{"anchor_refs":["104:3:1"],"branch_refs":[],"candidate_id":"cand_1b85ad2761d1c4068b09","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"104:3:1:counting-becomes-misreckoning","source_type":"word_analysis","support_ids":["sup_47f0e4b15b0fcd941e66","sup_c0922d283336e821e42b"],"title":"counting turns into false reckoning","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:1","qac_refs":["104:3:1:1"],"status":"accepted"}},{"anchor_refs":["104:3:1"],"branch_refs":[],"candidate_id":"cand_868076437e56f42f92b8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"104:3:1:false-reckoning-field","source_type":"word_analysis","support_ids":["sup_3a0d738fd54ec1be5472","sup_47f0e4b15b0fcd941e66"],"title":"a known false-estimate verb is localized","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:1","qac_refs":["104:3:1:1"],"status":"accepted"}},{"anchor_refs":["104:3:1"],"branch_refs":[],"candidate_id":"cand_7abf60dbf4ae308cab55","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"104:3:1:false-sufficiency","source_type":"word_analysis","support_ids":["sup_47f0e4b15b0fcd941e66","sup_56909273dab03c1ac04b"],"title":"wealth is treated as enough","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:1","qac_refs":["104:3:1:1"],"status":"accepted"}},{"anchor_refs":["104:3:1"],"branch_refs":[],"candidate_id":"cand_3b81264b8dbd49280ed8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"104:3:1:habitual-completed-mismatch","source_type":"word_analysis","support_ids":["sup_3ecf1919fa413f05bd90","sup_47f0e4b15b0fcd941e66"],"title":"ongoing belief asserts a finished result","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:1","qac_refs":["104:3:1:1"],"status":"accepted"}},{"anchor_refs":["104:3:1"],"branch_refs":[],"candidate_id":"cand_109b77f8dd0fb3191562","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"104:3:1:prior-actor-carried","source_type":"word_analysis","support_ids":["sup_47f0e4b15b0fcd941e66","sup_6d6b1c64e2d20dac0872"],"title":"the same actor continues silently","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:1","qac_refs":["104:3:1:1"],"status":"accepted"}},{"anchor_refs":["104:3:1"],"branch_refs":[],"candidate_id":"cand_1ff2b86ecad1ffcfd428","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"104:3:1:proposition-object","source_type":"word_analysis","support_ids":["sup_3708291f25d9bbee1623","sup_47f0e4b15b0fcd941e66"],"title":"the whole claim is reckoned","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:1","qac_refs":["104:3:1:1"],"status":"accepted"}},{"anchor_refs":["104:3:1"],"branch_refs":[],"candidate_id":"cand_68fe6f96c806a3e31d96","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"104:3:1:true-permanence-contrast","source_type":"word_analysis","support_ids":["sup_47f0e4b15b0fcd941e66","sup_9b669dd3e258cd5f040a"],"title":"permanence vocabulary is inverted","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:1","qac_refs":["104:3:1:1"],"status":"accepted"}},{"anchor_refs":["104:3:1"],"branch_refs":[],"candidate_id":"cand_11d60b44f1596df6ec16","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"104:3:1:variant-and-sound","source_type":"word_analysis","support_ids":["sup_30ac45764fdc1e2f30de","sup_47f0e4b15b0fcd941e66"],"title":"vowel variation leaves the frame intact","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:1","qac_refs":["104:3:1:1"],"status":"accepted"}},{"anchor_refs":["104:3:2"],"branch_refs":[],"candidate_id":"cand_7542f35cf0494bb5f070","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:3:2:embedded-object-clause","source_type":"word_analysis","support_ids":["sup_52080d0dd56766ae5a34","sup_7d6dbcb8a658f0418f20"],"title":"the particle embeds the whole claim","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:2","qac_refs":["104:3:2:1"],"status":"accepted"}},{"anchor_refs":["104:3:2"],"branch_refs":[],"candidate_id":"cand_e8fcd6e795b6dd7d2488","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:3:2:heavy-form-closed-proposition","source_type":"word_analysis","support_ids":["sup_52080d0dd56766ae5a34","sup_7420a3dbae41ff722246"],"title":"heavy form seals the noun clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:2","qac_refs":["104:3:2:1"],"status":"accepted"}},{"anchor_refs":["104:3:2"],"branch_refs":[],"candidate_id":"cand_94986fa248e5fb79cc9b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:3:2:reported-certainty","source_type":"word_analysis","support_ids":["sup_52080d0dd56766ae5a34","sup_90681193ac52cb9d9917"],"title":"certainty is reported, not endorsed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:2","qac_refs":["104:3:2:1"],"status":"accepted"}},{"anchor_refs":["104:3:3"],"branch_refs":[],"candidate_id":"cand_47487850873e07b2b53f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"104:3:3:concrete-and-inclining-wealth","source_type":"word_analysis","support_ids":["sup_4888699fa3609f1cd3e4","sup_adba9979dad79338e9c0"],"title":"concrete property carries attraction pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:3","qac_refs":["104:3:3:1","104:3:3:2"],"status":"accepted"}},{"anchor_refs":["104:3:3"],"branch_refs":[],"candidate_id":"cand_3263ba4d59d2e79bfdcf","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"104:3:3:embedded-subject-agent","source_type":"word_analysis","support_ids":["sup_0e27fbd3ae3227692ff3","sup_adba9979dad79338e9c0"],"title":"wealth becomes the acting subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:3","qac_refs":["104:3:3:1","104:3:3:2"],"status":"accepted"}},{"anchor_refs":["104:3:3"],"branch_refs":[],"candidate_id":"cand_abec2dba5029b50f390a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"104:3:3:garden-owner-parallel","source_type":"word_analysis","support_ids":["sup_868ad5439b1b341b56a1","sup_adba9979dad79338e9c0"],"title":"wealth-superiority parallel is secondary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:3","qac_refs":["104:3:3:1","104:3:3:2"],"status":"accepted"}},{"anchor_refs":["104:3:3"],"branch_refs":[],"candidate_id":"cand_7c43d0029d8ab85e04a9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"104:3:3:non-availing-contrast","source_type":"word_analysis","support_ids":["sup_4a4409c6e89726ed9677","sup_adba9979dad79338e9c0"],"title":"another possessed wealth fails","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:3","qac_refs":["104:3:3:1","104:3:3:2"],"status":"accepted"}},{"anchor_refs":["104:3:3"],"branch_refs":[],"candidate_id":"cand_5e5ed595b98834b205aa","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"104:3:3:owner-owned-reversal","source_type":"word_analysis","support_ids":["sup_97eb2b99335b40a7c486","sup_adba9979dad79338e9c0"],"title":"the suffix loop reverses agency","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:3","qac_refs":["104:3:3:1","104:3:3:2"],"status":"accepted"}},{"anchor_refs":["104:3:3"],"branch_refs":[],"candidate_id":"cand_0ea079cbf42f08da111a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"104:3:3:possessed-definite-return","source_type":"word_analysis","support_ids":["sup_adba9979dad79338e9c0","sup_ce03306215ab8743aeb7"],"title":"gathered wealth returns as his","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:3","qac_refs":["104:3:3:1","104:3:3:2"],"status":"accepted"}},{"anchor_refs":["104:3:3"],"branch_refs":[],"candidate_id":"cand_ff0eb6a06dbd7f7e9248","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"104:3:3:singular-owned-mass","source_type":"word_analysis","support_ids":["sup_adba9979dad79338e9c0","sup_f000fd34b6f62c97f424"],"title":"wealth is consolidated as one possession","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:3","qac_refs":["104:3:3:1","104:3:3:2"],"status":"accepted"}},{"anchor_refs":["104:3:3"],"branch_refs":[],"candidate_id":"cand_64b82e0e91a74e792ec3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"104:3:3:sound-bound-governance","source_type":"word_analysis","support_ids":["sup_adba9979dad79338e9c0","sup_cfdad1b2c518e353a386"],"title":"sound marks the clause bond","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:3","qac_refs":["104:3:3:1","104:3:3:2"],"status":"accepted"}},{"anchor_refs":["104:3:3"],"branch_refs":[],"candidate_id":"cand_a1721a0702ed4066bd2e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"104:3:3:wealth-reckoning-permanence-pairing","source_type":"word_analysis","support_ids":["sup_adba9979dad79338e9c0","sup_d5092b6fca394192be5c"],"title":"wealth feeds the permanence calculation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:3","qac_refs":["104:3:3:1","104:3:3:2"],"status":"accepted"}},{"anchor_refs":["104:3:4"],"branch_refs":[],"candidate_id":"cand_eca2a3ff85b5e8033d5d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000429"],"scope":"focus_ayah","source_local_id":"104:3:4:causative-wealth-agent","source_type":"word_analysis","support_ids":["sup_a1e334e6c0cb82c69ab1","sup_a436e8d9cbc8598722bc"],"title":"wealth is made the cause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:4","qac_refs":["104:3:4:1","104:3:4:2"],"status":"accepted"}},{"anchor_refs":["104:3:4"],"branch_refs":[],"candidate_id":"cand_7c700746652e191612a8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000429"],"scope":"focus_ayah","source_local_id":"104:3:4:direct-object-not-prepositional","source_type":"word_analysis","support_ids":["sup_2976fded63fa9bc9722f","sup_a1e334e6c0cb82c69ab1"],"title":"clinging contrast is compressed, not governing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:4","qac_refs":["104:3:4:1","104:3:4:2"],"status":"accepted"}},{"anchor_refs":["104:3:4"],"branch_refs":[],"candidate_id":"cand_ad71ac44f5ef61e454fb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000429"],"scope":"focus_ayah","source_local_id":"104:3:4:final-and-forward-reversal","source_type":"word_analysis","support_ids":["sup_80578ffa56794bd7bd7d","sup_a1e334e6c0cb82c69ab1"],"title":"the landing word sets up rejection","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:4","qac_refs":["104:3:4:1","104:3:4:2"],"status":"accepted"}},{"anchor_refs":["104:3:4"],"branch_refs":[],"candidate_id":"cand_9f2cf9b2cee58a35eabe","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000429"],"scope":"focus_ayah","source_local_id":"104:3:4:form-iv-not-form-ii","source_type":"word_analysis","support_ids":["sup_5c733cd0235562f20e94","sup_a1e334e6c0cb82c69ab1"],"title":"single causation, not intensive perpetuation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:4","qac_refs":["104:3:4:1","104:3:4:2"],"status":"accepted"}},{"anchor_refs":["104:3:4"],"branch_refs":[],"candidate_id":"cand_328b25aabdf3d6f4d3e8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000429"],"scope":"focus_ayah","source_local_id":"104:3:4:owner-as-object-loop","source_type":"word_analysis","support_ids":["sup_a1e334e6c0cb82c69ab1","sup_b30b415b548fc19279af"],"title":"the owner receives the action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:4","qac_refs":["104:3:4:1","104:3:4:2"],"status":"accepted"}},{"anchor_refs":["104:3:4"],"branch_refs":[],"candidate_id":"cand_279326051692bff951d7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000429"],"scope":"focus_ayah","source_local_id":"104:3:4:perfect-under-imperfect","source_type":"word_analysis","support_ids":["sup_a1e334e6c0cb82c69ab1","sup_d684c9521485e5abaeb4"],"title":"the impossible result is treated as done","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:4","qac_refs":["104:3:4:1","104:3:4:2"],"status":"accepted"}},{"anchor_refs":["104:3:4"],"branch_refs":[],"candidate_id":"cand_400a48d9828337686c06","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000429"],"scope":"focus_ayah","source_local_id":"104:3:4:permanence-clinging-irony","source_type":"word_analysis","support_ids":["sup_6755d233815e87283a81","sup_a1e334e6c0cb82c69ab1"],"title":"permanence is shadowed by earthward attachment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:4","qac_refs":["104:3:4:1","104:3:4:2"],"status":"accepted"}},{"anchor_refs":["104:3:4"],"branch_refs":[],"candidate_id":"cand_860bb09beb120ae5a64d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000429"],"scope":"focus_ayah","source_local_id":"104:3:4:rare-finite-event-claim","source_type":"word_analysis","support_ids":["sup_3976fb1ba7004e6941ef","sup_a1e334e6c0cb82c69ab1"],"title":"eternity becomes an event claim","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:4","qac_refs":["104:3:4:1","104:3:4:2"],"status":"accepted"}},{"anchor_refs":["104:3:4"],"branch_refs":[],"candidate_id":"cand_c924b8e36433ab07d01a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000429"],"scope":"focus_ayah","source_local_id":"104:3:4:root-field-irony","source_type":"word_analysis","support_ids":["sup_08224eb4bdec9f84bcdb","sup_a1e334e6c0cb82c69ab1"],"title":"the root field darkens permanence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:4","qac_refs":["104:3:4:1","104:3:4:2"],"status":"accepted"}},{"anchor_refs":["104:3:4"],"branch_refs":[],"candidate_id":"cand_065784c82ea0f7f74374","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000429"],"scope":"focus_ayah","source_local_id":"104:3:4:sound-weight-and-loop","source_type":"word_analysis","support_ids":["sup_7517c4d7fe70c5841552","sup_a1e334e6c0cb82c69ab1"],"title":"the closure sounds heavy and looped","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:4","qac_refs":["104:3:4:1","104:3:4:2"],"status":"accepted"}},{"anchor_refs":["104:3:1"],"branch_refs":[],"candidate_id":"cand_fc77823ed35156419ea7","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"104:3:1:1","source_type":"qac_morpheme","support_ids":["sup_b59085336ea020dfe94a"],"title":"QAC root occurrence: ح س ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["104:3:3"],"branch_refs":[],"candidate_id":"cand_f204571afe38c1f697fd","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"104:3:3:1","source_type":"qac_morpheme","support_ids":["sup_4e60c38eb76af52e2971"],"title":"QAC root occurrence: م و ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["104:3:4"],"branch_refs":[],"candidate_id":"cand_b58b3142376ce98dcf8b","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000429"],"scope":"focus_ayah","source_local_id":"104:3:4:1","source_type":"qac_morpheme","support_ids":["sup_4d49bd0f281c9f793ef0"],"title":"QAC root occurrence: خ ل د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["104:3:4"],"branch_refs":[],"candidate_id":"cand_df2ddd578a22ecf6b75b","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000429"],"scope":"focus_ayah","source_local_id":"104:3:4:remote-burrowing-image","source_type":"word_analysis","support_ids":["sup_07357e51bc6d35973b21","sup_a1e334e6c0cb82c69ab1"],"title":"remote image not locally needed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:3:4","qac_refs":["104:3:4:1","104:3:4:2"],"status":"accepted"}},{"anchor_refs":["104:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:3","branch_refs":["root_000318/B002","root_000429/B001","root_001457/B001"],"candidate_id":"cand_677c82ef547a34a7806a","commentary_obligation":"review","hft_ref":"hft_608ee91138ba97b131c6","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_supposed_causal_permanence","source_type":"hft","support_ids":["sup_a5d14fa88a405c5daf3c"],"title":"b_supposed_causal_permanence","trust":"legacy_unbound"},{"anchor_refs":["104:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:3","branch_refs":["root_000318/B001","root_000429/B001","root_001457/B001"],"candidate_id":"cand_93f1eda88186c0d94ece","commentary_obligation":"review","hft_ref":"hft_3473b74836c5fec31912","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_quantity_converted_to_duration","source_type":"hft","support_ids":["sup_4a78d971a33817b4ceb0"],"title":"b_quantity_converted_to_duration","trust":"legacy_unbound"},{"anchor_refs":["104:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:3","branch_refs":["root_000318/B003","root_000318/B008","root_000429/B002","root_001457/B001"],"candidate_id":"cand_51b1d1fc565bc4fd7ac4","commentary_obligation":"review","hft_ref":"hft_3a5aaaa65ba619d9676e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_wealth_as_prop_for_clinging","source_type":"hft","support_ids":["sup_b536e11f375c81d424b5"],"title":"b_wealth_as_prop_for_clinging","trust":"legacy_unbound"},{"anchor_refs":["104:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:3","branch_refs":["root_000318/B004","root_000429/B003","root_001457/B001"],"candidate_id":"cand_dcec01042f7f3fe6e960","commentary_obligation":"review","hft_ref":"hft_aa5fb03c5c6eb54db5f5","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_wealth_as_fixed_status_insignia","source_type":"hft","support_ids":["sup_7997df843d843a7107ae"],"title":"b_wealth_as_fixed_status_insignia","trust":"legacy_unbound"},{"anchor_refs":["104:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:3","branch_refs":["root_000318/B002","root_000429/B004","root_001457/B001"],"candidate_id":"cand_02f464379c2a0a55c3f9","commentary_obligation":"review","hft_ref":"hft_bdaaf084e31592badc74","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_immortality_as_settled_inner_thought","source_type":"hft","support_ids":["sup_007498efdaabcfdfe43a"],"title":"b_immortality_as_settled_inner_thought","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ","qac_morphemes":[{"lemma_ar":"حَسِبَ","morph_features":"STEM|POS:V|IMPF|LEM:Hasiba|ROOT:Hsb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:3:1:1","qac_word_ref":"104:3:1","root_ar":"ح س ب","surface_ar":"يَحْسَبُ"},{"lemma_ar":"أَنّ","morph_features":"STEM|POS:ACC|LEM:>an~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"104:3:2:1","qac_word_ref":"104:3:2","root_ar":"","surface_ar":"أَنَّ"},{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"104:3:3:1","qac_word_ref":"104:3:3","root_ar":"م و ل","surface_ar":"مَالَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"104:3:3:2","qac_word_ref":"104:3:3","root_ar":"","surface_ar":"هُۥٓ"},{"lemma_ar":"أَخْلَدَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axolada|ROOT:xld|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:3:4:1","qac_word_ref":"104:3:4","root_ar":"خ ل د","surface_ar":"أَخْلَدَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"104:3:4:2","qac_word_ref":"104:3:4","root_ar":"","surface_ar":"هُۥ"}],"word_analysis_qac_refs":[["104:3:1:1"],["104:3:2:1"],["104:3:3:1","104:3:3:2"],["104:3:4:1","104:3:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["104:3:1","104:3:2","104:3:3","104:3:4"]},"focus_surface_evidence":{"arabic_uthmani":"يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ","qac_morphemes":[{"lemma_ar":"حَسِبَ","morph_features":"STEM|POS:V|IMPF|LEM:Hasiba|ROOT:Hsb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:3:1:1","qac_word_ref":"104:3:1","root_ar":"ح س ب","surface_ar":"يَحْسَبُ"},{"lemma_ar":"أَنّ","morph_features":"STEM|POS:ACC|LEM:>an~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"104:3:2:1","qac_word_ref":"104:3:2","root_ar":"","surface_ar":"أَنَّ"},{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"104:3:3:1","qac_word_ref":"104:3:3","root_ar":"م و ل","surface_ar":"مَالَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"104:3:3:2","qac_word_ref":"104:3:3","root_ar":"","surface_ar":"هُۥٓ"},{"lemma_ar":"أَخْلَدَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>axolada|ROOT:xld|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:3:4:1","qac_word_ref":"104:3:4","root_ar":"خ ل د","surface_ar":"أَخْلَدَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"104:3:4:2","qac_word_ref":"104:3:4","root_ar":"","surface_ar":"هُۥ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["104:3:1:1"],["104:3:2:1"],["104:3:3:1","104:3:3:2"],["104:3:4:1","104:3:4:2"]],"word_analysis_refs":["104:3:1","104:3:2","104:3:3","104:3:4"],"word_rows":[{"analysis_record_ref":"104:3:1","analytic_gloss_range_en":"supposes, reckons, or miscalculates; here a cognition verb governing the full embedded proposition","analytic_root_gloss_range_en":"counting, reckoning, supposing, sufficiency, and related branches; the local frame selects supposing/misreckoning while letting counting and false sufficiency press on the reading","qac_refs":["104:3:1:1"],"root":{"arabic":"ح س ب","transliteration":"ḥ-s-b"},"surface":{"arabic":"يَحْسَبُ","transliteration":"yaḥsabu"}},{"analysis_record_ref":"104:3:2","analytic_gloss_range_en":"heavy emphatic complementizer introducing the proposition reckoned by the main verb","analytic_root_gloss_range_en":null,"qac_refs":["104:3:2:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"أَنَّ","transliteration":"anna"}},{"analysis_record_ref":"104:3:3","analytic_gloss_range_en":"his wealth, concrete owned property now functioning as the embedded subject of the causative predicate","analytic_root_gloss_range_en":"wealth, property, capital, and owned resources; local possession narrows the range to the subject's accumulated wealth while some inclining pressure remains only as a qualified lexical color","qac_refs":["104:3:3:1","104:3:3:2"],"root":{"arabic":"م و ل","transliteration":"m-w-l"},"surface":{"arabic":"مَالَهُۥٓ","transliteration":"mālahū"}},{"analysis_record_ref":"104:3:4","analytic_gloss_range_en":"made him permanent or caused him to be treated as enduring; locally a Form IV perfect causative with wealth as subject and the owner as object","analytic_root_gloss_range_en":"permanence, enduring, being made lasting, and the Form IV earthward-clinging frame; local direct-object grammar selects causative immortalizing while allowing the 7:176 clinging contrast as a narrowed echo","qac_refs":["104:3:4:1","104:3:4:2"],"root":{"arabic":"خ ل د","transliteration":"kh-l-d"},"surface":{"arabic":"أَخْلَدَهُۥ","transliteration":"akhladahū"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["104:3"],"branch_refs":["root_000318/B002","root_000429/B001","root_001457/B001"],"candidate_id":"cand_677c82ef547a34a7806a","evidence_scope":"focus_ayah","hft_ref":"hft_608ee91138ba97b131c6","item_id":"b_supposed_causal_permanence","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_supposed_causal_permanence","support_id":"sup_a5d14fa88a405c5daf3c"},{"anchor_refs":["104:3"],"branch_refs":["root_000318/B001","root_000429/B001","root_001457/B001"],"candidate_id":"cand_93f1eda88186c0d94ece","evidence_scope":"focus_ayah","hft_ref":"hft_3473b74836c5fec31912","item_id":"b_quantity_converted_to_duration","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_quantity_converted_to_duration","support_id":"sup_4a78d971a33817b4ceb0"},{"anchor_refs":["104:3"],"branch_refs":["root_000318/B003","root_000318/B008","root_000429/B002","root_001457/B001"],"candidate_id":"cand_51b1d1fc565bc4fd7ac4","evidence_scope":"focus_ayah","hft_ref":"hft_3a5aaaa65ba619d9676e","item_id":"b_wealth_as_prop_for_clinging","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_wealth_as_prop_for_clinging","support_id":"sup_b536e11f375c81d424b5"},{"anchor_refs":["104:3"],"branch_refs":["root_000318/B004","root_000429/B003","root_001457/B001"],"candidate_id":"cand_dcec01042f7f3fe6e960","evidence_scope":"focus_ayah","hft_ref":"hft_aa5fb03c5c6eb54db5f5","item_id":"b_wealth_as_fixed_status_insignia","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_wealth_as_fixed_status_insignia","support_id":"sup_7997df843d843a7107ae"},{"anchor_refs":["104:3"],"branch_refs":["root_000318/B002","root_000429/B004","root_001457/B001"],"candidate_id":"cand_02f464379c2a0a55c3f9","evidence_scope":"focus_ayah","hft_ref":"hft_bdaaf084e31592badc74","item_id":"b_immortality_as_settled_inner_thought","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_immortality_as_settled_inner_thought","support_id":"sup_007498efdaabcfdfe43a"}],"diagnostics":[],"lane_counts":{"global":10,"macro":13,"micro":5},"packet_summary":{"ayah_count":9,"focus_ref":"104:3","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"و ص د","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000036","furuq_root_norm":"ء ص د","furuq_source_root_norm":"أ ص د","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001653","furuq_root_norm":"و ص د","furuq_source_root_norm":"و ص د","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:8","104:9"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"104:3","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":18,"unstructured_record_count":0},"identity":{"ayah_ref":"104:3","lane":"micro","linguistic_source_ref":"104:3","surface_ref":"104:3","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"104:3","target_tokens":[["Malının",["104:3:3"]],["kendisini",["104:3:4"]],["ölümsüz",["104:3:4"]],["kıldığını",["104:3:2","104:3:4"]],["sanır",["104:3:1"]]],"text":"Malının kendisini ölümsüz kıldığını sanır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":9,"id":"s104-p01-001-009","label":"Whole surah","number":1,"refs":["104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:8","104:9"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:4:remote-burrowing-image","source_type":"word_analysis","support_id":"sup_07357e51bc6d35973b21","text":"{\"blocking_evidence\":null,\"headline\":\"remote image not locally needed\",\"reader_payoff\":null,\"reason\":\"The local surface is a Form IV perfect verb with direct object, so this remote noun-image branch would overfill the prose without changing the local lexical judgment.\",\"representative_source_ids\":[\"QS-58dd8deb\"],\"status\":\"dropped_filler\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:4:root-field-irony","source_type":"word_analysis","support_id":"sup_08224eb4bdec9f84bcdb","text":"{\"blocking_evidence\":null,\"headline\":\"the root field darkens permanence\",\"reader_payoff\":\"The reader notices that eternity, settled inward thought, and remaining-behind pressures make the claimed permanence feel like confinement rather than triumph.\",\"reason\":\"V4 includes permanence, inward thought, and clinging or remaining fields for {{ar:خ ل د}} ({{tr:kh-l-d}}); these remain lexical pressures, not replacements for the local Form IV direct-object sense.\",\"representative_source_ids\":[\"QS-0fc27173\",\"QS-97627597\",\"QE-be5792a8\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:3:embedded-subject-agent","source_type":"word_analysis","support_id":"sup_0e27fbd3ae3227692ff3","text":"{\"blocking_evidence\":null,\"headline\":\"wealth becomes the acting subject\",\"reader_payoff\":\"The reader notices that {{ar:مَالَهُۥٓ}} ({{tr:mālahū}}) is not the object of reckoning but the subject of the false causal predicate.\",\"reason\":\"Attachment evidence identifies {{ar:مَالَهُۥٓ}} ({{tr:mālahū}}) as the governed ism of {{ar:أَنَّ}} ({{tr:anna}}) and as the explicit subject of {{ar:أَخْلَدَهُۥ}} ({{tr:akhladahū}}).\",\"representative_source_ids\":[\"QG-c34bd5d5\",\"QG-ee7a199c\",\"QG-ff43796e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:4:direct-object-not-prepositional","source_type":"word_analysis","support_id":"sup_2976fded63fa9bc9722f","text":"{\"blocking_evidence\":null,\"headline\":\"clinging contrast is compressed, not governing\",\"reader_payoff\":\"The reader notices the contrast with {{ar:أَخْلَدَ إِلَى}} ({{tr:akhlada ilā}}) at 7:176, while the local direct object keeps this as a causative claim imposed on the owner.\",\"reason\":\"V4 supports the {{ar:أَخْلَدَ إِلَى}} ({{tr:akhlada ilā}}) clinging frame, but the local word lacks {{ar:إِلَى}} ({{tr:ilā}}) and takes a direct object suffix, so the echo is narrowed to contrast rather than local valency.\",\"representative_source_ids\":[\"QG-0ca6758e\",\"QG-98933248\",\"QI-2be32586\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:1:variant-and-sound","source_type":"word_analysis","support_id":"sup_30ac45764fdc1e2f30de","text":"{\"blocking_evidence\":null,\"headline\":\"vowel variation leaves the frame intact\",\"reader_payoff\":\"The reader notices that the accepted {{ar:يَحْسِبُ}} ({{tr:yaḥsibu}}) variant changes recitational color while preserving the same root, consonantal texture, and syntactic misreckoning.\",\"reason\":\"The variant affects the medial vowel but not the consonantal root or the governing clausal-complement frame.\",\"representative_source_ids\":[\"QF-4276b041\",\"QP-08689860\",\"QP-a50717c4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:1:proposition-object","source_type":"word_analysis","support_id":"sup_3708291f25d9bbee1623","text":"{\"blocking_evidence\":null,\"headline\":\"the whole claim is reckoned\",\"reader_payoff\":\"The reader notices that the object of reckoning is the full proposition, not wealth alone, so the ayah exposes a complete false explanation.\",\"reason\":\"Attachment evidence marks {{ar:أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ}} ({{tr:anna mālahū akhladahū}}) as the clausal complement governed by {{ar:يَحْسَبُ}} ({{tr:yaḥsabu}}).\",\"representative_source_ids\":[\"QG-99afdac8\",\"QS-86ac643b\",\"QT-3bdcf601\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:4:rare-finite-event-claim","source_type":"word_analysis","support_id":"sup_3976fb1ba7004e6941ef","text":"{\"blocking_evidence\":null,\"headline\":\"eternity becomes an event claim\",\"reader_payoff\":\"The reader notices that permanence is cast as a finite caused event attributed to wealth, not as ordinary participial eternity language.\",\"reason\":\"The contextual profile marks this exact form as low-occurrence, and the CRITICAL distribution contrasts it with more common nominal or participial eternity forms.\",\"representative_source_ids\":[\"QI-09f4d837\",\"QH-d3760c87\",\"QH-fd033bf7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:1:false-reckoning-field","source_type":"word_analysis","support_id":"sup_3a0d738fd54ec1be5472","text":"{\"blocking_evidence\":null,\"headline\":\"a known false-estimate verb is localized\",\"reader_payoff\":\"The reader notices that the verb frames the immortality claim as unreliable estimation rather than knowledge.\",\"reason\":\"V4 includes supposition or non-certain judgment for {{ar:ح س ب}} ({{tr:ḥ-s-b}}), and the local attachment keeps the permanence proposition under the cognition verb rather than asserting it as fact.\",\"representative_source_ids\":[\"QS-c0d3d938\",\"QI-1d868920\",\"QE-f6140aa1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:1:habitual-completed-mismatch","source_type":"word_analysis","support_id":"sup_3ecf1919fa413f05bd90","text":"{\"blocking_evidence\":null,\"headline\":\"ongoing belief asserts a finished result\",\"reader_payoff\":\"The reader notices the temporal irony: the man keeps supposing that wealth has already secured him.\",\"reason\":\"The main verb is a bare imperfect while the embedded predicate {{ar:أَخْلَدَهُۥ}} ({{tr:akhladahū}}) is perfect, supporting a habitual supposition about a claimed completed effect.\",\"representative_source_ids\":[\"QG-b6e2ae3c\",\"QF-49e92820\",\"QB-b4249edf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:1","source_type":"word_analysis","support_id":"sup_47f0e4b15b0fcd941e66","text":"{\"gloss_range\":\"supposes, reckons, or miscalculates; here a cognition verb governing the full embedded proposition\",\"prose\":\"{{ar:يَحْسَبُ}} ({{tr:yaḥsabu}}) opens the ayah by moving from the prior acts of collecting and counting into an inner diagnosis. Its 3ms imperfect form carries the same man from 104:2 without renaming him, so the reader feels the hoarder pass directly from external accumulation into habitual reckoning. The verb does not take {{ar:مَالَهُۥٓ}} ({{tr:mālahū}}) as a simple object; it governs the whole {{ar:أَنَّ}} ({{tr:anna}}) proposition, making the error a complete claim about wealth causing permanence. The root's counting and supposing ranges converge here: counted wealth becomes a false calculation, and the sufficiency branch sharpens the mistake because wealth is treated as what will be enough against death. The bare imperfect keeps this as an ongoing state, while the embedded perfect {{ar:أَخْلَدَهُۥ}} ({{tr:akhladahū}}) presents the imagined result as already accomplished. The accepted {{ar:يَحْسِبُ}} ({{tr:yaḥsibu}}) vowel variant changes the medial sound color while the ḥāʾ-and-sīn texture remains breathy and tight, so the recitational variation does not loosen the misreckoning frame. Against the true permanence language cited at 76:19, the same broad permanence field is inverted here into a wealth-based estimate rather than an actual enduring state.\",\"root_display\":\"{{ar:ح س ب}} ({{tr:ḥ-s-b}})\",\"root_gloss_range\":\"counting, reckoning, supposing, sufficiency, and related branches; the local frame selects supposing/misreckoning while letting counting and false sufficiency press on the reading\",\"surface_display\":\"{{ar:يَحْسَبُ}} ({{tr:yaḥsabu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:3:concrete-and-inclining-wealth","source_type":"word_analysis","support_id":"sup_4888699fa3609f1cd3e4","text":"{\"blocking_evidence\":null,\"headline\":\"concrete property carries attraction pressure\",\"reader_payoff\":\"The reader notices that the delusion is grounded in concrete owned resources, with the inclining image adding attraction pressure without replacing the local wealth sense.\",\"reason\":\"V4 supports the wealth/property range for {{ar:مَال}} ({{tr:māl}}); the inclining association survives as qualified lexical pressure from the CRITICAL row family, not as the selected local gloss.\",\"representative_source_ids\":[\"QS-1a917edf\",\"QS-6d7cf52b\",\"QS-d17d45ea\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:3:non-availing-contrast","source_type":"word_analysis","support_id":"sup_4a4409c6e89726ed9677","text":"{\"blocking_evidence\":null,\"headline\":\"another possessed wealth fails\",\"reader_payoff\":\"The reader notices the contrast with {{ar:مَالُهُ}} ({{tr:māluhu}}) at 111:2, where possessed wealth does not avail its owner.\",\"reason\":\"The cited recurrence gives a valid cross-surah contrast, while the local role remains the embedded subject of the false causal claim.\",\"representative_source_ids\":[\"QI-feb6a359\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"104:3:4:1","source_type":"qac_morpheme","support_id":"sup_4d49bd0f281c9f793ef0","text":"{\"lemma_ar\":\"أَخْلَدَ\",\"morph_features\":\"STEM|POS:V|PERF|(IV)|LEM:>axolada|ROOT:xld|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"104:3:4:1\",\"qac_word_ref\":\"104:3:4\",\"root_ar\":\"خ ل د\",\"surface_ar\":\"أَخْلَدَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"104:3:3:1","source_type":"qac_morpheme","support_id":"sup_4e60c38eb76af52e2971","text":"{\"lemma_ar\":\"مَال\",\"morph_features\":\"STEM|POS:N|LEM:maAl|ROOT:mwl|M|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"104:3:3:1\",\"qac_word_ref\":\"104:3:3\",\"root_ar\":\"م و ل\",\"surface_ar\":\"مَالَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:2","source_type":"word_analysis","support_id":"sup_52080d0dd56766ae5a34","text":"{\"gloss_range\":\"heavy emphatic complementizer introducing the proposition reckoned by the main verb\",\"prose\":\"{{ar:أَنَّ}} ({{tr:anna}}) is the hinge where the ayah turns from the act of supposing into the content of that supposition. It governs {{ar:مَالَهُۥٓ}} ({{tr:mālahū}}) as its ism and lets the embedded clause feel assertive from inside the man's belief, while the whole clause remains dependent on {{ar:يَحْسَبُ}} ({{tr:yaḥsabu}}). That balance is the payoff: the claim sounds firm in his mind but is not endorsed by the syntax. The heavy, geminated form also blocks a light {{ar:أَنْ}} ({{tr:an}}) reparse and keeps a closed noun-clause architecture: wealth as subject, immortalizing predicate, no outside agent entering the imagined causal chamber.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:أَنَّ}} ({{tr:anna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:1:false-sufficiency","source_type":"word_analysis","support_id":"sup_56909273dab03c1ac04b","text":"{\"blocking_evidence\":null,\"headline\":\"wealth is treated as enough\",\"reader_payoff\":\"The reader notices that the reckoning is not abstract: wealth is treated as sufficient material for a permanence claim.\",\"reason\":\"The sufficiency branch belongs to the broader root field, and the local co-occurrence with wealth and permanence lets it color the delusion; local grammar still keeps supposing as the selected verbal sense.\",\"representative_source_ids\":[\"QS-4f0946ec\",\"QI-39d00690\",\"QI-daaf08c4\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:4:form-iv-not-form-ii","source_type":"word_analysis","support_id":"sup_5c733cd0235562f20e94","text":"{\"blocking_evidence\":null,\"headline\":\"single causation, not intensive perpetuation\",\"reader_payoff\":\"The reader notices that the selected form frames wealth as causing a state, not simply describing remaining or intensively perpetuating.\",\"reason\":\"The local form is {{ar:أَخْلَدَ}} ({{tr:akhlada}}) with object suffix, not simple {{ar:خَلَدَ}} ({{tr:khalada}}) or intensive {{ar:خَلَّدَ}} ({{tr:khallada}}).\",\"representative_source_ids\":[\"QF-d17650a0\",\"QF-ecfcee0b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:4:permanence-clinging-irony","source_type":"word_analysis","support_id":"sup_6755d233815e87283a81","text":"{\"blocking_evidence\":null,\"headline\":\"permanence is shadowed by earthward attachment\",\"reader_payoff\":\"The reader notices that the word's permanence claim is shadowed by the 7:176 earthward-clinging frame, undercutting the fantasy of transcendence.\",\"reason\":\"The clinging frame is a valid lexical contrast for the same Form IV root, but local direct-object grammar selects the causative immortalizing claim as the near sense.\",\"representative_source_ids\":[\"QS-003fad8d\",\"QS-df7c3561\",\"QE-6e59bc13\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:1:boundary-diagnosis","source_type":"word_analysis","support_id":"sup_6a76e0075892c4ca8ffa","text":"{\"blocking_evidence\":null,\"headline\":\"action shifts into diagnosis\",\"reader_payoff\":\"The reader notices the abrupt boundary movement from external hoarding in 104:2 to the inner logic that hoarding has produced.\",\"reason\":\"{{ar:يَحْسَبُ}} ({{tr:yaḥsabu}}) begins 104:3 with no conjunction and with a recoverable subject from the prior ayah, so the boundary can be read as a direct move from act to diagnosis.\",\"representative_source_ids\":[\"QT-088f7aea\",\"QT-0fc20f13\",\"QB-ed9775e8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:1:prior-actor-carried","source_type":"word_analysis","support_id":"sup_6d6b1c64e2d20dac0872","text":"{\"blocking_evidence\":null,\"headline\":\"the same actor continues silently\",\"reader_payoff\":\"The reader notices that {{ar:يَحْسَبُ}} ({{tr:yaḥsabu}}) does not introduce a new subject; its 3ms morphology carries the wealth-counter from 104:2 into his inner calculation.\",\"reason\":\"QAC reads {{ar:يَحْسَبُ}} ({{tr:yaḥsabu}}) as a 3ms imperfect verb, and attachment evidence resolves the implicit subject to the same masculine figure active in the preceding relative clause.\",\"representative_source_ids\":[\"QG-6e856f80\",\"QG-848b6259\",\"QF-4175b9d2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:2:heavy-form-closed-proposition","source_type":"word_analysis","support_id":"sup_7420a3dbae41ff722246","text":"{\"blocking_evidence\":null,\"headline\":\"heavy form seals the noun clause\",\"reader_payoff\":\"The reader notices that the doubled particle presses and structures the proposition as a closed emphatic clause with {{ar:مَالَهُۥٓ}} ({{tr:mālahū}}) as governed subject.\",\"reason\":\"The heavy form {{ar:أَنَّ}} ({{tr:anna}}), not light {{ar:أَنْ}} ({{tr:an}}), governs {{ar:مَالَهُۥٓ}} ({{tr:mālahū}}) and supports the embedded nominal proposition.\",\"representative_source_ids\":[\"QF-1909aa88\",\"QF-b68fa70d\",\"QP-5ebd22a0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:4:sound-weight-and-loop","source_type":"word_analysis","support_id":"sup_7517c4d7fe70c5841552","text":"{\"blocking_evidence\":null,\"headline\":\"the closure sounds heavy and looped\",\"reader_payoff\":\"The reader notices that the repeated final {{ar:ـهُ}} ({{tr:-hū}}) binds owner and wealth, while the heavier consonants give the closing permanence claim weight.\",\"reason\":\"Both {{ar:مَالَهُۥٓ}} ({{tr:mālahū}}) and {{ar:أَخْلَدَهُۥ}} ({{tr:akhladahū}}) carry final {{ar:ـهُ}} ({{tr:-hū}}), while the final word supplies the ayah's closing stem.\",\"representative_source_ids\":[\"QF-e7067007\",\"QP-4d60dddb\",\"QP-ba75cbe6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:2:embedded-object-clause","source_type":"word_analysis","support_id":"sup_7d6dbcb8a658f0418f20","text":"{\"blocking_evidence\":null,\"headline\":\"the particle embeds the whole claim\",\"reader_payoff\":\"The reader notices that {{ar:أَنَّ}} ({{tr:anna}}) makes the wealth-permanence claim the content of reckoning, not an independent assertion.\",\"reason\":\"Attachment evidence marks the {{ar:أَنَّ}} ({{tr:anna}}) clause as a content complement governed by {{ar:يَحْسَبُ}} ({{tr:yaḥsabu}}).\",\"representative_source_ids\":[\"QG-70e87035\",\"QT-2c5f1029\",\"QT-e8fa3762\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:4:final-and-forward-reversal","source_type":"word_analysis","support_id":"sup_80578ffa56794bd7bd7d","text":"{\"blocking_evidence\":null,\"headline\":\"the landing word sets up rejection\",\"reader_payoff\":\"The reader notices that the final permanence claim completes the economic delusion and becomes the target for {{ar:كَلَّا}} ({{tr:kallā}}) in 104:4.\",\"reason\":\"{{ar:أَخْلَدَهُۥ}} ({{tr:akhladahū}}) supplies the embedded predicate and closes 104:3, while the next ayah's opening rejection answers the claim.\",\"representative_source_ids\":[\"QT-d0799597\",\"QB-82ced7fb\",\"QB-f8cc8200\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:3:garden-owner-parallel","source_type":"word_analysis","support_id":"sup_868ad5439b1b341b56a1","text":"{\"blocking_evidence\":null,\"headline\":\"wealth-superiority parallel is secondary\",\"reader_payoff\":\"The reader notices a secondary wealth-delusion parallel with the garden-owner claim at 18:34, while the local grammar keeps wealth-as-agent as the main point.\",\"reason\":\"The 18:34 parallel is useful as a contrast in wealth confidence, but it does not override the local {{ar:أَنَّ}} ({{tr:anna}}) clause structure.\",\"representative_source_ids\":[\"MG-fcdaff0c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:2:reported-certainty","source_type":"word_analysis","support_id":"sup_90681193ac52cb9d9917","text":"{\"blocking_evidence\":null,\"headline\":\"certainty is reported, not endorsed\",\"reader_payoff\":\"The reader notices the double value of {{ar:أَنَّ}} ({{tr:anna}}): it gives the claim inner firmness while keeping that firmness inside a faulty supposition.\",\"reason\":\"QAC describes {{ar:أَنَّ}} ({{tr:anna}}) as an emphatic complementizer, while the governing verb keeps the clause under the subject's reckoning.\",\"representative_source_ids\":[\"QG-ec23db58\",\"QS-f07414c5\",\"QI-bc950d4c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:3:owner-owned-reversal","source_type":"word_analysis","support_id":"sup_97eb2b99335b40a7c486","text":"{\"blocking_evidence\":null,\"headline\":\"the suffix loop reverses agency\",\"reader_payoff\":\"The reader notices that the same {{ar:ـهُ}} ({{tr:-hū}}) sound first marks his ownership and then marks him as the affected object, reversing owner and owned.\",\"reason\":\"Attachment evidence resolves the suffix on {{ar:مَالَهُۥٓ}} ({{tr:mālahū}}) as possessive and the suffix on {{ar:أَخْلَدَهُۥ}} ({{tr:akhladahū}}) as direct object referring to the same masculine figure.\",\"representative_source_ids\":[\"QG-d1b2fd0b\",\"QE-c1186a4f\",\"QY-36d0a715\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:1:true-permanence-contrast","source_type":"word_analysis","support_id":"sup_9b669dd3e258cd5f040a","text":"{\"blocking_evidence\":null,\"headline\":\"permanence vocabulary is inverted\",\"reader_payoff\":\"The reader notices a contrast with true permanence language such as {{ar:مُّخَلَّدُونَ}} ({{tr:mukhalladūn}}) (76:19): here permanence enters as a false wealth-based estimate.\",\"reason\":\"The cited echo can serve as contrast, but it does not control the local parse; locally, {{ar:يَحْسَبُ}} ({{tr:yaḥsabu}}) subordinates the permanence claim as supposition.\",\"representative_source_ids\":[\"QE-56f0e9bc\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:4","source_type":"word_analysis","support_id":"sup_a1e334e6c0cb82c69ab1","text":"{\"gloss_range\":\"made him permanent or caused him to be treated as enduring; locally a Form IV perfect causative with wealth as subject and the owner as object\",\"prose\":\"{{ar:أَخْلَدَهُۥ}} ({{tr:akhladahū}}) is the ayah's landing word, and it makes the false claim syntactically complete. The Form IV causative does not merely say that the man remains; it casts {{ar:مَالَهُۥٓ}} ({{tr:mālahū}}) as the agent that has made him permanent, while the attached {{ar:ـهُ}} ({{tr:-hū}}) makes the owner the affected object. That is the central reversal: the possessed thing becomes the imagined cause, and the possessor becomes what it acts upon. The perfect form treats this impossible result as already done, even though the whole claim remains inside the ongoing {{ar:يَحْسَبُ}} ({{tr:yaḥsabu}}). The finite verbal shape is therefore marked: eternity is cast as an event that wealth has supposedly performed, not as ordinary participial eternity language. The selected form also differs from simple remaining or intensive perpetuation; it frames a single caused state attributed to wealth. The 7:176 frame {{ar:أَخْلَدَ إِلَى}} ({{tr:akhlada ilā}}) can shadow the word as an earthward-clinging contrast, but the missing {{ar:إِلَى}} ({{tr:ilā}}) and the direct object here keep the local sense narrowed to causative immortalizing. The broader root field of eternity, settled inward thought, and remaining behind deepens the irony without replacing the grammar. Final position lets the reader exit on the claimed permanence that 104:4 will reject with {{ar:كَلَّا}} ({{tr:kallā}}), turning imagined security into impending expulsion.\",\"root_display\":\"{{ar:خ ل د}} ({{tr:kh-l-d}})\",\"root_gloss_range\":\"permanence, enduring, being made lasting, and the Form IV earthward-clinging frame; local direct-object grammar selects causative immortalizing while allowing the 7:176 clinging contrast as a narrowed echo\",\"surface_display\":\"{{ar:أَخْلَدَهُۥ}} ({{tr:akhladahū}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:4:causative-wealth-agent","source_type":"word_analysis","support_id":"sup_a436e8d9cbc8598722bc","text":"{\"blocking_evidence\":null,\"headline\":\"wealth is made the cause\",\"reader_payoff\":\"The reader notices that the Form IV verb makes wealth the imagined agent that causes permanence, not merely an object associated with permanence.\",\"reason\":\"QAC marks {{ar:أَخْلَدَهُۥ}} ({{tr:akhladahū}}) as a Form IV perfect causative, and attachment evidence identifies {{ar:مَالَهُۥٓ}} ({{tr:mālahū}}) as its subject.\",\"representative_source_ids\":[\"QF-90727f99\",\"QS-1143c6b0\",\"QG-a70f19bc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:3","source_type":"word_analysis","support_id":"sup_adba9979dad79338e9c0","text":"{\"gloss_range\":\"his wealth, concrete owned property now functioning as the embedded subject of the causative predicate\",\"prose\":\"{{ar:مَالَهُۥٓ}} ({{tr:mālahū}}) is not just the thing he thinks about. Because {{ar:أَنَّ}} ({{tr:anna}}) governs it as the embedded subject, and because {{ar:أَخْلَدَهُۥ}} ({{tr:akhladahū}}) supplies the predicate, wealth becomes the imagined actor inside the false claim. The same root had appeared in 104:2 as indefinite wealth gathered; here it returns as possessed, definite {{ar:مَالَهُۥٓ}} ({{tr:mālahū}}), a consolidated mass marked as his before it is imagined to act on him. The repeated {{ar:ـهُ}} ({{tr:-hū}}) then becomes crucial: first it marks ownership in {{ar:مَالَهُۥٓ}} ({{tr:mālahū}}), then it marks the owner as object in {{ar:أَخْلَدَهُۥ}} ({{tr:akhladahū}}). That suffix loop makes the reversal visible and audible: what he owns is grammatically staged as what secures, and traps, him. The nasal handoff from the heavy particle into the wealth noun also makes the governor-to-ism bond audible before the final suffix cadence closes the loop. The concrete wealth range keeps the delusion material, while the inclining association can be retained only as a narrowed pressure: he leans toward wealth so deeply that the clause imagines it leaning back with causal power. The recurrence at 111:2, where wealth does not avail, makes the local confidence look even more exposed, and the garden-owner wealth-superiority claim at 18:34 adds a secondary parallel for wealth-confidence without displacing the local wealth-as-agent grammar.\",\"root_display\":\"{{ar:م و ل}} ({{tr:m-w-l}})\",\"root_gloss_range\":\"wealth, property, capital, and owned resources; local possession narrows the range to the subject's accumulated wealth while some inclining pressure remains only as a qualified lexical color\",\"surface_display\":\"{{ar:مَالَهُۥٓ}} ({{tr:mālahū}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:4:owner-as-object-loop","source_type":"word_analysis","support_id":"sup_b30b415b548fc19279af","text":"{\"blocking_evidence\":null,\"headline\":\"the owner receives the action\",\"reader_payoff\":\"The reader notices that the suffix on {{ar:أَخْلَدَهُۥ}} ({{tr:akhladahū}}) turns the possessor into the object acted on by his possession.\",\"reason\":\"Attachment evidence marks the final {{ar:ـهُ}} ({{tr:-hū}}) as the direct object of {{ar:أَخْلَدَ}} ({{tr:akhlada}}), referring to the same owner marked in {{ar:مَالَهُۥٓ}} ({{tr:mālahū}}).\",\"representative_source_ids\":[\"QG-0b68eab4\",\"QG-c2b3ce55\",\"QF-8c702d13\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"104:3:1:1","source_type":"qac_morpheme","support_id":"sup_b59085336ea020dfe94a","text":"{\"lemma_ar\":\"حَسِبَ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:Hasiba|ROOT:Hsb|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"104:3:1:1\",\"qac_word_ref\":\"104:3:1\",\"root_ar\":\"ح س ب\",\"surface_ar\":\"يَحْسَبُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:1:counting-becomes-misreckoning","source_type":"word_analysis","support_id":"sup_c0922d283336e821e42b","text":"{\"blocking_evidence\":null,\"headline\":\"counting turns into false reckoning\",\"reader_payoff\":\"The reader notices that the prior counting of wealth in 104:2 becomes a mental calculation about permanence in 104:3.\",\"reason\":\"V4 supports counting/reckoning and supposing branches for {{ar:ح س ب}} ({{tr:ḥ-s-b}}), while the local syntax selects the supposing frame; the counting branch survives as the same-surah pressure from 104:2, not as the direct local sense.\",\"representative_source_ids\":[\"QS-4b38b352\",\"QS-d91867fa\",\"MI-f20a87b1\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:3:possessed-definite-return","source_type":"word_analysis","support_id":"sup_ce03306215ab8743aeb7","text":"{\"blocking_evidence\":null,\"headline\":\"gathered wealth returns as his\",\"reader_payoff\":\"The reader notices the same-surah shift from indefinite wealth gathered in 104:2 to possessed definite wealth that can dominate the embedded claim.\",\"reason\":\"QAC marks {{ar:مَالَهُۥٓ}} ({{tr:mālahū}}) as a concrete noun with possessive suffix, while the prior ayah's indefinite {{ar:مَالًا}} ({{tr:mālan}}) supplies the same-surah contrast.\",\"representative_source_ids\":[\"QG-4a978327\",\"QF-becfa99f\",\"QE-387ca958\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:3:sound-bound-governance","source_type":"word_analysis","support_id":"sup_cfdad1b2c518e353a386","text":"{\"blocking_evidence\":null,\"headline\":\"sound marks the clause bond\",\"reader_payoff\":\"The reader notices that the nasal handoff from {{ar:أَنَّ}} ({{tr:anna}}) to {{ar:مَالَهُۥٓ}} ({{tr:mālahū}}) and the shared final {{ar:ـهُ}} ({{tr:-hū}}) cadence make the grammar audible.\",\"reason\":\"The surface sequence places {{ar:أَنَّ}} ({{tr:anna}}) before its governed noun, and both {{ar:مَالَهُۥٓ}} ({{tr:mālahū}}) and {{ar:أَخْلَدَهُۥ}} ({{tr:akhladahū}}) end in the same bound pronoun sound.\",\"representative_source_ids\":[\"QP-51f4f438\",\"QP-abcd38f2\",\"QB-25cd463b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:3:wealth-reckoning-permanence-pairing","source_type":"word_analysis","support_id":"sup_d5092b6fca394192be5c","text":"{\"blocking_evidence\":null,\"headline\":\"wealth feeds the permanence calculation\",\"reader_payoff\":\"The reader notices that wealth is the material input through which reckoning reaches the permanence claim.\",\"reason\":\"Contextual co-occurrence profiles and the local clause align wealth with both reckoning and {{ar:خ ل د}} ({{tr:kh-l-d}}) permanence vocabulary in this ayah.\",\"representative_source_ids\":[\"QI-154fe93c\",\"QI-943e2fb1\",\"MI-47501fc0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:4:perfect-under-imperfect","source_type":"word_analysis","support_id":"sup_d684c9521485e5abaeb4","text":"{\"blocking_evidence\":null,\"headline\":\"the impossible result is treated as done\",\"reader_payoff\":\"The reader notices that an ongoing supposition continually asserts a completed immortalization.\",\"reason\":\"QAC marks {{ar:أَخْلَدَهُۥ}} ({{tr:akhladahū}}) as perfect, while {{ar:يَحْسَبُ}} ({{tr:yaḥsabu}}) is imperfect and governs the entire claim.\",\"representative_source_ids\":[\"QG-897fc53b\",\"QT-ccaae1d8\",\"MF-00ee3a8e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:3:3:singular-owned-mass","source_type":"word_analysis","support_id":"sup_f000fd34b6f62c97f424","text":"{\"blocking_evidence\":null,\"headline\":\"wealth is consolidated as one possession\",\"reader_payoff\":\"The reader notices that the singular possessed form makes the accumulated resources sound like one owner-marked mass at the pivot before the predicate.\",\"reason\":\"{{ar:مَالَهُۥٓ}} ({{tr:mālahū}}) is a singular concrete noun with bound possessive suffix, and the recitational surface lets that possession linger before the predicate.\",\"representative_source_ids\":[\"QF-7e329f3b\",\"QF-ffd3622c\",\"QF-4684dad0\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ","ayah_ref":"104:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000318/B002","root_000429/B001","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000318","role":"The supposition branch supplies the uncertain mental judgment that launches the causal claim.","root":"ح س ب","source_ref":"104:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"The acquiring-and-having branch supplies the possessed stock that is promoted into an agent.","root":"م و ل","source_ref":"104:3","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000429","role":"The enduring-state branch supplies the imagined result, while the causative form assigns its production to wealth.","root":"خ ل د","source_ref":"104:3","source_word_indices":["4"]}],"changed_reading":{"after":"He performs a causal misattribution in which possessed stock is treated as a machine for producing duration in its possessor.","before":"He thinks his wealth has made him immortal."},"confidence":"strong","focus_anchor":"The cognition at word 1 takes the possessed wealth at word 3 as the cause expressed by the causative permanence verb at word 4.","mechanism":"A supposition transfers causal power from the possessor to his possession: accumulated property is imagined to manufacture an enduring state for him.","model_id":"b_supposed_causal_permanence"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_supposed_causal_permanence","source_type":"hft","support_id":"sup_a5d14fa88a405c5daf3c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ","ayah_ref":"104:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000318/B001","root_000429/B001","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000318","role":"The counting-and-accounting branch supplies the quantitative operation behind the judgment.","root":"ح س ب","source_ref":"104:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"The wealth branch supplies an inventory capable of being totaled and increased.","root":"م و ل","source_ref":"104:3","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000429","role":"The long-lasting-state branch supplies the temporal quantity onto which the property total is projected.","root":"خ ل د","source_ref":"104:3","source_word_indices":["4"]}],"changed_reading":{"after":"He reads life as a balance sheet, converting a rising property total into an imagined extension of personal time.","before":"Wealth vaguely gives him confidence that he will last."},"confidence":"medium","focus_anchor":"The reckoning verb at word 1, the countable possession at word 3, and the duration predicate at word 4 form a quantity-to-time sequence.","mechanism":"The same mental operation that totals property silently extrapolates the total into lifespan: measurable abundance is mistaken for an increase in duration.","model_id":"b_quantity_converted_to_duration"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_quantity_converted_to_duration","source_type":"hft","support_id":"sup_4a78d971a33817b4ceb0","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ","ayah_ref":"104:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000318/B003","root_000318/B008","root_000429/B002","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000318","role":"The sufficiency branch supplies the belief that wealth is enough to answer vulnerability.","root":"ح س ب","source_ref":"104:3","source_word_indices":["1"]},{"branch_id":"B008","mapped_root_id":"root_000318","role":"The cushioning branch physicalizes that sufficiency as something that props or seats the subject.","root":"ح س ب","source_ref":"104:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"The property branch supplies the material converted into the imagined support.","root":"م و ل","source_ref":"104:3","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000429","role":"The leaning-and-clinging branch turns permanence into settled attachment rather than abstract endlessness.","root":"خ ل د","source_ref":"104:3","source_word_indices":["4"]}],"changed_reading":{"after":"He imagines wealth as a sufficient physical and social prop on which he can settle and become immovable.","before":"He expects wealth to grant abstract immortality."},"confidence":"exploratory","focus_anchor":"A support image latent at word 1 can act through the possessive noun at word 3 upon the staying-and-clinging range of word 4.","mechanism":"Wealth is imagined as enoughness made material: a cushion or prop on which the subject can settle, remain attached, and resist displacement.","model_id":"b_wealth_as_prop_for_clinging"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_wealth_as_prop_for_clinging","source_type":"hft","support_id":"sup_b536e11f375c81d424b5","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ","ayah_ref":"104:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000318/B004","root_000429/B003","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000318","role":"The counted-merit branch supplies social worth, including wealth, as a basis of rank.","root":"ح س ب","source_ref":"104:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"The possession branch supplies the visible resource from which rank is inferred.","root":"م و ل","source_ref":"104:3","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_000429","role":"The body-fixed adornment branch supplies the image of status worn as a lasting insignia.","root":"خ ل د","source_ref":"104:3","source_word_indices":["4"]}],"changed_reading":{"after":"He may also mistake wealth-marked prestige, fixed to him like an insignia, for an undying social self.","before":"He expects biological survival from wealth."},"confidence":"exploratory","focus_anchor":"The cognition at word 1 can reckon wealth among grounds of standing, while word 4 can image something enduringly fixed upon a person.","mechanism":"Possession is converted into visible merit; the subject mistakes an attached badge of rank for a status that cannot decay.","model_id":"b_wealth_as_fixed_status_insignia"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_wealth_as_fixed_status_insignia","source_type":"hft","support_id":"sup_7997df843d843a7107ae","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ","ayah_ref":"104:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000318/B002","root_000429/B004","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000318","role":"The supposition branch supplies the proposition whose persistence is at issue.","root":"ح س ب","source_ref":"104:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"The wealth branch supplies both the proposition's object and the force that repeatedly confirms it.","root":"م و ل","source_ref":"104:3","source_word_indices":["3"]},{"branch_id":"B004","mapped_root_id":"root_000429","role":"The inwardly settled-thought branch relocates permanence from lifespan to the durability of the conviction itself.","root":"خ ل د","source_ref":"104:3","source_word_indices":["4"]}],"changed_reading":{"after":"It can simultaneously diagnose wealth as having made the longevity-belief itself settle and persist within the subject.","before":"The verse reports a mistaken belief about external longevity."},"confidence":"exploratory","focus_anchor":"The sentence begins with an uncertain judgment at word 1 and ends with a root whose inventory includes a thought settled inwardly at word 4.","mechanism":"The predicate can echo back into the cognition: wealth not only appears to prolong the subject but makes the prolongation-belief lodge and persist inside him.","model_id":"b_immortality_as_settled_inner_thought"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_immortality_as_settled_inner_thought","source_type":"hft","support_id":"sup_007498efdaabcfdfe43a","trust":"legacy_unbound"}]}
</lane_packet_json>
