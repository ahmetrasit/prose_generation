# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **100:7**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s100-regular-20260911/s100/100_7/micro.discovery.json` and modify nothing
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
  "ayah_ref": "100:7",
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
{"analysis_context":{"analysis_id":"s100-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"100:7","host_surah":100,"lane_context_refs":[],"ordered_context_refs":["100:0","100:1","100:2","100:3","100:4","100:5","100:6","100:8","100:9","100:10","100:11","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Çekirdek, görerek ya da yerinde bulunarak hazır olmaktır; hukuki bildirim, yemin formülü ve bal anlamı dışarıda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000822/B001","candidate_links":[{"candidate_id":"cand_54cb9a8a1203d1d9b06b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَهِيد","morph_features":"STEM|POS:N|LEM:$ahiyd|ROOT:$hd|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"100:7:4:2","qac_word_ref":"100:7:4","surface_ar":"شَهِيدٌ"}],"gloss":"hazır bulunup görme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir olayın ya da yerin yanında hazır bulunma ve onu doğrudan görme çekirdeği vardır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsanların bulunduğu ya da toplandığı yer, bu hazır bulunma çekirdeğinin yer adı olarak uzantısıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hac törenlerinin yapıldığı yerler, bulunulan ibadet mahalleri olarak özel bir kullanımdır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Eşi yanında bulunan kadın kullanımı, hazır bulunma ilişkisinin aile içi duruma uygulanmasıdır."}}],"root_ar":"ش ه د","root_id":"root_000822","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çekirdek hazır bulunma ve doğrudan deneyim için uygundur; yer ve aile durumu uzantılarını tek başına anlatmaz.","boundary_detail":"Çekirdek, görerek ya da yerinde bulunarak hazır olmaktır; hukuki bildirim, yemin formülü ve bal anlamı dışarıda kalır.","concept_gloss":"hazır bulunup görme","contextual_glosses":[{"applicability":"Görme yönünün belirgin olmadığı hazır bulunma bağlamlarında çalışır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Doğrudan görme ve yerinde deneyim boyutunu açıkça söylemez.","preserves":"Hazır bulunma çekirdeğini korur."},"facet_ids":["F001"],"text":"orada bulunma","usage_role":"contextual"},{"applicability":"İnsanların bulunduğu veya bir araya geldiği yer anlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bulunma çekirdeğinin yer adı olarak uzantısını korur."},"facet_ids":["F002"],"text":"toplanma yeri","usage_role":"contextual"},{"applicability":"Yalnızca ibadet uygulamalarının yerine getirildiği belirli yerler için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bulunulan ibadet yerleri özel kullanımını korur."},"facet_ids":["F003"],"text":"hac töreni yeri","usage_role":"contextual"}],"definition":"Bir kişi ya da şeyin bir yerde hazır bulunması ve çoğu bağlamda olayı doğrudan görerek deneyimlemesidir. Bu çekirdekten, insanların bulunduğu yer, belli ibadet yerleri ve yanında eşi bulunan kadın gibi bağlı kullanımlar doğar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir olayın ya da yerin yanında hazır bulunma ve onu doğrudan görme çekirdeği vardır."},{"facet_id":"F002","role":"extension","statement":"İnsanların bulunduğu ya da toplandığı yer, bu hazır bulunma çekirdeğinin yer adı olarak uzantısıdır."},{"facet_id":"F003","role":"specialization","statement":"Hac törenlerinin yapıldığı yerler, bulunulan ibadet mahalleri olarak özel bir kullanımdır."},{"facet_id":"F004","role":"associated_use","statement":"Eşi yanında bulunan kadın kullanımı, hazır bulunma ilişkisinin aile içi duruma uygulanmasıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bilgiye dayalı sözlü bildirim ve hukuki tanık olma alanını ekler.","collision":"Bu söz B002 dalının ana karşılığıyla çakışır.","fit":"displacement","loses":"Yerinde hazır bulunma çekirdeğini geri plana iter.","preserves":"Görme ve olayla ilişkili olma çağrışımını kısmen korur."},"text":"tanıklık"}],"identity_rationale":"Kaynak ifadesi bu dalı hazır bulunma, bu hazır bulunuşa eşlik eden doğrudan görme ve bundan türeyen bulunma yeri kullanımlarıyla kuruyor. Eşin hazır olması ve ibadet yerleri gibi örnekler çekirdek anlamı genişletir; sözlü tanıklık veya bal anlamı bu dalın sınırına girmez.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"hazır bulunmak ve bizzat görmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"görerek hazır bulunma"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bizzat görme ve gözle karşılaşma"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"insanların bulunduğu veya toplandığı yer"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"hac törenlerinin yapıldığı yerler"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"eşi yanında bulunan kadın"}],"lexicalization_note":"Tanım çıplak hazır bulunma ve görme çekirdeğini verir; hac yeri ve eşi yanında olan kadın gibi kullanımlar yapıya bağlı özel yüzlerdir.","neighbor_coverage_note":"Adayların tamamı hazır bulunma, görme, sözlü tanıklık ya da aynı kökün uzak anlamları açısından değerlendirildi. Bal, doğum artığı ve gösterge dalları biçim ortaklığı dışında bu sınırı keskinleştirmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Okur iki dalı hazır bulunma yüzünden yakın görebilir; bu dal görerek hazır bulunma ve bundan doğan tanık yeri kullanımlarına bağlıyken komşu dal genel varış, yakınlık ve mahal alanında daha geniştir.","focus_only":"Bu dalda hazır bulunma çoğu kez doğrudan görme ve olay yanında bulunma ile bağlıdır.","gloss":"hazır bulunma","neighbor_only":"Komşu dal geliş, yakınlık, yanında olma ve mahal gibi daha geniş bulunma alanlarını kapsar.","neighbor_ref":"root_000333/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir kişinin ya da şeyin bir yerde mevcut olmasını anlatır."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği sadece görsel algı değildir; kişi olayda hazırdır. Komşu dal ise bakış ve gözle kesin görme tarafında yoğunlaşır.","focus_only":"Bu dalda görme, olayın yanında bulunma ve yerinde hazır olma çerçevesindedir.","gloss":"bizzat görme","neighbor_only":"Komşu dal doğrudan gözle görme ve kesin bakış bilgisini, hazır bulunma şartı olmadan öne çıkarır.","neighbor_ref":"root_001069/B002","relation_type":"near_neighbor","shared_zone":"İki dal da dolaysız deneyim ve gözle karşılaşma alanına değer."},{"boundary_match":"partial","distinction":"B001 olayın yanında bulunmayı ve görmeyi adlandırır; B002 bu bilgiyi sözlü bildirim veya kanıtlayıcı beyan olarak dışa vurur.","focus_only":"Bu dal yerinde bulunma ve doğrudan görmeyi anlatır.","gloss":"görerek hazır bulunma","neighbor_only":"B002 bilgiden çıkan kesin bildirimi ve tanık sıfatıyla beyanı anlatır.","neighbor_ref":"root_000822/B002","relation_type":"near_neighbor","shared_zone":"İki dal tanık olma senaryosunda buluşur."}],"source_summary":"Kaynaklar dalın merkezini hazır bulunma ve doğrudan görme etrafında ortaklaştırır. Aynı iddia, toplanma yeri, ibadet yerleri ve eşin yanında bulunması gibi kullanımları çekirdeğin bağlı uzantıları olarak verir."},"support_links":["sup_25e5057ab0e14e70f1ff"]},{"boundary":"Bu dal bilgiye dayalı beyan ve tanık konumudur; salt orada bulunma, yemin formülü ve bal anlamı dışarıda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000822/B002","candidate_links":[{"candidate_id":"cand_e5c6f79574c84f64b4cd","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَهِيد","morph_features":"STEM|POS:N|LEM:$ahiyd|ROOT:$hd|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"100:7:4:2","qac_word_ref":"100:7:4","surface_ar":"شَهِيدٌ"}],"gloss":"bilgiye dayalı tanıklık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Merkezde bilinen bir şeyi kesin haber veya açıklama olarak bildirme vardır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tanık olan kişi, bildiğini ortaya koyan ve hak konusunda söz söyleyen kimsedir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birini tanıklığa çağırma veya bir konuda tanık kılma, çekirdeğin toplumsal ve hukuki işlem yüzüdür."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kapsamlı bilgi ya da güvenilir bildirme niteliği, tanık olma fikrinin nitelik adı olarak uzantısıdır."}}],"root_ar":"ش ه د","root_id":"root_000822","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bilinen şeyi kesin beyan olarak sunma ve tanık konumu için en uygun kısa karşılıktır.","boundary_detail":"Bu dal bilgiye dayalı beyan ve tanık konumudur; salt orada bulunma, yemin formülü ve bal anlamı dışarıda kalır.","concept_gloss":"bilgiye dayalı tanıklık","contextual_glosses":[{"applicability":"Bir kişinin bildiğini beyan ettiği olağan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilgiye dayalı beyan ve tanık sıfatıyla söyleme çekirdeğini korur."},"facet_ids":["F001","F002"],"text":"tanıklık etmek","usage_role":"general"},{"applicability":"Birini tanıklığa çağırma veya bir konuda tanık kılma yapılarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tanıklığa çağırma ve tanık kılma işlem yüzünü korur."},"facet_ids":["F003"],"text":"tanık göstermek","usage_role":"contextual"},{"applicability":"Kapsamlı bilgi ve güvenilir tanıklık niteliği anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilgisinden hiçbir şeyin uzak kalmadığı güvenilir tanık niteliğini korur."},"facet_ids":["F004"],"text":"her şeyi bilen tanık","usage_role":"explanatory"}],"definition":"Bilgiye dayanarak kesin bir haber ya da açıklama vermek ve bu nedenle bir kişi veya şey için tanık konumunda olmaktır. Yapı, tanık isteme, tanık kılma ve kapsamlı bilgiyle niteleme gibi bağlı kullanımlara açılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Merkezde bilinen bir şeyi kesin haber veya açıklama olarak bildirme vardır."},{"facet_id":"F002","role":"specialization","statement":"Tanık olan kişi, bildiğini ortaya koyan ve hak konusunda söz söyleyen kimsedir."},{"facet_id":"F003","role":"associated_use","statement":"Birini tanıklığa çağırma veya bir konuda tanık kılma, çekirdeğin toplumsal ve hukuki işlem yüzüdür."},{"facet_id":"F004","role":"extension","statement":"Kapsamlı bilgi ya da güvenilir bildirme niteliği, tanık olma fikrinin nitelik adı olarak uzantısıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Bu karşılık B001 dalının çekirdeğiyle çakışır.","fit":"narrowing","loses":"Bilgiye dayalı kesin beyanı ve tanık sıfatıyla açıklamayı kaybeder.","preserves":"Tanıklığın görmeye ve hazır olmaya dayanabilen tarafını korur."},"text":"hazır bulunma"}],"identity_rationale":"Kaynak ifadesi bu dalı hazır bulunuş ve bilgiden doğan kesin haber, bildirme ve tanık sıfatıyla söyleme alanında kuruyor. Dal, salt fiziksel hazır bulunmadan ayrılır; esas olan bilinen şeyi beyan etmek veya bir kimsenin tanık konumunda olmasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bilgiye dayalı kesin tanıklık sözü"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bildiğini tanık olarak açıklamak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"tanıklık eden kişi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"tanık olan veya başkası hakkında tanıklık eden kişi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"birinden tanıklık etmesini istemek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"birini bir konuda tanık kılmak"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ilahi nitelik olarak güvenilir tanık veya bilgisine hiçbir şey uzak kalmayan"}],"lexicalization_note":"Tanım bilgiye dayalı beyan çekirdeğini verir; birini tanık isteme, tanık kılma ve ilahi nitelik gibi kullanımlar ayrı bağlı yüzlerdir.","neighbor_coverage_note":"Adayların tamamı bilgi, kanıt, saklama, hazır bulunma ve aynı kökün uzak dalları bakımından incelendi. Bal, doğum ve ibadet formülü dalları yalnızca biçim ortaklığı taşıdığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B002 bilgiyi kesin tanıklık sözüne dönüştürür; komşu dalda bilgi sahibi olma, haber alma veya iç yüzü bilme ön plandadır.","focus_only":"Bu dal bilinen şeyi tanık sıfatıyla dışa vuran beyanı içerir.","gloss":"bilerek haber verme","neighbor_only":"Komşu dal haber, iç bilgi ve deneyimle tanıma alanında kalabilir; tanıklık işlemini gerektirmez.","neighbor_ref":"root_000387/B001","relation_type":"near_neighbor","shared_zone":"İki dal bilgi ve haber alanında kesişir."},{"boundary_match":"partial","distinction":"B002 tanığın bildiğini söylemesine odaklanır; komşu dal ise kanıtın kendisi ve hükümle sabit kılma sürecidir.","focus_only":"Bu dal tanık sözünü ve tanık konumunu anlatır.","gloss":"tanıklıkla bildirme","neighbor_only":"Komşu dal delil, ispat ve hükümle sabitleme alanını daha doğrudan anlatır.","neighbor_ref":"root_000192/B006","relation_type":"near_neighbor","shared_zone":"İki dal hakikatin ortaya konması ve kanıtlanması alanında buluşur."},{"boundary_match":"opposed","distinction":"B002 tanıklığı açığa çıkarma yönüdür; komşu dal aynı tür bilginin gizlenmesi veya tutulması yönünü temsil eder.","focus_only":"Bu dal bilinen şeyi açıklayıp tanıklık etmeyi gerektirir.","gloss":"açıklama ve saklama","neighbor_only":"Komşu dal söz, hak veya tanıklık gibi bilinen şeyi saklamayı anlatır.","neighbor_ref":"root_001284/B001","relation_type":"polarity_pair","shared_zone":"İki dal bilginin dışa vurulup vurulmaması ekseninde karşılaşır."},{"boundary_match":"partial","distinction":"B001 bilginin doğabileceği hazır bulunma durumudur; B002 bu bilginin kesin söz olarak iletilmesidir.","focus_only":"Bu dal bilgiyi beyan etme ve tanık konumuna geçme tarafındadır.","gloss":"tanıklık beyanı","neighbor_only":"B001 olayın yanında bulunma ve doğrudan görme tarafındadır.","neighbor_ref":"root_000822/B001","relation_type":"near_neighbor","shared_zone":"İki dal bir tanık senaryosunun deneyim ve beyan aşamalarını paylaşır."}],"source_summary":"Kaynaklar tanıklığı hazır oluş, bilgi ve bildirme ekseninde ortaklaştırır. Kesin haber verme, bildiğini ortaya koyma, hak lehine veya aleyhine tanık sıfatı taşıma aynı dal içinde toplanır."},"support_links":["sup_ae566337038aa36c8eb4"]},{"boundary":"Bu dal formül ve namazdaki okuma içindir; genel hazır bulunma ve mahkemede tanıklık etme çekirdeği değildir.","branch_kind":"bare","branch_ref":"root_000822/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَهِيد","morph_features":"STEM|POS:N|LEM:$ahiyd|ROOT:$hd|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"100:7:4:2","qac_word_ref":"100:7:4","surface_ar":"شَهِيدٌ"}],"gloss":"tanıklık bildirme sözü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tanıklık bildiren söz kalıbı, yemin etme veya bildiğini açıklama göreviyle kullanılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Namazdaki belirli okuma bölümü, bu söz kalıbından doğan ibadet içi kullanımdır."}}],"root_ar":"ش ه د","root_id":"root_000822","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yemin, açıklama ve namaz okumasını birleştiren söz kalıbı için uygundur.","boundary_detail":"Bu dal formül ve namazdaki okuma içindir; genel hazır bulunma ve mahkemede tanıklık etme çekirdeği değildir.","concept_gloss":"tanıklık bildirme sözü","contextual_glosses":[{"applicability":"Söz kalıbının yemin işlevi gördüğü kullanımlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Açıklama ve namazdaki okuma bölümünü kapsamaz.","preserves":"Kalıbın yemin işlevini korur."},"facet_ids":["F001"],"text":"yemin etmek","usage_role":"contextual"},{"applicability":"İbadet içindeki özel okuma bölümünü anlatırken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Namazdaki tanıklık sözlerine dayalı özel okumayı korur."},"facet_ids":["F002"],"text":"namazdaki tanıklık bölümünü okumak","usage_role":"contextual"}],"definition":"Tanıklık bildiren söz kalıbının yemin, açıklama veya ibadet okuması olarak kullanılmasıdır. Namazdaki belirli okuma bölümü bu kalıptan türemiş özel bir uygulamadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tanıklık bildiren söz kalıbı, yemin etme veya bildiğini açıklama göreviyle kullanılır."},{"facet_id":"F002","role":"specialization","statement":"Namazdaki belirli okuma bölümü, bu söz kalıbından doğan ibadet içi kullanımdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Mahkeme veya resmi beyan alanını ekler.","collision":"Bu karşılık B002 dalına kayar.","fit":"displacement","loses":"Söz kalıbı ve namazdaki okuma sınırını kaybeder.","preserves":"Tanıklık sözünün bilgiyle ilişkisini korur."},"text":"hukuki tanıklık"}],"identity_rationale":"Kaynak ifadesi bu dalı belirli bir tanıklık söylemi formülüne ve namazdaki okuma bölümüne bağlıyor. Bu nedenle anlam salt yemin ya da salt hukuki tanıklık değil, belli söz kalıbının bildirme, yemin ve ibadet içindeki kullanımıdır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"tanıklık sözüyle yemin etmek veya bildirmek"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"namazda okunan tanıklık ve selamlama bölümü"}],"lexicalization_note":"Mekanik profil dalı çıplak sayar; tanım yine kaynak ifadesindeki söz formülü ve namaz okuması sınırını korur.","neighbor_coverage_note":"Adaylar yemin kalıpları, dua sözleri, ibadet alanı ve aynı kökün yakın dalları bakımından değerlendirildi. Hazır bulunma, bal ve doğum dalları bu formül sınırını açıklamadığı için dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B003 sadece genel yemin değildir; tanıklık bildiren özel formül ve namazdaki okuma bölümü dalın sınırını belirler.","focus_only":"Bu dal belli bir tanıklık söz kalıbını ve onun ibadet içi türevini kapsar.","gloss":"yemin formülü","neighbor_only":"Komşu dal genel yemin, ant ve yemin ettirme alanıdır.","neighbor_ref":"root_000349/B001","relation_type":"near_neighbor","shared_zone":"İki dal yemin sözünün kullanıldığı bağlamda kesişir."},{"boundary_match":"field_only","distinction":"Her iki aday kalıplaşmış yemin alanında dursa da kullanılan ifade ve bunun ibadetle bağı farklıdır.","focus_only":"Bu dal tanıklık bildiren söz kalıbına dayanır.","gloss":"kalıpla yemin","neighbor_only":"Komşu dal ömür sözüyle yapılan yemin veya rica kalıbına dayanır.","neighbor_ref":"root_001044/B002","relation_type":"same_field","shared_zone":"İki dal belirli söz kalıplarının yemin işlevi kazanması alanındadır."},{"boundary_match":"partial","distinction":"B003 ifade kalıbı ve ibadet okumasıdır; B002 kalıptan bağımsız olarak bilinen şeyin tanıkça bildirilmesidir.","focus_only":"Bu dal tanıklık bildiren sözün formül olarak söylenmesine odaklanır.","gloss":"tanıklık sözü","neighbor_only":"B002 bilgiye dayalı kesin beyan ve tanık konumudur.","neighbor_ref":"root_000822/B002","relation_type":"near_neighbor","shared_zone":"İki dal tanıklık bildiren söz etrafında kesişir."}],"source_summary":"Kaynaklar dalı tanıklık bildiren söz kalıbı ile namazdaki okuma arasında kurar. Aynı iddia, kalıbın yemin değeri taşıyabildiğini ve açıklama anlamında da kullanılabildiğini bildirir."},"support_links":[]},{"boundary":"Dal ölümle ve özel kişi adıyla sınırlıdır; tanık beyanı veren kişi veya petekli bal anlamı değildir.","branch_kind":"bare","branch_ref":"root_000822/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَهِيد","morph_features":"STEM|POS:N|LEM:$ahiyd|ROOT:$hd|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"100:7:4:2","qac_word_ref":"100:7:4","surface_ar":"شَهِيدٌ"}],"gloss":"Tanrı yolunda öldürülen kişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Merkezde Tanrı yolunda öldürülen kişi için kullanılan özel adlandırma vardır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ölüm anında bulunan kişi açıklaması, ölüm sahnesiyle bağlantılı bir uzantıdır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Diri sayılma açıklaması, aynı özel kişi adının kaynak içi yorum yüzüdür."}}],"root_ar":"ش ه د","root_id":"root_000822","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın ana kişi adını en açık biçimde verir; ölüm anı ve diri sayılma açıklamaları bağlı yorumlardır.","boundary_detail":"Dal ölümle ve özel kişi adıyla sınırlıdır; tanık beyanı veren kişi veya petekli bal anlamı değildir.","concept_gloss":"Tanrı yolunda öldürülen kişi","contextual_glosses":[{"applicability":"Dini veya kutsal amaç uğrunda ölme bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tanrı yolu ifadesini ve kaynaklardaki ölüm anı yorumunu açıkça söylemez.","preserves":"Özel ölüm statüsünü ve kişi adını korur."},"facet_ids":["F001"],"text":"bu uğurda ölen kişi","usage_role":"contextual"},{"applicability":"Kaynaklarda ölüm anında bulunma açıklamasının öne çıktığı yerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölüm anı uzantısını korur."},"facet_ids":["F002"],"text":"ölüm anındaki kişi","usage_role":"explanatory"}],"definition":"Tanrı yolunda öldürülen ya da bu statüyle anılan kişidir; kaynaklarda ölüm anında bulunan kişi ve diri sayılan kişi açıklaması da aynı özel adlandırmaya bağlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Merkezde Tanrı yolunda öldürülen kişi için kullanılan özel adlandırma vardır."},{"facet_id":"F002","role":"extension","statement":"Ölüm anında bulunan kişi açıklaması, ölüm sahnesiyle bağlantılı bir uzantıdır."},{"facet_id":"F003","role":"source_variant","statement":"Diri sayılma açıklaması, aynı özel kişi adının kaynak içi yorum yüzüdür."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Sözlü beyan veren kişi anlamını ekler.","collision":"Bu karşılık B002 dalıyla çakışır.","fit":"displacement","loses":"Ölüm, kutsal uğur ve özel kişi adı sınırını kaybeder.","preserves":"Aynı kökteki tanık kişi çağrışımını korur."},"text":"tanık"}],"identity_rationale":"Kaynak ifadesi bu dalı Tanrı yolunda öldürülen kişi, böyle ölen kişi ve ölüm anında bulunan kişi çevresinde topluyor. Bu, haber veren tanık anlamından ayrı, ölüm ve özel saygınlık taşıyan kişi adı olarak sözlükleşmiş bir daldır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"Tanrı yolunda öldürülen veya ölüm anında bulunan kişi"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bu özel ölüm statüsüyle ölmek"}],"lexicalization_note":"Mekanik profil çıplak daldır; tanım sözlükleşmiş kişi adını verir ve bunu sözlü tanıklık anlamına yaymaz.","neighbor_coverage_note":"Dış adayların çoğu yol, mesafe ve seyahat alanında olduğundan bu dalın ölüm temelli kişi adını açıklamadı. İç adaylardan yalnızca tanık rolü ve hazır bulunma yorumu anlam sınırını belirginleştirdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B004 ölümle tanımlanan kişi adıdır; B002 ise bilgiyi açıklayan tanık rolüdür.","focus_only":"Bu dal özel ölüm statüsüyle anılan kişiyi anlatır.","gloss":"özel ölüm kişisi","neighbor_only":"B002 bilgiye dayalı beyan veren tanığı anlatır.","neighbor_ref":"root_000822/B002","relation_type":"near_neighbor","shared_zone":"İki dal kişi adı olarak aynı biçim alanında karşılaşabilir."},{"boundary_match":"thematic_only","distinction":"Bu bağ dal çekirdeği değildir; B004 kişinin özel ölüm adı, B001 ise genel hazır bulunma ve görme dalıdır.","focus_only":"Bu dal ölüm statüsünü ve özel kişi adını taşır.","gloss":"ölümde hazır bulunma","neighbor_only":"B001 hazır bulunma ve doğrudan görmeyi taşır.","neighbor_ref":"root_000822/B001","relation_type":"thematic","shared_zone":"Kaynak açıklamasındaki ölüm anında bulunma yorumu, hazır bulunma fikrine zayıf bir bağ kurar."}],"source_summary":"Kaynaklar özel adlandırmayı Tanrı yolunda öldürülme ve bu şekilde ölme etrafında toplar. Aynı iddia, ölüm anında bulunma ve diri sayılma açıklamalarını dalın bağlı yorumları olarak taşır."},"support_links":[]},{"boundary":"Dal dil ve ifade açıklığı içindir; tanıklık beyanı, yıldız göstergesi ve petekli bal anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000822/B005","candidate_links":[{"candidate_id":"cand_86ec624cf53dcb38a7b0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَهِيد","morph_features":"STEM|POS:N|LEM:$ahiyd|ROOT:$hd|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"100:7:4:2","qac_word_ref":"100:7:4","surface_ar":"شَهِيدٌ"}],"gloss":"ifade eden dil","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dil, konuşma ve sahibini belli eden ifade dalın çekirdeğidir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Görünüşü ve dili olmama sözü, kişinin kendini gösteren dış ve sözlü niteliğinin yokluğunu anlatır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Güzel ifade kullanımı, dilin sahibini olumlu biçimde ortaya koyan anlatım niteliğine uzanır."}}],"root_ar":"ش ه د","root_id":"root_000822","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dil organı ve sahibini ortaya koyan sözlü ifade için uygundur.","boundary_detail":"Dal dil ve ifade açıklığı içindir; tanıklık beyanı, yıldız göstergesi ve petekli bal anlamı değildir.","concept_gloss":"ifade eden dil","contextual_glosses":[{"applicability":"Organ veya konuşma yetisi anlamı öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sahibini ortaya koyan ifade niteliğini açıkça belirtmez.","preserves":"Dil ve konuşma çekirdeğini korur."},"facet_ids":["F001"],"text":"dil","usage_role":"general"},{"applicability":"Kişinin sözünün güzel ve açıklayıcı oluşunu anlatan kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Olumlu anlatım niteliği uzantısını korur."},"facet_ids":["F003"],"text":"güzel ifade","usage_role":"contextual"}],"definition":"Kişinin dilini veya onu görünür kılan sözlü ifadesini anlatır. Güzel anlatım ya da birinde görünüş ve dil bulunmaması gibi kullanımlar, ifadenin sahibini ortaya koyma işlevine bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dil, konuşma ve sahibini belli eden ifade dalın çekirdeğidir."},{"facet_id":"F002","role":"example","statement":"Görünüşü ve dili olmama sözü, kişinin kendini gösteren dış ve sözlü niteliğinin yokluğunu anlatır."},{"facet_id":"F003","role":"extension","statement":"Güzel ifade kullanımı, dilin sahibini olumlu biçimde ortaya koyan anlatım niteliğine uzanır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kişinin bilgi beyan eden tanık olması anlamını ekler.","collision":"Bu karşılık B002 dalına kayar.","fit":"displacement","loses":"Dil ve ifade organı anlamını kaybeder.","preserves":"Bir şeyi belli etme çağrışımını kısmen korur."},"text":"tanık"}],"identity_rationale":"Kaynak ifadesi bu dalı dil organı ve sahibini ortaya koyan ifade olarak verir. Bu, mahkemede tanık olan kişi değil, konuşma ve açık ifade yoluyla bir kimsenin durumunu belli eden dildir.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"dil veya sahibini belli eden ifade"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"ne görünüşü ne de dili var"}],"lexicalization_note":"Tanım dil ve ifade çekirdeğini verir; görünüş ve dil yokluğu ile güzel ifade gibi kullanımlar kalıba bağlıdır.","neighbor_coverage_note":"Adaylar dil, konuşma açıklığı, kapalı söz, işaret ve aynı kökün tanıklık dalları bakımından incelendi. Yalnızca dil ve ifade sınırını keskinleştiren ilişkiler yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B005 dilin kişiyi temsil eden ifade yüzünü öne çıkarır; komşu dal ayrıntılandıran ve açıklayan konuşma gücünü daha doğrudan anlatır.","focus_only":"Bu dal dilin sahibini belli eden ifade değeri üzerinde durur.","gloss":"açıklayan dil","neighbor_only":"Komşu dal dili, işleri ayıran ve açıklayan konuşma gücü olarak verir.","neighbor_ref":"root_001159/B004","relation_type":"near_synonym","shared_zone":"İki dal dilin açık ifade ve ayırt ettirme işlevinde buluşur."},{"boundary_match":"field_only","distinction":"B005 bir kişide dil veya ifade bulunup bulunmamasını anlatabilir; komşu dal özellikle konuşmanın fasih ve açık oluşudur.","focus_only":"Bu dal dilin sahibini gösteren ifade olmasına odaklanır.","gloss":"dil ve konuşma","neighbor_only":"Komşu dal akıcı, açık ve doğru konuşma niteliğine odaklanır.","neighbor_ref":"root_001158/B002","relation_type":"same_field","shared_zone":"İki dal dil, konuşma ve açıklık alanını paylaşır."},{"boundary_match":"opposed","distinction":"B005 ifade ederek belli etme yönüdür; komşu dal ise sözün bulanıklaşıp açıklık kazanmaması yönüdür.","focus_only":"Bu dal açıklayan dil ve ifade niteliğini taşır.","gloss":"açık ve kapalı söz","neighbor_only":"Komşu dal sözün anlaşılmaz kalmasını ve açıklanmamasını anlatır.","neighbor_ref":"root_000261/B008","relation_type":"polarity_pair","shared_zone":"İki dal sözün anlaşılır olup olmaması ekseninde karşılaşır."},{"boundary_match":"partial","distinction":"B005 göstergenin sözlü ifade veya dil oluşudur; B008 sözsüz işaret ve belirti alanına geçer.","focus_only":"Bu dal dili ve sözlü ifadeyi gösterici unsur sayar.","gloss":"gösteren ifade","neighbor_only":"B008 yıldız, namaz vakti veya at koşusu gibi sözsüz göstergeleri anlatır.","neighbor_ref":"root_000822/B008","relation_type":"near_neighbor","shared_zone":"İki dal bir şeyin başka bir durumu göstermesi fikrinde buluşur."}],"source_summary":"Kaynaklar dalı dil ve ifade anlamında ortaklaştırır. Aynı iddia, görünüş ve dil yokluğu ile güzel ifade örneklerini, kişinin dışa vuran niteliğini anlatan bağlı kullanımlar olarak verir."},"support_links":["sup_290a4a96d70f18eb2229"]},{"boundary":"Bu dal doğum ve erginlik belirtileridir; hazır bulunma, sözlü tanıklık ve petekli bal anlamı dışarıda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000822/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَهِيد","morph_features":"STEM|POS:N|LEM:$ahiyd|ROOT:$hd|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"100:7:4:2","qac_word_ref":"100:7:4","surface_ar":"شَهِيدٌ"}],"gloss":"doğum ve erginlik belirtisi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Doğum veya erginlik sırasında beliren bedensel madde, akıntı ya da iz dalın çekirdeğidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Çocukla ya da çocuğun başıyla birlikte çıkan şey doğum bağlamındaki özel kullanımdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Devenin doğurduğu yerdeki kan veya zar izi hayvan doğumu bağlamındaki özel kullanımdır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Erkek çocuğun salgı çıkarması ve kız çocuğun adet görmesi erginlik belirtisi olarak uzantıdır."}}],"root_ar":"ش ه د","root_id":"root_000822","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Doğumla çıkan madde, doğum izi ve erginliğe erişme belirtilerini birlikte anlatır.","boundary_detail":"Bu dal doğum ve erginlik belirtileridir; hazır bulunma, sözlü tanıklık ve petekli bal anlamı dışarıda kalır.","concept_gloss":"doğum ve erginlik belirtisi","contextual_glosses":[{"applicability":"Çocukla veya başıyla birlikte çıkan madde bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Deve doğumu izi ve erginlik belirtisi kullanımlarını kapsamaz.","preserves":"Doğumla birlikte çıkan madde yüzünü korur."},"facet_ids":["F002"],"text":"doğumla çıkan zar","usage_role":"contextual"},{"applicability":"Devenin doğurduğu yerde kalan kan veya zar izi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvan doğumu yerinde kalan kan veya zar izini korur."},"facet_ids":["F003"],"text":"doğum izi","usage_role":"contextual"},{"applicability":"Bedensel akıntı veya adet görme ile olgunlaşma bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Erginlik belirtisi olan bedensel değişimi korur."},"facet_ids":["F004"],"text":"ergenliğe ermek","usage_role":"contextual"}],"definition":"Doğumla birlikte görülen zar, akıntı veya iz ile erginliği gösteren bedensel çıkıştır. Çocukla çıkan madde, devenin doğurduğu yerde kalan kan veya zar ve ergenliğe erişme belirtileri aynı dalda toplanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Doğum veya erginlik sırasında beliren bedensel madde, akıntı ya da iz dalın çekirdeğidir."},{"facet_id":"F002","role":"specialization","statement":"Çocukla ya da çocuğun başıyla birlikte çıkan şey doğum bağlamındaki özel kullanımdır."},{"facet_id":"F003","role":"specialization","statement":"Devenin doğurduğu yerdeki kan veya zar izi hayvan doğumu bağlamındaki özel kullanımdır."},{"facet_id":"F004","role":"extension","statement":"Erkek çocuğun salgı çıkarması ve kız çocuğun adet görmesi erginlik belirtisi olarak uzantıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bilgiye dayalı sözlü beyan alanını ekler.","collision":"Bu karşılık B002 dalına kayar.","fit":"displacement","loses":"Doğum maddesi, doğum izi ve erginlik belirtisi alanını kaybeder.","preserves":"Bir durumun belirtiyle anlaşılması çağrışımını ancak dolaylı korur."},"text":"tanıklık"}],"identity_rationale":"Kaynak ifadesi doğum sırasında çocukla birlikte çıkan maddeyi, devenin doğum yerinde kalan kan veya zar izlerini ve erginlikte görülen bedensel akıntı ya da adet halini birlikte verir. Dalın ortak noktası tanıklık değil, doğum veya bedensel olgunlaşmayı gösteren çıkış ve izdir.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"doğumda çocuğun başıyla ya da çocukla birlikte çıkan şey"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"devenin doğurduğu yerde kalan kan veya zar izi"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"erkek çocuğun salgıyla, kız çocuğun adetle erginleşmesi"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"meni öncesi salgı çıkarmak"}],"lexicalization_note":"Tanım çıkış ve bedensel belirti çekirdeğini korur; çocuk, deve doğumu ve erginlik kullanımları ayrı bağlı bağlamlardır.","neighbor_coverage_note":"Adaylar doğum zarı, doğum artığı, adet, göbek ve kan akışı alanları bakımından değerlendirildi. Hazır bulunma, beyan ve bal dalları yalnızca biçim ortaklığı taşıdığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B006 daha geniştir; doğumla çıkan şeyi, hayvan doğum izini ve erginlik belirtisini birlikte taşır. Komşu dal ise doğum zarına yakın özel maddedir.","focus_only":"Bu dal doğum maddesinin yanında deve doğumu izlerini ve erginlik belirtilerini de kapsar.","gloss":"doğumla çıkan zar","neighbor_only":"Komşu dal doğumla çıkan zar, su veya benzeri örtüye daha dar biçimde odaklanır.","neighbor_ref":"root_000373/B008","relation_type":"near_synonym","shared_zone":"İki dal çocukla birlikte çıkan doğum maddesi alanında örtüşür."},{"boundary_match":"partial","distinction":"B006 olayın kendisini gösteren çıkış ya da izdir; komşu dal daha çok birikmiş artık madde ve yara kirine yönelir.","focus_only":"Bu dal doğum ve erginlik olaylarında çıkan veya kalan belirtiyi anlatır.","gloss":"doğum sonrası madde","neighbor_only":"Komşu dal yara veya doğum sonrası biriken irin, zar ve kir gibi birikintilere odaklanır.","neighbor_ref":"root_000333/B008","relation_type":"near_neighbor","shared_zone":"İki dal doğumla ilişkili zar, artık veya bedensel madde alanında kesişir."},{"boundary_match":"partial","distinction":"B006 adet görmeyi erginlik göstergelerinden biri olarak verir; komşu dalın ana anlamı doğrudan adet kanamasıdır.","focus_only":"Bu dal adet görmeyi erginlik belirtisi olarak yalnızca bir yüzünde kullanır.","gloss":"adetle erginleşme","neighbor_only":"Komşu dal adet kanaması ve onun zaman, yer ve durum adlarını ana çekirdek yapar.","neighbor_ref":"root_000379/B001","relation_type":"near_neighbor","shared_zone":"İki dal kız çocuğunda adet görme olayında kesişir."},{"boundary_match":"field_only","distinction":"B006 zar, akıntı, kan izi ve erginlik belirtisiyle ilgilidir; komşu dal göbek bağı ve göbek yerinde kalır.","focus_only":"Bu dal doğumla çıkan madde veya doğum yerinde kalan izi anlatır.","gloss":"doğum bedeni artığı","neighbor_only":"Komşu dal göbek ve doğumdan sonra kesilen göbek parçasını anlatır.","neighbor_ref":"root_000697/B006","relation_type":"same_field","shared_zone":"İki dal doğumla ilişkili bedensel parçalar ve artıklar alanındadır."}],"source_summary":"Kaynaklar doğumla çıkan şey, doğum yerinde kalan iz ve erginlik belirtisi olan bedensel çıkışları aynı dal içinde toplar. Ortak içerik, bir beden olayının dışa çıkan madde veya görünür belirtiyle anlaşılmasıdır."},"support_links":[]},{"boundary":"Dal petek içinde süzülmemiş baldır; tanıklık, hazır bulunma ve doğum artığı anlamları dışarıda kalır.","branch_kind":"bare","branch_ref":"root_000822/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَهِيد","morph_features":"STEM|POS:N|LEM:$ahiyd|ROOT:$hd|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"100:7:4:2","qac_word_ref":"100:7:4","surface_ar":"شَهِيدٌ"}],"gloss":"petekli bal","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Balmumu peteği içinde bulunan ve henüz süzülmemiş bal dalın çekirdeğidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tek parça adı, petekli balın bir birimini gösterir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çoğul ad, aynı petekli bal parçalarının toplu biçimini anlatır."}}],"root_ar":"ش ه د","root_id":"root_000822","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Balmumu içinde duran, süzülmemiş bal için en doğal kısa karşılıktır.","boundary_detail":"Dal petek içinde süzülmemiş baldır; tanıklık, hazır bulunma ve doğum artığı anlamları dışarıda kalır.","concept_gloss":"petekli bal","contextual_glosses":[{"applicability":"Balın henüz petekten ayrılmadığını açıkça belirtmek gerektiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Petek içinde kalma ve süzülmeme koşullarını korur."},"facet_ids":["F001"],"text":"süzülmemiş petek balı","usage_role":"explanatory"},{"applicability":"Tekil bir parça ya da birim anlatılırken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Petekli balın tek birimini korur."},"facet_ids":["F002"],"text":"bir petek bal parçası","usage_role":"contextual"}],"definition":"Balmumu peteğinin içinde duran, henüz süzülmemiş baldır. Tek parça ve çoğul adları da bu petek içindeki bal anlayışına bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Balmumu peteği içinde bulunan ve henüz süzülmemiş bal dalın çekirdeğidir."},{"facet_id":"F002","role":"specialization","statement":"Tek parça adı, petekli balın bir birimini gösterir."},{"facet_id":"F003","role":"extension","statement":"Çoğul ad, aynı petekli bal parçalarının toplu biçimini anlatır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Süzülmüş veya petekten ayrılmış balı da kapsayacak biçimde genişler.","collision":null,"fit":"broadening","loses":null,"preserves":"Bal maddesini korur."},"text":"bal"}],"identity_rationale":"Kaynak ifadesi bu dalı süzülmeden önce balmumu içinde duran bal ve bunun tekil ile çoğul adları olarak verir. Hazır bulunma, tanıklık veya doğum belirtisiyle semantik bir çekirdek paylaşmaz; ayrı sözlükleşmiş bal anlamıdır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"petek içindeki süzülmemiş bal"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"petekli baldan bir parça"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"petekli ballar"}],"lexicalization_note":"Mekanik profil çıplak daldır; tanım yalnızca petekli bal alanını verir ve tanıklık dallarından anlam taşımaz.","neighbor_coverage_note":"Adaylar bal, petek, balmumu, bal toplama ve iç kökün uzak dalları bakımından incelendi. Tanıklık, dil, doğum ve gösterge dalları semantik sınırı açıklamadığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B007 petek ve süzülmemiş olma koşuluyla daralır; komşu dal balın genel adı ve baldan yapılan ya da bala benzeyen şeylerdir.","focus_only":"Bu dal balın özellikle petek içinde ve süzülmeden önceki halidir.","gloss":"bal","neighbor_only":"Komşu dal balı genel madde, yiyecek ve benzer tatlı şeyler alanında daha geniş verir.","neighbor_ref":"root_001014/B001","relation_type":"near_synonym","shared_zone":"İki dal bal maddesinde kesişir."},{"boundary_match":"partial","distinction":"B007 yiyecek olan petekli baldır; komşu dal daha çok arının yuvası veya balın üretildiği yerdir.","focus_only":"Bu dal petek içindeki balın kendisini anlatır.","gloss":"petek ve bal","neighbor_only":"Komşu dal arı yuvası, petek yeri ve arıların barındığı yapı alanına odaklanır.","neighbor_ref":"root_001330/B006","relation_type":"near_neighbor","shared_zone":"İki dal arı peteği ve balın bulunduğu ortamda buluşur."},{"boundary_match":"field_only","distinction":"B007 balın yenebilir petekli hali; komşu dal ise mum veya balın içindeki karışık tortu ve artık tarafıdır.","focus_only":"Bu dal petek içindeki balı anlatır.","gloss":"bal ve balmumu","neighbor_only":"Komşu dal bal mumu, balın içindeki tortu veya karışık artıklar alanındadır.","neighbor_ref":"root_000221/B003","relation_type":"same_field","shared_zone":"İki dal bal, balmumu ve petek çevresinde aynı alanda durur."},{"boundary_match":"thematic_only","distinction":"B007 ürünün kendisidir; komşu dal ürünü elde etme eylemi ve araçlarıdır.","focus_only":"Bu dal petekteki balın adıdır.","gloss":"bal toplama","neighbor_only":"Komşu dal balı yerinden alma, toplama ve bu işe yarayan araçlar alanıdır.","neighbor_ref":"root_000827/B002","relation_type":"thematic","shared_zone":"İki dal bal ve petek çevresindeki üretim sahnesini paylaşır."}],"source_summary":"Kaynaklar dalı balın petek ya da balmumu içinde ve süzülmeden önceki hali olarak ortaklaştırır. Tekil ve çoğul adlar da bu petekli bal anlamının biçimsel uzantılarıdır."},"support_links":[]},{"boundary":"Dal sözsüz belirti ve gösterge kullanımlarıdır; dil, hukuki tanıklık, petekli bal ve doğum artığı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000822/B008","candidate_links":[{"candidate_id":"cand_053dbd5f06d5eec5408c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَهِيد","morph_features":"STEM|POS:N|LEM:$ahiyd|ROOT:$hd|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"100:7:4:2","qac_word_ref":"100:7:4","surface_ar":"شَهِيدٌ"}],"gloss":"durumu gösteren belirti","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin başka bir zaman, durum veya niteliğe belirti olarak işaret etmesi dalın çekirdeğidir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yıldızın geceye işaret etmesi, sözsüz belirti kullanımının göksel örneğidir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Akşam namazı adı, vakit ve uygulama düzenine bağlı özel bir göstergedir."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Atın koşusunun üstünlüğe ve iyi koşmaya işaret etmesi, nitelik göstergesi örneğidir."}}],"root_ar":"ش ه د","root_id":"root_000822","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yıldız, namaz vakti ve at koşusu gibi sözsüz gösterge kullanımlarını birlikte karşılar.","boundary_detail":"Dal sözsüz belirti ve gösterge kullanımlarıdır; dil, hukuki tanıklık, petekli bal ve doğum artığı değildir.","concept_gloss":"durumu gösteren belirti","contextual_glosses":[{"applicability":"Yıldızın geceye işaret ettiği kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yıldızın geceye belirti olmasını korur."},"facet_ids":["F002"],"text":"geceyi gösteren yıldız","usage_role":"contextual"},{"applicability":"Namaz adı olarak verilen özel kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Akşam namazı adlandırmasını ve vakit göstergesi bağını korur."},"facet_ids":["F003"],"text":"akşam namazı","usage_role":"contextual"},{"applicability":"Atın koşusunun hız ve kaliteye delil olduğu bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Atın koşusunun üstünlük ve iyi nitelik göstermesini korur."},"facet_ids":["F004"],"text":"üstün koşuyu gösteren iz","usage_role":"contextual"}],"definition":"Bir zaman, durum veya niteliği gösteren belirtiye verilen addır. Yıldızın geceye, akşam namazının vakit düzenine ve atın koşusunun hız ile kaliteye işaret etmesi bu bağlı kullanımları oluşturur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin başka bir zaman, durum veya niteliğe belirti olarak işaret etmesi dalın çekirdeğidir."},{"facet_id":"F002","role":"example","statement":"Yıldızın geceye işaret etmesi, sözsüz belirti kullanımının göksel örneğidir."},{"facet_id":"F003","role":"example","statement":"Akşam namazı adı, vakit ve uygulama düzenine bağlı özel bir göstergedir."},{"facet_id":"F004","role":"example","statement":"Atın koşusunun üstünlüğe ve iyi koşmaya işaret etmesi, nitelik göstergesi örneğidir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kişi veya sözlü beyan sahibi anlamını ekler.","collision":"Bu karşılık B002 dalıyla çakışır.","fit":"displacement","loses":"Sözsüz belirti, zaman ve nitelik göstergesi sınırını kaybeder.","preserves":"Bir şeyin başka bir şeye kanıt olması çağrışımını korur."},"text":"tanık"}],"identity_rationale":"Kaynak ifadesi bu dalı bir duruma, zamana veya niteliğe işaret eden şeyler için kullanılan ad olarak verir: geceyi gösteren yıldız, akşam namazı ve atın koşusunun üstünlüğe işaret eden yanı. Dal, sözlü tanıklıktan çok belirti ve gösterge işlevine dayanır.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"geceye işaret eden yıldız"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"akşam namazı için kullanılan ad"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"atın üstünlüğünü ve iyi koştuğunu gösteren koşu"}],"lexicalization_note":"Tanım gösterge çekirdeğini verir; yıldız, akşam namazı ve at koşusu kullanımları ayrı kalıp veya bağlamlara bağlıdır.","neighbor_coverage_note":"Adaylar işaret, iz, zaman, yıldız gözlemi ve iç kökün tanıklık dalları bakımından incelendi. Dil, bal ve doğum dalları bu gösterge çekirdeğine yalnızca uzak biçim ortaklığıyla bağlıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B008 belirli örnekler üzerinden sözsüz tanıklık eden belirti adıdır; komşu dal genel işaret ve nişan sistemini daha geniş kapsar.","focus_only":"Bu dal belirti adını yıldız, namaz vakti ve at koşusu örnekleriyle verir.","gloss":"işaret eden belirti","neighbor_only":"Komşu dal işaret, nişan, yol gösteren belirti, bayrak ve sınır gibi daha geniş işaretler alanındadır.","neighbor_ref":"root_001040/B002","relation_type":"near_synonym","shared_zone":"İki dal bir şeyin başka bir şeyi tanıtması veya göstermesi alanında örtüşür."},{"boundary_match":"partial","distinction":"B008 etkin bir gösterge adıdır; komşu dal daha çok geride kalan iz veya kalıntı üzerinden anlam kurar.","focus_only":"Bu dal zaman, durum veya niteliği gösteren belirtiyi anlatır.","gloss":"iz ve belirti","neighbor_only":"Komşu dal geçmiş bir varlık veya olaydan kalan iz ve kalıntıya odaklanır.","neighbor_ref":"root_000011/B003","relation_type":"near_neighbor","shared_zone":"İki dal bir şeyden başka bir şeyin anlaşılması alanını paylaşır."},{"boundary_match":"partial","distinction":"B008 örnek adlandırmalara bağlıdır; komşu dal daha genel işaret ve belirlenmiş zaman sözlüğüdür.","focus_only":"Bu dal yıldız, namaz ve koşu gibi örnekleri belirti sayar.","gloss":"belirti ve zaman","neighbor_only":"Komşu dal işaret, yol alameti, belirlenmiş zaman veya randevu alanını kapsar.","neighbor_ref":"root_000051/B005","relation_type":"near_neighbor","shared_zone":"İki dal işaret ve zaman gösterme alanında kesişir."},{"boundary_match":"partial","distinction":"B008 kişi olmayan işaretler ve örneklerdir; B002 tanığın bildiğini sözle ortaya koymasıdır.","focus_only":"Bu dal sözsüz belirtiyi tanık gibi işler.","gloss":"belirti olarak tanıklık","neighbor_only":"B002 bilgiyi açıklayan kişi ya da beyanı anlatır.","neighbor_ref":"root_000822/B002","relation_type":"near_neighbor","shared_zone":"İki dal bir şeyin başka bir şey için kanıt veya gösterge olmasında buluşur."}],"source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynaklı iddia; yıldız, akşam namazı ve at koşusu örneklerini belirti adı olarak verir."}],"source_summary":"Bu dalda ortak kaynak iddiası yerine tek kaynaklı bir belirti kullanımı verilir. İddia, yıldız, akşam namazı ve at koşusu örneklerini sözsüz gösterge işlevi altında toplar."},"support_links":["sup_d1d7ccfa40709322258c"]}],"candidate_inventory":[{"anchor_refs":["100:7:1"],"branch_refs":[],"candidate_id":"cand_1172efc732eca1e5aa10","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:7:1:coordinated-twin-assertion","source_type":"word_analysis","support_ids":["sup_169032e00e99e13d6b08","sup_8f8f344fcc29ebeb198c"],"title":"connector makes the witness claim paired","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:1","qac_refs":["100:7:1:1"],"status":"accepted"}},{"anchor_refs":["100:7:1"],"branch_refs":[],"candidate_id":"cand_3924ebb91ad8b7aa74d4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:7:1:simultaneous-witnessing-shade","source_type":"word_analysis","support_ids":["sup_8f8f344fcc29ebeb198c","sup_ae34dab2e2638cb0c757"],"title":"coordination keeps simultaneity audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:1","qac_refs":["100:7:1:1"],"status":"accepted"}},{"anchor_refs":["100:7:2"],"branch_refs":[],"candidate_id":"cand_0d1cb586dbf66cdb7c9b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:7:2:controlled-referent-openness","source_type":"word_analysis","support_ids":["sup_249365056bd27d326d94","sup_791350df25cef4a17e13"],"title":"one pronoun routes multiple witnesses","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:2","qac_refs":["100:7:1:2","100:7:1:3"],"status":"accepted"}},{"anchor_refs":["100:7:2"],"branch_refs":[],"candidate_id":"cand_7d90c298dd57cdd1a6ec","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:7:2:emphatic-subject-pivot","source_type":"word_analysis","support_ids":["sup_249365056bd27d326d94","sup_41e71880ac29b7111dba"],"title":"assertion and subject arrive fused","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:2","qac_refs":["100:7:1:2","100:7:1:3"],"status":"accepted"}},{"anchor_refs":["100:7:3"],"branch_refs":[],"candidate_id":"cand_571b5e78487484387242","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:7:3:delayed-predicate-frame","source_type":"word_analysis","support_ids":["sup_63c9953151624cf7b224","sup_acf9a1fb778116e8149b"],"title":"fronted phrase delays the witness landing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:3","qac_refs":["100:7:2:1"],"status":"accepted"}},{"anchor_refs":["100:7:3"],"branch_refs":[],"candidate_id":"cand_effa397a460e7d77f51d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:7:3:relation-to-evidence-shift","source_type":"word_analysis","support_ids":["sup_63c9953151624cf7b224","sup_fc89811686160b15faa8"],"title":"relation becomes evidence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:3","qac_refs":["100:7:2:1"],"status":"accepted"}},{"anchor_refs":["100:7:3"],"branch_refs":[],"candidate_id":"cand_8ce4c5e9966d679fd3f7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:7:3:witness-relation-range","source_type":"word_analysis","support_ids":["sup_3eb6102b04fd1335f122","sup_63c9953151624cf7b224"],"title":"preposition gives testimony a domain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:3","qac_refs":["100:7:2:1"],"status":"accepted"}},{"anchor_refs":["100:7:4"],"branch_refs":[],"candidate_id":"cand_a57f1d0128ac31c579b5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:7:4:distant-demonstrative-exhibit","source_type":"word_analysis","support_ids":["sup_77404e6a06af6a6d3978","sup_919c1a951a3fa21ccf89"],"title":"distance makes the charge inspectable","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:4","qac_refs":["100:7:3:1"],"status":"accepted"}},{"anchor_refs":["100:7:4"],"branch_refs":[],"candidate_id":"cand_774e661836e80b760010","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:7:4:fronted-pointer-before-predicate","source_type":"word_analysis","support_ids":["sup_919c1a951a3fa21ccf89","sup_d8c858bab51c90caa968"],"title":"the pointer arrives before the predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:4","qac_refs":["100:7:3:1"],"status":"accepted"}},{"anchor_refs":["100:7:4"],"branch_refs":[],"candidate_id":"cand_65e73c22dd9460ba3707","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:7:4:governed-evidentiary-object","source_type":"word_analysis","support_ids":["sup_919c1a951a3fa21ccf89","sup_fe9c4d0b50d47678941a"],"title":"that becomes the witness matter","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:4","qac_refs":["100:7:3:1"],"status":"accepted"}},{"anchor_refs":["100:7:5"],"branch_refs":[],"candidate_id":"cand_011ac71f675a9835ce10","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:7:5:delayed-khabar-arrival","source_type":"word_analysis","support_ids":["sup_d1d6f7dca191e4f6fb29","sup_eaeedacce454e9c7c9d9"],"title":"lām marks the delayed predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:5","qac_refs":["100:7:4:1"],"status":"accepted"}},{"anchor_refs":["100:7:5"],"branch_refs":[],"candidate_id":"cand_6d8965616c4f4efc5a10","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:7:5:double-emphasis-frame","source_type":"word_analysis","support_ids":["sup_09e2c42fa72123a67126","sup_d1d6f7dca191e4f6fb29"],"title":"predicate is sealed under emphasis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:5","qac_refs":["100:7:4:1"],"status":"accepted"}},{"anchor_refs":["100:7:5"],"branch_refs":[],"candidate_id":"cand_201702b3eb737ed6a351","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:7:5:predicate-fusion-sound","source_type":"word_analysis","support_ids":["sup_5619db268991f75d0609","sup_d1d6f7dca191e4f6fb29"],"title":"emphasis is heard inside the noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:5","qac_refs":["100:7:4:1"],"status":"accepted"}},{"anchor_refs":["100:7:6"],"branch_refs":[],"candidate_id":"cand_8250904638f5989f3060","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000822"],"scope":"focus_ayah","source_local_id":"100:7:6:active-primary-passive-undertone","source_type":"word_analysis","support_ids":["sup_a2e14d07c42d223b5141","sup_c7be7dfa644608d80719"],"title":"active witness with exposed undertone","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:6","qac_refs":["100:7:4:2"],"status":"accepted"}},{"anchor_refs":["100:7:6"],"branch_refs":[],"candidate_id":"cand_f3dfc3f090e04f426e4d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000822"],"scope":"focus_ayah","source_local_id":"100:7:6:broad-root-field-limited","source_type":"word_analysis","support_ids":["sup_6c623c8cab64831040e3","sup_a2e14d07c42d223b5141"],"title":"broad root field is locally selected","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:6","qac_refs":["100:7:4:2"],"status":"accepted"}},{"anchor_refs":["100:7:6"],"branch_refs":[],"candidate_id":"cand_b8246e5cc332c6f65e5e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000822"],"scope":"focus_ayah","source_local_id":"100:7:6:converging-form-meaning-sound","source_type":"word_analysis","support_ids":["sup_4f09061c935f3a2a0097","sup_a2e14d07c42d223b5141"],"title":"form, meaning, and echo converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:6","qac_refs":["100:7:4:2"],"status":"accepted"}},{"anchor_refs":["100:7:6"],"branch_refs":[],"candidate_id":"cand_4ce95163d2f11f6f73e1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000822"],"scope":"focus_ayah","source_local_id":"100:7:6:diagnosis-to-exposure-boundary","source_type":"word_analysis","support_ids":["sup_92fe3bb8478a9244ec61","sup_a2e14d07c42d223b5141"],"title":"charge becomes exposure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:6","qac_refs":["100:7:4:2"],"status":"accepted"}},{"anchor_refs":["100:7:6"],"branch_refs":[],"candidate_id":"cand_3389636869c43278ed70","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000822"],"scope":"focus_ayah","source_local_id":"100:7:6:final-predicate-landing","source_type":"word_analysis","support_ids":["sup_9718a4fdb76592663be9","sup_a2e14d07c42d223b5141"],"title":"final noun resolves the clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:6","qac_refs":["100:7:4:2"],"status":"accepted"}},{"anchor_refs":["100:7:6"],"branch_refs":[],"candidate_id":"cand_41d1c75243139eb7e40b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000822"],"scope":"focus_ayah","source_local_id":"100:7:6:governed-witness-domain","source_type":"word_analysis","support_ids":["sup_a2e14d07c42d223b5141","sup_fd39b11b749dbfd37098"],"title":"witnesshood is tied to that matter","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:6","qac_refs":["100:7:4:2"],"status":"accepted"}},{"anchor_refs":["100:7:6"],"branch_refs":[],"candidate_id":"cand_da93a45af866a9f3510a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000822"],"scope":"focus_ayah","source_local_id":"100:7:6:presence-testimony-field","source_type":"word_analysis","support_ids":["sup_075927a055e9ba1912ff","sup_a2e14d07c42d223b5141"],"title":"presence becomes accountable testimony","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:6","qac_refs":["100:7:4:2"],"status":"accepted"}},{"anchor_refs":["100:7:6"],"branch_refs":[],"candidate_id":"cand_e95c76a1541de4630e11","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000822"],"scope":"focus_ayah","source_local_id":"100:7:6:qualitative-durable-predicate","source_type":"word_analysis","support_ids":["sup_9cdc27cadf51b388c14e","sup_a2e14d07c42d223b5141"],"title":"indefinite faʿīl makes witnesshood durable","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:6","qac_refs":["100:7:4:2"],"status":"accepted"}},{"anchor_refs":["100:7:6"],"branch_refs":[],"candidate_id":"cand_f920d12842e8f3448063","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000822"],"scope":"focus_ayah","source_local_id":"100:7:6:shahid-shadid-forward-echo","source_type":"word_analysis","support_ids":["sup_a2e14d07c42d223b5141","sup_f2d1142055c132f3e30f"],"title":"witness sound carries into intensity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:6","qac_refs":["100:7:4:2"],"status":"accepted"}},{"anchor_refs":["100:7:6"],"branch_refs":[],"candidate_id":"cand_54d794bc099c27aae610","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000822"],"scope":"focus_ayah","source_local_id":"100:7:6:sound-sealed-testimony","source_type":"word_analysis","support_ids":["sup_26e4a013c407ac134a48","sup_a2e14d07c42d223b5141"],"title":"sound closes as testimony","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:7:6","qac_refs":["100:7:4:2"],"status":"accepted"}},{"anchor_refs":["100:7:4"],"branch_refs":[],"candidate_id":"cand_1ba61d7133c6161b2304","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000822"],"scope":"focus_ayah","source_local_id":"100:7:4:2","source_type":"qac_morpheme","support_ids":["sup_0b1625b7bf40868e8ca9"],"title":"QAC root occurrence: ش ه د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["100:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:7","branch_refs":["root_000822/B001"],"candidate_id":"cand_54cb9a8a1203d1d9b06b","commentary_obligation":"review","hft_ref":"hft_ef46d7a3d00436736a6e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:BSL-01-direct-presence","source_type":"hft","support_ids":["sup_25e5057ab0e14e70f1ff"],"title":"BSL-01-direct-presence","trust":"legacy_unbound"},{"anchor_refs":["100:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:7","branch_refs":["root_000822/B002"],"candidate_id":"cand_e5c6f79574c84f64b4cd","commentary_obligation":"review","hft_ref":"hft_f555701c4a3d248a0f65","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:BSL-02-knowledge-testimony","source_type":"hft","support_ids":["sup_ae566337038aa36c8eb4"],"title":"BSL-02-knowledge-testimony","trust":"legacy_unbound"},{"anchor_refs":["100:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:7","branch_refs":["root_000822/B005"],"candidate_id":"cand_86ec624cf53dcb38a7b0","commentary_obligation":"review","hft_ref":"hft_4d76d57709805ad5b1b7","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:BSL-03-visible-expression","source_type":"hft","support_ids":["sup_290a4a96d70f18eb2229"],"title":"BSL-03-visible-expression","trust":"legacy_unbound"},{"anchor_refs":["100:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:7","branch_refs":["root_000822/B008"],"candidate_id":"cand_053dbd5f06d5eec5408c","commentary_obligation":"review","hft_ref":"hft_03f8ea84123cba680127","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:BSL-04-witnessing-sign","source_type":"hft","support_ids":["sup_d1d7ccfa40709322258c"],"title":"BSL-04-witnessing-sign","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"100:7:1:1","qac_word_ref":"100:7:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"100:7:1:2","qac_word_ref":"100:7:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"100:7:1:3","qac_word_ref":"100:7:1","root_ar":"","surface_ar":"هُۥ"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"100:7:2:1","qac_word_ref":"100:7:2","root_ar":"","surface_ar":"عَلَىٰ"},{"lemma_ar":"ذَٰلِك","morph_features":"STEM|POS:DEM|LEM:*a`lik|MS","morpheme_role":"STEM","pos":"DEM","qac_ref":"100:7:3:1","qac_word_ref":"100:7:3","root_ar":"","surface_ar":"ذَٰلِكَ"},{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"100:7:4:1","qac_word_ref":"100:7:4","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"شَهِيد","morph_features":"STEM|POS:N|LEM:$ahiyd|ROOT:$hd|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"100:7:4:2","qac_word_ref":"100:7:4","root_ar":"ش ه د","surface_ar":"شَهِيدٌ"}],"word_analysis_qac_refs":[["100:7:1:1"],["100:7:1:2","100:7:1:3"],["100:7:2:1"],["100:7:3:1"],["100:7:4:1"],["100:7:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["100:7:1","100:7:2","100:7:3","100:7:4","100:7:5","100:7:6"]},"focus_surface_evidence":{"arabic_uthmani":"وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"100:7:1:1","qac_word_ref":"100:7:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"100:7:1:2","qac_word_ref":"100:7:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"100:7:1:3","qac_word_ref":"100:7:1","root_ar":"","surface_ar":"هُۥ"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"100:7:2:1","qac_word_ref":"100:7:2","root_ar":"","surface_ar":"عَلَىٰ"},{"lemma_ar":"ذَٰلِك","morph_features":"STEM|POS:DEM|LEM:*a`lik|MS","morpheme_role":"STEM","pos":"DEM","qac_ref":"100:7:3:1","qac_word_ref":"100:7:3","root_ar":"","surface_ar":"ذَٰلِكَ"},{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"100:7:4:1","qac_word_ref":"100:7:4","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"شَهِيد","morph_features":"STEM|POS:N|LEM:$ahiyd|ROOT:$hd|MS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"100:7:4:2","qac_word_ref":"100:7:4","root_ar":"ش ه د","surface_ar":"شَهِيدٌ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["100:7:1:1"],["100:7:1:2","100:7:1:3"],["100:7:2:1"],["100:7:3:1"],["100:7:4:1"],["100:7:4:2"]],"word_analysis_refs":["100:7:1","100:7:2","100:7:3","100:7:4","100:7:5","100:7:6"],"word_rows":[{"analysis_record_ref":"100:7:1","analytic_gloss_range_en":"coordinating connector that binds this ayah to the prior emphatic diagnosis; a circumstantial shade is available only under that linkage","analytic_root_gloss_range_en":null,"qac_refs":["100:7:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"100:7:2","analytic_gloss_range_en":"emphatic particle plus third-person suffix; the subject slot is syntactically fixed while the referent remains deliberately open","analytic_root_gloss_range_en":null,"qac_refs":["100:7:1:2","100:7:1:3"],"root":{},"surface":{"arabic":"إِنَّهُۥ","transliteration":"innahū"}},{"analysis_record_ref":"100:7:3","analytic_gloss_range_en":"preposition governing the demonstrative as the matter over, regarding, or against which witnesshood applies","analytic_root_gloss_range_en":null,"qac_refs":["100:7:2:1"],"root":{},"surface":{"arabic":"عَلَىٰ","transliteration":"ʿalā"}},{"analysis_record_ref":"100:7:4","analytic_gloss_range_en":"distant demonstrative governed by the preposition; points back to the prior proposition and makes it an identifiable matter under witness","analytic_root_gloss_range_en":null,"qac_refs":["100:7:3:1"],"root":{},"surface":{"arabic":"ذَٰلِكَ","transliteration":"dhālika"}},{"analysis_record_ref":"100:7:5","analytic_gloss_range_en":"predicate lām of emphasis attached to the witness noun; confirms the khabar and makes the final predicate arrive with asserted certainty","analytic_root_gloss_range_en":null,"qac_refs":["100:7:4:1"],"root":{},"surface":{"arabic":"لَ","transliteration":"la-"}},{"analysis_record_ref":"100:7:6","analytic_gloss_range_en":"witness, one characterized by testimony or witnesshood; locally an indefinite nominative predicate governed by the emphatic clause and restricted by {{ar:عَلَىٰ ذَٰلِكَ}} ({{tr:ʿalā dhālika}})","analytic_root_gloss_range_en":"root range centered on presence, witnessing, seeing, and testifying from knowledge, with farther branches such as attestation formula, martyrdom, visible signs, and nonlocal lexical byways; the local noun selects the witness/testimony field","qac_refs":["100:7:4:2"],"root":{"arabic":"ش ه د","transliteration":"sh-h-d"},"surface":{"arabic":"شَهِيدٌۭ","transliteration":"shahīdun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":6,"words_total":6,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["100:7"],"branch_refs":["root_000822/B001"],"candidate_id":"cand_54cb9a8a1203d1d9b06b","evidence_scope":"focus_ayah","hft_ref":"hft_ef46d7a3d00436736a6e","item_id":"BSL-01-direct-presence","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:BSL-01-direct-presence","support_id":"sup_25e5057ab0e14e70f1ff"},{"anchor_refs":["100:7"],"branch_refs":["root_000822/B002"],"candidate_id":"cand_e5c6f79574c84f64b4cd","evidence_scope":"focus_ayah","hft_ref":"hft_f555701c4a3d248a0f65","item_id":"BSL-02-knowledge-testimony","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:BSL-02-knowledge-testimony","support_id":"sup_ae566337038aa36c8eb4"},{"anchor_refs":["100:7"],"branch_refs":["root_000822/B005"],"candidate_id":"cand_86ec624cf53dcb38a7b0","evidence_scope":"focus_ayah","hft_ref":"hft_4d76d57709805ad5b1b7","item_id":"BSL-03-visible-expression","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:BSL-03-visible-expression","support_id":"sup_290a4a96d70f18eb2229"},{"anchor_refs":["100:7"],"branch_refs":["root_000822/B008"],"candidate_id":"cand_053dbd5f06d5eec5408c","evidence_scope":"focus_ayah","hft_ref":"hft_03f8ea84123cba680127","item_id":"BSL-04-witnessing-sign","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:BSL-04-witnessing-sign","support_id":"sup_d1d7ccfa40709322258c"}],"diagnostics":[{"warning":"Unrecognized HFT reader field is preserved as a global review record"},{"warning":"Unrecognized HFT reader field is preserved as a global review record"}],"lane_counts":{"global":11,"macro":13,"micro":4},"packet_summary":{"ayah_count":11,"focus_ref":"100:7","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ع د و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000993","furuq_root_norm":"ع د و","furuq_source_root_norm":"ع د و","is_dominant":true,"target_occurrences":68,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":5,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":false,"target_occurrences":4,"target_rank":3}]},{"qac_root":"ث و ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000210","furuq_root_norm":"ث و ر","furuq_source_root_norm":"ث و ر","is_dominant":true,"target_occurrences":4,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000011","furuq_root_norm":"ء ث ر","furuq_source_root_norm":"أ ث ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["100:1","100:2","100:3","100:4","100:5","100:6","100:7","100:8","100:9","100:10","100:11"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"100:7","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v3","reader_id":"reader_hft_a","trace_kind":null}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":17,"unstructured_record_count":2},"identity":{"ayah_ref":"100:7","lane":"micro","linguistic_source_ref":"100:7","surface_ref":"100:7","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"100:7","target_tokens":[["O",["100:7:1"]],["da",["100:7:1"]],["buna",["100:7:2","100:7:3"]],["gerçekten",["100:7:1","100:7:4"]],["tanıktır",["100:7:4"]]],"text":"O da buna gerçekten tanıktır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s100-p01-001-011","label":"Whole surah","number":1,"refs":["100:1","100:2","100:3","100:4","100:5","100:6","100:7","100:8","100:9","100:10","100:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:6:presence-testimony-field","source_type":"word_analysis","support_id":"sup_075927a055e9ba1912ff","text":"{\"blocking_evidence\":null,\"headline\":\"presence becomes accountable testimony\",\"reader_payoff\":\"The reader notices that self-knowledge is recast as evidence-bearing presence, seeing, and declaration rather than private awareness.\",\"reason\":\"V4 supports the presence-with-witnessing and testimony-from-knowledge branches; the topic is narrowed because farther dictionary branches do not activate in the local witness predicate.\",\"representative_source_ids\":[\"QS-6fda8852\",\"QS-a741c06f\",\"QS-da567c10\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:5:double-emphasis-frame","source_type":"word_analysis","support_id":"sup_09e2c42fa72123a67126","text":"{\"blocking_evidence\":null,\"headline\":\"predicate is sealed under emphasis\",\"reader_payoff\":\"The reader notices that the witness claim is not offered as neutral description but as a confirmed verdict.\",\"reason\":\"QAC identifies the prefix as lām al-tawkīd on the predicate of {{ar:إِنَّ}} ({{tr:inna}}), and translation support warns not to weaken the coordinated emphatic assertion.\",\"representative_source_ids\":[\"QG-e830dca5\",\"QS-25086bb7\",\"QT-a8b28d1c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"100:7:4:2","source_type":"qac_morpheme","support_id":"sup_0b1625b7bf40868e8ca9","text":"{\"lemma_ar\":\"شَهِيد\",\"morph_features\":\"STEM|POS:N|LEM:$ahiyd|ROOT:$hd|MS|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"100:7:4:2\",\"qac_word_ref\":\"100:7:4\",\"root_ar\":\"ش ه د\",\"surface_ar\":\"شَهِيدٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:1:coordinated-twin-assertion","source_type":"word_analysis","support_id":"sup_169032e00e99e13d6b08","text":"{\"blocking_evidence\":null,\"headline\":\"connector makes the witness claim paired\",\"reader_payoff\":\"The reader notices that the witness statement is the immediate evidentiary counterpart to the prior charge, not a new disconnected topic.\",\"reason\":\"QAC identifies the word as coordination, and attachment evidence treats 100:7 as a coordinated emphatic nominal clause continuing the prior assertion.\",\"representative_source_ids\":[\"QG-1056d95c\",\"QT-cfb3569c\",\"QB-e04e083f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:2","source_type":"word_analysis","support_id":"sup_249365056bd27d326d94","text":"{\"gloss_range\":\"emphatic particle plus third-person suffix; the subject slot is syntactically fixed while the referent remains deliberately open\",\"prose\":\"{{ar:إِنَّهُۥ}} ({{tr:innahū}}) fuses the confirmer with the pronoun before the witness predicate appears, so the clause begins as a formal assertion rather than a loose statement. The suffix is the governed subject of {{ar:إِنَّ}} ({{tr:inna}}), but its referent is not flattened: the human reading remains the nearest continuation from 100:6, while divine or record-like witnessing remains grammatically live. That openness is controlled by the fixed nominal architecture, so the ambiguity can frame accountability as self-witness, divine warning, or preserved record without making the clause unstable.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِنَّهُۥ}} ({{tr:innahū}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:6:sound-sealed-testimony","source_type":"word_analysis","support_id":"sup_26e4a013c407ac134a48","text":"{\"blocking_evidence\":null,\"headline\":\"sound closes as testimony\",\"reader_payoff\":\"The reader notices the predicate's audible movement from spreading sh into dental d with tanwin, matching the way testimony exposes and then fixes the matter.\",\"reason\":\"The row is phonetic rather than lexical, but it has a concrete local payoff in the final predicate's closure.\",\"representative_source_ids\":[\"QP-609637bf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:3:witness-relation-range","source_type":"word_analysis","support_id":"sup_3eb6102b04fd1335f122","text":"{\"blocking_evidence\":null,\"headline\":\"preposition gives testimony a domain\",\"reader_payoff\":\"The reader notices that the testimony is not free-floating; it is positioned over, about, and even as evidence against the self concerning the named matter.\",\"reason\":\"QAC and attachment evidence both make {{ar:عَلَىٰ}} ({{tr:ʿalā}}) govern {{ar:ذَٰلِكَ}} ({{tr:dhālika}}) as the matter over which the witness predicate applies.\",\"representative_source_ids\":[\"QG-bae31aa2\",\"MG-4ea35612\",\"QS-d36d5490\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:2:emphatic-subject-pivot","source_type":"word_analysis","support_id":"sup_41e71880ac29b7111dba","text":"{\"blocking_evidence\":null,\"headline\":\"assertion and subject arrive fused\",\"reader_payoff\":\"The reader notices that the witness claim is already placed under emphatic assertion before the predicate lands.\",\"reason\":\"Attachment evidence makes the suffix the governed ism of {{ar:إِنَّ}} ({{tr:inna}}), with {{ar:شَهِيدٌۭ}} ({{tr:shahīdun}}) as the predicate of the same emphatic nominal clause.\",\"representative_source_ids\":[\"QG-076745fc\",\"QF-37f80f6e\",\"QT-f7e0101b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:6:converging-form-meaning-sound","source_type":"word_analysis","support_id":"sup_4f09061c935f3a2a0097","text":"{\"blocking_evidence\":null,\"headline\":\"form, meaning, and echo converge\",\"reader_payoff\":\"The reader notices that durable faʿīl quality, witness/exposure pressure, and the 100:8 sh/-i-/d sound echo work together rather than as isolated details.\",\"reason\":\"The synthesis row is supported by the faʿīl predicate, the locally narrowed witness field, and the concrete echo with the intense predicate in 100:8.\",\"representative_source_ids\":[\"QY-29efe3b4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:5:predicate-fusion-sound","source_type":"word_analysis","support_id":"sup_5619db268991f75d0609","text":"{\"blocking_evidence\":null,\"headline\":\"emphasis is heard inside the noun\",\"reader_payoff\":\"The reader notices that the certainty marker is audibly fused to the witness predicate rather than standing outside it.\",\"reason\":\"The local surface is pronounced as {{ar:لَشَهِيدٌۭ}} ({{tr:la-shahīdun}}), making the emphatic prefix part of the predicate's surface form.\",\"representative_source_ids\":[\"QF-25a2f62d\",\"QP-a9495157\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:3","source_type":"word_analysis","support_id":"sup_63c9953151624cf7b224","text":"{\"gloss_range\":\"preposition governing the demonstrative as the matter over, regarding, or against which witnesshood applies\",\"prose\":\"{{ar:عَلَىٰ}} ({{tr:ʿalā}}) makes the testimony relational rather than vague. It governs {{ar:ذَٰلِكَ}} ({{tr:dhālika}}) and positions the witness with respect to the prior matter: concerning it, over it, and with an adversarial edge that can mount self-knowledge as evidence against the self. Because the phrase comes before {{ar:لَشَهِيدٌۭ}} ({{tr:la-shahīdun}}), the clause names the evidentiary object before the predicate lands, moving the scene from the relationship named in 100:6 into an accountable witness posture.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:عَلَىٰ}} ({{tr:ʿalā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:6:broad-root-field-limited","source_type":"word_analysis","support_id":"sup_6c623c8cab64831040e3","text":"{\"blocking_evidence\":null,\"headline\":\"broad root field is locally selected\",\"reader_payoff\":\"The reader notices that the word belongs to a broad Quranic testimony field while the ayah selects the witness/testimony branch for this predicate.\",\"reason\":\"The root distribution and V4 branches supply lexical breadth, but formal match is not activation; nonlocal branches such as martyrdom, ritual formula, honeycomb, and birth traces are not made local here.\",\"representative_source_ids\":[\"QS-99a9e035\",\"QI-b62aec48\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:4:distant-demonstrative-exhibit","source_type":"word_analysis","support_id":"sup_77404e6a06af6a6d3978","text":"{\"blocking_evidence\":null,\"headline\":\"distance makes the charge inspectable\",\"reader_payoff\":\"The reader notices that the prior inner condition is set at a measured distance as something assessable.\",\"reason\":\"QAC identifies the word as a distant demonstrative pointing back to 100:6, while translation support warns against adding an explanatory noun that would over-resolve the deictic reference.\",\"representative_source_ids\":[\"QG-f7a15362\",\"QS-8792dce7\",\"QB-57f952c5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:2:controlled-referent-openness","source_type":"word_analysis","support_id":"sup_791350df25cef4a17e13","text":"{\"blocking_evidence\":null,\"headline\":\"one pronoun routes multiple witnesses\",\"reader_payoff\":\"The reader notices that the ayah can keep human self-witness, divine warning, and record-like testimony in play without choosing a single explicit noun.\",\"reason\":\"The guardrails mark the pronoun antecedent as ambiguous and warn against forcing an explicit target-language subject; the claim is narrowed because the local surface preserves live readings rather than proving that all readings are equally primary.\",\"representative_source_ids\":[\"QG-2eb67c9b\",\"MG-863bfa35\",\"QS-386cfdea\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:1","source_type":"word_analysis","support_id":"sup_8f8f344fcc29ebeb198c","text":"{\"gloss_range\":\"coordinating connector that binds this ayah to the prior emphatic diagnosis; a circumstantial shade is available only under that linkage\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) does not let 100:7 open as a detached comment. It carries the charge of 100:6 into a paired emphatic assertion: the human is described as kanūd, and then the matter is immediately placed under witness. The connector also allows a narrowed circumstantial pressure, so the witnessing can be heard as accompanying the ingratitude, but the local grammar keeps coordination as the main relation rather than replacing it with a free-standing \\\"while\\\" clause.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:4","source_type":"word_analysis","support_id":"sup_919c1a951a3fa21ccf89","text":"{\"gloss_range\":\"distant demonstrative governed by the preposition; points back to the prior proposition and makes it an identifiable matter under witness\",\"prose\":\"{{ar:ذَٰلِكَ}} ({{tr:dhālika}}) is the pointed matter of testimony. Under {{ar:عَلَىٰ}} ({{tr:ʿalā}}), the demonstrative turns the prior charge from 100:6 into an identifiable exhibit rather than a general theme or a new object. Its form packages pointing, distance, and address, so the ingratitude is held out as \\\"that,\\\" something pointed to, measured, and inspectable before the witness noun answers it.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:ذَٰلِكَ}} ({{tr:dhālika}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:6:diagnosis-to-exposure-boundary","source_type":"word_analysis","support_id":"sup_92fe3bb8478a9244ec61","text":"{\"blocking_evidence\":null,\"headline\":\"charge becomes exposure\",\"reader_payoff\":\"The reader notices that the ayah turns the charge of ingratitude into accountable exposure, leaving ignorance unavailable as an escape.\",\"reason\":\"The boundary rows coherently connect the witness predicate to the prior diagnosis and Lord relation, while the local prepositional phrase supplies the evidentiary matter.\",\"representative_source_ids\":[\"QB-29faa8fd\",\"QB-9d27dd27\",\"QB-d6248501\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:6:final-predicate-landing","source_type":"word_analysis","support_id":"sup_9718a4fdb76592663be9","text":"{\"blocking_evidence\":null,\"headline\":\"final noun resolves the clause\",\"reader_payoff\":\"The reader notices the final predicate answering the accumulated subject, emphatic force, and evidentiary phrase.\",\"reason\":\"The clause order places the witness predicate after {{ar:إِنَّهُۥ}} ({{tr:innahū}}) and {{ar:عَلَىٰ ذَٰلِكَ}} ({{tr:ʿalā dhālika}}), giving the final noun closure weight.\",\"representative_source_ids\":[\"QT-1cef13e1\",\"QT-8be98129\",\"QT-f9706767\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:6:qualitative-durable-predicate","source_type":"word_analysis","support_id":"sup_9cdc27cadf51b388c14e","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite faʿīl makes witnesshood durable\",\"reader_payoff\":\"The reader notices that the clause characterizes the subject with witnesshood as a settled quality, not merely as the performer of a momentary act.\",\"reason\":\"QAC describes the word as an indefinite nominative predicate on the faʿīl pattern, and attachment evidence makes it the khabar of {{ar:إِنَّ}} ({{tr:inna}}).\",\"representative_source_ids\":[\"QG-2f7f13bf\",\"QG-ea34cdb0\",\"QF-146beabb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:6","source_type":"word_analysis","support_id":"sup_a2e14d07c42d223b5141","text":"{\"gloss_range\":\"witness, one characterized by testimony or witnesshood; locally an indefinite nominative predicate governed by the emphatic clause and restricted by {{ar:عَلَىٰ ذَٰلِكَ}} ({{tr:ʿalā dhālika}})\",\"prose\":\"{{ar:شَهِيدٌۭ}} ({{tr:shahīdun}}) is the predicate that resolves the whole suspended clause. It is not a bare act of seeing: the {{ar:ش ه د}} ({{tr:sh-h-d}}) field joins presence, perception, and declaration, so the prior condition becomes accountable testimony that cannot be treated as ignorance. Locally, {{ar:عَلَىٰ ذَٰلِكَ}} ({{tr:ʿalā dhālika}}) restricts that witnesshood to the pointed matter from 100:6, and the indefinite faʿīl predicate makes witnesshood a durable quality rather than a titled office or a one-time verb. The wider Quranic testimony field stays in view, but this predicate selects witness and testimony rather than nonlocal branches. The active reading is primary, but the form and context preserve a narrowed passive undertone: the subject is witness, and the ingratitude is also exposed as witnessed evidence. In final position, {{ar:لَشَهِيدٌۭ}} ({{tr:la-shahīdun}}) lands with closure weight, moving from a spreading sh-opening into a dental d with tanwin, then its shared sh-opening, long -i- cadence, and final d prepare the next ayah's intense predicate (100:8), carrying testimony forward into intensity.\",\"root_display\":\"{{ar:ش ه د}} ({{tr:sh-h-d}})\",\"root_gloss_range\":\"root range centered on presence, witnessing, seeing, and testifying from knowledge, with farther branches such as attestation formula, martyrdom, visible signs, and nonlocal lexical byways; the local noun selects the witness/testimony field\",\"surface_display\":\"{{ar:شَهِيدٌۭ}} ({{tr:shahīdun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:3:delayed-predicate-frame","source_type":"word_analysis","support_id":"sup_acf9a1fb778116e8149b","text":"{\"blocking_evidence\":null,\"headline\":\"fronted phrase delays the witness landing\",\"reader_payoff\":\"The reader notices the clause making the evidentiary matter audible before naming the witness role.\",\"reason\":\"The prepositional phrase intervenes between {{ar:إِنَّهُۥ}} ({{tr:innahū}}) and the predicate {{ar:لَشَهِيدٌۭ}} ({{tr:la-shahīdun}}).\",\"representative_source_ids\":[\"QT-ad1fd4b7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:1:simultaneous-witnessing-shade","source_type":"word_analysis","support_id":"sup_ae34dab2e2638cb0c757","text":"{\"blocking_evidence\":null,\"headline\":\"coordination keeps simultaneity audible\",\"reader_payoff\":\"The reader notices that the witness relation can press into the same moment as the ingratitude, so awareness is not merely later commentary.\",\"reason\":\"The circumstantial reading is meaningful as a shade of the connector, but the guardrail grammar names the main local function as coordination between two emphatic assertions.\",\"representative_source_ids\":[\"MG-cc95c0e5\",\"QS-d75141e6\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:6:active-primary-passive-undertone","source_type":"word_analysis","support_id":"sup_c7be7dfa644608d80719","text":"{\"blocking_evidence\":null,\"headline\":\"active witness with exposed undertone\",\"reader_payoff\":\"The reader notices that the subject is primarily the witness while the same wording also sharpens exposure: the matter witnessed is on display.\",\"reason\":\"The active witness reading fits the predicate and distributional guardrails best, while the passive undertone remains a marked pressure rather than a replacement of the local parse.\",\"representative_source_ids\":[\"QS-1701b645\",\"MF-17205012\",\"QI-0aa44927\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:5","source_type":"word_analysis","support_id":"sup_d1d6f7dca191e4f6fb29","text":"{\"gloss_range\":\"predicate lām of emphasis attached to the witness noun; confirms the khabar and makes the final predicate arrive with asserted certainty\",\"prose\":\"{{ar:لَ}} ({{tr:la-}}) is not a separate lexical topic; it is the emphatic prefix that makes {{ar:لَشَهِيدٌۭ}} ({{tr:la-shahīdun}}) arrive as a confirmed predicate. Together with {{ar:إِنَّهُۥ}} ({{tr:innahū}}), it builds a double-emphasis frame, so the witness statement is heard as a verdict resistant to denial. Its attachment also matters audibly: the certainty marker enters the same pronounced shape as the witness noun and lands after the intervening phrase.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَ}} ({{tr:la-}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:4:fronted-pointer-before-predicate","source_type":"word_analysis","support_id":"sup_d8c858bab51c90caa968","text":"{\"blocking_evidence\":null,\"headline\":\"the pointer arrives before the predicate\",\"reader_payoff\":\"The reader notices the demonstrative's fused pointing, distance, and address before the final witness noun supplies the role.\",\"reason\":\"The demonstrative phrase precedes {{ar:لَشَهِيدٌۭ}} ({{tr:la-shahīdun}}), so the pointed matter is heard before the predicate resolves the clause.\",\"representative_source_ids\":[\"QF-d7ae6f9d\",\"QT-541ef564\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:5:delayed-khabar-arrival","source_type":"word_analysis","support_id":"sup_eaeedacce454e9c7c9d9","text":"{\"blocking_evidence\":null,\"headline\":\"lām marks the delayed predicate\",\"reader_payoff\":\"The reader notices that the final noun lands as a structurally marked arrival after the subject and evidentiary phrase.\",\"reason\":\"The lām appears on the predicate after the intervening phrase and carries the emphatic pattern already present in the prior assertion.\",\"representative_source_ids\":[\"QT-3f752306\",\"QB-078f08c9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:6:shahid-shadid-forward-echo","source_type":"word_analysis","support_id":"sup_f2d1142055c132f3e30f","text":"{\"blocking_evidence\":null,\"headline\":\"witness sound carries into intensity\",\"reader_payoff\":\"The reader notices that the witness predicate does not close the movement completely; its sh-opening, long -i- cadence, and final d prepare the intense predicate of 100:8.\",\"reason\":\"The CRITICAL rows give the concrete next-ayah echo between {{ar:شَهِيدٌۭ}} ({{tr:shahīdun}}) in 100:7 and the intense predicate in 100:8.\",\"representative_source_ids\":[\"QE-3e4de6c1\",\"QE-bb74aaff\",\"QP-27d9a601\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:3:relation-to-evidence-shift","source_type":"word_analysis","support_id":"sup_fc89811686160b15faa8","text":"{\"blocking_evidence\":null,\"headline\":\"relation becomes evidence\",\"reader_payoff\":\"The reader notices the movement from relational failure in 100:6 into a witness-position in 100:7.\",\"reason\":\"The preposition helps convert the prior charge into the object of testimony without introducing a new entity.\",\"representative_source_ids\":[\"QB-fec998a4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:6:governed-witness-domain","source_type":"word_analysis","support_id":"sup_fd39b11b749dbfd37098","text":"{\"blocking_evidence\":null,\"headline\":\"witnesshood is tied to that matter\",\"reader_payoff\":\"The reader notices that the word does not name a general witness role; the testimony is fixed to the pointed matter of 100:6.\",\"reason\":\"Attachment evidence links {{ar:عَلَىٰ ذَٰلِكَ}} ({{tr:ʿalā dhālika}}) to the witness predicate as the matter over which it applies.\",\"representative_source_ids\":[\"QG-1da2773e\",\"QG-4cae0b92\",\"QI-5e3c4004\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:7:4:governed-evidentiary-object","source_type":"word_analysis","support_id":"sup_fe9c4d0b50d47678941a","text":"{\"blocking_evidence\":null,\"headline\":\"that becomes the witness matter\",\"reader_payoff\":\"The reader notices that the clause stages an evidentiary object, not merely a witness in the abstract.\",\"reason\":\"The demonstrative is governed by {{ar:عَلَىٰ}} ({{tr:ʿalā}}), and attachment evidence says it points back to the preceding predication rather than introducing a new entity.\",\"representative_source_ids\":[\"QG-133c8741\",\"QT-e03e3f45\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌۭ","ayah_ref":"100:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000822/B001"],"payload":{"activation_trace":[{"assigned_role":"Grounds the subject's witness-role in firsthand presence rather than hearsay.","branch_id":"B001","branch_image_ar":"الحضور مع المشاهدة","literal_contribution":"Presence together with direct witnessing or seeing.","mapped_root_id":"root_000822","mapped_root_norm":"ش ه د","root":"ش ه د","source_phrase_ar":"شَهِيدٌ","source_ref":"100:7"}],"changed_reading":{"after":"The subject is present to the matter indicated by ذَٰلِكَ and witnesses it from direct proximity.","before":"An unspecified subject is called a witness concerning an unspecified matter."},"confidence":"strong","focus_anchor":"شَهِيدٌ, root ش ه د, through root_000822/B001; the construction عَلَىٰ ذَٰلِكَ places the pronominal subject in an evidentiary relation to an unspecified matter.","mechanism":"The witness is present with the matter and sees it directly. Its force comes from participation or immediate observation, not from receiving a report.","model_id":"BSL-01-direct-presence","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:BSL-01-direct-presence","source_type":"hft","support_id":"sup_25e5057ab0e14e70f1ff","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌۭ","ayah_ref":"100:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000822/B002"],"payload":{"activation_trace":[{"assigned_role":"Makes the subject a bearer and discloser of evidence concerning ذَٰلِكَ.","branch_id":"B002","branch_image_ar":"البيان بعلم","literal_contribution":"A statement, acknowledgement, or decisive report made from knowledge.","mapped_root_id":"root_000822","mapped_root_norm":"ش ه د","root":"ش ه د","source_phrase_ar":"شَهِيدٌ","source_ref":"100:7"}],"changed_reading":{"after":"The subject bears articulate, knowledge-based testimony concerning that matter.","before":"The predicate may mean only that the subject has seen something."},"confidence":"strong","focus_anchor":"شَهِيدٌ, root ش ه د, through root_000822/B002, with عَلَىٰ ذَٰلِكَ supplying the matter about or against which testimony bears.","mechanism":"Knowledge is converted into a decisive declaration, acknowledgement, or proof-bearing judgment. The witness does not merely perceive; it makes what is known evidentially available.","model_id":"BSL-02-knowledge-testimony","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:BSL-02-knowledge-testimony","source_type":"hft","support_id":"sup_ae566337038aa36c8eb4","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌۭ","ayah_ref":"100:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000822/B005"],"payload":{"activation_trace":[{"assigned_role":"Shifts testimony from a courtroom-like utterance to self-disclosing expression.","branch_id":"B005","branch_image_ar":"اللسان الشاهد","literal_contribution":"A tongue or visible expression that reveals its owner.","mapped_root_id":"root_000822","mapped_root_norm":"ش ه د","root":"ش ه د","source_phrase_ar":"شَهِيدٌ","source_ref":"100:7"}],"changed_reading":{"after":"The subject's own expression can speak evidentially about the subject, even before deliberate confession.","before":"The subject deliberately reports what it knows."},"confidence":"medium","focus_anchor":"شَهِيدٌ, root ش ه د, through root_000822/B005; this branch allows a tongue or outward expression to stand as its owner's witness.","mechanism":"An expression can testify about its source independently of a formal declaration. The subject's outward articulation is therefore capable of exposing the subject.","model_id":"BSL-03-visible-expression","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:BSL-03-visible-expression","source_type":"hft","support_id":"sup_290a4a96d70f18eb2229","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌۭ","ayah_ref":"100:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000822/B008"],"payload":{"activation_trace":[{"assigned_role":"Allows the subject itself to be evidence of the matter designated by ذَٰلِكَ.","branch_id":"B008","branch_image_ar":"العلامة الشاهدة","literal_contribution":"A visible sign that testifies to a time, state, or quality.","mapped_root_id":"root_000822","mapped_root_norm":"ش ه د","root":"ش ه د","source_phrase_ar":"شَهِيدٌ","source_ref":"100:7"}],"changed_reading":{"after":"The subject can be a standing evidentiary sign whose condition testifies without a separate speech act.","before":"Witnesshood is a conscious act of seeing or speaking."},"confidence":"medium","focus_anchor":"شَهِيدٌ, root ش ه د, through root_000822/B008; the nominal predicate can characterize the subject as an enduring sign of a condition or quality.","mechanism":"A visible condition functions indexically: it points beyond itself to the state that produced it. Witnesshood can thus reside in what the subject is or displays, not only in what the subject says.","model_id":"BSL-04-witnessing-sign","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:BSL-04-witnessing-sign","source_type":"hft","support_id":"sup_d1d7ccfa40709322258c","trust":"legacy_unbound"}]}
</lane_packet_json>
