# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **100:9**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s100-regular-20260911/s100/100_9/micro.discovery.json` and modify nothing
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
  "ayah_ref": "100:9",
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
{"analysis_context":{"analysis_id":"s100-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"100:9","host_surah":100,"lane_context_refs":[],"ordered_context_refs":["100:0","100:1","100:2","100:3","100:4","100:5","100:6","100:7","100:8","100:10","100:11","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Bu dal genel bir dağıtma ya da yıkma eylemini değil, toprağı çevirerek gömülü veya örtülü olanı ortaya çıkarma eylemini anlatır.","branch_kind":"bare","branch_ref":"root_000130/B001","candidate_links":[{"candidate_id":"cand_cf7e3bede216562d291f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"بُعْثِرَ","morph_features":"STEM|POS:V|PERF|PASS|LEM:buEovira|ROOT:bEvr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:9:4:1","qac_word_ref":"100:9:4","surface_ar":"بُعْثِرَ"}],"gloss":"toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gömülü şeyin üzerindeki toprak çevrilip kaldırılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Mezarlardakiler yerinden kaldırılıp dışarı çıkarılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Örtülü veya saklı bir şey çıkarılarak görünür duruma getirilir."}}],"root_ar":"ب ع ث ر","root_id":"root_000130","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İlk bölüm toprağı çevirip gömülüyü çıkarma çekirdeğini, ikinci bölüm ise toprak koşulu taşımayan genel çıkarıp açığa kavuşturma uzantısını karşılar.","boundary_detail":"Bu dal genel bir dağıtma ya da yıkma eylemini değil, toprağı çevirerek gömülü veya örtülü olanı ortaya çıkarma eylemini anlatır.","branch_image_ar":"قلب التراب وكشف المدفون","concept_gloss":"toprağı çevirip gömülüyü çıkarma; bir şeyi çıkarıp açığa kavuşturma","contextual_glosses":[{"applicability":"Gömülü bir nesnenin üstündeki toprağın karıştırılıp kaldırıldığı somut bir anlatımda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Mezarlardakilerin topluca dışarı çıkarılması ile genel olarak örtülü bir şeyi açığa çıkarma uzantısını açıkça söylemez.","preserves":"Toprağı hareket ettirerek gömülü şeyi ortaya çıkarma işlemini korur."},"facet_ids":["F001"],"text":"toprağı eşeleyip ortaya çıkarmak","usage_role":"contextual"}],"definition":"Bir şeyin üzerindeki toprağı altüst edip onu gömülü olduğu yerden çıkarmak ve mezardakileri dışarı almak; ayrıca daha genel olarak bir şeyi çıkarıp açığa kavuşturmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gömülü şeyin üzerindeki toprak çevrilip kaldırılır."},{"facet_id":"F002","role":"specialization","statement":"Mezarlardakiler yerinden kaldırılıp dışarı çıkarılır."},{"facet_id":"F003","role":"extension","statement":"Örtülü veya saklı bir şey çıkarılarak görünür duruma getirilir."}],"identity_rationale":"Kaynak ifadesi, gömülü olanın üstündeki toprağı çevirip kaldırmayı, mezarlardakileri yerinden çıkarıp dışarı almayı ve örtülü bir şeyi açığa çıkarmayı birlikte bildirir. Verilen dal çerçevesi bu işlem dizisini ve ortaya çıkarma sonucunu doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"toprağı altüst edip gömülüyü ortaya çıkarmak; örtülü şeyi çıkarıp açığa kavuşturmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"gömülüyü ortaya çıkarmak için toprağı altüst etme"}],"lexicalization_note":"Tanım yalın eylemin kapsamını verir; eşya dağıtma ve havuz yıkma gibi yalnızca belirli yapılarda görülen anlamlar bu dala katılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; gizliyi ortaya çıkarma dalı ile iki kardeş dal sınırı keskinleştirdi. Kalan adaylar mezar, gömme, yok olma veya ilgili nesneler bakımından yalnızca uzak alan ortaklığı taşıdığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal genel çıkarıp açığa kavuşturma uzantısını komşuyla paylaşır, ancak özel çekirdeğinde toprağı çevirip gömülüyü veya mezardakileri çıkarır. Komşu dal gizliliği kaldırmayı toprak işleminden bağımsız biçimde daha geniş tutar ve başka çıkarma kullanımlarına da uzanır.","focus_only":"Dal genel çıkarıp açığa kavuşturmayı da kapsar; ayırt edici özel çekirdeğinde ise toprak çevrilerek gömülü olan veya mezardakiler çıkarılır.","gloss":"gizliyi ortaya çıkarma","neighbor_only":"Gizliliği kaldırma, bir şeyi yerinden çıkarmadan yalnız görünür kılmaya ve yağmurun canlıları yuvalarından çıkarması gibi başka çıkarma durumlarına da uzanır.","neighbor_ref":"root_000428/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi çıkarıp açığa kavuşturma uzantısında örtüşür."},{"boundary_match":"partial","distinction":"Bu dalın sonucu gömülünün açığa çıkmasıdır. Komşu dal ise yalnız eşya üzerinde gerçekleşen dağıtma ve parçaları üst üste çevirme işlemidir; saklı bir şeyi çıkarma içermez.","focus_only":"Toprak gömülü şeyin üzerinden kaldırılır ve saklı olan açığa çıkarılır.","gloss":"eşyayı dağıtıp altüst etme","neighbor_only":"Eşyalar birbirinden ayrılır, dağıtılır ve parçaları birbirinin üstüne çevrilir.","neighbor_ref":"root_000130/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da bir düzeni bozacak biçimde çevirme ve yer değiştirme görüntüsü vardır."},{"boundary_match":"partial","distinction":"Bu dalda çevirme, toprağın altındakini açığa çıkaran araçtır ve nesnenin yok edilmesini gerektirmez. Komşu dalda ise havuzun yıkılması ve altının üste gelmesi doğrudan sonuçtur.","focus_only":"Toprağın çevrilmesi, altındaki gömülü veya örtülü şeyi ortaya çıkarır.","gloss":"havuzu yıkıp tersine çevirme","neighbor_only":"Havuz yıkılır ve yapının alt bölümü üste gelecek biçimde tersine çevrilir.","neighbor_ref":"root_000130/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da altı üstüne getiren güçlü bir çevirme işlemi bulunur."}],"source_phrase_ar":"بعثره بعثرة إذا قلب التراب عنه (ayn)؛ بعثر ما في القبور أثير وأخرج؛ بعثرت الشيء إذا استخرجته وكشفته (sihah)؛ قلب ترابها وأثير ما فيها (mufradat)","source_summary":"Kaynak dizisi, toprağı çevirerek gömülüyü ve mezardakileri çıkarma çekirdeğinin yanında, aynı ayrıntıları zorunlu kılmadan bir şeyi çıkarıp açığa kavuşturan daha genel bir uzantı da verir.","sources":["AY","SI","MU"],"what_is_ar":"يدخل فيه قلب التراب عن الشيء المدفون وإثارة ما في القبور وإخراجه وكشف الشيء المستور","what_is_not_ar":"ليس تفريق المتاع وتبديده ولا هدم الحوض بجعل أسفله أعلاه"},"support_links":["sup_2ac542177bd28ea0dfdb"]},{"boundary":"Bu anlam yalnız eşya üzerinde kurulan kullanımda geçerlidir; genel dağıtma anlamına veya gömülü olanı açığa çıkarma dalına genişletilemez.","branch_kind":"collocation","branch_ref":"root_000130/B002","candidate_links":[{"candidate_id":"cand_24cddf9c024e1c3acc80","lane":"micro"},{"candidate_id":"cand_d31695c8ece2465a1236","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"بُعْثِرَ","morph_features":"STEM|POS:V|PERF|PASS|LEM:buEovira|ROOT:bEvr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:9:4:1","qac_word_ref":"100:9:4","surface_ar":"بُعْثِرَ"}],"gloss":"eşyayı dağıtıp altüst etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eşyalar birbirinden ayrılarak çeşitli yönlere dağıtılır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eşyanın parçaları birbirinin üstüne gelecek biçimde çevrilip altüst edilir."}}],"root_ar":"ب ع ث ر","root_id":"root_000130","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eşyanın hem ayrılıp dağıtıldığı hem de parçalarının birbirinin üstüne çevrildiği kullanımı eksiksiz karşılar.","boundary_detail":"Bu anlam yalnız eşya üzerinde kurulan kullanımda geçerlidir; genel dağıtma anlamına veya gömülü olanı açığa çıkarma dalına genişletilemez.","branch_image_ar":"تبديد المتاع وقلب بعضه على بعض","concept_gloss":"eşyayı dağıtıp altüst etme","contextual_glosses":[{"applicability":"Eşyanın düzensiz biçimde dağıtıldığı bir olayın akıcı anlatımında kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Parçaların birbirinin üstüne gelecek biçimde çevrilmesini açıkça belirtmez.","preserves":"Eşyanın dağıtılması ve önceki düzeninin bozulması yönlerini korur."},"facet_ids":["F001"],"text":"eşyasını darmadağın etmek","usage_role":"contextual"}],"definition":"Bir kimsenin eşyasını birbirinden ayırıp dağıtması ve parçalarını birbirinin üstüne gelecek biçimde altüst etmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eşyalar birbirinden ayrılarak çeşitli yönlere dağıtılır."},{"facet_id":"F002","role":"core","statement":"Eşyanın parçaları birbirinin üstüne gelecek biçimde çevrilip altüst edilir."}],"identity_rationale":"Kaynak ifadesi bir kimsenin eşyasını birbirinden ayırmasını, dağıtmasını ve parçalarını birbirinin üstüne gelecek biçimde çevirmesini açıkça birlikte verir. Dal çerçevesi bu üç bileşeni korur ve kullanımı belirtilen nesneyle sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"eşyasını ayırıp dağıtmak ve parçalarını birbirinin üstüne gelecek biçimde altüst etmek"}],"lexicalization_note":"Tanım yalnız eşya üzerinde kurulan yapıya bağlıdır; dağıtma ve altüst etme bileşimi yalın eylemin genel anlamı gibi sunulmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yayma ve tohum saçma dalları ile iki kardeş dal en yararlı sınırları verdi. Kalan adaylar dağılma, eşya veya alma alanını paylaşsa da işlem bileşimini daha iyi açıklamadığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal eşya ile sınırlıdır ve dağıtmaya parçaları birbirinin üstüne çevirme işlemini ekler. Komşu dal daha geniş nesne ve olaylara yayılır, fakat bu özel altüst etme koşulunu gerektirmez.","focus_only":"Eşyayı dağıtırken parçaları birbirinin üstüne çevirmek de anlamın gerekli bir parçasıdır.","gloss":"nesneleri dağıtıp yayma","neighbor_only":"Dağıtma çok çeşitli nesnelere, canlı kümelerine ve yayılma olaylarına uzanır.","neighbor_ref":"root_000083/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir arada bulunan şeyleri ayırıp çevreye dağıtmayı içerir."},{"boundary_match":"partial","distinction":"Bu dalın nesnesi eşyadır ve altüst etme bileşeni zorunludur. Komşu dalın belirgin örneği tohumu ekmek için saçmaktır; parçaları üst üste çevirme içermez.","focus_only":"Eşya dağıtılırken parçaları da birbirinin üstüne gelecek biçimde çevrilir.","gloss":"tohumu saçıp dağıtma","neighbor_only":"Tohum ekmek amacıyla saçılabilir ve dağıtma belirli bir üretim amacına bağlı olabilir.","neighbor_ref":"root_000098/B001","relation_type":"near_neighbor","shared_zone":"İki dal da çok sayıdaki parçayı bulundukları yerden ayırıp çeşitli yönlere dağıtabilir."},{"boundary_match":"partial","distinction":"Bu dal eşyanın dağıtılmasıyla sonuçlanır; saklı bir şeyi bulup çıkarma amacı taşımaz. Komşu dalda toprak çevirme, gömülünün açığa çıkarılmasına hizmet eder.","focus_only":"Eşya parçaları ayrılır, dağıtılır ve birbirinin üstüne çevrilir.","gloss":"gömülüyü ortaya çıkarma","neighbor_only":"Toprak kaldırılarak gömülü veya örtülü olan şey yerinden çıkarılıp açığa kavuşturulur.","neighbor_ref":"root_000130/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da nesnelerin önceki yerleşimini bozan bir çevirme hareketi bulunur."},{"boundary_match":"partial","distinction":"Bu dal çok parçalı eşyanın dağıtılmasına bağlıdır. Komşu dal dağıtmayı değil, havuzun yıkılıp altının üste getirilmesini anlatır.","focus_only":"Bir eşya topluluğu ayrılıp dağıtılır ve parçaları birbirinin üstüne çevrilir.","gloss":"havuzu yıkıp altını üste getirme","neighbor_only":"Tek bir havuz yapısı yıkılır ve alt bölümü üste gelecek biçimde bütünüyle ters çevrilir.","neighbor_ref":"root_000130/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir düzeni bozup parçaların veya bölümlerin konumunu tersine çevirir."}],"source_phrase_ar":"بعثر الرجل متاعه وبحثره إذا فرقه وبدده وقلب بعضه على بعض","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, eşyanın ayrılıp dağıtılmasını ve parçalarının birbirinin üstüne çevrilmesini birlikte verir."}],"source_summary":"Bu dal genel bir dağıtmayı değil, eşya üzerinde gerçekleşen dağıtma ve altüst etme bileşimini anlatır.","sources":["SI"],"what_is_ar":"يدخل فيه تفريق المتاع وتبديده وقلب بعضه على بعض","what_is_not_ar":"ليس استخراج المدفون وكشفه ولا قلب تراب القبور"},"support_links":["sup_8be49e51a89e2d628b74","sup_d11e43af5856b12e3d7e"]},{"boundary":"Bu anlam havuz üzerinde kurulan kullanıma bağlıdır; genel yıkılma, eşya dağıtma veya toprağı çevirme anlamı değildir.","branch_kind":"collocation","branch_ref":"root_000130/B003","candidate_links":[{"candidate_id":"cand_24cddf9c024e1c3acc80","lane":"micro"},{"candidate_id":"cand_55a67f901f4baabb49c0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"بُعْثِرَ","morph_features":"STEM|POS:V|PERF|PASS|LEM:buEovira|ROOT:bEvr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:9:4:1","qac_word_ref":"100:9:4","surface_ar":"بُعْثِرَ"}],"gloss":"havuzu yıkıp altını üste çevirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Havuzun yapısı yıkılarak bütünlüğü ortadan kaldırılır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yıkılan havuzun alt bölümü üste gelecek biçimde ters çevrilir."}}],"root_ar":"ب ع ث ر","root_id":"root_000130","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir havuzun hem yıkıldığı hem de alt bölümünün üste gelecek biçimde tersine çevrildiği kullanımın tamamını karşılar.","boundary_detail":"Bu anlam havuz üzerinde kurulan kullanıma bağlıdır; genel yıkılma, eşya dağıtma veya toprağı çevirme anlamı değildir.","branch_image_ar":"هدم الحوض وقلب أسفله أعلاه","concept_gloss":"havuzu yıkıp altını üste çevirme","contextual_glosses":[{"applicability":"Havuzun yapısının bütünüyle bozulduğu ve bölümlerinin ters konuma geldiği bir olay anlatımında doğal bir karşılıktır.","error_profile":{"adds":"Yerle bir etme sözü, kaynakta zorunlu olmayan tam düzleşme veya daha ileri ölçüde yok olma izlenimi ekleyebilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Havuzu yıkma ve yapıyı ters konuma getirme bileşenlerini korur."},"facet_ids":["F001","F002"],"text":"havuzu yerle bir edip ters çevirmek","usage_role":"contextual"}],"definition":"Bir havuzu yıkmak ve yapının alt bölümünü üste gelecek biçimde tersine çevirmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Havuzun yapısı yıkılarak bütünlüğü ortadan kaldırılır."},{"facet_id":"F002","role":"core","statement":"Yıkılan havuzun alt bölümü üste gelecek biçimde ters çevrilir."}],"identity_rationale":"Kaynak ifadesi havuzun yıkılmasını ve alt bölümünün üste gelecek biçimde çevrilmesini aynı kullanımın iki kurucu parçası olarak verir. Dal çerçevesi hem yıkma işlemini hem de ortaya çıkan ters dönmüş durumu doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"havuzunu yıkıp alt bölümünü üste gelecek biçimde ters çevirmek"}],"lexicalization_note":"Tanım yalnız havuz üzerinde kurulan yapıyı kapsar; yıkıp altını üste getirme anlamı yalın eyleme veya bütün yapılara genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yıkma dalları, iki kardeş dal ve havuzun kendisini adlandıran dal en açıklayıcı karşılaştırmaları sağladı. Kalan adaylar çökme, yarılma, çukur veya havuz bölümü gibi yalnızca yakın alanları paylaştığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yalnız havuzun yıkılıp altının üste getirilmesini anlatır. Komşu dalın yıkma ve çöküş alanı daha geniştir ve ters çevirme sonucunu zorunlu kılmaz.","focus_only":"Yıkılan nesne havuzdur ve alt bölümünün üste getirilmesi zorunlu sonuçtur.","gloss":"yapıyı yıkıp dayanağını bozma","neighbor_only":"Yıkma ev ve başka nesnelere, kendiliğinden çöküşe ve düzen ya da saygınlık kaybına uzanabilir.","neighbor_ref":"root_000204/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da bir yapının bütünlüğünü bozarak onu ayakta tutan düzeni ortadan kaldırır."},{"boundary_match":"partial","distinction":"Bu dal nesne olarak havuzu ve sonuç olarak altın üste gelmesini şart koşar. Komşu dal şiddetli kırma ve yıkmayı daha geniş nesnelere uygular, fakat ters dönmeyi gerektirmez.","focus_only":"Havuzun alt bölümünün üste gelecek biçimde çevrilmesi yıkmanın kurucu sonucudur.","gloss":"şiddetle kırıp yıkma","neighbor_only":"Şiddetli kırma ve yıkma duvar, bina, dağ ve dayanak gibi çok çeşitli nesnelere uygulanabilir.","neighbor_ref":"root_001580/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da sağlam bir yapıyı güçlü biçimde bozup yıkmayı içerir."},{"boundary_match":"partial","distinction":"Bu dalda çevirme, havuzun yıkılmasıyla birlikte doğrudan sonuçtur. Komşu dalda ise toprağı çevirme, saklı olanı ortaya çıkarmaya yarar ve bir yapıyı yıkmayı gerektirmez.","focus_only":"Havuz yıkılır ve alt bölümü üste gelecek biçimde tersine çevrilir.","gloss":"toprağı çevirip gömülüyü çıkarma","neighbor_only":"Toprak çevrilip kaldırılarak altındaki gömülü veya örtülü şey açığa çıkarılır.","neighbor_ref":"root_000130/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da alt ve üst konumlarını değiştiren güçlü bir çevirme görüntüsü vardır."},{"boundary_match":"partial","distinction":"Bu dal havuzun yıkılmasına ve ters dönmesine bağlıdır. Komşu dalda yapısal yıkım yoktur; eşyanın ayrılması, dağıtılması ve üst üste çevrilmesi vardır.","focus_only":"Tek bir havuz yapısı yıkılır ve altı üste gelecek biçimde ters çevrilir.","gloss":"eşyayı dağıtıp altüst etme","neighbor_only":"Çok parçalı eşya birbirinden ayrılır, dağıtılır ve parçaları birbirinin üstüne çevrilir.","neighbor_ref":"root_000130/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da önceki düzeni bozarak bölümlerin veya parçaların konumunu değiştirir."},{"boundary_match":"thematic_only","distinction":"Bu dal havuz üzerinde gerçekleştirilen yıkıcı bir işlemi bildirir. Komşu dal ise suyu toplamak için kullanılan yapının kendisini adlandırır; yıkma veya ters çevirme anlamı taşımaz.","focus_only":"Bir havuzun yıkılması ve alt bölümünün üste gelecek biçimde çevrilmesi anlatılır.","gloss":"su biriktirme havuzu","neighbor_only":"Suyun toplandığı geniş bir havuz veya su biriktirme yeri bir nesne olarak adlandırılır.","neighbor_ref":"root_000016/B007","relation_type":"thematic","shared_zone":"İki dal aynı tür su yapısını konu edinir."}],"source_phrase_ar":"بعثرت حوضي أي هدمته وجعلت أسفله أعلاه","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, havuzu yıkma eylemini yapının altını üste getirme sonucuyla birlikte bildirir."}],"source_summary":"Bu dal, havuzun yıkılmasını ve altının üste getirilmesini birbirinden ayrılmaz iki sonuç olarak birleştirir.","sources":["SI"],"what_is_ar":"يدخل فيه هدم الحوض وجعل أسفله أعلاه","what_is_not_ar":"ليس مجرد تفريق المتاع ولا إخراج ما في القبور"},"support_links":["sup_1da28a5555193d9c8027","sup_8be49e51a89e2d628b74"]},{"boundary":"Çekirdek, bir şeyi bilme ve gerçeğiyle kavramadır; bildirme, öğretme, öğrenme ve bilgi yarışında yenme ayrı biçimlere bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001040/B001","candidate_links":[{"candidate_id":"cand_cf7e3bede216562d291f","lane":"micro"},{"candidate_id":"cand_24cddf9c024e1c3acc80","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:9:2:1","qac_word_ref":"100:9:2","surface_ar":"يَعْلَمُ"}],"gloss":"bilme ve gerçeğini kavrama","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi bilme, tanıma ve gerçeğine uygun biçimde kavrama durumu bilgisizliğin karşıtıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir haberin farkına varmak veya ondan haberdar olmak, bilme çekirdeğinin belirli bir konuya uygulanmasıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bildirme, öğretme ve öğrenme biçimleri bilginin bir başkasına ulaştırılması ya da kişinin onu edinmesi süreçlerini anlatır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Karşılıklı bilgi sınamasında birini yenmek, belirli bir kuruluşta ortaya çıkan rekabetçi kullanımdır."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bilgisizliğin karşıtı olan temel zihinsel edinimi, tanımayı ve gerçeğe uygun kavrayışı birlikte karşılar.","boundary_detail":"Çekirdek, bir şeyi bilme ve gerçeğiyle kavramadır; bildirme, öğretme, öğrenme ve bilgi yarışında yenme ayrı biçimlere bağlıdır.","branch_image_ar":"انكشاف الشيء للعارف","concept_gloss":"bilme ve gerçeğini kavrama","contextual_glosses":[{"applicability":"Bir olay veya gelişme hakkındaki haberin kişinin bilgisine ulaşması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Haberin farkına varma ve ondan bilgi edinme yönünü korur."},"facet_ids":["F002"],"text":"haberinden haberdar olmak","usage_role":"contextual"},{"applicability":"Bilginin tekrar ve yönlendirmeyle bir öğrenende yerleşmesini sağlayan öğretim bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilginin aktarılması ve öğrenende kalıcı bir sonuç oluşturması sürecini korur."},"facet_ids":["F003"],"text":"öğretmek ve öğrenmesini sağlamak","usage_role":"explanatory"},{"applicability":"İki kişi arasındaki bilgi sınamasında bir tarafın ötekini yenmesi bağlamına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilgi alanındaki karşılaştırmayı ve üstün gelme sonucunu korur."},"facet_ids":["F004"],"text":"bilgide üstün gelmek","usage_role":"contextual"}],"definition":"Bir şeyi bilmek, tanımak ve onu gerçeğine uygun biçimde kavramak; böylece bilgisizlikten çıkmaktır. Haber verilmesi, öğretme, öğrenme ve bilgi bakımından üstün gelme bu çekirdekten hareket eden, belirli biçimlere bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi bilme, tanıma ve gerçeğine uygun biçimde kavrama durumu bilgisizliğin karşıtıdır."},{"facet_id":"F002","role":"extension","statement":"Bir haberin farkına varmak veya ondan haberdar olmak, bilme çekirdeğinin belirli bir konuya uygulanmasıdır."},{"facet_id":"F003","role":"associated_use","statement":"Bildirme, öğretme ve öğrenme biçimleri bilginin bir başkasına ulaştırılması ya da kişinin onu edinmesi süreçlerini anlatır."},{"facet_id":"F004","role":"associated_use","statement":"Karşılıklı bilgi sınamasında birini yenmek, belirli bir kuruluşta ortaya çıkan rekabetçi kullanımdır."}],"identity_rationale":"Dalın bilme ve bilgisizliğin karşıtı olma yönündeki çekirdeği kaynak ifadesiyle uyumludur. Ancak haberden haberdar olma, öğretme, öğrenme ve bilgi bakımından üstün gelme kullanımları bu çekirdekle aynı düzeyde değil, belirli biçimlere bağlı uzantılar olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bilgi; bir şeyi gerçeğiyle kavrama"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyi bilmek ve tanımak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"haberinden haberdar olmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bildirmek, haberdar etmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"öğretmek, öğrenmesini sağlamak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"öğrenmek, kavramaya yönelmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bilmek; buyrukta bil ki"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bilgi yarışında yenmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bilen ve bildiğine göre davranan kişi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bilgili, bilgi sahibi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"çok bilgili, çok bilen"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"son derece bilgili kişi"}],"lexicalization_note":"Tanım çıplak bilme çekirdeğini öne alır; haber, öğretim, öğrenim ve karşılıklı bilgi sınamasıyla ilgili anlamları yalnızca ilgili biçim ve kuruluşlara bağlar.","neighbor_coverage_note":"Bilme çekirdeğini en çok açıklayan yakın kavrayış dalı, açık karşıtı olan bilgisizlik dalı ve doğru kullanım boyutu taşıyan bilgelik dalı seçildi; öteki adaylar yalnızca uzak çağrışım veya ayrı kök içi anlam alanı sunar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekleri yakın olsa da odak dalın biçime bağlı aktarım ve edinim süreçleri ile komşunun akletme ve hızlı anlama vurgusu karşılıklı değiştirilebilirliği sınırlar.","focus_only":"Odak dal, haberden haberdar etme, öğretme, öğrenme ve bilgi yarışında üstün gelme gibi biçime bağlı uzantıları da kapsar.","gloss":"bilmek ve anlamını kavramak","neighbor_only":"Komşu dal, anlamları doğrulama, akletme ve çabuk kavrama yönlerini ayrıca öne çıkarır.","neighbor_ref":"root_001182/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi bilme, tanıma ve zihnen kavrama alanında büyük ölçüde örtüşür."},{"boundary_match":"opposed","distinction":"Odak dal bilgiye erişmeyi ve kavramayı bildirirken komşu dal bu erişimin bulunmamasını ya da gerçeğin yanlış bilinmesini bildirir.","focus_only":"Bir şeyi tanıma, gerçeğine uygun kavrama ve bilgi sahibi olma bulunur.","gloss":"bilgi ile bilgisizlik karşıtlığı","neighbor_only":"Bilginin yokluğu, durumu tanımama veya gerçeğe aykırı bir kanaat bulunur.","neighbor_ref":"root_000271/B001","relation_type":"antonym","shared_zone":"İki dal aynı zihinsel erişim ekseninin olumlu ve olumsuz uçlarını gösterir."},{"boundary_match":"partial","distinction":"Bilmek tek başına odak dal için yeterli olabilir; komşu dal ise bilginin doğru yargı ve isabetli davranışla birleşmesini öne çıkarır.","focus_only":"Odak dalda yalın bilme ve tanıma, bilginin doğru kullanımından bağımsız olarak çekirdekte yer alabilir.","gloss":"bilgi ile bilgelik","neighbor_only":"Komşu dal doğruyu bulma, yerinde yargı ve bilgiyi isabetli kullanma niteliğini gerektirir.","neighbor_ref":"root_000348/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal bilgi sahibi olmayı ve zihinsel kavrayışı paylaşır."}],"source_phrase_ar":"العلم نقيض الجهل (maqayis;ayn;tahdhib)؛ علمت الشيء عرفته (sihah;tahdhib)؛ إدراك الشيء بحقيقته (mufradat)؛ ما علمت بخبرك أي ما شعرت به (ayn;tahdhib)؛ أعلمته بكذا وعلمته تعليما (ayn)؛ التعليم تنبيه النفس لتصور المعاني (mufradat)؛ تعلم بمعنى اعلم (maqayis;sihah;tahdhib)؛ عالمت الرجل فعلمته (sihah;tahdhib)","source_summary":"Kaynakların ortak çekirdeği, bilgiyi bilgisizliğin karşıtı sayar ve bir şeyi tanıyıp gerçeğiyle kavramayı öne çıkarır. Toplu tanıklık ayrıca haberden haberdar olmayı, bilgiyi aktarmayı, öğrenmeyi ve bilgiyle üstün gelmeyi biçime bağlı uzantılar olarak gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العلم نقيض الجهل وإدراك الشيء ومعرفته والشعور بالخبر والتعلم والتعليم والإعلام والمغالبة بالعلم","what_is_not_ar":"ليس هو العلامة الحسية ولا الجبل ولا الراية ولا الشق في الشفة ولا اسم العالمين"},"support_links":["sup_2ac542177bd28ea0dfdb","sup_8be49e51a89e2d628b74"]},{"boundary":"Dal bütün işaret türlerini sınırsızca kapsamaz; kaynakta anılan ayırt etme ve yol gösterme işlevli izlerle bunlara bağlı kullanımlarla sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001040/B002","candidate_links":[{"candidate_id":"cand_d31695c8ece2465a1236","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:9:2:1","qac_word_ref":"100:9:2","surface_ar":"يَعْلَمُ"}],"gloss":"ayırt edici ve yol gösterici işaret","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesneyi veya kişiyi başkalarından ayırıp tanınır kılan belirgin iz ya da işaret çekirdeği oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bayrak, belirgin dağ, yol belirtisi ve kumaşın kenar deseni yön bulduran veya tanıtan somut gerçekleşmelerdir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Savaşçının, kumaşın veya sarığın ayırt edici bir işaretle donatılması belirli kuruluşlara bağlı eylemsel kullanımdır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Tanınmış bir kişinin belirgin bir bayrağa benzetilmesi ve yaklaşan son zamanı gösteren belirti, işaret çekirdeğinin uzantılarıdır."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyi tanınır kılan veya ona ulaşmayı sağlayan belirgin iz ve işaretlerin ortak çekirdeğini karşılar.","boundary_detail":"Dal bütün işaret türlerini sınırsızca kapsamaz; kaynakta anılan ayırt etme ve yol gösterme işlevli izlerle bunlara bağlı kullanımlarla sınırlıdır.","branch_image_ar":"أثر يميز الشيء ويهدي إليه","concept_gloss":"ayırt edici ve yol gösterici işaret","contextual_glosses":[{"applicability":"Askerlerin çevresinde toplandığı bayrak ya da yol bulmayı sağlayan belirgin dağ ve iz bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Görünürlük ile yöneltme ve tanıtma işlevini korur."},"facet_ids":["F002"],"text":"bayrak veya uzaktan seçilen kılavuz","usage_role":"contextual"},{"applicability":"Bir savaşçıya, kumaşa veya sarığa başkalarından ayıran görünür bir belirti ekleme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşaretin sonradan konmasını ve ayırt etme amacını korur."},"facet_ids":["F003"],"text":"tanıtıcı işaret koymak","usage_role":"contextual"},{"applicability":"Belirli bir son zamanın yaklaştığını haber veren gösterge bağlamına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir olayın yakınlığını gösterme işlevini korur."},"facet_ids":["F004"],"text":"yaklaşmayı gösteren belirti","usage_role":"explanatory"}],"definition":"Bir şeyi başkalarından ayıran, tanınmasını sağlayan veya ona götüren belirgin iz ya da işarettir. Bayrak, uzaktan seçilen dağ, yol belirtisi, kumaş kenarı ve sonradan konan tanıtıcı izler bu işlevin farklı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesneyi veya kişiyi başkalarından ayırıp tanınır kılan belirgin iz ya da işaret çekirdeği oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Bayrak, belirgin dağ, yol belirtisi ve kumaşın kenar deseni yön bulduran veya tanıtan somut gerçekleşmelerdir."},{"facet_id":"F003","role":"associated_use","statement":"Savaşçının, kumaşın veya sarığın ayırt edici bir işaretle donatılması belirli kuruluşlara bağlı eylemsel kullanımdır."},{"facet_id":"F004","role":"extension","statement":"Tanınmış bir kişinin belirgin bir bayrağa benzetilmesi ve yaklaşan son zamanı gösteren belirti, işaret çekirdeğinin uzantılarıdır."}],"identity_rationale":"Kaynak ifadesi, bir şeyi başkasından ayıran belirgin izi dalın ortak çekirdeği olarak açıkça destekler. Bayrak, belirgin dağ, yol belirtisi, kumaş deseni ve savaş işareti gibi örnekler bu çekirdeğin farklı gerçekleşmeleridir; tanınmış kişi ve son zaman belirtisi ise benzetme veya gösterme ilişkisine bağlı uzantılardır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ayırt edici işaret"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bayrak, sancak"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yol gösteren belirgin dağ"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"kumaşın kenar işareti veya deseni"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yol gösteren iz veya belirti"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"savaşta kendine ayırt edici işaret takmak"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kumaşı işaretlemek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"işaret olarak kullanılan kına"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"sarığı tanıtıcı bir biçimde sarmak"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"tanınmış ve öne çıkan kişi"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"son saatin yaklaştığını gösteren belirti"}],"lexicalization_note":"Ayırt edici iz çıplak çekirdektir; savaşçı, kumaş, sarık ve belirli zaman göstergesiyle kurulan anlamlar kendi kuruluşlarına bağlı tutulur.","neighbor_coverage_note":"En yararlı karşılaştırmalar geçmişten kalan iz, bilerek konan tanıtıcı işaret ve fiziksel damga ile yapıldı; bayrak adayı yalnızca tek bir alt gerçekleşmeyi, öteki adaylar ise daha uzak renk veya biçim belirtilerini karşılar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda işaret önceden konabilir veya doğal bir kılavuz olabilir; komşu dalda iz, daha önceki bir varlık ya da olayın geride kalan sonucudur.","focus_only":"Odak dal, bilerek konan bayrak ve işaretlerin yanı sıra yön bulduran belirgin dağ gibi göstergeleri de kapsar.","gloss":"işaret ile kalıntı iz","neighbor_only":"Komşu dal, geçmişte var olmuş veya gerçekleşmiş bir şeyden geriye kalan izi özellikle gerektirir.","neighbor_ref":"root_000011/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da görünür bir izin başka bir şeyi tanıtması veya ona kanıt olması bakımından örtüşür."},{"boundary_match":"partial","distinction":"Komşu dalın çekirdeği işaretleme eylemine daha sıkı bağlıdır; odak dal ise konmuş işaretlerin yanında doğal kılavuzları ve bayrağı da adlandırır.","focus_only":"Odak dal doğal dağ işaretini, bayrağı, yol belirtisini ve kumaş kenarını da içine alan daha geniş bir gösterge alanına sahiptir.","gloss":"ayırt edici işaret koyma","neighbor_only":"Komşu dal özellikle atlara, varlıklara veya nesnelere tanıtma amacıyla işaret koyma eylemini öne çıkarır.","neighbor_ref":"root_000764/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir varlığı başkalarından ayıracak görünür bir işaretle tanıtmayı kapsar."},{"boundary_match":"partial","distinction":"Damga bir yüzeye bilerek bırakılan fiziksel izdir; odak dalın işareti ise doğal veya yapılmış olabilir ve yön gösterme işlevi de taşıyabilir.","focus_only":"Odak dal işaret koyma dışında bayrak, dağ, yol kılavuzu ve kumaş deseni gibi bağımsız adları da kapsar.","gloss":"işaret ile damga","neighbor_only":"Komşu dal, hayvana veya nesneye yakma, kesme ya da benzeri yolla bırakılan bedensel ve maddi damgayı gerektirir.","neighbor_ref":"root_001650/B001","relation_type":"near_synonym","shared_zone":"Her iki dal görünür bir belirti aracılığıyla tanıtma ve ayırt etme işlevini paylaşır."}],"source_phrase_ar":"أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره (maqayis)؛ العلامة وهي معروفة (maqayis)؛ العلم الراية والجمع أعلام (maqayis;sihah;tahdhib)؛ العلم الجبل الطويل والجميع الأعلام (ayn)؛ العلم الجبل (sihah;mufradat)؛ المعلم الأثر يستدل به على الطريق (sihah;tahdhib)؛ علم الثوب ورقمه في أطرافه (sihah;tahdhib;mufradat)؛ أعلم الفارس إذا كانت له علامة في الحرب (maqayis;sihah;tahdhib)؛ العلام الحناء (maqayis;sihah;tahdhib;mufradat)؛ علمت عمتي أعلمها علما (tahdhib)","source_summary":"Kaynaklar ayırt edici izi ortak temel sayar ve bayrak, yüksek ya da belirgin dağ, yol göstergesi, kumaş kenarı, kına ve sonradan yerleştirilen tanıtıcı işaretleri bu temelde toplar. Tanınmış kişi ile yaklaşan son zamanın belirtisi de görünürlük ve gösterme işlevinden doğan uzantılardır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العلامة والعلم والراية والجبل والمعلم ومعالم الطريق والحدود وعلم الثوب ورقمه وتعليم الفارس والثوب والقدح والعمامة والحناء إذا جعلت علامة","what_is_not_ar":"ليس هو إدراك العلم ولا اسم الخلق ولا شق الشفة العليا"},"support_links":["sup_d11e43af5856b12e3d7e"]},{"boundary":"Dal yaratılmış varlıkların bütünü veya sınıflarıyla sınırlıdır; bilme durumu ve bağımsız bir fiziksel işaret anlamına gelmez.","branch_kind":"bare","branch_ref":"root_001040/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:9:2:1","qac_word_ref":"100:9:2","surface_ar":"يَعْلَمُ"}],"gloss":"evren ve bütün yaratılmışlar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Evren ve içindeki yaratılmış varlıkların tamamı tek bir bütün olarak adlandırılır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ad, yaratılmışların tamamı yanında onların her bir cinsini veya sınıfını ayrı bir bütün olarak da gösterebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yaratılmış bütünün kendi yaratıcısına gösterge olması, adlandırmanın açıklayıcı dayanağı olarak sunulur."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaratılmış varlıkların tümünü tek bir düzen veya bütün olarak anlatan temel kullanım için uygundur.","boundary_detail":"Dal yaratılmış varlıkların bütünü veya sınıflarıyla sınırlıdır; bilme durumu ve bağımsız bir fiziksel işaret anlamına gelmez.","branch_image_ar":"الخلق عالم يدل على صانعه","concept_gloss":"evren ve bütün yaratılmışlar","contextual_glosses":[{"applicability":"Sözün bütün evren yerine insan, görünmeyen varlıklar veya başka bir yaratık cinsi gibi ayrı sınıflara dağıtıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Her yaratık cinsinin ayrı bir bütün sayılması yönünü korur."},"facet_ids":["F002"],"text":"varlıkların her bir sınıfı","usage_role":"explanatory"}],"definition":"Yaratılmış olanların bütünü; bağlama göre evren ile içindekilerin tamamı veya yaratıkların ayrı ayrı sınıflarıdır. Bu bütünün yaratıcıyı gösteren bir belirti sayılması, adın açıklanan dayanağıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Evren ve içindeki yaratılmış varlıkların tamamı tek bir bütün olarak adlandırılır."},{"facet_id":"F002","role":"source_variant","statement":"Ad, yaratılmışların tamamı yanında onların her bir cinsini veya sınıfını ayrı bir bütün olarak da gösterebilir."},{"facet_id":"F003","role":"associated_use","statement":"Yaratılmış bütünün kendi yaratıcısına gösterge olması, adlandırmanın açıklayıcı dayanağı olarak sunulur."}],"identity_rationale":"Kaynak ifadesi, dalı yaratılmışların bütünü, gök düzeni ve içindekiler ya da yaratıkların ayrı sınıfları olarak açıklar. Her sınıfın ve bütünün yaratıcıyı gösteren bir belirti sayılması adlandırmanın gerekçesidir; bilme eylemi veya somut işaret dalıyla özdeş değildir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"evren veya yaratılmışlar bütünü"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bütün yaratıklar veya varlık sınıfları"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"evrenler, varlık dünyaları"}],"lexicalization_note":"Tanım, çıplak dalın evren, yaratılmışların bütünü ve varlık sınıfları anlamlarını verir; başka kuruluşlardan anlam aktarmaz.","neighbor_coverage_note":"Adayların çoğu hayvan bedenindeki renk ve işaretleri ya da ilgisiz özel adları anlatır; aynı kökün bilme ve işaret dalları adlandırma gerekçesini açıklasa da bu dalın yaratılmışlar bütünü sınırını keskinleştirecek bir karşıtlık oluşturmaz.","source_phrase_ar":"العالمون كل جنس من الخلق فهو في نفسه معلم وعلم (maqayis)؛ العالم الخلق والجمع العوالم (sihah)؛ العالمين رب الجن والإنس ورب الخلق كلهم (tahdhib)؛ العالم اسم للفلك وما يحويه وهو في الأصل اسم لما يعلم به (mufradat)؛ أصناف الخلائق (mufradat)","source_summary":"Kaynaklar bu adı yaratılmışların bütünü için kullanır; kapsam bazen evren ve içindekilerin tamamı, bazen de yaratıkların her bir cinsi veya sınıfıdır. Bütünün kendi yaratıcısına işaret etmesi adlandırmayı açıklayan ortak bir düşüncedir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه العالم والعالمون بمعنى الخلق أو أصناف الخلائق أو كل جنس من الخلق لأنه معلم في نفسه ودال","what_is_not_ar":"ليس هو العلم بمعنى المعرفة ولا العلم بمعنى الراية أو الجبل"},"support_links":[]},{"boundary":"Belirti özellikle üst dudakta bulunur; genel çatlaklar, alt dudak ve ağız çevresindeki başka eğrilikler kapsam dışıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001040/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:9:2:1","qac_word_ref":"100:9:2","surface_ar":"يَعْلَمُ"}],"gloss":"üst dudak yarığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Üst dudakta bulunan yarık, dalın anatomik çekirdeğini oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Üst dudağı yarık insan veya üst dudak bölgesinde bu belirti bulunan deve, özelliği taşıyan varlık olarak nitelenir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birinin üst dudağını yarmak, anatomik sonucun oluşturulmasını bildiren eylemsel kullanımdır."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan veya devenin üst dudak bölgesindeki belirgin yarığı adlandıran temel kullanım için uygundur.","boundary_detail":"Belirti özellikle üst dudakta bulunur; genel çatlaklar, alt dudak ve ağız çevresindeki başka eğrilikler kapsam dışıdır.","branch_image_ar":"شق ظاهر في الشفة العليا","concept_gloss":"üst dudak yarığı","contextual_glosses":[{"applicability":"Bir insanı veya deveyi üst dudak bölgesindeki yarıkla niteleyen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Özelliğin taşıyıcıda bulunmasını ve anatomik yerini korur."},"facet_ids":["F002"],"text":"üst dudağı yarık","usage_role":"contextual"},{"applicability":"Bir kişinin üst dudağında yarık oluşturma eylemini anlatan kuruluşta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemi, etkilenen kişiyi ve üst dudak sınırını korur."},"facet_ids":["F003"],"text":"üst dudağını yarmak","usage_role":"contextual"}],"definition":"İnsanın üst dudağında veya devenin üst dudak bölgesinde bulunan belirgin yarıktır. Aynı dal, bu özelliği taşıyanı niteleyen biçimi ve üst dudağı yarma eylemini de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Üst dudakta bulunan yarık, dalın anatomik çekirdeğini oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Üst dudağı yarık insan veya üst dudak bölgesinde bu belirti bulunan deve, özelliği taşıyan varlık olarak nitelenir."},{"facet_id":"F003","role":"associated_use","statement":"Birinin üst dudağını yarmak, anatomik sonucun oluşturulmasını bildiren eylemsel kullanımdır."}],"identity_rationale":"Kaynak ifadesi dalı açıkça üst dudaktaki yarıkla sınırlar; insanın üst dudağının yarılmış olması, devenin üst dudak bölgesindeki aynı belirti ve üst dudağı yarma eylemi bu kimliği doğrular. Genel yarılma anlamı veya alt dudaktaki bir biçim bozukluğu bu dala dahil değildir.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"üst dudaktaki yarık"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"üst dudağı yarık kişi veya deve"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"üst dudağını yarmak"}],"lexicalization_note":"Üst dudak yarığı dalın temelidir; yarıklı kişi veya deve nitelemesi ile üst dudağı yarma eylemi ilgili biçimlere bağlı tutulur.","neighbor_coverage_note":"Genel yarılma dalı süreç ve kapsam farkını, ağız eğriliği dalı ise yakın anatomik karışmayı açıklar; öteki adaylar kırık iyileşmesi, hayvan yapısı veya daha uzak ayrılma türleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yer ve sonuç bakımından üst dudağa özelleşmiş anatomik bir addır; komşu dal ise nesne ve yüzey türü bakımından geniş bir yarılma eylemidir.","focus_only":"Odak dal belirli bir anatomik yerde, üst dudakta bulunan yarığı ve bu yarıkla niteleneni bildirir.","gloss":"üst dudak yarığı ile genel yarılma","neighbor_only":"Komşu dal nesne, deri, toprak, dağ ve başka yüzeylerdeki genel yarılma ve açılma sürecini kapsar.","neighbor_ref":"root_000807/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir yüzeyin ayrılmasıyla oluşan yarık düşüncesi bulunur."},{"boundary_match":"field_only","distinction":"Yarık, dokuda açılma veya ayrılmadır; eğrilik ise bir bölümün yana yönelmiş biçimidir ve üst dudakta bir açıklık gerektirmez.","focus_only":"Odak dalda üst dudak dokusunun yarılmış olması gerekir.","gloss":"dudak yarığı ile ağız eğriliği","neighbor_only":"Komşu dalda ağız, dudak veya gözün bir yana eğri oluşu vardır; doku yarığı gerekmez.","neighbor_ref":"root_000866/B003","relation_type":"same_field","shared_zone":"İki dal yüz ve ağız çevresindeki belirgin bir yapısal özelliği adlandırır."}],"source_phrase_ar":"العلم الشق في الشفة العليا والرجل أعلم (maqayis)؛ الأعلم الذي انشقت شفته العليا (ayn)؛ علم الرجل يعلم علما إذا صار أعلم وهو المشقوق الشفة العليا (sihah)؛ علمت الرجل أعلمه علما إذا شققت شفته العليا (tahdhib)؛ البعير يقال له أعلم لعلم في مشفره الأعلى (tahdhib)؛ الشق في الشفة العليا علم (mufradat)","source_summary":"Kaynaklar yarığın yerini üst dudak olarak ortak biçimde sınırlar ve yarıklı insanı bu özellikle niteler. Toplu tanıklık, devenin üst dudak bölgesindeki karşılığını ve üst dudağı yarma eylemini de aynı dalda gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العلم والشق في الشفة العليا ووصف الرجل أو البعير بالأعلم إذا كان الشق أو العلم في الموضع الأعلى","what_is_not_ar":"ليس هو العلم بمعنى المعرفة ولا العلامة الموضوعة اختيارا ولا الشق في الشفة السفلى"},"support_links":[]},{"boundary":"Deniz ile suyu bol kuyu tek bir ara nesnede birleştirilmez; bunlar aynı biçimin kaynaklarda verilen iki ayrı sözlük karşılığıdır.","branch_kind":"bare","branch_ref":"root_001040/B005","candidate_links":[{"candidate_id":"cand_55a67f901f4baabb49c0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:9:2:1","qac_word_ref":"100:9:2","surface_ar":"يَعْلَمُ"}],"gloss":"deniz ya da suyu bol kuyu","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dal, aynı adın iki ayrı su varlığına verilen sözlük karşılıklarını birlikte kaydeder."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kaynak karşılığında ad, geniş tuzlu su kütlesi olan denizi gösterir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Diğer ve daha yaygın kaynak karşılığında ad, suyu çok olan kuyuyu gösterir."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözlük biçiminin kaynaklarda verilen iki ayrı karşılığını eksiltmeden birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Deniz ile suyu bol kuyu tek bir ara nesnede birleştirilmez; bunlar aynı biçimin kaynaklarda verilen iki ayrı sözlük karşılığıdır.","branch_image_ar":"ماء كثير مجتمع في عيلم","concept_gloss":"deniz ya da suyu bol kuyu","contextual_glosses":[{"applicability":"Sözlük biçiminin geniş su kütlesi karşılığıyla kullanıldığı tanıklığa özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı biçim için tanıklanan suyu bol kuyu karşılığını dışarıda bırakır.","preserves":"Deniz karşılığını doğal ve doğrudan biçimde korur."},"facet_ids":["F002"],"text":"deniz","usage_role":"contextual"},{"applicability":"Sözlük biçiminin bol su içeren kuyu karşılığıyla kullanıldığı tanıklıklara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı biçim için tanıklanan deniz karşılığını dışarıda bırakır.","preserves":"Kuyu türünü ve suyunun çokluğu koşulunu korur."},"facet_ids":["F003"],"text":"suyu bol kuyu","usage_role":"contextual"}],"definition":"Aynı sözlük biçiminin bir kullanımda denizi, başka bir kullanımda ise suyu bol kuyuyu adlandırmasıdır. İki karşılık, genel bir su birikintisi anlamında kaynaştırılmaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dal, aynı adın iki ayrı su varlığına verilen sözlük karşılıklarını birlikte kaydeder."},{"facet_id":"F002","role":"source_variant","statement":"Bir kaynak karşılığında ad, geniş tuzlu su kütlesi olan denizi gösterir."},{"facet_id":"F003","role":"source_variant","statement":"Diğer ve daha yaygın kaynak karşılığında ad, suyu çok olan kuyuyu gösterir."}],"identity_rationale":"Kaynak ifadesi tek bir su birikimi türü tanımlamaz; aynı sözlük biçimi için deniz ve suyu bol kuyu olmak üzere iki ayrı karşılık verir. Dal korunabilir, ancak geçici çerçevedeki ortak su kütlesi görüntüsü yerine bu açık seçeneklilik tanıma yazılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"deniz"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"suyu bol kuyu"}],"lexicalization_note":"Tanım çıplak sözlük biçiminin deniz ve suyu bol kuyu karşılıklarını ayrı ayrı korur; bunlardan genel bir su birikintisi anlamı türetmez.","neighbor_coverage_note":"Deniz karşılığını açıklayan geniş su dalı ile kuyu çevresindeki bol su dalı seçildi; diğer adaylar gölet, artık su, taşkın veya su tutan arazi gibi farklı taşıyıcı ve süreçlere bağlıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Örtüşme yalnızca deniz karşılığındadır; odak dalın kuyu seçeneği komşuda bulunmaz, komşunun büyük ırmak ve genel su genişliği ise odak dalın tanımına girmez.","focus_only":"Odak dal aynı sözlük biçiminin suyu bol kuyu karşılığını da bağımsız bir seçenek olarak taşır.","gloss":"deniz ve geniş su","neighbor_only":"Komşu dal deniz yanında büyük ırmak ve farklı büyüklükte su alanlarına uzanan genel bir geniş su kapsamına sahiptir.","neighbor_ref":"root_000086/B001","relation_type":"near_synonym","shared_zone":"Odak dalın deniz karşılığı, komşu dalın geniş ve çok su çekirdeğiyle örtüşür."},{"boundary_match":"partial","distinction":"Odak dal suyu taşıyan kuyuyu niteler; komşu dal ise kuyudan dökülen suyu ve taşma sürecini merkez alır.","focus_only":"Odak dal kuyunun kendisini suyunun bol olması koşuluyla adlandırır.","gloss":"suyu bol kuyu ile kuyu suyu","neighbor_only":"Komşu dal kuyudaki kovadan dökülen veya havuza taşan suyu, kokusunu ve taşma olayını anlatır.","neighbor_ref":"root_001077/B003","relation_type":"near_neighbor","shared_zone":"İki dal kuyu çevresinde suyun çokluğu ve görünür birikimiyle ilişkilidir."}],"source_phrase_ar":"العيلم يقال إنه البحر ويقال إنه البئر الكثيرة الماء (maqayis)؛ العيلم الركية الكثيرة الماء (sihah)؛ العيلم البئر الكثيرة الماء (tahdhib)","source_summary":"Toplu tanıklık iki karşılığı yan yana verir: bir aktarım sözcüğü deniz olarak açıklar, öteki tanıklıklar ise suyu bol kuyu anlamını destekler. Kaynaklara özgü ayrı claim kimlikleri bulunmadığı için bu karşıtlık ortak özet içinde, atıf uydurulmadan korunur.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه العيلم بمعنى البحر أو البئر الكثيرة الماء","what_is_not_ar":"ليس هو العالمين ولا العلم ولا العلامة ولا العيلم بمعنى آخر غير مائي"},"support_links":["sup_1da28a5555193d9c8027"]},{"boundary":"Çekirdek yırtıcı kuş adıdır; çevik ve zeki erkek nitelemesi yalnızca bu addan türeyen biçime bağlıdır.","branch_kind":"bare","branch_ref":"root_001040/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:9:2:1","qac_word_ref":"100:9:2","surface_ar":"يَعْلَمُ"}],"gloss":"doğan veya atmaca türü yırtıcı kuş","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ad, doğan veya atmaca türünden avcı bir kuşu gösterir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuş adından türeyen insan nitelemesi, çevik ve zeki bir erkeği belirtir."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın temel kuş adını iki kaynak karşılığı arasındaki seçenekliliği koruyarak açıklamak için uygundur.","boundary_detail":"Çekirdek yırtıcı kuş adıdır; çevik ve zeki erkek nitelemesi yalnızca bu addan türeyen biçime bağlıdır.","branch_image_ar":"طائر جارح يسمى العلام","concept_gloss":"doğan veya atmaca türü yırtıcı kuş","contextual_glosses":[{"applicability":"Kuş adından türemiş insan nitelemesinin kullanıldığı bağlama özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan oluşu ile çeviklik ve zekâ niteliklerini birlikte korur."},"facet_ids":["F002"],"text":"çevik ve zeki adam","usage_role":"contextual"}],"definition":"Doğan veya atmaca türünden bir yırtıcı kuş adıdır. Bu kuş adından türetilen bir niteleme, çevik ve zeki bir erkeği anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ad, doğan veya atmaca türünden avcı bir kuşu gösterir."},{"facet_id":"F002","role":"associated_use","statement":"Kuş adından türeyen insan nitelemesi, çevik ve zeki bir erkeği belirtir."}],"identity_rationale":"Kaynak ifadesi temel adı doğan veya atmaca türünden yırtıcı kuş için verir ve geçici dal görüntüsünü doğrular. Çevik ve zeki erkek nitelemesi ise kuş adından türetilmiş ayrı bir biçimdir; kuşun tanımına doğrudan katılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"doğan veya atmaca"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"çevik ve zeki adam"}],"lexicalization_note":"Çıplak dal doğan veya atmaca türünden kuş adını tanımlar; insan nitelemesi türemiş bir sözcüksel uzantı olarak bağımlı tutulur.","neighbor_coverage_note":"Yırtıcı kuş sınıfında en yakın iki aday seçildi; diğer adaylar kanat çırpma, beslenme, farklı hayvan adları veya yalnızca uzak bir doğan ilişkisi taşır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Aynı kuş alanını paylaşsalar da komşu dal renk ve ara tür özellikleriyle daha dar bir kuşu adlandırır; odak dalın türemiş insan nitelemesi de komşuda yoktur.","focus_only":"Odak dal doğan veya atmaca karşılığı taşıyan kuş adını ve ondan türeyen insan nitelemesini içerir.","gloss":"yırtıcı kuş adları","neighbor_only":"Komşu dal mavi renkli, doğan ile atmaca arasında tanımlanan veya beyaz doğan sayılan daha özel bir kuş adıdır.","neighbor_ref":"root_000631/B002","relation_type":"same_field","shared_zone":"Her iki dal doğan ve atmaca çevresindeki avcı kuş adlandırmaları alanındadır."},{"boundary_match":"partial","distinction":"Odak dalda zekâ kuştan türetilen insan niteliğinde belirginleşir; komşuda ise doğrudan belirli doğanların özelliğidir.","focus_only":"Odak dal doğan veya atmaca türünü genel bir adla karşılar ve bu addan insan nitelemesi türetir.","gloss":"doğan adı ile zeki doğan nitelemesi","neighbor_only":"Komşu dal özellikle zeki ve keskin bakışlı doğanlara verilen bir adı belirtir.","neighbor_ref":"root_001375/B006","relation_type":"near_neighbor","shared_zone":"İki dal doğan türünden yırtıcı kuşları adlandırır ve zekâ çağrışımını paylaşır."}],"source_phrase_ar":"العلام الصقر؛ العلامي الرجل الخفيف الذكي مأخوذ من العلام؛ العلام الباشق (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık temel adı doğan veya atmaca türünden kuş için verir ve türemiş biçimi çevik, zeki erkek olarak açıklar."}],"source_summary":"Dal tek bir sözlük tanıklığında yırtıcı kuş adı ile bu addan türetilmiş çevik ve zeki erkek nitelemesini birlikte sunar.","sources":["TA"],"what_is_ar":"يدخل فيه العلام بمعنى الصقر أو الباشق وما نسب إليه من العلامي","what_is_not_ar":"ليس هو العلام بمعنى الحناء ولا العلامة ولا العالم"},"support_links":[]},{"boundary":"Dal yalnızca erkek sırtlanı adlandırır; başka erkek hayvan adları ve benzer sesli su veya kuş adları kapsam dışıdır.","branch_kind":"bare","branch_ref":"root_001040/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:9:2:1","qac_word_ref":"100:9:2","surface_ar":"يَعْلَمُ"}],"gloss":"erkek sırtlan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Adlandırılan canlı, cinsiyeti erkek olan sırtlandır."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanın türünü ve erkek oluşunu birlikte veren bütün bağlamlarda tam karşılıktır.","boundary_detail":"Dal yalnızca erkek sırtlanı adlandırır; başka erkek hayvan adları ve benzer sesli su veya kuş adları kapsam dışıdır.","branch_image_ar":"ذكر الضباع يسمى العيلام","concept_gloss":"erkek sırtlan","definition":"Erkek sırtlanı adlandıran yalın bir hayvan adıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Adlandırılan canlı, cinsiyeti erkek olan sırtlandır."}],"identity_rationale":"Kaynak ifadesinin iki tanıklığı da sözcüğü doğrudan erkek sırtlan olarak açıklar. Geçici dal görüntüsü bu yalın hayvan adıyla tam uyumludur ve başka bir tür, özellik veya mecaz eklemeyi gerektirmez.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"erkek sırtlan"}],"lexicalization_note":"Tanım çıplak hayvan adını erkek sırtlanla sınırlar ve başka türlere ya da bağlı kuruluşlara genişletmez.","neighbor_coverage_note":"Erkek sırtlanı aynı sınırlarla adlandıran aday tam eş anlamlı olarak seçildi; diğer adaylar kurt, erkek domuz, aslan, kuş veya daha geniş hayvan sınıflarıdır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Anlam çekirdeği, hayvan türü ve cinsiyet sınırı aynıdır; ayrım yalnızca kullanılan sözlük biçimindedir.","focus_only":null,"gloss":"erkek sırtlan","neighbor_only":null,"neighbor_ref":"root_001068/B007","relation_type":"synonym","shared_zone":"Her iki dal da hiçbir ek koşul getirmeden erkek sırtlanı adlandırır."}],"source_phrase_ar":"العيلام الذكر من الضباع (sihah)؛ العيلام الضبعان وهو ذكر الضباع (tahdhib)","source_summary":"Kaynaklar sözcüğün erkek sırtlanı adlandırdığı konusunda birleşir ve ek bir anlam ayrımı bildirmez.","sources":["SI","TA"],"what_is_ar":"يدخل فيه العيلام بمعنى ذكر الضباع","what_is_not_ar":"ليس هو العيلم البئر الكثيرة الماء ولا العلامة ولا العلم"},"support_links":[]},{"boundary":"Dal, kuş adını, burunla ilgili kullanımları ve alçak ya da gizli şeylere ilişkin ayrı anlamları kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001195/B001","candidate_links":[{"candidate_id":"cand_cf7e3bede216562d291f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَبْر","morph_features":"STEM|POS:N|LEM:qabor|ROOT:qbr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:9:7:2","qac_word_ref":"100:9:7","surface_ar":"قُبُورِ"}],"gloss":"ölüyü gömme, ona gömü yeri sağlama ve gömü yeri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gömüt, ölünün gömüldüğü ve kalacağı yerdir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem olarak ölüyü gömmek, onu gömü yerine koymaktır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen kullanım, ölüye gömü yeri sağlama, onu gömülecek duruma getirme veya gömülmesine izin verme ayrımını taşır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yer adı, gömütlerin bir arada bulunduğu alanı da belirtir."}}],"root_ar":"ق ب ر","root_id":"root_001195","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yer, doğrudan gömme, gömülmeyi sağlama ve toplu gömü alanı yönlerini birlikte temsil eder.","boundary_detail":"Dal, kuş adını, burunla ilgili kullanımları ve alçak ya da gizli şeylere ilişkin ayrı anlamları kapsamaz.","branch_image_ar":"مواراة الميت في القبر","concept_gloss":"ölüyü gömme, ona gömü yeri sağlama ve gömü yeri","contextual_glosses":[{"applicability":"Ölüyü doğrudan gömü yerine koyma eyleminin geçtiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğrudan gömme eylemini ve ölü katılımcısını eksiksiz korur."},"facet_ids":["F002"],"text":"ölüyü gömmek","usage_role":"general"},{"applicability":"Kişinin ölüyü kendi eliyle gömmesinden çok, onun gömülmesini mümkün kıldığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gömme eylemi ile gömülmeyi sağlama arasındaki katılımcı farkını korur."},"facet_ids":["F003"],"text":"ölüye gömü yeri sağlamak","usage_role":"explanatory"},{"applicability":"Birden çok gömütün yer aldığı toplu gömü alanı kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tek gömüt ile toplu gömü alanı arasındaki kapsam ayrımını korur."},"facet_ids":["F004"],"text":"gömütlerin bulunduğu alan","usage_role":"contextual"}],"definition":"Ölünün konulduğu gömü yerini ve ölüyü bu yere koyma eylemini; ayrıca ölüye böyle bir yer sağlama, gömülmesine izin verme ve gömütlerin bulunduğu yeri anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gömüt, ölünün gömüldüğü ve kalacağı yerdir."},{"facet_id":"F002","role":"core","statement":"Eylem olarak ölüyü gömmek, onu gömü yerine koymaktır."},{"facet_id":"F003","role":"specialization","statement":"Ettirgen kullanım, ölüye gömü yeri sağlama, onu gömülecek duruma getirme veya gömülmesine izin verme ayrımını taşır."},{"facet_id":"F004","role":"extension","statement":"Yer adı, gömütlerin bir arada bulunduğu alanı da belirtir."}],"identity_rationale":"Kaynak ifadesi bu dalı ölünün gömüldüğü yer, ölüyü oraya koyma eylemi, ölüye gömü yeri sağlama ya da gömme izni verme ve gömütlerin toplandığı yer çevresinde açıkça kurar. Geçişli gömme eylemi ile birine gömü yeri sağlama anlamı aynı sayılmamalı, dal içinde ayrı yönler olarak korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ölünün gömüldüğü yer; gömüt"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ölüyü gömmek ve gömü yerine koymak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"ölüyü gömü yerine koyma işi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ölüye gömü yeri sağlamak, gömülmesine izin vermek veya onu gömülecek duruma getirmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"ölü için gömü yeri hazırlama ve onu gömülmeye layık sayılanlar arasına koyma"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"onu gömmemize izin ver"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ölüyü kendi eliyle gömen kimse"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"gömütlerin bulunduğu yer; mezarlık"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"gömüt yeri veya gömütlerin bulunduğu yer"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"gömme işi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ölüye gömü yeri veren"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"gömütler; mezarlıklar"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"mezarlığa veya gömüt yerine ilişkin"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"gömüt kazısında sana yardım eden kişi"}],"lexicalization_note":"Tanım yalın ad ve eylem çekirdeğini kapsar; gömme izni isteyen kalıplaşmış söz ile türemiş yer ve kişi adlarını kendi özel kapsamlarında tutar.","neighbor_coverage_note":"Listelenen bütün komşu kartları incelendi; gömme eylemi, örtüp gizleme, genel gizleme ve gömütün özel bölümüyle en açıklayıcı sınırları kuran dört karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal gömme eyleminin gözden kaybolma sonucuna odaklanırken odak dal yer adlarını ve gömülmeyi sağlama ya da buna izin verme katılımcı ayrımını da korur.","focus_only":"Odak dal gömüt adını, toplu gömü alanını ve ölüye gömü yeri sağlama ayrımını da içerir.","gloss":"ölüyü gömerek gözden kaldırmak","neighbor_only":null,"neighbor_ref":"root_001117/B009","relation_type":"near_synonym","shared_zone":"Her iki dal da ölünün bir gömü yerine konulması eyleminde örtüşür."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği gömü yeri ve ölüyü oraya koymaktır; komşu dalın çekirdeği ise daha genel olarak ölüyü örtüp gizlemektir.","focus_only":"Odak dal gömüt, toplu gömü alanı ve gömülmeye yer ya da izin sağlama anlamlarını taşır.","gloss":"ölüyü örtüp gizlemek","neighbor_only":"Komşu dal ölüyü örtüp gizleme alanına kefeni ve başka örtünme adlarını da katar.","neighbor_ref":"root_000266/B009","relation_type":"near_neighbor","shared_zone":"İki dal ölünün gömülerek görünmez kılındığı cenaze işlemi alanında buluşur."},{"boundary_match":"partial","distinction":"Komşu dal nesne ve yöntem bakımından geneldir; odak dal ise ölünün belirli bir gömü yerine konulması ve bu yerin sağlanması çevresinde uzmanlaşır.","focus_only":"Odak dal özellikle ölüyü, onun gömü yerini ve gömülmesine ilişkin rolleri konu eder.","gloss":"bir şeyi altına sokarak gizlemek","neighbor_only":"Komşu dal insan dışındaki herhangi bir şeyin toprakta veya başka bir şeyin altında gizlenmesini kapsar.","neighbor_ref":"root_000475/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir varlığı toprağın altında görünmez kılma durumu bulunabilir."},{"boundary_match":"field_only","distinction":"Odak dal genel gömü yeri ve gömme eylemidir; komşu dal bu yerin içindeki belirli bir mimari bölümle sınırlıdır.","focus_only":"Odak dal gömütün bütününü, gömme eylemini ve gömütlerin bulunduğu alanı kapsar.","gloss":"gömütün yanındaki özel oyuk","neighbor_only":"Komşu dal gömütün yan tarafında açılan özel oyuğu ve ölünün oraya yerleştirilmesini belirtir.","neighbor_ref":"root_001345/B002","relation_type":"same_field","shared_zone":"İki dal aynı gömme düzeninin yerlerini ve işlemlerini konu eder."}],"source_phrase_ar":"القبر قبر الميت (maqayis)؛ القبر مدفن الإنسان (tahdhib)؛ القبر مقر الميت (mufradat)؛ قبرت الميت أي دفنته (jamhara;sihah;tahdhib)؛ أقبرته جعلت له مكانا يقبر فيه (maqayis;mufradat)؛ المقبرة موضع القبور (ayn;jamhara;tahdhib;mufradat)","source_summary":"Kaynakların ortak anlatımı ölünün gömüldüğü yeri, ölüyü gömme eylemini, ona gömü yeri sağlama veya gömme izni verme ayrımını ve gömütlerin bulunduğu alanı birlikte destekler.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه القبر مدفن الميت ومقره، وقبر الميت أي دفنه وجعله في القبر، وأقبره أي جعل له قبرا أو أذن في قبره أو صيره ذا قبر، والمقبرة موضع القبور","what_is_not_ar":"ليس القُبَّرة الطائر ولا طرف الأنف ولا غموض الأرض والنخل إلا من جهة الأصل العام"},"support_links":["sup_2ac542177bd28ea0dfdb"]},{"boundary":"Genel çekirdek gizli, içe gömülü veya alçakta kalma durumudur; özel bitki, arazi ve doğum kullanımları bu çekirdeğin yerine geçmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001195/B002","candidate_links":[{"candidate_id":"cand_24cddf9c024e1c3acc80","lane":"micro"},{"candidate_id":"cand_d31695c8ece2465a1236","lane":"micro"},{"candidate_id":"cand_55a67f901f4baabb49c0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَبْر","morph_features":"STEM|POS:N|LEM:qabor|ROOT:qbr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:9:7:2","qac_word_ref":"100:9:7","surface_ar":"قُبُورِ"}],"gloss":"gizli, alçakta veya içe gömülü kalma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin belirsiz, gizli, alçalmış veya içe çekilmiş durumda bulunması temel anlam alanını oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Arazi için kullanım, çukurda kalan ve kolay seçilmeyen yeri anlatır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hurma ağacı için kullanım, ürünün yaprakların arasında saklı kalmasını belirtir."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Hoş kokulu ağacın içinde aşınmış ve gevşemiş oyuk bölüm bu adla anılır."}},{"facet_id":"F005","role":"specialization","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Yeni doğan için kullanım, bedenin yarıksız ve deliksiz kapalı bir zarla çevrili olmasını anlatır."}}],"root_ar":"ق ب ر","root_id":"root_001195","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın genel durum çekirdeğini ve özel kullanımları birbirine karıştırmadan ortaklaştırır.","boundary_detail":"Genel çekirdek gizli, içe gömülü veya alçakta kalma durumudur; özel bitki, arazi ve doğum kullanımları bu çekirdeğin yerine geçmez.","branch_image_ar":"غموض الشيء وتطامنه","concept_gloss":"gizli, alçakta veya içe gömülü kalma","contextual_glosses":[{"applicability":"Araziyi niteleyen söz öbeğinde hem alçaklığı hem de kolay seçilmemeyi anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Araziye bağlı alçaklık ve belirsizlik özelliklerini birlikte korur."},"facet_ids":["F002"],"text":"çukurda ve gözden ırak arazi","usage_role":"contextual"},{"applicability":"Yalnızca ürünün ağacın yaprakları arasında kaldığını anlatan bitki kullanımına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ürünün yapraklar arasında saklı kalması koşulunu tam olarak korur."},"facet_ids":["F003"],"text":"ürünü yapraklarında saklı hurma ağacı","usage_role":"explanatory"},{"applicability":"Yeni doğanın üzerinde yarık ya da delik bulunmayan bütün bir zar olduğu bağlama özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yeni doğanı çevreleyen zarın kapalı ve kesintisiz olma koşulunu korur."},"facet_ids":["F005"],"text":"kapalı bir zar içinde doğmuş çocuk","usage_role":"explanatory"}],"definition":"Bir şeyin belirgin olmaması, alçakta ya da içe gömülü kalması çekirdektir. Arazi çukurluğu, ürünün yapraklar arasında saklı kalması, ağacın içindeki gevşek oyuk ve kapalı bir zar içindeki yeni doğan bu çekirdeğin ayrı, sözcüksel olarak sınırlı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin belirsiz, gizli, alçalmış veya içe çekilmiş durumda bulunması temel anlam alanını oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Arazi için kullanım, çukurda kalan ve kolay seçilmeyen yeri anlatır."},{"facet_id":"F003","role":"specialization","statement":"Hurma ağacı için kullanım, ürünün yaprakların arasında saklı kalmasını belirtir."},{"facet_id":"F004","role":"specialization","statement":"Hoş kokulu ağacın içinde aşınmış ve gevşemiş oyuk bölüm bu adla anılır."},{"facet_id":"F005","role":"specialization","statement":"Yeni doğan için kullanım, bedenin yarıksız ve deliksiz kapalı bir zarla çevrili olmasını anlatır."}],"identity_rationale":"Kaynak ifadesi dalın çekirdeğini bir şeyde belirsizlik, gizlilik ve alçalma olarak verir; arazi, hurma ağacı, hoş kokulu ağacın içi ve kapalı zarla doğan çocuk bunun farklı gerçekleşmeleridir. Bu örnekler tek bir yalın anlam gibi birleştirilemez; her biri kendi ad veya söz kalıbına bağlı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"çukurda ve gözden ırak arazi"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"ürünü yapraklarının arasında saklı duran hurma ağacı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"hoş kokulu ağacın içinde gevşeyip aşınmış oyuk bölüm"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"üzerinde yarıksız ve deliksiz kapalı bir zarla doğan çocuk"}],"lexicalization_note":"Yalın çekirdek ile arazi, hurma ağacı ve yeni doğan için kullanılan söz öbekleri ayrılır; söz öbeklerinin özel anlamları yalın köke genellenmez.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; alçalma, çukur arazi, derinleşme ve etkin gizleme ile sınırı en iyi gösteren dört ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dalın çekirdeği fiziksel alçalma ve içe girmedir; odak dal ise buna kolay seçilmeme ve çeşitli nesnelerde saklı kalma boyutunu ekler.","focus_only":"Odak dal belirsizlik ve gizliliği, ayrıca bitki, ağaç içi ve doğum kullanımlarını da kapsar.","gloss":"alçalmak ve içe girmek","neighbor_only":"Komşu dal evin geride kalması ile bacak ve ayaktaki çukur bölümler gibi başka içe girme örneklerini içerir.","neighbor_ref":"root_001107/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da alçalma, çukurlaşma veya dış yüzeyden içe çekilme görünümü vardır."},{"boundary_match":"partial","distinction":"Arazi bağlamında yakın karşılık olsalar da odak dalın kapsamı gizlilik çekirdeğine bağlı başka sözcüksel kullanımlara uzanır.","focus_only":"Odak dal belirsizliği ve arazi dışındaki yaprak, ağaç içi ve kapalı zar kullanımlarını da taşır.","gloss":"arazinin çukur iç bölümü","neighbor_only":"Komşu dal yer, vadi ve özel yer adları olarak kullanılan toprak içi çukurla sınırlıdır.","neighbor_ref":"root_000279/B004","relation_type":"near_synonym","shared_zone":"İki dal arazideki alçak ve içe çökmüş yer anlamında büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Komşu dal derinlik eksenine dayanır; odak dal için derinlik zorunlu değildir, belirgin olmama ve çevre içinde saklı kalma da yeterlidir.","focus_only":"Odak dal görünmezlik, ürünün yapraklarda saklanması ve kapalı zarla çevrilme gibi durumları içerir.","gloss":"derine inmek","neighbor_only":"Komşu dal suyun derinliği ile göz, yağ ve yaranın içeri girmesi gibi doğrudan derinleşme örneklerini içerir.","neighbor_ref":"root_001112/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal yüzeyden aşağıda veya içeride bulunma durumunu paylaşır."},{"boundary_match":"partial","distinction":"Odak dal bir durum ve nitelik alanıdır; komşu dal ise bir nesneyi etkin biçimde gizleme işlemini anlatır.","focus_only":"Odak dal çoğunlukla bir şeyin kendiliğinden alçak, içte veya kapalı durumda olmasını bildirir.","gloss":"altına sokarak gizlemek","neighbor_only":"Komşu dal bir failin nesneyi başka bir şeyin altına sokup gizlemesi eylemini gerektirir.","neighbor_ref":"root_000475/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalın sonucunda söz konusu şey görünmez veya zor seçilir duruma gelebilir."}],"source_phrase_ar":"أصل صحيح يدل على غموض في شيء وتطامن (maqayis)؛ أرض قبور غامضة (maqayis;jamhara;tahdhib)؛ نخلة قبور وكبوس يكون حملها في سعفها (maqayis;jamhara;tahdhib)؛ القبر موضع متأكل مسترخى في العود الذي يتطيب به وهو جوفه (ayn)؛ ولد مقبورا لأن عليه جلدة مصمتة ليس فيها شق ولا ثقب (tahdhib)","source_summary":"Kaynaklar belirsizlik ve alçalma çekirdeğini, çukur araziyi ve ürünü yapraklar arasında kalan hurma ağacını birlikte destekler; ayrıca ağaç içindeki gevşek oyuk ile kapalı zarla doğan çocuk özel örnekler olarak aktarılır.","sources":["MQ","AY","JA","TA"],"what_is_ar":"يدخل فيه الغموض والتطامن في الشيء، والأرض القبور الغامضة، والنخلة القبور التي يكون حملها في سعفها، وجوف عود الطيب المتأكل، والمقبور المحصور في جلدة مصمتة","what_is_not_ar":"ليس دفن الميت في القبر ولا المقبرة موضع القبور ولا القُبَّرة الطائر"},"support_links":["sup_1da28a5555193d9c8027","sup_8be49e51a89e2d628b74","sup_d11e43af5856b12e3d7e"]},{"boundary":"Dal yalnızca kuş adını ve onun dil biçimlerini kapsar; gömü, alçalma veya burun anlamlarıyla birleştirilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001195/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَبْر","morph_features":"STEM|POS:N|LEM:qabor|ROOT:qbr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:9:7:2","qac_word_ref":"100:9:7","surface_ar":"قُبُورِ"}],"gloss":"belirli bir kuş türünün adı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim belirli bir kuş türüdür."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynaklar aynı kuş adının birbiriyle bağlantılı tekil, çoğul ve söyleniş biçimlerini aktarır."}}],"root_ar":"ق ب ر","root_id":"root_001195","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kanıtın türü daha dar biçimde tanımlamadığı bu kuş adı dalının tamamı için uygundur.","boundary_detail":"Dal yalnızca kuş adını ve onun dil biçimlerini kapsar; gömü, alçalma veya burun anlamlarıyla birleştirilmez.","branch_image_ar":"القُبَّرة الطائر","concept_gloss":"belirli bir kuş türünün adı","contextual_glosses":[{"applicability":"Ad biçimleri arasındaki ayrım önemli değilken kuş gönderimini doğal cümle içinde verir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Canlı türüne yapılan kuş gönderimini herhangi bir ek tür iddiası olmadan korur."},"facet_ids":["F001"],"text":"bir kuş türü","usage_role":"general"},{"applicability":"Bir biçimin aynı kuşu adlandıran dilsel bir değişke olduğu açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ad biçimleri arasındaki değişke ilişkisini ve aynı gönderimi korur."},"facet_ids":["F002"],"text":"aynı kuş adının başka bir biçimi","usage_role":"explanatory"}],"definition":"Belirli bir kuş türü için kullanılan bir ad ile bu adın tekil, çoğul veya değişik söyleniş olarak aktarılan bağlantılı biçimlerini kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim belirli bir kuş türüdür."},{"facet_id":"F002","role":"source_variant","statement":"Kaynaklar aynı kuş adının birbiriyle bağlantılı tekil, çoğul ve söyleniş biçimlerini aktarır."}],"identity_rationale":"Kaynak ifadesi bu dalı belirli bir kuşun adı ve aynı adın birbiriyle ilişkili dil biçimleri olarak sınırlar. Kanıt kuşun daha dar tür kimliğini açıklamadığından, tanım kuş adı olmanın ötesinde tür belirlemez.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"belirli bir kuş türünün tekil adı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"aynı kuşun adı veya çoğul biçimi"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"aynı kuş adının değişik söylenişi"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"aynı kuş için kullanılan başka bir ad biçimi"}],"lexicalization_note":"Dal, kuş için kullanılan ayrı ad biçimlerini kapsar; bu biçimler tek bir yalın kök anlamı varmış gibi genellenmez.","neighbor_coverage_note":"Adayların tümü ayrı hayvan veya kuş adları olarak denetlendi; tür özdeşliği göstermeyen kartlardan alan ortaklığını en açık gösteren üçü seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Ortak alan yalnızca kuş adlandırmasıdır; kartlar farklı kuş adlarını verir ve aralarında tür özdeşliği kurulamaz.","focus_only":"Odak dal kendi kuş adını ve o adın bağlantılı dil biçimlerini belirtir.","gloss":"başka bir küçük kuş adı","neighbor_only":"Komşu dal serçegillerden olduğu söylenen başka bir kuşun özel adıdır.","neighbor_ref":"root_000465/B008","relation_type":"same_field","shared_zone":"Her iki dal da bir kuş türünü adlandıran söz varlığına aittir."},{"boundary_match":"field_only","distinction":"Komşu kart görünüş ve bölge bilgisiyle başka bir kuşu tanımlar; odak kartta bu özellikler yoktur ve adlar birbirinin yerine geçmez.","focus_only":"Odak dal türü daha dar tanımlanmayan ayrı bir kuş adını ve biçimlerini kapsar.","gloss":"güvercine benzeyen kuş","neighbor_only":"Komşu dal güvercine benzeyen ve belirli bir bölgeyle ilişkilendirilen başka bir kuşu anlatır.","neighbor_ref":"root_001066/B009","relation_type":"same_field","shared_zone":"İki dal da kuş türü adları alanında yer alır."},{"boundary_match":"field_only","distinction":"Ad biçimlerinin bulunması yapısal bir benzerliktir; gönderilen kuş türleri farklı olduğundan anlam örtüşmesi yoktur.","focus_only":"Odak dal farklı biçimleri bulunan ayrı bir kuş adıdır.","gloss":"toy kuşu","neighbor_only":"Komşu dal toy kuşunu ve onunla bağlantılı ad biçimlerini belirtir.","neighbor_ref":"root_000287/B008","relation_type":"same_field","shared_zone":"Her iki dal kuş adlarını ve bu adlarla bağlantılı biçimleri içerir."}],"source_phrase_ar":"القبرة واحدة القبر وهو ضرب من الطير (sihah)؛ القنبراء لغة فيها (sihah)؛ يقال للقنبرة قبرة وقبر (tahdhib)","source_summary":"Kaynaklar aynı kuşun iki temel ad biçimini birlikte destekler; bunlardan biri diğerinin tekili olarak açıklanır ve kuş adı için ek bir söyleniş biçimi de verilir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه القُبَّرة والقُبَّر اسما لطائر، وما يتصل بهما من لغة القنبرة والقنبراء","what_is_not_ar":"ليس القبر مدفن الإنسان ولا غموض الأرض والنخل ولا طرف الأنف"},"support_links":[]},{"boundary":"Burun ucu adları yalın anatomik kullanımlardır; öfkeli geliş anlamı ise yalnızca verilen söz kalıplarına bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001195/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَبْر","morph_features":"STEM|POS:N|LEM:qabor|ROOT:qbr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:9:7:2","qac_word_ref":"100:9:7","surface_ar":"قُبُورِ"}],"gloss":"burun ucu ve öfkeli gelişte burnun belirginleşmesi","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yalın anatomik kullanım burun ucunu adlandırır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Küçültme biçimi, çıkıntılı burnun baş kısmı için kullanılan ayrı bir addır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir söz kalıbı, burnu öne çıkmış görünerek öfkeli biçimde gelmeyi anlatır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İkinci söz kalıbı da aynı biçimde öfkeli gelişi anlatan eş yapılı bir kullanımdır."}}],"root_ar":"ق ب ر","root_id":"root_001195","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Anatomik adları ve yalnızca özel söz kalıplarında bulunan öfkeli geliş anlamını birlikte, fakat ayrımlı biçimde temsil eder.","boundary_detail":"Burun ucu adları yalın anatomik kullanımlardır; öfkeli geliş anlamı ise yalnızca verilen söz kalıplarına bağlıdır.","branch_image_ar":"طرف الأنف في الغضب","concept_gloss":"burun ucu ve öfkeli gelişte burnun belirginleşmesi","contextual_glosses":[{"applicability":"Öfke anlamı bulunmadan yalnızca anatomik bölüm adlandırıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yalın anatomik gönderimi herhangi bir öfke anlamı eklemeden korur."},"facet_ids":["F001"],"text":"burun ucu","usage_role":"general"},{"applicability":"Kişinin öfkeli gelişini burnunun belirgin görünümüyle anlatan ilk söz kalıbına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geliş eylemini, öfke durumunu ve burnun belirgin görünümünü birlikte korur."},"facet_ids":["F003"],"text":"burnu öne çıkmış biçimde öfkeli gelmek","usage_role":"contextual"},{"applicability":"İlk öfke ifadesine denk gösterilen ikinci söz kalıbını doğal Türkçeyle karşılar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İkinci kalıbın öfkeli geliş ve belirgin burun görünümü yönlerini korur."},"facet_ids":["F004"],"text":"burnu kabarmış halde öfkeli gelmek","usage_role":"contextual"}],"definition":"Burun ucuna ve çıkıntılı burnun baş kısmına verilen adları kapsar. İki özel söz kalıbında ise burnun öne çıkmış ya da kabarmış görünümü, kişinin öfkeli gelişiyle ilişkilendirilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yalın anatomik kullanım burun ucunu adlandırır."},{"facet_id":"F002","role":"specialization","statement":"Küçültme biçimi, çıkıntılı burnun baş kısmı için kullanılan ayrı bir addır."},{"facet_id":"F003","role":"associated_use","statement":"Bir söz kalıbı, burnu öne çıkmış görünerek öfkeli biçimde gelmeyi anlatır."},{"facet_id":"F004","role":"source_variant","statement":"İkinci söz kalıbı da aynı biçimde öfkeli gelişi anlatan eş yapılı bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi yalnızca öfke anındaki burun ucunu değil, burun ucuna verilen adları ve burnun belirginleştiği öfkeli gelişi anlatan iki kalıplaşmış sözü birlikte verir. Bu nedenle dal, anatomik ad ile öfke ifadesini ayıran biçimde yeniden çerçevelenmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"burun ucu"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"çıkıntılı burnun baş kısmı için kullanılan küçültme biçimi"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"burnu öne çıkmış biçimde öfkeli gelmek"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"burnu kabarmış halde öfkeli gelmek"}],"lexicalization_note":"Yalın burun ucu adları ile öfkeli gelişi bildiren iki kalıplaşmış söz ayrı tutulur; öfke anlamı anatomik adın geneline yayılmaz.","neighbor_coverage_note":"Tüm adaylar incelendi; genel öfke izi, öfkeden yüzün alevlenmesi, burun organı ve burnun rüzgârı karşılamasıyla sınırı gösteren dört komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirtiyi burun ucuna ve iki geliş kalıbına bağlar; komşu dal ise yüzün genelindeki öfke izini anlatır.","focus_only":"Odak dal burun ucunun adını ve öfkeli gelişte burnun belirgin görünmesini içerir.","gloss":"öfkenin yüzdeki izi","neighbor_only":"Komşu dal öfkenin yüzdeki herhangi bir görünür izini organ ve hareket belirtmeden kapsar.","neighbor_ref":"root_000198/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal öfkenin yüzde dışarıdan görülen bir belirti kazanmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal burun biçimi ve geliş eylemiyle sınırlıdır; komşu dal bütün yüzün ısınma ve alevlenme görünümüne dayanır.","focus_only":"Odak dal burnun öne çıkması veya kabarmasıyla birlikte kişinin gelişini bildirir.","gloss":"yüzün öfkeden alevlenmesi","neighbor_only":"Komşu dal yüzün öfkeden alevlenmesini ve iç sıcaklığın yükselmesini ateş benzetmesiyle anlatır.","neighbor_ref":"root_000225/B004","relation_type":"near_neighbor","shared_zone":"İki dal da öfkeyi yüzde beliren bedensel bir görünüm aracılığıyla ifade eder."},{"boundary_match":"field_only","distinction":"Komşu dal organın genel adıdır; odak dal yalnızca ucuna verilen adları ve belirli öfke kalıplarını içerir.","focus_only":"Odak dal burun ucunu ve burun görünümüyle kurulan iki öfke ifadesini kapsar.","gloss":"burun organı","neighbor_only":"Komşu dal burun organının bütünü, büyüklüğü, kokusu, yaralanması ve işlevleri gibi geniş bir alanı kapsar.","neighbor_ref":"root_000060/B002","relation_type":"same_field","shared_zone":"Her iki dal insan veya hayvan burnuyla ilgili söz varlığı alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal öfke ifadesidir; komşu dal yönelme ve rüzgârı karşılama eylemidir, öfke içermez.","focus_only":"Odak dal öfke sırasında burnun görünümünü ve kişinin gelişini anlatır.","gloss":"rüzgârı burunla karşılamak","neighbor_only":"Komşu dal insanın veya atın burnuyla rüzgâra yönelip onu karşılaması eylemini anlatır.","neighbor_ref":"root_001405/B002","relation_type":"same_field","shared_zone":"İki dalda da burun belirli bir görünüm veya eylemin merkezindedir."}],"source_phrase_ar":"جاء فلان رامعا قبراه ورامعا أنفه إذا جاء مغضبا (tahdhib)؛ جاءنا فخا قبراه (tahdhib)؛ القبراة أيضا طرف الأنف (tahdhib)؛ القبيرة تصغير القبرة وهي رأس القنفاء (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Burun ucu ve çıkıntılı burnun baş kısmı için iki ad, burnun belirgin görünümüyle öfkeli gelişi anlatan iki söz kalıbıyla birlikte aktarılır."}],"source_summary":"Bu dalda birden çok kaynağın ortak katmanı yoktur; anatomik adlar ile öfkeli gelişi bildiren iki söz kalıbının tamamı tek kaynaklı bir tanıklıkta toplanır.","sources":["TA"],"what_is_ar":"يدخل فيه القبراة طرف الأنف، والقبيرة رأس القنفاء، وقولهم جاء رامعا قبراه أو فخا قبراه في الغضبان","what_is_not_ar":"ليس القبر مدفن الإنسان ولا القُبَّرة الطائر ولا الغموض العام"},"support_links":[]},{"boundary":"Dal gerçek gömü yerini adlandırmaz; ölüm, gizlilik, açığa çıkma, kâfir ile cahilin gömülmüş diye nitelenmesi ve ölüler hükmünde olma yönlerini mecazi kullanımlarla sınırlar.","branch_kind":"mixed_non_bare","branch_ref":"root_001195/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَبْر","morph_features":"STEM|POS:N|LEM:qabor|ROOT:qbr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:9:7:2","qac_word_ref":"100:9:7","surface_ar":"قُبُورِ"}],"gloss":"gömülme üzerinden ölüm, gizlilik ve ölü hükmünde olma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gömü alanına varma sözü ölümün dolaylı anlatımı olabilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gömülerde olanın çıkarılması, diriliş durumunu veya gizli sırların açığa çıkmasını anlatır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsanın dünyadaki durumları, henüz açığa çıkmadıkları için gömülmüşçesine gizli sayılır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kâfir ile cahil, dünyadayken gömülmüş diye nitelenir."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Bazı kişiler ölüler hükmünde anlatılabilir."}}],"root_ar":"ق ب ر","root_id":"root_001195","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın ölüm, saklılık, açığa çıkma ve dirilikten yoksun sayılma yönlerini ortak gömülme imgesi altında toplar.","boundary_detail":"Dal gerçek gömü yerini adlandırmaz; ölüm, gizlilik, açığa çıkma, kâfir ile cahilin gömülmüş diye nitelenmesi ve ölüler hükmünde olma yönlerini mecazi kullanımlarla sınırlar.","branch_image_ar":"استعارة القبر للموت والاستتار","concept_gloss":"gömülme üzerinden ölüm, gizlilik ve ölü hükmünde olma","contextual_glosses":[{"applicability":"Gömü alanına varmanın ölümü dolaylı biçimde anlattığı bağlamda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dolaylı sözün bağlam içinde ulaştığı ölüm anlamını tam olarak korur."},"facet_ids":["F001"],"text":"ölmek","usage_role":"contextual"},{"applicability":"Gömülü olanın dirilişte ortaya çıkarılması veya sırların açığa dökülmesi bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önce gizli olanın daha sonra ortaya çıkarılması yönünü korur."},"facet_ids":["F002"],"text":"gizli olanların açığa çıkarılması","usage_role":"explanatory"},{"applicability":"Bilgisiz kişinin dünyadayken gizlenmiş ve işlevsiz kalmış sayıldığı mecazi nitelemeye özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilgisizliği çevreleyen ve kişiyi etkisiz bırakan bir durum olarak korur."},"facet_ids":["F004"],"text":"bilgisizliğe gömülmüş","usage_role":"contextual"},{"applicability":"Gerçekte canlı olup etkisizlik veya algısızlık bakımından ölü sayılan kişiler için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gerçek ölüm ile mecazi olarak ölü sayılma arasındaki hüküm farkını korur."},"facet_ids":["F005"],"text":"ölü hükmünde olanlar","usage_role":"contextual"}],"definition":"Gömü ve gömülme imgesi, ölümün dolaylı anlatımı, gizli durumların gömülmüş sayılması, gömülü olanın dirilişte ya da sırlar açığa çıktığında ortaya çıkarılması, kâfir ile cahilin dünyadayken gömülmüş diye nitelenmesi ve bazı kişilerin ölüler hükmünde görülmesi için mecazen kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gömü alanına varma sözü ölümün dolaylı anlatımı olabilir."},{"facet_id":"F002","role":"extension","statement":"Gömülerde olanın çıkarılması, diriliş durumunu veya gizli sırların açığa çıkmasını anlatır."},{"facet_id":"F003","role":"extension","statement":"İnsanın dünyadaki durumları, henüz açığa çıkmadıkları için gömülmüşçesine gizli sayılır."},{"facet_id":"F004","role":"extension","statement":"Kâfir ile cahil, dünyadayken gömülmüş diye nitelenir."},{"facet_id":"F005","role":"extension","statement":"Bazı kişiler ölüler hükmünde anlatılabilir."}],"identity_rationale":"Kaynak ifadesi gömü alanı üzerinden ölümü anlatma, gömülü olanın dirilişte veya sırların açığa çıkışında ortaya çıkarılması, insanın durumlarının gizli sayılması, kâfir ile cahilin dünyadayken gömülmüş diye nitelenmesi ve bazı kişilerin ölüler hükmünde görülmesi gibi birkaç mecazi yön verir. Bunlar tek bir 'gizlenme' anlamına indirgenmemeli, gömülme imgesine bağlı ayrı aktarımlar olarak korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"ölmek"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"gömülerde saklı olanların dirilişte veya sırlar açığa çıkarken ortaya çıkarılması"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"gömülmüşçesine gizli"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"bilgisizliğe gömülmüş"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"ölü hükmünde olanlar"}],"lexicalization_note":"Mecazi anlamlar belirli söz kalıpları ve türemiş biçimlere bağlıdır; ölüm veya gizlilik anlamı yalın gömü adı için genel anlam sayılmaz.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; gerçek gömme dalı, gömütün eş adlı karşılığı ve gömütü ev sayan aktarım mecazi sınırı en yararlı biçimde açıkladığı için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal fiziksel yer ve işlemdir; odak dal bu alanı ölüm, saklılık, gömülmüş sayılma ve ölü hükmünde olma gibi mecazi durumlara taşır.","focus_only":"Odak dal ölüm, gizlilik, açığa çıkma, kâfir ile cahilin gömülmüş diye nitelenmesi ve ölü hükmünde olma için mecazi aktarımlar içerir.","gloss":"gerçek gömü yeri ve gömme","neighbor_only":"Komşu dal gerçek gömü yerini, ölüyü oraya koymayı ve gömülmesine yer ya da izin sağlamayı anlatır.","neighbor_ref":"root_001195/B001","relation_type":"near_neighbor","shared_zone":"Mecazi kullanımların tümü gerçek gömü ve gömülme tasarımından yararlanır."},{"boundary_match":"field_only","distinction":"Komşu dal doğrudan fiziksel yeri adlandırır; odak dal ise fiziksel adı mecazi bir anlatım aracı olarak kullanır.","focus_only":"Odak dal gömü fikrini ölüm, gizlilik, gömülmüş sayılma ve ölü hükmünde olma gibi mecazi anlatımlarda kullanır.","gloss":"gömütün başka bir adı","neighbor_only":"Komşu dal gerçek gömütün başka bir adını ve o yerin yapılmasını belirtir.","neighbor_ref":"root_000226/B001","relation_type":"same_field","shared_zone":"Her iki dal gömü yeri düşüncesi çevresinde yer alır."},{"boundary_match":"partial","distinction":"Komşu dal gömütü ev olarak kavramlaştırır; odak dal gömülmeyi ölüm, saklılık, gömülmüş sayılma ve ölü hükmünde olma durumlarına genişletir.","focus_only":"Odak dal gizlilik, dirilişte açığa çıkma, kâfir ile cahilin gömülmüş diye nitelenmesi ve ölü hükmünde sayılma yönlerine uzanır.","gloss":"gömütü ölünün evi saymak","neighbor_only":"Komşu dal gömütü ölünün evi veya kaldığı yer olarak yeniden adlandırır.","neighbor_ref":"root_000166/B007","relation_type":"near_neighbor","shared_zone":"İki dal gerçek gömü yerinden hareketle ölüm hakkında aktarmalı bir anlatım kurar."}],"source_phrase_ar":"حتى زرتم المقابر كناية عن الموت (mufradat)؛ إذا بعثر ما في القبور إشارة إلى حال البعث (mufradat)؛ أحوال الإنسان ما دام في الدنيا مستورة كأنها مقبورة (mufradat)؛ الكافر والجاهل ما دام في الدنيا فهو مقبور (mufradat)؛ من في القبور أي الذين هم في حكم الأموات (mufradat)","source_qualifications":[{"kind":"sole_attestation","summary":"Gömülme imgesi ölümün dolaylı anlatımına, gizlinin açığa çıkmasına, insan durumlarının saklılığına, kâfir ile cahilin dünyadayken gömülmüş diye nitelenmesine ve ölüler hükmünde olanlara yapılan ayrı gönderime genişletilir."}],"source_summary":"Bu dalda birden çok kaynağın ortak katmanı yoktur; ölüm, dirilişte açığa çıkma, gizli durumlar, kâfir ile cahilin gömülmüş diye nitelenmesi ve ölü hükmünde sayılma yönleri tek kaynaklı bir açıklamada toplanır.","sources":["MU"],"what_is_ar":"يدخل فيه استعمال المقابر كناية عن الموت، والقبور إشارة إلى كشف المستور، والمقبور استعارة للمستور أو الجاهل أو من في حكم الأموات","what_is_not_ar":"ليس المدفن الحسي نفسه ولا اسم الطائر ولا طرف الأنف"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["100:9:1"],"branch_refs":[],"candidate_id":"cand_91396d60a43738e177a8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:9:1:audible-interruption","source_type":"word_analysis","support_ids":["sup_e53f9f6fd2b654dc2e00","sup_fe14e1dc2fb4a484c9e7"],"title":"abrupt opening sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:1","qac_refs":["100:9:1:1","100:9:1:2"],"status":"accepted"}},{"anchor_refs":["100:9:1"],"branch_refs":[],"candidate_id":"cand_fe01fc96591bbd32fc39","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:9:1:consequence-scoped-question","source_type":"word_analysis","support_ids":["sup_806ed96f82eb861c7b1b","sup_e53f9f6fd2b654dc2e00"],"title":"question as consequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:1","qac_refs":["100:9:1:1","100:9:1:2"],"status":"accepted"}},{"anchor_refs":["100:9:1"],"branch_refs":[],"candidate_id":"cand_e2ee953eaa6b8c383cb7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:9:1:fused-opening-form","source_type":"word_analysis","support_ids":["sup_a9058078c7984fb5427d","sup_e53f9f6fd2b654dc2e00"],"title":"compressed particle fusion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:1","qac_refs":["100:9:1:1","100:9:1:2"],"status":"accepted"}},{"anchor_refs":["100:9:1"],"branch_refs":[],"candidate_id":"cand_e98922c34e26b32b6fdc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:9:1:rebuke-and-register-shift","source_type":"word_analysis","support_ids":["sup_14969907a88cac726194","sup_e53f9f6fd2b654dc2e00"],"title":"rebuke after diagnosis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:1","qac_refs":["100:9:1:1","100:9:1:2"],"status":"accepted"}},{"anchor_refs":["100:9:2"],"branch_refs":[],"candidate_id":"cand_bc09661c842ce0248783","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:9:2:negated-cognition-scope","source_type":"word_analysis","support_ids":["sup_5487976aae2f7b4bf184","sup_cb74b56525c7e8746f81"],"title":"negation scopes over knowing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:2","qac_refs":["100:9:1:3"],"status":"accepted"}},{"anchor_refs":["100:9:2"],"branch_refs":[],"candidate_id":"cand_11d7765459da92e92901","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:9:2:rhetorical-negative-force","source_type":"word_analysis","support_ids":["sup_0171a7c366589d83d7a4","sup_5487976aae2f7b4bf184"],"title":"negation becomes rebuke","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:2","qac_refs":["100:9:1:3"],"status":"accepted"}},{"anchor_refs":["100:9:3"],"branch_refs":[],"candidate_id":"cand_33007883a3ac77ca8d6c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"100:9:3:forward-divine-knowing-closure","source_type":"word_analysis","support_ids":["sup_8b986c0372dd46981bc6","sup_e622d28a1c6f1540d8f2"],"title":"human knowing before divine knowing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:3","qac_refs":["100:9:2:1"],"status":"accepted"}},{"anchor_refs":["100:9:3"],"branch_refs":[],"candidate_id":"cand_9ea42dfe20d09c0671d5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"100:9:3:human-referent-continuity","source_type":"word_analysis","support_ids":["sup_8b986c0372dd46981bc6","sup_e7d86cdafc483e62425a"],"title":"same human remains exposed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:3","qac_refs":["100:9:2:1"],"status":"accepted"}},{"anchor_refs":["100:9:3"],"branch_refs":[],"candidate_id":"cand_023f566682079335df9e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"100:9:3:objectless-knowing","source_type":"word_analysis","support_ids":["sup_8b986c0372dd46981bc6","sup_a41d587e90b77e710742"],"title":"objectless knowing opens scope","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:3","qac_refs":["100:9:2:1"],"status":"accepted"}},{"anchor_refs":["100:9:3"],"branch_refs":[],"candidate_id":"cand_3ae9b93cff702992eafc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"100:9:3:present-accountability","source_type":"word_analysis","support_ids":["sup_8b986c0372dd46981bc6","sup_9001100394f95c597a1e"],"title":"present cognitive accountability","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:3","qac_refs":["100:9:2:1"],"status":"accepted"}},{"anchor_refs":["100:9:3"],"branch_refs":[],"candidate_id":"cand_25148ff0c29082865184","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"100:9:3:recognition-and-sign-pressure","source_type":"word_analysis","support_ids":["sup_8b986c0372dd46981bc6","sup_a6875cb64451dee5194d"],"title":"knowledge as recognition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:3","qac_refs":["100:9:2:1"],"status":"accepted"}},{"anchor_refs":["100:9:3"],"branch_refs":[],"candidate_id":"cand_00c767835d712980aa02","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"100:9:3:sound-link-to-opening","source_type":"word_analysis","support_ids":["sup_3bba4f5d7692d99fc9cc","sup_8b986c0372dd46981bc6"],"title":"secondary sound link","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:3","qac_refs":["100:9:2:1"],"status":"accepted"}},{"anchor_refs":["100:9:4"],"branch_refs":[],"candidate_id":"cand_ad1c9554dc6b5dc74ef2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:9:4:certain-when-clause","source_type":"word_analysis","support_ids":["sup_6d2d4ac55b1f326bf8b6","sup_82a0f599584f92e1f506"],"title":"certain future when-scene","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:4","qac_refs":["100:9:3:1"],"status":"accepted"}},{"anchor_refs":["100:9:4"],"branch_refs":[],"candidate_id":"cand_3dd538a63cc38a00273c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:9:4:forward-protasis-pull","source_type":"word_analysis","support_ids":["sup_82a0f599584f92e1f506","sup_ca00b4bda7e491253070"],"title":"syntax pulls toward closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:4","qac_refs":["100:9:3:1"],"status":"accepted"}},{"anchor_refs":["100:9:4"],"branch_refs":[],"candidate_id":"cand_732087eb0b01c15dcbc7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:9:4:second-beat-event-frame","source_type":"word_analysis","support_ids":["sup_82a0f599584f92e1f506","sup_be207a31ccf7a323b811"],"title":"second beat opens the scene","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:4","qac_refs":["100:9:3:1"],"status":"accepted"}},{"anchor_refs":["100:9:5"],"branch_refs":[],"candidate_id":"cand_985f845b7d31c12caf01","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000130"],"scope":"focus_ayah","source_local_id":"100:9:5:burial-reversal-5-31","source_type":"word_analysis","support_ids":["sup_b1db4b703a414aebe2f2","sup_b62fc026b83a308f61bf"],"title":"digging reversal in apparatus","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:5","qac_refs":["100:9:4:1"],"status":"accepted"}},{"anchor_refs":["100:9:5"],"branch_refs":[],"candidate_id":"cand_8b830332146880668aaa","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000130"],"scope":"focus_ayah","source_local_id":"100:9:5:external-to-internal-disclosure","source_type":"word_analysis","support_ids":["sup_b1db4b703a414aebe2f2","sup_e0fc32e3e3d252ac1005"],"title":"outer disclosure begins the pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:5","qac_refs":["100:9:4:1"],"status":"accepted"}},{"anchor_refs":["100:9:5"],"branch_refs":[],"candidate_id":"cand_02cba46aed45c71cc4fc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000130"],"scope":"focus_ayah","source_local_id":"100:9:5:passive-perfect-certainty","source_type":"word_analysis","support_ids":["sup_6f3e10c73879e0365b92","sup_b1db4b703a414aebe2f2"],"title":"passive perfect certainty","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:5","qac_refs":["100:9:4:1"],"status":"accepted"}},{"anchor_refs":["100:9:5"],"branch_refs":[],"candidate_id":"cand_73a181626f6597cabf48","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000130"],"scope":"focus_ayah","source_local_id":"100:9:5:raising-and-finding-pressure","source_type":"word_analysis","support_ids":["sup_8f0a26cb0a75ced2c48c","sup_b1db4b703a414aebe2f2"],"title":"raising with discovery pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:5","qac_refs":["100:9:4:1"],"status":"accepted"}},{"anchor_refs":["100:9:5"],"branch_refs":[],"candidate_id":"cand_3465450a771b548efe8c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000130"],"scope":"focus_ayah","source_local_id":"100:9:5:rare-82-4-pairing","source_type":"word_analysis","support_ids":["sup_b1db4b703a414aebe2f2","sup_e4eb8ca5050372c17519"],"title":"rare grave-overturning pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:5","qac_refs":["100:9:4:1"],"status":"accepted"}},{"anchor_refs":["100:9:5"],"branch_refs":[],"candidate_id":"cand_5ac8dca109a4055e5b14","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000130"],"scope":"focus_ayah","source_local_id":"100:9:5:rupture-sound","source_type":"word_analysis","support_ids":["sup_b1db4b703a414aebe2f2","sup_c8fd7c4c412d051db468"],"title":"consonants suit rupture","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:5","qac_refs":["100:9:4:1"],"status":"accepted"}},{"anchor_refs":["100:9:5"],"branch_refs":[],"candidate_id":"cand_9ea7dc92b736eb9fc28e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000130"],"scope":"focus_ayah","source_local_id":"100:9:5:variant-contrast","source_type":"word_analysis","support_ids":["sup_b1db4b703a414aebe2f2","sup_eb05e3fc73b8814c41e3"],"title":"variant readings as contrast","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:5","qac_refs":["100:9:4:1"],"status":"accepted"}},{"anchor_refs":["100:9:5"],"branch_refs":[],"candidate_id":"cand_f7fc7d068c36e22be68e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000130"],"scope":"focus_ayah","source_local_id":"100:9:5:violent-disclosure-lexis","source_type":"word_analysis","support_ids":["sup_43237b49ee0493e938de","sup_b1db4b703a414aebe2f2"],"title":"overturning exposes what was hidden","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:5","qac_refs":["100:9:4:1"],"status":"accepted"}},{"anchor_refs":["100:9:6"],"branch_refs":[],"candidate_id":"cand_a5a7c4b206533747a8f2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:9:6:interrogative-pressure","source_type":"word_analysis","support_ids":["sup_82d134828227545b66a8","sup_c4d295d83af6873bdd21"],"title":"question-like openness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:6","qac_refs":["100:9:5:1"],"status":"accepted"}},{"anchor_refs":["100:9:6"],"branch_refs":[],"candidate_id":"cand_5f2d35025004611c9d66","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:9:6:outer-inner-ma-echo","source_type":"word_analysis","support_ids":["sup_3778efc7bb7894354751","sup_82d134828227545b66a8"],"title":"outer phrase anticipates inner phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:6","qac_refs":["100:9:5:1"],"status":"accepted"}},{"anchor_refs":["100:9:6"],"branch_refs":[],"candidate_id":"cand_4fc8ba16f9b618948d56","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:9:6:passive-subject-promotion","source_type":"word_analysis","support_ids":["sup_82d134828227545b66a8","sup_c2b89364e4c52e3dd1e6"],"title":"contents become subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:6","qac_refs":["100:9:5:1"],"status":"accepted"}},{"anchor_refs":["100:9:6"],"branch_refs":[],"candidate_id":"cand_f94f15e34318d8ca82d2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:9:6:unspecified-relative-scope","source_type":"word_analysis","support_ids":["sup_21b7657affdc8b47c708","sup_82d134828227545b66a8"],"title":"unspecified contents remain open","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:6","qac_refs":["100:9:5:1"],"status":"accepted"}},{"anchor_refs":["100:9:7"],"branch_refs":[],"candidate_id":"cand_8ca21a579d64eb91bc64","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:9:7:containment-focus","source_type":"word_analysis","support_ids":["sup_52e04c97c62d5a0671d1","sup_f9bb410a3d792b47c3e5"],"title":"inside relation becomes visible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:7","qac_refs":["100:9:6:1"],"status":"accepted"}},{"anchor_refs":["100:9:7"],"branch_refs":[],"candidate_id":"cand_9e2abd9a928e6ea60fba","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:9:7:contents-not-containers","source_type":"word_analysis","support_ids":["sup_beb1ed7b03450e186f6d","sup_f9bb410a3d792b47c3e5"],"title":"contents rather than containers","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:7","qac_refs":["100:9:6:1"],"status":"accepted"}},{"anchor_refs":["100:9:7"],"branch_refs":[],"candidate_id":"cand_7b71ccef751966a9b9b1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:9:7:recitational-binding","source_type":"word_analysis","support_ids":["sup_41ec0d7e5df7fa40e023","sup_f9bb410a3d792b47c3e5"],"title":"liaison binds the phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:7","qac_refs":["100:9:6:1"],"status":"accepted"}},{"anchor_refs":["100:9:7"],"branch_refs":[],"candidate_id":"cand_ee57d6d200bf0f81cd80","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:9:7:relative-phrase-completion","source_type":"word_analysis","support_ids":["sup_c4e4106d12074fdf502b","sup_f9bb410a3d792b47c3e5"],"title":"phrase completes the subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:7","qac_refs":["100:9:6:1"],"status":"accepted"}},{"anchor_refs":["100:9:8"],"branch_refs":[],"candidate_id":"cand_e5e94198d4b90374283c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001195"],"scope":"focus_ayah","source_local_id":"100:9:8:audible-ur-link","source_type":"word_analysis","support_ids":["sup_a79c0a2ab8bfdb6e3be0","sup_d43fab1205a18ca17f81"],"title":"ending sound links forward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:8","qac_refs":["100:9:7:1","100:9:7:2"],"status":"accepted"}},{"anchor_refs":["100:9:8"],"branch_refs":[],"candidate_id":"cand_410317535933becd1974","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001195"],"scope":"focus_ayah","source_local_id":"100:9:8:ayah-ending-concealment","source_type":"word_analysis","support_ids":["sup_a79c0a2ab8bfdb6e3be0","sup_bdc5ac16c6fa513b8ec1"],"title":"ending lands on concealment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:8","qac_refs":["100:9:7:1","100:9:7:2"],"status":"accepted"}},{"anchor_refs":["100:9:8"],"branch_refs":[],"candidate_id":"cand_dc981dcd9686de78dde6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001195"],"scope":"focus_ayah","source_local_id":"100:9:8:concealment-site-reversed","source_type":"word_analysis","support_ids":["sup_8f138faafc887292b4c9","sup_a79c0a2ab8bfdb6e3be0"],"title":"burial concealment overturned","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:8","qac_refs":["100:9:7:1","100:9:7:2"],"status":"accepted"}},{"anchor_refs":["100:9:8"],"branch_refs":[],"candidate_id":"cand_381426e2b27dec6a90d3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001195"],"scope":"focus_ayah","source_local_id":"100:9:8:definite-plural-totality","source_type":"word_analysis","support_ids":["sup_9d65e561ff7492ee248f","sup_a79c0a2ab8bfdb6e3be0"],"title":"definite plural grave-field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:8","qac_refs":["100:9:7:1","100:9:7:2"],"status":"accepted"}},{"anchor_refs":["100:9:8"],"branch_refs":[],"candidate_id":"cand_15d8cf106eaf561a21c6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001195"],"scope":"focus_ayah","source_local_id":"100:9:8:genitive-container-role","source_type":"word_analysis","support_ids":["sup_7228a526d04b66b25656","sup_a79c0a2ab8bfdb6e3be0"],"title":"container, not subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:8","qac_refs":["100:9:7:1","100:9:7:2"],"status":"accepted"}},{"anchor_refs":["100:9:8"],"branch_refs":[],"candidate_id":"cand_0e3801d1260f0619bb9f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001195"],"scope":"focus_ayah","source_local_id":"100:9:8:marked-82-4-contrast","source_type":"word_analysis","support_ids":["sup_7c3c8932cb3e2d1a0c7d","sup_a79c0a2ab8bfdb6e3be0"],"title":"marked pair refocused from 82:4","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:8","qac_refs":["100:9:7:1","100:9:7:2"],"status":"accepted"}},{"anchor_refs":["100:9:8"],"branch_refs":[],"candidate_id":"cand_fb6dac2d33ca5051bf21","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001195"],"scope":"focus_ayah","source_local_id":"100:9:8:outer-inner-disclosure-pair","source_type":"word_analysis","support_ids":["sup_74f70a81dc629ce376dc","sup_a79c0a2ab8bfdb6e3be0"],"title":"outer concealment anticipates inner concealment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:9:8","qac_refs":["100:9:7:1","100:9:7:2"],"status":"accepted"}},{"anchor_refs":["100:9:2"],"branch_refs":[],"candidate_id":"cand_0081752b6447afc9caaa","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"100:9:2:1","source_type":"qac_morpheme","support_ids":["sup_3b22687fc047e7f94f31"],"title":"QAC root occurrence: ع ل م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["100:9:4"],"branch_refs":[],"candidate_id":"cand_5491d42e3f813575a7be","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000130"],"scope":"focus_ayah","source_local_id":"100:9:4:1","source_type":"qac_morpheme","support_ids":["sup_03eb5cfd26299a79f12c"],"title":"QAC root occurrence: ب ع ث ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["100:9:7"],"branch_refs":[],"candidate_id":"cand_2f6592dd0944c6f7d317","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001195"],"scope":"focus_ayah","source_local_id":"100:9:7:2","source_type":"qac_morpheme","support_ids":["sup_edab5bc9a880cfbf185e"],"title":"QAC root occurrence: ق ب ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["100:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:9","branch_refs":["root_000130/B001","root_001040/B001","root_001195/B001"],"candidate_id":"cand_cf7e3bede216562d291f","commentary_obligation":"review","hft_ref":"hft_528e30e349952bddd406","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_unveiling_threshold","source_type":"hft","support_ids":["sup_2ac542177bd28ea0dfdb"],"title":"base_unveiling_threshold","trust":"legacy_unbound"},{"anchor_refs":["100:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:9","branch_refs":["root_000130/B002","root_000130/B003","root_001040/B001","root_001195/B002"],"candidate_id":"cand_24cddf9c024e1c3acc80","commentary_obligation":"review","hft_ref":"hft_4ba920f82ada344e3bcf","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_container_reversal","source_type":"hft","support_ids":["sup_8be49e51a89e2d628b74"],"title":"base_container_reversal","trust":"legacy_unbound"},{"anchor_refs":["100:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:9","branch_refs":["root_000130/B002","root_001040/B002","root_001195/B002"],"candidate_id":"cand_d31695c8ece2465a1236","commentary_obligation":"review","hft_ref":"hft_2a3c2e8035a62d653ac9","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_trace_identification","source_type":"hft","support_ids":["sup_d11e43af5856b12e3d7e"],"title":"base_trace_identification","trust":"legacy_unbound"},{"anchor_refs":["100:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:9","branch_refs":["root_000130/B003","root_001040/B005","root_001195/B002"],"candidate_id":"cand_55a67f901f4baabb49c0","commentary_obligation":"review","hft_ref":"hft_69c981dad64da4ec9e0b","kind":"surprising_outlier","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:outlier_fluid_container_failure","source_type":"hft","support_ids":["sup_1da28a5555193d9c8027"],"title":"outlier_fluid_container_failure","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"۞ أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|A:INTG+","morpheme_role":"PREFIX","pos":"INTG","qac_ref":"100:9:1:1","qac_word_ref":"100:9:1","root_ar":"","surface_ar":"أَ"},{"lemma_ar":"","morph_features":"PREFIX|f:SUP+","morpheme_role":"PREFIX","pos":"SUP","qac_ref":"100:9:1:2","qac_word_ref":"100:9:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"100:9:1:3","qac_word_ref":"100:9:1","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:9:2:1","qac_word_ref":"100:9:2","root_ar":"ع ل م","surface_ar":"يَعْلَمُ"},{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"100:9:3:1","qac_word_ref":"100:9:3","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"بُعْثِرَ","morph_features":"STEM|POS:V|PERF|PASS|LEM:buEovira|ROOT:bEvr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:9:4:1","qac_word_ref":"100:9:4","root_ar":"ب ع ث ر","surface_ar":"بُعْثِرَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:REL|LEM:maA","morpheme_role":"STEM","pos":"REL","qac_ref":"100:9:5:1","qac_word_ref":"100:9:5","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"100:9:6:1","qac_word_ref":"100:9:6","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"100:9:7:1","qac_word_ref":"100:9:7","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"قَبْر","morph_features":"STEM|POS:N|LEM:qabor|ROOT:qbr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:9:7:2","qac_word_ref":"100:9:7","root_ar":"ق ب ر","surface_ar":"قُبُورِ"}],"word_analysis_qac_refs":[["100:9:1:1","100:9:1:2"],["100:9:1:3"],["100:9:2:1"],["100:9:3:1"],["100:9:4:1"],["100:9:5:1"],["100:9:6:1"],["100:9:7:1","100:9:7:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["100:9:1","100:9:2","100:9:3","100:9:4","100:9:5","100:9:6","100:9:7","100:9:8"]},"focus_surface_evidence":{"arabic_uthmani":"۞ أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|A:INTG+","morpheme_role":"PREFIX","pos":"INTG","qac_ref":"100:9:1:1","qac_word_ref":"100:9:1","root_ar":"","surface_ar":"أَ"},{"lemma_ar":"","morph_features":"PREFIX|f:SUP+","morpheme_role":"PREFIX","pos":"SUP","qac_ref":"100:9:1:2","qac_word_ref":"100:9:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"100:9:1:3","qac_word_ref":"100:9:1","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:9:2:1","qac_word_ref":"100:9:2","root_ar":"ع ل م","surface_ar":"يَعْلَمُ"},{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"100:9:3:1","qac_word_ref":"100:9:3","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"بُعْثِرَ","morph_features":"STEM|POS:V|PERF|PASS|LEM:buEovira|ROOT:bEvr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:9:4:1","qac_word_ref":"100:9:4","root_ar":"ب ع ث ر","surface_ar":"بُعْثِرَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:REL|LEM:maA","morpheme_role":"STEM","pos":"REL","qac_ref":"100:9:5:1","qac_word_ref":"100:9:5","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"100:9:6:1","qac_word_ref":"100:9:6","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"100:9:7:1","qac_word_ref":"100:9:7","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"قَبْر","morph_features":"STEM|POS:N|LEM:qabor|ROOT:qbr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:9:7:2","qac_word_ref":"100:9:7","root_ar":"ق ب ر","surface_ar":"قُبُورِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["100:9:1:1","100:9:1:2"],["100:9:1:3"],["100:9:2:1"],["100:9:3:1"],["100:9:4:1"],["100:9:5:1"],["100:9:6:1"],["100:9:7:1","100:9:7:2"]],"word_analysis_refs":["100:9:1","100:9:2","100:9:3","100:9:4","100:9:5","100:9:6","100:9:7","100:9:8"],"word_rows":[{"analysis_record_ref":"100:9:1","analytic_gloss_range_en":"fused interrogative and consequential opening that turns the preceding diagnosis into a rhetorical challenge","analytic_root_gloss_range_en":null,"qac_refs":["100:9:1:1","100:9:1:2"],"root":{},"surface":{"arabic":"أَفَ","transliteration":"a-fa"}},{"analysis_record_ref":"100:9:2","analytic_gloss_range_en":"negator scoped over the cognition verb inside a rhetorical question","analytic_root_gloss_range_en":null,"qac_refs":["100:9:1:3"],"root":{},"surface":{"arabic":"لَا","transliteration":"lā"}},{"analysis_record_ref":"100:9:3","analytic_gloss_range_en":"present knowing, perceiving, or recognizing, here objectless inside a rebuking rhetorical question","analytic_root_gloss_range_en":"knowledge and recognition are locally selected; the mark/sign branch supplies recognition pressure, while unrelated branch images are not active","qac_refs":["100:9:2:1"],"root":{"arabic":"ع ل م","transliteration":"ʿ-l-m"},"surface":{"arabic":"يَعْلَمُ","transliteration":"yaʿlamu"}},{"analysis_record_ref":"100:9:4","analytic_gloss_range_en":"temporal-conditional particle that introduces a certain future event-scene and can pull the syntax forward","analytic_root_gloss_range_en":null,"qac_refs":["100:9:3:1"],"root":{},"surface":{"arabic":"إِذَا","transliteration":"idhā"}},{"analysis_record_ref":"100:9:5","analytic_gloss_range_en":"passive perfect of a rare quadriliteral verb for violent overturning, scattering, exhuming, and disclosure of buried contents","analytic_root_gloss_range_en":"upturning buried contents is locally primary; scattering into disorder and forceful inversion sharpen the image, while variant search/investigation readings are apparatus-level contrasts","qac_refs":["100:9:4:1"],"root":{"arabic":"ب ع ث ر","transliteration":"b-ʿ-th-r"},"surface":{"arabic":"بُعْثِرَ","transliteration":"buʿthira"}},{"analysis_record_ref":"100:9:6","analytic_gloss_range_en":"headless relative pronoun functioning as passive subject and keeping the grave-contents unspecified","analytic_root_gloss_range_en":null,"qac_refs":["100:9:5:1"],"root":{},"surface":{"arabic":"مَا","transliteration":"mā"}},{"analysis_record_ref":"100:9:7","analytic_gloss_range_en":"preposition of containment that binds the unspecified contents to the grave-field","analytic_root_gloss_range_en":null,"qac_refs":["100:9:6:1"],"root":{},"surface":{"arabic":"فِى","transliteration":"fī"}},{"analysis_record_ref":"100:9:8","analytic_gloss_range_en":"definite plural graves as concrete containment-sites, governed by the preposition and selected for concealment being overturned","analytic_root_gloss_range_en":"burial and grave-place are locally primary; hiddenness and concealment sharpen the image, while unrelated bird and idiom branches are inactive","qac_refs":["100:9:7:1","100:9:7:2"],"root":{"arabic":"ق ب ر","transliteration":"q-b-r"},"surface":{"arabic":"ٱلْقُبُورِ","transliteration":"al-qubūr"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":8,"words_total":8,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["100:9"],"branch_refs":["root_000130/B001","root_001040/B001","root_001195/B001"],"candidate_id":"cand_cf7e3bede216562d291f","evidence_scope":"focus_ayah","hft_ref":"hft_528e30e349952bddd406","item_id":"base_unveiling_threshold","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_unveiling_threshold","support_id":"sup_2ac542177bd28ea0dfdb"},{"anchor_refs":["100:9"],"branch_refs":["root_000130/B002","root_000130/B003","root_001040/B001","root_001195/B002"],"candidate_id":"cand_24cddf9c024e1c3acc80","evidence_scope":"focus_ayah","hft_ref":"hft_4ba920f82ada344e3bcf","item_id":"base_container_reversal","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_container_reversal","support_id":"sup_8be49e51a89e2d628b74"},{"anchor_refs":["100:9"],"branch_refs":["root_000130/B002","root_001040/B002","root_001195/B002"],"candidate_id":"cand_d31695c8ece2465a1236","evidence_scope":"focus_ayah","hft_ref":"hft_2a3c2e8035a62d653ac9","item_id":"base_trace_identification","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_trace_identification","support_id":"sup_d11e43af5856b12e3d7e"},{"anchor_refs":["100:9"],"branch_refs":["root_000130/B003","root_001040/B005","root_001195/B002"],"candidate_id":"cand_55a67f901f4baabb49c0","evidence_scope":"focus_ayah","hft_ref":"hft_69c981dad64da4ec9e0b","item_id":"outlier_fluid_container_failure","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_fluid_container_failure","support_id":"sup_1da28a5555193d9c8027"}],"diagnostics":[{"warning":"Unrecognized HFT reader field is preserved as a global review record"},{"warning":"Unrecognized HFT reader field is preserved as a global review record"}],"lane_counts":{"global":13,"macro":11,"micro":4},"packet_summary":{"ayah_count":11,"focus_ref":"100:9","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ع د و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000993","furuq_root_norm":"ع د و","furuq_source_root_norm":"ع د و","is_dominant":true,"target_occurrences":68,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":5,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":false,"target_occurrences":4,"target_rank":3}]},{"qac_root":"ث و ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000210","furuq_root_norm":"ث و ر","furuq_source_root_norm":"ث و ر","is_dominant":true,"target_occurrences":4,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000011","furuq_root_norm":"ء ث ر","furuq_source_root_norm":"أ ث ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["100:1","100:2","100:3","100:4","100:5","100:6","100:7","100:8","100:9","100:10","100:11"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"100:9","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v3","reader_id":"reader_hft_a","trace_kind":null}]},"reader_synthesis_count":11,"source_present":true,"structured_insight_count":15,"unstructured_record_count":2},"identity":{"ayah_ref":"100:9","lane":"micro","linguistic_source_ref":"100:9","surface_ref":"100:9","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"100:9","target_tokens":[["Öyleyse",["100:9:1"]],["bilmez",["100:9:1","100:9:2"]],["mi",["100:9:1"]],["ki",["100:9:2"]],["mezarlarda",["100:9:6","100:9:7"]],["olanlar",["100:9:5"]],["dışarı",["100:9:4"]],["çıkarıldığında",["100:9:3","100:9:4"]]],"text":"Öyleyse bilmez mi ki mezarlarda olanlar dışarı çıkarıldığında,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s100-p01-001-011","label":"Whole surah","number":1,"refs":["100:1","100:2","100:3","100:4","100:5","100:6","100:7","100:8","100:9","100:10","100:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:2:rhetorical-negative-force","source_type":"word_analysis","support_id":"sup_0171a7c366589d83d7a4","text":"{\"blocking_evidence\":null,\"headline\":\"negation becomes rebuke\",\"reader_payoff\":\"The reader notices that the rhetorical negative expects recognition and treats failure to know as blameworthy.\",\"reason\":\"The surrounding interrogative and prior human exposure support rhetorical rebuke rather than a plain negative statement.\",\"representative_source_ids\":[\"MG-490565cb\",\"QS-aa213575\",\"QI-ca472d42\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"100:9:4:1","source_type":"qac_morpheme","support_id":"sup_03eb5cfd26299a79f12c","text":"{\"lemma_ar\":\"بُعْثِرَ\",\"morph_features\":\"STEM|POS:V|PERF|PASS|LEM:buEovira|ROOT:bEvr|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"100:9:4:1\",\"qac_word_ref\":\"100:9:4\",\"root_ar\":\"ب ع ث ر\",\"surface_ar\":\"بُعْثِرَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:1:rebuke-and-register-shift","source_type":"word_analysis","support_id":"sup_14969907a88cac726194","text":"{\"blocking_evidence\":null,\"headline\":\"rebuke after diagnosis\",\"reader_payoff\":\"The reader notices the register shift from describing the human to confronting him with culpable recognition.\",\"reason\":\"The interrogative form, negation, and preceding discourse make ordinary information-seeking implausible; the question functions as rebuke.\",\"representative_source_ids\":[\"MG-7568cf9a\",\"MG-b6aa7f4a\",\"QI-ee1743fc\",\"QB-c2ac66d3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:6:unspecified-relative-scope","source_type":"word_analysis","support_id":"sup_21b7657affdc8b47c708","text":"{\"blocking_evidence\":null,\"headline\":\"unspecified contents remain open\",\"reader_payoff\":\"The reader notices that the grammar identifies the slot but refuses to narrow what exactly is in the graves.\",\"reason\":\"QAC and attachment evidence identify a headless relative pronoun, and translation support warns against adding an explanatory noun.\",\"representative_source_ids\":[\"QG-2d6ec203\",\"MG-ae948bd7\",\"QS-1c0f6931\",\"QY-ab58f789\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:6:outer-inner-ma-echo","source_type":"word_analysis","support_id":"sup_3778efc7bb7894354751","text":"{\"blocking_evidence\":null,\"headline\":\"outer phrase anticipates inner phrase\",\"reader_payoff\":\"The reader notices that the phrase about what is in graves anticipates what is in breasts in the supplied continuation (100:10).\",\"reason\":\"The supplied context window and CRITICAL row explicitly link the 100:9 phrase with the 100:10 inner-disclosure phrase.\",\"representative_source_ids\":[\"QE-b5d7ad97\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"100:9:2:1","source_type":"qac_morpheme","support_id":"sup_3b22687fc047e7f94f31","text":"{\"lemma_ar\":\"عَلِمَ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"100:9:2:1\",\"qac_word_ref\":\"100:9:2\",\"root_ar\":\"ع ل م\",\"surface_ar\":\"يَعْلَمُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:3:sound-link-to-opening","source_type":"word_analysis","support_id":"sup_3bba4f5d7692d99fc9cc","text":"{\"blocking_evidence\":null,\"headline\":\"secondary sound link\",\"reader_payoff\":\"The reader notices a secondary sound echo that ties the cognitive challenge back to the surah's earlier driven motion.\",\"reason\":\"The row itself limits the sound connection to a supplied echo rather than making it the main argument, so it survives as a modest recitational observation.\",\"representative_source_ids\":[\"QP-25fb543f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:7:recitational-binding","source_type":"word_analysis","support_id":"sup_41ec0d7e5df7fa40e023","text":"{\"blocking_evidence\":null,\"headline\":\"liaison binds the phrase\",\"reader_payoff\":\"The reader notices that the recited link into the grave noun audibly binds preposition and governed noun.\",\"reason\":\"The recitational observation supports the already forced grammatical binding, so it survives as a secondary payoff.\",\"representative_source_ids\":[\"QP-38e732bc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:5:violent-disclosure-lexis","source_type":"word_analysis","support_id":"sup_43237b49ee0493e938de","text":"{\"blocking_evidence\":null,\"headline\":\"overturning exposes what was hidden\",\"reader_payoff\":\"The reader notices that the verb pictures disclosure through forceful overturning and scattering, not merely resurrection in abstract terms.\",\"reason\":\"V4 supports upturning buried contents and scattering into disorder, and the local grave-content subject selects disclosure through upheaval.\",\"representative_source_ids\":[\"QS-b1413e1a\",\"QS-b4cd3abf\",\"QS-e69ebe3e\",\"QF-fad0f1f0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:7:containment-focus","source_type":"word_analysis","support_id":"sup_52e04c97c62d5a0671d1","text":"{\"blocking_evidence\":null,\"headline\":\"inside relation becomes visible\",\"reader_payoff\":\"The reader notices that the preposition foregrounds hidden-inward containment before the verb overturns it.\",\"reason\":\"The preposition governs the grave noun and completes the phrase defining what is inside the graves.\",\"representative_source_ids\":[\"QG-7db263b2\",\"MG-6bf39a6e\",\"QS-591cd55f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:2","source_type":"word_analysis","support_id":"sup_5487976aae2f7b4bf184","text":"{\"gloss_range\":\"negator scoped over the cognition verb inside a rhetorical question\",\"prose\":\"{{ar:لَا}} ({{tr:lā}}) fixes the polarity of {{ar:يَعْلَمُ}} ({{tr:yaʿlamu}}), not of the later grave-upheaval clause. Inside {{ar:أَفَلَا يَعْلَمُ}} ({{tr:a-fa-lā yaʿlamu}}), the negation is not a neutral report that the human lacks information; the rhetorical question presses toward the opposite recognition and makes ignorance culpable. It also completes the first beat before {{ar:إِذَا}} ({{tr:idhā}}) opens the event scene, so the reader hears the failure of knowing before seeing what will be disclosed.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَا}} ({{tr:lā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:4:certain-when-clause","source_type":"word_analysis","support_id":"sup_6d2d4ac55b1f326bf8b6","text":"{\"blocking_evidence\":null,\"headline\":\"certain future when-scene\",\"reader_payoff\":\"The reader notices that the future event is framed as certain in a temporal-conditional form, not as a speculative possibility.\",\"reason\":\"QAC identifies a temporal-conditional particle governing the perfect passive, and attachment support says the clause supplies the setting for the knowing question.\",\"representative_source_ids\":[\"QG-780214e0\",\"MG-2ea004b8\",\"QS-923ee975\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:5:passive-perfect-certainty","source_type":"word_analysis","support_id":"sup_6f3e10c73879e0365b92","text":"{\"blocking_evidence\":null,\"headline\":\"passive perfect certainty\",\"reader_payoff\":\"The reader notices an unavoidable event in which the agent is suppressed and the affected buried contents move to the center.\",\"reason\":\"The local verb is passive perfect with an unresolved implicit agent, and {{ar:مَا}} ({{tr:mā}}) is the syntactically forced passive subject.\",\"representative_source_ids\":[\"QG-77308e91\",\"QG-dfe338a7\",\"QT-759ce8fb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:8:genitive-container-role","source_type":"word_analysis","support_id":"sup_7228a526d04b66b25656","text":"{\"blocking_evidence\":null,\"headline\":\"container, not subject\",\"reader_payoff\":\"The reader notices that the graves provide the container location, while the unspecified contents occupy the passive subject slot.\",\"reason\":\"Attachment evidence makes the noun the governed complement of {{ar:فِى}} ({{tr:fī}}), not the subject of {{ar:بُعْثِرَ}} ({{tr:buʿthira}}).\",\"representative_source_ids\":[\"QG-51974365\",\"QG-58de2c2a\",\"QT-5c9ab9c1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:8:outer-inner-disclosure-pair","source_type":"word_analysis","support_id":"sup_74f70a81dc629ce376dc","text":"{\"blocking_evidence\":null,\"headline\":\"outer concealment anticipates inner concealment\",\"reader_payoff\":\"The reader notices that the grave-contents phrase prepares the breast-contents phrase in 100:10, forming an outer-to-inner exposure sequence.\",\"reason\":\"The supplied context and CRITICAL bridge rows explicitly connect the grave phrase in 100:9 with the breast phrase in 100:10.\",\"representative_source_ids\":[\"QE-a5ec184b\",\"QB-c2817af2\",\"QY-653f593d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:8:marked-82-4-contrast","source_type":"word_analysis","support_id":"sup_7c3c8932cb3e2d1a0c7d","text":"{\"blocking_evidence\":null,\"headline\":\"marked pair refocused from 82:4\",\"reader_payoff\":\"The reader notices that 100:9 inherits the grave-overturning formula from 82:4 while shifting attention from graves themselves to what is inside them.\",\"reason\":\"The supplied co-occurrence evidence links {{ar:ق ب ر}} ({{tr:q-b-r}}) with {{ar:ب ع ث ر}} ({{tr:b-ʿ-th-r}}), and the CRITICAL rows name the concrete 82:4 parallel.\",\"representative_source_ids\":[\"QI-8a5ffcdd\",\"QI-e5eb2aa0\",\"QE-8d20d96f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:1:consequence-scoped-question","source_type":"word_analysis","support_id":"sup_806ed96f82eb861c7b1b","text":"{\"blocking_evidence\":null,\"headline\":\"question as consequence\",\"reader_payoff\":\"The reader notices that the question is drawn out of the preceding diagnosis (100:6-8), not introduced as an unrelated reflection.\",\"reason\":\"QAC identifies interrogative hamza fused with consequential {{tr:fāʾ}}, and attachment support marks the whole opening as a rhetorical verbal question.\",\"representative_source_ids\":[\"QG-b275db3e\",\"QS-e4e606d6\",\"QB-f54cbc0d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:4","source_type":"word_analysis","support_id":"sup_82a0f599584f92e1f506","text":"{\"gloss_range\":\"temporal-conditional particle that introduces a certain future event-scene and can pull the syntax forward\",\"prose\":\"{{ar:إِذَا}} ({{tr:idhā}}) turns the second half of the ayah into a when-scene, not a loose time phrase. Because the following verb is perfect in form, the future grave-upheaval is presented with certainty: the question is oriented toward when that exposure arrives, not whether it will arrive. The supplied parallels place this in a recognizable Last Day when-plus-perfect pattern (81:1; 82:3; 82:4), with 82:4 also showing the grave-overturning scene that 100:9 refocuses around contents. The particle also has conditional force, so it can hold the reader forward through the supplied continuation until the fuller consequence and divine knowing closure appear (100:11). Locally, though, it already supplies the temporal setting for {{ar:يَعْلَمُ}} ({{tr:yaʿlamu}}): the knowledge question is tested against the coming exposure scene.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِذَا}} ({{tr:idhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:6","source_type":"word_analysis","support_id":"sup_82d134828227545b66a8","text":"{\"gloss_range\":\"headless relative pronoun functioning as passive subject and keeping the grave-contents unspecified\",\"prose\":\"{{ar:مَا}} ({{tr:mā}}) is small but it controls the scene. Grammatically it is the overt passive subject of {{ar:بُعْثِرَ}} ({{tr:buʿthira}}), so the affected contents are promoted into the clause's main position. Semantically it refuses to name exactly what fills that slot: bodies, deeds, records, or hidden contents are not separated out by the wording. The possible interrogative pressure is narrowed by the local parse, because the attachment evidence reads it as a relative pronoun, but the open surface still keeps the contents question-like. That openness matters for the supplied next ayah too: {{ar:مَا فِى ٱلْقُبُورِ}} ({{tr:mā fī al-qubūr}}) prepares the paired inner phrase in 100:10, so external and internal hidden things are brought under one disclosure movement.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مَا}} ({{tr:mā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:3","source_type":"word_analysis","support_id":"sup_8b986c0372dd46981bc6","text":"{\"gloss_range\":\"present knowing, perceiving, or recognizing, here objectless inside a rebuking rhetorical question\",\"prose\":\"{{ar:يَعْلَمُ}} ({{tr:yaʿlamu}}) carries the challenge through a simple Form I imperfect: the issue is the human's own present awareness, not being taught by someone else. The verb is left without an explicit object, so the reader must let the following exposure sequence fill the pressure: what should he know when grave-contents are overturned and, in the supplied continuation, breast-contents are disclosed (100:10)? Its subject remains the same human introduced in 100:6 and described through 100:8, so the ayah pivots from intense attachment to deficient recognition. The question also points forward: human knowing is challenged here before the supplied closure names divine full awareness (100:11), while a secondary ʿayn echo ties the cognition verb back to the surah's earlier driven motion. The {{ar:ع ل م}} ({{tr:ʿ-l-m}}) root's mark/sign family is only a narrowed background here: the local verb means knowing or recognizing, while the coming disclosure makes hidden reality readable.\",\"root_display\":\"{{ar:ع ل م}} ({{tr:ʿ-l-m}})\",\"root_gloss_range\":\"knowledge and recognition are locally selected; the mark/sign branch supplies recognition pressure, while unrelated branch images are not active\",\"surface_display\":\"{{ar:يَعْلَمُ}} ({{tr:yaʿlamu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:5:raising-and-finding-pressure","source_type":"word_analysis","support_id":"sup_8f0a26cb0a75ced2c48c","text":"{\"blocking_evidence\":null,\"headline\":\"raising with discovery pressure\",\"reader_payoff\":\"The reader notices that the debated root analysis makes resurrection and discovery press together, while the local sense remains the quadriliteral passive overturning verb.\",\"reason\":\"The derivational debate is meaningful but should not replace the local lexical unit with two separate triliteral roots; it is kept as semantic pressure.\",\"representative_source_ids\":[\"QS-d6cf8a34\",\"MH-1b610b72\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:8:concealment-site-reversed","source_type":"word_analysis","support_id":"sup_8f138faafc887292b4c9","text":"{\"blocking_evidence\":null,\"headline\":\"burial concealment overturned\",\"reader_payoff\":\"The reader notices that a grave is a concealment-site whose function is being reversed, while the physical grave sense remains primary.\",\"reason\":\"V4 supports burial and hiddenness branches, but local grammar selects the concrete grave noun; broader repository language is retained only as concealment pressure.\",\"representative_source_ids\":[\"QS-343254db\",\"QS-547ac147\",\"QS-edc5e298\",\"QI-f8ad9952\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:3:present-accountability","source_type":"word_analysis","support_id":"sup_9001100394f95c597a1e","text":"{\"blocking_evidence\":null,\"headline\":\"present cognitive accountability\",\"reader_payoff\":\"The reader notices that the ayah challenges present awareness through direct knowing rather than merely forecasting later realization.\",\"reason\":\"The imperfect Form I cognition verb stands inside a negated rhetorical frame, selecting knowing, perceiving, and recognizing as the response channel.\",\"representative_source_ids\":[\"QG-b65fc4f4\",\"QS-4fef5e4a\",\"QF-86205e70\",\"QI-0906c356\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:8:definite-plural-totality","source_type":"word_analysis","support_id":"sup_9d65e561ff7492ee248f","text":"{\"blocking_evidence\":null,\"headline\":\"definite plural grave-field\",\"reader_payoff\":\"The reader notices a concrete, countable, total grave-field rather than a single grave-image or an abstract idea of death.\",\"reason\":\"QAC and noun-instance evidence identify a definite plural concrete noun governed by the preposition.\",\"representative_source_ids\":[\"QG-ac83c109\",\"QF-1235fb26\",\"QF-9de9793f\",\"MS-04ff8422\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:3:objectless-knowing","source_type":"word_analysis","support_id":"sup_a41d587e90b77e710742","text":"{\"blocking_evidence\":null,\"headline\":\"objectless knowing opens scope\",\"reader_payoff\":\"The reader notices that the verb withholds its object, forcing the following disclosure sequence to answer what the human should know.\",\"reason\":\"The local verb instance is marked with no surfaced object, and translation support warns against supplying a narrow object if compression can be preserved.\",\"representative_source_ids\":[\"QG-0ecedae0\",\"MG-a7736860\",\"QI-76b40ec3\",\"QT-2356e0b3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:3:recognition-and-sign-pressure","source_type":"word_analysis","support_id":"sup_a6875cb64451dee5194d","text":"{\"blocking_evidence\":null,\"headline\":\"knowledge as recognition\",\"reader_payoff\":\"The reader notices that knowing here includes recognition of exposed signs, while the local verb still selects cognition rather than a separate mark noun.\",\"reason\":\"V4 supports both knowledge and mark/sign branches for the root, but the local Form I verb selects knowing or recognizing; the mark field is retained only as recognition pressure.\",\"representative_source_ids\":[\"QS-021ff275\",\"QS-2a1604e5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:8","source_type":"word_analysis","support_id":"sup_a79c0a2ab8bfdb6e3be0","text":"{\"gloss_range\":\"definite plural graves as concrete containment-sites, governed by the preposition and selected for concealment being overturned\",\"prose\":\"{{ar:ٱلْقُبُورِ}} ({{tr:al-qubūr}}) lands the ayah on the place of concealment. It is not the passive subject; attachment evidence makes it the genitive complement governed by {{ar:فِى}} ({{tr:fī}}), while {{ar:مَا}} ({{tr:mā}}) carries the subject role. Its definite plural form gathers the grave-field as a concrete totality: many countable repositories, not a single symbolic grave. The {{ar:ق ب ر}} ({{tr:q-b-r}}) root's burial and concealment field is locally active because the phrase names places whose hiding function is being reversed by {{ar:بُعْثِرَ}} ({{tr:buʿthira}}). The supplied 82:4 echo keeps the rare grave-overturning formula in view, but 100:9 refocuses it from containers to contents. The final sound and forward bridge also prepare 100:10, where concealed breast-contents answer the concealed grave-contents, making {{ar:ٱلْقُبُورِ}} ({{tr:al-qubūr}}) the outer half of a total-disclosure sequence.\",\"root_display\":\"{{ar:ق ب ر}} ({{tr:q-b-r}})\",\"root_gloss_range\":\"burial and grave-place are locally primary; hiddenness and concealment sharpen the image, while unrelated bird and idiom branches are inactive\",\"surface_display\":\"{{ar:ٱلْقُبُورِ}} ({{tr:al-qubūr}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:1:fused-opening-form","source_type":"word_analysis","support_id":"sup_a9058078c7984fb5427d","text":"{\"blocking_evidence\":null,\"headline\":\"compressed particle fusion\",\"reader_payoff\":\"The reader notices that interrogation and consequence are compressed before the negator and verb arrive, making the transition feel immediate.\",\"reason\":\"The surface particle is a fused written unit before {{ar:لَا يَعْلَمُ}} ({{tr:lā yaʿlamu}}), so the first beat launches the interrogative section.\",\"representative_source_ids\":[\"QF-1b772b41\",\"QT-217931e8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:5","source_type":"word_analysis","support_id":"sup_b1db4b703a414aebe2f2","text":"{\"gloss_range\":\"passive perfect of a rare quadriliteral verb for violent overturning, scattering, exhuming, and disclosure of buried contents\",\"prose\":\"{{ar:بُعْثِرَ}} ({{tr:buʿthira}}) is the event center of the when-clause. As a passive perfect after {{ar:إِذَا}} ({{tr:idhā}}), it makes the future upheaval sound completed and unavoidable, while suppressing any named agent so the buried contents become the grammatical focus. The local field is not gentle rising: V4 and the CRITICAL rows converge on overturning earth, scattering, exhuming, and bringing hidden material out. The rare root has only the supplied parallel at 82:4, where the graves themselves are overturned; here the same resurrection formula is reshaped around {{ar:مَا فِى ٱلْقُبُورِ}} ({{tr:mā fī al-qubūr}}), the contents inside them. Variant pressures toward active voice or search language are useful contrasts, including the digging reversal linked to 5:31, but the standard local reading keeps the passive quadriliteral force: disclosure happens through violent upheaval, not through a named investigator. Even the sound texture stays secondary but concrete: hard onset, guttural, fricative, and liquid consonants suit rupture and scattering.\",\"root_display\":\"{{ar:ب ع ث ر}} ({{tr:b-ʿ-th-r}})\",\"root_gloss_range\":\"upturning buried contents is locally primary; scattering into disorder and forceful inversion sharpen the image, while variant search/investigation readings are apparatus-level contrasts\",\"surface_display\":\"{{ar:بُعْثِرَ}} ({{tr:buʿthira}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:5:burial-reversal-5-31","source_type":"word_analysis","support_id":"sup_b62fc026b83a308f61bf","text":"{\"blocking_evidence\":null,\"headline\":\"digging reversal in apparatus\",\"reader_payoff\":\"The reader notices that search-root variants can make the burial lesson of 5:31 reverse into exposure, while that contrast remains variant pressure rather than the canonical parse.\",\"reason\":\"The 5:31 link depends on b-h-th variant pressure, so it survives as apparatus-level contrast and does not govern the standard {{ar:بُعْثِرَ}} ({{tr:buʿthira}}) reading.\",\"representative_source_ids\":[\"QI-b2da88b7\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:8:ayah-ending-concealment","source_type":"word_analysis","support_id":"sup_bdc5ac16c6fa513b8ec1","text":"{\"blocking_evidence\":null,\"headline\":\"ending lands on concealment\",\"reader_payoff\":\"The reader notices that the ayah ends at the very place of concealment after the verb has announced its exposure.\",\"reason\":\"The noun is the final word of the ayah and completes the containment phrase, so the closure observation is locally grounded.\",\"representative_source_ids\":[\"QT-b18059db\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:4:second-beat-event-frame","source_type":"word_analysis","support_id":"sup_be207a31ccf7a323b811","text":"{\"blocking_evidence\":null,\"headline\":\"second beat opens the scene\",\"reader_payoff\":\"The reader notices the ayah's two-part architecture: first a knowledge question, then the scene that makes that knowledge unavoidable.\",\"reason\":\"Attachment constraints divide the ayah into a rhetorical verbal question and a temporal clause, matching the CRITICAL two-beat observation.\",\"representative_source_ids\":[\"QT-6224cef4\",\"QT-67ec2dd9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:7:contents-not-containers","source_type":"word_analysis","support_id":"sup_beb1ed7b03450e186f6d","text":"{\"blocking_evidence\":null,\"headline\":\"contents rather than containers\",\"reader_payoff\":\"The reader notices the contrast with 82:4: 100:9 turns attention from the graves themselves to what they contain.\",\"reason\":\"The supplied 82:4 parallel lacks this prepositional contents phrase, while local syntax makes {{ar:فِى ٱلْقُبُورِ}} ({{tr:fī al-qubūr}}) complete the relative subject.\",\"representative_source_ids\":[\"QT-814a470e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:6:passive-subject-promotion","source_type":"word_analysis","support_id":"sup_c2b89364e4c52e3dd1e6","text":"{\"blocking_evidence\":null,\"headline\":\"contents become subject\",\"reader_payoff\":\"The reader notices that the passive grammar makes the buried contents the scene center rather than leaving them as a mere object.\",\"reason\":\"Attachment evidence marks {{ar:مَا}} ({{tr:mā}}) as the overt passive subject of {{ar:بُعْثِرَ}} ({{tr:buʿthira}}).\",\"representative_source_ids\":[\"QG-0341a8c9\",\"QT-b1528279\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:6:interrogative-pressure","source_type":"word_analysis","support_id":"sup_c4d295d83af6873bdd21","text":"{\"blocking_evidence\":null,\"headline\":\"question-like openness\",\"reader_payoff\":\"The reader notices that the contents remain question-like, while the local syntax still requires a relative subject reading.\",\"reason\":\"The interrogative pressure is plausible as a semantic effect, but the forced local role is relative pronoun subject.\",\"representative_source_ids\":[\"QF-6be3fd53\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:7:relative-phrase-completion","source_type":"word_analysis","support_id":"sup_c4e4106d12074fdf502b","text":"{\"blocking_evidence\":null,\"headline\":\"phrase completes the subject\",\"reader_payoff\":\"The reader notices that the prepositional phrase is not ornamental; it completes the subject phrase around which the passive clause is built.\",\"reason\":\"Attachment evidence makes the PP the complement specifying the headless relative contents.\",\"representative_source_ids\":[\"QT-9e07579c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:5:rupture-sound","source_type":"word_analysis","support_id":"sup_c8fd7c4c412d051db468","text":"{\"blocking_evidence\":null,\"headline\":\"consonants suit rupture\",\"reader_payoff\":\"The reader notices a secondary sound texture that suits the image of buried contents being broken open and scattered.\",\"reason\":\"The phonetic claim is not contradicted and remains secondary to the grammar and lexicon.\",\"representative_source_ids\":[\"QP-cb02d833\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:4:forward-protasis-pull","source_type":"word_analysis","support_id":"sup_ca00b4bda7e491253070","text":"{\"blocking_evidence\":null,\"headline\":\"syntax pulls toward closure\",\"reader_payoff\":\"The reader notices that the when-frame can keep the resurrection scene open until the divine knowing closure (100:11), while the local ayah still functions as the setting for the knowledge question.\",\"reason\":\"The supplied context supports a continuation through 100:11, but attachment evidence also marks the {{ar:إِذَا}} ({{tr:idhā}}) clause as the local adverbial setting for {{ar:يَعْلَمُ}} ({{tr:yaʿlamu}}), so the claim is narrowed rather than made exclusive.\",\"representative_source_ids\":[\"QG-f9768043\",\"QI-2dc12de5\",\"MI-b37d1080\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:2:negated-cognition-scope","source_type":"word_analysis","support_id":"sup_cb74b56525c7e8746f81","text":"{\"blocking_evidence\":null,\"headline\":\"negation scopes over knowing\",\"reader_payoff\":\"The reader notices that the negation targets the human's knowing before the resurrection scene is unfolded.\",\"reason\":\"QAC identifies the particle as negating the imperfect verb, and attachment evidence divides the first beat from the following temporal clause.\",\"representative_source_ids\":[\"QG-bbb86777\",\"QT-562a8f84\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:8:audible-ur-link","source_type":"word_analysis","support_id":"sup_d43fab1205a18ca17f81","text":"{\"blocking_evidence\":null,\"headline\":\"ending sound links forward\",\"reader_payoff\":\"The reader notices that the final sound prepares the matching ending of the supplied next phrase in 100:10.\",\"reason\":\"The fawāṣil link is a secondary sound observation tied to the concrete 100:10 continuation.\",\"representative_source_ids\":[\"QP-cd6a0d35\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:5:external-to-internal-disclosure","source_type":"word_analysis","support_id":"sup_e0fc32e3e3d252ac1005","text":"{\"blocking_evidence\":null,\"headline\":\"outer disclosure begins the pair\",\"reader_payoff\":\"The reader notices that this external exposure of grave-contents prepares the inner exposure of breast-contents in the supplied next ayah (100:10).\",\"reason\":\"The supplied context window and CRITICAL bridge rows support a forward relation from grave disclosure to the next inner-disclosure phrase (100:10).\",\"representative_source_ids\":[\"QB-844e1ec4\",\"QB-e7913d11\",\"QY-f02300fc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:5:rare-82-4-pairing","source_type":"word_analysis","support_id":"sup_e4eb8ca5050372c17519","text":"{\"blocking_evidence\":null,\"headline\":\"rare grave-overturning pair\",\"reader_payoff\":\"The reader notices that the rare root and its grave pairing at 82:4 make this a marked resurrection formula, not an incidental verb choice.\",\"reason\":\"Contextual evidence marks the root as low occurrence with a supplied grave-pairing parallel, and the CRITICAL rows give the concrete reference 82:4.\",\"representative_source_ids\":[\"QI-1379b233\",\"QI-589b77e2\",\"QE-6b71cbb4\",\"QH-80057c72\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:1","source_type":"word_analysis","support_id":"sup_e53f9f6fd2b654dc2e00","text":"{\"gloss_range\":\"fused interrogative and consequential opening that turns the preceding diagnosis into a rhetorical challenge\",\"prose\":\"{{ar:أَفَ}} ({{tr:a-fa}}) does not let the question arrive as a detached new topic. Its hamza opens interrogation, while the bound {{tr:fāʾ}} makes the question a consequence of the preceding human diagnosis (100:6-8). The result is a compressed turn from declarative exposure to direct challenge: after the human has been described as ungrateful, self-witnessing, and intense in love of wealth, the wording abruptly asks whether he does not know. The opening sound can be heard as an arresting break, but the stronger payoff is structural: the ayah changes register by making the prior diagnosis demand an answer.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:أَفَ}} ({{tr:a-fa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:3:forward-divine-knowing-closure","source_type":"word_analysis","support_id":"sup_e622d28a1c6f1540d8f2","text":"{\"blocking_evidence\":null,\"headline\":\"human knowing before divine knowing\",\"reader_payoff\":\"The reader notices that the human knowledge-question frames the scene that later closes with divine full awareness (100:11).\",\"reason\":\"The supplied context window says the question continues through 100:10 and closes in 100:11, so the forward relation is valid but should not replace the local verb sense.\",\"representative_source_ids\":[\"QE-d9f8f64d\",\"QT-4d43ce3c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:3:human-referent-continuity","source_type":"word_analysis","support_id":"sup_e7d86cdafc483e62425a","text":"{\"blocking_evidence\":null,\"headline\":\"same human remains exposed\",\"reader_payoff\":\"The reader notices that the human described in 100:6-8 is the same one now interrogated about knowledge.\",\"reason\":\"The 3ms agreement and attachment evidence continue the generic human topic introduced in 100:6.\",\"representative_source_ids\":[\"QG-c5e96ed0\",\"QB-3a6e5645\",\"QB-3c191ad2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:5:variant-contrast","source_type":"word_analysis","support_id":"sup_eb05e3fc73b8814c41e3","text":"{\"blocking_evidence\":null,\"headline\":\"variant readings as contrast\",\"reader_payoff\":\"The reader notices what the standard reading does by contrast: it avoids an explicit actor and keeps quadriliteral upheaval stronger than a pure search reading.\",\"reason\":\"Variant readings may illuminate contrast, but QAC and attachment evidence identify the local canonical surface as passive perfect with {{ar:مَا}} ({{tr:mā}}) as subject.\",\"representative_source_ids\":[\"QG-9efac9a6\",\"QF-1cb9d2db\",\"QF-e1c50512\",\"QF-eff2825c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"100:9:7:2","source_type":"qac_morpheme","support_id":"sup_edab5bc9a880cfbf185e","text":"{\"lemma_ar\":\"قَبْر\",\"morph_features\":\"STEM|POS:N|LEM:qabor|ROOT:qbr|MP|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"100:9:7:2\",\"qac_word_ref\":\"100:9:7\",\"root_ar\":\"ق ب ر\",\"surface_ar\":\"قُبُورِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:7","source_type":"word_analysis","support_id":"sup_f9bb410a3d792b47c3e5","text":"{\"gloss_range\":\"preposition of containment that binds the unspecified contents to the grave-field\",\"prose\":\"{{ar:فِى}} ({{tr:fī}}) is the containment hinge of the phrase. It makes the ayah speak about what is in the graves, not simply about graves as external structures. That differs from the supplied 82:4 parallel, where the graves themselves are the focus; here the preposition shifts attention inward to the hidden contents that {{ar:بُعْثِرَ}} ({{tr:buʿthira}}) will expose. It also creates a nested concealment relation, things hidden inside graves that are themselves hidden, which makes the later exposure sharper. Syntactically, {{ar:فِى ٱلْقُبُورِ}} ({{tr:fī al-qubūr}}) completes the relative subject phrase governed by {{ar:مَا}} ({{tr:mā}}). In recitation, the liaison into the following noun reinforces the same payoff at the sound level: containment is heard as a continuous bond before it is overturned.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فِى}} ({{tr:fī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:9:1:audible-interruption","source_type":"word_analysis","support_id":"sup_fe14e1dc2fb4a484c9e7","text":"{\"blocking_evidence\":null,\"headline\":\"abrupt opening sound\",\"reader_payoff\":\"The reader notices that the initial interrogative onset helps the new question feel like an interruption of the prior declarative flow.\",\"reason\":\"The sound claim is modest and consistent with the particle's structural function, so it can survive as secondary recitational payoff.\",\"representative_source_ids\":[\"QP-2299bd1e\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"۞ أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ","ayah_ref":"100:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000130/B001","root_001040/B001","root_001195/B001"],"payload":{"activation_trace":[{"assigned_role":"Names the epistemic result whose timing the question challenges.","branch_id":"B001","branch_image_ar":"انكشاف الشيء للعارف","literal_contribution":"Knowing is the coming-clear of a thing to a knower.","mapped_root_id":"root_001040","root":"ع ل م","source_phrase_ar":"يَعْلَمُ","source_ref":"100:9"},{"assigned_role":"Supplies the disclosure event that changes access to the object.","branch_id":"B001","branch_image_ar":"قلب التراب وكشف المدفون","literal_contribution":"Earth is overturned and buried contents are uncovered.","mapped_root_id":"root_000130","root":"ب ع ث ر","source_phrase_ar":"بُعْثِرَ","source_ref":"100:9"},{"assigned_role":"Supplies the prior state of burial that the event reverses.","branch_id":"B001","branch_image_ar":"مواراة الميت في القبر","literal_contribution":"The dead have been placed out of sight in graves.","mapped_root_id":"root_001195","root":"ق ب ر","source_phrase_ar":"قُبُورِ","source_ref":"100:9"}],"changed_reading":{"after":"A challenge about an impending epistemic threshold: the one who can defer recognition now will confront disclosure when burial is physically reversed.","before":"A generic rhetorical question about whether someone knows that graves will open."},"confidence":"strong","focus_anchor":"يَعْلَمُ (ع ل م; root_001040/B001), بُعْثِرَ (ب ع ث ر; root_000130/B001), and قُبُورِ (ق ب ر; root_001195/B001).","mechanism":"The rhetorical أَفَلَا and temporal إِذَا place knowing at an event-threshold: earth is overturned, the buried are disclosed, and what was unavailable becomes clear to a knower. The packet supplies disclosure and burial; I infer that the event changes the knower's epistemic position.","model_id":"base_unveiling_threshold","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_unveiling_threshold","source_type":"hft","support_id":"sup_2ac542177bd28ea0dfdb","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"۞ أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ","ayah_ref":"100:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000130/B002","root_000130/B003","root_001040/B001","root_001195/B002"],"payload":{"activation_trace":[{"assigned_role":"Makes disclosure a loss of arrangement, not a neat opening.","branch_id":"B002","branch_image_ar":"تبديد المتاع وقلب بعضه على بعض","literal_contribution":"Stored belongings are dispersed and turned over upon one another.","mapped_root_id":"root_000130","root":"ب ع ث ر","source_phrase_ar":"بُعْثِرَ","source_ref":"100:9"},{"assigned_role":"Supplies the vertical and container-topology reversal.","branch_id":"B003","branch_image_ar":"هدم الحوض وقلب أسفله أعلاه","literal_contribution":"A containing basin is demolished and inverted.","mapped_root_id":"root_000130","root":"ب ع ث ر","source_phrase_ar":"بُعْثِرَ","source_ref":"100:9"},{"assigned_role":"Defines the enclosed below-state that is abolished.","branch_id":"B002","branch_image_ar":"غموض الشيء وتطامنه","literal_contribution":"The thing is hidden and sunk inward.","mapped_root_id":"root_001195","root":"ق ب ر","source_phrase_ar":"قُبُورِ","source_ref":"100:9"},{"assigned_role":"Turns spatial inversion into an epistemic consequence.","branch_id":"B001","branch_image_ar":"انكشاف الشيء للعارف","literal_contribution":"A thing becomes clear to a knower.","mapped_root_id":"root_001040","root":"ع ل م","source_phrase_ar":"يَعْلَمُ","source_ref":"100:9"}],"changed_reading":{"after":"The entire architecture of concealment fails: below becomes above, enclosed contents lose their ordering, and knowledge arrives through that catastrophic topological reversal.","before":"The graves are opened and their occupants simply come out."},"confidence":"medium","focus_anchor":"بُعْثِرَ (ب ع ث ر; root_000130/B002 and root_000130/B003), قُبُورِ (ق ب ر; root_001195/B002), and يَعْلَمُ (ع ل م; root_001040/B001).","mechanism":"The graves are not only locations but hidden, inward-sunk enclosures. بُعْثِرَ contributes both disordered scattering and the geometry of a basin whose bottom is made its top. I infer that knowing follows a collapse of the distinctions inside/outside and below/above.","model_id":"base_container_reversal","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_container_reversal","source_type":"hft","support_id":"sup_8be49e51a89e2d628b74","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"۞ أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ","ayah_ref":"100:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000130/B002","root_001040/B002","root_001195/B002"],"payload":{"activation_trace":[{"assigned_role":"Models knowledge as identification by exposed evidence.","branch_id":"B002","branch_image_ar":"أثر يميز الشيء ويهدي إليه","literal_contribution":"A distinguishing trace marks a thing and guides toward it.","mapped_root_id":"root_001040","root":"ع ل م","source_phrase_ar":"يَعْلَمُ","source_ref":"100:9"},{"assigned_role":"Creates the evidentiary problem that trace-reading must solve.","branch_id":"B002","branch_image_ar":"تبديد المتاع وقلب بعضه على بعض","literal_contribution":"Contents are dispersed into disorder.","mapped_root_id":"root_000130","root":"ب ع ث ر","source_phrase_ar":"بُعْثِرَ","source_ref":"100:9"},{"assigned_role":"Makes the recovered signs signs of a previously inaccessible interior.","branch_id":"B002","branch_image_ar":"غموض الشيء وتطامنه","literal_contribution":"The object had been hidden and inwardly sunk.","mapped_root_id":"root_001195","root":"ق ب ر","source_phrase_ar":"قُبُورِ","source_ref":"100:9"}],"changed_reading":{"after":"Knowing may require identifying and reconstructing what upheaval has disordered from the marks by which the hidden is made legible.","before":"Knowing means directly seeing what was buried once it is exposed."},"confidence":"medium","focus_anchor":"يَعْلَمُ (ع ل م; root_001040/B002), بُعْثِرَ (ب ع ث ر; root_000130/B002), and قُبُورِ (ق ب ر; root_001195/B002).","mechanism":"Scattering can reduce immediate order even while hidden contents surface. The distinguishing-mark branch of ع ل م allows knowing to be reconstructive: identities or histories are followed through signs generated or exposed by disturbance. This does not replace ordinary knowing; it specifies one way disclosure becomes legible.","model_id":"base_trace_identification","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_trace_identification","source_type":"hft","support_id":"sup_d11e43af5856b12e3d7e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"۞ أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ","ayah_ref":"100:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000130/B003","root_001040/B005","root_001195/B002"],"payload":{"activation_trace":[{"assigned_role":"Supplies a deliberately branch-distant model of pooled contents.","branch_id":"B005","branch_image_ar":"ماء كثير مجتمع في عيلم","literal_contribution":"A large body of water is gathered in a containing place.","mapped_root_id":"root_001040","root":"ع ل م","source_phrase_ar":"يَعْلَمُ","source_ref":"100:9"},{"assigned_role":"Releases the pooled contents by container failure.","branch_id":"B003","branch_image_ar":"هدم الحوض وقلب أسفله أعلاه","literal_contribution":"A basin is demolished and its bottom made its top.","mapped_root_id":"root_000130","root":"ب ع ث ر","source_phrase_ar":"بُعْثِرَ","source_ref":"100:9"},{"assigned_role":"Makes graves materially comparable to recessed containers.","branch_id":"B002","branch_image_ar":"غموض الشيء وتطامنه","literal_contribution":"The contents occupy a hidden, inward-sunk state.","mapped_root_id":"root_001195","root":"ق ب ر","source_phrase_ar":"قُبُورِ","source_ref":"100:9"}],"changed_reading":{"after":"The burial system fails like an inverted basin: recessed containers turn over and their pooled contents pour into exposure, so knowing follows irreversible loss of enclosure.","before":"Each grave opens as a lid is removed."},"confidence":"exploratory","focus_anchor":"The inward-sunk قُبُورِ (root_001195/B002) and inverted-container بُعْثِرَ (root_000130/B003) remain primary; يَعْلَمُ (root_001040/B005) contributes only the gathered-fluid analogy.","outlier_id":"outlier_fluid_container_failure","rendering_caution":"Do not gloss يَعْلَمُ as water or claim that graves are literally basins; render this only as a contained material analogy activated by root_001040/B005 and root_000130/B003.","why_still_valid":"All three images attach to exact focus roots: يَعْلَمُ (root_001040/B005), بُعْثِرَ (root_000130/B003), and قُبُورِ (root_001195/B002). The reading changes the geometry of disclosure without replacing the ordinary verbal sense of knowing.","why_surprising":"It lets the form-distant gathered-water branch of ع ل م interact with the basin-inversion branch of ب ع ث ر, treating the focus as a material containment experiment rather than only an exhumation scene."},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:outlier_fluid_container_failure","source_type":"hft","support_id":"sup_1da28a5555193d9c8027","trust":"legacy_unbound"}]}
</lane_packet_json>
