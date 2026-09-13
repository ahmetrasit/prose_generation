# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **91:4**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s091-regular-20260912/s091/91_4/micro.discovery.json` and modify nothing
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
  "ayah_ref": "91:4",
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
{"branch_registry":[{"boundary":"Bu dal gelme, cinsel ilişki, bayılma ve herkesi saran büyük olay anlamlarını içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_001088/B001","candidate_links":[{"candidate_id":"cand_28d7ca13aa39cff4604f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"غَشِيَ","morph_features":"STEM|POS:V|IMPF|LEM:ga$iya|ROOT:g$w|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:4:3:1","qac_word_ref":"91:4:3","surface_ar":"يَغْشَىٰ"}],"gloss":"örtme ve perdeleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey başka bir şeyle örtülür ve üstü kapatılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Örtü, gözün görmesini ya da gönlün kavrayışını engelleyen bir perde olabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Giysiyle örtünme ve eyerin üstüne konan örtü, çekirdeğin yapıya bağlı somut gerçekleşmeleridir."}}],"root_ar":"غ ش و","root_id":"root_001088","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Somut bir üst örtüsünü ve algıyı engelleyen perdeyi birlikte anlatan genel karşılıktır.","boundary_detail":"Bu dal gelme, cinsel ilişki, bayılma ve herkesi saran büyük olay anlamlarını içermez.","branch_image_ar":"غطاء يعلو الشيء ويستره","concept_gloss":"örtme ve perdeleme","contextual_glosses":[{"applicability":"Bir nesnenin başka bir şeyle doğrudan kapatıldığı somut bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gözün veya gönlün perdelenmesi ile yapıya bağlı örtünme örneklerini tek başına göstermez.","preserves":"Somut kapatma eylemini açık biçimde korur."},"facet_ids":["F001"],"text":"üstünü örtmek","usage_role":"general"},{"applicability":"Bir örtünün görmeyi ya da kavrayışı engellediği bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Somut nesne örtülerini ve giysiyle örtünmeyi dışarıda bırakır.","preserves":"Algının bir perdeyle engellenmesi yönünü korur."},"facet_ids":["F002"],"text":"görüşünü perdelemek","usage_role":"contextual"},{"applicability":"Kişinin kendi giysisini üstüne çekerek örtündüğü özel yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka nesnelerin örtülmesini ve algı perdesini kapsamaz.","preserves":"Giysiyi örtü yaparak örtünme gerçekleşmesini korur."},"facet_ids":["F003"],"text":"giysisine bürünmek","usage_role":"contextual"}],"definition":"Bir şeyin üstünü başka bir şeyle kapatarak onu görünmez, algılanmaz ya da erişilmez kılma; bu çekirdek somut örtüyü ve gözün ya da gönlün perdelenmesini kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey başka bir şeyle örtülür ve üstü kapatılır."},{"facet_id":"F002","role":"extension","statement":"Örtü, gözün görmesini ya da gönlün kavrayışını engelleyen bir perde olabilir."},{"facet_id":"F003","role":"specialization","statement":"Giysiyle örtünme ve eyerin üstüne konan örtü, çekirdeğin yapıya bağlı somut gerçekleşmeleridir."}],"identity_rationale":"Kaynak ifadesi, bir şeyin başka bir şeyle örtülmesini ortak çekirdek olarak verir; somut örtü, gözün ya da gönlün perdelenmesi, giysiyle örtünme ve eyer örtüsü bu çekirdeğin desteklenen gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyin üstünü örtmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"örtü"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"gözü veya gönlü örten perde"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"göz perdesi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"örtmek veya görüşü engellemek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"giysisiyle örtünmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"giysisiyle örtünmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"eyer örtüsü"}],"lexicalization_note":"Örtme çekirdeği yalın kullanımda bulunur; giysiyle örtünme ve eyer örtüsü gibi anlamlar ise kendi yapılarına bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yararlı sınır karşılaştırması tam örtüşen dal ile verildi, öteki adaylar ya daha genel örtme alanında kaldı ya da bu kökün ayrı dallarını yineledi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen sınırlar arasında anlamlı bir çekirdek ya da kapsam ayrımı yoktur; ayrı nesne örnekleri eş anlamlılığı bozmaz.","focus_only":null,"gloss":"örtme ve örtü","neighbor_only":null,"neighbor_ref":"root_001089/B001","relation_type":"synonym","shared_zone":"İki dal da bir şeyi örtme çekirdeğini ve bu çekirdeğin somut ya da algısal örtü gerçekleşmelerini kapsar."}],"source_phrase_ar":"أصل صحيح يدل على تغطية شيء بشيء (maqayis)؛ الغشاوة ما غشي القلب من رين الطبع (ayn)؛ الغشاء الغطاء وغشاوة أي غطاء وتغطيته واستغشى بثوبه (sihah)؛ الغشاوة ما غشي القلب من الطبع والغشاء الغطاء وغاشية السرج غطاؤه والرجل يستغشي ثوبه (tahdhib)؛ الغشاوة ما يغطى به الشيء واستغشوا ثيابهم (mufradat)","source_summary":"Kaynaklar, temel anlamı bir şeyi başka bir şeyle örtme olarak birleştirir; göz ve gönül perdesini, giysiyle örtünmeyi ve nesne örtülerini bu temele bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الغشاء والغطاء والغشاوة على القلب أو البصر، واستغشاء الثوب، وما يسمى غاشية لأنه يغطي كغاشية السرج والرحل.","what_is_not_ar":"ليس مجرد الإتيان والزيارة، ولا كناية الجماع، ولا الغشيان بمعنى الإغماء، ولا الغاشية بمعنى نازلة عامة إلا من جهة أصل التغطية."},"support_links":["sup_2c8e1a17b0e5eb712e22"]},{"boundary":"Dal sıradan bir örtüyü ya da tek başına bayılmayı değil, adı ve yapısı belirli kuşatıcı olay ile hastalık kullanımlarını anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001088/B002","candidate_links":[{"candidate_id":"cand_daa2aa5b84e15b37ed6e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"غَشِيَ","morph_features":"STEM|POS:V|IMPF|LEM:ga$iya|ROOT:g$w|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:4:3:1","qac_word_ref":"91:4:3","surface_ar":"يَغْشَىٰ"}],"gloss":"her yanı saran büyük olay","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Büyük bir olay veya sıkıntı, etkilediği kişileri her yandan sarıp kuşatır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu kuşatıcı ad, korkusuyla bütün insanları saran dünyanın sonu ve hesap günü için kullanılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bir söz öbeğinde, kişiyi tutan ve karnında etkili olan bir hastalığı adlandırır."}}],"root_ar":"غ ش و","root_id":"root_001088","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kuşatıcı etkiyi çekirdeğe alır; son gün, ağır karşılık ve hastalık adlandırmaları bağlama göre belirlenir.","boundary_detail":"Dal sıradan bir örtüyü ya da tek başına bayılmayı değil, adı ve yapısı belirli kuşatıcı olay ile hastalık kullanımlarını anlatır.","branch_image_ar":"غاشية تعم وتجلل","concept_gloss":"her yanı saran büyük olay","contextual_glosses":[{"applicability":"Bir ağır olayın veya karşılığın topluluğun tümünü kapladığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dünyanın sonu ve iç hastalık adlandırmalarını tek başına taşımaz.","preserves":"Yaygın ve kuşatıcı sıkıntı yönünü korur."},"facet_ids":["F001"],"text":"herkesi kuşatan felaket","usage_role":"contextual"},{"applicability":"Bütün insanları korkusuyla saracak son günü adlandıran bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka yaygın sıkıntıları ve iç hastalık kullanımını kapsamaz.","preserves":"Son günün bütün insanları kuşatan korkutucu olay oluşunu korur."},"facet_ids":["F002"],"text":"dünyanın sonu ve hesap günü","usage_role":"contextual"},{"applicability":"Kişinin karnında etkili olan hastalığı adlandıran özel söz öbeğini açıklar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Topluluğu kuşatan olay ve son gün anlamlarını dışarıda bırakır.","preserves":"Kişiyi tutup etkisi altına alan hastalık kullanımını korur."},"facet_ids":["F003"],"text":"içini tutan hastalık","usage_role":"explanatory"}],"definition":"İnsanları korkusu ya da etkisiyle bütünüyle sarıp kuşatan büyük olay veya sıkıntı; belirli kullanımlarda dünyanın sonu ve hesap gününü, yaygın ağır karşılığı ya da kişiyi tutan bir iç hastalığı adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Büyük bir olay veya sıkıntı, etkilediği kişileri her yandan sarıp kuşatır."},{"facet_id":"F002","role":"specialization","statement":"Bu kuşatıcı ad, korkusuyla bütün insanları saran dünyanın sonu ve hesap günü için kullanılır."},{"facet_id":"F003","role":"associated_use","statement":"Belirli bir söz öbeğinde, kişiyi tutan ve karnında etkili olan bir hastalığı adlandırır."}],"identity_rationale":"Kaynak ifadesi, insanları bütünüyle sarıp kaplayan korkutucu olay veya sıkıntıyı temel alır; dünyanın sonu ve hesap günü, yaygın ağır karşılık ve kişiyi tutan iç hastalık bu adlandırmanın belirtilen kullanımlarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"dünyanın sonu ve hesap günü"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"herkesi kuşatan ağır karşılık veya bela"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"karnında ağır bir hastalığa tutuldu"}],"lexicalization_note":"Kuşatıp kaplama bağı ortak olsa da dünyanın sonu, yaygın ağır karşılık ve iç hastalık anlamları belirli ad ve söz öbeklerine bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel sıkıntı dalı en yakın karışma alanını gösterir, öteki adaylar belirli felaket türlerine ya da bu kökün ayrı anlamlarına aittir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda her yanı sarma ve kaplama imgesi belirleyicidir; komşu dalda ise bir olayın zaman içinde başa gelmesi yeterlidir.","focus_only":"Bu dal, sıkıntının insanları bütünüyle sarıp kuşatmasını kurucu özellik yapar ve son gün ile iç hastalık kullanımlarını da taşır.","gloss":"kuşatıcı felaket ile genel sıkıntı","neighbor_only":"Karşı dal, zaman içinde ortaya çıkan olay ve sıkıntıları kuşatıcı etki koşulu olmadan genel olarak kapsar.","neighbor_ref":"root_000299/B005","relation_type":"near_neighbor","shared_zone":"İki dal da insanlara gelen ağır olayları ve sıkıntıları adlandırabilir."}],"source_phrase_ar":"الغاشية القيامة لأنها تغشى الخلق بإفزاعها ورماه الله بغاشية وهو داء يأخذ كأنه يغشاه (maqayis)؛ الغاشية القيامة لأنها تغشى بإفزاعها ورماه الله بغاشية وهي داء يأخذ في الجوف (sihah)؛ غاشية من عذاب الله أي عقوبة مجللة تعمهم وغاشية اسم من أسماء القيامة وداء يأخذه في جوفه (tahdhib)؛ الغاشية كل ما يغطي الشيء ونائبة تغشاهم وتجللهم وكناية عن القيامة (mufradat)","source_summary":"Kaynaklar kuşatıp kaplama imgesini, bütün insanları saran son gün ve ağır karşılık kullanımlarıyla, ayrıca kişiyi tutan bir iç hastalık adıyla birlikte verir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الغاشية للقيامة أو العذاب أو النائبة التي تغشى الناس وتعمهم، والداء المسمى غاشية لأنه يأخذ صاحبه.","what_is_not_ar":"ليس الغطاء الحسي وحده، ولا مجرد زيارة الناس، ولا إغماء الفرد إلا إذا صرح باسم الغاشية أو النائبة."},"support_links":["sup_8d96c944c734fc146032"]},{"boundary":"Bu dal örtmeyi, cinsel ilişkiyi ve bilinç yitimini değil, hedefe gelme veya uğrama hareketini temel alır.","branch_kind":"mixed_non_bare","branch_ref":"root_001088/B003","candidate_links":[{"candidate_id":"cand_3ade8cf804882c5325bd","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"غَشِيَ","morph_features":"STEM|POS:V|IMPF|LEM:ga$iya|ROOT:g$w|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:4:3:1","qac_word_ref":"91:4:3","surface_ar":"يَغْشَىٰ"}],"gloss":"gelip uğrama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hareket eden kişi, hedefteki kişiye ya da yere gelir ve uğrar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kimseye gelen ziyaretçiler, dostlar ve istekte bulunanlar topluca adlandırılır."}}],"root_ar":"غ ش و","root_id":"root_001088","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiyi ya da yeri hedef alan gelme hareketini ve bağlama göre oraya gelenleri anlatır.","boundary_detail":"Bu dal örtmeyi, cinsel ilişkiyi ve bilinç yitimini değil, hedefe gelme veya uğrama hareketini temel alır.","branch_image_ar":"إتيان يغشى المقصود","concept_gloss":"gelip uğrama","contextual_glosses":[{"applicability":"Hedefin bir kişi olduğu ve ona gelindiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir yere gelmeyi ve ziyaretçilerin toplu adını kapsamaz.","preserves":"Bir kişiyi hedef alan gelme hareketini korur."},"facet_ids":["F001"],"text":"yanına gelmek","usage_role":"contextual"},{"applicability":"Hedefin bir yer olduğu gelme ve varma bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişiye gelme ile ziyaretçi topluluğu kullanımını dışarıda bırakır.","preserves":"Belirli bir yere gelme ve uğrama yönünü korur."},"facet_ids":["F001"],"text":"bir yere uğramak","usage_role":"contextual"},{"applicability":"Bir kimsenin ziyaretçilerini ve ona düzenli olarak uğrayanları topluca anlatır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tekil gelme hareketini ve yer hedefini doğrudan anlatmaz.","preserves":"Bir kişiye gelen ziyaretçi çevresi yönünü korur."},"facet_ids":["F002"],"text":"gelip gidenleri","usage_role":"contextual"}],"definition":"Bir kişiye ya da yere gelme, oraya varıp uğrama; belirli bir adlaşmış kullanımda, bir kimseye gelen ziyaretçi, dost ve istekte bulunanların tümünü anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hareket eden kişi, hedefteki kişiye ya da yere gelir ve uğrar."},{"facet_id":"F002","role":"specialization","statement":"Bir kimseye gelen ziyaretçiler, dostlar ve istekte bulunanlar topluca adlandırılır."}],"identity_rationale":"Kaynak ifadesi, bir kişiye ya da yere gelme ve uğrama anlamını açıkça verir; bir kişiye sık sık gelen ziyaretçiler, dostlar ve istekte bulunanlar bu hareketin adlaşmış özel görünümüdür.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yanına gelmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bir yere gelmek"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bir kimsenin ziyaretçileri ve gelip gidenleri"}],"lexicalization_note":"Kişiye veya yere gelme anlamı yalın kullanımlarda görülür; bir kimsenin ziyaretçi çevresini anlatan adlaşmış anlam belirli yapıya bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam örtüşen dal en yararlı karşılaştırmadır, öteki adaylar genel gelme alanında daha geniş ya da farklı hareket ilişkileri taşır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen çekirdek, hedef türleri ve ziyaretçi uzantısı bakımından iki dal arasında anlamlı bir sınır farkı yoktur.","focus_only":null,"gloss":"gelme ve uğrama","neighbor_only":null,"neighbor_ref":"root_001089/B005","relation_type":"synonym","shared_zone":"İki dal da kişiye veya yere gelmeyi ve kişiye gelen ziyaretçi ya da istekte bulunanları kapsar."}],"source_phrase_ar":"غشيه غشيانا أي جاءه (sihah)؛ الغاشية السؤال الذين يغشونك وغاشية الرجل من ينتابه من زواره وأصدقائه (tahdhib)؛ غشيت موضع كذا أتيته (mufradat)","source_summary":"Kaynaklar kişiye veya yere gelme anlamında birleşir ve bir kimseye gelen ziyaretçi, dost ve istekte bulunanları bu hareketin özel adlaşmış kullanımı olarak verir.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه غشيان الرجل أو الموضع بمعنى جاءه أو أتاه، ومن يغشى الرجل من سؤال وزوار وأصدقاء.","what_is_not_ar":"ليس الغطاء والستر، ولا غشيان المرأة كناية عن الجماع، ولا الإغماء."},"support_links":["sup_8d9578dfc8fafdd6d9ef"]},{"boundary":"Anlam, sıradan gelme ya da örtme değildir; kadın nesnesiyle kurulan ve cinsel ilişkiyi dolaylı anlatan kullanımla sınırlıdır.","branch_kind":"non_bare","branch_ref":"root_001088/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"غَشِيَ","morph_features":"STEM|POS:V|IMPF|LEM:ga$iya|ROOT:g$w|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:4:3:1","qac_word_ref":"91:4:3","surface_ar":"يَغْشَىٰ"}],"gloss":"kadınla cinsel ilişkiyi dolaylı anlatma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir erkek ile bir kadın arasındaki cinsel ilişki anlatılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İlişki doğrudan adlandırılmayıp gelme veya örtme eylemi üzerinden dolaylı söylenir."}}],"root_ar":"غ ش و","root_id":"root_001088","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kadın veya eş katılımcısıyla kurulan ve cinsel ilişkiyi örtülü biçimde bildiren yapılara özgüdür.","boundary_detail":"Anlam, sıradan gelme ya da örtme değildir; kadın nesnesiyle kurulan ve cinsel ilişkiyi dolaylı anlatan kullanımla sınırlıdır.","branch_image_ar":"غشيان المرأة كناية عن الجماع","concept_gloss":"kadınla cinsel ilişkiyi dolaylı anlatma","contextual_glosses":[{"applicability":"Cinsel ilişkinin bağlamdan açıkça anlaşıldığı ve dolaylı söyleyişin korunmak istendiği yerlerde kullanılır.","error_profile":{"adds":"Cinsel olmayan sıradan birliktelik anlamına da gelebilir.","collision":"Bağlam yetersizse yalnızca aynı yerde bulunma anlamıyla karışabilir.","fit":"broadening","loses":null,"preserves":"Kadınla ilişkiyi doğrudan adlandırmadan anlatma yönünü korur."},"facet_ids":["F001","F002"],"text":"kadınla birlikte olmak","usage_role":"contextual"}],"definition":"Bir erkeğin bir kadınla cinsel ilişkide bulunmasını, ona gelme ya da onu örtme anlatımı üzerinden dolaylı biçimde söyleme.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir erkek ile bir kadın arasındaki cinsel ilişki anlatılır."},{"facet_id":"F002","role":"specialization","statement":"İlişki doğrudan adlandırılmayıp gelme veya örtme eylemi üzerinden dolaylı söylenir."}],"identity_rationale":"Kaynak ifadesi, bir erkeğin bir kadınla cinsel ilişkide bulunmasını gelme ya da örtme anlatımıyla dolaylı biçimde söyleyen kullanımı açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kadınla birlikte olmak; cinsel ilişkiyi dolaylı anlatır"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"eşiyle birlikte olmak; cinsel ilişkiyi dolaylı anlatır"}],"lexicalization_note":"Cinsel ilişki anlamı yalın köke genellenmez; kadın veya eş katılımcısını alan, dolaylı anlatım kuran belirli kullanımlara bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; basma imgesine dayalı dolaylı anlatım en yakın karşılıktır, diğerleri aynı alanın farklı ve daha özel söyleyişleridir.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen anlam sınırları bakımından iki dal arasında anlamlı bir çekirdek ya da kapsam ayrımı yoktur; farklı dolaylı anlatım imgeleri aynı yerleşmiş cinsel ilişki gönderimini değiştirip daraltmaz.","focus_only":null,"gloss":"cinsel ilişki için iki dolaylı anlatım","neighbor_only":null,"neighbor_ref":"root_001659/B006","relation_type":"synonym","shared_zone":"İki dal da bir erkeğin kadınla cinsel ilişkide bulunmasını doğrudan adlandırmadan bildirir."}],"source_phrase_ar":"الغشيان غشيان الرجل المرأة (maqayis)؛ غشيها غشيانا جامعها (sihah)؛ الغشيان كناية عن إتيان الرجل المرأة وتغشى امرأته (tahdhib)؛ غشيت موضع كذا أتيته وكني بذلك عن الجماع وغشاها وتغشاها (mufradat)","source_summary":"Kaynaklar, erkeğin kadınla cinsel ilişkide bulunmasını gelme ve örtme anlatımıyla dolaylı söyleyen yapılar üzerinde birleşir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه غشي الرجل المرأة أو تغشاها بمعنى جامعها، ويذكر على جهة الكناية عن الإتيان.","what_is_not_ar":"ليس مطلق الإتيان إلى موضع أو زيارة رجل، ولا الغطاء الحسي، ولا الإغماء."},"support_links":[]},{"boundary":"Bu dal somut örtüyü ya da topluluğu saran felaketi değil, bireyin anlayış ve bilinç kaybını anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001088/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"غَشِيَ","morph_features":"STEM|POS:V|IMPF|LEM:ga$iya|ROOT:g$w|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:4:3:1","qac_word_ref":"91:4:3","surface_ar":"يَغْشَىٰ"}],"gloss":"bilincini yitirip bayılma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir durum kişinin anlayışını veya bilincini kapatır ve kişi baygın hale gelir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ölüm yaklaşırken ortaya çıkan baygınlık, aynı bilinç örtülmesinin özel bir türüdür."}}],"root_ar":"غ ش و","root_id":"root_001088","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Anlayışın veya bilincin kapanmasıyla oluşan baygınlığı ve ölüm sırasındaki özel görünümünü kapsar.","boundary_detail":"Bu dal somut örtüyü ya da topluluğu saran felaketi değil, bireyin anlayış ve bilinç kaybını anlatır.","branch_image_ar":"غشية تغطي الوعي","concept_gloss":"bilincini yitirip bayılma","contextual_glosses":[{"applicability":"Kişinin bilincini geçici olarak yitirdiği olağan bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Anlayışı örten durum imgesini ve ölüm sırasındaki özel kullanımı belirtmez.","preserves":"Bilinç yitimi ve baygın hale gelme sonucunu korur."},"facet_ids":["F001"],"text":"bayılmak","usage_role":"general"},{"applicability":"Ölüm yaklaşırken kişiyi kaplayan baygınlık durumunu adlandıran özel bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ölümle bağlantısız genel bayılma durumlarını kapsamaz.","preserves":"Ölüm sırasında ortaya çıkan bilinç yitimini korur."},"facet_ids":["F002"],"text":"ölüm baygınlığı","usage_role":"contextual"}],"definition":"Kişinin başına gelen bir durumun anlayışını ya da bilincini örtmesiyle onun bayılıp bilinçsiz kalması; ölüm sırasında beliren baygınlık bunun özel bir gerçekleşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir durum kişinin anlayışını veya bilincini kapatır ve kişi baygın hale gelir."},{"facet_id":"F002","role":"specialization","statement":"Ölüm yaklaşırken ortaya çıkan baygınlık, aynı bilinç örtülmesinin özel bir türüdür."}],"identity_rationale":"Kaynak ifadesi, kişinin anlayışını ya da bilincini örten bir durumun başına gelmesini ve onun baygın kalmasını açıkça verir; ölüm sırasında gelen baygınlık da bu duruma bağlı özel kullanımdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bilincini yitirip bayılmak"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"baygınlık; ölüm baygınlığı"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"baygın, bilinci kapalı"}],"lexicalization_note":"Bilinç yitimi anlamı belirli edilgen yapılarda ve baygınlık adında gerçekleşir; ölüm sırasındaki kullanım ayrıca kendi söz öbeğine bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam örtüşen dal en yararlı karşılaştırmadır, öteki adaylar bilinç kaybının nedeni, sonucu veya daha özel türleriyle ayrılır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen çekirdek, süreç, sonuç ve ölümle ilgili özel kullanım bakımından iki dal arasında sınır farkı yoktur.","focus_only":null,"gloss":"bilinç ve anlayışın kapanması","neighbor_only":null,"neighbor_ref":"root_001089/B007","relation_type":"synonym","shared_zone":"İki dal da kişinin anlayışının kapanmasını, baygın hale gelmesini ve ölüm sırasındaki baygınlığı kapsar."}],"source_phrase_ar":"غشي عليه غشية وغشيا وغشيانا فهو مغشي عليه (sihah)؛ غشي عليه فهو مغشي عليه وهي الغشية وكذلك غشية الموت (tahdhib)؛ غشي على فلان إذا نابه ما غشي فهمه (mufradat)","source_summary":"Kaynaklar, kişinin anlayışını veya bilincini örten bir durum yüzünden baygın hale gelmesini ortak anlam olarak verir ve ölüm sırasındaki baygınlığı buna bağlar.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه غشي عليه وغشيان الموت، أي حالة تنوب الإنسان فتغشى فهمه أو وعيه فيصير مغشيا عليه.","what_is_not_ar":"ليس الغطاء المحسوس، ولا النازلة العامة المسماة غاشية، ولا الجماع."},"support_links":[]},{"boundary":"Dal genel örtme ya da genel vurma değildir; kişi ile kamçı veya kılıç katılımcılarını birleştiren yapılara bağlıdır.","branch_kind":"non_bare","branch_ref":"root_001088/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"غَشِيَ","morph_features":"STEM|POS:V|IMPF|LEM:ga$iya|ROOT:g$w|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:4:3:1","qac_word_ref":"91:4:3","surface_ar":"يَغْشَىٰ"}],"gloss":"kamçı veya kılıçla vurma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiye kamçı veya kılıç kullanılarak darbe indirilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem, kişiyi araçla bağlayan ya da aracı doğrudan vuruş olarak kuran iki belirli yapıda gerçekleşir."}}],"root_ar":"غ ش و","root_id":"root_001088","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Vurulan kişinin ve kamçı ya da kılıç aracının açıkça yer aldığı belirli yapılara uygulanır.","boundary_detail":"Dal genel örtme ya da genel vurma değildir; kişi ile kamçı veya kılıç katılımcılarını birleştiren yapılara bağlıdır.","branch_image_ar":"إلباس الضربة بالسوط أو السيف","concept_gloss":"kamçı veya kılıçla vurma","contextual_glosses":[{"applicability":"Vurma aracının kamçı olduğu yapıda kullanılan doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kılıçla darbe indirme seçeneğini kapsamaz.","preserves":"Kişiye araçla darbe indirme eylemini ve kamçı koşulunu korur."},"facet_ids":["F001","F002"],"text":"kamçıyla vurmak","usage_role":"contextual"},{"applicability":"Vuruş aracının kılıç olduğu yapıda eylemi açık biçimde karşılar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kamçıyla vurma seçeneğini kapsamaz.","preserves":"Hedef kişinin üzerine kılıçla darbe indirilmesini korur."},"facet_ids":["F001","F002"],"text":"üzerine kılıç darbesi indirmek","usage_role":"contextual"}],"definition":"Bir kimsenin üzerine kamçı ya da kılıçla vuruş indirme; anlam, vurulan kişiyi ve kullanılan aracı birlikte belirten yapılara bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiye kamçı veya kılıç kullanılarak darbe indirilir."},{"facet_id":"F002","role":"specialization","statement":"Eylem, kişiyi araçla bağlayan ya da aracı doğrudan vuruş olarak kuran iki belirli yapıda gerçekleşir."}],"identity_rationale":"Kaynak ifadesi, bir kişiye kamçıyla vurmayı veya onun üzerine kamçı ya da kılıç darbesi indirmeyi açıkça bildirir; örtme benzetisi yalnızca bu araçlı vurma yapısının kuruluşunu açıklar.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bir kimseye kamçıyla vurmak"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"üzerine kamçı veya kılıç darbesi indirmek"}],"lexicalization_note":"Vurma anlamı yalın köke genellenmez; kamçı veya kılıç aracını açıkça içeren belirli kişi nesneli yapılarda geçerlidir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam örtüşen dal en yararlı karşılaştırmadır, öteki adaylar belirli araçlara, beden bölgelerine veya vuruş sonuçlarına göre ayrılır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen katılımcılar, araç koşulu ve vuruş yapıları bakımından iki dal arasında anlamlı bir sınır farkı yoktur.","focus_only":null,"gloss":"kamçı veya kılıç darbesi indirme","neighbor_only":null,"neighbor_ref":"root_001089/B006","relation_type":"synonym","shared_zone":"İki dal da bir kişiye kamçıyla vurmayı veya onun üzerine kamçı ya da kılıç darbesi indirmeyi anlatır."}],"source_phrase_ar":"غشيت الرجل بالسوط ضربته (sihah)؛ غشيته سوطا أو سيفا ككسوته وعممته (mufradat)","source_summary":"Kaynaklar, kişiye kamçıyla vurma ve onun üzerine kamçı ya da kılıç darbesi indirme yapılarını aynı araçlı vurma anlamında birleştirir.","sources":["SI","MU"],"what_is_ar":"يدخل فيه غشيت الرجل بالسوط أو غشيته سوطا أو سيفا، أي أوقعت عليه الضرب بذلك.","what_is_not_ar":"ليس مطلق التغطية، ولا الإتيان والزيارة، ولا الجماع."},"support_links":[]},{"boundary":"Dal, hayvanın başını veya yüzünü bütünüyle kaplayan aklıkla ve bunu adlandıran özel biçimlerle sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001088/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"غَشِيَ","morph_features":"STEM|POS:V|IMPF|LEM:ga$iya|ROOT:g$w|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:4:3:1","qac_word_ref":"91:4:3","surface_ar":"يَغْشَىٰ"}],"gloss":"hayvanın başını veya yüzünü kaplayan aklık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Aklık, hayvanın başını veya yüzünü parça bırakmadan kaplar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"At ve benzeri hayvanlarda aklık başın tümünü kaplar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Keçide aklık yüzün tümünü kaplar ve özellik buna bağlı özel adla belirtilir."}}],"root_ar":"غ ش و","root_id":"root_001088","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"At ve benzeri hayvanların bütün başı ile keçinin bütün yüzünü örten aklık için kullanılır.","boundary_detail":"Dal, hayvanın başını veya yüzünü bütünüyle kaplayan aklıkla ve bunu adlandıran özel biçimlerle sınırlıdır.","branch_image_ar":"بياض يغشى وجه الحيوان","concept_gloss":"hayvanın başını veya yüzünü kaplayan aklık","contextual_glosses":[{"applicability":"At veya benzeri bir hayvanın bütün başının ak olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Keçinin bütün yüzünü kaplayan aklık kullanımını kapsamaz.","preserves":"Aklığın başın tümünü kaplaması koşulunu korur."},"facet_ids":["F001","F002"],"text":"başı bütünüyle ak","usage_role":"contextual"},{"applicability":"Aklığın keçinin bütün yüzünü kapladığı özel hayvan betimlemesinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"At ve benzeri hayvanlarda bütün başı kaplayan aklığı kapsamaz.","preserves":"Hayvan türünü ve yüzü bütünüyle kaplayan aklığı korur."},"facet_ids":["F001","F003"],"text":"yüzü bütünüyle ak keçi","usage_role":"contextual"}],"definition":"At ve benzeri hayvanlarda başın tümünü ya da keçide yüzün tümünü kaplayan aklık; özellik, hayvan türü ve kaplanan beden bölgesini belirten özel yapılarda adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Aklık, hayvanın başını veya yüzünü parça bırakmadan kaplar."},{"facet_id":"F002","role":"specialization","statement":"At ve benzeri hayvanlarda aklık başın tümünü kaplar."},{"facet_id":"F003","role":"specialization","statement":"Keçide aklık yüzün tümünü kaplar ve özellik buna bağlı özel adla belirtilir."}],"identity_rationale":"Kaynak ifadesi, at ve benzeri hayvanlarda başın tümünün, keçide ise yüzün tümünün aklıkla kaplanmasını açıkça verir; bu, sıradan körlük ya da genel renk adı değildir.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"başı bütünüyle ak at"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yüzü bütünüyle ak keçi"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"keçinin yüzünü kaplayan aklık"}],"lexicalization_note":"Aklık özelliği, atın başını veya keçinin yüzünü belirten söz öbeklerinde ve bunlara bağlı özel ad biçiminde gerçekleşir; genel aklık anlamına yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam örtüşen dal en yararlı karşılaştırmadır, öteki adaylar aklığın başka beden bölgeleri, biçimleri veya genel görünümleriyle ayrılır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen beden bölgesi, kaplama derecesi ve hayvan alanı bakımından iki dal arasında anlamlı bir sınır farkı yoktur.","focus_only":null,"gloss":"hayvan yüzünü veya başını örten aklık","neighbor_only":null,"neighbor_ref":"root_001089/B008","relation_type":"synonym","shared_zone":"İki dal da hayvanın yüzünü ya da başını kaplayan aklığı ve buna göre yapılan özel adlandırmayı kapsar."}],"source_phrase_ar":"الأعشى من الخيل وغيرها ما ابيض رأسه كله وعنزة غشواء بينة الغشا (sihah)؛ الغشواء من المعزى التي يغشى وجهها كله بياض (tahdhib)","source_summary":"Kaynaklar, at ve benzeri hayvanlarda bütün başı, keçide ise bütün yüzü örten aklığı ve bu görünümün özel adlarını birlikte verir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الأعشى من الخيل وغيره إذا ابيض رأسه كله، والغشواء من المعزى إذا غشى وجهها كله بياض.","what_is_not_ar":"ليس عمى العين من غير هذا الوصف، ولا الغطاء المصنوع، ولا الغشاوة المعنوية."},"support_links":[]},{"boundary":"Anlam, fiziksel ya da algısal bir örtmeyle sınırlıdır; gelme, cinsel birleşme, vurma, bayılma ve hayvanlardaki beyazlık bu sınıra girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001089/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"غَشِيَ","morph_features":"STEM|POS:V|IMPF|LEM:ga$iya|ROOT:g$w|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:4:3:1","qac_word_ref":"91:4:3","surface_ar":"يَغْشَىٰ"}],"gloss":"örtüp kapatma ve örten şey","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel işlem, bir şeyi başka bir şeyle örtüp kapalı duruma getirmektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Örten şey, genel bir örtü veya perde olabileceği gibi kılıç, eyer ya da yük semeri için kullanılan bir kılıf da olabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Örtme, gözün görmesini veya gönlün kavrayışını engelleyen bir perde biçiminde algısal alana uzanabilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kişinin giysisine bürünerek kendini görme ve işitmeden uzak tutması, çekirdeğin belirli bir kullanım biçimidir."}}],"root_ar":"غ ش و","root_id":"root_001089","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem örtme işlemini hem de nesneyi fiziksel veya algısal olarak kapatan örtü, perde ya da kılıfı birlikte anlatır.","boundary_detail":"Anlam, fiziksel ya da algısal bir örtmeyle sınırlıdır; gelme, cinsel birleşme, vurma, bayılma ve hayvanlardaki beyazlık bu sınıra girmez.","branch_image_ar":"الستر والتغطية","concept_gloss":"örtüp kapatma ve örten şey","contextual_glosses":[{"applicability":"Bir nesnenin başka bir şeyle fiziksel olarak kapatıldığı eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Örtünün adını ve algısal perde uzantısını dışarıda bırakır.","preserves":"Fiziksel örtme işlemini doğal bir eylem olarak korur."},"facet_ids":["F001"],"text":"üstünü örtmek","usage_role":"contextual"},{"applicability":"Gözün önüne gelen bir engelin görmeyi kapattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel fiziksel örtmeyi ve nesne kılıflarını dışarıda bırakır.","preserves":"Algısal engelleme ve perdeleme sonucunu korur."},"facet_ids":["F003"],"text":"görüşünü perdelemek","usage_role":"contextual"}],"definition":"Bir şeyin üstünü başka bir şeyle örterek onu kapatmak ya da görünmesini veya algılanmasını engellemek; ayrıca bu işi gören örtü, perde ya da kılıf.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel işlem, bir şeyi başka bir şeyle örtüp kapalı duruma getirmektir."},{"facet_id":"F002","role":"specialization","statement":"Örten şey, genel bir örtü veya perde olabileceği gibi kılıç, eyer ya da yük semeri için kullanılan bir kılıf da olabilir."},{"facet_id":"F003","role":"extension","statement":"Örtme, gözün görmesini veya gönlün kavrayışını engelleyen bir perde biçiminde algısal alana uzanabilir."},{"facet_id":"F004","role":"associated_use","statement":"Kişinin giysisine bürünerek kendini görme ve işitmeden uzak tutması, çekirdeğin belirli bir kullanım biçimidir."}],"identity_rationale":"Kaynak ifadesi, bir şeyi başka bir şeyle örtme çekirdeğini; örtü, perde, kılıf ve giysiye bürünme gibi buna bağlı gerçekleşmeleri birlikte açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyin üstünü örtüp kapatmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"örtü; kaplayıcı tabaka"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyi, gözü veya gönlü örten perde"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"görüşü kapatan perde"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kılıcın ve yük semerinin örtüsü"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"eyer örtüsü"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"görmemek ve işitmemek için giysisine bürünmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"giysisine bürünmek"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"bir şeyi başka bir şeyin üstünü örter duruma getirmek"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bir şeyi örten şey"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"üstten kaplayan örtüler"}],"lexicalization_note":"Tanım, genel örtme çekirdeğini ayrı tutar; kılıç, eyer, yük semeri, giysi, göz ve gönülle ilgili gerçekleşmeleri yalnız kendi biçim ve kullanım çevrelerinde ele alır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnız tam örtüşen örtme dalı ile daha geniş gizleme dalı sınırı açıklığa kavuşturduğu için yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kaynak kartlarında çekirdek ve kapsam bakımından anlamlı bir sınır farkı görünmez; iki dal birbirinin yerine kullanılabilecek ölçüde örtüşür.","focus_only":null,"gloss":"örtüyle kapatma","neighbor_only":null,"neighbor_ref":"root_001088/B001","relation_type":"synonym","shared_zone":"Her iki dal da genel örtme işlemini, örten şeyi ve göz, gönül, giysi, eyer gibi özel gerçekleşmeleri kapsar."},{"boundary_match":"partial","distinction":"Odak dalın merkezi kaplayıcı bir örtü veya perdeyken komşu dal daha geniş bir gizleme alanına açılır; bu yüzden kapsamları tam olarak aynı değildir.","focus_only":"Bu dal, nesne kılıfları ile göz ve gönül önündeki perdeyi özellikle kapsar.","gloss":"örtme ve gizleme","neighbor_only":"Komşu dal, haber veya tanıklığı gizleme ve utanma gibi örtme dışındaki gizleme uzantılarını da kapsar.","neighbor_ref":"root_000438/B001","relation_type":"near_synonym","shared_zone":"İki dalın ortak alanı, bir şeyin görünmesini engelleyecek biçimde üstünü örtmektir."}],"source_phrase_ar":"يدل على تغطية شيء بشيء (maqayis)؛ الغشاء الغطاء (maqayis;sihah;tahdhib)؛ غاشية السيف والرحل غطاؤه (ayn)؛ غاشية السرج غطاؤه (tahdhib)؛ جعل على بصره غشوة وغشاوة أي غطاء (sihah)؛ يستغشي ثوبه كي لا يسمع ولا يرى (ayn;tahdhib)؛ الغشاوة ما يغطى به الشيء (mufradat)","source_summary":"Kaynaklar, anlamı örtme işlemi ve bu işlemi gören örtü çevresinde birleştirir; nesne kılıfları, göz veya gönül perdesi ve giysiye bürünme bu ortak çekirdeğin özel gerçekleşmeleridir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"ستر الشيء وتغطيته وما يكون غطاء كالغشاء والغشاوة وغاشية السيف والرحل والسرج والاستغشاء بالثوب وما يغشى البصر أو القلب","what_is_not_ar":"ليس إتيان المرأة ولا الغاشية بمعنى القيامة أو العقوبة ولا الداء ولا الغشي على المرء"},"support_links":[]},{"boundary":"Bu dal sıradan fiziksel örtüyü değil, topluluğun tamamını etkisi altına alan son gün, yıkım veya ceza kullanımını kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001089/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"غَشِيَ","morph_features":"STEM|POS:V|IMPF|LEM:ga$iya|ROOT:g$w|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:4:3:1","qac_word_ref":"91:4:3","surface_ar":"يَغْشَىٰ"}],"gloss":"herkesi kuşatan son gün veya ağır yıkım","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ortak çekirdek, ürkütücü bir olayın insanları ayrım gözetmeden bütünüyle etkisi altına almasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sözcük, dehşeti bütün yaratılmışları kuşatan dünyanın son günü için bir ad olarak kullanılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bir kullanımda herkesi kaplayan ağır bir ceza, yıkım veya felaket anlatılır."}}],"root_ar":"غ ش و","root_id":"root_001089","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem dünyanın son bulacağı gün adını hem de bir topluluğu bütünüyle kaplayan ceza veya felaket kullanımını korur.","boundary_detail":"Bu dal sıradan fiziksel örtüyü değil, topluluğun tamamını etkisi altına alan son gün, yıkım veya ceza kullanımını kapsar.","branch_image_ar":"الغاشية التي تعم","concept_gloss":"herkesi kuşatan son gün veya ağır yıkım","contextual_glosses":[{"applicability":"Bütün insanları dehşetiyle kuşatan son günün özel adı olarak kullanıldığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel bir ceza veya felaketin topluluğu kuşatması kullanımını dışarıda bırakır.","preserves":"Son gün göndergesini ve herkesi etkileyen dehşeti korur."},"facet_ids":["F001","F002"],"text":"dünyanın son bulacağı gün","usage_role":"contextual"},{"applicability":"Bir ceza veya felaketin bir topluluğun tümünü etkisi altına aldığı anlatımlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dünyanın son günü için özel ad olma yönünü dışarıda bırakır.","preserves":"Kapsayıcı etkiyi ve ağır ceza yönünü korur."},"facet_ids":["F001","F003"],"text":"her yanı saran ağır ceza","usage_role":"contextual"}],"definition":"İnsanların tümünü korkusu ve dehşetiyle kuşatan dünyanın son günü; ayrıca bir topluluğu bütünüyle kaplayan ağır yıkım veya ceza.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ortak çekirdek, ürkütücü bir olayın insanları ayrım gözetmeden bütünüyle etkisi altına almasıdır."},{"facet_id":"F002","role":"specialization","statement":"Sözcük, dehşeti bütün yaratılmışları kuşatan dünyanın son günü için bir ad olarak kullanılır."},{"facet_id":"F003","role":"associated_use","statement":"Belirli bir kullanımda herkesi kaplayan ağır bir ceza, yıkım veya felaket anlatılır."}],"identity_rationale":"Kaynak ifadesi, insanları dehşetiyle bütünüyle kuşatan son günü ve herkesi kaplayan ağır bir yıkım ya da cezayı aynı kuşatma imgesi altında açıkça verir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"dünyanın son bulup herkesin yeniden diriltileceği gün"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"Tanrı'dan gelen, herkesi kuşatan ağır ceza"}],"lexicalization_note":"Tanım, tek başına kullanılan son gün adını ve yalnız belirli ceza anlatımında ortaya çıkan herkesi kuşatma anlamını ayrı yüzler olarak korur.","neighbor_coverage_note":"Adayların çoğu farklı alanlara aittir; yalnız fiziksel örtme dalı, bu anlamdaki mecazlaşmış toplu kuşatmanın kaynağını ve sınırını belirginleştirir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda kuşatma, son günün ya da ağır bir cezanın insanlar üzerindeki etkisidir; komşu dalda ise örtme işlemi ve örtü doğrudan anlamın çekirdeğidir.","focus_only":"Bu dal, insan topluluğunu dehşet veya cezanın bütünüyle etkisi altına almasını anlatır.","gloss":"kuşatıcı felaket","neighbor_only":"Komşu dal, bir nesneyi fiziksel ya da algısal bir örtüyle kapatmayı ve o örtüyü anlatır.","neighbor_ref":"root_001089/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da bir şeyin başka bir şey tarafından bütünüyle kaplanması veya kuşatılması imgesi vardır."}],"source_phrase_ar":"الغاشية القيامة لأنها تغشى الخلق بإفزاعها (maqayis;sihah)؛ الغاشية القيامة (ayn)؛ الغاشية اسم من أسماء القيامة في القرآن (tahdhib)؛ غاشية من عذاب الله أي عقوبة مجللة تعمهم (tahdhib)؛ نائبة تغشاهم وتجللهم (mufradat)","source_summary":"Kaynakların ortak anlatımı, ürkütücü etkisi herkesi kuşatan son gün adını öne çıkarır ve aynı kuşatma biçimini topluluğu bütünüyle kaplayan ağır ceza veya felakete de uygular.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الغاشية للقيامة أو للنائبة والعقوبة التي تغشى الناس وتعمهم","what_is_not_ar":"ليس مطلق الغطاء المحسوس ولا غاشية السرج ولا الداء"},"support_links":[]},{"boundary":"Hastalık anlamı kalıba bağlıdır; sözcüğün tek başına genel bir hastalık adı olduğu sonucuna genişletilemez.","branch_kind":"collocation","branch_ref":"root_001089/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"غَشِيَ","morph_features":"STEM|POS:V|IMPF|LEM:ga$iya|ROOT:g$w|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:4:3:1","qac_word_ref":"91:4:3","surface_ar":"يَغْشَىٰ"}],"gloss":"içini tutan hastalığa uğrama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kalıbın bildirdiği durum, kişinin içini tutan bir hastalığa yakalanmasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu hastalık anlamı serbest bir kullanım değil, kaynakta verilen uğratma bildiren söz kalıbına özgü bir anlamdır."}}],"root_ar":"غ ش و","root_id":"root_001089","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kaynakta verilen kalıp içinde, kişinin iç organlarını etkileyen bir hastalığa uğramasını karşılar.","boundary_detail":"Hastalık anlamı kalıba bağlıdır; sözcüğün tek başına genel bir hastalık adı olduğu sonucuna genişletilemez.","branch_image_ar":"الداء الآخذ في الجوف","concept_gloss":"içini tutan hastalığa uğrama","contextual_glosses":[{"applicability":"Söz kalıbının bir kişinin içini tutan hastalığa uğradığını bildirdiği cümlelerde kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin beden içinde etkili bir hastalığa uğraması anlamını korur."},"facet_ids":["F001","F002"],"text":"iç hastalığına yakalanmak","usage_role":"contextual"}],"definition":"Yalnız belirli bir söz kalıbında, kişinin içini tutan bir hastalığa uğraması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kalıbın bildirdiği durum, kişinin içini tutan bir hastalığa yakalanmasıdır."},{"facet_id":"F002","role":"specialization","statement":"Bu hastalık anlamı serbest bir kullanım değil, kaynakta verilen uğratma bildiren söz kalıbına özgü bir anlamdır."}],"identity_rationale":"Kaynak ifadesi, yalnız belirli bir söz kalıbında kişinin içini tutan bir hastalığa uğramasını verir ve geçici bayılma ya da genel örtme anlamını desteklemez.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kişinin içini tutan bir hastalığa uğraması"}],"lexicalization_note":"Tanım yalnız kişinin iç organlarını tutan hastalığa uğratılmasını bildiren kaynakta verilmiş söz kalıbına bağlıdır; buradan yalın bir kök anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün hastalık ve aynı kökün öteki anlam adayları karşılaştırıldı; yalnız içe yerleşen ağrı dalı yakın ama eş olmayan sınırı açıklamaktadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği kalıba bağlı bir hastalığa uğramadır; komşu dalın çekirdeği ise içeri giren ağrının kendisidir.","focus_only":"Bu dal, belirli bir söz kalıbında iç organları tutan bir hastalığa uğramayı bildirir.","gloss":"içe işleyen rahatsızlık","neighbor_only":"Komşu dal, kişinin içine girer gibi hissedilen ağrı veya sancıyı doğrudan adlandırır.","neighbor_ref":"root_001682/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da bedenin iç kısmında ortaya çıkan bir rahatsızlığı anlatır."}],"source_phrase_ar":"رماه الله بغاشية وهو داء يأخذ كأنه يغشاه (maqayis)؛ رماه الله بغاشية وهي داء يأخذ في الجوف (sihah)؛ رماه الله بغاشية وهو داء يأخذه في جوفه (tahdhib)","source_summary":"Kaynaklar, aynı söz kalıbını kişinin içini tutan bir hastalığa uğraması biçiminde açıklar; hastalığın türünü bunun ötesinde belirlemez.","sources":["MQ","SI","TA"],"what_is_ar":"الغاشية اسما لداء يأخذ في الجوف كأنه يغشى صاحبه","what_is_not_ar":"ليس غاشية القيامة ولا غاشية السرج ولا مطلق الغطاء"},"support_links":[]},{"boundary":"Bu dal cinsel birleşmeye özgü örtmeceli kullanımdır; bir kişiye veya yere sıradan biçimde gelme anlamına genellenmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001089/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"غَشِيَ","morph_features":"STEM|POS:V|IMPF|LEM:ga$iya|ROOT:g$w|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:4:3:1","qac_word_ref":"91:4:3","surface_ar":"يَغْشَىٰ"}],"gloss":"kadınla cinsel birleşmeyi örtmeceli anlatma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Anlamın çekirdeği, erkek ile kadın arasındaki cinsel birleşmedir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Cinsel birleşme, doğrudan adlandırılmak yerine erkeğin kadına gelmesi veya onu kaplaması üzerinden örtmeceli biçimde ifade edilir."}}],"root_ar":"غ ش و","root_id":"root_001089","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Erkeğin kadınla cinsel birleşmesini doğrudan adlandırmadan anlatan eylem adı ve kadın nesneli fiil kullanımlarını kapsar.","boundary_detail":"Bu dal cinsel birleşmeye özgü örtmeceli kullanımdır; bir kişiye veya yere sıradan biçimde gelme anlamına genellenmez.","branch_image_ar":"غشيان المرأة","concept_gloss":"kadınla cinsel birleşmeyi örtmeceli anlatma","contextual_glosses":[{"applicability":"Fiilin bir erkeğin bir kadınla cinsel birleşmesini anlattığı cümlelerde doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kaynak anlatımdaki örtmeceli söyleyiş özelliğini doğrudan karşılıkta görünür kılmaz.","preserves":"Eylemi ve iki katılımcının ayrımını açıkça korur."},"facet_ids":["F001"],"text":"kadınla cinsel birleşmeye girmek","usage_role":"contextual"},{"applicability":"Bağlamın cinsel ilişkiyi zaten açıkça belirlediği ve daha örtülü bir Türkçe anlatımın istendiği yerlerde kullanılabilir.","error_profile":{"adds":null,"collision":"Cinsel bağlam kurulmadığında sıradan birleşme anlamıyla karışabilir.","fit":"narrowing","loses":"Erkek ve kadın katılımcılarını tek başına belirtmez.","preserves":"Örtülü söyleyiş içinde birleşme eylemini korur."},"facet_ids":["F001","F002"],"text":"birleşmek","usage_role":"contextual"}],"definition":"Erkeğin kadınla cinsel birleşmeye girmesini, ona gelme veya onu kaplama tasarımı üzerinden örtmeceli biçimde anlatmak.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Anlamın çekirdeği, erkek ile kadın arasındaki cinsel birleşmedir."},{"facet_id":"F002","role":"associated_use","statement":"Cinsel birleşme, doğrudan adlandırılmak yerine erkeğin kadına gelmesi veya onu kaplaması üzerinden örtmeceli biçimde ifade edilir."}],"identity_rationale":"Kaynak ifadesi, erkeğin kadınla cinsel birleşmesini doğrudan değil, ona gelme ve onu kaplama tasarımıyla örtmeceli biçimde anlatan kullanımları birlikte doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"erkeğin kadınla cinsel birleşmesi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"kadınla cinsel birleşmeye girmek"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"karısıyla cinsel birleşmeye girmek"}],"lexicalization_note":"Tanım, eylem adındaki örtmeceli cinsel birleşme anlamını ve kadın nesnesiyle kurulan kullanımları ayırır; genel gelme anlamını bu dala taşımaz.","neighbor_coverage_note":"Cinsel birleşme alanındaki bütün adaylar değerlendirildi; yalnız aynı fiil ailesini ve aynı örtmeceli sınırı taşıyan dal tam eşdeğer bir karşılaştırma sunar.","source_phrase_ar":"الغشيان غشيان الرجل المرأة (maqayis)؛ الغشيان إتيان الرجل المرأة (ayn)؛ غشيها غشيانا جامعها (sihah)؛ الغشيان كناية عن إتيان الرجل المرأة (tahdhib)؛ كني بذلك عن الجماع يقال غشاها وتغشاها (mufradat)","source_summary":"Kaynaklar, eylem adını ve ilgili fiil biçimlerini erkeğin kadınla cinsel birleşmesi için kullanılan örtmeceli anlatımlar olarak ortak biçimde açıklar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"غشيان المرأة والتغشي بمعنى الجماع كناية","what_is_not_ar":"ليس مطلق الإتيان إلى موضع ولا الستر بثوب ولا الضرب بسوط"},"support_links":[]},{"boundary":"Bu dal sıradan gelme ve birinin çevresine gelip gitme alanındadır; cinsel birleşme, örtme veya saldırma anlamlarını içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_001089/B005","candidate_links":[{"candidate_id":"cand_3ade8cf804882c5325bd","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"غَشِيَ","morph_features":"STEM|POS:V|IMPF|LEM:ga$iya|ROOT:g$w|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:4:3:1","qac_word_ref":"91:4:3","surface_ar":"يَغْشَىٰ"}],"gloss":"birine veya bir yere gelme ve gelip gidenler","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eylem çekirdeği, bir kişiye veya belirli bir yere gelmektir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlaşmış kullanım, bir kişinin yanına gelip giden ziyaretçi ve dostları bildirir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gelenler, kişinin iyiliğinden yararlanmayı uman ve istekte bulunan kimseler de olabilir."}}],"root_ar":"غ ش و","root_id":"root_001089","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem kişi ya da yer hedefli gelme eylemini hem de bir kimsenin ziyaretçi, dost ve istekte bulunan çevresini kapsar.","boundary_detail":"Bu dal sıradan gelme ve birinin çevresine gelip gitme alanındadır; cinsel birleşme, örtme veya saldırma anlamlarını içermez.","branch_image_ar":"الإتيان والانتباب","concept_gloss":"birine veya bir yere gelme ve gelip gidenler","contextual_glosses":[{"applicability":"Eylemin hedefi bir kişi olduğunda doğal bir Türkçe karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yer hedefini ve gelip gidenler biçimindeki adlaşmış kullanımı dışarıda bırakır.","preserves":"Bir kişiye yönelip gelme eylemini korur."},"facet_ids":["F001"],"text":"yanına gelmek","usage_role":"contextual"},{"applicability":"Bir kişinin yanına düzenli ya da zaman zaman gelip giden çevresinden söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel gelme eylemini ve özellikle istekte bulunanları tek başına belirtmez.","preserves":"Kişinin yanına gelip giden insan topluluğunu korur."},"facet_ids":["F002"],"text":"ziyaretçileri ve dostları","usage_role":"contextual"}],"definition":"Bir kişiye ya da yere gelmek; ayrıca iyiliğini umarak bir kimsenin yanına gelip giden dilenci, ziyaretçi ve dostlar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eylem çekirdeği, bir kişiye veya belirli bir yere gelmektir."},{"facet_id":"F002","role":"extension","statement":"Adlaşmış kullanım, bir kişinin yanına gelip giden ziyaretçi ve dostları bildirir."},{"facet_id":"F003","role":"specialization","statement":"Gelenler, kişinin iyiliğinden yararlanmayı uman ve istekte bulunan kimseler de olabilir."}],"identity_rationale":"Kaynak ifadesi, bir kişiye veya yere gelme eylemini ve bir kimseye iyiliğini umarak gelen dilenci, ziyaretçi ve dost topluluğunu açıkça aynı dalda toplar.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yanına gelmek"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir yere gelmek"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"iyilik umarak gelenler ve ziyaretçiler"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bir kişinin ziyaretçileri ve dostları"}],"lexicalization_note":"Tanım, genel gelme eylemini kişi ve yer nesneli kullanımlardan; ziyaretçi, dost ve istekte bulunanları bildiren adlaşmış kullanımdan ayrı tutar.","neighbor_coverage_note":"Bütün gelme, ziyaret ve istekte bulunma adayları incelendi; aynı eylem ve kişi topluluğu sınırını taşıyan dal tek tam eşdeğerdir.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kaynak kartlarının eylem çekirdeği, hedefleri ve adlaşmış kişi topluluğu uzantısı aynıdır; belirgin bir sınır farkı bulunmaz.","focus_only":null,"gloss":"gelme ve gelip gidenler","neighbor_only":null,"neighbor_ref":"root_001088/B003","relation_type":"synonym","shared_zone":"Her iki dal da kişiye veya yere gelmeyi ve kişinin yanına gelen ziyaretçi, dost ya da istekte bulunanları kapsar."}],"source_phrase_ar":"الغاشية الذين يغشونك يرجون فضلك (ayn)؛ غشيه غشيانا أي جاءه (sihah)؛ الغاشية السؤال الذين يغشونك يرجون فضلك ومعروفك (tahdhib)؛ غاشية الرجل من ينتابه من زواره وأصدقائه (tahdhib)؛ غشيت موضع كذا أتيته (mufradat)","source_summary":"Kaynaklar, kişiye veya yere gelme çekirdeğini; bundan türeyen ziyaretçi, dost ve iyilik umarak istekte bulunan kimseler kullanımını birlikte destekler.","sources":["AY","SI","TA","MU"],"what_is_ar":"إتيان شخص أو موضع وانتباب الزوار والسؤال ومن يغشى الإنسان لفضله أو معروفه","what_is_not_ar":"ليس الجماع الكنائي ولا الغطاء المحسوس ولا الغاشية بمعنى القيامة"},"support_links":["sup_8d9578dfc8fafdd6d9ef"]},{"boundary":"Anlam yalnız kırbaç veya kılıç aracını nesne ya da ilgeçli tümleç olarak alan vurma yapısına bağlıdır; genel örtme anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001089/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"غَشِيَ","morph_features":"STEM|POS:V|IMPF|LEM:ga$iya|ROOT:g$w|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:4:3:1","qac_word_ref":"91:4:3","surface_ar":"يَغْشَىٰ"}],"gloss":"kırbaç veya kılıçla vurma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eylem, kırbaç ya da kılıçla bir kişiye vurmayı bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Vurma anlamı, aracın doğrudan nesne veya araç bildiren tümleç olduğu belirli yapılara özgüdür."}}],"root_ar":"غ ش و","root_id":"root_001089","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız aracın kırbaç ya da kılıç olduğu ve vuruşun bir kişiye yöneldiği kaynak yapıları karşılar.","boundary_detail":"Anlam yalnız kırbaç veya kılıç aracını nesne ya da ilgeçli tümleç olarak alan vurma yapısına bağlıdır; genel örtme anlamı değildir.","branch_image_ar":"إغشاء الضرب","concept_gloss":"kırbaç veya kılıçla vurma","contextual_glosses":[{"applicability":"Kaynak yapıda vurma aracının kırbaç olduğu cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kılıcın araç olduğu paralel kullanımı dışarıda bırakır.","preserves":"Kişiye araçla vurma eylemini ve kırbaç aracını korur."},"facet_ids":["F001","F002"],"text":"kırbaçla vurmak","usage_role":"contextual"},{"applicability":"Kaynak yapıda vurma aracının kılıç olduğu cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kırbacın araç olduğu paralel kullanımı dışarıda bırakır.","preserves":"Kişiye araçla vurma eylemini ve kılıç aracını korur."},"facet_ids":["F001","F002"],"text":"kılıçla vurmak","usage_role":"contextual"}],"definition":"Yalnız belirli söz dizimi yapılarında, kırbacı veya kılıcı bir kişinin üzerine indirerek ona vurmak.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eylem, kırbaç ya da kılıçla bir kişiye vurmayı bildirir."},{"facet_id":"F002","role":"specialization","statement":"Vurma anlamı, aracın doğrudan nesne veya araç bildiren tümleç olduğu belirli yapılara özgüdür."}],"identity_rationale":"Kaynak ifadesi, kişiye kırbaçla vurmayı ve aynı yapı içinde kılıçla vurmayı, aracın vuruş olarak kişinin üzerine indirilmesi biçiminde açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"adama kırbaçla vurmak"}],"lexicalization_note":"Tanım yalnız kişiye kırbaçla veya kılıçla vurmayı bildiren kaynakta verilmiş yapılara bağlıdır; fiile bağımsız bir genel vurma anlamı yüklenmez.","neighbor_coverage_note":"Bütün vurma adayları değerlendirildi; yalnız aynı araçları ve aynı yapısal sınırı taşıyan dal tam eşdeğer bir karşılaştırma sunar.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kaynak kartlarında eylem, araçlar, hedef kişi ve söz dizimi sınırı aynıdır; kapsam bakımından ayrışmazlar.","focus_only":null,"gloss":"kırbaç veya kılıçla vurma","neighbor_only":null,"neighbor_ref":"root_001088/B006","relation_type":"synonym","shared_zone":"Her iki dal da aynı yapılarda kırbaç veya kılıcı kişinin üzerine indirerek vurmayı bildirir."}],"source_phrase_ar":"غشيت الرجل بالسوط ضربته (sihah)؛ غشيته سوطا أو سيفا ككسوته وعممته (mufradat)","source_summary":"Kaynaklar, belirli yapılarda fiilin kişiye kırbaçla vurmayı bildirdiğinde birleşir; kapsam aynı yapıda kılıçla vurmaya da uzanır.","sources":["SI","MU"],"what_is_ar":"إيقاع السوط أو السيف على الرجل بصيغة غشيته سوطا أو سيفا","what_is_not_ar":"ليس الستر بالغشاء ولا الجماع ولا الغشي على المرء"},"support_links":[]},{"boundary":"Çekirdek bilinç ve kavrayışın kapanmasıdır; sıradan uyku, yalnız baş dönmesi, iç hastalığı veya ölümün kendisi değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001089/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"غَشِيَ","morph_features":"STEM|POS:V|IMPF|LEM:ga$iya|ROOT:g$w|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:4:3:1","qac_word_ref":"91:4:3","surface_ar":"يَغْشَىٰ"}],"gloss":"kavrayışı kapanıp bayılma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin başına gelen bir durum kavrayışını örter ve bilincinin kapanmasına yol açar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Durum adı, kişinin içine düştüğü baygınlığı ve baygın kişiyi bildiren biçimlerde kullanılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Anlam, ölümü andıran ağır bilinç kapanması için de kullanılır."}}],"root_ar":"غ ش و","root_id":"root_001089","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin bilincini örten bir durum yüzünden bayılmasını, baygınlığı ve ölümü andıran ağır biçimini kapsar.","boundary_detail":"Çekirdek bilinç ve kavrayışın kapanmasıdır; sıradan uyku, yalnız baş dönmesi, iç hastalığı veya ölümün kendisi değildir.","branch_image_ar":"الغشي على الفهم","concept_gloss":"kavrayışı kapanıp bayılma","contextual_glosses":[{"applicability":"Kişinin geçici olarak bilincini yitirdiğini bildiren eylem cümlelerinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kavrayışın örtülmesi tasarımını ve ölüme yaklaşan özel biçimi belirtmez.","preserves":"Bilinç yitimi ve bayılma sonucunu korur."},"facet_ids":["F001"],"text":"bayılmak","usage_role":"contextual"},{"applicability":"Eylemden çok kişinin içine düştüğü bilinçsizlik durumunun adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Durumun kişiye gelmesi sürecini ve ölümü andıran özel kullanımı dışarıda bırakır.","preserves":"Bilincin kapanmış olduğu durumu ad olarak korur."},"facet_ids":["F002"],"text":"baygınlık","usage_role":"contextual"}],"definition":"Kişinin kavrayışını örten bir durum yüzünden bilincini yitirip bayılması; ayrıca bu baygınlık durumu ve ölümü andıran biçimi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin başına gelen bir durum kavrayışını örter ve bilincinin kapanmasına yol açar."},{"facet_id":"F002","role":"specialization","statement":"Durum adı, kişinin içine düştüğü baygınlığı ve baygın kişiyi bildiren biçimlerde kullanılır."},{"facet_id":"F003","role":"extension","statement":"Anlam, ölümü andıran ağır bilinç kapanması için de kullanılır."}],"identity_rationale":"Kaynak ifadesi, kişinin kavrayışını örten bir durumun başına gelmesiyle bilincinin kapanmasını, bu durumu ve ölümü andıran baygınlığı açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bilinci kapanıp bayılmak"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"baygınlık"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"baygın; bilinci kapalı"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"ölümü andıran baygınlık"}],"lexicalization_note":"Tanım, bilinç yitimini bildiren kişi üzerindeki yapıları, durum adını ve ölüme yaklaşan baygınlık kullanımını ayrı tutar; bunları yalın örtme anlamıyla birleştirmez.","neighbor_coverage_note":"Bütün bilinç yitimi, hastalık ve ölüm adayları karşılaştırıldı; tam eşdeğer dal ile baş dönmesini de içeren daha geniş dal okuyucu için yararlı iki sınır sunar.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kaynak kartlarında süreç, sonuç ve ağır uzantı bakımından anlamlı bir sınır farkı bulunmaz.","focus_only":null,"gloss":"bilinci örten baygınlık","neighbor_only":null,"neighbor_ref":"root_001088/B005","relation_type":"synonym","shared_zone":"Her iki dal da kişinin kavrayışını örten bir durumla bilincinin kapanmasını ve ölümü andıran ağır biçimi kapsar."},{"boundary_match":"partial","distinction":"Odak dal bilinç kapanmasını zorunlu tutar; komşu dal ise baş dönmesinden bayılmaya uzanan daha geniş bir belirti alanına sahiptir.","focus_only":"Bu dalın çekirdeği kavrayışın kapanmasıyla ortaya çıkan bilinç yitimidir.","gloss":"baş dönmesi ve baygınlık","neighbor_only":"Komşu dal baş dönmesini de kapsar ve bilinç yitimi her kullanımda zorunlu değildir.","neighbor_ref":"root_000499/B005","relation_type":"near_neighbor","shared_zone":"İki dal da kişide baş gösterip bilinci veya kavrayışı etkileyebilen bir durumu anlatır."}],"source_phrase_ar":"غشي عليه غشية وغشيا وغشيانا فهو مغشي عليه (sihah)؛ غشي عليه فهو مغشي عليه وهي الغشية وكذلك غشية الموت (tahdhib)؛ غشي على فلان إذا نابه ما غشي فهمه (mufradat)","source_summary":"Kaynaklar, kişinin kavrayışını örten bir durumla bilincini yitirmesinde birleşir; durum adı, baygın kişi ve ölümü andıran baygınlık bu çekirdeğe bağlı biçimlerdir.","sources":["SI","TA","MU"],"what_is_ar":"الغشي على المرء وذهاب فهمه والغشية وغشية الموت","what_is_not_ar":"ليس النوم أو النعاس بمجرده ولا الغطاء المحسوس ولا الداء المسمى غاشية"},"support_links":[]},{"boundary":"Dal, hayvanlarda yüzün tamamını veya başın tamamını kaplayan beyaz renk işaretidir; genel beyazlık ya da yalnız alın, ayak veya karın beyazlığı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001089/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"غَشِيَ","morph_features":"STEM|POS:V|IMPF|LEM:ga$iya|ROOT:g$w|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:4:3:1","qac_word_ref":"91:4:3","surface_ar":"يَغْشَىٰ"}],"gloss":"hayvanın yüzünü veya başını kaplayan beyazlık","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, beyazlığın hayvanın yüzünü ya da başını kesintisiz biçimde kaplamasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Keçiler için kullanılan biçim, yüzün tamamının beyaz olmasını bildirir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"At ve benzeri hayvanlar için verilen başka bir biçim, gövdeden farklı olarak başın tamamının beyaz olmasını bildirir."}}],"root_ar":"غ ش و","root_id":"root_001089","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Keçinin tüm yüzünü kaplayan beyazlığı ya da at ve benzeri hayvanların gövdesinden ayrılan tümüyle beyaz başı kapsar.","boundary_detail":"Dal, hayvanlarda yüzün tamamını veya başın tamamını kaplayan beyaz renk işaretidir; genel beyazlık ya da yalnız alın, ayak veya karın beyazlığı değildir.","branch_image_ar":"بياض يغشى الوجه","concept_gloss":"hayvanın yüzünü veya başını kaplayan beyazlık","contextual_glosses":[{"applicability":"Keçinin yüzünün tamamını beyazlığın kapladığı renk işareti bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başın tamamının beyaz olduğu at ve benzeri hayvan kullanımını dışarıda bırakır.","preserves":"Yüzün tümünü kaplayan beyaz renk koşulunu korur."},"facet_ids":["F001","F002"],"text":"yüzü bütünüyle beyaz","usage_role":"contextual"},{"applicability":"At veya benzeri bir hayvanın başı bütünüyle beyaz, gövdesi ise başka renkte olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalnız yüzün tamamını kaplayan keçi kullanımını dışarıda bırakır.","preserves":"Başın tümünün beyaz ve gövdeden farklı olması koşulunu korur."},"facet_ids":["F001","F003"],"text":"başı bütünüyle beyaz","usage_role":"contextual"}],"definition":"Bir hayvanın yüzünün tamamını kaplayan beyazlık veya gövdesinin geri kalanından ayrılan, başının tamamını kaplayan beyaz renk işareti.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, beyazlığın hayvanın yüzünü ya da başını kesintisiz biçimde kaplamasıdır."},{"facet_id":"F002","role":"specialization","statement":"Keçiler için kullanılan biçim, yüzün tamamının beyaz olmasını bildirir."},{"facet_id":"F003","role":"source_variant","statement":"At ve benzeri hayvanlar için verilen başka bir biçim, gövdeden farklı olarak başın tamamının beyaz olmasını bildirir."}],"identity_rationale":"Kaynak ifadesi hayvanın yüzünü bütünüyle kaplayan beyazlığı destekler, ancak başka bir biçimde at ve benzeri hayvanların gövdeden ayrılan bembeyaz başını da ayrıca verir; yalnız yüzle sınırlı bir çerçeve eksik kalır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yüzü bütünüyle beyaz keçi"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"başı bütünüyle beyaz, gövdesi başka renkte hayvan"}],"lexicalization_note":"Tanım, keçide yüzü bütünüyle kaplayan beyazlık ile at ve benzeri hayvanlarda başın tümünün beyaz olmasını ayrı biçimlere bağlar; genel bir beyazlık anlamına genişletmez.","neighbor_coverage_note":"Bütün renk işareti ve aynı kökün öteki anlam adayları değerlendirildi; tüm baş beyazlığı ile alın beyazlığına ilişkin iki kart yer sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal tümüyle beyaz başla sınırlıdır; odak dal buna ek olarak keçinin tüm yüzünü kaplayan beyazlık biçimini de içerir.","focus_only":"Bu dal, keçinin yüzünün tamamını kaplayan beyazlık biçimini de kapsar.","gloss":"hayvanda bembeyaz baş","neighbor_only":null,"neighbor_ref":"root_000438/B008","relation_type":"near_synonym","shared_zone":"İki dal da hayvanın başının bütünüyle beyaz olup gövdesinin geri kalanından ayrılmasını kapsar."},{"boundary_match":"field_only","distinction":"Odak dalın ayırıcı koşulu bütün yüzü ya da başı kaplamadır; komşu dalın çekirdeği alın üzerindeki belirgin beyazlıktır.","focus_only":"Bu dalda beyazlık yüzün veya başın tamamını kaplamak zorundadır.","gloss":"alın veya yüz beyazlığı","neighbor_only":"Komşu dal özellikle alın beyazlığını ve daha genel görünen beyazlığı kapsar.","neighbor_ref":"root_001078/B003","relation_type":"same_field","shared_zone":"Her iki dal hayvanın baş bölgesindeki belirgin beyaz renk işaretlerini adlandırır."}],"source_phrase_ar":"الأعشى من الخيل وغيرها ما ابيض رأسه كله من بين جسده (sihah)؛ عنز غشواء بينة الغشا (sihah)؛ الغشواء من المعزى التي يغشى وجهها كله بياض (tahdhib)","source_summary":"Toplu kaynak ifadesi, hayvanın yüzünü bütünüyle kaplayan beyazlık ile gövdesinden ayrılan tümüyle beyaz baş biçimini aynı renk işareti alanında verir.","sources":["SI","TA"],"what_is_ar":"الغشواء وما شاكلها في الدواب إذا غشى البياض وجهها أو رأسها","what_is_not_ar":"ليس الغشاوة على البصر ولا الغشاء الغطاء ولا المرض"},"support_links":[]},{"boundary":"Dal genel gece zamanını ve karanlığını kapsar; şiddet, uzunluk ve ayın son gecesi anlamları yalnız ilgili söz öbeklerine bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001392/B001","candidate_links":[{"candidate_id":"cand_28d7ca13aa39cff4604f","lane":"micro"},{"candidate_id":"cand_daa2aa5b84e15b37ed6e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:4:1:3","qac_word_ref":"91:4:1","surface_ar":"يْلِ"}],"gloss":"gündüzün karşıtı olan gece ve onun karanlığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gündüzün karşıtı olan zaman bölümü gecedir; tek bir gece veya birden çok gece olarak sayılabilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gece adı, bu zaman bölümüne özgü karanlığı da anlatabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli niteleme kalıpları çok karanlık veya çetin bir geceyi anlatır."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir başka pekiştirme kalıbı gecenin uzunluğunu veya şiddetini özellikle öne çıkarır."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Özel bir söz öbeği, ayın hem en karanlık hem de son gecesini belirtir."}}],"root_ar":"ل ي ل","root_id":"root_001392","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel gece zamanını ve bu zamana bağlı karanlık anlamını birlikte temsil eder; özel nitelemeler ayrıca bağlama göre çevrilir.","boundary_detail":"Dal genel gece zamanını ve karanlığını kapsar; şiddet, uzunluk ve ayın son gecesi anlamları yalnız ilgili söz öbeklerine bağlıdır.","branch_image_ar":"الليل خلاف النهار وظلمته","concept_gloss":"gündüzün karşıtı olan gece ve onun karanlığı","contextual_glosses":[{"applicability":"Zaman bölümünden çok o zamandaki karanlığın anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geceye özgü karanlık görünümünü doğrudan korur."},"facet_ids":["F002"],"text":"gece karanlığı","usage_role":"contextual"},{"applicability":"Yalnız karanlığın şiddetini veya gecenin çetinliğini pekiştiren söz öbeklerinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gecenin yoğun karanlığını ve çetinlik vurgusunu korur."},"facet_ids":["F003"],"text":"çok karanlık ve çetin gece","usage_role":"contextual"},{"applicability":"Uzunluk ile genel şiddet arasında değişebilen özel pekiştirme kalıbını açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kalıbın uzunluk ve pekiştirilmiş şiddet seçeneklerini birlikte korur."},"facet_ids":["F004"],"text":"uzun ya da şiddeti pekiştirilmiş gece","usage_role":"explanatory"},{"applicability":"Yalnız ay içindeki özel konumu ve olağanüstü karanlığı birlikte belirten söz öbeğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ayın son gecesi olma koşulunu ve en yoğun karanlığı korur."},"facet_ids":["F005"],"text":"ayın en karanlık ve son gecesi","usage_role":"contextual"}],"definition":"Gündüzün karşıtı olan gece zamanı ve bu zamana özgü karanlıktır. Belirli söz öbekleri, temel anlamı değiştirmeden gecenin çok karanlık, çetin ya da uzun oluşunu veya ayın en karanlık son gecesini belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gündüzün karşıtı olan zaman bölümü gecedir; tek bir gece veya birden çok gece olarak sayılabilir."},{"facet_id":"F002","role":"extension","statement":"Gece adı, bu zaman bölümüne özgü karanlığı da anlatabilir."},{"facet_id":"F003","role":"specialization","statement":"Belirli niteleme kalıpları çok karanlık veya çetin bir geceyi anlatır."},{"facet_id":"F004","role":"specialization","statement":"Bir başka pekiştirme kalıbı gecenin uzunluğunu veya şiddetini özellikle öne çıkarır."},{"facet_id":"F005","role":"source_variant","statement":"Özel bir söz öbeği, ayın hem en karanlık hem de son gecesini belirtir."}],"identity_rationale":"Kaynak ifadesi, gündüzün karşıtı olan gece zamanını ve gece karanlığını açıkça temel anlam olarak verir; tekil ve çoğul biçimlerin yanında karanlığın şiddetini, gecenin uzunluğunu veya belirli bir ay gecesini anlatan kalıpları da ayrıca tanıklar. Bu nedenle dal kimliği korunabilir, ancak kalıba bağlı nitelemeler temel gece anlamıyla bir tutulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"gündüzün karşıtı olan gece"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"gece karanlığı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"tek bir gece"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"geceler"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"geceler"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"geceler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"çok karanlık ve çetin gece"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"çok karanlık gece"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"uzun ya da şiddeti pekiştirilmiş gece"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ayın en karanlık ve son gecesi"}],"lexicalization_note":"Dal hem genel gece adını hem de yalnız belirli söz öbeklerinde ortaya çıkan karanlık, zorluk, uzunluk ve ay sonu nitelemelerini içerir; tanım bu iki düzeyi ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gece, geceleyin eylem, bugüne bağlı gece, yoğunlaşan karanlık ve adlandırma arasındaki sınırı en açık gösteren dört komşu seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal gecenin kendisini ve karanlığını gösterir; komşu dal ise geceyi bir eylemin gerçekleşme zamanı veya yönü olarak kodlar.","focus_only":"Geceyi bir zaman bölümü ve karanlık olarak adlandırır.","gloss":"gece ile geceleyin yapılan iş arasındaki ayrım","neighbor_only":"Geceye girme, geceleyin işlem yapma veya gece yol alma eylemlerini anlatır.","neighbor_ref":"root_001392/B002","relation_type":"same_field","shared_zone":"Her iki dal da geceyi zaman bakımından ortak eksen olarak kullanır."},{"boundary_match":"partial","distinction":"Bu dalda bugüne göre yakınlık zorunlu değildir; komşu dalın anlamı konuşma gününe ve gün içindeki söyleme anına bağlı bir gece seçimi gerektirir.","focus_only":"Herhangi bir geceyi genel zaman türü olarak kapsar.","gloss":"genel gece ile bugüne bağlı gece arasındaki ayrım","neighbor_only":"Konuşma gününe göre en yakın, geçen veya girilecek geceyi seçer.","neighbor_ref":"root_001392/B003","relation_type":"near_neighbor","shared_zone":"İki dal da gece zamanını gösterir ve belirli bağlamlarda aynı zaman dilimine işaret edebilir."},{"boundary_match":"partial","distinction":"Bu dal geceyi veya mevcut karanlığını adlandırabilir; komşu dal ise karanlığın şiddetlenmesi durumunu öne çıkarır ve genel gece adı yerine geçmez.","focus_only":"Gece zamanını, karanlığını ve bazı kalıplarda yoğun karanlık niteliğini kapsar.","gloss":"gece karanlığı ile karanlığın şiddetlenmesi arasındaki ayrım","neighbor_only":"Gecenin giderek koyulaşmasını veya karanlığının şiddetlenmesini merkez alır.","neighbor_ref":"root_001015/B004","relation_type":"near_neighbor","shared_zone":"Her ikisi de gecenin yoğun karanlığını anlatan bağlamlarda buluşur."},{"boundary_match":"thematic_only","distinction":"Bu dalın çekirdeği bir zaman bölümü ve karanlıktır; komşu dalda biçim bir kişiyi adlandırır veya daha geniş bir söz öbeği içinde şarabı örtülü biçimde anar.","focus_only":"Gece zamanını ve onun karanlığını anlatır.","gloss":"gece anlamı ile adlandırma kullanımı arasındaki ayrım","neighbor_only":"Bir kadın adını ve ayrı bir söz öbeğinde şarabın örtülü adını anlatır.","neighbor_ref":"root_001392/B004","relation_type":"thematic","shared_zone":"Dallar aynı biçim ailesiyle bağlantılıdır, fakat kavramsal alanları örtüşmez."}],"source_phrase_ar":"الليل خلاف النهار (maqayis)؛ الليل ضد النهار (jamhara;tahdhib)؛ ظلام الليل (tahdhib)؛ ليل وليلة وليلات وليال (maqayis;sihah;mufradat)؛ ليل أليل وليلة ليلاء وليل لائل (jamhara;sihah;tahdhib;mufradat)؛ ليلة ليلى أشد ليلة في الشهر ظلمة وآخر ليلة فيه (jamhara)","source_summary":"Kaynakların ortak çekirdeği geceyi gündüzün karşıtı bir zaman ve ona bağlı karanlık olarak tanımlar. Toplu kanıt ayrıca tek ve çok gece biçimlerini, karanlığı ya da uzunluğu pekiştiren kullanımları ve ayın en karanlık son gecesine özgü ifadeyi birlikte gösterir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الليل والليلة والليالي، وضده النهار، وظلام الليل وشدته وطوله في نحو ليلة ليلاء وليل أليل وليل لائل وليلة ليلى","what_is_not_ar":"لا يدخل فيه النهار ولا اليوم إلا من جهة المقابلة، ولا التسمية بليلى، ولا ولد الطائر المختلف فيه"},"support_links":["sup_2c8e1a17b0e5eb712e22","sup_8d96c944c734fc146032"]},{"boundary":"Dal gecenin kendisini değil, geceye geçişi veya geceyi zaman ve yön olarak alan işlem ile yolculuk kullanımlarını kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001392/B002","candidate_links":[{"candidate_id":"cand_3ade8cf804882c5325bd","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:4:1:3","qac_word_ref":"91:4:1","surface_ar":"يْلِ"}],"gloss":"geceye girme ya da geceleyin iş görüp yol alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iş veya karşılıklı işlem, gündüz yerine geceye göre yürütülür."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Zaman akışı içinde geceye girme veya gece vaktine ulaşma anlatılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Geceleyin yol alan veya gece yolculuğuna dayanabilen kişi anlatılır."}}],"root_ar":"ل ي ل","root_id":"root_001392","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın geceye geçiş, geceye göre işlem ve gece yolculuğu alt görünümlerini birlikte açıklayan üst karşılıktır.","boundary_detail":"Dal gecenin kendisini değil, geceye geçişi veya geceyi zaman ve yön olarak alan işlem ile yolculuk kullanımlarını kapsar.","branch_image_ar":"مزاولة الأمر في الليل","concept_gloss":"geceye girme ya da geceleyin iş görüp yol alma","contextual_glosses":[{"applicability":"Bir işlemin gündüze göre yapılan benzeriyle karşılaştırılarak gece üzerinden yürütüldüğü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı işlemin özellikle geceye göre yürütülmesini korur."},"facet_ids":["F001"],"text":"geceye göre karşılıklı işlem yapmak","usage_role":"contextual"},{"applicability":"Bir kişinin veya durumun gece vaktine ulaştığını bildiren kullanımda geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gündüzden gece vaktine geçiş ilişkisini doğrudan korur."},"facet_ids":["F002"],"text":"geceye girmek","usage_role":"contextual"},{"applicability":"Gece yolculuğu yapan veya böyle bir yolculuğa dayanabilen kişinin anlatıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gece yolculuğu yapan kişiyi ve bu yolculuğa güç yetirme koşulunu korur."},"facet_ids":["F003"],"text":"gece yol alan kimse","usage_role":"contextual"}],"definition":"Geceye girmek ya da bir işi, karşılıklı işlemi veya yolculuğu geceyi zaman ve yön olarak alarak gerçekleştirmektir. Gece yolculuğuna dayanabilen kişi de bu eylem alanına bağlı olarak adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iş veya karşılıklı işlem, gündüz yerine geceye göre yürütülür."},{"facet_id":"F002","role":"core","statement":"Zaman akışı içinde geceye girme veya gece vaktine ulaşma anlatılır."},{"facet_id":"F003","role":"specialization","statement":"Geceleyin yol alan veya gece yolculuğuna dayanabilen kişi anlatılır."}],"identity_rationale":"Kaynak ifadesi geceyi yalın bir zaman adı olarak değil, karşılıklı bir işlemin geceye göre yapılması, geceye girilmesi ve gece yolculuğu yapılması ya da buna güç yetirilmesi üzerinden verir. Geçici dal çerçevesi bu ortak eylem yönelimini doğru yakalar.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"geceye göre karşılıklı işlem yapma"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"geceye girmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"gece yol alan veya gece yolculuğuna dayanabilen kimse"}],"lexicalization_note":"Anlam yalnız türemiş biçimlerde ve belirli kullanım kalıplarında tanıklanır; karşılıklı işlem, geceye giriş ve gece yolculuğu ayrı alt görünümler olarak tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gece anlamı ile gece yolculuğunun bağımsız, zorlu veya gündüzden geceye kesintisiz türleri en yararlı dört karşılaştırmayı verdi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dalda gece, girişin, işlemin veya yolculuğun yönünü belirler; komşu dalda ise eylem değil, doğrudan zaman bölümü ve karanlık adlandırılır.","focus_only":"Geceye girme veya geceyi bir eylemin zamanı olarak kullanma anlamlarını taşır.","gloss":"geceleyin eylem ile gece zamanının ayrımı","neighbor_only":"Gece zamanını ve ona bağlı karanlığı adlandırır.","neighbor_ref":"root_001392/B001","relation_type":"same_field","shared_zone":"Her iki dalın ortak zaman ekseni gecedir."},{"boundary_match":"partial","distinction":"Bu dalın yolculuk görünümü yanında geceye giriş ve işlem anlamları vardır; komşu dal ise gece yolculuğunu kendi başına merkezî bir hareket alanı olarak kurar.","focus_only":"Geceye giriş ve geceye göre karşılıklı işlem yapma anlamlarını da kapsar.","gloss":"geniş gece eylemi ile gece yolculuğu arasındaki ayrım","neighbor_only":"Gece yolculuğunu bağımsız bir hareket olarak ve yol alan topluluğu da kapsayacak biçimde merkezleştirir.","neighbor_ref":"root_000702/B001","relation_type":"near_neighbor","shared_zone":"İki dal geceleyin yol alma anlamında belirgin biçimde örtüşür."},{"boundary_match":"partial","distinction":"Bu dal için sürekli çaba ve güçlük kurucu değildir; komşu dal gece boyunca ısrarlı ilerlemeyi ve yolculuğun zahmetini anlamın merkezine alır.","focus_only":"Geceyle bağlantılı işlemi, geçişi ve olağan yolculuk yetisini kapsar.","gloss":"gece yol alma ile gece boyunca çabalayarak ilerleme ayrımı","neighbor_only":"Gece boyunca yolculuğu sürdürme ve bunun güçlüğüne katlanma yönünü özellikle öne çıkarır.","neighbor_ref":"root_001422/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal gece yolculuğu ve bu yolculuğa dayanma alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dalda gündüzden geceye kesintisiz devam şartı yoktur; komşu dalın ayırt edici sınırı, yolculuğun bir gündüz ile bir gece boyunca sürdürülmesidir.","focus_only":"Eylemin yalnız geceye göre yapılmasını veya geceye girilmesini anlatabilir.","gloss":"geceye bağlı eylem ile kesintisiz gündüz gece yolculuğu ayrımı","neighbor_only":"Yolculuğun gündüz ile gece arasında kesintisiz sürdürülmesini zorunlu kılar.","neighbor_ref":"root_001670/B006","relation_type":"near_neighbor","shared_zone":"İki dalın kesişiminde gece boyunca yol alma bulunur."}],"source_phrase_ar":"عاملته ملايلة كما تقول مياومة من اليوم (sihah)؛ أليلت صرت في الليل (tahdhib)؛ لست بليلي ولكني نهر أي أسير بالنهار ولا أطيق سرى الليل (tahdhib)","source_summary":"Toplu kanıt geceye göre yapılan karşılıklı işlemi, gece vaktine girmeyi ve gece yolculuğu yapabilen kişiyi aynı eylem alanında birleştirir. Bu kullanımların hiçbiri yalın gece zamanını tek başına adlandırmaz.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الفعل أو المعاملة على جهة الليل، مثل الملايلة، والدخول في الليل، والسير أو السرى في الليل","what_is_not_ar":"لا يدخل فيه اسم الليل نفسه ولا الليلة بوصفها زمنا مجردا"},"support_links":["sup_8d9578dfc8fafdd6d9ef"]},{"boundary":"Dal yalnız konuşma gününe göre belirlenen en yakın geceyi kapsar; yönelim, cümlenin zamanı ve gün içindeki söyleme anına göre geçmişe veya geleceğe dönebilir.","branch_kind":"non_bare","branch_ref":"root_001392/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:4:1:3","qac_word_ref":"91:4:1","surface_ar":"يْلِ"}],"gloss":"bugüne göre belirlenen en yakın gece","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gece, konuşmacının içinde bulunduğu güne göre en yakın gece olarak belirlenir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gündüz söylenen ileri yönelimli kullanım, konuşmacının gireceği yaklaşan geceyi gösterir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tamamlanmış bir eylem günün ilk yarısında anlatılırken ifade önceki geceye dönebilir; gün ilerleyince geçmiş gece için başka bir zaman sözü seçilir."}}],"root_ar":"ل ي ل","root_id":"root_001392","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Geçmiş veya gelecek yönelimi cümle bağlamından anlaşılan, konuşma gününe en yakın geceyi üst düzeyde karşılar.","boundary_detail":"Dal yalnız konuşma gününe göre belirlenen en yakın geceyi kapsar; yönelim, cümlenin zamanı ve gün içindeki söyleme anına göre geçmişe veya geleceğe dönebilir.","branch_image_ar":"الليلة القريبة من اليوم","concept_gloss":"bugüne göre belirlenen en yakın gece","contextual_glosses":[{"applicability":"Gündüz söylenip konuşmacının gireceği yaklaşan geceye yönelen bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Konuşma gününe en yakın yaklaşan gece yönelimini korur."},"facet_ids":["F001","F002"],"text":"bu gece","usage_role":"contextual"},{"applicability":"Günün ilk yarısında tamamlanmış bir eylemi en yakın önceki geceye bağlayan Türkçe anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tamamlanmış eylemin konuşma gününden önceki en yakın geceye bağlanmasını korur."},"facet_ids":["F001","F003"],"text":"dün gece","usage_role":"contextual"}],"definition":"Konuşma gününe en yakın olan ve bağlama göre bir önceki ya da girilecek olan gecedir. Geçmiş bir eylem anlatılırken günün ilk yarısında önceki geceyi gösterebilir; gündüzden yaklaşan gece anlatılırken sonraki geceyi seçer.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gece, konuşmacının içinde bulunduğu güne göre en yakın gece olarak belirlenir."},{"facet_id":"F002","role":"specialization","statement":"Gündüz söylenen ileri yönelimli kullanım, konuşmacının gireceği yaklaşan geceyi gösterir."},{"facet_id":"F003","role":"specialization","statement":"Tamamlanmış bir eylem günün ilk yarısında anlatılırken ifade önceki geceye dönebilir; gün ilerleyince geçmiş gece için başka bir zaman sözü seçilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Bugünle ilişkisi bulunmayan herhangi bir geceyi de kapsar.","collision":null,"fit":"broadening","loses":"Konuşma gününe göre yakınlık ve bağlama bağlı zaman yönelimini belirtmez.","preserves":"Gece zamanına yapılan temel gönderimi korur."},"text":"gece"}],"identity_rationale":"Kaynak ifadesi, genel gece türünü değil konuşma gününe en yakın geceyi seçen bağlamsal bir kullanımı açıkça tanımlar. Gündüz konuşulurken girilecek geceye yönelim ile günün ilk yarısında tamamlanmış bir eylemin önceki geceye bağlanması, geçici çerçevede belirtilen yakınlık ve söyleme zamanı sınırını doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bugüne en yakın gece; bağlama göre geçen ya da girilecek olan gece"}],"lexicalization_note":"Anlam belirli bir gece ifadesinin konuşma gününe göre yorumlanmasına bağlıdır; genel ve bağlamsız gece anlamına genişletilemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gece, geceleyin eylem, ertesi gün ve bitişik zaman sınırı karşılaştırmaları dalın bugüne bağlı gönderimini en açık biçimde ayırdı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın gönderimi konuşma gününe göre hesaplanır; komşu dal genel gece adıdır ve bugüne yakınlık, söyleme anı veya geçmiş gelecek yönelimi gerektirmez.","focus_only":"Konuşma gününe en yakın geceyi ve bağlama bağlı geçmiş ya da gelecek yönelimini zorunlu kılar.","gloss":"bugüne en yakın gece ile genel gece arasındaki ayrım","neighbor_only":"Herhangi bir geceyi, geceleri ve gece karanlığını bağlamsız olarak kapsayabilir.","neighbor_ref":"root_001392/B001","relation_type":"near_synonym","shared_zone":"İki dal da tek bir gece zamanını gösterebilir ve uygun bağlamda aynı zaman aralığına işaret edebilir."},{"boundary_match":"field_only","distinction":"Bu dalın çekirdeği bağlam içinde seçilen gecedir; komşu dalda gece bir geçişin, işlemin veya yolculuğun gerçekleşme zamanı ve yönüdür.","focus_only":"Bugüne göre seçilen belirli bir gece zamanını gösterir.","gloss":"yakın gece göndergesi ile geceleyin eylem arasındaki ayrım","neighbor_only":"Geceye girme, geceleyin işlem yapma veya gece yolculuğu gerçekleştirme eylemini gösterir.","neighbor_ref":"root_001392/B002","relation_type":"same_field","shared_zone":"Her iki dal da geceyi konuşma veya eylem için zaman çerçevesi yapar."},{"boundary_match":"field_only","distinction":"Bu dal geceyi seçer ve yönelimi bağlama göre değişebilir; komşu dal ise gün birimini seçer ve zorunlu olarak konuşma gününün sonrasına yönelir.","focus_only":"Bugüne komşu geceyi, cümle yönelimine göre geçmişte veya gelecekte seçebilir.","gloss":"en yakın gece ile ertesi gün arasındaki ayrım","neighbor_only":"Yalnız konuşma gününden sonraki günü, yani gelecek gündüzlü zaman birimini seçer.","neighbor_ref":"root_001076/B002","relation_type":"same_field","shared_zone":"İki dal da konuşma gününü merkez alan yakın zaman ifadeleridir."},{"boundary_match":"field_only","distinction":"Bu dal belirli bir gece göndergesini seçer; komşu dal ise geceyi seçmekten çok iki zaman bölümünün birbirine değen başlangıç veya bitiş sınırını adlandırır.","focus_only":"Konuşma gününe göre en yakın gecenin hangisi olduğunu belirler.","gloss":"yakın gece seçimi ile zaman sınırı arasındaki ayrım","neighbor_only":"Bir zaman parçasının başlangıç veya bitiş sınırında başka bir zamanla karşı karşıya gelmesini anlatır.","neighbor_ref":"root_001479/B006","relation_type":"same_field","shared_zone":"Her ikisi de komşu zaman parçaları arasındaki ilişkiyi konu eder."}],"source_phrase_ar":"إلى نصف النهار تقول فعلت الليلة فإذا زالت الشمس قلت فعلت البارحة (tahdhib)؛ هذه الليلة التي في السماء أقرب الليالي من يومك وهي الليلة التي تليه (tahdhib)؛ الهلال في هذه الليلة التي في السماء يعني الليلة التي تدخلها يتكلم بهذا في النهار (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, günün ilk yarısında tamamlanmış bir eylem için önceki gecenin bu ifadeyle anılabildiğini, gün ilerleyince başka bir geçmiş zaman sözünün seçildiğini ve gündüzden bakıldığında yaklaşan gecenin de aynı yakınlık ilkesiyle belirlendiğini bildirir."}],"source_summary":"Kanıt, bu kullanımın genel gece adından farklı olarak konuşma gününe ve gün içindeki söyleme anına göre çözüldüğünü gösterir. Yaklaşan gece ile henüz yakın geçmiş sayılan önceki gece, cümlenin yönelimine göre ayrılır.","sources":["TA"],"what_is_ar":"يدخل فيه إطلاق الليلة على أقرب الليالي من اليوم أو على الليلة الداخلة، والفصل بينها وبين البارحة بحسب وقت الكلام","what_is_not_ar":"لا يدخل فيه مطلق الليل ولا الليالي المجموعة ولا أوصاف شدة الظلمة"},"support_links":[]},{"boundary":"Kadın adı temel adlandırma kullanımıdır; şarap anlamı yalnız ayrı ve tam bir söz öbeğinin örtülü ad işlevine aittir.","branch_kind":"non_bare","branch_ref":"root_001392/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:4:1:3","qac_word_ref":"91:4:1","surface_ar":"يْلِ"}],"gloss":"bir kadın adı; ayrıca belirli bir söz öbeğinde şarabın örtülü adı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Söz konusu biçim bir kadını adlandıran kişi adı olarak kullanılır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu adı içeren ayrı bir söz öbeği, şarabı doğrudan söylemeden anan örtülü bir ad olarak kullanılır."}}],"root_ar":"ل ي ل","root_id":"root_001392","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kişi adı çekirdeğini ve yalnız tam söz öbeğine bağlı şarap adlandırmasını sınırlarıyla birlikte açıklar.","boundary_detail":"Kadın adı temel adlandırma kullanımıdır; şarap anlamı yalnız ayrı ve tam bir söz öbeğinin örtülü ad işlevine aittir.","branch_image_ar":"التسمية بليلى","concept_gloss":"bir kadın adı; ayrıca belirli bir söz öbeğinde şarabın örtülü adı","contextual_glosses":[{"applicability":"Biçimin bir kadını adlandırdığı kişi adı kullanımında geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Biçimin kadın kişi adı olma işlevini korur."},"facet_ids":["F001"],"text":"bir kadın adı","usage_role":"contextual"},{"applicability":"Yalnız kadın adını içeren tam söz öbeğinin şarabı dolaylı biçimde andığı kullanımda geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tam söz öbeğinin şarabı örterek adlandırma işlevini korur."},"facet_ids":["F002"],"text":"şarap için kullanılan örtülü ad","usage_role":"contextual"}],"definition":"Bir biçimin kadın adı olarak kullanılmasıdır; aynı adı içeren ayrı bir söz öbeği ise şarabı anan örtülü bir ad işlevi görür. İki kullanım aynı dalda bulunsa da kadın adı ile içki anlamı birbirine eşit değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Söz konusu biçim bir kadını adlandıran kişi adı olarak kullanılır."},{"facet_id":"F002","role":"associated_use","statement":"Bu adı içeren ayrı bir söz öbeği, şarabı doğrudan söylemeden anan örtülü bir ad olarak kullanılır."}],"identity_rationale":"Kaynak ifadesi bir biçimin kadın adı olduğunu ve bu adı içeren ayrı bir söz öbeğinin şarabı örtülü biçimde anlattığını doğrular. Dal bir adlandırma kümesi olarak korunabilir; ancak kadın adının kendi başına şarap anlamına geldiği sanılmamalı, şarap anlamı yalnız tam söz öbeğine bağlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"bir kadın adı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"şarap için kullanılan örtülü ad"}],"lexicalization_note":"Dal yalnız ad olarak kullanılan biçimi ve şarabı anan tam söz öbeğini kapsar; bunlar genel gece veya karanlık anlamına genişletilemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gece dalı ile iki ayrı kişi adı dalı, adlandırma işlevini biçimsel yakınlıktan ve farklı ad kimliklerinden ayırmak için seçildi.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Bu dalın anlamı kişi ve içki adlandırmasıdır; komşu dal ise bir zaman bölümünü ve karanlığı gösterir, dolayısıyla iki dal olağan kullanımda birbirinin yerine geçmez.","focus_only":"Bir kadın adını ve ayrı bir söz öbeğinde şarabın örtülü adını kapsar.","gloss":"adlandırma ile gece anlamı arasındaki ayrım","neighbor_only":"Gece zamanını ve gece karanlığını anlatır.","neighbor_ref":"root_001392/B001","relation_type":"thematic","shared_zone":"Dallar aynı biçim ailesiyle bağlantılıdır, fakat yalnız tarihsel ve biçimsel bir çağrışım paylaşır."},{"boundary_match":"field_only","distinction":"Adlandırma işlevleri aynı alandadır, fakat adların kimlikleri ayrıdır; ayrıca bu dalda belirli bir söz öbeğine bağlı şarap kullanımı bulunur.","focus_only":"Farklı bir kadın adını ve bu adı içeren örtülü şarap sözünü kapsar.","gloss":"iki ayrı kadın adının anlam alanı","neighbor_only":"Başka ve ayrı bir kadın adını kapsar.","neighbor_ref":"root_000848/B009","relation_type":"same_field","shared_zone":"Her iki dal da bir biçimin kadın kişi adı olarak kullanılmasını tanıklar."},{"boundary_match":"field_only","distinction":"Ortak alan adlandırmadır; ancak gösterilen adlar farklıdır ve komşu dalın erkek adı ile lakap kapsamı bu dalda bulunmaz, bu dalın şarap söz öbeği de komşuda yoktur.","focus_only":"Bir kadın adı ile ona bağlı örtülü şarap sözünü içerir.","gloss":"ayrı kişi adları ve lakaplar alanı","neighbor_only":"Başka biçimlerin erkek adı, kadın adı veya lakap olarak kullanılmasını içerir.","neighbor_ref":"root_000799/B007","relation_type":"same_field","shared_zone":"İki dal da sözlük biçimlerinin kişi adı olarak aktarılmasını konu eder."}],"source_phrase_ar":"وبه سميت ليلى (jamhara)؛ ليلى اسم امرأة (sihah)؛ أم ليلى هي الخمر (tahdhib)","source_summary":"Toplu kanıt kadın adı kullanımını ortak biçimde destekler ve ayrıca bu adı içeren tam bir söz öbeğinin şarabı örten bir ad olduğunu bildirir. İkinci kullanım bağımsız söz öbeğine bağlı tutulmalıdır.","sources":["JA","SI","TA"],"what_is_ar":"يدخل فيه ليلى اسما لامرأة، وأم ليلى كنية للخمر","what_is_not_ar":"لا يدخل فيه الليل زمنا ولا الظلمة ولا المعاملة بالليل"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["91:4:1"],"branch_refs":[],"candidate_id":"cand_fd79fe121840213ee41d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:4:1:bound-cadence","source_type":"word_analysis","support_ids":["sup_e62571667aa7afeb28d1","sup_faaebda87dcbc8b20def"],"title":"single-letter attached reset","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:1","qac_refs":["91:4:1:1"],"status":"accepted"}},{"anchor_refs":["91:4:1"],"branch_refs":[],"candidate_id":"cand_884ec4a5c781af9c5415","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:4:1:oath-chain-continuation","source_type":"word_analysis","support_ids":["sup_12a0b5f1736cc0c0f814","sup_faaebda87dcbc8b20def"],"title":"continued four-part oath chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:1","qac_refs":["91:4:1:1"],"status":"accepted"}},{"anchor_refs":["91:4:1"],"branch_refs":[],"candidate_id":"cand_a3d79709342f41c577a9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:4:1:oath-governance","source_type":"word_analysis","support_ids":["sup_35660ebda69b6c629904","sup_faaebda87dcbc8b20def"],"title":"qasam particle governs the night noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:1","qac_refs":["91:4:1:1"],"status":"accepted"}},{"anchor_refs":["91:4:2"],"branch_refs":[],"candidate_id":"cand_38eef8b834ec3aa6996e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"91:4:2:darkness-field","source_type":"word_analysis","support_ids":["sup_68f526662407868d7674","sup_bf94a072153025f133b0"],"title":"night as concealment field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:2","qac_refs":["91:4:1:2","91:4:1:3"],"status":"accepted"}},{"anchor_refs":["91:4:2"],"branch_refs":[],"candidate_id":"cand_7bc84775fe575b706230","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"91:4:2:day-night-reversal","source_type":"word_analysis","support_ids":["sup_68f526662407868d7674","sup_e99f6396acaddf58b03d"],"title":"night reverses the day disclosure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:2","qac_refs":["91:4:1:2","91:4:1:3"],"status":"accepted"}},{"anchor_refs":["91:4:2"],"branch_refs":[],"candidate_id":"cand_bba42908bd29b14d25d4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"91:4:2:definite-genitive-night","source_type":"word_analysis","support_ids":["sup_68f526662407868d7674","sup_a9372ce418eabb2c9da6"],"title":"known night as genitive oath object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:2","qac_refs":["91:4:1:2","91:4:1:3"],"status":"accepted"}},{"anchor_refs":["91:4:2"],"branch_refs":[],"candidate_id":"cand_637d6c5b235bf98e8511","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"91:4:2:form-and-root-limit","source_type":"word_analysis","support_ids":["sup_4b801daa2429e3938915","sup_68f526662407868d7674"],"title":"singular form and derivational dispute bounded","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:2","qac_refs":["91:4:1:2","91:4:1:3"],"status":"accepted"}},{"anchor_refs":["91:4:2"],"branch_refs":[],"candidate_id":"cand_2161f34ff4bdae7d0082","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"91:4:2:series-and-later-echoes","source_type":"word_analysis","support_ids":["sup_03bbda1e43ff20301dff","sup_68f526662407868d7674"],"title":"local pair with wider echo pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:2","qac_refs":["91:4:1:2","91:4:1:3"],"status":"accepted"}},{"anchor_refs":["91:4:2"],"branch_refs":[],"candidate_id":"cand_003ec9a005e57c6a8ca3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"91:4:2:sound-texture","source_type":"word_analysis","support_ids":["sup_2c4dbe65ced6359e435c","sup_68f526662407868d7674"],"title":"heavy night-word texture","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:2","qac_refs":["91:4:1:2","91:4:1:3"],"status":"accepted"}},{"anchor_refs":["91:4:2"],"branch_refs":[],"candidate_id":"cand_6d6edb6d06a31cea705a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"91:4:2:sworn-witness-as-agent","source_type":"word_analysis","support_ids":["sup_35f8cc8f5e616a5a46ed","sup_68f526662407868d7674"],"title":"oath object becomes coverer","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:2","qac_refs":["91:4:1:2","91:4:1:3"],"status":"accepted"}},{"anchor_refs":["91:4:3"],"branch_refs":[],"candidate_id":"cand_54c909348d6d401af358","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:4:3:entity-when-action-architecture","source_type":"word_analysis","support_ids":["sup_061f5cffd7a07eedf065","sup_5c87f7026f502165b01e"],"title":"hinge from witness to action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:3","qac_refs":["91:4:2:1"],"status":"accepted"}},{"anchor_refs":["91:4:3"],"branch_refs":[],"candidate_id":"cand_212e60abbd1381e1f0e9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:4:3:fixed-particle-sound-pivot","source_type":"word_analysis","support_ids":["sup_310513ba486c7c9ba437","sup_5c87f7026f502165b01e"],"title":"rootless acoustic pivot","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:3","qac_refs":["91:4:2:1"],"status":"accepted"}},{"anchor_refs":["91:4:3"],"branch_refs":[],"candidate_id":"cand_257cb8a51df82729c0f5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:4:3:recurring-temporal-condition","source_type":"word_analysis","support_ids":["sup_5c87f7026f502165b01e","sup_cdc52556cf8eface9b5e"],"title":"certain recurring when-clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:3","qac_refs":["91:4:2:1"],"status":"accepted"}},{"anchor_refs":["91:4:4"],"branch_refs":[],"candidate_id":"cand_276ace084d323336f98b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001088","root_001089"],"scope":"focus_ayah","source_local_id":"91:4:4:agent-object-compression","source_type":"word_analysis","support_ids":["sup_3781c156e8ddeb983ed2","sup_43d535108dc80d67272c"],"title":"night as agent, suffix as patient","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:4","qac_refs":["91:4:3:1","91:4:3:2"],"status":"accepted"}},{"anchor_refs":["91:4:4"],"branch_refs":[],"candidate_id":"cand_3116c4dcd005d9848f0f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001088","root_001089"],"scope":"focus_ayah","source_local_id":"91:4:4:covering-envelopment","source_type":"word_analysis","support_ids":["sup_3781c156e8ddeb983ed2","sup_ba1e59eb5bffaa76157e"],"title":"covering as spatial concealment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:4","qac_refs":["91:4:3:1","91:4:3:2"],"status":"accepted"}},{"anchor_refs":["91:4:4"],"branch_refs":[],"candidate_id":"cand_02575514935b33c3e43b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001088","root_001089"],"scope":"focus_ayah","source_local_id":"91:4:4:finite-active-form","source_type":"word_analysis","support_ids":["sup_3781c156e8ddeb983ed2","sup_e70aec599308c904f481"],"title":"finite active verb over static noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:4","qac_refs":["91:4:3:1","91:4:3:2"],"status":"accepted"}},{"anchor_refs":["91:4:4"],"branch_refs":[],"candidate_id":"cand_84762cd13739bd77fdc5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001088","root_001089"],"scope":"focus_ayah","source_local_id":"91:4:4:opposition-and-cadence","source_type":"word_analysis","support_ids":["sup_3781c156e8ddeb983ed2","sup_4f875b20f7478b8069f3"],"title":"same suffix cadence, opposite action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:4","qac_refs":["91:4:3:1","91:4:3:2"],"status":"accepted"}},{"anchor_refs":["91:4:4"],"branch_refs":[],"candidate_id":"cand_44c2c4fc4417cae795de","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001088","root_001089"],"scope":"focus_ayah","source_local_id":"91:4:4:overwhelm-branch-limited","source_type":"word_analysis","support_ids":["sup_03b7d4368c5589e85eb1","sup_3781c156e8ddeb983ed2"],"title":"overwhelm imagery bounded by cosmic context","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:4","qac_refs":["91:4:3:1","91:4:3:2"],"status":"accepted"}},{"anchor_refs":["91:4:4"],"branch_refs":[],"candidate_id":"cand_17bf4c365aa0906b34f6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001088","root_001089"],"scope":"focus_ayah","source_local_id":"91:4:4:pronoun-ambiguity","source_type":"word_analysis","support_ids":["sup_3047d08c15017aa7b8fb","sup_3781c156e8ddeb983ed2"],"title":"feminine object kept unresolved","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:4","qac_refs":["91:4:3:1","91:4:3:2"],"status":"accepted"}},{"anchor_refs":["91:4:4"],"branch_refs":[],"candidate_id":"cand_82517f7c1897a1bfa060","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001088","root_001089"],"scope":"focus_ayah","source_local_id":"91:4:4:recurring-active-imperfect","source_type":"word_analysis","support_ids":["sup_3781c156e8ddeb983ed2","sup_ae9ffb2b30a200d77b3c"],"title":"active imperfect recurrence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:4","qac_refs":["91:4:3:1","91:4:3:2"],"status":"accepted"}},{"anchor_refs":["91:4:4"],"branch_refs":[],"candidate_id":"cand_b3e0741132743824dcbf","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001088","root_001089"],"scope":"focus_ayah","source_local_id":"91:4:4:sound-texture","source_type":"word_analysis","support_ids":["sup_3781c156e8ddeb983ed2","sup_c5c2bab9640149ec3804"],"title":"spreading sound texture","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:4","qac_refs":["91:4:3:1","91:4:3:2"],"status":"accepted"}},{"anchor_refs":["91:4:4"],"branch_refs":[],"candidate_id":"cand_a740cfb72317d2a464f2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001088","root_001089"],"scope":"focus_ayah","source_local_id":"91:4:4:wider-formula-echo","source_type":"word_analysis","support_ids":["sup_3781c156e8ddeb983ed2","sup_fdb7389fc0cfd5d1b1b8"],"title":"night-when-covering formula","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:4:4","qac_refs":["91:4:3:1","91:4:3:2"],"status":"accepted"}},{"anchor_refs":["91:4:1"],"branch_refs":[],"candidate_id":"cand_364540a84a40a7136d5f","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"91:4:1:3","source_type":"qac_morpheme","support_ids":["sup_e8a6b84d80685c2b040d"],"title":"QAC root occurrence: ل ي ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:4:3"],"branch_refs":[],"candidate_id":"cand_a9df197ccdf307153cbe","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001088","root_001089"],"scope":"focus_ayah","source_local_id":"91:4:3:1","source_type":"qac_morpheme","support_ids":["sup_cba603dc6bd6b73bcdfc"],"title":"QAC root occurrence: غ ش و","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:4","branch_refs":["root_001088/B001","root_001392/B001"],"candidate_id":"cand_28d7ca13aa39cff4604f","commentary_obligation":"review","hft_ref":"hft_406b80060b8e85d5e80a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b01_surface_veil","source_type":"hft","support_ids":["sup_2c8e1a17b0e5eb712e22"],"title":"b01_surface_veil","trust":"legacy_unbound"},{"anchor_refs":["91:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:4","branch_refs":["root_001088/B003","root_001089/B005","root_001392/B002"],"candidate_id":"cand_3ade8cf804882c5325bd","commentary_obligation":"review","hft_ref":"hft_92c529835c8361406b4c","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b02_arriving_night","source_type":"hft","support_ids":["sup_8d9578dfc8fafdd6d9ef"],"title":"b02_arriving_night","trust":"legacy_unbound"},{"anchor_refs":["91:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:4","branch_refs":["root_001088/B002","root_001392/B001"],"candidate_id":"cand_daa2aa5b84e15b37ed6e","commentary_obligation":"review","hft_ref":"hft_939a730db00fa6efd390","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b03_total_overtaking","source_type":"hft","support_ids":["sup_8d96c944c734fc146032"],"title":"b03_total_overtaking","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَٱلَّيْلِ إِذَا يَغْشَىٰهَا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:4:1:1","qac_word_ref":"91:4:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"91:4:1:2","qac_word_ref":"91:4:1","root_ar":"","surface_ar":"ٱلَّ"},{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:4:1:3","qac_word_ref":"91:4:1","root_ar":"ل ي ل","surface_ar":"يْلِ"},{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"91:4:2:1","qac_word_ref":"91:4:2","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"غَشِيَ","morph_features":"STEM|POS:V|IMPF|LEM:ga$iya|ROOT:g$w|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:4:3:1","qac_word_ref":"91:4:3","root_ar":"غ ش و","surface_ar":"يَغْشَىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:4:3:2","qac_word_ref":"91:4:3","root_ar":"","surface_ar":"هَا"}],"word_analysis_qac_refs":[["91:4:1:1"],["91:4:1:2","91:4:1:3"],["91:4:2:1"],["91:4:3:1","91:4:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["91:4:1","91:4:2","91:4:3","91:4:4"]},"focus_surface_evidence":{"arabic_uthmani":"وَٱلَّيْلِ إِذَا يَغْشَىٰهَا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:4:1:1","qac_word_ref":"91:4:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"91:4:1:2","qac_word_ref":"91:4:1","root_ar":"","surface_ar":"ٱلَّ"},{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:4:1:3","qac_word_ref":"91:4:1","root_ar":"ل ي ل","surface_ar":"يْلِ"},{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"91:4:2:1","qac_word_ref":"91:4:2","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"غَشِيَ","morph_features":"STEM|POS:V|IMPF|LEM:ga$iya|ROOT:g$w|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:4:3:1","qac_word_ref":"91:4:3","root_ar":"غ ش و","surface_ar":"يَغْشَىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:4:3:2","qac_word_ref":"91:4:3","root_ar":"","surface_ar":"هَا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["91:4:1:1"],["91:4:1:2","91:4:1:3"],["91:4:2:1"],["91:4:3:1","91:4:3:2"]],"word_analysis_refs":["91:4:1","91:4:2","91:4:3","91:4:4"],"word_rows":[{"analysis_record_ref":"91:4:1","analytic_gloss_range_en":"oath-coordinating particle before the genitive night noun; not a loose circumstantial or resumptive connector here","analytic_root_gloss_range_en":null,"qac_refs":["91:4:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"91:4:2","analytic_gloss_range_en":"the known recurring night, genitive as sworn object and reactivated as the covering subject","analytic_root_gloss_range_en":"night as the opposite of day and its darkness; night-oriented action and naming branches remain outside the local noun sense","qac_refs":["91:4:1:2","91:4:1:3"],"root":{"arabic":"ل ي ل","transliteration":"l-y-l"},"surface":{"arabic":"ٱلَّيْلِ","transliteration":"al-layli"}},{"analysis_record_ref":"91:4:3","analytic_gloss_range_en":"temporal particle setting the recurring when-clause for the covering action","analytic_root_gloss_range_en":null,"qac_refs":["91:4:2:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"إِذَا","transliteration":"idhā"}},{"analysis_record_ref":"91:4:4","analytic_gloss_range_en":"active imperfect covering with a feminine object suffix; locally concealment and envelopment, not every root branch as a translation sense","analytic_root_gloss_range_en":"covering, veiling, enveloping, coming upon, overwhelming, and intimate or other specialized branches; the local cosmic verb selects covering/envelopment while allowing bounded sensory pressure from overwhelm imagery","qac_refs":["91:4:3:1","91:4:3:2"],"root":{"arabic":"غ ش و","transliteration":"gh-sh-w"},"surface":{"arabic":"يَغْشَىٰهَا","transliteration":"yaghshāhā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["91:4"],"branch_refs":["root_001088/B001","root_001392/B001"],"candidate_id":"cand_28d7ca13aa39cff4604f","evidence_scope":"focus_ayah","hft_ref":"hft_406b80060b8e85d5e80a","item_id":"b01_surface_veil","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b01_surface_veil","support_id":"sup_2c8e1a17b0e5eb712e22"},{"anchor_refs":["91:4"],"branch_refs":["root_001088/B003","root_001089/B005","root_001392/B002"],"candidate_id":"cand_3ade8cf804882c5325bd","evidence_scope":"focus_ayah","hft_ref":"hft_92c529835c8361406b4c","item_id":"b02_arriving_night","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b02_arriving_night","support_id":"sup_8d9578dfc8fafdd6d9ef"},{"anchor_refs":["91:4"],"branch_refs":["root_001088/B002","root_001392/B001"],"candidate_id":"cand_daa2aa5b84e15b37ed6e","evidence_scope":"focus_ayah","hft_ref":"hft_939a730db00fa6efd390","item_id":"b03_total_overtaking","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b03_total_overtaking","support_id":"sup_8d96c944c734fc146032"}],"diagnostics":[],"lane_counts":{"global":12,"macro":12,"micro":3},"packet_summary":{"ayah_count":15,"focus_ref":"91:4","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ت ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000186","furuq_root_norm":"ت ل و","furuq_source_root_norm":"ت ل و","is_dominant":true,"target_occurrences":39,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000185","furuq_root_norm":"ت ل ل","furuq_source_root_norm":"ت ل ل","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["91:1","91:2","91:3","91:4","91:5","91:6","91:7","91:8","91:9","91:10","91:11","91:12","91:13","91:14","91:15"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"91:4","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":12,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"91:4","lane":"micro","linguistic_source_ref":"91:4","surface_ref":"91:4","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"91:4","target_tokens":[["Ve",["91:4:1"]],["onu",["91:4:3"]],["örttüğünde",["91:4:2","91:4:3"]],["geceye",["91:4:1"]]],"text":"Ve onu örttüğünde geceye,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":15,"id":"s091-p01-001-015","label":"Whole surah","number":1,"refs":["91:1","91:2","91:3","91:4","91:5","91:6","91:7","91:8","91:9","91:10","91:11","91:12","91:13","91:14","91:15"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:4:overwhelm-branch-limited","source_type":"word_analysis","support_id":"sup_03b7d4368c5589e85eb1","text":"{\"blocking_evidence\":null,\"headline\":\"overwhelm imagery bounded by cosmic context\",\"reader_payoff\":\"The reader feels the covering as forceful and sensory without mistaking the verse for a calamity title or sexual wording.\",\"reason\":\"V4 accepts branches for overwhelming affliction, fainting, and intimate covering, but local grammar selects a cosmic night subject and a covering object, so those branches are narrowed to contact-intensity and sensory force.\",\"representative_source_ids\":[\"QS-4be00210\",\"QS-cdb280b9\",\"QS-e4cc6324\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:2:series-and-later-echoes","source_type":"word_analysis","support_id":"sup_03bbda1e43ff20301dff","text":"{\"blocking_evidence\":null,\"headline\":\"local pair with wider echo pressure\",\"reader_payoff\":\"The reader notices that the night clause participates in a broader discourse pattern while the local oath sequence remains primary.\",\"reason\":\"The sun connection is local in 91:1-4, while the broader night-sun formula in 36:37-40 and the concealment echo toward 91:10 can be kept as secondary parallels rather than controlling the local parse.\",\"representative_source_ids\":[\"MT-14cfc25b\",\"MT-e6452747\",\"ME-a1b51051\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:3:entity-when-action-architecture","source_type":"word_analysis","support_id":"sup_061f5cffd7a07eedf065","text":"{\"blocking_evidence\":null,\"headline\":\"hinge from witness to action\",\"reader_payoff\":\"The reader sees the oath series presenting each cosmic witness at the moment that displays it.\",\"reason\":\"The local support identifies the repeated oath-refrain pattern, and the particle's position between noun and verb creates the same entity-when-action architecture in 91:2-4.\",\"representative_source_ids\":[\"QT-36c5e4b9\",\"QT-7cb24f90\",\"QE-211eef56\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:1:oath-chain-continuation","source_type":"word_analysis","support_id":"sup_12a0b5f1736cc0c0f814","text":"{\"blocking_evidence\":null,\"headline\":\"continued four-part oath chain\",\"reader_payoff\":\"The reader hears 91:4 as the next member of a repeated cosmic oath pattern rather than as an isolated verse opening.\",\"reason\":\"Attachment support identifies the near-verbatim oath refrain across the local sequence, and the CRITICAL rows align the opening particle with the repeated oath mechanism in 91:1-4.\",\"representative_source_ids\":[\"QS-0f3adb7e\",\"QI-b00442e2\",\"MT-b58963b5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:2:sound-texture","source_type":"word_analysis","support_id":"sup_2c4dbe65ced6359e435c","text":"{\"blocking_evidence\":null,\"headline\":\"heavy night-word texture\",\"reader_payoff\":\"The reader hears the night word as a compact, weighty entry into the covering scene.\",\"reason\":\"The local surface supports the assimilation and doubled-consonant observations, and the sound comments remain tied to the actual oath noun.\",\"representative_source_ids\":[\"QF-acafdb65\",\"QP-19aa3542\",\"QP-eabd48bd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:4:pronoun-ambiguity","source_type":"word_analysis","support_id":"sup_3047d08c15017aa7b8fb","text":"{\"blocking_evidence\":null,\"headline\":\"feminine object kept unresolved\",\"reader_payoff\":\"The reader notices that the covered object is deliberately carried by a feminine suffix whose discourse reach matters.\",\"reason\":\"Attachment evidence marks the object suffix as ambiguous and warns not to resolve it by default, so claims naming the sun, earth, or later feminine echoes are preserved only as layered reference pressure.\",\"representative_source_ids\":[\"QG-6b235002\",\"QG-bcfa7e06\",\"MS-70a732d5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:3:fixed-particle-sound-pivot","source_type":"word_analysis","support_id":"sup_310513ba486c7c9ba437","text":"{\"blocking_evidence\":null,\"headline\":\"rootless acoustic pivot\",\"reader_payoff\":\"The reader hears a small stop at the point where the oath noun turns into its action.\",\"reason\":\"QAC treats {{ar:إِذَا}} ({{tr:idhā}}) as a rootless temporal adverb, while the local surface supports the hamza-onset sound observation.\",\"representative_source_ids\":[\"QF-13e76813\",\"QF-bd15b258\",\"QP-18b783fe\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:1:oath-governance","source_type":"word_analysis","support_id":"sup_35660ebda69b6c629904","text":"{\"blocking_evidence\":null,\"headline\":\"qasam particle governs the night noun\",\"reader_payoff\":\"The reader notices that night enters as sworn evidence, not as a merely coordinated time marker.\",\"reason\":\"QAC marks {{ar:وَ}} ({{tr:wa}}) as a particle, and attachment evidence makes {{ar:ٱلَّيْلِ}} ({{tr:al-layli}}) its genitive oath complement, so the qasam reading is locally forced.\",\"representative_source_ids\":[\"QG-22c0afc2\",\"QG-7a730acb\",\"MG-444c7255\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:2:sworn-witness-as-agent","source_type":"word_analysis","support_id":"sup_35f8cc8f5e616a5a46ed","text":"{\"blocking_evidence\":null,\"headline\":\"oath object becomes coverer\",\"reader_payoff\":\"The reader sees night shift from named witness into the agent performing the clause's action.\",\"reason\":\"Attachment evidence licenses {{ar:ٱلَّيْلِ}} ({{tr:al-layli}}) as the subject of {{ar:يَغْشَىٰهَا}} ({{tr:yaghshāhā}}), matching the CRITICAL rows that make night both sworn object and covering agent.\",\"representative_source_ids\":[\"QG-6a0d57aa\",\"QG-ada0ca87\",\"QG-d370839d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:4","source_type":"word_analysis","support_id":"sup_3781c156e8ddeb983ed2","text":"{\"gloss_range\":\"active imperfect covering with a feminine object suffix; locally concealment and envelopment, not every root branch as a translation sense\",\"prose\":\"{{ar:يَغْشَىٰهَا}} ({{tr:yaghshāhā}}) compresses the whole scene into one final word: the masculine verbal subject points back to night, while the attached feminine suffix marks the covered patient. The suffix most naturally reaches back into the oath chain, with the sun of 91:1 and the prior revealed object in 91:3 exerting the strongest local pressure, but earth as the observer's field and the later feminine self (91:7) remain secondary reference pressure; the evidence warns against resolving the feminine object too narrowly. The imperfect active form makes the covering a recurring observed fact inside {{ar:إِذَا}} ({{tr:idhā}}), not a command, wish, passive state, or one completed nightfall. Lexically, {{ar:غ ش و}} ({{tr:gh-sh-w}}) gives the action more than chronological darkness: night comes over, veils, encloses, and obscures what had been disclosed. Wider branches such as overwhelming force, faintness, and intimate covering add contact-intensity only within that cosmic covering scene; they do not change the local translation into calamity or sexual language. The deep ghayn onset, hushing shīn, and open long vowel let the sound feel like a cover spreading over the field. The closing {{tr:-āhā}} sound binds the verb to 91:3's opposite disclosure, echoes the night-when-covering oath formula (92:1) while adding the local object suffix, and prepares the next feminine-suffix closure in 91:5, so grammar, sound, and meaning all make the night clause the recurring concealer of what day had revealed.\",\"root_display\":\"{{ar:غ ش و}} ({{tr:gh-sh-w}})\",\"root_gloss_range\":\"covering, veiling, enveloping, coming upon, overwhelming, and intimate or other specialized branches; the local cosmic verb selects covering/envelopment while allowing bounded sensory pressure from overwhelm imagery\",\"surface_display\":\"{{ar:يَغْشَىٰهَا}} ({{tr:yaghshāhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:4:agent-object-compression","source_type":"word_analysis","support_id":"sup_43d535108dc80d67272c","text":"{\"blocking_evidence\":null,\"headline\":\"night as agent, suffix as patient\",\"reader_payoff\":\"The reader sees the final word keep coverer and covered distinct without repeating either noun.\",\"reason\":\"Attachment evidence identifies the suffix on {{ar:يَغْشَىٰهَا}} ({{tr:yaghshāhā}}) as the direct object and licenses {{ar:ٱلَّيْلِ}} ({{tr:al-layli}}) as the subject, matching the CRITICAL role distinction.\",\"representative_source_ids\":[\"QG-14d8abc8\",\"QG-38b61e5a\",\"QG-e692d95e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:2:form-and-root-limit","source_type":"word_analysis","support_id":"sup_4b801daa2429e3938915","text":"{\"blocking_evidence\":null,\"headline\":\"singular form and derivational dispute bounded\",\"reader_payoff\":\"The reader keeps the lexical review caveat without losing the stable local reading of the known night.\",\"reason\":\"The alternative derivational note affects root analysis, but QAC and V4 still support the local definite night noun as the selected sense.\",\"representative_source_ids\":[\"QS-1bb34bf8\",\"QF-c24ab758\",\"QF-45980f63\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:4:opposition-and-cadence","source_type":"word_analysis","support_id":"sup_4f875b20f7478b8069f3","text":"{\"blocking_evidence\":null,\"headline\":\"same suffix cadence, opposite action\",\"reader_payoff\":\"The reader hears continuity in the ending while meaning pivots from disclosure to concealment.\",\"reason\":\"The local oath chain supplies the prior revealing clause in 91:3 and the following matched feminine-suffix closure in 91:5, so the CRITICAL sound-and-meaning reversal is locally anchored.\",\"representative_source_ids\":[\"QS-94cb48f0\",\"QE-ab0a94d2\",\"QB-be5520a1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:3","source_type":"word_analysis","support_id":"sup_5c87f7026f502165b01e","text":"{\"gloss_range\":\"temporal particle setting the recurring when-clause for the covering action\",\"prose\":\"{{ar:إِذَا}} ({{tr:idhā}}) turns the night oath into an entity-at-action frame: not night in abstraction, but night when it covers. With the imperfect verb, the particle points to a reliable recurring threshold, the whenever of nightfall rather than a single completed event or uncertain if. It also mediates the syntax: the noun is named first as the sworn witness, then this fixed rootless particle opens the verbal scene in which that witness acts. Its initial hamza gives that hinge a small articulated stop, so the turn from named night to acting night is heard as well as parsed.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِذَا}} ({{tr:idhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:2","source_type":"word_analysis","support_id":"sup_68f526662407868d7674","text":"{\"gloss_range\":\"the known recurring night, genitive as sworn object and reactivated as the covering subject\",\"prose\":\"{{ar:ٱلَّيْلِ}} ({{tr:al-layli}}) is definite and genitive, so the ayah invokes the familiar recurring night as an oath object, not one dated night or an adverbial by-night setting. The same referent then becomes the masculine subject of {{ar:يَغْشَىٰهَا}} ({{tr:yaghshāhā}}): the sworn witness is immediately shown doing its defining work. That keeps night from being a mere absence of sunlight; in this clause it is the active covering phase that answers the prior day-revealing scene of 91:3 and reaches back toward the sun oath of 91:1. As secondary pressure, the night-sun pairing belongs to a wider formula (36:37-40), and the cosmic concealment can later resonate with concealment of the self (91:10) without controlling the local parse. The assimilated article and doubled lām make the night noun enter with audible weight before the covering verb unfolds. The root note remains narrow: the local sense is the common night and its darkness, while the recorded derivational dispute affects morphology more than the ayah's oath function.\",\"root_display\":\"{{ar:ل ي ل}} ({{tr:l-y-l}})\",\"root_gloss_range\":\"night as the opposite of day and its darkness; night-oriented action and naming branches remain outside the local noun sense\",\"surface_display\":\"{{ar:ٱلَّيْلِ}} ({{tr:al-layli}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:2:definite-genitive-night","source_type":"word_analysis","support_id":"sup_a9372ce418eabb2c9da6","text":"{\"blocking_evidence\":null,\"headline\":\"known night as genitive oath object\",\"reader_payoff\":\"The reader notices that the oath invokes night as a familiar recurring class, not as a single dark episode.\",\"reason\":\"QAC and attachment evidence identify {{ar:ٱلَّيْلِ}} ({{tr:al-layli}}) as a definite genitive oath complement, and V4 keeps the local noun in the night-opposite-day branch.\",\"representative_source_ids\":[\"QG-54d16cc0\",\"QG-94b39b19\",\"QF-e2337c37\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:4:recurring-active-imperfect","source_type":"word_analysis","support_id":"sup_ae9ffb2b30a200d77b3c","text":"{\"blocking_evidence\":null,\"headline\":\"active imperfect recurrence\",\"reader_payoff\":\"The reader notices that the ayah witnesses a repeated cosmic action, not a command or a single past event.\",\"reason\":\"QAC marks the word as an imperfect active indicative verb with a suffix, and {{ar:إِذَا}} ({{tr:idhā}}) scopes that form as the recurring temporal event.\",\"representative_source_ids\":[\"QG-77137b8b\",\"QG-f3000304\",\"MG-115b0107\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:4:covering-envelopment","source_type":"word_analysis","support_id":"sup_ba1e59eb5bffaa76157e","text":"{\"blocking_evidence\":null,\"headline\":\"covering as spatial concealment\",\"reader_payoff\":\"The reader senses night as an enclosing concealment that changes visibility, not as mere sequence after day.\",\"reason\":\"V4's accepted covering branch for {{ar:غ ش و}} ({{tr:gh-sh-w}}) aligns with the local transitive verb and the night subject, so spatial and perceptual concealment are locally licensed.\",\"representative_source_ids\":[\"QS-26bff70b\",\"QS-28ff758f\",\"QS-f15c097b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:2:darkness-field","source_type":"word_analysis","support_id":"sup_bf94a072153025f133b0","text":"{\"blocking_evidence\":null,\"headline\":\"night as concealment field\",\"reader_payoff\":\"The reader notices that night is a reduced-visibility field, not just a point on a clock.\",\"reason\":\"V4's active branch for {{ar:ل ي ل}} ({{tr:l-y-l}}) includes night and its darkness, and the following covering verb locally realizes that darkness as perceptual concealment.\",\"representative_source_ids\":[\"QS-0bf567ea\",\"QS-1575b577\",\"QS-99181725\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:4:sound-texture","source_type":"word_analysis","support_id":"sup_c5c2bab9640149ec3804","text":"{\"blocking_evidence\":null,\"headline\":\"spreading sound texture\",\"reader_payoff\":\"The reader hears the covering action carried by the word's constricted onset and open final cadence.\",\"reason\":\"The sound observations remain tied to the actual local surface {{ar:يَغْشَىٰهَا}} ({{tr:yaghshāhā}}) and its shared final cadence.\",\"representative_source_ids\":[\"QP-08c293ad\",\"QP-818ced3c\",\"QP-bf279868\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"91:4:3:1","source_type":"qac_morpheme","support_id":"sup_cba603dc6bd6b73bcdfc","text":"{\"lemma_ar\":\"غَشِيَ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:ga$iya|ROOT:g$w|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"91:4:3:1\",\"qac_word_ref\":\"91:4:3\",\"root_ar\":\"غ ش و\",\"surface_ar\":\"يَغْشَىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:3:recurring-temporal-condition","source_type":"word_analysis","support_id":"sup_cdc52556cf8eface9b5e","text":"{\"blocking_evidence\":null,\"headline\":\"certain recurring when-clause\",\"reader_payoff\":\"The reader notices that the ayah is about night at its recurring covering phase, not about a hypothetical or one-time event.\",\"reason\":\"Attachment evidence makes {{ar:إِذَا}} ({{tr:idhā}}) the temporal adverbial for {{ar:يَغْشَىٰهَا}} ({{tr:yaghshāhā}}), and the imperfect verb supports a recurring condition.\",\"representative_source_ids\":[\"QG-2f51672f\",\"QS-751bb8ca\",\"MG-a668c194\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:1:bound-cadence","source_type":"word_analysis","support_id":"sup_e62571667aa7afeb28d1","text":"{\"blocking_evidence\":null,\"headline\":\"single-letter attached reset\",\"reader_payoff\":\"The reader notices how much syntactic and acoustic work is packed into the short attached particle.\",\"reason\":\"The particle has no lexical root here and the oath verb is formulaically unexpressed, so its bound position before the genitive noun carries the local force.\",\"representative_source_ids\":[\"QF-05ab84db\",\"QF-1bd5c7e7\",\"QP-0cf74c1d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:4:finite-active-form","source_type":"word_analysis","support_id":"sup_e70aec599308c904f481","text":"{\"blocking_evidence\":null,\"headline\":\"finite active verb over static noun\",\"reader_payoff\":\"The reader sees night itself doing the covering in motion, rather than an object merely lying covered.\",\"reason\":\"The local surface is a finite active verb with a direct object suffix, so the CRITICAL contrast with static covering nouns, passive forms, and causative paraphrase has a coherent local payoff.\",\"representative_source_ids\":[\"QF-93b398e0\",\"QF-9406d1a1\",\"MF-d78cc425\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"91:4:1:3","source_type":"qac_morpheme","support_id":"sup_e8a6b84d80685c2b040d","text":"{\"lemma_ar\":\"لَيْل\",\"morph_features\":\"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"91:4:1:3\",\"qac_word_ref\":\"91:4:1\",\"root_ar\":\"ل ي ل\",\"surface_ar\":\"يْلِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:2:day-night-reversal","source_type":"word_analysis","support_id":"sup_e99f6396acaddf58b03d","text":"{\"blocking_evidence\":null,\"headline\":\"night reverses the day disclosure\",\"reader_payoff\":\"The reader sees 91:4 as a semantic reversal of 91:3 rather than as one more time-word in a list.\",\"reason\":\"The local sequence places the night oath after the day-revealing clause of 91:3, while contextual evidence supports the familiar pairing of night with day and covering.\",\"representative_source_ids\":[\"QS-5a9f2773\",\"MI-86ed9988\",\"QE-0822a120\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:1","source_type":"word_analysis","support_id":"sup_faaebda87dcbc8b20def","text":"{\"gloss_range\":\"oath-coordinating particle before the genitive night noun; not a loose circumstantial or resumptive connector here\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) keeps 91:4 inside the oath sequence before the night noun is even heard. It is not merely an additive and; before the genitive {{ar:ٱلَّيْلِ}} ({{tr:al-layli}}), the particle renews qasam force and makes night the next sworn witness. Its small attached form also matters: the oath relation is compressed into one bound consonant, so the ayah crosses from the prior day clause into the night clause without breaking the formal oath frame.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:4:4:wider-formula-echo","source_type":"word_analysis","support_id":"sup_fdb7389fc0cfd5d1b1b8","text":"{\"blocking_evidence\":null,\"headline\":\"night-when-covering formula\",\"reader_payoff\":\"The reader recognizes the local wording as part of a broader formula where night is characterized by covering.\",\"reason\":\"Contextual evidence supports close night-covering association, and the CRITICAL row's echo with 92:1 is valid as a formulaic parallel while the local suffix remains distinctive.\",\"representative_source_ids\":[\"QI-bd3322a3\",\"QE-e4d1e9c4\",\"ME-e7267590\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلَّيْلِ إِذَا يَغْشَىٰهَا","ayah_ref":"91:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001088/B001","root_001392/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001392","role":"Night as the dark opposite of day supplies the temporal-dark layer and serves as the covering agent.","root":"ل ي ل","source_ref":"91:4","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001088","role":"A veil laid over and concealing something supplies the contact geometry and makes the verb an external overlay on -hā.","root":"غ ش و","source_ref":"91:4","source_word_indices":["3"]}],"changed_reading":{"after":"Night is an agentive veil that advances over and withholds a feminine field from view.","before":"Night coincides with an otherwise unspecified darkening."},"confidence":"strong","focus_anchor":"The construction ٱلَّيْلِ ... يَغْشَىٰهَا makes night the agent of a transitive action upon an unspecified feminine object.","mechanism":"Night's darkness behaves as a moving upper layer: when its phase arrives, it overlays the pronominal field and restricts access to it without yet implying damage or permanence.","model_id":"b01_surface_veil"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b01_surface_veil","source_type":"hft","support_id":"sup_2c8e1a17b0e5eb712e22","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلَّيْلِ إِذَا يَغْشَىٰهَا","ayah_ref":"91:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001088/B003","root_001089/B005","root_001392/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001392","role":"Entering or undertaking something by night turns the temporal noun into an enacted phase rather than a passive background.","root":"ل ي ل","source_ref":"91:4","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_001088","role":"Coming to or frequenting a target supplies the approach relation and lets night arrive upon -hā.","root":"غ ش و","source_ref":"91:4","source_word_indices":["3"]},{"branch_id":"B005","mapped_root_id":"root_001089","role":"The non-dominant mapped inventory independently preserves visiting or habitual arrival and keeps the encounter reading live.","root":"غ ش و","source_ref":"91:4","source_word_indices":["3"]}],"changed_reading":{"after":"Night itself comes upon the object like a recurring visitor whose arrival effects the cover.","before":"To cover is only to place darkness over an object."},"confidence":"medium","focus_anchor":"The same verb in يَغْشَىٰهَا can describe coming upon a person or place, while ٱلَّيْلِ can name entry into nocturnal activity.","mechanism":"The clause can stage an encounter rather than a static screen: night enters, comes upon, or visits the pronominal object as an event with approach and contact.","model_id":"b02_arriving_night"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b02_arriving_night","source_type":"hft","support_id":"sup_8d9578dfc8fafdd6d9ef","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلَّيْلِ إِذَا يَغْشَىٰهَا","ayah_ref":"91:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001088/B002","root_001392/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001392","role":"Night's darkness supplies the medium capable of filling the field.","root":"ل ي ل","source_ref":"91:4","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001088","role":"An enveloping event that overtakes people supplies total scope and raises covering from placement to seizure.","root":"غ ش و","source_ref":"91:4","source_word_indices":["3"]}],"changed_reading":{"after":"Night overtakes the entire referential field as an encompassing event.","before":"Night places a bounded veil over something."},"confidence":"exploratory","focus_anchor":"The verb يَغْشَىٰهَا admits an event that envelops and overtakes, while night supplies the expanding dark medium.","mechanism":"The scale of covering enlarges from a surface veil to a total event: night takes the whole field, temporarily leaving no exterior vantage within it.","model_id":"b03_total_overtaking"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b03_total_overtaking","source_type":"hft","support_id":"sup_8d96c944c734fc146032","trust":"legacy_unbound"}]}
</lane_packet_json>
