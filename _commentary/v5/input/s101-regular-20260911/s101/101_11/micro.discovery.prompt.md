# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **101:11**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s101-regular-20260911/s101/101_11/micro.discovery.json` and modify nothing
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
  "ayah_ref": "101:11",
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
{"branch_registry":[{"boundary":"Isı durumu ile bir şeyi ısıtma birlikte yer alır; ata ve metallere ilişkin kullanımlar bu çekirdeğin özel gerçekleşmeleridir.","branch_kind":"mixed_non_bare","branch_ref":"root_000358/B001","candidate_links":[{"candidate_id":"cand_5e6b9eaec877d6f1636e","lane":"micro"},{"candidate_id":"cand_5c24bde719f39f52e0b8","lane":"micro"},{"candidate_id":"cand_1a1863173e9f041ca7cd","lane":"micro"},{"candidate_id":"cand_db9a48af999f394e0b7b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَامِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:HaAmiyap|ROOT:Hmy|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:11:2:1","qac_word_ref":"101:11:2","surface_ar":"حَامِيَةٌۢ"}],"gloss":"ısınma ve ısıtma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesne ya da ortam ısınır ve sıcaklığı artar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Demir gibi bir metal ateşte bilerek ısıtılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bedenin ısısı ile koşudan sonra ısınıp terleyen at aynı ısı çekirdeğine bağlanır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Altın ve gümüşün ısıtma işleminden güzel çıkması, işlemin sonucuna ilişkin özel bir kullanımdır."}}],"root_ar":"ح م ي","root_id":"root_000358","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem kendiliğinden ya da durumsal ısınma yönünü hem de bir şeyi ısıtma yönünü birlikte karşılar.","boundary_detail":"Isı durumu ile bir şeyi ısıtma birlikte yer alır; ata ve metallere ilişkin kullanımlar bu çekirdeğin özel gerçekleşmeleridir.","branch_image_ar":"الحرارة والإحماء","concept_gloss":"ısınma ve ısıtma","contextual_glosses":[{"applicability":"Gün, ocak ya da metal gibi bir şeyin belirgin ölçüde ısındığı bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Beden, terleyen at ve işlemden iyi çıkan metal kapsamını tek başına vermez.","preserves":"Belirgin ısı artışını korur."},"facet_ids":["F001","F002"],"text":"iyice kızmak","usage_role":"contextual"}],"definition":"Bir şeyin sıcak duruma gelmesi, ısısının güçlenmesi ya da ateş gibi bir kaynakla ısıtılmasıdır. Bedende ve koşan atta beliren ısı ile metalin ısıtma sonunda iyi duruma gelmesi bunun özel görünümleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesne ya da ortam ısınır ve sıcaklığı artar."},{"facet_id":"F002","role":"specialization","statement":"Demir gibi bir metal ateşte bilerek ısıtılır."},{"facet_id":"F003","role":"extension","statement":"Bedenin ısısı ile koşudan sonra ısınıp terleyen at aynı ısı çekirdeğine bağlanır."},{"facet_id":"F004","role":"associated_use","statement":"Altın ve gümüşün ısıtma işleminden güzel çıkması, işlemin sonucuna ilişkin özel bir kullanımdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Zararı savma ve yaklaşmayı önleme anlamı ekler.","collision":"Koruma ve yasaklama dalıyla karışır.","fit":"displacement","loses":"Isınma ve ısıtma çekirdeğini bütünüyle yitirir.","preserves":"Aynı kökün başka bir dalıyla biçim bağını korur."},"text":"koruma"}],"identity_rationale":"Kaynak sözü, bir şeyin ısınmasını ve ısısının artmasını temel alır; ayrıca demirin ateşte ısıtılmasını, günün ve ocağın kızışmasını, beden ısısını, koşudan terleyen atı ve ısıtıldıktan sonra iyi çıkan altın ile gümüşü kapsar. Bu yüzden verilen çerçeve kaynak kapsamını doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"ısındı, sıcaklığı arttı"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"demiri ateşte ısıttı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"at koşudan ısınıp terledi"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"altın ve gümüşü ısıtma, bu işlemden iyi çıkma"}],"lexicalization_note":"Tanım, genel ısınma çekirdeğini özel söz öbeklerinden ayırır; demir, at ve değerli metal kullanımları bütün dala yayılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yalnız genel sıcaklık alanı ile şiddet dalı sınırı belirginleştiren yararlı karşıtlıklar sundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu, sıcaklığı geniş bir nitelik alanı olarak verir; odak dal ise ısınma sürecini ve ısıtma eylemini özel canlı ve metal kullanımlarıyla birlikte taşır.","focus_only":"Bir şeyi ateşte ısıtma, koşudan terleyen at ve ısıtılmış metal sonucu bu dalda ayrıca bulunur.","gloss":"genel sıcaklık","neighbor_only":"Tat, hava ve sıcaklığın soğuğa karşı genel niteliği komşuda daha geniş yer tutar.","neighbor_ref":"root_000306/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin sıcak olmasını ve ısısının artmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal gerçek sıcaklık değişimini anlatır; komşu dal içki, acı ya da başka bir şeyin etkisindeki keskin yükselişi anlatır.","focus_only":"Gerçek fiziksel ısınma ve bir nesneyi ısıtma bu dala özgüdür.","gloss":"ısı ile şiddet","neighbor_only":"İçkinin yükselen etkisi, acının keskinliği ve genel şiddet komşu dala özgüdür.","neighbor_ref":"root_000358/B008","relation_type":"near_neighbor","shared_zone":"İki dalda da yükselme ve güçlenme tasarımı vardır."}],"source_phrase_ar":"حمي الشيء يحمى حميا إذا سخن (ayn)؛ الحامية الحارة (ayn)؛ حمى النهار وحمي التنور أي اشتد حره (sihah)؛ أحميت الحديد في النار فهو محمى (sihah)؛ الحمي الحرارة المتولدة من الجواهر المحمية كالنار والشمس ومن القوة الحارة في البدن (mufradat)؛ حمي الفرس إذا عرق يحمى حميا وحمى الشد مثله (ayn;tahdhib)؛ هذا الذهب والفضة لحسن الحماء أي خرج من الحماء حسنا (ayn;tahdhib)","source_summary":"Kaynaklar ısınma ve ısıtma çekirdeğinde birleşir; gün, ocak, ateş, beden ve koşan at bu çekirdeğin ortam ve canlı örnekleridir. Metal örneği ise ısıtma işlemi ile bu işlemden iyi çıkma sonucunu birlikte gösterir.","sources":["AY","SI","TA","MU"],"what_is_ar":"حرارة الشيء واشتداد حره وإحماء الحديد وحر النهار والشمس والتنور وحرارة البدن والفرس والشد","what_is_not_ar":"ليس قرابة الزوج ولا الحمأة الطين الأسود"},"support_links":["sup_1a709eb0c6ceffb62cb3","sup_1cbc60c875be9c5e4f1e","sup_8c2f90e06aa06a751714","sup_f1f4b7e2df1eb4727ae6"]},{"boundary":"Çekirdek zararı ya da yaklaşmayı savmadır; korunan alan, yiyecek kısıtlaması ve karşılıklı sakınma özel yapılardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000358/B002","candidate_links":[{"candidate_id":"cand_af7bb7eafdfdcf84091b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَامِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:HaAmiyap|ROOT:Hmy|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:11:2:1","qac_word_ref":"101:11:2","surface_ar":"حَامِيَةٌۢ"}],"gloss":"koruma ve uzak tutma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi ya da şey zarar, saldırı veya istenmeyen yaklaşmaya karşı korunur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir otlak ya da yer başkalarının yaklaşmasına ve yararlanmasına kapatılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hasta, kendisine zarar verecek yiyeceklerden uzak tutulur ya da bunlardan kendisi sakınır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İnsanlar sakıncalı gördükleri bir şeyden uzak durur ve ona yaklaşmaz."}}],"root_ar":"ح م ي","root_id":"root_000358","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Zararı savma ile bir kişi ya da şeyi istenmeyen erişimden uzak tutma yönlerini birlikte karşılar.","boundary_detail":"Çekirdek zararı ya da yaklaşmayı savmadır; korunan alan, yiyecek kısıtlaması ve karşılıklı sakınma özel yapılardır.","branch_image_ar":"الدفع والحماية والمنع","concept_gloss":"koruma ve uzak tutma","contextual_glosses":[{"applicability":"Kişinin yiyecekten ya da tehlikeli gördüğü bir şeyden kendi isteğiyle uzak durduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkasını savunma ve bir alanı erişime kapatma yönlerini vermez.","preserves":"Zarara karşı uzak durma yönünü korur."},"facet_ids":["F003","F004"],"text":"zarardan sakınmak","usage_role":"contextual"}],"definition":"Bir kişiye, topluluğa, yere ya da şeye yönelebilecek zararı veya yaklaşmayı savmak ve onu erişimden uzak tutmaktır. Korunan otlak, hastaya zararlı yiyeceği yasaklama ve insanların tehlikeli gördükleri şeyden kaçınması bu çekirdeğin özel düzenlemeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi ya da şey zarar, saldırı veya istenmeyen yaklaşmaya karşı korunur."},{"facet_id":"F002","role":"specialization","statement":"Bir otlak ya da yer başkalarının yaklaşmasına ve yararlanmasına kapatılır."},{"facet_id":"F003","role":"specialization","statement":"Hasta, kendisine zarar verecek yiyeceklerden uzak tutulur ya da bunlardan kendisi sakınır."},{"facet_id":"F004","role":"extension","statement":"İnsanlar sakıncalı gördükleri bir şeyden uzak durur ve ona yaklaşmaz."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"İncinmiş onurdan doğan öfkeyi ekler.","collision":"Onur ve öfke dalıyla karışır.","fit":"displacement","loses":"Koruma, savma ve yaklaşmayı önleme çekirdeğini yitirir.","preserves":"Kimi bağlamlarda tepki ve direnme düşüncesi çağrıştırır."},"text":"öfkeli onur"}],"identity_rationale":"Kaynak sözü, bir kişiyi ya da şeyi tehlikeden savmayı temel alır ve buradan korunan otlak, yaklaşılması yasak şey, hastayı zararlı yiyecekten uzak tutma, insanların bir şeyden sakınması ve savaşta yakınları koruma kullanımlarına açılır. Verilen koruma ve önleme çerçevesi bu yapıyı doğru kurar.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"onu korudu, yaklaşanı savdı"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"otlatmaya kapalı korunan yer"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yeri korunan ve girilmez alan yaptı"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"hastaya zararlı yiyeceği yasakladı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"hasta sakıncalı yiyeceklerden uzak durdu"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"insanlar ondan sakınıp uzak durdu"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"onu savundu ve korudu"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yanındakileri ya da kendini koruyan kişi veya topluluk"}],"lexicalization_note":"Genel koruma çekirdeği korunur; otlak, hasta, yiyecek ve kaçınma yapılarının özel kapsamı yalın koruma anlamına katılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; savma ve zarar karşısında koruma dalları, kapsam farklarını göstermede en yararlı iki komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekler büyük ölçüde örtüşür; odak dal, erişimi yasaklama ve kişinin yiyecekten ya da tehlikeden sakınması yönlerine de düzenli biçimde uzanır.","focus_only":"Korunan otlak, hastanın yiyeceği ve insanların karşılıklı sakınması bu dalın ek kapsamıdır.","gloss":"savma ve koruma","neighbor_only":"Zarar vereni açıkça kovma ve korunan çevreye yönelen tehdidi püskürtme komşuda daha baskındır.","neighbor_ref":"root_000507/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir kişiyi, topluluğu veya korunan alanı tehlikeden savmayı anlatır."},{"boundary_match":"partial","distinction":"Komşu, zarara karşı koruyucu araç veya engeli öne çıkarır; odak dal ise savma, erişimi kapatma ve sakınmayı aynı anlam alanında toplar.","focus_only":"Bir yeri yasak alan yapma ve başkalarını yaklaşmaktan alıkoyma bu dalda belirgindir.","gloss":"zarara karşı koruma","neighbor_only":"Zarar ile korunan şey arasına koruyucu bir engel koyma komşu dalın özel anlatımıdır.","neighbor_ref":"root_001677/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın çekirdeğinde zararı önleme ve korunan şeyi esirgeme vardır."}],"source_phrase_ar":"حميت القوم حماية وكل شيء دفعت عنه فقد حميته (ayn)؛ الحمى موضع فيه كلأ يحمى من الناس أن يرعى (ayn;tahdhib)؛ حميته حماية إذا دفعت عنه (sihah)؛ هذا شيء حمى أي محظور لا يقرب (sihah)؛ حميت المريض حمية منعته أكل ما يضره (ayn)؛ حاميت عنه محاماة وحماء (sihah)؛ تحاماه الناس أي توقوه واجتنبوه (sihah)؛ حمى أهله في القتال حماية (tahdhib)","source_summary":"Kaynaklar, bir şeye yönelen zararı veya yaklaşmayı savma çekirdeğini ortaklaşa verir. Bu çekirdek savaşta yakınları savunmaya, erişimi kapatılmış yere, hastayı zararlı yiyecekten uzak tutmaya ve insanların bir şeyden sakınmasına uygulanır.","sources":["AY","SI","TA","MU"],"what_is_ar":"دفع الشيء وحمايته ومنع القرب منه والحمى المحظور وحماية القوم والأهل والحمية عن الطعام والتحامي والاجتناب","what_is_not_ar":"ليس الحمية بمعنى الأنفة والغضب ولا الحام من الإبل"},"support_links":["sup_0c97f3d4cf7e81ec7639"]},{"boundary":"Onur incinmesi, utanç ve aşağılanmayı kabul etmeme belirgin kullanımlardır; bunun yanında birine doğrudan öfkelenme de ayrıca tanıklanır.","branch_kind":"mixed_non_bare","branch_ref":"root_000358/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَامِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:HaAmiyap|ROOT:Hmy|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:11:2:1","qac_word_ref":"101:11:2","surface_ar":"حَامِيَةٌۢ"}],"gloss":"gücenme ve öfkelenme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir şey karşısında gücenip öfkelenir veya öfkesini doğrudan bir kişiye yöneltir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi onuruna yediremediği bir durum karşısında utançla karışık gücenme ve öfke duyar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aşağılanmayı kabul etmeyen onurlu tutum, bedenin bir parçası üzerinden kurulan kalıp bir anlatımla belirtilir."}}],"root_ar":"ح م ي","root_id":"root_000358","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem onur incinmesine bağlı gücenmeyi hem de bir kişiye yönelen doğrudan öfkeyi karşılar.","boundary_detail":"Onur incinmesi, utanç ve aşağılanmayı kabul etmeme belirgin kullanımlardır; bunun yanında birine doğrudan öfkelenme de ayrıca tanıklanır.","branch_image_ar":"الحمية والأنفة والغضب","concept_gloss":"gücenme ve öfkelenme","contextual_glosses":[{"applicability":"Kişinin bir durumu kendisine yakıştıramayıp utanç, gücenme ve öfke duyduğu bağlamlarda doğal bir anlatımdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Doğrudan birine öfkelenmeyi ve öfke gücünün kabarıp çoğalmasını tek başına vermez.","preserves":"Onur incinmesini ve durumu kabul etmeme yönünü korur."},"facet_ids":["F001"],"text":"gururuna yedirememek","usage_role":"contextual"}],"definition":"Bir şey karşısında gücenme ve öfkelenme ya da birine doğrudan öfkelenme durumudur. Kişinin bunu onuruna yedirememesi, utanç duyması ve içindeki öfke gücünün kabarıp çoğalması bu alanın belirgin görünümleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir şey karşısında gücenip öfkelenir veya öfkesini doğrudan bir kişiye yöneltir."},{"facet_id":"F002","role":"specialization","statement":"Kişi onuruna yediremediği bir durum karşısında utançla karışık gücenme ve öfke duyar."},{"facet_id":"F003","role":"associated_use","statement":"Aşağılanmayı kabul etmeyen onurlu tutum, bedenin bir parçası üzerinden kurulan kalıp bir anlatımla belirtilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Dışarıdan gelen zararı önleme eylemi ekler.","collision":"Koruma ve uzak tutma dalıyla karışır.","fit":"displacement","loses":"Gücenme ve öfke duygusunu yitirir.","preserves":"Onuru savunma çağrışımını dolaylı olarak koruyabilir."},"text":"korumak"}],"identity_rationale":"Kaynak sözü, kişinin bir şeyi onuruna yedirememesi, bundan utanç ve gücenme duyması, birine doğrudan öfkelenmesi ve öfke gücünün kabarıp çoğalması durumlarını birlikte verir. Bu nedenle dal hem onura bağlı hiddeti hem de doğrudan öfkeyi kapsar.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"onuruna yedirememe, gücenme ve öfke"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"ona öfkelendi"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"onurlu, aşağılanmayı kabul etmeyen"}],"lexicalization_note":"Tanım, onur kaynaklı duygu çekirdeğini korur; birine öfkelenme ve burnu üzerinden kurulan kalıp anlatımın kapsamı ayrıştırılır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; onurla uyanan öfke dalı en yakın sınırı verir, öteki adaylar ya genel öfke ya da yalnız aynı durum alanındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, utancı ve aşağılanmayı kabul etmemeyi açıkça çekirdeğe alır; komşu dal aynı duyguyu koruma güdüsüyle daha sıkı bağlar.","focus_only":"Utanç duygusu ve bir şeyi kendine yedirememe bu dalda açık bir koşuldur.","gloss":"onurla kabaran öfke","neighbor_only":"Öfkeyi uyandıran şeyi koruma duygusuyla birlikte ele alma komşu dalda daha belirgindir.","neighbor_ref":"root_000342/B005","relation_type":"near_synonym","shared_zone":"İki dal da onur duygusunun uyardığı öfke ve gücenme alanında buluşur."}],"source_phrase_ar":"حميت من هذا الشيء أحمى منه حمية أي أنفت أنفا وغضبا (ayn)؛ حميت عن كذا حمية ومحمية إذا أنفت منه وداخلك عار وأنفة (sihah)؛ حميت عليه غضبت (sihah)؛ حمى فلان أنفه يحميه حمية ومحمية (tahdhib)؛ عبر عن القوة الغضبية إذا ثارت وكثرت بالحمية (mufradat)","source_summary":"Kaynaklar, onura dokunan bir durumdan ötürü gücenme ve öfkelenmeyi ortak çekirdek olarak verir. Bu duygu utançla iç içe geçebilir, bir kişiye yönelebilir ve içteki öfke gücünün kabarması olarak anlatılabilir.","sources":["AY","SI","TA","MU"],"what_is_ar":"الأنفة والغيظ والغضب وحمية الأنف والحمية التي تثور في النفس","what_is_not_ar":"ليس الحمى الموضع المحظور ولا حرارة الأجسام"},"support_links":[]},{"boundary":"Kapsam koca tarafından gelen yakınlarla sınırlıdır; kadın tarafından gelen yakınlar ve iki tarafı birden kapsayan genel evlilik bağı bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000358/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَامِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:HaAmiyap|ROOT:Hmy|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:11:2:1","qac_word_ref":"101:11:2","surface_ar":"حَامِيَةٌۢ"}],"gloss":"kocanın yakınları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadının kocasının tarafından gelen yakınları topluca adlandırılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kocanın babası ve erkek kardeşi bu yakınların başlıca tekil örnekleridir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kocanın annesi, kadın açısından ayrı bir akrabalık adıyla belirtilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kocanın erkek yakınıyla baş başa kalmanın ağır tehlikesi kalıp bir uyarıyla anlatılır."}}],"root_ar":"ح م ي","root_id":"root_000358","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kadın açısından kocanın anne, baba, kardeş ve öteki yakınlarını kapsayan akrabalık alanını karşılar.","boundary_detail":"Kapsam koca tarafından gelen yakınlarla sınırlıdır; kadın tarafından gelen yakınlar ve iki tarafı birden kapsayan genel evlilik bağı bu dala girmez.","branch_image_ar":"قرابة الزوج","concept_gloss":"kocanın yakınları","contextual_glosses":[{"applicability":"Kocanın ailesinden bir yakını tekil ve cinsiyetten bağımsız biçimde belirtmek gereken bağlamlarda kullanılabilir.","error_profile":{"adds":"Güncel kullanımda eşin iki tarafından gelen yakınları da kapsayabilir.","collision":"Kadının kendi tarafından gelen evlilik yakınlarıyla karışabilir.","fit":"broadening","loses":null,"preserves":"Evlilik yoluyla kurulan akrabalık yönünü korur."},"facet_ids":["F001"],"text":"kayın hısımı","usage_role":"contextual"}],"definition":"Evli bir kadının kocası tarafından gelen baba, anne, kardeş ve öteki yakınlarıdır. Kocanın erkek yakınıyla baş başa kalmanın ağır tehlikesini bildiren kalıp söz bu akrabalık çekirdeğine bağlı özel bir kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadının kocasının tarafından gelen yakınları topluca adlandırılır."},{"facet_id":"F002","role":"specialization","statement":"Kocanın babası ve erkek kardeşi bu yakınların başlıca tekil örnekleridir."},{"facet_id":"F003","role":"specialization","statement":"Kocanın annesi, kadın açısından ayrı bir akrabalık adıyla belirtilir."},{"facet_id":"F004","role":"associated_use","statement":"Kocanın erkek yakınıyla baş başa kalmanın ağır tehlikesi kalıp bir uyarıyla anlatılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kadın tarafından gelen yakınları da kapsama alır.","collision":"İki taraflı genel evlilik akrabalığıyla karışır.","fit":"broadening","loses":null,"preserves":"Evlilik yoluyla kurulan yakınlık alanını korur."},"text":"eşin bütün hısımları"}],"identity_rationale":"Kaynak sözü, kadının kocasının babasını, kardeşini, annesini ve koca tarafından gelen öteki yakınları aynı akrabalık alanında toplar; ayrıca kocanın erkek yakınıyla baş başa kalmanın ağır sakıncasını bildiren kalıp sözü verir. Verilen koca tarafı akrabalığı çerçevesi bunu doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kocanın babası, erkek kardeşi ya da başka bir erkek yakını"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kadının kocası tarafından gelen yakınları"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"kadının kayınvalidesi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kocanın erkek yakınıyla baş başa kalmak ölüm kadar tehlikelidir"}],"lexicalization_note":"Koca tarafındaki akrabalık çekirdeği korunur; anne, baba, kardeş ve uyarı sözü gibi biçime bağlı ayrımlar birbirine karıştırılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı koca tarafı akrabalığını veren dal gerçek eşanlamlıdır, öteki adayların akrabalık yönü ya da çekirdeği farklıdır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek ve yön sınırı aynıdır; anneye ilişkin özel ad ile uyarı sözü, ortak akrabalık çekirdeğine bağlı ayrıntılardır.","focus_only":null,"gloss":"koca tarafının yakınları","neighbor_only":null,"neighbor_ref":"root_000354/B003","relation_type":"synonym","shared_zone":"İki dal da kadına göre kocanın babası, erkek kardeşi ve koca tarafından gelen yakınları adlandırır."}],"source_phrase_ar":"الحمو أبو الزوج وأخو الزوج وكل من ولي الزوج من ذي قرابته فهم أحماء المرأة وأم زوجها حماتها (ayn;tahdhib)؛ حماة المرأة أم زوجها (sihah;tahdhib)؛ كل شيء من قبل الزوج مثل الأب والأخ فهم الأحماء واحدهم حما (sihah)؛ الأحماء من قبل الزوج والأختان من قبل المرأة (tahdhib)؛ الحمو الموت (tahdhib)؛ أحماء المرأة كل من كان من قبل زوجها (mufradat)","source_summary":"Kaynaklar, koca tarafından gelen yakınları ortak bir akrabalık kümesi olarak verir ve kocanın anne, baba ile erkek kardeşini bu kümede ayırt eder. Ağır uyarı bildiren kalıp söz, erkek yakının kadınla baş başa kalmasına ilişkin özel bir kullanımdır.","sources":["AY","SI","TA","MU"],"what_is_ar":"الحمو وأحماء المرأة وحماة المرأة وألفاظ قرابة الزوج وما يتصل بمثل الحمو الموت","what_is_not_ar":"ليس الأختان من قبل المرأة ولا الصهر الجامع للطرفين"},"support_links":[]},{"boundary":"Bu ad yalnız damızlık geçmişi nedeniyle kullanım dışı bırakılan erkek deveye aittir; genel koruma altındaki hayvanı anlatmaz.","branch_kind":"bare","branch_ref":"root_000358/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَامِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:HaAmiyap|ROOT:Hmy|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:11:2:1","qac_word_ref":"101:11:2","surface_ar":"حَامِيَةٌۢ"}],"gloss":"dokunulmaz sayılan damızlık erkek deve","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Damızlık geçmişi belirli bir ölçüye ulaşan erkek devenin sırtı kullanım dışı ve dokunulmaz sayılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu ölçü uzun süre damızlıkta kalma, torun dölletme ya da on batın döl verme biçiminde aktarılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hayvana binilmez, yünü kırkılmaz ve otlakta yemesi engellenmez."}}],"root_ar":"ح م ي","root_id":"root_000358","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanın türünü, damızlık koşulunu ve kullanım dışı bırakılma sonucunu birlikte açıklar.","boundary_detail":"Bu ad yalnız damızlık geçmişi nedeniyle kullanım dışı bırakılan erkek deveye aittir; genel koruma altındaki hayvanı anlatmaz.","branch_image_ar":"الحام من الإبل","concept_gloss":"dokunulmaz sayılan damızlık erkek deve","contextual_glosses":[{"applicability":"Eski uygulamadaki hayvanı, en belirgin kullanım yasağı üzerinden kısa biçimde anlatır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yününün kırkılmaması, otlaktan alıkonmaması ve damızlık eşiğinin ayrıntılarını vermez.","preserves":"Damızlık deveye binilmeme yönünü korur."},"facet_ids":["F001","F003"],"text":"binilmeyen damızlık deve","usage_role":"explanatory"}],"definition":"Damızlıkta uzun süre kullanıldığı ya da belirli bir döl verme ölçüsüne ulaştığı için sırtı dokunulmaz sayılan erkek devedir. Bu hayvana binilmez, yünü kırkılmaz ve otlakta serbestçe yemesi engellenmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Damızlık geçmişi belirli bir ölçüye ulaşan erkek devenin sırtı kullanım dışı ve dokunulmaz sayılır."},{"facet_id":"F002","role":"specialization","statement":"Bu ölçü uzun süre damızlıkta kalma, torun dölletme ya da on batın döl verme biçiminde aktarılır."},{"facet_id":"F003","role":"extension","statement":"Hayvana binilmez, yünü kırkılmaz ve otlakta yemesi engellenmez."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Damızlık koşulu bulunmayan her türlü korunan deveyi kapsar.","collision":"Genel hayvan korumasıyla karışır.","fit":"broadening","loses":null,"preserves":"Hayvanın kullanım dışı bırakılması yönünü kısmen korur."},"text":"korunan deve"}],"identity_rationale":"Kaynak sözü, uzun süre damızlıkta kalan ya da belirli sayıda döl veren erkek devenin sırtının dokunulmaz sayılmasını; ona binilmemesini, yününün kırkılmamasını ve otlaktan alıkonmamasını anlatır. Verilen çerçeve doğrudur, ancak bu ayrıcalık her erkek deveye değil, kaynaklarda farklı biçimde belirtilen damızlık koşulunu karşılayan hayvana aittir.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"binilmeyen, kırkılmayan ve otlaktan alıkonmayan damızlık erkek deve"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"damızlık geçmişi nedeniyle sırtı dokunulmaz sayılan erkek deve"}],"lexicalization_note":"Tanım, yalın hayvan adını kendi eski uygulama sınırında tutar ve genel koruma ya da serbest otlatma anlamlarını dala katmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; eski uygulamayla serbest bırakılan hayvan dalı ortak kullanım yasağına rağmen koşul ve kapsam farkını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın hayvanı erkek ve damızlık geçmişiyle belirlenir; komşu dalın serbest bırakma düzeni tür, neden ve hukuki sonuç bakımından daha geniştir.","focus_only":"Odak, damızlık eşiğine ulaşmış erkek deveye binmeme, onu kırkmama ve otlaktan alıkoymama düzenidir.","gloss":"eski törede serbest bırakılan hayvan","neighbor_only":"Komşu, eski töre ya da adakla serbest bırakılan dişi deveyi ve ayrıca özgür bırakılan köleyi kapsar.","neighbor_ref":"root_000767/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da eski bir uygulamayla yararlanma dışı bırakılan bir hayvan vardır."}],"source_phrase_ar":"الحامي الفحل من الإبل الذي طال مكثه عندهم (sihah)؛ إذا لقح ولد ولده فقد حمى ظهره فلا يركب ولا يجز له وبر ولا يمنع من مرعى (sihah)؛ ولا حام قيل هو الفحل إذا ضرب عشرة أبطن كأن يقال حمى ظهره فلا يركب (mufradat)","source_summary":"Kaynaklar, damızlık geçmişi nedeniyle sırtı dokunulmaz sayılan erkek deve ve ona tanınan binilmeme, kırkılmama, otlaktan alıkonmama ayrıcalıklarında birleşir. Damızlık eşiği uzun süre, torun dölü ya da on batın ölçüsüyle farklı biçimlerde anlatılır.","sources":["SI","MU"],"what_is_ar":"الفحل من الإبل إذا حمى ظهره فلا يركب ولا يجز وبره ولا يمنع من مرعى","what_is_not_ar":"ليس مطلق الحماية ولا حامي القوم"},"support_links":[]},{"boundary":"Çekirdek kara ve kimi anlatımlarda kötü kokulu balçıktır; suyun kendisi, genel bulanıklık ve başka tür tortular dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000358/B006","candidate_links":[{"candidate_id":"cand_3517e6fa56f85e7cd47c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَامِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:HaAmiyap|ROOT:Hmy|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:11:2:1","qac_word_ref":"101:11:2","surface_ar":"حَامِيَةٌۢ"}],"gloss":"kara ve kötü kokulu balçık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Madde kara ve çoğu kez kötü kokulu bir balçıktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Akarsu ya da kuyudan çıkarılan balçık bu adla anılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir pınar, içinde bu balçık bulunduğu için balçıklı diye nitelenir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kuyudaki balçık çıkarılabilir ya da kuyuya balçık konabilir."}}],"root_ar":"ح م ي","root_id":"root_000358","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Maddenin rengini, yapısını ve kaynaklarda öne çıkan kokusunu birlikte karşılar.","boundary_detail":"Çekirdek kara ve kimi anlatımlarda kötü kokulu balçıktır; suyun kendisi, genel bulanıklık ve başka tür tortular dala girmez.","branch_image_ar":"الحمأة والطين الأسود","concept_gloss":"kara ve kötü kokulu balçık","contextual_glosses":[{"applicability":"Pınarın içinde kara balçık bulunduğunu belirten yer nitelemesi olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Balçığın genel madde anlamını ve kuyudaki işlemleri vermez.","preserves":"Su kaynağında balçık bulunması yönünü korur."},"facet_ids":["F003"],"text":"balçıklı pınar","usage_role":"contextual"}],"definition":"Kara, çoğu anlatımda kötü kokulu olan ve akarsu, kuyu ya da pınar çevresinde bulunan balçıktır. Bir su kaynağında bu balçığın bulunması, kuyudan çıkarılması veya kuyuya konması bu madde çekirdeğine bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Madde kara ve çoğu kez kötü kokulu bir balçıktır."},{"facet_id":"F002","role":"specialization","statement":"Akarsu ya da kuyudan çıkarılan balçık bu adla anılır."},{"facet_id":"F003","role":"associated_use","statement":"Bir pınar, içinde bu balçık bulunduğu için balçıklı diye nitelenir."},{"facet_id":"F004","role":"extension","statement":"Kuyudaki balçık çıkarılabilir ya da kuyuya balçık konabilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Suyun kendisini ve genel bulanıklığı anlamın merkezine koyar.","collision":"Bulanmış su ve tortu dallarıyla karışır.","fit":"displacement","loses":"Kara, kötü kokulu balçığın madde kimliğini yitirir.","preserves":"Su ile toprak karışımı çağrışımını korur."},"text":"bulanık su"}],"identity_rationale":"Kaynak sözü, kara ve kötü kokulu balçığı, akarsu ya da kuyudan çıkarılan balçığı, balçıklı pınarı ve kuyudan balçık çıkarma ya da kuyuya balçık koyma eylemlerini birlikte verir. Verilen kara balçık çerçevesi bu çekirdeği doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kara ve kötü kokulu balçık"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kara balçık, akarsu ya da kuyudan çıkarılan balçık"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"balçıklı pınar"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kuyunun balçığını çıkardı"}],"lexicalization_note":"Balçık adı temel alınır; balçıklı pınar ile kuyudan çıkarma veya kuyuya koyma yapıları ayrı özel kullanımlar olarak tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kara balçığı aynı yer ve işlem sınırlarıyla veren dal gerçek eşanlamlıdır, diğerleri yalnız aynı madde alanındadır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek ve sınırlar aynıdır; yer ve işlem örnekleri ortak madde anlamının bağımlı görünümleridir.","focus_only":null,"gloss":"sudaki kara balçık","neighbor_only":null,"neighbor_ref":"root_000354/B001","relation_type":"synonym","shared_zone":"İki dal da kara, kötü kokulu balçığı; balçıklı su kaynağını ve kuyudaki balçık işlemlerini kapsar."}],"source_phrase_ar":"الحمأ الطين الأسود المنتن (ayn)؛ يسمى الطين الذي نبث من النهر الحمأة (ayn)؛ عين حمئة أي ذات حمأة (ayn;mufradat)؛ الحمأة والحمأ طين أسود منتن (mufradat)؛ حمأت البئر أخرجت حمأتها وأحمأتها جعلت فيها حما (mufradat)","source_summary":"Kaynaklar kara ve kötü kokulu balçık çekirdeğinde birleşir; akarsu, kuyu ve pınar bu maddenin bulunduğu yerlerdir. Kaynak sözü ayrıca kuyudan balçık çıkarma ile kuyuya balçık koyma yönlerini ayırır.","sources":["AY","MU"],"what_is_ar":"الحمأ والحمأة والطين الأسود المنتن وما في البئر والعين الحمئة","what_is_not_ar":"ليس حمى الموضع المحظور ولا الحُمَة السم"},"support_links":["sup_5a313d3382ca1d178087"]},{"boundary":"Gönderim sokucu canlının iğnesine değil, zehrine, zararına ve zehrin yakıcı etkisine yöneliktir.","branch_kind":"mixed_non_bare","branch_ref":"root_000358/B007","candidate_links":[{"candidate_id":"cand_3c7feb0f5d2e6730bc05","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَامِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:HaAmiyap|ROOT:Hmy|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:11:2:1","qac_word_ref":"101:11:2","surface_ar":"حَامِيَةٌۢ"}],"gloss":"sokucu hayvan zehrinin yakıcı etkisi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sokan ya da ısıran bir canlının zehri ve verdiği zarar anlatılır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Zehrin yakıcı sıcaklığı ve hızla kabaran etkisi anlamın bir parçasıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Akrep söz konusu olduğunda gönderim iğneye değil, zehre ve onun zararına yönelir."}}],"root_ar":"ح م ي","root_id":"root_000358","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Zehrin kaynağını, zararını ve yakıcı yükselişini birlikte karşılayan açıklayıcı bir üst karşılıktır.","boundary_detail":"Gönderim sokucu canlının iğnesine değil, zehrine, zararına ve zehrin yakıcı etkisine yöneliktir.","branch_image_ar":"الحُمَة وحرارة السم","concept_gloss":"sokucu hayvan zehrinin yakıcı etkisi","contextual_glosses":[{"applicability":"Akrebin sokması ve bunun verdiği zarar söz konusu olduğunda en doğal kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka sokucu ya da ısırıcı canlıları ve zehrin yakıcı etki vurgusunu daraltır.","preserves":"Akrep zehri ve onun zararını korur."},"facet_ids":["F001","F003"],"text":"akrep zehri","usage_role":"contextual"}],"definition":"Sokan ya da ısıran bir canlının verdiği zehir ve bu zehrin bedende duyulan yakıcı, hızla yükselen etkisidir. Ad, özellikle akrebin zehrini ve zararını belirtir; iğnenin kendisini belirtmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sokan ya da ısıran bir canlının zehri ve verdiği zarar anlatılır."},{"facet_id":"F002","role":"core","statement":"Zehrin yakıcı sıcaklığı ve hızla kabaran etkisi anlamın bir parçasıdır."},{"facet_id":"F003","role":"specialization","statement":"Akrep söz konusu olduğunda gönderim iğneye değil, zehre ve onun zararına yönelir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Zehri taşıyan beden parçasını anlamın kendisi yapar.","collision":"Kaynağın açıkça düzelttiği yaygın kullanımla karışır.","fit":"displacement","loses":"Zehrin kendisini ve yakıcı zararını yitirir.","preserves":"Sokma olayını ve hayvanı korur."},"text":"akrep iğnesi"}],"identity_rationale":"Kaynak sözü, sokan ya da ısıran canlının zehrini ve bu zehrin yakıcı sıcaklığını açıkça verir; halk kullanımında iğnenin kendisine verilen adın doğru olmadığını da belirtir. Verilen zehir ve yakıcı etki çerçevesi kaynak sınırını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"sokan ya da ısıran canlının zehri ve yakıcı etkisi"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"akrebin zehri ve verdiği zarar, iğnesi değil"}],"lexicalization_note":"Zehir ve yakıcı etki çekirdeği korunur; belirli bir sokucu hayvana bağlı söz öbeği genel iğne anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel zehir dalı kapsam sınırını, akrep sokması dalı ise zehir ile eylem ayrımını açıkça gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal zehri sokma ya da ısırma kaynağına ve yakıcı etkisine bağlar; komşu dal zehrin türünü ve bedene giriş yolunu daha geniş tutar.","focus_only":"Sokucu ya da ısırıcı canlının zehri ile onun yakıcı ve kabaran etkisi bu dala özgü sınırdır.","gloss":"bedene giren zehir","neighbor_only":"Yiyeceğe katılan, içirilen veya başka yoldan bedene giren öldürücü zehir komşu dalın daha geniş kapsamındadır.","neighbor_ref":"root_000743/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da hayvansal zehri ve bedene verdiği zararı kapsar."},{"boundary_match":"field_only","distinction":"Biri olayın taşıdığı zehri ve zararı, öteki ise sokma eyleminin kendisini öne çıkarır; bu nedenle birbirlerinin yerine geçmezler.","focus_only":"Odak dal sokma sonrasında verilen zehir ve onun yakıcı etkisidir.","gloss":"akrep sokması","neighbor_only":"Komşu dal doğrudan akrebin sokma eylemini adlandırır.","neighbor_ref":"root_001333/B004","relation_type":"near_neighbor","shared_zone":"İki dal aynı akrep sokması olayında zehir ve eylem katmanlarını paylaşır."}],"source_phrase_ar":"الحُمَة سم كل شيء يلدغ أو يلسع (ayn;tahdhib)؛ حمة العقرب سمها وضرها (sihah)؛ الحمة مخففة حرارة السم وليست كما تسمي العامة حمة العقرب إبرتها (jamhara)؛ هي فوعة السم أي حرارته وفورته (jamhara)؛ بسم العقرب الحمة والحمة (tahdhib)","source_summary":"Kaynaklar sokucu ya da ısırıcı canlının zehri ve zararı üzerinde birleşir; zehrin yakıcı sıcaklığı ile birden yükselen etkisi de çekirdeğin içindedir. Akrep örneğinde iğnenin kendisi açıkça kapsam dışında tutulur.","sources":["JA","SI","TA","AY"],"what_is_ar":"سم ما يلدغ أو يلسع وحرارة السم وفوعته لا إبرة العقرب نفسها","what_is_not_ar":"ليست الإبرة عند التحقيق ولا الحمة المشددة لمعظم الحر"},"support_links":["sup_31d221978bba061d14e8"]},{"boundary":"İçkinin etkisi başlıca özel alandır; ağrı ve genel şiddet kullanımları fiziksel sıcaklık dalıyla özdeşleştirilmemelidir.","branch_kind":"bare","branch_ref":"root_000358/B008","candidate_links":[{"candidate_id":"cand_3c7feb0f5d2e6730bc05","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَامِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:HaAmiyap|ROOT:Hmy|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:11:2:1","qac_word_ref":"101:11:2","surface_ar":"حَامِيَةٌۢ"}],"gloss":"etkinin keskinliği ve şiddeti","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir etki belirgin bir keskinlik, sertlik ve şiddet taşır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İçkinin içene ulaşan ilk yükselişi, yayılışı ve sıcaklığı anlatılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ağrının kabaran keskinliği aynı güçlenme tasarımıyla anlatılır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir şeyin genel sertliği, keskinliği ve şiddeti de bu kapsama uzanır."}}],"root_ar":"ح م ي","root_id":"root_000358","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İçki, ağrı ve başka şeylerde ortak olan güç, keskinlik ve şiddet çekirdeğini karşılar.","boundary_detail":"İçkinin etkisi başlıca özel alandır; ağrı ve genel şiddet kullanımları fiziksel sıcaklık dalıyla özdeşleştirilmemelidir.","branch_image_ar":"سورة الشراب والحدة","concept_gloss":"etkinin keskinliği ve şiddeti","contextual_glosses":[{"applicability":"İçkinin içene ulaşıp ilk kez belirgin ve sıcak bir etki doğurduğu bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ağrının keskinliği ile başka şeylerin genel sertlik ve şiddetini vermez.","preserves":"İçkinin başlangıçta yükselen etkisini korur."},"facet_ids":["F001","F002"],"text":"içkinin ilk çarpması","usage_role":"contextual"}],"definition":"İçkinin içene ulaşırken yayılıp yükselen, kimi anlatımda ilk anda beliren güçlü etkisi ve sıcaklığıdır; aynı ad ağrının kabaran keskinliği ile bir şeyin sertlik ve şiddeti için de kullanılır. Ortak çekirdek etkinin keskinliği ve şiddetidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir etki belirgin bir keskinlik, sertlik ve şiddet taşır."},{"facet_id":"F002","role":"specialization","statement":"İçkinin içene ulaşan ilk yükselişi, yayılışı ve sıcaklığı anlatılır."},{"facet_id":"F003","role":"extension","statement":"Ağrının kabaran keskinliği aynı güçlenme tasarımıyla anlatılır."},{"facet_id":"F004","role":"extension","statement":"Bir şeyin genel sertliği, keskinliği ve şiddeti de bu kapsama uzanır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Fiziksel ısınma dalıyla karışır.","fit":"narrowing","loses":"Yayılma, yükselme, keskinlik ve şiddet öğelerini yitirir.","preserves":"İçkinin sıcaklık yönünü korur."},"text":"sıcaklık"}],"identity_rationale":"Kaynak sözü, içkinin içene ulaşıp yükselen ilk etkisini, yayılışını ve sıcaklığını; ayrıca ağrının kabaran keskinliğini ve genel olarak bir şeyin sertlik ile şiddetini verir. Verilen içki etkisi ve keskinlik çerçevesi bu çok katmanlı kapsamı doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"içkinin ilk yükselişi, sıcaklığı ve içene yayılan etkisi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"ağrının kabaran keskinliği"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"şeyin sertliği ve şiddeti"}],"lexicalization_note":"Mekanik yalın dal sınırı korunur; tanım içkinin etkisini, ağrının keskinliğini ve genel şiddeti tek çekirdeğin kapsamları olarak verir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; içkinin sertleşmesi dalı ortak çekirdeğe en yakın sınırı verir, öteki adaylar yalnız içki alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, etkinin içene ulaşan ilk yükselişini ve başka alanlara uzanan şiddeti kapsar; komşu dal yalnız içkinin sertliğine odaklanır.","focus_only":"İçkinin ilk yükselişi ve içene yayılması yanında ağrı ile genel şiddet kapsamı bu dalda bulunur.","gloss":"içkinin sertleşmesi","neighbor_only":"Komşu dal içkinin yerleşik sertliğini ve güçlü oluşunu daha doğrudan anlatır.","neighbor_ref":"root_001103/B003","relation_type":"near_synonym","shared_zone":"İki dal da içkinin güçlü ve keskin etkisini anlatır."}],"source_phrase_ar":"الحميا بلوغ الخمر من شاربها (ayn)؛ حميا الكأس أول سورتها (sihah)؛ حموة الألم سورته (sihah)؛ حميا الكأس يعني سورتها (tahdhib)؛ الحميا دبيب الشراب (tahdhib)؛ حميا الشيء حدته وشدته (tahdhib)؛ حميا الكأس سورتها وحرارتها (mufradat)","source_summary":"Kaynaklar içkinin içene ulaşıp yayılması, ilk yükselişi ve sıcaklığı çevresinde birleşir. Aynı güçlenme yapısı ağrının keskinliği ile herhangi bir şeyin sertlik ve şiddetine de aktarılır.","sources":["AY","SI","TA","MU"],"what_is_ar":"حميا الكأس والخمر وسورتها ودبيبها وبلوغها الشارب وحدتها وشدة الشيء وحموة الألم","what_is_not_ar":"ليس الحرارة الجسمية العامة ولا الحمية بمعنى الغضب"},"support_links":["sup_31d221978bba061d14e8"]},{"boundary":"Gönderim genel kas dokusuna değil, bacağın içi ya da eni üzerinde belirginleşen özel et ve kas çıkıntısına yöneliktir.","branch_kind":"bare","branch_ref":"root_000358/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَامِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:HaAmiyap|ROOT:Hmy|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:11:2:1","qac_word_ref":"101:11:2","surface_ar":"حَامِيَةٌۢ"}],"gloss":"bacağın içindeki kabarık kas parçası","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bacağın iç tarafında belirgin biçimde kabaran bir et ya da kas parçasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Atın bacağında enine yerleşen iki eş et parçası birlikte adlandırılır."}}],"root_ar":"ح م ي","root_id":"root_000358","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Beden bölümünü, yerini ve çıkıntılı biçimini birlikte belirten açıklayıcı karşılıktır.","boundary_detail":"Gönderim genel kas dokusuna değil, bacağın içi ya da eni üzerinde belirginleşen özel et ve kas çıkıntısına yöneliktir.","branch_image_ar":"لحمة الساق","concept_gloss":"bacağın içindeki kabarık kas parçası","contextual_glosses":[{"applicability":"Atın bacağındaki iki eş parçanın birlikte anıldığı bağlamda doğal ve kısa bir anlatımdır.","error_profile":{"adds":"Bacaktaki öteki kasları da kapsayabilecek kadar geniştir.","collision":"Genel bacak kaslarıyla karışabilir.","fit":"broadening","loses":null,"preserves":"At, bacak ve kas öğelerini korur."},"facet_ids":["F002"],"text":"atın bacak kasları","usage_role":"contextual"}],"definition":"Bacağın iç yanında kabarık duran özel et ya da kas parçasıdır. Atın bacağında, bacağın eni üzerinde iki yanda bulunan eş parçalar da bu adın ikili biçimiyle belirtilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bacağın iç tarafında belirgin biçimde kabaran bir et ya da kas parçasıdır."},{"facet_id":"F002","role":"specialization","statement":"Atın bacağında enine yerleşen iki eş et parçası birlikte adlandırılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Belirli çıkıntılı parça yerine bütün baldır bölgesini kapsar.","collision":"Genel bacak bölümüyle karışır.","fit":"broadening","loses":null,"preserves":"Bacağın ilgili genel bölgesini korur."},"text":"baldır"}],"identity_rationale":"Kaynak sözü, bacağın iç tarafında kabarık duran et ya da kas parçasını ve atın bacağının iki yanında bulunan iki et parçasını açıkça tanımlar. Verilen bacak eti ve kası çerçevesi bu beden bölgesini doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bacağın içindeki kabarık et ya da kas parçası"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"atın bacağının eninde bulunan iki et parçası"}],"lexicalization_note":"Tanım yalın beden bölümü adını korur; başka kaslar, kalça çevresi ve toynak bölümleri bu dala alınmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel kas dokusu dalı madde benzerliğini korurken odak dalın kesin bacak konumunu açıkça ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal anatomik yeri belirli tek bir parçadır; komşu dal kasın dokusunu ve kaslı beden yapısını genel olarak kapsar.","focus_only":"Bacağın içindeki belirli kabarık parça ve attaki iki eş parça odak dala özgüdür.","gloss":"sert ve toplu kas dokusu","neighbor_only":"Kas dokusunun sertliği, kalınlığı ve beden yapısının kaslı oluşu komşu dalda daha geniştir.","neighbor_ref":"root_001025/B001","relation_type":"near_neighbor","shared_zone":"İki dal da sıkı ve belirgin kas ya da et dokusunu anlatır."}],"source_phrase_ar":"الحمأة لحمة منتبرة في باطن الساق (ayn)؛ الحماة عضلة الساق (sihah)؛ في ساق الفرس حماتان وهما اللحمتان اللتان في عرض الساق (sihah)؛ الحماة لحمة منتبرة في باطن الساق (tahdhib)؛ الحماتان اللحمتان اللتان في عرض الساق (tahdhib)","source_summary":"Kaynaklar bacağın içinde kabaran et veya kas parçası üzerinde birleşir. At için kullanılan ikili biçim, bacağın eni boyunca iki yanda yer alan eş parçaları belirtir.","sources":["AY","SI","TA"],"what_is_ar":"الحماة والحمأة لحمة أو عضلة منتبرة في باطن الساق أو عرضها","what_is_not_ar":"ليس حماة المرأة ولا الحوامي من الحافر أو البئر"},"support_links":[]},{"boundary":"Kapsam toynağın sağ ve sol yan kenarlarıyla sınırlıdır; tabandaki çıkıntı, bacak eti ve genel kenar adı değildir.","branch_kind":"bare","branch_ref":"root_000358/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَامِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:HaAmiyap|ROOT:Hmy|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:11:2:1","qac_word_ref":"101:11:2","surface_ar":"حَامِيَةٌۢ"}],"gloss":"toynağın iki yan kenarı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Toynağın ortadaki bölümünün sağında ve solunda iki yan parça bulunur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu parçalar toynağın sağ ve sol yan kenarları olarak topluca adlandırılır."}}],"root_ar":"ح م ي","root_id":"root_000358","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Parçanın toynakta oluşunu, iki yana yerleşmesini ve kenar niteliğini birlikte karşılar.","boundary_detail":"Kapsam toynağın sağ ve sol yan kenarlarıyla sınırlıdır; tabandaki çıkıntı, bacak eti ve genel kenar adı değildir.","branch_image_ar":"جانبا الحافر","concept_gloss":"toynağın iki yan kenarı","contextual_glosses":[{"applicability":"Kesin anatomik ayrıntının bağlamdan anlaşıldığı yerlerde iki parçayı kısa biçimde karşılar.","error_profile":{"adds":"Toynağın sağ ve solundaki başka yan yapıları da kapsayabilir.","collision":"Genel toynak kenarlarıyla karışabilir.","fit":"broadening","loses":null,"preserves":"Toynakta iki yana yerleşme yönünü korur."},"facet_ids":["F001","F002"],"text":"toynak yanları","usage_role":"general"}],"definition":"Toynağın ortadaki ana bölümünün sağında ve solunda yer alan iki yan parça ya da kenardır. Çoğul kullanım, toynağın bu iki yandaki sınırlarını topluca belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Toynağın ortadaki bölümünün sağında ve solunda iki yan parça bulunur."},{"facet_id":"F002","role":"extension","statement":"Bu parçalar toynağın sağ ve sol yan kenarları olarak topluca adlandırılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Toynağın alt yüzünü anlamın merkezi yapar.","collision":"Tabandaki sert çıkıntı dalıyla karışır.","fit":"displacement","loses":"Sağ ve sol yan konumunu yitirir.","preserves":"Aynı beden bölümünü korur."},"text":"toynak tabanı"}],"identity_rationale":"Kaynak sözü, toynağın ortadaki bölümünün sağında ve solunda bulunan iki yanı ve bu yan kenarları çoğul olarak açıkça tanımlar. Verilen toynak yanları çerçevesi hem konumu hem parça türünü doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"toynağın ortadaki bölümünün sağ ve solundaki iki parça"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"toynağın sağ ve sol yan kenarları"}],"lexicalization_note":"Tanım yalın toynak bölümü adını korur ve genel yan, bacak ya da kuyu kenarı anlamlarını bu dala taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; toynak tabanındaki çıkıntı aynı beden alanında olup yan kenarların konumunu en açık biçimde karşıtlar.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak sağ ve sol yan kenarlardır; komşu ise tabanda bulunan kuru ve çıkıntılı et parçasıdır, dolayısıyla konumları ve yapıları ayrıdır.","focus_only":"Odak dal toynağın ortadaki bölümünü iki yandan kuşatan kenar parçalarıdır.","gloss":"toynak tabanındaki sert çıkıntı","neighbor_only":"Komşu dal toynağın alt yüzünde çekirdek ya da çakıl gibi duran sert çıkıntıdır.","neighbor_ref":"root_001496/B007","relation_type":"near_neighbor","shared_zone":"İki dal da toynağın belirli anatomik parçalarını adlandırır."}],"source_phrase_ar":"الحاميتان ما عن يمين السنبك وشماله (sihah;tahdhib)؛ الحوامي وهي حروفها من عن يمين وشمال (tahdhib)","source_summary":"Kaynaklar, toynağın ortadaki bölümünün sağ ve solunda bulunan iki parçada birleşir. Tekil çift anlatımı konumu, çoğul anlatım ise toynağın yan kenarlarını öne çıkarır.","sources":["SI","TA"],"what_is_ar":"الحاميتان والحوامي عن يمين السنبك وشماله وحروف الحافر","what_is_not_ar":"ليس لحمة الساق ولا حجارة البئر"},"support_links":[]},{"boundary":"Gönderim kuyunun kendisine ya da örme işine değil, taş örgüde kullanılan ağır taş ve kayalara yöneliktir.","branch_kind":"bare","branch_ref":"root_000358/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَامِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:HaAmiyap|ROOT:Hmy|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:11:2:1","qac_word_ref":"101:11:2","surface_ar":"حَامِيَةٌۢ"}],"gloss":"kuyu duvarını ören ağır taşlar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Taş, kuyunun iç duvarını örmekte kullanılan bir yapı parçasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Büyük ve ağır kayalar örgünün arka kesimlerine yerleştirilerek yapıyı sağlamlaştırır."}}],"root_ar":"ح م ي","root_id":"root_000358","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Malzemeyi, kuyu içindeki yapısal yerini ve ağır taş niteliğini birlikte karşılar.","boundary_detail":"Gönderim kuyunun kendisine ya da örme işine değil, taş örgüde kullanılan ağır taş ve kayalara yöneliktir.","branch_image_ar":"حجارة طي البئر","concept_gloss":"kuyu duvarını ören ağır taşlar","contextual_glosses":[{"applicability":"Tek bir yapı parçasının kuyu duvarındaki görevini kısa biçimde belirtmek için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Büyük ve ağır kayaların örgünün arka kesimindeki sağlamlaştırıcı görevini belirtmez.","preserves":"Kuyuda taş örgü malzemesi olma yönünü korur."},"facet_ids":["F001"],"text":"kuyu örgüsü taşı","usage_role":"general"}],"definition":"Kuyunun iç duvarını örmekte kullanılan taş, özellikle örgünün arka kesimlerine yerleştirilerek yapıyı sağlamlaştıran büyük ve ağır kayadır. Çoğul biçim kuyunun taş örgüsündeki bu ağır parçaları topluca belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Taş, kuyunun iç duvarını örmekte kullanılan bir yapı parçasıdır."},{"facet_id":"F002","role":"specialization","statement":"Büyük ve ağır kayalar örgünün arka kesimlerine yerleştirilerek yapıyı sağlamlaştırır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Tek tek yapı taşları yerine tamamlanmış duvarın bütününü kapsar.","collision":"Örülmüş kuyu yapısıyla karışır.","fit":"broadening","loses":null,"preserves":"Kuyudaki taş yapı alanını korur."},"text":"kuyu duvarı"}],"identity_rationale":"Kaynak sözü, kuyunun iç duvarını örmekte kullanılan taşları ve özellikle örgünün arka bölümlerine konan büyük, ağır kayaları anlatır. Verilen kuyu örgüsü taşları çerçevesi hem malzemeyi hem yapısal görevi doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"kuyu duvarını örmekte kullanılan taş"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"kuyu örgüsünü sağlamlaştıran büyük ve ağır kayalar"}],"lexicalization_note":"Tanım yalın yapı taşı adını korur; kuyu örme eylemi, ahşap kuyu yapısı ve genel taş anlamı dala eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kuyuyu taşla örme dalı aynı yapım alanında malzeme ile işlem arasındaki sınırı en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak malzeme ve yapı parçasıdır; komşu ise yapım işlemi ile ortaya çıkan kuyudur, bu nedenle nesne düzeyleri ayrıdır.","focus_only":"Odak dal, kuyu örgüsünde kullanılan tek tek ağır taş ve kayaları adlandırır.","gloss":"kuyuyu taşla örme","neighbor_only":"Komşu dal kuyunun taşla örülmesi işini ve bu işlemle oluşan kuyuyu kapsar.","neighbor_ref":"root_000960/B004","relation_type":"near_neighbor","shared_zone":"İki dal da kuyunun iç duvarını taşla kurma durumuna katılır."}],"source_phrase_ar":"الحامية الحجارة يطوى بها البئر (ayn;tahdhib)؛ الحوامي عظام الحجارة وثقالها (tahdhib)؛ الحوامي صخر عظام تجعل في مآخير الطي (tahdhib)؛ حجارة الركية كلها حوام (tahdhib)","source_summary":"Kaynaklar kuyunun taşla örülen iç duvarında kullanılan taşları ortak çekirdek olarak verir. Özellikle büyük ve ağır kayaların örgünün arka kesimlerine yerleştirilmesi, bu yapı parçalarının görevini açıklar.","sources":["AY","TA"],"what_is_ar":"الحامية والحوامي حجارة أو صخر عظام يطوى بها البئر أو تثبت مآخير الطي","what_is_not_ar":"ليست الحامية الرجل الذي يحمي أصحابه ولا حروف الحافر"},"support_links":[]},{"boundary":"Çekirdek kararma ve kara görünmedir; balçığın kara rengi, genel gece karanlığı ve bulutun yalnız hareket etmesi bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000358/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حَامِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:HaAmiyap|ROOT:Hmy|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:11:2:1","qac_word_ref":"101:11:2","surface_ar":"حَامِيَةٌۢ"}],"gloss":"kararıp kara bir görünüm alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey kara bir görünüm alacak biçimde kararır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gece ve bulut bu kararma durumunun başlıca taşıyıcılarıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kara bulutlar üst üste yığılıp yoğun bir kütle oluşturur."}}],"root_ar":"ح م ي","root_id":"root_000358","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Süreci ve ortaya çıkan kara görünümü birlikte karşılar; gece ile bulut başlıca bağlamlardır.","boundary_detail":"Çekirdek kararma ve kara görünmedir; balçığın kara rengi, genel gece karanlığı ve bulutun yalnız hareket etmesi bu dala girmez.","branch_image_ar":"اسوداد الليل والسحاب","concept_gloss":"kararıp kara bir görünüm alma","contextual_glosses":[{"applicability":"Bulutların kararıp üst üste yoğunlaştığı gökyüzü bağlamında doğal ve açıklayıcı bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel kararma sürecini ve geceye ilişkin kullanımı vermez.","preserves":"Bulutun kara görünmesini ve yığılmasını korur."},"facet_ids":["F002","F003"],"text":"kara bulutların yığılması","usage_role":"contextual"}],"definition":"Bir şeyin kara bir görünüm alacak ölçüde kararmasıdır; özellikle gece ve bulut için kullanılır. Kara bulutların üst üste yığılıp yoğunlaşması bu çekirdeğin buluta bağlı özel sonucudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey kara bir görünüm alacak biçimde kararır."},{"facet_id":"F002","role":"specialization","statement":"Gece ve bulut bu kararma durumunun başlıca taşıyıcılarıdır."},{"facet_id":"F003","role":"extension","statement":"Kara bulutlar üst üste yığılıp yoğun bir kütle oluşturur."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Balçık maddesini anlamın merkezine koyar.","collision":"Kara balçık dalıyla karışır.","fit":"displacement","loses":"Kararma sürecini, geceyi ve bulutu yitirir.","preserves":"Kara renk öğesini korur."},"text":"kara balçık"}],"identity_rationale":"Kaynak sözü, bir şeyin kararmasını ve özellikle gece ile bulutun kara bir görünüm almasını; ayrıca kara bulutların üst üste yığılmasını anlatır. Verilen gece ve bulut kararması çerçevesi bu süreç ile sonucu doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"karardı, kara bir görünüm aldı"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"üst üste yığılmış kara bulut"}],"lexicalization_note":"Genel kararma yapısı ile gece ve buluta bağlı kullanımlar ayrılır; yığılan kara bulut biçimi bütün kararma olaylarına yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yoğun karanlık dalı ortak kara görünümü korurken odak dalın kararma süreci ve bulut yığılması sınırını belirginleştirir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kararma sürecini gece ve buluta bağlayıp yığılmış kara bulutu ayrıca kapsar; komşu dal koyuluğu daha geniş nesne alanlarına taşır.","focus_only":"Gece veya bulutun kararma süreci ve kara bulutların yığılması odak dala özgüdür.","gloss":"yoğun karanlık ve koyuluk","neighbor_only":"Gözün koyuluğu ve yerin yoğun yeşilliği gibi başka koyu görünüşler komşu dalın kapsamındadır.","neighbor_ref":"root_001344/B007","relation_type":"near_synonym","shared_zone":"İki dal da gecenin koyulaşmasını ve güçlü kara görünümü anlatır."}],"source_phrase_ar":"احمومى الشيء فهو محموم واحمومى الليل والسحاب وذلك من السواد (ayn)؛ احمومى الشيء فهو محموم يوصف به الأسود من نحو الليل والسحاب (tahdhib)؛ المحمومي من السحاب الأسود المتراكم (tahdhib)","source_summary":"Kaynaklar bir şeyin kararması ve gece ile bulutun kara görünmesi üzerinde birleşir. Buluta özgü kullanım, kara bulutların üst üste yığılarak yoğunlaşmasını ayrıca belirtir.","sources":["AY","TA"],"what_is_ar":"احموماء الشيء واسوداد الليل والسحاب وتراكم السحاب الأسود","what_is_not_ar":"ليس الحمأ الطين الأسود"},"support_links":[]},{"boundary":"Dal yalnızca ışık ve aydınlatma anlamını kapsar; ateş, çiçek ve yol işareti ayrı dallardadır.","branch_kind":"bare","branch_ref":"root_001564/B001","candidate_links":[{"candidate_id":"cand_c9b1c6b4c9bc52e9c2c9","lane":"micro"},{"candidate_id":"cand_db9a48af999f394e0b7b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:11:1:1","qac_word_ref":"101:11:1","surface_ar":"نَارٌ"}],"gloss":"ışık ve aydınlatma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Görmeyi sağlayan aydınlık ve ışık, dalın ad çekirdeğini oluşturur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyin ışık vermesi, aydınlanması veya aydınlatılması eylem alanını oluşturur."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Işığın kendisiyle ışık verme, aydınlanma ve aydınlatma eylemlerinin tamamını karşılayan genel anlatımdır.","boundary_detail":"Dal yalnızca ışık ve aydınlatma anlamını kapsar; ateş, çiçek ve yol işareti ayrı dallardadır.","branch_image_ar":"الضياء والإضاءة","concept_gloss":"ışık ve aydınlatma","contextual_glosses":[{"applicability":"Bir nesnenin ya da ortamın ışık kazanmasını anlatan geçişsiz eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Işığın ad olarak kullanımı ile başkasını aydınlatma anlamını dışarıda bırakır.","preserves":"Işık kazanma ve aydınlık duruma gelme eylemini korur."},"facet_ids":["F002"],"text":"aydınlanmak","usage_role":"contextual"},{"applicability":"Bir kaynağın başka bir nesneye ya da ortama ışık vermesini anlatan geçişli eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Işığın ad anlamını ve kendiliğinden aydınlanma kullanımını dışarıda bırakır.","preserves":"Başka bir şeyi ışıklı duruma getirme eylemini korur."},"facet_ids":["F002"],"text":"aydınlatmak","usage_role":"contextual"}],"definition":"Işığın kendisini, bir şeyin ışık vermesini ya da başka bir şeyi aydınlatmasını anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Görmeyi sağlayan aydınlık ve ışık, dalın ad çekirdeğini oluşturur."},{"facet_id":"F002","role":"extension","statement":"Bir şeyin ışık vermesi, aydınlanması veya aydınlatılması eylem alanını oluşturur."}],"identity_rationale":"Kaynak ifadesi dalı doğrudan ışık, aydınlık ve bir şeyin ışık vermesi üzerinden kurar. Geçici çerçeve bu çekirdeği doğru yansıtır ve ateşin kendisini, çiçeği ya da yalnızca belirgin bir işareti bu anlama katmaz.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ışık, aydınlık"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ışık vermek, aydınlanmak veya aydınlatmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"aydınlatma; günün ağarması"}],"lexicalization_note":"Tanım yalın dalın ışık ve aydınlatma çekirdeğiyle sınırlıdır; başka yapılara özgü anlamlar içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca doğrudan eşdeğerlik, sabah aydınlığı sınırı ve ateşle karışma ihtimalini açıklayan üç ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kartlarda kapsamı ayıran bir koşul, katılımcı veya sonuç bulunmaz; farklı örnek dizileri dal sınırını değiştirmez.","focus_only":null,"gloss":"ışık ve ışık verme","neighbor_only":null,"neighbor_ref":"root_000919/B001","relation_type":"synonym","shared_zone":"Her iki dal da ışığın kendisini ve bir şeyin ışık vermesi ya da başka bir şeyi aydınlatması eylemini kapsar."},{"boundary_match":"partial","distinction":"Odak dal genel ışık ve aydınlatmadır; komşu dal ise sabahın ağarması gibi karanlık sonrası açılma bağlamına daha sıkı bağlıdır.","focus_only":"Her türlü ışık, ışık verme ve aydınlatma bağlamını kapsar.","gloss":"ağarma ve aydınlanma","neighbor_only":"Özellikle karanlıktan sonra beliren gün ışığına ve yüzün parlamasına uzanır.","neighbor_ref":"root_000712/B002","relation_type":"near_synonym","shared_zone":"İki dal da ışığın görünür hale gelmesi ve ortamın aydınlanması alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal ışığın kendisini ve aydınlatmayı anlatır; komşu dal ise ışığın kaynağı olan yanan ateşi ve ona bağlı damgalama kullanımını anlatır.","focus_only":"Maddi bir ateş bulunmadan da ışık ve aydınlanma gerçekleşebilir.","gloss":"ışık ile ateş","neighbor_only":"Yanma, hareketli alev ve ateşle yapılan hayvan damgasını kapsar.","neighbor_ref":"root_001564/B002","relation_type":"near_neighbor","shared_zone":"Ateş ışık verdiği için iki dal aydınlık üretme noktasında kesişir."}],"source_phrase_ar":"النور الضياء والفعل نار وأنار ونورا وإنارة واستنار أي أضاء (ayn)؛ النور: الضياء؛ أنار الشئ واستنار بمعنى أي أضاء؛ التنوير: الإنارة؛ التنوير: الإسفار (sihah)؛ أصل صحيح يدل على إضاءة واضطراب وقلة ثبات؛ النور والنار سميا بذلك من طريقة الإضاءة (maqayis)","source_summary":"Kaynaklar ışık ve aydınlık anlamında, ayrıca ışık verme ve aydınlatma eylemlerinde birleşir; günün ağarması da aydınlanmanın bağlamsal bir gerçekleşmesi olarak verilir.","sources":["AY","SI","MQ"],"what_is_ar":"يدخل فيه النور بمعنى الضياء، وأفعال نار وأنار واستنار وأضاء، والتنوير بمعنى الإنارة والإسفار.","what_is_not_ar":"لا يدخل فيه النار المتقدة، ولا نور الشجر، ولا المنارة والعلامة إلا من جهة الإضاءة."},"support_links":["sup_1cbc60c875be9c5e4f1e","sup_7820cd66702bb5de0e08"]},{"boundary":"Yanan ateş çekirdektir; hayvan damgası ateşle yakma işlemine bağlı özel kullanımdır, yalın ışık değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001564/B002","candidate_links":[{"candidate_id":"cand_1a1863173e9f041ca7cd","lane":"micro"},{"candidate_id":"cand_af7bb7eafdfdcf84091b","lane":"micro"},{"candidate_id":"cand_3c7feb0f5d2e6730bc05","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:11:1:1","qac_word_ref":"101:11:1","surface_ar":"نَارٌ"}],"gloss":"yanan ateş ve ateşle yapılan hayvan damgası","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Işık veren ve hızlı, kararsız hareket gösteren yanan ateş temel anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvan üzerinde ateşle yakılarak oluşturulan damga, ateş çekirdeğine bağlı özel anlamdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hayvanın soyu ile damgasını ilişkilendiren söz, damga anlamına bağlı kalıplaşmış kullanımdır."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın ateş çekirdeğini ve yalnız hayvan damgası yapılarında görülen yakma temelli özel anlamı birlikte gösterir.","boundary_detail":"Yanan ateş çekirdektir; hayvan damgası ateşle yakma işlemine bağlı özel kullanımdır, yalın ışık değildir.","branch_image_ar":"النار المتقدة والسمة بها","concept_gloss":"yanan ateş ve ateşle yapılan hayvan damgası","contextual_glosses":[{"applicability":"Yanmakta olan ateşin kendisinin anlatıldığı yalın bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvan damgasını ve bu damgaya bağlı kalıplaşmış sözü dışarıda bırakır.","preserves":"Yanan ve ışık yayan ateş çekirdeğini korur."},"facet_ids":["F001"],"text":"ateş","usage_role":"general"},{"applicability":"Bir hayvanın ateşle yakılarak oluşturulmuş ayırt edici işaretinin sorulduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalın ateş anlamını ve kalıplaşmış soy-damga sözünü dışarıda bırakır.","preserves":"Hayvana ateşle yapılan damga anlamını korur."},"facet_ids":["F002"],"text":"yakma damgası","usage_role":"contextual"}],"definition":"Yanarak ışık ve ısı yayan, hareketli alevleri bulunan ateşi anlatır. Aynı dalda, hayvana ateşle yakılarak yapılan damgaya ve bu damga üzerinden kurulan bir söze bağlı özel kullanımlar da vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Işık veren ve hızlı, kararsız hareket gösteren yanan ateş temel anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Hayvan üzerinde ateşle yakılarak oluşturulan damga, ateş çekirdeğine bağlı özel anlamdır."},{"facet_id":"F003","role":"associated_use","statement":"Hayvanın soyu ile damgasını ilişkilendiren söz, damga anlamına bağlı kalıplaşmış kullanımdır."}],"identity_rationale":"Kaynak ifadesi yanan ateşi, bu adın ışık ve hızlı hareketle bağlantısını ve hayvanın ateşle yapılan damgasını birlikte verir. Geçici çerçeve bu çok parçalı yapıyı doğru yansıtır; damga kullanımı ateşin temel tanımına değil, ona bağlı ayrı bir kullanıma yerleştirilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yanan ateş"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"ateşler"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"devenin ateşle yapılmış damgası"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"hayvanın soyu damgasından belli olur"}],"lexicalization_note":"Yalın ateş anlamı ile hayvana ait damga ve atasözü yapıları ayrı tutulur; özel yapılar genel ateş anlamına yayılmaz.","neighbor_coverage_note":"Tüm adaylar incelendi; alev, hayvan damgası ve ışıkla sınır karışıklığını en açık gösteren üç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ateşin tamamını ve damga kullanımını içerir; komşu dal ise yalnız ateşin alevlenen bölümüne odaklanır.","focus_only":"Ateşin bütünü ile hayvanın ateşle yapılan damgasını kapsar.","gloss":"ateş ve alev","neighbor_only":"Ateşin yalnız saf ve yükselen alev bölümünü anlatır.","neighbor_ref":"root_001357/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da yanma ve görünür alev alanına aittir."},{"boundary_match":"field_only","distinction":"Ortak alan damgalamadır; odak dalın belirleyici özelliği yakma aracıdır, komşu dalın belirleyici özelliği ise damganın gizli konumudur.","focus_only":"Damganın ateşle yakılarak yapılmasını ve ateş anlamıyla bağını belirtir.","gloss":"hayvan damgaları","neighbor_only":"Seçkin bir devenin gizli bir yerine konan özel damgayı belirtir.","neighbor_ref":"root_000384/B005","relation_type":"same_field","shared_zone":"İki dal da hayvanı ayırt eden kalıcı bir işaret alanındadır."},{"boundary_match":"partial","distinction":"Odak dal ışık veren fiziksel ateştir; komşu dal ise kaynağından bağımsız olarak ışığı ve aydınlatmayı anlatır.","focus_only":"Yanma, ısı, hareketli alev ve ateşle yapılan damga bulunur.","gloss":"ateş ile ışık","neighbor_only":"Ateş gerektirmeyen genel ışık, aydınlanma ve aydınlatma bulunur.","neighbor_ref":"root_001564/B001","relation_type":"near_neighbor","shared_zone":"Ateşin ışık vermesi iki dalın kesişme noktasıdır."}],"source_phrase_ar":"النار مؤنثة وهي من الواو؛ الجمع نور ونيران (sihah)؛ ما نار هذه الناقة أي ما سمتها؛ نجارها نارها؛ سماتها (sihah)؛ النور والنار سميا بذلك من طريقة الإضاءة ولأن ذلك يكون مضطربا سريع الحركة (maqayis)","source_summary":"Kaynaklar yanan ateşi ışık ve hareket niteliğiyle açıklar; çoğul biçimlerini ve hayvanın ateşle yapılan damgasına bağlı kullanımları da aynı dalda toplar.","sources":["SI","MQ"],"what_is_ar":"يدخل فيه النار وما سميت به لطريقة الإضاءة واضطراب الحركة، وجموعها، والسمة بالنار في الناقة والإبل.","what_is_not_ar":"لا يدخل فيه مجرد الضياء بلا نار، ولا تنور النار من بعيد، ولا النائرة بين القوم."},"support_links":["sup_0c97f3d4cf7e81ec7639","sup_31d221978bba061d14e8","sup_8c2f90e06aa06a751714"]},{"boundary":"Anlam yalnız ateşle kurulan bu yapıya aittir; uzaktan görme ve ateşe yönelme iki ayrı kaynak açıklamasıdır.","branch_kind":"collocation","branch_ref":"root_001564/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:11:1:1","qac_word_ref":"101:11:1","surface_ar":"نَارٌ"}],"gloss":"ateşi uzaktan görüp ona yönelmek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Uzakta bulunan ateşi görüp seçmek, yapının algısal açıklamasıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ateşe doğru yönelmek, aynı yapının amaç ve hareket bildiren kaynak açıklamasıdır."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ateş nesnesiyle kurulan yapının hem uzaktan seçme hem de ona doğru gitme açıklamasını birlikte gösterir.","boundary_detail":"Anlam yalnız ateşle kurulan bu yapıya aittir; uzaktan görme ve ateşe yönelme iki ayrı kaynak açıklamasıdır.","branch_image_ar":"تنور النار من بعيد","concept_gloss":"ateşi uzaktan görüp ona yönelmek","contextual_glosses":[{"applicability":"Uzakta görünen ateşin fark edilmesi ve gözle seçilmesi öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ateşe doğru yönelme ve onu amaç edinme açıklamasını dışarıda bırakır.","preserves":"Ateşin uzaktan görülmesi ve seçilmesi anlamını korur."},"facet_ids":["F001"],"text":"ateşi uzaktan seçmek","usage_role":"contextual"},{"applicability":"Bir kimsenin gördüğü ya da bildiği ateşi hedef alarak ona doğru gitmesi öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalnız uzaktan görüp seçme açıklamasını dışarıda bırakır.","preserves":"Ateşi amaç edinip ona doğru gitme anlamını korur."},"facet_ids":["F002"],"text":"ateşe yönelmek","usage_role":"contextual"}],"definition":"Ateşi uzaktan seçmeyi veya ateşe doğru yönelmeyi anlatan yapıdır. Uzaktan görme ile yönelme, aynı yapı için verilen iki yakın kaynak açıklaması olarak ayrı tutulur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Uzakta bulunan ateşi görüp seçmek, yapının algısal açıklamasıdır."},{"facet_id":"F002","role":"source_variant","statement":"Ateşe doğru yönelmek, aynı yapının amaç ve hareket bildiren kaynak açıklamasıdır."}],"identity_rationale":"Kaynak ifadesi aynı ateş yapısını iki yakın fakat özdeş olmayan biçimde açıklar: ateşe yönelmek ve ateşi uzaktan seçmek. Geçici çerçeve kullanılabilir, ancak görme ile yönelmenin birbirine indirgenmemesi gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"ateşe doğru yönelmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ateşi uzaktan görüp seçmek"}],"lexicalization_note":"Tanım yalnız ateş nesnesiyle kurulan yapıya bağlıdır; genel görme, arama veya yönelme anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; gece ateşine yönelme, gözetleme ve görünürlükle en öğretici üç sınır seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak yapı görme veya yönelme düzeyinde kalır; komşu dal gece koşulunu ve ateş ışığıyla yol bulma sonucunu da içerir.","focus_only":"Ateşi uzaktan seçme açıklaması gece veya yol bulma koşuluna bağlı değildir.","gloss":"uzaktaki ateşe yönelme","neighbor_only":"Gece görünen ateşin ışığıyla yol bulma ve o ışığı kılavuz edinme anlamını taşır.","neighbor_ref":"root_001017/B002","relation_type":"near_synonym","shared_zone":"İki dal da uzakta görülen ateşi hedef alma ve ona doğru yönelme alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal belirli bir ateş yapısıdır; komşu dal nesnesi değişebilen, süreğen izleme ve bekleme eylemidir.","focus_only":"Nesne ateştir ve bazı açıklamalarda ona doğru gitme de bulunur.","gloss":"uzaktan görme ve gözetleme","neighbor_only":"Bakılan şeyi izleme, gözetleme ve bekleme sürecini kapsar.","neighbor_ref":"root_000142/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da uzaktaki bir şeyi gözle seçme alanını paylaşır."},{"boundary_match":"field_only","distinction":"Odak dal algılayan kişinin ateşle kurduğu eylemdir; komşu dal ise görülen şeyin açıklık niteliğini tanımlar.","focus_only":"Bir kişinin ateşi görmesi veya ateşe yönelmesi eylemini anlatır.","gloss":"görünürlük ve görme","neighbor_only":"Bir şeyin kendisinin açıkça görünür ve anlaşılır hale gelmesini anlatır.","neighbor_ref":"root_001473/B002","relation_type":"same_field","shared_zone":"İki dalda da bir şeyin gözle seçilebilir olması önemlidir."}],"source_phrase_ar":"تنورت نارا قصدت إليها (ayn)؛ تنورت النار من بعيد: تبصرتها (sihah)؛ تنورت النار تبصرتها (maqayis)","source_summary":"Kaynak açıklamaları aynı ateş yapısını uzaktan görme ile ateşe yönelme arasında konumlandırır; bu iki açıklama birleştirilmeden aynı kullanım çevresinin parçaları olarak korunur.","sources":["AY","SI","MQ"],"what_is_ar":"يدخل فيه تنورت النار إذا قصدت إليها أو تبصرتها من بعد.","what_is_not_ar":"لا يدخل فيه مطلق الإضاءة، ولا النار نفسها بلا فعل التنور."},"support_links":[]},{"boundary":"Dal ağaç çiçeği ve ağacın çiçek açmasıyla sınırlıdır; genel bitki çıkışı veya ışık anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001564/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:11:1:1","qac_word_ref":"101:11:1","surface_ar":"نَارٌ"}],"gloss":"ağaç çiçeği ve çiçeklenme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ağaç üzerinde açan çiçek, dalın ad anlamıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ağacın çiçek çıkarması ve çiçeklenmesi, aynı çekirdeğin eylem görünümüdür."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ağaçta beliren çiçeği ve ağacın bu çiçeği çıkarma sürecini birlikte karşılayan genel anlatımdır.","boundary_detail":"Dal ağaç çiçeği ve ağacın çiçek açmasıyla sınırlıdır; genel bitki çıkışı veya ışık anlamı değildir.","branch_image_ar":"نور الشجر وزهره","concept_gloss":"ağaç çiçeği ve çiçeklenme","contextual_glosses":[{"applicability":"Ağaç üzerinde açmış çiçeğin ad olarak belirtildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ağacın çiçek çıkarma ve çiçeklenme eylemini dışarıda bırakır.","preserves":"Ağaç üzerinde beliren çiçek anlamını korur."},"facet_ids":["F001"],"text":"ağaç çiçeği","usage_role":"general"},{"applicability":"Ağacın çiçeklerini ortaya çıkarması ve çiçekli hale gelmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ortaya çıkan çiçeğin bağımsız ad anlamını dışarıda bırakır.","preserves":"Ağacın çiçek çıkarma sürecini korur."},"facet_ids":["F002"],"text":"çiçek açmak","usage_role":"contextual"}],"definition":"Ağaçta beliren çiçeği ve ağacın çiçek çıkararak çiçeklenmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ağaç üzerinde açan çiçek, dalın ad anlamıdır."},{"facet_id":"F002","role":"extension","statement":"Ağacın çiçek çıkarması ve çiçeklenmesi, aynı çekirdeğin eylem görünümüdür."}],"identity_rationale":"Kaynak ifadesi ağacın çiçeğini ve ağacın çiçek açmasını açıkça aynı dalda toplar. Geçici çerçeve hem ortaya çıkan çiçeği hem de çiçek çıkarma sürecini korur ve genel ışık anlamını bu dala taşımaz.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ağaç çiçeği"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ağaç çiçekleri; tek bir ağaç çiçeği"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ağaç çiçek açtı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ağacın çiçek açması"}],"lexicalization_note":"Ağaç çiçeğini adlandıran biçimler ile ağaç öznesine bağlı çiçek açma yapıları ayrılır; kapsam genel aydınlanmaya genişletilmez.","neighbor_coverage_note":"Bütün adaylar incelendi; ağaç çiçeği, çayır çiçeği ve genel bitki çıkışı arasındaki sınırı gösteren üç ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel ağaç çiçeği çekirdeğidir; komşu dal belirli ağaç, renk ve bitki adlarıyla daha özel bir kapsama sahiptir.","focus_only":"Ağaç çiçeğini tür ve renk sınırlaması olmadan, ayrıca çiçeklenme eylemiyle kapsar.","gloss":"ağaç çiçeği","neighbor_only":"Belirli bir ağacın çiçeklenmesine, beyaz çiçeğe ve bazı bitki adlarına uzanır.","neighbor_ref":"root_000620/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da ağaçta ortaya çıkan çiçeği ve çiçeklenmeyi kapsar."},{"boundary_match":"partial","distinction":"Odak dal ağaç ve çiçeklenme sürecine bağlıdır; komşu dal çayırın çiçekli görünümüne bağlıdır.","focus_only":"Ağaç çiçeğini ve ağacın çiçek açma eylemini kapsar.","gloss":"çiçek örtüsü","neighbor_only":"Çayırın çiçek örtüsünü anlatan özel bir adlandırmadır.","neighbor_ref":"root_001331/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da bitkinin görünen çiçeklerini adlandırır."},{"boundary_match":"field_only","distinction":"Odak dalın sonucu çiçektir; komşu dal çiçekle sınırlı olmayan sürgün ve ekin çıkışını anlatır.","focus_only":"Özellikle ağaç çiçeğinin ortaya çıkmasını anlatır.","gloss":"bitkinin belirmesi","neighbor_only":"Hurma sürgününün ve ekinin genel olarak topraktan ya da bitkiden belirmesini anlatır.","neighbor_ref":"root_000945/B005","relation_type":"same_field","shared_zone":"İki dal da bitkide yeni bir bölümün görünür hale gelmesi sürecindedir."}],"source_phrase_ar":"النور نور الشجر؛ تنوير الشجرة إزهارها؛ النوار نور الشجر (ayn)؛ تنوير الشجرة: إزهارها؛ نورت الشجرة وأنارت أي أخرجت نورها؛ النوار نور الشجر (sihah)؛ ومنه النور نور الشجر ونواره؛ أنارت الشجرة أخرجت النور (maqayis)","source_summary":"Kaynaklar ağaç çiçeğini adlandırmada ve ağacın çiçek çıkarıp çiçeklenmesini anlatan eylemlerde birleşir.","sources":["AY","SI","MQ"],"what_is_ar":"يدخل فيه نور الشجر ونواره، وتنوير الشجرة أو إنارتها بمعنى إزهارها وإخراج نورها.","what_is_not_ar":"لا يدخل فيه الضوء العام، ولا النار، ولا النُّورَة التي يطلى بها."},"support_links":[]},{"boundary":"Belirginlik yol bulma, sınır gösterme, ışık taşıma veya çağrı yeri olma işlevine bağlıdır; yalın ışık değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001564/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:11:1:1","qac_word_ref":"101:11:1","surface_ar":"نَارٌ"}],"gloss":"yol gösteren belirgin işaret ve yüksek yapı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yol üzerinde kolayca görülüp yön bulmayı sağlayan işaret temel işlevdir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Arazinin belirgin sınırları ve sınır işaretleri, gösterme işlevinin özel alanıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Üstünde ışık bulunan veya çağrı yapılan yüksek ve görünür yapı, işaret işlevinin yapısal uzantısıdır."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yol işaretini, arazi sınırını ve ışık ya da çağrı işlevli görünür yüksek yapıyı ortak işlevleriyle karşılar.","boundary_detail":"Belirginlik yol bulma, sınır gösterme, ışık taşıma veya çağrı yeri olma işlevine bağlıdır; yalın ışık değildir.","branch_image_ar":"المنار والمنارة الظاهرة","concept_gloss":"yol gösteren belirgin işaret ve yüksek yapı","contextual_glosses":[{"applicability":"Yol üzerinde yön bulmayı sağlayan görünür bir işaret anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Arazi sınırını ve ışık ya da çağrı işlevli yüksek yapıyı dışarıda bırakır.","preserves":"Belirgin olma ve yol göstermeye yarama işlevini korur."},"facet_ids":["F001"],"text":"yol gösteren işaret","usage_role":"general"},{"applicability":"Üstünde ışık taşınan veya insanlara çağrı yapılan yüksek ve görünür yapı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yol işaretini ve arazinin sınır işaretlerini dışarıda bırakır.","preserves":"Yüksek yapının görünürlük, ışık taşıma ve çağrı yeri olma işlevini korur."},"facet_ids":["F003"],"text":"ışık ya da çağrı kulesi","usage_role":"explanatory"}],"definition":"Yol bulmayı veya sınırı tanımayı sağlayan belirgin işaretleri anlatır. Ayrıca üstünde ışık taşınan ya da insanlara çağrı yapılan görünür yüksek yapı bu işlevsel çekirdeğe bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yol üzerinde kolayca görülüp yön bulmayı sağlayan işaret temel işlevdir."},{"facet_id":"F002","role":"specialization","statement":"Arazinin belirgin sınırları ve sınır işaretleri, gösterme işlevinin özel alanıdır."},{"facet_id":"F003","role":"extension","statement":"Üstünde ışık bulunan veya çağrı yapılan yüksek ve görünür yapı, işaret işlevinin yapısal uzantısıdır."}],"identity_rationale":"Kaynak ifadesi yol gösteren belirgin işareti, arazi sınır ve işaretlerini ve üstünde ışık bulunan ya da çağrı yapılan yüksek yapıyı aynı görünürlük işlevi çevresinde toplar. Geçici çerçeve bu işlevsel ortaklığı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yol gösteren belirgin işaret"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"arazinin sınırları ve belirgin işaretleri"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yol gösteren, üstünde ışık bulunan veya çağrı yapılan yüksek yapı"}],"lexicalization_note":"Yalın belirgin yol işareti ile arazi sınırı yapısı ve yüksek yapı anlamı ayrılır; özel yapıların kapsamı her işarete yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel işaret alanı, zaman anlamına uzanan işaret ve taş yapı arasındaki üç temel sınır seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yol, arazi sınırı ve yüksek yapı çevresinde toplanır; komşu dal çok daha geniş bir işaretleme ve ayırt etme alanına yayılır.","focus_only":"Işık taşınan veya çağrı yapılan yüksek yapıyı da kapsar.","gloss":"yol ve sınır işaretleri","neighbor_only":"Bayrak, dağ, kumaş işareti, boya ve çeşitli nesnelere konan ayırt edici izleri kapsar.","neighbor_ref":"root_001040/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da yol bulmaya veya bir şeyi tanımaya yarayan görünür işaretleri kapsar."},{"boundary_match":"partial","distinction":"Odak dal görünür yapı ve sınır işlevinde kalır; komşu dal işaret anlamından belirlenmiş zamana da uzanır.","focus_only":"Arazi sınırları ile ışık veya çağrı işlevli yüksek yapıyı kapsar.","gloss":"belirgin yol işareti","neighbor_only":"Belirlenmiş zaman ve buluşma vaktini de kapsar.","neighbor_ref":"root_000051/B005","relation_type":"near_synonym","shared_zone":"İki dal da yol veya açık arazide yön bulduran işareti anlatır."},{"boundary_match":"partial","distinction":"Odak dal işlev ve görünürlük üzerinden tanımlanır; komşu dalın ayırıcı özelliği taş malzeme ve dikili yapı biçimidir.","focus_only":"Taşla sınırlı değildir ve ışık ya da çağrı işlevli yüksek yapıyı içerir.","gloss":"yüksek yol işareti","neighbor_only":"Taşlardan yapılmış veya taş olarak dikilmiş yüksek işareti özel olarak belirtir.","neighbor_ref":"root_000075/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da uzaktan görülen ve yön bulmaya yardım eden yükseltilmiş işareti kapsar."}],"source_phrase_ar":"المنارة مفعلة من الإنارة؛ كانوا ينورون في الجاهلية ليهتدى ويقتدى بها؛ المنارة الشمعة ذات السراج؛ المنارة ما يوضع عليه للمسرجة؛ المنارة للمؤذن (ayn)؛ المنار: علم الطريق؛ ضرب المنار على طريقه ليهتدى بها؛ المنارة التي يؤذن عليها؛ المنارة ما يوضع فوقها السراج (sihah)؛ المنارة مفعلة من الاستنارة؛ منار الأرض حدودها وأعلامها سميت لبيانها وظهورها (maqayis)","source_summary":"Kaynaklar belirginlik ve görünürlüğü ortak zemin yapar; yol işareti, arazi sınırı ve ışık ya da çağrı için kullanılan yüksek yapı bu zeminde birleşir.","sources":["AY","SI","MQ"],"what_is_ar":"يدخل فيه المنار علامة الطريق، ومنار الأرض حدودها وأعلامها، والمنارة التي يهتدى بها أو يوضع عليها السراج أو يؤذن عليها.","what_is_not_ar":"لا يدخل فيه أسماء الأعلام مثل ذي المنار ومنور إلا من جهة التسمية، ولا يدخل فيه النور المجرد بلا علامة."},"support_links":[]},{"boundary":"Dal kaçınma, ürkme ve uzaklaştırmayı kapsar; genel ışık ya da topluluklar arası düşmanlık anlamına girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001564/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:11:1:1","qac_word_ref":"101:11:1","surface_ar":"نَارٌ"}],"gloss":"ürkmek, kaçınmak ve uzaklaştırmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyden ürkme, kaçınma ve uzaklaşma temel hareket ve tutumdur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kötülükten veya erkeklerden uzak duran kadın ile eşten kaçınan dişi hayvan, katılımcıya bağlı özel nitelemelerdir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir başkasını söz veya davranışla ürkütüp uzaklaştırmak, katılımcıyı değiştiren ettirgen uzantıdır."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan ve hayvandaki kaçınmayı, uzaklaşmayı ve bir başkasını ürkütüp uzaklaştıran ettirgen eylemi birlikte kapsar.","boundary_detail":"Dal kaçınma, ürkme ve uzaklaştırmayı kapsar; genel ışık ya da topluluklar arası düşmanlık anlamına girmez.","branch_image_ar":"النِّفار وقلة الثبات","concept_gloss":"ürkmek, kaçınmak ve uzaklaştırmak","contextual_glosses":[{"applicability":"Bir insanın ya da hayvanın istemediği şeyden kaçınarak uzak durması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkasını ürkütüp uzaklaştıran ettirgen kullanımı dışarıda bırakır.","preserves":"Ürkme, kaçınma ve uzaklaşma çekirdeğini korur."},"facet_ids":["F001","F002"],"text":"ürkü̈p uzaklaşmak","usage_role":"general"},{"applicability":"Bir kişinin söz veya davranışla başka birini kaçırması ya da uzak durmaya itmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öznenin kendisinin kaçınması ile insan ve hayvan nitelemelerini dışarıda bırakır.","preserves":"Başka bir katılımcıyı ürkütüp uzaklaştırma eylemini korur."},"facet_ids":["F003"],"text":"ürkü̈tüp uzaklaştırmak","usage_role":"contextual"}],"definition":"Bir insanın ya da hayvanın hoş görülmeyen bir şeyden, kişiden veya eşten ürküp kaçınmasını ve uzaklaşmasını anlatır. Ettirgen kullanımda bir başkasını söz veya davranışla ürkütüp uzaklaştırma vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyden ürkme, kaçınma ve uzaklaşma temel hareket ve tutumdur."},{"facet_id":"F002","role":"specialization","statement":"Kötülükten veya erkeklerden uzak duran kadın ile eşten kaçınan dişi hayvan, katılımcıya bağlı özel nitelemelerdir."},{"facet_id":"F003","role":"extension","statement":"Bir başkasını söz veya davranışla ürkütüp uzaklaştırmak, katılımcıyı değiştiren ettirgen uzantıdır."}],"identity_rationale":"Kaynak ifadesi insanın kötülükten veya erkeklerden uzak durmasını, hayvanın ürküp eşinden kaçınmasını, bir şeyden uzaklaşmayı ve başkasını ürkütmeyi ortak bir kaçınma çekirdeğinde toplar. Geçici çerçeve kapsamı ve ettirgen katılımcı değişimini doğru verir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kötülükten veya erkeklerden uzak duran iffetli kadın"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"ürkek ve insandan kaçan ceylanlar"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kuşku verici durumdan uzak duran kadınlar"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"eşinden ürküp kaçınan kısrak veya inek"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir şeyden ürküp uzaklaşmak"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"birini söz veya davranışla ürkütüp uzaklaştırmak"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"ürkme, kaçınma ve uzaklaşma"}],"lexicalization_note":"İnsan ve hayvan nitelemeleri ile kaçınma ve başkasını uzaklaştırma eylemleri ayrı tutulur; özel katılımcılar bütün dala zorunlu kılınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel uzaklaşma, hayvanın dirençli ürkekliği ve hoşnutsuzluktan kaçınma sınırlarını gösteren üçü seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli insan ve eşleşme bağlamlarını içerir; komşu dal korku ve düşünsel uzaklaşma dahil daha geniş bir kapsam taşır.","focus_only":"İffetli kadının kötülükten kaçınmasını ve dişi hayvanın eşten uzak durmasını özel olarak kapsar.","gloss":"ürkmek ve uzaklaşmak","neighbor_only":"Korku, vahşi hayvanın kaçışı ve gerçekten uzaklaşma gibi daha geniş neden ve nesnelere uzanır.","neighbor_ref":"root_001532/B001","relation_type":"near_synonym","shared_zone":"İki dal da insan veya hayvanın bir şeyden ürküp uzaklaşmasını ve başkasını uzaklaştırmayı kapsar."},{"boundary_match":"partial","distinction":"Odak dal kaçınma ve uzaklaştırma çekirdeğindedir; komşu dal hayvanın binilmeye direnmesi ve zor huy gibi ek davranışları içerir.","focus_only":"İnsan için ahlaki kaçınmayı ve başkasını ürkütme eylemini kapsar.","gloss":"hayvanın ürkekliği","neighbor_only":"Hayvanın sırtını kullandırmaması ile insandaki huysuzluk ve geçimsizliği kapsar.","neighbor_ref":"root_000818/B002","relation_type":"near_synonym","shared_zone":"İki dal da hayvanın ürkmesi, yaklaşanı kabul etmemesi ve yerinde durmaması alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal ürkme ve kaçışı öne çıkarır; komşu dal hoşnutsuzluk ve tiksinme nedenlerine göre çeşitlenir.","focus_only":"Kötülükten uzak duran kadın ile bir başkasını ürkütüp uzaklaştırmayı kapsar.","gloss":"istenmeyenden kaçınma","neighbor_only":"Yemden, ülkeden, sinekten ve çeşitli isteklerden tiksinme gibi belirli hoşnutsuzluk nedenlerini kapsar.","neighbor_ref":"root_000060/B006","relation_type":"near_synonym","shared_zone":"İki dal da insan veya hayvanın istemediği bir şeye yaklaşmaması ve ondan uzak durmasıdır."}],"source_phrase_ar":"امرأة نوار وهي العفيفة النافرة عن الشر والقبيح؛ التي تكره الرجال؛ بقرة نوار تنفر من الفحل؛ نرت فلانا أي أنفرته (ayn)؛ النور أيضا: النفر من الظباء؛ نسوة نور أي نفر من الربية؛ الواحدة نوار وهي الفرور؛ فرس وديق نوار؛ نرت من الشئ؛ نرت غيري أي نفرته (sihah)؛ امرأة نوار أي عفيفة تنور أي تنفر من القبيح؛ نارت نفرت؛ نرت فلانا نفرته؛ النوار النفار (maqayis)","source_summary":"Kaynaklar ürkme ve uzak durma çekirdeğinde birleşir; insanın ahlaki ya da toplumsal kaçınmasını, hayvanın eşten uzaklaşmasını ve başkasını ürkütme eylemini aynı dalda verir.","sources":["AY","SI","MQ"],"what_is_ar":"يدخل فيه نوار للمرأة العفيفة النافرة من القبيح أو الرجال، والنور أو النوار في الظباء والنساء والفرس والبقرة النافرة، ونرت فلانا إذا أنفرته.","what_is_not_ar":"لا يدخل فيه النور بمعنى الضياء، ولا نور الشجر، ولا النائرة بمعنى العداوة."},"support_links":[]},{"boundary":"Dal topluluklar arasında var olan düşmanlık ve kine aittir; savaşın kendisini veya yalnız ilan edilmesini zorunlu kılmaz.","branch_kind":"bare","branch_ref":"root_001564/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:11:1:1","qac_word_ref":"101:11:1","surface_ar":"نَارٌ"}],"gloss":"topluluklar arası düşmanlık ve kin","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Topluluklar arasında ortaya çıkan düşmanlık ve kin, dalın ilişkisel çekirdeğidir."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki topluluk arasında doğan ve süren düşmanlık durumunu genel olarak karşılar.","boundary_detail":"Dal topluluklar arasında var olan düşmanlık ve kine aittir; savaşın kendisini veya yalnız ilan edilmesini zorunlu kılmaz.","branch_image_ar":"النائرة بين القوم","concept_gloss":"topluluklar arası düşmanlık ve kin","contextual_glosses":[{"applicability":"İki topluluğun ilişkisindeki kin ve karşıtlık doğal bir cümle içinde anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taraflar arasında süren düşmanlık ve kin durumunu korur."},"facet_ids":["F001"],"text":"aralarında düşmanlık var","usage_role":"contextual"}],"definition":"İki topluluk arasında ortaya çıkan ve ilişkilerini bozan düşmanlık, kin ve geçimsizlik durumunu anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Topluluklar arasında ortaya çıkan düşmanlık ve kin, dalın ilişkisel çekirdeğidir."}],"identity_rationale":"Kaynak ifadesi topluluklar arasında ortaya çıkan düşmanlık ve kini açıkça belirtir. Geçici çerçeve bu ilişkisel durumu doğru yansıtır ve onu fiziksel ateş, bireysel ürkme veya yalnız açık düşmanlık ilanıyla karıştırmaz.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"topluluklar arasında çıkan düşmanlık ve kin"}],"lexicalization_note":"Tanım yalın düşmanlık durumu ile sınırlıdır; savaş, açık ilan veya çatışma gibi komşu sonuçlar zorunlu anlam yapılmaz.","neighbor_coverage_note":"Tüm adaylar incelendi; savaş, etkin çatışma ve düşmanlığı açıkça gösterme ile olan üç temel kapsam farkı seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal düşmanlık durumunda kalır; komşu dal bu durumdan fiili savaşa, yere ve katılımcıya kadar genişler.","focus_only":"Özellikle topluluklar arasında ortaya çıkan kin ve bozuk ilişkiyi anlatır.","gloss":"düşmanlık ve savaş","neighbor_only":"Savaş eylemini, savaş durumunu, savaş ülkesini ve savaşan kişiyi de kapsar.","neighbor_ref":"root_000302/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da taraflar arasındaki düşmanlık ve barış karşıtı ilişkiyi kapsar."},{"boundary_match":"partial","distinction":"Odak dal ilişkisel düşmanlık durumudur; komşu dal düşmanlığın karşılıklı mücadele ve savaş halinde gerçekleşmesini öne çıkarır.","focus_only":"Fiili çarpışma olmadan da topluluklar arasındaki kin durumunu anlatabilir.","gloss":"düşmanlık ve çatışma","neighbor_only":"Karşılıklı savaşma, dövüşme ve etkin çatışmayı özellikle kapsar.","neighbor_ref":"root_001550/B007","relation_type":"near_synonym","shared_zone":"İki dal da tarafların birbirine düşman olması alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal durumun kendisidir; komşu dal bu durumun açıkça gösterilmesi ve ilan edilmesi eylemidir.","focus_only":"Düşmanlığın varlığını anlatır ve onun açıkça ilan edilmesini gerektirmez.","gloss":"düşmanlığı açığa vurmak","neighbor_only":"Düşmanlığın gizlenmeden açıkça ortaya konması eylemini anlatır.","neighbor_ref":"root_000097/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da taraflar arasındaki düşmanlık ilişkisine dayanır."}],"source_phrase_ar":"النائرة الكائنة تقع بين القوم (ayn)؛ بينهم نائرة أي عداوة وشحناء (sihah)","source_summary":"Kaynaklar anlamı topluluklar arasında beliren düşmanlık ve kin durumu olarak ortak biçimde açıklar.","sources":["AY","SI"],"what_is_ar":"يدخل فيه النائرة الواقعة بين القوم بمعنى العداوة والشحناء.","what_is_not_ar":"لا يدخل فيه النار الحسية، ولا النِّفار، ولا الضياء."},"support_links":[]},{"boundary":"Duman maddesi yalnız göz boyası veya dövme kullanımında yer alır; genel duman ve genel ışık anlamı bu dala girmez.","branch_kind":"bare","branch_ref":"root_001564/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:11:1:1","qac_word_ref":"101:11:1","surface_ar":"نَارٌ"}],"gloss":"göz boyası ve dövme için kullanılan duman karası","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Fitil veya yağ dumanından elde edilen ve göz boyası ya da dövmede kullanılan koyu madde temel nesnedir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Deri veya diş eti iğnelendikten sonra açılan yerlere koyu madde sürme işlemi, nesneye bağlı eylemdir."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Duman kökenli koyu maddeyi ve iğneleme sonrasında bu maddeyi uygulama eylemini birlikte kapsar.","boundary_detail":"Duman maddesi yalnız göz boyası veya dövme kullanımında yer alır; genel duman ve genel ışık anlamı bu dala girmez.","branch_image_ar":"دخان الوشم والكحل","concept_gloss":"göz boyası ve dövme için kullanılan duman karası","contextual_glosses":[{"applicability":"Fitil veya yağ dumanından elde edilip göz çevresinde ya da dövmede kullanılan koyu madde anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Deriyi veya diş etini iğneleyip madde uygulama eylemini dışarıda bırakır.","preserves":"Duman kökenli koyu madde ve onun göz boyası ile dövme amaçlarını korur."},"facet_ids":["F001"],"text":"duman karası","usage_role":"explanatory"},{"applicability":"Deri ya da diş etinde iğneyle açılan yerlere koyu madde veya göz boyası uygulanması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kullanılan duman kökenli maddenin bağımsız ad anlamını dışarıda bırakır.","preserves":"İğneleme ile ardından boya maddesi uygulama aşamalarını korur."},"facet_ids":["F002"],"text":"iğneleyip boya serpmek","usage_role":"contextual"}],"definition":"Fitil ya da yağ dumanından elde edilip göz boyası veya dövme maddesi olarak kullanılan koyu ürünü anlatır. Buna bağlı eylem, deri ya da diş etini iğneleyip açılan yerlere bu ürünü veya göz boyasını serpmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Fitil veya yağ dumanından elde edilen ve göz boyası ya da dövmede kullanılan koyu madde temel nesnedir."},{"facet_id":"F002","role":"associated_use","statement":"Deri veya diş eti iğnelendikten sonra açılan yerlere koyu madde sürme işlemi, nesneye bağlı eylemdir."}],"identity_rationale":"Kaynak ifadesi fitil ya da yağ dumanından elde edilen koyu maddeyi göz boyası veya dövme malzemesi olarak tanımlar; ayrıca deriyi ya da diş etini iğneleyip bu maddeyi veya göz boyasını uygulama eylemini verir. Geçici çerçeve kullanım amacını doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"göz boyası veya dövme için kullanılan fitil ya da yağ dumanı karası"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"deriyi veya diş etini iğneleyip üzerine duman karası ya da göz boyası serpmek"}],"lexicalization_note":"Tanım yalın dalda kozmetik ve dövme amaçlı duman maddesi ile buna bağlı iğneleme işlemini kapsar; genel dumana genişlemez.","neighbor_coverage_note":"Bütün adaylar incelendi; genel siyahlık, alevsiz duman ve göz boyası alanlarıyla en güçlü üç sınır karşılaştırması seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kullanım amacıyla sınırlı bir boya maddesidir; komşu dal genel siyahlık, kömür, kül ve duman alanına yayılır.","focus_only":"Duman karasını göz boyası veya dövme maddesi olarak ve iğneleme işleminde kullanır.","gloss":"duman karası ve genel siyahlık","neighbor_only":"Kömür, yanık kül, yoğun kara duman ve insan, hayvan ya da bitkideki genel siyahlığı kapsar.","neighbor_ref":"root_000001/B001","relation_type":"near_neighbor","shared_zone":"İki dal da yanma ya da duman sonucunda oluşan koyu siyah madde alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal dumanın kullanım için elde edilen katımsı karasına odaklanır; komşu dal dumanın kendisini anlatır.","focus_only":"Duman ürünü göz boyası veya dövme maddesi olarak toplanıp uygulanır.","gloss":"alevsiz duman ve boya maddesi","neighbor_only":"Alevsiz dumanı, herhangi bir kozmetik veya dövme amacı olmadan anlatır.","neighbor_ref":"root_001480/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da alevden ayrı düşünülebilen duman alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal maddenin duman kökeni ve dövme işleviyle tanımlanır; komşu dal parlatma ve görüşü açma işlevine yönelir.","focus_only":"Duman kökenli maddeyi dövmede de kullanır ve iğneleme sonrası uygulama işlemini kapsar.","gloss":"göz boyası kullanımı","neighbor_only":"Kılıcı parlatma ve görüşü açtığı düşünülen göz boyasını kapsar.","neighbor_ref":"root_000256/B002","relation_type":"same_field","shared_zone":"İki dal da göze uygulanan koyu boya maddesi alanında kesişir."}],"source_phrase_ar":"النؤور دخان الفتيلة يتخذ كحلا أو وشما (ayn)؛ النوور: النيلج، وهو دخان الشحم يعالج به الوشم؛ وقد نور ذراعه إذا غرزها بإبرة ثم ذر عليها النوور (sihah)؛ مما شذ عن هذا الأصل النؤور دخان الفتيلة يتخذ كحلا ووشما؛ نورت اللثة غرزتها بإبرة ثم جعلت في الغرز الإثمد (maqayis)","source_summary":"Kaynaklar duman kökenli koyu maddenin göz boyası ve dövme amacıyla kullanımında birleşir; iğneleme sonrası bu maddeyi ya da göz boyasını uygulama işlemini de açıklar.","sources":["AY","SI","MQ"],"what_is_ar":"يدخل فيه النُّؤور أو النُّوور، وهو دخان الفتيلة أو الشحم المتخذ كحلا أو وشما، ويدخل فيه نور العضو إذا غرز ثم ذر عليه الإثمد أو النُّوور.","what_is_not_ar":"لا يدخل فيه ضياء النور، ولا دخان النار مطلقا بلا استعمال كحل أو وشم."},"support_links":[]},{"boundary":"Dal bedene sürülen belirli madde ve onun uygulanmasıyla sınırlıdır; her türlü yağ, boya veya yapıştırıcıyı kapsamaz.","branch_kind":"bare","branch_ref":"root_001564/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:11:1:1","qac_word_ref":"101:11:1","surface_ar":"نَارٌ"}],"gloss":"bedene sürülen özel karışım ve onu sürünme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bedene sürülmek için kullanılan özel karışım, dalın nesne anlamıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin bu karışımı kendi bedenine sürmesi, nesne anlamına bağlı eylemdir."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özel maddenin kendisini ve kişinin onu bedenine uygulamasını birlikte karşılar.","boundary_detail":"Dal bedene sürülen belirli madde ve onun uygulanmasıyla sınırlıdır; her türlü yağ, boya veya yapıştırıcıyı kapsamaz.","branch_image_ar":"النُّورَة المطلية","concept_gloss":"bedene sürülen özel karışım ve onu sürünme","contextual_glosses":[{"applicability":"Kişisel bakım amacıyla bedene sürülen özel maddenin kendisi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin bu maddeyi kendi bedenine sürmesi eylemini dışarıda bırakır.","preserves":"Maddenin bedene sürülmek üzere hazırlanmış olmasını korur."},"facet_ids":["F001"],"text":"bedene sürülen karışım","usage_role":"explanatory"},{"applicability":"Bir kişinin söz konusu özel karışımı kendi bedenine uygulaması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uygulanan özel maddenin bağımsız ad anlamını dışarıda bırakır.","preserves":"Kişinin maddeyi kendi bedenine uygulama eylemini korur."},"facet_ids":["F002"],"text":"bedenine sürmek","usage_role":"contextual"}],"definition":"Bedene sürülen özel bir karışımı ve kişinin bu karışımı bedenine sürmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bedene sürülmek için kullanılan özel karışım, dalın nesne anlamıdır."},{"facet_id":"F002","role":"extension","statement":"Kişinin bu karışımı kendi bedenine sürmesi, nesne anlamına bağlı eylemdir."}],"identity_rationale":"Kaynak ifadesi bedene sürülen özel bir maddeyi ve kişinin bu maddeyi bedenine sürmesini açıkça verir. Geçici çerçeve nesne ile uygulama eylemini doğru bir arada tutar ve onu ışık, duman karası veya genel boya anlamına genişletmez.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bedene sürülen özel karışım"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"özel karışımı bedenine sürmek"}],"lexicalization_note":"Tanım yalın dalın bedene sürülen özel madde ve onu sürünme anlamıyla sınırlıdır; komşu kaplama maddeleri içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yağlama, metal araçla beden bakımı ve sıva benzeri kaplama arasındaki üç sınır seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal özel madde ve beden nesnesine bağlıdır; komşu dal maddenin yağ olması ve daha genel yüzeylere uygulanmasıyla tanımlanır.","focus_only":"Belirli bir karışımın insan bedenine uygulanmasıyla sınırlıdır.","gloss":"bedene sürülen madde ve yağ","neighbor_only":"Her tür yağ ve yağlama eylemini, nesnesi beden olsun olmasın kapsar.","neighbor_ref":"root_000497/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir maddeyi yüzeye sürerek kaplama eylemini kapsar."},{"boundary_match":"thematic_only","distinction":"Anlamsal çekirdekleri farklıdır: odak dal madde sürmedir, komşu dal metal araçla kesme veya keskinleştirmedir.","focus_only":"Bedene bir karışım sürerek bakım yapmayı anlatır.","gloss":"beden bakımı","neighbor_only":"Demir araç kullanmayı, kıl kesmeyi ve bıçağı keskinleştirmeyi anlatır.","neighbor_ref":"root_000002/B008","relation_type":"thematic","shared_zone":"İki dal kişisel bakım senaryosunda, özellikle beden üzerindeki uygulamalarda buluşabilir."},{"boundary_match":"field_only","distinction":"Odak dal beden uygulamasıdır; komşu dal yapı sıvası ve beyazlık belirtisi çevresinde toplanır.","focus_only":"İnsan bedenine sürülen özel karışımı ve kişinin onu uygulamasını kapsar.","gloss":"sürülen açık renkli madde","neighbor_only":"Yapı ve mezarların sıvanmasını, ayrıca bedensel bir beyazlık belirtisini kapsar.","neighbor_ref":"root_001232/B007","relation_type":"same_field","shared_zone":"İki dal yüzeye sürülen bir madde ve kaplama görüntüsü alanında ilişkilidir."}],"source_phrase_ar":"النورة يطلى بها (ayn)؛ تنور الرجل: تطلى بالنورة (sihah)","source_summary":"Kaynaklar bedene sürülen özel maddeyi ve bir kişinin bu maddeyi kendi bedenine sürmesi eylemini aynı dalda verir.","sources":["AY","SI"],"what_is_ar":"يدخل فيه النُّورَة التي يطلى بها، وتنور الرجل إذا تطلى بالنُّورَة.","what_is_not_ar":"لا يدخل فيه النور بمعنى الضوء، ولا النُّؤور دخان الفتيلة، ولا نور الشجر."},"support_links":[]},{"boundary":"Anlam yalnız kişi yöneltmeli yapıda bir işi karıştırıp yanıltmaktır; genel gizleme veya açıklama anlamına yayılmaz.","branch_kind":"collocation","branch_ref":"root_001564/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:11:1:1","qac_word_ref":"101:11:1","surface_ar":"نَارٌ"}],"gloss":"bir işi karışık gösterip yanıltmak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işi muhataba karışık göstererek onu yanıltmak, yapının temel eylemidir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynak, bu kullanımın kökenini bütünüyle yerli saymadığını ayrıca belirtir."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız belirli bir kişiye yönelen ve bir işi ona karışık gösteren yapı için geçerlidir.","boundary_detail":"Anlam yalnız kişi yöneltmeli yapıda bir işi karıştırıp yanıltmaktır; genel gizleme veya açıklama anlamına yayılmaz.","branch_image_ar":"التلبيس على الغير","concept_gloss":"bir işi karışık gösterip yanıltmak","contextual_glosses":[{"applicability":"Bir işi bir kişiye belirsiz veya başka türlü göstererek onun doğru anlamasını engelleme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiye yönelen karıştırma ve onu doğru anlamdan uzaklaştırma eylemini korur."},"facet_ids":["F001","F002"],"text":"kafasını karıştırmak","usage_role":"contextual"}],"definition":"Belirli bir kişiye bir işi karışık ve başka türlü göstererek onun doğru anlamasını engellemeyi anlatan yapıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işi muhataba karışık göstererek onu yanıltmak, yapının temel eylemidir."},{"facet_id":"F002","role":"source_variant","statement":"Kaynak, bu kullanımın kökenini bütünüyle yerli saymadığını ayrıca belirtir."}],"identity_rationale":"Kaynak ifadesi belirli bir kişi yöneltmeli yapıda bir işi ona karışık gösterip onu yanıltma anlamını açıkça verir. Bununla birlikte kaynak kullanımın bütünüyle yerli olmadığını belirtir; bu nedenle anlam kabul edilirken köken açıklaması kesinleştirilmez.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"bir işi birine karışık gösterip onu yanıltmak"}],"lexicalization_note":"Tanım yalnız verilen kişi yöneltmeli yapıya bağlıdır; yalın biçime genel yanıltma anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel belirsizleştirme, gizleme, hile ve açıklığa çıkarma karşıtlığı en yararlı dört sınır olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal muhatabı yanıltan belirli bir yapıdır; komşu dal nesnenin karışması veya karıştırılması biçiminde daha genel bir kapsama sahiptir.","focus_only":"Belirli bir kişi yöneltmeli yapıda bir işi ona karışık gösterir.","gloss":"karıştırmak ve belirsizleştirmek","neighbor_only":"İşin, sözün veya karanlığın kendisinin karışıp belirsizleşmesini daha genel biçimde kapsar.","neighbor_ref":"root_001341/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir işin anlaşılmasını güçleştiren karışıklık ve belirsizlik yaratır."},{"boundary_match":"partial","distinction":"Odak dal yanlış veya karışık görünüm üretir; komşu dal bilginin kendisini saklar ve görünmez kılar.","focus_only":"İşi kişiye başka türlü göstererek zihinsel karışıklık yaratır.","gloss":"yanıltmak ve gizlemek","neighbor_only":"İşi doğrudan gizleyip kişinin ondan haberdar olmasını engeller.","neighbor_ref":"root_001617/B009","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişinin bir işi doğru biçimde öğrenmesini engeller."},{"boundary_match":"partial","distinction":"Odak dal anlama sürecini karıştırır; komşu dal gizli amaç taşıyan daha geniş bir hile ve davranış düzenini anlatır.","focus_only":"Kişiye belirli bir işi karışık gösterme yapısıyla sınırlıdır.","gloss":"aldatıcı karıştırma","neighbor_only":"Bir şeyi gösterip başka bir şeyi amaçlayan hileli davranışı ve kalıplaşmış sözü kapsar.","neighbor_ref":"root_000439/B008","relation_type":"near_neighbor","shared_zone":"İki dal da görünüş ile gerçek amaç arasındaki ayrılıktan yararlanarak karşı tarafı yanıltır."},{"boundary_match":"opposed","distinction":"Odak dal anlaşılabilirliği azaltır ve yanıltır; komşu dal görünürlüğü ve açıklığı artırır.","focus_only":"Bir işi anlaşılmaz veya yanlış anlaşılır hale getirir.","gloss":"karıştırma ve açıklığa çıkarma","neighbor_only":"Bir şeyin görünür, açık ve kanıtlanabilir hale gelmesini anlatır.","neighbor_ref":"root_000170/B004","relation_type":"polarity_pair","shared_zone":"İki dal da bir işin muhatap tarafından ne ölçüde açıkça anlaşılabildiği eksenindedir."}],"source_phrase_ar":"فلان ينور على فلان إذا شبه عليه أمرا؛ ليست الكلمة بعربية محضة؛ امرأة كانت تسمى نورة (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Bir işi kişiye karışık gösterip onu yanıltan yapı tek başına tanıklanır; kullanımın bütünüyle yerli olmadığı da belirtilir."}],"source_summary":"Dalın anlamı ve köken sınırlaması tek bir kaynak tanıklığına dayanır.","sources":["AY"],"what_is_ar":"يدخل فيه قولهم نور على فلان إذا شبه عليه أمرا.","what_is_not_ar":"لا يدخل فيه الإنارة، ولا النُّورَة، ولا النار."},"support_links":[]},{"boundary":"Anlam kümesi açıklık ve belirgin çıkıntı çevresinde tutulur; incelenen köke bağlılığı olasılık düzeyindedir.","branch_kind":"mixed_non_bare","branch_ref":"root_001564/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:11:1:1","qac_word_ref":"101:11:1","surface_ar":"نَارٌ"}],"gloss":"açıkça seçilen veya belirgin biçimde çıkan şey","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin açıkça seçilmesi ve çevresinden belirgin biçimde çıkması ortak anlam ilkesidir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Açık yol oluğu ve kumaştaki belirgin işaret, görünürlük ilkesinin nesne örnekleridir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çift hayvanının boynuna konan boyunduruk ve iki kat güçle nitelenen kişi, kümenin özel kullanımlarıdır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bu ses yapısının incelenen köke dönmesi kaynakta kesinlik değil, yalnız olasılık olarak sunulur."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yol oluğu, kumaş işareti, boyunduruk ve güç nitelemesini ortak belirginlik ilkesiyle, kök bağına kesinlik vermeden kapsar.","boundary_detail":"Anlam kümesi açıklık ve belirgin çıkıntı çevresinde tutulur; incelenen köke bağlılığı olasılık düzeyindedir.","branch_image_ar":"وضوح النِّير وبروزه","concept_gloss":"açıkça seçilen veya belirgin biçimde çıkan şey","contextual_glosses":[{"applicability":"Yol üzerinde açıkça görülen uzun çukur ya da iz anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kumaş işareti, boyunduruk, güç nitelemesi ve kök belirsizliğini dışarıda bırakır.","preserves":"Yoldaki açıkça seçilen oluk ve belirginlik özelliğini korur."},"facet_ids":["F001","F002"],"text":"belirgin yol oluğu","usage_role":"contextual"},{"applicability":"Çift süren hayvanın boynuna aracıyla birlikte konan ağaç parça anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yol oluğu, kumaş işareti, güç nitelemesi ve kök belirsizliğini dışarıda bırakır.","preserves":"Hayvanın boynuna konan belirgin ağaç parça anlamını korur."},"facet_ids":["F001","F003"],"text":"çift hayvanı boyunduruğu","usage_role":"contextual"}],"definition":"Açıkça seçilen veya çevresinden belirgin biçimde çıkan şeyleri anlatan bir kümedir; açık yol oluğu, kumaştaki belirgin işaret, çift hayvanının boynundaki boyunduruk ve gücü iki kat sayılan kişi bu çerçevede verilir. Kümenin incelenen köke bağlılığı kesin değil, olasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin açıkça seçilmesi ve çevresinden belirgin biçimde çıkması ortak anlam ilkesidir."},{"facet_id":"F002","role":"example","statement":"Açık yol oluğu ve kumaştaki belirgin işaret, görünürlük ilkesinin nesne örnekleridir."},{"facet_id":"F003","role":"specialization","statement":"Çift hayvanının boynuna konan boyunduruk ve iki kat güçle nitelenen kişi, kümenin özel kullanımlarıdır."},{"facet_id":"F004","role":"source_variant","statement":"Bu ses yapısının incelenen köke dönmesi kaynakta kesinlik değil, yalnız olasılık olarak sunulur."}],"identity_rationale":"Kaynak ifadesi bu kümeyi önce ayrı bir ses yapısı altında açıklık ve çıkıntı ilkesiyle kurar; yol oluğu, kumaş işareti, boyunduruk ve iki kat güç örneklerini verir. Aynı kaynak bunun incelenen köke dönmesinin mümkün olduğunu yalnız ihtimal olarak söyler, bu yüzden dal korunur ancak kök bağı kesin gösterilemez.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"yolun belirgin oluğu"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"kumaşın belirgin işareti veya çizgisi"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"çift hayvanının boynundaki boyunduruk ve takımı"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"gücü başkasının iki katı olan adam"}],"lexicalization_note":"Yol oluğu ve boyunduruk adları ile kumaş ve kişi yapıları ayrı tutulur; olası kök bağı bütün örnekleri yalın ışık anlamına dönüştürmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yol oluğu, işaret, koşum takımı ve görünür hale gelme alanlarıyla en açıklayıcı dört sınır seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kullanım açık yol oluğuna bağlı bir alt alandır; komşu dal malzeme ve yer bakımından daha geniş uzun yarık çekirdeğine sahiptir.","focus_only":"Yol üzerindeki açık oluğun yanında kumaş işareti, boyunduruk ve güç nitelemesini de kapsar.","gloss":"belirgin oluk ve uzun yarık","neighbor_only":"Toprakta veya bedende oluşan uzun, derin yarık ve kazılmış izleri daha genel biçimde kapsar.","neighbor_ref":"root_000395/B002","relation_type":"near_synonym","shared_zone":"İki dal da zeminde uzanan, çevresinden ayrılan oluk veya yarık biçimini kapsar."},{"boundary_match":"partial","distinction":"Odak dal kumaştaki işareti genel belirginlik ilkesine bağlar; komşu dalın çekirdeği nesnelerin kenarı boyunca uzanan yan çizgidir.","focus_only":"Kumaştaki belirgin işareti yol oluğu, boyunduruk ve güç nitelemesiyle aynı açıklık kümesinde verir.","gloss":"kumaş işareti ve yan çizgi","neighbor_only":"Dizgin ve yanak üzerindeki yan çizgiyi, duvar ve vadi kenarlarını, yan yana uzanan yolları kapsar.","neighbor_ref":"root_000995/B008","relation_type":"near_neighbor","shared_zone":"İki dal da bir yüzeyde uzanan ve çevresinden belirgin biçimde ayrılan çizgi ya da işaret alanında buluşur."},{"boundary_match":"field_only","distinction":"Odak parça boyun üzerindeki sert boyunduruktur; komşu parça karın ya da bel çevresinde kullanılan bağ ve iptir.","focus_only":"Çift hayvanının boynuna konan ağaç boyunduruğu ve takımını anlatır.","gloss":"hayvan koşum takımı","neighbor_only":"Devenin karnından geçirilen eyer bağı ile bele bağlanan ipi anlatır.","neighbor_ref":"root_000345/B002","relation_type":"same_field","shared_zone":"İki dal da yük veya araç bağlantısında hayvanın bedenine yerleştirilen koşum parçası alanındadır."},{"boundary_match":"partial","distinction":"Odak dal belirgin nesneleri adlandıran bir kümedir; komşu dal görünür hale gelme ve ortaya çıkma sürecini anlatır.","focus_only":"Belirginliği somut nesne adlarına ve güç nitelemesine dönüştürür.","gloss":"belirginlik ve ortaya çıkma","neighbor_only":"Yolun, gerçeğin, işin veya topluluğun görünür hale gelmesi eylem ve durumlarını kapsar.","neighbor_ref":"root_000268/B007","relation_type":"near_neighbor","shared_zone":"İki dal da bir şeyin çevresinden ayrılarak açıkça görünmesi düşüncesini paylaşır."}],"source_phrase_ar":"النون والياء والراء كلمة تدل على وضوح شيء وبروزه؛ أخدود الطريق الواضح منه نير؛ نير الثوب علمه؛ النير الخشبة على عنق الفدان؛ ما ننكر أن يكون أصل هذا كله الواو فيرجع إلى ما ذكرناه في باب النور والنار (maqayis)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık açıklık ve belirgin çıkıntı ilkesini yol oluğu, kumaş işareti, boyunduruk ve iki kat güç örnekleriyle verir; kök bağını ise olası sayar."}],"source_summary":"Dalın bütün anlamları ve kök bağlantısına ilişkin ihtimal tek bir kaynak tanıklığına dayanır.","sources":["MQ"],"what_is_ar":"يدخل فيه النِّير في أخدود الطريق الواضح، وعلم الثوب، والخشبة على عنق الفدان، وما قيس على الوضوح والبروز في مدخل نير.","what_is_not_ar":"لا يدخل فيه جذر ن و ر إلا على احتمال رجوع الواو الذي ذكره مقاييس."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["101:11:1"],"branch_refs":[],"candidate_id":"cand_5aab5fa7e1097667b1b5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001564"],"scope":"focus_ayah","source_local_id":"101:11:1:compressed-nominal-answer","source_type":"word_analysis","support_ids":["sup_97e778758d2ac98fda0c","sup_db22298a681fa792d558"],"title":"compressed nominal answer","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:11:1","qac_refs":["101:11:1:1"],"status":"accepted"}},{"anchor_refs":["101:11:1"],"branch_refs":[],"candidate_id":"cand_9acd5ad1071b08a5da7d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001564"],"scope":"focus_ayah","source_local_id":"101:11:1:convergent-answer-pressure","source_type":"word_analysis","support_ids":["sup_6caaf5c6b01126c3f54f","sup_db22298a681fa792d558"],"title":"ellipsis, indefiniteness, and root pressure converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:11:1","qac_refs":["101:11:1:1"],"status":"accepted"}},{"anchor_refs":["101:11:1"],"branch_refs":["root_001564/B001"],"candidate_id":"cand_c9b1c6b4c9bc52e9c2c9","commentary_obligation":"candidate","focus_branch_refs":["root_001564/B001"],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001564"],"scope":"focus_ayah","source_local_id":"101:11:1:destructive-radiance","source_type":"word_analysis","support_ids":["sup_7820cd66702bb5de0e08","sup_db22298a681fa792d558"],"title":"fire-light family narrowed to burning radiance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:11:1","qac_refs":["101:11:1:1"],"status":"accepted"}},{"anchor_refs":["101:11:1"],"branch_refs":[],"candidate_id":"cand_404f0013b19be0e77fac","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001564"],"scope":"focus_ayah","source_local_id":"101:11:1:fire-heat-formula","source_type":"word_analysis","support_ids":["sup_96be923ffd3f3b226814","sup_db22298a681fa792d558"],"title":"fire-heat formula made nominative","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:11:1","qac_refs":["101:11:1:1"],"status":"accepted"}},{"anchor_refs":["101:11:1"],"branch_refs":[],"candidate_id":"cand_42fa704066fb9cff05ba","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001564"],"scope":"focus_ayah","source_local_id":"101:11:1:indefinite-fire-quality","source_type":"word_analysis","support_ids":["sup_35b57f65deddee60cefc","sup_db22298a681fa792d558"],"title":"indefinite qualitative fire","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:11:1","qac_refs":["101:11:1:1"],"status":"accepted"}},{"anchor_refs":["101:11:1"],"branch_refs":[],"candidate_id":"cand_2dfd9f09f78ba0019fc5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001564"],"scope":"focus_ayah","source_local_id":"101:11:1:sound-boundary-cadence","source_type":"word_analysis","support_ids":["sup_4687eef4fd4dd1ecc034","sup_db22298a681fa792d558"],"title":"sound turns question into substance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:11:1","qac_refs":["101:11:1:1"],"status":"accepted"}},{"anchor_refs":["101:11:2"],"branch_refs":[],"candidate_id":"cand_0537ebf5e547ad4180b1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000358"],"scope":"focus_ayah","source_local_id":"101:11:2:adjective-standing-heat","source_type":"word_analysis","support_ids":["sup_5576f90bd801c4357500","sup_8f7882169552bdd0e1f3"],"title":"adjective makes heat a standing property","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:11:2","qac_refs":["101:11:2:1"],"status":"accepted"}},{"anchor_refs":["101:11:2"],"branch_refs":["root_000358/B001"],"candidate_id":"cand_5e6b9eaec877d6f1636e","commentary_obligation":"candidate","focus_branch_refs":["root_000358/B001"],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000358"],"scope":"focus_ayah","source_local_id":"101:11:2:boundary-shift-to-impersonal-heat","source_type":"word_analysis","support_ids":["sup_5576f90bd801c4357500","sup_f1f4b7e2df1eb4727ae6"],"title":"question boundary becomes impersonal heat","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:11:2","qac_refs":["101:11:2:1"],"status":"accepted"}},{"anchor_refs":["101:11:2"],"branch_refs":[],"candidate_id":"cand_38b8b21c38b493892c37","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000358"],"scope":"focus_ayah","source_local_id":"101:11:2:final-closure-cadence","source_type":"word_analysis","support_ids":["sup_5576f90bd801c4357500","sup_e5e45e6ceafbd2eb1170"],"title":"final heat as closure landing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:11:2","qac_refs":["101:11:2:1"],"status":"accepted"}},{"anchor_refs":["101:11:2"],"branch_refs":[],"candidate_id":"cand_6d1d19d8414e6b0ec1dd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000358"],"scope":"focus_ayah","source_local_id":"101:11:2:marked-fire-heat-pair","source_type":"word_analysis","support_ids":["sup_5576f90bd801c4357500","sup_a97cfd60bbe1e08be2e2"],"title":"marked fire-heat pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:11:2","qac_refs":["101:11:2:1"],"status":"accepted"}},{"anchor_refs":["101:11:2"],"branch_refs":["root_000358/B001"],"candidate_id":"cand_5c24bde719f39f52e0b8","commentary_obligation":"must_integrate","focus_branch_refs":["root_000358/B001"],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000358"],"scope":"focus_ayah","source_local_id":"101:11:2:repelling-thermal-root","source_type":"word_analysis","support_ids":["sup_1a709eb0c6ceffb62cb3","sup_5576f90bd801c4357500"],"title":"thermal heat with repelling root pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:11:2","qac_refs":["101:11:2:1"],"status":"accepted"}},{"anchor_refs":["101:11:2"],"branch_refs":["root_000358/B006"],"candidate_id":"cand_3517e6fa56f85e7cd47c","commentary_obligation":"candidate","focus_branch_refs":["root_000358/B006"],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000358"],"scope":"focus_ayah","source_local_id":"101:11:2:variant-muddy-contrast","source_type":"word_analysis","support_ids":["sup_5576f90bd801c4357500","sup_5a313d3382ca1d178087"],"title":"irregular variant exposes the final slot","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:11:2","qac_refs":["101:11:2:1"],"status":"accepted"}},{"anchor_refs":["101:11:1"],"branch_refs":[],"candidate_id":"cand_ef33e555448365aba672","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001564"],"scope":"focus_ayah","source_local_id":"101:11:1:1","source_type":"qac_morpheme","support_ids":["sup_1102b5ae10284c0110c3"],"title":"QAC root occurrence: ن و ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["101:11:2"],"branch_refs":[],"candidate_id":"cand_ce317d2120779981b41a","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000358"],"scope":"focus_ayah","source_local_id":"101:11:2:1","source_type":"qac_morpheme","support_ids":["sup_c96ebd47a842ba80d57a"],"title":"QAC root occurrence: ح م ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["101:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:11","branch_refs":["root_000358/B001","root_001564/B002"],"candidate_id":"cand_1a1863173e9f041ca7cd","commentary_obligation":"review","hft_ref":"hft_6f149935ef910ad77de4","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_combustive_intensity","source_type":"hft","support_ids":["sup_8c2f90e06aa06a751714"],"title":"base_combustive_intensity","trust":"legacy_unbound"},{"anchor_refs":["101:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:11","branch_refs":["root_000358/B001","root_001564/B001"],"candidate_id":"cand_db9a48af999f394e0b7b","commentary_obligation":"review","hft_ref":"hft_a60f75d009cd81b4b2e9","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_luminous_exposure","source_type":"hft","support_ids":["sup_1cbc60c875be9c5e4f1e"],"title":"base_luminous_exposure","trust":"legacy_unbound"},{"anchor_refs":["101:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:11","branch_refs":["root_000358/B002","root_001564/B002"],"candidate_id":"cand_af7bb7eafdfdcf84091b","commentary_obligation":"review","hft_ref":"hft_64c22cb57e43d1d07cb1","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_exclusionary_zone","source_type":"hft","support_ids":["sup_0c97f3d4cf7e81ec7639"],"title":"base_exclusionary_zone","trust":"legacy_unbound"},{"anchor_refs":["101:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:11","branch_refs":["root_000358/B007","root_000358/B008","root_001564/B002"],"candidate_id":"cand_3c7feb0f5d2e6730bc05","commentary_obligation":"review","hft_ref":"hft_b1937f3b94e90747ce1b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_stinging_surge","source_type":"hft","support_ids":["sup_31d221978bba061d14e8"],"title":"base_stinging_surge","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"نَارٌ حَامِيَةٌۢ","qac_morphemes":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:11:1:1","qac_word_ref":"101:11:1","root_ar":"ن و ر","surface_ar":"نَارٌ"},{"lemma_ar":"حَامِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:HaAmiyap|ROOT:Hmy|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:11:2:1","qac_word_ref":"101:11:2","root_ar":"ح م ي","surface_ar":"حَامِيَةٌۢ"}],"word_analysis_qac_refs":[["101:11:1:1"],["101:11:2:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["101:11:1","101:11:2"]},"focus_surface_evidence":{"arabic_uthmani":"نَارٌ حَامِيَةٌۢ","qac_morphemes":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:11:1:1","qac_word_ref":"101:11:1","root_ar":"ن و ر","surface_ar":"نَارٌ"},{"lemma_ar":"حَامِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:HaAmiyap|ROOT:Hmy|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:11:2:1","qac_word_ref":"101:11:2","root_ar":"ح م ي","surface_ar":"حَامِيَةٌۢ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["101:11:1:1"],["101:11:2:1"]],"word_analysis_refs":["101:11:1","101:11:2"],"word_rows":[{"analysis_record_ref":"101:11:1","analytic_gloss_range_en":"an indefinite nominative concrete fire noun, locally functioning as the compressed answer to the previous question","analytic_root_gloss_range_en":"broad root range of light, illumination, fire, visible markers, recoil, and other branches; locally narrowed to burning fire while retaining the fire-light family pressure","qac_refs":["101:11:1:1"],"root":{"arabic":"ن و ر","transliteration":"n-w-r"},"surface":{"arabic":"نَارٌ","transliteration":"nārun"}},{"analysis_record_ref":"101:11:2","analytic_gloss_range_en":"feminine active participle used adjectivally for intensely hot fire, with predicative force possible inside the nominal answer","analytic_root_gloss_range_en":"broad h-m-y range including heat, protection, zeal or anger, feverish intensity, and other lexical branches; locally narrowed to heat that repels and defines the fire","qac_refs":["101:11:2:1"],"root":{"arabic":"ح م ي","transliteration":"ḥ-m-y"},"surface":{"arabic":"حَامِيَةٌۢ","transliteration":"ḥāmiyah"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":2,"words_total":2,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["101:11"],"branch_refs":["root_000358/B001","root_001564/B002"],"candidate_id":"cand_1a1863173e9f041ca7cd","evidence_scope":"focus_ayah","hft_ref":"hft_6f149935ef910ad77de4","item_id":"base_combustive_intensity","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_combustive_intensity","support_id":"sup_8c2f90e06aa06a751714"},{"anchor_refs":["101:11"],"branch_refs":["root_000358/B001","root_001564/B001"],"candidate_id":"cand_db9a48af999f394e0b7b","evidence_scope":"focus_ayah","hft_ref":"hft_a60f75d009cd81b4b2e9","item_id":"base_luminous_exposure","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_luminous_exposure","support_id":"sup_1cbc60c875be9c5e4f1e"},{"anchor_refs":["101:11"],"branch_refs":["root_000358/B002","root_001564/B002"],"candidate_id":"cand_af7bb7eafdfdcf84091b","evidence_scope":"focus_ayah","hft_ref":"hft_64c22cb57e43d1d07cb1","item_id":"base_exclusionary_zone","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_exclusionary_zone","support_id":"sup_0c97f3d4cf7e81ec7639"},{"anchor_refs":["101:11"],"branch_refs":["root_000358/B007","root_000358/B008","root_001564/B002"],"candidate_id":"cand_3c7feb0f5d2e6730bc05","evidence_scope":"focus_ayah","hft_ref":"hft_b1937f3b94e90747ce1b","item_id":"base_stinging_surge","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_stinging_surge","support_id":"sup_31d221978bba061d14e8"}],"diagnostics":[],"lane_counts":{"global":12,"macro":13,"micro":4},"packet_summary":{"ayah_count":11,"focus_ref":"101:11","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["101:1","101:2","101:3","101:4","101:5","101:6","101:7","101:8","101:9","101:10","101:11"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"101:11","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":12,"source_present":true,"structured_insight_count":17,"unstructured_record_count":0},"identity":{"ayah_ref":"101:11","lane":"micro","linguistic_source_ref":"101:11","surface_ref":"101:11","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"101:11","target_tokens":[["Kızgın",["101:11:2"]],["bir",["101:11:1"]],["ateştir",["101:11:1"]]],"text":"Kızgın bir ateştir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s101-p01-001-011","label":"Whole surah","number":1,"refs":["101:1","101:2","101:3","101:4","101:5","101:6","101:7","101:8","101:9","101:10","101:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"101:11:1:1","source_type":"qac_morpheme","support_id":"sup_1102b5ae10284c0110c3","text":"{\"lemma_ar\":\"نَار\",\"morph_features\":\"STEM|POS:N|LEM:naAr|ROOT:nwr|F|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"101:11:1:1\",\"qac_word_ref\":\"101:11:1\",\"root_ar\":\"ن و ر\",\"surface_ar\":\"نَارٌ\"}","trust":"trusted"},{"branch_refs":["root_000358/B001"],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:11:2:repelling-thermal-root","source_type":"word_analysis","support_id":"sup_1a709eb0c6ceffb62cb3","text":"{\"blocking_evidence\":null,\"headline\":\"thermal heat with repelling root pressure\",\"reader_payoff\":\"The reader feels the final heat as a repelling, feverish, charged intensity while still reading the local word as hot fire.\",\"reason\":\"V4 supports heat, protection, and zeal branches for the root, but local attachment to {{ar:نَارٌ}} ({{tr:nārun}}) selects the heat branch and narrows the other branches to semantic pressure.\",\"representative_source_ids\":[\"QS-5e3ff63b\",\"QS-a99278fa\",\"QS-addff318\",\"MS-67e52315\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:11:1:indefinite-fire-quality","source_type":"word_analysis","support_id":"sup_35b57f65deddee60cefc","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite qualitative fire\",\"reader_payoff\":\"The reader sees that the answer is grammatically precise while still refusing a bounded or already titled name.\",\"reason\":\"The local noun is indefinite and nominative, and the agreeing indefinite adjective confirms that indefiniteness carries through the whole answer phrase.\",\"representative_source_ids\":[\"QF-3706745c\",\"QF-62b1f519\",\"QB-5e549b21\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:11:1:sound-boundary-cadence","source_type":"word_analysis","support_id":"sup_4687eef4fd4dd1ecc034","text":"{\"blocking_evidence\":null,\"headline\":\"sound turns question into substance\",\"reader_payoff\":\"The reader hears the transition from the previous suspended question into a compact fire-and-heat answer, not only a semantic reply.\",\"reason\":\"The sound rows are locally tied to the two-word surface and to the 101:10-to-101:11 answer boundary; the attachment evidence confirms that the two words form one noun-adjective unit.\",\"representative_source_ids\":[\"QE-995dfe34\",\"QP-00ac4e66\",\"QP-b90675a7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:11:2","source_type":"word_analysis","support_id":"sup_5576f90bd801c4357500","text":"{\"gloss_range\":\"feminine active participle used adjectivally for intensely hot fire, with predicative force possible inside the nominal answer\",\"prose\":\"{{ar:حَامِيَةٌۢ}} ({{tr:ḥāmiyah}}) locks the answer onto heat. It agrees with {{ar:نَارٌ}} ({{tr:nārun}}) and normally reads as its adjective, though the nominal frame can also let the adjective carry final predicative force; either route makes heat the closing definition, not a new action. As an active participle in a verbless sentence, the word presents heat as a standing property of the fire rather than a process that starts to happen. The local sense is thermal, but the {{ar:ح م ي}} ({{tr:ḥ-m-y}}) family lets that heat feel repelling, guarded, fever-like, and charged; the protection and zeal branches color the intensity without replacing the fire reading. The sparse active-participle fire-heat pair is especially marked beside 88:4, while 9:35 keeps h-m-y heat near punishment imagery. The reported {{ar:حَمِئَةٌ}} ({{tr:ḥamiʾah}}) variant is a useful apparatus contrast: a small hamza shift darkens the final slot toward muddy materiality, but it does not govern the canonical local parse. Because this is the final word of the surah, its heavier cadence and breath-texture make the listener land on heat as both sound and barrier, after the addressed knowing question of 101:10 has disappeared into an impersonal, verbless qualifier and the abyss word in 101:9 has turned in sound toward the closing heat word in 101:11.\",\"root_display\":\"{{ar:ح م ي}} ({{tr:ḥ-m-y}})\",\"root_gloss_range\":\"broad h-m-y range including heat, protection, zeal or anger, feverish intensity, and other lexical branches; locally narrowed to heat that repels and defines the fire\",\"surface_display\":\"{{ar:حَامِيَةٌۢ}} ({{tr:ḥāmiyah}})\"}","trust":"trusted"},{"branch_refs":["root_000358/B006"],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:11:2:variant-muddy-contrast","source_type":"word_analysis","support_id":"sup_5a313d3382ca1d178087","text":"{\"blocking_evidence\":null,\"headline\":\"irregular variant exposes the final slot\",\"reader_payoff\":\"The reader notices how much the final descriptor depends on root and sound: canonical heat can be contrasted with a reported muddy-dark variant without being displaced by it.\",\"reason\":\"The variant {{ar:حَمِئَةٌ}} ({{tr:ḥamiʾah}}) is preserved as apparatus contrast, but the canonical local surface remains {{ar:حَامِيَةٌۢ}} ({{tr:ḥāmiyah}}), so mud-darkness cannot replace heat in the main parse.\",\"representative_source_ids\":[\"QF-0925f90d\",\"QF-33325826\",\"QP-55b8b233\",\"QY-853c19fb\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:11:1:convergent-answer-pressure","source_type":"word_analysis","support_id":"sup_6caaf5c6b01126c3f54f","text":"{\"blocking_evidence\":null,\"headline\":\"ellipsis, indefiniteness, and root pressure converge\",\"reader_payoff\":\"The reader can hold together the missing subject, indefinite fire noun, and fire-light root pressure as one compressed answer rather than separate observations.\",\"reason\":\"The synthesis survives, but it is narrowed away from unsupported exclusivity claims and toward the locally checked convergence of answer ellipsis, indefiniteness, and concrete fire from the light-root family.\",\"representative_source_ids\":[\"MS-28d1187c\",\"QY-9d507a33\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":["root_001564/B001"],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:11:1:destructive-radiance","source_type":"word_analysis","support_id":"sup_7820cd66702bb5de0e08","text":"{\"blocking_evidence\":null,\"headline\":\"fire-light family narrowed to burning radiance\",\"reader_payoff\":\"The reader hears the answer as fire from the light-root family, so illumination arrives as consuming exposure rather than guidance.\",\"reason\":\"The local surface selects the concrete fire branch, while V4 also records the light and illumination branch for the same root; the topic is narrowed so the light-family pressure does not replace the local fire sense.\",\"representative_source_ids\":[\"QS-63c38a4e\",\"QS-9d383978\",\"QS-c856bb05\",\"QF-46e0da7a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:11:2:adjective-standing-heat","source_type":"word_analysis","support_id":"sup_8f7882169552bdd0e1f3","text":"{\"blocking_evidence\":null,\"headline\":\"adjective makes heat a standing property\",\"reader_payoff\":\"The reader sees heat as the fire's defining property in the nominal answer, not as a later action or separate predicate floating away.\",\"reason\":\"QAC identifies the word as a feminine active participle, and attachment evidence strongly licenses agreement with {{ar:نَارٌ}} ({{tr:nārun}}).\",\"representative_source_ids\":[\"QG-4d901a25\",\"QG-72b4cabb\",\"QG-b39dfd76\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:11:1:fire-heat-formula","source_type":"word_analysis","support_id":"sup_96be923ffd3f3b226814","text":"{\"blocking_evidence\":null,\"headline\":\"fire-heat formula made nominative\",\"reader_payoff\":\"The reader notices that a known fire-heat association is not merely repeated; it is shifted into a stark identity answer here.\",\"reason\":\"The CRITICAL rows point to the fire-heat wording in 88:4 and heated punishment in 9:35; local QAC case makes the current phrase nominative rather than an accusative object.\",\"representative_source_ids\":[\"QI-1bce2fb8\",\"QI-fff073f3\",\"QE-e4887237\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:11:1:compressed-nominal-answer","source_type":"word_analysis","support_id":"sup_97e778758d2ac98fda0c","text":"{\"blocking_evidence\":null,\"headline\":\"compressed nominal answer\",\"reader_payoff\":\"The reader notices that the ayah answers the question by identification, not by narrating a new event.\",\"reason\":\"QAC allows nominative predicate analysis, and translation support specifically marks the two-word phrase as the compressed answer to the previous question.\",\"representative_source_ids\":[\"QG-332f3a6b\",\"QG-bda732bd\",\"QT-1a79cb29\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:11:2:marked-fire-heat-pair","source_type":"word_analysis","support_id":"sup_a97cfd60bbe1e08be2e2","text":"{\"blocking_evidence\":null,\"headline\":\"marked fire-heat pair\",\"reader_payoff\":\"The reader recognizes the adjective as part of a sparse fire-heat pattern rather than ordinary descriptive heat vocabulary.\",\"reason\":\"The contextual profile gives this active-participle form only two instances and makes the fire noun its top partner; the CRITICAL rows tie that pattern to 88:4 and 9:35.\",\"representative_source_ids\":[\"QI-9e9f5d9a\",\"QI-ca2b75e4\",\"QH-cfe5ede2\",\"QE-35bc49d9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"101:11:2:1","source_type":"qac_morpheme","support_id":"sup_c96ebd47a842ba80d57a","text":"{\"lemma_ar\":\"حَامِيَة\",\"morph_features\":\"STEM|POS:ADJ|ACT|PCPL|LEM:HaAmiyap|ROOT:Hmy|F|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"101:11:2:1\",\"qac_word_ref\":\"101:11:2\",\"root_ar\":\"ح م ي\",\"surface_ar\":\"حَامِيَةٌۢ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:11:1","source_type":"word_analysis","support_id":"sup_db22298a681fa792d558","text":"{\"gloss_range\":\"an indefinite nominative concrete fire noun, locally functioning as the compressed answer to the previous question\",\"prose\":\"{{ar:نَارٌ}} ({{tr:nārun}}) begins the answer with a bare nominative noun: the previous question in 101:10 supplies the referent, while this ayah gives only the identifying content. The result is not a narrated event or a motion into punishment, but a compressed nominal identification, with no connector softening the move from question to answer. Its indefiniteness matters: the word says a fire, not a titled institution, so the answer is exact in grammar but unbounded in quality. The local branch is concrete burning fire, yet the {{ar:ن و ر}} ({{tr:n-w-r}}) family keeps the answer from feeling like inert matter; it is consuming radiance, made material by the following {{ar:حَامِيَةٌۢ}} ({{tr:ḥāmiyah}}). The phrase {{ar:نَارٌ حَامِيَةٌۢ}} ({{tr:nārun ḥāmiyah}}) also stands against the verbal, accusative fire-heat wording of 88:4 and the heated-punishment field of 9:35, so the same association is recast here as final nominal identity. In sound, the breathy close of 101:10 gives way to the resonant opening of the fire noun, and the short noun then hands the listener into the heavier adjective, making the two-word answer land as one sealed predicate.\",\"root_display\":\"{{ar:ن و ر}} ({{tr:n-w-r}})\",\"root_gloss_range\":\"broad root range of light, illumination, fire, visible markers, recoil, and other branches; locally narrowed to burning fire while retaining the fire-light family pressure\",\"surface_display\":\"{{ar:نَارٌ}} ({{tr:nārun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:11:2:final-closure-cadence","source_type":"word_analysis","support_id":"sup_e5e45e6ceafbd2eb1170","text":"{\"blocking_evidence\":null,\"headline\":\"final heat as closure landing\",\"reader_payoff\":\"The reader hears the surah end not merely with fire named, but with heat carrying the final acoustic and conceptual weight.\",\"reason\":\"The word is the final member of the two-word construction and the final word of the surah; the grammar and attachment evidence make that final word the completing qualifier.\",\"representative_source_ids\":[\"QT-adc7a75a\",\"QP-10e15549\",\"QP-289dcd14\",\"QY-a8bde9a1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":["root_000358/B001"],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:11:2:boundary-shift-to-impersonal-heat","source_type":"word_analysis","support_id":"sup_f1f4b7e2df1eb4727ae6","text":"{\"blocking_evidence\":null,\"headline\":\"question boundary becomes impersonal heat\",\"reader_payoff\":\"The reader notices the movement from addressed knowing and abyss imagery into an impersonal heat descriptor at the close.\",\"reason\":\"The previous question in 101:10 and the abyss term in 101:9 provide the boundary setting, while the local final adjective supplies impersonal heat as the answer's closure.\",\"representative_source_ids\":[\"QB-a0dea108\",\"QB-d7bc86b1\",\"QE-4e6086d9\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"نَارٌ حَامِيَةٌۢ","ayah_ref":"101:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000358/B001","root_001564/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001564","role":"Burning, flickering fire supplies the material carrier and its capacity to leave a mark.","root":"ن و ر","source_ref":"101:11","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000358","role":"Intense heating, including furnace-like heating, makes the adjective an active intensifier of the fire.","root":"ح م ي","source_ref":"101:11","source_word_indices":["2"]}],"changed_reading":{"after":"A fire defined by heat in active intensification, as though combustion and heating are one continuing operation.","before":"An unspecified fire with a routine temperature adjective."},"confidence":"strong","focus_anchor":"The fire noun at word 1 is directly qualified by the feminine adjective at word 2.","mechanism":"Active combustion and intensified heating form a compact process: the referent is not merely named as fire but specified by heat at full operation.","model_id":"base_combustive_intensity"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_combustive_intensity","source_type":"hft","support_id":"sup_8c2f90e06aa06a751714","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"نَارٌ حَامِيَةٌۢ","ayah_ref":"101:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000358/B001","root_001564/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001564","role":"Illumination supplies outward disclosure, so the fire functions as an exposing light as well as fuel.","root":"ن و ر","source_ref":"101:11","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000358","role":"Escalating heat prevents the luminous reading from becoming merely visual and gives disclosure material force.","root":"ح م ي","source_ref":"101:11","source_word_indices":["2"]}],"changed_reading":{"after":"The fire exposes and burns together: visibility itself arrives with thermal consequence.","before":"The fire primarily burns."},"confidence":"medium","focus_anchor":"Word 1 belongs to a root inventory that carries both fire and illumination, while word 2 supplies forceful heat.","mechanism":"Light and heat coexist as two effects of one fire: it makes what it reaches perceptible while also materially affecting it.","model_id":"base_luminous_exposure"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_luminous_exposure","source_type":"hft","support_id":"sup_1cbc60c875be9c5e4f1e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"نَارٌ حَامِيَةٌۢ","ayah_ref":"101:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000358/B002","root_001564/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001564","role":"The burning fire supplies the dangerous material zone whose edge can be enforced.","root":"ن و ر","source_ref":"101:11","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000358","role":"Warding, keeping away, and protected enclosure turn heat into the zone's self-enforcing boundary.","root":"ح م ي","source_ref":"101:11","source_word_indices":["2"]}],"changed_reading":{"after":"Heat is also what closes the fire around its occupant and bars any safe crossing of its boundary.","before":"Heat is only a property measured inside the fire."},"confidence":"medium","focus_anchor":"The adjective at word 2 can activate both heat and the root's warding or prohibited-preserve image.","mechanism":"The heat functions spatially as a boundary. Its intensity does not merely describe conditions inside the fire; it actively prevents approach or escape across its edge.","model_id":"base_exclusionary_zone"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_exclusionary_zone","source_type":"hft","support_id":"sup_0c97f3d4cf7e81ec7639","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"نَارٌ حَامِيَةٌۢ","ayah_ref":"101:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000358/B007","root_000358/B008","root_001564/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001564","role":"Flickering combustion supplies the moving medium through which the attack is carried.","root":"ن و ر","source_ref":"101:11","source_word_indices":["1"]},{"branch_id":"B007","mapped_root_id":"root_000358","role":"The burning force of a sting or poison makes the heat invasive rather than merely surrounding.","root":"ح م ي","source_ref":"101:11","source_word_indices":["2"]},{"branch_id":"B008","mapped_root_id":"root_000358","role":"A spreading rush of sharp intensity gives the invasive heat temporal momentum.","root":"ح م ي","source_ref":"101:11","source_word_indices":["2"]}],"changed_reading":{"after":"A fire whose heat repeatedly arrives as a penetrating sting and accelerating surge.","before":"A uniformly hot environment."},"confidence":"exploratory","focus_anchor":"The adjective at word 2 retains root branches of burning poison and sharply advancing intensity.","mechanism":"Heat can be modeled as an attacking dose rather than an ambient condition: it stings, enters, and surges through what it reaches.","model_id":"base_stinging_surge"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_stinging_surge","source_type":"hft","support_id":"sup_31d221978bba061d14e8","trust":"legacy_unbound"}]}
</lane_packet_json>
