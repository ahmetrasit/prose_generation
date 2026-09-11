# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **101:8**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s101-regular-20260911/s101/101_8/micro.discovery.json` and modify nothing
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
  "ayah_ref": "101:8",
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
{"analysis_context":{"analysis_id":"s101-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"101:8","host_surah":101,"lane_context_refs":[],"ordered_context_refs":["101:0","101:1","101:2","101:3","101:4","101:5","101:6","101:7","101:9","101:10","101:11","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, yalın ağırlık azlığını ve ondan türeyen kullanımları birlikte kapsar; söz ve secde örnekleri yalnız kendi bağlamlarında geçerlidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000427/B001","candidate_links":[{"candidate_id":"cand_0184ba9741ba8cb92b16","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَفَّتْ","morph_features":"STEM|POS:V|PERF|LEM:xaf~ato|ROOT:xff|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:8:3:1","qac_word_ref":"101:8:3","surface_ar":"خَفَّتْ"}],"gloss":"ağırlığın veya yükün az olması ve azaltılması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin ağırlığı veya taşıdığı yük, ağır olma durumuna göre azdır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir nesnenin ya da yükün ağırlığı azaltılabilir ve taşıması daha kolay duruma getirilebilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişinin durumu, yükü veya eşyası az güç gerektirecek ölçüde kolaylaşabilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Sözün dilde kolay akması ve secdede bedeni denetimsizce ağır bırakmama, çekirdeğin özel bağlamlardaki uygulamalarıdır."}}],"root_ar":"خ ف ف","root_id":"root_000427","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın fiziksel çekirdeği ile yük ve durum kolaylığını birlikte anlatan genel karşılıktır.","boundary_detail":"Dal, yalın ağırlık azlığını ve ondan türeyen kullanımları birlikte kapsar; söz ve secde örnekleri yalnız kendi bağlamlarında geçerlidir.","branch_image_ar":"خفة الثقل والحمل","concept_gloss":"ağırlığın veya yükün az olması ve azaltılması","contextual_glosses":[{"applicability":"Bir nesnenin ya da yükün önceye veya bir karşıta göre daha az ağır olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir başkasının ağırlığı azaltması ile söz ve secdeye özgü kullanımları kapsamaz.","preserves":"Ağırlık azalması çekirdeğini doğal bir eylem olarak korur."},"facet_ids":["F001"],"text":"ağırlığı azalmak","usage_role":"general"},{"applicability":"Taşınan yükün veya kişinin üstündeki güçlüğün azaltıldığı geçişli bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kendiliğinden ağırlık azlığını ve sözün dilde kolay akmasını dışarıda bırakır.","preserves":"Bir yükü daha az ağır ve daha kolay taşınır kılmayı korur."},"facet_ids":["F002","F003"],"text":"yükünü azaltmak","usage_role":"contextual"},{"applicability":"Yalnız sözün söyleniş bakımından dilde rahatça aktığı bağlam için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Fiziksel ağırlık, yük ve azaltma anlamlarını taşımaz.","preserves":"Sözün söylenişindeki kolaylığı ve akıcılığı korur."},"facet_ids":["F004"],"text":"dile kolay gelmek","usage_role":"contextual"}],"definition":"Bir şeyin ağırlığının, yükünün veya taşınma güçlüğünün az olması ya da bunların azaltılmasıdır. Durumun kolaylaşması, eşyanın kolay taşınması, sözün dilde rahat akması ve secdede bedeni ağır bırakmama bu çekirdeğin bağlama bağlı uzantılarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin ağırlığı veya taşıdığı yük, ağır olma durumuna göre azdır."},{"facet_id":"F002","role":"core","statement":"Bir nesnenin ya da yükün ağırlığı azaltılabilir ve taşıması daha kolay duruma getirilebilir."},{"facet_id":"F003","role":"extension","statement":"Kişinin durumu, yükü veya eşyası az güç gerektirecek ölçüde kolaylaşabilir."},{"facet_id":"F004","role":"associated_use","statement":"Sözün dilde kolay akması ve secdede bedeni denetimsizce ağır bırakmama, çekirdeğin özel bağlamlardaki uygulamalarıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kişi veya hak hakkında olumsuz bir değer yargısı ekler.","collision":"Küçümseme ve aşağılama dalıyla karışır.","fit":"displacement","loses":"Ağırlık, yük, taşıma kolaylığı ve azaltma çekirdeğini bütünüyle kaybeder.","preserves":"Azlık düşüncesini değer alanına taşıyan uzak bir çağrışımı korur."},"text":"değersiz saymak"}],"identity_rationale":"Yetkili ifade, bir şeyin ağırlığının veya yükünün azalmasını çekirdek alır; bir şeyi daha az ağır kılma, yük ve durum kolaylığı, eşyanın taşınabilirliği, sözün dilde kolay akması ve secdede bedeni ağır bırakmama kullanımlarını bu çekirdeğe bağlar. Bu nedenle dalın fiziksel ağırlıkla sınırlanmaması, ancak küçümseme, düşüncesiz davranış ya da ayak giysisi anlamlarıyla da karıştırılmaması gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ağırlığı azalmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"az ağırlıklı, taşıması kolay"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"ağırlık, yük veya güçlük azlığı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ağırlığını azaltmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yükünü azaltmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"ağırlığı az bulmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"durumu kolaylaşıp yükü azalmak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"taşınması kolay eşya"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"dile kolay gelen söz"}],"lexicalization_note":"Yalın ağırlık azlığı ile türemiş biçimler birlikte ele alınır; sözün dilde kolay akması ve secde kullanımı bütün dala genellenmez.","neighbor_coverage_note":"Adayların tümü değerlendirildi; ağır yükü karşı kutupta gösteren iki dal ile nicelik azlığını ayıran kardeş dal en açıklayıcı karşılaştırmalar olarak seçildi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dalı ağırlığın düşük ya da azaltılmış kutbunda, komşu dal ise taşıyıcıya yük olan ağır kutuptadır.","focus_only":"Odak dalı ağırlığın azlığını veya azaltılmasını anlatır.","gloss":"az ağırlık ve ağır yük","neighbor_only":"Komşu dal sırtta, başta ya da başka bir taşıyıcıda bulunan ağır yükü anlatır.","neighbor_ref":"root_001674/B002","relation_type":"polarity_pair","shared_zone":"İki dal da taşınan şeyin ağırlığını ve yük olma niteliğini konu edinir."},{"boundary_match":"opposed","distinction":"Odak dalı güçlüğün azalmasını, komşu dal ise ağırlığın taşıyanı büken baskısını öne çıkarır.","focus_only":"Odak dalında yük azdır veya azaltılarak taşıma kolaylaştırılır.","gloss":"kolaylaşan ve büken yük","neighbor_only":"Komşu dalda yük, sahibini eğecek ve zorlayacak ölçüde ağırlaşır.","neighbor_ref":"root_000066/B002","relation_type":"polarity_pair","shared_zone":"Her iki dal bir yükün taşıyan üzerindeki ağırlık etkisini değerlendirir."},{"boundary_match":"partial","distinction":"Odak dalı taşıma ve ağırlık niteliğine, komşu dal ise sayı ya da ölçü miktarının azlığına dayanır.","focus_only":"Odak dalı nesne, yük ve durum bakımından ağırlık azlığını merkez alır.","gloss":"ağırlık azlığı ve nicelik azlığı","neighbor_only":"Komşu dal topluluk sayısının, kalabalığın veya tartıdaki nicel payın azlığını merkez alır.","neighbor_ref":"root_000427/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal bir ölçünün düşük oluşunu anlatabildiği için tartı bağlamında yaklaşır."}],"source_phrase_ar":"خف الشيء يخف خفة وهو خفيف (maqayis;sihah)؛ الخفة خفة الوزن وخفة الحال (ayn;tahdhib)؛ التخفيف ضد التثقيل واستخفه خلاف استثقله (sihah)؛ خففه تخفيفا وتخفف تخففا وخف المتاع وكلام خفيف على اللسان (mufradat)؛ خفوا في السجود ولا ترسل نفسك إرسالا ثقيلا (tahdhib)","source_summary":"Kanıtlar ağırlık azlığını ortak çekirdek olarak verir; azaltma işlemini, yük ve durum kolaylığını, taşınabilir eşyayı, dilde kolay sözü ve secdedeki ölçülü beden hareketini buna bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه خف الشيء وخفة الوزن والحال والحمل والمتاع والكلام والتخفيف ضد التثقيل وترك الإرسال الثقيل في السجود","what_is_not_ar":"لا يدخل فيه الخُفّ الملبوس ولا الخفخفة الصوتية ولا خفة الطيش والاستهانة إلا بقرينة"},"support_links":["sup_588f2e617ee9e4c86ffd"]},{"boundary":"Hızlı ayrılış çekirdektir; hızlı binekler ve hızlı deve kuşu bu çekirdeğin taşıyıcıya bağlı özel gerçekleşmeleridir.","branch_kind":"bare","branch_ref":"root_000427/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَفَّتْ","morph_features":"STEM|POS:V|PERF|LEM:xaf~ato|ROOT:xff|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:8:3:1","qac_word_ref":"101:8:3","surface_ar":"خَفَّتْ"}],"gloss":"hızla yola çıkmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluk bulunduğu konak yerinden hızlı ve çevik biçimde ayrılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Topluluğun binekleri, hızlı yol almaya elverişli ve süratlidir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hızlı koşan deve kuşu, hareket süratinin canlıya yüklenen bir örneğidir."}}],"root_ar":"خ ف ف","root_id":"root_000427","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir topluluğun konak yerinden süratle ayrılışını veren doğal ve kısa genel karşılıktır.","boundary_detail":"Hızlı ayrılış çekirdektir; hızlı binekler ve hızlı deve kuşu bu çekirdeğin taşıyıcıya bağlı özel gerçekleşmeleridir.","branch_image_ar":"خفة السير والارتحال","concept_gloss":"hızla yola çıkmak","contextual_glosses":[{"applicability":"Bir topluluğun konak yerini topluca ve süratle terk ettiği göç bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Göç sayılmayan hızlı ayrılışları ve canlı niteliği kullanımlarını kapsamaz.","preserves":"Topluca hızlı ayrılış ve yer değiştirme çekirdeğini korur."},"facet_ids":["F001"],"text":"hızla göçmek","usage_role":"contextual"},{"applicability":"Topluluğun süratinin kullandığı bineklerin çevikliğine bağlandığı bağlam için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Topluluğun konaktan ayrılması ile başka hızlı canlı örneklerini dışarıda bırakır.","preserves":"Hareket süratini bineklerin niteliği üzerinden açıklar."},"facet_ids":["F002"],"text":"binekleri hızlı olmak","usage_role":"explanatory"},{"applicability":"Yalnız süratiyle nitelenen deve kuşunu adlandıran özel kullanımda geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Topluluğun ayrılışı ve bineklerin sürati anlamlarını taşımaz.","preserves":"Canlının hızlı hareket etmesi özelliğini açıkça korur."},"facet_ids":["F003"],"text":"hızlı deve kuşu","usage_role":"contextual"}],"definition":"Bir topluluğun konak yerinden çevik ve hızlı biçimde ayrılıp yola çıkmasıdır. Bineklerin hızlı olması ve hızlı deve kuşu, bu hareket niteliğinin canlıya bağlı özel görünümleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluk bulunduğu konak yerinden hızlı ve çevik biçimde ayrılır."},{"facet_id":"F002","role":"specialization","statement":"Topluluğun binekleri, hızlı yol almaya elverişli ve süratlidir."},{"facet_id":"F003","role":"example","statement":"Hızlı koşan deve kuşu, hareket süratinin canlıya yüklenen bir örneğidir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Yavaş, uzun veya konak ayrılışı içermeyen her türlü yolculuğu kapsar.","collision":"Genel yolculuk ve ülkede dolaşma dallarıyla karışabilir.","fit":"broadening","loses":"Konaktan süratli ve çevik biçimde ayrılma koşulunu belirginleştirmez.","preserves":"Bir yerden ayrılıp yol alma düşüncesini genel düzeyde korur."},"text":"seyahat etmek"}],"identity_rationale":"Yetkili ifade, topluluğun konak yerinden hızlı ve çevik biçimde ayrılmasını temel alır; bineklerin hızlı oluşunu ve hızlı deve kuşunu buna bağlı gerçekleşmeler olarak verir. Dal yalnız genel yolculuğu değil, ayrılışın süratini ve hareket kolaylığını içerdiği için mevcut çerçeve kanıtla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"topluluk hızla yola çıktı"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"konaktan hızlı ayrılış, yola çıkma vakti"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"topluluğun binekleri hızlıydı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"hızlı deve kuşu"}],"lexicalization_note":"Dal yalın hızlı ayrılış anlamıyla tanımlanır; belirli bir araç, yol türü veya özel söz kalıbı çekirdeğe eklenmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel yola koyuluş, şiddetli yol alış ve fiziksel ağırlık azlığı odak dalın hız ile ayrılış sınırını en iyi görünür kılan üç karşılıktır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında konaktan ayrılma sürati kurucudur; komşu dalda yönelip ilerlemek yeterlidir.","focus_only":"Odak dalı konak yerinden hızlı ve çevik ayrılışı zorunlu kılar.","gloss":"hızlı ayrılış ve genel yola koyuluş","neighbor_only":"Komşu dal yönelme, yolculuğa başlama ve ülkede ilerlemeyi hız veya eğim şartı olmadan kapsar.","neighbor_ref":"root_000862/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir yerden ayrılarak yola koyulma olayında örtüşür."},{"boundary_match":"partial","distinction":"Odak dalı ayrılışın çevikliğine, komşu dal ise sürmekte olan yol alışın şiddetine odaklanır.","focus_only":"Odak dalı bir topluluğun konak yerinden ayrılışını ve hızlı canlıları da kapsar.","gloss":"hızlı ayrılmak ve sert yol almak","neighbor_only":"Komşu dal belirli bir başlangıç yeri olmadan yol almanın şiddetini anlatır.","neighbor_ref":"root_000654/B007","relation_type":"near_synonym","shared_zone":"Her iki dal süratli yol alma ve güçlü hareket alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dalında gerçekleşen hızlı hareket kurucudur; komşu dalda hareket olmadan da ağırlık az olabilir.","focus_only":"Odak dalı süratli ayrılış ve hareket kolaylığını olay olarak anlatır.","gloss":"çevik hareket ve az ağırlık","neighbor_only":"Komşu dal nesnenin, yükün veya durumun ağırlık bakımından az olmasını anlatır.","neighbor_ref":"root_000427/B001","relation_type":"near_neighbor","shared_zone":"Ağırlık azlığı hızlı ve kolay harekete elverişlilik çağrışımı doğurur."}],"source_phrase_ar":"خف القوم ارتحلوا (maqayis)؛ الخفوف سرعة السير من المحلة وحان الخفوف وخف القوم إذا ارتحلوا مسرعين (ayn;tahdhib)؛ أخف القوم إذا كانت دوابهم خفافا (sihah)؛ خفوا عن منازلهم ارتحلوا منها في خفة (mufradat)؛ الخفانة النعامة السريعة (ayn)","source_summary":"Kanıtlar hızlı ayrılıp yola çıkmayı ortak çekirdek olarak sunar; hızlı binekleri ve hızlı deve kuşunu bu hareket niteliğinin özel taşıyıcıları olarak ekler.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه سرعة السير من المنزل وارتحال القوم مسرعين وخفة الدواب والنعامة السريعة","what_is_not_ar":"لا يدخل فيه قلة العدد ولا الخُفّ الملبوس ولا الطاعة المجردة"},"support_links":[]},{"boundary":"Dal sayı, kalabalık veya ölçülen pay azlığıyla sınırlıdır; nesnenin taşınma ağırlığı ya da hızlı hareket bu sınıra girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000427/B003","candidate_links":[{"candidate_id":"cand_54d2564bd0c21a5d557d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَفَّتْ","morph_features":"STEM|POS:V|PERF|LEM:xaf~ato|ROOT:xff|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:8:3:1","qac_word_ref":"101:8:3","surface_ar":"خَفَّتْ"}],"gloss":"sayısı veya ölçülen payı az olmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir toplulukta bulunan kişi sayısı azdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir yerdeki kalabalık veya sıkışıklık nicel olarak azalır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tartıyla gösterilen payın azlığı, ölçülen iyi işlerin az olmasına işaret eder."}}],"root_ar":"خ ف ف","root_id":"root_000427","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Topluluk, kalabalık ve tartıyla gösterilen nicelik alanlarını birlikte kapsayan genel karşılıktır.","boundary_detail":"Dal sayı, kalabalık veya ölçülen pay azlığıyla sınırlıdır; nesnenin taşınma ağırlığı ya da hızlı hareket bu sınıra girmez.","branch_image_ar":"قلة المقدار والعدد","concept_gloss":"sayısı veya ölçülen payı az olmak","contextual_glosses":[{"applicability":"Bir topluluğun üyeleri veya bir yerdeki insanlar sayıca az olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tartıyla gösterilen payın ve kalabalık yoğunluğunun özel anlatımlarını kapsamaz.","preserves":"Topluluğun nicel azlığını açık ve doğal biçimde korur."},"facet_ids":["F001"],"text":"sayıca az olmak","usage_role":"general"},{"applicability":"Bir yerdeki insan yoğunluğunun veya sıkışıklığın azaldığı bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel topluluk sayısını ve tartıyla ölçülen payı kapsamaz.","preserves":"Kalabalığın nicel olarak gerilemesini ve seyrelmesini korur."},"facet_ids":["F002"],"text":"kalabalığı azalmak","usage_role":"contextual"},{"applicability":"Kişinin iyi işlerinin tartıyla gösterilen payının düşük olduğu değerlendirme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Topluluk sayısı ve kalabalık azlığı kullanımlarını dışarıda bırakır.","preserves":"Tartıdaki düşüklüğün ölçülen iyi işlerin azlığı olduğunu açıklar."},"facet_ids":["F003"],"text":"ölçülen iyilikleri az gelmek","usage_role":"explanatory"}],"definition":"Bir topluluğun sayısının, bir yerdeki kalabalığın veya tartıyla gösterilen payın az olmasıdır. Tartı bağlamında az olan, kişinin ölçülen iyi işlerinin miktarıdır; nesnenin yalnızca az ağır olması değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir toplulukta bulunan kişi sayısı azdır."},{"facet_id":"F002","role":"extension","statement":"Bir yerdeki kalabalık veya sıkışıklık nicel olarak azalır."},{"facet_id":"F003","role":"specialization","statement":"Tartıyla gösterilen payın azlığı, ölçülen iyi işlerin az olmasına işaret eder."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Nesnenin fiziksel olarak kolay taşınması anlamını ekler.","collision":"Fiziksel ağırlık azlığı dalıyla karışır.","fit":"displacement","loses":"Kişi sayısı, kalabalık ve ölçülen iyi işlerin niceliği anlamlarını kaybeder.","preserves":"Tartıda düşük görünme çağrışımını yüzeysel olarak korur."},"text":"ağırlığı az olmak"}],"identity_rationale":"Yetkili ifade, insan topluluğunun ve kalabalığın azlığını tartıdaki miktar azlığıyla aynı nicel çekirdekte birleştirir. Tartı örneğinde söz konusu olan yalnız fiziksel ağırlık değil, iyi işlerin ölçülen payının azlığıdır; bu ayrım mevcut dalı ağırlık dalından bağımsız tutar.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"topluluğun sayısı azaldı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kalabalıkları azaldı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"arkadaşlarından küçük bir topluluk içinde"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ölçülen iyi işleri az geldi"}],"lexicalization_note":"Yalın sayı azlığı ile kalabalık ve tartıya bağlı söz kalıpları ayrıştırılır; tartı kullanımı genel fiziksel ağırlık anlamına genişletilmez.","neighbor_coverage_note":"Bütün nicelik adayları değerlendirildi; genel az miktar, eksilme süreci ve yığılmış çokluk odak dalın sayı ile ölçülen pay sınırını en açık biçimde belirledi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı belirli sayım ve ölçüm alanlarına bağlıdır; komşu dal daha genel bir azlık niteliğidir.","focus_only":"Odak dalı özellikle topluluk sayısını, kalabalığı ve tartıyla ölçülen payı kapsar.","gloss":"sayısal azlık ve genel az miktar","neighbor_only":"Komşu dal herhangi bir şeyin ya da sürenin küçük miktarını genel olarak anlatır.","neighbor_ref":"root_001694/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir miktarın küçük veya yetersiz oluşunu bildirir."},{"boundary_match":"partial","distinction":"Odak dalı önceki miktara göre değişim gerektirmez; komşu dalda kayıp veya azalma ilişkisi kurucudur.","focus_only":"Odak dalı mevcut sayı veya ölçünün düşük olma durumunu anlatır.","gloss":"az olma ve eksilme","neighbor_only":"Komşu dal bir şeyin bir bölümünün gitmesiyle ortaya çıkan eksilme sürecini ve sonucunu anlatır.","neighbor_ref":"root_001542/B001","relation_type":"near_neighbor","shared_zone":"Eksilme sonunda kalan miktar az olabileceği için iki anlam sonuç düzeyinde yaklaşır."},{"boundary_match":"opposed","distinction":"Odak dalı düşük sayı ve seyrekliği, komşu dal ise birikmiş çokluk ve sıkışıklığı gösterir.","focus_only":"Odak dalı topluluğun veya ölçülen payın azlığını bildirir.","gloss":"azlık ve yığılmış çokluk","neighbor_only":"Komşu dal insanların ya da malın üst üste yığılacak ölçüde çok ve yoğun oluşunu bildirir.","neighbor_ref":"root_001340/B002","relation_type":"polarity_pair","shared_zone":"Her iki dal insan veya mal miktarının nicel yoğunluğunu değerlendirir."}],"source_phrase_ar":"خرج فلان في خف من أصحابه أي في جماعة قليلة وخف القوم خفوفا أي قلوا وقد خفت زحمتهم (sihah)؛ فمن خفت موازينه إشارة إلى كثرة الأعمال الصالحة وقلتها (mufradat)","source_summary":"Kanıt, azlığı kişi sayısı ve kalabalık üzerinden gösterir; tartı ifadesinde ise ölçülen iyi işlerin payının düşük oluşunu aynı nicel çerçeveye yerleştirir.","sources":["SI","MU"],"what_is_ar":"يدخل فيه قلة الجماعة والزحام وقلة المقدار في الميزان","what_is_not_ar":"لا يدخل فيه الارتحال المسارع ولا خفة الحمل من جهة الوزن وحدها"},"support_links":["sup_f95bd775dbe5f04e5483"]},{"boundary":"Kurucu ortaklık zihinsel veya duygusal kararlılığın kolayca bozulmasıdır; küçümseme ve fiziksel ağırlık azlığı bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000427/B004","candidate_links":[{"candidate_id":"cand_2d8539be5f688a08342c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَفَّتْ","morph_features":"STEM|POS:V|PERF|LEM:xaf~ato|ROOT:xff|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:8:3:1","qac_word_ref":"101:8:3","surface_ar":"خَفَّتْ"}],"gloss":"kararlılığını yitirip ölçüsüzce yönelmek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi işinde düşüncesiz, ölçüsüz ve kararsız davranır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi çabuk coşan ve duygusal hareketliliğe kolay kapılan bir yapı gösterir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sevinç kişiyi yerinden oynatıp bir işe hevesle yöneltebilir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir etken kişiyi sarsarak yerleşik görüşünden veya kararından uzaklaştırabilir."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Bir yönlendirici, kişinin bilgisizliğini kullanıp onu kendi yanlış yolunun peşine takabilir."}}],"root_ar":"خ ف ف","root_id":"root_000427","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Düşüncesizlik, duygusal hareketlenme ve dış etkiyle yön değiştirme çekirdeğini birlikte taşıyan genel karşılıktır.","boundary_detail":"Kurucu ortaklık zihinsel veya duygusal kararlılığın kolayca bozulmasıdır; küçümseme ve fiziksel ağırlık azlığı bu dala girmez.","branch_image_ar":"خفة الطيش والاضطراب","concept_gloss":"kararlılığını yitirip ölçüsüzce yönelmek","contextual_glosses":[{"applicability":"Kişinin işinde ölçüyü ve sağduyuyu korumadan davrandığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Duygusal coşmayı, karardan sarsılmayı ve başkasınca yanlış yola sürüklenmeyi kapsamaz.","preserves":"Düşüncesiz ve ölçüsüz davranış çekirdeğini doğal biçimde korur."},"facet_ids":["F001"],"text":"düşünmeden davranmak","usage_role":"general"},{"applicability":"Sevincin kişiyi hareketlendirip bir işe hevesle yönelttiği özel bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel düşüncesizlik ile dış etki sonucu görüş değiştirmeyi kapsamaz.","preserves":"Sevincin doğurduğu güçlü hareketlenme ve coşmayı korur."},"facet_ids":["F002","F003"],"text":"sevinçten yerinde duramamak","usage_role":"contextual"},{"applicability":"Bir etkenin kişiyi yerleşik görüş veya kararından uzaklaştırdığı geçişli bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin kendi düşüncesizliğini ve sevinçle hareketlenmesini dışarıda bırakır.","preserves":"Dış etkinin kişide kararlılık kaybı oluşturmasını korur."},"facet_ids":["F004","F005"],"text":"kararından saptırmak","usage_role":"contextual"}],"definition":"Kişinin düşünce veya duygu bakımından kararlılığını kolayca yitirip ölçüsüz davranması ya da hızla coşmasıdır. Bir etkenin onu yerleşik görüşünden oynatması veya bilgisizliğinden yararlanarak yanlış bir yönelişe sürüklemesi bu çekirdeğin ettirgen gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi işinde düşüncesiz, ölçüsüz ve kararsız davranır."},{"facet_id":"F002","role":"specialization","statement":"Kişi çabuk coşan ve duygusal hareketliliğe kolay kapılan bir yapı gösterir."},{"facet_id":"F003","role":"associated_use","statement":"Sevinç kişiyi yerinden oynatıp bir işe hevesle yöneltebilir."},{"facet_id":"F004","role":"extension","statement":"Bir etken kişiyi sarsarak yerleşik görüşünden veya kararından uzaklaştırabilir."},{"facet_id":"F005","role":"extension","statement":"Bir yönlendirici, kişinin bilgisizliğini kullanıp onu kendi yanlış yolunun peşine takabilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Karşıdakinin değerini düşük görme yargısını ekler.","collision":"Aşağılama ve hakka değer vermeme dalıyla karışır.","fit":"displacement","loses":"Düşüncesizlik, coşma, kararlılık kaybı ve yanlış yola sürüklenme çekirdeğini kaybeder.","preserves":"Bir kişiye yönelik olumsuz tutum çağrışımını sınırlı biçimde korur."},"text":"küçümsemek"}],"identity_rationale":"Yetkili ifade düşüncesiz ve dengesiz davranışı, çabuk coşmayı, sevinçle yerinden oynamayı, birini yerleşik inancından uzaklaştırmayı ve bilgisizliğinden yararlanarak yanlış yola sürüklemeyi aynı kararlılık kaybı çevresinde toplar. Geçici duygu hareketi ile kasıtlı yönlendirme aynı olay değildir; bu yüzden dal korunabilir, ancak bu kullanımlar çekirdeğe bağlı ayrı gerçekleşmeler olarak gösterilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kişinin düşüncesiz ve ölçüsüz davranması"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"çabuk coşan, yerinde duramayan"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"sevinç onu hareketlendirdi"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"seni kararından oynatmasın"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bilgisizliğini kullanıp yanlış yola sürükledi"}],"lexicalization_note":"Kişinin düşüncesizliği ile sevinç, sarsma ve yanlış yola sürükleme kalıpları ayrı tutulur; yapıya bağlı ettirgen anlamlar yalın kişilik niteliğine genellenmez.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; sağduyu karşıtı mizaç, genel sarsılma ve öfkeli taşkınlık odak dalın karar ile yöneliş merkezini en iyi ayıran karşılaştırmalardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı belirli etkilerle hareketlenme veya görüşten sapmayı, komşu dal daha genel bir sağduyu ve dinginlik yokluğunu öne çıkarır.","focus_only":"Odak dalı sevinçle hareketlenmeyi ve kişiyi yerleşik görüşünden saptırmayı açıkça kapsar.","gloss":"kolay yön değiştirme ve dengesiz mizaç","neighbor_only":"Komşu dal dinginliğin karşıtı olan mizaç bozukluğunu ve bir işi hakkına aykırı yapmayı daha genel verir.","neighbor_ref":"root_000271/B002","relation_type":"near_synonym","shared_zone":"İki dal düşüncesizlik, iç kararsızlık ve bilgisizlik üzerinden yönlendirilmeyi paylaşır."},{"boundary_match":"partial","distinction":"Odak dalı zihinsel ve davranışsal ölçüsüzlüğe bağlıdır; komşu dal fiziksel yer değiştirmeye kadar uzanan genel bir sarsma alanıdır.","focus_only":"Odak dalı düşüncesiz davranış, sevinçle coşma ve yanlış yönelişe ikna edilmeyi kapsar.","gloss":"zihinsel kararsızlık ve genel sarsılma","neighbor_only":"Komşu dal korkutma, çağırma veya yerinden çıkarma gibi fiziksel ve duygusal sarsmaları daha geniş kapsar.","neighbor_ref":"root_001151/B001","relation_type":"near_synonym","shared_zone":"Her iki dal kişinin yerleşik durumunun bozulup kolayca harekete geçirilmesinde örtüşür."},{"boundary_match":"partial","distinction":"Odak dalı karar ve davranışın kolayca yön değiştirmesine, komşu dal öfke ve taşkın uyarılmaya dayanır.","focus_only":"Odak dalında görüşten sapma ve başkasının yanlış yoluna uyma bulunur.","gloss":"ölçüsüz yöneliş ve öfkeli taşkınlık","neighbor_only":"Komşu dal öfke, keskinlik ve insan ya da hayvandaki taşkın uyarılmayı kapsar.","neighbor_ref":"root_000962/B005","relation_type":"near_synonym","shared_zone":"İki dal hızlı duygusal uyarılma ve denetimin zayıflaması alanında buluşur."}],"source_phrase_ar":"وخفة الرجل طيشه وخفته في عمله (ayn;tahdhib)؛ خفيف القلب في توقده فهو خفاف (ayn;tahdhib)؛ الخفيف فيمن يطيش (mufradat)؛ لا يستخفنك أي لا يزعجنك ويزيلنك عن اعتقادك (mufradat)؛ استخفه الفرح إذا ارتاح لأمر (tahdhib)؛ استخفه فلان إذا استجهله فحمله على اتباعه في غيه (tahdhib)","source_summary":"Kanıtlar düşüncesiz davranış ve çabuk coşma çekirdeğini, sevinçle hareketlenme, karardan sarsılma ve bilgisizlik üzerinden yanlış yola yöneltilme gibi farklı sonuçlarla birlikte verir.","sources":["AY","TA","MU"],"what_is_ar":"يدخل فيه طيش الرجل وخفته في العمل وخفة القلب واضطراب الفرح والإزعاج والإزالة عن الاعتقاد والاستجهال الذي يحمل على الغي","what_is_not_ar":"لا يدخل فيه الاستهانة بالحق ولا خفة الوزن والحمل إلا بقرينة"},"support_links":["sup_374aea94482de53dc43a"]},{"boundary":"Dal, kişi veya hakkı değersiz görüp gereğini yerine getirmemeyle sınırlıdır; düşüncesizce yönlendirme ya da yalnız alay etme değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000427/B005","candidate_links":[{"candidate_id":"cand_cfaa52bd10fb9aa72630","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَفَّتْ","morph_features":"STEM|POS:V|PERF|LEM:xaf~ato|ROOT:xff|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:8:3:1","qac_word_ref":"101:8:3","surface_ar":"خَفَّتْ"}],"gloss":"aşağılayıp değersiz saymak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi değeri düşük görülerek aşağılanır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birine ait hak değersiz sayılır ve gereği önemsenmez."}}],"root_ar":"خ ف ف","root_id":"root_000427","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem doğrudan kişiye hem de onun hakkına yönelen değer düşürücü tutumu kapsayan genel karşılıktır.","boundary_detail":"Dal, kişi veya hakkı değersiz görüp gereğini yerine getirmemeyle sınırlıdır; düşüncesizce yönlendirme ya da yalnız alay etme değildir.","branch_image_ar":"الاستخفاف إهانة واستهانة","concept_gloss":"aşağılayıp değersiz saymak","contextual_glosses":[{"applicability":"Değer düşürücü tutumun doğrudan bir kişiye yöneldiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir hakka değer vermeme biçimindeki özel kullanımı kapsamaz.","preserves":"Kişiye yönelen onur kırıcı ve değer düşürücü davranışı korur."},"facet_ids":["F001"],"text":"onu aşağılamak","usage_role":"general"},{"applicability":"Bir kişinin hakkının gereğini yerine getirmeye değer görülmediği bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin doğrudan aşağılanmasını tek başına ifade etmez.","preserves":"Hakkı değersiz görme ve ona gereken önemi vermeme tutumunu korur."},"facet_ids":["F002"],"text":"hakkını önemsememek","usage_role":"contextual"}],"definition":"Bir kişiyi aşağılamak veya ona ait hakkı değersiz sayarak gereğini önemsememektir. Tutum doğrudan kişiye de, korunması gereken hakka da yönelebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi değeri düşük görülerek aşağılanır."},{"facet_id":"F002","role":"specialization","statement":"Birine ait hak değersiz sayılır ve gereği önemsenmez."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Gülme, taklit veya sözlü eğlence yoluyla yergi unsurunu ekler.","collision":"Alay ve başkasına gülme dalıyla karışır.","fit":"displacement","loses":"Alay içermeyen aşağılama ile bir hakkı değersiz sayma kapsamını kaybeder.","preserves":"Karşıdakini küçültücü bir tutum sergileme yönünü korur."},"text":"alay etmek"}],"identity_rationale":"Yetkili ifade bir kişiyi aşağılamayı ve onun hakkını önemsememeyi aynı değer düşürme tutumunda birleştirir. Biri doğrudan kişiye, diğeri kişiye ait hakka yönelse de ikisinde de muhataba gereken değerin verilmemesi kurucudur; mevcut çerçeve bunu doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"onu aşağılayıp değersiz saydı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"hakkımı önemsemedi"}],"lexicalization_note":"Kişiyi aşağılayan kullanım ile hakka değer vermeme kalıbı ayrı gösterilir; bu iki yapıdan genel ağırlık azlığı anlamı çıkarılmaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; genel ayıplama, değer düşürme ve alay dalları, odak dalın kişi ile hakka yönelen değersiz sayma sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında değersiz sayma tutumu yeterlidir; komşu dal buna ayıp bulma, kınama ve azarlama yollarını da ekler.","focus_only":"Odak dalı özellikle kişiyi aşağılamayı ve onun hakkına değer vermemeyi kapsar.","gloss":"değersiz sayma ve ayıplayarak düşürme","neighbor_only":"Komşu dal ayıplama, azarlama, kusur bulma ve değerden düşürme eylemlerini daha geniş kapsar.","neighbor_ref":"root_000632/B001","relation_type":"near_synonym","shared_zone":"İki dal bir kişi veya şeyi değersiz görme ve saygınlığını düşürme alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dalının hakka yönelen belirli bir kullanımı vardır; komşu dal daha genel bir değer düşürme eylemidir.","focus_only":"Odak dalı kişiye yönelik aşağılama ile hakka değer vermemeyi birlikte içerir.","gloss":"aşağılamak ve değerini düşürmek","neighbor_only":"Komşu dal genel olarak değerini düşürme veya hor gösterme eylemini bildirir.","neighbor_ref":"root_000414/B006","relation_type":"near_synonym","shared_zone":"Her iki dal birinin değerini düşüren olumsuz değerlendirmeyi paylaşır."},{"boundary_match":"partial","distinction":"Odak dalı değer vermemeye, komşu dal ise gülme veya yergi yoluyla alaya dayanır.","focus_only":"Odak dalında alay veya gülme olmadan da kişi ya da hak değersiz sayılabilir.","gloss":"değersiz saymak ve alay etmek","neighbor_only":"Komşu dal başkasını gülünç kılma ve onunla eğlenme davranışını kurucu kılar.","neighbor_ref":"root_000685/B003","relation_type":"near_neighbor","shared_zone":"İki dal muhatabı küçülten ve saygınlığını zedeleyen tutumlarda buluşur."}],"source_phrase_ar":"استخف به أهانه (sihah)؛ استخف فلان بحقي إذا استهان به (tahdhib)","source_summary":"Kanıtlar kişiyi aşağılamayı ve onun hakkına değer vermemeyi, muhatabın değerini veya hak iddiasının ağırlığını reddeden ortak bir tutumda birleştirir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه استخف به إذا أهانه واستخف بحقه إذا استهان به","what_is_not_ar":"لا يدخل فيه الاستجهال الذي يحمل على الغي ولا خفة الوزن"},"support_links":["sup_88ccbdfc18ccc7ec8393"]},{"boundary":"Deve ayağı, insan ayak giysisi, benzetmeli hayvan ayağı ve yarıştaki deve adlandırması ayrıdır; fiziksel ağırlık azlığı bu dala katılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000427/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَفَّتْ","morph_features":"STEM|POS:V|PERF|LEM:xaf~ato|ROOT:xff|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:8:3:1","qac_word_ref":"101:8:3","surface_ar":"خَفَّتْ"}],"gloss":"deve ayağı ucu veya kapalı ayak giysisi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ad, devenin tırnak bölümlerinin birleştiği ayak ucunu belirtir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı ad, insan ayağına giyilen ve sandaldan daha kalın veya kapalı olan ayak giysisini belirtir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Deve ve deve kuşunun ayak ucu, insanın ayak giysisine benzetilerek aynı adla anılır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yarış bağlamında ayak ucunu taşıyan hayvan adı üzerinden develer kastedilir."}}],"root_ar":"خ ف ف","root_id":"root_000427","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın iki temel nesne alanını açıkça ayıran ve benzetmeli uzantılara temel sağlayan genel karşılıktır.","boundary_detail":"Deve ayağı, insan ayak giysisi, benzetmeli hayvan ayağı ve yarıştaki deve adlandırması ayrıdır; fiziksel ağırlık azlığı bu dala katılmaz.","branch_image_ar":"الخُفّ والقدم الملبوسة","concept_gloss":"deve ayağı ucu veya kapalı ayak giysisi","contextual_glosses":[{"applicability":"Devenin yere basan ve tırnak bölümlerini bir araya getiren ayak kısmı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsanın ayak giysisini, deve kuşu benzetmesini ve yarıştaki ad aktarmasını kapsamaz.","preserves":"Deveye özgü anatomik ayak ucu anlamını açıklar."},"facet_ids":["F001"],"text":"devenin tabanlı ayak ucu","usage_role":"explanatory"},{"applicability":"İnsanın ayağına giydiği, sandaldan daha kapalı veya kalın giysi kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvan ayağı ile yarıştaki deve adlandırmasını dışarıda bırakır.","preserves":"İnsan ayağına giyilen nesnenin temel işlevini ve biçim ayrımını korur."},"facet_ids":["F002"],"text":"kapalı ayak giysisi","usage_role":"general"},{"applicability":"Yarışta ayak yapısı üzerinden develerin kastedildiği ad aktarmalı kullanımda geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ayak ucunun anatomik anlamını ve insanın giydiği nesneyi kapsamaz.","preserves":"Yarış bağlamında hayvan türünü ad aktarmasıyla belirtme işlevini korur."},"facet_ids":["F004"],"text":"deve türünden yarış hayvanı","usage_role":"contextual"}],"definition":"Devenin tırnak bölümlerinin birleştiği ayak ucu ile insanın ayağına giydiği, sandaldan daha kalın veya kapalı ayak giysisi için kullanılan ortak addır. Ad, benzetmeyle deve kuşu ayağına ve yarış bağlamında deveye de aktarılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ad, devenin tırnak bölümlerinin birleştiği ayak ucunu belirtir."},{"facet_id":"F002","role":"core","statement":"Aynı ad, insan ayağına giyilen ve sandaldan daha kalın veya kapalı olan ayak giysisini belirtir."},{"facet_id":"F003","role":"extension","statement":"Deve ve deve kuşunun ayak ucu, insanın ayak giysisine benzetilerek aynı adla anılır."},{"facet_id":"F004","role":"associated_use","statement":"Yarış bağlamında ayak ucunu taşıyan hayvan adı üzerinden develer kastedilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"At ve benzeri hayvanların sert tırnaklı ayaklarıyla karışabilir.","fit":"narrowing","loses":"İnsan ayak giysisini, yarıştaki deve adlandırmasını ve deve ayağının özel birleşik yapısını kaybeder.","preserves":"Hayvanın yere basan ayak ucunu genel olarak korur."},"text":"toynak"}],"identity_rationale":"Yetkili ifade devenin tırnak bölümlerinin birleştiği ayak ucunu, insanın ayağına giydiği kapalı ayak giysisini, deve kuşu ve deve ayağına benzetmeli adlandırmayı ve yarışta develeri gösteren kullanımı aynı dalda toplar. Bunlar tek bir anatomik nesne değildir; dal, ayak ucu ile ayak giysisi arasındaki geleneksel benzetme ve bundan doğan ad aktarması açık tutulursa korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"devenin tabanlı ayak ucu"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"ayağa giyilen kapalı ayak giysisi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"sandaldan daha kalın ayak giysisi"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"deve türünden yarış hayvanı"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"deve veya deve kuşunun ayak ucu"}],"lexicalization_note":"Anatomik ad, giyilen nesne ve yarışa bağlı ad aktarması ayrı yüzeyler olarak korunur; söz kalıpları bütün dala tek bir nesne anlamı vermez.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; deve ayağının alt bölümü, koruyucu ayak giysisi ve at toynağı, anatomik ad ile giyilen nesne arasındaki sınırı en yararlı biçimde açar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı daha geniş ayak ucunu ve başka anlamları içerir; komşu dal bunun alt iç yüzündeki belirli bölümdür.","focus_only":"Odak dalı devenin bütün tabanlı ayak ucunu, insan ayak giysisini ve bunların uzantılarını kapsar.","gloss":"deve ayağı ucu ve taban içi","neighbor_only":"Komşu dal yalnız deve ayağının tabanında, tırnak altına bitişik iç yüzü belirtir.","neighbor_ref":"root_000966/B007","relation_type":"near_neighbor","shared_zone":"İki dal devenin yere basan ayak yapısının bölümlerini konu edinir."},{"boundary_match":"partial","distinction":"Odak dalında nesnenin geleneksel adı ve hayvan ayağı benzetmesi kurucudur; komşu dal koruma işlevine dayanır.","focus_only":"Odak dalı belirli bir ayak giysisi türünü ve hayvan ayağı adını içerir.","gloss":"ayak giysisi ve koruyucu tabanlık","neighbor_only":"Komşu dal ayağın veya hayvan ayağının altını taş ve zeminden koruyan giysi ile giydirme işlevini merkez alır.","neighbor_ref":"root_001524/B001","relation_type":"near_neighbor","shared_zone":"İki dal ayağın altını örten ve zemine karşı koruyan giyilebilir nesnelerde örtüşür."},{"boundary_match":"field_only","distinction":"Odak dalı deveye özgü ayak yapısına ve giysi benzetmesine, komşu dal at türündeki sert toynağa bağlıdır.","focus_only":"Odak dalı deve ve deve kuşunun ayak ucuyla insan ayak giysisini kapsar.","gloss":"deve ayağı ve at toynağı","neighbor_only":"Komşu dal at ve benzeri hayvanların zeminde iz bırakan sert ayak ucunu belirtir.","neighbor_ref":"root_000341/B002","relation_type":"same_field","shared_zone":"İki dal farklı hayvan türlerinin yere basan ayak uçlarını adlandırır."}],"source_phrase_ar":"الخف مجمع فرسن البعير (ayn;tahdhib)؛ الخف ما يلبسه الإنسان (ayn;tahdhib)؛ الخف واحد أخفاف البعير والخف واحد الخفاف التي تلبس والخف في الأرض أغلظ من النعل (sihah)؛ الخف فمن الباب لأن الماشي يخف وهو لابسه وخف البعير منه أيضا (maqayis)؛ الخف الملبوس وخف النعامة والبعير تشبيها بخف الإنسان (mufradat)؛ لا سبق إلا في خف أو نصل أو حافر فالخف الإبل ها هنا (tahdhib)","source_summary":"Kanıtlar deve ayağının birleşik ucunu ve insanın kapalı ya da kalın ayak giysisini birlikte verir; benzetmeyi hayvan ayağına, ad aktarmasını da yarıştaki develere uzatır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه خف البعير ومجمع فرسنه والخف الذي يلبسه الإنسان والخف في الأرض وتشبيه خف النعامة والبعير بخف الإنسان وذو الخف في السبق","what_is_not_ar":"لا يدخل فيه خفة الوزن ولا الخفخفة الصوتية"},"support_links":[]},{"boundary":"Dal, uyma ve boyun eğme davranışını kapsar; hazır ve çevik katılım yalnız geçişli topluluk kullanımının açıklamasıdır, salt düşüncesizlik ve küçümseme ise bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000427/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَفَّتْ","morph_features":"STEM|POS:V|PERF|LEM:xaf~ato|ROOT:xff|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:8:3:1","qac_word_ref":"101:8:3","surface_ar":"خَفَّتْ"}],"gloss":"uyup boyun eğmek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi başkasına uyar ve onun yönlendirmesine boyun eğer."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişi eşeklerin erkek eşeğe uyması, canlılar arasındaki yönelişin özel örneğidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir önder topluluğunu kendisiyle birlikte davranmaya yöneltebilir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Aynı geçişli kullanım, topluluğun bedence ve kararlılıkça hazır bulunup öndere uyması biçiminde de açıklanır."}}],"root_ar":"خ ف ف","root_id":"root_000427","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişi ve hayvan örneklerindeki itaat çekirdeğini karşılar; hazır ve çevik katılım yalnız topluluğa ilişkin kaynak açıklamasında geçerlidir.","boundary_detail":"Dal, uyma ve boyun eğme davranışını kapsar; hazır ve çevik katılım yalnız geçişli topluluk kullanımının açıklamasıdır, salt düşüncesizlik ve küçümseme ise bu dala girmez.","branch_image_ar":"الخفوف للطاعة والانقياد","concept_gloss":"uyup boyun eğmek","contextual_glosses":[{"applicability":"Bir kişinin başka birinin yönlendirmesine uyduğu ve ona boyun eğdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Birlikte çevik hareket etme ve topluluğu buna yöneltme açıklamalarını tam taşımaz.","preserves":"Uyma ve yönlendiriciye boyun eğme çekirdeğini korur."},"facet_ids":["F001"],"text":"ona uyup boyun eğmek","usage_role":"general"},{"applicability":"Bir önderin topluluğunu kendisiyle birlikte çevik davranmaya yönelttiği geçişli bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Topluluğu zaten hazır bulma açıklamasını ve yalın uyma kullanımını kapsamaz.","preserves":"Önderin topluluğu birlikte davranmaya yöneltmesi bileşenini korur."},"facet_ids":["F003"],"text":"onunla birlikte harekete geçirmek","usage_role":"contextual"},{"applicability":"Topluluğun bedence ve kararlılıkça hazır bulunmasının uyma sonucuyla birlikte anlatıldığı açıklamada kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvan örneğini ve doğrudan harekete geçirme yorumunu kapsamaz.","preserves":"Hazır bulma ile öndere uyma sonucunu birlikte açıklar."},"facet_ids":["F004"],"text":"hazır bulup kendine uydurmak","usage_role":"explanatory"}],"definition":"Bir kimseye veya yönlendiriciye uyup onun yönlendirmesine boyun eğmektir. Geçişli kullanımda önder, topluluğunu kendisiyle birlikte davranmaya yöneltir veya onları bedence ve kararlılıkça buna hazır bulur; ardından topluluk ona uyar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi başkasına uyar ve onun yönlendirmesine boyun eğer."},{"facet_id":"F002","role":"example","statement":"Dişi eşeklerin erkek eşeğe uyması, canlılar arasındaki yönelişin özel örneğidir."},{"facet_id":"F003","role":"extension","statement":"Bir önder topluluğunu kendisiyle birlikte davranmaya yöneltebilir."},{"facet_id":"F004","role":"source_variant","statement":"Aynı geçişli kullanım, topluluğun bedence ve kararlılıkça hazır bulunup öndere uyması biçiminde de açıklanır."}],"identity_rationale":"Yetkili ifade birine uyup boyun eğmeyi, dişi eşeklerin erkeğe uymasını ve bir önderin topluluğunu kendisiyle birlikte davranmaya yöneltmesini verir. Son kullanım için topluluğu bedence ve kararlılıkça hazır bulma açıklaması da sunulur; bu hazır ve çevik katılım, yalın itaat kullanımlarına genellenmemesi gereken kaynak varyantıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"ona uyup boyun eğdi"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"dişi eşekler erkek eşeğe uydu"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"hizmetine çevikçe koştu"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"topluluğunu kendisiyle birlikte harekete geçirip kendine uydurdu"}],"lexicalization_note":"Kişiye uyma, hayvanın eşine uyma ve topluluğu birlikte hareket ettirme yapıları ayrı tutulur; hizmete koşma yalnız kendi söz biriminin anlamıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel boyun eğme, gönüllü kabul ve anlayıp uygulama dalları, odak dalın istekli çeviklik ile birlikte hareket etme sınırını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı kişi, hayvan ve topluluğa bağlı özel yapıları verir; komşu dal buyruğa uyma ve kolay yönetilme çevresindeki daha genel itaat alanıdır.","focus_only":"Odak dalı belirli bir kişiye uyma, dişi eşeklerin erkeğe uyması ve topluluğun önderle birlikte harekete geçirilmesi yüzeylerini kapsar.","gloss":"belirli uyma yüzeyleri ve genel boyun eğme","neighbor_only":"Komşu dal buyruğa uyma, söz dinleme ve el ya da dizgin altında kolay yönetilme gibi genel durumları kapsar.","neighbor_ref":"root_000956/B001","relation_type":"near_synonym","shared_zone":"İki dal bir yönlendiricinin sözüne veya hareketine uyup onun ardından gitmeyi paylaşır."},{"boundary_match":"partial","distinction":"Odak dalı kişi, hayvan ve topluluğa bağlı uyma yapılarını verir; komşu dal boyun eğme, itaatte hız ve kolay yönetilebilirliğe dayanır.","focus_only":"Odak dalı bir başkasına uyma ve topluluğu onunla birlikte davranmaya yöneltme yüzeylerini kapsar.","gloss":"birlikte davranmaya uyma ve genel boyun eğme","neighbor_only":"Komşu dal boyun eğme, kolay yönlendirilme ve itaatte hızlı davranmayı daha genel biçimde kapsar.","neighbor_ref":"root_000514/B001","relation_type":"near_synonym","shared_zone":"İki dal boyun eğme ve yönlendirmeye karşılık verme alanında güçlü biçimde örtüşür."},{"boundary_match":"partial","distinction":"Odak dalı uyma ve birlikte davranmayı, komşu dal ise sözü kavrama veya kabul etmeden doğan uygulamayı merkez alır.","focus_only":"Odak dalında önceden anlama koşulu olmadan uyma ve topluluğun önderle birlikte davranması öne çıkar.","gloss":"uyma ve anlayıp yerine getirme","neighbor_only":"Komşu dal sözü anlamayı veya kabul etmeyi ve ardından gereğini yapmayı kurucu kılar.","neighbor_ref":"root_000741/B003","relation_type":"near_neighbor","shared_zone":"İki dal bir kişinin yönlendirmeyi kabul edip davranışını ona göre düzenlemesinde buluşur."}],"source_phrase_ar":"خف فلان لفلان إذا أطاعه وانقاد له وخفت الأتن لعيرها إذا أطاعته (tahdhib)؛ استخف قومه فأطاعوه أي حملهم أن يخفوا معه أو وجدهم خفافا في أبدانهم وعزائمهم (mufradat)","source_summary":"Kanıtlar uyma ve boyun eğme çekirdeğini kişi ve hayvan örnekleriyle verir; topluluğun uyumunu ise önderin onları harekete geçirmesi veya bedence ve kararlılıkça hazır bulması biçiminde iki açıklamayla sunar.","sources":["TA","MU"],"what_is_ar":"يدخل فيه خف فلان لفلان إذا أطاعه وانقاد وخفت الأتن لعيرها وحمل القوم على أن يخفوا معه","what_is_not_ar":"لا يدخل فيه الطيش المجرد ولا الاستخفاف بالحق"},"support_links":[]},{"boundary":"Anlam develerin birbirini izleyen düzenine bağlıdır; bağlanmış olma şart değildir ve ifade tek bir ayak nesnesini göstermez.","branch_kind":"collocation","branch_ref":"root_000427/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَفَّتْ","morph_features":"STEM|POS:V|PERF|LEM:xaf~ato|ROOT:xff|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:8:3:1","qac_word_ref":"101:8:3","surface_ar":"خَفَّتْ"}],"gloss":"develerin birbirini izleyerek art arda gelmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Develer birbirini izleyerek birbiri ardınca gelir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu art arda geliş, develer birbirine bağlanmışken de bağlanmamışken de gerçekleşebilir."}}],"root_ar":"خ ف ف","root_id":"root_000427","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız verilen yapı içinde develerin tek bir izleme düzeni oluşturduğu durumu karşılar.","boundary_detail":"Anlam develerin birbirini izleyen düzenine bağlıdır; bağlanmış olma şart değildir ve ifade tek bir ayak nesnesini göstermez.","branch_image_ar":"الإبل على خف واحد","concept_gloss":"develerin birbirini izleyerek art arda gelmesi","contextual_glosses":[{"applicability":"Develerin biri ötekinin ardından aynı geliş düzenini sürdürdüğü anlatı bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Develerin birbirini izleyen art arda gelişini doğal cümle içinde korur."},"facet_ids":["F001","F002"],"text":"develer peş peşe geldi","usage_role":"general"},{"applicability":"Develerin bağlanma durumundan bağımsız olarak birbirini izlediğinin özellikle açıklanması gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İzleme düzenini ve bağlı olmanın gerekli olmayışını açıkça korur."},"facet_ids":["F001","F002"],"text":"bağlı ya da bağsız tek sıra ilerlemek","usage_role":"explanatory"}],"definition":"Develerin, birbirine bağlanmış olsun veya olmasın, birinin ardından öteki gelecek biçimde art arda ilerlemesidir. Anlam, develerin oluşturduğu izleme düzenine bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Develer birbirini izleyerek birbiri ardınca gelir."},{"facet_id":"F002","role":"specialization","statement":"Bu art arda geliş, develer birbirine bağlanmışken de bağlanmamışken de gerçekleşebilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Yan yana, dağınık veya toplu biçimde gelen her türlü hayvan kümesini kapsar.","collision":"Genel sürü ve topluluk hareketi anlatımlarıyla karışır.","fit":"broadening","loses":"Develerin birbirini tek tek izlemesi ve bağlılığın önemsiz oluşu koşullarını belirsizleştirir.","preserves":"Birden çok hayvanın birlikte gelişini genel olarak korur."},"text":"sürü halinde gelmek"}],"identity_rationale":"Yetkili ifade yalnız develerin birbirini izleyerek art arda gelmesini anlatır ve bağlı olup olmamalarının sonucu değiştirmediğini açıkça belirtir. Mevcut çerçeve bu yapı koşulunu koruduğu ve genel hızlı yol alma ya da tek bir deve ayağı anlamına genişlemediği için kabul edilebilir.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"develerin birbirini izlediği tek sıra halinde"}],"lexicalization_note":"Tanım yalnız verilen yapıda develerin art arda gelişi için geçerlidir; yalın köke veya bütün sıralı hareketlere genellenmez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; aynı izde ardışıklık, insanları da kapsayan izleme ve daha geniş sıra düzeni, yapıya bağlı deve dizisinin sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı yalnız deve dizisine ve belirli yapıya bağlıdır; komşu dal aynı ardışıklığı başka olaylara da uzatır.","focus_only":"Odak dalı develerin bağlı veya bağsız olarak birbirini izlemesini belirli bir yapıda anlatır.","gloss":"deve sırası ve genel ardışıklık","neighbor_only":"Komşu dal develerin iz üzerindeki sıralanmasına ek olarak doğumların art arda gelişini de kapsar.","neighbor_ref":"root_000762/B012","relation_type":"near_synonym","shared_zone":"İki dal develerin biri ötekinin ardından aynı izleme düzeninde ilerlemesini paylaşır."},{"boundary_match":"partial","distinction":"Odak dalı hayvan türü ve yapı bakımından daha dardır; komşu dal insanlara ve gidiş yönüne de açılır.","focus_only":"Odak dalı yalnız develeri ve bağlı olup olmama karşıtlığını belirtir.","gloss":"develerin sırası ve aynı izden gitmek","neighbor_only":"Komşu dal develerle birlikte insan topluluklarını ve aynı yoldan geliş ya da gidişi kapsar.","neighbor_ref":"root_000932/B009","relation_type":"near_synonym","shared_zone":"İki dal develerin birbiri ardınca aynı yönde ilerlemesinde örtüşür."},{"boundary_match":"partial","distinction":"Odak dalı tek bir deve dizisine bağlıdır; komşu dal sıra kurma düşüncesini farklı topluluk ve işlemlere genişletir.","focus_only":"Odak dalı bağlı olsun olmasın develerin birbirini izlemesini tek olay olarak verir.","gloss":"birbirini izleyen develer ve düzenli dizi","neighbor_only":"Komşu dal düzenli kervanı, grupların aralıklı gelişini, mahkumların bağlanmasını ve satış sıralarını da kapsar.","neighbor_ref":"root_001238/B004","relation_type":"near_synonym","shared_zone":"İki dal develerin belirli bir sıra ve düzen içinde art arda gelmesini paylaşır."}],"source_phrase_ar":"جاءت الإبل على خف واحد إذا تبع بعضها بعضا مقطورة كانت أو غير مقطورة (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tekil tanıklık, birbirine bağlı ve bağlı olmayan develeri aynı art arda geliş düzenine dahil eder."}],"source_summary":"Kanıt, develerin birbirini izleyerek art arda gelmesini açıkça tanımlar ve bu düzenin hayvanların birbirine bağlanmasına bağlı olmadığını belirtir.","sources":["TA"],"what_is_ar":"يدخل فيه مجيء الإبل متتابعة يتبع بعضها بعضا مقطورة أو غير مقطورة","what_is_not_ar":"لا يدخل فيه الخُفّ المفرد ولا سرعة السير العامة"},"support_links":[]},{"boundary":"Dal belirli sesleri ve kanat çırpan kuş adını kapsar; ağırlık azlığı, ayak giysisi ve sessiz kanat hareketi bu sınıra girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000427/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَفَّتْ","morph_features":"STEM|POS:V|PERF|LEM:xaf~ato|ROOT:xff|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:8:3:1","qac_word_ref":"101:8:3","surface_ar":"خَفَّتْ"}],"gloss":"köpek sesi veya giysi hışırtısı; kanat çırparak uçan kuş","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli köpek sesleri bu ses adıyla anılır."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yeni bir gömlek hareket ettirildiğinde çıkan hışırtı aynı ses alanında adlandırılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Uçarken kanatlarını çırpan bir kuş, bu belirgin uçuş davranışı üzerinden adlandırılır."}}],"root_ar":"خ ف ف","root_id":"root_000427","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın iki ses yüzeyi ile uçuş davranışına dayalı kuş adını birbirine karıştırmadan gösteren açıklayıcı karşılıktır.","boundary_detail":"Dal belirli sesleri ve kanat çırpan kuş adını kapsar; ağırlık azlığı, ayak giysisi ve sessiz kanat hareketi bu sınıra girmez.","branch_image_ar":"خفخفة الصوت والحركة","concept_gloss":"köpek sesi veya giysi hışırtısı; kanat çırparak uçan kuş","contextual_glosses":[{"applicability":"Ses adının doğrudan köpeklerin çıkardığı ses için kullanıldığı bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Giysi hışırtısını ve kanat çırparak uçan kuş adını kapsamaz.","preserves":"Köpek sesine özgü temel adlandırmayı açıkça korur."},"facet_ids":["F001"],"text":"köpeklerin çıkardığı ses","usage_role":"explanatory"},{"applicability":"Yeni gömleğin hareket ettirilmesiyle duyulan ses anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Köpek sesini ve kanat çırpan kuşun adlandırılmasını dışarıda bırakır.","preserves":"Giysinin hareketinden doğan özel hışırtıyı korur."},"facet_ids":["F002"],"text":"yeni gömleğin hışırtısı","usage_role":"contextual"},{"applicability":"Kuşun uçuş biçimi üzerinden adlandırıldığı söz birimi için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Köpek sesi ile yeni gömlek hışırtısını kapsamaz.","preserves":"Kuşu ve uçarken kanatlarını çırpma davranışını birlikte korur."},"facet_ids":["F003"],"text":"kanatlarını çırparak uçan kuş","usage_role":"explanatory"}],"definition":"Dal, köpeklerin çıkardığı ses adını ve yeni bir gömlek hareket ettirilince duyulan hışırtıyı kapsar. Ayrıca kanatlarını çırparak uçan bir kuş bu davranış üzerinden adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli köpek sesleri bu ses adıyla anılır."},{"facet_id":"F002","role":"example","statement":"Yeni bir gömlek hareket ettirildiğinde çıkan hışırtı aynı ses alanında adlandırılır."},{"facet_id":"F003","role":"extension","statement":"Uçarken kanatlarını çırpan bir kuş, bu belirgin uçuş davranışı üzerinden adlandırılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Genel yaprak, kumaş veya nesne sürtünmesi sesleriyle karışabilir.","fit":"narrowing","loses":"Köpek sesini ve kanat çırparak uçan kuşun adlandırılmasını kaybeder.","preserves":"Yeni giysinin hareketinden çıkan sürtünmeli sesi iyi karşılar."},"text":"hışırtı"}],"identity_rationale":"Yetkili ifade köpeklerin sesini, yeni gömleğin hareket ettirilince çıkardığı sesi ve uçarken kanatlarını çırpan bir kuşun adını birlikte verir. Bunların hepsi tek bir hareket sesi değildir; köpek sesi ayrı bir ses türüdür, kuş adı ise kanat çırpma davranışına dayalı adlandırmadır. Dal bu üç yüzey ayrıştırıldığı sürece korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"köpeklerin çıkardığı ses"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"yeni gömleği hareket ettirip hışırtı çıkarmak"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"kanatlarını çırparak uçan kuş"}],"lexicalization_note":"Köpek sesi, yeni giysinin hareket sesi ve kanat çırparak uçan kuş ayrı yüzeylerdir; kuş adı genel bir ses veya hareket fiiline dönüştürülmez.","neighbor_coverage_note":"Bütün ses ve kuş adayları değerlendirildi; genel hareket hışırtısı, daha geniş hareket uğultusu ve kanat hareketi, dalın belirli kaynaklarla sınırlı ses alanını en iyi ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı belirli köpek, gömlek ve kuş yüzeylerine bağlıdır; komşu dal hareket eden birçok kaynağın genel hışırtısıdır.","focus_only":"Odak dalı köpek sesini ve kanat çırpan kuş adını, giysi hışırtısıyla birlikte kapsar.","gloss":"özel ses kümesi ve genel hareket hışırtısı","neighbor_only":"Komşu dal ağaç, kanat, at, yağmur ve ateş gibi birçok kaynağın hareket hışırtısını genel olarak kapsar.","neighbor_ref":"root_000343/B002","relation_type":"near_synonym","shared_zone":"İki dal kanat veya nesne hareketinden doğan hışırtılı seslerde örtüşür."},{"boundary_match":"partial","distinction":"Odak dalı sınırlı kaynaklara ve bir kuş adına bağlıdır; komşu dal çok çeşitli hareket kaynaklarının ses alanıdır.","focus_only":"Odak dalı köpek sesi ile belirli giysi ve kuş kullanımlarını sınırlar.","gloss":"belirli hışırtılar ve hareket uğultusu","neighbor_only":"Komşu dal rüzgarın ağaçtaki uğultısını, kalabalık gürültüsünü ve kaynayan kabın sesini de kapsar.","neighbor_ref":"root_001588/B005","relation_type":"near_synonym","shared_zone":"İki dal hareketin doğurduğu hışırtı ve uğultu türü seslerde yaklaşır."},{"boundary_match":"partial","distinction":"Odak dalı kanat çırparak uçan kuşun adına, komşu dal ise kanat hareketinin kendisine dayanır.","focus_only":"Odak dalında kanat çırpan kuş, uçuş davranışı üzerinden adlandırılır.","gloss":"kanat çırpan kuş adı ve kanat hareketi","neighbor_only":"Komşu dal kuşun kanatlarını havada veya bir şeyin çevresinde hareket ettirmesini eylem olarak anlatır.","neighbor_ref":"root_000581/B001","relation_type":"near_neighbor","shared_zone":"İki dal kuşun uçuş sırasında kanatlarını art arda hareket ettirmesinde buluşur."}],"source_phrase_ar":"أصوات الكلاب فيقال لها الخفخفة فهو قريب من الباب (maqayis)؛ خفخف إذا حرك قميصه الجديد فسمعت له خفخفة أي صوتا (tahdhib)؛ الخفخوف الطائر الذي يصفق بجناحيه إذا طار (tahdhib)","source_summary":"Kanıtlar köpek sesini bir adlandırma olarak verir; ayrıca yeni giysinin hareket sesini ve kanat çırparak uçan kuşu aynı ses ve hareket ailesine bağlar.","sources":["MQ","TA"],"what_is_ar":"يدخل فيه أصوات الكلاب وخفخفة القميص الجديد وصوت تصفيق الجناحين في الطيران","what_is_not_ar":"لا يدخل فيه خفة الوزن ولا الخُفّ الملبوس"},"support_links":[]},{"boundary":"Dal, ölçme ve ölçüyü belirleme eylemiyle sınırlıdır; adalet, hizalanma ve toplumsal değer ancak başka dallarda ele alınır.","branch_kind":"mixed_non_bare","branch_ref":"root_001645/B001","candidate_links":[{"candidate_id":"cand_54d2564bd0c21a5d557d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مِيزَان","morph_features":"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:8:4:1","qac_word_ref":"101:8:4","surface_ar":"مَوَٰزِينُ"}],"gloss":"tartarak veya yaklaşık ölçüp biçerek niceliği belirleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin ağırlığı veya niceliği, tartı ya da denk bir ölçü aracılığıyla belirlenir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ağaçtaki hurma ürününün miktarı, doğrudan tartılmadan yaklaşık olarak kestirilebilir."}}],"root_ar":"و ز ن","root_id":"root_001645","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem doğrudan tartmayı hem de ürün miktarını yaklaşık kestirme gibi ölçü belirleme uygulamalarını birlikte karşılar.","boundary_detail":"Dal, ölçme ve ölçüyü belirleme eylemiyle sınırlıdır; adalet, hizalanma ve toplumsal değer ancak başka dallarda ele alınır.","branch_image_ar":"تقدير الشيء بوزن أو خرْص","concept_gloss":"tartarak veya yaklaşık ölçüp biçerek niceliği belirleme","contextual_glosses":[{"applicability":"Bir nesnenin ağırlığının tartı veya denk bir ölçü kullanılarak belirlendiği somut bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Doğrudan tartmadan yapılan yaklaşık ürün kestirimini kapsamaz.","preserves":"Doğrudan ağırlık ölçme işlemini doğal ve kısa biçimde korur."},"facet_ids":["F001"],"text":"tartmak","usage_role":"general"},{"applicability":"Ağaçtaki meyvenin miktarının doğrudan tartı yapılmadan yaklaşık olarak belirlendiği bağlamlara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel tartma ve kesin ağırlık belirleme kapsamını dışarıda bırakır.","preserves":"Yaklaşık kestirim işlemini ve ürün bağlamını açıkça korur."},"facet_ids":["F002"],"text":"ürün miktarını göz kararı kestirmek","usage_role":"contextual"}],"definition":"Bir şeyin ağırlığını veya niceliğini, onu tartarak, denk bir ölçüyle karşılaştırarak ya da uygun bağlamda yaklaşık kestirerek belirlemektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin ağırlığı veya niceliği, tartı ya da denk bir ölçü aracılığıyla belirlenir."},{"facet_id":"F002","role":"specialization","statement":"Ağaçtaki hurma ürününün miktarı, doğrudan tartılmadan yaklaşık olarak kestirilebilir."}],"identity_rationale":"Kaynak anlatımı, bir şeyin ağırlığını ya da ölçüsünü tartarak, eş bir ölçüyle karşılaştırarak veya yaklaşık kestirerek belirleme çekirdeğini açıkça destekler. Hurma ürünü için yapılan yaklaşık kestirim bu çekirdeğin özel bir uygulamasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi tartmak veya ölçüsünü belirlemek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"hurma ürününün miktarını yaklaşık kestirmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyin ağırlık ölçüsü"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir dirhem ağırlığında gelmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bir kimse için veya ona karşı bir şeyi tartmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kendisi için tartılanı teslim almak"}],"lexicalization_note":"Tanım, genel tartma eylemiyle birlikte yalnız belirli kalıplarda görülen ürün kestirimi ve alışveriş kullanımlarını ayırır; bu kalıplar çıplak anlama genellenmez.","neighbor_coverage_note":"Bütün adaylar ölçme, ağırlık, satış ve kökün öteki dalları bakımından karşılaştırıldı; yalnız çekirdek sınırını en açık gösteren iki karşıtlık yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda tartı veya denk ölçü temel yöntem olabilir ve yaklaşık kestirim yalnız özel bir uygulamadır; komşuda ise varsayıma dayalı kestirim kendi başına çekirdektir.","focus_only":"Bu dal, tartıyla kesin ağırlık belirlemeyi ve alışverişteki tartma rollerini de kapsar.","gloss":"tartma ile yaklaşık kestirim","neighbor_only":"Komşu dal, sayı, hacim ve meyve miktarını eksik bilgiyle sezgisel olarak kestirmeye özellikle açıktır.","neighbor_ref":"root_000403/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da önceden bilinmeyen bir niceliği belirleme alanında buluşur."},{"boundary_match":"field_only","distinction":"Buradaki çekirdek bir niceliği belirleme eylemidir; komşunun çekirdeği ise ölçülen şeyin ağır olma niteliğidir.","focus_only":"Bu dal, ağırlığı belirleyen ölçme işlemini ve bu işlemin yaklaşık kestirim uzantısını anlatır.","gloss":"ölçme işlemi ve ağırlık niteliği","neighbor_only":"Komşu dal, bir cismin ya da soyut bir şeyin ağır olma niteliğini ve hafifliğe karşı üstün gelmesini anlatır.","neighbor_ref":"root_000202/B001","relation_type":"same_field","shared_zone":"İki dal da ağırlık ve ölçü alanında yer alır."}],"source_phrase_ar":"وزنت الشيء وزنا؛ الزنة قدر وزن الشيء (maqayis)؛ الوزن ثقل شيء بشيء مثله؛ وزن الشيء إذا قدره؛ وزن ثمر النخل إذا خرصه (ayn;tahdhib)؛ وزنت الشئ وزنا وزنة؛ هذا يزن درهما (sihah)؛ الوزن معرفة قدر الشيء؛ ما يقدر بالقسط والقبان (mufradat)","source_summary":"Ortak anlatım, ağırlığı bilinen bir ölçüye göre belirleme ile daha genel nicelik belirlemeyi aynı çekirdekte toplar; ürün kestirimi bunun bağlama bağlı bir uygulamasıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه وزن الشيء بالميزان، قدر وزن الشيء، ثقل الشيء بشيء مثله، وخرص ثمر النخل أو الحزر بوصفه تقديرا.","what_is_not_ar":"لا يدخل فيه مجرد العدل أو المحاذاة أو منزلة الشخص إلا من جهة استعارة الوزن لها."},"support_links":["sup_f95bd775dbe5f04e5483"]},{"boundary":"Somut tartı aracı çekirdekte, adil değerlendirme ise soyut uzantıdadır; yaklaşık ürün kestirimi ve salt hizalanma bu dala girmez.","branch_kind":"bare","branch_ref":"root_001645/B002","candidate_links":[{"candidate_id":"cand_54d2564bd0c21a5d557d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مِيزَان","morph_features":"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:8:4:1","qac_word_ref":"101:8:4","surface_ar":"مَوَٰزِينُ"}],"gloss":"tartı aracı ve adil değerlendirme ölçütü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesnelerin ağırlığını belirlemeye yarayan tartı aracı ve onun ölçü birimleri söz konusudur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tartı düşüncesi, insanların yaptıklarını ve haklarını adil ve denk biçimde değerlendirmeye aktarılır."}}],"root_ar":"و ز ن","root_id":"root_001645","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Somut ağırlık ölçme aracını ve ondan gelişen adil, denk değerlendirme kullanımını birlikte temsil eder.","boundary_detail":"Somut tartı aracı çekirdekte, adil değerlendirme ise soyut uzantıdadır; yaklaşık ürün kestirimi ve salt hizalanma bu dala girmez.","branch_image_ar":"ميزان العدل والقسط","concept_gloss":"tartı aracı ve adil değerlendirme ölçütü","contextual_glosses":[{"applicability":"Nesnelerin ağırlığını ölçmeye yarayan somut aracın kastedildiği bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Adil değerlendirme ve hesap görme uzantısını karşılamaz.","preserves":"Tartı aracını ve onun ağırlık ölçme işlevini eksiksiz korur."},"facet_ids":["F001"],"text":"terazi","usage_role":"general"},{"applicability":"İnsanların eylem ve haklarının doğru ve denk biçimde değerlendirildiği soyut bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Somut tartı aracını ve fiziksel ağırlık ölçümünü dışarıda bırakır.","preserves":"Adil değerlendirme ve doğru denge düşüncesini korur."},"facet_ids":["F002"],"text":"adalet ölçüsü","usage_role":"contextual"}],"definition":"Nesnelerin ağırlığını belirlemeye yarayan tartı aracıdır; soyut kullanımda ise eylem ve hakların doğru, denk ve adil biçimde değerlendirilmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesnelerin ağırlığını belirlemeye yarayan tartı aracı ve onun ölçü birimleri söz konusudur."},{"facet_id":"F002","role":"extension","statement":"Tartı düşüncesi, insanların yaptıklarını ve haklarını adil ve denk biçimde değerlendirmeye aktarılır."}],"identity_rationale":"Kaynak anlatımı hem nesneleri tartmaya yarayan aracı hem de doğru ve denk değerlendirme düşüncesini açıkça verir. İnsanların yaptıklarının adil biçimde değerlendirilmesi, ölçme aracından gelişen soyut bir uzantıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"terazi"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"teraziler ve tartı ağırlıkları"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"hesapta adil ve denk değerlendirme"}],"lexicalization_note":"Tanım, yalın biçimlerde tanıklanan tartı aracı ile adil ölçüt anlamını kapsar ve yalnız başka kalıplara ait okumaları içeri almaz.","neighbor_coverage_note":"Tüm adaylar araç, adalet, eksik ölçme ve kökün öteki dalları yönünden değerlendirildi; araç sınırı ile adalet uzantısını en iyi açıklayan üç ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Somut araç alanında büyük ölçüde örtüşürler; ancak bu dal adalet uzantısına açılırken komşu dal belirli araç adlarıyla sınırlanır.","focus_only":"Bu dal, tartı aracına ek olarak adil değerlendirme ve hesap görme uzantısını da içerir.","gloss":"tartı aracı","neighbor_only":"Komşu dal, tartı aracının belirli adlarını ve özel bir tartı türünü kendi söz varlığı içinde toplar.","neighbor_ref":"root_001225/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın somut çekirdeğinde ağırlık ölçmeye yarayan araç bulunur."},{"boundary_match":"thematic_only","distinction":"Burada araç ve adil ölçüt söz konusudur; komşuda ise bu ölçütün çiğnenmesi olan eksik ölçme eylemi vardır.","focus_only":"Bu dal, ölçme aracını ve ölçümün adil olmasını olumlu bir ölçüt olarak anlatır.","gloss":"adil tartı ve eksik tartma","neighbor_only":"Komşu dal, ölçüyü eksik verme ve karşı tarafın payını azaltma eylemini anlatır.","neighbor_ref":"root_000940/B003","relation_type":"thematic","shared_zone":"İki dal, alışverişte ölçü ve hakkaniyet senaryosunda buluşur."},{"boundary_match":"partial","distinction":"Bu dalın somut odağı araçtır; komşu dalın odağı o araçla ya da başka bir ölçüyle yapılan belirleme işlemidir.","focus_only":"Bu dal, tartı aracını adlandırır ve adil değerlendirme anlamına uzanır.","gloss":"terazi ve tartma","neighbor_only":"Komşu dal, aracın kendisinden çok bir şeyin ağırlığını veya niceliğini belirleme eylemini anlatır.","neighbor_ref":"root_001645/B001","relation_type":"near_neighbor","shared_zone":"İki dal, ağırlık ölçme olayının araç ve işlem yönlerini paylaşır."}],"source_phrase_ar":"بناء يدل على تعديل واستقامة (maqayis)؛ الميزان ما وزنت به (ayn)؛ الميزان معروف (sihah)؛ الموازين واحدها ميزان وهو المثاقيل؛ الآلة التي يوزن بها الأشياء ميزان؛ الميزان العدل (tahdhib)؛ مراعاة المعدلة؛ الوزن يومئذ الحق فإشارة إلى العدل في محاسبة الناس (mufradat)","source_summary":"Ortak anlatım, somut tartı aracını temel alır ve doğru denge ile adil değerlendirmenin bu araçtan gelişen soyut kullanımını da doğrular.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الميزان آلة الوزن، والموازين والمثاقيل، واستعمال الوزن والميزان في القسط والعدل ومحاسبة الأعمال.","what_is_not_ar":"لا يدخل فيه خرص الثمر المحض ولا محاذاة الشيئين ولا قام ميزان النهار إلا بقرينة العدل أو الآلة."},"support_links":["sup_f95bd775dbe5f04e5483"]},{"boundary":"Dal, denklik veya karşılıklı hizalanma gerektirir; salt tartma işlemi ve genel adalet düşüncesi bu koşul olmadan kapsama girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001645/B003","candidate_links":[{"candidate_id":"cand_0184ba9741ba8cb92b16","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مِيزَان","morph_features":"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:8:4:1","qac_word_ref":"101:8:4","surface_ar":"مَوَٰزِينُ"}],"gloss":"iki şeyi denk veya karşılıklı konumda tutma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki şey ölçü bakımından karşılaştırılır ve denk ya da karşılıklı konumda görülür."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yer bildiren kullanımda bir dağın yanı, karşısı veya onunla aynı hiza anlatılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Zihinsel değerlendirmede bir şey başka bir şeye denk sayılır."}}],"root_ar":"و ز ن","root_id":"root_001645","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ölçüsel denklik, karşılıklı hizalanma, yer bildirme ve zihinde denk sayma kullanımlarının ortak çekirdeğini karşılar.","boundary_detail":"Dal, denklik veya karşılıklı hizalanma gerektirir; salt tartma işlemi ve genel adalet düşüncesi bu koşul olmadan kapsama girmez.","branch_image_ar":"موازنة ومحاذاة بين شيئين","concept_gloss":"iki şeyi denk veya karşılıklı konumda tutma","contextual_glosses":[{"applicability":"İki şeyin ölçü veya değer bakımından karşılaştırılıp denk tutulduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Salt yer ve hiza bildiren özel kullanımı doğrudan karşılamaz.","preserves":"İki şeyi karşılaştırma ve ölçü bakımından denk tutma çekirdeğini korur."},"facet_ids":["F001","F003"],"text":"birbirine denklemek","usage_role":"general"},{"applicability":"Bir yerin, özellikle bir dağın yanı, karşısı veya aynı hizası belirtildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ölçüsel karşılaştırma ve zihinsel denklik okumalarını dışarıda bırakır.","preserves":"Karşılıklı konum ve yer bildirme uzantısını doğal biçimde korur."},"facet_ids":["F002"],"text":"hizasında veya yanında olmak","usage_role":"contextual"}],"definition":"İki şeyi ölçü, değer veya konum bakımından birbirine denk ve karşılıklı duruma getirmek ya da öyle görmek; özel yer kullanımında bir şeyin yanını veya hizasını belirtmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki şey ölçü bakımından karşılaştırılır ve denk ya da karşılıklı konumda görülür."},{"facet_id":"F002","role":"extension","statement":"Yer bildiren kullanımda bir dağın yanı, karşısı veya onunla aynı hiza anlatılır."},{"facet_id":"F003","role":"extension","statement":"Zihinsel değerlendirmede bir şey başka bir şeye denk sayılır."}],"identity_rationale":"Kaynak anlatımı, iki şeyi denk ölçüde veya karşılıklı konumda buluşturmayı açıkça destekler. Dağın yanı ya da hizası ve zihinde bir şeyi başkasına denk sayma kullanımları aynı karşılaştırma ve hizalama çekirdeğinin uzantılarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"iki şeyi karşılaştırıp birbirine denklemek"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"bu, ötekiyle aynı ölçüde veya onun hizasındadır"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"dağın yanı veya hizası"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bu, ötekiyle zihinde denk tutulur"}],"lexicalization_note":"Tanım, karşılaştırma kalıpları ile yer bildiren özel kullanımı ayrı tutar; dağla kurulan yer kalıbı genel bir çıplak kök anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar denklik, benzerlik, karşılaştırma, yön ve kökün diğer dalları bakımından sınandı; en yakın iki karışma alanı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda ölçü karşılaştırması ya da karşılıklı hiza belirgindir; komşu dal daha genel bir eşitlik ve benzerlik alanına sahiptir.","focus_only":"Bu dal, denkliğin yanında karşılıklı hizalanmayı ve dağın yanı gibi özel yer kullanımlarını da içerir.","gloss":"denklik ve eşitlik","neighbor_only":"Komşu dal, kişi ve şeyler arasındaki genel eşitlik ve benzerliği konum ilişkisi aramadan anlatabilir.","neighbor_ref":"root_000991/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da iki şey arasında eşitlik veya denklik kurar."},{"boundary_match":"partial","distinction":"Buradaki hiza, ölçü ve denklik düşüncesine bağlanabilir; komşudaki çekirdek ise doğrudan karşıda bulunma yönüdür.","focus_only":"Bu dal, fiziksel hizanın yanı sıra ölçüsel ve zihinsel denklik kurmayı da kapsar.","gloss":"hizalama ve karşı karşıya bulunma","neighbor_only":"Komşu dal, evlerin karşı karşıya bulunması gibi doğrudan yönelme ve yüz yüze konum ilişkisine odaklanır.","neighbor_ref":"root_001450/B010","relation_type":"near_synonym","shared_zone":"İki dal, nesnelerin birbirinin karşısında veya hizasında bulunması alanında örtüşür."}],"source_phrase_ar":"هذا يوازن ذلك أي هو محاذيه (maqayis)؛ وازنت بين الشيئين؛ هذا يوازن هذا إذا كان على زنته أو كان محاذيه؛ هو وزن الجبل أي ناحية منه؛ هو زنة الجبل أي حذاءه (sihah)؛ هذا في وزن هذا؛ قام في النفس مساويا لغيره (tahdhib)","source_summary":"Ortak anlatım, karşılaştırılan iki şeyin aynı ölçüde ya da birbirinin hizasında bulunmasını çekirdek kabul eder; yer ve zihinsel değerlendirme kullanımları bu ilişkiden gelişir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه وازنت بين الشيئين، هذا يوازن هذا، كونه على زنته أو محاذيه، وزنة الجبل أو وزن الجبل بمعنى حذاءه أو ناحيته، وما قام في النفس مساويا لغيره.","what_is_not_ar":"لا يدخل فيه وزن البيع بالميزان ولا العدل العام إلا إذا ظهر معنى المساواة أو المقابلة."},"support_links":["sup_588f2e617ee9e4c86ffd"]},{"boundary":"Anlam yalnız günün ortasına gelmeyi bildiren kalıba bağlıdır; tartı aracı, adalet ve başka zaman dönemleri kapsama girmez.","branch_kind":"collocation","branch_ref":"root_001645/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مِيزَان","morph_features":"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:8:4:1","qac_word_ref":"101:8:4","surface_ar":"مَوَٰزِينُ"}],"gloss":"günün tam ortasına gelmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gün yarıya ulaşmış ve öğle ortası gelmiştir."}}],"root_ar":"و ز ن","root_id":"root_001645","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kalıplaşmış sözün günün yarıya ulaşmasını bildirdiği zaman bağlamını eksiksiz karşılar.","boundary_detail":"Anlam yalnız günün ortasına gelmeyi bildiren kalıba bağlıdır; tartı aracı, adalet ve başka zaman dönemleri kapsama girmez.","branch_image_ar":"قيام ميزان النهار في وسطه","concept_gloss":"günün tam ortasına gelmesi","contextual_glosses":[{"applicability":"Günün ilk yarısının bittiğini ve öğle ortasının geldiğini akıcı cümlede bildirmek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Günün yarıya ulaşması ve öğle ortasının gelmesi anlamını korur."},"facet_ids":["F001"],"text":"gün ortalandı","usage_role":"contextual"}],"definition":"Yalnız belirli bir zaman kalıbında, günün yarısının tamamlandığını ve öğle ortasına gelindiğini bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gün yarıya ulaşmış ve öğle ortası gelmiştir."}],"identity_rationale":"Kaynak anlatımı yalnız belirli zaman kalıbını ve bu kalıbın günün yarıya ulaşıp öğle ortasının gelmesi anlamını verir. Geçici dal çerçevesi bu dar, kalıplaşmış kullanımı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"gün ortalandı"}],"lexicalization_note":"Tanım yalnız günün ortasına erişildiğini bildiren kalıplaşmış zaman sözünü açıklar ve bunu yalın kökün genel anlamına dönüştürmez.","neighbor_coverage_note":"Bütün zaman adayları yükseklik, mevsim, ay, güneş hareketi ve öğle vakti yönünden karşılaştırıldı; doğrudan gün ortası sınırını açıklayan iki aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Zaman noktası aynıdır; ancak bu dal tek bir kalıpla sınırlıyken komşu dal aynı vakti başka sözler ve güneş belirtileriyle de anlatır.","focus_only":"Bu dal, yalnız tek bir kalıpla günün yarıya ulaşmasını bildirir.","gloss":"gün ortası","neighbor_only":"Komşu dal, güneşin tepe konumu ve gölgenin çok kısalması gibi öğle ortasının gözlenebilir belirtilerini de kapsar.","neighbor_ref":"root_001273/B017","relation_type":"near_synonym","shared_zone":"Her iki dal da günün yarıya ulaştığı öğle ortasını gösterir."},{"boundary_match":"partial","distinction":"Bu dal bir anlık orta noktayı bildirir; komşu dal ise daha geniş bir vakit dilimini ve o vakitle ilişkili olayları kapsar.","focus_only":"Bu dal, günün tam yarıya ulaşma sınırını bildiren tek bir kalıba bağlıdır.","gloss":"gün ortası ve öğle vakti","neighbor_only":"Komşu dal, daha geniş öğle vaktini, o vakte girmeyi, o sıradaki ibadeti ve düzenli uğrağı kapsar.","neighbor_ref":"root_000970/B004","relation_type":"near_neighbor","shared_zone":"İki dal da öğle çevresindeki zamanı belirtir."}],"source_phrase_ar":"قام ميزان النهار إذا انتصف النهار (maqayis;mufradat)؛ قام ميزان النهار أي انتصف (sihah)","source_summary":"Kaynakların ortak anlatımı, kalıplaşmış sözü günün tam ortasına erişme ve öğle vaktinin yarılanması anlamında açıklar.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه التعبير الزمني قام ميزان النهار إذا انتصف النهار.","what_is_not_ar":"لا يدخل فيه الميزان آلة الوزن ولا ميزان العدل إلا بقرينة مستقلة."},"support_links":[]},{"boundary":"Sağlam düşünce dalın çekirdeğidir; kendini bir işe hazırlama yalnız tanıklanan kalıba bağlı uzantıdır ve genel tartma anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001645/B005","candidate_links":[{"candidate_id":"cand_2d8539be5f688a08342c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مِيزَان","morph_features":"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:8:4:1","qac_word_ref":"101:8:4","surface_ar":"مَوَٰزِينُ"}],"gloss":"sağlam yargı ve kararlı yöneliş","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Düşünce dengeli, sağlam, ağırbaşlı ve acelecilikten uzak biçimde kararlıdır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi belirli bir işe girişmek üzere kendisini hazırlar ve kararlılıkla ona yönelir."}}],"root_ar":"و ز ن","root_id":"root_001645","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Düşüncenin dengeli ve sağlam oluşunu çekirdek, kişinin kendisini işe hazırlamasını ise kalıba bağlı uzantı olarak birlikte gösterir.","boundary_detail":"Sağlam düşünce dalın çekirdeğidir; kendini bir işe hazırlama yalnız tanıklanan kalıba bağlı uzantıdır ve genel tartma anlamı değildir.","branch_image_ar":"رأي وزين ثابت راجح","concept_gloss":"sağlam yargı ve kararlı yöneliş","contextual_glosses":[{"applicability":"Bir kişinin görüşünün dengeli, güvenilir ve acelecilikten uzak olduğunu anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin kendisini belirli bir işe hazırlaması uzantısını dışarıda bırakır.","preserves":"Düşüncenin sağlam, dengeli ve ağırbaşlı oluşunu korur."},"facet_ids":["F001"],"text":"sağlam ve ağırbaşlı düşünceli","usage_role":"general"},{"applicability":"Kişinin belirli bir işe girişmeyi kabullenip kendisini ona kararlı biçimde yönelttiği kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Düşüncenin dengeli ve sağlam oluşunu niteleyen çekirdeği kapsamaz.","preserves":"Hazırlanma ve kararlı biçimde işe yönelme uzantısını korur."},"facet_ids":["F002"],"text":"kendini o işe hazırlamak","usage_role":"contextual"}],"definition":"Bir kimsenin düşüncesinin dengeli, sağlam, ağırbaşlı ve kararlı olmasıdır; ayrı bir kalıpta kişinin kendisini bir işe hazırlayıp ona kesin biçimde yöneltmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Düşünce dengeli, sağlam, ağırbaşlı ve acelecilikten uzak biçimde kararlıdır."},{"facet_id":"F002","role":"associated_use","statement":"Kişi belirli bir işe girişmek üzere kendisini hazırlar ve kararlılıkla ona yönelir."}],"identity_rationale":"Kaynak anlatımı, dengeli, sağlam ve kararlı düşünceyi açıkça destekler; ayrıca kişinin kendisini bir işe hazırlayıp ona bağlamasını ayrı bir kalıpta verir. Bu ikinci kullanım düşüncenin niteliği değil, kararlı yöneliş olduğundan bağımlı bir uzantı olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"sağlam ve ağırbaşlı düşünceli"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yargısı güçlü ve aklı sağlam"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kendini o işe hazırlayıp kararlılıkla yönelmek"}],"lexicalization_note":"Tanım yalnız düşünceyi niteleyen ve kişinin kendisini bir işe hazırlamasını bildiren kalıplara bağlıdır; bunlardan yalın bir kök anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar akıl, ağırbaşlılık, sağlam görüş, düşünme süreci ve karşıt akıl kaybı yönünden değerlendirildi; çekirdeği en iyi sınırlayan üç aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Düşünce niteliğinde yakınlaşırlar; bu dal ayrıca ağırbaşlı kararlılık ve işe hazırlanma uzantısına sahiptir.","focus_only":"Bu dal, sağlam düşünce yanında kararlılığı ve kişinin kendisini bir işe hazırladığı özel kalıbı da kapsar.","gloss":"sağlam düşünce","neighbor_only":"Komşu dal, doğrudan iyi ve yerinde düşünceyi niteleyen daha dar bir söz varlığına dayanır.","neighbor_ref":"root_000599/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kimsenin düşüncesini sağlam ve iyi olarak niteler."},{"boundary_match":"partial","distinction":"Bu dalın odağı düşüncenin dengesi ve kararlılığıdır; komşu dal kişinin akıl gücüyle bağlantılı daha geniş karakter niteliklerini kapsar.","focus_only":"Bu dal, düşüncenin dengeli oluşunu ve belirli işe kararlı yönelişi anlatır.","gloss":"ağırbaşlılık ve güçlü akıl","neighbor_only":"Komşu dal, güçlü aklın yanında sakınganlık, sır tutma ve ileri görüşlü davranma niteliklerini de içerir.","neighbor_ref":"root_000332/B003","relation_type":"near_synonym","shared_zone":"İki dal, sağlam akıl ve ağırbaşlı yargı alanında örtüşür."},{"boundary_match":"partial","distinction":"Burada sonuç niteliğindeki sağlam ve kararlı yargı öndedir; komşuda ise o sonuca götüren düşünme süreci çekirdektir.","focus_only":"Bu dal, düşünmenin sonucunda ortaya çıkan sağlam yargıyı ve kararlı tutumu niteler.","gloss":"sağlam yargı ve düşünüp taşınma","neighbor_only":"Komşu dal, bir konu üzerinde düşünüp inceleme sürecini ve ölçüp biçmeyi anlatır.","neighbor_ref":"root_000615/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal, karar verme ve düşünce alanında yer alır."}],"source_phrase_ar":"وزين الرأى معتدله؛ راجح الوزن إذا نسبوه إلى رجاحة الرأي وشدة العقل (maqayis)؛ رجل وزين الرأي وقد وزن وزانة إذا كان متثبتا (ayn;tahdhib)؛ فلان وزين الرأي أي رزينه (sihah)؛ أوزن فلان نفسه على الأمر إذا وطن نفسه عليه (tahdhib)","source_summary":"Ortak anlatım, düşüncedeki dengeyi sağlam yargı, güçlü kavrayış ve kararlı tutumla açıklar; kendini bir işe hazırlama kullanımı ayrı bir kalıba bağlıdır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه وزين الرأي، رزين الرأي، المتثبت، رجاحة الرأي وشدة العقل، وتوطين النفس على الأمر.","what_is_not_ar":"لا يدخل فيه مجرد وزن الأجسام أو قصر الجارية أو القدر الاجتماعي إلا إذا صرح بسياق الرأي والعقل."},"support_links":["sup_374aea94482de53dc43a"]},{"boundary":"Dal kadın veya kız için kısa boylulukla sınırlıdır; aklı başında olma yalnız ilgili kalıpta ek niteliktir.","branch_kind":"mixed_non_bare","branch_ref":"root_001645/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مِيزَان","morph_features":"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:8:4:1","qac_word_ref":"101:8:4","surface_ar":"مَوَٰزِينُ"}],"gloss":"kısa boylu, kimi kullanımda aklı başında kadın","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kız veya kadın kısa boylu olarak nitelenir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli kadın nitelemesinde kısa boyluluğa aklı başında olma özelliği eşlik eder."}}],"root_ar":"و ز ن","root_id":"root_001645","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kadın veya kız için kısa boyluluk çekirdeğini ve yalnız dar bir kullanımda eklenen aklı başında olma niteliğini karşılar.","boundary_detail":"Dal kadın veya kız için kısa boylulukla sınırlıdır; aklı başında olma yalnız ilgili kalıpta ek niteliktir.","branch_image_ar":"قصر موزون في الجارية أو المرأة","concept_gloss":"kısa boylu, kimi kullanımda aklı başında kadın","contextual_glosses":[{"applicability":"Bir kızın bedensel olarak kısa boylu oluşunun anlatıldığı kullanımda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kadına özgü kullanımı ve koşullu aklı başında olma niteliğini kapsamaz.","preserves":"Kız olma sınırını ve kısa boyluluk niteliğini korur."},"facet_ids":["F001"],"text":"kısa boylu kız","usage_role":"contextual"},{"applicability":"Kaynakta iki niteliğin birlikte verildiği özel kadın nitelemesinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Akıl niteliği belirtilmeyen daha geniş kız ve kadın kullanımlarını dışarıda bırakır.","preserves":"Kısa boyluluk ile aklı başında olma niteliklerini birlikte korur."},"facet_ids":["F001","F002"],"text":"kısa boylu, aklı başında kadın","usage_role":"contextual"}],"definition":"Bir kızın veya kadının kısa boylu olduğunu anlatır; yalnız belirli kadın nitelemesinde kısa boyluluğa aklı başında olma özelliği de eklenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kız veya kadın kısa boylu olarak nitelenir."},{"facet_id":"F002","role":"specialization","statement":"Belirli kadın nitelemesinde kısa boyluluğa aklı başında olma özelliği eşlik eder."}],"identity_rationale":"Kaynak anlatımı kız veya kadın için kısa boyluluğu açıkça destekler. Akıllı olma niteliği yalnız kadınla kurulan belirli tanıklıkta bulunur; bütün kısa boy kullanımlarına taşınmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kısa boylu kız"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kısa boylu, aklı başında kadın"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kısa boylu kadın"}],"lexicalization_note":"Tanım, kız ve kadınla kurulan niteleme kalıpları ile kadın adı olan biçimi ayırır; bu cinsiyet ve kullanım sınırı çıplak anlama genellenmez.","neighbor_coverage_note":"Bütün adaylar kısa boy, beden yapısı, kadın ve kız adlandırması, uzunluk ve düzgün yapı yönünden karşılaştırıldı; en yakın iki kısa boy dalı seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kadın ve kız nitelemesine özgüdür; komşu dal daha genel beden küçüklüğüne ve başka canlılara uzanır.","focus_only":"Bu dal, kısa boyluluğu kız veya kadınla sınırlar ve bir kalıpta aklı başında olma niteliği ekler.","gloss":"kısa boyluluk","neighbor_only":"Komşu dal, cinsiyet sınırı olmadan kısa ya da küçük gövdeli olmayı ve kimi hayvanların zayıflığını anlatabilir.","neighbor_ref":"root_000286/B010","relation_type":"near_synonym","shared_zone":"Her iki dal da bedenin kısa veya küçük oluşunu anlatır."},{"boundary_match":"partial","distinction":"Burada toplu beden yapısı gerekli değildir ve kullanım kadınlarla sınırlıdır; komşuda kısa ve toplu yapı birlikte bulunur.","focus_only":"Bu dal, kadın veya kız için yalın kısa boyluluğu ve koşullu bir akıl niteliğini anlatır.","gloss":"kısa ve toplu beden","neighbor_only":"Komşu dal, kısa boyun yanında gövdenin toplu ve sıkı yapılı olmasını da kurucu özellik yapar.","neighbor_ref":"root_000080/B006","relation_type":"near_synonym","shared_zone":"İki dalın ortak alanı kısa boylu insan betimlemesidir."}],"source_phrase_ar":"جارية موزونة فيها قصر (ayn;tahdhib)؛ امرأة موزونة قصيرة عاقلة؛ الوزنة المرأة القصيرة (tahdhib)","source_summary":"Ortak tanıklık kız veya kadın için kısa boyluluğu verir; aklı başında olma kaydı yalnız daha dar bir kadın nitelemesine bağlıdır.","sources":["AY","TA"],"what_is_ar":"يدخل فيه جارية موزونة فيها قصر، وامرأة موزونة أو الوزنة بمعنى المرأة القصيرة، مع قيد العقل حيث ذكره المصدر.","what_is_not_ar":"لا يدخل فيه وزن الشيء ولا الرأي الراجح إلا إذا كان الوصف خاصا بالمرأة أو الجارية."},"support_links":[]},{"boundary":"Toplumsal değer ve eksiksiz para ağırlığı ayrı kalıplara bağlı iki yüzdür; bunlardan genel bir çıplak anlam çıkarılmaz.","branch_kind":"collocation","branch_ref":"root_001645/B007","candidate_links":[{"candidate_id":"cand_cfaa52bd10fb9aa72630","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مِيزَان","morph_features":"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:8:4:1","qac_word_ref":"101:8:4","surface_ar":"مَوَٰزِينُ"}],"gloss":"toplumsal değer; eksiksiz ağırlıktaki para","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kimsenin toplum içindeki önemi, değeri veya saygınlığı ağırlık düşüncesiyle değerlendirilir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli para nitelemesinde bir dirhemin eksiksiz ağırlıkta olduğu belirtilir."}}],"root_ar":"و ز ن","root_id":"root_001645","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin önem ve saygınlığına ilişkin kalıpları çekirdek, tam ağırlıktaki para nitelemesini ayrı kullanım olarak gösterir.","boundary_detail":"Toplumsal değer ve eksiksiz para ağırlığı ayrı kalıplara bağlı iki yüzdür; bunlardan genel bir çıplak anlam çıkarılmaz.","branch_image_ar":"قدر ومنزلة لها وزن","concept_gloss":"toplumsal değer; eksiksiz ağırlıktaki para","contextual_glosses":[{"applicability":"Bir kimsenin önemsiz, değersiz veya saygınlıktan yoksun sayıldığı olumsuz kalıplarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tam ağırlıktaki parayı anlatan somut kullanımı kapsamaz.","preserves":"Kişiye verilen değerin ve saygınlığın yok sayılmasını korur."},"facet_ids":["F001"],"text":"hiçbir değeri ve saygınlığı yok","usage_role":"contextual"},{"applicability":"Paranın eksiksiz ve beklenen ağırlıkta olduğunu bildiren somut nitelemede kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin toplum içindeki değeri ve saygınlığı okumasını dışarıda bırakır.","preserves":"Paranın eksiksiz ağırlıkta olma niteliğini korur."},"facet_ids":["F002"],"text":"tam ağırlıktaki dirhem","usage_role":"contextual"}],"definition":"Belirli söz kalıplarında bir kimsenin önem, değer veya saygınlık taşıyıp taşımadığını anlatır; ayrı bir para nitelemesinde ise paranın eksiksiz ağırlıkta olduğunu bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kimsenin toplum içindeki önemi, değeri veya saygınlığı ağırlık düşüncesiyle değerlendirilir."},{"facet_id":"F002","role":"associated_use","statement":"Belirli para nitelemesinde bir dirhemin eksiksiz ağırlıkta olduğu belirtilir."}],"identity_rationale":"Kaynak anlatımı, kişi için ağırlık bulunmamasını değer ve saygınlık yokluğu olarak açıklar. Tam ağırlıktaki para tanıklığı ise toplumsal değerin doğrudan parçası değil, ayrı bir kalıpta eksiksiz ağırlık bildiren somut kullanımdır; iki kullanım tek yalın anlama kaynaştırılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bizim yanımızda hiçbir değeri ve saygınlığı yok"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"onlara hiçbir değer ve saygınlık tanımayız"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"tam ağırlıktaki dirhem"}],"lexicalization_note":"Tanım, kişi değerini reddeden sözler ile tam ağırlıktaki parayı niteleyen ayrı kalıbı açıkça ayırır ve ikisini yalın kök anlamı olarak genellemez.","neighbor_coverage_note":"Bütün adaylar değer, saygınlık, övgü, küçültme, sıra ve toplumsal konum yönünden değerlendirildi; kişi değerini en iyi sınırlayan iki ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kalıplaşmış kişi değerlendirmesiyle ve ayrı para nitelemesiyle sınırlıdır; komşu dal değerli varlıklar ve önemli kişiler için daha geniştir.","focus_only":"Bu dal, kişi değerini belirli ağırlık kalıplarında ifade eder ve tam ağırlıktaki parayı ayrıca kapsar.","gloss":"değer ve ağırlık","neighbor_only":"Komşu dal, değerli ve korunmaya layık nesneleri, önemli kişiyi ve etkili sözü daha geniş biçimde kapsar.","neighbor_ref":"root_000202/B005","relation_type":"near_synonym","shared_zone":"İki dal da değer, önem ve saygınlığı ağırlık düşüncesiyle ilişkilendirir."},{"boundary_match":"partial","distinction":"Buradaki çekirdek kişiye biçilen önem ve saygınlıktır; komşuda ise yer veya konum kavramı kendi başına çekirdektir.","focus_only":"Bu dal, kişiye verilen önemi ve saygınlığı değer yargısı olarak anlatır.","gloss":"değer ve konum","neighbor_only":"Komşu dal, fiziksel yer ile görev veya toplum içindeki konumu ve bir yerde yerleşik olmayı kapsar.","neighbor_ref":"root_001332/B002","relation_type":"near_neighbor","shared_zone":"İki dal, kişinin toplum içindeki yerini anlatan bağlamlarda buluşabilir."}],"source_phrase_ar":"درهم وازن أي تام (sihah)؛ ما لفلان عندنا وزن أي قدر لخسته؛ فلا نقيم لهم يوم القيامة وزنا (tahdhib)؛ فلا نقيم لهم يوم القيامة وزنا (mufradat)","source_summary":"Ortak anlatım, kişi için ağırlığı değer ve saygınlıkla ilişkilendiren olumsuz kalıpları verir; tam ağırlıktaki para ise aynı dalda yer alan ayrı ve somut bir kullanımdır.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه الوزن بمعنى قدر الشخص أو منزلته، ونفي الوزن لمن لا قدر له، والتام الوافي في مثل درهم وازن.","what_is_not_ar":"لا يدخل فيه آلة الميزان ولا الموازنة بين شيئين إلا من جهة دلالة القدر والمنزلة."},"support_links":["sup_88ccbdfc18ccc7ec8393"]},{"boundary":"Anlam yalnız ölçülü veya dengeli yaratılmayı bildiren kalıba bağlıdır; madenler olası dar yorum, bütün yaratılmışlar ise geniş yorumdur.","branch_kind":"collocation","branch_ref":"root_001645/B008","candidate_links":[{"candidate_id":"cand_0184ba9741ba8cb92b16","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مِيزَان","morph_features":"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:8:4:1","qac_word_ref":"101:8:4","surface_ar":"مَوَٰزِينُ"}],"gloss":"ölçülü ve dengeli yaratılmış şey","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey belirlenmiş ölçüye uygun, dengeli ve düzgün biçimde var edilmiştir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kapsam bir yorumda madenlere daralır, başka bir yorumda yaratılmış her şeye genişler."}}],"root_ar":"و ز ن","root_id":"root_001645","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaratılmış şeyin belirli ölçüye, dengeye ve düzgünlüğe sahip oluşunu, değişebilen kapsam yorumlarından bağımsız olarak karşılar.","boundary_detail":"Anlam yalnız ölçülü veya dengeli yaratılmayı bildiren kalıba bağlıdır; madenler olası dar yorum, bütün yaratılmışlar ise geniş yorumdur.","branch_image_ar":"شيء موزون مخلوق باعتدال","concept_gloss":"ölçülü ve dengeli yaratılmış şey","contextual_glosses":[{"applicability":"Bir varlığın uygun ölçü ve dengeyle meydana getirildiğinin anlatıldığı geniş yorumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaratılıştaki belirlenmiş ölçüyü, dengeyi ve düzgünlüğü korur."},"facet_ids":["F001"],"text":"ölçülü ve dengeli yaratılmış","usage_role":"general"},{"applicability":"Kapsamın gümüş ve altın gibi madenlere daraltıldığı özel yorum açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yaratılmış her şeyi kapsayan geniş yorumu dışarıda bırakır.","preserves":"Belirlenmiş ölçü düşüncesini ve madenlere özgü dar yorumu korur."},"facet_ids":["F001","F002"],"text":"ölçüsü belirlenmiş madenler","usage_role":"explanatory"}],"definition":"Bir şeyin belirlenmiş ölçüye uygun, dengeli ve düzgün biçimde var edilmiş olduğunu anlatır; bağlama göre madenlerle sınırlandırılabilir veya yaratılmış her şeyi kapsayabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey belirlenmiş ölçüye uygun, dengeli ve düzgün biçimde var edilmiştir."},{"facet_id":"F002","role":"source_variant","statement":"Kapsam bir yorumda madenlere daralır, başka bir yorumda yaratılmış her şeye genişler."}],"identity_rationale":"Kaynak anlatımı, ölçülü ve dengeli biçimde var edilmiş şeyi destekler. Belirli bir anlatım bunu madenler olarak yorumlarken daha geniş anlatım yaratılmış her şeyi kapsar; maden örneği bütün dalın zorunlu kapsamı yapılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"ölçülü ve dengeli yaratılmış şey"}],"lexicalization_note":"Tanım yalnız ölçülü ve dengeli yaratılmış şeyi bildiren kalıba bağlıdır; bu yaratılış okuması yalın kökün genel anlamına aktarılmaz.","neighbor_coverage_note":"Bütün adaylar düzgünlük, ölçüye uygunluk, yaratılış, yapı, maden ve genel ölçme yönünden karşılaştırıldı; sınırı en iyi açıklayan üç ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yaratılmış şeye ilişkin tek bir kalıpla sınırlıdır; komşu dal düzeltme eylemi ve çeşitli alanlardaki genel denge için daha geniştir.","focus_only":"Bu dal, yalnız yaratılmış bir şeyin belirlenmiş ölçü ve dengeye sahip olduğunu bildiren kalıba bağlıdır.","gloss":"yaratılışta denge ve genel düzgünlük","neighbor_only":"Komşu dal, bir şeyi düzeltip düzgün kılma eylemini ve beden, sıcaklık ya da soğukluktaki genel dengeyi de kapsar.","neighbor_ref":"root_000991/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da düzgünlük, denge ve uygun ölçü düşüncesini taşır."},{"boundary_match":"partial","distinction":"Buradaki ölçü yaratılış ve var edilme bağlamına bağlıdır; komşu dal uygun miktar, orta boy ve beden oranı gibi daha geniş kullanımlara sahiptir.","focus_only":"Bu dal, var edilmiş şeyin yaratılıştan belirli ölçü ve denge taşımasını anlatır.","gloss":"uygun ölçü ve dengeli yaratılış","neighbor_only":"Komşu dal, bir şeyin uygun miktarda gelmesini, orta boyu ve hayvan gövdesindeki belirli oranları da kapsar.","neighbor_ref":"root_001205/B006","relation_type":"near_synonym","shared_zone":"İki dal, bir şeyin kendisine uygun ölçüde ve dengede bulunması alanında örtüşür."},{"boundary_match":"partial","distinction":"Bu dalda uygun ölçü ve denge kurucudur; komşuda ise parçalı yapı ve kuruluş biçimi kurucudur.","focus_only":"Bu dal, yaratılmış şeyin ölçülü ve dengeli olma niteliğini öne çıkarır.","gloss":"dengeli yaratılış ve yapı","neighbor_only":"Komşu dal, bir şeyin parçalarının nasıl kurulup birleştiğini anlatan yapı ve kuruluş biçimine odaklanır.","neighbor_ref":"root_000156/B002","relation_type":"near_neighbor","shared_zone":"İki dal, bir varlığın yaratılış biçimini ve beden yapısını anlatırken buluşabilir."}],"source_phrase_ar":"بناء يدل على تعديل واستقامة (maqayis)؛ وأنبتنا فيها من كل شيء موزون؛ قيل هو المعادن كالفضة والذهب؛ كل ما أوجده الله وأنه خلقه باعتدال (mufradat)","source_summary":"Ortak çekirdek, var edilen şeyde belirlenmiş ölçü, denge ve düzgünlüktür; kapsamın yalnız madenler mi yoksa bütün yaratılmışlar mı olduğu konusunda dar ve geniş yorumlar bulunur.","sources":["MQ","MU"],"what_is_ar":"يدخل فيه الموزون بمعنى المقدر أو المخلوق باعتدال، وما قيل في المعادن أو كل مخلوق مقدر.","what_is_not_ar":"لا يدخل فيه وزن المعاملة بالميزان ولا قصر المرأة ولا أسماء المواضع والنجوم."},"support_links":["sup_588f2e617ee9e4c86ffd"]}],"candidate_inventory":[{"anchor_refs":["101:8:1"],"branch_refs":[],"candidate_id":"cand_cf5b63a4766bc9928686","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:8:1:coordinate-reopening","source_type":"word_analysis","support_ids":["sup_117a988422589f4f1282","sup_4c453c460ecc4fbb42ac"],"title":"closure shifts to reopening","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:1","qac_refs":["101:8:1:1"],"status":"accepted"}},{"anchor_refs":["101:8:1"],"branch_refs":[],"candidate_id":"cand_cf4d054d7c25b6b5339b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:8:1:coordinated-second-branch","source_type":"word_analysis","support_ids":["sup_117a988422589f4f1282","sup_69a48646fc7ec2a64e00"],"title":"coordinated second branch","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:1","qac_refs":["101:8:1:1"],"status":"accepted"}},{"anchor_refs":["101:8:2"],"branch_refs":[],"candidate_id":"cand_64ee52cdf9c7f3a089b5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:8:2:boundary-from-result-to-condition","source_type":"word_analysis","support_ids":["sup_3dc571d4e3181dd25dda","sup_a44b9c955a5ea540b18d"],"title":"result gives way to condition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:2","qac_refs":["101:8:1:2"],"status":"accepted"}},{"anchor_refs":["101:8:2"],"branch_refs":[],"candidate_id":"cand_e4acb5e0699c4935210c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:8:2:delayed-fa-answer","source_type":"word_analysis","support_ids":["sup_9209194cfd919e2bd676","sup_a44b9c955a5ea540b18d"],"title":"answer delayed across boundary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:2","qac_refs":["101:8:1:2"],"status":"accepted"}},{"anchor_refs":["101:8:2"],"branch_refs":[],"candidate_id":"cand_144358711d229b6ce85a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:8:2:sorting-particle","source_type":"word_analysis","support_ids":["sup_a44b9c955a5ea540b18d","sup_e37dc2eb54e51fe11013"],"title":"case-sorting particle","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:2","qac_refs":["101:8:1:2"],"status":"accepted"}},{"anchor_refs":["101:8:3"],"branch_refs":[],"candidate_id":"cand_35472c050ec3b6c0bd23","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:8:3:generic-individualized-person","source_type":"word_analysis","support_ids":["sup_5cf690c8e85579e166e0","sup_afc747f27278c39fd9cf"],"title":"generic person individualized by suffixes","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:3","qac_refs":["101:8:2:1"],"status":"accepted"}},{"anchor_refs":["101:8:3"],"branch_refs":[],"candidate_id":"cand_4ffc9b7dc5d2cf1e9067","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:8:3:new-slot-not-same-referent","source_type":"word_analysis","support_ids":["sup_1ebc4d07ddfbc3edde89","sup_afc747f27278c39fd9cf"],"title":"parallel slot with new referent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:3","qac_refs":["101:8:2:1"],"status":"accepted"}},{"anchor_refs":["101:8:3"],"branch_refs":[],"candidate_id":"cand_23c348ff0d25c9c0be9c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:8:3:relative-conditional-force","source_type":"word_analysis","support_ids":["sup_afc747f27278c39fd9cf","sup_baf6ddfd56ca8056329d"],"title":"relative and conditional at once","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:3","qac_refs":["101:8:2:1"],"status":"accepted"}},{"anchor_refs":["101:8:4"],"branch_refs":[],"candidate_id":"cand_f8d078b9a5909daab2f6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000427"],"scope":"focus_ayah","source_local_id":"101:8:4:antithetical-scale-verb","source_type":"word_analysis","support_ids":["sup_ca7e31fcd21a587fc46f","sup_f764a3a828bc9946e87d"],"title":"light verb reverses heavy verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:4","qac_refs":["101:8:3:1"],"status":"accepted"}},{"anchor_refs":["101:8:4"],"branch_refs":[],"candidate_id":"cand_6b38cf1eb4afa9e694b7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000427"],"scope":"focus_ayah","source_local_id":"101:8:4:clipped-sound-effect","source_type":"word_analysis","support_ids":["sup_35931ae058b7ffabd8de","sup_ca7e31fcd21a587fc46f"],"title":"clipped doubled sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:4","qac_refs":["101:8:3:1"],"status":"accepted"}},{"anchor_refs":["101:8:4"],"branch_refs":[],"candidate_id":"cand_e797f985d2987dca68d9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000427"],"scope":"focus_ayah","source_local_id":"101:8:4:completed-intransitive-state","source_type":"word_analysis","support_ids":["sup_4629a1986addb9831450","sup_ca7e31fcd21a587fc46f"],"title":"completed lightness state","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:4","qac_refs":["101:8:3:1"],"status":"accepted"}},{"anchor_refs":["101:8:4"],"branch_refs":[],"candidate_id":"cand_c5ea14b616597cd54f99","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000427"],"scope":"focus_ayah","source_local_id":"101:8:4:cross-passage-delayed-result","source_type":"word_analysis","support_ids":["sup_2d8653c0db20eb9e42c0","sup_ca7e31fcd21a587fc46f"],"title":"known light-scales formula with delayed result","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:4","qac_refs":["101:8:3:1"],"status":"accepted"}},{"anchor_refs":["101:8:4"],"branch_refs":[],"candidate_id":"cand_fe6f2e2040f740fc3fdb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000427"],"scope":"focus_ayah","source_local_id":"101:8:4:geminate-root-correction","source_type":"word_analysis","support_ids":["sup_4aa633972ed9a3ebbee6","sup_ca7e31fcd21a587fc46f"],"title":"geminate lightness root","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:4","qac_refs":["101:8:3:1"],"status":"accepted"}},{"anchor_refs":["101:8:4"],"branch_refs":[],"candidate_id":"cand_04fa98809b3e6aebe554","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000427"],"scope":"focus_ayah","source_local_id":"101:8:4:measured-insufficiency-pressure","source_type":"word_analysis","support_ids":["sup_2c895184b9a78629d7cc","sup_ca7e31fcd21a587fc46f"],"title":"lightness as failed substance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:4","qac_refs":["101:8:3:1"],"status":"accepted"}},{"anchor_refs":["101:8:4"],"branch_refs":[],"candidate_id":"cand_580a4debd61bbcf6ff8a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000427"],"scope":"focus_ayah","source_local_id":"101:8:4:reward-to-measurement-reset","source_type":"word_analysis","support_ids":["sup_65cd4b0c349b1b4a2b15","sup_ca7e31fcd21a587fc46f"],"title":"reward state resets to measurement","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:4","qac_refs":["101:8:3:1"],"status":"accepted"}},{"anchor_refs":["101:8:4"],"branch_refs":[],"candidate_id":"cand_15690a1afbac04bebe45","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000427"],"scope":"focus_ayah","source_local_id":"101:8:4:scales-as-subject","source_type":"word_analysis","support_ids":["sup_b3ed7105ead292b29dc4","sup_ca7e31fcd21a587fc46f"],"title":"agreement points to scales","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:4","qac_refs":["101:8:3:1"],"status":"accepted"}},{"anchor_refs":["101:8:5"],"branch_refs":[],"candidate_id":"cand_d28008d0232c9233f5e9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:8:5:boundary-and-cadence-reset","source_type":"word_analysis","support_ids":["sup_30ef53a4cde47a2390fe","sup_ae29e9b3b9477c635b84"],"title":"measurement scene carries the boundary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:5","qac_refs":["101:8:4:1","101:8:4:2"],"status":"accepted"}},{"anchor_refs":["101:8:5"],"branch_refs":[],"candidate_id":"cand_6fcf243dfdf6a0e0ecc1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:8:5:closing-on-scales","source_type":"word_analysis","support_ids":["sup_2e4d67e70c1588b5364a","sup_ae29e9b3b9477c635b84"],"title":"ayah closes before the answer","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:5","qac_refs":["101:8:4:1","101:8:4:2"],"status":"accepted"}},{"anchor_refs":["101:8:5"],"branch_refs":[],"candidate_id":"cand_5548889bc47019b77052","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:8:5:formula-anchor","source_type":"word_analysis","support_ids":["sup_ae29e9b3b9477c635b84","sup_bc7a92608f95240abecc"],"title":"same scale phrase anchors reversal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:5","qac_refs":["101:8:4:1","101:8:4:2"],"status":"accepted"}},{"anchor_refs":["101:8:5"],"branch_refs":[],"candidate_id":"cand_07f2f3a4d33497ec33d7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:8:5:instrument-subject","source_type":"word_analysis","support_ids":["sup_72133bb6ba074aab8255","sup_ae29e9b3b9477c635b84"],"title":"instrument noun reports the verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:5","qac_refs":["101:8:4:1","101:8:4:2"],"status":"accepted"}},{"anchor_refs":["101:8:5"],"branch_refs":[],"candidate_id":"cand_35a7b358c1c8e3fa0305","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:8:5:plural-justice-standards","source_type":"word_analysis","support_ids":["sup_ae29e9b3b9477c635b84","sup_fca691ab973d5c7e39eb"],"title":"plural scales as calibrated standards","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:5","qac_refs":["101:8:4:1","101:8:4:2"],"status":"accepted"}},{"anchor_refs":["101:8:5"],"branch_refs":[],"candidate_id":"cand_871ee1c23db44d2e7611","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:8:5:possessed-personal-scales","source_type":"word_analysis","support_ids":["sup_a66a28de81dd83525055","sup_ae29e9b3b9477c635b84"],"title":"possessed scales personalize the case","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:8:5","qac_refs":["101:8:4:1","101:8:4:2"],"status":"accepted"}},{"anchor_refs":["101:8:3"],"branch_refs":[],"candidate_id":"cand_53c35b3f4a356c6b2d24","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000427"],"scope":"focus_ayah","source_local_id":"101:8:3:1","source_type":"qac_morpheme","support_ids":["sup_0673e6b94a6a9b8c988e"],"title":"QAC root occurrence: خ ف ف","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["101:8:4"],"branch_refs":[],"candidate_id":"cand_703abf415a1838f36a0e","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:8:4:1","source_type":"qac_morpheme","support_ids":["sup_408dc4d901b9226a0dca"],"title":"QAC root occurrence: و ز ن","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["101:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:8","branch_refs":["root_000427/B003","root_001645/B001","root_001645/B002"],"candidate_id":"cand_54d2564bd0c21a5d557d","commentary_obligation":"review","hft_ref":"hft_0f63f83865ce4ea5bed6","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:B01_evidentiary_deficit","source_type":"hft","support_ids":["sup_f95bd775dbe5f04e5483"],"title":"B01_evidentiary_deficit","trust":"legacy_unbound"},{"anchor_refs":["101:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:8","branch_refs":["root_000427/B005","root_001645/B007"],"candidate_id":"cand_cfaa52bd10fb9aa72630","commentary_obligation":"review","hft_ref":"hft_b0139f9aac36be7737af","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:B02_devalued_standing","source_type":"hft","support_ids":["sup_88ccbdfc18ccc7ec8393"],"title":"B02_devalued_standing","trust":"legacy_unbound"},{"anchor_refs":["101:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:8","branch_refs":["root_000427/B004","root_001645/B005"],"candidate_id":"cand_2d8539be5f688a08342c","commentary_obligation":"review","hft_ref":"hft_0694f88183ce138d910c","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:B03_unsettled_judgment","source_type":"hft","support_ids":["sup_374aea94482de53dc43a"],"title":"B03_unsettled_judgment","trust":"legacy_unbound"},{"anchor_refs":["101:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:8","branch_refs":["root_000427/B001","root_001645/B003","root_001645/B008"],"candidate_id":"cand_0184ba9741ba8cb92b16","commentary_obligation":"review","hft_ref":"hft_4ba82cc72e635907ee95","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:B04_failed_proportion","source_type":"hft","support_ids":["sup_588f2e617ee9e4c86ffd"],"title":"B04_failed_proportion","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"101:8:1:1","qac_word_ref":"101:8:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"أَمَّا","morph_features":"STEM|POS:EXL|LEM:>am~aA","morpheme_role":"STEM","pos":"EXL","qac_ref":"101:8:1:2","qac_word_ref":"101:8:1","root_ar":"","surface_ar":"أَمَّا"},{"lemma_ar":"مَن","morph_features":"STEM|POS:COND|LEM:man","morpheme_role":"STEM","pos":"COND","qac_ref":"101:8:2:1","qac_word_ref":"101:8:2","root_ar":"","surface_ar":"مَنْ"},{"lemma_ar":"خَفَّتْ","morph_features":"STEM|POS:V|PERF|LEM:xaf~ato|ROOT:xff|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:8:3:1","qac_word_ref":"101:8:3","root_ar":"خ ف ف","surface_ar":"خَفَّتْ"},{"lemma_ar":"مِيزَان","morph_features":"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:8:4:1","qac_word_ref":"101:8:4","root_ar":"و ز ن","surface_ar":"مَوَٰزِينُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"101:8:4:2","qac_word_ref":"101:8:4","root_ar":"","surface_ar":"هُۥ"}],"word_analysis_qac_refs":[["101:8:1:1"],["101:8:1:2"],["101:8:2:1"],["101:8:3:1"],["101:8:4:1","101:8:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["101:8:1","101:8:2","101:8:3","101:8:4","101:8:5"]},"focus_surface_evidence":{"arabic_uthmani":"وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"101:8:1:1","qac_word_ref":"101:8:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"أَمَّا","morph_features":"STEM|POS:EXL|LEM:>am~aA","morpheme_role":"STEM","pos":"EXL","qac_ref":"101:8:1:2","qac_word_ref":"101:8:1","root_ar":"","surface_ar":"أَمَّا"},{"lemma_ar":"مَن","morph_features":"STEM|POS:COND|LEM:man","morpheme_role":"STEM","pos":"COND","qac_ref":"101:8:2:1","qac_word_ref":"101:8:2","root_ar":"","surface_ar":"مَنْ"},{"lemma_ar":"خَفَّتْ","morph_features":"STEM|POS:V|PERF|LEM:xaf~ato|ROOT:xff|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:8:3:1","qac_word_ref":"101:8:3","root_ar":"خ ف ف","surface_ar":"خَفَّتْ"},{"lemma_ar":"مِيزَان","morph_features":"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:8:4:1","qac_word_ref":"101:8:4","root_ar":"و ز ن","surface_ar":"مَوَٰزِينُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"101:8:4:2","qac_word_ref":"101:8:4","root_ar":"","surface_ar":"هُۥ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["101:8:1:1"],["101:8:1:2"],["101:8:2:1"],["101:8:3:1"],["101:8:4:1","101:8:4:2"]],"word_analysis_refs":["101:8:1","101:8:2","101:8:3","101:8:4","101:8:5"],"word_rows":[{"analysis_record_ref":"101:8:1","analytic_gloss_range_en":"opening conjunction for the second conditional branch, coordinating it with the earlier heavy-scales case while also restarting the paired contrast","analytic_root_gloss_range_en":null,"qac_refs":["101:8:1:1"],"root":{"note":"no root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"101:8:2","analytic_gloss_range_en":"conditional-topical detailing particle that classifies a case and suspends its answer until the following fāʾ-response in 101:9","analytic_root_gloss_range_en":null,"qac_refs":["101:8:1:2"],"root":{"note":"no root"},"surface":{"arabic":"أَمَّا","transliteration":"ammā"}},{"analysis_record_ref":"101:8:3","analytic_gloss_range_en":"generic conditional-relative pronoun, introducing whoever belongs to this case and supplying the antecedent for the later possessive suffix","analytic_root_gloss_range_en":null,"qac_refs":["101:8:2:1"],"root":{"note":"no root"},"surface":{"arabic":"مَنْ","transliteration":"man"}},{"analysis_record_ref":"101:8:4","analytic_gloss_range_en":"the scales came up light as a completed measured state; the local scale noun selects insufficiency of weight while allowing moral insubstantiality as pressure","analytic_root_gloss_range_en":"lightness, becoming light, quickness or ease, slightness, and levity; locally narrowed to measured lightness in a scale-verdict frame","qac_refs":["101:8:3:1"],"root":{"arabic":"خ ف ف","transliteration":"kh-f-f"},"surface":{"arabic":"خَفَّتْ","transliteration":"khaffat"}},{"analysis_record_ref":"101:8:5","analytic_gloss_range_en":"his plural scales or measuring standards, grammatically the subject of the lightness verb and personally bound to the generic case","analytic_root_gloss_range_en":"weighing, measuring, balancing, proportion, worth, and calibrated judgment; locally expressed through a plural instrument noun in a verdict frame","qac_refs":["101:8:4:1","101:8:4:2"],"root":{"arabic":"و ز ن","transliteration":"w-z-n"},"surface":{"arabic":"مَوَٰزِينُهُۥ","transliteration":"mawāzīnuhū"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["101:8"],"branch_refs":["root_000427/B003","root_001645/B001","root_001645/B002"],"candidate_id":"cand_54d2564bd0c21a5d557d","evidence_scope":"focus_ayah","hft_ref":"hft_0f63f83865ce4ea5bed6","item_id":"B01_evidentiary_deficit","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:B01_evidentiary_deficit","support_id":"sup_f95bd775dbe5f04e5483"},{"anchor_refs":["101:8"],"branch_refs":["root_000427/B005","root_001645/B007"],"candidate_id":"cand_cfaa52bd10fb9aa72630","evidence_scope":"focus_ayah","hft_ref":"hft_b0139f9aac36be7737af","item_id":"B02_devalued_standing","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:B02_devalued_standing","support_id":"sup_88ccbdfc18ccc7ec8393"},{"anchor_refs":["101:8"],"branch_refs":["root_000427/B004","root_001645/B005"],"candidate_id":"cand_2d8539be5f688a08342c","evidence_scope":"focus_ayah","hft_ref":"hft_0694f88183ce138d910c","item_id":"B03_unsettled_judgment","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:B03_unsettled_judgment","support_id":"sup_374aea94482de53dc43a"},{"anchor_refs":["101:8"],"branch_refs":["root_000427/B001","root_001645/B003","root_001645/B008"],"candidate_id":"cand_0184ba9741ba8cb92b16","evidence_scope":"focus_ayah","hft_ref":"hft_4ba82cc72e635907ee95","item_id":"B04_failed_proportion","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:B04_failed_proportion","support_id":"sup_588f2e617ee9e4c86ffd"}],"diagnostics":[],"lane_counts":{"global":11,"macro":12,"micro":4},"packet_summary":{"ayah_count":11,"focus_ref":"101:8","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["101:1","101:2","101:3","101:4","101:5","101:6","101:7","101:8","101:9","101:10","101:11"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"101:8","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":11,"source_present":true,"structured_insight_count":16,"unstructured_record_count":0},"identity":{"ayah_ref":"101:8","lane":"micro","linguistic_source_ref":"101:8","surface_ref":"101:8","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"101:8","target_tokens":[["Ama",["101:8:1"]],["tartıları",["101:8:4"]],["hafif",["101:8:3"]],["gelen",["101:8:3"]],["kişiye",["101:8:2"]],["gelince",["101:8:1"]]],"text":"Ama tartıları hafif gelen kişiye gelince,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s101-p01-001-011","label":"Whole surah","number":1,"refs":["101:1","101:2","101:3","101:4","101:5","101:6","101:7","101:8","101:9","101:10","101:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"101:8:3:1","source_type":"qac_morpheme","support_id":"sup_0673e6b94a6a9b8c988e","text":"{\"lemma_ar\":\"خَفَّتْ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:xaf~ato|ROOT:xff|3FS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"101:8:3:1\",\"qac_word_ref\":\"101:8:3\",\"root_ar\":\"خ ف ف\",\"surface_ar\":\"خَفَّتْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:1","source_type":"word_analysis","support_id":"sup_117a988422589f4f1282","text":"{\"gloss_range\":\"opening conjunction for the second conditional branch, coordinating it with the earlier heavy-scales case while also restarting the paired contrast\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) does not merely add another statement. At the start of this branch, it places the light-scales case beside the heavy-scales case (101:6) as a coordinated alternative, while reopening the same judgment architecture after the first outcome has closed in 101:7. The following detailing particle makes the onset compressed: linkage and repartition arrive together.\",\"root_display\":\"no root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:3:new-slot-not-same-referent","source_type":"word_analysis","support_id":"sup_1ebc4d07ddfbc3edde89","text":"{\"blocking_evidence\":null,\"headline\":\"parallel slot with new referent\",\"reader_payoff\":\"The reader compares this person-slot with the prior branch without confusing the satisfied person in 101:7 with the light-scales case.\",\"reason\":\"The parallel construction remains audible, but the new generic pronoun starts a new case rather than continuing the previous referent.\",\"representative_source_ids\":[\"QB-7606e4bb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:4:measured-insufficiency-pressure","source_type":"word_analysis","support_id":"sup_2c895184b9a78629d7cc","text":"{\"blocking_evidence\":null,\"headline\":\"lightness as failed substance\",\"reader_payoff\":\"The reader feels the physical lightness of the scales carrying moral insufficiency, while the local noun keeps the sense anchored in measured weight.\",\"reason\":\"The broader root field can support slightness or levity as pressure, but adjacency to the scale noun selects measured insufficiency rather than speed, ease, or free-standing triviality.\",\"representative_source_ids\":[\"QS-9613d6bc\",\"QS-c360a72e\",\"QI-9ffc2c08\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:4:cross-passage-delayed-result","source_type":"word_analysis","support_id":"sup_2d8653c0db20eb9e42c0","text":"{\"blocking_evidence\":null,\"headline\":\"known light-scales formula with delayed result\",\"reader_payoff\":\"The reader recognizes the light-scales formula from 7:9 and 23:103, then notices that this ayah withholds the result until 101:9.\",\"reason\":\"The contextual profile ties this verb to the scale noun in the light-scales construction, and the local detailing frame delays the answer across the ayah boundary.\",\"representative_source_ids\":[\"QI-be3a43cb\",\"QE-818e2873\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:5:closing-on-scales","source_type":"word_analysis","support_id":"sup_2e4d67e70c1588b5364a","text":"{\"blocking_evidence\":null,\"headline\":\"ayah closes before the answer\",\"reader_payoff\":\"The reader is left at the possessed scales at the end of 101:8, with the required consequence still pending in 101:9.\",\"reason\":\"The noun completes the relative clause but not the larger detailing construction, whose answer follows in the next ayah.\",\"representative_source_ids\":[\"QT-0efcdb53\",\"QB-d01ef8ed\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:5:boundary-and-cadence-reset","source_type":"word_analysis","support_id":"sup_30ef53a4cde47a2390fe","text":"{\"blocking_evidence\":null,\"headline\":\"measurement scene carries the boundary\",\"reader_payoff\":\"The reader feels the prior reward scene give way to the measuring noun, whose long cadence and suffix carry the clause toward the next consequence.\",\"reason\":\"The boundary reset and suffix bridge are locally licensed; the cadence claim is kept as a cautious acoustic effect rather than a separate semantic branch.\",\"representative_source_ids\":[\"QP-f2c34040\",\"QB-22f90dfc\",\"QB-7a7be275\",\"QB-8711750e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:4:clipped-sound-effect","source_type":"word_analysis","support_id":"sup_35931ae058b7ffabd8de","text":"{\"blocking_evidence\":null,\"headline\":\"clipped doubled sound\",\"reader_payoff\":\"The reader can hear the short doubled sound as an abrupt acoustic counterpart to the semantic lightness and the shift from the prior reward cadence.\",\"reason\":\"The doubled consonant is real surface evidence; the acoustic contrast is preserved cautiously as a reader effect rather than a separate lexical sense.\",\"representative_source_ids\":[\"QP-4867f9cb\",\"QP-b67cd839\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:2:boundary-from-result-to-condition","source_type":"word_analysis","support_id":"sup_3dc571d4e3181dd25dda","text":"{\"blocking_evidence\":null,\"headline\":\"result gives way to condition\",\"reader_payoff\":\"The reader feels the move from the previous completed reward statement into an unfinished negative condition.\",\"reason\":\"The construction starts a dependency that crosses the ayah boundary, so the boundary itself carries syntactic pressure.\",\"representative_source_ids\":[\"QB-39407090\",\"QB-dc924620\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"101:8:4:1","source_type":"qac_morpheme","support_id":"sup_408dc4d901b9226a0dca","text":"{\"lemma_ar\":\"مِيزَان\",\"morph_features\":\"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"101:8:4:1\",\"qac_word_ref\":\"101:8:4\",\"root_ar\":\"و ز ن\",\"surface_ar\":\"مَوَٰزِينُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:4:completed-intransitive-state","source_type":"word_analysis","support_id":"sup_4629a1986addb9831450","text":"{\"blocking_evidence\":null,\"headline\":\"completed lightness state\",\"reader_payoff\":\"The reader notices the verdict as already settled in the state of the scales, with no visible agent still adjusting them.\",\"reason\":\"The perfect Form I intransitive frame and absence of an object support completed statehood rather than causation.\",\"representative_source_ids\":[\"QG-2f550e8d\",\"QF-220e6532\",\"QY-5ccf07d4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:4:geminate-root-correction","source_type":"word_analysis","support_id":"sup_4aa633972ed9a3ebbee6","text":"{\"blocking_evidence\":null,\"headline\":\"geminate lightness root\",\"reader_payoff\":\"The reader avoids a fear-root misreading and hears the doubled consonant as the surface clue to the lightness root.\",\"reason\":\"The aligned QAC root, local meaning, doubled consonant, and heavy-light contrast support the geminate lightness root.\",\"representative_source_ids\":[\"MG-4b031992\",\"QS-5559ee54\",\"QF-9aeea070\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:1:coordinate-reopening","source_type":"word_analysis","support_id":"sup_4c453c460ecc4fbb42ac","text":"{\"blocking_evidence\":null,\"headline\":\"closure shifts to reopening\",\"reader_payoff\":\"The reader feels the transition from delivered consequence back into a fresh case-frame for the opposite outcome.\",\"reason\":\"The prior ayah closes the first branch, and this conjunction licenses a coordinated reopening rather than a chronological next event.\",\"representative_source_ids\":[\"QT-1a2fd53a\",\"QB-ee1ac35d\",\"QS-b8dfc15c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:3:generic-individualized-person","source_type":"word_analysis","support_id":"sup_5cf690c8e85579e166e0","text":"{\"blocking_evidence\":null,\"headline\":\"generic person individualized by suffixes\",\"reader_payoff\":\"The reader notices that the judgment is universal in reach but still lands on each person through the later possessed scales.\",\"reason\":\"The pronoun is indeterminate and conditional-relative, while the possessive suffix on the scale noun is syntactically tied back to it.\",\"representative_source_ids\":[\"QG-6df93342\",\"MG-0dfe1fca\",\"QF-b064359e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:4:reward-to-measurement-reset","source_type":"word_analysis","support_id":"sup_65cd4b0c349b1b4a2b15","text":"{\"blocking_evidence\":null,\"headline\":\"reward state resets to measurement\",\"reader_payoff\":\"The reader feels the discourse leave the prior satisfied life and return to the measurement event that explains why this branch fails.\",\"reason\":\"The perfect verbal condition restarts the negative branch at the evaluative event after the previous nominal reward state.\",\"representative_source_ids\":[\"QT-1a319fff\",\"QB-ca691e30\",\"QB-d9e3a2ff\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:1:coordinated-second-branch","source_type":"word_analysis","support_id":"sup_69a48646fc7ec2a64e00","text":"{\"blocking_evidence\":null,\"headline\":\"coordinated second branch\",\"reader_payoff\":\"The reader notices the ayah as the second side of a balanced judgment partition, not as a loose continuation after the first result.\",\"reason\":\"The local evidence supports coordination with the prior branch and compression with the following detailing particle, while the word remains an opening conjunction rather than an independently complete compound particle.\",\"representative_source_ids\":[\"QG-808ec32d\",\"MG-793a79b1\",\"QF-46a443fa\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:5:instrument-subject","source_type":"word_analysis","support_id":"sup_72133bb6ba074aab8255","text":"{\"blocking_evidence\":null,\"headline\":\"instrument noun reports the verdict\",\"reader_payoff\":\"The reader sees the measuring system itself occupying the subject position, so the verdict sounds impersonal and calibrated.\",\"reason\":\"The noun is an instrument plural and nominative subject of the lightness verb, not an abstract weight or a direct object.\",\"representative_source_ids\":[\"QG-822f0f31\",\"QS-eabb8276\",\"QF-62c0a4a8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:2:delayed-fa-answer","source_type":"word_analysis","support_id":"sup_9209194cfd919e2bd676","text":"{\"blocking_evidence\":null,\"headline\":\"answer delayed across boundary\",\"reader_payoff\":\"The reader notices that the ayah deliberately stops in a grammatically suspended condition whose result must be carried into 101:9.\",\"reason\":\"The local clause is marked as the dependent branch, and the attachment evidence identifies the answer as the following fāʾ-response in 101:9.\",\"representative_source_ids\":[\"QG-da9b7336\",\"QT-1fc205ca\",\"QY-15f99e27\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:2","source_type":"word_analysis","support_id":"sup_a44b9c955a5ea540b18d","text":"{\"gloss_range\":\"conditional-topical detailing particle that classifies a case and suspends its answer until the following fāʾ-response in 101:9\",\"prose\":\"{{ar:أَمَّا}} ({{tr:ammā}}) makes the ayah a case-frame before it is a completed report. It introduces the person as a sorted case, but the construction does not finish inside 101:8; the required fāʾ-answer waits in 101:9. That delay is part of the force: the negative branch is classified, measured, and then held open until the next ayah supplies the consequence.\",\"root_display\":\"no root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:أَمَّا}} ({{tr:ammā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:5:possessed-personal-scales","source_type":"word_analysis","support_id":"sup_a66a28de81dd83525055","text":"{\"blocking_evidence\":null,\"headline\":\"possessed scales personalize the case\",\"reader_payoff\":\"The reader notices that the universal case becomes personal through scales bound to the one being judged.\",\"reason\":\"The possessive suffix is syntactically tied back to the generic pronoun and is fused to the plural scale noun.\",\"representative_source_ids\":[\"QG-67ff5765\",\"QG-a2cc4c41\",\"QF-85384c19\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:5","source_type":"word_analysis","support_id":"sup_ae29e9b3b9477c635b84","text":"{\"gloss_range\":\"his plural scales or measuring standards, grammatically the subject of the lightness verb and personally bound to the generic case\",\"prose\":\"{{ar:مَوَٰزِينُهُۥ}} ({{tr:mawāzīnuhū}}) is not the object being weighed; it is the subject whose lightness is reported. The plural instrument noun keeps the scene concrete as scales, while the {{ar:و ز ن}} ({{tr:w-z-n}}) field lets those scales function as standards of worth and calibrated justice. The attached suffix makes them his scales, tying the measures back to the generic person without naming that person. Because the same possessed scale phrase anchors both 101:6 and 101:8, the unchanged noun makes the heavy-light verb swap decisive; cross-surah verdict patterns in 7:8-9 and 23:102-103 reinforce that formula. At the boundary, the word pulls the listener from the prior satisfied-life scene back to the measuring instrument; its long cadence and possessive suffix carry the clause toward the consequence in 101:9, while the ayah itself closes on the scales before stating the result.\",\"root_display\":\"{{ar:و ز ن}} ({{tr:w-z-n}})\",\"root_gloss_range\":\"weighing, measuring, balancing, proportion, worth, and calibrated judgment; locally expressed through a plural instrument noun in a verdict frame\",\"surface_display\":\"{{ar:مَوَٰزِينُهُۥ}} ({{tr:mawāzīnuhū}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:3","source_type":"word_analysis","support_id":"sup_afc747f27278c39fd9cf","text":"{\"gloss_range\":\"generic conditional-relative pronoun, introducing whoever belongs to this case and supplying the antecedent for the later possessive suffix\",\"prose\":\"{{ar:مَنْ}} ({{tr:man}}) keeps the case universal without making it vague. It means the one whose condition fits the branch, so the later possessive suffix can individualize the scales while the person remains unnamed; one generic person is held against plural measures. The word also carries both relative and conditional force: it defines the person by the light-scales clause and points forward to the consequence still waiting in 101:9. It also opens a new parallel person-slot after 101:7, so the listener compares the branches without carrying over the satisfied person's referent.\",\"root_display\":\"no root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مَنْ}} ({{tr:man}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:4:scales-as-subject","source_type":"word_analysis","support_id":"sup_b3ed7105ead292b29dc4","text":"{\"blocking_evidence\":null,\"headline\":\"agreement points to scales\",\"reader_payoff\":\"The reader sees that the grammar reports the condition of the scales, making the measurement itself speak before the person is named again.\",\"reason\":\"The feminine singular verb agrees with the broken plural subject, and attachment evidence makes the scale noun the explicit subject.\",\"representative_source_ids\":[\"QG-ef5a5b5e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:3:relative-conditional-force","source_type":"word_analysis","support_id":"sup_baf6ddfd56ca8056329d","text":"{\"blocking_evidence\":null,\"headline\":\"relative and conditional at once\",\"reader_payoff\":\"The reader sees the word both defining a person by a measured condition and suspending that person toward the next ayah's answer.\",\"reason\":\"Local grammar identifies the pronoun as the complement of the detailing particle and the introducer of the relative clause.\",\"representative_source_ids\":[\"QS-a07f0030\",\"QT-c9020686\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:5:formula-anchor","source_type":"word_analysis","support_id":"sup_bc7a92608f95240abecc","text":"{\"blocking_evidence\":null,\"headline\":\"same scale phrase anchors reversal\",\"reader_payoff\":\"The reader notices that 101:6 and 101:8 keep the same possessed scale phrase while the weight predicate reverses, with 7:8-9 and 23:102-103 confirming a recognizable verdict formula.\",\"reason\":\"The same-surah mirror and cross-surah scale verdicts preserve the formulaic payoff without requiring the parallels to control the local parse.\",\"representative_source_ids\":[\"QI-4bf4c1df\",\"QI-a4209516\",\"QI-b6bbf6f4\",\"QT-9f0f69c9\",\"MT-cd0a55e4\",\"QE-53081ee2\",\"QE-dbe26c6f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:4","source_type":"word_analysis","support_id":"sup_ca7e31fcd21a587fc46f","text":"{\"gloss_range\":\"the scales came up light as a completed measured state; the local scale noun selects insufficiency of weight while allowing moral insubstantiality as pressure\",\"prose\":\"{{ar:خَفَّتْ}} ({{tr:khaffat}}) states the lightness as an accomplished verdict, not as an ongoing test or an outside act of making something light. Its feminine singular agreement keeps the scales as the grammatical subject, so the report falls on the measuring instruments rather than directly saying that the person is light. The geminate {{ar:خ ف ف}} ({{tr:kh-f-f}}) root is essential: this is lightness, not fear, and the prior heavy-scales branch (101:6) makes the antonymic swap carry the whole reversal. Because the same light-scale pairing appears in 7:9 and 23:103, 101:8 can invoke a known failed-weighing formula while holding the consequence until 101:9. After the satisfied-life clause in 101:7, the perfect verb resets the branch from reward state back to the accomplished event of measurement. The clipped doubled sound can register that abrupt insufficiency acoustically, while the root's wider field lets measured lightness feel like moral insufficiency; the local noun still keeps the selected sense tied to scales, not speed or generic triviality.\",\"root_display\":\"{{ar:خ ف ف}} ({{tr:kh-f-f}})\",\"root_gloss_range\":\"lightness, becoming light, quickness or ease, slightness, and levity; locally narrowed to measured lightness in a scale-verdict frame\",\"surface_display\":\"{{ar:خَفَّتْ}} ({{tr:khaffat}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:2:sorting-particle","source_type":"word_analysis","support_id":"sup_e37dc2eb54e51fe11013","text":"{\"blocking_evidence\":null,\"headline\":\"case-sorting particle\",\"reader_payoff\":\"The reader sees grammar enacting judgment: the particle sorts the person into a case before the scale-result is even stated.\",\"reason\":\"The particle is locally conditional and topical at once, preserving both the classification force and the forward consequence requirement.\",\"representative_source_ids\":[\"MG-bc36c38f\",\"QS-0aa57043\",\"QT-cdad9e5b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:4:antithetical-scale-verb","source_type":"word_analysis","support_id":"sup_f764a3a828bc9946e87d","text":"{\"blocking_evidence\":null,\"headline\":\"light verb reverses heavy verb\",\"reader_payoff\":\"The reader notices that one predicate swap against 101:6 reverses the entire fate while the scale frame remains constant.\",\"reason\":\"The same-surah frame repeats the scale construction, and the verb changes from heaviness to lightness in the same evaluative slot.\",\"representative_source_ids\":[\"QS-173e29fc\",\"QI-62090e99\",\"QT-4431bf6c\",\"QE-89959948\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:8:5:plural-justice-standards","source_type":"word_analysis","support_id":"sup_fca691ab973d5c7e39eb","text":"{\"blocking_evidence\":null,\"headline\":\"plural scales as calibrated standards\",\"reader_payoff\":\"The reader holds together concrete scales, multiple measures, and standards of worth without reducing the word to either hardware alone or a free metaphor alone.\",\"reason\":\"The plural instrument noun and root field preserve measuring, worth, and justice pressure, while local grammar keeps the selected image anchored in scales rather than replacing it with an abstract doctrine or unrelated cosmic measure.\",\"representative_source_ids\":[\"QS-497ff9bc\",\"QS-59673315\",\"QS-b19847a4\",\"MS-e40a46d7\",\"QF-40f673d9\",\"QY-b8dd39fc\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ","ayah_ref":"101:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000427/B003","root_001645/B001","root_001645/B002"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000427","role":"Fewness supplies reduced quantity and makes the measured record evidentially insufficient.","root":"خ ف ف","source_ref":"101:8","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001645","role":"Estimation by weight supplies the act of appraising what the record amounts to.","root":"و ز ن","source_ref":"101:8","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_001645","role":"Equitable accounting makes the appraisal adjudicative rather than merely physical.","root":"و ز ن","source_ref":"101:8","source_word_indices":["4"]}],"changed_reading":{"after":"His multiple reckonings yield too little evidentiary load to carry his case.","before":"His scales have little physical weight."},"confidence":"strong","focus_anchor":"The predicated lightness of خَفَّتْ attaches to the possessive plural مَوَازِينُهُ.","mechanism":"Fewness and reduced load combine with appraisal and just accounting: the plural balances aggregate assessments, but the material available to them is insufficient to establish countervailing weight.","model_id":"B01_evidentiary_deficit"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:B01_evidentiary_deficit","source_type":"hft","support_id":"sup_f95bd775dbe5f04e5483","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ","ayah_ref":"101:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000427/B005","root_001645/B007"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000427","role":"Disparagement supplies the social act of making a person or right count for little.","root":"خ ف ف","source_ref":"101:8","source_word_indices":["3"]},{"branch_id":"B007","mapped_root_id":"root_001645","role":"Weight as standing or worth turns low weight into failed recognized significance.","root":"و ز ن","source_ref":"101:8","source_word_indices":["4"]}],"changed_reading":{"after":"The apparatus of his standing has become negligible: his claim carries no acknowledged weight.","before":"The verse reports a numerical shortfall."},"confidence":"medium","focus_anchor":"The same lightness verb and possessive balances can activate insignificance and recognized worth within their own focus-root inventories.","mechanism":"Disparagement or treating a right as negligible intersects with weight as standing and value. The balances can therefore be light because the claim they register has lost acknowledged significance, not only because a pan contains little.","model_id":"B02_devalued_standing"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:B02_devalued_standing","source_type":"hft","support_id":"sup_88ccbdfc18ccc7ec8393","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ","ayah_ref":"101:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000427/B004","root_001645/B005"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000427","role":"Levity and agitation supply instability within the act of evaluation.","root":"خ ف ف","source_ref":"101:8","source_word_indices":["3"]},{"branch_id":"B005","mapped_root_id":"root_001645","role":"Steady, weighty judgment supplies the state that the agitated balances fail to attain.","root":"و ز ن","source_ref":"101:8","source_word_indices":["4"]}],"changed_reading":{"after":"His criteria of judgment cannot themselves settle into a weighty decision; they tilt and flicker.","before":"The balances settle a result whose total is low."},"confidence":"exploratory","focus_anchor":"خَفَّتْ can carry agitation while مَوَازِينُ can carry steadiness of judgment.","mechanism":"The focus roots form a qualitative opposition between levity and weighty deliberation. Light balances may be evaluative criteria that cannot settle, oscillating instead of reaching a firm judgment.","model_id":"B03_unsettled_judgment"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:B03_unsettled_judgment","source_type":"hft","support_id":"sup_374aea94482de53dc43a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ","ayah_ref":"101:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000427/B001","root_001645/B003","root_001645/B008"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000427","role":"Reduced load supplies the diminished force borne by the relational structure.","root":"خ ف ف","source_ref":"101:8","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_001645","role":"Balancing and alignment make the scales a network of correspondences rather than a single total.","root":"و ز ن","source_ref":"101:8","source_word_indices":["4"]},{"branch_id":"B008","mapped_root_id":"root_001645","role":"Measured proportion supplies the coherent whole whose internal fit has failed.","root":"و ز ن","source_ref":"101:8","source_word_indices":["4"]}],"changed_reading":{"after":"The relations that should make his account proportionate no longer align into load-bearing weight.","before":"One side simply contains less."},"confidence":"medium","focus_anchor":"The plural balances join reduced load to comparison, alignment, and measured proportion.","mechanism":"A balance is not only a container but a relation between terms. Its lightness can mark the failure of correspondences that should align action, value, and measure into a proportioned whole.","model_id":"B04_failed_proportion"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:B04_failed_proportion","source_type":"hft","support_id":"sup_588f2e617ee9e4c86ffd","trust":"legacy_unbound"}]}
</lane_packet_json>
